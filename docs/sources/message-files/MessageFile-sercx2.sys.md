## sercx2.sys

Path: %SystemRoot%\system32\drivers\SerCx2.sys

### 6.3.9600.16384, 6.3.9600.16444, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000002 | SerCx2 failed to load (%2).\r\n
0x10000001 | Rundown events that list all devices when the provider is enabled.\r\n
0x10000002 | Plug & Play events.\r\n
0x10000003 | TransferStateMachine events.\r\n
0x10000004 | Transmit TransferStateMachine events.\r\n
0x10000005 | Receive TransferStateMachine events.\r\n
0x10000006 | I/O request events.\r\n
0x10000007 | Transmit I/O request events.\r\n
0x10000008 | Receive I/O request events.\r\n
0x10000009 | I/O request payloads.\r\n
0x1000000a | Transmit I/O request payloads.\r\n
0x1000000b | Receive I/O request payloads.\r\n
0x1000000c | IOCTL request events.\r\n
0x1000000d | Power state transition events.\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3003000b | I/O StateMachine operation.\r\n
0x3003000c | I/O payload operation.\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Rundown events.\r\n
0x70000002 | IOCTL request.\r\n
0x70000003 | I/O request.\r\n
0x70000004 | Power state transitions.\r\n
0x90000001 | Microsoft-Windows-Serial-ClassExtension-V2\r\n
0x90000002 | System\r\n
0x90000003 | Analytic\r\n
0xb0010001 | SerCx2 loaded (%1).\r\n
0xb0010003 | SerCx2 unloading.\r\n
0xb0010004 | Starting rundown.\r\n
0xb0010005 | Device rundown (%1).\r\n
0xb0010006 | Rundown complete.\r\n
0xb0010007 | Device created (%1).\r\n
0xb0010008 | Device destroyed (%1).\r\n
0xb0010009 | TransmitSM (%1) Event: %2\r\n
0xb001000a | TransmitSM (%1) Transition: %2[%3] -> %4\r\n
0xb001000b | Invalid Transition TransmitSM (%1) Transition: %2[%3] -> %4\r\n
0xb001000c | ReceiveSM (%1) Event: %2\r\n
0xb001000d | ReceiveSM (%1) Transition: %2[%3] -> %4\r\n
0xb001000e | Invalid Transition ReceiveSM (%1) Transition: %2[%3] -> %4\r\n
0xb001000f | Processing %2.\r\n
0xb0010010 | Completed %2 with %3.\r\n
0xb0010011 | Transmit I/O request for %2 bytes started.\r\n
0xb0010012 | Transmit I/O request completed (%2).\r\n
0xb0010013 | Transmit I/O chunk of %3 bytes using %4.\r\n
0xb0010014 | Receive I/O request for %2 bytes started.\r\n
0xb0010015 | Receive I/O request completed (%2).\r\n
0xb0010016 | Receive I/O chunk of %3 bytes using %4.\r\n
0xb0010017 | Saved %2 bytes before exiting D0. Total %3 bytes.\r\n
0xb0010018 | Transitioning to system power state %2.\r\n
0xb0010019 | Transitioning to device power state %2.\r\n
0xb001001a | System power state transition %2 complete (%3).\r\n
0xb001001b | Device power state transition %2 complete (%3).\r\n
0xb001001c | Event %2.\r\n
0xd0000001 | Working\r\n
0xd0000002 | S1\r\n
0xd0000003 | S2\r\n
0xd0000004 | S3\r\n
0xd0000005 | Hibernate\r\n
0xd0000006 | Shutdown\r\n
0xd0000007 | D0\r\n
0xd0000008 | D1\r\n
0xd0000009 | D2\r\n
0xd000000a | D3\r\n
0xd000000b | EvtProgramDmaTransmit\r\n
0xd000000c | EvtProgramDmaReceive\r\n
0xd000000d | EvtDmaTransactionConfigureDmaChannelTransmit\r\n
0xd000000e | EvtDmaTransactionConfigureDmaChannelReceive\r\n
0xd000000f | IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION\r\n
0xd0000010 | IOCTL_SERIAL_CLEAR_STATS\r\n
0xd0000011 | IOCTL_SERIAL_CLR_DTR\r\n
0xd0000012 | IOCTL_SERIAL_CLR_RTS\r\n
0xd0000013 | IOCTL_SERIAL_CONFIG_SIZE\r\n
0xd0000014 | IOCTL_SERIAL_GET_BAUD_RATE\r\n
0xd0000015 | IOCTL_SERIAL_GET_CHARS\r\n
0xd0000016 | IOCTL_SERIAL_GET_COMMSTATUS\r\n
0xd0000017 | IOCTL_SERIAL_GET_DTRRTS\r\n
0xd0000018 | IOCTL_SERIAL_GET_HANDFLOW\r\n
0xd0000019 | IOCTL_SERIAL_GET_LINE_CONTROL\r\n
0xd000001a | IOCTL_SERIAL_GET_MODEMSTATUS\r\n
0xd000001b | IOCTL_SERIAL_GET_MODEM_CONTROL\r\n
0xd000001c | IOCTL_SERIAL_GET_PROPERTIES\r\n
0xd000001d | IOCTL_SERIAL_GET_STATS\r\n
0xd000001e | IOCTL_SERIAL_GET_TIMEOUTS\r\n
0xd000001f | IOCTL_SERIAL_GET_WAIT_MASK\r\n
0xd0000020 | IOCTL_SERIAL_IMMEDIATE_CHAR\r\n
0xd0000021 | IOCTL_SERIAL_LSRMST_INSERT\r\n
0xd0000022 | IOCTL_SERIAL_PURGE\r\n
0xd0000023 | IOCTL_SERIAL_RESET_DEVICE\r\n
0xd0000024 | IOCTL_SERIAL_SET_BAUD_RATE\r\n
0xd0000025 | IOCTL_SERIAL_SET_BREAK_OFF\r\n
0xd0000026 | IOCTL_SERIAL_SET_BREAK_ON\r\n
0xd0000027 | IOCTL_SERIAL_SET_CHARS\r\n
0xd0000028 | IOCTL_SERIAL_SET_DTR\r\n
0xd0000029 | IOCTL_SERIAL_SET_FIFO_CONTROL\r\n
0xd000002a | IOCTL_SERIAL_SET_HANDFLOW\r\n
0xd000002b | IOCTL_SERIAL_SET_LINE_CONTROL\r\n
0xd000002c | IOCTL_SERIAL_SET_MODEM_CONTROL\r\n
0xd000002d | IOCTL_SERIAL_SET_QUEUE_SIZE\r\n
0xd000002e | IOCTL_SERIAL_SET_RTS\r\n
0xd000002f | IOCTL_SERIAL_SET_TIMEOUTS\r\n
0xd0000030 | IOCTL_SERIAL_SET_WAIT_MASK\r\n
0xd0000031 | IOCTL_SERIAL_SET_XOFF\r\n
0xd0000032 | IOCTL_SERIAL_SET_XON\r\n
0xd0000033 | IOCTL_SERIAL_WAIT_ON_MASK\r\n
0xd0000034 | IOCTL_SERIAL_XOFF_COUNTER\r\n
