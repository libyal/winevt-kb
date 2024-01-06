## servermanager.deploymentprovider.dll

Path: %SystemRoot%\system32\wbem\ServerManager.DeploymentProvider.dll

### 6.3.9600.17041, 10.0.14393.0, 10.0.17763.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | GetServerComponentAsync method call.\r\n
0x70000002 | GetServerComponent request on a separate thread.\r\n
0x70000003 | GetEnumerationState method call.\r\n
0x70000004 | AddServerComponentAsync method call.\r\n
0x70000005 | RemoveServerComponentAsync method call.\r\n
0x70000006 | Deployment provider shutdown.\r\n
0x70000007 | Deployment provider initialization.\r\n
0x70000008 | GetAlterationState method call.\r\n
0x70000009 | KeepAlive Mechanism actions.\r\n
0x7000000a | Provider Lifecycle actions.\r\n
0x90000001 | Microsoft-Windows-ServerManager-DeploymentProvider\r\n
0x90000002 | Operational\r\n
0x90000003 | Debug\r\n
0xb0000064 | GetServerComponentAsync method started.\r\n
0xb0000065 | GetServerComponentAsync method returned Completed.  Restart required: %1\r\n
0xb0000066 | GetServerComponentAsync method returned InProgress. %1 of %2\r\n
0xb0000067 | GetServerComponentAsync method returned Failed. Error: %1\r\n
0xb0000068 | GetEnumerationState method started.\r\n
0xb0000069 | GetEnumerationState method returned Completed. Restart required: %1\r\n
0xb000006a | GetEnumerationState method returned InProgress. %1 of %2\r\n
0xb000006b | GetEnumerationState method returned Failed. Error: %1\r\n
0xb000006c | GetServerComponent request started on a separate thread.\r\n
0xb000006d | GetServerComponent request ended on a separate thread.\r\n
0xb000006e | Generic Deployment Error: %1.\r\n
0xb000006f | Starting a GetServerComponent request.\r\n
0xb0000070 | Completed processing the GetServerComponent request.  Restart required: %1\r\n
0xb0000071 | An error occured while processing the GetServerComponent. Error: %1\r\n
0xb0000072 | An error occured while creating Wbem CIM entry: %1 ClassName: %2 Error: %3\r\n
0xb0000073 | Component %1 has invalid DISM state %2\r\n
0xb00000c8 | AddServerComponentAsync method started. Adding ClassNames: %1\r\n
0xb00000c9 | AddServerComponentAsync method returned InProgress. %1 of %2\r\n
0xb00000ca | AddServerComponentAsync method returned Failed. %1\r\n
0xb00000cb | Processing request to add Server Components: %1\r\n
0xb00000cc | Add request complete. Server Components added: %1\r\n
0xb000012c | RemoveServerComponentAsync method started. Removing ClassNames: %1\r\n
0xb000012d | RemoveServerComponentAsync method returned InProgress. %1 of %2\r\n
0xb000012e | RemoveServerComponentAsync method returned Failed. Error: %1\r\n
0xb000012f | Processing request to remove Server Components: %1\r\n
0xb0000130 | Remove request complete. Server Components removed: %1\r\n
0xb0000190 | GetAlterationState method started.\r\n
0xb0000191 | GetAlterationState method ended. Reboot required: %1\r\n
0xb0000192 | GetAlterationState method returned InProgress. %1 of %2\r\n
0xb0000193 | GetAlterationState method returned Failed. Error: %1\r\n
0xb00001c2 | Calling MI_RefuseUnload method.\r\n
0xb00001c3 | Calling MI_RequestUnload method.\r\n
0xb00001c4 | CreateEvent method call failed.\r\n
0xb00001c5 | CreateMutex method call failed.\r\n
0xb00001c6 | MI_PostResult method call failed.\r\n
0xb00001c7 | MI_Application_Initialize method call failed.\r\n
0xb00001c8 | MI_Application_Close method call failed.\r\n
0xb00001c9 | MI_RefuseUnload method call failed.\r\n
0xb00001ca | MI_RequestUnload method call failed.\r\n
0xb00001cb | The KeepAlive Callback method threw an exception.\r\n
0xb00001cc | Starting the KeepAlive Mechanism.\r\n
0xb00001cd | The KeepAlive Mechanism started on another thread.\r\n
0xb00001ce | The KeepAlive Mutex is in Abandoned state.\r\n
0xb00001cf | Loading Deployment provider.\r\n
0xb00001d0 | Unloading Deployment provider.\r\n
0xb00001d1 | Invalid Request GUID: %1\r\n
0xb00001d2 | A WMI operation failed. Op: %1 ErrorCode: %2\r\n
0xb00001d3 | Exception detected while reporting a failure. Unable to recover. %1\r\n
0xb00001f4 | ExecuteEnumerationCommand %1 Guid %2.\r\n
0xb00001f5 | ExecuteEnumerationCommand ReadFromCache %1 Guid %2.\r\n
0xb00001f6 | ExecuteEnumerationCommand SpawnThread %1 Guid %2.\r\n
0xb00001f7 | Enumerate Function Call %1 Guid %2.\r\n
0xb00001f8 | Component Repository LoadFromCache %1.\r\n
0xb00001f9 | Component Repository BuildRelationshipModel %1.\r\n
0xb00001fa | Component Repository ScanSystem %1.\r\n
0xb00001fb | Create DismSessionManager %1.\r\n
0xb00001fc | LoadRepository delete existing components %1.\r\n
0xb00001fd | LoadRepository DismGetFeaturesEx API %1.\r\n
0xb00001fe | LoadRepository add updates %1.\r\n
0xb00001ff | LoadRepository add components %1.\r\n
0xb0000200 | LoadRepository validate components %1.\r\n
0xb0000201 | Original Server components, Update WMI CLass definitions %1 Guid %2.\r\n
0xb0000202 | Write component results to registry %1 Guid %2.\r\n
0xb0000203 | Write ServiceReport to registry %1 Guid %2.\r\n
0xb0000204 | Consequtive Get Status requests %1 Guid %2.\r\n
0xb0000205 | Consequtive Get requests read from registry %1 Guid %2.\r\n
0xb0000206 | Consequtive Get requests build sorted component tree %1 Guid %2.\r\n
0xb0000207 | Consequtive Get request select based on component names %1 Guid %2.\r\n
0xb0000208 | Consequtive Get request returning InProgress %1 Guid %2.\r\n
0xb0000209 | Add server component %1 Guid %2.\r\n
0xb000020a | Add server component on vhd %1 Guid %2.\r\n
0xb000020b | Reset component repository before Add %1.\r\n
0xb000020c | Prepare components for Add %1.\r\n
0xb000020d | Validate Mutual exclusion groups before add %1.\r\n
0xb000020e | Open Dism session for adding components %1.\r\n
0xb000020f | Get updates to deploy %1.\r\n
0xb0000210 | DismEnableFeatures API %1.\r\n
0xb0000211 | DismCommitImage API called after EnableFeatures %1.\r\n
0xb0000212 | Refresh state fo modified components %1.\r\n
0xb0000213 | Remove server component %1 Guid %2.\r\n
0xb0000214 | Remove server component on vhd %1 Guid %2.\r\n
0xb0000215 | Reset repository before removing components %1.\r\n
0xb0000216 | Prepare components for remove %1.\r\n
0xb0000217 | Create a list of components that are left installed after remove %1.\r\n
0xb0000218 | Refresh the state of the modified components after refresh %1.\r\n
0xb0000219 | Get the list of updates to remove %1.\r\n
0xb000021a | Update the children of Dism updates for removal %1.\r\n
0xb000021b | Add unused dism updates to the list for removal %1..\r\n
0xb000021c | DismDisableFeatures API %1.\r\n
0xb000021d | DismCommitImage API for remove %1.\r\n
0xb000021f | Submit Alteration request %1 Guid %2.\r\n
0xb0000220 | Convert Ids to unique names and save config data %1 Guid %2.\r\n
0xb0000221 | Validate component identities %1 Guid %2.\r\n
0xb0000222 | Mount Image %1 Image %2.\r\n
0xb0000223 | Renmount Image %1 Image %2.\r\n
0xb0000224 | Unmount Image %1 Image %2.\r\n
0xb0000225 | UpdateImageInfo %1 Image %2.\r\n
0xb0000226 | CBS Restart Check %1.\r\n
0xb0000501 | Unknown MUM2 element detected. FeatureName: %1 UnknownElement: %2\r\n
0xb0000502 | Unknown MUM2 attribute detected. FeatureName: %1 Element: %2 UnknownAttribute: %3\r\n
0xb0000503 | Server components require the Id property. Container Update: %1\r\n
0xb0000504 | Server components require the UniqueName property. Feature: %1\r\n
0xb0000505 | Server components require the DisplayName property. Container Update: %1\r\n
0xb0000506 | Server components require the Description property. Feature: %1\r\n
0xb0000507 | Server component's parent not found. Container Update: %1\r\n
0xb0000508 | Server components require the Version property. Container Update: %1\r\n
0xb0000509 | Server component's deploys section contains an update that was not found. Container Update: %1. Deploys Update: %2\r\n
0xb000050a | Mutual Exclusion conflict detected. Components "%1" are all members of group "%2"\r\n
0xb000050b | Failed to parse MUM2 Xml blob for update %1 hResult: %2\r\n
0xb000050c | Invalid MUM2 configuration status detected. Missing registry value. FeatureName: %1\r\n
0xb000050d | Internal fatal error while parsing MUM2 data. hResult: %1\r\n
0xb000050e | Internal fatal error. Op: %1 hResult: %2\r\n
0xb000050f | CBS Session %1 status. IsComplete: %2 hResult: %3\r\n
0xb0000510 | Task Start:  %1\r\n
0xb0000511 | Task Stop:   %1\r\n
0xb0000512 | Failed to read ConfigurationStatus from registry. Update %1 Key: %2 Value: %3\r\n
0xb0000513 | Using existing component cache from memory. Count: %1\r\n
0xb0000514 | Component cache read from registry. Count: %1\r\n
0xb0000515 | Component cache loaded from Dism. Count: %1\r\n
0xb0000516 | Unknown MUM2 value detected. FeatureName: %1 Attribute: %2 UnknownValue: %3\r\n
0xb0000517 | Failed to parse MUM2 for feature %1\r\n
0xb0000518 | Found unknown update. FeatureName %1\r\n
0xb0000519 | Unable to find component %1 referenced by component %2\r\n
0xb000051a | Component %1 has invalid ServerComponentType %2. This type is only valid if the component has a parent.\r\n
0xb000051b | Failed to unmount image - %1.\r\n
0xb000051d | Partial install detected. Component %1 depends on uninstalled component %2\r\n
0xb000051e | Invalid Mum2 detected for component %1.\r\n
0xb000051f | Invalid OptionalCompanionFor detected in registry.\r\n
0xb0000520 | Failure loading OptionalCompanionFor from registry. Error: %1.\r\n
0xb0000521 | Failed to load cache from registry. Error: %1 Attempting to load components from system.\r\n
0xb0000522 | Update %1 is not present. ServerComponent %2 will be removed from the Role and Feature list.\r\n
0xb0000523 | Exception Detected: %1 ErrorID: %2\r\n
0xb0000524 | Unknown Parent %1 required by %2. Removing %2 from feature list.\r\n
0xb0000525 | Unknown dependency %1 required by %2. Removing %2 from feature list.\r\n
0xb0000526 | Unknown optional tool %1 for feature %2.\r\n
0xb0000601 | Unable to open installer session. Error Code: %1\r\n
0xb0000602 | Unable to initialize installer. Error Code: %1\r\n
0xb0000603 | Failed to obtain status information from mounted images. hResult: %1\r\n
0xb0000604 | Failed to mount image. ImageFile: %1 MountPath: %2 hResult: %3\r\n
0xb0000605 | Failed read features from system. hResult: %1\r\n
0xb0000606 | Failed read feature info. Feature: %1 hResult: %2\r\n
0xb0000607 | Failed get the last CBS session ID. hResult: %1\r\n
0xb0000608 | Failed get the state from CBS session ID %1. hResult: %2\r\n
0xb0000609 | Failed to unmount image. ImageFile: %1 MountPath: %2 hResult: %3\r\n
0xb000060a | Failed to remount image. ImageFile: %1 MountPath: %2 hResult: %3\r\n
0xb000060b | Unable to install updates %1. hResult: %2\r\n
0xb000060c | Unable to uninstall updates %1. hResult: %2\r\n
0xb000060d | Dism session busy. Retry: %1\r\n
0xb000060e | Attempting to enable updates via Dism: %1\r\n
0xb000060f | Attempting to disable updates via Dism: %1\r\n
0xb0000610 | CBS session busy. Retry: %1\r\n
0xb0000611 | Internal fatal error. Op: %1 Message: %2\r\n
0xb0000612 | Error reading configuration status for %1. Error: %2\r\n
0xb0000613 | Failed to load module %1. Error: %2\r\n
0xb0000614 | Failed to resource ID %2 from module %1.\r\n
