## peerdist.dll

Path: %SystemRoot%\system32\peerdist.dll

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000a | The BranchCache service is starting up.\r\n
0x3000000b | Republishing content - making content available to others in the branch office.\r\n
0x3000000c | Publishing content on the server.\r\n
0x3000000d | Downloading content.\r\n
0x3000000e | Offering content to hosted cache.\r\n
0x3000000f | Publishing content on the server.\r\n
0x30000010 | Loading local cache.\r\n
0x30000011 | Saving local cache.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BranchCache\r\n
0x90000002 | Microsoft-Windows-BranchCache/Operational\r\n
0x91000001 | Microsoft-Windows-BranchCacheMonitoring\r\n
0x91000002 | Microsoft-Windows-BranchCacheMonitoring/Analytic\r\n
0x92000001 | Microsoft-Windows-BranchCacheEventProvider\r\n
0x92000002 | Microsoft-Windows-BranchCacheEventProvider/DiagnosticChannel\r\n
0x93000001 | Microsoft-Windows-BranchCacheClientEventProvider\r\n
0x93000002 | Microsoft-Windows-BranchCacheClientEventProvider/DiagnosticChannel\r\n
0xb0000001 | The BranchCache service started successfully.\r\n
0xb0000002 | The BranchCache service stopped successfully.\r\n
0xb0000003 | The BranchCache service detected that this computer roamed to a different location. Group Policy settings will refresh.\r\n
0xb0000004 | The BranchCache service failed to start.%nError: %1 %2\r\n
0xb0000005 | A BranchCache configuration change was detected.\r\n
0xb0000006 | This computer is configured as a Hosted Cache server and it is also configured to use a Hosted Cache. Only one of these options is allowed.\r\n
0xb0000007 | A firewall is blocking inbound traffic on UDP port 3702, which is used to discover the availability of cached content on this computer. Other computers on the network cannot discover this client. %nTo create a Windows Firewall rule that allows traffic on UDP port 3702, run the command "Enable-BCDistributed" from an elevated PowerShell command prompt. If a different firewall is used, modify the firewall settings to allow this traffic.\r\n
0xb0000008 | A firewall is blocking inbound traffic on TCP port 80, which is used to serve content to requesting computers. As a result, other computers on the network, including the Hosted Cache server, cannot retrieve content from this client. %nTo create a Windows Firewall rule that allows inbound traffic on TCP port 80, run the enable cmdlet appropriate to your service mode from an elevated PowerShell command prompt. If a different firewall is used, modify the firewall settings to allow this traffic.\r\n
0xb0000009 | A firewall is blocking inbound traffic on TCP port 443, which is used by the Hosted Cache server for accepting incoming client offers to add content. As a result, clients cannot add content to the Hosted Cache. %nTo create a Windows Firewall rule that allows inbound traffic on TCP port 443, run the command "Enable-BCHostedServer" from an elevated PowerShell command prompt. If a different firewall is used, modify the firewall settings to allow this traffic.\r\n
0xb000000a | The BranchCache service cannot start because the HTTP namespace used for serving content to requesting clients is not reserved. %nRun the enable cmdlet appropriate to your service mode from an elevated PowerShell command prompt.\r\n
0xb000000b | Content was not cached. BranchCache cannot free enough space in the local cache to accommodate the content being added. %nThe maximum cache size is %1 MB.%nTo increase the cache size, run the command "Set-BCCache" from an elevated PowerShell command prompt and ensure that the disk where the local cache is saved has enough free space.\r\n
0xb000000c | BranchCache cannot publish the content at location %1.%nError: %2 %3%nThis might be because the publication directory location is not on an NTFS partition, the path is too long (typically, greater than 190 characters) or does not exist, or the BranchCache service does not have the permissions to write to the directory location. %nRun the command "Set-BCCache" from an elevated PowerShell command prompt.\r\n
0xb000000d | BranchCache cannot publish the content with content-id: %2 because the publication cache size was exceeded or the disk does not have enough space.%nError: %3 %4%nRun the command "Set-BCCache" from an elevated PowerShell command prompt to increase the cache size.\r\n
0xb000000e | A request message sent to another BranchCache client failed.%nError: %6 %7\r\n
0xb000000f | A request message sent to the Hosted Cache server failed.%nError: %6 %7\r\n
0xb0000010 | A BranchCache client or hosted cache server was unresponsive or provided invalid data. For the next %2 minute(s), BranchCache will not attempt to download data from this machine.\r\n
0xb0000011 | A request message from another BranchCache client was dropped because it was not valid.%nRemote client address: %1%nError: %3 %4\r\n
0xb0000012 | A content retrieval request from another BranchCache client was denied.%nRemote client address: %1%nError: %2 %3\r\n
0xb0000013 | BranchCache tried to offer content to the Hosted Cache server on %1, but there was an error connecting to the Hosted Cache server. %nError: %2 %3 %nPossible reasons for this error:%n-the client has been configured with an incorrect Hosted Cache server name%n-the client has been configured with an incorrect Hosted Cache server port%n-the firewall on the Hosted Cache server is blocking communication%n-the hosted cache server has not been configured with a certificate trusted by the client%n-the client has been configured to use TLS when communicating with the hosted cache, but the hosted cache has not been configured to use TLS%n-the client has been configured to not use TLS when communicating with the hosted cache, but the hosted cache has not been configured to expect TLS%n%nThe client can be configured by running the "netsh branchcache set service hostedclient location=[HOSTEDSERVER]" command from an elevated prompt.%nThe Hosted Cache server can be configured by running the "netsh branchcache set service hostedserver" command from an elevated prompt.%n%nFor advanced configuration and information about certificate deployment on a Hosted Cache server, please see the BranchCache deployment guide.\r\n
0xb0000014 | BranchCache tried to offer content to the Hosted Cache server on %1, but the request timed out. The Hosted Cache server might be experiencing heavy loads or might not be reachable because of network or authentication issues.\r\n
0xb0000015 | %2 instance(s) of event id %1 occurred.\r\n
0xb0000016 | The Windows Firewall rules for the BranchCache service are not configured correctly. %nRun the enable cmdlet appropriate to your service mode from an elevated PowerShell command prompt to set the Windows Firewall configuration correctly.\r\n
0xb0000017 | The BranchCache service could not be started because it has been disabled. %nUse the Services snap-in console to set the Startup Type for the BranchCache service to "Manual" on client computers and to "Automatic" on server computers.\r\n
0xb0000018 | The BranchCache service started, but was unable to load the cache file from disk because the cache file was corrupted or was an incompatible version.%nSub code: %2%nError: %1 %3\r\n
0xb0000019 | The BranchCache service started and loaded a cache file from disk.\r\n
0xb000001a | BranchCache saved a cache file to disk.\r\n
0xb000001b | The BranchCache service stopped and was unable to save the cache file to disk.%nError: %1 %2\r\n
0xb000001c | The BranchCache service is stopping.\r\n
0xb000001d | An SSL certificate is not bound to the port %1 on the Hosted Cache server. As a result, clients cannot add content to the Hosted Cache.%nRun the command "netsh http add sslcert" from an elevated command prompt to bind a certificate.\r\n
0xb000001e | BranchCache cannot initialize the local cache at location %1.%nError: %2 %3%nPossible reasons are that the local cache directory location is not on an NTFS partition, the path is too long (typically, greater than 190 characters) or does not exist, or the BranchCache service does not have the permissions to write to the directory location. %nRun the command "Set-BCCache" from an elevated PowerShell command prompt.\r\n
0xb000001f | A request message sent to a Hosted Cache client failed.%nError: %6 %7\r\n
0xb0000020 | The size of the republication cache store at %1 is too small. The size %2 bytes was rounded up to %3 bytes.\r\n
0xb0000021 | The size of the publication cache store at %1 is too small. The size %2 bytes was rounded up to %3 bytes.\r\n
0xb0000022 | BranchCache failed to register a service connection point.\r\n
0xb0000023 | BranchCache failed to update a service connection point.\r\n
0xb0000024 | BranchCache failed to delete a service connection point.\r\n
0xb0000025 | BranchCache failed to discover a service connection point.\r\n
0xb0000026 | BranchCache completed defragmentation of the republication cache store at %1.%nError: %2 %3\r\n
0xb0000027 | It is recommended that you consider defragmentation of the republication cache store at %1. Defragmentation improves the storage efficiency and performance of BranchCache.%nConfigured max size of the cache store: %2 MB%nActual size of data in the cache store: %3 MB\r\n
0xb0000028 | Client request was dropped because allowable simultaneous uploads limit was reached.%n%nRemote client address: %1%nCurrent Uploads: %2%nMaximum Simultaneous Uploads: %3\r\n
0xb0000029 | BranchCache cannot start because another application or service is listening on TCP port %1 (HTTP).  BranchCache expects incoming requests for content on this port.\r\n
0xb1000001 | Component %1 has arrived as a BranchCache Monitoring provider\r\n
0xb1000002 | Component %1 has departed as a BranchCache Monitoring provider\r\n
0xb1000065 | MS-PCCRR Statistics Snapshot\r\n
0xb1000066 | Segment Id=%5 has been published for Content Id=%3\r\n
0xb1000067 | Content Information has been added for Segment Id=%5 of Content Id=%3\r\n
0xb1000068 | Content Data has been added for Segment Id=%5 of Content Id=%3\r\n
0xb1000069 | A StreamRead has been initiated at Content Offset %6, Segment Offset %7 for Segment Id=%5 of Content Id=%3\r\n
0xb100006a | A BlockRead has been initiated at Content Offset %6, Segment Offset %7 for Segment Id=%5 of Content Id=%3\r\n
0xb100006b | A Discovery Request for Segment Id=%2 has been received from peer %3\r\n
0xb100006c | A Discovery Request for Segment Id=%2 has been sent to %3\r\n
0xb100006d | A Discovery Response for Segment Id=%2 has been received from peer %3\r\n
0xb100006e | A Discovery Response for Segment Id=%2 has been sent to peer %3\r\n
0xb100006f | No discovery response for Segment Id=%2 has been received in time to be used for downloading data\r\n
0xb1000070 | A late discovery response has been received for Segment Id=%2 from peer %3\r\n
0xb1000071 | A block request for block ID=%3 of Segment=%2 has been received from peer %5\r\n
0xb1000072 | A block request for block ID=%3 of Segment=%2 has been sent to peer %5\r\n
0xb1000073 | A block response for block ID=%3 of Segment=%2 with size=%4 has been received from peer %5\r\n
0xb1000074 | A block response for block ID=%3 of Segment=%2 with size=%4 has been sent to peer %5\r\n
0xb10000c9 | Inbound Non-PeerDist HTTP request for URL %2 from client at address IPv4=%3 IPv6=%4\r\n
0xb10000ca | Inbound PeerDist HTTP request for URL %2 from client at address IPv4=%3 IPv6=%4\r\n
0xb10000cb | Inbound PeerDist Missing Data HTTP request for URL %2 from client at address IPv4=%3 IPv6=%4\r\n
0xb10000cc | Inbound PeerDist Hash HTTP request for URL %2 from client at address IPv4=%3 IPv6=%4\r\n
0xb10000cd | Outbound Non-PeerDist HTTP response for URL %2 from client at address IPv4=%3 IPv6=%4\r\n
0xb10000ce | Outbound PeerDist encoded HTTP response for URL %2 from client at address IPv4=%3 IPv6=%4\r\n
0xb10000cf | Outbound PeerDist encoded HTTP response to a PeerDist Hash-only request for URL %2 from client at address IPv4=%3 IPv6=%4\r\n
0xb10000d0 | Outbound HTTP response to a PeerDist Missing Data request for URL %2 from client at address IPv4=%3 IPv6=%4\r\n
0xb2002710 | CreateRequest\r\n
0xb2002711 | SendRequest\r\n
0xb2002712 | SendResponse\r\n
0xb2002713 | CloseRequest\r\n
0xb3002774 | ClientOpenContent\r\n
0xb3002775 | ClientCloseContent\r\n
0xb3002776 | ClientAddData\r\n
0xb3002777 | ClientAddDataComplete\r\n
0xb3002778 | ClientBlockRead\r\n
0xb3002779 | ClientBlockReadComplete\r\n
0xb300277a | ClientStreamRead\r\n
0xb300277b | ClientStreamReadComplete\r\n
