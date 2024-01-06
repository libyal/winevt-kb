## discan.dll

Path: %SystemRoot%\System32\discan.dll

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | Data Integrity Task started.\r\n
0xb0000004 | Data Integrity Task completed.\r\n
0xb000000b | Disk scan started for disk number %1.\r\n
0xb000000c | Disk scan completed for disk number %1.\r\n
0xb0000015 | Volume scan started. Volume name: %4 (%2).\r\n
0xb0000016 | Volume scan completed. Volume name: %4 (%2); repaired: %11 bytes; not repaired: %12 bytes; HResult: %5.\r\n
0xb0000017 | Volume scan was partially completed. Volume name: %4 (%2); repaired: %11 bytes; not repaired: %12 bytes; HResult: %5.\r\n
0xb0000018 | %6 file(s) were skipped by volume scan. Volume name: %4 (%2); first skipped file name: %8; HResult: %5.\r\n
0xb0000036 | File data inconsistency was detected and was repaired successfully. File name: %2; range offset: %4; range length: %5 bytes; repaired: %6 bytes; status: %8.\r\n
0xb0000037 | File data scrub operation failed. File name: %2; range offset: %4; range length: %5 bytes; repaired: %6 bytes; not repaired: %7 bytes; status: %8.\r\n
0xb0000038 | Volume metadata inconsistency was detected and was repaired successfully. Volume name: %2; metadata reference: %3; range offset: %4; range length: %5 bytes; repaired: %6 bytes; status: %8.\r\n
0xb0000039 | Volume metadata scrub operation failed. Volume name: %2; metadata reference: %3; range offset: %4; range length: %5 bytes; repaired: %6 bytes; not repaired: %7 bytes; status: %8.\r\n
0xb000003a | File metadata inconsistency was detected and was repaired successfully. File name: %2; metadata reference: %3; range offset: %4; range length: %5 bytes; repaired: %6 bytes; status: %8.\r\n
0xb000003b | File metadata scrub operation failed. File name: %2; metadata reference: %3; range offset: %4; range length: %5 bytes; repaired: %6 bytes; not repaired: %7 bytes; status: %8.\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | Started checking data integrity.\r\n
0xb0000004 | Completed data integrity checks.\r\n
0xb000000b | Disk scan started. Disk number: %1\r\n
0xb000000c | Disk scan completed. Disk number: %1\r\n
0xb0000015 | Volume scan started. Volume name: %4 (%2).\r\n
0xb0000016 | Volume scan completed. Volume name: %4 (%2); bytes repaired: %11; bytes not repaired: %12; HResult: %5.\r\n
0xb0000017 | Volume scan was partially completed. Volume name: %4 (%2); bytes repaired: %11; bytes not repaired: %12; HResult: %5.\r\n
0xb0000018 | Files were skipped during the volume scan. Files skipped: %6; volume name: %4 (%2); first skipped file name: %8; HResult: %5.\r\n
0xb0000036 | File data inconsistency was detected and was repaired successfully. File name: %2; range offset: %4; range length (in bytes): %5; bytes repaired: %6; status: %8.\r\n
0xb0000037 | File data scrub operation failed. File name: %2; range offset: %4; range length (in bytes): %5; bytes repaired: %6; bytes not repaired: %7; status: %8.\r\n
0xb0000038 | Volume metadata inconsistency was detected and was repaired successfully. Volume name: %2; metadata reference: %3; range offset: %4; range length (in bytes): %5; bytes repaired: %6; status: %8.\r\n
0xb0000039 | Volume metadata scrub operation failed. Volume name: %2; metadata reference: %3; range offset: %4; range length (in bytes): %5; bytes repaired: %6; bytes not repaired: %7; status: %8.\r\n
0xb000003a | File metadata inconsistency was detected and was repaired successfully. File name: %2; metadata reference: %3; range offset: %4; range length (in bytes): %5; bytes repaired: %6; status: %8.\r\n
0xb000003b | File metadata scrub operation failed. File name: %2; metadata reference: %3; range offset: %4; range length (in bytes): %5; bytes repaired: %6; bytes not repaired: %7; status: %8.\r\n
0xb000003c | File data inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required. File name: %2; range offset: %4; range length (in bytes): %5; bytes repaired: %6; status: %8.\r\n
0xb000003d | Volume metadata inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required. Volume name: %2; metadata reference: %3; range offset: %4; range length (in bytes): %5; bytes repaired: %6; status: %8.\r\n
0xb000003e | File metadata inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required. File name: %2; metadata reference: %3; range offset: %4; range length (in bytes): %5; bytes repaired: %6; status: %8.\r\n
0xb00000a0 | Parity repair completed. Volume name: %4 (%2); extent count: %5; length (in bytes): %6.\r\n
0xb00000a1 | Parity repair failed. Volume name: %4 (%2); extent count: %5; length (in bytes): %6; HResult: %7.\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | Started checking data integrity.\r\n
0xb0000004 | Completed data integrity checks.\r\n
0xb000000b | Disk scan started on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb000000c | Disk scan completed on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb0000015 | Volume scan started on %4 (%2) in \\?\PhysicalDrive%5 (\\?\Disk%6)\r\n
0xb0000016 | Volume scan completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb0000017 | Volume scan was partially completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb0000018 | Files were skipped during the volume scan.%nFiles skipped: %6%nVolume name: %4 (%2)%nFirst skipped file name: %8%nHResult: %5\r\n
0xb0000036 | File data inconsistency was detected and was repaired successfully.%nFile name: %2%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb0000037 | File data scrub operation failed.%nFile name: %2%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nBytes not repaired: %7%nStatus: %8\r\n
0xb0000038 | Volume metadata inconsistency was detected and was repaired successfully.%nVolume name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb0000039 | Volume metadata scrub operation failed.%nVolume name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nBytes not repaired: %7%nStatus: %8\r\n
0xb000003a | File metadata inconsistency was detected and was repaired successfully.%nFile name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb000003b | File metadata scrub operation failed.%nFile name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nBytes not repaired: %7%nStatus: %8\r\n
0xb000003c | File data inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required.%nFile name: %2%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb000003d | Volume metadata inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required.%nVolume name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb000003e | File metadata inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required.%nFile name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb0000065 | Started checking data integrity for crash recovery.\r\n
0xb0000068 | Completed data integrity checks for crash recovery.\r\n
0xb000006f | Crash recovery disk scan started on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb0000070 | Crash recovery disk scan completed on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb0000079 | Crash recovery volume scan started on %4 (%2) in \\?\PhysicalDrive%5 (\\?\Disk%9)\r\n
0xb000007a | Crash recovery volume scan completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb000007b | Volume scan was partially completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb00000a0 | Parity repair completed.%nVolume name: %4 (%2)%nExtent count: %5%nLength (in bytes): %6\r\n
0xb00000a1 | Parity repair failed.%nVolume name: %4 (%2)%nExtent count: %5%nLength (in bytes): %6%nHResult: %7\r\n

### 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | Started checking data integrity.\r\n
0xb0000004 | Completed data integrity checks.\r\n
0xb000000b | Disk scan started on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb000000c | Disk scan completed on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb0000015 | Volume scan started on %4 (%2) in \\?\PhysicalDrive%5 (\\?\Disk%6)\r\n
0xb0000016 | Volume scan completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb0000017 | Volume scan was partially completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb0000018 | Files were skipped during the volume scan.%nFiles skipped: %6%nVolume name: %4 (%2)%nFirst skipped file name: %8%nHResult: %5\r\n
0xb000001b | Volume scan completion at %17% on %4 (%2)%nBytes repaired: %10%nBytes not repaired: %11\r\n
0xb0000036 | File data inconsistency was detected and was repaired successfully.%nFile name: %2%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb0000037 | File data scrub operation failed.%nFile name: %2%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nBytes not repaired: %7%nStatus: %8\r\n
0xb0000038 | Volume metadata inconsistency was detected and was repaired successfully.%nVolume name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb0000039 | Volume metadata scrub operation failed.%nVolume name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nBytes not repaired: %7%nStatus: %8\r\n
0xb000003a | File metadata inconsistency was detected and was repaired successfully.%nFile name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb000003b | File metadata scrub operation failed.%nFile name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nBytes not repaired: %7%nStatus: %8\r\n
0xb000003c | File data inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required.%nFile name: %2%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb000003d | Volume metadata inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required.%nVolume name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb000003e | File metadata inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required.%nFile name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb0000065 | Started checking data integrity for crash recovery.\r\n
0xb0000068 | Completed data integrity checks for crash recovery.\r\n
0xb000006f | Crash recovery disk scan started on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb0000070 | Crash recovery disk scan completed on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb0000079 | Crash recovery volume scan started on %4 (%2) in \\?\PhysicalDrive%5 (\\?\Disk%9)\r\n
0xb000007a | Crash recovery volume scan completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb000007b | Volume scan was partially completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb000007f | Drt clear completed on %4 (%2)%nHResult: %5\r\n
0xb0000081 | Crash recovery volume scan completion at %18% on %4 (%2)%nBytes repaired: %10%nBytes not repaired: %11\r\n
0xb00000a0 | Parity repair completed.%nVolume name: %4 (%2)%nExtent count: %5%nLength (in bytes): %6\r\n
0xb00000a1 | Parity repair failed.%nVolume name: %4 (%2)%nExtent count: %5%nLength (in bytes): %6%nHResult: %7\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | Started checking data integrity.\r\n
0xb0000004 | Completed data integrity checks.\r\n
0xb000000b | Disk scan started on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb000000c | Disk scan completed on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb0000015 | Volume scan started on %4 (%2) in \\?\PhysicalDrive%5 (\\?\Disk%6)\r\n
0xb0000016 | Volume scan completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb0000017 | Volume scan was partially completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb0000018 | Files were skipped during the volume scan.%nFiles skipped: %6%nVolume name: %4 (%2)%nFirst skipped file name: %8%nHResult: %5\r\n
0xb000001b | Volume scan completion at %25% on %4 (%2)%nBytes repaired: %10%nBytes not repaired: %11\r\n
0xb0000036 | File data inconsistency was detected and was repaired successfully.%nFile name: %2%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb0000037 | File data scrub operation failed.%nFile name: %2%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nBytes not repaired: %7%nStatus: %8\r\n
0xb0000038 | Volume metadata inconsistency was detected and was repaired successfully.%nVolume name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb0000039 | Volume metadata scrub operation failed.%nVolume name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nBytes not repaired: %7%nStatus: %8\r\n
0xb000003a | File metadata inconsistency was detected and was repaired successfully.%nFile name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb000003b | File metadata scrub operation failed.%nFile name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nBytes not repaired: %7%nStatus: %8\r\n
0xb000003c | File data inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required.%nFile name: %2%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb000003d | Volume metadata inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required.%nVolume name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb000003e | File metadata inconsistency was detected and the parity repair was scheduled at the end of the task. No user action is required.%nFile name: %2%nMetadata reference: %3%nRange offset: %4%nRange length (in bytes): %5%nBytes repaired: %6%nStatus: %8\r\n
0xb0000065 | Started checking data integrity for crash recovery.\r\n
0xb0000068 | Completed data integrity checks for crash recovery.\r\n
0xb000006f | Crash recovery disk scan started on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb0000070 | Crash recovery disk scan completed on \\?\PhysicalDrive%1 (\\?\Disk%2)\r\n
0xb0000079 | Crash recovery volume scan started on %4 (%2) in \\?\PhysicalDrive%5 (\\?\Disk%9)\r\n
0xb000007a | Crash recovery volume scan completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb000007b | Volume scan was partially completed on %4 (%2)%nBytes repaired: %11%nBytes not repaired: %12%nHResult: %5\r\n
0xb000007f | Drt clear completed on %4 (%2)%nHResult: %5\r\n
0xb0000081 | Crash recovery volume scan completion at %26% on %4 (%2)%nBytes repaired: %10%nBytes not repaired: %11\r\n
0xb00000a0 | Parity repair completed.%nVolume name: %4 (%2)%nExtent count: %5%nLength (in bytes): %6\r\n
0xb00000a1 | Parity repair failed.%nVolume name: %4 (%2)%nExtent count: %5%nLength (in bytes): %6%nHResult: %7\r\n
