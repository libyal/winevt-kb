## ws2_32.dll

Path: %SystemRoot%\system32\ws2_32.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x90000001 | Microsoft-Windows-Winsock Catalog Change\r\n
0x90000002 | Microsoft-Windows-Winsock Catalog Change/Operational\r\n
0x91000001 | Microsoft-Windows-Winsock Network Event\r\n
0x91000002 | Microsoft-Windows-Winsock Network Event/Operational\r\n
0xb0000001 | LSP %1 was installed in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000002 | LSP %1 was removed from the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000003 | LSP %1 was disabled in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000004 | The %1-bit catalog was reset by the administrator\r\n
0xb1000001 | Socket creation: %1 %2 %3 %4 %5\r\n
0xb1000002 | Socket bind: %1 %2 %3 %4 %5\r\n
0xb1000004 | Socket connect: %1 %2 %3 %4\r\n
0xb1000006 | Connect completed: %1 %2 %3\r\n
0xb1000007 | AFD initiated abort: %1 %2 %3\r\n
0xb1000008 | Transport initiated abort: %1 %2 %3\r\n
0xb1000009 | Failed send request: %1 %2 %3\r\n
0xb100000a | Failed WSASendMsg request: %1 %2 %3\r\n
0xb100000b | Failed recv request: %1 %2 %3\r\n
0xb100000c | Failed recvfrom request: %1 %2 %3\r\n
0xb100000d | Socket close: %1 %2 %3\r\n
0xb100000e | Socket cleanup (all references removed): %1 %2 %3\r\n
0xb100000f | Socket accept: %1 %2 %3 %4 %5\r\n
0xb1000011 | Accept failed: %1 %2 %3\r\n
0xb1000012 | Send posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000013 | Receive posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000014 | RecvFrom posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000015 | SendTo posted: %1 %2 %3 %4 %5 %6 %7 %8\r\n
0xb1000017 | Recv completed: %1 %2 %3 %4\r\n
0xb1000018 | Send completed: %1 %2 %3 %4\r\n
0xb1000019 | SendMsg completed: %1 %2 %3 %4\r\n
0xb100001a | RecvFrom completed: %1 %2 %3 %4 %5 %6 %7\r\n
0xb100001c | SendTo completed: %1 %2 %3 %4\r\n
0xb100001d | Socket option set: %1 %2 %3 %4\r\n
0xb100001e | Select/Poll posted: %1 %2 %3\r\n
0xb100001f | Select/Poll completed: %1 %2 %3\r\n
0xb1000020 | WSAEventSelect: %1 %2 %3\r\n
0xb1000021 | Datagram dropped: %1 %2 %3 %4 %5 %6\r\n
0xb1000023 | Connection indicated: %1 %2 %3 %4\r\n
0xb1000025 | Data indicated from transport: %1 %2 %3\r\n
0xb1000026 | Data indicated from transport: %1 %2 %3 %4 %5\r\n
0xb1000028 | Failed bind: %1 %2 %3\r\n
0xb1000029 | Disconnect indicated from transport: %1 %2\r\n
0xd1000001 | SOCK_STREAM\r\n
0xd1000002 | SOCK_DGRAM\r\n
0xd1000003 | SOCK_RAW\r\n
0xd1000004 | SOCK_RDM\r\n
0xd1000005 | SOCK_SEQPACKET\r\n
0xd1000006 | Attempt to flush pending receive requests failed\r\n
0xd1000007 | Abortive disconnect requested on endpoint\r\n
0xd1000008 | Shutdown with SD_RECEIVE posted with receive data pending\r\n
0xd1000009 | Transport indicated abortive disconnect\r\n
0xd100000a | Error on accepted connection not associated with listening socket\r\n
0xd100000b | Disconnect failed\r\n
0xd100000c | Pending data on connection when disconnect called\r\n
0xd100000d | Invalid buffer specified on fastio receive\r\n
0xd100000e | Accept operation failed\r\n
0xd100000f | Unable to allocate buffer\r\n
0xd1000010 | Counter overflow\r\n
0xd1000011 | Data arrives after shutting down receive path\r\n
0xd1000012 | Data arrives during endpoint cleanup\r\n
0xd1000013 | Receive request failed\r\n
0xd1000014 | Send request failed\r\n
0xd1000015 | Send request cancelled\r\n
0xd1000016 | TransmitPackets/TransmitFile request cancelled\r\n
0xd1000017 | Abort indicated during connection request\r\n
0xd1000018 | Plug and play event caused abort\r\n
0xd1000019 | Datagram source address does not match connected address\r\n
0xd100001a | Insufficient local buffer space\r\n
0xd100001b | Buffer allocation failed\r\n
0xd100001c | Insufficient local buffer space - circular queueing enabled\r\n
0xd100001d | Indicated datagram too large - integer overflow\r\n
0xd100001e | SO_OOBINLINE\r\n
0xd100001f | FIONBIO\r\n
0xd1000020 | SO_RCVBUF\r\n
0xd1000021 | SO_SNDBUF\r\n
0xd1000022 | SIO_ENABLE_CIRCULAR_QUEUEING\r\n
0xd1000023 | SIO_UDP_CONNRESET\r\n
0xd1000024 | AFD_IPV6_V6ONLY\r\n
0xd1000025 | SIO_UDP_NETRESET\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x11000001 | Datagram socket\r\n
0x11000002 | Stream socket\r\n
0x11000003 | Winsock initiated event\r\n
0x11000004 | Transport initiated event\r\n
0x11000005 | Fastpath I/O\r\n
0x11000006 | Buffered\r\n
0x12000034 | SQM\r\n
0x3100000a | Open\r\n
0x3100000b | Bound\r\n
0x3100000c | Connected\r\n
0x3100000d | Disconnected\r\n
0x3100000e | Aborted\r\n
0x3100000f | Closed\r\n
0x31000010 | Freed\r\n
0x51000002 | Error\r\n
0x51000004 | Information\r\n
0x51000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-Winsock Catalog Change\r\n
0x90000002 | Microsoft-Windows-Winsock Catalog Change/Operational\r\n
0x91000001 | Microsoft-Windows-Winsock Network Event\r\n
0x91000002 | Microsoft-Windows-Winsock Network Event/Operational\r\n
0xb0000001 | LSP %1 was installed in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000002 | LSP %1 was removed from the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000003 | LSP %1 was disabled in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000004 | The %1-bit catalog was reset by the administrator\r\n
0xb1000001 | Socket creation: %1 %2 %3 %4 %5\r\n
0xb1000002 | Socket bind: %1 %2 %3 %4 %5\r\n
0xb1000004 | Socket connect: %1 %2 %3 %4\r\n
0xb1000006 | Connect completed: %1 %2 %3\r\n
0xb1000007 | AFD initiated abort: %1 %2 %3\r\n
0xb1000008 | Transport initiated abort: %1 %2 %3\r\n
0xb1000009 | Failed send request: %1 %2 %3\r\n
0xb100000a | Failed WSASendMsg request: %1 %2 %3\r\n
0xb100000b | Failed recv request: %1 %2 %3\r\n
0xb100000c | Failed recvfrom request: %1 %2 %3\r\n
0xb100000d | Socket close: %1 %2 %3\r\n
0xb100000e | Socket cleanup (all references removed): %1 %2 %3\r\n
0xb100000f | Socket accept: %1 %2 %3 %4 %5\r\n
0xb1000011 | Accept failed: %1 %2 %3\r\n
0xb1000012 | Send posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000013 | Receive posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000014 | RecvFrom posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000015 | SendTo posted: %1 %2 %3 %4 %5 %6 %7 %8\r\n
0xb1000017 | Recv completed: %1 %2 %3 %4\r\n
0xb1000018 | Send completed: %1 %2 %3 %4\r\n
0xb1000019 | SendMsg completed: %1 %2 %3 %4\r\n
0xb100001a | RecvFrom completed: %1 %2 %3 %4 %5 %6 %7\r\n
0xb100001c | SendTo completed: %1 %2 %3 %4\r\n
0xb100001d | Socket option set: %1 %2 %3 %4\r\n
0xb100001e | Select/Poll posted: %1 %2 %3\r\n
0xb100001f | Select/Poll completed: %1 %2 %3\r\n
0xb1000020 | WSAEventSelect: %1 %2 %3\r\n
0xb1000021 | Datagram dropped: %1 %2 %3 %4 %5 %6\r\n
0xb1000023 | Connection indicated: %1 %2 %3 %4\r\n
0xb1000025 | Data indicated from transport: %1 %2 %3\r\n
0xb1000026 | Data indicated from transport: %1 %2 %3 %4 %5\r\n
0xb1000028 | Failed bind: %1 %2 %3\r\n
0xb1000029 | Disconnect indicated from transport: %1 %2\r\n
0xb10003e8 | socket: %1: Process %3 (%8), Endpoint %4, Family %5, Type %6, Protocol %7, Seq %2, Status %9\r\n
0xb10003e9 | closesocket: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003ea | socket cleanup: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003eb | send: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ec | recv: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ed | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ee | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ef | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f1 | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f3 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f4 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f5 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f7 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f9 | connect: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fa | connect: %1: Process %3, Endpoint %4, Address %9, Seq %2, Status %7\r\n
0xb10003fc | ConnectEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fd | ConnectEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Seq %2, Status %7\r\n
0xb10003ff | accept: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000400 | accept: %1: Process %3, Endpoint %4, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000402 | AcceptEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000403 | AcceptEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000405 | bind: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000406 | bind: %1: Process %3, Endpoint %4, Address %7, Seq %2, Status %5\r\n
0xb1000408 | connection aborted: %1: Process %3, Endpoint %4, Seq %2, Reason %5\r\n
0xb1000409 | datagram dropped: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2, Reason %9\r\n
0xb100040b | Socket option: %1: Process %3, Endpoint %4, Option %5, Value %6, Seq %2, Status %7\r\n
0xb100040c | Wait for listen: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb100040d | Listen: %1: Process %3, Endpoint %4, Backlog %5, Seq %2, Status %6\r\n
0xb1000bb8 | Connect indication: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000bb9 | Connect indication: %1: Process %3, Endpoint %4, Address %7, Backlog Count %8, Seq %2, Status %5\r\n
0xb1000bbb | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Seq %2\r\n
0xb1000bbc | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2\r\n
0xb1000bbe | disconnect indicated: %1: Process %3, Endpoint %4, Seq %2\r\n
0xb1000bbf | Transport send backlog: Process %1, Endpoint %2, Send Backlog %5\r\n
0xd1000001 | SOCK_STREAM\r\n
0xd1000002 | SOCK_DGRAM\r\n
0xd1000003 | SOCK_RAW\r\n
0xd1000004 | SOCK_RDM\r\n
0xd1000005 | SOCK_SEQPACKET\r\n
0xd1000006 | Attempt to flush pending receive requests failed\r\n
0xd1000007 | Abortive disconnect requested on endpoint\r\n
0xd1000008 | Shutdown with SD_RECEIVE posted with receive data pending\r\n
0xd1000009 | Transport indicated abortive disconnect\r\n
0xd100000a | Error on accepted connection not associated with listening socket\r\n
0xd100000b | Disconnect failed\r\n
0xd100000c | Pending data on connection when disconnect called\r\n
0xd100000d | Invalid buffer specified on fastio receive\r\n
0xd100000e | Accept operation failed\r\n
0xd100000f | Unable to allocate buffer\r\n
0xd1000010 | Counter overflow\r\n
0xd1000011 | Data arrives after shutting down receive path\r\n
0xd1000012 | Data arrives during endpoint cleanup\r\n
0xd1000013 | Receive request failed\r\n
0xd1000014 | Send request failed\r\n
0xd1000015 | Send request cancelled\r\n
0xd1000016 | TransmitPackets/TransmitFile request cancelled\r\n
0xd1000017 | Abort indicated during connection request\r\n
0xd1000018 | Plug and play event caused abort\r\n
0xd1000019 | Datagram source address does not match connected address\r\n
0xd100001a | Insufficient local buffer space\r\n
0xd100001b | Buffer allocation failed\r\n
0xd100001c | Insufficient local buffer space - circular queueing enabled\r\n
0xd100001d | Indicated datagram too large - integer overflow\r\n
0xd100001e | SO_OOBINLINE\r\n
0xd100001f | FIONBIO\r\n
0xd1000020 | SO_RCVBUF\r\n
0xd1000021 | SO_SNDBUF\r\n
0xd1000022 | SIO_ENABLE_CIRCULAR_QUEUEING\r\n
0xd1000023 | SIO_UDP_CONNRESET\r\n
0xd1000024 | AFD_IPV6_V6ONLY\r\n
0xd1000025 | SIO_UDP_NETRESET\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x11000001 | Datagram socket\r\n
0x11000002 | Stream socket\r\n
0x11000003 | Winsock initiated event\r\n
0x11000004 | Transport initiated event\r\n
0x11000005 | Fastpath I/O\r\n
0x11000006 | Buffered\r\n
0x11000007 | RIO\r\n
0x12000034 | SQM\r\n
0x3100000a | Open\r\n
0x3100000b | Bound\r\n
0x3100000c | Connected\r\n
0x3100000d | Disconnected\r\n
0x3100000e | Aborted\r\n
0x3100000f | Closed\r\n
0x31000010 | Freed\r\n
0x31000011 | Modified\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x51000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-Winsock Catalog Change\r\n
0x90000002 | Microsoft-Windows-Winsock Catalog Change/Operational\r\n
0x91000001 | Microsoft-Windows-Winsock Network Event\r\n
0x91000002 | Microsoft-Windows-Winsock Network Event/Operational\r\n
0xb0000001 | LSP %1 was installed in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000002 | LSP %1 was removed from the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000003 | LSP %1 was disabled in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000004 | The %1-bit catalog was reset by the administrator\r\n
0xb1000001 | Socket creation: %1 %2 %3 %4 %5\r\n
0xb1000002 | Socket bind: %1 %2 %3 %4 %5\r\n
0xb1000004 | Socket connect: %1 %2 %3 %4\r\n
0xb1000006 | Connect completed: %1 %2 %3\r\n
0xb1000007 | AFD initiated abort: %1 %2 %3\r\n
0xb1000008 | Transport initiated abort: %1 %2 %3\r\n
0xb1000009 | Failed send request: %1 %2 %3\r\n
0xb100000a | Failed WSASendMsg request: %1 %2 %3\r\n
0xb100000b | Failed recv request: %1 %2 %3\r\n
0xb100000c | Failed recvfrom request: %1 %2 %3\r\n
0xb100000d | Socket close: %1 %2 %3\r\n
0xb100000e | Socket cleanup (all references removed): %1 %2 %3\r\n
0xb100000f | Socket accept: %1 %2 %3 %4 %5\r\n
0xb1000011 | Accept failed: %1 %2 %3\r\n
0xb1000012 | Send posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000013 | Receive posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000014 | RecvFrom posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000015 | SendTo posted: %1 %2 %3 %4 %5 %6 %7 %8\r\n
0xb1000017 | Recv completed: %1 %2 %3 %4\r\n
0xb1000018 | Send completed: %1 %2 %3 %4\r\n
0xb1000019 | SendMsg completed: %1 %2 %3 %4\r\n
0xb100001a | RecvFrom completed: %1 %2 %3 %4 %5 %6 %7\r\n
0xb100001c | SendTo completed: %1 %2 %3 %4\r\n
0xb100001d | Socket option set: %1 %2 %3 %4\r\n
0xb100001e | Select/Poll posted: %1 %2 %3\r\n
0xb100001f | Select/Poll completed: %1 %2 %3\r\n
0xb1000020 | WSAEventSelect: %1 %2 %3\r\n
0xb1000021 | Datagram dropped: %1 %2 %3 %4 %5 %6\r\n
0xb1000023 | Connection indicated: %1 %2 %3 %4\r\n
0xb1000025 | Data indicated from transport: %1 %2 %3\r\n
0xb1000026 | Data indicated from transport: %1 %2 %3 %4 %5\r\n
0xb1000028 | Failed bind: %1 %2 %3\r\n
0xb1000029 | Disconnect indicated from transport: %1 %2\r\n
0xb10003e8 | socket: %1: Process %3 (%8), Endpoint %4, Family %5, Type %6, Protocol %7, Seq %2, Status %9\r\n
0xb10003e9 | closesocket: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003ea | socket cleanup: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003eb | send: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ec | recv: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ed | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ee | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ef | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f1 | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f3 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f4 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f5 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f7 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f9 | connect: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fa | connect: %1: Process %3, Endpoint %4, Address %9, Seq %2, Status %7\r\n
0xb10003fc | ConnectEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fd | ConnectEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Seq %2, Status %7\r\n
0xb10003ff | accept: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000400 | accept: %1: Process %3, Endpoint %4, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000402 | AcceptEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000403 | AcceptEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000405 | bind: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000406 | bind: %1: Process %3, Endpoint %4, Address %7, Seq %2, Status %5\r\n
0xb1000408 | connection aborted: %1: Process %3, Endpoint %4, Seq %2, Reason %5\r\n
0xb1000409 | datagram dropped: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2, Reason %9\r\n
0xb100040b | Socket option: %1: Process %3, Endpoint %4, Option %5, Value %6, Seq %2, Status %7\r\n
0xb100040c | Wait for listen: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb100040d | Listen: %1: Process %3, Endpoint %4, Backlog %5, Seq %2, Status %6\r\n
0xb1000bb8 | Connect indication: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000bb9 | Connect indication: %1: Process %3, Endpoint %4, Address %7, Backlog Count %8, Seq %2, Status %5\r\n
0xb1000bbb | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Seq %2\r\n
0xb1000bbc | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2\r\n
0xb1000bbe | disconnect indicated: %1: Process %3, Endpoint %4, Seq %2\r\n
0xb1000bbf | Transport send backlog: Process %1, Endpoint %2, Send Backlog %5\r\n
0xb1000fa0 | Registration domain %1 create status %2\r\n
0xb1000fa1 | Registration domain %1 closed\r\n
0xb1000fa2 | CQ %1 created with %3 entries, index %7 and notification type %8, status %13\r\n
0xb1000fa3 | CQ %1 closed with %2 commit\r\n
0xb1000fa4 | CQ %1 cleaned up\r\n
0xb1000fa5 | CQ %1 with %5 commit resized from %2 to %6, status %10\r\n
0xb1000fa6 | RQ %2 created on endpoint %1 with %8 receive and %4 send entries, using receive CQ %13 and send CQ %12, status %14\r\n
0xb1000fa7 | RQ %1 closed, receive = (%2,%3) send = (%4,%5)\r\n
0xb1000fa8 | RQ %1 cleaned up\r\n
0xb1000fa9 | RQ %1 resized from (%9,%2) to (%12,%5), status = %16\r\n
0xb1000faa | Buffer %1 registered with address %3 and length %5, system address = %4, ID = %6, status = %7\r\n
0xb1000fab | Buffer %1 deregistered with %2 references\r\n
0xb1000fac | Buffer %1 cleaned up\r\n
0xb1000fad | RQ %2 using invalid buffer ID %3\r\n
0xb1000fae | RQ %2 invalid use of buffer %3, offset = %4, length = %5\r\n
0xb1000faf | RQ %1 using invalid buffer size for %2, specified = %3, required = %4\r\n
0xd1000001 | SOCK_STREAM\r\n
0xd1000002 | SOCK_DGRAM\r\n
0xd1000003 | SOCK_RAW\r\n
0xd1000004 | SOCK_RDM\r\n
0xd1000005 | SOCK_SEQPACKET\r\n
0xd1000006 | Attempt to flush pending receive requests failed\r\n
0xd1000007 | Abortive disconnect requested on endpoint\r\n
0xd1000008 | Shutdown with SD_RECEIVE posted with receive data pending\r\n
0xd1000009 | Transport indicated abortive disconnect\r\n
0xd100000a | Error on accepted connection not associated with listening socket\r\n
0xd100000b | Disconnect failed\r\n
0xd100000c | Pending data on connection when disconnect called\r\n
0xd100000d | Invalid buffer specified on fastio receive\r\n
0xd100000e | Accept operation failed\r\n
0xd100000f | Unable to allocate buffer\r\n
0xd1000010 | Counter overflow\r\n
0xd1000011 | Data arrives after shutting down receive path\r\n
0xd1000012 | Data arrives during endpoint cleanup\r\n
0xd1000013 | Receive request failed\r\n
0xd1000014 | Send request failed\r\n
0xd1000015 | Send request cancelled\r\n
0xd1000016 | TransmitPackets/TransmitFile request cancelled\r\n
0xd1000017 | Abort indicated during connection request\r\n
0xd1000018 | Plug and play event caused abort\r\n
0xd1000019 | Datagram source address does not match connected address\r\n
0xd100001a | Insufficient local buffer space\r\n
0xd100001b | Buffer allocation failed\r\n
0xd100001c | Insufficient local buffer space - circular queueing enabled\r\n
0xd100001d | Indicated datagram too large - integer overflow\r\n
0xd100001e | SO_OOBINLINE\r\n
0xd100001f | FIONBIO\r\n
0xd1000020 | SO_RCVBUF\r\n
0xd1000021 | SO_SNDBUF\r\n
0xd1000022 | SIO_ENABLE_CIRCULAR_QUEUEING\r\n
0xd1000023 | SIO_UDP_CONNRESET\r\n
0xd1000024 | AFD_IPV6_V6ONLY\r\n
0xd1000025 | SIO_UDP_NETRESET\r\n
0xd1000026 | None\r\n
0xd1000027 | Event\r\n
0xd1000028 | IOCP\r\n
0xd1000029 | source address\r\n
0xd100002a | destination address\r\n
0xd100002b | flags\r\n
0xd100002c | control\r\n
0xd100002d | send\r\n
0xd100002e | receive\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x11000001 | Datagram socket\r\n
0x11000002 | Stream socket\r\n
0x11000003 | Winsock initiated event\r\n
0x11000004 | Transport initiated event\r\n
0x11000005 | Fastpath I/O\r\n
0x11000006 | Buffered\r\n
0x11000007 | RIO\r\n
0x12000034 | SQM\r\n
0x3100000a | Open\r\n
0x3100000b | Bound\r\n
0x3100000c | Connected\r\n
0x3100000d | Disconnected\r\n
0x3100000e | Aborted\r\n
0x3100000f | Closed\r\n
0x31000010 | Freed\r\n
0x31000011 | Modified\r\n
0x33000000 | Info\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x51000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-Winsock Catalog Change\r\n
0x90000002 | Microsoft-Windows-Winsock Catalog Change/Operational\r\n
0x91000001 | Microsoft-Windows-Winsock Network Event\r\n
0x91000002 | Microsoft-Windows-Winsock Network Event/Operational\r\n
0x93000001 | Microsoft-Windows-Winsock NameResolution Event\r\n
0x93000002 | Microsoft-Windows-Winsock NameResolution Event/Operational\r\n
0xb0000001 | LSP %1 was installed in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000002 | LSP %1 was removed from the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000003 | LSP %1 was disabled in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000004 | The %1-bit catalog was reset by the administrator\r\n
0xb1000001 | Socket creation: %1 %2 %3 %4 %5\r\n
0xb1000002 | Socket bind: %1 %2 %3 %4 %5\r\n
0xb1000004 | Socket connect: %1 %2 %3 %4\r\n
0xb1000006 | Connect completed: %1 %2 %3\r\n
0xb1000007 | AFD initiated abort: %1 %2 %3\r\n
0xb1000008 | Transport initiated abort: %1 %2 %3\r\n
0xb1000009 | Failed send request: %1 %2 %3\r\n
0xb100000a | Failed WSASendMsg request: %1 %2 %3\r\n
0xb100000b | Failed recv request: %1 %2 %3\r\n
0xb100000c | Failed recvfrom request: %1 %2 %3\r\n
0xb100000d | Socket close: %1 %2 %3\r\n
0xb100000e | Socket cleanup (all references removed): %1 %2 %3\r\n
0xb100000f | Socket accept: %1 %2 %3 %4 %5\r\n
0xb1000011 | Accept failed: %1 %2 %3\r\n
0xb1000012 | Send posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000013 | Receive posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000014 | RecvFrom posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000015 | SendTo posted: %1 %2 %3 %4 %5 %6 %7 %8\r\n
0xb1000017 | Recv completed: %1 %2 %3 %4\r\n
0xb1000018 | Send completed: %1 %2 %3 %4\r\n
0xb1000019 | SendMsg completed: %1 %2 %3 %4\r\n
0xb100001a | RecvFrom completed: %1 %2 %3 %4 %5 %6 %7\r\n
0xb100001c | SendTo completed: %1 %2 %3 %4\r\n
0xb100001d | Socket option set: %1 %2 %3 %4\r\n
0xb100001e | Select/Poll posted: %1 %2 %3\r\n
0xb100001f | Select/Poll completed: %1 %2 %3\r\n
0xb1000020 | WSAEventSelect: %1 %2 %3\r\n
0xb1000021 | Datagram dropped: %1 %2 %3 %4 %5 %6\r\n
0xb1000023 | Connection indicated: %1 %2 %3 %4\r\n
0xb1000025 | Data indicated from transport: %1 %2 %3\r\n
0xb1000026 | Data indicated from transport: %1 %2 %3 %4 %5\r\n
0xb1000028 | Failed bind: %1 %2 %3\r\n
0xb1000029 | Disconnect indicated from transport: %1 %2\r\n
0xb10003e8 | socket: %1: Process %3 (%8), Endpoint %4, Family %5, Type %6, Protocol %7, Seq %2, Status %9\r\n
0xb10003e9 | closesocket: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003ea | socket cleanup: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003eb | send: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ec | recv: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ed | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ee | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ef | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f1 | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f3 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f4 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f5 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f7 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f9 | connect: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fa | connect: %1: Process %3, Endpoint %4, Address %9, Seq %2, Status %7\r\n
0xb10003fc | ConnectEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fd | ConnectEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Seq %2, Status %7\r\n
0xb10003ff | accept: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000400 | accept: %1: Process %3, Endpoint %4, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000402 | AcceptEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000403 | AcceptEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000405 | bind: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000406 | bind: %1: Process %3, Endpoint %4, Address %7, Seq %2, Status %5\r\n
0xb1000408 | connection aborted: %1: Process %3, Endpoint %4, Seq %2, Reason %5\r\n
0xb1000409 | datagram dropped: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2, Reason %9\r\n
0xb100040b | Socket option: %1: Process %3, Endpoint %4, Option %5, Value %6, Seq %2, Status %7\r\n
0xb100040c | Wait for listen: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb100040d | Listen: %1: Process %3, Endpoint %4, Backlog %5, Seq %2, Status %6\r\n
0xb1000bb8 | Connect indication: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000bb9 | Connect indication: %1: Process %3, Endpoint %4, Address %7, Backlog Count %8, Seq %2, Status %5\r\n
0xb1000bbb | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Seq %2\r\n
0xb1000bbc | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2\r\n
0xb1000bbe | disconnect indicated: %1: Process %3, Endpoint %4, Seq %2\r\n
0xb1000bbf | Transport send backlog: Process %1, Endpoint %2, Send Backlog %5\r\n
0xb1000fa0 | Registration domain %1 create status %2\r\n
0xb1000fa1 | Registration domain %1 closed\r\n
0xb1000fa2 | CQ %1 created with %3 entries, index %7 and notification type %8, status %13\r\n
0xb1000fa3 | CQ %1 closed with %2 commit\r\n
0xb1000fa4 | CQ %1 cleaned up\r\n
0xb1000fa5 | CQ %1 with %5 commit resized from %2 to %6, status %10\r\n
0xb1000fa6 | RQ %2 created on endpoint %1 with %8 receive and %4 send entries, using receive CQ %13 and send CQ %12, status %14\r\n
0xb1000fa7 | RQ %1 closed, receive = (%2,%3) send = (%4,%5)\r\n
0xb1000fa8 | RQ %1 cleaned up\r\n
0xb1000fa9 | RQ %1 resized from (%9,%2) to (%12,%5), status = %16\r\n
0xb1000faa | Buffer %1 registered with address %3 and length %5, system address = %4, ID = %6, status = %7\r\n
0xb1000fab | Buffer %1 deregistered with %2 references\r\n
0xb1000fac | Buffer %1 cleaned up\r\n
0xb1000fad | RQ %2 using invalid buffer ID %3\r\n
0xb1000fae | RQ %2 invalid use of buffer %3, offset = %4, length = %5\r\n
0xb1000faf | RQ %1 using invalid buffer size for %2, specified = %3, required = %4\r\n
0xb30003e8 | GetAddrInfoW is called for queryName %1, serviceName %2, flags %4, family %5, socketType %6, protocol %7 and seq %3\r\n
0xb30003e9 | GetAddrInfoW is completed for queryName %1 with status %2 and result %3\r\n
0xb30003ea | GetAddrInfoExW is called for queryName %1, serviceName %2, nameSpace %4, nameSpace GUID %5, flags %6, family %7, socketType %8, protocol %9, interface index %10, timeOut %11, asyncWithCallBack %12, asyncWithOverlapped %13 and seq %3\r\n
0xb30003eb | GetAddrInfoExW asynchronous query is pending for queryName: %1 with cancel Handle %2\r\n
0xb30003ec | GetAddrInfoExW is completed for queryName %1 with status %2 and result %3\r\n
0xb30003ed | GetAddrInfoExCancel is called for  query %1 and seq %2\r\n
0xb30003ee | NSPLookupServiceBegin is called for provider %1, queryName %2, serviceGUID %3, interface index %4 and control flags %5\r\n
0xb30003ef | NSPLookupServiceBegin is completed for provider %1, queryName %2 serviceGUID %3, interface index %4, control flags %5 and lookup handle %6 with status %7\r\n
0xb30003f0 | NSPLookupServiceNext is called for provider %1, control Flags %2 and lookup handle %3\r\n
0xb30003f1 | NSPLookupServiceNext is completed for provider %1, control Flags %2 and lookup Handle %3 with status %4 and result %5\r\n
0xb30003f2 | NSPLookupServiceEnd is called for provider %1 and lookup handle %2\r\n
0xb30003f3 | NSPLookupServiceEnd completed for provider %1 and lookup handle %2 with status %3\r\n
0xd1000001 | SOCK_STREAM\r\n
0xd1000002 | SOCK_DGRAM\r\n
0xd1000003 | SOCK_RAW\r\n
0xd1000004 | SOCK_RDM\r\n
0xd1000005 | SOCK_SEQPACKET\r\n
0xd1000006 | Attempt to flush pending receive requests failed\r\n
0xd1000007 | Abortive disconnect requested on endpoint\r\n
0xd1000008 | Shutdown with SD_RECEIVE posted with receive data pending\r\n
0xd1000009 | Transport indicated abortive disconnect\r\n
0xd100000a | Error on accepted connection not associated with listening socket\r\n
0xd100000b | Disconnect failed\r\n
0xd100000c | Pending data on connection when disconnect called\r\n
0xd100000d | Invalid buffer specified on fastio receive\r\n
0xd100000e | Accept operation failed\r\n
0xd100000f | Unable to allocate buffer\r\n
0xd1000010 | Counter overflow\r\n
0xd1000011 | Data arrives after shutting down receive path\r\n
0xd1000012 | Data arrives during endpoint cleanup\r\n
0xd1000013 | Receive request failed\r\n
0xd1000014 | Send request failed\r\n
0xd1000015 | Send request cancelled\r\n
0xd1000016 | TransmitPackets/TransmitFile request cancelled\r\n
0xd1000017 | Abort indicated during connection request\r\n
0xd1000018 | Plug and play event caused abort\r\n
0xd1000019 | Datagram source address does not match connected address\r\n
0xd100001a | Insufficient local buffer space\r\n
0xd100001b | Buffer allocation failed\r\n
0xd100001c | Insufficient local buffer space - circular queueing enabled\r\n
0xd100001d | Indicated datagram too large - integer overflow\r\n
0xd100001e | SO_OOBINLINE\r\n
0xd100001f | FIONBIO\r\n
0xd1000020 | SO_RCVBUF\r\n
0xd1000021 | SO_SNDBUF\r\n
0xd1000022 | SIO_ENABLE_CIRCULAR_QUEUEING\r\n
0xd1000023 | SIO_UDP_CONNRESET\r\n
0xd1000024 | AFD_IPV6_V6ONLY\r\n
0xd1000025 | SIO_UDP_NETRESET\r\n
0xd1000026 | None\r\n
0xd1000027 | Event\r\n
0xd1000028 | IOCP\r\n
0xd1000029 | source address\r\n
0xd100002a | destination address\r\n
0xd100002b | flags\r\n
0xd100002c | control\r\n
0xd100002d | send\r\n
0xd100002e | receive\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x11000001 | Datagram socket\r\n
0x11000002 | Stream socket\r\n
0x11000003 | Winsock initiated event\r\n
0x11000004 | Transport initiated event\r\n
0x11000005 | Fastpath I/O\r\n
0x11000006 | Buffered\r\n
0x11000007 | RIO\r\n
0x12000034 | SQM\r\n
0x3100000a | Open\r\n
0x3100000b | Bound\r\n
0x3100000c | Connected\r\n
0x3100000d | Disconnected\r\n
0x3100000e | Aborted\r\n
0x3100000f | Closed\r\n
0x31000010 | Freed\r\n
0x31000011 | Modified\r\n
0x33000000 | Info\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x51000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-Winsock Catalog Change\r\n
0x90000002 | Microsoft-Windows-Winsock Catalog Change/Operational\r\n
0x91000001 | Microsoft-Windows-Winsock Network Event\r\n
0x91000002 | Microsoft-Windows-Winsock Network Event/Operational\r\n
0x93000001 | Microsoft-Windows-Winsock NameResolution Event\r\n
0x93000002 | Microsoft-Windows-Winsock NameResolution Event/Operational\r\n
0xb0000001 | LSP %1 was installed in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000002 | LSP %1 was removed from the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000003 | LSP %1 was disabled in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000004 | The %1-bit catalog was reset by the administrator\r\n
0xb1000001 | Socket creation: %1 %2 %3 %4 %5\r\n
0xb1000002 | Socket bind: %1 %2 %3 %4 %5\r\n
0xb1000004 | Socket connect: %1 %2 %3 %4\r\n
0xb1000006 | Connect completed: %1 %2 %3\r\n
0xb1000007 | AFD initiated abort: %1 %2 %3\r\n
0xb1000008 | Transport initiated abort: %1 %2 %3\r\n
0xb1000009 | Failed send request: %1 %2 %3\r\n
0xb100000a | Failed WSASendMsg request: %1 %2 %3\r\n
0xb100000b | Failed recv request: %1 %2 %3\r\n
0xb100000c | Failed recvfrom request: %1 %2 %3\r\n
0xb100000d | Socket close: %1 %2 %3\r\n
0xb100000e | Socket cleanup (all references removed): %1 %2 %3\r\n
0xb100000f | Socket accept: %1 %2 %3 %4 %5\r\n
0xb1000011 | Accept failed: %1 %2 %3\r\n
0xb1000012 | Send posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000013 | Receive posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000014 | RecvFrom posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000015 | SendTo posted: %1 %2 %3 %4 %5 %6 %7 %8\r\n
0xb1000017 | Recv completed: %1 %2 %3 %4\r\n
0xb1000018 | Send completed: %1 %2 %3 %4\r\n
0xb1000019 | SendMsg completed: %1 %2 %3 %4\r\n
0xb100001a | RecvFrom completed: %1 %2 %3 %4 %5 %6 %7\r\n
0xb100001c | SendTo completed: %1 %2 %3 %4\r\n
0xb100001d | Socket option set: %1 %2 %3 %4\r\n
0xb100001e | Select/Poll posted: %1 %2 %3\r\n
0xb100001f | Select/Poll completed: %1 %2 %3\r\n
0xb1000020 | WSAEventSelect: %1 %2 %3\r\n
0xb1000021 | Datagram dropped: %1 %2 %3 %4 %5 %6\r\n
0xb1000023 | Connection indicated: %1 %2 %3 %4\r\n
0xb1000025 | Data indicated from transport: %1 %2 %3\r\n
0xb1000026 | Data indicated from transport: %1 %2 %3 %4 %5\r\n
0xb1000028 | Failed bind: %1 %2 %3\r\n
0xb1000029 | Disconnect indicated from transport: %1 %2\r\n
0xb10003e8 | socket: %1: Process %3 (%8), Endpoint %4, Family %5, Type %6, Protocol %7, Seq %2, Status %9\r\n
0xb10003e9 | closesocket: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003ea | socket cleanup: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003eb | send: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ec | recv: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ed | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ee | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ef | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f1 | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f3 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f4 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f5 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f7 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f9 | connect: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fa | connect: %1: Process %3, Endpoint %4, Address %9, Seq %2, Status %7\r\n
0xb10003fc | ConnectEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fd | ConnectEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Seq %2, Status %7\r\n
0xb10003ff | accept: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000400 | accept: %1: Process %3, Endpoint %4, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000402 | AcceptEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000403 | AcceptEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000405 | bind: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000406 | bind: %1: Process %3, Endpoint %4, Address %7, Seq %2, Status %5\r\n
0xb1000408 | connection aborted: %1: Process %3, Endpoint %4, Seq %2, Reason %5\r\n
0xb1000409 | datagram dropped: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2, Reason %9\r\n
0xb100040b | Socket option: %1: Process %3, Endpoint %4, Option %5, Value %6, Seq %2, Status %7\r\n
0xb100040c | Wait for listen: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb100040d | Listen: %1: Process %3, Endpoint %4, Backlog %5, Seq %2, Status %6\r\n
0xb1000bb8 | Connect indication: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000bb9 | Connect indication: %1: Process %3, Endpoint %4, Address %7, Backlog Count %8, Seq %2, Status %5\r\n
0xb1000bbb | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Seq %2\r\n
0xb1000bbc | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2\r\n
0xb1000bbe | disconnect indicated: %1: Process %3, Endpoint %4, Seq %2\r\n
0xb1000bbf | Transport send backlog: Process %1, Endpoint %2, Send Backlog %5\r\n
0xb1000fa0 | Registration domain %1 create status %2\r\n
0xb1000fa1 | Registration domain %1 closed\r\n
0xb1000fa2 | CQ %1 created with %3 entries, index %7 and notification type %8, status %13\r\n
0xb1000fa3 | CQ %1 closed with %2 commit\r\n
0xb1000fa4 | CQ %1 cleaned up\r\n
0xb1000fa5 | CQ %1 with %5 commit resized from %2 to %6, status %10\r\n
0xb1000fa6 | RQ %2 created on endpoint %1 with %8 receive and %4 send entries, using receive CQ %13 and send CQ %12, status %14\r\n
0xb1000fa7 | RQ %1 closed, receive = (%2,%3) send = (%4,%5)\r\n
0xb1000fa8 | RQ %1 cleaned up\r\n
0xb1000fa9 | RQ %1 resized from (%9,%2) to (%12,%5), status = %16\r\n
0xb1000faa | Buffer %1 registered with address %3 and length %5, system address = %4, ID = %6, status = %7\r\n
0xb1000fab | Buffer %1 deregistered with %2 references\r\n
0xb1000fac | Buffer %1 cleaned up\r\n
0xb1000fad | RQ %2 using invalid buffer ID %3\r\n
0xb1000fae | RQ %2 invalid use of buffer %3, offset = %4, length = %5\r\n
0xb1000faf | RQ %1 using invalid buffer size for %2, specified = %3, required = %4\r\n
0xb30003e8 | GetAddrInfoW is called for queryName %1, serviceName %2, flags %4, family %5, socketType %6, protocol %7 and seq %3\r\n
0xb30003e9 | GetAddrInfoW is completed for queryName %1 with status %2 and result %3\r\n
0xb30003ea | GetAddrInfoExW is called for queryName %1, serviceName %2, nameSpace %4, nameSpace GUID %5, flags %6, family %7, socketType %8, protocol %9, interface index %10, timeOut %11, asyncWithCallBack %12, asyncWithOverlapped %13 and seq %3\r\n
0xb30003eb | GetAddrInfoExW asynchronous query is pending for queryName: %1 with cancel Handle %2\r\n
0xb30003ec | GetAddrInfoExW is completed for queryName %1 with status %2 and result %3\r\n
0xb30003ed | GetAddrInfoExCancel is called for  query %1 and seq %2\r\n
0xb30003ee | NSPLookupServiceBegin is called for provider %1, queryName %2, serviceGUID %3, interface index %4 and control flags %5\r\n
0xb30003ef | NSPLookupServiceBegin is completed for provider %1, queryName %2 serviceGUID %3, interface index %4, control flags %5 and lookup handle %6 with status %7\r\n
0xb30003f0 | NSPLookupServiceNext is called for provider %1, control Flags %2 and lookup handle %3\r\n
0xb30003f1 | NSPLookupServiceNext is completed for provider %1, control Flags %2 and lookup Handle %3 with status %4 and result %5\r\n
0xb30003f2 | NSPLookupServiceEnd is called for provider %1 and lookup handle %2\r\n
0xb30003f3 | NSPLookupServiceEnd completed for provider %1 and lookup handle %2 with status %3\r\n
0xb30003f4 | GetAddrInfoExW info.  queryName %1, serviceName %2, nameSpace %4, nameSpace GUID %5, flags %6, family %7, socketType %8, protocol %9, interface index %10, timeOut %11, asyncWithCallBack %12, asyncWithOverlapped %13, error %14 and seq %3\r\n
0xb30003f5 | Wsa Startup. seq: %1.\r\n
0xb30003f6 | Wsa Cleanup. seq: %1.  Refcount: %2.\r\n
0xb30003f7 | NSJOB info.  seq %1.  Refcount: %2.\r\n
0xd1000001 | SOCK_STREAM\r\n
0xd1000002 | SOCK_DGRAM\r\n
0xd1000003 | SOCK_RAW\r\n
0xd1000004 | SOCK_RDM\r\n
0xd1000005 | SOCK_SEQPACKET\r\n
0xd1000006 | Attempt to flush pending receive requests failed\r\n
0xd1000007 | Abortive disconnect requested on endpoint\r\n
0xd1000008 | Shutdown with SD_RECEIVE posted with receive data pending\r\n
0xd1000009 | Transport indicated abortive disconnect\r\n
0xd100000a | Error on accepted connection not associated with listening socket\r\n
0xd100000b | Disconnect failed\r\n
0xd100000c | Pending data on connection when disconnect called\r\n
0xd100000d | Invalid buffer specified on fastio receive\r\n
0xd100000e | Accept operation failed\r\n
0xd100000f | Unable to allocate buffer\r\n
0xd1000010 | Counter overflow\r\n
0xd1000011 | Data arrives after shutting down receive path\r\n
0xd1000012 | Data arrives during endpoint cleanup\r\n
0xd1000013 | Receive request failed\r\n
0xd1000014 | Send request failed\r\n
0xd1000015 | Send request cancelled\r\n
0xd1000016 | TransmitPackets/TransmitFile request cancelled\r\n
0xd1000017 | Abort indicated during connection request\r\n
0xd1000018 | Plug and play event caused abort\r\n
0xd1000019 | Datagram source address does not match connected address\r\n
0xd100001a | Insufficient local buffer space\r\n
0xd100001b | Buffer allocation failed\r\n
0xd100001c | Insufficient local buffer space - circular queueing enabled\r\n
0xd100001d | Indicated datagram too large - integer overflow\r\n
0xd100001e | SO_OOBINLINE\r\n
0xd100001f | FIONBIO\r\n
0xd1000020 | SO_RCVBUF\r\n
0xd1000021 | SO_SNDBUF\r\n
0xd1000022 | SIO_ENABLE_CIRCULAR_QUEUEING\r\n
0xd1000023 | SIO_UDP_CONNRESET\r\n
0xd1000024 | AFD_IPV6_V6ONLY\r\n
0xd1000025 | SIO_UDP_NETRESET\r\n
0xd1000026 | None\r\n
0xd1000027 | Event\r\n
0xd1000028 | IOCP\r\n
0xd1000029 | source address\r\n
0xd100002a | destination address\r\n
0xd100002b | flags\r\n
0xd100002c | control\r\n
0xd100002d | send\r\n
0xd100002e | receive\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x11000001 | Datagram socket\r\n
0x11000002 | Stream socket\r\n
0x11000003 | Winsock initiated event\r\n
0x11000004 | Transport initiated event\r\n
0x11000005 | Fastpath I/O\r\n
0x11000006 | Buffered\r\n
0x11000007 | RIO\r\n
0x11000008 | NRT\r\n
0x12000034 | SQM\r\n
0x3100000a | Open\r\n
0x3100000b | Bound\r\n
0x3100000c | Connected\r\n
0x3100000d | Disconnected\r\n
0x3100000e | Aborted\r\n
0x3100000f | Closed\r\n
0x31000010 | Freed\r\n
0x31000011 | Modified\r\n
0x33000000 | Info\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x51000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-Winsock Catalog Change\r\n
0x90000002 | Microsoft-Windows-Winsock Catalog Change/Operational\r\n
0x91000001 | Microsoft-Windows-Winsock Network Event\r\n
0x91000002 | Microsoft-Windows-Winsock Network Event/Operational\r\n
0x93000001 | Microsoft-Windows-Winsock NameResolution Event\r\n
0x93000002 | Microsoft-Windows-Winsock NameResolution Event/Operational\r\n
0xb0000001 | LSP %1 was installed in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000002 | LSP %1 was removed from the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000003 | LSP %1 was disabled in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000004 | The %1-bit catalog was reset by the administrator\r\n
0xb1000001 | Socket creation: %1 %2 %3 %4 %5\r\n
0xb1000002 | Socket bind: %1 %2 %3 %4 %5\r\n
0xb1000004 | Socket connect: %1 %2 %3 %4\r\n
0xb1000006 | Connect completed: %1 %2 %3\r\n
0xb1000007 | AFD initiated abort: %1 %2 %3\r\n
0xb1000008 | Transport initiated abort: %1 %2 %3\r\n
0xb1000009 | Failed send request: %1 %2 %3\r\n
0xb100000a | Failed WSASendMsg request: %1 %2 %3\r\n
0xb100000b | Failed recv request: %1 %2 %3\r\n
0xb100000c | Failed recvfrom request: %1 %2 %3\r\n
0xb100000d | Socket close: %1 %2 %3\r\n
0xb100000e | Socket cleanup (all references removed): %1 %2 %3\r\n
0xb100000f | Socket accept: %1 %2 %3 %4 %5\r\n
0xb1000011 | Accept failed: %1 %2 %3\r\n
0xb1000012 | Send posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000013 | Receive posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000014 | RecvFrom posted: %1 %2 %3 %4 %5 %6\r\n
0xb1000015 | SendTo posted: %1 %2 %3 %4 %5 %6 %7 %8\r\n
0xb1000017 | Recv completed: %1 %2 %3 %4\r\n
0xb1000018 | Send completed: %1 %2 %3 %4\r\n
0xb1000019 | SendMsg completed: %1 %2 %3 %4\r\n
0xb100001a | RecvFrom completed: %1 %2 %3 %4 %5 %6 %7\r\n
0xb100001c | SendTo completed: %1 %2 %3 %4\r\n
0xb100001d | Socket option set: %1 %2 %3 %4\r\n
0xb100001e | Select/Poll posted: %1 %2 %3\r\n
0xb100001f | Select/Poll completed: %1 %2 %3\r\n
0xb1000020 | WSAEventSelect: %1 %2 %3\r\n
0xb1000021 | Datagram dropped: %1 %2 %3 %4 %5 %6\r\n
0xb1000023 | Connection indicated: %1 %2 %3 %4\r\n
0xb1000025 | Data indicated from transport: %1 %2 %3\r\n
0xb1000026 | Data indicated from transport: %1 %2 %3 %4 %5\r\n
0xb1000028 | Failed bind: %1 %2 %3\r\n
0xb1000029 | Disconnect indicated from transport: %1 %2\r\n
0xb10003e8 | socket: %1: Process %3 (%8), Endpoint %4, Family %5, Type %6, Protocol %7, Seq %2, Status %9\r\n
0xb10003e9 | closesocket: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003ea | socket cleanup: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003eb | send: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ec | recv: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ed | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ee | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003ef | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f1 | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f3 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f4 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb10003f5 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f7 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb10003f9 | connect: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fa | connect: %1: Process %3, Endpoint %4, Address %9, Seq %2, Status %7\r\n
0xb10003fc | ConnectEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb10003fd | ConnectEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Seq %2, Status %7\r\n
0xb10003ff | accept: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000400 | accept: %1: Process %3, Endpoint %4, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000402 | AcceptEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000403 | AcceptEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb1000405 | bind: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000406 | bind: %1: Process %3, Endpoint %4, Address %7, Seq %2, Status %5\r\n
0xb1000408 | connection aborted: %1: Process %3, Endpoint %4, Seq %2, Reason %5\r\n
0xb1000409 | datagram dropped: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2, Reason %9\r\n
0xb100040b | Socket option: %1: Process %3, Endpoint %4, Option %5, Value %6, Seq %2, Status %7\r\n
0xb100040c | Wait for listen: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb100040d | Listen: %1: Process %3, Endpoint %4, Backlog %5, Seq %2, Status %6\r\n
0xb1000bb8 | Connect indication: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb1000bb9 | Connect indication: %1: Process %3, Endpoint %4, Address %7, Backlog Count %8, Seq %2, Status %5\r\n
0xb1000bbb | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Seq %2\r\n
0xb1000bbc | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2\r\n
0xb1000bbe | disconnect indicated: %1: Process %3, Endpoint %4, Seq %2\r\n
0xb1000bbf | Transport send backlog: Process %1, Endpoint %2, Send Backlog %5\r\n
0xb1000fa0 | Registration domain %1 create status %2\r\n
0xb1000fa1 | Registration domain %1 closed\r\n
0xb1000fa2 | CQ %1 created with %3 entries, index %7 and notification type %8, status %13\r\n
0xb1000fa3 | CQ %1 closed with %2 commit\r\n
0xb1000fa4 | CQ %1 cleaned up\r\n
0xb1000fa5 | CQ %1 with %5 commit resized from %2 to %6, status %10\r\n
0xb1000fa6 | RQ %2 created on endpoint %1 with %8 receive and %4 send entries, using receive CQ %13 and send CQ %12, status %14\r\n
0xb1000fa7 | RQ %1 closed, receive = (%2,%3) send = (%4,%5)\r\n
0xb1000fa8 | RQ %1 cleaned up\r\n
0xb1000fa9 | RQ %1 resized from (%9,%2) to (%12,%5), status = %16\r\n
0xb1000faa | Buffer %1 registered with address %3 and length %5, system address = %4, ID = %6, status = %7\r\n
0xb1000fab | Buffer %1 deregistered with %2 references\r\n
0xb1000fac | Buffer %1 cleaned up\r\n
0xb1000fad | RQ %2 using invalid buffer ID %3\r\n
0xb1000fae | RQ %2 invalid use of buffer %3, offset = %4, length = %5\r\n
0xb1000faf | RQ %1 using invalid buffer size for %2, specified = %3, required = %4\r\n
0xb1000fb0 | NRT Create: Handle = %1 Process = %2 Status = %3\r\n
0xb1000fb1 | NRT Close: Handle = %1 Process = %2\r\n
0xb30003e8 | GetAddrInfoW is called for queryName %1, serviceName %2, flags %4, family %5, socketType %6, protocol %7 and seq %3\r\n
0xb30003e9 | GetAddrInfoW is completed for queryName %1 with status %2 and result %3\r\n
0xb30003ea | GetAddrInfoExW is called for queryName %1, serviceName %2, nameSpace %4, nameSpace GUID %5, flags %6, family %7, socketType %8, protocol %9, interface index %10, timeOut %11, asyncWithCallBack %12, asyncWithOverlapped %13 and seq %3\r\n
0xb30003eb | GetAddrInfoExW asynchronous query is pending for queryName: %1 with cancel Handle %2\r\n
0xb30003ec | GetAddrInfoExW is completed for queryName %1 with status %2 and result %3\r\n
0xb30003ed | GetAddrInfoExCancel is called for  query %1 and seq %2\r\n
0xb30003ee | NSPLookupServiceBegin is called for provider %1, queryName %2, serviceGUID %3, interface index %4 and control flags %5\r\n
0xb30003ef | NSPLookupServiceBegin is completed for provider %1, queryName %2 serviceGUID %3, interface index %4, control flags %5 and lookup handle %6 with status %7\r\n
0xb30003f0 | NSPLookupServiceNext is called for provider %1, control Flags %2 and lookup handle %3\r\n
0xb30003f1 | NSPLookupServiceNext is completed for provider %1, control Flags %2 and lookup Handle %3 with status %4 and result %5\r\n
0xb30003f2 | NSPLookupServiceEnd is called for provider %1 and lookup handle %2\r\n
0xb30003f3 | NSPLookupServiceEnd completed for provider %1 and lookup handle %2 with status %3\r\n
0xb30003f4 | GetAddrInfoExW info.  queryName %1, serviceName %2, nameSpace %4, nameSpace GUID %5, flags %6, family %7, socketType %8, protocol %9, interface index %10, timeOut %11, asyncWithCallBack %12, asyncWithOverlapped %13, error %14 and seq %3\r\n
0xb30003f5 | Wsa Startup. seq: %1.\r\n
0xb30003f6 | Wsa Cleanup. seq: %1.  Refcount: %2.\r\n
0xb30003f7 | NSJOB info.  seq %1.  Refcount: %2.\r\n
0xd1000001 | SOCK_STREAM\r\n
0xd1000002 | SOCK_DGRAM\r\n
0xd1000003 | SOCK_RAW\r\n
0xd1000004 | SOCK_RDM\r\n
0xd1000005 | SOCK_SEQPACKET\r\n
0xd1000006 | Attempt to flush pending receive requests failed\r\n
0xd1000007 | Abortive disconnect requested on endpoint\r\n
0xd1000008 | Shutdown with SD_RECEIVE posted with receive data pending\r\n
0xd1000009 | Transport indicated abortive disconnect\r\n
0xd100000a | Error on accepted connection not associated with listening socket\r\n
0xd100000b | Disconnect failed\r\n
0xd100000c | Pending data on connection when disconnect called\r\n
0xd100000d | Invalid buffer specified on fastio receive\r\n
0xd100000e | Accept operation failed\r\n
0xd100000f | Unable to allocate buffer\r\n
0xd1000010 | Counter overflow\r\n
0xd1000011 | Data arrives after shutting down receive path\r\n
0xd1000012 | Data arrives during endpoint cleanup\r\n
0xd1000013 | Receive request failed\r\n
0xd1000014 | Send request failed\r\n
0xd1000015 | Send request cancelled\r\n
0xd1000016 | TransmitPackets/TransmitFile request cancelled\r\n
0xd1000017 | Abort indicated during connection request\r\n
0xd1000018 | Plug and play event caused abort\r\n
0xd1000019 | Datagram source address does not match connected address\r\n
0xd100001a | Insufficient local buffer space\r\n
0xd100001b | Buffer allocation failed\r\n
0xd100001c | Insufficient local buffer space - circular queueing enabled\r\n
0xd100001d | Indicated datagram too large - integer overflow\r\n
0xd100001e | SO_OOBINLINE\r\n
0xd100001f | FIONBIO\r\n
0xd1000020 | SO_RCVBUF\r\n
0xd1000021 | SO_SNDBUF\r\n
0xd1000022 | SIO_ENABLE_CIRCULAR_QUEUEING\r\n
0xd1000023 | SIO_UDP_CONNRESET\r\n
0xd1000024 | AFD_IPV6_V6ONLY\r\n
0xd1000025 | SIO_UDP_NETRESET\r\n
0xd1000026 | None\r\n
0xd1000027 | Event\r\n
0xd1000028 | IOCP\r\n
0xd1000029 | source address\r\n
0xd100002a | destination address\r\n
0xd100002b | flags\r\n
0xd100002c | control\r\n
0xd100002d | send\r\n
0xd100002e | receive\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x12000001 | Datagram socket\r\n
0x12000002 | Stream socket\r\n
0x12000003 | Winsock initiated event\r\n
0x12000004 | Transport initiated event\r\n
0x12000005 | Fastpath I/O\r\n
0x12000006 | Buffered\r\n
0x12000007 | RIO\r\n
0x12000008 | NRT\r\n
0x13000034 | SQM\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x3200000a | Open\r\n
0x3200000b | Bound\r\n
0x3200000c | Connected\r\n
0x3200000d | Disconnected\r\n
0x3200000e | Aborted\r\n
0x3200000f | Closed\r\n
0x32000010 | Freed\r\n
0x32000011 | Modified\r\n
0x34000000 | Info\r\n
0x51000004 | Information\r\n
0x51000005 | Verbose\r\n
0x52000002 | Error\r\n
0x52000003 | Warning\r\n
0x90000001 | Microsoft-Windows-Winsock Catalog Change\r\n
0x90000002 | Microsoft-Windows-Winsock Catalog Change/Operational\r\n
0x91000001 | Microsoft-Windows-Winsock-Sockets sockets provider\r\n
0x92000001 | Microsoft-Windows-Winsock Network Event\r\n
0x92000002 | Microsoft-Windows-Winsock Network Event/Operational\r\n
0x94000001 | Microsoft-Windows-Winsock NameResolution Event\r\n
0x94000002 | Microsoft-Windows-Winsock NameResolution Event/Operational\r\n
0xb0000001 | LSP %1 was installed in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000002 | LSP %1 was removed from the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000003 | LSP %1 was disabled in the %2-bit catalog by %3 (GUID=%4, Category ID=%5)\r\n
0xb0000004 | The %1-bit catalog was reset by the administrator\r\n
0xb0000005 | LSP %1 was bypassed as due to legacy technology bypass policy (GUID=%2)\r\n
0xb2000001 | Socket creation: %1 %2 %3 %4 %5\r\n
0xb2000002 | Socket bind: %1 %2 %3 %4 %5\r\n
0xb2000004 | Socket connect: %1 %2 %3 %4\r\n
0xb2000006 | Connect completed: %1 %2 %3\r\n
0xb2000007 | AFD initiated abort: %1 %2 %3\r\n
0xb2000008 | Transport initiated abort: %1 %2 %3\r\n
0xb2000009 | Failed send request: %1 %2 %3\r\n
0xb200000a | Failed WSASendMsg request: %1 %2 %3\r\n
0xb200000b | Failed recv request: %1 %2 %3\r\n
0xb200000c | Failed recvfrom request: %1 %2 %3\r\n
0xb200000d | Socket close: %1 %2 %3\r\n
0xb200000e | Socket cleanup (all references removed): %1 %2 %3\r\n
0xb200000f | Socket accept: %1 %2 %3 %4 %5\r\n
0xb2000011 | Accept failed: %1 %2 %3\r\n
0xb2000012 | Send posted: %1 %2 %3 %4 %5 %6\r\n
0xb2000013 | Receive posted: %1 %2 %3 %4 %5 %6\r\n
0xb2000014 | RecvFrom posted: %1 %2 %3 %4 %5 %6\r\n
0xb2000015 | SendTo posted: %1 %2 %3 %4 %5 %6 %7 %8\r\n
0xb2000017 | Recv completed: %1 %2 %3 %4\r\n
0xb2000018 | Send completed: %1 %2 %3 %4\r\n
0xb2000019 | SendMsg completed: %1 %2 %3 %4\r\n
0xb200001a | RecvFrom completed: %1 %2 %3 %4 %5 %6 %7\r\n
0xb200001c | SendTo completed: %1 %2 %3 %4\r\n
0xb200001d | Socket option set: %1 %2 %3 %4\r\n
0xb200001e | Select/Poll posted: %1 %2 %3\r\n
0xb200001f | Select/Poll completed: %1 %2 %3\r\n
0xb2000020 | WSAEventSelect: %1 %2 %3\r\n
0xb2000021 | Datagram dropped: %1 %2 %3 %4 %5 %6\r\n
0xb2000023 | Connection indicated: %1 %2 %3 %4\r\n
0xb2000025 | Data indicated from transport: %1 %2 %3\r\n
0xb2000026 | Data indicated from transport: %1 %2 %3 %4 %5\r\n
0xb2000028 | Failed bind: %1 %2 %3\r\n
0xb2000029 | Disconnect indicated from transport: %1 %2\r\n
0xb20003e8 | socket: %1: Process %3 (%8), Endpoint %4, Family %5, Type %6, Protocol %7, Seq %2, Status %9\r\n
0xb20003e9 | closesocket: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb20003ea | socket cleanup: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb20003eb | send: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb20003ec | recv: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb20003ed | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb20003ee | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb20003ef | sendto: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb20003f1 | recvfrom: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb20003f3 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb20003f4 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Seq %2, Status %8\r\n
0xb20003f5 | sendmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb20003f7 | recvmsg: %1: Process %3, Endpoint %4, Buffer Count %5, Buffer %6, Length %7, Addr %10, Seq %2, Status %8\r\n
0xb20003f9 | connect: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb20003fa | connect: %1: Process %3, Endpoint %4, Address %9, Seq %2, Status %7\r\n
0xb20003fc | ConnectEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb20003fd | ConnectEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Seq %2, Status %7\r\n
0xb20003ff | accept: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb2000400 | accept: %1: Process %3, Endpoint %4, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb2000402 | AcceptEx: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb2000403 | AcceptEx: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %9, Accept Endpoint %10, Current Backlog %11, Seq %2, Status %7\r\n
0xb2000405 | bind: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb2000406 | bind: %1: Process %3, Endpoint %4, Address %7, Seq %2, Status %5\r\n
0xb2000408 | connection aborted: %1: Process %3, Endpoint %4, Seq %2, Reason %5\r\n
0xb2000409 | datagram dropped: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2, Reason %9\r\n
0xb200040b | Socket option: %1: Process %3, Endpoint %4, Option %5, Value %6, Seq %2, Status %7\r\n
0xb200040c | Wait for listen: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb200040d | Listen: %1: Process %3, Endpoint %4, Backlog %5, Seq %2, Status %6\r\n
0xb2000bb8 | Connect indication: %1: Process %3, Endpoint %4, Seq %2, Status %5\r\n
0xb2000bb9 | Connect indication: %1: Process %3, Endpoint %4, Address %7, Backlog Count %8, Seq %2, Status %5\r\n
0xb2000bbb | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Seq %2\r\n
0xb2000bbc | Data indication: %1: Process %3, Endpoint %4, Buffer %5, Length %6, Address %8, Seq %2\r\n
0xb2000bbe | disconnect indicated: %1: Process %3, Endpoint %4, Seq %2\r\n
0xb2000bbf | Transport send backlog: Process %1, Endpoint %2, Send Backlog %5\r\n
0xb2000fa0 | Registration domain %1 create status %2\r\n
0xb2000fa1 | Registration domain %1 closed\r\n
0xb2000fa2 | CQ %1 created with %3 entries, index %7 and notification type %8, status %13\r\n
0xb2000fa3 | CQ %1 closed with %2 commit\r\n
0xb2000fa4 | CQ %1 cleaned up\r\n
0xb2000fa5 | CQ %1 with %5 commit resized from %2 to %6, status %10\r\n
0xb2000fa6 | RQ %2 created on endpoint %1 with %8 receive and %4 send entries, using receive CQ %13 and send CQ %12, status %14\r\n
0xb2000fa7 | RQ %1 closed, receive = (%2,%3) send = (%4,%5)\r\n
0xb2000fa8 | RQ %1 cleaned up\r\n
0xb2000fa9 | RQ %1 resized from (%9,%2) to (%12,%5), status = %16\r\n
0xb2000faa | Buffer %1 registered with address %3 and length %5, system address = %4, ID = %6, status = %7\r\n
0xb2000fab | Buffer %1 deregistered with %2 references\r\n
0xb2000fac | Buffer %1 cleaned up\r\n
0xb2000fad | RQ %2 using invalid buffer ID %3\r\n
0xb2000fae | RQ %2 invalid use of buffer %3, offset = %4, length = %5\r\n
0xb2000faf | RQ %1 using invalid buffer size for %2, specified = %3, required = %4\r\n
0xb2000fb0 | NRT Create: Handle = %1 Process = %2 Status = %3\r\n
0xb2000fb1 | NRT Close: Handle = %1 Process = %2\r\n
0xb2000fb2 | CQ %5 notify %1 Seq %2 Status %6\r\n
0xb2000fb3 | accept %1 [1 = Pause, 0 = Unpause] %5 Seq %2 Endpoint %3 Process %4 TlBacklogCount %6.\r\n
0xb40003e8 | GetAddrInfoW is called for queryName %1, serviceName %2, flags %4, family %5, socketType %6, protocol %7 and seq %3\r\n
0xb40003e9 | GetAddrInfoW is completed for queryName %1 with status %2 and result %3\r\n
0xb40003ea | GetAddrInfoExW is called for queryName %1, serviceName %2, nameSpace %4, nameSpace GUID %5, flags %6, family %7, socketType %8, protocol %9, interface index %10, timeOut %11, asyncWithCallBack %12, asyncWithOverlapped %13 and seq %3\r\n
0xb40003eb | GetAddrInfoExW asynchronous query is pending for queryName: %1 with cancel Handle %2\r\n
0xb40003ec | GetAddrInfoExW is completed for queryName %1 with status %2 and result %3\r\n
0xb40003ed | GetAddrInfoExCancel is called for  query %1 and seq %2\r\n
0xb40003ee | NSPLookupServiceBegin is called for provider %1, queryName %2, serviceGUID %3, interface index %4 and control flags %5\r\n
0xb40003ef | NSPLookupServiceBegin is completed for provider %1, queryName %2 serviceGUID %3, interface index %4, control flags %5 and lookup handle %6 with status %7\r\n
0xb40003f0 | NSPLookupServiceNext is called for provider %1, control Flags %2 and lookup handle %3\r\n
0xb40003f1 | NSPLookupServiceNext is completed for provider %1, control Flags %2 and lookup Handle %3 with status %4 and result %5\r\n
0xb40003f2 | NSPLookupServiceEnd is called for provider %1 and lookup handle %2\r\n
0xb40003f3 | NSPLookupServiceEnd completed for provider %1 and lookup handle %2 with status %3\r\n
0xb40003f4 | GetAddrInfoExW info.  queryName %1, serviceName %2, nameSpace %4, nameSpace GUID %5, flags %6, family %7, socketType %8, protocol %9, interface index %10, timeOut %11, asyncWithCallBack %12, asyncWithOverlapped %13, error %14 and seq %3\r\n
0xb40003f5 | Wsa Startup. seq: %1.\r\n
0xb40003f6 | Wsa Cleanup. seq: %1.  Refcount: %2.\r\n
0xb40003f7 | NSJOB info.  seq %1.  Refcount: %2.\r\n
0xd2000001 | SOCK_STREAM\r\n
0xd2000002 | SOCK_DGRAM\r\n
0xd2000003 | SOCK_RAW\r\n
0xd2000004 | SOCK_RDM\r\n
0xd2000005 | SOCK_SEQPACKET\r\n
0xd2000006 | Attempt to flush pending receive requests failed\r\n
0xd2000007 | Abortive disconnect requested on endpoint\r\n
0xd2000008 | Shutdown with SD_RECEIVE posted with receive data pending\r\n
0xd2000009 | Transport indicated abortive disconnect\r\n
0xd200000a | Error on accepted connection not associated with listening socket\r\n
0xd200000b | Disconnect failed\r\n
0xd200000c | Pending data on connection when disconnect called\r\n
0xd200000d | Invalid buffer specified on fastio receive\r\n
0xd200000e | Accept operation failed\r\n
0xd200000f | Unable to allocate buffer\r\n
0xd2000010 | Counter overflow\r\n
0xd2000011 | Data arrives after shutting down receive path\r\n
0xd2000012 | Data arrives during endpoint cleanup\r\n
0xd2000013 | Receive request failed\r\n
0xd2000014 | Send request failed\r\n
0xd2000015 | Send request cancelled\r\n
0xd2000016 | TransmitPackets/TransmitFile request cancelled\r\n
0xd2000017 | Abort indicated during connection request\r\n
0xd2000018 | Plug and play event caused abort\r\n
0xd2000019 | Datagram source address does not match connected address\r\n
0xd200001a | Insufficient local buffer space\r\n
0xd200001b | Buffer allocation failed\r\n
0xd200001c | Insufficient local buffer space - circular queueing enabled\r\n
0xd200001d | Indicated datagram too large - integer overflow\r\n
0xd200001e | SO_OOBINLINE\r\n
0xd200001f | FIONBIO\r\n
0xd2000020 | SO_RCVBUF\r\n
0xd2000021 | SO_SNDBUF\r\n
0xd2000022 | SIO_ENABLE_CIRCULAR_QUEUEING\r\n
0xd2000023 | SIO_UDP_CONNRESET\r\n
0xd2000024 | AFD_IPV6_V6ONLY\r\n
0xd2000025 | SIO_UDP_NETRESET\r\n
0xd2000026 | None\r\n
0xd2000027 | Event\r\n
0xd2000028 | IOCP\r\n
0xd2000029 | source address\r\n
0xd200002a | destination address\r\n
0xd200002b | flags\r\n
0xd200002c | control\r\n
0xd200002d | send\r\n
0xd200002e | receive\r\n
