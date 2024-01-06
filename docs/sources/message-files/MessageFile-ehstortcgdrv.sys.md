## ehstortcgdrv.sys

Path: %SystemRoot%\System32\Drivers\EhStorTcgDrv.sys

### 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.14393.187, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000001 | An operation has failed (%3, %4, %5, %6).%n%1%nHResult: %2\r\n
0x00000002 | An operation has failed (%3, %4, %5, %6).%n%1%nWin32Error: %2\r\n
0x00000003 | An operation has failed (%3, %4, %5, %6).%n%1%nNTStatus: %2\r\n
0x00000004 | Failed to allocate object.%nObject: %1%nSize: %2\r\n
0x00000005 | Unexpected size.%nObject: %1%nExpected Size: %2%nActual Size: %3\r\n
0x00000006 | Invalid data.%nName: %1%nValue: %2\r\n
0x00000007 | Device responded with an error status.%nStatus: %1\r\n
0x00000008 | Bad device.%nDevice: %1%nReason: %2\r\n
0x00000009 | The function is not supported.%nFunction: %1%nContext: %2\r\n
0x0000000a | A TCG Command has returned an error.%nDesc: %1%nParam1: %2%nParam2: %3%nParam3: %4%nParam4: %5%nStatus: %6\r\n
0x0000000b | A TCG Silo Command has returned an error.%n%1%nSiloCommand=%2, SiloStatus=%3%nInvokingID=%4, MethodID=%5\r\n
0x0000000c | A TCG Silo has returned the capabilities value of %1.\r\n
0x0000000d | The system has performed an authentication operation on an Enhanced Storage device.%nBandID=%1%nAuthorize=%2%nStatus=%3\r\n
0x00000064 | The following informational event has occurred (%2, %3, %4, %5).%n%1\r\n
0x00000065 | The following warning event has occurred (%2, %3, %4, %5).%n%1\r\n
0x00000066 | The following error event has occurred (%2, %3, %4, %5).%n%1\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000032 | General\r\n
0x30000033 | Init\r\n
0x30000034 | Pnp\r\n
0x30000035 | Power\r\n
0x30000036 | IoRequest\r\n
0x30000037 | Ioctl\r\n
0x30000038 | IoQueue\r\n
0x30000039 | TcgLib\r\n
0x3000003a | TcgSilo\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Driver\r\n
0x70000002 | GetSiloCaps\r\n
0x70000003 | ExecuteSiloCmd\r\n
0x70000004 | Reset\r\n
0x70000005 | IoctlQueryCapabilities\r\n
0x70000006 | IoctlActivate\r\n
0x70000007 | IoctlRevert\r\n
0x70000008 | IoctlEnumerateBands\r\n
0x70000009 | IoctlCreateBand\r\n
0x7000000a | IoctlSetBandLocation\r\n
0x7000000b | IoctlSetBandSecurity\r\n
0x7000000c | IoctlDeleteBand\r\n
0x7000000d | IoctlEraseBand\r\n
0x7000000e | IoctlGetBandMetadata\r\n
0x7000000f | IoctlSetBandMetadata\r\n
0x70000010 | IoctlRelinquishSilo\r\n
0x90000001 | Microsoft-Windows-EnhancedStorage-EhStorTcgDrv\r\n
0x90000002 | System\r\n
0xb00000c8 | Get silo capabilities (SiloCmd=%2).\r\n
0xb00000c9 | Get silo capabilities returned (SiloCmd=%2, Status=%3).\r\n
0xb00000ca | Execute silo command (SiloCmd=%2).\r\n
0xb00000cb | Excute silo command returned (SiloCmd=%2, Status=%3).%nInvokingId = %4%nMethodId = %5\r\n
0xb00000cc | Silo reset (SiloCmd=%2).\r\n
0xb00000cd | Silo reset returned (SiloCmd=%2, Status=%3).\r\n
0xb00000ce | Ioctl: QueryCapabilities\r\n
0xb00000cf | Ioctl: QueryCapabilities returned (Status=%2).\r\n
0xb00000d0 | Ioctl: Activate\r\n
0xb00000d1 | Ioctl: Activate returned (Status=%2).\r\n
0xb00000d2 | Ioctl: Revert\r\n
0xb00000d3 | Ioctl: Revert returned (Status=%2).\r\n
0xb00000d4 | Ioctl: EnumBands\r\n
0xb00000d5 | Ioctl: EnumBands returned (Status=%2).\r\n
0xb00000d6 | Ioctl: CreateBand\r\n
0xb00000d7 | Ioctl: CreateBand returned (Status=%2).\r\n
0xb00000d8 | Ioctl: SetBandLocation\r\n
0xb00000d9 | Ioctl: SetBandLocation returned (Status=%2).\r\n
0xb00000da | Ioctl: SetBandSecurity\r\n
0xb00000db | Ioctl: SetBandSecurity returned (Status=%2).\r\n
0xb00000dc | Ioctl: DeleteBand\r\n
0xb00000dd | Ioctl: DeleteBand returned (Status=%2).\r\n
0xb00000de | Ioctl: EraseBand\r\n
0xb00000df | Ioctl: EraseBand returned (Status=%2).\r\n
0xb00000e0 | Ioctl: GetBandMetadata\r\n
0xb00000e1 | Ioctl: GetBandMetadata returned (Status=%2).\r\n
0xb00000e2 | Ioctl: SetBandMetadata\r\n
0xb00000e3 | Ioctl: SetBandMetadata returned (Status=%2).\r\n
0xb00000e4 | Ioctl: RelinquishSilo\r\n
0xb00000e5 | Ioctl: RelinquishSilo returned (Status=%2).\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000001 | An operation has failed (%3, %4, %5, %6).%n%1%nHResult: %2\r\n
0x00000002 | An operation has failed (%3, %4, %5, %6).%n%1%nWin32Error: %2\r\n
0x00000003 | An operation has failed (%3, %4, %5, %6).%n%1%nNTStatus: %2\r\n
0x00000004 | Failed to allocate object.%nObject: %1%nSize: %2\r\n
0x00000005 | Unexpected size.%nObject: %1%nExpected Size: %2%nActual Size: %3\r\n
0x00000006 | Invalid data.%nName: %1%nValue: %2\r\n
0x00000007 | Device responded with an error status.%nStatus: %1\r\n
0x00000008 | Bad device.%nDevice: %1%nReason: %2\r\n
0x00000009 | The function is not supported.%nFunction: %1%nContext: %2\r\n
0x0000000a | A TCG Command has returned an error.%nDesc: %1%nParam1: %2%nParam2: %3%nParam3: %4%nParam4: %5%nStatus: %6\r\n
0x0000000b | A TCG Silo Command has returned an error.%n%1%nSiloCommand=%2, SiloStatus=%3%nInvokingID=%4, MethodID=%5\r\n
0x0000000c | A TCG Silo has returned the capabilities value of %1.\r\n
0x0000000d | The system has performed an authentication operation on an Enhanced Storage device.%nBandID=%1%nAuthorize=%2%nStatus=%3\r\n
0x00000064 | The following informational event has occurred (%2, %3, %4, %5).%n%1\r\n
0x00000065 | The following warning event has occurred (%2, %3, %4, %5).%n%1\r\n
0x00000066 | The following error event has occurred (%2, %3, %4, %5).%n%1\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000032 | General\r\n
0x30000033 | Init\r\n
0x30000034 | Pnp\r\n
0x30000035 | Power\r\n
0x30000036 | IoRequest\r\n
0x30000037 | Ioctl\r\n
0x30000038 | IoQueue\r\n
0x30000039 | TcgLib\r\n
0x3000003a | TcgSilo\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Driver\r\n
0x70000002 | GetSiloCaps\r\n
0x70000003 | ExecuteSiloCmd\r\n
0x70000004 | Reset\r\n
0x70000005 | IoctlQueryCapabilities\r\n
0x70000006 | IoctlActivate\r\n
0x70000007 | IoctlRevert\r\n
0x70000008 | IoctlEnumerateBands\r\n
0x70000009 | IoctlCreateBand\r\n
0x7000000a | IoctlSetBandLocation\r\n
0x7000000b | IoctlSetBandSecurity\r\n
0x7000000c | IoctlDeleteBand\r\n
0x7000000d | IoctlEraseBand\r\n
0x7000000e | IoctlGetBandMetadata\r\n
0x7000000f | IoctlSetBandMetadata\r\n
0x70000010 | IoctlRelinquishSilo\r\n
0x70000011 | IoctlSetSid\r\n
0x90000001 | Microsoft-Windows-EnhancedStorage-EhStorTcgDrv\r\n
0x90000002 | System\r\n
0xb00000c8 | Get silo capabilities (SiloCmd=%2).\r\n
0xb00000c9 | Get silo capabilities returned (SiloCmd=%2, Status=%3).\r\n
0xb00000ca | Execute silo command (SiloCmd=%2).\r\n
0xb00000cb | Excute silo command returned (SiloCmd=%2, Status=%3).%nInvokingId = %4%nMethodId = %5\r\n
0xb00000cc | Silo reset (SiloCmd=%2).\r\n
0xb00000cd | Silo reset returned (SiloCmd=%2, Status=%3).\r\n
0xb00000ce | Ioctl: QueryCapabilities\r\n
0xb00000cf | Ioctl: QueryCapabilities returned (Status=%2).\r\n
0xb00000d0 | Ioctl: Activate\r\n
0xb00000d1 | Ioctl: Activate returned (Status=%2).\r\n
0xb00000d2 | Ioctl: Revert\r\n
0xb00000d3 | Ioctl: Revert returned (Status=%2).\r\n
0xb00000d4 | Ioctl: EnumBands\r\n
0xb00000d5 | Ioctl: EnumBands returned (Status=%2).\r\n
0xb00000d6 | Ioctl: CreateBand\r\n
0xb00000d7 | Ioctl: CreateBand returned (Status=%2).\r\n
0xb00000d8 | Ioctl: SetBandLocation\r\n
0xb00000d9 | Ioctl: SetBandLocation returned (Status=%2).\r\n
0xb00000da | Ioctl: SetBandSecurity\r\n
0xb00000db | Ioctl: SetBandSecurity returned (Status=%2).\r\n
0xb00000dc | Ioctl: DeleteBand\r\n
0xb00000dd | Ioctl: DeleteBand returned (Status=%2).\r\n
0xb00000de | Ioctl: EraseBand\r\n
0xb00000df | Ioctl: EraseBand returned (Status=%2).\r\n
0xb00000e0 | Ioctl: GetBandMetadata\r\n
0xb00000e1 | Ioctl: GetBandMetadata returned (Status=%2).\r\n
0xb00000e2 | Ioctl: SetBandMetadata\r\n
0xb00000e3 | Ioctl: SetBandMetadata returned (Status=%2).\r\n
0xb00000e4 | Ioctl: RelinquishSilo\r\n
0xb00000e5 | Ioctl: RelinquishSilo returned (Status=%2).\r\n
0xb00000e6 | Ioctl: SetSid\r\n
0xb00000e7 | Ioctl: SetSid returned (Status=%2).\r\n
