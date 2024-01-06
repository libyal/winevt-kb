## ntfs.sys

Path: %SystemRoot%\system32\drivers\ntfs.sys

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events has occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains unicode NULL.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%3 of index entry %4 of index %2\r\nin file 0x%5 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%4 of index entry %3 of index %2\r\nwith parent 0x%1 is not the same as 0x%5.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n

### 6.1.7600.16385, 6.1.7601.17577

Message identifier | Message string
--- | ---
0x10000034 | SQM\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains unicode NULL.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%3 of index entry %4 of index %2\r\nin file 0x%5 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%4 of index entry %3 of index %2\r\nwith parent 0x%1 is not the same as 0x%5.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %1, DeviceName: %2.%n(%3)\r\n
0x12000034 | SQM\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | VolumeMount VolumeId: %1, DeviceName: %3\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001012 | Index Sort\r\n
0x00001013 | Index Cycle\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002120 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted subtree is rooted at entry number %4!lu! of the index block located at Vcn 0x%5!0I64x!.\r\n
0x00002130 | A file system index structure contains a cycle.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The cycle includes %4!lu! index blocks starting at Vcn 0x%5!0I64x! and ending at Vcn 0x%6!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x000061c7 | Swapping attribute of type code 0x%1 and instance tag 0x%2 with\r\nattribute of type code 0x%3 and instance tag 0x%4 for file record 0x%5.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %1, DeviceName: %2.%n(%3)\r\n
0x12000034 | SQM\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | VolumeMount VolumeId: %1, DeviceName: %3\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n

### 6.3.9600.18838

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001012 | Index Sort\r\n
0x00001013 | Index Cycle\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002120 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted subtree is rooted at entry number %4!lu! of the index block located at Vcn 0x%5!0I64x!.\r\n
0x00002130 | A file system index structure contains a cycle.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The cycle includes %4!lu! index blocks starting at Vcn 0x%5!0I64x! and ending at Vcn 0x%6!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x000061c7 | Swapping attribute of type code 0x%1 and instance tag 0x%2 with\r\nattribute of type code 0x%3 and instance tag 0x%4 for file record 0x%5.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %1, DeviceName: %2.%n(%3)\r\n
0x12000034 | SQM\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | VolumeMount VolumeId: %1, DeviceName: %3\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb100008d | An operation failed because the disk was full.%n%n\n          Process: %5%n\n          Free space in bytes: %7%n\n          Page file size in bytes: 0%n\n          Volume guid: %1%n\n          Volume name: %3%n\n          Is boot volume: %6%n%nYour disk '%3' is full. Use disk cleanup to free up disk space by deleting unnecessary files. If this is a thinly provisioned volume the physical storage backing this volume may have been exhausted.%n\r\n
0xb100008e | Summary of disk space usage, since last event:%n%n\n          Lowest free space in bytes: %4%n\n          Highest free space in bytes: %5%n\n          Page file size in bytes: 0%n\n          Volume guid: %1%n\n          Volume name: %3%n\n          Is boot volume: %6%n\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001012 | Index Sort\r\n
0x00001013 | Index Cycle\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002120 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted subtree is rooted at entry number %4!lu! of the index block located at Vcn 0x%5!0I64x!.\r\n
0x00002130 | A file system index structure contains a cycle.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The cycle includes %4!lu! index blocks starting at Vcn 0x%5!0I64x! and ending at Vcn 0x%6!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x000061c7 | Swapping attribute of type code 0x%1 and instance tag 0x%2 with\r\nattribute of type code 0x%3 and instance tag 0x%4 for file record 0x%5.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %1, DeviceName: %2.%n(%3)\r\n
0x010000d2 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nIt is now fixed.\r\n
0x010000d3 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nRepair was unsucccessful.%nPossibly out of available slabs.\r\n
0x12000034 | SQM\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x31000007 | Resume\r\n
0x31000008 | Suspend\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | The NTFS volume has been successfully mounted.%n%n\n          Volume GUID: %4%n\n          Volume Name: %6%n\n          Volume Label: %8%n\n          Device Name: %3%n\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb100008d | An operation failed because the disk was full.%n%n\n          Process: %5%n\n          Free space in bytes: %7%n\n          Page file size in bytes: 0%n\n          Volume guid: %1%n\n          Volume name: %3%n\n          Is boot volume: %6%n%nYour disk '%3' is full. Use disk cleanup to free up disk space by deleting unnecessary files. If this is a thinly provisioned volume the physical storage backing this volume may have been exhausted.%n\r\n
0xb100008e | Summary of disk space usage, since last event:%n%n\n          Lowest free space in bytes: %4%n\n          Highest free space in bytes: %5%n\n          Page file size in bytes: 0%n\n          Volume guid: %1%n\n          Volume name: %3%n\n          Is boot volume: %6%n\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xb10000f0 | File metadata optimization started.%n%n\n                   Volume guid: %1%n\n                   Volume name: %3%n\n                   File reference: %4%n\r\n
0xb10000f1 | File metadata optimization completed.%n%n\n                   Volume guid: %1%n\n                   Volume name: %3%n\n                   File reference: %4%n\r\n
0xb100012c | NTFS volume dismount has started.%n%n\n          Volume GUID: %4%n\n          Volume Name: %6%n\n          Volume Label: %8%n\r\n
0xb100012d | NTFS has sent volume dismount event notification and is waiting for the notifications to complete.\r\n
0xb100012e | The volume dismount event notification on the NTFS volume has completed.\r\n
0xb100012f | The NTFS volume has successfully dismounted.%n%n\n          Volume GUID: %4%n\n          Volume Name: %6%n\n          Volume Label: %8%n\r\n
0xb1000130 | The NTFS volume dismount failed.%n%n\n          Error:%1%n\r\n
0xb1000131 | NTFS failed to mount the volume.%n%n\n          Error: %1%n\n          Volume GUID: %2%n\n          Volume Name: %4%n%nGuidance:%nThe volume is recognized by NTFS but it is corrupted that NTFS could not mount it. Run CHKDSK /F to fix any errors on this volume, and then try accessing it.\r\n
0xb1000191 | Efs offloading initiated.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000192 | Efs offloading read regular file.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000193 | Efs offloading write regular file.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000194 | Efs legacy initiated.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000195 | Efs legacy read regular file.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000196 | Efs legacy write regular file.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n

### 10.0.14393.0, 10.0.14393.447

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001012 | Index Sort\r\n
0x00001013 | Index Cycle\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002120 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted subtree is rooted at entry number %4!lu! of the index block located at Vcn 0x%5!0I64x!.\r\n
0x00002130 | A file system index structure contains a cycle.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The cycle includes %4!lu! index blocks starting at Vcn 0x%5!0I64x! and ending at Vcn 0x%6!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x000061c7 | Swapping attribute of type code 0x%1 and instance tag 0x%2 with\r\nattribute of type code 0x%3 and instance tag 0x%4 for file record 0x%5.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %1, DeviceName: %2.%n(%3)\r\n
0x0100008f | Surprise removal of a persistent memory device with active DAX mappings. This might lead to data corruption.%n%n\n          Volume GUID: %4%n\n          Volume Name: %6%n\n          Volume Label: %8%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000090 | A volume that already has DAX mappings is being mounted. This generally occurs after surprise removal. This might lead to data corruption.%n%n\n          Volume GUID: %4%n\n          Volume Name: %6%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000096 | An IO failed with %12 and NTFS has relocated the clusters. The original clusters are now marked as bad and they will not be reused.%nThis may indicate a failing disk.%n%n\n          Process Id: %5%n\n          Process name: %6%n\n          File name: %8%n\n          File offset: %9%n\n          %11 cluster(s) were marked as bad starting at cluster %10%n%n\n          Volume guid: %1%n\n          Volume name: %3%n\n          Is boot volume: %4%n\r\n
0x010000d2 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nIt is now fixed.\r\n
0x010000d3 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nRepair was unsucccessful.%nPossibly out of available slabs.\r\n
0x11000016 | Statistics\r\n
0x11000019 | BadClusterHotFix\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x31000007 | Resume\r\n
0x31000008 | Suspend\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | The NTFS volume has been successfully mounted.%n%n\n          Volume GUID: %4%n\n          Volume Name: %6%n\n          Volume Label: %8%n\n          Device Name: %3%n\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb100008d | An operation failed because the disk was full.%n%n\n          Process: %5%n\n          Free space in bytes: %7%n\n          Page file size in bytes: 0%n\n          Volume guid: %1%n\n          Volume name: %3%n\n          Is boot volume: %6%n%nYour disk '%3' is full. Use disk cleanup to free up disk space by deleting unnecessary files. If this is a thinly provisioned volume the physical storage backing this volume may have been exhausted.%n\r\n
0xb100008e | Summary of disk space usage, since last event:%n%n\n          Lowest free space in bytes: %4%n\n          Highest free space in bytes: %5%n\n          Page file size in bytes: 0%n\n          Volume guid: %1%n\n          Volume name: %3%n\n          Is boot volume: %6%n\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xb10000f0 | File metadata optimization started.%n%n\n                   Volume guid: %1%n\n                   Volume name: %3%n\n                   File reference: %4%n\r\n
0xb10000f1 | File metadata optimization completed.%n%n\n                   Volume guid: %1%n\n                   Volume name: %3%n\n                   File reference: %4%n\r\n
0xb100012c | NTFS volume dismount has started.%n%n\n          Volume GUID: %4%n\n          Volume Name: %6%n\n          Volume Label: %8%n\r\n
0xb100012d | NTFS has sent volume dismount event notification and is waiting for the notifications to complete.\r\n
0xb100012e | The volume dismount event notification on the NTFS volume has completed.\r\n
0xb100012f | The NTFS volume has successfully dismounted.%n%n\n          Volume GUID: %4%n\n          Volume Name: %6%n\n          Volume Label: %8%n\r\n
0xb1000130 | The NTFS volume dismount failed.%n%n\n          Error:%1%n\r\n
0xb1000131 | NTFS failed to mount the volume.%n%n\n          Error: %1%n\n          Volume GUID: %2%n\n          Volume Name: %4%n%nGuidance:%nThe volume is recognized by NTFS but it is corrupted that NTFS could not mount it. Run CHKDSK /F to fix any errors on this volume, and then try accessing it.\r\n
0xb1000191 | Efs offloading initiated.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000192 | Efs offloading read regular file.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000193 | Efs offloading write regular file.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000194 | Efs legacy initiated.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000195 | Efs legacy read regular file.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1000196 | Efs legacy write regular file.%n%n\n                   Volume serial: %1%n\n                   File reference: %2%n\n                   File name: %4%n\r\n
0xb1010091 | IO latency summary common data for volume:%n%n\n          Volume Id: %1%n\n          Volume name: %3%n\n          Is boot volume: %4%n%n\n          Max Acceptable IO Latency: %5 ms%n\n          Read/Write latency buckets (us): [%6, %7, %8, %9, %10, %11, %12]%n\n          Trim latency buckets (us): [%13, %14, %15, %16, %17, %18, %19]%n\n          Flush latency buckets (us): [%20, %21, %22, %23, %24, %25, %26]%n\r\n
0xb1010092 | IO latency summary:%n%n\n          Volume Id: %1%n\n          Volume name: %3%n\n          Is boot volume: %4%n%n\n          Interval duration: %6 us%n%n\n          Non-cached reads:%n\n                    IO count: %7%n\n                    Total bytes: %8%n\n                    Avg latency: %9 ns%n%n\n          Non-cached writes: %n\n                    IO count: %10%n\n                    Total bytes: %11%n\n                    Avg latency: %12 ns%n%n\n          File flushes: %n\n                    IO count: %13%n\n                    Avg latency: %14 ns%n%n\n          Volume flushes: %n\n                    IO count: %15%n\n                    Avg latency: %16 ns%n%n\n          File level trims: %n\n                    IO count: %17%n\n                    Total bytes: %18%n\n                    Extents count: %19%n\n                    Avg latency: %20 ns%n%n\n          Volume trims: %n\n                    IO count: %21%n\n                    Total bytes: %22%n\n                    Extents count: %23%n\n                    Avg latency: %24 ns%n%n\nFor more details see the details tab.%n\r\n
0xb1010094 | A %9 failed with %14.%nThis may indicate a failing disk.%n%n\n          Process Id: %5%n\n          Process name: %6%n\n          File name: %8%n\n          IO Size: %10 bytes%n\n          File offset: %11%n\n          %13 cluster(s) starting at cluster %12%n%n\n          Volume Id: %1%n\n          Volume name: %3%n\n          Is boot volume: %4%n\r\n
0xb1010095 | In the past %5 seconds we had IO failures.%nThis may indicate a failing disk.%n%n\n          High latency IO count: %6%n\n          Failed writes: %7%n\n          Failed reads: %8%n\n          Bad clusters relocated: %9%n%n\n          Volume Id: %1%n\n          Volume name: %3%n\n          Is boot volume: %4%n\r\n
0xb1020093 | An IO took more than %5 ms to complete:%n%n\n          Process Id: %6%n\n          Process name: %7%n\n          File name: %9%n\n          File offset: %12%n\n          IO Type: %10%n\n          IO Size: %11 bytes%n\n          %15 cluster(s) starting at cluster %14%n\n          Latency: %13 ms%n%n\n          Volume Id: %1%n\n          Volume name: %3%n\n          Is boot volume: %4%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n
0xd1000026 | Write: NonPaging, NonCached, Async\r\n
0xd1000027 | Write: NonPaging, NonCached, Sync\r\n
0xd1000028 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd1000029 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd100002a | Write: NonPaging, Cached, Async\r\n
0xd100002b | Write: NonPaging, Cached, Sync\r\n
0xd100002c | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd100002d | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd100002e | Write: Paging, NonCached, Async\r\n
0xd100002f | Write: Paging, NonCached, Sync\r\n
0xd1000030 | Write: Paging, NonCached, Async, Writethrough\r\n
0xd1000031 | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd1000032 | Read: NonPaging, NonCached, Async\r\n
0xd1000033 | Read: NonPaging, NonCached, Sync\r\n
0xd1000034 | Read: NonPaging, Cached, Async\r\n
0xd1000035 | Read: NonPaging, Cached, Sync\r\n
0xd1000036 | Read: Paging, NonCached, Async\r\n
0xd1000037 | Read: Paging, NonCached, Sync\r\n
0xd1000038 | read\r\n
0xd1000039 | write\r\n

### 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001012 | Index Sort\r\n
0x00001013 | Index Cycle\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002120 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted subtree is rooted at entry number %4!lu! of the index block located at Vcn 0x%5!0I64x!.\r\n
0x00002130 | A file system index structure contains a cycle.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The cycle includes %4!lu! index blocks starting at Vcn 0x%5!0I64x! and ending at Vcn 0x%6!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x000061c7 | Swapping attribute of type code 0x%1 and instance tag 0x%2 with\r\nattribute of type code 0x%3 and instance tag 0x%4 for file record 0x%5.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %1, DeviceName: %2.%n(%3)\r\n
0x0100008f | Surprise removal of a persistent memory device with active DAX mappings. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000090 | A volume that already has DAX mappings is being mounted. This generally occurs after surprise removal. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000096 | An IO failed with %12 and NTFS has relocated the clusters. The original clusters are now marked as bad and they will not be reused.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          File offset: %9%n\r\n          %11 cluster(s) were marked as bad starting at cluster %10%n%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0x010000d2 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nIt is now fixed.\r\n
0x010000d3 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nRepair was unsucccessful.%nPossibly out of available slabs.\r\n
0x11000016 | Statistics\r\n
0x11000019 | BadClusterHotFix\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x31000007 | Resume\r\n
0x31000008 | Suspend\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | The NTFS volume has been successfully mounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n          Device Name: %3%n\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb100008d | An operation failed because the disk was full.%n%n\r\n          Process: %5%n\r\n          Free space in bytes: %7%n\r\n          Page file size in bytes: 0%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n%nYour disk '%3' is full. Use disk cleanup to free up disk space by deleting unnecessary files. If this is a thinly provisioned volume the physical storage backing this volume may have been exhausted.%n\r\n
0xb100008e | Summary of disk space usage, since last event:%n%n\r\n          Lowest free space in bytes: %4%n\r\n          Highest free space in bytes: %5%n\r\n          Page file size in bytes: 0%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xb10000f0 | File metadata optimization started.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb10000f1 | File metadata optimization completed.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb100012c | NTFS volume dismount has started.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb100012d | NTFS has sent volume dismount event notification and is waiting for the notifications to complete.\r\n
0xb100012e | The volume dismount event notification on the NTFS volume has completed.\r\n
0xb100012f | The NTFS volume has successfully dismounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb1000130 | The NTFS volume dismount failed.%n%n\r\n          Error:%1%n\r\n
0xb1000131 | NTFS failed to mount the volume.%n%n\r\n          Error: %1%n\r\n          Volume GUID: %2%n\r\n          Volume Name: %4%n%nGuidance:%nThe volume is recognized by NTFS but it is corrupted that NTFS could not mount it. Run CHKDSK /F to fix any errors on this volume, and then try accessing it.\r\n
0xb1000191 | Efs offloading initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000192 | Efs offloading read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000193 | Efs offloading write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000194 | Efs legacy initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000195 | Efs legacy read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000196 | Efs legacy write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1010092 | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Interval duration: %6 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %7%n\r\n                    Total bytes: %8%n\r\n                    Avg latency: %9 ns%n%n\r\n          Non-cached writes: %n\r\n                    IO count: %10%n\r\n                    Total bytes: %11%n\r\n                    Avg latency: %12 ns%n%n\r\n          File flushes: %n\r\n                    IO count: %13%n\r\n                    Avg latency: %14 ns%n%n\r\n          Volume flushes: %n\r\n                    IO count: %15%n\r\n                    Avg latency: %16 ns%n%n\r\n          File level trims: %n\r\n                    IO count: %17%n\r\n                    Total bytes: %18%n\r\n                    Extents count: %19%n\r\n                    Avg latency: %20 ns%n%n\r\n          Volume trims: %n\r\n                    IO count: %21%n\r\n                    Total bytes: %22%n\r\n                    Extents count: %23%n\r\n                    Avg latency: %24 ns%n%n\r\nFor more details see the details tab.%n\r\n
0xb1010094 | A %9 failed with %14.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          IO Size: %10 bytes%n\r\n          File offset: %11%n\r\n          %13 cluster(s) starting at cluster %12%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xb1010095 | In the past %5 seconds we had IO failures.%nThis may indicate a failing disk.%n%n\r\n          High latency IO count: %6%n\r\n          Failed writes: %7%n\r\n          Failed reads: %8%n\r\n          Bad clusters relocated: %9%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xb1020091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Max Acceptable IO Latency: %5 ms%n\r\n          Read/Write latency buckets (ns): [%6, %7, %8, %9, %10, %11, %12]%n\r\n          Trim latency buckets (ns): [%13, %14, %15, %16, %17, %18, %19]%n\r\n          Flush latency buckets (ns): [%20, %21, %22, %23, %24, %25, %26]%n\r\n
0xb1020093 | An IO took more than %5 ms to complete:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          File offset: %12%n\r\n          IO Type: %10%n\r\n          IO Size: %11 bytes%n\r\n          %15 cluster(s) starting at cluster %14%n\r\n          Latency: %13 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n
0xd1000026 | Write: NonPaging, NonCached, Async\r\n
0xd1000027 | Write: NonPaging, NonCached, Sync\r\n
0xd1000028 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd1000029 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd100002a | Write: NonPaging, Cached, Async\r\n
0xd100002b | Write: NonPaging, Cached, Sync\r\n
0xd100002c | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd100002d | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd100002e | Write: Paging, NonCached, Async\r\n
0xd100002f | Write: Paging, NonCached, Sync\r\n
0xd1000030 | Write: Paging, NonCached, Async, Writethrough\r\n
0xd1000031 | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd1000032 | Read: NonPaging, NonCached, Async\r\n
0xd1000033 | Read: NonPaging, NonCached, Sync\r\n
0xd1000034 | Read: NonPaging, Cached, Async\r\n
0xd1000035 | Read: NonPaging, Cached, Sync\r\n
0xd1000036 | Read: Paging, NonCached, Async\r\n
0xd1000037 | Read: Paging, NonCached, Sync\r\n
0xd1000038 | read\r\n
0xd1000039 | write\r\n

### 10.0.17134.677, 10.0.17763.404, 10.0.17763.529

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001012 | Index Sort\r\n
0x00001013 | Index Cycle\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002120 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted subtree is rooted at entry number %4!lu! of the index block located at Vcn 0x%5!0I64x!.\r\n
0x00002130 | A file system index structure contains a cycle.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The cycle includes %4!lu! index blocks starting at Vcn 0x%5!0I64x! and ending at Vcn 0x%6!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x000061c7 | Swapping attribute of type code 0x%1 and instance tag 0x%2 with\r\nattribute of type code 0x%3 and instance tag 0x%4 for file record 0x%5.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %1, DeviceName: %2.%n(%3)\r\n
0x0100008f | Surprise removal of a persistent memory device with active DAX mappings. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000090 | A volume that already has DAX mappings is being mounted. This generally occurs after surprise removal. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000096 | An IO failed with %12 and NTFS has relocated the clusters. The original clusters are now marked as bad and they will not be reused.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          File offset: %9%n\r\n          %11 cluster(s) were marked as bad starting at cluster %10%n%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0x010000d2 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nIt is now fixed.\r\n
0x010000d3 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nRepair was unsucccessful.%nPossibly out of available slabs.\r\n
0x11000016 | Statistics\r\n
0x11000019 | BadClusterHotFix\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x31000007 | Resume\r\n
0x31000008 | Suspend\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | The NTFS volume has been successfully mounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n          Device Name: %3%n\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb100008d | An operation failed because the disk was full.%n%n\r\n          Process: %5%n\r\n          Free space in bytes: %7%n\r\n          Total reserved space in bytes: %8%n\r\n          Txf TotalAbortReservation space in bytes: %9%n\r\n          Requested space in bytes: %10%n\r\n          Page file size in bytes: %11%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n%nYour disk '%3' is full. Use disk cleanup to free up disk space by deleting unnecessary files. If this is a thinly provisioned volume the physical storage backing this volume may have been exhausted.%n\r\n
0xb100008e | Summary of disk space usage, since last event:%n%n\r\n          Lowest free space in bytes: %4%n\r\n          Highest free space in bytes: %5%n\r\n          Page file size in bytes: 0%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xb10000f0 | File metadata optimization started.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb10000f1 | File metadata optimization completed.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb100012c | NTFS volume dismount has started.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb100012d | NTFS has sent volume dismount event notification and is waiting for the notifications to complete.\r\n
0xb100012e | The volume dismount event notification on the NTFS volume has completed.\r\n
0xb100012f | The NTFS volume has successfully dismounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb1000130 | The NTFS volume dismount failed.%n%n\r\n          Error:%1%n\r\n
0xb1000131 | NTFS failed to mount the volume.%n%n\r\n          Error: %1%n\r\n          Volume GUID: %2%n\r\n          Volume Name: %4%n%nGuidance:%nThe volume is recognized by NTFS but it is corrupted that NTFS could not mount it. Run CHKDSK /F to fix any errors on this volume, and then try accessing it.\r\n
0xb1000191 | Efs offloading initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000192 | Efs offloading read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000193 | Efs offloading write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000194 | Efs legacy initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000195 | Efs legacy read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000196 | Efs legacy write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1010092 | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Interval duration: %6 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %7%n\r\n                    Total bytes: %8%n\r\n                    Avg latency: %9 ns%n%n\r\n          Non-cached writes: %n\r\n                    IO count: %10%n\r\n                    Total bytes: %11%n\r\n                    Avg latency: %12 ns%n%n\r\n          File flushes: %n\r\n                    IO count: %13%n\r\n                    Avg latency: %14 ns%n%n\r\n          Volume flushes: %n\r\n                    IO count: %15%n\r\n                    Avg latency: %16 ns%n%n\r\n          File level trims: %n\r\n                    IO count: %17%n\r\n                    Total bytes: %18%n\r\n                    Extents count: %19%n\r\n                    Avg latency: %20 ns%n%n\r\n          Volume trims: %n\r\n                    IO count: %21%n\r\n                    Total bytes: %22%n\r\n                    Extents count: %23%n\r\n                    Avg latency: %24 ns%n%n\r\nFor more details see the details tab.%n\r\n
0xb1010094 | A %9 failed with %14.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          IO Size: %10 bytes%n\r\n          File offset: %11%n\r\n          %13 cluster(s) starting at cluster %12%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xb1010095 | In the past %5 seconds we had IO failures.%nThis may indicate a failing disk.%n%n\r\n          High latency IO count: %6%n\r\n          Failed writes: %7%n\r\n          Failed reads: %8%n\r\n          Bad clusters relocated: %9%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xb1020091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Max Acceptable IO Latency: %5 ms%n\r\n          Read/Write latency buckets (ns): [%6, %7, %8, %9, %10, %11, %12]%n\r\n          Trim latency buckets (ns): [%13, %14, %15, %16, %17, %18, %19]%n\r\n          Flush latency buckets (ns): [%20, %21, %22, %23, %24, %25, %26]%n\r\n
0xb1020093 | An IO took more than %5 ms to complete:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          File offset: %12%n\r\n          IO Type: %10%n\r\n          IO Size: %11 bytes%n\r\n          %15 cluster(s) starting at cluster %14%n\r\n          Latency: %13 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n
0xd1000026 | Write: NonPaging, NonCached, Async\r\n
0xd1000027 | Write: NonPaging, NonCached, Sync\r\n
0xd1000028 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd1000029 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd100002a | Write: NonPaging, Cached, Async\r\n
0xd100002b | Write: NonPaging, Cached, Sync\r\n
0xd100002c | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd100002d | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd100002e | Write: Paging, NonCached, Async\r\n
0xd100002f | Write: Paging, NonCached, Sync\r\n
0xd1000030 | Write: Paging, NonCached, Async, Writethrough\r\n
0xd1000031 | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd1000032 | Read: NonPaging, NonCached, Async\r\n
0xd1000033 | Read: NonPaging, NonCached, Sync\r\n
0xd1000034 | Read: NonPaging, Cached, Async\r\n
0xd1000035 | Read: NonPaging, Cached, Sync\r\n
0xd1000036 | Read: Paging, NonCached, Async\r\n
0xd1000037 | Read: Paging, NonCached, Sync\r\n
0xd1000038 | read\r\n
0xd1000039 | write\r\n

### 10.0.18362.1, 10.0.18362.719

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001012 | Index Sort\r\n
0x00001013 | Index Cycle\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002120 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted subtree is rooted at entry number %4!lu! of the index block located at Vcn 0x%5!0I64x!.\r\n
0x00002130 | A file system index structure contains a cycle.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The cycle includes %4!lu! index blocks starting at Vcn 0x%5!0I64x! and ending at Vcn 0x%6!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x000061c7 | Swapping attribute of type code 0x%1 and instance tag 0x%2 with\r\nattribute of type code 0x%3 and instance tag 0x%4 for file record 0x%5.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %1, DeviceName: %2.%n(%3)\r\n
0x0100008f | Surprise removal of a persistent memory device with active DAX mappings. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000090 | A volume that already has DAX mappings is being mounted. This generally occurs after surprise removal. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000096 | An IO failed with %12 and NTFS has relocated the clusters. The original clusters are now marked as bad and they will not be reused.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          File offset: %9%n\r\n          %11 cluster(s) were marked as bad starting at cluster %10%n%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0x010000d2 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nIt is now fixed.\r\n
0x010000d3 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nRepair was unsucccessful.%nPossibly out of available slabs.\r\n
0x11000016 | Statistics\r\n
0x11000019 | BadClusterHotFix\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x31000007 | Resume\r\n
0x31000008 | Suspend\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | The NTFS volume has been successfully mounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n          Device Name: %3%n\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb100008d | An operation failed because the disk was full.%n%n\r\n          Process: %5%n\r\n          Free space in bytes: %7%n\r\n          Total reserved space in bytes: %8%n\r\n          Txf TotalAbortReservation space in bytes: %9%n\r\n          Requested space in bytes: %10%n\r\n          Page file size in bytes: %11%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n%nYour disk '%3' is full. Use disk cleanup to free up disk space by deleting unnecessary files. If this is a thinly provisioned volume the physical storage backing this volume may have been exhausted.%n\r\n
0xb100008e | Summary of disk space usage, since last event:%n%n\r\n          Lowest free space in bytes: %4%n\r\n          Highest free space in bytes: %5%n\r\n          Page file size in bytes: 0%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xb10000f0 | File metadata optimization started.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb10000f1 | File metadata optimization completed.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb100012c | NTFS volume dismount has started.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb100012d | NTFS has sent volume dismount event notification and is waiting for the notifications to complete.\r\n
0xb100012e | The volume dismount event notification on the NTFS volume has completed.\r\n
0xb100012f | The NTFS volume has successfully dismounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb1000130 | The NTFS volume dismount failed.%n%n\r\n          Error:%1%n\r\n
0xb1000131 | NTFS failed to mount the volume.%n%n\r\n          Error: %1%n\r\n          Volume GUID: %2%n\r\n          Volume Name: %4%n%nGuidance:%nThe volume is recognized by NTFS but it is corrupted that NTFS could not mount it. Run CHKDSK /F to fix any errors on this volume, and then try accessing it.\r\n
0xb1000191 | Efs offloading initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000192 | Efs offloading read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000193 | Efs offloading write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000194 | Efs legacy initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000195 | Efs legacy read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000196 | Efs legacy write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1010094 | A %9 failed with %14.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          IO Size: %10 bytes%n\r\n          File offset: %11%n\r\n          %13 cluster(s) starting at cluster %12%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xb1010095 | In the past %5 seconds we had IO failures.%nThis may indicate a failing disk.%n%n\r\n          High latency IO count: %6%n\r\n          Failed writes: %7%n\r\n          Failed reads: %8%n\r\n          Bad clusters relocated: %9%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xb1020091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Max Acceptable IO Latency: %5 ms%n\r\n          Read/Write latency buckets (ns): [%6, %7, %8, %9, %10, %11, %12]%n\r\n          Trim latency buckets (ns): [%13, %14, %15, %16, %17, %18, %19]%n\r\n          Flush latency buckets (ns): [%20, %21, %22, %23, %24, %25, %26]%n\r\n
0xb1020092 | IO latency summary:%n%n\r\n          Version: %1%n\r\n          Volume Id: %2%n\r\n          Volume name: %4%n\r\n          Tier index: %6%n%n\r\n          Max Acceptable IO Latency: %7 ms%n%n\r\n          Read/Write latency buckets (ns): [%8, %9, %10, %11, %12, %13, %14]%n\r\n          Trim latency buckets (ns): [%15, %16, %17, %18, %19, %20, %21]%n\r\n          Flush latency buckets (ns): [%22, %23, %24, %25, %26, %27, %28]%n%n\r\n          Interval duration: %30 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %31%n\r\n                    Total bytes: %32%n\r\n                    Avg latency: %33 ns%n%n\r\n          Non-cached writes: %n\r\n                    IO count: %34%n\r\n                    Total bytes: %35%n\r\n                    Avg latency: %36 ns%n%n\r\n          File flushes: %n\r\n                    IO count: %37%n\r\n                    Avg latency: %38 ns%n%n\r\n          Directory flushes: %n\r\n                    IO count: %39%n\r\n                    Avg latency: %40 ns%n%n\r\n          Volume flushes: %n\r\n                    IO count: %41%n\r\n                    Avg latency: %42 ns%n%n\r\n          File level trims: %n\r\n                    IO count: %43%n\r\n                    Total bytes: %44%n\r\n                    Extents count: %45%n\r\n                    Avg latency: %46 ns%n%n\r\n          Volume trims: %n\r\n                    IO count: %47%n\r\n                    Total bytes: %48%n\r\n                    Extents count: %49\r\n                    Avg latency: %50 ns%n%n\r\nFor more details see the details tab.%n\r\n
0xb1020093 | An IO took more than %5 ms to complete:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          File offset: %12%n\r\n          IO Type: %10%n\r\n          IO Size: %11 bytes%n\r\n          %15 cluster(s) starting at cluster %14%n\r\n          Latency: %13 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n
0xd1000026 | Write: NonPaging, NonCached, Async\r\n
0xd1000027 | Write: NonPaging, NonCached, Sync\r\n
0xd1000028 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd1000029 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd100002a | Write: NonPaging, Cached, Async\r\n
0xd100002b | Write: NonPaging, Cached, Sync\r\n
0xd100002c | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd100002d | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd100002e | Write: Paging, NonCached, Async\r\n
0xd100002f | Write: Paging, NonCached, Sync\r\n
0xd1000030 | Write: Paging, NonCached, Async, Writethrough\r\n
0xd1000031 | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd1000032 | Read: NonPaging, NonCached, Async\r\n
0xd1000033 | Read: NonPaging, NonCached, Sync\r\n
0xd1000034 | Read: NonPaging, Cached, Async\r\n
0xd1000035 | Read: NonPaging, Cached, Sync\r\n
0xd1000036 | Read: Paging, NonCached, Async\r\n
0xd1000037 | Read: Paging, NonCached, Sync\r\n
0xd1000038 | read\r\n
0xd1000039 | write\r\n

### 10.0.19041.1, 10.0.19041.610

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001012 | Index Sort\r\n
0x00001013 | Index Cycle\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002120 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted subtree is rooted at entry number %4!lu! of the index block located at Vcn 0x%5!0I64x!.\r\n
0x00002130 | A file system index structure contains a cycle.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The cycle includes %4!lu! index blocks starting at Vcn 0x%5!0I64x! and ending at Vcn 0x%6!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x00005000 | The file size is 0x%1!0I64x!. The maximum size for the volume is 0x%2!0I64x!.\r\n
0x00005001 | The bitmap size is 0x%1!0I64x!. The system limit is 0x%2!0I64x!.\r\n
0x00005002 | The USN journal size is 0x%1!0I64x!. The system limit is 0x%2!0I64x!.\r\n
0x00005003 | The file size is 0x%1!0I64x!. The system limit is 0x%2!0I64x!.\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x000061c7 | Swapping attribute of type code 0x%1 and instance tag 0x%2 with\r\nattribute of type code 0x%3 and instance tag 0x%4 for file record 0x%5.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x00006aa2 | Faild to enumerate blocks\r\n
0x00006aa3 | Unsupported on thinly provisioned volume\r\n
0x00006aa4 | Claiming persisted memory failed\r\n
0x00006aa5 | Allocating memory for KSR runs failed\r\n
0x00006aa6 | Could not get system address from Mdl\r\n
0x00006aa7 | Invalid KSR version\r\n
0x00006aa8 | Vcb's TotalClusters did not match with KSRData's TotalClusters\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %2, DeviceName: %4.%n%n\r\n          Failure status: %5%n%n\r\n          Device GUID: %6%n\r\n          Device manufacturer: %8%n\r\n          Device model: %10%n\r\n          Device revision: %12%n\r\n          Device serial number: %14%n\r\n          Bus type: %15%n%n\r\n          Adapter serial number: %17%n\r\n
0x0100008f | Surprise removal of a persistent memory device with active DAX mappings. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000090 | A volume that already has DAX mappings is being mounted. This generally occurs after surprise removal. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000096 | An IO failed with %12 and NTFS has relocated the clusters. The original clusters are now marked as bad and they will not be reused.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          File offset: %9%n\r\n          %11 cluster(s) were marked as bad starting at cluster %10%n%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0x010000d2 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nIt is now fixed.\r\n
0x010000d3 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nRepair was unsucccessful.%nPossibly out of available slabs.\r\n
0x11000016 | Statistics\r\n
0x11000019 | BadClusterHotFix\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x31000007 | Resume\r\n
0x31000008 | Suspend\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | The NTFS volume has been successfully mounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n          Device Name: %3%n\r\n
0xb1000005 | NTFS KSR data retrieved successfully.%n%n\r\n          Volume GUID: %4%n\r\n          Device Name: %3%n\r\n
0xb1000006 | NTFS KSR data retrieval failed.%n%n\r\n          Volume GUID: %4%n\r\n          Device Name: %3%n\r\n          Error: %6\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb100008d | An operation failed because the disk was full.%n%n\r\n          Process: %5%n\r\n          Free space in bytes: %7%n\r\n          Total reserved space in bytes: %8%n\r\n          Txf TotalAbortReservation space in bytes: %9%n\r\n          Requested space in bytes: %10%n\r\n          Page file size in bytes: %11%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n%nYour disk '%3' is full. Use disk cleanup to free up disk space by deleting unnecessary files. If this is a thinly provisioned volume the physical storage backing this volume may have been exhausted.%n\r\n
0xb100008e | Summary of disk space usage, since last event:%n%n\r\n          Lowest free space in bytes: %4%n\r\n          Highest free space in bytes: %5%n\r\n          Page file size in bytes: 0%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n\r\n
0xb1000097 | In the past %5 seconds %6 files were deleted.  %7 of the deletions record their process name.%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Process name: %8%n\r\n          Delete file count: %9\r\n
0xb1000098 | A process has not acknowledged an NTFS oplock break in a long time.%n%n\r\n          Time (seconds): %1%n\r\n          Owner Process: %2%n\r\n          Breaking Process: %3%n\r\n
0xb100009a | System file pages are now locked into memory.%n%n\r\n                   Volume Id: %1%n\r\n                   Volume name: %3%n%n\r\n                   File reference: %4%n\r\n                   File name: %6%n\r\n
0xb100009b | System file pages are no longer locked into memory.%n%n\r\n                   Volume Id: %1%n\r\n                   Volume name: %3%n%n\r\n                   File reference: %4%n\r\n                   File name: %6%n%n\r\n                   Reason: %7%n\r\n
0xb100009d | An exclusive resource duration exceeded %5 ms:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          Major function: %8%n\r\n          Minor function: %9%n\r\n          Control code: %10%n\r\n          Resource name: %11%n\r\n          Wait duration: %12 ms%n\r\n          Hold duration: %13 ms%n\r\n          Combined duration: %14 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %15%n\r\n          Device manufacturer: %17%n\r\n          Device model: %19%n\r\n          Device revision: %21%n\r\n          Device serial number: %23%n\r\n          Bus type: %24%n%n\r\n          Adapter serial number: %26%n\r\n
0xb100009e | NTFS metadata statistics for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          UserFileReads: %4%n\r\n          UserFileReadBytes: %5%n\r\n          UserDiskReads: %6%n\r\n          UserFileWrites: %7%n\r\n          UserFileWriteBytes: %8%n\r\n          UserDiskWrites: %9%n%n\r\n          MetaDataReads: %10%n\r\n          MetaDataReadBytes: %11%n\r\n          MetaDataDiskReads: %12%n\r\n          MetaDataWrites: %13%n\r\n          MetaDataWriteBytes: %14%n\r\n          MetaDataDiskWrites: %15%n%n\r\n          MftReads: %16%n\r\n          MftReadBytes: %17%n\r\n          MftWrites: %18%n\r\n          MftWriteBytes: %19%n\r\n          Mft2Writes: %20%n\r\n          Mft2WriteBytes: %21%n\r\n          RootIndexReads: %22%n\r\n          RootIndexReadBytes: %23%n\r\n          RootIndexWrites: %24%n\r\n          RootIndexWriteBytes: %25%n\r\n          BitmapReads: %26%n\r\n          BitmapReadBytes: %27%n\r\n          BitmapWrites: %28%n\r\n          BitmapWriteBytes: %29%n\r\n          MftBitmapReads: %30%n\r\n          MftBitmapReadBytes: %31%n\r\n          MftBitmapWrites: %32%n\r\n          MftBitmapWriteBytes: %33%n\r\n          UserIndexReads: %34%n\r\n          UserIndexReadBytes: %35%n\r\n          UserIndexWrites: %36%n\r\n          UserIndexWriteBytes: %37%n\r\n          LogFileReads: %38%n\r\n          LogFileReadBytes: %39%n\r\n          LogFileWrites: %40%n\r\n          LogFileWriteBytes: %41%n\r\n          LogFileFull: %42%n\r\n          LogFileFullReasons:%n\r\n                    LF_LOG_SPACE: %43%n\r\n                    LF_DIRTY_PAGES: %44%n\r\n                    LF_OPEN_ATTRIBUTES: %45%n\r\n                    LF_TRANSACTION_DRAIN: %46%n\r\n                    LF_FASTIO_CALLBACK: %47%n\r\n                    LF_DEALLOCATED_CLUSTERS: %48%n\r\n                    LF_DEALLOCATED_CLUSTERS_MEM: %49%n\r\n                    LF_RECORD_STACK_CHECK: %50%n\r\n                    LF_DISMOUNT: %51%n\r\n                    LF_COMPRESSION: %52%n\r\n                    LF_SNAPSHOT: %53%n\r\n                    LF_MOUNT: %54%n\r\n                    LF_SHUTDOWN: %55%n\r\n                    LF_RECURSIVE_COMPRESSION: %56%n\r\n                    LF_TESTING: %57%n%n\r\n          DiskResourceFailure: %58%n\r\n          VolumeTrimCount: %59%n\r\n                    VolumeTrimTime (ms): %60%n\r\n                    VolumeTrimSize (KB): %61%n\r\n                    AvgVolumeTrimTime (ms): %62%n\r\n                    AvgVolumeTrimSize (KB): %63%n\r\n          VolumeTrimSkippedCount: %64%n\r\n                    VolumeTrimSkippedSize (KB): %65%n\r\n          FileLevelTrimCount: %66%n\r\n                    FileLevelTrimTime (ms): %67%n\r\n                    FileLevelTrimSize (KB): %68%n\r\n                    AvgFileLevelTrimTime (ms): %69%n\r\n                    AvgFileLevelTrimSize (KB): %70%n\r\n          NtfsFillStatInfoFromMftRecordCalledCount: %71%n\r\n          NtfsFillStatInfoFromMftRecordBailedBecauseOfAttributeListCount: %72%n\r\n          NtfsFillStatInfoFromMftRecordBailedBecauseOfNonResReparsePointCount: %73%n\r\n
0xb100009f | NTFS has successfully completed the %19 request in %20 ms when trying to %18 the volume size from %4 (MB) to %5 (MB).%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Device GUID: %6%n\r\n          Device manufacturer: %8%n\r\n          Device model: %10%n\r\n          Device revision: %12%n\r\n          Device serial number: %14%n\r\n          Bus type: %15%n%n\r\n          Adapter serial number: %17%n%n\r\n          Operation: %18%n\r\n                    Request Type: %19%n%n\r\n          Stage Durations:%n\r\n                    Stage 1. Verify input and calculate new volume size (ms): %21%n\r\n                    Stage 2. Set boundary and allocate/deallocate cluster (ms): %22%n\r\n                    Stage 3. Update bitmap (ms): %23%n\r\n
0xb10000a0 | NTFS has failed to complete the %19 request after %20 ms when trying to %18 the volume size from %4 (MB) to %5 (MB).%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Device GUID: %6%n\r\n          Device manufacturer: %8%n\r\n          Device model: %10%n\r\n          Device revision: %12%n\r\n          Device serial number: %14%n\r\n          Bus type: %15%n%n\r\n          Adapter serial number: %17%n%n\r\n          Operation: %18%n\r\n                    Request Type: %19%n%n\r\n          Stage Durations:%n\r\n                    Stage 1. Verify input and calculate new volume size (ms): %21%n\r\n                    Stage 2. Set boundary and allocate/deallocate cluster (ms): %22%n\r\n                    Stage 3. Update bitmap (ms): %23%n%n\r\n          Failure Stage: %24%n\r\n          Status Code: %25%n\r\n          Failure Reason: %26%n\r\n
0xb10000a1 | An operation has failed due to a file system limitation.%n%n\r\n          Reason: %1%n\r\n          Volume Id: %3%n\r\n          Volume Name: %4%n\r\n          File Path: %5%n\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xb10000f0 | File metadata optimization started.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb10000f1 | File metadata optimization completed.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb100012c | NTFS volume dismount has started.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb100012d | NTFS has sent volume dismount event notification and is waiting for the notifications to complete.\r\n
0xb100012e | The volume dismount event notification on the NTFS volume has completed.\r\n
0xb100012f | The NTFS volume has successfully dismounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb1000130 | The NTFS volume dismount failed.%n%n\r\n          Error:%1%n\r\n
0xb1000131 | NTFS failed to mount the volume.%n%n\r\n          Error: %1%n\r\n          Volume GUID: %2%n\r\n          Volume Name: %4%n%nGuidance:%nThe volume is recognized by NTFS but it is corrupted that NTFS could not mount it. Run CHKDSK /F to fix any errors on this volume, and then try accessing it.\r\n
0xb1000191 | Efs offloading initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000192 | Efs offloading read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000193 | Efs offloading write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000194 | Efs legacy initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000195 | Efs legacy read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000196 | Efs legacy write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb10001f4 | A process has created a USN journal on a volume.%n%n\r\n          Process: %1%n\r\n          Volume Id: %2%n\r\n          Volume Name: %4%n\r\n          Maximum Size: %5%n\r\n          Allocation Delta: %6%n\r\n
0xb10001f5 | A process has deleted a USN journal on a volume.%n%n\r\n          Process: %1%n\r\n          Volume Id: %2%n\r\n          Volume Name: %4%n\r\n
0xb1020094 | A %9 failed with %14.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          IO Size: %10 bytes%n\r\n          File offset: %11%n\r\n          %13 cluster(s) starting at cluster %12%n\r\n          Latency: %15 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %16%n\r\n          Device manufacturer: %18%n\r\n          Device model: %20%n\r\n          Device revision: %22%n\r\n          Device serial number: %24%n\r\n          Bus type: %25%n%n\r\n          Adapter serial number: %27%n\r\n
0xb1020095 | In the past %17 seconds we had IO failures.%nThis may indicate a failing disk.%n%n\r\n          High latency IO count: %18%n\r\n          Failed writes: %19%n\r\n          Failed reads: %20%n\r\n          Bad clusters relocated: %21%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %5%n\r\n          Device manufacturer: %7%n\r\n          Device model: %9%n\r\n          Device revision: %11%n\r\n          Device serial number: %13%n\r\n          Bus type: %14%n%n\r\n          Adapter serial number: %16%n\r\n
0xb1030092 | IO latency summary:%n%n\r\n          Volume Id: %2%n\r\n          Volume name: %4%n\r\n          Is boot volume: %5%n%n\r\n          Device GUID: %7%n\r\n          Device manufacturer: %9%n\r\n          Device model: %11%n\r\n          Device revision: %13%n\r\n          Device serial number: %15%n\r\n          Bus type: %16%n%n\r\n          Adapter serial number: %18%n%n\r\n          Max Acceptable IO Latency: %19 ms%n%n\r\n          Read/Write latency buckets (ns): [%20, %21, %22, %23, %24, %25, %26]%n\r\n          Trim latency buckets (ns): [%27, %28, %29, %30, %31, %32, %33]%n\r\n          Flush latency buckets (ns): [%34, %35, %36, %37, %38, %39, %40]%n%n\r\n          Interval duration: %42 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %43%n\r\n                    Total bytes: %44%n\r\n                    Avg latency: %45 ns%n%n\r\n          Non-cached writes:%n\r\n                    IO count: %46%n\r\n                    Total bytes: %47%n\r\n                    Avg latency: %48 ns%n%n\r\n          File flushes:%n\r\n                    IO count: %49%n\r\n                    Avg latency: %50 ns%n%n\r\n          Directory flushes:%n\r\n                    IO count: %51%n\r\n                    Avg latency: %52 ns%n%n\r\n          Volume flushes:%n\r\n                    IO count: %53%n\r\n                    Avg latency: %54 ns%n%n\r\n          File level trims:%n\r\n                    IO count: %55%n\r\n                    Total bytes: %56%n\r\n                    Extents count: %57%n\r\n                    Avg latency: %58 ns%n%n\r\n          Volume trims:%n\r\n                    IO count: %59%n\r\n                    Total bytes: %60%n\r\n                    Extents count: %61%n\r\n                    Avg latency: %62 ns%n%n\r\n          VCB exclusive resource acquires:%n\r\n                    Acquire count: %71%n\r\n                    Max wait duration: %72 ms%n\r\n                    Avg wait duration: %73 ms%n\r\n                    Max hold duration: %74 ms%n\r\n                    Avg hold duration: %75 ms%n\r\n                    Max combined duration: %76 ms%n\r\n                    Avg combined duration: %77 ms%n%n\r\n          For more details see the details tab.%n\r\n
0xb1030093 | An IO took more than %5 ms to complete:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          File offset: %12%n\r\n          IO Type: %10%n\r\n          IO Size: %11 bytes%n\r\n          %15 cluster(s) starting at cluster %14%n\r\n          Latency: %13 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %16%n\r\n          Device manufacturer: %18%n\r\n          Device model: %20%n\r\n          Device revision: %22%n\r\n          Device serial number: %24%n\r\n          Bus type: %25%n%n\r\n          Adapter serial number: %27%n\r\n
0xb1040091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %2%n\r\n          Volume name: %4%n\r\n          Is boot volume: %5%n%n\r\n          Device GUID: %7%n\r\n          Device manufacturer: %9%n\r\n          Device model: %11%n\r\n          Device revision: %13%n\r\n          Device serial number: %15%n\r\n          Bus type: %16%n%n\r\n          Adapter serial number: %18%n%n\r\n          Max Acceptable IO Latency: %19 ms%n%n\r\n          Read/Write latency buckets (ns): [%20, %21, %22, %23, %24, %25, %26]%n\r\n          Trim latency buckets (ns): [%27, %28, %29, %30, %31, %32, %33]%n\r\n          Flush latency buckets (ns): [%34, %35, %36, %37, %38, %39, %40]%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n
0xd1000026 | Write: NonPaging, NonCached, Async\r\n
0xd1000027 | Write: NonPaging, NonCached, Sync\r\n
0xd1000028 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd1000029 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd100002a | Write: NonPaging, Cached, Async\r\n
0xd100002b | Write: NonPaging, Cached, Sync\r\n
0xd100002c | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd100002d | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd100002e | Write: Paging, NonCached, Async\r\n
0xd100002f | Write: Paging, NonCached, Sync\r\n
0xd1000030 | Write: Paging, NonCached, Async, Writethrough\r\n
0xd1000031 | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd1000032 | Read: NonPaging, NonCached, Async\r\n
0xd1000033 | Read: NonPaging, NonCached, Sync\r\n
0xd1000034 | Read: NonPaging, Cached, Async\r\n
0xd1000035 | Read: NonPaging, Cached, Sync\r\n
0xd1000036 | Read: Paging, NonCached, Async\r\n
0xd1000037 | Read: Paging, NonCached, Sync\r\n
0xd1000038 | read\r\n
0xd1000039 | write\r\n
0xd100003a | <unknown>\r\n
0xd100003b | SCSI\r\n
0xd100003c | ATAPI\r\n
0xd100003d | ATA\r\n
0xd100003e | 1394\r\n
0xd100003f | SSA\r\n
0xd1000040 | Fibre\r\n
0xd1000041 | USB\r\n
0xd1000042 | RAID\r\n
0xd1000043 | iSCSI\r\n
0xd1000044 | SAS\r\n
0xd1000045 | SATA\r\n
0xd1000046 | SD\r\n
0xd1000047 | MMC\r\n
0xd1000048 | Virtual\r\n
0xd1000049 | File backed virtual\r\n
0xd100004a | Spaces\r\n
0xd100004b | NVMe\r\n
0xd100004c | Unknown\r\n
0xd100004d | Internal attribute stream was deleted\r\n
0xd100004e | Stream was purged\r\n
0xd100004f | Configuration changed\r\n
0xd1000050 | VCB\r\n
0xd1000051 | Extend\r\n
0xd1000052 | Shrink\r\n
0xd1000053 | Extend\r\n
0xd1000054 | Prepare\r\n
0xd1000055 | Shrink\r\n
0xd1000056 | Abort\r\n
0xd1000057 | Unknown\r\n
0xd1000058 | File size exceeds the maximum allowed by a volume\r\n
0xd1000059 | File size exceeds a system limit\r\n
0xd100005a | A file record could not be split\r\n
0xd100005b | Bitmap size exceeds a system limit\r\n
0xd100005c | USN journal size exceeds a system limit\r\n

### 10.0.22000.41

Message identifier | Message string
--- | ---
0x00000037 | A corruption was discovered in the file system structure on volume %1.%n%n%8\r\n
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.%nPlease run the chkdsk utility on the volume %2.\r\n
0x00000084 | Too many repair events have occurred in a short period of time.%nTemporarily suspending posting of further repair events.\r\n
0x00000085 | Skipped posting of %1 repair events.  Repair event posting will now be resumed.%n\r\nHere are the skipped posting repair events count by repair verbs:%n\r\nBadFRS:            %2%n\r\nOrphanChildFRS:    %3%n\r\nBadClusters:       %4%n\r\nBadFreeClusters:   %5%n\r\nCrossLink:         %6%n\r\nSDEntry:           %7%n\r\nInvalidSecurityId: %8%n\r\nIndexAttribute:    %9%n\r\nIndexSubtree:      %10%n\r\nIndexOffset:       %11%n\r\nIndexEntry:        %12%n\r\nIndexOrder:        %13%n\r\nConnect:           %14%n\r\nBreakCycle:        %15%n\r\nFRSAllocate:       %16%n\r\nOthers:            %17%n\r\n
0x00001000 | No-Op\r\n
0x00001001 | Force Full Chkdsk\r\n
0x00001002 | Force Proactive Scan\r\n
0x00001003 | Bad FRS\r\n
0x00001004 | Orphan Child FRS\r\n
0x00001005 | Bad Clusters\r\n
0x00001006 | Bad Free Clusters\r\n
0x00001007 | Cross-Link\r\n
0x00001008 | SD Entry\r\n
0x00001009 | Invalid Security Id\r\n
0x0000100a | Index Attribute\r\n
0x0000100b | Index Subtree\r\n
0x0000100c | Index Offset\r\n
0x0000100d | Index Entry\r\n
0x0000100e | Index Order\r\n
0x0000100f | Connect\r\n
0x00001010 | Break Cycle\r\n
0x00001011 | FRS Allocate\r\n
0x00001012 | Index Sort\r\n
0x00001013 | Index Cycle\r\n
0x00001100 | File System Driver\r\n
0x00001101 | Proactive Scanner\r\n
0x00001102 | User Application\r\n
0x00001200 | Read Only Volume\r\n
0x00001201 | Self Healed\r\n
0x00001202 | Spot Corruption Handling Disabled\r\n
0x00001203 | Spot Verifier Bypassed On Critical\r\n
0x00001204 | Spot Verifier Bypassed On Error\r\n
0x00001205 | Sent To Spot Fixer\r\n
0x00001206 | Spot Fixer Bypassed On Critical\r\n
0x00001207 | Spot Fixer Bypassed On Error\r\n
0x00001208 | Duplicate\r\n
0x00001209 | Malformed\r\n
0x0000120a | Unsupported\r\n
0x0000120b | Verified\r\n
0x0000120c | False Positive\r\n
0x0000120d | Superseded\r\n
0x0000120e | Purged\r\n
0x0000120f | Pseudo Verb\r\n
0x00001210 | Unexpected Corruption\r\n
0x00001211 | Volume Not Available\r\n
0x00001300 | Maintenance\r\n
0x00001301 | Normal\r\n
0x00001302 | Critical\r\n
0x00001f00 | <unable to determine file name>\r\n
0x00002010 | The exact nature of the corruption is unknown.  The file system structures need to be scanned and fixed offline.\r\n
0x00002020 | The exact nature of the corruption is unknown.  The file system structures need to be scanned online.\r\n
0x00002030 | The Master File Table (MFT) contains a corrupted file record.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".\r\n
0x00002040 | The Master File Table (MFT) contains a child file record segment that is not reachable from its base file record segment.  The file reference number is 0x%1!0I64x!.\r\n
0x00002050 | A bad cluster was discovered while accessing file data.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002060 | A bad cluster was discovered outside of any existing file on the volume.  The bad cluster is located at Lcn 0x%1!0I64x!.\r\n
0x00002070 | Two files were found to occupy the same location on the volume.  The owning file reference number is 0x%1!0I64x!.  The name of the owning file is "%2!wZ!".  The owning extent containing the bad cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.  The crossing file reference number is 0x%5!0I64x!.  The name of the crossing file is "%6!wZ!".  The crossing extent containing the bad cluster is located at Vcn 0x%7!0I64x!.\r\n
0x00002080 | A corruption was found in the security descriptor stream.  The corrupted entry is at offset 0x%1!I64x!.\r\n
0x00002090 | A file was found to have a security ID that is not described in the security file.  The invalid security ID is 0x%1!lx!.  The file reference number is 0x%2!0I64x!.  The name of the file is "%3!wZ!".  There may be additional files on the volume that also refer to this invalid security ID.\r\n
0x000020a0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020b0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020c0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted index block is located at Vcn 0x%4!0I64x!, Lcn 0x%5!0I64x!.  The corruption begins at offset %6!lu! within the index block.\r\n
0x000020d0 | A corruption was found in a file system index structure.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020e0 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".\r\n
0x000020f0 | A file on the volume is no longer reachable from its parent directory.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The parent index attribute is "%3!wZ!".  The file reference number of the file that needs to be reconnected is 0x%4!0I64x!.  There may be additional files on the volume that also need to be reconnected to this parent directory.\r\n
0x00002100 | A cycle was found in the directory hierarchy on the volume, which can only be fixed by severing a parent-child relationship.  The parent file reference number is 0x%1!0I64x!.  The name of the parent directory is "%2!wZ!".  The child file reference number is 0x%3!0I64x!.  The name of the child directory is "%4!wZ!".  There may be additional directories on the volume that also participate in this cycle.\r\n
0x00002110 | A cluster was found to be used by a file but not marked as used in the volume bitmap.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The unallocated cluster is located at Vcn 0x%3!0I64x!, Lcn 0x%4!0I64x!.\r\n
0x00002120 | A file system index structure contains entries that violate ordering rules.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The corrupted subtree is rooted at entry number %4!lu! of the index block located at Vcn 0x%5!0I64x!.\r\n
0x00002130 | A file system index structure contains a cycle.  The file reference number is 0x%1!0I64x!.  The name of the file is "%2!wZ!".  The corrupted index attribute is "%3!wZ!".  The cycle includes %4!lu! index blocks starting at Vcn 0x%5!0I64x! and ending at Vcn 0x%6!0I64x!.\r\n
0x00004000 | $UNUSED\r\n
0x00004001 | $STANDARD_INFORMATION\r\n
0x00004002 | $ATTRIBUTE_LIST\r\n
0x00004003 | $FILE_NAME\r\n
0x00004004 | $OBJECT_ID\r\n
0x00004005 | $SECURITY_DESCRIPTOR\r\n
0x00004006 | $VOLUME_NAME\r\n
0x00004007 | $VOLUME_INFORMATION\r\n
0x00004008 | $DATA\r\n
0x00004009 | $INDEX_ROOT\r\n
0x0000400a | $INDEX_ALLOCATION\r\n
0x0000400b | $BITMAP\r\n
0x0000400c | $REPARSE_POINT\r\n
0x0000400d | $EA_INFORMATION\r\n
0x0000400e | $EA\r\n
0x00004010 | $LOGGED_UTILITY_STREAM\r\n
0x00005000 | The file size is 0x%1!0I64x!. The maximum size for the volume is 0x%2!0I64x!.\r\n
0x00005001 | The bitmap size is 0x%1!0I64x!. The system limit is 0x%2!0I64x!.\r\n
0x00005002 | The USN journal size is 0x%1!0I64x!. The system limit is 0x%2!0I64x!.\r\n
0x00005003 | The file size is 0x%1!0I64x!. The system limit is 0x%2!0I64x!.\r\n
0x000061a8 | Clearing the in use bit for file record 0x%1.\r\n
0x000061a9 | Repairing the sequence number for file record 0x%1.\r\n
0x000061aa | Repairing the first free byte for file record 0x%1.\r\n
0x000061ab | Repairing the segment number for file record 0x%1.\r\n
0x000061ac | Repairing the file attributes for file record 0x%1.\r\n
0x000061ad | Deleting attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x000061ae | Repairing the flags for file record 0x%1.\r\n
0x000061af | Adding attribute of type code 0x%1 for file record 0x%2.\r\n
0x000061b0 | Start repair on %2/%3/%1 at %4:%5:%6:%7%\r\n
0x000061b1 | End repair on %2/%3/%1 at %4:%5:%6:%7\r\n
0x000061b2 | Marked file record %1 as in use in MFT bitmap.\r\n
0x000061b3 | Security Id 0x%2 is invalid in file record segment 0x%1.\r\nIt will be replaced with an administrator only Security Id.\r\n
0x000061b4 | Marked %5 clusters in attribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000061b5 | Processing repair verb BadFrs: 0x%1\r\nFlags: 0x%2, 0x%3\r\n
0x000061b6 | Processing repair verb InvalidSid: 0x%1, 0x%2, 0x%3,,, 0x%4\r\nFlags: 0x%5, 0x%6\r\n
0x000061b7 | Processing repair verb FrsAllocate: 0x%1, 0x%2, "%3", 0x%4, 0x%5, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b8 | Processing repair verb Connect: 0x%1, "%2", 0x%3, 0x%4, 0x%5,,, 0x%6\r\nFlags: 0x%7, 0x%8\r\n
0x000061b9 | Processing repair verb IndexEntry: 0x%1, "%2", "%3"\r\nFlags: 0x%4, 0x%5\r\n
0x000061ba | Processing repair verb OrphanChildFrs: 0x%1, 0x%2,,, 0x%3\r\nFlags: 0x%4, 0x%5\r\n
0x000061c6 | This repair generated too many messages.  %1 messages were skipped.\r\n
0x000061c7 | Swapping attribute of type code 0x%1 and instance tag 0x%2 with\r\nattribute of type code 0x%3 and instance tag 0x%4 for file record 0x%5.\r\n
0x00006590 | Deleting corrupt file record segment 0x%1.\r\n
0x000065aa | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas in use by file 0x%1 in the volume bitmap.\r\n
0x000065ca | Correcting a minor error in file 0x%1.\r\n
0x000065ce | Marking cluster starting at VCN 0x%5 with LCN 0x%6 for 0x%7 clusters in\r\nattribute %4 of type code 0x%2 and instance tag 0x%3\r\nas not in use by file 0x%1 in the volume bitmap.\r\n
0x000065d1 | Deleting index entry %3 in index 0x%2 of file 0x%1.\r\n
0x000065e4 | Deleting an index entry from index 0x%2 of file 0x%1.\r\n
0x000065f5 | Inserting an index entry %3 into index 0x%2 of file 0x%1.\r\n
0x0000660f | Inserting an index entry with Id 0x%3 into index 0x%2 of file 0x%1.\r\n
0x00006784 | Change file name flags from 0x%3 to 0x%4 for\r\nfile name instance 0x%2 in file 0x%1.\r\n
0x00006978 | Volume has 0x%1 file record segments which is more than 32 bits.\r\n
0x00006979 | The file name index present bit is not set for file 0x%1.\r\n
0x0000697a | The view index present bit is not set for file 0x%1.\r\n
0x0000697b | The system file bit is not set for file 0x%1.\r\n
0x0000697c | The %2 index is missing from file 0x%1.\r\n
0x0000697d | EA Information is incorrect.\r\n                 Actual          On Disk\r\nPackedEaSize      0x%1            0x%4\r\nNeedEaCount       0x%2            0x%5\r\nUnpackedEaSize    0x%3            0x%6\r\n
0x0000697e | The EA INFORMATION attribute is not consistency with the EA DATA attribute\r\nfor file 0x%1.  EA INFORMATION equals 0x%2 while EA DATA equals 0x%3.\r\n
0x0000697f | The EA INFORMATION is not readable for file 0x%1.\r\n
0x00006980 | The EA INFORMATION size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006981 | The EA DATA is not readable for file 0x%1.\r\n
0x00006982 | The EA DATA size, 0x%2, in file 0x%1 is incorrect.\r\nThe expected size is 0x%3.\r\n
0x00006983 | %1%2\r\n
0x00006984 | Corrupt EA set for file 0x%1.  The remaining length, 0x%2,\r\nis too small.\r\n
0x00006985 | Corrupt EA set for file 0x%1.  The unpacked total length, 0x%2,\r\nis larger than the total data length, 0x%3.\r\n
0x00006986 | Corrupt EA set for file 0x%1.  The EA name is of length 0x%2.\r\n
0x00006987 | Corrupt EA set for file 0x%1.  The unpacked length, 0x%2,\r\nis not the same as the record length, 0x%3.\r\n
0x00006988 | The EA Information value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006989 | The EA total packed length, 0x%2, is too large in file 0x%1.\r\n
0x0000698a | The second MFT starting LCN in the boot sector is incorrect.\r\nThe actual value is 0x%2 while the expected value is 0x%1.\r\n
0x0000698b | The reparse point length, 0x%1, has exceeded a maximum of 0x%2.\r\n
0x0000698c | The reparse point length, 0x%1, is less than a minimum of 0x%2.\r\n
0x0000698d | Unable to read reparse point data buffer.\r\n
0x0000698e | Only 0x%1 bytes returned from a read of 0x%d bytes\r\nof the reparse data buffer.\r\n
0x0000698f | ReparseDataLength, 0x%1, inconsistence with the attribute length 0x%2.\r\n
0x00006990 | Reparse Tag, 0x%1, is a reserved tag.\r\n
0x00006992 | File 0x%1 has bad reparse point attribute.\r\n
0x00006993 | Both reparse point and EA INFORMATION attributes exist in file 0x%1.\r\n
0x00006994 | The attribute definition table length, 0x%1, is not divisible by 0x%2.\r\n
0x00006995 | Unable to find child frs 0x%1 with sequence number 0x%2.\r\n
0x00006996 | Unable to locate attribute of type 0x%1, lowest vcn 0x%2,\r\ninstance tag 0x%3 in file 0x%4.\r\n
0x00006997 | The is an attribute list attribute within the attribute list in file 0x%1.\r\n
0x00006998 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nand instance tag 0x%3 in file 0x%4.\r\n
0x00006999 | The lowest vcn, 0x%2, is not zero for attribute of type 0x%1\r\nin file 0x%3.\r\n
0x0000699a | The first attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699b | The attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be resident.\r\n
0x0000699c | The attributes with instance tags 0x%2 and 0x%4 have different\r\ntype codes 0x%1 and 0x%3 respectively in file 0x%5.\r\n
0x0000699d | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have non-contiguous VCN numbers 0x%3 and 0x%5\r\nrespectively in file 0x%6.\r\n
0x0000699e | The attributes with same type code 0x%1 but different instance tags\r\n0x%2 and 0x%4 have different names %3 and %5\r\nrespectively in file 0x%6.\r\n
0x0000699f | The attribute of type 0x%1 and instance tag 0x%2 in file 0x%5\r\nhas allocated length of 0x%3 instead of 0x%4.\r\n
0x000069a0 | The attribute of type 0x%1 in file 0x%4 has allocated length\r\nof 0x%2 instead of 0x%3.\r\n
0x000069a1 | The file attributes flag 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x000069a2 | The sequence number 0x%1 in file 0x%2 is incorrect.\r\n
0x000069a3 | The total allocated size 0x%3 of attribute of type 0x%1 and instance\r\ntag 0x%2 in file 0x%5 is incorrect.  The expected value is %4.\r\n
0x000069a4 | Read failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a5 | Incorrect read at offset 0x%1 for 0x%3 bytes but got 0x%2 bytes.\r\n
0x000069a6 | Write failure with status 0x%1 at offset 0x%2 for 0x%3 bytes.\r\n
0x000069a7 | Incorrect write at offset 0x%1 for 0x%3 bytes but wrote 0x%2 bytes.\r\n
0x000069a8 | The data written out is different from what is being read back\r\nat offset 0x%1 for 0x%2 bytes.\r\n
0x000069a9 | The file 0x%1 belongs to parent 0x%3 but got 0x%2 as parent.\r\n
0x000069aa | The file 0x%1 has file name %2 when it should be %3.\r\n
0x000069ab | The multi-sector header with total size 0x%1, USA offset 0x%2,\r\nand USA count 0x%3 is incorrect.\r\n
0x000069ac | The USA check value, 0x%2, at block 0x%1 is incorrect.\r\nThe expected value is 0x%3.\r\n
0x000069ad | Unable to query LCN from VCN 0x%2 for attribute of type 0x%1.\r\n
0x000069ae | Attribute record of type 0x%1 and instance tag 0x%2 is cross linked\r\nstarting at 0x%3 for possibly 0x%4 clusters.\r\n
0x000069af | Attribute record of type 0x%1 is cross linked starting at\r\ncluster 0x%2 for possibly 0x%3 clusters.\r\n
0x000069b0 | The attribute list in file 0x%1 does not contain\r\nstandard information attribute.\r\n
0x000069b1 | The attribute list in file 0x%1 indicates the standard information\r\nattribute is outside the base file record segment.\r\n
0x000069b2 | The index root %2 is missing in file 0x%1.\r\n
0x000069b3 | The index bitmap %2 is missing in file 0x%1.\r\n
0x000069b4 | The index bitmap %2 in file 0x%1 is incorrect.\r\n
0x000069b5 | The index bitmap %2 is present but there is no corresponding\r\nindex allocation attribute in file 0x%1.\r\n
0x000069b6 | The length, 0x%2, of the root index %1 in file 0x%4\r\nis too small.  The minimum length is 0x%3.\r\n
0x000069b7 | The root index %1 in file 0x%3 is incorrect.\r\nThe expected name is %2.\r\n
0x000069b8 | The collation rule 0x%3 for index root %1 in file 0x%2\r\nis incorrect.  The expected value is 0x%4.\r\n
0x000069b9 | Breaking the parent 0x%1 and child 0x%2\r\nfile relationship.  This also makes the child an orphan.\r\n
0x000069ba | The index attribute of type 0x%2 for index root %1\r\nin file 0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069bb | The index %1 is not a known quota index in file 0x%2.\r\n
0x000069bc | The index %1 is not a known security index in file 0x%2.\r\n
0x000069bd | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not recognized.\r\n
0x000069be | The index attribute of type 0x%2 for index root %1\r\nin file 0x%3 is not indexable.\r\n
0x000069bf | The bytes per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c0 | The clusters per index buffer, 0x%2, for index root %1 in file\r\n0x%4 is incorrect.  The expected value is 0x%3.\r\n
0x000069c1 | The index allocation value length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c2 | The index allocation allocated length, 0x%2, for index %1 in file\r\n0x%4 is not in multiple of 0x%3.\r\n
0x000069c3 | The first free byte, 0x%2, and bytes available, 0x%3, for\r\nroot index %1 in file 0x%4 are not equal.\r\n
0x000069c4 | The index entry offset, 0x%3, of index %1 and VCN 0x%2\r\nin file 0x%4 is incorrect.\r\n
0x000069c5 | The index entry offset, 0x%2, of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069c6 | The bytes available, 0x%2, in index header for index %1 in file\r\n0x%4 is not equal to 0x%3.\r\n
0x000069c7 | The index header for index %1 and VCN 0x%2 in file 0x%3\r\nis not marked as index node.\r\n
0x000069c8 | The VCN 0x%2 of index %1 in file 0x%3 is incorrect.\r\n
0x000069c9 | The index bitmap for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069ca | The VCN 0x%2 of index %1 in file 0x%3 is already in use.\r\n
0x000069cb | The index allocation for index %1 in file 0x%2 is invalid or missing.\r\n
0x000069cc | The multi-sector header signature for VCN 0x%2 of index %1\r\nin file 0x%3 is incorrect.\r\n
0x000069cd | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%5 is below 0x%4.\r\n
0x000069ce | The VCN 0x%2 of index %1 in file 0x%4 is inconsistence with\r\nthe VCN 0x%3 stored inside the index buffer.\r\n
0x000069cf | The bytes per block, 0x%3, read from index buffer of VCN 0x%2\r\nof index %1 in file 0x%4 is incorrect.\r\n
0x000069d0 | The USA offset 0x%3 of VCN 0x%2 of index %1\r\nin file 0x%4 is incorrect.\r\n
0x000069d1 | The USA size 0x%3 of VCN 0x%2 of index %1 in file\r\n0x%5 is incorrect.  The expected value is 0x%4.\r\n
0x000069d2 | The index header of index %1 in file 0x%2\r\nis marked as index node when it should not.\r\n
0x000069d3 | The first free byte, 0x%2, in index header of index %1\r\nin file 0x%4 is not equal to 0x%3.\r\n
0x000069d4 | Unable to query the name of a file name index entry of length 0x%3\r\nof index %2 in file 0x%4 with parent 0x%1.\r\n
0x000069d5 | Index entry %2 of index 0x%1 points to unused or reused file 0x%3.\r\n
0x000069d6 | An index entry of index 0x%1 points to unused or reused file 0x%2.\r\n
0x000069d7 | The file 0x%4 pointed to by index entry %3 of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d8 | The file 0x%3 pointed to by an index entry of index %2 with\r\nparent file 0x%1 is not a base file record segment.\r\n
0x000069d9 | Unable to locate the file name attribute of index entry %3\r\nof index %2 with parent 0x%1 in file 0x%4.\r\n
0x000069da | Unable to locate the file name attribute of an index entry\r\nof index %2 with parent 0x%1 in file 0x%3.\r\n
0x000069db | The object id index entry in file 0x%1 points to file 0x%2\r\nbut the file has no object id in it.\r\n
0x000069dc | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069dd | The object id in index entry in file 0x%1 is incorrect.\r\nThe entry points to file 0x%2.\r\n
0x000069de | The parent 0x%2 in an object id index entry in file 0x%1\r\nis incorrect.  The correct value is 0x%3.\r\n
0x000069df | The object id in file 0x%2 already existed in the object\r\nid index in file 0x%1.\r\n
0x000069e0 | The object id in file 0x%2 does not appear in the object\r\nid index in file 0x%1.\r\n
0x000069e1 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not a base file record segment.\r\n
0x000069e2 | The reparse tag 0x%2 of reparse point index entry in file 0x%1\r\nis incorrect.  The correct reparse tag in file 0x%4 is 0x%3.\r\n
0x000069e3 | The parent 0x%2 in the reparse point index entry with tag 0x%4\r\nin file 0x%1 is incorrect.  The correct value is 0x%3.\r\n
0x000069e4 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nbut the file has no reparse point in it.\r\n
0x000069e5 | The reparse point in file 0x%2 does not appear in\r\nthe reparse point index in file 0x%1.\r\n
0x000069e6 | The file name index present bit is set in file 0x%1\r\nbut there is no file name index.\r\n
0x000069e7 | The root index %2 in file 0x%1 is missing or invalid.\r\n
0x000069e8 | The index entry length 0x%1 is incorrect.  The maximum value is 0x%2.\r\n
0x000069e9 | The index entry attribute length 0x%2 of index entry type 0x%1\r\nis incorrect.  The correct length is 0x%3.\r\n
0x000069ea | The index entry data offset 0x%1 and length 0x%2 is\r\ninconsistence with the index entry length 0x%3.\r\n
0x000069eb | The index entry length is incorrect for index entry type 0x%1.\r\n
0x000069ec | The index entry length is too small for index entry type 0x%1.\r\n
0x000069ed | The volume information attribute is missing from file 0x%1.\r\n
0x000069ee | The attribute record length 0x%1 is too small for attribute of\r\ntype 0x%3 and instance tag 0x%4.  The minimum value is 0x%2.\r\n
0x000069ef | The attribute form code 0x%1 is invalid for attribute of type 0x%2\r\nand instance tag 0x%3.\r\n
0x000069f0 | The attribute of type 0x%1 and instance tag 0x%2 should be resident.\r\n
0x000069f1 | The standard information attribute length 0x%1 is incorrect.\r\nThe expected value is 0x%2, 0x%3, or 0x%4.\r\n
0x000069f2 | Attribute name is not allowed for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x000069f3 | The attribute of type 0x%1 and instance tag 0x%2 should not be resident.\r\n
0x000069f4 | The attribute name offset for attribute of type 0x%1\r\nand instance tag 0x%2 is incorrect.\r\n
0x000069f5 | The attribute name for attribute of type 0x%1 and instance tag 0x%2\r\ncontains unicode NULL.\r\n
0x000069f6 | Unknown attribute of type 0x%1 and instance tag 0x%2.\r\n
0x000069f7 | The attribute of type 0x%1 and instance tag 0x%2 should not be indexed.\r\n
0x000069f8 | The attribute of type 0x%1 and instance tag 0x%2 should be indexed.\r\n
0x000069f9 | The indexable attribute of type 0x%1 and instance tag 0x%2\r\nshould not have name.\r\n
0x000069fa | The attribute of type 0x%1 and instance tag 0x%2 should have a name.\r\n
0x000069fb | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x000069fc | The attribute length 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is too big.  The maximum value is 0x%2.\r\n
0x000069fd | The resident attribute for attribute of type 0x%4 and instance\r\ntag 0x%5 is incorrect.  The attribute has value of length 0x%1,\r\nand offset 0x%2.  The attribute length is 0x%3.\r\n
0x000069fe | The resident attribute name is colliding with the resident value for attribute\r\nof type 0x%4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the attribute value offset is 0x%3.\r\n
0x000069ff | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 exceeded the attribute length 0x%2.\r\n
0x00006a00 | The mapping pairs offset 0x%1 for attribute of type 0x%3 and instance\r\ntag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a01 | The attribute name is colliding with the mapping pairs for attribute\r\nof type %4 and instance tag 0x%5.  The attribute name offset is\r\n0x%2, length 0x%1, and the mapping pairs offset is 0x%3.\r\n
0x00006a02 | The attribute of type 0x%2 and instance tag 0x%3 in file 0x%4\r\nhas bad mapping pairs at attribute offset 0x%1.\r\n
0x00006a03 | Unable to initialize an extent list for attribute type 0x%1 with\r\ninstance tag 0x%2.\r\n
0x00006a04 | The highest VCN 0x%1 of attribute of type 0x%3 and instance\r\ntag 0x%4 is incorrect.  The expected value is 0x%2.\r\n
0x00006a05 | The non resident attribute of type 0x%4 and instance tag 0x%5 is\r\ninconsistent.  The valid data length is 0x%1, file size 0x%2, and\r\nallocated length 0x%3.\r\n
0x00006a06 | The non resident attribute of type 0x%4 is inconsistent.  The valid data\r\nlength is 0x%1, file size 0x%2, and allocated length 0x%3.\r\n
0x00006a07 | The allocated length 0x%1 is not in multiple of 0x%2 for attribute\r\nof type 0x%3 and instance tag 0x%4.\r\n
0x00006a08 | The file name value length 0x%1 for attribute of type 0x%3 with\r\ninstance tag 0x%4 is too small.  The minimum value is 0x%2.\r\n
0x00006a09 | The attribute of type 0x%2 and instance tag 0x%3 is inconsistence.\r\nThe attribute value length is 0x%1.\r\n
0x00006a0a | The file name length is zero for attribute of type 0x%1\r\nand instance tag 0x%2.\r\n
0x00006a0b | The file name in file name value in attribute of type 0x%1 and instance\r\ntag %2 contains invalid character.\r\n
0x00006a0c | The multi-sector header signature in file 0x%1 is incorrect.\r\n
0x00006a0d | The USA offset 0x%1 in file 0x%3 is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a0e | The file record segment size 0x%1 is invalid in file 0x%2.\r\n
0x00006a0f | The USA offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a10 | The USA size 0x%1 in file 0x%3 is incorrect.\r\nThe expected value is 0x%2.\r\n
0x00006a11 | The first attribute offset 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a12 | The bytes available, 0x%1, in the file record segment header for\r\nfile 0x%3 is incorrect.  The expected value is 0x%2.\r\n
0x00006a13 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%3\r\nis already in use.\r\n
0x00006a14 | The instance tag 0x%2 of attribute of type 0x%1 in file 0x%4\r\nis too large.  The instance tag should be less than 0x%3.\r\n
0x00006a15 | The standard information attribute in file 0x%1 is missing.\r\n
0x00006a16 | The attribute record offset 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a17 | The record length of attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 should not be zero.\r\n
0x00006a18 | The record length 0x%1 of attribute of type 0x%2 and\r\ninstance tag 0x%3 in file 0x%4 is not aligned.\r\n
0x00006a19 | The record length 0x%1 is too large for attribute of type 0x%3\r\nand instance tag 0x%4 in file 0x%5.  The maximum value is 0x%2.\r\n
0x00006a1a | The first free byte, 0x%1, in file 0x%4 is incorrect.  The number of\r\nbytes free in the file record segment is 0x%2 and the total length\r\nis 0x%3.\r\n
0x00006a1b | The attribute of type 0x%1 and instance tag 0x%2 should be after\r\nattribute of type 0x%3 and instance tag 0x%4 in file 0x%5.\r\n
0x00006a1c | All attribute of type 0x%1 and instance tag 0x%2 should be indexed\r\nin file 0x%5.\r\n
0x00006a1d | Two identical attributes of type 0x%1 and instance tag 0x%2 are\r\nin file 0x%3.\r\n
0x00006a1e | The file name index present bit in file 0x%1 should not be set.\r\n
0x00006a20 | The sparse flag in the standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a21 | The sparse flag in the standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a22 | The old encrypted flag is being replaced by the new encrypted flag\r\nin file 0x%1.\r\n
0x00006a23 | The encrypted flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a24 | The reparse flag in standard information attribute in file 0x%1\r\nis not set.\r\n
0x00006a25 | The reparse flag in standard information attribute in file 0x%1\r\nshould not be set.\r\n
0x00006a26 | There are more than one NTFS file name attribute in file 0x%1.\r\n
0x00006a27 | The file name attributes in file 0x%3 has different parents.\r\nThe DOS name has 0x%1 as parent.  The NTFS name has 0x%2 as parent.\r\n
0x00006a28 | There are more than one DOS file name attribute in file 0x%1.\r\n
0x00006a29 | The DOS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a2a | There is no NTFS file name attribute in file 0x%1.\r\n
0x00006a2b | There is no DOS file name attribute in file 0x%1.\r\n
0x00006a2c | The DOS and NTFS file name attributes in file 0x%1 are identical.\r\n
0x00006a2d | Unable to setup the attribute list in file 0x%1.\r\n
0x00006a2e | The attribute type 0x%1 with name %2 in file 0x%3 is missing.\r\n
0x00006a2f | The attribute of type 0x%1 in file 0x%2 is missing.\r\n
0x00006a30 | The unnamed data attribute in file 0x%1 is missing.\r\n
0x00006a31 | The attribute list in file 0x%1 is missing.\r\n
0x00006a32 | The length, 0x%3, of the attribute list entry with attribute of type\r\n0x%1 and instance tag 0x%2 in file 0x%4 is not aligned.\r\n
0x00006a33 | The attribute list entry with attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%6 is incorrect.  The attribute list entry name length is 0x%3,\r\nand offset 0x%4.  The attribute list length is 0x%5.\r\n
0x00006a34 | The attribute name offset 0x%3 of attribute list entry with attribute of\r\ntype 0x%1 and instance tag 0x%2 in file 0x%5 is too small.\r\nThe minimum value is 0x%4.\r\n
0x00006a35 | The attribute list length 0x%2 in file 0x%3 is incorrect.\r\nThe expected value is 0x%1.\r\n
0x00006a36 | The extent list of the attribute list is crossed linked at 0x%1\r\nfor possibly 0x%2 clusters in file 0x%3.\r\n
0x00006a37 | The attribute list entry with attribute of type 0x%1 and instance tag\r\n0x%2 should be after attribute of type 0x%3 and instance tag 0x%4.\r\n
0x00006a38 | Two identical attribute list entries of type 0x%1 and instance tag 0x%2\r\nare found.\r\n
0x00006a39 | The attribute length 0x%3 of attribute of type 0x%1 and name %2 in\r\nfile 0x%5 is too small.  The minimum value is 0x%4.\r\n
0x00006a3a | The sparse flag of attribute of type 0x%1 and name %2 in file\r\n0x%3 is not set.\r\n
0x00006a3b | The USN Journal offset 0x%1 in file 0x%2 is not at a page boundary.\r\n
0x00006a3c | The USN Journal length 0x%1 in file 0x%3 is too large.\r\nThe maximum value is 0x%2.\r\n
0x00006a3d | The USN Journal length 0x%1 in file 0x%3 is less than\r\nits offset 0x%2.\r\n
0x00006a3e | The remaining USN block at offset 0x%1 in file 0x%2 is\r\nless than a page.\r\n
0x00006a3f | The remaining of an USN page at offset 0x%1 in file 0x%2\r\nshould be filled with zeros.\r\n
0x00006a40 | The USN Journal entry at offset 0x%1 and length 0x%2 crosses\r\nthe page boundary.\r\n
0x00006a41 | The USN Journal entry length 0x%2 at offset 0x%1, in file\r\n0x%4 is larger than the remaining length 0x%3 of a page.\r\n
0x00006a42 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 exceeded the page size 0x%3.\r\n
0x00006a43 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%3 is not aligned.\r\n
0x00006a44 | The USN Journal entry version %2.%3 at offset 0x%1\r\nin file 0x%4 is not recognized.\r\n
0x00006a45 | The USN Journal entry length 0x%2 at offset 0x%1 in file\r\n0x%4 is too small.  The minimum value is 0x%3.\r\n
0x00006a46 | The remaining USN page length 0x%2 is too small to fit another\r\nUSN Journal entry at offset 0x%1 in file 0x%4.\r\nIt needs at least 0x%3 bytes.\r\n
0x00006a47 | The USN value 0x%1 of USN Journal entry at offset 0x%2\r\nin file 0x%3 is incorrect.\r\n
0x00006a48 | The USN Journal entry at offset 0x%1 in file 0x%4 is not\r\nconsistence.  The entry has length of 0x%3 and a file name length of 0x%2.\r\n
0x00006a49 | The USN Journal length 0x%1 in file 0x%4 is less the\r\nlargest USN encountered, 0x%2, plus eight in file 0x%3.\r\n
0x00006a4a | The security data stream is missing from file 0x%1.\r\n
0x00006a4b | The security data stream size 0x%1 should not be less than 0x%2.\r\n
0x00006a4c | The remaining of a security data stream page starting at offset 0x%1\r\nfor 0x%2 bytes contains non-zero.\r\n
0x00006a4d | The security data stream entry at offset 0x%1 with length 0x%2\r\ncrosses the page boundary.\r\n
0x00006a4e | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 is too small.  The minimum value is 0x%3.\r\n
0x00006a4f | The length, 0x%2, of the security data stream entry at offset\r\n0x%1 exceeded the page size 0x%3.\r\n
0x00006a50 | The security data stream entry at offset 0x%1 does not fit into the\r\nremaining length, 0x%2, of a page.  The minimum value is 0x%3.\r\n\r\n
0x00006a51 | The security descriptor entry with Id 0x%2 at offset 0x%1 is invalid.\r\n
0x00006a52 | The security Id 0x%2 of security descriptor entry at offset 0x%1\r\nis a duplicate.\r\n
0x00006a53 | The hash value 0x%2 of the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a54 | The offset 0x%2 stored in the security descriptor entry with Id\r\n0x%4 at offset 0x%1 is invalid.  The correct value is 0x%3.\r\n
0x00006a55 | The security descriptor in file 0x%1 is invalid.\r\n
0x00006a56 | The security Id 0x%1 in file 0x%2 is invalid.\r\n
0x00006a57 | The data stream with name %1 in file 0x%2 is not recognized.\r\n
0x00006a58 | The attribute definition table length 0x%1 is incorrect.\r\nThe correct value is 0x%2.\r\n
0x00006a59 | The attribute definition table content is incorrect.\r\n
0x00006a5a | Cluster zero is missing from the data attribute in boot file.\r\n
0x00006a5b | Attribute list found in the log file.\r\n
0x00006a5c | The data attribute is either resident or missing in the log file.\r\n
0x00006a5d | Unable to obtain the LCN in data attribute of the MFT mirror.\r\n
0x00006a5e | There is no physical LCN for VCN 0 in data attribute of the MFT mirror.\r\n
0x00006a5f | The data attribute of the MFT mirror is not contiguous for 0x%1 sectors.\r\n
0x00006a60 | The MFT mirror is different from the MFT.\r\n
0x00006a61 | The data attribute is missing from the upcase file.\r\n
0x00006a62 | The upcase file length 0x%1 is incorrect.  The expected value is 0x%2.\r\n
0x00006a63 | The upcase file content is incorrect.\r\n
0x00006a64 | The data attribute is either resident or missing in the MFT mirror.\r\n
0x00006a65 | The two index entries of length 0x%1 and 0x%2 are either identical\r\nor appear in the wrong order.\r\n
0x00006a66 | The first index entry of length 0x%1 is a leaf but it is not in the root.\r\n
0x00006a67 | The first index entry of length 0x%1 is a leaf but the previous entry is not.\r\n
0x00006a68 | Current leaf index entry of length 0x%3 is at depth 0x%2 which\r\nis different from other leaf index entry which has a depth of 0x%1.\r\n
0x00006a69 | The down pointer of current index entry with length 0x%1 is invalid.\r\n
0x00006a6a | The index entry length 0x%1 is too large.  The maximum value is 0x%2.\r\n
0x00006a6b | The allocation attribute does not exist.\r\n
0x00006a6c | Clearing unused security descriptor stream entries.\r\n
0x00006a6d | Mirror security descriptor block different from that of\r\nmaster security descriptor at offset 0x%1.\r\n
0x00006a6e | The attribute definition table cannot be read.\r\n
0x00006a6f | The index buffer at VCN 0x%2 of index %1 in file 0x%3\r\ncannot be read.\r\n
0x00006a70 | The MFT mirror starting at cluster 0x%1 for 0x%2 sectors\r\ncannot be read.\r\n
0x00006a71 | The security descriptor in file 0x%1 cannot be read.\r\n
0x00006a72 | The upcase table cannot be read.\r\n
0x00006a73 | The USN attrib of type code 0x%1 and name %2 cannot be\r\nread in file 0x%3.\r\n
0x00006a74 | The EA Data value length, 0x%1, in file 0x%2 is incorrect.\r\n
0x00006a75 | The index entry length 0x%2 for index %1 in file 0x%4\r\nis too large.  The maximum value is 0x%3.\r\n
0x00006a76 | Unable to query extent list entry 0x%3 from attribute\r\nof type 0x%1 and instance tag 0x%2.\r\n
0x00006a77 | The total allocated size 0x%1 for attribute of type 0x%3 and\r\ninstance tag 0x%4 is larger than the allocated length 0x%2.\r\n
0x00006a78 | Unable to locate attribute with instance tag 0x%2 and segment\r\nreference 0x%3.  The expected attribute type is 0x%1.\r\n
0x00006a79 | The first index entry offset, 0x%2, for index %1 in file 0x%4\r\npoints beyond the length, 0x%3, of the index.  VCN is unknown.\r\n
0x00006a7a | Some clusters occupied by attribute of type 0x%1 and instance tag 0x%2\r\nin file 0x%3 is already in use.\r\n
0x00006a7b | Unable to setup the child file record segment 0x%2 in file 0x%1.\r\n
0x00006a7c | The parent 0x%2 of index entry %3\r\nin file 0x%4 is incorrect.  The expected parent is 0x%1.\r\n
0x00006a7d | The file reference 0x%3 of an index entry %2 in\r\nparent 0x%1 is not the same as 0x%4.\r\n
0x00006a7e | The file reference 0x%3 of an index entry of index %2\r\nwith parent 0x%1 is not the same as 0x%4.\r\n
0x00006a7f | Multiple object id index entries in file 0x%1\r\npoint to the same file 0x%2.\r\n
0x00006a80 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a81 | The object id index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a82 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is not in use.\r\n
0x00006a83 | The reparse point index entry in file 0x%1 points to file 0x%2\r\nwhich is unreadable.\r\n
0x00006a84 | ----------------------------------------------------------------------\r\n
0x00006a85 | Cleaning up instance tags for file 0x%1.\r\n
0x00006a86 | Cleaning up encrypted flag for file 0x%1.\r\n
0x00006a87 | Cleaning up sparse flag for file 0x%1.\r\n
0x00006a88 | Cleaning up %3 unused index entries from index %2 of file 0x%1.\r\n
0x00006a89 | Cleaning up %1 unused security descriptors.\r\n
0x00006a8a | The value length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8b | The valid data length, 0x%1, of the MFT mirror is too small.\r\nThe minimum value is 0x%2.\r\n
0x00006a8c | Index entry %3 of index %2 in file 0x%1 points to unused file 0x%4.\r\n
0x00006a8d | An index entry of index %2 in file 0x%1 points to unused file 0x%3.\r\n
0x00006a8e | Unable to obtain the LCN in data attribute for VCN 0x%1 of the MFT.\r\n
0x00006a8f | An index entry of index %2 in file 0x%1 points to file 0x%3\r\nwhich is beyond the MFT.\r\n
0x00006a90 | The segment number 0x%1 in file 0x%2 is incorrect.\r\n
0x00006a91 | \r\nInternal Info:\r\n
0x00006a92 | The mapping pairs offset 0x%1 for attribute of type 0x%2 and instance\r\ntag 0x%3 is not quad aligned.\r\n
0x00006a93 | The NTFS file name attribute in file 0x%1 is incorrect.\r\n
0x00006a94 | The attribute of type 0x%1 and instance tag 0x%2 has unexpected holes in the extent list.\r\n
0x00006a95 | The TxF file name attribute in file 0x%1 is corrupt.\r\n
0x00006a96 | The $Txf file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a97 | The $Txf file name attribute in file 0x%1 is corrupt.\r\n
0x00006a98 | The $STANDARD_INFORMATION attribute was corrupted for a $Txf directory.\r\n
0x00006a99 | The $STANDARD_INFORMATION attribute was corrupted for a RM Root directory.\r\n
0x00006a9a | The TxF file name attribute in file 0x%1 is a duplicate.\r\n
0x00006a9b | A TxF RM root file reference was corrupt.\r\n
0x00006a9c | Detected cross linked attribute of type code 0x%1 and instance tag 0x%2\r\nfor file record 0x%3.\r\n
0x00006a9d | File record 0x%1 maps to "%2".\r\n
0x00006a9e | The index entry %3 in index 0x%2 of file 0x%1 is missing.\r\n
0x00006a9f | The parent 0x%1 of file name attribute %2 in file 0x%3 cannot be found.\r\n
0x00006aa0 | The file name flags 0x%1 in index entry %2 of parent 0x%3 is inconsistent\r\nwith that in file 0x%4.\r\n
0x00006aa1 | The only attribute in the file 0x%1 is the standard information.\r\n
0x00006aa2 | Failed to enumerate blocks\r\n
0x00006aa3 | Unsupported on thinly provisioned volume\r\n
0x00006aa4 | Claiming persisted memory failed\r\n
0x00006aa5 | Allocating memory for KSR runs failed\r\n
0x00006aa6 | Could not get system address from Mdl\r\n
0x00006aa7 | Invalid KSR version\r\n
0x00006aa8 | Vcb's TotalClusters did not match with KSRData's TotalClusters\r\n
0x01000007 | Ntfs has detected MFT torn write on a volume.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n\r\n          File reference: %6%n\r\n          File name: %8%n\r\n          Byte offset of the buffer within the file: %9%n\r\n          Byte offset of the torn structure within the buffer: %10%n\r\n          Block index: %11%n\r\n          Expected sequence number: %12%n\r\n          Actual sequence number: %13%n\r\n          FRS file reference: %14%n\r\n          FRS file name: %16%n\r\n          Is child FRS: %17%n\r\n
0x01000062 | Volume %1 (%2) %3\r\n
0x0100008c | The system failed to flush data to the transaction log. Corruption may occur in VolumeId: %2, DeviceName: %4.%n%n\r\n          Failure status: %5%n%n\r\n          Device GUID: %6%n\r\n          Device manufacturer: %8%n\r\n          Device model: %10%n\r\n          Device revision: %12%n\r\n          Device serial number: %14%n\r\n          Bus type: %15%n%n\r\n          Adapter serial number: %17%n\r\n
0x0100008f | Surprise removal of a persistent memory device with active DAX mappings. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000090 | A volume that already has DAX mappings is being mounted. This generally occurs after surprise removal. This might lead to data corruption.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n%nGuidance:%nA reboot is required to clean up the DAX mappings.\r\n
0x01000096 | An IO failed with %12 and NTFS has relocated the clusters. The original clusters are now marked as bad and they will not be reused.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          File offset: %9%n\r\n          %11 cluster(s) were marked as bad starting at cluster %10%n%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0x010000a2 | The data read from the storage does not match what was previously written or read.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n\r\n          Device name: %7%n\r\n          File reference: %8%n\r\n          File name: %10%n\r\n          Attribute type code: %11%n\r\n          Attribute name: %13%n\r\n          File offset: %14%n\r\n          Volume offset: %15%n\r\n          Length: %16%n\r\n          Called from worker: %17%n\r\n          Livedump worker status: %18%n\r\n
0x010000a3 | MftBitmap is not big enough for MftData or does not have required allocations.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n\r\n          Device name: %7%n\r\n          Mft data allocation size: %20%n\r\n          Mft data file size: %21%n\r\n          Mft bitmap allocation size: %22%n\r\n          Mft bitmap file size: %23%n\r\n          Bytes per FRS: %24%n\r\n          Mft data attribute allocation size: %25%n\r\n          Mft data attribute file size: %26%n\r\n          Mft bitmap attribute highest Vcn: %27%n\r\n          Mft bitmap attribute allocation size: %28%n\r\n          Mft bitmap attribute file size: %29%n\r\n          Last data and bitmap attribute record in Mft are in same FRS: %30%n\r\n          Called from worker: %31%n\r\n          Livedump worker status: %32%n\r\n          Major function: %33%n\r\n          Minor function: %34%n\r\n          Source tag: %35%n\r\n
0x010000d2 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nIt is now fixed.\r\n
0x010000d3 | Thinly provisioned volume %1 (%2)%nwere not being mapped between clusters %3 and %4.%nRepair was unsucccessful.%nPossibly out of available slabs.\r\n
0x11000006 | Volume Mount/Dismount\r\n
0x11000016 | Statistics\r\n
0x11000019 | BadClusterHotFix\r\n
0x11000031 | Response Time\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x31000007 | Resume\r\n
0x31000008 | Suspend\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x71000006 | Volume mount\r\n
0x71000008 | Volume dismount\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xb1000001 | RundownStart\r\n
0xb1000002 | RundownComplete\r\n
0xb1000003 | RundownVolumeInformation VolumeId: %1, DeviceName: %3\r\n
0xb1000004 | The NTFS volume has been successfully mounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n          Device Name: %3%n\r\n
0xb1000005 | NTFS KSR data retrieved successfully.%n%n\r\n          Volume GUID: %4%n\r\n          Device Name: %3%n%n\r\n          NTFS KSR version: %5%n\r\n          Number of runs restored: %6%n\r\n          Time to restore (ms): %7%n\r\n
0xb1000006 | NTFS KSR data retrieval failed.%n%n\r\n          Volume GUID: %4%n\r\n          Device Name: %3%n\r\n          Error: %6\r\n
0xb1000007 | Ntfs has detected torn write on a volume.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n\r\n          File reference: %6%n\r\n          File name: %8%n\r\n          Byte offset of the buffer within the file: %9%n\r\n          Byte offset of the torn structure within the buffer: %10%n\r\n          Block index: %11%n\r\n          Expected sequence number: %12%n\r\n          Actual sequence number: %13%n\r\n
0xb1000008 | File's duplicate info has been updated during flush.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          File Reference: %4%n\r\n          File Name: %6%n\r\n          File Link name: %8%n\r\n          Parent file reference: %9%n\r\n          Parent file name: %11%n\r\n          Update Reason: [%12] %13%n\r\n
0xb1000009 | NTFS scanned entire volume bitmap.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n%n\r\n          Device name: %7%n\r\n          Device GUID: %8%n\r\n          Device manufacturer: %10%n\r\n          Device model: %12%n\r\n          Device revision: %14%n\r\n          Device serial number: %16%n\r\n          Bus type: %17%n%n\r\n          Adapter serial number: %19%n%n\r\n          Duration (micro seconds): %20%n\r\n          InputFlags: %21%n\r\n          Reason: %22%n\r\n          Flags: %23%n\r\n
0xb100000a | NTFS cached runs statistics.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %2%n\r\n          Volume label: %3%n%n\r\n          Device name: %4%n\r\n          Device GUID: %5%n\r\n          Device manufacturer: %6%n\r\n          Device model: %7%n\r\n          Device revision: %8%n\r\n          Device serial number: %9%n\r\n          Bus type: %10%n%n\r\n          Adapter serial number: %11%n%n\r\n          Media type: %12%n\r\n          Runs cached: %13%n\r\n          Longest run cached: %15%n\r\n          Most populated bin Count: %16%n\r\n          Most populated bin's minimum length: %18%n\r\n          Most populated bin's maximum length: %20%n\r\n
0xb1000064 | NTFS global corruption action state is now %1.\r\n
0xb100008b | The file system structure that maintains security information on volume %1 (%2) has grown excessively large and fragmented.  The structure has reached %3%% of its maximum fragmentation limit.  If the structure continues to grow and reaches this limit, it may not be possible to create new files on this volume.  It is strongly recommended that the volume be taken offline for preventative maintenance.\r\n
0xb100008d | An operation failed because the disk was full.%n%n\r\n          Process: %5%n\r\n          Free space in bytes: %7%n\r\n          Total reserved space in bytes: %8%n\r\n          Txf TotalAbortReservation space in bytes: %9%n\r\n          Requested space in bytes: %10%n\r\n          Page file size in bytes: %11%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n%nYour disk '%3' is full. Use disk cleanup to free up disk space by deleting unnecessary files. If this is a thinly provisioned volume the physical storage backing this volume may have been exhausted.%n\r\n
0xb100008e | Summary of disk space usage, since last event:%n%n\r\n          Lowest free space in bytes: %4%n\r\n          Highest free space in bytes: %5%n\r\n          Page file size in bytes: 0%n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %6%n\r\n
0xb1000097 | In the past %5 seconds %6 files were deleted from the user's popular known folders (i.e. Desktop, Documents, Downloads, Music, Pictures, Videos, etc.).%n%7 of the deletions recorded their process names.%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Process names: [%8]%n\r\n          Delete counts: %n\r\n            Desktop: [%9]%n\r\n            Documents: [%10]%n\r\n            Downloads: [%11]%n\r\n            Music: [%12]%n\r\n            Pictures: [%13]%n\r\n            Videos: [%14]%n\r\n            Other: [%15]%n\r\n
0xb1000098 | A process has not acknowledged an NTFS oplock break in a long time.%n%n\r\n          Time (seconds): %1%n\r\n          Owner Process: %2%n\r\n          Breaking Process: %3%n\r\n
0xb100009a | System file pages are now locked into memory.%n%n\r\n                   Volume Id: %1%n\r\n                   Volume name: %3%n%n\r\n                   File reference: %4%n\r\n                   File name: %6%n\r\n
0xb100009b | System file pages are no longer locked into memory.%n%n\r\n                   Volume Id: %1%n\r\n                   Volume name: %3%n%n\r\n                   File reference: %4%n\r\n                   File name: %6%n%n\r\n                   Reason: %7%n\r\n
0xb100009c | VCB exclusive resource acquires:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Interval duration: %18%n%n\r\n          Acquire count: %19%n\r\n          Max wait duration: %20 ms%n\r\n          Avg wait duration: %21 ms%n\r\n          Max hold duration: %22 ms%n\r\n          Avg hold duration: %23 ms%n\r\n          Max combined duration: %24 ms%n\r\n          Avg combined duration: %25 ms%n%n\r\n          Device GUID: %5%n\r\n          Device manufacturer: %7%n\r\n          Device model: %9%n\r\n          Device revision: %11%n\r\n          Device serial number: %13%n\r\n          Bus type: %14%n\r\n          %n\r\n          Adapter serial number: %16%n\r\n          %n\r\n          For more details see the details tab.%n\r\n
0xb100009d | A resource duration exceeded %5 ms:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          Major function: %8%n\r\n          Minor function: %9%n\r\n          Control code: %10%n\r\n          Resource name: %11%n\r\n          Exclusive acquire: %27%n\r\n          Wait duration: %12 ms%n\r\n          Hold duration: %13 ms%n\r\n          Combined duration: %14 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %15%n\r\n          Device manufacturer: %17%n\r\n          Device model: %19%n\r\n          Device revision: %21%n\r\n          Device serial number: %23%n\r\n          Bus type: %24%n%n\r\n          Adapter serial number: %26%n\r\n
0xb100009e | NTFS metadata statistics for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          UserFileReads: %4%n\r\n          UserFileReadBytes: %5%n\r\n          UserDiskReads: %6%n\r\n          UserFileWrites: %7%n\r\n          UserFileWriteBytes: %8%n\r\n          UserDiskWrites: %9%n%n\r\n          MetaDataReads: %10%n\r\n          MetaDataReadBytes: %11%n\r\n          MetaDataDiskReads: %12%n\r\n          MetaDataWrites: %13%n\r\n          MetaDataWriteBytes: %14%n\r\n          MetaDataDiskWrites: %15%n%n\r\n          MftReads: %16%n\r\n          MftReadBytes: %17%n\r\n          MftWrites: %18%n\r\n          MftWriteBytes: %19%n\r\n          Mft2Writes: %20%n\r\n          Mft2WriteBytes: %21%n\r\n          RootIndexReads: %22%n\r\n          RootIndexReadBytes: %23%n\r\n          RootIndexWrites: %24%n\r\n          RootIndexWriteBytes: %25%n\r\n          BitmapReads: %26%n\r\n          BitmapReadBytes: %27%n\r\n          BitmapWrites: %28%n\r\n          BitmapWriteBytes: %29%n\r\n          MftBitmapReads: %30%n\r\n          MftBitmapReadBytes: %31%n\r\n          MftBitmapWrites: %32%n\r\n          MftBitmapWriteBytes: %33%n\r\n          UserIndexReads: %34%n\r\n          UserIndexReadBytes: %35%n\r\n          UserIndexWrites: %36%n\r\n          UserIndexWriteBytes: %37%n\r\n          LogFileReads: %38%n\r\n          LogFileReadBytes: %39%n\r\n          LogFileWrites: %40%n\r\n          LogFileWriteBytes: %41%n\r\n          LogFileFull: %42%n\r\n          LogFileFullReasons:%n\r\n                    LF_LOG_SPACE: %43%n\r\n                    LF_DIRTY_PAGES: %44%n\r\n                    LF_OPEN_ATTRIBUTES: %45%n\r\n                    LF_TRANSACTION_DRAIN: %46%n\r\n                    LF_FASTIO_CALLBACK: %47%n\r\n                    LF_DEALLOCATED_CLUSTERS: %48%n\r\n                    LF_DEALLOCATED_CLUSTERS_MEM: %49%n\r\n                    LF_RECORD_STACK_CHECK: %50%n\r\n                    LF_DISMOUNT: %51%n\r\n                    LF_COMPRESSION: %52%n\r\n                    LF_SNAPSHOT: %53%n\r\n                    LF_MOUNT: %54%n\r\n                    LF_SHUTDOWN: %55%n\r\n                    LF_RECURSIVE_COMPRESSION: %56%n\r\n                    LF_TESTING: %57%n%n\r\n          DiskResourceFailure: %58%n\r\n          VolumeTrimCount: %59%n\r\n                    VolumeTrimTime (ms): %60%n\r\n                    VolumeTrimSize (KB): %61%n\r\n                    AvgVolumeTrimTime (ms): %62%n\r\n                    AvgVolumeTrimSize (KB): %63%n\r\n          VolumeTrimSkippedCount: %64%n\r\n                    VolumeTrimSkippedSize (KB): %65%n\r\n          FileLevelTrimCount: %66%n\r\n                    FileLevelTrimTime (ms): %67%n\r\n                    FileLevelTrimSize (KB): %68%n\r\n                    AvgFileLevelTrimTime (ms): %69%n\r\n                    AvgFileLevelTrimSize (KB): %70%n\r\n          NtfsFillStatInfoFromMftRecordCalledCount: %71%n\r\n          NtfsFillStatInfoFromMftRecordBailedBecauseOfAttributeListCount: %72%n\r\n          NtfsFillStatInfoFromMftRecordBailedBecauseOfNonResReparsePointCount: %73%n\r\n
0xb100009f | NTFS has successfully completed the %19 request in %20 ms when trying to %18 the volume size from %4 (MB) to %5 (MB).%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Device GUID: %6%n\r\n          Device manufacturer: %8%n\r\n          Device model: %10%n\r\n          Device revision: %12%n\r\n          Device serial number: %14%n\r\n          Bus type: %15%n%n\r\n          Adapter serial number: %17%n%n\r\n          Operation: %18%n\r\n                    Request Type: %19%n%n\r\n          Stage Durations:%n\r\n                    Stage 1. Verify input and calculate new volume size (ms): %21%n\r\n                    Stage 2. Set boundary and allocate/deallocate cluster (ms): %22%n\r\n                    Stage 3. Update bitmap (ms): %23%n\r\n
0xb10000a0 | NTFS has failed to complete the %19 request after %20 ms when trying to %18 the volume size from %4 (MB) to %5 (MB).%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Device GUID: %6%n\r\n          Device manufacturer: %8%n\r\n          Device model: %10%n\r\n          Device revision: %12%n\r\n          Device serial number: %14%n\r\n          Bus type: %15%n%n\r\n          Adapter serial number: %17%n%n\r\n          Operation: %18%n\r\n                    Request Type: %19%n%n\r\n          Stage Durations:%n\r\n                    Stage 1. Verify input and calculate new volume size (ms): %21%n\r\n                    Stage 2. Set boundary and allocate/deallocate cluster (ms): %22%n\r\n                    Stage 3. Update bitmap (ms): %23%n%n\r\n          Failure Stage: %24%n\r\n          Status Code: %25%n\r\n          Failure Reason: %26%n\r\n
0xb10000a1 | An operation has failed due to a file system limitation.%n%n\r\n          Reason: %1%n\r\n          Volume Id: %3%n\r\n          Volume Name: %4%n\r\n          File Path: %5%n\r\n
0xb10000c9 | NtfsLogFileFull VolumeId: %1, Reason: %2\r\n
0xb10000ca | PeriodicCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cb | PeriodicCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000cc | CleanCheckpointStart VolumeId: %1, Reason: %2, Usage: %3%\r\n
0xb10000cd | CleanCheckpointComplete VolumeId: %1, DirtyMetaDataPages: %2\r\n
0xb10000ce | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3, CacheHit: %4\r\n
0xb10000d0 | MftRecordRead VolumeId: %1, BaseFileId: %2, FileId: %3\r\n
0xb10000e6 | WorkItem queued, WorkItem: %1, Reason: %2\r\n
0xb10000e7 | WorkItem queue failed, WorkItem: %1, Reason: %2, Error: %3\r\n
0xb10000e8 | WorkItem started, WorkItem: %1, Reason: %2\r\n
0xb10000e9 | WorkItem completed, WorkItem: %1, Reason: %2\r\n
0xb10000f0 | File metadata optimization started.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb10000f1 | File metadata optimization completed.%n%n\r\n                   Volume guid: %1%n\r\n                   Volume name: %3%n\r\n                   File reference: %4%n\r\n
0xb100012c | NTFS volume dismount has started.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb100012d | NTFS has sent volume dismount event notification and is waiting for the notifications to complete.\r\n
0xb100012e | The volume dismount event notification on the NTFS volume has completed.\r\n
0xb100012f | The NTFS volume has successfully dismounted.%n%n\r\n          Volume GUID: %4%n\r\n          Volume Name: %6%n\r\n          Volume Label: %8%n\r\n
0xb1000130 | The NTFS volume dismount failed.%n%n\r\n          Error:%1%n\r\n
0xb1000131 | NTFS failed to mount the volume.%n%n\r\n          Error: %1%n\r\n          Volume GUID: %2%n\r\n          Volume Name: %4%n%nGuidance:%nThe volume is recognized by NTFS but it is corrupted that NTFS could not mount it. Run CHKDSK /F to fix any errors on this volume, and then try accessing it.\r\n
0xb1000191 | Efs offloading initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000192 | Efs offloading read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000193 | Efs offloading write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000194 | Efs legacy initiated.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000195 | Efs legacy read regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb1000196 | Efs legacy write regular file.%n%n\r\n                   Volume serial: %1%n\r\n                   File reference: %2%n\r\n                   File name: %4%n\r\n
0xb10001f4 | A process has created a USN journal on a volume.%n%n\r\n          Process: %1%n\r\n          Volume Id: %2%n\r\n          Volume Name: %4%n\r\n          Journal Id: %5%n\r\n          Maximum Size: %6%n\r\n          Allocation Delta: %7%n\r\n
0xb10001f5 | A process has deleted a USN journal on a volume.%n%n\r\n          Process: %1%n\r\n          Volume Id: %2%n\r\n          Volume Name: %4%n\r\n          Journal Id: %5%n\r\n          Current USN: %6%n\r\n
0xb1010004 | The NTFS volume has been successfully mounted.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n%n\r\n          Device name: %7%n\r\n          Device GUID: %8%n\r\n          Device manufacturer: %10%n\r\n          Device model: %12%n\r\n          Device revision: %14%n\r\n          Device serial number: %16%n\r\n          Bus type: %17%n%n\r\n          Adapter serial number: %19%n\r\n          %n\r\n          Total mount duration: %22%n\r\n          Longest stage: %23. Duration %24 (%25% of the total)%n\r\n          Second longest stage: %26. Duration %27 (%28% of the total)%n\r\n          Volume restart applied: %29%n\r\n
0xb101000a | NTFS cached runs statistics.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %2%n\r\n          Volume label: %3%n%n\r\n          Device name: %4%n\r\n          Device GUID: %5%n\r\n          Device manufacturer: %6%n\r\n          Device model: %7%n\r\n          Device revision: %8%n\r\n          Device serial number: %9%n\r\n          Bus type: %10%n%n\r\n          Adapter serial number: %11%n%n\r\n          Capacity tier name: %12%n\r\n            Media type: %13%n\r\n            Runs cached: %14%n\r\n            Longest run cached: %16%n\r\n            Most populated bin Count: %17%n\r\n            Most populated bin's minimum length: %19%n\r\n            Most populated bin's maximum length: %21%n\r\n          Performance tier name: %30%n\r\n            Media type: %31%n\r\n            Runs cached: %32%n\r\n            Longest run cached: %34%n\r\n            Most populated bin Count: %35%n\r\n            Most populated bin's minimum length: %37%n\r\n            Most populated bin's maximum length: %39%n\r\n
0xb101008e | Summary of disk space usage, since last event:%n%n\r\n          Available space was between %6 and %7%n\r\n          Change in available space: %8%n\r\n          %n\r\n          Available clusters were between: %9 and %10%n\r\n          Reserved clusters were between: %13 and %14%n\r\n          Txf abort reserved clusters were between: %15 and %16%n\r\n          %n\r\n          Elapsed seconds: %5%n\r\n          %n\r\n          Pagefile size: %18%n\r\n          Volume size: %20%n\r\n          Bytes per cluster: %21%n\r\n          %n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n
0xb10100aa | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n          %n\r\n          IO type: %20%n\r\n          %n\r\n          Interval duration: %18%n\r\n          %n\r\n          Max Acceptable IO Latency: %22%n\r\n          High Latency IOs: %23%n\r\n          %n\r\n          IO count: %24%n\r\n          Avg IOPS: %25%n\r\n          Avg latency: %27%n\r\n          %n\r\n          Latency buckets: [%28]%n\r\n          IO count buckets: [%29, %30, %31, %32, %33, %34, %35, %36, %37, %38, %39, %40]%n\r\n          Total time buckets (ns): [%41, %42, %43, %44, %45, %46, %47, %48, %49, %50, %51, %52]%n\r\n          %n\r\n          Device GUID: %5%n\r\n          Device manufacturer: %7%n\r\n          Device model: %9%n\r\n          Device revision: %11%n\r\n          Device serial number: %13%n\r\n          Bus type: %14%n\r\n          %n\r\n          Adapter serial number: %16%n\r\n          %n\r\n          For more details see the details tab.%n\r\n
0xb101012c | NTFS volume dismount has started.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n%n\r\n          Device name: %7%n\r\n          Device GUID: %8%n\r\n          Device manufacturer: %10%n\r\n          Device model: %12%n\r\n          Device revision: %14%n\r\n          Device serial number: %16%n\r\n          Bus type: %17%n\r\n          %n\r\n          Adapter serial number: %19%n\r\n          %n\r\n          Process Id: %21%n\r\n          Process name: %22%n\r\n          %n\r\n          Reason: %23%n\r\n
0xb101012f | The NTFS volume has successfully dismounted.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n%n\r\n          Device name: %7%n\r\n          Device GUID: %8%n\r\n          Device manufacturer: %10%n\r\n          Device model: %12%n\r\n          Device revision: %14%n\r\n          Device serial number: %16%n\r\n          Bus type: %17%n%n\r\n          Adapter serial number: %19%n\r\n          %n\r\n          Process Id: %21%n\r\n          Process name: %22%n\r\n          %n\r\n          Reason: %23%n\r\n
0xb1010130 | The NTFS volume dismount failed.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n%n\r\n          Device name: %7%n\r\n          Device GUID: %8%n\r\n          Device manufacturer: %10%n\r\n          Device model: %12%n\r\n          Device revision: %14%n\r\n          Device serial number: %16%n\r\n          Bus type: %17%n\r\n          %n\r\n          Adapter serial number: %19%n\r\n          %n\r\n          Error:%21%n\r\n
0xb1010131 | NTFS failed to mount the volume.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Volume label: %5%n%n\r\n          Device name: %7%n\r\n          Device GUID: %8%n\r\n          Device manufacturer: %10%n\r\n          Device model: %12%n\r\n          Device revision: %14%n\r\n          Device serial number: %16%n\r\n          Bus type: %17%n%n\r\n          Adapter serial number: %19%n\r\n          %n\r\n          Error: %20%n\r\n          %nGuidance:%nThe volume is recognized by NTFS but it is corrupted and NTFS could not mount it. Run CHKDSK /F to fix any errors on this volume, and then try accessing it.\r\n
0xb102008e | Summary of disk space usage, since last event:%n%n\r\n          Available space was between %6 and %7%n\r\n          Change in available space: %8%n\r\n          %n\r\n          Available clusters were between: %9 and %10%n\r\n          Reserved clusters were between: %13 and %14%n\r\n          Txf abort reserved clusters were between: %15 and %16%n\r\n          %n\r\n          Elapsed seconds: %5%n\r\n          %n\r\n          Pagefile size: %18%n\r\n          Volume size: %20%n\r\n          Bytes per cluster: %21%n\r\n          %n\r\n          Slab size: %23%n\r\n          Slabs in use: %24%n\r\n          Slabs required for volume: %25%n\r\n          Thin provisioning map failures: %26%n\r\n          %n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n          Volume is thinly provisioned%n\r\n
0xb1020094 | A %9 failed with %14.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          IO Size: %10 bytes%n\r\n          File offset: %11%n\r\n          %13 cluster(s) starting at cluster %12%n\r\n          Latency: %15 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %16%n\r\n          Device manufacturer: %18%n\r\n          Device model: %20%n\r\n          Device revision: %22%n\r\n          Device serial number: %24%n\r\n          Bus type: %25%n%n\r\n          Adapter serial number: %27%n\r\n
0xb1020095 | In the past %17 seconds we had high latency IOs and/or IO failures.%n%n\r\n          High latency IO count: %18%n\r\n          Failed writes: %19%n\r\n          Failed reads: %20%n\r\n          Bad clusters relocated: %21%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %5%n\r\n          Device manufacturer: %7%n\r\n          Device model: %9%n\r\n          Device revision: %11%n\r\n          Device serial number: %13%n\r\n          Bus type: %14%n%n\r\n          Adapter serial number: %16%n\r\n
0xb10200aa | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n          %n\r\n          IO type: %20%n\r\n          %n\r\n          Interval duration: %18%n\r\n          %n\r\n          Max Acceptable IO Latency: %22%n\r\n          High Latency IOs: %23%n\r\n          %n\r\n          IO count: %24%n\r\n          Total bytes: %53%n\r\n          Avg IOPS: %25%n\r\n          Avg Bps: %54%n\r\n          Avg latency: %27%n\r\n          %n\r\n          Latency buckets: [%28]%n\r\n          IO count buckets: [%29, %30, %31, %32, %33, %34, %35, %36, %37, %38, %39, %40]%n\r\n          Total time buckets (ns): [%41, %42, %43, %44, %45, %46, %47, %48, %49, %50, %51, %52]%n\r\n          %n\r\n          Device GUID: %5%n\r\n          Device manufacturer: %7%n\r\n          Device model: %9%n\r\n          Device revision: %11%n\r\n          Device serial number: %13%n\r\n          Bus type: %14%n\r\n          %n\r\n          Adapter serial number: %16%n\r\n          %n\r\n          For more details see the details tab.%n\r\n
0xb10200ab | File-Level Trim Summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n          %n\r\n          Period duration (us): %5%n\r\n          %n\r\n          Operation count: %6%n\r\n          Reposted operation count: %7%n\r\n          Failed operation count: %8%n\r\n          Operation range count: %9%n\r\n          Operation byte count: %10%n\r\n          Operation long range byte count %11%n\r\n          Unaligned range count: %12%n\r\n          Bytes in unaligned ranges: %13%n\r\n          Operation trim extent count: %14%n\r\n          Non-blocking aligned trim byte count: %15%n\r\n          Reclaimed byte count: %16%n\r\n          %n\r\n          Byte count bucket values: [%18]%n\r\n          %n\r\n          Operation counts: [%19, %20, %21, %22, %23, %24, %25, %26, %27, %28, %29, %30]%n\r\n          Operation byte counts: [%31, %32, %33, %34, %35, %36, %37, %38, %39, %40, %41, %42]%n\r\n          Operation bytes reclaimed: [%43, %44, %45, %46, %47, %48, %49, %50, %51, %52, %53, %54]%n\r\n          Operation latency (us): [%55, %56, %57, %58, %59, %60, %61, %62, %63, %64, %65, %67]%n\r\n          %n\r\n          Latency bucket values: [%68]%n\r\n          %n\r\n          Operation latency count: [%69, %70, %71, %72, %73, %74, %75, %76, %77, %78, %79, %80, %81, %82, %83]%n\r\n
0xb103008e | Summary of disk space usage, since last event:%n%n\r\n          Available space was between %6 and %7%n\r\n          Change in available space: %8%n\r\n          %n\r\n          Available clusters were between: %9 and %10%n\r\n          Reserved clusters were between: %13 and %14%n\r\n          Txf abort reserved clusters were between: %15 and %16%n\r\n          %n\r\n          Elapsed seconds: %5%n\r\n          %n\r\n          Pagefile size: %18%n\r\n          Volume size: %20%n\r\n          Bytes per cluster: %21%n\r\n          %n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n          %n\r\n          Cached runs miss counts:%n\r\n              For MFT: %22%n\r\n              For MFT zone: %23%n\r\n              Everything else: %24%n\r\n
0xb1030092 | IO latency summary:%n%n\r\n          Volume Id: %2%n\r\n          Volume name: %4%n\r\n          Is boot volume: %5%n%n\r\n          Device GUID: %7%n\r\n          Device manufacturer: %9%n\r\n          Device model: %11%n\r\n          Device revision: %13%n\r\n          Device serial number: %15%n\r\n          Bus type: %16%n%n\r\n          Adapter serial number: %18%n%n\r\n          Max Acceptable IO Latency: %19 ms%n%n\r\n          Read/Write latency buckets (ns): [%20, %21, %22, %23, %24, %25, %26]%n\r\n          Trim latency buckets (ns): [%27, %28, %29, %30, %31, %32, %33]%n\r\n          Flush latency buckets (ns): [%34, %35, %36, %37, %38, %39, %40]%n%n\r\n          Interval duration: %42 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %43%n\r\n                    Total bytes: %44%n\r\n                    Avg latency: %45 ns%n%n\r\n          Non-cached writes:%n\r\n                    IO count: %46%n\r\n                    Total bytes: %47%n\r\n                    Avg latency: %48 ns%n%n\r\n          File flushes:%n\r\n                    IO count: %49%n\r\n                    Avg latency: %50 ns%n%n\r\n          Directory flushes:%n\r\n                    IO count: %51%n\r\n                    Avg latency: %52 ns%n%n\r\n          Volume flushes:%n\r\n                    IO count: %53%n\r\n                    Avg latency: %54 ns%n%n\r\n          File level trims:%n\r\n                    IO count: %55%n\r\n                    Total bytes: %56%n\r\n                    Extents count: %57%n\r\n                    Avg latency: %58 ns%n%n\r\n          Volume trims:%n\r\n                    IO count: %59%n\r\n                    Total bytes: %60%n\r\n                    Extents count: %61%n\r\n                    Avg latency: %62 ns%n%n\r\n          VCB exclusive resource acquires:%n\r\n                    Acquire count: %71%n\r\n                    Max wait duration: %72 ms%n\r\n                    Avg wait duration: %73 ms%n\r\n                    Max hold duration: %74 ms%n\r\n                    Avg hold duration: %75 ms%n\r\n                    Max combined duration: %76 ms%n\r\n                    Avg combined duration: %77 ms%n%n\r\n          For more details see the details tab.%n\r\n
0xb1030093 | An IO took more than %5 ms to complete:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          File offset: %12%n\r\n          IO Type: %10%n\r\n          IO Size: %11 bytes%n\r\n          %15 cluster(s) starting at cluster %14%n\r\n          Latency: %13 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %16%n\r\n          Device manufacturer: %18%n\r\n          Device model: %20%n\r\n          Device revision: %22%n\r\n          Device serial number: %24%n\r\n          Bus type: %25%n%n\r\n          Adapter serial number: %27%n\r\n
0xb1030094 | A %11 failed with %16.%nThis may indicate a failing disk.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          IO Size: %12 bytes%n\r\n          File offset: %13%n\r\n          %15 cluster(s) starting at cluster %14%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %17%n\r\n          Device manufacturer: %19%n\r\n          Device model: %21%n\r\n          Device revision: %23%n\r\n          Device serial number: %25%n\r\n          Bus type: %26%n%n\r\n          Adapter serial number: %28%n\r\n
0xb10300aa | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n          %n\r\n          IO type: %20%n\r\n          %n\r\n          Interval duration: %18%n\r\n          %n\r\n          Max Acceptable IO Latency: %22%n\r\n          High Latency IOs: %23%n\r\n          %n\r\n          IO count: %24%n\r\n          Total bytes: %53%n\r\n          Total extents: %67%n\r\n          Avg IOPS: %25%n\r\n          Avg Bps: %54%n\r\n          Avg latency: %27%n\r\n          %n\r\n          Latency buckets: [%28]%n\r\n          IO count buckets: [%29, %30, %31, %32, %33, %34, %35, %36, %37, %38, %39, %40]%n\r\n          Total time buckets (ns): [%41, %42, %43, %44, %45, %46, %47, %48, %49, %50, %51, %52]%n\r\n          %n\r\n          Device GUID: %5%n\r\n          Device manufacturer: %7%n\r\n          Device model: %9%n\r\n          Device revision: %11%n\r\n          Device serial number: %13%n\r\n          Bus type: %14%n\r\n          %n\r\n          Adapter serial number: %16%n\r\n          %n\r\n          For more details see the details tab.%n\r\n
0xb104008e | Summary of disk space usage, since last event:%n%n\r\n          Available space was between %6 and %7%n\r\n          Change in available space: %8%n\r\n          %n\r\n          Available clusters were between: %9 and %10%n\r\n          Reserved clusters were between: %13 and %14%n\r\n          Txf abort reserved clusters were between: %15 and %16%n\r\n          %n\r\n          Elapsed seconds: %5%n\r\n          %n\r\n          Pagefile size: %18%n\r\n          Volume size: %20%n\r\n          Bytes per cluster: %21%n\r\n          %n\r\n          Slab size: %23%n\r\n          Slabs in use: %24%n\r\n          Slabs required for volume: %25%n\r\n          Thin provisioning map failures: %26%n\r\n          %n\r\n          Volume guid: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n\r\n          Volume is thinly provisioned%n\r\n          %n\r\n          Cached runs miss counts:%n\r\n              For MFT: %27%n\r\n              For MFT zone: %28%n\r\n              Everything else: %29%n\r\n
0xb1040091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %2%n\r\n          Volume name: %4%n\r\n          Is boot volume: %5%n%n\r\n          Device GUID: %7%n\r\n          Device manufacturer: %9%n\r\n          Device model: %11%n\r\n          Device revision: %13%n\r\n          Device serial number: %15%n\r\n          Bus type: %16%n%n\r\n          Adapter serial number: %18%n%n\r\n          Max Acceptable IO Latency: %19 ms%n%n\r\n          Read/Write latency buckets (ns): [%20, %21, %22, %23, %24, %25, %26]%n\r\n          Trim latency buckets (ns): [%27, %28, %29, %30, %31, %32, %33]%n\r\n          Flush latency buckets (ns): [%34, %35, %36, %37, %38, %39, %40]%n\r\n
0xb1040093 | An IO took more than %5 ms to complete:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          File offset: %15%n\r\n          IO Type: %13%n\r\n          IO Size: %14 bytes%n\r\n          %18 cluster(s) starting at cluster %17%n\r\n          Latency: %16 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %19%n\r\n          Device manufacturer: %21%n\r\n          Device model: %23%n\r\n          Device revision: %25%n\r\n          Device serial number: %27%n\r\n          Bus type: %28%n%n\r\n          Adapter serial number: %30%n\r\n
0xb1050093 | An IO took more than %5 ms to complete:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          IO Type: %13%n\r\n          Latency: %14 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Is boot volume: %4%n%n\r\n          Device GUID: %15%n\r\n          Device manufacturer: %17%n\r\n          Device model: %19%n\r\n          Device revision: %21%n\r\n          Device serial number: %23%n\r\n          Bus type: %24%n%n\r\n          Adapter serial number: %26%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xd1000001 | is healthy.  No action is needed.\r\n
0xd1000002 | requires an Online Scan.  An Online Scan will automatically run as part of the next scheduled maintenance task.  Alternatively you may run "CHKDSK /SCAN" locally via the command line, or run "REPAIR-VOLUME <drive:> -SCAN" locally or remotely via PowerShell.\r\n
0xd1000003 | needs to be taken offline for a short time to perform a Spot Fix.  Please run "CHKDSK /SPOTFIX" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000004 | needs to be taken offline to perform a Full Chkdsk.  Please run "CHKDSK /F" locally via the command line, or run "REPAIR-VOLUME <drive:>" locally or remotely via PowerShell.\r\n
0xd1000005 | LogSpace\r\n
0xd1000006 | DirtyPages\r\n
0xd1000007 | OpenAttributes\r\n
0xd1000008 | TransactionDrain\r\n
0xd1000009 | FastIOCallback\r\n
0xd100000a | DeallocatedClusters\r\n
0xd100000b | DeallocatedClustersMem\r\n
0xd100000c | RecordStackCheck\r\n
0xd100000d | Dismount\r\n
0xd100000e | Compression\r\n
0xd100000f | Snapshot\r\n
0xd1000010 | Mount\r\n
0xd1000011 | Shutdown\r\n
0xd1000012 | RecursiveCompression\r\n
0xd1000013 | Testing\r\n
0xd1000014 | PostRequest\r\n
0xd1000015 | Checkpoint\r\n
0xd1000016 | DelayClose\r\n
0xd1000017 | MarkUnusedContextCompletion\r\n
0xd1000018 | HotFix\r\n
0xd1000019 | DiskFlushCompletion\r\n
0xd100001a | McbCleanup\r\n
0xd100001b | UsnTimeOut\r\n
0xd100001c | Repair\r\n
0xd100001d | TxfRmDelayedWorkItem\r\n
0xd100001e | TxfRmCriticalWorkItem\r\n
0xd100001f | TxfRmRestartWorkItem\r\n
0xd1000020 | TxfThawRmsWorker\r\n
0xd1000021 | ScavengeDeleteUsn\r\n
0xd1000022 | ScavengeRepairObjectId\r\n
0xd1000023 | ScavengeRepairQuotaIndex\r\n
0xd1000024 | ScavengeMarkUserLimit\r\n
0xd1000025 | ScavengeResolveVolumeAndLogEvent\r\n
0xd1000026 | Write: NonPaging, NonCached, Async\r\n
0xd1000027 | Write: NonPaging, NonCached, Sync\r\n
0xd1000028 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd1000029 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd100002a | Write: NonPaging, Cached, Async\r\n
0xd100002b | Write: NonPaging, Cached, Sync\r\n
0xd100002c | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd100002d | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd100002e | Write: Paging, NonCached, Async\r\n
0xd100002f | Write: Paging, NonCached, Sync\r\n
0xd1000030 | Write: Paging, NonCached, Async, Writethrough\r\n
0xd1000031 | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd1000032 | Read: NonPaging, NonCached, Async\r\n
0xd1000033 | Read: NonPaging, NonCached, Sync\r\n
0xd1000034 | Read: NonPaging, Cached, Async\r\n
0xd1000035 | Read: NonPaging, Cached, Sync\r\n
0xd1000036 | Read: Paging, NonCached, Async\r\n
0xd1000037 | Read: Paging, NonCached, Sync\r\n
0xd1000038 | create\r\n
0xd1000039 | create named pipe\r\n
0xd100003a | close\r\n
0xd100003b | read\r\n
0xd100003c | write\r\n
0xd100003d | query information\r\n
0xd100003e | set information\r\n
0xd100003f | query EA\r\n
0xd1000040 | set EA\r\n
0xd1000041 | flush buffers\r\n
0xd1000042 | query volume information\r\n
0xd1000043 | set volume information\r\n
0xd1000044 | directory control\r\n
0xd1000045 | file system control\r\n
0xd1000046 | device control\r\n
0xd1000047 | internal device control\r\n
0xd1000048 | shutdown\r\n
0xd1000049 | lock control\r\n
0xd100004a | cleanup\r\n
0xd100004b | create mail slot\r\n
0xd100004c | query security\r\n
0xd100004d | set security\r\n
0xd100004e | power\r\n
0xd100004f | system control\r\n
0xd1000050 | device change\r\n
0xd1000051 | query quota\r\n
0xd1000052 | set quota\r\n
0xd1000053 | plug and play\r\n
0xd1000054 | <unknown>\r\n
0xd1000055 | SCSI\r\n
0xd1000056 | ATAPI\r\n
0xd1000057 | ATA\r\n
0xd1000058 | 1394\r\n
0xd1000059 | SSA\r\n
0xd100005a | Fibre\r\n
0xd100005b | USB\r\n
0xd100005c | RAID\r\n
0xd100005d | iSCSI\r\n
0xd100005e | SAS\r\n
0xd100005f | SATA\r\n
0xd1000060 | SD\r\n
0xd1000061 | MMC\r\n
0xd1000062 | Virtual\r\n
0xd1000063 | File backed virtual\r\n
0xd1000064 | Spaces\r\n
0xd1000065 | NVMe\r\n
0xd1000066 | SCM\r\n
0xd1000067 | Ufs\r\n
0xd1000068 | Unknown\r\n
0xd1000069 | Internal attribute stream was deleted\r\n
0xd100006a | Stream was purged\r\n
0xd100006b | Configuration changed\r\n
0xd100006c | VCB\r\n
0xd100006d | Extend\r\n
0xd100006e | Shrink\r\n
0xd100006f | Extend\r\n
0xd1000070 | Prepare\r\n
0xd1000071 | Shrink\r\n
0xd1000072 | Abort\r\n
0xd1000073 | Unknown\r\n
0xd1000074 | File size exceeds the maximum allowed by a volume\r\n
0xd1000075 | File size exceeds a system limit\r\n
0xd1000076 | A file record could not be split\r\n
0xd1000077 | Bitmap size exceeds a system limit\r\n
0xd1000078 | USN journal size exceeds a system limit\r\n
0xd1000079 | false\r\n
0xd100007a | true\r\n
0xd100007b | <unknown>\r\n
0xd100007c | Unknown\r\n
0xd100007d | File create\r\n
0xd100007e | Last modification time\r\n
0xd100007f | Last change time \r\n
0xd1000080 | Last access time\r\n
0xd1000081 | Allocation size\r\n
0xd1000082 | File size\r\n
0xd1000083 | File attributes\r\n
0xd1000084 | File EA size\r\n
0xd1000085 | Mismatch info found\r\n
0xd1000086 | Unspecified\r\n
0xd1000087 | Hard disk\r\n
0xd1000088 | SSD\r\n
0xd1000089 | Storage class memory\r\n
0xd100008a | Mount\r\n
0xd100008b | Reload requested because of an exception or configuration change\r\n
0xd100008c | Could not extend Mft without fragmenting it\r\n
0xd100008d | Previously reduced Mft zone is now being expanded\r\n
0xd100008e | Change in volume size\r\n
0xd100008f | New cluster alignment was initialized\r\n
0xd1000090 | Proactive background scan to repopulate cached runs\r\n
