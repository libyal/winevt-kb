## nfccx.dll

Path: %SystemRoot%\system32\drivers\umdf\nfccx.dll

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x10000001 | Payload logging of different types of packets.\r\n
0x10000002 | NCI packet events.\r\n
0x10000003 | NFP interface events.\r\n
0x10000004 | Power interface events.\r\n
0x10000005 | RF interface events.\r\n
0x10000006 | General device events.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE\r\n
0x70000002 | IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE\r\n
0x70000003 | RF interface initialization.\r\n
0x70000004 | RF firmware download.\r\n
0x70000005 | RF NDEF tag read.\r\n
0x70000006 | RF NDEF tag write.\r\n
0x90000001 | Microsoft-Windows-NFC-ClassExtension\r\n
0x90000002 | Analytical\r\n
0xb0010001 | Write NCI packet payload (MessageType: %1, PacketBoundaryFlag: %2, Size: %3).\r\n
0xb0010002 | Received NCI packet payload (MessageType: %1, PacketBoundaryFlag: %2, Size: %3).\r\n
0xb0010003 | Write NCI packet (MessageType: %1, PacketBoundaryFlag: %2, Size: %3).\r\n
0xb0010004 | Received NCI packet (MessageType: %1, PacketBoundaryFlag: %2, Size: %3).\r\n
0xb0010065 | NFP client created (FileObject: %1, Role: %2).\r\n
0xb0010066 | NFP client destroyed (FileObject: %1, Role: %2).\r\n
0xb0010067 | NFP set payload (FileObject: %1, PayloadSize: %2).\r\n
0xb0010068 | NFP get next subscribed message start (FileObject: %1).\r\n
0xb0010069 | NFP get next subscribed message completed (FileObject: %1, Status: %2, Information: %3).\r\n
0xb001006a | NFP get next transmitted message start (FileObject: %1).\r\n
0xb001006b | NFP get next transmitted message completed (FileObject: %1, Status: %2).\r\n
0xb00100c9 | Power set radio state (RadioIsOn: %1).\r\n
0xb001012d | RF interface initialization started.\r\n
0xb001012e | RF interface initialization completed (Status: %1).\r\n
0xb001012f | RF firmware version is: %1.\r\n
0xb0010130 | RF firmware download started (File: %1, ForceDownload: %2).\r\n
0xb0010131 | RF firmware download completed (Status: %1).\r\n
0xb0010132 | RF event: %1.\r\n
0xb0010133 | RF NDEF tag read start.\r\n
0xb0010134 | RF NDEF tag read stop (Status: %1, Length: %2).\r\n
0xb0010135 | RF NDEF tag write start (Length: %1).\r\n
0xb0010136 | RF NDEF tag write stop (Status: %1).\r\n
0xb0010191 | Device registry settings.\r\n
0xb0010192 | Device persisted registry settings.\r\n
0xd0000001 | RoleConfiguration\r\n
0xd0000002 | RoleSubscription\r\n
0xd0000003 | RolePublication\r\n
0xd0000004 | RoleSmartCard\r\n
0xd0000005 | RoleSecureElementEvent\r\n
0xd0000006 | RoleSecureElementManager\r\n
0xd0000007 | TagArrival\r\n
0xd0000008 | TagWritableArrival\r\n
0xd0000009 | TagDeparture\r\n
0xd000000a | P2PArrival\r\n
0xd000000b | P2PDeparture\r\n
