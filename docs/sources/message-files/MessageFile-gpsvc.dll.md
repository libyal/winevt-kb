## gpsvc.dll

Path: %SystemRoot%\system32\gpsvc.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x000003ea | The processing of Group Policy failed because of a system allocation failure. Please ensure the computer is not running low on resources (memory, available disk space). Group Policy processing will be attempted at the next refresh cycle.\r\n
0x000003ee | The processing of Group Policy failed. Windows could not authenticate to the Active Directory service on a domain controller. (LDAP Bind function call failed). Look in the details tab for error code and description.\r\n
0x000003ef | The processing of Group Policy failed. Windows could not determine the site associated for this computer, which is required for Group Policy processing.\r\n
0x00000406 | The processing of Group Policy failed. Windows attempted to retrieve new Group Policy settings for this user or computer. Look in the details tab for error code and description. Windows will automatically retry this operation at the next refresh cycle. Computers joined to the domain must have proper name resolution and network connectivity to a domain controller for discovery of new Group Policy objects and settings. An event will be logged when Group Policy is successful.\r\n
0x0000041c | The processing of Group Policy failed. Windows could not determine the role of this computer. Role information (Workgroup, Member Server, or Domain Controller) is required to process Group Policy.\r\n
0x0000041d | The processing of Group Policy failed. Windows could not resolve the user name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x0000041e | The processing of Group Policy failed. Windows could not obtain the name of a domain controller. This could be caused by a name resolution failure. Verify your Domain Name Sysytem (DNS) is configured and working correctly.\r\n
0x0000041f | The processing of Group Policy failed. Windows could not resolve the computer name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x00000422 | The processing of Group Policy failed. Windows attempted to read the file %9 from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: %na) Name Resolution/Network Connectivity to the current domain controller. %nb) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller). %nc) The Distributed File System (DFS) client has been disabled.\r\n
0x00000429 | The processing of Group Policy failed. Windows could not evaluate the Windows Management Instrumentation (WMI) filter for the Group Policy object %8. This could be caused by RSOP being disabled  or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Make sure the WMI service is started and the startup type is set to automatic. New Group Policy objects or settings will not process until this event has been resolved.\r\n
0x0000042c | The processing of Group Policy was interrupted. Windows prematurely ended the discovery and enforcement of Group Policy settings because the computer was requested to shutdown or the user logged off. Group Policy processing will be attempted next refresh cycle, on the next computer reboot, or the next user logon.\r\n
0x00000437 | The processing of Group Policy failed. Windows could not obtain the list of Group Policy objects applicable for this computer or user. View the event details for more information.\r\n
0x00000438 | The processing of Group Policy failed. Windows could not search the Active Directory organization unit hierarchy. View the event details for more information.\r\n
0x0000043d | Windows failed to apply the %8 settings. %8 settings might have its own log file. Please click on the "More information" link.\r\n
0x00000440 | The processing of Group Policy failed. Windows attempted to query the list of Group Policy objects and exceeded the maximum limit (999).\r\n
0x00000441 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by RSOP being disabled or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000442 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000443 | Windows could not record  the Resultant Set of Policy (RSoP) information for the Group Policy extension <%8>. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000447 | Windows encountered an error while recording Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000448 | The processing of Group Policy failed. Windows could not apply the registry-based policy settings for the Group Policy object %8. Group Policy settings will not be resolved until this event is resolved. View the event details for more information on the file name and path that caused the failure.\r\n
0x00000449 | The processing of Group Policy failed. Windows could not determine the computer account to enforce Group Policy settings. This may be transient. Group Policy settings, including computer configuration, will not be enforced for this computer.\r\n
0x0000044d | The processing of Group Policy failed. Windows could not locate the directory object %8. Group Policy settings will not be enforced until this event is resolved. View the event details for more information on this error.\r\n
0x00000450 | Windows was unable to read the Windows Management Instrumentation (WMI) filter information associated with the Group Policy object %8.This may be caused by a deleted WMI Filter defined in the domain that is still in use by Group Policy objects. Group Policy settings for this Group Policy object will not be enforced. Other Group Policy objects may still apply. Windows will attempt to retrieve this information at the next policy cycle. This speciffic problem may be resolved by identifying all GPOs that reference the WMI filter and removing the references. Contact an administrator if this event recurs for several hours.\r\n
0x00000455 | The user account is in a different forest than the computer account. The processing of Group Policy from another forest is not allowed. Group Policy will be processed using Loopback Replace mode. The scope of the user policy settings will be determined by the location of the computer object in Active Directory. The settings will be aquired from the User Configuration of these policies.\r\n
0x00000456 | The processing of Group Policy failed. Windows could not determine if the user and computer accounts are in the same forest. Ensure the user domain name matches the name of a trusted domain that resides in the same forest as the computer account.\r\n
0x00000458 | The Group Policy Client Side Extension %8 was unable to apply one or more settings because the changes must be processed before system startup or user logon. The system will wait for Group Policy processing to finish completely before the next startup or logon for this user, and this may result in slow startup and boot performance.\r\n
0x00000465 | The processing of Group Policy failed because of an internal system error. Please see the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000466 | Windows was unable to determine whether new Group Policy settings defined by a network administrator should be enforced for this user or computer because this computer's clock is not synchronized with the clock of one of the domain controllers for the domain. Because of this issue, this computer system may not be in compliance with the network administrator’s requirements, and users of this system may not be able to use some functionality on the network. Windows will periodically attempt to retry this operation, and it is possible that either this system or the domain controller will correct the time settings without intervention by an administrator, so the problem will be corrected. %n%nIf this issue persists for more than an hour, checking the local system's clock settings to ensure they are accurate and are synchronized with the clocks on the network's domain controllers is one way to resolve this problem. A network administrator may be required to resolve the issue if correcting the local time settings does not address the problem.\r\n
0x00000467 | The processing of Group Policy failed due to an internal error. Please look into the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000468 | The Group Policy Client Side Extension %3 may have caused the Group Policy Service to terminate unexpectedly. To prevent further failures in the Group Policy Service, this extension has been temporarily disabled until after the next system restart. Group Policy settings managed by this extension may no longer be enforced until the system is restarted. The vendor of this extension should be contacted if this issue recurs.\r\n
0x00000469 | The processing of Group Policy failed because of lack of network connectivity to a domain controller. This may be a transient condition. A success message would be generated once the machine gets connected to the domain controller and Group Policy has succesfully processed. If you do not see a success message for several hours, then contact your administrator.\r\n
0x0000046a | %5 failed. %n%tGPO Name : %6%n%tGPO File System Path : %7%n%tScript Name: %8\r\n
0x000005dc | The Group Policy settings for the computer were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005dd | The Group Policy settings for the user were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005de | The Group Policy settings for the computer were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x000005df | The Group Policy settings for the user were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x00001000 | Retrieving Domain Controller details.\r\n
0x00001001 | Forcing re-discovery of Domain Controller details.\r\n
0x00001002 | Network state change detected.\r\n
0x00001003 | seconds\r\n
0x00001004 | minutes\r\n
0x00001005 | No changes were detected.\r\n
0x00001006 | Changes were detected.\r\n
0x00001007 | Group Policy wait for network subsystem failed at computer boot. Group Policy processing will continue.\r\n
0x00001008 | Group Policy cannot be applied because the computer has been booted in Directory Services Restore Mode.\r\n
0x00001009 | Access check based on security descriptor failed.\r\n
0x0000100a | Startup scripts are not visible. Startup scripts are visible only when startup scripts are configured to run synchronously.\r\n
0x0000100b | Failed to get the active console session.\r\n
0x0000100c | Group Policy refresh access check failed.\r\n
0x0000100d | Group Policy notify access check failed.\r\n
0x0000100e | Group Policy notify access check for console session failed.\r\n
0x0000100f | Policy to deny users from refreshing computer policy is set.\r\n
0x00001010 | slow\r\n
0x00001011 | fast\r\n
0x00001012 | Attempting to retrieve the account information.\r\n
0x00001013 | Retrieved account information.\r\n
0x00001014 | Retrying to retrieve account information.\r\n
0x00001015 | Making system call to get account information.\r\n
0x00001016 | The system call to get account information completed.\r\n
0x00001017 | Making LDAP calls to connect and bind to Active Directory.\r\n
0x00001018 | The LDAP call to connect and bind to Active Directory completed.\r\n
0x00001019 | Bandwidth estimation failure: Failed to refresh network data associated with query.\r\n
0x0000101a | Bandwidth estimation failure: Failed to enumerate network signatures associated with query.\r\n
0x0000101b | Bandwidth estimation failure: Failed to query Intranet capability.\r\n
0x0000101c | Bandwidth estimation failure: Failed to inspect result of NLA query.\r\n
0x0000101d | Failed to register for connectivity notification.\r\n
0x0000101e | Failed to query information about security package.\r\n
0x0000101f | Failed to acquire handle to preexisting credentials of security principal.\r\n
0x00001020 | Failed to initiate security context.\r\n
0x00001021 | Failed to establish security context.\r\n
0x00001022 | Failed to obtain access token for security context.\r\n
0x00001023 | Making system calls to access specified file.\r\n
0x00001024 | The system calls to access specified file completed.\r\n
0x00001025 | Failed to determine the Group Policy properties of the installed system. Only a subset of Group Policy functionality will be available.\r\n
0x00001026 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon.\r\n
0x00001027 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon for a maximum of 120 seconds.\r\n
0x00001040 | Initializing and reading current service configuration for the Group Policy Client service.\r\n
0x00001041 | Checking for Group Policy client extensions that are not part of the system.\r\n
0x00001042 | Service configuration must be updated to standalone due to the presence of a Group Policy client extension that is not part of the operating system.\r\n
0x00001043 | Service configuration update to standalone is not required and will be skipped.\r\n
0x00001044 | Attempting to update service configuration to standalone.\r\n
0x00001045 | Finished checking for non-system extensions.\r\n
0x00001046 | Initializing service instance state to detect previous instances of the service.\r\n
0x00001047 | A previous instance of the Group Policy Client Service has been detected.\r\n
0x00001048 | The Group Policy Client service is currently configured as a shared service.\r\n
0x00001049 | The Group Policy Client service is currently configured as a standalone service.\r\n
0x90000001 | Microsoft-Windows-GroupPolicy\r\n
0x90000002 | Microsoft-Windows-GroupPolicy/Operational\r\n
0xb0000fa0 | Starting computer boot policy processing for %2. %nActivity id: %1\r\n
0xb0000fa1 | Starting user logon Policy processing for %2. %nActivity id: %1\r\n
0xb0000fa2 | Starting policy processing due to network state change for computer %2. %nActivity id: %1\r\n
0xb0000fa3 | Starting policy processing due to network state change for user %2. %nActivity id: %1\r\n
0xb0000fa4 | Starting manual processing of policy for computer %2. %nActivity id: %1\r\n
0xb0000fa5 | Starting manual processing of policy for user %2. %nActivity id: %1\r\n
0xb0000fa6 | Starting periodic policy processing for computer %2. %nActivity id: %1\r\n
0xb0000fa7 | Starting periodic policy processing for user %2. %nActivity id: %1\r\n
0xb0000fb0 | Starting %2 Extension Processing. %n%nList of applicable Group Policy objects: (%5)%n%n%6\r\n
0xb0000fb1 | %1 %n%2\r\n
0xb0000fb2 | Starting %2 for %1.\r\n
0xb0000fb3 | Running script name %1.\r\n
0xb00010e6 | Group Policy is trying to discover the Domain Controller information.\r\n
0xb0001398 | Completed %3 Extension Processing in %1 milliseconds.\r\n
0xb0001399 | %3 %n%4%nThe call completed in %1 milliseconds.\r\n
0xb000139a | Completed %4 for %3 in %1 seconds.\r\n
0xb000139b | Completed %3 in %1 seconds.\r\n
0xb00014bc | Domain Controller details: %n%tDomain Controller Name : %1%n%tDomain Controller IP Address : %2\r\n
0xb00014bd | Computer details: %n%tComputer role : %1%n%tNetwork name : %2\r\n
0xb00014be | Account details: %n%tAccount Name : %1%n%tAccount Domain Name : %2%n%tDC Name : %3%n%tDC Domain Name : %4\r\n
0xb00014bf | The loopback policy processing mode is %1.\r\n
0xb00014c0 | List of applicable Group Policy objects: %n%n%1\r\n
0xb00014c1 | The following Group Policy objects were not applicable because they were filtered out : %n%n%1\r\n
0xb00014c2 | A %6 link was detected. The Estimated bandwidth is %1 kbps. The slow link threshold is %3 kbps.\r\n
0xb00014c3 | Next policy processing for %1 will be attempted in %2 %3.\r\n
0xb00014c8 | %1\r\n
0xb00014c9 | %1 Parameter: %2\r\n
0xb00014ca | Group policy waited for %3 milliseconds for the network subsystem at computer boot.\r\n
0xb00014cc | Group Policy received the notification %1 from Winlogon for session %2.\r\n
0xb00014cd | Group Policy received %1 notification from Service Control Manager.\r\n
0xb00014ce | Group Policy successfully discovered the Domain Controller in %1 milliseconds.\r\n
0xb00014cf | Estimated network bandwidth on one of the connections: %1 kbps.\r\n
0xb00014d3 | Service configuration update to standalone was attempted due to the presence of Group Policy client extension %1 that is not part of the operating system and completed with status %3.\r\n
0xb0001770 | Invalid Error Message.\r\n
0xb00018aa | Group policy bandwidth estimation failed. Group policy processing will continue. Assuming %6 link.\r\n
0xb00018b0 | Warning: %1 Warning code %2.\r\n
0xb00018b1 | Warning: %1 Parameter: %3 : Warning code %2.\r\n
0xb00018b3 | Group Policy dependency (%1) did not start. As a result, network related features of Group Policy such as bandwidth estimation and response to network changes will not work.\r\n
0xb00018ba | An unfinished invocation of the Group Policy Client Side Extension %1 from a previous instance of the Group Policy Service has been detected.  This may indicate that the extension caused the Group Policy Client Service to terminate unexpectedly.\r\n
0xb0001b58 | Computer boot policy processing failed for %3 in %1 seconds.\r\n
0xb0001b59 | User logon policy processing failed for %3 in %1 seconds.\r\n
0xb0001b5a | Policy processing due to network state change failed for computer %3 in %1 seconds.\r\n
0xb0001b5b | Policy processing due to network state change failed for user %3 in %1 seconds.\r\n
0xb0001b5c | Manual processing of policy failed for computer %3 in %1 seconds.\r\n
0xb0001b5d | Manual processing of policy failed for user %3 in %1 seconds.\r\n
0xb0001b5e | Periodic policy processing failed for computer %3 in %1 seconds.\r\n
0xb0001b5f | Periodic policy processing failed for user %3 in %1 seconds.\r\n
0xb0001b69 | %3 %n%4%nThe call failed after %1 milliseconds.\r\n
0xb0001b6a | Script for %3 failed in %1 seconds.\r\n
0xb0001c98 | Error: %1 Error code %2.\r\n
0xb0001c99 | Error: %1 Parameter: %3 : Error code %2.\r\n
0xb0001c9e | Group Policy failed to discover the Domain Controller details in %1 milliseconds.\r\n
0xb0001f40 | Completed computer boot policy processing for %3 in %1 seconds.\r\n
0xb0001f41 | Completed user logon policy processing for %3 in %1 seconds.\r\n
0xb0001f42 | Completed policy processing due to network state change for computer %3 in %1 seconds.\r\n
0xb0001f43 | Completed policy processing due to network state change for user %3 in %1 seconds.\r\n
0xb0001f44 | Completed manual processing of policy for computer %3 in %1 seconds.\r\n
0xb0001f45 | Completed manual processing of policy for user %3 in %1 seconds.\r\n
0xb0001f46 | Completed periodic policy processing for computer %3 in %1 seconds.\r\n
0xb0001f47 | Completed periodic policy processing for user %3 in %1 seconds.\r\n
0xd0000001 | No need for synchronous\r\n
0xd0000002 | First policy refresh\r\n
0xd0000003 | CSE requires foreground\r\n
0xd0000004 | CSE returned error\r\n
0xd0000005 | Forced synchronous refresh\r\n
0xd0000006 | Synchronous policy\r\n
0xd0000007 | SKU\r\n
0xd0000008 | Scripts synchronous\r\n
0xd0000009 | Synchronous due to internal processing error\r\n
0xd000000a | Background\r\n
0xd000000b | Foreground synchronous\r\n
0xd000000c | Foreground asynchronous\r\n
0xd000000d | "No loopback mode"\r\n
0xd000000e | "Merge"\r\n
0xd000000f | "Replace"\r\n
0xd0000010 | Startup script\r\n
0xd0000011 | Logon script\r\n
0xd0000012 | Logoff script\r\n
0xd0000013 | Shutdown script\r\n
0xd0000014 | User\r\n
0xd0000015 | Computer\r\n
0xd0000016 | CreateSession\r\n
0xd0000017 | Logon\r\n
0xd0000018 | Logoff\r\n
0xd0000019 | StartShell\r\n
0xd000001a | EndShell\r\n
0xd000001b | Preshutdown\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x000003ea | The processing of Group Policy failed because of a system allocation failure. Please ensure the computer is not running low on resources (memory, available disk space). Group Policy processing will be attempted at the next refresh cycle.\r\n
0x000003ee | The processing of Group Policy failed. Windows could not authenticate to the Active Directory service on a domain controller. (LDAP Bind function call failed). Look in the details tab for error code and description.\r\n
0x000003ef | The processing of Group Policy failed. Windows could not determine the site associated for this computer, which is required for Group Policy processing.\r\n
0x00000406 | The processing of Group Policy failed. Windows attempted to retrieve new Group Policy settings for this user or computer. Look in the details tab for error code and description. Windows will automatically retry this operation at the next refresh cycle. Computers joined to the domain must have proper name resolution and network connectivity to a domain controller for discovery of new Group Policy objects and settings. An event will be logged when Group Policy is successful.\r\n
0x0000041c | The processing of Group Policy failed. Windows could not determine the role of this computer. Role information (Workgroup, Member Server, or Domain Controller) is required to process Group Policy.\r\n
0x0000041d | The processing of Group Policy failed. Windows could not resolve the user name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x0000041e | The processing of Group Policy failed. Windows could not obtain the name of a domain controller. This could be caused by a name resolution failure. Verify your Domain Name System (DNS) is configured and working correctly.\r\n
0x0000041f | The processing of Group Policy failed. Windows could not resolve the computer name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x00000422 | The processing of Group Policy failed. Windows attempted to read the file %9 from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: %na) Name Resolution/Network Connectivity to the current domain controller. %nb) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller). %nc) The Distributed File System (DFS) client has been disabled.\r\n
0x00000429 | The processing of Group Policy failed. Windows could not evaluate the Windows Management Instrumentation (WMI) filter for the Group Policy object %8. This could be caused by RSOP being disabled  or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Make sure the WMI service is started and the startup type is set to automatic. New Group Policy objects or settings will not process until this event has been resolved.\r\n
0x0000042c | The processing of Group Policy was interrupted. Windows prematurely ended the discovery and enforcement of Group Policy settings because the computer was requested to shutdown or the user logged off. Group Policy processing will be attempted next refresh cycle, on the next computer reboot, or the next user logon.\r\n
0x00000437 | The processing of Group Policy failed. Windows could not obtain the list of Group Policy objects applicable for this computer or user. View the event details for more information.\r\n
0x00000438 | The processing of Group Policy failed. Windows could not search the Active Directory organization unit hierarchy. View the event details for more information.\r\n
0x0000043d | Windows failed to apply the %8 settings. %8 settings might have its own log file. Please click on the "More information" link.\r\n
0x00000440 | The processing of Group Policy failed. Windows attempted to query the list of Group Policy objects and exceeded the maximum limit (999).\r\n
0x00000441 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by RSOP being disabled or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000442 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000443 | Windows could not record  the Resultant Set of Policy (RSoP) information for the Group Policy extension <%8>. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000447 | Windows encountered an error while recording Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000448 | The processing of Group Policy failed. Windows could not apply the registry-based policy settings for the Group Policy object %8. Group Policy settings will not be resolved until this event is resolved. View the event details for more information on the file name and path that caused the failure.\r\n
0x00000449 | The processing of Group Policy failed. Windows could not determine the computer account to enforce Group Policy settings. This may be transient. Group Policy settings, including computer configuration, will not be enforced for this computer.\r\n
0x0000044d | The processing of Group Policy failed. Windows could not locate the directory object %8. Group Policy settings will not be enforced until this event is resolved. View the event details for more information on this error.\r\n
0x00000450 | Windows was unable to read the Windows Management Instrumentation (WMI) filter information associated with the Group Policy object %8.This may be caused by a deleted WMI Filter defined in the domain that is still in use by Group Policy objects. Group Policy settings for this Group Policy object will not be enforced. Other Group Policy objects may still apply. Windows will attempt to retrieve this information at the next policy cycle. This speciffic problem may be resolved by identifying all GPOs that reference the WMI filter and removing the references. Contact an administrator if this event recurs for several hours.\r\n
0x00000455 | The user account is in a different forest than the computer account. The processing of Group Policy from another forest is not allowed. Group Policy will be processed using Loopback Replace mode. The scope of the user policy settings will be determined by the location of the computer object in Active Directory. The settings will be aquired from the User Configuration of these policies.\r\n
0x00000456 | The processing of Group Policy failed. Windows could not determine if the user and computer accounts are in the same forest. Ensure the user domain name matches the name of a trusted domain that resides in the same forest as the computer account.\r\n
0x00000458 | The Group Policy Client Side Extension %8 was unable to apply one or more settings because the changes must be processed before system startup or user logon. The system will wait for Group Policy processing to finish completely before the next startup or logon for this user, and this may result in slow startup and boot performance.\r\n
0x00000465 | The processing of Group Policy failed because of an internal system error. Please see the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000466 | Windows was unable to determine whether new Group Policy settings defined by a network administrator should be enforced for this user or computer because this computer's clock is not synchronized with the clock of one of the domain controllers for the domain. Because of this issue, this computer system may not be in compliance with the network administrator’s requirements, and users of this system may not be able to use some functionality on the network. Windows will periodically attempt to retry this operation, and it is possible that either this system or the domain controller will correct the time settings without intervention by an administrator, so the problem will be corrected. %n%nIf this issue persists for more than an hour, checking the local system's clock settings to ensure they are accurate and are synchronized with the clocks on the network's domain controllers is one way to resolve this problem. A network administrator may be required to resolve the issue if correcting the local time settings does not address the problem.\r\n
0x00000467 | The processing of Group Policy failed due to an internal error. Please look into the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000468 | The Group Policy Client Side Extension %3 may have caused the Group Policy Service to terminate unexpectedly. To prevent further failures in the Group Policy Service, this extension has been temporarily disabled until after the next system restart. Group Policy settings managed by this extension may no longer be enforced until the system is restarted. The vendor of this extension should be contacted if this issue recurs.\r\n
0x00000469 | The processing of Group Policy failed because of lack of network connectivity to a domain controller. This may be a transient condition. A success message would be generated once the machine gets connected to the domain controller and Group Policy has succesfully processed. If you do not see a success message for several hours, then contact your administrator.\r\n
0x0000046a | %5 failed. %n%tGPO Name : %6%n%tGPO File System Path : %7%n%tScript Name: %8\r\n
0x000005dc | The Group Policy settings for the computer were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005dd | The Group Policy settings for the user were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005de | The Group Policy settings for the computer were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x000005df | The Group Policy settings for the user were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x00001000 | Retrieving Domain Controller details.\r\n
0x00001001 | Forcing re-discovery of Domain Controller details.\r\n
0x00001002 | Network state change detected.\r\n
0x00001003 | seconds\r\n
0x00001004 | minutes\r\n
0x00001005 | No changes were detected.\r\n
0x00001006 | Changes were detected.\r\n
0x00001007 | Group Policy wait for network subsystem failed at computer boot. Group Policy processing will continue.\r\n
0x00001008 | Group Policy cannot be applied because the computer has been booted in Directory Services Restore Mode.\r\n
0x00001009 | Access check based on security descriptor failed.\r\n
0x0000100a | Startup scripts are not visible. Startup scripts are visible only when startup scripts are configured to run synchronously.\r\n
0x0000100b | Failed to get the active console session.\r\n
0x0000100c | Group Policy refresh access check failed.\r\n
0x0000100d | Group Policy notify access check failed.\r\n
0x0000100e | Group Policy notify access check for console session failed.\r\n
0x0000100f | Policy to deny users from refreshing computer policy is set.\r\n
0x00001010 | slow\r\n
0x00001011 | fast\r\n
0x00001012 | Attempting to retrieve the account information.\r\n
0x00001013 | Retrieved account information.\r\n
0x00001014 | Retrying to retrieve account information.\r\n
0x00001015 | Making system call to get account information.\r\n
0x00001016 | The system call to get account information completed.\r\n
0x00001017 | Making LDAP calls to connect and bind to Active Directory.\r\n
0x00001018 | The LDAP call to connect and bind to Active Directory completed.\r\n
0x00001019 | Bandwidth estimation failure: Failed to refresh network data associated with query.\r\n
0x0000101a | Bandwidth estimation failure: Failed to enumerate network signatures associated with query.\r\n
0x0000101b | Bandwidth estimation failure: Failed to query Intranet capability.\r\n
0x0000101c | Bandwidth estimation failure: Failed to inspect result of NLA query.\r\n
0x0000101d | Failed to register for connectivity notification.\r\n
0x0000101e | Failed to query information about security package.\r\n
0x0000101f | Failed to acquire handle to preexisting credentials of security principal.\r\n
0x00001020 | Failed to initiate security context.\r\n
0x00001021 | Failed to establish security context.\r\n
0x00001022 | Failed to obtain access token for security context.\r\n
0x00001023 | Making system calls to access specified file.\r\n
0x00001024 | The system calls to access specified file completed.\r\n
0x00001025 | Failed to determine the Group Policy properties of the installed system. Only a subset of Group Policy functionality will be available.\r\n
0x00001026 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon.\r\n
0x00001027 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon for a maximum of 120 seconds.\r\n
0x00001040 | Initializing and reading current service configuration for the Group Policy Client service.\r\n
0x00001041 | Checking for Group Policy client extensions that are not part of the system.\r\n
0x00001042 | Service configuration must be updated to standalone due to the presence of a Group Policy client extension that is not part of the operating system.\r\n
0x00001043 | Service configuration update to standalone is not required and will be skipped.\r\n
0x00001044 | Attempting to update service configuration to standalone.\r\n
0x00001045 | Finished checking for non-system extensions.\r\n
0x00001046 | Initializing service instance state to detect previous instances of the service.\r\n
0x00001047 | A previous instance of the Group Policy Client Service has been detected.\r\n
0x00001048 | The Group Policy Client service is currently configured as a shared service.\r\n
0x00001049 | The Group Policy Client service is currently configured as a standalone service.\r\n
0x00001050 | Computer determined to be not in a site.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-GroupPolicy\r\n
0x90000002 | System\r\n
0x90000003 | Microsoft-Windows-GroupPolicy/Operational\r\n
0xb0000fb0 | Starting %2 Extension Processing. %n%nList of applicable Group Policy objects: (%5)%n%n%6\r\n
0xb0000fb1 | %1 %n%2\r\n
0xb0000fb2 | Starting %2 for %1.\r\n
0xb0000fb3 | Running script name %1.\r\n
0xb00010e6 | Group Policy is trying to discover the Domain Controller information.\r\n
0xb0001398 | Completed %3 Extension Processing in %1 milliseconds.\r\n
0xb0001399 | %3 %n%4%nThe call completed in %1 milliseconds.\r\n
0xb000139a | Completed %4 for %3 in %1 seconds.\r\n
0xb000139b | Completed %3 in %1 seconds.\r\n
0xb00014bc | Domain Controller details: %n%tDomain Controller Name : %1%n%tDomain Controller IP Address : %2\r\n
0xb00014bd | Computer details: %n%tComputer role : %1%n%tNetwork name : %2\r\n
0xb00014be | Account details: %n%tAccount Name : %1%n%tAccount Domain Name : %2%n%tDC Name : %3%n%tDC Domain Name : %4\r\n
0xb00014bf | The loopback policy processing mode is %1.\r\n
0xb00014c0 | List of applicable Group Policy objects: %n%n%1\r\n
0xb00014c1 | The following Group Policy objects were not applicable because they were filtered out : %n%n%1\r\n
0xb00014c2 | A %6 link was detected. The Estimated bandwidth is %1 kbps. The slow link threshold is %3 kbps.\r\n
0xb00014c3 | Next policy processing for %1 will be attempted in %2 %3.\r\n
0xb00014c8 | %1\r\n
0xb00014c9 | %1 Parameter: %2\r\n
0xb00014ca | Group policy waited for %3 milliseconds for the network subsystem at computer boot.\r\n
0xb00014cc | Group Policy received the notification %1 from Winlogon for session %2.\r\n
0xb00014cd | Group Policy received %1 notification from Service Control Manager.\r\n
0xb00014ce | Group Policy successfully discovered the Domain Controller in %1 milliseconds.\r\n
0xb00014cf | Estimated network bandwidth on one of the connections: %1 kbps.\r\n
0xb00014d3 | Service configuration update to standalone was attempted due to the presence of Group Policy client extension %1 that is not part of the operating system and completed with status %3.\r\n
0xb0001770 | Invalid Error Message.\r\n
0xb00018aa | Group policy bandwidth estimation failed. Group policy processing will continue. Assuming %6 link.\r\n
0xb00018b0 | Warning: %1 Warning code %2.\r\n
0xb00018b1 | Warning: %1 Parameter: %3 : Warning code %2.\r\n
0xb00018b3 | Group Policy dependency (%1) did not start. As a result, network related features of Group Policy such as bandwidth estimation and response to network changes will not work.\r\n
0xb00018ba | An unfinished invocation of the Group Policy Client Side Extension %1 from a previous instance of the Group Policy Service has been detected.  This may indicate that the extension caused the Group Policy Client Service to terminate unexpectedly.\r\n
0xb0001b69 | %3 %n%4%nThe call failed after %1 milliseconds.\r\n
0xb0001b6a | Script for %3 failed in %1 seconds.\r\n
0xb0001c98 | Error: %1 Error code %2.\r\n
0xb0001c99 | Error: %1 Parameter: %3 : Error code %2.\r\n
0xb0001c9e | Group Policy failed to discover the Domain Controller details in %1 milliseconds.\r\n
0xb0010fa0 | Starting computer boot policy processing for %2. %nActivity id: %1\r\n
0xb0010fa1 | Starting user logon Policy processing for %2. %nActivity id: %1\r\n
0xb0010fa2 | Starting policy processing due to network state change for computer %2. %nActivity id: %1\r\n
0xb0010fa3 | Starting policy processing due to network state change for user %2. %nActivity id: %1\r\n
0xb0010fa4 | Starting manual processing of policy for computer %2. %nActivity id: %1\r\n
0xb0010fa5 | Starting manual processing of policy for user %2. %nActivity id: %1\r\n
0xb0010fa6 | Starting periodic policy processing for computer %2. %nActivity id: %1\r\n
0xb0010fa7 | Starting periodic policy processing for user %2. %nActivity id: %1\r\n
0xb0011b58 | Computer boot policy processing failed for %3 in %1 seconds.\r\n
0xb0011b59 | User logon policy processing failed for %3 in %1 seconds.\r\n
0xb0011b5a | Policy processing due to network state change failed for computer %3 in %1 seconds.\r\n
0xb0011b5b | Policy processing due to network state change failed for user %3 in %1 seconds.\r\n
0xb0011b5c | Manual processing of policy failed for computer %3 in %1 seconds.\r\n
0xb0011b5d | Manual processing of policy failed for user %3 in %1 seconds.\r\n
0xb0011b5e | Periodic policy processing failed for computer %3 in %1 seconds.\r\n
0xb0011b5f | Periodic policy processing failed for user %3 in %1 seconds.\r\n
0xb0011f40 | Completed computer boot policy processing for %3 in %1 seconds.\r\n
0xb0011f41 | Completed user logon policy processing for %3 in %1 seconds.\r\n
0xb0011f42 | Completed policy processing due to network state change for computer %3 in %1 seconds.\r\n
0xb0011f43 | Completed policy processing due to network state change for user %3 in %1 seconds.\r\n
0xb0011f44 | Completed manual processing of policy for computer %3 in %1 seconds.\r\n
0xb0011f45 | Completed manual processing of policy for user %3 in %1 seconds.\r\n
0xb0011f46 | Completed periodic policy processing for computer %3 in %1 seconds.\r\n
0xb0011f47 | Completed periodic policy processing for user %3 in %1 seconds.\r\n
0xd0000001 | No need for synchronous\r\n
0xd0000002 | First policy refresh\r\n
0xd0000003 | CSE requires foreground\r\n
0xd0000004 | CSE returned error\r\n
0xd0000005 | Forced synchronous refresh\r\n
0xd0000006 | Synchronous policy\r\n
0xd0000007 | SKU\r\n
0xd0000008 | Scripts synchronous\r\n
0xd0000009 | Synchronous due to internal processing error\r\n
0xd000000a | Background\r\n
0xd000000b | Foreground synchronous\r\n
0xd000000c | Foreground asynchronous\r\n
0xd000000d | "No loopback mode"\r\n
0xd000000e | "Merge"\r\n
0xd000000f | "Replace"\r\n
0xd0000010 | Startup script\r\n
0xd0000011 | Logon script\r\n
0xd0000012 | Logoff script\r\n
0xd0000013 | Shutdown script\r\n
0xd0000014 | User\r\n
0xd0000015 | Computer\r\n
0xd0000016 | CreateSession\r\n
0xd0000017 | Logon\r\n
0xd0000018 | Logoff\r\n
0xd0000019 | StartShell\r\n
0xd000001a | EndShell\r\n
0xd000001b | Preshutdown\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x000003ea | The processing of Group Policy failed because of a system allocation failure. Please ensure the computer is not running low on resources (memory, available disk space). Group Policy processing will be attempted at the next refresh cycle.\r\n
0x000003ee | The processing of Group Policy failed. Windows could not authenticate to the Active Directory service on a domain controller. (LDAP Bind function call failed). Look in the details tab for error code and description.\r\n
0x000003ef | The processing of Group Policy failed. Windows could not determine the site associated for this computer, which is required for Group Policy processing.\r\n
0x00000406 | The processing of Group Policy failed. Windows attempted to retrieve new Group Policy settings for this user or computer. Look in the details tab for error code and description. Windows will automatically retry this operation at the next refresh cycle. Computers joined to the domain must have proper name resolution and network connectivity to a domain controller for discovery of new Group Policy objects and settings. An event will be logged when Group Policy is successful.\r\n
0x0000041c | The processing of Group Policy failed. Windows could not determine the role of this computer. Role information (Workgroup, Member Server, or Domain Controller) is required to process Group Policy.\r\n
0x0000041d | The processing of Group Policy failed. Windows could not resolve the user name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x0000041e | The processing of Group Policy failed. Windows could not obtain the name of a domain controller. This could be caused by a name resolution failure. Verify your Domain Name System (DNS) is configured and working correctly.\r\n
0x0000041f | The processing of Group Policy failed. Windows could not resolve the computer name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x00000422 | The processing of Group Policy failed. Windows attempted to read the file %9 from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: %na) Name Resolution/Network Connectivity to the current domain controller. %nb) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller). %nc) The Distributed File System (DFS) client has been disabled.\r\n
0x00000429 | The processing of Group Policy failed. Windows could not evaluate the Windows Management Instrumentation (WMI) filter for the Group Policy object %8. This could be caused by RSOP being disabled  or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Make sure the WMI service is started and the startup type is set to automatic. New Group Policy objects or settings will not process until this event has been resolved.\r\n
0x0000042c | The processing of Group Policy was interrupted. Windows prematurely ended the discovery and enforcement of Group Policy settings because the computer was requested to shutdown or the user logged off. Group Policy processing will be attempted next refresh cycle, on the next computer reboot, or the next user logon.\r\n
0x00000437 | The processing of Group Policy failed. Windows could not obtain the list of Group Policy objects applicable for this computer or user. View the event details for more information.\r\n
0x00000438 | The processing of Group Policy failed. Windows could not search the Active Directory organization unit hierarchy. View the event details for more information.\r\n
0x0000043d | Windows failed to apply the %8 settings. %8 settings might have its own log file. Please click on the "More information" link.\r\n
0x00000440 | The processing of Group Policy failed. Windows attempted to query the list of Group Policy objects and exceeded the maximum limit (999).\r\n
0x00000441 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by RSOP being disabled or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000442 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000443 | Windows could not record  the Resultant Set of Policy (RSoP) information for the Group Policy extension <%8>. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000447 | Windows encountered an error while recording Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000448 | The processing of Group Policy failed. Windows could not apply the registry-based policy settings for the Group Policy object %8. Group Policy settings will not be resolved until this event is resolved. View the event details for more information on the file name and path that caused the failure.\r\n
0x00000449 | The processing of Group Policy failed. Windows could not determine the computer account to enforce Group Policy settings. This may be transient. Group Policy settings, including computer configuration, will not be enforced for this computer.\r\n
0x0000044d | The processing of Group Policy failed. Windows could not locate the directory object %8. Group Policy settings will not be enforced until this event is resolved. View the event details for more information on this error.\r\n
0x00000450 | Windows was unable to read the Windows Management Instrumentation (WMI) filter information associated with the Group Policy object %8.This may be caused by a deleted WMI Filter defined in the domain that is still in use by Group Policy objects. Group Policy settings for this Group Policy object will not be enforced. Other Group Policy objects may still apply. Windows will attempt to retrieve this information at the next policy cycle. This specific problem may be resolved by identifying all GPOs that reference the WMI filter and removing the references. Contact an administrator if this event recurs for several hours.\r\n
0x00000455 | The user account is in a different forest than the computer account. The processing of Group Policy from another forest is not allowed. Group Policy will be processed using Loopback Replace mode. The scope of the user policy settings will be determined by the location of the computer object in Active Directory. The settings will be acquired from the User Configuration of these policies.\r\n
0x00000456 | The processing of Group Policy failed. Windows could not determine if the user and computer accounts are in the same forest. Ensure the user domain name matches the name of a trusted domain that resides in the same forest as the computer account.\r\n
0x00000458 | The Group Policy Client Side Extension %8 was unable to apply one or more settings because the changes must be processed before system startup or user logon. The system will wait for Group Policy processing to finish completely before the next startup or logon for this user, and this may result in slow startup and boot performance.\r\n
0x00000465 | The processing of Group Policy failed because of an internal system error. Please see the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000466 | Windows was unable to determine whether new Group Policy settings defined by a network administrator should be enforced for this user or computer because this computer's clock is not synchronized with the clock of one of the domain controllers for the domain. Because of this issue, this computer system may not be in compliance with the network administrator’s requirements, and users of this system may not be able to use some functionality on the network. Windows will periodically attempt to retry this operation, and it is possible that either this system or the domain controller will correct the time settings without intervention by an administrator, so the problem will be corrected. %n%nIf this issue persists for more than an hour, checking the local system's clock settings to ensure they are accurate and are synchronized with the clocks on the network's domain controllers is one way to resolve this problem. A network administrator may be required to resolve the issue if correcting the local time settings does not address the problem.\r\n
0x00000467 | The processing of Group Policy failed due to an internal error. Please look into the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000468 | The Group Policy Client Side Extension %3 may have caused the Group Policy Service to terminate unexpectedly. To prevent further failures in the Group Policy Service, this extension has been temporarily disabled until after the next system restart. Group Policy settings managed by this extension may no longer be enforced until the system is restarted. The vendor of this extension should be contacted if this issue recurs.\r\n
0x00000469 | The processing of Group Policy failed because of lack of network connectivity to a domain controller. This may be a transient condition. A success message would be generated once the machine gets connected to the domain controller and Group Policy has successfully processed. If you do not see a success message for several hours, then contact your administrator.\r\n
0x0000046a | %5 failed. %n%tGPO Name : %6%n%tGPO File System Path : %7%n%tScript Name: %8\r\n
0x000005dc | The Group Policy settings for the computer were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005dd | The Group Policy settings for the user were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005de | The Group Policy settings for the computer were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x000005df | The Group Policy settings for the user were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x00001000 | Retrieving Domain Controller details.\r\n
0x00001001 | Forcing re-discovery of Domain Controller details.\r\n
0x00001002 | Network state change detected.\r\n
0x00001003 | seconds\r\n
0x00001004 | minutes\r\n
0x00001005 | No changes were detected.\r\n
0x00001006 | Changes were detected.\r\n
0x00001007 | Group Policy wait for network subsystem failed at computer boot. Group Policy processing will continue.\r\n
0x00001008 | Group Policy cannot be applied because the computer has been booted in Directory Services Restore Mode.\r\n
0x00001009 | Access check based on security descriptor failed.\r\n
0x0000100a | Startup scripts are not visible. Startup scripts are visible only when startup scripts are configured to run synchronously.\r\n
0x0000100b | Failed to get the active console session.\r\n
0x0000100c | Group Policy refresh access check failed.\r\n
0x0000100d | Group Policy notify access check failed.\r\n
0x0000100e | Group Policy notify access check for console session failed.\r\n
0x0000100f | Policy to deny users from refreshing computer policy is set.\r\n
0x00001010 | slow\r\n
0x00001011 | fast\r\n
0x00001012 | Attempting to retrieve the account information.\r\n
0x00001013 | Retrieved account information.\r\n
0x00001014 | Retrying to retrieve account information.\r\n
0x00001015 | Making system call to get account information.\r\n
0x00001016 | The system call to get account information completed.\r\n
0x00001017 | Making LDAP calls to connect and bind to Active Directory.\r\n
0x00001018 | The LDAP call to connect and bind to Active Directory completed.\r\n
0x00001019 | Bandwidth estimation failure: Failed to refresh network data associated with query.\r\n
0x0000101a | Bandwidth estimation failure: Failed to enumerate network signatures associated with query.\r\n
0x0000101b | Bandwidth estimation failure: Failed to query Intranet capability.\r\n
0x0000101c | Bandwidth estimation failure: Failed to inspect result of NLA query.\r\n
0x0000101d | Failed to register for connectivity notification.\r\n
0x0000101e | Failed to query information about security package.\r\n
0x0000101f | Failed to acquire handle to preexisting credentials of security principal.\r\n
0x00001020 | Failed to initiate security context.\r\n
0x00001021 | Failed to establish security context.\r\n
0x00001022 | Failed to obtain access token for security context.\r\n
0x00001023 | Making system calls to access specified file.\r\n
0x00001024 | The system calls to access specified file completed.\r\n
0x00001025 | Failed to determine the Group Policy properties of the installed system. Only a subset of Group Policy functionality will be available.\r\n
0x00001026 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon.\r\n
0x00001027 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon for a maximum of 120 seconds.\r\n
0x00001040 | Initializing and reading current service configuration for the Group Policy Client service.\r\n
0x00001041 | Checking for Group Policy client extensions that are not part of the system.\r\n
0x00001042 | Service configuration must be updated to standalone due to the presence of a Group Policy client extension that is not part of the operating system.\r\n
0x00001043 | Service configuration update to standalone is not required and will be skipped.\r\n
0x00001044 | Attempting to update service configuration to standalone.\r\n
0x00001045 | Finished checking for non-system extensions.\r\n
0x00001046 | Initializing service instance state to detect previous instances of the service.\r\n
0x00001047 | A previous instance of the Group Policy Client Service has been detected.\r\n
0x00001048 | The Group Policy Client service is currently configured as a shared service.\r\n
0x00001049 | The Group Policy Client service is currently configured as a standalone service.\r\n
0x00001050 | Computer determined to be not in a site.\r\n
0x00001051 | Group Policy wait for Direct Access CorpNet connectivity failed at computer boot. Group Policy processing will continue.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-GroupPolicy\r\n
0x90000002 | System\r\n
0x90000003 | Microsoft-Windows-GroupPolicy/Operational\r\n
0xb0000fb0 | Starting %2 Extension Processing. %n%nList of applicable Group Policy objects: (%5)%n%n%6\r\n
0xb0000fb1 | %1 %n%2\r\n
0xb0000fb2 | Starting %2 for %1.\r\n
0xb0000fb3 | Running script name %1.\r\n
0xb00010e6 | Group Policy is trying to discover the Domain Controller information.\r\n
0xb0001398 | Completed %3 Extension Processing in %1 milliseconds.\r\n
0xb0001399 | %3 %n%4%nThe call completed in %1 milliseconds.\r\n
0xb000139a | Completed %4 for %3 in %1 seconds.\r\n
0xb000139b | Completed %3 in %1 seconds.\r\n
0xb00014bc | Domain Controller details: %n%tDomain Controller Name : %1%n%tDomain Controller IP Address : %2\r\n
0xb00014bd | Computer details: %n%tComputer role : %1%n%tNetwork name : %2\r\n
0xb00014be | Account details: %n%tAccount Name : %1%n%tAccount Domain Name : %2%n%tDC Name : %3%n%tDC Domain Name : %4\r\n
0xb00014bf | The loopback policy processing mode is %1.\r\n
0xb00014c0 | List of applicable Group Policy objects: %n%n%1\r\n
0xb00014c1 | The following Group Policy objects were not applicable because they were filtered out : %n%n%1\r\n
0xb00014c2 | A %6 link was detected. The Estimated bandwidth is %1 kbps. The slow link threshold is %3 kbps.\r\n
0xb00014c3 | Next policy processing for %1 will be attempted in %2 %3.\r\n
0xb00014c8 | %1\r\n
0xb00014c9 | %1 Parameter: %2\r\n
0xb00014ca | Group Policy waited for %3 milliseconds for the network subsystem at computer boot.\r\n
0xb00014cc | Group Policy received the notification %1 from Winlogon for session %2.\r\n
0xb00014cd | Group Policy received %1 notification from Service Control Manager.\r\n
0xb00014ce | Group Policy successfully discovered the Domain Controller in %1 milliseconds.\r\n
0xb00014cf | Estimated network bandwidth on one of the connections: %1 kbps.\r\n
0xb00014d3 | Service configuration update to standalone was attempted due to the presence of Group Policy client extension %1 that is not part of the operating system and completed with status %3.\r\n
0xb00014d4 | Group Policy waited for %3 milliseconds for the Direct Access CorpNet connectivity at computer boot.\r\n
0xb00014dc | The Group Policy processing mode is %1.\r\n
0xb0001770 | Invalid Error Message.\r\n
0xb0001791 | Skipped %1 Extension based on Group Policy client-side processing rules.  Refer to a Resultant Set of Policy report for more information.\r\n
0xb0001792 | Group Policy changed from synchronous foreground to asynchronous foreground based on slow link detection.\r\n
0xb0001793 | %1 Extension deferred processing until next synchronous foreground.  Refer to a Resultant Set of Policy report for more information.\r\n
0xb00018aa | Group Policy bandwidth estimation failed. Group Policy processing will continue. Assuming %6 link.\r\n
0xb00018b0 | Warning: %1 Warning code %2.\r\n
0xb00018b1 | Warning: %1 Parameter: %3 : Warning code %2.\r\n
0xb00018b3 | Group Policy dependency (%1) did not start. As a result, network related features of Group Policy such as bandwidth estimation and response to network changes will not work.\r\n
0xb00018ba | An unfinished invocation of the Group Policy Client Side Extension %1 from a previous instance of the Group Policy Service has been detected.  This may indicate that the extension caused the Group Policy Client Service to terminate unexpectedly.\r\n
0xb00018c1 | Group Policy network connection is via Direct Access.\r\n
0xb00018c2 | Group Policy Winlogon status reporting has completed.\r\n
0xb00018c3 | Group Policy Winlogon Start Shell handling completed.\r\n
0xb00018c5 | A Group Policy setting was used to override the fast/slow link detection.\r\n
0xb00018c6 | The network connection is using a WWAN device for connectivity.\r\n
0xb0001b69 | %3 %n%4%nThe call failed after %1 milliseconds.\r\n
0xb0001b6a | Script for %3 failed in %1 seconds.\r\n
0xb0001c98 | Error: %1 Error code %2.\r\n
0xb0001c99 | Error: %1 Parameter: %3 : Error code %2.\r\n
0xb0001c9e | Group Policy failed to discover the Domain Controller details in %1 milliseconds.\r\n
0xb0010fa0 | Starting computer boot policy processing for %2. %nActivity id: %1\r\n
0xb0010fa1 | Starting user logon Policy processing for %2. %nActivity id: %1\r\n
0xb0010fa2 | Starting policy processing due to network state change for computer %2. %nActivity id: %1\r\n
0xb0010fa3 | Starting policy processing due to network state change for user %2. %nActivity id: %1\r\n
0xb0010fa4 | Starting manual processing of policy for computer %2. %nActivity id: %1\r\n
0xb0010fa5 | Starting manual processing of policy for user %2. %nActivity id: %1\r\n
0xb0010fa6 | Starting periodic policy processing for computer %2. %nActivity id: %1\r\n
0xb0010fa7 | Starting periodic policy processing for user %2. %nActivity id: %1\r\n
0xb0011b58 | Computer boot policy processing failed for %3 in %1 seconds.\r\n
0xb0011b59 | User logon policy processing failed for %3 in %1 seconds.\r\n
0xb0011b5a | Policy processing due to network state change failed for computer %3 in %1 seconds.\r\n
0xb0011b5b | Policy processing due to network state change failed for user %3 in %1 seconds.\r\n
0xb0011b5c | Manual processing of policy failed for computer %3 in %1 seconds.\r\n
0xb0011b5d | Manual processing of policy failed for user %3 in %1 seconds.\r\n
0xb0011b5e | Periodic policy processing failed for computer %3 in %1 seconds.\r\n
0xb0011b5f | Periodic policy processing failed for user %3 in %1 seconds.\r\n
0xb0011f40 | Completed computer boot policy processing for %3 in %1 seconds.\r\n
0xb0011f41 | Completed user logon policy processing for %3 in %1 seconds.\r\n
0xb0011f42 | Completed policy processing due to network state change for computer %3 in %1 seconds.\r\n
0xb0011f43 | Completed policy processing due to network state change for user %3 in %1 seconds.\r\n
0xb0011f44 | Completed manual processing of policy for computer %3 in %1 seconds.\r\n
0xb0011f45 | Completed manual processing of policy for user %3 in %1 seconds.\r\n
0xb0011f46 | Completed periodic policy processing for computer %3 in %1 seconds.\r\n
0xb0011f47 | Completed periodic policy processing for user %3 in %1 seconds.\r\n
0xd0000001 | No need for synchronous\r\n
0xd0000002 | First policy refresh\r\n
0xd0000003 | CSE requires foreground\r\n
0xd0000004 | CSE returned error\r\n
0xd0000005 | Forced synchronous refresh\r\n
0xd0000006 | Synchronous policy\r\n
0xd0000007 | SKU\r\n
0xd0000008 | Scripts synchronous\r\n
0xd0000009 | Synchronous due to internal processing error\r\n
0xd000000a | Background\r\n
0xd000000b | Foreground synchronous\r\n
0xd000000c | Foreground asynchronous\r\n
0xd000000d | "No loopback mode"\r\n
0xd000000e | "Merge"\r\n
0xd000000f | "Replace"\r\n
0xd0000010 | Startup script\r\n
0xd0000011 | Logon script\r\n
0xd0000012 | Logoff script\r\n
0xd0000013 | Shutdown script\r\n
0xd0000014 | User\r\n
0xd0000015 | Computer\r\n
0xd0000016 | CreateSession\r\n
0xd0000017 | Logon\r\n
0xd0000018 | Logoff\r\n
0xd0000019 | StartShell\r\n
0xd000001a | EndShell\r\n
0xd000001b | Preshutdown\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x000003ea | The processing of Group Policy failed because of a system allocation failure. Please ensure the computer is not running low on resources (memory, available disk space). Group Policy processing will be attempted at the next refresh cycle.\r\n
0x000003ee | The processing of Group Policy failed. Windows could not authenticate to the Active Directory service on a domain controller. (LDAP Bind function call failed). Look in the details tab for error code and description.\r\n
0x000003ef | The processing of Group Policy failed. Windows could not determine the site associated for this computer, which is required for Group Policy processing.\r\n
0x00000406 | The processing of Group Policy failed. Windows attempted to retrieve new Group Policy settings for this user or computer. Look in the details tab for error code and description. Windows will automatically retry this operation at the next refresh cycle. Computers joined to the domain must have proper name resolution and network connectivity to a domain controller for discovery of new Group Policy objects and settings. An event will be logged when Group Policy is successful.\r\n
0x0000041c | The processing of Group Policy failed. Windows could not determine the role of this computer. Role information (Workgroup, Member Server, or Domain Controller) is required to process Group Policy.\r\n
0x0000041d | The processing of Group Policy failed. Windows could not resolve the user name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x0000041e | The processing of Group Policy failed. Windows could not obtain the name of a domain controller. This could be caused by a name resolution failure. Verify your Domain Name System (DNS) is configured and working correctly.\r\n
0x0000041f | The processing of Group Policy failed. Windows could not resolve the computer name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x00000422 | The processing of Group Policy failed. Windows attempted to read the file %9 from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: %na) Name Resolution/Network Connectivity to the current domain controller. %nb) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller). %nc) The Distributed File System (DFS) client has been disabled.\r\n
0x00000429 | The processing of Group Policy failed. Windows could not evaluate the Windows Management Instrumentation (WMI) filter for the Group Policy object %8. This could be caused by RSOP being disabled  or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Make sure the WMI service is started and the startup type is set to automatic. New Group Policy objects or settings will not process until this event has been resolved.\r\n
0x0000042c | The processing of Group Policy was interrupted. Windows prematurely ended the discovery and enforcement of Group Policy settings because the computer was requested to shutdown or the user logged off. Group Policy processing will be attempted next refresh cycle, on the next computer reboot, or the next user logon.\r\n
0x00000437 | The processing of Group Policy failed. Windows could not obtain the list of Group Policy objects applicable for this computer or user. View the event details for more information.\r\n
0x00000438 | The processing of Group Policy failed. Windows could not search the Active Directory organization unit hierarchy. View the event details for more information.\r\n
0x0000043d | Windows failed to apply the %8 settings. %8 settings might have its own log file. Please click on the "More information" link.\r\n
0x00000440 | The processing of Group Policy failed. Windows attempted to query the list of Group Policy objects and exceeded the maximum limit (999).\r\n
0x00000441 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by RSOP being disabled or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000442 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000443 | Windows could not record  the Resultant Set of Policy (RSoP) information for the Group Policy extension <%8>. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000447 | Windows encountered an error while recording Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000448 | The processing of Group Policy failed. Windows could not apply the registry-based policy settings for the Group Policy object %8. Group Policy settings will not be resolved until this event is resolved. View the event details for more information on the file name and path that caused the failure.\r\n
0x00000449 | The processing of Group Policy failed. Windows could not determine the computer account to enforce Group Policy settings. This may be transient. Group Policy settings, including computer configuration, will not be enforced for this computer.\r\n
0x0000044d | The processing of Group Policy failed. Windows could not locate the directory object %8. Group Policy settings will not be enforced until this event is resolved. View the event details for more information on this error.\r\n
0x00000450 | Windows was unable to read the Windows Management Instrumentation (WMI) filter information associated with the Group Policy object %8.This may be caused by a deleted WMI Filter defined in the domain that is still in use by Group Policy objects. Group Policy settings for this Group Policy object will not be enforced. Other Group Policy objects may still apply. Windows will attempt to retrieve this information at the next policy cycle. This specific problem may be resolved by identifying all GPOs that reference the WMI filter and removing the references. Contact an administrator if this event recurs for several hours.\r\n
0x00000455 | The user account is in a different forest than the computer account. The processing of Group Policy from another forest is not allowed. Group Policy will be processed using Loopback Replace mode. The scope of the user policy settings will be determined by the location of the computer object in Active Directory. The settings will be acquired from the User Configuration of these policies.\r\n
0x00000456 | The processing of Group Policy failed. Windows could not determine if the user and computer accounts are in the same forest. Ensure the user domain name matches the name of a trusted domain that resides in the same forest as the computer account.\r\n
0x00000458 | The Group Policy Client Side Extension %8 was unable to apply one or more settings because the changes must be processed before system startup or user logon. The system will wait for Group Policy processing to finish completely before the next startup or logon for this user, and this may result in slow startup and boot performance.\r\n
0x00000465 | The processing of Group Policy failed because of an internal system error. Please see the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000466 | Windows was unable to determine whether new Group Policy settings defined by a network administrator should be enforced for this user or computer because this computer's clock is not synchronized with the clock of one of the domain controllers for the domain. Because of this issue, this computer system may not be in compliance with the network administrator’s requirements, and users of this system may not be able to use some functionality on the network. Windows will periodically attempt to retry this operation, and it is possible that either this system or the domain controller will correct the time settings without intervention by an administrator, so the problem will be corrected. %n%nIf this issue persists for more than an hour, checking the local system's clock settings to ensure they are accurate and are synchronized with the clocks on the network's domain controllers is one way to resolve this problem. A network administrator may be required to resolve the issue if correcting the local time settings does not address the problem.\r\n
0x00000467 | The processing of Group Policy failed due to an internal error. Please look into the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000468 | The Group Policy Client Side Extension %3 may have caused the Group Policy Service to terminate unexpectedly. To prevent further failures in the Group Policy Service, this extension has been temporarily disabled until after the next system restart. Group Policy settings managed by this extension may no longer be enforced until the system is restarted. The vendor of this extension should be contacted if this issue recurs.\r\n
0x00000469 | The processing of Group Policy failed because of lack of network connectivity to a domain controller. This may be a transient condition. A success message would be generated once the machine gets connected to the domain controller and Group Policy has successfully processed. If you do not see a success message for several hours, then contact your administrator.\r\n
0x0000046a | %5 failed. %n%tGPO Name : %6%n%tGPO File System Path : %7%n%tScript Name: %8\r\n
0x000005dc | The Group Policy settings for the computer were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005dd | The Group Policy settings for the user were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005de | The Group Policy settings for the computer were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x000005df | The Group Policy settings for the user were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x00001000 | Retrieving Domain Controller details.\r\n
0x00001001 | Forcing re-discovery of Domain Controller details.\r\n
0x00001002 | Network state change detected.\r\n
0x00001003 | seconds\r\n
0x00001004 | minutes\r\n
0x00001005 | No changes were detected.\r\n
0x00001006 | Changes were detected.\r\n
0x00001007 | Group Policy wait for network subsystem failed at computer boot. Group Policy processing will continue.\r\n
0x00001008 | Group Policy cannot be applied because the computer has been booted in Directory Services Restore Mode.\r\n
0x00001009 | Access check based on security descriptor failed.\r\n
0x0000100a | Startup scripts are not visible. Startup scripts are visible only when startup scripts are configured to run synchronously.\r\n
0x0000100b | Failed to get the active console session.\r\n
0x0000100c | Group Policy refresh access check failed.\r\n
0x0000100d | Group Policy notify access check failed.\r\n
0x0000100e | Group Policy notify access check for console session failed.\r\n
0x0000100f | Policy to deny users from refreshing computer policy is set.\r\n
0x00001010 | slow\r\n
0x00001011 | fast\r\n
0x00001012 | Attempting to retrieve the account information.\r\n
0x00001013 | Retrieved account information.\r\n
0x00001014 | Retrying to retrieve account information.\r\n
0x00001015 | Making system call to get account information.\r\n
0x00001016 | The system call to get account information completed.\r\n
0x00001017 | Making LDAP calls to connect and bind to Active Directory.\r\n
0x00001018 | The LDAP call to connect and bind to Active Directory completed.\r\n
0x00001019 | Bandwidth estimation failure: Failed to refresh network data associated with query.\r\n
0x0000101a | Bandwidth estimation failure: Failed to enumerate network signatures associated with query.\r\n
0x0000101b | Bandwidth estimation failure: Failed to query Intranet capability.\r\n
0x0000101c | Bandwidth estimation failure: Failed to inspect result of NLA query.\r\n
0x0000101d | Failed to register for connectivity notification.\r\n
0x0000101e | Failed to query information about security package.\r\n
0x0000101f | Failed to acquire handle to preexisting credentials of security principal.\r\n
0x00001020 | Failed to initiate security context.\r\n
0x00001021 | Failed to establish security context.\r\n
0x00001022 | Failed to obtain access token for security context.\r\n
0x00001023 | Making system calls to access specified file.\r\n
0x00001024 | The system calls to access specified file completed.\r\n
0x00001025 | Failed to determine the Group Policy properties of the installed system. Only a subset of Group Policy functionality will be available.\r\n
0x00001026 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon.\r\n
0x00001027 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon for a maximum of 120 seconds.\r\n
0x00001040 | Initializing and reading current service configuration for the Group Policy Client service.\r\n
0x00001041 | Checking for Group Policy client extensions that are not part of the system.\r\n
0x00001042 | Service configuration must be updated to standalone due to the presence of a Group Policy client extension that is not part of the operating system.\r\n
0x00001043 | Service configuration update to standalone is not required and will be skipped.\r\n
0x00001044 | Attempting to update service configuration to standalone.\r\n
0x00001045 | Finished checking for non-system extensions.\r\n
0x00001046 | Initializing service instance state to detect previous instances of the service.\r\n
0x00001047 | A previous instance of the Group Policy Client Service was detected.\r\n
0x00001048 | The Group Policy Client service is currently configured as a shared service.\r\n
0x00001049 | The Group Policy Client service is currently configured as a standalone service.\r\n
0x00001050 | Computer determined to be not in a site.\r\n
0x00001051 | Group Policy wait for Direct Access CorpNet connectivity failed at computer boot. Group Policy processing will continue.\r\n
0x00001052 | Group Policy Service aborted due to computer shutdown or user logoff.\r\n
0x00001060 | A non group policy SYSVOL file is locked. This may prevent synchronizing important Group Policy files between domain controllers.\r\n
0x00001061 | A group policy file in SYSVOL is locked. This may prevent synchronizing important Group Policy files between domain controllers. Forcefully closed it.\r\n
0x00001062 | A group policy file in SYSVOL is locked. This may prevent synchronizing important Group Policy files between domain controllers. Failed to forcefully close it.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-GroupPolicy\r\n
0x90000002 | System\r\n
0x90000003 | Microsoft-Windows-GroupPolicy/Operational\r\n
0xb0000fb0 | Starting %2 Extension Processing. %n%nList of applicable Group Policy objects: (%5)%n%n%6\r\n
0xb0000fb1 | %1 %n%2\r\n
0xb0000fb2 | Starting %2 for %1.\r\n
0xb0000fb3 | Running script name %1.\r\n
0xb0001013 | Group Policy Service started.\r\n
0xb0001014 | Started the Group Policy service initialization phase.\r\n
0xb0001015 | Group Policy Session started.\r\n
0xb000101e | Group Policy receiving applicable GPOs from the domain controller.\r\n
0xb0001078 | Starting to save policies to the local datastore.\r\n
0xb0001079 | Starting to load policies from the local datastore.\r\n
0xb000107a | Starting the first WMI query for the policy.\r\n
0xb00010a1 | Starting to download policies.\r\n
0xb00010e6 | Group Policy is trying to discover the Domain Controller information.\r\n
0xb0001398 | Completed %3 Extension Processing in %1 milliseconds.\r\n
0xb0001399 | %3 %n%4%nThe call completed in %1 milliseconds.\r\n
0xb000139a | Completed %4 for %3 in %1 seconds.\r\n
0xb000139b | Completed %3 in %1 seconds.\r\n
0xb00013fb | Group Policy Service stopped.\r\n
0xb00013fc | Successfully completed the Group Policy Service initialization phase.\r\n
0xb00013fd | Group policy session completed successfully.\r\n
0xb0001406 | Group Policy successfully got applicable GPOs from the domain controller.\r\n
0xb0001460 | Successfully saved policies to the local datastore.\r\n
0xb0001461 | Successfully loaded policies from the local datastore.\r\n
0xb0001462 | Successfully completed the first WMI query.\r\n
0xb0001489 | Successfully completed downloading policies.\r\n
0xb00014bc | Domain Controller details: %n%tDomain Controller Name : %1%n%tDomain Controller IP Address : %2\r\n
0xb00014bd | Computer details: %n%tComputer role : %1%n%tNetwork name : %2\r\n
0xb00014be | Account details: %n%tAccount Name : %1%n%tAccount Domain Name : %2%n%tDC Name : %3%n%tDC Domain Name : %4\r\n
0xb00014bf | The loopback policy processing mode is %1.\r\n
0xb00014c0 | List of applicable Group Policy objects: %n%n%1\r\n
0xb00014c1 | The following Group Policy objects were not applicable because they were filtered out : %n%n%1\r\n
0xb00014c2 | A %6 link was detected. The Estimated bandwidth is %1 kbps. The slow link threshold is %3 kbps.\r\n
0xb00014c3 | Next policy processing for %1 will be attempted in %2 %3.\r\n
0xb00014c8 | %1\r\n
0xb00014c9 | %1 Parameter: %2\r\n
0xb00014ca | Group Policy waited for %3 milliseconds for the network subsystem at computer boot.\r\n
0xb00014cc | Group Policy received the notification %1 from Winlogon for session %2.\r\n
0xb00014cd | Group Policy received %1 notification from Service Control Manager.\r\n
0xb00014ce | Group Policy successfully discovered the Domain Controller in %1 milliseconds.\r\n
0xb00014cf | Estimated network bandwidth on one of the connections: %1 kbps.\r\n
0xb00014d3 | Service configuration update to standalone was attempted due to the presence of Group Policy client extension %1 that is not part of the operating system and completed with status %3.\r\n
0xb00014d4 | Group Policy waited for %3 milliseconds for the Direct Access CorpNet connectivity at computer boot.\r\n
0xb00014dc | The Group Policy processing mode is %1.\r\n
0xb00014e7 | Group policy session returned to winlogon.\r\n
0xb0001770 | Invalid Error Message.\r\n
0xb0001791 | Skipped %1 Extension based on Group Policy client-side processing rules.  Refer to a Resultant Set of Policy report for more information.\r\n
0xb0001792 | Group Policy changed from synchronous foreground to asynchronous foreground based on slow link detection.\r\n
0xb0001793 | %1 Extension deferred processing until next synchronous foreground.  Refer to a Resultant Set of Policy report for more information.\r\n
0xb00018aa | Group Policy bandwidth estimation failed. Group Policy processing will continue. Assuming %6 link.\r\n
0xb00018b0 | Warning: %1 Warning code %2.\r\n
0xb00018b1 | Warning: %1 Parameter: %3 : Warning code %2.\r\n
0xb00018b3 | Group Policy dependency (%1) did not start. As a result, network related features of Group Policy such as bandwidth estimation and response to network changes will not work.\r\n
0xb00018ba | An unfinished invocation of the Group Policy Client Side Extension %1 from a previous instance of the Group Policy Service was detected.  This may indicate that the extension caused the Group Policy Client Service to terminate unexpectedly.\r\n
0xb00018c1 | Group Policy network connection is via Direct Access.\r\n
0xb00018c2 | Group Policy Winlogon status reporting has completed.\r\n
0xb00018c3 | Group Policy Winlogon Start Shell handling completed.\r\n
0xb00018c5 | A Group Policy setting was used to override the fast/slow link detection.\r\n
0xb00018c6 | The network connection is using a WWAN device for connectivity.\r\n
0xb00018c8 | Group Policy detected a slow link during sync mode processing.\r\n
0xb00018c9 | The connection to DC timed out during the Group Policy sync mode process.\r\n
0xb00018ca | Group Policy switched the sync mode process to async mode.\r\n
0xb0001b69 | %3 %n%4%nThe call failed after %1 milliseconds.\r\n
0xb0001b6a | Script for %3 failed in %1 seconds.\r\n
0xb0001bcd | Group policy session completed with error.\r\n
0xb0001bd6 | Group Policy could not get applicable GPOs from the domain controller.\r\n
0xb0001c30 | Saved policies to the local datastore with error.\r\n
0xb0001c31 | Loaded policies from the local datastore with error.\r\n
0xb0001c59 | Downloaded policies with error.\r\n
0xb0001c98 | Error: %1 Error code %2.\r\n
0xb0001c99 | Error: %1 Parameter: %3 : Error code %2.\r\n
0xb0001c9e | Group Policy failed to discover the Domain Controller details in %1 milliseconds.\r\n
0xb0001f50 | %1 Extension (%2) requests a sync mode process.\r\n
0xb0010fa0 | Starting computer boot policy processing for %2. %nActivity id: %1\r\n
0xb0010fa1 | Starting user logon Policy processing for %2. %nActivity id: %1\r\n
0xb0010fa2 | Starting policy processing due to network state change for computer %2. %nActivity id: %1\r\n
0xb0010fa3 | Starting policy processing due to network state change for user %2. %nActivity id: %1\r\n
0xb0010fa4 | Starting manual processing of policy for computer %2. %nActivity id: %1\r\n
0xb0010fa5 | Starting manual processing of policy for user %2. %nActivity id: %1\r\n
0xb0010fa6 | Starting periodic policy processing for computer %2. %nActivity id: %1\r\n
0xb0010fa7 | Starting periodic policy processing for user %2. %nActivity id: %1\r\n
0xb0011b58 | Computer boot policy processing failed for %3 in %1 seconds.\r\n
0xb0011b59 | User logon policy processing failed for %3 in %1 seconds.\r\n
0xb0011b5a | Policy processing due to network state change failed for computer %3 in %1 seconds.\r\n
0xb0011b5b | Policy processing due to network state change failed for user %3 in %1 seconds.\r\n
0xb0011b5c | Manual processing of policy failed for computer %3 in %1 seconds.\r\n
0xb0011b5d | Manual processing of policy failed for user %3 in %1 seconds.\r\n
0xb0011b5e | Periodic policy processing failed for computer %3 in %1 seconds.\r\n
0xb0011b5f | Periodic policy processing failed for user %3 in %1 seconds.\r\n
0xb0011f40 | Completed computer boot policy processing for %3 in %1 seconds.\r\n
0xb0011f41 | Completed user logon policy processing for %3 in %1 seconds.\r\n
0xb0011f42 | Completed policy processing due to network state change for computer %3 in %1 seconds.\r\n
0xb0011f43 | Completed policy processing due to network state change for user %3 in %1 seconds.\r\n
0xb0011f44 | Completed manual processing of policy for computer %3 in %1 seconds.\r\n
0xb0011f45 | Completed manual processing of policy for user %3 in %1 seconds.\r\n
0xb0011f46 | Completed periodic policy processing for computer %3 in %1 seconds.\r\n
0xb0011f47 | Completed periodic policy processing for user %3 in %1 seconds.\r\n
0xd0000001 | No need for synchronous\r\n
0xd0000002 | First policy refresh\r\n
0xd0000003 | CSE requires foreground\r\n
0xd0000004 | CSE returned error\r\n
0xd0000005 | Forced synchronous refresh\r\n
0xd0000006 | Synchronous policy\r\n
0xd0000007 | SKU\r\n
0xd0000008 | Scripts synchronous\r\n
0xd0000009 | Synchronous due to internal processing error\r\n
0xd000000a | Background\r\n
0xd000000b | Foreground synchronous\r\n
0xd000000c | Foreground asynchronous\r\n
0xd000000d | "No loopback mode"\r\n
0xd000000e | "Merge"\r\n
0xd000000f | "Replace"\r\n
0xd0000010 | Startup script\r\n
0xd0000011 | Logon script\r\n
0xd0000012 | Logoff script\r\n
0xd0000013 | Shutdown script\r\n
0xd0000014 | User\r\n
0xd0000015 | Computer\r\n
0xd0000016 | CreateSession\r\n
0xd0000017 | Logon\r\n
0xd0000018 | Logoff\r\n
0xd0000019 | StartShell\r\n
0xd000001a | EndShell\r\n
0xd000001b | Preshutdown\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x000003ea | The processing of Group Policy failed because of a system allocation failure. Please ensure the computer is not running low on resources (memory, available disk space). Group Policy processing will be attempted at the next refresh cycle.\r\n
0x000003ee | The processing of Group Policy failed. Windows could not authenticate to the Active Directory service on a domain controller. (LDAP Bind function call failed). Look in the details tab for error code and description.\r\n
0x000003ef | The processing of Group Policy failed. Windows could not determine the site associated for this computer, which is required for Group Policy processing.\r\n
0x00000406 | The processing of Group Policy failed. Windows attempted to retrieve new Group Policy settings for this user or computer. Look in the details tab for error code and description. Windows will automatically retry this operation at the next refresh cycle. Computers joined to the domain must have proper name resolution and network connectivity to a domain controller for discovery of new Group Policy objects and settings. An event will be logged when Group Policy is successful.\r\n
0x0000041c | The processing of Group Policy failed. Windows could not determine the role of this computer. Role information (Workgroup, Member Server, or Domain Controller) is required to process Group Policy.\r\n
0x0000041d | The processing of Group Policy failed. Windows could not resolve the user name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x0000041e | The processing of Group Policy failed. Windows could not obtain the name of a domain controller. This could be caused by a name resolution failure. Verify your Domain Name System (DNS) is configured and working correctly.\r\n
0x0000041f | The processing of Group Policy failed. Windows could not resolve the computer name. This could be caused by one of more of the following: %na) Name Resolution failure on the current domain controller. %nb) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).\r\n
0x00000422 | The processing of Group Policy failed. Windows attempted to read the file %9 from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: %na) Name Resolution/Network Connectivity to the current domain controller. %nb) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller). %nc) The Distributed File System (DFS) client has been disabled.\r\n
0x00000429 | The processing of Group Policy failed. Windows could not evaluate the Windows Management Instrumentation (WMI) filter for the Group Policy object %8. This could be caused by RSOP being disabled  or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Make sure the WMI service is started and the startup type is set to automatic. New Group Policy objects or settings will not process until this event has been resolved.\r\n
0x0000042c | The processing of Group Policy was interrupted. Windows prematurely ended the discovery and enforcement of Group Policy settings because the computer was requested to shutdown or the user logged off. Group Policy processing will be attempted next refresh cycle, on the next computer reboot, or the next user logon.\r\n
0x00000437 | The processing of Group Policy failed. Windows could not obtain the list of Group Policy objects applicable for this computer or user. View the event details for more information.\r\n
0x00000438 | The processing of Group Policy failed. Windows could not search the Active Directory organization unit hierarchy. View the event details for more information.\r\n
0x0000043d | Windows failed to apply the %8 settings. %8 settings might have its own log file. Please click on the "More information" link.\r\n
0x00000440 | The processing of Group Policy failed. Windows attempted to query the list of Group Policy objects and exceeded the maximum limit (999).\r\n
0x00000441 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by RSOP being disabled or Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000442 | Windows failed to record Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. This could be caused by Windows Management Instrumentation (WMI) service being disabled, stopped, or other WMI errors. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000443 | Windows could not record  the Resultant Set of Policy (RSoP) information for the Group Policy extension <%8>. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000447 | Windows encountered an error while recording Resultant Set of Policy (RSoP) information, which describes the scope of Group Policy objects applied to the computer or user. Group Policy settings successfully applied to the computer or user; however, management tools may not report accurately.\r\n
0x00000448 | The processing of Group Policy failed. Windows could not apply the registry-based policy settings for the Group Policy object %8. Group Policy settings will not be resolved until this event is resolved. View the event details for more information on the file name and path that caused the failure.\r\n
0x00000449 | The processing of Group Policy failed. Windows could not determine the computer account to enforce Group Policy settings. This may be transient. Group Policy settings, including computer configuration, will not be enforced for this computer.\r\n
0x0000044d | The processing of Group Policy failed. Windows could not locate the directory object %8. Group Policy settings will not be enforced until this event is resolved. View the event details for more information on this error.\r\n
0x00000450 | Windows was unable to read the Windows Management Instrumentation (WMI) filter information associated with the Group Policy object %8.This may be caused by a deleted WMI Filter defined in the domain that is still in use by Group Policy objects. Group Policy settings for this Group Policy object will not be enforced. Other Group Policy objects may still apply. Windows will attempt to retrieve this information at the next policy cycle. This specific problem may be resolved by identifying all GPOs that reference the WMI filter and removing the references. Contact an administrator if this event recurs for several hours.\r\n
0x00000455 | The user account is in a different forest than the computer account. The processing of Group Policy from another forest is not allowed. Group Policy will be processed using Loopback Replace mode. The scope of the user policy settings will be determined by the location of the computer object in Active Directory. The settings will be acquired from the User Configuration of these policies.\r\n
0x00000456 | The processing of Group Policy failed. Windows could not determine if the user and computer accounts are in the same forest. Ensure the user domain name matches the name of a trusted domain that resides in the same forest as the computer account.\r\n
0x00000458 | The Group Policy Client Side Extension %8 was unable to apply one or more settings because the changes must be processed before system startup or user logon. The system will wait for Group Policy processing to finish completely before the next startup or logon for this user, and this may result in slow startup and boot performance.\r\n
0x00000465 | The processing of Group Policy failed because of an internal system error. Please see the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000466 | Windows was unable to determine whether new Group Policy settings defined by a network administrator should be enforced for this user or computer because this computer's clock is not synchronized with the clock of one of the domain controllers for the domain. Because of this issue, this computer system may not be in compliance with the network administrator’s requirements, and users of this system may not be able to use some functionality on the network. Windows will periodically attempt to retry this operation, and it is possible that either this system or the domain controller will correct the time settings without intervention by an administrator, so the problem will be corrected. %n%nIf this issue persists for more than an hour, checking the local system's clock settings to ensure they are accurate and are synchronized with the clocks on the network's domain controllers is one way to resolve this problem. A network administrator may be required to resolve the issue if correcting the local time settings does not address the problem.\r\n
0x00000467 | The processing of Group Policy failed due to an internal error. Please look into the Group Policy operational log for the specific error message. An attempt will be made to process Group Policy again at the next refresh cycle.\r\n
0x00000468 | The Group Policy Client Side Extension %3 may have caused the Group Policy Service to terminate unexpectedly. To prevent further failures in the Group Policy Service, this extension has been temporarily disabled until after the next system restart. Group Policy settings managed by this extension may no longer be enforced until the system is restarted. The vendor of this extension should be contacted if this issue recurs.\r\n
0x00000469 | The processing of Group Policy failed because of lack of network connectivity to a domain controller. This may be a transient condition. A success message would be generated once the machine gets connected to the domain controller and Group Policy has successfully processed. If you do not see a success message for several hours, then contact your administrator.\r\n
0x0000046a | %5 failed. %n%tGPO Name : %6%n%tGPO File System Path : %7%n%tScript Name: %8\r\n
0x000005dc | The Group Policy settings for the computer were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005dd | The Group Policy settings for the user were processed successfully. There were no changes detected since the last successful processing of Group Policy.\r\n
0x000005de | The Group Policy settings for the computer were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x000005df | The Group Policy settings for the user were processed successfully. New settings from %6 Group Policy objects were detected and applied.\r\n
0x00001000 | Retrieving Domain Controller details.\r\n
0x00001001 | Forcing re-discovery of Domain Controller details.\r\n
0x00001002 | Network state change detected.\r\n
0x00001003 | seconds\r\n
0x00001004 | minutes\r\n
0x00001005 | No changes were detected.\r\n
0x00001006 | Changes were detected.\r\n
0x00001007 | Group Policy wait for network subsystem failed at computer boot. Group Policy processing will continue.\r\n
0x00001008 | Group Policy cannot be applied because the computer has been booted in Directory Services Restore Mode.\r\n
0x00001009 | Access check based on security descriptor failed.\r\n
0x0000100a | Startup scripts are not visible. Startup scripts are visible only when startup scripts are configured to run synchronously.\r\n
0x0000100b | Failed to get the active console session.\r\n
0x0000100c | Group Policy refresh access check failed.\r\n
0x0000100d | Group Policy notify access check failed.\r\n
0x0000100e | Group Policy notify access check for console session failed.\r\n
0x0000100f | Policy to deny users from refreshing computer policy is set.\r\n
0x00001010 | slow\r\n
0x00001011 | fast\r\n
0x00001012 | Attempting to retrieve the account information.\r\n
0x00001013 | Retrieved account information.\r\n
0x00001014 | Retrying to retrieve account information.\r\n
0x00001015 | Making system call to get account information.\r\n
0x00001016 | The system call to get account information completed.\r\n
0x00001017 | Making LDAP calls to connect and bind to Active Directory.\r\n
0x00001018 | The LDAP call to connect and bind to Active Directory completed.\r\n
0x00001019 | Bandwidth estimation failure: Failed to refresh network data associated with query.\r\n
0x0000101a | Bandwidth estimation failure: Failed to enumerate network signatures associated with query.\r\n
0x0000101b | Bandwidth estimation failure: Failed to query Intranet capability.\r\n
0x0000101c | Bandwidth estimation failure: Failed to inspect result of NLA query.\r\n
0x0000101d | Failed to register for connectivity notification.\r\n
0x0000101e | Failed to query information about security package.\r\n
0x0000101f | Failed to acquire handle to preexisting credentials of security principal.\r\n
0x00001020 | Failed to initiate security context.\r\n
0x00001021 | Failed to establish security context.\r\n
0x00001022 | Failed to obtain access token for security context.\r\n
0x00001023 | Making system calls to access specified file.\r\n
0x00001024 | The system calls to access specified file completed.\r\n
0x00001025 | Failed to determine the Group Policy properties of the installed system. Only a subset of Group Policy functionality will be available.\r\n
0x00001026 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon.\r\n
0x00001027 | Failed to determine the Group Policy properties of the installed system. Group Policy will wait for the network at startup and logon for a maximum of 120 seconds.\r\n
0x00001040 | Initializing and reading current service configuration for the Group Policy Client service.\r\n
0x00001041 | Checking for Group Policy client extensions that are not part of the system.\r\n
0x00001042 | Service configuration must be updated to standalone due to the presence of a Group Policy client extension that is not part of the operating system.\r\n
0x00001043 | Service configuration update to standalone is not required and will be skipped.\r\n
0x00001044 | Attempting to update service configuration to standalone.\r\n
0x00001045 | Finished checking for non-system extensions.\r\n
0x00001046 | Initializing service instance state to detect previous instances of the service.\r\n
0x00001047 | A previous instance of the Group Policy Client Service was detected.\r\n
0x00001048 | The Group Policy Client service is currently configured as a shared service.\r\n
0x00001049 | The Group Policy Client service is currently configured as a standalone service.\r\n
0x00001050 | Computer determined to be not in a site.\r\n
0x00001051 | Group Policy wait for Direct Access CorpNet connectivity failed at computer boot. Group Policy processing will continue.\r\n
0x00001052 | Group Policy Service aborted due to computer shutdown or user logoff.\r\n
0x00001060 | A non group policy SYSVOL file is locked. This may prevent synchronizing important Group Policy files between domain controllers.\r\n
0x00001061 | A group policy file in SYSVOL is locked. This may prevent synchronizing important Group Policy files between domain controllers. Forcefully closed it.\r\n
0x00001062 | A group policy file in SYSVOL is locked. This may prevent synchronizing important Group Policy files between domain controllers. Failed to forcefully close it.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-GroupPolicy\r\n
0x90000002 | System\r\n
0x90000003 | Microsoft-Windows-GroupPolicy/Operational\r\n
0xb0000fb0 | Starting %2 Extension Processing. %n%nList of applicable Group Policy objects: (%5)%n%n%6\r\n
0xb0000fb1 | %1 %n%2\r\n
0xb0000fb2 | Starting %2 for %1.\r\n
0xb0000fb3 | Running script name %1.\r\n
0xb0001013 | Group Policy Service started.\r\n
0xb0001014 | Started the Group Policy service initialization phase.\r\n
0xb0001015 | Group Policy Session started.\r\n
0xb000101e | Group Policy receiving applicable GPOs from the domain controller.\r\n
0xb0001078 | Starting to save policies to the local datastore.\r\n
0xb0001079 | Starting to load policies from the local datastore.\r\n
0xb000107a | Starting the first WMI query for the policy.\r\n
0xb00010a1 | Starting to download policies.\r\n
0xb00010e6 | Group Policy is trying to discover the Domain Controller information.\r\n
0xb0001398 | Completed %3 Extension Processing in %1 milliseconds.\r\n
0xb0001399 | %3 %n%4%nThe call completed in %1 milliseconds.\r\n
0xb000139a | Completed %4 for %3 in %1 seconds.\r\n
0xb000139b | Completed %3 in %1 seconds.\r\n
0xb00013fb | Group Policy Service stopped.\r\n
0xb00013fc | Successfully completed the Group Policy Service initialization phase.\r\n
0xb00013fd | Group policy session completed successfully.\r\n
0xb0001406 | Group Policy successfully got applicable GPOs from the domain controller.\r\n
0xb0001460 | Successfully saved policies to the local datastore.\r\n
0xb0001461 | Successfully loaded policies from the local datastore.\r\n
0xb0001462 | Successfully completed the first WMI query.\r\n
0xb0001489 | Successfully completed downloading policies.\r\n
0xb00014bc | Domain Controller details: %n%tDomain Controller Name : %1%n%tDomain Controller IP Address : %2\r\n
0xb00014bd | Computer details: %n%tComputer role : %1%n%tNetwork name : %2\r\n
0xb00014be | Account details: %n%tAccount Name : %1%n%tAccount Domain Name : %2%n%tDC Name : %3%n%tDC Domain Name : %4\r\n
0xb00014bf | The loopback policy processing mode is %1.\r\n
0xb00014c0 | List of applicable Group Policy objects: %n%n%1\r\n
0xb00014c1 | The following Group Policy objects were not applicable because they were filtered out : %n%n%1\r\n
0xb00014c2 | A %6 link was detected. The Estimated bandwidth is %1 kbps. The slow link threshold is %3 kbps.\r\n
0xb00014c3 | Next policy processing for %1 will be attempted in %2 %3.\r\n
0xb00014c8 | %1\r\n
0xb00014c9 | %1 Parameter: %2\r\n
0xb00014ca | Group Policy waited for %3 milliseconds for the network subsystem at computer boot.\r\n
0xb00014cc | Group Policy received the notification %1 from Winlogon for session %2.\r\n
0xb00014cd | Group Policy received %1 notification from Service Control Manager.\r\n
0xb00014ce | Group Policy successfully discovered the Domain Controller in %1 milliseconds.\r\n
0xb00014cf | Estimated network bandwidth on one of the connections: %1 kbps.\r\n
0xb00014d3 | Service configuration update to standalone was attempted due to the presence of Group Policy client extension %1 that is not part of the operating system and completed with status %3.\r\n
0xb00014d4 | Group Policy waited for %3 milliseconds for the Direct Access CorpNet connectivity at computer boot.\r\n
0xb00014dc | The Group Policy processing mode is %1.\r\n
0xb00014e7 | Group policy session returned to winlogon.\r\n
0xb0001770 | Invalid Error Message.\r\n
0xb0001791 | Skipped %1 Extension based on Group Policy client-side processing rules.  Refer to a Resultant Set of Policy report for more information.\r\n
0xb0001792 | Group Policy changed from synchronous foreground to asynchronous foreground based on slow link detection.\r\n
0xb0001793 | %1 Extension deferred processing until next synchronous foreground.  Refer to a Resultant Set of Policy report for more information.\r\n
0xb00018aa | Group Policy bandwidth estimation failed. Group Policy processing will continue. Assuming %6 link.\r\n
0xb00018b0 | Warning: %1 Warning code %2.\r\n
0xb00018b1 | Warning: %1 Parameter: %3 : Warning code %2.\r\n
0xb00018b3 | Group Policy dependency (%1) did not start. As a result, network related features of Group Policy such as bandwidth estimation and response to network changes will not work.\r\n
0xb00018ba | An unfinished invocation of the Group Policy Client Side Extension %1 from a previous instance of the Group Policy Service was detected.  This may indicate that the extension caused the Group Policy Client Service to terminate unexpectedly.\r\n
0xb00018c1 | Group Policy network connection is via Direct Access.\r\n
0xb00018c2 | Group Policy Winlogon status reporting has completed.\r\n
0xb00018c3 | Group Policy Winlogon Start Shell handling completed.\r\n
0xb00018c5 | A Group Policy setting was used to override the fast/slow link detection.\r\n
0xb00018c6 | The network connection is using a WWAN device for connectivity.\r\n
0xb00018c8 | Group Policy detected a slow link during sync mode processing.\r\n
0xb00018c9 | The connection to DC timed out during the Group Policy sync mode process.\r\n
0xb00018ca | Group Policy switched the sync mode process to async mode.\r\n
0xb0001b69 | %3 %n%4%nThe call failed after %1 milliseconds.\r\n
0xb0001b6a | Script for %3 failed in %1 seconds.\r\n
0xb0001bcd | Group policy session completed with error.\r\n
0xb0001bd6 | Group Policy could not get applicable GPOs from the domain controller.\r\n
0xb0001c30 | Saved policies to the local datastore with error.\r\n
0xb0001c31 | Loaded policies from the local datastore with error.\r\n
0xb0001c59 | Downloaded policies with error.\r\n
0xb0001c98 | Error: %1 Error code %2.\r\n
0xb0001c99 | Error: %1 Parameter: %3 : Error code %2.\r\n
0xb0001c9e | Group Policy failed to discover the Domain Controller details in %1 milliseconds.\r\n
0xb0001f50 | %1 Extension (%2) requests a sync mode process.\r\n
0xb0002329 | This machine is configured to retrieve Group Policy files from a file share in an insecure way.%n%nUNC Path: %1%nMutual Authentication Enforced: %2%nIntegrity Enforced: %3%n%nGuidance: The UNC path contains logon scripts and/or files that control system security policies. Microsoft recommends configuring Windows to require both mutual authentication and integrity when accessing files on this UNC path.%n%nFor details on configuring Windows machines to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb0010fa0 | Starting computer boot policy processing for %2. %nActivity id: %1\r\n
0xb0010fa1 | Starting user logon Policy processing for %2. %nActivity id: %1\r\n
0xb0010fa2 | Starting policy processing due to network state change for computer %2. %nActivity id: %1\r\n
0xb0010fa3 | Starting policy processing due to network state change for user %2. %nActivity id: %1\r\n
0xb0010fa4 | Starting manual processing of policy for computer %2. %nActivity id: %1\r\n
0xb0010fa5 | Starting manual processing of policy for user %2. %nActivity id: %1\r\n
0xb0010fa6 | Starting periodic policy processing for computer %2. %nActivity id: %1\r\n
0xb0010fa7 | Starting periodic policy processing for user %2. %nActivity id: %1\r\n
0xb0011b58 | Computer boot policy processing failed for %3 in %1 seconds.\r\n
0xb0011b59 | User logon policy processing failed for %3 in %1 seconds.\r\n
0xb0011b5a | Policy processing due to network state change failed for computer %3 in %1 seconds.\r\n
0xb0011b5b | Policy processing due to network state change failed for user %3 in %1 seconds.\r\n
0xb0011b5c | Manual processing of policy failed for computer %3 in %1 seconds.\r\n
0xb0011b5d | Manual processing of policy failed for user %3 in %1 seconds.\r\n
0xb0011b5e | Periodic policy processing failed for computer %3 in %1 seconds.\r\n
0xb0011b5f | Periodic policy processing failed for user %3 in %1 seconds.\r\n
0xb0011f40 | Completed computer boot policy processing for %3 in %1 seconds.\r\n
0xb0011f41 | Completed user logon policy processing for %3 in %1 seconds.\r\n
0xb0011f42 | Completed policy processing due to network state change for computer %3 in %1 seconds.\r\n
0xb0011f43 | Completed policy processing due to network state change for user %3 in %1 seconds.\r\n
0xb0011f44 | Completed manual processing of policy for computer %3 in %1 seconds.\r\n
0xb0011f45 | Completed manual processing of policy for user %3 in %1 seconds.\r\n
0xb0011f46 | Completed periodic policy processing for computer %3 in %1 seconds.\r\n
0xb0011f47 | Completed periodic policy processing for user %3 in %1 seconds.\r\n
0xd0000001 | No need for synchronous\r\n
0xd0000002 | First policy refresh\r\n
0xd0000003 | CSE requires foreground\r\n
0xd0000004 | CSE returned error\r\n
0xd0000005 | Forced synchronous refresh\r\n
0xd0000006 | Synchronous policy\r\n
0xd0000007 | SKU\r\n
0xd0000008 | Scripts synchronous\r\n
0xd0000009 | Synchronous due to internal processing error\r\n
0xd000000a | Background\r\n
0xd000000b | Foreground synchronous\r\n
0xd000000c | Foreground asynchronous\r\n
0xd000000d | "No loopback mode"\r\n
0xd000000e | "Merge"\r\n
0xd000000f | "Replace"\r\n
0xd0000010 | Startup script\r\n
0xd0000011 | Logon script\r\n
0xd0000012 | Logoff script\r\n
0xd0000013 | Shutdown script\r\n
0xd0000014 | User\r\n
0xd0000015 | Computer\r\n
0xd0000016 | CreateSession\r\n
0xd0000017 | Logon\r\n
0xd0000018 | Logoff\r\n
0xd0000019 | StartShell\r\n
0xd000001a | EndShell\r\n
0xd000001b | Preshutdown\r\n
