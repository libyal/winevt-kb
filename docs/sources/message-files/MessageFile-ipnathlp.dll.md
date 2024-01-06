## ipnathlp.dll

Path: %SystemRoot%\System32\ipnathlp.dll

### 5.0.2195.6708

Message identifier | Message string
--- | ---
0x00007531 | The DHCP allocator was unable to check whether the IP address %1\r\nis in use on the network for local IP address %2.\r\nThis error may indicate lack of support for address-resolution on the\r\nnetwork, or an error condition on the local machine.\r\nThe data is the error code.\r\n
0x00007532 | The DHCP allocator was unable to bind to the IP address %1.\r\nThis error may indicate a problem with TCP/IP networking.\r\nThe data is the error code.\r\n
0x00007533 | The DHCP allocator was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x00007534 | The DHCP allocator received a message containing an unrecognized code (%1).\r\nThe message was neither a BOOTP request nor a BOOTP reply, and was ignored.\r\n
0x00007535 | The DHCP allocator has detected a DHCP server with IP address %1\r\non the same network as the interface with IP address %2.\r\nThe allocator has disabled itself on the interface in order to avoid\r\nconfusing DHCP clients.\r\n
0x00007536 | The DHCP allocator encountered a network error while attempting to detect\r\nexisting DHCP servers on the network of the interface with IP address %1.\r\nThe data is the error code.\r\n
0x00007537 | The DHCP allocator received a message smaller than the minimum message size.\r\nThe message has been discarded.\r\n
0x00007538 | The DHCP allocator received a message whose format was invalid.\r\nThe message has been discarded.\r\n
0x00007539 | The DHCP allocator encountered a network error while attempting to reply\r\non IP address %1 to a request from a client.\r\nThe data is the error code.\r\n
0x0000753a | The DHCP allocator received a DHCP message containing an unrecognized\r\nmessage type (%1) in the DHCP message type option field.\r\nThe message has been discarded.\r\n
0x0000753b | The DHCP allocator encountered a network error while attempting to\r\nreceive messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000753c | The DHCP allocator detected network address translation (NAT) enabled\r\non the interface with index '%1'.\r\nThe allocator has disabled itself on the interface in order to avoid\r\nconfusing DHCP clients.\r\n
0x0000753d | The DHCP allocator has disabled itself on IP address %1,\r\nsince the IP address is outside the %2/%3 scope\r\nfrom which addresses are being allocated to DHCP clients.\r\nTo enable the DHCP allocator on this IP address,\r\nplease change the scope to include the IP address,\r\nor change the IP address to fall within the scope.\r\n
0x00007917 | end.\r\n
0x00007919 | The DNS proxy agent detected network address translation (NAT) enabled\r\non the interface with index '%1'.\r\nThe agent has disabled itself on the interface in order to avoid\r\nconfusing clients.\r\n
0x0000791a | The DNS proxy agent was unable to bind to the IP address %1.\r\nThis error may indicate a problem with TCP/IP networking.\r\nThe data is the error code.\r\n
0x0000791b | The DNS proxy agent encountered a network error while attempting to\r\nreceive messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000791c | The DNS proxy agent was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x0000791d | The DNS proxy agent encountered a network error while attempting\r\nto forward a response to a client from a name-resolution server\r\non the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000791e | The DNS proxy agent encountered a network error while attempting\r\nto forward a query from the client %1 to the server %2\r\non the interface with IP address %3.\r\nThe data is the error code.\r\n
0x0000791f | The DNS proxy agent was unable to register for notification of changes\r\nto the local list of DNS and WINS servers.\r\nThis may indicate that system resources are low.\r\nThe data is the error code.\r\n
0x00007920 | The DNS proxy agent was unable to read the local list of name-resolution\r\nservers from the registry.\r\nThe data is the error code.\r\n
0x00007921 | The DNS proxy agent was unable to resolve a query from %1\r\nafter consulting all entries in the local list of name-resolution servers.\r\n
0x00007922 | The DNS proxy agent was unable to initiate a demand-dial connection\r\non the default interface while trying to resolve a query from %1.\r\n
0x00007923 | The DNS proxy agent was unable to resolve a query\r\nbecause no list of name-resolution servers is configured locally\r\nand no interface is configured as the default for name-resolution.\r\nPlease configure one or more name-resolution server addresses,\r\nor configure an interface to be automatically dialed when a request\r\nis received by the DNS proxy agent.\r\n
0x00007924 | The DNS proxy agent encountered an error while obtaining the local list\r\nof name-resolution servers.\r\nSome DNS or WINS servers may be inaccessible to clients on the local network.\r\nThe data is the error code.\r\n
0x00007cff | end.\r\n
0x00007d01 | The Network Address Translator (NAT) was unable to update the\r\nlocal address-resolution table to respond to requests for\r\nIP address %1 and mask %2.\r\nAddress-resolution may fail to operate for addresses in the given range.\r\nThis error may indicate a problem with TCP/IP networking,\r\nor it may indicate lack of support for address-resolution\r\nin the underlying network interface.\r\nThe data is the error code.\r\n
0x00007d02 | The Network Address Translator (NAT) was unable to allocate %1 bytes.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x00007d03 | The Network Address Translator (NAT) was unable to request an operation\r\nof the kernel-mode translation module.\r\nThis may indicate misconfiguration, insufficient resources, or\r\nan internal error.\r\nThe data is the error code.\r\n
0x00007d04 | The Network Address Translator (NAT) was unable to load\r\nthe kernel-mode translation module.\r\nThe data is the error code.\r\n
0x00007d05 | The Network Address Translator (NAT) was unable to unload\r\nthe kernel-mode translation module.\r\nThe data is the error code.\r\n
0x00007d06 | The Internet Connection Sharing service could not start because\r\nanother process has taken control of the kernel-mode translation module.\r\nThis may occur when the Connection Sharing component has been installed\r\nin the Routing and Remote Access Manager.\r\nIf this is the case, please remove the Connection Sharing component \r\nand restart the Internet Connection Sharing service.\r\n
0x00007d07 | The Connection Sharing component could not start because another process\r\nhas taken control of the kernel-mode translation module.\r\nThis may occur when Internet Connection Sharing has been enabled\r\nfor a connection.\r\nIf this is the case, please disable Internet Connection Sharing\r\nfor the connection in the Network Connections folder and then\r\nrestart Routing and Remote Access.\r\n
0x000080e7 | end.\r\n
0x000080e9 | The DirectPlay transparent proxy detected network address translation (NAT)\r\nenabled on the interface with index '%1'.\r\nThe agent has disabled itself on the interface in order to avoid\r\nconfusing clients.\r\n
0x000080ea | The DirectPlay transparent proxy was unable to bind to the IP address %1.\r\nThis error may indicate a problem with TCP/IP networking.\r\nThe data is the error code.\r\n
0x000080eb | The DirectPlay transparent proxy encountered a network error while\r\nattempting to receive messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x000080ec | The DirectPlay transparent proxy was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x000080ed | The DirectPlay transparent proxy encountered a network error while\r\nattempting to accept connections on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x000080ef | The DirectPlay transparent proxy encountered a network error while\r\nattempting to send messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x000084cf | end.\r\n
0x000084d1 | The H.323 transparent proxy detected network address translation (NAT)\r\nenabled on the interface with index '%1'.\r\nThe agent has disabled itself on the interface in order to avoid\r\nconfusing clients.\r\n
0x000084d2 | The H.323 transparent proxy was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x000088b7 | end.\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x00007531 | The DHCP allocator was unable to check whether the IP address %1\r\nis in use on the network for local IP address %2.\r\nThis error may indicate lack of support for address-resolution on the\r\nnetwork, or an error condition on the local machine.\r\nThe data is the error code.\r\n
0x00007532 | The DHCP allocator was unable to bind to the IP address %1.\r\nThis error may indicate a problem with TCP/IP networking.\r\nThe data is the error code.\r\n
0x00007533 | The DHCP allocator was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x00007534 | The DHCP allocator received a message containing an unrecognized code (%1).\r\nThe message was neither a BOOTP request nor a BOOTP reply, and was ignored.\r\n
0x00007535 | The DHCP allocator has detected a DHCP server with IP address %1\r\non the same network as the interface with IP address %2.\r\nThe allocator has disabled itself on the interface in order to avoid\r\nconfusing DHCP clients.\r\n
0x00007536 | The DHCP allocator encountered a network error while attempting to detect\r\nexisting DHCP servers on the network of the interface with IP address %1.\r\nThe data is the error code.\r\n
0x00007537 | The DHCP allocator received a message smaller than the minimum message size.\r\nThe message has been discarded.\r\n
0x00007538 | The DHCP allocator received a message whose format was invalid.\r\nThe message has been discarded.\r\n
0x00007539 | The DHCP allocator encountered a network error while attempting to reply\r\non IP address %1 to a request from a client.\r\nThe data is the error code.\r\n
0x0000753a | The DHCP allocator received a DHCP message containing an unrecognized\r\nmessage type (%1) in the DHCP message type option field.\r\nThe message has been discarded.\r\n
0x0000753b | The DHCP allocator encountered a network error while attempting to\r\nreceive messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000753c | The DHCP allocator detected network address translation (NAT) enabled\r\non the interface with index '%1'.\r\nThe allocator has disabled itself on the interface in order to avoid\r\nconfusing DHCP clients.\r\n
0x0000753d | The DHCP allocator has disabled itself on IP address %1,\r\nsince the IP address is outside the %2/%3 scope\r\nfrom which addresses are being allocated to DHCP clients.\r\nTo enable the DHCP allocator on this IP address,\r\nplease change the scope to include the IP address,\r\nor change the IP address to fall within the scope.\r\n
0x00007917 | end.\r\n
0x00007919 | The DNS proxy agent detected network address translation (NAT) enabled\r\non the interface with index '%1'.\r\nThe agent has disabled itself on the interface in order to avoid\r\nconfusing clients.\r\n
0x0000791a | The DNS proxy agent was unable to bind to the IP address %1.\r\nThis error may indicate a problem with TCP/IP networking.\r\nThe data is the error code.\r\n
0x0000791b | The DNS proxy agent encountered a network error while attempting to\r\nreceive messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000791c | The DNS proxy agent was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x0000791d | The DNS proxy agent encountered a network error while attempting\r\nto forward a response to a client from a name-resolution server\r\non the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000791e | The DNS proxy agent encountered a network error while attempting\r\nto forward a query from the client %1 to the server %2\r\non the interface with IP address %3.\r\nThe data is the error code.\r\n
0x0000791f | The DNS proxy agent was unable to register for notification of changes\r\nto the local list of DNS and WINS servers.\r\nThis may indicate that system resources are low.\r\nThe data is the error code.\r\n
0x00007920 | The DNS proxy agent was unable to read the local list of name-resolution\r\nservers from the registry.\r\nThe data is the error code.\r\n
0x00007921 | The DNS proxy agent was unable to resolve a query from %1\r\nafter consulting all entries in the local list of name-resolution servers.\r\n
0x00007922 | The DNS proxy agent was unable to initiate a demand-dial connection\r\non the default interface while trying to resolve a query from %1.\r\n
0x00007923 | The DNS proxy agent was unable to resolve a query\r\nbecause no list of name-resolution servers is configured locally\r\nand no interface is configured as the default for name-resolution.\r\nPlease configure one or more name-resolution server addresses,\r\nor configure an interface to be automatically dialed when a request\r\nis received by the DNS proxy agent.\r\n
0x00007924 | The DNS proxy agent encountered an error while obtaining the local list\r\nof name-resolution servers.\r\nSome DNS or WINS servers may be inaccessible to clients on the local network.\r\nThe data is the error code.\r\n
0x00007925 | The DNS proxy agent was unable to register for notification of changes\r\nto the ICS Domain suffix string.\r\nThis may indicate that system resources are low.\r\nThe data is the error code.\r\n
0x00007926 | The DNS proxy agent was unable to read the ICS Domain suffix string\r\nfrom the registry.\r\nThe data is the error code.\r\n
0x00007cff | end.\r\n
0x00007d01 | The Network Address Translator (NAT) was unable to update the\r\nlocal address-resolution table to respond to requests for\r\nIP address %1 and mask %2.\r\nAddress-resolution may fail to operate for addresses in the given range.\r\nThis error may indicate a problem with TCP/IP networking,\r\nor it may indicate lack of support for address-resolution\r\nin the underlying network interface.\r\nThe data is the error code.\r\n
0x00007d02 | The Network Address Translator (NAT) was unable to allocate %1 bytes.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x00007d03 | The Network Address Translator (NAT) was unable to request an operation\r\nof the kernel-mode translation module.\r\nThis may indicate misconfiguration, insufficient resources, or\r\nan internal error.\r\nThe data is the error code.\r\n
0x00007d04 | The Network Address Translator (NAT) was unable to load\r\nthe kernel-mode translation module.\r\nThe data is the error code.\r\n
0x00007d05 | The Network Address Translator (NAT) was unable to unload\r\nthe kernel-mode translation module.\r\nThe data is the error code.\r\n
0x00007d06 | The Internet Connection Sharing service could not start because\r\nanother process has taken control of the kernel-mode translation module.\r\nThis may occur when the Connection Sharing component has been installed\r\nin the Routing and Remote Access Manager.\r\nIf this is the case, please remove the Connection Sharing component \r\nand restart the Internet Connection Sharing service.\r\n
0x00007d07 | The Connection Sharing component could not start because another process\r\nhas taken control of the kernel-mode translation module.\r\nThis may occur when Internet Connection Sharing has been enabled\r\nfor a connection.\r\nIf this is the case, please disable Internet Connection Sharing\r\nfor the connection in the Network Connections folder and then\r\nrestart Routing and Remote Access.\r\n
0x000080e7 | end.\r\n
0x000084d1 | The H.323 transparent proxy detected network address translation (NAT)\r\nenabled on the interface with index '%1'.\r\nThe agent has disabled itself on the interface in order to avoid\r\nconfusing clients.\r\n
0x000084d2 | The H.323 transparent proxy was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x000088b7 | end.\r\n
0x000088b9 | The FTP transparent proxy detected network address translation (NAT)\r\nenabled on the interface with index '%1'.\r\nThe agent has disabled itself on the interface in order to avoid\r\nconfusing clients.\r\n
0x000088ba | The FTP transparent proxy was unable to bind to the IP address %1.\r\nThis error may indicate a problem with TCP/IP networking.\r\nThe data is the error code.\r\n
0x000088bb | The FTP transparent proxy encountered a network error while\r\nattempting to receive messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x000088bc | The FTP transparent proxy was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x000088bd | The FTP transparent proxy encountered a network error while\r\nattempting to accept connections on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x000088bf | The FTP transparent proxy encountered a network error while\r\nattempting to send messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x00008c9f | end.\r\n
0x00008ca1 | The PAST transparent proxy detected network address translation (NAT)\r\nenabled on the interface with index '%1'.\r\nThe agent has disabled itself on the interface in order to avoid\r\nconfusing clients.\r\n
0x00008ca2 | The PAST transparent proxy was unable to bind to the IP address %1.\r\nThis error may indicate a problem with TCP/IP networking.\r\nThe data is the error code.\r\n
0x00008ca3 | The PAST transparent proxy encountered a network error while\r\nattempting to receive messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x00008ca4 | The PAST transparent proxy was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x00008ca5 | The PAST transparent proxy encountered a network error while\r\nattempting to accept connections on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x00008ca7 | The PAST transparent proxy encountered a network error while\r\nattempting to send messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x00009087 | end.\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00007531 | The DHCP allocator was unable to check whether the IP address %1\r\nis in use on the network for local IP address %2.\r\nThis error may indicate lack of support for address-resolution on the\r\nnetwork, or an error condition on the local machine.\r\nThe data is the error code.\r\n
0x00007532 | The DHCP allocator was unable to bind to the IP address %1.\r\nThis error may indicate a problem with TCP/IP networking.\r\nThe data is the error code.\r\n
0x00007533 | The DHCP allocator was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x00007534 | The DHCP allocator received a message containing an unrecognized code (%1).\r\nThe message was neither a BOOTP request nor a BOOTP reply, and was ignored.\r\n
0x00007535 | The DHCP allocator has detected a DHCP server with IP address %1\r\non the same network as the interface with IP address %2.\r\nThe allocator has disabled itself on the interface in order to avoid\r\nconfusing DHCP clients.\r\n
0x00007536 | The DHCP allocator encountered a network error while attempting to detect\r\nexisting DHCP servers on the network of the interface with IP address %1.\r\nThe data is the error code.\r\n
0x00007537 | The DHCP allocator received a message smaller than the minimum message size.\r\nThe message has been discarded.\r\n
0x00007538 | The DHCP allocator received a message whose format was invalid.\r\nThe message has been discarded.\r\n
0x00007539 | The DHCP allocator encountered a network error while attempting to reply\r\non IP address %1 to a request from a client.\r\nThe data is the error code.\r\n
0x0000753a | The DHCP allocator received a DHCP message containing an unrecognized\r\nmessage type (%1) in the DHCP message type option field.\r\nThe message has been discarded.\r\n
0x0000753b | The DHCP allocator encountered a network error while attempting to\r\nreceive messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000753c | The DHCP allocator detected network address translation (NAT) enabled\r\non the interface with index '%1'.\r\nThe allocator has disabled itself on the interface in order to avoid\r\nconfusing DHCP clients.\r\n
0x0000753d | The DHCP allocator has disabled itself on IP address %1,\r\nsince the IP address is outside the %2/%3 scope\r\nfrom which addresses are being allocated to DHCP clients.\r\nTo enable the DHCP allocator on this IP address,\r\nplease change the scope to include the IP address,\r\nor change the IP address to fall within the scope.\r\n
0x00007917 | end.\r\n
0x00007919 | The DNS proxy agent detected network address translation (NAT) enabled\r\non the interface with index '%1'.\r\nThe agent has disabled itself on the interface in order to avoid\r\nconfusing clients.\r\n
0x0000791a | The DNS proxy agent was unable to bind to the IP address %1.\r\nThis error may indicate a problem with TCP/IP networking.\r\nThe data is the error code.\r\n
0x0000791b | The DNS proxy agent encountered a network error while attempting to\r\nreceive messages on the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000791c | The DNS proxy agent was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x0000791d | The DNS proxy agent encountered a network error while attempting\r\nto forward a response to a client from a name-resolution server\r\non the interface with IP address %1.\r\nThe data is the error code.\r\n
0x0000791e | The DNS proxy agent encountered a network error while attempting\r\nto forward a query from the client %1 to the server %2\r\non the interface with IP address %3.\r\nThe data is the error code.\r\n
0x0000791f | The DNS proxy agent was unable to register for notification of changes\r\nto the local list of DNS and WINS servers.\r\nThis may indicate that system resources are low.\r\nThe data is the error code.\r\n
0x00007920 | The DNS proxy agent was unable to read the local list of name-resolution\r\nservers from the registry.\r\nThe data is the error code.\r\n
0x00007921 | The DNS proxy agent was unable to resolve a query from %1\r\nafter consulting all entries in the local list of name-resolution servers.\r\n
0x00007922 | The DNS proxy agent was unable to initiate a demand-dial connection\r\non the default interface while trying to resolve a query from %1.\r\n
0x00007923 | The DNS proxy agent was unable to resolve a query\r\nbecause no list of name-resolution servers is configured locally\r\nand no interface is configured as the default for name-resolution.\r\nPlease configure one or more name-resolution server addresses,\r\nor configure an interface to be automatically dialed when a request\r\nis received by the DNS proxy agent.\r\n
0x00007924 | The DNS proxy agent encountered an error while obtaining the local list\r\nof name-resolution servers.\r\nSome DNS or WINS servers may be inaccessible to clients on the local network.\r\nThe data is the error code.\r\n
0x00007925 | The DNS proxy agent was unable to register for notification of changes\r\nto the ICS Domain suffix string.\r\nThis may indicate that system resources are low.\r\nThe data is the error code.\r\n
0x00007926 | The DNS proxy agent was unable to read the ICS Domain suffix string\r\nfrom the registry.\r\nThe data is the error code.\r\n
0x00007927 | The DNS proxy agent received a message smaller than the\r\nminimum message size.\r\nThe message has been discarded.\r\n
0x00007cff | end.\r\n
0x00007d01 | The Network Address Translator (NAT) was unable to update the\r\nlocal address-resolution table to respond to requests for\r\nIP address %1 and mask %2.\r\nAddress-resolution may fail to operate for addresses in the given range.\r\nThis error may indicate a problem with TCP/IP networking,\r\nor it may indicate lack of support for address-resolution\r\nin the underlying network interface.\r\nThe data is the error code.\r\n
0x00007d02 | The Network Address Translator (NAT) was unable to allocate %1 bytes.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x00007d03 | The Network Address Translator (NAT) was unable to request an operation\r\nof the kernel-mode translation module.\r\nThis may indicate misconfiguration, insufficient resources, or\r\nan internal error.\r\nThe data is the error code.\r\n
0x00007d04 | The Network Address Translator (NAT) was unable to load\r\nthe kernel-mode translation module.\r\nThe data is the error code.\r\n
0x00007d05 | The Network Address Translator (NAT) was unable to unload\r\nthe kernel-mode translation module.\r\nThe data is the error code.\r\n
0x00007d06 | The Internet Connection Sharing service could not start because\r\nanother process has taken control of the kernel-mode translation module.\r\nThis may occur when the Connection Sharing component has been installed\r\nin the Routing and Remote Access Manager.\r\nIf this is the case, please remove the Connection Sharing component \r\nand restart the Internet Connection Sharing service.\r\n
0x00007d07 | The Connection Sharing component could not start because another process\r\nhas taken control of the kernel-mode translation module.\r\nThis may occur when Internet Connection Sharing has been enabled\r\nfor a connection.\r\nIf this is the case, please disable Internet Connection Sharing\r\nfor the connection in the Network Connections folder and then\r\nrestart Routing and Remote Access.\r\n
0x00007d08 | The Network Address Translator (NAT) was unable to expand the wildcard \r\nmappings.\r\nThis may indicate misconfiguration, insufficient resources, or\r\nan internal error.\r\nThe data is the error code.\r\n
0x000080e7 | end.\r\n
0x000084d1 | The H.323 transparent proxy detected network address translation (NAT)\r\nenabled on the interface with index '%1'.\r\nThe agent has disabled itself on the interface in order to avoid\r\nconfusing clients.\r\n
0x000084d2 | The H.323 transparent proxy was unable to allocate %1 bytes of memory.\r\nThis may indicate that the system is low on virtual memory,\r\nor that the memory-manager has encountered an internal error.\r\n
0x000088b7 | end.\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x00007531 | The DHCP allocator was unable to check whether the IP address %1 is in use on the network for local IP address %2. This error may indicate lack of support for address-resolution on the network, or an error condition on the local machine. The data is the error code.\r\n
0x00007532 | The DHCP allocator was unable to bind to the IP address %1. This error may indicate a problem with TCP/IP networking. The data is the error code.\r\n
0x00007533 | The DHCP allocator was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory-manager has encountered an internal error.\r\n
0x00007534 | The DHCP allocator received a message containing an unrecognized code (%1). The message was neither a BOOTP request nor a BOOTP reply, and was ignored.\r\n
0x00007535 | The DHCP allocator has detected a DHCP server with IP address %1 on the same network as the interface with IP address %2. The allocator has disabled itself on the interface to avoid confusing DHCP clients.\r\n
0x00007536 | The DHCP allocator encountered a network error while attempting to detect existing DHCP servers on the network of the interface with IP address %1. The data is the error code.\r\n
0x00007537 | The DHCP allocator received a message smaller than the minimum message size. The message has been discarded.\r\n
0x00007538 | The DHCP allocator received a message whose format was invalid. The message has been discarded.\r\n
0x00007539 | The DHCP allocator encountered a network error while attempting to reply on IP address %1 to a request from a client. The data is the error code.\r\n
0x0000753a | The DHCP allocator received a DHCP message containing an unrecognized message type (%1) in the DHCP message type option field. The message has been discarded.\r\n
0x0000753b | The DHCP allocator encountered a network error while attempting to receive messages on the interface with IP address %1. The data is the error code.\r\n
0x0000753c | The DHCP allocator detected network address translation (NAT) enabled on the interface with index '%1'. The allocator has disabled itself on the interface to avoid confusing DHCP clients.\r\n
0x0000753d | The DHCP allocator has disabled itself on IP address %1, since the IP address is outside the %2/%3 scope from which addresses are being allocated to DHCP clients. To enable the DHCP allocator on this IP address, change the scope to include the IP address, or change the IP address to fall within the scope.\r\n
0x00007917 | end.\r\n
0x00007919 | The DNS proxy agent detected network address translation (NAT) enabled on the interface with index '%1'. The agent has disabled itself on the interface to avoid confusing clients.\r\n
0x0000791a | The DNS proxy agent was unable to bind to the IP address %1. This error may indicate a problem with TCP/IP networking. The data is the error code.\r\n
0x0000791b | The DNS proxy agent encountered a network error while attempting to receive messages on the interface with IP address %1. The data is the error code.\r\n
0x0000791c | The DNS proxy agent was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x0000791d | The DNS proxy agent encountered a network error while attempting to forward a response to a client from a name resolution server on the interface with IP address %1. The data is the error code.\r\n
0x0000791e | The DNS proxy agent encountered a network error while attempting to forward a query from the client %1 to the server %2 on the interface with IP address %3. The data is the error code.\r\n
0x0000791f | The DNS proxy agent was unable to register for notification of changes to the local list of DNS and WINS servers. This may indicate that system resources are low. The data is the error code.\r\n
0x00007920 | The DNS proxy agent was unable to read the local list of name resolution servers from the registry. The data is the error code.\r\n
0x00007921 | The DNS proxy agent was unable to resolve a query from %1 after consulting all entries in the local list of name resolution servers.\r\n
0x00007922 | The DNS proxy agent was unable to initiate a demand dial connection on the default interface while trying to resolve a query from %1.\r\n
0x00007923 | The DNS proxy agent was unable to resolve a query because no list of name resolution servers is configured locally and no interface is configured as the default for name resolution.\r\n
0x00007924 | The DNS proxy agent encountered an error while obtaining the local list of name resolution servers. Some DNS or WINS servers may be inaccessible to clients on the local network. The data is the error code.\r\n
0x00007925 | The DNS proxy agent was unable to register for notification of changes to the ICS Domain suffix string. This may indicate that system resources are low. The data is the error code.\r\n
0x00007926 | The DNS proxy agent was unable to read the ICS Domain suffix string from the registry. The data is the error code.\r\n
0x00007927 | The DNS proxy agent received a message smaller than the minimum message size. The message has been discarded.\r\n
0x00007cff | end.\r\n
0x00007d01 | The Network Address Translator (NAT) was unable to update the local address resolution table to respond to requests for IP address %1 and mask %2. Address resolution may fail to operate for addresses in the given range. This error may indicate a problem with TCP/IP networking, or it may indicate lack of support for address resolution in the underlying network interface. The data is the error code.\r\n
0x00007d02 | The Network Address Translator (NAT) was unable to allocate %1 bytes. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x00007d03 | The Network Address Translator (NAT) was unable to request an operation of the kernel-mode translation module. This may indicate misconfiguration, insufficient resources, or an internal error. The data is the error code.\r\n
0x00007d04 | The Network Address Translator (NAT) was unable to load the kernel-mode translation module. The data is the error code.\r\n
0x00007d05 | The Network Address Translator (NAT) was unable to unload the kernel-mode translation module. The data is the error code.\r\n
0x00007d06 | The Internet Connection Sharing service could not start because another process has taken control of the kernel-mode translation module.\r\n
0x00007d07 | The Connection Sharing component could not start because another process has taken control of the kernel-mode translation module.\r\n
0x00007d08 | The Network Address Translator (NAT) was unable to expand the wildcard  mappings. This may indicate misconfiguration, insufficient resources, or an internal error. The data is the error code.\r\n
0x000080e7 | end.\r\n
0x000084d1 | The ICS_IPV6 failed to configure IPv6 stack.\r\n
0x000084d2 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d3 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d4 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d5 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d6 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d7 | Failed to create registry key "System\\CurrentControlSet\\Services\\Tcpip6\\Parameters".\r\n
0x000088b7 | end.\r\n
0x90000001 | Microsoft-Windows-SharedAccess_NAT\r\n

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x00007531 | The DHCP allocator was unable to check whether the IP address %1 is in use on the network for local IP address %2. This error may indicate lack of support for address-resolution on the network, or an error condition on the local machine. The data is the error code.\r\n
0x00007532 | The DHCP allocator was unable to bind to the IP address %1. This error may indicate a problem with TCP/IP networking. The data is the error code.\r\n
0x00007533 | The DHCP allocator was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory-manager has encountered an internal error.\r\n
0x00007534 | The DHCP allocator received a message containing an unrecognized code (%1). The message was neither a BOOTP request nor a BOOTP reply, and was ignored.\r\n
0x00007535 | The DHCP allocator has detected a DHCP server with IP address %1 on the same network as the interface with IP address %2. The allocator has disabled itself on the interface to avoid confusing DHCP clients.\r\n
0x00007536 | The DHCP allocator encountered a network error while attempting to detect existing DHCP servers on the network of the interface with IP address %1. The data is the error code.\r\n
0x00007537 | The DHCP allocator received a message smaller than the minimum message size. The message has been discarded.\r\n
0x00007538 | The DHCP allocator received a message whose format was invalid. The message has been discarded.\r\n
0x00007539 | The DHCP allocator encountered a network error while attempting to reply on IP address %1 to a request from a client. The data is the error code.\r\n
0x0000753a | The DHCP allocator received a DHCP message containing an unrecognized message type (%1) in the DHCP message type option field. The message has been discarded.\r\n
0x0000753b | The DHCP allocator encountered a network error while attempting to receive messages on the interface with IP address %1. The data is the error code.\r\n
0x0000753c | The DHCP allocator detected network address translation (NAT) enabled on the interface with index '%1'. The allocator has disabled itself on the interface to avoid confusing DHCP clients.\r\n
0x0000753d | The DHCP allocator has disabled itself on IP address %1, since the IP address is outside the %2/%3 scope from which addresses are being allocated to DHCP clients. To enable the DHCP allocator on this IP address, change the scope to include the IP address, or change the IP address to fall within the scope.\r\n
0x00007917 | end.\r\n
0x00007919 | The DNS proxy agent detected network address translation (NAT) enabled on the interface with index '%1'. The agent has disabled itself on the interface to avoid confusing clients.\r\n
0x0000791a | The DNS proxy agent was unable to bind to the IP address %1. This error may indicate a problem with TCP/IP networking. The data is the error code.\r\n
0x0000791b | The DNS proxy agent encountered a network error while attempting to receive messages on the interface with IP address %1. The data is the error code.\r\n
0x0000791c | The DNS proxy agent was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x0000791d | The DNS proxy agent encountered a network error while attempting to forward a response to a client from a name resolution server on the interface with IP address %1. The data is the error code.\r\n
0x0000791e | The DNS proxy agent encountered a network error while attempting to forward a query from the client %1 to the server %2 on the interface with IP address %3. The data is the error code.\r\n
0x0000791f | The DNS proxy agent was unable to register for notification of changes to the local list of DNS and WINS servers. This may indicate that system resources are low. The data is the error code.\r\n
0x00007920 | The DNS proxy agent was unable to read the local list of name resolution servers from the registry. The data is the error code.\r\n
0x00007921 | The DNS proxy agent was unable to resolve a query from %1 after consulting all entries in the local list of name resolution servers.\r\n
0x00007922 | The DNS proxy agent was unable to initiate a demand dial connection on the default interface while trying to resolve a query from %1.\r\n
0x00007923 | The DNS proxy agent was unable to resolve a query because no list of name resolution servers is configured locally and no interface is configured as the default for name resolution.\r\n
0x00007924 | The DNS proxy agent encountered an error while obtaining the local list of name resolution servers. Some DNS or WINS servers may be inaccessible to clients on the local network. The data is the error code.\r\n
0x00007925 | The DNS proxy agent was unable to register for notification of changes to the ICS Domain suffix string. This may indicate that system resources are low. The data is the error code.\r\n
0x00007926 | The DNS proxy agent was unable to read the ICS Domain suffix string from the registry. The data is the error code.\r\n
0x00007927 | The DNS proxy agent received a message smaller than the minimum message size. The message has been discarded.\r\n
0x00007cff | end.\r\n
0x00007d01 | The Network Address Translator (NAT) was unable to update the local address resolution table to respond to requests for IP address %1 and mask %2. Address resolution may fail to operate for addresses in the given range. This error may indicate a problem with TCP/IP networking, or it may indicate lack of support for address resolution in the underlying network interface. The data is the error code.\r\n
0x00007d02 | The Network Address Translator (NAT) was unable to allocate %1 bytes. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x00007d03 | The Network Address Translator (NAT) was unable to request an operation of the kernel-mode translation module. This may indicate misconfiguration, insufficient resources, or an internal error. The data is the error code.\r\n
0x00007d04 | The Network Address Translator (NAT) was unable to load the kernel-mode translation module. The data is the error code.\r\n
0x00007d05 | The Network Address Translator (NAT) was unable to unload the kernel-mode translation module. The data is the error code.\r\n
0x00007d06 | The Internet Connection Sharing service could not start because another process has taken control of the kernel-mode translation module.\r\n
0x00007d07 | The Connection Sharing component could not start because another process has taken control of the kernel-mode translation module.\r\n
0x00007d08 | The Network Address Translator (NAT) was unable to expand the wildcard  mappings. This may indicate misconfiguration, insufficient resources, or an internal error. The data is the error code.\r\n
0x000080e7 | end.\r\n
0x000084d1 | The ICS_IPV6 failed to configure IPv6 stack.\r\n
0x000084d2 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d3 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d4 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d5 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d6 | The ICS_IPV6 was unable to allocate %1 bytes of memory. This may indicate that the system is low on virtual memory, or that the memory manager has encountered an internal error.\r\n
0x000084d7 | Failed to create registry key "System\\CurrentControlSet\\Services\\Tcpip6\\Parameters".\r\n
0x000088b7 | end.\r\n
0x10000038 | Classic\r\n
0x90000001 | Microsoft-Windows-SharedAccess_NAT\r\n
