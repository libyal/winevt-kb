## dhcpcore6.dll

Path: %SystemRoot%\system32\dhcpcore6.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x000003ec | Error occurred in stopping the Dhcpv6 client service. ErrorCode is %1.ShutDown Flag value is %2.\r\n
0x0000c766 | DHCPv6 client service is started\r\n
0x0000c767 | DHCPv6 client service is stopped. ShutDown Flag value is %1\r\n
0x10000031 | Response Time\r\n
0x3000000b | MediaConnect\r\n
0x3000000c | MediaDisconnect\r\n
0x3000000d | RAChanged\r\n
0x3000000e | PerfTrackMediaConnect\r\n
0x3000000f | PerfTrackMediaConnectEnd\r\n
0x30000010 | InterfaceAdded\r\n
0x30000011 | InitSARR\r\n
0x30000012 | InitConfirmReply\r\n
0x30000013 | SolicitSent\r\n
0x30000014 | AdvertiseReceived\r\n
0x30000015 | AdvertiseDiscarded\r\n
0x30000016 | RequestSent\r\n
0x30000017 | ReplyForRequestReceived\r\n
0x30000018 | InvalidReplyForRequestReceived\r\n
0x30000019 | RenewSent\r\n
0x3000001a | ReplyForRenewReceived\r\n
0x3000001b | InvalidReplyForRenewReceived\r\n
0x3000001c | RebindSent\r\n
0x3000001d | ReplyForRebindReceived\r\n
0x3000001e | InvalidReplyForRebindReceived\r\n
0x3000001f | ConfirmSent\r\n
0x30000020 | ReplyForConfirmReceived\r\n
0x30000021 | InvalidReplyForConfirmReceived\r\n
0x30000022 | DeclineSent\r\n
0x30000023 | ReplyForDeclineReceived\r\n
0x30000024 | InvalidReplyForDeclineReceived\r\n
0x30000025 | ReleaseSent\r\n
0x30000026 | InfoRequestSent\r\n
0x30000027 | ReplyForInfoRequestReceived\r\n
0x30000028 | InvalidReplyForInfoRequestReceived\r\n
0x3000002a | ErrorCreatingPacket\r\n
0x3000002b | ErrorExtractingOptions\r\n
0x3000002c | ErrorInParsing\r\n
0x3000002d | InformationRefreshTimeOptionReceived\r\n
0x3000002e | InformationRefreshTimeExpired\r\n
0x3000002f | PerfTrackSARR\r\n
0x30000030 | PerfTrackInfoRequest\r\n
0x30000031 | StatefulToStateless\r\n
0x30000032 | StatelessToStateful\r\n
0x30000033 | NonDhcpToStateful\r\n
0x30000034 | NonDhcpToStateless\r\n
0x30000035 | StaticMode\r\n
0x30000036 | AddressPlumbed\r\n
0x30000037 | AddressUnplumbed\r\n
0x30000038 | IPConflict\r\n
0x30000039 | LeaseExpired\r\n
0x3000003a | InitNetworkInterfaceFailed\r\n
0x3000003b | ErrorPlumbingParameters\r\n
0x3000003c | ErrorOpeningSocket\r\n
0x3000003d | ErrorClosingSocket\r\n
0x3000003e | ServiceStart\r\n
0x3000003f | ServiceStop\r\n
0x30000040 | ErrorInitService\r\n
0x30000041 | DnsRegistrationDone\r\n
0x30000042 | dnsDeregistrationDone\r\n
0x30000043 | ErrorInitializingInterface\r\n
0x30000044 | NetworkError\r\n
0x30000045 | StatefulToStateful\r\n
0x30000046 | InvalidMessageDiscarded\r\n
0x30000047 | AddressAlreadyExists\r\n
0x30000048 | LostIpAddress\r\n
0x30000049 | SetClassID\r\n
0x3000004a | FailedToObtainLease\r\n
0x3000004b | LeaseRenewalFailed\r\n
0x3000004c | ErrorServiceStop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Media State Event\r\n
0x70000002 | Protocol State Event\r\n
0x70000003 | Address Configuration State Event\r\n
0x70000004 | Service State Event\r\n
0x70000005 | Winsock State Event\r\n
0x70000006 | DNS State Event\r\n
0x90000001 | Microsoft-Windows-DHCPv6-Client\r\n
0x90000002 | Microsoft-Windows-DHCPv6 Client Events/Admin\r\n
0x90000003 | Microsoft-Windows-DHCP Client Events/Operational\r\n
0x90000004 | System\r\n
0xb00003e8 | Your computer has lost the lease to its IP address %1 on the Network Card with network address %3.\r\n
0xb00003eb | Your computer was not able to renew its address from the network (from the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb00003ed | Your computer has detected that the IP address %1 for the Network Card with network address %3 is already in use on the network. Your computer will automatically attempt to obtain a different address.\r\n
0xb00003ee | Router Advertisement settings have been changed on the network adapter %1. The current M - Managed Address Configuration flag is %2 and the O - Other Stateful Configuration flag is %3. User Action: If you are seeing this event frequently, then it could be due to frequent change in M and O flag settings on the router in the network. Please contact your network administrator to have it resolved.\r\n
0xb00003f0 | An error occurred in initializing the interface. The error code is: %1.\r\n
0xb000c389 | A network error occurred when trying to send a message. The error code is: %1.\r\n
0xb000c739 | Media Connect notification has been received with Adapter interface id %1\r\n
0xb000c73a | Media Disconnect notification has been received with Adapter interface id %1\r\n
0xb000c73c | Confirm-Reply is initiated on the adapter with Interface Id %1\r\n
0xb000c73d | Solicit-Advertise-Request-Reply is initiated on the adapter with Interface Id %1\r\n
0xb000c73e | Solicit is sent from the adapter %1. Status code is %2\r\n
0xb000c73f | Advertise is received from the adapter %1. Status code is %2. Offered Address is %3\r\n
0xb000c740 | Advertise is discarded from the adapter %1. Status code is %2\r\n
0xb000c741 | Request is sent from the adapter %1. Status code is %2\r\n
0xb000c742 | A valid reply is received for request from the adapter %1. Status code is %2. Received address is %3\r\n
0xb000c743 | Incorrect reply is received for request from the adapter %1. Status code is %2\r\n
0xb000c744 | Renew is sent in the adapter %1. Status code is %2\r\n
0xb000c745 | A valid reply is received for renew from the adapter %1. Status code is %2\r\n
0xb000c746 | A Invalid reply is received for renew from the adapter %1. Status code is %2\r\n
0xb000c747 | Rebind is sent in the adapter %1. Status code is %2\r\n
0xb000c748 | A valid reply is received for rebind from the adapter %1. Status code is %2\r\n
0xb000c749 | A Invalid reply is received for rebind from the adapter %1. Status code is %2\r\n
0xb000c74a | Release is sent in the adapter %1. Status code is %2\r\n
0xb000c74b | Decline is sent in the adapter %1. Status code is %2\r\n
0xb000c74c | A valid reply is received for decline in the adapter %1. Status code is %2\r\n
0xb000c74d | A Invalid reply is received for decline from the adapter %1. Status code is %2\r\n
0xb000c74e | Confirm is sent in the adapter %1. Status code is %2\r\n
0xb000c74f | A valid reply is received for confirm in the adapter %1. Status code is %2\r\n
0xb000c750 | A Invalid reply is received for confirm in the adapter %1. Status code is %2\r\n
0xb000c751 | Info-request is sent in the adapter %1. Status code is %2\r\n
0xb000c752 | A valid reply is received for Info-request in the adapter %1. Status code is %2\r\n
0xb000c753 | A Invalid reply is received for Info-request in the adapter %1. Status code is %2\r\n
0xb000c755 | An error occurred in creation of packet for the adapter %1. Error code is %2\r\n
0xb000c756 | An error occurred in extracting options from the message received in the adapter %1. Status code is %2\r\n
0xb000c757 | Dhcp is changed from stateful to stateless mode in the adapter %1. Status Code is %2.\r\n
0xb000c758 | Dhcp is changed from stateless to stateful mode in the adapter %1. Status Code is %2.\r\n
0xb000c759 | Dhcp is changed from nondhcp to stateful mode in the adapter %1. Status Code is %2.\r\n
0xb000c75a | Dhcp is changed from nondhcp to stateless mode in the adapter %1. Status Code is %2.\r\n
0xb000c75b | Dhcp is converted to static mode in the adapter %1. Status Code is %2.\r\n
0xb000c75c | Error occurred in parsing the dhcp message received in the interface id %1\r\n
0xb000c75d | Information refresh time option is received in the interface %1 with a refresh time value of %2\r\n
0xb000c75e | The information refresh time has expired, hence triggering a new inform packet on the interface %1.\r\n
0xb000c75f | Address %1 is plumbed to the adapter %2. Status Code is %3.\r\n
0xb000c760 | Address %1 is unplumbed from the adapter %2. Status Code is %3.\r\n
0xb000c763 | An interface is added whose interface index is %1. Status Code is %2.\r\n
0xb000c764 | An error occurred in initializing the interface %1. Status Code is %2.\r\n
0xb000c765 | An error occurred in plumbing the parameters into stack. Status Code is %1.\r\n
0xb000c768 | An error has occurred in opening the socket in the adapter %1. Error Code is %2.\r\n
0xb000c769 | An error has occurred in closing the socket in the adapter %1. Error Code is %2.\r\n
0xb000c76a | Dns registration has happened for the adapter %1. Status Code is %2.DNS Flag settings is %3.\r\n
0xb000c76b | Dns deregistration has happened for the adapter %1. Status Code is %2.\r\n
0xb000c772 | Dhcp is changed from stateful to stateful mode in the adapter %1. Status Code is %2.\r\n
0xb000c773 | Message is Invalid and it is discarded.\r\n
0xb000c774 | The Class ID %1 was set for the adapter %3.\r\n
0xb000c775 | Address %1 being plumbed for adapter %2 already exists\r\n
0xb000c776 | Your computer was not assigned an address from the network (by the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb000ea60 | PERFTRACK (DHCPSOLICIT): Offer is accepted in the IPv6 adapter %2. Offered Address is %3.\r\n
0xb000ea61 | PERFTRACK (DHCINFORMATIONREQUEST): Options received in the IPv6 adapter %2. \r\n
0xb000ea62 | PERFTRACK (DHCPv6): Media Connect on adapter %2\r\n
0xb000ea63 | PERFTRACK (DHCPv6): End of Media Connect on adapter %2\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x000003ec | Error occurred in stopping the Dhcpv6 client service. ErrorCode is %1.ShutDown Flag value is %2.\r\n
0x0000c766 | DHCPv6 client service is started\r\n
0x0000c767 | DHCPv6 client service is stopped. ShutDown Flag value is %1\r\n
0x10000031 | Response Time\r\n
0x3000000b | MediaConnect\r\n
0x3000000c | MediaDisconnect\r\n
0x3000000d | RAChanged\r\n
0x3000000e | PerfTrackMediaConnect\r\n
0x3000000f | PerfTrackMediaConnectEnd\r\n
0x30000010 | InterfaceAdded\r\n
0x30000011 | InitSARR\r\n
0x30000012 | InitConfirmReply\r\n
0x30000013 | SolicitSent\r\n
0x30000014 | AdvertiseReceived\r\n
0x30000015 | AdvertiseDiscarded\r\n
0x30000016 | RequestSent\r\n
0x30000017 | ReplyForRequestReceived\r\n
0x30000018 | InvalidReplyForRequestReceived\r\n
0x30000019 | RenewSent\r\n
0x3000001a | ReplyForRenewReceived\r\n
0x3000001b | InvalidReplyForRenewReceived\r\n
0x3000001c | RebindSent\r\n
0x3000001d | ReplyForRebindReceived\r\n
0x3000001e | InvalidReplyForRebindReceived\r\n
0x3000001f | ConfirmSent\r\n
0x30000020 | ReplyForConfirmReceived\r\n
0x30000021 | InvalidReplyForConfirmReceived\r\n
0x30000022 | DeclineSent\r\n
0x30000023 | ReplyForDeclineReceived\r\n
0x30000024 | InvalidReplyForDeclineReceived\r\n
0x30000025 | ReleaseSent\r\n
0x30000026 | InfoRequestSent\r\n
0x30000027 | ReplyForInfoRequestReceived\r\n
0x30000028 | InvalidReplyForInfoRequestReceived\r\n
0x3000002a | ErrorCreatingPacket\r\n
0x3000002b | ErrorExtractingOptions\r\n
0x3000002c | ErrorInParsing\r\n
0x3000002d | InformationRefreshTimeOptionReceived\r\n
0x3000002e | InformationRefreshTimeExpired\r\n
0x3000002f | PerfTrackSARR\r\n
0x30000030 | PerfTrackInfoRequest\r\n
0x30000031 | StatefulToStateless\r\n
0x30000032 | StatelessToStateful\r\n
0x30000033 | NonDhcpToStateful\r\n
0x30000034 | NonDhcpToStateless\r\n
0x30000035 | StaticMode\r\n
0x30000036 | AddressPlumbed\r\n
0x30000037 | AddressUnplumbed\r\n
0x30000038 | IPConflict\r\n
0x30000039 | LeaseExpired\r\n
0x3000003a | InitNetworkInterfaceFailed\r\n
0x3000003b | ErrorPlumbingParameters\r\n
0x3000003c | ErrorOpeningSocket\r\n
0x3000003d | ErrorClosingSocket\r\n
0x3000003e | ServiceStart\r\n
0x3000003f | ServiceStop\r\n
0x30000040 | ErrorInitService\r\n
0x30000041 | DnsRegistrationDone\r\n
0x30000042 | dnsDeregistrationDone\r\n
0x30000043 | ErrorInitializingInterface\r\n
0x30000044 | NetworkError\r\n
0x30000045 | StatefulToStateful\r\n
0x30000046 | InvalidMessageDiscarded\r\n
0x30000047 | AddressAlreadyExists\r\n
0x30000048 | LostIpAddress\r\n
0x30000049 | SetClassID\r\n
0x3000004a | FailedToObtainLease\r\n
0x3000004b | LeaseRenewalFailed\r\n
0x3000004c | ErrorServiceStop\r\n
0x3000004d | FirewallPortExempted\r\n
0x3000004e | FirewallPortClosed\r\n
0x3000004f | ModeChanging\r\n
0x30000050 | AggressiveRetryOn\r\n
0x30000051 | DontStartSolicitInCSSinceV4Plumbed\r\n
0x30000052 | StartSolicitInCSSinceV4Unplumbed\r\n
0x30000053 | AbandonSolicitInCSSinceDhcp\r\n
0x30000054 | StartSolicitInCSAtCompulsoryTime\r\n
0x30000055 | AcquireNICReference\r\n
0x30000056 | ReleaseNICReference\r\n
0x30000057 | FirewallPortExemptionTriggered\r\n
0x30000058 | FirewallPortCloseTriggered\r\n
0x30000059 | NotifyCSEntry\r\n
0x3000005a | NotifyCSExit\r\n
0x3000005b | AbandonSolicitInCSSinceStatic\r\n
0x3000005c | EnableDhcpV6\r\n
0x3000005d | DisableDhcpV6\r\n
0x3000005e | NoProcessingSinceDhcpV6Disabled\r\n
0x3000005f | AbandonSolicitInCSSinceV6Static\r\n
0x30000060 | AbandonSolicitInCSSinceV6Stateless\r\n
0x30000061 | AbandonSolicitSinceNonMulticast\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Media State Event\r\n
0x70000002 | Protocol State Event\r\n
0x70000003 | Address Configuration State Event\r\n
0x70000004 | Service State Event\r\n
0x70000005 | Winsock State Event\r\n
0x70000006 | DNS State Event\r\n
0x70000007 | Network Parameter State Event\r\n
0x90000001 | Microsoft-Windows-DHCPv6-Client\r\n
0x90000002 | Microsoft-Windows-DHCPv6 Client Events/Admin\r\n
0x90000003 | Microsoft-Windows-DHCP Client Events/Operational\r\n
0x90000004 | System\r\n
0xb00003e8 | Your computer has lost the lease to its IP address %1 on the Network Card with network address %3.\r\n
0xb00003eb | Your computer was not able to renew its address from the network (from the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb00003ed | Your computer has detected that the IP address %1 for the Network Card with network address %3 is already in use on the network. Your computer will automatically attempt to obtain a different address.\r\n
0xb00003ee | Router Advertisement settings have been changed on the network adapter %1. The current M - Managed Address Configuration flag is %2 and the O - Other Stateful Configuration flag is %3. User Action: If you are seeing this event frequently, then it could be due to frequent change in M and O flag settings on the router in the network. Please contact your network administrator to have it resolved.\r\n
0xb00003f0 | An error occurred in initializing the interface. The error code is: %1.\r\n
0xb000c389 | A network error occurred when trying to send a message. The error code is: %1.\r\n
0xb000c397 | Attempting to acquire a reference for interface %1. Error code is %2.\r\n
0xb000c398 | Attempting to release the reference for interface %1. Error code is %2.\r\n
0xb000c739 | Media Connect notification has been received on interface with interface id %1\r\n
0xb000c73a | Media Disconnect notification has been received on interface with interface id %1\r\n
0xb000c73c | Confirm-Reply is initiated on the interface with Interface Id %1\r\n
0xb000c73d | Solicit-Advertise-Request-Reply is initiated on the interface with Interface Id %1. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c73e | Solicit is sent from the interface %1. Status code is %2\r\n
0xb000c73f | Advertise is received from the interface %1. Status code is %2. Offered Address is %3\r\n
0xb000c740 | Advertise is discarded from the interface %1. Status code is %2\r\n
0xb000c741 | Request is sent from the interface %1. Status code is %2\r\n
0xb000c742 | A valid reply is received for request from the interface %1. Status code is %2. Received address is %3\r\n
0xb000c743 | Incorrect reply is received for request from the interface %1. Status code is %2\r\n
0xb000c744 | Renew is sent on the interface %1. Status code is %2\r\n
0xb000c745 | A valid reply is received for renew from the interface %1. Status code is %2\r\n
0xb000c746 | An invalid reply is received for renew from the interface %1. Status code is %2\r\n
0xb000c747 | Rebind is sent on the interface %1. Status code is %2\r\n
0xb000c748 | A valid reply is received for rebind from the interface %1. Status code is %2\r\n
0xb000c749 | An invalid reply is received for rebind from the interface %1. Status code is %2\r\n
0xb000c74a | Release is sent on the interface %1. Status code is %2\r\n
0xb000c74b | Decline is sent on the interface %1. Status code is %2\r\n
0xb000c74c | A valid reply is received for decline on the interface %1. Status code is %2\r\n
0xb000c74d | An invalid reply is received for decline on the interface %1. Status code is %2\r\n
0xb000c74e | Confirm is sent on the interface %1. Status code is %2\r\n
0xb000c74f | A valid reply is received for confirm on the interface %1. Status code is %2\r\n
0xb000c750 | An invalid reply is received for confirm on the interface %1. Status code is %2\r\n
0xb000c751 | Info-request is sent on the interface %1. Status code is %2\r\n
0xb000c752 | A valid reply is received for Info-request on the interface %1. Status code is %2\r\n
0xb000c753 | An invalid reply is received for Info-request on the interface %1. Status code is %2\r\n
0xb000c755 | An error occurred in creation of packet on the interface %1. Error code is %2\r\n
0xb000c756 | An error occurred in extracting options from the message received on the interface %1. Status code is %2\r\n
0xb000c757 | DHCP is changed from stateful to stateless mode on the interface %1. Status Code is %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c758 | DHCP is changed from stateless to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c759 | DHCP is changed from nondhcp to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c75a | DHCP is changed from nondhcp to stateless mode on the interface %1. Status Code is %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c75b | DHCP is converted to static mode on the interface %1. Status Code is %2.\r\n
0xb000c75c | Error occurred in parsing the DHCP message received on the interface id %1\r\n
0xb000c75d | Information refresh time option is received in the interface %1 with a refresh time value of %2\r\n
0xb000c75e | The information refresh time has expired, hence triggering a new inform packet on the interface %1.\r\n
0xb000c75f | Address %1 is plumbed on the interface %2. Status Code is %3.\r\n
0xb000c760 | Address %1 is unplumbed on the interface %2. Status Code is %3.\r\n
0xb000c763 | An interface is added whose interface index is %1. Status Code is %2.\r\n
0xb000c764 | An error occurred in initializing the interface %1. Status Code is %2.\r\n
0xb000c765 | An error occurred in plumbing the parameters into stack. Status Code is %1.\r\n
0xb000c768 | An error has occurred in opening the socket on the interface %1. Error Code is %2.\r\n
0xb000c769 | An error has occurred in closing the socket on the interface %1. Error Code is %2.\r\n
0xb000c76a | DNS registration has happened for the interface %1. Status Code is %2.DNS Flag settings is %3.\r\n
0xb000c76b | DNS deregistration has happened for the interface %1. Status Code is %2.\r\n
0xb000c772 | DHCP is changed from stateful to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c773 | Message is Invalid and it is discarded.\r\n
0xb000c774 | The Class ID %1 was set for the interface %3.\r\n
0xb000c775 | Address %1 being plumbed for adapter %2 already exists\r\n
0xb000c776 | Your computer was not assigned an address from the network (by the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb000c777 | Firewall port %1 is exempted on interface %2. Error code is %3.\r\n
0xb000c778 | Firewall port %1 is closed on interface %2. Error code is %3.\r\n
0xb000c779 | DHCP is changing mode to %2 on the interface %1.\r\n
0xb000c77a | Regular address acquisition will be done on interface %1 because aggressive address acquisition is turned ON.\r\n
0xb000c77b | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the DHCP IPv4 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c77c | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the static IPv4 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c77d | DHCP will not try regular IPv6 address acquisition on interface %1 since the machine is in Connected Standby state and the interface has the IPv4 address %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c77e | DHCP will try regular IPv6 address acquisition on interface %1 even though the machine is in Connected Standby state since the interface has no IPv4 or IPv6 address. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c781 | Firewall port %2 exemption triggered on interface %1.\r\n
0xb000c782 | Firewall port %2 close triggered on interface %1.\r\n
0xb000c783 | The DHCPv6 client received connected standby entry notification.\r\n
0xb000c784 | The DHCPv6 client received connected standby exit notification.\r\n
0xb000c785 | DHCP will try regular IPv6 address acquisition on interface %1 due to registry settings even though the machine is in Connected Standby state and the interface has an IPv4 address. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c786 | DHCP is enabled on the interface %1. Status code is %2.\r\n
0xb000c787 | DHCP is disabled on the interface %1. Status code is %2.\r\n
0xb000c788 | DHCP transaction will not be attempted on interface %1 because DHCP is disabled on it.\r\n
0xb000c789 | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the static IPv6 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c78a | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the stateless IPv6 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c78b | DHCP has cancelled IPv6 address acquisition on interface %1 because the interface is not multicast enabled.\r\n
0xb000ea60 | PERFTRACK (DHCPSOLICIT): Offer is accepted on the IPv6 interface %2. Offered Address is %3.\r\n
0xb000ea61 | PERFTRACK (DHCINFORMATIONREQUEST): Options received on the IPv6 interface %2. \r\n
0xb000ea62 | PERFTRACK (DHCPv6): Media Connect on interface %2\r\n
0xb000ea63 | PERFTRACK (DHCPv6): End of Media Connect on interface %2\r\n

### 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0

Message identifier | Message string
--- | ---
0x000003ec | Error occurred in stopping the Dhcpv6 client service. ErrorCode is %1.ShutDown Flag value is %2.\r\n
0x0000c766 | DHCPv6 client service is started\r\n
0x0000c767 | DHCPv6 client service is stopped. ShutDown Flag value is %1\r\n
0x10000031 | Response Time\r\n
0x3000000b | MediaConnect\r\n
0x3000000c | MediaDisconnect\r\n
0x3000000d | RAChanged\r\n
0x3000000e | PerfTrackMediaConnect\r\n
0x3000000f | PerfTrackMediaConnectEnd\r\n
0x30000010 | InterfaceAdded\r\n
0x30000011 | InitSARR\r\n
0x30000012 | InitConfirmReply\r\n
0x30000013 | SolicitSent\r\n
0x30000014 | AdvertiseReceived\r\n
0x30000015 | AdvertiseDiscarded\r\n
0x30000016 | RequestSent\r\n
0x30000017 | ReplyForRequestReceived\r\n
0x30000018 | InvalidReplyForRequestReceived\r\n
0x30000019 | RenewSent\r\n
0x3000001a | ReplyForRenewReceived\r\n
0x3000001b | InvalidReplyForRenewReceived\r\n
0x3000001c | RebindSent\r\n
0x3000001d | ReplyForRebindReceived\r\n
0x3000001e | InvalidReplyForRebindReceived\r\n
0x3000001f | ConfirmSent\r\n
0x30000020 | ReplyForConfirmReceived\r\n
0x30000021 | InvalidReplyForConfirmReceived\r\n
0x30000022 | DeclineSent\r\n
0x30000023 | ReplyForDeclineReceived\r\n
0x30000024 | InvalidReplyForDeclineReceived\r\n
0x30000025 | ReleaseSent\r\n
0x30000026 | InfoRequestSent\r\n
0x30000027 | ReplyForInfoRequestReceived\r\n
0x30000028 | InvalidReplyForInfoRequestReceived\r\n
0x3000002a | ErrorCreatingPacket\r\n
0x3000002b | ErrorExtractingOptions\r\n
0x3000002c | ErrorInParsing\r\n
0x3000002d | InformationRefreshTimeOptionReceived\r\n
0x3000002e | InformationRefreshTimeExpired\r\n
0x3000002f | PerfTrackSARR\r\n
0x30000030 | PerfTrackInfoRequest\r\n
0x30000031 | StatefulToStateless\r\n
0x30000032 | StatelessToStateful\r\n
0x30000033 | NonDhcpToStateful\r\n
0x30000034 | NonDhcpToStateless\r\n
0x30000035 | StaticMode\r\n
0x30000036 | AddressPlumbed\r\n
0x30000037 | AddressUnplumbed\r\n
0x30000038 | IPConflict\r\n
0x30000039 | LeaseExpired\r\n
0x3000003a | InitNetworkInterfaceFailed\r\n
0x3000003b | ErrorPlumbingParameters\r\n
0x3000003c | ErrorOpeningSocket\r\n
0x3000003d | ErrorClosingSocket\r\n
0x3000003e | ServiceStart\r\n
0x3000003f | ServiceStop\r\n
0x30000040 | ErrorInitService\r\n
0x30000041 | DnsRegistrationDone\r\n
0x30000042 | dnsDeregistrationDone\r\n
0x30000043 | ErrorInitializingInterface\r\n
0x30000044 | NetworkError\r\n
0x30000045 | StatefulToStateful\r\n
0x30000046 | InvalidMessageDiscarded\r\n
0x30000047 | AddressAlreadyExists\r\n
0x30000048 | LostIpAddress\r\n
0x30000049 | SetClassID\r\n
0x3000004a | FailedToObtainLease\r\n
0x3000004b | LeaseRenewalFailed\r\n
0x3000004c | ErrorServiceStop\r\n
0x3000004d | FirewallPortExempted\r\n
0x3000004e | FirewallPortClosed\r\n
0x3000004f | ModeChanging\r\n
0x30000050 | AggressiveRetryOn\r\n
0x30000051 | DontStartSolicitInCSSinceV4Plumbed\r\n
0x30000052 | StartSolicitInCSSinceV4Unplumbed\r\n
0x30000053 | AbandonSolicitInCSSinceDhcp\r\n
0x30000054 | StartSolicitInCSAtCompulsoryTime\r\n
0x30000055 | AcquireNICReference\r\n
0x30000056 | ReleaseNICReference\r\n
0x30000057 | FirewallPortExemptionTriggered\r\n
0x30000058 | FirewallPortCloseTriggered\r\n
0x30000059 | NotifyCSEntry\r\n
0x3000005a | NotifyCSExit\r\n
0x3000005b | AbandonSolicitInCSSinceStatic\r\n
0x3000005c | EnableDhcpV6\r\n
0x3000005d | DisableDhcpV6\r\n
0x3000005e | NoProcessingSinceDhcpV6Disabled\r\n
0x3000005f | AbandonSolicitInCSSinceV6Static\r\n
0x30000060 | AbandonSolicitInCSSinceV6Stateless\r\n
0x30000061 | AbandonSolicitSinceNonMulticast\r\n
0x30000062 | DHCPv6DUIDValidationFailed\r\n
0x30000063 | DHCPv6NetworkHintMatch\r\n
0x30000064 | DHCPv6NetworkHintStatefullConfig\r\n
0x30000065 | DHCPv6NetworkHintStatelessConfig\r\n
0x30000066 | DHCPv6NetworkHintConfigExpired\r\n
0x30000067 | NoteFlagValues\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Media State Event\r\n
0x70000002 | Protocol State Event\r\n
0x70000003 | Address Configuration State Event\r\n
0x70000004 | Service State Event\r\n
0x70000005 | Winsock State Event\r\n
0x70000006 | DNS State Event\r\n
0x70000007 | Network Parameter State Event\r\n
0x90000001 | Microsoft-Windows-DHCPv6-Client\r\n
0x90000002 | Microsoft-Windows-DHCPv6 Client Events/Admin\r\n
0x90000003 | Microsoft-Windows-DHCP Client Events/Operational\r\n
0x90000004 | System\r\n
0xb00003e8 | Your computer has lost the lease to its IP address %1 on the Network Card with network address %3.\r\n
0xb00003eb | Your computer was not able to renew its address from the network (from the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb00003ed | Your computer has detected that the IP address %1 for the Network Card with network address %3 is already in use on the network. Your computer will automatically attempt to obtain a different address.\r\n
0xb00003ee | Router Advertisement settings have been changed on the network adapter %1. The current M - Managed Address Configuration flag is %2 and the O - Other Stateful Configuration flag is %3. User Action: If you are seeing this event frequently, then it could be due to frequent change in M and O flag settings on the router in the network. Please contact your network administrator to have it resolved.\r\n
0xb00003f0 | An error occurred in initializing the interface. The error code is: %1.\r\n
0xb00003f1 | MAC Address %2 in DUID %4 could not be found in the system. Generated new DUID %8 based on MAC address %6.\r\n
0xb00003f2 | DHCPv6 has found SSID %1 in the cached networks for interface %4.\r\n
0xb00003f3 | DHCPv6 found a valid IPv6 address %1 and options in the cache for network SSID %2 under interface %4. DHCPv6 will use this cached configuration.\r\n
0xb00003f4 | DHCPv6 found options in the cache for network %1 under interface %4. DHCPv6 will use this cached configuration.\r\n
0xb00003f5 | DHCPv6 client found expired cached configuration for network %1 under interface %3. DHCPv6 client will discard the expired configuration and obtain new configuration from DHCPv6 server.\r\n
0xb000c389 | A network error occurred when trying to send a message. The error code is: %1.\r\n
0xb000c397 | Attempting to acquire a reference for interface %1. Error code is %2.\r\n
0xb000c398 | Attempting to release the reference for interface %1. Error code is %2.\r\n
0xb000c739 | Media Connect notification has been received on interface with interface id %1\r\n
0xb000c73a | Media Disconnect notification has been received on interface with interface id %1\r\n
0xb000c73c | Confirm-Reply is initiated on the interface with Interface Id %1\r\n
0xb000c73d | Solicit-Advertise-Request-Reply is initiated on the interface with Interface Id %1. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c73e | Solicit is sent from the interface %1. Status code is %2\r\n
0xb000c73f | Advertise is received from the interface %1. Status code is %2. Offered Address is %3\r\n
0xb000c740 | Advertise is discarded from the interface %1. Status code is %2\r\n
0xb000c741 | Request is sent from the interface %1. Status code is %2\r\n
0xb000c742 | A valid reply is received for request from the interface %1. Status code is %2. Received address is %3\r\n
0xb000c743 | Incorrect reply is received for request from the interface %1. Status code is %2\r\n
0xb000c744 | Renew is sent on the interface %1. Status code is %2\r\n
0xb000c745 | A valid reply is received for renew from the interface %1. Status code is %2\r\n
0xb000c746 | An invalid reply is received for renew from the interface %1. Status code is %2\r\n
0xb000c747 | Rebind is sent on the interface %1. Status code is %2\r\n
0xb000c748 | A valid reply is received for rebind from the interface %1. Status code is %2\r\n
0xb000c749 | An invalid reply is received for rebind from the interface %1. Status code is %2\r\n
0xb000c74a | Release is sent on the interface %1. Status code is %2\r\n
0xb000c74b | Decline is sent on the interface %1. Status code is %2\r\n
0xb000c74c | A valid reply is received for decline on the interface %1. Status code is %2\r\n
0xb000c74d | An invalid reply is received for decline on the interface %1. Status code is %2\r\n
0xb000c74e | Confirm is sent on the interface %1. Status code is %2\r\n
0xb000c74f | A valid reply is received for confirm on the interface %1. Status code is %2\r\n
0xb000c750 | An invalid reply is received for confirm on the interface %1. Status code is %2\r\n
0xb000c751 | Info-request is sent on the interface %1. Status code is %2\r\n
0xb000c752 | A valid reply is received for Info-request on the interface %1. Status code is %2\r\n
0xb000c753 | An invalid reply is received for Info-request on the interface %1. Status code is %2\r\n
0xb000c755 | An error occurred in creation of packet on the interface %1. Error code is %2\r\n
0xb000c756 | An error occurred in extracting options from the message received on the interface %1. Status code is %2\r\n
0xb000c757 | DHCP is changed from stateful to stateless mode on the interface %1. Status Code is %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c758 | DHCP is changed from stateless to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c759 | DHCP is changed from nondhcp to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c75a | DHCP is changed from nondhcp to stateless mode on the interface %1. Status Code is %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c75b | DHCP is converted to static mode on the interface %1. Status Code is %2.\r\n
0xb000c75c | Error occurred in parsing the DHCP message received on the interface id %1\r\n
0xb000c75d | Information refresh time option is received in the interface %1 with a refresh time value of %2\r\n
0xb000c75e | The information refresh time has expired, hence triggering a new inform packet on the interface %1.\r\n
0xb000c75f | Address %1 is plumbed on the interface %2. Status Code is %3.\r\n
0xb000c760 | Address %1 is unplumbed on the interface %2. Status Code is %3.\r\n
0xb000c763 | An interface is added whose interface index is %1. Status Code is %2.\r\n
0xb000c764 | An error occurred in initializing the interface %1. Status Code is %2.\r\n
0xb000c765 | An error occurred in plumbing the parameters into stack. Status Code is %1.\r\n
0xb000c768 | An error has occurred in opening the socket on the interface %1. Error Code is %2.\r\n
0xb000c769 | An error has occurred in closing the socket on the interface %1. Error Code is %2.\r\n
0xb000c76a | DNS registration has happened for the interface %1. Status Code is %2.DNS Flag settings is %3.\r\n
0xb000c76b | DNS deregistration has happened for the interface %1. Status Code is %2.\r\n
0xb000c772 | DHCP is changed from stateful to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c773 | Message is Invalid and it is discarded.\r\n
0xb000c774 | The Class ID %1 was set for the interface %3.\r\n
0xb000c775 | Address %1 being plumbed for adapter %2 already exists\r\n
0xb000c776 | Your computer was not assigned an address from the network (by the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb000c777 | Firewall port %1 is exempted on interface %2. Error code is %3.\r\n
0xb000c778 | Firewall port %1 is closed on interface %2. Error code is %3.\r\n
0xb000c779 | DHCP is changing mode to %2 on the interface %1.\r\n
0xb000c77a | Regular address acquisition will be done on interface %1 because aggressive address acquisition is turned ON.\r\n
0xb000c77b | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the DHCP IPv4 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c77c | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the static IPv4 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c77d | DHCP will not try regular IPv6 address acquisition on interface %1 since the machine is in Connected Standby state and the interface has the IPv4 address %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c77e | DHCP will try regular IPv6 address acquisition on interface %1 even though the machine is in Connected Standby state since the interface has no IPv4 or IPv6 address. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c781 | Firewall port %2 exemption triggered on interface %1.\r\n
0xb000c782 | Firewall port %2 close triggered on interface %1.\r\n
0xb000c783 | The DHCPv6 client received connected standby entry notification.\r\n
0xb000c784 | The DHCPv6 client received connected standby exit notification.\r\n
0xb000c785 | DHCP will try regular IPv6 address acquisition on interface %1 due to registry settings even though the machine is in Connected Standby state and the interface has an IPv4 address. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c786 | DHCP is enabled on the interface %1. Status code is %2.\r\n
0xb000c787 | DHCP is disabled on the interface %1. Status code is %2.\r\n
0xb000c788 | DHCP transaction will not be attempted on interface %1 because DHCP is disabled on it.\r\n
0xb000c789 | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the static IPv6 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c78a | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the stateless IPv6 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c78b | DHCP has cancelled IPv6 address acquisition on interface %1 because the interface is not multicast enabled.\r\n
0xb000c78c | The values of flags received on interface %1 are: Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000ea60 | PERFTRACK (DHCPSOLICIT): Offer is accepted on the IPv6 interface %2. Offered Address is %3.\r\n
0xb000ea61 | PERFTRACK (DHCINFORMATIONREQUEST): Options received on the IPv6 interface %2. \r\n
0xb000ea62 | PERFTRACK (DHCPv6): Media Connect on interface %2\r\n
0xb000ea63 | PERFTRACK (DHCPv6): End of Media Connect on interface %2\r\n

### 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x000003ec | Error occurred in stopping the Dhcpv6 client service. ErrorCode is %1.ShutDown Flag value is %2.\r\n
0x0000c766 | DHCPv6 client service is started\r\n
0x0000c767 | DHCPv6 client service is stopped. ShutDown Flag value is %1\r\n
0x0000c771 | DHCPv6 client service stop is almost done.DHCP Context Ref count is %1\r\n
0x10000031 | Response Time\r\n
0x3000000b | MediaConnect\r\n
0x3000000c | MediaDisconnect\r\n
0x3000000d | RAChanged\r\n
0x3000000e | PerfTrackMediaConnect\r\n
0x3000000f | PerfTrackMediaConnectEnd\r\n
0x30000010 | InterfaceAdded\r\n
0x30000011 | InitSARR\r\n
0x30000012 | InitConfirmReply\r\n
0x30000013 | SolicitSent\r\n
0x30000014 | AdvertiseReceived\r\n
0x30000015 | AdvertiseDiscarded\r\n
0x30000016 | RequestSent\r\n
0x30000017 | ReplyForRequestReceived\r\n
0x30000018 | InvalidReplyForRequestReceived\r\n
0x30000019 | RenewSent\r\n
0x3000001a | ReplyForRenewReceived\r\n
0x3000001b | InvalidReplyForRenewReceived\r\n
0x3000001c | RebindSent\r\n
0x3000001d | ReplyForRebindReceived\r\n
0x3000001e | InvalidReplyForRebindReceived\r\n
0x3000001f | ConfirmSent\r\n
0x30000020 | ReplyForConfirmReceived\r\n
0x30000021 | InvalidReplyForConfirmReceived\r\n
0x30000022 | DeclineSent\r\n
0x30000023 | ReplyForDeclineReceived\r\n
0x30000024 | InvalidReplyForDeclineReceived\r\n
0x30000025 | ReleaseSent\r\n
0x30000026 | InfoRequestSent\r\n
0x30000027 | ReplyForInfoRequestReceived\r\n
0x30000028 | InvalidReplyForInfoRequestReceived\r\n
0x3000002a | ErrorCreatingPacket\r\n
0x3000002b | ErrorExtractingOptions\r\n
0x3000002c | ErrorInParsing\r\n
0x3000002d | InformationRefreshTimeOptionReceived\r\n
0x3000002e | InformationRefreshTimeExpired\r\n
0x3000002f | PerfTrackSARR\r\n
0x30000030 | PerfTrackInfoRequest\r\n
0x30000031 | StatefulToStateless\r\n
0x30000032 | StatelessToStateful\r\n
0x30000033 | NonDhcpToStateful\r\n
0x30000034 | NonDhcpToStateless\r\n
0x30000035 | StaticMode\r\n
0x30000036 | AddressPlumbed\r\n
0x30000037 | AddressUnplumbed\r\n
0x30000038 | IPConflict\r\n
0x30000039 | LeaseExpired\r\n
0x3000003a | InitNetworkInterfaceFailed\r\n
0x3000003b | ErrorPlumbingParameters\r\n
0x3000003c | ErrorOpeningSocket\r\n
0x3000003d | ErrorClosingSocket\r\n
0x3000003e | ServiceStart\r\n
0x3000003f | ServiceStop\r\n
0x30000040 | ErrorInitService\r\n
0x30000041 | DnsRegistrationDone\r\n
0x30000042 | dnsDeregistrationDone\r\n
0x30000043 | ErrorInitializingInterface\r\n
0x30000044 | NetworkError\r\n
0x30000045 | StatefulToStateful\r\n
0x30000046 | InvalidMessageDiscarded\r\n
0x30000047 | AddressAlreadyExists\r\n
0x30000048 | LostIpAddress\r\n
0x30000049 | SetClassID\r\n
0x3000004a | FailedToObtainLease\r\n
0x3000004b | LeaseRenewalFailed\r\n
0x3000004c | ErrorServiceStop\r\n
0x3000004d | FirewallPortExempted\r\n
0x3000004e | FirewallPortClosed\r\n
0x3000004f | ModeChanging\r\n
0x30000050 | AggressiveRetryOn\r\n
0x30000051 | DontStartSolicitInCSSinceV4Plumbed\r\n
0x30000052 | StartSolicitInCSSinceV4Unplumbed\r\n
0x30000053 | AbandonSolicitInCSSinceDhcp\r\n
0x30000054 | StartSolicitInCSAtCompulsoryTime\r\n
0x30000055 | AcquireNICReference\r\n
0x30000056 | ReleaseNICReference\r\n
0x30000057 | FirewallPortExemptionTriggered\r\n
0x30000058 | FirewallPortCloseTriggered\r\n
0x30000059 | NotifyCSEntry\r\n
0x3000005a | NotifyCSExit\r\n
0x3000005b | AbandonSolicitInCSSinceStatic\r\n
0x3000005c | EnableDhcpV6\r\n
0x3000005d | DisableDhcpV6\r\n
0x3000005e | NoProcessingSinceDhcpV6Disabled\r\n
0x3000005f | AbandonSolicitInCSSinceV6Static\r\n
0x30000060 | AbandonSolicitInCSSinceV6Stateless\r\n
0x30000061 | AbandonSolicitSinceNonMulticast\r\n
0x30000062 | DHCPv6DUIDValidationFailed\r\n
0x30000063 | DHCPv6NetworkHintMatch\r\n
0x30000064 | DHCPv6NetworkHintStatefullConfig\r\n
0x30000065 | DHCPv6NetworkHintStatelessConfig\r\n
0x30000066 | DHCPv6NetworkHintConfigExpired\r\n
0x30000067 | NoteFlagValues\r\n
0x30000068 | ServiceStopWithRefCount\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Media State Event\r\n
0x70000002 | Protocol State Event\r\n
0x70000003 | Address Configuration State Event\r\n
0x70000004 | Service State Event\r\n
0x70000005 | Winsock State Event\r\n
0x70000006 | DNS State Event\r\n
0x70000007 | Network Parameter State Event\r\n
0x90000001 | Microsoft-Windows-DHCPv6-Client\r\n
0x90000002 | Microsoft-Windows-DHCPv6 Client Events/Admin\r\n
0x90000003 | Microsoft-Windows-DHCP Client Events/Operational\r\n
0x90000004 | System\r\n
0xb00003e8 | Your computer has lost the lease to its IP address %1 on the Network Card with network address %3.\r\n
0xb00003eb | Your computer was not able to renew its address from the network (from the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb00003ed | Your computer has detected that the IP address %1 for the Network Card with network address %3 is already in use on the network. Your computer will automatically attempt to obtain a different address.\r\n
0xb00003ee | Router Advertisement settings have been changed on the network adapter %1. The current M - Managed Address Configuration flag is %2 and the O - Other Stateful Configuration flag is %3. User Action: If you are seeing this event frequently, then it could be due to frequent change in M and O flag settings on the router in the network. Please contact your network administrator to have it resolved.\r\n
0xb00003f0 | An error occurred in initializing the interface. The error code is: %1.\r\n
0xb00003f1 | MAC Address %2 in DUID %4 could not be found in the system. Generated new DUID %8 based on MAC address %6.\r\n
0xb00003f2 | DHCPv6 has found SSID %1 in the cached networks for interface %4.\r\n
0xb00003f3 | DHCPv6 found a valid IPv6 address %1 and options in the cache for network SSID %2 under interface %4. DHCPv6 will use this cached configuration.\r\n
0xb00003f4 | DHCPv6 found options in the cache for network %1 under interface %4. DHCPv6 will use this cached configuration.\r\n
0xb00003f5 | DHCPv6 client found expired cached configuration for network %1 under interface %3. DHCPv6 client will discard the expired configuration and obtain new configuration from DHCPv6 server.\r\n
0xb000c389 | A network error occurred when trying to send a message. The error code is: %1.\r\n
0xb000c397 | Attempting to acquire a reference for interface %1. Error code is %2.\r\n
0xb000c398 | Attempting to release the reference for interface %1. Error code is %2.\r\n
0xb000c739 | Media Connect notification has been received on interface with interface id %1\r\n
0xb000c73a | Media Disconnect notification has been received on interface with interface id %1\r\n
0xb000c73c | Confirm-Reply is initiated on the interface with Interface Id %1\r\n
0xb000c73d | Solicit-Advertise-Request-Reply is initiated on the interface with Interface Id %1. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c73e | Solicit is sent from the interface %1. Status code is %2\r\n
0xb000c73f | Advertise is received from the interface %1. Status code is %2. Offered Address is %3\r\n
0xb000c740 | Advertise is discarded from the interface %1. Status code is %2\r\n
0xb000c741 | Request is sent from the interface %1. Status code is %2\r\n
0xb000c742 | A valid reply is received for request from the interface %1. Status code is %2. Received address is %3\r\n
0xb000c743 | Incorrect reply is received for request from the interface %1. Status code is %2\r\n
0xb000c744 | Renew is sent on the interface %1. Status code is %2\r\n
0xb000c745 | A valid reply is received for renew from the interface %1. Status code is %2\r\n
0xb000c746 | An invalid reply is received for renew from the interface %1. Status code is %2\r\n
0xb000c747 | Rebind is sent on the interface %1. Status code is %2\r\n
0xb000c748 | A valid reply is received for rebind from the interface %1. Status code is %2\r\n
0xb000c749 | An invalid reply is received for rebind from the interface %1. Status code is %2\r\n
0xb000c74a | Release is sent on the interface %1. Status code is %2\r\n
0xb000c74b | Decline is sent on the interface %1. Status code is %2\r\n
0xb000c74c | A valid reply is received for decline on the interface %1. Status code is %2\r\n
0xb000c74d | An invalid reply is received for decline on the interface %1. Status code is %2\r\n
0xb000c74e | Confirm is sent on the interface %1. Status code is %2\r\n
0xb000c74f | A valid reply is received for confirm on the interface %1. Status code is %2\r\n
0xb000c750 | An invalid reply is received for confirm on the interface %1. Status code is %2\r\n
0xb000c751 | Info-request is sent on the interface %1. Status code is %2\r\n
0xb000c752 | A valid reply is received for Info-request on the interface %1. Status code is %2\r\n
0xb000c753 | An invalid reply is received for Info-request on the interface %1. Status code is %2\r\n
0xb000c755 | An error occurred in creation of packet on the interface %1. Error code is %2\r\n
0xb000c756 | An error occurred in extracting options from the message received on the interface %1. Status code is %2\r\n
0xb000c757 | DHCP is changed from stateful to stateless mode on the interface %1. Status Code is %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c758 | DHCP is changed from stateless to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c759 | DHCP is changed from nondhcp to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c75a | DHCP is changed from nondhcp to stateless mode on the interface %1. Status Code is %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c75b | DHCP is converted to static mode on the interface %1. Status Code is %2.\r\n
0xb000c75c | Error occurred in parsing the DHCP message received on the interface id %1\r\n
0xb000c75d | Information refresh time option is received in the interface %1 with a refresh time value of %2\r\n
0xb000c75e | The information refresh time has expired, hence triggering a new inform packet on the interface %1.\r\n
0xb000c75f | Address %1 is plumbed on the interface %2. Status Code is %3.\r\n
0xb000c760 | Address %1 is unplumbed on the interface %2. Status Code is %3.\r\n
0xb000c763 | An interface is added whose interface index is %1. Status Code is %2.\r\n
0xb000c764 | An error occurred in initializing the interface %1. Status Code is %2.\r\n
0xb000c765 | An error occurred in plumbing the parameters into stack. Status Code is %1.\r\n
0xb000c768 | An error has occurred in opening the socket on the interface %1. Error Code is %2.\r\n
0xb000c769 | An error has occurred in closing the socket on the interface %1. Error Code is %2.\r\n
0xb000c76a | DNS registration has happened for the interface %1. Status Code is %2.DNS Flag settings is %3.\r\n
0xb000c76b | DNS deregistration has happened for the interface %1. Status Code is %2.\r\n
0xb000c772 | DHCP is changed from stateful to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c773 | Message is Invalid and it is discarded.\r\n
0xb000c774 | The Class ID %1 was set for the interface %3.\r\n
0xb000c775 | Address %1 being plumbed for adapter %2 already exists\r\n
0xb000c776 | Your computer was not assigned an address from the network (by the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb000c777 | Firewall port %1 is exempted on interface %2. Error code is %3.\r\n
0xb000c778 | Firewall port %1 is closed on interface %2. Error code is %3.\r\n
0xb000c779 | DHCP is changing mode to %2 on the interface %1.\r\n
0xb000c77a | Regular address acquisition will be done on interface %1 because aggressive address acquisition is turned ON.\r\n
0xb000c77b | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the DHCP IPv4 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c77c | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the static IPv4 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c77d | DHCP will not try regular IPv6 address acquisition on interface %1 since the machine is in Connected Standby state and the interface has the IPv4 address %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c77e | DHCP will try regular IPv6 address acquisition on interface %1 even though the machine is in Connected Standby state since the interface has no IPv4 or IPv6 address. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c781 | Firewall port %2 exemption triggered on interface %1.\r\n
0xb000c782 | Firewall port %2 close triggered on interface %1.\r\n
0xb000c783 | The DHCPv6 client received connected standby entry notification.\r\n
0xb000c784 | The DHCPv6 client received connected standby exit notification.\r\n
0xb000c785 | DHCP will try regular IPv6 address acquisition on interface %1 due to registry settings even though the machine is in Connected Standby state and the interface has an IPv4 address. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c786 | DHCP is enabled on the interface %1. Status code is %2.\r\n
0xb000c787 | DHCP is disabled on the interface %1. Status code is %2.\r\n
0xb000c788 | DHCP transaction will not be attempted on interface %1 because DHCP is disabled on it.\r\n
0xb000c789 | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the static IPv6 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c78a | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the stateless IPv6 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c78b | DHCP has cancelled IPv6 address acquisition on interface %1 because the interface is not multicast enabled.\r\n
0xb000c78c | The values of flags received on interface %1 are: Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000ea60 | PERFTRACK (DHCPSOLICIT): Offer is accepted on the IPv6 interface %2. Offered Address is %3.\r\n
0xb000ea61 | PERFTRACK (DHCINFORMATIONREQUEST): Options received on the IPv6 interface %2. \r\n
0xb000ea62 | PERFTRACK (DHCPv6): Media Connect on interface %2\r\n
0xb000ea63 | PERFTRACK (DHCPv6): End of Media Connect on interface %2\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x000003ec | Error occurred in stopping the Dhcpv6 client service. ErrorCode is %1. ShutDown Flag value is %2.\r\n
0x0000c766 | DHCPv6 client service is started\r\n
0x0000c767 | DHCPv6 client service is stopped. ShutDown Flag value is %1\r\n
0x0000c771 | DHCPv6 client service stop is almost done.DHCP Context Ref count is %1\r\n
0x10000031 | Response Time\r\n
0x3000000b | MediaConnect\r\n
0x3000000c | MediaDisconnect\r\n
0x3000000d | RAChanged\r\n
0x3000000e | PerfTrackMediaConnect\r\n
0x3000000f | PerfTrackMediaConnectEnd\r\n
0x30000010 | InterfaceAdded\r\n
0x30000011 | InitSARR\r\n
0x30000012 | InitConfirmReply\r\n
0x30000013 | SolicitSent\r\n
0x30000014 | AdvertiseReceived\r\n
0x30000015 | AdvertiseDiscarded\r\n
0x30000016 | RequestSent\r\n
0x30000017 | ReplyForRequestReceived\r\n
0x30000018 | InvalidReplyForRequestReceived\r\n
0x30000019 | RenewSent\r\n
0x3000001a | ReplyForRenewReceived\r\n
0x3000001b | InvalidReplyForRenewReceived\r\n
0x3000001c | RebindSent\r\n
0x3000001d | ReplyForRebindReceived\r\n
0x3000001e | InvalidReplyForRebindReceived\r\n
0x3000001f | ConfirmSent\r\n
0x30000020 | ReplyForConfirmReceived\r\n
0x30000021 | InvalidReplyForConfirmReceived\r\n
0x30000022 | DeclineSent\r\n
0x30000023 | ReplyForDeclineReceived\r\n
0x30000024 | InvalidReplyForDeclineReceived\r\n
0x30000025 | ReleaseSent\r\n
0x30000026 | InfoRequestSent\r\n
0x30000027 | ReplyForInfoRequestReceived\r\n
0x30000028 | InvalidReplyForInfoRequestReceived\r\n
0x3000002a | ErrorCreatingPacket\r\n
0x3000002b | ErrorExtractingOptions\r\n
0x3000002c | ErrorInParsing\r\n
0x3000002d | InformationRefreshTimeOptionReceived\r\n
0x3000002e | InformationRefreshTimeExpired\r\n
0x3000002f | PerfTrackSARR\r\n
0x30000030 | PerfTrackInfoRequest\r\n
0x30000031 | StatefulToStateless\r\n
0x30000032 | StatelessToStateful\r\n
0x30000033 | NonDhcpToStateful\r\n
0x30000034 | NonDhcpToStateless\r\n
0x30000035 | StaticMode\r\n
0x30000036 | AddressPlumbed\r\n
0x30000037 | AddressUnplumbed\r\n
0x30000038 | IPConflict\r\n
0x30000039 | LeaseExpired\r\n
0x3000003a | InitNetworkInterfaceFailed\r\n
0x3000003b | ErrorPlumbingParameters\r\n
0x3000003c | ErrorOpeningSocket\r\n
0x3000003d | ErrorClosingSocket\r\n
0x3000003e | ServiceStart\r\n
0x3000003f | ServiceStop\r\n
0x30000040 | ErrorInitService\r\n
0x30000041 | DnsRegistrationDone\r\n
0x30000042 | dnsDeregistrationDone\r\n
0x30000043 | ErrorInitializingInterface\r\n
0x30000044 | NetworkError\r\n
0x30000045 | StatefulToStateful\r\n
0x30000046 | InvalidMessageDiscarded\r\n
0x30000047 | AddressAlreadyExists\r\n
0x30000048 | LostIpAddress\r\n
0x30000049 | SetClassID\r\n
0x3000004a | FailedToObtainLease\r\n
0x3000004b | LeaseRenewalFailed\r\n
0x3000004c | ErrorServiceStop\r\n
0x3000004d | FirewallPortExempted\r\n
0x3000004e | FirewallPortClosed\r\n
0x3000004f | ModeChanging\r\n
0x30000050 | AggressiveRetryOn\r\n
0x30000051 | DontStartSolicitInCSSinceV4Plumbed\r\n
0x30000052 | StartSolicitInCSSinceV4Unplumbed\r\n
0x30000053 | AbandonSolicitInCSSinceDhcp\r\n
0x30000054 | StartSolicitInCSAtCompulsoryTime\r\n
0x30000055 | AcquireNICReference\r\n
0x30000056 | ReleaseNICReference\r\n
0x30000057 | FirewallPortExemptionTriggered\r\n
0x30000058 | FirewallPortCloseTriggered\r\n
0x30000059 | NotifyCSEntry\r\n
0x3000005a | NotifyCSExit\r\n
0x3000005b | AbandonSolicitInCSSinceStatic\r\n
0x3000005c | EnableDhcpV6\r\n
0x3000005d | DisableDhcpV6\r\n
0x3000005e | NoProcessingSinceDhcpV6Disabled\r\n
0x3000005f | AbandonSolicitInCSSinceV6Static\r\n
0x30000060 | AbandonSolicitInCSSinceV6Stateless\r\n
0x30000061 | AbandonSolicitSinceNonMulticast\r\n
0x30000062 | DHCPv6DUIDValidationFailed\r\n
0x30000063 | DHCPv6NetworkHintMatch\r\n
0x30000064 | DHCPv6NetworkHintStatefullConfig\r\n
0x30000065 | DHCPv6NetworkHintStatelessConfig\r\n
0x30000066 | DHCPv6NetworkHintConfigExpired\r\n
0x30000067 | NoteFlagValues\r\n
0x30000068 | ServiceStopWithRefCount\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Media State Event\r\n
0x70000002 | Protocol State Event\r\n
0x70000003 | Address Configuration State Event\r\n
0x70000004 | Service State Event\r\n
0x70000005 | Winsock State Event\r\n
0x70000006 | DNS State Event\r\n
0x70000007 | Network Parameter State Event\r\n
0x90000001 | Microsoft-Windows-DHCPv6-Client\r\n
0x90000002 | Microsoft-Windows-DHCPv6 Client Events/Admin\r\n
0x90000003 | Microsoft-Windows-DHCP Client Events/Operational\r\n
0x90000004 | System\r\n
0xb00003e8 | Your computer has lost the lease to its IP address %1 on the Network Card with network address %3.\r\n
0xb00003eb | Your computer was not able to renew its address from the network (from the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb00003ed | Your computer has detected that the IP address %1 for the Network Card with network address %3 is already in use on the network. Your computer will automatically attempt to obtain a different address.\r\n
0xb00003ee | Router Advertisement settings have been changed on the network adapter %1. The current M - Managed Address Configuration flag is %2 and the O - Other Stateful Configuration flag is %3. User Action: If you are seeing this event frequently, then it could be due to frequent change in M and O flag settings on the router in the network. Please contact your network administrator to have it resolved.\r\n
0xb00003f0 | An error occurred in initializing the interface. The error code is: %1.\r\n
0xb00003f1 | MAC Address %2 in DUID %4 could not be found in the system. Generated new DUID %8 based on MAC address %6.\r\n
0xb00003f2 | DHCPv6 has found SSID %1 in the cached networks for interface %4.\r\n
0xb00003f3 | DHCPv6 found a valid IPv6 address %1 and options in the cache for network SSID %2 under interface %4. DHCPv6 will use this cached configuration.\r\n
0xb00003f4 | DHCPv6 found options in the cache for network %1 under interface %4. DHCPv6 will use this cached configuration.\r\n
0xb00003f5 | DHCPv6 client found expired cached configuration for network %1 under interface %3. DHCPv6 client will discard the expired configuration and obtain new configuration from DHCPv6 server.\r\n
0xb00003f6 | IPv6 Address is unplumbed, Interface %1 uninitialized.\r\n
0xb00003f7 | Failed to Unplumb IPv6 Address %1. ErrorCode is %2.\r\n
0xb00003f8 | Failed to Update Registry %1. ErrorCode is %2.\r\n
0xb00003f9 | Unable to register with DNS %1. ErrorCode is %2.\r\n
0xb00003fa | Trying to Add or Update %1 on %2.\r\n
0xb00003fb | Address Conflict Detected for RAS.\r\n
0xb00003fc | Number of requests in queue are above LONG_MAX. AdapterName is %1.\r\n
0xb00003fd | Error in creating renewal thread. ErrorCode is %1.\r\n
0xb00003fe | Error in forever request thread. ErrorCode is %1.\r\n
0xb00003ff | Error in Media Connected. ErrorCode is %1.\r\n
0xb0000400 | Media Disconnected on %1.\r\n
0xb0000401 | MEDIA DISCONNECT: Someone still using context. So not destroying the context\r\n
0xb0000402 | Error Media Disconnected. ErrorCode is %1.\r\n
0xb0000403 | FAILED TO PLUMB %1 in %2. ErrorCode is %3\r\n
0xb0000404 | Lease Acquisition Success in %1.\r\n
0xb0000405 | Event NACK Lease in %1. Error is RESOURCE_NOT_AVAILABLE.\r\n
0xb0000406 | Failed to release IPV6 Address on %1.\r\n
0xb0000407 | Error in getting interface metric. Error code is %1.\r\n
0xb0000408 | Error in enumerating hardware address. Error code is %1.\r\n
0xb0000409 | Unable to get Link characteristics. Error code is %1.\r\n
0xb000040a | Error in adding Ipv6 Address %1. Error code is %2.\r\n
0xb000040b | Successfully deleted Ipv6 Address %1.\r\n
0xb000040c | Error in deleting Ipv6 Address %1. Error code is %2.\r\n
0xb000040d | Error in updating Ipv6 Address. Error code is %1.\r\n
0xb000040e | Error in enumerating Interface. Error code is %1.\r\n
0xb000040f | Error in Querying for RA Settings. Error code is %1.\r\n
0xb0000410 | Error in Callback of Media Sense. Error code is %1.\r\n
0xb0000411 | Error in initializing Media Sense. Error code is %1.\r\n
0xb0000412 | Error in getting static parameters from stack. Error code is %1.\r\n
0xb0000413 | Error in getting All parameters from stack. Error code is %1.\r\n
0xb0000414 | Error in querying DNS config for Adapter %1. ErrorCode is %2.\r\n
0xb0000415 | Error in Registering Address with DNS %1. ErrorCode is %2.\r\n
0xb0000416 | Error in Deregistering Address with DNS %1. ErrorCode is %2.\r\n
0xb0000417 | Error in DynDnsRegister Adapter %1. ErrorCode is %2.\r\n
0xb000c389 | A network error occurred when trying to send a message. The error code is: %1.\r\n
0xb000c397 | Attempting to acquire a reference for interface %1. Error code is %2.\r\n
0xb000c398 | Attempting to release the reference for interface %1. Error code is %2.\r\n
0xb000c739 | Media Connect notification has been received on interface with interface id %1\r\n
0xb000c73a | Media Disconnect notification has been received on interface with interface id %1\r\n
0xb000c73c | Confirm-Reply is initiated on the interface with Interface Id %1\r\n
0xb000c73d | Solicit-Advertise-Request-Reply is initiated on the interface with Interface Id %1. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c73e | Solicit is sent from the interface %1. Status code is %2\r\n
0xb000c73f | Advertise is received from the interface %1. Status code is %2. Offered Address is %3\r\n
0xb000c740 | Advertise is discarded from the interface %1. Status code is %2\r\n
0xb000c741 | Request is sent from the interface %1. Status code is %2\r\n
0xb000c742 | A valid reply is received for request from the interface %1. Status code is %2. Received address is %3\r\n
0xb000c743 | Incorrect reply is received for request from the interface %1. Status code is %2\r\n
0xb000c744 | Renew is sent on the interface %1. Status code is %2\r\n
0xb000c745 | A valid reply is received for renew from the interface %1. Status code is %2\r\n
0xb000c746 | An invalid reply is received for renew from the interface %1. Status code is %2\r\n
0xb000c747 | Rebind is sent on the interface %1. Status code is %2\r\n
0xb000c748 | A valid reply is received for rebind from the interface %1. Status code is %2\r\n
0xb000c749 | An invalid reply is received for rebind from the interface %1. Status code is %2\r\n
0xb000c74a | Release is sent on the interface %1. Status code is %2\r\n
0xb000c74b | Decline is sent on the interface %1. Status code is %2\r\n
0xb000c74c | A valid reply is received for decline on the interface %1. Status code is %2\r\n
0xb000c74d | An invalid reply is received for decline on the interface %1. Status code is %2\r\n
0xb000c74e | Confirm is sent on the interface %1. Status code is %2\r\n
0xb000c74f | A valid reply is received for confirm on the interface %1. Status code is %2\r\n
0xb000c750 | An invalid reply is received for confirm on the interface %1. Status code is %2\r\n
0xb000c751 | Info-request is sent on the interface %1. Status code is %2\r\n
0xb000c752 | A valid reply is received for Info-request on the interface %1. Status code is %2\r\n
0xb000c753 | An invalid reply is received for Info-request on the interface %1. Status code is %2\r\n
0xb000c755 | An error occurred in creation of packet on the interface %1. Error code is %2\r\n
0xb000c756 | An error occurred in extracting options from the message received on the interface %1. Status code is %2\r\n
0xb000c757 | DHCP is changed from stateful to stateless mode on the interface %1. Status Code is %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c758 | DHCP is changed from stateless to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c759 | DHCP is changed from nondhcp to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c75a | DHCP is changed from nondhcp to stateless mode on the interface %1. Status Code is %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c75b | DHCP is converted to static mode on the interface %1. Status Code is %2.\r\n
0xb000c75c | Error occurred in parsing the DHCP message received on the interface id %1\r\n
0xb000c75d | Information refresh time option is received in the interface %1 with a refresh time value of %2\r\n
0xb000c75e | The information refresh time has expired, hence triggering a new inform packet on the interface %1.\r\n
0xb000c75f | Address %1 is plumbed on the interface %2. Status Code is %3.\r\n
0xb000c760 | Address %1 is unplumbed on the interface %2. Status Code is %3.\r\n
0xb000c763 | An interface is added whose interface index is %1. Status Code is %2.\r\n
0xb000c764 | An error occurred in initializing the interface %1. Status Code is %2.\r\n
0xb000c765 | An error occurred in plumbing the parameters into stack. Status Code is %1.\r\n
0xb000c768 | An error has occurred in opening the socket on the interface %1. Error Code is %2.\r\n
0xb000c769 | An error has occurred in closing the socket on the interface %1. Error Code is %2.\r\n
0xb000c76a | DNS registration has happened for the interface %1. Status Code is %2. DNS Flag settings is %3.\r\n
0xb000c76b | DNS deregistration has happened for the interface %1. Status Code is %2.\r\n
0xb000c772 | DHCP is changed from stateful to stateful mode on the interface %1. Status Code is %2.\r\n
0xb000c773 | Message is Invalid and it is discarded.\r\n
0xb000c774 | The Class ID %1 was set for the interface %3.\r\n
0xb000c775 | Address %1 being plumbed for adapter %2 already exists\r\n
0xb000c776 | Your computer was not assigned an address from the network (by the DHCP Server) for the Network Card with network address %2.  The following error occurred: %3. Your computer will continue to try and obtain an address on its own from the network address (DHCP) server.\r\n
0xb000c777 | Firewall port %1 is exempted on interface %2. Error code is %3.\r\n
0xb000c778 | Firewall port %1 is closed on interface %2. Error code is %3.\r\n
0xb000c779 | DHCP is changing mode to %2 on the interface %1.\r\n
0xb000c77a | Regular address acquisition will be done on interface %1 because aggressive address acquisition is turned ON.\r\n
0xb000c77b | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the DHCP IPv4 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c77c | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the static IPv4 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c77d | DHCP will not try regular IPv6 address acquisition on interface %1 since the machine is in Connected Standby state and the interface has the IPv4 address %2. Managed Flag value %3 OtherConfig Flag value %4.\r\n
0xb000c77e | DHCP will try regular IPv6 address acquisition on interface %1 even though the machine is in Connected Standby state since the interface has no IPv4 or IPv6 address. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c781 | Firewall port %2 exemption triggered on interface %1.\r\n
0xb000c782 | Firewall port %2 close triggered on interface %1.\r\n
0xb000c783 | The DHCPv6 client received connected standby entry notification.\r\n
0xb000c784 | The DHCPv6 client received connected standby exit notification.\r\n
0xb000c785 | DHCP will try regular IPv6 address acquisition on interface %1 due to registry settings even though the machine is in Connected Standby state and the interface has an IPv4 address. Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000c786 | DHCP is enabled on the interface %1. Status code is %2.\r\n
0xb000c787 | DHCP is disabled on the interface %1. Status code is %2.\r\n
0xb000c788 | DHCP transaction will not be attempted on interface %1 because DHCP is disabled on it.\r\n
0xb000c789 | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the static IPv6 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c78a | DHCP has cancelled IPv6 address acquisition cycle after %1 SOLICIT transmissions on interface %2 because the machine is in Connected Standby state and the interface has the stateless IPv6 address %3. Managed Flag value %4 OtherConfig Flag value %5.\r\n
0xb000c78b | DHCP has cancelled IPv6 address acquisition on interface %1 because the interface is not multicast enabled.\r\n
0xb000c78c | The values of flags received on interface %1 are: Managed Flag value %2 OtherConfig Flag value %3.\r\n
0xb000ea60 | PERFTRACK (DHCPSOLICIT): Offer is accepted on the IPv6 interface %2. Offered Address is %3.\r\n
0xb000ea61 | PERFTRACK (DHCINFORMATIONREQUEST): Options received on the IPv6 interface %2. \r\n
0xb000ea62 | PERFTRACK (DHCPv6): Media Connect on interface %2\r\n
0xb000ea63 | PERFTRACK (DHCPv6): End of Media Connect on interface %2\r\n
