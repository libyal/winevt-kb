## workfolderssvc.dll

Path: %SystemRoot%\system32\WorkFoldersSvc.dll

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | SyncPartnership\r\n
0x90000001 | Microsoft-Windows-WorkFolders\r\n
0x90000002 | Operational\r\n
0x90000003 | Debug\r\n
0x90000004 | Analytic\r\n
0x90000005 | ManagementAgent\r\n
0xb0000000 | The Windows Work Folders service is running.\r\n
0xb0000001 | The Windows Work Folders service is stopping.\r\n
0xb0000002 | A sync partnership was created between %1 and %2 (%3).\r\n
0xb0000003 | A sync partnership between %1 and %2 (%3) was deleted.\r\n
0xb0000004 | Resuming sync between %1 and %2 (%3).\r\n
0xb0000005 | Attempting to apply the following Work Folders Group Policy configuration:%nWork Folders URL: %1%nForce automatic setup: %2\r\n
0xb0000006 | Attempting to remove the following Work Folders Group Policy configuration:%nDiscovery URL: %1 %nServer URL: %2\r\n
0xb0000007 | Configuring Work Folders through Group Policy with the following options:%nPartnership ID: %1%nPartnership type: %2%nDiscovery URL: %3%nServer URL: %4\r\n
0xb0000008 | Configuration of Work Folders through Group Policy succeeded.\r\n
0xb0000009 | While applying Work Folders configuration through Group Policy, an existing Work Folders configuration was found. %nDiscovery URL: %1 %nServer URL: %2%nConfigured by policy: %3\r\n
0xb000000a | Configuration of Work Folders through Group Policy failed. %nError: %1.\r\n
0xb000000b | There was a problem removing the Work Folders configuration when applying Group Policy. %nError: %1\r\n
0xb000000c | There was a problem communicating with the Windows Work Folders service. Confirm that this service is running. %nError: %1\r\n
0xb000000d | There was a problem retrieving your Work Folders Group Policy configuration. %nError: %1\r\n
0xb000000e | There was a problem retrieving your current Work Folders configuration. %nError: %1.\r\n
0xb000000f | There was a problem comparing the existing Work Folders configuration to the configuration being applied by Group Policy. %nError: %1.\r\n
0xb0000010 | Server discovery on %1 found server %2.\r\n
0xb0000011 | Sync Share discovery succeeded. Server URL: %1; Partnership type: %2; Server partnership id: %3\r\n
0xb0000012 | The discovery URL was found from the user's email address. User's email address: %1; Discovery URL %2\r\n
0xb0000013 | This PC is incompatible with the Work Folders server and must be upgraded. Please contact your administrator for instructions on upgrading your PC.\r\n
0xb00001f6 | A sync partnership between %1 and %2 (%3) failed to create with %4.\r\n
0xb00001f7 | A sync partnership between %1 and %2 (%3) failed to delete with %4.\r\n
0xb0000204 | Server discovery on %1 failed with %2.\r\n
0xb0000205 | Sync Share discovery failed. Server URL: %1; Partnership type: %2; Error: %3\r\n
0xb0000206 | Searching for a discovery URL from the user's email address failed. User's email address: %1; Error: %2\r\n
0xb00003e8 | Some files cannot be downloaded. Make sure the drive for %1 has at least %2 MB free.\r\n
0xb00003e9 | Failed to get an ADFS access token from the server. User: %1. ADFS URI: %2. Error: %3\r\n
0xb00003ea | Failed to get an ADFS refresh token from the server. User: %1. ADFS URI: %2. Error: %3\r\n
0xb000044c | Work Folders sucessfully uploaded a file. File name:%1; Sync ID: %2\r\n
0xb000044d | Work Folders failed to upload a file. File name:%1; Sync ID: %2; Error: %3\r\n
0xb000044e | Work Folders sucessfully downloaded a file. File name:%1; Sync ID: %2\r\n
0xb000044f | Work Folders failed to download a file. File name:%1; Sync ID: %2; Error: %3\r\n
0xb0000450 | Work Folders sucessfully uploaded a change batch. Partnership ID:%1\r\n
0xb0000451 | Work Folders failed to upload a change batch. Partnership ID:%1; Error: %2\r\n
0xb0000452 | Work Folders sucessfully downloaded a change batch. Partnership ID:%1\r\n
0xb0000453 | Work Folders failed to download a change batch. Partnership ID:%1; Error: %2\r\n
0xb00007d0 | Work Folders couldn't detect changed files using the USN change journal, so it's scanning all files for changes. No action is required. Path: %1\r\n
0xb00007d1 | Sync started. URI: %1\r\n
0xb00007d2 | Sync completed.  URI: %1\r\n
0xb00007d3 | Sync batch upload completed.%n%nUploaded %1 file(s) (%2 bytes).%nFailed %3 file(s) (%4 bytes).%nElapsed time: %5 seconds.%nRate: %6 KBps.\r\n
0xb00007d4 | Sync batch download completed.%n%nDownloaded %1 file(s) (%2 bytes).%nFailed %3 file(s).%nElapsed time: %5 seconds.%nRate: %6 KBps.\r\n
0xb00007d5 | HTTP request failure.%n%nURI: %1 %nVerb: %2 %nHeaders: %3 %nBody Length: %4 %nHTTP Response: %5 %nServer HRESULT: %6\r\n
0xb00007d6 | Work Folders skipped uploading a file because of an error. Sync ID: %1; Error: %2\r\n
0xb00007d7 | Work Folders will skip downloading files because the user doesn't have enough free space on the drive where Work Folders is located. User: %1\r\n
0xb00007d8 | Couldn't authenticate the user. User: %1\r\n
0xb00007d9 | Work Folders successfully synchronized an item. Item: %1; Sync ID: %2; Sync action: %3\r\n
0xb00007db | Work Folders successfully updated the current state of an item. Item: %1; Sync ID: %2; Update action: %3\r\n
0xb00007dd | Work Folders detected a conflict on an item and decided a conflict resolution. Concurrency conflict: %1; Source item name: %2; Source sync ID: %3; Destination item name: %4; Destination sync ID: %5; Data winner: %6; Namespace winner: %7; Attributes winner: %8; Tie breaker winner: %9\r\n
0xb0000834 | Sync failed. Work Folders path: %1; Error: %2\r\n
0xb0000835 | Work Folders suspended sync. Partnership: %1\r\n
0xb0000836 | Work Folders resumed syncing. Partnership: %1\r\n
0xb0000837 | Work Folders sync stopped because the Enterprise ID for this PC was remotely revoked by the issuing authority. Access to files in Work Folders is blocked on this PC. To resume syncing, in the Work Folders Control Panel, click Stop using Work Folders and then recreate the Work Folders synchronization partnership. Partnership: %1\r\n
0xb0000838 | Work Folders detected a database corruption and recovered. Database path: %1\r\n
0xb0000839 | Work Folders detected a database corruption and recovery failed. Database path: %1; Error: %2\r\n
0xb000083a | Work Folders detected that the server database has been recreated. Local epoch: %1; Server epoch: %2\r\n
0xb000083b | Work Folders detected that an error occured that requires the database to be recreated. Database path: %1; Error code: %2\r\n
0xb000083c | Work Folders synchronization metadata is stale. It will be automatically rebuild. Work Folders path: %1\r\n
0xb000083d | The Work Folders synchronization metadata was created. Work Folders path: %1\r\n
0xb000083e | The Work Folders synchronization metadata could not be created. Work Folders path: %1; Error: %2\r\n
0xb000083f | The Work Folders synchronization metadata was deleted. Work Folders path: %1\r\n
0xb0000840 | The Work Folders synchronization metadata could not be deleted. Work Folders path: %1; Error: %2\r\n
0xb0000841 | Work Folders failed to update the current state of an item. Item: %1; Sync ID: %2; Update action: %3; Error code: %4\r\n
0xb0000842 | Work Folders failed to synchronize an item. Item: %1; Sync ID: %2; Sync action: %3; Error code: %4\r\n
0xb0001f40 | Starting sync. Work Folders path: %1\r\n
0xb0001f41 | Work Folders is looking for changed files. Work Folders path: %1\r\n
0xb0001f42 | Starting to download files. Work Folders path: %1\r\n
0xb0001f43 | Starting to upload files. Work Folders path: %1\r\n
0xb0001f44 | Finished syncing. Work Folders path: %1\r\n
0xb0001f45 | Starting reconciliation sync. Work Folders path: %1\r\n
0xb0001f46 | Finished reconciliation sync. Work Folders path: %1\r\n
0xb0001f47 | Starting sync knowledge upload. Server partnership id: %1\r\n
0xb0001f48 | Starting data transfer for file download. Server partnership id: %1\r\n
0xb0001f49 | Applying downloaded files. Work Folders path: %1\r\n
0xb0001f4a | Starting sync knowledge download. Server partnership id: %1\r\n
0xb0001f4b | Creating a change batch for upload. Work Folders path: %1\r\n
0xb0001f4c | Starting data transfer for file upload. Server partnership id: %1\r\n
0xb0002329 | Credentials required for the user.\r\n
0xb000232a | Work Folders detected a sync error. Check partnership status, network connectivity, and disk space.\r\n
0xb000232b | Work Folders detected a file error. Check file sizes and types are supported.\r\n
0xb000232c | Your PC doesn't comply with your organization's security policies.\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | SyncPartnership\r\n
0x90000001 | Microsoft-Windows-WorkFolders\r\n
0x90000002 | Operational\r\n
0x90000003 | Debug\r\n
0x90000004 | Analytic\r\n
0x90000005 | ManagementAgent\r\n
0xb0000000 | The Windows Work Folders service is running.\r\n
0xb0000001 | The Windows Work Folders service is stopping.\r\n
0xb0000002 | A sync partnership was created between %1 and %2 (%3).\r\n
0xb0000003 | A sync partnership between %1 and %2 (%3) was deleted.\r\n
0xb0000004 | Resuming sync between %1 and %2 (%3).\r\n
0xb0000005 | Attempting to apply the following Work Folders Group Policy configuration:%nWork Folders URL: %1%nForce automatic setup: %2\r\n
0xb0000006 | Attempting to remove the following Work Folders Group Policy configuration:%nDiscovery URL: %1 %nServer URL: %2\r\n
0xb0000007 | Configuring Work Folders through Group Policy with the following options:%nPartnership ID: %1%nPartnership type: %2%nDiscovery URL: %3%nServer URL: %4\r\n
0xb0000008 | Configuration of Work Folders through Group Policy succeeded.\r\n
0xb0000009 | While applying Work Folders configuration through Group Policy, an existing Work Folders configuration was found. %nDiscovery URL: %1 %nServer URL: %2%nConfigured by policy: %3\r\n
0xb000000a | Configuration of Work Folders through Group Policy failed. %nError: %1.\r\n
0xb000000b | There was a problem removing the Work Folders configuration when applying Group Policy. %nError: %1\r\n
0xb000000c | There was a problem communicating with the Windows Work Folders service. Confirm that this service is running. %nError: %1\r\n
0xb000000d | There was a problem retrieving your Work Folders Group Policy configuration. %nError: %1\r\n
0xb000000e | There was a problem retrieving your current Work Folders configuration. %nError: %1.\r\n
0xb000000f | There was a problem comparing the existing Work Folders configuration to the configuration being applied by Group Policy. %nError: %1.\r\n
0xb0000010 | Server discovery on %1 found server %2.\r\n
0xb0000011 | Sync Share discovery succeeded. Server URL: %1; Partnership type: %2; Server partnership id: %3\r\n
0xb0000012 | The discovery URL was found from the user's email address. User's email address: %1; Discovery URL %2\r\n
0xb0000013 | This PC is incompatible with the Work Folders server and must be upgraded. Please contact your administrator for instructions on upgrading your PC.\r\n
0xb00001f6 | A sync partnership between %1 and %2 (%3) failed to create with %4.\r\n
0xb00001f7 | A sync partnership between %1 and %2 (%3) failed to delete with %4.\r\n
0xb0000204 | Server discovery on %1 failed with %2.\r\n
0xb0000205 | Sync Share discovery failed. Server URL: %1; Partnership type: %2; Error: %3\r\n
0xb0000206 | Searching for a discovery URL from the user's email address failed. User's email address: %1; Error: %2\r\n
0xb00003e8 | Some files cannot be downloaded. Make sure the drive for %1 has at least %2 MB free.\r\n
0xb00003e9 | Failed to get an ADFS access token from the server. User: %1. ADFS URI: %2. Error: %3\r\n
0xb00003ea | Failed to get an ADFS refresh token from the server. User: %1. ADFS URI: %2. Error: %3\r\n
0xb000044c | Work Folders sucessfully uploaded a file. File name:%1; Sync ID: %2\r\n
0xb000044d | Work Folders failed to upload a file. File name:%1; Sync ID: %2; Error: %3\r\n
0xb000044e | Work Folders sucessfully downloaded a file. File name:%1; Sync ID: %2\r\n
0xb000044f | Work Folders failed to download a file. File name:%1; Sync ID: %2; Error: %3\r\n
0xb0000450 | Work Folders sucessfully uploaded a change batch. Partnership ID:%1\r\n
0xb0000451 | Work Folders failed to upload a change batch. Partnership ID:%1; Error: %2\r\n
0xb0000452 | Work Folders sucessfully downloaded a change batch. Partnership ID:%1\r\n
0xb0000453 | Work Folders failed to download a change batch. Partnership ID:%1; Error: %2\r\n
0xb00007d0 | Work Folders couldn't detect changed files using the USN change journal, so it's scanning all files for changes. No action is required. Path: %1\r\n
0xb00007d1 | Sync started. URI: %1\r\n
0xb00007d2 | Sync completed.  URI: %1\r\n
0xb00007d3 | Sync batch upload completed.%n%nUploaded %1 file(s) (%2 bytes).%nFailed %3 file(s) (%4 bytes).%nElapsed time: %5 seconds.%nRate: %6 KBps.\r\n
0xb00007d4 | Sync batch download completed.%n%nDownloaded %1 file(s) (%2 bytes).%nFailed %3 file(s).%nElapsed time: %5 seconds.%nRate: %6 KBps.\r\n
0xb00007d5 | HTTP request failure.%n%nURI: %1 %nVerb: %2 %nHeaders: %3 %nBody Length: %4 %nHTTP Response: %5 %nServer HRESULT: %6\r\n
0xb00007d6 | Work Folders skipped uploading a file because of an error. Sync ID: %1; Error: %2\r\n
0xb00007d7 | Work Folders will skip downloading files because the user doesn't have enough free space on the drive where Work Folders is located. User: %1\r\n
0xb00007d8 | Couldn't authenticate the user. User: %1\r\n
0xb00007d9 | Work Folders successfully synchronized an item. Item: %1; Sync ID: %2; Sync action: %3\r\n
0xb00007db | Work Folders successfully updated the current state of an item. Item: %1; Sync ID: %2; Update action: %3\r\n
0xb00007dd | Work Folders detected a conflict on an item and decided a conflict resolution. Concurrency conflict: %1; Source item name: %2; Source sync ID: %3; Destination item name: %4; Destination sync ID: %5; Data winner: %6; Namespace winner: %7; Attributes winner: %8; Tie breaker winner: %9\r\n
0xb0000834 | Sync failed. Work Folders path: %1; Error: %2\r\n
0xb0000835 | Work Folders suspended sync. Partnership: %1\r\n
0xb0000836 | Work Folders resumed syncing. Partnership: %1\r\n
0xb0000837 | Work Folders sync stopped because the Enterprise ID for this PC was remotely revoked by the issuing authority. Access to files in Work Folders is blocked on this PC. To resume syncing, in the Work Folders Control Panel, click Stop using Work Folders and then recreate the Work Folders synchronization partnership. Partnership: %1\r\n
0xb0000838 | Work Folders detected a database corruption and recovered. Database path: %1\r\n
0xb0000839 | Work Folders detected a database corruption and recovery failed. Database path: %1; Error: %2\r\n
0xb000083a | Work Folders detected that the server database has been recreated. Local epoch: %1; Server epoch: %2\r\n
0xb000083b | Work Folders detected that an error occured that requires the database to be recreated. Database path: %1; Error code: %2\r\n
0xb000083c | Work Folders synchronization metadata is stale. It will be automatically rebuild. Work Folders path: %1\r\n
0xb000083d | The Work Folders synchronization metadata was created. Work Folders path: %1\r\n
0xb000083e | The Work Folders synchronization metadata could not be created. Work Folders path: %1; Error: %2\r\n
0xb000083f | The Work Folders synchronization metadata was deleted. Work Folders path: %1\r\n
0xb0000840 | The Work Folders synchronization metadata could not be deleted. Work Folders path: %1; Error: %2\r\n
0xb0000841 | Work Folders failed to update the current state of an item. Item: %1; Sync ID: %2; Update action: %3; Error code: %4\r\n
0xb0000842 | Work Folders failed to synchronize an item. Item: %1; Sync ID: %2; Sync action: %3; Error code: %4\r\n
0xb0000843 | Work Folders detected a database version that is incompatible and recovered it. Database path: %1\r\n
0xb0000844 | Work Folders detected a database version that is incompatible and recovery failed. Database path: %1; Error: %2\r\n
0xb0001f40 | Starting sync. Work Folders path: %1\r\n
0xb0001f41 | Work Folders is looking for changed files. Work Folders path: %1\r\n
0xb0001f42 | Starting to download files. Work Folders path: %1\r\n
0xb0001f43 | Starting to upload files. Work Folders path: %1\r\n
0xb0001f44 | Finished syncing. Work Folders path: %1\r\n
0xb0001f45 | Starting reconciliation sync. Work Folders path: %1\r\n
0xb0001f46 | Finished reconciliation sync. Work Folders path: %1\r\n
0xb0001f47 | Starting sync knowledge upload. Server partnership id: %1\r\n
0xb0001f48 | Starting data transfer for file download. Server partnership id: %1\r\n
0xb0001f49 | Applying downloaded files. Work Folders path: %1\r\n
0xb0001f4a | Starting sync knowledge download. Server partnership id: %1\r\n
0xb0001f4b | Creating a change batch for upload. Work Folders path: %1\r\n
0xb0001f4c | Starting data transfer for file upload. Server partnership id: %1\r\n
0xb0002329 | Credentials required for the user.\r\n
0xb000232a | Work Folders detected a sync error. Check partnership status, network connectivity, and disk space.\r\n
0xb000232b | Work Folders detected a file error. Check file sizes and types are supported.\r\n
0xb000232c | Your PC doesn't comply with your organization's security policies.\r\n

### 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | SyncPartnership\r\n
0x90000001 | Microsoft-Windows-WorkFolders\r\n
0x90000002 | Operational\r\n
0x90000003 | Debug\r\n
0x90000004 | Analytic\r\n
0x90000005 | ManagementAgent\r\n
0xb0000000 | The Windows Work Folders service is running.\r\n
0xb0000001 | The Windows Work Folders service is stopping.\r\n
0xb0000002 | A sync partnership was created between %1 and %2 (%3).\r\n
0xb0000003 | A sync partnership between %1 and %2 (%3) was deleted.\r\n
0xb0000004 | Resuming sync between %1 and %2 (%3).\r\n
0xb0000005 | Attempting to apply the following Work Folders Group Policy configuration:%nWork Folders URL: %1%nForce automatic setup: %2%nGhosting policy: %3\r\n
0xb0000006 | Attempting to remove the following Work Folders Group Policy configuration:%nDiscovery URL: %1 %nServer URL: %2%nGhosting policy: %3\r\n
0xb0000007 | Configuring Work Folders through Group Policy with the following options:%nPartnership ID: %1%nPartnership type: %2%nDiscovery URL: %3%nServer URL: %4%nGhosting policy: %5\r\n
0xb0000008 | Configuration of Work Folders through Group Policy succeeded.\r\n
0xb0000009 | While applying Work Folders configuration through Group Policy, an existing Work Folders configuration was found. %nDiscovery URL: %1 %nServer URL: %2%nConfigured by policy: %3%nGhosting policy: %4\r\n
0xb000000a | Configuration of Work Folders through Group Policy failed. %nError: %1.\r\n
0xb000000b | There was a problem removing the Work Folders configuration when applying Group Policy. %nError: %1\r\n
0xb000000c | There was a problem communicating with the Windows Work Folders service. Confirm that this service is running. %nError: %1\r\n
0xb000000d | There was a problem retrieving your Work Folders Group Policy configuration. %nError: %1\r\n
0xb000000e | There was a problem retrieving your current Work Folders configuration. %nError: %1.\r\n
0xb000000f | There was a problem comparing the existing Work Folders configuration to the configuration being applied by Group Policy. %nError: %1.\r\n
0xb0000010 | Server discovery on %1 found server %2.\r\n
0xb0000011 | Sync Share discovery succeeded. Server URL: %1; Partnership type: %2; Server partnership id: %3\r\n
0xb0000012 | The discovery URL was found from the user's email address. User's email address: %1; Discovery URL %2\r\n
0xb0000013 | This PC is incompatible with the Work Folders server and must be upgraded. Please contact your administrator for instructions on upgrading your PC.\r\n
0xb00001f6 | A sync partnership between %1 and %2 (%3) failed to create with %4.\r\n
0xb00001f7 | A sync partnership between %1 and %2 (%3) failed to delete with %4.\r\n
0xb0000204 | Server discovery on %1 failed with %2.\r\n
0xb0000205 | Sync Share discovery failed. Server URL: %1; Partnership type: %2; Error: %3\r\n
0xb0000206 | Searching for a discovery URL from the user's email address failed. User's email address: %1; Error: %2\r\n
0xb00003e8 | Some files cannot be downloaded. Make sure the drive for %1 has at least %2 MB free.\r\n
0xb00003e9 | Failed to get an ADFS access token from the server. User: %1. ADFS URI: %2. Error: %3\r\n
0xb00003ea | Failed to get an ADFS refresh token from the server. User: %1. ADFS URI: %2. Error: %3\r\n
0xb000044c | Work Folders sucessfully uploaded a file. File name:%1; Sync ID: %2\r\n
0xb000044d | Work Folders failed to upload a file. File name:%1; Sync ID: %2; Error: %3\r\n
0xb000044e | Work Folders sucessfully downloaded a file. File name:%1; Sync ID: %2\r\n
0xb000044f | Work Folders failed to download a file. File name:%1; Sync ID: %2; Error: %3\r\n
0xb0000450 | Work Folders sucessfully uploaded a change batch. Partnership ID:%1\r\n
0xb0000451 | Work Folders failed to upload a change batch. Partnership ID:%1; Error: %2\r\n
0xb0000452 | Work Folders sucessfully downloaded a change batch. Partnership ID:%1\r\n
0xb0000453 | Work Folders failed to download a change batch. Partnership ID:%1; Error: %2\r\n
0xb00007d0 | Work Folders couldn't detect changed files using the USN change journal, so it's scanning all files for changes. No action is required. Path: %1\r\n
0xb00007d1 | Sync started. URI: %1\r\n
0xb00007d2 | Sync completed.  URI: %1\r\n
0xb00007d3 | Sync batch upload completed.%n%nUploaded %1 file(s) (%2 bytes).%nFailed %3 file(s) (%4 bytes).%nElapsed time: %5 seconds.%nRate: %6 KBps.\r\n
0xb00007d4 | Sync batch download completed.%n%nDownloaded %1 file(s) (%2 bytes).%nFailed %3 file(s).%nElapsed time: %5 seconds.%nRate: %6 KBps.\r\n
0xb00007d5 | HTTP request failure.%n%nURI: %1 %nVerb: %2 %nHeaders: %3 %nBody Length: %4 %nHTTP Response: %5 %nServer HRESULT: %6\r\n
0xb00007d6 | Work Folders skipped uploading a file because of an error. Sync ID: %1; Error: %2\r\n
0xb00007d7 | Work Folders will skip downloading files because the user doesn't have enough free space on the drive where Work Folders is located. User: %1\r\n
0xb00007d8 | Couldn't authenticate the user. User: %1\r\n
0xb00007d9 | Work Folders successfully synchronized an item. Item: %1; Sync ID: %2; Sync action: %3\r\n
0xb00007db | Work Folders successfully updated the current state of an item. Item: %1; Sync ID: %2; Update action: %3\r\n
0xb00007dd | Work Folders detected a conflict on an item and decided a conflict resolution. Concurrency conflict: %1; Source item name: %2; Source sync ID: %3; Destination item name: %4; Destination sync ID: %5; Data winner: %6; Namespace winner: %7; Attributes winner: %8; Tie breaker winner: %9\r\n
0xb00007e0 | Work Folders successfully fetched file content for a file. File name: %1\r\n
0xb00007e1 | Work Folders failed to fetch file content for a file. File name: %1. Error: %2\r\n
0xb00007e2 | Work Folders cancelled fetching file content for a file. File name: %1\r\n
0xb00007e3 | Work Folders successfully removed file content from disk a file. File name: %1\r\n
0xb00007e4 | Work Folders failed to remove file content from disk a file. File name: %1. Error: %2\r\n
0xb00007e5 | Work Folders successfully repaired a broken file. File name: %1\r\n
0xb00007e6 | Work Folders failed to repair a broken file. File name: %1. Error: %2\r\n
0xb00007e7 | Work Folders could not find a broken file on the server. The broken file will be deleted. File name: %1\r\n
0xb00007e8 | The on-demand file access setting has changed. On-demand file access is now Disabled.\r\n
0xb00007e9 | The on-demand file access setting has changed. On-demand file access is now Enabled.\r\n
0xb00007ea | Work Folders successfully converted a file to enable on-demand functionality. File name: %1\r\n
0xb00007eb | Work Folders failed to convert a file to enable on-demand functionality. File name: %1. Error: %2\r\n
0xb0000834 | Sync failed. Work Folders path: %1; Error: %2\r\n
0xb0000835 | Work Folders suspended sync. Partnership: %1\r\n
0xb0000836 | Work Folders resumed syncing. Partnership: %1\r\n
0xb0000837 | Work Folders sync stopped because the Enterprise ID for this PC was remotely revoked by the issuing authority. Access to files in Work Folders is blocked on this PC. To resume syncing, in the Work Folders Control Panel, click Stop using Work Folders and then recreate the Work Folders synchronization partnership. Partnership: %1\r\n
0xb0000838 | Work Folders detected a database corruption and recovered. Database path: %1\r\n
0xb0000839 | Work Folders detected a database corruption and recovery failed. Database path: %1; Error: %2\r\n
0xb000083a | Work Folders detected that the server database has been recreated. Local epoch: %1; Server epoch: %2\r\n
0xb000083b | Work Folders detected that an error occured that requires the database to be recreated. Database path: %1; Error code: %2\r\n
0xb000083c | Work Folders synchronization metadata is stale. It will be automatically rebuild. Work Folders path: %1\r\n
0xb000083d | The Work Folders synchronization metadata was created. Work Folders path: %1\r\n
0xb000083e | The Work Folders synchronization metadata could not be created. Work Folders path: %1; Error: %2\r\n
0xb000083f | The Work Folders synchronization metadata was deleted. Work Folders path: %1\r\n
0xb0000840 | The Work Folders synchronization metadata could not be deleted. Work Folders path: %1; Error: %2\r\n
0xb0000841 | Work Folders failed to update the current state of an item. Item: %1; Sync ID: %2; Update action: %3; Error code: %4\r\n
0xb0000842 | Work Folders failed to synchronize an item. Item: %1; Sync ID: %2; Sync action: %3; Error code: %4\r\n
0xb0000843 | Work Folders detected a database version that is incompatible and recovered it. Database path: %1\r\n
0xb0000844 | Work Folders detected a database version that is incompatible and recovery failed. Database path: %1; Error: %2\r\n
0xb0000845 | Work Folders failed to connect with Cloud Files. Sync Path: %1. Error: %2\r\n
0xb0000846 | Work Folders failed to disconnect with Cloud Files. Error: %1\r\n
0xb0000847 | Work Folders failed to register with Cloud Files. Sync Path: %1. Error: %2\r\n
0xb0000848 | Work Folders failed to unregister with Cloud Files. Sync Path: %1. Error: %2\r\n
0xb0001f40 | Starting sync. Work Folders path: %1\r\n
0xb0001f41 | Work Folders is looking for changed files. Work Folders path: %1\r\n
0xb0001f42 | Starting to download files. Work Folders path: %1\r\n
0xb0001f43 | Starting to upload files. Work Folders path: %1\r\n
0xb0001f44 | Finished syncing. Work Folders path: %1\r\n
0xb0001f45 | Starting reconciliation sync. Work Folders path: %1\r\n
0xb0001f46 | Finished reconciliation sync. Work Folders path: %1\r\n
0xb0001f47 | Starting sync knowledge upload. Server partnership id: %1\r\n
0xb0001f48 | Starting data transfer for file download. Server partnership id: %1\r\n
0xb0001f49 | Applying downloaded files. Work Folders path: %1\r\n
0xb0001f4a | Starting sync knowledge download. Server partnership id: %1\r\n
0xb0001f4b | Creating a change batch for upload. Work Folders path: %1\r\n
0xb0001f4c | Starting data transfer for file upload. Server partnership id: %1\r\n
0xb0001f4d | Work Folders successfully connected with Cloud Files.\r\n
0xb0001f4e | Work Folders successfully disconnected with Cloud Files.\r\n
0xb0001f4f | Work Folders successfully registered with Cloud Files. Sync Path: %1\r\n
0xb0001f50 | Work Folders successfully unregistered with Cloud Files. Sync Path: %1.\r\n
0xb0001f51 | Work Folders detected files that cannot be uploaded. File repair started.\r\n
0xb0001f52 | Work Folders file repair completed.\r\n
0xb0001f53 | Starting cleanup before reconciliation. Work Folders path: %1\r\n
0xb0001f54 | Finished cleanup before reconciliation. Work Folders path: %1\r\n
0xb0002329 | Credentials required for the user.\r\n
0xb000232a | Work Folders detected a sync error. Check partnership status, network connectivity, and disk space.\r\n
0xb000232b | Work Folders detected a file error. Check file sizes and types are supported.\r\n
0xb000232c | Your PC doesn't comply with your organization's security policies.\r\n
