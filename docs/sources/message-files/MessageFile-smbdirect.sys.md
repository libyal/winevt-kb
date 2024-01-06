## smbdirect.sys

Path: %SystemRoot%\system32\drivers\smbdirect.sys

### 6.3.9600.17056, 10.0.14393.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBDirect/Admin\r\n
0x90000002 | Microsoft-Windows-SMBDirect/Debug\r\n
0x90000003 | Microsoft-Windows-SMBDirect/Netmon\r\n
0xb0010001 | The network adapter '%1' is incompatible with SMB Direct. Compatible network adapters are required to support at least %2 SGE(s) per receive queue work request. This adapter supports a maximum of %3 SGE(s) per receive queue work request.\r\n
0xb0010002 | The network adapter '%1' is incompatible with SMB Direct. Compatible network adapters are required to support at least %2 SGE(s) per send queue work request. This adapter supports a maximum of %3 SGE(s) per send queue work request.\r\n
0xb0010003 | The network adapter '%1' is incompatible with SMB Direct. Compatible network adapters are required to support at least %2 SGE(s) per RDMA read request. This adapter supports a maximum of %3 SGE(s) per RDMA read request.\r\n
0xb0010004 | Setting %1\%2 is invalid. Verify that %2 is a DWORD (32-bit) value in the range %3 to %4 (inclusive). The default value of %5 will be used for this setting until the error is corrected.\r\n
0xb0010005 | The network adapter '%1' does not support a value of %4 for setting %2\%3. The closest adapter supported value of %5 will be used.\r\n
0xb0010006 | A connection has been terminated because no pending requests to network adapter '%6' have completed in the last %7 milliseconds. Verify that the network is operational and that the peer is responsive. This event may also indicate that there are insufficient send credits to support the workload. Socket = %1 Local = %3 Remote = %5\r\n
0xb0010007 | Settings BaseAffinityNode and MaxAffinityNode (\Registry\Machine\System\CurrentControlSet\Services\SmbDirect\Parameters) must specify a set of NUMA nodes that contain active processors. All of the system's processors will be eligible to perform SMB Direct processing until the error is corrected.\r\n
0xb001012c | Starting connect. Socket = %1 Local = %3 Remote = %5\r\n
0xb001012d | Connect succeeded. Socket = %1 Local = %3 Remote = %5\r\n
0xb001012e | Connect failed. Socket = %1 Local = %3 Remote = %5 Status = %6\r\n
0xb001012f | Timed out while waiting for connection establishment to complete - cancelling connect. Socket = %1 Local = %3 Remote = %5\r\n
0xb0010130 | NdkConnect failed. Socket = %1 Local = %3 Remote = %5 Status = %6\r\n
0xb0010131 | NdkCompleteConnect failed. Socket = %1 Local = %3 Remote = %5 Status = %6\r\n
0xb0010132 | Failed to negotiate a common SMB Direct version with the peer. Socket = %1 Local = %3 Remote = %5 MinVersion = %6 MaxVersion = %7 PeerMinVersion = %8 PeerMaxVersion = %9\r\n
0xb001015e | Received connect request. ListenSocket = %1 Local = %3 Remote = %5\r\n
0xb001015f | Rejected connect request - connect backlog limit exceeded. ListenSocket = %1 Local = %3 Remote = %5\r\n
0xb0010160 | Rejected connect request - not enough memory. ListenSocket = %1 Local = %3 Remote = %5\r\n
0xb0010161 | Timed-out while waiting to receive a negotiate request - cancelling accept. Socket = %1 Local = %3 Remote = %5\r\n
0xb0010162 | NdkAccept failed. Socket = %1 Local = %3 Remote = %5 Status = %6\r\n
0xb0010163 | Accept started. Socket = %1 Local = %3 Remote = %5\r\n
0xb0010164 | Accept succeeded. Socket = %1 Local = %3 Remote = %5\r\n
0xb0010165 | Accept failed. Socket = %1 Local = %3 Remote = %5 Status = %6\r\n
0xb0010166 | Upper-level driver rejected the connection. Socket = %1 Status = %2\r\n
0xb0010190 | NDK disconnect event. Socket = %1 Local = %3 Remote = %5\r\n
0xb0010193 | Close started. Socket = %1 Local = %3 Remote = %5\r\n
0xb0010194 | Close completed. Socket = %1\r\n
0xb00101c2 | Out of send credits - starting credit grant timer. Socket = %1 Local = %3 Remote = %5\r\n
0xb00101c3 | Peer used their last send credit. Socket = %1 Local = %3 Remote = %5\r\n
0xb00101c4 | Using last send credit. Socket = %1 Local = %3 Remote = %5\r\n
0xb00101c5 | Timed-out while waiting to receive send credits. Socket = %1 Local = %3 Remote = %5\r\n
0xb00101c6 | Protocol violation - the peer sent a packet but does not have a send credit. Socket = %1 Local = %3 Remote = %5\r\n
0xb00101c7 | Protocol violation - the peer used their last send credit but did not grant a send credit. Socket = %1 Local = %3 Remote = %5\r\n
0xb00101c8 | Granted the peer %6 additional send credits. Socket %1 Local = %3 Remote = %5 PeerSendCredits = %7\r\n
0xb00101c9 | Received a grant of %6 credits. Socket = %1 Local = %3 Remote = %5 SendCreditsAccepted = %7 SendCredits = %8\r\n
0xb00101f4 | Failed to post a %6 SQ work request. Socket = %1 Local = %3 Remote = %5 Status = %7\r\n
0xb00101f5 | %6 SQ work request failed. Socket = %1 Local = %3 Remote = %5 Status = %7\r\n
0xb00101f6 | Failed to post a Receive work request. Socket = %1 Local = %3 Remote = %5 Status = %6\r\n
0xb00101f7 | Receive work request failed. Socket = %1 Local = %3 Remote = %5 Status = %6\r\n
0xb00103e8 | Timed-out out while waiting to receive a keepalive response. Socket = %1 Local = %3 Remote = %5\r\n
0xb00103e9 | Protocol violation - received packet is too small or contains at least one invalid value. Socket = %1 Local = %3 Remote = %5\r\n
0xb00103ea | Protocol violation - total fragmented payload is larger than indicated by first fragment. Socket = %1 Local = %3 Remote = %5\r\n
0xb00103eb | Protocol violation - total fragmented payload is smaller than indicated by first fragment. Socket = %1 Local = %3 Remote = %5\r\n
0xb00103ec | Failed to allocate a fragment reassembly buffer. Socket = %1 Local = %3 Remote = %5\r\n
0xb00103ed | %6 operation failed. Socket = %1 Local = %3 Remote = %5 Status = %7\r\n
0xb00103ee | Created socket. Socket = %1\r\n
0xb00103ef | Failed to create socket. Socket = %1 Status = %2\r\n
0xb00103f0 | Finished negotiating connection properties. Socket = %1 Local = %3 Remote = %5 ProtocolVersion = %6 MaxReadWriteSize = %7 MaxReceiveSize = %8 MaxFragmentedReceiveSize = %9 MaxSendSize = %10 MaxFragmentedSendSize = %11 IRD = %12 ORD = %13\r\n
0xb00103f1 | A completion queue has failed and is no longer indicating completions. Socket = %1 Local = %3 Remote = %5 Status = %6\r\n
0xb00103f2 | Updated SCQ interrupt moderation parameters. Socket = %1 Count = %2 IntervalInMicroSeconds = %3\r\n
0xb00103f3 | Updated RCQ interrupt moderation parameters. Socket = %1 Count = %2 IntervalInMicroSeconds = %3\r\n
0xb001251c | Opened network adapter '%1'. NdkMajorVer = %2 NdkMinorVer = %3 VendorId = %4 DeviceId = %5 MaxRegistrationSize = %6 MaxWindowSize = %7 FrmrPageCount = %8 MaxInitiatorRequestSge = %9 MaxReceiveRequestSge = %10 MaxReadRequestSge = %11 MaxTransferLength = %12 MaxInlineDataSize = %13 MaxInboundReadLimit = %14 MaxOutboundReadLimit = %15 MaxReceiveQueueDepth = %16 MaxInitiatorQueueDepth = %17 MaxSrqDepth = %18 MaxCqDepth = %19 LargeRequestThreshold = %20 MaxCallerData = %21 MaxCalleeData = %22 AdapterFlags = %23\r\n
0xb0012710 | Received negotiate request. Socket = %1 Local = %3 Remote = %5 MinVersion = %6 MaxVersion = %7 Reserved = %8 CreditsRequested = %9 PreferredSendSize = %10 MaxReceiveSize = %11 MaxFragmentReassemblyBufferSize = %12\r\n
0xb0012711 | Sending negotiate request. Socket = %1 Local = %3 Remote = %5 MinVersion = %6 MaxVersion = %7 Reserved = %8 CreditsRequested = %9 PreferredSendSize = %10 MaxReceiveSize = %11 MaxFragmentReassemblyBufferSize = %12\r\n
0xb0012712 | Received negotiate response. Socket = %1 Local = %3 Remote = %5 MinVersion = %6 MaxVersion = %7 NegotiatedVersion = %8 Reserved = %9 CreditsRequested = %10 CreditsGranted = %11 Status = %12 MaxReadWriteSize = %13 PreferredSendSize = %14 MaxReceiveSize = %15 MaxFragmentReassemblyBufferSize = %16\r\n
0xb0012713 | Sending negotiate response. Socket = %1 Local = %3 Remote = %5 MinVersion = %6 MaxVersion = %7 NegotiatedVersion = %8 Reserved = %9 CreditsRequested = %10 CreditsGranted = %11 Status = %12 MaxReadWriteSize = %13 PreferredSendSize = %14 MaxReceiveSize = %15 MaxFragmentReassemblyBufferSize = %16\r\n
0xb0012714 | Received data. Socket = %1 Local = %3 Remote = %5 CreditsRequested = %6 CreditsGranted = %7 Flags = %8 Reserved = %9 RemainingDataLength = %10 DataOffset = %11 DataLength = %12\r\n
0xb0012715 | Sending data. Socket = %1 Local = %3 Remote = %5 CreditsRequested = %6 CreditsGranted = %7 Flags = %8 Reserved = %9 RemainingDataLength = %10 DataOffset = %11 DataLength = %12\r\n
0xb0020191 | Disconnect started. Socket = %1 Local = %3 Remote = %5 State = %6\r\n
0xb0020192 | Disconnect completed. Socket = %1 Local = %3 Remote = %5\r\n
0xd0000001 | Initializing\r\n
0xd0000002 | Initialized\r\n
0xd0000003 | Connecting\r\n
0xd0000004 | Connected\r\n
0xd0000005 | Disconnecting\r\n
0xd0000006 | Disconnected\r\n
0xd0000007 | Send\r\n
0xd0000008 | Register\r\n
0xd0000009 | Invalidate\r\n
0xd000000a | Read\r\n
0xd000000b | Write\r\n
0xd000000c | Send\r\n
0xd000000d | Register\r\n
0xd000000e | Invalidate\r\n
0xd000000f | Read\r\n
0xd0000010 | Write\r\n
