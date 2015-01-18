#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Script to extract the strings from message resource files for
# Event Log sources.
#
# Copyright (c) 2013-2015, Joachim Metz <joachim.metz@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
import argparse
import logging
import os
import re
import stat
import sys

import dfvfs
import pyexe
import pyregf
import pywrc
import sqlite3

from dfvfs.lib import definitions as dfvfs_definitions
from dfvfs.lib import errors as dfvfs_errors
from dfvfs.helpers import source_scanner
from dfvfs.helpers import windows_path_resolver
from dfvfs.resolver import resolver
from dfvfs.volume import tsk_volume_system


if dfvfs.__version__ < '20140727':
  raise ImportWarning('shellfolder.py requires dfvfs 20140727 or later.')

if pyexe.get_version() < '20131229':
  raise ImportWarning('extract.py requires pyexe 20131229 or later.')

if pyregf.get_version() < '20130716':
  raise ImportWarning('extract.py requires pyregf 20130716 or later.')

if pywrc.get_version() < '20140128':
  raise ImportWarning('extract.py requires pywrc 20140128 or later.')


LANGUAGES = {
    0x0001: ['ar', 'Arabic'],
    0x0002: ['bg', 'Bulgarian'],
    0x0003: ['ca', 'Catalan'],
    0x0004: ['zh-Hans', 'Chinese, Han (Simplified variant)'],
    0x0005: ['cs', 'Czech'],
    0x0006: ['da', 'Danish'],
    0x0007: ['de', 'German'],
    0x0008: ['el', 'Modern Greek (1453 and later)'],
    0x0009: ['en', 'English'],
    0x000a: ['es', 'Spanish'],
    0x000b: ['fi', 'Finnish'],
    0x000c: ['fr', 'French'],
    0x000d: ['he', 'Hebrew'],
    0x000e: ['hu', 'Hungarian'],
    0x000f: ['is', 'Icelandic'],
    0x0010: ['it', 'Italian'],
    0x0011: ['ja', 'Japanese'],
    0x0012: ['ko', 'Korean'],
    0x0013: ['nl', 'Dutch'],
    0x0014: ['no', 'Norwegian'],
    0x0015: ['pl', 'Polish'],
    0x0016: ['pt', 'Portuguese'],
    0x0017: ['rm', 'Romansh'],
    0x0018: ['ro', 'Romanian'],
    0x0019: ['ru', 'Russian'],
    0x001a: ['hr', 'Croatian'],
    0x001b: ['sk', 'Slovak'],
    0x001c: ['sq', 'Albanian'],
    0x001d: ['sv', 'Swedish'],
    0x001e: ['th', 'Thai'],
    0x001f: ['tr', 'Turkish'],
    0x0020: ['ur', 'Urdu'],
    0x0021: ['id', 'Indonesian'],
    0x0022: ['uk', 'Ukrainian'],
    0x0023: ['be', 'Belarusian'],
    0x0024: ['sl', 'Slovenian'],
    0x0025: ['et', 'Estonian'],
    0x0026: ['lv', 'Latvian'],
    0x0027: ['lt', 'Lithuanian'],
    0x0028: ['tg', 'Tajik'],
    0x0029: ['fa', 'Persian'],
    0x002a: ['vi', 'Vietnamese'],
    0x002b: ['hy', 'Armenian'],
    0x002c: ['az', 'Azerbaijani'],
    0x002d: ['eu', 'Basque'],
    0x002e: ['hsb', 'Upper Sorbian'],
    0x002f: ['mk', 'Macedonian'],
    0x0032: ['tn', 'Tswana'],
    0x0034: ['xh', 'Xhosa'],
    0x0035: ['zu', 'Zulu'],
    0x0036: ['af', 'Afrikaans'],
    0x0037: ['ka', 'Georgian'],
    0x0038: ['fo', 'Faroese'],
    0x0039: ['hi', 'Hindi'],
    0x003a: ['mt', 'Maltese'],
    0x003b: ['se', 'Northern Sami'],
    0x003c: ['ga', 'Irish'],
    0x003e: ['ms', 'Malay (macrolanguage)'],
    0x003f: ['kk', 'Kazakh'],
    0x0040: ['ky', 'Kirghiz'],
    0x0041: ['sw', 'Swahili (macrolanguage)'],
    0x0042: ['tk', 'Turkmen'],
    0x0043: ['uz', 'Uzbek'],
    0x0044: ['tt', 'Tatar'],
    0x0045: ['bn', 'Bengali'],
    0x0046: ['pa', 'Panjabi'],
    0x0047: ['gu', 'Gujarati'],
    0x0048: ['or', 'Oriya'],
    0x0049: ['ta', 'Tamil'],
    0x004a: ['te', 'Telugu'],
    0x004b: ['kn', 'Kannada'],
    0x004c: ['ml', 'Malayalam'],
    0x004d: ['as', 'Assamese'],
    0x004e: ['mr', 'Marathi'],
    0x004f: ['sa', 'Sanskrit'],
    0x0050: ['mn', 'Mongolian'],
    0x0051: ['bo', 'Tibetan'],
    0x0052: ['cy', 'Welsh'],
    0x0053: ['km', 'Central Khmer'],
    0x0054: ['lo', 'Lao'],
    0x0056: ['gl', 'Galician'],
    0x0057: ['kok', 'Konkani (macrolanguage)'],
    0x005a: ['syr', 'Syriac'],
    0x005b: ['si', 'Sinhala'],
    0x005d: ['iu', 'Inuktitut'],
    0x005e: ['am', 'Amharic'],
    0x005f: ['tzm', 'Central Atlas Tamazight'],
    0x0061: ['ne', 'Nepali'],
    0x0062: ['fy', 'Western Frisian'],
    0x0063: ['ps', 'Pushto'],
    0x0064: ['fil', 'Filipino'],
    0x0065: ['dv', 'Dhivehi'],
    0x0068: ['ha', 'Hausa'],
    0x006a: ['yo', 'Yoruba'],
    0x006b: ['quz', 'Cusco Quechua'],
    0x006c: ['nso', 'Pedi'],
    0x006d: ['ba', 'Bashkir'],
    0x006e: ['lb', 'Luxembourgish'],
    0x006f: ['kl', 'Kalaallisut'],
    0x0070: ['ig', 'Igbo'],
    0x0078: ['ii', 'Sichuan Yi'],
    0x007a: ['arn', 'Mapudungun'],
    0x007c: ['moh', 'Mohawk'],
    0x007e: ['br', 'Breton'],
    0x0080: ['ug', 'Uighur'],
    0x0081: ['mi', 'Maori'],
    0x0082: ['oc', 'Occitan (post 1500)'],
    0x0083: ['co', 'Corsican'],
    0x0084: ['gsw', 'Swiss German'],
    0x0085: ['sah', 'Yakut'],
    0x0086: ['qut', 'Guatemala'],
    0x0087: ['rw', 'Kinyarwanda'],
    0x0088: ['wo', 'Wolof'],
    0x008c: ['prs', 'Dari'],
    0x0091: ['gd', 'Scottish Gaelic'],
    0x0401: ['ar-SA', 'Arabic, Saudi Arabia'],
    0x0402: ['bg-BG', 'Bulgarian, Bulgaria'],
    0x0403: ['ca-ES', 'Catalan, Spain'],
    0x0404: ['zh-TW', 'Chinese, Taiwan, Province of China'],
    0x0405: ['cs-CZ', 'Czech, Czech Republic'],
    0x0406: ['da-DK', 'Danish, Denmark'],
    0x0407: ['de-DE', 'German, Germany'],
    0x0408: ['el-GR', 'Modern Greek (1453-), Greece'],
    0x0409: ['en-US', 'English, United States'],
    0x040a: ['es-ES_tradnl', 'Spanish'],
    0x040b: ['fi-FI', 'Finnish, Finland'],
    0x040c: ['fr-FR', 'French, France'],
    0x040d: ['he-IL', 'Hebrew, Israel'],
    0x040e: ['hu-HU', 'Hungarian, Hungary'],
    0x040f: ['is-IS', 'Icelandic, Iceland'],
    0x0410: ['it-IT', 'Italian, Italy'],
    0x0411: ['ja-JP', 'Japanese, Japan'],
    0x0412: ['ko-KR', 'Korean, Republic of Korea'],
    0x0413: ['nl-NL', 'Dutch, Netherlands'],
    0x0414: ['nb-NO', 'Norwegian Bokmål, Norway'],
    0x0415: ['pl-PL', 'Polish, Poland'],
    0x0416: ['pt-BR', 'Portuguese, Brazil'],
    0x0417: ['rm-CH', 'Romansh, Switzerland'],
    0x0418: ['ro-RO', 'Romanian, Romania'],
    0x0419: ['ru-RU', 'Russian, Russian Federation'],
    0x041a: ['hr-HR', 'Croatian, Croatia'],
    0x041b: ['sk-SK', 'Slovak, Slovakia'],
    0x041c: ['sq-AL', 'Albanian, Albania'],
    0x041d: ['sv-SE', 'Swedish, Sweden'],
    0x041e: ['th-TH', 'Thai, Thailand'],
    0x041f: ['tr-TR', 'Turkish, Turkey'],
    0x0420: ['ur-PK', 'Urdu, Pakistan'],
    0x0421: ['id-ID', 'Indonesian, Indonesia'],
    0x0422: ['uk-UA', 'Ukrainian, Ukraine'],
    0x0423: ['be-BY', 'Belarusian, Belarus'],
    0x0424: ['sl-SI', 'Slovenian, Slovenia'],
    0x0425: ['et-EE', 'Estonian, Estonia'],
    0x0426: ['lv-LV', 'Latvian, Latvia'],
    0x0427: ['lt-LT', 'Lithuanian, Lithuania'],
    0x0428: ['tg-Cyrl-TJ', 'Tajik, Cyrillic, Tajikistan'],
    0x0429: ['fa-IR', 'Persian, Islamic Republic of Iran'],
    0x042a: ['vi-VN', 'Vietnamese, Viet Nam'],
    0x042b: ['hy-AM', 'Armenian, Armenia'],
    0x042c: ['az-Latn-AZ', 'Azerbaijani, Latin, Azerbaijan'],
    0x042d: ['eu-ES', 'Basque, Spain'],
    0x042e: ['wen-DE', 'Sorbian languages, Germany'],
    0x042f: ['mk-MK', 'Macedonian, The Former Yugoslav Republic of Macedonia'],
    0x0430: ['st-ZA', 'Southern Sotho, South Africa'],
    0x0431: ['ts-ZA', 'Tsonga, South Africa'],
    0x0432: ['tn-ZA', 'Tswana, South Africa'],
    0x0433: ['ven-ZA', 'South Africa'],
    0x0434: ['xh-ZA', 'Xhosa, South Africa'],
    0x0435: ['zu-ZA', 'Zulu, South Africa'],
    0x0436: ['af-ZA', 'Afrikaans, South Africa'],
    0x0437: ['ka-GE', 'Georgian, Georgia'],
    0x0438: ['fo-FO', 'Faroese, Faroe Islands'],
    0x0439: ['hi-IN', 'Hindi, India'],
    0x043a: ['mt-MT', 'Maltese, Malta'],
    0x043b: ['se-NO', 'Northern Sami, Norway'],
    0x043e: ['ms-MY', 'Malay (macrolanguage), Malaysia'],
    0x043f: ['kk-KZ', 'Kazakh, Kazakhstan'],
    0x0440: ['ky-KG', 'Kirghiz, Kyrgyzstan'],
    0x0441: ['sw-KE', 'Swahili (macrolanguage), Kenya'],
    0x0442: ['tk-TM', 'Turkmen, Turkmenistan'],
    0x0443: ['uz-Latn-UZ', 'Uzbek, Latin, Uzbekistan'],
    0x0444: ['tt-RU', 'Tatar, Russian Federation'],
    0x0445: ['bn-IN', 'Bengali, India'],
    0x0446: ['pa-IN', 'Panjabi, India'],
    0x0447: ['gu-IN', 'Gujarati, India'],
    0x0448: ['or-IN', 'Oriya, India'],
    0x0449: ['ta-IN', 'Tamil, India'],
    0x044a: ['te-IN', 'Telugu, India'],
    0x044b: ['kn-IN', 'Kannada, India'],
    0x044c: ['ml-IN', 'Malayalam, India'],
    0x044d: ['as-IN', 'Assamese, India'],
    0x044e: ['mr-IN', 'Marathi, India'],
    0x044f: ['sa-IN', 'Sanskrit, India'],
    0x0450: ['mn-MN', 'Mongolian, Mongolia'],
    0x0451: ['bo-CN', 'Tibetan, China'],
    0x0452: ['cy-GB', 'Welsh, United Kingdom'],
    0x0453: ['km-KH', 'Central Khmer, Cambodia'],
    0x0454: ['lo-LA', 'Lao, Lao People\'s Democratic Republic'],
    0x0455: ['my-MM', 'Burmese, Myanmar'],
    0x0456: ['gl-ES', 'Galician, Spain'],
    0x0457: ['kok-IN', 'Konkani (macrolanguage), India'],
    0x0458: ['mni', 'Manipuri'],
    0x0459: ['sd-IN', 'Sindhi, India'],
    0x045a: ['syr-SY', 'Syriac, Syrian Arab Republic'],
    0x045b: ['si-LK', 'Sinhala, Sri Lanka'],
    0x045c: ['chr-US', 'Cherokee, United States'],
    0x045d: ['iu-Cans-CA', 'Inuktitut, Unified Canadian Aboriginal Syllabics, Canada'],
    0x045e: ['am-ET', 'Amharic, Ethiopia'],
    0x045f: ['tmz', 'Tamanaku'],
    0x0461: ['ne-NP', 'Nepali, Nepal'],
    0x0462: ['fy-NL', 'Western Frisian, Netherlands'],
    0x0463: ['ps-AF', 'Pushto, Afghanistan'],
    0x0464: ['fil-PH', 'Filipino, Philippines'],
    0x0465: ['dv-MV', 'Dhivehi, Maldives'],
    0x0466: ['bin-NG', 'Bini, Nigeria'],
    0x0467: ['fuv-NG', 'Nigerian Fulfulde, Nigeria'],
    0x0468: ['ha-Latn-NG', 'Hausa, Latin, Nigeria'],
    0x0469: ['ibb-NG', 'Ibibio, Nigeria'],
    0x046a: ['yo-NG', 'Yoruba, Nigeria'],
    0x046b: ['quz-BO', 'Cusco Quechua, Bolivia'],
    0x046c: ['nso-ZA', 'Pedi, South Africa'],
    0x046d: ['ba-RU', 'Bashkir, Russian Federation'],
    0x046e: ['lb-LU', 'Luxembourgish, Luxembourg'],
    0x046f: ['kl-GL', 'Kalaallisut, Greenland'],
    0x0470: ['ig-NG', 'Igbo, Nigeria'],
    0x0471: ['kr-NG', 'Kanuri, Nigeria'],
    0x0472: ['gaz-ET', 'West Central Oromo, Ethiopia'],
    0x0473: ['ti-ER', 'Tigrinya, Eritrea'],
    0x0474: ['gn-PY', 'Guarani, Paraguay'],
    0x0475: ['haw-US', 'Hawaiian, United States'],
    0x0477: ['so-SO', 'Somali, Somalia'],
    0x0478: ['ii-CN', 'Sichuan Yi, China'],
    0x0479: ['pap-AN', 'Papiamento, Netherlands Antilles'],
    0x047a: ['arn-CL', 'Mapudungun, Chile'],
    0x047c: ['moh-CA', 'Mohawk, Canada'],
    0x047e: ['br-FR', 'Breton, France'],
    0x0480: ['ug-CN', 'Uighur, China'],
    0x0481: ['mi-NZ', 'Maori, New Zealand'],
    0x0482: ['oc-FR', 'Occitan (post 1500), France'],
    0x0483: ['co-FR', 'Corsican, France'],
    0x0484: ['gsw-FR', 'Swiss German, France'],
    0x0485: ['sah-RU', 'Yakut, Russian Federation'],
    0x0486: ['qut-GT', 'Guatemala'],
    0x0487: ['rw-RW', 'Kinyarwanda, Rwanda'],
    0x0488: ['wo-SN', 'Wolof, Senegal'],
    0x048c: ['prs-AF', 'Dari, Afghanistan'],
    0x048d: ['plt-MG', 'Plateau Malagasy, Madagascar'],
    0x0491: ['gd-GB', 'Scottish Gaelic, United Kingdom'],
    0x0801: ['ar-IQ', 'Arabic, Iraq'],
    0x0804: ['zh-CN', 'Chinese, China'],
    0x0807: ['de-CH', 'German, Switzerland'],
    0x0809: ['en-GB', 'English, United Kingdom'],
    0x080a: ['es-MX', 'Spanish, Mexico'],
    0x080c: ['fr-BE', 'French, Belgium'],
    0x0810: ['it-CH', 'Italian, Switzerland'],
    0x0813: ['nl-BE', 'Dutch, Belgium'],
    0x0814: ['nn-NO', 'Norwegian Nynorsk, Norway'],
    0x0816: ['pt-PT', 'Portuguese, Portugal'],
    0x0818: ['ro-MO', 'Romanian, Macao'],
    0x0819: ['ru-MO', 'Russian, Macao'],
    0x081a: ['sr-Latn-CS', 'Serbian, Latin, Serbia and Montenegro'],
    0x081d: ['sv-FI', 'Swedish, Finland'],
    0x0820: ['ur-IN', 'Urdu, India'],
    0x082c: ['az-Cyrl-AZ', 'Azerbaijani, Cyrillic, Azerbaijan'],
    0x082e: ['dsb-DE', 'Lower Sorbian, Germany'],
    0x083b: ['se-SE', 'Northern Sami, Sweden'],
    0x083c: ['ga-IE', 'Irish, Ireland'],
    0x083e: ['ms-BN', 'Malay (macrolanguage), Brunei Darussalam'],
    0x0843: ['uz-Cyrl-UZ', 'Uzbek, Cyrillic, Uzbekistan'],
    0x0845: ['bn-BD', 'Bengali, Bangladesh'],
    0x0846: ['pa-PK', 'Panjabi, Pakistan'],
    0x0850: ['mn-Mong-CN', 'Mongolian, Mongolian, China'],
    0x0851: ['bo-BT', 'Tibetan, Bhutan'],
    0x0859: ['sd-PK', 'Sindhi, Pakistan'],
    0x085d: ['iu-Latn-CA', 'Inuktitut, Latin, Canada'],
    0x085f: ['tzm-Latn-DZ', 'Central Atlas Tamazight, Latin, Algeria'],
    0x0861: ['ne-IN', 'Nepali, India'],
    0x086b: ['quz-EC', 'Cusco Quechua, Ecuador'],
    0x0873: ['ti-ET', 'Tigrinya, Ethiopia'],
    0x0c01: ['ar-EG', 'Arabic, Egypt'],
    0x0c04: ['zh-HK', 'Chinese, Hong Kong'],
    0x0c07: ['de-AT', 'German, Austria'],
    0x0c09: ['en-AU', 'English, Australia'],
    0x0c0a: ['es-ES', 'Spanish, Spain'],
    0x0c0c: ['fr-CA', 'French, Canada'],
    0x0c1a: ['sr-Cyrl-CS', 'Serbian, Cyrillic, Serbia and Montenegro'],
    0x0c3b: ['se-FI', 'Northern Sami, Finland'],
    0x0c5f: ['tmz-MA', 'Tamanaku, Morocco'],
    0x0c6b: ['quz-PE', 'Cusco Quechua, Peru'],
    0x1001: ['ar-LY', 'Arabic, Libyan Arab Jamahiriya'],
    0x1004: ['zh-SG', 'Chinese, Singapore'],
    0x1007: ['de-LU', 'German, Luxembourg'],
    0x1009: ['en-CA', 'English, Canada'],
    0x100a: ['es-GT', 'Spanish, Guatemala'],
    0x100c: ['fr-CH', 'French, Switzerland'],
    0x101a: ['hr-BA', 'Croatian, Bosnia and Herzegovina'],
    0x103b: ['smj-NO', 'Lule Sami, Norway'],
    0x1401: ['ar-DZ', 'Arabic, Algeria'],
    0x1404: ['zh-MO', 'Chinese, Macao'],
    0x1407: ['de-LI', 'German, Liechtenstein'],
    0x1409: ['en-NZ', 'English, New Zealand'],
    0x140a: ['es-CR', 'Spanish, Costa Rica'],
    0x140c: ['fr-LU', 'French, Luxembourg'],
    0x141a: ['bs-Latn-BA', 'Bosnian, Latin, Bosnia and Herzegovina'],
    0x143b: ['smj-SE', 'Lule Sami, Sweden'],
    0x1801: ['ar-MA', 'Arabic, Morocco'],
    0x1809: ['en-IE', 'English, Ireland'],
    0x180a: ['es-PA', 'Spanish, Panama'],
    0x180c: ['fr-MC', 'French, Monaco'],
    0x181a: ['sr-Latn-BA', 'Serbian, Latin, Bosnia and Herzegovina'],
    0x183b: ['sma-NO', 'Southern Sami, Norway'],
    0x1c01: ['ar-TN', 'Arabic, Tunisia'],
    0x1c09: ['en-ZA', 'English, South Africa'],
    0x1c0a: ['es-DO', 'Spanish, Dominican Republic'],
    0x1c0c: ['fr-West', 'French'],
    0x1c1a: ['sr-Cyrl-BA', 'Serbian, Cyrillic, Bosnia and Herzegovina'],
    0x1c3b: ['sma-SE', 'Southern Sami, Sweden'],
    0x2001: ['ar-OM', 'Arabic, Oman'],
    0x2009: ['en-JM', 'English, Jamaica'],
    0x200a: ['es-VE', 'Spanish, Venezuela'],
    0x200c: ['fr-RE', 'French, Réunion'],
    0x201a: ['bs-Cyrl-BA', 'Bosnian, Cyrillic, Bosnia and Herzegovina'],
    0x203b: ['sms-FI', 'Skolt Sami, Finland'],
    0x2401: ['ar-YE', 'Arabic, Yemen'],
    0x2409: ['en-CB', 'English'],
    0x240a: ['es-CO', 'Spanish, Colombia'],
    0x240c: ['fr-CG', 'French, Congo'],
    0x241a: ['sr-Latn-RS', 'Serbian, Latin, Serbia'],
    0x243b: ['smn-FI', 'Inari Sami, Finland'],
    0x2801: ['ar-SY', 'Arabic, Syrian Arab Republic'],
    0x2809: ['en-BZ', 'English, Belize'],
    0x280a: ['es-PE', 'Spanish, Peru'],
    0x280c: ['fr-SN', 'French, Senegal'],
    0x281a: ['sr-Cyrl-RS', 'Serbian, Cyrillic, Serbia'],
    0x2c01: ['ar-JO', 'Arabic, Jordan'],
    0x2c09: ['en-TT', 'English, Trinidad and Tobago'],
    0x2c0a: ['es-AR', 'Spanish, Argentina'],
    0x2c0c: ['fr-CM', 'French, Cameroon'],
    0x2c1a: ['sr-Latn-ME', 'Serbian, Latin, Montenegro'],
    0x3001: ['ar-LB', 'Arabic, Lebanon'],
    0x3009: ['en-ZW', 'English, Zimbabwe'],
    0x300a: ['es-EC', 'Spanish, Ecuador'],
    0x300c: ['fr-CI', 'French, Côte d\'Ivoire'],
    0x301a: ['sr-Cyrl-ME', 'Serbian, Cyrillic, Montenegro'],
    0x3401: ['ar-KW', 'Arabic, Kuwait'],
    0x3409: ['en-PH', 'English, Philippines'],
    0x340a: ['es-CL', 'Spanish, Chile'],
    0x340c: ['fr-ML', 'French, Mali'],
    0x3801: ['ar-AE', 'Arabic, United Arab Emirates'],
    0x3809: ['en-ID', 'English, Indonesia'],
    0x380a: ['es-UY', 'Spanish, Uruguay'],
    0x380c: ['fr-MA', 'French, Morocco'],
    0x3c01: ['ar-BH', 'Arabic, Bahrain'],
    0x3c09: ['en-HK', 'English, Hong Kong'],
    0x3c0a: ['es-PY', 'Spanish, Paraguay'],
    0x3c0c: ['fr-HT', 'French, Haiti'],
    0x4001: ['ar-QA', 'Arabic, Qatar'],
    0x4009: ['en-IN', 'English, India'],
    0x400a: ['es-BO', 'Spanish, Bolivia'],
    0x4409: ['en-MY', 'English, Malaysia'],
    0x440a: ['es-SV', 'Spanish, El Salvador'],
    0x4809: ['en-SG', 'English, Singapore'],
    0x480a: ['es-HN', 'Spanish, Honduras'],
    0x4c0a: ['es-NI', 'Spanish, Nicaragua'],
    0x500a: ['es-PR', 'Spanish, Puerto Rico'],
    0x540a: ['es-US', 'Spanish, United States'],
    0x641a: ['bs-Cyrl', 'Bosnian, Cyrillic'],
    0x681a: ['bs-Latn', 'Bosnian, Latin'],
    0x6c1a: ['sr-Cyrl', 'Serbian, Cyrillic'],
    0x701a: ['sr-Latn', 'Serbian, Latin'],
    0x703b: ['smn', 'Inari Sami'],
    0x742c: ['az-Cyrl', 'Azerbaijani, Cyrillic'],
    0x743b: ['sms', 'Skolt Sami'],
    0x7804: ['zh', 'Chinese'],
    0x7814: ['nn', 'Norwegian Nynorsk'],
    0x781a: ['bs', 'Bosnian'],
    0x782c: ['az-Latn', 'Azerbaijani, Latin'],
    0x783b: ['sma', 'Southern Sami'],
    0x7843: ['uz-Cyrl', 'Uzbek, Cyrillic'],
    0x7850: ['mn-Cyrl', 'Mongolian, Cyrillic'],
    0x785d: ['iu-Cans', 'Inuktitut, Unified Canadian Aboriginal Syllabics'],
    0x7c04: ['zh-Hant', 'Chinese, Han (Traditional variant)'],
    0x7c14: ['nb', 'Norwegian Bokmål'],
    0x7c1a: ['sr', 'Serbian'],
    0x7c28: ['tg-Cyrl', 'Tajik, Cyrillic'],
    0x7c2e: ['dsb', 'Lower Sorbian'],
    0x7c3b: ['smj', 'Lule Sami'],
    0x7c43: ['uz-Latn', 'Uzbek, Latin'],
    0x7c50: ['mn-Mong', 'Mongolian, Mongolian'],
    0x7c5d: ['iu-Latn', 'Inuktitut, Latin'],
    0x7c5f: ['tzm-Latn', 'Central Atlas Tamazight, Latin'],
    0x7c68: ['ha-Latn', 'Hausa, Latin'],
}


class CollectorError(Exception):
  """Class that defines collector errors."""


class WindowsVolumeCollector(object):
  """Class that defines a Windows volume collector."""

  _WINDOWS_DIRECTORIES = frozenset([
      u'C:\\Windows',
      u'C:\\WINNT',
      u'C:\\WTSRV',
      u'C:\\WINNT35',
  ])

  def __init__(self):
    """Initializes the Windows volume collector object."""
    super(WindowsVolumeCollector, self).__init__()
    self._file_system = None
    self._path_resolver = None
    self._scanner = source_scanner.SourceScanner()
    self._windows_directory = None

  def _ScanFileSystem(self, path_resolver):
    """Scans a file system for the Windows volume.

    Args:
      path_resolver: the path resolver (instance of dfvfs.WindowsPathResolver).

    Returns:
      True if the Windows directory was found, false otherwise.

    """
    result = False

    for windows_path in self._WINDOWS_DIRECTORIES:
      windows_path_spec = path_resolver.ResolvePath(windows_path)

      result = windows_path_spec is not None
      if result:
        self._windows_directory = windows_path
        break

    return result

  def _ScanTSKPartionVolumeSystemPathSpec(self, scan_context):
    """Scans a path specification for the Windows volume.

    Args:
      scan_context: the scan context (instance of dfvfs.ScanContext).

    Returns:
      The volume scan node (instance of dfvfs.SourceScanNode) of the volume
      that contains the Windows directory or None.

    Raises:
      CollectorError: if the scan context is invalid.
    """
    if (not scan_context or not scan_context.last_scan_node or
        not scan_context.last_scan_node.path_spec):
      raise CollectorError(u'Invalid scan context.')

    volume_system = tsk_volume_system.TSKVolumeSystem()
    volume_system.Open(scan_context.last_scan_node.path_spec)

    volume_identifiers = self._scanner.GetVolumeIdentifiers(volume_system)
    if not volume_identifiers:
      return

    volume_scan_node = None
    result = False

    for volume_identifier in volume_identifiers:
      volume_location = u'/{0:s}'.format(volume_identifier)
      volume_scan_node = scan_context.last_scan_node.GetSubNodeByLocation(
          volume_location)
      volume_path_spec = getattr(volume_scan_node, 'path_spec', None)

      # The leaf scan node contains the actual file system.
      file_system_scan_node = volume_scan_node.GetSubNodeByLocation(u'/')
      while file_system_scan_node.sub_nodes:
        file_system_scan_node = file_system_scan_node.GetSubNodeByLocation(u'/')

      file_system_path_spec = getattr(file_system_scan_node, 'path_spec', None)
      file_system = resolver.Resolver.OpenFileSystem(file_system_path_spec)

      if file_system is None:
        continue

      path_resolver = windows_path_resolver.WindowsPathResolver(
          file_system, volume_path_spec)

      result = self._ScanFileSystem(path_resolver)
      if result:
        break

    if not result:
      return

    return volume_scan_node

  def GetWindowsVolumePathSpec(self, source_path):
    """Determines the file system path specification of the Windows volume.

    Args:
      source_path: the source path.

    Returns:
      True if successful or False otherwise.

    Raises:
      CollectorError: if the source path does not exists, or if the source path
                      is not a file or directory, or if the format of or within
                      the source file is not supported.
    """
    # Note that os.path.exists() does not support Windows device paths.
    if (not source_path.startswith('\\\\.\\') and
        not os.path.exists(source_path)):
      raise CollectorError(
          u'No such device, file or directory: {0:s}.'.format(source_path))

    scan_context = source_scanner.SourceScannerContext()
    scan_path_spec = None

    scan_context.OpenSourcePath(source_path)

    while True:
      last_scan_node = scan_context.last_scan_node
      try:
        scan_context = self._scanner.Scan(
            scan_context, scan_path_spec=scan_path_spec)
      except dfvfs_errors.BackEndError as exception:
        raise CollectorError(
            u'Unable to scan source, with error: {0:s}'.format(exception))

      # The source is a directory or file.
      if scan_context.source_type in [
          scan_context.SOURCE_TYPE_DIRECTORY, scan_context.SOURCE_TYPE_FILE]:
        break

      if (not scan_context.last_scan_node or
          scan_context.last_scan_node == last_scan_node):
        raise CollectorError(
            u'No supported file system found in source: {0:s}.'.format(
                self._source_path))

      # The source scanner found a file system.
      if scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_TSK]:
        break

      # The source scanner found a BitLocker encrypted volume and we need
      # a credential to unlock the volume.
      if scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_BDE]:
        # TODO: ask for password.
        raise CollectorError(
            u'BitLocker encrypted volume not yet supported.')

      # The source scanner found a partition table and we need to determine
      # which partition contains the Windows directory.
      elif scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_TSK_PARTITION]:
        scan_node = self._ScanTSKPartionVolumeSystemPathSpec(scan_context)
        if not scan_node:
          return False
        scan_context.last_scan_node = scan_node

      # The source scanner found Volume Shadow Snapshot which is ignored.
      elif scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_VSHADOW]:
        # Get the scan node of the current volume.
        scan_node = scan_context.last_scan_node.GetSubNodeByLocation(u'/')
        scan_context.last_scan_node = scan_node
        break

      else:
        raise CollectorError(
            u'Unsupported volume system found in source: {0:s}.'.format(
                self._source_path))

    # TODO: add single file support.
    if scan_context.source_type == scan_context.SOURCE_TYPE_FILE:
      raise CollectorError(
          u'Unsupported source: {0:s}.'.format(source_path))

    if scan_context.source_type != scan_context.SOURCE_TYPE_DIRECTORY:
      if not scan_context.last_scan_node.type_indicator in [
          dfvfs_definitions.TYPE_INDICATOR_TSK]:
        raise CollectorError(
            u'Unsupported source: {0:s} found unsupported file system.'.format(
                source_path))

    file_system_path_spec = getattr(
        scan_context.last_scan_node, 'path_spec', None)
    self._file_system = resolver.Resolver.OpenFileSystem(
        file_system_path_spec)

    if file_system_path_spec.type_indicator == dfvfs_definitions.TYPE_INDICATOR_OS:
      mount_point = file_system_path_spec
    else:
      mount_point = file_system_path_spec.parent

    self._path_resolver = windows_path_resolver.WindowsPathResolver(
        self._file_system, mount_point)

    if scan_context.source_type == scan_context.SOURCE_TYPE_DIRECTORY:
      if not self._ScanFileSystem(self._path_resolver):
        return False

    self._path_resolver.SetEnvironmentVariable(
        'WinDir', self._windows_directory)

    return True

  def OpenFile(self, windows_path):
    """Opens the file specificed by the Windows path.

    Args:
      windows_path: the Windows path to the file.

    Returns:
      The file-like object (instance of dfvfs.FileIO) or None if
      the file does not exist.
    """
    path_spec = self._path_resolver.ResolvePath(windows_path)
    if path_spec is None:
      return None

    return resolver.Resolver.OpenFileObject(path_spec)


class EventMessageStringExtractor(WindowsVolumeCollector):
  """Class that defines an event message string extractor."""

  def __init__(self):
    """Initializes the event message string extractor object."""
    super(EventMessageStringExtractor, self).__init__()
    self._system_root = None
    self._windows_version = None
    self.ascii_codepage = 'cp1252'
    self.invalid_message_filenames = None
    self.missing_table_message_filenames = None
    self.preferred_language_identifier = 0x0409

  def _CollectEventLogTypes(self):
    """Collects the Event Log types form the SYSTEM Registry file.

    Returns:
      A dictionary containing a dictionary of Event Log providers per event
      log type. E.g. { 'Application': { 'EventSystem': instance of 
                                        EventLogProvider, ... }, ... }
    """
    registry_filename = u'\\'.join([
        self._windows_directory, u'System32', u'config', u'SYSTEM'])

    registry_file = self._OpenRegistryFile(registry_filename)
    event_log_types = {}

    for event_log_provider in registry_file.GetEventLogProviders():
      if event_log_provider.log_type not in event_log_types:
        event_log_types[event_log_provider.log_type] = {}

      event_log_sources = event_log_types[event_log_provider.log_type]
      if event_log_provider.log_source in event_log_sources:
        logging.warning((
            u'Found duplicate Event Log source: {0:s} in type: {1:s}.').format(
                event_log_provider.log_source, event_log_provider.log_type))

      event_log_sources[event_log_provider.log_source] = event_log_provider

    registry_file.Close()

    return event_log_types

  def _GetSystemRoot(self):
    """Retrieves the value of %SystemRoot%.

    Returns:
      A string containing the system root.
    """
    if not self._system_root:
      self._system_root = self._GetSystemRootFromRegistry()

    if self._system_root:
      self._path_resolver.SetEnvironmentVariable(
          'SystemRoot', self._system_root)

    return self._system_root

  def _GetSystemRootFromRegistry(self):
    """Determines the value of %SystemRoot% from the SOFTWARE Registry file.

       The Windows path resolver is updated to expand this environment variable.

    Returns:
      A string containing the System Root or None otherwise.
    """
    registry_filename = u'\\'.join([
        self._windows_directory, u'System32', u'config', u'SOFTWARE'])

    registry_file = self._OpenRegistryFile(registry_filename)
    system_root = registry_file.GetSystemRoot()
    registry_file.Close()

    if system_root:
      system_root = system_root
    else:
      system_root = self._windows_directory

    return system_root

  def _GetWindowsVersion(self):
    """Determines the Windows version from kernel executable file.

    Returns:
      A string containing the Windows version or None otherwise.
    """
    system_root = self._GetSystemRoot()

    # Window NT variants.
    kernel_executable_path = u'\\'.join([
          system_root, u'System32', u'ntoskrnl.exe'])
    message_file = self._OpenMessageResourceFile(kernel_executable_path)

    if not message_file:
      # Window 9x variants.
      kernel_executable_path = u'\\'.join([
          system_root, u'System32', u'\kernel32.dll'])
      message_file = self._OpenMessageResourceFile(kernel_executable_path)

    if not message_file:
      return None

    return message_file.file_version

  def _OpenMessageResourceFile(self, windows_path):
    """Opens the message resource file specificed by the Windows path.

    Args:
      windows_path: the Windows path containing the messagge resource filename.

    Returns:
      The message resource file (instance of MessageResourceFile) or None.
    """
    path_spec = self._path_resolver.ResolvePath(windows_path)
    if path_spec is None:
      return None

    windows_path = self._path_resolver.GetWindowsPath(path_spec)
    if windows_path is None:
      logging.warning(u'Unable to retrieve Windows path.')

    file_object = resolver.Resolver.OpenFileObject(path_spec)
    if file_object is None:
      return None

    message_file = MessageResourceFile(
        windows_path, ascii_codepage=self.ascii_codepage,
        preferred_language_identifier=self.preferred_language_identifier)
    if not message_file.Open(file_object):
      return None

    return message_file

  def _OpenRegistryFile(self, windows_path):
    """Opens the registry file specificed by the Windows path.

    Args:
      windows_path: the Windows path containing the Registry filename.

    Returns:
      The Registry file (instance of RegistryFile) or None.
    """
    file_object = self.OpenFile(windows_path)
    if file_object is None:
      return None

    registry_file = RegistryFile()
    registry_file.Open(file_object)
    return registry_file

  @property
  def windows_version(self):
    """The Windows version."""
    if self._windows_version is None:
      self._windows_version = self._GetWindowsVersion()
    return self._windows_version

  @windows_version.setter
  def windows_version(self, value):
    """The Windows version."""
    self._windows_version = value

  def ExtractEventLogMessageStrings(self, output_writer):
    """Extracts the Event Log message strings from the message files.

    Args:
      output_writer: the output writer (instance of OutputWriter).
    """
    self.invalid_message_filenames = []
    self.missing_table_message_filenames = []
    processed_message_filenames = []
    event_log_types = self._CollectEventLogTypes()

    for event_log_type, event_log_sources in event_log_types.iteritems():
      for event_log_source, event_log_provider in event_log_sources.iteritems():
        output_writer.WriteEventLogProvider(event_log_provider)

        # TODO: parse category and parameter messages files.
        if event_log_provider.event_message_files:
          for message_filename in event_log_provider.event_message_files:
            if message_filename in processed_message_filenames:
              continue

            message_file = self._OpenMessageResourceFile(message_filename)
            mui_message_filename = None

            if not message_file:
              if message_filename in self.invalid_message_filenames:
                self.invalid_message_filenames.append(message_filename)
              continue

            if message_file.windows_path in processed_message_filenames:
              message_file.Close()
              continue

            message_table = message_file.GetMessageTableResource()
            if not message_table:
              # Windows Vista and later use a MUI resource to redirect to
              # a language specific message file.
              mui_language = message_file.GetMuiLanguage()

              if mui_language:
                message_filename_path, _, message_filename_name = (
                    message_filename.rpartition(u'\\'))

                mui_message_filename = u'{0:s}\\{1:s}\\{2:s}.mui'.format(
                    message_filename_path, mui_language, message_filename_name)

                mui_message_file = self._OpenMessageResourceFile(
                    mui_message_filename)

                if not mui_message_file:
                  mui_message_filename = u'{0:s}\\{1:s}.mui'.format(
                    message_filename_path, message_filename_name)

                  mui_message_file = self._OpenMessageResourceFile(
                      mui_message_filename)

                if mui_message_file:
                  message_file.Close()
                  message_file = mui_message_file

                  message_table = message_file.GetMessageTableResource()

            if not message_table:
              if message_filename not in self.missing_table_message_filenames:
                self.missing_table_message_filenames.append(message_filename)
            else:
              normalized_message_filename = message_filename.lower()

              if normalized_message_filename.startswith(
                  self._windows_directory.lower()):
                normalized_message_filename = u'%SystemRoot%{0:s}'.format(
                    message_filename[len(self._windows_directory):])

              elif normalized_message_filename.startswith(
                  u'%SystemRoot%'.lower()):
                normalized_message_filename = u'%SystemRoot%{0:s}'.format(
                    message_filename[len(u'%SystemRoot%'):])

              else:
                normalized_message_filename = message_filename

              logging.info('Processing: {0:s}'.format(normalized_message_filename))
              output_writer.WriteMessageFile(
                  event_log_provider, message_file, normalized_message_filename)

            if message_filename != message_file.windows_path:
              processed_message_filenames.append(message_file.windows_path)
            processed_message_filenames.append(message_filename)

            message_file.Close()


class EventLogProvider(object):
  """Class that defines a Windows Event Log provider."""

  def __init__(
      self, log_type, log_source, category_message_filenames,
      event_message_filenames, parameter_message_filenames):
    """Initializes the Windows Event Log provider.

    Args:
      log_type: the Event Log type.
      log_source: the Event Log source.
      category_message_filenames: the message filenames that contain
                                  the category strings.
      event_message_filenames: the message filenames that contain
                               the event messages.
      parameter_message_filenames: the message filenames that contain
                                   the parameter strings.
    """
    super(EventLogProvider, self).__init__()
    self.log_type = log_type
    self.log_source = log_source

    # It not empty the messages filenames can contain a list
    # of message file paths separated by ;
    if category_message_filenames:
      self.category_message_files = category_message_filenames.split(';')
    else:
      self.category_message_files = category_message_filenames

    if event_message_filenames:
      self.event_message_files = event_message_filenames.split(';')
    else:
      self.event_message_files = event_message_filenames

    if parameter_message_filenames:
      self.parameter_message_files = parameter_message_filenames.split(';')
    else:
      self.parameter_message_files = parameter_message_filenames


class MessageResourceFile(object):
  """Class that defines a Windows Message Resource file."""

  _RESOURCE_IDENTIFIER_STRING = 0x06
  _RESOURCE_IDENTIFIER_MESSAGE_TABLE = 0x0b
  _RESOURCE_IDENTIFIER_VERSION = 0x10

  def __init__(
      self, windows_path, ascii_codepage='cp1252',
      preferred_language_identifier=0x0409):
    """Initializes the Windows Message Resource file.

    Args:
      windows_path: normalized version of the Windows path.
      ascii_codepage: optional ASCII string codepage. The default is cp1252
                      (or windows-1252).
      preferred_language_identifier: optional preferred language identifier
                                     (LCID). The default is 0x0409 (en-US).
    """
    super(MessageResourceFile, self).__init__()
    self._ascii_codepage = ascii_codepage
    self._exe_file = pyexe.file()
    self._exe_file.set_ascii_codepage(self._ascii_codepage)
    self._file_version = None
    self._is_open = False
    self._preferred_language_identifier = preferred_language_identifier
    self._product_version = None
    self._wrc_stream = pywrc.stream()
    # TODO: wrc stream set codepage?
    self.windows_path = windows_path

  def _GetVersionInformation(self):
    """Retrieves the file and product version."""
    version_resource = self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_VERSION)
    if not version_resource:
      return None, None

    file_version = None
    product_version = None
    language_identifier = self._preferred_language_identifier
    if language_identifier in version_resource.language_identifiers:
      file_version = version_resource.get_file_version(language_identifier)
      product_version = version_resource.get_product_version(
          language_identifier)

    if not file_version or not product_version:
      for language_identifier in version_resource.language_identifiers:
        file_version = version_resource.get_file_version(language_identifier)
        product_version = version_resource.get_product_version(
            language_identifier)

        if file_version and product_version:
          break

    self._file_version = u'{0:d}.{1:d}.{2:d}.{3:d}'.format(
        (file_version >> 48) & 0xffff, (file_version >> 32) & 0xffff,
        (file_version >> 16) & 0xffff, file_version & 0xffff)

    self._product_version = u'{0:d}.{1:d}.{2:d}.{3:d}'.format(
        (product_version >> 48) & 0xffff, (product_version >> 32) & 0xffff,
        (product_version >> 16) & 0xffff, product_version & 0xffff)

    if file_version != product_version:
      logging.warning((
          u'Mismatch between file version: {0:s} and product version: '
          u'{1:s} in message file: {2:s}.').format(
              self._file_version, self._product_version, self.windows_path))

  @property
  def file_version(self):
    """The file version."""
    if self._file_version is None:
      self._GetVersionInformation()
    return self._file_version

  @property
  def product_version(self):
    """The product version."""
    if self._product_version is None:
      self._GetVersionInformation()
    return self._product_version

  def GetMessageTableResource(self):
    """Retrieves the message table resource."""
    return self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_MESSAGE_TABLE)

  def GetMuiLanguage(self):
    """Retrieves the MUI language or None if not available."""
    mui_resource = self._wrc_stream.get_resource_by_name('MUI')
    if not mui_resource:
      return None

    mui_language = None
    language_identifier = self._preferred_language_identifier
    if language_identifier in mui_resource.language_identifiers:
      mui_language = mui_resource.get_language(language_identifier)

    if not mui_language:
      for language_identifier in mui_resource.language_identifiers:
        mui_language = mui_resource.get_language(language_identifier)
        if mui_language:
          break

    return mui_language

  def GetStringResource(self):
    """Retrieves the string resource."""
    return self._wrc_stream.get_resource_by_identifier(
        self._RESOURCE_IDENTIFIER_STRING)

  def Open(self, file_object):
    """Opens the Windows Message Resource file using a file-like object.

    Args:
      file_object: the file-like object.

    Returns:
      A boolean containing True if successful or False if not.

    Raises:
      IOError: if already open.
    """
    if self._is_open:
      raise IOError(u'Already open.')

    self._file_object = file_object
    self._exe_file.open_file_object(self._file_object)
    exe_section = self._exe_file.get_section_by_name('.rsrc')

    if not exe_section:
      self._exe_file.close()
      return False

    self._wrc_stream.set_virtual_address(exe_section.virtual_address)
    self._wrc_stream.open_file_object(exe_section)

    return True

  def Close(self):
    """Closes the Windows Message Resource file.

    Raises:
      IOError: if not open.
    """
    if self._is_open:
      raise IOError(u'Not opened.')

    self._wrc_stream.close()
    self._exe_file.close()
    self._file_object.close()
    self._file_object = None


class RegistryFile(object):
  """Class that defines a Windows Registry file."""

  def __init__(self, ascii_codepage='cp1252'):
    """Initializes the Windows Registry file.

    Args:
      ascii_codepage: optional ASCII string codepage. The default is cp1252
                      (or windows-1252).
    """
    super(RegistryFile, self).__init__()
    self._file_object = None
    self._regf_file = pyregf.file()
    self._regf_file.set_ascii_codepage(ascii_codepage)

  def Open(self, file_object):
    """Opens the Windows Registry file using a file-like object.

    Args:
      file_object: the file-like object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._file_object = file_object
    self._regf_file.open_file_object(self._file_object)
    return True

  def Close(self):
    """Closes the Windows Registry file."""
    self._regf_file.close()
    self._file_object.close()
    self._file_object = None

  def GetSystemRoot(self):
    """Retrieves the value of %SystemRoot%.

    Returns:
      A string containing value of %SystemRoot%
      or None if the value could not be retrieved.
    """
    system_root = None

    current_version_key = self._regf_file.get_key_by_path(
        'Microsoft\\Windows NT\\CurrentVersion')

    if current_version_key:
      system_root_value = current_version_key.get_value_by_name('SystemRoot')
      if system_root_value:
        system_root = system_root_value.data_as_string

    return system_root

  def GetCurrentControlSet(self):
    """Retrieves the current control set.

    Returns:
      An integer containing the number of the current control set
      or 0 if no current control set could be retrieved.
    """
    control_set = 0
  
    select_key = self._regf_file.get_key_by_path('Select')
  
    if select_key:
      current_value = select_key.get_value_by_name('Current')
      if current_value: 
        control_set = current_value.data_as_integer
  
    return control_set

  def GetEventLogProviders(self):
    """Retrieves the Event Log providers.

    Yields:
      An Event Log provider object (EventLogProvider).
    """
    control_set = self.GetCurrentControlSet()
  
    if control_set > 0 and control_set <= 999:
      eventlog_key_path = 'ControlSet{0:03d}\\Services\\EventLog'.format(
          control_set)
  
      eventlog_key = self._regf_file.get_key_by_path(eventlog_key_path)
  
      if eventlog_key:
        for log_type_key in eventlog_key.sub_keys:
          log_type = log_type_key.name
  
          for log_source_key in log_type_key.sub_keys:
            log_source = log_source_key.name

            category_message_file_value = log_source_key.get_value_by_name(
                'CategoryMessageFile')
  
            if category_message_file_value:
              category_message_files = (
                  category_message_file_value.data_as_string)
            else:
              category_message_files = None
  
            event_message_file_value = log_source_key.get_value_by_name(
                'EventMessageFile')
  
            if event_message_file_value:
              event_message_files = event_message_file_value.data_as_string
            else:
              event_message_files = None

            parameter_message_file_value = log_source_key.get_value_by_name(
                'ParameterMessageFile')
  
            if parameter_message_file_value:
              parameter_message_files = parameter_message_file_value.data_as_string
            else:
              parameter_message_files = None

            yield EventLogProvider(
                log_type, log_source, category_message_files,
                event_message_files, parameter_message_files)


class Sqlite3DatabaseFile(object):
  """Class that defines a sqlite3 database file."""

  _HAS_TABLE_QUERY = (
      u'SELECT name FROM sqlite_master '
      u'WHERE type = "table" AND name = "{0:s}"')

  def __init__(self):
    """Initializes the database file object."""
    super(Sqlite3DatabaseFile, self).__init__()
    self._connection = None
    self._cursor = None
    self.filename = None

  def Close(self):
    """Closes the database file."""
    # We need to run commit or not all data is stored in the database.
    self._connection.commit()
    self._connection.close()

    self._connection = None
    self._cursor = None
    self.filename = None

  def CreateTable(self, table_name, column_definitions):
    """Creates a table.

    Args:
      table_name: the table name.
      column_definitions: list of strings containing column definitions.
    """
    sql_query = u'CREATE TABLE {0:s} ( {1:s} )'.format(
        table_name, u', '.join(column_definitions))

    self._cursor.execute(sql_query)

  def HasTable(self, table_name):
    """Determines if a specific table exists.

    Args:
      table_name: the table name.

    Returns:
      True if the table exists, false otheriwse.
    """
    sql_query = self._HAS_TABLE_QUERY.format(table_name)

    self._cursor.execute(sql_query)
    if self._cursor.fetchone():
      has_table = True
    else:
      has_table = False
    return has_table

  def GetValues(self, table_names, column_names, condition):
    """Retrieves values from a table.

    Args:
      table_names: list of table names.
      column_names: list of column names.
      condition: string containing the condition.

    Yields:
      A row object (instance of sqlite3.row).
    """
    if condition:
      condition = u' WHERE {0:s}'.format(condition)

    sql_query = u'SELECT {1:s} FROM {0:s}{2:s}'.format(
        u', '.join(table_names), u', '.join(column_names), condition)

    self._cursor.execute(sql_query)

    for row in self._cursor:
      values = {}
      for column_index in range(0, len(column_names)):
        column_name = column_names[column_index]
        values[column_name] = row[column_index]
      yield values

  def InsertValues(self, table_name, column_names, values):
    """Inserts values into a table.

    Args:
      table_name: the table name.
      column_names: list of column names.
      values: list of values formatted as a string.

    Raises:
      RuntimeError: if an unsupported value type is encountered.
    """
    if not values:
      return

    sql_values = []
    for value in values:
      if isinstance(value, basestring):
        # In sqlite3 the double quote is escaped with a second double quote.
        value = u'"{0:s}"'.format(re.sub('"', '""', value))
      elif isinstance(value, (int, long)):
        value = u'{0:d}'.format(value)
      elif isinstance(value, float):
        value = u'{0:f}'.format(value)
      else:
        raise RuntimeError(u'Unsupported value type: {0:s}.'.format(type(value)))
      sql_values.append(value)

    sql_query = u'INSERT INTO {0:s} ( {1:s} ) VALUES ( {2:s} )'.format(
        table_name, u', '.join(column_names), u', '.join(sql_values))

    self._cursor.execute(sql_query)

  def Open(self, filename):
    """Opens the database file.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self.filename = filename
    self._connection = sqlite3.connect(filename)
    if not self._connection:
      return False

    self._cursor = self._connection.cursor()
    if not self._cursor:
      return False

    return True


class Sqlite3EventProvidersWriter(object):
  """Class to represent a sqlite3 Event Log providers writer."""

  def __init__(self):
    """Initializes the Event Log providers writer object."""
    super(Sqlite3EventProvidersWriter, self).__init__()
    self._database_file = Sqlite3DatabaseFile()

  def _GetEventLogProviderKey(self, event_log_provider):
    """Retrieves the key of an Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).

    Returns:
      An integer containing the Event Log provider key or None if no such value.

    Raises:
      RuntimeError: if more than one value is found in the database.
    """
    table_names = ['event_log_providers']
    column_names = ['event_log_provider_key']
    condition = 'log_source = "{0:s}" AND log_type = "{1:s}"'.format(
        event_log_provider.log_source, event_log_provider.log_type)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values['event_log_provider_key']

    raise RuntimeError(u'More than one value found in database.')

  def _GetMessageFileKey(self, message_file, message_filename):
    """Retrieves the key of a message file.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.

    Returns:
      An integer containing the message file key or None if no such value.

    Raises:
      RuntimeError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = 'message_filename = "{0:s}"'.format(message_filename)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise RuntimeError(u'More than one value found in database.')

  def Open(self, filename):
    """Opens the Event Log providers writer object.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._database_file.Open(filename)

  def Close(self):
    """Closes the Event Log providers writer object."""
    self._database_file.Close()

  def WriteMessageFilePerEventLogProvider(
      self, event_log_provider, message_file, message_filename):
    """Writes the message files used by an Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
    """
    table_name = 'message_file_per_event_log_provider'
    column_names = ['message_file_key', 'event_log_provider_key']

    event_log_provider_key = self._GetEventLogProviderKey(event_log_provider)
    if event_log_provider_key is None:
      logging.warning(u'Missing event log provider key for: {0:s}'.format(
          event_log_provider.log_source))

    message_file_key = self._GetMessageFileKey(message_file, message_filename)
    if message_file_key is None:
      logging.warning(u'Missing message file key for: {0:s}'.format(
          message_filename))

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'message_file_key INTEGER', 'event_log_provider_key INTEGER']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = (
          'message_file_key = {0:d} AND event_log_provider_key = {1:d}').format(
              message_file_key, event_log_provider_key)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [message_file_key, event_log_provider_key]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    table_name = 'event_log_providers'
    column_names = ['log_source', 'log_type']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'event_log_provider_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'log_source TEXT', 'log_type TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = 'log_source = "{0:s}" AND log_type = "{1:s}"'.format(
          event_log_provider.log_source, event_log_provider.log_type)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [event_log_provider.log_source, event_log_provider.log_type]
      self._database_file.InsertValues(table_name, column_names, values)

  def WriteMessageFile(
      self, message_file, message_filename, database_filename):
    """Writes the Windows Message Resource file.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
      database_filename: the database filename.
    """
    table_name = 'message_files'
    column_names = ['message_filename', 'database_filename']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'message_filename TEXT', 'database_filename TEXT']
      self._database_file.CreateTable(table_name, column_definitions)
      insert_values = True

    else:
      condition = 'message_filename = "{0:s}"'.format(message_filename)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        # TODO: check if more than 1 result.
        insert_values = False

    if insert_values:
      values = [message_filename, database_filename]
      self._database_file.InsertValues(table_name, column_names, values)


class Sqlite3MessageFileWriter(object):
  """Class to represent a sqlite3 message file writer."""

  def __init__(self, message_file):
    """Initializes the message file writer object.

    Args:
      message_file: the message file (instance of MessageResourceFile).
    """
    super(Sqlite3MessageFileWriter, self).__init__()
    self._database_file = Sqlite3DatabaseFile()
    self._message_file = message_file

  def _GetMessageFileKey(self, message_file):
    """Retrieves the key of a message file.

    Args:
      message_file: the message file (instance of MessageResourceFile).

    Returns:
      An integer containing the message file key or None if no such value.

    Raises:
      RuntimeError: if more than one value is found in the database.
    """
    table_names = ['message_files']
    column_names = ['message_file_key']
    condition = (
        'path = "{0:s}" AND file_version = "{1:s}" AND '
        'product_version = "{2:s}"').format(
            message_file.windows_path, message_file.file_version,
            message_file.product_version)
    values_list = list(self._database_file.GetValues(
        table_names, column_names, condition))

    number_of_values = len(values_list)
    if number_of_values == 0:
      return

    if number_of_values == 1:
      values = values_list[0]
      return values['message_file_key']

    raise RuntimeError(u'More than one value found in database.')

  def _WriteLanguage(self, message_file, message_file_key, language_identifier):
    """Writes a language.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_file_key: the message file key.
      language_identifier: the language identifier (LCID).
    """
    table_name = 'language_per_message_file'
    column_names = ['lcid', 'message_file_key', 'identifier']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'lcid TEXT', 'message_file_key INT', 'identifier TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = 'lcid = "0x{0:08x}" AND message_file_key = "{1:d}"'.format(
          language_identifier, message_file_key)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        insert_values = False

    if insert_values:
      values = [
          '0x{0:08x}'.format(language_identifier), message_file_key,
          LANGUAGES.get(language_identifier, ['', ''])[0]]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessage(
      self, message_file, message_table, language_identifier, message_index,
      table_name, has_table):
    """Writes a message to a specific message table.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_table: the message table (instance of pywrc.message_table).
      language_identifier: the language identifier (LCID).
      message_index: the message index.
      table_name: the name of the table.
      has_table: boolean value to indicate the table previously existed in
                 the database.
    """
    column_names = ['message_identifier', 'message_string']

    message_identifier = message_table.get_message_identifier(
        language_identifier, message_index)
    message_identifier = '0x{0:08x}'.format(message_identifier)

    message_string = message_table.get_string(
        language_identifier, message_index)

    if not has_table:
      insert_values = True

    else:
      condition = 'message_identifier = "{0:s}"'.format(message_identifier)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 1:
        values = values_list[0]
        if message_string != values['message_string']:
          logging.warning((
              u'Message string mismatch for LCID: 0x{0:08x}, '
              u'file version: {1:s}, message identifier: {2:s}.\n'
              u'Found: {2:s}\nStored: {3:s}\n').format(
                  language_identifier, message_file.file_version,
                  message_identifier, message_string,
                  values['message_string']))

      elif number_of_values != 0:
        logging.warning((
             u'More than one message string found for LCID: 0x{0:08x}, '
             u'file version: {1:s}, message identifier: {2:s}.').format(
                 language_identifier, message_file.file_version,
                 message_identifier))

      # TODO: warn if new message has been found.
      insert_values = False

    if insert_values:
      values = [message_identifier, message_string]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageFile(self, message_file):
    """Writes a message file.

    Args:
      message_file: the message file (instance of MessageResourceFile).
    """
    table_name = 'message_files'
    column_names = ['path', 'file_version', 'product_version']

    has_table = self._database_file.HasTable(table_name)
    if not has_table:
      column_definitions = [
          'message_file_key INTEGER PRIMARY KEY AUTOINCREMENT',
          'path TEXT', 'file_version TEXT', 'product_version TEXT']
      self._database_file.CreateTable(table_name, column_definitions)

    if not has_table:
      insert_values = True

    else:
      condition = (
          'path = "{0:s}" AND file_version = "{1:s}" AND '
          'product_version = "{2:s}"').format(
              message_file.windows_path, message_file.file_version,
              message_file.product_version)
      values_list = list(self._database_file.GetValues(
          [table_name], column_names, condition))

      number_of_values = len(values_list)
      if number_of_values == 0:
        insert_values = True
      else:
        insert_values = False

    if insert_values:
      values = [
          message_file.windows_path, message_file.file_version,
          message_file.product_version]
      self._database_file.InsertValues(table_name, column_names, values)

  def _WriteMessageTable(
      self, message_file, message_table, language_identifier):
    """Writes a message table for a specific language identifier.

    Args:
      message_file: the message file (instance of MessageResourceFile).
      message_table: the message table (instance of pywrc.message_table).
      language_identifier: the language identifier (LCID).
    """
    number_of_messages = message_table.get_number_of_messages(
        language_identifier)

    if number_of_messages > 0:
      message_file_key = self._GetMessageFileKey(message_file)
      if message_file_key is None:
        logging.warning(u'Missing message file key for: {0:s}'.format(
            message_filename))

      self._WriteLanguage(message_file, message_file_key, language_identifier)

      table_name = u'message_table_0x{0:08x}_{1:s}'.format(
          language_identifier, message_file.file_version)
      table_name = re.sub('\.', '_', table_name)

      has_table = self._database_file.HasTable(table_name)
      if not has_table:
        column_definitions = ['message_identifier TEXT', 'message_string TEXT']
        self._database_file.CreateTable(table_name, column_definitions)

      for message_index in range(0, number_of_messages):
        self._WriteMessage(
            message_file, message_table, language_identifier, message_index,
            table_name, has_table)

  def Close(self):
    """Closes the message file writer object."""
    self._database_file.Close()

  def Open(self, filename):
    """Opens the message file writer object.

    Args:
      filename: the filename of the database.

    Returns:
      A boolean containing True if successful or False if not.
    """
    self._database_file.Open(filename)

  def WriteMessageTables(self):
    """Writes the message tables."""
    self._WriteMessageFile(self._message_file)

    message_table = self._message_file.GetMessageTableResource()
    try:
      number_of_languages = message_table.get_number_of_languages()
    except IOError as exception:
      number_of_languages = 0
      logging.warning(
          u'Unable to retrieve number of languages from: {0:s} '
          u'with error: {1:s}.'.format(self._message_file, exception))

    if number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        # TODO track the languages in a table.
        self._WriteMessageTable(
            self._message_file, message_table, language_identifier)


class Sqlite3OutputWriter(object):
  """Class that defines a sqlite3 output writer."""

  EVENT_PROVIDERS_DATABASE_FILENAME = u'winevt-kb.db'

  def __init__(self, databases_path):
    """Initializes the output writer object.

    Args:
      databases_path: the path to the database files.
    """
    super(Sqlite3OutputWriter, self).__init__()
    self._databases_path = databases_path
    self._event_providers_writer = None

  def Close(self):
    """Closes the output writer object."""
    self._event_providers_writer.Close()
    self._event_providers_writer = None

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    if not os.path.isdir(self._databases_path):
      return False

    self._event_providers_writer = Sqlite3EventProvidersWriter()
    self._event_providers_writer.Open(os.path.join(
        self._databases_path, self.EVENT_PROVIDERS_DATABASE_FILENAME))

    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    self._event_providers_writer.WriteEventLogProvider(event_log_provider)

  def WriteMessageFile(
      self, event_log_provider, message_file, message_filename):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
    """
    _, _, database_filename = message_file.windows_path.rpartition(u'\\')
    database_filename = u'{0:s}.db'.format(database_filename.lower())
    database_filename = re.sub('\.mui', '', database_filename)

    message_file_writer = Sqlite3MessageFileWriter(message_file)
    message_file_writer.Open(
        os.path.join(self._databases_path, database_filename))
    message_file_writer.WriteMessageTables()
    message_file_writer.Close()

    self._event_providers_writer.WriteMessageFile(
        message_file, message_filename, database_filename)

    # TODO: write the relationship between the event log provider and
    # the message file and the Windows version?
    self._event_providers_writer.WriteMessageFilePerEventLogProvider(
        event_log_provider, message_file, message_filename)


class StdoutOutputWriter(object):
  """Class that defines a stdout output writer."""

  def _WriteMessageTable(self, message_table):
    """Writes the Windows Message Resource file message table.

    Args:
      message_table: the message table (instance of pywrc.message_table).
    """
    try:
      number_of_languages = message_table.get_number_of_languages()
    except IOError as exception:
      number_of_languages = 0
      logging.warning(
          u'Unable to retrieve number of languages with error: {0:s}.'.format(
              exception))

    if number_of_languages > 0:
      for language_identifier in message_table.language_identifiers:
        number_of_messages = message_table.get_number_of_messages(
            language_identifier)

        if number_of_messages > 0:
          print(u'Message table:')
          print(u'LCID\t\t: 0x{0:08x}'.format(language_identifier))
          for message_index in range(0, number_of_messages):
            message_identifier = message_table.get_message_identifier(
                language_identifier, message_index)
            message_string = message_table.get_string(
                language_identifier, message_index)

            ouput_string = u'0x{0:08x}\t: {1:s}'.format(
                message_identifier, message_string)

            print(ouput_string.encode('utf8'))

          print(u'')

  def Close(self):
    """Closes the output writer object."""
    pass

  def Open(self):
    """Opens the output writer object.

    Returns:
      A boolean containing True if successful or False if not.
    """
    return True

  def WriteEventLogProvider(self, event_log_provider):
    """Writes the Event Log provider.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
    """
    print(u'Source\t\t: {0:s}'.format(
        event_log_provider.log_source))

    print(u'Event Log type\t: {0:s}'.format(
        event_log_provider.log_type))

    print(u'Categories\t: {0:s}'.format(
        event_log_provider.category_message_files))

    print(u'Messages\t: {0:s}'.format(
        event_log_provider.event_message_files))

    print(u'Parameters\t: {0:s}'.format(
        event_log_provider.parameter_message_files))

    print(u'')

  def WriteMessageFile(
      self, event_log_provider, message_file, message_filename):
    """Writes the Windows Message Resource file.

    Args:
      event_log_provider: the Event Log provider (instance of EventLogProvider).
      message_file: the message file (instance of MessageResourceFile).
      message_filename: the message filename.
    """
    file_version = getattr(message_file, 'file_version', '')
    product_version = getattr(message_file, 'product_version', '')

    print(u'Message file:')
    print(u'Path\t\t: {0:s}'.format(message_file.windows_path))
    print(u'File version\t: {0:s}'.format(file_version))
    print(u'Product version\t: {0:s}'.format(product_version))

    message_table = message_file.GetMessageTableResource()
    self._WriteMessageTable(message_table)


def Main():
  """The main program function.

  Returns:
    A boolean containing True if successful or False if not.
  """
  args_parser = argparse.ArgumentParser(description=(
      'Extract strings from message resource files for Event Log sources.'))

  args_parser.add_argument(
      'source', nargs='?', action='store', metavar='/mnt/c/',
      default=None, help=('path of the volume containing C:\\Windows or the '
                          'filename of a storage media image containing the '
                          'C:\\Windows directory.'))

  args_parser.add_argument(
      '--db', dest='database', action='store', metavar='./winevt-db/',
      default=None, help='path to write the sqlite3 databases to.')

  args_parser.add_argument(
      '--winver', dest='windows_version', action='store', metavar='xp',
      default=None, help=('string that identifies the Windows version '
                          'in the database.'))

  options = args_parser.parse_args()

  if not options.source:
    print(u'Source value is missing.')
    print(u'')
    args_parser.print_help()
    print(u'')
    return False

  logging.basicConfig(
      level=logging.INFO, format=u'[%(levelname)s] %(message)s')

  if options.database:
    if not os.path.isdir(options.database):
      print(u'No such directory: {0:s}'.format(options.database))
      print(u'')
      return False

    output_writer = Sqlite3OutputWriter(options.database)
  else:
    output_writer = StdoutOutputWriter()

  if not output_writer.Open():
    print(u'Unable to open output writer.')
    print(u'')
    return False

  extractor = EventMessageStringExtractor()

  if not extractor.GetWindowsVolumePathSpec(options.source):
    print((u'Unable to retrieve the volume with the Windows directory from: '
           u'{0:s}.').format(options.source))
    print(u'')
    return False

  if not extractor.windows_version:
    if not options.windows_version:
      print(u'Unable to determine Windows version.')

      if options.database:
        print(u'Database output requires a Windows version, specify one with '
              u'--winver.')
        print(u'')
        return False

    extractor.windows_version = options.windows_version

  print(u'Windows version: {0:s}.'.format(extractor.windows_version))
  print(u'')

  extractor.ExtractEventLogMessageStrings(output_writer)
  output_writer.Close()

  if extractor.invalid_message_filenames:
    print(u'Message resource files not found or without resource section:')
    for message_filename in extractor.invalid_message_filenames:
      print(u'{0:s}'.format(message_filename))
    print(u'')

  if extractor.missing_table_message_filenames:
    print(u'Message resource files without a message table resource:')
    for message_filename in extractor.missing_table_message_filenames:
      print(u'{0:s}'.format(message_filename))
    print(u'')

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)
