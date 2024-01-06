## ialpss2i_i2c.sys

Path: %SystemRoot%\system32\drivers\iaLPSS2i_I2C.sys

### 30.63.1519.7, 30.63.1610.8, 30.100.1633.3, 30.100.1724.1, 30.100.1816.3

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | iaLPSS2_I2C Driver routines\r\n
0x70000002 | iaLPSS2_I2C Init routines\r\n
0x70000003 | iaLPSS2_I2C Power routines\r\n
0x70000004 | iaLPSS2_I2C SPB DDI calls\r\n
0x70000005 | iaLPSS2_I2C Dma routines\r\n
0x70000006 | iaLPSS2_I2C Controller routines\r\n
0x90000001 | Intel-iaLPSS2-I2C\r\n
0x90000002 | iaLPSS2_I2C Debug channel\r\n
0x90000003 | iaLPSS2_I2C Performance channel\r\n
0xb00003e9 | ERROR: %1 - Status:%2\r\n
0xb00003ea | INFO: %1\r\n
0xb00003eb | [%1] -->\r\n
0xb00003ec | [%1] -&lt;--\r\n
0xb00003ed | [%1] -&lt;-- Status:%2\r\n
0xb00003f3 | DriverEntry Start\r\n
0xb00003f4 | DriverEntry End\r\n
0xb00003f5 | Driver ERROR: WdfDriverCreate() returned status:%1\r\n
0xb00003f6 | Driver ERROR: CheckSupportedOs() returned status:%1\r\n
0xb00003f7 | DriverCleanup Info\r\n
0xb00003fd | DeviceAdd Start\r\n
0xb00003fe | DeviceAdd End\r\n
0xb00003ff | Device ERROR: SpbDeviceInitConfig() returned status:%1\r\n
0xb0000400 | Device ERROR: WdfDeviceInitAssignSDDLString() returned status:%1\r\n
0xb0000401 | Device ERROR: WdfDeviceCreate() returned status:%1\r\n
0xb0000402 | Device HW profile FOUND: Instance:%1 Version:%2 Revision:%3 Mode:%4\r\n
0xb0000403 | Device HW profile ERROR: Instance:%1 Version:%2 Revision:%3 Mode:%4\r\n
0xb0000404 | Device ERROR: SpbDeviceInitialize() returned status:%1\r\n
0xb0000405 | Device ERROR: WdfSpinLockCreate() returned status:%1\r\n
0xb0000406 | Device ERROR: WdfInterruptCreate() returned status:%1\r\n
0xb0000407 | Device ERROR: WdfTimerCreate() returned status:%1\r\n
0xb0000408 | Device ERROR: WdfDeviceAssignS0IdleSettings() returned status:%1\r\n
0xb0000411 | PrepareHardware Start\r\n
0xb0000412 | PrepareHardware End\r\n
0xb0000413 | PrepareHardware MBAR%1 mapped: PA:%2 LEN:%3 VA:%4\r\n
0xb0000414 | PrepareHardware WARNING: Too many MBAR resources IDX:%1 PA:%2 LEN:%3 - MBAR disabled\r\n
0xb0000415 | PrepareHardware ERROR: Can't map MMIO for MBAR%1 PA:%2 LEN:%3 - STATUS:%4\r\n
0xb0000416 | PrepareHardware INTERRUPT VEC:%1\r\n
0xb0000417 | PrepareHardware ERROR: Incorrect resource count. MMIO:%1 (exp. 1 or 2) INT:%2 (exp. 1) - STATUS:%3\r\n
0xb0000418 | PrepareHardware ERROR: DMA SW initialization failed\r\n
0xb0000419 | PrepareHardware DMA SW initialized\r\n
0xb000041a | PrepareHardware DMA disabled or not needed\r\n
0xb000041b | ReleaseHardware Start\r\n
0xb000041c | ReleaseHardware End\r\n
0xb0000425 | D0Entry Start\r\n
0xb0000426 | D0Entry End\r\n
0xb0000427 | D0Exit Start\r\n
0xb0000428 | D0Exit End\r\n
0xb0000429 | Power ERROR: PoRegisterPowerSettingCallback() returned status:%1\r\n
0xb000042a | Power ERROR: Invalid power callback context\r\n
0xb000042b | Power INFO: Monitor is %1. Setting idle timeout to %2 ms\r\n
0xb000042c | Power ERROR: WdfDeviceAssignS0IdleSettings() returned status:%1\r\n
0xb000042e | SpbCx DDI: %1\r\n
0xb000042f | SpbCx DDI: EvtSpbTargetConnect: SpbController:%1 SpbTarget:%2\r\n
0xb0000430 | SpbCx DDI: EvtSpbTargetDisconnect: SpbController:%1 SpbTarget:%2\r\n
0xb0000431 | SpbCx DDI: EvtSpbControllerLock: SpbController:%1 SpbTarget:%2 SpbRequest:%3\r\n
0xb0000432 | SpbCx DDI: EvtSpbControllerUnlock: SpbController:%1 SpbTarget:%2 SpbRequest:%3\r\n
0xb0000433 | SpbCx DDI: EvtSpbIoRead: SpbController:%1 SpbTarget:%2 SpbRequest:%3 Length:%4\r\n
0xb0000434 | SpbCx DDI: EvtSpbIoWrite: SpbController:%1 SpbTarget:%2 SpbRequest:%3 Length:%4\r\n
0xb0000435 | SpbCx DDI: EvtSpbIoSequence: SpbController:%1 SpbTarget:%2 SpbRequest:%3 TransferCount:%4\r\n
0xb0000436 | SpbCx DDI: EvtSpbOtherInCallerContext: SpbController:%1 FxRequest:%2\r\n
0xb0000437 | SpbCx DDI: EvtSpbOther: SpbController:%1 SpbTarget:%2 SpbRequest:%3 InLength:%4 OutLength:%5 IoCtrlCode:%6\r\n
0xb0000439 | Controller INFO: Connected to target: Addr:%1 Mode:%2 ClkFreq:%3\r\n
0xb000043a | Controller ERROR: Incorrect target settings - STATUS:%1\r\n
0xb000043b | Controller INFO: Disconnected from target: Addr:%1\r\n
0xb000043c | Controller INFO: Controller locked to target: Addr:%1\r\n
0xb000043d | Controller ERROR: Controller lock failed - STATUS:%1\r\n
0xb000043e | Controller INFO: Connected unlocked from target: Addr:%1\r\n
0xb0000443 | Request INFO: Addr:%1 Idx:%2 Cnt:%3 - context configured for %4 (type:%5) with length %6\r\n
0xb0000444 | Request ERROR: Addr:%1 Idx:%2 Cnt:%3 - invalid request direction %4 (type:%5) with length %6\r\n
0xb0000445 | Request ERROR: Addr:%1 Idx:%2 Cnt:%3 - invalid transfer length %4 (size), supported max is 64KB\r\n
0xb0000446 | Request ERROR: Addr:%1 Idx:%2 Cnt:%3 - invalid transfer length %4 (alignment), supported is 8, 16, 32\r\n
0xb0000447 | Request INFO: Addr:%1 Idx:%2 Cnt:%3 - transfer delayed for %4 us\r\n
0xb0000448 | Request INFO: Addr:%1 Idx:%2 Cnt:%3 - delay timer expired - start transfer\r\n
0xb000044c | Interrupt ISR: Status:%1\r\n
0xb000044d | Interrupt DPC: HW_Status:%1 SW_Status:%2\r\n
0xb000044e | Interrupt DPC: Reenable HW interrupts with mask:%1\r\n
0xb0000493 | Target ERROR: Invalid connection properties length (current:%1, supported:%2)\r\n
0xb0000494 | Target ERROR: Invalid bus type (current:%1, supported:I2C)\r\n
0xb0000498 | Target ERROR: Invalid clock frequency (requested:%1)\r\n
0xb0000499 | Request WARNING: Cancel Timer Callback without valid Target - this happen when request was already cancelled\r\n
0xb000049a | Request WARNING: Cancel Timer Callback without valid Request - this happen when request was already cancelled\r\n
0xb000049b | Request INFO: Cancel Timer Callback with outstanding Request: SpbController:%1 SpbTarget:%2 SpbRequest:%3\r\n
0xb000049d | Request WARNING: Timer Callback without valid Target - this happen when request was already cancelled\r\n
0xb000049e | Request WARNING: Timer Callback without valid Request - this happen when request was already cancelled\r\n
0xb000049f | Request WARNING: DPC Callback without valid Target - this happen when request was already cancelled\r\n
0xb00004a0 | Request WARNING: DPC Callback without valid Request - this happen when request was already cancelled\r\n
0xb00004a1 | Request WARNING: Cancel Callback without valid Target - this happen when request was already cancelled\r\n
0xb00004a2 | Request WARNING: Cancel Callback without valid Request - this happen when request was already cancelled\r\n
0xb00004a3 | Request INFO: Cancel Callback with outstanding Request: SpbController:%1 SpbTarget:%2 SpbRequest:%3\r\n
0xb00004a4 | Request ERROR: Failed to configure controller for transfer - Status:%1\r\n
0xb00004a5 | Request ERROR: Other transfer requires 0us delays - Status:%1\r\n
0xb00004a6 | Request ERROR: Other transfer requires write then read sequence items - Status:%1\r\n
0xb00004a7 | Request ERROR: Other transfer requires 2 sequence items - Status:%1\r\n
0xb00004a8 | Request ERROR: Failed to enqueue Other request - Status:%1\r\n
0xb00004a9 | Request ERROR: Unsupported Other RequestType - Status:%1\r\n
0xb00004aa | Request ERROR: Unsupported Other IoControlCode - Status:%1\r\n
0xb00004ab | Request ERROR: Failed to capture Other TransferList - Status:%1\r\n
0xb00004ac | Request ERROR: Request failed to mark cancelable - Status:%1\r\n
0xb00004ad | Request ERROR: Request for SpbController:%1 SpbRequest:%2 Type:%3 failed and is finished synchronously - Status:%4\r\n
0xb00004ae | Request INFO: Request for SpbController:%2 SpbRequest:%3 complete with Length:%4 - Status:%5\r\n
0xb00004af | Request ERROR: Request for SpbController:%2 SpbRequest:%3 complete with Length:%4 - Status:%5\r\n
0xb00004b0 | Controller ERROR: Failing device !!!\r\n
0xb00004b1 | Controller ERROR: Invalid capability (Type:%1, Capability:%2)\r\n
0xb00004b2 | Controller INFO: Configured for LOCKed operation\r\n
0xb00004b3 | Controller INFO: Addr:%1 Idx:%2 Cnt:%3 - Configured for WRITE %4 bytes\r\n
0xb00004b4 | Controller INFO: Addr:%1 Idx:%2 Cnt:%3 - Configured for READ %4 bytes\r\n
0xb00004b5 | Controller ERROR: Addr:%1 Idx:%2 Cnt:%3 - Other transfer is not supported\r\n
0xb00004b6 | Controller INFO: Addr:%1 Idx:%2 Cnt:%3 - DMA Processing\r\n
0xb00004b7 | Controller INFO: Addr:%1 Idx:%2 Cnt:%3 - PIO Processing\r\n
0xb00004b8 | Controller ERROR: Addr:%1 Idx:%2 Cnt:%3 - I2C Bus busy on controler init start\r\n
0xb00004b9 | Controller ERROR: Addr:%1 Idx:%2 Cnt:%3 - Timeout disabling controller\r\n
0xb00004ba | Controller ERROR: Addr:%1 Idx:%2 Cnt:%3 - Timeout enabling controller\r\n
0xb00004bf | Controller ERROR: Addr:%1 Idx:%2 Cnt:%3 - Controller initialization failed - STATUS:%4\r\n
0xb00004c4 | Controller INFO: Addr:%1 Idx:%2 Cnt:%3 - Transfer ended with %4 bytes processed - STATUS:%5\r\n
0xb00004c9 | Controller INFO: Interrupt processing started: HW_Status:%1 SW_Status:%2\r\n
0xd0000001 | LPT-LP\r\n
0xd0000002 | WPT-LP\r\n
0xd0000003 | SPT-LP\r\n
0xd0000004 | SPT-H\r\n
0xd0000005 | NOT SET\r\n
0xd0000006 | A0\r\n
0xd0000007 | A1\r\n
0xd0000008 | B0\r\n
0xd0000009 | F0\r\n
0xd000000a | F1\r\n
0xd000000b | NOT SET\r\n
0xd000000c | 0\r\n
0xd000000d | 1\r\n
0xd000000e | 2\r\n
0xd000000f | 3\r\n
0xd0000010 | 4\r\n
0xd0000011 | 5\r\n
0xd0000012 | 6\r\n
0xd0000013 | NOT SET\r\n
0xd0000014 | ACPI\r\n
0xd0000015 | PCI\r\n
0xd0000016 | WdfPowerDeviceInvalid\r\n
0xd0000017 | WdfPowerDeviceD0\r\n
0xd0000018 | WdfPowerDeviceD1\r\n
0xd0000019 | WdfPowerDeviceD2\r\n
0xd000001a | WdfPowerDeviceD3\r\n
0xd000001b | WdfPowerDeviceD3Final\r\n
0xd000001c | WdfPowerDevicePrepareForHibernation\r\n
0xd000001d | OFF\r\n
0xd000001e | ON\r\n
0xd000001f | 7bit\r\n
0xd0000020 | 10bit\r\n
0xd0000021 | Undefined\r\n
0xd0000022 | READ\r\n
0xd0000023 | WRITE\r\n
0xd0000024 | Undefined\r\n
0xd0000025 | Read\r\n
0xd0000026 | Write\r\n
0xd0000027 | Sequence\r\n
0xd0000028 | LockController\r\n
0xd0000029 | UnlockController\r\n
0xd000002a | LockConnection\r\n
0xd000002b | UnlockConnection\r\n
0xd000002c | Other\r\n
0xd000002d | I2C\r\n
0xd000002e | SPI\r\n
0xd000002f | UART\r\n
0xd0000030 | I2C\r\n
0xd0000031 | UART\r\n
0xd0000032 | SPI\r\n
