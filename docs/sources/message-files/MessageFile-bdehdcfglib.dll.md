## bdehdcfglib.dll

Path: %SystemRoot%\system32\BdeHdCfgLib.dll

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x3000000a | Initialization\r\n
0x3000000b | Shrink\r\n
0x3000000c | Create\r\n
0x3000000d | Prepare\r\n
0x40a00033 | BitLocker Drive Preparation Tool version %1!s!\r\nCopyright (C) 2012 Microsoft Corporation. All rights reserved.\r\n\r\n
0x40a00034 | Initializing, please wait...\r\n\r\n
0x40a00035 | You must restart your computer to apply these changes.\r\n\r\nBefore restarting, save any open files and close all programs.\r\n
0x40a00036 | Usage:\r\n\r\nBdeHdCfg[.exe] \r\n               [-driveinfo]\r\n               [-target {default | unallocated | \r\n                         TargetDriveLetter {shrink | merge}}]\r\n               [-newdriveletter DriveLetter]\r\n               [-size SizeInMegabytes]\r\n               [-quiet] [-restart] [{-? | /?}]\r\n\r\nDescription:\r\n  This command prepares your hard drive for BitLocker Drive Encryption.\r\n\r\n  Command line parameters are not case-sensitive.\r\n\r\nParameters:\r\n  -driveinfo\r\n        Displays information about valid target drives.\r\n\r\n  -target\r\n        Specifies the target and operation.\r\n\r\n        Specify 'shrink' to create a new active partition.\r\n        Specify 'merge' to make an existing partition active.\r\n        Specify 'unallocated' to use unformatted space on disk.\r\n        Specify 'default' for the target to be chosen automatically.\r\n\r\n        Examples: -target D: merge\r\n                  -target C: shrink\r\n                  -target unallocated\r\n                  -target default\r\n\r\n  -newdriveletter\r\n        Specifies the desired drive letter for the new drive. This option is\r\n        only valid when a new drive is created.\r\n\r\n        Example: -newdriveletter S:\r\n\r\n  -size\r\n        Specifies the desired size of the new drive. This option is only valid\r\n        when a new drive is created.\r\n\r\n        If not specified, the Drive Preparation Tool assumes the required\r\n        minimum size of %1!d! megabytes.\r\n\r\n        Example: -size 700\r\n        \r\n  -quiet\r\n        Specifies operation in quiet mode. No output from the drive preparation\r\n        tool is displayed.\r\n\r\n  -restart\r\n        Enables an automatic restart after drive preparation.\r\n\r\n        You must restart your computer before enabling BitLocker.\r\n\r\n  -? or /?\r\n        Displays help for this command.\r\n\r\nExamples:\r\n    BdeHdCfg -target c: shrink -newdriveletter x: -size %1!d! -quiet -restart\r\n    BdeHdCfg -target d: merge -quiet -restart\r\n    BdeHdCfg -target unallocated -newdriveletter s:\r\n    BdeHdCfg -target default\r\n\r\n
0x40a00038 | The target drive has a cluster size larger than 4 KB.\r\n
0x40a00039 | The target drive is not large enough for the requested operation.\r\n
0x40a0003a | The target drive does not have sufficient free space for the requested\r\noperation.\r\n
0x40a0003b | The target drive cannot shrink by the requested size.\r\n
0x40a0003c | The target drive is compressed and cannot be used for the merge operation.\r\n
0x40a0003d | The target drive is not on the same physical disk as the system drive.\r\n
0x40a0003e | The target drive is on a logical (extended) partition.\r\n
0x40a0003f | The system drive cannot be used for the merge operation.\r\n
0x40a00040 | The target drive is encrypted and cannot be used for the merge operation.\r\n
0x40a00041 | The target drive is not a type 0x07 or 0x27 partition.\r\n
0x40a00042 | The target drive is not formatted with the NTFS file system.\r\n
0x40a00043 | The system is currently running on battery power.\r\n
0x40a00044 | An error occurred when attempting to query the system's power status.\r\n
0x40a00045 | The new disk drive's DACL could not be modified.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x80a00017 | BitLocker Setup failed to query the system's power status. It could not be\r\nverified that the machine is on AC power.\r\n
0x80a00037 | BitLocker Setup could not lock the target drive. The drive will be forcibly \r\ndismounted.\r\n
0x90000001 | Microsoft-Windows-BitLocker-DrivePreparationTool\r\n
0x90000002 | Microsoft-Windows-BitLocker-DrivePreparationTool/Admin\r\n
0x90000003 | Microsoft-Windows-BitLocker-DrivePreparationTool/Operational\r\n
0xb0010001 | A problem occurred while running the BitLocker Drive Preparation Tool.%nError Code: %1%nError Text: %2\r\n
0xb0010100 | Warning Code: %1%nWarning Text: %2\r\n
0xb0010200 | The BitLocker Drive Configuration Tool successfully completed. The target hard disk is ready for BitLocker.\r\n
0xb0011000 | Found a candidate volume for shrink or merge.%nShrinkable: %1%nCandidate Volume Name: %3\r\n
0xb0011001 | Found an unallocated extent large enough for the requested size.%nOffset: %3%nSize: %4\r\n
0xb0011002 | Disk extent located on the hard disk containing the System Drive.%nOffset: %3%nSize: %4\r\n
0xb0011003 | Command-line parameters for the BitLocker Drive Preparation Tool:%n   %1\r\n
0xb0011004 | Drive will shrink and new active drive %6 will be created. %nVolume Name: %1%nShrink Size: %5 Bytes\r\n
0xb0011005 | New drive %3 will be created from unallocated space%nUnallocated extent offset: %1%nNew partition size: %2 Bytes\r\n
0xb0011006 | Drive will be set as the new system drive%nVolume Name: %1\r\n
0xb0011007 | Detected Windows Recovery Environment volume%nVolume Path: %1\r\n
0xb0011008 | A volume failed to meet the requirements for a target volume.%nVolume Name: %3%nReason: %2\r\n
0xc0a00001 | The current process is not elevated, and does not have the necessary privileges\r\nto run. Open an Administrator command prompt and run BitLocker Setup again.\r\n
0xc0a00002 | This computer's hard drive is properly configured for BitLocker. It is not\r\nnecessary to run BitLocker Setup.\r\n
0xc0a00003 | BitLocker Setup requires a fixed hard drive. Run this setup from the hard drive\r\nintended for BitLocker.\r\n
0xc0a00004 | BitLocker Setup was expecting MBR (Master Boot Record) partitioning style, but \r\na different partitioning style was found. You may need to manually prepare \r\nyour drive for BitLocker.\r\n
0xc0a00005 | BitLocker Setup requires the disk cluster size to be no more than than 4 KB.\r\nYou may need to manually prepare your drive for BitLocker.\r\n
0xc0a00006 | Changes made to your computer require that you restart before running BitLocker\r\nSetup.\r\n
0xc0a00007 | BitLocker Setup could not find a target system drive. You may need to manually\r\nprepare your drive for BitLocker.\r\n
0xc0a00008 | BitLocker Setup requires the drive file system to be NTFS. Convert the file\r\nsystem and run BitLocker Setup again.\r\n
0xc0a00009 | BitLocker Setup requires a basic disk. Convert your dynamic disk to a basic\r\ndisk and run BitLocker Setup again.\r\n
0xc0a0000a | BitLocker Setup could not change the active partition. You may need to manually\r\nprepare your drive for BitLocker.\r\n
0xc0a0000b | BitLocker Setup failed to copy boot files. You may need to manually prepare\r\nyour drive for BitLocker.\r\n
0xc0a0000c | BitLocker Setup failed to export the BCD (Boot Configuration Data) store. You\r\nmay need to manually prepare your drive for BitLocker.\r\n
0xc0a0000d | Do not restart this computer until original drive is set to active! BitLocker\r\nSetup failed to import the BCD (Boot Configuration Data) store and could not\r\nset active partition back. Use DISKMGMT.MSC to set the system partition active.\r\n
0xc0a0000e | BitLocker Setup failed to import the BCD (Boot Configuration Data) store. You\r\nmay need to manually prepare your drive for BitLocker.\r\n
0xc0a0000f | BitLocker Setup failed to modify the exported BCD (Boot Configuration Data)\r\nstore. You may need to manually prepare your drive for BitLocker.\r\n
0xc0a00010 | The new active drive cannot be formatted. You may need to manually prepare your\r\ndrive for BitLocker.\r\n
0xc0a00011 | BitLocker Setup was cancelled. The hard disk configuration may have changed.\r\nRun the setup again to prepare your system for BitLocker.\r\n
0xc0a00012 | BitLocker Setup cannot shrink the target drive sufficiently to create the \r\nactive drive required by BitLocker. You may need to manually prepare your drive\r\nfor BitLocker.\r\n
0xc0a00013 | BitLocker Setup failed to get the requested element from the BCD (Boot \r\nConfiguration Data) store. You may need to manually prepare your drive for \r\nBitLocker.\r\n
0xc0a00014 | BitLocker Setup failed to open an object in the BCD (Boot Configuration Data)\r\nstore. You may need to manually prepare your drive for BitLocker.\r\n
0xc0a00015 | BitLocker Setup failed to open the temporary BCD (Boot Configuration Data)\r\nstore. You may need to manually prepare your drive for BitLocker.\r\n
0xc0a00016 | BitLocker Setup library was not properly initialized. You may need to manually\r\nprepare your drive for BitLocker.\r\n
0xc0a00018 | BitLocker Setup requires the system to be connected to an AC power source\r\nbefore any changes can be made. Please plug your computer into a power source\r\nand run BitLocker Setup again.\r\n
0xc0a00019 | BitLocker Setup could not apply security settings to the newly created drive.\r\nPlease check the drive's security settings. You may need to manually prepare\r\nyour drive for BitLocker.\r\n
0xc0a0001a | BitLocker setup could not move the Windows Recovery Environment image to the\r\nnew system drive. You will need to move Windows Recovery Environment from your\r\nWindows drive before encryption or Windows Recovery Environment will not\r\nfunction.\r\n
0xc0a0001b | An unexpected error occurred while running BitLocker Setup. You may need to\r\nmanually prepare your drive for BitLocker.\r\n
0xc0a0001c | The '-target' command requires additional arguments.\r\n\r\nExamples: -target default\r\n          -target unallocated\r\n          -target C: shrink\r\n          -target D: merge\r\n
0xc0a0001d | Invalid target drive letter. Use the '-driveinfo' command for a list of valid\r\ntarget drives.\r\n\r\nExamples: -target C: shrink\r\n          -target D: merge\r\n
0xc0a0001e | The specified target drive could not be found. Specify an existing drive\r\nletter.\r\n\r\nExamples: -target C: shrink\r\n          -target D: merge\r\n
0xc0a0001f | The specified target drive is not valid for shrink. Use the '-driveinfo'\r\ncommand for a list of valid target drives.\r\n
0xc0a00020 | The specified target drive is not valid for merge. Use the '-driveinfo' \r\ncommand for a list of valid target drives.\r\n
0xc0a00021 | You must specify a drive letter with the '-newdriveletter' parameter.\r\n\r\nExample: -newdriveletter S:\r\n
0xc0a00022 | Invalid drive letter. Use a drive letter in the form 'C:'.\r\n\r\nExample: -newdriveletter S:\r\n
0xc0a00023 | The specified drive letter is in use. Use a different drive letter.\r\n\r\nExample: -newdriveletter S:\r\n
0xc0a00024 | The '-size' parameter requires a value of at least %1!d!.\r\n\r\nExample: -size %1!d!\r\n
0xc0a00025 | The minimum size for the new partition is %1!d! megabytes. Please specify a size\r\nof at least %1!d!.\r\n\r\nExample: -size %1!d!\r\n
0xc0a00026 | The 'merge' parameter and the '-size' parameter cannot be specified together.\r\n
0xc0a00027 | You must specify a target drive using the '-target' parameter.\r\n
0xc0a00028 | The 'merge' parameter and the '-newdriveletter' parameter cannot be specified\r\ntogether.\r\n
0xc0a00029 | The '-driveinfo' parameter cannot be specified with any other parameters.\r\n
0xc0a0002a | Invalid command line syntax. Use the 'BdeHdCfg -?' command for a list of valid\r\noperations.\r\n
0xc0a0002b | No new drives can be created. Specify a target for the merge. Use the\r\n'-driveinfo' command for a list of valid target drives. \r\n
0xc0a0002c | Insufficient unallocated space on disk to create new system drive. Use the\r\n'-driveinfo' command for a list of valid target drives.\r\n
0xc0a0002d | The target drive must be on the same disk as the system drive. Use the\r\n'-driveinfo' command for a list of valid target drives.\r\n
0xc0a0002e | A problem occurred while preparing your drive for BitLocker.\r\nError code: %1!#.8x!\r\n
0xc0a0002f | Disk already has the maximum number of primary and extended partitions. Use the\r\n'-driveinfo' command for a list of valid target drives.\r\n
0xc0a00030 | There is not enough free space on the target drive. Running DISK CLEANUP may\r\ncreate additional free space.\r\n
0xc0a00031 | There is not enough free space on the target Windows Recovery Environment\r\ndrive. 100 MB of free space is required for a Windows Recovery Environment\r\ndrive to be made the new system drive.\r\n
0xc0a00032 | The target drive does not meet the size requirements for BitLocker. The new  \r\nsystem drive must be at least %1!d! MB in size.\r\n

### 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x3000000a | Initialization\r\n
0x3000000b | Shrink\r\n
0x3000000c | Create\r\n
0x3000000d | Prepare\r\n
0x40a00033 | BitLocker Drive Preparation Tool version %1!s!\r\nCopyright (C) 2013 Microsoft Corporation. All rights reserved.\r\n\r\n
0x40a00034 | Initializing, please wait...\r\n\r\n
0x40a00035 | You must restart your computer to apply these changes.\r\n\r\nBefore restarting, save any open files and close all programs.\r\n
0x40a00036 | Usage:\r\n\r\nBdeHdCfg[.exe] \r\n               [-driveinfo]\r\n               [-target {default | unallocated | \r\n                         TargetDriveLetter {shrink | merge}}]\r\n               [-newdriveletter DriveLetter]\r\n               [-size SizeInMegabytes]\r\n               [-quiet] [-restart] [{-? | /?}]\r\n\r\nDescription:\r\n  This command prepares your hard drive for BitLocker Drive Encryption.\r\n\r\n  Command line parameters are not case-sensitive.\r\n\r\nParameters:\r\n  -driveinfo\r\n        Displays information about valid target drives.\r\n\r\n  -target\r\n        Specifies the target and operation.\r\n\r\n        Specify 'shrink' to create a new active partition.\r\n        Specify 'merge' to make an existing partition active.\r\n        Specify 'unallocated' to use unformatted space on disk.\r\n        Specify 'default' for the target to be chosen automatically.\r\n\r\n        Examples: -target D: merge\r\n                  -target C: shrink\r\n                  -target unallocated\r\n                  -target default\r\n\r\n  -newdriveletter\r\n        Specifies the desired drive letter for the new drive. This option is\r\n        only valid when a new drive is created.\r\n\r\n        Example: -newdriveletter S:\r\n\r\n  -size\r\n        Specifies the desired size of the new drive. This option is only valid\r\n        when a new drive is created.\r\n\r\n        If not specified, the Drive Preparation Tool assumes the required\r\n        minimum size of %1!d! megabytes.\r\n\r\n        Example: -size 700\r\n        \r\n  -quiet\r\n        Specifies operation in quiet mode. No output from the drive preparation\r\n        tool is displayed.\r\n\r\n  -restart\r\n        Enables an automatic restart after drive preparation.\r\n\r\n        You must restart your computer before enabling BitLocker.\r\n\r\n  -? or /?\r\n        Displays help for this command.\r\n\r\nExamples:\r\n    BdeHdCfg -target c: shrink -newdriveletter x: -size %1!d! -quiet -restart\r\n    BdeHdCfg -target d: merge -quiet -restart\r\n    BdeHdCfg -target unallocated -newdriveletter s:\r\n    BdeHdCfg -target default\r\n\r\n
0x40a00038 | The target drive has a cluster size larger than 4 KB.\r\n
0x40a00039 | The target drive is not large enough for the requested operation.\r\n
0x40a0003a | The target drive does not have sufficient free space for the requested\r\noperation.\r\n
0x40a0003b | The target drive cannot shrink by the requested size.\r\n
0x40a0003c | The target drive is compressed and cannot be used for the merge operation.\r\n
0x40a0003d | The target drive is not on the same physical disk as the system drive.\r\n
0x40a0003e | The target drive is on a logical (extended) partition.\r\n
0x40a0003f | The system drive cannot be used for the merge operation.\r\n
0x40a00040 | The target drive is encrypted and cannot be used for the merge operation.\r\n
0x40a00041 | The target drive is not a type 0x07 or 0x27 partition.\r\n
0x40a00042 | The target drive is not formatted with the NTFS file system.\r\n
0x40a00043 | The system is currently running on battery power.\r\n
0x40a00044 | An error occurred when attempting to query the system's power status.\r\n
0x40a00045 | The new disk drive's DACL could not be modified.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x80a00017 | BitLocker Setup failed to query the system's power status. It could not be\r\nverified that the machine is on AC power.\r\n
0x80a00037 | BitLocker Setup could not lock the target drive. The drive will be forcibly \r\ndismounted.\r\n
0x90000001 | Microsoft-Windows-BitLocker-DrivePreparationTool\r\n
0x90000002 | Microsoft-Windows-BitLocker-DrivePreparationTool/Admin\r\n
0x90000003 | Microsoft-Windows-BitLocker-DrivePreparationTool/Operational\r\n
0xb0010001 | A problem occurred while running the BitLocker Drive Preparation Tool.%nError Code: %1%nError Text: %2\r\n
0xb0010100 | Warning Code: %1%nWarning Text: %2\r\n
0xb0010200 | The BitLocker Drive Configuration Tool successfully completed. The target hard disk is ready for BitLocker.\r\n
0xb0011000 | Found a candidate volume for shrink or merge.%nShrinkable: %1%nCandidate Volume Name: %3\r\n
0xb0011001 | Found an unallocated extent large enough for the requested size.%nOffset: %3%nSize: %4\r\n
0xb0011002 | Disk extent located on the hard disk containing the System Drive.%nOffset: %3%nSize: %4\r\n
0xb0011003 | Command-line parameters for the BitLocker Drive Preparation Tool:%n   %1\r\n
0xb0011004 | Drive will shrink and new active drive %6 will be created. %nVolume Name: %1%nShrink Size: %5 Bytes\r\n
0xb0011005 | New drive %3 will be created from unallocated space%nUnallocated extent offset: %1%nNew partition size: %2 Bytes\r\n
0xb0011006 | Drive will be set as the new system drive%nVolume Name: %1\r\n
0xb0011007 | Detected Windows Recovery Environment volume%nVolume Path: %1\r\n
0xb0011008 | A volume failed to meet the requirements for a target volume.%nVolume Name: %3%nReason: %2\r\n
0xc0a00001 | The current process is not elevated, and does not have the necessary privileges\r\nto run. Open an Administrator command prompt and run BitLocker Setup again.\r\n
0xc0a00002 | This computer's hard drive is properly configured for BitLocker. It is not\r\nnecessary to run BitLocker Setup.\r\n
0xc0a00003 | BitLocker Setup requires a fixed hard drive. Run this setup from the hard drive\r\nintended for BitLocker.\r\n
0xc0a00004 | BitLocker Setup was expecting MBR (Master Boot Record) partitioning style, but \r\na different partitioning style was found. You may need to manually prepare \r\nyour drive for BitLocker.\r\n
0xc0a00005 | BitLocker Setup requires the disk cluster size to be no more than than 4 KB.\r\nYou may need to manually prepare your drive for BitLocker.\r\n
0xc0a00006 | Changes made to your computer require that you restart before running BitLocker\r\nSetup.\r\n
0xc0a00007 | BitLocker Setup could not find a target system drive. You may need to manually\r\nprepare your drive for BitLocker.\r\n
0xc0a00008 | BitLocker Setup requires the drive file system to be NTFS. Convert the file\r\nsystem and run BitLocker Setup again.\r\n
0xc0a00009 | BitLocker Setup requires a basic disk. Convert your dynamic disk to a basic\r\ndisk and run BitLocker Setup again.\r\n
0xc0a0000a | BitLocker Setup could not change the active partition. You may need to manually\r\nprepare your drive for BitLocker.\r\n
0xc0a0000b | BitLocker Setup failed to copy boot files. You may need to manually prepare\r\nyour drive for BitLocker.\r\n
0xc0a0000c | BitLocker Setup failed to export the BCD (Boot Configuration Data) store. You\r\nmay need to manually prepare your drive for BitLocker.\r\n
0xc0a0000d | Do not restart this computer until original drive is set to active! BitLocker\r\nSetup failed to import the BCD (Boot Configuration Data) store and could not\r\nset active partition back. Use DISKMGMT.MSC to set the system partition active.\r\n
0xc0a0000e | BitLocker Setup failed to import the BCD (Boot Configuration Data) store. You\r\nmay need to manually prepare your drive for BitLocker.\r\n
0xc0a0000f | BitLocker Setup failed to modify the exported BCD (Boot Configuration Data)\r\nstore. You may need to manually prepare your drive for BitLocker.\r\n
0xc0a00010 | The new active drive cannot be formatted. You may need to manually prepare your\r\ndrive for BitLocker.\r\n
0xc0a00011 | BitLocker Setup was cancelled. The hard disk configuration may have changed.\r\nRun the setup again to prepare your system for BitLocker.\r\n
0xc0a00012 | BitLocker Setup cannot shrink the target drive sufficiently to create the \r\nactive drive required by BitLocker. You may need to manually prepare your drive\r\nfor BitLocker.\r\n
0xc0a00013 | BitLocker Setup failed to get the requested element from the BCD (Boot \r\nConfiguration Data) store. You may need to manually prepare your drive for \r\nBitLocker.\r\n
0xc0a00014 | BitLocker Setup failed to open an object in the BCD (Boot Configuration Data)\r\nstore. You may need to manually prepare your drive for BitLocker.\r\n
0xc0a00015 | BitLocker Setup failed to open the temporary BCD (Boot Configuration Data)\r\nstore. You may need to manually prepare your drive for BitLocker.\r\n
0xc0a00016 | BitLocker Setup library was not properly initialized. You may need to manually\r\nprepare your drive for BitLocker.\r\n
0xc0a00018 | BitLocker Setup requires the system to be connected to an AC power source\r\nbefore any changes can be made. Please plug your computer into a power source\r\nand run BitLocker Setup again.\r\n
0xc0a00019 | BitLocker Setup could not apply security settings to the newly created drive.\r\nPlease check the drive's security settings. You may need to manually prepare\r\nyour drive for BitLocker.\r\n
0xc0a0001a | BitLocker setup could not move the Windows Recovery Environment image to the\r\nnew system drive. You will need to move Windows Recovery Environment from your\r\nWindows drive before encryption or Windows Recovery Environment will not\r\nfunction.\r\n
0xc0a0001b | An unexpected error occurred while running BitLocker Setup. You may need to\r\nmanually prepare your drive for BitLocker.\r\n
0xc0a0001c | The '-target' command requires additional arguments.\r\n\r\nExamples: -target default\r\n          -target unallocated\r\n          -target C: shrink\r\n          -target D: merge\r\n
0xc0a0001d | Invalid target drive letter. Use the '-driveinfo' command for a list of valid\r\ntarget drives.\r\n\r\nExamples: -target C: shrink\r\n          -target D: merge\r\n
0xc0a0001e | The specified target drive could not be found. Specify an existing drive\r\nletter.\r\n\r\nExamples: -target C: shrink\r\n          -target D: merge\r\n
0xc0a0001f | The specified target drive is not valid for shrink. Use the '-driveinfo'\r\ncommand for a list of valid target drives.\r\n
0xc0a00020 | The specified target drive is not valid for merge. Use the '-driveinfo' \r\ncommand for a list of valid target drives.\r\n
0xc0a00021 | You must specify a drive letter with the '-newdriveletter' parameter.\r\n\r\nExample: -newdriveletter S:\r\n
0xc0a00022 | Invalid drive letter. Use a drive letter in the form 'C:'.\r\n\r\nExample: -newdriveletter S:\r\n
0xc0a00023 | The specified drive letter is in use. Use a different drive letter.\r\n\r\nExample: -newdriveletter S:\r\n
0xc0a00024 | The '-size' parameter requires a value of at least %1!d!.\r\n\r\nExample: -size %1!d!\r\n
0xc0a00025 | The minimum size for the new partition is %1!d! megabytes. Please specify a size\r\nof at least %1!d!.\r\n\r\nExample: -size %1!d!\r\n
0xc0a00026 | The 'merge' parameter and the '-size' parameter cannot be specified together.\r\n
0xc0a00027 | You must specify a target drive using the '-target' parameter.\r\n
0xc0a00028 | The 'merge' parameter and the '-newdriveletter' parameter cannot be specified\r\ntogether.\r\n
0xc0a00029 | The '-driveinfo' parameter cannot be specified with any other parameters.\r\n
0xc0a0002a | Invalid command line syntax. Use the 'BdeHdCfg -?' command for a list of valid\r\noperations.\r\n
0xc0a0002b | No new drives can be created. Specify a target for the merge. Use the\r\n'-driveinfo' command for a list of valid target drives. \r\n
0xc0a0002c | Insufficient unallocated space on disk to create new system drive. Use the\r\n'-driveinfo' command for a list of valid target drives.\r\n
0xc0a0002d | The target drive must be on the same disk as the system drive. Use the\r\n'-driveinfo' command for a list of valid target drives.\r\n
0xc0a0002e | A problem occurred while preparing your drive for BitLocker.\r\nError code: %1!#.8x!\r\n
0xc0a0002f | Disk already has the maximum number of primary and extended partitions. Use the\r\n'-driveinfo' command for a list of valid target drives.\r\n
0xc0a00030 | There is not enough free space on the target drive. Running DISK CLEANUP may\r\ncreate additional free space.\r\n
0xc0a00031 | There is not enough free space on the target Windows Recovery Environment\r\ndrive. 100 MB of free space is required for a Windows Recovery Environment\r\ndrive to be made the new system drive.\r\n
0xc0a00032 | The target drive does not meet the size requirements for BitLocker. The new  \r\nsystem drive must be at least %1!d! MB in size.\r\n
