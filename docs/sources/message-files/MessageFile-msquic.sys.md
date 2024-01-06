## msquic.sys

Path: %SystemRoot%\system32\drivers\msquic.sys

### 1.1.6.0

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb0000001 | [ lib] Initialized, PartitionCount=%1 DatapathFeatures=%2\r\n
0xb0000002 | [ lib] Uninitialized\r\n
0xb0000003 | [ lib] AddRef\r\n
0xb0000004 | [ lib] Release\r\n
0xb0000005 | [ lib] Shared server state initializing\r\n
0xb0000006 | Allocation of '%1' failed. (%2 bytes)\r\n
0xb0000007 | [ lib] Rundown, PartitionCount=%1 DatapathFeatures=%2\r\n
0xb0000008 | [ lib] ERROR, %1.\r\n
0xb0000009 | [ lib] ERROR, %1, %2.\r\n
0xb000000a | [ lib] ASSERT, %2:%1 - %3.\r\n
0xb000000b | [ api] Enter %1 (%2).\r\n
0xb000000c | [ api] Exit\r\n
0xb000000d | [ api] Exit %1\r\n
0xb000000e | [ api] Waiting on operation\r\n
0xb000000f | [ lib] Perf counters Rundown\r\n
0xb0000010 | [ lib] New SendRetryEnabled state, %1\r\n
0xb0000400 | [ reg][%1] Created, AppName=%2\r\n
0xb0000401 | [ reg][%1] Destroyed\r\n
0xb0000402 | [ reg][%1] Cleaning up\r\n
0xb0000403 | [ reg][%1] Rundown, AppName=%2\r\n
0xb0000404 | [ reg][%1] ERROR, %2.\r\n
0xb0000405 | [ reg][%1] ERROR, %2, %3.\r\n
0xb0000406 | [ reg][%1] Shutting down connections, Flags=%2, ErrorCode=%3\r\n
0xb0000800 | [wrkr][%1] Created, IdealProc=%2 Owner=%3\r\n
0xb0000801 | [wrkr][%1] Start\r\n
0xb0000802 | [wrkr][%1] Stop\r\n
0xb0000803 | [wrkr][%1] IsActive = %2, Arg = %3\r\n
0xb0000804 | [wrkr][%1] QueueDelay = %2\r\n
0xb0000805 | [wrkr][%1] Destroyed\r\n
0xb0000806 | [wrkr][%1] Cleaning up\r\n
0xb0000807 | [wrkr][%1] ERROR, %2.\r\n
0xb0000808 | [wrkr][%1] ERROR, %2, %3.\r\n
0xb0000c00 | [cnfg][%1] Created, Registration=%2\r\n
0xb0000c01 | [cnfg][%1] Destroyed\r\n
0xb0000c02 | [cnfg][%1] Cleaning up\r\n
0xb0000c04 | [cnfg][%1] Rundown, Registration=%2\r\n
0xb0000c05 | [cnfg][%1] ERROR, %2.\r\n
0xb0000c06 | [cnfg][%1] ERROR, %2, %3.\r\n
0xb0001000 | [list][%1] Created, Registration=%2\r\n
0xb0001001 | [list][%1] Destroyed\r\n
0xb0001002 | [list][%1] Started, Binding=%2, LocalAddr=%4\r\n
0xb0001003 | [list][%1] Stopped\r\n
0xb0001004 | [list][%1] Rundown, Registration=%2\r\n
0xb0001005 | [list][%1] ERROR, %2.\r\n
0xb0001006 | [list][%1] ERROR, %2, %3.\r\n
0xb0001400 | [conn][%1] Created, IsServer=%2, CorrelationId=%3\r\n
0xb0001401 | [conn][%1] Destroyed\r\n
0xb0001402 | [conn][%1] Handshake complete\r\n
0xb0001403 | [conn][%1] Scheduling: %2\r\n
0xb0001404 | [conn][%1] Execute: %2\r\n
0xb0001407 | [conn][%1] New Local IP: %3\r\n
0xb0001408 | [conn][%1] New Remote IP: %3\r\n
0xb0001409 | [conn][%1] Removed Local IP: %3\r\n
0xb000140a | [conn][%1] Removed Remote IP: %3\r\n
0xb000140b | [conn][%1] Assigned worker: %2\r\n
0xb000140c | [conn][%1] Handshake start\r\n
0xb000140d | [conn][%1] Registered with %2\r\n
0xb000140e | [conn][%1] Unregistered from %2\r\n
0xb000140f | [conn][%1] Transport Shutdown: %2 (Remote=%3) (QS=%4)\r\n
0xb0001410 | [conn][%1] App Shutdown: %2 (Remote=%3)\r\n
0xb0001411 | [conn][%1] Initialize complete\r\n
0xb0001412 | [conn][%1] Handle closed\r\n
0xb0001413 | [conn][%1] QUIC Version: %2\r\n
0xb0001414 | [conn][%1] OUT: BytesSent=%2 InFlight=%3 InFlightMax=%4 CWnd=%5 SSThresh=%6 ConnFC=%7 ISB=%8 PostedBytes=%9 SRtt=%10\r\n
0xb0001415 | [conn][%1] Send Blocked Flags: %2\r\n
0xb0001416 | [conn][%1] IN: BytesRecv=%2\r\n
0xb0001417 | [conn][%1] CUBIC: SlowStartThreshold=%2 K=%3 WindowMax=%4 WindowLastMax=%5\r\n
0xb0001418 | [conn][%1] Congestion event\r\n
0xb0001419 | [conn][%1] Persistent congestion event\r\n
0xb000141a | [conn][%1] Recovery complete\r\n
0xb000141b | [conn][%1] Rundown, IsServer=%2, CorrelationId=%3\r\n
0xb000141c | [conn][%1] (SeqNum=%2) New Source CID: %4\r\n
0xb000141d | [conn][%1] (SeqNum=%2) New Destination CID: %4\r\n
0xb000141e | [conn][%1] (SeqNum=%2) Removed Source CID: %4\r\n
0xb000141f | [conn][%1] (SeqNum=%2) Removed Destination CID: %4\r\n
0xb0001420 | [conn][%1] Setting loss detection %2 timer for %3 ms. (ProbeCount=%4)\r\n
0xb0001421 | [conn][%1] Cancelling loss detection timer.\r\n
0xb0001422 | [conn][%1] DROP packet Dst=%3 Src=%5 Reason=%6.\r\n
0xb0001423 | [conn][%1] DROP packet Dst=%4 Src=%6 Reason=%7, %2.\r\n
0xb0001424 | [conn][%1] ERROR, %2.\r\n
0xb0001425 | [conn][%1] ERROR, %2, %3.\r\n
0xb0001426 | [conn][%1] New packet keys created successfully.\r\n
0xb0001427 | [conn][%1] Key phase change (locally initiated=%2).\r\n
0xb0001428 | [conn][%1] STATS: SRtt=%2 CongestionCount=%3 PersistentCongestionCount=%4 SendTotalBytes=%5 RecvTotalBytes=%6\r\n
0xb0001429 | [conn][%1] Shutdown complete, PeerFailedToAcknowledged=%2.\r\n
0xb000142a | [conn][%1] Read Key Updated, %2.\r\n
0xb000142b | [conn][%1] Write Key Updated, %2.\r\n
0xb000142c | [conn][%1][TX][%2] %3 (%4 bytes)\r\n
0xb000142d | [conn][%1][RX][%2] %3 (%4 bytes)\r\n
0xb000142e | [conn][%1][TX][%2] %3 Lost: %4\r\n
0xb000142f | [conn][%1][TX][%2] %3 ACKed\r\n
0xb0001430 | [conn][%1] %2\r\n
0xb0001434 | [conn][%1] Queueing send flush, reason=%2\r\n
0xb0001435 | [conn][%1] OUT: StreamFC=%2 StreamSendWindow=%3\r\n
0xb0001436 | [conn][%1] STATS: SendTotalPackets=%2 SendSuspectedLostPackets=%3 SendSpuriousLostPackets=%4 RecvTotalPackets=%5 RecvReorderedPackets=%6 RecvDroppedPackets=%7 RecvDuplicatePackets=%8 RecvDecryptionFailures=%9\r\n
0xb0001437 | [conn][%1] Server app accepted resumption ticket\r\n
0xb0001438 | [conn][%1] Client VNI Compatible Version List: %3\r\n
0xb0001439 | [conn][%1] Client VNI Received Version List: %3\r\n
0xb000143a | [conn][%1] Server VNI Supported Version List: %3\r\n
0xb0001800 | [strm][%1] Created, Conn=%2 ID=%3 IsLocal=%4\r\n
0xb0001801 | [strm][%1] Destroyed\r\n
0xb0001802 | [strm][%1] Send Blocked Flags: %2\r\n
0xb0001803 | [strm][%1] Rundown, Conn=%2 ID=%3 IsLocal=%4\r\n
0xb0001804 | [strm][%1] Send State: %2\r\n
0xb0001805 | [strm][%1] Recv State: %2\r\n
0xb0001806 | [strm][%1] ERROR, %2.\r\n
0xb0001807 | [strm][%1] ERROR, %2, %3.\r\n
0xb0001808 | [strm][%1] %2\r\n
0xb0001c00 | [bind][%1] Created, Udp=%2 LocalAddr=%4 RemoteAddr=%6\r\n
0xb0001c01 | [bind][%1] Rundown, Udp=%2 LocalAddr=%4 RemoteAddr=%6\r\n
0xb0001c02 | [bind][%1] Destroyed\r\n
0xb0001c03 | [bind][%1] Cleaning up\r\n
0xb0001c04 | [bind][%1] DROP packet Dst=%3 Src=%5 Reason=%6.\r\n
0xb0001c05 | [bind][%1] DROP packet Dst=%4 Src=%6 Reason=%7, %2.\r\n
0xb0001c06 | [bind][%1] ERROR, %2.\r\n
0xb0001c07 | [bind][%1] ERROR, %2, %3.\r\n
0xb0001c08 | [bind][%1] Execute: %2\r\n
0xb0002000 | [ tls][%1] ERROR, %2.\r\n
0xb0002001 | [ tls][%1] ERROR, %2, %3.\r\n
0xb0002002 | [ tls][%1] %2\r\n
0xb0002401 | [data][%1] Send %2 bytes in %3 buffers (segment=%4) Dst=%6 Src=%8\r\n
0xb0002402 | [data][%1] Recv %2 bytes (segment=%3) Src=%5 Dst=%7\r\n
0xb0002403 | [data][%1] ERROR, %2.\r\n
0xb0002404 | [data][%1] ERROR, %2, %3.\r\n
0xb0002405 | [data][%1] Created, local=%3, remote=%5\r\n
0xb0002406 | [data][%1] Destroyed\r\n
0xb0002800 | %1\r\n
0xd0000001 | IDLE\r\n
0xd0000002 | QUEUED\r\n
0xd0000003 | PROCESSING\r\n
0xd0000004 | API\r\n
0xd0000005 | FLUSH_RECV\r\n
0xd0000006 | UNREACHABLE\r\n
0xd0000007 | FLUSH_STREAM_RECV\r\n
0xd0000008 | FLUSH_SEND\r\n
0xd0000009 | TLS_COMPLETE\r\n
0xd000000a | TIMER_EXPIRED\r\n
0xd000000b | TRACE_RUNDOWN\r\n
0xd000000c | VERSION_NEGOTIATION\r\n
0xd000000d | STATELESS_RESET\r\n
0xd000000e | RETRY\r\n
0xd000000f | API.CONN_CLOSE\r\n
0xd0000010 | API.CONN_SHUTDOWN\r\n
0xd0000011 | API.CONN_START\r\n
0xd0000012 | API.STRM_CLOSE\r\n
0xd0000013 | API.STRM_SHUTDOWN\r\n
0xd0000014 | API.STRM_START\r\n
0xd0000015 | API.STRM_SEND\r\n
0xd0000016 | API.STRM_RECV_COMPLETE\r\n
0xd0000017 | API.STRM_RECV_SET_ENABLED\r\n
0xd0000018 | API.SET_PARAM\r\n
0xd0000019 | API.GET_PARAM\r\n
0xd000001a | API.DATAGRAM_SEND\r\n
0xd000001b | TIMER.PACING\r\n
0xd000001c | TIMER.ACK_DELAY\r\n
0xd000001d | TIMER.LOSS_DETECTION\r\n
0xd000001e | TIMER.KEEP_ALIVE\r\n
0xd000001f | TIMER.IDLE\r\n
0xd0000020 | TIMER.SHUTDOWN\r\n
0xd0000021 | INITIAL\r\n
0xd0000022 | RACK\r\n
0xd0000023 | PROBE\r\n
0xd0000024 | DISABLED\r\n
0xd0000025 | STARTED\r\n
0xd0000026 | RESET\r\n
0xd0000027 | RESET_ACKED\r\n
0xd0000028 | FIN\r\n
0xd0000029 | FIN_ACKED\r\n
0xd000002a | DISABLED\r\n
0xd000002b | STARTED\r\n
0xd000002c | PAUSED\r\n
0xd000002d | STOPPED\r\n
0xd000002e | RESET\r\n
0xd000002f | FIN\r\n
0xd0000030 | VERSION_NEGOTIATION\r\n
0xd0000031 | INITIAL\r\n
0xd0000032 | ZERO_RTT\r\n
0xd0000033 | HANDSHAKE\r\n
0xd0000034 | RETRY\r\n
0xd0000035 | ONE_RTT\r\n
0xd0000036 | RACK\r\n
0xd0000037 | FACK\r\n
0xd0000038 | PROBE\r\n
0xd0000039 | SET_PARAM\r\n
0xd000003a | GET_PARAM\r\n
0xd000003b | REGISTRATION_OPEN\r\n
0xd000003c | REGISTRATION_CLOSE\r\n
0xd000003d | REGISTRATION_SHUTDOWN\r\n
0xd000003e | CONFIGURATION_OPEN\r\n
0xd000003f | CONFIGURATION_CLOSE\r\n
0xd0000040 | CONFIGURATION_LOAD_CREDENTIAL\r\n
0xd0000041 | LISTENER_OPEN\r\n
0xd0000042 | LISTENER_CLOSE\r\n
0xd0000043 | LISTENER_START\r\n
0xd0000044 | LISTENER_STOP\r\n
0xd0000045 | CONNECTION_OPEN\r\n
0xd0000046 | CONNECTION_CLOSE\r\n
0xd0000047 | CONNECTION_SHUTDOWN\r\n
0xd0000048 | CONNECTION_START\r\n
0xd0000049 | CONNECTION_SET_CONFIGURATION\r\n
0xd000004a | CONNECTION_SEND_RESUMPTION_TICKET\r\n
0xd000004b | STREAM_OPEN\r\n
0xd000004c | STREAM_CLOSE\r\n
0xd000004d | STREAM_START\r\n
0xd000004e | STREAM_SHUTDOWN\r\n
0xd000004f | STREAM_SEND\r\n
0xd0000050 | STREAM_RECEIVE_COMPLETE\r\n
0xd0000051 | STREAM_RECEIVE_SET_ENABLED\r\n
0xd0000052 | DATAGRAM_SEND\r\n
0xd0000053 | CONNECTION_FLAGS\r\n
0xd0000054 | STREAM_FLAGS\r\n
0xd0000055 | PROBE\r\n
0xd0000056 | LOSS\r\n
0xd0000057 | ACK\r\n
0xd0000058 | TRANSPORT_PARAMETERS\r\n
0xd0000059 | CONGESTION_CONTROL\r\n
0xd000005a | CONNECTION_FLOW_CONTROL\r\n
0xd000005b | NEW_KEY\r\n
0xd000005c | STREAM_FLOW_CONTROL\r\n
0xd000005d | STREAM_ID_FLOW_CONTROL\r\n
0xd000005e | AMPLIFICATION_PROTECTION\r\n
0xd000005f | SCHEDULING\r\n

### 10.0.19041.1, 10.0.19041.488

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb0000001 | [ lib] Initialized, PartitionCount=%1 DatapathFeatures=%2\r\n
0xb0000002 | [ lib] Uninitialized\r\n
0xb0000003 | [ lib] AddRef\r\n
0xb0000004 | [ lib] Release\r\n
0xb0000005 | [ lib] Shared worker pool initializing\r\n
0xb0000006 | Allocation of '%1' failed. (%2 bytes)\r\n
0xb0000007 | [ lib] Rundown, PartitionCount=%1 DatapathFeatures=%2\r\n
0xb0000008 | [ lib] ERROR, %1.\r\n
0xb0000009 | [ lib] ERROR, %1, %2.\r\n
0xb000000a | [ lib] ASSERT, %2:%1 - %3.\r\n
0xb0000400 | [ reg][%1] Created, AppName=%2\r\n
0xb0000401 | [ reg][%1] Destroyed\r\n
0xb0000402 | [ reg][%1] Cleaning up\r\n
0xb0000403 | [ reg][%1] Rundown, AppName=%2\r\n
0xb0000404 | [ reg][%1] ERROR, %2.\r\n
0xb0000405 | [ reg][%1] ERROR, %2, %3.\r\n
0xb0000800 | [wrkr][%1] Created, IdealProc=%2 Owner=%3\r\n
0xb0000801 | [wrkr][%1] Start\r\n
0xb0000802 | [wrkr][%1] Stop\r\n
0xb0000803 | [wrkr][%1] IsActive = %2, Arg = %3\r\n
0xb0000804 | [wrkr][%1] QueueDelay = %2\r\n
0xb0000805 | [wrkr][%1] Destroyed\r\n
0xb0000806 | [wrkr][%1] Cleaning up\r\n
0xb0000807 | [wrkr][%1] ERROR, %2.\r\n
0xb0000808 | [wrkr][%1] ERROR, %2, %3.\r\n
0xb0000c00 | [sess][%1] Created, Registration=%2, Alpn=%3\r\n
0xb0000c01 | [sess][%1] Destroyed\r\n
0xb0000c02 | [sess][%1] Cleaning up\r\n
0xb0000c03 | [sess][%1] Shutting down connections, Flags=%2, ErrorCode=%3\r\n
0xb0000c04 | [sess][%1] Rundown, Registration=%2, Alpn=%3\r\n
0xb0000c05 | [sess][%1] ERROR, %2.\r\n
0xb0000c06 | [sess][%1] ERROR, %2, %3.\r\n
0xb0001000 | [list][%1] Created, Session=%2\r\n
0xb0001001 | [list][%1] Destroyed\r\n
0xb0001002 | [list][%1] Started, Binding=%2, LocalAddr=%4\r\n
0xb0001003 | [list][%1] Stopped\r\n
0xb0001004 | [list][%1] Rundown, Session=%2\r\n
0xb0001005 | [list][%1] ERROR, %2.\r\n
0xb0001006 | [list][%1] ERROR, %2, %3.\r\n
0xb0001400 | [conn][%1] Created, IsServer=%2\r\n
0xb0001401 | [conn][%1] Destroyed\r\n
0xb0001402 | [conn][%1] Handshake complete\r\n
0xb0001403 | [conn][%1] Scheduling: %2\r\n
0xb0001404 | [conn][%1] Execute: %2\r\n
0xb0001407 | [conn][%1] New Local IP: %3\r\n
0xb0001408 | [conn][%1] New Remote IP: %3\r\n
0xb0001409 | [conn][%1] Removed Local IP: %3\r\n
0xb000140a | [conn][%1] Removed Remote IP: %3\r\n
0xb000140b | [conn][%1] Assigned worker: %2\r\n
0xb000140c | [conn][%1] Handshake start\r\n
0xb000140d | [conn][%1] Registered with session: %2\r\n
0xb000140e | [conn][%1] Unregistered from session: %2\r\n
0xb000140f | [conn][%1] Transport Shutdown: %2 (Remote=%3) (QS=%4)\r\n
0xb0001410 | [conn][%1] App Shutdown: %2 (Remote=%3)\r\n
0xb0001411 | [conn][%1] Initialize complete\r\n
0xb0001412 | [conn][%1] Handle closed\r\n
0xb0001413 | [conn][%1] Version = %2\r\n
0xb0001414 | [conn][%1] OUT: BytesSent=%2 InFlight=%3 InFlightMax=%4 CWnd=%5 SSThresh=%6 ConnFC=%7 StreamFC=%8 ISB=%9 PostedBytes=%10 SRtt=%11\r\n
0xb0001415 | [conn][%1] Send Blocked Flags: %2\r\n
0xb0001416 | [conn][%1] IN: BytesRecv=%2\r\n
0xb0001417 | [conn][%1] CUBIC: SlowStartThreshold=%2 K=%3 WindowMax=%4 WindowLastMax=%5\r\n
0xb0001418 | [conn][%1] Congestion event\r\n
0xb0001419 | [conn][%1] Persistent congestion event\r\n
0xb000141a | [conn][%1] Recovery complete\r\n
0xb000141b | [conn][%1] Rundown, IsServer=%2\r\n
0xb000141c | [conn][%1] New Source CID: %3\r\n
0xb000141d | [conn][%1] New Destination CID: %3\r\n
0xb000141e | [conn][%1] Removed Source CID: %3\r\n
0xb000141f | [conn][%1] Removed Destination CID: %3\r\n
0xb0001420 | [conn][%1] Setting loss detection %2 timer for %3 ms. (ProbeCount=%4)\r\n
0xb0001421 | [conn][%1] Cancelling loss detection timer.\r\n
0xb0001422 | [conn][%1] DROP packet[%2] Src=%6 Dst=%5 Reason=%7.\r\n
0xb0001423 | [conn][%1] DROP packet[%2] Src=%7 Dst=%6 Reason=%8, %3.\r\n
0xb0001424 | [conn][%1] ERROR, %2.\r\n
0xb0001425 | [conn][%1] ERROR, %2, %3.\r\n
0xb0001426 | [conn][%1] New packet keys created successfully.\r\n
0xb0001427 | [conn][%1] Key phase change (locally initiated=%2).\r\n
0xb0001428 | [conn][%1] STATS: LifeTimeUs=%2 SendTotalPackets=%3 SendSuspectedLostPackets=%4 SendSpuriousLostPackets=%5 RecvTotalPackets=%6 RecvReorderedPackets=%7 RecvDroppedPackets=%8 RecvDuplicatePackets=%9 RecvDecryptionFailures=%10 CongestionCount=%11 PersistentCongestionCount=%12 SendTotalBytes=%13 RecvTotalBytes=%14\r\n
0xb0001429 | [conn][%1] Shutdown complete, PeerFailedToAcknowledged=%2.\r\n
0xb000142a | [conn][%1] Read Key Updated, %2.\r\n
0xb000142b | [conn][%1] Write Key Updated, %2.\r\n
0xb000142c | [conn][%1][TX][%2] %3 (%4 bytes)\r\n
0xb000142d | [conn][%1][RX][%2] %3 (%4 bytes)\r\n
0xb000142e | [conn][%1][TX][%2] %3 Lost: %4\r\n
0xb000142f | [conn][%1][TX][%2] %3 ACKed\r\n
0xb0001800 | [strm][%1] Created, Conn=%2 ID=%3 IsLocal=%4\r\n
0xb0001801 | [strm][%1] Destroyed\r\n
0xb0001802 | [strm][%1] Send Blocked Flags: %2\r\n
0xb0001803 | [strm][%1] Rundown, Conn=%2 ID=%3 IsLocal=%4\r\n
0xb0001804 | [strm][%1] Send State: %2\r\n
0xb0001805 | [strm][%1] Recv State: %2\r\n
0xb0001806 | [strm][%1] ERROR, %2.\r\n
0xb0001807 | [strm][%1] ERROR, %2, %3.\r\n
0xb0001c00 | [bind][%1] Created, Udp=%2 LocalAddr=%5 RemoteAddr=%6\r\n
0xb0001c01 | [bind][%1] Rundown, Udp=%2 LocalAddr=%5 RemoteAddr=%6\r\n
0xb0001c02 | [bind][%1] Destroyed\r\n
0xb0001c03 | [bind][%1] Cleaning up\r\n
0xb0001c04 | [bind][%1] DROP packet[%2] Src=%6 Dst=%5 Reason=%7.\r\n
0xb0001c05 | [bind][%1] DROP packet[%2] Src=%7 Dst=%6 Reason=%8, %3.\r\n
0xb0001c06 | [bind][%1] ERROR, %2.\r\n
0xb0001c07 | [bind][%1] ERROR, %2, %3.\r\n
0xb0001c08 | [bind][%1] Execute: %2\r\n
0xb0002000 | [ tls][%1] ERROR, %2.\r\n
0xb0002001 | [ tls][%1] ERROR, %2, %3.\r\n
0xb00023ff | [mitls] %1\r\n
0xb0002400 | [ udp][%1] Send %2 bytes in %3 buffers (segment=%4) Dst=%6\r\n
0xb0002401 | [ udp][%1] Send %2 bytes in %3 buffers (segment=%4) Src=%8 Dst=%7\r\n
0xb0002402 | [ udp][%1] Recv %2 bytes (segment=%3) Src=%4 Dst=%5\r\n
0xb0002403 | [ udp][%1] ERROR, %2.\r\n
0xb0002404 | [ udp][%1] ERROR, %2, %3.\r\n
0xd0000001 | IDLE\r\n
0xd0000002 | QUEUED\r\n
0xd0000003 | PROCESSING\r\n
0xd0000004 | API\r\n
0xd0000005 | FLUSH_RECV\r\n
0xd0000006 | UNREACHABLE\r\n
0xd0000007 | FLUSH_STREAM_RECV\r\n
0xd0000008 | FLUSH_SEND\r\n
0xd0000009 | TLS_COMPLETE\r\n
0xd000000a | TIMER_EXPIRED\r\n
0xd000000b | TRACE_RUNDOWN\r\n
0xd000000c | VERSION_NEGOTIATION\r\n
0xd000000d | STATELESS_RESET\r\n
0xd000000e | RETRY\r\n
0xd000000f | API.CONN_OPEN\r\n
0xd0000010 | API.CONN_CLOSE\r\n
0xd0000011 | API.CONN_SHUTDOWN\r\n
0xd0000012 | API.CONN_START\r\n
0xd0000013 | API.STRM_OPEN\r\n
0xd0000014 | API.STRM_CLOSE\r\n
0xd0000015 | API.STRM_SHUTDOWN\r\n
0xd0000016 | API.STRM_START\r\n
0xd0000017 | API.STRM_SEND\r\n
0xd0000018 | API.STRM_RECV_COMPLETE\r\n
0xd0000019 | API.SET_PARAM\r\n
0xd000001a | API.GET_PARAM\r\n
0xd000001b | TIMER.PACING\r\n
0xd000001c | TIMER.ACK_DELAY\r\n
0xd000001d | TIMER.LOSS_DETECTION\r\n
0xd000001e | TIMER.KEEP_ALIVE\r\n
0xd000001f | TIMER.IDLE\r\n
0xd0000020 | TIMER.SHUTDOWN\r\n
0xd0000021 | CRYPTO\r\n
0xd0000022 | RACK\r\n
0xd0000023 | PROBE\r\n
0xd0000024 | DISABLED\r\n
0xd0000025 | STARTED\r\n
0xd0000026 | RESET\r\n
0xd0000027 | RESET_ACKED\r\n
0xd0000028 | FIN\r\n
0xd0000029 | FIN_ACKED\r\n
0xd000002a | DISABLED\r\n
0xd000002b | STARTED\r\n
0xd000002c | PAUSED\r\n
0xd000002d | STOPPED\r\n
0xd000002e | RESET\r\n
0xd000002f | FIN\r\n
0xd0000030 | VERSION_NEGOTIATION\r\n
0xd0000031 | INITIAL\r\n
0xd0000032 | ZERO_RTT\r\n
0xd0000033 | HANDSHAKE\r\n
0xd0000034 | RETRY\r\n
0xd0000035 | ONE_RTT\r\n
0xd0000036 | RACK\r\n
0xd0000037 | FACK\r\n
