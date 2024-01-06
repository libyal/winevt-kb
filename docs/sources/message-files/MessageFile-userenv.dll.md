## userenv.dll

Path: %SystemRoot%\System32\userenv.dll

### 5.0.2195.6711

Message identifier | Message string
--- | ---
0xc00003e8 | %1\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x400005ec | Windows unloaded user %1 registry when it received a notification that no other applications or services were using the profile.\r\n
0x400005ed | Windows saved user %1 registry while an application or service was still using the registry during log off. The memory used by the user's registry has not been freed. The registry will be unloaded when it is no longer in use. %n%n\r\nThis is often caused by services running as a user account, try configuring the services to run in either the LocalService or NetworkService account.\r\n
0x800005f4 | Windows cannot unload your classes registry file - it is still in use by other applications or services. The file will be unloaded when it is no longer in use.  %n%n\r\n
0x800005f5 | Windows has detected that Offline Caching is enabled on the Roaming Profile share - to avoid potential profile corruption, Offline Caching must be disabled on shares where roaming user profiles are stored. %n%n\r\n
0xc00003e8 | %1\r\n
0xc00003e9 | Windows cannot load %1. (%2).\r\n
0xc00003ea | Windows cannot allocate memory. Contact your administrator. (%1).\r\n
0xc00003eb | Windows cannot process Group Policy Client Side Extension (%1). Exception %2.\r\n
0xc00003ec | The local Group Policy Object is disabled.\r\n
0xc00003ed | Windows cannot connect to %1 domain. (%2). Group Policy processing aborted. \r\n
0xc00003ee | Windows cannot bind to %1 domain. (%2). Group Policy processing aborted. \r\n
0xc00003ef | Windows cannot determine the associated site for this computer. (%1). Group Policy processing aborted. \r\n
0xc00003f0 | The search for the root Active Directory object failed with error (%1). Group Policy processing aborted. \r\n
0xc00003f1 | Windows is searching %1 for Group Policy objects.\r\n
0xc00003f2 | Windows found Group Policy object: %1, also known as %2.\r\n
0xc00003f3 | Windows found a Local Group Policy object.\r\n
0xc00003f4 | Windows cannot apply Group Policy object %1 because it is disabled.\r\n
0xc00003f5 | Windows cannot apply Group Policy object %1 because the link to the GPO is disabled.\r\n
0xc00003f6 | Windows cannot find any Group Policy objects for %1.\r\n
0xc00003f7 | Windows cannot find Group Policy object %1 in Active Directory. The object may not exist, or access to the object may be denied. (%2).\r\n
0xc00003f8 | Windows is setting registry value %1 to %2.\r\n
0xc00003f9 | Windows is setting registry value %1 to (%2).\r\n
0xc00003fa | Windows set the registry value %1 successfully.\r\n
0xc00003fb | Windows cannot set registry value %1. (%2).\r\n
0xc00003fc | Windows cannot create registry key %1. (%2).\r\n
0xc00003fd | Windows deleted registry value %1.\r\n
0xc00003fe | Windows cannot delete registry value %1. (%2).\r\n
0xc00003ff | Windows deleted registry key %1.\r\n
0xc0000400 | Windows completed processing of User Group Policy.\r\n
0xc0000401 | Windows completed processing of Computer Group Policy.\r\n
0xc0000402 | User or computer name: %1.\r\n
0xc0000403 | Domain name:  %1.\r\n
0xc0000404 | Domain controller name: %1.\r\n
0xc0000405 | Windows detected a slow network link.\r\n
0xc0000406 | Windows cannot query for the list of Group Policy objects. A message that describes the reason for this was previously logged by the policy engine.\r\n
0xc0000407 | Group Policy objects to be applied: %1.\r\n
0xc0000408 | Windows is starting computer Group Policy processing...\r\n
0xc0000409 | Windows is starting user Group Policy processing...\r\n
0xc000040a | There are no domain-based Group Policy objects for this user/computer.\r\n
0xc000040b | Windows cannot claim critical section. (%1). Group Policy processing aborted. \r\n
0xc000040c | Windows cannot load extension %1. (%2).\r\n
0xc000040d | Windows cannot find the entry point function in extension %1 and it will not be loaded.\r\n
0xc000040e | Windows cannot find the RSoP enabling entry point function (specified by ProcessGroupPolicyEx) in extension %1 and it will not be loaded.\r\n
0xc000040f | Windows cannot find the RSoP planning mode entry point function (specified by GenerateGroupPolicy) for extension <%1> in the dll %2 and it will not be loaded..\r\n
0xc0000410 | Windows cannot query ProcessGroupPolicy registry entry for %1 and it will not be loaded. This is most likely caused by a faulty registration.\r\n
0xc0000411 | Windows cannot query DllName registry entry for %1 and it will not be loaded. This is most likely caused by a faulty registration.\r\n
0xc0000412 | The list of Group Policy objects for this user or computer has changed. Windows will remove some Group Policy objects and apply the new list.\r\n
0xc0000413 | Windows cannot access the registry information at %1. (%2).\r\n
0xc0000414 | The user or computer does not have access to the Group Policy object %1.\r\n
0xc0000415 | The user or computer does not pass the filter check to the Group Policy object %1.\r\n
0xc0000416 | Windows did not detect any changes in the list of Group Policy objects: the revision numbers and the list of Group Policy objects are the same as the last time the policy was applied.\r\n
0xc0000417 | Windows cannot read the history of GPOs from the registry. Continuing Group Policy Processing. \r\n
0xc0000418 | The object %1 does not exist in Active Directory.\r\n
0xc0000419 | This computer is not a member of a domain.  Windows will apply local Group Policy only.\r\n
0xc000041a | This computer is a member of a domain without Active Directory support.\r\n
0xc000041b | This computer is a member of a domain with Active Directory support.\r\n
0xc000041c | Windows cannot determine the role of this computer. Group Policy processing aborted. \r\n
0xc000041d | Windows cannot determine the user or computer name. (%1). Group Policy processing aborted. \r\n
0xc000041e | Windows cannot obtain the domain controller name for your computer network. (%1). Group Policy processing aborted. \r\n
0xc000041f | Windows cannot determine the computer name. (%1). Group Policy processing aborted. \r\n
0xc0000420 | The computer's domain %1 is unavailable. (%2). Group Policy processing aborted. \r\n
0xc0000421 | GPO %1 does not have a file system path defined. The gPCFileSysPath property must have a UNC path to the GPO storage location on the SysVol.\r\n
0xc0000422 | Windows cannot access the file gpt.ini for GPO %1. The file must be present at the location <%2>. (%3). Group Policy processing aborted. \r\n
0xc0000423 | Windows cannot access common name (usually a GUID) for GPO %1. This is most likely caused by the cn property not being found or access denied. Group Policy processing aborted. \r\n
0xc0000424 | GPO %1 does not have a version number. The versionNumber property must be defined. An attempt to access it failed with error (%2). Group Policy processing aborted. \r\n
0xc0000425 | Windows will not add GPO %1 to the list of Group Policy objects because the 'Block from Above' attribute is set and the link to this GPO does not have ""No Override"" attribute set.\r\n
0xc0000426 | %1 has the 'Block From Above' attribute set.  All policies that can be overwritten will be removed from the list.\r\n
0xc0000427 | Windows cannot allocate memory. (%1).\r\n
0xc0000428 | Windows cannot check security for %1. (%2). Group Policy processing aborted. \r\n
0xc0000429 | Windows cannot perform filter check for Group Policy object %1. Group Policy processing aborted. \r\n
0xc000042a | Windows cannot read extensions from registry. Group Policy processing aborted. \r\n
0xc000042b | Windows did not apply extension %1, and flags are (%2).\r\n
0xc000042c | Windows ended GPO processing because the computer shut down or the user logged off.\r\n
0xc000042d | Windows cannot process extension %1. Return value (%2).\r\n
0xc000042e | Windows cannot obtain the deleted list for extension %1.\r\n
0xc000042f | Windows did not apply extension %1 because the registry extension failed.\r\n
0xc0000430 | GPO %1 does not have a functionality version number defined. Group Policy processing aborted. \r\n
0xc0000431 | GPO %1 was created by an older version of Group Policy Editor and cannot be processed. Please create a new Group Policy Object to replace this one.\r\n
0xc0000432 | GPO %1 does not contain any policy information because the version number is 0. Windows will not apply it.\r\n
0xc0000433 | Windows cannot set up GPO lists for Extensions to process. Group Policy processing aborted. \r\n
0xc0000434 | Windows did not apply extension %1 because there are no deleted or changed Group Policy objects.\r\n
0xc0000435 | Object %1 is not a member of objectClass %2. Group Policy processing aborted. \r\n
0xc0000436 | Windows cannot obtain the security ID of the user. Group Policy processing aborted. \r\n
0xc0000437 | Windows cannot search for Group Policy objects. (%1). Group Policy processing aborted. \r\n
0xc0000438 | Windows cannot search for Organizational Unit hierarchy. (%1). Group Policy processing aborted. \r\n
0xc0000439 | Windows cannot impersonate the user. (%1). Group Policy processing aborted. \r\n
0xc000043a | Windows cannot set the background refresh timer for Group Policy. %1 (%2). Group Policy processing aborted. \r\n
0xc000043b | Windows cannot write the security ID of the user to the registry. Group Policy processing aborted. \r\n
0xc000043c | Windows cannot move group policy history data from the user's old security ID to new security ID. Group Policy processing aborted. \r\n
0xc000043d | The Group Policy client-side extension %1 failed to execute. Please look for any errors reported earlier by that extension.\r\n
0xc000043e | Windows cannot do loopback processing for downlevel or local users.  Loopback processing will be disabled.\r\n
0xc000043f | Windows cannot do loopback processing when the computer is joined to a downlevel domain or is a member of a workgroup.  Loopback processing will be disabled.\r\n
0xc0000440 | Windows cannot query the list of Group Policy Objects because the number of GPOs has exceeded a maximum limit. Contact your network administrator to reduce the number of Group Policy Objects applied to you.\r\n
0xc0000441 | Windows couldn't set the RSoP (Resultant Set of Policies) session status for Group Policy Engine. (%1). No more RSoP logging will be done for this application of policy .\r\n
0xc0000442 | Windows couldn't log the RSoP (Resultant Set of Policies) session status. An attempt to connect to WMI failed. No more RSoP logging will be done for this application of policy.\r\n
0xc0000443 | The Group Policy client-side extension %1 failed to log RSOP (Resultant Set of Policy) data. Please look for any errors reported earlier by that extension.\r\n
0xc0000444 | The Group Policy client-side extension %1 does not support Diagnostic Mode RSOP (Resultant Set of Policy) logging. \r\n
0xc0000445 | The Group Policy client-side extension %1 does not support Planning Mode RSOP (Resultant Set of Policy) logging. \r\n
0xc0000446 | Windows could not set the security on Group Policy Events. (%1). Processing aborted. \r\n
0xc0000447 | Windows could not log all the RSOP (Resultant Set of Policy) Data. Group Policy processing will continue but the RSOP data might not be accurate. \r\n
0xc0000448 | Windows cannot access the registry policy file, %1. (%2).\r\n
0xc0000449 | Windows cannot find the machine account, %1.\r\n
0xc000044a | Windows cannot query for the site.\r\n
0xc000044b | Windows cannot access the GPLink property for the object %1 in Active Directory. The access to the object may be denied. The return value is (%2). Group Policy processing aborted. \r\n
0xc000044c | Windows has detected that the user/computer will be denied access on the object %1. Group Policy processing aborted. \r\n
0xc000044d | Windows cannot access the the object %1 in Active Directory. The access to the object may be denied. Group Policy processing aborted. \r\n
0xc000044e | Windows cannot find Group Policy object %1 in Active Directory. The object may not exist, or access to the object may be denied. \r\n
0xc000044f | There are no domain-based Group Policy objects for this user/computer.\r\n
0xc0000450 | Windows cannot perform filter check for Group Policy object %1. The associated filter cannot be found. This Group Policy Object will be skipped.\r\n
0xc0000451 | Windows cannot initialize connection to %1 domain. (%2). Group Policy processing aborted. \r\n
0xc00005dc | Windows cannot log you on because your profile cannot be loaded. Check that you are connected to the network, or that your network is functioning correctly. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005dd | Windows cannot create a temporary profile directory. This may be caused by insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005de | Windows cannot load the locally stored profile. Possible causes of this error include insufficient security rights or a corrupt local profile. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005df | Windows cannot set security on your registry. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005e0 | Windows cannot update your roaming profile. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005e1 | Windows cannot load the user's profile but has logged you on with the default profile for the system. %n%n\r\nDETAIL - %1\r\n
0xc00005e2 | Your roaming profile is not available. You are logged on with the locally stored profile. Changes to the profile will not be copied to the server. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005e3 | This computer is in manual policy mode, but the policy file cannot be found. Windows is logging you on without applying any policy. Return value (%1).\r\n
0xc00005e4 | Windows was unable to load the registry. This is often caused by insufficient memory or insufficient security rights. %n%n\r\nDETAIL - %1 for %2\r\n
0xc00005e5 | Windows cannot copy file %1 to location %2. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %3\r\n
0xc00005e6 | Windows cannot load your profile because it may be corrupted. Contact your administrator.\r\n
0xc00005e7 | Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.\r\n
0xc00005e8 | Windows cannot unload your registry file. The memory used by the registry has not been freed. This is often caused by services running as a user account, try configuring the services to run in either the LocalService or NetworkService account. If this problem persists, contact your administrator.  %n%n\r\nDETAIL - %1\r\n
0xc00005e9 | Windows cannot copy your profile  because it contains encrypted files or directories. The keys to decrypt the files or directories are also stored in the profile and are not\r\navailable now. Please decrypt the files and try again.\r\n
0xc00005ea | The roaming profile path %1 is too long. Windows is logging you on with a default profile.\r\n
0xc00005eb | Windows has backed up this user's profile. Windows will automatically try to use the backed up profile the next time this user logs on.\r\n
0xc00005ee | Windows cannot create a local profile and is logging you on with a temporary profile. This profile will be deleted when you log off. This may be caused by incorrect file system permissions or network problems.\r\n
0xc00005ef | Windows cannot locate your roaming mandatory profile and is attempting to log you on with your local profile. This may be caused by incorrect file system permissions or network problems. %n%n\r\nDETAIL - %1\r\n
0xc00005f0 | Windows cannot log you on because your roaming mandatory profile is not available. This may be caused by incorrect file system permissions or network problems. Contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005f1 | Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you logoff. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator.   %n%n\r\nDETAIL - %1\r\n
0xc00005f2 | Windows cannot locate your roaming profile (read only) and is attempting to log you on with your local profile. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005f3 | Your roaming profile (read only) is not available. You are logged on with the locally stored profile. This may be caused by incorrect file system permissions or network problems. Contact your network administrator. %n%n\r\nDETAIL - %1\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x400005ec | Windows unloaded user %1 registry when it received a notification that no other applications or services were using the profile.\r\n
0x400005ed | Windows saved user %1 registry while an application or service was still using the registry during log off. The memory used by the user's registry has not been freed. The registry will be unloaded when it is no longer in use. %n%n\r\nThis is often caused by services running as a user account, try configuring the services to run in either the LocalService or NetworkService account.\r\n
0x800005f4 | Windows cannot unload your classes registry file - it is still in use by other applications or services. The file will be unloaded when it is no longer in use.  %n%n\r\n
0x800005f5 | Windows has detected that Offline Caching is enabled on the Roaming Profile share - to avoid potential profile corruption, Offline Caching must be disabled on shares where roaming user profiles are stored. %n%n\r\n
0xc00003e8 | %1\r\n
0xc00003e9 | Windows cannot load %1. (%2).\r\n
0xc00003ea | Windows cannot allocate memory. Contact your administrator. (%1).\r\n
0xc00003eb | Windows cannot process Group Policy Client Side Extension (%1). Exception %2.\r\n
0xc00003ec | The local Group Policy Object is disabled.\r\n
0xc00003ed | Windows cannot connect to %1 domain. (%2). Group Policy processing aborted. \r\n
0xc00003ee | Windows cannot bind to %1 domain. (%2). Group Policy processing aborted. \r\n
0xc00003ef | Windows cannot determine the associated site for this computer. (%1). Group Policy processing aborted. \r\n
0xc00003f0 | The search for the root Active Directory object failed with error (%1). Group Policy processing aborted. \r\n
0xc00003f1 | Windows is searching %1 for Group Policy objects.\r\n
0xc00003f2 | Windows found Group Policy object: %1, also known as %2.\r\n
0xc00003f3 | Windows found a Local Group Policy object.\r\n
0xc00003f4 | Windows cannot apply Group Policy object %1 because it is disabled.\r\n
0xc00003f5 | Windows cannot apply Group Policy object %1 because the link to the GPO is disabled.\r\n
0xc00003f6 | Windows cannot find any Group Policy objects for %1.\r\n
0xc00003f7 | Windows cannot find Group Policy object %1 in Active Directory. The object may not exist, or access to the object may be denied. (%2).\r\n
0xc00003f8 | Windows is setting registry value %1 to %2.\r\n
0xc00003f9 | Windows is setting registry value %1 to (%2).\r\n
0xc00003fa | Windows set the registry value %1 successfully.\r\n
0xc00003fb | Windows cannot set registry value %1. (%2).\r\n
0xc00003fc | Windows cannot create registry key %1. (%2).\r\n
0xc00003fd | Windows deleted registry value %1.\r\n
0xc00003fe | Windows cannot delete registry value %1. (%2).\r\n
0xc00003ff | Windows deleted registry key %1.\r\n
0xc0000400 | Windows completed processing of User Group Policy.\r\n
0xc0000401 | Windows completed processing of Computer Group Policy.\r\n
0xc0000402 | User or computer name: %1.\r\n
0xc0000403 | Domain name:  %1.\r\n
0xc0000404 | Domain controller name: %1.\r\n
0xc0000405 | Windows detected a slow network link.\r\n
0xc0000406 | Windows cannot query for the list of Group Policy objects. Check the event log for possible messages previously logged by the policy engine that describes the reason for this.\r\n
0xc0000407 | Group Policy objects to be applied: %1.\r\n
0xc0000408 | Windows is starting computer Group Policy processing...\r\n
0xc0000409 | Windows is starting user Group Policy processing...\r\n
0xc000040a | There are no domain-based Group Policy objects for this user/computer.\r\n
0xc000040b | Windows cannot claim critical section. (%1). Group Policy processing aborted. \r\n
0xc000040c | Windows cannot load extension %1. (%2).\r\n
0xc000040d | Windows cannot find the entry point function in extension %1 and it will not be loaded.\r\n
0xc000040e | Windows cannot find the RSoP enabling entry point function (specified by ProcessGroupPolicyEx) in extension %1 and it will not be loaded.\r\n
0xc000040f | Windows cannot find the RSoP planning mode entry point function (specified by GenerateGroupPolicy) for extension <%1> in the dll %2 and it will not be loaded..\r\n
0xc0000410 | Windows cannot query ProcessGroupPolicy registry entry for %1 and it will not be loaded. This is most likely caused by a faulty registration.\r\n
0xc0000411 | Windows cannot query DllName registry entry for %1 and it will not be loaded. This is most likely caused by a faulty registration.\r\n
0xc0000412 | The list of Group Policy objects for this user or computer has changed. Windows will remove some Group Policy objects and apply the new list.\r\n
0xc0000413 | Windows cannot access the registry information at %1. (%2).\r\n
0xc0000414 | The user or computer does not have access to the Group Policy object %1.\r\n
0xc0000415 | The user or computer does not pass the filter check to the Group Policy object %1.\r\n
0xc0000416 | Windows did not detect any changes in the list of Group Policy objects: the revision numbers and the list of Group Policy objects are the same as the last time the policy was applied.\r\n
0xc0000417 | Windows cannot read the history of GPOs from the registry. Continuing Group Policy Processing. \r\n
0xc0000418 | The object %1 does not exist in Active Directory.\r\n
0xc0000419 | This computer is not a member of a domain.  Windows will apply local Group Policy only.\r\n
0xc000041a | This computer is a member of a domain without Active Directory support.\r\n
0xc000041b | This computer is a member of a domain with Active Directory support.\r\n
0xc000041c | Windows cannot determine the role of this computer. Group Policy processing aborted. \r\n
0xc000041d | Windows cannot determine the user or computer name. (%1). Group Policy processing aborted. \r\n
0xc000041e | Windows cannot obtain the domain controller name for your computer network. (%1). Group Policy processing aborted. \r\n
0xc000041f | Windows cannot determine the computer name. (%1). Group Policy processing aborted. \r\n
0xc0000420 | The computer's domain %1 is unavailable. (%2). Group Policy processing aborted. \r\n
0xc0000421 | GPO %1 does not have a file system path defined. The gPCFileSysPath property must have a UNC path to the GPO storage location on the SysVol.\r\n
0xc0000422 | Windows cannot access the file gpt.ini for GPO %1. The file must be present at the location <%2>. (%3). Group Policy processing aborted. \r\n
0xc0000423 | Windows cannot access common name (usually a GUID) for GPO %1. This is most likely caused by the cn property not being found or access denied. Group Policy processing aborted. \r\n
0xc0000424 | GPO %1 does not have a version number. The versionNumber property must be defined. An attempt to access it failed with error (%2). Group Policy processing aborted. \r\n
0xc0000425 | Windows will not add GPO %1 to the list of Group Policy objects because the 'Block from Above' attribute is set and the link to this GPO does not have ""No Override"" attribute set.\r\n
0xc0000426 | %1 has the 'Block From Above' attribute set.  All policies that can be overwritten will be removed from the list.\r\n
0xc0000427 | Windows cannot allocate memory. (%1).\r\n
0xc0000428 | Windows cannot check security for %1. (%2). Group Policy processing aborted. \r\n
0xc0000429 | Windows cannot perform filter check for Group Policy object %1. Group Policy processing aborted. \r\n
0xc000042a | Windows cannot read extensions from registry. Group Policy processing aborted. \r\n
0xc000042b | Windows did not apply extension %1, and flags are (%2).\r\n
0xc000042c | Windows ended GPO processing because the computer shut down or the user logged off.\r\n
0xc000042d | Windows cannot process extension %1. Return value (%2).\r\n
0xc000042e | Windows cannot obtain the deleted list for extension %1.\r\n
0xc000042f | Windows did not apply extension %1 because the registry extension failed.\r\n
0xc0000430 | GPO %1 does not have a functionality version number defined. Group Policy processing aborted. \r\n
0xc0000431 | GPO %1 was created by an older version of Group Policy Editor and cannot be processed. Please create a new Group Policy Object to replace this one.\r\n
0xc0000432 | GPO %1 does not contain any policy information because the version number is 0. Windows will not apply it.\r\n
0xc0000433 | Windows cannot set up GPO lists for Extensions to process. Group Policy processing aborted. \r\n
0xc0000434 | Windows did not apply extension %1 because there are no deleted or changed Group Policy objects.\r\n
0xc0000435 | Object %1 is not a member of objectClass %2. Group Policy processing aborted. \r\n
0xc0000436 | Windows cannot obtain the security ID of the user. Group Policy processing aborted. \r\n
0xc0000437 | Windows cannot search for Group Policy objects. (%1). Group Policy processing aborted. \r\n
0xc0000438 | Windows cannot search for Organizational Unit hierarchy. (%1). Group Policy processing aborted. \r\n
0xc0000439 | Windows cannot impersonate the user. (%1). Group Policy processing aborted. \r\n
0xc000043a | Windows cannot set the background refresh timer for Group Policy. %1 (%2). Group Policy processing aborted. \r\n
0xc000043b | Windows cannot write the security ID of the user to the registry. Group Policy processing aborted. \r\n
0xc000043c | Windows cannot move group policy history data from the user's old security ID to new security ID. Group Policy processing aborted. \r\n
0xc000043d | The Group Policy client-side extension %1 failed to execute. Please look for any errors reported earlier by that extension.\r\n
0xc000043e | Windows cannot do loopback processing for downlevel or local users.  Loopback processing will be disabled.\r\n
0xc000043f | Windows cannot do loopback processing when the computer is joined to a downlevel domain or is a member of a workgroup.  Loopback processing will be disabled.\r\n
0xc0000440 | Windows cannot query the list of Group Policy Objects because the number of GPOs has exceeded a maximum limit. Contact your network administrator to reduce the number of Group Policy Objects applied to you.\r\n
0xc0000441 | Windows couldn't set the RSoP (Resultant Set of Policies) session status for Group Policy Engine. (%1). No more RSoP logging will be done for this application of policy .\r\n
0xc0000442 | Windows couldn't log the RSoP (Resultant Set of Policies) session status. An attempt to connect to WMI failed. No more RSoP logging will be done for this application of policy.\r\n
0xc0000443 | The Group Policy client-side extension %1 failed to log RSOP (Resultant Set of Policy) data. Please look for any errors reported earlier by that extension.\r\n
0xc0000444 | The Group Policy client-side extension %1 does not support Diagnostic Mode RSOP (Resultant Set of Policy) logging. \r\n
0xc0000445 | The Group Policy client-side extension %1 does not support Planning Mode RSOP (Resultant Set of Policy) logging. \r\n
0xc0000446 | Windows could not set the security on Group Policy Events. (%1). Processing aborted. \r\n
0xc0000447 | Windows could not log all the RSOP (Resultant Set of Policy) Data. Group Policy processing will continue but the RSOP data might not be accurate. \r\n
0xc0000448 | Windows cannot access the registry policy file, %1. (%2).\r\n
0xc0000449 | Windows cannot find the machine account, %1.\r\n
0xc000044a | Windows cannot query for the site.\r\n
0xc000044b | Windows cannot access the GPLink property for the object %1 in Active Directory. The access to the object may be denied. The return value is (%2). Group Policy processing aborted. \r\n
0xc000044c | Windows has detected that the user/computer will be denied access on the object %1. Group Policy processing aborted. \r\n
0xc000044d | Windows cannot access the the object %1 in Active Directory. The access to the object may be denied. Group Policy processing aborted. \r\n
0xc000044e | Windows cannot find Group Policy object %1 in Active Directory. The object may not exist, or access to the object may be denied. \r\n
0xc000044f | There are no domain-based Group Policy objects for this user/computer.\r\n
0xc0000450 | Windows cannot perform filter check for Group Policy object %1. The associated filter cannot be found. This Group Policy Object will be skipped.\r\n
0xc0000451 | Windows cannot initialize connection to %1 domain. (%2). Group Policy processing aborted. \r\n
0xc0000452 | Windows cannot perform filter check for Group Policy object %1. The WMI service is currently disabled. This Group Policy Object will be skipped.\r\n
0xc0000453 | Windows cannot initialize resources for Group Policy Processing. (%1). Group Policy processing aborted. \r\n
0xc0000454 | Windows cannot read the user policy loopback mode for policy application. (%1). Group Policy processing aborted. \r\n
0xc0000455 | %1 from a different forest logged onto this machine. Cross Forest Group Policy processing is disabled and loopback processing has been enforced in this forest for this user account.\r\n
0xc0000456 | Attempt to determine whether user and machine accounts are in the same forest failed (%1).\r\n
0xc00005dc | Windows cannot log you on because your profile cannot be loaded. Check that you are connected to the network, or that your network is functioning correctly. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005dd | Windows cannot create a temporary profile directory. This may be caused by insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005de | Windows cannot load the locally stored profile. Possible causes of this error include insufficient security rights or a corrupt local profile. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005df | Windows cannot set security on your registry. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005e0 | Windows cannot update your roaming profile. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005e1 | Windows cannot load the user's profile but has logged you on with the default profile for the system. %n%n\r\nDETAIL - %1\r\n
0xc00005e2 | Your roaming profile is not available. You are logged on with the locally stored profile. Changes to the profile will not be copied to the server. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005e3 | This computer is in manual policy mode, but the policy file cannot be found. Windows is logging you on without applying any policy. Return value (%1).\r\n
0xc00005e4 | Windows was unable to load the registry. This is often caused by insufficient memory or insufficient security rights. %n%n\r\nDETAIL - %1 for %2\r\n
0xc00005e5 | Windows cannot copy file %1 to location %2. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %3\r\n
0xc00005e6 | Windows cannot load your profile because it may be corrupted. Contact your administrator.\r\n
0xc00005e7 | Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.\r\n
0xc00005e8 | Windows cannot unload your registry file. The memory used by the registry has not been freed. This is often caused by services running as a user account, try configuring the services to run in either the LocalService or NetworkService account. If this problem persists, contact your administrator.  %n%n\r\nDETAIL - %1\r\n
0xc00005e9 | Windows cannot copy your profile  because it contains encrypted files or directories. The keys to decrypt the files or directories are also stored in the profile and are not\r\navailable now. Please decrypt the files and try again.\r\n
0xc00005ea | The roaming profile path %1 is too long. Windows is logging you on with a default profile.\r\n
0xc00005eb | Windows has backed up this user's profile. Windows will automatically try to use the backed up profile the next time this user logs on.\r\n
0xc00005ee | Windows cannot create a local profile and is logging you on with a temporary profile. This profile will be deleted when you log off. This may be caused by incorrect file system permissions or network problems.\r\n
0xc00005ef | Windows cannot locate your roaming mandatory profile and is attempting to log you on with your local profile. This may be caused by incorrect file system permissions or network problems. %n%n\r\nDETAIL - %1\r\n
0xc00005f0 | Windows cannot log you on because your roaming mandatory profile is not available. This may be caused by incorrect file system permissions or network problems. Contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005f1 | Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you logoff. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator.   %n%n\r\nDETAIL - %1\r\n
0xc00005f2 | Windows cannot locate your roaming profile (read only) and is attempting to log you on with your local profile. Possible causes of this error include network problems or insufficient security rights. If this problem persists, contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005f3 | Your roaming profile (read only) is not available. You are logged on with the locally stored profile. This may be caused by incorrect file system permissions or network problems. Contact your network administrator. %n%n\r\nDETAIL - %1\r\n
0xc00005f6 | Windows did not load your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you logoff. Windows did not load your profile because a server copy of the profile folder already exists that does not have the correct security. Either the current user or the Administrator's group must be the owner of the folder. Contact your network administrator. %n%n\r\n
0xc00005f7 | Windows failed Initialize user profiles. Non-console users will be unable to log on. Contact your network administrator.\r\n
0xc00005f9 | Cross Forest roaming user profiles are disabled. Windows did not load your roaming profile and is logging you on with a local profile. Changes to the profile will not be copied to the server when you logoff.  Contact your network administrator. \r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x800005e5 | Windows cannot copy file %1 to location %2. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %3\r\n
0x800005fe | There are too many profile copy errors. Refer to the previous events for details. Windows will not log any additional copy errors for this copy process. %n%n\r\n
0x80000640 | Windows cannot copy profile from %1 to %2, you do not have enough disk space.%n%n\r\n
0x80000641 | Windows cannot copy profile from %1 to %2, you have exceeded the profile quota.%n%n\r\n
0x90000001 | Microsoft-Windows-User Profile General\r\n
0xc00005df | Windows cannot set security on your registry. %n%n DETAIL - %1\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x000005e5 | Windows cannot copy file %1 to location %2. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %3\r\n
0x000005fe | There are too many profile copy errors. Refer to the previous events for details. Windows will not log any additional copy errors for this copy process. %n%n\r\n
0x00000640 | Windows cannot copy profile from %1 to %2, you do not have enough disk space.%n%n\r\n
0x00000641 | Windows cannot copy profile from %1 to %2, you have exceeded the profile quota.%n%n\r\n
0x50000003 | Warning\r\n
0x90000001 | Microsoft-Windows-User Profile General\r\n
0x90000002 | Application\r\n

### 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x000005e5 | Windows cannot copy file %1 to location %2. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %3\r\n
0x000005fe | There are too many profile copy errors. Refer to the previous events for details. Windows will not log any additional copy errors for this copy process. %n%n\r\n
0x00000640 | Windows cannot copy profile from %1 to %2, you do not have enough disk space.%n%n\r\n
0x00000641 | Windows cannot copy profile from %1 to %2, you have exceeded the profile quota.%n%n\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-User Profile General\r\n
0x90000002 | Application\r\n
0xb0000045 | %1 which has timestamp %2 was not copied to %3 which has timestamp %4 since it is older than the file it would be overwriting.\r\n
0xb00003ee | File %1 of size %2 kilobytes copied from %3 to %4 in %5 seconds.\r\n
0xb00003ef | %1 which has timestamp %2 was not copied to %3 which has timestamp %4 since it is older than the file it would be overwriting.\r\n
