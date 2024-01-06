## ipbootp.dll

Path: %SystemRoot%\System32\ipbootp.dll

### 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00007531 | IPBOOTP was unable to initialize a critical section.\r\nThe data is the exception code.\r\n
0x00007532 | IPBOOTP was unable to create a heap for memory allocation.\r\nThe data is the error code.\r\n
0x00007533 | IPBOOTP was unable to allocate memory from its heap.\r\nThe data is the error code.\r\n
0x00007534 | IPBOOTP was called to start when it was already running.\r\n
0x00007535 | IPBOOTP was unable to initialize Windows Sockets.\r\nThe data is the error code.\r\n
0x00007536 | IPBOOTP was unable to create a synchronization object.\r\nThe data is the exception code.\r\n
0x00007537 | IPBOOTP was unable to create a table to hold interface information.\r\nThe data is the error code.\r\n
0x00007538 | IPBOOTP was unable to create a semaphore.\r\nThe data is the error code.\r\n
0x00007539 | IPBOOTP was unable to create an event.\r\nThe data is the error code.\r\n
0x0000753a | IPBOOTP was unable to create a timer queue using CreateTimerQueue.\r\nThe data is the error code.\r\n
0x0000753b | IPBOOTP started successfully.\r\n
0x0000753c | IPBOOTP has stopped.\r\n
0x0000753d | IPBOOTP was unable to bind to IP address %1.\r\nPlease make sure TCP/IP is installed and configured correctly.\r\nThe data is the error code.\r\n
0x0000753e | IPBOOTP was unable to activate the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000753f | IPBOOTP was unable to request notification of events\r\non the socket for the local interface with IP address %1.\r\nThe data is the error code.\r\n
0x00007540 | IPBOOTP has discarded a packet received on the local interface\r\nwith IP address %1. The packet had a hop-count of %2, which is\r\ngreater than the maximum value allowed in packets received for\r\nthis interface.\r\nThe hop-count field in a DHCP REQUEST packet indicates how many times\r\nthe packet has been forwarded from one relay-agent to another.\r\n
0x00007541 | IPBOOTP has discarded a packet received on the local interface\r\nwith IP address %1. The packet had a seconds-since-boot of %2,\r\nwhich is less than the minimum value needed for packets to be\r\nforwarded on this interface.\r\nThe seconds-since-boot field in a DHCP REQUEST packet indicates\r\nhow long the DHCP client machine which sent the packet has been\r\ntrying to obtain an IP address.\r\n
0x00007542 | IPBOOTP was unable to relay a DHCP REQUEST packet on the local interface\r\nwith IP address %1; the REQUEST was to have been relayed to\r\nthe DHCP server with IP address %2.\r\nThe data is the error code.\r\n
0x00007543 | IPBOOTP was unable to relay a DHCP REPLY packet on the local interface\r\nwith IP address %1; the REPLY was to have been relayed to\r\nthe DHCP client with hardware address %2.\r\nThe data is the error code.\r\n
0x00007544 | IPBOOTP was unable to enumerate network events on the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x00007545 | IPBOOTP detected an error on the local interface with IP address %1.\r\nThe error occurred while the interface was receiving packets.\r\nThe data is the error code.\r\n
0x00007546 | IPBOOTP was unable to receive an incoming message on the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x00007547 | IPBOOTP received a packet which was smaller than the minimum size\r\nallowed for DHCP packets. The packet has been discarded.\r\nIt was received on the local interface with IP address %1, \r\nand it came from a machine with IP address %2.\r\n
0x00007548 | IPBOOTP received a packet containing an invalid op-code.\r\nThe packet has been discarded. It was received on the local interface\r\nwith IP address %1, and it came from a machine with IP address %2.\r\n
0x00007549 | IPBOOTP could not schedule the processing of a packet received\r\non the local interface with IP address %1. The packet was received\r\nfrom a machine with IP address %2.\r\nThis error may have been caused by a memory allocation failure.\r\nThe data is the error code.\r\n
0x0000754a | IPBOOTP could not schedule a task to be executed.\r\nThis error may have been caused by a memory allocation failure.\r\nThe data is the error code.\r\n
0x0000754b | IPBOOTP could not create a socket for the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x0000754c | IPBOOTP could not enable broadcasting on the socket for\r\nthe local interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000754d | IPBOOTP was unable to register an event with the ntdll wait threads.\r\nThe data is the error code.\r\n
0x0000754e | IPBOOTP could not be configured on the interface.\r\nThe invalid parameter is: %1, value: %2\r\n
