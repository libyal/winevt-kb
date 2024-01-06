## tcpip.sys

Path: %SystemRoot%\system32\drivers\tcpip.sys

### 6.1.7600.16385, 6.1.7601.17802

Message identifier | Message string
--- | ---
0x11000034 | SQM\r\n
0x30000000 | Info\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 posted %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Source = %4, Destination = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | DisconnectTimer\r\n
0xd000002c | SwsTimer\r\n
0xd000002d | ReassemblyRateTimer\r\n
0xd000002e | SynOrRstValidationTimer\r\n
0xd000002f | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000030 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000031 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000032 | TCP_KEEPALIVE\r\n
0xd0000033 | TCP_MAXSEG\r\n
0xd0000034 | TCP_MAXRT\r\n
0xd0000035 | TCP_STDURG\r\n
0xd0000036 | TCP_NOURG\r\n
0xd0000037 | TCP_ATMARK\r\n
0xd0000038 | TCP_NOSYNRETRIES\r\n
0xd0000039 | TCP_TIMESTAMPS\r\n
0xd000003a | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003b | TCP_CONGESTION_ALGORITHM\r\n
0xd000003c | TCP_DELAY_FIN_ACK\r\n
0xd000003d | SO_DEBUG\r\n
0xd000003e | SO_ACCEPTCONN\r\n
0xd000003f | SO_REUSEADDR\r\n
0xd0000040 | SO_KEEPALIVE\r\n
0xd0000041 | SO_DONTROUTE\r\n
0xd0000042 | SO_BROADCAST\r\n
0xd0000043 | SO_USELOOPBACK\r\n
0xd0000044 | SO_LINGER\r\n
0xd0000045 | SO_OOBINLINE\r\n
0xd0000046 | SO_SNDBUF\r\n
0xd0000047 | SO_RCVBUF\r\n
0xd0000048 | SO_CONDITIONAL_ACCEPT\r\n
0xd0000049 | SO_PAUSE_ACCEPT\r\n
0xd000004a | SO_COMPARTMENT_ID\r\n
0xd000004b | SO_RANDOMIZE_PORT\r\n
0xd000004c | SO_PORT_SCALABILITY\r\n
0xd000004d | NldsInvalid\r\n
0xd000004e | NldsTentative\r\n
0xd000004f | NldsDuplicate\r\n
0xd0000050 | NldsDeprecated\r\n
0xd0000051 | Indicate\r\n
0xd0000052 | Pend\r\n
0xd0000053 | Satisfy\r\n
0xd0000054 | NdisPhysicalMediumUnspecified\r\n
0xd0000055 | NdisPhysicalMediumWirelessLan\r\n
0xd0000056 | NdisPhysicalMediumCableModem\r\n
0xd0000057 | NdisPhysicalMediumPhoneLine\r\n
0xd0000058 | NdisPhysicalMediumDSL\r\n
0xd0000059 | NdisPhysicalMedium1394\r\n
0xd000005a | NdisPhysicalMediumWirelessWan\r\n
0xd000005b | NdisPhysicalMediumNative802_11\r\n
0xd000005c | NdisPhysicalMediumBluetooth\r\n
0xd000005d | NdisPhysicalMediumInfiniband\r\n
0xd000005e | NdisPhysicalMediumWiMax\r\n
0xd000005f | NdisPhysicalMedium802_3\r\n
0xd0000060 | NdisPhysicalMedium802_5\r\n
0xd0000061 | NdisPhysicalMediumIrda\r\n
0xd0000062 | NdisPhysicalMediumWiredWAN\r\n
0xd0000063 | IP checksum offload not computed\r\n
0xd0000064 | TCP checksum offload not computed\r\n
0xd0000065 | UDP checksum offload not computed\r\n
0xd0000066 | Header not aligned on 4-byte boundary\r\n
0xd0000067 | IP fragmentation\r\n
0xd0000068 | Source address is not unicast\r\n
0xd0000069 | Destination address is not unicast\r\n
0xd000006a | Ethernet and IP header not contiguous\r\n
0xd000006b | IP options present\r\n
0xd000006c | ESP over UDP\r\n
0xd000006d | Lack contiguous space for upper layer headers\r\n
0xd000006e | WFP filters present\r\n
0xd000006f | Nexthop is unavailable\r\n
0xd0000070 | Path has been invalidated due to policy change\r\n
0xd0000071 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000072 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000073 | Session state is not compatible\r\n
0xd0000074 | Failed to allocate the WSD cache\r\n
0xd0000075 | Failure initializing PnP work queue\r\n
0xd0000076 | Failed to get persistent parameters\r\n
0xd0000077 | Rejected persistent parameters\r\n
0xd0000078 | qualified profile\r\n
0xd0000079 | qualified destination\r\n
0xd000007a | sample collection completion\r\n
0xd000007b | idle time expiration\r\n
0xd000007c | allocation\r\n
0xd000007d | new sample request\r\n
0xd000007e | configuration change\r\n
0xd000007f | Idle\r\n
0xd0000080 | ProbingWs\r\n
0xd0000081 | ProbeWait\r\n
0xd0000082 | ProbingWithoutWs\r\n
0xd0000083 | RecordWait\r\n
0xd0000084 | EreQualified\r\n
0xd0000085 | Qualified\r\n
0xd0000086 | Destination is multicast\r\n
0xd0000087 | Header is invalid\r\n
0xd0000088 | Checksum is invalid\r\n
0xd0000089 | Transport endpoint was not found\r\n
0xd000008a | Connected path error\r\n
0xd000008b | Session state error\r\n
0xd000008c | Bad source address\r\n
0xd000008d | Not locally destined\r\n
0xd000008e | Protocol unreachable\r\n
0xd000008f | Port unreachable\r\n
0xd0000090 | Bad length\r\n
0xd0000091 | Malformed Header\r\n
0xd0000092 | No route available\r\n
0xd0000093 | Beyond scope\r\n
0xd0000094 | Inspection drop\r\n
0xd0000095 | Too many decapsulations\r\n
0xd0000096 | Administratively prohibited\r\n
0xd0000097 | Hop limit exceeded\r\n
0xd0000098 | Address unreachable\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x11000034 | SQM\r\n
0x30000000 | Info\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 posted %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Source = %4, Destination = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto=%3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm=%6, MaxDataRetransmissions=%7, DelayedAckTicks=%8 msec.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, Status = %7.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3.\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick= %4 Time= %5.\r\n
0xb0000527 | %1 rescheduled by processor %2 for processor %3 at %4 from %5 to %6.\r\n
0xb0000528 | %1 fired on processor %2 at Tick= %3, scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | DisconnectTimer\r\n
0xd000002c | SwsTimer\r\n
0xd000002d | ReassemblyRateTimer\r\n
0xd000002e | SynOrRstValidationTimer\r\n
0xd000002f | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000030 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000031 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000032 | TCP_KEEPALIVE\r\n
0xd0000033 | TCP_MAXSEG\r\n
0xd0000034 | TCP_MAXRT\r\n
0xd0000035 | TCP_STDURG\r\n
0xd0000036 | TCP_NOURG\r\n
0xd0000037 | TCP_ATMARK\r\n
0xd0000038 | TCP_NOSYNRETRIES\r\n
0xd0000039 | TCP_TIMESTAMPS\r\n
0xd000003a | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003b | TCP_CONGESTION_ALGORITHM\r\n
0xd000003c | TCP_DELAY_FIN_ACK\r\n
0xd000003d | SO_DEBUG\r\n
0xd000003e | SO_ACCEPTCONN\r\n
0xd000003f | SO_REUSEADDR\r\n
0xd0000040 | SO_KEEPALIVE\r\n
0xd0000041 | SO_DONTROUTE\r\n
0xd0000042 | SO_BROADCAST\r\n
0xd0000043 | SO_USELOOPBACK\r\n
0xd0000044 | SO_LINGER\r\n
0xd0000045 | SO_OOBINLINE\r\n
0xd0000046 | SO_SNDBUF\r\n
0xd0000047 | SO_RCVBUF\r\n
0xd0000048 | SO_CONDITIONAL_ACCEPT\r\n
0xd0000049 | SO_PAUSE_ACCEPT\r\n
0xd000004a | SO_COMPARTMENT_ID\r\n
0xd000004b | SO_RANDOMIZE_PORT\r\n
0xd000004c | SO_PORT_SCALABILITY\r\n
0xd000004d | NldsInvalid\r\n
0xd000004e | NldsTentative\r\n
0xd000004f | NldsDuplicate\r\n
0xd0000050 | NldsDeprecated\r\n
0xd0000051 | Indicate\r\n
0xd0000052 | Pend\r\n
0xd0000053 | Satisfy\r\n
0xd0000054 | NdisPhysicalMediumUnspecified\r\n
0xd0000055 | NdisPhysicalMediumWirelessLan\r\n
0xd0000056 | NdisPhysicalMediumCableModem\r\n
0xd0000057 | NdisPhysicalMediumPhoneLine\r\n
0xd0000058 | NdisPhysicalMediumDSL\r\n
0xd0000059 | NdisPhysicalMedium1394\r\n
0xd000005a | NdisPhysicalMediumWirelessWan\r\n
0xd000005b | NdisPhysicalMediumNative802_11\r\n
0xd000005c | NdisPhysicalMediumBluetooth\r\n
0xd000005d | NdisPhysicalMediumInfiniband\r\n
0xd000005e | NdisPhysicalMediumWiMax\r\n
0xd000005f | NdisPhysicalMedium802_3\r\n
0xd0000060 | NdisPhysicalMedium802_5\r\n
0xd0000061 | NdisPhysicalMediumIrda\r\n
0xd0000062 | NdisPhysicalMediumWiredWAN\r\n
0xd0000063 | IP checksum offload not computed\r\n
0xd0000064 | TCP checksum offload not computed\r\n
0xd0000065 | UDP checksum offload not computed\r\n
0xd0000066 | Header not aligned on 4-byte boundary\r\n
0xd0000067 | IP fragmentation\r\n
0xd0000068 | Source address is not unicast\r\n
0xd0000069 | Destination address is not unicast\r\n
0xd000006a | Ethernet and IP header not contiguous\r\n
0xd000006b | IP options present\r\n
0xd000006c | ESP over UDP\r\n
0xd000006d | Lack contiguous space for upper layer headers\r\n
0xd000006e | WFP filters present\r\n
0xd000006f | Nexthop is unavailable\r\n
0xd0000070 | Path has been invalidated due to policy change\r\n
0xd0000071 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000072 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000073 | Session state is not compatible\r\n
0xd0000074 | TCP options present\r\n
0xd0000075 | UDP IPv6 checksum absent in packet\r\n
0xd0000076 | Packet is for a loopback interface\r\n
0xd0000077 | Failed to allocate the WSD cache\r\n
0xd0000078 | Failure initializing PnP work queue\r\n
0xd0000079 | Failed to get persistent parameters\r\n
0xd000007a | Rejected persistent parameters\r\n
0xd000007b | qualified profile\r\n
0xd000007c | qualified destination\r\n
0xd000007d | sample collection completion\r\n
0xd000007e | idle time expiration\r\n
0xd000007f | allocation\r\n
0xd0000080 | new sample request\r\n
0xd0000081 | configuration change\r\n
0xd0000082 | Idle\r\n
0xd0000083 | ProbingWs\r\n
0xd0000084 | ProbeWait\r\n
0xd0000085 | ProbingWithoutWs\r\n
0xd0000086 | RecordWait\r\n
0xd0000087 | EreQualified\r\n
0xd0000088 | Qualified\r\n
0xd0000089 | Destination is multicast\r\n
0xd000008a | Header is invalid\r\n
0xd000008b | Checksum is invalid\r\n
0xd000008c | Transport endpoint was not found\r\n
0xd000008d | Connected path error\r\n
0xd000008e | Session state error\r\n
0xd000008f | Bad source address\r\n
0xd0000090 | Not locally destined\r\n
0xd0000091 | Protocol unreachable\r\n
0xd0000092 | Port unreachable\r\n
0xd0000093 | Bad length\r\n
0xd0000094 | Malformed Header\r\n
0xd0000095 | No route available\r\n
0xd0000096 | Beyond scope\r\n
0xd0000097 | Inspection drop\r\n
0xd0000098 | Too many decapsulations\r\n
0xd0000099 | Administratively prohibited\r\n
0xd000009a | Hop limit exceeded\r\n
0xd000009b | Address unreachable\r\n
0xd000009c | Fragment MTU exceeded\r\n
0xd000009d | Buffer Length Exceeded\r\n
0xd000009e | Address Resolution Timeout\r\n
0xd000009f | Address Resolution Failure\r\n
0xd00000a0 | IPsec failure\r\n
0xd00000a1 | Extension Headers Failure\r\n
0xd00000a2 | Allocation Failure\r\n
0xd00000a3 | Default\r\n
0xd00000a4 | NewReno\r\n
0xd00000a5 | CcmCtcp\r\n
0xd00000a6 | CcmDctcp\r\n
0xd00000a7 | TcpTemplateTypeInternet\r\n
0xd00000a8 | TcpTemplateTypeDatacenter\r\n
0xd00000a9 | TcpTemplateTypeCompat\r\n
0xd00000aa | TcpTemplateTypeCustom\r\n
0xd00000ab | TcpTemplateTypeDefault\r\n
0xd00000ac | TcpTemplateTypeAutomatic\r\n
0xd00000ad | No Failure\r\n
0xd00000ae | Unknown\r\n
0xd00000af | System Policy\r\n
0xd00000b0 | NIC Capacity Reached\r\n
0xd00000b1 | System Low On Memory\r\n
0xd00000b2 | WFP driver / Stream inspection\r\n
0xd00000b3 | Weak Host Model Enabled\r\n
0xd00000b4 | Forwarding Enabled\r\n
0xd00000b5 | Hardware capability\r\n
0xd00000b6 | NDIS filter/NIC property\r\n
0xd00000b7 | Loopback fast path socket option not set on both ends\r\n
0xd00000b8 | Filter policy existed for the loopback connection\r\n
0xd00000b9 | IPv4\r\n
0xd00000ba | IPv6\r\n
0xd00000bb | unbind\r\n
0xd00000bc | bind\r\n
0xd00000bd | port change\r\n
0xd00000be | none\r\n
0xd00000bf | receive hash\r\n
0xd00000c0 | receive scale\r\n
0xd00000c1 | enabled\r\n
0xd00000c2 | disabled\r\n
0xd00000c3 | removing\r\n
0xd00000c4 | adding\r\n
0xd00000c5 | complete binding initialization\r\n
0xd00000c6 | complete port initialization\r\n
0xd00000c7 | enumerate interface ports\r\n
0xd00000c8 | query port link state\r\n
0xd00000c9 | query port interface index\r\n
0xd00000ca | query interface ports\r\n
0xd00000cb | query port RSS capabilities\r\n
0xd00000cc | get usable processors\r\n
0xd00000cd | query port driver version\r\n
0xd00000ce | query port RSS processor configuration\r\n
0xd00000cf | set receive scale parameters\r\n
0xd00000d0 | set receive hash parameters\r\n
0xd00000d1 | update interface ports\r\n
0xd00000d2 | not available\r\n
0xd00000d3 | available\r\n
0xd00000d4 | available on ports\r\n
0xd00000d5 | global configuration\r\n
0xd00000d6 | active mode\r\n
0xd00000d7 | Bind Adapter\r\n
0xd00000d8 | Unbind Adapter (begin)\r\n
0xd00000d9 | Unbind Adapter (end)\r\n
0xd00000da | NetEvent Restart\r\n
0xd00000db | NetEvent Power-down\r\n
0xd00000dc | NetEvent Power-up\r\n
0xd00000dd | NetEvent NDK-enable\r\n
0xd00000de | NetEvent NDK-disable\r\n
0xd00000df | NetEvent NDK usage stopped\r\n
0xd00000e0 | Indicate new NDK interface arrival\r\n
0xd00000e1 | Indicate NDK interface removal\r\n
0xd00000e2 | Indicate NDK operational status change\r\n
0xd00000e3 | Undefined\r\n
0xd00000e4 | Adapter\r\n
0xd00000e5 | QP\r\n
0xd00000e6 | CQ\r\n
0xd00000e7 | MR\r\n
0xd00000e8 | MW\r\n
0xd00000e9 | PD\r\n
0xd00000ea | SharedEndpoint\r\n
0xd00000eb | Connector\r\n
0xd00000ec | Listener\r\n
0xd00000ed | SRQ\r\n
0xd00000ee | Max\r\n
0xd00000ef | Async\r\n
0xd00000f0 | Inline\r\n
0xd00000f1 | Local\r\n
0xd00000f2 | Remote\r\n
0xd00000f3 | Privileged\r\n
0xd00000f4 | Local\r\n
0xd00000f5 | Remote\r\n
0xd00000f6 | NotifyErrors\r\n
0xd00000f7 | NotifyAny\r\n
0xd00000f8 | NotifySolicited\r\n
0xd00000f9 | Invalid\r\n
0xd00000fa | Software Slot allocated\r\n
0xd00000fb | Hardware Slot allocated\r\n
0xd00000fc | Policy error\r\n
0xd00000fd | system error\r\n
0xd00000fe | Enabled\r\n
0xd00000ff | Send request dropped\r\n
0xd0000100 | Receive dropped\r\n
0xd0000101 | Disconnect request dropped\r\n
0xd0000102 | Reset dropped\r\n
0xd0000103 | WFP API No Failure\r\n
0xd0000104 | WFP API WasRedirectedToProxy\r\n
0xd0000105 | WFP API RegisterForExitingEndpoint\r\n
0xd0000106 | WFP API ClassifiableFieldGetAf\r\n
0xd0000107 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000108 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd0000109 | WFP API ClassifiableFieldGetRemotePort\r\n
0xd000010a | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd000010b | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd000010c | Processor Add\r\n
0xd000010d | Power Source Change\r\n
0xd000010e | AC\r\n
0xd000010f | DC\r\n
0xd0000110 | DC Short Term\r\n
0xd0000111 | Unknown\r\n
0xd0000112 | is stopping timers\r\n
0xd0000113 | has stopped timers\r\n
0xd0000114 | is locking partitions\r\n
0xd0000115 | has locked partitions\r\n
0xd0000116 | is unlocking partitions\r\n
0xd0000117 | has unlocked partitions\r\n
0xd0000118 | is starting timers\r\n
0xd0000119 | has started timers\r\n
0xd000011a | is starting\r\n
0xd000011b | is complete\r\n
0xd000011c | IP\r\n
0xd000011d | TCP\r\n
0xd000011e | leaving S0\r\n
0xd000011f | entering S0\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x11000034 | SQM\r\n
0x30000000 | Info\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 posted %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Source = %4, Destination = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto=%3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm=%6, MaxDataRetransmissions=%7, DelayedAckTicks=%8 msec.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3.\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick= %4 Time= %5.\r\n
0xb0000527 | %1 rescheduled by processor %2 for processor %3 at %4 from %5 to %6.\r\n
0xb0000528 | %1 fired on processor %2 at Tick= %3, scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for destination %4 Rule = %5.%6.\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000535 | TCP: connection %1: TCP CTCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \\n\t\t%8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \\n\t\tMaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \\n\t\tSndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | DisconnectTimer\r\n
0xd000002c | SwsTimer\r\n
0xd000002d | ReassemblyRateTimer\r\n
0xd000002e | SynOrRstValidationTimer\r\n
0xd000002f | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000030 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000031 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000032 | TCP_KEEPALIVE\r\n
0xd0000033 | TCP_MAXSEG\r\n
0xd0000034 | TCP_MAXRT\r\n
0xd0000035 | TCP_STDURG\r\n
0xd0000036 | TCP_NOURG\r\n
0xd0000037 | TCP_ATMARK\r\n
0xd0000038 | TCP_NOSYNRETRIES\r\n
0xd0000039 | TCP_TIMESTAMPS\r\n
0xd000003a | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003b | TCP_CONGESTION_ALGORITHM\r\n
0xd000003c | TCP_DELAY_FIN_ACK\r\n
0xd000003d | SO_DEBUG\r\n
0xd000003e | SO_ACCEPTCONN\r\n
0xd000003f | SO_REUSEADDR\r\n
0xd0000040 | SO_KEEPALIVE\r\n
0xd0000041 | SO_DONTROUTE\r\n
0xd0000042 | SO_BROADCAST\r\n
0xd0000043 | SO_USELOOPBACK\r\n
0xd0000044 | SO_LINGER\r\n
0xd0000045 | SO_OOBINLINE\r\n
0xd0000046 | SO_SNDBUF\r\n
0xd0000047 | SO_RCVBUF\r\n
0xd0000048 | SO_CONDITIONAL_ACCEPT\r\n
0xd0000049 | SO_PAUSE_ACCEPT\r\n
0xd000004a | SO_COMPARTMENT_ID\r\n
0xd000004b | SO_RANDOMIZE_PORT\r\n
0xd000004c | SO_PORT_SCALABILITY\r\n
0xd000004d | NldsInvalid\r\n
0xd000004e | NldsTentative\r\n
0xd000004f | NldsDuplicate\r\n
0xd0000050 | NldsDeprecated\r\n
0xd0000051 | Indicate\r\n
0xd0000052 | Pend\r\n
0xd0000053 | Satisfy\r\n
0xd0000054 | NdisPhysicalMediumUnspecified\r\n
0xd0000055 | NdisPhysicalMediumWirelessLan\r\n
0xd0000056 | NdisPhysicalMediumCableModem\r\n
0xd0000057 | NdisPhysicalMediumPhoneLine\r\n
0xd0000058 | NdisPhysicalMediumDSL\r\n
0xd0000059 | NdisPhysicalMedium1394\r\n
0xd000005a | NdisPhysicalMediumWirelessWan\r\n
0xd000005b | NdisPhysicalMediumNative802_11\r\n
0xd000005c | NdisPhysicalMediumBluetooth\r\n
0xd000005d | NdisPhysicalMediumInfiniband\r\n
0xd000005e | NdisPhysicalMediumWiMax\r\n
0xd000005f | NdisPhysicalMedium802_3\r\n
0xd0000060 | NdisPhysicalMedium802_5\r\n
0xd0000061 | NdisPhysicalMediumIrda\r\n
0xd0000062 | NdisPhysicalMediumWiredWAN\r\n
0xd0000063 | IP checksum offload not computed\r\n
0xd0000064 | TCP checksum offload not computed\r\n
0xd0000065 | UDP checksum offload not computed\r\n
0xd0000066 | Header not aligned on 4-byte boundary\r\n
0xd0000067 | IP fragmentation\r\n
0xd0000068 | Source address is not unicast\r\n
0xd0000069 | Destination address is not unicast\r\n
0xd000006a | Ethernet and IP header not contiguous\r\n
0xd000006b | IP options present\r\n
0xd000006c | ESP over UDP\r\n
0xd000006d | Lack contiguous space for upper layer headers\r\n
0xd000006e | WFP filters present\r\n
0xd000006f | Nexthop is unavailable\r\n
0xd0000070 | Path has been invalidated due to policy change\r\n
0xd0000071 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000072 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000073 | Session state is not compatible\r\n
0xd0000074 | TCP options present\r\n
0xd0000075 | UDP IPv6 checksum absent in packet\r\n
0xd0000076 | Packet is for a loopback interface\r\n
0xd0000077 | Failed to allocate the WSD cache\r\n
0xd0000078 | Failure initializing PnP work queue\r\n
0xd0000079 | Failed to get persistent parameters\r\n
0xd000007a | Rejected persistent parameters\r\n
0xd000007b | qualified profile\r\n
0xd000007c | qualified destination\r\n
0xd000007d | sample collection completion\r\n
0xd000007e | idle time expiration\r\n
0xd000007f | allocation\r\n
0xd0000080 | new sample request\r\n
0xd0000081 | configuration change\r\n
0xd0000082 | Idle\r\n
0xd0000083 | ProbingWs\r\n
0xd0000084 | ProbeWait\r\n
0xd0000085 | ProbingWithoutWs\r\n
0xd0000086 | RecordWait\r\n
0xd0000087 | EreQualified\r\n
0xd0000088 | Qualified\r\n
0xd0000089 | Destination is multicast\r\n
0xd000008a | Header is invalid\r\n
0xd000008b | Checksum is invalid\r\n
0xd000008c | Transport endpoint was not found\r\n
0xd000008d | Connected path error\r\n
0xd000008e | Session state error\r\n
0xd000008f | Bad source address\r\n
0xd0000090 | Not locally destined\r\n
0xd0000091 | Protocol unreachable\r\n
0xd0000092 | Port unreachable\r\n
0xd0000093 | Bad length\r\n
0xd0000094 | Malformed Header\r\n
0xd0000095 | No route available\r\n
0xd0000096 | Beyond scope\r\n
0xd0000097 | Inspection drop\r\n
0xd0000098 | Too many decapsulations\r\n
0xd0000099 | Administratively prohibited\r\n
0xd000009a | Hop limit exceeded\r\n
0xd000009b | Address unreachable\r\n
0xd000009c | Fragment MTU exceeded\r\n
0xd000009d | Buffer Length Exceeded\r\n
0xd000009e | Address Resolution Timeout\r\n
0xd000009f | Address Resolution Failure\r\n
0xd00000a0 | IPsec failure\r\n
0xd00000a1 | Extension Headers Failure\r\n
0xd00000a2 | Allocation Failure\r\n
0xd00000a3 | Default\r\n
0xd00000a4 | NewReno\r\n
0xd00000a5 | CcmCtcp\r\n
0xd00000a6 | CcmDctcp\r\n
0xd00000a7 | TcpTemplateTypeInternet\r\n
0xd00000a8 | TcpTemplateTypeDatacenter\r\n
0xd00000a9 | TcpTemplateTypeCompat\r\n
0xd00000aa | TcpTemplateTypeDatacenterCustom\r\n
0xd00000ab | TcpTemplateTypeInternetCustom\r\n
0xd00000ac | TcpTemplateTypeDefault\r\n
0xd00000ad | TcpTemplateTypeAutomatic\r\n
0xd00000ae | No Failure\r\n
0xd00000af | Unknown\r\n
0xd00000b0 | System Policy\r\n
0xd00000b1 | NIC Capacity Reached\r\n
0xd00000b2 | System Low On Memory\r\n
0xd00000b3 | WFP driver / Stream inspection\r\n
0xd00000b4 | Weak Host Model Enabled\r\n
0xd00000b5 | Forwarding Enabled\r\n
0xd00000b6 | Hardware capability\r\n
0xd00000b7 | NDIS filter/NIC property\r\n
0xd00000b8 | Loopback fast path socket option not set on both ends\r\n
0xd00000b9 | Filter policy existed for the loopback connection\r\n
0xd00000ba | IPv4\r\n
0xd00000bb | IPv6\r\n
0xd00000bc | unbind\r\n
0xd00000bd | bind\r\n
0xd00000be | port change\r\n
0xd00000bf | none\r\n
0xd00000c0 | receive hash\r\n
0xd00000c1 | receive scale\r\n
0xd00000c2 | enabled\r\n
0xd00000c3 | disabled\r\n
0xd00000c4 | removing\r\n
0xd00000c5 | adding\r\n
0xd00000c6 | complete binding initialization\r\n
0xd00000c7 | complete port initialization\r\n
0xd00000c8 | enumerate interface ports\r\n
0xd00000c9 | query port link state\r\n
0xd00000ca | query port interface index\r\n
0xd00000cb | query interface ports\r\n
0xd00000cc | query port RSS capabilities\r\n
0xd00000cd | get usable processors\r\n
0xd00000ce | query port driver version\r\n
0xd00000cf | query port RSS processor configuration\r\n
0xd00000d0 | set receive scale parameters\r\n
0xd00000d1 | set receive hash parameters\r\n
0xd00000d2 | update interface ports\r\n
0xd00000d3 | not available\r\n
0xd00000d4 | available\r\n
0xd00000d5 | available on ports\r\n
0xd00000d6 | global configuration\r\n
0xd00000d7 | active mode\r\n
0xd00000d8 | Bind Adapter\r\n
0xd00000d9 | Unbind Adapter (begin)\r\n
0xd00000da | Unbind Adapter (end)\r\n
0xd00000db | NetEvent Restart\r\n
0xd00000dc | NetEvent Power-down\r\n
0xd00000dd | NetEvent Power-up\r\n
0xd00000de | NetEvent NDK-enable\r\n
0xd00000df | NetEvent NDK-disable\r\n
0xd00000e0 | NetEvent NDK usage stopped\r\n
0xd00000e1 | Indicate new NDK interface arrival\r\n
0xd00000e2 | Indicate NDK interface removal\r\n
0xd00000e3 | Indicate NDK operational status change\r\n
0xd00000e4 | Undefined\r\n
0xd00000e5 | Adapter\r\n
0xd00000e6 | QP\r\n
0xd00000e7 | CQ\r\n
0xd00000e8 | MR\r\n
0xd00000e9 | MW\r\n
0xd00000ea | PD\r\n
0xd00000eb | SharedEndpoint\r\n
0xd00000ec | Connector\r\n
0xd00000ed | Listener\r\n
0xd00000ee | SRQ\r\n
0xd00000ef | Max\r\n
0xd00000f0 | Async\r\n
0xd00000f1 | Inline\r\n
0xd00000f2 | Local\r\n
0xd00000f3 | Remote\r\n
0xd00000f4 | Privileged\r\n
0xd00000f5 | Local\r\n
0xd00000f6 | Remote\r\n
0xd00000f7 | NotifyErrors\r\n
0xd00000f8 | NotifyAny\r\n
0xd00000f9 | NotifySolicited\r\n
0xd00000fa | Invalid\r\n
0xd00000fb | Software Slot allocated\r\n
0xd00000fc | Hardware Slot allocated\r\n
0xd00000fd | Policy error\r\n
0xd00000fe | system error\r\n
0xd00000ff | Enabled\r\n
0xd0000100 | Send request dropped\r\n
0xd0000101 | Receive dropped\r\n
0xd0000102 | Disconnect request dropped\r\n
0xd0000103 | Reset dropped\r\n
0xd0000104 | WFP API No Failure\r\n
0xd0000105 | WFP API WasRedirectedToProxy\r\n
0xd0000106 | WFP API RegisterForExitingEndpoint\r\n
0xd0000107 | WFP API ClassifiableFieldGetAf\r\n
0xd0000108 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000109 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd000010a | WFP API ClassifiableFieldGetRemotePort\r\n
0xd000010b | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd000010c | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd000010d | Processor Add\r\n
0xd000010e | Power Source Change\r\n
0xd000010f | AC\r\n
0xd0000110 | DC\r\n
0xd0000111 | DC Short Term\r\n
0xd0000112 | Unknown\r\n
0xd0000113 | is stopping timers\r\n
0xd0000114 | has stopped timers\r\n
0xd0000115 | is locking partitions\r\n
0xd0000116 | has locked partitions\r\n
0xd0000117 | is unlocking partitions\r\n
0xd0000118 | has unlocked partitions\r\n
0xd0000119 | is starting timers\r\n
0xd000011a | has started timers\r\n
0xd000011b | is starting\r\n
0xd000011c | is complete\r\n
0xd000011d | IP\r\n
0xd000011e | TCP\r\n
0xd000011f | leaving S0\r\n
0xd0000120 | entering S0\r\n
0xd0000121 | Unreachable\r\n
0xd0000122 | Incomplete\r\n
0xd0000123 | Probe\r\n
0xd0000124 | Delay\r\n
0xd0000125 | Stale\r\n
0xd0000126 | Reachable\r\n
0xd0000127 | Permanent\r\n
0xd0000128 | Maximum\r\n
0xd0000129 | Map\r\n
0xd000012a | Configure\r\n
0xd000012b | TlSuspectsReachability\r\n
0xd000012c | TlConfirmsReachability\r\n
0xd000012d | NaConfirmsReachability\r\n
0xd000012e | ProbeReachability\r\n
0xd000012f | DadSolicitation\r\n
0xd0000130 | NewDlAddress\r\n
0xd0000131 | TriggerNud\r\n
0xd0000132 | Resolve\r\n
0xd0000133 | Timeout\r\n
0xd0000134 | Sending neighbor solicitation\r\n
0xd0000135 | Received neighbor solicitation\r\n
0xd0000136 | Sending neighbor advertisement\r\n
0xd0000137 | Received neighbor advertisement\r\n
0xd0000138 | Sending router solicitation\r\n
0xd0000139 | Received router solicitation\r\n
0xd000013a | Sending router advertisement\r\n
0xd000013b | Received router advertisement\r\n
0xd000013c | Receive\r\n
0xd000013d | ReceiveAndInvalidate\r\n
0xd000013e | Send\r\n
0xd000013f | FastRegister\r\n
0xd0000140 | Bind\r\n
0xd0000141 | Invalidate\r\n
0xd0000142 | Read\r\n
0xd0000143 | Write\r\n
0xd0000144 | Not Activated\r\n
0xd0000145 | Activated\r\n
0xd0000146 | TCP connect\r\n
0xd0000147 | TCP send\r\n
0xd0000148 | UDP send\r\n
0xd0000149 | RAW send\r\n
0xd000014a | Received Router Advertisement\r\n
0xd000014b | AdminConfigured\r\n
0xd000014c | NetworkProperty\r\n

### 6.3.9600.18725

Message identifier | Message string
--- | ---
0x11000034 | SQM\r\n
0x30000000 | Info\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 posted %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Source = %4, Destination = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto=%3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm=%6, MaxDataRetransmissions=%7, DelayedAckTicks=%8 msec.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3.\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick= %4 Time= %5.\r\n
0xb0000527 | %1 rescheduled by processor %2 for processor %3 at %4 from %5 to %6.\r\n
0xb0000528 | %1 fired on processor %2 at Tick= %3, scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for destination %4 Rule = %5.%6.\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000535 | TCP: connection %1: TCP CTCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \\n\t\t%8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \\n\t\tMaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \\n\t\tSndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | DisconnectTimer\r\n
0xd000002c | SwsTimer\r\n
0xd000002d | ReassemblyRateTimer\r\n
0xd000002e | SynOrRstValidationTimer\r\n
0xd000002f | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000030 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000031 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000032 | TCP_KEEPALIVE\r\n
0xd0000033 | TCP_MAXSEG\r\n
0xd0000034 | TCP_MAXRT\r\n
0xd0000035 | TCP_STDURG\r\n
0xd0000036 | TCP_NOURG\r\n
0xd0000037 | TCP_ATMARK\r\n
0xd0000038 | TCP_NOSYNRETRIES\r\n
0xd0000039 | TCP_TIMESTAMPS\r\n
0xd000003a | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003b | TCP_CONGESTION_ALGORITHM\r\n
0xd000003c | TCP_DELAY_FIN_ACK\r\n
0xd000003d | SO_DEBUG\r\n
0xd000003e | SO_ACCEPTCONN\r\n
0xd000003f | SO_REUSEADDR\r\n
0xd0000040 | SO_KEEPALIVE\r\n
0xd0000041 | SO_DONTROUTE\r\n
0xd0000042 | SO_BROADCAST\r\n
0xd0000043 | SO_USELOOPBACK\r\n
0xd0000044 | SO_LINGER\r\n
0xd0000045 | SO_OOBINLINE\r\n
0xd0000046 | SO_SNDBUF\r\n
0xd0000047 | SO_RCVBUF\r\n
0xd0000048 | SO_CONDITIONAL_ACCEPT\r\n
0xd0000049 | SO_PAUSE_ACCEPT\r\n
0xd000004a | SO_COMPARTMENT_ID\r\n
0xd000004b | SO_RANDOMIZE_PORT\r\n
0xd000004c | SO_PORT_SCALABILITY\r\n
0xd000004d | NldsInvalid\r\n
0xd000004e | NldsTentative\r\n
0xd000004f | NldsDuplicate\r\n
0xd0000050 | NldsDeprecated\r\n
0xd0000051 | Indicate\r\n
0xd0000052 | Pend\r\n
0xd0000053 | Satisfy\r\n
0xd0000054 | NdisPhysicalMediumUnspecified\r\n
0xd0000055 | NdisPhysicalMediumWirelessLan\r\n
0xd0000056 | NdisPhysicalMediumCableModem\r\n
0xd0000057 | NdisPhysicalMediumPhoneLine\r\n
0xd0000058 | NdisPhysicalMediumDSL\r\n
0xd0000059 | NdisPhysicalMedium1394\r\n
0xd000005a | NdisPhysicalMediumWirelessWan\r\n
0xd000005b | NdisPhysicalMediumNative802_11\r\n
0xd000005c | NdisPhysicalMediumBluetooth\r\n
0xd000005d | NdisPhysicalMediumInfiniband\r\n
0xd000005e | NdisPhysicalMediumWiMax\r\n
0xd000005f | NdisPhysicalMedium802_3\r\n
0xd0000060 | NdisPhysicalMedium802_5\r\n
0xd0000061 | NdisPhysicalMediumIrda\r\n
0xd0000062 | NdisPhysicalMediumWiredWAN\r\n
0xd0000063 | IP checksum offload not computed\r\n
0xd0000064 | TCP checksum offload not computed\r\n
0xd0000065 | UDP checksum offload not computed\r\n
0xd0000066 | Header not aligned on 4-byte boundary\r\n
0xd0000067 | IP fragmentation\r\n
0xd0000068 | Source address is not unicast\r\n
0xd0000069 | Destination address is not unicast\r\n
0xd000006a | Ethernet and IP header not contiguous\r\n
0xd000006b | IP options present\r\n
0xd000006c | ESP over UDP\r\n
0xd000006d | Lack contiguous space for upper layer headers\r\n
0xd000006e | WFP filters present\r\n
0xd000006f | Nexthop is unavailable\r\n
0xd0000070 | Path has been invalidated due to policy change\r\n
0xd0000071 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000072 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000073 | Session state is not compatible\r\n
0xd0000074 | TCP options present\r\n
0xd0000075 | UDP IPv6 checksum absent in packet\r\n
0xd0000076 | Packet is for a loopback interface\r\n
0xd0000077 | Failed to allocate the WSD cache\r\n
0xd0000078 | Failure initializing PnP work queue\r\n
0xd0000079 | Failed to get persistent parameters\r\n
0xd000007a | Rejected persistent parameters\r\n
0xd000007b | qualified profile\r\n
0xd000007c | qualified destination\r\n
0xd000007d | sample collection completion\r\n
0xd000007e | idle time expiration\r\n
0xd000007f | allocation\r\n
0xd0000080 | new sample request\r\n
0xd0000081 | configuration change\r\n
0xd0000082 | Idle\r\n
0xd0000083 | ProbingWs\r\n
0xd0000084 | ProbeWait\r\n
0xd0000085 | ProbingWithoutWs\r\n
0xd0000086 | RecordWait\r\n
0xd0000087 | EreQualified\r\n
0xd0000088 | Qualified\r\n
0xd0000089 | Destination is multicast\r\n
0xd000008a | Header is invalid\r\n
0xd000008b | Checksum is invalid\r\n
0xd000008c | Transport endpoint was not found\r\n
0xd000008d | Connected path error\r\n
0xd000008e | Session state error\r\n
0xd000008f | Bad source address\r\n
0xd0000090 | Not locally destined\r\n
0xd0000091 | Protocol unreachable\r\n
0xd0000092 | Port unreachable\r\n
0xd0000093 | Bad length\r\n
0xd0000094 | Malformed Header\r\n
0xd0000095 | No route available\r\n
0xd0000096 | Beyond scope\r\n
0xd0000097 | Inspection drop\r\n
0xd0000098 | Too many decapsulations\r\n
0xd0000099 | Administratively prohibited\r\n
0xd000009a | Hop limit exceeded\r\n
0xd000009b | Address unreachable\r\n
0xd000009c | Fragment MTU exceeded\r\n
0xd000009d | Buffer Length Exceeded\r\n
0xd000009e | Address Resolution Timeout\r\n
0xd000009f | Address Resolution Failure\r\n
0xd00000a0 | IPsec failure\r\n
0xd00000a1 | Extension Headers Failure\r\n
0xd00000a2 | Allocation Failure\r\n
0xd00000a3 | Default\r\n
0xd00000a4 | NewReno\r\n
0xd00000a5 | CcmCtcp\r\n
0xd00000a6 | CcmDctcp\r\n
0xd00000a7 | TcpTemplateTypeInternet\r\n
0xd00000a8 | TcpTemplateTypeDatacenter\r\n
0xd00000a9 | TcpTemplateTypeCompat\r\n
0xd00000aa | TcpTemplateTypeDatacenterCustom\r\n
0xd00000ab | TcpTemplateTypeInternetCustom\r\n
0xd00000ac | TcpTemplateTypeDefault\r\n
0xd00000ad | TcpTemplateTypeAutomatic\r\n
0xd00000ae | No Failure\r\n
0xd00000af | Unknown\r\n
0xd00000b0 | System Policy\r\n
0xd00000b1 | NIC Capacity Reached\r\n
0xd00000b2 | System Low On Memory\r\n
0xd00000b3 | WFP driver / Stream inspection\r\n
0xd00000b4 | Weak Host Model Enabled\r\n
0xd00000b5 | Forwarding Enabled\r\n
0xd00000b6 | Hardware capability\r\n
0xd00000b7 | NDIS filter/NIC property\r\n
0xd00000b8 | Loopback fast path socket option not set on both ends\r\n
0xd00000b9 | Filter policy existed for the loopback connection\r\n
0xd00000ba | IPv4\r\n
0xd00000bb | IPv6\r\n
0xd00000bc | unbind\r\n
0xd00000bd | bind\r\n
0xd00000be | port change\r\n
0xd00000bf | none\r\n
0xd00000c0 | receive hash\r\n
0xd00000c1 | receive scale\r\n
0xd00000c2 | enabled\r\n
0xd00000c3 | disabled\r\n
0xd00000c4 | removing\r\n
0xd00000c5 | adding\r\n
0xd00000c6 | complete binding initialization\r\n
0xd00000c7 | complete port initialization\r\n
0xd00000c8 | enumerate interface ports\r\n
0xd00000c9 | query port link state\r\n
0xd00000ca | query port interface index\r\n
0xd00000cb | query interface ports\r\n
0xd00000cc | query port RSS capabilities\r\n
0xd00000cd | get usable processors\r\n
0xd00000ce | query port driver version\r\n
0xd00000cf | query port RSS processor configuration\r\n
0xd00000d0 | set receive scale parameters\r\n
0xd00000d1 | set receive hash parameters\r\n
0xd00000d2 | update interface ports\r\n
0xd00000d3 | not available\r\n
0xd00000d4 | available\r\n
0xd00000d5 | available on ports\r\n
0xd00000d6 | global configuration\r\n
0xd00000d7 | active mode\r\n
0xd00000d8 | Bind Adapter\r\n
0xd00000d9 | Unbind Adapter (begin)\r\n
0xd00000da | Unbind Adapter (end)\r\n
0xd00000db | NetEvent Restart\r\n
0xd00000dc | NetEvent Power-down\r\n
0xd00000dd | NetEvent Power-up\r\n
0xd00000de | NetEvent NDK-enable\r\n
0xd00000df | NetEvent NDK-disable\r\n
0xd00000e0 | NetEvent NDK usage stopped\r\n
0xd00000e1 | Indicate new NDK interface arrival\r\n
0xd00000e2 | Indicate NDK interface removal\r\n
0xd00000e3 | Indicate NDK operational status change\r\n
0xd00000e4 | Undefined\r\n
0xd00000e5 | Adapter\r\n
0xd00000e6 | QP\r\n
0xd00000e7 | CQ\r\n
0xd00000e8 | MR\r\n
0xd00000e9 | MW\r\n
0xd00000ea | PD\r\n
0xd00000eb | SharedEndpoint\r\n
0xd00000ec | Connector\r\n
0xd00000ed | Listener\r\n
0xd00000ee | SRQ\r\n
0xd00000ef | Max\r\n
0xd00000f0 | Async\r\n
0xd00000f1 | Inline\r\n
0xd00000f2 | Local\r\n
0xd00000f3 | Remote\r\n
0xd00000f4 | Privileged\r\n
0xd00000f5 | Local\r\n
0xd00000f6 | Remote\r\n
0xd00000f7 | NotifyErrors\r\n
0xd00000f8 | NotifyAny\r\n
0xd00000f9 | NotifySolicited\r\n
0xd00000fa | Invalid\r\n
0xd00000fb | Software Slot allocated\r\n
0xd00000fc | Hardware Slot allocated\r\n
0xd00000fd | Policy error\r\n
0xd00000fe | system error\r\n
0xd00000ff | Enabled\r\n
0xd0000100 | Send request dropped\r\n
0xd0000101 | Receive dropped\r\n
0xd0000102 | Disconnect request dropped\r\n
0xd0000103 | Reset dropped\r\n
0xd0000104 | WFP API No Failure\r\n
0xd0000105 | WFP API WasRedirectedToProxy\r\n
0xd0000106 | WFP API RegisterForExitingEndpoint\r\n
0xd0000107 | WFP API ClassifiableFieldGetAf\r\n
0xd0000108 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000109 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd000010a | WFP API ClassifiableFieldGetRemotePort\r\n
0xd000010b | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd000010c | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd000010d | Processor Add\r\n
0xd000010e | Power Source Change\r\n
0xd000010f | AC\r\n
0xd0000110 | DC\r\n
0xd0000111 | DC Short Term\r\n
0xd0000112 | Unknown\r\n
0xd0000113 | is stopping timers\r\n
0xd0000114 | has stopped timers\r\n
0xd0000115 | is locking partitions\r\n
0xd0000116 | has locked partitions\r\n
0xd0000117 | is unlocking partitions\r\n
0xd0000118 | has unlocked partitions\r\n
0xd0000119 | is starting timers\r\n
0xd000011a | has started timers\r\n
0xd000011b | is starting\r\n
0xd000011c | is complete\r\n
0xd000011d | IP\r\n
0xd000011e | TCP\r\n
0xd000011f | leaving S0\r\n
0xd0000120 | entering S0\r\n
0xd0000121 | Unreachable\r\n
0xd0000122 | Incomplete\r\n
0xd0000123 | Probe\r\n
0xd0000124 | Delay\r\n
0xd0000125 | Stale\r\n
0xd0000126 | Reachable\r\n
0xd0000127 | Permanent\r\n
0xd0000128 | Maximum\r\n
0xd0000129 | Map\r\n
0xd000012a | Configure\r\n
0xd000012b | TlSuspectsReachability\r\n
0xd000012c | TlConfirmsReachability\r\n
0xd000012d | NaConfirmsReachability\r\n
0xd000012e | ProbeReachability\r\n
0xd000012f | DadSolicitation\r\n
0xd0000130 | NewDlAddress\r\n
0xd0000131 | TriggerNud\r\n
0xd0000132 | Resolve\r\n
0xd0000133 | Timeout\r\n
0xd0000134 | Sending neighbor solicitation\r\n
0xd0000135 | Received neighbor solicitation\r\n
0xd0000136 | Sending neighbor advertisement\r\n
0xd0000137 | Received neighbor advertisement\r\n
0xd0000138 | Sending router solicitation\r\n
0xd0000139 | Received router solicitation\r\n
0xd000013a | Sending router advertisement\r\n
0xd000013b | Received router advertisement\r\n
0xd000013c | Receive\r\n
0xd000013d | ReceiveAndInvalidate\r\n
0xd000013e | Send\r\n
0xd000013f | FastRegister\r\n
0xd0000140 | Bind\r\n
0xd0000141 | Invalidate\r\n
0xd0000142 | Read\r\n
0xd0000143 | Write\r\n
0xd0000144 | Not Activated\r\n
0xd0000145 | Activated\r\n
0xd0000146 | TCP connect\r\n
0xd0000147 | TCP send\r\n
0xd0000148 | UDP send\r\n
0xd0000149 | RAW send\r\n
0xd000014a | Received Router Advertisement\r\n
0xd000014b | AdminConfigured\r\n
0xd000014c | NetworkProperty\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x11000034 | SQM\r\n
0x30000000 | Info\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 posted %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto=%3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm=%6, MaxDataRetransmissions=%7, DelayedAckTicks=%8 msec.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick= %4 Time= %5.\r\n
0xb0000527 | %1 rescheduled by processor %2 for processor %3 at %4 from %5 to %6.\r\n
0xb0000528 | %1 fired on processor %2 at Tick= %3, scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for destination %4 Rule = %5.%6.\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010534 | TCP: connection %1: TCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | DisconnectTimer\r\n
0xd000002c | SwsTimer\r\n
0xd000002d | ReassemblyRateTimer\r\n
0xd000002e | SynOrRstValidationTimer\r\n
0xd000002f | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000030 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000031 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000032 | TCP_KEEPALIVE\r\n
0xd0000033 | TCP_MAXSEG\r\n
0xd0000034 | TCP_MAXRT\r\n
0xd0000035 | TCP_STDURG\r\n
0xd0000036 | TCP_NOURG\r\n
0xd0000037 | TCP_ATMARK\r\n
0xd0000038 | TCP_NOSYNRETRIES\r\n
0xd0000039 | TCP_TIMESTAMPS\r\n
0xd000003a | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003b | TCP_CONGESTION_ALGORITHM\r\n
0xd000003c | TCP_DELAY_FIN_ACK\r\n
0xd000003d | SO_DEBUG\r\n
0xd000003e | SO_ACCEPTCONN\r\n
0xd000003f | SO_REUSEADDR\r\n
0xd0000040 | SO_KEEPALIVE\r\n
0xd0000041 | SO_DONTROUTE\r\n
0xd0000042 | SO_BROADCAST\r\n
0xd0000043 | SO_USELOOPBACK\r\n
0xd0000044 | SO_LINGER\r\n
0xd0000045 | SO_OOBINLINE\r\n
0xd0000046 | SO_SNDBUF\r\n
0xd0000047 | SO_RCVBUF\r\n
0xd0000048 | SO_CONDITIONAL_ACCEPT\r\n
0xd0000049 | SO_PAUSE_ACCEPT\r\n
0xd000004a | SO_COMPARTMENT_ID\r\n
0xd000004b | SO_RANDOMIZE_PORT\r\n
0xd000004c | SO_PORT_SCALABILITY\r\n
0xd000004d | NldsInvalid\r\n
0xd000004e | NldsTentative\r\n
0xd000004f | NldsDuplicate\r\n
0xd0000050 | NldsDeprecated\r\n
0xd0000051 | Indicate\r\n
0xd0000052 | Pend\r\n
0xd0000053 | Satisfy\r\n
0xd0000054 | NdisPhysicalMediumUnspecified\r\n
0xd0000055 | NdisPhysicalMediumWirelessLan\r\n
0xd0000056 | NdisPhysicalMediumCableModem\r\n
0xd0000057 | NdisPhysicalMediumPhoneLine\r\n
0xd0000058 | NdisPhysicalMediumDSL\r\n
0xd0000059 | NdisPhysicalMedium1394\r\n
0xd000005a | NdisPhysicalMediumWirelessWan\r\n
0xd000005b | NdisPhysicalMediumNative802_11\r\n
0xd000005c | NdisPhysicalMediumBluetooth\r\n
0xd000005d | NdisPhysicalMediumInfiniband\r\n
0xd000005e | NdisPhysicalMediumWiMax\r\n
0xd000005f | NdisPhysicalMedium802_3\r\n
0xd0000060 | NdisPhysicalMedium802_5\r\n
0xd0000061 | NdisPhysicalMediumIrda\r\n
0xd0000062 | NdisPhysicalMediumWiredWAN\r\n
0xd0000063 | IP checksum offload not computed\r\n
0xd0000064 | TCP checksum offload not computed\r\n
0xd0000065 | UDP checksum offload not computed\r\n
0xd0000066 | Header not aligned on 4-byte boundary\r\n
0xd0000067 | IP fragmentation\r\n
0xd0000068 | Source address is not unicast\r\n
0xd0000069 | Destination address is not unicast\r\n
0xd000006a | Ethernet and IP header not contiguous\r\n
0xd000006b | IP options present\r\n
0xd000006c | ESP over UDP\r\n
0xd000006d | Lack contiguous space for upper layer headers\r\n
0xd000006e | WFP filters present\r\n
0xd000006f | Nexthop is unavailable\r\n
0xd0000070 | Path has been invalidated due to policy change\r\n
0xd0000071 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000072 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000073 | Session state is not compatible\r\n
0xd0000074 | TCP options present\r\n
0xd0000075 | UDP IPv6 checksum absent in packet\r\n
0xd0000076 | Packet is for a loopback interface\r\n
0xd0000077 | Packet is from a Raw Socket\r\n
0xd0000078 | TL Ancillary headers present\r\n
0xd0000079 | NL Ancillary headers present\r\n
0xd000007a | Type of Service present\r\n
0xd000007b | IpSec headers present\r\n
0xd000007c | Interface is not Ethernet\r\n
0xd000007d | Nbl check failed\r\n
0xd000007e | Destination address is unknown\r\n
0xd000007f | Failed to allocate the WSD cache\r\n
0xd0000080 | Failure initializing PnP work queue\r\n
0xd0000081 | Failed to get persistent parameters\r\n
0xd0000082 | Rejected persistent parameters\r\n
0xd0000083 | qualified profile\r\n
0xd0000084 | qualified destination\r\n
0xd0000085 | sample collection completion\r\n
0xd0000086 | idle time expiration\r\n
0xd0000087 | allocation\r\n
0xd0000088 | new sample request\r\n
0xd0000089 | configuration change\r\n
0xd000008a | Idle\r\n
0xd000008b | ProbingWs\r\n
0xd000008c | ProbeWait\r\n
0xd000008d | ProbingWithoutWs\r\n
0xd000008e | RecordWait\r\n
0xd000008f | EreQualified\r\n
0xd0000090 | Qualified\r\n
0xd0000091 | Destination is multicast\r\n
0xd0000092 | Header is invalid\r\n
0xd0000093 | Checksum is invalid\r\n
0xd0000094 | Transport endpoint was not found\r\n
0xd0000095 | Connected path error\r\n
0xd0000096 | Session state error\r\n
0xd0000097 | Receive Inspection\r\n
0xd0000098 | ACK Invalid\r\n
0xd0000099 | Expected SYN\r\n
0xd000009a | Received RST\r\n
0xd000009b | Received SYN while in SYN_RCVD state\r\n
0xd000009c | Simultaneous Connect\r\n
0xd000009d | PAWS Failed\r\n
0xd000009e | Land Attack\r\n
0xd000009f | Missed RST\r\n
0xd00000a0 | Outside Receive Window\r\n
0xd00000a1 | Duplicate Segment\r\n
0xd00000a2 | Closed Window\r\n
0xd00000a3 | TCB Removed\r\n
0xd00000a4 | FIN-WAIT2\r\n
0xd00000a5 | Reassembly Conflict\r\n
0xd00000a6 | FIN Received\r\n
0xd00000a7 | Listener received segment with invalid flags\r\n
0xd00000a8 | URG flag set but could not allocate urgent data state\r\n
0xd00000a9 | TCB was not inserted in TCB table\r\n
0xd00000aa | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000ab | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000ac | Packet dropped by TIME-WAIT TCB\r\n
0xd00000ad | Bad source address\r\n
0xd00000ae | Not locally destined\r\n
0xd00000af | Protocol unreachable\r\n
0xd00000b0 | Port unreachable\r\n
0xd00000b1 | Bad length\r\n
0xd00000b2 | Malformed Header\r\n
0xd00000b3 | No route available\r\n
0xd00000b4 | Beyond scope\r\n
0xd00000b5 | Inspection drop\r\n
0xd00000b6 | Too many decapsulations\r\n
0xd00000b7 | Administratively prohibited\r\n
0xd00000b8 | Hop limit exceeded\r\n
0xd00000b9 | Address unreachable\r\n
0xd00000ba | Fragment MTU exceeded\r\n
0xd00000bb | Buffer Length Exceeded\r\n
0xd00000bc | Address Resolution Timeout\r\n
0xd00000bd | Address Resolution Failure\r\n
0xd00000be | IPsec failure\r\n
0xd00000bf | Extension Headers Failure\r\n
0xd00000c0 | Allocation Failure\r\n
0xd00000c1 | Default\r\n
0xd00000c2 | NewReno\r\n
0xd00000c3 | CcmCtcp\r\n
0xd00000c4 | CcmDctcp\r\n
0xd00000c5 | TcpTemplateTypeInternet\r\n
0xd00000c6 | TcpTemplateTypeDatacenter\r\n
0xd00000c7 | TcpTemplateTypeCompat\r\n
0xd00000c8 | TcpTemplateTypeDatacenterCustom\r\n
0xd00000c9 | TcpTemplateTypeInternetCustom\r\n
0xd00000ca | TcpTemplateTypeDefault\r\n
0xd00000cb | TcpTemplateTypeAutomatic\r\n
0xd00000cc | No Failure\r\n
0xd00000cd | Unknown\r\n
0xd00000ce | System Policy\r\n
0xd00000cf | NIC Capacity Reached\r\n
0xd00000d0 | System Low On Memory\r\n
0xd00000d1 | WFP driver / Stream inspection\r\n
0xd00000d2 | Weak Host Model Enabled\r\n
0xd00000d3 | Forwarding Enabled\r\n
0xd00000d4 | Hardware capability\r\n
0xd00000d5 | NDIS filter/NIC property\r\n
0xd00000d6 | Loopback fast path socket option not set on both ends\r\n
0xd00000d7 | Filter policy existed for the loopback connection\r\n
0xd00000d8 | IPv4\r\n
0xd00000d9 | IPv6\r\n
0xd00000da | unbind\r\n
0xd00000db | bind\r\n
0xd00000dc | port change\r\n
0xd00000dd | none\r\n
0xd00000de | receive hash\r\n
0xd00000df | receive scale\r\n
0xd00000e0 | enabled\r\n
0xd00000e1 | disabled\r\n
0xd00000e2 | removing\r\n
0xd00000e3 | adding\r\n
0xd00000e4 | complete binding initialization\r\n
0xd00000e5 | complete port initialization\r\n
0xd00000e6 | enumerate interface ports\r\n
0xd00000e7 | query port link state\r\n
0xd00000e8 | query port interface index\r\n
0xd00000e9 | query interface ports\r\n
0xd00000ea | query port RSS capabilities\r\n
0xd00000eb | get usable processors\r\n
0xd00000ec | query port driver version\r\n
0xd00000ed | query port RSS processor configuration\r\n
0xd00000ee | set receive scale parameters\r\n
0xd00000ef | set receive hash parameters\r\n
0xd00000f0 | update interface ports\r\n
0xd00000f1 | not available\r\n
0xd00000f2 | available\r\n
0xd00000f3 | available on ports\r\n
0xd00000f4 | global configuration\r\n
0xd00000f5 | active mode\r\n
0xd00000f6 | Bind Adapter\r\n
0xd00000f7 | Unbind Adapter (begin)\r\n
0xd00000f8 | Unbind Adapter (end)\r\n
0xd00000f9 | NetEvent Restart\r\n
0xd00000fa | NetEvent Power-down\r\n
0xd00000fb | NetEvent Power-up\r\n
0xd00000fc | NetEvent NDK-enable\r\n
0xd00000fd | NetEvent NDK-disable\r\n
0xd00000fe | NetEvent NDK usage stopped\r\n
0xd00000ff | Indicate new NDK interface arrival\r\n
0xd0000100 | Indicate NDK interface removal\r\n
0xd0000101 | Indicate NDK operational status change\r\n
0xd0000102 | Undefined\r\n
0xd0000103 | Adapter\r\n
0xd0000104 | QP\r\n
0xd0000105 | CQ\r\n
0xd0000106 | MR\r\n
0xd0000107 | MW\r\n
0xd0000108 | PD\r\n
0xd0000109 | SharedEndpoint\r\n
0xd000010a | Connector\r\n
0xd000010b | Listener\r\n
0xd000010c | SRQ\r\n
0xd000010d | Max\r\n
0xd000010e | Async\r\n
0xd000010f | Inline\r\n
0xd0000110 | Local\r\n
0xd0000111 | Remote\r\n
0xd0000112 | Privileged\r\n
0xd0000113 | Local\r\n
0xd0000114 | Remote\r\n
0xd0000115 | NotifyErrors\r\n
0xd0000116 | NotifyAny\r\n
0xd0000117 | NotifySolicited\r\n
0xd0000118 | Invalid\r\n
0xd0000119 | Software Slot allocated\r\n
0xd000011a | Hardware Slot allocated\r\n
0xd000011b | Policy error\r\n
0xd000011c | system error\r\n
0xd000011d | Enabled\r\n
0xd000011e | Send request dropped\r\n
0xd000011f | Receive dropped\r\n
0xd0000120 | Disconnect request dropped\r\n
0xd0000121 | Reset dropped\r\n
0xd0000122 | WFP API No Failure\r\n
0xd0000123 | WFP API WasRedirectedToProxy\r\n
0xd0000124 | WFP API RegisterForExitingEndpoint\r\n
0xd0000125 | WFP API ClassifiableFieldGetAf\r\n
0xd0000126 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000127 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd0000128 | WFP API ClassifiableFieldGetRemotePort\r\n
0xd0000129 | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd000012a | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd000012b | Processor Add\r\n
0xd000012c | Power Source Change\r\n
0xd000012d | AC\r\n
0xd000012e | DC\r\n
0xd000012f | DC Short Term\r\n
0xd0000130 | Unknown\r\n
0xd0000131 | is stopping timers\r\n
0xd0000132 | has stopped timers\r\n
0xd0000133 | is locking partitions\r\n
0xd0000134 | has locked partitions\r\n
0xd0000135 | is unlocking partitions\r\n
0xd0000136 | has unlocked partitions\r\n
0xd0000137 | is starting timers\r\n
0xd0000138 | has started timers\r\n
0xd0000139 | is starting\r\n
0xd000013a | is complete\r\n
0xd000013b | IP\r\n
0xd000013c | TCP\r\n
0xd000013d | leaving S0\r\n
0xd000013e | entering S0\r\n
0xd000013f | Unreachable\r\n
0xd0000140 | Incomplete\r\n
0xd0000141 | Probe\r\n
0xd0000142 | Delay\r\n
0xd0000143 | Stale\r\n
0xd0000144 | Reachable\r\n
0xd0000145 | Permanent\r\n
0xd0000146 | Maximum\r\n
0xd0000147 | Map\r\n
0xd0000148 | Configure\r\n
0xd0000149 | TlSuspectsReachability\r\n
0xd000014a | TlConfirmsReachability\r\n
0xd000014b | NaConfirmsReachability\r\n
0xd000014c | ProbeReachability\r\n
0xd000014d | DadSolicitation\r\n
0xd000014e | NewDlAddress\r\n
0xd000014f | TriggerNud\r\n
0xd0000150 | Resolve\r\n
0xd0000151 | Timeout\r\n
0xd0000152 | Sending neighbor solicitation\r\n
0xd0000153 | Received neighbor solicitation\r\n
0xd0000154 | Sending neighbor advertisement\r\n
0xd0000155 | Received neighbor advertisement\r\n
0xd0000156 | Sending router solicitation\r\n
0xd0000157 | Received router solicitation\r\n
0xd0000158 | Sending router advertisement\r\n
0xd0000159 | Received router advertisement\r\n
0xd000015a | Receive\r\n
0xd000015b | ReceiveAndInvalidate\r\n
0xd000015c | Send\r\n
0xd000015d | FastRegister\r\n
0xd000015e | Bind\r\n
0xd000015f | Invalidate\r\n
0xd0000160 | Read\r\n
0xd0000161 | Write\r\n
0xd0000162 | Not Activated\r\n
0xd0000163 | Activated\r\n
0xd0000164 | TCP connect\r\n
0xd0000165 | TCP send\r\n
0xd0000166 | UDP send\r\n
0xd0000167 | RAW send\r\n
0xd0000168 | Received Router Advertisement\r\n
0xd0000169 | AdminConfigured\r\n
0xd000016a | NetworkProperty\r\n
0xd000016b | CreateWolContext\r\n
0xd000016c | DeleteWolContext\r\n
0xd000016d | SetWolContext\r\n
0xd000016e | ClearWolContext\r\n
0xd000016f | WolContextEvicted\r\n
0xd0000170 | AddWolAddress\r\n
0xd0000171 | RemoveWolAddress\r\n
0xd0000172 | Send\r\n
0xd0000173 | Receive\r\n

### 10.0.14393.0, 10.0.14393.351

Message identifier | Message string
--- | ---
0x11000034 | SQM\r\n
0x30000000 | Info\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 posted %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto = %3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm = %6, MaxDataRetransmissions = %7, DelayedAckTicks = %8 msec, DelayedAckFrequency = %9, RACK enabled = %10, Tail Loss Probe enabled = %11.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick = %4 Time = %5.\r\n
0xb0000527 | %1 timer rescheduled by processor %2 for processor %3 at Tick = %4 to Tick = %5, OldScheduledExpiration = %6 NewScheduledExpiration = %7 DueTime = %8 Aperiodic = %9.\r\n
0xb0000528 | %1 timer fired on processor %2 at Tick = %3, was scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for Destination %4 in Compartment %5, Reason: %8 (Rule %6.%7).\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0000558 | Teredo Add -- PID: %1 started listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb0000559 | Teredo Remove -- PID: %1 stopped listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb000055a | IP: RouteLookup - API: %1 DstAddr: %3 ConstrainSrcAddr: %4 ConstrainIfIndex: %5 ConstraintOveridden: %6 ReturnConstrained: %7 OutgoingIfIndex: %8 NextHopAddr: %9 Status: %10\r\n
0xb000055b | IP: SourceAddrLookup - DstAddr: %2 ConstrainSrcAddr: %3 ConstrainIfIndex: %4 OutgoingIfIndex: %5 ReturnConstrained: %6 SelectedSrcAddr: %7\r\n
0xb000055c | WFP-ALE: Partition Count=%1 Partition Mask=%2: Partition Id=%d Partition NumEntries = %4.\r\n
0xb000055d | WFP-ALE: HotAdd/Remove: Old Partiton Count=%1 Old Partition Mask=%2 New Partiton Count=%1 New Partition Mask=%2.\r\n
0xb000055e | WFP-ALE: RemoteEndPoint Insertion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb000055f | WFP-ALE: RemoteEndPoint Deletion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb0000560 | WFP-ALE: ALE: low memory state detected. LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000561 | WFP-ALE: leaving low memory state. HighMemoryEvent = %1 HighNonPagedPoolEvent = %2.\r\n
0xb0000562 | WFP-ALE: Dpc for cleanup initiated: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000563 | WFP: Dpc for cleanup QUEUED or RE-QUEUED: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000564 | TCP: LEDBAT %2: Connection %1, BaseDelayMs = %6, CurrentDelayMs = %7, CWnd = %3, SsThresh = %4, SndWnd = %5, DelayBasedCwndFactor %9%%, RemainingTimeMs = %8.\r\n
0xb0000565 | TCP: AssociateNameResContext Endpoint: %1 Status: %16 NameResolutionContext: %2 DnsName: %3 InterfaceIndex: %4 IPAddrCount: %5 IPAddrs: %7 %9 %11 %13 %15\r\n
0xb0000566 | TCP: InspectConnectWithNameResContext Connection: %5 (local: %2 remote: %4) NameResolutionContext: %6 DnsName: %7 Status: %8.\r\n
0xb0000567 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 InterfaceMetric: %10 RouteMetric: %11] is preferred over Route [DestinationPrefix: %14/%12 NextHop: %16 InterfaceIndex: %17 InterfaceMetric: %18 RouteMetric: %19] for Destination: %3 in Compartment: %1, Reason: %20.\r\n
0xb0000568 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 RouteMetric: %10] is blocked for Destination: %3 ConstrainInterfaceIndex: %11 ConstrainScopeZone: %12 in Compartment: %1, Reason: %13.\r\n
0xb0000569 | TCP: Tail Loss Probe Send Connection = %1 SndUna = %2, SndMax = %3, SendAvailable = %4, TailProbeSeq = %5, TailProbeLast = %6, ControlsToSend = %7, ThFlags = %8.\r\n
0xb000056a | TCP: Tail Loss Probe Event Connection = %1, Event = %2.\r\n
0xb000056b | TCP: RACK Event Connection = %1, Event = %2, MinRTT = %3, ReoWind = %4, TimeSlotDeltaMin = %5, SeqNum = %6, Timestamp = %7, RttSample = %8.\r\n
0xb000056c | TCP: Fastopen state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000056d | UDP: endpoint (family=%5 pid=%3) create failed: address family not attached.\r\n
0xb000056e | UDP: endpoint %1 (family=%5 pid=%3) create failed: compartment %4 not found.\r\n
0xb000056f | UDP: endpoint %1 (family=%5 pid=%3) created.\r\n
0xb0000570 | UDP: endpoint %1 (family=%5 pid=%3) create failed: inspection status = %2\r\n
0xb0000571 | UDP: endpoint %4 bind failed: address %2 cannot be resolved, status = %3\r\n
0xb0000572 | UDP: endpoint %4 (sockaddr=%2) bind failed: port-acquisition status = %3\r\n
0xb0000573 | UDP: endpoint %4 (sockaddr=%2) bind failed: inspection status = %3\r\n
0xb0000574 | UDP: endpoint %4 (sockaddr=%2) bound.\r\n
0xb0000575 | UDP: endpoint %4 (sockaddr=%2) closed.\r\n
0xb0000576 | UDP: endpoint %4 closed.\r\n
0xb0000577 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address resolution status = %6\r\n
0xb0000578 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address validation failed.\r\n
0xb0000579 | UDP: endpoint %1 (sockaddr=%3) send messages %5: source-address selection status = %6\r\n
0xb000057a | UDP: endpoint %1 too many packets queued for the pending join path.\r\n
0xb000057b | UDP: address family %2added to interface %1.\r\n
0xb000057c | UDP: address family %2removed from interface %1.\r\n
0xb000057d | UDP: Failure initializing transport protocol, status = %1\r\n
0xb000057e | UDP: Failure starting NLNPI client, status = %1\r\n
0xb000057f | UDP: Failure initializing NSI support, status = %1\r\n
0xb0000580 | UDP: Failure starting TLNPI provider, status = %1\r\n
0xb0000581 | UDP: Failure initializing QoS support, status = %1\r\n
0xb0000582 | UDP: Failure starting %1, status = %2\r\n
0xb0000583 | UDP: endpoint %1 (sockaddr=%3) send messages %5: could not allocate send context.\r\n
0xb0000584 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path af failure, status = %6\r\n
0xb0000585 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path missing next hop failure.\r\n
0xb0000586 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path next hop address failure.\r\n
0xb0000587 | TCP: Early Retransmission, FACK or RACK, Connection = %1, SndUna = %2, SackIsLostSeq = %3, DupAckCount = %4\r\n
0xb0000588 | TCP: Ignoring fastopen SYN option due to limit on concurrent SYN_RCVD fastopen connections, Connection = %1, SynRcvdLimit = %2\r\n
0xb0000589 | TCP: Failed to update fastopen key state, Location = %1, Status = %2. Server-side fastopen will be disabled\r\n
0xb000058a | TCP: Fast Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058b | TCP: SACK Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058c | TCP: Limited Transmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058d | TCP: SACK Retransmit Additional Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058e | %1: %2message. Type = %3, Code = %4, CompartmentId = %5, SourceAddress = %7, DestAddress = %9\r\n
0xb000058f | %1: %2path drop. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11\r\n
0xb0000590 | %1: Echo timeout. Status = %4\r\n
0xb0000591 | %1 Timer state changed to %3 by Processor %2 Usage = %4 at Tick = %5\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010534 | TCP: connection %1: TCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP Send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | DisconnectTimer\r\n
0xd000002c | SwsTimer\r\n
0xd000002d | ReassemblyRateTimer\r\n
0xd000002e | SynOrRstValidationTimer\r\n
0xd000002f | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000030 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000031 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000032 | TCP_KEEPALIVE\r\n
0xd0000033 | TCP_MAXSEG\r\n
0xd0000034 | TCP_MAXRT\r\n
0xd0000035 | TCP_STDURG\r\n
0xd0000036 | TCP_NOURG\r\n
0xd0000037 | TCP_ATMARK\r\n
0xd0000038 | TCP_NOSYNRETRIES\r\n
0xd0000039 | TCP_TIMESTAMPS\r\n
0xd000003a | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003b | TCP_CONGESTION_ALGORITHM\r\n
0xd000003c | TCP_DELAY_FIN_ACK\r\n
0xd000003d | SO_DEBUG\r\n
0xd000003e | SO_ACCEPTCONN\r\n
0xd000003f | SO_REUSEADDR\r\n
0xd0000040 | SO_KEEPALIVE\r\n
0xd0000041 | SO_DONTROUTE\r\n
0xd0000042 | SO_BROADCAST\r\n
0xd0000043 | SO_USELOOPBACK\r\n
0xd0000044 | SO_LINGER\r\n
0xd0000045 | SO_OOBINLINE\r\n
0xd0000046 | SO_SNDBUF\r\n
0xd0000047 | SO_RCVBUF\r\n
0xd0000048 | SO_CONDITIONAL_ACCEPT\r\n
0xd0000049 | SO_PAUSE_ACCEPT\r\n
0xd000004a | SO_COMPARTMENT_ID\r\n
0xd000004b | SO_RANDOMIZE_PORT\r\n
0xd000004c | SO_PORT_SCALABILITY\r\n
0xd000004d | NldsInvalid\r\n
0xd000004e | NldsTentative\r\n
0xd000004f | NldsDuplicate\r\n
0xd0000050 | NldsDeprecated\r\n
0xd0000051 | Indicate\r\n
0xd0000052 | Pend\r\n
0xd0000053 | Satisfy\r\n
0xd0000054 | NdisPhysicalMediumUnspecified\r\n
0xd0000055 | NdisPhysicalMediumWirelessLan\r\n
0xd0000056 | NdisPhysicalMediumCableModem\r\n
0xd0000057 | NdisPhysicalMediumPhoneLine\r\n
0xd0000058 | NdisPhysicalMediumDSL\r\n
0xd0000059 | NdisPhysicalMedium1394\r\n
0xd000005a | NdisPhysicalMediumWirelessWan\r\n
0xd000005b | NdisPhysicalMediumNative802_11\r\n
0xd000005c | NdisPhysicalMediumBluetooth\r\n
0xd000005d | NdisPhysicalMediumInfiniband\r\n
0xd000005e | NdisPhysicalMediumWiMax\r\n
0xd000005f | NdisPhysicalMedium802_3\r\n
0xd0000060 | NdisPhysicalMedium802_5\r\n
0xd0000061 | NdisPhysicalMediumIrda\r\n
0xd0000062 | NdisPhysicalMediumWiredWAN\r\n
0xd0000063 | IP checksum offload not computed\r\n
0xd0000064 | TCP checksum offload not computed\r\n
0xd0000065 | UDP checksum offload not computed\r\n
0xd0000066 | Header not aligned on 4-byte boundary\r\n
0xd0000067 | IP fragmentation\r\n
0xd0000068 | Source address is not unicast\r\n
0xd0000069 | Destination address is not unicast\r\n
0xd000006a | Ethernet and IP header not contiguous\r\n
0xd000006b | IP options present\r\n
0xd000006c | ESP over UDP\r\n
0xd000006d | Lack contiguous space for upper layer headers\r\n
0xd000006e | WFP filters present\r\n
0xd000006f | Nexthop is unavailable\r\n
0xd0000070 | Path has been invalidated due to policy change\r\n
0xd0000071 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000072 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000073 | Session state is not compatible\r\n
0xd0000074 | TCP options present\r\n
0xd0000075 | UDP IPv6 checksum absent in packet\r\n
0xd0000076 | Packet is for a loopback interface\r\n
0xd0000077 | Packet is from a Raw Socket\r\n
0xd0000078 | TL Ancillary headers present\r\n
0xd0000079 | NL Ancillary headers present\r\n
0xd000007a | Type of Service present\r\n
0xd000007b | IpSec headers present\r\n
0xd000007c | Interface is not Ethernet\r\n
0xd000007d | Nbl check failed\r\n
0xd000007e | Destination address is unknown\r\n
0xd000007f | Failed to allocate the WSD cache\r\n
0xd0000080 | Failure initializing PnP work queue\r\n
0xd0000081 | Failed to get persistent parameters\r\n
0xd0000082 | Rejected persistent parameters\r\n
0xd0000083 | qualified profile\r\n
0xd0000084 | qualified destination\r\n
0xd0000085 | sample collection completion\r\n
0xd0000086 | idle time expiration\r\n
0xd0000087 | allocation\r\n
0xd0000088 | new sample request\r\n
0xd0000089 | configuration change\r\n
0xd000008a | Idle\r\n
0xd000008b | ProbingWs\r\n
0xd000008c | ProbeWait\r\n
0xd000008d | ProbingWithoutWs\r\n
0xd000008e | RecordWait\r\n
0xd000008f | EreQualified\r\n
0xd0000090 | Qualified\r\n
0xd0000091 | Destination is multicast\r\n
0xd0000092 | Header is invalid\r\n
0xd0000093 | Checksum is invalid\r\n
0xd0000094 | Transport endpoint was not found\r\n
0xd0000095 | Connected path error\r\n
0xd0000096 | Session state error\r\n
0xd0000097 | Receive Inspection\r\n
0xd0000098 | ACK Invalid\r\n
0xd0000099 | Expected SYN\r\n
0xd000009a | Received RST\r\n
0xd000009b | Received SYN while in SYN_RCVD state\r\n
0xd000009c | Simultaneous Connect\r\n
0xd000009d | PAWS Failed\r\n
0xd000009e | Land Attack\r\n
0xd000009f | Missed RST\r\n
0xd00000a0 | Outside Receive Window\r\n
0xd00000a1 | Duplicate Segment\r\n
0xd00000a2 | Closed Window\r\n
0xd00000a3 | TCB Removed\r\n
0xd00000a4 | FIN-WAIT2\r\n
0xd00000a5 | Reassembly Conflict\r\n
0xd00000a6 | FIN Received\r\n
0xd00000a7 | Listener received segment with invalid flags\r\n
0xd00000a8 | URG flag set but could not allocate urgent data state\r\n
0xd00000a9 | TCB was not inserted in TCB table\r\n
0xd00000aa | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000ab | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000ac | Packet dropped by TIME-WAIT TCB\r\n
0xd00000ad | SYN+ACK with Fastopen cookie request\r\n
0xd00000ae | Bad source address\r\n
0xd00000af | Not locally destined\r\n
0xd00000b0 | Protocol unreachable\r\n
0xd00000b1 | Port unreachable\r\n
0xd00000b2 | Bad length\r\n
0xd00000b3 | Malformed Header\r\n
0xd00000b4 | No route available\r\n
0xd00000b5 | Beyond scope\r\n
0xd00000b6 | Inspection drop\r\n
0xd00000b7 | Too many decapsulations\r\n
0xd00000b8 | Administratively prohibited\r\n
0xd00000b9 | Hop limit exceeded\r\n
0xd00000ba | Address unreachable\r\n
0xd00000bb | Fragment MTU exceeded\r\n
0xd00000bc | Buffer Length Exceeded\r\n
0xd00000bd | Address Resolution Timeout\r\n
0xd00000be | Address Resolution Failure\r\n
0xd00000bf | IPsec failure\r\n
0xd00000c0 | Extension Headers Failure\r\n
0xd00000c1 | Allocation Failure\r\n
0xd00000c2 | Default\r\n
0xd00000c3 | NewReno\r\n
0xd00000c4 | CTCP\r\n
0xd00000c5 | DCTCP\r\n
0xd00000c6 | LEDBAT\r\n
0xd00000c7 | TcpTemplateTypeInternet\r\n
0xd00000c8 | TcpTemplateTypeDatacenter\r\n
0xd00000c9 | TcpTemplateTypeCompat\r\n
0xd00000ca | TcpTemplateTypeDatacenterCustom\r\n
0xd00000cb | TcpTemplateTypeInternetCustom\r\n
0xd00000cc | TcpTemplateTypeDefault\r\n
0xd00000cd | TcpTemplateTypeAutomatic\r\n
0xd00000ce | No Failure\r\n
0xd00000cf | Unknown\r\n
0xd00000d0 | System Policy\r\n
0xd00000d1 | NIC Capacity Reached\r\n
0xd00000d2 | System Low On Memory\r\n
0xd00000d3 | WFP driver / Stream inspection\r\n
0xd00000d4 | Weak Host Model Enabled\r\n
0xd00000d5 | Forwarding Enabled\r\n
0xd00000d6 | Hardware capability\r\n
0xd00000d7 | NDIS filter/NIC property\r\n
0xd00000d8 | Loopback fast path socket option not set on both ends\r\n
0xd00000d9 | Filter policy existed for the loopback connection\r\n
0xd00000da | IPv4\r\n
0xd00000db | IPv6\r\n
0xd00000dc | unbind\r\n
0xd00000dd | bind\r\n
0xd00000de | port change\r\n
0xd00000df | none\r\n
0xd00000e0 | receive hash\r\n
0xd00000e1 | receive scale\r\n
0xd00000e2 | enabled\r\n
0xd00000e3 | disabled\r\n
0xd00000e4 | removing\r\n
0xd00000e5 | adding\r\n
0xd00000e6 | complete binding initialization\r\n
0xd00000e7 | complete port initialization\r\n
0xd00000e8 | enumerate interface ports\r\n
0xd00000e9 | query port link state\r\n
0xd00000ea | query port interface index\r\n
0xd00000eb | query interface ports\r\n
0xd00000ec | query port RSS capabilities\r\n
0xd00000ed | get usable processors\r\n
0xd00000ee | query port driver version\r\n
0xd00000ef | query port RSS processor configuration\r\n
0xd00000f0 | set receive scale parameters\r\n
0xd00000f1 | set receive hash parameters\r\n
0xd00000f2 | update interface ports\r\n
0xd00000f3 | not available\r\n
0xd00000f4 | available\r\n
0xd00000f5 | available on ports\r\n
0xd00000f6 | global configuration\r\n
0xd00000f7 | active mode\r\n
0xd00000f8 | Bind Adapter\r\n
0xd00000f9 | Unbind Adapter (begin)\r\n
0xd00000fa | Unbind Adapter (end)\r\n
0xd00000fb | NetEvent Restart\r\n
0xd00000fc | NetEvent Power-down\r\n
0xd00000fd | NetEvent Power-up\r\n
0xd00000fe | NetEvent NDK-enable\r\n
0xd00000ff | NetEvent NDK-disable\r\n
0xd0000100 | NetEvent NDK usage stopped\r\n
0xd0000101 | Indicate new NDK interface arrival\r\n
0xd0000102 | Indicate NDK interface removal\r\n
0xd0000103 | Indicate NDK operational status change\r\n
0xd0000104 | Undefined\r\n
0xd0000105 | Adapter\r\n
0xd0000106 | QP\r\n
0xd0000107 | CQ\r\n
0xd0000108 | MR\r\n
0xd0000109 | MW\r\n
0xd000010a | PD\r\n
0xd000010b | SharedEndpoint\r\n
0xd000010c | Connector\r\n
0xd000010d | Listener\r\n
0xd000010e | SRQ\r\n
0xd000010f | Max\r\n
0xd0000110 | Async\r\n
0xd0000111 | Inline\r\n
0xd0000112 | Local\r\n
0xd0000113 | Remote\r\n
0xd0000114 | Privileged\r\n
0xd0000115 | Local\r\n
0xd0000116 | Remote\r\n
0xd0000117 | NotifyErrors\r\n
0xd0000118 | NotifyAny\r\n
0xd0000119 | NotifySolicited\r\n
0xd000011a | Invalid\r\n
0xd000011b | Software Slot allocated\r\n
0xd000011c | Hardware Slot allocated\r\n
0xd000011d | Policy error\r\n
0xd000011e | system error\r\n
0xd000011f | Enabled\r\n
0xd0000120 | Send request dropped\r\n
0xd0000121 | Receive dropped\r\n
0xd0000122 | Disconnect request dropped\r\n
0xd0000123 | Reset dropped\r\n
0xd0000124 | WFP API No Failure\r\n
0xd0000125 | WFP API WasRedirectedToProxy\r\n
0xd0000126 | WFP API RegisterForExitingEndpoint\r\n
0xd0000127 | WFP API ClassifiableFieldGetAf\r\n
0xd0000128 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000129 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd000012a | WFP API ClassifiableFieldGetRemotePort\r\n
0xd000012b | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd000012c | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd000012d | Processor Add\r\n
0xd000012e | Power Source Change\r\n
0xd000012f | AC\r\n
0xd0000130 | DC\r\n
0xd0000131 | DC Short Term\r\n
0xd0000132 | Unknown\r\n
0xd0000133 | is stopping timers\r\n
0xd0000134 | has stopped timers\r\n
0xd0000135 | is locking partitions\r\n
0xd0000136 | has locked partitions\r\n
0xd0000137 | is unlocking partitions\r\n
0xd0000138 | has unlocked partitions\r\n
0xd0000139 | is starting timers\r\n
0xd000013a | has started timers\r\n
0xd000013b | is starting\r\n
0xd000013c | is complete\r\n
0xd000013d | IP\r\n
0xd000013e | TCP\r\n
0xd000013f | leaving S0\r\n
0xd0000140 | entering S0\r\n
0xd0000141 | Unreachable\r\n
0xd0000142 | Incomplete\r\n
0xd0000143 | Probe\r\n
0xd0000144 | Delay\r\n
0xd0000145 | Stale\r\n
0xd0000146 | Reachable\r\n
0xd0000147 | Permanent\r\n
0xd0000148 | Maximum\r\n
0xd0000149 | Map\r\n
0xd000014a | Configure\r\n
0xd000014b | TlSuspectsReachability\r\n
0xd000014c | TlConfirmsReachability\r\n
0xd000014d | NaConfirmsReachability\r\n
0xd000014e | ProbeReachability\r\n
0xd000014f | DadSolicitation\r\n
0xd0000150 | NewDlAddress\r\n
0xd0000151 | TriggerNud\r\n
0xd0000152 | Resolve\r\n
0xd0000153 | Timeout\r\n
0xd0000154 | Sending neighbor solicitation\r\n
0xd0000155 | Received neighbor solicitation\r\n
0xd0000156 | Sending neighbor advertisement\r\n
0xd0000157 | Received neighbor advertisement\r\n
0xd0000158 | Sending router solicitation\r\n
0xd0000159 | Received router solicitation\r\n
0xd000015a | Sending router advertisement\r\n
0xd000015b | Received router advertisement\r\n
0xd000015c | Receive\r\n
0xd000015d | ReceiveAndInvalidate\r\n
0xd000015e | Send\r\n
0xd000015f | FastRegister\r\n
0xd0000160 | Bind\r\n
0xd0000161 | Invalidate\r\n
0xd0000162 | Read\r\n
0xd0000163 | Write\r\n
0xd0000164 | Not Activated\r\n
0xd0000165 | Activated\r\n
0xd0000166 | TCP connect\r\n
0xd0000167 | TCP send\r\n
0xd0000168 | UDP send\r\n
0xd0000169 | RAW send\r\n
0xd000016a | Received Router Advertisement\r\n
0xd000016b | AdminConfigured\r\n
0xd000016c | NetworkProperty\r\n
0xd000016d | CreateWolContext\r\n
0xd000016e | DeleteWolContext\r\n
0xd000016f | SetWolContext\r\n
0xd0000170 | ClearWolContext\r\n
0xd0000171 | WolContextEvicted\r\n
0xd0000172 | AddWolAddress\r\n
0xd0000173 | RemoveWolAddress\r\n
0xd0000174 | Send\r\n
0xd0000175 | Receive\r\n
0xd0000176 | WFP-ALE: RemoteEndPoint Address\r\n
0xd0000177 | WFP-ALE: RemoteEndPoint Port\r\n
0xd0000178 | WFP-ALE: LocalEndPoint Address\r\n
0xd0000179 | WFP-ALE: LocalEndPoint Port\r\n
0xd000017a | WFP-ALE: Partition Id\r\n
0xd000017b | WFP-ALE: Parition NumEnties\r\n
0xd000017c | SlowDownEntry\r\n
0xd000017d | SlowDownExit\r\n
0xd000017e | SlowDownTracking\r\n
0xd000017f | BaseDelayUpdate\r\n
0xd0000180 | Ack\r\n
0xd0000181 | DupAck\r\n
0xd0000182 | Timeout\r\n
0xd0000183 | Ecn\r\n
0xd0000184 | SpuriousTimeout\r\n
0xd0000185 | Network Context Constraint\r\n
0xd0000186 | Prefix Length Policy\r\n
0xd0000187 | Start Epoch Policy\r\n
0xd0000188 | Default Routes Disabled On Interface\r\n
0xd0000189 | Unconstrained Lookup Disallowed On Interface\r\n
0xd000018a | Interface Disconnected\r\n
0xd000018b | Route Invalid Lifetime\r\n
0xd000018c | Interface Constraint\r\n
0xd000018d | Scope Constraint\r\n
0xd000018e | Rechability\r\n
0xd000018f | Prefix Length\r\n
0xd0000190 | Route And Interface Metrics\r\n
0xd0000191 | Destination And Source Hash\r\n
0xd0000192 | Route Order\r\n
0xd0000193 | Dead Gateway\r\n
0xd0000194 | OnLink Route\r\n
0xd0000195 | Prefer Same Address\r\n
0xd0000196 | Prefer Appropriate Scope\r\n
0xd0000197 | Avoid Deprecated Addresses\r\n
0xd0000198 | Prefer Home Addresses\r\n
0xd0000199 | Prefer Outgoing Interface\r\n
0xd000019a | Prefer Addresses Associated With NextHop\r\n
0xd000019b | Prefer Matching Label\r\n
0xd000019c | Prefer Temporary Addresses\r\n
0xd000019d | System Defined Preference (Windows Specific)\r\n
0xd000019e | Prefer Longest Matching Prefix With NextHop (Windows Specific)\r\n
0xd000019f | Prefer Longest Matching Prefix\r\n
0xd00001a0 | TimerArmed\r\n
0xd00001a1 | TimerFired\r\n
0xd00001a2 | Failed\r\n
0xd00001a3 | Init\r\n
0xd00001a4 | SetTimeSlotData\r\n
0xd00001a5 | SetTailTimeSlot\r\n
0xd00001a6 | EraseTimestamps\r\n
0xd00001a7 | GetRecoverySeq\r\n
0xd00001a8 | RttSampleUpdate\r\n
0xd00001a9 | TcpFastopenOff\r\n
0xd00001aa | TcpFastopenAccepting\r\n
0xd00001ab | TcpFastopenServerSendingCookie\r\n
0xd00001ac | TcpFastopenServerSentCookie\r\n
0xd00001ad | TcpFastopenNegotiate\r\n
0xd00001ae | TcpFastopenAttempt\r\n
0xd00001af | TcpFastopenNegotiateSuccess\r\n
0xd00001b0 | TcpFastopenAttemptSuccess\r\n
0xd00001b1 | TcpFastopenCookieRollover\r\n
0xd00001b2 | TcpFastopenFailed\r\n
0xd00001b3 | TcpFastopenFailedBlocklist\r\n
0xd00001b4 | General failure\r\n
0xd00001b5 | Truncated header\r\n
0xd00001b6 | Invalid checksum\r\n
0xd00001b7 | Inspection drop\r\n
0xd00001b8 | Rejecting loopback neighbor discovery\r\n
0xd00001b9 | Unknown type/code\r\n
0xd00001ba | Truncated IP header\r\n
0xd00001bb | Oversized IP header\r\n
0xd00001bc | No handler\r\n
0xd00001bd | Not responding with error for error\r\n
0xd00001be | Invalid source\r\n
0xd00001bf | Interface rate limit\r\n
0xd00001c0 | Path rate limit\r\n
0xd00001c1 | No route\r\n
0xd00001c2 | No matching request\r\n
0xd00001c3 | Buffer too small\r\n
0xd00001c4 | Failed to obtain ancillary data\r\n
0xd00001c5 | Echo Reply\r\n
0xd00001c6 | Destination Unreachable\r\n
0xd00001c7 | Packet Too Big\r\n
0xd00001c8 | Destination Unreachable(v4)/Time Exceeded(v6)\r\n
0xd00001c9 | Source Quench(v4)/Parameter Problem(v6)\r\n
0xd00001ca | Redirect\r\n
0xd00001cb | Echo Request\r\n
0xd00001cc | Router Advertisement\r\n
0xd00001cd | Router Solicitation\r\n
0xd00001ce | Time Exceeded\r\n
0xd00001cf | Parameter Problem\r\n
0xd00001d0 | Timestamp Request\r\n
0xd00001d1 | Timestamp Reply\r\n
0xd00001d2 | Address Mask Request\r\n
0xd00001d3 | Address Mask Reply\r\n
0xd00001d4 | Echo Request\r\n
0xd00001d5 | Echo Reply\r\n
0xd00001d6 | Multicast Listener Query\r\n
0xd00001d7 | Multicast Listener Report\r\n
0xd00001d8 | Multicast Listener Done\r\n
0xd00001d9 | Router Solicitation\r\n
0xd00001da | Router Advertisement\r\n
0xd00001db | Neighbor Solicitation\r\n
0xd00001dc | Neighbor Advertisement\r\n
0xd00001dd | Redirect Message\r\n
0xd00001de | Multicast Listener Discovery\r\n
0xd00001df | Not Parsed\r\n
0xd00001e0 | Periodic\r\n
0xd00001e1 | Aperiodic\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x11000034 | SQM\r\n
0x30000000 | Info\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto = %3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm = %6, MaxDataRetransmissions = %7, DelayedAckTicks = %8 msec, DelayedAckFrequency = %9, RACK enabled = %10, Tail Loss Probe enabled = %11.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5, Event = %6.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick = %4 Time = %5.\r\n
0xb0000527 | %1 timer rescheduled by processor %2 for processor %3 at Tick = %4 to Tick = %5, OldScheduledExpiration = %6 NewScheduledExpiration = %7 DueTime = %8 Aperiodic = %9.\r\n
0xb0000528 | %1 timer fired on processor %2 at Tick = %3, was scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for Destination %4 in Compartment %5, Reason: %8 (Rule %6.%7).\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0000558 | Teredo Add -- PID: %1 started listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb0000559 | Teredo Remove -- PID: %1 stopped listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb000055a | IP: RouteLookup - API: %1 DstAddr: %3 ConstrainSrcAddr: %4 ConstrainIfIndex: %5 ConstraintOveridden: %6 ReturnConstrained: %7 OutgoingIfIndex: %8 NextHopAddr: %9 Status: %10\r\n
0xb000055b | IP: SourceAddrLookup - DstAddr: %2 ConstrainSrcAddr: %3 ConstrainIfIndex: %4 OutgoingIfIndex: %5 ReturnConstrained: %6 SelectedSrcAddr: %7\r\n
0xb000055c | WFP-ALE: Partition Count=%1 Partition Mask=%2: Partition Id=%d Partition NumEntries = %4.\r\n
0xb000055d | WFP-ALE: HotAdd/Remove: Old Partiton Count=%1 Old Partition Mask=%2 New Partiton Count=%1 New Partition Mask=%2.\r\n
0xb000055e | WFP-ALE: RemoteEndPoint Insertion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb000055f | WFP-ALE: RemoteEndPoint Deletion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb0000560 | WFP-ALE: ALE: low memory state detected. LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000561 | WFP-ALE: leaving low memory state. HighMemoryEvent = %1 HighNonPagedPoolEvent = %2.\r\n
0xb0000562 | WFP-ALE: Dpc for cleanup initiated: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000563 | WFP: Dpc for cleanup QUEUED or RE-QUEUED: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000564 | TCP: LEDBAT %2: Connection %1, BaseDelayMs = %6, CurrentDelayMs = %7, CWnd = %3, SsThresh = %4, SndWnd = %5, DelayBasedCwndFactor %9%%, RemainingTimeMs = %8.\r\n
0xb0000565 | TCP: AssociateNameResContext Endpoint: %1 Status: %16 NameResolutionContext: %2 DnsName: %3 InterfaceIndex: %4 IPAddrCount: %5 IPAddrs: %7 %9 %11 %13 %15\r\n
0xb0000566 | TCP: InspectConnectWithNameResContext Connection: %5 (local: %2 remote: %4) NameResolutionContext: %6 DnsName: %7 Status: %8.\r\n
0xb0000567 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 InterfaceMetric: %10 RouteMetric: %11] is preferred over Route [DestinationPrefix: %14/%12 NextHop: %16 InterfaceIndex: %17 InterfaceMetric: %18 RouteMetric: %19] for Destination: %3 in Compartment: %1, Reason: %20.\r\n
0xb0000568 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 RouteMetric: %10] is blocked for Destination: %3 ConstrainInterfaceIndex: %11 ConstrainScopeZone: %12 in Compartment: %1, Reason: %13.\r\n
0xb0000569 | TCP: Tail Loss Probe Send Connection = %1 SndUna = %2, SndMax = %3, SendAvailable = %4, TailProbeSeq = %5, TailProbeLast = %6, ControlsToSend = %7, ThFlags = %8.\r\n
0xb000056a | TCP: Tail Loss Probe Event Connection = %1, Event = %2.\r\n
0xb000056b | TCP: RACK Event Connection = %1, Event = %2, MinRTT = %3, ReoWind = %4, TimeSlotDeltaMin = %5, SeqNum = %6, Timestamp = %7, RttSample = %8.\r\n
0xb000056c | TCP: Fastopen state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000056d | UDP: endpoint (family=%5 pid=%3) create failed: address family not attached.\r\n
0xb000056e | UDP: endpoint %1 (family=%5 pid=%3) create failed: compartment %4 not found.\r\n
0xb000056f | UDP: endpoint %1 (family=%5 pid=%3) created.\r\n
0xb0000570 | UDP: endpoint %1 (family=%5 pid=%3) create failed: inspection status = %2\r\n
0xb0000571 | UDP: endpoint %4 bind failed: address %2 cannot be resolved, status = %3\r\n
0xb0000572 | UDP: endpoint %4 (sockaddr=%2) bind failed: port-acquisition status = %3\r\n
0xb0000573 | UDP: endpoint %4 (sockaddr=%2) bind failed: inspection status = %3\r\n
0xb0000574 | UDP: endpoint %4 (sockaddr=%2) bound.\r\n
0xb0000575 | UDP: endpoint %4 (sockaddr=%2) closed.\r\n
0xb0000576 | UDP: endpoint %4 closed.\r\n
0xb0000577 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address resolution status = %6\r\n
0xb0000578 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address validation failed.\r\n
0xb0000579 | UDP: endpoint %1 (sockaddr=%3) send messages %5: source-address selection status = %6\r\n
0xb000057a | UDP: endpoint %1 too many packets queued for the pending join path.\r\n
0xb000057b | UDP: address family %2added to interface %1.\r\n
0xb000057c | UDP: address family %2removed from interface %1.\r\n
0xb000057d | UDP: Failure initializing transport protocol, status = %1\r\n
0xb000057e | UDP: Failure starting NLNPI client, status = %1\r\n
0xb000057f | UDP: Failure initializing NSI support, status = %1\r\n
0xb0000580 | UDP: Failure starting TLNPI provider, status = %1\r\n
0xb0000581 | UDP: Failure initializing QoS support, status = %1\r\n
0xb0000582 | UDP: Failure starting %1, status = %2\r\n
0xb0000583 | UDP: endpoint %1 (sockaddr=%3) send messages %5: could not allocate send context.\r\n
0xb0000584 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path af failure, status = %6\r\n
0xb0000585 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path missing next hop failure.\r\n
0xb0000586 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path next hop address failure.\r\n
0xb0000587 | TCP: Early Retransmission, FACK or RACK, Connection = %1, SndUna = %2, SackIsLostSeq = %3, DupAckCount = %4\r\n
0xb0000588 | TCP: Ignoring fastopen SYN option due to limit on concurrent SYN_RCVD fastopen connections, Connection = %1, SynRcvdLimit = %2\r\n
0xb0000589 | TCP: Failed to update fastopen key state, Location = %1, Status = %2. Server-side fastopen will be disabled\r\n
0xb000058a | TCP: Fast Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058b | TCP: SACK Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058c | TCP: Limited Transmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058d | TCP: SACK Retransmit Additional Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058e | %1: %2message. Type = %3, Code = %4, CompartmentId = %5, SourceAddress = %7, DestAddress = %9\r\n
0xb000058f | %1: %2path drop. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11\r\n
0xb0000590 | %1: Echo timeout. Status = %4\r\n
0xb0000591 | %1 Timer state changed to %3 by Processor %2 Usage = %4 at Tick = %5\r\n
0xb0000592 | TCP: connection %1 send complete %3 bytes at %4 (%2).\r\n
0xb0000593 | IP: Compartment creation. Compartment = %1, Protocol = %2, Private = %3, Status = %4.\r\n
0xb0000594 | IP: Compartment deletion. Compartment = %1, Protocol = %2.\r\n
0xb0000595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13.\r\n
0xb0000596 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5 CwrMax = %6.\r\n
0xb0000597 | IP: Compartment cleanup. Compartment = %1, Protocol = %2.\r\n
0xb0000598 | IP: Interface network category state change. Interface = %1, Compartment = %2 , Protocol = %3, NetworkCategory = %4, DomainNetworkLocation = %5, DomainType = %6, Signature = %7.\r\n
0xb0000599 | IP: Interface creation. Interface = %1, Compartment = %2, Protocol = %3, PhysicalMediumType = %4, Status = %5.\r\n
0xb000059a | IP: Interface deletion. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059b | IP: Interface cleanup. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059c | IP: SubInterface creation. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4, Status = %5.\r\n
0xb000059d | IP: SubInterface deletion. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059e | IP: SubInterface cleanup. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059f | IP: Interface change Notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005a0 | IP: Interface internet connectivity status change. Interface = %1, Compartment = %2, Protocol = %3, OldConnectivityStatus = %4, NewConnectivityStatus = %5.\r\n
0xb00005a1 | IP: Address change notification. Address = %2, Interface = %3, Compartment = %4, Protocol = %5, Reason = %6.\r\n
0xb00005a2 | IP: Route change notification. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, NotifyFlags = %8.\r\n
0xb00005a3 | IP: Neighbor change notification. IpAddress = %2, DlAddress = %4, Interface = %5, Compartment = %6, State = %7, Reason = %8.\r\n
0xb00005a4 | IP: Address DAD state change. Address = %2, Interface = %3, Compartment = %4, OldState = %5, NewState = %6, Reason = %7.\r\n
0xb00005a5 | IP: Route Dead Gateway Detection state change. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, OldState = %8, NewState = %9, OldProbeCount = %10, NewProbeCount = %11, OldUnreachablePaths = %12, NewUnreachablePaths = %13, OldMovedPaths = %14, NewMovedPaths = %15, TotalPaths = %16, OldStateChangeTick = %17, NewStateChangeTick = %18, DgdNeedsReset = %19, Reason = %20.\r\n
0xb00005a6 | IP: Disconnecting TCP connections with Address = %2, Interface = %3, Compartment = %4, SkipLocal = %5, SkipOnLink = %6.\r\n
0xb00005a7 | TCP: connection %1: Sending paced chunk of %6 bytes with CWnd = %2, SndWnd = %3, BytesAvailable = %4, BytesOutstanding = %5\r\n
0xb00005a8 | Fallback: Context = %1, Feature = %2, TraceReason = %3, Confidence = %4, Successes = %5, Failures = %6\r\n
0xb00005a9 | TCPIP: TCB %1 using fast loopback\r\n
0xb00005aa | IP: Router information change notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005ab | IP: %1. Interface = %2, Compartment = %3, RouterAddress = %5, DNS Server/Suffix: %7 %8, Lifetime = %9.\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010452 | IP: Interface media disconnect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001045a | IP: Address DAD successful. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001045b | IP: Address DAD failed. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2, DL address of packet = %5.\r\n
0xb001045c | IP: Address DAD started. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010467 | IP: Address addition. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010468 | IP: Address deletion. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001046a | Framing: Interface operation status change. Interface = %1, Compartment = %4, Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0010470 | Framing: NDIS pause event. Interface = %1, Compartment = %3.\r\n
0xb0010471 | Framing: NDIS restart event. Interface = %1, Compartment = %3.\r\n
0xb0010478 | IP: Interface property change. Interface = %1, Compartment = %10, Protocol = %11, Advertise = %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7, WeakHostSend = %8, WeakHostReceive = %9.\r\n
0xb00104b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, Address = %4 %3 %6.\r\n
0xb00104b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7.\r\n
0xb0010529 | IP: Interface media connect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052a | IP: Interface limited link connectivity set. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052b | IP: Interface limited link connectivity reset. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052c | IP: Neighbor state change. IPAddress = %3, DLAddress = %5, Interface = %1, Compartment = %9, OldState = %6, NewState = %7, Event = %8.\r\n
0xb001052d | IP: Neighbor Discovery. Event = %5, Interface = %1, Compartment = %6, SourceIpAddress = %3, TargetIpAddress = %4.\r\n
0xb0010534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb001054e | IP: Interface configuration flags updated. Interface = %1, Compartment = %5, Protocol = %6, Property = %2, Value = %3, Event = %4.\r\n
0xb0010557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9, NrtNameResolutionId %10\r\n
0xb0010565 | TCP: AssociateNameResContext EndpointObj: %1 IsConnectionObj: %2 NameResContext: %3 Status: %4\r\n
0xb00204b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, Address = %4 %3 %6.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | PacingTimer\r\n
0xd000002c | DisconnectTimer\r\n
0xd000002d | SwsTimer\r\n
0xd000002e | ReassemblyRateTimer\r\n
0xd000002f | SynOrRstValidationTimer\r\n
0xd0000030 | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000031 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000032 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000033 | TCP_KEEPALIVE\r\n
0xd0000034 | TCP_MAXSEG\r\n
0xd0000035 | TCP_MAXRT\r\n
0xd0000036 | TCP_STDURG\r\n
0xd0000037 | TCP_NOURG\r\n
0xd0000038 | TCP_ATMARK\r\n
0xd0000039 | TCP_NOSYNRETRIES\r\n
0xd000003a | TCP_TIMESTAMPS\r\n
0xd000003b | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003c | TCP_CONGESTION_ALGORITHM\r\n
0xd000003d | TCP_DELAY_FIN_ACK\r\n
0xd000003e | SO_DEBUG\r\n
0xd000003f | SO_ACCEPTCONN\r\n
0xd0000040 | SO_REUSEADDR\r\n
0xd0000041 | SO_KEEPALIVE\r\n
0xd0000042 | SO_DONTROUTE\r\n
0xd0000043 | SO_BROADCAST\r\n
0xd0000044 | SO_USELOOPBACK\r\n
0xd0000045 | SO_LINGER\r\n
0xd0000046 | SO_OOBINLINE\r\n
0xd0000047 | SO_SNDBUF\r\n
0xd0000048 | SO_RCVBUF\r\n
0xd0000049 | SO_CONDITIONAL_ACCEPT\r\n
0xd000004a | SO_PAUSE_ACCEPT\r\n
0xd000004b | SO_COMPARTMENT_ID\r\n
0xd000004c | SO_RANDOMIZE_PORT\r\n
0xd000004d | SO_PORT_SCALABILITY\r\n
0xd000004e | NldsInvalid\r\n
0xd000004f | NldsTentative\r\n
0xd0000050 | NldsDuplicate\r\n
0xd0000051 | NldsDeprecated\r\n
0xd0000052 | NldsPreferred\r\n
0xd0000053 | Indicate\r\n
0xd0000054 | Pend\r\n
0xd0000055 | Satisfy\r\n
0xd0000056 | NdisPhysicalMediumUnspecified\r\n
0xd0000057 | NdisPhysicalMediumWirelessLan\r\n
0xd0000058 | NdisPhysicalMediumCableModem\r\n
0xd0000059 | NdisPhysicalMediumPhoneLine\r\n
0xd000005a | NdisPhysicalMediumDSL\r\n
0xd000005b | NdisPhysicalMedium1394\r\n
0xd000005c | NdisPhysicalMediumWirelessWan\r\n
0xd000005d | NdisPhysicalMediumNative802_11\r\n
0xd000005e | NdisPhysicalMediumBluetooth\r\n
0xd000005f | NdisPhysicalMediumInfiniband\r\n
0xd0000060 | NdisPhysicalMediumWiMax\r\n
0xd0000061 | NdisPhysicalMedium802_3\r\n
0xd0000062 | NdisPhysicalMedium802_5\r\n
0xd0000063 | NdisPhysicalMediumIrda\r\n
0xd0000064 | NdisPhysicalMediumWiredWAN\r\n
0xd0000065 | IP checksum offload not computed\r\n
0xd0000066 | TCP checksum offload not computed\r\n
0xd0000067 | UDP checksum offload not computed\r\n
0xd0000068 | Header not aligned on 4-byte boundary\r\n
0xd0000069 | IP fragmentation\r\n
0xd000006a | Source address is not unicast\r\n
0xd000006b | Destination address is not unicast\r\n
0xd000006c | Ethernet and IP header not contiguous\r\n
0xd000006d | IP options present\r\n
0xd000006e | ESP over UDP\r\n
0xd000006f | Lack contiguous space for upper layer headers\r\n
0xd0000070 | WFP filters present\r\n
0xd0000071 | Nexthop is unavailable\r\n
0xd0000072 | Path has been invalidated due to policy change\r\n
0xd0000073 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000074 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000075 | Session state is not compatible\r\n
0xd0000076 | TCP options present\r\n
0xd0000077 | UDP IPv6 checksum absent in packet\r\n
0xd0000078 | Packet is for a loopback interface\r\n
0xd0000079 | Packet is from a Raw Socket\r\n
0xd000007a | TL Ancillary headers present\r\n
0xd000007b | NL Ancillary headers present\r\n
0xd000007c | Type of Service present\r\n
0xd000007d | IpSec headers present\r\n
0xd000007e | Interface is not Ethernet\r\n
0xd000007f | Nbl check failed\r\n
0xd0000080 | Destination address is unknown\r\n
0xd0000081 | Failed to allocate the WSD cache\r\n
0xd0000082 | Failure initializing PnP work queue\r\n
0xd0000083 | Failed to get persistent parameters\r\n
0xd0000084 | Rejected persistent parameters\r\n
0xd0000085 | qualified profile\r\n
0xd0000086 | qualified destination\r\n
0xd0000087 | sample collection completion\r\n
0xd0000088 | idle time expiration\r\n
0xd0000089 | allocation\r\n
0xd000008a | new sample request\r\n
0xd000008b | configuration change\r\n
0xd000008c | Idle\r\n
0xd000008d | ProbingWs\r\n
0xd000008e | ProbeWait\r\n
0xd000008f | ProbingWithoutWs\r\n
0xd0000090 | RecordWait\r\n
0xd0000091 | EreQualified\r\n
0xd0000092 | Qualified\r\n
0xd0000093 | Destination is multicast\r\n
0xd0000094 | Header is invalid (location 0)\r\n
0xd0000095 | Header is invalid (subreason 1)\r\n
0xd0000096 | Checksum is invalid\r\n
0xd0000097 | Transport endpoint was not found\r\n
0xd0000098 | Connected path error\r\n
0xd0000099 | Session state error\r\n
0xd000009a | Receive Inspection\r\n
0xd000009b | ACK Invalid (subreason 0) (invalid ACK in SYN_SENT state)\r\n
0xd000009c | ACK Invalid (subreason 1) (SYN_SENT state; received RST without ACK bit)\r\n
0xd000009d | ACK Invalid (subreason 2)\r\n
0xd000009e | ACK Invalid (subreason 3)\r\n
0xd000009f | ACK Invalid (subreason 4)\r\n
0xd00000a0 | Expected SYN\r\n
0xd00000a1 | Received RST (subreason 0)\r\n
0xd00000a2 | Received RST (subreason 1)\r\n
0xd00000a3 | Received RST (subreason 2)\r\n
0xd00000a4 | Received SYN while in SYN_RCVD state\r\n
0xd00000a5 | Simultaneous Connect\r\n
0xd00000a6 | PAWS Failed\r\n
0xd00000a7 | Land Attack (subreason 0)\r\n
0xd00000a8 | Land Attack (subreason 1)\r\n
0xd00000a9 | Land Attack (subreason 2)\r\n
0xd00000aa | Missed RST\r\n
0xd00000ab | Outside Receive Window (subreason 0)\r\n
0xd00000ac | Outside Receive Window (subreason 1)\r\n
0xd00000ad | Duplicate Segment\r\n
0xd00000ae | Closed Window\r\n
0xd00000af | TCB Removed\r\n
0xd00000b0 | FIN-WAIT2\r\n
0xd00000b1 | Reassembly Conflict\r\n
0xd00000b2 | FIN Received\r\n
0xd00000b3 | Listener received segment with invalid flags\r\n
0xd00000b4 | URG flag set but could not allocate urgent data state\r\n
0xd00000b5 | TCB was not inserted in TCB table\r\n
0xd00000b6 | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000b7 | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000b8 | Packet dropped by TIME-WAIT TCB (subreason 0)\r\n
0xd00000b9 | Packet dropped by TIME-WAIT TCB (subreason 1)\r\n
0xd00000ba | Packet dropped by TIME-WAIT TCB (subreason 2)\r\n
0xd00000bb | SYN+ACK with Fastopen cookie request\r\n
0xd00000bc | Listener dropped SYN because SO_PAUSE_ACCEPT was set\r\n
0xd00000bd | Listener dropped SYN to reduce memory pressure\r\n
0xd00000be | Bad source address\r\n
0xd00000bf | Not locally destined\r\n
0xd00000c0 | Protocol unreachable\r\n
0xd00000c1 | Port unreachable\r\n
0xd00000c2 | Bad length\r\n
0xd00000c3 | Malformed Header\r\n
0xd00000c4 | No route available\r\n
0xd00000c5 | Beyond scope\r\n
0xd00000c6 | Inspection drop\r\n
0xd00000c7 | Too many decapsulations\r\n
0xd00000c8 | Administratively prohibited\r\n
0xd00000c9 | Hop limit exceeded\r\n
0xd00000ca | Address unreachable\r\n
0xd00000cb | Fragment MTU exceeded\r\n
0xd00000cc | Buffer Length Exceeded\r\n
0xd00000cd | Address Resolution Timeout\r\n
0xd00000ce | Address Resolution Failure\r\n
0xd00000cf | IPsec failure\r\n
0xd00000d0 | Extension Headers Failure\r\n
0xd00000d1 | Allocation Failure\r\n
0xd00000d2 | Default\r\n
0xd00000d3 | NewReno\r\n
0xd00000d4 | CTCP\r\n
0xd00000d5 | DCTCP\r\n
0xd00000d6 | LEDBAT\r\n
0xd00000d7 | TcpTemplateTypeInternet\r\n
0xd00000d8 | TcpTemplateTypeDatacenter\r\n
0xd00000d9 | TcpTemplateTypeCompat\r\n
0xd00000da | TcpTemplateTypeDatacenterCustom\r\n
0xd00000db | TcpTemplateTypeInternetCustom\r\n
0xd00000dc | TcpTemplateTypeDefault\r\n
0xd00000dd | TcpTemplateTypeAutomatic\r\n
0xd00000de | No Failure\r\n
0xd00000df | Unknown\r\n
0xd00000e0 | System Policy\r\n
0xd00000e1 | NIC Capacity Reached\r\n
0xd00000e2 | System Low On Memory\r\n
0xd00000e3 | WFP driver / Stream inspection\r\n
0xd00000e4 | Weak Host Model Enabled\r\n
0xd00000e5 | Forwarding Enabled\r\n
0xd00000e6 | Hardware capability\r\n
0xd00000e7 | NDIS filter/NIC property\r\n
0xd00000e8 | Loopback fast path socket option not set on both ends\r\n
0xd00000e9 | Filter policy existed for the loopback connection\r\n
0xd00000ea | IPv4\r\n
0xd00000eb | IPv6\r\n
0xd00000ec | unbind\r\n
0xd00000ed | bind\r\n
0xd00000ee | port change\r\n
0xd00000ef | none\r\n
0xd00000f0 | receive hash\r\n
0xd00000f1 | receive scale\r\n
0xd00000f2 | enabled\r\n
0xd00000f3 | disabled\r\n
0xd00000f4 | removing\r\n
0xd00000f5 | adding\r\n
0xd00000f6 | complete binding initialization\r\n
0xd00000f7 | complete port initialization\r\n
0xd00000f8 | enumerate interface ports\r\n
0xd00000f9 | query port link state\r\n
0xd00000fa | query port interface index\r\n
0xd00000fb | query interface ports\r\n
0xd00000fc | query port RSS capabilities\r\n
0xd00000fd | get usable processors\r\n
0xd00000fe | query port driver version\r\n
0xd00000ff | query port RSS processor configuration\r\n
0xd0000100 | set receive scale parameters\r\n
0xd0000101 | set receive hash parameters\r\n
0xd0000102 | update interface ports\r\n
0xd0000103 | not available\r\n
0xd0000104 | available\r\n
0xd0000105 | available on ports\r\n
0xd0000106 | global configuration\r\n
0xd0000107 | active mode\r\n
0xd0000108 | Bind Adapter\r\n
0xd0000109 | Unbind Adapter (begin)\r\n
0xd000010a | Unbind Adapter (end)\r\n
0xd000010b | NetEvent Restart\r\n
0xd000010c | NetEvent Power-down\r\n
0xd000010d | NetEvent Power-up\r\n
0xd000010e | NetEvent NDK-enable\r\n
0xd000010f | NetEvent NDK-disable\r\n
0xd0000110 | NetEvent NDK usage stopped\r\n
0xd0000111 | Indicate new NDK interface arrival\r\n
0xd0000112 | Indicate NDK interface removal\r\n
0xd0000113 | Indicate NDK operational status change\r\n
0xd0000114 | Undefined\r\n
0xd0000115 | Adapter\r\n
0xd0000116 | QP\r\n
0xd0000117 | CQ\r\n
0xd0000118 | MR\r\n
0xd0000119 | MW\r\n
0xd000011a | PD\r\n
0xd000011b | SharedEndpoint\r\n
0xd000011c | Connector\r\n
0xd000011d | Listener\r\n
0xd000011e | SRQ\r\n
0xd000011f | Max\r\n
0xd0000120 | Async\r\n
0xd0000121 | Inline\r\n
0xd0000122 | Local\r\n
0xd0000123 | Remote\r\n
0xd0000124 | Privileged\r\n
0xd0000125 | Local\r\n
0xd0000126 | Remote\r\n
0xd0000127 | NotifyErrors\r\n
0xd0000128 | NotifyAny\r\n
0xd0000129 | NotifySolicited\r\n
0xd000012a | Invalid\r\n
0xd000012b | Software Slot allocated\r\n
0xd000012c | Hardware Slot allocated\r\n
0xd000012d | Policy error\r\n
0xd000012e | system error\r\n
0xd000012f | Enabled\r\n
0xd0000130 | Send request dropped\r\n
0xd0000131 | Receive dropped\r\n
0xd0000132 | Disconnect request dropped\r\n
0xd0000133 | Reset dropped\r\n
0xd0000134 | WFP API No Failure\r\n
0xd0000135 | WFP API WasRedirectedToProxy\r\n
0xd0000136 | WFP API RegisterForExitingEndpoint\r\n
0xd0000137 | WFP API ClassifiableFieldGetAf\r\n
0xd0000138 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000139 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd000013a | WFP API ClassifiableFieldGetRemotePort\r\n
0xd000013b | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd000013c | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd000013d | Processor Add\r\n
0xd000013e | Power Source Change\r\n
0xd000013f | AC\r\n
0xd0000140 | DC\r\n
0xd0000141 | DC Short Term\r\n
0xd0000142 | Unknown\r\n
0xd0000143 | is stopping timers\r\n
0xd0000144 | has stopped timers\r\n
0xd0000145 | is locking partitions\r\n
0xd0000146 | has locked partitions\r\n
0xd0000147 | is unlocking partitions\r\n
0xd0000148 | has unlocked partitions\r\n
0xd0000149 | is starting timers\r\n
0xd000014a | has started timers\r\n
0xd000014b | is starting\r\n
0xd000014c | is complete\r\n
0xd000014d | IP\r\n
0xd000014e | TCP\r\n
0xd000014f | leaving S0\r\n
0xd0000150 | entering S0\r\n
0xd0000151 | Unreachable\r\n
0xd0000152 | Incomplete\r\n
0xd0000153 | Probe\r\n
0xd0000154 | Delay\r\n
0xd0000155 | Stale\r\n
0xd0000156 | Reachable\r\n
0xd0000157 | Permanent\r\n
0xd0000158 | Maximum\r\n
0xd0000159 | Map\r\n
0xd000015a | Configure\r\n
0xd000015b | TlSuspectsReachability\r\n
0xd000015c | TlConfirmsReachability\r\n
0xd000015d | NaConfirmsReachability\r\n
0xd000015e | ProbeReachability\r\n
0xd000015f | DadSolicitation\r\n
0xd0000160 | NewDlAddress\r\n
0xd0000161 | TriggerNud\r\n
0xd0000162 | Resolve\r\n
0xd0000163 | Timeout\r\n
0xd0000164 | Sending neighbor solicitation\r\n
0xd0000165 | Received neighbor solicitation\r\n
0xd0000166 | Sending neighbor advertisement\r\n
0xd0000167 | Received neighbor advertisement\r\n
0xd0000168 | Sending router solicitation\r\n
0xd0000169 | Received router solicitation\r\n
0xd000016a | Sending router advertisement\r\n
0xd000016b | Received router advertisement\r\n
0xd000016c | Receive\r\n
0xd000016d | ReceiveAndInvalidate\r\n
0xd000016e | Send\r\n
0xd000016f | FastRegister\r\n
0xd0000170 | Bind\r\n
0xd0000171 | Invalidate\r\n
0xd0000172 | Read\r\n
0xd0000173 | Write\r\n
0xd0000174 | Not Activated\r\n
0xd0000175 | Activated\r\n
0xd0000176 | TCP connect\r\n
0xd0000177 | TCP send\r\n
0xd0000178 | UDP send\r\n
0xd0000179 | RAW send\r\n
0xd000017a | Received Router Advertisement\r\n
0xd000017b | AdminConfigured\r\n
0xd000017c | NetworkProperty\r\n
0xd000017d | CreateWolContext\r\n
0xd000017e | DeleteWolContext\r\n
0xd000017f | SetWolContext\r\n
0xd0000180 | ClearWolContext\r\n
0xd0000181 | WolContextEvicted\r\n
0xd0000182 | AddWolAddress\r\n
0xd0000183 | RemoveWolAddress\r\n
0xd0000184 | Send\r\n
0xd0000185 | Receive\r\n
0xd0000186 | WFP-ALE: RemoteEndPoint Address\r\n
0xd0000187 | WFP-ALE: RemoteEndPoint Port\r\n
0xd0000188 | WFP-ALE: LocalEndPoint Address\r\n
0xd0000189 | WFP-ALE: LocalEndPoint Port\r\n
0xd000018a | WFP-ALE: Partition Id\r\n
0xd000018b | WFP-ALE: Parition NumEnties\r\n
0xd000018c | SlowDownEntry\r\n
0xd000018d | SlowDownExit\r\n
0xd000018e | SlowDownTracking\r\n
0xd000018f | BaseDelayUpdate\r\n
0xd0000190 | Ack\r\n
0xd0000191 | DupAck\r\n
0xd0000192 | Timeout\r\n
0xd0000193 | Ecn\r\n
0xd0000194 | SpuriousTimeout\r\n
0xd0000195 | Network Context Constraint\r\n
0xd0000196 | Prefix Length Policy\r\n
0xd0000197 | Start Epoch Policy\r\n
0xd0000198 | Default Routes Disabled On Interface\r\n
0xd0000199 | Unconstrained Lookup Disallowed On Interface\r\n
0xd000019a | Interface Disconnected\r\n
0xd000019b | Route Invalid Lifetime\r\n
0xd000019c | Interface Constraint\r\n
0xd000019d | Scope Constraint\r\n
0xd000019e | Rechability\r\n
0xd000019f | Prefix Length\r\n
0xd00001a0 | Route And Interface Metrics\r\n
0xd00001a1 | Destination And Source Hash\r\n
0xd00001a2 | Route Order\r\n
0xd00001a3 | Dead Gateway\r\n
0xd00001a4 | OnLink Route\r\n
0xd00001a5 | Prefer Same Address\r\n
0xd00001a6 | Prefer Appropriate Scope\r\n
0xd00001a7 | Avoid Deprecated Addresses\r\n
0xd00001a8 | Prefer Home Addresses\r\n
0xd00001a9 | Prefer Outgoing Interface\r\n
0xd00001aa | Prefer Addresses Associated With NextHop\r\n
0xd00001ab | Prefer Matching Label\r\n
0xd00001ac | Prefer Temporary Addresses\r\n
0xd00001ad | System Defined Preference (Windows Specific)\r\n
0xd00001ae | Prefer Longest Matching Prefix With NextHop (Windows Specific)\r\n
0xd00001af | Prefer Longest Matching Prefix\r\n
0xd00001b0 | TimerArmed\r\n
0xd00001b1 | TimerFired\r\n
0xd00001b2 | Failed\r\n
0xd00001b3 | Init\r\n
0xd00001b4 | SetTimeSlotData\r\n
0xd00001b5 | SetTailTimeSlot\r\n
0xd00001b6 | EraseTimestamps\r\n
0xd00001b7 | GetRecoverySeq\r\n
0xd00001b8 | RttSampleUpdate\r\n
0xd00001b9 | TcpFastopenOff\r\n
0xd00001ba | TcpFastopenAccepting\r\n
0xd00001bb | TcpFastopenServerSendingCookie\r\n
0xd00001bc | TcpFastopenServerSentCookie\r\n
0xd00001bd | TcpFastopenNegotiate\r\n
0xd00001be | TcpFastopenAttempt\r\n
0xd00001bf | TcpFastopenNegotiateSuccess\r\n
0xd00001c0 | TcpFastopenAttemptSuccess\r\n
0xd00001c1 | TcpFastopenCookieRollover\r\n
0xd00001c2 | TcpFastopenFailed\r\n
0xd00001c3 | TcpFastopenFailedBlocklist\r\n
0xd00001c4 | TcpFastopenServerAcceptSuccess\r\n
0xd00001c5 | TcpFastopenServerAcceptTimeout\r\n
0xd00001c6 | TcpFastopenServerAcceptSendData\r\n
0xd00001c7 | TcpFastopenFailedSimultaneousConnect\r\n
0xd00001c8 | TcpFastopenFailedInvalidCookie\r\n
0xd00001c9 | TcpFastopenFailedSingleTimeout\r\n
0xd00001ca | TcpFastopenFailedTimeout\r\n
0xd00001cb | TcpFastopenFailedReset\r\n
0xd00001cc | TcpFastopenFallback\r\n
0xd00001cd | General failure\r\n
0xd00001ce | Truncated header\r\n
0xd00001cf | Invalid checksum\r\n
0xd00001d0 | Inspection drop\r\n
0xd00001d1 | Rejecting loopback neighbor discovery\r\n
0xd00001d2 | Unknown type/code\r\n
0xd00001d3 | Truncated IP header\r\n
0xd00001d4 | Oversized IP header\r\n
0xd00001d5 | No handler\r\n
0xd00001d6 | Not responding with error for error\r\n
0xd00001d7 | Invalid source\r\n
0xd00001d8 | Interface rate limit\r\n
0xd00001d9 | Path rate limit\r\n
0xd00001da | No route\r\n
0xd00001db | No matching request\r\n
0xd00001dc | Buffer too small\r\n
0xd00001dd | Failed to obtain ancillary data\r\n
0xd00001de | Incorrect hop limit\r\n
0xd00001df | Unknown code\r\n
0xd00001e0 | Source not linklocal\r\n
0xd00001e1 | Truncated ND header\r\n
0xd00001e2 | Invalid ND option SourceLinkAddr\r\n
0xd00001e3 | Invalid ND option MTU\r\n
0xd00001e4 | Invalid ND option PrefixInformation\r\n
0xd00001e5 | Invalid ND option RouteInformation\r\n
0xd00001e6 | Invalid ND option RDNSS\r\n
0xd00001e7 | Invalid ND option DNSSL\r\n
0xd00001e8 | Packet parsing failure\r\n
0xd00001e9 | Echo Reply\r\n
0xd00001ea | Destination Unreachable\r\n
0xd00001eb | Packet Too Big\r\n
0xd00001ec | Destination Unreachable(v4)/Time Exceeded(v6)\r\n
0xd00001ed | Source Quench(v4)/Parameter Problem(v6)\r\n
0xd00001ee | Redirect\r\n
0xd00001ef | Echo Request\r\n
0xd00001f0 | Router Advertisement\r\n
0xd00001f1 | Router Solicitation\r\n
0xd00001f2 | Time Exceeded\r\n
0xd00001f3 | Parameter Problem\r\n
0xd00001f4 | Timestamp Request\r\n
0xd00001f5 | Timestamp Reply\r\n
0xd00001f6 | Address Mask Request\r\n
0xd00001f7 | Address Mask Reply\r\n
0xd00001f8 | Echo Request\r\n
0xd00001f9 | Echo Reply\r\n
0xd00001fa | Multicast Listener Query\r\n
0xd00001fb | Multicast Listener Report\r\n
0xd00001fc | Multicast Listener Done\r\n
0xd00001fd | Router Solicitation\r\n
0xd00001fe | Router Advertisement\r\n
0xd00001ff | Neighbor Solicitation\r\n
0xd0000200 | Neighbor Advertisement\r\n
0xd0000201 | Redirect Message\r\n
0xd0000202 | Multicast Listener Discovery\r\n
0xd0000203 | Not Parsed\r\n
0xd0000204 | Periodic\r\n
0xd0000205 | Aperiodic\r\n
0xd0000206 | Unknown\r\n
0xd0000207 | Public\r\n
0xd0000208 | Private\r\n
0xd0000209 | Domain\r\n
0xd000020a | Remote\r\n
0xd000020b | Link\r\n
0xd000020c | NonDomainNetwork\r\n
0xd000020d | DomainNetwork\r\n
0xd000020e | DomainAuthenticated\r\n
0xd000020f | InterfaceAddition\r\n
0xd0000210 | InterfaceDeletion\r\n
0xd0000211 | ZoneChange\r\n
0xd0000212 | ConfigurationFlagChange\r\n
0xd0000213 | ForwardingEnable\r\n
0xd0000214 | ForwardingDisable\r\n
0xd0000215 | WeakHostReceiveEnable\r\n
0xd0000216 | WeakHostReceiveDisable\r\n
0xd0000217 | NetworkCategoryStateChange\r\n
0xd0000218 | MetricChange\r\n
0xd0000219 | MediaConnect\r\n
0xd000021a | MediaDisconnect\r\n
0xd000021b | OffloadCapabilityChange\r\n
0xd000021c | DisableDefaultRoutesSet\r\n
0xd000021d | DisableDefaultRoutesReset\r\n
0xd000021e | ForceTunnelingSet\r\n
0xd000021f | ForceTunnelingReset\r\n
0xd0000220 | LimitedLinkConnectivitySet\r\n
0xd0000221 | LimitedLinkConnectivityReset\r\n
0xd0000222 | LocalityConfigChange\r\n
0xd0000223 | DisableUnconstrainedRouteLookupSet\r\n
0xd0000224 | DisableUnconstrainedRouteLookupReset\r\n
0xd0000225 | PortStateChange\r\n
0xd0000226 | NoInternetConnectivity\r\n
0xd0000227 | NoInternetDnsResolutionSucceeded\r\n
0xd0000228 | InternetConnectivityDetected\r\n
0xd0000229 | Timeout\r\n
0xd000022a | DadStarted\r\n
0xd000022b | OptimisticDadStarted\r\n
0xd000022c | DadPassed\r\n
0xd000022d | NSReceived\r\n
0xd000022e | NAReceived\r\n
0xd000022f | InterfaceDisabled\r\n
0xd0000230 | DadDisabled\r\n
0xd0000231 | AddressAddition\r\n
0xd0000232 | AddressDeletion\r\n
0xd0000233 | DadStatePreferred\r\n
0xd0000234 | DadStateDuplicate\r\n
0xd0000235 | DadStateDeprecated\r\n
0xd0000236 | SkipAsSourceSet\r\n
0xd0000237 | SkipAsSourceReset\r\n
0xd0000238 | TunnelSkipAsSourceSet\r\n
0xd0000239 | TunnelSkipAsSourceReset\r\n
0xd000023a | ZoneChange\r\n
0xd000023b | NeighborAddition\r\n
0xd000023c | NeighborDeletion\r\n
0xd000023d | NeighborUnreachable\r\n
0xd000023e | NeighborReachable\r\n
0xd000023f | NeighborAddressUpdate\r\n
0xd0000240 | DeadRouteTimeout\r\n
0xd0000241 | DeadRouteProbeTimeout\r\n
0xd0000242 | AllRoutesDead\r\n
0xd0000243 | TlConfirmsForwardReachability\r\n
0xd0000244 | DeadGatewayDetected\r\n
0xd0000245 | RouterRedirect\r\n
0xd0000246 | ProbeConnectionFailed\r\n
0xd0000247 | ConfigurationChange\r\n
0xd0000248 | Alive\r\n
0xd0000249 | Dead\r\n
0xd000024a | Probe\r\n
0xd000024b | Disable\r\n
0xd000024c | Enable\r\n
0xd000024d | NotConfident\r\n
0xd000024e | TCP Fastopen\r\n
0xd000024f | Init\r\n
0xd0000250 | StatusIndication\r\n
0xd0000251 | GlobalSetting\r\n
0xd0000252 | Forwarding\r\n
0xd0000253 | IncompatibleCallout\r\n
0xd0000254 | RA DNS information change\r\n
0xd0000255 | RA DNS entry added\r\n
0xd0000256 | RA DNS entry expired by RA\r\n
0xd0000257 | RA DNS entry expired by timer\r\n
0xd0000258 | RA DNS entry lifetime reset\r\n
0xd0000259 | RA DNS entry reordered\r\n
0xd000025a | RA DNS entry deleted due to max limit\r\n
0xd000025b | RA DNS entry lifetime updated\r\n
0xd000025c | RA DNS ND entry ignored due to limit\r\n
0xd000025d | RA DNS ND entry ignored due to memory failure\r\n
0xd000025e | RA DNS ND entry ignored due to zero lifetime\r\n
0xd000025f | RA DNS ND entries corrupted\r\n
0xd0000260 | RA DNS RouterContext init failed\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x11000034 | SQM\r\n
0x30000000 | Info\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto = %3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm = %6, MaxDataRetransmissions = %7, DelayedAckTicks = %8 msec, DelayedAckFrequency = %9, RACK enabled = %10, Tail Loss Probe enabled = %11.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5, Event = %6.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick = %4 Time = %5.\r\n
0xb0000527 | %1 timer rescheduled by processor %2 for processor %3 at Tick = %4 to Tick = %5, OldScheduledExpiration = %6 NewScheduledExpiration = %7 DueTime = %8 Aperiodic = %9.\r\n
0xb0000528 | %1 timer fired on processor %2 at Tick = %3, was scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for Destination %4 in Compartment %5, Reason: %8 (Rule %6.%7).\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0000558 | Teredo Add -- PID: %1 started listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb0000559 | Teredo Remove -- PID: %1 stopped listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb000055a | IP: RouteLookup - API: %1 DstAddr: %3 ConstrainSrcAddr: %4 ConstrainIfIndex: %5 ConstraintOveridden: %6 ReturnConstrained: %7 OutgoingIfIndex: %8 NextHopAddr: %9 Status: %10\r\n
0xb000055b | IP: SourceAddrLookup - DstAddr: %2 ConstrainSrcAddr: %3 ConstrainIfIndex: %4 OutgoingIfIndex: %5 ReturnConstrained: %6 SelectedSrcAddr: %7\r\n
0xb000055c | WFP-ALE: Partition Count=%1 Partition Mask=%2: Partition Id=%d Partition NumEntries = %4.\r\n
0xb000055d | WFP-ALE: HotAdd/Remove: Old Partiton Count=%1 Old Partition Mask=%2 New Partiton Count=%1 New Partition Mask=%2.\r\n
0xb000055e | WFP-ALE: RemoteEndPoint Insertion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb000055f | WFP-ALE: RemoteEndPoint Deletion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb0000560 | WFP-ALE: ALE: low memory state detected. LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000561 | WFP-ALE: leaving low memory state. HighMemoryEvent = %1 HighNonPagedPoolEvent = %2.\r\n
0xb0000562 | WFP-ALE: Dpc for cleanup initiated: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000563 | WFP: Dpc for cleanup QUEUED or RE-QUEUED: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000564 | TCP: LEDBAT %2: Connection %1, BaseDelayMs = %6, CurrentDelayMs = %7, CWnd = %3, SsThresh = %4, SndWnd = %5, DelayBasedCwndFactor %9%%, RemainingTimeMs = %8.\r\n
0xb0000565 | TCP: AssociateNameResContext Endpoint: %1 Status: %16 NameResolutionContext: %2 DnsName: %3 InterfaceIndex: %4 IPAddrCount: %5 IPAddrs: %7 %9 %11 %13 %15\r\n
0xb0000566 | TCP: InspectConnectWithNameResContext Connection: %5 (local: %2 remote: %4) NameResolutionContext: %6 DnsName: %7 Status: %8.\r\n
0xb0000567 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 InterfaceMetric: %10 RouteMetric: %11] is preferred over Route [DestinationPrefix: %14/%12 NextHop: %16 InterfaceIndex: %17 InterfaceMetric: %18 RouteMetric: %19] for Destination: %3 in Compartment: %1, Reason: %20.\r\n
0xb0000568 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 RouteMetric: %10] is blocked for Destination: %3 ConstrainInterfaceIndex: %11 ConstrainScopeZone: %12 in Compartment: %1, Reason: %13.\r\n
0xb0000569 | TCP: Tail Loss Probe Send Connection = %1 SndUna = %2, SndMax = %3, SendAvailable = %4, TailProbeSeq = %5, TailProbeLast = %6, ControlsToSend = %7, ThFlags = %8.\r\n
0xb000056a | TCP: Tail Loss Probe Event Connection = %1, Event = %2.\r\n
0xb000056b | TCP: RACK Event Connection = %1, Event = %2, MinRTT = %3, ReoWind = %4, TimeSlotDeltaMin = %5, SeqNum = %6, Timestamp = %7, RttSample = %8.\r\n
0xb000056c | TCP: Fastopen state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000056d | UDP: endpoint (family=%5 pid=%3) create failed: address family not attached.\r\n
0xb000056e | UDP: endpoint %1 (family=%5 pid=%3) create failed: compartment %4 not found.\r\n
0xb000056f | UDP: endpoint %1 (family=%5 pid=%3) created.\r\n
0xb0000570 | UDP: endpoint %1 (family=%5 pid=%3) create failed: inspection status = %2\r\n
0xb0000571 | UDP: endpoint %4 bind failed: address %2 cannot be resolved, status = %3\r\n
0xb0000572 | UDP: endpoint %4 (sockaddr=%2) bind failed: port-acquisition status = %3\r\n
0xb0000573 | UDP: endpoint %4 (sockaddr=%2) bind failed: inspection status = %3\r\n
0xb0000574 | UDP: endpoint %4 (sockaddr=%2) bound.\r\n
0xb0000575 | UDP: endpoint %4 (sockaddr=%2) closed.\r\n
0xb0000576 | UDP: endpoint %4 closed.\r\n
0xb0000577 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address resolution status = %6\r\n
0xb0000578 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address validation failed.\r\n
0xb0000579 | UDP: endpoint %1 (sockaddr=%3) send messages %5: source-address selection status = %6\r\n
0xb000057a | UDP: endpoint %1 too many packets queued for the pending join path.\r\n
0xb000057b | UDP: address family %2added to interface %1.\r\n
0xb000057c | UDP: address family %2removed from interface %1.\r\n
0xb000057d | UDP: Failure initializing transport protocol, status = %1\r\n
0xb000057e | UDP: Failure starting NLNPI client, status = %1\r\n
0xb000057f | UDP: Failure initializing NSI support, status = %1\r\n
0xb0000580 | UDP: Failure starting TLNPI provider, status = %1\r\n
0xb0000581 | UDP: Failure initializing QoS support, status = %1\r\n
0xb0000582 | UDP: Failure starting %1, status = %2\r\n
0xb0000583 | UDP: endpoint %1 (sockaddr=%3) send messages %5: could not allocate send context.\r\n
0xb0000584 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path af failure, status = %6\r\n
0xb0000585 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path missing next hop failure.\r\n
0xb0000586 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path next hop address failure.\r\n
0xb0000587 | TCP: Early Retransmission, FACK or RACK, Connection = %1, SndUna = %2, SackIsLostSeq = %3, DupAckCount = %4\r\n
0xb0000588 | TCP: Ignoring fastopen SYN option due to limit on concurrent SYN_RCVD fastopen connections, Connection = %1, SynRcvdLimit = %2\r\n
0xb0000589 | TCP: Failed to update fastopen key state, Location = %1, Status = %2. Server-side fastopen will be disabled\r\n
0xb000058a | TCP: Fast Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058b | TCP: SACK Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058c | TCP: Limited Transmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058d | TCP: SACK Retransmit Additional Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058e | %1: %2message. Type = %3, Code = %4, CompartmentId = %5, SourceAddress = %7, DestAddress = %9\r\n
0xb000058f | %1: %2path drop. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11\r\n
0xb0000590 | %1: Echo timeout. Status = %4\r\n
0xb0000591 | %1 Timer state changed to %3 by Processor %2 Usage = %4 at Tick = %5\r\n
0xb0000592 | TCP: connection %1 send complete %3 bytes at %4 (%2).\r\n
0xb0000593 | IP: Compartment creation. Compartment = %1, Protocol = %2, Private = %3, Status = %4.\r\n
0xb0000594 | IP: Compartment deletion. Compartment = %1, Protocol = %2.\r\n
0xb0000595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13.\r\n
0xb0000596 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5 CwrMax = %6.\r\n
0xb0000597 | IP: Compartment cleanup. Compartment = %1, Protocol = %2.\r\n
0xb0000598 | IP: Interface network category state change. Interface = %1, Compartment = %2 , Protocol = %3, NetworkCategory = %4, DomainNetworkLocation = %5, DomainType = %6, Signature = %7.\r\n
0xb0000599 | IP: Interface creation. Interface = %1, Compartment = %2, Protocol = %3, PhysicalMediumType = %4, Status = %5.\r\n
0xb000059a | IP: Interface deletion. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059b | IP: Interface cleanup. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059c | IP: SubInterface creation. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4, Status = %5.\r\n
0xb000059d | IP: SubInterface deletion. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059e | IP: SubInterface cleanup. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059f | IP: Interface change Notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005a0 | IP: Interface internet connectivity status change. Interface = %1, Compartment = %2, Protocol = %3, OldConnectivityStatus = %4, NewConnectivityStatus = %5.\r\n
0xb00005a1 | IP: Address change notification. Address = %2, Interface = %3, Compartment = %4, Protocol = %5, Reason = %6.\r\n
0xb00005a2 | IP: Route change notification. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, NotifyFlags = %8.\r\n
0xb00005a3 | IP: Neighbor change notification. IpAddress = %2, DlAddress = %4, Interface = %5, Compartment = %6, State = %7, Reason = %8.\r\n
0xb00005a4 | IP: Address DAD state change. Address = %2, Interface = %3, Compartment = %4, OldState = %5, NewState = %6, Reason = %7.\r\n
0xb00005a5 | IP: Route Dead Gateway Detection state change. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, OldState = %8, NewState = %9, OldProbeCount = %10, NewProbeCount = %11, OldUnreachablePaths = %12, NewUnreachablePaths = %13, OldMovedPaths = %14, NewMovedPaths = %15, TotalPaths = %16, OldStateChangeTick = %17, NewStateChangeTick = %18, DgdNeedsReset = %19, Reason = %20.\r\n
0xb00005a6 | IP: Disconnecting TCP connections with Address = %2, Interface = %3, Compartment = %4, SkipLocal = %5, SkipOnLink = %6.\r\n
0xb00005a7 | TCP: connection %1: Sending paced chunk of %6 bytes with CWnd = %2, SndWnd = %3, BytesAvailable = %4, BytesOutstanding = %5\r\n
0xb00005a8 | Fallback: Context = %1, Feature = %2, TraceReason = %3, Confidence = %4, Successes = %5, Failures = %6\r\n
0xb00005a9 | TCPIP: TCB %1 using fast loopback\r\n
0xb00005aa | IP: Router information change notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005ab | IP: %1. Interface = %2, Compartment = %3, RouterAddress = %5, DNS Server/Suffix: %7 %8, Lifetime = %9.\r\n
0xb00005ac | IP: Route rundown. Interface = %1, Compartment = %2, Prefix = %4/%5, NextHop = %7, Metric = %8, State = %9, Origin = %10, Age = %11, ValidLifetime = %12, PreferredLifetime = %13, Flags = %14.\r\n
0xb00005ad | TCP: CUBIC ECN event. Connection %1, CWnd %2, SSThresh = %3, SndUna = %4\r\n
0xb00005ae | INETINSPECT: Owner = %1, InspectHandle = %2, InspectType = %3, Action = %4, Status = %5\r\n
0xb00005b0 | FallbackCheck: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b1 | FallbackUpdate: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b2 | Fallback: Permanently disabling feature, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b3 | Fallback: Enabling feature for this boot session, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b4 | Fallback: Feature previously disabled, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b5 | TCP Fastopen fallback update: Tcb = %1, FastopenState = %2, DataBytesIn = %3, ShutdownStatus = %4, ProbeStatus = %5\r\n
0xb00005b6 | Disabling feature until connectivity is established: CompartmentId =%1, IfIndex = %2, Feature = %3, ConnectivityStatus = %4\r\n
0xb00005b7 | Disabling %1 for loopback connection\r\n
0xb00005b8 | Disabling TCP Fastopen for BaseEndpoint = %1 because an incompatible WFP callout is installed\r\n
0xb00005b9 | IP: Setting source constraint for route lookup - Compartment: %1 DstAddr: %3 ConstrainSrcAddr: %5 ConstrainIfIndex: %6 ConstraintFlags: %7\r\n
0xb00005ba | WFP-ALE: RemoteEndPoint Insertion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bb | WFP-ALE: RemoteEndPoint Deletion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010452 | IP: Interface media disconnect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001045a | IP: Address DAD successful. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001045b | IP: Address DAD failed. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2, DL address of packet = %5.\r\n
0xb001045c | IP: Address DAD started. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010467 | IP: Address addition. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010468 | IP: Address deletion. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001046a | Framing: Interface operation status change. Interface = %1, Compartment = %4, Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0010470 | Framing: NDIS pause event. Interface = %1, Compartment = %3.\r\n
0xb0010471 | Framing: NDIS restart event. Interface = %1, Compartment = %3.\r\n
0xb0010478 | IP: Interface property change. Interface = %1, Compartment = %10, Protocol = %11, Advertise = %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7, WeakHostSend = %8, WeakHostReceive = %9.\r\n
0xb00104b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, Address = %4 %3 %6.\r\n
0xb00104b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7.\r\n
0xb0010529 | IP: Interface media connect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052a | IP: Interface limited link connectivity set. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052b | IP: Interface limited link connectivity reset. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052c | IP: Neighbor state change. IPAddress = %3, DLAddress = %5, Interface = %1, Compartment = %9, OldState = %6, NewState = %7, Event = %8.\r\n
0xb001052d | IP: Neighbor Discovery. Event = %5, Interface = %1, Compartment = %6, SourceIpAddress = %3, TargetIpAddress = %4.\r\n
0xb001052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions: %6, Reason: %10 (Rule %7 %8.%9).\r\n
0xb0010534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb001054e | IP: Interface configuration flags updated. Interface = %1, Compartment = %5, Protocol = %6, Property = %2, Value = %3, Event = %4.\r\n
0xb0010557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9, NrtNameResolutionId %10\r\n
0xb0010565 | TCP: AssociateNameResContext EndpointObj: %1 IsConnectionObj: %2 NameResContext: %3 Status: %4\r\n
0xb00204b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, Address = %4 %3 %6.\r\n
0xb00304b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Metric = %11, Connected = %12, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, InternetConnectivityStatus = %13, Flags = %14, Address = %4 %3 %6.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | PacingTimer\r\n
0xd000002c | DisconnectTimer\r\n
0xd000002d | SwsTimer\r\n
0xd000002e | ReassemblyRateTimer\r\n
0xd000002f | SynOrRstValidationTimer\r\n
0xd0000030 | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000031 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000032 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000033 | TCP_KEEPALIVE\r\n
0xd0000034 | TCP_MAXSEG\r\n
0xd0000035 | TCP_MAXRT\r\n
0xd0000036 | TCP_STDURG\r\n
0xd0000037 | TCP_NOURG\r\n
0xd0000038 | TCP_ATMARK\r\n
0xd0000039 | TCP_NOSYNRETRIES\r\n
0xd000003a | TCP_TIMESTAMPS\r\n
0xd000003b | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003c | TCP_CONGESTION_ALGORITHM\r\n
0xd000003d | TCP_DELAY_FIN_ACK\r\n
0xd000003e | SO_DEBUG\r\n
0xd000003f | SO_ACCEPTCONN\r\n
0xd0000040 | SO_REUSEADDR\r\n
0xd0000041 | SO_KEEPALIVE\r\n
0xd0000042 | SO_DONTROUTE\r\n
0xd0000043 | SO_BROADCAST\r\n
0xd0000044 | SO_USELOOPBACK\r\n
0xd0000045 | SO_LINGER\r\n
0xd0000046 | SO_OOBINLINE\r\n
0xd0000047 | SO_SNDBUF\r\n
0xd0000048 | SO_RCVBUF\r\n
0xd0000049 | SO_CONDITIONAL_ACCEPT\r\n
0xd000004a | SO_PAUSE_ACCEPT\r\n
0xd000004b | SO_COMPARTMENT_ID\r\n
0xd000004c | SO_RANDOMIZE_PORT\r\n
0xd000004d | SO_PORT_SCALABILITY\r\n
0xd000004e | NldsInvalid\r\n
0xd000004f | NldsTentative\r\n
0xd0000050 | NldsDuplicate\r\n
0xd0000051 | NldsDeprecated\r\n
0xd0000052 | NldsPreferred\r\n
0xd0000053 | Indicate\r\n
0xd0000054 | Pend\r\n
0xd0000055 | Satisfy\r\n
0xd0000056 | NdisPhysicalMediumUnspecified\r\n
0xd0000057 | NdisPhysicalMediumWirelessLan\r\n
0xd0000058 | NdisPhysicalMediumCableModem\r\n
0xd0000059 | NdisPhysicalMediumPhoneLine\r\n
0xd000005a | NdisPhysicalMediumDSL\r\n
0xd000005b | NdisPhysicalMedium1394\r\n
0xd000005c | NdisPhysicalMediumWirelessWan\r\n
0xd000005d | NdisPhysicalMediumNative802_11\r\n
0xd000005e | NdisPhysicalMediumBluetooth\r\n
0xd000005f | NdisPhysicalMediumInfiniband\r\n
0xd0000060 | NdisPhysicalMediumWiMax\r\n
0xd0000061 | NdisPhysicalMedium802_3\r\n
0xd0000062 | NdisPhysicalMedium802_5\r\n
0xd0000063 | NdisPhysicalMediumIrda\r\n
0xd0000064 | NdisPhysicalMediumWiredWAN\r\n
0xd0000065 | IP checksum offload not computed\r\n
0xd0000066 | TCP checksum offload not computed\r\n
0xd0000067 | UDP checksum offload not computed\r\n
0xd0000068 | Header not aligned on 4-byte boundary\r\n
0xd0000069 | IP fragmentation\r\n
0xd000006a | Source address is not unicast\r\n
0xd000006b | Destination address is not unicast\r\n
0xd000006c | Ethernet and IP header not contiguous\r\n
0xd000006d | IP options present\r\n
0xd000006e | ESP over UDP\r\n
0xd000006f | Lack contiguous space for upper layer headers\r\n
0xd0000070 | WFP filters present\r\n
0xd0000071 | Nexthop is unavailable\r\n
0xd0000072 | Path has been invalidated due to policy change\r\n
0xd0000073 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000074 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000075 | Session state is not compatible\r\n
0xd0000076 | TCP options present\r\n
0xd0000077 | UDP IPv6 checksum absent in packet\r\n
0xd0000078 | Packet is for a loopback interface\r\n
0xd0000079 | Packet is from a Raw Socket\r\n
0xd000007a | TL Ancillary headers present\r\n
0xd000007b | NL Ancillary headers present\r\n
0xd000007c | Type of Service present\r\n
0xd000007d | IpSec headers present\r\n
0xd000007e | Interface is not Ethernet\r\n
0xd000007f | Nbl check failed\r\n
0xd0000080 | Destination address is unknown\r\n
0xd0000081 | Failed to allocate the WSD cache\r\n
0xd0000082 | Failure initializing PnP work queue\r\n
0xd0000083 | Failed to get persistent parameters\r\n
0xd0000084 | Rejected persistent parameters\r\n
0xd0000085 | qualified profile\r\n
0xd0000086 | qualified destination\r\n
0xd0000087 | sample collection completion\r\n
0xd0000088 | idle time expiration\r\n
0xd0000089 | allocation\r\n
0xd000008a | new sample request\r\n
0xd000008b | configuration change\r\n
0xd000008c | Idle\r\n
0xd000008d | ProbingWs\r\n
0xd000008e | ProbeWait\r\n
0xd000008f | ProbingWithoutWs\r\n
0xd0000090 | RecordWait\r\n
0xd0000091 | EreQualified\r\n
0xd0000092 | Qualified\r\n
0xd0000093 | Source Unspecified\r\n
0xd0000094 | Destination is multicast\r\n
0xd0000095 | Header is invalid (location 0)\r\n
0xd0000096 | Checksum is invalid\r\n
0xd0000097 | Transport endpoint was not found\r\n
0xd0000098 | Connected path error\r\n
0xd0000099 | Session state error\r\n
0xd000009a | Receive Inspection\r\n
0xd000009b | ACK Invalid (subreason 0) (invalid ACK in SYN_SENT state)\r\n
0xd000009c | Expected SYN\r\n
0xd000009d | Received RST (subreason 0)\r\n
0xd000009e | Received SYN while in SYN_RCVD state\r\n
0xd000009f | Simultaneous Connect\r\n
0xd00000a0 | PAWS Failed\r\n
0xd00000a1 | Land Attack (subreason 0)\r\n
0xd00000a2 | Missed RST\r\n
0xd00000a3 | Outside Receive Window (subreason 0)\r\n
0xd00000a4 | Duplicate Segment\r\n
0xd00000a5 | Closed Window\r\n
0xd00000a6 | TCB Removed\r\n
0xd00000a7 | FIN-WAIT2\r\n
0xd00000a8 | Reassembly Conflict\r\n
0xd00000a9 | FIN Received\r\n
0xd00000aa | Listener received segment with invalid flags\r\n
0xd00000ab | URG flag set but could not allocate urgent data state\r\n
0xd00000ac | TCB was not inserted in TCB table\r\n
0xd00000ad | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000ae | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000af | Packet dropped by TIME-WAIT TCB (subreason 0)\r\n
0xd00000b0 | SYN+ACK with Fastopen cookie request\r\n
0xd00000b1 | Listener dropped SYN because SO_PAUSE_ACCEPT was set\r\n
0xd00000b2 | Listener dropped SYN to reduce memory pressure\r\n
0xd00000b3 | Bad source address\r\n
0xd00000b4 | Not locally destined\r\n
0xd00000b5 | Protocol unreachable\r\n
0xd00000b6 | Port unreachable\r\n
0xd00000b7 | Bad length\r\n
0xd00000b8 | Malformed Header\r\n
0xd00000b9 | No route available\r\n
0xd00000ba | Beyond scope\r\n
0xd00000bb | Inspection drop\r\n
0xd00000bc | Too many decapsulations\r\n
0xd00000bd | Administratively prohibited\r\n
0xd00000be | Hop limit exceeded\r\n
0xd00000bf | Address unreachable\r\n
0xd00000c0 | Fragment MTU exceeded\r\n
0xd00000c1 | Buffer Length Exceeded\r\n
0xd00000c2 | Address Resolution Timeout\r\n
0xd00000c3 | Address Resolution Failure\r\n
0xd00000c4 | IPsec failure\r\n
0xd00000c5 | Extension Headers Failure\r\n
0xd00000c6 | Allocation Failure\r\n
0xd00000c7 | Default\r\n
0xd00000c8 | NewReno\r\n
0xd00000c9 | CTCP\r\n
0xd00000ca | DCTCP\r\n
0xd00000cb | LEDBAT\r\n
0xd00000cc | TcpTemplateTypeInternet\r\n
0xd00000cd | TcpTemplateTypeDatacenter\r\n
0xd00000ce | TcpTemplateTypeCompat\r\n
0xd00000cf | TcpTemplateTypeDatacenterCustom\r\n
0xd00000d0 | TcpTemplateTypeInternetCustom\r\n
0xd00000d1 | TcpTemplateTypeDefault\r\n
0xd00000d2 | TcpTemplateTypeAutomatic\r\n
0xd00000d3 | No Failure\r\n
0xd00000d4 | Unknown\r\n
0xd00000d5 | System Policy\r\n
0xd00000d6 | NIC Capacity Reached\r\n
0xd00000d7 | System Low On Memory\r\n
0xd00000d8 | WFP driver / Stream inspection\r\n
0xd00000d9 | Weak Host Model Enabled\r\n
0xd00000da | Forwarding Enabled\r\n
0xd00000db | Hardware capability\r\n
0xd00000dc | NDIS filter/NIC property\r\n
0xd00000dd | Loopback fast path socket option not set on both ends\r\n
0xd00000de | Filter policy existed for the loopback connection\r\n
0xd00000df | IPv4\r\n
0xd00000e0 | IPv6\r\n
0xd00000e1 | unbind\r\n
0xd00000e2 | bind\r\n
0xd00000e3 | port change\r\n
0xd00000e4 | none\r\n
0xd00000e5 | receive hash\r\n
0xd00000e6 | receive scale\r\n
0xd00000e7 | enabled\r\n
0xd00000e8 | disabled\r\n
0xd00000e9 | removing\r\n
0xd00000ea | adding\r\n
0xd00000eb | complete binding initialization\r\n
0xd00000ec | complete port initialization\r\n
0xd00000ed | enumerate interface ports\r\n
0xd00000ee | query port link state\r\n
0xd00000ef | query port interface index\r\n
0xd00000f0 | query interface ports\r\n
0xd00000f1 | query port RSS capabilities\r\n
0xd00000f2 | get usable processors\r\n
0xd00000f3 | query port driver version\r\n
0xd00000f4 | query port RSS processor configuration\r\n
0xd00000f5 | set receive scale parameters\r\n
0xd00000f6 | set receive hash parameters\r\n
0xd00000f7 | update interface ports\r\n
0xd00000f8 | not available\r\n
0xd00000f9 | available\r\n
0xd00000fa | available on ports\r\n
0xd00000fb | global configuration\r\n
0xd00000fc | active mode\r\n
0xd00000fd | Bind Adapter\r\n
0xd00000fe | Unbind Adapter (begin)\r\n
0xd00000ff | Unbind Adapter (end)\r\n
0xd0000100 | NetEvent Restart\r\n
0xd0000101 | NetEvent Power-down\r\n
0xd0000102 | NetEvent Power-up\r\n
0xd0000103 | NetEvent NDK-enable\r\n
0xd0000104 | NetEvent NDK-disable\r\n
0xd0000105 | NetEvent NDK usage stopped\r\n
0xd0000106 | Indicate new NDK interface arrival\r\n
0xd0000107 | Indicate NDK interface removal\r\n
0xd0000108 | Indicate NDK operational status change\r\n
0xd0000109 | Undefined\r\n
0xd000010a | Adapter\r\n
0xd000010b | QP\r\n
0xd000010c | CQ\r\n
0xd000010d | MR\r\n
0xd000010e | MW\r\n
0xd000010f | PD\r\n
0xd0000110 | SharedEndpoint\r\n
0xd0000111 | Connector\r\n
0xd0000112 | Listener\r\n
0xd0000113 | SRQ\r\n
0xd0000114 | Max\r\n
0xd0000115 | Async\r\n
0xd0000116 | Inline\r\n
0xd0000117 | Local\r\n
0xd0000118 | Remote\r\n
0xd0000119 | Privileged\r\n
0xd000011a | Local\r\n
0xd000011b | Remote\r\n
0xd000011c | NotifyErrors\r\n
0xd000011d | NotifyAny\r\n
0xd000011e | NotifySolicited\r\n
0xd000011f | Invalid\r\n
0xd0000120 | Software Slot allocated\r\n
0xd0000121 | Hardware Slot allocated\r\n
0xd0000122 | Policy error\r\n
0xd0000123 | system error\r\n
0xd0000124 | Enabled\r\n
0xd0000125 | Send request dropped\r\n
0xd0000126 | Receive dropped\r\n
0xd0000127 | Disconnect request dropped\r\n
0xd0000128 | Reset dropped\r\n
0xd0000129 | WFP API No Failure\r\n
0xd000012a | WFP API WasRedirectedToProxy\r\n
0xd000012b | WFP API RegisterForExitingEndpoint\r\n
0xd000012c | WFP API ClassifiableFieldGetAf\r\n
0xd000012d | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd000012e | WFP API ClassifiableFieldGetLocalPort\r\n
0xd000012f | WFP API ClassifiableFieldGetRemotePort\r\n
0xd0000130 | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd0000131 | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd0000132 | Processor Add\r\n
0xd0000133 | Power Source Change\r\n
0xd0000134 | AC\r\n
0xd0000135 | DC\r\n
0xd0000136 | DC Short Term\r\n
0xd0000137 | Unknown\r\n
0xd0000138 | is stopping timers\r\n
0xd0000139 | has stopped timers\r\n
0xd000013a | is locking partitions\r\n
0xd000013b | has locked partitions\r\n
0xd000013c | is unlocking partitions\r\n
0xd000013d | has unlocked partitions\r\n
0xd000013e | is starting timers\r\n
0xd000013f | has started timers\r\n
0xd0000140 | is starting\r\n
0xd0000141 | is complete\r\n
0xd0000142 | IP\r\n
0xd0000143 | TCP\r\n
0xd0000144 | leaving S0\r\n
0xd0000145 | entering S0\r\n
0xd0000146 | Unreachable\r\n
0xd0000147 | Incomplete\r\n
0xd0000148 | Probe\r\n
0xd0000149 | Delay\r\n
0xd000014a | Stale\r\n
0xd000014b | Reachable\r\n
0xd000014c | Permanent\r\n
0xd000014d | Maximum\r\n
0xd000014e | Map\r\n
0xd000014f | Configure\r\n
0xd0000150 | TlSuspectsReachability\r\n
0xd0000151 | TlConfirmsReachability\r\n
0xd0000152 | NaConfirmsReachability\r\n
0xd0000153 | ProbeReachability\r\n
0xd0000154 | DadSolicitation\r\n
0xd0000155 | NewDlAddress\r\n
0xd0000156 | TriggerNud\r\n
0xd0000157 | Resolve\r\n
0xd0000158 | Timeout\r\n
0xd0000159 | Sending neighbor solicitation\r\n
0xd000015a | Received neighbor solicitation\r\n
0xd000015b | Sending neighbor advertisement\r\n
0xd000015c | Received neighbor advertisement\r\n
0xd000015d | Sending router solicitation\r\n
0xd000015e | Received router solicitation\r\n
0xd000015f | Sending router advertisement\r\n
0xd0000160 | Received router advertisement\r\n
0xd0000161 | Receive\r\n
0xd0000162 | ReceiveAndInvalidate\r\n
0xd0000163 | Send\r\n
0xd0000164 | FastRegister\r\n
0xd0000165 | Bind\r\n
0xd0000166 | Invalidate\r\n
0xd0000167 | Read\r\n
0xd0000168 | Write\r\n
0xd0000169 | Not Activated\r\n
0xd000016a | Activated\r\n
0xd000016b | TCP connect\r\n
0xd000016c | TCP send\r\n
0xd000016d | UDP send\r\n
0xd000016e | RAW send\r\n
0xd000016f | Received Router Advertisement\r\n
0xd0000170 | AdminConfigured\r\n
0xd0000171 | NetworkProperty\r\n
0xd0000172 | CreateWolContext\r\n
0xd0000173 | DeleteWolContext\r\n
0xd0000174 | SetWolContext\r\n
0xd0000175 | ClearWolContext\r\n
0xd0000176 | WolContextEvicted\r\n
0xd0000177 | AddWolAddress\r\n
0xd0000178 | RemoveWolAddress\r\n
0xd0000179 | Send\r\n
0xd000017a | Receive\r\n
0xd000017b | WFP-ALE: RemoteEndPoint Address\r\n
0xd000017c | WFP-ALE: RemoteEndPoint Port\r\n
0xd000017d | WFP-ALE: LocalEndPoint Address\r\n
0xd000017e | WFP-ALE: LocalEndPoint Port\r\n
0xd000017f | WFP-ALE: Partition Id\r\n
0xd0000180 | WFP-ALE: Parition NumEnties\r\n
0xd0000181 | SlowDownEntry\r\n
0xd0000182 | SlowDownExit\r\n
0xd0000183 | SlowDownTracking\r\n
0xd0000184 | BaseDelayUpdate\r\n
0xd0000185 | Ack\r\n
0xd0000186 | DupAck\r\n
0xd0000187 | Timeout\r\n
0xd0000188 | Ecn\r\n
0xd0000189 | SpuriousTimeout\r\n
0xd000018a | Network Context Constraint\r\n
0xd000018b | Prefix Length Policy\r\n
0xd000018c | Start Epoch Policy\r\n
0xd000018d | Default Routes Disabled On Interface\r\n
0xd000018e | Unconstrained Lookup Disallowed On Interface\r\n
0xd000018f | Interface Disconnected\r\n
0xd0000190 | Route Invalid Lifetime\r\n
0xd0000191 | Interface Constraint\r\n
0xd0000192 | Scope Constraint\r\n
0xd0000193 | Rechability\r\n
0xd0000194 | Prefix Length\r\n
0xd0000195 | Route And Interface Metrics\r\n
0xd0000196 | Destination And Source Hash\r\n
0xd0000197 | Route Order\r\n
0xd0000198 | Dead Gateway\r\n
0xd0000199 | OnLink Route\r\n
0xd000019a | Prefer Same Address\r\n
0xd000019b | Prefer Appropriate Scope\r\n
0xd000019c | Avoid Deprecated Addresses\r\n
0xd000019d | Prefer Home Addresses\r\n
0xd000019e | Prefer Outgoing Interface\r\n
0xd000019f | Prefer Addresses Associated With NextHop\r\n
0xd00001a0 | Prefer Matching Label\r\n
0xd00001a1 | Prefer Temporary Addresses\r\n
0xd00001a2 | System Defined Preference (Windows Specific)\r\n
0xd00001a3 | Prefer Longest Matching Prefix With NextHop (Windows Specific)\r\n
0xd00001a4 | Prefer Longest Matching Prefix\r\n
0xd00001a5 | TimerArmed\r\n
0xd00001a6 | TimerFired\r\n
0xd00001a7 | Failed\r\n
0xd00001a8 | Init\r\n
0xd00001a9 | SetTimeSlotData\r\n
0xd00001aa | SetTailTimeSlot\r\n
0xd00001ab | EraseTimestamps\r\n
0xd00001ac | GetRecoverySeq\r\n
0xd00001ad | RttSampleUpdate\r\n
0xd00001ae | TcpFastopenOff\r\n
0xd00001af | TcpFastopenAccepting\r\n
0xd00001b0 | TcpFastopenServerSendingCookie\r\n
0xd00001b1 | TcpFastopenServerSentCookie\r\n
0xd00001b2 | TcpFastopenNegotiate\r\n
0xd00001b3 | TcpFastopenAttempt\r\n
0xd00001b4 | TcpFastopenNegotiateSuccess\r\n
0xd00001b5 | TcpFastopenAttemptSuccess\r\n
0xd00001b6 | TcpFastopenCookieRollover\r\n
0xd00001b7 | TcpFastopenFailed\r\n
0xd00001b8 | TcpFastopenFailedBlocklist\r\n
0xd00001b9 | TcpFastopenServerAcceptSuccess\r\n
0xd00001ba | TcpFastopenServerAcceptTimeout\r\n
0xd00001bb | TcpFastopenServerAcceptSendData\r\n
0xd00001bc | TcpFastopenFailedSimultaneousConnect\r\n
0xd00001bd | TcpFastopenFailedInvalidCookie\r\n
0xd00001be | TcpFastopenFailedSynTimeout\r\n
0xd00001bf | TcpFastopenFailedTimeout\r\n
0xd00001c0 | TcpFastopenFailedReset\r\n
0xd00001c1 | TcpFastopenFallback\r\n
0xd00001c2 | TcpFastopenCookieRequestDeclined\r\n
0xd00001c3 | TcpFastopenFailedSuddenRttIncrease\r\n
0xd00001c4 | General failure\r\n
0xd00001c5 | Truncated header\r\n
0xd00001c6 | Invalid checksum\r\n
0xd00001c7 | Inspection drop\r\n
0xd00001c8 | Rejecting loopback neighbor discovery\r\n
0xd00001c9 | Unknown type/code\r\n
0xd00001ca | Truncated IP header\r\n
0xd00001cb | Oversized IP header\r\n
0xd00001cc | No handler\r\n
0xd00001cd | Not responding with error for error\r\n
0xd00001ce | Invalid source\r\n
0xd00001cf | Interface rate limit\r\n
0xd00001d0 | Path rate limit\r\n
0xd00001d1 | No route\r\n
0xd00001d2 | No matching request\r\n
0xd00001d3 | Buffer too small\r\n
0xd00001d4 | Failed to obtain ancillary data\r\n
0xd00001d5 | Incorrect hop limit\r\n
0xd00001d6 | Unknown code\r\n
0xd00001d7 | Source not linklocal\r\n
0xd00001d8 | Truncated ND header\r\n
0xd00001d9 | Invalid ND option SourceLinkAddr\r\n
0xd00001da | Invalid ND option MTU\r\n
0xd00001db | Invalid ND option PrefixInformation\r\n
0xd00001dc | Invalid ND option RouteInformation\r\n
0xd00001dd | Invalid ND option RDNSS\r\n
0xd00001de | Invalid ND option DNSSL\r\n
0xd00001df | Packet parsing failure\r\n
0xd00001e0 | Echo Reply\r\n
0xd00001e1 | Destination Unreachable\r\n
0xd00001e2 | Packet Too Big\r\n
0xd00001e3 | Destination Unreachable(v4)/Time Exceeded(v6)\r\n
0xd00001e4 | Source Quench(v4)/Parameter Problem(v6)\r\n
0xd00001e5 | Redirect\r\n
0xd00001e6 | Echo Request\r\n
0xd00001e7 | Router Advertisement\r\n
0xd00001e8 | Router Solicitation\r\n
0xd00001e9 | Time Exceeded\r\n
0xd00001ea | Parameter Problem\r\n
0xd00001eb | Timestamp Request\r\n
0xd00001ec | Timestamp Reply\r\n
0xd00001ed | Address Mask Request\r\n
0xd00001ee | Address Mask Reply\r\n
0xd00001ef | Echo Request\r\n
0xd00001f0 | Echo Reply\r\n
0xd00001f1 | Multicast Listener Query\r\n
0xd00001f2 | Multicast Listener Report\r\n
0xd00001f3 | Multicast Listener Done\r\n
0xd00001f4 | Router Solicitation\r\n
0xd00001f5 | Router Advertisement\r\n
0xd00001f6 | Neighbor Solicitation\r\n
0xd00001f7 | Neighbor Advertisement\r\n
0xd00001f8 | Redirect Message\r\n
0xd00001f9 | Multicast Listener Discovery\r\n
0xd00001fa | Not Parsed\r\n
0xd00001fb | Periodic\r\n
0xd00001fc | Aperiodic\r\n
0xd00001fd | Unknown\r\n
0xd00001fe | Public\r\n
0xd00001ff | Private\r\n
0xd0000200 | Domain\r\n
0xd0000201 | Remote\r\n
0xd0000202 | Link\r\n
0xd0000203 | NonDomainNetwork\r\n
0xd0000204 | DomainNetwork\r\n
0xd0000205 | DomainAuthenticated\r\n
0xd0000206 | InterfaceAddition\r\n
0xd0000207 | InterfaceDeletion\r\n
0xd0000208 | ZoneChange\r\n
0xd0000209 | ConfigurationFlagChange\r\n
0xd000020a | ForwardingEnable\r\n
0xd000020b | ForwardingDisable\r\n
0xd000020c | WeakHostReceiveEnable\r\n
0xd000020d | WeakHostReceiveDisable\r\n
0xd000020e | NetworkCategoryStateChange\r\n
0xd000020f | MetricChange\r\n
0xd0000210 | MediaConnect\r\n
0xd0000211 | MediaDisconnect\r\n
0xd0000212 | OffloadCapabilityChange\r\n
0xd0000213 | DisableDefaultRoutesSet\r\n
0xd0000214 | DisableDefaultRoutesReset\r\n
0xd0000215 | ForceTunnelingSet\r\n
0xd0000216 | ForceTunnelingReset\r\n
0xd0000217 | LimitedLinkConnectivitySet\r\n
0xd0000218 | LimitedLinkConnectivityReset\r\n
0xd0000219 | LocalityConfigChange\r\n
0xd000021a | DisableUnconstrainedRouteLookupSet\r\n
0xd000021b | DisableUnconstrainedRouteLookupReset\r\n
0xd000021c | PortStateChange\r\n
0xd000021d | NoInternetConnectivity\r\n
0xd000021e | NoInternetDnsResolutionSucceeded\r\n
0xd000021f | InternetConnectivityDetected\r\n
0xd0000220 | InternetConnectivityUnknown\r\n
0xd0000221 | Timeout\r\n
0xd0000222 | DadStarted\r\n
0xd0000223 | OptimisticDadStarted\r\n
0xd0000224 | DadPassed\r\n
0xd0000225 | NSReceived\r\n
0xd0000226 | NAReceived\r\n
0xd0000227 | InterfaceDisabled\r\n
0xd0000228 | DadDisabled\r\n
0xd0000229 | AddressAddition\r\n
0xd000022a | AddressDeletion\r\n
0xd000022b | DadStatePreferred\r\n
0xd000022c | DadStateDuplicate\r\n
0xd000022d | DadStateDeprecated\r\n
0xd000022e | SkipAsSourceSet\r\n
0xd000022f | SkipAsSourceReset\r\n
0xd0000230 | TunnelSkipAsSourceSet\r\n
0xd0000231 | TunnelSkipAsSourceReset\r\n
0xd0000232 | ZoneChange\r\n
0xd0000233 | NeighborAddition\r\n
0xd0000234 | NeighborDeletion\r\n
0xd0000235 | NeighborUnreachable\r\n
0xd0000236 | NeighborReachable\r\n
0xd0000237 | NeighborAddressUpdate\r\n
0xd0000238 | DeadRouteTimeout\r\n
0xd0000239 | DeadRouteProbeTimeout\r\n
0xd000023a | AllRoutesDead\r\n
0xd000023b | TlConfirmsForwardReachability\r\n
0xd000023c | DeadGatewayDetected\r\n
0xd000023d | RouterRedirect\r\n
0xd000023e | ProbeConnectionFailed\r\n
0xd000023f | ConfigurationChange\r\n
0xd0000240 | Alive\r\n
0xd0000241 | Dead\r\n
0xd0000242 | Probe\r\n
0xd0000243 | Disable\r\n
0xd0000244 | Enable\r\n
0xd0000245 | NotConfident\r\n
0xd0000246 | InvalidLoad\r\n
0xd0000247 | ConfidenceUpdate\r\n
0xd0000248 | TCP Fastopen\r\n
0xd0000249 | Init\r\n
0xd000024a | StatusIndication\r\n
0xd000024b | GlobalSetting\r\n
0xd000024c | Forwarding\r\n
0xd000024d | IncompatibleCallout\r\n
0xd000024e | RA DNS information change\r\n
0xd000024f | RA DNS entry added\r\n
0xd0000250 | RA DNS entry expired by RA\r\n
0xd0000251 | RA DNS entry expired by timer\r\n
0xd0000252 | RA DNS entry lifetime reset\r\n
0xd0000253 | RA DNS entry reordered\r\n
0xd0000254 | RA DNS entry deleted due to max limit\r\n
0xd0000255 | RA DNS entry lifetime updated\r\n
0xd0000256 | RA DNS ND entry ignored due to limit\r\n
0xd0000257 | RA DNS ND entry ignored due to memory failure\r\n
0xd0000258 | RA DNS ND entry ignored due to zero lifetime\r\n
0xd0000259 | RA DNS ND entries corrupted\r\n
0xd000025a | RA DNS RouterContext init failed\r\n
0xd000025b | Manual\r\n
0xd000025c | WellKnown\r\n
0xd000025d | DHCP\r\n
0xd000025e | RouterAdvertisement\r\n
0xd000025f | 6to4\r\n
0xd0000260 | Avoid Unusable Destination\r\n
0xd0000261 | Prefer Aoac Interface\r\n
0xd0000262 | Prefer Matching Scope\r\n
0xd0000263 | Avoid Deprecated Address\r\n
0xd0000264 | Prefer Matching Label\r\n
0xd0000265 | Prefer Internet Connected Interface\r\n
0xd0000266 | Prefer Higher Precedence\r\n
0xd0000267 | Prefer Longer Route Destination Prefix\r\n
0xd0000268 |  Prefer Native Transport(Physical Interface)\r\n
0xd0000269 | Prefer Lower Interface Metric\r\n
0xd000026a | Prefer Smaller Scope\r\n
0xd000026b | Prefer Same Address\r\n
0xd000026c | Prefer Appropriate Scope\r\n
0xd000026d | Avoid Deprecated Address\r\n
0xd000026e | Prefer Outgoing Interface\r\n
0xd000026f | Prefer Source Address Associated With Nexthop\r\n
0xd0000270 | Prefer Temporary Address\r\n
0xd0000271 | System Defined Preference\r\n
0xd0000272 | Prefer Source With Longer NextHop Prefix Match\r\n
0xd0000273 | Locality Metric\r\n
0xd0000274 | Prefer Longer Source/Destination Common Prefix Length\r\n
0xd0000275 | Order Unchanged (No Preference)\r\n
0xd0000276 | Send\r\n
0xd0000277 | Disconnect\r\n
0xd0000278 | Accept\r\n
0xd0000279 | Receive\r\n
0xd000027a | ReceiveTcpDatagram\r\n
0xd000027b | ReceiveDatagram\r\n
0xd000027c | RemoteDisconnect\r\n
0xd000027d | ReceiveControlMessage\r\n
0xd000027e | RespondDatagram\r\n
0xd000027f | BindEndpoint\r\n
0xd0000280 | Listen\r\n
0xd0000281 | AcceptComplete\r\n
0xd0000282 | Connect\r\n
0xd0000283 | ConnectComplete\r\n
0xd0000284 | Raw\r\n
0xd0000285 | ConnectRequest\r\n
0xd0000286 | CreateEndpoint\r\n
0xd0000287 | AcquirePort\r\n
0xd0000288 | Offload\r\n
0xd0000289 | SocketOption\r\n
0xd000028a | BindEndpointRequest\r\n
0xd000028b | Drop\r\n
0xd000028c | Allow\r\n
0xd000028d | Pend\r\n
0xd000028e | DropAndSendIcmp\r\n
0xd000028f | Allow\r\n
0xd0000290 | Deny\r\n
0xd0000291 | Authorize\r\n
0xd0000292 | RetryWithHint\r\n

### 10.0.17134.706

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto = %3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm = %6, MaxDataRetransmissions = %7, DelayedAckTicks = %8 msec, DelayedAckFrequency = %9, RACK enabled = %10, Tail Loss Probe enabled = %11.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5, Event = %6.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick = %4 Time = %5.\r\n
0xb0000527 | %1 timer rescheduled by processor %2 for processor %3 at Tick = %4 to Tick = %5, OldScheduledExpiration = %6 NewScheduledExpiration = %7 DueTime = %8 Aperiodic = %9.\r\n
0xb0000528 | %1 timer fired on processor %2 at Tick = %3, was scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for Destination %4 in Compartment %5, Reason: %8 (Rule %6.%7).\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0000558 | Teredo Add -- PID: %1 started listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb0000559 | Teredo Remove -- PID: %1 stopped listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb000055a | IP: RouteLookup - API: %1 DstAddr: %3 ConstrainSrcAddr: %4 ConstrainIfIndex: %5 ConstraintOveridden: %6 ReturnConstrained: %7 OutgoingIfIndex: %8 NextHopAddr: %9 Status: %10\r\n
0xb000055b | IP: SourceAddrLookup - DstAddr: %2 ConstrainSrcAddr: %3 ConstrainIfIndex: %4 OutgoingIfIndex: %5 ReturnConstrained: %6 SelectedSrcAddr: %7\r\n
0xb000055c | WFP-ALE: Partition Count=%1 Partition Mask=%2: Partition Id=%d Partition NumEntries = %4.\r\n
0xb000055d | WFP-ALE: HotAdd/Remove: Old Partiton Count=%1 Old Partition Mask=%2 New Partiton Count=%1 New Partition Mask=%2.\r\n
0xb000055e | WFP-ALE: RemoteEndPoint Insertion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb000055f | WFP-ALE: RemoteEndPoint Deletion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb0000560 | WFP-ALE: ALE: low memory state detected. LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000561 | WFP-ALE: leaving low memory state. HighMemoryEvent = %1 HighNonPagedPoolEvent = %2.\r\n
0xb0000562 | WFP-ALE: Dpc for cleanup initiated: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000563 | WFP: Dpc for cleanup QUEUED or RE-QUEUED: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000564 | TCP: LEDBAT %2: Connection %1, BaseDelayMs = %6, CurrentDelayMs = %7, CWnd = %3, SsThresh = %4, SndWnd = %5, DelayBasedCwndFactor %9%%, RemainingTimeMs = %8.\r\n
0xb0000565 | TCP: AssociateNameResContext Endpoint: %1 Status: %16 NameResolutionContext: %2 DnsName: %3 InterfaceIndex: %4 IPAddrCount: %5 IPAddrs: %7 %9 %11 %13 %15\r\n
0xb0000566 | TCP: InspectConnectWithNameResContext Connection: %5 (local: %2 remote: %4) NameResolutionContext: %6 DnsName: %7 Status: %8.\r\n
0xb0000567 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 InterfaceMetric: %10 RouteMetric: %11] is preferred over Route [DestinationPrefix: %14/%12 NextHop: %16 InterfaceIndex: %17 InterfaceMetric: %18 RouteMetric: %19] for Destination: %3 in Compartment: %1, Reason: %20.\r\n
0xb0000568 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 RouteMetric: %10] is blocked for Destination: %3 ConstrainInterfaceIndex: %11 ConstrainScopeZone: %12 in Compartment: %1, Reason: %13.\r\n
0xb0000569 | TCP: Tail Loss Probe Send Connection = %1 SndUna = %2, SndMax = %3, SendAvailable = %4, TailProbeSeq = %5, TailProbeLast = %6, ControlsToSend = %7, ThFlags = %8.\r\n
0xb000056a | TCP: Tail Loss Probe Event Connection = %1, Event = %2.\r\n
0xb000056b | TCP: RACK Event Connection = %1, Event = %2, MinRTT = %3, ReoWind = %4, TimeSlotDeltaMin = %5, SeqNum = %6, Timestamp = %7, RttSample = %8.\r\n
0xb000056c | TCP: Fastopen state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000056d | UDP: endpoint (family=%5 pid=%3) create failed: address family not attached.\r\n
0xb000056e | UDP: endpoint %1 (family=%5 pid=%3) create failed: compartment %4 not found.\r\n
0xb000056f | UDP: endpoint %1 (family=%5 pid=%3) created.\r\n
0xb0000570 | UDP: endpoint %1 (family=%5 pid=%3) create failed: inspection status = %2\r\n
0xb0000571 | UDP: endpoint %4 bind failed: address %2 cannot be resolved, status = %3\r\n
0xb0000572 | UDP: endpoint %4 (sockaddr=%2) bind failed: port-acquisition status = %3\r\n
0xb0000573 | UDP: endpoint %4 (sockaddr=%2) bind failed: inspection status = %3\r\n
0xb0000574 | UDP: endpoint %4 (sockaddr=%2) bound.\r\n
0xb0000575 | UDP: endpoint %4 (sockaddr=%2) closed.\r\n
0xb0000576 | UDP: endpoint %4 closed.\r\n
0xb0000577 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address resolution status = %6\r\n
0xb0000578 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address validation failed.\r\n
0xb0000579 | UDP: endpoint %1 (sockaddr=%3) send messages %5: source-address selection status = %6\r\n
0xb000057a | UDP: endpoint %1 too many packets queued for the pending join path.\r\n
0xb000057b | UDP: address family %2added to interface %1.\r\n
0xb000057c | UDP: address family %2removed from interface %1.\r\n
0xb000057d | UDP: Failure initializing transport protocol, status = %1\r\n
0xb000057e | UDP: Failure starting NLNPI client, status = %1\r\n
0xb000057f | UDP: Failure initializing NSI support, status = %1\r\n
0xb0000580 | UDP: Failure starting TLNPI provider, status = %1\r\n
0xb0000581 | UDP: Failure initializing QoS support, status = %1\r\n
0xb0000582 | UDP: Failure starting %1, status = %2\r\n
0xb0000583 | UDP: endpoint %1 (sockaddr=%3) send messages %5: could not allocate send context.\r\n
0xb0000584 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path af failure, status = %6\r\n
0xb0000585 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path missing next hop failure.\r\n
0xb0000586 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path next hop address failure.\r\n
0xb0000587 | TCP: Early Retransmission, FACK or RACK, Connection = %1, SndUna = %2, SackIsLostSeq = %3, DupAckCount = %4\r\n
0xb0000588 | TCP: Ignoring fastopen SYN option due to limit on concurrent SYN_RCVD fastopen connections, Connection = %1, SynRcvdLimit = %2\r\n
0xb0000589 | TCP: Failed to update fastopen key state, Location = %1, Status = %2. Server-side fastopen will be disabled\r\n
0xb000058a | TCP: Fast Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058b | TCP: SACK Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058c | TCP: Limited Transmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058d | TCP: SACK Retransmit Additional Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058e | %1: %2message. Type = %3, Code = %4, CompartmentId = %5, SourceAddress = %7, DestAddress = %9\r\n
0xb000058f | %1: %2path drop. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11\r\n
0xb0000590 | %1: Echo timeout. Status = %4\r\n
0xb0000591 | %1 Timer state changed to %3 by Processor %2 Usage = %4 at Tick = %5\r\n
0xb0000592 | TCP: connection %1 send complete %3 bytes at %4 (%2).\r\n
0xb0000593 | IP: Compartment creation. Compartment = %1, Protocol = %2, Private = %3, Status = %4.\r\n
0xb0000594 | IP: Compartment deletion. Compartment = %1, Protocol = %2.\r\n
0xb0000595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13.\r\n
0xb0000596 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5 CwrMax = %6.\r\n
0xb0000597 | IP: Compartment cleanup. Compartment = %1, Protocol = %2.\r\n
0xb0000598 | IP: Interface network category state change. Interface = %1, Compartment = %2 , Protocol = %3, NetworkCategory = %4, DomainNetworkLocation = %5, DomainType = %6, Signature = %7.\r\n
0xb0000599 | IP: Interface creation. Interface = %1, Compartment = %2, Protocol = %3, PhysicalMediumType = %4, Status = %5.\r\n
0xb000059a | IP: Interface deletion. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059b | IP: Interface cleanup. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059c | IP: SubInterface creation. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4, Status = %5.\r\n
0xb000059d | IP: SubInterface deletion. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059e | IP: SubInterface cleanup. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059f | IP: Interface change Notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005a0 | IP: Interface internet connectivity status change. Interface = %1, Compartment = %2, Protocol = %3, OldConnectivityStatus = %4, NewConnectivityStatus = %5.\r\n
0xb00005a1 | IP: Address change notification. Address = %2, Interface = %3, Compartment = %4, Protocol = %5, Reason = %6.\r\n
0xb00005a2 | IP: Route change notification. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, NotifyFlags = %8.\r\n
0xb00005a3 | IP: Neighbor change notification. IpAddress = %2, DlAddress = %4, Interface = %5, Compartment = %6, State = %7, Reason = %8.\r\n
0xb00005a4 | IP: Address DAD state change. Address = %2, Interface = %3, Compartment = %4, OldState = %5, NewState = %6, Reason = %7.\r\n
0xb00005a5 | IP: Route Dead Gateway Detection state change. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, OldState = %8, NewState = %9, OldProbeCount = %10, NewProbeCount = %11, OldUnreachablePaths = %12, NewUnreachablePaths = %13, OldMovedPaths = %14, NewMovedPaths = %15, TotalPaths = %16, OldStateChangeTick = %17, NewStateChangeTick = %18, DgdNeedsReset = %19, Reason = %20.\r\n
0xb00005a6 | IP: Disconnecting TCP connections with Address = %2, Interface = %3, Compartment = %4, SkipLocal = %5, SkipOnLink = %6.\r\n
0xb00005a7 | TCP: connection %1: Sending paced chunk of %6 bytes with CWnd = %2, SndWnd = %3, BytesAvailable = %4, BytesOutstanding = %5\r\n
0xb00005a8 | Fallback: Context = %1, Feature = %2, TraceReason = %3, Confidence = %4, Successes = %5, Failures = %6\r\n
0xb00005a9 | TCPIP: TCB %1 using fast loopback\r\n
0xb00005aa | IP: Router information change notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005ab | IP: %1. Interface = %2, Compartment = %3, RouterAddress = %5, DNS Server/Suffix: %7 %8, Lifetime = %9.\r\n
0xb00005ac | IP: Route rundown. Interface = %1, Compartment = %2, Prefix = %4/%5, NextHop = %7, Metric = %8, State = %9, Origin = %10, Age = %11, ValidLifetime = %12, PreferredLifetime = %13, Flags = %14.\r\n
0xb00005ad | TCP: CUBIC ECN event. Connection %1, CWnd %2, SSThresh = %3, SndUna = %4\r\n
0xb00005ae | INETINSPECT: Owner = %1, InspectHandle = %2, InspectType = %3, Action = %4, Status = %5\r\n
0xb00005b0 | FallbackCheck: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b1 | FallbackUpdate: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b2 | Fallback: Permanently disabling feature, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b3 | Fallback: Enabling feature for this boot session, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b4 | Fallback: Feature previously disabled, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b5 | TCP Fastopen fallback update: Tcb = %1, FastopenState = %2, DataBytesIn = %3, ShutdownStatus = %4, ProbeStatus = %5\r\n
0xb00005b6 | Disabling feature until connectivity is established: CompartmentId =%1, IfIndex = %2, Feature = %3, ConnectivityStatus = %4\r\n
0xb00005b7 | Disabling %1 for loopback connection\r\n
0xb00005b8 | Disabling TCP Fastopen for BaseEndpoint = %1 because an incompatible WFP callout is installed\r\n
0xb00005b9 | IP: Setting source constraint for route lookup - Compartment: %1 DstAddr: %3 ConstrainSrcAddr: %5 ConstrainIfIndex: %6 ConstraintFlags: %7\r\n
0xb00005ba | WFP-ALE: RemoteEndPoint Insertion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bb | WFP-ALE: RemoteEndPoint Deletion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bc | TCP: connection %8 (local=%2 remote=%4) system abort. PID = %6.\r\n
0xb00005bd | Disabling %1 due to no next hop\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010452 | IP: Interface media disconnect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001045a | IP: Address DAD successful. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001045b | IP: Address DAD failed. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2, DL address of packet = %5.\r\n
0xb001045c | IP: Address DAD started. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010467 | IP: Address addition. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010468 | IP: Address deletion. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001046a | Framing: Interface operation status change. Interface = %1, Compartment = %4, Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0010470 | Framing: NDIS pause event. Interface = %1, Compartment = %3.\r\n
0xb0010471 | Framing: NDIS restart event. Interface = %1, Compartment = %3.\r\n
0xb0010478 | IP: Interface property change. Interface = %1, Compartment = %10, Protocol = %11, Advertise = %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7, WeakHostSend = %8, WeakHostReceive = %9.\r\n
0xb00104b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, Address = %4 %3 %6.\r\n
0xb00104b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7.\r\n
0xb0010529 | IP: Interface media connect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052a | IP: Interface limited link connectivity set. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052b | IP: Interface limited link connectivity reset. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052c | IP: Neighbor state change. IPAddress = %3, DLAddress = %5, Interface = %1, Compartment = %9, OldState = %6, NewState = %7, Event = %8.\r\n
0xb001052d | IP: Neighbor Discovery. Event = %5, Interface = %1, Compartment = %6, SourceIpAddress = %3, TargetIpAddress = %4.\r\n
0xb001052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions: %6, Reason: %10 (Rule %7 %8.%9).\r\n
0xb0010534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb001054e | IP: Interface configuration flags updated. Interface = %1, Compartment = %5, Protocol = %6, Property = %2, Value = %3, Event = %4.\r\n
0xb0010557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9, NrtNameResolutionId %10\r\n
0xb0010565 | TCP: AssociateNameResContext EndpointObj: %1 IsConnectionObj: %2 NameResContext: %3 Status: %4\r\n
0xb00204b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, Address = %4 %3 %6.\r\n
0xb00304b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Metric = %11, Connected = %12, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, InternetConnectivityStatus = %13, Flags = %14, Address = %4 %3 %6.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | PacingTimer\r\n
0xd000002c | DisconnectTimer\r\n
0xd000002d | SwsTimer\r\n
0xd000002e | ReassemblyRateTimer\r\n
0xd000002f | SynOrRstValidationTimer\r\n
0xd0000030 | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000031 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000032 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000033 | TCP_KEEPALIVE\r\n
0xd0000034 | TCP_MAXSEG\r\n
0xd0000035 | TCP_MAXRT\r\n
0xd0000036 | TCP_STDURG\r\n
0xd0000037 | TCP_NOURG\r\n
0xd0000038 | TCP_ATMARK\r\n
0xd0000039 | TCP_NOSYNRETRIES\r\n
0xd000003a | TCP_TIMESTAMPS\r\n
0xd000003b | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003c | TCP_CONGESTION_ALGORITHM\r\n
0xd000003d | TCP_DELAY_FIN_ACK\r\n
0xd000003e | SO_DEBUG\r\n
0xd000003f | SO_ACCEPTCONN\r\n
0xd0000040 | SO_REUSEADDR\r\n
0xd0000041 | SO_KEEPALIVE\r\n
0xd0000042 | SO_DONTROUTE\r\n
0xd0000043 | SO_BROADCAST\r\n
0xd0000044 | SO_USELOOPBACK\r\n
0xd0000045 | SO_LINGER\r\n
0xd0000046 | SO_OOBINLINE\r\n
0xd0000047 | SO_SNDBUF\r\n
0xd0000048 | SO_RCVBUF\r\n
0xd0000049 | SO_CONDITIONAL_ACCEPT\r\n
0xd000004a | SO_PAUSE_ACCEPT\r\n
0xd000004b | SO_COMPARTMENT_ID\r\n
0xd000004c | SO_RANDOMIZE_PORT\r\n
0xd000004d | SO_PORT_SCALABILITY\r\n
0xd000004e | NldsInvalid\r\n
0xd000004f | NldsTentative\r\n
0xd0000050 | NldsDuplicate\r\n
0xd0000051 | NldsDeprecated\r\n
0xd0000052 | NldsPreferred\r\n
0xd0000053 | Indicate\r\n
0xd0000054 | Pend\r\n
0xd0000055 | Satisfy\r\n
0xd0000056 | NdisPhysicalMediumUnspecified\r\n
0xd0000057 | NdisPhysicalMediumWirelessLan\r\n
0xd0000058 | NdisPhysicalMediumCableModem\r\n
0xd0000059 | NdisPhysicalMediumPhoneLine\r\n
0xd000005a | NdisPhysicalMediumDSL\r\n
0xd000005b | NdisPhysicalMedium1394\r\n
0xd000005c | NdisPhysicalMediumWirelessWan\r\n
0xd000005d | NdisPhysicalMediumNative802_11\r\n
0xd000005e | NdisPhysicalMediumBluetooth\r\n
0xd000005f | NdisPhysicalMediumInfiniband\r\n
0xd0000060 | NdisPhysicalMediumWiMax\r\n
0xd0000061 | NdisPhysicalMedium802_3\r\n
0xd0000062 | NdisPhysicalMedium802_5\r\n
0xd0000063 | NdisPhysicalMediumIrda\r\n
0xd0000064 | NdisPhysicalMediumWiredWAN\r\n
0xd0000065 | IP checksum offload not computed\r\n
0xd0000066 | TCP checksum offload not computed\r\n
0xd0000067 | UDP checksum offload not computed\r\n
0xd0000068 | Header not aligned on 4-byte boundary\r\n
0xd0000069 | IP fragmentation\r\n
0xd000006a | Source address is not unicast\r\n
0xd000006b | Destination address is not unicast\r\n
0xd000006c | Ethernet and IP header not contiguous\r\n
0xd000006d | IP options present\r\n
0xd000006e | ESP over UDP\r\n
0xd000006f | Lack contiguous space for upper layer headers\r\n
0xd0000070 | WFP filters present\r\n
0xd0000071 | Nexthop is unavailable\r\n
0xd0000072 | Path has been invalidated due to policy change\r\n
0xd0000073 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000074 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000075 | Session state is not compatible\r\n
0xd0000076 | TCP options present\r\n
0xd0000077 | UDP IPv6 checksum absent in packet\r\n
0xd0000078 | Packet is for a loopback interface\r\n
0xd0000079 | Packet is from a Raw Socket\r\n
0xd000007a | TL Ancillary headers present\r\n
0xd000007b | NL Ancillary headers present\r\n
0xd000007c | Type of Service present\r\n
0xd000007d | IpSec headers present\r\n
0xd000007e | Interface is not Ethernet\r\n
0xd000007f | Nbl check failed\r\n
0xd0000080 | Destination address is unknown\r\n
0xd0000081 | Failed to allocate the WSD cache\r\n
0xd0000082 | Failure initializing PnP work queue\r\n
0xd0000083 | Failed to get persistent parameters\r\n
0xd0000084 | Rejected persistent parameters\r\n
0xd0000085 | qualified profile\r\n
0xd0000086 | qualified destination\r\n
0xd0000087 | sample collection completion\r\n
0xd0000088 | idle time expiration\r\n
0xd0000089 | allocation\r\n
0xd000008a | new sample request\r\n
0xd000008b | configuration change\r\n
0xd000008c | Idle\r\n
0xd000008d | ProbingWs\r\n
0xd000008e | ProbeWait\r\n
0xd000008f | ProbingWithoutWs\r\n
0xd0000090 | RecordWait\r\n
0xd0000091 | EreQualified\r\n
0xd0000092 | Qualified\r\n
0xd0000093 | Source Unspecified\r\n
0xd0000094 | Destination is multicast\r\n
0xd0000095 | Header is invalid (location 0)\r\n
0xd0000096 | Checksum is invalid\r\n
0xd0000097 | Transport endpoint was not found\r\n
0xd0000098 | Connected path error\r\n
0xd0000099 | Session state error\r\n
0xd000009a | Receive Inspection\r\n
0xd000009b | ACK Invalid (subreason 0) (invalid ACK in SYN_SENT state)\r\n
0xd000009c | Expected SYN\r\n
0xd000009d | Received RST (subreason 0)\r\n
0xd000009e | Received SYN while in SYN_RCVD state\r\n
0xd000009f | Simultaneous Connect\r\n
0xd00000a0 | PAWS Failed\r\n
0xd00000a1 | Land Attack (subreason 0)\r\n
0xd00000a2 | Missed RST\r\n
0xd00000a3 | Outside Receive Window (subreason 0)\r\n
0xd00000a4 | Duplicate Segment\r\n
0xd00000a5 | Closed Window\r\n
0xd00000a6 | TCB Removed\r\n
0xd00000a7 | FIN-WAIT2\r\n
0xd00000a8 | Reassembly Conflict\r\n
0xd00000a9 | FIN Received\r\n
0xd00000aa | Listener received segment with invalid flags\r\n
0xd00000ab | URG flag set but could not allocate urgent data state\r\n
0xd00000ac | TCB was not inserted in TCB table\r\n
0xd00000ad | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000ae | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000af | Packet dropped by TIME-WAIT TCB (subreason 0)\r\n
0xd00000b0 | SYN+ACK with Fastopen cookie request\r\n
0xd00000b1 | Listener dropped SYN because SO_PAUSE_ACCEPT was set\r\n
0xd00000b2 | Listener dropped SYN to reduce memory pressure\r\n
0xd00000b3 | Bad source address\r\n
0xd00000b4 | Not locally destined\r\n
0xd00000b5 | Protocol unreachable\r\n
0xd00000b6 | Port unreachable\r\n
0xd00000b7 | Bad length\r\n
0xd00000b8 | Malformed Header\r\n
0xd00000b9 | No route available\r\n
0xd00000ba | Beyond scope\r\n
0xd00000bb | Inspection drop\r\n
0xd00000bc | Too many decapsulations\r\n
0xd00000bd | Administratively prohibited\r\n
0xd00000be | Hop limit exceeded\r\n
0xd00000bf | Address unreachable\r\n
0xd00000c0 | Fragment MTU exceeded\r\n
0xd00000c1 | Buffer Length Exceeded\r\n
0xd00000c2 | Address Resolution Timeout\r\n
0xd00000c3 | Address Resolution Failure\r\n
0xd00000c4 | IPsec failure\r\n
0xd00000c5 | Extension Headers Failure\r\n
0xd00000c6 | Allocation Failure\r\n
0xd00000c7 | IPSNPI Drop\r\n
0xd00000c8 | Unsupported Offload\r\n
0xd00000c9 | Routing Failure\r\n
0xd00000ca | Ancillary Data Failure\r\n
0xd00000cb | Raw Data Failure\r\n
0xd00000cc | Session State Failure\r\n
0xd00000cd | Default\r\n
0xd00000ce | NewReno\r\n
0xd00000cf | CTCP\r\n
0xd00000d0 | DCTCP\r\n
0xd00000d1 | LEDBAT\r\n
0xd00000d2 | TcpTemplateTypeInternet\r\n
0xd00000d3 | TcpTemplateTypeDatacenter\r\n
0xd00000d4 | TcpTemplateTypeCompat\r\n
0xd00000d5 | TcpTemplateTypeDatacenterCustom\r\n
0xd00000d6 | TcpTemplateTypeInternetCustom\r\n
0xd00000d7 | TcpTemplateTypeDefault\r\n
0xd00000d8 | TcpTemplateTypeAutomatic\r\n
0xd00000d9 | No Failure\r\n
0xd00000da | Unknown\r\n
0xd00000db | System Policy\r\n
0xd00000dc | NIC Capacity Reached\r\n
0xd00000dd | System Low On Memory\r\n
0xd00000de | WFP driver / Stream inspection\r\n
0xd00000df | Weak Host Model Enabled\r\n
0xd00000e0 | Forwarding Enabled\r\n
0xd00000e1 | Hardware capability\r\n
0xd00000e2 | NDIS filter/NIC property\r\n
0xd00000e3 | Loopback fast path socket option not set on both ends\r\n
0xd00000e4 | Filter policy existed for the loopback connection\r\n
0xd00000e5 | IPv4\r\n
0xd00000e6 | IPv6\r\n
0xd00000e7 | unbind\r\n
0xd00000e8 | bind\r\n
0xd00000e9 | port change\r\n
0xd00000ea | none\r\n
0xd00000eb | receive hash\r\n
0xd00000ec | receive scale\r\n
0xd00000ed | enabled\r\n
0xd00000ee | disabled\r\n
0xd00000ef | removing\r\n
0xd00000f0 | adding\r\n
0xd00000f1 | complete binding initialization\r\n
0xd00000f2 | complete port initialization\r\n
0xd00000f3 | enumerate interface ports\r\n
0xd00000f4 | query port link state\r\n
0xd00000f5 | query port interface index\r\n
0xd00000f6 | query interface ports\r\n
0xd00000f7 | query port RSS capabilities\r\n
0xd00000f8 | get usable processors\r\n
0xd00000f9 | query port driver version\r\n
0xd00000fa | query port RSS processor configuration\r\n
0xd00000fb | set receive scale parameters\r\n
0xd00000fc | set receive hash parameters\r\n
0xd00000fd | update interface ports\r\n
0xd00000fe | not available\r\n
0xd00000ff | available\r\n
0xd0000100 | available on ports\r\n
0xd0000101 | global configuration\r\n
0xd0000102 | active mode\r\n
0xd0000103 | Bind Adapter\r\n
0xd0000104 | Unbind Adapter (begin)\r\n
0xd0000105 | Unbind Adapter (end)\r\n
0xd0000106 | NetEvent Restart\r\n
0xd0000107 | NetEvent Power-down\r\n
0xd0000108 | NetEvent Power-up\r\n
0xd0000109 | NetEvent NDK-enable\r\n
0xd000010a | NetEvent NDK-disable\r\n
0xd000010b | NetEvent NDK usage stopped\r\n
0xd000010c | Indicate new NDK interface arrival\r\n
0xd000010d | Indicate NDK interface removal\r\n
0xd000010e | Indicate NDK operational status change\r\n
0xd000010f | Undefined\r\n
0xd0000110 | Adapter\r\n
0xd0000111 | QP\r\n
0xd0000112 | CQ\r\n
0xd0000113 | MR\r\n
0xd0000114 | MW\r\n
0xd0000115 | PD\r\n
0xd0000116 | SharedEndpoint\r\n
0xd0000117 | Connector\r\n
0xd0000118 | Listener\r\n
0xd0000119 | SRQ\r\n
0xd000011a | Max\r\n
0xd000011b | Async\r\n
0xd000011c | Inline\r\n
0xd000011d | Local\r\n
0xd000011e | Remote\r\n
0xd000011f | Privileged\r\n
0xd0000120 | Local\r\n
0xd0000121 | Remote\r\n
0xd0000122 | NotifyErrors\r\n
0xd0000123 | NotifyAny\r\n
0xd0000124 | NotifySolicited\r\n
0xd0000125 | Invalid\r\n
0xd0000126 | Software Slot allocated\r\n
0xd0000127 | Hardware Slot allocated\r\n
0xd0000128 | Policy error\r\n
0xd0000129 | system error\r\n
0xd000012a | Enabled\r\n
0xd000012b | Send request dropped\r\n
0xd000012c | Receive dropped\r\n
0xd000012d | Disconnect request dropped\r\n
0xd000012e | Reset dropped\r\n
0xd000012f | WFP API No Failure\r\n
0xd0000130 | WFP API WasRedirectedToProxy\r\n
0xd0000131 | WFP API RegisterForExitingEndpoint\r\n
0xd0000132 | WFP API ClassifiableFieldGetAf\r\n
0xd0000133 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000134 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd0000135 | WFP API ClassifiableFieldGetRemotePort\r\n
0xd0000136 | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd0000137 | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd0000138 | Processor Add\r\n
0xd0000139 | Power Source Change\r\n
0xd000013a | AC\r\n
0xd000013b | DC\r\n
0xd000013c | DC Short Term\r\n
0xd000013d | Unknown\r\n
0xd000013e | is stopping timers\r\n
0xd000013f | has stopped timers\r\n
0xd0000140 | is locking partitions\r\n
0xd0000141 | has locked partitions\r\n
0xd0000142 | is unlocking partitions\r\n
0xd0000143 | has unlocked partitions\r\n
0xd0000144 | is starting timers\r\n
0xd0000145 | has started timers\r\n
0xd0000146 | is starting\r\n
0xd0000147 | is complete\r\n
0xd0000148 | IP\r\n
0xd0000149 | TCP\r\n
0xd000014a | leaving S0\r\n
0xd000014b | entering S0\r\n
0xd000014c | Unreachable\r\n
0xd000014d | Incomplete\r\n
0xd000014e | Probe\r\n
0xd000014f | Delay\r\n
0xd0000150 | Stale\r\n
0xd0000151 | Reachable\r\n
0xd0000152 | Permanent\r\n
0xd0000153 | Maximum\r\n
0xd0000154 | Map\r\n
0xd0000155 | Configure\r\n
0xd0000156 | TlSuspectsReachability\r\n
0xd0000157 | TlConfirmsReachability\r\n
0xd0000158 | NaConfirmsReachability\r\n
0xd0000159 | ProbeReachability\r\n
0xd000015a | DadSolicitation\r\n
0xd000015b | NewDlAddress\r\n
0xd000015c | TriggerNud\r\n
0xd000015d | Resolve\r\n
0xd000015e | Timeout\r\n
0xd000015f | Sending neighbor solicitation\r\n
0xd0000160 | Received neighbor solicitation\r\n
0xd0000161 | Sending neighbor advertisement\r\n
0xd0000162 | Received neighbor advertisement\r\n
0xd0000163 | Sending router solicitation\r\n
0xd0000164 | Received router solicitation\r\n
0xd0000165 | Sending router advertisement\r\n
0xd0000166 | Received router advertisement\r\n
0xd0000167 | Receive\r\n
0xd0000168 | ReceiveAndInvalidate\r\n
0xd0000169 | Send\r\n
0xd000016a | FastRegister\r\n
0xd000016b | Bind\r\n
0xd000016c | Invalidate\r\n
0xd000016d | Read\r\n
0xd000016e | Write\r\n
0xd000016f | Not Activated\r\n
0xd0000170 | Activated\r\n
0xd0000171 | TCP connect\r\n
0xd0000172 | TCP send\r\n
0xd0000173 | UDP send\r\n
0xd0000174 | RAW send\r\n
0xd0000175 | Received Router Advertisement\r\n
0xd0000176 | AdminConfigured\r\n
0xd0000177 | NetworkProperty\r\n
0xd0000178 | CreateWolContext\r\n
0xd0000179 | DeleteWolContext\r\n
0xd000017a | SetWolContext\r\n
0xd000017b | ClearWolContext\r\n
0xd000017c | WolContextEvicted\r\n
0xd000017d | AddWolAddress\r\n
0xd000017e | RemoveWolAddress\r\n
0xd000017f | Send\r\n
0xd0000180 | Receive\r\n
0xd0000181 | WFP-ALE: RemoteEndPoint Address\r\n
0xd0000182 | WFP-ALE: RemoteEndPoint Port\r\n
0xd0000183 | WFP-ALE: LocalEndPoint Address\r\n
0xd0000184 | WFP-ALE: LocalEndPoint Port\r\n
0xd0000185 | WFP-ALE: Partition Id\r\n
0xd0000186 | WFP-ALE: Parition NumEnties\r\n
0xd0000187 | SlowDownEntry\r\n
0xd0000188 | SlowDownExit\r\n
0xd0000189 | SlowDownTracking\r\n
0xd000018a | BaseDelayUpdate\r\n
0xd000018b | Ack\r\n
0xd000018c | DupAck\r\n
0xd000018d | Timeout\r\n
0xd000018e | Ecn\r\n
0xd000018f | SpuriousTimeout\r\n
0xd0000190 | Network Context Constraint\r\n
0xd0000191 | Prefix Length Policy\r\n
0xd0000192 | Start Epoch Policy\r\n
0xd0000193 | Default Routes Disabled On Interface\r\n
0xd0000194 | Unconstrained Lookup Disallowed On Interface\r\n
0xd0000195 | Interface Disconnected\r\n
0xd0000196 | Route Invalid Lifetime\r\n
0xd0000197 | Interface Constraint\r\n
0xd0000198 | Scope Constraint\r\n
0xd0000199 | Rechability\r\n
0xd000019a | Prefix Length\r\n
0xd000019b | Route And Interface Metrics\r\n
0xd000019c | Destination And Source Hash\r\n
0xd000019d | Route Order\r\n
0xd000019e | Dead Gateway\r\n
0xd000019f | OnLink Route\r\n
0xd00001a0 | Prefer Same Address\r\n
0xd00001a1 | Prefer Appropriate Scope\r\n
0xd00001a2 | Avoid Deprecated Addresses\r\n
0xd00001a3 | Prefer Home Addresses\r\n
0xd00001a4 | Prefer Outgoing Interface\r\n
0xd00001a5 | Prefer Addresses Associated With NextHop\r\n
0xd00001a6 | Prefer Matching Label\r\n
0xd00001a7 | Prefer Temporary Addresses\r\n
0xd00001a8 | System Defined Preference (Windows Specific)\r\n
0xd00001a9 | Prefer Longest Matching Prefix With NextHop (Windows Specific)\r\n
0xd00001aa | Prefer Longest Matching Prefix\r\n
0xd00001ab | TimerArmed\r\n
0xd00001ac | TimerFired\r\n
0xd00001ad | Failed\r\n
0xd00001ae | Init\r\n
0xd00001af | SetTimeSlotData\r\n
0xd00001b0 | SetTailTimeSlot\r\n
0xd00001b1 | EraseTimestamps\r\n
0xd00001b2 | GetRecoverySeq\r\n
0xd00001b3 | RttSampleUpdate\r\n
0xd00001b4 | TcpFastopenOff\r\n
0xd00001b5 | TcpFastopenAccepting\r\n
0xd00001b6 | TcpFastopenServerSendingCookie\r\n
0xd00001b7 | TcpFastopenServerSentCookie\r\n
0xd00001b8 | TcpFastopenNegotiate\r\n
0xd00001b9 | TcpFastopenAttempt\r\n
0xd00001ba | TcpFastopenNegotiateSuccess\r\n
0xd00001bb | TcpFastopenAttemptSuccess\r\n
0xd00001bc | TcpFastopenCookieRollover\r\n
0xd00001bd | TcpFastopenFailed\r\n
0xd00001be | TcpFastopenFailedBlocklist\r\n
0xd00001bf | TcpFastopenServerAcceptSuccess\r\n
0xd00001c0 | TcpFastopenServerAcceptTimeout\r\n
0xd00001c1 | TcpFastopenServerAcceptSendData\r\n
0xd00001c2 | TcpFastopenFailedSimultaneousConnect\r\n
0xd00001c3 | TcpFastopenFailedInvalidCookie\r\n
0xd00001c4 | TcpFastopenFailedSynTimeout\r\n
0xd00001c5 | TcpFastopenFailedTimeout\r\n
0xd00001c6 | TcpFastopenFailedReset\r\n
0xd00001c7 | TcpFastopenFallback\r\n
0xd00001c8 | TcpFastopenCookieRequestDeclined\r\n
0xd00001c9 | TcpFastopenFailedSuddenRttIncrease\r\n
0xd00001ca | TcpFastopenFailedSynAckWithCookieRequest\r\n
0xd00001cb | TcpFastopenFailedNoNextHop\r\n
0xd00001cc | General failure\r\n
0xd00001cd | Truncated header\r\n
0xd00001ce | Invalid checksum\r\n
0xd00001cf | Inspection drop\r\n
0xd00001d0 | Rejecting loopback neighbor discovery\r\n
0xd00001d1 | Unknown type/code\r\n
0xd00001d2 | Truncated IP header\r\n
0xd00001d3 | Oversized IP header\r\n
0xd00001d4 | No handler\r\n
0xd00001d5 | Not responding with error for error\r\n
0xd00001d6 | Invalid source\r\n
0xd00001d7 | Interface rate limit\r\n
0xd00001d8 | Path rate limit\r\n
0xd00001d9 | No route\r\n
0xd00001da | No matching request\r\n
0xd00001db | Buffer too small\r\n
0xd00001dc | Failed to obtain ancillary data\r\n
0xd00001dd | Incorrect hop limit\r\n
0xd00001de | Unknown code\r\n
0xd00001df | Source not linklocal\r\n
0xd00001e0 | Truncated ND header\r\n
0xd00001e1 | Invalid ND option SourceLinkAddr\r\n
0xd00001e2 | Invalid ND option MTU\r\n
0xd00001e3 | Invalid ND option PrefixInformation\r\n
0xd00001e4 | Invalid ND option RouteInformation\r\n
0xd00001e5 | Invalid ND option RDNSS\r\n
0xd00001e6 | Invalid ND option DNSSL\r\n
0xd00001e7 | Packet parsing failure\r\n
0xd00001e8 | Echo Reply\r\n
0xd00001e9 | Destination Unreachable\r\n
0xd00001ea | Packet Too Big\r\n
0xd00001eb | Destination Unreachable(v4)/Time Exceeded(v6)\r\n
0xd00001ec | Source Quench(v4)/Parameter Problem(v6)\r\n
0xd00001ed | Redirect\r\n
0xd00001ee | Echo Request\r\n
0xd00001ef | Router Advertisement\r\n
0xd00001f0 | Router Solicitation\r\n
0xd00001f1 | Time Exceeded\r\n
0xd00001f2 | Parameter Problem\r\n
0xd00001f3 | Timestamp Request\r\n
0xd00001f4 | Timestamp Reply\r\n
0xd00001f5 | Address Mask Request\r\n
0xd00001f6 | Address Mask Reply\r\n
0xd00001f7 | Echo Request\r\n
0xd00001f8 | Echo Reply\r\n
0xd00001f9 | Multicast Listener Query\r\n
0xd00001fa | Multicast Listener Report\r\n
0xd00001fb | Multicast Listener Done\r\n
0xd00001fc | Router Solicitation\r\n
0xd00001fd | Router Advertisement\r\n
0xd00001fe | Neighbor Solicitation\r\n
0xd00001ff | Neighbor Advertisement\r\n
0xd0000200 | Redirect Message\r\n
0xd0000201 | Multicast Listener Discovery\r\n
0xd0000202 | Not Parsed\r\n
0xd0000203 | Periodic\r\n
0xd0000204 | Aperiodic\r\n
0xd0000205 | Unknown\r\n
0xd0000206 | Public\r\n
0xd0000207 | Private\r\n
0xd0000208 | Domain\r\n
0xd0000209 | Remote\r\n
0xd000020a | Link\r\n
0xd000020b | NonDomainNetwork\r\n
0xd000020c | DomainNetwork\r\n
0xd000020d | DomainAuthenticated\r\n
0xd000020e | InterfaceAddition\r\n
0xd000020f | InterfaceDeletion\r\n
0xd0000210 | ZoneChange\r\n
0xd0000211 | ConfigurationFlagChange\r\n
0xd0000212 | ForwardingEnable\r\n
0xd0000213 | ForwardingDisable\r\n
0xd0000214 | WeakHostReceiveEnable\r\n
0xd0000215 | WeakHostReceiveDisable\r\n
0xd0000216 | NetworkCategoryStateChange\r\n
0xd0000217 | MetricChange\r\n
0xd0000218 | MediaConnect\r\n
0xd0000219 | MediaDisconnect\r\n
0xd000021a | OffloadCapabilityChange\r\n
0xd000021b | DisableDefaultRoutesSet\r\n
0xd000021c | DisableDefaultRoutesReset\r\n
0xd000021d | ForceTunnelingSet\r\n
0xd000021e | ForceTunnelingReset\r\n
0xd000021f | LimitedLinkConnectivitySet\r\n
0xd0000220 | LimitedLinkConnectivityReset\r\n
0xd0000221 | LocalityConfigChange\r\n
0xd0000222 | DisableUnconstrainedRouteLookupSet\r\n
0xd0000223 | DisableUnconstrainedRouteLookupReset\r\n
0xd0000224 | PortStateChange\r\n
0xd0000225 | NoInternetConnectivity\r\n
0xd0000226 | NoInternetDnsResolutionSucceeded\r\n
0xd0000227 | InternetConnectivityDetected\r\n
0xd0000228 | InternetConnectivityUnknown\r\n
0xd0000229 | Timeout\r\n
0xd000022a | DadStarted\r\n
0xd000022b | OptimisticDadStarted\r\n
0xd000022c | DadPassed\r\n
0xd000022d | NSReceived\r\n
0xd000022e | NAReceived\r\n
0xd000022f | InterfaceDisabled\r\n
0xd0000230 | DadDisabled\r\n
0xd0000231 | AddressAddition\r\n
0xd0000232 | AddressDeletion\r\n
0xd0000233 | DadStatePreferred\r\n
0xd0000234 | DadStateDuplicate\r\n
0xd0000235 | DadStateDeprecated\r\n
0xd0000236 | SkipAsSourceSet\r\n
0xd0000237 | SkipAsSourceReset\r\n
0xd0000238 | TunnelSkipAsSourceSet\r\n
0xd0000239 | TunnelSkipAsSourceReset\r\n
0xd000023a | ZoneChange\r\n
0xd000023b | NeighborAddition\r\n
0xd000023c | NeighborDeletion\r\n
0xd000023d | NeighborUnreachable\r\n
0xd000023e | NeighborReachable\r\n
0xd000023f | NeighborAddressUpdate\r\n
0xd0000240 | DeadRouteTimeout\r\n
0xd0000241 | DeadRouteProbeTimeout\r\n
0xd0000242 | AllRoutesDead\r\n
0xd0000243 | TlConfirmsForwardReachability\r\n
0xd0000244 | DeadGatewayDetected\r\n
0xd0000245 | RouterRedirect\r\n
0xd0000246 | ProbeConnectionFailed\r\n
0xd0000247 | ConfigurationChange\r\n
0xd0000248 | Alive\r\n
0xd0000249 | Dead\r\n
0xd000024a | Probe\r\n
0xd000024b | Disable\r\n
0xd000024c | Enable\r\n
0xd000024d | NotConfident\r\n
0xd000024e | InvalidLoad\r\n
0xd000024f | ConfidenceUpdate\r\n
0xd0000250 | TCP Fastopen\r\n
0xd0000251 | Init\r\n
0xd0000252 | StatusIndication\r\n
0xd0000253 | GlobalSetting\r\n
0xd0000254 | Forwarding\r\n
0xd0000255 | IncompatibleCallout\r\n
0xd0000256 | RA DNS information change\r\n
0xd0000257 | RA DNS entry added\r\n
0xd0000258 | RA DNS entry expired by RA\r\n
0xd0000259 | RA DNS entry expired by timer\r\n
0xd000025a | RA DNS entry lifetime reset\r\n
0xd000025b | RA DNS entry reordered\r\n
0xd000025c | RA DNS entry deleted due to max limit\r\n
0xd000025d | RA DNS entry lifetime updated\r\n
0xd000025e | RA DNS ND entry ignored due to limit\r\n
0xd000025f | RA DNS ND entry ignored due to memory failure\r\n
0xd0000260 | RA DNS ND entry ignored due to zero lifetime\r\n
0xd0000261 | RA DNS ND entries corrupted\r\n
0xd0000262 | RA DNS RouterContext init failed\r\n
0xd0000263 | Manual\r\n
0xd0000264 | WellKnown\r\n
0xd0000265 | DHCP\r\n
0xd0000266 | RouterAdvertisement\r\n
0xd0000267 | 6to4\r\n
0xd0000268 | Avoid Unusable Destination\r\n
0xd0000269 | Prefer Aoac Interface\r\n
0xd000026a | Prefer Matching Scope\r\n
0xd000026b | Avoid Deprecated Address\r\n
0xd000026c | Prefer Matching Label\r\n
0xd000026d | Prefer Internet Connected Interface\r\n
0xd000026e | Prefer Higher Precedence\r\n
0xd000026f | Prefer Longer Route Destination Prefix\r\n
0xd0000270 |  Prefer Native Transport(Physical Interface)\r\n
0xd0000271 | Prefer Lower Interface Metric\r\n
0xd0000272 | Prefer Smaller Scope\r\n
0xd0000273 | Prefer Same Address\r\n
0xd0000274 | Prefer Appropriate Scope\r\n
0xd0000275 | Avoid Deprecated Address\r\n
0xd0000276 | Prefer Outgoing Interface\r\n
0xd0000277 | Prefer Source Address Associated With Nexthop\r\n
0xd0000278 | Prefer Temporary Address\r\n
0xd0000279 | System Defined Preference\r\n
0xd000027a | Prefer Source With Longer NextHop Prefix Match\r\n
0xd000027b | Locality Metric\r\n
0xd000027c | Prefer Longer Source/Destination Common Prefix Length\r\n
0xd000027d | Order Unchanged (No Preference)\r\n
0xd000027e | Send\r\n
0xd000027f | Disconnect\r\n
0xd0000280 | Accept\r\n
0xd0000281 | Receive\r\n
0xd0000282 | ReceiveTcpDatagram\r\n
0xd0000283 | ReceiveDatagram\r\n
0xd0000284 | RemoteDisconnect\r\n
0xd0000285 | ReceiveControlMessage\r\n
0xd0000286 | RespondDatagram\r\n
0xd0000287 | BindEndpoint\r\n
0xd0000288 | Listen\r\n
0xd0000289 | AcceptComplete\r\n
0xd000028a | Connect\r\n
0xd000028b | ConnectComplete\r\n
0xd000028c | Raw\r\n
0xd000028d | ConnectRequest\r\n
0xd000028e | CreateEndpoint\r\n
0xd000028f | AcquirePort\r\n
0xd0000290 | Offload\r\n
0xd0000291 | SocketOption\r\n
0xd0000292 | BindEndpointRequest\r\n
0xd0000293 | Drop\r\n
0xd0000294 | Allow\r\n
0xd0000295 | Pend\r\n
0xd0000296 | DropAndSendIcmp\r\n
0xd0000297 | Allow\r\n
0xd0000298 | Deny\r\n
0xd0000299 | Authorize\r\n
0xd000029a | RetryWithHint\r\n

### 10.0.17763.437, 10.0.17763.557

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto = %3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm = %6, MaxDataRetransmissions = %7, DelayedAckTicks = %8 msec, DelayedAckFrequency = %9, RACK enabled = %10, Tail Loss Probe enabled = %11.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5, Event = %6.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick = %4 Time = %5.\r\n
0xb0000527 | %1 timer rescheduled by processor %2 for processor %3 at Tick = %4 to Tick = %5, OldScheduledExpiration = %6 NewScheduledExpiration = %7 DueTime = %8 Aperiodic = %9.\r\n
0xb0000528 | %1 timer fired on processor %2 at Tick = %3, was scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for Destination %4 in Compartment %5, Reason: %8 (Rule %6.%7).\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0000558 | Teredo Add -- PID: %1 started listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb0000559 | Teredo Remove -- PID: %1 stopped listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb000055a | IP: RouteLookup - API: %1 DstAddr: %3 ConstrainSrcAddr: %4 ConstrainIfIndex: %5 ConstraintOveridden: %6 ReturnConstrained: %7 OutgoingIfIndex: %8 NextHopAddr: %9 Status: %10\r\n
0xb000055b | IP: SourceAddrLookup - DstAddr: %2 ConstrainSrcAddr: %3 ConstrainIfIndex: %4 OutgoingIfIndex: %5 ReturnConstrained: %6 SelectedSrcAddr: %7\r\n
0xb000055c | WFP-ALE: Partition Count=%1 Partition Mask=%2: Partition Id=%d Partition NumEntries = %4.\r\n
0xb000055d | WFP-ALE: HotAdd/Remove: Old Partiton Count=%1 Old Partition Mask=%2 New Partiton Count=%1 New Partition Mask=%2.\r\n
0xb000055e | WFP-ALE: RemoteEndPoint Insertion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb000055f | WFP-ALE: RemoteEndPoint Deletion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb0000560 | WFP-ALE: ALE: low memory state detected. LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000561 | WFP-ALE: leaving low memory state. HighMemoryEvent = %1 HighNonPagedPoolEvent = %2.\r\n
0xb0000562 | WFP-ALE: Dpc for cleanup initiated: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000563 | WFP: Dpc for cleanup QUEUED or RE-QUEUED: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000564 | TCP: LEDBAT %2: Connection %1, BaseDelayMs = %6, CurrentDelayMs = %7, CWnd = %3, SsThresh = %4, SndWnd = %5, DelayBasedCwndFactor %9%%, RemainingTimeMs = %8.\r\n
0xb0000565 | TCP: AssociateNameResContext Endpoint: %1 Status: %16 NameResolutionContext: %2 DnsName: %3 InterfaceIndex: %4 IPAddrCount: %5 IPAddrs: %7 %9 %11 %13 %15\r\n
0xb0000566 | TCP: InspectConnectWithNameResContext Connection: %5 (local: %2 remote: %4) NameResolutionContext: %6 DnsName: %7 Status: %8.\r\n
0xb0000567 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 InterfaceMetric: %10 RouteMetric: %11] is preferred over Route [DestinationPrefix: %14/%12 NextHop: %16 InterfaceIndex: %17 InterfaceMetric: %18 RouteMetric: %19] for Destination: %3 in Compartment: %1, Reason: %20.\r\n
0xb0000568 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 RouteMetric: %10] is blocked for Destination: %3 ConstrainInterfaceIndex: %11 ConstrainScopeZone: %12 in Compartment: %1, Reason: %13.\r\n
0xb0000569 | TCP: Tail Loss Probe Send Connection = %1 SndUna = %2, SndMax = %3, SendAvailable = %4, TailProbeSeq = %5, TailProbeLast = %6, ControlsToSend = %7, ThFlags = %8.\r\n
0xb000056a | TCP: Tail Loss Probe Event Connection = %1, Event = %2.\r\n
0xb000056b | TCP: RACK Event Connection = %1, Event = %2, MinRTT = %3, ReoWind = %4, TimeSlotDeltaMin = %5, SeqNum = %6, Timestamp = %7, RttSample = %8.\r\n
0xb000056c | TCP: Fastopen state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000056d | UDP: endpoint (family=%5 pid=%3) create failed: address family not attached.\r\n
0xb000056e | UDP: endpoint %1 (family=%5 pid=%3) create failed: compartment %4 not found.\r\n
0xb000056f | UDP: endpoint %1 (family=%5 pid=%3) created.\r\n
0xb0000570 | UDP: endpoint %1 (family=%5 pid=%3) create failed: inspection status = %2\r\n
0xb0000571 | UDP: endpoint %4 bind failed: address %2 cannot be resolved, status = %3\r\n
0xb0000572 | UDP: endpoint %4 (sockaddr=%2) bind failed: port-acquisition status = %3\r\n
0xb0000573 | UDP: endpoint %4 (sockaddr=%2) bind failed: inspection status = %3\r\n
0xb0000574 | UDP: endpoint %4 (sockaddr=%2) bound.\r\n
0xb0000575 | UDP: endpoint %4 (sockaddr=%2) closed.\r\n
0xb0000576 | UDP: endpoint %4 closed.\r\n
0xb0000577 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address resolution status = %6\r\n
0xb0000578 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address validation failed.\r\n
0xb0000579 | UDP: endpoint %1 (sockaddr=%3) send messages %5: source-address selection status = %6\r\n
0xb000057b | UDP: address family %2added to interface %1.\r\n
0xb000057c | UDP: address family %2removed from interface %1.\r\n
0xb000057d | UDP: Failure initializing transport protocol, status = %1\r\n
0xb000057e | UDP: Failure starting NLNPI client, status = %1\r\n
0xb000057f | UDP: Failure initializing NSI support, status = %1\r\n
0xb0000580 | UDP: Failure starting TLNPI provider, status = %1\r\n
0xb0000581 | UDP: Failure initializing QoS support, status = %1\r\n
0xb0000582 | UDP: Failure starting %1, status = %2\r\n
0xb0000583 | UDP: endpoint %1 (sockaddr=%3) send messages %5: could not allocate send context.\r\n
0xb0000584 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path af failure, status = %6\r\n
0xb0000585 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path missing next hop failure.\r\n
0xb0000586 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path next hop address failure.\r\n
0xb0000587 | TCP: Early Retransmission, FACK or RACK, Connection = %1, SndUna = %2, SackIsLostSeq = %3, DupAckCount = %4\r\n
0xb0000588 | TCP: Ignoring fastopen SYN option due to limit on concurrent SYN_RCVD fastopen connections, Connection = %1, SynRcvdLimit = %2\r\n
0xb0000589 | TCP: Failed to update fastopen key state, Location = %1, Status = %2. Server-side fastopen will be disabled\r\n
0xb000058a | TCP: Fast Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058b | TCP: SACK Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058c | TCP: Limited Transmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058d | TCP: SACK Retransmit Additional Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058e | %1: %2message. Type = %3, Code = %4, CompartmentId = %5, SourceAddress = %7, DestAddress = %9\r\n
0xb000058f | %1: %2path drop. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11\r\n
0xb0000590 | %1: Echo timeout. Status = %4\r\n
0xb0000591 | %1 Timer state changed to %3 by Processor %2 Usage = %4 at Tick = %5\r\n
0xb0000592 | TCP: connection %1 send complete %3 bytes at %4 (%2).\r\n
0xb0000593 | IP: Compartment creation. Compartment = %1, Protocol = %2, Private = %3, Status = %4.\r\n
0xb0000594 | IP: Compartment deletion. Compartment = %1, Protocol = %2.\r\n
0xb0000595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13.\r\n
0xb0000596 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5 CwrMax = %6.\r\n
0xb0000597 | IP: Compartment cleanup. Compartment = %1, Protocol = %2.\r\n
0xb0000598 | IP: Interface network category state change. Interface = %1, Compartment = %2 , Protocol = %3, NetworkCategory = %4, DomainNetworkLocation = %5, DomainType = %6, Signature = %7.\r\n
0xb0000599 | IP: Interface creation. Interface = %1, Compartment = %2, Protocol = %3, PhysicalMediumType = %4, Status = %5.\r\n
0xb000059a | IP: Interface deletion. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059b | IP: Interface cleanup. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059c | IP: SubInterface creation. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4, Status = %5.\r\n
0xb000059d | IP: SubInterface deletion. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059e | IP: SubInterface cleanup. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059f | IP: Interface change Notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005a0 | IP: Interface internet connectivity status change. Interface = %1, Compartment = %2, Protocol = %3, OldConnectivityStatus = %4, NewConnectivityStatus = %5.\r\n
0xb00005a1 | IP: Address change notification. Address = %2, Interface = %3, Compartment = %4, Protocol = %5, Reason = %6.\r\n
0xb00005a2 | IP: Route change notification. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, NotifyFlags = %8.\r\n
0xb00005a3 | IP: Neighbor change notification. IpAddress = %2, DlAddress = %4, Interface = %5, Compartment = %6, State = %7, Reason = %8.\r\n
0xb00005a4 | IP: Address DAD state change. Address = %2, Interface = %3, Compartment = %4, OldState = %5, NewState = %6, Reason = %7.\r\n
0xb00005a5 | IP: Route Dead Gateway Detection state change. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, OldState = %8, NewState = %9, OldProbeCount = %10, NewProbeCount = %11, OldUnreachablePaths = %12, NewUnreachablePaths = %13, OldMovedPaths = %14, NewMovedPaths = %15, TotalPaths = %16, OldStateChangeTick = %17, NewStateChangeTick = %18, DgdNeedsReset = %19, Reason = %20.\r\n
0xb00005a6 | IP: Disconnecting TCP connections with Address = %2, Interface = %3, Compartment = %4, SkipLocal = %5, SkipOnLink = %6.\r\n
0xb00005a7 | TCP: connection %1: Sending paced chunk of %6 bytes with CWnd = %2, SndWnd = %3, BytesAvailable = %4, BytesOutstanding = %5\r\n
0xb00005a8 | Fallback: Context = %1, Feature = %2, TraceReason = %3, Confidence = %4, Successes = %5, Failures = %6\r\n
0xb00005a9 | TCPIP: TCB %1 using fast loopback\r\n
0xb00005aa | IP: Router information change notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005ab | IP: %1. Interface = %2, Compartment = %3, RouterAddress = %5, DNS Server/Suffix: %7 %8, Lifetime = %9.\r\n
0xb00005ac | IP: Route rundown. Interface = %1, Compartment = %2, Prefix = %4/%5, NextHop = %7, Metric = %8, State = %9, Origin = %10, Age = %11, ValidLifetime = %12, PreferredLifetime = %13, Flags = %14.\r\n
0xb00005ad | TCP: CUBIC ECN event. Connection %1, CWnd %2, SSThresh = %3, SndUna = %4\r\n
0xb00005ae | INETINSPECT: Owner = %1, InspectHandle = %2, InspectType = %3, Action = %4, Status = %5\r\n
0xb00005b0 | FallbackCheck: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b1 | FallbackUpdate: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b2 | Fallback: Permanently disabling feature, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b3 | Fallback: Enabling feature for this boot session, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b4 | Fallback: Feature previously disabled, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b5 | TCP Fastopen fallback update: Tcb = %1, FastopenState = %2, DataBytesIn = %3, ShutdownStatus = %4, ProbeStatus = %5\r\n
0xb00005b6 | Disabling feature until connectivity is established: CompartmentId =%1, IfIndex = %2, Feature = %3, ConnectivityStatus = %4\r\n
0xb00005b7 | Disabling %1 for loopback connection\r\n
0xb00005b8 | Disabling TCP Fastopen for BaseEndpoint = %1 because an incompatible WFP callout is installed\r\n
0xb00005b9 | IP: Setting source constraint for route lookup - Compartment: %1 DstAddr: %3 ConstrainSrcAddr: %5 ConstrainIfIndex: %6 ConstraintFlags: %7\r\n
0xb00005ba | WFP-ALE: RemoteEndPoint Insertion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bb | WFP-ALE: RemoteEndPoint Deletion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bc | TCP: connection %8 (local=%2 remote=%4) system abort. PID = %6.\r\n
0xb00005bd | Disabling %1 due to no next hop\r\n
0xb00005be | TCP: endpoint (sockaddr=%2) bind failed: wake status = %3.\r\n
0xb00005bf | UDP: endpoint %4 (sockaddr=%2) bind failed: wake status = %3\r\n
0xb00005c0 | Acquire wake port %2, type=%1, family=%3, IF=%4, compartment=%5\r\n
0xb00005c1 | TCP: Connection %1 reached max SACK queue length\r\n
0xb00005c2 | TCP: Connection %1 requested fast open\r\n
0xb00005c3 | TCP: CUBIC Hystart state change event. Connection %1, State %2, CWnd %3, SSThresh = %4.\r\n
0xb00005c4 | IP: Transmitting loopback Nbl %1. Interface=%2, Compartment=%3, Src=%6, Dst=%5, Proto=%7.\r\n
0xb00005c5 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26 ConnectionTimeMs %27 Timestamps %28 RttUs %29 MinRtt %30 MaxRtt %31 SynRetrans %32 CongestionAlgorithm %33 \   State %34 Local %36 Remote %38 CWnd %39 SsThresh %40 RcvWnd %41 RcvBuf %42 SndWnd %43.\r\n
0xb00005c6 | TCPIP: Framing layer %1 (AddressFamily=%2) dropped %4 packet(s) on interface=%3, Reason=%5, Data=%6.\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010452 | IP: Interface media disconnect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001045a | IP: Address DAD successful. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001045b | IP: Address DAD failed. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2, DL address of packet = %5.\r\n
0xb001045c | IP: Address DAD started. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010467 | IP: Address addition. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010468 | IP: Address deletion. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001046a | Framing: Interface operation status change. Interface = %1, Compartment = %4, Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0010470 | Framing: NDIS pause event. Interface = %1, Compartment = %3.\r\n
0xb0010471 | Framing: NDIS restart event. Interface = %1, Compartment = %3.\r\n
0xb0010478 | IP: Interface property change. Interface = %1, Compartment = %10, Protocol = %11, Advertise = %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7, WeakHostSend = %8, WeakHostReceive = %9.\r\n
0xb00104b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, Address = %4 %3 %6.\r\n
0xb00104b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7.\r\n
0xb0010529 | IP: Interface media connect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052a | IP: Interface limited link connectivity set. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052b | IP: Interface limited link connectivity reset. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052c | IP: Neighbor state change. IPAddress = %3, DLAddress = %5, Interface = %1, Compartment = %9, OldState = %6, NewState = %7, Event = %8.\r\n
0xb001052d | IP: Neighbor Discovery. Event = %5, Interface = %1, Compartment = %6, SourceIpAddress = %3, TargetIpAddress = %4.\r\n
0xb001052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions: %6, Reason: %10 (Rule %7 %8.%9).\r\n
0xb0010534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb001054e | IP: Interface configuration flags updated. Interface = %1, Compartment = %5, Protocol = %6, Property = %2, Value = %3, Event = %4.\r\n
0xb0010557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9, NrtNameResolutionId %10\r\n
0xb0010565 | TCP: AssociateNameResContext EndpointObj: %1 IsConnectionObj: %2 NameResContext: %3 Status: %4\r\n
0xb0010595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13 IsLimitedSlowStart = %14.\r\n
0xb00204b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, Address = %4 %3 %6.\r\n
0xb00304b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Metric = %11, Connected = %12, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, InternetConnectivityStatus = %13, Flags = %14, Address = %4 %3 %6.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | PacingTimer\r\n
0xd000002c | DisconnectTimer\r\n
0xd000002d | SwsTimer\r\n
0xd000002e | ReassemblyRateTimer\r\n
0xd000002f | SynOrRstValidationTimer\r\n
0xd0000030 | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000031 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000032 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000033 | TCP_KEEPALIVE\r\n
0xd0000034 | TCP_MAXSEG\r\n
0xd0000035 | TCP_MAXRT\r\n
0xd0000036 | TCP_STDURG\r\n
0xd0000037 | TCP_NOURG\r\n
0xd0000038 | TCP_ATMARK\r\n
0xd0000039 | TCP_NOSYNRETRIES\r\n
0xd000003a | TCP_TIMESTAMPS\r\n
0xd000003b | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003c | TCP_CONGESTION_ALGORITHM\r\n
0xd000003d | TCP_DELAY_FIN_ACK\r\n
0xd000003e | SO_DEBUG\r\n
0xd000003f | SO_ACCEPTCONN\r\n
0xd0000040 | SO_REUSEADDR\r\n
0xd0000041 | SO_KEEPALIVE\r\n
0xd0000042 | SO_DONTROUTE\r\n
0xd0000043 | SO_BROADCAST\r\n
0xd0000044 | SO_USELOOPBACK\r\n
0xd0000045 | SO_LINGER\r\n
0xd0000046 | SO_OOBINLINE\r\n
0xd0000047 | SO_SNDBUF\r\n
0xd0000048 | SO_RCVBUF\r\n
0xd0000049 | SO_CONDITIONAL_ACCEPT\r\n
0xd000004a | SO_PAUSE_ACCEPT\r\n
0xd000004b | SO_COMPARTMENT_ID\r\n
0xd000004c | SO_RANDOMIZE_PORT\r\n
0xd000004d | SO_PORT_SCALABILITY\r\n
0xd000004e | NldsInvalid\r\n
0xd000004f | NldsTentative\r\n
0xd0000050 | NldsDuplicate\r\n
0xd0000051 | NldsDeprecated\r\n
0xd0000052 | NldsPreferred\r\n
0xd0000053 | Indicate\r\n
0xd0000054 | Pend\r\n
0xd0000055 | Satisfy\r\n
0xd0000056 | NdisPhysicalMediumUnspecified\r\n
0xd0000057 | NdisPhysicalMediumWirelessLan\r\n
0xd0000058 | NdisPhysicalMediumCableModem\r\n
0xd0000059 | NdisPhysicalMediumPhoneLine\r\n
0xd000005a | NdisPhysicalMediumDSL\r\n
0xd000005b | NdisPhysicalMedium1394\r\n
0xd000005c | NdisPhysicalMediumWirelessWan\r\n
0xd000005d | NdisPhysicalMediumNative802_11\r\n
0xd000005e | NdisPhysicalMediumBluetooth\r\n
0xd000005f | NdisPhysicalMediumInfiniband\r\n
0xd0000060 | NdisPhysicalMediumWiMax\r\n
0xd0000061 | NdisPhysicalMedium802_3\r\n
0xd0000062 | NdisPhysicalMedium802_5\r\n
0xd0000063 | NdisPhysicalMediumIrda\r\n
0xd0000064 | NdisPhysicalMediumWiredWAN\r\n
0xd0000065 | IP checksum offload not computed\r\n
0xd0000066 | TCP checksum offload not computed\r\n
0xd0000067 | UDP checksum offload not computed\r\n
0xd0000068 | Header not aligned on 4-byte boundary\r\n
0xd0000069 | IP fragmentation\r\n
0xd000006a | Source address is not unicast\r\n
0xd000006b | Destination address is not unicast\r\n
0xd000006c | Ethernet and IP header not contiguous\r\n
0xd000006d | IP options present\r\n
0xd000006e | ESP over UDP\r\n
0xd000006f | Lack contiguous space for upper layer headers\r\n
0xd0000070 | WFP filters present\r\n
0xd0000071 | Nexthop is unavailable\r\n
0xd0000072 | Path has been invalidated due to policy change\r\n
0xd0000073 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000074 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000075 | Session state is not compatible\r\n
0xd0000076 | TCP options present\r\n
0xd0000077 | UDP IPv6 checksum absent in packet\r\n
0xd0000078 | Packet is for a loopback interface\r\n
0xd0000079 | Packet is from a Raw Socket\r\n
0xd000007a | TL Ancillary headers present\r\n
0xd000007b | NL Ancillary headers present\r\n
0xd000007c | Type of Service present\r\n
0xd000007d | IpSec headers present\r\n
0xd000007e | Interface is not Ethernet\r\n
0xd000007f | Nbl check failed\r\n
0xd0000080 | Destination address is unknown\r\n
0xd0000081 | Loopback inspect failed\r\n
0xd0000082 | Failed to allocate the WSD cache\r\n
0xd0000083 | Failure initializing PnP work queue\r\n
0xd0000084 | Failed to get persistent parameters\r\n
0xd0000085 | Rejected persistent parameters\r\n
0xd0000086 | qualified profile\r\n
0xd0000087 | qualified destination\r\n
0xd0000088 | sample collection completion\r\n
0xd0000089 | idle time expiration\r\n
0xd000008a | allocation\r\n
0xd000008b | new sample request\r\n
0xd000008c | configuration change\r\n
0xd000008d | Idle\r\n
0xd000008e | ProbingWs\r\n
0xd000008f | ProbeWait\r\n
0xd0000090 | ProbingWithoutWs\r\n
0xd0000091 | RecordWait\r\n
0xd0000092 | EreQualified\r\n
0xd0000093 | Qualified\r\n
0xd0000094 | Source Unspecified\r\n
0xd0000095 | Destination is multicast\r\n
0xd0000096 | Header is invalid (location 0)\r\n
0xd0000097 | Checksum is invalid\r\n
0xd0000098 | Transport endpoint was not found\r\n
0xd0000099 | Connected path error\r\n
0xd000009a | Session state error\r\n
0xd000009b | Receive Inspection\r\n
0xd000009c | ACK Invalid (subreason 0) (invalid ACK in SYN_SENT state)\r\n
0xd000009d | Expected SYN\r\n
0xd000009e | Received RST (subreason 0)\r\n
0xd000009f | Received SYN while in SYN_RCVD state\r\n
0xd00000a0 | Simultaneous Connect\r\n
0xd00000a1 | PAWS Failed\r\n
0xd00000a2 | Land Attack (subreason 0)\r\n
0xd00000a3 | Missed RST\r\n
0xd00000a4 | Outside Receive Window (subreason 0)\r\n
0xd00000a5 | Duplicate Segment\r\n
0xd00000a6 | Closed Window\r\n
0xd00000a7 | TCB Removed\r\n
0xd00000a8 | FIN-WAIT2\r\n
0xd00000a9 | Reassembly Conflict\r\n
0xd00000aa | FIN Received\r\n
0xd00000ab | Listener received segment with invalid flags\r\n
0xd00000ac | URG flag set but could not allocate urgent data state\r\n
0xd00000ad | TCB was not inserted in TCB table\r\n
0xd00000ae | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000af | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000b0 | Packet dropped by TIME-WAIT TCB (subreason 0)\r\n
0xd00000b1 | SYN+ACK with Fastopen cookie request\r\n
0xd00000b2 | Listener dropped SYN because SO_PAUSE_ACCEPT was set\r\n
0xd00000b3 | Listener dropped SYN to reduce memory pressure\r\n
0xd00000b4 | Bad source address\r\n
0xd00000b5 | Not locally destined\r\n
0xd00000b6 | Protocol unreachable\r\n
0xd00000b7 | Port unreachable\r\n
0xd00000b8 | Bad length\r\n
0xd00000b9 | Malformed Header\r\n
0xd00000ba | No route available\r\n
0xd00000bb | Beyond scope\r\n
0xd00000bc | Inspection drop\r\n
0xd00000bd | Too many decapsulations\r\n
0xd00000be | Administratively prohibited\r\n
0xd00000bf | Hop limit exceeded\r\n
0xd00000c0 | Address unreachable\r\n
0xd00000c1 | Fragment MTU exceeded\r\n
0xd00000c2 | Buffer Length Exceeded\r\n
0xd00000c3 | Address Resolution Timeout\r\n
0xd00000c4 | Address Resolution Failure\r\n
0xd00000c5 | IPsec failure\r\n
0xd00000c6 | Extension Headers Failure\r\n
0xd00000c7 | Allocation Failure\r\n
0xd00000c8 | IPSNPI Drop\r\n
0xd00000c9 | Unsupported Offload\r\n
0xd00000ca | Routing Failure\r\n
0xd00000cb | Ancillary Data Failure\r\n
0xd00000cc | Raw Data Failure\r\n
0xd00000cd | Session State Failure\r\n
0xd00000ce | Default\r\n
0xd00000cf | NewReno\r\n
0xd00000d0 | CTCP\r\n
0xd00000d1 | DCTCP\r\n
0xd00000d2 | LEDBAT\r\n
0xd00000d3 | CUBIC\r\n
0xd00000d4 | TcpTemplateTypeInternet\r\n
0xd00000d5 | TcpTemplateTypeDatacenter\r\n
0xd00000d6 | TcpTemplateTypeCompat\r\n
0xd00000d7 | TcpTemplateTypeDatacenterCustom\r\n
0xd00000d8 | TcpTemplateTypeInternetCustom\r\n
0xd00000d9 | TcpTemplateTypeDefault\r\n
0xd00000da | TcpTemplateTypeAutomatic\r\n
0xd00000db | No Failure\r\n
0xd00000dc | Unknown\r\n
0xd00000dd | System Policy\r\n
0xd00000de | NIC Capacity Reached\r\n
0xd00000df | System Low On Memory\r\n
0xd00000e0 | WFP driver / Stream inspection\r\n
0xd00000e1 | Weak Host Model Enabled\r\n
0xd00000e2 | Forwarding Enabled\r\n
0xd00000e3 | Hardware capability\r\n
0xd00000e4 | NDIS filter/NIC property\r\n
0xd00000e5 | Loopback fast path socket option not set on both ends\r\n
0xd00000e6 | Filter policy existed for the loopback connection\r\n
0xd00000e7 | IPv4\r\n
0xd00000e8 | IPv6\r\n
0xd00000e9 | unbind\r\n
0xd00000ea | bind\r\n
0xd00000eb | port change\r\n
0xd00000ec | none\r\n
0xd00000ed | receive hash\r\n
0xd00000ee | receive scale\r\n
0xd00000ef | enabled\r\n
0xd00000f0 | disabled\r\n
0xd00000f1 | removing\r\n
0xd00000f2 | adding\r\n
0xd00000f3 | complete binding initialization\r\n
0xd00000f4 | complete port initialization\r\n
0xd00000f5 | enumerate interface ports\r\n
0xd00000f6 | query port link state\r\n
0xd00000f7 | query port interface index\r\n
0xd00000f8 | query interface ports\r\n
0xd00000f9 | query port RSS capabilities\r\n
0xd00000fa | get usable processors\r\n
0xd00000fb | query port driver version\r\n
0xd00000fc | query port RSS processor configuration\r\n
0xd00000fd | set receive scale parameters\r\n
0xd00000fe | set receive hash parameters\r\n
0xd00000ff | update interface ports\r\n
0xd0000100 | not available\r\n
0xd0000101 | available\r\n
0xd0000102 | available on ports\r\n
0xd0000103 | global configuration\r\n
0xd0000104 | active mode\r\n
0xd0000105 | Bind Adapter\r\n
0xd0000106 | Unbind Adapter (begin)\r\n
0xd0000107 | Unbind Adapter (end)\r\n
0xd0000108 | NetEvent Restart\r\n
0xd0000109 | NetEvent Power-down\r\n
0xd000010a | NetEvent Power-up\r\n
0xd000010b | NetEvent NDK-enable\r\n
0xd000010c | NetEvent NDK-disable\r\n
0xd000010d | NetEvent NDK usage stopped\r\n
0xd000010e | Indicate new NDK interface arrival\r\n
0xd000010f | Indicate NDK interface removal\r\n
0xd0000110 | Indicate NDK operational status change\r\n
0xd0000111 | Undefined\r\n
0xd0000112 | Adapter\r\n
0xd0000113 | QP\r\n
0xd0000114 | CQ\r\n
0xd0000115 | MR\r\n
0xd0000116 | MW\r\n
0xd0000117 | PD\r\n
0xd0000118 | SharedEndpoint\r\n
0xd0000119 | Connector\r\n
0xd000011a | Listener\r\n
0xd000011b | SRQ\r\n
0xd000011c | Max\r\n
0xd000011d | Async\r\n
0xd000011e | Inline\r\n
0xd000011f | Local\r\n
0xd0000120 | Remote\r\n
0xd0000121 | Privileged\r\n
0xd0000122 | Local\r\n
0xd0000123 | Remote\r\n
0xd0000124 | NotifyErrors\r\n
0xd0000125 | NotifyAny\r\n
0xd0000126 | NotifySolicited\r\n
0xd0000127 | Invalid\r\n
0xd0000128 | Software Slot allocated\r\n
0xd0000129 | Hardware Slot allocated\r\n
0xd000012a | Policy error\r\n
0xd000012b | system error\r\n
0xd000012c | Enabled\r\n
0xd000012d | Send request dropped\r\n
0xd000012e | Receive dropped\r\n
0xd000012f | Disconnect request dropped\r\n
0xd0000130 | Reset dropped\r\n
0xd0000131 | WFP API No Failure\r\n
0xd0000132 | WFP API WasRedirectedToProxy\r\n
0xd0000133 | WFP API RegisterForExitingEndpoint\r\n
0xd0000134 | WFP API ClassifiableFieldGetAf\r\n
0xd0000135 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000136 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd0000137 | WFP API ClassifiableFieldGetRemotePort\r\n
0xd0000138 | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd0000139 | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd000013a | Processor Add\r\n
0xd000013b | Power Source Change\r\n
0xd000013c | AC\r\n
0xd000013d | DC\r\n
0xd000013e | DC Short Term\r\n
0xd000013f | Unknown\r\n
0xd0000140 | is stopping timers\r\n
0xd0000141 | has stopped timers\r\n
0xd0000142 | is locking partitions\r\n
0xd0000143 | has locked partitions\r\n
0xd0000144 | is unlocking partitions\r\n
0xd0000145 | has unlocked partitions\r\n
0xd0000146 | is starting timers\r\n
0xd0000147 | has started timers\r\n
0xd0000148 | is starting\r\n
0xd0000149 | is complete\r\n
0xd000014a | IP\r\n
0xd000014b | TCP\r\n
0xd000014c | leaving S0\r\n
0xd000014d | entering S0\r\n
0xd000014e | Unreachable\r\n
0xd000014f | Incomplete\r\n
0xd0000150 | Probe\r\n
0xd0000151 | Delay\r\n
0xd0000152 | Stale\r\n
0xd0000153 | Reachable\r\n
0xd0000154 | Permanent\r\n
0xd0000155 | Maximum\r\n
0xd0000156 | Map\r\n
0xd0000157 | Configure\r\n
0xd0000158 | TlSuspectsReachability\r\n
0xd0000159 | TlConfirmsReachability\r\n
0xd000015a | NaConfirmsReachability\r\n
0xd000015b | ProbeReachability\r\n
0xd000015c | DadSolicitation\r\n
0xd000015d | NewDlAddress\r\n
0xd000015e | TriggerNud\r\n
0xd000015f | Resolve\r\n
0xd0000160 | Timeout\r\n
0xd0000161 | Sending neighbor solicitation\r\n
0xd0000162 | Received neighbor solicitation\r\n
0xd0000163 | Sending neighbor advertisement\r\n
0xd0000164 | Received neighbor advertisement\r\n
0xd0000165 | Sending router solicitation\r\n
0xd0000166 | Received router solicitation\r\n
0xd0000167 | Sending router advertisement\r\n
0xd0000168 | Received router advertisement\r\n
0xd0000169 | Receive\r\n
0xd000016a | ReceiveAndInvalidate\r\n
0xd000016b | Send\r\n
0xd000016c | FastRegister\r\n
0xd000016d | Bind\r\n
0xd000016e | Invalidate\r\n
0xd000016f | Read\r\n
0xd0000170 | Write\r\n
0xd0000171 | Not Activated\r\n
0xd0000172 | Activated\r\n
0xd0000173 | TCP connect\r\n
0xd0000174 | TCP send\r\n
0xd0000175 | UDP send\r\n
0xd0000176 | RAW send\r\n
0xd0000177 | Received Router Advertisement\r\n
0xd0000178 | AdminConfigured\r\n
0xd0000179 | NetworkProperty\r\n
0xd000017a | CreateWolContext\r\n
0xd000017b | DeleteWolContext\r\n
0xd000017c | SetWolContext\r\n
0xd000017d | ClearWolContext\r\n
0xd000017e | WolContextEvicted\r\n
0xd000017f | AddWolAddress\r\n
0xd0000180 | RemoveWolAddress\r\n
0xd0000181 | Send\r\n
0xd0000182 | Receive\r\n
0xd0000183 | WFP-ALE: RemoteEndPoint Address\r\n
0xd0000184 | WFP-ALE: RemoteEndPoint Port\r\n
0xd0000185 | WFP-ALE: LocalEndPoint Address\r\n
0xd0000186 | WFP-ALE: LocalEndPoint Port\r\n
0xd0000187 | WFP-ALE: Partition Id\r\n
0xd0000188 | WFP-ALE: Parition NumEnties\r\n
0xd0000189 | SlowDownEntry\r\n
0xd000018a | SlowDownExit\r\n
0xd000018b | SlowDownTracking\r\n
0xd000018c | BaseDelayUpdate\r\n
0xd000018d | Ack\r\n
0xd000018e | DupAck\r\n
0xd000018f | Timeout\r\n
0xd0000190 | Ecn\r\n
0xd0000191 | SpuriousTimeout\r\n
0xd0000192 | Network Context Constraint\r\n
0xd0000193 | Prefix Length Policy\r\n
0xd0000194 | Start Epoch Policy\r\n
0xd0000195 | Default Routes Disabled On Interface\r\n
0xd0000196 | Unconstrained Lookup Disallowed On Interface\r\n
0xd0000197 | Interface Disconnected\r\n
0xd0000198 | Route Invalid Lifetime\r\n
0xd0000199 | Interface Constraint\r\n
0xd000019a | Scope Constraint\r\n
0xd000019b | Unconstrained Offlink Route Lookup Disallowed On Interface\r\n
0xd000019c | Rechability\r\n
0xd000019d | Prefix Length\r\n
0xd000019e | Route And Interface Metrics\r\n
0xd000019f | Destination And Source Hash\r\n
0xd00001a0 | Route Order\r\n
0xd00001a1 | Dead Gateway\r\n
0xd00001a2 | OnLink Route\r\n
0xd00001a3 | Prefer Same Address\r\n
0xd00001a4 | Prefer Appropriate Scope\r\n
0xd00001a5 | Avoid Deprecated Addresses\r\n
0xd00001a6 | Prefer Home Addresses\r\n
0xd00001a7 | Prefer Outgoing Interface\r\n
0xd00001a8 | Prefer Addresses Associated With NextHop\r\n
0xd00001a9 | Prefer Matching Label\r\n
0xd00001aa | Prefer Temporary Addresses\r\n
0xd00001ab | System Defined Preference (Windows Specific)\r\n
0xd00001ac | Prefer Longest Matching Prefix With NextHop (Windows Specific)\r\n
0xd00001ad | Prefer Longest Matching Prefix\r\n
0xd00001ae | TimerArmed\r\n
0xd00001af | TimerFired\r\n
0xd00001b0 | Failed\r\n
0xd00001b1 | Init\r\n
0xd00001b2 | SetTimeSlotData\r\n
0xd00001b3 | SetTailTimeSlot\r\n
0xd00001b4 | EraseTimestamps\r\n
0xd00001b5 | GetRecoverySeq\r\n
0xd00001b6 | RttSampleUpdate\r\n
0xd00001b7 | TcpFastopenOff\r\n
0xd00001b8 | TcpFastopenAccepting\r\n
0xd00001b9 | TcpFastopenServerSendingCookie\r\n
0xd00001ba | TcpFastopenServerSentCookie\r\n
0xd00001bb | TcpFastopenNegotiate\r\n
0xd00001bc | TcpFastopenAttempt\r\n
0xd00001bd | TcpFastopenNegotiateSuccess\r\n
0xd00001be | TcpFastopenAttemptSuccess\r\n
0xd00001bf | TcpFastopenCookieRollover\r\n
0xd00001c0 | TcpFastopenFailed\r\n
0xd00001c1 | TcpFastopenFailedBlocklist\r\n
0xd00001c2 | TcpFastopenServerAcceptSuccess\r\n
0xd00001c3 | TcpFastopenServerAcceptTimeout\r\n
0xd00001c4 | TcpFastopenServerAcceptSendData\r\n
0xd00001c5 | TcpFastopenFailedSimultaneousConnect\r\n
0xd00001c6 | TcpFastopenFailedInvalidCookie\r\n
0xd00001c7 | TcpFastopenFailedSynTimeout\r\n
0xd00001c8 | TcpFastopenFailedTimeout\r\n
0xd00001c9 | TcpFastopenFailedReset\r\n
0xd00001ca | TcpFastopenFallback\r\n
0xd00001cb | TcpFastopenCookieRequestDeclined\r\n
0xd00001cc | TcpFastopenFailedSuddenRttIncrease\r\n
0xd00001cd | TcpFastopenFailedSynAckWithCookieRequest\r\n
0xd00001ce | TcpFastopenFailedNoNextHop\r\n
0xd00001cf | General failure\r\n
0xd00001d0 | Truncated header\r\n
0xd00001d1 | Invalid checksum\r\n
0xd00001d2 | Inspection drop\r\n
0xd00001d3 | Rejecting loopback neighbor discovery\r\n
0xd00001d4 | Unknown type/code\r\n
0xd00001d5 | Truncated IP header\r\n
0xd00001d6 | Oversized IP header\r\n
0xd00001d7 | No handler\r\n
0xd00001d8 | Not responding with error for error\r\n
0xd00001d9 | Invalid source\r\n
0xd00001da | Interface rate limit\r\n
0xd00001db | Path rate limit\r\n
0xd00001dc | No route\r\n
0xd00001dd | No matching request\r\n
0xd00001de | Buffer too small\r\n
0xd00001df | Failed to obtain ancillary data\r\n
0xd00001e0 | Incorrect hop limit\r\n
0xd00001e1 | Unknown code\r\n
0xd00001e2 | Source not linklocal\r\n
0xd00001e3 | Truncated ND header\r\n
0xd00001e4 | Invalid ND option SourceLinkAddr\r\n
0xd00001e5 | Invalid ND option MTU\r\n
0xd00001e6 | Invalid ND option PrefixInformation\r\n
0xd00001e7 | Invalid ND option RouteInformation\r\n
0xd00001e8 | Invalid ND option RDNSS\r\n
0xd00001e9 | Invalid ND option DNSSL\r\n
0xd00001ea | Packet parsing failure\r\n
0xd00001eb | Echo Reply\r\n
0xd00001ec | Destination Unreachable\r\n
0xd00001ed | Packet Too Big\r\n
0xd00001ee | Destination Unreachable(v4)/Time Exceeded(v6)\r\n
0xd00001ef | Source Quench(v4)/Parameter Problem(v6)\r\n
0xd00001f0 | Redirect\r\n
0xd00001f1 | Echo Request\r\n
0xd00001f2 | Router Advertisement\r\n
0xd00001f3 | Router Solicitation\r\n
0xd00001f4 | Time Exceeded\r\n
0xd00001f5 | Parameter Problem\r\n
0xd00001f6 | Timestamp Request\r\n
0xd00001f7 | Timestamp Reply\r\n
0xd00001f8 | Address Mask Request\r\n
0xd00001f9 | Address Mask Reply\r\n
0xd00001fa | Echo Request\r\n
0xd00001fb | Echo Reply\r\n
0xd00001fc | Multicast Listener Query\r\n
0xd00001fd | Multicast Listener Report\r\n
0xd00001fe | Multicast Listener Done\r\n
0xd00001ff | Router Solicitation\r\n
0xd0000200 | Router Advertisement\r\n
0xd0000201 | Neighbor Solicitation\r\n
0xd0000202 | Neighbor Advertisement\r\n
0xd0000203 | Redirect Message\r\n
0xd0000204 | Multicast Listener Discovery\r\n
0xd0000205 | Not Parsed\r\n
0xd0000206 | Periodic\r\n
0xd0000207 | Aperiodic\r\n
0xd0000208 | Unknown\r\n
0xd0000209 | Public\r\n
0xd000020a | Private\r\n
0xd000020b | Domain\r\n
0xd000020c | Remote\r\n
0xd000020d | Link\r\n
0xd000020e | NonDomainNetwork\r\n
0xd000020f | DomainNetwork\r\n
0xd0000210 | DomainAuthenticated\r\n
0xd0000211 | InterfaceAddition\r\n
0xd0000212 | InterfaceDeletion\r\n
0xd0000213 | ZoneChange\r\n
0xd0000214 | ConfigurationFlagChange\r\n
0xd0000215 | ForwardingEnable\r\n
0xd0000216 | ForwardingDisable\r\n
0xd0000217 | WeakHostReceiveEnable\r\n
0xd0000218 | WeakHostReceiveDisable\r\n
0xd0000219 | NetworkCategoryStateChange\r\n
0xd000021a | MetricChange\r\n
0xd000021b | MediaConnect\r\n
0xd000021c | MediaDisconnect\r\n
0xd000021d | OffloadCapabilityChange\r\n
0xd000021e | DisableDefaultRoutesSet\r\n
0xd000021f | DisableDefaultRoutesReset\r\n
0xd0000220 | ForceTunnelingSet\r\n
0xd0000221 | ForceTunnelingReset\r\n
0xd0000222 | LimitedLinkConnectivitySet\r\n
0xd0000223 | LimitedLinkConnectivityReset\r\n
0xd0000224 | LocalityConfigChange\r\n
0xd0000225 | RoutingFlagsSet\r\n
0xd0000226 | RoutingFlagsReset\r\n
0xd0000227 | PortStateChange\r\n
0xd0000228 | RscUnawareIpsnpiClientPresent\r\n
0xd0000229 | RscUnawareIpsnpiClientAbsent\r\n
0xd000022a | NoInternetConnectivity\r\n
0xd000022b | NoInternetDnsResolutionSucceeded\r\n
0xd000022c | InternetConnectivityDetected\r\n
0xd000022d | InternetConnectivityUnknown\r\n
0xd000022e | Timeout\r\n
0xd000022f | DadStarted\r\n
0xd0000230 | OptimisticDadStarted\r\n
0xd0000231 | DadPassed\r\n
0xd0000232 | NSReceived\r\n
0xd0000233 | NAReceived\r\n
0xd0000234 | InterfaceDisabled\r\n
0xd0000235 | DadDisabled\r\n
0xd0000236 | AddressAddition\r\n
0xd0000237 | AddressDeletion\r\n
0xd0000238 | DadStatePreferred\r\n
0xd0000239 | DadStateDuplicate\r\n
0xd000023a | DadStateDeprecated\r\n
0xd000023b | SkipAsSourceSet\r\n
0xd000023c | SkipAsSourceReset\r\n
0xd000023d | TunnelSkipAsSourceSet\r\n
0xd000023e | TunnelSkipAsSourceReset\r\n
0xd000023f | ZoneChange\r\n
0xd0000240 | NeighborAddition\r\n
0xd0000241 | NeighborDeletion\r\n
0xd0000242 | NeighborUnreachable\r\n
0xd0000243 | NeighborReachable\r\n
0xd0000244 | NeighborAddressUpdate\r\n
0xd0000245 | DeadRouteTimeout\r\n
0xd0000246 | DeadRouteProbeTimeout\r\n
0xd0000247 | AllRoutesDead\r\n
0xd0000248 | TlConfirmsForwardReachability\r\n
0xd0000249 | DeadGatewayDetected\r\n
0xd000024a | RouterRedirect\r\n
0xd000024b | ProbeConnectionFailed\r\n
0xd000024c | ConfigurationChange\r\n
0xd000024d | Alive\r\n
0xd000024e | Dead\r\n
0xd000024f | Probe\r\n
0xd0000250 | Disable\r\n
0xd0000251 | Enable\r\n
0xd0000252 | NotConfident\r\n
0xd0000253 | InvalidLoad\r\n
0xd0000254 | ConfidenceUpdate\r\n
0xd0000255 | TCP Fastopen\r\n
0xd0000256 | Init\r\n
0xd0000257 | StatusIndication\r\n
0xd0000258 | GlobalSetting\r\n
0xd0000259 | Forwarding\r\n
0xd000025a | IncompatibleCallout\r\n
0xd000025b | RA DNS information change\r\n
0xd000025c | RA DNS entry added\r\n
0xd000025d | RA DNS entry expired by RA\r\n
0xd000025e | RA DNS entry expired by timer\r\n
0xd000025f | RA DNS entry lifetime reset\r\n
0xd0000260 | RA DNS entry reordered\r\n
0xd0000261 | RA DNS entry deleted due to max limit\r\n
0xd0000262 | RA DNS entry lifetime updated\r\n
0xd0000263 | RA DNS ND entry ignored due to limit\r\n
0xd0000264 | RA DNS ND entry ignored due to memory failure\r\n
0xd0000265 | RA DNS ND entry ignored due to zero lifetime\r\n
0xd0000266 | RA DNS ND entries corrupted\r\n
0xd0000267 | RA DNS RouterContext init failed\r\n
0xd0000268 | Manual\r\n
0xd0000269 | WellKnown\r\n
0xd000026a | DHCP\r\n
0xd000026b | RouterAdvertisement\r\n
0xd000026c | 6to4\r\n
0xd000026d | Avoid Unusable Destination\r\n
0xd000026e | Prefer Aoac Interface\r\n
0xd000026f | Prefer Matching Scope\r\n
0xd0000270 | Avoid Deprecated Address\r\n
0xd0000271 | Prefer Matching Label\r\n
0xd0000272 | Prefer Internet Connected Interface\r\n
0xd0000273 | Prefer Higher Precedence\r\n
0xd0000274 | Prefer Longer Route Destination Prefix\r\n
0xd0000275 |  Prefer Native Transport(Physical Interface)\r\n
0xd0000276 | Prefer Lower Interface Metric\r\n
0xd0000277 | Prefer Smaller Scope\r\n
0xd0000278 | Prefer Same Address\r\n
0xd0000279 | Prefer Appropriate Scope\r\n
0xd000027a | Avoid Deprecated Address\r\n
0xd000027b | Prefer Outgoing Interface\r\n
0xd000027c | Prefer Source Address Associated With Nexthop\r\n
0xd000027d | Prefer Temporary Address\r\n
0xd000027e | System Defined Preference\r\n
0xd000027f | Prefer Source With Longer NextHop Prefix Match\r\n
0xd0000280 | Locality Metric\r\n
0xd0000281 | Prefer Longer Source/Destination Common Prefix Length\r\n
0xd0000282 | Order Unchanged (No Preference)\r\n
0xd0000283 | Send\r\n
0xd0000284 | Disconnect\r\n
0xd0000285 | Accept\r\n
0xd0000286 | Receive\r\n
0xd0000287 | ReceiveTcpDatagram\r\n
0xd0000288 | ReceiveDatagram\r\n
0xd0000289 | RemoteDisconnect\r\n
0xd000028a | ReceiveControlMessage\r\n
0xd000028b | RespondDatagram\r\n
0xd000028c | BindEndpoint\r\n
0xd000028d | Listen\r\n
0xd000028e | AcceptComplete\r\n
0xd000028f | Connect\r\n
0xd0000290 | ConnectComplete\r\n
0xd0000291 | Raw\r\n
0xd0000292 | ConnectRequest\r\n
0xd0000293 | CreateEndpoint\r\n
0xd0000294 | AcquirePort\r\n
0xd0000295 | Offload\r\n
0xd0000296 | SocketOption\r\n
0xd0000297 | BindEndpointRequest\r\n
0xd0000298 | Drop\r\n
0xd0000299 | Allow\r\n
0xd000029a | Pend\r\n
0xd000029b | DropAndSendIcmp\r\n
0xd000029c | Allow\r\n
0xd000029d | Deny\r\n
0xd000029e | Authorize\r\n
0xd000029f | RetryWithHint\r\n
0xd00002a0 | Reference\r\n
0xd00002a1 | Coalesced\r\n
0xd00002a2 | Dedicated\r\n
0xd00002a3 | FailureMemory\r\n
0xd00002a4 | FailurePlumbing\r\n
0xd00002a5 | NotFound\r\n
0xd00002a6 | Found\r\n
0xd00002a7 | Done\r\n
0xd00002a8 | Loopback Ethernet packet\r\n
0xd00002a9 | Invalid Snap header\r\n
0xd00002aa | Invalid ethernet type\r\n
0xd00002ab | Invalid packet length\r\n
0xd00002ac | Header not contiguous\r\n
0xd00002ad | Invalid destination type\r\n
0xd00002ae | Allocation failure\r\n
0xd00002af | Interface reference failure\r\n
0xd00002b0 | Packet provider reference failure\r\n
0xd00002b1 | Invalid LSO information\r\n

### 10.0.18362.1, 10.0.18362.836

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto = %3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm = %6, MaxDataRetransmissions = %7, DelayedAckTicks = %8 msec, DelayedAckFrequency = %9, RACK enabled = %10, Tail Loss Probe enabled = %11.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5, Event = %6.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick = %4 Time = %5.\r\n
0xb0000527 | %1 timer rescheduled by processor %2 for processor %3 at Tick = %4 to Tick = %5, OldScheduledExpiration = %6 NewScheduledExpiration = %7 DueTime = %8 Aperiodic = %9.\r\n
0xb0000528 | %1 timer fired on processor %2 at Tick = %3, was scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for Destination %4 in Compartment %5, Reason: %8 (Rule %6.%7).\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0000558 | Teredo Add -- PID: %1 started listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb0000559 | Teredo Remove -- PID: %1 stopped listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb000055a | IP: RouteLookup - API: %1 DstAddr: %3 ConstrainSrcAddr: %4 ConstrainIfIndex: %5 ConstraintOveridden: %6 ReturnConstrained: %7 OutgoingIfIndex: %8 NextHopAddr: %9 Status: %10\r\n
0xb000055b | IP: SourceAddrLookup - DstAddr: %2 ConstrainSrcAddr: %3 ConstrainIfIndex: %4 OutgoingIfIndex: %5 ReturnConstrained: %6 SelectedSrcAddr: %7\r\n
0xb000055c | WFP-ALE: Partition Count=%1 Partition Mask=%2: Partition Id=%d Partition NumEntries = %4.\r\n
0xb000055d | WFP-ALE: HotAdd/Remove: Old Partiton Count=%1 Old Partition Mask=%2 New Partiton Count=%1 New Partition Mask=%2.\r\n
0xb000055e | WFP-ALE: RemoteEndPoint Insertion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb000055f | WFP-ALE: RemoteEndPoint Deletion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb0000560 | WFP-ALE: ALE: low memory state detected. LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000561 | WFP-ALE: leaving low memory state. HighMemoryEvent = %1 HighNonPagedPoolEvent = %2.\r\n
0xb0000562 | WFP-ALE: Dpc for cleanup initiated: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000563 | WFP: Dpc for cleanup QUEUED or RE-QUEUED: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000564 | TCP: LEDBAT %2: Connection %1, BaseDelayMs = %6, CurrentDelayMs = %7, CWnd = %3, SsThresh = %4, SndWnd = %5, DelayBasedCwndFactor %9%%, RemainingTimeMs = %8.\r\n
0xb0000565 | TCP: AssociateNameResContext Endpoint: %1 Status: %16 NameResolutionContext: %2 DnsName: %3 InterfaceIndex: %4 IPAddrCount: %5 IPAddrs: %7 %9 %11 %13 %15\r\n
0xb0000566 | TCP: InspectConnectWithNameResContext Connection: %5 (local: %2 remote: %4) NameResolutionContext: %6 DnsName: %7 Status: %8.\r\n
0xb0000567 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 InterfaceMetric: %10 RouteMetric: %11] is preferred over Route [DestinationPrefix: %14/%12 NextHop: %16 InterfaceIndex: %17 InterfaceMetric: %18 RouteMetric: %19] for Destination: %3 in Compartment: %1, Reason: %20.\r\n
0xb0000568 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 RouteMetric: %10] is blocked for Destination: %3 ConstrainInterfaceIndex: %11 ConstrainScopeZone: %12 in Compartment: %1, Reason: %13.\r\n
0xb0000569 | TCP: Tail Loss Probe Send Connection = %1 SndUna = %2, SndMax = %3, SendAvailable = %4, TailProbeSeq = %5, TailProbeLast = %6, ControlsToSend = %7, ThFlags = %8.\r\n
0xb000056a | TCP: Tail Loss Probe Event Connection = %1, Event = %2.\r\n
0xb000056b | TCP: RACK Event Connection = %1, Event = %2, MinRTT = %3, ReoWind = %4, TimeSlotDeltaMin = %5, SeqNum = %6, Timestamp = %7, RttSample = %8.\r\n
0xb000056c | TCP: Fastopen state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000056d | UDP: endpoint (family=%5 pid=%3) create failed: address family not attached.\r\n
0xb000056e | UDP: endpoint %1 (family=%5 pid=%3) create failed: compartment %4 not found.\r\n
0xb000056f | UDP: endpoint %1 (family=%5 pid=%3) created.\r\n
0xb0000570 | UDP: endpoint %1 (family=%5 pid=%3) create failed: inspection status = %2\r\n
0xb0000571 | UDP: endpoint %4 bind failed: address %2 cannot be resolved, status = %3\r\n
0xb0000572 | UDP: endpoint %4 (sockaddr=%2) bind failed: port-acquisition status = %3\r\n
0xb0000573 | UDP: endpoint %4 (sockaddr=%2) bind failed: inspection status = %3\r\n
0xb0000574 | UDP: endpoint %4 (sockaddr=%2) bound.\r\n
0xb0000575 | UDP: endpoint %4 (sockaddr=%2) closed.\r\n
0xb0000576 | UDP: endpoint %4 closed.\r\n
0xb0000577 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address resolution status = %6\r\n
0xb0000578 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address validation failed.\r\n
0xb0000579 | UDP: endpoint %1 (sockaddr=%3) send messages %5: source-address selection status = %6\r\n
0xb000057b | UDP: address family %2added to interface %1.\r\n
0xb000057c | UDP: address family %2removed from interface %1.\r\n
0xb000057d | UDP: Failure initializing transport protocol, status = %1\r\n
0xb000057e | UDP: Failure starting NLNPI client, status = %1\r\n
0xb000057f | UDP: Failure initializing NSI support, status = %1\r\n
0xb0000580 | UDP: Failure starting TLNPI provider, status = %1\r\n
0xb0000581 | UDP: Failure initializing QoS support, status = %1\r\n
0xb0000582 | UDP: Failure starting %1, status = %2\r\n
0xb0000583 | UDP: endpoint %1 (sockaddr=%3) send messages %5: could not allocate send context.\r\n
0xb0000584 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path af failure, status = %6\r\n
0xb0000585 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path missing next hop failure.\r\n
0xb0000586 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path next hop address failure.\r\n
0xb0000587 | TCP: Early Retransmission, FACK or RACK, Connection = %1, SndUna = %2, SackIsLostSeq = %3, DupAckCount = %4\r\n
0xb0000588 | TCP: Ignoring fastopen SYN option due to limit on concurrent SYN_RCVD fastopen connections, Connection = %1, SynRcvdLimit = %2\r\n
0xb0000589 | TCP: Failed to update fastopen key state, Location = %1, Status = %2. Server-side fastopen will be disabled\r\n
0xb000058a | TCP: Fast Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058b | TCP: SACK Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058c | TCP: Limited Transmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058d | TCP: SACK Retransmit Additional Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058e | %1: %2message. Type = %3, Code = %4, CompartmentId = %5, SourceAddress = %7, DestAddress = %9\r\n
0xb000058f | %1: %2path drop. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11\r\n
0xb0000590 | %1: Echo timeout. Status = %4\r\n
0xb0000591 | %1 Timer state changed to %3 by Processor %2 Usage = %4 at Tick = %5\r\n
0xb0000592 | TCP: connection %1 send complete %3 bytes at %4 (%2).\r\n
0xb0000593 | IP: Compartment creation. Compartment = %1, Protocol = %2, Private = %3, Status = %4.\r\n
0xb0000594 | IP: Compartment deletion. Compartment = %1, Protocol = %2.\r\n
0xb0000595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13.\r\n
0xb0000596 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5 CwrMax = %6.\r\n
0xb0000597 | IP: Compartment cleanup. Compartment = %1, Protocol = %2.\r\n
0xb0000598 | IP: Interface network category state change. Interface = %1, Compartment = %2 , Protocol = %3, NetworkCategory = %4, DomainNetworkLocation = %5, DomainType = %6, Signature = %7.\r\n
0xb0000599 | IP: Interface creation. Interface = %1, Compartment = %2, Protocol = %3, PhysicalMediumType = %4, Status = %5.\r\n
0xb000059a | IP: Interface deletion. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059b | IP: Interface cleanup. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059c | IP: SubInterface creation. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4, Status = %5.\r\n
0xb000059d | IP: SubInterface deletion. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059e | IP: SubInterface cleanup. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059f | IP: Interface change Notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005a0 | IP: Interface internet connectivity status change. Interface = %1, Compartment = %2, Protocol = %3, OldConnectivityStatus = %4, NewConnectivityStatus = %5.\r\n
0xb00005a1 | IP: Address change notification. Address = %2, Interface = %3, Compartment = %4, Protocol = %5, Reason = %6.\r\n
0xb00005a2 | IP: Route change notification. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, NotifyFlags = %8.\r\n
0xb00005a3 | IP: Neighbor change notification. IpAddress = %2, DlAddress = %4, Interface = %5, Compartment = %6, State = %7, Reason = %8.\r\n
0xb00005a4 | IP: Address DAD state change. Address = %2, Interface = %3, Compartment = %4, OldState = %5, NewState = %6, Reason = %7.\r\n
0xb00005a5 | IP: Route Dead Gateway Detection state change. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, OldState = %8, NewState = %9, OldProbeCount = %10, NewProbeCount = %11, OldUnreachablePaths = %12, NewUnreachablePaths = %13, OldMovedPaths = %14, NewMovedPaths = %15, TotalPaths = %16, OldStateChangeTick = %17, NewStateChangeTick = %18, DgdNeedsReset = %19, Reason = %20.\r\n
0xb00005a6 | IP: Disconnecting TCP connections with Address = %2, Interface = %3, Compartment = %4, SkipLocal = %5, SkipOnLink = %6.\r\n
0xb00005a7 | TCP: connection %1: Sending paced chunk of %6 bytes with CWnd = %2, SndWnd = %3, BytesAvailable = %4, BytesOutstanding = %5\r\n
0xb00005a8 | Fallback: Context = %1, Feature = %2, TraceReason = %3, Confidence = %4, Successes = %5, Failures = %6\r\n
0xb00005a9 | TCPIP: TCB %1 using fast loopback\r\n
0xb00005aa | IP: Router information change notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005ab | IP: %1. Interface = %2, Compartment = %3, RouterAddress = %5, DNS Server/Suffix: %7 %8, Lifetime = %9.\r\n
0xb00005ac | IP: Route rundown. Interface = %1, Compartment = %2, Prefix = %4/%5, NextHop = %7, Metric = %8, State = %9, Origin = %10, Age = %11, ValidLifetime = %12, PreferredLifetime = %13, Flags = %14.\r\n
0xb00005ad | TCP: CUBIC ECN event. Connection %1, CWnd %2, SSThresh = %3, SndUna = %4\r\n
0xb00005ae | INETINSPECT: Owner = %1, InspectHandle = %2, InspectType = %3, Action = %4, Status = %5\r\n
0xb00005b0 | FallbackCheck: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b1 | FallbackUpdate: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b2 | Fallback: Permanently disabling feature, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b3 | Fallback: Enabling feature for this boot session, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b4 | Fallback: Feature previously disabled, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b5 | TCP Fastopen fallback update: Tcb = %1, FastopenState = %2, DataBytesIn = %3, ShutdownStatus = %4, ProbeStatus = %5\r\n
0xb00005b6 | Disabling feature until connectivity is established: CompartmentId =%1, IfIndex = %2, Feature = %3, ConnectivityStatus = %4\r\n
0xb00005b7 | Disabling %1 for loopback connection\r\n
0xb00005b8 | Disabling TCP Fastopen for BaseEndpoint = %1 because an incompatible WFP callout is installed\r\n
0xb00005b9 | IP: Setting source constraint for route lookup - Compartment: %1 DstAddr: %3 ConstrainSrcAddr: %5 ConstrainIfIndex: %6 ConstraintFlags: %7\r\n
0xb00005ba | WFP-ALE: RemoteEndPoint Insertion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bb | WFP-ALE: RemoteEndPoint Deletion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bc | TCP: connection %8 (local=%2 remote=%4) system abort. PID = %6.\r\n
0xb00005bd | Disabling %1 due to no next hop\r\n
0xb00005be | TCP: endpoint (sockaddr=%2) bind failed: wake status = %3.\r\n
0xb00005bf | UDP: endpoint %4 (sockaddr=%2) bind failed: wake status = %3\r\n
0xb00005c0 | Acquire wake port %2, type=%1, family=%3, IF=%4, compartment=%5\r\n
0xb00005c1 | TCP: Connection %1 reached max SACK queue length\r\n
0xb00005c2 | TCP: Connection %1 requested fast open\r\n
0xb00005c3 | TCP: CUBIC Hystart state change event. Connection %1, State %2, CWnd %3, SSThresh = %4.\r\n
0xb00005c4 | IP: Transmitting loopback Nbl %1. Interface=%2, Compartment=%3, Src=%6, Dst=%5, Proto=%7.\r\n
0xb00005c5 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26 ConnectionTimeMs %27 Timestamps %28 RttUs %29 MinRtt %30 MaxRtt %31 SynRetrans %32 CongestionAlgorithm %33 \   State %34 Local %36 Remote %38 CWnd %39 SsThresh %40 RcvWnd %41 RcvBuf %42 SndWnd %43.\r\n
0xb00005c6 | TCPIP: Framing layer %1 (AddressFamily=%2) dropped %4 packet(s) on interface=%3, Reason=%5, Data=%6.\r\n
0xb00005c7 | TCP: Connection %1 Transport (Protocol %2, AddressFamily = %3) sent RST with Local = %5, Remote = %7. Reason = %8.\r\n
0xb00005c8 | TCP connection failed with Status = %1, Local = %3, Remote = %5, ProcessId = %6, TcpState = %7 at %8:%9:%10 Reason = %11.\r\n
0xb00005c9 | TCP: Connection %1 PRR send SackIsLostSeq %2 SackInFlight %3 SackBytes %4 SackIsLost %5 SsThresh %6 RecoveryFS %7 AckedData %8 BytesInFlight %9 BytesToSend %10 PrrDelivered %11 PrrOut %12.\r\n
0xb00005ca | UDP: Endpoint %1 segment message. SegmentSize = %2 (0 == No Segmentation) MessageLength = %3 HwDatagrams = %4 HwSegments = %5 SwSegments = %6 Status = %7.\r\n
0xb00005cb | UDP: Endpoint %1 segmentation offload unavailable. Reason = %2 SegmentSize = %3 LocalAddress = %5, RemoteAddress = %7.\r\n
0xb00005cc | TCPIP: Framing layer interface %1 (AddressFamily = %2) failed to bind to its provider. Code = %3. Status = %4.\r\n
0xb00005cd | TCPIP: OID request from framing layer interface %1 (AddressFamily = %2) failed. OID = %3. Status = %4.\r\n
0xb00005ce | TCPIP received a status indication on interface %1. AddressFamily = %2. NdisStatus = %3.\r\n
0xb00005cf | IP: Failed to set socket option. Level = %1. Option = %2. Status = %3.\r\n
0xb00005d0 | IP: Failed to set socket IOCTL. IOCTL = %1. Status = %2.\r\n
0xb00005d1 | Failed to process multicast %1 request. Address = %2 %6. Source Address = %3 %7. Reason = %8. Status = %9.\r\n
0xb00005d2 | Processed multicast %1 request successfully. Address = %2 %6. Source Address = %3 %7.\r\n
0xb00005d3 | %1. Interface = %2. Address = %3 %5. Data = %6.\r\n
0xb00005d4 | %1. Interface = %2. Address = %3 %5. Data = %6. Status = %7.\r\n
0xb00005d5 | Invalid ECN codepoints in reassembly. Ce = %1. Ect0 = %2. Ect1 = %3. NotEct = %4.\r\n
0xb00005d6 | Reassembly failure: packets do not add up correctly.  Interface = %1. Address family = %2.\r\n
0xb00005d7 | Reassembly failure: failed to restore IPSec packet history.  Interface = %1. Address family = %2. Status = %3.\r\n
0xb00005d8 | Could not transfer %1.  Interface = %2. Address family = %3.\r\n
0xb00005d9 | Attempting to %1 the multicast group at FL.  Interface = %2. Address = %3 %5. Data = %6. Status = %7.\r\n
0xb00005da | Failed to update address list at FL. Interface = %1. Address Family = %2. Status = %3.\r\n
0xb00005db | Too many DAD failures, so will not create temporary address. Interface = %1. Address = %2 %4.\r\n
0xb00005dc | Failed to address interface; deleting it. Interface = %1. Status = %2.\r\n
0xb00005dd | Failed to reach default gateway after reconnect; cleaning settings.  Interface = %1.\r\n
0xb00005de | Failed to sync interface with registry.  Interface = %1. Field = %2. Status = %3.\r\n
0xb00005df | Failed to %1 an active reference on the interface.  Interface = %2. Reference Reason = %3. Status = %4.\r\n
0xb00005e0 | Redirect path hijack for destination %2 %3 from %5 %6. Interface = %1.\r\n
0xb00005e1 | Redirect path rate limit for IPv6 source address %3. Interface = %1.\r\n
0xb00005e2 | Dropped %2 fragment. Interface = %3. Reason = %1.\r\n
0xb00005e3 | Reassembly timeout. Interface = %1. Id = %2. Source Address = %3 %6.  Destination Address = %4 %7.\r\n
0xb00005e4 | Invalid IP option. Option = %3. Level = %2. Reason = %1.\r\n
0xb00005e5 | Invalid IP hop-by-hop option.  Option = %2. Reason = %1.\r\n
0xb00005e7 | Invalid IP routing header option. Reason = %1.\r\n
0xb00005e9 | This option cannot be specified by the user\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010452 | IP: Interface media disconnect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001045a | IP: Address DAD successful. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001045b | IP: Address DAD failed. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2, DL address of packet = %5.\r\n
0xb001045c | IP: Address DAD started. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010467 | IP: Address addition. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010468 | IP: Address deletion. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001046a | Framing: Interface operation status change. Interface = %1, Compartment = %4, Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0010470 | Framing: NDIS pause event. Interface = %1, Compartment = %3.\r\n
0xb0010471 | Framing: NDIS restart event. Interface = %1, Compartment = %3.\r\n
0xb0010478 | IP: Interface property change. Interface = %1, Compartment = %10, Protocol = %11, Advertise = %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7, WeakHostSend = %8, WeakHostReceive = %9.\r\n
0xb00104b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, Address = %4 %3 %6.\r\n
0xb00104b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7.\r\n
0xb0010529 | IP: Interface media connect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052a | IP: Interface limited link connectivity set. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052b | IP: Interface limited link connectivity reset. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052c | IP: Neighbor state change. IPAddress = %3, DLAddress = %5, Interface = %1, Compartment = %9, OldState = %6, NewState = %7, Event = %8.\r\n
0xb001052d | IP: Neighbor Discovery. Event = %5, Interface = %1, Compartment = %6, SourceIpAddress = %3, TargetIpAddress = %4.\r\n
0xb001052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions: %6, Reason: %10 (Rule %7 %8.%9).\r\n
0xb0010534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb001054e | IP: Interface configuration flags updated. Interface = %1, Compartment = %5, Protocol = %6, Property = %2, Value = %3, Event = %4.\r\n
0xb0010557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, UdpSegmentationOffloadInfo/TcpRecvSegCoalesceInfo %9, NrtNameResolutionId %10\r\n
0xb0010565 | TCP: AssociateNameResContext EndpointObj: %1 IsConnectionObj: %2 NameResContext: %3 Status: %4\r\n
0xb0010595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13 IsLimitedSlowStart = %14.\r\n
0xb00204b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, Address = %4 %3 %6.\r\n
0xb00204b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7, ReceiveLinkSpeed = %10 bps, MediaConnectState = %11.\r\n
0xb00304b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Metric = %11, Connected = %12, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, InternetConnectivityStatus = %13, Flags = %14, Address = %4 %3 %6.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | PacingTimer\r\n
0xd000002c | DisconnectTimer\r\n
0xd000002d | SwsTimer\r\n
0xd000002e | ReassemblyRateTimer\r\n
0xd000002f | SynOrRstValidationTimer\r\n
0xd0000030 | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000031 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000032 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000033 | TCP_KEEPALIVE\r\n
0xd0000034 | TCP_MAXSEG\r\n
0xd0000035 | TCP_MAXRT\r\n
0xd0000036 | TCP_STDURG\r\n
0xd0000037 | TCP_NOURG\r\n
0xd0000038 | TCP_ATMARK\r\n
0xd0000039 | TCP_NOSYNRETRIES\r\n
0xd000003a | TCP_TIMESTAMPS\r\n
0xd000003b | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003c | TCP_CONGESTION_ALGORITHM\r\n
0xd000003d | TCP_DELAY_FIN_ACK\r\n
0xd000003e | SO_DEBUG\r\n
0xd000003f | SO_ACCEPTCONN\r\n
0xd0000040 | SO_REUSEADDR\r\n
0xd0000041 | SO_KEEPALIVE\r\n
0xd0000042 | SO_DONTROUTE\r\n
0xd0000043 | SO_BROADCAST\r\n
0xd0000044 | SO_USELOOPBACK\r\n
0xd0000045 | SO_LINGER\r\n
0xd0000046 | SO_OOBINLINE\r\n
0xd0000047 | SO_SNDBUF\r\n
0xd0000048 | SO_RCVBUF\r\n
0xd0000049 | SO_CONDITIONAL_ACCEPT\r\n
0xd000004a | SO_PAUSE_ACCEPT\r\n
0xd000004b | SO_COMPARTMENT_ID\r\n
0xd000004c | SO_RANDOMIZE_PORT\r\n
0xd000004d | SO_PORT_SCALABILITY\r\n
0xd000004e | NldsInvalid\r\n
0xd000004f | NldsTentative\r\n
0xd0000050 | NldsDuplicate\r\n
0xd0000051 | NldsDeprecated\r\n
0xd0000052 | NldsPreferred\r\n
0xd0000053 | Indicate\r\n
0xd0000054 | Pend\r\n
0xd0000055 | Satisfy\r\n
0xd0000056 | NdisPhysicalMediumUnspecified\r\n
0xd0000057 | NdisPhysicalMediumWirelessLan\r\n
0xd0000058 | NdisPhysicalMediumCableModem\r\n
0xd0000059 | NdisPhysicalMediumPhoneLine\r\n
0xd000005a | NdisPhysicalMediumDSL\r\n
0xd000005b | NdisPhysicalMedium1394\r\n
0xd000005c | NdisPhysicalMediumWirelessWan\r\n
0xd000005d | NdisPhysicalMediumNative802_11\r\n
0xd000005e | NdisPhysicalMediumBluetooth\r\n
0xd000005f | NdisPhysicalMediumInfiniband\r\n
0xd0000060 | NdisPhysicalMediumWiMax\r\n
0xd0000061 | NdisPhysicalMedium802_3\r\n
0xd0000062 | NdisPhysicalMedium802_5\r\n
0xd0000063 | NdisPhysicalMediumIrda\r\n
0xd0000064 | NdisPhysicalMediumWiredWAN\r\n
0xd0000065 | IP checksum offload not computed\r\n
0xd0000066 | TCP checksum offload not computed\r\n
0xd0000067 | UDP checksum offload not computed\r\n
0xd0000068 | Header not aligned on 4-byte boundary\r\n
0xd0000069 | IP fragmentation\r\n
0xd000006a | Source address is not unicast\r\n
0xd000006b | Destination address is not unicast\r\n
0xd000006c | Ethernet and IP header not contiguous\r\n
0xd000006d | IP options present\r\n
0xd000006e | ESP over UDP\r\n
0xd000006f | Lack contiguous space for upper layer headers\r\n
0xd0000070 | WFP filters present\r\n
0xd0000071 | Nexthop is unavailable\r\n
0xd0000072 | Path has been invalidated due to policy change\r\n
0xd0000073 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000074 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000075 | Session state is not compatible\r\n
0xd0000076 | TCP options present\r\n
0xd0000077 | UDP IPv6 checksum absent in packet\r\n
0xd0000078 | Packet is for a loopback interface\r\n
0xd0000079 | Packet is from a Raw Socket\r\n
0xd000007a | TL Ancillary headers present\r\n
0xd000007b | NL Ancillary headers present\r\n
0xd000007c | Type of Service present\r\n
0xd000007d | IpSec headers present\r\n
0xd000007e | Interface is not Ethernet\r\n
0xd000007f | Nbl check failed\r\n
0xd0000080 | Destination address is unknown\r\n
0xd0000081 | Loopback inspect failed\r\n
0xd0000082 | Failed to allocate the WSD cache\r\n
0xd0000083 | Failure initializing PnP work queue\r\n
0xd0000084 | Failed to get persistent parameters\r\n
0xd0000085 | Rejected persistent parameters\r\n
0xd0000086 | qualified profile\r\n
0xd0000087 | qualified destination\r\n
0xd0000088 | sample collection completion\r\n
0xd0000089 | idle time expiration\r\n
0xd000008a | allocation\r\n
0xd000008b | new sample request\r\n
0xd000008c | configuration change\r\n
0xd000008d | Idle\r\n
0xd000008e | ProbingWs\r\n
0xd000008f | ProbeWait\r\n
0xd0000090 | ProbingWithoutWs\r\n
0xd0000091 | RecordWait\r\n
0xd0000092 | EreQualified\r\n
0xd0000093 | Qualified\r\n
0xd0000094 | Source Unspecified\r\n
0xd0000095 | Destination is multicast\r\n
0xd0000096 | Header is invalid (location 0)\r\n
0xd0000097 | Checksum is invalid\r\n
0xd0000098 | Transport endpoint was not found\r\n
0xd0000099 | Connected path error\r\n
0xd000009a | Session state error\r\n
0xd000009b | Receive Inspection\r\n
0xd000009c | ACK Invalid (subreason 0) (invalid ACK in SYN_SENT state)\r\n
0xd000009d | Expected SYN\r\n
0xd000009e | Received RST (subreason 0)\r\n
0xd000009f | Received SYN while in SYN_RCVD state\r\n
0xd00000a0 | Simultaneous Connect\r\n
0xd00000a1 | PAWS Failed\r\n
0xd00000a2 | Land Attack (subreason 0)\r\n
0xd00000a3 | Missed RST\r\n
0xd00000a4 | Outside Receive Window (subreason 0)\r\n
0xd00000a5 | Duplicate Segment\r\n
0xd00000a6 | Closed Window\r\n
0xd00000a7 | TCB Removed\r\n
0xd00000a8 | FIN-WAIT2\r\n
0xd00000a9 | Reassembly Conflict\r\n
0xd00000aa | FIN Received\r\n
0xd00000ab | Listener received segment with invalid flags\r\n
0xd00000ac | URG flag set but could not allocate urgent data state\r\n
0xd00000ad | TCB was not inserted in TCB table\r\n
0xd00000ae | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000af | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000b0 | Packet dropped by TIME-WAIT TCB (subreason 0)\r\n
0xd00000b1 | SYN+ACK with Fastopen cookie request\r\n
0xd00000b2 | Listener dropped SYN because SO_PAUSE_ACCEPT was set\r\n
0xd00000b3 | Listener dropped SYN to reduce memory pressure\r\n
0xd00000b4 | Bad source address\r\n
0xd00000b5 | Not locally destined\r\n
0xd00000b6 | Protocol unreachable\r\n
0xd00000b7 | Port unreachable\r\n
0xd00000b8 | Bad length\r\n
0xd00000b9 | Malformed Header\r\n
0xd00000ba | No route available\r\n
0xd00000bb | Beyond scope\r\n
0xd00000bc | Inspection drop\r\n
0xd00000bd | Too many decapsulations\r\n
0xd00000be | Administratively prohibited\r\n
0xd00000bf | Bad checksum\r\n
0xd00000c0 | Hop limit exceeded\r\n
0xd00000c1 | Address unreachable\r\n
0xd00000c2 | Fragment MTU exceeded\r\n
0xd00000c3 | Buffer Length Exceeded\r\n
0xd00000c4 | Address Resolution Timeout\r\n
0xd00000c5 | Address Resolution Failure\r\n
0xd00000c6 | IPsec failure\r\n
0xd00000c7 | Extension Headers Failure\r\n
0xd00000c8 | Allocation Failure\r\n
0xd00000c9 | IPSNPI Drop\r\n
0xd00000ca | Unsupported Offload\r\n
0xd00000cb | Routing Failure\r\n
0xd00000cc | Ancillary Data Failure\r\n
0xd00000cd | Raw Data Failure\r\n
0xd00000ce | Session State Failure\r\n
0xd00000cf | Default\r\n
0xd00000d0 | NewReno\r\n
0xd00000d1 | CTCP\r\n
0xd00000d2 | DCTCP\r\n
0xd00000d3 | LEDBAT\r\n
0xd00000d4 | CUBIC\r\n
0xd00000d5 | TcpTemplateTypeInternet\r\n
0xd00000d6 | TcpTemplateTypeDatacenter\r\n
0xd00000d7 | TcpTemplateTypeCompat\r\n
0xd00000d8 | TcpTemplateTypeDatacenterCustom\r\n
0xd00000d9 | TcpTemplateTypeInternetCustom\r\n
0xd00000da | TcpTemplateTypeDefault\r\n
0xd00000db | TcpTemplateTypeAutomatic\r\n
0xd00000dc | No Failure\r\n
0xd00000dd | Unknown\r\n
0xd00000de | System Policy\r\n
0xd00000df | NIC Capacity Reached\r\n
0xd00000e0 | System Low On Memory\r\n
0xd00000e1 | WFP driver / Stream inspection\r\n
0xd00000e2 | Weak Host Model Enabled\r\n
0xd00000e3 | Forwarding Enabled\r\n
0xd00000e4 | Hardware capability\r\n
0xd00000e5 | NDIS filter/NIC property\r\n
0xd00000e6 | Loopback fast path socket option not set on both ends\r\n
0xd00000e7 | Filter policy existed for the loopback connection\r\n
0xd00000e8 | IPv4\r\n
0xd00000e9 | IPv6\r\n
0xd00000ea | unbind\r\n
0xd00000eb | bind\r\n
0xd00000ec | port change\r\n
0xd00000ed | none\r\n
0xd00000ee | receive hash\r\n
0xd00000ef | receive scale\r\n
0xd00000f0 | enabled\r\n
0xd00000f1 | disabled\r\n
0xd00000f2 | removing\r\n
0xd00000f3 | adding\r\n
0xd00000f4 | complete binding initialization\r\n
0xd00000f5 | complete port initialization\r\n
0xd00000f6 | enumerate interface ports\r\n
0xd00000f7 | query port link state\r\n
0xd00000f8 | query port interface index\r\n
0xd00000f9 | query interface ports\r\n
0xd00000fa | query port RSS capabilities\r\n
0xd00000fb | get usable processors\r\n
0xd00000fc | query port driver version\r\n
0xd00000fd | query port RSS processor configuration\r\n
0xd00000fe | set receive scale parameters\r\n
0xd00000ff | set receive hash parameters\r\n
0xd0000100 | update interface ports\r\n
0xd0000101 | not available\r\n
0xd0000102 | available\r\n
0xd0000103 | available on ports\r\n
0xd0000104 | global configuration\r\n
0xd0000105 | active mode\r\n
0xd0000106 | Bind Adapter\r\n
0xd0000107 | Unbind Adapter (begin)\r\n
0xd0000108 | Unbind Adapter (end)\r\n
0xd0000109 | NetEvent Restart\r\n
0xd000010a | NetEvent Power-down\r\n
0xd000010b | NetEvent Power-up\r\n
0xd000010c | NetEvent NDK-enable\r\n
0xd000010d | NetEvent NDK-disable\r\n
0xd000010e | NetEvent NDK usage stopped\r\n
0xd000010f | Indicate new NDK interface arrival\r\n
0xd0000110 | Indicate NDK interface removal\r\n
0xd0000111 | Indicate NDK operational status change\r\n
0xd0000112 | Undefined\r\n
0xd0000113 | Adapter\r\n
0xd0000114 | QP\r\n
0xd0000115 | CQ\r\n
0xd0000116 | MR\r\n
0xd0000117 | MW\r\n
0xd0000118 | PD\r\n
0xd0000119 | SharedEndpoint\r\n
0xd000011a | Connector\r\n
0xd000011b | Listener\r\n
0xd000011c | SRQ\r\n
0xd000011d | Max\r\n
0xd000011e | Async\r\n
0xd000011f | Inline\r\n
0xd0000120 | Local\r\n
0xd0000121 | Remote\r\n
0xd0000122 | Privileged\r\n
0xd0000123 | Local\r\n
0xd0000124 | Remote\r\n
0xd0000125 | NotifyErrors\r\n
0xd0000126 | NotifyAny\r\n
0xd0000127 | NotifySolicited\r\n
0xd0000128 | Invalid\r\n
0xd0000129 | Software Slot allocated\r\n
0xd000012a | Hardware Slot allocated\r\n
0xd000012b | Policy error\r\n
0xd000012c | system error\r\n
0xd000012d | Enabled\r\n
0xd000012e | Send request dropped\r\n
0xd000012f | Receive dropped\r\n
0xd0000130 | Disconnect request dropped\r\n
0xd0000131 | Reset dropped\r\n
0xd0000132 | WFP API No Failure\r\n
0xd0000133 | WFP API WasRedirectedToProxy\r\n
0xd0000134 | WFP API RegisterForExitingEndpoint\r\n
0xd0000135 | WFP API ClassifiableFieldGetAf\r\n
0xd0000136 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000137 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd0000138 | WFP API ClassifiableFieldGetRemotePort\r\n
0xd0000139 | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd000013a | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd000013b | Processor Add\r\n
0xd000013c | Power Source Change\r\n
0xd000013d | AC\r\n
0xd000013e | DC\r\n
0xd000013f | DC Short Term\r\n
0xd0000140 | Unknown\r\n
0xd0000141 | is stopping timers\r\n
0xd0000142 | has stopped timers\r\n
0xd0000143 | is locking partitions\r\n
0xd0000144 | has locked partitions\r\n
0xd0000145 | is unlocking partitions\r\n
0xd0000146 | has unlocked partitions\r\n
0xd0000147 | is starting timers\r\n
0xd0000148 | has started timers\r\n
0xd0000149 | is starting\r\n
0xd000014a | is complete\r\n
0xd000014b | IP\r\n
0xd000014c | TCP\r\n
0xd000014d | leaving S0\r\n
0xd000014e | entering S0\r\n
0xd000014f | Unreachable\r\n
0xd0000150 | Incomplete\r\n
0xd0000151 | Probe\r\n
0xd0000152 | Delay\r\n
0xd0000153 | Stale\r\n
0xd0000154 | Reachable\r\n
0xd0000155 | Permanent\r\n
0xd0000156 | Maximum\r\n
0xd0000157 | Map\r\n
0xd0000158 | Configure\r\n
0xd0000159 | TlSuspectsReachability\r\n
0xd000015a | TlConfirmsReachability\r\n
0xd000015b | NaConfirmsReachability\r\n
0xd000015c | ProbeReachability\r\n
0xd000015d | DadSolicitation\r\n
0xd000015e | NewDlAddress\r\n
0xd000015f | TriggerNud\r\n
0xd0000160 | Resolve\r\n
0xd0000161 | Timeout\r\n
0xd0000162 | Sending neighbor solicitation\r\n
0xd0000163 | Received neighbor solicitation\r\n
0xd0000164 | Sending neighbor advertisement\r\n
0xd0000165 | Received neighbor advertisement\r\n
0xd0000166 | Sending router solicitation\r\n
0xd0000167 | Received router solicitation\r\n
0xd0000168 | Sending router advertisement\r\n
0xd0000169 | Received router advertisement\r\n
0xd000016a | Receive\r\n
0xd000016b | ReceiveAndInvalidate\r\n
0xd000016c | Send\r\n
0xd000016d | FastRegister\r\n
0xd000016e | Bind\r\n
0xd000016f | Invalidate\r\n
0xd0000170 | Read\r\n
0xd0000171 | Write\r\n
0xd0000172 | Not Activated\r\n
0xd0000173 | Activated\r\n
0xd0000174 | TCP connect\r\n
0xd0000175 | TCP send\r\n
0xd0000176 | UDP send\r\n
0xd0000177 | RAW send\r\n
0xd0000178 | Received Router Advertisement\r\n
0xd0000179 | AdminConfigured\r\n
0xd000017a | NetworkProperty\r\n
0xd000017b | CreateWolContext\r\n
0xd000017c | DeleteWolContext\r\n
0xd000017d | SetWolContext\r\n
0xd000017e | ClearWolContext\r\n
0xd000017f | WolContextEvicted\r\n
0xd0000180 | AddWolAddress\r\n
0xd0000181 | RemoveWolAddress\r\n
0xd0000182 | Send\r\n
0xd0000183 | Receive\r\n
0xd0000184 | WFP-ALE: RemoteEndPoint Address\r\n
0xd0000185 | WFP-ALE: RemoteEndPoint Port\r\n
0xd0000186 | WFP-ALE: LocalEndPoint Address\r\n
0xd0000187 | WFP-ALE: LocalEndPoint Port\r\n
0xd0000188 | WFP-ALE: Partition Id\r\n
0xd0000189 | WFP-ALE: Parition NumEnties\r\n
0xd000018a | SlowDownEntry\r\n
0xd000018b | SlowDownExit\r\n
0xd000018c | SlowDownTracking\r\n
0xd000018d | BaseDelayUpdate\r\n
0xd000018e | Ack\r\n
0xd000018f | DupAck\r\n
0xd0000190 | Timeout\r\n
0xd0000191 | Ecn\r\n
0xd0000192 | SpuriousTimeout\r\n
0xd0000193 | Network Context Constraint\r\n
0xd0000194 | Prefix Length Policy\r\n
0xd0000195 | Start Epoch Policy\r\n
0xd0000196 | Default Routes Disabled On Interface\r\n
0xd0000197 | Unconstrained Lookup Disallowed On Interface\r\n
0xd0000198 | Interface Disconnected\r\n
0xd0000199 | Route Invalid Lifetime\r\n
0xd000019a | Interface Constraint\r\n
0xd000019b | Scope Constraint\r\n
0xd000019c | Unconstrained Offlink Route Lookup Disallowed On Interface\r\n
0xd000019d | Rechability\r\n
0xd000019e | Prefix Length\r\n
0xd000019f | Route And Interface Metrics\r\n
0xd00001a0 | Destination And Source Hash\r\n
0xd00001a1 | Route Order\r\n
0xd00001a2 | Dead Gateway\r\n
0xd00001a3 | OnLink Route\r\n
0xd00001a4 | Prefer Same Address\r\n
0xd00001a5 | Prefer Appropriate Scope\r\n
0xd00001a6 | Avoid Deprecated Addresses\r\n
0xd00001a7 | Prefer Home Addresses\r\n
0xd00001a8 | Prefer Outgoing Interface\r\n
0xd00001a9 | Prefer Addresses Associated With NextHop\r\n
0xd00001aa | Prefer Matching Label\r\n
0xd00001ab | Prefer Temporary Addresses\r\n
0xd00001ac | System Defined Preference (Windows Specific)\r\n
0xd00001ad | Prefer Longest Matching Prefix With NextHop (Windows Specific)\r\n
0xd00001ae | Prefer Longest Matching Prefix\r\n
0xd00001af | TimerArmed\r\n
0xd00001b0 | TimerFired\r\n
0xd00001b1 | Failed\r\n
0xd00001b2 | Init\r\n
0xd00001b3 | SetTimeSlotData\r\n
0xd00001b4 | SetTailTimeSlot\r\n
0xd00001b5 | EraseTimestamps\r\n
0xd00001b6 | GetRecoverySeq\r\n
0xd00001b7 | RttSampleUpdate\r\n
0xd00001b8 | TcpFastopenOff\r\n
0xd00001b9 | TcpFastopenAccepting\r\n
0xd00001ba | TcpFastopenServerSendingCookie\r\n
0xd00001bb | TcpFastopenServerSentCookie\r\n
0xd00001bc | TcpFastopenNegotiate\r\n
0xd00001bd | TcpFastopenAttempt\r\n
0xd00001be | TcpFastopenNegotiateSuccess\r\n
0xd00001bf | TcpFastopenAttemptSuccess\r\n
0xd00001c0 | TcpFastopenCookieRollover\r\n
0xd00001c1 | TcpFastopenFailed\r\n
0xd00001c2 | TcpFastopenFailedBlocklist\r\n
0xd00001c3 | TcpFastopenServerAcceptSuccess\r\n
0xd00001c4 | TcpFastopenServerAcceptTimeout\r\n
0xd00001c5 | TcpFastopenServerAcceptSendData\r\n
0xd00001c6 | TcpFastopenFailedSimultaneousConnect\r\n
0xd00001c7 | TcpFastopenFailedInvalidCookie\r\n
0xd00001c8 | TcpFastopenFailedSynTimeout\r\n
0xd00001c9 | TcpFastopenFailedTimeout\r\n
0xd00001ca | TcpFastopenFailedReset\r\n
0xd00001cb | TcpFastopenFallback\r\n
0xd00001cc | TcpFastopenCookieRequestDeclined\r\n
0xd00001cd | TcpFastopenFailedSuddenRttIncrease\r\n
0xd00001ce | TcpFastopenFailedSynAckWithCookieRequest\r\n
0xd00001cf | TcpFastopenFailedNoNextHop\r\n
0xd00001d0 | General failure\r\n
0xd00001d1 | Truncated header\r\n
0xd00001d2 | Invalid checksum\r\n
0xd00001d3 | Inspection drop\r\n
0xd00001d4 | Rejecting loopback neighbor discovery\r\n
0xd00001d5 | Unknown type/code\r\n
0xd00001d6 | Truncated IP header\r\n
0xd00001d7 | Oversized IP header\r\n
0xd00001d8 | No handler\r\n
0xd00001d9 | Not responding with error for error\r\n
0xd00001da | Invalid source\r\n
0xd00001db | Interface rate limit\r\n
0xd00001dc | Path rate limit\r\n
0xd00001dd | No route\r\n
0xd00001de | No matching request\r\n
0xd00001df | Buffer too small\r\n
0xd00001e0 | Failed to obtain ancillary data\r\n
0xd00001e1 | Incorrect hop limit\r\n
0xd00001e2 | Unknown code\r\n
0xd00001e3 | Source not linklocal\r\n
0xd00001e4 | Truncated ND header\r\n
0xd00001e5 | Invalid ND option SourceLinkAddr\r\n
0xd00001e6 | Invalid ND option MTU\r\n
0xd00001e7 | Invalid ND option PrefixInformation\r\n
0xd00001e8 | Invalid ND option RouteInformation\r\n
0xd00001e9 | Invalid ND option RDNSS\r\n
0xd00001ea | Invalid ND option DNSSL\r\n
0xd00001eb | Packet parsing failure\r\n
0xd00001ec | Echo Reply\r\n
0xd00001ed | Destination Unreachable\r\n
0xd00001ee | Packet Too Big\r\n
0xd00001ef | Destination Unreachable(v4)/Time Exceeded(v6)\r\n
0xd00001f0 | Source Quench(v4)/Parameter Problem(v6)\r\n
0xd00001f1 | Redirect\r\n
0xd00001f2 | Echo Request\r\n
0xd00001f3 | Router Advertisement\r\n
0xd00001f4 | Router Solicitation\r\n
0xd00001f5 | Time Exceeded\r\n
0xd00001f6 | Parameter Problem\r\n
0xd00001f7 | Timestamp Request\r\n
0xd00001f8 | Timestamp Reply\r\n
0xd00001f9 | Address Mask Request\r\n
0xd00001fa | Address Mask Reply\r\n
0xd00001fb | Echo Request\r\n
0xd00001fc | Echo Reply\r\n
0xd00001fd | Multicast Listener Query\r\n
0xd00001fe | Multicast Listener Report\r\n
0xd00001ff | Multicast Listener Done\r\n
0xd0000200 | Router Solicitation\r\n
0xd0000201 | Router Advertisement\r\n
0xd0000202 | Neighbor Solicitation\r\n
0xd0000203 | Neighbor Advertisement\r\n
0xd0000204 | Redirect Message\r\n
0xd0000205 | Multicast Listener Discovery\r\n
0xd0000206 | Not Parsed\r\n
0xd0000207 | Periodic\r\n
0xd0000208 | Aperiodic\r\n
0xd0000209 | Unknown\r\n
0xd000020a | Public\r\n
0xd000020b | Private\r\n
0xd000020c | Domain\r\n
0xd000020d | Remote\r\n
0xd000020e | Link\r\n
0xd000020f | NonDomainNetwork\r\n
0xd0000210 | DomainNetwork\r\n
0xd0000211 | DomainAuthenticated\r\n
0xd0000212 | InterfaceAddition\r\n
0xd0000213 | InterfaceDeletion\r\n
0xd0000214 | ZoneChange\r\n
0xd0000215 | ConfigurationFlagChange\r\n
0xd0000216 | ForwardingEnable\r\n
0xd0000217 | ForwardingDisable\r\n
0xd0000218 | WeakHostReceiveEnable\r\n
0xd0000219 | WeakHostReceiveDisable\r\n
0xd000021a | NetworkCategoryStateChange\r\n
0xd000021b | MetricChange\r\n
0xd000021c | MediaConnect\r\n
0xd000021d | MediaDisconnect\r\n
0xd000021e | OffloadCapabilityChange\r\n
0xd000021f | DisableDefaultRoutesSet\r\n
0xd0000220 | DisableDefaultRoutesReset\r\n
0xd0000221 | ForceTunnelingSet\r\n
0xd0000222 | ForceTunnelingReset\r\n
0xd0000223 | LimitedLinkConnectivitySet\r\n
0xd0000224 | LimitedLinkConnectivityReset\r\n
0xd0000225 | LocalityConfigChange\r\n
0xd0000226 | RoutingFlagsSet\r\n
0xd0000227 | RoutingFlagsReset\r\n
0xd0000228 | PortStateChange\r\n
0xd0000229 | RscUnawareIpsnpiClientPresent\r\n
0xd000022a | RscUnawareIpsnpiClientAbsent\r\n
0xd000022b | NoInternetConnectivity\r\n
0xd000022c | NoInternetDnsResolutionSucceeded\r\n
0xd000022d | InternetConnectivityDetected\r\n
0xd000022e | InternetConnectivityUnknown\r\n
0xd000022f | Timeout\r\n
0xd0000230 | DadStarted\r\n
0xd0000231 | OptimisticDadStarted\r\n
0xd0000232 | DadPassed\r\n
0xd0000233 | NSReceived\r\n
0xd0000234 | NAReceived\r\n
0xd0000235 | InterfaceDisabled\r\n
0xd0000236 | DadDisabled\r\n
0xd0000237 | AddressAddition\r\n
0xd0000238 | AddressDeletion\r\n
0xd0000239 | DadStatePreferred\r\n
0xd000023a | DadStateDuplicate\r\n
0xd000023b | DadStateDeprecated\r\n
0xd000023c | SkipAsSourceSet\r\n
0xd000023d | SkipAsSourceReset\r\n
0xd000023e | TunnelSkipAsSourceSet\r\n
0xd000023f | TunnelSkipAsSourceReset\r\n
0xd0000240 | ZoneChange\r\n
0xd0000241 | NeighborAddition\r\n
0xd0000242 | NeighborDeletion\r\n
0xd0000243 | NeighborUnreachable\r\n
0xd0000244 | NeighborReachable\r\n
0xd0000245 | NeighborAddressUpdate\r\n
0xd0000246 | DeadRouteTimeout\r\n
0xd0000247 | DeadRouteProbeTimeout\r\n
0xd0000248 | AllRoutesDead\r\n
0xd0000249 | TlConfirmsForwardReachability\r\n
0xd000024a | DeadGatewayDetected\r\n
0xd000024b | RouterRedirect\r\n
0xd000024c | ProbeConnectionFailed\r\n
0xd000024d | ConfigurationChange\r\n
0xd000024e | Alive\r\n
0xd000024f | Dead\r\n
0xd0000250 | Probe\r\n
0xd0000251 | Disable\r\n
0xd0000252 | Enable\r\n
0xd0000253 | NotConfident\r\n
0xd0000254 | InvalidLoad\r\n
0xd0000255 | ConfidenceUpdate\r\n
0xd0000256 | TCP Fastopen\r\n
0xd0000257 | Init\r\n
0xd0000258 | StatusIndication\r\n
0xd0000259 | GlobalSetting\r\n
0xd000025a | Forwarding\r\n
0xd000025b | IncompatibleCallout\r\n
0xd000025c | RA DNS information change\r\n
0xd000025d | RA DNS entry added\r\n
0xd000025e | RA DNS entry expired by RA\r\n
0xd000025f | RA DNS entry expired by timer\r\n
0xd0000260 | RA DNS entry lifetime reset\r\n
0xd0000261 | RA DNS entry reordered\r\n
0xd0000262 | RA DNS entry deleted due to max limit\r\n
0xd0000263 | RA DNS entry lifetime updated\r\n
0xd0000264 | RA DNS ND entry ignored due to limit\r\n
0xd0000265 | RA DNS ND entry ignored due to memory failure\r\n
0xd0000266 | RA DNS ND entry ignored due to zero lifetime\r\n
0xd0000267 | RA DNS ND entries corrupted\r\n
0xd0000268 | RA DNS RouterContext init failed\r\n
0xd0000269 | Manual\r\n
0xd000026a | WellKnown\r\n
0xd000026b | DHCP\r\n
0xd000026c | RouterAdvertisement\r\n
0xd000026d | 6to4\r\n
0xd000026e | Avoid Unusable Destination\r\n
0xd000026f | Prefer Aoac Interface\r\n
0xd0000270 | Prefer Matching Scope\r\n
0xd0000271 | Avoid Deprecated Address\r\n
0xd0000272 | Prefer Matching Label\r\n
0xd0000273 | Prefer Internet Connected Interface\r\n
0xd0000274 | Prefer Higher Precedence\r\n
0xd0000275 | Prefer Longer Route Destination Prefix\r\n
0xd0000276 |  Prefer Native Transport(Physical Interface)\r\n
0xd0000277 | Prefer Lower Interface Metric\r\n
0xd0000278 | Prefer Smaller Scope\r\n
0xd0000279 | Prefer Same Address\r\n
0xd000027a | Prefer Appropriate Scope\r\n
0xd000027b | Avoid Deprecated Address\r\n
0xd000027c | Prefer Outgoing Interface\r\n
0xd000027d | Prefer Source Address Associated With Nexthop\r\n
0xd000027e | Prefer Temporary Address\r\n
0xd000027f | System Defined Preference\r\n
0xd0000280 | Prefer Source With Longer NextHop Prefix Match\r\n
0xd0000281 | Locality Metric\r\n
0xd0000282 | Prefer Longer Source/Destination Common Prefix Length\r\n
0xd0000283 | Order Unchanged (No Preference)\r\n
0xd0000284 | Send\r\n
0xd0000285 | Disconnect\r\n
0xd0000286 | Accept\r\n
0xd0000287 | Receive\r\n
0xd0000288 | ReceiveTcpDatagram\r\n
0xd0000289 | ReceiveDatagram\r\n
0xd000028a | RemoteDisconnect\r\n
0xd000028b | ReceiveControlMessage\r\n
0xd000028c | RespondDatagram\r\n
0xd000028d | BindEndpoint\r\n
0xd000028e | Listen\r\n
0xd000028f | AcceptComplete\r\n
0xd0000290 | Connect\r\n
0xd0000291 | ConnectComplete\r\n
0xd0000292 | Raw\r\n
0xd0000293 | ConnectRequest\r\n
0xd0000294 | CreateEndpoint\r\n
0xd0000295 | AcquirePort\r\n
0xd0000296 | Offload\r\n
0xd0000297 | SocketOption\r\n
0xd0000298 | BindEndpointRequest\r\n
0xd0000299 | Drop\r\n
0xd000029a | Allow\r\n
0xd000029b | Pend\r\n
0xd000029c | DropAndSendIcmp\r\n
0xd000029d | Allow\r\n
0xd000029e | Deny\r\n
0xd000029f | Authorize\r\n
0xd00002a0 | RetryWithHint\r\n
0xd00002a1 | Reference\r\n
0xd00002a2 | Coalesced\r\n
0xd00002a3 | Dedicated\r\n
0xd00002a4 | FailureMemory\r\n
0xd00002a5 | FailurePlumbing\r\n
0xd00002a6 | NotFound\r\n
0xd00002a7 | Found\r\n
0xd00002a8 | Done\r\n
0xd00002a9 | Loopback Ethernet packet\r\n
0xd00002aa | Invalid Snap header\r\n
0xd00002ab | Invalid ethernet type\r\n
0xd00002ac | Invalid packet length\r\n
0xd00002ad | Header not contiguous\r\n
0xd00002ae | Invalid destination type\r\n
0xd00002af | Allocation failure\r\n
0xd00002b0 | Interface reference failure\r\n
0xd00002b1 | Packet provider reference failure\r\n
0xd00002b2 | Invalid LSO information\r\n
0xd00002b3 | Receive discarded\r\n
0xd00002b4 | Listener received a packet other than SYN\r\n
0xd00002b5 | Listener was paused\r\n
0xd00002b6 | Listener inpsection rejected\r\n
0xd00002b7 | SYN was not acked in SynTcb receive\r\n
0xd00002b8 | Received invalid ACK\r\n
0xd00002b9 | Received SYN+ACK with TFO cookie request\r\n
0xd00002ba | Received in-window SYN in unexpected TCP state\r\n
0xd00002bb | Received invalid ACK in SynRcvd state\r\n
0xd00002bc | Received SYN and other flags in Timewait state\r\n
0xd00002bd | Connection aborted\r\n
0xd00002be | Bind endpoint was failed by InetInspect\r\n
0xd00002bf | Bind endpoint request was failed by InetInspect\r\n
0xd00002c0 | Listen was failed by InetInspect\r\n
0xd00002c1 | Listener receive was failed by InetInspect\r\n
0xd00002c2 | Accept complete was failed by InetInspect\r\n
0xd00002c3 | Create endpoint was failed by InetInspect\r\n
0xd00002c4 | Create connect endpoint was failed by InetInspect\r\n
0xd00002c5 | Create listen endpoint was failed by InetInspect\r\n
0xd00002c6 | Connect request was failed by InetInspect\r\n
0xd00002c7 | Connect request was failed by InetInspect\r\n
0xd00002c8 | Connect complete was failed by InetInspect\r\n
0xd00002c9 | Rate-limited connect complete was failed by InetInspect\r\n
0xd00002ca | Connection was cancelled\r\n
0xd00002cb | Connection aborted\r\n
0xd00002cc | Failed to send SYN packet\r\n
0xd00002cd | Failed to insert connection\r\n
0xd00002ce | Delivery aborted on connection-reset or timeout\r\n
0xd00002cf | An early disconnect injected\r\n
0xd00002d0 | Connection was aborted by the system\r\n
0xd00002d1 | Network name was deleted\r\n
0xd00002d2 | Incompatible next hop\r\n
0xd00002d3 | SegmentSize is larger than MTU\r\n
0xd00002d4 | Raw listeners on path\r\n
0xd00002d5 | IP extension headers present\r\n
0xd00002d6 | Exceeds hardware capabilities\r\n
0xd00002d7 | Incompatible inspection callout\r\n
0xd00002d8 | Unknown\r\n
0xd00002d9 | Connected\r\n
0xd00002da | Disconnected\r\n
0xd00002db | IPPROTO_IP\r\n
0xd00002dc | IPPROTO_IPV6\r\n
0xd00002dd | SOL_SOCKET\r\n
0xd00002de | IP_OPTIONS/IPV6_HOPOPTS\r\n
0xd00002df | IP_HDRINCL/IPV6_HDRINCL\r\n
0xd00002e0 | IP_TOS\r\n
0xd00002e1 | IP_TTL/IPV6_UNICAST_HOPS\r\n
0xd00002e2 | IP_MULTICAST_IF/IPV6_MULTICAST_IF\r\n
0xd00002e3 | IP_MULTICAST_TTL/IPV6_MULTICAST_HOPS\r\n
0xd00002e4 | IP_MULTICAST_LOOP/IPV6_MULTICAST_LOOP\r\n
0xd00002e5 | IP_ADD_MEMBERSHIP/IPV6_ADD_MEMBERSHIP\r\n
0xd00002e6 | IP_DROP_MEMBERSHIP/IPV6_DROP_MEMBERSHIP\r\n
0xd00002e7 | IP_DONTFRAGMENT/IPV6_DONTFRAG\r\n
0xd00002e8 | IP_ADD_SOURCE_MEMBERSHIP\r\n
0xd00002e9 | IP_DROP_SOURCE_MEMBERSHIP\r\n
0xd00002ea | IP_BLOCK_SOURCE\r\n
0xd00002eb | IP_UNBLOCK_SOURCE\r\n
0xd00002ec | IP_PKTINFO/IPV6_PKTINFO\r\n
0xd00002ed | IP_HOPLIMIT/IP_RECVTTL/IPV6_HOPLIMIT\r\n
0xd00002ee | IP_RECEIVE_BROADCAST\r\n
0xd00002ef | IPV6_PROTECTION_LEVEL\r\n
0xd00002f0 | IP_RECVIF/IPV6_RECVIF\r\n
0xd00002f1 | IP_RECVDSTADDR/IPV6_RECVDSTADDR\r\n
0xd00002f2 | IP_FLIST/IPV6_FLIST\r\n
0xd00002f3 | IP_ADD_IFLIST/IPV6_ADD_FLIST\r\n
0xd00002f4 | IP_DEL_IFLIST/IPV6_DEL_IFLIST\r\n
0xd00002f5 | IP_RTHDR/IPV6_RTHDR\r\n
0xd00002f6 | IP_UNICAST_IF/IPV6_UNICAST_IF\r\n
0xd00002f7 | IP_RECVRTHDR/IPV6_RECVRTHDR\r\n
0xd00002f8 | IP_RECVTCLASS/IP_RECVTOS/IPV6_RECVTCLASS\r\n
0xd00002f9 | MCAST_JOIN_GROUP\r\n
0xd00002fa | MCAST_LEAVE_GROUP\r\n
0xd00002fb | MCAST_BLOCK_SOURCE\r\n
0xd00002fc | MCAST_UNBLOCK_SOURCE\r\n
0xd00002fd | MCAST_JOIN_SOURCE_GROUP\r\n
0xd00002fe | MCAST_LEAVE_SOURCE_GROUP\r\n
0xd00002ff | IP_ORIGINAL_ARRIVAL_IF/IPV6_ORIGINAL_ARRIVAL_IF\r\n
0xd0000300 | IP_ECN/IPV6_ECN\r\n
0xd0000301 | IP_PKTINFO_EX/IPV6_PKTINFO_EX\r\n
0xd0000302 | IP_WFP_REDIRECT_RECORDS/IPV6_WFP_REDIRECT_RECORDS\r\n
0xd0000303 | IP_WFP_REDIRECT_CONTEXT/IPV6_WFP_REDIRECT_CONTEXT\r\n
0xd0000304 | IP_MTU_DISCOVER\r\n
0xd0000305 | IP_NRT_INTERFACE/IPV6_NRT_INTERFACE\r\n
0xd0000306 | IP_RECVERR/IPV6_RECVERR\r\n
0xd0000307 | SIO_GET_INTERFACE_LIST\r\n
0xd0000308 | SIO_GET_MULTICAST_FILTER\r\n
0xd0000309 | SIO_SET_MULTICAST_FILTER\r\n
0xd000030a | SIOCSMSFILTER\r\n
0xd000030b | SIOCGMSFILTER\r\n
0xd000030c | SIO_MULTIPOINT_LOOPBACK\r\n
0xd000030d | SIO_MULTICAST_SCOPE\r\n
0xd000030e | SIO_RCVALL\r\n
0xd000030f | SIO_RCVALL_MCAST\r\n
0xd0000310 | SIO_RCVALL_IGMPMCAST\r\n
0xd0000311 | SIO_RCVALL_MCAST_IF\r\n
0xd0000312 | SIO_RCVALL_IF\r\n
0xd0000313 | SIO_ADDRESS_LIST_SORT\r\n
0xd0000314 | join group\r\n
0xd0000315 | leave group\r\n
0xd0000316 | join group and add source\r\n
0xd0000317 | leave group and drop source\r\n
0xd0000318 | block source\r\n
0xd0000319 | unblock source\r\n
0xd000031a | set filter\r\n
0xd000031b | MLD level does not match protocol\r\n
0xd000031c | Invalid multicast address\r\n
0xd000031d | Invalid multicast source address\r\n
0xd000031e | Group already exists\r\n
0xd000031f | No existing state for group\r\n
0xd0000320 | Group is in exclude mode\r\n
0xd0000321 | No existing state for group or group is in exclude mode\r\n
0xd0000322 | No existing state for group or group is in include mode\r\n
0xd0000323 | Failed to set the state for the group\r\n
0xd0000324 | Failed to create the state for the group\r\n
0xd0000325 | Failed to modify the state for the group\r\n
0xd0000326 | Successfully created multicast session state\r\n
0xd0000327 | Another duplicate multicast session state exists, so no need to create a new one\r\n
0xd0000328 | Successfully added sources to multicast group\r\n
0xd0000329 | Successfully removed sources from multicast group\r\n
0xd000032a | Updated multicast group state; will send report\r\n
0xd000032b | Not modifying multicast group state\r\n
0xd000032c | Updated multicast discovery version\r\n
0xd000032d | Failed to create multicast session state when updating the multicast group\r\n
0xd000032e | Failed to create multicast session state from callback\r\n
0xd000032f | Failed to create multicast session state when searching for the interface\r\n
0xd0000330 | Failed to create multicast session state because access is denied\r\n
0xd0000331 | Failed to create multicast session state when adding sources to the session state\r\n
0xd0000332 | Failed to create multicast session state when creating the address\r\n
0xd0000333 | Failed to add sources to multicast group\r\n
0xd0000334 | Failed to modify multicast session state because access is denied\r\n
0xd0000335 | WFP context to the fragment\r\n
0xd0000336 | WFP context from the fragment to the reassembly context\r\n
0xd0000337 | leave\r\n
0xd0000338 | join\r\n
0xd0000339 | acquire\r\n
0xd000033a | release\r\n
0xd000033b | Unknown\r\n
0xd000033c | DAD\r\n
0xd000033d | Router solicitation\r\n
0xd000033e | WOL address pattern\r\n
0xd000033f | WOL TCP pattern\r\n
0xd0000340 | WOL local port pattern\r\n
0xd0000341 | Reassembly is prohibited\r\n
0xd0000342 | Fragment was filtered out\r\n
0xd0000343 | Out of memory\r\n
0xd0000344 | Protocol does not match\r\n
0xd0000345 | Fragment causes total packet length to exceed maximum payload size\r\n
0xd0000346 | Packet length does not properly align\r\n
0xd0000347 | The next header has the wrong IP option\r\n
0xd0000348 | Received mixed IPSec and non-IPSec fragments\r\n
0xd0000349 | Received zero length fragment\r\n
0xd000034a | Duplicate fragment\r\n
0xd000034b | Fragment falls beyond the data length\r\n
0xd000034c | Received duplicate or unsupported fragment\r\n
0xd000034d | End of list\r\n
0xd000034e | No operation\r\n
0xd000034f | Security\r\n
0xd0000350 | Loose source route\r\n
0xd0000351 | Timestamp\r\n
0xd0000352 | Record route\r\n
0xd0000353 | Struct source route\r\n
0xd0000354 | Stream ID\r\n
0xd0000355 | Router alert\r\n
0xd0000356 | Multi-destination\r\n
0xd0000357 | Single byte pad\r\n
0xd0000358 | Multiple byte pad\r\n
0xd0000359 | Tunnel limit\r\n
0xd000035a | Router alert\r\n
0xd000035b | Jumbogram\r\n
0xd000035c | NSAP address\r\n
0xd000035d | Message length is not long enough\r\n
0xd000035e | Data length must be greater than or equal to the size of the message header\r\n
0xd000035f | Invalid message type\r\n
0xd0000360 | Invalid message level\r\n
0xd0000361 | Invalid data length for this option\r\n
0xd0000362 | Invalid hop limit value\r\n
0xd0000363 | Invalid type of service value\r\n
0xd0000364 | Invalid hop-by-hop options\r\n
0xd0000365 | Invalid routing header\r\n
0xd0000366 | Invalid ECN field value\r\n
0xd0000367 | Invalid option\r\n
0xd0000368 | Option length is either too small or too large\r\n
0xd0000369 | Option length must be greater than or equal to the size of the option header\r\n
0xd000036a | The length of the supplied buffer is smaller than the option length\r\n
0xd000036b | The option length is smaller than the minimum length for this option\r\n
0xd000036c | The option list must have space for an integral, non-zero number of entries\r\n
0xd000036d | The data alignment of the option payload is invalid\r\n
0xd000036e | Invalid flags\r\n
0xd000036f | Multi-byte options can only occur once, or the combination of options is invalid\r\n
0xd0000370 | Invalid pointer value\r\n
0xd0000371 | Invalid address value\r\n
0xd0000372 | Invalid option\r\n
0xd0000373 | Option length is either too small or too large\r\n
0xd0000374 | Option length must be greater than or equal to the size of the option header\r\n
0xd0000375 | The length of the supplied buffer is smaller than the option length\r\n
0xd0000376 | The option list must have space for an integral, non-zero number of entries\r\n
0xd0000377 | Invalid address value\r\n
0xd0000378 | This option cannot be specified by the user\r\n
0xd0000379 | Message length is not long enough\r\n
0xd000037a | Data length must be greater than or equal to the size of the message header\r\n
0xd000037b | Invalid message level\r\n
0xd000037c | Invalid IP_PKTINFO_EX option length\r\n
0xd000037d | Invalid option length\r\n
0xd000037e | Interface not found\r\n
0xd000037f | Scope ID does not match the scope ID for the interface\r\n
0xd0000380 | Failed to find or create address to return\r\n

### 10.0.19041.84

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto = %3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm = %6, MaxDataRetransmissions = %7, DelayedAckTicks = %8 msec, DelayedAckFrequency = %9, RACK enabled = %10, Tail Loss Probe enabled = %11.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5, Event = %6.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick = %4 Time = %5.\r\n
0xb0000527 | %1 timer rescheduled by processor %2 for processor %3 at Tick = %4 to Tick = %5, OldScheduledExpiration = %6 NewScheduledExpiration = %7 DueTime = %8 Aperiodic = %9.\r\n
0xb0000528 | %1 timer fired on processor %2 at Tick = %3, was scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for Destination %4 in Compartment %5, Reason: %8 (Rule %6.%7).\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0000558 | Teredo Add -- PID: %1 started listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb0000559 | Teredo Remove -- PID: %1 stopped listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb000055a | IP: RouteLookup - API: %1 DstAddr: %3 ConstrainSrcAddr: %4 ConstrainIfIndex: %5 ConstraintOveridden: %6 ReturnConstrained: %7 OutgoingIfIndex: %8 NextHopAddr: %9 Status: %10\r\n
0xb000055b | IP: SourceAddrLookup - DstAddr: %2 ConstrainSrcAddr: %3 ConstrainIfIndex: %4 OutgoingIfIndex: %5 ReturnConstrained: %6 SelectedSrcAddr: %7\r\n
0xb000055c | WFP-ALE: Partition Count=%1 Partition Mask=%2: Partition Id=%d Partition NumEntries = %4.\r\n
0xb000055d | WFP-ALE: HotAdd/Remove: Old Partiton Count=%1 Old Partition Mask=%2 New Partiton Count=%1 New Partition Mask=%2.\r\n
0xb000055e | WFP-ALE: RemoteEndPoint Insertion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb000055f | WFP-ALE: RemoteEndPoint Deletion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb0000560 | WFP-ALE: ALE: low memory state detected. LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000561 | WFP-ALE: leaving low memory state. HighMemoryEvent = %1 HighNonPagedPoolEvent = %2.\r\n
0xb0000562 | WFP-ALE: Dpc for cleanup initiated: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000563 | WFP: Dpc for cleanup QUEUED or RE-QUEUED: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000564 | TCP: LEDBAT %2: Connection %1, BaseDelayMs = %6, CurrentDelayMs = %7, CWnd = %3, SsThresh = %4, SndWnd = %5, DelayBasedCwndFactor %9%%, RemainingTimeMs = %8.\r\n
0xb0000565 | TCP: AssociateNameResContext Endpoint: %1 Status: %16 NameResolutionContext: %2 DnsName: %3 InterfaceIndex: %4 IPAddrCount: %5 IPAddrs: %7 %9 %11 %13 %15\r\n
0xb0000566 | TCP: InspectConnectWithNameResContext Connection: %5 (local: %2 remote: %4) NameResolutionContext: %6 DnsName: %7 Status: %8.\r\n
0xb0000567 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 InterfaceMetric: %10 RouteMetric: %11] is preferred over Route [DestinationPrefix: %14/%12 NextHop: %16 InterfaceIndex: %17 InterfaceMetric: %18 RouteMetric: %19] for Destination: %3 in Compartment: %1, Reason: %20.\r\n
0xb0000568 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 RouteMetric: %10] is blocked for Destination: %3 ConstrainInterfaceIndex: %11 ConstrainScopeZone: %12 in Compartment: %1, Reason: %13.\r\n
0xb0000569 | TCP: Tail Loss Probe Send Connection = %1 SndUna = %2, SndMax = %3, SendAvailable = %4, TailProbeSeq = %5, TailProbeLast = %6, ControlsToSend = %7, ThFlags = %8.\r\n
0xb000056a | TCP: Tail Loss Probe Event Connection = %1, Event = %2.\r\n
0xb000056b | TCP: RACK Event Connection = %1, Event = %2, MinRTT = %3, ReoWind = %4, TimeSlotDeltaMin = %5, SeqNum = %6, Timestamp = %7, RttSample = %8.\r\n
0xb000056c | TCP: Fastopen state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000056d | UDP: endpoint (family=%5 pid=%3) create failed: address family not attached.\r\n
0xb000056e | UDP: endpoint %1 (family=%5 pid=%3) create failed: compartment %4 not found.\r\n
0xb000056f | UDP: endpoint %1 (family=%5 pid=%3) created.\r\n
0xb0000570 | UDP: endpoint %1 (family=%5 pid=%3) create failed: inspection status = %2\r\n
0xb0000571 | UDP: endpoint %4 bind failed: address %2 cannot be resolved, status = %3\r\n
0xb0000572 | UDP: endpoint %4 (sockaddr=%2) bind failed: port-acquisition status = %3\r\n
0xb0000573 | UDP: endpoint %4 (sockaddr=%2) bind failed: inspection status = %3\r\n
0xb0000574 | UDP: endpoint %4 (sockaddr=%2) bound.\r\n
0xb0000575 | UDP: endpoint %4 (sockaddr=%2) closed.\r\n
0xb0000576 | UDP: endpoint %4 closed.\r\n
0xb0000577 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address resolution status = %6\r\n
0xb0000578 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address validation failed.\r\n
0xb0000579 | UDP: endpoint %1 (sockaddr=%3) send messages %5: source-address selection status = %6\r\n
0xb000057b | UDP: address family %2added to interface %1.\r\n
0xb000057c | UDP: address family %2removed from interface %1.\r\n
0xb000057d | UDP: Failure initializing transport protocol, status = %1\r\n
0xb000057e | UDP: Failure starting NLNPI client, status = %1\r\n
0xb000057f | UDP: Failure initializing NSI support, status = %1\r\n
0xb0000580 | UDP: Failure starting TLNPI provider, status = %1\r\n
0xb0000581 | UDP: Failure initializing QoS support, status = %1\r\n
0xb0000582 | UDP: Failure starting %1, status = %2\r\n
0xb0000583 | UDP: endpoint %1 (sockaddr=%3) send messages %5: could not allocate send context.\r\n
0xb0000584 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path af failure, status = %6\r\n
0xb0000585 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path missing next hop failure.\r\n
0xb0000586 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path next hop address failure.\r\n
0xb0000587 | TCP: Early Retransmission, FACK or RACK, Connection = %1, SndUna = %2, SackIsLostSeq = %3, DupAckCount = %4\r\n
0xb0000588 | TCP: Ignoring fastopen SYN option due to limit on concurrent SYN_RCVD fastopen connections, Connection = %1, SynRcvdLimit = %2\r\n
0xb0000589 | TCP: Failed to update fastopen key state, Location = %1, Status = %2. Server-side fastopen will be disabled\r\n
0xb000058a | TCP: Fast Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058b | TCP: SACK Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058c | TCP: Limited Transmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058d | TCP: SACK Retransmit Additional Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058e | %1: %2message. Type = %3, Code = %4, CompartmentId = %5, SourceAddress = %7, DestAddress = %9\r\n
0xb000058f | %1: %2path drop. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11\r\n
0xb0000590 | %1: Echo timeout. Status = %4\r\n
0xb0000591 | %1 Timer state changed to %3 by Processor %2 Usage = %4 at Tick = %5\r\n
0xb0000592 | TCP: connection %1 send complete %3 bytes at %4 (%2).\r\n
0xb0000593 | IP: Compartment creation. Compartment = %1, Protocol = %2, Private = %3, Status = %4.\r\n
0xb0000594 | IP: Compartment deletion. Compartment = %1, Protocol = %2.\r\n
0xb0000595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13.\r\n
0xb0000596 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5 CwrMax = %6.\r\n
0xb0000597 | IP: Compartment cleanup. Compartment = %1, Protocol = %2.\r\n
0xb0000598 | IP: Interface network category state change. Interface = %1, Compartment = %2 , Protocol = %3, NetworkCategory = %4, DomainNetworkLocation = %5, DomainType = %6, Signature = %7.\r\n
0xb0000599 | IP: Interface creation. Interface = %1, Compartment = %2, Protocol = %3, PhysicalMediumType = %4, Status = %5.\r\n
0xb000059a | IP: Interface deletion. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059b | IP: Interface cleanup. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059c | IP: SubInterface creation. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4, Status = %5.\r\n
0xb000059d | IP: SubInterface deletion. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059e | IP: SubInterface cleanup. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059f | IP: Interface change Notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005a0 | IP: Interface internet connectivity status change. Interface = %1, Compartment = %2, Protocol = %3, OldConnectivityStatus = %4, NewConnectivityStatus = %5.\r\n
0xb00005a1 | IP: Address change notification. Address = %2, Interface = %3, Compartment = %4, Protocol = %5, Reason = %6.\r\n
0xb00005a2 | IP: Route change notification. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, NotifyFlags = %8.\r\n
0xb00005a3 | IP: Neighbor change notification. IpAddress = %2, DlAddress = %4, Interface = %5, Compartment = %6, State = %7, Reason = %8.\r\n
0xb00005a4 | IP: Address DAD state change. Address = %2, Interface = %3, Compartment = %4, OldState = %5, NewState = %6, Reason = %7.\r\n
0xb00005a5 | IP: Route Dead Gateway Detection state change. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, OldState = %8, NewState = %9, OldProbeCount = %10, NewProbeCount = %11, OldUnreachablePaths = %12, NewUnreachablePaths = %13, OldMovedPaths = %14, NewMovedPaths = %15, TotalPaths = %16, OldStateChangeTick = %17, NewStateChangeTick = %18, DgdNeedsReset = %19, Reason = %20.\r\n
0xb00005a6 | IP: Disconnecting TCP connections with Address = %2, Interface = %3, Compartment = %4, SkipLocal = %5, SkipOnLink = %6.\r\n
0xb00005a7 | TCP: connection %1: Sending paced chunk of %6 bytes with CWnd = %2, SndWnd = %3, BytesAvailable = %4, BytesOutstanding = %5\r\n
0xb00005a8 | Fallback: Context = %1, Feature = %2, TraceReason = %3, Confidence = %4, Successes = %5, Failures = %6\r\n
0xb00005a9 | TCPIP: TCB %1 using fast loopback\r\n
0xb00005aa | IP: Router information change notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005ab | IP: %1. Interface = %2, Compartment = %3, RouterAddress = %5, DNS Server/Suffix: %7 %8, Lifetime = %9.\r\n
0xb00005ac | IP: Route rundown. Interface = %1, Compartment = %2, Prefix = %4/%5, NextHop = %7, Metric = %8, State = %9, Origin = %10, Age = %11, ValidLifetime = %12, PreferredLifetime = %13, Flags = %14.\r\n
0xb00005ad | TCP: CUBIC ECN event. Connection %1, CWnd %2, SSThresh = %3, SndUna = %4\r\n
0xb00005ae | INETINSPECT: Owner = %1, InspectHandle = %2, InspectType = %3, Action = %4, Status = %5\r\n
0xb00005b0 | FallbackCheck: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b1 | FallbackUpdate: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b2 | Fallback: Permanently disabling feature, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b3 | Fallback: Enabling feature for this boot session, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b4 | Fallback: Feature previously disabled, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b5 | TCP Fastopen fallback update: Tcb = %1, FastopenState = %2, DataBytesIn = %3, ShutdownStatus = %4, ProbeStatus = %5\r\n
0xb00005b6 | Disabling feature until connectivity is established: CompartmentId =%1, IfIndex = %2, Feature = %3, ConnectivityStatus = %4\r\n
0xb00005b7 | Disabling %1 for loopback connection\r\n
0xb00005b8 | Disabling TCP Fastopen for BaseEndpoint = %1 because an incompatible WFP callout is installed\r\n
0xb00005b9 | IP: Setting source constraint for route lookup - Compartment: %1 DstAddr: %3 ConstrainSrcAddr: %5 ConstrainIfIndex: %6 ConstraintFlags: %7\r\n
0xb00005ba | WFP-ALE: RemoteEndPoint Insertion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bb | WFP-ALE: RemoteEndPoint Deletion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bc | TCP: connection %8 (local=%2 remote=%4) system abort. PID = %6.\r\n
0xb00005bd | Disabling %1 due to no next hop\r\n
0xb00005be | TCP: endpoint (sockaddr=%2) bind failed: wake status = %3.\r\n
0xb00005bf | UDP: endpoint %4 (sockaddr=%2) bind failed: wake status = %3\r\n
0xb00005c0 | Acquire wake port %2, type=%1, family=%3, IF=%4, compartment=%5\r\n
0xb00005c1 | TCP: Connection %1 reached max SACK queue length\r\n
0xb00005c2 | TCP: Connection %1 requested fast open\r\n
0xb00005c3 | TCP: CUBIC Hystart state change event. Connection %1, State %2, CWnd %3, SSThresh = %4.\r\n
0xb00005c4 | IP: Transmitting loopback Nbl %1. Interface=%2, Compartment=%3, Src=%6, Dst=%5, Proto=%7.\r\n
0xb00005c5 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26 ConnectionTimeMs %27 Timestamps %28 RttUs %29 MinRtt %30 MaxRtt %31 SynRetrans %32 CongestionAlgorithm %33 \   State %34 Local %36 Remote %38 CWnd %39 SsThresh %40 RcvWnd %41 RcvBuf %42 SndWnd %43.\r\n
0xb00005c6 | TCPIP: Framing layer %1 (AddressFamily=%2) dropped %4 packet(s) on interface=%3, Reason=%5, Data=%6.\r\n
0xb00005c7 | TCP: Connection %1 Transport (Protocol %2, AddressFamily = %3) sent RST with Local = %5, Remote = %7. Reason = %8.\r\n
0xb00005c8 | TCP connection failed with Status = %1, Local = %3, Remote = %5, ProcessId = %6, TcpState = %7 at %8:%9:%10 Reason = %11.\r\n
0xb00005c9 | TCP: Connection %1 PRR send SackIsLostSeq %2 SackInFlight %3 SackBytes %4 SackIsLost %5 SsThresh %6 RecoveryFS %7 AckedData %8 BytesInFlight %9 BytesToSend %10 PrrDelivered %11 PrrOut %12.\r\n
0xb00005ca | UDP: Endpoint %1 segment message. SegmentSize = %2 (0 == No Segmentation) MessageLength = %3 HwDatagrams = %4 HwSegments = %5 SwSegments = %6 Status = %7.\r\n
0xb00005cb | UDP: Endpoint %1 segmentation offload unavailable. Reason = %2 SegmentSize = %3 LocalAddress = %5, RemoteAddress = %7.\r\n
0xb00005cc | TCPIP: Framing layer interface %1 (AddressFamily = %2) failed to bind to its provider. Code = %3. Status = %4.\r\n
0xb00005cd | TCPIP: OID request from framing layer interface %1 (AddressFamily = %2) failed. OID = %3. Status = %4.\r\n
0xb00005ce | TCPIP received a status indication on interface %1. AddressFamily = %2. NdisStatus = %3.\r\n
0xb00005cf | IP: Failed to set socket option. Level = %1. Option = %2. Status = %3.\r\n
0xb00005d0 | IP: Failed to set socket IOCTL. IOCTL = %1. Status = %2.\r\n
0xb00005d1 | Failed to process multicast %1 request. Address = %2 %6. Source Address = %3 %7. Reason = %8. Status = %9.\r\n
0xb00005d2 | Processed multicast %1 request successfully. Address = %2 %6. Source Address = %3 %7.\r\n
0xb00005d3 | %1. Interface = %2. Address = %3 %5. Data = %6.\r\n
0xb00005d4 | %1. Interface = %2. Address = %3 %5. Data = %6. Status = %7.\r\n
0xb00005d5 | Invalid ECN codepoints in reassembly. Ce = %1. Ect0 = %2. Ect1 = %3. NotEct = %4.\r\n
0xb00005d6 | Reassembly failure: packets do not add up correctly.  Interface = %1. Address family = %2.\r\n
0xb00005d7 | Reassembly failure: failed to restore IPSec packet history.  Interface = %1. Address family = %2. Status = %3.\r\n
0xb00005d8 | Could not transfer %1.  Interface = %2. Address family = %3.\r\n
0xb00005d9 | Attempting to %1 the multicast group at FL.  Interface = %2. Address = %3 %5. Data = %6. Status = %7.\r\n
0xb00005da | Failed to update address list at FL. Interface = %1. Address Family = %2. Status = %3.\r\n
0xb00005db | Too many DAD failures, so will not create temporary address. Interface = %1. Address = %2 %4.\r\n
0xb00005dc | Failed to address interface; deleting it. Interface = %1. Status = %2.\r\n
0xb00005dd | Failed to reach default gateway after reconnect; cleaning settings.  Interface = %1.\r\n
0xb00005de | Failed to sync interface with registry.  Interface = %1. Field = %2. Status = %3.\r\n
0xb00005df | Failed to %1 an active reference on the interface.  Interface = %2. Reference Reason = %3. Status = %4.\r\n
0xb00005e0 | Redirect path hijack for destination %2 %3 from %5 %6. Interface = %1.\r\n
0xb00005e1 | Redirect path rate limit for IPv6 source address %3. Interface = %1.\r\n
0xb00005e2 | Dropped %2 fragment. Interface = %3. Reason = %1.\r\n
0xb00005e3 | Reassembly timeout. Interface = %1. Id = %2. Source Address = %3 %6.  Destination Address = %4 %7.\r\n
0xb00005e4 | Invalid IP option. Option = %3. Level = %2. Reason = %1.\r\n
0xb00005e5 | Invalid IP hop-by-hop option.  Option = %2. Reason = %1.\r\n
0xb00005e7 | Invalid IP routing header option. Reason = %1.\r\n
0xb00005e9 | This option cannot be specified by the user\r\n
0xb00005ea | TCP: interface %1: received potential RSC status indication. Current IPv4 State = %2, Offload IPv4 State = %3, Current IPv6 State = %4, Offload IPv6 State = %5.\r\n
0xb00005eb | UDP: endpoint %1: URO SCU received. SegCount = %2, SegSize = %3, DataLength = %4.\r\n
0xb00005ec | TCP software RSC global disabled mask = %1, UDP software URO global disabled mask = %2.\r\n
0xb00005ed | UDP: Global parameters updated for Address Family %1: DisableUro = %2.\r\n
0xb00005ee | IP: IPSNPI client rundown. %3 Interface = %1, Compartment = %2, Client = %4.\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010452 | IP: Interface media disconnect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001045a | IP: Address DAD successful. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001045b | IP: Address DAD failed. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2, DL address of packet = %5.\r\n
0xb001045c | IP: Address DAD started. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010467 | IP: Address addition. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010468 | IP: Address deletion. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001046a | Framing: Interface operation status change. Interface = %1, Compartment = %4, Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0010470 | Framing: NDIS pause event. Interface = %1, Compartment = %3.\r\n
0xb0010471 | Framing: NDIS restart event. Interface = %1, Compartment = %3.\r\n
0xb0010478 | IP: Interface property change. Interface = %1, Compartment = %10, Protocol = %11, Advertise = %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7, WeakHostSend = %8, WeakHostReceive = %9.\r\n
0xb00104b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, Address = %4 %3 %6.\r\n
0xb00104b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7.\r\n
0xb0010529 | IP: Interface media connect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052a | IP: Interface limited link connectivity set. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052b | IP: Interface limited link connectivity reset. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052c | IP: Neighbor state change. IPAddress = %3, DLAddress = %5, Interface = %1, Compartment = %9, OldState = %6, NewState = %7, Event = %8.\r\n
0xb001052d | IP: Neighbor Discovery. Event = %5, Interface = %1, Compartment = %6, SourceIpAddress = %3, TargetIpAddress = %4.\r\n
0xb001052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions: %6, Reason: %10 (Rule %7 %8.%9).\r\n
0xb0010534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb001054e | IP: Interface configuration flags updated. Interface = %1, Compartment = %5, Protocol = %6, Property = %2, Value = %3, Event = %4.\r\n
0xb0010557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, UdpSegmentationOffloadInfo/TcpRecvSegCoalesceInfo %9, NrtNameResolutionId/UdpRecvSegCoalesceOffloadInfo %10\r\n
0xb0010565 | TCP: AssociateNameResContext EndpointObj: %1 IsConnectionObj: %2 NameResContext: %3 Status: %4\r\n
0xb0010595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13 IsLimitedSlowStart = %14.\r\n
0xb00105ca | UDP: Endpoint %1 segment message. SegmentSize = %2 (0 == No Segmentation) MessageLength = %3 HwDatagrams = %4 HwSegments = %5 SwSegments = %6 SubMssSegments = %7 Status = %8.\r\n
0xb00204b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, Address = %4 %3 %6.\r\n
0xb00204b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7, ReceiveLinkSpeed = %10 bps, MediaConnectState = %11.\r\n
0xb00304b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Metric = %11, Connected = %12, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, InternetConnectivityStatus = %13, Flags = %14, Address = %4 %3 %6.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | PacingTimer\r\n
0xd000002c | DisconnectTimer\r\n
0xd000002d | SwsTimer\r\n
0xd000002e | ReassemblyRateTimer\r\n
0xd000002f | SynOrRstValidationTimer\r\n
0xd0000030 | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000031 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000032 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000033 | TCP_KEEPALIVE\r\n
0xd0000034 | TCP_MAXSEG\r\n
0xd0000035 | TCP_MAXRT\r\n
0xd0000036 | TCP_STDURG\r\n
0xd0000037 | TCP_NOURG\r\n
0xd0000038 | TCP_ATMARK\r\n
0xd0000039 | TCP_NOSYNRETRIES\r\n
0xd000003a | TCP_TIMESTAMPS\r\n
0xd000003b | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003c | TCP_CONGESTION_ALGORITHM\r\n
0xd000003d | TCP_DELAY_FIN_ACK\r\n
0xd000003e | SO_DEBUG\r\n
0xd000003f | SO_ACCEPTCONN\r\n
0xd0000040 | SO_REUSEADDR\r\n
0xd0000041 | SO_KEEPALIVE\r\n
0xd0000042 | SO_DONTROUTE\r\n
0xd0000043 | SO_BROADCAST\r\n
0xd0000044 | SO_USELOOPBACK\r\n
0xd0000045 | SO_LINGER\r\n
0xd0000046 | SO_OOBINLINE\r\n
0xd0000047 | SO_SNDBUF\r\n
0xd0000048 | SO_RCVBUF\r\n
0xd0000049 | SO_CONDITIONAL_ACCEPT\r\n
0xd000004a | SO_PAUSE_ACCEPT\r\n
0xd000004b | SO_COMPARTMENT_ID\r\n
0xd000004c | SO_RANDOMIZE_PORT\r\n
0xd000004d | SO_PORT_SCALABILITY\r\n
0xd000004e | NldsInvalid\r\n
0xd000004f | NldsTentative\r\n
0xd0000050 | NldsDuplicate\r\n
0xd0000051 | NldsDeprecated\r\n
0xd0000052 | NldsPreferred\r\n
0xd0000053 | Indicate\r\n
0xd0000054 | Pend\r\n
0xd0000055 | Satisfy\r\n
0xd0000056 | NdisPhysicalMediumUnspecified\r\n
0xd0000057 | NdisPhysicalMediumWirelessLan\r\n
0xd0000058 | NdisPhysicalMediumCableModem\r\n
0xd0000059 | NdisPhysicalMediumPhoneLine\r\n
0xd000005a | NdisPhysicalMediumDSL\r\n
0xd000005b | NdisPhysicalMedium1394\r\n
0xd000005c | NdisPhysicalMediumWirelessWan\r\n
0xd000005d | NdisPhysicalMediumNative802_11\r\n
0xd000005e | NdisPhysicalMediumBluetooth\r\n
0xd000005f | NdisPhysicalMediumInfiniband\r\n
0xd0000060 | NdisPhysicalMediumWiMax\r\n
0xd0000061 | NdisPhysicalMedium802_3\r\n
0xd0000062 | NdisPhysicalMedium802_5\r\n
0xd0000063 | NdisPhysicalMediumIrda\r\n
0xd0000064 | NdisPhysicalMediumWiredWAN\r\n
0xd0000065 | IP checksum offload not computed\r\n
0xd0000066 | TCP checksum offload not computed\r\n
0xd0000067 | UDP checksum offload not computed\r\n
0xd0000068 | Header not aligned on 4-byte boundary\r\n
0xd0000069 | IP fragmentation\r\n
0xd000006a | Source address is not unicast\r\n
0xd000006b | Destination address is neither TCP/UDP unicast nor UDP multicast\r\n
0xd000006c | Ethernet and IP header not contiguous\r\n
0xd000006d | IP options present\r\n
0xd000006e | ESP over UDP\r\n
0xd000006f | Lack contiguous space for upper layer headers\r\n
0xd0000070 | WFP filters present\r\n
0xd0000071 | Nexthop is unavailable\r\n
0xd0000072 | Path has been invalidated due to policy change\r\n
0xd0000073 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000074 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000075 | Session state is not compatible\r\n
0xd0000076 | TCP options present\r\n
0xd0000077 | UDP IPv6 checksum absent in packet\r\n
0xd0000078 | Packet is for a loopback interface\r\n
0xd0000079 | Packet is from a Raw Socket\r\n
0xd000007a | TL Ancillary headers present\r\n
0xd000007b | NL Ancillary headers present\r\n
0xd000007c | Type of Service present\r\n
0xd000007d | IpSec headers present\r\n
0xd000007e | Interface is not Ethernet\r\n
0xd000007f | Nbl check failed\r\n
0xd0000080 | Destination address is unknown\r\n
0xd0000081 | Loopback inspect failed\r\n
0xd0000082 | Next header is not a transport protocol eligible for the fast path\r\n
0xd0000083 | IP packet length is invalid\r\n
0xd0000084 | IP version is invalid\r\n
0xd0000085 | Failed to allocate the WSD cache\r\n
0xd0000086 | Failure initializing PnP work queue\r\n
0xd0000087 | Failed to get persistent parameters\r\n
0xd0000088 | Rejected persistent parameters\r\n
0xd0000089 | qualified profile\r\n
0xd000008a | qualified destination\r\n
0xd000008b | sample collection completion\r\n
0xd000008c | idle time expiration\r\n
0xd000008d | allocation\r\n
0xd000008e | new sample request\r\n
0xd000008f | configuration change\r\n
0xd0000090 | Idle\r\n
0xd0000091 | ProbingWs\r\n
0xd0000092 | ProbeWait\r\n
0xd0000093 | ProbingWithoutWs\r\n
0xd0000094 | RecordWait\r\n
0xd0000095 | EreQualified\r\n
0xd0000096 | Qualified\r\n
0xd0000097 | Source Unspecified\r\n
0xd0000098 | Destination is multicast\r\n
0xd0000099 | Header is invalid (location 0)\r\n
0xd000009a | Checksum is invalid\r\n
0xd000009b | Transport endpoint was not found\r\n
0xd000009c | Connected path error\r\n
0xd000009d | Session state error\r\n
0xd000009e | Receive Inspection\r\n
0xd000009f | ACK Invalid (subreason 0) (invalid ACK in SYN_SENT state)\r\n
0xd00000a0 | Expected SYN\r\n
0xd00000a1 | Received RST (subreason 0)\r\n
0xd00000a2 | Received SYN while in SYN_RCVD state\r\n
0xd00000a3 | Simultaneous Connect\r\n
0xd00000a4 | PAWS Failed\r\n
0xd00000a5 | Land Attack (subreason 0)\r\n
0xd00000a6 | Missed RST\r\n
0xd00000a7 | Outside Receive Window (subreason 0)\r\n
0xd00000a8 | Duplicate Segment\r\n
0xd00000a9 | Closed Window\r\n
0xd00000aa | TCB Removed\r\n
0xd00000ab | FIN-WAIT2\r\n
0xd00000ac | Reassembly Conflict\r\n
0xd00000ad | FIN Received\r\n
0xd00000ae | Listener received segment with invalid flags\r\n
0xd00000af | URG flag set but could not allocate urgent data state\r\n
0xd00000b0 | TCB was not inserted in TCB table\r\n
0xd00000b1 | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000b2 | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000b3 | Packet dropped by TIME-WAIT TCB (subreason 0)\r\n
0xd00000b4 | SYN+ACK with Fastopen cookie request\r\n
0xd00000b5 | Listener dropped SYN because SO_PAUSE_ACCEPT was set\r\n
0xd00000b6 | Listener dropped SYN to reduce memory pressure\r\n
0xd00000b7 | Bad source address\r\n
0xd00000b8 | Not locally destined\r\n
0xd00000b9 | Protocol unreachable\r\n
0xd00000ba | Port unreachable\r\n
0xd00000bb | Bad length\r\n
0xd00000bc | Malformed Header\r\n
0xd00000bd | No route available\r\n
0xd00000be | Beyond scope\r\n
0xd00000bf | Inspection drop\r\n
0xd00000c0 | Too many decapsulations\r\n
0xd00000c1 | Administratively prohibited\r\n
0xd00000c2 | Bad checksum\r\n
0xd00000c3 | Hop limit exceeded\r\n
0xd00000c4 | Address unreachable\r\n
0xd00000c5 | Fragment MTU exceeded\r\n
0xd00000c6 | Buffer Length Exceeded\r\n
0xd00000c7 | Address Resolution Timeout\r\n
0xd00000c8 | Address Resolution Failure\r\n
0xd00000c9 | IPsec failure\r\n
0xd00000ca | Extension Headers Failure\r\n
0xd00000cb | Allocation Failure\r\n
0xd00000cc | IPSNPI Client Drop\r\n
0xd00000cd | Unsupported Offload\r\n
0xd00000ce | Routing Failure\r\n
0xd00000cf | Ancillary Data Failure\r\n
0xd00000d0 | Raw Data Failure\r\n
0xd00000d1 | Session State Failure\r\n
0xd00000d2 | IPSNPI Allocation Failure\r\n
0xd00000d3 | IPSNPI Modified But Not Forwarded\r\n
0xd00000d4 | IPSNPI No Next Hop Specified\r\n
0xd00000d5 | IPSNPI Compartment Not Found\r\n
0xd00000d6 | IPSNPI Interface Not Found\r\n
0xd00000d7 | IPSNPI Subinterface Not Found\r\n
0xd00000d8 | IPSNPI Interface disabled\r\n
0xd00000d9 | IPSNPI Segmentation Failed\r\n
0xd00000da | IPSNPI No Ethernet Header\r\n
0xd00000db | IPSNPI Unexpected Fragment\r\n
0xd00000dc | IPSNPI Unsupported Interface Type\r\n
0xd00000dd | Default\r\n
0xd00000de | NewReno\r\n
0xd00000df | CTCP\r\n
0xd00000e0 | DCTCP\r\n
0xd00000e1 | LEDBAT\r\n
0xd00000e2 | CUBIC\r\n
0xd00000e3 | TcpTemplateTypeInternet\r\n
0xd00000e4 | TcpTemplateTypeDatacenter\r\n
0xd00000e5 | TcpTemplateTypeCompat\r\n
0xd00000e6 | TcpTemplateTypeDatacenterCustom\r\n
0xd00000e7 | TcpTemplateTypeInternetCustom\r\n
0xd00000e8 | TcpTemplateTypeDefault\r\n
0xd00000e9 | TcpTemplateTypeAutomatic\r\n
0xd00000ea | No Failure\r\n
0xd00000eb | Unknown\r\n
0xd00000ec | System Policy\r\n
0xd00000ed | NIC Capacity Reached\r\n
0xd00000ee | System Low On Memory\r\n
0xd00000ef | WFP driver / Stream inspection\r\n
0xd00000f0 | Weak Host Model Enabled\r\n
0xd00000f1 | Forwarding Enabled\r\n
0xd00000f2 | Hardware capability\r\n
0xd00000f3 | NDIS filter/NIC property\r\n
0xd00000f4 | Loopback fast path socket option not set on both ends\r\n
0xd00000f5 | Filter policy existed for the loopback connection\r\n
0xd00000f6 | IPv4\r\n
0xd00000f7 | IPv6\r\n
0xd00000f8 | unbind\r\n
0xd00000f9 | bind\r\n
0xd00000fa | port change\r\n
0xd00000fb | none\r\n
0xd00000fc | receive hash\r\n
0xd00000fd | receive scale\r\n
0xd00000fe | enabled\r\n
0xd00000ff | disabled\r\n
0xd0000100 | removing\r\n
0xd0000101 | adding\r\n
0xd0000102 | complete binding initialization\r\n
0xd0000103 | complete port initialization\r\n
0xd0000104 | enumerate interface ports\r\n
0xd0000105 | query port link state\r\n
0xd0000106 | query port interface index\r\n
0xd0000107 | query interface ports\r\n
0xd0000108 | query port RSS capabilities\r\n
0xd0000109 | get usable processors\r\n
0xd000010a | query port driver version\r\n
0xd000010b | query port RSS processor configuration\r\n
0xd000010c | set receive scale parameters\r\n
0xd000010d | set receive hash parameters\r\n
0xd000010e | update interface ports\r\n
0xd000010f | not available\r\n
0xd0000110 | available\r\n
0xd0000111 | available on ports\r\n
0xd0000112 | global configuration\r\n
0xd0000113 | active mode\r\n
0xd0000114 | Bind Adapter\r\n
0xd0000115 | Unbind Adapter (begin)\r\n
0xd0000116 | Unbind Adapter (end)\r\n
0xd0000117 | NetEvent Restart\r\n
0xd0000118 | NetEvent Power-down\r\n
0xd0000119 | NetEvent Power-up\r\n
0xd000011a | NetEvent NDK-enable\r\n
0xd000011b | NetEvent NDK-disable\r\n
0xd000011c | NetEvent NDK usage stopped\r\n
0xd000011d | Indicate new NDK interface arrival\r\n
0xd000011e | Indicate NDK interface removal\r\n
0xd000011f | Indicate NDK operational status change\r\n
0xd0000120 | Undefined\r\n
0xd0000121 | Adapter\r\n
0xd0000122 | QP\r\n
0xd0000123 | CQ\r\n
0xd0000124 | MR\r\n
0xd0000125 | MW\r\n
0xd0000126 | PD\r\n
0xd0000127 | SharedEndpoint\r\n
0xd0000128 | Connector\r\n
0xd0000129 | Listener\r\n
0xd000012a | SRQ\r\n
0xd000012b | Max\r\n
0xd000012c | Async\r\n
0xd000012d | Inline\r\n
0xd000012e | Local\r\n
0xd000012f | Remote\r\n
0xd0000130 | Privileged\r\n
0xd0000131 | Local\r\n
0xd0000132 | Remote\r\n
0xd0000133 | NotifyErrors\r\n
0xd0000134 | NotifyAny\r\n
0xd0000135 | NotifySolicited\r\n
0xd0000136 | Invalid\r\n
0xd0000137 | Software Slot allocated\r\n
0xd0000138 | Hardware Slot allocated\r\n
0xd0000139 | Policy error\r\n
0xd000013a | system error\r\n
0xd000013b | Enabled\r\n
0xd000013c | Send request dropped\r\n
0xd000013d | Receive dropped\r\n
0xd000013e | Disconnect request dropped\r\n
0xd000013f | Reset dropped\r\n
0xd0000140 | WFP API No Failure\r\n
0xd0000141 | WFP API WasRedirectedToProxy\r\n
0xd0000142 | WFP API RegisterForExitingEndpoint\r\n
0xd0000143 | WFP API ClassifiableFieldGetAf\r\n
0xd0000144 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000145 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd0000146 | WFP API ClassifiableFieldGetRemotePort\r\n
0xd0000147 | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd0000148 | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd0000149 | Processor Add\r\n
0xd000014a | Power Source Change\r\n
0xd000014b | AC\r\n
0xd000014c | DC\r\n
0xd000014d | DC Short Term\r\n
0xd000014e | Unknown\r\n
0xd000014f | is stopping timers\r\n
0xd0000150 | has stopped timers\r\n
0xd0000151 | is locking partitions\r\n
0xd0000152 | has locked partitions\r\n
0xd0000153 | is unlocking partitions\r\n
0xd0000154 | has unlocked partitions\r\n
0xd0000155 | is starting timers\r\n
0xd0000156 | has started timers\r\n
0xd0000157 | is starting\r\n
0xd0000158 | is complete\r\n
0xd0000159 | IP\r\n
0xd000015a | TCP\r\n
0xd000015b | leaving S0\r\n
0xd000015c | entering S0\r\n
0xd000015d | Unreachable\r\n
0xd000015e | Incomplete\r\n
0xd000015f | Probe\r\n
0xd0000160 | Delay\r\n
0xd0000161 | Stale\r\n
0xd0000162 | Reachable\r\n
0xd0000163 | Permanent\r\n
0xd0000164 | Maximum\r\n
0xd0000165 | Map\r\n
0xd0000166 | Configure\r\n
0xd0000167 | TlSuspectsReachability\r\n
0xd0000168 | TlConfirmsReachability\r\n
0xd0000169 | NaConfirmsReachability\r\n
0xd000016a | ProbeReachability\r\n
0xd000016b | DadSolicitation\r\n
0xd000016c | NewDlAddress\r\n
0xd000016d | TriggerNud\r\n
0xd000016e | Resolve\r\n
0xd000016f | Timeout\r\n
0xd0000170 | Sending neighbor solicitation\r\n
0xd0000171 | Received neighbor solicitation\r\n
0xd0000172 | Sending neighbor advertisement\r\n
0xd0000173 | Received neighbor advertisement\r\n
0xd0000174 | Sending router solicitation\r\n
0xd0000175 | Received router solicitation\r\n
0xd0000176 | Sending router advertisement\r\n
0xd0000177 | Received router advertisement\r\n
0xd0000178 | Receive\r\n
0xd0000179 | ReceiveAndInvalidate\r\n
0xd000017a | Send\r\n
0xd000017b | FastRegister\r\n
0xd000017c | Bind\r\n
0xd000017d | Invalidate\r\n
0xd000017e | Read\r\n
0xd000017f | Write\r\n
0xd0000180 | Not Activated\r\n
0xd0000181 | Activated\r\n
0xd0000182 | TCP connect\r\n
0xd0000183 | TCP send\r\n
0xd0000184 | UDP send\r\n
0xd0000185 | RAW send\r\n
0xd0000186 | Received Router Advertisement\r\n
0xd0000187 | AdminConfigured\r\n
0xd0000188 | NetworkProperty\r\n
0xd0000189 | CreateWolContext\r\n
0xd000018a | DeleteWolContext\r\n
0xd000018b | SetWolContext\r\n
0xd000018c | ClearWolContext\r\n
0xd000018d | WolContextEvicted\r\n
0xd000018e | AddWolAddress\r\n
0xd000018f | RemoveWolAddress\r\n
0xd0000190 | Send\r\n
0xd0000191 | Receive\r\n
0xd0000192 | WFP-ALE: RemoteEndPoint Address\r\n
0xd0000193 | WFP-ALE: RemoteEndPoint Port\r\n
0xd0000194 | WFP-ALE: LocalEndPoint Address\r\n
0xd0000195 | WFP-ALE: LocalEndPoint Port\r\n
0xd0000196 | WFP-ALE: Partition Id\r\n
0xd0000197 | WFP-ALE: Parition NumEnties\r\n
0xd0000198 | SlowDownEntry\r\n
0xd0000199 | SlowDownExit\r\n
0xd000019a | SlowDownTracking\r\n
0xd000019b | BaseDelayUpdate\r\n
0xd000019c | Ack\r\n
0xd000019d | DupAck\r\n
0xd000019e | Timeout\r\n
0xd000019f | Ecn\r\n
0xd00001a0 | SpuriousTimeout\r\n
0xd00001a1 | Network Context Constraint\r\n
0xd00001a2 | Prefix Length Policy\r\n
0xd00001a3 | Start Epoch Policy\r\n
0xd00001a4 | Default Routes Disabled On Interface\r\n
0xd00001a5 | Unconstrained Lookup Disallowed On Interface\r\n
0xd00001a6 | Interface Disconnected\r\n
0xd00001a7 | Route Invalid Lifetime\r\n
0xd00001a8 | Interface Constraint\r\n
0xd00001a9 | Scope Constraint\r\n
0xd00001aa | Unconstrained Offlink Route Lookup Disallowed On Interface\r\n
0xd00001ab | Rechability\r\n
0xd00001ac | Prefix Length\r\n
0xd00001ad | Route And Interface Metrics\r\n
0xd00001ae | Destination And Source Hash\r\n
0xd00001af | Route Order\r\n
0xd00001b0 | Dead Gateway\r\n
0xd00001b1 | OnLink Route\r\n
0xd00001b2 | Prefer Same Address\r\n
0xd00001b3 | Prefer Appropriate Scope\r\n
0xd00001b4 | Avoid Deprecated Addresses\r\n
0xd00001b5 | Prefer Home Addresses\r\n
0xd00001b6 | Prefer Outgoing Interface\r\n
0xd00001b7 | Prefer Addresses Associated With NextHop\r\n
0xd00001b8 | Prefer Matching Label\r\n
0xd00001b9 | Prefer Temporary Addresses\r\n
0xd00001ba | System Defined Preference (Windows Specific)\r\n
0xd00001bb | Prefer Longest Matching Prefix With NextHop (Windows Specific)\r\n
0xd00001bc | Prefer Longest Matching Prefix\r\n
0xd00001bd | TimerArmed\r\n
0xd00001be | TimerFired\r\n
0xd00001bf | Failed\r\n
0xd00001c0 | Init\r\n
0xd00001c1 | SetTimeSlotData\r\n
0xd00001c2 | SetTailTimeSlot\r\n
0xd00001c3 | EraseTimestamps\r\n
0xd00001c4 | GetRecoverySeq\r\n
0xd00001c5 | RttSampleUpdate\r\n
0xd00001c6 | TcpFastopenOff\r\n
0xd00001c7 | TcpFastopenAccepting\r\n
0xd00001c8 | TcpFastopenServerSendingCookie\r\n
0xd00001c9 | TcpFastopenServerSentCookie\r\n
0xd00001ca | TcpFastopenNegotiate\r\n
0xd00001cb | TcpFastopenAttempt\r\n
0xd00001cc | TcpFastopenNegotiateSuccess\r\n
0xd00001cd | TcpFastopenAttemptSuccess\r\n
0xd00001ce | TcpFastopenCookieRollover\r\n
0xd00001cf | TcpFastopenFailed\r\n
0xd00001d0 | TcpFastopenFailedBlocklist\r\n
0xd00001d1 | TcpFastopenServerAcceptSuccess\r\n
0xd00001d2 | TcpFastopenServerAcceptTimeout\r\n
0xd00001d3 | TcpFastopenServerAcceptSendData\r\n
0xd00001d4 | TcpFastopenFailedSimultaneousConnect\r\n
0xd00001d5 | TcpFastopenFailedInvalidCookie\r\n
0xd00001d6 | TcpFastopenFailedSynTimeout\r\n
0xd00001d7 | TcpFastopenFailedTimeout\r\n
0xd00001d8 | TcpFastopenFailedReset\r\n
0xd00001d9 | TcpFastopenFallback\r\n
0xd00001da | TcpFastopenCookieRequestDeclined\r\n
0xd00001db | TcpFastopenFailedSuddenRttIncrease\r\n
0xd00001dc | TcpFastopenFailedSynAckWithCookieRequest\r\n
0xd00001dd | TcpFastopenFailedNoNextHop\r\n
0xd00001de | General failure\r\n
0xd00001df | Truncated header\r\n
0xd00001e0 | Invalid checksum\r\n
0xd00001e1 | Inspection drop\r\n
0xd00001e2 | Rejecting loopback neighbor discovery\r\n
0xd00001e3 | Unknown type/code\r\n
0xd00001e4 | Truncated IP header\r\n
0xd00001e5 | Oversized IP header\r\n
0xd00001e6 | No handler\r\n
0xd00001e7 | Not responding with error for error\r\n
0xd00001e8 | Invalid source\r\n
0xd00001e9 | Interface rate limit\r\n
0xd00001ea | Path rate limit\r\n
0xd00001eb | No route\r\n
0xd00001ec | No matching request\r\n
0xd00001ed | Buffer too small\r\n
0xd00001ee | Failed to obtain ancillary data\r\n
0xd00001ef | Incorrect hop limit\r\n
0xd00001f0 | Unknown code\r\n
0xd00001f1 | Source not linklocal\r\n
0xd00001f2 | Truncated ND header\r\n
0xd00001f3 | Invalid ND option SourceLinkAddr\r\n
0xd00001f4 | Invalid ND option MTU\r\n
0xd00001f5 | Invalid ND option PrefixInformation\r\n
0xd00001f6 | Invalid ND option RouteInformation\r\n
0xd00001f7 | Invalid ND option RDNSS\r\n
0xd00001f8 | Invalid ND option DNSSL\r\n
0xd00001f9 | Packet parsing failure\r\n
0xd00001fa | Echo Reply\r\n
0xd00001fb | Destination Unreachable\r\n
0xd00001fc | Packet Too Big\r\n
0xd00001fd | Destination Unreachable(v4)/Time Exceeded(v6)\r\n
0xd00001fe | Source Quench(v4)/Parameter Problem(v6)\r\n
0xd00001ff | Redirect\r\n
0xd0000200 | Echo Request\r\n
0xd0000201 | Router Advertisement\r\n
0xd0000202 | Router Solicitation\r\n
0xd0000203 | Time Exceeded\r\n
0xd0000204 | Parameter Problem\r\n
0xd0000205 | Timestamp Request\r\n
0xd0000206 | Timestamp Reply\r\n
0xd0000207 | Address Mask Request\r\n
0xd0000208 | Address Mask Reply\r\n
0xd0000209 | Echo Request\r\n
0xd000020a | Echo Reply\r\n
0xd000020b | Multicast Listener Query\r\n
0xd000020c | Multicast Listener Report\r\n
0xd000020d | Multicast Listener Done\r\n
0xd000020e | Router Solicitation\r\n
0xd000020f | Router Advertisement\r\n
0xd0000210 | Neighbor Solicitation\r\n
0xd0000211 | Neighbor Advertisement\r\n
0xd0000212 | Redirect Message\r\n
0xd0000213 | Multicast Listener Discovery\r\n
0xd0000214 | Not Parsed\r\n
0xd0000215 | Periodic\r\n
0xd0000216 | Aperiodic\r\n
0xd0000217 | Unknown\r\n
0xd0000218 | Public\r\n
0xd0000219 | Private\r\n
0xd000021a | Domain\r\n
0xd000021b | Remote\r\n
0xd000021c | Link\r\n
0xd000021d | NonDomainNetwork\r\n
0xd000021e | DomainNetwork\r\n
0xd000021f | DomainAuthenticated\r\n
0xd0000220 | InterfaceAddition\r\n
0xd0000221 | InterfaceDeletion\r\n
0xd0000222 | ZoneChange\r\n
0xd0000223 | ConfigurationFlagChange\r\n
0xd0000224 | ForwardingEnable\r\n
0xd0000225 | ForwardingDisable\r\n
0xd0000226 | WeakHostReceiveEnable\r\n
0xd0000227 | WeakHostReceiveDisable\r\n
0xd0000228 | NetworkCategoryStateChange\r\n
0xd0000229 | MetricChange\r\n
0xd000022a | MediaConnect\r\n
0xd000022b | MediaDisconnect\r\n
0xd000022c | OffloadCapabilityChange\r\n
0xd000022d | DisableDefaultRoutesSet\r\n
0xd000022e | DisableDefaultRoutesReset\r\n
0xd000022f | ForceTunnelingSet\r\n
0xd0000230 | ForceTunnelingReset\r\n
0xd0000231 | LimitedLinkConnectivitySet\r\n
0xd0000232 | LimitedLinkConnectivityReset\r\n
0xd0000233 | LocalityConfigChange\r\n
0xd0000234 | RoutingFlagsSet\r\n
0xd0000235 | RoutingFlagsReset\r\n
0xd0000236 | PortStateChange\r\n
0xd0000237 | RscUnawareIpsnpiClientPresent\r\n
0xd0000238 | RscUnawareIpsnpiClientAbsent\r\n
0xd0000239 | PromiscuousModeEnabled\r\n
0xd000023a | PromiscuousModeDisabled\r\n
0xd000023b | NoInternetConnectivity\r\n
0xd000023c | NoInternetDnsResolutionSucceeded\r\n
0xd000023d | InternetConnectivityDetected\r\n
0xd000023e | InternetConnectivityUnknown\r\n
0xd000023f | Timeout\r\n
0xd0000240 | DadStarted\r\n
0xd0000241 | OptimisticDadStarted\r\n
0xd0000242 | DadPassed\r\n
0xd0000243 | NSReceived\r\n
0xd0000244 | NAReceived\r\n
0xd0000245 | InterfaceDisabled\r\n
0xd0000246 | DadDisabled\r\n
0xd0000247 | AddressAddition\r\n
0xd0000248 | AddressDeletion\r\n
0xd0000249 | DadStatePreferred\r\n
0xd000024a | DadStateDuplicate\r\n
0xd000024b | DadStateDeprecated\r\n
0xd000024c | SkipAsSourceSet\r\n
0xd000024d | SkipAsSourceReset\r\n
0xd000024e | TunnelSkipAsSourceSet\r\n
0xd000024f | TunnelSkipAsSourceReset\r\n
0xd0000250 | ZoneChange\r\n
0xd0000251 | NeighborAddition\r\n
0xd0000252 | NeighborDeletion\r\n
0xd0000253 | NeighborUnreachable\r\n
0xd0000254 | NeighborReachable\r\n
0xd0000255 | NeighborAddressUpdate\r\n
0xd0000256 | DeadRouteTimeout\r\n
0xd0000257 | DeadRouteProbeTimeout\r\n
0xd0000258 | AllRoutesDead\r\n
0xd0000259 | TlConfirmsForwardReachability\r\n
0xd000025a | DeadGatewayDetected\r\n
0xd000025b | RouterRedirect\r\n
0xd000025c | ProbeConnectionFailed\r\n
0xd000025d | ConfigurationChange\r\n
0xd000025e | Alive\r\n
0xd000025f | Dead\r\n
0xd0000260 | Probe\r\n
0xd0000261 | Disable\r\n
0xd0000262 | Enable\r\n
0xd0000263 | NotConfident\r\n
0xd0000264 | InvalidLoad\r\n
0xd0000265 | ConfidenceUpdate\r\n
0xd0000266 | TCP Fastopen\r\n
0xd0000267 | Init\r\n
0xd0000268 | StatusIndication\r\n
0xd0000269 | GlobalSetting\r\n
0xd000026a | Forwarding\r\n
0xd000026b | IncompatibleCallout\r\n
0xd000026c | RA DNS information change\r\n
0xd000026d | RA DNS entry added\r\n
0xd000026e | RA DNS entry expired by RA\r\n
0xd000026f | RA DNS entry expired by timer\r\n
0xd0000270 | RA DNS entry lifetime reset\r\n
0xd0000271 | RA DNS entry reordered\r\n
0xd0000272 | RA DNS entry deleted due to max limit\r\n
0xd0000273 | RA DNS entry lifetime updated\r\n
0xd0000274 | RA DNS ND entry ignored due to limit\r\n
0xd0000275 | RA DNS ND entry ignored due to memory failure\r\n
0xd0000276 | RA DNS ND entry ignored due to zero lifetime\r\n
0xd0000277 | RA DNS ND entries corrupted\r\n
0xd0000278 | RA DNS RouterContext init failed\r\n
0xd0000279 | Manual\r\n
0xd000027a | WellKnown\r\n
0xd000027b | DHCP\r\n
0xd000027c | RouterAdvertisement\r\n
0xd000027d | 6to4\r\n
0xd000027e | Avoid Unusable Destination\r\n
0xd000027f | Prefer Aoac Interface\r\n
0xd0000280 | Prefer Matching Scope\r\n
0xd0000281 | Avoid Deprecated Address\r\n
0xd0000282 | Prefer Matching Label\r\n
0xd0000283 | Prefer Internet Connected Interface\r\n
0xd0000284 | Prefer Higher Precedence\r\n
0xd0000285 | Prefer Longer Route Destination Prefix\r\n
0xd0000286 |  Prefer Native Transport(Physical Interface)\r\n
0xd0000287 | Prefer Lower Interface Metric\r\n
0xd0000288 | Prefer Smaller Scope\r\n
0xd0000289 | Prefer Same Address\r\n
0xd000028a | Prefer Appropriate Scope\r\n
0xd000028b | Avoid Deprecated Address\r\n
0xd000028c | Prefer Outgoing Interface\r\n
0xd000028d | Prefer Source Address Associated With Nexthop\r\n
0xd000028e | Prefer Temporary Address\r\n
0xd000028f | System Defined Preference\r\n
0xd0000290 | Prefer Source With Longer NextHop Prefix Match\r\n
0xd0000291 | Locality Metric\r\n
0xd0000292 | Prefer Longer Source/Destination Common Prefix Length\r\n
0xd0000293 | Order Unchanged (No Preference)\r\n
0xd0000294 | Send\r\n
0xd0000295 | Disconnect\r\n
0xd0000296 | Accept\r\n
0xd0000297 | Receive\r\n
0xd0000298 | ReceiveTcpDatagram\r\n
0xd0000299 | ReceiveDatagram\r\n
0xd000029a | RemoteDisconnect\r\n
0xd000029b | ReceiveControlMessage\r\n
0xd000029c | RespondDatagram\r\n
0xd000029d | BindEndpoint\r\n
0xd000029e | Listen\r\n
0xd000029f | AcceptComplete\r\n
0xd00002a0 | Connect\r\n
0xd00002a1 | ConnectComplete\r\n
0xd00002a2 | Raw\r\n
0xd00002a3 | ConnectRequest\r\n
0xd00002a4 | CreateEndpoint\r\n
0xd00002a5 | AcquirePort\r\n
0xd00002a6 | Offload\r\n
0xd00002a7 | SocketOption\r\n
0xd00002a8 | BindEndpointRequest\r\n
0xd00002a9 | Drop\r\n
0xd00002aa | Allow\r\n
0xd00002ab | Pend\r\n
0xd00002ac | DropAndSendIcmp\r\n
0xd00002ad | Allow\r\n
0xd00002ae | Deny\r\n
0xd00002af | Authorize\r\n
0xd00002b0 | RetryWithHint\r\n
0xd00002b1 | Reference\r\n
0xd00002b2 | Coalesced\r\n
0xd00002b3 | Dedicated\r\n
0xd00002b4 | FailureMemory\r\n
0xd00002b5 | FailurePlumbing\r\n
0xd00002b6 | NotFound\r\n
0xd00002b7 | Found\r\n
0xd00002b8 | Done\r\n
0xd00002b9 | Loopback Ethernet packet\r\n
0xd00002ba | Invalid Snap header\r\n
0xd00002bb | Invalid ethernet type\r\n
0xd00002bc | Invalid packet length\r\n
0xd00002bd | Header not contiguous\r\n
0xd00002be | Invalid destination type\r\n
0xd00002bf | Allocation failure\r\n
0xd00002c0 | Interface reference failure\r\n
0xd00002c1 | Packet provider reference failure\r\n
0xd00002c2 | Invalid LSO information\r\n
0xd00002c3 | Receive discarded\r\n
0xd00002c4 | Listener received a packet other than SYN\r\n
0xd00002c5 | Listener was paused\r\n
0xd00002c6 | Listener inpsection rejected\r\n
0xd00002c7 | SYN was not acked in SynTcb receive\r\n
0xd00002c8 | Received invalid ACK\r\n
0xd00002c9 | Received SYN+ACK with TFO cookie request\r\n
0xd00002ca | Received in-window SYN in unexpected TCP state\r\n
0xd00002cb | Received invalid ACK in SynRcvd state\r\n
0xd00002cc | Received SYN and other flags in Timewait state\r\n
0xd00002cd | Connection aborted\r\n
0xd00002ce | Bind endpoint was failed by InetInspect\r\n
0xd00002cf | Bind endpoint request was failed by InetInspect\r\n
0xd00002d0 | Listen was failed by InetInspect\r\n
0xd00002d1 | Listener receive was failed by InetInspect\r\n
0xd00002d2 | Accept complete was failed by InetInspect\r\n
0xd00002d3 | Create endpoint was failed by InetInspect\r\n
0xd00002d4 | Create connect endpoint was failed by InetInspect\r\n
0xd00002d5 | Create listen endpoint was failed by InetInspect\r\n
0xd00002d6 | Connect request was failed by InetInspect\r\n
0xd00002d7 | Connect request was failed by InetInspect\r\n
0xd00002d8 | Connect complete was failed by InetInspect\r\n
0xd00002d9 | Rate-limited connect complete was failed by InetInspect\r\n
0xd00002da | Connection was cancelled\r\n
0xd00002db | Connection aborted\r\n
0xd00002dc | Failed to send SYN packet\r\n
0xd00002dd | Failed to insert connection\r\n
0xd00002de | Delivery aborted on connection-reset or timeout\r\n
0xd00002df | An early disconnect injected\r\n
0xd00002e0 | Connection was aborted by the system\r\n
0xd00002e1 | Network name was deleted\r\n
0xd00002e2 | Incompatible next hop\r\n
0xd00002e3 | SegmentSize is larger than MTU\r\n
0xd00002e4 | Raw listeners on path\r\n
0xd00002e5 | IP extension headers present\r\n
0xd00002e6 | Exceeds hardware capabilities\r\n
0xd00002e7 | Incompatible inspection callout\r\n
0xd00002e8 | Unknown\r\n
0xd00002e9 | Connected\r\n
0xd00002ea | Disconnected\r\n
0xd00002eb | IPPROTO_IP\r\n
0xd00002ec | IPPROTO_IPV6\r\n
0xd00002ed | SOL_SOCKET\r\n
0xd00002ee | IP_OPTIONS/IPV6_HOPOPTS\r\n
0xd00002ef | IP_HDRINCL/IPV6_HDRINCL\r\n
0xd00002f0 | IP_TOS\r\n
0xd00002f1 | IP_TTL/IPV6_UNICAST_HOPS\r\n
0xd00002f2 | IP_MULTICAST_IF/IPV6_MULTICAST_IF\r\n
0xd00002f3 | IP_MULTICAST_TTL/IPV6_MULTICAST_HOPS\r\n
0xd00002f4 | IP_MULTICAST_LOOP/IPV6_MULTICAST_LOOP\r\n
0xd00002f5 | IP_ADD_MEMBERSHIP/IPV6_ADD_MEMBERSHIP\r\n
0xd00002f6 | IP_DROP_MEMBERSHIP/IPV6_DROP_MEMBERSHIP\r\n
0xd00002f7 | IP_DONTFRAGMENT/IPV6_DONTFRAG\r\n
0xd00002f8 | IP_ADD_SOURCE_MEMBERSHIP\r\n
0xd00002f9 | IP_DROP_SOURCE_MEMBERSHIP\r\n
0xd00002fa | IP_BLOCK_SOURCE\r\n
0xd00002fb | IP_UNBLOCK_SOURCE\r\n
0xd00002fc | IP_PKTINFO/IPV6_PKTINFO\r\n
0xd00002fd | IP_HOPLIMIT/IP_RECVTTL/IPV6_HOPLIMIT\r\n
0xd00002fe | IP_RECEIVE_BROADCAST\r\n
0xd00002ff | IPV6_PROTECTION_LEVEL\r\n
0xd0000300 | IP_RECVIF/IPV6_RECVIF\r\n
0xd0000301 | IP_RECVDSTADDR/IPV6_RECVDSTADDR\r\n
0xd0000302 | IP_FLIST/IPV6_FLIST\r\n
0xd0000303 | IP_ADD_IFLIST/IPV6_ADD_FLIST\r\n
0xd0000304 | IP_DEL_IFLIST/IPV6_DEL_IFLIST\r\n
0xd0000305 | IP_RTHDR/IPV6_RTHDR\r\n
0xd0000306 | IP_UNICAST_IF/IPV6_UNICAST_IF\r\n
0xd0000307 | IP_RECVRTHDR/IPV6_RECVRTHDR\r\n
0xd0000308 | IP_RECVTCLASS/IP_RECVTOS/IPV6_RECVTCLASS\r\n
0xd0000309 | MCAST_JOIN_GROUP\r\n
0xd000030a | MCAST_LEAVE_GROUP\r\n
0xd000030b | MCAST_BLOCK_SOURCE\r\n
0xd000030c | MCAST_UNBLOCK_SOURCE\r\n
0xd000030d | MCAST_JOIN_SOURCE_GROUP\r\n
0xd000030e | MCAST_LEAVE_SOURCE_GROUP\r\n
0xd000030f | IP_ORIGINAL_ARRIVAL_IF/IPV6_ORIGINAL_ARRIVAL_IF\r\n
0xd0000310 | IP_ECN/IPV6_ECN\r\n
0xd0000311 | IP_PKTINFO_EX/IPV6_PKTINFO_EX\r\n
0xd0000312 | IP_WFP_REDIRECT_RECORDS/IPV6_WFP_REDIRECT_RECORDS\r\n
0xd0000313 | IP_WFP_REDIRECT_CONTEXT/IPV6_WFP_REDIRECT_CONTEXT\r\n
0xd0000314 | IP_MTU_DISCOVER\r\n
0xd0000315 | IP_NRT_INTERFACE/IPV6_NRT_INTERFACE\r\n
0xd0000316 | IP_RECVERR/IPV6_RECVERR\r\n
0xd0000317 | SIO_GET_INTERFACE_LIST\r\n
0xd0000318 | SIO_GET_MULTICAST_FILTER\r\n
0xd0000319 | SIO_SET_MULTICAST_FILTER\r\n
0xd000031a | SIOCSMSFILTER\r\n
0xd000031b | SIOCGMSFILTER\r\n
0xd000031c | SIO_MULTIPOINT_LOOPBACK\r\n
0xd000031d | SIO_MULTICAST_SCOPE\r\n
0xd000031e | SIO_RCVALL\r\n
0xd000031f | SIO_RCVALL_MCAST\r\n
0xd0000320 | SIO_RCVALL_IGMPMCAST\r\n
0xd0000321 | SIO_RCVALL_MCAST_IF\r\n
0xd0000322 | SIO_RCVALL_IF\r\n
0xd0000323 | SIO_ADDRESS_LIST_SORT\r\n
0xd0000324 | join group\r\n
0xd0000325 | leave group\r\n
0xd0000326 | join group and add source\r\n
0xd0000327 | leave group and drop source\r\n
0xd0000328 | block source\r\n
0xd0000329 | unblock source\r\n
0xd000032a | set filter\r\n
0xd000032b | MLD level does not match protocol\r\n
0xd000032c | Invalid multicast address\r\n
0xd000032d | Invalid multicast source address\r\n
0xd000032e | Group already exists\r\n
0xd000032f | No existing state for group\r\n
0xd0000330 | Group is in exclude mode\r\n
0xd0000331 | No existing state for group or group is in exclude mode\r\n
0xd0000332 | No existing state for group or group is in include mode\r\n
0xd0000333 | Failed to set the state for the group\r\n
0xd0000334 | Failed to create the state for the group\r\n
0xd0000335 | Failed to modify the state for the group\r\n
0xd0000336 | Successfully created multicast session state\r\n
0xd0000337 | Another duplicate multicast session state exists, so no need to create a new one\r\n
0xd0000338 | Successfully added sources to multicast group\r\n
0xd0000339 | Successfully removed sources from multicast group\r\n
0xd000033a | Updated multicast group state; will send report\r\n
0xd000033b | Not modifying multicast group state\r\n
0xd000033c | Updated multicast discovery version\r\n
0xd000033d | Failed to create multicast session state when updating the multicast group\r\n
0xd000033e | Failed to create multicast session state from callback\r\n
0xd000033f | Failed to create multicast session state when searching for the interface\r\n
0xd0000340 | Failed to create multicast session state because access is denied\r\n
0xd0000341 | Failed to create multicast session state when adding sources to the session state\r\n
0xd0000342 | Failed to create multicast session state when creating the address\r\n
0xd0000343 | Failed to add sources to multicast group\r\n
0xd0000344 | Failed to modify multicast session state because access is denied\r\n
0xd0000345 | WFP context to the fragment\r\n
0xd0000346 | WFP context from the fragment to the reassembly context\r\n
0xd0000347 | leave\r\n
0xd0000348 | join\r\n
0xd0000349 | acquire\r\n
0xd000034a | release\r\n
0xd000034b | Unknown\r\n
0xd000034c | DAD\r\n
0xd000034d | Router solicitation\r\n
0xd000034e | WOL address pattern\r\n
0xd000034f | WOL TCP pattern\r\n
0xd0000350 | WOL local port pattern\r\n
0xd0000351 | Reassembly is prohibited\r\n
0xd0000352 | Fragment was filtered out\r\n
0xd0000353 | Out of memory\r\n
0xd0000354 | Protocol does not match\r\n
0xd0000355 | Fragment causes total packet length to exceed maximum payload size\r\n
0xd0000356 | Packet length does not properly align\r\n
0xd0000357 | The next header has the wrong IP option\r\n
0xd0000358 | Received mixed IPSec and non-IPSec fragments\r\n
0xd0000359 | Received zero length fragment\r\n
0xd000035a | Duplicate fragment\r\n
0xd000035b | Fragment falls beyond the data length\r\n
0xd000035c | Received duplicate or unsupported fragment\r\n
0xd000035d | Jumbogram received\r\n
0xd000035e | End of list\r\n
0xd000035f | No operation\r\n
0xd0000360 | Security\r\n
0xd0000361 | Loose source route\r\n
0xd0000362 | Timestamp\r\n
0xd0000363 | Record route\r\n
0xd0000364 | Struct source route\r\n
0xd0000365 | Stream ID\r\n
0xd0000366 | Router alert\r\n
0xd0000367 | Multi-destination\r\n
0xd0000368 | Single byte pad\r\n
0xd0000369 | Multiple byte pad\r\n
0xd000036a | Tunnel limit\r\n
0xd000036b | Router alert\r\n
0xd000036c | Jumbogram\r\n
0xd000036d | NSAP address\r\n
0xd000036e | Message length is not long enough\r\n
0xd000036f | Data length must be greater than or equal to the size of the message header\r\n
0xd0000370 | Invalid message type\r\n
0xd0000371 | Invalid message level\r\n
0xd0000372 | Invalid data length for this option\r\n
0xd0000373 | Invalid hop limit value\r\n
0xd0000374 | Invalid type of service value\r\n
0xd0000375 | Invalid hop-by-hop options\r\n
0xd0000376 | Invalid routing header\r\n
0xd0000377 | Invalid ECN field value\r\n
0xd0000378 | Invalid option\r\n
0xd0000379 | Option length is either too small or too large\r\n
0xd000037a | Option length must be greater than or equal to the size of the option header\r\n
0xd000037b | The length of the supplied buffer is smaller than the option length\r\n
0xd000037c | The option length is smaller than the minimum length for this option\r\n
0xd000037d | The option list must have space for an integral, non-zero number of entries\r\n
0xd000037e | The data alignment of the option payload is invalid\r\n
0xd000037f | Invalid flags\r\n
0xd0000380 | Multi-byte options can only occur once, or the combination of options is invalid\r\n
0xd0000381 | Invalid pointer value\r\n
0xd0000382 | Invalid address value\r\n
0xd0000383 | Invalid option\r\n
0xd0000384 | Option length is either too small or too large\r\n
0xd0000385 | Option length must be greater than or equal to the size of the option header\r\n
0xd0000386 | The length of the supplied buffer is smaller than the option length\r\n
0xd0000387 | The option list must have space for an integral, non-zero number of entries\r\n
0xd0000388 | Invalid address value\r\n
0xd0000389 | This option cannot be specified by the user\r\n
0xd000038a | Message length is not long enough\r\n
0xd000038b | Data length must be greater than or equal to the size of the message header\r\n
0xd000038c | Invalid message level\r\n
0xd000038d | Invalid IP_PKTINFO_EX option length\r\n
0xd000038e | Invalid option length\r\n
0xd000038f | Interface not found\r\n
0xd0000390 | Scope ID does not match the scope ID for the interface\r\n
0xd0000391 | Failed to find or create address to return\r\n

### 10.0.19041.610

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: SendDatagram %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto = %3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm = %6, MaxDataRetransmissions = %7, DelayedAckTicks = %8 msec, DelayedAckFrequency = %9, RACK enabled = %10, Tail Loss Probe enabled = %11.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5, Event = %6.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick = %4 Time = %5.\r\n
0xb0000527 | %1 timer rescheduled by processor %2 for processor %3 at Tick = %4 to Tick = %5, OldScheduledExpiration = %6 NewScheduledExpiration = %7 DueTime = %8 Aperiodic = %9.\r\n
0xb0000528 | %1 timer fired on processor %2 at Tick = %3, was scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for Destination %4 in Compartment %5, Reason: %8 (Rule %6.%7).\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0000558 | Teredo Add -- PID: %1 started listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb0000559 | Teredo Remove -- PID: %1 stopped listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb000055a | IP: RouteLookup - API: %1 DstAddr: %3 ConstrainSrcAddr: %4 ConstrainIfIndex: %5 ConstraintOveridden: %6 ReturnConstrained: %7 OutgoingIfIndex: %8 NextHopAddr: %9 Status: %10\r\n
0xb000055b | IP: SourceAddrLookup - DstAddr: %2 ConstrainSrcAddr: %3 ConstrainIfIndex: %4 OutgoingIfIndex: %5 ReturnConstrained: %6 SelectedSrcAddr: %7\r\n
0xb000055c | WFP-ALE: Partition Count=%1 Partition Mask=%2: Partition Id=%d Partition NumEntries = %4.\r\n
0xb000055d | WFP-ALE: HotAdd/Remove: Old Partiton Count=%1 Old Partition Mask=%2 New Partiton Count=%1 New Partition Mask=%2.\r\n
0xb000055e | WFP-ALE: RemoteEndPoint Insertion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb000055f | WFP-ALE: RemoteEndPoint Deletion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb0000560 | WFP-ALE: ALE: low memory state detected. LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000561 | WFP-ALE: leaving low memory state. HighMemoryEvent = %1 HighNonPagedPoolEvent = %2.\r\n
0xb0000562 | WFP-ALE: Dpc for cleanup initiated: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000563 | WFP: Dpc for cleanup QUEUED or RE-QUEUED: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000564 | TCP: LEDBAT %2: Connection %1, BaseDelayMs = %6, CurrentDelayMs = %7, CWnd = %3, SsThresh = %4, SndWnd = %5, DelayBasedCwndFactor %9%%, RemainingTimeMs = %8.\r\n
0xb0000565 | TCP: AssociateNameResContext Endpoint: %1 Status: %16 NameResolutionContext: %2 DnsName: %3 InterfaceIndex: %4 IPAddrCount: %5 IPAddrs: %7 %9 %11 %13 %15\r\n
0xb0000566 | TCP: InspectConnectWithNameResContext Connection: %5 (local: %2 remote: %4) NameResolutionContext: %6 DnsName: %7 Status: %8.\r\n
0xb0000567 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 InterfaceMetric: %10 RouteMetric: %11] is preferred over Route [DestinationPrefix: %14/%12 NextHop: %16 InterfaceIndex: %17 InterfaceMetric: %18 RouteMetric: %19] for Destination: %3 in Compartment: %1, Reason: %20.\r\n
0xb0000568 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 RouteMetric: %10] is blocked for Destination: %3 ConstrainInterfaceIndex: %11 ConstrainScopeZone: %12 in Compartment: %1, Reason: %13.\r\n
0xb0000569 | TCP: Tail Loss Probe Send Connection = %1 SndUna = %2, SndMax = %3, SendAvailable = %4, TailProbeSeq = %5, TailProbeLast = %6, ControlsToSend = %7, ThFlags = %8.\r\n
0xb000056a | TCP: Tail Loss Probe Event Connection = %1, Event = %2.\r\n
0xb000056b | TCP: RACK Event Connection = %1, Event = %2, MinRTT = %3, ReoWind = %4, TimeSlotDeltaMin = %5, SeqNum = %6, Timestamp = %7, RttSample = %8.\r\n
0xb000056c | TCP: Fastopen state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000056d | UDP: endpoint (family=%5 pid=%3) create failed: address family not attached.\r\n
0xb000056e | UDP: endpoint %1 (family=%5 pid=%3) create failed: compartment %4 not found.\r\n
0xb000056f | UDP: endpoint %1 (family=%5 pid=%3) created.\r\n
0xb0000570 | UDP: endpoint %1 (family=%5 pid=%3) create failed: inspection status = %2\r\n
0xb0000571 | UDP: endpoint %4 bind failed: address %2 cannot be resolved, status = %3\r\n
0xb0000572 | UDP: endpoint %4 (sockaddr=%2) bind failed: port-acquisition status = %3\r\n
0xb0000573 | UDP: endpoint %4 (sockaddr=%2) bind failed: inspection status = %3\r\n
0xb0000574 | UDP: endpoint %4 (sockaddr=%2) bound.\r\n
0xb0000575 | UDP: endpoint %4 (sockaddr=%2) closed.\r\n
0xb0000576 | UDP: endpoint %4 closed.\r\n
0xb0000577 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address resolution status = %6\r\n
0xb0000578 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address validation failed.\r\n
0xb0000579 | UDP: endpoint %1 (sockaddr=%3) send messages %5: source-address selection status = %6\r\n
0xb000057b | UDP: address family %2added to interface %1.\r\n
0xb000057c | UDP: address family %2removed from interface %1.\r\n
0xb000057d | UDP: Failure initializing transport protocol, status = %1\r\n
0xb000057e | UDP: Failure starting NLNPI client, status = %1\r\n
0xb000057f | UDP: Failure initializing NSI support, status = %1\r\n
0xb0000580 | UDP: Failure starting TLNPI provider, status = %1\r\n
0xb0000581 | UDP: Failure initializing QoS support, status = %1\r\n
0xb0000582 | UDP: Failure starting %1, status = %2\r\n
0xb0000583 | UDP: endpoint %1 (sockaddr=%3) send messages %5: could not allocate send context.\r\n
0xb0000584 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path af failure, status = %6\r\n
0xb0000585 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path missing next hop failure.\r\n
0xb0000586 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path next hop address failure.\r\n
0xb0000587 | TCP: Early Retransmission, FACK or RACK, Connection = %1, SndUna = %2, SackIsLostSeq = %3, DupAckCount = %4\r\n
0xb0000588 | TCP: Ignoring fastopen SYN option due to limit on concurrent SYN_RCVD fastopen connections, Connection = %1, SynRcvdLimit = %2\r\n
0xb0000589 | TCP: Failed to update fastopen key state, Location = %1, Status = %2. Server-side fastopen will be disabled\r\n
0xb000058a | TCP: Fast Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058b | TCP: SACK Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058c | TCP: Limited Transmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058d | TCP: SACK Retransmit Additional Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058e | %1: %2message. Type = %3, Code = %4, CompartmentId = %5, SourceAddress = %7, DestAddress = %9\r\n
0xb000058f | %1: %2path drop. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11\r\n
0xb0000590 | %1: Echo timeout. Status = %4\r\n
0xb0000591 | %1 Timer state changed to %3 by Processor %2 Usage = %4 at Tick = %5\r\n
0xb0000592 | TCP: connection %1 send complete %3 bytes at %4 (%2).\r\n
0xb0000593 | IP: Compartment creation. Compartment = %1, Protocol = %2, Private = %3, Status = %4.\r\n
0xb0000594 | IP: Compartment deletion. Compartment = %1, Protocol = %2.\r\n
0xb0000595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13.\r\n
0xb0000596 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5 CwrMax = %6.\r\n
0xb0000597 | IP: Compartment cleanup. Compartment = %1, Protocol = %2.\r\n
0xb0000598 | IP: Interface network category state change. Interface = %1, Compartment = %2 , Protocol = %3, NetworkCategory = %4, DomainNetworkLocation = %5, DomainType = %6, Signature = %7.\r\n
0xb0000599 | IP: Interface creation. Interface = %1, Compartment = %2, Protocol = %3, PhysicalMediumType = %4, Status = %5.\r\n
0xb000059a | IP: Interface deletion. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059b | IP: Interface cleanup. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059c | IP: SubInterface creation. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4, Status = %5.\r\n
0xb000059d | IP: SubInterface deletion. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059e | IP: SubInterface cleanup. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059f | IP: Interface change Notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005a0 | IP: Interface internet connectivity status change. Interface = %1, Compartment = %2, Protocol = %3, OldConnectivityStatus = %4, NewConnectivityStatus = %5.\r\n
0xb00005a1 | IP: Address change notification. Address = %2, Interface = %3, Compartment = %4, Protocol = %5, Reason = %6.\r\n
0xb00005a2 | IP: Route change notification. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, NotifyFlags = %8.\r\n
0xb00005a3 | IP: Neighbor change notification. IpAddress = %2, DlAddress = %4, Interface = %5, Compartment = %6, State = %7, Reason = %8.\r\n
0xb00005a4 | IP: Address DAD state change. Address = %2, Interface = %3, Compartment = %4, OldState = %5, NewState = %6, Reason = %7.\r\n
0xb00005a5 | IP: Route Dead Gateway Detection state change. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, OldState = %8, NewState = %9, OldProbeCount = %10, NewProbeCount = %11, OldUnreachablePaths = %12, NewUnreachablePaths = %13, OldMovedPaths = %14, NewMovedPaths = %15, TotalPaths = %16, OldStateChangeTick = %17, NewStateChangeTick = %18, DgdNeedsReset = %19, Reason = %20.\r\n
0xb00005a6 | IP: Disconnecting TCP connections with Address = %2, Interface = %3, Compartment = %4, SkipLocal = %5, SkipOnLink = %6.\r\n
0xb00005a7 | TCP: connection %1: Sending paced chunk of %6 bytes with CWnd = %2, SndWnd = %3, BytesAvailable = %4, BytesOutstanding = %5\r\n
0xb00005a8 | Fallback: Context = %1, Feature = %2, TraceReason = %3, Confidence = %4, Successes = %5, Failures = %6\r\n
0xb00005a9 | TCPIP: TCB %1 using fast loopback\r\n
0xb00005aa | IP: Router information change notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005ab | IP: %1. Interface = %2, Compartment = %3, RouterAddress = %5, DNS Server/Suffix: %7 %8, Lifetime = %9.\r\n
0xb00005ac | IP: Route rundown. Interface = %1, Compartment = %2, Prefix = %4/%5, NextHop = %7, Metric = %8, State = %9, Origin = %10, Age = %11, ValidLifetime = %12, PreferredLifetime = %13, Flags = %14.\r\n
0xb00005ad | TCP: CUBIC ECN event. Connection %1, CWnd %2, SSThresh = %3, SndUna = %4\r\n
0xb00005ae | INETINSPECT: Owner = %1, InspectHandle = %2, InspectType = %3, Action = %4, Status = %5\r\n
0xb00005b0 | FallbackCheck: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b1 | FallbackUpdate: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b2 | Fallback: Permanently disabling feature, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b3 | Fallback: Enabling feature for this boot session, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b4 | Fallback: Feature previously disabled, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b5 | TCP Fastopen fallback update: Tcb = %1, FastopenState = %2, DataBytesIn = %3, ShutdownStatus = %4, ProbeStatus = %5\r\n
0xb00005b6 | Disabling feature until connectivity is established: CompartmentId =%1, IfIndex = %2, Feature = %3, ConnectivityStatus = %4\r\n
0xb00005b7 | Disabling %1 for loopback connection\r\n
0xb00005b8 | Disabling TCP Fastopen for BaseEndpoint = %1 because an incompatible WFP callout is installed\r\n
0xb00005b9 | IP: Setting source constraint for route lookup - Compartment: %1 DstAddr: %3 ConstrainSrcAddr: %5 ConstrainIfIndex: %6 ConstraintFlags: %7\r\n
0xb00005ba | WFP-ALE: RemoteEndPoint Insertion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bb | WFP-ALE: RemoteEndPoint Deletion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bc | TCP: connection %8 (local=%2 remote=%4) system abort. PID = %6.\r\n
0xb00005bd | Disabling %1 due to no next hop\r\n
0xb00005be | TCP: endpoint (sockaddr=%2) bind failed: wake status = %3.\r\n
0xb00005bf | UDP: endpoint %4 (sockaddr=%2) bind failed: wake status = %3\r\n
0xb00005c0 | Acquire wake port %2, type=%1, family=%3, IF=%4, compartment=%5\r\n
0xb00005c1 | TCP: Connection %1 reached max SACK queue length\r\n
0xb00005c2 | TCP: Connection %1 requested fast open\r\n
0xb00005c3 | TCP: CUBIC Hystart state change event. Connection %1, State %2, CWnd %3, SSThresh = %4.\r\n
0xb00005c4 | IP: Transmitting loopback Nbl %1. Interface=%2, Compartment=%3, Src=%6, Dst=%5, Proto=%7.\r\n
0xb00005c5 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26 ConnectionTimeMs %27 Timestamps %28 RttUs %29 MinRtt %30 MaxRtt %31 SynRetrans %32 CongestionAlgorithm %33 \   State %34 Local %36 Remote %38 CWnd %39 SsThresh %40 RcvWnd %41 RcvBuf %42 SndWnd %43.\r\n
0xb00005c6 | TCPIP: Framing layer %1 (AddressFamily=%2) dropped %4 packet(s) on interface=%3, Reason=%5, Data=%6.\r\n
0xb00005c7 | TCP: Connection %1 Transport (Protocol %2, AddressFamily = %3) sent RST with Local = %5, Remote = %7. Reason = %8.\r\n
0xb00005c8 | TCP connection failed with Status = %1, Local = %3, Remote = %5, ProcessId = %6, TcpState = %7 at %8:%9:%10 Reason = %11.\r\n
0xb00005c9 | TCP: Connection %1 PRR send SackIsLostSeq %2 SackInFlight %3 SackBytes %4 SackIsLost %5 SsThresh %6 RecoveryFS %7 AckedData %8 BytesInFlight %9 BytesToSend %10 PrrDelivered %11 PrrOut %12.\r\n
0xb00005ca | UDP: Endpoint %1 segment message. SegmentSize = %2 (0 == No Segmentation) MessageLength = %3 HwDatagrams = %4 HwSegments = %5 SwSegments = %6 Status = %7.\r\n
0xb00005cb | UDP: Endpoint %1 segmentation offload unavailable. Reason = %2 SegmentSize = %3 LocalAddress = %5, RemoteAddress = %7.\r\n
0xb00005cc | TCPIP: Framing layer interface %1 (AddressFamily = %2) failed to bind to its provider. Code = %3. Status = %4.\r\n
0xb00005cd | TCPIP: OID request from framing layer interface %1 (AddressFamily = %2) failed. OID = %3. Status = %4.\r\n
0xb00005ce | TCPIP received a status indication on interface %1. AddressFamily = %2. NdisStatus = %3.\r\n
0xb00005cf | IP: Failed to set socket option. Level = %1. Option = %2. Status = %3.\r\n
0xb00005d0 | IP: Failed to set socket IOCTL. IOCTL = %1. Status = %2.\r\n
0xb00005d1 | Failed to process multicast %1 request. Address = %2 %6. Source Address = %3 %7. Reason = %8. Status = %9.\r\n
0xb00005d2 | Processed multicast %1 request successfully. Address = %2 %6. Source Address = %3 %7.\r\n
0xb00005d3 | %1. Interface = %2. Address = %3 %5. Data = %6.\r\n
0xb00005d4 | %1. Interface = %2. Address = %3 %5. Data = %6. Status = %7.\r\n
0xb00005d5 | Invalid ECN codepoints in reassembly. Ce = %1. Ect0 = %2. Ect1 = %3. NotEct = %4.\r\n
0xb00005d6 | Reassembly failure: packets do not add up correctly.  Interface = %1. Address family = %2.\r\n
0xb00005d7 | Reassembly failure: failed to restore IPSec packet history.  Interface = %1. Address family = %2. Status = %3.\r\n
0xb00005d8 | Could not transfer %1.  Interface = %2. Address family = %3.\r\n
0xb00005d9 | Attempting to %1 the multicast group at FL.  Interface = %2. Address = %3 %5. Data = %6. Status = %7.\r\n
0xb00005da | Failed to update address list at FL. Interface = %1. Address Family = %2. Status = %3.\r\n
0xb00005db | Too many DAD failures, so will not create temporary address. Interface = %1. Address = %2 %4.\r\n
0xb00005dc | Failed to address interface; deleting it. Interface = %1. Status = %2.\r\n
0xb00005dd | Failed to reach default gateway after reconnect; cleaning settings.  Interface = %1.\r\n
0xb00005de | Failed to sync interface with registry.  Interface = %1. Field = %2. Status = %3.\r\n
0xb00005df | Failed to %1 an active reference on the interface.  Interface = %2. Reference Reason = %3. Status = %4.\r\n
0xb00005e0 | Redirect path hijack for destination %2 %3 from %5 %6. Interface = %1.\r\n
0xb00005e1 | Redirect path rate limit for IPv6 source address %3. Interface = %1.\r\n
0xb00005e2 | Dropped %2 fragment. Interface = %3. Reason = %1.\r\n
0xb00005e3 | Reassembly timeout. Interface = %1. Id = %2. Source Address = %3 %6.  Destination Address = %4 %7.\r\n
0xb00005e4 | Invalid IP option. Option = %3. Level = %2. Reason = %1.\r\n
0xb00005e5 | Invalid IP hop-by-hop option.  Option = %2. Reason = %1.\r\n
0xb00005e7 | Invalid IP routing header option. Reason = %1.\r\n
0xb00005e9 | This option cannot be specified by the user\r\n
0xb00005ea | TCP: interface %1: received potential RSC status indication. Current IPv4 State = %2, Offload IPv4 State = %3, Current IPv6 State = %4, Offload IPv6 State = %5.\r\n
0xb00005eb | UDP: endpoint %1: URO SCU received. SegCount = %2, SegSize = %3, DataLength = %4.\r\n
0xb00005ec | TCP software RSC global disabled mask = %1, UDP software URO global disabled mask = %2.\r\n
0xb00005ed | UDP: Global parameters updated for Address Family %1: DisableUro = %2.\r\n
0xb00005ee | IP: IPSNPI client rundown. %3 Interface = %1, Compartment = %2, Client = %4.\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010452 | IP: Interface media disconnect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001045a | IP: Address DAD successful. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001045b | IP: Address DAD failed. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2, DL address of packet = %5.\r\n
0xb001045c | IP: Address DAD started. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010467 | IP: Address addition. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010468 | IP: Address deletion. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001046a | Framing: Interface operation status change. Interface = %1, Compartment = %4, Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0010470 | Framing: NDIS pause event. Interface = %1, Compartment = %3.\r\n
0xb0010471 | Framing: NDIS restart event. Interface = %1, Compartment = %3.\r\n
0xb0010478 | IP: Interface property change. Interface = %1, Compartment = %10, Protocol = %11, Advertise = %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7, WeakHostSend = %8, WeakHostReceive = %9.\r\n
0xb00104b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, Address = %4 %3 %6.\r\n
0xb00104b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7.\r\n
0xb0010529 | IP: Interface media connect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052a | IP: Interface limited link connectivity set. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052b | IP: Interface limited link connectivity reset. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052c | IP: Neighbor state change. IPAddress = %3, DLAddress = %5, Interface = %1, Compartment = %9, OldState = %6, NewState = %7, Event = %8.\r\n
0xb001052d | IP: Neighbor Discovery. Event = %5, Interface = %1, Compartment = %6, SourceIpAddress = %3, TargetIpAddress = %4.\r\n
0xb001052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions: %6, Reason: %10 (Rule %7 %8.%9).\r\n
0xb0010534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb001054e | IP: Interface configuration flags updated. Interface = %1, Compartment = %5, Protocol = %6, Property = %2, Value = %3, Event = %4.\r\n
0xb0010557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, UdpSegmentationOffloadInfo/TcpRecvSegCoalesceInfo %9, NrtNameResolutionId/UdpRecvSegCoalesceOffloadInfo %10\r\n
0xb0010565 | TCP: AssociateNameResContext EndpointObj: %1 IsConnectionObj: %2 NameResContext: %3 Status: %4\r\n
0xb0010595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13 IsLimitedSlowStart = %14.\r\n
0xb00105ca | UDP: Endpoint %1 segment message. SegmentSize = %2 (0 == No Segmentation) MessageLength = %3 HwDatagrams = %4 HwSegments = %5 SwSegments = %6 SubMssSegments = %7 Status = %8.\r\n
0xb00204b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, Address = %4 %3 %6.\r\n
0xb00204b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7, ReceiveLinkSpeed = %10 bps, MediaConnectState = %11.\r\n
0xb00304b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Metric = %11, Connected = %12, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, InternetConnectivityStatus = %13, Flags = %14, Address = %4 %3 %6.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | PacingTimer\r\n
0xd000002c | DisconnectTimer\r\n
0xd000002d | SwsTimer\r\n
0xd000002e | ReassemblyRateTimer\r\n
0xd000002f | SynOrRstValidationTimer\r\n
0xd0000030 | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000031 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000032 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000033 | TCP_KEEPALIVE\r\n
0xd0000034 | TCP_MAXSEG\r\n
0xd0000035 | TCP_MAXRT\r\n
0xd0000036 | TCP_STDURG\r\n
0xd0000037 | TCP_NOURG\r\n
0xd0000038 | TCP_ATMARK\r\n
0xd0000039 | TCP_NOSYNRETRIES\r\n
0xd000003a | TCP_TIMESTAMPS\r\n
0xd000003b | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003c | TCP_CONGESTION_ALGORITHM\r\n
0xd000003d | TCP_DELAY_FIN_ACK\r\n
0xd000003e | SO_DEBUG\r\n
0xd000003f | SO_ACCEPTCONN\r\n
0xd0000040 | SO_REUSEADDR\r\n
0xd0000041 | SO_KEEPALIVE\r\n
0xd0000042 | SO_DONTROUTE\r\n
0xd0000043 | SO_BROADCAST\r\n
0xd0000044 | SO_USELOOPBACK\r\n
0xd0000045 | SO_LINGER\r\n
0xd0000046 | SO_OOBINLINE\r\n
0xd0000047 | SO_SNDBUF\r\n
0xd0000048 | SO_RCVBUF\r\n
0xd0000049 | SO_CONDITIONAL_ACCEPT\r\n
0xd000004a | SO_PAUSE_ACCEPT\r\n
0xd000004b | SO_COMPARTMENT_ID\r\n
0xd000004c | SO_RANDOMIZE_PORT\r\n
0xd000004d | SO_PORT_SCALABILITY\r\n
0xd000004e | NldsInvalid\r\n
0xd000004f | NldsTentative\r\n
0xd0000050 | NldsDuplicate\r\n
0xd0000051 | NldsDeprecated\r\n
0xd0000052 | NldsPreferred\r\n
0xd0000053 | Indicate\r\n
0xd0000054 | Pend\r\n
0xd0000055 | Satisfy\r\n
0xd0000056 | NdisPhysicalMediumUnspecified\r\n
0xd0000057 | NdisPhysicalMediumWirelessLan\r\n
0xd0000058 | NdisPhysicalMediumCableModem\r\n
0xd0000059 | NdisPhysicalMediumPhoneLine\r\n
0xd000005a | NdisPhysicalMediumDSL\r\n
0xd000005b | NdisPhysicalMedium1394\r\n
0xd000005c | NdisPhysicalMediumWirelessWan\r\n
0xd000005d | NdisPhysicalMediumNative802_11\r\n
0xd000005e | NdisPhysicalMediumBluetooth\r\n
0xd000005f | NdisPhysicalMediumInfiniband\r\n
0xd0000060 | NdisPhysicalMediumWiMax\r\n
0xd0000061 | NdisPhysicalMedium802_3\r\n
0xd0000062 | NdisPhysicalMedium802_5\r\n
0xd0000063 | NdisPhysicalMediumIrda\r\n
0xd0000064 | NdisPhysicalMediumWiredWAN\r\n
0xd0000065 | IP checksum offload not computed\r\n
0xd0000066 | TCP checksum offload not computed\r\n
0xd0000067 | UDP checksum offload not computed\r\n
0xd0000068 | Header not aligned on 4-byte boundary\r\n
0xd0000069 | IP fragmentation\r\n
0xd000006a | Source address is not unicast\r\n
0xd000006b | Destination address is neither TCP/UDP unicast nor UDP multicast\r\n
0xd000006c | Ethernet and IP header not contiguous\r\n
0xd000006d | IP options present\r\n
0xd000006e | ESP over UDP\r\n
0xd000006f | Lack contiguous space for upper layer headers\r\n
0xd0000070 | WFP filters present\r\n
0xd0000071 | Nexthop is unavailable\r\n
0xd0000072 | Path has been invalidated due to policy change\r\n
0xd0000073 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000074 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000075 | Session state is not compatible\r\n
0xd0000076 | TCP options present\r\n
0xd0000077 | UDP IPv6 checksum absent in packet\r\n
0xd0000078 | Packet is for a loopback interface\r\n
0xd0000079 | Packet is from a Raw Socket\r\n
0xd000007a | TL Ancillary headers present\r\n
0xd000007b | NL Ancillary headers present\r\n
0xd000007c | Type of Service present\r\n
0xd000007d | IpSec headers present\r\n
0xd000007e | Interface is not Ethernet\r\n
0xd000007f | Nbl check failed\r\n
0xd0000080 | Destination address is unknown\r\n
0xd0000081 | Loopback inspect failed\r\n
0xd0000082 | Next header is not a transport protocol eligible for the fast path\r\n
0xd0000083 | IP packet length is invalid\r\n
0xd0000084 | IP version is invalid\r\n
0xd0000085 | Failed to allocate the WSD cache\r\n
0xd0000086 | Failure initializing PnP work queue\r\n
0xd0000087 | Failed to get persistent parameters\r\n
0xd0000088 | Rejected persistent parameters\r\n
0xd0000089 | qualified profile\r\n
0xd000008a | qualified destination\r\n
0xd000008b | sample collection completion\r\n
0xd000008c | idle time expiration\r\n
0xd000008d | allocation\r\n
0xd000008e | new sample request\r\n
0xd000008f | configuration change\r\n
0xd0000090 | Idle\r\n
0xd0000091 | ProbingWs\r\n
0xd0000092 | ProbeWait\r\n
0xd0000093 | ProbingWithoutWs\r\n
0xd0000094 | RecordWait\r\n
0xd0000095 | EreQualified\r\n
0xd0000096 | Qualified\r\n
0xd0000097 | Source Unspecified\r\n
0xd0000098 | Destination is multicast\r\n
0xd0000099 | Header is invalid (location 0)\r\n
0xd000009a | Checksum is invalid\r\n
0xd000009b | Transport endpoint was not found\r\n
0xd000009c | Connected path error\r\n
0xd000009d | Session state error\r\n
0xd000009e | Receive Inspection\r\n
0xd000009f | ACK Invalid (subreason 0) (invalid ACK in SYN_SENT state)\r\n
0xd00000a0 | Expected SYN\r\n
0xd00000a1 | Received RST (subreason 0)\r\n
0xd00000a2 | Received SYN while in SYN_RCVD state\r\n
0xd00000a3 | Simultaneous Connect\r\n
0xd00000a4 | PAWS Failed\r\n
0xd00000a5 | Land Attack (subreason 0)\r\n
0xd00000a6 | Missed RST\r\n
0xd00000a7 | Outside Receive Window (subreason 0)\r\n
0xd00000a8 | Duplicate Segment\r\n
0xd00000a9 | Closed Window\r\n
0xd00000aa | TCB Removed\r\n
0xd00000ab | FIN-WAIT2\r\n
0xd00000ac | Reassembly Conflict\r\n
0xd00000ad | FIN Received\r\n
0xd00000ae | Listener received segment with invalid flags\r\n
0xd00000af | URG flag set but could not allocate urgent data state\r\n
0xd00000b0 | TCB was not inserted in TCB table\r\n
0xd00000b1 | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000b2 | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000b3 | Packet dropped by TIME-WAIT TCB (subreason 0)\r\n
0xd00000b4 | SYN+ACK with Fastopen cookie request\r\n
0xd00000b5 | Listener dropped SYN because SO_PAUSE_ACCEPT was set\r\n
0xd00000b6 | Listener dropped SYN to reduce memory pressure\r\n
0xd00000b7 | Bad source address\r\n
0xd00000b8 | Not locally destined\r\n
0xd00000b9 | Protocol unreachable\r\n
0xd00000ba | Port unreachable\r\n
0xd00000bb | Bad length\r\n
0xd00000bc | Malformed Header\r\n
0xd00000bd | No route available\r\n
0xd00000be | Beyond scope\r\n
0xd00000bf | Inspection drop\r\n
0xd00000c0 | Too many decapsulations\r\n
0xd00000c1 | Administratively prohibited\r\n
0xd00000c2 | Bad checksum\r\n
0xd00000c3 | Hop limit exceeded\r\n
0xd00000c4 | Address unreachable\r\n
0xd00000c5 | Fragment MTU exceeded\r\n
0xd00000c6 | Buffer Length Exceeded\r\n
0xd00000c7 | Address Resolution Timeout\r\n
0xd00000c8 | Address Resolution Failure\r\n
0xd00000c9 | IPsec failure\r\n
0xd00000ca | Extension Headers Failure\r\n
0xd00000cb | Allocation Failure\r\n
0xd00000cc | IPSNPI Client Drop\r\n
0xd00000cd | Unsupported Offload\r\n
0xd00000ce | Routing Failure\r\n
0xd00000cf | Ancillary Data Failure\r\n
0xd00000d0 | Raw Data Failure\r\n
0xd00000d1 | Session State Failure\r\n
0xd00000d2 | IPSNPI Allocation Failure\r\n
0xd00000d3 | IPSNPI Modified But Not Forwarded\r\n
0xd00000d4 | IPSNPI No Next Hop Specified\r\n
0xd00000d5 | IPSNPI Compartment Not Found\r\n
0xd00000d6 | IPSNPI Interface Not Found\r\n
0xd00000d7 | IPSNPI Subinterface Not Found\r\n
0xd00000d8 | IPSNPI Interface disabled\r\n
0xd00000d9 | IPSNPI Segmentation Failed\r\n
0xd00000da | IPSNPI No Ethernet Header\r\n
0xd00000db | IPSNPI Unexpected Fragment\r\n
0xd00000dc | IPSNPI Unsupported Interface Type\r\n
0xd00000dd | Default\r\n
0xd00000de | NewReno\r\n
0xd00000df | CTCP\r\n
0xd00000e0 | DCTCP\r\n
0xd00000e1 | LEDBAT\r\n
0xd00000e2 | CUBIC\r\n
0xd00000e3 | TcpTemplateTypeInternet\r\n
0xd00000e4 | TcpTemplateTypeDatacenter\r\n
0xd00000e5 | TcpTemplateTypeCompat\r\n
0xd00000e6 | TcpTemplateTypeDatacenterCustom\r\n
0xd00000e7 | TcpTemplateTypeInternetCustom\r\n
0xd00000e8 | TcpTemplateTypeDefault\r\n
0xd00000e9 | TcpTemplateTypeAutomatic\r\n
0xd00000ea | No Failure\r\n
0xd00000eb | Unknown\r\n
0xd00000ec | System Policy\r\n
0xd00000ed | NIC Capacity Reached\r\n
0xd00000ee | System Low On Memory\r\n
0xd00000ef | WFP driver / Stream inspection\r\n
0xd00000f0 | Weak Host Model Enabled\r\n
0xd00000f1 | Forwarding Enabled\r\n
0xd00000f2 | Hardware capability\r\n
0xd00000f3 | NDIS filter/NIC property\r\n
0xd00000f4 | Loopback fast path socket option not set on both ends\r\n
0xd00000f5 | Filter policy existed for the loopback connection\r\n
0xd00000f6 | IPv4\r\n
0xd00000f7 | IPv6\r\n
0xd00000f8 | unbind\r\n
0xd00000f9 | bind\r\n
0xd00000fa | port change\r\n
0xd00000fb | none\r\n
0xd00000fc | receive hash\r\n
0xd00000fd | receive scale\r\n
0xd00000fe | enabled\r\n
0xd00000ff | disabled\r\n
0xd0000100 | removing\r\n
0xd0000101 | adding\r\n
0xd0000102 | complete binding initialization\r\n
0xd0000103 | complete port initialization\r\n
0xd0000104 | enumerate interface ports\r\n
0xd0000105 | query port link state\r\n
0xd0000106 | query port interface index\r\n
0xd0000107 | query interface ports\r\n
0xd0000108 | query port RSS capabilities\r\n
0xd0000109 | get usable processors\r\n
0xd000010a | query port driver version\r\n
0xd000010b | query port RSS processor configuration\r\n
0xd000010c | set receive scale parameters\r\n
0xd000010d | set receive hash parameters\r\n
0xd000010e | update interface ports\r\n
0xd000010f | not available\r\n
0xd0000110 | available\r\n
0xd0000111 | available on ports\r\n
0xd0000112 | global configuration\r\n
0xd0000113 | active mode\r\n
0xd0000114 | Bind Adapter\r\n
0xd0000115 | Unbind Adapter (begin)\r\n
0xd0000116 | Unbind Adapter (end)\r\n
0xd0000117 | NetEvent Restart\r\n
0xd0000118 | NetEvent Power-down\r\n
0xd0000119 | NetEvent Power-up\r\n
0xd000011a | NetEvent NDK-enable\r\n
0xd000011b | NetEvent NDK-disable\r\n
0xd000011c | NetEvent NDK usage stopped\r\n
0xd000011d | Indicate new NDK interface arrival\r\n
0xd000011e | Indicate NDK interface removal\r\n
0xd000011f | Indicate NDK operational status change\r\n
0xd0000120 | Undefined\r\n
0xd0000121 | Adapter\r\n
0xd0000122 | QP\r\n
0xd0000123 | CQ\r\n
0xd0000124 | MR\r\n
0xd0000125 | MW\r\n
0xd0000126 | PD\r\n
0xd0000127 | SharedEndpoint\r\n
0xd0000128 | Connector\r\n
0xd0000129 | Listener\r\n
0xd000012a | SRQ\r\n
0xd000012b | Max\r\n
0xd000012c | Async\r\n
0xd000012d | Inline\r\n
0xd000012e | Local\r\n
0xd000012f | Remote\r\n
0xd0000130 | Privileged\r\n
0xd0000131 | Local\r\n
0xd0000132 | Remote\r\n
0xd0000133 | NotifyErrors\r\n
0xd0000134 | NotifyAny\r\n
0xd0000135 | NotifySolicited\r\n
0xd0000136 | Invalid\r\n
0xd0000137 | Software Slot allocated\r\n
0xd0000138 | Hardware Slot allocated\r\n
0xd0000139 | Policy error\r\n
0xd000013a | system error\r\n
0xd000013b | Enabled\r\n
0xd000013c | Send request dropped\r\n
0xd000013d | Receive dropped\r\n
0xd000013e | Disconnect request dropped\r\n
0xd000013f | Reset dropped\r\n
0xd0000140 | WFP API No Failure\r\n
0xd0000141 | WFP API WasRedirectedToProxy\r\n
0xd0000142 | WFP API RegisterForExitingEndpoint\r\n
0xd0000143 | WFP API ClassifiableFieldGetAf\r\n
0xd0000144 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000145 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd0000146 | WFP API ClassifiableFieldGetRemotePort\r\n
0xd0000147 | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd0000148 | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd0000149 | Processor Add\r\n
0xd000014a | Power Source Change\r\n
0xd000014b | AC\r\n
0xd000014c | DC\r\n
0xd000014d | DC Short Term\r\n
0xd000014e | Unknown\r\n
0xd000014f | is stopping timers\r\n
0xd0000150 | has stopped timers\r\n
0xd0000151 | is locking partitions\r\n
0xd0000152 | has locked partitions\r\n
0xd0000153 | is unlocking partitions\r\n
0xd0000154 | has unlocked partitions\r\n
0xd0000155 | is starting timers\r\n
0xd0000156 | has started timers\r\n
0xd0000157 | is starting\r\n
0xd0000158 | is complete\r\n
0xd0000159 | IP\r\n
0xd000015a | TCP\r\n
0xd000015b | leaving S0\r\n
0xd000015c | entering S0\r\n
0xd000015d | Unreachable\r\n
0xd000015e | Incomplete\r\n
0xd000015f | Probe\r\n
0xd0000160 | Delay\r\n
0xd0000161 | Stale\r\n
0xd0000162 | Reachable\r\n
0xd0000163 | Permanent\r\n
0xd0000164 | Maximum\r\n
0xd0000165 | Map\r\n
0xd0000166 | Configure\r\n
0xd0000167 | TlSuspectsReachability\r\n
0xd0000168 | TlConfirmsReachability\r\n
0xd0000169 | NaConfirmsReachability\r\n
0xd000016a | ProbeReachability\r\n
0xd000016b | DadSolicitation\r\n
0xd000016c | NewDlAddress\r\n
0xd000016d | TriggerNud\r\n
0xd000016e | Resolve\r\n
0xd000016f | Timeout\r\n
0xd0000170 | Sending neighbor solicitation\r\n
0xd0000171 | Received neighbor solicitation\r\n
0xd0000172 | Sending neighbor advertisement\r\n
0xd0000173 | Received neighbor advertisement\r\n
0xd0000174 | Sending router solicitation\r\n
0xd0000175 | Received router solicitation\r\n
0xd0000176 | Sending router advertisement\r\n
0xd0000177 | Received router advertisement\r\n
0xd0000178 | Receive\r\n
0xd0000179 | ReceiveAndInvalidate\r\n
0xd000017a | Send\r\n
0xd000017b | FastRegister\r\n
0xd000017c | Bind\r\n
0xd000017d | Invalidate\r\n
0xd000017e | Read\r\n
0xd000017f | Write\r\n
0xd0000180 | Not Activated\r\n
0xd0000181 | Activated\r\n
0xd0000182 | TCP connect\r\n
0xd0000183 | TCP send\r\n
0xd0000184 | UDP send\r\n
0xd0000185 | RAW send\r\n
0xd0000186 | Received Router Advertisement\r\n
0xd0000187 | AdminConfigured\r\n
0xd0000188 | NetworkProperty\r\n
0xd0000189 | CreateWolContext\r\n
0xd000018a | DeleteWolContext\r\n
0xd000018b | SetWolContext\r\n
0xd000018c | ClearWolContext\r\n
0xd000018d | WolContextEvicted\r\n
0xd000018e | AddWolAddress\r\n
0xd000018f | RemoveWolAddress\r\n
0xd0000190 | Send\r\n
0xd0000191 | Receive\r\n
0xd0000192 | WFP-ALE: RemoteEndPoint Address\r\n
0xd0000193 | WFP-ALE: RemoteEndPoint Port\r\n
0xd0000194 | WFP-ALE: LocalEndPoint Address\r\n
0xd0000195 | WFP-ALE: LocalEndPoint Port\r\n
0xd0000196 | WFP-ALE: Partition Id\r\n
0xd0000197 | WFP-ALE: Parition NumEnties\r\n
0xd0000198 | SlowDownEntry\r\n
0xd0000199 | SlowDownExit\r\n
0xd000019a | SlowDownTracking\r\n
0xd000019b | BaseDelayUpdate\r\n
0xd000019c | Ack\r\n
0xd000019d | DupAck\r\n
0xd000019e | Timeout\r\n
0xd000019f | Ecn\r\n
0xd00001a0 | SpuriousTimeout\r\n
0xd00001a1 | Network Context Constraint\r\n
0xd00001a2 | Prefix Length Policy\r\n
0xd00001a3 | Start Epoch Policy\r\n
0xd00001a4 | Default Routes Disabled On Interface\r\n
0xd00001a5 | Unconstrained Lookup Disallowed On Interface\r\n
0xd00001a6 | Interface Disconnected\r\n
0xd00001a7 | Route Invalid Lifetime\r\n
0xd00001a8 | Interface Constraint\r\n
0xd00001a9 | Scope Constraint\r\n
0xd00001aa | Unconstrained Offlink Route Lookup Disallowed On Interface\r\n
0xd00001ab | Rechability\r\n
0xd00001ac | Prefix Length\r\n
0xd00001ad | Route And Interface Metrics\r\n
0xd00001ae | Destination And Source Hash\r\n
0xd00001af | Route Order\r\n
0xd00001b0 | Dead Gateway\r\n
0xd00001b1 | OnLink Route\r\n
0xd00001b2 | Prefer Same Address\r\n
0xd00001b3 | Prefer Appropriate Scope\r\n
0xd00001b4 | Avoid Deprecated Addresses\r\n
0xd00001b5 | Prefer Home Addresses\r\n
0xd00001b6 | Prefer Outgoing Interface\r\n
0xd00001b7 | Prefer Addresses Associated With NextHop\r\n
0xd00001b8 | Prefer Matching Label\r\n
0xd00001b9 | Prefer Temporary Addresses\r\n
0xd00001ba | System Defined Preference (Windows Specific)\r\n
0xd00001bb | Prefer Longest Matching Prefix With NextHop (Windows Specific)\r\n
0xd00001bc | Prefer Longest Matching Prefix\r\n
0xd00001bd | TimerArmed\r\n
0xd00001be | TimerFired\r\n
0xd00001bf | Failed\r\n
0xd00001c0 | Init\r\n
0xd00001c1 | SetTimeSlotData\r\n
0xd00001c2 | SetTailTimeSlot\r\n
0xd00001c3 | EraseTimestamps\r\n
0xd00001c4 | GetRecoverySeq\r\n
0xd00001c5 | RttSampleUpdate\r\n
0xd00001c6 | TcpFastopenOff\r\n
0xd00001c7 | TcpFastopenAccepting\r\n
0xd00001c8 | TcpFastopenServerSendingCookie\r\n
0xd00001c9 | TcpFastopenServerSentCookie\r\n
0xd00001ca | TcpFastopenNegotiate\r\n
0xd00001cb | TcpFastopenAttempt\r\n
0xd00001cc | TcpFastopenNegotiateSuccess\r\n
0xd00001cd | TcpFastopenAttemptSuccess\r\n
0xd00001ce | TcpFastopenCookieRollover\r\n
0xd00001cf | TcpFastopenFailed\r\n
0xd00001d0 | TcpFastopenFailedBlocklist\r\n
0xd00001d1 | TcpFastopenServerAcceptSuccess\r\n
0xd00001d2 | TcpFastopenServerAcceptTimeout\r\n
0xd00001d3 | TcpFastopenServerAcceptSendData\r\n
0xd00001d4 | TcpFastopenFailedSimultaneousConnect\r\n
0xd00001d5 | TcpFastopenFailedInvalidCookie\r\n
0xd00001d6 | TcpFastopenFailedSynTimeout\r\n
0xd00001d7 | TcpFastopenFailedTimeout\r\n
0xd00001d8 | TcpFastopenFailedReset\r\n
0xd00001d9 | TcpFastopenFallback\r\n
0xd00001da | TcpFastopenCookieRequestDeclined\r\n
0xd00001db | TcpFastopenFailedSuddenRttIncrease\r\n
0xd00001dc | TcpFastopenFailedSynAckWithCookieRequest\r\n
0xd00001dd | TcpFastopenFailedNoNextHop\r\n
0xd00001de | General failure\r\n
0xd00001df | Truncated header\r\n
0xd00001e0 | Invalid checksum\r\n
0xd00001e1 | Inspection drop\r\n
0xd00001e2 | Rejecting loopback neighbor discovery\r\n
0xd00001e3 | Unknown type/code\r\n
0xd00001e4 | Truncated IP header\r\n
0xd00001e5 | Oversized IP header\r\n
0xd00001e6 | No handler\r\n
0xd00001e7 | Not responding with error for error\r\n
0xd00001e8 | Invalid source\r\n
0xd00001e9 | Interface rate limit\r\n
0xd00001ea | Path rate limit\r\n
0xd00001eb | No route\r\n
0xd00001ec | No matching request\r\n
0xd00001ed | Buffer too small\r\n
0xd00001ee | Failed to obtain ancillary data\r\n
0xd00001ef | Incorrect hop limit\r\n
0xd00001f0 | Unknown code\r\n
0xd00001f1 | Source not linklocal\r\n
0xd00001f2 | Truncated ND header\r\n
0xd00001f3 | Invalid ND option SourceLinkAddr\r\n
0xd00001f4 | Invalid ND option MTU\r\n
0xd00001f5 | Invalid ND option PrefixInformation\r\n
0xd00001f6 | Invalid ND option RouteInformation\r\n
0xd00001f7 | Invalid ND option RDNSS\r\n
0xd00001f8 | Invalid ND option DNSSL\r\n
0xd00001f9 | Packet parsing failure\r\n
0xd00001fa | Echo Reply\r\n
0xd00001fb | Destination Unreachable\r\n
0xd00001fc | Packet Too Big\r\n
0xd00001fd | Destination Unreachable(v4)/Time Exceeded(v6)\r\n
0xd00001fe | Source Quench(v4)/Parameter Problem(v6)\r\n
0xd00001ff | Redirect\r\n
0xd0000200 | Echo Request\r\n
0xd0000201 | Router Advertisement\r\n
0xd0000202 | Router Solicitation\r\n
0xd0000203 | Time Exceeded\r\n
0xd0000204 | Parameter Problem\r\n
0xd0000205 | Timestamp Request\r\n
0xd0000206 | Timestamp Reply\r\n
0xd0000207 | Address Mask Request\r\n
0xd0000208 | Address Mask Reply\r\n
0xd0000209 | Echo Request\r\n
0xd000020a | Echo Reply\r\n
0xd000020b | Multicast Listener Query\r\n
0xd000020c | Multicast Listener Report\r\n
0xd000020d | Multicast Listener Done\r\n
0xd000020e | Router Solicitation\r\n
0xd000020f | Router Advertisement\r\n
0xd0000210 | Neighbor Solicitation\r\n
0xd0000211 | Neighbor Advertisement\r\n
0xd0000212 | Redirect Message\r\n
0xd0000213 | Multicast Listener Discovery\r\n
0xd0000214 | Not Parsed\r\n
0xd0000215 | Periodic\r\n
0xd0000216 | Aperiodic\r\n
0xd0000217 | Unknown\r\n
0xd0000218 | Public\r\n
0xd0000219 | Private\r\n
0xd000021a | Domain\r\n
0xd000021b | Remote\r\n
0xd000021c | Link\r\n
0xd000021d | NonDomainNetwork\r\n
0xd000021e | DomainNetwork\r\n
0xd000021f | DomainAuthenticated\r\n
0xd0000220 | InterfaceAddition\r\n
0xd0000221 | InterfaceDeletion\r\n
0xd0000222 | ZoneChange\r\n
0xd0000223 | ConfigurationFlagChange\r\n
0xd0000224 | ForwardingEnable\r\n
0xd0000225 | ForwardingDisable\r\n
0xd0000226 | WeakHostReceiveEnable\r\n
0xd0000227 | WeakHostReceiveDisable\r\n
0xd0000228 | NetworkCategoryStateChange\r\n
0xd0000229 | MetricChange\r\n
0xd000022a | MediaConnect\r\n
0xd000022b | MediaDisconnect\r\n
0xd000022c | OffloadCapabilityChange\r\n
0xd000022d | DisableDefaultRoutesSet\r\n
0xd000022e | DisableDefaultRoutesReset\r\n
0xd000022f | ForceTunnelingSet\r\n
0xd0000230 | ForceTunnelingReset\r\n
0xd0000231 | LimitedLinkConnectivitySet\r\n
0xd0000232 | LimitedLinkConnectivityReset\r\n
0xd0000233 | LocalityConfigChange\r\n
0xd0000234 | RoutingFlagsSet\r\n
0xd0000235 | RoutingFlagsReset\r\n
0xd0000236 | PortStateChange\r\n
0xd0000237 | RscUnawareIpsnpiClientPresent\r\n
0xd0000238 | RscUnawareIpsnpiClientAbsent\r\n
0xd0000239 | PromiscuousModeEnabled\r\n
0xd000023a | PromiscuousModeDisabled\r\n
0xd000023b | NoInternetConnectivity\r\n
0xd000023c | NoInternetDnsResolutionSucceeded\r\n
0xd000023d | InternetConnectivityDetected\r\n
0xd000023e | InternetConnectivityUnknown\r\n
0xd000023f | Timeout\r\n
0xd0000240 | DadStarted\r\n
0xd0000241 | OptimisticDadStarted\r\n
0xd0000242 | DadPassed\r\n
0xd0000243 | NSReceived\r\n
0xd0000244 | NAReceived\r\n
0xd0000245 | InterfaceDisabled\r\n
0xd0000246 | DadDisabled\r\n
0xd0000247 | AddressAddition\r\n
0xd0000248 | AddressDeletion\r\n
0xd0000249 | DadStatePreferred\r\n
0xd000024a | DadStateDuplicate\r\n
0xd000024b | DadStateDeprecated\r\n
0xd000024c | SkipAsSourceSet\r\n
0xd000024d | SkipAsSourceReset\r\n
0xd000024e | TunnelSkipAsSourceSet\r\n
0xd000024f | TunnelSkipAsSourceReset\r\n
0xd0000250 | ZoneChange\r\n
0xd0000251 | NeighborAddition\r\n
0xd0000252 | NeighborDeletion\r\n
0xd0000253 | NeighborUnreachable\r\n
0xd0000254 | NeighborReachable\r\n
0xd0000255 | NeighborAddressUpdate\r\n
0xd0000256 | DeadRouteTimeout\r\n
0xd0000257 | DeadRouteProbeTimeout\r\n
0xd0000258 | AllRoutesDead\r\n
0xd0000259 | TlConfirmsForwardReachability\r\n
0xd000025a | DeadGatewayDetected\r\n
0xd000025b | RouterRedirect\r\n
0xd000025c | ProbeConnectionFailed\r\n
0xd000025d | ConfigurationChange\r\n
0xd000025e | Alive\r\n
0xd000025f | Dead\r\n
0xd0000260 | Probe\r\n
0xd0000261 | Disable\r\n
0xd0000262 | Enable\r\n
0xd0000263 | NotConfident\r\n
0xd0000264 | InvalidLoad\r\n
0xd0000265 | ConfidenceUpdate\r\n
0xd0000266 | TCP Fastopen\r\n
0xd0000267 | Init\r\n
0xd0000268 | StatusIndication\r\n
0xd0000269 | GlobalSetting\r\n
0xd000026a | Forwarding\r\n
0xd000026b | IncompatibleCallout\r\n
0xd000026c | RA DNS information change\r\n
0xd000026d | RA DNS entry added\r\n
0xd000026e | RA DNS entry expired by RA\r\n
0xd000026f | RA DNS entry expired by timer\r\n
0xd0000270 | RA DNS entry lifetime reset\r\n
0xd0000271 | RA DNS entry reordered\r\n
0xd0000272 | RA DNS entry deleted due to max limit\r\n
0xd0000273 | RA DNS entry lifetime updated\r\n
0xd0000274 | RA DNS ND entry ignored due to limit\r\n
0xd0000275 | RA DNS ND entry ignored due to memory failure\r\n
0xd0000276 | RA DNS ND entry ignored due to zero lifetime\r\n
0xd0000277 | RA DNS ND entries corrupted\r\n
0xd0000278 | RA DNS RouterContext init failed\r\n
0xd0000279 | Manual\r\n
0xd000027a | WellKnown\r\n
0xd000027b | DHCP\r\n
0xd000027c | RouterAdvertisement\r\n
0xd000027d | 6to4\r\n
0xd000027e | Avoid Unusable Destination\r\n
0xd000027f | Prefer Aoac Interface\r\n
0xd0000280 | Prefer Matching Scope\r\n
0xd0000281 | Avoid Deprecated Address\r\n
0xd0000282 | Prefer Matching Label\r\n
0xd0000283 | Prefer Internet Connected Interface\r\n
0xd0000284 | Prefer Higher Precedence\r\n
0xd0000285 | Prefer Longer Route Destination Prefix\r\n
0xd0000286 |  Prefer Native Transport(Physical Interface)\r\n
0xd0000287 | Prefer Lower Interface Metric\r\n
0xd0000288 | Prefer Smaller Scope\r\n
0xd0000289 | Prefer Same Address\r\n
0xd000028a | Prefer Appropriate Scope\r\n
0xd000028b | Avoid Deprecated Address\r\n
0xd000028c | Prefer Outgoing Interface\r\n
0xd000028d | Prefer Source Address Associated With Nexthop\r\n
0xd000028e | Prefer Temporary Address\r\n
0xd000028f | System Defined Preference\r\n
0xd0000290 | Prefer Source With Longer NextHop Prefix Match\r\n
0xd0000291 | Locality Metric\r\n
0xd0000292 | Prefer Longer Source/Destination Common Prefix Length\r\n
0xd0000293 | Order Unchanged (No Preference)\r\n
0xd0000294 | Send\r\n
0xd0000295 | Disconnect\r\n
0xd0000296 | Accept\r\n
0xd0000297 | Receive\r\n
0xd0000298 | ReceiveTcpDatagram\r\n
0xd0000299 | ReceiveDatagram\r\n
0xd000029a | RemoteDisconnect\r\n
0xd000029b | ReceiveControlMessage\r\n
0xd000029c | RespondDatagram\r\n
0xd000029d | BindEndpoint\r\n
0xd000029e | Listen\r\n
0xd000029f | AcceptComplete\r\n
0xd00002a0 | Connect\r\n
0xd00002a1 | ConnectComplete\r\n
0xd00002a2 | Raw\r\n
0xd00002a3 | ConnectRequest\r\n
0xd00002a4 | CreateEndpoint\r\n
0xd00002a5 | AcquirePort\r\n
0xd00002a6 | Offload\r\n
0xd00002a7 | SocketOption\r\n
0xd00002a8 | BindEndpointRequest\r\n
0xd00002a9 | Drop\r\n
0xd00002aa | Allow\r\n
0xd00002ab | Pend\r\n
0xd00002ac | DropAndSendIcmp\r\n
0xd00002ad | Allow\r\n
0xd00002ae | Deny\r\n
0xd00002af | Authorize\r\n
0xd00002b0 | RetryWithHint\r\n
0xd00002b1 | Reference\r\n
0xd00002b2 | Coalesced\r\n
0xd00002b3 | Dedicated\r\n
0xd00002b4 | FailureMemory\r\n
0xd00002b5 | FailurePlumbing\r\n
0xd00002b6 | NotFound\r\n
0xd00002b7 | Found\r\n
0xd00002b8 | Done\r\n
0xd00002b9 | Loopback Ethernet packet\r\n
0xd00002ba | Invalid Snap header\r\n
0xd00002bb | Invalid ethernet type\r\n
0xd00002bc | Invalid packet length\r\n
0xd00002bd | Header not contiguous\r\n
0xd00002be | Invalid destination type\r\n
0xd00002bf | Allocation failure\r\n
0xd00002c0 | Interface reference failure\r\n
0xd00002c1 | Packet provider reference failure\r\n
0xd00002c2 | Invalid LSO information\r\n
0xd00002c3 | Receive discarded\r\n
0xd00002c4 | Listener received a packet other than SYN\r\n
0xd00002c5 | Listener was paused\r\n
0xd00002c6 | Listener inpsection rejected\r\n
0xd00002c7 | SYN was not acked in SynTcb receive\r\n
0xd00002c8 | Received invalid ACK\r\n
0xd00002c9 | Received SYN+ACK with TFO cookie request\r\n
0xd00002ca | Received in-window SYN in unexpected TCP state\r\n
0xd00002cb | Received invalid ACK in SynRcvd state\r\n
0xd00002cc | Received SYN and other flags in Timewait state\r\n
0xd00002cd | Connection aborted\r\n
0xd00002ce | Bind endpoint was failed by InetInspect\r\n
0xd00002cf | Bind endpoint request was failed by InetInspect\r\n
0xd00002d0 | Listen was failed by InetInspect\r\n
0xd00002d1 | Listener receive was failed by InetInspect\r\n
0xd00002d2 | Accept complete was failed by InetInspect\r\n
0xd00002d3 | Create endpoint was failed by InetInspect\r\n
0xd00002d4 | Create connect endpoint was failed by InetInspect\r\n
0xd00002d5 | Create listen endpoint was failed by InetInspect\r\n
0xd00002d6 | Connect request was failed by InetInspect\r\n
0xd00002d7 | Connect request was failed by InetInspect\r\n
0xd00002d8 | Connect complete was failed by InetInspect\r\n
0xd00002d9 | Rate-limited connect complete was failed by InetInspect\r\n
0xd00002da | Connection was cancelled\r\n
0xd00002db | Connection aborted\r\n
0xd00002dc | Failed to send SYN packet\r\n
0xd00002dd | Failed to insert connection\r\n
0xd00002de | Delivery aborted on connection-reset or timeout\r\n
0xd00002df | An early disconnect injected\r\n
0xd00002e0 | Connection was aborted by the system\r\n
0xd00002e1 | Network name was deleted\r\n
0xd00002e2 | Incompatible next hop\r\n
0xd00002e3 | SegmentSize is larger than MTU\r\n
0xd00002e4 | Raw listeners on path\r\n
0xd00002e5 | IP extension headers present\r\n
0xd00002e6 | Exceeds hardware capabilities\r\n
0xd00002e7 | Incompatible inspection callout\r\n
0xd00002e8 | Unknown\r\n
0xd00002e9 | Connected\r\n
0xd00002ea | Disconnected\r\n
0xd00002eb | IPPROTO_IP\r\n
0xd00002ec | IPPROTO_IPV6\r\n
0xd00002ed | SOL_SOCKET\r\n
0xd00002ee | IP_OPTIONS/IPV6_HOPOPTS\r\n
0xd00002ef | IP_HDRINCL/IPV6_HDRINCL\r\n
0xd00002f0 | IP_TOS\r\n
0xd00002f1 | IP_TTL/IPV6_UNICAST_HOPS\r\n
0xd00002f2 | IP_MULTICAST_IF/IPV6_MULTICAST_IF\r\n
0xd00002f3 | IP_MULTICAST_TTL/IPV6_MULTICAST_HOPS\r\n
0xd00002f4 | IP_MULTICAST_LOOP/IPV6_MULTICAST_LOOP\r\n
0xd00002f5 | IP_ADD_MEMBERSHIP/IPV6_ADD_MEMBERSHIP\r\n
0xd00002f6 | IP_DROP_MEMBERSHIP/IPV6_DROP_MEMBERSHIP\r\n
0xd00002f7 | IP_DONTFRAGMENT/IPV6_DONTFRAG\r\n
0xd00002f8 | IP_ADD_SOURCE_MEMBERSHIP\r\n
0xd00002f9 | IP_DROP_SOURCE_MEMBERSHIP\r\n
0xd00002fa | IP_BLOCK_SOURCE\r\n
0xd00002fb | IP_UNBLOCK_SOURCE\r\n
0xd00002fc | IP_PKTINFO/IPV6_PKTINFO\r\n
0xd00002fd | IP_HOPLIMIT/IP_RECVTTL/IPV6_HOPLIMIT\r\n
0xd00002fe | IP_RECEIVE_BROADCAST\r\n
0xd00002ff | IPV6_PROTECTION_LEVEL\r\n
0xd0000300 | IP_RECVIF/IPV6_RECVIF\r\n
0xd0000301 | IP_RECVDSTADDR/IPV6_RECVDSTADDR\r\n
0xd0000302 | IP_FLIST/IPV6_FLIST\r\n
0xd0000303 | IP_ADD_IFLIST/IPV6_ADD_FLIST\r\n
0xd0000304 | IP_DEL_IFLIST/IPV6_DEL_IFLIST\r\n
0xd0000305 | IP_RTHDR/IPV6_RTHDR\r\n
0xd0000306 | IP_UNICAST_IF/IPV6_UNICAST_IF\r\n
0xd0000307 | IP_RECVRTHDR/IPV6_RECVRTHDR\r\n
0xd0000308 | IP_RECVTCLASS/IP_RECVTOS/IPV6_RECVTCLASS\r\n
0xd0000309 | MCAST_JOIN_GROUP\r\n
0xd000030a | MCAST_LEAVE_GROUP\r\n
0xd000030b | MCAST_BLOCK_SOURCE\r\n
0xd000030c | MCAST_UNBLOCK_SOURCE\r\n
0xd000030d | MCAST_JOIN_SOURCE_GROUP\r\n
0xd000030e | MCAST_LEAVE_SOURCE_GROUP\r\n
0xd000030f | IP_ORIGINAL_ARRIVAL_IF/IPV6_ORIGINAL_ARRIVAL_IF\r\n
0xd0000310 | IP_ECN/IPV6_ECN\r\n
0xd0000311 | IP_PKTINFO_EX/IPV6_PKTINFO_EX\r\n
0xd0000312 | IP_WFP_REDIRECT_RECORDS/IPV6_WFP_REDIRECT_RECORDS\r\n
0xd0000313 | IP_WFP_REDIRECT_CONTEXT/IPV6_WFP_REDIRECT_CONTEXT\r\n
0xd0000314 | IP_MTU_DISCOVER\r\n
0xd0000315 | IP_NRT_INTERFACE/IPV6_NRT_INTERFACE\r\n
0xd0000316 | IP_RECVERR/IPV6_RECVERR\r\n
0xd0000317 | SIO_GET_INTERFACE_LIST\r\n
0xd0000318 | SIO_GET_MULTICAST_FILTER\r\n
0xd0000319 | SIO_SET_MULTICAST_FILTER\r\n
0xd000031a | SIOCSMSFILTER\r\n
0xd000031b | SIOCGMSFILTER\r\n
0xd000031c | SIO_MULTIPOINT_LOOPBACK\r\n
0xd000031d | SIO_MULTICAST_SCOPE\r\n
0xd000031e | SIO_RCVALL\r\n
0xd000031f | SIO_RCVALL_MCAST\r\n
0xd0000320 | SIO_RCVALL_IGMPMCAST\r\n
0xd0000321 | SIO_RCVALL_MCAST_IF\r\n
0xd0000322 | SIO_RCVALL_IF\r\n
0xd0000323 | SIO_ADDRESS_LIST_SORT\r\n
0xd0000324 | join group\r\n
0xd0000325 | leave group\r\n
0xd0000326 | join group and add source\r\n
0xd0000327 | leave group and drop source\r\n
0xd0000328 | block source\r\n
0xd0000329 | unblock source\r\n
0xd000032a | set filter\r\n
0xd000032b | MLD level does not match protocol\r\n
0xd000032c | Invalid multicast address\r\n
0xd000032d | Invalid multicast source address\r\n
0xd000032e | Group already exists\r\n
0xd000032f | No existing state for group\r\n
0xd0000330 | Group is in exclude mode\r\n
0xd0000331 | No existing state for group or group is in exclude mode\r\n
0xd0000332 | No existing state for group or group is in include mode\r\n
0xd0000333 | Failed to set the state for the group\r\n
0xd0000334 | Failed to create the state for the group\r\n
0xd0000335 | Failed to modify the state for the group\r\n
0xd0000336 | Successfully created multicast session state\r\n
0xd0000337 | Another duplicate multicast session state exists, so no need to create a new one\r\n
0xd0000338 | Successfully added sources to multicast group\r\n
0xd0000339 | Successfully removed sources from multicast group\r\n
0xd000033a | Updated multicast group state; will send report\r\n
0xd000033b | Not modifying multicast group state\r\n
0xd000033c | Updated multicast discovery version\r\n
0xd000033d | Failed to create multicast session state when updating the multicast group\r\n
0xd000033e | Failed to create multicast session state from callback\r\n
0xd000033f | Failed to create multicast session state when searching for the interface\r\n
0xd0000340 | Failed to create multicast session state because access is denied\r\n
0xd0000341 | Failed to create multicast session state when adding sources to the session state\r\n
0xd0000342 | Failed to create multicast session state when creating the address\r\n
0xd0000343 | Failed to add sources to multicast group\r\n
0xd0000344 | Failed to modify multicast session state because access is denied\r\n
0xd0000345 | WFP context to the fragment\r\n
0xd0000346 | WFP context from the fragment to the reassembly context\r\n
0xd0000347 | leave\r\n
0xd0000348 | join\r\n
0xd0000349 | acquire\r\n
0xd000034a | release\r\n
0xd000034b | Unknown\r\n
0xd000034c | DAD\r\n
0xd000034d | Router solicitation\r\n
0xd000034e | WOL address pattern\r\n
0xd000034f | WOL TCP pattern\r\n
0xd0000350 | WOL local port pattern\r\n
0xd0000351 | Reassembly is prohibited\r\n
0xd0000352 | Fragment was filtered out\r\n
0xd0000353 | Out of memory\r\n
0xd0000354 | Protocol does not match\r\n
0xd0000355 | Fragment causes total packet length to exceed maximum payload size\r\n
0xd0000356 | Packet length does not properly align\r\n
0xd0000357 | The next header has the wrong IP option\r\n
0xd0000358 | Received mixed IPSec and non-IPSec fragments\r\n
0xd0000359 | Received zero length fragment\r\n
0xd000035a | Duplicate fragment\r\n
0xd000035b | Fragment falls beyond the data length\r\n
0xd000035c | Received duplicate or unsupported fragment\r\n
0xd000035d | End of list\r\n
0xd000035e | No operation\r\n
0xd000035f | Security\r\n
0xd0000360 | Loose source route\r\n
0xd0000361 | Timestamp\r\n
0xd0000362 | Record route\r\n
0xd0000363 | Struct source route\r\n
0xd0000364 | Stream ID\r\n
0xd0000365 | Router alert\r\n
0xd0000366 | Multi-destination\r\n
0xd0000367 | Single byte pad\r\n
0xd0000368 | Multiple byte pad\r\n
0xd0000369 | Tunnel limit\r\n
0xd000036a | Router alert\r\n
0xd000036b | Jumbogram\r\n
0xd000036c | NSAP address\r\n
0xd000036d | Message length is not long enough\r\n
0xd000036e | Data length must be greater than or equal to the size of the message header\r\n
0xd000036f | Invalid message type\r\n
0xd0000370 | Invalid message level\r\n
0xd0000371 | Invalid data length for this option\r\n
0xd0000372 | Invalid hop limit value\r\n
0xd0000373 | Invalid type of service value\r\n
0xd0000374 | Invalid hop-by-hop options\r\n
0xd0000375 | Invalid routing header\r\n
0xd0000376 | Invalid ECN field value\r\n
0xd0000377 | Invalid option\r\n
0xd0000378 | Option length is either too small or too large\r\n
0xd0000379 | Option length must be greater than or equal to the size of the option header\r\n
0xd000037a | The length of the supplied buffer is smaller than the option length\r\n
0xd000037b | The option length is smaller than the minimum length for this option\r\n
0xd000037c | The option list must have space for an integral, non-zero number of entries\r\n
0xd000037d | The data alignment of the option payload is invalid\r\n
0xd000037e | Invalid flags\r\n
0xd000037f | Multi-byte options can only occur once, or the combination of options is invalid\r\n
0xd0000380 | Invalid pointer value\r\n
0xd0000381 | Invalid address value\r\n
0xd0000382 | Invalid option\r\n
0xd0000383 | Option length is either too small or too large\r\n
0xd0000384 | Option length must be greater than or equal to the size of the option header\r\n
0xd0000385 | The length of the supplied buffer is smaller than the option length\r\n
0xd0000386 | The option list must have space for an integral, non-zero number of entries\r\n
0xd0000387 | Invalid address value\r\n
0xd0000388 | This option cannot be specified by the user\r\n
0xd0000389 | Message length is not long enough\r\n
0xd000038a | Data length must be greater than or equal to the size of the message header\r\n
0xd000038b | Invalid message level\r\n
0xd000038c | Invalid IP_PKTINFO_EX option length\r\n
0xd000038d | Invalid option length\r\n
0xd000038e | Interface not found\r\n
0xd000038f | Scope ID does not match the scope ID for the interface\r\n
0xd0000390 | Failed to find or create address to return\r\n

### 10.0.22000.132

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | TCP: endpoint %2 (Family=%3, PID=%4) created with status = %1.\r\n
0xb00003ea | TCP: Tcb %1 (local=%3 remote=%5) requested to connect.\r\n
0xb00003eb | TCP: Inspect Connect has been completed on Tcb %1 with status = %2.\r\n
0xb00003ec | TCP: Tcb %1 is going to output SYN with ISN = %2, RcvWnd = %3, RcvWndScale = %4.\r\n
0xb00003ed | TCP: endpoint bind failed: address %2 cannot be resolved (%3).\r\n
0xb00003ee | TCP: endpoint (sockaddr=%2) bind failed: port-acquisition status = %3.\r\n
0xb00003ef | TCP: endpoint (sockaddr=%2) bind failed: inspection status = %3.\r\n
0xb00003f0 | TCP: endpoint (sockaddr=%2) bound.\r\n
0xb00003f1 | TCP: endpoint (sockaddr=%2) closed.\r\n
0xb00003f2 | TCP: endpoint (Family=%6 PID=%4) create failed: address family not attached.\r\n
0xb00003f3 | TCP: endpoint (Family=%6 PID=%4) create failed: compartment %5 not found.\r\n
0xb00003f4 | TCP: endpoint (Family=%6 PID=%4) create failed: inspection status %3.\r\n
0xb00003f5 | TCP: endpoint (Family=%6 PID=%4) created.\r\n
0xb00003f6 | TCP: listener (local=%2 remote=%4) accept failed: Route lookup status = %5, TCB = %8.\r\n
0xb00003f7 | TCP: listener (local=%3 remote=%5) accept failed: connection insertion. Duplicate TCB = %1.\r\n
0xb00003f8 | TCP: listener (local=%2 remote=%4) accept failed: client rejection status = %5.\r\n
0xb00003f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6.\r\n
0xb00003fa | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: address family not attached.\r\n
0xb00003fb | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: compartment %7 not found.\r\n
0xb00003fc | TCP: connection %8 (local=%2 remote=%4 PID=%6) connect failed: inspection status = %5.\r\n
0xb00003fd | TCP: connection %8 (local=%2 remote=%4) connect failed: route lookup status = %5.\r\n
0xb00003fe | TCP: Bypass rate limiting since flag is set on path %5 (local=%2 remote=%4) \r\n
0xb00003ff | TCP: Charge rate limiting quota and set rate limiting flag for path %5 (local=%2 remote=%4) \r\n
0xb0000400 | TCP: connection %8 (local=%2 remote=%4) deferred.\r\n
0xb0000401 | TCP: %6 rate-limiting paths %3 backlogged connections.\r\n
0xb0000402 | TCP: Release and set rate limiting flag on path %5 (local=%2 remote=%4) \r\n
0xb0000403 | TCP: connection %8 (local=%2 remote=%4) released.\r\n
0xb0000404 | TCP: Clear rate limiting flag on path %5 (local=%2 remote=%4) since connection is cancelled.\r\n
0xb0000405 | TCP: connection %8 (local=%2 remote=%4) connect failed: connection cancelled.\r\n
0xb0000406 | TCP: connection (local=%2 remote=%4) connect failed: connection insertion status = %5.\r\n
0xb0000407 | TCP: connection %8 (local=%2 remote=%4) connect proceeding.\r\n
0xb0000408 | TCP: connection %8 (local=%2 remote=%4) released due to cancel.\r\n
0xb0000409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6.\r\n
0xb000040a | TCP: connection %8 (local=%2 remote=%4) connect attempt failed with status = %5.\r\n
0xb000040b | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-complete inspect status = %5.\r\n
0xb000040c | TCP: ApplySynOptions, failed to create session state with status = %5, TCB = %8.\r\n
0xb000040d | TCP: ApplySynOptions, failed to update DF with status = %5, TCB = %8.\r\n
0xb000040e | TCP: connection %8 (local=%2 remote=%4) close issued.\r\n
0xb000040f | TCP: connection %8 (local=%2 remote=%4) abort issued.\r\n
0xb0000410 | TCP: connection %8 (local=%2 remote=%4) abort completed.\r\n
0xb0000411 | TCP: Injecting disconnect on a shutdown TCB failed. TCB = %1.\r\n
0xb0000412 | TCP: connection disconnect %3, length=%1.\r\n
0xb0000413 | TCP: connection %8 (local=%2 remote=%4) disconnect completed.\r\n
0xb0000414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6.\r\n
0xb0000415 | TCP: connection %8 (local=%2 remote=%4) connect failed: connect-request timeout expired.\r\n
0xb0000416 | TCP: connection %8 (local=%2 remote=%4) terminating: retransmission timeout expired.\r\n
0xb0000417 | TCP: connection %8 (local=%2 remote=%4) terminating: keep-alive timeout expired.\r\n
0xb0000418 | TCP: connection %8 (local=%2 remote=%4) terminating: disconnect timeout expired.\r\n
0xb0000419 | TCP: connection %8 (local=%2 remote=%4) connect failed: extended statistics status = %5.\r\n
0xb000041a | TCP: connection %8 (local=%2 remote=%4) connect failed: port-acquisition status = %5.\r\n
0xb000041b | TCP: connection %4 transition from %1 to %2, SndNxt = %3.\r\n
0xb000041c | TCP: Process with PID = %1 reserved %4 ports starting at %3.\r\n
0xb000041d | TCP: Process with PID = %1 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb000041e | TCP: Process with PID = %1 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb000041f | TCP: entering SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000420 | TCP: reasembly rate-limiting violated %2 times since boot.\r\n
0xb0000421 | TCP: connection rate-limiting violated %4 times since boot.\r\n
0xb0000422 | TCP: land attack has dropped %5 packets since boot.\r\n
0xb0000423 | TCP: low memory state detected. LowMemoryEvent =%3 LowPagedPoolEvent = %4.\r\n
0xb0000424 | TCP: leaving low memory state. HighMemoryEvent = %1 HighPagedPoolEvent = %2.\r\n
0xb0000425 | TCP: address family %2 added to interface %1.\r\n
0xb0000426 | TCP: address family %2 removed from interface %1.\r\n
0xb0000427 | TCP: leaving SYN attack resistance mode, Syn Attacks Detected = %1.\r\n
0xb0000428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms.\r\n
0xb0000429 | TCP: Connection %1 stopping %2 timer. \r\n
0xb000042a | TCP: Connection %1 %2 timer has expired.\r\n
0xb000042b | TCP: ISB changed to %1. CWnd = %2 SndWnd = %3 SendAvailable = %4 SSThresh = %5.\r\n
0xb000042c | TCP: moving RSS indirection table index %6 from processor %1 to processor %3.\r\n
0xb000042d | TCP: connection %1: Timeout Event updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb000042e | TCP: connection %1:  Rtt sample recorded %4.\r\n
0xb000042f | TCP: connection %1: Cumulative ACK updated cwnd = %2.\r\n
0xb0000430 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3.\r\n
0xb0000431 | TCP: connection %1: Sent data with number of bytes = %5 and Sequence number = %6.\r\n
0xb0000432 | TCP: connection %1: Received data with number of bytes = %2. ThSeq = %3.\r\n
0xb0000433 | TCP: connection %1: ECN Echo updated cwnd = %2 and updated ssthresh = %3. SndUna = %4, Mss = %5, ThAck = %6.\r\n
0xb0000434 | TCP: connection %1: Spurious timeout with SndUna = %7.\r\n
0xb0000435 | TCP: connection %1: Send Retransmit round with SndUna = %6, Round = %8, SRTT = %9, RTO = %10.\r\n
0xb0000436 | TCP: connection %1: Entered loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000437 | TCP: connection %1: Leaving loss recovery phase with SndUna = %2 and SndMax = %3.\r\n
0xb0000438 | TCP: connection %1 entering SACK mode with SndUna = %2.\r\n
0xb0000439 | TCP: connection %1 leaving SACK mode with SndUna = %2.\r\n
0xb000043a | TCP: connection %1 entering Congestion Avoidance Phase with cwnd = %2 and ssthresh = %3.\r\n
0xb000043c | TCP: connection %1 entered BH, BH MSS %2, original MSS %3.\r\n
0xb000043d | TCP: connection %1 Exiting BH due to %4, BH mss %2, Original MSS %3.\r\n
0xb000043e | TCP: connection %1 not entering BH due to %4.\r\n
0xb000043f | TCP: connection %1 spurious RTO detection initiated at %7.\r\n
0xb0000440 | TCP: connection %1 spurious RTO detection terminated at %7.\r\n
0xb0000441 | TCP: active connect failed (family=%2) connect-complete inspection failed: status = %3.\r\n
0xb0000442 | TCP: TcpReleaseIndicationList: Nbl = %1.\r\n
0xb0000443 | TCP: connection %1 posted an average of %5 bytes per send.\r\n
0xb0000444 | TCP: connection (local=%2 remote=%4) starting receive window auto-tuning.\r\n
0xb0000445 | TCP: connection (local=%2 remote=%4) ending receive window auto-tuning.\r\n
0xb0000446 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because fine-grained RTT estimation could not be started.\r\n
0xb0000447 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because receiver bandwidth estimation could not be started.\r\n
0xb0000448 | TCP: connection (local=%2 remote=%4) failed to enter auto-tuning because of receive window tuning allocation failure.\r\n
0xb0000449 | TCP: connection (local=%2 remote=%4) auto-tuner adjusted receive buffer size to %5 bytes.\r\n
0xb000044a | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %4 and new SRTT = %9.\r\n
0xb000044b | TCP: connection %5: Connection State = %1, Offload State = %2. SndNxt = %3, RcvNxt = %4. NdisStatus = %6.\r\n
0xb000044c | TCP: SWS avoidance began on connection %1. Timer set for %2 ms. BytesToSend = %3, SendAvailable = %4, Cwnd = %5, MaxSndWnd = %6.\r\n
0xb000044d | TCP: SWS avoidance ended on connection %1.\r\n
0xb000044e | TCP: connection %1 send: Beginning zero-window probing with SndUna = %2.\r\n
0xb000044f | TCP: connection %1 send: Leaving zero-window probing with SndUna = %2.\r\n
0xb0000450 | TCP: Option %2 is going to be set for connection %1.\r\n
0xb0000451 | TCP: Socket Option %3 is going to be set for connection %1.\r\n
0xb0000452 | IP: Disconnecting interface %1, trace = %2.\r\n
0xb0000453 | TCPIP: Module %1 started.\r\n
0xb0000454 | TCPIP: Module %1 stopped.\r\n
0xb0000455 | TCPIP: Failure allocating %1.\r\n
0xb0000456 | TCP: Global parameters updated for Address Family %1: EnablePMtuDiscovery = %2, UseRfc1122UrgentPointer = %3, DisableTaskOffload = %4, DisableTcpChimneyOffload = %5, DisableRss = %6, EnablePMtuBHDetect = %7, EcnCapability = %8, MaxDataRetransmissions = %9, KeepAliveTime = %10, KeepAliveInterval = %11, TimedWaitDelay = %12, SillyWindowTimeout = %13, FinWait2Timeout = %14, CongestionAlgorithm = %15, UseRfc1323Timestamps = %16, AutoTuningLevelLocal = %17, AutoTuningLevelGroupPolicy = %18.\r\n
0xb0000457 | TCP: Connection %1 Large Send Offload, Bytes in segment = %2 and Bytes remaining = %3.\r\n
0xb0000458 | TCP: Connection %1 status changed to %2.\r\n
0xb0000459 | TCP: Connection %1 status = %2, Interface = %3, PMax = %4.\r\n
0xb000045a | IP: DAD successful for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045b | IP: DAD failed for IP address = %7 %9 %8 on interface = %1, protocol = %2, DL address of packet = %5.\r\n
0xb000045c | IP: DAD started for IP address = %7 %9 %8 on interface = %1, protocol = %2.\r\n
0xb000045d | TCP: listener (sockaddr=%3 PID=%5) activation failed: address family not attached.\r\n
0xb000045e | TCP: listener %1 (family=%7 PID=%5) activation failed: compartment %6 not found. Status=%4.\r\n
0xb000045f | TCP: listener %1 (family=%7 PID=%5) activation failed: inspection status=%4.\r\n
0xb0000460 | TCP: listener %1 (sockaddr=%3) activation failed: inspection status=%4.\r\n
0xb0000461 | TCP: listener %1 (sockaddr=%3) bind failed: port-acquisition status=%4.\r\n
0xb0000462 | TCP: listener %1 (family=%7 PID=%5) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0000463 | TCP: listener %1 (sockaddr=%3) activated.\r\n
0xb0000464 | TCP: listener %1 (sockaddr=%3) unbound.\r\n
0xb0000467 | IP: IP address = %7 %9 %8 added on interface = %1, Protocol = %2.\r\n
0xb0000468 | IP: IP address = %7 %9 %8 deleted on interface = %1, Protocol = %2.\r\n
0xb000046a | Framing: Interface %1 Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0000470 | Framing: NDIS pause event on interface %1.\r\n
0xb0000471 | Framing: NDIS restart event on interface %1.\r\n
0xb0000472 | IP: IP address = %7 %9 %8 state changed to Preferred. Interface = %1.\r\n
0xb0000473 | IP: IP address = %7 %9 %8 state changed to Non-preferred. Interface = %1. DadState = %3.\r\n
0xb0000478 | IP: Interface %1 property change. Advertise= %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7.\r\n
0xb0000479 | IP: Route %1 created on interface %2. Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047a | IP: Route %1 deleted on interface %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8.\r\n
0xb000047b | IP: Route %1 property change. Interface = %2, Protocol = %5, DestinationPrefix = %16 %18 %7 /%6, Nexthop = %17 %18 %8. Properties: ValidLifetime = %9, PreferredLifetime = %10, Metric = %11, Loopback = %12, AutoconfigureAddress = %13, Publish = %14, Immortal = %15.\r\n
0xb000047c | IP: Neighbor unreachable. Interface %1, IP address = %5 %7 %6.\r\n
0xb000047d | IP: Neighbor reachable. Interface %1, IP address = %5 %7 %6, DlAddress = %3.\r\n
0xb000047e | TCP: CTCP DataTransferTimeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb000047f | TCP: CTCP Cumulative Ack event Connection %1, sequence = %6, CWnd = %2, DWnd = %11, BaseRtt = %12.\r\n
0xb0000480 | TCP: CTCP Duplicate Ack event. Connection %1, sequence = %6, SndUna = %7, CWnd = %2, DWnd = %11, BaseRtt = %12, DupAckCount = %13.\r\n
0xb0000481 | TCP: CTCP Send event. Connection %1, sequence = %6, length = %5.\r\n
0xb0000482 | TCP: CTCP ECN event. Connection %1, CWnd %2, SndUna = %4, Mss = %5, DWnd = %7, BaseRtt = %8.\r\n
0xb0000483 | TCP: CTCP Spurious timeout event. Connection %1, CWnd = %2, SsThresh = %3.\r\n
0xb0000484 | TCP: connection %1, delivery %2, Request %3  posted for %4 bytes, flags = %5. RcvNxt = %10.\r\n
0xb0000485 | TCP: connection %1 delivery %2 indicated %4 bytes accepted %6 bytes, status = %7. RcvNxt = %10.\r\n
0xb0000486 | TCP: connection %1 delivery %2 satisfied %4 bytes %6 requested. IsFullySatisfied = %9. RcvNxt = %10.\r\n
0xb0000487 | TCP: connection %1 send %2 %3 bytes at %4.\r\n
0xb0000488 | TCP: connection %1 send transmitted %3 bytes at %4.\r\n
0xb0000489 | TCP: connection %1 send advance %3 bytes at %4.\r\n
0xb000048a | TCP: CTcp: Connection %1 Delay window has not kicked in.\r\n
0xb000048b | TCP: CTcp: Allocated blocks: %1; Assigned blocks: %2.\r\n
0xb000048c | TCP: CTcp: Connection %1, DWnd = %2 (Prev = %3), BaseRtt = %4, AverageRtt = %5, CWnd =%6, DiffWnd = %7, DWnd increment = %8.\r\n
0xb000048d | TCP: CTcp: Gamma Autotuning: Connection %1 Updated Gamma %2, Average backlog %3, Average backlog across LFPs %4.\r\n
0xb000048e | TCP: connection %1 SRTT measurement started (seq = %2, tick = %3).\r\n
0xb000048f | TCP: connection %1 SRTT measurement complete (tick = %3, sample = %4 ms, new srtt = %5 ms).\r\n
0xb0000490 | TCP: connection %1: SRTT measurement cancelled.\r\n
0xb0000491 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) sending %2 messages and a total of %3 bytes. PID = %8.\r\n
0xb0000492 | UDP: endpoint %1 (LocalAddress = %5, RemoteAddress = %7) delivering %3 bytes. PID = %8.\r\n
0xb0000493 | TCP: connection %1 delivery %2 flushing %4 bytes %6 requested status = %7.\r\n
0xb0000494 | TCP: Injecting receive on a shutdown TCB failed. TCB = %1.\r\n
0xb0000495 | TCP: connection %1 delivery %2 injecting %4 bytes delta %6, IsUrgentDelivery = %8.\r\n
0xb0000496 | TCP: Injecting fin on a shutdown TCB failed. TCB = %1.\r\n
0xb0000497 | TCP: connection %1 delivery %2 accepting %4 bytes. RcvNxt = %10.\r\n
0xb0000498 | TCP: connection %1 delivery %2 delivering FIN. RcvNxt = %10.\r\n
0xb000049a | TCP: connection %1 delivery %2 pushing %4 bytes %6 requested. Delayed push = %9.\r\n
0xb000049c | TCP: Injecting fin on TCB completed. TCB = %1, Processor = %4.\r\n
0xb000049d | TCP: connection %1 delivery %2 urgent boundary completing %4 bytes %6 requested.\r\n
0xb000049e | TCP: connection %1 (local=%3 remote=%5): initiating SYN/RST validation.\r\n
0xb000049f | TCP: connection %1 (local=%3 remote=%5) connect failed: received RST.\r\n
0xb00004a0 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received RST.\r\n
0xb00004a1 | TCP: connection %1 (local=%3 remote=%5) connection terminated: received SYN in state %6.\r\n
0xb00004a2 | TCP: connection %1 (local=%3 remote=%5) retransmitting connect attempt, RexmitCount = %7.\r\n
0xb00004a3 | TCP: connection %1 (local=%3 remote=%5) retransmitting data, RexmitCount = %7.\r\n
0xb00004a4 | TCP: connection %1 send keep-alive at SndUna = %2.\r\n
0xb00004a5 | TCP: connection %1, delivery %2: delivery state changed from %3 to %4.\r\n
0xb00004a6 | TCP: connection %1 delivery %2 dropping data. TotalBytesEnqueued = %4. Length = %6. RcvNxt = %10.\r\n
0xb00004a7 | TCP: endpoint/connection %1 acquired port number %2.\r\n
0xb00004a8 | TCP: connection %1 attempted to acquire weak reference on port number %2 inherited from endpoint %4. Successful = %3.\r\n
0xb00004a9 | TCP: endpoint/connection %1 released port number %2. WeakReference = %3.\r\n
0xb00004aa | TCP: endpoint/connection %1 replaced base endpoint %4 and acquired reference to port number %2.\r\n
0xb00004ab | TCP: Portpool assigned port number %2 with weak references due to port exhaustion.\r\n
0xb00004ac | TCP: connection %1 BH receive ACK for full size seq. Seq = %2. IsSack = %5.\r\n
0xb00004ad | TCP: connection %1 flushed SACK state at SndUna = %2. Reason: %4.\r\n
0xb00004ae | TCP: Connection %1 entering reassembly at RcvNxt = %2.\r\n
0xb00004af | TCP: Connection %1 leaving reassembly at RcvNxt = %2.\r\n
0xb00004b0 | TCP: connection %8 (local=%2 remote=%4) terminating: Zero window probe timeout expired.\r\n
0xb00004b1 | TCP: connection %8 (local=%2 remote=%4) terminating: FIN-WAIT-2 timeout expired.\r\n
0xb00004b2 | IP: Interface rundown: Index = %1, Linkspeed = %2 bps, PhysicalMediumType = %7, IP Address = %4 %3 %6.\r\n
0xb00004b3 | IP: Interface Index = %1, Linkspeed changed to %2 bps, PhysicalMediumType = %7.\r\n
0xb00004b4 | TCP: Connection %1 flushing reassembly state at RcvNxt = %2. Reason = %4.\r\n
0xb00004b5 | TCPIP: NBL %1 fell off the receive fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b6 | TCPIP: NBL %1 fell off the send fast path, Reason: %10. Protocol = %2, Family = %3, Number of NBLs = %11. SourceAddress = %4 %12 %7. DestAddress = %5 %12 %9.\r\n
0xb00004b7 | TCP: WSD - %1 Status: %2.\r\n
0xb00004b9 | TCP: WSD - TCB %2 will use a highly restricted window scale factor due to a %1.\r\n
0xb00004bb | TCP: WSD - Entry (%2, %3) moved from %4 to %5 due to %1.\r\n
0xb00004bc | TCP: WSD - Profile: %1 State: %2 Qualified: %3 EreQualified: %4.\r\n
0xb00004bd | TCP: WSD - Enabled moved from %1 to %2. Threshold moved from  %3 to %4.\r\n
0xb00004be | TCPIP: Transport (Protocol %1, AddressFamily = %2) dropped %8 packet(s) with Local = %4, Remote = %6. Reason = %7.\r\n
0xb00004bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s). SourceAddress = %3 %11 %6. DestAddress = %4 %11 %8. Reason = %9.\r\n
0xb00004c0 | TCP: MPP NPP Evaluation PhysicalPages = %1 NonPagedPoolPages = %2 Current = %3 Peak = %4 Low = %5 High = %6.\r\n
0xb00004c1 | TCP: MPP: Episode started. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Current = %5 Low = %6 Reentry = %7.\r\n
0xb00004c2 | TCP: MPP: Episode ended. LowNppEventState = %1 HighNppEventState = %2 EpisodeStartTick = %3 EpisodeStopTick = %4 Reentry = %5.\r\n
0xb00004c3 | TCP: MPP: Epoch %1 started. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 -> %7 TcbKillRate = %8 -> %9 CurrentWatermark = %10.\r\n
0xb00004c4 | TCP: MPP: Epoch %1 ended. LowNppEventState = %2 HighNppEventState = %3 EpochStartTick = %4 EpochStopTick = %5 SynDropRate = %6 TcbKillRate = %7 Current = %8.\r\n
0xb00004c5 | TCP: Connection %1 restarting Cwnd. Old Cwnd = %2, New Cwnd = %3, Processor = %4, CurrentTick = %5, IdleTick = %6, Rto = %7.\r\n
0xb00004c6 | TCP: Connection %1 adjust InitalCwnd. Cwnd = %2, New Initial Cwnd = %3 MSS.\r\n
0xb00004c7 | TCP: Connection %1 committed TemplateType = %2. MinRto = %3 msec, EnableCwndRestart = %4, InitialCwnd = %5 MSS, CongestionAlgorithm = %6, MaxDataRetransmissions = %7, DelayedAckTicks = %8 msec, DelayedAckFrequency = %9, RACK enabled = %10, Tail Loss Probe enabled = %11.\r\n
0xb00004c8 | TCP: Connection %1 template changed. New template=%2. Context=%3.\r\n
0xb00004c9 | TCP: connection %1: End of a round, SndRound = %2, Bytes sent = %3. Bytes marked = %4, ThAck = %5, updated EcnAlpha = %6.\r\n
0xb00004ca | TCP: interface %1: RSC state changed, IPV4 State = %2, IPV4 Failure Reason = %3, IPV6 State = %4, IPV6 Failure Reason = %5, Event = %6.\r\n
0xb00004cb | TCP: connection %1: RSC SCU received. CoalescedSegCount = %2, DupAckCount = %3, RscTcpTimestampDelta = %4, HeaderFlags = %5, EcnCePresent = %6.\r\n
0xb00004cc | TCPIP: TCB %1 does not take fast path, Cause: %2.\r\n
0xb00004cd | TCP: Connection %1 send queue is idle. Cwnd = %2, Processor = %4, CurrentTick = %5, IdleTick = %6.\r\n
0xb00004ce | RSS: %3 notification for %2 on interface %1.\r\n
0xb00004cf | RSS: %4 notification for adapter %1.\r\n
0xb00004d0 | RSS: %4 reference on adapter %1.\r\n
0xb00004d1 | RSS: adapter %1 with capabilities %2 and %4 receive queues.\r\n
0xb00004d2 | RSS: adapter %1 processor group %2 maximum processors %3 processor affinity %4.\r\n
0xb00004d3 | RSS: assigning processor %2 from adapter %3 to %1.\r\n
0xb00004d4 | RSS: unassigning processor %2 from adapter %1.\r\n
0xb00004d5 | RSS: adapter %1 reassigning indirection entry %2 from processor %3 to %4.\r\n
0xb00004d6 | RSS: adapter %1 removing processor %2 from its indirection table.\r\n
0xb00004d7 | RSS: adapter %1 changing %2 to %3.\r\n
0xb00004d8 | RSS: Failed to %2 on IfIndex %1: %3\r\n
0xb00004d9 | RSS: bind completed successfully for %2 on interface %1.\r\n
0xb00004da | RSS: bind completed successfully for adapter %1.\r\n
0xb00004db | RSS: adapter %1 not supported.\r\n
0xb00004dc | RSS: adapter %1 indirection table initialized on group %4 with processor set %5.\r\n
0xb00004dd | RSS: Rundown: interface %1 with adapter %2 at port %3.\r\n
0xb00004de | RSS: Rundown: adapter %1 hash info %2 maximum processors %3 group %4 affinity %5 active processors %6 active mode: %7.\r\n
0xb00004df | RSS: interface %1 support: %2.\r\n
0xb00004e0 | NDKPI Create CQ: RequestContext %6 Adapter %1 CqDepth %2 CqNotificationContext %3 AffinityMask %4 AffinityGroup %5\r\n
0xb00004e1 | NDKPI Create Completion: RequestContext %1 Status %2 (%4) %5 %3\r\n
0xb00004e2 | NDKPI Close %2: RequestContext %3 %2 %1\r\n
0xb00004e3 | NDKPI Close Completion: RequestContext %1 (%2)\r\n
0xb00004e4 | NDKPI Resize CQ: RequestContext %3 CQ %1 CqDepth %2\r\n
0xb00004e5 | NDKPI Request Completion: RequestContext %1 Status %2 (%3)\r\n
0xb00004e6 | NDKPI Arm CQ: CQ %1 %2\r\n
0xb00004e7 | NDKPI Result %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4\r\n
0xb00004e8 | NDKPI Create MR: RequestContext %3 PD %1 FastRegister %2\r\n
0xb00004e9 | NDKPI Flush: QP %1\r\n
0xb00004ea | NDKPI Send (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 Flags %7\r\n
0xb00004eb | NDKPI Receive (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5\r\n
0xb00004ec | NDKPI Register MR: RequestContext %5 MR %1 MDL %2 Length %3 Flags %4\r\n
0xb00004ed | NDKPI Deregister MR: RequestContext %2 MR %1\r\n
0xb00004ee | NDKPI Initialize FastRegister MR: RequestContext %4 MR %1 AdapterPageCount %2 RemoteAccess %3\r\n
0xb00004ef | NDKPI Modify SRQ: RequestContext %4 SRQ %1 SrqDepth %2 NotifyThreshold %3\r\n
0xb00004f0 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SrcAddress %4 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f1 | NDKPI Connect: RequestContext %9 Connector %1 QP %2 SharedEndpoint %10 DestAddress %6 IRD %7 ORD %8 PrivateDataLength %11\r\n
0xb00004f2 | NDKPI CompleteConnect: RequestContext %3 Connector %1 DisconnectEventContext %2\r\n
0xb00004f3 | NDKPI Accept: RequestContext %6 Connector %1 QP %2 IRD %3 ORD %4 PrivateDataLength %7 DisconnectEventContext %5\r\n
0xb00004f4 | NDKPI Disconnect: RequestContext %2 Connector %1\r\n
0xb00004f5 | NDKPI Listen: RequestContext %4 Listener %1 Address %3\r\n
0xb00004f6 | NDKPI Create MW: RequestContext %2 PD %1\r\n
0xb00004f7 | NDKPI Create SRQ: RequestContext %8 PD %1 SrqDepth %2 MaxReceiveRequestSge %3 NotifyThreshold %4 SrqNotificationContext %5 AffinityMask %6 AffinityGroup %7\r\n
0xb00004f8 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 QPContext %4 ReceiveQueueDepth %5 InitiatorQueueDepth %6 MaxReceiveRequestSge %7 MaxInitiatorRequestSge %8\r\n
0xb00004f9 | NDKPI Create QP: RequestContext %9 PD %1 ReceiveCQ %2 InitiatorCQ %3 SRQ %10 QPContext %4 InitiatorQueueDepth %6 MaxInitiatorRequestSge %8\r\n
0xb00004fa | NDKPI Create PD: RequestContext %2 Adapter %1\r\n
0xb00004fb | NDKPI Create SharedEndpoint: RequestContext %4 Adapter %1 Address %3\r\n
0xb00004fc | NDKPI Create Connector: RequestContext %2 Adapter %1\r\n
0xb00004fd | NDKPI Create Listener: RequestContext %3 Adapter %1 ConnectEventContext %2\r\n
0xb00004fe | NDKPI Build LAM: RequestContext %4 Adapter %1 MDL %2 Length %3 LAMBuffer %5 LAMBufferSize %6\r\n
0xb00004ff | NDKPI Release LAM: Adapter %1 LAMBuffer %2\r\n
0xb0000500 | NDKPI CQ Notification Callback: CqNotificationContext %1 CqStatus %2\r\n
0xb0000501 | NDKPI SRQ Notification Callback: SrqNotificationContext %1 SrqStatus %2\r\n
0xb0000502 | NDKPI Disconnect Event Callback: DisconnectEventContext %1\r\n
0xb0000503 | NDKPI Connect Event Callback: ConnectEventContext %1 Connector %2\r\n
0xb0000504 | NDKPI Got %3 Token %4 from %2 %1\r\n
0xb0000505 | NDKPI Got %3 Address %5 from %2 %1\r\n
0xb0000506 | NDKPI %3 Address query failure %4 on %2 %1\r\n
0xb0000507 | NDKPI Reject: Connector %1 PrivateDataLength %2 Status %3\r\n
0xb0000508 | NDKPI Get Connect Data: Connector %1 IRD %2 ORD %3 PrivateDataLength %4 Status %5\r\n
0xb0000509 | NDKPI Work Request Inline Failure: RequestContext %2 QP %1 Status %3\r\n
0xb000050a | NDKPI Bind: RequestContext %2 QP %1 MR %3 MW %4 VirtualAddress %5 Length %6 Flags %7\r\n
0xb000050b | NDKPI FastRegister: RequestContext %2 QP %1 MR %3 AdapterPageCount %4 AdapterPageArray %5 FBO %6 Length %7 BaseVirtualAddress %8 Flags %9\r\n
0xb000050c | NDKPI Invalidate: RequestContext %2 QP %1 %4 %3 Flags %5\r\n
0xb000050d | NDKPI Read (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050e | NDKPI Write (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteAddress %9 RemoteToken %10 Flags %7\r\n
0xb000050f | NDKPI SRQ Receive (SGE %8/%6): RequestContext %2 SRQ %1 SGE %3/%4/%5\r\n
0xb0000510 | NDKPI SRQ Work Request Inline Failure: RequestContext %2 SRQ %1 Status %3\r\n
0xb0000511 | NDKPI Open Adapter: InterfaceIndex %1 Adapter %2 Status %3\r\n
0xb0000512 | NDKPI Close Adapter (Enter): Adapter %1\r\n
0xb0000513 | NDKPI Close Adapter (Exit): Adapter %1\r\n
0xb0000514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7.\r\n
0xb0000515 | NDKPI Interface Event: InterfaceIndex %1, NDK-Operational %3, %2 (%4)\r\n
0xb0000516 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %8. Destination MAC address: %5. Source: %6 : %9, Destination: %7 : %10.\r\n
0xb0000517 | Network adapter Luid %1 received a wake packet matching pattern %2. Protocol: %9. Destination MAC address: %5. Source: %7 : %10, Destination %8 : %11.\r\n
0xb0000518 | TCP: Connection %1: Silent Mode %2 Context %3\r\n
0xb0000519 | TCP: Connection %1 notification channel request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb000051a | TCP: Connection %1 query notification channel status request. NcmContext = %2, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb000051b | TCP: Connection %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb000051c | TCP: Connection %1 notification channel signal event. NcmContext = %2, PID = %3, RcvNxt = %4, Delivered Data = %5, Indicated Data = %6, FinalEvent = %7.\r\n
0xb000051d | TCP: Connection %1 notification channel detached. NcmContext = %2, TCB State = %3. Cleanup NcmContext = %5\r\n
0xb000051e | TCP: Connection %1 notification channel unlinked. TCB State = %3.\r\n
0xb000051f | TCP: Connection %1 notification channel wake pattern plumbing. SystemReserved = %2, Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000520 | TCP: Connection %1 notification channel wake pattern deplumbing. Wake-on-Lan Handle = %3, Status = %4.\r\n
0xb0000521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12.\r\n
0xb0000522 | NDKPI Control CQ Interrupt Moderation: CQ %1 Interval %2 Count %3 Status %4\r\n
0xb0000523 | TCP: Connection %1 notification channel request processing. IsRedirected = %2, WfpFailure = %3, Status = %4, WaitStatus = %5, Local IP address = %7 %9 %8, Remote IP address = %10 %9 %11 Local Port = %12, Remote Port = %13.\r\n
0xb0000524 | IP: IP address lifetime = %4 %6 %5 on interface = %1, protocol = %2, CurrentTime = %7 Old BaseTime = %8 Old ValidTime = %9 New BaseTime = %11 New ValidTime = %12.\r\n
0xb0000525 | TCP: Repartition event %1 (%2) %5.\r\n
0xb0000526 | %1 %2 on processor %3 at Tick = %4 Time = %5.\r\n
0xb0000527 | %1 timer rescheduled by processor %2 for processor %3 at Tick = %4 to Tick = %5, OldScheduledExpiration = %6 NewScheduledExpiration = %7 DueTime = %8 Aperiodic = %9.\r\n
0xb0000528 | %1 timer fired on processor %2 at Tick = %3, was scheduled for = %4.\r\n
0xb0000529 | IP: Connecting interface %1, trace = %2.\r\n
0xb000052a | IP: Limited link connectivity set on interface %1, trace = %2.\r\n
0xb000052b | IP: Limited link connectivity reset on interface %1, trace = %2.\r\n
0xb000052c | IP: Neighbor with IpAddress = %3 DlAddress = %5 on Interface = %1 changed state from %6 to %7 due to Event = %8.\r\n
0xb000052d | IP: %5 on Interface = %1 from SourceIpAddress = %3 for TargetIpAddress = %4.\r\n
0xb000052e | IP: Source address %2 is preferred over %3 for Destination %4 in Compartment %5, Reason: %8 (Rule %6.%7).\r\n
0xb000052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions = %6, Rule = %7 %8.%9.\r\n
0xb0000530 | NDKPI ResultEx %6/%7: CQ %1 RequestContext %5 Status %2 BytesTransferred %3 QpContext %4 Type %8 TypeSpecific %9\r\n
0xb0000531 | NDKPI SendInvalidate (SGE %8/%6): RequestContext %2 QP %1 SGE %3/%4/%5 RemoteToken %9 Flags %7\r\n
0xb0000532 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000533 | TCP: connection %1: CTCP Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd =%3.\r\n
0xb0000534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8\r\n
0xb0000535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8.\r\n
0xb0000536 | UDP: Endpoint %1 notification channel request. NcmContext = %2, Endpoint State = %3, PID = %4, IsLoopback = %5, Status = %7.\r\n
0xb0000537 | UDP: Endpoint %1 query notification channel status request. NcmContext = %2, Endpoint State = %3, PID = %4, Channel Status = %6, Status = %7.\r\n
0xb0000538 | UDP: Endpoint %1 notification channel request processed. NcmContext = %2, PID = %3, Status = %4 PushNotificationId = %5.\r\n
0xb0000539 | UDP: Endpoint %1 notification channel signal event. NcmContext = %2, PID = %3, Delivered Data = %4 FinalEvent = %5.\r\n
0xb000053a | UDP: Endpoint %1 notification channel detached. NcmContext = %2, Endpoint State = %3.\r\n
0xb000053b | UDP: Endpoint %1 notification channel unlinked. Endpoint State = %3.\r\n
0xb000053c | UDP: Endpoint %1 notification channel request processing. Local IP address = %3 %5 %4, Local Port = %6.\r\n
0xb000053d | TCP: connection %1:  Rtt sample recorded %2 SRTT %4 RttVar %3.\r\n
0xb000053e | TCP: connection %1: Rtt resiliency detection complete with Rtt sample = %2 and new SRTT = %4.\r\n
0xb000053f | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5.\r\n
0xb0000540 | TCP: CTCP Duplicate Ack event. Connection %1, SndUna = %5, CWnd = %2, DupAckCount = %4.\r\n
0xb0000541 | TCP: connection %1: Spurious timeout at Seq = %2.\r\n
0xb0000542 | TCP: connection %1 spurious RTO detection initiated at %2.\r\n
0xb0000543 | TCP: connection %1 spurious RTO detection terminated at %2.\r\n
0xb0000547 | TCP: connection %1: Send Retransmit round with SndUna = %2, Round = %3, SRTT = %4, RTO = %5.\r\n
0xb0000548 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26.\r\n
0xb0000549 | TCPIP: Message %1 %2 %3 %4 %5.\r\n
0xb000054a | TCP: Connection %1 SACK updated SndUna %2 SndMax %3 SackCount %4 SackBytes %5 SackInFlight %6 SackIsLost %7.\r\n
0xb000054b | TCP: TCB %1 Requires address based pattern = %2 LocalPort = %3 RtcPortRange = [%4, %5] Status = %6.\r\n
0xb000054c | TCP: Rtc Port Range Assignment. Allocated = %1, Port = %2.\r\n
0xb000054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 with %7 since network interface %9 is in low-power mode.\r\n
0xb000054e | IP: Interface configuration updated on interface %1 property %2 value %3 event %4.\r\n
0xb000054f | TCP: Connection %1 notification channel unmark request. NcmContext = %2, TCB State = %3, PID = %4, IsLoopback = %5, IsShutdown = %6, Status = %7.\r\n
0xb0000550 | TCPIP: A packet has been cloned for a raw listener. NBL %2 cloned from NBL %1. Protocol = %3, Family = %4.\r\n
0xb0000551 | TCPIP: A cloned packet has been dropped. NBL %2 cloned from NBL %1. Family = %3.\r\n
0xb0000552 | IP: Interface = %1 IpAddress = %3 processing WolEvent = %4 with Status = %5.\r\n
0xb0000553 | IP: Interface = %1 WolHandle = %3 has DestinationIpAddress = %4 TargetIpAddress1 = %5 TargetIpAddress2 = %6 Flags = %7 while processing WolEvent = %8 with Status = %9.\r\n
0xb0000554 | TCP connection tuple inserted- TCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000555 | TCP connection tuple removed- TCB/TWTCB: %1 LocalAddress: %3 RemoteAddress: %5\r\n
0xb0000556 | TCP port selection deferred for outbound connect- LocalAddress: %2\r\n
0xb0000557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, TcpRecvSegCoalesceInfo %9\r\n
0xb0000558 | Teredo Add -- PID: %1 started listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb0000559 | Teredo Remove -- PID: %1 stopped listening on %3. AddressType %4. ScopeLevel %5. Port %6. EndpointRecord %7.\r\n
0xb000055a | IP: RouteLookup - API: %1 DstAddr: %3 ConstrainSrcAddr: %4 ConstrainIfIndex: %5 ConstraintOveridden: %6 ReturnConstrained: %7 OutgoingIfIndex: %8 NextHopAddr: %9 Status: %10\r\n
0xb000055b | IP: SourceAddrLookup - DstAddr: %2 ConstrainSrcAddr: %3 ConstrainIfIndex: %4 OutgoingIfIndex: %5 ReturnConstrained: %6 SelectedSrcAddr: %7\r\n
0xb000055c | WFP-ALE: Partition Count=%1 Partition Mask=%2: Partition Id=%d Partition NumEntries = %4.\r\n
0xb000055d | WFP-ALE: HotAdd/Remove: Old Partiton Count=%1 Old Partition Mask=%2 New Partiton Count=%1 New Partition Mask=%2.\r\n
0xb000055e | WFP-ALE: RemoteEndPoint Insertion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb000055f | WFP-ALE: RemoteEndPoint Deletion: AddrLen=%1 RemoteAddr=%2 RemotePort=%3 LocalAddr=%4 LocalPort=%5 PartitionId=%6 PartitionNumEntries=%7\r\n
0xb0000560 | WFP-ALE: ALE: low memory state detected. LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000561 | WFP-ALE: leaving low memory state. HighMemoryEvent = %1 HighNonPagedPoolEvent = %2.\r\n
0xb0000562 | WFP-ALE: Dpc for cleanup initiated: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000563 | WFP: Dpc for cleanup QUEUED or RE-QUEUED: LowMemoryEvent = %3 LowNonPagedPoolEvent = %4.\r\n
0xb0000564 | TCP: LEDBAT %2: Connection %1, BaseDelayMs = %6, CurrentDelayMs = %7, CWnd = %3, SsThresh = %4, SndWnd = %5, DelayBasedCwndFactor %9%%, RemainingTimeMs = %8.\r\n
0xb0000565 | TCP: AssociateNameResContext Endpoint: %1 Status: %16 NameResolutionContext: %2 DnsName: %3 InterfaceIndex: %4 IPAddrCount: %5 IPAddrs: %7 %9 %11 %13 %15\r\n
0xb0000566 | TCP: InspectConnectWithNameResContext Connection: %5 (local: %2 remote: %4) NameResolutionContext: %6 DnsName: %7 Status: %8.\r\n
0xb0000567 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 InterfaceMetric: %10 RouteMetric: %11] is preferred over Route [DestinationPrefix: %14/%12 NextHop: %16 InterfaceIndex: %17 InterfaceMetric: %18 RouteMetric: %19] for Destination: %3 in Compartment: %1, Reason: %20.\r\n
0xb0000568 | IP: Route [DestinationPrefix: %6/%4 NextHop: %8 InterfaceIndex: %9 RouteMetric: %10] is blocked for Destination: %3 ConstrainInterfaceIndex: %11 ConstrainScopeZone: %12 in Compartment: %1, Reason: %13.\r\n
0xb0000569 | TCP: Tail Loss Probe Send Connection = %1 SndUna = %2, SndMax = %3, SendAvailable = %4, TailProbeSeq = %5, TailProbeLast = %6, ControlsToSend = %7, ThFlags = %8.\r\n
0xb000056a | TCP: Tail Loss Probe Event Connection = %1, Event = %2.\r\n
0xb000056b | TCP: RACK Event Connection = %1, Event = %2, MinRTT = %3, ReoWind = %4, TimeSlotDeltaMin = %5, SeqNum = %6, Timestamp = %7, RttSample = %8.\r\n
0xb000056c | TCP: Fastopen state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000056d | UDP: endpoint (family=%5 pid=%3) create failed: address family not attached.\r\n
0xb000056e | UDP: endpoint %1 (family=%5 pid=%3) create failed: compartment %4 not found.\r\n
0xb000056f | UDP: endpoint %1 (family=%5 pid=%3) created.\r\n
0xb0000570 | UDP: endpoint %1 (family=%5 pid=%3) create failed: inspection status = %2\r\n
0xb0000571 | UDP: endpoint %4 bind failed: address %2 cannot be resolved, status = %3\r\n
0xb0000572 | UDP: endpoint %4 (sockaddr=%2) bind failed: port-acquisition status = %3\r\n
0xb0000573 | UDP: endpoint %4 (sockaddr=%2) bind failed: inspection status = %3\r\n
0xb0000574 | UDP: endpoint %4 (sockaddr=%2) bound.\r\n
0xb0000575 | UDP: endpoint %4 (sockaddr=%2) closed.\r\n
0xb0000576 | UDP: endpoint %4 closed.\r\n
0xb0000577 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address resolution status = %6\r\n
0xb0000578 | UDP: endpoint %1 (sockaddr=%3) send messages %5: address validation failed.\r\n
0xb0000579 | UDP: endpoint %1 (sockaddr=%3) send messages %5: source-address selection status = %6\r\n
0xb000057b | UDP: address family %2added to interface %1.\r\n
0xb000057c | UDP: address family %2removed from interface %1.\r\n
0xb000057d | UDP: Failure initializing transport protocol, status = %1\r\n
0xb000057e | UDP: Failure starting NLNPI client, status = %1\r\n
0xb000057f | UDP: Failure initializing NSI support, status = %1\r\n
0xb0000580 | UDP: Failure starting TLNPI provider, status = %1\r\n
0xb0000581 | UDP: Failure initializing QoS support, status = %1\r\n
0xb0000582 | UDP: Failure starting %1, status = %2\r\n
0xb0000583 | UDP: endpoint %1 (sockaddr=%3) send messages %5: could not allocate send context.\r\n
0xb0000584 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path af failure, status = %6\r\n
0xb0000585 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path missing next hop failure.\r\n
0xb0000586 | UDP: endpoint %1 (sockaddr=%3) send messages %5: path next hop address failure.\r\n
0xb0000587 | TCP: Early Retransmission, FACK or RACK, Connection = %1, SndUna = %2, SackIsLostSeq = %3, DupAckCount = %4\r\n
0xb0000588 | TCP: Ignoring fastopen SYN option due to limit on concurrent SYN_RCVD fastopen connections, Connection = %1, SynRcvdLimit = %2\r\n
0xb0000589 | TCP: Failed to update fastopen key state, Location = %1, Status = %2. Server-side fastopen will be disabled\r\n
0xb000058a | TCP: Fast Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058b | TCP: SACK Retransmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058c | TCP: Limited Transmit Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058d | TCP: SACK Retransmit Additional Send, Connection = %1, BytesToSend = %2, SndNxt = %3\r\n
0xb000058e | %1: %2message. Type = %3, Code = %4, CompartmentId = %5, SourceAddress = %7, DestAddress = %9\r\n
0xb000058f | %1: %2path drop. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11\r\n
0xb0000590 | %1: Echo timeout. Status = %4\r\n
0xb0000591 | %1 Timer state changed to %3 by Processor %2 Usage = %4 at Tick = %5\r\n
0xb0000592 | TCP: connection %1 send complete %3 bytes at %4 (%2).\r\n
0xb0000593 | IP: Compartment creation. Compartment = %1, Protocol = %2, Private = %3, Status = %4.\r\n
0xb0000594 | IP: Compartment deletion. Compartment = %1, Protocol = %2.\r\n
0xb0000595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13.\r\n
0xb0000596 | TCP: connection %1: Duplicate ACK updated cwnd = %2 and updated ssthresh = %3 DupAckCount = %4 SndUna = %5 CwrMax = %6.\r\n
0xb0000597 | IP: Compartment cleanup. Compartment = %1, Protocol = %2.\r\n
0xb0000598 | IP: Interface network category state change. Interface = %1, Compartment = %2 , Protocol = %3, NetworkCategory = %4, DomainNetworkLocation = %5, DomainType = %6, Signature = %7.\r\n
0xb0000599 | IP: Interface creation. Interface = %1, Compartment = %2, Protocol = %3, PhysicalMediumType = %4, Status = %5.\r\n
0xb000059a | IP: Interface deletion. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059b | IP: Interface cleanup. Interface = %1, Compartment = %2, Protocol = %3.\r\n
0xb000059c | IP: SubInterface creation. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4, Status = %5.\r\n
0xb000059d | IP: SubInterface deletion. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059e | IP: SubInterface cleanup. SubInterface = %1, Interface = %2, Compartment = %3, Protocol = %4.\r\n
0xb000059f | IP: Interface change Notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005a0 | IP: Interface internet connectivity status change. Interface = %1, Compartment = %2, Protocol = %3, OldConnectivityStatus = %4, NewConnectivityStatus = %5.\r\n
0xb00005a1 | IP: Address change notification. Address = %2, Interface = %3, Compartment = %4, Protocol = %5, Reason = %6.\r\n
0xb00005a2 | IP: Route change notification. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, NotifyFlags = %8.\r\n
0xb00005a3 | IP: Neighbor change notification. IpAddress = %2, DlAddress = %4, Interface = %5, Compartment = %6, State = %7, Reason = %8.\r\n
0xb00005a4 | IP: Address DAD state change. Address = %2, Interface = %3, Compartment = %4, OldState = %5, NewState = %6, Reason = %7.\r\n
0xb00005a5 | IP: Route Dead Gateway Detection state change. DestinationPrefix = %2/%5, NextHop = %4, Interface = %7, Compartment = %6, OldState = %8, NewState = %9, OldProbeCount = %10, NewProbeCount = %11, OldUnreachablePaths = %12, NewUnreachablePaths = %13, OldMovedPaths = %14, NewMovedPaths = %15, TotalPaths = %16, OldStateChangeTick = %17, NewStateChangeTick = %18, DgdNeedsReset = %19, Reason = %20.\r\n
0xb00005a6 | IP: Disconnecting TCP connections with Address = %2, Interface = %3, Compartment = %4, SkipLocal = %5, SkipOnLink = %6.\r\n
0xb00005a7 | TCP: connection %1: Sending paced chunk of %6 bytes with CWnd = %2, SndWnd = %3, BytesAvailable = %4, BytesOutstanding = %5\r\n
0xb00005a8 | Fallback: Context = %1, Feature = %2, TraceReason = %3, Confidence = %4, Successes = %5, Failures = %6\r\n
0xb00005a9 | TCPIP: TCB %1 using fast loopback\r\n
0xb00005aa | IP: Router information change notification. Interface = %1, Compartment = %2, Protocol = %3, Reason = %4.\r\n
0xb00005ab | IP: %1. Interface = %2, Compartment = %3, RouterAddress = %5, DNS Server/Suffix: %7 %8, Lifetime = %9.\r\n
0xb00005ac | IP: Route rundown. Interface = %1, Compartment = %2, Prefix = %4/%5, NextHop = %7, Metric = %8, State = %9, Origin = %10, Age = %11, ValidLifetime = %12, PreferredLifetime = %13, Flags = %14.\r\n
0xb00005ad | TCP: CUBIC ECN event. Connection %1, CWnd %2, SSThresh = %3, SndUna = %4\r\n
0xb00005ae | INETINSPECT: Owner = %1, InspectHandle = %2, InspectType = %3, Action = %4, Status = %5\r\n
0xb00005b0 | FallbackCheck: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b1 | FallbackUpdate: Ctx = %1, Feature = %2, Failed = %3, Succeeeded = %4, InProbe = %5, PathsProbed = %6, Status = %7\r\n
0xb00005b2 | Fallback: Permanently disabling feature, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b3 | Fallback: Enabling feature for this boot session, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b4 | Fallback: Feature previously disabled, Ctx = %1, Feature = %2, PathsProbed = %6\r\n
0xb00005b5 | TCP Fastopen fallback update: Tcb = %1, FastopenState = %2, DataBytesIn = %3, ShutdownStatus = %4, ProbeStatus = %5\r\n
0xb00005b6 | Disabling feature until connectivity is established: CompartmentId =%1, IfIndex = %2, Feature = %3, ConnectivityStatus = %4\r\n
0xb00005b7 | Disabling %1 for loopback connection\r\n
0xb00005b8 | Disabling TCP Fastopen for BaseEndpoint = %1 because an incompatible WFP callout is installed\r\n
0xb00005b9 | IP: Setting source constraint for route lookup - Compartment: %1 DstAddr: %3 ConstrainSrcAddr: %5 ConstrainIfIndex: %6 ConstraintFlags: %7\r\n
0xb00005ba | WFP-ALE: RemoteEndPoint Insertion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bb | WFP-ALE: RemoteEndPoint Deletion: (local=%2 remote=%3) PartitionId=%4 PartitionNumEntries=%5\r\n
0xb00005bc | TCP: connection %8 (local=%2 remote=%4) system abort. PID = %6.\r\n
0xb00005bd | Disabling %1 due to no next hop\r\n
0xb00005be | TCP: endpoint (sockaddr=%2) bind failed: wake status = %3.\r\n
0xb00005bf | UDP: endpoint %4 (sockaddr=%2) bind failed: wake status = %3\r\n
0xb00005c0 | Acquire wake port %2, type=%1, family=%3, IF=%4, compartment=%5\r\n
0xb00005c1 | TCP: Connection %1 reached max SACK queue length\r\n
0xb00005c2 | TCP: Connection %1 requested fast open\r\n
0xb00005c3 | TCP: CUBIC Hystart state change event. Connection %1, State %2, CWnd %3, SSThresh = %4.\r\n
0xb00005c4 | IP: Transmitting loopback Nbl %1. Interface=%2, Compartment=%3, Src=%6, Dst=%5, Proto=%7.\r\n
0xb00005c5 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26 ConnectionTimeMs %27 Timestamps %28 RttUs %29 MinRtt %30 MaxRtt %31 SynRetrans %32 CongestionAlgorithm %33 \   State %34 Local %36 Remote %38 CWnd %39 SsThresh %40 RcvWnd %41 RcvBuf %42 SndWnd %43.\r\n
0xb00005c6 | TCPIP: Framing layer %1 (AddressFamily=%2) dropped %4 packet(s) on interface=%3, Reason=%5, Data=%6.\r\n
0xb00005c7 | TCP: Connection %1 Transport (Protocol %2, AddressFamily = %3) sent RST with Local = %5, Remote = %7. Reason = %8.\r\n
0xb00005c8 | TCP connection failed with Status = %1, Local = %3, Remote = %5, ProcessId = %6, TcpState = %7 at %8:%9:%10 Reason = %11.\r\n
0xb00005c9 | TCP: Connection %1 PRR send SackIsLostSeq %2 SackInFlight %3 SackBytes %4 SackIsLost %5 SsThresh %6 RecoveryFS %7 AckedData %8 BytesInFlight %9 BytesToSend %10 PrrDelivered %11 PrrOut %12.\r\n
0xb00005ca | UDP: Endpoint %1 segment message. SegmentSize = %2 (0 == No Segmentation) MessageLength = %3 HwDatagrams = %4 HwSegments = %5 SwSegments = %6 Status = %7.\r\n
0xb00005cb | UDP: Endpoint %1 segmentation offload unavailable. Reason = %2 SegmentSize = %3 LocalAddress = %5, RemoteAddress = %7.\r\n
0xb00005cc | TCPIP: Framing layer interface %1 (AddressFamily = %2) failed to bind to its provider. Code = %3. Status = %4.\r\n
0xb00005cd | TCPIP: OID request from framing layer interface %1 (AddressFamily = %2) failed. OID = %3. Status = %4.\r\n
0xb00005ce | TCPIP received a status indication on interface %1. AddressFamily = %2. NdisStatus = %3.\r\n
0xb00005cf | IP: Failed to set socket option. Level = %1. Option = %2. Status = %3.\r\n
0xb00005d0 | IP: Failed to set socket IOCTL. IOCTL = %1. Status = %2.\r\n
0xb00005d1 | Failed to process multicast %1 request. Address = %2 %6. Source Address = %3 %7. Reason = %8. Status = %9.\r\n
0xb00005d2 | Processed multicast %1 request successfully. Address = %2 %6. Source Address = %3 %7.\r\n
0xb00005d3 | %1. Interface = %2. Address = %3 %5. Data = %6.\r\n
0xb00005d4 | %1. Interface = %2. Address = %3 %5. Data = %6. Status = %7.\r\n
0xb00005d5 | Invalid ECN codepoints in reassembly. Ce = %1. Ect0 = %2. Ect1 = %3. NotEct = %4.\r\n
0xb00005d6 | Reassembly failure: packets do not add up correctly.  Interface = %1. Address family = %2.\r\n
0xb00005d7 | Reassembly failure: failed to restore IPSec packet history.  Interface = %1. Address family = %2. Status = %3.\r\n
0xb00005d8 | Could not transfer %1.  Interface = %2. Address family = %3.\r\n
0xb00005d9 | Attempting to %1 the multicast group at FL.  Interface = %2. Address = %3 %5. Data = %6. Status = %7.\r\n
0xb00005da | Failed to update address list at FL. Interface = %1. Address Family = %2. Status = %3.\r\n
0xb00005db | Too many DAD failures, so will not create temporary address. Interface = %1. Address = %2 %4.\r\n
0xb00005dc | Failed to address interface; deleting it. Interface = %1. Status = %2.\r\n
0xb00005dd | Failed to reach default gateway after reconnect; cleaning settings.  Interface = %1.\r\n
0xb00005de | Failed to sync interface with registry.  Interface = %1. Field = %2. Status = %3.\r\n
0xb00005df | Failed to %1 an active reference on the interface.  Interface = %2. Reference Reason = %3. Status = %4.\r\n
0xb00005e0 | Redirect path hijack for destination %2 %3 from %5 %6. Interface = %1.\r\n
0xb00005e1 | Redirect path rate limit for IPv6 source address %3. Interface = %1.\r\n
0xb00005e2 | Dropped %2 fragment. Interface = %3. Reason = %1.\r\n
0xb00005e3 | Reassembly timeout. Interface = %1. Id = %2. Source Address = %3 %6.  Destination Address = %4 %7.\r\n
0xb00005e4 | Invalid IP option. Option = %3. Level = %2. Reason = %1.\r\n
0xb00005e5 | Invalid IP hop-by-hop option.  Option = %2. Reason = %1.\r\n
0xb00005e7 | Invalid IP routing header option. Reason = %1.\r\n
0xb00005e9 | This option cannot be specified by the user\r\n
0xb00005ea | TCP: interface %1: received potential RSC status indication. Current IPv4 State = %2, Offload IPv4 State = %3, Current IPv6 State = %4, Offload IPv6 State = %5.\r\n
0xb00005eb | UDP: endpoint %1: URO SCU received. SegCount = %2, SegSize = %3, DataLength = %4.\r\n
0xb00005ec | TCP software RSC global disabled mask = %1, UDP software URO global disabled mask = %2.\r\n
0xb00005ed | UDP: Global parameters updated for Address Family %1: DisableUro = %2.\r\n
0xb00005ee | IP: IPSNPI client rundown. %3 Interface = %1, Compartment = %2, Client = %4.\r\n
0xb00005ef | TCPIP: Process with PID=%1, ProcessSeqNum=%7 acquired port tracker reservation of type %3, Protocol %4 for %6 ports starting at %5 with status = %2.\r\n
0xb00005f0 | Illegal tunnel. Interface: %1, Tunnel type: %2. Reason: %3.\r\n
0xb00005f1 | Framing: Interface change in progress. Interface: %1. Address Family: %2. Current progress: %3. Status: %4.\r\n
0xb00005f2 | Framing: Isolation is not supported on this network adapter. Interface: %1. Address Family: %2. Reason: %3.\r\n
0xb00005f3 | Framing: Failed to set pattern. Interface: %1. Address Family: %2. Pattern type: %3. Status: %4.\r\n
0xb00005f4 | Framing: Interface management request. Interface: %1. Address Family: %2. Request code: %3. Status: %4.\r\n
0xb00005f5 | Framing: WOL capabilities update in progress. Interface: %1. Address Family: %2. Current progress: %3. Status: %4.\r\n
0xb00005f6 | Framing: A PNP event has been indicated. Interface: %1. Address Family: %2. Compartment: %3. Event: %4. Data: %5.\r\n
0xb00005f7 | Framing: interface rundown: Interface = %1, Luid = %2, Address family = %3, Compartment = %4, Isolation mode = %5, Isolation ID = %6, DL address = %8, Interface type = %9, Physical medium type = %10, SW RSC/URO applicable = %11, SW RSC enabled = %12, Alias = %13.\r\n
0xb00005f8 | RAW: endpoint %1 (Proto = %2, LocalAddress = %6, RemoteAddress = %8) sending %3 messages and a total of %4 bytes.\r\n
0xb00005f9 | RAW: endpoint %1 (Proto = %2, LocalAddress = %6, RemoteAddress = %8) delivering %4 bytes.\r\n
0xb00005fa | RAW: endpoint %1 (Proto = %2, LocalAddress = %4, RemoteAddress = %6) send failed with reason = %7 status = %8.\r\n
0xb00005fb | RAW: endpoint %1 (Family = %2, Proto = %3, Compartment = %4, PID = %5, ProcessSeqNum = %6) created.\r\n
0xb00005fc | RAW: endpoint (Family = %2, Proto = %3, Compartment = %4, PID = %5, ProcessSeqNum = %6) create failed with reason %7 status %8.\r\n
0xb00005fd | RAW: endpoint %1 (Proto = %2, LocalAddress = %4) bound.\r\n
0xb00005fe | RAW: endpoint %1 (Proto = %2, LocalAddress = %4) bind failed with reason %5 status %6.\r\n
0xb00005ff | RAW: endpoint %1 closed.\r\n
0xb0000600 | TCPIP: Error processing router advertisement on interface index %1 - Preferred lifetime of %2 should not be greater than the valid lifetime of %3.\r\n
0xb0000601 | TCPIP: Error processing router advertisement on interface index %1 - Prefix length of %2 and identifier of %3 must add up to the size of an IPv6 address (128 bits).\r\n
0xb0000602 | TCPIP: An ARP request was dropped on interface %1. Physical address = %3, IP source address = %4, IP target address = %5, Reason = %6.\r\n
0xb0000603 | TCPIP: An ARP reply was dropped on interface %1. Physical address = %3, IP source address = %4, Directed to this interface = %5, Reason = %6.\r\n
0xb0000604 | TCPIP: No handler found for an %1 packet with upper layer protocol %2\r\n
0xb0000605 | TCPIP: Upper layer protocol handler for an %1 packet returned with error %3\r\n
0xb0000606 | IP: neighbor rundown: Interface = %1, Compartment = %2, IpAddress = %4, DlAddress = %6, State = %7, LastReachable = %8 ms, IsUnreachable = %9, Flags = %10.\r\n
0xb0000608 | Endpoint %1 socket option set with level %2, name %3, value %5.\r\n
0xb0000609 | TCP: connection = %1 RACK timeout expired. SndUna = %2, SndMax = %3, SackedBytes = %4, LossDetected = %5, InRecovery = %6.\r\n
0xb000060a | TCP: connection = %1 armed RACK timer. SndUna = %2, SndMax = %3, SackedBytes = %4, LossDetected = %5, InRecovery = %6, DeltaTicks = %7.\r\n
0xb000060b | TCP: connection = %1 received a SACK block. SndUna = %2, SndMax = %3, Ack = %4, SLE = %5, SRE = %6.\r\n
0xb000060c | TCP: connection = %1 received a SACK. SndUna = %2, SndMax = %3, Ack = %4, SackedBytes = %5, LossDetected = %6, InRecovery = %7, NumSackBlocks = %8, DSackCount = %9, NewSackInfo = %10, RecoveryMax = %11.\r\n
0xb000060d | TCP: connection = %1 enabled send tracker.\r\n
0xb000060e | TCP: connection = %1 send tracker acked a transmit. AckNo = %2, Start = %3, End = %4, Timestamp = %5, EverTransmitted = %6, SackedBytes = %7, BytesInFlight = %8.\r\n
0xb000060f | TCP: connection = %1 send tracker enqueued a transmit. Start = %2, End = %3, Timestamp = %4, SackedBytes = %5, BytesInFlight = %6.\r\n
0xb0000610 | TCP: connection = %1 send tracker marked a transmit as lost. Start = %2, End = %3, Timestamp = %4, EverTransmitted = %5, InFlightCount = %6, SackedBytes = %7, BytesInFlight = %8.\r\n
0xb0000611 | TCP: accept redirection: original listener = %1, redirected listener = %2, succeeded = %3, redirected = %4, codepath = %5, local address = %6, remote address = %7, redirected address = %8\r\n
0xb0000612 | TCP: connection = %1 dropped a SACK block due to SACK limit reached. SndUna = %2, SndMax = %3, Ack = %4, SLE = %5, SRE = %6, NumSackedTransmits = %7, limit = %8.\r\n
0xb0000613 | TCP: connection %1 terminated by NSI. State = %2, PID = %3, ProcessSeqNum = %4, Shutdown = %5.\r\n
0xb0000614 | TCP: connection = %1 rate-based pacing timeout expired. SndUna = %2, SndMax = %3, PacingAllowance = %4 B, PacingRate = %5 B/ms.\r\n
0xb0000615 | TCP RLedbat connection = %1. Type = %2, SSThresh = %3, Wnd = %4, WndWs = %5, DrainedBytes = %6, ReceiveHigh = %7, TsHigh = %8, LastRollOverTimeMs = %9, EndReductionTimeMs = %10, MinDelaySampleMs = %11, MinBaseDelayMs = %12\r\n
0xb000061a | TCP: endpoint (PID=%4 ProcessSeqNum=%7) create failed: access denied.\r\n
0xb000061b | UDP: endpoint (PID=%3 ProcessSeqNum=%6) create failed: access denied.\r\n
0xb000061c | TCP: connection %8 (local=%2 remote=%4 PID=%6 ProcessSeqNum=%9) connect failed: access denied.\r\n
0xb000061d | TCP: Congestion state changed for connection = %1 from OldState = %2 to NewState = %3.\r\n
0xb000061e | TCP: connection = %1 detected reordering. MaxReorderingBytes = %2, Fack = %3, EndSeq = %4.\r\n
0xb0000629 | TCP: connection = %1 updated reownd. Multiplier = %2, Persist = %3, Reownd = %4, ReorderingSeen = %5, DSackSeenOnLatestAck = %6, InLossRecovery = %7, DupAckCountReached = %8, DSackRound = %9, DSackRoundValid = %10.\r\n
0xb00103ed | TCP: endpoint %1 (sockaddr=%3) bind failed: address resolution status = %4.\r\n
0xb00103ee | TCP: endpoint %1 (sockaddr=%3) bind failed: port-acquisition status = %4.\r\n
0xb00103ef | TCP: endpoint %1 (sockaddr=%3) bind failed: inspection status = %4.\r\n
0xb00103f0 | TCP: endpoint %1 (sockaddr=%3) bound.\r\n
0xb00103f1 | TCP: endpoint %1 (sockaddr=%3) closed.\r\n
0xb00103f2 | TCP: endpoint (Family=%6 PID=%4 ProcessSeqNum=%7) create failed: address family not attached.\r\n
0xb00103f3 | TCP: endpoint (Family=%6 Compartment=%5 PID=%4 ProcessSeqNum=%7) create failed: compartment not found.\r\n
0xb00103f4 | TCP: endpoint (Family=%6 Compartment=%5 PID=%4 ProcessSeqNum=%7) create failed: inspection status %3.\r\n
0xb00103f5 | TCP: endpoint (Family=%6 PID=%4 ProcessSeqNum=%7) created.\r\n
0xb00103f9 | TCP: listener (local=%2 remote=%4) accept completed. TCB = %8. PID = %6 ProcessSeqNum = %9.\r\n
0xb00103fa | TCP: connection %8 (local=%2 remote=%4 PID=%6 ProcessSeqNum=%9) connect failed: address family not attached.\r\n
0xb00103fc | TCP: connection %8 (local=%2 remote=%4 PID=%6 ProcessSeqNum=%9) connect failed: inspection status = %5.\r\n
0xb0010409 | TCP: connection %8 (local=%2 remote=%4) connect completed. PID = %6 ProcessSeqNum = %9.\r\n
0xb0010414 | TCP: connection %8 (local=%2 remote=%4) shutdown initiated (%5). PID = %6 ProcessSeqNum = %9.\r\n
0xb001041c | TCP: Process with PID = %1 ProcessSeqNum = %5 reserved %4 ports starting at %3.\r\n
0xb001041d | TCP: Process with PID = %1 ProcessSeqNum = %5 failed to reserve %4 ports starting at %3 with status = %2.\r\n
0xb001041e | TCP: Process with PID = %1 ProcessSeqNum = %5 completed global port reservation of %4 ports starting at %3 with status = %2.\r\n
0xb0010428 | TCP: Connection %1 %2 timer started. Scheduled to expire in %3 ms. Processor %4: LastInterruptTime %5 100-ns ticks; LastMicrosecondCount %6 msec; CachedKQPCValue %7 ticks; CachedFrequencyValue %8.\r\n
0xb0010452 | IP: Interface media disconnect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001045a | IP: Address DAD successful. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001045b | IP: Address DAD failed. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2, DL address of packet = %5.\r\n
0xb001045c | IP: Address DAD started. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001045d | TCP: listener (sockaddr=%3 PID=%5 ProcessSeqNum=%8) activation failed: address family not attached.\r\n
0xb001045e | TCP: listener %1 (family=%7 PID=%5 ProcessSeqNum=%8) activation failed: compartment %6 not found. Status=%4.\r\n
0xb001045f | TCP: listener %1 (family=%7 PID=%5 ProcessSeqNum=%8) activation failed: inspection status=%4.\r\n
0xb0010462 | TCP: listener %1 (family=%7 PID=%5 ProcessSeqNum=%8) bind failed: address %3 cannot be resolved (Status=%4).\r\n
0xb0010463 | TCP: listener %1 (sockaddr=%3 PID=%5 processseqnum=%8) activated.\r\n
0xb0010467 | IP: Address addition. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb0010468 | IP: Address deletion. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2.\r\n
0xb001046a | Framing: Interface operation status change. Interface = %1, Compartment = %4, Operational Status = %2, Operational Status Flags = %3.\r\n
0xb0010470 | Framing: NDIS pause event. Interface = %1, Compartment = %3.\r\n
0xb0010471 | Framing: NDIS restart event. Interface = %1, Compartment = %3.\r\n
0xb0010478 | IP: Interface property change. Interface = %1, Compartment = %10, Protocol = %11, Advertise = %2, AdvertiseDefaultRoute = %3, Forward = %4, ForwardMulticast = %5, UseNud = %6, AdvertisingEnabled = %7, WeakHostSend = %8, WeakHostReceive = %9.\r\n
0xb00104b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, Address = %4 %3 %6.\r\n
0xb00104b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7.\r\n
0xb00104bf | TCPIP: Network layer (Protocol %1, AddressFamily = %2) dropped %10 packet(s) on interface %16. SourceAddress = %13. DestAddress = %15. Reason = %9. Direction = %17.\r\n
0xb0010514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6. PID = %7. ProcessSeqNum = %8.\r\n
0xb0010521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, pattern priority = %6, interface medium = %7, Status = %12, Has been AOAC capable = %13.\r\n
0xb0010529 | IP: Interface media connect. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052a | IP: Interface limited link connectivity set. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052b | IP: Interface limited link connectivity reset. Interface = %1, Compartment = %3, Protocol = %2.\r\n
0xb001052c | IP: Neighbor state change. IPAddress = %3, DLAddress = %5, Interface = %1, Compartment = %9, OldState = %6, NewState = %7, Event = %8.\r\n
0xb001052d | IP: Neighbor Discovery. Event = %5, Interface = %1, Compartment = %6, SourceIpAddress = %3, TargetIpAddress = %4.\r\n
0xb001052f | IP: Address pair (%2, %3) is preferred over (%4, %5) by SortOptions: %6, Reason: %10 (Rule %7 %8.%9).\r\n
0xb0010534 | TCP: connection %1: TCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb0010535 | TCP: connection %1: TCP CTCP send event, SeqNo = %5, BytesSent = %4, CWnd = %2, SndWnd = %3, SRtt = %6, RttVar = %7, RTO = %8, RcvWnd = %9.\r\n
0xb001054d | TCPIP has failed a %1 request from %4 to %6 on endpoint %2 owned by process %8 processseqnum %10 with %7 since network interface %9 is in low-power mode.\r\n
0xb001054e | IP: Interface configuration flags updated. Interface = %1, Compartment = %5, Protocol = %6, Property = %2, Value = %3, Event = %4.\r\n
0xb0010557 | Nbl %1 OOB info (%2): TcpIpChecksumNetBufferListInfo %3, TcpLargeSendNetBufferListInfo %4, Ieee8021QNetBufferListInfo %5, NetBufferListHashValue %6, NetBufferListHashInfo %7, VirtualSubnetInfo %8, UdpSegmentationOffloadInfo/TcpRecvSegCoalesceInfo %9, NrtNameResolutionId/UdpRecvSegCoalesceOffloadInfo %10\r\n
0xb0010565 | TCP: AssociateNameResContext EndpointObj: %1 IsConnectionObj: %2 NameResContext: %3 Status: %4\r\n
0xb001056d | UDP: endpoint (family=%5 pid=%3 processseqnum=%6) create failed: address family not attached.\r\n
0xb001056e | UDP: endpoint %1 (family=%5 compartment=%4 pid=%3 processseqnum=%6) create failed: compartment not found.\r\n
0xb001056f | UDP: endpoint %1 (family=%5 compartment=%4 pid=%3 processseqnum=%6) created.\r\n
0xb0010570 | UDP: endpoint %1 (family=%5 compartment=%4 pid=%3 processseqnum=%6) create failed: inspection status = %2\r\n
0xb001058f | %1: %2path drop on interface %12. Type = %3, Code = %4, Reason = %5, Status = %6, CompartmentId = %7, SourceAddress = %9, DestAddress = %11.\r\n
0xb0010595 | TCP: connection %1: Cumulative Ack event, SeqNo = %5, BytesAcked = %4, CWnd = %2, SndWnd = %3, InRecovery = %6, TimeSinceLastLossMS = %7, CubicCwnd = %8, AimdCwnd = %9, K = %10, Wmax = %11, LastWmax = %12, MaxSndWnd = %13 IsLimitedSlowStart = %14.\r\n
0xb00105bc | TCP: connection %8 (local=%2 remote=%4) system abort. PID = %6 ProcessSeqNum = %9.\r\n
0xb00105be | TCP: endpoint %1 (sockaddr=%3) bind failed: wake status = %4.\r\n
0xb00105c5 | TCP: Connection %1 Summary: DataBytesOut %2 DataBytesIn %3 DataSegmentsOut %4 DataSegmentsIn %5 SegmentsOut %6 SegmentsIn %7 NonRecovDa \   %8 NonRecovDaEpisodes %9 DupAcksIn %10 BytesRetrans %11 Timeouts %12 SpuriousRtoDetections %13 FastRetran %14 MaxSsthresh %15 MaxSsCwnd %16 \   MaxCaCwnd %17 SndLimTransRwin %18 SndLimTimeRwin %19 SndLimBytesRwin %20 SndLimTransCwnd %21 SndLimTimeCwnd %22 SndLimBytesCwnd %23 \   SndLimTransSnd %24 SndLimTimeSnd %25 SndLimBytesSnd %26 ConnectionTimeMs %27 Timestamps %28 RttUs %29 MinRtt %30 MaxRtt %31 SynRetrans %32 CongestionAlgorithm %33 \   State %34 Local %36 Remote %38 CWnd %39 SsThresh %40 RcvWnd %41 RcvBuf %42 SndWnd %43 \   InterfaceIndex %44 LocalPort %45 IsLoopback %46.\r\n
0xb00105c8 | TCP connection failed with Status = %1, Local = %3, Remote = %5, ProcessId = %6, ProcessSeqNum = %12, TcpState = %7 at %8:%9:%10 Reason = %11.\r\n
0xb00105ca | UDP: Endpoint %1 segment message. SegmentSize = %2 (0 == No Segmentation) MessageLength = %3 HwDatagrams = %4 HwSegments = %5 SwSegments = %6 SubMssSegments = %7 Status = %8.\r\n
0xb00203f5 | TCP: endpoint %1 (Family=%7 Compartment=%6 PID=%5 ProcessSeqNum=%8) created.\r\n
0xb0020467 | IP: Address addition. Address = %7 %9 %8, Interface = %1, Compartment = %10, Protocol = %2, Prefix origin = %11, Suffix origin = %12.\r\n
0xb00204b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, Address = %4 %3 %6.\r\n
0xb00204b3 | IP: Interface linkspeed change. Interface = %1, Compartment = %8, OldLinkspeed = %9 bps, NewLinkspeed = %2 bps, PhysicalMediumType = %7, ReceiveLinkSpeed = %10 bps, MediaConnectState = %11.\r\n
0xb0020514 | TCP: connection %1 (local=%3 remote=%5) exists. State = %6, PID = %7, ProcessSeqNum = %8, SendTrackerEnabled = %9.\r\n
0xb0020521 | TCPIP: Interface index %1 wake pattern properties. AOAC capable = %2, Bitmap pattern supported = %3, ARP/ND offload supported = %4, IP address = %9 %11 %10 wake ready = %5, Wol handle = %14, pattern priority = %7, interface medium = %8, Status = %12, Has been AOAC capable = %13.\r\n
0xb00304b2 | IP: Interface rundown: Interface = %1, Compartment = %8, Metric = %11, Connected = %12, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, InternetConnectivityStatus = %13, Flags = %14, Address = %4 %3 %6.\r\n
0xb00404b2 | IP: Interface rundown: Interface = %1, Compartment = %8, IsolationId = %15, Metric = %11, Connected = %12, Linkspeed = %2 bps, PhysicalMediumType = %7, NetworkCategory = %10, InternetConnectivityStatus = %13, Flags = %14, Address = %4 %3 %6.\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | FALSE\r\n
0xd0000004 | TRUE\r\n
0xd0000005 |  \r\n
0xd0000006 | (Ignore IPv4 address), IPv6 address =\r\n
0xd0000007 | Unknown (Header corrupt / not parsed)\r\n
0xd0000008 | ICMP\r\n
0xd0000009 | IGMP\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ROUTING\r\n
0xd000000d | FRAGMENT\r\n
0xd000000e | GRE\r\n
0xd000000f | ESP\r\n
0xd0000010 | AH\r\n
0xd0000011 | ICMPV6\r\n
0xd0000012 | Unknown\r\n
0xd0000013 | Operational\r\n
0xd0000014 | Unoperational\r\n
0xd0000015 | Unknown\r\n
0xd0000016 | Dormant\r\n
0xd0000017 | IPV4\r\n
0xd0000018 | IPV6\r\n
0xd0000019 | ClosedState\r\n
0xd000001a | ListenState\r\n
0xd000001b | SynSentState\r\n
0xd000001c | SynRcvdState\r\n
0xd000001d | EstablishedState\r\n
0xd000001e | FinWait1State\r\n
0xd000001f | FinWait2State\r\n
0xd0000020 | CloseWaitState\r\n
0xd0000021 | ClosingState\r\n
0xd0000022 | LastAckState\r\n
0xd0000023 | TimeWaitState\r\n
0xd0000024 | TcpConnectionOffloadStateInHost\r\n
0xd0000025 | TcpConnectionOffloadStateOffloaded\r\n
0xd0000026 | RetransmitTimer\r\n
0xd0000027 | ConnectTimer\r\n
0xd0000028 | DelAckTimer\r\n
0xd0000029 | PushTimer\r\n
0xd000002a | KeepAliveTimer\r\n
0xd000002b | PacingTimer\r\n
0xd000002c | DisconnectTimer\r\n
0xd000002d | SwsTimer\r\n
0xd000002e | ReassemblyRateTimer\r\n
0xd000002f | SynOrRstValidationTimer\r\n
0xd0000030 | TCP_OFFLOAD_NO_PREFERENCE\r\n
0xd0000031 | TCP_OFFLOAD_NOT_PREFERRED\r\n
0xd0000032 | TCP_OFFLOAD_PREFERRED\r\n
0xd0000033 | TCP_KEEPALIVE\r\n
0xd0000034 | TCP_MAXSEG\r\n
0xd0000035 | TCP_MAXRT\r\n
0xd0000036 | TCP_STDURG\r\n
0xd0000037 | TCP_NOURG\r\n
0xd0000038 | TCP_ATMARK\r\n
0xd0000039 | TCP_NOSYNRETRIES\r\n
0xd000003a | TCP_TIMESTAMPS\r\n
0xd000003b | TCP_OFFLOAD_PREFERENCE\r\n
0xd000003c | TCP_CONGESTION_ALGORITHM\r\n
0xd000003d | TCP_DELAY_FIN_ACK\r\n
0xd000003e | SO_DEBUG\r\n
0xd000003f | SO_ACCEPTCONN\r\n
0xd0000040 | SO_REUSEADDR\r\n
0xd0000041 | SO_KEEPALIVE\r\n
0xd0000042 | SO_DONTROUTE\r\n
0xd0000043 | SO_BROADCAST\r\n
0xd0000044 | SO_USELOOPBACK\r\n
0xd0000045 | SO_LINGER\r\n
0xd0000046 | SO_OOBINLINE\r\n
0xd0000047 | SO_SNDBUF\r\n
0xd0000048 | SO_RCVBUF\r\n
0xd0000049 | SO_CONDITIONAL_ACCEPT\r\n
0xd000004a | SO_PAUSE_ACCEPT\r\n
0xd000004b | SO_COMPARTMENT_ID\r\n
0xd000004c | SO_RANDOMIZE_PORT\r\n
0xd000004d | SO_PORT_SCALABILITY\r\n
0xd000004e | NldsInvalid\r\n
0xd000004f | NldsTentative\r\n
0xd0000050 | NldsDuplicate\r\n
0xd0000051 | NldsDeprecated\r\n
0xd0000052 | NldsPreferred\r\n
0xd0000053 | Indicate\r\n
0xd0000054 | Pend\r\n
0xd0000055 | Satisfy\r\n
0xd0000056 | NdisPhysicalMediumUnspecified\r\n
0xd0000057 | NdisPhysicalMediumWirelessLan\r\n
0xd0000058 | NdisPhysicalMediumCableModem\r\n
0xd0000059 | NdisPhysicalMediumPhoneLine\r\n
0xd000005a | NdisPhysicalMediumDSL\r\n
0xd000005b | NdisPhysicalMedium1394\r\n
0xd000005c | NdisPhysicalMediumWirelessWan\r\n
0xd000005d | NdisPhysicalMediumNative802_11\r\n
0xd000005e | NdisPhysicalMediumBluetooth\r\n
0xd000005f | NdisPhysicalMediumInfiniband\r\n
0xd0000060 | NdisPhysicalMediumWiMax\r\n
0xd0000061 | NdisPhysicalMedium802_3\r\n
0xd0000062 | NdisPhysicalMedium802_5\r\n
0xd0000063 | NdisPhysicalMediumIrda\r\n
0xd0000064 | NdisPhysicalMediumWiredWAN\r\n
0xd0000065 | NdisPhysicalMediumWiredCoWan\r\n
0xd0000066 | NdisPhysicalMediumOther\r\n
0xd0000067 | NdisPhysicalMediumNative802_15_4\r\n
0xd0000068 | IP checksum offload not computed\r\n
0xd0000069 | TCP checksum offload not computed\r\n
0xd000006a | UDP checksum offload not computed\r\n
0xd000006b | Header not aligned on 4-byte boundary\r\n
0xd000006c | IP fragmentation\r\n
0xd000006d | Source address is not unicast\r\n
0xd000006e | Destination address is neither TCP/UDP unicast nor UDP multicast\r\n
0xd000006f | Ethernet and IP header not contiguous\r\n
0xd0000070 | IP options present\r\n
0xd0000071 | ESP over UDP\r\n
0xd0000072 | Lack contiguous space for upper layer headers\r\n
0xd0000073 | WFP filters present\r\n
0xd0000074 | Nexthop is unavailable\r\n
0xd0000075 | Path has been invalidated due to policy change\r\n
0xd0000076 | DHCP assigned IP address' promiscuous count is non-zero\r\n
0xd0000077 | ECN codepoint has not been negotiated for this traffic\r\n
0xd0000078 | Session state is not compatible\r\n
0xd0000079 | TCP options present\r\n
0xd000007a | UDP IPv6 checksum absent in packet\r\n
0xd000007b | Packet is for a loopback interface\r\n
0xd000007c | Packet is from a Raw Socket\r\n
0xd000007d | TL Ancillary headers present\r\n
0xd000007e | NL Ancillary headers present\r\n
0xd000007f | Type of Service present\r\n
0xd0000080 | IpSec headers present\r\n
0xd0000081 | Interface is not Ethernet\r\n
0xd0000082 | Nbl check failed\r\n
0xd0000083 | Destination address is unknown\r\n
0xd0000084 | Loopback inspect failed\r\n
0xd0000085 | Next header is not a transport protocol eligible for the fast path\r\n
0xd0000086 | IP packet length is invalid\r\n
0xd0000087 | IP version is invalid\r\n
0xd0000088 | Failed to allocate the WSD cache\r\n
0xd0000089 | Failure initializing PnP work queue\r\n
0xd000008a | Failed to get persistent parameters\r\n
0xd000008b | Rejected persistent parameters\r\n
0xd000008c | qualified profile\r\n
0xd000008d | qualified destination\r\n
0xd000008e | sample collection completion\r\n
0xd000008f | idle time expiration\r\n
0xd0000090 | allocation\r\n
0xd0000091 | new sample request\r\n
0xd0000092 | configuration change\r\n
0xd0000093 | Idle\r\n
0xd0000094 | ProbingWs\r\n
0xd0000095 | ProbeWait\r\n
0xd0000096 | ProbingWithoutWs\r\n
0xd0000097 | RecordWait\r\n
0xd0000098 | EreQualified\r\n
0xd0000099 | Qualified\r\n
0xd000009a | Source Unspecified\r\n
0xd000009b | Destination is multicast\r\n
0xd000009c | Header is invalid (location 0)\r\n
0xd000009d | Checksum is invalid\r\n
0xd000009e | Transport endpoint was not found\r\n
0xd000009f | Connected path error\r\n
0xd00000a0 | Session state error\r\n
0xd00000a1 | Receive Inspection\r\n
0xd00000a2 | ACK Invalid (subreason 0) (invalid ACK in SYN_SENT state)\r\n
0xd00000a3 | Expected SYN\r\n
0xd00000a4 | Received RST (subreason 0)\r\n
0xd00000a5 | Received SYN while in SYN_RCVD state\r\n
0xd00000a6 | Simultaneous Connect\r\n
0xd00000a7 | PAWS Failed\r\n
0xd00000a8 | Land Attack (subreason 0)\r\n
0xd00000a9 | Missed RST\r\n
0xd00000aa | Outside Receive Window (subreason 0)\r\n
0xd00000ab | Duplicate Segment\r\n
0xd00000ac | Closed Window\r\n
0xd00000ad | TCB Removed\r\n
0xd00000ae | FIN-WAIT2\r\n
0xd00000af | Reassembly Conflict\r\n
0xd00000b0 | FIN Received\r\n
0xd00000b1 | Listener received segment with invalid flags\r\n
0xd00000b2 | URG flag set but could not allocate urgent data state\r\n
0xd00000b3 | TCB was not inserted in TCB table\r\n
0xd00000b4 | TIME-WAIT TCB received RST outside receive window\r\n
0xd00000b5 | TIME-WAIT TCB received segment with SYN and other flags set\r\n
0xd00000b6 | Packet dropped by TIME-WAIT TCB (subreason 0)\r\n
0xd00000b7 | SYN+ACK with Fastopen cookie request\r\n
0xd00000b8 | Listener dropped SYN because SO_PAUSE_ACCEPT was set\r\n
0xd00000b9 | Listener dropped SYN to reduce memory pressure\r\n
0xd00000ba | Accept inspection\r\n
0xd00000bb | Accept redirection\r\n
0xd00000bc | Bad source address\r\n
0xd00000bd | Not locally destined\r\n
0xd00000be | Protocol unreachable\r\n
0xd00000bf | Port unreachable\r\n
0xd00000c0 | Bad length\r\n
0xd00000c1 | Malformed Header\r\n
0xd00000c2 | No route available\r\n
0xd00000c3 | Beyond scope\r\n
0xd00000c4 | Inspection drop\r\n
0xd00000c5 | Too many decapsulations\r\n
0xd00000c6 | Administratively prohibited\r\n
0xd00000c7 | Bad checksum\r\n
0xd00000c8 | Hop limit exceeded\r\n
0xd00000c9 | Address unreachable\r\n
0xd00000ca | RSC packet\r\n
0xd00000cb | Arbitration unhandled\r\n
0xd00000cc | Inspection absorb\r\n
0xd00000cd | Fragment MTU exceeded\r\n
0xd00000ce | Buffer Length Exceeded\r\n
0xd00000cf | Address Resolution Timeout\r\n
0xd00000d0 | Address Resolution Failure\r\n
0xd00000d1 | IPsec failure\r\n
0xd00000d2 | Extension Headers Failure\r\n
0xd00000d3 | Allocation Failure\r\n
0xd00000d4 | IPSNPI Client Drop\r\n
0xd00000d5 | Unsupported Offload\r\n
0xd00000d6 | Routing Failure\r\n
0xd00000d7 | Ancillary Data Failure\r\n
0xd00000d8 | Raw Data Failure\r\n
0xd00000d9 | Session State Failure\r\n
0xd00000da | IPSNPI Allocation Failure\r\n
0xd00000db | IPSNPI Modified But Not Forwarded\r\n
0xd00000dc | IPSNPI No Next Hop Specified\r\n
0xd00000dd | IPSNPI Compartment Not Found\r\n
0xd00000de | IPSNPI Interface Not Found\r\n
0xd00000df | IPSNPI Subinterface Not Found\r\n
0xd00000e0 | IPSNPI Interface Disabled\r\n
0xd00000e1 | IPSNPI Segmentation Failed\r\n
0xd00000e2 | IPSNPI No Ethernet Header\r\n
0xd00000e3 | IPSNPI Unexpected Fragment\r\n
0xd00000e4 | IPSNPI Unsupported Interface Type\r\n
0xd00000e5 | Invalid LSO info\r\n
0xd00000e6 | Invalid USO info\r\n
0xd00000e7 | Unexpected internal error\r\n
0xd00000e8 | Administratively configured setting\r\n
0xd00000e9 | Bad option\r\n
0xd00000ea | This type of packet is not accepted over loopback\r\n
0xd00000eb | Scope of address is too limited\r\n
0xd00000ec | Full queue\r\n
0xd00000ed | Disabled interface\r\n
0xd00000ee | URO segment size exceeds forward interface MTU\r\n
0xd00000ef | Default\r\n
0xd00000f0 | NewReno\r\n
0xd00000f1 | CTCP\r\n
0xd00000f2 | DCTCP\r\n
0xd00000f3 | LEDBAT\r\n
0xd00000f4 | CUBIC\r\n
0xd00000f5 | TcpTemplateTypeInternet\r\n
0xd00000f6 | TcpTemplateTypeDatacenter\r\n
0xd00000f7 | TcpTemplateTypeCompat\r\n
0xd00000f8 | TcpTemplateTypeDatacenterCustom\r\n
0xd00000f9 | TcpTemplateTypeInternetCustom\r\n
0xd00000fa | TcpTemplateTypeDefault\r\n
0xd00000fb | TcpTemplateTypeAutomatic\r\n
0xd00000fc | No Failure\r\n
0xd00000fd | Unknown\r\n
0xd00000fe | System Policy\r\n
0xd00000ff | NIC Capacity Reached\r\n
0xd0000100 | System Low On Memory\r\n
0xd0000101 | WFP driver / Stream inspection\r\n
0xd0000102 | Weak Host Model Enabled\r\n
0xd0000103 | Forwarding Enabled\r\n
0xd0000104 | Hardware capability\r\n
0xd0000105 | NDIS filter/NIC property\r\n
0xd0000106 | Loopback fast path socket option not set on both ends\r\n
0xd0000107 | Filter policy existed for the loopback connection\r\n
0xd0000108 | IPv4\r\n
0xd0000109 | IPv6\r\n
0xd000010a | unbind\r\n
0xd000010b | bind\r\n
0xd000010c | port change\r\n
0xd000010d | none\r\n
0xd000010e | receive hash\r\n
0xd000010f | receive scale\r\n
0xd0000110 | enabled\r\n
0xd0000111 | disabled\r\n
0xd0000112 | removing\r\n
0xd0000113 | adding\r\n
0xd0000114 | complete binding initialization\r\n
0xd0000115 | complete port initialization\r\n
0xd0000116 | enumerate interface ports\r\n
0xd0000117 | query port link state\r\n
0xd0000118 | query port interface index\r\n
0xd0000119 | query interface ports\r\n
0xd000011a | query port RSS capabilities\r\n
0xd000011b | get usable processors\r\n
0xd000011c | query port driver version\r\n
0xd000011d | query port RSS processor configuration\r\n
0xd000011e | set receive scale parameters\r\n
0xd000011f | set receive hash parameters\r\n
0xd0000120 | update interface ports\r\n
0xd0000121 | not available\r\n
0xd0000122 | available\r\n
0xd0000123 | available on ports\r\n
0xd0000124 | global configuration\r\n
0xd0000125 | active mode\r\n
0xd0000126 | Bind Adapter\r\n
0xd0000127 | Unbind Adapter (begin)\r\n
0xd0000128 | Unbind Adapter (end)\r\n
0xd0000129 | NetEvent Restart\r\n
0xd000012a | NetEvent Power-down\r\n
0xd000012b | NetEvent Power-up\r\n
0xd000012c | NetEvent NDK-enable\r\n
0xd000012d | NetEvent NDK-disable\r\n
0xd000012e | NetEvent NDK usage stopped\r\n
0xd000012f | Indicate new NDK interface arrival\r\n
0xd0000130 | Indicate NDK interface removal\r\n
0xd0000131 | Indicate NDK operational status change\r\n
0xd0000132 | Undefined\r\n
0xd0000133 | Adapter\r\n
0xd0000134 | QP\r\n
0xd0000135 | CQ\r\n
0xd0000136 | MR\r\n
0xd0000137 | MW\r\n
0xd0000138 | PD\r\n
0xd0000139 | SharedEndpoint\r\n
0xd000013a | Connector\r\n
0xd000013b | Listener\r\n
0xd000013c | SRQ\r\n
0xd000013d | Max\r\n
0xd000013e | Async\r\n
0xd000013f | Inline\r\n
0xd0000140 | Local\r\n
0xd0000141 | Remote\r\n
0xd0000142 | Privileged\r\n
0xd0000143 | Local\r\n
0xd0000144 | Remote\r\n
0xd0000145 | NotifyErrors\r\n
0xd0000146 | NotifyAny\r\n
0xd0000147 | NotifySolicited\r\n
0xd0000148 | Invalid\r\n
0xd0000149 | Software Slot allocated\r\n
0xd000014a | Hardware Slot allocated\r\n
0xd000014b | Policy error\r\n
0xd000014c | system error\r\n
0xd000014d | Enabled\r\n
0xd000014e | Send request dropped\r\n
0xd000014f | Receive dropped\r\n
0xd0000150 | Disconnect request dropped\r\n
0xd0000151 | Reset dropped\r\n
0xd0000152 | WFP API No Failure\r\n
0xd0000153 | WFP API WasRedirectedToProxy\r\n
0xd0000154 | WFP API RegisterForExitingEndpoint\r\n
0xd0000155 | WFP API ClassifiableFieldGetAf\r\n
0xd0000156 | WFP API ClassifiableFieldGetAfPostWait\r\n
0xd0000157 | WFP API ClassifiableFieldGetLocalPort\r\n
0xd0000158 | WFP API ClassifiableFieldGetRemotePort\r\n
0xd0000159 | WFP API ClassifiableFieldGetLocalAddress\r\n
0xd000015a | WFP API ClassifiableFieldGetRemoteAddress\r\n
0xd000015b | Processor Add\r\n
0xd000015c | Power Source Change\r\n
0xd000015d | AC\r\n
0xd000015e | DC\r\n
0xd000015f | DC Short Term\r\n
0xd0000160 | Unknown\r\n
0xd0000161 | is stopping timers\r\n
0xd0000162 | has stopped timers\r\n
0xd0000163 | is locking partitions\r\n
0xd0000164 | has locked partitions\r\n
0xd0000165 | is unlocking partitions\r\n
0xd0000166 | has unlocked partitions\r\n
0xd0000167 | is starting timers\r\n
0xd0000168 | has started timers\r\n
0xd0000169 | is starting\r\n
0xd000016a | is complete\r\n
0xd000016b | IP\r\n
0xd000016c | TCP\r\n
0xd000016d | leaving S0\r\n
0xd000016e | entering S0\r\n
0xd000016f | Unreachable\r\n
0xd0000170 | Incomplete\r\n
0xd0000171 | Probe\r\n
0xd0000172 | Delay\r\n
0xd0000173 | Stale\r\n
0xd0000174 | Reachable\r\n
0xd0000175 | Permanent\r\n
0xd0000176 | Maximum\r\n
0xd0000177 | Map\r\n
0xd0000178 | Configure\r\n
0xd0000179 | TlSuspectsReachability\r\n
0xd000017a | TlConfirmsReachability\r\n
0xd000017b | NaConfirmsReachability\r\n
0xd000017c | ProbeReachability\r\n
0xd000017d | DadSolicitation\r\n
0xd000017e | NewDlAddress\r\n
0xd000017f | TriggerNud\r\n
0xd0000180 | Resolve\r\n
0xd0000181 | Timeout\r\n
0xd0000182 | Sending neighbor solicitation\r\n
0xd0000183 | Received neighbor solicitation\r\n
0xd0000184 | Sending neighbor advertisement\r\n
0xd0000185 | Received neighbor advertisement\r\n
0xd0000186 | Sending router solicitation\r\n
0xd0000187 | Received router solicitation\r\n
0xd0000188 | Sending router advertisement\r\n
0xd0000189 | Received router advertisement\r\n
0xd000018a | Receive\r\n
0xd000018b | ReceiveAndInvalidate\r\n
0xd000018c | Send\r\n
0xd000018d | FastRegister\r\n
0xd000018e | Bind\r\n
0xd000018f | Invalidate\r\n
0xd0000190 | Read\r\n
0xd0000191 | Write\r\n
0xd0000192 | Not Activated\r\n
0xd0000193 | Activated\r\n
0xd0000194 | TCP connect\r\n
0xd0000195 | TCP send\r\n
0xd0000196 | UDP send\r\n
0xd0000197 | RAW send\r\n
0xd0000198 | Received Router Advertisement\r\n
0xd0000199 | AdminConfigured\r\n
0xd000019a | NetworkProperty\r\n
0xd000019b | CreateWolContext\r\n
0xd000019c | DeleteWolContext\r\n
0xd000019d | SetWolContext\r\n
0xd000019e | ClearWolContext\r\n
0xd000019f | WolContextEvicted\r\n
0xd00001a0 | AddWolAddress\r\n
0xd00001a1 | RemoveWolAddress\r\n
0xd00001a2 | Send\r\n
0xd00001a3 | Receive\r\n
0xd00001a4 | WFP-ALE: RemoteEndPoint Address\r\n
0xd00001a5 | WFP-ALE: RemoteEndPoint Port\r\n
0xd00001a6 | WFP-ALE: LocalEndPoint Address\r\n
0xd00001a7 | WFP-ALE: LocalEndPoint Port\r\n
0xd00001a8 | WFP-ALE: Partition Id\r\n
0xd00001a9 | WFP-ALE: Parition NumEnties\r\n
0xd00001aa | SlowDownEntry\r\n
0xd00001ab | SlowDownExit\r\n
0xd00001ac | SlowDownTracking\r\n
0xd00001ad | BaseDelayUpdate\r\n
0xd00001ae | Ack\r\n
0xd00001af | DupAck\r\n
0xd00001b0 | Timeout\r\n
0xd00001b1 | Ecn\r\n
0xd00001b2 | SpuriousTimeout\r\n
0xd00001b3 | Loss Recovery\r\n
0xd00001b4 | Network Context Constraint\r\n
0xd00001b5 | Prefix Length Policy\r\n
0xd00001b6 | Start Epoch Policy\r\n
0xd00001b7 | Default Routes Disabled On Interface\r\n
0xd00001b8 | Unconstrained Lookup Disallowed On Interface\r\n
0xd00001b9 | Interface Disconnected\r\n
0xd00001ba | Route Invalid Lifetime\r\n
0xd00001bb | Interface Constraint\r\n
0xd00001bc | Scope Constraint\r\n
0xd00001bd | Unconstrained Offlink Route Lookup Disallowed On Interface\r\n
0xd00001be | Rechability\r\n
0xd00001bf | Prefix Length\r\n
0xd00001c0 | Route And Interface Metrics\r\n
0xd00001c1 | Destination And Source Hash\r\n
0xd00001c2 | Route Order\r\n
0xd00001c3 | Dead Gateway\r\n
0xd00001c4 | OnLink Route\r\n
0xd00001c5 | Prefer Same Address\r\n
0xd00001c6 | Prefer Appropriate Scope\r\n
0xd00001c7 | Avoid Deprecated Addresses\r\n
0xd00001c8 | Prefer Home Addresses\r\n
0xd00001c9 | Prefer Outgoing Interface\r\n
0xd00001ca | Prefer Addresses Associated With NextHop\r\n
0xd00001cb | Prefer Matching Label\r\n
0xd00001cc | Prefer Temporary Addresses\r\n
0xd00001cd | System Defined Preference (Windows Specific)\r\n
0xd00001ce | Prefer Longest Matching Prefix With NextHop (Windows Specific)\r\n
0xd00001cf | Prefer Longest Matching Prefix\r\n
0xd00001d0 | TimerArmed\r\n
0xd00001d1 | TimerFired\r\n
0xd00001d2 | Failed\r\n
0xd00001d3 | Init\r\n
0xd00001d4 | SetTimeSlotData\r\n
0xd00001d5 | SetTailTimeSlot\r\n
0xd00001d6 | EraseTimestamps\r\n
0xd00001d7 | GetRecoverySeq\r\n
0xd00001d8 | RttSampleUpdate\r\n
0xd00001d9 | TcpFastopenOff\r\n
0xd00001da | TcpFastopenAccepting\r\n
0xd00001db | TcpFastopenServerSendingCookie\r\n
0xd00001dc | TcpFastopenServerSentCookie\r\n
0xd00001dd | TcpFastopenNegotiate\r\n
0xd00001de | TcpFastopenAttempt\r\n
0xd00001df | TcpFastopenNegotiateSuccess\r\n
0xd00001e0 | TcpFastopenAttemptSuccess\r\n
0xd00001e1 | TcpFastopenCookieRollover\r\n
0xd00001e2 | TcpFastopenFailed\r\n
0xd00001e3 | TcpFastopenFailedBlocklist\r\n
0xd00001e4 | TcpFastopenServerAcceptSuccess\r\n
0xd00001e5 | TcpFastopenServerAcceptTimeout\r\n
0xd00001e6 | TcpFastopenServerAcceptSendData\r\n
0xd00001e7 | TcpFastopenFailedSimultaneousConnect\r\n
0xd00001e8 | TcpFastopenFailedInvalidCookie\r\n
0xd00001e9 | TcpFastopenFailedSynTimeout\r\n
0xd00001ea | TcpFastopenFailedTimeout\r\n
0xd00001eb | TcpFastopenFailedReset\r\n
0xd00001ec | TcpFastopenFallback\r\n
0xd00001ed | TcpFastopenCookieRequestDeclined\r\n
0xd00001ee | TcpFastopenFailedSuddenRttIncrease\r\n
0xd00001ef | TcpFastopenFailedSynAckWithCookieRequest\r\n
0xd00001f0 | TcpFastopenFailedNoNextHop\r\n
0xd00001f1 | General failure\r\n
0xd00001f2 | Truncated header\r\n
0xd00001f3 | Invalid checksum\r\n
0xd00001f4 | Inspection drop\r\n
0xd00001f5 | Rejecting loopback neighbor discovery\r\n
0xd00001f6 | Unknown type/code\r\n
0xd00001f7 | Truncated IP header\r\n
0xd00001f8 | Oversized IP header\r\n
0xd00001f9 | No handler\r\n
0xd00001fa | Not responding with error for error\r\n
0xd00001fb | Invalid source\r\n
0xd00001fc | Interface rate limit\r\n
0xd00001fd | Path rate limit\r\n
0xd00001fe | No route\r\n
0xd00001ff | No matching request\r\n
0xd0000200 | Buffer too small\r\n
0xd0000201 | Failed to obtain ancillary data\r\n
0xd0000202 | Incorrect hop limit\r\n
0xd0000203 | Unknown code\r\n
0xd0000204 | Source not linklocal\r\n
0xd0000205 | Truncated ND header\r\n
0xd0000206 | Invalid ND option SourceLinkAddr\r\n
0xd0000207 | Invalid ND option MTU\r\n
0xd0000208 | Invalid ND option PrefixInformation\r\n
0xd0000209 | Invalid ND option RouteInformation\r\n
0xd000020a | Invalid ND option RDNSS\r\n
0xd000020b | Invalid ND option DNSSL\r\n
0xd000020c | Packet parsing failure\r\n
0xd000020d | Disallowed by the current configuration\r\n
0xd000020e | Invalid router advertisement\r\n
0xd000020f | Source address is not on the same link as this interface\r\n
0xd0000210 | Invalid destination or target address for redirect message\r\n
0xd0000211 | Invalid neighbor discovery target\r\n
0xd0000212 | Invalid neighbor advertisement - the solicited flag cannot be set if the destination address is multicast\r\n
0xd0000213 | The link layer address belongs to this interface\r\n
0xd0000214 | Insufficient resources\r\n
0xd0000215 | Duplicate echo request\r\n
0xd0000216 | Router advertisement came from a router that is not part of the potential router list\r\n
0xd0000217 | Invalid MLD query\r\n
0xd0000218 | Invalid MLD report\r\n
0xd0000219 | Received MLD report from local machine\r\n
0xd000021a | Not locally destined\r\n
0xd000021b | Echo Reply\r\n
0xd000021c | Destination Unreachable\r\n
0xd000021d | Packet Too Big\r\n
0xd000021e | Destination Unreachable(v4)/Time Exceeded(v6)\r\n
0xd000021f | Source Quench(v4)/Parameter Problem(v6)\r\n
0xd0000220 | Redirect\r\n
0xd0000221 | Echo Request\r\n
0xd0000222 | Router Advertisement\r\n
0xd0000223 | Router Solicitation\r\n
0xd0000224 | Time Exceeded\r\n
0xd0000225 | Parameter Problem\r\n
0xd0000226 | Timestamp Request\r\n
0xd0000227 | Timestamp Reply\r\n
0xd0000228 | Address Mask Request\r\n
0xd0000229 | Address Mask Reply\r\n
0xd000022a | Echo Request\r\n
0xd000022b | Echo Reply\r\n
0xd000022c | Multicast Listener Query\r\n
0xd000022d | Multicast Listener Report\r\n
0xd000022e | Multicast Listener Done\r\n
0xd000022f | Router Solicitation\r\n
0xd0000230 | Router Advertisement\r\n
0xd0000231 | Neighbor Solicitation\r\n
0xd0000232 | Neighbor Advertisement\r\n
0xd0000233 | Redirect Message\r\n
0xd0000234 | Multicast Listener Discovery\r\n
0xd0000235 | Not Parsed\r\n
0xd0000236 | Periodic\r\n
0xd0000237 | Aperiodic\r\n
0xd0000238 | Unknown\r\n
0xd0000239 | Public\r\n
0xd000023a | Private\r\n
0xd000023b | Domain\r\n
0xd000023c | Remote\r\n
0xd000023d | Link\r\n
0xd000023e | NonDomainNetwork\r\n
0xd000023f | DomainNetwork\r\n
0xd0000240 | DomainAuthenticated\r\n
0xd0000241 | InterfaceAddition\r\n
0xd0000242 | InterfaceDeletion\r\n
0xd0000243 | ZoneChange\r\n
0xd0000244 | ConfigurationFlagChange\r\n
0xd0000245 | ForwardingEnable\r\n
0xd0000246 | ForwardingDisable\r\n
0xd0000247 | WeakHostReceiveEnable\r\n
0xd0000248 | WeakHostReceiveDisable\r\n
0xd0000249 | NetworkCategoryStateChange\r\n
0xd000024a | MetricChange\r\n
0xd000024b | MediaConnect\r\n
0xd000024c | MediaDisconnect\r\n
0xd000024d | OffloadCapabilityChange\r\n
0xd000024e | DisableDefaultRoutesSet\r\n
0xd000024f | DisableDefaultRoutesReset\r\n
0xd0000250 | ForceTunnelingSet\r\n
0xd0000251 | ForceTunnelingReset\r\n
0xd0000252 | LimitedLinkConnectivitySet\r\n
0xd0000253 | LimitedLinkConnectivityReset\r\n
0xd0000254 | LocalityConfigChange\r\n
0xd0000255 | RoutingFlagsSet\r\n
0xd0000256 | RoutingFlagsReset\r\n
0xd0000257 | PortStateChange\r\n
0xd0000258 | RscUnawareIpsnpiClientPresent\r\n
0xd0000259 | RscUnawareIpsnpiClientAbsent\r\n
0xd000025a | PromiscuousModeEnabled\r\n
0xd000025b | PromiscuousModeDisabled\r\n
0xd000025c | NoInternetConnectivity\r\n
0xd000025d | NoInternetDnsResolutionSucceeded\r\n
0xd000025e | InternetConnectivityDetected\r\n
0xd000025f | InternetConnectivityUnknown\r\n
0xd0000260 | Timeout\r\n
0xd0000261 | DadStarted\r\n
0xd0000262 | OptimisticDadStarted\r\n
0xd0000263 | DadPassed\r\n
0xd0000264 | NSReceived\r\n
0xd0000265 | NAReceived\r\n
0xd0000266 | InterfaceDisabled\r\n
0xd0000267 | DadDisabled\r\n
0xd0000268 | AddressAddition\r\n
0xd0000269 | AddressDeletion\r\n
0xd000026a | DadStatePreferred\r\n
0xd000026b | DadStateDuplicate\r\n
0xd000026c | DadStateDeprecated\r\n
0xd000026d | SkipAsSourceSet\r\n
0xd000026e | SkipAsSourceReset\r\n
0xd000026f | TunnelSkipAsSourceSet\r\n
0xd0000270 | TunnelSkipAsSourceReset\r\n
0xd0000271 | ZoneChange\r\n
0xd0000272 | NeighborAddition\r\n
0xd0000273 | NeighborDeletion\r\n
0xd0000274 | NeighborUnreachable\r\n
0xd0000275 | NeighborReachable\r\n
0xd0000276 | NeighborAddressUpdate\r\n
0xd0000277 | DeadRouteTimeout\r\n
0xd0000278 | DeadRouteProbeTimeout\r\n
0xd0000279 | AllRoutesDead\r\n
0xd000027a | TlConfirmsForwardReachability\r\n
0xd000027b | DeadGatewayDetected\r\n
0xd000027c | RouterRedirect\r\n
0xd000027d | ProbeConnectionFailed\r\n
0xd000027e | ConfigurationChange\r\n
0xd000027f | Alive\r\n
0xd0000280 | Dead\r\n
0xd0000281 | Probe\r\n
0xd0000282 | Disable\r\n
0xd0000283 | Enable\r\n
0xd0000284 | NotConfident\r\n
0xd0000285 | InvalidLoad\r\n
0xd0000286 | ConfidenceUpdate\r\n
0xd0000287 | TCP Fastopen\r\n
0xd0000288 | Init\r\n
0xd0000289 | StatusIndication\r\n
0xd000028a | GlobalSetting\r\n
0xd000028b | Forwarding\r\n
0xd000028c | IncompatibleCallout\r\n
0xd000028d | RA DNS information change\r\n
0xd000028e | RA DNS entry added\r\n
0xd000028f | RA DNS entry expired by RA\r\n
0xd0000290 | RA DNS entry expired by timer\r\n
0xd0000291 | RA DNS entry lifetime reset\r\n
0xd0000292 | RA DNS entry reordered\r\n
0xd0000293 | RA DNS entry deleted due to max limit\r\n
0xd0000294 | RA DNS entry lifetime updated\r\n
0xd0000295 | RA DNS ND entry ignored due to limit\r\n
0xd0000296 | RA DNS ND entry ignored due to memory failure\r\n
0xd0000297 | RA DNS ND entry ignored due to zero lifetime\r\n
0xd0000298 | RA DNS ND entries corrupted\r\n
0xd0000299 | RA DNS RouterContext init failed\r\n
0xd000029a | RA DNS ND entry invalid\r\n
0xd000029b | RA DNS ND entry duplicate\r\n
0xd000029c | Manual\r\n
0xd000029d | WellKnown\r\n
0xd000029e | DHCP\r\n
0xd000029f | RouterAdvertisement\r\n
0xd00002a0 | 6to4\r\n
0xd00002a1 | Avoid Unusable Destination\r\n
0xd00002a2 | Prefer Aoac Interface\r\n
0xd00002a3 | Prefer Matching Scope\r\n
0xd00002a4 | Avoid Deprecated Address\r\n
0xd00002a5 | Prefer Matching Label\r\n
0xd00002a6 | Prefer Internet Connected Interface\r\n
0xd00002a7 | Prefer Higher Precedence\r\n
0xd00002a8 | Prefer Longer Route Destination Prefix\r\n
0xd00002a9 |  Prefer Native Transport(Physical Interface)\r\n
0xd00002aa | Prefer Lower Interface Metric\r\n
0xd00002ab | Prefer Smaller Scope\r\n
0xd00002ac | Prefer Same Address\r\n
0xd00002ad | Prefer Appropriate Scope\r\n
0xd00002ae | Avoid Deprecated Address\r\n
0xd00002af | Prefer Outgoing Interface\r\n
0xd00002b0 | Prefer Source Address Associated With Nexthop\r\n
0xd00002b1 | Prefer Temporary Address\r\n
0xd00002b2 | System Defined Preference\r\n
0xd00002b3 | Prefer Source With Longer NextHop Prefix Match\r\n
0xd00002b4 | Locality Metric\r\n
0xd00002b5 | Prefer Longer Source/Destination Common Prefix Length\r\n
0xd00002b6 | Order Unchanged (No Preference)\r\n
0xd00002b7 | Send\r\n
0xd00002b8 | Disconnect\r\n
0xd00002b9 | Accept\r\n
0xd00002ba | Receive\r\n
0xd00002bb | ReceiveTcpDatagram\r\n
0xd00002bc | ReceiveDatagram\r\n
0xd00002bd | RemoteDisconnect\r\n
0xd00002be | ReceiveControlMessage\r\n
0xd00002bf | RespondDatagram\r\n
0xd00002c0 | BindEndpoint\r\n
0xd00002c1 | Listen\r\n
0xd00002c2 | AcceptComplete\r\n
0xd00002c3 | Connect\r\n
0xd00002c4 | ConnectComplete\r\n
0xd00002c5 | Raw\r\n
0xd00002c6 | ConnectRequest\r\n
0xd00002c7 | CreateEndpoint\r\n
0xd00002c8 | AcquirePort\r\n
0xd00002c9 | Offload\r\n
0xd00002ca | SocketOption\r\n
0xd00002cb | BindEndpointRequest\r\n
0xd00002cc | Drop\r\n
0xd00002cd | Allow\r\n
0xd00002ce | Pend\r\n
0xd00002cf | DropAndSendIcmp\r\n
0xd00002d0 | Allow\r\n
0xd00002d1 | Deny\r\n
0xd00002d2 | Authorize\r\n
0xd00002d3 | RetryWithHint\r\n
0xd00002d4 | Reference\r\n
0xd00002d5 | Coalesced\r\n
0xd00002d6 | Dedicated\r\n
0xd00002d7 | FailureMemory\r\n
0xd00002d8 | FailurePlumbing\r\n
0xd00002d9 | NotFound\r\n
0xd00002da | Found\r\n
0xd00002db | Done\r\n
0xd00002dc | Loopback Ethernet packet\r\n
0xd00002dd | Invalid Snap header\r\n
0xd00002de | Invalid ethernet type\r\n
0xd00002df | Invalid packet length\r\n
0xd00002e0 | Header not contiguous\r\n
0xd00002e1 | Invalid destination type\r\n
0xd00002e2 | Allocation failure\r\n
0xd00002e3 | Interface reference failure\r\n
0xd00002e4 | Packet provider reference failure\r\n
0xd00002e5 | Invalid LSO information\r\n
0xd00002e6 | Receive discarded\r\n
0xd00002e7 | Listener received a packet other than SYN\r\n
0xd00002e8 | Listener was paused\r\n
0xd00002e9 | Listener inspection rejected\r\n
0xd00002ea | SYN was not acked in SynTcb receive\r\n
0xd00002eb | Received invalid ACK\r\n
0xd00002ec | Received SYN+ACK with TFO cookie request\r\n
0xd00002ed | Received in-window SYN in unexpected TCP state\r\n
0xd00002ee | Received invalid ACK in SynRcvd state\r\n
0xd00002ef | Received SYN and other flags in Timewait state\r\n
0xd00002f0 | Connection aborted\r\n
0xd00002f1 | Bind endpoint was failed by InetInspect\r\n
0xd00002f2 | Bind endpoint request was failed by InetInspect\r\n
0xd00002f3 | Listen was failed by InetInspect\r\n
0xd00002f4 | Listener receive was failed by InetInspect\r\n
0xd00002f5 | Accept complete was failed by InetInspect\r\n
0xd00002f6 | Create endpoint was failed by InetInspect\r\n
0xd00002f7 | Create connect endpoint was failed by InetInspect\r\n
0xd00002f8 | Create listen endpoint was failed by InetInspect\r\n
0xd00002f9 | Connect request was failed by InetInspect\r\n
0xd00002fa | Connect request was failed by InetInspect\r\n
0xd00002fb | Connect complete was failed by InetInspect\r\n
0xd00002fc | Rate-limited connect complete was failed by InetInspect\r\n
0xd00002fd | Connection was cancelled\r\n
0xd00002fe | Connection aborted\r\n
0xd00002ff | Failed to send SYN packet\r\n
0xd0000300 | Failed to insert connection\r\n
0xd0000301 | Delivery aborted on connection-reset or timeout\r\n
0xd0000302 | An early disconnect injected\r\n
0xd0000303 | Connection was aborted by the system\r\n
0xd0000304 | Network name was deleted\r\n
0xd0000305 | Incompatible next hop\r\n
0xd0000306 | SegmentSize is larger than MTU\r\n
0xd0000307 | Raw listeners on path\r\n
0xd0000308 | IP extension headers present\r\n
0xd0000309 | Exceeds hardware capabilities\r\n
0xd000030a | Incompatible inspection callout\r\n
0xd000030b | Unknown\r\n
0xd000030c | Connected\r\n
0xd000030d | Disconnected\r\n
0xd000030e | IPPROTO_IP\r\n
0xd000030f | IPPROTO_IPV6\r\n
0xd0000310 | SOL_SOCKET\r\n
0xd0000311 | IP_OPTIONS/IPV6_HOPOPTS\r\n
0xd0000312 | IP_HDRINCL/IPV6_HDRINCL\r\n
0xd0000313 | IP_TOS\r\n
0xd0000314 | IP_TTL/IPV6_UNICAST_HOPS\r\n
0xd0000315 | IP_MULTICAST_IF/IPV6_MULTICAST_IF\r\n
0xd0000316 | IP_MULTICAST_TTL/IPV6_MULTICAST_HOPS\r\n
0xd0000317 | IP_MULTICAST_LOOP/IPV6_MULTICAST_LOOP\r\n
0xd0000318 | IP_ADD_MEMBERSHIP/IPV6_ADD_MEMBERSHIP\r\n
0xd0000319 | IP_DROP_MEMBERSHIP/IPV6_DROP_MEMBERSHIP\r\n
0xd000031a | IP_DONTFRAGMENT/IPV6_DONTFRAG\r\n
0xd000031b | IP_ADD_SOURCE_MEMBERSHIP\r\n
0xd000031c | IP_DROP_SOURCE_MEMBERSHIP\r\n
0xd000031d | IP_BLOCK_SOURCE\r\n
0xd000031e | IP_UNBLOCK_SOURCE\r\n
0xd000031f | IP_PKTINFO/IPV6_PKTINFO\r\n
0xd0000320 | IP_HOPLIMIT/IP_RECVTTL/IPV6_HOPLIMIT\r\n
0xd0000321 | IP_RECEIVE_BROADCAST\r\n
0xd0000322 | IPV6_PROTECTION_LEVEL\r\n
0xd0000323 | IP_RECVIF/IPV6_RECVIF\r\n
0xd0000324 | IP_RECVDSTADDR/IPV6_RECVDSTADDR\r\n
0xd0000325 | IP_FLIST/IPV6_FLIST\r\n
0xd0000326 | IP_ADD_IFLIST/IPV6_ADD_FLIST\r\n
0xd0000327 | IP_DEL_IFLIST/IPV6_DEL_IFLIST\r\n
0xd0000328 | IP_RTHDR/IPV6_RTHDR\r\n
0xd0000329 | IP_UNICAST_IF/IPV6_UNICAST_IF\r\n
0xd000032a | IP_RECVRTHDR/IPV6_RECVRTHDR\r\n
0xd000032b | IP_RECVTCLASS/IP_RECVTOS/IPV6_RECVTCLASS\r\n
0xd000032c | MCAST_JOIN_GROUP\r\n
0xd000032d | MCAST_LEAVE_GROUP\r\n
0xd000032e | MCAST_BLOCK_SOURCE\r\n
0xd000032f | MCAST_UNBLOCK_SOURCE\r\n
0xd0000330 | MCAST_JOIN_SOURCE_GROUP\r\n
0xd0000331 | MCAST_LEAVE_SOURCE_GROUP\r\n
0xd0000332 | IP_ORIGINAL_ARRIVAL_IF/IPV6_ORIGINAL_ARRIVAL_IF\r\n
0xd0000333 | IP_ECN/IPV6_ECN\r\n
0xd0000334 | IP_PKTINFO_EX/IPV6_PKTINFO_EX\r\n
0xd0000335 | IP_WFP_REDIRECT_RECORDS/IPV6_WFP_REDIRECT_RECORDS\r\n
0xd0000336 | IP_WFP_REDIRECT_CONTEXT/IPV6_WFP_REDIRECT_CONTEXT\r\n
0xd0000337 | IP_MTU_DISCOVER\r\n
0xd0000338 | IP_NRT_INTERFACE/IPV6_NRT_INTERFACE\r\n
0xd0000339 | IP_RECVERR/IPV6_RECVERR\r\n
0xd000033a | SIO_GET_INTERFACE_LIST\r\n
0xd000033b | SIO_GET_MULTICAST_FILTER\r\n
0xd000033c | SIO_SET_MULTICAST_FILTER\r\n
0xd000033d | SIOCSMSFILTER\r\n
0xd000033e | SIOCGMSFILTER\r\n
0xd000033f | SIO_MULTIPOINT_LOOPBACK\r\n
0xd0000340 | SIO_MULTICAST_SCOPE\r\n
0xd0000341 | SIO_RCVALL\r\n
0xd0000342 | SIO_RCVALL_MCAST\r\n
0xd0000343 | SIO_RCVALL_IGMPMCAST\r\n
0xd0000344 | SIO_RCVALL_MCAST_IF\r\n
0xd0000345 | SIO_RCVALL_IF\r\n
0xd0000346 | SIO_ADDRESS_LIST_SORT\r\n
0xd0000347 | join group\r\n
0xd0000348 | leave group\r\n
0xd0000349 | join group and add source\r\n
0xd000034a | leave group and drop source\r\n
0xd000034b | block source\r\n
0xd000034c | unblock source\r\n
0xd000034d | set filter\r\n
0xd000034e | MLD level does not match protocol\r\n
0xd000034f | Invalid multicast address\r\n
0xd0000350 | Invalid multicast source address\r\n
0xd0000351 | Group already exists\r\n
0xd0000352 | No existing state for group\r\n
0xd0000353 | Group is in exclude mode\r\n
0xd0000354 | No existing state for group or group is in exclude mode\r\n
0xd0000355 | No existing state for group or group is in include mode\r\n
0xd0000356 | Failed to set the state for the group\r\n
0xd0000357 | Failed to create the state for the group\r\n
0xd0000358 | Failed to modify the state for the group\r\n
0xd0000359 | Successfully created multicast session state\r\n
0xd000035a | Another duplicate multicast session state exists, so no need to create a new one\r\n
0xd000035b | Successfully added sources to multicast group\r\n
0xd000035c | Successfully removed sources from multicast group\r\n
0xd000035d | Updated multicast group state; will send report\r\n
0xd000035e | Not modifying multicast group state\r\n
0xd000035f | Updated multicast discovery version\r\n
0xd0000360 | Failed to create multicast session state when updating the multicast group\r\n
0xd0000361 | Failed to create multicast session state from callback\r\n
0xd0000362 | Failed to create multicast session state when searching for the interface\r\n
0xd0000363 | Failed to create multicast session state because access is denied\r\n
0xd0000364 | Failed to create multicast session state when adding sources to the session state\r\n
0xd0000365 | Failed to create multicast session state when creating the address\r\n
0xd0000366 | Failed to add sources to multicast group\r\n
0xd0000367 | Failed to modify multicast session state because access is denied\r\n
0xd0000368 | WFP context to the fragment\r\n
0xd0000369 | WFP context from the fragment to the reassembly context\r\n
0xd000036a | leave\r\n
0xd000036b | join\r\n
0xd000036c | acquire\r\n
0xd000036d | release\r\n
0xd000036e | Unknown\r\n
0xd000036f | DAD\r\n
0xd0000370 | Router solicitation\r\n
0xd0000371 | WOL address pattern\r\n
0xd0000372 | WOL TCP pattern\r\n
0xd0000373 | WOL local port pattern\r\n
0xd0000374 | Reassembly is prohibited\r\n
0xd0000375 | Fragment was filtered out\r\n
0xd0000376 | Out of memory\r\n
0xd0000377 | Protocol does not match\r\n
0xd0000378 | Fragment causes total packet length to exceed maximum payload size\r\n
0xd0000379 | Packet length does not properly align\r\n
0xd000037a | The next header has the wrong IP option\r\n
0xd000037b | Received mixed IPSec and non-IPSec fragments\r\n
0xd000037c | Received zero length fragment\r\n
0xd000037d | Duplicate fragment\r\n
0xd000037e | Fragment falls beyond the data length\r\n
0xd000037f | Received a partially overlapping fragment\r\n
0xd0000380 | Failed to retreat NBL\r\n
0xd0000381 | Too many out of order fragments received\r\n
0xd0000382 | Jumbogram received\r\n
0xd0000383 | End of list\r\n
0xd0000384 | No operation\r\n
0xd0000385 | Security\r\n
0xd0000386 | Loose source route\r\n
0xd0000387 | Timestamp\r\n
0xd0000388 | Record route\r\n
0xd0000389 | Struct source route\r\n
0xd000038a | Stream ID\r\n
0xd000038b | Router alert\r\n
0xd000038c | Multi-destination\r\n
0xd000038d | Single byte pad\r\n
0xd000038e | Multiple byte pad\r\n
0xd000038f | Tunnel limit\r\n
0xd0000390 | Router alert\r\n
0xd0000391 | Jumbogram\r\n
0xd0000392 | NSAP address\r\n
0xd0000393 | Message length is not long enough\r\n
0xd0000394 | Data length must be greater than or equal to the size of the message header\r\n
0xd0000395 | Invalid message type\r\n
0xd0000396 | Invalid message level\r\n
0xd0000397 | Invalid data length for this option\r\n
0xd0000398 | Invalid hop limit value\r\n
0xd0000399 | Invalid type of service value\r\n
0xd000039a | Invalid hop-by-hop options\r\n
0xd000039b | Invalid routing header\r\n
0xd000039c | Invalid ECN field value\r\n
0xd000039d | Invalid option\r\n
0xd000039e | Option length is either too small or too large\r\n
0xd000039f | Option length must be greater than or equal to the size of the option header\r\n
0xd00003a0 | The length of the supplied buffer is smaller than the option length\r\n
0xd00003a1 | The option length is smaller than the minimum length for this option\r\n
0xd00003a2 | The option list must have space for an integral, non-zero number of entries\r\n
0xd00003a3 | The data alignment of the option payload is invalid\r\n
0xd00003a4 | Invalid flags\r\n
0xd00003a5 | Multi-byte options can only occur once, or the combination of options is invalid\r\n
0xd00003a6 | Invalid pointer value\r\n
0xd00003a7 | Invalid address value\r\n
0xd00003a8 | Invalid option\r\n
0xd00003a9 | Option length is either too small or too large\r\n
0xd00003aa | Option length must be greater than or equal to the size of the option header\r\n
0xd00003ab | The length of the supplied buffer is smaller than the option length\r\n
0xd00003ac | The option list must have space for an integral, non-zero number of entries\r\n
0xd00003ad | Invalid address value\r\n
0xd00003ae | This option cannot be specified by the user\r\n
0xd00003af | Message length is not long enough\r\n
0xd00003b0 | Data length must be greater than or equal to the size of the message header\r\n
0xd00003b1 | Invalid message level\r\n
0xd00003b2 | Invalid IP_PKTINFO_EX option length\r\n
0xd00003b3 | Invalid option length\r\n
0xd00003b4 | Interface not found\r\n
0xd00003b5 | Scope ID does not match the scope ID for the interface\r\n
0xd00003b6 | Failed to find or create address to return\r\n
0xd00003b7 | None\r\n
0xd00003b8 | Other\r\n
0xd00003b9 | Direct\r\n
0xd00003ba | 6to4\r\n
0xd00003bb | Teredo\r\n
0xd00003bc | ISATAP\r\n
0xd00003bd | IP-HTTPS\r\n
0xd00003be | Unknown tunnel type\r\n
0xd00003bf | ISATAP tunnels cannot bind to IPv4 interfaces\r\n
0xd00003c0 | 6to4 tunnels cannot bind to IPv4 interfaces\r\n
0xd00003c1 | Teredo tunnels cannot bind to IPv4 interfaces\r\n
0xd00003c2 | Bind started\r\n
0xd00003c3 | Bind completed\r\n
0xd00003c4 | Unbind started\r\n
0xd00003c5 | Unbind completed\r\n
0xd00003c6 | Add started\r\n
0xd00003c7 | Add completed\r\n
0xd00003c8 | Delete started\r\n
0xd00003c9 | Delete completed\r\n
0xd00003ca | NDIS open started\r\n
0xd00003cb | NDIS open completed\r\n
0xd00003cc | NDIS close failed\r\n
0xd00003cd | The miniport's NDIS version is below 6.40 and does not support isolation configuration\r\n
0xd00003ce | Failed to process isolation configuration\r\n
0xd00003cf | TCP SYN WOL pattern\r\n
0xd00003d0 | TCP port coalesced WOL pattern\r\n
0xd00003d1 | UDP port coalesced WOL pattern\r\n
0xd00003d2 | Local port WOL pattern\r\n
0xd00003d3 | Update started\r\n
0xd00003d4 | Update failed\r\n
0xd00003d5 | Update completed\r\n
0xd00003d6 | None\r\n
0xd00003d7 | Native VSID\r\n
0xd00003d8 | External VSID\r\n
0xd00003d9 | VLAN\r\n
0xd00003da | Invalid source\r\n
0xd00003db | Invalid target\r\n
0xd00003dc | The source address in the DL header belongs to this interface\r\n
0xd00003dd | Not locally destined\r\n
0xd00003de | IPSNPI client drop\r\n
0xd00003df | IPSNPI allocation failure\r\n
0xd00003e0 | IPSNPI modified but not forwarded\r\n
0xd00003e1 | IPSNPI no next hop specified\r\n
0xd00003e2 | IPSNPI compartment not found\r\n
0xd00003e3 | IPSNPI interface not found\r\n
0xd00003e4 | IPSNPI subinterface not found\r\n
0xd00003e5 | IPSNPI interface disabled\r\n
0xd00003e6 | IPSNPI no ethernet header\r\n
0xd00003e7 | IPSNPI unexpected fragment\r\n
0xd00003e8 | IPSNPI unsupported interface type\r\n
0xd00003e9 | Other\r\n
0xd00003ea | Manual\r\n
0xd00003eb | Well Known\r\n
0xd00003ec | DHCP\r\n
0xd00003ed | Router Advertisement\r\n
0xd00003ee | Other\r\n
0xd00003ef | Manual\r\n
0xd00003f0 | Well Known\r\n
0xd00003f1 | DHCP\r\n
0xd00003f2 | Link Layer Address\r\n
0xd00003f3 | Random\r\n
