## mrxsmb.sys

Path: %SystemRoot%\system32\drivers\mrxsmb.sys

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007595 | SMB ISC request: SessionEntry %1 ServerName %3\r\n
0xb0007596 | SMB ISC completion: SessionEntry %1 ServerName %3 Status %4\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759b | SMB exchange expired: Exchange %1 Window %2\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075f9 | WSK get address info request: ServerName %2 Irp %3\r\n
0xb00075fa | WSK get address info completion: Irp %1 Status %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb0007601 | WSK disconnect: VcEndpoint %1 Socket %2 Status %3\r\n
0xb0007603 | Connection to server %5 IP Address %3 was aborted.\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb0007793 | Persistent handle %2:%3 CreateGUID %4 to %10%12 failed with Status %7\r\n
0xb0007794 | Resilient handle %2:%3 to %10%12 failed with Status %7\r\n
0xb0007795 | Attempt to open CA handle %2:%3 CreateGUID %4 to %10%12 failed with Status %7\r\n
0xb0007796 | Persistent handle %2:%3 CreateGUID %4 to %10%12 was orphaned.\r\n
0xb0007797 | Resilient handle %2:%3 to %10%12 was orphaned.\r\n
0xb000779d | Session to server %6 was lost Status %4\r\n
0xb000779e | Session to server %6 was re-established.\r\n
0xb000779f | Connection to share %6 was lost. Status %4\r\n
0xb00077a0 | Connection to share %6 was re-established.\r\n
0xb00077a1 | Handle %2:%3 CreateGUID %4 to %10%12 granted without persistence.\r\n
0xb00077a2 | The SMB client received a request to move file server cluster %2 to IP address %4\r\n
0xb00077a3 | The SMB client successfully moved file server cluster %2 to IP address %4\r\n
0xb00077a4 | The SMB client failed to move file server cluster %2. Error: %5\r\n
0xb00077ec | The server %2 does not support multichannel\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb00077f2 | The client can not connect to the server %2 due to a multichannel constraint registry setting\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | Tdi\r\n
0xd000000b | Wsk\r\n
0xd000000c | Rdma\r\n

### 6.3.9600.16384, 6.3.9600.18586

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0x90000007 | Microsoft-Windows-SMBClient/Connectivity\r\n
0x90000008 | Microsoft-Windows-SMBClient/Security\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb0007795 | Failed to open a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb0007850 | The server name cannot be resolved.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe client cannot resolve the server address in DNS or WINS. This issue often manifests immediately after joining a computer to the domain, when the client's DNS registration may not yet have propagated to all DNS servers. You should also expect this event at system startup on a DNS server (such as a domain controller) that points to itself for the primary DNS. You should validate the DNS client settings on this computer using IPCONFIG /ALL and NSLOOKUP.\r\n
0xb0007851 | %1.%n%nError: %2%n%nServer name: %4\r\n
0xb0007853 | The network connection failed.%n%nError: %2%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks port 445 or 5445 can also cause this issue.\r\n
0xb0007859 | A request timed out because there was no response from the server.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThe server is responding over TCP but not over SMB. Ensure the Server service is running and responsive, and the disks do not have high per-IO latency, which makes the disks appear unresponsive to SMB. Also, ensure the server is responsive overall and not paused; for instance, make sure you can log on to it.\r\n
0xb000785a | Added a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TCP/IP. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785b | Deleted a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785c | Added a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TDI. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785d | Deleted a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785e | Witness registration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%nFile server cluster address: %6%n%nGuidance:%nThe client successfully registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb000785f | Witness deregistration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%n%nGuidance:%nThe client successfully de-registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb0007860 | The server failed the negotiate request.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe server does not support any dialect that the client is trying to negotiate, such as the client has SMB2/SMB3 disabled and the server has SMB1 disabled.\r\n
0xb0007861 | Close request failed.%n%nError: %2%n%nPath: %4%6%n%nGuidance:%nA persistent handle (Continuous Availability) or a resilient handle failed to close.\r\n
0xb0007862 | RDMA interfaces are available but the client failed to connect to the server over RDMA transport.%n%nServer name: %2%n%nGuidance:%nBoth client and server have RDMA (SMB Direct) adaptors but there was a problem with the connection and the client had to fall back to using TCP/IP SMB (non-RDMA).\r\n
0xb00078ba | A request on persistent/resilient handle failed because the handle was invalid or it exceeded the timeout.%n%nStatus: %7%n%nType: %1%nPath: %4%6%nRestart count: %2%n%nGuidance:%nAfter retrying a request on a Continuously Available (Persistent) handle or a Resilient handle, the client was unable to reconnect the handle. This event is the result of a handle recovery failure. Review other events for more details.\r\n
0xb00078bb | The SMB Multichannel registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:%2%n%nGuidance:%nYou can configure SMB Multichannel on the client using the Windows PowerShell cmdlet Set-SmbClientConfiguration. Disabling SMB client multichannel support is not a recommended configuration, as it can lead to degraded performance and decreased reliability if one channel or network path fails.\r\n
0xb00078bc | The SMB 3 and SMB 2 driver is not configured with the default start type.%n%nDefault Start Type: DEMAND_START%nConfigured Start Type: DISABLED%n%nGuidance:%nYou should expect this event when disabling SMB2/SMB3 for the client using SC.EXE or editing the Windows registry. Microsoft does not recommend disabling SMB2/SMB3. Disabling SMB2/SMB3 prevents use of features such as SMB Transparent Failover, SMB Scale Out, SMB Multichannel, SMB Direct (RDMA), SMB Encryption, VSS for SMB file shares, and SMB Directory Leasing. SMB provides alternative troubleshooting workarounds to disabling SMB2/SMB3 in most cases.\r\n
0xb00078bd | The client supports SMB Direct (RDMA) and SMB Signing is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Signing. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078be | The client supports SMB Direct (RDMA) and SMB Encryption is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Encryption on the server for shares accessed by this client. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb0007918 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nSerrver name: %6\r\n
0xb0007919 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nServer name: %6%nPrincipal name: %8\r\n
0xb000791a | The outbound authentication failed using a network token.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThis typically indicates that delegation must be configured for a Kerberos double-hop scenario. If delegation is configured, confirm that the services are configured correctly on the middle-tier server.\r\n
0xb000791b | The LmCompatibilityLevel value is different from the default.%n%nConfigured LM Compatibility Level: %2%nDefault LM Compatibility Level: 3%n%nGuidance:%nLAN Manager (LM) authentication is the protocol used to authenticate Windows clients for network operations. This includes joining a domain, accessing network resources, and authenticating users or computers. This determines which challenge/response authentication protocol is negotiated between the client and the server computers. Specifically, the LM authentication level determines which authentication protocols the client will try to negotiate or the server will accept. The value set for LmCompatibilityLevel determines which challenge/response authentication protocol is used for network logons. This value affects the level of authentication protocol that clients use, the level of session security negotiated, and the level of authentication accepted by servers.%n%nValue (Setting) - Description%n%n0 (Send LM & NTLM responses) - Clients use LM and NTLM authentication and never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n1 (Send LM & NTLM - use NTLMv2 session security if negotiated) - Clients use LM and NTLM authentication, and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n2 (Send NTLM response only) - Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n3 (Send NTLM v2 response only) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n4 (Send NTLMv2 response only/refuse LM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and accept only NTLM and NTLMv2 authentication.%n%n5 (Send NTLM v2 response only/refuse LM & NTLM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM and accept only NTLMv2 authentication.%n%nIncompatibly configured  LmCompatibility levels between a client and server (such as 0 on a client and 5 on a server) prevent access to the server. Non-Microsoft clients and servers also provide these configuration settings.\r\n
0xb0007922 | The SMB client failed to connect to the share.%n%nError: %2%n%nPath: %4%6\r\n
0xb0007924 | The negotiate validation failed.%n%nFrom negotiate response:%nDialect: %1%nSecurityMode: %2%nCapabilities: %3%nServerGuid: %4%n%nFrom FSCTL_VALIDATE_NEGOTIATE_INFO response:%nDialect: %5%nSecurityMode: %6%nCapabilities: %7%nServerGuid: %8%n%nGuidance:%nThe client successfully negotiated SMB dialect, security mode, capabilities and server GUID with the server, but the validation of these values then failed after connecting to a share. This may be due to a "man-in-the-middle" compromise attempt.\r\n
0xb0007925 | The signing validation failed.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007926 | The client received an unencrypted message when encryption was expected.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007927 | Failed to decrypt an encrypted SMB message.%n%nError:%7%n%nServer name: %6%nSession ID:%3%n%nGuidance:%nThe client received an encrypted SMB message but cannot decrypt the data. This typically means that the communication came from a previous session that no longer exists. The encryption header may also have been damaged or tampered with on the network between the client and server.\r\n
0xb0007928 | The SMB Signing registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:1%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:0%n%nGuidance:%nEven though you can disable, enable, or require SMB Signing, the negotiation rules changed starting with SMB2 and not all combinations operate like SMB1.%n%nThe effective behavior for SMB2/SMB3 is:%nClient Required and Server Required = Signed%nClient Not Required and Server Required = Signed%nServer Required and Client Not Required = Signed%nServer Not Required and Client Not Required = Not Signed%n%nWhen requiring SMB Encryption, SMB Signing is not used, regardless of settings. SMB Encryption implicitly provides the same integrity guarantees as SMB Signing.\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xb0027793 | Failed to reconnect a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027794 | Failed to reconnect a resilient handle.%n%nError: %7%n%nFileId: %2:%3%nPath: %10%12%n%nReason: %8.%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA resilient handle provides guarantees to applications requesting it. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027855 | The client lost its session to the server.%n%nError: %1%n%nServer name: %5%nSession ID: %2%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30806 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027856 | The client re-established its session to the server.%n%nServer name: %5%nServer address: %7%nSession ID: %2%n%nGuidance:%nYou should expect this event if there was a previous event 30805, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027857 | The connection to the share was lost.%n%nError: %1%n%nShare name: %5%nSession ID: %2%nTree ID: %3%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30808 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027858 | The connection to the share was re-established.%n%nShare name: %5%nServer address: %7%nSession ID: %2%nTree ID: %3%n%nGuidance:%nYou should expect this event if there was a previous event 30807, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027863 | The SMB client received a request to move to a different node on a file server cluster.%n%nFile server cluster name: %4%nNew file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer is going to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027864 | The SMB client successfully moved to a different node on a file server cluster.%n%nFile server cluster name: %4%n New file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer successfully moved to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027865 | The SMB client failed to move to a different node on a file server cluster.%n%nError: %1%n%nFile server cluster name: %4%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer failed to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). The attempt to connect to the destination server failed, which is typically due to a network configuration issue. For example, this issue may occur if the destination node's IP address cannot be resolved, if the destination node is behind a firewall, or if there is no network route from the client to the node.\r\n
0xb00278b4 | The handle was created without persistence.%n%nFile ID: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nGuidance:%nThe server supports Continuous Availability (persistent handles) and the request to create the handle succeeded. However, the server did not grant persistence. You should verify that the Resume Key Filter is running on the server and is attached to the target volume.\r\n
0xb00278b8 | The server does not support multichannel.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has disabled multichannel support on the server. This may also be a non-Microsoft file server that does not support multichannel or has multichannel disabled. You can enable SMB Multichannel on the server using this Windows PowerShell cmdlet: Set-SmbServerConfiguration -EnableMultiChannel:$true. This event does not apply to the multichannel settings of SMB client, which are controlled by the Set-SmbClientConfiguration Windows PowerShell cmdlet. Enabling or disabling client multichannel support does not affect server multichannel support.\r\n
0xb00278b9 | The client cannot connect to the server due to a multichannel constraint registry setting.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has configured multichannel support to prevent multichannel on the client. You can configure SMB Multichannel on the client using the Windows PowerShell cmdlets: New-SmbMultichannelConstraint and Remove-SmbMultichannelConstraint.\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | Tdi\r\n
0xd000000b | Wsk\r\n
0xd000000c | Rdma\r\n
0xd000000d | The reason is not specified\r\n
0xd000000e | The server name cannot be resolved\r\n
0xd000000f | Set socket security failed\r\n
0xd0000010 | The connection attempt failed with an IPSec error\r\n
0xd0000011 | The connection attempt failed with a network error\r\n
0xd0000012 | The negotiate validation failed\r\n
0xd0000013 | Disconnected because the exchange expired\r\n
0xd0000014 | Disconnected because there was a network disconnect indication\r\n
0xd0000015 | The connect attempt failed because the unreachable server cache contains the destination server name\r\n
0xd0000016 | An attempt to acquire a credential handle failed\r\n
0xd0000017 | An attempt to initialize a security context failed\r\n
0xd0000018 | The server failed a session setup request\r\n
0xd0000019 | The server denied the share connect request\r\n
0xd000001a | The validate negotiate FSCTL request failed\r\n
0xd000001b | Failed to reconnect the handle\r\n
0xd000001c | The server denied the create request\r\n
0xd000001d | The request was canceled by the client\r\n
0xd000001e | The connection object was suspended by the client\r\n
0xd000001f | Negotiate\r\n
0xd0000020 | Session setup\r\n
0xd0000021 | Logoff\r\n
0xd0000022 | Tree connect\r\n
0xd0000023 | Tree disconnect\r\n
0xd0000024 | Create\r\n
0xd0000025 | Close\r\n
0xd0000026 | Flush\r\n
0xd0000027 | Read\r\n
0xd0000028 | Write\r\n
0xd0000029 | Lock\r\n
0xd000002a | Ioctl\r\n
0xd000002b | Cancel\r\n
0xd000002c | Echo\r\n
0xd000002d | Query directory\r\n
0xd000002e | Change notify\r\n
0xd000002f | Query info\r\n
0xd0000030 | Set info\r\n
0xd0000031 | Oplock break\r\n
0xd0000032 | Create\r\n
0xd0000033 | Close\r\n
0xd0000034 | Read\r\n
0xd0000035 | Write\r\n
0xd0000036 | Query information\r\n
0xd0000037 | Set information\r\n
0xd0000038 | Query EA\r\n
0xd0000039 | Set EA\r\n
0xd000003a | Flush buffers\r\n
0xd000003b | Query volume information\r\n
0xd000003c | Set volume information\r\n
0xd000003d | Directory control\r\n
0xd000003e | File system control\r\n
0xd000003f | Device control\r\n
0xd0000040 | Internal device control\r\n
0xd0000041 | Lock control\r\n
0xd0000042 | Cleanup\r\n
0xd0000043 | Query security\r\n
0xd0000044 | Set security\r\n
0xd0000045 | Query quota information\r\n
0xd0000046 | Set quota information\r\n
0xd0000047 | Internal probe I/O\r\n
0xd0000048 | Symmetric\r\n
0xd0000049 | Asymmetric\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.14393.187

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0x90000007 | Microsoft-Windows-SMBClient/Connectivity\r\n
0x90000008 | Microsoft-Windows-SMBClient/Security\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb0007795 | Failed to open a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb0007850 | The server name cannot be resolved.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe client cannot resolve the server address in DNS or WINS. This issue often manifests immediately after joining a computer to the domain, when the client's DNS registration may not yet have propagated to all DNS servers. You should also expect this event at system startup on a DNS server (such as a domain controller) that points to itself for the primary DNS. You should validate the DNS client settings on this computer using IPCONFIG /ALL and NSLOOKUP.\r\n
0xb0007851 | %1.%n%nError: %2%n%nServer name: %4\r\n
0xb0007853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0007854 | A network connection was disconnected.%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0007859 | A request timed out because there was no response from the server.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThe server is responding over TCP but not over SMB. Ensure the Server service is running and responsive, and the disks do not have high per-IO latency, which makes the disks appear unresponsive to SMB. Also, ensure the server is responsive overall and not paused; for instance, make sure you can log on to it.\r\n
0xb000785a | Added a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TCP/IP. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785b | Deleted a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785c | Added a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TDI. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785d | Deleted a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785e | Witness registration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%nFile server cluster address: %6%n%nGuidance:%nThe client successfully registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb000785f | Witness deregistration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%n%nGuidance:%nThe client successfully de-registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb0007860 | The server failed the negotiate request.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe server does not support any dialect that the client is trying to negotiate, such as the client has SMB2/SMB3 disabled and the server has SMB1 disabled.\r\n
0xb0007861 | Close request failed.%n%nError: %2%n%nPath: %4%6%n%nGuidance:%nA persistent handle (Continuous Availability) or a resilient handle failed to close.\r\n
0xb0007862 | RDMA interfaces are available but the client failed to connect to the server over RDMA transport.%n%nServer name: %2%n%nGuidance:%nBoth client and server have RDMA (SMB Direct) adaptors but there was a problem with the connection and the client had to fall back to using TCP/IP SMB (non-RDMA).\r\n
0xb00078ba | A request on persistent/resilient handle failed because the handle was invalid or it exceeded the timeout.%n%nStatus: %7%n%nType: %1%nPath: %4%6%nRestart count: %2%n%nGuidance:%nAfter retrying a request on a Continuously Available (Persistent) handle or a Resilient handle, the client was unable to reconnect the handle. This event is the result of a handle recovery failure. Review other events for more details.\r\n
0xb00078bb | The SMB Multichannel registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:%2%n%nGuidance:%nYou can configure SMB Multichannel on the client using the Windows PowerShell cmdlet Set-SmbClientConfiguration. Disabling SMB client multichannel support is not a recommended configuration, as it can lead to degraded performance and decreased reliability if one channel or network path fails.\r\n
0xb00078bc | The SMB 3 and SMB 2 driver is not configured with the default start type.%n%nDefault Start Type: DEMAND_START%nConfigured Start Type: DISABLED%n%nGuidance:%nYou should expect this event when disabling SMB2/SMB3 for the client using SC.EXE or editing the Windows registry. Microsoft does not recommend disabling SMB2/SMB3. Disabling SMB2/SMB3 prevents use of features such as SMB Transparent Failover, SMB Scale Out, SMB Multichannel, SMB Direct (RDMA), SMB Encryption, VSS for SMB file shares, and SMB Directory Leasing. SMB provides alternative troubleshooting workarounds to disabling SMB2/SMB3 in most cases.\r\n
0xb00078bd | The client supports SMB Direct (RDMA) and SMB Signing is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Signing. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078be | The client supports SMB Direct (RDMA) and SMB Encryption is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Encryption on the server for shares accessed by this client. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078bf | The Cipher Suite Order group policy setting is invalid.%n%nGuidance:%n%nThis event indicates that an administrator has configured an invalid value for the "Computer Configuration\Administrative Templates\Network\Lanman Workstation\Cipher Suite Order" group policy setting. The client will use the default cipher suite order "%1" until this error is resolved.\r\n
0xb00078c0 | The RequireSecureNegotiate setting has been removed.%n%nRegistry Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters%nRegistry Value: RequireSecureNegotiate%n%nGuidance:%n%nYou should expect this event when an administrator configures the RequireSecureNegotiate setting. Secure negotiate prevents man-in-the-middle attacks against SMB connection establishment. Previous versions of Windows allowed secure negotiate to be disabled. Disabling secure negotiate is no longer allowed. The client removed the setting from the registry. No user action is required.\r\n
0xb0007918 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nSerrver name: %6\r\n
0xb0007919 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nServer name: %6%nPrincipal name: %8\r\n
0xb000791a | The outbound authentication failed using a network token.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThis typically indicates that delegation must be configured for a Kerberos double-hop scenario. If delegation is configured, confirm that the services are configured correctly on the middle-tier server.\r\n
0xb000791b | The LmCompatibilityLevel value is different from the default.%n%nConfigured LM Compatibility Level: %2%nDefault LM Compatibility Level: 3%n%nGuidance:%nLAN Manager (LM) authentication is the protocol used to authenticate Windows clients for network operations. This includes joining a domain, accessing network resources, and authenticating users or computers. This determines which challenge/response authentication protocol is negotiated between the client and the server computers. Specifically, the LM authentication level determines which authentication protocols the client will try to negotiate or the server will accept. The value set for LmCompatibilityLevel determines which challenge/response authentication protocol is used for network logons. This value affects the level of authentication protocol that clients use, the level of session security negotiated, and the level of authentication accepted by servers.%n%nValue (Setting) - Description%n%n0 (Send LM & NTLM responses) - Clients use LM and NTLM authentication and never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n1 (Send LM & NTLM - use NTLMv2 session security if negotiated) - Clients use LM and NTLM authentication, and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n2 (Send NTLM response only) - Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n3 (Send NTLM v2 response only) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n4 (Send NTLMv2 response only/refuse LM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and accept only NTLM and NTLMv2 authentication.%n%n5 (Send NTLM v2 response only/refuse LM & NTLM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM and accept only NTLMv2 authentication.%n%nIncompatibly configured  LmCompatibility levels between a client and server (such as 0 on a client and 5 on a server) prevent access to the server. Non-Microsoft clients and servers also provide these configuration settings.\r\n
0xb0007922 | The SMB client failed to connect to the share.%n%nError: %2%n%nPath: %4%6\r\n
0xb0007924 | The negotiate validation failed.%n%nFrom negotiate response:%nDialect: %1%nSecurityMode: %2%nCapabilities: %3%nServerGuid: %4%n%nFrom FSCTL_VALIDATE_NEGOTIATE_INFO response:%nDialect: %5%nSecurityMode: %6%nCapabilities: %7%nServerGuid: %8%n%nGuidance:%nThe client successfully negotiated SMB dialect, security mode, capabilities and server GUID with the server, but the validation of these values then failed after connecting to a share. This may be due to a "man-in-the-middle" compromise attempt.\r\n
0xb0007925 | The signing validation failed.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007926 | The client received an unencrypted message when encryption was expected.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007927 | Failed to decrypt an encrypted SMB message.%n%nError:%7%n%nServer name: %6%nSession ID:%3%n%nGuidance:%nThe client received an encrypted SMB message but cannot decrypt the data. This typically means that the communication came from a previous session that no longer exists. The encryption header may also have been damaged or tampered with on the network between the client and server.\r\n
0xb0007928 | The SMB Signing registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:1%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:0%n%nGuidance:%nEven though you can disable, enable, or require SMB Signing, the negotiation rules changed starting with SMB2 and not all combinations operate like SMB1.%n%nThe effective behavior for SMB2/SMB3 is:%nClient Required and Server Required = Signed%nClient Not Required and Server Required = Signed%nServer Required and Client Not Required = Signed%nServer Not Required and Client Not Required = Not Signed%n%nWhen requiring SMB Encryption, SMB Signing is not used, regardless of settings. SMB Encryption implicitly provides the same integrity guarantees as SMB Signing.\r\n
0xb0007929 | Rejected an insecure guest logon.%n%nUser name: %2%nServer name: %4%n%nGuidance:%nThis event indicates that the server attempted to log the user on as an unauthenticated guest and was denied by the client. Guest logons do not support standard security features such as signing and encryption. As a result, guest logons are vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792a | The %1 registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:%2%n%nGuidance:%nThis event indicates that an administrator has enabled insecure guest logons. An insecure guest logon occurs when a server logs the user on as an unauthenticated guest, typically in response to an authentication failure. Guest logons do not support standard security features such as signing and encryption. As a result, allowing guest logons makes the client vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792b | Mutual authentication was unexpectedly lost after re-authenticating to %6%nUser %10%nLogonID %4%nStatus %2%n\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xb0027793 | Failed to reconnect a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027794 | Failed to reconnect a resilient handle.%n%nError: %7%n%nFileId: %2:%3%nPath: %10%12%n%nReason: %8.%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA resilient handle provides guarantees to applications requesting it. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027855 | The client lost its session to the server.%n%nError: %1%n%nServer name: %5%nSession ID: %2%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30806 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027856 | The client re-established its session to the server.%n%nServer name: %5%nServer address: %7%nSession ID: %2%n%nGuidance:%nYou should expect this event if there was a previous event 30805, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027857 | The connection to the share was lost.%n%nError: %1%n%nShare name: %5%nSession ID: %2%nTree ID: %3%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30808 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027858 | The connection to the share was re-established.%n%nShare name: %5%nServer address: %7%nSession ID: %2%nTree ID: %3%n%nGuidance:%nYou should expect this event if there was a previous event 30807, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027863 | The SMB client received a request to move to a different node on a file server cluster.%n%nFile server cluster name: %4%nNew file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer is going to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027864 | The SMB client successfully moved to a different node on a file server cluster.%n%nFile server cluster name: %4%n New file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer successfully moved to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027865 | The SMB client failed to move to a different node on a file server cluster.%n%nError: %1%n%nFile server cluster name: %4%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer failed to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). The attempt to connect to the destination server failed, which is typically due to a network configuration issue. For example, this issue may occur if the destination node's IP address cannot be resolved, if the destination node is behind a firewall, or if there is no network route from the client to the node.\r\n
0xb00278b4 | The handle was created without persistence.%n%nFile ID: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nGuidance:%nThe server supports Continuous Availability (persistent handles) and the request to create the handle succeeded. However, the server did not grant persistence. You should verify that the Resume Key Filter is running on the server and is attached to the target volume.\r\n
0xb00278b8 | The server does not support multichannel.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has disabled multichannel support on the server. This may also be a non-Microsoft file server that does not support multichannel or has multichannel disabled. You can enable SMB Multichannel on the server using this Windows PowerShell cmdlet: Set-SmbServerConfiguration -EnableMultiChannel:$true. This event does not apply to the multichannel settings of SMB client, which are controlled by the Set-SmbClientConfiguration Windows PowerShell cmdlet. Enabling or disabling client multichannel support does not affect server multichannel support.\r\n
0xb00278b9 | The client cannot connect to the server due to a multichannel constraint registry setting.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has configured multichannel support to prevent multichannel on the client. You can configure SMB Multichannel on the client using the Windows PowerShell cmdlets: New-SmbMultichannelConstraint and Remove-SmbMultichannelConstraint.\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | Tdi\r\n
0xd000000b | Wsk\r\n
0xd000000c | Rdma\r\n
0xd000000d | The reason is not specified\r\n
0xd000000e | The server name cannot be resolved\r\n
0xd000000f | Set socket security failed\r\n
0xd0000010 | The connection attempt failed with an IPSec error\r\n
0xd0000011 | The connection attempt failed with a network error\r\n
0xd0000012 | The negotiate validation failed\r\n
0xd0000013 | Disconnected because the exchange expired\r\n
0xd0000014 | Disconnected because there was a network disconnect indication\r\n
0xd0000015 | The connect attempt failed because the unreachable server cache contains the destination server name\r\n
0xd0000016 | An attempt to acquire a credential handle failed\r\n
0xd0000017 | An attempt to initialize a security context failed\r\n
0xd0000018 | The server failed a session setup request\r\n
0xd0000019 | The server denied the share connect request\r\n
0xd000001a | The validate negotiate FSCTL request failed\r\n
0xd000001b | Failed to reconnect the handle\r\n
0xd000001c | The server denied the create request\r\n
0xd000001d | The request was canceled by the client\r\n
0xd000001e | The connection object was suspended by the client\r\n
0xd000001f | The connection was disconnected by a user or application\r\n
0xd0000020 | The file handle was closed by the application\r\n
0xd0000021 | Negotiate\r\n
0xd0000022 | Session setup\r\n
0xd0000023 | Logoff\r\n
0xd0000024 | Tree connect\r\n
0xd0000025 | Tree disconnect\r\n
0xd0000026 | Create\r\n
0xd0000027 | Close\r\n
0xd0000028 | Flush\r\n
0xd0000029 | Read\r\n
0xd000002a | Write\r\n
0xd000002b | Lock\r\n
0xd000002c | Ioctl\r\n
0xd000002d | Cancel\r\n
0xd000002e | Echo\r\n
0xd000002f | Query directory\r\n
0xd0000030 | Change notify\r\n
0xd0000031 | Query info\r\n
0xd0000032 | Set info\r\n
0xd0000033 | Oplock break\r\n
0xd0000034 | Create\r\n
0xd0000035 | Close\r\n
0xd0000036 | Read\r\n
0xd0000037 | Write\r\n
0xd0000038 | Query information\r\n
0xd0000039 | Set information\r\n
0xd000003a | Query EA\r\n
0xd000003b | Set EA\r\n
0xd000003c | Flush buffers\r\n
0xd000003d | Query volume information\r\n
0xd000003e | Set volume information\r\n
0xd000003f | Directory control\r\n
0xd0000040 | File system control\r\n
0xd0000041 | Device control\r\n
0xd0000042 | Internal device control\r\n
0xd0000043 | Lock control\r\n
0xd0000044 | Cleanup\r\n
0xd0000045 | Query security\r\n
0xd0000046 | Set security\r\n
0xd0000047 | Query quota information\r\n
0xd0000048 | Set quota information\r\n
0xd0000049 | Internal probe I/O\r\n
0xd000004a | Symmetric\r\n
0xd000004b | Asymmetric\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0x90000007 | Microsoft-Windows-SMBClient/Connectivity\r\n
0x90000008 | Microsoft-Windows-SMBClient/Security\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb0007795 | Failed to open a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb0007850 | The server name cannot be resolved.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe client cannot resolve the server address in DNS or WINS. This issue often manifests immediately after joining a computer to the domain, when the client's DNS registration may not yet have propagated to all DNS servers. You should also expect this event at system startup on a DNS server (such as a domain controller) that points to itself for the primary DNS. You should validate the DNS client settings on this computer using IPCONFIG /ALL and NSLOOKUP.\r\n
0xb0007851 | %1.%n%nError: %2%n%nServer name: %4\r\n
0xb0007853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0007854 | A network connection was disconnected.%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0007859 | A request timed out because there was no response from the server.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThe server is responding over TCP but not over SMB. Ensure the Server service is running and responsive, and the disks do not have high per-IO latency, which makes the disks appear unresponsive to SMB. Also, ensure the server is responsive overall and not paused; for instance, make sure you can log on to it.\r\n
0xb000785a | Added a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TCP/IP. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785b | Deleted a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785c | Added a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TDI. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785d | Deleted a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785e | Witness registration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%nFile server cluster address: %6%n%nGuidance:%nThe client successfully registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb000785f | Witness deregistration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%n%nGuidance:%nThe client successfully de-registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb0007860 | The server failed the negotiate request.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe server does not support any dialect that the client is trying to negotiate, such as the client has SMB2/SMB3 disabled and the server has SMB1 disabled.\r\n
0xb0007861 | Close request failed.%n%nError: %2%n%nPath: %4%6%n%nGuidance:%nA persistent handle (Continuous Availability) or a resilient handle failed to close.\r\n
0xb0007862 | RDMA interfaces are available but the client failed to connect to the server over RDMA transport.%n%nServer name: %2%n%nGuidance:%nBoth client and server have RDMA (SMB Direct) adaptors but there was a problem with the connection and the client had to fall back to using TCP/IP SMB (non-RDMA).\r\n
0xb0007866 | Failed to establish an SMB multichannel network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue. Since the error occurred while trying to connect extra channels, it will not result in an application error. This event is for diagnostics only.\r\n
0xb00078ba | A request on persistent/resilient handle failed because the handle was invalid or it exceeded the timeout.%n%nStatus: %7%n%nType: %1%nPath: %4%6%nRestart count: %2%n%nGuidance:%nAfter retrying a request on a Continuously Available (Persistent) handle or a Resilient handle, the client was unable to reconnect the handle. This event is the result of a handle recovery failure. Review other events for more details.\r\n
0xb00078bb | The SMB Multichannel registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:%2%n%nGuidance:%nYou can configure SMB Multichannel on the client using the Windows PowerShell cmdlet Set-SmbClientConfiguration. Disabling SMB client multichannel support is not a recommended configuration, as it can lead to degraded performance and decreased reliability if one channel or network path fails.\r\n
0xb00078bc | The SMB 3 and SMB 2 driver is not configured with the default start type.%n%nDefault Start Type: DEMAND_START%nConfigured Start Type: DISABLED%n%nGuidance:%nYou should expect this event when disabling SMB2/SMB3 for the client using SC.EXE or editing the Windows registry. Microsoft does not recommend disabling SMB2/SMB3. Disabling SMB2/SMB3 prevents use of features such as SMB Transparent Failover, SMB Scale Out, SMB Multichannel, SMB Direct (RDMA), SMB Encryption, VSS for SMB file shares, and SMB Directory Leasing. SMB provides alternative troubleshooting workarounds to disabling SMB2/SMB3 in most cases.\r\n
0xb00078bd | The client supports SMB Direct (RDMA) and SMB Signing is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Signing. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078be | The client supports SMB Direct (RDMA) and SMB Encryption is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Encryption on the server for shares accessed by this client. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078bf | The Cipher Suite Order group policy setting is invalid.%n%nGuidance:%n%nThis event indicates that an administrator has configured an invalid value for the "Computer Configuration\Administrative Templates\Network\Lanman Workstation\Cipher Suite Order" group policy setting. The client will use the default cipher suite order "%1" until this error is resolved.\r\n
0xb00078c0 | The RequireSecureNegotiate setting has been removed.%n%nRegistry Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters%nRegistry Value: RequireSecureNegotiate%n%nGuidance:%n%nYou should expect this event when an administrator configures the RequireSecureNegotiate setting. Secure negotiate prevents man-in-the-middle attacks against SMB connection establishment. Previous versions of Windows allowed secure negotiate to be disabled. Disabling secure negotiate is no longer allowed. The client removed the setting from the registry. No user action is required.\r\n
0xb0007918 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nSerrver name: %6\r\n
0xb0007919 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nServer name: %6%nPrincipal name: %8\r\n
0xb000791a | The outbound authentication failed using a network token.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThis typically indicates that delegation must be configured for a Kerberos double-hop scenario. If delegation is configured, confirm that the services are configured correctly on the middle-tier server.\r\n
0xb000791b | The LmCompatibilityLevel value is different from the default.%n%nConfigured LM Compatibility Level: %2%nDefault LM Compatibility Level: 3%n%nGuidance:%nLAN Manager (LM) authentication is the protocol used to authenticate Windows clients for network operations. This includes joining a domain, accessing network resources, and authenticating users or computers. This determines which challenge/response authentication protocol is negotiated between the client and the server computers. Specifically, the LM authentication level determines which authentication protocols the client will try to negotiate or the server will accept. The value set for LmCompatibilityLevel determines which challenge/response authentication protocol is used for network logons. This value affects the level of authentication protocol that clients use, the level of session security negotiated, and the level of authentication accepted by servers.%n%nValue (Setting) - Description%n%n0 (Send LM & NTLM responses) - Clients use LM and NTLM authentication and never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n1 (Send LM & NTLM - use NTLMv2 session security if negotiated) - Clients use LM and NTLM authentication, and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n2 (Send NTLM response only) - Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n3 (Send NTLM v2 response only) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n4 (Send NTLMv2 response only/refuse LM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and accept only NTLM and NTLMv2 authentication.%n%n5 (Send NTLM v2 response only/refuse LM & NTLM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM and accept only NTLMv2 authentication.%n%nIncompatibly configured  LmCompatibility levels between a client and server (such as 0 on a client and 5 on a server) prevent access to the server. Non-Microsoft clients and servers also provide these configuration settings.\r\n
0xb0007922 | The SMB client failed to connect to the share.%n%nError: %2%n%nPath: %4%6\r\n
0xb0007924 | The negotiate validation failed.%n%nFrom negotiate response:%nDialect: %1%nSecurityMode: %2%nCapabilities: %3%nServerGuid: %4%n%nFrom FSCTL_VALIDATE_NEGOTIATE_INFO response:%nDialect: %5%nSecurityMode: %6%nCapabilities: %7%nServerGuid: %8%n%nGuidance:%nThe client successfully negotiated SMB dialect, security mode, capabilities and server GUID with the server, but the validation of these values then failed after connecting to a share. This may be due to a "man-in-the-middle" compromise attempt.\r\n
0xb0007925 | The signing validation failed.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007926 | The client received an unencrypted message when encryption was expected.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007927 | Failed to decrypt an encrypted SMB message.%n%nError:%7%n%nServer name: %6%nSession ID:%3%n%nGuidance:%nThe client received an encrypted SMB message but cannot decrypt the data. This typically means that the communication came from a previous session that no longer exists. The encryption header may also have been damaged or tampered with on the network between the client and server.\r\n
0xb0007928 | The SMB Signing registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:1%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:0%n%nGuidance:%nEven though you can disable, enable, or require SMB Signing, the negotiation rules changed starting with SMB2 and not all combinations operate like SMB1.%n%nThe effective behavior for SMB2/SMB3 is:%nClient Required and Server Required = Signed%nClient Not Required and Server Required = Signed%nServer Required and Client Not Required = Signed%nServer Not Required and Client Not Required = Not Signed%n%nWhen requiring SMB Encryption, SMB Signing is not used, regardless of settings. SMB Encryption implicitly provides the same integrity guarantees as SMB Signing.\r\n
0xb0007929 | Rejected an insecure guest logon.%n%nUser name: %2%nServer name: %4%n%nGuidance:%nThis event indicates that the server attempted to log the user on as an unauthenticated guest and was denied by the client. Guest logons do not support standard security features such as signing and encryption. As a result, guest logons are vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792a | The %1 registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:%2%n%nGuidance:%nThis event indicates that an administrator has enabled insecure guest logons. An insecure guest logon occurs when a server logs the user on as an unauthenticated guest, typically in response to an authentication failure. Guest logons do not support standard security features such as signing and encryption. As a result, allowing guest logons makes the client vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792b | Mutual authentication was unexpectedly lost after re-authenticating to %6%nUser %10%nLogonID %4%nStatus %2%n\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xb0027793 | Failed to reconnect a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027794 | Failed to reconnect a resilient handle.%n%nError: %7%n%nFileId: %2:%3%nPath: %10%12%n%nReason: %8.%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA resilient handle provides guarantees to applications requesting it. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0027855 | The client lost its session to the server.%n%nError: %1%n%nServer name: %5%nSession ID: %2%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30806 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027856 | The client re-established its session to the server.%n%nServer name: %5%nServer address: %7%nSession ID: %2%n%nGuidance:%nYou should expect this event if there was a previous event 30805, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027857 | The connection to the share was lost.%n%nError: %1%n%nShare name: %5%nSession ID: %2%nTree ID: %3%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30808 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027858 | The connection to the share was re-established.%n%nShare name: %5%nServer address: %7%nSession ID: %2%nTree ID: %3%n%nGuidance:%nYou should expect this event if there was a previous event 30807, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027863 | The SMB client received a request to move to a different node on a file server cluster.%n%nFile server cluster name: %4%nNew file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer is going to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027864 | The SMB client successfully moved to a different node on a file server cluster.%n%nFile server cluster name: %4%n New file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer successfully moved to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027865 | The SMB client failed to move to a different node on a file server cluster.%n%nError: %1%n%nFile server cluster name: %4%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer failed to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). The attempt to connect to the destination server failed, which is typically due to a network configuration issue. For example, this issue may occur if the destination node's IP address cannot be resolved, if the destination node is behind a firewall, or if there is no network route from the client to the node.\r\n
0xb00278b4 | The handle was created without persistence.%n%nFile ID: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nGuidance:%nThe server supports Continuous Availability (persistent handles) and the request to create the handle succeeded. However, the server did not grant persistence. You should verify that the Resume Key Filter is running on the server and is attached to the target volume.\r\n
0xb00278b8 | The server does not support multichannel.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has disabled multichannel support on the server. This may also be a non-Microsoft file server that does not support multichannel or has multichannel disabled. You can enable SMB Multichannel on the server using this Windows PowerShell cmdlet: Set-SmbServerConfiguration -EnableMultiChannel:$true. This event does not apply to the multichannel settings of SMB client, which are controlled by the Set-SmbClientConfiguration Windows PowerShell cmdlet. Enabling or disabling client multichannel support does not affect server multichannel support.\r\n
0xb00278b9 | The client cannot connect to the server due to a multichannel constraint registry setting.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has configured multichannel support to prevent multichannel on the client. You can configure SMB Multichannel on the client using the Windows PowerShell cmdlets: New-SmbMultichannelConstraint and Remove-SmbMultichannelConstraint.\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | Tdi\r\n
0xd000000b | Wsk\r\n
0xd000000c | Rdma\r\n
0xd000000d | The reason is not specified\r\n
0xd000000e | The server name cannot be resolved\r\n
0xd000000f | Set socket security failed\r\n
0xd0000010 | The connection attempt failed with an IPSec error\r\n
0xd0000011 | The connection attempt failed with a network error\r\n
0xd0000012 | The negotiate validation failed\r\n
0xd0000013 | Disconnected because the exchange expired\r\n
0xd0000014 | Disconnected because there was a network disconnect indication\r\n
0xd0000015 | The connect attempt failed because the unreachable server cache contains the destination server name\r\n
0xd0000016 | An attempt to acquire a credential handle failed\r\n
0xd0000017 | An attempt to initialize a security context failed\r\n
0xd0000018 | The server failed a session setup request\r\n
0xd0000019 | The server denied the share connect request\r\n
0xd000001a | The validate negotiate FSCTL request failed\r\n
0xd000001b | Failed to reconnect the handle\r\n
0xd000001c | The server denied the create request\r\n
0xd000001d | The request was canceled by the client\r\n
0xd000001e | The connection object was suspended by the client\r\n
0xd000001f | The connection was disconnected by a user or application\r\n
0xd0000020 | The file handle was closed by the application\r\n
0xd0000021 | Negotiate\r\n
0xd0000022 | Session setup\r\n
0xd0000023 | Logoff\r\n
0xd0000024 | Tree connect\r\n
0xd0000025 | Tree disconnect\r\n
0xd0000026 | Create\r\n
0xd0000027 | Close\r\n
0xd0000028 | Flush\r\n
0xd0000029 | Read\r\n
0xd000002a | Write\r\n
0xd000002b | Lock\r\n
0xd000002c | Ioctl\r\n
0xd000002d | Cancel\r\n
0xd000002e | Echo\r\n
0xd000002f | Query directory\r\n
0xd0000030 | Change notify\r\n
0xd0000031 | Query info\r\n
0xd0000032 | Set info\r\n
0xd0000033 | Oplock break\r\n
0xd0000034 | Create\r\n
0xd0000035 | Close\r\n
0xd0000036 | Read\r\n
0xd0000037 | Write\r\n
0xd0000038 | Query information\r\n
0xd0000039 | Set information\r\n
0xd000003a | Query EA\r\n
0xd000003b | Set EA\r\n
0xd000003c | Flush buffers\r\n
0xd000003d | Query volume information\r\n
0xd000003e | Set volume information\r\n
0xd000003f | Directory control\r\n
0xd0000040 | File system control\r\n
0xd0000041 | Device control\r\n
0xd0000042 | Internal device control\r\n
0xd0000043 | Lock control\r\n
0xd0000044 | Cleanup\r\n
0xd0000045 | Query security\r\n
0xd0000046 | Set security\r\n
0xd0000047 | Query quota information\r\n
0xd0000048 | Set quota information\r\n
0xd0000049 | Internal probe I/O\r\n
0xd000004a | Symmetric\r\n
0xd000004b | Asymmetric\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0x90000007 | Microsoft-Windows-SMBClient/Connectivity\r\n
0x90000008 | Microsoft-Windows-SMBClient/Security\r\n
0x90000009 | Microsoft-Windows-SMBClient/Audit\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb0007795 | Failed to open a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb0007850 | The server name cannot be resolved.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe client cannot resolve the server address in DNS or WINS. This issue often manifests immediately after joining a computer to the domain, when the client's DNS registration may not yet have propagated to all DNS servers. You should also expect this event at system startup on a DNS server (such as a domain controller) that points to itself for the primary DNS. You should validate the DNS client settings on this computer using IPCONFIG /ALL and NSLOOKUP.\r\n
0xb0007851 | %1.%n%nError: %2%n%nServer name: %4\r\n
0xb0007853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0007854 | A network connection was disconnected.%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0007859 | A request timed out because there was no response from the server.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThe server is responding over TCP but not over SMB. Ensure the Server service is running and responsive, and the disks do not have high per-IO latency, which makes the disks appear unresponsive to SMB. Also, ensure the server is responsive overall and not paused; for instance, make sure you can log on to it.\r\n
0xb000785a | Added a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TCP/IP. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785b | Deleted a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785c | Added a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TDI. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785d | Deleted a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785e | Witness registration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%nFile server cluster address: %6%n%nGuidance:%nThe client successfully registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb000785f | Witness deregistration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%n%nGuidance:%nThe client successfully de-registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb0007860 | The server failed the negotiate request.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe server does not support any dialect that the client is trying to negotiate, such as the client has SMB2/SMB3 disabled and the server has SMB1 disabled.\r\n
0xb0007861 | Close request failed.%n%nError: %2%n%nPath: %4%6%n%nGuidance:%nA persistent handle (Continuous Availability) or a resilient handle failed to close.\r\n
0xb0007862 | RDMA interfaces are available but the client failed to connect to the server over RDMA transport.%n%nServer name: %2%n%nGuidance:%nBoth client and server have RDMA (SMB Direct) adaptors but there was a problem with the connection and the client had to fall back to using TCP/IP SMB (non-RDMA).\r\n
0xb0007866 | Failed to establish an SMB multichannel network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue. Since the error occurred while trying to connect extra channels, it will not result in an application error. This event is for diagnostics only.\r\n
0xb00078ba | A request on persistent/resilient handle failed because the handle was invalid or it exceeded the timeout.%n%nStatus: %7%n%nType: %1%nPath: %4%6%nRestart count: %2%n%nGuidance:%nAfter retrying a request on a Continuously Available (Persistent) handle or a Resilient handle, the client was unable to reconnect the handle. This event is the result of a handle recovery failure. Review other events for more details.\r\n
0xb00078bb | The SMB Multichannel registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:%2%n%nGuidance:%nYou can configure SMB Multichannel on the client using the Windows PowerShell cmdlet Set-SmbClientConfiguration. Disabling SMB client multichannel support is not a recommended configuration, as it can lead to degraded performance and decreased reliability if one channel or network path fails.\r\n
0xb00078bc | The SMB 3 and SMB 2 driver is not configured with the default start type.%n%nDefault Start Type: DEMAND_START%nConfigured Start Type: DISABLED%n%nGuidance:%nYou should expect this event when disabling SMB2/SMB3 for the client using SC.EXE or editing the Windows registry. Microsoft does not recommend disabling SMB2/SMB3. Disabling SMB2/SMB3 prevents use of features such as SMB Transparent Failover, SMB Scale Out, SMB Multichannel, SMB Direct (RDMA), SMB Encryption, VSS for SMB file shares, and SMB Directory Leasing. SMB provides alternative troubleshooting workarounds to disabling SMB2/SMB3 in most cases.\r\n
0xb00078bd | The client supports SMB Direct (RDMA) and SMB Signing is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Signing. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078be | The client supports SMB Direct (RDMA) and SMB Encryption is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Encryption on the server for shares accessed by this client. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078bf | The Cipher Suite Order group policy setting is invalid.%n%nGuidance:%n%nThis event indicates that an administrator has configured an invalid value for the "Computer Configuration\Administrative Templates\Network\Lanman Workstation\Cipher Suite Order" group policy setting. The client will use the default cipher suite order "%1" until this error is resolved.\r\n
0xb00078c0 | The RequireSecureNegotiate setting has been removed.%n%nRegistry Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters%nRegistry Value: RequireSecureNegotiate%n%nGuidance:%n%nYou should expect this event when an administrator configures the RequireSecureNegotiate setting. Secure negotiate prevents man-in-the-middle attacks against SMB connection establishment. Previous versions of Windows allowed secure negotiate to be disabled. Disabling secure negotiate is no longer allowed. The client removed the setting from the registry. No user action is required.\r\n
0xb0007918 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nSerrver name: %6\r\n
0xb0007919 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nServer name: %6%nPrincipal name: %8\r\n
0xb000791a | The outbound authentication failed using a network token.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThis typically indicates that delegation must be configured for a Kerberos double-hop scenario. If delegation is configured, confirm that the services are configured correctly on the middle-tier server.\r\n
0xb000791b | The LmCompatibilityLevel value is different from the default.%n%nConfigured LM Compatibility Level: %2%nDefault LM Compatibility Level: 3%n%nGuidance:%nLAN Manager (LM) authentication is the protocol used to authenticate Windows clients for network operations. This includes joining a domain, accessing network resources, and authenticating users or computers. This determines which challenge/response authentication protocol is negotiated between the client and the server computers. Specifically, the LM authentication level determines which authentication protocols the client will try to negotiate or the server will accept. The value set for LmCompatibilityLevel determines which challenge/response authentication protocol is used for network logons. This value affects the level of authentication protocol that clients use, the level of session security negotiated, and the level of authentication accepted by servers.%n%nValue (Setting) - Description%n%n0 (Send LM & NTLM responses) - Clients use LM and NTLM authentication and never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n1 (Send LM & NTLM - use NTLMv2 session security if negotiated) - Clients use LM and NTLM authentication, and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n2 (Send NTLM response only) - Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n3 (Send NTLM v2 response only) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n4 (Send NTLMv2 response only/refuse LM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and accept only NTLM and NTLMv2 authentication.%n%n5 (Send NTLM v2 response only/refuse LM & NTLM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM and accept only NTLMv2 authentication.%n%nIncompatibly configured  LmCompatibility levels between a client and server (such as 0 on a client and 5 on a server) prevent access to the server. Non-Microsoft clients and servers also provide these configuration settings.\r\n
0xb0007922 | The SMB client failed to connect to the share.%n%nError: %2%n%nPath: %4%6\r\n
0xb0007924 | The negotiate validation failed.%n%nFrom negotiate response:%nDialect: %1%nSecurityMode: %2%nCapabilities: %3%nServerGuid: %4%n%nFrom FSCTL_VALIDATE_NEGOTIATE_INFO response:%nDialect: %5%nSecurityMode: %6%nCapabilities: %7%nServerGuid: %8%n%nGuidance:%nThe client successfully negotiated SMB dialect, security mode, capabilities and server GUID with the server, but the validation of these values then failed after connecting to a share. This may be due to a "man-in-the-middle" compromise attempt.\r\n
0xb0007925 | The signing validation failed.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.%n%nPacketFragment:%9\r\n
0xb0007926 | The client received an unencrypted message when encryption was expected.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007927 | Failed to decrypt an encrypted SMB message.%n%nError:%7%n%nServer name: %6%nSession ID:%3%n%nGuidance:%nThe client received an encrypted SMB message but cannot decrypt the data. This typically means that the communication came from a previous session that no longer exists. The encryption header may also have been damaged or tampered with on the network between the client and server.\r\n
0xb0007928 | The SMB Signing registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:1%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:0%n%nGuidance:%nEven though you can disable, enable, or require SMB Signing, the negotiation rules changed starting with SMB2 and not all combinations operate like SMB1.%n%nThe effective behavior for SMB2/SMB3 is:%nClient Required and Server Required = Signed%nClient Not Required and Server Required = Signed%nServer Required and Client Not Required = Signed%nServer Not Required and Client Not Required = Not Signed%n%nWhen requiring SMB Encryption, SMB Signing is not used, regardless of settings. SMB Encryption implicitly provides the same integrity guarantees as SMB Signing.\r\n
0xb0007929 | Rejected an insecure guest logon.%n%nUser name: %2%nServer name: %4%n%nGuidance:%nThis event indicates that the server attempted to log the user on as an unauthenticated guest and was denied by the client. Guest logons do not support standard security features such as signing and encryption. As a result, guest logons are vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792a | The %1 registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:%2%n%nGuidance:%nThis event indicates that an administrator has enabled insecure guest logons. An insecure guest logon occurs when a server logs the user on as an unauthenticated guest, typically in response to an authentication failure. Guest logons do not support standard security features such as signing and encryption. As a result, allowing guest logons makes the client vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792b | Mutual authentication was unexpectedly lost after re-authenticating to %6%nUser %8%nLogonID %4%nStatus %2%n AuthProtocol Old %9  New %10%nMutualAuthState Old %11 New %12%nClustered %13%n\r\n
0xb0007d00 | SMB1 negotiate response received from remote device when SMB1 cannot be negotiated by the local computer. %n%nDialect: %1%n%n Server name: %3%n%n Guidance:%nThe client has SMB1 disabled or uninstalled. For more information: https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d02 | The local computer received an SMB1 negotiate response.%n%nDialect: %1%n%n SecurityMode %2 Server name: %3%n%n Guidance:%n SMB1 is deprecated and should not be installed nor enabled. For more information, see https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xb0027793 | Failed to reconnect a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027794 | Failed to reconnect a resilient handle.%n%nError: %7%n%nFileId: %2:%3%nPath: %10%12%n%nReason: %8.%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA resilient handle provides guarantees to applications requesting it. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0027855 | The client lost its session to the server.%n%nError: %1%n%nServer name: %5%nSession ID: %2%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30806 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027856 | The client re-established its session to the server.%n%nServer name: %5%nServer address: %7%nSession ID: %2%n%nGuidance:%nYou should expect this event if there was a previous event 30805, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027857 | The connection to the share was lost.%n%nError: %1%n%nShare name: %5%nSession ID: %2%nTree ID: %3%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30808 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027858 | The connection to the share was re-established.%n%nShare name: %5%nServer address: %7%nSession ID: %2%nTree ID: %3%n%nGuidance:%nYou should expect this event if there was a previous event 30807, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027863 | The SMB client received a request to move to a different node on a file server cluster.%n%nFile server cluster name: %4%nNew file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer is going to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027864 | The SMB client successfully moved to a different node on a file server cluster.%n%nFile server cluster name: %4%n New file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer successfully moved to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027865 | The SMB client failed to move to a different node on a file server cluster.%n%nError: %1%n%nFile server cluster name: %4%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer failed to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). The attempt to connect to the destination server failed, which is typically due to a network configuration issue. For example, this issue may occur if the destination node's IP address cannot be resolved, if the destination node is behind a firewall, or if there is no network route from the client to the node.\r\n
0xb00278b4 | The handle was created without persistence.%n%nFile ID: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nGuidance:%nThe server supports Continuous Availability (persistent handles) and the request to create the handle succeeded. However, the server did not grant persistence. You should verify that the Resume Key Filter is running on the server and is attached to the target volume.\r\n
0xb00278b8 | The server does not support multichannel.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has disabled multichannel support on the server. This may also be a non-Microsoft file server that does not support multichannel or has multichannel disabled. You can enable SMB Multichannel on the server using this Windows PowerShell cmdlet: Set-SmbServerConfiguration -EnableMultiChannel:$true. This event does not apply to the multichannel settings of SMB client, which are controlled by the Set-SmbClientConfiguration Windows PowerShell cmdlet. Enabling or disabling client multichannel support does not affect server multichannel support.\r\n
0xb00278b9 | The client cannot connect to the server due to a multichannel constraint registry setting.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has configured multichannel support to prevent multichannel on the client. You can configure SMB Multichannel on the client using the Windows PowerShell cmdlets: New-SmbMultichannelConstraint and Remove-SmbMultichannelConstraint.\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | Tdi\r\n
0xd000000b | Wsk\r\n
0xd000000c | Rdma\r\n
0xd000000d | The reason is not specified\r\n
0xd000000e | The server name cannot be resolved\r\n
0xd000000f | Set socket security failed\r\n
0xd0000010 | The connection attempt failed with an IPSec error\r\n
0xd0000011 | The connection attempt failed with a network error\r\n
0xd0000012 | The negotiate validation failed\r\n
0xd0000013 | Disconnected because the exchange expired\r\n
0xd0000014 | Disconnected because there was a network disconnect indication\r\n
0xd0000015 | The connect attempt failed because the unreachable server cache contains the destination server name\r\n
0xd0000016 | An attempt to acquire a credential handle failed\r\n
0xd0000017 | An attempt to initialize a security context failed\r\n
0xd0000018 | The server failed a session setup request\r\n
0xd0000019 | The server denied the share connect request\r\n
0xd000001a | The validate negotiate FSCTL request failed\r\n
0xd000001b | Failed to reconnect the handle\r\n
0xd000001c | The server denied the create request\r\n
0xd000001d | The request was canceled by the client\r\n
0xd000001e | The connection object was suspended by the client\r\n
0xd000001f | The connection was disconnected by a user or application\r\n
0xd0000020 | The file handle was closed by the application\r\n
0xd0000021 | Negotiate\r\n
0xd0000022 | Session setup\r\n
0xd0000023 | Logoff\r\n
0xd0000024 | Tree connect\r\n
0xd0000025 | Tree disconnect\r\n
0xd0000026 | Create\r\n
0xd0000027 | Close\r\n
0xd0000028 | Flush\r\n
0xd0000029 | Read\r\n
0xd000002a | Write\r\n
0xd000002b | Lock\r\n
0xd000002c | Ioctl\r\n
0xd000002d | Cancel\r\n
0xd000002e | Echo\r\n
0xd000002f | Query directory\r\n
0xd0000030 | Change notify\r\n
0xd0000031 | Query info\r\n
0xd0000032 | Set info\r\n
0xd0000033 | Oplock break\r\n
0xd0000034 | Create\r\n
0xd0000035 | Close\r\n
0xd0000036 | Read\r\n
0xd0000037 | Write\r\n
0xd0000038 | Query information\r\n
0xd0000039 | Set information\r\n
0xd000003a | Query EA\r\n
0xd000003b | Set EA\r\n
0xd000003c | Flush buffers\r\n
0xd000003d | Query volume information\r\n
0xd000003e | Set volume information\r\n
0xd000003f | Directory control\r\n
0xd0000040 | File system control\r\n
0xd0000041 | Device control\r\n
0xd0000042 | Internal device control\r\n
0xd0000043 | Lock control\r\n
0xd0000044 | Cleanup\r\n
0xd0000045 | Query security\r\n
0xd0000046 | Set security\r\n
0xd0000047 | Query quota information\r\n
0xd0000048 | Set quota information\r\n
0xd0000049 | Internal probe I/O\r\n
0xd000004a | Symmetric\r\n
0xd000004b | Asymmetric\r\n

### 10.0.17134.345

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0x90000007 | Microsoft-Windows-SMBClient/Connectivity\r\n
0x90000008 | Microsoft-Windows-SMBClient/Security\r\n
0x90000009 | Microsoft-Windows-SMBClient/Audit\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb000778c | The local computer didn't received an SMB1 negotiate response in the last 20 minutes.n%nGuidance:%n%nThis event indicates that no attempt was made to contact this computer via the SMB1 protocol. After %1 online days of no SMB1 contact attempts, the SMB1 Client service will automatically uninstall.\r\n
0xb0007795 | Failed to open a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb0007850 | The server name cannot be resolved.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe client cannot resolve the server address in DNS or WINS. This issue often manifests immediately after joining a computer to the domain, when the client's DNS registration may not yet have propagated to all DNS servers. You should also expect this event at system startup on a DNS server (such as a domain controller) that points to itself for the primary DNS. You should validate the DNS client settings on this computer using IPCONFIG /ALL and NSLOOKUP.\r\n
0xb0007851 | %1.%n%nError: %2%n%nServer name: %4\r\n
0xb0007853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0007854 | A network connection was disconnected.%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0007859 | A request timed out because there was no response from the server.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThe server is responding over TCP but not over SMB. Ensure the Server service is running and responsive, and the disks do not have high per-IO latency, which makes the disks appear unresponsive to SMB. Also, ensure the server is responsive overall and not paused; for instance, make sure you can log on to it.\r\n
0xb000785a | Added a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TCP/IP. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785b | Deleted a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785c | Added a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TDI. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785d | Deleted a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785e | Witness registration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%nFile server cluster address: %6%n%nGuidance:%nThe client successfully registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb000785f | Witness deregistration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%n%nGuidance:%nThe client successfully de-registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb0007860 | The server failed the negotiate request.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe server does not support any dialect that the client is trying to negotiate, such as the client has SMB2/SMB3 disabled and the server has SMB1 disabled.\r\n
0xb0007861 | Close request failed.%n%nError: %2%n%nPath: %4%6%n%nGuidance:%nA persistent handle (Continuous Availability) or a resilient handle failed to close.\r\n
0xb0007862 | RDMA interfaces are available but the client failed to connect to the server over RDMA transport.%n%nServer name: %2%n%nGuidance:%nBoth client and server have RDMA (SMB Direct) adaptors but there was a problem with the connection and the client had to fall back to using TCP/IP SMB (non-RDMA).\r\n
0xb0007866 | Failed to establish an SMB multichannel network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue. Since the error occurred while trying to connect extra channels, it will not result in an application error. This event is for diagnostics only.\r\n
0xb00078ba | A request on persistent/resilient handle failed because the handle was invalid or it exceeded the timeout.%n%nStatus: %7%n%nType: %1%nPath: %4%6%nRestart count: %2%n%nGuidance:%nAfter retrying a request on a Continuously Available (Persistent) handle or a Resilient handle, the client was unable to reconnect the handle. This event is the result of a handle recovery failure. Review other events for more details.\r\n
0xb00078bb | The SMB Multichannel registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:%2%n%nGuidance:%nYou can configure SMB Multichannel on the client using the Windows PowerShell cmdlet Set-SmbClientConfiguration. Disabling SMB client multichannel support is not a recommended configuration, as it can lead to degraded performance and decreased reliability if one channel or network path fails.\r\n
0xb00078bc | The SMB 3 and SMB 2 driver is not configured with the default start type.%n%nDefault Start Type: DEMAND_START%nConfigured Start Type: DISABLED%n%nGuidance:%nYou should expect this event when disabling SMB2/SMB3 for the client using SC.EXE or editing the Windows registry. Microsoft does not recommend disabling SMB2/SMB3. Disabling SMB2/SMB3 prevents use of features such as SMB Transparent Failover, SMB Scale Out, SMB Multichannel, SMB Direct (RDMA), SMB Encryption, VSS for SMB file shares, and SMB Directory Leasing. SMB provides alternative troubleshooting workarounds to disabling SMB2/SMB3 in most cases.\r\n
0xb00078bd | The client supports SMB Direct (RDMA) and SMB Signing is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Signing. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078be | The client supports SMB Direct (RDMA) and SMB Encryption is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Encryption on the server for shares accessed by this client. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078bf | The Cipher Suite Order group policy setting is invalid.%n%nGuidance:%n%nThis event indicates that an administrator has configured an invalid value for the "Computer Configuration\Administrative Templates\Network\Lanman Workstation\Cipher Suite Order" group policy setting. The client will use the default cipher suite order "%1" until this error is resolved.\r\n
0xb00078c0 | The RequireSecureNegotiate setting has been removed.%n%nRegistry Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters%nRegistry Value: RequireSecureNegotiate%n%nGuidance:%n%nYou should expect this event when an administrator configures the RequireSecureNegotiate setting. Secure negotiate prevents man-in-the-middle attacks against SMB connection establishment. Previous versions of Windows allowed secure negotiate to be disabled. Disabling secure negotiate is no longer allowed. The client removed the setting from the registry. No user action is required.\r\n
0xb0007918 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nSerrver name: %6\r\n
0xb0007919 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nServer name: %6%nPrincipal name: %8\r\n
0xb000791a | The outbound authentication failed using a network token.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThis typically indicates that delegation must be configured for a Kerberos double-hop scenario. If delegation is configured, confirm that the services are configured correctly on the middle-tier server.\r\n
0xb000791b | The LmCompatibilityLevel value is different from the default.%n%nConfigured LM Compatibility Level: %2%nDefault LM Compatibility Level: 3%n%nGuidance:%nLAN Manager (LM) authentication is the protocol used to authenticate Windows clients for network operations. This includes joining a domain, accessing network resources, and authenticating users or computers. This determines which challenge/response authentication protocol is negotiated between the client and the server computers. Specifically, the LM authentication level determines which authentication protocols the client will try to negotiate or the server will accept. The value set for LmCompatibilityLevel determines which challenge/response authentication protocol is used for network logons. This value affects the level of authentication protocol that clients use, the level of session security negotiated, and the level of authentication accepted by servers.%n%nValue (Setting) - Description%n%n0 (Send LM & NTLM responses) - Clients use LM and NTLM authentication and never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n1 (Send LM & NTLM - use NTLMv2 session security if negotiated) - Clients use LM and NTLM authentication, and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n2 (Send NTLM response only) - Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n3 (Send NTLM v2 response only) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n4 (Send NTLMv2 response only/refuse LM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and accept only NTLM and NTLMv2 authentication.%n%n5 (Send NTLM v2 response only/refuse LM & NTLM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM and accept only NTLMv2 authentication.%n%nIncompatibly configured  LmCompatibility levels between a client and server (such as 0 on a client and 5 on a server) prevent access to the server. Non-Microsoft clients and servers also provide these configuration settings.\r\n
0xb0007922 | The SMB client failed to connect to the share.%n%nError: %2%n%nPath: %4%6\r\n
0xb0007924 | The negotiate validation failed.%n%nFrom negotiate response:%nDialect: %1%nSecurityMode: %2%nCapabilities: %3%nServerGuid: %4%n%nFrom FSCTL_VALIDATE_NEGOTIATE_INFO response:%nDialect: %5%nSecurityMode: %6%nCapabilities: %7%nServerGuid: %8%n%nGuidance:%nThe client successfully negotiated SMB dialect, security mode, capabilities and server GUID with the server, but the validation of these values then failed after connecting to a share. This may be due to a "man-in-the-middle" compromise attempt.\r\n
0xb0007925 | The signing validation failed.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.%n%nPacketFragment:%9\r\n
0xb0007926 | The client received an unencrypted message when encryption was expected.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007927 | Failed to decrypt an encrypted SMB message.%n%nError:%7%n%nServer name: %6%nSession ID:%3%n%nGuidance:%nThe client received an encrypted SMB message but cannot decrypt the data. This typically means that the communication came from a previous session that no longer exists. The encryption header may also have been damaged or tampered with on the network between the client and server.\r\n
0xb0007928 | The SMB Signing registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:1%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:0%n%nGuidance:%nEven though you can disable, enable, or require SMB Signing, the negotiation rules changed starting with SMB2 and not all combinations operate like SMB1.%n%nThe effective behavior for SMB2/SMB3 is:%nClient Required and Server Required = Signed%nClient Not Required and Server Required = Signed%nServer Required and Client Not Required = Signed%nServer Not Required and Client Not Required = Not Signed%n%nWhen requiring SMB Encryption, SMB Signing is not used, regardless of settings. SMB Encryption implicitly provides the same integrity guarantees as SMB Signing.\r\n
0xb0007929 | Rejected an insecure guest logon.%n%nUser name: %2%nServer name: %4%n%nGuidance:%nThis event indicates that the server attempted to log the user on as an unauthenticated guest and was denied by the client. Guest logons do not support standard security features such as signing and encryption. As a result, guest logons are vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792a | The %1 registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:%2%n%nGuidance:%nThis event indicates that an administrator has enabled insecure guest logons. An insecure guest logon occurs when a server logs the user on as an unauthenticated guest, typically in response to an authentication failure. Guest logons do not support standard security features such as signing and encryption. As a result, allowing guest logons makes the client vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792b | Mutual authentication was unexpectedly lost after re-authenticating to %6%nUser %8%nLogonID %4%nStatus %2%n AuthProtocol Old %9  New %10%nMutualAuthState Old %11 New %12%nClustered %13%n\r\n
0xb0007d00 | SMB1 negotiate response received from remote device when SMB1 cannot be negotiated by the local computer. %n%nDialect: %1%n%n Server name: %3%n%n Guidance:%nThe client has SMB1 disabled or uninstalled. For more information: https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d02 | The local computer received an SMB1 negotiate response.%n%nDialect: %1%n%n SecurityMode %2 Server name: %3%n%n Guidance:%n SMB1 is deprecated and should not be installed nor enabled. For more information, see https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d03 | The local computer didn't received an SMB1 negotiate response in the last %1 days.n%nGuidance:%n%nThis event indicates that after detecting no attempts to contact this computer via the SMB1 protocol for %1 online days, the SMB1 Client service was automatically uninstalled.\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xb0027793 | Failed to reconnect a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027794 | Failed to reconnect a resilient handle.%n%nError: %7%n%nFileId: %2:%3%nPath: %10%12%n%nReason: %8.%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA resilient handle provides guarantees to applications requesting it. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0027855 | The client lost its session to the server.%n%nError: %1%n%nServer name: %5%nSession ID: %2%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30806 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027856 | The client re-established its session to the server.%n%nServer name: %5%nServer address: %7%nSession ID: %2%n%nGuidance:%nYou should expect this event if there was a previous event 30805, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027857 | The connection to the share was lost.%n%nError: %1%n%nShare name: %5%nSession ID: %2%nTree ID: %3%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30808 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027858 | The connection to the share was re-established.%n%nShare name: %5%nServer address: %7%nSession ID: %2%nTree ID: %3%n%nGuidance:%nYou should expect this event if there was a previous event 30807, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027863 | The SMB client received a request to move to a different node on a file server cluster.%n%nFile server cluster name: %4%nNew file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer is going to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027864 | The SMB client successfully moved to a different node on a file server cluster.%n%nFile server cluster name: %4%n New file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer successfully moved to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027865 | The SMB client failed to move to a different node on a file server cluster.%n%nError: %1%n%nFile server cluster name: %4%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer failed to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). The attempt to connect to the destination server failed, which is typically due to a network configuration issue. For example, this issue may occur if the destination node's IP address cannot be resolved, if the destination node is behind a firewall, or if there is no network route from the client to the node.\r\n
0xb00278b4 | The handle was created without persistence.%n%nFile ID: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nGuidance:%nThe server supports Continuous Availability (persistent handles) and the request to create the handle succeeded. However, the server did not grant persistence. You should verify that the Resume Key Filter is running on the server and is attached to the target volume.\r\n
0xb00278b8 | The server does not support multichannel.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has disabled multichannel support on the server. This may also be a non-Microsoft file server that does not support multichannel or has multichannel disabled. You can enable SMB Multichannel on the server using this Windows PowerShell cmdlet: Set-SmbServerConfiguration -EnableMultiChannel:$true. This event does not apply to the multichannel settings of SMB client, which are controlled by the Set-SmbClientConfiguration Windows PowerShell cmdlet. Enabling or disabling client multichannel support does not affect server multichannel support.\r\n
0xb00278b9 | The client cannot connect to the server due to a multichannel constraint registry setting.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has configured multichannel support to prevent multichannel on the client. You can configure SMB Multichannel on the client using the Windows PowerShell cmdlets: New-SmbMultichannelConstraint and Remove-SmbMultichannelConstraint.\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | Tdi\r\n
0xd000000b | Wsk\r\n
0xd000000c | Rdma\r\n
0xd000000d | The reason is not specified\r\n
0xd000000e | The server name cannot be resolved\r\n
0xd000000f | Set socket security failed\r\n
0xd0000010 | The connection attempt failed with an IPSec error\r\n
0xd0000011 | The connection attempt failed with a network error\r\n
0xd0000012 | The negotiate validation failed\r\n
0xd0000013 | Disconnected because the exchange expired\r\n
0xd0000014 | Disconnected because there was a network disconnect indication\r\n
0xd0000015 | The connect attempt failed because the unreachable server cache contains the destination server name\r\n
0xd0000016 | An attempt to acquire a credential handle failed\r\n
0xd0000017 | An attempt to initialize a security context failed\r\n
0xd0000018 | The server failed a session setup request\r\n
0xd0000019 | The server denied the share connect request\r\n
0xd000001a | The validate negotiate FSCTL request failed\r\n
0xd000001b | Failed to reconnect the handle\r\n
0xd000001c | The server denied the create request\r\n
0xd000001d | The request was canceled by the client\r\n
0xd000001e | The connection object was suspended by the client\r\n
0xd000001f | The connection was disconnected by a user or application\r\n
0xd0000020 | The file handle was closed by the application\r\n
0xd0000021 | Negotiate\r\n
0xd0000022 | Session setup\r\n
0xd0000023 | Logoff\r\n
0xd0000024 | Tree connect\r\n
0xd0000025 | Tree disconnect\r\n
0xd0000026 | Create\r\n
0xd0000027 | Close\r\n
0xd0000028 | Flush\r\n
0xd0000029 | Read\r\n
0xd000002a | Write\r\n
0xd000002b | Lock\r\n
0xd000002c | Ioctl\r\n
0xd000002d | Cancel\r\n
0xd000002e | Echo\r\n
0xd000002f | Query directory\r\n
0xd0000030 | Change notify\r\n
0xd0000031 | Query info\r\n
0xd0000032 | Set info\r\n
0xd0000033 | Oplock break\r\n
0xd0000034 | Create\r\n
0xd0000035 | Close\r\n
0xd0000036 | Read\r\n
0xd0000037 | Write\r\n
0xd0000038 | Query information\r\n
0xd0000039 | Set information\r\n
0xd000003a | Query EA\r\n
0xd000003b | Set EA\r\n
0xd000003c | Flush buffers\r\n
0xd000003d | Query volume information\r\n
0xd000003e | Set volume information\r\n
0xd000003f | Directory control\r\n
0xd0000040 | File system control\r\n
0xd0000041 | Device control\r\n
0xd0000042 | Internal device control\r\n
0xd0000043 | Lock control\r\n
0xd0000044 | Cleanup\r\n
0xd0000045 | Query security\r\n
0xd0000046 | Set security\r\n
0xd0000047 | Query quota information\r\n
0xd0000048 | Set quota information\r\n
0xd0000049 | Internal probe I/O\r\n
0xd000004a | Symmetric\r\n
0xd000004b | Asymmetric\r\n

### 10.0.17763.292

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0x90000007 | Microsoft-Windows-SMBClient/Connectivity\r\n
0x90000008 | Microsoft-Windows-SMBClient/Security\r\n
0x90000009 | Microsoft-Windows-SMBClient/Audit\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb000778c | The local computer didn't received an SMB1 negotiate response in the last 20 minutes.n%nGuidance:%n%nThis event indicates that no attempt was made to contact this computer via the SMB1 protocol. After %1 online days of no SMB1 contact attempts, the SMB1 Client service will automatically uninstall.\r\n
0xb0007795 | Failed to open a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb0007850 | The server name cannot be resolved.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe client cannot resolve the server address in DNS or WINS. This issue often manifests immediately after joining a computer to the domain, when the client's DNS registration may not yet have propagated to all DNS servers. You should also expect this event at system startup on a DNS server (such as a domain controller) that points to itself for the primary DNS. You should validate the DNS client settings on this computer using IPCONFIG /ALL and NSLOOKUP.\r\n
0xb0007851 | %1.%n%nError: %2%n%nServer name: %4\r\n
0xb0007853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0007854 | A network connection was disconnected.%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0007859 | A request timed out because there was no response from the server.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%nInstance Name: %9%nRetryCount: %10%nElapsedTime(ms): %11%n%nGuidance:%nThe server is responding over TCP but not over SMB. Ensure the Server service is running and responsive, and the disks do not have high per-IO latency, which makes the disks appear unresponsive to SMB. Also, ensure the server is responsive overall and not paused; for instance, make sure you can log on to it.\r\n
0xb000785a | Added a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TCP/IP. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785b | Deleted a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785c | Added a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TDI. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785d | Deleted a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785e | Witness registration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%nFile server cluster address: %6%n%nGuidance:%nThe client successfully registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb000785f | Witness deregistration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%n%nGuidance:%nThe client successfully de-registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb0007860 | The server failed the negotiate request.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe server does not support any dialect that the client is trying to negotiate, such as the client has SMB2/SMB3 disabled and the server has SMB1 disabled.\r\n
0xb0007861 | Close request failed.%n%nError: %2%n%nPath: %4%6%n%nGuidance:%nA persistent handle (Continuous Availability) or a resilient handle failed to close.\r\n
0xb0007862 | RDMA interfaces are available but the client failed to connect to the server over RDMA transport.%n%nServer name: %2%n%nGuidance:%nBoth client and server have RDMA (SMB Direct) adaptors but there was a problem with the connection and the client had to fall back to using TCP/IP SMB (non-RDMA).\r\n
0xb0007866 | Failed to establish an SMB multichannel network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue. Since the error occurred while trying to connect extra channels, it will not result in an application error. This event is for diagnostics only.\r\n
0xb00078ba | A request on persistent/resilient handle failed because the handle was invalid or it exceeded the timeout.%n%nStatus: %7%n%nType: %1%nPath: %4%6%nRestart count: %2%n%nGuidance:%nAfter retrying a request on a Continuously Available (Persistent) handle or a Resilient handle, the client was unable to reconnect the handle. This event is the result of a handle recovery failure. Review other events for more details.\r\n
0xb00078bb | The SMB Multichannel registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:%2%n%nGuidance:%nYou can configure SMB Multichannel on the client using the Windows PowerShell cmdlet Set-SmbClientConfiguration. Disabling SMB client multichannel support is not a recommended configuration, as it can lead to degraded performance and decreased reliability if one channel or network path fails.\r\n
0xb00078bc | The SMB 3 and SMB 2 driver is not configured with the default start type.%n%nDefault Start Type: DEMAND_START%nConfigured Start Type: DISABLED%n%nGuidance:%nYou should expect this event when disabling SMB2/SMB3 for the client using SC.EXE or editing the Windows registry. Microsoft does not recommend disabling SMB2/SMB3. Disabling SMB2/SMB3 prevents use of features such as SMB Transparent Failover, SMB Scale Out, SMB Multichannel, SMB Direct (RDMA), SMB Encryption, VSS for SMB file shares, and SMB Directory Leasing. SMB provides alternative troubleshooting workarounds to disabling SMB2/SMB3 in most cases.\r\n
0xb00078bd | The client supports SMB Direct (RDMA) and SMB Signing is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Signing. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078be | The client supports SMB Direct (RDMA) and SMB Encryption is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Encryption on the server for shares accessed by this client. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078bf | The Cipher Suite Order group policy setting is invalid.%n%nGuidance:%n%nThis event indicates that an administrator has configured an invalid value for the "Computer Configuration\Administrative Templates\Network\Lanman Workstation\Cipher Suite Order" group policy setting. The client will use the default cipher suite order "%1" until this error is resolved.\r\n
0xb00078c0 | The RequireSecureNegotiate setting has been removed.%n%nRegistry Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters%nRegistry Value: RequireSecureNegotiate%n%nGuidance:%n%nYou should expect this event when an administrator configures the RequireSecureNegotiate setting. Secure negotiate prevents man-in-the-middle attacks against SMB connection establishment. Previous versions of Windows allowed secure negotiate to be disabled. Disabling secure negotiate is no longer allowed. The client removed the setting from the registry. No user action is required.\r\n
0xb0007918 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nSerrver name: %6\r\n
0xb0007919 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nServer name: %6%nPrincipal name: %8\r\n
0xb000791a | The outbound authentication failed using a network token.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThis typically indicates that delegation must be configured for a Kerberos double-hop scenario. If delegation is configured, confirm that the services are configured correctly on the middle-tier server.\r\n
0xb000791b | The LmCompatibilityLevel value is different from the default.%n%nConfigured LM Compatibility Level: %2%nDefault LM Compatibility Level: 3%n%nGuidance:%nLAN Manager (LM) authentication is the protocol used to authenticate Windows clients for network operations. This includes joining a domain, accessing network resources, and authenticating users or computers. This determines which challenge/response authentication protocol is negotiated between the client and the server computers. Specifically, the LM authentication level determines which authentication protocols the client will try to negotiate or the server will accept. The value set for LmCompatibilityLevel determines which challenge/response authentication protocol is used for network logons. This value affects the level of authentication protocol that clients use, the level of session security negotiated, and the level of authentication accepted by servers.%n%nValue (Setting) - Description%n%n0 (Send LM & NTLM responses) - Clients use LM and NTLM authentication and never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n1 (Send LM & NTLM - use NTLMv2 session security if negotiated) - Clients use LM and NTLM authentication, and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n2 (Send NTLM response only) - Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n3 (Send NTLM v2 response only) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n4 (Send NTLMv2 response only/refuse LM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and accept only NTLM and NTLMv2 authentication.%n%n5 (Send NTLM v2 response only/refuse LM & NTLM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM and accept only NTLMv2 authentication.%n%nIncompatibly configured  LmCompatibility levels between a client and server (such as 0 on a client and 5 on a server) prevent access to the server. Non-Microsoft clients and servers also provide these configuration settings.\r\n
0xb0007922 | The SMB client failed to connect to the share.%n%nError: %2%n%nPath: %4%6\r\n
0xb0007924 | The negotiate validation failed.%n%nFrom negotiate response:%nDialect: %1%nSecurityMode: %2%nCapabilities: %3%nServerGuid: %4%n%nFrom FSCTL_VALIDATE_NEGOTIATE_INFO response:%nDialect: %5%nSecurityMode: %6%nCapabilities: %7%nServerGuid: %8%n%nGuidance:%nThe client successfully negotiated SMB dialect, security mode, capabilities and server GUID with the server, but the validation of these values then failed after connecting to a share. This may be due to a "man-in-the-middle" compromise attempt.\r\n
0xb0007925 | The signing validation failed.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.%n%nPacketFragment:%9\r\n
0xb0007926 | The client received an unencrypted message when encryption was expected.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%nInstance Name: %9%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007927 | Failed to decrypt an encrypted SMB message.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nInstance Name: %9%n%nGuidance:%nThe client received an encrypted SMB message but cannot decrypt the data. This typically means that the communication came from a previous session that no longer exists. The encryption header may also have been damaged or tampered with on the network between the client and server.\r\n
0xb0007928 | The SMB Signing registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:1%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:0%n%nGuidance:%nEven though you can disable, enable, or require SMB Signing, the negotiation rules changed starting with SMB2 and not all combinations operate like SMB1.%n%nThe effective behavior for SMB2/SMB3 is:%nClient Required and Server Required = Signed%nClient Not Required and Server Required = Signed%nServer Required and Client Not Required = Signed%nServer Not Required and Client Not Required = Not Signed%n%nWhen requiring SMB Encryption, SMB Signing is not used, regardless of settings. SMB Encryption implicitly provides the same integrity guarantees as SMB Signing.\r\n
0xb0007929 | Rejected an insecure guest logon.%n%nUser name: %2%nServer name: %4%n%nGuidance:%nThis event indicates that the server attempted to log the user on as an unauthenticated guest and was denied by the client. Guest logons do not support standard security features such as signing and encryption. As a result, guest logons are vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792a | The %1 registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:%2%n%nGuidance:%nThis event indicates that an administrator has enabled insecure guest logons. An insecure guest logon occurs when a server logs the user on as an unauthenticated guest, typically in response to an authentication failure. Guest logons do not support standard security features such as signing and encryption. As a result, allowing guest logons makes the client vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792b | Mutual authentication was unexpectedly lost after re-authenticating to %6%nUser %8%nLogonID %4%nStatus %2%n AuthProtocol Old %9  New %10%nMutualAuthState Old %11 New %12%nClustered %13%n\r\n
0xb0007d00 | SMB1 negotiate response received from remote device when SMB1 cannot be negotiated by the local computer. %n%nDialect: %1%n%n Server name: %3%n%n Guidance:%nThe client has SMB1 disabled or uninstalled. For more information: https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d02 | The local computer received an SMB1 negotiate response.%n%nDialect: %1%n%n SecurityMode %3%n%n Server name: %5%n%n Guidance:%n SMB1 is deprecated and should not be installed nor enabled. For more information, see https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d03 | The local computer didn't received an SMB1 negotiate response in the last %1 days.n%nGuidance:%n%nThis event indicates that after detecting no attempts to contact this computer via the SMB1 protocol for %1 online days, the SMB1 Client service was automatically uninstalled.\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xb0027793 | Failed to reconnect a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027794 | Failed to reconnect a resilient handle.%n%nError: %7%n%nFileId: %2:%3%nPath: %10%12%n%nReason: %8.%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA resilient handle provides guarantees to applications requesting it. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0027855 | The client lost its session to the server.%n%nError: %1%n%nServer name: %5%nSession ID: %2%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30806 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027856 | The client re-established its session to the server.%n%nServer name: %5%nServer address: %7%nSession ID: %2%n%nGuidance:%nYou should expect this event if there was a previous event 30805, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027857 | The connection to the share was lost.%n%nError: %1%n%nShare name: %5%nSession ID: %2%nTree ID: %3%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30808 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027858 | The connection to the share was re-established.%n%nShare name: %5%nServer address: %7%nSession ID: %2%nTree ID: %3%n%nGuidance:%nYou should expect this event if there was a previous event 30807, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027863 | The SMB client received a request to move to a different node on a file server cluster.%n%nFile server cluster name: %4%nNew file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer is going to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027864 | The SMB client successfully moved to a different node on a file server cluster.%n%nFile server cluster name: %4%n New file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer successfully moved to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027865 | The SMB client failed to move to a different node on a file server cluster.%n%nError: %1%n%nFile server cluster name: %4%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer failed to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). The attempt to connect to the destination server failed, which is typically due to a network configuration issue. For example, this issue may occur if the destination node's IP address cannot be resolved, if the destination node is behind a firewall, or if there is no network route from the client to the node.\r\n
0xb0027867 | The connection was terminated due to one or more IO request timeouts.%n%nError: %2%n%nName: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or the storage stack on the remote server. IO operations were not completed within the allotted time. The application may not see this failure because IOs are usually retried on a different connection. This event is for diagnostics only.\r\n
0xb00278b4 | The handle was created without persistence.%n%nFile ID: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nGuidance:%nThe server supports Continuous Availability (persistent handles) and the request to create the handle succeeded. However, the server did not grant persistence. You should verify that the Resume Key Filter is running on the server and is attached to the target volume.\r\n
0xb00278b8 | The server does not support multichannel.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has disabled multichannel support on the server. This may also be a non-Microsoft file server that does not support multichannel or has multichannel disabled. You can enable SMB Multichannel on the server using this Windows PowerShell cmdlet: Set-SmbServerConfiguration -EnableMultiChannel:$true. This event does not apply to the multichannel settings of SMB client, which are controlled by the Set-SmbClientConfiguration Windows PowerShell cmdlet. Enabling or disabling client multichannel support does not affect server multichannel support.\r\n
0xb00278b9 | The client cannot connect to the server due to a multichannel constraint registry setting.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has configured multichannel support to prevent multichannel on the client. You can configure SMB Multichannel on the client using the Windows PowerShell cmdlets: New-SmbMultichannelConstraint and Remove-SmbMultichannelConstraint.\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | Tdi\r\n
0xd000000b | Wsk\r\n
0xd000000c | Rdma\r\n
0xd000000d | VMBUS\r\n
0xd000000e | The reason is not specified\r\n
0xd000000f | The server name cannot be resolved\r\n
0xd0000010 | Set socket security failed\r\n
0xd0000011 | The connection attempt failed with an IPSec error\r\n
0xd0000012 | The connection attempt failed with a network error\r\n
0xd0000013 | The negotiate validation failed\r\n
0xd0000014 | Disconnected because the exchange expired\r\n
0xd0000015 | Disconnected because there was a network disconnect indication\r\n
0xd0000016 | The connect attempt failed because the unreachable server cache contains the destination server name\r\n
0xd0000017 | An attempt to acquire a credential handle failed\r\n
0xd0000018 | An attempt to initialize a security context failed\r\n
0xd0000019 | The server failed a session setup request\r\n
0xd000001a | The server denied the share connect request\r\n
0xd000001b | The validate negotiate FSCTL request failed\r\n
0xd000001c | Failed to reconnect the handle\r\n
0xd000001d | The server denied the create request\r\n
0xd000001e | The request was canceled by the client\r\n
0xd000001f | The connection object was suspended by the client\r\n
0xd0000020 | The connection was disconnected by a user or application\r\n
0xd0000021 | The file handle was closed by the application\r\n
0xd0000022 | Negotiate\r\n
0xd0000023 | Session setup\r\n
0xd0000024 | Logoff\r\n
0xd0000025 | Tree connect\r\n
0xd0000026 | Tree disconnect\r\n
0xd0000027 | Create\r\n
0xd0000028 | Close\r\n
0xd0000029 | Flush\r\n
0xd000002a | Read\r\n
0xd000002b | Write\r\n
0xd000002c | Lock\r\n
0xd000002d | Ioctl\r\n
0xd000002e | Cancel\r\n
0xd000002f | Echo\r\n
0xd0000030 | Query directory\r\n
0xd0000031 | Change notify\r\n
0xd0000032 | Query info\r\n
0xd0000033 | Set info\r\n
0xd0000034 | Oplock break\r\n
0xd0000035 | Create\r\n
0xd0000036 | Close\r\n
0xd0000037 | Read\r\n
0xd0000038 | Write\r\n
0xd0000039 | Query information\r\n
0xd000003a | Set information\r\n
0xd000003b | Query EA\r\n
0xd000003c | Set EA\r\n
0xd000003d | Flush buffers\r\n
0xd000003e | Query volume information\r\n
0xd000003f | Set volume information\r\n
0xd0000040 | Directory control\r\n
0xd0000041 | File system control\r\n
0xd0000042 | Device control\r\n
0xd0000043 | Internal device control\r\n
0xd0000044 | Lock control\r\n
0xd0000045 | Cleanup\r\n
0xd0000046 | Query security\r\n
0xd0000047 | Set security\r\n
0xd0000048 | Query quota information\r\n
0xd0000049 | Set quota information\r\n
0xd000004a | Internal probe I/O\r\n
0xd000004b | Symmetric\r\n
0xd000004c | Asymmetric\r\n

### 10.0.18362.1, 10.0.18362.900

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0x90000007 | Microsoft-Windows-SMBClient/Connectivity\r\n
0x90000008 | Microsoft-Windows-SMBClient/Security\r\n
0x90000009 | Microsoft-Windows-SMBClient/Audit\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb0007601 | Compression requested for file object %3: Status %4\r\n
0xb0007602 | Decompression failed: VcEndpoint %1 Socket %2 ReceiveBuffer %3 ReceiveLength %4 Status %5\r\n
0xb0007603 | Compression failed: VcEndpoint %1 Socket %2 SendBuffer %3 SendLength %4 Status %5\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb000778c | The local computer didn't received an SMB1 negotiate response in the last 20 minutes.n%nGuidance:%n%nThis event indicates that no attempt was made to contact this computer via the SMB1 protocol. After %1 online days of no SMB1 contact attempts, the SMB1 Client service will automatically uninstall.\r\n
0xb0007795 | Failed to open a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb0007850 | The server name cannot be resolved.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe client cannot resolve the server address in DNS or WINS. This issue often manifests immediately after joining a computer to the domain, when the client's DNS registration may not yet have propagated to all DNS servers. You should also expect this event at system startup on a DNS server (such as a domain controller) that points to itself for the primary DNS. You should validate the DNS client settings on this computer using IPCONFIG /ALL and NSLOOKUP.\r\n
0xb0007851 | %1.%n%nError: %2%n%nServer name: %4\r\n
0xb0007853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0007854 | A network connection was disconnected.%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0007859 | A request timed out because there was no response from the server.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%nInstance Name: %9%nRetryCount: %10%nElapsedTime(ms): %11%n%nGuidance:%nThe server is responding over TCP but not over SMB. Ensure the Server service is running and responsive, and the disks do not have high per-IO latency, which makes the disks appear unresponsive to SMB. Also, ensure the server is responsive overall and not paused; for instance, make sure you can log on to it.\r\n
0xb000785a | Added a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TCP/IP. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785b | Deleted a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785c | Added a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TDI. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785d | Deleted a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785e | Witness registration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%nFile server cluster address: %6%n%nGuidance:%nThe client successfully registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb000785f | Witness deregistration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%n%nGuidance:%nThe client successfully de-registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb0007860 | The server failed the negotiate request.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe server does not support any dialect that the client is trying to negotiate, such as the client has SMB2/SMB3 disabled and the server has SMB1 disabled.\r\n
0xb0007861 | Close request failed.%n%nError: %2%n%nPath: %4%6%n%nGuidance:%nA persistent handle (Continuous Availability) or a resilient handle failed to close.\r\n
0xb0007862 | RDMA interfaces are available but the client failed to connect to the server over RDMA transport.%n%nServer name: %2%n%nGuidance:%nBoth client and server have RDMA (SMB Direct) adaptors but there was a problem with the connection and the client had to fall back to using TCP/IP SMB (non-RDMA).\r\n
0xb0007866 | Failed to establish an SMB multichannel network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue. Since the error occurred while trying to connect extra channels, it will not result in an application error. This event is for diagnostics only.\r\n
0xb00078ba | A request on persistent/resilient handle failed because the handle was invalid or it exceeded the timeout.%n%nStatus: %7%n%nType: %1%nPath: %4%6%nRestart count: %2%n%nGuidance:%nAfter retrying a request on a Continuously Available (Persistent) handle or a Resilient handle, the client was unable to reconnect the handle. This event is the result of a handle recovery failure. Review other events for more details.\r\n
0xb00078bb | The SMB Multichannel registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:%2%n%nGuidance:%nYou can configure SMB Multichannel on the client using the Windows PowerShell cmdlet Set-SmbClientConfiguration. Disabling SMB client multichannel support is not a recommended configuration, as it can lead to degraded performance and decreased reliability if one channel or network path fails.\r\n
0xb00078bc | The SMB 3 and SMB 2 driver is not configured with the default start type.%n%nDefault Start Type: DEMAND_START%nConfigured Start Type: DISABLED%n%nGuidance:%nYou should expect this event when disabling SMB2/SMB3 for the client using SC.EXE or editing the Windows registry. Microsoft does not recommend disabling SMB2/SMB3. Disabling SMB2/SMB3 prevents use of features such as SMB Transparent Failover, SMB Scale Out, SMB Multichannel, SMB Direct (RDMA), SMB Encryption, VSS for SMB file shares, and SMB Directory Leasing. SMB provides alternative troubleshooting workarounds to disabling SMB2/SMB3 in most cases.\r\n
0xb00078bd | The client supports SMB Direct (RDMA) and SMB Signing is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Signing. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078be | The client supports SMB Direct (RDMA) and SMB Encryption is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Encryption on the server for shares accessed by this client. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078bf | The Cipher Suite Order group policy setting is invalid.%n%nGuidance:%n%nThis event indicates that an administrator has configured an invalid value for the "Computer Configuration\Administrative Templates\Network\Lanman Workstation\Cipher Suite Order" group policy setting. The client will use the default cipher suite order "%1" until this error is resolved.\r\n
0xb00078c0 | The RequireSecureNegotiate setting has been removed.%n%nRegistry Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters%nRegistry Value: RequireSecureNegotiate%n%nGuidance:%n%nYou should expect this event when an administrator configures the RequireSecureNegotiate setting. Secure negotiate prevents man-in-the-middle attacks against SMB connection establishment. Previous versions of Windows allowed secure negotiate to be disabled. Disabling secure negotiate is no longer allowed. The client removed the setting from the registry. No user action is required.\r\n
0xb0007918 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nSerrver name: %6\r\n
0xb0007919 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nServer name: %6%nPrincipal name: %8\r\n
0xb000791a | The outbound authentication failed using a network token.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThis typically indicates that delegation must be configured for a Kerberos double-hop scenario. If delegation is configured, confirm that the services are configured correctly on the middle-tier server.\r\n
0xb000791b | The LmCompatibilityLevel value is different from the default.%n%nConfigured LM Compatibility Level: %2%nDefault LM Compatibility Level: 3%n%nGuidance:%nLAN Manager (LM) authentication is the protocol used to authenticate Windows clients for network operations. This includes joining a domain, accessing network resources, and authenticating users or computers. This determines which challenge/response authentication protocol is negotiated between the client and the server computers. Specifically, the LM authentication level determines which authentication protocols the client will try to negotiate or the server will accept. The value set for LmCompatibilityLevel determines which challenge/response authentication protocol is used for network logons. This value affects the level of authentication protocol that clients use, the level of session security negotiated, and the level of authentication accepted by servers.%n%nValue (Setting) - Description%n%n0 (Send LM & NTLM responses) - Clients use LM and NTLM authentication and never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n1 (Send LM & NTLM - use NTLMv2 session security if negotiated) - Clients use LM and NTLM authentication, and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n2 (Send NTLM response only) - Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n3 (Send NTLM v2 response only) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n4 (Send NTLMv2 response only/refuse LM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and accept only NTLM and NTLMv2 authentication.%n%n5 (Send NTLM v2 response only/refuse LM & NTLM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM and accept only NTLMv2 authentication.%n%nIncompatibly configured  LmCompatibility levels between a client and server (such as 0 on a client and 5 on a server) prevent access to the server. Non-Microsoft clients and servers also provide these configuration settings.\r\n
0xb0007922 | The SMB client failed to connect to the share.%n%nError: %2%n%nPath: %4%6\r\n
0xb0007924 | The negotiate validation failed.%n%nFrom negotiate response:%nDialect: %1%nSecurityMode: %2%nCapabilities: %3%nServerGuid: %4%n%nFrom FSCTL_VALIDATE_NEGOTIATE_INFO response:%nDialect: %5%nSecurityMode: %6%nCapabilities: %7%nServerGuid: %8%n%nGuidance:%nThe client successfully negotiated SMB dialect, security mode, capabilities and server GUID with the server, but the validation of these values then failed after connecting to a share. This may be due to a "man-in-the-middle" compromise attempt.\r\n
0xb0007925 | The signing validation failed.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.%n%nPacketFragment:%9\r\n
0xb0007926 | The client received an unencrypted message when encryption was expected.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%nInstance Name: %9%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007927 | Failed to decrypt an encrypted SMB message.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nInstance Name: %9%n%nGuidance:%nThe client received an encrypted SMB message but cannot decrypt the data. This typically means that the communication came from a previous session that no longer exists. The encryption header may also have been damaged or tampered with on the network between the client and server.\r\n
0xb0007928 | The SMB Signing registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:1%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:0%n%nGuidance:%nEven though you can disable, enable, or require SMB Signing, the negotiation rules changed starting with SMB2 and not all combinations operate like SMB1.%n%nThe effective behavior for SMB2/SMB3 is:%nClient Required and Server Required = Signed%nClient Not Required and Server Required = Signed%nServer Required and Client Not Required = Signed%nServer Not Required and Client Not Required = Not Signed%n%nWhen requiring SMB Encryption, SMB Signing is not used, regardless of settings. SMB Encryption implicitly provides the same integrity guarantees as SMB Signing.\r\n
0xb0007929 | Rejected an insecure guest logon.%n%nUser name: %2%nServer name: %4%n%nGuidance:%nThis event indicates that the server attempted to log the user on as an unauthenticated guest and was denied by the client. Guest logons do not support standard security features such as signing and encryption. As a result, guest logons are vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792a | The %1 registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:%2%n%nGuidance:%nThis event indicates that an administrator has enabled insecure guest logons. An insecure guest logon occurs when a server logs the user on as an unauthenticated guest, typically in response to an authentication failure. Guest logons do not support standard security features such as signing and encryption. As a result, allowing guest logons makes the client vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792b | Mutual authentication was unexpectedly lost after re-authenticating to %6%nUser %8%nLogonID %4%nStatus %2%n AuthProtocol Old %9  New %10%nMutualAuthState Old %11 New %12%nClustered %13%n\r\n
0xb0007d00 | SMB1 negotiate response received from remote device when SMB1 cannot be negotiated by the local computer. %n%nDialect: %1%n%n Server name: %3%n%n Guidance:%nThe client has SMB1 disabled or uninstalled. For more information: https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d02 | The local computer received an SMB1 negotiate response.%n%nDialect: %1%n%n SecurityMode %3%n%n Server name: %5%n%n Guidance:%n SMB1 is deprecated and should not be installed nor enabled. For more information, see https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d03 | The local computer didn't received an SMB1 negotiate response in the last %1 days.n%nGuidance:%n%nThis event indicates that after detecting no attempts to contact this computer via the SMB1 protocol for %1 online days, the SMB1 Client service was automatically uninstalled.\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xb0017868 | The connection was forcibly disconnected. %n%nError: %2%n%nName: %4%n%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis connection is disconnected to force existing requests to fail back as soon as possible. This is a fast-fail mechanism to allow upper layers to apply their recovery policies as soon as possible. This event is for diagnostics only.\r\n
0xb0017869 | The disconnect state on connection was cleared %n%nName: %3%nInstance name: %5%n%nGuidance:%nAny persistent disconnect state on this connection is cleared. Any new IO will be sent to the server as usual. This event is for diagnostics only.\r\n
0xb0027793 | Failed to reconnect a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027794 | Failed to reconnect a resilient handle.%n%nError: %7%n%nFileId: %2:%3%nPath: %10%12%n%nReason: %8.%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA resilient handle provides guarantees to applications requesting it. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0027855 | The client lost its session to the server.%n%nError: %1%n%nServer name: %5%nSession ID: %2%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30806 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027856 | The client re-established its session to the server.%n%nServer name: %5%nServer address: %7%nSession ID: %2%n%nGuidance:%nYou should expect this event if there was a previous event 30805, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027857 | The connection to the share was lost.%n%nError: %1%n%nShare name: %5%nSession ID: %2%nTree ID: %3%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30808 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027858 | The connection to the share was re-established.%n%nShare name: %5%nServer address: %7%nSession ID: %2%nTree ID: %3%n%nGuidance:%nYou should expect this event if there was a previous event 30807, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027863 | The SMB client received a request to move to a different node on a file server cluster.%n%nFile server cluster name: %4%nNew file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer is going to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027864 | The SMB client successfully moved to a different node on a file server cluster.%n%nFile server cluster name: %4%n New file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer successfully moved to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027865 | The SMB client failed to move to a different node on a file server cluster.%n%nError: %1%n%nFile server cluster name: %4%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer failed to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). The attempt to connect to the destination server failed, which is typically due to a network configuration issue. For example, this issue may occur if the destination node's IP address cannot be resolved, if the destination node is behind a firewall, or if there is no network route from the client to the node.\r\n
0xb0027867 | The connection was terminated due to one or more IO request timeouts.%n%nError: %2%n%nName: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or the storage stack on the remote server. IO operations were not completed within the allotted time. The application may not see this failure because IOs are usually retried on a different connection. This event is for diagnostics only.\r\n
0xb00278b4 | The handle was created without persistence.%n%nFile ID: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nGuidance:%nThe server supports Continuous Availability (persistent handles) and the request to create the handle succeeded. However, the server did not grant persistence. You should verify that the Resume Key Filter is running on the server and is attached to the target volume.\r\n
0xb00278b8 | The server does not support multichannel.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has disabled multichannel support on the server. This may also be a non-Microsoft file server that does not support multichannel or has multichannel disabled. You can enable SMB Multichannel on the server using this Windows PowerShell cmdlet: Set-SmbServerConfiguration -EnableMultiChannel:$true. This event does not apply to the multichannel settings of SMB client, which are controlled by the Set-SmbClientConfiguration Windows PowerShell cmdlet. Enabling or disabling client multichannel support does not affect server multichannel support.\r\n
0xb00278b9 | The client cannot connect to the server due to a multichannel constraint registry setting.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has configured multichannel support to prevent multichannel on the client. You can configure SMB Multichannel on the client using the Windows PowerShell cmdlets: New-SmbMultichannelConstraint and Remove-SmbMultichannelConstraint.\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | Tdi\r\n
0xd000000b | Wsk\r\n
0xd000000c | Rdma\r\n
0xd000000d | VMBUS\r\n
0xd000000e | Smb2DiagReasonNotSpecified\r\n
0xd000000f | Smb2DiagReasonDns\r\n
0xd0000010 | Smb2DiagReasonSetSocketSecurity\r\n
0xd0000011 | Smb2DiagReasonIPSec\r\n
0xd0000012 | Smb2DiagReasonNetworkConnect\r\n
0xd0000013 | Smb2DiagReasonNegotiateValidation\r\n
0xd0000014 | Smb2DiagReasonExchangeExpiry\r\n
0xd0000015 | Smb2DiagReasonDisconnectIndication\r\n
0xd0000016 | Smb2DiagReasonNegativeCache\r\n
0xd0000017 | Smb2DiagReasonConsecutiveSessionSetupFailures\r\n
0xd0000018 | Smb2DiagReasonAcquireCredHandle\r\n
0xd0000019 | Smb2DiagReasonISC\r\n
0xd000001a | Smb2DiagReasonSessionSetupResponse\r\n
0xd000001b | Smb2DiagReasonMADowngrade\r\n
0xd000001c | Smb2DiagReasonCreateSigningKey\r\n
0xd000001d | Smb2DiagReasonRegisterCryptoKeys\r\n
0xd000001e | Smb2DiagReasonQCA\r\n
0xd000001f | Smb2DiagReasonEncryptionOnNullSession\r\n
0xd0000020 | Smb2DiagReasonTreeConnectResponse\r\n
0xd0000021 | Smb2DiagReasonValidateNegotiateFsctl\r\n
0xd0000022 | Smb2DiagReasonHandleReconnect\r\n
0xd0000023 | Smb2DiagReasonCreateResponse\r\n
0xd0000024 | Smb2DiagReasonExchangeCancellation\r\n
0xd0000025 | Smb2DiagReasonExchangeNoBindingObject\r\n
0xd0000026 | Smb2DiagReasonExchangeSendFailure\r\n
0xd0000027 | Smb2DiagReasonObjectSuspended\r\n
0xd0000028 | Smb2DiagReasonUserDisconnect\r\n
0xd0000029 | Smb2DiagReasonHandleClosed\r\n
0xd000002a | Smb2DiagDisconnectReasonReceiveContextAllocation\r\n
0xd000002b | Smb2DiagDisconnectReasonPaddingAllocation\r\n
0xd000002c | Smb2DiagDisconnectReasonExchangeReceiveHandlerError\r\n
0xd000002d | Smb2DiagDisconnectReasonMessageBufferAllocation\r\n
0xd000002e | Smb2DiagDisconnectReasonVcEndpointTornDown\r\n
0xd000002f | Smb2DiagDisconnectReasonMessageSizeReceiveError\r\n
0xd0000030 | Smb2DiagDisconnectReasonMessageSizeTooLargeError\r\n
0xd0000031 | Smb2DiagDisconnectReasonMessageCopyError\r\n
0xd0000032 | Smb2DiagDisconnectReasonVcReceiveHandlerError\r\n
0xd0000033 | Smb2DiagDisconnectReasonVcReceiveError\r\n
0xd0000034 | Negotiate\r\n
0xd0000035 | Session setup\r\n
0xd0000036 | Logoff\r\n
0xd0000037 | Tree connect\r\n
0xd0000038 | Tree disconnect\r\n
0xd0000039 | Create\r\n
0xd000003a | Close\r\n
0xd000003b | Flush\r\n
0xd000003c | Read\r\n
0xd000003d | Write\r\n
0xd000003e | Lock\r\n
0xd000003f | Ioctl\r\n
0xd0000040 | Cancel\r\n
0xd0000041 | Echo\r\n
0xd0000042 | Query directory\r\n
0xd0000043 | Change notify\r\n
0xd0000044 | Query info\r\n
0xd0000045 | Set info\r\n
0xd0000046 | Oplock break\r\n
0xd0000047 | Create\r\n
0xd0000048 | Close\r\n
0xd0000049 | Read\r\n
0xd000004a | Write\r\n
0xd000004b | Query information\r\n
0xd000004c | Set information\r\n
0xd000004d | Query EA\r\n
0xd000004e | Set EA\r\n
0xd000004f | Flush buffers\r\n
0xd0000050 | Query volume information\r\n
0xd0000051 | Set volume information\r\n
0xd0000052 | Directory control\r\n
0xd0000053 | File system control\r\n
0xd0000054 | Device control\r\n
0xd0000055 | Internal device control\r\n
0xd0000056 | Lock control\r\n
0xd0000057 | Cleanup\r\n
0xd0000058 | Query security\r\n
0xd0000059 | Set security\r\n
0xd000005a | Query quota information\r\n
0xd000005b | Set quota information\r\n
0xd000005c | Internal probe I/O\r\n
0xd000005d | Symmetric\r\n
0xd000005e | Asymmetric\r\n

### 10.0.19041.153, 10.0.19041.488

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0x90000007 | Microsoft-Windows-SMBClient/Connectivity\r\n
0x90000008 | Microsoft-Windows-SMBClient/Security\r\n
0x90000009 | Microsoft-Windows-SMBClient/Audit\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb0007601 | Compression requested for file object %3: Status %4\r\n
0xb0007602 | Decompression failed: VcEndpoint %1 Socket %2 ReceiveBuffer %3 ReceiveLength %4 Status %5\r\n
0xb0007603 | Compression failed: VcEndpoint %1 Socket %2 SendBuffer %3 SendLength %4 Status %5\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb000778c | The local computer didn't received an SMB1 negotiate response in the last 20 minutes.n%nGuidance:%n%nThis event indicates that no attempt was made to contact this computer via the SMB1 protocol. After %1 online days of no SMB1 contact attempts, the SMB1 Client service will automatically uninstall.\r\n
0xb0007795 | Failed to open a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb0007850 | The server name cannot be resolved.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe client cannot resolve the server address in DNS or WINS. This issue often manifests immediately after joining a computer to the domain, when the client's DNS registration may not yet have propagated to all DNS servers. You should also expect this event at system startup on a DNS server (such as a domain controller) that points to itself for the primary DNS. You should validate the DNS client settings on this computer using IPCONFIG /ALL and NSLOOKUP.\r\n
0xb0007851 | %1.%n%nError: %2%n%nServer name: %4\r\n
0xb0007853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0007854 | A network connection was disconnected.%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0007859 | A request timed out because there was no response from the server.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%nInstance Name: %9%nRetryCount: %10%nElapsedTime(ms): %11%n%nGuidance:%nThe server is responding over TCP but not over SMB. Ensure the Server service is running and responsive, and the disks do not have high per-IO latency, which makes the disks appear unresponsive to SMB. Also, ensure the server is responsive overall and not paused; for instance, make sure you can log on to it.\r\n
0xb000785a | Added a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TCP/IP. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785b | Deleted a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785c | Added a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TDI. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785d | Deleted a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785e | Witness registration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%nFile server cluster address: %6%n%nGuidance:%nThe client successfully registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb000785f | Witness deregistration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%n%nGuidance:%nThe client successfully de-registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb0007860 | The server failed the negotiate request.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe server does not support any dialect that the client is trying to negotiate, such as the client has SMB2/SMB3 disabled and the server has SMB1 disabled.\r\n
0xb0007861 | Close request failed.%n%nError: %2%n%nPath: %4%6%n%nGuidance:%nA persistent handle (Continuous Availability) or a resilient handle failed to close.\r\n
0xb0007862 | RDMA interfaces are available but the client failed to connect to the server over RDMA transport.%n%nServer name: %2%n%nGuidance:%nBoth client and server have RDMA (SMB Direct) adaptors but there was a problem with the connection and the client had to fall back to using TCP/IP SMB (non-RDMA).\r\n
0xb0007866 | Failed to establish an SMB multichannel network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter can also cause this issue. Since the error occurred while trying to connect extra channels, it will not result in an application error. This event is for diagnostics only.\r\n
0xb00078ba | A request on persistent/resilient handle failed because the handle was invalid or it exceeded the timeout.%n%nStatus: %7%n%nType: %1%nPath: %4%6%nRestart count: %2%n%nGuidance:%nAfter retrying a request on a Continuously Available (Persistent) handle or a Resilient handle, the client was unable to reconnect the handle. This event is the result of a handle recovery failure. Review other events for more details.\r\n
0xb00078bb | The SMB Multichannel registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:%2%n%nGuidance:%nYou can configure SMB Multichannel on the client using the Windows PowerShell cmdlet Set-SmbClientConfiguration. Disabling SMB client multichannel support is not a recommended configuration, as it can lead to degraded performance and decreased reliability if one channel or network path fails.\r\n
0xb00078bc | The SMB 3 and SMB 2 driver is not configured with the default start type.%n%nDefault Start Type: DEMAND_START%nConfigured Start Type: DISABLED%n%nGuidance:%nYou should expect this event when disabling SMB2/SMB3 for the client using SC.EXE or editing the Windows registry. Microsoft does not recommend disabling SMB2/SMB3. Disabling SMB2/SMB3 prevents use of features such as SMB Transparent Failover, SMB Scale Out, SMB Multichannel, SMB Direct (RDMA), SMB Encryption, VSS for SMB file shares, and SMB Directory Leasing. SMB provides alternative troubleshooting workarounds to disabling SMB2/SMB3 in most cases.\r\n
0xb00078bd | The client supports SMB Direct (RDMA) and SMB Signing is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Signing. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078be | The client supports SMB Direct (RDMA) and SMB Encryption is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Encryption on the server for shares accessed by this client. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078bf | The Cipher Suite Order group policy setting is invalid.%n%nGuidance:%n%nThis event indicates that an administrator has configured an invalid value for the "Computer Configuration\Administrative Templates\Network\Lanman Workstation\Cipher Suite Order" group policy setting. The client will use the default cipher suite order "%1" until this error is resolved.\r\n
0xb00078c0 | The RequireSecureNegotiate setting has been removed.%n%nRegistry Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters%nRegistry Value: RequireSecureNegotiate%n%nGuidance:%n%nYou should expect this event when an administrator configures the RequireSecureNegotiate setting. Secure negotiate prevents man-in-the-middle attacks against SMB connection establishment. Previous versions of Windows allowed secure negotiate to be disabled. Disabling secure negotiate is no longer allowed. The client removed the setting from the registry. No user action is required.\r\n
0xb0007918 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nSerrver name: %6\r\n
0xb0007919 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nServer name: %6%nPrincipal name: %8\r\n
0xb000791a | The outbound authentication failed using a network token.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThis typically indicates that delegation must be configured for a Kerberos double-hop scenario. If delegation is configured, confirm that the services are configured correctly on the middle-tier server.\r\n
0xb000791b | The LmCompatibilityLevel value is different from the default.%n%nConfigured LM Compatibility Level: %2%nDefault LM Compatibility Level: 3%n%nGuidance:%nLAN Manager (LM) authentication is the protocol used to authenticate Windows clients for network operations. This includes joining a domain, accessing network resources, and authenticating users or computers. This determines which challenge/response authentication protocol is negotiated between the client and the server computers. Specifically, the LM authentication level determines which authentication protocols the client will try to negotiate or the server will accept. The value set for LmCompatibilityLevel determines which challenge/response authentication protocol is used for network logons. This value affects the level of authentication protocol that clients use, the level of session security negotiated, and the level of authentication accepted by servers.%n%nValue (Setting) - Description%n%n0 (Send LM & NTLM responses) - Clients use LM and NTLM authentication and never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n1 (Send LM & NTLM - use NTLMv2 session security if negotiated) - Clients use LM and NTLM authentication, and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n2 (Send NTLM response only) - Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n3 (Send NTLM v2 response only) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n4 (Send NTLMv2 response only/refuse LM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and accept only NTLM and NTLMv2 authentication.%n%n5 (Send NTLM v2 response only/refuse LM & NTLM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM and accept only NTLMv2 authentication.%n%nIncompatibly configured  LmCompatibility levels between a client and server (such as 0 on a client and 5 on a server) prevent access to the server. Non-Microsoft clients and servers also provide these configuration settings.\r\n
0xb0007922 | The SMB client failed to connect to the share.%n%nError: %2%n%nPath: %4%6\r\n
0xb0007924 | The negotiate validation failed.%n%nFrom negotiate response:%nDialect: %1%nSecurityMode: %2%nCapabilities: %3%nServerGuid: %4%n%nFrom FSCTL_VALIDATE_NEGOTIATE_INFO response:%nDialect: %5%nSecurityMode: %6%nCapabilities: %7%nServerGuid: %8%n%nGuidance:%nThe client successfully negotiated SMB dialect, security mode, capabilities and server GUID with the server, but the validation of these values then failed after connecting to a share. This may be due to a "man-in-the-middle" compromise attempt.\r\n
0xb0007925 | The signing validation failed.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.%n%nPacketFragment:%9\r\n
0xb0007926 | The client received an unencrypted message when encryption was expected.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%nInstance Name: %9%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007927 | Failed to decrypt an encrypted SMB message.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nInstance Name: %9%n%nGuidance:%nThe client received an encrypted SMB message but cannot decrypt the data. This typically means that the communication came from a previous session that no longer exists. The encryption header may also have been damaged or tampered with on the network between the client and server.\r\n
0xb0007928 | The SMB Signing registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:1%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:0%n%nGuidance:%nEven though you can disable, enable, or require SMB Signing, the negotiation rules changed starting with SMB2 and not all combinations operate like SMB1.%n%nThe effective behavior for SMB2/SMB3 is:%nClient Required and Server Required = Signed%nClient Not Required and Server Required = Signed%nServer Required and Client Not Required = Signed%nServer Not Required and Client Not Required = Not Signed%n%nWhen requiring SMB Encryption, SMB Signing is not used, regardless of settings. SMB Encryption implicitly provides the same integrity guarantees as SMB Signing.\r\n
0xb0007929 | Rejected an insecure guest logon.%n%nUser name: %2%nServer name: %4%n%nGuidance:%nThis event indicates that the server attempted to log the user on as an unauthenticated guest and was denied by the client. Guest logons do not support standard security features such as signing and encryption. As a result, guest logons are vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792a | The %1 registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:%2%n%nGuidance:%nThis event indicates that an administrator has enabled insecure guest logons. An insecure guest logon occurs when a server logs the user on as an unauthenticated guest, typically in response to an authentication failure. Guest logons do not support standard security features such as signing and encryption. As a result, allowing guest logons makes the client vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792b | Mutual authentication was unexpectedly lost after re-authenticating to %6%nUser %8%nLogonID %4%nStatus %2%n AuthProtocol Old %9  New %10%nMutualAuthState Old %11 New %12%nClustered %13%n\r\n
0xb0007d00 | SMB1 negotiate response received from remote device when SMB1 cannot be negotiated by the local computer. %n%nDialect: %1%n%n Server name: %3%n%n Guidance:%nThe client has SMB1 disabled or uninstalled. For more information: https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d02 | The local computer received an SMB1 negotiate response.%n%nDialect: %1%n%n SecurityMode %3%n%n Server name: %5%n%n Guidance:%n SMB1 is deprecated and should not be installed nor enabled. For more information, see https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d03 | The local computer didn't received an SMB1 negotiate response in the last %1 days.n%nGuidance:%n%nThis event indicates that after detecting no attempts to contact this computer via the SMB1 protocol for %1 online days, the SMB1 Client service was automatically uninstalled.\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xb0017868 | The connection was forcibly disconnected. %n%nError: %2%n%nName: %4%n%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis connection is disconnected to force existing requests to fail back as soon as possible. This is a fast-fail mechanism to allow upper layers to apply their recovery policies as soon as possible. This event is for diagnostics only.\r\n
0xb0017869 | The disconnect state on connection was cleared %n%nName: %3%nInstance name: %5%n%nGuidance:%nAny persistent disconnect state on this connection is cleared. Any new IO will be sent to the server as usual. This event is for diagnostics only.\r\n
0xb00275fb | %5 connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00275fc | %4 connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00275fd | %5 send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00275fe | %6 send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00275ff | %5 receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0027600 | %6 receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb0027793 | Failed to reconnect a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027794 | Failed to reconnect a resilient handle.%n%nError: %7%n%nFileId: %2:%3%nPath: %10%12%n%nReason: %8.%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA resilient handle provides guarantees to applications requesting it. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter can also cause this issue.\r\n
0xb0027854 | A network connection was disconnected.%n%nInstance name: %4%nServer name: %6%nServer address: %8%nConnection type: %9%nInterfaceId: %10%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0027855 | The client lost its session to the server.%n%nError: %1%n%nServer name: %5%nSession ID: %2%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30806 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027856 | The client re-established its session to the server.%n%nServer name: %5%nServer address: %7%nSession ID: %2%n%nGuidance:%nYou should expect this event if there was a previous event 30805, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027857 | The connection to the share was lost.%n%nError: %1%n%nShare name: %5%nSession ID: %2%nTree ID: %3%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30808 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027858 | The connection to the share was re-established.%n%nShare name: %5%nServer address: %7%nSession ID: %2%nTree ID: %3%n%nGuidance:%nYou should expect this event if there was a previous event 30807, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027863 | The SMB client received a request to move to a different node on a file server cluster.%n%nFile server cluster name: %4%nNew file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer is going to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027864 | The SMB client successfully moved to a different node on a file server cluster.%n%nFile server cluster name: %4%n New file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer successfully moved to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027865 | The SMB client failed to move to a different node on a file server cluster.%n%nError: %1%n%nFile server cluster name: %4%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer failed to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). The attempt to connect to the destination server failed, which is typically due to a network configuration issue. For example, this issue may occur if the destination node's IP address cannot be resolved, if the destination node is behind a firewall, or if there is no network route from the client to the node.\r\n
0xb0027867 | The connection was terminated due to one or more IO request timeouts.%n%nError: %2%n%nName: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or the storage stack on the remote server. IO operations were not completed within the allotted time. The application may not see this failure because IOs are usually retried on a different connection. This event is for diagnostics only.\r\n
0xb00278b4 | The handle was created without persistence.%n%nFile ID: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nGuidance:%nThe server supports Continuous Availability (persistent handles) and the request to create the handle succeeded. However, the server did not grant persistence. You should verify that the Resume Key Filter is running on the server and is attached to the target volume.\r\n
0xb00278b8 | The server does not support multichannel.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has disabled multichannel support on the server. This may also be a non-Microsoft file server that does not support multichannel or has multichannel disabled. You can enable SMB Multichannel on the server using this Windows PowerShell cmdlet: Set-SmbServerConfiguration -EnableMultiChannel:$true. This event does not apply to the multichannel settings of SMB client, which are controlled by the Set-SmbClientConfiguration Windows PowerShell cmdlet. Enabling or disabling client multichannel support does not affect server multichannel support.\r\n
0xb00278b9 | The client cannot connect to the server due to a multichannel constraint registry setting.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has configured multichannel support to prevent multichannel on the client. You can configure SMB Multichannel on the client using the Windows PowerShell cmdlets: New-SmbMultichannelConstraint and Remove-SmbMultichannelConstraint.\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | Tdi\r\n
0xd000000b | Wsk\r\n
0xd000000c | Rdma\r\n
0xd000000d | VMBUS\r\n
0xd000000e | Quic\r\n
0xd000000f | Smb2DiagReasonNotSpecified\r\n
0xd0000010 | Smb2DiagReasonDns\r\n
0xd0000011 | Smb2DiagReasonSetSocketSecurity\r\n
0xd0000012 | Smb2DiagReasonIPSec\r\n
0xd0000013 | Smb2DiagReasonNetworkConnect\r\n
0xd0000014 | Smb2DiagReasonNegotiateValidation\r\n
0xd0000015 | Smb2DiagReasonExchangeExpiry\r\n
0xd0000016 | Smb2DiagReasonDisconnectIndication\r\n
0xd0000017 | Smb2DiagReasonNegativeCache\r\n
0xd0000018 | Smb2DiagReasonConsecutiveSessionSetupFailures\r\n
0xd0000019 | Smb2DiagReasonQuicServerCertificateError\r\n
0xd000001a | Smb2DiagReasonQuicServerConfigFailure\r\n
0xd000001b | Smb2DiagReasonAcquireCredHandle\r\n
0xd000001c | Smb2DiagReasonISC\r\n
0xd000001d | Smb2DiagReasonSessionSetupResponse\r\n
0xd000001e | Smb2DiagReasonMADowngrade\r\n
0xd000001f | Smb2DiagReasonCreateSigningKey\r\n
0xd0000020 | Smb2DiagReasonRegisterCryptoKeys\r\n
0xd0000021 | Smb2DiagReasonQCA\r\n
0xd0000022 | Smb2DiagReasonEncryptionOnNullSession\r\n
0xd0000023 | Smb2DiagReasonTreeConnectResponse\r\n
0xd0000024 | Smb2DiagReasonValidateNegotiateFsctl\r\n
0xd0000025 | Smb2DiagReasonHandleReconnect\r\n
0xd0000026 | Smb2DiagReasonCreateResponse\r\n
0xd0000027 | Smb2DiagReasonExchangeCancellation\r\n
0xd0000028 | Smb2DiagReasonExchangeNoBindingObject\r\n
0xd0000029 | Smb2DiagReasonExchangeSendFailure\r\n
0xd000002a | Smb2DiagReasonObjectSuspended\r\n
0xd000002b | Smb2DiagReasonUserDisconnect\r\n
0xd000002c | Smb2DiagReasonHandleClosed\r\n
0xd000002d | Smb2DiagDisconnectReasonReceiveContextAllocation\r\n
0xd000002e | Smb2DiagDisconnectReasonPaddingAllocation\r\n
0xd000002f | Smb2DiagDisconnectReasonExchangeReceiveHandlerError\r\n
0xd0000030 | Smb2DiagDisconnectReasonMessageBufferAllocation\r\n
0xd0000031 | Smb2DiagDisconnectReasonVcEndpointTornDown\r\n
0xd0000032 | Smb2DiagDisconnectReasonMessageSizeReceiveError\r\n
0xd0000033 | Smb2DiagDisconnectReasonMessageSizeTooLargeError\r\n
0xd0000034 | Smb2DiagDisconnectReasonMessageCopyError\r\n
0xd0000035 | Smb2DiagDisconnectReasonVcReceiveHandlerError\r\n
0xd0000036 | Smb2DiagDisconnectReasonVcReceiveError\r\n
0xd0000037 | Negotiate\r\n
0xd0000038 | Session setup\r\n
0xd0000039 | Logoff\r\n
0xd000003a | Tree connect\r\n
0xd000003b | Tree disconnect\r\n
0xd000003c | Create\r\n
0xd000003d | Close\r\n
0xd000003e | Flush\r\n
0xd000003f | Read\r\n
0xd0000040 | Write\r\n
0xd0000041 | Lock\r\n
0xd0000042 | Ioctl\r\n
0xd0000043 | Cancel\r\n
0xd0000044 | Echo\r\n
0xd0000045 | Query directory\r\n
0xd0000046 | Change notify\r\n
0xd0000047 | Query info\r\n
0xd0000048 | Set info\r\n
0xd0000049 | Oplock break\r\n
0xd000004a | Create\r\n
0xd000004b | Close\r\n
0xd000004c | Read\r\n
0xd000004d | Write\r\n
0xd000004e | Query information\r\n
0xd000004f | Set information\r\n
0xd0000050 | Query EA\r\n
0xd0000051 | Set EA\r\n
0xd0000052 | Flush buffers\r\n
0xd0000053 | Query volume information\r\n
0xd0000054 | Set volume information\r\n
0xd0000055 | Directory control\r\n
0xd0000056 | File system control\r\n
0xd0000057 | Device control\r\n
0xd0000058 | Internal device control\r\n
0xd0000059 | Lock control\r\n
0xd000005a | Cleanup\r\n
0xd000005b | Query security\r\n
0xd000005c | Set security\r\n
0xd000005d | Query quota information\r\n
0xd000005e | Set quota information\r\n
0xd000005f | Internal probe I/O\r\n
0xd0000060 | Symmetric\r\n
0xd0000061 | Asymmetric\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x3000000b | Server Error\r\n
0x3000000c | Cached Error\r\n
0x3000000d | Initialize Security Context Error\r\n
0x3000000e | Security Signature Error\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-SMBClient\r\n
0x90000002 | Microsoft-Windows-SMBClient/HelperClassDiagnostic\r\n
0x90000003 | Microsoft-Windows-SMBClient/ObjectStateDiagnostic\r\n
0x90000004 | Microsoft-Windows-SMBClient/Operational\r\n
0x90000005 | Microsoft-Windows-SMBClient/XPerfAnalytic\r\n
0x90000006 | Microsoft-Windows-SMBClient/Diagnostic\r\n
0x90000007 | Microsoft-Windows-SMBClient/Connectivity\r\n
0x90000008 | Microsoft-Windows-SMBClient/Security\r\n
0x90000009 | Microsoft-Windows-SMBClient/Audit\r\n
0xb0000065 | Create SrvCall Error: %1 Location: %2 Context: %3\r\n
0xb00000c9 | Session Setup Error: %1 Location: %2 Context: %3\r\n
0xb000012d | Tree Connect Error: %1 Location: %2 Context: %3\r\n
0xb0000191 | Create VNetRoot Error: %1 Location: %2 Context: %3\r\n
0xb00001f5 | Create File Error: %1 Location: %2 Context: %3\r\n
0xb00007d0 | Packet Fragment (%2 bytes)\r\n
0xb0004e21 | Transitioned to State: %1 Context: %2\r\n
0xb0007597 | SMB exchange suspended: RxContext %1 Exchange %2 ListHead %3\r\n
0xb0007598 | SMB exchange resumed: RxContext %1 Exchange %2 ExchangeState %3 ExchangeStatus %4\r\n
0xb0007599 | SMB buffer context suspended: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759a | SMB buffer context resumed: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759c | SMB Mid window blocked: Window %1 HungSession %2\r\n
0xb000759d | SMB rechunk multi-credit request: BufferCtxt %1 Exchange %2 MidCharge %3 Window %4 CurrentWindowLimit %5 ThrottlingWindowLimit %6 CurrentWindowSize %7\r\n
0xb000759e | SMB initialize Mid window: Server %2 Window %3\r\n
0xb000759f | SMB Mid window state: Window %1 CurrentWindowSize %2 CurrentWindowLimit %3 ThrottlingWindowLimit %4 OldestPendingMid %5 NextAvailableMid %6 CreditsGranted %7\r\n
0xb00075a0 | SMB teardown Mid window: Server %2 Window %3\r\n
0xb00075a1 | SMB copy data completion: Status %1 VcEndpoint %2\r\n
0xb00075a2 | SMB send completion: Status %1 VcEndpoint %2\r\n
0xb00075fb | WSK connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00075fc | WSK connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00075fd | WSK send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00075fe | WSK send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00075ff | WSK receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0007600 | WSK receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb0007601 | Compression requested for file object %3: Status %4\r\n
0xb0007602 | Decompression failed: VcEndpoint %1 Socket %2 ReceiveBuffer %3 ReceiveLength %4 Status %5\r\n
0xb0007603 | Compression failed: VcEndpoint %1 Socket %2 SendBuffer %3 SendLength %4 Status %5\r\n
0xb00076c1 | SMB session expired: SessionEntry %1 ServerName %3\r\n
0xb00076c2 | SMB 3 part SPN reauth: SessionEntry %1 ServiceName %3\r\n
0xb00076c3 | SMB reconnect durable open: Fcb %1 SrvOpen %2\r\n
0xb00076c4 | SMB defer open: Fcb %1 SrvOpen %2\r\n
0xb00076c5 | SMB undefer open: Fcb %1 SrvOpen %2\r\n
0xb00076c6 | SMB send[%1]: [%2] (Mid/Sid/Tid) (%3/%4/%5) MidCharge %6 Creds %7 SendLengh %8 VcEndpoint %9\r\n
0xb00076c7 | SMB receive: [%1] (Mid/Sid/Tid) (%2/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c8 | SMB receive interim: [%1] (Mid/AsyncId/Sid/Tid) (%2/%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076c9 | SMB receive async: [%1] (AsyncId/Sid/Tid) (%3/%4/%5) Creds %6 Status %7 VcEndpoint %8\r\n
0xb00076ca | SMB registry key: %1 = %2\r\n
0xb0007725 | SMB update file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007726 | SMB fetch file info cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007727 | SMB invalidate file info cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007728 | SMB update file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb0007729 | SMB fetch file not found cache: RxContext %1 Fcb %2 FileName %4 Result %5\r\n
0xb000772a | SMB invalidate file not found cache: RxContext %1 Fcb %2 FileName %4\r\n
0xb000772b | SMB populate dir cache: RxContext %1 Fcb %2 DirName %4\r\n
0xb000772c | SMB fetch dir cache: RxContext %1 Fcb %2 FileName %4 Status %5\r\n
0xb0007788 | Session %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb0007789 | Share connection %1 to %6 transitioned from [%2] to [%3] with Status %4\r\n
0xb000778b | Open handle %1 to %10%12 transitioned from [%5] to [%6] with Status %7\r\n
0xb000778c | The local computer didn't received an SMB1 negotiate response in the last 20 minutes.n%nGuidance:%n%nThis event indicates that no attempt was made to contact this computer via the SMB1 protocol. After %1 online days of no SMB1 contact attempts, the SMB1 Client service will automatically uninstall.\r\n
0xb0007795 | Failed to open a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb00077ed | An invalid FSCTL_QUERY_NETWORK_INTERFACE_INFO response was sent by the server %2\r\n
0xb00077ee | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport. Error: %7\r\n
0xb00077ef | The client failed to connect to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport. Error: %7\r\n
0xb00077f0 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over TCP transport successfully\r\n
0xb00077f1 | The client connected to the server %2 from the local IP address %4 to the remote IP address %6 over RDMA transport successfully\r\n
0xb0007850 | The server name cannot be resolved.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe client cannot resolve the server address in DNS or WINS. This issue often manifests immediately after joining a computer to the domain, when the client's DNS registration may not yet have propagated to all DNS servers. You should also expect this event at system startup on a DNS server (such as a domain controller) that points to itself for the primary DNS. You should validate the DNS client settings on this computer using IPCONFIG /ALL and NSLOOKUP.\r\n
0xb0007851 | %1.%n%nError: %2%n%nServer name: %4\r\n
0xb0007853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP, and not with SMB. A firewall that blocks TCP port 445, or TCP port 5445 when using an iWARP RDMA adapter, can also cause this issue.\r\n
0xb0007854 | A network connection was disconnected.%n%nServer name: %4%nServer address: %6%nConnection type: %7%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0007859 | A request timed out because there was no response from the server.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%nInstance Name: %9%nRetryCount: %10%nElapsedTime(ms): %11%n%nGuidance:%nThe server is responding over TCP but not over SMB. Ensure the Server service is running and responsive, and the disks do not have high per-IO latency, which makes the disks appear unresponsive to SMB. Also, ensure the server is responsive overall and not paused; for instance, make sure you can log on to it.\r\n
0xb000785a | Added a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TCP/IP. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785b | Deleted a TCP/IP transport interface.%n%nName: %2%nInterfaceIndex: %3%n%nGuidance:%nA TCP/IP binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785c | Added a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was added to the specified network adapter for the SMB client. The SMB client can now send and receive SMB traffic on this network adapter using TDI. You should expect this event when a computer restarts or when a previously disabled network adaptor is re-enabled. No user action is required.\r\n
0xb000785d | Deleted a TDI transport interface.%n%nName: %2%n%nGuidance:%nA TDI (NetBIOS) binding was removed from the specified network adapter for the SMB client. You should expect this event when a computer shuts down or when a previously enabled network adaptor is disabled. No user action is required.\r\n
0xb000785e | Witness registration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%nFile server cluster address: %6%n%nGuidance:%nThe client successfully registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb000785f | Witness deregistration has completed.%n%nStatus: %1%n%nCluster share name: %4%nCluster share type: %2%n%nGuidance:%nThe client successfully de-registered with the SMB Witness through RPC using TCP (port 135, then an endpoint port above 1023). No action is required.\r\n
0xb0007860 | The server failed the negotiate request.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThe server does not support any dialect that the client is trying to negotiate, such as the client has SMB2/SMB3 disabled and the server has SMB1 disabled.\r\n
0xb0007861 | Close request failed.%n%nError: %2%n%nPath: %4%6%n%nGuidance:%nA persistent handle (Continuous Availability) or a resilient handle failed to close.\r\n
0xb0007862 | RDMA interfaces are available but the client failed to connect to the server over RDMA transport.%n%nServer name: %2%n%nGuidance:%nBoth client and server have RDMA (SMB Direct) adaptors but there was a problem with the connection and the client had to fall back to using TCP/IP SMB (non-RDMA).\r\n
0xb0007866 | Failed to establish an SMB multichannel network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP or QUIC/UDP, and not with SMB. A firewall that blocks TCP port 445 or UDP port 443 or TCP port 5445 when using an iWARP RDMA adapter can also cause this issue. Since the error occurred while trying to connect extra channels, it will not result in an application error. This event is for diagnostics only.\r\n
0xb00078ba | A request on persistent/resilient handle failed because the handle was invalid or it exceeded the timeout.%n%nStatus: %7%n%nType: %1%nPath: %4%6%nRestart count: %2%n%nGuidance:%nAfter retrying a request on a Continuously Available (Persistent) handle or a Resilient handle, the client was unable to reconnect the handle. This event is the result of a handle recovery failure. Review other events for more details.\r\n
0xb00078bb | The SMB Multichannel registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"DisableMultiChannel"=dword:%2%n%nGuidance:%nYou can configure SMB Multichannel on the client using the Windows PowerShell cmdlet Set-SmbClientConfiguration. Disabling SMB client multichannel support is not a recommended configuration, as it can lead to degraded performance and decreased reliability if one channel or network path fails.\r\n
0xb00078bc | The SMB 3 and SMB 2 driver is not configured with the default start type.%n%nDefault Start Type: DEMAND_START%nConfigured Start Type: DISABLED%n%nGuidance:%nYou should expect this event when disabling SMB2/SMB3 for the client using SC.EXE or editing the Windows registry. Microsoft does not recommend disabling SMB2/SMB3. Disabling SMB2/SMB3 prevents use of features such as SMB Transparent Failover, SMB Scale Out, SMB Multichannel, SMB Direct (RDMA), SMB Encryption, VSS for SMB file shares, and SMB Directory Leasing. SMB provides alternative troubleshooting workarounds to disabling SMB2/SMB3 in most cases.\r\n
0xb00078bd | The client supports SMB Direct (RDMA) and SMB Signing is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Signing. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078be | The client supports SMB Direct (RDMA) and SMB Encryption is in use.%n%nShare name: %2%n%nGuidance:%nFor optimal SMB Direct performance, you can disable SMB Encryption on the server for shares accessed by this client. This configuration is less secure and you should only consider this configuration on trustworthy private networks with strict access control.\r\n
0xb00078bf | The Cipher Suite Order group policy setting is invalid.%n%nGuidance:%n%nThis event indicates that an administrator has configured an invalid value for the "Computer Configuration\Administrative Templates\Network\Lanman Workstation\Cipher Suite Order" group policy setting. The client will use the default cipher suite order "%1" until this error is resolved.\r\n
0xb00078c0 | The RequireSecureNegotiate setting has been removed.%n%nRegistry Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters%nRegistry Value: RequireSecureNegotiate%n%nGuidance:%n%nYou should expect this event when an administrator configures the RequireSecureNegotiate setting. Secure negotiate prevents man-in-the-middle attacks against SMB connection establishment. Previous versions of Windows allowed secure negotiate to be disabled. Disabling secure negotiate is no longer allowed. The client removed the setting from the registry. No user action is required.\r\n
0xb0007918 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nSerrver name: %6\r\n
0xb0007919 | %1.%n%nError: %2%n%nSecurity status: %3%nUser name: %10%nLogon ID: %4%nServer name: %6%nPrincipal name: %8\r\n
0xb000791a | The outbound authentication failed using a network token.%n%nError: %2%n%nServer name: %4%n%nGuidance:%nThis typically indicates that delegation must be configured for a Kerberos double-hop scenario. If delegation is configured, confirm that the services are configured correctly on the middle-tier server.\r\n
0xb000791b | The LmCompatibilityLevel value is different from the default.%n%nConfigured LM Compatibility Level: %2%nDefault LM Compatibility Level: 3%n%nGuidance:%nLAN Manager (LM) authentication is the protocol used to authenticate Windows clients for network operations. This includes joining a domain, accessing network resources, and authenticating users or computers. This determines which challenge/response authentication protocol is negotiated between the client and the server computers. Specifically, the LM authentication level determines which authentication protocols the client will try to negotiate or the server will accept. The value set for LmCompatibilityLevel determines which challenge/response authentication protocol is used for network logons. This value affects the level of authentication protocol that clients use, the level of session security negotiated, and the level of authentication accepted by servers.%n%nValue (Setting) - Description%n%n0 (Send LM & NTLM responses) - Clients use LM and NTLM authentication and never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n1 (Send LM & NTLM - use NTLMv2 session security if negotiated) - Clients use LM and NTLM authentication, and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n2 (Send NTLM response only) - Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n3 (Send NTLM v2 response only) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.%n%n4 (Send NTLMv2 response only/refuse LM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and accept only NTLM and NTLMv2 authentication.%n%n5 (Send NTLM v2 response only/refuse LM & NTLM) - Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM and accept only NTLMv2 authentication.%n%nIncompatibly configured  LmCompatibility levels between a client and server (such as 0 on a client and 5 on a server) prevent access to the server. Non-Microsoft clients and servers also provide these configuration settings.\r\n
0xb0007922 | The SMB client failed to connect to the share.%n%nError: %2%n%nPath: %4%6\r\n
0xb0007924 | The negotiate validation failed.%n%nFrom negotiate response:%nDialect: %1%nSecurityMode: %2%nCapabilities: %3%nServerGuid: %4%n%nFrom FSCTL_VALIDATE_NEGOTIATE_INFO response:%nDialect: %5%nSecurityMode: %6%nCapabilities: %7%nServerGuid: %8%n%nGuidance:%nThe client successfully negotiated SMB dialect, security mode, capabilities and server GUID with the server, but the validation of these values then failed after connecting to a share. This may be due to a "man-in-the-middle" compromise attempt.\r\n
0xb0007925 | The signing validation failed.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.%n%nPacketFragment:%9\r\n
0xb0007926 | The client received an unencrypted message when encryption was expected.%n%nServer name: %6%nSession ID:%3%nTree ID:%4%nMessage ID:%2%nCommand: %1%nInstance Name: %9%n%nGuidance:%nThis error indicates that SMB messages are being modified in transit across the network from the server to the client. This may be due to the session ending on the server, a problem with the network, a problem with a third-party SMB server, or a "man-in-the-middle" compromise attempt.\r\n
0xb0007927 | Failed to decrypt an encrypted SMB message.%n%nError:%7%n%nServer name: %6%nSession ID:%3%nInstance Name: %9%n%nGuidance:%nThe client received an encrypted SMB message but cannot decrypt the data. This typically means that the communication came from a previous session that no longer exists. The encryption header may also have been damaged or tampered with on the network between the client and server.\r\n
0xb0007928 | The SMB Signing registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:1%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"EnableSecuritySignature"=dword:0%n%nGuidance:%nEven though you can disable, enable, or require SMB Signing, the negotiation rules changed starting with SMB2 and not all combinations operate like SMB1.%n%nThe effective behavior for SMB2/SMB3 is:%nClient Required and Server Required = Signed%nClient Not Required and Server Required = Signed%nServer Required and Client Not Required = Signed%nServer Not Required and Client Not Required = Not Signed%n%nWhen requiring SMB Encryption, SMB Signing is not used, regardless of settings. SMB Encryption implicitly provides the same integrity guarantees as SMB Signing.\r\n
0xb0007929 | Rejected an insecure guest logon.%n%nUser name: %2%nServer name: %4%n%nGuidance:%nThis event indicates that the server attempted to log the user on as an unauthenticated guest and was denied by the client. Guest logons do not support standard security features such as signing and encryption. As a result, guest logons are vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792a | The %1 registry value is not configured with default settings.%n%nDefault Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:0%nConfigured Registry Value:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"%1"=dword:%2%n%nGuidance:%nThis event indicates that an administrator has enabled insecure guest logons. An insecure guest logon occurs when a server logs the user on as an unauthenticated guest, typically in response to an authentication failure. Guest logons do not support standard security features such as signing and encryption. As a result, allowing guest logons makes the client vulnerable to man-in-the-middle attacks that can expose sensitive data on the network. Windows disables insecure guest logons by default. Microsoft does not recommend enabling insecure guest logons.\r\n
0xb000792b | Mutual authentication was unexpectedly lost after re-authenticating to %6%nUser %8%nLogonID %4%nStatus %2%n AuthProtocol Old %9  New %10%nMutualAuthState Old %11 New %12%nClustered %13%n\r\n
0xb000792c | Session key for connection is weaker than required. Connection will be closed as a result.%n%nServer: %2%nUser: %6%nSession key length: %3%nRequired Session key length: %4%n%nGuidance:%nTo establish a connection with a shorter session key, set the following registry DWORD value name with the value as decimal bits:%n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]%n"MinimumSessionKeyLength"%n%nImportant: If you have configured the 'Network security: Configure encryption types allowed for Kerberos' security policy to prevent use of 256-bit keys but also set the MinimumSessionKeyLength greater than 128 bits, the computer will not be able to make SMB connections. Setting MinimumSessionKeyLength higher than 128 bits will also prevent SMB connections using NTLM.\r\n
0xb0007d00 | SMB1 negotiate response received from remote device when SMB1 cannot be negotiated by the local computer. %n%nDialect: %1%n%n Server name: %3%n%n Guidance:%nThe client has SMB1 disabled or uninstalled. For more information: https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d02 | The local computer received an SMB1 negotiate response.%n%nDialect: %1%n%n SecurityMode %3%n%n Server name: %5%n%n Guidance:%n SMB1 is deprecated and should not be installed nor enabled. For more information, see https://go.microsoft.com/fwlink/?linkid=852747.\r\n
0xb0007d03 | The local computer didn't received an SMB1 negotiate response in the last %1 days.n%nGuidance:%n%nThis event indicates that after detecting no attempts to contact this computer via the SMB1 protocol for %1 online days, the SMB1 Client service was automatically uninstalled.\r\n
0xb0009c40 | Packet (%4 bytes)\r\n
0xb0017868 | The connection was forcibly disconnected. %n%nError: %2%n%nName: %4%n%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis connection is disconnected to force existing requests to fail back as soon as possible. This is a fast-fail mechanism to allow upper layers to apply their recovery policies as soon as possible. This event is for diagnostics only.\r\n
0xb0017869 | The disconnect state on connection was cleared %n%nName: %3%nInstance name: %5%n%nGuidance:%nAny persistent disconnect state on this connection is cleared. Any new IO will be sent to the server as usual. This event is for diagnostics only.\r\n
0xb00275fb | %5 connect: SocketAddress %2 VcEndpoint %3 Socket %4\r\n
0xb00275fc | %4 connect completion: VcEndpoint %1 Socket %2 Status %3\r\n
0xb00275fd | %5 send: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4\r\n
0xb00275fe | %6 send completion: VcEndpoint %1 Socket %2 SendMdl %3 SendLength %4 Status %5\r\n
0xb00275ff | %5 receive: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4\r\n
0xb0027600 | %6 receive completion: VcEndpoint %1 Socket %2 ReceiveMdl %3 ReceiveLength %4 Status %5\r\n
0xb0027793 | Failed to reconnect a persistent handle.%n%nError: %7%n%nFileId: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nReason: %8%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA persistent handle allows transparent failover on Windows File Server clusters. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027794 | Failed to reconnect a resilient handle.%n%nError: %7%n%nFileId: %2:%3%nPath: %10%12%n%nReason: %8.%n%nPrevious reconnect error: %13%nPrevious reconnect reason: %14%n%nGuidance:%nA resilient handle provides guarantees to applications requesting it. This event has many causes and does not always indicate an issue with SMB. Review online documentation for troubleshooting information.\r\n
0xb0027853 | Failed to establish a network connection.%n%nError: %2%n%nServer name: %4%nServer address: %6%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or transport, such as with TCP/IP or QUIC/UDP, and not with SMB. A firewall that blocks TCP port 445 or UDP port 443 or TCP port 5445 when using an iWARP RDMA adapter can also cause this issue.\r\n
0xb0027854 | A network connection was disconnected.%n%nInstance name: %4%nServer name: %6%nServer address: %8%nConnection type: %9%nInterfaceId: %10%n%nGuidance:%nThis indicates that the client's connection to the server was disconnected.%n%nFrequent, unexpected disconnects when using an RDMA over Converged Ethernet (RoCE) adapter may indicate a network misconfiguration. RoCE requires Priority Flow Control (PFC) to be configured for every host, switch and router on the RoCE network. Failure to properly configure PFC will cause packet loss, frequent disconnects and poor performance.\r\n
0xb0027855 | The client lost its session to the server.%n%nError: %1%n%nServer name: %5%nSession ID: %2%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30806 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027856 | The client re-established its session to the server.%n%nServer name: %5%nServer address: %7%nSession ID: %2%n%nGuidance:%nYou should expect this event if there was a previous event 30805, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027857 | The connection to the share was lost.%n%nError: %1%n%nShare name: %5%nSession ID: %2%nTree ID: %3%n%nGuidance:%nIf the server is a Windows Failover Cluster file server, then this message occurs when the file share moves between cluster nodes. There should also be an anti-event 30808 indicating the session to the server was re-established. If the server is not a failover cluster, it is likely that the server was previously online, but it is now inaccessible over the network.\r\n
0xb0027858 | The connection to the share was re-established.%n%nShare name: %5%nServer address: %7%nSession ID: %2%nTree ID: %3%n%nGuidance:%nYou should expect this event if there was a previous event 30807, but the client successfully resumed the cached connection before the timeout expired.\r\n
0xb0027863 | The SMB client received a request to move to a different node on a file server cluster.%n%nFile server cluster name: %4%nNew file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer is going to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027864 | The SMB client successfully moved to a different node on a file server cluster.%n%nFile server cluster name: %4%n New file server cluster address: %6%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer successfully moved to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). No user action is required.\r\n
0xb0027865 | The SMB client failed to move to a different node on a file server cluster.%n%nError: %1%n%nFile server cluster name: %4%n%nGuidance:%nContinuous Availability (Transparent Failover) is in use and the client computer failed to move to a different node after an SMB witness request over RPC using TCP (first contacting port 135, then contacting an endpoint port above 1023). The attempt to connect to the destination server failed, which is typically due to a network configuration issue. For example, this issue may occur if the destination node's IP address cannot be resolved, if the destination node is behind a firewall, or if there is no network route from the client to the node.\r\n
0xb0027867 | The connection was terminated due to one or more IO request timeouts.%n%nError: %2%n%nName: %4%nServer address: %6%nClient address: %7%nInstance name: %9%nConnection type: %10%n%nGuidance:%nThis indicates a problem with the underlying network or the storage stack on the remote server. IO operations were not completed within the allotted time. The application may not see this failure because IOs are usually retried on a different connection. This event is for diagnostics only.\r\n
0xb00278b4 | The handle was created without persistence.%n%nFile ID: %2:%3%nCreateGUID: %4%nPath: %10%12%n%nGuidance:%nThe server supports Continuous Availability (persistent handles) and the request to create the handle succeeded. However, the server did not grant persistence. You should verify that the Resume Key Filter is running on the server and is attached to the target volume.\r\n
0xb00278b8 | The server does not support multichannel.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has disabled multichannel support on the server. This may also be a non-Microsoft file server that does not support multichannel or has multichannel disabled. You can enable SMB Multichannel on the server using this Windows PowerShell cmdlet: Set-SmbServerConfiguration -EnableMultiChannel:$true. This event does not apply to the multichannel settings of SMB client, which are controlled by the Set-SmbClientConfiguration Windows PowerShell cmdlet. Enabling or disabling client multichannel support does not affect server multichannel support.\r\n
0xb00278b9 | The client cannot connect to the server due to a multichannel constraint registry setting.%n%nServer name: %2%n%nGuidance:%nThe client attempted to use SMB Multichannel, but an administrator has configured multichannel support to prevent multichannel on the client. You can configure SMB Multichannel on the client using the Windows PowerShell cmdlets: New-SmbMultichannelConstraint and Remove-SmbMultichannelConstraint.\r\n
0xd0000001 | Active\r\n
0xd0000002 | Disconnected\r\n
0xd0000003 | Suspended\r\n
0xd0000004 | Construction in progress\r\n
0xd0000005 | Recovery in progress\r\n
0xd0000006 | Disconnect in progress\r\n
0xd0000007 | Invalidation in progress\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | Deleted\r\n
0xd000000a | NetBT\r\n
0xd000000b | TCPIP\r\n
0xd000000c | Rdma\r\n
0xd000000d | VMBUS\r\n
0xd000000e | Quic\r\n
0xd000000f | Smb2DiagReasonNotSpecified\r\n
0xd0000010 | Smb2DiagReasonDns\r\n
0xd0000011 | Smb2DiagReasonSetSocketSecurity\r\n
0xd0000012 | Smb2DiagReasonIPSec\r\n
0xd0000013 | Smb2DiagReasonNetworkConnect\r\n
0xd0000014 | Smb2DiagReasonNegotiateValidation\r\n
0xd0000015 | Smb2DiagReasonExchangeExpiry\r\n
0xd0000016 | Smb2DiagReasonDisconnectIndication\r\n
0xd0000017 | Smb2DiagReasonNegativeCache\r\n
0xd0000018 | Smb2DiagReasonConsecutiveSessionSetupFailures\r\n
0xd0000019 | Smb2DiagReasonQuicServerCertificateError\r\n
0xd000001a | Smb2DiagReasonQuicServerConfigFailure\r\n
0xd000001b | Smb2DiagReasonAcquireCredHandle\r\n
0xd000001c | Smb2DiagReasonISC\r\n
0xd000001d | Smb2DiagReasonSessionSetupResponse\r\n
0xd000001e | Smb2DiagReasonMADowngrade\r\n
0xd000001f | Smb2DiagReasonCreateSigningKey\r\n
0xd0000020 | Smb2DiagReasonRegisterCryptoKeys\r\n
0xd0000021 | Smb2DiagReasonQCA\r\n
0xd0000022 | Smb2DiagReasonEncryptionOnNullSession\r\n
0xd0000023 | Smb2DiagReasonSessionKeyLength\r\n
0xd0000024 | Smb2DiagReasonTreeConnectResponse\r\n
0xd0000025 | Smb2DiagReasonValidateNegotiateFsctl\r\n
0xd0000026 | Smb2DiagReasonHandleReconnect\r\n
0xd0000027 | Smb2DiagReasonCreateResponse\r\n
0xd0000028 | Smb2DiagReasonExchangeCancellation\r\n
0xd0000029 | Smb2DiagReasonExchangeNoBindingObject\r\n
0xd000002a | Smb2DiagReasonExchangeSendFailure\r\n
0xd000002b | Smb2DiagReasonObjectSuspended\r\n
0xd000002c | Smb2DiagReasonUserDisconnect\r\n
0xd000002d | Smb2DiagReasonHandleClosed\r\n
0xd000002e | Smb2DiagReasonInternalError\r\n
0xd000002f | Smb2DiagDisconnectReasonReceiveContextAllocation\r\n
0xd0000030 | Smb2DiagDisconnectReasonPaddingAllocation\r\n
0xd0000031 | Smb2DiagDisconnectReasonExchangeReceiveHandlerError\r\n
0xd0000032 | Smb2DiagDisconnectReasonMessageBufferAllocation\r\n
0xd0000033 | Smb2DiagDisconnectReasonVcEndpointTornDown\r\n
0xd0000034 | Smb2DiagDisconnectReasonMessageSizeReceiveError\r\n
0xd0000035 | Smb2DiagDisconnectReasonMessageSizeTooLargeError\r\n
0xd0000036 | Smb2DiagDisconnectReasonMessageCopyError\r\n
0xd0000037 | Smb2DiagDisconnectReasonVcReceiveHandlerError\r\n
0xd0000038 | Smb2DiagDisconnectReasonVcReceiveError\r\n
0xd0000039 | Negotiate\r\n
0xd000003a | Session setup\r\n
0xd000003b | Logoff\r\n
0xd000003c | Tree connect\r\n
0xd000003d | Tree disconnect\r\n
0xd000003e | Create\r\n
0xd000003f | Close\r\n
0xd0000040 | Flush\r\n
0xd0000041 | Read\r\n
0xd0000042 | Write\r\n
0xd0000043 | Lock\r\n
0xd0000044 | Ioctl\r\n
0xd0000045 | Cancel\r\n
0xd0000046 | Echo\r\n
0xd0000047 | Query directory\r\n
0xd0000048 | Change notify\r\n
0xd0000049 | Query info\r\n
0xd000004a | Set info\r\n
0xd000004b | Oplock break\r\n
0xd000004c | Create\r\n
0xd000004d | Close\r\n
0xd000004e | Read\r\n
0xd000004f | Write\r\n
0xd0000050 | Query information\r\n
0xd0000051 | Set information\r\n
0xd0000052 | Query EA\r\n
0xd0000053 | Set EA\r\n
0xd0000054 | Flush buffers\r\n
0xd0000055 | Query volume information\r\n
0xd0000056 | Set volume information\r\n
0xd0000057 | Directory control\r\n
0xd0000058 | File system control\r\n
0xd0000059 | Device control\r\n
0xd000005a | Internal device control\r\n
0xd000005b | Lock control\r\n
0xd000005c | Cleanup\r\n
0xd000005d | Query security\r\n
0xd000005e | Set security\r\n
0xd000005f | Query quota information\r\n
0xd0000060 | Set quota information\r\n
0xd0000061 | Internal probe I/O\r\n
0xd0000062 | Symmetric\r\n
0xd0000063 | Asymmetric\r\n
0xd0000064 | None\r\n
0xd0000065 | NTLM\r\n
0xd0000066 | Kerberos\r\n
0xd0000067 | PKU2U\r\n
