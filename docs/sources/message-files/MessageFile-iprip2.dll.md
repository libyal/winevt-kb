## iprip2.dll

Path: %SystemRoot%\System32\iprip2.dll

### 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00007531 | IPRIPv2 was unable to initialize a critical section.\r\nThe data is the exception code.\r\n
0x00007532 | IPRIPv2 was unable to create a heap.\r\nThe data is the error code.\r\n
0x00007533 | IPRIPv2 was unable to allocate memory from its heap.\r\nThe data is the error code.\r\n
0x00007534 | IPRIPv2 received a start request when it was already running.\r\n
0x00007535 | IPRIPv2 was unable to start Windows Sockets.\r\nThe data is the error code.\r\n
0x00007536 | IPRIPv2 was unable to create a synchronization object.\r\nThe data is the error code.\r\n
0x00007537 | IPRIPv2 was unable to create an event.\r\nThe data is the error code.\r\n
0x00007538 | IPRIPv2 was unable to initialize a table to hold information\r\nabout configured network interfaces.\r\nThe data is the error code.\r\n
0x00007539 | IPRIPv2 was unable to initialize a table to hold information\r\nabout neighboring IPRIP routers.\r\nThe data is the error code.\r\n
0x0000753a | IPRIPv2 was unable to initialize a table to hold information\r\nabout local IP addresses.\r\nThe data is the error code.\r\n
0x0000753b | IPRIPv2 was unable to create a semaphore.\r\nThe data is the error code.\r\n
0x0000753c | IPRIPv2 was unable to create a socket.\r\nThe data is the error code.\r\n
0x0000753d | IPRIPv2 was unable to register with the Routing Table Manager.\r\nThe data is the error code.\r\n
0x0000753e | IPRIPv2 was unable to create a thread.\r\nThe data is the error code.\r\n
0x0000753f | IPRIPv2 has started successfully.\r\n
0x00007540 | IPRIPv2 could not bind to IP address %1.\r\nPlease make sure TCP/IP is installed and configured correctly.\r\nThe data is the error code.\r\n
0x00007541 | IPRIPv2 could not schedule a task to be executed.\r\nThis may have been caused by a memory allocation failure.\r\nThe data is the error code.\r\n
0x00007542 | IPRIPv2 was unable to add a route to the Routing Table Manager.\r\nThe route is to network %1 with next-hop %3.\r\nThe data is the error code.\r\n
0x00007543 | IPRIPv2 received an error in a call to select().\r\nThis may indicate underlying network problems.\r\nThe data is the error code.\r\n
0x00007544 | IPRIPv2 was unable to receive an incoming message\r\non the local interface with IP address %1.\r\nThe data is the error code.\r\n
0x00007545 | IPRIPv2 received a packet which was smaller than the minimum size\r\nallowed for IPRIP packets. The packet has been discarded.\r\nIt was received on the local interface with IP address %1,\r\nand it came from the neighboring router with IP address %2.\r\n
0x00007546 | IPRIPv2 received a packet with an invalid version in its header.\r\nThe packet has been discarded. It was received on the local interface\r\nwith IP address %1, and it came from the neighboring router\r\nwith IP address %2.\r\n
0x00007547 | IPRIPv2 received a packet with an invalid header. The packet has been\r\ndiscarded. It was received on the local interface with IP address %1,\r\nand it came from the neighboring router with IP address %2.\r\n
0x00007548 | IPRIPv2 was unable to send a packet from the interface with IP address %1\r\nto the IP address %2.\r\nThe data is the error code.\r\n
0x00007549 | IPRIPv2 discarded a response packet from a neighbor with IP address %1.\r\nIPRIPv2 is not configured to accept packets from the above neighbor.\r\n
0x0000754a | IPRIPv2 discarded a version %1 packet received on the interface\r\nwith IP address %2 from a neighbor with IP address %3.\r\nThe above interface is configured to accept only version %4 packets.\r\n
0x0000754b | IPRIPv2 discarded a packet received on the interface with IP address %1\r\nfrom a neighboring router with IP address %2, because the packet\r\nfailed authentication.\r\n
0x0000754c | IPRIPv2 is ignoring a route to %1 with next-hop %2 which was advertised\r\nby a neighbor with IP address %3. The route's network class is invalid.\r\n
0x0000754d | IPRIPv2 is ignoring a route to the loopback network %1 with next-hop %2\r\nwhich was advertised by a neighbor with IP address %3.\r\n
0x0000754e | IPRIPv2 is ignoring a route to the broadcast network %1 with next-hop %2\r\nwhich was advertised by a neighbor with IP address %3.\r\n
0x0000754f | IPRIPv2 is ignoring a host route to %1 with next-hop %2 which was\r\nadvertised by a neighbor with IP address %3, because the interface\r\non which the route was received is configured to reject host routes.\r\n
0x00007550 | IPRIPv2 is ignoring a default route with next-hop %2 which was\r\nadvertised by a neighbor with IP address %3, because the interface\r\non which the route was received is configured to reject default routes.\r\n
0x00007551 | IPRIPv2 is ignoring a route to %1 with next-hop %2 which was advertised\r\nby a neighbor with IP address %3, because the interface on which\r\nthe route was received has a filter configured which excluded this route.\r\n
0x00007552 | IPRIPv2 was unable to add a route to the Routing Table Manager.\r\nThe route is to %1 with next-hop %2 and it was received from a neighbor\r\nwith IP address %3.\r\nThe data is the error code.\r\n
0x00007553 | IPRIPv2 was unable to enumerate the routes in the Routing Table Manager.\r\nThe data is the error code.\r\n
0x00007554 | IPRIPv2 has stopped.\r\n
0x00007555 | IPRIPv2 has learnt of a new route. The route is to network %1\r\nwith next-hop %2, and the route was learnt from the neighbor\r\nwith IP address %3.\r\n
0x00007556 | IPRIPv2 has changed the next-hop of the route to %1.\r\nThe new next-hop is %2.\r\n
0x00007557 | IPRIPv2 has learnt of a change in metric for its route to %1 \r\nwith next-hop %2. The new metric is %3.\r\n
0x00007558 | IPRIPv2 has learnt of a new route. The route is to network %1\r\nwith next-hop %2.\r\n
0x00007559 | IPRIPv2 has timed-out its route to %1 with next-hop %2,\r\nsince no neighboring routers announced the route.\r\nThe route will now be marked for deletion.\r\n
0x0000755a | IPRIPv2 has deleted its route to %1 with next-hop %2,\r\nsince the route timed-out and no neighboring routers announced the route.\r\n
0x0000755b | IPRIPv2 is ignoring a route on the local interface with IP address %1.\r\nThe route is to the network %1 and it was received from a neighbor\r\nwith IP address %2.\r\nThe route is being ignored because it contains some invalid information.\r\n
0x0000755c | IPRIPv2 is ignoring a route to %1 with next-hop %2\r\nwhich was advertised by a neighbor with IP address %3,\r\nsince the route was advertised with an invalid metric.\r\nThe data is the metric.\r\n
0x0000755d | IPRIPv2 was unable to enumerate network events on the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x0000755e | IPRIPv2 detected an error on the local interface with IP address %1.\r\nThe error occurred while the interface was receiving packets.\r\nThe data is the error code.\r\n
0x0000755f | IPRIPv2 was unable to request notification of events\r\non the socket for the local interface with IP address %1.\r\nThe data is the error code.\r\n
0x00007560 | IPRIPv2 was unable to create a socket for the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x00007561 | IPRIPv2 could not enable broadcasting on the socket for\r\nthe local interface with IP address %1.\r\nThe data is the error code.\r\n
0x00007562 | IPRIPv2 could not bind to port 520 on the socket for\r\nthe local interface with IP address %1.\r\nThe data is the error code.\r\n
0x00007563 | IPRIPv2 could not request multicasting on the local interface\r\nwith IP address %1.\r\nThe data is the error code.\r\n
0x00007564 | IPRIPv2 could not join the multicast group 224.0.0.9\r\non the local interface with IP address %1.\r\nThe data is the error code.\r\n
0x00007565 | IPRIPv2 discarded a response packet from a neighbor with IP address %1.\r\nThe packet was not sent from the standard IP RIP port (520).\r\n
0x00007566 | IPRIPv2 could not register an event with the Ntdll wait thread.\r\nThe data is the error code.\r\n
0x00007567 | IPRIPv2 could not register a timer queue with the Ntdll thread.\r\nThe data is the error code.\r\n
0x00007568 | IPRIPV2 could not be enabled on the interface.\r\nParameter %1 has an invalid value %2.\r\n
0x00007569 | Peer with IP address %1 was unable to receive RIP message sent out\r\nfrom interface with IP address %2.\r\nThe peer might be rebooting, or Routing and Remote Access service\r\nmight not be running on the peer.\r\n
