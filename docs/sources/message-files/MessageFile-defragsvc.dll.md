## defragsvc.dll

Path: %SystemRoot%\system32\defragsvc.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x00000102 | The disk defragmenter successfully completed %1 on %2\r\n
0x09000100 | This file could not be defragmented because it is unmovable.\r\n
0x09000101 | This file was corrupt or unreadable and should be skipped.\r\n
0x09000103 | This element was not found in the table.\r\n
0x09000104 | No extents of the file were moved.\r\n
0x40000103 | A volume shrink analysis was initiated on volume %1. This event log entry details information about the last unmovable file that could limit the maximum number of reclaimable bytes.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000101 | The volume %1 was not defragmented because an error was encountered: %2\r\n
0x80000104 | Error: during volume shrink initiated on volume %1 we failed to move a movable file extent.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The unmovable cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %3" command.\r\n
0x80000105 | Error: a file blocked volume shrink on volume %1.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %3" command.\r\n
0x89000000 | An operation is currently in progress on this volume.\r\n
0x89000001 | The given volume path is invalid.\r\n
0x89000002 | The given volume path is invalid.\r\n
0x89000003 | Starting new operations is disabled.\r\n
0x89000004 | The engine has been shut down. Starting new operations is disabled.\r\n
0x89000005 | The operation ID is invalid.\r\n
0x89000006 | The user cancelled the operation.\r\n
0x89000007 | Please specify a volume to perform the operation on.\r\n
0x89000008 | An invalid command line option was specified.\r\n
0x89000009 | This is not a supported operation.\r\n
0x8900000a | There is no operation in progress on the specified volume.\r\n
0x8900000b | You cannot request to attach to a volume's operation and specify a new operation simulateneously.\r\n
0x8900000c | No client is registered with the server, with this client ID.\r\n
0x8900000d | This volume cannot be defragmented.\r\n
0x8900000e | Network volumes cannot be defragmented.\r\n
0x8900000f | CD-ROM volumes cannot be defragmented.\r\n
0x89000010 | The connection to the Disk Defragmenter service was lost.\r\n
0x89000011 | The disk was disconnected from the system.\r\n
0x89000012 | The disk defragmenter engine is shutting down.\r\n
0x89000013 | This program can only track the operation on one volume at a time. Please specify only one volume.\r\n
0x89000014 | This element already exists in the table. All entries in the table must be unique.\r\n
0x89000015 | The dirty bit is set on this volume.\r\n
0x89000016 | The file move failed.\r\n
0x89000017 | Some registry entries were missing from the boot optimization section of the registry.\r\n
0x89000018 | Boot optimization has been disabled in the registry.\r\n
0x89000019 | Boot optimization could not complete due to a lack of free space.\r\n
0x8900001a | Boot optimization must be run on the boot volume.\r\n
0x8900001b | Boot optimization could not run because the prefetch layout file is missing or invalid.\r\n
0x8900001c | The user requested that the UI not be launched.\r\n
0x8900001d | The disk is corrupted.\r\n
0x8900001e | The file on the disk cannot be opened.\r\n
0x8900001f | The disk being defragmented is full.\r\n
0x89000020 | This operation is not supported on this filesystem.\r\n
0x89000021 | This shrink size specified is too big.\r\n
0x89000022 | The task scheduler service is disabled.\r\n
0x89000023 | The disk defragmenter cannot continue because the file system's master file table is too fragmented.\r\n
0x89000024 | The disk defragmenter cannot start because you have insufficient priveleges to perform this operation.\r\n
0x89000025 | The operation being tracked completed and another operation was invoked.\r\n
0x89000026 | The Disk Defragmenter was not able to disable the machine from entering automatic sleep.\r\n
0x89000027 | The given volume is currently locked. A format may be in progress, or the disk checking tool is running.\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00000102 | The storage optimizer successfully completed %1 on %2\r\n
0x09000100 | This file could not be optimized because it is unmovable.\r\n
0x09000101 | This file was corrupt or unreadable and should be skipped.\r\n
0x09000103 | This element was not found in the table.\r\n
0x09000104 | No extents of the file were moved.\r\n
0x40000103 | A volume shrink analysis was initiated on volume %1. This event log entry details information about the last unmovable file that could limit the maximum number of reclaimable bytes.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000101 | The volume %1 was not optimized because an error was encountered: %2\r\n
0x80000104 | Error: during volume shrink initiated on volume %1 we failed to move a movable file extent.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The unmovable cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %3" command.\r\n
0x80000105 | Error: a file blocked volume shrink on volume %1.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %3" command.\r\n
0x89000000 | An operation is currently in progress on this volume.\r\n
0x89000001 | The given volume path is invalid.\r\n
0x89000002 | The given volume path is invalid.\r\n
0x89000003 | Starting new operations is disabled.\r\n
0x89000004 | The engine has been shut down. Starting new operations is disabled.\r\n
0x89000005 | The operation ID is invalid.\r\n
0x89000006 | The user cancelled the operation.\r\n
0x89000007 | Please specify a volume to perform the operation on.\r\n
0x89000008 | An invalid command line option was specified.\r\n
0x89000009 | This is not a supported operation.\r\n
0x8900000a | There is no operation in progress on the specified volume.\r\n
0x8900000b | You cannot request to attach to a volume's operation and specify a new operation simulateneously.\r\n
0x8900000c | No client is registered with the server, with this client ID.\r\n
0x8900000d | This volume cannot be optimized.\r\n
0x8900000e | Network volumes cannot be optimized.\r\n
0x8900000f | CD-ROM volumes cannot be optimized.\r\n
0x89000010 | The connection to the Optimize Drives service was lost.\r\n
0x89000011 | The disk was disconnected from the system.\r\n
0x89000012 | The storage optimizer engine is shutting down.\r\n
0x89000013 | This program can only track the operation on one volume at a time. Please specify only one volume.\r\n
0x89000014 | This element already exists in the table. All entries in the table must be unique.\r\n
0x89000015 | The dirty bit is set on this volume.\r\n
0x89000016 | The file move failed.\r\n
0x89000017 | Some registry entries were missing from the boot optimization section of the registry.\r\n
0x89000018 | Boot optimization has been disabled in the registry.\r\n
0x89000019 | Boot optimization could not complete due to a lack of free space.\r\n
0x8900001a | Boot optimization must be run on the boot volume.\r\n
0x8900001b | Boot optimization could not run because the prefetch layout file is missing or invalid.\r\n
0x8900001c | The user requested that the UI not be launched.\r\n
0x8900001d | The disk is corrupted.\r\n
0x8900001e | The file on the disk cannot be opened.\r\n
0x8900001f | The disk being optimized is full.\r\n
0x89000020 | This operation is not supported on this filesystem.\r\n
0x89000021 | This shrink size specified is too big.\r\n
0x89000022 | The task scheduler service is disabled.\r\n
0x89000023 | The storage optimizer cannot continue because the file system's master file table is too fragmented.\r\n
0x89000024 | The storage optimizer cannot start because you have insufficient priveleges to perform this operation.\r\n
0x89000025 | The operation being tracked completed and another operation was invoked.\r\n
0x89000026 | The Storage Optimizer was not able to disable the machine from entering automatic sleep.\r\n
0x89000027 | The given volume is currently locked. A format may be in progress, or the disk checking tool is running.\r\n
0x89000028 | The slab consolidation operation was aborted because an insufficient number of slabs could be reclaimed (based on the limits specified in the registry).\r\n
0x89000029 | The slab consolidation / trim operation cannot be performed because the volume alignment is invalid.\r\n
0x8900002a | The operation requested is not supported by the hardware backing the volume.\r\n
0x8900002b | The operation aborted because the storage slab size changed while performing the operation.\r\n
0x8900002c | The boot optimization operation was not run because it is not supported on this volume.\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00000102 | The storage optimizer successfully completed %1 on %2\r\n
0x09000100 | This file could not be optimized because it is unmovable.\r\n
0x09000101 | This file was corrupt or unreadable and should be skipped.\r\n
0x09000103 | This element was not found in the table.\r\n
0x09000104 | No extents of the file were moved.\r\n
0x40000103 | A volume shrink analysis was initiated on volume %1. This event log entry details information about the last unmovable file that could limit the maximum number of reclaimable bytes.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000101 | The volume %1 was not optimized because an error was encountered: %2\r\n
0x80000104 | Error: during volume shrink initiated on volume %1 we failed to move a movable file extent.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The unmovable cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000105 | Error: a file blocked volume shrink on volume %1.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x89000000 | An operation is currently in progress on this volume.\r\n
0x89000001 | The given volume path is invalid.\r\n
0x89000002 | The given volume path is invalid.\r\n
0x89000003 | Starting new operations is disabled.\r\n
0x89000004 | The engine has been shut down. Starting new operations is disabled.\r\n
0x89000005 | The operation ID is invalid.\r\n
0x89000006 | The user cancelled the operation.\r\n
0x89000007 | Please specify a volume to perform the operation on.\r\n
0x89000008 | An invalid command line option was specified.\r\n
0x89000009 | This is not a supported operation.\r\n
0x8900000a | There is no operation in progress on the specified volume.\r\n
0x8900000b | You cannot request to attach to a volume's operation and specify a new operation simulateneously.\r\n
0x8900000c | No client is registered with the server, with this client ID.\r\n
0x8900000d | This volume cannot be optimized.\r\n
0x8900000e | Network volumes cannot be optimized.\r\n
0x8900000f | CD-ROM volumes cannot be optimized.\r\n
0x89000010 | The connection to the Optimize Drives service was lost.\r\n
0x89000011 | The disk was disconnected from the system.\r\n
0x89000012 | The storage optimizer engine is shutting down.\r\n
0x89000013 | This program can only track the operation on one volume at a time. Please specify only one volume.\r\n
0x89000014 | This element already exists in the table. All entries in the table must be unique.\r\n
0x89000015 | The dirty bit is set on this volume.\r\n
0x89000016 | The file move failed.\r\n
0x89000017 | Some registry entries were missing from the boot optimization section of the registry.\r\n
0x89000018 | Boot optimization has been disabled in the registry.\r\n
0x89000019 | Boot optimization could not complete due to a lack of free space.\r\n
0x8900001a | Boot optimization must be run on the boot volume.\r\n
0x8900001b | Boot optimization could not run because the prefetch layout file is missing or invalid.\r\n
0x8900001c | The user requested that the UI not be launched.\r\n
0x8900001d | The disk is corrupted.\r\n
0x8900001e | The file on the disk cannot be opened.\r\n
0x8900001f | The disk being optimized is full.\r\n
0x89000020 | This operation is not supported on this filesystem.\r\n
0x89000021 | This shrink size specified is too big.\r\n
0x89000022 | The task scheduler service is disabled.\r\n
0x89000023 | The storage optimizer cannot continue because the file system's master file table is too fragmented.\r\n
0x89000024 | The storage optimizer cannot start because you have insufficient priveleges to perform this operation.\r\n
0x89000025 | The operation being tracked completed and another operation was invoked.\r\n
0x89000026 | The Storage Optimizer was not able to disable the machine from entering automatic sleep.\r\n
0x89000027 | The given volume is currently locked. A format may be in progress, or the disk checking tool is running.\r\n
0x89000028 | The slab consolidation operation was aborted because an insufficient number of slabs could be reclaimed (based on the limits specified in the registry).\r\n
0x89000029 | The slab consolidation / trim operation cannot be performed because the volume alignment is invalid.\r\n
0x8900002a | The operation requested is not supported by the hardware backing the volume.\r\n
0x8900002b | The operation aborted because the storage slab size changed while performing the operation.\r\n
0x8900002c | The boot optimization operation was not run because it is not supported on this volume.\r\n

### 6.3.9600.17238, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x00000102 | The storage optimizer successfully completed %1 on %2\r\n
0x09000100 | This file could not be optimized because it is unmovable.\r\n
0x09000101 | This file was corrupt or unreadable and should be skipped.\r\n
0x09000103 | This element was not found in the table.\r\n
0x09000104 | No extents of the file were moved.\r\n
0x40000103 | A volume shrink analysis was initiated on volume %1. This event log entry details information about the last unmovable file that could limit the maximum number of reclaimable bytes.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000101 | The volume %1 was not optimized because an error was encountered: %2\r\n
0x80000104 | Error: during volume shrink initiated on volume %1 we failed to move a movable file extent.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The unmovable cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000105 | Error: a file blocked volume shrink on volume %1.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x89000000 | An operation is currently in progress on this volume.\r\n
0x89000001 | The given volume path is invalid.\r\n
0x89000002 | The given volume path is invalid.\r\n
0x89000003 | Starting new operations is disabled.\r\n
0x89000004 | The engine has been shut down. Starting new operations is disabled.\r\n
0x89000005 | The operation ID is invalid.\r\n
0x89000006 | The user cancelled the operation.\r\n
0x89000007 | Please specify a volume to perform the operation on.\r\n
0x89000008 | An invalid command line option was specified.\r\n
0x89000009 | This is not a supported operation.\r\n
0x8900000a | There is no operation in progress on the specified volume.\r\n
0x8900000b | You cannot request to attach to a volume's operation and specify a new operation simulateneously.\r\n
0x8900000c | No client is registered with the server, with this client ID.\r\n
0x8900000d | This volume cannot be optimized.\r\n
0x8900000e | Network volumes cannot be optimized.\r\n
0x8900000f | CD-ROM volumes cannot be optimized.\r\n
0x89000010 | The connection to the Optimize Drives service was lost.\r\n
0x89000011 | The disk was disconnected from the system.\r\n
0x89000012 | The storage optimizer engine is shutting down.\r\n
0x89000013 | This program can only track the operation on one volume at a time. Please specify only one volume.\r\n
0x89000014 | This element already exists in the table. All entries in the table must be unique.\r\n
0x89000015 | The dirty bit is set on this volume.\r\n
0x89000016 | The file move failed.\r\n
0x89000017 | Some registry entries were missing from the boot optimization section of the registry.\r\n
0x89000018 | Boot optimization has been disabled in the registry.\r\n
0x89000019 | Boot optimization could not complete due to a lack of free space.\r\n
0x8900001a | Boot optimization must be run on the boot volume.\r\n
0x8900001b | Boot optimization could not run because the prefetch layout file is missing or invalid.\r\n
0x8900001c | The user requested that the UI not be launched.\r\n
0x8900001d | The disk is corrupted.\r\n
0x8900001e | The file on the disk cannot be opened.\r\n
0x8900001f | The disk being optimized is full.\r\n
0x89000020 | This operation is not supported on this filesystem.\r\n
0x89000021 | This shrink size specified is too big.\r\n
0x89000022 | The task scheduler service is disabled.\r\n
0x89000023 | The storage optimizer cannot continue because the file system's master file table is too fragmented.\r\n
0x89000024 | The storage optimizer cannot start because you have insufficient priveleges to perform this operation.\r\n
0x89000025 | The operation being tracked completed and another operation was invoked.\r\n
0x89000026 | The Storage Optimizer was not able to disable the machine from entering automatic sleep.\r\n
0x89000027 | The given volume is currently locked. A format may be in progress, or the disk checking tool is running.\r\n
0x89000028 | The slab consolidation operation was aborted because an insufficient number of slabs could be reclaimed (based on the limits specified in the registry).\r\n
0x89000029 | The slab consolidation / trim operation cannot be performed because the volume alignment is invalid.\r\n
0x8900002a | The operation requested is not supported by the hardware backing the volume.\r\n
0x8900002b | The operation aborted because the storage slab size changed while performing the operation.\r\n
0x8900002c | The boot optimization operation was not run because it is not supported on this volume.\r\n
0x8900002d | Neither Slab Consolidation nor Slab Analysis will run if slabs are less than 8 MB.\r\n

### 10.0.17134.1, 10.0.17763.1

Message identifier | Message string
--- | ---
0x00000102 | The storage optimizer successfully completed %1 on %2\r\n
0x09000100 | This file could not be optimized because it is unmovable.\r\n
0x09000101 | This file was corrupt or unreadable and should be skipped.\r\n
0x09000103 | This element was not found in the table.\r\n
0x09000104 | No extents of the file were moved.\r\n
0x40000103 | A volume shrink analysis was initiated on volume %1. This event log entry details information about the last unmovable file that could limit the maximum number of reclaimable bytes.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x40000106 | The storage optimizer skipped %1 on %2 because: %3\r\n
0x40000107 | Cluster shared volume %2 is not in redirected mode, %1 might not optimize all files.\r\n
0x80000101 | The volume %1 was not optimized because an error was encountered: %2\r\n
0x80000104 | Error: during volume shrink initiated on volume %1 we failed to move a movable file extent.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The unmovable cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000105 | Error: a file blocked volume shrink on volume %1.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x89000000 | An operation is currently in progress on this volume.\r\n
0x89000001 | The given volume path is invalid.\r\n
0x89000002 | The given volume path is invalid.\r\n
0x89000003 | Starting new operations is disabled.\r\n
0x89000004 | The engine has been shut down. Starting new operations is disabled.\r\n
0x89000005 | The operation ID is invalid.\r\n
0x89000006 | The user cancelled the operation.\r\n
0x89000007 | Please specify a volume to perform the operation on.\r\n
0x89000008 | An invalid command line option was specified.\r\n
0x89000009 | This is not a supported operation.\r\n
0x8900000a | There is no operation in progress on the specified volume.\r\n
0x8900000b | You cannot request to attach to a volume's operation and specify a new operation simulateneously.\r\n
0x8900000c | No client is registered with the server, with this client ID.\r\n
0x8900000d | This volume cannot be optimized.\r\n
0x8900000e | Network volumes cannot be optimized.\r\n
0x8900000f | CD-ROM volumes cannot be optimized.\r\n
0x89000010 | The connection to the Optimize Drives service was lost.\r\n
0x89000011 | The disk was disconnected from the system.\r\n
0x89000012 | The storage optimizer engine is shutting down.\r\n
0x89000013 | This program can only track the operation on one volume at a time. Please specify only one volume.\r\n
0x89000014 | This element already exists in the table. All entries in the table must be unique.\r\n
0x89000015 | The dirty bit is set on this volume.\r\n
0x89000016 | The file move failed.\r\n
0x89000017 | Some registry entries were missing from the boot optimization section of the registry.\r\n
0x89000018 | Boot optimization has been disabled in the registry.\r\n
0x89000019 | Boot optimization could not complete due to a lack of free space.\r\n
0x8900001a | Boot optimization must be run on the boot volume.\r\n
0x8900001b | Boot optimization could not run because the prefetch layout file is missing or invalid.\r\n
0x8900001c | The user requested that the UI not be launched.\r\n
0x8900001d | The disk is corrupted.\r\n
0x8900001e | The file on the disk cannot be opened.\r\n
0x8900001f | The disk being optimized is full.\r\n
0x89000020 | This operation is not supported on this filesystem.\r\n
0x89000021 | This shrink size specified is too big.\r\n
0x89000022 | The task scheduler service is disabled.\r\n
0x89000023 | The storage optimizer cannot continue because the file system's master file table is too fragmented.\r\n
0x89000024 | The storage optimizer cannot start because you have insufficient priveleges to perform this operation.\r\n
0x89000025 | The operation being tracked completed and another operation was invoked.\r\n
0x89000026 | The Storage Optimizer was not able to disable the machine from entering automatic sleep.\r\n
0x89000027 | The given volume is currently locked. A format may be in progress, or the disk checking tool is running.\r\n
0x89000028 | The slab consolidation operation was aborted because an insufficient number of slabs could be reclaimed (based on the limits specified in the registry).\r\n
0x89000029 | The slab consolidation / trim operation cannot be performed because the volume alignment is invalid.\r\n
0x8900002a | The operation requested is not supported by the hardware backing the volume.\r\n
0x8900002b | The operation aborted because the storage slab size changed while performing the operation.\r\n
0x8900002c | The boot optimization operation was not run because it is not supported on this volume.\r\n
0x8900002d | Neither Slab Consolidation nor Slab Analysis will run if slabs are less than 8 MB.\r\n

### 10.0.18362.1

Message identifier | Message string
--- | ---
0x00000102 | The storage optimizer successfully completed %1 on %2\r\n
0x09000100 | This file could not be optimized because it is unmovable.\r\n
0x09000101 | This file was corrupt or unreadable and should be skipped.\r\n
0x09000103 | This element was not found in the table.\r\n
0x09000104 | No extents of the file were moved.\r\n
0x40000103 | A volume shrink analysis was initiated on volume %1. This event log entry details information about the last unmovable file that could limit the maximum number of reclaimable bytes.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x40000106 | The storage optimizer skipped %1 on %2 because: %3\r\n
0x40000107 | Cluster shared volume %2 is not in redirected mode, %1 might not optimize all files.\r\n
0x80000101 | The volume %1 was not optimized because an error was encountered: %2\r\n
0x80000104 | Error: during volume shrink initiated on volume %1 we failed to move a movable file extent.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The unmovable cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000105 | Error: a file blocked volume shrink on volume %1.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x89000000 | An operation is currently in progress on this volume.\r\n
0x89000001 | The given volume path is invalid.\r\n
0x89000002 | The given volume path is invalid.\r\n
0x89000003 | Starting new operations is disabled.\r\n
0x89000004 | The engine has been shut down. Starting new operations is disabled.\r\n
0x89000005 | The operation ID is invalid.\r\n
0x89000006 | The user cancelled the operation.\r\n
0x89000007 | Please specify a volume to perform the operation on.\r\n
0x89000008 | An invalid command line option was specified.\r\n
0x89000009 | This is not a supported operation.\r\n
0x8900000a | There is no operation in progress on the specified volume.\r\n
0x8900000b | You cannot request to attach to a volume's operation and specify a new operation simulateneously.\r\n
0x8900000c | No client is registered with the server, with this client ID.\r\n
0x8900000d | This volume cannot be optimized.\r\n
0x8900000e | Network volumes cannot be optimized.\r\n
0x8900000f | CD-ROM volumes cannot be optimized.\r\n
0x89000010 | The connection to the Optimize Drives service was lost.\r\n
0x89000011 | The disk was disconnected from the system.\r\n
0x89000012 | The storage optimizer engine is shutting down.\r\n
0x89000013 | This program can only track the operation on one volume at a time. Please specify only one volume.\r\n
0x89000014 | This element already exists in the table. All entries in the table must be unique.\r\n
0x89000015 | The dirty bit is set on this volume.\r\n
0x89000016 | The file move failed.\r\n
0x89000017 | Some registry entries were missing from the boot optimization section of the registry.\r\n
0x89000018 | Boot optimization has been disabled in the registry.\r\n
0x89000019 | Boot optimization could not complete due to a lack of free space.\r\n
0x8900001a | Boot optimization must be run on the boot volume.\r\n
0x8900001b | Boot optimization could not run because the prefetch layout file is missing or invalid.\r\n
0x8900001c | The user requested that the UI not be launched.\r\n
0x8900001d | The disk is corrupted.\r\n
0x8900001e | The file on the disk cannot be opened.\r\n
0x8900001f | The disk being optimized is full.\r\n
0x89000020 | This operation is not supported on this filesystem.\r\n
0x89000021 | This shrink size specified is too big.\r\n
0x89000022 | The task scheduler service is disabled.\r\n
0x89000023 | The storage optimizer cannot continue because the file system's master file table is too fragmented.\r\n
0x89000024 | The storage optimizer cannot start because you have insufficient privileges to perform this operation.\r\n
0x89000025 | The operation being tracked completed and another operation was invoked.\r\n
0x89000026 | The Storage Optimizer was not able to disable the machine from entering automatic sleep.\r\n
0x89000027 | The given volume is currently locked. A format may be in progress, or the disk checking tool is running.\r\n
0x89000028 | The slab consolidation operation was aborted because an insufficient number of slabs could be reclaimed (based on the limits specified in the registry).\r\n
0x89000029 | The slab consolidation / trim operation cannot be performed because the volume alignment is invalid.\r\n
0x8900002a | The operation requested is not supported by the hardware backing the volume.\r\n
0x8900002b | The operation aborted because the storage slab size changed while performing the operation.\r\n
0x8900002c | The boot optimization operation was not run because it is not supported on this volume.\r\n
0x8900002d | Neither Slab Consolidation nor Slab Analysis will run if slabs are less than 8 MB.\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000102 | The storage optimizer successfully completed %1 on %2\r\n
0x09000100 | This file could not be optimized because it is unmovable.\r\n
0x09000101 | This file was corrupt or unreadable and should be skipped.\r\n
0x09000103 | This element was not found in the table.\r\n
0x09000104 | No extents of the file were moved.\r\n
0x40000103 | A volume shrink analysis was initiated on volume %1. This event log entry details information about the last unmovable file that could limit the maximum number of reclaimable bytes.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x40000106 | The storage optimizer skipped %1 on %2 because: %3\r\n
0x40000107 | Cluster shared volume %2 is not in redirected mode, %1 might not optimize all files.\r\n
0x80000101 | The volume %1 was not optimized because an error was encountered: %2\r\n
0x80000104 | Error: during volume shrink initiated on volume %1 we failed to move a movable file extent.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The unmovable cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000105 | Error: a file blocked volume shrink on volume %1.%n\r\n%n\r\nDiagnostic details:%n\r\n- The last unmovable file appears to be: %3%n\r\n- The last cluster of the file is: %4%n\r\n- Shrink potential target (LCN address): %5%n\r\n- The NTFS file flags are: %6%n\r\n- Shrink phase: %7%n\r\n%n\r\nTo find more details about this file please use the "fsutil volume querycluster %2 %4" command.\r\n
0x80000108 | The storage optimizer couldn't complete %1 on %2 because: %3\r\n
0x89000000 | An operation is currently in progress on this volume.\r\n
0x89000001 | The given volume path is invalid.\r\n
0x89000002 | The given volume path is invalid.\r\n
0x89000003 | Starting new operations is disabled.\r\n
0x89000004 | The engine has been shut down. Starting new operations is disabled.\r\n
0x89000005 | The operation ID is invalid.\r\n
0x89000006 | The user cancelled the operation.\r\n
0x89000007 | Please specify a volume to perform the operation on.\r\n
0x89000008 | An invalid command line option was specified.\r\n
0x89000009 | This is not a supported operation.\r\n
0x8900000a | There is no operation in progress on the specified volume.\r\n
0x8900000b | You cannot request to attach to a volume's operation and specify a new operation simulateneously.\r\n
0x8900000c | No client is registered with the server, with this client ID.\r\n
0x8900000d | This volume cannot be optimized.\r\n
0x8900000e | Network volumes cannot be optimized.\r\n
0x8900000f | CD-ROM volumes cannot be optimized.\r\n
0x89000010 | The connection to the Optimize Drives service was lost.\r\n
0x89000011 | The disk was disconnected from the system.\r\n
0x89000012 | The storage optimizer engine is shutting down.\r\n
0x89000013 | This program can only track the operation on one volume at a time. Please specify only one volume.\r\n
0x89000014 | This element already exists in the table. All entries in the table must be unique.\r\n
0x89000015 | The dirty bit is set on this volume.\r\n
0x89000016 | The file move failed.\r\n
0x89000017 | Some registry entries were missing from the boot optimization section of the registry.\r\n
0x89000018 | Boot optimization has been disabled in the registry.\r\n
0x89000019 | Boot optimization could not complete due to a lack of free space.\r\n
0x8900001a | Boot optimization must be run on the boot volume.\r\n
0x8900001b | Boot optimization could not run because the prefetch layout file is missing or invalid.\r\n
0x8900001c | The user requested that the UI not be launched.\r\n
0x8900001d | The disk is corrupted.\r\n
0x8900001e | The file on the disk cannot be opened.\r\n
0x8900001f | The disk being optimized is full.\r\n
0x89000020 | This operation is not supported on this filesystem.\r\n
0x89000021 | This shrink size specified is too big.\r\n
0x89000022 | The task scheduler service is disabled.\r\n
0x89000023 | The storage optimizer cannot continue because the file system's master file table is too fragmented.\r\n
0x89000024 | The storage optimizer cannot start because you have insufficient privileges to perform this operation.\r\n
0x89000025 | The operation being tracked completed and another operation was invoked.\r\n
0x89000026 | The Storage Optimizer was not able to disable the machine from entering automatic sleep.\r\n
0x89000027 | The given volume is currently locked. A format may be in progress, or the disk checking tool is running.\r\n
0x89000028 | The slab consolidation operation was aborted because an insufficient number of slabs could be reclaimed (based on the limits specified in the registry).\r\n
0x89000029 | The slab consolidation / trim operation cannot be performed because the volume alignment is invalid.\r\n
0x8900002a | The operation requested is not supported by the hardware backing the volume.\r\n
0x8900002b | The operation aborted because the storage slab size changed while performing the operation.\r\n
0x8900002c | The boot optimization operation was not run because it is not supported on this volume.\r\n
0x8900002d | Slab size is too small.\r\n
