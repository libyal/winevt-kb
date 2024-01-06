## rdpcorets.dll

Path: %SystemRoot%\system32\RdpCoreTS.dll

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x3000000b | Initialize\r\n
0x3000000c | Terminate\r\n
0x3000000d | RCMProtocolImpl\r\n
0x3000000e | ProtocolExchange\r\n
0x3000000f | EstablishConnection\r\n
0x30000010 | NetworkDetect\r\n
0x30000011 | CloseConnection\r\n
0x30000012 | NetworkBinding\r\n
0x30000013 | Runtime\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | RDP Stack\r\n
0x70000002 | RDP Graphics module\r\n
0x70000003 | RemoteFX module\r\n
0x70000004 | RemoteFX module\r\n
0x90000001 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Admin\r\n
0x90000002 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational\r\n
0xb0000001 | The RDP Graphics module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status error code was %1.\r\n
0xb0000002 | Remote Desktop Protocol will use the RDP Graphics module to connect to the client computer. The RDP Graphics module is being used based on the server configuration, client configuration, and network connection.\r\n
0xb0000003 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000004 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000005 | The client computer does not support RemoteFX. The connection will be made with the RDP Graphics. The relevant status code was %1.\r\n
0xb0000006 | The resolution requested by the remote client is not supported by RemoteFX. The connection will be made with RemoteFX using a supported resolution. Resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000007 | The resolution requested by the remote client could not be set. The default resolution will be set for the RemoteFX session. The server may be experiencing high load or require a restart.\r\n
0xb0000008 | Module terminated.\r\n
0xb0000021 | Remote Desktop Protocol will use the RemoteFX guest mode module to connect to the client computer.\r\n
0xb0000022 | Remote Desktop Protocol will use the RemoteFX host mode module to connect to the client computer.\r\n
0xb0000023 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000024 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000025 | The display resolution requested by the remote client is not supported by RemoteFX host mode module. The resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000026 | The display resolution requested by the remote client could not be enabled. The default resolution will be enabled for the RemoteFX session. The server may be experiencing high load\r\n
0xb0000041 | Connection %1 created \r\n
0xb0000042 | The connection %1 was assigned to session #2\r\n
0xb0000043 | The RemoteFX protocol connection %1 encountered an error (%2)\r\n
0xb0000061 | The RDP protocol component %1 detected an error (%2) in the protocol stream and the client was disconnected.\r\n
0xb0000062 | A TCP connection has been successfully established.\r\n
0xb0000063 | The TCP connection has failed with the error code %1.\r\n
0xb0000064 | The server has confirmed that the client's multi-transport capability.\r\n
0xb0000065 | The network characteristics detection function has been disabled because of %1.\r\n
0xb0000066 | The server has terminated main RDP connection with the client.\r\n
0xb0000081 | The server is using %1 to bind to port %2.\r\n
0xb0000082 | The server has initiated a multi-transport request to the client, for tunnel: %1.\r\n
0xb0000083 | The server accepted a new %1 connection from client %2.\r\n
0xb0000084 | A channel %1 has been connected between the server and the client using transport tunnel: %2.\r\n
0xb0000085 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps.\r\n
0xb0000086 | Link latency and bandwidth could not be detected for tunnel %2.  The error code is %1. The following default network characteristics will be used;  Link latency: %3 milliseconds and Bandwidth:%4 kbps. \r\n
0xb0000087 | The multi-transport connection finished for tunnel: %1, its transport type set to %2.\r\n
0xb0000088 | Unable to establish a multi-transport connection; the connection will use TCP. Consult the product documentation to enable UDP Connections.\r\n
0xb0000089 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps. Connections with these network characteristics may impact user experience.\r\n
0xb000008a | The DTLS initialization failed with the error code %1, TLS will be used instead. Audio/Video experience may be impacted.\r\n
0xb000008b | The server security layer detected an error (%1) in the protocol stream and the client (Client IP:%2) has been disconnected.\r\n
0xb000008c | A connection from the client computer with an IP address of %1 failed because the user name or password is not correct.\r\n
0xb00000a1 | The RemoteFX encoding engine encountered an error (%1).\r\n
0xb00000a2 | The client supports RDP 8.0 protocol.\r\n
0xb00000a3 | The client suports RDP 7.1 or lower protocol.\r\n
0xb00000a4 | The client advertized RDP8 protocol configuration is not supported by the server.\r\n
0xb00000a5 | RemoteFX Encoding for RemoteFX Clients designed for Windows Server 2008 R2 SP1 is enabled and a compatible session was created.\r\n
0xb00000a6 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for the use minimum network bandwidth. The configuration code is %1.\r\n
0xb00000a7 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for experience. The configuration code is %1.\r\n
0xb00000c1 | The RemoteFX Media Remoting is not supported by the client.\r\n
0xb00000c2 | The RemoteFX Media Remoting is not supported by the current server configuration.\r\n
0xb00000c3 | The RemoteFX Media Remoting module encountered an error. The error code is %1.\r\n

### 6.3.9600.16384, 6.3.9600.17335

Message identifier | Message string
--- | ---
0x3000000b | Initialize\r\n
0x3000000c | Terminate\r\n
0x3000000d | RCMProtocolImpl\r\n
0x3000000e | ProtocolExchange\r\n
0x3000000f | EstablishConnection\r\n
0x30000010 | NetworkDetect\r\n
0x30000011 | CloseConnection\r\n
0x30000012 | NetworkBinding\r\n
0x30000013 | Runtime\r\n
0x30000014 | AdvancedRemoteAppEnabled\r\n
0x30000015 | AdvancedRemoteAppNotEnabled\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | RDP Stack\r\n
0x70000002 | RDP Graphics module\r\n
0x70000003 | RemoteFX module\r\n
0x70000004 | RemoteFX module\r\n
0x90000001 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Admin\r\n
0x90000002 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational\r\n
0x90000003 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Debug\r\n
0xb0000001 | The RDP Graphics module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status error code was %1.\r\n
0xb0000002 | Remote Desktop Protocol will use the RDP Graphics module to connect to the client computer. The RDP Graphics module is being used based on the server configuration, client configuration, and network connection.\r\n
0xb0000003 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000004 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000005 | The client computer does not support RemoteFX. The connection will be made with the RDP Graphics. The relevant status code was %1.\r\n
0xb0000006 | The resolution requested by the remote client is not supported by RemoteFX. The connection will be made with RemoteFX using a supported resolution. Resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000007 | The resolution requested by the remote client could not be set. The default resolution will be set for the RemoteFX session. The server may be experiencing high load or require a restart.\r\n
0xb0000008 | Module terminated.\r\n
0xb0000021 | Remote Desktop Protocol will use the RemoteFX guest mode module to connect to the client computer.\r\n
0xb0000022 | Remote Desktop Protocol will use the RemoteFX host mode module to connect to the client computer.\r\n
0xb0000023 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000024 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000025 | The display resolution requested by the remote client is not supported by RemoteFX host mode module. The resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000026 | The display resolution requested by the remote client could not be enabled. The default resolution will be enabled for the RemoteFX session. The server may be experiencing high load\r\n
0xb0000041 | Connection %1 created \r\n
0xb0000042 | The connection %1 was assigned to session %2\r\n
0xb0000043 | The RemoteFX protocol connection %1 encountered an error (%2)\r\n
0xb0000044 | TMT: ConnectionName=%1, PromptForCredentials=%2, PromptForCredentialsDone=%3, GfxChannelOpened=%4, FirstGraphicsReceived=%5 [ms]\r\n
0xb0000061 | The RDP protocol component %1 detected an error (%2) in the protocol stream and the client was disconnected.\r\n
0xb0000062 | A TCP connection has been successfully established.\r\n
0xb0000063 | The TCP connection has failed with the error code %1.\r\n
0xb0000064 | The server has confirmed that the client's multi-transport capability.\r\n
0xb0000065 | The network characteristics detection function has been disabled because of %1.\r\n
0xb0000066 | The server has terminated main RDP connection with the client.\r\n
0xb0000067 | The disconnect reason is %1\r\n
0xb0000081 | The server is using %1 to bind to port %2.\r\n
0xb0000082 | The server has initiated a multi-transport request to the client, for tunnel: %1.\r\n
0xb0000083 | The server accepted a new %1 connection from client %2.\r\n
0xb0000084 | A channel %1 has been connected between the server and the client using transport tunnel: %2.\r\n
0xb0000085 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps.\r\n
0xb0000086 | Link latency and bandwidth could not be detected for tunnel %2.  The error code is %1. The following default network characteristics will be used;  Link latency: %3 milliseconds and Bandwidth:%4 kbps. \r\n
0xb0000087 | The multi-transport connection finished for tunnel: %1, its transport type set to %2.\r\n
0xb0000088 | Unable to establish a multi-transport connection; the connection will use TCP. Consult the product documentation to enable UDP Connections.\r\n
0xb0000089 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps. Connections with these network characteristics may impact user experience.\r\n
0xb000008a | The DTLS initialization failed with the error code %1, TLS will be used instead. Audio/Video experience may be impacted.\r\n
0xb000008b | The server security layer detected an error (%1) in the protocol stream and the client (Client IP:%2) has been disconnected.\r\n
0xb000008c | A connection from the client computer with an IP address of %1 failed because the user name or password is not correct.\r\n
0xb000008d | PerfCounter session started with instance ID %1\r\n
0xb00000a1 | The RemoteFX encoding engine encountered an error (%1).\r\n
0xb00000a2 | The client supports version %1 of the RDP graphics protocol, client mode: %2, H264 enabled: %3\r\n
0xb00000a3 | The client suports RDP 7.1 or lower protocol.\r\n
0xb00000a4 | The client advertized RDP8 protocol configuration is not supported by the server.\r\n
0xb00000a5 | RemoteFX Encoding for RemoteFX Clients designed for Windows Server 2008 R2 SP1 is enabled and a compatible session was created.\r\n
0xb00000a6 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for the minimum use of network bandwidth.\r\n
0xb00000a7 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for experience.\r\n
0xb00000a8 | The resolution requested by the client: Monitor %1: (%2, %3), origin: (%4, %5).\r\n
0xb00000a9 | The client operating system type is (%1, %2).\r\n
0xb00000c1 | The RemoteFX Media Remoting is not supported by the client.\r\n
0xb00000c2 | The RemoteFX Media Remoting is not supported by the current server configuration.\r\n
0xb00000c3 | The RemoteFX Media Remoting module encountered an error. The error code is %1.\r\n
0xb00000e1 | %1: Transitioned successfully from %3 to %5 in response to %7.\r\n
0xb00000e2 | %1: An error was encountered when transitioning from %3 in response to %7 (error code %8).\r\n
0xb0000101 | The connection is using advanced RemoteFX RemoteApp graphics.\r\n
0xb0000102 | The connection is not using advanced RemoteFX RemoteApp graphics\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x3000000b | Initialize\r\n
0x3000000c | Terminate\r\n
0x3000000d | RCMProtocolImpl\r\n
0x3000000e | ProtocolExchange\r\n
0x3000000f | EstablishConnection\r\n
0x30000010 | NetworkDetect\r\n
0x30000011 | CloseConnection\r\n
0x30000012 | NetworkBinding\r\n
0x30000013 | Runtime\r\n
0x30000014 | AdvancedRemoteAppEnabled\r\n
0x30000015 | AdvancedRemoteAppNotEnabled\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | RDP Stack\r\n
0x70000002 | RDP Graphics module\r\n
0x70000003 | RemoteFX module\r\n
0x70000004 | RemoteFX module\r\n
0x90000001 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Admin\r\n
0x90000002 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational\r\n
0x90000003 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Debug\r\n
0xb0000001 | The RDP Graphics module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status error code was %1.\r\n
0xb0000002 | Remote Desktop Protocol will use the RDP Graphics module to connect to the client computer. The RDP Graphics module is being used based on the server configuration, client configuration, and network connection.\r\n
0xb0000003 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000004 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000005 | The client computer does not support RemoteFX. The connection will be made with the RDP Graphics. The relevant status code was %1.\r\n
0xb0000006 | The resolution requested by the remote client is not supported by RemoteFX. The connection will be made with RemoteFX using a supported resolution. Resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000007 | The resolution requested by the remote client could not be set. The default resolution will be set for the RemoteFX session. The server may be experiencing high load or require a restart.\r\n
0xb0000008 | Module terminated.\r\n
0xb0000021 | Remote Desktop Protocol will use the RemoteFX guest mode module to connect to the client computer.\r\n
0xb0000022 | Remote Desktop Protocol will use the RemoteFX host mode module to connect to the client computer.\r\n
0xb0000023 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000024 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000025 | The display resolution requested by the remote client is not supported by RemoteFX host mode module. The resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000026 | The display resolution requested by the remote client could not be enabled. The default resolution will be enabled for the RemoteFX session. The server may be experiencing high load\r\n
0xb0000041 | Connection %1 created \r\n
0xb0000042 | The connection %1 was assigned to session %2\r\n
0xb0000043 | The RemoteFX protocol connection %1 encountered an error (%2)\r\n
0xb0000044 | TMT: ConnectionName=%1, PromptForCredentials=%2, PromptForCredentialsDone=%3, GfxChannelOpened=%4, FirstGraphicsReceived=%5 [ms]\r\n
0xb0000045 | Listener %1 is loaded\r\n
0xb0000046 | The listener listens with display driver %1 available.\r\n
0xb0000047 | The connection %1 uses display driver %2.\r\n
0xb0000061 | The RDP protocol component %1 detected an error (%2) in the protocol stream and the client was disconnected.\r\n
0xb0000062 | A TCP connection has been successfully established.\r\n
0xb0000063 | The TCP connection has failed with the error code %1.\r\n
0xb0000064 | The server has confirmed that the client's multi-transport capability.\r\n
0xb0000065 | The network characteristics detection function has been disabled because of %1.\r\n
0xb0000066 | The server has terminated main RDP connection with the client.\r\n
0xb0000067 | The disconnect reason is %1\r\n
0xb0000068 | Client timezone is %1 hour from UTC; \r\n
0xb0000069 | The server's security layer setting allows it to use native RDP encryption, which is no longer recommended. Consider changing the server security layer to require SSL. You can change this setting in Group Policy.\r\n
0xb0000081 | The server is using %1 to bind to port %2.\r\n
0xb0000082 | The server has initiated a multi-transport request to the client, for tunnel: %1.\r\n
0xb0000083 | The server accepted a new %1 connection from client %2.\r\n
0xb0000084 | A channel %1 has been connected between the server and the client using transport tunnel: %2.\r\n
0xb0000085 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps.\r\n
0xb0000086 | Link latency and bandwidth could not be detected for tunnel %2.  The error code is %1. The following default network characteristics will be used;  Link latency: %3 milliseconds and Bandwidth:%4 kbps. \r\n
0xb0000087 | The multi-transport connection finished for tunnel: %1, its transport type set to %2.\r\n
0xb0000088 | Unable to establish a multi-transport connection; the connection will use TCP. Consult the product documentation to enable UDP Connections.\r\n
0xb0000089 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps. Connections with these network characteristics may impact user experience.\r\n
0xb000008a | The DTLS initialization failed with the error code %1, TLS will be used instead. Audio/Video experience may be impacted.\r\n
0xb000008b | The server security layer detected an error (%1) in the protocol stream and the client (Client IP:%2) has been disconnected.\r\n
0xb000008c | A connection from the client computer with an IP address of %1 failed because the user name or password is not correct.\r\n
0xb000008d | PerfCounter session started with instance ID %1\r\n
0xb000008e | TCP socket READ operation failed, error %1\r\n
0xb000008f | TCP socket WRITE operation failed, error %1\r\n
0xb0000090 | TCP socket was gracefully terminated\r\n
0xb0000091 | During this connection, server has not sent data or graphics update for %1 seconds (Idle1: %2, Idle2: %3).\r\n
0xb0000092 | AutoReconnect failed with error %1\r\n
0xb0000093 | LogonUserExEx failed with error %1\r\n
0xb0000094 | Channel %1 has been closed between the server and the client on transport tunnel: %2.\r\n
0xb0000095 | Logon certificate sent by client did not pass validation. Error: %1\r\n
0xb00000a1 | The RemoteFX encoding engine encountered an error (%1). Server: %2\r\n
0xb00000a2 | The client supports version %1 of the RDP graphics protocol, client mode: %2, AVC available: %3, Initial profile: %4. Server: %5\r\n
0xb00000a3 | The client supports RDP 7.1 or lower protocol. Server: %1\r\n
0xb00000a4 | The client advertised protocol configurations which are not supported by the server. Server: %1\r\n
0xb00000a5 | RDP RemoteFX graphics encoding is enabled. Server: %1\r\n
0xb00000a6 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for the minimum use of network bandwidth. Server: %1\r\n
0xb00000a7 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for experience. Server: %1\r\n
0xb00000a8 | The resolution requested by the client: Monitor %1: (%2, %3), origin: (%4, %5). Server: %6\r\n
0xb00000a9 | The client operating system type is (%1, %2).  Server: %3\r\n
0xb00000aa | AVC hardware encoder enabled: %1, encoder name is %2. Server: %3\r\n
0xb00000c1 | The RemoteFX Media Remoting is not supported by the client.\r\n
0xb00000c2 | The RemoteFX Media Remoting is not supported by the current server configuration.\r\n
0xb00000c3 | The RemoteFX Media Remoting module encountered an error. The error code is %1.\r\n
0xb00000e1 | %1: Transitioned successfully from %3 to %5 in response to %7.\r\n
0xb00000e2 | %1: An error was encountered when transitioning from %3 in response to %7 (error code %8).\r\n
0xb0000101 | The connection is using advanced RemoteFX RemoteApp graphics.\r\n
0xb0000102 | The connection is not using advanced RemoteFX RemoteApp graphics\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x3000000b | Initialize\r\n
0x3000000c | Terminate\r\n
0x3000000d | RCMProtocolImpl\r\n
0x3000000e | ProtocolExchange\r\n
0x3000000f | EstablishConnection\r\n
0x30000010 | NetworkDetect\r\n
0x30000011 | CloseConnection\r\n
0x30000012 | NetworkBinding\r\n
0x30000013 | Runtime\r\n
0x30000014 | AdvancedRemoteAppEnabled\r\n
0x30000015 | AdvancedRemoteAppNotEnabled\r\n
0x30000016 | UDPReverseConnect\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | RDP Stack\r\n
0x70000002 | RDP Graphics module\r\n
0x70000003 | RemoteFX module\r\n
0x70000004 | RemoteFX module\r\n
0x90000001 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Admin\r\n
0x90000002 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational\r\n
0x90000003 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Debug\r\n
0xb0000001 | The RDP Graphics module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status error code was %1.\r\n
0xb0000002 | Remote Desktop Protocol will use the RDP Graphics module to connect to the client computer. The RDP Graphics module is being used based on the server configuration, client configuration, and network connection.\r\n
0xb0000003 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000004 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000005 | The client computer does not support RemoteFX. The connection will be made with the RDP Graphics. The relevant status code was %1.\r\n
0xb0000006 | The resolution requested by the remote client is not supported by RemoteFX. The connection will be made with RemoteFX using a supported resolution. Resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000007 | The resolution requested by the remote client could not be set. The default resolution will be set for the RemoteFX session. The server may be experiencing high load or require a restart.\r\n
0xb0000008 | Module terminated.\r\n
0xb0000021 | Remote Desktop Protocol will use the RemoteFX guest mode module to connect to the client computer.\r\n
0xb0000022 | Remote Desktop Protocol will use the RemoteFX host mode module to connect to the client computer.\r\n
0xb0000023 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000024 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000025 | The display resolution requested by the remote client is not supported by RemoteFX host mode module. The resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000026 | The display resolution requested by the remote client could not be enabled. The default resolution will be enabled for the RemoteFX session. The server may be experiencing high load\r\n
0xb0000041 | Connection %1 created \r\n
0xb0000042 | The connection %1 was assigned to session %2\r\n
0xb0000043 | The RemoteFX protocol connection %1 encountered an error (%2)\r\n
0xb0000044 | TMT: ConnectionName=%1, PromptForCredentials=%2, PromptForCredentialsDone=%3, GfxChannelOpened=%4, FirstGraphicsReceived=%5 [ms]\r\n
0xb0000045 | Listener %1 is loaded\r\n
0xb0000046 | The listener listens with display driver %1 available.\r\n
0xb0000047 | The connection %1 uses display driver %2.\r\n
0xb0000048 | Interface method called: %1\r\n
0xb0000049 | Inner encryption disabled? %1\r\n
0xb0000061 | The RDP protocol component %1 detected an error (%2) in the protocol stream and the client was disconnected.\r\n
0xb0000062 | A TCP connection has been successfully established.\r\n
0xb0000063 | The TCP connection has failed with the error code %1.\r\n
0xb0000064 | The server has confirmed that the client's multi-transport capability.\r\n
0xb0000065 | The network characteristics detection function has been disabled because of %1.\r\n
0xb0000066 | The server has terminated main RDP connection with the client.\r\n
0xb0000067 | The disconnect reason is %1\r\n
0xb0000068 | Client timezone is %1 hour from UTC; \r\n
0xb0000069 | The server's security layer setting allows it to use native RDP encryption, which is no longer recommended. Consider changing the server security layer to require SSL. You can change this setting in Group Policy.\r\n
0xb000006a | Disconnect initiated by server; forcing an AutoReconnect since listener is disabled.\r\n
0xb000006b | Received Disconnect Provider Indication from the client.\r\n
0xb0000081 | The server is using %1 to bind to port %2.\r\n
0xb0000082 | The server has initiated a multi-transport request to the client, for tunnel: %1.\r\n
0xb0000083 | The server accepted a new %1 connection from client %2.\r\n
0xb0000084 | A channel %1 has been connected between the server and the client using transport tunnel: %2.\r\n
0xb0000085 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps.\r\n
0xb0000086 | Link latency and bandwidth could not be detected for tunnel %2.  The error code is %1. The following default network characteristics will be used;  Link latency: %3 milliseconds and Bandwidth:%4 kbps. \r\n
0xb0000087 | The multi-transport connection finished for tunnel: %1, its transport type set to %2.\r\n
0xb0000088 | Unable to establish a multi-transport connection; the connection will use TCP. Consult the product documentation to enable UDP Connections.\r\n
0xb0000089 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps. Connections with these network characteristics may impact user experience.\r\n
0xb000008a | The DTLS initialization failed with the error code %1, TLS will be used instead. Audio/Video experience may be impacted.\r\n
0xb000008b | The server security layer detected an error (%1) in the protocol stream and the client (Client IP:%2) has been disconnected.\r\n
0xb000008c | A connection from the client computer with an IP address of %1 failed because the user name or password is not correct.\r\n
0xb000008d | PerfCounter session started with instance ID %1\r\n
0xb000008e | TCP socket READ operation failed, error %1\r\n
0xb000008f | TCP socket WRITE operation failed, error %1\r\n
0xb0000090 | TCP socket was gracefully terminated\r\n
0xb0000091 | During this connection, server has not sent data or graphics update for %1 seconds (Idle1: %2, Idle2: %3).\r\n
0xb0000092 | AutoReconnect failed with error %1\r\n
0xb0000093 | LogonUserExEx failed with error %1\r\n
0xb0000094 | Channel %1 has been closed between the server and the client on transport tunnel: %2.\r\n
0xb0000095 | Logon certificate sent by client did not pass validation. Error: %1\r\n
0xb0000096 | Long delay experienced while flushing data to the network. Flush time: %1 ms, flush interval: %2 ms.\r\n
0xb0000097 | In the past %1 ms, %2 heartbeats were sent to the client. Max time without sending packets in recent history: %3 ms (all packets); throughout connection: %4 ms (data), %5 ms (heartbeats), %6 ms (all packets). Time between disconnect and last packet sent: %7 ms\r\n
0xb0000098 | Timestamp: %1 ms, heartbeats sent: %2, data packet last sent: %3 ms, heartbeat last sent: %4 ms.\r\n
0xb0000099 | Session negotiated TLS version %1\r\n
0xb000009a | %1. Error %2\r\n
0xb00000a1 | The RemoteFX encoding engine encountered an error (%1). Server: %2\r\n
0xb00000a2 | The client supports version %1 of the RDP graphics protocol, client mode: %2, AVC available: %3, Initial profile: %4. Server: %5\r\n
0xb00000a3 | The client supports RDP 7.1 or lower protocol. Server: %1\r\n
0xb00000a4 | The client advertised protocol configurations which are not supported by the server. Server: %1\r\n
0xb00000a5 | RDP RemoteFX graphics encoding is enabled. Server: %1\r\n
0xb00000a6 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for the minimum use of network bandwidth. Server: %1\r\n
0xb00000a7 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for experience. Server: %1\r\n
0xb00000a8 | The resolution requested by the client: Monitor %1: (%2, %3), origin: (%4, %5). Server: %6\r\n
0xb00000a9 | The client operating system type is (%1, %2).  Server: %3\r\n
0xb00000aa | AVC hardware encoder enabled: %1, encoder name is %2. Server: %3\r\n
0xb00000c1 | The RemoteFX Media Remoting is not supported by the client.\r\n
0xb00000c2 | The RemoteFX Media Remoting is not supported by the current server configuration.\r\n
0xb00000c3 | The RemoteFX Media Remoting module encountered an error. The error code is %1.\r\n
0xb00000e1 | %1: Transitioned successfully from %3 to %5 in response to %7.\r\n
0xb00000e2 | %1: An error was encountered when transitioning from %3 in response to %7 (error code %8).\r\n
0xb00000e3 | %3\r\n
0xb00000e4 | Disconnect trace:%1 %2, Error code:%3\r\n
0xb00000e5 | %2\r\n
0xb0000101 | The connection is using advanced RemoteFX RemoteApp graphics.\r\n
0xb0000102 | The connection is not using advanced RemoteFX RemoteApp graphics\r\n
0xb0000121 | Got UDP reverse connect request to %1 port %2 connection id %3.\r\n
0xb0000122 | UDP reverse connect successful.\r\n
0xb0000123 | UDP reverse connect failed with error %1.\r\n
0xb0000124 | Multi transport listener NOT initialized. UDP reverse connect NOT supported.\r\n
0xb0000125 | Multi transport listener initialized. UDP reverse connect supported.\r\n
0xb0000126 | Reverse UDP connect is disabled by SxS registry settings.\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x3000000b | Initialize\r\n
0x3000000c | Terminate\r\n
0x3000000d | RCMProtocolImpl\r\n
0x3000000e | ProtocolExchange\r\n
0x3000000f | EstablishConnection\r\n
0x30000010 | NetworkDetect\r\n
0x30000011 | CloseConnection\r\n
0x30000012 | NetworkBinding\r\n
0x30000013 | Runtime\r\n
0x30000014 | AdvancedRemoteAppEnabled\r\n
0x30000015 | AdvancedRemoteAppNotEnabled\r\n
0x30000016 | UDPReverseConnect\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | RDP Stack\r\n
0x70000002 | RDP Graphics module\r\n
0x70000003 | RemoteFX module\r\n
0x70000004 | RemoteFX module\r\n
0x90000001 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Admin\r\n
0x90000002 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational\r\n
0x90000003 | Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Debug\r\n
0xb0000001 | The RDP Graphics module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status error code was %1.\r\n
0xb0000002 | Remote Desktop Protocol will use the RDP Graphics module to connect to the client computer. The RDP Graphics module is being used based on the server configuration, client configuration, and network connection.\r\n
0xb0000003 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000004 | The RemoteFX module failed to initialize. Verify that the server is correctly configured. A restart of the system may be needed. The relevant status code was %1.\r\n
0xb0000005 | The client computer does not support RemoteFX. The connection will be made with the RDP Graphics. The relevant status code was %1.\r\n
0xb0000006 | The resolution requested by the remote client is not supported by RemoteFX. The connection will be made with RemoteFX using a supported resolution. Resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000007 | The resolution requested by the remote client could not be set. The default resolution will be set for the RemoteFX session. The server may be experiencing high load or require a restart.\r\n
0xb0000008 | Module terminated.\r\n
0xb0000021 | Remote Desktop Protocol will use the RemoteFX guest mode module to connect to the client computer.\r\n
0xb0000022 | Remote Desktop Protocol will use the RemoteFX host mode module to connect to the client computer.\r\n
0xb0000023 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000024 | Unable to initialize the RemoteFX host mode module. Restart the computer to resolve the issue. If the issue is not resolved, verify the computer configuration.. The error code is %1.\r\n
0xb0000025 | The display resolution requested by the remote client is not supported by RemoteFX host mode module. The resolution requested by the client: Monitors %1: %2. Resolution applied: %3.\r\n
0xb0000026 | The display resolution requested by the remote client could not be enabled. The default resolution will be enabled for the RemoteFX session. The server may be experiencing high load\r\n
0xb0000041 | Connection %1 created \r\n
0xb0000042 | The connection %1 was assigned to session %2\r\n
0xb0000043 | The RemoteFX protocol connection %1 encountered an error (%2)\r\n
0xb0000044 | TMT: ConnectionName=%1, PromptForCredentials=%2, PromptForCredentialsDone=%3, GfxChannelOpened=%4, FirstGraphicsReceived=%5 [ms]\r\n
0xb0000045 | Listener %1 is loaded\r\n
0xb0000046 | The listener listens with display driver %1 available.\r\n
0xb0000047 | The connection %1 uses display driver %2.\r\n
0xb0000048 | Interface method called: %1\r\n
0xb0000049 | Inner encryption disabled? %1\r\n
0xb0000061 | The RDP protocol component %1 detected an error (%2) in the protocol stream and the client was disconnected.\r\n
0xb0000062 | A TCP connection has been successfully established.\r\n
0xb0000063 | The TCP connection has failed with the error code %1.\r\n
0xb0000064 | The server has confirmed that the client's multi-transport capability.\r\n
0xb0000065 | The network characteristics detection function has been disabled because of %1.\r\n
0xb0000066 | The server has terminated main RDP connection with the client.\r\n
0xb0000067 | The disconnect reason is %1\r\n
0xb0000068 | Client timezone is %1 hour from UTC; \r\n
0xb0000069 | The server's security layer setting allows it to use native RDP encryption, which is no longer recommended. Consider changing the server security layer to require SSL. You can change this setting in Group Policy.\r\n
0xb000006a | Disconnect initiated by server; forcing an AutoReconnect since listener is disabled.\r\n
0xb000006b | Received Disconnect Provider Indication from the client.\r\n
0xb0000081 | The server is using %1 to bind to port %2.\r\n
0xb0000082 | The server has initiated a multi-transport request to the client, for tunnel: %1.\r\n
0xb0000083 | The server accepted a new %1 connection from client %2.\r\n
0xb0000084 | A channel %1 has been connected between the server and the client using transport tunnel: %2.\r\n
0xb0000085 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps.\r\n
0xb0000086 | Link latency and bandwidth could not be detected for tunnel %2.  The error code is %1. The following default network characteristics will be used;  Link latency: %3 milliseconds and Bandwidth:%4 kbps. \r\n
0xb0000087 | The multi-transport connection finished for tunnel: %1, its transport type set to %2.\r\n
0xb0000088 | Unable to establish a multi-transport connection; the connection will use TCP. Consult the product documentation to enable UDP Connections.\r\n
0xb0000089 | The following network characteristics have been detected for tunnel %1; Link latency : %2 milliseconds and Bandwidth: %3 kbps. Connections with these network characteristics may impact user experience.\r\n
0xb000008a | The DTLS initialization failed with the error code %1, TLS will be used instead. Audio/Video experience may be impacted.\r\n
0xb000008b | The server security layer detected an error (%1) in the protocol stream and the client (Client IP:%2) has been disconnected.\r\n
0xb000008c | A connection from the client computer with an IP address of %1 failed because the user name or password is not correct.\r\n
0xb000008d | PerfCounter session started with instance ID %1\r\n
0xb000008e | TCP socket READ operation failed, error %1\r\n
0xb000008f | TCP socket WRITE operation failed, error %1\r\n
0xb0000090 | TCP socket was gracefully terminated\r\n
0xb0000091 | During this connection, server has not sent data or graphics update for %1 seconds (Idle1: %2, Idle2: %3).\r\n
0xb0000092 | AutoReconnect failed with error %1\r\n
0xb0000093 | LogonUserExEx failed with error %1\r\n
0xb0000094 | Channel %1 has been closed between the server and the client on transport tunnel: %2.\r\n
0xb0000095 | Logon certificate sent by client did not pass validation. Error: %1\r\n
0xb0000096 | Long delay experienced while flushing data to the network. Flush time: %1 ms, flush interval: %2 ms.\r\n
0xb0000097 | In the past %1 ms, %2 heartbeats were sent to the client. Max time without sending packets in recent history: %3 ms (all packets); throughout connection: %4 ms (data), %5 ms (heartbeats), %6 ms (all packets). Time between disconnect and last packet sent: %7 ms\r\n
0xb0000098 | Timestamp: %1 ms, heartbeats sent: %2, data packet last sent: %3 ms, heartbeat last sent: %4 ms.\r\n
0xb0000099 | Session negotiated TLS version %1\r\n
0xb000009a | %1. Error %2\r\n
0xb000009b | RDP Diagnostic Heartbeat\r\n
0xb00000a1 | The RemoteFX encoding engine encountered an error (%1). Server: %2\r\n
0xb00000a2 | The client supports version %1 of the RDP graphics protocol, client mode: %2, AVC available: %3, Initial profile: %4. Server: %5\r\n
0xb00000a3 | The client supports RDP 7.1 or lower protocol. Server: %1\r\n
0xb00000a4 | The client advertised protocol configurations which are not supported by the server. Server: %1\r\n
0xb00000a5 | RDP RemoteFX graphics encoding is enabled. Server: %1\r\n
0xb00000a6 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for the minimum use of network bandwidth. Server: %1\r\n
0xb00000a7 | The RemoteFX Adaptive Graphics internal configuration changed to optimize for experience. Server: %1\r\n
0xb00000a8 | The resolution requested by the client: Monitor %1: (%2, %3), origin: (%4, %5). Server: %6\r\n
0xb00000a9 | The client operating system type is (%1, %2).  Server: %3\r\n
0xb00000aa | AVC hardware encoder enabled: %1, encoder name is %2. Server: %3\r\n
0xb00000ab | The client is uncapable to support screen capture protection feature. Server: %1\r\n
0xb00000c1 | The RemoteFX Media Remoting is not supported by the client.\r\n
0xb00000c2 | The RemoteFX Media Remoting is not supported by the current server configuration.\r\n
0xb00000c3 | The RemoteFX Media Remoting module encountered an error. The error code is %1.\r\n
0xb00000e1 | %1: Transitioned successfully from %3 to %5 in response to %7.\r\n
0xb00000e2 | %1: An error was encountered when transitioning from %3 in response to %7 (error code %8).\r\n
0xb00000e3 | %3\r\n
0xb00000e4 | Disconnect trace:%1 %2, Error code:%3\r\n
0xb00000e5 | %2\r\n
0xb0000101 | The connection is using advanced RemoteFX RemoteApp graphics.\r\n
0xb0000102 | The connection is not using advanced RemoteFX RemoteApp graphics\r\n
0xb0000121 | Got UDP reverse connect request to %1 port %2 connection id %3.\r\n
0xb0000122 | UDP reverse connect successful.\r\n
0xb0000123 | UDP reverse connect failed with error %1.\r\n
0xb0000124 | Multi transport listener NOT initialized. UDP reverse connect NOT supported.\r\n
0xb0000125 | Multi transport listener initialized. UDP reverse connect supported.\r\n
0xb0000126 | Reverse UDP connect is disabled by SxS registry settings.\r\n
