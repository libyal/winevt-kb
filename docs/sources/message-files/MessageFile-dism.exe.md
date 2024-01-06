## dism.exe

Path: %SystemRoot%\system32\Dism.exe

### 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0x01500020 | The operation completed successfully.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x81500027 | A error occurred while initializing the DISM event reporting component. \r\nFor more information, review the log file.\r\n
0x81500034 | Logging is disabled: Unable to obtain access to the log file %1!s!.\r\n
0x90000001 | Deployment Image Servicing And Management CLI\r\n
0xc1500003 | An initialization error occurred. \r\nFor more information, review the log file.\r\n
0xc1500004 | DISM doesn't recognize the command-line option "%1". \r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc1500005 | Invalid command-line argument. \r\nTo retrieve help, do not specify a command-line option with an argument.\r\n
0xc1500006 | An error occurred while parsing the command-line options specified. \r\nFor more information, review the log file.\r\n
0xc1500007 | An initialization error occurred while accessing the path to the offline image.\r\nFor more information, review the log file.\r\n
0xc1500008 | Unable to access the image. \r\nMake sure that the image path and the Windows directory for the image exist and you have Read permissions on the folder.\r\n
0xc150000a | An error occurred while processing the command-line options.\r\nFor more information, review the log file.\r\n
0xc150000e | The command-line is missing a required servicing command. \r\nFor more information, refer to the help by running DISM.exe /Image=<path_to_offline_image> /? where <path_to_the_offline_image> is the full path to an offline Windows image.\r\n
0xc1500010 | An error occurred while creating the log file. \r\nEnsure that the path to the log file exists and that you have Read/Write permissions on the folder where the log files will be created.\r\n
0xc1500011 | A path and file name were not specified for the /LogPath option. \r\nMake sure the /LogPath argument is not empty. For more information, refer to the help by running DISM.exe /LogPath /?\r\n
0xc1500012 | The option /WinDir is not recognized in this context. It can only be used with an offline image. \r\nFor more information, refer to the help by running DISM.exe /WinDir /?.\r\n
0xc1500013 | An error occurred closing a servicing component in the image. \r\nWait a few minutes and try running the command again.\r\n
0xc1500014 | Restart Windows to complete this operation.\r\n
0xc1500016 | Unable to automatically restart Windows. \r\nManually restart the computer to complete this operation.\r\n
0xc1500018 | Windows failed to restart. \r\nManually restart the computer to complete this operation.\r\n
0xc1500019 | Do not use the /Image or /WinDir option when using the /Online option to specify a running operating system. \r\nFor more information, refer to the help by running DISM.exe /Online /?.\r\n
0xc150001a | Unable to find the Windows directory in the running Windows installation. \r\nFor more information, review the log file.\r\n
0xc150001c | The /Image option that is specified points to a running Windows installation. \r\nTo service the running operating system, use the /Online option. For more information, refer to the help by running DISM.exe /Online /?.\r\n
0xc150001e | DISM failed. No operation was performed. \r\nFor more information, review the log file.\r\n
0xc150001f | An error occurred while accessing the DISM binaries in the image. \r\nFor more information, review the log file.\r\n
0xc1500021 | The %1 option is missing a required argument. \r\nFor more information, refer to the help by running DISM %1 /?.\r\n
0xc1500022 | DISM cannot service an image on a network path. \r\nMount the image locally and run DISM again.\r\n
0xc1500023 | An error occurred while attempting to access the image at %1.\r\nFor more information, review the log file.\r\n
0xc1500024 | An error occurred while attempting to access the image.\r\nFor more information, review the log file.\r\n
0xc1500025 | An error occurred accessing the DISM binaries on the host system. \r\nEnsure that the local DISM binaries exist and that you have Read permission on the folder.\r\n
0xc1500026 | An error occurred while validating the path to the image.\r\nEnsure that the image path is correct and that you have Read permissions on the folder.\r\n
0xc1500028 | An error occurred while accessing the temporary directory. \r\nEnsure that the path to the directory exists and that you have Read/Write permissions on the folder. For more information, refer to the help by running DISM.exe /ScratchDir /?.\r\n
0xc1500029 | The directory %1 does not appear to be a valid Windows directory.\r\nEnsure that the /WinDir option that is specified is valid. For more information, refer to the help by running DISM.exe /WinDir /?.\r\n
0xc150002a | Elevated permissions are required to run DISM. \r\nUse an elevated command prompt to complete these tasks.\r\n
0xc150002b | An error occurred while locating the DISM binaries. DISM is attempting to locate dismcore.dll. \r\nEnsure that the DISM binaries are present and that you have Read permissions on the folder. \r\n
0xc150002c | An error occurred while initializing COM security. \r\nTry running DISM again.\r\n
0xc150002d | The file %1 does not appear to be a valid DLL. \r\nEnsure that the file has not been corrupted. \r\n
0xc150002e | An error occurred while processing the command.\r\nEnsure that the command-line arguments are valid. For more information, review the log file.\r\n
0xc1500032 | An invalid log level was specified. \r\nFor more information, refer to the help by running DISM.exe /LogLevel /?. \r\n
0xc1500035 | The command-line is missing a required servicing command. \r\nFor more information, refer to the help by running DISM.exe /Online /?.\r\n
0xc1500036 | The DISM process encountered a problem and shutdown.\r\nFor more information, review the log file.\r\n
0xc1500038 | Image Version: %1!s!\r\n\r\n
0xc1500039 | No DISM options were specified on the command-line. \r\nRun DISM with a command-line option specified, such as /Image or /Online. For more information, refer to the help by running DISM.exe /?.\r\n
0xc150003a | An error occurred while loading DISM. The DISM tool may be corrupt. \r\nTry reinstalling DISM.\r\n
0xc150003b | You cannot service a running 64-bit operating system with a 32-bit version of DISM. \r\nPlease use the version of DISM that corresponds to your computer's architecture.\r\n
0xc150003c | DISM does not support servicing Windows PE with the /Online option.\r\n
0xc150003d | The %1 option does not take an argument. \r\nRemove the argument and run DISM again.\r\n
0xc150003e | An error occurred while initializing the log file. \r\nEnsure that the path to the log file is a valid. For more information, refer to the help by running DISM.exe /LogPath /?.\r\n
0xc150003f | DISM does not support servicing a Windows Vista RTM or earlier operating system. \r\nIf the operating system is supported check that SSShim.DLL is present.\r\n
0xc1500040 | An error occurred while attempting to start the servicing process for the image located at %1!s!. \r\nFor more information, review the log file.\r\n
0xc1500041 | DISM does not support servicing Windows Vista or Windows Server 2008 with the /Online option.\r\n
0xc1500042 | Invalid command-line option "%1". \r\nEnsure that /? is the last option listed on the command-line.\r\n
0xc1500043 | The %1 option is missing a required argument. \r\nFor more information, refer to the help for the %1 option.\r\n
0xc1500044 | Unable to access the System directory for the specified image. \r\nMake sure the System directory for the image exists and you have Read permissions on the folder.\r\n
0xc1500064 | No help topic could be found for the %1 option.\r\nSpecify an image to see relevant help topics, using either the /Image or\r\n/Online command-line option:\r\n\r\n/Image:<path_to_offline_image>  \r\n\r\n  This is the path to the root directory of the offline Windows image.\r\n\r\n    Example: \r\n      DISM.exe /Image:C:\test\offline /?\r\n\r\n/Online                 \r\n\r\n  Specifies that the operation is to be performed against the running Windows\r\n  installation. \r\n\r\n    Example: \r\n      DISM.exe /Online /?\r\n
0xc1500066 | The %1 option is unknown. \r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc1500067 | \r\nError: %1!d!\r\n\r\n
0xc1500068 | \r\nError: 0x%1!x!\r\n\r\n
0xc1500069 | The /Image option cannot be used in this context.\r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc150006a | The %1 argument given for the %2 option is invalid.\r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc150006b | Operation was incomplete because of a cancel request.\r\n
0xc150006c | Invalid command-line. \r\nFor more information, refer to the help.\r\n
0xc150006d | The %1 option has been duplicated on the command-line. \r\nRemove the duplicate option and try the command again.\r\n

### 6.3.9600.17031, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0

Message identifier | Message string
--- | ---
0x01500020 | The operation completed successfully.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x81500027 | A error occurred while initializing the DISM event reporting component. \r\nFor more information, review the log file.\r\n
0x81500034 | Logging is disabled: Unable to obtain access to the log file %1!s!.\r\n
0x90000001 | Deployment Image Servicing And Management CLI\r\n
0xc1500003 | An initialization error occurred. \r\nFor more information, review the log file.\r\n
0xc1500004 | DISM doesn't recognize the command-line option "%1". \r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc1500005 | Invalid command-line argument. \r\nTo retrieve help, do not specify a command-line option with an argument.\r\n
0xc1500006 | An error occurred while parsing the command-line options specified. \r\nFor more information, review the log file.\r\n
0xc1500007 | An initialization error occurred while accessing the path to the offline image.\r\nFor more information, review the log file.\r\n
0xc1500008 | Unable to access the image. \r\nMake sure that the image path and the Windows directory for the image exist and you have Read permissions on the folder.\r\n
0xc150000a | An error occurred while processing the command-line options.\r\nFor more information, review the log file.\r\n
0xc150000e | The command-line is missing a required servicing command. \r\nFor more information, refer to the help by running DISM.exe /Image=<path_to_offline_image> /? where <path_to_the_offline_image> is the full path to an offline Windows image.\r\n
0xc1500010 | An error occurred while creating the log file. \r\nEnsure that the path to the log file exists and that you have Read/Write permissions on the folder where the log files will be created.\r\n
0xc1500011 | A path and file name were not specified for the /LogPath option. \r\nMake sure the /LogPath argument is not empty. For more information, refer to the help by running DISM.exe /LogPath /?\r\n
0xc1500012 | The option /WinDir is not recognized in this context. It can only be used with an offline image. \r\nFor more information, refer to the help by running DISM.exe /WinDir /?.\r\n
0xc1500013 | An error occurred closing a servicing component in the image. \r\nWait a few minutes and try running the command again.\r\n
0xc1500014 | Restart Windows to complete this operation.\r\n
0xc1500016 | Unable to automatically restart Windows. \r\nManually restart the computer to complete this operation.\r\n
0xc1500018 | Windows failed to restart. \r\nManually restart the computer to complete this operation.\r\n
0xc1500019 | Do not use the /Image or /WinDir option when using the /Online option to specify a running operating system. \r\nFor more information, refer to the help by running DISM.exe /Online /?.\r\n
0xc150001a | Unable to find the Windows directory in the running Windows installation. \r\nFor more information, review the log file.\r\n
0xc150001c | The /Image option that is specified points to a running Windows installation. \r\nTo service the running operating system, use the /Online option. For more information, refer to the help by running DISM.exe /Online /?.\r\n
0xc150001e | DISM failed. No operation was performed. \r\nFor more information, review the log file.\r\n
0xc150001f | An error occurred while accessing the DISM binaries in the image. \r\nFor more information, review the log file.\r\n
0xc1500021 | The %1 option is missing a required argument. \r\nFor more information, refer to the help by running DISM %1 /?.\r\n
0xc1500022 | DISM cannot service an image on a network path. \r\nMount the image locally and run DISM again.\r\n
0xc1500023 | An error occurred while attempting to access the image at %1.\r\nFor more information, review the log file.\r\n
0xc1500024 | An error occurred while attempting to access the image.\r\nFor more information, review the log file.\r\n
0xc1500025 | An error occurred accessing the DISM binaries on the host system. \r\nEnsure that the local DISM binaries exist and that you have Read permission on the folder.\r\n
0xc1500026 | An error occurred while validating the path to the image.\r\nEnsure that the image path is correct and that you have Read permissions on the folder.\r\n
0xc1500028 | An error occurred while accessing the temporary directory. \r\nEnsure that the path to the directory exists and that you have Read/Write permissions on the folder. For more information, refer to the help by running DISM.exe /ScratchDir /?.\r\n
0xc1500029 | The directory %1 does not appear to be a valid Windows directory.\r\nEnsure that the /WinDir option that is specified is valid. For more information, refer to the help by running DISM.exe /WinDir /?.\r\n
0xc150002a | Elevated permissions are required to run DISM. \r\nUse an elevated command prompt to complete these tasks.\r\n
0xc150002b | An error occurred while locating the DISM binaries. DISM is attempting to locate dismcore.dll. \r\nEnsure that the DISM binaries are present and that you have Read permissions on the folder. \r\n
0xc150002c | An error occurred while initializing COM security. \r\nTry running DISM again.\r\n
0xc150002d | The file %1 does not appear to be a valid DLL. \r\nEnsure that the file has not been corrupted. \r\n
0xc150002e | An error occurred while processing the command.\r\nEnsure that the command-line arguments are valid. For more information, review the log file.\r\n
0xc1500032 | An invalid log level was specified. \r\nFor more information, refer to the help by running DISM.exe /LogLevel /?. \r\n
0xc1500035 | The command-line is missing a required servicing command. \r\nFor more information, refer to the help by running DISM.exe /Online /?.\r\n
0xc1500036 | The DISM process encountered a problem and shutdown.\r\nFor more information, review the log file.\r\n
0xc1500038 | Image Version: %1!s!\r\n\r\n
0xc1500039 | No DISM options were specified on the command-line. \r\nRun DISM with a command-line option specified, such as /Image or /Online. For more information, refer to the help by running DISM.exe /?.\r\n
0xc150003a | An error occurred while loading DISM. The DISM tool may be corrupt. \r\nTry reinstalling DISM.\r\n
0xc150003b | You cannot service a running 64-bit operating system with a 32-bit version of DISM. \r\nPlease use the version of DISM that corresponds to your computer's architecture.\r\n
0xc150003c | DISM does not support servicing Windows PE with the /Online option.\r\n
0xc150003d | The %1 option does not take an argument. \r\nRemove the argument and run DISM again.\r\n
0xc150003e | An error occurred while initializing the log file. \r\nEnsure that the path to the log file is a valid. For more information, refer to the help by running DISM.exe /LogPath /?.\r\n
0xc150003f | DISM does not support servicing a Windows Vista RTM or earlier operating system. \r\nIf the operating system is supported check that SSShim.DLL is present.\r\n
0xc1500040 | An error occurred while attempting to start the servicing process for the image located at %1!s!. \r\nFor more information, review the log file.\r\n
0xc1500041 | DISM does not support servicing Windows Vista or Windows Server 2008 with the /Online option.\r\n
0xc1500042 | Invalid command-line option "%1". \r\nEnsure that /? is the last option listed on the command-line.\r\n
0xc1500043 | The %1 option is missing a required argument. \r\nFor more information, refer to the help for the %1 option.\r\n
0xc1500044 | Unable to access the System directory for the specified image. \r\nMake sure the System directory for the image exists and you have Read permissions on the folder.\r\n
0xc1500064 | No help topic could be found for the %1 option.\r\nSpecify an image to see relevant help topics, using either the /Image or\r\n/Online command-line option:\r\n\r\n/Image:<path_to_offline_image>  \r\n\r\n  This is the path to the root directory of the offline Windows image.\r\n\r\n    Example: \r\n      DISM.exe /Image:C:\test\offline /?\r\n\r\n/Online                 \r\n\r\n  Specifies that the operation is to be performed against the running Windows\r\n  installation. \r\n\r\n    Example: \r\n      DISM.exe /Online /?\r\n
0xc1500066 | The %1 option is unknown. \r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc1500067 | \r\nError: %1!d!\r\n\r\n
0xc1500068 | \r\nError: 0x%1!x!\r\n\r\n
0xc1500069 | The /Image option cannot be used in this context.\r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc150006a | The %1 argument given for the %2 option is invalid.\r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc150006b | Operation was incomplete because of a cancel request.\r\n
0xc150006c | Invalid command-line. \r\nFor more information, refer to the help.\r\n
0xc150006d | The %1 option has been duplicated on the command-line. \r\nRemove the duplicate option and try the command again.\r\n
0xc150006e | A destination path must be specified.\r\n
0xc150006f | The destination path %1!s! does not exist.\r\n

### 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.18362.900, 10.0.19041.1, 10.0.19041.572, 10.0.22000.1

Message identifier | Message string
--- | ---
0x01500020 | The operation completed successfully.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x81500027 | A error occurred while initializing the DISM event reporting component. \r\nFor more information, review the log file.\r\n
0x81500034 | Logging is disabled: Unable to obtain access to the log file %1!s!.\r\n
0x90000001 | Deployment Image Servicing And Management CLI\r\n
0xc1500003 | An initialization error occurred. \r\nFor more information, review the log file.\r\n
0xc1500004 | DISM doesn't recognize the command-line option "%1". \r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc1500005 | Invalid command-line argument. \r\nTo retrieve help, do not specify a command-line option with an argument.\r\n
0xc1500006 | An error occurred while parsing the command-line options specified. \r\nFor more information, review the log file.\r\n
0xc1500007 | An initialization error occurred while accessing the path to the offline image.\r\nFor more information, review the log file.\r\n
0xc1500008 | Unable to access the image. \r\nMake sure that the image path and the Windows directory for the image exist and you have Read permissions on the folder.\r\n
0xc150000a | An error occurred while processing the command-line options.\r\nFor more information, review the log file.\r\n
0xc150000e | The command-line is missing a required servicing command. \r\nFor more information, refer to the help by running DISM.exe /Image=<path_to_offline_image> /? where <path_to_the_offline_image> is the full path to an offline Windows image.\r\n
0xc1500010 | An error occurred while creating the log file. \r\nEnsure that the path to the log file exists and that you have Read/Write permissions on the folder where the log files will be created.\r\n
0xc1500011 | A path and file name were not specified for the /LogPath option. \r\nMake sure the /LogPath argument is not empty. For more information, refer to the help by running DISM.exe /LogPath /?\r\n
0xc1500012 | The option /WinDir is not recognized in this context. It can only be used with an offline image. \r\nFor more information, refer to the help by running DISM.exe /WinDir /?.\r\n
0xc1500013 | An error occurred closing a servicing component in the image. \r\nWait a few minutes and try running the command again.\r\n
0xc1500014 | Restart Windows to complete this operation.\r\n
0xc1500016 | Unable to automatically restart Windows. \r\nManually restart the computer to complete this operation.\r\n
0xc1500018 | Windows failed to restart. \r\nManually restart the computer to complete this operation.\r\n
0xc1500019 | Do not use the /Image or /WinDir option when using the /Online option to specify a running operating system. \r\nFor more information, refer to the help by running DISM.exe /Online /?.\r\n
0xc150001a | Unable to find the Windows directory in the running Windows installation. \r\nFor more information, review the log file.\r\n
0xc150001c | The /Image option that is specified points to a running Windows installation. \r\nTo service the running operating system, use the /Online option. For more information, refer to the help by running DISM.exe /Online /?.\r\n
0xc150001e | DISM failed. No operation was performed. \r\nFor more information, review the log file.\r\n
0xc150001f | An error occurred while accessing the DISM binaries in the image. \r\nFor more information, review the log file.\r\n
0xc1500021 | The %1 option is missing a required argument. \r\nFor more information, refer to the help by running DISM %1 /?.\r\n
0xc1500022 | DISM cannot service an image on a network path. \r\nMount the image locally and run DISM again.\r\n
0xc1500023 | An error occurred while attempting to access the image at %1.\r\nFor more information, review the log file.\r\n
0xc1500024 | An error occurred while attempting to access the image.\r\nFor more information, review the log file.\r\n
0xc1500025 | An error occurred accessing the DISM binaries on the host system. \r\nEnsure that the local DISM binaries exist and that you have Read permission on the folder.\r\n
0xc1500026 | An error occurred while validating the path to the image.\r\nEnsure that the image path is correct and that you have Read permissions on the folder.\r\n
0xc1500028 | An error occurred while accessing the temporary directory. \r\nEnsure that the path to the directory exists and that you have Read/Write permissions on the folder. For more information, refer to the help by running DISM.exe /ScratchDir /?.\r\n
0xc1500029 | The directory %1 does not appear to be a valid Windows directory.\r\nEnsure that the /WinDir option that is specified is valid. For more information, refer to the help by running DISM.exe /WinDir /?.\r\n
0xc150002a | Elevated permissions are required to run DISM. \r\nUse an elevated command prompt to complete these tasks.\r\n
0xc150002b | An error occurred while locating the DISM binaries. DISM is attempting to locate dismcore.dll. \r\nEnsure that the DISM binaries are present and that you have Read permissions on the folder. \r\n
0xc150002c | An error occurred while initializing COM security. \r\nTry running DISM again.\r\n
0xc150002d | The file %1 does not appear to be a valid DLL. \r\nEnsure that the file has not been corrupted. \r\n
0xc150002e | An error occurred while processing the command.\r\nEnsure that the command-line arguments are valid. For more information, review the log file.\r\n
0xc1500032 | An invalid log level was specified. \r\nFor more information, refer to the help by running DISM.exe /LogLevel /?. \r\n
0xc1500035 | The command-line is missing a required servicing command. \r\nFor more information, refer to the help by running DISM.exe /Online /?.\r\n
0xc1500036 | The DISM process encountered a problem and shutdown.\r\nFor more information, review the log file.\r\n
0xc1500038 | Image Version: %1!s!\r\n\r\n
0xc1500039 | No DISM options were specified on the command-line. \r\nRun DISM with a command-line option specified, such as /Image or /Online. For more information, refer to the help by running DISM.exe /?.\r\n
0xc150003a | An error occurred while loading DISM. The DISM tool may be corrupt. \r\nTry reinstalling DISM.\r\n
0xc150003c | DISM does not support servicing Windows PE with the /Online option.\r\n
0xc150003d | The %1 option does not take an argument. \r\nRemove the argument and run DISM again.\r\n
0xc150003e | An error occurred while initializing the log file. \r\nEnsure that the path to the log file is a valid. For more information, refer to the help by running DISM.exe /LogPath /?.\r\n
0xc150003f | DISM does not support servicing a Windows Vista RTM or earlier operating system. \r\nIf the operating system is supported check that SSShim.DLL is present.\r\n
0xc1500040 | An error occurred while attempting to start the servicing process for the image located at %1!s!. \r\nFor more information, review the log file.\r\n
0xc1500041 | DISM does not support servicing Windows Vista or Windows Server 2008 with the /Online option.\r\n
0xc1500042 | Invalid command-line option "%1". \r\nEnsure that /? is the last option listed on the command-line.\r\n
0xc1500043 | The %1 option is missing a required argument. \r\nFor more information, refer to the help for the %1 option.\r\n
0xc1500044 | Unable to access the System directory for the specified image. \r\nMake sure the System directory for the image exists and you have Read permissions on the folder.\r\n
0xc1500064 | No help topic could be found for the %1 option.\r\nSpecify an image to see relevant help topics, using either the /Image or\r\n/Online command-line option:\r\n\r\n/Image:<path_to_offline_image>  \r\n\r\n  This is the path to the root directory of the offline Windows image.\r\n\r\n    Example: \r\n      DISM.exe /Image:C:\test\offline /?\r\n\r\n/Online                 \r\n\r\n  Specifies that the operation is to be performed against the running Windows\r\n  installation. \r\n\r\n    Example: \r\n      DISM.exe /Online /?\r\n
0xc1500066 | The %1 option is unknown. \r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc1500067 | \r\nError: %1!d!\r\n\r\n
0xc1500068 | \r\nError: 0x%1!x!\r\n\r\n
0xc1500069 | The /Image option cannot be used in this context.\r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc150006a | The %1 argument given for the %2 option is invalid.\r\nFor more information, refer to the help by running DISM.exe /?.\r\n
0xc150006b | Operation was incomplete because of a cancel request.\r\n
0xc150006c | Invalid command-line. \r\nFor more information, refer to the help.\r\n
0xc150006d | The %1 option has been duplicated on the command-line. \r\nRemove the duplicate option and try the command again.\r\n
0xc150006e | A destination path must be specified.\r\n
0xc150006f | The destination path %1!s! does not exist.\r\n
