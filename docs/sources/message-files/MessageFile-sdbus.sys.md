## sdbus.sys

Path: %SystemRoot%\system32\drivers\sdbus.sys

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x70000001 | Interrupt\r\n
0x70000002 | CallbackRoutine\r\n
0xb0000064 | Interrupt detected in ISR.%nSD Host Physical Address: %1%nEvents (masked): %2\r\n
0xb0000065 | Entering callback routine.%nSD Host Physical Address: %1\r\n
0xb0000066 | Exiting callback routine.%nSD Host Physical Address: %1\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x10000001 | Interrupt handling\r\n
0x10000002 | eMMC specific processing\r\n
0x10000003 | SDIO specific processing\r\n
0x10000004 | SD specific processing\r\n
0x10000005 | Sdbus P-state frequency scaling\r\n
0x10000006 | SD bus errors\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x70000001 | Interrupt\r\n
0x70000002 | Callback Routine\r\n
0x70000003 | Retune\r\n
0x70000004 |  Error\r\n
0x70000005 | HPI IO\r\n
0x70000006 | P-State Request\r\n
0x70000007 | P-State Completion\r\n
0x70000008 | Command Issued\r\n
0x70000009 | Command Completed\r\n
0x7000000a | HPI CMD Issued\r\n
0x7000000b | HPI CMD Accepted\r\n
0x7000000c | HPI Worker Process\r\n
0x7000000d | P-State Utilization\r\n
0xb0000064 | Interrupt detected in ISR.%nSD Host Physical Address: %1%nEvents (masked): %2\r\n
0xb0000065 | Entering callback routine.%nSD Host Physical Address: %1\r\n
0xb0000066 | Exiting callback routine.%nSD Host Physical Address: %1\r\n
0xb0000067 | Retuning Sequence detected.%nSD Host Physical Address: %1%nRetuning Count: %2\r\n
0xb0000068 | Error in bus transfer.%nSD Host Physical Address: %1%nError Code: %2%nError Count: %3\r\n
0xb0000069 | Hpi IO detected.%nSD Host Physical Address: %1%nHpi Count: %2\r\n
0xb000006a | P-State change requested.%nPoFx Device Handle: %1%nP-State Requested: %2%nP-State Request Count: %3\r\n
0xb000006b | P-State change requested.%nPoFx Device Handle: %1%nP-State Completed: %2%nP-State Completion Count: %3\r\n
0xb000006c | Command issued.%nSD Host Physical Address: %1%nCommand: %2%nArgument: %3%nSize: %4\r\n
0xb000006d | Command completed.%nSD Host Physical Address: %1%nCommand: %2%nArgument: %3%nSize: %4\r\n
0xb000006e | Hpi CMD sent to the hardware. IRP %1\r\n
0xb000006f | Hpi CMD was accepted by the hardware. IRP %1\r\n
0xb0000070 | Hpi CMD worker started. IRP %1\r\n
0xb0000071 | Hpi CMD worker exited. IRP %1 Reason: %2\r\n
0xb0000072 | P-State change requested.%nPoFx Device Handle: %1%nP-State Active Percentage: %2%nP-State Active Duration: %3%nP-State Sample Duration: %4%nP-State Current Frequency: %5%nP-State Requested Frequency: %6\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.14393.321, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.292, 10.0.18362.1, 10.0.18362.752, 10.0.19041.1, 10.0.19041.630, 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000001 | Interrupt handling\r\n
0x10000002 | eMMC specific processing\r\n
0x10000003 | SDIO specific processing\r\n
0x10000004 | SD specific processing\r\n
0x10000005 | Sdbus P-state frequency scaling\r\n
0x10000006 | SD bus errors\r\n
0x10000007 | SD bus DPC\r\n
0x10000008 | SD bus request\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x70000001 | Interrupt\r\n
0x70000002 | Callback Routine\r\n
0x70000003 | Retune\r\n
0x70000004 |  Error\r\n
0x70000005 | HPI IO\r\n
0x70000006 | P-State Request\r\n
0x70000007 | P-State Completion\r\n
0x70000008 | Command Issued\r\n
0x70000009 | Command Completed\r\n
0x7000000a | HPI CMD Issued\r\n
0x7000000b | HPI CMD Accepted\r\n
0x7000000c | HPI Worker Process\r\n
0x7000000d | P-State Utilization\r\n
0x7000000e | SdbusWorkerDpc\r\n
0x7000000f | SdbusRequest\r\n
0xb0000064 | Interrupt detected in ISR.%nSD Host Physical Address: %1%nEvents (masked): %2\r\n
0xb0000065 | Entering callback routine.%nSD Host Physical Address: %1\r\n
0xb0000066 | Exiting callback routine.%nSD Host Physical Address: %1\r\n
0xb0000067 | Retuning Sequence detected.%nSD Host Physical Address: %1%nRetuning Count: %2\r\n
0xb0000068 | Error in bus transfer.%nSD Host Physical Address: %1%nError Code: %2%nError Count: %3\r\n
0xb0000069 | Hpi IO detected.%nSD Host Physical Address: %1%nHpi Count: %2\r\n
0xb000006a | P-State change requested.%nPoFx Device Handle: %1%nP-State Requested: %2%nP-State Request Count: %3\r\n
0xb000006b | P-State change requested.%nPoFx Device Handle: %1%nP-State Completed: %2%nP-State Completion Count: %3\r\n
0xb000006c | Command issued.%nSD Host Physical Address: %1%nCommand: %2%nArgument: %3%nSize: %4\r\n
0xb000006d | Command completed.%nSD Host Physical Address: %1%nCommand: %2%nArgument: %3%nSize: %4\r\n
0xb000006e | Hpi CMD sent to the hardware. IRP %1\r\n
0xb000006f | Hpi CMD was accepted by the hardware. IRP %1\r\n
0xb0000070 | Hpi CMD worker started. IRP %1\r\n
0xb0000071 | Hpi CMD worker exited. IRP %1 Reason: %2\r\n
0xb0000072 | P-State change requested.%nPoFx Device Handle: %1%nP-State Active Percentage: %2%nP-State Active Duration: %3%nP-State Sample Duration: %4%nP-State Current Frequency: %5%nP-State Requested Frequency: %6\r\n
0xb0000073 | SdbusWorkerDpcEnter: SD Host Physical Address: %1 Irp: %2 Workpacket Function: %3 CurrentState: %4 FunctionPhase: %5\r\n
0xb0000074 | SdbusWorkerDpcExit: SD Host Physical Address: %1 Irp: %2 Workpacket Function: %3 CurrentState: %4 FunctionPhase: %5\r\n
0xb0000075 | SdbusRequestStart: SD Host Physical Address: %1 Irp: %2 Cmd: %3 Arg: %4 Status: %5\r\n
0xb0000076 | SdbusRequestComplete: SD Host Physical Address: %1 Irp: %2 Cmd: %3 Arg %4 Status %5\r\n
0xb0000077 | Scheduled callback routine.%nSD Host Physical Address: %1\r\n
0xb0000078 | Interrupt DPC scheduled.\r\n
0xb0000079 | Interrupt DPC entered.\r\n
0xb000007a | Interrupt DPC exited.\r\n
