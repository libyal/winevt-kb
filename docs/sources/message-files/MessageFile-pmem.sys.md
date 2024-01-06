## pmem.sys

Path: %SystemRoot%\system32\drivers\pmem.sys

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x0000012c | NVDIMM %1 is now in read-only mode.  Use the Get-PhysicalDisk command to get the device’s health status.  The Microsoft-Windows-PmemDisk/Operational event log may also contain more information.\r\n
0x0000012d | NVDIMM %1 is no longer in read-only mode.\r\n
0x0000012e | Windows does not support this configuration: two or more NVDIMMs on this system are part of an interleaved set. Back up the data on the interleaved set to a different drive and then break up the interleaved set. Consider using Storage Spaces if NVDIMM capacity needs to be aggregated.\r\n
0x10000002 | Hardware events\r\n
0x10000021 | Read request\r\n
0x10000022 | Write request\r\n
0x10000023 | Paging Read request\r\n
0x10000024 | Paging Write request\r\n
0x10000025 | Non-Read/Write request\r\n
0x10000026 | Device I/O control request\r\n
0x10000027 | PnP request\r\n
0x10000028 | IO Performance measurement\r\n
0x30000000 | Info\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000001 | Reported memory resource.\r\n
0xb0000002 | Memory operation duration, in hundreds of nanoseconds.\r\n
0xb0000003 | Request servicing time taken by lower driver stack(s).\r\n
0xb0000065 | Dispatching a read request.\r\n
0xb0000066 | Dispatching a write request.\r\n
0xb0000069 | Completing an IO (read/write) request.\r\n
0xb000006a | Dispatching an IOCTL.\r\n
0xb000006b | Completing a non-read/write request.\r\n
0xb000006c | Dispatching a PnP request.\r\n
0xb000006d | Completing a PnP request.\r\n
0xb00000c9 | Critical metadata on NVDIMM %1 has been corrupted. Windows needs this metadata to start the NVDIMM correctly, so we had to reinitialize it. The data on that NVDIMM may have been lost.\r\n                   %n\r\n                   %nConsider replacing the NVDIMM.\r\n                   %n\r\n                   %nThis NVDIMM may be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000ca | NVDIMM %1 failed to start. %6\r\n                   %n\r\n                   %nThis NVDIMM may be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000cb | NVDIMM %1 started successfully.\r\n
0xb00000cc | One of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media (see the Details tab for more information). Some of your data may have been lost. As a precaution, this persistent memory disk is now in read-only mode. If you want to keep using it, run the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000cd | During a previous boot session, one of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media. Some of your data may have been lost then. As a precaution, Windows made this persistent memory disk temporarily read-only. If you want to keep using this persistent memory disk, use the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000ce | NVDIMM %5 notified the persistent memory disk driver of a change in its health state. The NVDIMM now has the following health status: %7.\r\n            %n\r\n            %nThis NVDIMM is part of interleave set %1.\r\n
0xb00000cf | One of the NVDIMMs that make up the persistent memory disk %1 encountered a serious problem and the disk is now in read-only mode. Data that was saved to this disk may be lost when the computer shuts down or restarts. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nUse the Get-PhysicalDisk command to get more information about the disk's health status.\r\n
0xb00000d0 | The driver could not confirm that the NVDIMM %1 is healthy. To protect your data, the NVDIMM is now in read-only mode. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nThis NVDIMM may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nManufacturer: %2\r\n                   %nModel Number: %3\r\n                   %nSerial Number: %4\r\n
0xb00000d1 | The computer didn't assign any memory resources to NVDIMM %1. You won't be able to access the data on the device, but you can still query its health status by using the Get-PhysicalDisk command.\r\n                   %n\r\n                   %nThis NVDIMM may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nManufacturer: %2\r\n                   %nModel Number: %3\r\n                   %nSerial Number: %4\r\n
0xb00000d2 | Some physical memory locations on NVDIMM %1 are corrupt. In order to protect your computer, Windows will not access those locations and you may see failures trying to read or write to your data. Contact your hardware vendor to learn what recovery steps are available.\r\n            %n\r\n            %nThis NVDIMM may need to be replaced. It can be located using the following information:\r\n            %n\r\n            %nManufacturer: %2\r\n            %nModel Number: %3\r\n            %nSerial Number: %4\r\n
0xb00000d3 | The problem with the persistent memory disk %1 was resolved and it is now back in read-write mode.\r\n
0xb00000d4 | One of the NVDIMMs that make up the persistent memory disk %1 is in a degraded health state and may soon encounter serious problems. Consider backing up your data to another disk. Use the Get-PhysicalDisk command to see more information.\r\n
0xb00000d5 | NVDIMM %1 has encountered %5 uncorrectable memory error(s). Uncorrectable memory errors can cause system instability and data loss. Consider replacing this NVDIMM.\r\n            %n\r\n            %nThis NVDIMM can be located using the following information:\r\n            %n\r\n            %nManufacturer: %2\r\n            %nModel Number: %3\r\n            %nSerial Number: %4\r\n
0xb0000384 | NVDIMM %1 logged:\r\n            %n\r\n            %n %2\r\n
0xd0000001 | The driver encountered an internal error.\r\n
0xd0000002 | The driver could not interpret the device's memory resources.\r\n
0xd0000003 | The driver could not discover the device's interleaving settings.\r\n
0xd0000004 | The driver could not read the device's serial number.\r\n
0xd0000005 | The driver could not discover whether boot-time operations, like save and restore, succeeded.\r\n
0xd0000006 | The driver could not register to be notified of health-related events on the NVDIMM.\r\n
0xd0000007 | The driver could not confirm that the NVDIMM is healthy.\r\n
0xd0000008 | unknown\r\n
0xd0000009 | unhealthy\r\n
0xd000000a | warning\r\n
0xd000000b | healthy\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x0000012c | Persistent memory disk %1 is now in read-only mode.  Use the Get-PhysicalDisk command to get the device’s health status.  The Microsoft-Windows-PersistentMemory-PmemDisk/Operational event log may also contain more information.\r\n
0x0000012d | Persistent memory disk %1 is no longer in read-only mode.\r\n
0x0000012e | Windows does not support this configuration: two or more NVDIMMs on this system are part of an interleaved set. Back up the data on the interleaved set to a different drive and then break up the interleaved set. Consider using Storage Spaces if NVDIMM capacity needs to be aggregated.\r\n
0x10000002 | Hardware events\r\n
0x10000021 | Read request\r\n
0x10000022 | Write request\r\n
0x10000023 | Paging Read request\r\n
0x10000024 | Paging Write request\r\n
0x10000025 | Non-Read/Write request\r\n
0x10000026 | Device I/O control request\r\n
0x10000027 | PnP request\r\n
0x10000028 | IO Performance measurement\r\n
0x30000000 | Info\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000001 | Reported memory resource.\r\n
0xb0000002 | Memory operation duration, in hundreds of nanoseconds.\r\n
0xb0000003 | Request servicing time taken by lower driver stack(s).\r\n
0xb0000065 | Dispatching a read request.\r\n
0xb0000066 | Dispatching a write request.\r\n
0xb0000069 | Completing an IO (read/write) request.\r\n
0xb000006a | Dispatching an IOCTL.\r\n
0xb000006b | Completing a non-read/write request.\r\n
0xb000006c | Dispatching a PnP request.\r\n
0xb000006d | Completing a PnP request.\r\n
0xb00000ca | Persistent memory disk %1 failed to start.\r\n                   %nReason: %5\r\n                   %nNTSTATUS code: %6\r\n
0xb00000cb | Persistent memory disk %1 started successfully.\r\n
0xb00000cc | One of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media (see the Details tab for more information). Some of your data may have been lost. As a precaution, this persistent memory disk is now in read-only mode. If you want to keep using it, run the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000cd | During a previous boot session, one of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media. Some of your data may have been lost then. As a precaution, Windows made this persistent memory disk temporarily read-only. If you want to keep using this persistent memory disk, use the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000ce | NVDIMM %5 notified persistent memory disk %1 of a change in its health state. The NVDIMM now has the following health status: %7.\r\n
0xb00000cf | One of the NVDIMMs that make up the persistent memory disk %1 encountered a serious problem and the disk is now in read-only mode. Data that was saved to this disk may be lost when the computer shuts down or restarts. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nUse the Get-PhysicalDisk command to get more information about the disk's health status.\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000d1 | The computer didn't assign any memory resources to persistent memory disk %1. You won't be able to access the data on the device, but you can still query its health status by using the Get-PhysicalDisk command.\r\n
0xb00000d3 | The problem with the persistent memory disk %1 was resolved and it is now back in read-write mode.\r\n
0xb00000d4 | One of the NVDIMMs that make up the persistent memory disk %1 is in a degraded health state and may soon encounter serious problems. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb0000384 | Persistent memory disk %1 logged:\r\n            %n\r\n            %n %2\r\n
0xb00200d2 | Some physical memory locations on persistent memory disk %1 are corrupt. In order to protect your computer, Windows will not access those locations and you may see failures trying to read or write to your data. Contact your hardware vendor to learn what recovery steps are available.\r\n
0xd0000001 | The driver encountered an internal error.\r\n
0xd0000002 | The driver could not interpret the device's memory resources.\r\n
0xd0000003 | The driver could not discover the device's interleaving settings.\r\n
0xd0000004 | The driver could not read the device's serial number.\r\n
0xd0000005 | The driver could not discover whether boot-time operations, like save and restore, succeeded.\r\n
0xd0000006 | The driver could not register to be notified of health-related events on the NVDIMM.\r\n
0xd0000007 | The driver could not determine the health status of the persistent memory disk.\r\n
0xd0000008 | There is an uncorrectable memory error in a critical region of the persistent memory disk.\r\n
0xd0000009 | unknown\r\n
0xd000000a | unhealthy\r\n
0xd000000b | warning\r\n
0xd000000c | healthy\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x0000012c | Persistent memory disk %1 is now in read-only mode.  Use the Get-PhysicalDisk command to get the device’s health status.  The Microsoft-Windows-PersistentMemory-PmemDisk/Operational event log may also contain more information.\r\n
0x0000012d | Persistent memory disk %1 is no longer in read-only mode.\r\n
0x0000012e | Windows does not support this configuration: two or more NVDIMMs on this system are part of an interleaved set. Back up the data on the interleaved set to a different drive and then break up the interleaved set. Consider using Storage Spaces if NVDIMM capacity needs to be aggregated.\r\n
0x10000002 | Hardware events\r\n
0x10000021 | Read request\r\n
0x10000022 | Write request\r\n
0x10000023 | Paging Read request\r\n
0x10000024 | Paging Write request\r\n
0x10000025 | Non-Read/Write request\r\n
0x10000026 | Device I/O control request\r\n
0x10000027 | PnP request\r\n
0x10000028 | IO Performance measurement\r\n
0x30000000 | Info\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000001 | Reported memory resource.\r\n
0xb0000002 | Memory operation duration, in hundreds of nanoseconds.\r\n
0xb0000003 | Request servicing time taken by lower driver stack(s).\r\n
0xb0000065 | Dispatching a read request.\r\n
0xb0000066 | Dispatching a write request.\r\n
0xb0000069 | Completing an IO (read/write) request.\r\n
0xb000006a | Dispatching an IOCTL.\r\n
0xb000006b | Completing a non-read/write request.\r\n
0xb000006c | Dispatching a PnP request.\r\n
0xb000006d | Completing a PnP request.\r\n
0xb00000ca | Persistent memory disk %1 failed to start.\r\n                   %nReason: %5\r\n                   %nNTSTATUS code: %6\r\n
0xb00000cb | Persistent memory disk %1 started successfully.\r\n
0xb00000cc | One of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media (see the Details tab for more information). Some of your data may have been lost. As a precaution, this persistent memory disk is now in read-only mode. If you want to keep using it, run the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000cd | During a previous boot session, one of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media. Some of your data may have been lost then. As a precaution, Windows made this persistent memory disk temporarily read-only. If you want to keep using this persistent memory disk, use the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000ce | NVDIMM %5 notified persistent memory disk %1 of a change in its health state. The NVDIMM now has the following health status: %7.\r\n
0xb00000cf | One of the NVDIMMs that make up the persistent memory disk %1 encountered a serious problem and the disk is now in read-only mode. Data that was saved to this disk may be lost when the computer shuts down or restarts. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nUse the Get-PhysicalDisk command to get more information about the disk's health status.\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000d1 | The computer didn't assign any memory resources to persistent memory disk %1. You won't be able to access the data on the device, but you can still query its health status by using the Get-PhysicalDisk command.\r\n
0xb00000d3 | The problem with the persistent memory disk %1 was resolved and it is now back in read-write mode.\r\n
0xb00000d4 | One of the NVDIMMs that make up the persistent memory disk %1 is in a degraded health state and may soon encounter serious problems. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000d5 | The physical devices that make up persistent memory disk %1 have an atomicity setting that is incompatible with the data on the disk. Windows didn't start the disk to prevent data loss.\r\n            %n\r\n            %nThis type of problem can happen when you update your computer's firmware, or when you upgrade from a version of Windows that doesn't look at atomicity settings to one that does.\r\n            %n\r\n            %nTo recover the disk, follow these steps:\r\n            %n1. Open the registry editor (regedit) and navigate to 'Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\ACPI\ACPI0012\<instance ID>\Device Parameters'. There will only be one instance ID key.\r\n            %n2. Create a registry key named 'ScmBus'. Inside it, create a new DWORD value named 'IgnoreLabels' and set it to 1.\r\n            %n3. Restart your computer.\r\n            %n4. When Windows starts again, your persistent memory disks will be accessible. Back up **all the data** on **all of them** to a different disk. NOTE: these recovery steps will clear all persistent memory disks, even the ones that aren't affected by this problem, so it's important to back up all your data.\r\n            %n5. Open the registry editor, navigate to the 'IgnoreLabels' value you created and set it to 0.\r\n            %n6. Restart your computer.\r\n            %n7. The persistent memory disk will be inaccessible again. To use it, you will have to reinitialize all physical persistent memory devices on the system. Open an elevated PowerShell window and run 'Get-PmemPhysicalDevice | Initialize-PmemPhysicalDevice'.\r\n            %n8. The last step is to recreate the persistent memory disks. You can do that in the elevated PowerShell window by running 'Get-PmemUnusedRegion | New-PmemDisk'. Look at the help content for 'New-PmemDisk' to learn how to specify the disks' atomicity modes.\r\n
0xb0000384 | Persistent memory disk %1 logged:\r\n            %n\r\n            %n %2\r\n
0xb00200d2 | Some physical memory locations on persistent memory disk %1 are corrupt. In order to protect your computer, Windows will not access those locations and you may see failures trying to read or write to your data. Contact your hardware vendor to learn what recovery steps are available.\r\n
0xd0000001 | The driver encountered an internal error.\r\n
0xd0000002 | The driver could not interpret the device's memory resources.\r\n
0xd0000003 | The driver could not discover the device's interleaving settings.\r\n
0xd0000004 | The driver could not read the device's serial number.\r\n
0xd0000005 | The driver could not discover whether boot-time operations, like save and restore, succeeded.\r\n
0xd0000006 | The driver could not register to be notified of health-related events on the NVDIMM.\r\n
0xd0000007 | The driver could not determine the health status of the persistent memory disk.\r\n
0xd0000008 | There is an uncorrectable memory error in a critical region of the persistent memory disk.\r\n
0xd0000009 | unknown\r\n
0xd000000a | unhealthy\r\n
0xd000000b | warning\r\n
0xd000000c | healthy\r\n

### 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x0000012c | Persistent memory disk %1 is now in read-only mode.  Use the Get-PhysicalDisk command to get the device’s health status.  The Microsoft-Windows-PersistentMemory-PmemDisk/Operational event log may also contain more information.\r\n
0x0000012d | Persistent memory disk %1 is no longer in read-only mode.\r\n
0x0000012e | Windows does not support this configuration: two or more NVDIMMs on this system are part of an interleaved set. Back up the data on the interleaved set to a different drive and then break up the interleaved set. Consider using Storage Spaces if NVDIMM capacity needs to be aggregated.\r\n
0x10000002 | Hardware events\r\n
0x10000021 | Read request\r\n
0x10000022 | Write request\r\n
0x10000023 | Paging Read request\r\n
0x10000024 | Paging Write request\r\n
0x10000025 | Non-Read/Write request\r\n
0x10000026 | Device I/O control request\r\n
0x10000027 | PnP request\r\n
0x10000028 | IO Performance measurement\r\n
0x30000000 | Info\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000001 | Reported memory resource.\r\n
0xb0000002 | Memory operation duration, in hundreds of nanoseconds.\r\n
0xb0000003 | Request servicing time taken by lower driver stack(s).\r\n
0xb0000065 | Dispatching a read request.\r\n
0xb0000066 | Dispatching a write request.\r\n
0xb0000069 | Completing an IO (read/write) request.\r\n
0xb000006a | Dispatching an IOCTL.\r\n
0xb000006b | Completing a non-read/write request.\r\n
0xb000006c | Dispatching a PnP request.\r\n
0xb000006d | Completing a PnP request.\r\n
0xb00000ca | Persistent memory disk %1 failed to start.\r\n                   %nReason: %5\r\n                   %nNTSTATUS code: %6\r\n
0xb00000cb | Persistent memory disk %1 started successfully.\r\n
0xb00000cc | One of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media (see the Details tab for more information). Some of your data may have been lost. As a precaution, this persistent memory disk is now in read-only mode. If you want to keep using it, run the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000cd | During a previous boot session, one of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media. Some of your data may have been lost then. As a precaution, Windows made this persistent memory disk temporarily read-only. If you want to keep using this persistent memory disk, use the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000ce | NVDIMM %5 notified persistent memory disk %1 of a change in its health state. The NVDIMM now has the following health status: %7.\r\n
0xb00000cf | One of the NVDIMMs that make up the persistent memory disk %1 encountered a serious problem and the disk is now in read-only mode. Data that was saved to this disk may be lost when the computer shuts down or restarts. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nUse the Get-PhysicalDisk command to get more information about the disk's health status.\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000d1 | The computer didn't assign any memory resources to persistent memory disk %1. You won't be able to access the data on the device, but you can still query its health status by using the Get-PhysicalDisk command.\r\n
0xb00000d3 | The problem with the persistent memory disk %1 was resolved and it is now back in read-write mode.\r\n
0xb00000d4 | One of the NVDIMMs that make up the persistent memory disk %1 is in a degraded health state and may soon encounter serious problems. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00000d5 | The physical devices that make up persistent memory disk %1 have an atomicity setting that is incompatible with the data on the disk. Windows didn't start the disk to prevent data loss.\r\n            %n\r\n            %nThis type of problem can happen when you update your computer's firmware, or when you upgrade from a version of Windows that doesn't look at atomicity settings to one that does.\r\n            %n\r\n            %nTo recover the disk, follow these steps:\r\n            %n1. Open the registry editor (regedit) and navigate to 'Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\ACPI\ACPI0012\<instance ID>\Device Parameters'. There will only be one instance ID key.\r\n            %n2. Create a registry key named 'ScmBus'. Inside it, create a new DWORD value named 'IgnoreLabels' and set it to 1.\r\n            %n3. Restart your computer.\r\n            %n4. When Windows starts again, your persistent memory disks will be accessible. Back up **all the data** on **all of them** to a different disk. NOTE: these recovery steps will clear all persistent memory disks, even the ones that aren't affected by this problem, so it's important to back up all your data.\r\n            %n5. Open the registry editor, navigate to the 'IgnoreLabels' value you created and set it to 0.\r\n            %n6. Restart your computer.\r\n            %n7. The persistent memory disk will be inaccessible again. To use it, you will have to reinitialize all physical persistent memory devices on the system. Open an elevated PowerShell window and run 'Get-PmemPhysicalDevice | Initialize-PmemPhysicalDevice'.\r\n            %n8. The last step is to recreate the persistent memory disks. You can do that in the elevated PowerShell window by running 'Get-PmemUnusedRegion | New-PmemDisk'. Look at the help content for 'New-PmemDisk' to learn how to specify the disks' atomicity modes.\r\n
0xb00000d6 | The persistent memory disk %1 is inaccessible because at least one of its NVDIMMs are locked. Contact your hardware vendor for instructions on how to unlock the NVDIMMs.\r\n
0xb00000d7 | The driver for persistent memory disk %1 encountered an internal error. The information in the Details tab might help Microsoft or your platform vendor to diagnose the problem.\r\n
0xb0000384 | Persistent memory disk %1 logged:\r\n            %n\r\n            %n %2\r\n
0xb00200d2 | Some physical memory locations on persistent memory disk %1 are corrupt. In order to protect your computer, Windows will not access those locations and you may see failures trying to read or write to your data. Contact your hardware vendor to learn what recovery steps are available.\r\n
0xd0000001 | The driver encountered an internal error.\r\n
0xd0000002 | The driver could not interpret the device's memory resources.\r\n
0xd0000003 | The driver could not discover the device's interleaving settings.\r\n
0xd0000004 | The driver could not read the device's serial number.\r\n
0xd0000005 | The driver could not discover whether boot-time operations, like save and restore, succeeded.\r\n
0xd0000006 | The driver could not register to be notified of health-related events on the NVDIMM.\r\n
0xd0000007 | The driver could not determine the health status of the persistent memory disk.\r\n
0xd0000008 | There is an uncorrectable memory error in a critical region of the persistent memory disk.\r\n
0xd0000009 | unknown\r\n
0xd000000a | unhealthy\r\n
0xd000000b | warning\r\n
0xd000000c | healthy\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x0000012c | Persistent memory disk %1 is now in read-only mode.  Use the Get-PhysicalDisk command to get the device’s health status.  The Microsoft-Windows-PersistentMemory-PmemDisk/Operational event log may also contain more information.\r\n
0x0000012d | Persistent memory disk %1 is no longer in read-only mode.\r\n
0x0000012e | Windows does not support this configuration: two or more NVDIMMs on this system are part of an interleaved set. Back up the data on the interleaved set to a different drive and then break up the interleaved set. Consider using Storage Spaces if NVDIMM capacity needs to be aggregated.\r\n
0x10000002 | Hardware events\r\n
0x10000021 | Read request\r\n
0x10000022 | Write request\r\n
0x10000023 | Paging Read request\r\n
0x10000024 | Paging Write request\r\n
0x10000025 | Non-Read/Write request\r\n
0x10000026 | Device I/O control request\r\n
0x10000027 | PnP request\r\n
0x10000028 | IO Performance measurement\r\n
0x30000000 | Info\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000001 | Reported memory resource.\r\n
0xb0000002 | Memory operation duration, in hundreds of nanoseconds.\r\n
0xb0000003 | Request servicing time taken by lower driver stack(s).\r\n
0xb0000065 | Dispatching a read request.\r\n
0xb0000066 | Dispatching a write request.\r\n
0xb0000069 | Completing an IO (read/write) request.\r\n
0xb000006a | Dispatching an IOCTL.\r\n
0xb000006b | Completing a non-read/write request.\r\n
0xb000006c | Dispatching a PnP request.\r\n
0xb000006d | Completing a PnP request.\r\n
0xb00000d8 | The driver couldn't configure the dump stack on persistent memory disk %1, which may cause hibernation or memory dump generation to fail.\r\n
0xb0000384 | Persistent memory disk %1 logged:\r\n            %n\r\n            %n %2\r\n
0xb00100d7 | The driver for persistent memory disk %1 encountered an internal error. The information in the Details tab might help Microsoft or your platform vendor to diagnose the problem.\r\n
0xb00200ca | Persistent memory disk %1 failed to start.\r\n                   %nReason: %5\r\n                   %nNTSTATUS code: %6\r\n
0xb00200cb | Persistent memory disk %1 started successfully.\r\n
0xb00200cc | One of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media (see the Details tab for more information). Some of your data may have been lost. If this is a data disk, it is now in read-only mode as a precaution. If you want to keep using it, run the Reset-PhysicalDisk command to make it writeable again. If this is the system disk, it will remain writeable but will appear as Unhealthy until you run the Reset-PhysicalDisk command in PowerShell.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00200cd | During a previous boot session, one of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media. Some of your data may have been lost then. If this is a data disk, it is now in read-only mode as a precaution. If you want to keep using it, run the Reset-PhysicalDisk command to make it writeable again. If this is the system disk, it will remain writeable but will appear as Unhealthy until you run the Reset-PhysicalDisk command in PowerShell.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00200ce | NVDIMM %5 notified persistent memory disk %1 of a change in its health state. The NVDIMM now has the following health status: %7.\r\n
0xb00200cf | One of the NVDIMMs that make up the persistent memory disk %1 encountered a serious problem and the disk is now in read-only mode. Data that was saved to this disk may be lost when the computer shuts down or restarts. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nUse the Get-PhysicalDisk command to get more information about the disk's health status.\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00200d1 | The computer didn't assign any memory resources to persistent memory disk %1. You won't be able to access the data on the device, but you can still query its health status by using the Get-PhysicalDisk command.\r\n
0xb00200d3 | The problem with the persistent memory disk %1 was resolved and it is now back in read-write mode.\r\n
0xb00200d4 | One of the NVDIMMs that make up the persistent memory disk %1 is in a degraded health state and may soon encounter serious problems. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00200d5 | The physical devices that make up persistent memory disk %1 have an atomicity setting that is incompatible with the data on the disk. Windows didn't start the disk to prevent data loss.\r\n            %n\r\n            %nThis type of problem can happen when you update your computer's firmware, or when you upgrade from a version of Windows that doesn't look at atomicity settings to one that does.\r\n            %n\r\n            %nTo recover the disk, follow these steps:\r\n            %n1. Open the registry editor (regedit) and navigate to 'Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\ACPI\ACPI0012\<instance ID>\Device Parameters'. There will only be one instance ID key.\r\n            %n2. Create a registry key named 'ScmBus'. Inside it, create a new DWORD value named 'IgnoreLabels' and set it to 1.\r\n            %n3. Restart your computer.\r\n            %n4. When Windows starts again, your persistent memory disks will be accessible. Back up **all the data** on **all of them** to a different disk. NOTE: these recovery steps will clear all persistent memory disks, even the ones that aren't affected by this problem, so it's important to back up all your data.\r\n            %n5. Open the registry editor, navigate to the 'IgnoreLabels' value you created and set it to 0.\r\n            %n6. Restart your computer.\r\n            %n7. The persistent memory disk will be inaccessible again. To use it, you will have to reinitialize all physical persistent memory devices on the system. Open an elevated PowerShell window and run 'Get-PmemPhysicalDevice | Initialize-PmemPhysicalDevice'.\r\n            %n8. The last step is to recreate the persistent memory disks. You can do that in the elevated PowerShell window by running 'Get-PmemUnusedRegion | New-PmemDisk'. Look at the help content for 'New-PmemDisk' to learn how to specify the disks' atomicity modes.\r\n
0xb00200d6 | The persistent memory disk %1 is inaccessible because at least one of its NVDIMMs are locked. Contact your hardware vendor for instructions on how to unlock the NVDIMMs.\r\n
0xb00300d2 | Some physical memory locations on persistent memory disk %1 are corrupt. In order to protect your computer, Windows will not access those locations and you may see failures trying to read or write to your data. Contact your hardware vendor to learn what recovery steps are available.\r\n
0xd0000001 | The driver encountered an internal error.\r\n
0xd0000002 | The driver could not interpret the device's memory resources.\r\n
0xd0000003 | The driver could not discover the device's interleaving settings.\r\n
0xd0000004 | The driver could not read the device's serial number.\r\n
0xd0000005 | The driver could not discover whether boot-time operations, like save and restore, succeeded.\r\n
0xd0000006 | The driver could not register to be notified of health-related events on the NVDIMM.\r\n
0xd0000007 | The driver could not determine the health status of the persistent memory disk.\r\n
0xd0000008 | There is an uncorrectable memory error in a critical region of the persistent memory disk.\r\n
0xd0000009 | unknown\r\n
0xd000000a | unhealthy\r\n
0xd000000b | warning\r\n
0xd000000c | healthy\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x0000012c | Persistent memory disk %1 is now in read-only mode.  Use the Get-PhysicalDisk command to get the device’s health status.  The Microsoft-Windows-PersistentMemory-PmemDisk/Operational event log may also contain more information.\r\n
0x0000012d | Persistent memory disk %1 is no longer in read-only mode.\r\n
0x0000012e | Windows does not support this configuration: two or more NVDIMMs on this system are part of an interleaved set. Back up the data on the interleaved set to a different drive and then break up the interleaved set. Consider using Storage Spaces if NVDIMM capacity needs to be aggregated.\r\n
0x10000002 | Hardware events\r\n
0x10000021 | Read request\r\n
0x10000022 | Write request\r\n
0x10000023 | Paging Read request\r\n
0x10000024 | Paging Write request\r\n
0x10000025 | Non-Read/Write request\r\n
0x10000026 | Device I/O control request\r\n
0x10000027 | PnP request\r\n
0x10000028 | IO Performance measurement\r\n
0x30000000 | Info\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000001 | Reported memory resource.\r\n
0xb0000002 | Memory operation duration, in hundreds of nanoseconds.\r\n
0xb0000003 | Request servicing time taken by lower driver stack(s).\r\n
0xb0000065 | Dispatching a read request.\r\n
0xb0000066 | Dispatching a write request.\r\n
0xb0000069 | Completing an IO (read/write) request.\r\n
0xb000006a | Dispatching an IOCTL.\r\n
0xb000006b | Completing a non-read/write request.\r\n
0xb000006c | Dispatching a PnP request.\r\n
0xb000006d | Completing a PnP request.\r\n
0xb0000384 | Persistent memory disk %1 logged:\r\n            %n\r\n            %n %2\r\n
0xb00100d7 | The driver for persistent memory disk %1 encountered an internal error. The information in the Details tab might help Microsoft or your platform vendor to diagnose the problem.\r\n
0xb00100d8 | The driver couldn't configure the dump stack on persistent memory disk %1, which may cause hibernation or memory dump generation to fail.\r\n
0xb00100d9 | The persistent memory disk %1 changed its powerfail persistence mode to %2. (0 is PerformanceMode, 1 is DurabilityMode)\r\n
0xb00200ca | Persistent memory disk %1 failed to start.\r\n                   %nReason: %7\r\n                   %nNTSTATUS code: %8\r\n
0xb00200cb | Persistent memory disk %1 started successfully.\r\n
0xb00200cc | One of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media (see the Details tab for more information). Some of your data may have been lost. If this is a data disk, it is now in read-only mode as a precaution. If you want to keep using it, run the Reset-PhysicalDisk command to make it writeable again. If this is the system disk, it will remain writeable but will appear as Unhealthy until you run the Reset-PhysicalDisk command in PowerShell.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00200cd | During a previous boot session, one of the NVDIMMs that make up persistent memory disk %1 encountered an error while transferring your data to or from persistent media. Some of your data may have been lost then. If this is a data disk, it is now in read-only mode as a precaution. If you want to keep using it, run the Reset-PhysicalDisk command to make it writeable again. If this is the system disk, it will remain writeable but will appear as Unhealthy until you run the Reset-PhysicalDisk command in PowerShell.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00200ce | NVDIMM %5 notified persistent memory disk %1 of a change in its health state. The NVDIMM now has the following health status: %7.\r\n
0xb00200cf | One of the NVDIMMs that make up the persistent memory disk %1 encountered a serious problem and the disk is now in read-only mode. Data that was saved to this disk may be lost when the computer shuts down or restarts. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nUse the Get-PhysicalDisk command to get more information about the disk's health status.\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00200d1 | The computer didn't assign any memory resources to persistent memory disk %1. You won't be able to access the data on the device, but you can still query its health status by using the Get-PhysicalDisk command.\r\n
0xb00200d3 | The problem with the persistent memory disk %1 was resolved and it is now back in read-write mode.\r\n
0xb00200d4 | One of the NVDIMMs that make up the persistent memory disk %1 is in a degraded health state and may soon encounter serious problems. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nLook at the events logged by the physical NVDIMM driver for more details.\r\n
0xb00200d5 | The physical devices that make up persistent memory disk %1 have an atomicity setting that is incompatible with the data on the disk. Windows didn't start the disk to prevent data loss.\r\n            %n\r\n            %nThis type of problem can happen when you update your computer's firmware, or when you upgrade from a version of Windows that doesn't look at atomicity settings to one that does.\r\n            %n\r\n            %nTo recover the disk, follow these steps:\r\n            %n1. Open the registry editor (regedit) and navigate to 'Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\ACPI\ACPI0012\<instance ID>\Device Parameters'. There will only be one instance ID key.\r\n            %n2. Create a registry key named 'ScmBus'. Inside it, create a new DWORD value named 'IgnoreLabels' and set it to 1.\r\n            %n3. Restart your computer.\r\n            %n4. When Windows starts again, your persistent memory disks will be accessible. Back up **all the data** on **all of them** to a different disk. NOTE: these recovery steps will clear all persistent memory disks, even the ones that aren't affected by this problem, so it's important to back up all your data.\r\n            %n5. Open the registry editor, navigate to the 'IgnoreLabels' value you created and set it to 0.\r\n            %n6. Restart your computer.\r\n            %n7. The persistent memory disk will be inaccessible again. To use it, you will have to reinitialize all physical persistent memory devices on the system. Open an elevated PowerShell window and run 'Get-PmemPhysicalDevice | Initialize-PmemPhysicalDevice'.\r\n            %n8. The last step is to recreate the persistent memory disks. You can do that in the elevated PowerShell window by running 'Get-PmemUnusedRegion | New-PmemDisk'. Look at the help content for 'New-PmemDisk' to learn how to specify the disks' atomicity modes.\r\n
0xb00200d6 | The persistent memory disk %1 is inaccessible because at least one of its NVDIMMs are locked. Contact your hardware vendor for instructions on how to unlock the NVDIMMs.\r\n
0xb00300d2 | Some physical memory locations on persistent memory disk %1 are corrupt. In order to protect your computer, Windows will not access those locations and you may see failures trying to read or write to your data. Contact your hardware vendor to learn what recovery steps are available.\r\n
0xd0000001 | The driver encountered an internal error.\r\n
0xd0000002 | The driver could not interpret the device's memory resources.\r\n
0xd0000003 | The driver could not discover the device's interleaving settings.\r\n
0xd0000004 | The driver could not read the device's serial number.\r\n
0xd0000005 | The driver could not discover whether boot-time operations, like save and restore, succeeded.\r\n
0xd0000006 | The driver could not register to be notified of health-related events on the NVDIMM.\r\n
0xd0000007 | The driver could not determine the health status of the persistent memory disk.\r\n
0xd0000008 | There is an uncorrectable memory error in a critical region of the persistent memory disk.\r\n
0xd0000009 | unknown\r\n
0xd000000a | unhealthy\r\n
0xd000000b | warning\r\n
0xd000000c | healthy\r\n
