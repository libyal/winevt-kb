## igmpv2.dll

Path: %SystemRoot%\System32\igmpv2.dll

### 5.2.3790.3959

Message identifier | Message string
--- | ---
0x0000a029 | IGMP was unable to initialize a critical section.\r\nThe data is the exception code.\r\n
0x0000a02a | IGMP was unable to create a heap.\r\nThe data is the error code.\r\n
0x0000a02b | IGMP was unable to allocate memory from its heap.\r\nThe data is the error code.\r\n
0x0000a02c | IGMP received a start request when it was already running.\r\n
0x0000a02d | IGMP was unable to start Windows Sockets.\r\nThe data is the error code.\r\n
0x0000a02e | IGMP was unable to create a synchronization object.\r\nThe data is the error code.\r\n
0x0000a02f | IGMP was unable to create an event.\r\nThe data is the error code.\r\n
0x0000a030 | IGMP was unable to create a semaphore.\r\nThe data is the error code.\r\n
0x0000a031 | IGMP was unable to create a socket.\r\nThe data is the error code.\r\n
0x0000a032 | IGMP has started successfully.\r\n
0x0000a033 | IGMP could not schedule a task to be executed.\r\nThis may have been caused by a memory allocation failure.\r\nThe data is the error code.\r\n
0x0000a034 | IGMP was unable to receive an incoming message\r\non the local interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000a035 | IGMP received a packet which was smaller than the minimum size\r\nallowed for IGMP packets. The packet has been discarded.\r\nIt was received on the local interface with IP address %1,\r\nand it came from the neighboring router with IP address %2.\r\n
0x0000a036 | IGMP received a packet with an invalid version in its header.\r\nThe packet has been discarded. It was received on the local interface\r\nwith IP address %1, and it came from the neighboring router\r\nwith IP address %2.\r\n
0x0000a037 | IGMP received a packet with an invalid header. The packet has been\r\ndiscarded. It was received on the local interface with IP address %1,\r\nand it came from the neighboring router with IP address %2.\r\n
0x0000a038 | Router received a general query from RAS Client(%1) on interface\r\nwith IP address %2.\r\nRAS clients are not supposed to send queries.\r\n
0x0000a039 | Different version router with IP Address %1\r\nexists on the interface with IP address %2.\r\n
0x0000a03b | IGMP was unable to send a packet from the interface with IP address %1\r\nto the IP address %2.\r\nThe data is the error code.\r\n
0x0000a03c | IGMP discarded a version %1 packet received on the interface\r\nwith IP address %2 from a neighbor with IP address %3.\r\nThe above interface is configured to accept only version %4 packets.\r\n
0x0000a03d | Igmpv2 was unable to enumerate network events on the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x0000a03e | Igmpv2 detected an error on the local interface with IP address %1.\r\nThe error occurred while the interface was receiving packets.\r\nThe data is the error code.\r\n
0x0000a03f | Igmpv2 was unable to request notification of events\r\non the socket for the local interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000a040 | IGMP was unable to create a socket for the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x0000a041 | IGMP could not bind to port 520 on the socket for\r\nthe local interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000a042 | IGMP could not be configured on Ras Client %1 on interface with\r\nindex %2.\r\nThe data is the error code.\r\n
0x0000a043 | Unable to disable IGMP on Ras Client %1 on the interface with\r\nindex %2.\r\nThe data is the error code.\r\n
0x0000a044 | IGMP could not request multicasting on the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x0000a045 | IGMP could not set router alert option on the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x0000a046 | IGMP could not set the IP header include option on interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x0000a047 | IGMP could not join the multicast group %1\r\non the local interface with IP address %2.\r\nThe data is the error code.\r\n
0x0000a048 | IGMP could not leave the multicast group %1\r\non the local interface with IP address %2.\r\nThe data is the error code.\r\n
0x0000a049 | StopProtocol() called to stop Igmp when it is \r\nalready being stopped.\r\nThe data is the error code.\r\n
0x0000a04a | AddInterface() called to add an Igmp Proxy interface.\r\nIgmp proxy already owns another interface.\r\nThe data is the error code.\r\n
0x0000a04b | AddInterface() called to add an Igmp Ras interface.\r\nRas Server cannot exist on multiple interfaces.\r\nThe data is the error code.\r\n
0x0000a04c | IGMP Router failed to register with MGM.\r\nThe data is the error code.\r\n
0x0000a04d | IGMP Proxy failed to register with MGM.\r\nThe data is the error code.\r\n
0x0000a04e | MgmTakeInterfaceOwnership() failed.\r\nThe data is the error code.\r\n
0x0000a04f | The robustness variable is being set to 1 for Igmp router \r\non Interface %1.\r\nYou should avoid setting it to 1.\r\n
0x0000a050 | One of the values passed to Igmp is invalid.\r\n%1\r\n
0x0000a051 | The wait-events-timers could not be registered with the \r\nwait server thread. Alertable threads might not have \r\nbeen initialized in Rtutils.\r\nThe data is the error code.\r\n
0x0000a052 | IGMP has stopped.\r\n
0x0000a053 | Fatal error. Could not complete.\r\nThe data is the error code.\r\n
0x0000a054 | The version field in the IGMP config field is incorrect.\r\nDelete and create the IGMP config again.\r\n
0x0000a055 | IGMP Protocol type for interface %1 has invalid value %2.\r\nThe data is the error code.\r\n
0x0000a056 | Cannot configure Proxy on RAS server interface %1.\r\n
0x0000a057 | Static group %1 configured on Interface%2 not a valid MCast address.\r\n
0x0000a058 | Static group %1 configured on Interface:%2 does not have valid mode.\r\n
0x0000a059 | Static group %1 configured on Interface:%2 has invalid filter.\r\n
0x0000a05a | Invalid robustness variable:%1 configured on Interface:%2. Max 7.\r\n
0x0000a05b | Invalid Startup Query Count:%1 configured on Interface:%2.\r\n
0x0000a05c | IGMP-Rtr-V%1 activated on Interface:%2.\r\n
0x0000a05d | IGMP Proxy activated on Interface:%1.\r\n
0x0000a05e | Failed to install IGMP Proxy on interface:%1.\r\n
0x0000a05f | Failed to install IGMP Rtr-V-%1 on interface:%2.\r\n
0x0000a060 | Failed to install IGMP Rtr-V-%1 on interface:%2.\r\n
0x0000a061 | Failed to install IGMP Rtr-V-%1 on interface:%2.\r\n
