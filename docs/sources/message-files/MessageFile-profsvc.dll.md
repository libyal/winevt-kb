## profsvc.dll

Path: %SystemRoot%\System32\profsvc.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x400005ec | Windows unloaded user %1 registry when it received a notification that no other applications or services were using the profile.\r\n
0x400005ed | Windows saved user %1 registry while an application or service was still using the registry when the user logged off. The memory used by the user registry has not been freed. The registry will be unloaded when it is no longer in use. %n%n This error may be caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account.\r\n
0x400005fb | The User Profile Service has started successfully.  %n%n\r\n
0x400005fc | The User Profile Service has stopped.  %n%n\r\n
0x400005ff | Successfully suspended folder "%1"\r\n
0x40000600 | Successfully unsuspended folder "%1"\r\n
0x800005f4 | Windows cannot unload your classes registry file - it is still in use by other applications or services. The file will be unloaded when it is no longer in use.  %n%n\r\n
0x800005f5 | Windows has detected that Automatic Offline Caching is enabled on the Roaming Profile share - to avoid potential profile corruption, Offline Caching must be set to manual or disabled on shares where roaming user profiles are stored. %n%n\r\n
0x800005fa | Windows detected your registry file is still in use by other applications or services. The file will be unloaded now. The applications or services that hold your registry file may not function properly afterwards.  %n%n DETAIL - %n %1\r\n
0x800005fe | Profile notification of event %1 for component %2 failed, error code is %3. %n%n\r\n
0x80000604 | Your roaming profile is not synchronized correctly with the server. Windows will load your previously-saved local profile instead. See the previous events for details.\r\n
0x90000001 | Microsoft-Windows-User Profile Service\r\n
0xc00005dc | Windows cannot log you on because your profile cannot be loaded. Check that you are connected to the network, and that your network is functioning correctly. %n%n DETAIL - %1\r\n
0xc00005dd | Windows cannot create a temporary profile directory. This problem may be caused by insufficient security rights. %n%n DETAIL - %1\r\n
0xc00005de | Windows cannot load the locally stored profile. Possible causes of this error include insufficient security rights or a corrupt local profile. %n%n DETAIL - %1\r\n
0xc00005df | Windows cannot set security on your registry. %n%n DETAIL - %1\r\n
0xc00005e0 | Windows Windows cannot update your roaming profile completely. Check previous events for more details. %n%n\r\n
0xc00005e1 | Windows cannot load the user's profile but has logged you on with the default profile for the system. %n%n DETAIL - %1\r\n
0xc00005e2 | Your roaming profile is not available. You are logged on with the locally stored profile. Changes to the profile will not be copied to the server. Possible causes of this error include network problems or insufficient security rights.  %n%n DETAIL - %1\r\n
0xc00005e4 | Windows was unable to load the registry. This problem is often caused by insufficient memory or insufficient security rights. %n%n DETAIL - %1 for %2\r\n
0xc00005e6 | Windows cannot load your profile because it appears to be corrupted.\r\n
0xc00005e7 | Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.\r\n
0xc00005e8 | Windows cannot unload your registry file. The memory used by the registry has not been freed. This problem is often caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account. %n%n DETAIL - %1\r\n
0xc00005e9 | Windows cannot copy your profile because it contains encrypted files or directories. The keys to decrypt the files or directories are also stored in the profile and are not available now. Decrypt the files and try again.\r\n
0xc00005ea | The roaming profile path %1 is too long. Windows is logging you on with a default profile.\r\n
0xc00005eb | Windows has backed up this user profile. Windows will automatically try to use the backup profile the next time this user logs on.\r\n
0xc00005ee | Windows cannot create a local profile and is logging you on with a temporary profile. This profile will be deleted when you log off. This problem may be caused by incorrect file system permissions or network problems.\r\n
0xc00005ef | Windows cannot locate your roaming mandatory profile and is attempting to log you on with your local profile. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0xc00005f0 | Windows cannot log you on because your roaming mandatory profile is not available. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0xc00005f1 | Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0xc00005f2 | Windows cannot locate your roaming profile (read only) and is attempting to log you on with your local profile. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0xc00005f3 | Your roaming profile (read only) is not available. You are logged on with the locally stored profile. This error may be caused by incorrect file system permissions or network problems.  %n%n DETAIL - %1\r\n
0xc00005f6 | Windows could not load your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. Windows could not load your profile because a server copy of the profile folder already exists that does not have the correct security. Either the current user or the Administrators group must be the owner of the folder. %n%n\r\n
0xc00005f7 | Windows failed to initialize user profiles. Non-console users will be unable to log on.\r\n
0xc00005f9 | Roaming user profiles across forests are disabled. Windows did not load your roaming profile and is logging you on with a local profile. Changes to the profile will not be copied to the server when you log off.\r\n
0xc00005fd | Windows cannot delete the profile directory %1. This error may be caused by files in this directory being used by another program. %n%n DETAIL - %2\r\n
0xc0000601 | Failed to suspend folder "%1"%n DETAIL - %2\r\n
0xc0000602 | Failed to unsuspend folder "%1"%n DETAIL - %2\r\n
0xc0000603 | Failed to sync folder "%1"%n DETAIL - %2\r\n
0xc0000605 | Failed to apply CSC suspend policy. Cannot connect to CSC service.%n DETAIL - %1\r\n
0xc0000606 | Windows cannot load classes registry file.%n DETAIL - %1\r\n
0xc0000607 | A slow network connection is detected for the roaming profile %1. It will not be synchronized with the profile on this computer.\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x000005dc | Windows cannot log you on because your profile cannot be loaded. Check that you are connected to the network, and that your network is functioning correctly. %n%n DETAIL - %1\r\n
0x000005dd | Windows cannot create a temporary profile directory. This problem may be caused by insufficient security rights. %n%n DETAIL - %1\r\n
0x000005de | Windows cannot load the locally stored profile. Possible causes of this error include insufficient security rights or a corrupt local profile. %n%n DETAIL - %1\r\n
0x000005df | Windows cannot set security on your registry. %n%n DETAIL - %1\r\n
0x000005e0 | Windows Windows cannot update your roaming profile completely. Check previous events for more details. %n%n\r\n
0x000005e1 | Windows cannot load the user's profile but has logged you on with the default profile for the system. %n%n DETAIL - %1\r\n
0x000005e2 | Your roaming profile is not available. You are logged on with the locally stored profile. Changes to the profile will not be copied to the server. Possible causes of this error include network problems or insufficient security rights.  %n%n DETAIL - %1\r\n
0x000005e4 | Windows was unable to load the registry. This problem is often caused by insufficient memory or insufficient security rights. %n%n DETAIL - %1 for %2\r\n
0x000005e6 | Windows cannot load your profile because it appears to be corrupted.\r\n
0x000005e7 | Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.\r\n
0x000005e8 | Windows cannot unload your registry file. The memory used by the registry has not been freed. This problem is often caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account. %n%n DETAIL - %1\r\n
0x000005e9 | Windows cannot copy your profile because it contains encrypted files or directories. The keys to decrypt the files or directories are also stored in the profile and are not available now. Decrypt the files and try again.\r\n
0x000005ea | The roaming profile path %1 is too long. Windows is logging you on with a default profile.\r\n
0x000005eb | Windows has backed up this user profile. Windows will automatically try to use the backup profile the next time this user logs on.\r\n
0x000005ed | Windows saved user %1 registry while an application or service was still using the registry when the user logged off. The memory used by the user registry has not been freed. The registry will be unloaded when it is no longer in use. %n%n This error may be caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account.\r\n
0x000005ee | Windows cannot create a local profile and is logging you on with a temporary profile. This profile will be deleted when you log off. This problem may be caused by incorrect file system permissions or network problems.\r\n
0x000005ef | Windows cannot locate your roaming mandatory profile and is attempting to log you on with your local profile. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f0 | Windows cannot log you on because your roaming mandatory profile is not available. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f1 | Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f2 | Windows cannot locate your roaming profile (read only) and is attempting to log you on with your local profile. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f3 | Your roaming profile (read only) is not available. You are logged on with the locally stored profile. This error may be caused by incorrect file system permissions or network problems.  %n%n DETAIL - %1\r\n
0x000005f4 | Windows cannot unload your classes registry file - it is still in use by other applications or services. The file will be unloaded when it is no longer in use.  %n%n\r\n
0x000005f5 | Windows has detected that Automatic Offline Caching is enabled on the Roaming Profile share - to avoid potential profile corruption, Offline Caching must be set to manual or disabled on shares where roaming user profiles are stored. %n%n\r\n
0x000005f6 | Windows could not load your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. Windows could not load your profile because a server copy of the profile folder already exists that does not have the correct security. Either the current user or the Administrators group must be the owner of the folder. %n%n\r\n
0x000005f7 | Windows failed to initialize user profiles. Non-console users will be unable to log on.\r\n
0x000005f9 | Roaming user profiles across forests are disabled. Windows did not load your roaming profile and is logging you on with a local profile. Changes to the profile will not be copied to the server when you log off.\r\n
0x000005fa | Windows detected your registry file is still in use by other applications or services. The file will be unloaded now. The applications or services that hold your registry file may not function properly afterwards.  %n%n DETAIL - %n %1\r\n
0x000005fb | The User Profile Service has started successfully.  %n%n\r\n
0x000005fc | The User Profile Service has stopped.  %n%n\r\n
0x000005fd | Windows cannot delete the profile directory %1. This error may be caused by files in this directory being used by another program. %n%n DETAIL - %2\r\n
0x000005fe | Profile notification of event %1 for component %2 failed, error code is %3. %n%n\r\n
0x000005ff | Successfully suspended folder "%1"\r\n
0x00000600 | Successfully unsuspended folder "%1"\r\n
0x00000601 | Failed to suspend folder "%1"%n DETAIL - %2\r\n
0x00000602 | Failed to unsuspend folder "%1"%n DETAIL - %2\r\n
0x00000603 | Failed to sync folder "%1"%n DETAIL - %2\r\n
0x00000604 | Your roaming profile is not synchronized correctly with the server. Windows will load your previously-saved local profile instead. See the previous events for details.\r\n
0x00000605 | Failed to apply CSC suspend policy. Cannot connect to CSC service.%n DETAIL - %1\r\n
0x00000606 | Windows cannot load classes registry file.%n DETAIL - %1\r\n
0x00000607 | A slow network connection is detected for the roaming profile %1. It will not be synchronized with the profile on this computer.\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-User Profile Service\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-User Profile Service/Operational\r\n
0xb0000001 | Recieved user logon notification on session %1.\r\n
0xb0000002 | Finished processing user logon notification on session %1.\r\n
0xb0000003 | Recieved user logoff notification on session %1.\r\n
0xb0000004 | Finished processing user logoff notification on session %1.\r\n
0xb0000005 | Registry file %1 is loaded at HKU\%2.\r\n
0xb0000006 | Starting synchronize profile from %1 to %2.\r\n
0xb0000007 | Finished synchronize profile from %1 to %2. %n%nResult: %3\r\n
0xb0000032 | Background hive upload for user %1 started.\r\n
0xb0000033 | Background hive upload for user %1 succeeded.\r\n
0xb0000034 | Background hive upload for user %1 failed.%n%n Error: %2\r\n
0xb0000035 | Cannot delete file %1.%n%n Error: %2\r\n
0xb0000036 | Open user regisry root key for %1 failed.%n%n Error: %2\r\n
0xb0000037 | Save user hive to file %1 failed.%n%n Error: %2\r\n
0xb0000038 | Save user hive to file %1 succeeded.\r\n
0xb0000039 | Enable background user hive upload task succeeded.\r\n
0xb000003a | Failed to enable background user hive upload task.%n%n Error: %1\r\n
0xb000003b | Disable background user hive upload task succeeded.\r\n
0xb000003c | Failed to disable background user hive upload task.%n%n Error: %1\r\n
0xb000003d | Slow network connection detected, abort background user hive upload task.\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x000005dc | Windows cannot log you on because your profile cannot be loaded. Check that you are connected to the network, and that your network is functioning correctly. %n%n DETAIL - %1\r\n
0x000005dd | Windows cannot create a temporary profile directory. This problem may be caused by insufficient security rights. %n%n DETAIL - %1\r\n
0x000005de | Windows cannot load the locally stored profile. Possible causes of this error include insufficient security rights or a corrupt local profile. %n%n DETAIL - %1\r\n
0x000005df | Windows cannot set security on your registry. %n%n DETAIL - %1\r\n
0x000005e0 | Windows cannot update your roaming profile completely. Check previous events for more details. %n%n\r\n
0x000005e1 | Windows cannot load the user's profile but has logged you on with the default profile for the system. %n%n DETAIL - %1\r\n
0x000005e2 | Your roaming profile is not available. You are logged on with the locally stored profile. Changes to the profile will not be copied to the server. Possible causes of this error include network problems or insufficient security rights.  %n%n DETAIL - %1\r\n
0x000005e4 | Windows was unable to load the registry. This problem is often caused by insufficient memory or insufficient security rights. %n%n DETAIL - %1 for %2\r\n
0x000005e5 | Windows was unable to load %1.\r\n
0x000005e6 | Windows cannot load your profile because it appears to be corrupted.\r\n
0x000005e7 | Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.\r\n
0x000005e8 | Windows cannot unload your registry file. The memory used by the registry has not been freed. This problem is often caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account. %n%n DETAIL - %1\r\n
0x000005e9 | Windows cannot copy your profile because it contains encrypted files or directories. The keys to decrypt the files or directories are also stored in the profile and are not available now. Decrypt the files and try again.\r\n
0x000005ea | The roaming profile path %1 is too long. Windows is logging you on with a default profile.\r\n
0x000005eb | Windows has backed up this user profile. Windows will automatically try to use the backup profile the next time this user logs on.\r\n
0x000005ed | Windows saved user %1 registry while an application or service was still using the registry when the user logged off. The memory used by the user registry has not been freed. The registry will be unloaded when it is no longer in use. %n%n This error may be caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account.\r\n
0x000005ee | Windows cannot create a local profile and is logging you on with a temporary profile. This profile will be deleted when you log off. This problem may be caused by incorrect file system permissions or network problems.\r\n
0x000005ef | Windows cannot locate your roaming mandatory profile and is attempting to log you on with your local profile. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f0 | Windows cannot log you on because your roaming mandatory profile is not available. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f1 | Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f2 | Windows cannot locate your roaming profile (read only) and is attempting to log you on with your local profile. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f3 | Your roaming profile (read only) is not available. You are logged on with the locally stored profile. This error may be caused by incorrect file system permissions or network problems.  %n%n DETAIL - %1\r\n
0x000005f4 | Windows cannot unload your classes registry file - it is still in use by other applications or services. The file will be unloaded when it is no longer in use.  %n%n\r\n
0x000005f5 | Windows has detected that Automatic Offline Caching is enabled on the Roaming Profile share - to avoid potential profile corruption, Offline Caching must be set to manual or disabled on shares where roaming user profiles are stored. %n%n\r\n
0x000005f6 | Windows could not load your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. Windows could not load your profile because a server copy of the profile folder already exists that does not have the correct security. Either the current user or the Administrators group must be the owner of the folder. %n%n\r\n
0x000005f7 | Windows failed to initialize user profiles. Non-console users will be unable to log on.\r\n
0x000005f9 | Roaming user profiles across forests are disabled. Windows did not load your roaming profile and is logging you on with a local profile. Changes to the profile will not be copied to the server when you log off.\r\n
0x000005fa | Windows detected your registry file is still in use by other applications or services. The file will be unloaded now. The applications or services that hold your registry file may not function properly afterwards.  %n%n DETAIL - %n %1\r\n
0x000005fb | The User Profile Service has started successfully.  %n%n\r\n
0x000005fc | The User Profile Service has stopped.  %n%n\r\n
0x000005fd | Windows cannot delete the profile directory %1. This error may be caused by files in this directory being used by another program. %n%n DETAIL - %2\r\n
0x000005fe | Profile notification of event %1 for component %2 failed, error code is %3. %n%n\r\n
0x000005ff | Successfully suspended folder "%1"\r\n
0x00000600 | Successfully unsuspended folder "%1"\r\n
0x00000601 | Failed to suspend folder "%1"%n DETAIL - %2\r\n
0x00000602 | Failed to unsuspend folder "%1"%n DETAIL - %2\r\n
0x00000603 | Failed to sync folder "%1"%n DETAIL - %2\r\n
0x00000604 | Your roaming profile is not synchronized correctly with the server. Windows will load your previously-saved local profile instead. See the previous events for details.\r\n
0x00000605 | Failed to apply CSC suspend policy. Cannot connect to CSC service.%n DETAIL - %1\r\n
0x00000606 | Windows cannot load classes registry file.%n DETAIL - %1\r\n
0x00000607 | A slow network connection is detected for the roaming profile %1. It will not be synchronized with the profile on this computer.\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-User Profile Service\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-User Profile Service/Operational\r\n
0xb0000001 | Recieved user logon notification on session %1.\r\n
0xb0000002 | Finished processing user logon notification on session %1.\r\n
0xb0000003 | Recieved user logoff notification on session %1.\r\n
0xb0000004 | Finished processing user logoff notification on session %1.\r\n
0xb0000005 | Registry file %1 is loaded at HKU\%2.\r\n
0xb0000006 | Starting synchronize profile from %1 to %2.\r\n
0xb0000007 | Finished synchronize profile from %1 to %2. %n%nResult: %3\r\n
0xb0000032 | Background hive upload for user %1 started.\r\n
0xb0000033 | Background hive upload for user %1 succeeded.\r\n
0xb0000034 | Background hive upload for user %1 failed.%n%n Error: %2\r\n
0xb0000035 | Cannot delete file %1.%n%n Error: %2\r\n
0xb0000036 | Open user regisry root key for %1 failed.%n%n Error: %2\r\n
0xb0000037 | Save user hive to file %1 failed.%n%n Error: %2\r\n
0xb0000038 | Save user hive to file %1 succeeded.\r\n
0xb0000039 | Enable background user hive upload task succeeded.\r\n
0xb000003a | Failed to enable background user hive upload task.%n%n Error: %1\r\n
0xb000003b | Disable background user hive upload task succeeded.\r\n
0xb000003c | Failed to disable background user hive upload task.%n%n Error: %1\r\n
0xb000003d | Slow network connection detected, abort background user hive upload task.\r\n
0xb000003e | Windows was unable to successfully evaluate whether this computer is a primary computer for this user. This may be due to failing to access the Active Directory server at this time. The user's roaming profile will be applied as configured. Contact the Administrator for more assistance. Error: %1\r\n
0xb000003f | This computer %1 a primary computer for this user.\r\n
0xb0000040 | The primary computer relationship for this computer and this user was not evaluated due to %1.\r\n
0xb0000041 | The attempt to create or open the profile key for the user failed with error %1.\r\n
0xb0000042 | Creating the local profile for the user failed with error %1.\r\n
0xb0000043 | Logon type: %1 %nLocal profile location: %2 %nProfile type: %3\r\n
0xb0000044 | LastDownloadTime: %1 %nLastUploadTime: %2\r\n
0xb0000046 | Waiting on network arrivals. Max wait time %1 ms.\r\n
0xb0000047 | After waiting %1 ms, a network with the necessary capabilities was not ready for use. Allowing profile load to proceed.\r\n
0xb0000048 | Terminating wait due to unexpected failure %1.\r\n
0xb0000049 | Wait complete due to connectivity event but network not ready.\r\n
0xb000004a | Wait completed due to network connectivity or determination that no viable network connection is likely to become available. Allowing profile load to proceed.\r\n
0xb000004b | Roaming Profiles configuration is being controlled by Group Policy.\r\n
0xb000004c | Roaming Profiles configuration is being controlled by WMI configuration classes Win32_RoamingProfileUserConfiguration and Win32_RoamingProfileMachineConfiguration.\r\n
0xb00003e9 | Begin new user profile creation.\r\n
0xb00003ea | New user profile creation complete.\r\n
0xb00003eb | A network latency of %1 milliseconds has been detected.  Maximum latency to synchronize a roaming profile is set at %2 milliseconds.\r\n
0xb00003ec | A network bandwidth of %1 kilobits per second has been detected.  Minimum bandwidth to synchronize a roaming profile is set at %2 kilobits per second.\r\n
0xb00003ed | Delete cached profile %1 since it is older than %2 days.\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x000005dc | Windows cannot log you on because your profile cannot be loaded. Check that you are connected to the network, and that your network is functioning correctly. %n%n DETAIL - %1\r\n
0x000005dd | Windows cannot create a temporary profile directory. This problem may be caused by insufficient security rights. %n%n DETAIL - %1\r\n
0x000005de | Windows cannot load the locally stored profile. Possible causes of this error include insufficient security rights or a corrupt local profile. %n%n DETAIL - %1\r\n
0x000005df | Windows cannot set security on your registry. %n%n DETAIL - %1\r\n
0x000005e0 | Windows cannot update your roaming profile completely. Check previous events for more details. %n%n\r\n
0x000005e1 | Windows cannot load the user's profile but has logged you on with the default profile for the system. %n%n DETAIL - %1\r\n
0x000005e2 | Your roaming profile is not available. You are logged on with the locally stored profile. Changes to the profile will not be copied to the server. Possible causes of this error include network problems or insufficient security rights.  %n%n DETAIL - %1\r\n
0x000005e4 | Windows was unable to load the registry. This problem is often caused by insufficient memory or insufficient security rights. %n%n DETAIL - %1 for %2\r\n
0x000005e5 | Windows was unable to load %1.\r\n
0x000005e6 | Windows cannot load your profile because it appears to be corrupted.\r\n
0x000005e7 | Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.\r\n
0x000005e8 | Windows cannot unload your registry file. The memory used by the registry has not been freed. This problem is often caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account. %n%n DETAIL - %1\r\n
0x000005e9 | Windows cannot copy your profile because it contains encrypted files or directories. The keys to decrypt the files or directories are also stored in the profile and are not available now. Decrypt the files and try again.\r\n
0x000005ea | The roaming profile path %1 is too long. Windows is logging you on with a default profile.\r\n
0x000005eb | Windows has backed up this user profile. Windows will automatically try to use the backup profile the next time this user logs on.\r\n
0x000005ed | Windows saved user %1 registry while an application or service was still using the registry when the user logged off. The memory used by the user registry has not been freed. The registry will be unloaded when it is no longer in use. %n%n This error may be caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account.\r\n
0x000005ee | Windows cannot create a local profile and is logging you on with a temporary profile. This profile will be deleted when you log off. This problem may be caused by incorrect file system permissions or network problems.\r\n
0x000005ef | Windows cannot locate your roaming mandatory profile and is attempting to log you on with your local profile. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f0 | Windows cannot log you on because your roaming mandatory profile is not available. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f1 | Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f2 | Windows cannot locate your roaming profile (read only) and is attempting to log you on with your local profile. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f3 | Your roaming profile (read only) is not available. You are logged on with the locally stored profile. This error may be caused by incorrect file system permissions or network problems.  %n%n DETAIL - %1\r\n
0x000005f4 | Windows cannot unload your classes registry file - it is still in use by other applications or services. The file will be unloaded when it is no longer in use.  %n%n\r\n
0x000005f5 | Windows has detected that Automatic Offline Caching is enabled on the Roaming Profile share - to avoid potential profile corruption, Offline Caching must be set to manual or disabled on shares where roaming user profiles are stored. %n%n\r\n
0x000005f6 | Windows could not load your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. Windows could not load your profile because a server copy of the profile folder already exists that does not have the correct security. Either the current user or the Administrators group must be the owner of the folder. %n%n\r\n
0x000005f7 | Windows failed to initialize user profiles. Non-console users will be unable to log on.\r\n
0x000005f9 | Roaming user profiles across forests are disabled. Windows did not load your roaming profile and is logging you on with a local profile. Changes to the profile will not be copied to the server when you log off.\r\n
0x000005fa | Windows detected your registry file is still in use by other applications or services. The file will be unloaded now. The applications or services that hold your registry file may not function properly afterwards. No user action is required.  %n%n DETAIL - %n %1\r\n
0x000005fb | The User Profile Service has started successfully.  %n%n\r\n
0x000005fc | The User Profile Service has stopped.  %n%n\r\n
0x000005fd | Windows cannot delete the profile directory %1. This error may be caused by files in this directory being used by another program. %n%n DETAIL - %2\r\n
0x000005fe | Profile notification of event %1 for component %2 failed, error code is %3. %n%n\r\n
0x000005ff | Successfully suspended folder "%1"\r\n
0x00000600 | Successfully unsuspended folder "%1"\r\n
0x00000601 | Failed to suspend folder "%1"%n DETAIL - %2\r\n
0x00000602 | Failed to unsuspend folder "%1"%n DETAIL - %2\r\n
0x00000603 | Failed to sync folder "%1"%n DETAIL - %2\r\n
0x00000604 | Your roaming profile is not synchronized correctly with the server. Windows will load your previously-saved local profile instead. See the previous events for details.\r\n
0x00000605 | Failed to apply CSC suspend policy. Cannot connect to CSC service.%n DETAIL - %1\r\n
0x00000606 | Windows cannot load classes registry file.%n DETAIL - %1\r\n
0x00000607 | A slow network connection is detected for the roaming profile %1. It will not be synchronized with the profile on this computer.\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-User Profile Service\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-User Profile Service/Operational\r\n
0xb0000001 | Recieved user logon notification on session %1.\r\n
0xb0000002 | Finished processing user logon notification on session %1.\r\n
0xb0000003 | Recieved user logoff notification on session %1.\r\n
0xb0000004 | Finished processing user logoff notification on session %1.\r\n
0xb0000005 | Registry file %1 is loaded at HKU\%2.\r\n
0xb0000006 | Starting synchronize profile from %1 to %2.\r\n
0xb0000007 | Finished synchronize profile from %1 to %2. %n%nResult: %3\r\n
0xb0000032 | Background hive upload for user %1 started.\r\n
0xb0000033 | Background hive upload for user %1 succeeded.\r\n
0xb0000034 | Background hive upload for user %1 failed.%n%n Error: %2\r\n
0xb0000035 | Cannot delete file %1.%n%n Error: %2\r\n
0xb0000036 | Open user regisry root key for %1 failed.%n%n Error: %2\r\n
0xb0000037 | Save user hive to file %1 failed.%n%n Error: %2\r\n
0xb0000038 | Save user hive to file %1 succeeded.\r\n
0xb0000039 | Enable background user hive upload task succeeded.\r\n
0xb000003a | Failed to enable background user hive upload task.%n%n Error: %1\r\n
0xb000003b | Disable background user hive upload task succeeded.\r\n
0xb000003c | Failed to disable background user hive upload task.%n%n Error: %1\r\n
0xb000003d | Slow network connection detected, abort background user hive upload task.\r\n
0xb000003e | Windows was unable to successfully evaluate whether this computer is a primary computer for this user. This may be due to failing to access the Active Directory server at this time. The user's roaming profile will be applied as configured. Contact the Administrator for more assistance. Error: %1\r\n
0xb000003f | This computer %1 a primary computer for this user.\r\n
0xb0000040 | The primary computer relationship for this computer and this user was not evaluated due to %1.\r\n
0xb0000041 | The attempt to create or open the profile key for the user failed with error %1.\r\n
0xb0000042 | Creating the local profile for the user failed with error %1.\r\n
0xb0000043 | Logon type: %1 %nLocal profile location: %2 %nProfile type: %3\r\n
0xb0000044 | LastDownloadTime: %1 %nLastUploadTime: %2\r\n
0xb0000046 | Waiting on network arrivals. Max wait time %1 ms.\r\n
0xb0000047 | After waiting %1 ms, a network with the necessary capabilities was not ready for use. Allowing profile load to proceed.\r\n
0xb0000048 | Terminating wait due to unexpected failure %1.\r\n
0xb0000049 | Wait complete due to connectivity event but network not ready.\r\n
0xb000004a | Wait completed due to network connectivity or determination that no viable network connection is likely to become available. Allowing profile load to proceed.\r\n
0xb000004b | Roaming Profiles configuration is being controlled by Group Policy.\r\n
0xb000004c | Roaming Profiles configuration is being controlled by WMI configuration classes Win32_RoamingProfileUserConfiguration and Win32_RoamingProfileMachineConfiguration.\r\n
0xb00003e9 | Begin new user profile creation.\r\n
0xb00003ea | New user profile creation complete.\r\n
0xb00003eb | A network latency of %1 milliseconds has been detected.  Maximum latency to synchronize a roaming profile is set at %2 milliseconds.\r\n
0xb00003ec | A network bandwidth of %1 kilobits per second has been detected.  Minimum bandwidth to synchronize a roaming profile is set at %2 kilobits per second.\r\n
0xb00003ed | Delete cached profile %1 since it is older than %2 days.\r\n

### 6.3.9600.17031, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x000005dc | Windows cannot log you on because your profile cannot be loaded. Check that you are connected to the network, and that your network is functioning correctly. %n%n DETAIL - %1\r\n
0x000005dd | Windows cannot create a temporary profile directory. This problem may be caused by insufficient security rights. %n%n DETAIL - %1\r\n
0x000005de | Windows cannot load the locally stored profile. Possible causes of this error include insufficient security rights or a corrupt local profile. %n%n DETAIL - %1\r\n
0x000005df | Windows cannot set security on your registry. %n%n DETAIL - %1\r\n
0x000005e0 | Windows cannot update your roaming profile completely. Check previous events for more details. %n%n\r\n
0x000005e1 | Windows cannot load the user's profile but has logged you on with the default profile for the system. %n%n DETAIL - %1\r\n
0x000005e2 | Your roaming profile is not available. You are logged on with the locally stored profile. Changes to the profile will not be copied to the server. Possible causes of this error include network problems or insufficient security rights.  %n%n DETAIL - %1\r\n
0x000005e4 | Windows was unable to load the registry. This problem is often caused by insufficient memory or insufficient security rights. %n%n DETAIL - %1 for %2\r\n
0x000005e5 | Windows was unable to load %1.\r\n
0x000005e6 | Windows cannot load your profile because it appears to be corrupted.\r\n
0x000005e7 | Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.\r\n
0x000005e8 | Windows cannot unload your registry file. The memory used by the registry has not been freed. This problem is often caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account. %n%n DETAIL - %1\r\n
0x000005e9 | Windows cannot copy your profile because it contains encrypted files or directories. The keys to decrypt the files or directories are also stored in the profile and are not available now. Decrypt the files and try again.\r\n
0x000005ea | The roaming profile path %1 is too long. Windows is logging you on with a default profile.\r\n
0x000005eb | Windows has backed up this user profile. Windows will automatically try to use the backup profile the next time this user logs on.\r\n
0x000005ed | Windows saved user %1 registry while an application or service was still using the registry when the user logged off. The memory used by the user registry has not been freed. The registry will be unloaded when it is no longer in use. %n%n This error may be caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account.\r\n
0x000005ee | Windows cannot create a local profile and is logging you on with a temporary profile. This profile will be deleted when you log off. This problem may be caused by incorrect file system permissions or network problems.\r\n
0x000005ef | Windows cannot locate your roaming mandatory profile and is attempting to log you on with your local profile. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f0 | Windows cannot log you on because your roaming mandatory profile is not available. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f1 | Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f2 | Windows cannot locate your roaming profile (read only) and is attempting to log you on with your local profile. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f3 | Your roaming profile (read only) is not available. You are logged on with the locally stored profile. This error may be caused by incorrect file system permissions or network problems.  %n%n DETAIL - %1\r\n
0x000005f4 | Windows cannot unload your classes registry file - it is still in use by other applications or services. The file will be unloaded when it is no longer in use.  %n%n\r\n
0x000005f5 | Windows has detected that Automatic Offline Caching is enabled on the Roaming Profile share - to avoid potential profile corruption, Offline Caching must be set to manual or disabled on shares where roaming user profiles are stored. %n%n\r\n
0x000005f6 | Windows could not load your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. Windows could not load your profile because a server copy of the profile folder already exists that does not have the correct security. Either the current user or the Administrators group must be the owner of the folder. %n%n\r\n
0x000005f7 | Windows failed to initialize user profiles. Non-console users will be unable to log on.\r\n
0x000005f9 | Roaming user profiles across forests are disabled. Windows did not load your roaming profile and is logging you on with a local profile. Changes to the profile will not be copied to the server when you log off.\r\n
0x000005fa | Windows detected your registry file is still in use by other applications or services. The file will be unloaded now. The applications or services that hold your registry file may not function properly afterwards. No user action is required.  %n%n DETAIL - %n %1\r\n
0x000005fb | The User Profile Service has started successfully.  %n%n\r\n
0x000005fc | The User Profile Service has stopped.  %n%n\r\n
0x000005fd | Windows cannot delete the profile directory %1. This error may be caused by files in this directory being used by another program. %n%n DETAIL - %2\r\n
0x000005fe | Profile notification of event %1 for component %2 failed, error code is %3. %n%n\r\n
0x000005ff | Successfully suspended folder "%1"\r\n
0x00000600 | Successfully unsuspended folder "%1"\r\n
0x00000601 | Failed to suspend folder "%1"%n DETAIL - %2\r\n
0x00000602 | Failed to unsuspend folder "%1"%n DETAIL - %2\r\n
0x00000603 | Failed to sync folder "%1"%n DETAIL - %2\r\n
0x00000604 | Your roaming profile is not synchronized correctly with the server. Windows will load your previously-saved local profile instead. See the previous events for details.\r\n
0x00000605 | Failed to apply CSC suspend policy. Cannot connect to CSC service.%n DETAIL - %1\r\n
0x00000606 | Windows cannot load classes registry file.%n DETAIL - %1\r\n
0x00000607 | A slow network connection is detected for the roaming profile %1. It will not be synchronized with the profile on this computer.\r\n
0x00000608 | Windows cannot back up a ProfileList entry because one already exists for this user. Only the existing backup entry will be kept in the ProfileList. Future logons will restore the ProfileList entry from the existing backup entry.\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-User Profile Service\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-User Profile Service/Operational\r\n
0xb0000001 | Recieved user logon notification on session %1.\r\n
0xb0000002 | Finished processing user logon notification on session %1.\r\n
0xb0000003 | Recieved user logoff notification on session %1.\r\n
0xb0000004 | Finished processing user logoff notification on session %1.\r\n
0xb0000005 | Registry file %1 is loaded at HKU\%2.\r\n
0xb0000006 | Starting synchronize profile from %1 to %2.\r\n
0xb0000007 | Finished synchronize profile from %1 to %2. %n%nResult: %3\r\n
0xb0000032 | Background hive upload for user %1 started.\r\n
0xb0000033 | Background hive upload for user %1 succeeded.\r\n
0xb0000034 | Background hive upload for user %1 failed.%n%n Error: %2\r\n
0xb0000035 | Cannot delete file %1.%n%n Error: %2\r\n
0xb0000036 | Open user regisry root key for %1 failed.%n%n Error: %2\r\n
0xb0000037 | Save user hive to file %1 failed.%n%n Error: %2\r\n
0xb0000038 | Save user hive to file %1 succeeded.\r\n
0xb0000039 | Enable background user hive upload task succeeded.\r\n
0xb000003a | Failed to enable background user hive upload task.%n%n Error: %1\r\n
0xb000003b | Disable background user hive upload task succeeded.\r\n
0xb000003c | Failed to disable background user hive upload task.%n%n Error: %1\r\n
0xb000003d | Slow network connection detected, abort background user hive upload task.\r\n
0xb000003e | Windows was unable to successfully evaluate whether this computer is a primary computer for this user. This may be due to failing to access the Active Directory server at this time. The user's roaming profile will be applied as configured. Contact the Administrator for more assistance. Error: %1\r\n
0xb000003f | This computer %1 a primary computer for this user.\r\n
0xb0000040 | The primary computer relationship for this computer and this user was not evaluated due to %1.\r\n
0xb0000041 | The attempt to create or open the profile key for the user failed with error %1.\r\n
0xb0000042 | Creating the local profile for the user failed with error %1.\r\n
0xb0000043 | Logon type: %1 %nLocal profile location: %2 %nProfile type: %3\r\n
0xb0000044 | LastDownloadTime: %1 %nLastUploadTime: %2\r\n
0xb0000046 | Waiting on network arrivals. Max wait time %1 ms.\r\n
0xb0000047 | After waiting %1 ms, a network with the necessary capabilities was not ready for use. Allowing profile load to proceed.\r\n
0xb0000048 | Terminating wait due to unexpected failure %1.\r\n
0xb0000049 | Wait complete due to connectivity event but network not ready.\r\n
0xb000004a | Wait completed due to network connectivity or determination that no viable network connection is likely to become available. Allowing profile load to proceed.\r\n
0xb000004b | Roaming Profiles configuration is being controlled by Group Policy.\r\n
0xb000004c | Roaming Profiles configuration is being controlled by WMI configuration classes Win32_RoamingProfileUserConfiguration and Win32_RoamingProfileMachineConfiguration.\r\n
0xb00003e9 | Begin new user profile creation.\r\n
0xb00003ea | New user profile creation complete.\r\n
0xb00003eb | A network latency of %1 milliseconds has been detected.  Maximum latency to synchronize a roaming profile is set at %2 milliseconds.\r\n
0xb00003ec | A network bandwidth of %1 kilobits per second has been detected.  Minimum bandwidth to synchronize a roaming profile is set at %2 kilobits per second.\r\n
0xb00003ed | Delete cached profile %1 since it is older than %2 days.\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x000005dc | Windows cannot log you on because your profile cannot be loaded. Check that you are connected to the network, and that your network is functioning correctly. %n%n DETAIL - %1\r\n
0x000005dd | Windows cannot create a temporary profile directory. This problem may be caused by insufficient security rights. %n%n DETAIL - %1\r\n
0x000005de | Windows cannot load the locally stored profile. Possible causes of this error include insufficient security rights or a corrupt local profile. %n%n DETAIL - %1\r\n
0x000005df | Windows cannot set security on your registry. %n%n DETAIL - %1\r\n
0x000005e0 | Windows cannot update your roaming profile completely. Check previous events for more details. %n%n\r\n
0x000005e1 | Windows cannot load the user's profile but has logged you on with the default profile for the system. %n%n DETAIL - %1\r\n
0x000005e2 | Your roaming profile is not available. You are logged on with the locally stored profile. Changes to the profile will not be copied to the server. Possible causes of this error include network problems or insufficient security rights.  %n%n DETAIL - %1\r\n
0x000005e4 | Windows was unable to load the registry. This problem is often caused by insufficient memory or insufficient security rights. %n%n DETAIL - %1 for %2\r\n
0x000005e5 | Windows was unable to load %1.\r\n
0x000005e6 | Windows cannot load your profile because it appears to be corrupted.\r\n
0x000005e7 | Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.\r\n
0x000005e8 | Windows cannot unload your registry file. The memory used by the registry has not been freed. This problem is often caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account. %n%n DETAIL - %1\r\n
0x000005e9 | Windows cannot copy your profile because it contains encrypted files or directories. The keys to decrypt the files or directories are also stored in the profile and are not available now. Decrypt the files and try again.\r\n
0x000005ea | The roaming profile path %1 is too long. Windows is logging you on with a default profile.\r\n
0x000005eb | Windows has backed up this user profile. Windows will automatically try to use the backup profile the next time this user logs on.\r\n
0x000005ed | Windows saved user %1 registry while an application or service was still using the registry when the user logged off. The memory used by the user registry has not been freed. The registry will be unloaded when it is no longer in use. %n%n This error may be caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account.\r\n
0x000005ee | Windows cannot create a local profile and is logging you on with a temporary profile. This profile will be deleted when you log off. This problem may be caused by incorrect file system permissions or network problems.\r\n
0x000005ef | Windows cannot locate your roaming mandatory profile and is attempting to log you on with your local profile. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f0 | Windows cannot log you on because your roaming mandatory profile is not available. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f1 | Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f2 | Windows cannot locate your roaming profile (read only) and is attempting to log you on with your local profile. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f3 | Your roaming profile (read only) is not available. You are logged on with the locally stored profile. This error may be caused by incorrect file system permissions or network problems.  %n%n DETAIL - %1\r\n
0x000005f4 | Windows cannot unload your classes registry file - it is still in use by other applications or services. The file will be unloaded when it is no longer in use.  %n%n\r\n
0x000005f5 | Windows has detected that Automatic Offline Caching is enabled on the Roaming Profile share - to avoid potential profile corruption, Offline Caching must be set to manual or disabled on shares where roaming user profiles are stored. %n%n\r\n
0x000005f6 | Windows could not load your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. Windows could not load your profile because a server copy of the profile folder already exists that does not have the correct security. Either the current user or the Administrators group must be the owner of the folder. %n%n\r\n
0x000005f7 | Windows failed to initialize user profiles. Non-console users will be unable to log on.\r\n
0x000005f9 | Roaming user profiles across forests are disabled. Windows did not load your roaming profile and is logging you on with a local profile. Changes to the profile will not be copied to the server when you log off.\r\n
0x000005fa | Windows detected your registry file is still in use by other applications or services. The file will be unloaded now. The applications or services that hold your registry file may not function properly afterwards. No user action is required.  %n%n DETAIL - %n %1\r\n
0x000005fb | The User Profile Service has started successfully.  %n%n\r\n
0x000005fc | The User Profile Service has stopped.  %n%n\r\n
0x000005fd | Windows cannot delete the profile directory %1. This error may be caused by files in this directory being used by another program. %n%n DETAIL - %2\r\n
0x000005fe | Profile notification of event %1 for component %2 failed, error code is %3. %n%n\r\n
0x000005ff | Successfully suspended folder "%1"\r\n
0x00000600 | Successfully unsuspended folder "%1"\r\n
0x00000601 | Failed to suspend folder "%1"%n DETAIL - %2\r\n
0x00000602 | Failed to unsuspend folder "%1"%n DETAIL - %2\r\n
0x00000603 | Failed to sync folder "%1"%n DETAIL - %2\r\n
0x00000604 | Your roaming profile is not synchronized correctly with the server. Windows will load your previously-saved local profile instead. See the previous events for details.\r\n
0x00000605 | Failed to apply CSC suspend policy. Cannot connect to CSC service.%n DETAIL - %1\r\n
0x00000606 | Windows cannot load classes registry file.%n DETAIL - %1\r\n
0x00000607 | A slow network connection is detected for the roaming profile %1. It will not be synchronized with the profile on this computer.\r\n
0x00000608 | Windows cannot back up a ProfileList entry because one already exists for this user. Only the existing backup entry will be kept in the ProfileList. Future logons will restore the ProfileList entry from the existing backup entry.\r\n
0x00000609 | User hive is loaded by another process. Process name: %1, PID: %2, ProfSvc PID: %3.\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-User Profile Service\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-User Profile Service/Operational\r\n
0xb0000001 | Recieved user logon notification on session %1.\r\n
0xb0000002 | Finished processing user logon notification on session %1.\r\n
0xb0000003 | Recieved user logoff notification on session %1.\r\n
0xb0000004 | Finished processing user logoff notification on session %1.\r\n
0xb0000005 | Registry file %1 is loaded at HKU\%2.\r\n
0xb0000006 | Starting synchronize profile from %1 to %2.\r\n
0xb0000007 | Finished synchronize profile from %1 to %2. %n%nResult: %3\r\n
0xb0000032 | Background hive upload for user %1 started.\r\n
0xb0000033 | Background hive upload for user %1 succeeded.\r\n
0xb0000034 | Background hive upload for user %1 failed.%n%n Error: %2\r\n
0xb0000035 | Cannot delete file %1.%n%n Error: %2\r\n
0xb0000036 | Open user regisry root key for %1 failed.%n%n Error: %2\r\n
0xb0000037 | Save user hive to file %1 failed.%n%n Error: %2\r\n
0xb0000038 | Save user hive to file %1 succeeded.\r\n
0xb0000039 | Enable background user hive upload task succeeded.\r\n
0xb000003a | Failed to enable background user hive upload task.%n%n Error: %1\r\n
0xb000003b | Disable background user hive upload task succeeded.\r\n
0xb000003c | Failed to disable background user hive upload task.%n%n Error: %1\r\n
0xb000003d | Slow network connection detected, abort background user hive upload task.\r\n
0xb000003e | Windows was unable to successfully evaluate whether this computer is a primary computer for this user. This may be due to failing to access the Active Directory server at this time. The user's roaming profile will be applied as configured. Contact the Administrator for more assistance. Error: %1\r\n
0xb000003f | This computer %1 a primary computer for this user.\r\n
0xb0000040 | The primary computer relationship for this computer and this user was not evaluated due to %1.\r\n
0xb0000041 | The attempt to create or open the profile key for the user failed with error %1.\r\n
0xb0000042 | Creating the local profile for the user failed with error %1.\r\n
0xb0000043 | Logon type: %1 %nLocal profile location: %2 %nProfile type: %3\r\n
0xb0000044 | LastDownloadTime: %1 %nLastUploadTime: %2\r\n
0xb0000046 | Waiting on network arrivals. Max wait time %1 ms.\r\n
0xb0000047 | After waiting %1 ms, a network with the necessary capabilities was not ready for use. Allowing profile load to proceed.\r\n
0xb0000048 | Terminating wait due to unexpected failure %1.\r\n
0xb0000049 | Wait complete due to connectivity event but network not ready.\r\n
0xb000004a | Wait completed due to network connectivity or determination that no viable network connection is likely to become available. Allowing profile load to proceed.\r\n
0xb000004b | Roaming Profiles configuration is being controlled by Group Policy.\r\n
0xb000004c | Roaming Profiles configuration is being controlled by WMI configuration classes Win32_RoamingProfileUserConfiguration and Win32_RoamingProfileMachineConfiguration.\r\n
0xb00003e9 | Begin new user profile creation.\r\n
0xb00003ea | New user profile creation complete.\r\n
0xb00003eb | A network latency of %1 milliseconds has been detected.  Maximum latency to synchronize a roaming profile is set at %2 milliseconds.\r\n
0xb00003ec | A network bandwidth of %1 kilobits per second has been detected.  Minimum bandwidth to synchronize a roaming profile is set at %2 kilobits per second.\r\n
0xb00003ed | Delete cached profile %1 since it is older than %2 days.\r\n

### 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x000005dc | Windows cannot log you on because your profile cannot be loaded. Check that you are connected to the network, and that your network is functioning correctly. %n%n DETAIL - %1\r\n
0x000005dd | Windows cannot create a temporary profile directory. This problem may be caused by insufficient security rights. %n%n DETAIL - %1\r\n
0x000005de | Windows cannot load the locally stored profile. Possible causes of this error include insufficient security rights or a corrupt local profile. %n%n DETAIL - %1\r\n
0x000005df | Windows cannot set security on your registry. %n%n DETAIL - %1\r\n
0x000005e0 | Windows cannot update your roaming profile completely. Check previous events for more details. %n%n\r\n
0x000005e1 | Windows cannot load the user's profile but has logged you on with the default profile for the system. %n%n DETAIL - %1\r\n
0x000005e2 | Your roaming profile is not available. You are logged on with the locally stored profile. Changes to the profile will not be copied to the server. Possible causes of this error include network problems or insufficient security rights.  %n%n DETAIL - %1\r\n
0x000005e4 | Windows was unable to load the registry. This problem is often caused by insufficient memory or insufficient security rights. %n%n DETAIL - %1 for %2\r\n
0x000005e5 | Windows was unable to load %1.\r\n
0x000005e6 | Windows cannot load your profile because it appears to be corrupted.\r\n
0x000005e7 | Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.\r\n
0x000005e8 | Windows cannot unload your registry file. The memory used by the registry has not been freed. This problem is often caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account. %n%n DETAIL - %1\r\n
0x000005e9 | Windows cannot copy your profile because it contains encrypted files or directories. The keys to decrypt the files or directories are also stored in the profile and are not available now. Decrypt the files and try again.\r\n
0x000005ea | The roaming profile path %1 is too long. Windows is logging you on with a default profile.\r\n
0x000005eb | Windows has backed up this user profile. Windows will automatically try to use the backup profile the next time this user logs on.\r\n
0x000005ed | Windows saved user %1 registry while an application or service was still using the registry when the user logged off. The memory used by the user registry has not been freed. The registry will be unloaded when it is no longer in use. %n%n This error may be caused by services running as a user account. Try configuring services to run in either the LocalService or NetworkService account.\r\n
0x000005ee | Windows cannot create a local profile and is logging you on with a temporary profile. This profile will be deleted when you log off. This problem may be caused by incorrect file system permissions or network problems.\r\n
0x000005ef | Windows cannot locate your roaming mandatory profile and is attempting to log you on with your local profile. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f0 | Windows cannot log you on because your roaming mandatory profile is not available. This error may be caused by incorrect file system permissions or network problems. %n%n DETAIL - %1\r\n
0x000005f1 | Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f2 | Windows cannot locate your roaming profile (read only) and is attempting to log you on with your local profile. This error may be caused by network problems or insufficient security rights. %n%n DETAIL - %1\r\n
0x000005f3 | Your roaming profile (read only) is not available. You are logged on with the locally stored profile. This error may be caused by incorrect file system permissions or network problems.  %n%n DETAIL - %1\r\n
0x000005f4 | Windows cannot unload your classes registry file - it is still in use by other applications or services. The file will be unloaded when it is no longer in use.  %n%n\r\n
0x000005f5 | Windows has detected that Automatic Offline Caching is enabled on the Roaming Profile share - to avoid potential profile corruption, Offline Caching must be set to manual or disabled on shares where roaming user profiles are stored. %n%n\r\n
0x000005f6 | Windows could not load your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. Windows could not load your profile because a server copy of the profile folder already exists that does not have the correct security. Either the current user or the Administrators group must be the owner of the folder. %n%n\r\n
0x000005f7 | Windows failed to initialize user profiles. Non-console users will be unable to log on.\r\n
0x000005f9 | Roaming user profiles across forests are disabled. Windows did not load your roaming profile and is logging you on with a local profile. Changes to the profile will not be copied to the server when you log off.\r\n
0x000005fa | Windows detected your registry file is still in use by other applications or services. The file will be unloaded now. The applications or services that hold your registry file may not function properly afterwards. No user action is required.  %n%n DETAIL - %n %1\r\n
0x000005fb | The User Profile Service has started successfully.  %n%n\r\n
0x000005fc | The User Profile Service has stopped.  %n%n\r\n
0x000005fd | Windows cannot delete the profile directory %1. This error may be caused by files in this directory being used by another program. %n%n DETAIL - %2\r\n
0x000005fe | Profile notification of event %1 for component %2 failed, error code is %3. %n%n\r\n
0x000005ff | Successfully suspended folder "%1"\r\n
0x00000600 | Successfully unsuspended folder "%1"\r\n
0x00000601 | Failed to suspend folder "%1"%n DETAIL - %2\r\n
0x00000602 | Failed to unsuspend folder "%1"%n DETAIL - %2\r\n
0x00000603 | Failed to sync folder "%1"%n DETAIL - %2\r\n
0x00000604 | Your roaming profile is not synchronized correctly with the server. Windows will load your previously-saved local profile instead. See the previous events for details.\r\n
0x00000605 | Failed to apply CSC suspend policy. Cannot connect to CSC service.%n DETAIL - %1\r\n
0x00000606 | Windows cannot load classes registry file.%n DETAIL - %1\r\n
0x00000607 | A slow network connection is detected for the roaming profile %1. It will not be synchronized with the profile on this computer.\r\n
0x00000608 | Windows cannot back up a ProfileList entry because one already exists for this user. Only the existing backup entry will be kept in the ProfileList. Future logons will restore the ProfileList entry from the existing backup entry.\r\n
0x00000609 | User hive is loaded by another process (File Lock). Process name: %1, PID: %2, ProfSvc PID: %3.\r\n
0x00000610 | User hive is loaded by another process (Registry Lock) Process name: %1, PID: %2, ProfSvc PID: %3.\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-User Profile Service\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-User Profile Service/Operational\r\n
0xb0000001 | Recieved user logon notification on session %1.\r\n
0xb0000002 | Finished processing user logon notification on session %1.\r\n
0xb0000003 | Recieved user logoff notification on session %1.\r\n
0xb0000004 | Finished processing user logoff notification on session %1.\r\n
0xb0000005 | Registry file %1 is loaded at HKU\%2.\r\n
0xb0000006 | Starting synchronize profile from %1 to %2.\r\n
0xb0000007 | Finished synchronize profile from %1 to %2. %n%nResult: %3\r\n
0xb0000032 | Background hive upload for user %1 started.\r\n
0xb0000033 | Background hive upload for user %1 succeeded.\r\n
0xb0000034 | Background hive upload for user %1 failed.%n%n Error: %2\r\n
0xb0000035 | Cannot delete file %1.%n%n Error: %2\r\n
0xb0000036 | Open user regisry root key for %1 failed.%n%n Error: %2\r\n
0xb0000037 | Save user hive to file %1 failed.%n%n Error: %2\r\n
0xb0000038 | Save user hive to file %1 succeeded.\r\n
0xb0000039 | Enable background user hive upload task succeeded.\r\n
0xb000003a | Failed to enable background user hive upload task.%n%n Error: %1\r\n
0xb000003b | Disable background user hive upload task succeeded.\r\n
0xb000003c | Failed to disable background user hive upload task.%n%n Error: %1\r\n
0xb000003d | Slow network connection detected, abort background user hive upload task.\r\n
0xb000003e | Windows was unable to successfully evaluate whether this computer is a primary computer for this user. This may be due to failing to access the Active Directory server at this time. The user's roaming profile will be applied as configured. Contact the Administrator for more assistance. Error: %1\r\n
0xb000003f | This computer %1 a primary computer for this user.\r\n
0xb0000040 | The primary computer relationship for this computer and this user was not evaluated due to %1.\r\n
0xb0000041 | The attempt to create or open the profile key for the user failed with error %1.\r\n
0xb0000042 | Creating the local profile for the user failed with error %1.\r\n
0xb0000043 | Logon type: %1 %nLocal profile location: %2 %nProfile type: %3\r\n
0xb0000044 | LastDownloadTime: %1 %nLastUploadTime: %2\r\n
0xb0000046 | Waiting on network arrivals. Max wait time %1 ms.\r\n
0xb0000047 | After waiting %1 ms, a network with the necessary capabilities was not ready for use. Allowing profile load to proceed.\r\n
0xb0000048 | Terminating wait due to unexpected failure %1.\r\n
0xb0000049 | Wait complete due to connectivity event but network not ready.\r\n
0xb000004a | Wait completed due to network connectivity or determination that no viable network connection is likely to become available. Allowing profile load to proceed.\r\n
0xb000004b | Roaming Profiles configuration is being controlled by Group Policy.\r\n
0xb000004c | Roaming Profiles configuration is being controlled by WMI configuration classes Win32_RoamingProfileUserConfiguration and Win32_RoamingProfileMachineConfiguration.\r\n
0xb00003e9 | Begin new user profile creation.\r\n
0xb00003ea | New user profile creation complete.\r\n
0xb00003eb | A network latency of %1 milliseconds has been detected.  Maximum latency to synchronize a roaming profile is set at %2 milliseconds.\r\n
0xb00003ec | A network bandwidth of %1 kilobits per second has been detected.  Minimum bandwidth to synchronize a roaming profile is set at %2 kilobits per second.\r\n
0xb00003ed | Delete cached profile %1 since it is older than %2 days.\r\n
