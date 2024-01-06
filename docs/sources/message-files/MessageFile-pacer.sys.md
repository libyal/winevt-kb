## pacer.sys

Path: %SystemRoot%\system32\drivers\pacer.sys

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x90000001 | Microsoft-Windows-QoS-Pacer\r\n
0xb0000001 | Create %2 at %3 bytes/sec with status %1\r\n
0xb0000002 | Update %2 from %3 to %11 with status %1\r\n
0xb0000003 | Start Pacer on NetLuid=%1 (%3)\r\n
0xb0000004 | Stop Pacer on NetLuid=%1 (%3)\r\n
0xb0000005 | Update %1 from %2 to %10\r\n
0xd0000001 | GQoS Flow\r\n
0xd0000002 | TC Flow\r\n
0xd0000003 | EQoS Flow\r\n

### 6.1.7600.16385, 6.1.7601.17514

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | Create %2 at %3 bytes/sec with status %1\r\n
0xb0000002 | Update %2 from %3 to %11 with status %1\r\n
0xb0000003 | Start Pacer on NetLuid=%1 (%3)\r\n
0xb0000004 | Stop Pacer on NetLuid=%1 (%3)\r\n
0xb0000005 | Update %1 from %2 to %10\r\n
0xb0000006 | PACER: Flow deleted (dropped=%1, scheduled=%2/%4, transmitted=%3/%5, nbl=%7/%6)\r\n
0xb0000007 | PACER: Packet dropped, reason=%1\r\n
0xb0000008 | PACER: Non-conformance marking, dscp=%1, 802.1p=%2, WMM=%3\r\n
0xb0000009 | PACER: Application-based DSCP marking policy state=%1\r\n
0xb000000a | PACER: Packet rescheduled (eligible=%1/%2, first-delta=%3, last-delta=%4)\r\n
0xb0010001 | PACER: Flow created with status %1 (type=%2, rate=%3Bps, service=%8, dscp=%11, 802.1p=%12, system=%15)\r\n
0xb0010002 | PACER: Flow updated with status %1 (rate=%3Bps, service=%8, dscp=%11, 802.1p=%12)\r\n
0xb0010003 | PACER: Starting adapter %4 (luid=%1)\r\n
0xb0010004 | PACER: Stopping adapter %4 (luid=%1)\r\n
0xd0000001 | GQoS\r\n
0xd0000002 | TC\r\n
0xd0000003 | EQoS\r\n
0xd0000004 | Full\r\n
0xd0000005 | IDP\r\n
0xd0000006 | NOTRAFFIC\r\n
0xd0000007 | BESTEFFORT\r\n
0xd0000008 | CONTROLLEDLOAD\r\n
0xd0000009 | GUARANTEED\r\n
0xd000000a | NETWORK_UNAVAILABLE\r\n
0xd000000b | GENERAL_INFORMATION\r\n
0xd000000c | NOCHANGE\r\n
0xd000000d | NONCONFORMING\r\n
0xd000000e | NETWORK_CONTROL\r\n
0xd000000f | QUALITATIVE\r\n
0xd0000010 | Non-conformance\r\n
0xd0000011 | Excessive delay\r\n

### 6.2.9200.16384, 6.3.9600.16384, 6.3.9600.17415, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.19041.546, 10.0.22000.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb0000001 | Create %2 at %3 bytes/sec with status %1\r\n
0xb0000002 | Update %2 from %3 to %11 with status %1\r\n
0xb0000003 | Start Pacer on NetLuid=%1 (%3)\r\n
0xb0000004 | Stop Pacer on NetLuid=%1 (%3)\r\n
0xb0000005 | Update %1 from %2 to %10\r\n
0xb0000006 | PACER: Flow deleted (dropped=%1, scheduled=%2/%4, transmitted=%3/%5, nbl=%7/%6)\r\n
0xb0000007 | PACER: Packet dropped, reason=%1\r\n
0xb0000008 | PACER: Non-conformance marking, dscp=%1, 802.1p=%2, WMM=%3\r\n
0xb0000009 | PACER: Application-based DSCP marking policy state=%1\r\n
0xb000000b | PACER: CurrentTime= %1 BytesSent= %2 BytesDropped= %3 NewSendWindow= %4 MinSendWindow= %5\r\n
0xb000000c | PACER: NetLuid= %1 CurrentTime= %2 ActiveFlows= %3 ActiveWeight= %4 NewSendWindow= %5\r\n
0xb000000d | PACER: FlowConformanceEventId= %1 CurrentTime= %2 LastConformanceTime= %3 PeakConformanceTime= %4 Tokens= %5 MaxTokens= %6 Rate= %7 LastConformanceCredits= %8\r\n
0xb000000e | PACER: FlowSendQueueEventId= %1 CurrentTime= %2 IdleTime= %3 DelayTime= %4 BytesRequested= %5 BytesSent= %6 BytesQueued= %7\r\n
0xb000000f | PACER: TimerId= %1 EventId= %2 CurrentTime= %3 SetTime= %4 RunTime= %5 FlowsProcessed= %6 NblsSent= %7 NblsDropped= %8 Flags= %9\r\n
0xb0000010 | PACER: NetLuid= %1 CurrentTime= %2 BytesRequested= %3 BytesCompleted= %4 BytesInQueue= %5 BufferAvailable= %6 AlphaTerm= %8 BetaTerm= %7 DeltaSendWindow= %9 NewSendWindow= %10\r\n
0xb0010001 | PACER: Flow created with status %1 (type=%2, rate=%3Bps, service=%8, dscp=%11, 802.1p=%12, system=%15)\r\n
0xb0010002 | PACER: Flow updated with status %1 (rate=%3Bps, service=%8, dscp=%11, 802.1p=%12)\r\n
0xb0010003 | PACER: Starting adapter %4 (luid=%1)\r\n
0xb0010004 | PACER: Stopping adapter %4 (luid=%1)\r\n
0xd0000001 | GQoS\r\n
0xd0000002 | TC\r\n
0xd0000003 | EQoS\r\n
0xd0000004 | Full\r\n
0xd0000005 | IDP\r\n
0xd0000006 | NOTRAFFIC\r\n
0xd0000007 | BESTEFFORT\r\n
0xd0000008 | CONTROLLEDLOAD\r\n
0xd0000009 | GUARANTEED\r\n
0xd000000a | NETWORK_UNAVAILABLE\r\n
0xd000000b | GENERAL_INFORMATION\r\n
0xd000000c | NOCHANGE\r\n
0xd000000d | NONCONFORMING\r\n
0xd000000e | NETWORK_CONTROL\r\n
0xd000000f | QUALITATIVE\r\n
0xd0000010 | Non-conformance\r\n
0xd0000011 | Excessive delay\r\n
0xd0000012 | Allocation failure\r\n
0xd0000013 | Packet assembly failure\r\n
0xd0000014 | Send NBL failure\r\n
0xd0000015 | Process Queue failure\r\n
0xd0000016 | Update Flow failure\r\n
0xd0000017 | Rate match\r\n
0xd0000018 | Recompute\r\n
0xd0000019 | Update\r\n
0xd000001a | Set\r\n
0xd000001b | PreSend\r\n
0xd000001c | PostSend\r\n
0xd000001d | Idle\r\n
0xd000001e | SendRequest\r\n
0xd000001f | DelayedSend\r\n
0xd0000020 | TimerSet\r\n
0xd0000021 | TimerExpired\r\n
0xd0000022 | TimerStopped\r\n
