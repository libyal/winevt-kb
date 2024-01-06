## nvdimmn.sys

Path: %SystemRoot%\system32\drivers\nvdimmn.sys

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x10000002 | Hardware events\r\n
0x10000025 | Non-Read/Write request\r\n
0x10000026 | Device I/O control request\r\n
0x10000027 | PnP request\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb000006a | Dispatching an IOCTL.\r\n
0xb000006b | Completing a non-read/write request.\r\n
0xb000006c | Dispatching a PnP request.\r\n
0xb000006d | Completing a PnP request.\r\n
0xb00000c9 | NVDIMM-N %1 failed to start. %6\r\n                   %n\r\n                   %nThis NVDIMM-N may be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000ca | NVDIMM-N %1 started successfully.\r\n
0xb00000cb | NVDIMM-N %1 encountered an error while transferring your data to or from persistent media (see the Details tab for more information). Some of your data may have been lost. As a precaution, this NVDIMM-N is now in read-only mode. If you want to keep using this NVDIMM-N, use the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000cc | During a previous boot session, the NVDIMM-N %1 encountered an error while transferring your data to or from persistent media. Some of your data may have been lost then. As a precaution, Windows made this NVDIMM-N temporarily read-only. If you want to keep using this NVDIMM-N, use the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000cd | NVDIMM-N %1 notified the driver that its health state changed.\r\n                   %n\r\n                   %nThis NVDIMM may be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000ce | NVDIMM %1 encountered a serious problem and is now in read-only mode. Data that was saved to this NVDIMM-N may be lost when the computer shuts down or restarts. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nUse the Get-PhysicalDisk command to get more information about the device’s health status.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000cf | The driver could not confirm that the NVDIMM-N %1 is healthy. To protect your data, the NVDIMM-N is now in read-only mode. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000d0 | The problem with NVDIMM-N %1 was resolved and it is now back in read-write mode.\r\n                   %n\r\n                   %nThis NVDIMM-N may be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000d1 | NVDIMM-N %1 is in a degraded health state and may soon encounter serious problems. Consider backing up your data to another disk. Use the Get-PhysicalDisk command to see more information.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n
0xb00000d2 | NVDIMM-N %1 has encountered %6 uncorrectable memory error(s). Uncorrectable memory errors can cause system instability and data loss. Consider replacing this NVDIMM-N.\r\n            %n\r\n            %nThis NVDIMM-N can be located using the following information:\r\n            %n\r\n            %nSlot number: %2\r\n            %nManufacturer: %3\r\n            %nModel Number: %4\r\n            %nSerial Number: %5\r\n
0xb00000d3 | The warning threshold for correctable memory errors on NVDIMM-N %1 has been exceeded. A large number of correctable memory errors increases the likelihood of an uncorrectable memory error in the future and reduces system performance. Contact your hardware vendor to determine if this NVDIMM-N needs to be replaced.\r\n            %n\r\n            %nThis NVDIMM-N can be located using the following information:\r\n            %n\r\n            %nSlot number: %2\r\n            %nManufacturer: %3\r\n            %nModel Number: %4\r\n            %nSerial Number: %5\r\n
0xb00000d4 | Windows could not determine where one of the NVDIMM-N devices on the system is located. As a result, all messages about that NVDIMM-N in this channel will show an invalid number, %1, as the slot number. This is not a fatal error and there is no action required.\r\n
0xb0000384 | NVDIMM-N %1 logged:\r\n            %n\r\n            %n %2\r\n
0xd0000001 | The driver encountered an internal error.\r\n
0xd0000002 | The driver could not read the device's serial number.\r\n
0xd0000003 | The driver could not discover whether boot-time operations, like save and restore, succeeded.\r\n
0xd0000004 | The driver could not register to be notified of health-related events on the NVDIMM-N.\r\n
0xd0000005 | The driver could not confirm that the NVDIMM-N is healthy.\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x10000002 | Hardware events\r\n
0x10000025 | Non-Read/Write request\r\n
0x10000026 | Device I/O control request\r\n
0x10000027 | PnP request\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb000006a | Dispatching an IOCTL.\r\n
0xb000006b | Completing a non-read/write request.\r\n
0xb000006c | Dispatching a PnP request.\r\n
0xb000006d | Completing a PnP request.\r\n
0xb00000c9 | NVDIMM-N %1 failed to start. %6\r\n                   %n\r\n                   %nThis NVDIMM-N may be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000ca | NVDIMM-N %1 started successfully.\r\n
0xb00000cb | NVDIMM-N %1 encountered an error while transferring your data to or from persistent media (see the Details tab for more information). Some of your data may have been lost. As a precaution, this NVDIMM-N is now in read-only mode. If you want to keep using this NVDIMM-N, use the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000cc | During a previous boot session, the NVDIMM-N %1 encountered an error while transferring your data to or from persistent media. Some of your data may have been lost then. As a precaution, Windows made this NVDIMM-N temporarily read-only. If you want to keep using this NVDIMM-N, use the Reset-PhysicalDisk command to make it writeable again.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000cd | NVDIMM-N %1 notified the driver that its health state changed.\r\n                   %n\r\n                   %nThis NVDIMM may be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000ce | NVDIMM %1 encountered a serious problem and is now in read-only mode. Data that was saved to this NVDIMM-N may be lost when the computer shuts down or restarts. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nUse the Get-PhysicalDisk command to get more information about the associated logical device’s health status.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000cf | The driver could not confirm that the NVDIMM-N %1 is healthy. To protect your data, the NVDIMM-N is now in read-only mode. Consider backing up your data to another disk.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000d0 | The problem with NVDIMM-N %1 was resolved and it is now back in read-write mode.\r\n                   %n\r\n                   %nThis NVDIMM-N may be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000d1 | NVDIMM-N %1 is in a degraded health state and may soon encounter serious problems. Consider backing up your data to another disk. Use the Get-PhysicalDisk command to see more information.\r\n                   %n\r\n                   %nThis NVDIMM-N may need to be replaced. It can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000d2 | NVDIMM-N %1 has encountered %6 uncorrectable memory error(s). Uncorrectable memory errors can cause system instability and data loss. Consider replacing this NVDIMM-N.\r\n                   %n\r\n                   %nThis NVDIMM-N can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000d3 | The warning threshold for correctable memory errors on NVDIMM-N %1 has been exceeded. A large number of correctable memory errors increases the likelihood of an uncorrectable memory error in the future and reduces system performance. Contact your hardware vendor to determine if this NVDIMM-N needs to be replaced.\r\n                   %n\r\n                   %nThis NVDIMM-N can be located using the following information:\r\n                   %n\r\n                   %nSlot number: %2\r\n                   %nManufacturer: %3\r\n                   %nModel Number: %4\r\n                   %nSerial Number: %5\r\n                   %nLocation: %6\r\n
0xb00000d4 | Windows could not determine where one of the NVDIMM-N devices on the system is located. As a result, all messages about that NVDIMM-N in this channel will show an invalid number, %1, as the slot number. This is not a fatal error and there is no action required.\r\n
0xb0000384 | NVDIMM-N %1 logged:\r\n            %n\r\n            %n %2\r\n
0xd0000001 | The driver encountered an internal error.\r\n
0xd0000002 | The driver could not read the device's serial number.\r\n
0xd0000003 | The driver could not discover whether boot-time operations, like save and restore, succeeded.\r\n
0xd0000004 | The driver could not register to be notified of health-related events on the NVDIMM-N.\r\n
0xd0000005 | The driver could not confirm that the NVDIMM-N is healthy.\r\n
