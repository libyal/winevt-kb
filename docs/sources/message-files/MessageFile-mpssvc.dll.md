## mpssvc.dll

Path: %SystemRoot%\System32\mpssvc.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x90000001 | Microsoft-Windows-MPS-SRV\r\n
0xb3001900 | An attempt to programmatically disable the Windows Firewall using a call to INetFwProfile.FirewallEnabled(FALSE) interface was rejected because this API is not supported on Windows Vista. This has most likely occurred due to an application which is incompatible with Windows Vista. Please contact the application's vendor to make sure you have a Windows Vista compatible application version.%n%nError Code:%t%tE_NOTIMPL%nCaller Process Name:%t%1%nProcess Id:%t%t%2%nPublisher:%t%t%3\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x04001900 | An attempt to programmatically disable the Windows Firewall using a call to INetFwProfile.FirewallEnabled(FALSE) interface was rejected because this API is not supported on Windows Vista. This has most likely occurred due to an application which is incompatible with Windows Vista. Please contact the application's vendor to make sure you have a Windows Vista compatible application version.%n%nError Code:%t%tE_NOTIMPL%nCaller Process Name:%t%1%nProcess Id:%t%t%2%nPublisher:%t%t%3\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x32000000 | Info\r\n
0x50000004 | Information\r\n
0x52000002 | Error\r\n
0x90000001 | Microsoft-Windows-Firewall-Service\r\n
0x91000001 | Microsoft-Windows-Firewall-Client\r\n
0x92000001 | Microsoft-Windows-Windows Firewall With Advanced Security\r\n
0x92000002 | Microsoft-Windows-Windows Firewall With Advanced Security/Firewall\r\n
0x92000003 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurity\r\n
0x92000004 | Microsoft-Windows-Windows Firewall With Advanced Security/FirewallVerbose\r\n
0x92000005 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurityVerbose\r\n
0x93000001 | Microsoft-Windows-Firewall-Driver\r\n
0x94000001 | Microsoft-Windows-Firewall\r\n
0x94000002 | System\r\n
0xb20007d0 | The following settings were applied to the Windows Firewall at startup%n%n%tCurrent Profile:%t%1%n%tIPsec SA Idle time:%t%2%n%tIPsec preshared key encoding:%t%3%n%tIPsec Exempt:%t%4%n%tIPsec CRL Check:%t%5%n%tIPsec Through NAT:%t%6%n%tPolicy Version Supported:%t%7%n%tPolicy Version:%t%8%n%tBinary Version Supported:%t%9%n%tStateful FTP:%t%10%n%tGroup Policy Applied:%t%11%n%tRemote Machine Authorization List:%t%12%n%tRemote UserAuthorization List:%t%13\r\n
0xb20007d1 | The following per profile settings were applied by Windows Firewall %n%n%tProfile:%t%1%n%tOperational Mode:%t%2%n%tStealth Mode:%t%3%n%tBlock all Incoming Connections:%t%4%n%tUnicast response to multicast broadcast:%t%5%n%tLog dropped packets:%t%6%n%tLog successful connections:%t%7%n%tLog ignored rules:%t%8%n%tInbound Notifications:%t%9%n%tAllow Local Policy Merge:%t%12%n%tAllow Local IPsec Policy Merge:%t%13%n%tDefault Outbound Action:%t%14%n%tDefault Inbound Action:%t%15%n%tRemote Administration:%t%16%n%tMaximum Log file size:%t%17%n%tLog File path:%t%18%n%tAllow User preferred merge of Authorized Applications:%t%10%n%tAllow User preferred merge of Globally open ports:%t%11\r\n
0xb20007d2 | A Windows Firewall setting has changed.%n%nNew Setting:%n%tType:%t%1%n%tValue:%t%4%n%tModifying User:%t%6%n%tModifying Application:%t%7\r\n
0xb20007d3 | A Windows Firewall setting in the %1 profile has changed.%nNew Setting:%n%tType:%t%2%n%tValue:%t%5%n%tModifying User:%t%7%n%tModifying Application:%t%8\r\n
0xb20007d4 | A rule has been added to the Windows Firewall exception list.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d5 | A rule has been modified in the Windows Firewall exception list.%n%nModified Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d6 | A rule has been deleted in the Windows Firewall exception list.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007d7 | A rule has been listed when the Windows Firewall started.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19\r\n
0xb20007d8 | Windows Firewall Group Policy settings have changed. The new settings have been applied\r\n
0xb20007d9 | The Windows Firewall service failed to load Group Policy.%nError:%t%1\r\n
0xb20007da | Network profile changed on an interface.%n%nAdapter GUID:%t%1%nAdapter Name:%t%2%nOld Profile:%t%3%nNew Profile:%t%4\r\n
0xb20007db | Windows Firewall was unable to notify the user that it blocked an application from accepting incoming connections on the network.%n%nReason:%t%t%1%nApplication Path:%t%2%nIP Version:%t%3%nProtocol:%t%4%nPort:%t%t%5%nProcess Id:%t%6%nUser:%t%t%7\r\n
0xb20007dc | A connection security rule was added to IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007dd | A connection security rule was modified in IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007de | A connection security rule was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007df | A connection security rule was added to IPsec settings when Windows Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007e0 | A main mode rule has been added in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e1 | A main mode rule has been modified in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e2 | A main mode rule has been deleted in the IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e3 | A main mode rule was added to the IPsec settings when Windows Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e4 | A phase 1 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e5 | A phase 1 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e6 | A phase 1 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e7 | A phase 1 crypto set was added to IPsec settings when Windows Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e8 | A phase 2 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007e9 | A phase 2 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ea | A phase 2 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007eb | A phase 2 crypto set was added to IPsec settings when Windows Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ec | An authentication set has been added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ed | An authentication set has been modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ee | An authentication set has been deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007ef | An authentication set has been added to IPsec settings when Windows Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007f0 | Windows Firewall has been reset to its default configuration.%n%n%tModifyingUser:%t%1%n%tModifyingApplication:%t%2\r\n
0xb20007f1 | All rules have been deleted from the Windows Firewall configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f2 | All connection security rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f3 | All main mode rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f4 | All authentication sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f5 | All crypto sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f6 | Windows Firewall did not apply the following rule because the rule was not properly configured on this computer:%n%nRule Information:%n%tID:%t%1%n%tName:%t%2%n%nError Information:%n%tReason:%t%3\r\n
0xd2000001 | Enable Windows Firewall\r\n
0xd2000002 | Disable Stealth Mode\r\n
0xd2000003 | Windows Firewall Shielded Mode\r\n
0xd2000004 | Disable Unicast Responses to Multicast\r\n
0xd2000005 | Log Dropped Packets\r\n
0xd2000006 | Log Successful Connections\r\n
0xd2000007 | Log Ignored Rules\r\n
0xd2000008 | Maximum Log File Size\r\n
0xd2000009 | Log File Path\r\n
0xd200000a | Disable Inbound Notifications\r\n
0xd200000b | Allow User preferred merge of Authorized Applications\r\n
0xd200000c | Allow User preferred merge of Globally open ports\r\n
0xd200000d | Allow Local Policy Merge\r\n
0xd200000e | Allow Local IPsec Policy Merge\r\n
0xd200000f | Disabled Interfaces\r\n
0xd2000010 | Default Outbound Action\r\n
0xd2000011 | Default Inbound Action\r\n
0xd2000012 | Current Profile\r\n
0xd2000013 | Disable Stateful FTP\r\n
0xd2000014 | Ignored Disable Stateful PPTP\r\n
0xd2000015 | IPsec SA Idle time\r\n
0xd2000016 | IPsec preshared key encoding\r\n
0xd2000017 | IPsec Exempt\r\n
0xd2000018 | IPsec CRL Check\r\n
0xd2000019 | IPsec Through NAT\r\n
0xd200001a | Policy Version\r\n
0xd200001b | Binary Version Supported\r\n
0xd200001c | Remote Machine Authorization List\r\n
0xd200001d | Remote User Authorization List\r\n
0xd200001e | Local\r\n
0xd200001f | Group Policy\r\n
0xd2000020 | Dynamic\r\n
0xd2000021 | AutoGenerated\r\n
0xd2000022 | Hardcoded\r\n
0xd2000023 | Allow\r\n
0xd2000024 | Block\r\n
0xd2000025 | Yes\r\n
0xd2000026 | No\r\n
0xd2000027 | Group policy RSOP\r\n
0xd2000028 | Local\r\n
0xd2000029 | WSH Static\r\n
0xd200002a | WSH Configurable\r\n
0xd200002b | Dynamic\r\n
0xd200002c | Group policy\r\n
0xd200002d | Enabled\r\n
0xd200002e | Disabled\r\n
0xd200002f | None\r\n
0xd2000030 | Allow\r\n
0xd2000031 | Defer to application\r\n
0xd2000032 | Defer to user\r\n
0xd2000033 | None\r\n
0xd2000034 | Require Authentication\r\n
0xd2000035 | Require Encryption\r\n
0xd2000036 | Require Authentication, Negotiate Encryption\r\n
0xd2000037 | Require Authentication, Allow no encapsulation\r\n
0xd2000038 | Never\r\n
0xd2000039 | Server behind NAT\r\n
0xd200003a | Server and client behind NAT\r\n
0xd200003b | Inbound\r\n
0xd200003c | Outbound\r\n
0xd200003d | Authenticated IPSec Bypass\r\n
0xd200003e | Block\r\n
0xd200003f | Allow\r\n
0xd2000040 | None\r\n
0xd2000041 | Private\r\n
0xd2000042 | Public\r\n
0xd2000043 | Domain\r\n
0xd2000044 | Private,Domain\r\n
0xd2000045 | Public, Domain\r\n
0xd2000046 | Public, Private\r\n
0xd2000047 | Private,Domain, Public\r\n
0xd2000048 | The application is a system service\r\n
0xd2000049 | The application is non interactive\r\n
0xd200004a | The firewall is off and the application is allowed\r\n
0xd200004b | The image is block listed\r\n
0xd200004c | The session is inactive\r\n
0xd200004d | An unknown error occurred\r\n
0xd200004e | Inbound notifications are not enabled\r\n
0xd200004f | All Inbound connections are disallowed\r\n
0xd2000050 | All Inbound connections are disallowed, Inbound notifications are not enabled\r\n
0xd2000051 | IPv4\r\n
0xd2000052 | IPv6\r\n
0xd2000053 | Any\r\n
0xd2000054 | TCP\r\n
0xd2000055 | UDP\r\n
0xd2000056 | ICMP V4\r\n
0xd2000057 | ICMP V6\r\n
0xd2000058 | Any\r\n
0xd2000059 | Disabled\r\n
0xd200005a | Check\r\n
0xd200005b | Enforce\r\n
0xd200005c | None\r\n
0xd200005d | UTF8\r\n
0xd200005e | None\r\n
0xd200005f | NeighborDiscovery\r\n
0xd2000060 | ICMP\r\n
0xd2000061 | Require authentication for inbound connections and request authentication for outbound connections\r\n
0xd2000062 | Request authentication for inbound and outbound connections\r\n
0xd2000063 | Require authentication for inbound and outbound connections\r\n
0xd2000064 | Do not authenticate\r\n
0xd2000065 | None\r\n
0xd2000066 | Do Not Skip DH\r\n
0xd2000067 | Invalid\r\n
0xd2000068 | None\r\n
0xd2000069 | MainMode\r\n
0xd200006a | DHGroup1\r\n
0xd200006b | DHGroup1\r\n
0xd200006c | DHGroup14\r\n
0xd200006d | ECDHP256\r\n
0xd200006e | ECDHP384\r\n
0xd200006f | Invalid\r\n
0xd2000070 | Phase 1\r\n
0xd2000071 | Phase 2\r\n

### 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0x04001900 | An attempt to programmatically disable the Windows Firewall using a call to INetFwProfile.FirewallEnabled(FALSE) interface was rejected because this API is not supported on Windows Vista. This has most likely occurred due to an application which is incompatible with Windows Vista. Please contact the application's vendor to make sure you have a Windows Vista compatible application version.%n%nError Code:%t%tE_NOTIMPL%nCaller Process Name:%t%1%nProcess Id:%t%t%2%nPublisher:%t%t%3\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x32000000 | Info\r\n
0x50000004 | Information\r\n
0x52000002 | Error\r\n
0x90000001 | Microsoft-Windows-Firewall-Service\r\n
0x91000001 | Microsoft-Windows-Firewall-Client\r\n
0x92000001 | Microsoft-Windows-Windows Firewall With Advanced Security\r\n
0x92000002 | Microsoft-Windows-Windows Firewall With Advanced Security/Firewall\r\n
0x92000003 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurity\r\n
0x92000004 | Microsoft-Windows-Windows Firewall With Advanced Security/FirewallVerbose\r\n
0x92000005 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurityVerbose\r\n
0x92000006 | Network Isolation Operational\r\n
0x93000001 | Microsoft-Windows-Firewall-Driver\r\n
0x94000001 | Microsoft-Windows-Firewall\r\n
0x94000002 | System\r\n
0xb20007d0 | The following settings were applied to the Windows Firewall at startup%n%n%tCurrent Profile:%t%1%n%tIPsec SA Idle time:%t%2%n%tIPsec preshared key encoding:%t%3%n%tIPsec Exempt:%t%4%n%tIPsec CRL Check:%t%5%n%tIPsec Through NAT:%t%6%n%tPolicy Version Supported:%t%7%n%tPolicy Version:%t%8%n%tBinary Version Supported:%t%9%n%tStateful FTP:%t%10%n%tGroup Policy Applied:%t%11%n%tRemote Machine Authorization List:%t%12%n%tRemote UserAuthorization List:%t%13\r\n
0xb20007d1 | The following per profile settings were applied by Windows Firewall %n%n%tProfile:%t%1%n%tOperational Mode:%t%2%n%tStealth Mode:%t%3%n%tBlock all Incoming Connections:%t%4%n%tUnicast response to multicast broadcast:%t%5%n%tLog dropped packets:%t%6%n%tLog successful connections:%t%7%n%tLog ignored rules:%t%8%n%tInbound Notifications:%t%9%n%tAllow Local Policy Merge:%t%12%n%tAllow Local IPsec Policy Merge:%t%13%n%tDefault Outbound Action:%t%14%n%tDefault Inbound Action:%t%15%n%tRemote Administration:%t%16%n%tStealth Mode IPsec Secured Packet Exemption:%t%21%n%tMaximum Log file size:%t%17%n%tLog File path:%t%18%n%tAllow User preferred merge of Authorized Applications:%t%10%n%tAllow User preferred merge of Globally open ports:%t%11\r\n
0xb20007d2 | A Windows Firewall setting has changed.%n%nNew Setting:%n%tType:%t%1%n%tValue:%t%4%n%tModifying User:%t%6%n%tModifying Application:%t%7\r\n
0xb20007d3 | A Windows Firewall setting in the %1 profile has changed.%nNew Setting:%n%tType:%t%2%n%tValue:%t%5%n%tModifying User:%t%7%n%tModifying Application:%t%8\r\n
0xb20007d4 | A rule has been added to the Windows Firewall exception list.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d5 | A rule has been modified in the Windows Firewall exception list.%n%nModified Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d6 | A rule has been deleted in the Windows Firewall exception list.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007d7 | A rule has been listed when the Windows Firewall started.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19\r\n
0xb20007d8 | Windows Firewall Group Policy settings have changed. The new settings have been applied\r\n
0xb20007d9 | The Windows Firewall service failed to load Group Policy.%nError:%t%1\r\n
0xb20007da | Network profile changed on an interface.%n%nAdapter GUID:%t%1%nAdapter Name:%t%2%nOld Profile:%t%3%nNew Profile:%t%4\r\n
0xb20007db | Windows Firewall was unable to notify the user that it blocked an application from accepting incoming connections on the network.%n%nReason:%t%t%1%nApplication Path:%t%2%nIP Version:%t%3%nProtocol:%t%4%nPort:%t%t%5%nProcess Id:%t%6%nUser:%t%t%7\r\n
0xb20007dc | A connection security rule was added to IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007dd | A connection security rule was modified in IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007de | A connection security rule was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007df | A connection security rule was added to IPsec settings when Windows Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007e0 | A main mode rule has been added in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e1 | A main mode rule has been modified in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e2 | A main mode rule has been deleted in the IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e3 | A main mode rule was added to the IPsec settings when Windows Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e4 | A phase 1 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e5 | A phase 1 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e6 | A phase 1 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e7 | A phase 1 crypto set was added to IPsec settings when Windows Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e8 | A phase 2 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007e9 | A phase 2 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ea | A phase 2 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007eb | A phase 2 crypto set was added to IPsec settings when Windows Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ec | An authentication set has been added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ed | An authentication set has been modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ee | An authentication set has been deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007ef | An authentication set has been added to IPsec settings when Windows Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007f0 | Windows Firewall has been reset to its default configuration.%n%n%tModifyingUser:%t%1%n%tModifyingApplication:%t%2\r\n
0xb20007f1 | All rules have been deleted from the Windows Firewall configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f2 | All connection security rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f3 | All main mode rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f4 | All authentication sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f5 | All crypto sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f6 | Windows Firewall did not apply the following rule because the rule was not properly configured on this computer:%n%nRule Information:%n%tID:%t%1%n%tName:%t%2%n%nError Information:%n%tReason:%t%3\r\n
0xb20007f7 | Http Proxies Changed%n%nReason: %t%1%n%nAll Proxies:%t%2%n%nAll Domain Proxies:%t%3%n%nGroup Policy Configured Domain Proxies:%t%4%n%nGroup Policy Configured Local Proxies:%t%5%n%nAll DA Nat64 Domain Proxies:%t%6%n%nGroup Policy is authoritative:%t%7%n\r\n
0xb20007f8 | Corp Subnets Changed%n%nReason: %t%1%n%nAll Domain Subnets:%t%2%n%nGroup Policy Configured Domain Subnets:%t%3%n%nAll DA Nat64 Domain Subnets:%t%4%n%nGroup Policy is authoritative:%t%5%n\r\n
0xb20007f9 | Capability Changed%n%nReason: %t%1%n%nCapability:%t%2%nProfile:%t%3%nIP Range Definition:%t%4\r\n
0xd2000001 | Enable Windows Firewall\r\n
0xd2000002 | Disable Stealth Mode\r\n
0xd2000003 | Windows Firewall Shielded Mode\r\n
0xd2000004 | Disable Unicast Responses to Multicast\r\n
0xd2000005 | Log Dropped Packets\r\n
0xd2000006 | Log Successful Connections\r\n
0xd2000007 | Log Ignored Rules\r\n
0xd2000008 | Maximum Log File Size\r\n
0xd2000009 | Log File Path\r\n
0xd200000a | Disable Inbound Notifications\r\n
0xd200000b | Allow User preferred merge of Authorized Applications\r\n
0xd200000c | Allow User preferred merge of Globally open ports\r\n
0xd200000d | Allow Local Policy Merge\r\n
0xd200000e | Allow Local IPsec Policy Merge\r\n
0xd200000f | Disabled Interfaces\r\n
0xd2000010 | Default Outbound Action\r\n
0xd2000011 | Default Inbound Action\r\n
0xd2000012 | Disable Stealth Mode IPsec Secured Packet Exemption\r\n
0xd2000013 | Current Profile\r\n
0xd2000014 | Disable Stateful FTP\r\n
0xd2000015 | Ignored Disable Stateful PPTP\r\n
0xd2000016 | IPsec SA Idle time\r\n
0xd2000017 | IPsec preshared key encoding\r\n
0xd2000018 | IPsec Exempt\r\n
0xd2000019 | IPsec CRL Check\r\n
0xd200001a | IPsec Through NAT\r\n
0xd200001b | Policy Version\r\n
0xd200001c | Binary Version Supported\r\n
0xd200001d | Remote Machine Authorization List\r\n
0xd200001e | Remote User Authorization List\r\n
0xd200001f | Local\r\n
0xd2000020 | Group Policy\r\n
0xd2000021 | Dynamic\r\n
0xd2000022 | AutoGenerated\r\n
0xd2000023 | Hardcoded\r\n
0xd2000024 | Allow\r\n
0xd2000025 | Block\r\n
0xd2000026 | Yes\r\n
0xd2000027 | No\r\n
0xd2000028 | Group policy RSOP\r\n
0xd2000029 | Local\r\n
0xd200002a | WSH Static\r\n
0xd200002b | WSH Configurable\r\n
0xd200002c | Dynamic\r\n
0xd200002d | Group policy\r\n
0xd200002e | Enabled\r\n
0xd200002f | Disabled\r\n
0xd2000030 | None\r\n
0xd2000031 | Allow\r\n
0xd2000032 | Defer to application\r\n
0xd2000033 | Defer to user\r\n
0xd2000034 | None\r\n
0xd2000035 | Require Authentication\r\n
0xd2000036 | Require Encryption\r\n
0xd2000037 | Require Authentication, Negotiate Encryption\r\n
0xd2000038 | Require Authentication, Allow no encapsulation\r\n
0xd2000039 | Never\r\n
0xd200003a | Server behind NAT\r\n
0xd200003b | Server and client behind NAT\r\n
0xd200003c | Inbound\r\n
0xd200003d | Outbound\r\n
0xd200003e | Authenticated IPSec Bypass\r\n
0xd200003f | Block\r\n
0xd2000040 | Allow\r\n
0xd2000041 | None\r\n
0xd2000042 | Private\r\n
0xd2000043 | Public\r\n
0xd2000044 | Domain\r\n
0xd2000045 | Private,Domain\r\n
0xd2000046 | Public, Domain\r\n
0xd2000047 | Public, Private\r\n
0xd2000048 | Private,Domain, Public\r\n
0xd2000049 | The application is a system service\r\n
0xd200004a | The application is non interactive\r\n
0xd200004b | The firewall is off and the application is allowed\r\n
0xd200004c | The image is block listed\r\n
0xd200004d | The session is inactive\r\n
0xd200004e | An unknown error occurred\r\n
0xd200004f | Inbound notifications are not enabled\r\n
0xd2000050 | All Inbound connections are disallowed\r\n
0xd2000051 | All Inbound connections are disallowed, Inbound notifications are not enabled\r\n
0xd2000052 | IPv4\r\n
0xd2000053 | IPv6\r\n
0xd2000054 | Any\r\n
0xd2000055 | TCP\r\n
0xd2000056 | UDP\r\n
0xd2000057 | ICMP V4\r\n
0xd2000058 | ICMP V6\r\n
0xd2000059 | Any\r\n
0xd200005a | Disabled\r\n
0xd200005b | Check\r\n
0xd200005c | Enforce\r\n
0xd200005d | None\r\n
0xd200005e | UTF8\r\n
0xd200005f | None\r\n
0xd2000060 | NeighborDiscovery\r\n
0xd2000061 | ICMP\r\n
0xd2000062 | Require authentication for inbound connections and request authentication for outbound connections\r\n
0xd2000063 | Request authentication for inbound and outbound connections\r\n
0xd2000064 | Require authentication for inbound and outbound connections\r\n
0xd2000065 | Do not authenticate\r\n
0xd2000066 | None\r\n
0xd2000067 | Do Not Skip DH\r\n
0xd2000068 | Invalid\r\n
0xd2000069 | None\r\n
0xd200006a | MainMode\r\n
0xd200006b | DHGroup1\r\n
0xd200006c | DHGroup1\r\n
0xd200006d | DHGroup14\r\n
0xd200006e | ECDHP256\r\n
0xd200006f | ECDHP384\r\n
0xd2000070 | DHGroup24\r\n
0xd2000071 | Invalid\r\n
0xd2000072 | Phase 1\r\n
0xd2000073 | Phase 2\r\n
0xd2000074 | Group Policy Change\r\n
0xd2000075 | Network Change\r\n
0xd2000076 | Manual Change\r\n
0xd2000077 | Indication Change\r\n
0xd2000078 | Subscription Refresh\r\n
0xd2000079 | Group Policy Change\r\n
0xd200007a | AD Subnets Change\r\n
0xd200007b | Subscription Refresh\r\n
0xd200007c | Local Address Change\r\n
0xd200007d | Corp Subnets\r\n
0xd200007e | Http Proxies\r\n
0xd200007f | Network Profile Change\r\n
0xd2000080 | Internet\r\n
0xd2000081 | PrivateNetwork\r\n
0xd2000082 | DA Remote PrivateNetwork\r\n
0xd2000083 | Proximity\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0

Message identifier | Message string
--- | ---
0x03001900 | An attempt to programmatically disable the Windows Firewall using a call to INetFwProfile.FirewallEnabled(FALSE) interface was rejected because this API is not supported on Windows Vista. This has most likely occurred due to an application which is incompatible with Windows Vista. Please contact the application's vendor to make sure you have a Windows Vista compatible application version.%n%nError Code:%t%tE_NOTIMPL%nCaller Process Name:%t%1%nProcess Id:%t%t%2%nPublisher:%t%t%3\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x32000000 | Info\r\n
0x50000004 | Information\r\n
0x52000002 | Error\r\n
0x90000001 | Microsoft-Windows-Firewall-Service\r\n
0x91000001 | Microsoft-Windows-Firewall-Client\r\n
0x92000001 | Microsoft-Windows-Windows Firewall With Advanced Security\r\n
0x92000002 | Microsoft-Windows-Windows Firewall With Advanced Security/Firewall\r\n
0x92000003 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurity\r\n
0x92000004 | Microsoft-Windows-Windows Firewall With Advanced Security/FirewallVerbose\r\n
0x92000005 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurityVerbose\r\n
0x92000006 | Network Isolation Operational\r\n
0x93000001 | Microsoft-Windows-Firewall\r\n
0x93000002 | System\r\n
0xb20007d0 | The following settings were applied to the Windows Firewall at startup%n%n%tCurrent Profile:%t%1%n%tIPsec SA Idle time:%t%2%n%tIPsec preshared key encoding:%t%3%n%tIPsec Exempt:%t%4%n%tIPsec CRL Check:%t%5%n%tIPsec Through NAT:%t%6%n%tPolicy Version Supported:%t%7%n%tPolicy Version:%t%8%n%tBinary Version Supported:%t%9%n%tStateful FTP:%t%10%n%tGroup Policy Applied:%t%11%n%tRemote Machine Authorization List:%t%12%n%tRemote UserAuthorization List:%t%13\r\n
0xb20007d1 | The following per profile settings were applied by Windows Firewall %n%n%tProfile:%t%1%n%tOperational Mode:%t%2%n%tStealth Mode:%t%3%n%tBlock all Incoming Connections:%t%4%n%tUnicast response to multicast broadcast:%t%5%n%tLog dropped packets:%t%6%n%tLog successful connections:%t%7%n%tLog ignored rules:%t%8%n%tInbound Notifications:%t%9%n%tAllow Local Policy Merge:%t%12%n%tAllow Local IPsec Policy Merge:%t%13%n%tDefault Outbound Action:%t%14%n%tDefault Inbound Action:%t%15%n%tRemote Administration:%t%16%n%tStealth Mode IPsec Secured Packet Exemption:%t%21%n%tMaximum Log file size:%t%17%n%tLog File path:%t%18%n%tAllow User preferred merge of Authorized Applications:%t%10%n%tAllow User preferred merge of Globally open ports:%t%11\r\n
0xb20007d2 | A Windows Firewall setting has changed.%n%nNew Setting:%n%tType:%t%1%n%tValue:%t%4%n%tModifying User:%t%6%n%tModifying Application:%t%7\r\n
0xb20007d3 | A Windows Firewall setting in the %1 profile has changed.%nNew Setting:%n%tType:%t%2%n%tValue:%t%5%n%tModifying User:%t%7%n%tModifying Application:%t%8\r\n
0xb20007d4 | A rule has been added to the Windows Firewall exception list.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d5 | A rule has been modified in the Windows Firewall exception list.%n%nModified Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d6 | A rule has been deleted in the Windows Firewall exception list.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007d7 | A rule has been listed when the Windows Firewall started.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19\r\n
0xb20007d8 | Windows Firewall Group Policy settings have changed. The new settings have been applied\r\n
0xb20007d9 | The Windows Firewall service failed to load Group Policy.%nError:%t%1\r\n
0xb20007da | Network profile changed on an interface.%n%nAdapter GUID:%t%1%nAdapter Name:%t%2%nOld Profile:%t%3%nNew Profile:%t%4\r\n
0xb20007db | Windows Firewall was unable to notify the user that it blocked an application from accepting incoming connections on the network.%n%nReason:%t%t%1%nApplication Path:%t%2%nIP Version:%t%3%nProtocol:%t%4%nPort:%t%t%5%nProcess Id:%t%6%nUser:%t%t%7\r\n
0xb20007dc | A connection security rule was added to IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007dd | A connection security rule was modified in IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007de | A connection security rule was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007df | A connection security rule was added to IPsec settings when Windows Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007e0 | A main mode rule has been added in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e1 | A main mode rule has been modified in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e2 | A main mode rule has been deleted in the IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e3 | A main mode rule was added to the IPsec settings when Windows Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e4 | A phase 1 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e5 | A phase 1 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e6 | A phase 1 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e7 | A phase 1 crypto set was added to IPsec settings when Windows Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e8 | A phase 2 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007e9 | A phase 2 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ea | A phase 2 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007eb | A phase 2 crypto set was added to IPsec settings when Windows Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ec | An authentication set has been added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ed | An authentication set has been modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ee | An authentication set has been deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007ef | An authentication set has been added to IPsec settings when Windows Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007f0 | Windows Firewall has been reset to its default configuration.%n%n%tModifyingUser:%t%1%n%tModifyingApplication:%t%2\r\n
0xb20007f1 | All rules have been deleted from the Windows Firewall configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f2 | All connection security rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f3 | All main mode rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f4 | All authentication sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f5 | All crypto sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f6 | Windows Firewall did not apply the following rule because the rule was not properly configured on this computer:%n%nRule Information:%n%tID:%t%1%n%tName:%t%2%n%nError Information:%n%tReason:%t%3\r\n
0xb20007f7 | Http Proxies Changed%n%nReason: %t%1%n%nAll Proxies:%t%2%n%nAll Domain Proxies:%t%3%n%nGroup Policy Configured Domain Proxies:%t%4%n%nGroup Policy Configured Local Proxies:%t%5%n%nAll DA Nat64 Domain Proxies:%t%6%n%nGroup Policy is authoritative:%t%7%n\r\n
0xb20007f8 | Corp Subnets Changed%n%nReason: %t%1%n%nAll Domain Subnets:%t%2%n%nGroup Policy Configured Domain Subnets:%t%3%n%nAll DA Nat64 Domain Subnets:%t%4%n%nGroup Policy is authoritative:%t%5%n\r\n
0xb20007f9 | Capability Changed%n%nReason: %t%1%n%nCapability:%t%2%nProfile:%t%3%nIP Range Definition:%t%4\r\n
0xd2000001 | Enable Windows Firewall\r\n
0xd2000002 | Disable Stealth Mode\r\n
0xd2000003 | Windows Firewall Shielded Mode\r\n
0xd2000004 | Disable Unicast Responses to Multicast\r\n
0xd2000005 | Log Dropped Packets\r\n
0xd2000006 | Log Successful Connections\r\n
0xd2000007 | Log Ignored Rules\r\n
0xd2000008 | Maximum Log File Size\r\n
0xd2000009 | Log File Path\r\n
0xd200000a | Disable Inbound Notifications\r\n
0xd200000b | Allow User preferred merge of Authorized Applications\r\n
0xd200000c | Allow User preferred merge of Globally open ports\r\n
0xd200000d | Allow Local Policy Merge\r\n
0xd200000e | Allow Local IPsec Policy Merge\r\n
0xd200000f | Disabled Interfaces\r\n
0xd2000010 | Default Outbound Action\r\n
0xd2000011 | Default Inbound Action\r\n
0xd2000012 | Disable Stealth Mode IPsec Secured Packet Exemption\r\n
0xd2000013 | Current Profile\r\n
0xd2000014 | Disable Stateful FTP\r\n
0xd2000015 | Ignored Disable Stateful PPTP\r\n
0xd2000016 | IPsec SA Idle time\r\n
0xd2000017 | IPsec preshared key encoding\r\n
0xd2000018 | IPsec Exempt\r\n
0xd2000019 | IPsec CRL Check\r\n
0xd200001a | IPsec Through NAT\r\n
0xd200001b | Policy Version\r\n
0xd200001c | Binary Version Supported\r\n
0xd200001d | Remote Machine Authorization List\r\n
0xd200001e | Remote User Authorization List\r\n
0xd200001f | Local\r\n
0xd2000020 | Group Policy\r\n
0xd2000021 | Dynamic\r\n
0xd2000022 | AutoGenerated\r\n
0xd2000023 | Hardcoded\r\n
0xd2000024 | Allow\r\n
0xd2000025 | Block\r\n
0xd2000026 | Yes\r\n
0xd2000027 | No\r\n
0xd2000028 | Group policy RSOP\r\n
0xd2000029 | Local\r\n
0xd200002a | WSH Static\r\n
0xd200002b | WSH Configurable\r\n
0xd200002c | Dynamic\r\n
0xd200002d | Group policy\r\n
0xd200002e | Enabled\r\n
0xd200002f | Disabled\r\n
0xd2000030 | None\r\n
0xd2000031 | Allow\r\n
0xd2000032 | Defer to application\r\n
0xd2000033 | Defer to user\r\n
0xd2000034 | None\r\n
0xd2000035 | Require Authentication\r\n
0xd2000036 | Require Encryption\r\n
0xd2000037 | Require Authentication, Negotiate Encryption\r\n
0xd2000038 | Require Authentication, Allow no encapsulation\r\n
0xd2000039 | Never\r\n
0xd200003a | Server behind NAT\r\n
0xd200003b | Server and client behind NAT\r\n
0xd200003c | Inbound\r\n
0xd200003d | Outbound\r\n
0xd200003e | Authenticated IPSec Bypass\r\n
0xd200003f | Block\r\n
0xd2000040 | Allow\r\n
0xd2000041 | None\r\n
0xd2000042 | Private\r\n
0xd2000043 | Public\r\n
0xd2000044 | Domain\r\n
0xd2000045 | Private,Domain\r\n
0xd2000046 | Public, Domain\r\n
0xd2000047 | Public, Private\r\n
0xd2000048 | Private,Domain, Public\r\n
0xd2000049 | The application is a system service\r\n
0xd200004a | The application is non interactive\r\n
0xd200004b | The firewall is off and the application is allowed\r\n
0xd200004c | The image is block listed\r\n
0xd200004d | The session is inactive\r\n
0xd200004e | An unknown error occurred\r\n
0xd200004f | Inbound notifications are not enabled\r\n
0xd2000050 | All Inbound connections are disallowed\r\n
0xd2000051 | All Inbound connections are disallowed, Inbound notifications are not enabled\r\n
0xd2000052 | IPv4\r\n
0xd2000053 | IPv6\r\n
0xd2000054 | Any\r\n
0xd2000055 | TCP\r\n
0xd2000056 | UDP\r\n
0xd2000057 | ICMP V4\r\n
0xd2000058 | ICMP V6\r\n
0xd2000059 | Any\r\n
0xd200005a | Disabled\r\n
0xd200005b | Check\r\n
0xd200005c | Enforce\r\n
0xd200005d | None\r\n
0xd200005e | UTF8\r\n
0xd200005f | None\r\n
0xd2000060 | NeighborDiscovery\r\n
0xd2000061 | ICMP\r\n
0xd2000062 | Require authentication for inbound connections and request authentication for outbound connections\r\n
0xd2000063 | Request authentication for inbound and outbound connections\r\n
0xd2000064 | Require authentication for inbound and outbound connections\r\n
0xd2000065 | Do not authenticate\r\n
0xd2000066 | None\r\n
0xd2000067 | Do Not Skip DH\r\n
0xd2000068 | Invalid\r\n
0xd2000069 | None\r\n
0xd200006a | MainMode\r\n
0xd200006b | DHGroup1\r\n
0xd200006c | DHGroup1\r\n
0xd200006d | DHGroup14\r\n
0xd200006e | ECDHP256\r\n
0xd200006f | ECDHP384\r\n
0xd2000070 | DHGroup24\r\n
0xd2000071 | Invalid\r\n
0xd2000072 | Phase 1\r\n
0xd2000073 | Phase 2\r\n
0xd2000074 | Group Policy Change\r\n
0xd2000075 | Network Change\r\n
0xd2000076 | Manual Change\r\n
0xd2000077 | Indication Change\r\n
0xd2000078 | Subscription Refresh\r\n
0xd2000079 | Group Policy Change\r\n
0xd200007a | AD Subnets Change\r\n
0xd200007b | Subscription Refresh\r\n
0xd200007c | Local Address Change\r\n
0xd200007d | Corp Subnets\r\n
0xd200007e | Http Proxies\r\n
0xd200007f | Network Profile Change\r\n
0xd2000080 | Internet\r\n
0xd2000081 | PrivateNetwork\r\n
0xd2000082 | DA Remote PrivateNetwork\r\n
0xd2000083 | Proximity\r\n

### 10.0.16299.15, 10.0.17134.1

Message identifier | Message string
--- | ---
0x03001900 | An attempt to programmatically disable the Windows Defender Firewall using a call to INetFwProfile.FirewallEnabled(FALSE) interface was rejected because this API is not supported on Windows Vista. This has most likely occurred due to an application which is incompatible with Windows Vista. Please contact the application's vendor to make sure you have a Windows Vista compatible application version.%n%nError Code:%t%tE_NOTIMPL%nCaller Process Name:%t%1%nProcess Id:%t%t%2%nPublisher:%t%t%3\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x32000000 | Info\r\n
0x50000004 | Information\r\n
0x52000002 | Error\r\n
0x90000001 | Microsoft-Windows-Firewall-Service\r\n
0x91000001 | Microsoft-Windows-Firewall-Client\r\n
0x92000001 | Microsoft-Windows-Windows Firewall With Advanced Security\r\n
0x92000002 | Microsoft-Windows-Windows Firewall With Advanced Security/Firewall\r\n
0x92000003 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurity\r\n
0x92000004 | Microsoft-Windows-Windows Firewall With Advanced Security/FirewallVerbose\r\n
0x92000005 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurityVerbose\r\n
0x92000006 | Network Isolation Operational\r\n
0x93000001 | Microsoft-Windows-Firewall\r\n
0x93000002 | System\r\n
0xb20007d0 | The following settings were applied to the Windows Defender Firewall at startup%n%n%tCurrent Profile:%t%1%n%tIPsec SA Idle time:%t%2%n%tIPsec preshared key encoding:%t%3%n%tIPsec Exempt:%t%4%n%tIPsec CRL Check:%t%5%n%tIPsec Through NAT:%t%6%n%tPolicy Version Supported:%t%7%n%tPolicy Version:%t%8%n%tBinary Version Supported:%t%9%n%tStateful FTP:%t%10%n%tGroup Policy Applied:%t%11%n%tRemote Machine Authorization List:%t%12%n%tRemote UserAuthorization List:%t%13\r\n
0xb20007d1 | The following per profile settings were applied by Windows Defender Firewall %n%n%tProfile:%t%1%n%tOperational Mode:%t%2%n%tStealth Mode:%t%3%n%tBlock all Incoming Connections:%t%4%n%tUnicast response to multicast broadcast:%t%5%n%tLog dropped packets:%t%6%n%tLog successful connections:%t%7%n%tLog ignored rules:%t%8%n%tInbound Notifications:%t%9%n%tAllow Local Policy Merge:%t%12%n%tAllow Local IPsec Policy Merge:%t%13%n%tDefault Outbound Action:%t%14%n%tDefault Inbound Action:%t%15%n%tRemote Administration:%t%16%n%tStealth Mode IPsec Secured Packet Exemption:%t%21%n%tMaximum Log file size:%t%17%n%tLog File path:%t%18%n%tAllow User preferred merge of Authorized Applications:%t%10%n%tAllow User preferred merge of Globally open ports:%t%11\r\n
0xb20007d2 | A Windows Defender Firewall setting has changed.%n%nNew Setting:%n%tType:%t%1%n%tValue:%t%4%n%tModifying User:%t%6%n%tModifying Application:%t%7\r\n
0xb20007d3 | A Windows Defender Firewall setting in the %1 profile has changed.%nNew Setting:%n%tType:%t%2%n%tValue:%t%5%n%tModifying User:%t%7%n%tModifying Application:%t%8\r\n
0xb20007d4 | A rule has been added to the Windows Defender Firewall exception list.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d5 | A rule has been modified in the Windows Defender Firewall exception list.%n%nModified Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d6 | A rule has been deleted in the Windows Defender Firewall exception list.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007d7 | A rule has been listed when the Windows Defender Firewall started.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19\r\n
0xb20007d8 | Windows Defender Firewall Group Policy settings have changed. The new settings have been applied\r\n
0xb20007d9 | The Windows Defender Firewall service failed to load Group Policy.%nError:%t%1\r\n
0xb20007da | Network profile changed on an interface.%n%nAdapter GUID:%t%1%nAdapter Name:%t%2%nOld Profile:%t%3%nNew Profile:%t%4\r\n
0xb20007db | Windows Defender Firewall was unable to notify the user that it blocked an application from accepting incoming connections on the network.%n%nReason:%t%t%1%nApplication Path:%t%2%nIP Version:%t%3%nProtocol:%t%4%nPort:%t%t%5%nProcess Id:%t%6%nUser:%t%t%7\r\n
0xb20007dc | A connection security rule was added to IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007dd | A connection security rule was modified in IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007de | A connection security rule was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007df | A connection security rule was added to IPsec settings when Windows Defender Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007e0 | A main mode rule has been added in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e1 | A main mode rule has been modified in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e2 | A main mode rule has been deleted in the IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e3 | A main mode rule was added to the IPsec settings when Windows Defender Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e4 | A phase 1 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e5 | A phase 1 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e6 | A phase 1 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e7 | A phase 1 crypto set was added to IPsec settings when Windows Defender Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e8 | A phase 2 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007e9 | A phase 2 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ea | A phase 2 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007eb | A phase 2 crypto set was added to IPsec settings when Windows Defender Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ec | An authentication set has been added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ed | An authentication set has been modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ee | An authentication set has been deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007ef | An authentication set has been added to IPsec settings when Windows Defender Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007f0 | Windows Defender Firewall has been reset to its default configuration.%n%n%tModifyingUser:%t%1%n%tModifyingApplication:%t%2\r\n
0xb20007f1 | All rules have been deleted from the Windows Defender Firewall configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f2 | All connection security rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f3 | All main mode rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f4 | All authentication sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f5 | All crypto sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f6 | Windows Defender Firewall did not apply the following rule because the rule was not properly configured on this computer:%n%nRule Information:%n%tID:%t%1%n%tName:%t%2%n%nError Information:%n%tReason:%t%3\r\n
0xb20007f7 | Http Proxies Changed%n%nReason: %t%1%n%nAll Proxies:%t%2%n%nAll Domain Proxies:%t%3%n%nGroup Policy Configured Domain Proxies:%t%4%n%nGroup Policy Configured Local Proxies:%t%5%n%nAll DA Nat64 Domain Proxies:%t%6%n%nGroup Policy is authoritative:%t%7%n\r\n
0xb20007f8 | Corp Subnets Changed%n%nReason: %t%1%n%nAll Domain Subnets:%t%2%n%nGroup Policy Configured Domain Subnets:%t%3%n%nAll DA Nat64 Domain Subnets:%t%4%n%nGroup Policy is authoritative:%t%5%n\r\n
0xb20007f9 | Capability Changed%n%nReason: %t%1%n%nCapability:%t%2%nProfile:%t%3%nIP Range Definition:%t%4\r\n
0xd2000001 | Enable Windows Defender Firewall\r\n
0xd2000002 | Disable Stealth Mode\r\n
0xd2000003 | Windows Defender Firewall Shielded Mode\r\n
0xd2000004 | Disable Unicast Responses to Multicast\r\n
0xd2000005 | Log Dropped Packets\r\n
0xd2000006 | Log Successful Connections\r\n
0xd2000007 | Log Ignored Rules\r\n
0xd2000008 | Maximum Log File Size\r\n
0xd2000009 | Log File Path\r\n
0xd200000a | Disable Inbound Notifications\r\n
0xd200000b | Allow User preferred merge of Authorized Applications\r\n
0xd200000c | Allow User preferred merge of Globally open ports\r\n
0xd200000d | Allow Local Policy Merge\r\n
0xd200000e | Allow Local IPsec Policy Merge\r\n
0xd200000f | Disabled Interfaces\r\n
0xd2000010 | Default Outbound Action\r\n
0xd2000011 | Default Inbound Action\r\n
0xd2000012 | Disable Stealth Mode IPsec Secured Packet Exemption\r\n
0xd2000013 | Current Profile\r\n
0xd2000014 | Disable Stateful FTP\r\n
0xd2000015 | Ignored Disable Stateful PPTP\r\n
0xd2000016 | IPsec SA Idle time\r\n
0xd2000017 | IPsec preshared key encoding\r\n
0xd2000018 | IPsec Exempt\r\n
0xd2000019 | IPsec CRL Check\r\n
0xd200001a | IPsec Through NAT\r\n
0xd200001b | Policy Version\r\n
0xd200001c | Binary Version Supported\r\n
0xd200001d | Remote Machine Authorization List\r\n
0xd200001e | Remote User Authorization List\r\n
0xd200001f | Local\r\n
0xd2000020 | Group Policy\r\n
0xd2000021 | Dynamic\r\n
0xd2000022 | AutoGenerated\r\n
0xd2000023 | Hardcoded\r\n
0xd2000024 | Allow\r\n
0xd2000025 | Block\r\n
0xd2000026 | Yes\r\n
0xd2000027 | No\r\n
0xd2000028 | Group policy RSOP\r\n
0xd2000029 | Local\r\n
0xd200002a | WSH Static\r\n
0xd200002b | WSH Configurable\r\n
0xd200002c | Dynamic\r\n
0xd200002d | Group policy\r\n
0xd200002e | Enabled\r\n
0xd200002f | Disabled\r\n
0xd2000030 | None\r\n
0xd2000031 | Allow\r\n
0xd2000032 | Defer to application\r\n
0xd2000033 | Defer to user\r\n
0xd2000034 | None\r\n
0xd2000035 | Require Authentication\r\n
0xd2000036 | Require Encryption\r\n
0xd2000037 | Require Authentication, Negotiate Encryption\r\n
0xd2000038 | Require Authentication, Allow no encapsulation\r\n
0xd2000039 | Never\r\n
0xd200003a | Server behind NAT\r\n
0xd200003b | Server and client behind NAT\r\n
0xd200003c | Inbound\r\n
0xd200003d | Outbound\r\n
0xd200003e | Authenticated IPSec Bypass\r\n
0xd200003f | Block\r\n
0xd2000040 | Allow\r\n
0xd2000041 | None\r\n
0xd2000042 | Private\r\n
0xd2000043 | Public\r\n
0xd2000044 | Domain\r\n
0xd2000045 | Private,Domain\r\n
0xd2000046 | Public, Domain\r\n
0xd2000047 | Public, Private\r\n
0xd2000048 | Private,Domain, Public\r\n
0xd2000049 | The application is a system service\r\n
0xd200004a | The application is non interactive\r\n
0xd200004b | The firewall is off and the application is allowed\r\n
0xd200004c | The image is block listed\r\n
0xd200004d | The session is inactive\r\n
0xd200004e | An unknown error occurred\r\n
0xd200004f | Inbound notifications are not enabled\r\n
0xd2000050 | All Inbound connections are disallowed\r\n
0xd2000051 | All Inbound connections are disallowed, Inbound notifications are not enabled\r\n
0xd2000052 | IPv4\r\n
0xd2000053 | IPv6\r\n
0xd2000054 | Any\r\n
0xd2000055 | TCP\r\n
0xd2000056 | UDP\r\n
0xd2000057 | ICMP V4\r\n
0xd2000058 | ICMP V6\r\n
0xd2000059 | Any\r\n
0xd200005a | Disabled\r\n
0xd200005b | Check\r\n
0xd200005c | Enforce\r\n
0xd200005d | None\r\n
0xd200005e | UTF8\r\n
0xd200005f | None\r\n
0xd2000060 | NeighborDiscovery\r\n
0xd2000061 | ICMP\r\n
0xd2000062 | Require authentication for inbound connections and request authentication for outbound connections\r\n
0xd2000063 | Request authentication for inbound and outbound connections\r\n
0xd2000064 | Require authentication for inbound and outbound connections\r\n
0xd2000065 | Do not authenticate\r\n
0xd2000066 | None\r\n
0xd2000067 | Do Not Skip DH\r\n
0xd2000068 | Invalid\r\n
0xd2000069 | None\r\n
0xd200006a | MainMode\r\n
0xd200006b | DHGroup1\r\n
0xd200006c | DHGroup1\r\n
0xd200006d | DHGroup14\r\n
0xd200006e | ECDHP256\r\n
0xd200006f | ECDHP384\r\n
0xd2000070 | DHGroup24\r\n
0xd2000071 | Invalid\r\n
0xd2000072 | Phase 1\r\n
0xd2000073 | Phase 2\r\n
0xd2000074 | Group Policy Change\r\n
0xd2000075 | Network Change\r\n
0xd2000076 | Manual Change\r\n
0xd2000077 | Indication Change\r\n
0xd2000078 | Subscription Refresh\r\n
0xd2000079 | Group Policy Change\r\n
0xd200007a | AD Subnets Change\r\n
0xd200007b | Subscription Refresh\r\n
0xd200007c | Local Address Change\r\n
0xd200007d | Corp Subnets\r\n
0xd200007e | Http Proxies\r\n
0xd200007f | Network Profile Change\r\n
0xd2000080 | Internet\r\n
0xd2000081 | PrivateNetwork\r\n
0xd2000082 | DA Remote PrivateNetwork\r\n
0xd2000083 | Proximity\r\n

### 10.0.17763.1

Message identifier | Message string
--- | ---
0x03001900 | An attempt to programmatically disable the Windows Defender Firewall using a call to INetFwProfile.FirewallEnabled(FALSE) interface was rejected because this API is not supported on Windows Vista. This has most likely occurred due to an application which is incompatible with Windows Vista. Please contact the application's vendor to make sure you have a Windows Vista compatible application version.%n%nError Code:%t%tE_NOTIMPL%nCaller Process Name:%t%1%nProcess Id:%t%t%2%nPublisher:%t%t%3\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x32000000 | Info\r\n
0x50000004 | Information\r\n
0x52000002 | Error\r\n
0x90000001 | Microsoft-Windows-Firewall-Service\r\n
0x91000001 | Microsoft-Windows-Firewall-Client\r\n
0x92000001 | Microsoft-Windows-Windows Firewall With Advanced Security\r\n
0x92000002 | Microsoft-Windows-Windows Firewall With Advanced Security/Firewall\r\n
0x92000003 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurity\r\n
0x92000004 | Microsoft-Windows-Windows Firewall With Advanced Security/FirewallVerbose\r\n
0x92000005 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurityVerbose\r\n
0x92000006 | Network Isolation Operational\r\n
0x92000007 | Microsoft-Windows-Windows Firewall With Advanced Security/FirewallDiagnostics\r\n
0x93000001 | Microsoft-Windows-Firewall\r\n
0x93000002 | System\r\n
0xb20007d0 | The following settings were applied to the Windows Defender Firewall at startup%n%n%tCurrent Profile:%t%1%n%tIPsec SA Idle time:%t%2%n%tIPsec preshared key encoding:%t%3%n%tIPsec Exempt:%t%4%n%tIPsec CRL Check:%t%5%n%tIPsec Through NAT:%t%6%n%tPolicy Version Supported:%t%7%n%tPolicy Version:%t%8%n%tBinary Version Supported:%t%9%n%tStateful FTP:%t%10%n%tGroup Policy Applied:%t%11%n%tRemote Machine Authorization List:%t%12%n%tRemote UserAuthorization List:%t%13\r\n
0xb20007d1 | The following per profile settings were applied by Windows Defender Firewall %n%n%tProfile:%t%1%n%tOperational Mode:%t%2%n%tStealth Mode:%t%3%n%tBlock all Incoming Connections:%t%4%n%tUnicast response to multicast broadcast:%t%5%n%tLog dropped packets:%t%6%n%tLog successful connections:%t%7%n%tLog ignored rules:%t%8%n%tInbound Notifications:%t%9%n%tAllow Local Policy Merge:%t%12%n%tAllow Local IPsec Policy Merge:%t%13%n%tDefault Outbound Action:%t%14%n%tDefault Inbound Action:%t%15%n%tRemote Administration:%t%16%n%tStealth Mode IPsec Secured Packet Exemption:%t%21%n%tMaximum Log file size:%t%17%n%tLog File path:%t%18%n%tAllow User preferred merge of Authorized Applications:%t%10%n%tAllow User preferred merge of Globally open ports:%t%11\r\n
0xb20007d2 | A Windows Defender Firewall setting has changed.%n%nNew Setting:%n%tType:%t%1%n%tValue:%t%4%n%tModifying User:%t%6%n%tModifying Application:%t%7\r\n
0xb20007d3 | A Windows Defender Firewall setting in the %1 profile has changed.%nNew Setting:%n%tType:%t%2%n%tValue:%t%5%n%tModifying User:%t%7%n%tModifying Application:%t%8\r\n
0xb20007d4 | A rule has been added to the Windows Defender Firewall exception list.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d5 | A rule has been modified in the Windows Defender Firewall exception list.%n%nModified Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d6 | A rule has been deleted in the Windows Defender Firewall exception list.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007d7 | A rule has been listed when the Windows Defender Firewall started.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19\r\n
0xb20007d8 | Windows Defender Firewall Group Policy settings have changed. The new settings have been applied\r\n
0xb20007d9 | The Windows Defender Firewall service failed to load Group Policy.%nError:%t%1\r\n
0xb20007da | Network profile changed on an interface.%n%nAdapter GUID:%t%1%nAdapter Name:%t%2%nOld Profile:%t%3%nNew Profile:%t%4\r\n
0xb20007db | Windows Defender Firewall was unable to notify the user that it blocked an application from accepting incoming connections on the network.%n%nReason:%t%t%1%nApplication Path:%t%2%nIP Version:%t%3%nProtocol:%t%4%nPort:%t%t%5%nProcess Id:%t%6%nUser:%t%t%7\r\n
0xb20007dc | A connection security rule was added to IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007dd | A connection security rule was modified in IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007de | A connection security rule was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007df | A connection security rule was added to IPsec settings when Windows Defender Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007e0 | A main mode rule has been added in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e1 | A main mode rule has been modified in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e2 | A main mode rule has been deleted in the IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e3 | A main mode rule was added to the IPsec settings when Windows Defender Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e4 | A phase 1 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e5 | A phase 1 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e6 | A phase 1 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e7 | A phase 1 crypto set was added to IPsec settings when Windows Defender Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e8 | A phase 2 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007e9 | A phase 2 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ea | A phase 2 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007eb | A phase 2 crypto set was added to IPsec settings when Windows Defender Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ec | An authentication set has been added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ed | An authentication set has been modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ee | An authentication set has been deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007ef | An authentication set has been added to IPsec settings when Windows Defender Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007f0 | Windows Defender Firewall has been reset to its default configuration.%n%n%tModifyingUser:%t%1%n%tModifyingApplication:%t%2\r\n
0xb20007f1 | All rules have been deleted from the Windows Defender Firewall configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f2 | All connection security rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f3 | All main mode rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f4 | All authentication sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f5 | All crypto sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f6 | Windows Defender Firewall did not apply the following rule because the rule was not properly configured on this computer:%n%nRule Information:%n%tID:%t%1%n%tName:%t%2%n%nError Information:%n%tReason:%t%3\r\n
0xb20007f7 | Http Proxies Changed%n%nReason: %t%1%n%nAll Proxies:%t%2%n%nAll Domain Proxies:%t%3%n%nGroup Policy Configured Domain Proxies:%t%4%n%nGroup Policy Configured Local Proxies:%t%5%n%nAll DA Nat64 Domain Proxies:%t%6%n%nGroup Policy is authoritative:%t%7%n\r\n
0xb20007f8 | Corp Subnets Changed%n%nReason: %t%1%n%nAll Domain Subnets:%t%2%n%nGroup Policy Configured Domain Subnets:%t%3%n%nAll DA Nat64 Domain Subnets:%t%4%n%nGroup Policy is authoritative:%t%5%n\r\n
0xb20007f9 | Capability Changed%n%nReason: %t%1%n%nCapability:%t%2%nProfile:%t%3%nIP Range Definition:%t%4\r\n
0xd2000001 | Enable Windows Defender Firewall\r\n
0xd2000002 | Disable Stealth Mode\r\n
0xd2000003 | Windows Defender Firewall Shielded Mode\r\n
0xd2000004 | Disable Unicast Responses to Multicast\r\n
0xd2000005 | Log Dropped Packets\r\n
0xd2000006 | Log Successful Connections\r\n
0xd2000007 | Log Ignored Rules\r\n
0xd2000008 | Maximum Log File Size\r\n
0xd2000009 | Log File Path\r\n
0xd200000a | Disable Inbound Notifications\r\n
0xd200000b | Allow User preferred merge of Authorized Applications\r\n
0xd200000c | Allow User preferred merge of Globally open ports\r\n
0xd200000d | Allow Local Policy Merge\r\n
0xd200000e | Allow Local IPsec Policy Merge\r\n
0xd200000f | Disabled Interfaces\r\n
0xd2000010 | Default Outbound Action\r\n
0xd2000011 | Default Inbound Action\r\n
0xd2000012 | Disable Stealth Mode IPsec Secured Packet Exemption\r\n
0xd2000013 | Current Profile\r\n
0xd2000014 | Disable Stateful FTP\r\n
0xd2000015 | Ignored Disable Stateful PPTP\r\n
0xd2000016 | IPsec SA Idle time\r\n
0xd2000017 | IPsec preshared key encoding\r\n
0xd2000018 | IPsec Exempt\r\n
0xd2000019 | IPsec CRL Check\r\n
0xd200001a | IPsec Through NAT\r\n
0xd200001b | Policy Version\r\n
0xd200001c | Binary Version Supported\r\n
0xd200001d | Remote Machine Authorization List\r\n
0xd200001e | Remote User Authorization List\r\n
0xd200001f | Local\r\n
0xd2000020 | Group Policy\r\n
0xd2000021 | Dynamic\r\n
0xd2000022 | AutoGenerated\r\n
0xd2000023 | Hardcoded\r\n
0xd2000024 | Allow\r\n
0xd2000025 | Block\r\n
0xd2000026 | Yes\r\n
0xd2000027 | No\r\n
0xd2000028 | Group policy RSOP\r\n
0xd2000029 | Local\r\n
0xd200002a | WSH Static\r\n
0xd200002b | WSH Configurable\r\n
0xd200002c | Dynamic\r\n
0xd200002d | Group policy\r\n
0xd200002e | Enabled\r\n
0xd200002f | Disabled\r\n
0xd2000030 | None\r\n
0xd2000031 | Allow\r\n
0xd2000032 | Defer to application\r\n
0xd2000033 | Defer to user\r\n
0xd2000034 | None\r\n
0xd2000035 | Require Authentication\r\n
0xd2000036 | Require Encryption\r\n
0xd2000037 | Require Authentication, Negotiate Encryption\r\n
0xd2000038 | Require Authentication, Allow no encapsulation\r\n
0xd2000039 | Never\r\n
0xd200003a | Server behind NAT\r\n
0xd200003b | Server and client behind NAT\r\n
0xd200003c | Inbound\r\n
0xd200003d | Outbound\r\n
0xd200003e | Authenticated IPSec Bypass\r\n
0xd200003f | Block\r\n
0xd2000040 | Allow\r\n
0xd2000041 | None\r\n
0xd2000042 | Private\r\n
0xd2000043 | Public\r\n
0xd2000044 | Domain\r\n
0xd2000045 | Private,Domain\r\n
0xd2000046 | Public, Domain\r\n
0xd2000047 | Public, Private\r\n
0xd2000048 | Private,Domain, Public\r\n
0xd2000049 | The application is a system service\r\n
0xd200004a | The application is non interactive\r\n
0xd200004b | The firewall is off and the application is allowed\r\n
0xd200004c | The image is block listed\r\n
0xd200004d | The session is inactive\r\n
0xd200004e | An unknown error occurred\r\n
0xd200004f | Inbound notifications are not enabled\r\n
0xd2000050 | All Inbound connections are disallowed\r\n
0xd2000051 | All Inbound connections are disallowed, Inbound notifications are not enabled\r\n
0xd2000052 | IPv4\r\n
0xd2000053 | IPv6\r\n
0xd2000054 | Any\r\n
0xd2000055 | TCP\r\n
0xd2000056 | UDP\r\n
0xd2000057 | ICMP V4\r\n
0xd2000058 | ICMP V6\r\n
0xd2000059 | Any\r\n
0xd200005a | Disabled\r\n
0xd200005b | Check\r\n
0xd200005c | Enforce\r\n
0xd200005d | None\r\n
0xd200005e | UTF8\r\n
0xd200005f | None\r\n
0xd2000060 | NeighborDiscovery\r\n
0xd2000061 | ICMP\r\n
0xd2000062 | Require authentication for inbound connections and request authentication for outbound connections\r\n
0xd2000063 | Request authentication for inbound and outbound connections\r\n
0xd2000064 | Require authentication for inbound and outbound connections\r\n
0xd2000065 | Do not authenticate\r\n
0xd2000066 | None\r\n
0xd2000067 | Do Not Skip DH\r\n
0xd2000068 | Invalid\r\n
0xd2000069 | None\r\n
0xd200006a | MainMode\r\n
0xd200006b | DHGroup1\r\n
0xd200006c | DHGroup1\r\n
0xd200006d | DHGroup14\r\n
0xd200006e | ECDHP256\r\n
0xd200006f | ECDHP384\r\n
0xd2000070 | DHGroup24\r\n
0xd2000071 | Invalid\r\n
0xd2000072 | Phase 1\r\n
0xd2000073 | Phase 2\r\n
0xd2000074 | Group Policy Change\r\n
0xd2000075 | Network Change\r\n
0xd2000076 | Manual Change\r\n
0xd2000077 | Indication Change\r\n
0xd2000078 | Subscription Refresh\r\n
0xd2000079 | Group Policy Change\r\n
0xd200007a | AD Subnets Change\r\n
0xd200007b | Subscription Refresh\r\n
0xd200007c | Local Address Change\r\n
0xd200007d | Corp Subnets\r\n
0xd200007e | Http Proxies\r\n
0xd200007f | Network Profile Change\r\n
0xd2000080 | Internet\r\n
0xd2000081 | PrivateNetwork\r\n
0xd2000082 | DA Remote PrivateNetwork\r\n
0xd2000083 | Proximity\r\n

### 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x020007fa | Config Read Failed%n%nConfig:%t%1%nError:%t%2\r\n
0x03001900 | An attempt to programmatically disable the Windows Defender Firewall using a call to INetFwProfile.FirewallEnabled(FALSE) interface was rejected because this API is not supported on Windows Vista. This has most likely occurred due to an application which is incompatible with Windows Vista. Please contact the application's vendor to make sure you have a Windows Vista compatible application version.%n%nError Code:%t%tE_NOTIMPL%nCaller Process Name:%t%1%nProcess Id:%t%t%2%nPublisher:%t%t%3\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x32000000 | Info\r\n
0x50000004 | Information\r\n
0x52000002 | Error\r\n
0x90000001 | Microsoft-Windows-Firewall-Service\r\n
0x91000001 | Microsoft-Windows-Firewall-Client\r\n
0x92000001 | Microsoft-Windows-Windows Firewall With Advanced Security\r\n
0x92000002 | Microsoft-Windows-Windows Firewall With Advanced Security/Firewall\r\n
0x92000003 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurity\r\n
0x92000004 | Microsoft-Windows-Windows Firewall With Advanced Security/FirewallVerbose\r\n
0x92000005 | Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurityVerbose\r\n
0x92000006 | Network Isolation Operational\r\n
0x92000007 | Microsoft-Windows-Windows Firewall With Advanced Security/FirewallDiagnostics\r\n
0x92000008 | System\r\n
0x93000001 | Microsoft-Windows-Firewall\r\n
0xb20007d0 | The following settings were applied to the Windows Defender Firewall at startup%n%n%tCurrent Profile:%t%1%n%tIPsec SA Idle time:%t%2%n%tIPsec preshared key encoding:%t%3%n%tIPsec Exempt:%t%4%n%tIPsec CRL Check:%t%5%n%tIPsec Through NAT:%t%6%n%tPolicy Version Supported:%t%7%n%tPolicy Version:%t%8%n%tBinary Version Supported:%t%9%n%tStateful FTP:%t%10%n%tGroup Policy Applied:%t%11%n%tRemote Machine Authorization List:%t%12%n%tRemote UserAuthorization List:%t%13\r\n
0xb20007d1 | The following per profile settings were applied by Windows Defender Firewall %n%n%tProfile:%t%1%n%tOperational Mode:%t%2%n%tStealth Mode:%t%3%n%tBlock all Incoming Connections:%t%4%n%tUnicast response to multicast broadcast:%t%5%n%tLog dropped packets:%t%6%n%tLog successful connections:%t%7%n%tLog ignored rules:%t%8%n%tInbound Notifications:%t%9%n%tAllow Local Policy Merge:%t%12%n%tAllow Local IPsec Policy Merge:%t%13%n%tDefault Outbound Action:%t%14%n%tDefault Inbound Action:%t%15%n%tRemote Administration:%t%16%n%tStealth Mode IPsec Secured Packet Exemption:%t%21%n%tMaximum Log file size:%t%17%n%tLog File path:%t%18%n%tAllow User preferred merge of Authorized Applications:%t%10%n%tAllow User preferred merge of Globally open ports:%t%11\r\n
0xb20007d2 | A Windows Defender Firewall setting has changed.%n%nNew Setting:%n%tType:%t%1%n%tValue:%t%4%n%tModifying User:%t%6%n%tModifying Application:%t%7\r\n
0xb20007d3 | A Windows Defender Firewall setting in the %1 profile has changed.%nNew Setting:%n%tType:%t%2%n%tValue:%t%5%n%tModifying User:%t%7%n%tModifying Application:%t%8\r\n
0xb20007d4 | A rule has been added to the Windows Defender Firewall exception list.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d5 | A rule has been modified in the Windows Defender Firewall exception list.%n%nModified Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19%n%tModifying User:%t%22%n%tModifying Application:%t%23\r\n
0xb20007d6 | A rule has been deleted in the Windows Defender Firewall exception list.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007d7 | A rule has been listed when the Windows Defender Firewall started.%n%nAdded Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%18%n%tDirection:%t%6%n%tProfiles:%t%11%n%tAction:%t%10%n%tApplication Path:%t%4%n%tService Name:%t%5%n%tProtocol:%t%7%n%tSecurity Options:%t%21%n%tEdge Traversal:%t%19\r\n
0xb20007d8 | Windows Defender Firewall Group Policy settings have changed. The new settings have been applied\r\n
0xb20007d9 | The Windows Defender Firewall service failed to load Group Policy.%nError:%t%1\r\n
0xb20007da | Network profile changed on an interface.%n%nAdapter GUID:%t%1%nAdapter Name:%t%2%nOld Profile:%t%3%nNew Profile:%t%4\r\n
0xb20007db | Windows Defender Firewall was unable to notify the user that it blocked an application from accepting incoming connections on the network.%n%nReason:%t%t%1%nApplication Path:%t%2%nIP Version:%t%3%nProtocol:%t%4%nPort:%t%t%5%nProcess Id:%t%6%nUser:%t%t%7\r\n
0xb20007dc | A connection security rule was added to IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007dd | A connection security rule was modified in IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007de | A connection security rule was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007df | A connection security rule was added to IPsec settings when Windows Defender Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tOrigin:%t%3%n%tActive:%t%4%n%tProtocol:%t%5%n%tEndPoint1Ports:%t%6%n%tEndPoint2Ports:%t%7%n%tLocalTunnelEndpointV4:%t%8%n%tLocalTunnelEndpointV6:%t%9%n%tRemoteTunnelEndpointV4:%t%10%n%tRemoteTunnelEndpointV6:%t%11%n%tPhase1AuthSetId:%t%12%n%tPhase2AuthSetId:%t%13%n%tPhase2CryptoSetId:%t%14%n%tAction:%t%15%n%tProfiles:%t%16%n%tLocalAddresses:%t%17%n%tRemoteAddresses:%t%18%n%tEmbeddedContext:%t%20%n%tIsDTM:%t%22%n%tApplyAuthZ:%t%23%n%tBypassTunnelIfEncrypted:%t%24%n%tNoIPSecOnOutbound:%t%25%n%tModifyingUser:%t%26%n%tModifyingApplication:%t%27\r\n
0xb20007e0 | A main mode rule has been added in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e1 | A main mode rule has been modified in the IPsec settings.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e2 | A main mode rule has been deleted in the IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e3 | A main mode rule was added to the IPsec settings when Windows Defender Firewall started.%n%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tProfiles:%t%3%n%tEndpoint1:%t%4%n%tEndpoint2:%t%5%n%tPhase1AuthSetId:%t%6%n%tPhase1CryptoSetId:%t%7%n%tFlags:%t%8%n%tActive:%t%9%n%tEmbeddedContext:%t%10%n%tOrigin:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e4 | A phase 1 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e5 | A phase 1 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e6 | A phase 1 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007e7 | A phase 1 crypto set was added to IPsec settings when Windows Defender Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tFlags:%t%6%n%tNumSuites:%t%7%n%tTimeOutMinutes:%t%10%n%tTimeOutSessions:%t%11%n%tModifyingUser:%t%12%n%tModifyingApplication:%t%13\r\n
0xb20007e8 | A phase 2 crypto set was added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007e9 | A phase 2 crypto set was modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ea | A phase 2 crypto set was deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007eb | A phase 2 crypto set was added to IPsec settings when Windows Defender Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tOrigin:%t%4%n%tPfs:%t%6%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ec | An authentication set has been added to IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ed | An authentication set has been modified in IPsec settings.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007ee | An authentication set has been deleted from IPsec settings.%n%nDeleted Rule:%n%tRule ID:%t%1%n%tRule Name:%t%2%n%tModifying User:%t%3%n%tModifying Application:%t%4\r\n
0xb20007ef | An authentication set has been added to IPsec settings when Windows Defender Firewall started.%n%n%tSet ID:%t%1%n%tSet Name:%t%2%n%tIPsec Phase:%t%3%n%tOrigin:%t%5%n%tNumSuites:%t%7%n%tModifyingUser:%t%10%n%tModifyingApplication:%t%11\r\n
0xb20007f0 | Windows Defender Firewall has been reset to its default configuration.%n%n%tModifyingUser:%t%1%n%tModifyingApplication:%t%2\r\n
0xb20007f1 | All rules have been deleted from the Windows Defender Firewall configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f2 | All connection security rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f3 | All main mode rules have been deleted from the IPsec configuration on this computer.%n%n%tStore Type:%t%1%n%tModifyingUser:%t%2%n%tModifyingApplication:%t%3\r\n
0xb20007f4 | All authentication sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f5 | All crypto sets have been deleted from the IPsec configuration on this computer.%n%n%tIPsec Phase:%t%1%n%tStore Type:%t%2%n%tModifyingUser:%t%3%n%tModifyingApplication:%t%4\r\n
0xb20007f6 | Windows Defender Firewall did not apply the following rule because the rule was not properly configured on this computer:%n%nRule Information:%n%tID:%t%1%n%tName:%t%2%n%nError Information:%n%tReason:%t%3\r\n
0xb20007f7 | Http Proxies Changed%n%nReason: %t%1%n%nAll Proxies:%t%2%n%nAll Domain Proxies:%t%3%n%nGroup Policy Configured Domain Proxies:%t%4%n%nGroup Policy Configured Local Proxies:%t%5%n%nAll DA Nat64 Domain Proxies:%t%6%n%nGroup Policy is authoritative:%t%7%n\r\n
0xb20007f8 | Corp Subnets Changed%n%nReason: %t%1%n%nAll Domain Subnets:%t%2%n%nGroup Policy Configured Domain Subnets:%t%3%n%nAll DA Nat64 Domain Subnets:%t%4%n%nGroup Policy is authoritative:%t%5%n\r\n
0xb20007f9 | Capability Changed%n%nReason: %t%1%n%nCapability:%t%2%nProfile:%t%3%nIP Range Definition:%t%4\r\n
0xd2000001 | Enable Windows Defender Firewall\r\n
0xd2000002 | Disable Stealth Mode\r\n
0xd2000003 | Windows Defender Firewall Shielded Mode\r\n
0xd2000004 | Disable Unicast Responses to Multicast\r\n
0xd2000005 | Log Dropped Packets\r\n
0xd2000006 | Log Successful Connections\r\n
0xd2000007 | Log Ignored Rules\r\n
0xd2000008 | Maximum Log File Size\r\n
0xd2000009 | Log File Path\r\n
0xd200000a | Disable Inbound Notifications\r\n
0xd200000b | Allow User preferred merge of Authorized Applications\r\n
0xd200000c | Allow User preferred merge of Globally open ports\r\n
0xd200000d | Allow Local Policy Merge\r\n
0xd200000e | Allow Local IPsec Policy Merge\r\n
0xd200000f | Disabled Interfaces\r\n
0xd2000010 | Default Outbound Action\r\n
0xd2000011 | Default Inbound Action\r\n
0xd2000012 | Disable Stealth Mode IPsec Secured Packet Exemption\r\n
0xd2000013 | Current Profile\r\n
0xd2000014 | Disable Stateful FTP\r\n
0xd2000015 | Ignored Disable Stateful PPTP\r\n
0xd2000016 | IPsec SA Idle time\r\n
0xd2000017 | IPsec preshared key encoding\r\n
0xd2000018 | IPsec Exempt\r\n
0xd2000019 | IPsec CRL Check\r\n
0xd200001a | IPsec Through NAT\r\n
0xd200001b | Policy Version\r\n
0xd200001c | Binary Version Supported\r\n
0xd200001d | Remote Machine Authorization List\r\n
0xd200001e | Remote User Authorization List\r\n
0xd200001f | Local\r\n
0xd2000020 | Group Policy\r\n
0xd2000021 | Dynamic\r\n
0xd2000022 | AutoGenerated\r\n
0xd2000023 | Hardcoded\r\n
0xd2000024 | Allow\r\n
0xd2000025 | Block\r\n
0xd2000026 | Yes\r\n
0xd2000027 | No\r\n
0xd2000028 | Group policy RSOP\r\n
0xd2000029 | Local\r\n
0xd200002a | WSH Static\r\n
0xd200002b | WSH Configurable\r\n
0xd200002c | Dynamic\r\n
0xd200002d | Group policy\r\n
0xd200002e | Enabled\r\n
0xd200002f | Disabled\r\n
0xd2000030 | None\r\n
0xd2000031 | Allow\r\n
0xd2000032 | Defer to application\r\n
0xd2000033 | Defer to user\r\n
0xd2000034 | None\r\n
0xd2000035 | Require Authentication\r\n
0xd2000036 | Require Encryption\r\n
0xd2000037 | Require Authentication, Negotiate Encryption\r\n
0xd2000038 | Require Authentication, Allow no encapsulation\r\n
0xd2000039 | Never\r\n
0xd200003a | Server behind NAT\r\n
0xd200003b | Server and client behind NAT\r\n
0xd200003c | Inbound\r\n
0xd200003d | Outbound\r\n
0xd200003e | Authenticated IPSec Bypass\r\n
0xd200003f | Block\r\n
0xd2000040 | Allow\r\n
0xd2000041 | None\r\n
0xd2000042 | Private\r\n
0xd2000043 | Public\r\n
0xd2000044 | Domain\r\n
0xd2000045 | Private,Domain\r\n
0xd2000046 | Public, Domain\r\n
0xd2000047 | Public, Private\r\n
0xd2000048 | Private,Domain, Public\r\n
0xd2000049 | The application is a system service\r\n
0xd200004a | The application is non interactive\r\n
0xd200004b | The firewall is off and the application is allowed\r\n
0xd200004c | The image is block listed\r\n
0xd200004d | The session is inactive\r\n
0xd200004e | An unknown error occurred\r\n
0xd200004f | Inbound notifications are not enabled\r\n
0xd2000050 | All Inbound connections are disallowed\r\n
0xd2000051 | All Inbound connections are disallowed, Inbound notifications are not enabled\r\n
0xd2000052 | IPv4\r\n
0xd2000053 | IPv6\r\n
0xd2000054 | Any\r\n
0xd2000055 | TCP\r\n
0xd2000056 | UDP\r\n
0xd2000057 | ICMP V4\r\n
0xd2000058 | ICMP V6\r\n
0xd2000059 | Any\r\n
0xd200005a | Disabled\r\n
0xd200005b | Check\r\n
0xd200005c | Enforce\r\n
0xd200005d | None\r\n
0xd200005e | UTF8\r\n
0xd200005f | None\r\n
0xd2000060 | NeighborDiscovery\r\n
0xd2000061 | ICMP\r\n
0xd2000062 | Require authentication for inbound connections and request authentication for outbound connections\r\n
0xd2000063 | Request authentication for inbound and outbound connections\r\n
0xd2000064 | Require authentication for inbound and outbound connections\r\n
0xd2000065 | Do not authenticate\r\n
0xd2000066 | None\r\n
0xd2000067 | Do Not Skip DH\r\n
0xd2000068 | Invalid\r\n
0xd2000069 | None\r\n
0xd200006a | MainMode\r\n
0xd200006b | DHGroup1\r\n
0xd200006c | DHGroup1\r\n
0xd200006d | DHGroup14\r\n
0xd200006e | ECDHP256\r\n
0xd200006f | ECDHP384\r\n
0xd2000070 | DHGroup24\r\n
0xd2000071 | Invalid\r\n
0xd2000072 | Phase 1\r\n
0xd2000073 | Phase 2\r\n
0xd2000074 | Group Policy Change\r\n
0xd2000075 | Network Change\r\n
0xd2000076 | Manual Change\r\n
0xd2000077 | Indication Change\r\n
0xd2000078 | Subscription Refresh\r\n
0xd2000079 | Group Policy Change\r\n
0xd200007a | AD Subnets Change\r\n
0xd200007b | Subscription Refresh\r\n
0xd200007c | Local Address Change\r\n
0xd200007d | Corp Subnets\r\n
0xd200007e | Http Proxies\r\n
0xd200007f | Network Profile Change\r\n
0xd2000080 | Internet\r\n
0xd2000081 | PrivateNetwork\r\n
0xd2000082 | DA Remote PrivateNetwork\r\n
0xd2000083 | Proximity\r\n
