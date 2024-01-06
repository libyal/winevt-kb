## winnat.sys

Path: %SystemRoot%\system32\drivers\winnat.sys

### 6.3.9600.18226

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | %7 session created. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState:%9\r\n
0xb00003ea | %7 session lifetime updated. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003eb | %7 session state updated. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003ec | %7 session timedout. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003ed | %7 session deleted. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003ee | %5 binding created. Internal transport addr: %2, External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00003ef | %5 binding deleted. Internal transport addr: %2, External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00003f0 | %5 binding session count updated. Internal transport addr: %2, External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00003f1 | Translating %8 packet from %2:%3 to %5:%6, IPID:%7. Status: %9, IcmpType: %10, IcmpCode: %11, IcmpErrorPayload: %12\r\n
0xb00003f2 | Nat Instance %1 %11 Status: %10.UdpIdleSessionTimeout: %2 sec, TcpTransientConnectionTimeout: %3, TcpEstablishedConnectionTimeout: %4, IcmpQueryTimeout: %5, TcpFilteringBehavior: %6, UdpFilteringBehavior: %7, UdpInboundRefresh: %8, Enabled: %9\r\n
0xb00003f3 | Packet filter %12 Status: %13. Instance: %1, SrcPrefix: %3, SrcPrefixLength: %4, DstPrefix: %5, DstPrefixLength: %6, Ipv4Prefix: %7, Ipv4PrefixLength: %8, Nat64: %9, InterfaceLuid: %10\r\n
0xb00003f4 | WFP filter %12 Status: %13. Instance: %1, FilterId: %11, SrcPrefix: %3, SrcPrefixLength: %4, DstPrefix: %5, DstPrefixLength: %6, Ipv4Prefix: %7, Ipv4PrefixLength: %8, Nat64: %9, InterfaceLuid: %10\r\n
0xb00003f5 | Address pool %6 Status: %7. Instance: %1, Address: %2, StartingPort: %3, EndingPort: %4, InterfaceLuid: %5 \r\n
0xb00003f6 | Address %6 notification. Address: %2, InterfaceLuid: %5 \r\n
0xb00003f7 | Static binding %6 Status: %7. Internal Source: %2, External Source: %4, Protocol: %5\r\n
0xb00003f8 | Memory allocation failure: %1\r\n
0xb00003f9 | %7 session created. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6\r\n
0xb00003fa | %7 session deleted. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6\r\n
0xb00003fb | Created NAT instance %1 for RoutingDomainId %2 (CompartmentId %5) with external interface prefix %4/%3\r\n
0xb00003fc | Modified NAT instance %1 properties\r\n
0xb00003fd | NAT instance %1 external interface index is %6 for prefix %4/%3\r\n
0xb00003fe | Deleted NAT instance %1\r\n
0xb00003ff | NAT instance %1: RoutingDomainId %2 (CompartmentId %5), external interface index %6 (%4/%3)\r\n
0xb0000400 | Added external address %3:%4-%5 to NAT instance %1\r\n
0xb0000401 | Removed external address %3:%4-%5 from NAT instance %1\r\n
0xb0000402 | NAT instance %1: external address %3:%4-%5\r\n
0xb0000403 | Added static mapping %2 %5 > %6 (CompartmentId %8) to NAT instance %1 (%3 %9/%10)\r\n
0xb0000404 | Removed static mapping %2 %5 > %6 (CompartmentId %8) from NAT instance %1 (%3 %9/%10)\r\n
0xb0000405 | NAT instance %1: static mapping %2 %5 > %6 (CompartmentId %8) (%3 %9/%10)\r\n
0xb0000406 | NAT dropped IPv4 %5 packet which arrived over %4 interface %3 in compartment %2 with reason: %1.\r\n
0xb0000407 | NAT detected a default route in compartment %1 interface %2. Default routes in internal compartments will prevent NAT operation for those compartments.\r\n
0xb0000409 | NAT instance %1 failed to allocate a %2 port dynamically because all ports in the instance's external address pool are in use.\r\n
0xb000040a | NAT left processing of IPv4 %5 packet to the host network stack over %4 interface %3 in compartment %2 with reason: %1.\r\n
0xb000040b | NAT translated and forwarded IPv4 %5 packet which arrived over %4 interface %3 in compartment %2 to interface %7 in compartment %6.\r\n
0xb000040c | NAT ERROR %1: %2 (%3) Status %4\r\n
0xb00103e9 | %7 session created. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState:%9\r\n
0xb00103ea | %7 session lifetime updated. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103eb | %7 session state updated. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103ec | %7 session timedout. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103ed | %7 session deleted. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103ee | %5 binding created. Internal transport addr: %2 (CompartmentId %8), External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00103ef | %5 binding deleted. Internal transport addr: %2 (CompartmentId %8), External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00103f0 | %5 binding session count updated. Internal transport addr: %2 (CompartmentId %8), External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xd0000001 | IPV4\r\n
0xd0000002 | IPV6\r\n
0xd0000003 | Endpoint independent\r\n
0xd0000004 | Adress dependent\r\n
0xd0000005 | modify\r\n
0xd0000006 | create\r\n
0xd0000007 | createandmodify\r\n
0xd0000008 | delete\r\n
0xd0000009 | ICMPv4\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ICMPv6\r\n
0xd000000d | Closed/NA\r\n
0xd000000e | Internal SYN received\r\n
0xd000000f | External SYN received\r\n
0xd0000010 | Established\r\n
0xd0000011 | Internal FIN received\r\n
0xd0000012 | External FIN received\r\n
0xd0000013 | Both FIN received\r\n
0xd0000014 | 4 minute timewait\r\n
0xd0000015 | one-to-one\r\n
0xd0000016 | one-to-many with remote IP prefix\r\n
0xd0000017 | None\r\n
0xd0000018 | Parsing failure\r\n
0xd0000019 | First packet for the fragmented datagram is not at offset 0\r\n
0xd000001a | Failed to parse or validate the IP packet contained in the ICMP error message payload\r\n
0xd000001b | IP packet contained in the ICMP error message payload does not match any existing session\r\n
0xd000001c | Failed to find a nexthop for external hairpinning\r\n
0xd000001d | No matching static mapping exists to let the packet in\r\n
0xd000001e | Failed to acquire a reference on the nexthop object\r\n
0xd000001f | Failed to clone the packet\r\n
0xd0000020 | Failed to translate the packet\r\n
0xd0000021 | Hop limit exceeded\r\n
0xd0000022 | Packet is larger than nexthop MTU and cannot be fragmented\r\n
0xd0000023 | Unexpected route look-up failure\r\n
0xd0000024 | No route to the packet's (translated) destination was found\r\n
0xd0000025 | Failed to create a session object\r\n
0xd0000026 | The interface over which the packet is to be routed is not a NAT external interface\r\n
0xd0000027 | The interface over which the packet is to be routed does not have a matching NAT instance\r\n
0xd0000028 | NAT device itself is not allowed to be an internal host at the same time\r\n
0xd0000029 | Packet is routable in its own arrival compartment\r\n
0xd000002a | Packet's transport protocol is not supported by NAT\r\n
0xd000002b | Packet is destined to NAT itself\r\n
0xd000002c | Packet's destination address and port do not fall within any NAT external address port range\r\n
0xd000002d | INTERNAL\r\n
0xd000002e | EXTERNAL\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | %7 session created. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState:%9\r\n
0xb00003ea | %7 session lifetime updated. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003eb | %7 session state updated. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003ec | %7 session timedout. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003ed | %7 session deleted. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003ee | %5 binding created. Internal transport addr: %2, External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00003ef | %5 binding deleted. Internal transport addr: %2, External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00003f0 | %5 binding session count updated. Internal transport addr: %2, External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00003f1 | Translating %8 packet from %2:%3 to %5:%6, IPID:%7. Status: %9, IcmpType: %10, IcmpCode: %11, IcmpErrorPayload: %12\r\n
0xb00003f2 | Nat Instance %1 %11 Status: %10.UdpIdleSessionTimeout: %2 sec, TcpTransientConnectionTimeout: %3, TcpEstablishedConnectionTimeout: %4, IcmpQueryTimeout: %5, TcpFilteringBehavior: %6, UdpFilteringBehavior: %7, UdpInboundRefresh: %8, Enabled: %9\r\n
0xb00003f3 | Packet filter %12 Status: %13. Instance: %1, SrcPrefix: %3, SrcPrefixLength: %4, DstPrefix: %5, DstPrefixLength: %6, Ipv4Prefix: %7, Ipv4PrefixLength: %8, Nat64: %9, InterfaceLuid: %10\r\n
0xb00003f4 | WFP filter %12 Status: %13. Instance: %1, FilterId: %11, SrcPrefix: %3, SrcPrefixLength: %4, DstPrefix: %5, DstPrefixLength: %6, Ipv4Prefix: %7, Ipv4PrefixLength: %8, Nat64: %9, InterfaceLuid: %10\r\n
0xb00003f5 | Address pool %6 Status: %7. Instance: %1, Address: %2, StartingPort: %3, EndingPort: %4, InterfaceLuid: %5 \r\n
0xb00003f6 | Address %6 notification. Address: %2, InterfaceLuid: %5 \r\n
0xb00003f7 | Static binding %6 Status: %7. Internal Source: %2, External Source: %4, Protocol: %5\r\n
0xb00003f8 | Memory allocation failure: %1\r\n
0xb00003f9 | %7 session created. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6\r\n
0xb00003fa | %7 session deleted. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6\r\n
0xb00003fb | Created NAT instance %1 for RoutingDomainId %2 (CompartmentId %5) with external interface prefix %4/%3\r\n
0xb00003fc | Modified NAT instance %1 properties\r\n
0xb00003fd | NAT instance %1 external interface index is %6 for prefix %4/%3\r\n
0xb00003fe | Deleted NAT instance %1\r\n
0xb00003ff | NAT instance %1: RoutingDomainId %2 (CompartmentId %5), external interface index %6 (%4/%3)\r\n
0xb0000400 | Added external address %3:%4-%5 to NAT instance %1\r\n
0xb0000401 | Removed external address %3:%4-%5 from NAT instance %1\r\n
0xb0000402 | NAT instance %1: external address %3:%4-%5\r\n
0xb0000403 | Added static mapping %2 %5 > %6 (CompartmentId %8) to NAT instance %1 (%3 %9/%10)\r\n
0xb0000404 | Removed static mapping %2 %5 > %6 (CompartmentId %8) from NAT instance %1 (%3 %9/%10)\r\n
0xb0000405 | NAT instance %1: static mapping %2 %5 > %6 (CompartmentId %8) (%3 %9/%10)\r\n
0xb0000406 | NAT dropped IPv4 %5 packet which arrived over %4 interface %3 in compartment %2 with reason: %1.\r\n
0xb0000407 | NAT detected a default route in compartment %1 interface %2. Default routes in internal compartments will prevent NAT operation for those compartments.\r\n
0xb0000409 | NAT instance %1 failed to allocate a %2 port dynamically because all ports in the instance's external address pool are in use.\r\n
0xb000040a | NAT left processing of IPv4 %5 packet to the host network stack over %4 interface %3 in compartment %2 with reason: %1.\r\n
0xb000040b | NAT translated and forwarded IPv4 %5 packet which arrived over %4 interface %3 in compartment %2 to interface %7 in compartment %6.\r\n
0xb000040c | NAT ERROR %1: %2 (%3) Status %4\r\n
0xb000040d | NAT Instance %1 created with no matching prefix %4/%3.\r\n
0xb000040e | %1\r\n
0xb0000411 | Added IPxlat instance for interface %1\r\n
0xb0000412 | Modified IPxlat instance for interface %1\r\n
0xb0000413 | Deleted IPxlat instance for interface %1\r\n
0xb00103e9 | %7 session created. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState:%9\r\n
0xb00103ea | %7 session lifetime updated. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103eb | %7 session state updated. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103ec | %7 session timedout. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103ed | %7 session deleted. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103ee | %5 binding created. Internal transport addr: %2 (CompartmentId %8), External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00103ef | %5 binding deleted. Internal transport addr: %2 (CompartmentId %8), External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00103f0 | %5 binding session count updated. Internal transport addr: %2 (CompartmentId %8), External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xd0000001 | IPV4\r\n
0xd0000002 | IPV6\r\n
0xd0000003 | Endpoint independent\r\n
0xd0000004 | Adress dependent\r\n
0xd0000005 | modify\r\n
0xd0000006 | create\r\n
0xd0000007 | createandmodify\r\n
0xd0000008 | delete\r\n
0xd0000009 | ICMPv4\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ICMPv6\r\n
0xd000000d | Closed/NA\r\n
0xd000000e | Internal SYN received\r\n
0xd000000f | External SYN received\r\n
0xd0000010 | Established\r\n
0xd0000011 | Internal FIN received\r\n
0xd0000012 | External FIN received\r\n
0xd0000013 | Both FIN received\r\n
0xd0000014 | 4 minute timewait\r\n
0xd0000015 | one-to-one\r\n
0xd0000016 | one-to-many with remote IP prefix\r\n
0xd0000017 | None\r\n
0xd0000018 | Parsing failure\r\n
0xd0000019 | First packet for the fragmented datagram is not at offset 0\r\n
0xd000001a | Failed to parse or validate the IP packet contained in the ICMP error message payload\r\n
0xd000001b | IP packet contained in the ICMP error message payload does not match any existing session\r\n
0xd000001c | Failed to find a nexthop for external hairpinning\r\n
0xd000001d | No matching static mapping exists to let the packet in\r\n
0xd000001e | Failed to acquire a reference on the nexthop object\r\n
0xd000001f | Failed to clone the packet\r\n
0xd0000020 | Failed to translate the packet\r\n
0xd0000021 | Hop limit exceeded\r\n
0xd0000022 | Packet is larger than nexthop MTU and cannot be fragmented\r\n
0xd0000023 | Unexpected route look-up failure\r\n
0xd0000024 | No route to the packet's (translated) destination was found\r\n
0xd0000025 | Failed to create a session object\r\n
0xd0000026 | The interface over which the packet is to be routed is not a NAT external interface\r\n
0xd0000027 | The interface over which the packet is to be routed does not have a matching NAT instance\r\n
0xd0000028 | NAT device itself is not allowed to be an internal host at the same time\r\n
0xd0000029 | Packet is routable in its own arrival compartment\r\n
0xd000002a | Packet's transport protocol is not supported by NAT\r\n
0xd000002b | Packet is destined to NAT itself\r\n
0xd000002c | Packet's destination address and port do not fall within any NAT external address port range\r\n
0xd000002d | INTERNAL\r\n
0xd000002e | EXTERNAL\r\n

### 10.0.15063.0, 10.0.16299.15, 10.0.17134.376, 10.0.17763.1, 10.0.17763.529, 10.0.18362.1, 10.0.18362.815, 10.0.19041.1, 10.0.19041.488, 10.0.22000.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Operational\r\n
0xb00003e9 | %7 session created. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState:%9\r\n
0xb00003ea | %7 session lifetime updated. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003eb | %7 session state updated. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003ec | %7 session timedout. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003ed | %7 session deleted. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00003ee | %5 binding created. Internal transport addr: %2, External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00003ef | %5 binding deleted. Internal transport addr: %2, External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00003f0 | %5 binding session count updated. Internal transport addr: %2, External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00003f1 | Translating %8 packet from %2:%3 to %5:%6, IPID:%7. Status: %9, IcmpType: %10, IcmpCode: %11, IcmpErrorPayload: %12\r\n
0xb00003f2 | Nat Instance %1 %11 Status: %10.UdpIdleSessionTimeout: %2 sec, TcpTransientConnectionTimeout: %3, TcpEstablishedConnectionTimeout: %4, IcmpQueryTimeout: %5, TcpFilteringBehavior: %6, UdpFilteringBehavior: %7, UdpInboundRefresh: %8, Enabled: %9\r\n
0xb00003f3 | Packet filter %12 Status: %13. Instance: %1, SrcPrefix: %3, SrcPrefixLength: %4, DstPrefix: %5, DstPrefixLength: %6, Ipv4Prefix: %7, Ipv4PrefixLength: %8, Nat64: %9, InterfaceLuid: %10\r\n
0xb00003f4 | WFP filter %12 Status: %13. Instance: %1, FilterId: %11, SrcPrefix: %3, SrcPrefixLength: %4, DstPrefix: %5, DstPrefixLength: %6, Ipv4Prefix: %7, Ipv4PrefixLength: %8, Nat64: %9, InterfaceLuid: %10\r\n
0xb00003f5 | Address pool %6 Status: %7. Instance: %1, Address: %2, StartingPort: %3, EndingPort: %4, InterfaceLuid: %5 \r\n
0xb00003f6 | Address %6 notification. Address: %2, InterfaceLuid: %5 \r\n
0xb00003f7 | Static binding %6 Status: %7. Internal Source: %2, External Source: %4, Protocol: %5\r\n
0xb00003f8 | Memory allocation failure: %1\r\n
0xb00003f9 | %7 session created. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6\r\n
0xb00003fa | %7 session deleted. Internal source transport addr: %2, Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6\r\n
0xb00003fb | Created NAT instance %1 for RoutingDomainId %2 (CompartmentId %5) with external interface prefix %4/%3\r\n
0xb00003fc | Modified NAT instance %1 properties\r\n
0xb00003fd | NAT instance %1 external interface index is %6 for prefix %4/%3\r\n
0xb00003fe | Deleted NAT instance %1\r\n
0xb00003ff | NAT instance %1: RoutingDomainId %2 (CompartmentId %5), external interface index %6 (%4/%3)\r\n
0xb0000400 | Added external address %3:%4-%5 to NAT instance %1\r\n
0xb0000401 | Removed external address %3:%4-%5 from NAT instance %1\r\n
0xb0000402 | NAT instance %1: external address %3:%4-%5\r\n
0xb0000403 | Added static mapping %2 %5 > %6 (CompartmentId %8) to NAT instance %1 (%3 %9/%10)\r\n
0xb0000404 | Removed static mapping %2 %5 > %6 (CompartmentId %8) from NAT instance %1 (%3 %9/%10)\r\n
0xb0000405 | NAT instance %1: static mapping %2 %5 > %6 (CompartmentId %8) (%3 %9/%10)\r\n
0xb0000406 | NAT dropped IPv4 %5 packet which arrived over %4 interface %3 in compartment %2 with reason: %1.\r\n
0xb0000407 | NAT detected a default route in compartment %1 interface %2. Default routes in internal compartments will prevent NAT operation for those compartments.\r\n
0xb0000409 | NAT instance %1 failed to allocate a %2 port dynamically because all ports in the instance's external address pool are in use.\r\n
0xb000040a | NAT left processing of IPv4 %5 packet to the host network stack over %4 interface %3 in compartment %2 with reason: %1.\r\n
0xb000040b | NAT translated and forwarded IPv4 %5 packet which arrived over %4 interface %3 in compartment %2 to interface %7 in compartment %6.\r\n
0xb000040c | NAT ERROR %1: %2 (%3) Status %4\r\n
0xb000040d | NAT Instance %1 created with no matching prefix %4/%3.\r\n
0xb000040e | %1\r\n
0xb0000411 | Added IPxlat instance for interface %1\r\n
0xb0000412 | Modified IPxlat instance for interface %1\r\n
0xb0000413 | Deleted IPxlat instance for interface %1\r\n
0xb0000414 | XLAT: %1\r\n
0xb0000415 | Added internal address %3, IfIndex %4 to NAT instance %1\r\n
0xb0000416 | Removed internal address %3: IfIndex %4 from NAT instance %1\r\n
0xb00103e9 | %7 session created. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState:%9\r\n
0xb00103ea | %7 session lifetime updated. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103eb | %7 session state updated. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103ec | %7 session timedout. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103ed | %7 session deleted. Internal source transport addr: %2 (CompartmentId %10), Internal dest transport addr: %3, External source transport addr %5, External dest transport addr %6, Lifetime: %8 seconds, TcpState: %9\r\n
0xb00103ee | %5 binding created. Internal transport addr: %2 (CompartmentId %8), External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00103ef | %5 binding deleted. Internal transport addr: %2 (CompartmentId %8), External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00103f0 | %5 binding session count updated. Internal transport addr: %2 (CompartmentId %8), External transport addr %4, SessionCount: %6, Configured: %7\r\n
0xb00103fb | Created %14 NAT %1 for RoutingDomainId %2 (CompartmentId %5) with prefix %4/%3\r\n
0xb00103ff | %14 NAT %1, Prefix %4/%3 RoutingDomainId %2 (CompartmentId %5), external interface index %6\r\n
0xb001040d | %14 NAT %1 created with no matching prefix %4/%3.\r\n
0xd0000001 | IPV4\r\n
0xd0000002 | IPV6\r\n
0xd0000003 | Endpoint independent\r\n
0xd0000004 | Adress dependent\r\n
0xd0000005 | modify\r\n
0xd0000006 | create\r\n
0xd0000007 | createandmodify\r\n
0xd0000008 | delete\r\n
0xd0000009 | ICMPv4\r\n
0xd000000a | TCP\r\n
0xd000000b | UDP\r\n
0xd000000c | ICMPv6\r\n
0xd000000d | Closed/NA\r\n
0xd000000e | Internal SYN received\r\n
0xd000000f | External SYN received\r\n
0xd0000010 | Established\r\n
0xd0000011 | Internal FIN received\r\n
0xd0000012 | External FIN received\r\n
0xd0000013 | Both FIN received\r\n
0xd0000014 | 4 minute timewait\r\n
0xd0000015 | one-to-one\r\n
0xd0000016 | one-to-many with remote IP prefix\r\n
0xd0000017 | None\r\n
0xd0000018 | Parsing failure\r\n
0xd0000019 | First packet for the fragmented datagram is not at offset 0\r\n
0xd000001a | Failed to parse or validate the IP packet contained in the ICMP error message payload\r\n
0xd000001b | IP packet contained in the ICMP error message payload does not match any existing session\r\n
0xd000001c | Failed to find a nexthop for external hairpinning\r\n
0xd000001d | No matching static mapping exists to let the packet in\r\n
0xd000001e | Failed to acquire a reference on the nexthop object\r\n
0xd000001f | Failed to clone the packet\r\n
0xd0000020 | Failed to translate the packet\r\n
0xd0000021 | Hop limit exceeded\r\n
0xd0000022 | Packet is larger than nexthop MTU and cannot be fragmented\r\n
0xd0000023 | Unexpected route look-up failure\r\n
0xd0000024 | No route to the packet's (translated) destination was found\r\n
0xd0000025 | Failed to create a session object\r\n
0xd0000026 | The interface over which the packet is to be routed is not a NAT external interface\r\n
0xd0000027 | The interface over which the packet is to be routed does not have a matching NAT instance\r\n
0xd0000028 | NAT device itself is not allowed to be an internal host at the same time\r\n
0xd0000029 | Packet is routable in its own arrival compartment\r\n
0xd000002a | Packet's transport protocol is not supported by NAT\r\n
0xd000002b | Packet is destined to NAT itself\r\n
0xd000002c | Packet's destination address and port do not fall within any NAT external address port range\r\n
0xd000002d | Winnat MUX rejected the packet\r\n
0xd000002e | Winnat MUX failed to find the VIP/DIP configuration\r\n
0xd000002f | Winnat MUX failed to send the encapsulated packet\r\n
0xd0000030 | The interface over which the packet has arrived does not have a matching NAT instance\r\n
0xd0000031 | INTERNAL\r\n
0xd0000032 | EXTERNAL\r\n
0xd0000033 | InternalPrefixInstance\r\n
0xd0000034 | ExternalPrefixInstance\r\n
