## mscms.dll

Path: %SystemRoot%\system32\mscms.dll

### 6.1.7600.16385, 6.1.7601.17514, 6.2.9200.16384, 6.3.9600.16384, 6.3.9600.18589, 10.0.10586.0

Message identifier | Message string
--- | ---
0x10000001 | CMM for ICC profiles\r\n
0x10000002 | CMM for WCS profiles\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Profile Management\r\n
0x70000002 | Transform Creation\r\n
0x70000003 | Color Translation\r\n
0x70000004 | Color Calibration\r\n
0x90000001 | Microsoft-Windows-WindowsColorSystem\r\n
0xb0000001 | Installed color profile %1.\r\n
0xb0000002 | Uninstalled color profile %1.\r\n
0xb0000003 | Associated color profile %1 with device %2 in %3 scope.\r\n
0xb0000004 | Disassociated color profile %1 from device %2 in %3 scope.\r\n
0xb0000005 | Set default profile to %1 for device %2 in %3 scope.\r\n
0xb0000006 | Set the "use per-user profiles" setting for device %1 to %2.\r\n
0xb0000008 | Set the default rendering intent to %1 in %2 scope.\r\n
0xb0000009 | Unset the default rendering intent in %1 scope. The system-wide default rendering intent will now be used.\r\n
0xb000000a | Set the default profile for %1 rendering intent to %2 in %3 scope.\r\n
0xb000000b | Unset the default profile for %1 rendering intent in %2 scope. This rendering intent will now use the corresponding system-wide default profile.\r\n
0xb000000c | Set the default profile for working space '%1' to %2 in %3 scope.\r\n
0xb000000d | Unset the default profile for working space '%1' in %2 scope. This working space will now use the corresponding system-wide default profile.\r\n
0xb000000e | Set the default CAMP profile to %1 in %2 scope.\r\n
0xb000000f | Unset the default CAMP profile in %1 scope. The system-wide default CAMP profile will now be used.\r\n
0xb0000010 | WCS profile %1 is invalid: %2\r\n
0xb0000011 | Initialized %1 plug-in %2.\r\n
0xb0000012 | Failed to initialize %1 plug-in %2: error %3. Fallback %4.\r\n
0xb0000013 | V4 LUT elements in '%1' tag: B curves %2, Matrix %3, M curves %4, CLUT %5, A curves %6.\r\n
0xb0000014 | Adjust black point from legacy encoding to V4 encoding.\r\n
0xb0000015 | Adjust black point from V4 encoding to legacy encoding.\r\n
0xb0000016 | Adjust LAB from legacy encoding to V4 encoding.\r\n
0xb0000017 | Adjust LAB from V4 encoding to legacy encoding.\r\n
0xb0000018 | Convert LAB to XYZ.\r\n
0xb0000019 | Convert XYZ  to LAB.\r\n
0xb000001a | Device has extended range: ([%1, %2], [%3, %4], [%5, %6]).\r\n
0xb000001b | Destination device lightness range: [%1, %2].\r\n
0xb000001c | Creating gamut map model for %1 intent.\r\n
0xb000001d | Created standard gamut map model for %1 intent.\r\n
0xb000001f | Failed to create gamut map model: error %1.\r\n
0xb0000020 | Opening color profile(CDMP = '%2' (%1), CAMP = '%4' (%3), GMMP = '%6' (%5), desired access = %7, share mode = %8, creation mode = %9).\r\n
0xb0000021 | Color profile successfully opened.\r\n
0xb0000022 | Failed to open color profile: error %1.\r\n
0xb0000023 | ICC profile information: size = %1 bytes, version = %2, class = '%3', data color space = '%4', profile connection space = '%5'.\r\n
0xb0000024 | Extracted WCS profile from ICC profile.\r\n
0xb0000025 | CITE color transform optimization: %1.\r\n
0xb0000026 | Selected %1 LUT.\r\n
0xb0000027 | Selected '%1' tag to create %2 LUT for '%3' class profile with %4 rendering intent.\r\n
0xb0000028 | Creating color transform(LCS type = %1, intent = %2, source profile = '%3', destination profile = '%5' (%4), target profile = '%7' (%6), flags = %8).\r\n
0xb0000029 | Creating multi-profile color transform(%1 profiles, %2 intents, flags = %3).\r\n
0xb000002a | Color transform successfully created: hxform = %1.\r\n
0xb000002b | Color transform creation failed: error %1.\r\n
0xb000002c | Translating colors(hxform = %1, %2 input colors, input color type = %3, output color type = %4).\r\n
0xb000002d | WCS translating colors(hxform = %1, %2 input colors, %3 input channels, input data type = %4, %5 input bytes, %6 output channels, output data type = %7, %8 output bytes).\r\n
0xb000002e | Translating bitmap bits(hxform = %1, input bitmap format = %2, width = %3, height = %4, input stride = %5, output bitmap format = %6, output stride = %7).\r\n
0xb000002f | Colors successfully translated\r\n
0xb0000030 | Color translation failed: error %1.\r\n
0xb0000031 | Calibration refresh invoked. Windows calibration state management enabled = %1.\r\n
0xb0000032 | Refreshing calibration for device '%1'. Color profile exists and contains calibration data = %2.\r\n
0xb0000033 | Calibration refresh finished, return code = %1.\r\n
0xb0000034 | Applying calibration adjustments.  Adapter gamma adjustments = %1, monitor adjustments = %2.\r\n
0xb0000035 | Setting Windows calibration state management to %1.\r\n
0xb0000036 | Not refreshing display calibration because Windows calibration management is not enabled.\r\n
0xb0000037 | Not refreshing display calibration because the session is a remote session.\r\n
0xb0000038 | Not refreshing display calibration on a device for which multiple physical monitors exist.\r\n
0xb0000039 | Loading calibration data from color profile %1 failed with error %2.\r\n
0xb000003a | Applying calibration data failed with error %1.\r\n
0xd0000001 | ICC profile\r\n
0xd0000002 | device model profile\r\n
0xd0000003 | color appearance model profile\r\n
0xd0000004 | gamut mapping model profile\r\n
0xd0000005 | perceptual\r\n
0xd0000006 | relative colorimetric\r\n
0xd0000007 | saturation\r\n
0xd0000008 | absolute colorimetric\r\n
0xd0000009 | none\r\n
0xd000000a | RGB working space\r\n
0xd000000b | custom working space\r\n
0xd000000c | perceptual\r\n
0xd000000d | relative colorimetric\r\n
0xd000000e | saturation\r\n
0xd000000f | absolute colorimetric\r\n
0xd0000010 | embedded\r\n
0xd0000011 | (invalid)\r\n
0xd0000012 | system-wide\r\n
0xd0000013 | current user\r\n
0xd0000014 | device model\r\n
0xd0000015 | gamut mapping model\r\n
0xd0000016 | not used\r\n
0xd0000017 | used\r\n
0xd0000018 | not present\r\n
0xd0000019 | present\r\n
0xd000001a | file based\r\n
0xd000001b | memory based\r\n
0xd000001c | not used\r\n
0xd000001d | read-only\r\n
0xd000001e | read-write\r\n
0xd000001f | for reading\r\n
0xd0000020 | for writing\r\n
0xd0000021 | create new\r\n
0xd0000022 | create always\r\n
0xd0000023 | open existing\r\n
0xd0000024 | open always\r\n
0xd0000025 | truncate existing\r\n
0xd0000026 | none\r\n
0xd0000027 | from source appearance space to destination colorimetric space\r\n
0xd0000028 | from source appearance space to destination device space\r\n
0xd0000029 | floating point\r\n
0xd000002a | integer\r\n
0xd000002b | gamut\r\n
0xd000002c | normal\r\n
0xd000002d | calibrated RGB\r\n
0xd000002e | sRGB\r\n
0xd000002f | Windows color space\r\n
0xd0000030 | business\r\n
0xd0000031 | graphics\r\n
0xd0000032 | images\r\n
0xd0000033 | absolute colorimetric\r\n
0xd0000034 | gray\r\n
0xd0000035 | RGB\r\n
0xd0000036 | XYZ\r\n
0xd0000037 | Yxy\r\n
0xd0000038 | Lab\r\n
0xd0000039 | 3-channel\r\n
0xd000003a | CMYK\r\n
0xd000003b | 5-channel\r\n
0xd000003c | 6-channel\r\n
0xd000003d | 7-channel\r\n
0xd000003e | 8-channel\r\n
0xd000003f | named\r\n
0xd0000040 | byte\r\n
0xd0000041 | word\r\n
0xd0000042 | float\r\n
0xd0000043 | S2.13 fixed-point\r\n
0xd0000044 | x555 RGB\r\n
0xd0000045 | x555 XYZ\r\n
0xd0000046 | x555 Yxy\r\n
0xd0000047 | x555 Lab\r\n
0xd0000048 | x555 G3CH\r\n
0xd0000049 | RGB triplets\r\n
0xd000004a | BGR triplets\r\n
0xd000004b | XYZ triplets\r\n
0xd000004c | Yxy triplets\r\n
0xd000004d | Lab triplets\r\n
0xd000004e | G3CH triplets\r\n
0xd000004f | 5-channel\r\n
0xd0000050 | 6-channel\r\n
0xd0000051 | 7-channel\r\n
0xd0000052 | 8-channel\r\n
0xd0000053 | gray\r\n
0xd0000054 | xRGB quads\r\n
0xd0000055 | xBGR quads\r\n
0xd0000056 | G3CH quads\r\n
0xd0000057 | KYMC quads\r\n
0xd0000058 | CMYK quads\r\n
0xd0000059 | 10-bit RGB\r\n
0xd000005a | 10-bit XYZ\r\n
0xd000005b | 10-bit Yxy\r\n
0xd000005c | 10-bit Lab\r\n
0xd000005d | 10-bit G3CH\r\n
0xd000005e | named index\r\n
0xd000005f | 16-bit RGB\r\n
0xd0000060 | 16-bit XYZ\r\n
0xd0000061 | 16-bit Yxy\r\n
0xd0000062 | 16-bit Lab\r\n
0xd0000063 | 16-bit G3CH\r\n
0xd0000064 | 16-bit gray\r\n
0xd0000065 | 565 RGB\r\n
0xd0000066 | 32-bit scRGB\r\n
0xd0000067 | 32-bit scARGB\r\n
0xd0000068 | S2.13 fixed-point scRGB\r\n
0xd0000069 | S2.13 fixed-point scARGB\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.18362.836, 10.0.19041.1, 10.0.19041.546, 10.0.22000.65

Message identifier | Message string
--- | ---
0x10000001 | CMM for ICC profiles\r\n
0x10000002 | CMM for WCS profiles\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Profile Management\r\n
0x70000002 | Transform Creation\r\n
0x70000003 | Color Translation\r\n
0x70000004 | Color Calibration\r\n
0x90000001 | Microsoft-Windows-WindowsColorSystem\r\n
0xb0000001 | Installed color profile %1.\r\n
0xb0000002 | Uninstalled color profile %1.\r\n
0xb0000003 | Associated color profile %1 with device %2 in %3 scope.\r\n
0xb0000004 | Disassociated color profile %1 from device %2 in %3 scope.\r\n
0xb0000005 | Set default profile to %1 for device %2 in %3 scope.\r\n
0xb0000006 | Set the "use per-user profiles" setting for device %1 to %2.\r\n
0xb0000008 | Set the default rendering intent to %1 in %2 scope.\r\n
0xb0000009 | Unset the default rendering intent in %1 scope. The system-wide default rendering intent will now be used.\r\n
0xb000000a | Set the default profile for %1 rendering intent to %2 in %3 scope.\r\n
0xb000000b | Unset the default profile for %1 rendering intent in %2 scope. This rendering intent will now use the corresponding system-wide default profile.\r\n
0xb000000c | Set the default profile for working space '%1' to %2 in %3 scope.\r\n
0xb000000d | Unset the default profile for working space '%1' in %2 scope. This working space will now use the corresponding system-wide default profile.\r\n
0xb000000e | Set the default CAMP profile to %1 in %2 scope.\r\n
0xb000000f | Unset the default CAMP profile in %1 scope. The system-wide default CAMP profile will now be used.\r\n
0xb0000010 | WCS profile %1 is invalid: %2\r\n
0xb0000013 | V4 LUT elements in '%1' tag: B curves %2, Matrix %3, M curves %4, CLUT %5, A curves %6.\r\n
0xb0000014 | Adjust black point from legacy encoding to V4 encoding.\r\n
0xb0000015 | Adjust black point from V4 encoding to legacy encoding.\r\n
0xb0000016 | Adjust LAB from legacy encoding to V4 encoding.\r\n
0xb0000017 | Adjust LAB from V4 encoding to legacy encoding.\r\n
0xb0000018 | Convert LAB to XYZ.\r\n
0xb0000019 | Convert XYZ  to LAB.\r\n
0xb000001a | Device has extended range: ([%1, %2], [%3, %4], [%5, %6]).\r\n
0xb000001b | Destination device lightness range: [%1, %2].\r\n
0xb000001c | Creating gamut map model for %1 intent.\r\n
0xb000001d | Created standard gamut map model for %1 intent.\r\n
0xb000001f | Failed to create gamut map model: error %1.\r\n
0xb0000020 | Opening color profile(CDMP = '%2' (%1), CAMP = '%4' (%3), GMMP = '%6' (%5), desired access = %7, share mode = %8, creation mode = %9).\r\n
0xb0000021 | Color profile successfully opened.\r\n
0xb0000022 | Failed to open color profile: error %1.\r\n
0xb0000023 | ICC profile information: size = %1 bytes, version = %2, class = '%3', data color space = '%4', profile connection space = '%5'.\r\n
0xb0000024 | Extracted WCS profile from ICC profile.\r\n
0xb0000025 | CITE color transform optimization: %1.\r\n
0xb0000026 | Selected %1 LUT.\r\n
0xb0000027 | Selected '%1' tag to create %2 LUT for '%3' class profile with %4 rendering intent.\r\n
0xb0000028 | Creating color transform(LCS type = %1, intent = %2, source profile = '%3', destination profile = '%5' (%4), target profile = '%7' (%6), flags = %8).\r\n
0xb0000029 | Creating multi-profile color transform(%1 profiles, %2 intents, flags = %3).\r\n
0xb000002a | Color transform successfully created: hxform = %1.\r\n
0xb000002b | Color transform creation failed: error %1.\r\n
0xb000002c | Translating colors(hxform = %1, %2 input colors, input color type = %3, output color type = %4).\r\n
0xb000002d | WCS translating colors(hxform = %1, %2 input colors, %3 input channels, input data type = %4, %5 input bytes, %6 output channels, output data type = %7, %8 output bytes).\r\n
0xb000002e | Translating bitmap bits(hxform = %1, input bitmap format = %2, width = %3, height = %4, input stride = %5, output bitmap format = %6, output stride = %7).\r\n
0xb000002f | Colors successfully translated\r\n
0xb0000030 | Color translation failed: error %1.\r\n
0xb0000031 | Calibration refresh invoked. Windows calibration state management enabled = %1.\r\n
0xb0000032 | Refreshing calibration for device '%1'. Color profile exists and contains calibration data = %2.\r\n
0xb0000033 | Calibration refresh finished, return code = %1.\r\n
0xb0000034 | Applying calibration adjustments.  Adapter gamma adjustments = %1, monitor adjustments = %2.\r\n
0xb0000035 | Setting Windows calibration state management to %1.\r\n
0xb0000036 | Not refreshing display calibration because Windows calibration management is not enabled.\r\n
0xb0000037 | Not refreshing display calibration because the session is a remote session.\r\n
0xb0000038 | Not refreshing display calibration on a device for which multiple physical monitors exist.\r\n
0xb0000039 | Loading calibration data from color profile %1 failed with error %2.\r\n
0xb000003a | Applying calibration data failed with error %1.\r\n
0xd0000001 | ICC profile\r\n
0xd0000002 | device model profile\r\n
0xd0000003 | color appearance model profile\r\n
0xd0000004 | gamut mapping model profile\r\n
0xd0000005 | perceptual\r\n
0xd0000006 | relative colorimetric\r\n
0xd0000007 | saturation\r\n
0xd0000008 | absolute colorimetric\r\n
0xd0000009 | none\r\n
0xd000000a | RGB working space\r\n
0xd000000b | custom working space\r\n
0xd000000c | perceptual\r\n
0xd000000d | relative colorimetric\r\n
0xd000000e | saturation\r\n
0xd000000f | absolute colorimetric\r\n
0xd0000010 | embedded\r\n
0xd0000011 | (invalid)\r\n
0xd0000012 | system-wide\r\n
0xd0000013 | current user\r\n
0xd0000014 | not present\r\n
0xd0000015 | present\r\n
0xd0000016 | file based\r\n
0xd0000017 | memory based\r\n
0xd0000018 | not used\r\n
0xd0000019 | read-only\r\n
0xd000001a | read-write\r\n
0xd000001b | for reading\r\n
0xd000001c | for writing\r\n
0xd000001d | create new\r\n
0xd000001e | create always\r\n
0xd000001f | open existing\r\n
0xd0000020 | open always\r\n
0xd0000021 | truncate existing\r\n
0xd0000022 | none\r\n
0xd0000023 | from source appearance space to destination colorimetric space\r\n
0xd0000024 | from source appearance space to destination device space\r\n
0xd0000025 | floating point\r\n
0xd0000026 | integer\r\n
0xd0000027 | gamut\r\n
0xd0000028 | normal\r\n
0xd0000029 | calibrated RGB\r\n
0xd000002a | sRGB\r\n
0xd000002b | Windows color space\r\n
0xd000002c | business\r\n
0xd000002d | graphics\r\n
0xd000002e | images\r\n
0xd000002f | absolute colorimetric\r\n
0xd0000030 | gray\r\n
0xd0000031 | RGB\r\n
0xd0000032 | XYZ\r\n
0xd0000033 | Yxy\r\n
0xd0000034 | Lab\r\n
0xd0000035 | 3-channel\r\n
0xd0000036 | CMYK\r\n
0xd0000037 | 5-channel\r\n
0xd0000038 | 6-channel\r\n
0xd0000039 | 7-channel\r\n
0xd000003a | 8-channel\r\n
0xd000003b | named\r\n
0xd000003c | byte\r\n
0xd000003d | word\r\n
0xd000003e | float\r\n
0xd000003f | S2.13 fixed-point\r\n
0xd0000040 | x555 RGB\r\n
0xd0000041 | x555 XYZ\r\n
0xd0000042 | x555 Yxy\r\n
0xd0000043 | x555 Lab\r\n
0xd0000044 | x555 G3CH\r\n
0xd0000045 | RGB triplets\r\n
0xd0000046 | BGR triplets\r\n
0xd0000047 | XYZ triplets\r\n
0xd0000048 | Yxy triplets\r\n
0xd0000049 | Lab triplets\r\n
0xd000004a | G3CH triplets\r\n
0xd000004b | 5-channel\r\n
0xd000004c | 6-channel\r\n
0xd000004d | 7-channel\r\n
0xd000004e | 8-channel\r\n
0xd000004f | gray\r\n
0xd0000050 | xRGB quads\r\n
0xd0000051 | xBGR quads\r\n
0xd0000052 | G3CH quads\r\n
0xd0000053 | KYMC quads\r\n
0xd0000054 | CMYK quads\r\n
0xd0000055 | 10-bit RGB\r\n
0xd0000056 | 10-bit XYZ\r\n
0xd0000057 | 10-bit Yxy\r\n
0xd0000058 | 10-bit Lab\r\n
0xd0000059 | 10-bit G3CH\r\n
0xd000005a | named index\r\n
0xd000005b | 16-bit RGB\r\n
0xd000005c | 16-bit XYZ\r\n
0xd000005d | 16-bit Yxy\r\n
0xd000005e | 16-bit Lab\r\n
0xd000005f | 16-bit G3CH\r\n
0xd0000060 | 16-bit gray\r\n
0xd0000061 | 565 RGB\r\n
0xd0000062 | 32-bit scRGB\r\n
0xd0000063 | 32-bit scARGB\r\n
0xd0000064 | S2.13 fixed-point scRGB\r\n
0xd0000065 | S2.13 fixed-point scARGB\r\n
