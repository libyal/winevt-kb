## polagent.dll

Path: %SystemRoot%\System32\polagent.dll

### 5.0.2195.6655

Message identifier | Message string
--- | ---
0x4bad0001 | %1 %2\r\n
0x4bad0002 | Policy Agent has not interface list.\r\n
0x4bad0003 | IPSec policy has been un-assigned.  No IPSec policy is currently active.\r\n
0x4bad0004 | Policy Agent did not update IPSEC policy. No changes detected.\r\n
0x4bad0005 | No filters were added to the main filter list. %1\r\n
0x4bad0006 | Policy contains no valid offers. %1\r\n
0x4bad0007 | Cached Policy in effect.\r\n
0x4bad0008 | Policy Agent attempted to insert an existing filter into IPSEC. \r\n
0x4bad0009 | Policy exists in policy table. \r\n
0x4bad000a | No matching policy found in the policy table.\r\n
0x4bad000b | Matching filter exists in associated policy.\r\n
0x4bad000c | Using Default policy.\r\n
0x4bad000d | Using Cached policy, as Active Directory Storage policy couldn't be applied successfully (network unreachable, policy integrity invalid, etc.).\r\n
0x4bad000e | Using the Active Local Registry policy, as (i) there's no Active Directory Storage policy or (ii) the Active Directory Storage policy couldn't be applied successfully and there's no Cached policy.\r\n
0x4bad000f | Using the Active Directory Storage policy.\r\n
0x4bad0010 | Not using any Ipsec policy, as (i) there's no Active Directory Storage or Active Local Registry policy or (ii) the Active Directory Storage policy couldn't be applied successfully and there's no Cached policy or no Active Local Registry policy.\r\n
0x4bad0011 | No IPSEC policy currently configured in the Active Directory.  Polling LSA for policy.\r\n
0x4bad0012 | Polling for new or modified policy. %1\r\n
0x4bad0013 | No IPSEC Policy information has been configured for this system.\r\n
0x4bad0014 | %1\r\n
0x4bad0015 | Service is shutting down.\r\n
0x4bad0016 | IPSec Policy agent started successfully.\r\n
0x4bad0017 | Polling had detected changes within the assigned Ipsec policy. Updated the policy successfully.\r\n
0x4bad0018 | Ip Public Help Api failed to get the Interface Table. Filters based on Interfaces will not be expanded and plumbed to the Ipsec Driver. %1\r\n
0x4bad0019 | Ip Public Help Api failed to get the IP Address Table. Filters based on Interfaces will not be expanded and plumbed to the Ipsec Driver. %1\r\n
0x4bad001a | IP address entry index not found in the Interface Table. Discarding the IP address.\r\n
0x8bad009c | Matching filter exists in filter list. \r\n
0x8bad009d | Default Policy already exists.\r\n
0x8bad009e | No IPSEC policy rules currently configured for this system.\r\n
0x8bad009f | IPSEC Policy Agent exiting normally.\r\n
0x8bad00a0 | Matching filter mirror exists in filter list. \r\n
0x8bad00a1 | Matching filter and mirror exists in filter list. \r\n
0x8bad00a2 | Some Parts of the expanded generic filter already exists in the driver.  \r\n
0x8bad00a3 | %1\r\n
0x8bad00a4 | WARNING! Policy in storage is a previous version (%1) than the version requested (%2)%nThis component may not behave as expected.  Default values will be used for any policy data not found in storage.%nIPSec policy storage should be upgraded to guarantee correct behavior.%n%nAdministrator's Note:%n%3\r\n
0x8bad00a5 | WARNING! Policy in storage is a more recent version (%1) than the version requested (%2)%nThis component may not behave as expected.  Some policy data in storage may be ignored.%nIPSec components should be upgraded to guarantee correct behavior.%n%nAdministrator's Note:%n %3\r\n
0x8bad00a6 | Number of Phase 1 offers greater than the maximum specified by Oakley. Extra offers have been truncated.\r\n
0x8bad00a7 | Number of Phase 2 offers greater than the maximum specified by Oakley. Extra offers have been truncated.\r\n
0x8bad00a8 | Zero Phase 1 offers. Discarding the ISAKMP policy.\r\n
0x8bad00a9 | Zero Phase 2 offers. Discarding the Negotiation policy.\r\n
0xcbad0100 | Policy Agent exhausted memory loading IPSEC policies.\r\n
0xcbad0101 | Policy Agent failed to load ISAKMP policy. %1\r\n
0xcbad0102 | Policy Agent failed to create a new policy table entry. \r\n
0xcbad0103 | Policy Agent failed to create a new policy in the Policy Table. \r\n
0xcbad0104 | IP Security Policy Agent could not be started.  No IP Security policy will be enforced. %1\r\n
0xcbad0105 | IP Security Policy Agent could not be started. No IP Security policy will be enforced. Unknown Error\r\n
0xcbad0106 | Policy Agent failed, shutting down. %1\r\n
0xcbad0107 | Policy Agent RPC Server failed to register protocol sequence.\r\n
0xcbad0108 | Policy Agent RPC Server failed to register interface. %1\r\n
0xcbad0109 | Policy Agent RPC Server failed to register interface bindings. %1\r\n
0xcbad010a | Policy Agent RPC Server failed to register interface endpoint. %1\r\n
0xcbad010b | Policy Agent RPC Server failed to register authentication mechanisms. %1\r\n
0xcbad010c | Policy Agent RPC Server failed to listen. %1\r\n
0xcbad010d | Policy Agent failed to start %1. Failed to connect to SCM Database.  Error: %2.\r\n
0xcbad010e | Policy Agent failed to start %1. Failed to open %1 Service. Error: %2\r\n
0xcbad010f | Policy Agent failed to start the %1 Service.  Error: %2\r\n
0xcbad0110 | Policy Agent failed to connect to the IPSEC Driver.  %1\r\n
0xcbad0111 | Policy Agent failed to load IPSEC policies.  %1\r\n
0xcbad0112 | Policy Agent failed to stop %1. Failed to connect to SCM Database. Error:  %2\r\n
0xcbad0113 | Policy Agent failed to stop %1. Failed to open the %1 Service.  Error: %2\r\n
0xcbad0114 | Policy Agent failed to stop the %1 Service.  Error: %2\r\n
0xcbad0115 | Policy Agent failed to connect to ISAKMP RPC interface.  Error %1\r\n
0xcbad0116 | Policy Agent failed to stop ISAKMP client RPC interface.  Error %1\r\n
0xcbad0117 | Not connected to ISAKMP client RPC interface.  Error %1\r\n
0xcbad0118 | Could not create or open ISAKMP policy exchange event. %1\r\n
0xcbad0119 | ISAKMP service is not available. \r\n
0xcbad011a | Policy Agent did not exchange ISAKMP Policy with ISAKMP Service. Error: %1\r\n
0xcbad011b | No polices exist.\r\n
0xcbad011c | Policy Agent failed to connect to the directory service.\r\n
0xcbad011d | Policy Agent failed to obtain Policy Distinguished Name. %1\r\n
0xcbad011e | Policy Agent failed to refresh a policy. %1\r\n
0xcbad011f | Failed to insert a filter into the Filter List. %1\r\n
0xcbad0120 | Policy Agent failed to instantiate a policy %1\r\n
0xcbad0121 | Failed to remove a filter from the Filter List. %1\r\n
0xcbad0122 | Parameters are ambiguous or conflicting.\r\n
0xcbad0123 | Policy identifier must be supplied.\r\n
0xcbad0124 | Policy exists in policy table. \r\n
0xcbad0125 | No matching policy found in the policy table.\r\n
0xcbad0126 | No matching filter in policy.\r\n
0xcbad0127 | Policy Agent Failed to start ISAKMP service.\r\n
0xcbad0128 | Could not add an entry to the IPSEC Policy table.\r\n
0xcbad0129 | Policy Agent failed to insert or update a filter in IPSEC. %1\r\n
0xcbad012a | Policy Agent failed to update a filter.\r\n
0xcbad012b | Policy Agent failed to update a policy. %1\r\n
0xcbad012c | Policy Agent failed to delete a policy. %1\r\n
0xcbad012d | Failed to instantiate IPSEC Policy. %1 \r\n
0xcbad012e | Failed to instantiate filters for policy. %1\r\n
0xcbad012f | Policy requires traffic be blocked.\r\n
0xcbad0130 | Failed to add RPC interface. %1\r\n
0xcbad0131 | Policy contains too many offers.\r\n
0xcbad0132 | Failed to create an offer list.\r\n
0xcbad0133 | A Secure communications policy cannot be enforced because the IP Security driver failed to start.  Contact your system administrator immediately.\r\n
0xcbad0134 | The IPSec policy assigned to this machine has a data format that is not supported.  No IPSec policy is currently active.\r\n
0xcbad0135 | %1\r\n
0xcbad0136 | Policy in storage is not supported. Policy in storage is version (%1.x).  This component only supports version (%2.x)%n  IPSec policy storage must be upgraded for stored policy to function properly.%n%nAdministrator's Note:%n%3\r\n
0xcbad0137 | Policy in storage is not supported. Policy in storage is version (%1.x).  This component only supports version (%2.x)%n IPSec components must be upgraded for stored policy to function properly.%n%nAdministrator's Note:%n%3\r\n
0xcbad0138 | No policy storage was found for the specified provider.%n%nAdministrator's Note:%n%1\r\n
0xcbad0139 | No policy version information was found.  IPSec stored policies cannot be retrieved.  Contact your administrator immediately.%n\r\n
0xcbad013a | Failed to insert a filter into the Ipsec Driver. %1\r\n
0xcbad013b | Failed to delete a filter from the Ipsec Driver. %1\r\n
0xcbad013c | Failed to plumb ISAKMP/IKE (Phase 1) policy into Oakley.\r\n
0xcbad013d | Failed to plumb IPSEC (Phase 2) policy into Oakley.\r\n
0xcbad013e | Failed to remove IPSEC (Phase 2) policy from Oakley.\r\n
0xcbad013f | IPSEC PolicyAgent Service couldn't be started: Oakley failed to start.\r\n
0xcbad0140 | IPSEC PolicyAgent Service couldn't be started: Failed to create the event for GP Notification.\r\n
0xcbad0141 | IPSEC PolicyAgent Service: Ipsec Driver failed to start.\r\n
