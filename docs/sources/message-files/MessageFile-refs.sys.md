## refs.sys

Path: %SystemRoot%\system32\drivers\refs.sys

### 6.3.9600.16384, 6.3.9600.18514

Message identifier | Message string
--- | ---
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.\r\n
0x00000084 | The file system detected a checksum error and was able to correct it. The name of the file or folder is "%2".\r\n
0x00000085 | The file system detected a checksum error and was not able to correct it. The name of the file or folder is "%2".\r\n
0x00000086 | The file system was unable to write metadata to the media backing volume %2. A write failed with status "%3" ReFS will take the volume offline. It may be mounted again automatically.\r\n
0x00000087 | Volume %2 is formatted as ReFS but ReFS is unable to mount it; ReFS encountered status %3.\r\n
0x00000088 | Volume "%2" was mounted in an older version of Windows. Some features may be lost.\r\n
0x00000201 | The file system detected a corruption on a file. The file has been removed from the file system namespace. The name of the file is "%2".\r\n
0x00000202 | The file system detected a corruption on a file. The file system may have failed to remove it from the file system namespace. The name of the file is "%2".\r\n
0x00000203 | The file system detected a corruption on a folder. Contents of the folder have been removed from the file system namespace. The name of the folder is "%2".\r\n
0x00000204 | The file system detected a corruption on a folder. The file system may have failed to remove contents of the folder from the file system namespace. The name of the folder is "%2".\r\n
0x00000207 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000208 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000209 | Volume "%2" detected a corruption on file system metadata. It will lose self-healing features.\r\n
0x00001f00 | <unable to determine file name>\r\n
0x10000034 | SQM\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | System\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.\r\n
0x00000084 | The file system detected a checksum error and was able to correct it. The name of the file or folder is "%2".\r\n
0x00000085 | The file system detected a checksum error and was not able to correct it. The name of the file or folder is "%2".\r\n
0x00000086 | The file system was unable to write metadata to the media backing volume %2. A write failed with status "%3" ReFS will take the volume offline. It may be mounted again automatically.\r\n
0x00000087 | Volume %2 is formatted as ReFS but ReFS is unable to mount it; ReFS encountered status %3.\r\n
0x00000088 | Volume "%2" was mounted in an older version of Windows. Some features may be lost.\r\n
0x00000089 | The file system was unable to write metadata to the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008a | The file system was unable to open redo log for the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008b | The file system detected a global metadata corruption and was able to repair it on volume %2. Space may be leaked as part of the repair. If future mounts fail, attempting a readonly volume mount may succeed.\r\n
0x0000008c | The file system detected a global metadata corruption and was not able to repair it on volume %2. Attempting a readonly volume mount may succeed.\r\n
0x00000201 | The file system detected a corruption on a file. The file has been removed from the file system namespace. The name of the file is "%2".\r\n
0x00000202 | The file system detected a corruption on a file. The file system may have failed to remove it from the file system namespace. The name of the file is "%2".\r\n
0x00000203 | The file system detected a corruption on a folder. Contents of the folder have been removed from the file system namespace. The name of the folder is "%2".\r\n
0x00000204 | The file system detected a corruption on a folder. The file system may have failed to remove contents of the folder from the file system namespace. The name of the folder is "%2".\r\n
0x00000205 | The file system determined that there were multiple volumes on the given disk so has disabled read cache for the volume "%2".  Status is "%3".\r\n
0x00000206 | The file system could not determine if there were multiple volumes on the given disk (status is "%3") so has disabled read cache for the volume "%2".\r\n
0x00000207 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000208 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000209 | Volume "%2" detected a corruption on file system metadata. It will lose self-healing features.\r\n
0x00001f00 | <unable to determine file name>\r\n
0x10000016 | Statistics\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | ReFS\r\n
0x90000002 | System\r\n
0xb0000004 | The ReFS volume has been successfully mounted.%n%nVolume GUID:%4%nVolume Name:%6%nVolume Label:%8%nDevice Name:%3\r\n
0xb0000005 | ReFS failed to mount the volume.%nContext: %1%nError: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7\r\n
0xb0000006 | ReFS is mounting the volume.%nContext: %1%nProgress: %2\r\n
0xb0000007 | ReFS failed to mount the volume. Version %4.%5 doesn't match expected value %2.%3 %nContext: %1%n\r\n
0xb0000008 | ReFS fast tier is filling up for volume.%n Context: %1%nFillRatio: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7 \r\n
0xb0000091 | IO latency summary common data for volume:%n%n\n          Volume Id: %1%n\n          Volume name: %3%n%n\n          Max Acceptable IO Latency: %5 ms%n\n          Read/Write latency buckets (us): [%6, %7, %8, %9, %10, %11, %12]%n\n          Trim latency buckets (us): [%13, %14, %15, %16, %17, %18, %19]%n\n          Flush latency buckets (us): [%20, %21, %22, %23, %24, %25, %26]%n\r\n
0xb0000092 | IO latency summary:%n%n\n          Volume Id: %1%n\n          Volume name: %3%n%n\n          Interval duration: %6 us%n%n\n          Non-cached reads:%n\n                    IO count: %7%n\n                    Total bytes: %8%n\n                    Avg latency: %9 ns%n%n\n          Non-cached writes: %n\n                    IO count: %10%n\n                    Total bytes: %11%n\n                    Avg latency: %12 ns%n%n\n          File flushes: %n\n                    IO count: %13%n\n                    Avg latency: %14 ns%n%n\n          Directory flushes: %n\n                    IO count: %15%n\n                    Avg latency: %16 ns%n%n\n          Volume flushes: %n\n                    IO count: %17%n\n                    Avg latency: %18 ns%n%n\n          File level trims: %n\n                    IO count: %19%n\n                    Total bytes: %20%n\n                    Extents count: %21%n\n                    Avg latency: %22 ns%n%n\n          Volume trims: %n\n                    IO count: %23%n\n                    Total bytes: %24%n\n                    Extents count: %25%n\n                    Avg latency: %26 ns%n%n\nFor more details see the details tab.%n\r\n
0xb0000093 | An IO took more than %5 ms to complete:%n%n\n          Process Id: %6%n\n          Process name: %7%n\n          File name: %9%n\n          File offset: %12%n\n          IO Type: %10%n\n          IO Size: %11 bytes%n\n          %15 cluster(s) starting at cluster %14%n\n          Latency: %13 ms%n%n\n          Volume Id: %1%n\n          Volume name: %3%n\r\n
0xb0000094 | A %9 failed with %14.%n%n\n          Process Id: %5%n\n          Process name: %6%n\n          File name: %8%n\n          IO Size: %10 bytes%n\n          File offset: %11%n\n          %13 cluster(s) starting at cluster %12%n%n\n          Volume Id: %1%n\n          Volume name: %3%n\r\n
0xb0000095 | In the past %5 seconds we had IO failures.%n%n\n          High latency IO count: %6%n\n          Failed writes: %7%n\n          Failed reads: %8%n\n          Volume Id: %1%n\n          Volume name: %3%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xd0000001 | Write: NonPaging, NonCached, Async\r\n
0xd0000002 | Write: NonPaging, NonCached, Sync\r\n
0xd0000003 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd0000004 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd0000005 | Write: NonPaging, Cached, Async\r\n
0xd0000006 | Write: NonPaging, Cached, Sync\r\n
0xd0000007 | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd0000008 | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd0000009 | Write: Paging, NonCached, Async\r\n
0xd000000a | Write: Paging, NonCached, Sync\r\n
0xd000000b | Write: Paging, NonCached, Async, Writethrough\r\n
0xd000000c | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd000000d | Read: NonPaging, NonCached, Async\r\n
0xd000000e | Read: NonPaging, NonCached, Sync\r\n
0xd000000f | Read: NonPaging, Cached, Async\r\n
0xd0000010 | Read: NonPaging, Cached, Sync\r\n
0xd0000011 | Read: Paging, NonCached, Async\r\n
0xd0000012 | Read: Paging, NonCached, Sync\r\n
0xd0000013 | read\r\n
0xd0000014 | write\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.\r\n
0x00000084 | The file system detected a checksum error and was able to correct it. The name of the file or folder is "%2".\r\n
0x00000085 | The file system detected a checksum error and was not able to correct it. The name of the file or folder is "%2".\r\n
0x00000086 | The file system was unable to write metadata to the media backing volume %2. A write failed with status "%3" ReFS will take the volume offline. It may be mounted again automatically.\r\n
0x00000087 | Volume %2 is formatted as ReFS but ReFS is unable to mount it; ReFS encountered status %3.\r\n
0x00000088 | Volume "%2" was mounted in an older version of Windows. Some features may be lost.\r\n
0x00000089 | The file system was unable to write metadata to the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008a | The file system was unable to open redo log for the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008b | The file system detected a global metadata corruption and was able to repair it on volume %2. Space may be leaked as part of the repair. If future mounts fail, attempting a readonly volume mount may succeed.\r\n
0x0000008c | The file system detected a global metadata corruption and was not able to repair it on volume %2. Attempting a readonly volume mount may succeed.\r\n
0x00000201 | The file system detected a corruption on a file. The file has been removed from the file system namespace. The name of the file is "%2".\r\n
0x00000202 | The file system detected a corruption on a file. The file system may have failed to remove it from the file system namespace. The name of the file is "%2".\r\n
0x00000203 | The file system detected a corruption on a folder. Contents of the folder have been removed from the file system namespace. The name of the folder is "%2".\r\n
0x00000204 | The file system detected a corruption on a folder. The file system may have failed to remove contents of the folder from the file system namespace. The name of the folder is "%2".\r\n
0x00000205 | The file system determined that there were multiple volumes on the given disk so has disabled read cache for the volume "%2".  Status is "%3".\r\n
0x00000206 | The file system could not determine if there were multiple volumes on the given disk (status is "%3") so has disabled read cache for the volume "%2".\r\n
0x00000207 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000208 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000209 | Volume "%2" detected a corruption on file system metadata. It will lose self-healing features.\r\n
0x00001f00 | <unable to determine file name>\r\n
0x10000016 | Statistics\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | ReFS\r\n
0x90000002 | System\r\n
0xb0000004 | The ReFS volume has been successfully mounted.%n%nVolume GUID:%4%nVolume Name:%6%nVolume Label:%8%nDevice Name:%3\r\n
0xb0000005 | ReFS failed to mount the volume.%nContext: %1%nError: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7\r\n
0xb0000006 | ReFS is mounting the volume.%nContext: %1%nProgress: %2\r\n
0xb0000007 | ReFS failed to mount the volume. Version %4.%5 doesn't match expected value %2.%3 %nContext: %1%n\r\n
0xb0000008 | ReFS fast tier is filling up for volume.%n Context: %1%nFillRatio: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7 \r\n
0xb0000092 | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Interval duration: %6 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %7%n\r\n                    Total bytes: %8%n\r\n                    Avg latency: %9 ns%n%n\r\n          Non-cached writes: %n\r\n                    IO count: %10%n\r\n                    Total bytes: %11%n\r\n                    Avg latency: %12 ns%n%n\r\n          File flushes: %n\r\n                    IO count: %13%n\r\n                    Avg latency: %14 ns%n%n\r\n          Directory flushes: %n\r\n                    IO count: %15%n\r\n                    Avg latency: %16 ns%n%n\r\n          Volume flushes: %n\r\n                    IO count: %17%n\r\n                    Avg latency: %18 ns%n%n\r\n          File level trims: %n\r\n                    IO count: %19%n\r\n                    Total bytes: %20%n\r\n                    Extents count: %21%n\r\n                    Avg latency: %22 ns%n%n\r\n          Volume trims: %n\r\n                    IO count: %23%n\r\n                    Total bytes: %24%n\r\n                    Extents count: %25%n\r\n                    Avg latency: %26 ns%n%n\r\nFor more details see the details tab.%n\r\n
0xb0000093 | An IO took more than %5 ms to complete:%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          File offset: %12%n\r\n          IO Type: %10%n\r\n          IO Size: %11 bytes%n\r\n          %15 cluster(s) starting at cluster %14%n\r\n          Latency: %13 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n
0xb0000094 | A %9 failed with %14.%n%n\r\n          Process Id: %5%n\r\n          Process name: %6%n\r\n          File name: %8%n\r\n          IO Size: %10 bytes%n\r\n          File offset: %11%n\r\n          %13 cluster(s) starting at cluster %12%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n
0xb0000095 | In the past %5 seconds we had IO failures.%n%n\r\n          High latency IO count: %6%n\r\n          Failed writes: %7%n\r\n          Failed reads: %8%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n
0xb0010091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Max Acceptable IO Latency: %5 ms%n\r\n          Read/Write latency buckets (ns): [%6, %7, %8, %9, %10, %11, %12]%n\r\n          Trim latency buckets (ns): [%13, %14, %15, %16, %17, %18, %19]%n\r\n          Flush latency buckets (ns): [%20, %21, %22, %23, %24, %25, %26]%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xd0000001 | Write: NonPaging, NonCached, Async\r\n
0xd0000002 | Write: NonPaging, NonCached, Sync\r\n
0xd0000003 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd0000004 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd0000005 | Write: NonPaging, Cached, Async\r\n
0xd0000006 | Write: NonPaging, Cached, Sync\r\n
0xd0000007 | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd0000008 | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd0000009 | Write: Paging, NonCached, Async\r\n
0xd000000a | Write: Paging, NonCached, Sync\r\n
0xd000000b | Write: Paging, NonCached, Async, Writethrough\r\n
0xd000000c | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd000000d | Read: NonPaging, NonCached, Async\r\n
0xd000000e | Read: NonPaging, NonCached, Sync\r\n
0xd000000f | Read: NonPaging, Cached, Async\r\n
0xd0000010 | Read: NonPaging, Cached, Sync\r\n
0xd0000011 | Read: Paging, NonCached, Async\r\n
0xd0000012 | Read: Paging, NonCached, Sync\r\n
0xd0000013 | read\r\n
0xd0000014 | write\r\n

### 10.0.16299.15, 10.0.17134.648

Message identifier | Message string
--- | ---
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.\r\n
0x00000084 | The file system detected a checksum error and was able to correct it. The name of the file or folder is "%2".\r\n
0x00000085 | The file system detected a checksum error and was not able to correct it. The name of the file or folder is "%2".\r\n
0x00000086 | The file system was unable to write metadata to the media backing volume %2. A write failed with status "%3" ReFS will take the volume offline. It may be mounted again automatically.\r\n
0x00000087 | Volume %2 is formatted as ReFS but ReFS is unable to mount it; ReFS encountered status %3.\r\n
0x00000088 | Volume "%2" was mounted in an older version of Windows. Some features may be lost.\r\n
0x00000089 | The file system was unable to write metadata to the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008a | The file system was unable to open redo log for the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008b | The file system detected a global metadata corruption and was able to repair it on volume %2. Space may be leaked as part of the repair. If future mounts fail, attempting a readonly volume mount may succeed.\r\n
0x0000008c | The file system detected a global metadata corruption and was not able to repair it on volume %2. Attempting a readonly volume mount may succeed.\r\n
0x00000201 | The file system detected a corruption on a file. The file has been removed from the file system namespace. The name of the file is "%2".\r\n
0x00000202 | The file system detected a corruption on a file. The file system may have failed to remove it from the file system namespace. The name of the file is "%2".\r\n
0x00000203 | The file system detected a corruption on a folder. Contents of the folder have been removed from the file system namespace. The name of the folder is "%2".\r\n
0x00000204 | The file system detected a corruption on a folder. The file system may have failed to remove contents of the folder from the file system namespace. The name of the folder is "%2".\r\n
0x00000205 | The file system determined that there were multiple volumes on the given disk so has disabled read cache for the volume "%2".  Status is "%3".\r\n
0x00000206 | The file system could not determine if there were multiple volumes on the given disk (status is "%3") so has disabled read cache for the volume "%2".\r\n
0x00000207 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000208 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000209 | Volume "%2" detected a corruption on file system metadata. It will lose self-healing features.\r\n
0x0000020a | The file system detected and fixed volume size inconsistency in boot sector of volume "%2".\r\n
0x00001f00 | <unable to determine file name>\r\n
0x10000016 | Statistics\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | ReFS\r\n
0x90000002 | System\r\n
0xb0000004 | The ReFS volume has been successfully mounted.%n%nVolume GUID:%4%nVolume Name:%6%nVolume Label:%8%nDevice Name:%3\r\n
0xb0000005 | ReFS failed to mount the volume.%nContext: %1%nError: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7\r\n
0xb0000006 | ReFS is mounting the volume.%nContext: %1%nProgress: %2\r\n
0xb0000007 | ReFS failed to mount the volume. Version %4.%5 doesn't match expected value %2.%3 %nContext: %1%n\r\n
0xb0000008 | ReFS fast tier is filling up for volume.%n Context: %1%nFillRatio: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7 \r\n
0xb0000094 | A %10 failed with %15.%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          IO Size: %11 bytes%n\r\n          File offset: %12%n\r\n          %14 cluster(s) starting at cluster %13%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5%n\r\n
0xb0000095 | In the past %5 seconds we had IO failures.%n%n\r\n          High latency IO count: %6%n\r\n          Failed writes: %7%n\r\n          Failed reads: %8%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n
0xb0010092 | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5%n%n\r\n          Interval duration: %7 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %8%n\r\n                    Total bytes: %9%n\r\n                    Avg latency: %10 ns%n%n\r\n          Non-cached writes: %n\r\n                    IO count: %11%n\r\n                    Total bytes: %12%n\r\n                    Avg latency: %13 ns%n%n\r\n          File flushes: %n\r\n                    IO count: %14%n\r\n                    Avg latency: %15 ns%n%n\r\n          Directory flushes: %n\r\n                    IO count: %16%n\r\n                    Avg latency: %17 ns%n%n\r\n          Volume flushes: %n\r\n                    IO count: %17%n\r\n                    Avg latency: %18 ns%n%n\r\n          File level trims: %n\r\n                    IO count: %20%n\r\n                    Total bytes: %21%n\r\n                    Extents count: %22%n\r\n                    Avg latency: %23 ns%n%n\r\n          Volume trims: %n\r\n                    IO count: %24%n\r\n                    Total bytes: %25%n\r\n                    Extents count: %26%n\r\n                    Avg latency: %27 ns%n%n\r\nFor more details see the details tab.%n\r\n
0xb0010093 | An IO took more than %6 ms to complete:%n%n\r\n          Process Id: %7%n\r\n          Process name: %8%n\r\n          File name: %10%n\r\n          File offset: %13%n\r\n          IO Type: %11%n\r\n          IO Size: %12 bytes%n\r\n          %15 cluster(s) starting at cluster %15%n\r\n          Latency: %14 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5\r\n
0xb0020091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Tier Index %5%n\r\n          Max Acceptable IO Latency: %6 ms%n\r\n          Read/Write latency buckets (ns): [%7, %8, %9, %10, %11, %12, %13]%n\r\n          Trim latency buckets (ns): [%14, %15, %16, %17, %18, %19, %20]%n\r\n          Flush latency buckets (ns): [%21, %22, %23, %24, %25, %26, %27]%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xd0000001 | Write: NonPaging, NonCached, Async\r\n
0xd0000002 | Write: NonPaging, NonCached, Sync\r\n
0xd0000003 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd0000004 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd0000005 | Write: NonPaging, Cached, Async\r\n
0xd0000006 | Write: NonPaging, Cached, Sync\r\n
0xd0000007 | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd0000008 | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd0000009 | Write: Paging, NonCached, Async\r\n
0xd000000a | Write: Paging, NonCached, Sync\r\n
0xd000000b | Write: Paging, NonCached, Async, Writethrough\r\n
0xd000000c | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd000000d | Read: NonPaging, NonCached, Async\r\n
0xd000000e | Read: NonPaging, NonCached, Sync\r\n
0xd000000f | Read: NonPaging, Cached, Async\r\n
0xd0000010 | Read: NonPaging, Cached, Sync\r\n
0xd0000011 | Read: Paging, NonCached, Async\r\n
0xd0000012 | Read: Paging, NonCached, Sync\r\n
0xd0000013 | read\r\n
0xd0000014 | write\r\n

### 10.0.17763.404

Message identifier | Message string
--- | ---
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.\r\n
0x00000084 | The file system detected a checksum error and was able to correct it. The name of the file or folder is "%2".\r\n
0x00000085 | The file system detected a checksum error and was not able to correct it. The name of the file or folder is "%2".\r\n
0x00000086 | The file system was unable to write metadata to the media backing volume %2. A write failed with status "%3" ReFS will take the volume offline. It may be mounted again automatically.\r\n
0x00000087 | Volume %2 is formatted as ReFS but ReFS is unable to mount it; ReFS encountered status %3.\r\n
0x00000088 | Volume "%2" was mounted in an older version of Windows. Some features may be lost.\r\n
0x00000089 | The file system was unable to write metadata to the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008a | The file system was unable to open redo log for the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008b | The file system detected a global metadata corruption and was able to repair it on volume %2. Space may be leaked as part of the repair. If future mounts fail, attempting a readonly volume mount may succeed.\r\n
0x0000008c | The file system detected a global metadata corruption and was not able to repair it on volume %2. Attempting a readonly volume mount may succeed.\r\n
0x00000201 | The file system detected a corruption on a file. The file has been removed from the file system namespace. The name of the file is "%2".\r\n
0x00000202 | The file system detected a corruption on a file. The file system may have failed to remove it from the file system namespace. The name of the file is "%2".\r\n
0x00000203 | The file system detected a corruption on a folder. Contents of the folder have been removed from the file system namespace. The name of the folder is "%2".\r\n
0x00000204 | The file system detected a corruption on a folder. The file system may have failed to remove contents of the folder from the file system namespace. The name of the folder is "%2".\r\n
0x00000205 | The file system determined that there were multiple volumes on the given disk so has disabled read cache for the volume "%2".  Status is "%3".\r\n
0x00000206 | The file system could not determine if there were multiple volumes on the given disk (status is "%3") so has disabled read cache for the volume "%2".\r\n
0x00000207 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000208 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000209 | Volume "%2" detected a corruption on file system metadata. It will lose self-healing features.\r\n
0x0000020a | The file system detected and fixed volume size inconsistency in boot sector of volume "%2".\r\n
0x00001f00 | <unable to determine file name>\r\n
0x10000016 | Statistics\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | ReFS\r\n
0x90000002 | System\r\n
0xb0000004 | The ReFS volume has been successfully mounted.%n%nVolume GUID:%4%nVolume Name:%6%nVolume Label:%8%nDevice Name:%3\r\n
0xb0000005 | ReFS failed to mount the volume.%nContext: %1%nError: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7\r\n
0xb0000006 | ReFS is mounting the volume.%nContext: %1%nProgress: %2\r\n
0xb0000007 | ReFS failed to mount the volume. Version %4.%5 doesn't match expected value %2.%3 %nContext: %1%n\r\n
0xb0000008 | ReFS fast tier is filling up for volume.%n Context: %1%nFillRatio: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7 \r\n
0xb0000094 | A %10 failed with %15.%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          IO Size: %11 bytes%n\r\n          File offset: %12%n\r\n          %14 cluster(s) starting at cluster %13%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5%n\r\n
0xb0000095 | In the past %5 seconds we had IO failures.%n%n\r\n          High latency IO count: %6%n\r\n          Failed writes: %7%n\r\n          Failed reads: %8%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n
0xb0010092 | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5%n%n\r\n          Interval duration: %7 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %8%n\r\n                    Total bytes: %9%n\r\n                    Avg latency: %10 ns%n%n\r\n          Non-cached writes: %n\r\n                    IO count: %11%n\r\n                    Total bytes: %12%n\r\n                    Avg latency: %13 ns%n%n\r\n          File flushes: %n\r\n                    IO count: %14%n\r\n                    Avg latency: %15 ns%n%n\r\n          Directory flushes: %n\r\n                    IO count: %16%n\r\n                    Avg latency: %17 ns%n%n\r\n          Volume flushes: %n\r\n                    IO count: %17%n\r\n                    Avg latency: %18 ns%n%n\r\n          File level trims: %n\r\n                    IO count: %20%n\r\n                    Total bytes: %21%n\r\n                    Extents count: %22%n\r\n                    Avg latency: %23 ns%n%n\r\n          Volume trims: %n\r\n                    IO count: %24%n\r\n                    Total bytes: %25%n\r\n                    Extents count: %26%n\r\n                    Avg latency: %27 ns%n%n\r\nFor more details see the details tab.%n\r\n
0xb0010093 | An IO took more than %6 ms to complete:%n%n\r\n          Process Id: %7%n\r\n          Process name: %8%n\r\n          File name: %10%n\r\n          File offset: %13%n\r\n          IO Type: %11%n\r\n          IO Size: %12 bytes%n\r\n          %15 cluster(s) starting at cluster %15%n\r\n          Latency: %14 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5\r\n
0xb0010096 | SMR information summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Sample Duration: %4%n%n\r\n          Free Space Minimum (Randomly-Writable Tier): %5%n\r\n          Free Space Maximum (Randomly-Writable Tier): %6%n\r\n          Free Space Average (Randomly-Writable Tier): %7%n%n\r\n          Free Space Minimum (SMR Tier): %8%n\r\n          Free Space Maximum (SMR Tier): %9%n\r\n          Free Space Average (SMR Tier): %10%n%n\r\n          Usable Free Space Mininum (SMR Tier): %11%n\r\n          Usable Free Space Maximum (SMR Tier): %12%n\r\n          Usable Free Space Average (SMR Tier): %13%n%n\r\n          Write Serialization Aborted Writes: %14%n\r\n          Write Serialization Events: %15%n\r\n          Write Serialization Latency Average: %16%n\r\n          Write Serialization Latency Maximum: %17%n\r\n          Write Serialization Blocked Events: %18%n\r\n          Write Serialization Blocked Latency Average: %19%n%n\r\n          Start Garbage Collection Calls Invoked: %20%n\r\n          Start Garbage Collection Calls Failed: %21%n\r\n          Start Garbage Collection Full Speed Calls Invoked: %22%n\r\n          Start Garbage Collection Full Speed Calls Failed: %23%n\r\n          Pause Garbage Collection Calls Invoked: %24%n\r\n          Pause Garbage Collection Calls Failed: %25%n\r\n          Stop Garbage Collection Calls Invoked: %26%n\r\n          Stop Garbage Collection Calls Failed: %27%n%n\r\n          Full SMR Band Cluster Allocations: %28%n\r\n          Shared SMR Band Cluster Allocations: %29%n%n\r\n          Garbage Collection Read Latency Total: %30%n\r\n          Garbage Collection Read Latency Average: %31%n\r\n          Garbage Collection Read Latency Maximum: %32%n\r\n          Garbage Collection Total Read IOs: %33%n\r\n          Garbage Collection Write Latency Total: %34%n\r\n          Garbage Collection Write Latency Average: %35%n\r\n          Garbage Collection Write Latency Maximum: %36%n\r\n          Garbage Collection Total Write IOs: %37%n\r\n          Disk Full Requires Garbage Collection: %38%n%n\r\n          SMR Zone Full Events: %39%n\r\n          CMR Zone Full Events: %40%n%n\r\n          Invalid Sector Errors: %41%n\r\n          IO Device Errors: %42%n\r\n          Write Errors: %43%n\r\n          Read Errors: %44%n\r\n          SMR Write-Head Requeries: %45%n\r\n
0xb0020091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Tier Index %5%n\r\n          Max Acceptable IO Latency: %6 ms%n\r\n          Read/Write latency buckets (ns): [%7, %8, %9, %10, %11, %12, %13]%n\r\n          Trim latency buckets (ns): [%14, %15, %16, %17, %18, %19, %20]%n\r\n          Flush latency buckets (ns): [%21, %22, %23, %24, %25, %26, %27]%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xd0000001 | Write: NonPaging, NonCached, Async\r\n
0xd0000002 | Write: NonPaging, NonCached, Sync\r\n
0xd0000003 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd0000004 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd0000005 | Write: NonPaging, Cached, Async\r\n
0xd0000006 | Write: NonPaging, Cached, Sync\r\n
0xd0000007 | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd0000008 | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd0000009 | Write: Paging, NonCached, Async\r\n
0xd000000a | Write: Paging, NonCached, Sync\r\n
0xd000000b | Write: Paging, NonCached, Async, Writethrough\r\n
0xd000000c | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd000000d | Read: NonPaging, NonCached, Async\r\n
0xd000000e | Read: NonPaging, NonCached, Sync\r\n
0xd000000f | Read: NonPaging, Cached, Async\r\n
0xd0000010 | Read: NonPaging, Cached, Sync\r\n
0xd0000011 | Read: Paging, NonCached, Async\r\n
0xd0000012 | Read: Paging, NonCached, Sync\r\n
0xd0000013 | read\r\n
0xd0000014 | write\r\n

### 10.0.18362.1, 10.0.18362.693

Message identifier | Message string
--- | ---
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.\r\n
0x00000084 | The file system detected a checksum error and was able to correct it. The name of the file or folder is "%2".\r\n
0x00000085 | The file system detected a checksum error and was not able to correct it. The name of the file or folder is "%2".\r\n
0x00000086 | The file system was unable to write metadata to the media backing volume %2. A write failed with status "%3" ReFS will take the volume offline. It may be mounted again automatically.\r\n
0x00000087 | Volume %2 is formatted as ReFS but ReFS is unable to mount it; ReFS encountered status %3.\r\n
0x00000088 | Volume "%2" was mounted in an older version of Windows. Some features may be lost.\r\n
0x00000089 | The file system was unable to write metadata to the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008a | The file system was unable to open redo log for the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008b | The file system detected a global metadata corruption and was able to repair it on volume %2. Space may be leaked as part of the repair. If future mounts fail, attempting a readonly volume mount may succeed.\r\n
0x0000008c | The file system detected a global metadata corruption and was not able to repair it on volume %2. Attempting a readonly volume mount may succeed.\r\n
0x00000201 | The file system detected a corruption on a file. The file has been removed from the file system namespace. The name of the file is "%2".\r\n
0x00000202 | The file system detected a corruption on a file. The file system may have failed to remove it from the file system namespace. The name of the file is "%2".\r\n
0x00000203 | The file system detected a corruption on a folder. Contents of the folder have been removed from the file system namespace. The name of the folder is "%2".\r\n
0x00000204 | The file system detected a corruption on a folder. The file system may have failed to remove contents of the folder from the file system namespace. The name of the folder is "%2".\r\n
0x00000205 | The file system determined that there were multiple volumes on the given disk so has disabled read cache for the volume "%2".  Status is "%3".\r\n
0x00000206 | The file system could not determine if there were multiple volumes on the given disk (status is "%3") so has disabled read cache for the volume "%2".\r\n
0x00000207 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000208 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000209 | Volume "%2" detected a corruption on file system metadata. It will lose self-healing features.\r\n
0x0000020a | The file system detected and fixed volume size inconsistency in boot sector of volume "%2".\r\n
0x00001f00 | <unable to determine file name>\r\n
0x10000016 | Statistics\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | ReFS\r\n
0x90000002 | System\r\n
0xb0000004 | The ReFS volume has been successfully mounted.%n%nVolume GUID:%4%nVolume Name:%6%nVolume Label:%8%nDevice Name:%3\r\n
0xb0000005 | ReFS failed to mount the volume.%nContext: %1%nError: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7\r\n
0xb0000006 | ReFS is mounting the volume.%nContext: %1%nProgress: %2\r\n
0xb0000007 | ReFS failed to mount the volume. Version %4.%5 doesn't match expected value %2.%3 %nContext: %1%n\r\n
0xb0000008 | ReFS fast tier is filling up for volume.%n Context: %1%nFillRatio: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7 \r\n
0xb0000094 | A %10 failed with %15.%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          IO Size: %11 bytes%n\r\n          File offset: %12%n\r\n          %14 cluster(s) starting at cluster %13%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5%n\r\n
0xb0000095 | In the past %5 seconds we had IO failures.%n%n\r\n          High latency IO count: %6%n\r\n          Failed writes: %7%n\r\n          Failed reads: %8%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n
0xb0010093 | An IO took more than %6 ms to complete:%n%n\r\n          Process Id: %7%n\r\n          Process name: %8%n\r\n          File name: %10%n\r\n          File offset: %13%n\r\n          IO Type: %11%n\r\n          IO Size: %12 bytes%n\r\n          %15 cluster(s) starting at cluster %15%n\r\n          Latency: %14 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5\r\n
0xb0010096 | SMR information summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Sample Duration: %4%n%n\r\n          Free Space Minimum (Randomly-Writable Tier): %5%n\r\n          Free Space Maximum (Randomly-Writable Tier): %6%n\r\n          Free Space Average (Randomly-Writable Tier): %7%n%n\r\n          Free Space Minimum (SMR Tier): %8%n\r\n          Free Space Maximum (SMR Tier): %9%n\r\n          Free Space Average (SMR Tier): %10%n%n\r\n          Usable Free Space Mininum (SMR Tier): %11%n\r\n          Usable Free Space Maximum (SMR Tier): %12%n\r\n          Usable Free Space Average (SMR Tier): %13%n%n\r\n          Write Serialization Aborted Writes: %14%n\r\n          Write Serialization Events: %15%n\r\n          Write Serialization Latency Average: %16%n\r\n          Write Serialization Latency Maximum: %17%n\r\n          Write Serialization Blocked Events: %18%n\r\n          Write Serialization Blocked Latency Average: %19%n%n\r\n          Start Garbage Collection Calls Invoked: %20%n\r\n          Start Garbage Collection Calls Failed: %21%n\r\n          Start Garbage Collection Full Speed Calls Invoked: %22%n\r\n          Start Garbage Collection Full Speed Calls Failed: %23%n\r\n          Pause Garbage Collection Calls Invoked: %24%n\r\n          Pause Garbage Collection Calls Failed: %25%n\r\n          Stop Garbage Collection Calls Invoked: %26%n\r\n          Stop Garbage Collection Calls Failed: %27%n%n\r\n          Full SMR Band Cluster Allocations: %28%n\r\n          Shared SMR Band Cluster Allocations: %29%n%n\r\n          Garbage Collection Read Latency Total: %30%n\r\n          Garbage Collection Read Latency Average: %31%n\r\n          Garbage Collection Read Latency Maximum: %32%n\r\n          Garbage Collection Total Read IOs: %33%n\r\n          Garbage Collection Write Latency Total: %34%n\r\n          Garbage Collection Write Latency Average: %35%n\r\n          Garbage Collection Write Latency Maximum: %36%n\r\n          Garbage Collection Total Write IOs: %37%n\r\n          Disk Full Requires Garbage Collection: %38%n%n\r\n          SMR Zone Full Events: %39%n\r\n          CMR Zone Full Events: %40%n%n\r\n          Invalid Sector Errors: %41%n\r\n          IO Device Errors: %42%n\r\n          Write Errors: %43%n\r\n          Read Errors: %44%n\r\n          SMR Write-Head Requeries: %45%n\r\n
0xb0020091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Tier Index %5%n\r\n          Max Acceptable IO Latency: %6 ms%n\r\n          Read/Write latency buckets (ns): [%7, %8, %9, %10, %11, %12, %13]%n\r\n          Trim latency buckets (ns): [%14, %15, %16, %17, %18, %19, %20]%n\r\n          Flush latency buckets (ns): [%21, %22, %23, %24, %25, %26, %27]%n\r\n
0xb0020092 | IO latency summary:%n%n\r\n          Version: %1%n\r\n          Volume Id: %2%n\r\n          Volume name: %4%n\r\n          Tier index: %6%n%n\r\n          Max Acceptable IO Latency: %7 ms%n%n\r\n          Read/Write latency buckets (ns): [%8, %9, %10, %11, %12, %13, %14]%n\r\n          Trim latency buckets (ns): [%15, %16, %17, %18, %19, %20, %21]%n\r\n          Flush latency buckets (ns): [%22, %23, %24, %25, %26, %27, %28]%n%n\r\n          Interval duration: %30 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %31%n\r\n                    Total bytes: %32%n\r\n                    Avg latency: %33 ns%n%n\r\n          Non-cached writes: %n\r\n                    IO count: %34%n\r\n                    Total bytes: %35%n\r\n                    Avg latency: %36 ns%n%n\r\n          File flushes: %n\r\n                    IO count: %37%n\r\n                    Avg latency: %38 ns%n%n\r\n          Directory flushes: %n\r\n                    IO count: %39%n\r\n                    Avg latency: %40 ns%n%n\r\n          Volume flushes: %n\r\n                    IO count: %41%n\r\n                    Avg latency: %42 ns%n%n\r\n          File level trims: %n\r\n                    IO count: %43%n\r\n                    Total bytes: %44%n\r\n                    Extents count: %45%n\r\n                    Avg latency: %46 ns%n%n\r\n          Volume trims: %n\r\n                    IO count: %47%n\r\n                    Total bytes: %48%n\r\n                    Extents count: %49\r\n                    Avg latency: %50 ns%n%n\r\nFor more details see the details tab.%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xd0000001 | Write: NonPaging, NonCached, Async\r\n
0xd0000002 | Write: NonPaging, NonCached, Sync\r\n
0xd0000003 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd0000004 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd0000005 | Write: NonPaging, Cached, Async\r\n
0xd0000006 | Write: NonPaging, Cached, Sync\r\n
0xd0000007 | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd0000008 | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd0000009 | Write: Paging, NonCached, Async\r\n
0xd000000a | Write: Paging, NonCached, Sync\r\n
0xd000000b | Write: Paging, NonCached, Async, Writethrough\r\n
0xd000000c | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd000000d | Read: NonPaging, NonCached, Async\r\n
0xd000000e | Read: NonPaging, NonCached, Sync\r\n
0xd000000f | Read: NonPaging, Cached, Async\r\n
0xd0000010 | Read: NonPaging, Cached, Sync\r\n
0xd0000011 | Read: Paging, NonCached, Async\r\n
0xd0000012 | Read: Paging, NonCached, Sync\r\n
0xd0000013 | read\r\n
0xd0000014 | write\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.\r\n
0x00000084 | The file system detected a checksum error and was able to correct it. The name of the file or folder is "%2".\r\n
0x00000085 | The file system detected a checksum error and was not able to correct it. The name of the file or folder is "%2".\r\n
0x00000086 | The file system was unable to write metadata to the media backing volume %2. A write failed with status "%3" ReFS will take the volume offline. It may be mounted again automatically.\r\n
0x00000087 | Volume %2 is formatted as ReFS but ReFS is unable to mount it; ReFS encountered status %3.\r\n
0x00000088 | Volume "%2" was mounted in an older version of Windows. Some features may be lost.\r\n
0x00000089 | The file system was unable to write metadata to the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008a | The file system was unable to open redo log for the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008b | The file system detected a global metadata corruption and was able to repair it on volume %2. Space may be leaked as part of the repair. If future mounts fail, attempting a readonly volume mount may succeed.\r\n
0x0000008c | The file system detected a global metadata corruption and was not able to repair it on volume %2. Attempting a readonly volume mount may succeed.\r\n
0x0000008d | The file system has skipped replaying the redo log on volume %2. Pending log records will not be applied. ReFS will mount the volume without applying the redo log.\r\n
0x00000201 | The file system detected a corruption on a file. The file has been removed from the file system namespace. The name of the file is "%2".\r\n
0x00000202 | The file system detected a corruption on a file. The file system may have failed to remove it from the file system namespace. The name of the file is "%2".\r\n
0x00000203 | The file system detected a corruption on a folder. Contents of the folder have been removed from the file system namespace. The name of the folder is "%2".\r\n
0x00000204 | The file system detected a corruption on a folder. The file system may have failed to remove contents of the folder from the file system namespace. The name of the folder is "%2".\r\n
0x00000205 | The file system determined that there were multiple volumes on the given disk so has disabled read cache for the volume "%2".  Status is "%3".\r\n
0x00000206 | The file system could not determine if there were multiple volumes on the given disk (status is "%3") so has disabled read cache for the volume "%2".\r\n
0x00000207 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000208 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000209 | Volume "%2" detected a corruption on file system metadata. It will lose self-healing features.\r\n
0x0000020a | The file system detected and fixed volume size inconsistency in boot sector of volume "%2".\r\n
0x00001f00 | <unable to determine file name>\r\n
0x10000016 | Statistics\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | ReFS\r\n
0x90000002 | System\r\n
0xb0000004 | The ReFS volume has been successfully mounted.%n%nVolume GUID:%4%nVolume Name:%6%nVolume Label:%8%nDevice Name:%3\r\n
0xb0000005 | ReFS failed to mount the volume.%nContext: %1%nError: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7\r\n
0xb0000006 | ReFS is mounting the volume.%nContext: %1%nProgress: %2\r\n
0xb0000007 | ReFS failed to mount the volume. Version %4.%5 doesn't match expected value %2.%3 %nContext: %1%n\r\n
0xb0000008 | ReFS fast tier is filling up for volume.%n Context: %1%nFillRatio: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7 \r\n
0xb0000094 | A %10 failed with %15.%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          IO Size: %11 bytes%n\r\n          File offset: %12%n\r\n          %14 cluster(s) starting at cluster %13%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5%n\r\n
0xb0000095 | In the past %5 seconds we had IO failures.%n%n\r\n          High latency IO count: %6%n\r\n          Failed writes: %7%n\r\n          Failed reads: %8%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n
0xb0010093 | An IO took more than %6 ms to complete:%n%n\r\n          Process Id: %7%n\r\n          Process name: %8%n\r\n          File name: %10%n\r\n          File offset: %13%n\r\n          IO Type: %11%n\r\n          IO Size: %12 bytes%n\r\n          %15 cluster(s) starting at cluster %15%n\r\n          Latency: %14 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5\r\n
0xb0010096 | SMR information summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Sample Duration: %4%n%n\r\n          Free Space Minimum (Randomly-Writable Tier): %5%n\r\n          Free Space Maximum (Randomly-Writable Tier): %6%n\r\n          Free Space Average (Randomly-Writable Tier): %7%n%n\r\n          Free Space Minimum (SMR Tier): %8%n\r\n          Free Space Maximum (SMR Tier): %9%n\r\n          Free Space Average (SMR Tier): %10%n%n\r\n          Usable Free Space Mininum (SMR Tier): %11%n\r\n          Usable Free Space Maximum (SMR Tier): %12%n\r\n          Usable Free Space Average (SMR Tier): %13%n%n\r\n          Write Serialization Aborted Writes: %14%n\r\n          Write Serialization Events: %15%n\r\n          Write Serialization Latency Average: %16%n\r\n          Write Serialization Latency Maximum: %17%n\r\n          Write Serialization Blocked Events: %18%n\r\n          Write Serialization Blocked Latency Average: %19%n%n\r\n          Start Garbage Collection Calls Invoked: %20%n\r\n          Start Garbage Collection Calls Failed: %21%n\r\n          Start Garbage Collection Full Speed Calls Invoked: %22%n\r\n          Start Garbage Collection Full Speed Calls Failed: %23%n\r\n          Pause Garbage Collection Calls Invoked: %24%n\r\n          Pause Garbage Collection Calls Failed: %25%n\r\n          Stop Garbage Collection Calls Invoked: %26%n\r\n          Stop Garbage Collection Calls Failed: %27%n%n\r\n          Full SMR Band Cluster Allocations: %28%n\r\n          Shared SMR Band Cluster Allocations: %29%n%n\r\n          Garbage Collection Read Latency Total: %30%n\r\n          Garbage Collection Read Latency Average: %31%n\r\n          Garbage Collection Read Latency Maximum: %32%n\r\n          Garbage Collection Total Read IOs: %33%n\r\n          Garbage Collection Write Latency Total: %34%n\r\n          Garbage Collection Write Latency Average: %35%n\r\n          Garbage Collection Write Latency Maximum: %36%n\r\n          Garbage Collection Total Write IOs: %37%n\r\n          Disk Full Requires Garbage Collection: %38%n%n\r\n          SMR Zone Full Events: %39%n\r\n          CMR Zone Full Events: %40%n%n\r\n          Invalid Sector Errors: %41%n\r\n          IO Device Errors: %42%n\r\n          IO Unaligned Write Errors: %43%n\r\n          Write Errors: %44%n\r\n          Read Errors: %45%n\r\n          SMR Write-Head Requeries: %46%n\r\n
0xb0020091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Tier Index %5%n\r\n          Max Acceptable IO Latency: %6 ms%n\r\n          Read/Write latency buckets (ns): [%7, %8, %9, %10, %11, %12, %13]%n\r\n          Trim latency buckets (ns): [%14, %15, %16, %17, %18, %19, %20]%n\r\n          Flush latency buckets (ns): [%21, %22, %23, %24, %25, %26, %27]%n\r\n
0xb0020092 | IO latency summary:%n%n\r\n          Version: %1%n\r\n          Volume Id: %2%n\r\n          Volume name: %4%n\r\n          Tier index: %6%n%n\r\n          Max Acceptable IO Latency: %7 ms%n%n\r\n          Read/Write latency buckets (ns): [%8, %9, %10, %11, %12, %13, %14]%n\r\n          Trim latency buckets (ns): [%15, %16, %17, %18, %19, %20, %21]%n\r\n          Flush latency buckets (ns): [%22, %23, %24, %25, %26, %27, %28]%n%n\r\n          Interval duration: %30 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %31%n\r\n                    Total bytes: %32%n\r\n                    Avg latency: %33 ns%n%n\r\n          Non-cached writes: %n\r\n                    IO count: %34%n\r\n                    Total bytes: %35%n\r\n                    Avg latency: %36 ns%n%n\r\n          File flushes: %n\r\n                    IO count: %37%n\r\n                    Avg latency: %38 ns%n%n\r\n          Directory flushes: %n\r\n                    IO count: %39%n\r\n                    Avg latency: %40 ns%n%n\r\n          Volume flushes: %n\r\n                    IO count: %41%n\r\n                    Avg latency: %42 ns%n%n\r\n          File level trims: %n\r\n                    IO count: %43%n\r\n                    Total bytes: %44%n\r\n                    Extents count: %45%n\r\n                    Avg latency: %46 ns%n%n\r\n          Volume trims: %n\r\n                    IO count: %47%n\r\n                    Total bytes: %48%n\r\n                    Extents count: %49\r\n                    Avg latency: %50 ns%n%n\r\nFor more details see the details tab.%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xd0000001 | Write: NonPaging, NonCached, Async\r\n
0xd0000002 | Write: NonPaging, NonCached, Sync\r\n
0xd0000003 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd0000004 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd0000005 | Write: NonPaging, Cached, Async\r\n
0xd0000006 | Write: NonPaging, Cached, Sync\r\n
0xd0000007 | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd0000008 | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd0000009 | Write: Paging, NonCached, Async\r\n
0xd000000a | Write: Paging, NonCached, Sync\r\n
0xd000000b | Write: Paging, NonCached, Async, Writethrough\r\n
0xd000000c | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd000000d | Read: NonPaging, NonCached, Async\r\n
0xd000000e | Read: NonPaging, NonCached, Sync\r\n
0xd000000f | Read: NonPaging, Cached, Async\r\n
0xd0000010 | Read: NonPaging, Cached, Sync\r\n
0xd0000011 | Read: Paging, NonCached, Async\r\n
0xd0000012 | Read: Paging, NonCached, Sync\r\n
0xd0000013 | read\r\n
0xd0000014 | write\r\n

### 10.0.22000.65

Message identifier | Message string
--- | ---
0x00000082 | The file system structure on volume %2 has now been repaired.\r\n
0x00000083 | The file system structure on volume %2 cannot be corrected.\r\n
0x00000084 | The file system detected a checksum error and was able to correct it. The name of the file or folder is "%2".\r\n
0x00000085 | The file system detected a checksum error and was not able to correct it. The name of the file or folder is "%2".\r\n
0x00000086 | The file system was unable to write metadata to the media backing volume %2. A write failed with status "%3" ReFS will take the volume offline. It may be mounted again automatically.\r\n
0x00000087 | Volume %2 is formatted as ReFS but ReFS is unable to mount it; ReFS encountered status %3.\r\n
0x00000088 | Volume "%2" was mounted in an older version of Windows. Some features may be lost.\r\n
0x00000089 | The file system was unable to write metadata to the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008a | The file system was unable to open redo log for the media backing volume %2. Log redo failed with status "%3" . The volume is being mounted without the log applied.\r\n
0x0000008b | The file system detected a global metadata corruption and was able to repair it on volume %2. Space may be leaked as part of the repair. If future mounts fail, attempting a readonly volume mount may succeed.\r\n
0x0000008c | The file system detected a global metadata corruption and was not able to repair it on volume %2. Attempting a readonly volume mount may succeed.\r\n
0x0000008d | The file system has skipped replaying the redo log on volume %2. Pending log records will not be applied. ReFS will mount the volume without applying the redo log.\r\n
0x00000201 | The file system detected a corruption on a file. The file has been removed from the file system namespace. The name of the file is "%2".\r\n
0x00000202 | The file system detected a corruption on a file. The file system may have failed to remove it from the file system namespace. The name of the file is "%2".\r\n
0x00000203 | The file system detected a corruption on a folder. Contents of the folder have been removed from the file system namespace. The name of the folder is "%2".\r\n
0x00000204 | The file system detected a corruption on a folder. The file system may have failed to remove contents of the folder from the file system namespace. The name of the folder is "%2".\r\n
0x00000205 | The file system determined that there were multiple volumes on the given disk so has disabled read cache for the volume "%2".  Status is "%3".\r\n
0x00000206 | The file system could not determine if there were multiple volumes on the given disk (status is "%3") so has disabled read cache for the volume "%2".\r\n
0x00000207 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000208 | The file system detected a corruption on file system metadata. The name of the stream is "%2".\r\n
0x00000209 | Volume "%2" detected a corruption on file system metadata. It will lose self-healing features.\r\n
0x0000020a | The file system detected and fixed volume size inconsistency in boot sector of volume "%2".\r\n
0x10000003 | Volume Dismount\r\n
0x10000016 | Statistics\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000007 | Resume\r\n
0x30000008 | Suspend\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Volume dismount\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x90000001 | ReFS\r\n
0x90000002 | System\r\n
0xb0000005 | ReFS failed to mount the volume.%nContext: %1%nError: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7\r\n
0xb0000006 | ReFS is mounting the volume.%nContext: %1%nProgress: %2\r\n
0xb0000007 | ReFS failed to mount the volume. Version %4.%5 doesn't match expected value %2.%3 %nContext: %1%n\r\n
0xb0000008 | ReFS fast tier is filling up for volume.%n Context: %1%nFillRatio: %2%n%nVolume GUID:%3%nDeviceName:%5%nVolume Name:%7 \r\n
0xb000008e | Summary of disk space usage, since last event:%n%n\r\n          Available clusters: %8 (%9)%n\r\n          Reserved clusters: %10 (%11)%n\r\n          Metadata clusters: %12 (%13)%n\r\n          Used clusters: %14 (%15)%n\r\n          %n\r\n          Volume size: %17%n\r\n          Bytes per cluster: %18%n\r\n          %n\r\n          Volume correlation ID: %1%n\r\n          Volume name: %3%n\r\n          Device name: %5%n\r\n          Space ID: %6%n\r\n          %n\r\n          Elapsed seconds: %7%n\r\n
0xb0000094 | A %10 failed with %15.%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          IO Size: %11 bytes%n\r\n          File offset: %12%n\r\n          %14 cluster(s) starting at cluster %13%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5%n\r\n
0xb0000095 | In the past %5 seconds we had IO failures.%n%n\r\n          High latency IO count: %6%n\r\n          Failed writes: %7%n\r\n          Failed reads: %8%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n
0xb000012c | ReFS volume dismount has started.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Device name: %5%n\r\n          %n\r\n          Process Id: %7%n\r\n          Process name: %8%n\r\n          %n\r\n          Reason: %9%n\r\n          %n\r\n          Number of dirty metadata pages: %10%n\r\n          Number of dirty table list entries: %11%n\r\n
0xb000012d | ReFS volume dismount notification sent.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Device name: %5%n\r\n
0xb000012e | ReFS volume  dismount notification completed.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Device name: %5%n\r\n          %n\r\n          Dismount notification duration: %7\r\n
0xb000012f | ReFS volume was successfully dismounted.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Device name: %5%n\r\n          %n\r\n          Process Id: %7%n\r\n          Process name: %8%n\r\n          %n\r\n          Reason: %9%n\r\n          %n\r\n          Dismount notification duration: %10%n\r\n          Dismount duration: %12%n\r\n          %n\r\n          Number of dirty metadata pages when dismount began: %14%n\r\n          Number of dirty table list entries when dismount began: %15%n\r\n          Number of pages dirtied during dismount: %16\r\n
0xb0000130 | ReFS dismount failed.%n%n\r\n          Volume correlation Id: %1%n\r\n          Volume name: %3%n\r\n          Device name: %5%n\r\n          %n\r\n          Error: %7\r\n
0xb0010004 | The ReFS volume has been successfully mounted.%n%n\r\n                        VCB Address: %1%n\r\n                        Volume GUID: %2%n\r\n                        Device Name: %4%n\r\n                        Volume Name: %6%n\r\n                        Cluster Size Bytes: %7%n\r\n                        Volume Size Bytes: %8%n\r\n                        Free Space Bytes: %9%n\r\n                        Redo Log LCN Count: %10%n\r\n                        Logical Sector Size Bytes: %11%n\r\n                        Physical Sector Size Bytes: %12%n\r\n                        Actual Physical Sector Size Bytes: %13%n\r\n                        Major Version: %14%n\r\n                        Minor Version: %15%n\r\n                        Number of Physical Copies: %16%n\r\n                        Number of Logical Copies: %17%n\r\n                        Volume ID for Heat: %18%n\r\n                        Root Integrity Stream Checksum Type: %19%n\r\n                        Volume State: %20%n\r\n                        USN Size: %21%n\r\n                        Security Descriptor Stream Size: %22%n\r\n                        Mount Duration (microseconds): %23%n\r\n                        Debug Version: %24%n\r\n                        Debugger Enabled: %25%n\r\n                        SSD Tier Size: %26%n\r\n                        Read Cache Size: %27%n\r\n                        Read Cache Line Size: %28%n\r\n                        Container Rotation Enabled: %29%n\r\n                        Delete Notification Disabled: %30%n\r\n                        VCB State Flags: %31%n\r\n                        VCB State Flags 2: %32%n\r\n                        Checkpoint Virtual Clock: %33%n\r\n                        Last Write Time: %34%n\r\n                        Boot Sector Flags: %35%n\r\n                        ReFS Data Flags %36%n\r\n                        Last Shutdown Was Dirty: %37%n\r\n                        Streams Supported: %38%n\r\n                        User Streams Available: %39%n\r\n                        Size of Randomly Writeable Tier: %40%n\r\n                        Size of SMR Tier: %41%n\r\n                        Log Restart Start LSN: %42%n\r\n                        Log Restart Last LSN: %43%n\r\n                        Log Restart Duration (microseconds): %44\r\n
0xb001008e | Summary of disk space usage, since last event:%n%n\r\n          Volume is thinly provisioned%n%n\r\n          Available clusters: %8 (%9)%n\r\n          Reserved clusters: %10 (%11)%n\r\n          Metadata clusters: %12 (%13)%n\r\n          Used clusters: %14 (%15)%n\r\n          %n\r\n          Volume size: %17%n\r\n          Bytes per cluster: %18%n\r\n          %n\r\n          Mapped clusters: %19 (%20)%n\r\n          Available mapped clusters: %21 (%22)%n\r\n          Slab size: %24%n\r\n          Slabs mapped: %26%n\r\n          Slabs mapped change: %27%n\r\n          Slabs required for volume: %28%n\r\n          %n\r\n          Map operations since mount: %29%n\r\n          Map operations during last interval: %30%n\r\n          Map failures since mount: %31%n\r\n          Map failures during last interval: %32%n\r\n          Mapped bytes since mount: %33 (%34)%n\r\n          Mapped bytes during last interval: %35 (%36)%n\r\n          %n\r\n          Unmap operations since mount: %37%n\r\n          Unmap operations during last interval: %38%n\r\n          Unmap failures since mount: %39%n\r\n          Unmap failures during last interval: %40%n\r\n          Unmapped bytes since mount: %41 (%42)%n\r\n          Unmapped bytes during last interval: %43 (%44)%n\r\n          %n\r\n          Volume correlation ID: %1%n\r\n          Volume name: %3%n\r\n          Device name: %5%n\r\n          Space ID: %6%n\r\n          %n\r\n          Elapsed seconds: %7%n\r\n
0xb0010093 | An IO took more than %6 ms to complete:%n%n\r\n          Process Id: %7%n\r\n          Process name: %8%n\r\n          File name: %10%n\r\n          File offset: %13%n\r\n          IO Type: %11%n\r\n          IO Size: %12 bytes%n\r\n          %16 cluster(s) starting at cluster %15%n\r\n          Latency: %14 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5\r\n
0xb0010094 | A %12 failed with %17.%n%n\r\n          Process Id: %6%n\r\n          Process name: %7%n\r\n          File name: %9%n\r\n          IO Size: %13 bytes%n\r\n          File offset: %14%n\r\n          %16 cluster(s) starting at cluster %15%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5%n\r\n
0xb0010096 | SMR information summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Sample Duration: %4%n%n\r\n          Free Space Minimum (Randomly-Writable Tier): %5%n\r\n          Free Space Maximum (Randomly-Writable Tier): %6%n\r\n          Free Space Average (Randomly-Writable Tier): %7%n%n\r\n          Free Space Minimum (SMR Tier): %8%n\r\n          Free Space Maximum (SMR Tier): %9%n\r\n          Free Space Average (SMR Tier): %10%n%n\r\n          Usable Free Space Minimum (SMR Tier): %11%n\r\n          Usable Free Space Maximum (SMR Tier): %12%n\r\n          Usable Free Space Average (SMR Tier): %13%n%n\r\n          Write Serialization Aborted Writes: %14%n\r\n          Write Serialization Events: %15%n\r\n          Write Serialization Latency Average: %16%n\r\n          Write Serialization Latency Maximum: %17%n\r\n          Write Serialization Blocked Events: %18%n\r\n          Write Serialization Blocked Latency Average: %19%n%n\r\n          Start Garbage Collection Calls Invoked: %20%n\r\n          Start Garbage Collection Calls Failed: %21%n\r\n          Start Garbage Collection Full Speed Calls Invoked: %22%n\r\n          Start Garbage Collection Full Speed Calls Failed: %23%n\r\n          Pause Garbage Collection Calls Invoked: %24%n\r\n          Pause Garbage Collection Calls Failed: %25%n\r\n          Stop Garbage Collection Calls Invoked: %26%n\r\n          Stop Garbage Collection Calls Failed: %27%n%n\r\n          Full SMR Band Cluster Allocations: %28%n\r\n          Shared SMR Band Cluster Allocations: %29%n%n\r\n          Garbage Collection Read Latency Total: %30%n\r\n          Garbage Collection Read Latency Average: %31%n\r\n          Garbage Collection Read Latency Maximum: %32%n\r\n          Garbage Collection Total Read IOs: %33%n\r\n          Garbage Collection Write Latency Total: %34%n\r\n          Garbage Collection Write Latency Average: %35%n\r\n          Garbage Collection Write Latency Maximum: %36%n\r\n          Garbage Collection Total Write IOs: %37%n\r\n          Disk Full Requires Garbage Collection: %38%n%n\r\n          SMR Zone Full Events: %39%n\r\n          CMR Zone Full Events: %40%n%n\r\n          Invalid Sector Errors: %41%n\r\n          IO Device Errors: %42%n\r\n          IO Unaligned Write Errors: %43%n\r\n          Write Errors: %44%n\r\n          Read Errors: %45%n\r\n          SMR Write-Head Requeries: %46%n\r\n
0xb00100aa | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          %n\r\n          IO type: %8%n\r\n          %n\r\n          Interval duration: %6%n\r\n          %n\r\n          Max Acceptable IO Latency: %10%n\r\n          High Latency IOs: %11%n\r\n          %n\r\n          IO count: %12%n\r\n          Avg IOPS: %13%n\r\n          Avg latency: %15%n\r\n          %n\r\n          Latency buckets: [%16]%n\r\n          IO count buckets: [%17, %18, %19, %20, %21, %22, %23, %24, %25, %26, %27, %28]%n\r\n          Total time buckets (ns): [%29, %30, %31, %32, %33, %34, %35, %36, %37, %38, %39, %40]%n\r\n          %n\r\n          For more details see the details tab.%n\r\n
0xb00100c8 | Stream Snapshot Periodic Data:%n%n\r\n                        Volume GUID: %1%n\r\n                        Device Name: %3%n\r\n                        Event Group Tag: %4%n%n\r\n                        Create Operation Count: %5%n\r\n                        Create Operation Total Duration (us): %6%n\r\n                        Create Operation Maximum Duration (us): %7%n%n\r\n                        List Operation Count: %8%n\r\n                        List Operation Total Duration (us): %9%n\r\n                        List Operation Maximum Duration (us): %10%n%n\r\n                        Query Deltas Operation Count: %11%n\r\n                        Query Deltas Operation Total Duration (us): %12%n\r\n                        Query Deltas Operation Maximum Duration (us): %13%n%n\r\n                        Revert Operation Count: %14%n\r\n                        Revert Operation Total Duration (us): %15%n\r\n                        Revert Operation Maximum Duration (us): %16%n%n\r\n                        Set Shadow B-Tree Operation Count: %17%n\r\n                        Set Shadow B-Tree OperationTotal Duration (us): %18%n\r\n                        Set Shadow B-Tree Operation Maximum Duration (us): %19%n%n\r\n                        Clear Shadow B-Tree Operation Count: %20%n\r\n                        Clear Shadow B-Tree OperationTotal Duration (us): %21%n\r\n                        Clear Shadow B-Tree Operation Maximum Duration (us): %22%n%n\r\n                        Error Count: %23\r\n
0xb00100c9 | Stream Snapshot Periodic Operation Latencies (Part 1):%n%n\r\n                        Volume GUID: %1%n\r\n                        Device Name: %3%n\r\n                        Event Group Tag: %4%n%n\r\n                        LatencyBucketValues:  [%6]%n%n\r\n                        Create Operation Counts: [%7, %8, %9, %10, %11, %12, %13, %14, %15, %16, %17, %18, %19, %20, %21]%n\r\n                        Create Operation Total Duration: [%22, %23, %24, %25, %26, %27, %28, %29, %30, %31, %32, %33, %34, %35, %36]%n%n\r\n                        List Operation Counts: [%37, %38, %39, %40, %41, %42, %43, %44, %45, %46, %47, %48, %49, %50, %51]%n\r\n                        List Operation Total Duration: [%52, %53, %54, %55, %56, %57, %58, %59, %60, %61, %62, %63, %64, %65, %66]%n%n\r\n                        Revert Operation Counts: [%67, %68, %69, %70, %71, %72, %73, %74, %75, %76, %77, %78, %79, %80, %81]%n\r\n                        Revert Deltas Operation Total Duration: [%82, %83, %84, %85, %86, %87, %88, %89, %90, %91, %92, %93, %94, %95, %96]\r\n
0xb00100ca | Stream Snapshot Periodic Operation Latencies (Part 2):%n%n\r\n                        Volume GUID: %1%n\r\n                        Device Name: %3%n\r\n                        Event Group Tag: %4%n%n\r\n                        LatencyBucketValues:  [%6]%n%n\r\n                        Query Deltas Operation Counts: [%7, %8, %9, %10, %11, %12, %13, %14, %15, %16, %17, %18, %19, %20, %21]%n\r\n                        Query Deltas Operation Total Duration: [%22, %23, %24, %25, %26, %27, %28, %29, %30, %31, %32, %33, %34, %35, %36]%n%n\r\n                        Set Shadow B-Tree Operation Counts: [%37, %38, %39, %40, %41, %42, %43, %44, %45, %46, %47, %48, %49, %50, %51]%n\r\n                        Set Shadow B-Tree Operation Total Duration: [%52, %53, %54, %55, %56, %57, %58, %59, %60, %61, %62, %63, %64, %65, %66]%n%n\r\n                        Clear Shadow B-Tree Operation Counts: [%67, %68, %69, %70, %71, %72, %73, %74, %75, %76, %77, %78, %79, %80, %81]%n\r\n                        Clear Shadow B-Tree Operation Total Duration: [%82, %83, %84, %85, %86, %87, %88, %89, %90, %91, %92, %93, %94, %95, %96]\r\n
0xb0020091 | IO latency summary common data for volume:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n%n\r\n          Tier Index %5%n\r\n          Max Acceptable IO Latency: %6 ms%n\r\n          Read/Write latency buckets (ns): [%7, %8, %9, %10, %11, %12, %13]%n\r\n          Trim latency buckets (ns): [%14, %15, %16, %17, %18, %19, %20]%n\r\n          Flush latency buckets (ns): [%21, %22, %23, %24, %25, %26, %27]%n\r\n
0xb0020092 | IO latency summary:%n%n\r\n          Version: %1%n\r\n          Volume Id: %2%n\r\n          Volume name: %4%n\r\n          Tier index: %6%n%n\r\n          Max Acceptable IO Latency: %7 ms%n%n\r\n          Read/Write latency buckets (ns): [%8, %9, %10, %11, %12, %13, %14]%n\r\n          Trim latency buckets (ns): [%15, %16, %17, %18, %19, %20, %21]%n\r\n          Flush latency buckets (ns): [%22, %23, %24, %25, %26, %27, %28]%n%n\r\n          Interval duration: %30 us%n%n\r\n          Non-cached reads:%n\r\n                    IO count: %31%n\r\n                    Total bytes: %32%n\r\n                    Avg latency: %33 ns%n%n\r\n          Non-cached writes: %n\r\n                    IO count: %34%n\r\n                    Total bytes: %35%n\r\n                    Avg latency: %36 ns%n%n\r\n          File flushes: %n\r\n                    IO count: %37%n\r\n                    Avg latency: %38 ns%n%n\r\n          Directory flushes: %n\r\n                    IO count: %39%n\r\n                    Avg latency: %40 ns%n%n\r\n          Volume flushes: %n\r\n                    IO count: %41%n\r\n                    Avg latency: %42 ns%n%n\r\n          File level trims: %n\r\n                    IO count: %43%n\r\n                    Total bytes: %44%n\r\n                    Extents count: %45%n\r\n                    Avg latency: %46 ns%n%n\r\n          Volume trims: %n\r\n                    IO count: %47%n\r\n                    Total bytes: %48%n\r\n                    Extents count: %49\r\n                    Avg latency: %50 ns%n%n\r\nFor more details see the details tab.%n\r\n
0xb0020093 | An IO took more than %6 ms to complete:%n%n\r\n          Process Id: %7%n\r\n          Process name: %8%n\r\n          File name: %10%n\r\n          File offset: %16%n\r\n          IO Type: %14%n\r\n          IO Size: %15 bytes%n\r\n          %19 cluster(s) starting at cluster %18%n\r\n          Latency: %17 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5\r\n
0xb00200aa | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          %n\r\n          IO type: %8%n\r\n          %n\r\n          Interval duration: %6%n\r\n          %n\r\n          Max Acceptable IO Latency: %10%n\r\n          High Latency IOs: %11%n\r\n          %n\r\n          IO count: %12%n\r\n          Total bytes: %41%n\r\n          Avg IOPS: %13%n\r\n          Avg Bps: %42%n\r\n          Avg latency: %15%n\r\n          %n\r\n          Latency buckets: [%16]%n\r\n          IO count buckets: [%17, %18, %19, %20, %21, %22, %23, %24, %25, %26, %27, %28]%n\r\n          Total time buckets (ns): [%29, %30, %31, %32, %33, %34, %35, %36, %37, %38, %39, %40]%n\r\n          %n\r\n          For more details see the details tab.%n\r\n
0xb0030093 | An IO took more than %6 ms to complete:%n%n\r\n          Process Id: %7%n\r\n          Process name: %8%n\r\n          File name: %10%n\r\n          IO Type: %14%n\r\n          Latency: %15 ms%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          Tier index: %5\r\n
0xb00300aa | IO latency summary:%n%n\r\n          Volume Id: %1%n\r\n          Volume name: %3%n\r\n          %n\r\n          IO type: %8%n\r\n          %n\r\n          Interval duration: %6%n\r\n          %n\r\n          Max Acceptable IO Latency: %10%n\r\n          High Latency IOs: %11%n\r\n          %n\r\n          IO count: %12%n\r\n          Total bytes: %41%n\r\n          Total extents: %55%n\r\n          Avg IOPS: %13%n\r\n          Avg Bps: %42%n\r\n          Avg latency: %15%n\r\n          %n\r\n          Latency buckets: [%16]%n\r\n          IO count buckets: [%17, %18, %19, %20, %21, %22, %23, %24, %25, %26, %27, %28]%n\r\n          Total time buckets (ns): [%29, %30, %31, %32, %33, %34, %35, %36, %37, %38, %39, %40]%n\r\n          %n\r\n          For more details see the details tab.%n\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xd0000001 | Write: NonPaging, NonCached, Async\r\n
0xd0000002 | Write: NonPaging, NonCached, Sync\r\n
0xd0000003 | Write: NonPaging, NonCached, Async, Writethrough\r\n
0xd0000004 | Write: NonPaging, NonCached, Sync, Writethrough\r\n
0xd0000005 | Write: NonPaging, Cached, Async\r\n
0xd0000006 | Write: NonPaging, Cached, Sync\r\n
0xd0000007 | Write: NonPaging, Cached, Async, Writethrough\r\n
0xd0000008 | Write: NonPaging, Cached, Sync, Writethrough\r\n
0xd0000009 | Write: Paging, NonCached, Async\r\n
0xd000000a | Write: Paging, NonCached, Sync\r\n
0xd000000b | Write: Paging, NonCached, Async, Writethrough\r\n
0xd000000c | Write: Paging, NonCached, Sync, Writethrough\r\n
0xd000000d | Read: NonPaging, NonCached, Async\r\n
0xd000000e | Read: NonPaging, NonCached, Sync\r\n
0xd000000f | Read: NonPaging, Cached, Async\r\n
0xd0000010 | Read: NonPaging, Cached, Sync\r\n
0xd0000011 | Read: Paging, NonCached, Async\r\n
0xd0000012 | Read: Paging, NonCached, Sync\r\n
0xd0000013 | read\r\n
0xd0000014 | write\r\n
