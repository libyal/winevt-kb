## mispace.dll

Path: %SystemRoot%\System32\mispace.dll

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000001 | Data is striped across physical disks, maximizing capacity and increasing throughput, but decreasing reliability. This storage layout requires at least one disk and does not protect you from a disk failure.%0\r\n
0x00000002 | Data is striped across physical disks, creating two or three copies of your data. This increases reliability, but reduces capacity. To protect against a single disk failure, use at least two disks (three if you're using a cluster); to protect against two disk failures, use at least five disks.%0\r\n
0x00000003 | Data and parity information are striped across physical disks, increasing reliability, but somewhat reducing capacity and performance. To protect against a single disk failure, use at least three disks; to protect against two disk failures, use at least seven disks.%0\r\n
0x00000004 | %1: Could not connect to subsystem "%2" on host "%3". Please check the credentials used and if this subsystem requires elevation.\r\n
0x00000005 | %1: An error was encountered while enumerating objects from subsystem "%2" on host "%3". Error encountered was %4 = "%6" (%5!u!).\r\n
0x00000006 | %1: An error was encountered while enumerating storage nodes or child objects for host %2. Error encountered was %3 = "%5" (%4!u!).\r\n
0x00000007 | %1: An error was encountered while enumerating storage nodes or child objects because it requires elevation.\r\n
0x00000008 | %1: An error was encountered while enumerating masking sets or child objects for host %2. Error encountered was %3 = "%5" (%4!u!).\r\n
0x00000009 | %1: An error was encountered while enumerating masking sets or child objects because it requires elevation.\r\n
0x0000000a | %1: An error was encountered while enumerating initiator ids or child objects for host %2. Error encountered was %3 = "%5" (%4!u!).\r\n
0x0000000b | %1: An error was encountered while enumerating initiator ids or child objects because it requires elevation.\r\n
0x0000000c | Cache out of date%0\r\n
0x0000000d | The access path that you provided was not applied to the CSV.\r\n
0x00000101 | Windows can't check the disk while it's in use.\r\nDo you want to check for hard disk errors the next time you start your computer?\r\n
0x00000102 | Windows can't check the volume while it's in use.\r\nDo you want to dismount this volume first? Note: All opened handles to this volume will become invalid.\r\n
0x00000103 | Scanning%0\r\n
0x00000104 | Repairing%0\r\n
0x00000105 | You do not have sufficient rights to check this drive.\r\n
0x00000106 | The disk is write protected.\r\n
0x00000107 | %1\r\n
0x00000108 | Volume compression was not enabled because it is not supported for the specified file system.\r\n
0x00000109 | Modifying short file name support is not supported for the specified file system.\r\n
0x0000010a | The specified file system is not supported on the drive.\r\n
0x0000010b | Windows cannot format this volume. Close any disk utilities or other programs that are using this volume, and make sure that no window is displaying the contents of the volume. Then try formatting again.\r\n
0x0000010c | This disk cannot be quick formatted.\r\n
0x0000010d | The volume label is not valid.\r\n
0x0000010e | The specified cluster size is too small.\r\n
0x0000010f | The specified cluster size is too large.\r\n
0x00000110 | The specified volume is too small.\r\n
0x00000111 | The specified volume is too large.\r\n
0x00000112 | The number of clusters exceeds 32 bits.\r\n
0x00000113 | The specified UDF version is not supported.\r\n
0x00000114 | The format might take a long time. You should not shut down the computer until the format is complete.\r\n
0x00000115 | A hardware error occurred while formatting this disc. You can  \r\ntry again with a different disc, but if this problem persists,  \r\nusing the Live File System on this drive is not recommended.  \r\nThe Mastered option should be used instead.  \r\n
0x00000116 | Warning, all data on the volume will be lost!\r\n
0x00000117 | Access Denied due to insufficient privileges.\r\nThis utility must be run in elevated mode.\r\n
0x00000118 | Windows could not open the volume for direct access.\r\n
0x00000119 | Windows could not determine the file system of volume %1.\r\n
0x0000011a | Formatting%0\r\n
0x0000011b | Volume integrity was not enabled because it is not supported for the specified file system.\r\n
0x0000011c | Creating new volume%0\r\n
0x0000011d | Resizing volume%0\r\n
0x00000201 | %1: No objects are returned from a subsystem on host "%2" because that subsystem doesn't support this type of object. Subsystem: "%3".\r\n
0x00000202 | %1: No objects are returned from a subsystem on host "%2" because that subsystem doesn't support remotely working with this type of object. Subsystem: "%3".\r\n
0x00000300 | Unable to retrieve stored credentials for subsystem %1 [%2].\r\n>>>>     Primary error = 0x%3!x!; Secondary error = 0x%4!x!\r\n
0x00000301 | Unable to impersonate the stored user %1 to access subsystem %2 [%3].\r\n>>>>     Primary error = 0x%4!x!; Secondary error = 0x%5!x!\r\n
0x00000302 | Unable to establish a connection to computer %1.\r\n>>>>     Primary error = 0x%2!x!; Secondary error = 0x%3!x!\r\n
0x00000303 | Unable to capture diagnostic info for computer %1.\r\n>>>>     Primary error = 0x%2!x!; Secondary error = 0x%3!x!\r\n
0x00000304 | Unable to clean up temporary diagnostic files on computer %1.\r\n>>>>     Primary error = 0x%2!x!; Secondary error = 0x%3!x!\r\n
0x00000305 | Failed to start traces on computer %1.\r\n>>>>     Primary error = 0x%2!x!; Secondary error = 0x%3!x!\r\n
0x00000306 | Failed to stop traces on computer %1.\r\n>>>>     Primary error = 0x%2!x!; Secondary error = 0x%3!x!\r\n
0x00000307 | Unable to copy diagnostic file for computer %1.\r\n>>>>     Source      [%2];\r\n>>>>     Destination [%3];\r\n>>>>     Primary error = 0x%4!x!; Secondary error = 0x%5!x!\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x51000001 | Critical\r\n
0x90000001 | Microsoft-Windows-StorageManagement-WSP-Spaces\r\n
0x91000001 | Microsoft-Windows-StorageManagement-WSP-Host\r\n
0xb00007d0 | The Windows Storage Provider could not start the remote storage subsystem.%n%nStorage Subsystem ID:%t%t%1%nStorage Subsystem URI:%t%2%nUsername:%t%t%t%3%nError Code:%t%t%t%4%nError String:%t%t%t%5%n%nEnsure that the remote storage subsystem is online and connected to the network.%nCheck if the user attempting to connect to the subsystem has the necessary permissions.\r\n
0xb00007d1 | The Windows Storage Provider has lost its connection to the cluster.\r\n
0xb00007d2 | The Windows Storage Provider has established a connection to the cluster.\r\n
0xb00007d3 | An error occurred during method execution.%n%nClass:%t%t%1%nMethod:%t%t%2%nObjectId:%t%3%nError Code:%t%4\r\n
0xb00007d4 | An error was posted by the Windows Storage Provider during the course of an operation.%n%nMessage:%t%1\r\n
0xb00007d5 | An error occurred during storage job execution.%n%nJob Name:%t%1%nError Code:%t%2\r\n
0xb00007d6 | An error occurred during a get instance operation.%n%nClass:%t%t%1%nObjectId:%t%2%nError Code:%t%3\r\n
0xb00007d7 | An error occurred during object enumeration.%n%nClass:%t%t%1%nError Code:%t%2\r\n
0xb00007d8 | An error occurred during method execution.%n%nClass:%t%t%1%nMethod:%t%t%2%nObjectId:%t%3%nMI_Result:%t%4\r\n
0xb00007d9 | An error occurred while trying to perform a diagnostic operation.%n%nComputer name: %1%nError Code: %2%nSecondary Error: %3\r\n
0xb10003e8 | A Windows Storage Provider failed to load.%n%nProvider:%t%t%1%nProvider DLL:%t%2%nError Code:%t%3%nLoad Phase:%t%4%n%nThis failure is indicative of a bad installation, or a missing or corrupt DLL.\r\n
0xd1000001 | Loading DLL\r\n
0xd1000002 | Find ShutdownCallback\r\n
0xd1000003 | Find WMI Entrypoint\r\n
0xd1000004 | Launch Hosted Provider\r\n
