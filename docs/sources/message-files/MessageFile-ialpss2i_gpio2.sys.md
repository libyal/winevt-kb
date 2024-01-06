## ialpss2i_gpio2.sys

Path: %SystemRoot%\system32\drivers\iaLPSS2i_GPIO2.sys

### 30.63.1610.8, 30.100.1633.3, 30.100.1724.1, 30.100.1816.3

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | iaLPSS_GPIO2 Driver routines\r\n
0x70000002 | iaLPSS_GPIO2 GpioCx DDI calls\r\n
0x70000003 | iaLPSS_GPIO2 Controller routines\r\n
0x70000004 | iaLPSS_GPIO2 GpioInt routines\r\n
0x70000005 | iaLPSS_GPIO2 GpioIo routines\r\n
0x90000001 | Intel-iaLPSS2-GPIO2\r\n
0x90000002 | iaLPSS_GPIO2 Debug channel\r\n
0x90000003 | iaLPSS_GPIO2 Performance channel\r\n
0xb00003e9 | ERROR: %1 - STATUS: %2\r\n
0xb00003ea | INFO: %1\r\n
0xb00003eb | [%1] -->\r\n
0xb00003ec | [%1] -&lt;--\r\n
0xb00003ed | [%1] -&lt;-- Status = %2\r\n
0xb00003f3 | DriverEntry Start\r\n
0xb00003f4 | DriverEntry End\r\n
0xb00003f5 | Driver ERROR: WdfDriverCreate() returned status:%1\r\n
0xb00003f6 | Driver ERROR: GPIO_CLX_RegisterClient() returned status:%1\r\n
0xb00003f7 | DriverUnload Start\r\n
0xb00003f8 | DriverUnload End\r\n
0xb00003f9 | Driver ERROR: GPIO_CLX_UnregisterClient() returned status:%1\r\n
0xb00003fa | Driver ERROR: CheckSupportedOs() returned status:%1\r\n
0xb00003fd | DeviceAdd Start\r\n
0xb00003fe | DeviceAdd End\r\n
0xb00003ff | Device ERROR: GPIO_CLX_ProcessAddDevicePreDeviceCreate() returned status:%1\r\n
0xb0000400 | Device ERROR: GPIO_CLX_ProcessAddDevicePostDeviceCreate() returned status:%1\r\n
0xb0000401 | Device ERROR: WdfDeviceCreate() returned status:%1\r\n
0xb0000402 | Device HW profile FOUND: Instance:%1 Version:%2 Revision:%3 Mode:%4\r\n
0xb0000403 | Device HW profile ERROR: Instance:%1 Version:%2 Revision:%3 Mode:%4\r\n
0xb0000407 | GpioCx DDI: %1\r\n
0xb0000408 | GpioCx DDI ERROR: Controller Context invalid\r\n
0xb0000409 | GpioCx DDI ERROR: Controller Object invalid\r\n
0xb000040a | GpioCx DDI ERROR: Controller Object allocate error\r\n
0xb000044d | ERROR: Invalid bank number: %1\r\n
0xb000044e | %1: ERROR: Invalid pin number: %2\r\n
0xb000044f | %1_%2: ERROR: Invalid pin ownership: %3\r\n
0xb0000450 | %1_%2: ERROR: Invalid pin mode: %3\r\n
0xb0000453 | PrepareController Start\r\n
0xb0000454 | PrepareController End\r\n
0xb0000455 | PrepareController ERROR: Can't allocate pin table\r\n
0xb0000456 | PrepareController ERROR: Can't initialize GPIO layout - STATUS:%1\r\n
0xb0000457 | PrepareController MBAR%1 mapped: PA:%2 LEN:%3 VA:%4\r\n
0xb0000458 | PrepareController ERROR: Too many MBAR resources IDX:%1 PA:%2 LEN:%3 - STATUS:%4\r\n
0xb0000459 | PrepareController ERROR: Can't map MMIO for MBAR%1 PA:%2 LEN:%3 - STATUS:%4\r\n
0xb000045a | PrepareController INTERRUPT VEC:%1\r\n
0xb000045b | PrepareController ERROR: Incorrect resource count. MMIO:%1 (exp. %2) INT:%3 (exp. %4) - STATUS:%5\r\n
0xb000045c | ReleaseController Start\r\n
0xb000045d | ReleaseController End\r\n
0xb000045e | Controller queried for properties\r\n
0xb000045f | Controller started\r\n
0xb0000460 | Controller stopped\r\n
0xb0000461 | %1_%2: ERROR: Interrupt configuration not supported: %3 %4\r\n
0xb0000462 | %1_%2: Interrupt configured to: %3 %4\r\n
0xb0000463 | %1_%2: WARNING: Pull configuration not supported: %3 - using default\r\n
0xb0000464 | %1_%2: Pull configured to: %3\r\n
0xb0000465 | %1_%2: Interrupt enabled\r\n
0xb0000466 | %1_%2: Interrupt disabled\r\n
0xb0000467 | %1: Interrupts mask set to:%2 (requested:%3, failed:%4)\r\n
0xb0000468 | %1_%2: Interrupt unmasked\r\n
0xb0000469 | %1: Interrupts queried active:%2 (raw:%3, mask:%4)\r\n
0xb000046a | %1: Interrupts queried enabled:%2\r\n
0xb000046b | %1: Interrupts status cleared with mask:%2 (requested:%3, failed:%4)\r\n
0xb000046c | %1_%2: ERROR: Pin already connected in mode %3\r\n
0xb000046d | %1_%2: ERROR: Pin not connected\r\n
0xb000046e | %1_%2: Pin output set %3\r\n
0xb000046f | %1_%2: Pin output pre-set %3\r\n
0xb0000470 | %1_%2: Pin input get %3\r\n
0xb0000471 | %1_%2: WARNING: Pin mode '%3' not supported. Buffer enable state not changed.\r\n
0xb0000472 | %1_%2: Pin connected in mode %3\r\n
0xb0000473 | %1_%2: ERROR: Pin connected in mode %3 while disconnect request for mode %4\r\n
0xb0000474 | %1_%2: Pin disconnected - output buffer disabled\r\n
0xb0000475 | %1_%2: Pin disconnected - output buffer left enabled\r\n
0xb0000476 | %1_%2: Pin disconnected - input buffer disabled\r\n
0xb0000477 | %1_%2: Pin disconnected - input buffer left enabled\r\n
0xb0000478 | %1_%2: WARNING: Pin mode '%3' not supported. Disconnecting input and output.\r\n
0xb000047e | %1_%2: Pin context restored\r\n
0xb000047f | %1: Bank context restored\r\n
0xb0000480 | %1_%2: Pin context saved\r\n
0xb0000481 | %1: Bank context saved\r\n
0xb00004b0 | ERROR: Invalid special function number\r\n
0xb00004b1 | %1_%2: Mask APIC interrupt\r\n
0xb00004b2 | %1_%2: Unmask APIC interrupt\r\n
0xb00004b3 | %1_%2: WriteGpioIo\r\n
0xb00004b4 | %1_%2: ReadGpioIo\r\n
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
0xd0000016 | ACPI\r\n
0xd0000017 | GPIO\r\n
0xd0000018 | GPIO\r\n
0xd0000019 | NATIVE_1\r\n
0xd000001a | NATIVE_2\r\n
0xd000001b | NATIVE_3\r\n
0xd000001c | Level\r\n
0xd000001d | Edge\r\n
0xd000001e | Unknown\r\n
0xd000001f | ActiveHigh/RisingEdge\r\n
0xd0000020 | ActiveLow/FallingEdge\r\n
0xd0000021 | ActiveBoth\r\n
0xd0000022 | ActiveBothTriggerHigh\r\n
0xd0000023 | Pull-Default\r\n
0xd0000024 | Pull-Up\r\n
0xd0000025 | Pull-Down\r\n
0xd0000026 | Pull-None\r\n
0xd0000027 | Unknown\r\n
0xd0000028 | Input\r\n
0xd0000029 | Output\r\n
