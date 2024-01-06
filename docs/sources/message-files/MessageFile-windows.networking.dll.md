## windows.networking.dll

Path: %SystemRoot%\system32\Windows.Networking.dll

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000002 | AsyncOperation\r\n
0x10000003 | Socket\r\n
0x10000004 | WebSocket\r\n
0x10000005 | Http\r\n
0x3000000a | API Enter\r\n
0x3000000b | API Exit\r\n
0x3000000c | Async operation start\r\n
0x3000000d | Async operation complete\r\n
0x3000000e | Async operation failure\r\n
0x3000000f | Async operation abort\r\n
0x30000010 | Async operation close\r\n
0x30000011 | Async operation completion\r\n
0x30000012 | Async operation progress\r\n
0x30000013 | HTTP operation\r\n
0x30000014 | Processing after read\r\n
0x30000015 | Start read\r\n
0x30000016 | Read complete\r\n
0x30000017 | Read error\r\n
0x30000018 | Start write\r\n
0x30000019 | Write complete\r\n
0x3000001a | State change\r\n
0x3000001b | I/O error\r\n
0x3000001c | TCP connected\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | APIs\r\n
0x70000002 | AsyncOperation\r\n
0x70000003 | EventNotification\r\n
0x70000004 | SocketConnect\r\n
0x70000005 | SocketAccept\r\n
0x70000006 | SocketSend\r\n
0x70000007 | SocketReceive\r\n
0x70000008 | SocketClose\r\n
0x70000009 | WebSocketConnect\r\n
0x7000000a | WebSocketSend\r\n
0x7000000b | WebSocketReceive\r\n
0x7000000c | WebSocketClose\r\n
0x7000000d | SslSocket\r\n
0x7000000e | SocketIO\r\n
0x90000001 | Microsoft-Windows-Runtime-Networking\r\n
0xb0000001 | %1 at %2 started.\r\n
0xb0000002 | %1 at %2 failed to start. The error code is %3: %4\r\n
0xb0000003 | %1 at %2 completed successfully.\r\n
0xb0000004 | %1 at %2 failed with error code %3: %4.\r\n
0xb0000005 | %1 at %2 was cancelled.\r\n
0xb0000006 | %1 at %2 was closed.\r\n
0xb0000007 | Failed to parse URI '%1'.\r\n
0xb0000008 | Failed to create URI with base URI '%1' and relative URI '%2'.\r\n
0xb0000009 | Add HTTP header '%1: %2'.\r\n
0xb000000a | Start connect request to '%1' with credential of '%2'.\r\n
0xb000000b | Start connect request to '%1' with default credential.\r\n
0xb000000c | Failed connect request to '%1' at port %2. The last error is %3: %4\r\n
0xb000000d | Opening request to '%1' to '%2' with flags %3.\r\n
0xb000000e | Failed open request to '%1'. The last error is %2: %3\r\n
0xb000000f | Request context %1 has request handle %2 to '%3'.\r\n
0xb0000010 | Set HTTP send and receive timeout to %2ms on request handle %1.\r\n
0xb0000011 | Start send to request handle %1 with content length %2.\r\n
0xb0000012 | Request handle %1 completed synchronously.\r\n
0xb0000013 | Request context %1 completed send asynchronously.\r\n
0xb0000014 | Writing %2 bytes to request handle %1.\r\n
0xb0000015 | Failed to send entity body to request handle %1. The last error is %2: %3\r\n
0xb0000016 | Sent HTTP request at request handle %1: %2\r\n
0xb0000017 | Start to receive response from request handle %1.\r\n
0xb0000018 | Received HTTP response from request handle %1 with status code %2 and status description '%3'.\r\n
0xb0000019 | Receive HTTP response from request handle %1: %2\r\n
0xb000001a | Failed to receive HTTP response from request handle %1. The last error is %2: %3\r\n
0xb000001b | Request context %1 received HTTP response of %2 bytes, which is over the %3 limit.\r\n
0xb000001c | Request context %1 resubmitting the request.\r\n
0xb000001d | Reusing the request handle %1 for server '%2'.\r\n
0xb000001e | Request context %1 was aborted.\r\n
0xb000001f | Progress to '%1': %2 bytes sent; %3 total bytes to send; %4 bytes received; %5 total bytes to receive.\r\n
0xb0000020 | HTTP request to '%1' completed. The error code is %2: %3\r\n
0xb0000021 | %1 at %2 failed to process HTTP response '%3'. The error code is %4: %5\r\n
0xb0000022 | %1::%2 is called.\r\n
0xb0000023 | %1::%2 returned successfully.\r\n
0xb0000024 | %1::%2 failed with HRESULT %3: %4\r\n
0xb0000025 | Win32 API %1 failed with error code %2: %3.\r\n
0xb0000026 | Unable to cancel GetAddrInfoEx with handle %1. The error code was %2: %3.\r\n
0xb0000027 | Unable to cancel DnsQueryEx with handle %1. The error code was %2: %3.\r\n
0xb0000028 | DatagramSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000029 | DatagramSocket %1 is raising event with %2 bytes received from sender '%4'.\r\n
0xb000002a | DatagramSocket %1 started receiving message at socket %2.\r\n
0xb000002b | DatagramSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb000002c | %1 at %2 is trying to receive %3 bytes at socket %4.\r\n
0xb000002d | %1 at %2 has received %3 bytes and continues to receive the remaining %4 bytes.\r\n
0xb000002e | %1 at %2 received %3 bytes.\r\n
0xb000002f | TCP socket %1 is connected: local port = %2; remote IP address: %3; remote port = %4.\r\n
0xb0000030 | UDP socket %1 is connected to remote address: %3.\r\n
0xb0000031 | The datagram received by socket %1 from sender '%3' does not contain IP packet information.\r\n
0xb0000032 | %1 at %2 sent %3 bytes.\r\n
0xb0000033 | %1 at %2 is trying to send %3 bytes at socket %4.\r\n
0xb0000034 | MessageWebSocket %1 received the close frame from the server.\r\n
0xb0000035 | MessageWebSocket %1 is raising event with %2 bytes received.\r\n
0xb0000036 | MessageWebSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb0000037 | MessageWebSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000039 | WebSocket %1 is sending the close frame.\r\n
0xb000003a | WebSocket %1 is receiving the close frame. Code: %2; Reason: %3\r\n
0xb000003b | WebSocket %1 I/O operation completed with error. The HRESULT was %2: %3.\r\n
0xb000003c | WebSocket %1 at %2 sent %3 bytes.\r\n
0xb000003d | WebSocket %1 at %2 is trying to send %3 bytes at WebSocket %4.\r\n
0xd0000001 | AcceptAsync\r\n
0xd0000002 | BindServiceNameAsync\r\n
0xd0000003 | ConnectAsync\r\n
0xd0000004 | ReadAsync\r\n
0xd0000005 | WriteAsync\r\n
0xd0000006 | JoinMulticastGroup\r\n
0xd0000007 | UpgradeToSslAsync\r\n
0xd0000008 | GetEndpointPairsAsync\r\n
0xd0000009 | GetOutputStreamAsync\r\n
0xd000000a | StreamSocket\r\n
0xd000000b | StreamSocketInputStream\r\n
0xd000000c | StreamSocketOutputStream\r\n
0xd000000d | DatagramSocket\r\n
0xd000000e | DatagramSocketOutputStream\r\n
0xd000000f | DatagramSocketWriteToOutputStream\r\n
0xd0000010 | MessageWebSocket\r\n
0xd0000011 | StreamWebSocket\r\n
0xd0000012 | StreamWebSocketInputStream\r\n
0xd0000013 | WebSocketOutputStream\r\n
0xd0000014 | StreamSocketListener\r\n
0xd0000015 | AcceptEx\r\n
0xd0000016 | connect\r\n
0xd0000017 | bind\r\n
0xd0000018 | listen\r\n
0xd0000019 | getpeername\r\n
0xd000001a | getsockname\r\n
0xd000001b | getsockopt\r\n
0xd000001c | setsockopt\r\n
0xd000001d | GetAddrInfoEx\r\n
0xd000001e | GetBestInferfaceEx\r\n
0xd000001f | WSAStartup\r\n
0xd0000020 | WSAConnectByName\r\n
0xd0000021 | WSAIoctl\r\n
0xd0000022 | WSARecv\r\n
0xd0000023 | WSARecvFrom\r\n
0xd0000024 | WSARecvMsg\r\n
0xd0000025 | WSASend\r\n
0xd0000026 | WSASendMsg\r\n
0xd0000027 | WSASocket\r\n
0xd0000028 | CreateThreadpoolIo\r\n
0xd0000029 | TrySubmitThreadpoolCallback\r\n
0xd000002a | HttpWebSocketCompleteUpgrade\r\n
0xd000002b | HttpWebSocketSend\r\n
0xd000002c | HttpWebSocketReceive\r\n
0xd000002d | InternetSetStatusCallback\r\n
0xd000002e | CancelIoEx\r\n
0xd000002f | DnsQueryEx\r\n
0xd0000030 | GetIfEntry2\r\n
0xd0000031 | GetPerTcpConnectionEStats\r\n
0xd0000032 | GetPerTcp6ConnectionEStats\r\n
0xd0000033 | GetTcpTable\r\n
0xd0000034 | GetTcp6Table\r\n
0xd0000035 | WlanOpenHandle\r\n
0xd0000036 | WlanSetInterface\r\n
0xd0000037 | WlanCloseHandle\r\n
0xd0000038 | GetAdaptersAddresses\r\n
0xd0000039 | ConnectOperation\r\n
0xd000003a | ReadOperation\r\n
0xd000003b | WriteOperation\r\n
0xd000003c | ListenOperation\r\n
0xd000003d | AcceptOperation\r\n
0xd000003e | UpgradeOperation\r\n
0xd000003f | GetEndpointPairsOperation\r\n
0xd0000040 | GetOutputStreamOperation\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000002 | AsyncOperation\r\n
0x10000003 | Socket\r\n
0x10000004 | WebSocket\r\n
0x10000005 | Http\r\n
0x10000006 | Rtc\r\n
0x30000000 | Info\r\n
0x3000000a | API Enter\r\n
0x3000000b | API Exit\r\n
0x3000000c | Async operation start\r\n
0x3000000d | Async operation complete\r\n
0x3000000e | Async operation failure\r\n
0x3000000f | Async operation abort\r\n
0x30000010 | Async operation close\r\n
0x30000011 | Async operation completion\r\n
0x30000012 | Async operation progress\r\n
0x30000013 | HTTP operation\r\n
0x30000014 | Processing after read\r\n
0x30000015 | Start read\r\n
0x30000016 | Read complete\r\n
0x30000017 | Read error\r\n
0x30000018 | Start write\r\n
0x30000019 | Write complete\r\n
0x3000001a | State change\r\n
0x3000001b | I/O error\r\n
0x3000001c | TCP connected\r\n
0x3000001d | RtcCompleteDelivery\r\n
0x3000001e | RtcFlush\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | APIs\r\n
0x70000002 | AsyncOperation\r\n
0x70000003 | EventNotification\r\n
0x70000004 | SocketConnect\r\n
0x70000005 | SocketAccept\r\n
0x70000006 | SocketSend\r\n
0x70000007 | SocketReceive\r\n
0x70000008 | SocketClose\r\n
0x70000009 | WebSocketConnect\r\n
0x7000000a | WebSocketSend\r\n
0x7000000b | WebSocketReceive\r\n
0x7000000c | WebSocketClose\r\n
0x7000000d | SslSocket\r\n
0x7000000e | SocketIO\r\n
0x90000001 | Microsoft-Windows-Runtime-Networking\r\n
0xb0000001 | %1 at %2 started.\r\n
0xb0000002 | %1 at %2 failed to start. The error code is %3: %4\r\n
0xb0000003 | %1 at %2 completed successfully.\r\n
0xb0000004 | %1 at %2 failed with error code %3: %4.\r\n
0xb0000005 | %1 at %2 was cancelled.\r\n
0xb0000006 | %1 at %2 was closed.\r\n
0xb0000007 | Failed to parse URI '%1'.\r\n
0xb0000008 | Failed to create URI with base URI '%1' and relative URI '%2'.\r\n
0xb0000009 | Add HTTP header '%1: %2'.\r\n
0xb000000a | Start connect request to '%1' with credential of '%2'.\r\n
0xb000000b | Start connect request to '%1' with default credential.\r\n
0xb000000c | Failed connect request to '%1' at port %2. The last error is %3: %4\r\n
0xb000000d | Opening request to '%1' to '%2' with flags %3.\r\n
0xb000000e | Failed open request to '%1'. The last error is %2: %3\r\n
0xb000000f | Request context %1 has request handle %2 to '%3'.\r\n
0xb0000010 | Set HTTP send and receive timeout to %2ms on request handle %1.\r\n
0xb0000011 | Start send to request handle %1 with content length %2.\r\n
0xb0000012 | Request handle %1 completed synchronously.\r\n
0xb0000013 | Request context %1 completed send asynchronously.\r\n
0xb0000014 | Writing %2 bytes to request handle %1.\r\n
0xb0000015 | Failed to send entity body to request handle %1. The last error is %2: %3\r\n
0xb0000016 | Sent HTTP request at request handle %1: %2\r\n
0xb0000017 | Start to receive response from request handle %1.\r\n
0xb0000018 | Received HTTP response from request handle %1 with status code %2 and status description '%3'.\r\n
0xb0000019 | Receive HTTP response from request handle %1: %2\r\n
0xb000001a | Failed to receive HTTP response from request handle %1. The last error is %2: %3\r\n
0xb000001b | Request context %1 received HTTP response of %2 bytes, which is over the %3 limit.\r\n
0xb000001c | Request context %1 resubmitting the request.\r\n
0xb000001d | Reusing the request handle %1 for server '%2'.\r\n
0xb000001e | Request context %1 was aborted.\r\n
0xb000001f | Progress to '%1': %2 bytes sent; %3 total bytes to send; %4 bytes received; %5 total bytes to receive.\r\n
0xb0000020 | HTTP request to '%1' completed. The error code is %2: %3\r\n
0xb0000021 | %1 at %2 failed to process HTTP response '%3'. The error code is %4: %5\r\n
0xb0000022 | %1::%2 is called.\r\n
0xb0000023 | %1::%2 returned successfully.\r\n
0xb0000024 | %1::%2 failed with HRESULT %3: %4\r\n
0xb0000025 | Win32 API %1 failed with error code %2: %3.\r\n
0xb0000026 | Unable to cancel GetAddrInfoEx with handle %1. The error code was %2: %3.\r\n
0xb0000027 | Unable to cancel DnsQueryEx with handle %1. The error code was %2: %3.\r\n
0xb0000028 | DatagramSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000029 | DatagramSocket %1 is raising event with %2 bytes received from sender '%4'.\r\n
0xb000002a | DatagramSocket %1 started receiving message at socket %2.\r\n
0xb000002b | DatagramSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb000002c | %1 at %2 is trying to receive %3 bytes at socket %4.\r\n
0xb000002d | %1 at %2 has received %3 bytes and continues to receive the remaining %4 bytes.\r\n
0xb000002e | %1 at %2 received %3 bytes.\r\n
0xb000002f | TCP socket %1 is connected: local port = %2; remote IP address: %3; remote port = %4.\r\n
0xb0000030 | UDP socket %1 is connected to remote address: %3.\r\n
0xb0000031 | The datagram received by socket %1 from sender '%3' does not contain IP packet information.\r\n
0xb0000032 | %1 at %2 sent %3 bytes.\r\n
0xb0000033 | %1 at %2 is trying to send %3 bytes at socket %4.\r\n
0xb0000034 | MessageWebSocket %1 received the close frame from the server.\r\n
0xb0000035 | MessageWebSocket %1 is raising event with %2 bytes received.\r\n
0xb0000036 | MessageWebSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb0000037 | MessageWebSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000039 | WebSocket %1 is sending the close frame.\r\n
0xb000003a | WebSocket %1 is receiving the close frame. Code: %2; Reason: %3\r\n
0xb000003b | WebSocket %1 I/O operation completed with error. The HRESULT was %2: %3.\r\n
0xb000003c | WebSocket %1 at %2 sent %3 bytes.\r\n
0xb000003d | WebSocket %1 at %2 is trying to send %3 bytes at WebSocket %4.\r\n
0xb000003e | %1 is already closed and CompleteDelivery is pending with: outstanding read operations: %2.\r\n
0xb000003f | %1.CompleteDelivery is pending with: outstanding read operations: %2, pending Winsock requests: %3, data available: %4.\r\n
0xb0000040 | %1.Flush is pending with: outstanding write operations: %2.\r\n
0xb0000041 | %1.CompleteDelivery is pending with: outstanding read operations: %2.\r\n
0xb0000042 | Socket connection established: %1.\r\n
0xb0000043 | Proxy lookup for socket connection to '%1' completed successfully: %2.\r\n
0xb0000044 | Proxy lookup for socket connection to '%1' completed with error %2: %3\r\n
0xb0000045 | Ignored server certificate error count: %1\r\n
0xb0000046 | Server certificate thumbprint: '%1', certificate error count: %3, contains fatal certificate errors: %2, intermediate certificate count: %5.\r\n
0xd0000001 | AcceptAsync\r\n
0xd0000002 | BindServiceNameAsync\r\n
0xd0000003 | ConnectAsync\r\n
0xd0000004 | ReadAsync\r\n
0xd0000005 | WriteAsync\r\n
0xd0000006 | JoinMulticastGroup\r\n
0xd0000007 | UpgradeToSslAsync\r\n
0xd0000008 | GetEndpointPairsAsync\r\n
0xd0000009 | GetOutputStreamAsync\r\n
0xd000000a | CompleteDelivery\r\n
0xd000000b | Flush\r\n
0xd000000c | StreamSocket\r\n
0xd000000d | StreamSocketInputStream\r\n
0xd000000e | StreamSocketOutputStream\r\n
0xd000000f | DatagramSocket\r\n
0xd0000010 | DatagramSocketOutputStream\r\n
0xd0000011 | DatagramSocketWriteToOutputStream\r\n
0xd0000012 | MessageWebSocket\r\n
0xd0000013 | StreamWebSocket\r\n
0xd0000014 | StreamWebSocketInputStream\r\n
0xd0000015 | WebSocketOutputStream\r\n
0xd0000016 | StreamSocketListener\r\n
0xd0000017 | DatagramSocketInputStream\r\n
0xd0000018 | AcceptEx\r\n
0xd0000019 | connect\r\n
0xd000001a | bind\r\n
0xd000001b | listen\r\n
0xd000001c | getpeername\r\n
0xd000001d | getsockname\r\n
0xd000001e | getsockopt\r\n
0xd000001f | setsockopt\r\n
0xd0000020 | GetAddrInfoEx\r\n
0xd0000021 | GetBestInferfaceEx\r\n
0xd0000022 | WSAStartup\r\n
0xd0000023 | WSAConnectByName\r\n
0xd0000024 | WSAIoctl\r\n
0xd0000025 | WSARecv\r\n
0xd0000026 | WSARecvFrom\r\n
0xd0000027 | WSARecvMsg\r\n
0xd0000028 | WSASend\r\n
0xd0000029 | WSASendMsg\r\n
0xd000002a | WSASocket\r\n
0xd000002b | CreateThreadpoolIo\r\n
0xd000002c | TrySubmitThreadpoolCallback\r\n
0xd000002d | HttpWebSocketCompleteUpgrade\r\n
0xd000002e | HttpWebSocketSend\r\n
0xd000002f | HttpWebSocketReceive\r\n
0xd0000030 | InternetSetStatusCallback\r\n
0xd0000031 | CancelIoEx\r\n
0xd0000032 | DnsQueryEx\r\n
0xd0000033 | GetIfEntry2\r\n
0xd0000034 | GetPerTcpConnectionEStats\r\n
0xd0000035 | GetPerTcp6ConnectionEStats\r\n
0xd0000036 | GetTcpTable\r\n
0xd0000037 | GetTcp6Table\r\n
0xd0000038 | WlanOpenHandle\r\n
0xd0000039 | WlanSetInterface\r\n
0xd000003a | WlanCloseHandle\r\n
0xd000003b | GetAdaptersAddresses\r\n
0xd000003c | ConnectOperation\r\n
0xd000003d | ReadOperation\r\n
0xd000003e | WriteOperation\r\n
0xd000003f | ListenOperation\r\n
0xd0000040 | AcceptOperation\r\n
0xd0000041 | UpgradeOperation\r\n
0xd0000042 | GetEndpointPairsOperation\r\n
0xd0000043 | GetOutputStreamOperation\r\n
0xd0000044 | Direct\r\n
0xd0000045 | Proxy\r\n
0xd0000046 | Direct connection available\r\n
0xd0000047 | Proxy connection required\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000002 | AsyncOperation\r\n
0x10000003 | Socket\r\n
0x10000004 | WebSocket\r\n
0x10000005 | Http\r\n
0x10000006 | Rtc\r\n
0x30000000 | Info\r\n
0x3000000a | API Enter\r\n
0x3000000b | API Exit\r\n
0x3000000c | Async operation start\r\n
0x3000000d | Async operation complete\r\n
0x3000000e | Async operation failure\r\n
0x3000000f | Async operation abort\r\n
0x30000010 | Async operation close\r\n
0x30000011 | Async operation completion\r\n
0x30000012 | Async operation progress\r\n
0x30000013 | HTTP operation\r\n
0x30000014 | Processing after read\r\n
0x30000015 | Start read\r\n
0x30000016 | Read complete\r\n
0x30000017 | Read error\r\n
0x30000018 | Start write\r\n
0x30000019 | Write complete\r\n
0x3000001a | State change\r\n
0x3000001b | I/O error\r\n
0x3000001c | TCP connected\r\n
0x3000001d | RtcCompleteDelivery\r\n
0x3000001e | RtcFlush\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | APIs\r\n
0x70000002 | AsyncOperation\r\n
0x70000003 | EventNotification\r\n
0x70000004 | SocketConnect\r\n
0x70000005 | SocketAccept\r\n
0x70000006 | SocketSend\r\n
0x70000007 | SocketReceive\r\n
0x70000008 | SocketClose\r\n
0x70000009 | WebSocketConnect\r\n
0x7000000a | WebSocketSend\r\n
0x7000000b | WebSocketReceive\r\n
0x7000000c | WebSocketClose\r\n
0x7000000d | SslSocket\r\n
0x7000000e | SocketIO\r\n
0x90000001 | Microsoft-Windows-Runtime-Networking\r\n
0xb0000001 | %1 at %2 started.\r\n
0xb0000002 | %1 at %2 failed to start. The error code is %3: %4\r\n
0xb0000003 | %1 at %2 completed successfully.\r\n
0xb0000004 | %1 at %2 failed with error code %3: %4.\r\n
0xb0000005 | %1 at %2 was cancelled.\r\n
0xb0000006 | %1 at %2 was closed.\r\n
0xb0000007 | Failed to parse URI '%1'.\r\n
0xb0000008 | Failed to create URI with base URI '%1' and relative URI '%2'.\r\n
0xb0000009 | Add HTTP header '%1: %2'.\r\n
0xb000000a | Start connect request to '%1' with credential of '%2'.\r\n
0xb000000b | Start connect request to '%1' with default credential.\r\n
0xb000000c | Failed connect request to '%1' at port %2. The last error is %3: %4\r\n
0xb000000d | Opening request to '%1' to '%2' with flags %3.\r\n
0xb000000e | Failed open request to '%1'. The last error is %2: %3\r\n
0xb000000f | Request context %1 has request handle %2 to '%3'.\r\n
0xb0000010 | Set HTTP send and receive timeout to %2ms on request handle %1.\r\n
0xb0000011 | Start send to request handle %1 with content length %2.\r\n
0xb0000012 | Request handle %1 completed synchronously.\r\n
0xb0000013 | Request context %1 completed send asynchronously.\r\n
0xb0000014 | Writing %2 bytes to request handle %1.\r\n
0xb0000015 | Failed to send entity body to request handle %1. The last error is %2: %3\r\n
0xb0000016 | Sent HTTP request at request handle %1: %2\r\n
0xb0000017 | Start to receive response from request handle %1.\r\n
0xb0000018 | Received HTTP response from request handle %1 with status code %2 and status description '%3'.\r\n
0xb0000019 | Receive HTTP response from request handle %1: %2\r\n
0xb000001a | Failed to receive HTTP response from request handle %1. The last error is %2: %3\r\n
0xb000001b | Request context %1 received HTTP response of %2 bytes, which is over the %3 limit.\r\n
0xb000001c | Request context %1 resubmitting the request.\r\n
0xb000001d | Reusing the request handle %1 for server '%2'.\r\n
0xb000001e | Request context %1 was aborted.\r\n
0xb000001f | Progress to '%1': %2 bytes sent; %3 total bytes to send; %4 bytes received; %5 total bytes to receive.\r\n
0xb0000020 | HTTP request to '%1' completed. The error code is %2: %3\r\n
0xb0000021 | %1 at %2 failed to process HTTP response '%3'. The error code is %4: %5\r\n
0xb0000022 | %1::%2 is called.\r\n
0xb0000023 | %1::%2 returned successfully.\r\n
0xb0000024 | %1::%2 failed with HRESULT %3: %4\r\n
0xb0000025 | Win32 API %1 failed with error code %2: %3.\r\n
0xb0000026 | Unable to cancel GetAddrInfoEx with handle %1. The error code was %2: %3.\r\n
0xb0000027 | Unable to cancel DnsQueryEx with handle %1. The error code was %2: %3.\r\n
0xb0000028 | DatagramSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000029 | DatagramSocket %1 is raising event with %2 bytes received from sender '%4'.\r\n
0xb000002a | DatagramSocket %1 started receiving message at socket %2.\r\n
0xb000002b | DatagramSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb000002c | %1 at %2 is trying to receive %3 bytes at socket %4.\r\n
0xb000002d | %1 at %2 has received %3 bytes and continues to receive the remaining %4 bytes.\r\n
0xb000002e | %1 at %2 received %3 bytes.\r\n
0xb000002f | TCP socket %1 is connected: local port = %2; remote IP address: %3; remote port = %4.\r\n
0xb0000030 | UDP socket %1 is connected to remote address: %3.\r\n
0xb0000031 | The datagram received by socket %1 from sender '%3' does not contain IP packet information.\r\n
0xb0000032 | %1 at %2 sent %3 bytes.\r\n
0xb0000033 | %1 at %2 is trying to send %3 bytes at socket %4.\r\n
0xb0000034 | MessageWebSocket %1 received the close frame from the server.\r\n
0xb0000035 | MessageWebSocket %1 is raising event with %2 bytes received.\r\n
0xb0000036 | MessageWebSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb0000037 | MessageWebSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000039 | WebSocket %1 is sending the close frame.\r\n
0xb000003a | WebSocket %1 is receiving the close frame. Code: %2; Reason: %3\r\n
0xb000003b | WebSocket %1 I/O operation completed with error. The HRESULT was %2: %3.\r\n
0xb000003c | WebSocket %1 at %2 sent %3 bytes.\r\n
0xb000003d | WebSocket %1 at %2 is trying to send %3 bytes at WebSocket %4.\r\n
0xb000003e | %1 is already closed and CompleteDelivery is pending with: outstanding read operations: %2.\r\n
0xb000003f | %1.CompleteDelivery is pending with: outstanding read operations: %2, pending Winsock requests: %3, data available: %4.\r\n
0xb0000040 | %1.Flush is pending with: outstanding write operations: %2.\r\n
0xb0000041 | %1.CompleteDelivery is pending with: outstanding read operations: %2.\r\n
0xb0000042 | Socket connection established: %1.\r\n
0xb0000043 | Proxy lookup for socket connection to '%1' completed successfully: %2.\r\n
0xb0000044 | Proxy lookup for socket connection to '%1' completed with error %2: %3\r\n
0xb0000045 | Ignored server certificate error count: %1\r\n
0xb0000046 | Server certificate thumbprint: '%1', certificate error count: %3, contains fatal certificate errors: %2, intermediate certificate count: %5.\r\n
0xb0000047 | Failed to flush reads and wait for pending I/O to complete with context %1. Error was %2: %3.\r\n
0xb0000048 | Handle %1: HTTP/2 enabled.\r\n
0xb0000049 | %1 - Line: %2 Status: %3\r\n
0xd0000001 | AcceptAsync\r\n
0xd0000002 | BindServiceNameAsync\r\n
0xd0000003 | ConnectAsync\r\n
0xd0000004 | ReadAsync\r\n
0xd0000005 | WriteAsync\r\n
0xd0000006 | JoinMulticastGroup\r\n
0xd0000007 | UpgradeToSslAsync\r\n
0xd0000008 | GetEndpointPairsAsync\r\n
0xd0000009 | GetOutputStreamAsync\r\n
0xd000000a | CompleteDelivery\r\n
0xd000000b | Flush\r\n
0xd000000c | StreamSocket\r\n
0xd000000d | StreamSocketInputStream\r\n
0xd000000e | StreamSocketOutputStream\r\n
0xd000000f | DatagramSocket\r\n
0xd0000010 | DatagramSocketOutputStream\r\n
0xd0000011 | DatagramSocketWriteToOutputStream\r\n
0xd0000012 | MessageWebSocket\r\n
0xd0000013 | StreamWebSocket\r\n
0xd0000014 | StreamWebSocketInputStream\r\n
0xd0000015 | WebSocketOutputStream\r\n
0xd0000016 | StreamSocketListener\r\n
0xd0000017 | DatagramSocketInputStream\r\n
0xd0000018 | AcceptEx\r\n
0xd0000019 | connect\r\n
0xd000001a | bind\r\n
0xd000001b | listen\r\n
0xd000001c | getpeername\r\n
0xd000001d | getsockname\r\n
0xd000001e | getsockopt\r\n
0xd000001f | setsockopt\r\n
0xd0000020 | GetAddrInfoEx\r\n
0xd0000021 | GetBestInferfaceEx\r\n
0xd0000022 | WSAStartup\r\n
0xd0000023 | WSAConnectByName\r\n
0xd0000024 | WSAIoctl\r\n
0xd0000025 | WSARecv\r\n
0xd0000026 | WSARecvFrom\r\n
0xd0000027 | WSARecvMsg\r\n
0xd0000028 | WSASend\r\n
0xd0000029 | WSASendMsg\r\n
0xd000002a | WSASocket\r\n
0xd000002b | CreateThreadpoolIo\r\n
0xd000002c | TrySubmitThreadpoolCallback\r\n
0xd000002d | HttpWebSocketCompleteUpgrade\r\n
0xd000002e | HttpWebSocketSend\r\n
0xd000002f | HttpWebSocketReceive\r\n
0xd0000030 | InternetSetStatusCallback\r\n
0xd0000031 | CancelIoEx\r\n
0xd0000032 | DnsQueryEx\r\n
0xd0000033 | GetIfEntry2\r\n
0xd0000034 | GetPerTcpConnectionEStats\r\n
0xd0000035 | GetPerTcp6ConnectionEStats\r\n
0xd0000036 | GetTcpTable\r\n
0xd0000037 | GetTcp6Table\r\n
0xd0000038 | WlanOpenHandle\r\n
0xd0000039 | WlanSetInterface\r\n
0xd000003a | WlanCloseHandle\r\n
0xd000003b | GetAdaptersAddresses\r\n
0xd000003c | ConnectOperation\r\n
0xd000003d | ReadOperation\r\n
0xd000003e | WriteOperation\r\n
0xd000003f | ListenOperation\r\n
0xd0000040 | AcceptOperation\r\n
0xd0000041 | UpgradeOperation\r\n
0xd0000042 | GetEndpointPairsOperation\r\n
0xd0000043 | GetOutputStreamOperation\r\n
0xd0000044 | Direct\r\n
0xd0000045 | Proxy\r\n
0xd0000046 | Direct connection available\r\n
0xd0000047 | Proxy connection required\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000002 | AsyncOperation\r\n
0x10000003 | Socket\r\n
0x10000004 | WebSocket\r\n
0x10000005 | Http\r\n
0x10000006 | Rtc\r\n
0x30000000 | Info\r\n
0x3000000a | API Enter\r\n
0x3000000b | API Exit\r\n
0x3000000c | Async operation start\r\n
0x3000000d | Async operation complete\r\n
0x3000000e | Async operation failure\r\n
0x3000000f | Async operation abort\r\n
0x30000010 | Async operation close\r\n
0x30000011 | Async operation completion\r\n
0x30000012 | Async operation progress\r\n
0x30000013 | HTTP operation\r\n
0x30000014 | Processing after read\r\n
0x30000015 | Start read\r\n
0x30000016 | Read complete\r\n
0x30000017 | Read error\r\n
0x30000018 | Start write\r\n
0x30000019 | Write complete\r\n
0x3000001a | State change\r\n
0x3000001b | I/O error\r\n
0x3000001c | TCP connected\r\n
0x3000001d | RtcCompleteDelivery\r\n
0x3000001e | RtcFlush\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | APIs\r\n
0x70000002 | AsyncOperation\r\n
0x70000003 | EventNotification\r\n
0x70000004 | SocketConnect\r\n
0x70000005 | SocketAccept\r\n
0x70000006 | SocketSend\r\n
0x70000007 | SocketReceive\r\n
0x70000008 | SocketClose\r\n
0x70000009 | WebSocketConnect\r\n
0x7000000a | WebSocketSend\r\n
0x7000000b | WebSocketReceive\r\n
0x7000000c | WebSocketClose\r\n
0x7000000d | SslSocket\r\n
0x7000000e | SocketIO\r\n
0x90000001 | Microsoft-Windows-Runtime-Networking\r\n
0xb0000001 | %1 at %2 started.\r\n
0xb0000002 | %1 at %2 failed to start. The error code is %3: %4\r\n
0xb0000003 | %1 at %2 completed successfully.\r\n
0xb0000004 | %1 at %2 failed with error code %3: %4.\r\n
0xb0000005 | %1 at %2 was cancelled.\r\n
0xb0000006 | %1 at %2 was closed.\r\n
0xb0000007 | Failed to parse URI '%1'.\r\n
0xb0000008 | Failed to create URI with base URI '%1' and relative URI '%2'.\r\n
0xb0000009 | Add HTTP header '%1: %2'.\r\n
0xb000000a | Start connect request to '%1' with credential of '%2'.\r\n
0xb000000b | Start connect request to '%1' with default credential.\r\n
0xb000000c | Failed connect request to '%1' at port %2. The last error is %3: %4\r\n
0xb000000d | Opening request to '%1' to '%2' with flags %3.\r\n
0xb000000e | Failed open request to '%1'. The last error is %2: %3\r\n
0xb000000f | Request context %1 has request handle %2 to '%3'.\r\n
0xb0000010 | Set HTTP send and receive timeout to %2ms on request handle %1.\r\n
0xb0000011 | Start send to request handle %1 with content length %2.\r\n
0xb0000012 | Request handle %1 completed synchronously.\r\n
0xb0000013 | Request context %1 completed send asynchronously.\r\n
0xb0000014 | Writing %2 bytes to request handle %1.\r\n
0xb0000015 | Failed to send entity body to request handle %1. The last error is %2: %3\r\n
0xb0000016 | Sent HTTP request at request handle %1: %2\r\n
0xb0000017 | Start to receive response from request handle %1.\r\n
0xb0000018 | Received HTTP response from request handle %1 with status code %2 and status description '%3'.\r\n
0xb0000019 | Receive HTTP response from request handle %1: %2\r\n
0xb000001a | Failed to receive HTTP response from request handle %1. The last error is %2: %3\r\n
0xb000001b | Request context %1 received HTTP response of %2 bytes, which is over the %3 limit.\r\n
0xb000001c | Request context %1 resubmitting the request.\r\n
0xb000001d | Reusing the request handle %1 for server '%2'.\r\n
0xb000001e | Request context %1 was aborted.\r\n
0xb000001f | Progress to '%1': %2 bytes sent; %3 total bytes to send; %4 bytes received; %5 total bytes to receive.\r\n
0xb0000020 | HTTP request to '%1' completed. The error code is %2: %3\r\n
0xb0000021 | %1 at %2 failed to process HTTP response '%3'. The error code is %4: %5\r\n
0xb0000022 | %1::%2 is called.\r\n
0xb0000023 | %1::%2 returned successfully.\r\n
0xb0000024 | %1::%2 failed with HRESULT %3: %4\r\n
0xb0000025 | Win32 API %1 failed with error code %2: %3.\r\n
0xb0000026 | Unable to cancel GetAddrInfoEx with handle %1. The error code was %2: %3.\r\n
0xb0000027 | Unable to cancel DnsQueryEx with handle %1. The error code was %2: %3.\r\n
0xb0000028 | DatagramSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000029 | DatagramSocket %1 is raising event with %2 bytes received from sender '%4'.\r\n
0xb000002a | DatagramSocket %1 started receiving message at socket %2.\r\n
0xb000002b | DatagramSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb000002c | %1 at %2 is trying to receive %3 bytes at socket %4.\r\n
0xb000002d | %1 at %2 has received %3 bytes and continues to receive the remaining %4 bytes.\r\n
0xb000002e | %1 at %2 received %3 bytes.\r\n
0xb000002f | TCP socket %1 is connected: local port = %2; remote IP address: %3; remote port = %4.\r\n
0xb0000030 | UDP socket %1 is connected to remote address: %3.\r\n
0xb0000031 | The datagram received by socket %1 from sender '%3' does not contain IP packet information.\r\n
0xb0000032 | %1 at %2 sent %3 bytes.\r\n
0xb0000033 | %1 at %2 is trying to send %3 bytes at socket %4.\r\n
0xb0000034 | MessageWebSocket %1 received the close frame from the server.\r\n
0xb0000035 | MessageWebSocket %1 is raising event with %2 bytes received.\r\n
0xb0000036 | MessageWebSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb0000037 | MessageWebSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000039 | WebSocket %1 is sending the close frame.\r\n
0xb000003a | WebSocket %1 is receiving the close frame. Code: %2; Reason: %3\r\n
0xb000003b | WebSocket %1 I/O operation completed with error. The HRESULT was %2: %3.\r\n
0xb000003c | WebSocket %1 at %2 sent %3 bytes.\r\n
0xb000003d | WebSocket %1 at %2 is trying to send %3 bytes at WebSocket %4.\r\n
0xb000003e | %1 is already closed and CompleteDelivery is pending with: outstanding read operations: %2.\r\n
0xb000003f | %1.CompleteDelivery is pending with: outstanding read operations: %2, pending Winsock requests: %3, data available: %4.\r\n
0xb0000040 | %1.Flush is pending with: outstanding write operations: %2.\r\n
0xb0000041 | %1.CompleteDelivery is pending with: outstanding read operations: %2.\r\n
0xb0000042 | Socket connection established: %1.\r\n
0xb0000043 | Proxy lookup for socket connection to '%1' completed successfully: %2.\r\n
0xb0000044 | Proxy lookup for socket connection to '%1' completed with error %2: %3\r\n
0xb0000045 | Ignored server certificate error count: %1\r\n
0xb0000046 | Server certificate thumbprint: '%1', certificate error count: %3, contains fatal certificate errors: %2, intermediate certificate count: %5.\r\n
0xb0000047 | Failed to flush reads and wait for pending I/O to complete with context %1. Error was %2: %3.\r\n
0xb0000048 | Handle %1: HTTP/2 enabled.\r\n
0xb0000049 | %1 - Line: %2 Status: %3\r\n
0xb000004a | Async operation %1 at %2 started server custom validation.\r\n
0xb000004b | Async operation %1 at %2 waiting for completion of server custom validation.\r\n
0xb000004c | Async operation %1 at %2 failed server custom validation.\r\n
0xb000004d | Async operation %1 at %2 successfully completed server custom validation.\r\n
0xd0000001 | AcceptAsync\r\n
0xd0000002 | BindServiceNameAsync\r\n
0xd0000003 | ConnectAsync\r\n
0xd0000004 | ReadAsync\r\n
0xd0000005 | WriteAsync\r\n
0xd0000006 | JoinMulticastGroup\r\n
0xd0000007 | UpgradeToSslAsync\r\n
0xd0000008 | GetEndpointPairsAsync\r\n
0xd0000009 | GetOutputStreamAsync\r\n
0xd000000a | CompleteDelivery\r\n
0xd000000b | Flush\r\n
0xd000000c | StreamSocket\r\n
0xd000000d | StreamSocketInputStream\r\n
0xd000000e | StreamSocketOutputStream\r\n
0xd000000f | DatagramSocket\r\n
0xd0000010 | DatagramSocketOutputStream\r\n
0xd0000011 | DatagramSocketWriteToOutputStream\r\n
0xd0000012 | MessageWebSocket\r\n
0xd0000013 | StreamWebSocket\r\n
0xd0000014 | StreamWebSocketInputStream\r\n
0xd0000015 | WebSocketOutputStream\r\n
0xd0000016 | StreamSocketListener\r\n
0xd0000017 | DatagramSocketInputStream\r\n
0xd0000018 | AcceptEx\r\n
0xd0000019 | connect\r\n
0xd000001a | bind\r\n
0xd000001b | listen\r\n
0xd000001c | getpeername\r\n
0xd000001d | getsockname\r\n
0xd000001e | getsockopt\r\n
0xd000001f | setsockopt\r\n
0xd0000020 | GetAddrInfoEx\r\n
0xd0000021 | GetBestInferfaceEx\r\n
0xd0000022 | WSAStartup\r\n
0xd0000023 | WSAConnectByName\r\n
0xd0000024 | WSAIoctl\r\n
0xd0000025 | WSARecv\r\n
0xd0000026 | WSARecvFrom\r\n
0xd0000027 | WSARecvMsg\r\n
0xd0000028 | WSASend\r\n
0xd0000029 | WSASendMsg\r\n
0xd000002a | WSASocket\r\n
0xd000002b | CreateThreadpoolIo\r\n
0xd000002c | TrySubmitThreadpoolCallback\r\n
0xd000002d | HttpWebSocketCompleteUpgrade\r\n
0xd000002e | HttpWebSocketSend\r\n
0xd000002f | HttpWebSocketReceive\r\n
0xd0000030 | InternetSetStatusCallback\r\n
0xd0000031 | CancelIoEx\r\n
0xd0000032 | DnsQueryEx\r\n
0xd0000033 | GetIfEntry2\r\n
0xd0000034 | GetPerTcpConnectionEStats\r\n
0xd0000035 | GetPerTcp6ConnectionEStats\r\n
0xd0000036 | GetTcpTable\r\n
0xd0000037 | GetTcp6Table\r\n
0xd0000038 | WlanOpenHandle\r\n
0xd0000039 | WlanSetInterface\r\n
0xd000003a | WlanCloseHandle\r\n
0xd000003b | GetAdaptersAddresses\r\n
0xd000003c | ConnectOperation\r\n
0xd000003d | ReadOperation\r\n
0xd000003e | WriteOperation\r\n
0xd000003f | ListenOperation\r\n
0xd0000040 | AcceptOperation\r\n
0xd0000041 | UpgradeOperation\r\n
0xd0000042 | GetEndpointPairsOperation\r\n
0xd0000043 | GetOutputStreamOperation\r\n
0xd0000044 | Direct\r\n
0xd0000045 | Proxy\r\n
0xd0000046 | Direct connection available\r\n
0xd0000047 | Proxy connection required\r\n

### 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000002 | AsyncOperation\r\n
0x10000003 | Socket\r\n
0x10000004 | WebSocket\r\n
0x10000005 | Http\r\n
0x10000006 | Rtc\r\n
0x30000000 | Info\r\n
0x3000000a | API Enter\r\n
0x3000000b | API Exit\r\n
0x3000000c | Async operation start\r\n
0x3000000d | Async operation complete\r\n
0x3000000e | Async operation failure\r\n
0x3000000f | Async operation abort\r\n
0x30000010 | Async operation close\r\n
0x30000011 | Async operation completion\r\n
0x30000012 | Async operation progress\r\n
0x30000013 | HTTP operation\r\n
0x30000014 | Processing after read\r\n
0x30000015 | Start read\r\n
0x30000016 | Read complete\r\n
0x30000017 | Read error\r\n
0x30000018 | Start write\r\n
0x30000019 | Write complete\r\n
0x3000001a | State change\r\n
0x3000001b | I/O error\r\n
0x3000001c | TCP connected\r\n
0x3000001d | RtcCompleteDelivery\r\n
0x3000001e | RtcFlush\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | APIs\r\n
0x70000002 | AsyncOperation\r\n
0x70000003 | EventNotification\r\n
0x70000004 | SocketConnect\r\n
0x70000005 | SocketAccept\r\n
0x70000006 | SocketSend\r\n
0x70000007 | SocketReceive\r\n
0x70000008 | SocketClose\r\n
0x70000009 | WebSocketConnect\r\n
0x7000000a | WebSocketSend\r\n
0x7000000b | WebSocketReceive\r\n
0x7000000c | WebSocketClose\r\n
0x7000000d | SslSocket\r\n
0x7000000e | SocketIO\r\n
0x90000001 | Microsoft-Windows-Runtime-Networking\r\n
0xb0000001 | %1 at %2 started.\r\n
0xb0000002 | %1 at %2 failed to start. The error code is %3: %4\r\n
0xb0000003 | %1 at %2 completed successfully.\r\n
0xb0000004 | %1 at %2 failed with error code %3: %4.\r\n
0xb0000005 | %1 at %2 was cancelled.\r\n
0xb0000006 | %1 at %2 was closed.\r\n
0xb0000007 | Failed to parse URI '%1'.\r\n
0xb0000008 | Failed to create URI with base URI '%1' and relative URI '%2'.\r\n
0xb0000009 | Add HTTP header '%1: %2'.\r\n
0xb000000a | Start connect request to '%1' with credential of '%2'.\r\n
0xb000000b | Start connect request to '%1' with default credential.\r\n
0xb000000c | Failed connect request to '%1' at port %2. The last error is %3: %4\r\n
0xb000000d | Opening request to '%1' to '%2' with flags %3.\r\n
0xb000000e | Failed open request to '%1'. The last error is %2: %3\r\n
0xb000000f | Request context %1 has request handle %2 to '%3'.\r\n
0xb0000010 | Set HTTP send and receive timeout to %2ms on request handle %1.\r\n
0xb0000011 | Start send to request handle %1 with content length %2.\r\n
0xb0000012 | Request handle %1 completed synchronously.\r\n
0xb0000013 | Request context %1 completed send asynchronously.\r\n
0xb0000014 | Writing %2 bytes to request handle %1.\r\n
0xb0000015 | Failed to send entity body to request handle %1. The last error is %2: %3\r\n
0xb0000016 | Sent HTTP request at request handle %1: %2\r\n
0xb0000017 | Start to receive response from request handle %1.\r\n
0xb0000018 | Received HTTP response from request handle %1 with status code %2 and status description '%3'.\r\n
0xb0000019 | Receive HTTP response from request handle %1: %2\r\n
0xb000001a | Failed to receive HTTP response from request handle %1. The last error is %2: %3\r\n
0xb000001b | Request context %1 received HTTP response of %2 bytes, which is over the %3 limit.\r\n
0xb000001c | Request context %1 resubmitting the request.\r\n
0xb000001d | Reusing the request handle %1 for server '%2'.\r\n
0xb000001e | Request context %1 was aborted.\r\n
0xb000001f | Progress to '%1': %2 bytes sent; %3 total bytes to send; %4 bytes received; %5 total bytes to receive.\r\n
0xb0000020 | HTTP request to '%1' completed. The error code is %2: %3\r\n
0xb0000021 | %1 at %2 failed to process HTTP response '%3'. The error code is %4: %5\r\n
0xb0000022 | %1::%2 is called.\r\n
0xb0000023 | %1::%2 returned successfully.\r\n
0xb0000024 | %1::%2 failed with HRESULT %3: %4\r\n
0xb0000025 | Win32 API %1 failed with error code %2: %3.\r\n
0xb0000026 | Unable to cancel GetAddrInfoEx with handle %1. The error code was %2: %3.\r\n
0xb0000027 | Unable to cancel DnsQueryEx with handle %1. The error code was %2: %3.\r\n
0xb0000028 | DatagramSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000029 | DatagramSocket %1 is raising event with %2 bytes received from sender '%4'.\r\n
0xb000002a | DatagramSocket %1 started receiving message at socket %2.\r\n
0xb000002b | DatagramSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb000002c | %1 at %2 is trying to receive %3 bytes at socket %4.\r\n
0xb000002d | %1 at %2 has received %3 bytes and continues to receive the remaining %4 bytes.\r\n
0xb000002e | %1 at %2 received %3 bytes.\r\n
0xb000002f | TCP socket %1 is connected: local port = %2; remote IP address: %3; remote port = %4.\r\n
0xb0000030 | UDP socket %1 is connected to remote address: %3.\r\n
0xb0000031 | The datagram received by socket %1 from sender '%3' does not contain IP packet information.\r\n
0xb0000032 | %1 at %2 sent %3 bytes.\r\n
0xb0000033 | %1 at %2 is trying to send %3 bytes at socket %4.\r\n
0xb0000034 | MessageWebSocket %1 received the close frame from the server.\r\n
0xb0000035 | MessageWebSocket %1 is raising event with %2 bytes received.\r\n
0xb0000036 | MessageWebSocket %1 failed to start receiving. The HRESULT was %2: %3.\r\n
0xb0000037 | MessageWebSocket %1 failed to deliver event and stopped receiving due to error %2: %3.\r\n
0xb0000039 | WebSocket %1 is sending the close frame.\r\n
0xb000003a | WebSocket %1 is receiving the close frame. Code: %2; Reason: %3\r\n
0xb000003b | WebSocket %1 I/O operation completed with error. The HRESULT was %2: %3.\r\n
0xb000003c | WebSocket %1 at %2 sent %3 bytes.\r\n
0xb000003d | WebSocket %1 at %2 is trying to send %3 bytes at WebSocket %4.\r\n
0xb000003e | %1 is already closed and CompleteDelivery is pending with: outstanding read operations: %2.\r\n
0xb000003f | %1.CompleteDelivery is pending with: outstanding read operations: %2, pending Winsock requests: %3, data available: %4.\r\n
0xb0000040 | %1.Flush is pending with: outstanding write operations: %2.\r\n
0xb0000041 | %1.CompleteDelivery is pending with: outstanding read operations: %2.\r\n
0xb0000042 | Socket connection established: %1.\r\n
0xb0000043 | Proxy lookup for socket connection to '%1' completed successfully: %2.\r\n
0xb0000044 | Proxy lookup for socket connection to '%1' completed with error %2: %3\r\n
0xb0000045 | Ignored server certificate error count: %1\r\n
0xb0000046 | Server certificate thumbprint: '%1', certificate error count: %3, contains fatal certificate errors: %2, intermediate certificate count: %5.\r\n
0xb0000047 | Failed to flush reads and wait for pending I/O to complete with context %1. Error was %2: %3.\r\n
0xb0000048 | Handle %1: HTTP/2 enabled.\r\n
0xb0000049 | %1 - Line: %2 Status: %3\r\n
0xb000004a | Async operation %1 at %2 started server custom validation.\r\n
0xb000004b | Async operation %1 at %2 waiting for completion of server custom validation.\r\n
0xb000004c | Async operation %1 at %2 failed server custom validation.\r\n
0xb000004d | Async operation %1 at %2 successfully completed server custom validation.\r\n
0xd0000001 | AcceptAsync\r\n
0xd0000002 | BindServiceNameAsync\r\n
0xd0000003 | ConnectAsync\r\n
0xd0000004 | ReadAsync\r\n
0xd0000005 | WriteAsync\r\n
0xd0000006 | JoinMulticastGroup\r\n
0xd0000007 | UpgradeToSslAsync\r\n
0xd0000008 | GetEndpointPairsAsync\r\n
0xd0000009 | GetOutputStreamAsync\r\n
0xd000000a | CompleteDelivery\r\n
0xd000000b | Flush\r\n
0xd000000c | FlushAsync\r\n
0xd000000d | SendFinalFrameAsync\r\n
0xd000000e | SendNonfinalFrameAsync\r\n
0xd000000f | StreamSocket\r\n
0xd0000010 | StreamSocketInputStream\r\n
0xd0000011 | StreamSocketOutputStream\r\n
0xd0000012 | DatagramSocket\r\n
0xd0000013 | DatagramSocketOutputStream\r\n
0xd0000014 | DatagramSocketWriteToOutputStream\r\n
0xd0000015 | MessageWebSocket\r\n
0xd0000016 | StreamWebSocket\r\n
0xd0000017 | StreamWebSocketInputStream\r\n
0xd0000018 | WebSocketOutputStream\r\n
0xd0000019 | StreamSocketListener\r\n
0xd000001a | DatagramSocketInputStream\r\n
0xd000001b | AcceptEx\r\n
0xd000001c | connect\r\n
0xd000001d | bind\r\n
0xd000001e | listen\r\n
0xd000001f | getpeername\r\n
0xd0000020 | getsockname\r\n
0xd0000021 | getsockopt\r\n
0xd0000022 | setsockopt\r\n
0xd0000023 | GetAddrInfoEx\r\n
0xd0000024 | GetBestInferfaceEx\r\n
0xd0000025 | WSAStartup\r\n
0xd0000026 | WSAConnectByName\r\n
0xd0000027 | WSAIoctl\r\n
0xd0000028 | WSARecv\r\n
0xd0000029 | WSARecvFrom\r\n
0xd000002a | WSARecvMsg\r\n
0xd000002b | WSASend\r\n
0xd000002c | WSASendMsg\r\n
0xd000002d | WSASocket\r\n
0xd000002e | CreateThreadpoolIo\r\n
0xd000002f | TrySubmitThreadpoolCallback\r\n
0xd0000030 | HttpWebSocketCompleteUpgrade\r\n
0xd0000031 | HttpWebSocketSend\r\n
0xd0000032 | HttpWebSocketReceive\r\n
0xd0000033 | InternetSetStatusCallback\r\n
0xd0000034 | CancelIoEx\r\n
0xd0000035 | DnsQueryEx\r\n
0xd0000036 | GetIfEntry2\r\n
0xd0000037 | GetPerTcpConnectionEStats\r\n
0xd0000038 | GetPerTcp6ConnectionEStats\r\n
0xd0000039 | GetTcpTable\r\n
0xd000003a | GetTcp6Table\r\n
0xd000003b | WlanOpenHandle\r\n
0xd000003c | WlanSetInterface\r\n
0xd000003d | WlanCloseHandle\r\n
0xd000003e | GetAdaptersAddresses\r\n
0xd000003f | ConnectOperation\r\n
0xd0000040 | ReadOperation\r\n
0xd0000041 | WriteOperation\r\n
0xd0000042 | ListenOperation\r\n
0xd0000043 | AcceptOperation\r\n
0xd0000044 | UpgradeOperation\r\n
0xd0000045 | GetEndpointPairsOperation\r\n
0xd0000046 | GetOutputStreamOperation\r\n
0xd0000047 | Direct\r\n
0xd0000048 | Proxy\r\n
0xd0000049 | Direct connection available\r\n
0xd000004a | Proxy connection required\r\n
