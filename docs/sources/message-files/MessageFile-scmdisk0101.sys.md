## scmdisk0101.sys

Path: %SystemRoot%\system32\drivers\scmdisk0101.sys

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x0000012c | NVDIMM %1 is now in read-only mode.  Use the Get-PhysicalDisk command to get the device’s health status.  The Microsoft-Windows-ScmDisk0101/Operational event log may also contain more information.\r\n
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
0xb00000c9 | Critical metadata on NVDIMM %1 has been corrupted. Windows needs this metadata to start the NVDIMM correctly, so we had to reinitialize it. The data on that NVDIMM may have been lost.\n                   %n\n                   %nConsider replacing the NVDIMM.\n                   %n\n                   %nThis NVDIMM may be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000ca | NVDIMM %1 failed to start. %6\n                   %n\n                   %nThis NVDIMM may be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000cb | NVDIMM %1 started successfully.\r\n
0xb00000cc | NVDIMM %1 encountered an error while transferring your data to or from persistent media (see the Details tab for more information). Some of your data may have been lost. As a precaution, this NVDIMM is now in read-only mode. If you want to keep using this NVDIMM, use the Reset-PhysicalDisk command to make it writeable again.\n                   %n\n                   %nThis NVDIMM may need to be replaced. It can be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000cd | During a previous boot session, the NVDIMM %1 encountered an error while transferring your data to or from persistent media. Some of your data may have been lost then. As a precaution, Windows made this NVDIMM temporarily read-only. If you want to keep using this NVDIMM, use the Reset-PhysicalDisk command to make it writeable again.\n                   %n\n                   %nThis NVDIMM may need to be replaced. It can be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000ce | NVDIMM %1 notified the driver that its health state changed.\n                   %n\n                   %nThis NVDIMM may be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000cf | NVDIMM %1 encountered a serious problem and is now in read-only mode. Data that was saved to this NVDIMM may be lost when the computer shuts down or restarts. Consider backing up your data to another disk.\n                   %n\n                   %nUse the Get-PhysicalDisk command to get more information about the device’s health status.\n                   %n\n                   %nThis NVDIMM may need to be replaced. It can be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000d0 | The driver could not confirm that the NVDIMM %1 is healthy. To protect your data, the NVDIMM is now in read-only mode. Consider backing up your data to another disk.\n                   %n\n                   %nThis NVDIMM may need to be replaced. It can be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000d1 | The computer didn't assign any memory resources to NVDIMM %1. You won't be able to access the data on the device, but you can still query its health status by using the Get-PhysicalDisk command.\n                   %n\n                   %nThis NVDIMM may need to be replaced. It can be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000d2 | Some physical memory locations on NVDIMM %1 are corrupt. In order to protect your computer, Windows will not access those locations and you may see failures trying to read or write to your data. Contact your hardware vendor to learn what recovery steps are available.\n            %n\n            %nThis NVDIMM may need to be replaced. It can be located using the following information:\n            %n\n            %nSlot number: %2\n            %nManufacturer: %3\n            %nModel Number: %4\n            %nSerial Number: %5\r\n
0xb00000d3 | The problem with NVDIMM %1 was resolved and it is now back in read-write mode.\n                   %n\n                   %nThis NVDIMM may be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000d4 | NVDIMM %1 is in a degraded health state and may soon encounter serious problems. Consider backing up your data to another disk. Use the Get-PhysicalDisk command to see more information.\n                   %n\n                   %nThis NVDIMM may need to be replaced. It can be located using the following information:\n                   %n\n                   %nSlot number: %2\n                   %nManufacturer: %3\n                   %nModel Number: %4\n                   %nSerial Number: %5\r\n
0xb00000d5 | NVDIMM %1 has encountered %6 uncorrectable memory error(s). Uncorrectable memory errors can cause system instability and data loss. Consider replacing this NVDIMM.\n            %n\n            %nThis NVDIMM can be located using the following information:\n            %n\n            %nSlot number: %2\n            %nManufacturer: %3\n            %nModel Number: %4\n            %nSerial Number: %5\r\n
0xb00000d6 | The warning threshold for correctable memory errors on NVDIMM %1 has been exceeded. A large number of correctable memory errors increases the likelihood of an uncorrectable memory error in the future and reduces system performance. Contact your hardware vendor to determine if this NVDIMM needs to be replaced.\n            %n\n            %nThis NVDIMM can be located using the following information:\n            %n\n            %nSlot number: %2\n            %nManufacturer: %3\n            %nModel Number: %4\n            %nSerial Number: %5\r\n
0xb0000384 | NVDIMM %1 logged:\n            %n\n            %n %2\r\n
0xd0000001 | The driver encountered an internal error.\r\n
0xd0000002 | The driver could not interpret the device's memory resources.\r\n
0xd0000003 | The driver could not discover the device's interleaving settings.\r\n
0xd0000004 | The driver could not read the device's serial number.\r\n
0xd0000005 | The driver could not discover whether boot-time operations, like save and restore, succeeded.\r\n
0xd0000006 | The driver could not register to be notified of health-related events on the NVDIMM.\r\n
0xd0000007 | The driver could not confirm that the NVDIMM is healthy.\r\n
