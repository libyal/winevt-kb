## websocket.dll

Path: %SystemRoot%\system32\websocket.dll

### 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000001 | KW_ALL\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Parser\r\n
0x70000002 | Action queue\r\n
0x90000001 | Microsoft-Windows-Websocket-Protocol-Component\r\n
0xb0000001 | %1\r\n
0xb0000002 | Operation of '%2' type queued with ID '%1'.\r\n
0xb0000003 | Operation '%1' is executing action '%2'.\r\n
0xb0000004 | Operation '%1' finished.\r\n
0xd0000001 | The action context passed to WebSocketCompleteAction has an incorrect value.\r\n
0xd0000002 | Received '%1!x!' frame, but expected either a continuation or a control frame.\r\n
0xd0000003 | Received unexpected continuation frames.\r\n
0xd0000004 | Received a data frame '%1!x!', but channel is already closed.\r\n
0xd0000005 | Received close frame with invalid size.\r\n
0xd0000006 | Received control frame '%1!x!' with size '%2!d!' bytes. Maximum allowed size is 125 bytes.\r\n
0xd0000007 | Received fragmented control frame '%1!x!'.\r\n
0xd0000008 | Sending a data frame '%1!x!', but channel is already closed.\r\n
0xd0000009 | Sending close frame, but channel is already closed.\r\n
0xd000000a | Received close frame, but channel is already closed.\r\n
0xd000000b | Close reason has '%1!d!' bytes, but cannot be larger than 123 bytes.\r\n
0xd000000c | Unable to parse '%1!.*S!'. Unable to parse %2 at offset '%3!d!'\r\n
0xd000000d | Unable to parse '%1!.*S!'. Expected at most '%2!d!' elements.\r\n
0xd000000e | Unable to parse '%1!.*S!'. Expected ',' at offset '%2!d!'\r\n
0xd000000f | Unable to parse '%1!.*S!'. Expected more characters to parse.\r\n
0xd0000010 | Verification of 'Sec-WebSocket-Protocol' header failed.\r\n
0xd0000011 | Verification of 'Sec-WebSocket-Extensions' header failed.\r\n
0xd0000012 | Verification of 'Sec-WebSocket-Version' header failed.\r\n
0xd0000013 | Verification of 'Upgrade' header failed.\r\n
0xd0000014 | Verification of 'Connection' header failed.\r\n
0xd0000015 | Token 'Connection' is missing in 'Upgrade' header.\r\n
0xd0000016 | Token 'WebSocket' is missing in 'Connection' header.\r\n
0xd0000017 | Subprotocol is not supported.\r\n
0xd0000018 | Extension is not supported.\r\n
0xd0000019 | Element '%1!.*S!' found twice in a header.\r\n
0xd000001a | Element '%1!.*S!' was not found in a header.\r\n
0xd000001b | Value of 'Sec-WebSocket-Accept' header does not match. Expected '%2!.*S!' but received '%3!.*S!'.\r\n
0xd000001c | Invalid buffer type. The message was started with '%1!x!' and must be finished with '%2!x!' before any other message type can be sent.\r\n
0xd000001d | A frame with reserved bits/opcodes cannot be mapped to a known type.\r\n
0xd000001e | Mask bit is reserved and cannot be used.\r\n
0xd000001f | The reason string must be NULL and reason length must be zero.\r\n
0xd0000020 | Specified status code cannot be used.\r\n
0xd0000021 | If buffer is NULL the length must be 0.\r\n
0xd0000022 | The parameter passed is invalid.\r\n
0xd0000023 | The UTF-8 sequence in the text frame is invalid.\r\n
0xd0000024 | Frame from server cannot have mask bit set.\r\n
0xd0000025 | Frame's length field is formatted incorrectly.\r\n
0xd0000026 | The default keep-alive value registry key does not exist or is malformed. Using default value.\r\n
0xd0000027 | The default keep-alive value registry key is set to too small a value. Using lowest allowed value instead.\r\n
0xd0000028 | At least one header is expected.\r\n
0xd0000029 | Multiple instances of '%1!.*S!' header found but only one instance is allowed.\r\n
0xd000002a | Header '%1!.*S!' required but not found.\r\n
0xd000002b | The mask bit is cleared, but client to server communication requires it to be set.\r\n
0xd000002c | The mask bit is set, but server to client communication requires it to be cleared.\r\n
0xd000002d | Invalid value of WEB_SOCKET_BUFFER_TYPE enumeration.\r\n
0xd000002e | Receive\r\n
0xd000002f | Send\r\n
0xd0000030 | WEB_SOCKET_NO_ACTION\r\n
0xd0000031 | WEB_SOCKET_SEND_TO_NETWORK_ACTION\r\n
0xd0000032 | WEB_SOCKET_INDICATE_SEND_COMPLETE_ACTION\r\n
0xd0000033 | WEB_SOCKET_RECEIVE_FROM_NETWORK_ACTION\r\n
0xd0000034 | WEB_SOCKET_INDICATE_RECEIVE_COMPLETE_ACTION\r\n
0xd0000035 | token\r\n
0xd0000036 | extension\r\n
