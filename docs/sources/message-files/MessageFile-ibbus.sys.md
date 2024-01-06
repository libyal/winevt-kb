## ibbus.sys

Path: %SystemRoot%\System32\drivers\ibbus.sys

### 4.4.13905.0

Message identifier | Message string
--- | ---
0x40090001 | %2\r\n
0x80090002 | %2\r\n
0xc0090003 | %2\r\n
0xc0090004 | One of the Mellanox HCAs failed to start since the same GUID is burned on multiple HCAs. This issue occurred due to FW burning mistake. Currently the system has detected %2 duplicated GUIDs\r\nTo resolve the issue, please reburn one of the HCAs with another GUID.\r\nPlease use Mellanox Firmware Tools to detect the HCAs with the same GUID and burn the latest firmware. \r\nMellanox firmware tools and the latest firmware can be downloaded from : www.mellanox.com\r\n
0xc0090005 | Bus failed to initialize the Mellanox interface, this issue occured due to inappropriate card revision.%n\r\ncard revision=%2, please use newer driver that supports this card revision.%n\r\n

### 4.91.10730.0, 5.1.11548.0, 5.50.14643.0, 5.50.14695.0

Message identifier | Message string
--- | ---
0x40090001 | %2\r\n
0x80090002 | %2\r\n
0x80090006 | Some of the ports on the HCA with GUID %2 may not be functional since the same GUID is burned on multiple ports. This issue probably occurred due to FW burning mistake.\r\nTo resolve the issue, please reburn one of the ports with another GUID.\r\nFor information on how to change the GUID please consult the HCA vendor support.\r\n
0xc0090003 | %2\r\n
0xc0090004 | One of the HCAs failed to start since the same GUID is burned on multiple HCAs. This issue probably occurred due to FW burning mistake. Currently the system has detected %2 duplicated GUIDs\r\nTo resolve the issue, please reburn one of the HCAs with another GUID.\r\nFor information on how to change the GUID please consult the HCA vendor support.\r\n
0xc0090005 | Bus failed to initialize the Network interface, this issue occured due to inappropriate card revision.%n\r\ncard revision=%2, please use newer driver that supports this card revision.%n\r\n
0xc0090007 | GUID of port %2 is equal to zero, which is incorrect. The possible reason is absence of opensm.\r\nTo resolve the issue, please run opensm before starting this card.\r\n
