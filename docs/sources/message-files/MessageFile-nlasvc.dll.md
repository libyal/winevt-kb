## nlasvc.dll

Path: %SystemRoot%\system32\nlasvc.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x10000031 | Response Time\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Wait for Identification\r\n
0x70000002 | Trigger\r\n
0x70000003 | Gateway Resolution\r\n
0x70000004 | Plugin\r\n
0x70000005 | Dhcp\r\n
0x70000006 | Intranet Resolution\r\n
0x70000007 | DsGetDcName(DnsSuffix)\r\n
0x70000008 | DsGetDcName(Ds)\r\n
0x70000009 | DsGetDcName(RootDomainGuid)\r\n
0x7000000a | Ldap Authentication\r\n
0x7000000b | ldap_connect\r\n
0x7000000c | ldap_bind\r\n
0x7000000d | Identifying\r\n
0x7000000e | Identified\r\n
0x7000000f | Disconnect\r\n
0x70000010 | Interface\r\n
0x90000001 | Microsoft-Windows-NlaSvc\r\n
0x90000002 | Microsoft-Windows-NlaSvc/Diagnostic\r\n
0x90000003 | Microsoft-Windows-NlaSvc/Operational\r\n
0xb0000fa1 | Entered State: %2 Interface Guid: %1\r\n
0xb0000fa2 | Transitioning to State: %2 Interface Guid: %1\r\n
0xb0001005 | Received WMI Media Connect Notification for '%2' %1\r\n
0xb0001006 | Received WMI Media Disconnect Notification for '%2' %1\r\n
0xb0001007 | Route change has occurred for interface %1 (%2)\r\n
0xb0001008 | Address change has occurred for interface %1 (%2)\r\n
0xb0001009 | Quarantine state has changed\r\n
0xb000100a | Received DHCP notification\r\n
0xb0001069 | Start link resolver\r\n
0xb000106a | Stop link resolver\r\n
0xb000106b | Start gateway resolution on interface %1 for %2\r\n
0xb000106c | Stop gateway resolution on interface %1 for %2. Error: %3 NlnsState: %4 MAC: %6\r\n
0xb000106d | Gateway resolution failed on interface %1 for %2 with error: %3\r\n
0xb000109b | Plug-in data indicated from %1 for entity %2 (%3 rows)%n%5\r\n
0xb00010a5 | DHCP has stabilized for %1 (%2)\r\n
0xb00010cd | Start Intranet resolver\r\n
0xb00010ce | Stop Intranet resolver\r\n
0xb00010d7 | Start DsGetDcName(%1,%2) for DnsSuffix\r\n
0xb00010d8 | Stop DsGetDcName(%1,%2) for DnsSuffix returned error %3 (domain=%4, forest=%5)\r\n
0xb00010d9 | DsGetDcName(%1,%2) for DnsSuffix failed with error %3\r\n
0xb00010e1 | Start DsGetDcName(%2) for DS info\r\n
0xb00010e2 | Stop DsGetDcName(%2) for DS info returned error %3 (domain=%4, forest=%5)\r\n
0xb00010e3 | DsGetDcName(%2) for DS info failed with error %3\r\n
0xb00010eb | Start DsGetDcName(%2) for root domain GUID\r\n
0xb00010ec | Stop DsGetDcName(%2) for root domain GUID returned error %3 (domain=%4, forest=%5)\r\n
0xb00010ed | DsGetDcName(%2) for root domain GUID failed with error %3\r\n
0xb00010f5 | Start LDAP authentication on interface %1 (%2) (%3 tries)\r\n
0xb00010f6 | Stop LDAP authentication on interface %1 (%2)\r\n
0xb00010f7 | LDAP authentication on interface %1 (%2) failed with error %4\r\n
0xb00010ff | Start ldap_connect(%1) for DC=%2 (%3 of %4 tries)\r\n
0xb0001100 | Stop ldap_connect(%1) for DC=%2 (%3 of %4 tries)\r\n
0xb0001101 | ldap_connect(%1) for DC=%2 (%3 of %4 tries) failed with %5\r\n
0xb0001102 | Start ldap_bind(%1) for DC=%2 (%3 of %4 tries)\r\n
0xb0001103 | Stop ldap_bind(%1) for DC=%2 (%3 of %4 tries)\r\n
0xb0001104 | ldap_bind(%1) for DC=%2 (%3 of %4 tries) failed with %5\r\n
0xb0001131 | Inserting identifying signature for interface %1 %nSource=%4 Signature=%3\r\n
0xb0001132 | Inserting identified signature for interface %1 %nSource=%4 Signature=%3\r\n
0xb0001133 | Removing identified signature for interface %1 %nSource=%4 Signature=%3\r\n
0xb0001137 | Adding interface '%2' %1\r\n
0xb0001138 | Removing interface '%2' %1\r\n
0xb0001163 | Network on %1 is unlikely to be authentication-capable; authentication will continue in the background. %nReason: %2%n\r\n
0xb00017d5 | Perftrack cancel event for interface '%2' %1\r\n
0xd0000001 | Identifying Network\r\n
0xd0000002 | Identified Network\r\n
0xd0000003 | MibAddInstance\r\n
0xd0000004 | MibDeleteInstance\r\n
0xd0000005 | NlnsUnreachable\r\n
0xd0000006 | NlnsIncomplete\r\n
0xd0000007 | NlnsStale\r\n
0xd0000008 | NlnsDelay\r\n
0xd0000009 | NlnsProbe\r\n
0xd000000a | NlnsReachable\r\n
0xd000000b | NlnsPermanent\r\n
0xd000000c | NlnsMaximum\r\n
0xd000000d | DHCPCAPI_ADDR_STABLE\r\n
0xd000000e | DHCPCAPI_ADDR_NOT_STABLE_ACQ\r\n
0xd000000f | DHCPCAPI_ADDR_NOT_STABLE_DONE\r\n
0xd0000010 | DHCPCAPI_ADDR_NOT_STABLE_ACQ_CONT\r\n
0xd0000011 | NLA_STABLE_UNKNOWN\r\n
0xd0000012 | NLA_STABLE_STABLE\r\n
0xd0000013 | NLA_STABLE_GAVE_UP\r\n
0xd0000014 | NLA_STABLE_TRYING\r\n
0xd0000015 | LDAP has had no previous successes with the current combination of adapter addresses\r\n
0xd0000016 | This is the first LDAP attempt ever and a speculative timeout occurred\r\n
0xd0000017 | DS validation failed; there may not be a DC available on this network\r\n
0xf0000001 | DS_FORCE_REDISCOVERY\r\n
0xf0000002 | DS_IS_FLAT_NAME\r\n
0xf0000003 | DS_IS_DNS_NAME\r\n
0xf0000004 | DS_RETURN_DNS_NAME\r\n
0xf0000005 | DS_RETURN_FLAT_NAME\r\n
0xf0000006 | NLA_SIGNATURE_SOURCE_UNIDENTIFIED\r\n
0xf0000007 | NLA_SIGNATURE_SOURCE_IDENTIFYING\r\n
0xf0000008 | NLA_SIGNATURE_SOURCE_RANDOM\r\n
0xf0000009 | NLA_SIGNATURE_SOURCE_GATEWAY_MAC\r\n
0xf000000a | NLA_SIGNATURE_SOURCE_DOMAIN_GUID\r\n
0xf000000b | NLA_SIGNATURE_SOURCE_ROOT_DOMAIN_GUID\r\n
0xf000000c | NLA_SIGNATURE_SOURCE_DOMAIN_NAME\r\n
0xf000000d | NLA_SIGNATURE_SOURCE_FOREST_NAME\r\n
0xf000000e | NLA_SIGNATURE_SOURCE_DNS_SUFFIX\r\n
0xf000000f | NLA_SIGNATURE_SOURCE_LOCAL_INTERFACE_ID\r\n
0xf0000010 | NLA_SIGNATURE_SOURCE_WLAN_SSID\r\n
0xf0000011 | NLA_SIGNATURE_SOURCE_WLAN_PROFILE\r\n
0xf0000012 | NLA_SIGNATURE_SOURCE_WWAN\r\n
0xf0000013 | NLA_SIGNATURE_SOURCE_SECURITY_DOWNGRADE\r\n
0xf0000014 | NLA_SIGNATURE_SOURCE_PRIVATE\r\n
0xf0000015 | NLA_SIGNATURE_SOURCE_SECONDARY\r\n

### 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x10000031 | Response Time\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Wait for Identification\r\n
0x70000002 | Trigger\r\n
0x70000003 | Gateway Resolution\r\n
0x70000004 | Plugin\r\n
0x70000005 | Dhcp\r\n
0x70000006 | Intranet Resolution\r\n
0x70000007 | DsGetDcName(DnsSuffix)\r\n
0x70000008 | DsGetDcName(Ds)\r\n
0x70000009 | DsGetDcName(RootDomainGuid)\r\n
0x7000000a | Ldap Authentication\r\n
0x7000000b | ldap_connect\r\n
0x7000000c | ldap_bind\r\n
0x7000000d | Identifying\r\n
0x7000000e | Identified\r\n
0x7000000f | Disconnect\r\n
0x70000010 | Interface\r\n
0x90000001 | Microsoft-Windows-NlaSvc\r\n
0x90000002 | Microsoft-Windows-NlaSvc/Diagnostic\r\n
0x90000003 | Microsoft-Windows-NlaSvc/Operational\r\n
0xb0000fa1 | Entered State: %2 Interface Guid: %1\r\n
0xb0000fa2 | Transitioning to State: %2 Interface Guid: %1\r\n
0xb0001005 | Received WMI Media Connect Notification for '%2' %1\r\n
0xb0001006 | Received WMI Media Disconnect Notification for '%2' %1\r\n
0xb0001007 | Route change has occurred for interface %1 (%2)\r\n
0xb0001008 | Address change has occurred for interface %1 (%2)\r\n
0xb0001009 | Quarantine state has changed\r\n
0xb000100a | Received DHCP notification\r\n
0xb0001069 | Start link resolver\r\n
0xb000106a | Stop link resolver\r\n
0xb000106b | Start gateway resolution on interface %1 for %2\r\n
0xb000106c | Stop gateway resolution on interface %1 for %2. Error: %3 NlnsState: %4 MAC: %6\r\n
0xb000106d | Gateway resolution failed on interface %1 for %2 with error: %3\r\n
0xb000109b | Plug-in data indicated from %1 for entity %2 (%3 rows)%n%5\r\n
0xb00010a5 | DHCP has stabilized for %1 (%2)\r\n
0xb00010cd | Start Intranet resolver\r\n
0xb00010ce | Stop Intranet resolver\r\n
0xb00010d7 | Start DsGetDcName(%1,%2) for DnsSuffix\r\n
0xb00010d8 | Stop DsGetDcName(%1,%2) for DnsSuffix returned error %3 (domain=%4, forest=%5)\r\n
0xb00010d9 | DsGetDcName(%1,%2) for DnsSuffix failed with error %3\r\n
0xb00010e1 | Start DsGetDcName(%2) for DS info\r\n
0xb00010e2 | Stop DsGetDcName(%2) for DS info returned error %3 (domain=%4, forest=%5)\r\n
0xb00010e3 | DsGetDcName(%2) for DS info failed with error %3\r\n
0xb00010eb | Start DsGetDcName(%2) for root domain GUID\r\n
0xb00010ec | Stop DsGetDcName(%2) for root domain GUID returned error %3 (domain=%4, forest=%5)\r\n
0xb00010ed | DsGetDcName(%2) for root domain GUID failed with error %3\r\n
0xb00010f5 | Start LDAP authentication on interface %1 (%2) (%3 tries)\r\n
0xb00010f6 | Stop LDAP authentication on interface %1 (%2)\r\n
0xb00010f7 | LDAP authentication on interface %1 (%2) failed with error %4\r\n
0xb00010ff | Start ldap_connect(%1) for DC=%2 (%3 of %4 tries)\r\n
0xb0001100 | Stop ldap_connect(%1) for DC=%2 (%3 of %4 tries)\r\n
0xb0001101 | ldap_connect(%1) for DC=%2 (%3 of %4 tries) failed with %5\r\n
0xb0001102 | Start ldap_bind(%1) for DC=%2 (%3 of %4 tries)\r\n
0xb0001103 | Stop ldap_bind(%1) for DC=%2 (%3 of %4 tries)\r\n
0xb0001104 | ldap_bind(%1) for DC=%2 (%3 of %4 tries) failed with %5\r\n
0xb0001131 | Inserting identifying signature for interface %1 %nSource=%4 Signature=%3\r\n
0xb0001132 | Inserting identified signature for interface %1 %nSource=%4 Signature=%3\r\n
0xb0001133 | Removing identified signature for interface %1 %nSource=%4 Signature=%3\r\n
0xb0001137 | Adding interface '%2' %1\r\n
0xb0001138 | Removing interface '%2' %1\r\n
0xb0001163 | Network on %1 is unlikely to be authentication-capable; authentication will continue in the background. %nReason: %2%n\r\n
0xb000138a | Inserting identified signature for interface %1 %nSource=%2 Characteristics=%3\r\n
0xb00017d5 | Perftrack cancel event for interface '%2' %1\r\n
0xd0000001 | Identifying Network\r\n
0xd0000002 | Identified Network\r\n
0xd0000003 | MibAddInstance\r\n
0xd0000004 | MibDeleteInstance\r\n
0xd0000005 | NlnsUnreachable\r\n
0xd0000006 | NlnsIncomplete\r\n
0xd0000007 | NlnsStale\r\n
0xd0000008 | NlnsDelay\r\n
0xd0000009 | NlnsProbe\r\n
0xd000000a | NlnsReachable\r\n
0xd000000b | NlnsPermanent\r\n
0xd000000c | NlnsMaximum\r\n
0xd000000d | DHCPCAPI_ADDR_STABLE\r\n
0xd000000e | DHCPCAPI_ADDR_NOT_STABLE_ACQ\r\n
0xd000000f | DHCPCAPI_ADDR_NOT_STABLE_DONE\r\n
0xd0000010 | DHCPCAPI_ADDR_NOT_STABLE_ACQ_CONT\r\n
0xd0000011 | NLA_STABLE_UNKNOWN\r\n
0xd0000012 | NLA_STABLE_STABLE\r\n
0xd0000013 | NLA_STABLE_GAVE_UP\r\n
0xd0000014 | NLA_STABLE_TRYING\r\n
0xd0000015 | LDAP has had no previous successes with the current combination of adapter addresses\r\n
0xd0000016 | This is the first LDAP attempt ever and a speculative timeout occurred\r\n
0xd0000017 | DS validation failed; there may not be a DC available on this network\r\n
0xf0000001 | DS_FORCE_REDISCOVERY\r\n
0xf0000002 | DS_IS_FLAT_NAME\r\n
0xf0000003 | DS_IS_DNS_NAME\r\n
0xf0000004 | DS_RETURN_DNS_NAME\r\n
0xf0000005 | DS_RETURN_FLAT_NAME\r\n
0xf0000006 | NLA_SIGNATURE_SOURCE_UNIDENTIFIED\r\n
0xf0000007 | NLA_SIGNATURE_SOURCE_IDENTIFYING\r\n
0xf0000008 | NLA_SIGNATURE_SOURCE_RANDOM\r\n
0xf0000009 | NLA_SIGNATURE_SOURCE_GATEWAY_MAC\r\n
0xf000000a | NLA_SIGNATURE_SOURCE_DOMAIN_GUID\r\n
0xf000000b | NLA_SIGNATURE_SOURCE_ROOT_DOMAIN_GUID\r\n
0xf000000c | NLA_SIGNATURE_SOURCE_DOMAIN_NAME\r\n
0xf000000d | NLA_SIGNATURE_SOURCE_FOREST_NAME\r\n
0xf000000e | NLA_SIGNATURE_SOURCE_DNS_SUFFIX\r\n
0xf000000f | NLA_SIGNATURE_SOURCE_LOCAL_INTERFACE_ID\r\n
0xf0000010 | NLA_SIGNATURE_SOURCE_WLAN_SSID\r\n
0xf0000011 | NLA_SIGNATURE_SOURCE_WLAN_PROFILE\r\n
0xf0000012 | NLA_SIGNATURE_SOURCE_WWAN\r\n
0xf0000013 | NLA_SIGNATURE_SOURCE_SECURITY_DOWNGRADE\r\n
0xf0000014 | NLA_SIGNATURE_SOURCE_PRIVATE\r\n
0xf0000015 | NLA_SIGNATURE_SOURCE_SECONDARY\r\n
0xf0000016 | SIGCHAR_IDENTIFIED\r\n
0xf0000017 | SIGCHAR_DHCP_ENABLED\r\n
0xf0000018 | SIGCHAR_DNSSUFFIX_PRESENT\r\n
0xf0000019 | SIGCHAR_DNSSUFFIX_IS_DC\r\n
0xf000001a | SIGCHAR_AUTH_EXPECTED\r\n
0xf000001b | SIGCHAR_AUTHENTICATED\r\n
0xf000001c | SIGCHAR_V4_GW_CONSIDERED\r\n
0xf000001d | SIGCHAR_V4_GW_RESOLVED\r\n
0xf000001e | SIGCHAR_V6_GW_CONSIDERED\r\n
0xf000001f | SIGCHAR_V6_GW_RESOLVED\r\n
0xf0000020 | SIGCHAR_DC_ROLE\r\n
0xf0000021 | SIGCHAR_FIRST_CONNECT\r\n
0xf0000022 | SIGCHAR_MULTI_HOMED\r\n
0xf0000023 | SIGCHAR_MULTIPLE_SIGNATURES\r\n
