## provdiagnostics.dll

Path: %SystemRoot%\system32\provdiagnostics.dll

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Provisioning-Diagnostics-Provider\r\n
0x90000002 | Admin\r\n
0x90000003 | Debug\r\n
0xb000000a | Configuring ProvXML with category '%1'.%n%nProvXML data:%n%2\r\n
0xb000000b | ProvXML category '%1' completed successfully. %2\r\n
0xb000000c | ProvXML category '%1' failed with '%2' at CSP node '%3'. %4\r\n
0xb0000014 | Applying package '%1' ID: %2.\r\n
0xb0000015 | Package '%1' has completed.\r\n
0xb0000016 | Package '%1' failed with '%2'.\r\n
0xb000001e | Initiating provisioning turn '%1'.\r\n
0xb000001f | Provisioning turn '%1' has completed.\r\n
0xb0000020 | Provisioning turn '%1' failed with '%2'.\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Provisioning-Diagnostics-Provider\r\n
0x90000002 | Admin\r\n
0x90000003 | AutoPilot\r\n
0x90000004 | Debug\r\n
0xb000000a | Configuring ProvXML with category '%1'.%n%nProvXML data:%n%2\r\n
0xb000000b | ProvXML category '%1' completed successfully. %2\r\n
0xb000000c | ProvXML category '%1' failed with '%2' at CSP node '%3'. %4\r\n
0xb0000014 | Applying package '%1' ID: %2.\r\n
0xb0000015 | Package '%1' has completed.\r\n
0xb0000016 | Package '%1' failed with '%2'.\r\n
0xb000001e | Initiating provisioning turn '%1'.\r\n
0xb000001f | Provisioning turn '%1' has completed.\r\n
0xb0000020 | Provisioning turn '%1' failed with '%2'.\r\n
0xb0000028 | Registry specified search path is invalid: %1.\r\n
0xb0000064 | AutoPilot policy [%1] not found.\r\n
0xb0000065 | AutoPilotGetPolicyDwordByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000066 | AutoPilotGetPolicyDwordByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000067 | AutoPilotGetPolicyStringByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000068 | AutoPilotGetPolicyStringByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000069 | AutoPilotDisable succeeded.\r\n
0xb000006a | AutoPilotDisable error:  HRESULT = %1.\r\n
0xb000006b | AutoPilot state = %1.\r\n
0xb000006c | AutoPilotIsDisabled error:  HRESULT = %1.\r\n
0xb000006d | AutoPilotGetOobeSettingsOverride succeeded:  OOBE setting = %1; state = %2.\r\n
0xb000006e | AutoPilotGetOobeSettingsOverride error:  OOBE setting = %2; HRESULT = %1.\r\n
0xb000006f | AutoPilotRetrieveSettings succeeded.\r\n
0xb0000070 | AutoPilotRetrieveSettings error:  HRESULT = %1.\r\n
0xb0000071 | AutoPilot reported the DLL was unloaded while there were %1 outstanding calls.\r\n
0xb0000072 | AutoPilotRetrieveSettings was skipped because this version of Windows does not support Azure Active Directory join.\r\n
0xb0000096 | AutoPilotManager started the MSA service for TPM attestation identity.\r\n
0xb0000097 | AutoPilotManager started the TPM task to update TPM attestation.\r\n
0xb0000098 | AutoPilotManager reported TPM task is complete.\r\n
0xb0000099 | AutoPilotManager reported the state changed from %1 to %2.\r\n
0xb000009a | AutoPilotManager failed to start MSA service.  HRESULT = %1.\r\n
0xb000009b | AutoPilotManager failed to start TPM task.  HRESULT = %1.\r\n
0xb000009c | AutoPilotManager reported that MSA TPM is not configured for hardware TPM attestation even though the profile indicates it is required.  AutoPilot cannot proceed.\r\n
0xb00000a0 | AutoPilotRetrieveSettings beginning acquisition.\r\n
0xb00000a1 | AutoPilotManager retrieve settings succeeded.\r\n
0xb00000a2 | AutoPilotManager determined download is not required and the device is not provisioned.  Clean or reset the device to change this.\r\n
0xb00000a3 | AutoPilotManager determined download is not required and the device is already provisioned.  Clean or reset the device to change this.\r\n
0xb00000a4 | AutoPilotManager determined Internet is available to attempt policy download.\r\n
0xb00000a5 | AutoPilotManager determined Internet is not available; policy download will queue when available.\r\n
0xb00000a6 | AutoPilotManager reported Internet is now available.\r\n
0xb00000a7 | AutoPilotManager reported Internet is still not available.\r\n
0xb00000a8 | AutoPilotManager reported MSA TPM device identity was updated.\r\n
0xb00000a9 | AutoPilotManager set TPM identity confirmed.\r\n
0xb00000aa | AutoPilotManager set AutoPilot profile as available.\r\n
0xb00000ab | AutoPilotManager failed to set TPM identity confirmed.  HRESULT = %1.\r\n
0xb00000ac | AutoPilotManager failed to set AutoPilot profile as available.  HRESULT = %1.\r\n
0xb00000ad | AutoPilotManager failed to register for network availability.  HRESULT = %1.\r\n
0xb00000ae | AutoPilotManager failed to register for device identity availability.  HRESULT = %1\r\n
0xb00000af | AutoPilotManager failed to register for device identity task update.  HRESULT = %1\r\n
0xb000012c | AutoPilotManager device enrollment reported an initialization failure.  HRESULT = %1.\r\n
0xb000012d | AutoPilotManager device enrollment reported a blocking failure.  Overall error %2, last reported stage %1.\r\n
0xb000012e | AutoPilotManager device enrollment failed during stage %1 with error %2.\r\n
0xb000012f | AutoPilotManager device enrollment succeeded.  Last valid stage: %1.\r\n
0xd0000001 | ProfileState_Unknown\r\n
0xd0000002 | ProfileState_NotProvisioned\r\n
0xd0000003 | ProfileState_TpmAttesting\r\n
0xd0000004 | ProfileState_Available\r\n
0xd0000005 | ProfileState_TpmNotAvailable\r\n
0xd0000006 | Initial\r\n
0xd0000007 | AADConfigure\r\n
0xd0000008 | AADEnroll\r\n
0xd0000009 | DeviceDiscovery\r\n
0xd000000a | AADTicket\r\n
0xd000000b | MDMEnrolling\r\n
0xd000000c | Completed\r\n
0xd000000d | Completed\r\n

### 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Provisioning-Diagnostics-Provider\r\n
0x90000002 | Admin\r\n
0x90000003 | AutoPilot\r\n
0x90000004 | Debug\r\n
0x90000005 | ManagementService\r\n
0xb000000a | Configuring ProvXML with category '%1'.%n%nProvXML data:%n%2\r\n
0xb000000b | ProvXML category '%1' completed successfully. %2\r\n
0xb000000c | ProvXML category '%1' failed with '%2' at CSP node '%3'. %4\r\n
0xb0000014 | Applying package '%1' ID: %2.\r\n
0xb0000015 | Package '%1' has completed.\r\n
0xb0000016 | Package '%1' failed with '%2'.\r\n
0xb0000028 | Registry specified search path is invalid: %1.\r\n
0xb0000029 | InitiateSystemShutdownEx succeeded.\r\n
0xb000002a | InitiateSystemShutdownEx failed. HRESULT = %1.\r\n
0xb000002b | Start RebootSystem ...\r\n
0xb000002c | InitiateSystemShutdownEx succeeded.\r\n
0xb000002d | InitiateSystemShutdownEx failed. HRESULT = %1.\r\n
0xb000003c | AddPackage initiated, pathCount = %1\r\n
0xb000003d | AddPackage succeeded, targetPath = %1\r\n
0xb000003e | AddPackage failed. HRESULT = %1\r\n
0xb000003f | RemovePackage initiated, package id = %1\r\n
0xb0000040 | RemovePackage succeeded, package id = %1\r\n
0xb0000041 | RemovePackage failed. HRESULT = %1, package id = %2, at stage = %3\r\n
0xb0000042 | RemovePackageMetadata succeeded, package id = %1\r\n
0xb0000043 | RemovePackageMetadata failed. HRESULT = %1, package id = %2, at stage = %3\r\n
0xb0000044 | RemoveResourceManagerPackageMetadataForCsp succeeded, package id = %1\r\n
0xb0000045 | RemoveResourceManagerPackageMetadataForCsp failed. HRESULT = %1, package id = %2\r\n
0xb0000046 | ApplyKnownPackages initiated, turn = %1\r\n
0xb0000047 | ApplyKnownPackages succeeded, turn = %1\r\n
0xb0000048 | ApplyKnownPackages failed. turn = %1, HRESULT = %2\r\n
0xb0000050 | GetLastProvisioningResultsAsync succeeded, resultCount = %1\r\n
0xb0000051 | GetLastProvisioningResultsAsync failed. HRESULT = %1\r\n
0xb0000052 | GetLastProvisioningCommandResultsAsync succeeded, resultCount = %1\r\n
0xb0000053 | GetLastProvisioningCommandResultsAsync. HRESULT = %1\r\n
0xb000005a | Settings detail.%nsource = %1.%npackageIdToDelete = %2.%npackagePathsToAdd = %3.\r\n
0xb000005b | RegisterForCspAlerts succeeded. EnrollmentId = %1.\r\n
0xb000005c | RegisterForCspAlerts Failed. HResult = %1, EnrollmentId = %2.\r\n
0xb000005d | UpdatePendingResultInternal succeeded. PackageId = %1.\r\n
0xb000005e | UpdatePendingResultInternal Failed. HResult = %1, PackageId = %2.\r\n
0xb0000064 | AutoPilot policy [%1] not found.\r\n
0xb0000065 | AutoPilotGetPolicyDwordByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000066 | AutoPilotGetPolicyDwordByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000067 | AutoPilotGetPolicyStringByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000068 | AutoPilotGetPolicyStringByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000069 | AutoPilotDisable succeeded.\r\n
0xb000006a | AutoPilotDisable error:  HRESULT = %1.\r\n
0xb000006b | AutoPilot state = %1.\r\n
0xb000006c | AutoPilotIsDisabled error:  HRESULT = %1.\r\n
0xb000006d | AutoPilotGetOobeSettingsOverride succeeded:  OOBE setting = %1; state = %2.\r\n
0xb000006e | AutoPilotGetOobeSettingsOverride error:  OOBE setting = %2; HRESULT = %1.\r\n
0xb000006f | AutoPilotRetrieveSettings succeeded.\r\n
0xb0000070 | AutoPilotRetrieveSettings error:  HRESULT = %1.\r\n
0xb0000071 | AutoPilot reported the DLL was unloaded while there were %1 outstanding calls.\r\n
0xb0000072 | AutoPilotRetrieveSettings was skipped because this version of Windows does not support Azure Active Directory join.\r\n
0xb0000073 | Autopilot discovery failed to find a valid MDM.  Confirm that the AAD tenant is properly provisioned and licensed for exactly one MDM.  HRESULT = %1\r\n
0xb0000096 | AutoPilotManager started the MSA service for TPM attestation identity.\r\n
0xb0000097 | AutoPilotManager started the TPM task to update TPM attestation.\r\n
0xb0000098 | AutoPilotManager reported TPM task is complete.\r\n
0xb0000099 | AutoPilotManager reported the state changed from %1 to %2.\r\n
0xb000009a | AutoPilotManager failed to start MSA service.  HRESULT = %1.\r\n
0xb000009b | AutoPilotManager failed to start TPM task.  HRESULT = %1.\r\n
0xb000009c | AutoPilotManager reported that MSA TPM is not configured for hardware TPM attestation even though the profile indicates it is required.  AutoPilot cannot proceed.\r\n
0xb000009d | AutoPilotManager reported that TPM attestation lasted %1 microseconds.\r\n
0xb00000a0 | AutoPilotRetrieveSettings beginning acquisition.\r\n
0xb00000a1 | AutoPilotManager retrieve settings succeeded.\r\n
0xb00000a2 | AutoPilotManager determined download is not required and the device is not provisioned.  Clean or reset the device to change this.\r\n
0xb00000a3 | AutoPilotManager determined download is not required and the device is already provisioned.  Clean or reset the device to change this.\r\n
0xb00000a4 | AutoPilotManager determined Internet is available to attempt policy download.\r\n
0xb00000a5 | AutoPilotManager determined Internet is not available; policy download will queue when available.\r\n
0xb00000a6 | AutoPilotManager reported Internet is now available.\r\n
0xb00000a7 | AutoPilotManager reported Internet is still not available.\r\n
0xb00000a8 | AutoPilotManager reported MSA TPM device identity was updated.\r\n
0xb00000a9 | AutoPilotManager set TPM identity confirmed.\r\n
0xb00000aa | AutoPilotManager set AutoPilot profile as available.\r\n
0xb00000ab | AutoPilotManager failed to set TPM identity confirmed.  HRESULT = %1.\r\n
0xb00000ac | AutoPilotManager failed to set AutoPilot profile as available.  HRESULT = %1.\r\n
0xb00000ad | AutoPilotManager failed to register for network availability.  HRESULT = %1.\r\n
0xb00000ae | AutoPilotManager failed to register for device identity availability.  HRESULT = %1\r\n
0xb00000af | AutoPilotManager failed to register for device identity task update.  HRESULT = %1\r\n
0xb00000b0 | MSA TPM keystate has been updated.  New server state = %1, new client state = %2\r\n
0xb00000b1 | TPM attestation retry is being attempted.  Current retry attempt %1 of %2 maximum\r\n
0xb00000b2 | AutoPilotManager began device enrollment with internal state %1.\r\n
0xb00000b3 | AutoPilotManager began device enrollment phase %1.\r\n
0xb00000b4 | AutoPilotManager failed during device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b5 | AutoPilotManager completed device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b6 | AutoPilotManager reported that the retry timer event was set to %1 milliseconds.\r\n
0xb00000b7 | AutoPilotManager reported that the retry timer event occurred\r\n
0xb00000b8 | AutoPilotManager failed to register for MSA keystate update availability.  HRESULT = %1\r\n
0xb000012c | AutoPilotManager device enrollment reported an initialization failure.  HRESULT = %1.\r\n
0xb000012d | AutoPilotManager device enrollment reported a blocking failure.  Overall error %2, last reported stage %1.\r\n
0xb000012e | AutoPilotManager device enrollment failed during stage %1 with error %2.\r\n
0xb000012f | AutoPilotManager device enrollment succeeded.  Last valid stage: %1.\r\n
0xb0000136 | AutoPilot configuration file path: %1 %nExpanded path:%2 %nFile path source:%3\r\n
0xb0000137 | Failed to load AutoPilot configuration file, HRESULT = %1.\r\n
0xb0000138 | Failed to parse AutoPilot configuration file, HRESULT = %1.\r\n
0xb0000139 | Invalid ZtdCorrelationId found in Autopilot configuration file, HRESULT = %1. ZtdCorrelationId: '%2'.\r\n
0xb00003e8 | Management service starting.\r\n
0xb00003e9 | Management service started.\r\n
0xb00003ea | Management service failed to start.  HRESULT = %1\r\n
0xb00003eb | Management service failed to register.\r\n
0xb00003ec | Management service shutdown.\r\n
0xb00003ed | Management service WIL error was reported.%nHRESULT: %1%nFile: %2, line %3%nMessage: %4\r\n
0xb00003ee | Management service call %1 is deprecated!\r\n
0xb00003ef | Management service cleared the local Autopilot cached state.\r\n
0xb00003f0 | Management service failed to clear the local Autopilot cached state.  HRESULT = %1\r\n
0xd0000001 | ProfileState_Unknown\r\n
0xd0000002 | ProfileState_NotProvisioned\r\n
0xd0000003 | ProfileState_TpmAttesting\r\n
0xd0000004 | ProfileState_Available\r\n
0xd0000005 | ProfileState_TpmNotAvailable\r\n
0xd0000006 | Completed\r\n
0xd0000007 | Initial\r\n
0xd0000008 | AADConfigure\r\n
0xd0000009 | AADEnroll\r\n
0xd000000a | DeviceDiscovery\r\n
0xd000000b | AADTicket\r\n
0xd000000c | MDMEnrolling\r\n
0xd000000d | Completed\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Provisioning-Diagnostics-Provider\r\n
0x90000002 | Admin\r\n
0x90000003 | AutoPilot\r\n
0x90000004 | Debug\r\n
0x90000005 | ManagementService\r\n
0xb000000a | Configuring ProvXML with category '%1'.%n%nProvXML data:%n%2\r\n
0xb000000b | ProvXML category '%1' completed successfully. %2\r\n
0xb000000c | ProvXML category '%1' failed with '%2' at CSP node '%3'. %4\r\n
0xb000000d | Setting %1 was ignored because it was not available on this OS build\r\n
0xb0000014 | Applying package '%1' ID: %2.\r\n
0xb0000015 | Package '%1' has completed.\r\n
0xb0000016 | Package '%1' failed with '%2'.\r\n
0xb0000028 | Registry specified search path is invalid: %1.\r\n
0xb0000029 | InitiateSystemShutdownEx succeeded.\r\n
0xb000002a | InitiateSystemShutdownEx failed. HRESULT = %1.\r\n
0xb000002b | Start RebootSystem ...\r\n
0xb000002c | InitiateSystemShutdownEx succeeded.\r\n
0xb000002d | InitiateSystemShutdownEx failed. HRESULT = %1.\r\n
0xb000003c | AddPackage initiated, pathCount = %1\r\n
0xb000003d | AddPackage succeeded, targetPath = %1\r\n
0xb000003e | AddPackage failed. HRESULT = %1\r\n
0xb000003f | RemovePackage initiated, package id = %1\r\n
0xb0000040 | RemovePackage succeeded, package id = %1\r\n
0xb0000041 | RemovePackage failed. HRESULT = %1, package id = %2, at stage = %3\r\n
0xb0000042 | RemovePackageMetadata succeeded, package id = %1\r\n
0xb0000043 | RemovePackageMetadata failed. HRESULT = %1, package id = %2, at stage = %3\r\n
0xb0000044 | RemoveResourceManagerPackageMetadataForCsp succeeded, package id = %1\r\n
0xb0000045 | RemoveResourceManagerPackageMetadataForCsp failed. HRESULT = %1, package id = %2\r\n
0xb0000046 | ApplyKnownPackages initiated, turn = %1\r\n
0xb0000047 | ApplyKnownPackages succeeded, turn = %1\r\n
0xb0000048 | ApplyKnownPackages failed. turn = %1, HRESULT = %2\r\n
0xb0000050 | GetLastProvisioningResultsAsync succeeded, resultCount = %1\r\n
0xb0000051 | GetLastProvisioningResultsAsync failed. HRESULT = %1\r\n
0xb0000052 | GetLastProvisioningCommandResultsAsync succeeded, resultCount = %1\r\n
0xb0000053 | GetLastProvisioningCommandResultsAsync. HRESULT = %1\r\n
0xb000005a | Settings detail.%nsource = %1.%npackageIdToDelete = %2.%npackagePathsToAdd = %3.\r\n
0xb000005b | RegisterForCspAlerts succeeded. EnrollmentId = %1.\r\n
0xb000005c | RegisterForCspAlerts Failed. HResult = %1, EnrollmentId = %2.\r\n
0xb000005d | UpdatePendingResultInternal succeeded. PackageId = %1.\r\n
0xb000005e | UpdatePendingResultInternal Failed. HResult = %1, PackageId = %2.\r\n
0xb0000064 | AutoPilot policy [%1] not found.\r\n
0xb0000065 | AutoPilotGetPolicyDwordByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000066 | AutoPilotGetPolicyDwordByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000067 | AutoPilotGetPolicyStringByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000068 | AutoPilotGetPolicyStringByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000069 | AutoPilotDisable succeeded.\r\n
0xb000006a | AutoPilotDisable error:  HRESULT = %1.\r\n
0xb000006b | AutoPilot state = %1.\r\n
0xb000006c | AutoPilotIsDisabled error:  HRESULT = %1.\r\n
0xb000006d | AutoPilotGetOobeSettingsOverride succeeded:  OOBE setting = %1; state = %2.\r\n
0xb000006e | AutoPilotGetOobeSettingsOverride error:  OOBE setting = %2; HRESULT = %1.\r\n
0xb000006f | AutoPilotRetrieveSettings succeeded.\r\n
0xb0000070 | AutoPilotRetrieveSettings error:  HRESULT = %1.\r\n
0xb0000071 | AutoPilot reported the DLL was unloaded while there were %1 outstanding calls.\r\n
0xb0000072 | AutoPilotRetrieveSettings was skipped because this version of Windows does not support Azure Active Directory join.\r\n
0xb0000073 | Autopilot discovery failed to find a valid MDM.  Confirm that the AAD tenant is properly provisioned and licensed for exactly one MDM.  HRESULT = %1\r\n
0xb0000096 | AutoPilotManager started the MSA service for TPM attestation identity.\r\n
0xb0000097 | AutoPilotManager started the TPM task to update TPM attestation.\r\n
0xb0000098 | AutoPilotManager reported TPM task is complete.\r\n
0xb0000099 | AutoPilotManager reported the state changed from %1 to %2.\r\n
0xb000009a | AutoPilotManager failed to start MSA service.  HRESULT = %1.\r\n
0xb000009b | AutoPilotManager failed to start TPM task.  HRESULT = %1.\r\n
0xb000009c | AutoPilotManager reported that MSA TPM is not configured for hardware TPM attestation even though the profile indicates it is required.  AutoPilot cannot proceed.\r\n
0xb000009d | AutoPilotManager reported that TPM attestation lasted %1 microseconds.\r\n
0xb00000a0 | AutoPilotRetrieveSettings beginning acquisition.\r\n
0xb00000a1 | AutoPilotManager retrieve settings succeeded.\r\n
0xb00000a2 | AutoPilotManager determined download is not required and the device is not provisioned.  Clean or reset the device to change this.\r\n
0xb00000a3 | AutoPilotManager determined download is not required and the device is already provisioned.  Clean or reset the device to change this.\r\n
0xb00000a4 | AutoPilotManager determined Internet is available to attempt policy download.\r\n
0xb00000a5 | AutoPilotManager determined Internet is not available; policy download will queue when available.\r\n
0xb00000a6 | AutoPilotManager reported Internet is now available.\r\n
0xb00000a7 | AutoPilotManager reported Internet is still not available.\r\n
0xb00000a8 | AutoPilotManager reported MSA TPM device identity was updated.\r\n
0xb00000a9 | AutoPilotManager set TPM identity confirmed.\r\n
0xb00000aa | AutoPilotManager set AutoPilot profile as available.\r\n
0xb00000ab | AutoPilotManager failed to set TPM identity confirmed.  HRESULT = %1.\r\n
0xb00000ac | AutoPilotManager failed to set AutoPilot profile as available.  HRESULT = %1.\r\n
0xb00000ad | AutoPilotManager failed to register for network availability.  HRESULT = %1.\r\n
0xb00000ae | AutoPilotManager failed to register for device identity availability.  HRESULT = %1\r\n
0xb00000af | AutoPilotManager failed to register for device identity task update.  HRESULT = %1\r\n
0xb00000b0 | MSA TPM keystate has been updated.  New server state = %1, new client state = %2\r\n
0xb00000b1 | TPM attestation retry is being attempted.  Current retry attempt %1 of %2 maximum\r\n
0xb00000b2 | AutoPilotManager began device enrollment with internal state %1.\r\n
0xb00000b3 | AutoPilotManager began device enrollment phase %1.\r\n
0xb00000b4 | AutoPilotManager failed during device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b5 | AutoPilotManager completed device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b6 | AutoPilotManager reported that the retry timer event was set to %1 milliseconds.\r\n
0xb00000b7 | AutoPilotManager reported that the retry timer event occurred\r\n
0xb00000b8 | AutoPilotManager failed to register for MSA keystate update availability.  HRESULT = %1\r\n
0xb000012c | AutoPilotManager device enrollment reported an initialization failure.  HRESULT = %1.\r\n
0xb000012d | AutoPilotManager device enrollment reported a blocking failure.  Overall error %2, last reported stage %1.\r\n
0xb000012e | AutoPilotManager device enrollment failed during stage %1 with error %2.\r\n
0xb000012f | AutoPilotManager device enrollment succeeded.  Last valid stage: %1.\r\n
0xb0000136 | AutoPilot configuration file path: %1 %nExpanded path:%2 %nFile path source:%3\r\n
0xb0000137 | Failed to load AutoPilot configuration file, HRESULT = %1.\r\n
0xb0000138 | Failed to parse AutoPilot configuration file, HRESULT = %1.\r\n
0xb0000139 | Invalid ZtdCorrelationId found in Autopilot configuration file, HRESULT = %1. ZtdCorrelationId: '%2'.\r\n
0xb00003e8 | Management service starting.\r\n
0xb00003e9 | Management service started.\r\n
0xb00003ea | Management service failed to start.  HRESULT = %1\r\n
0xb00003eb | Management service failed to register.\r\n
0xb00003ec | Management service shutdown.\r\n
0xb00003ed | Management service WIL error was reported.%nHRESULT: %1%nFile: %2, line %3%nMessage: %4\r\n
0xb00003ee | Management service call %1 is deprecated!\r\n
0xb00003ef | Management service cleared the local Autopilot cached state.\r\n
0xb00003f0 | Management service failed to clear the local Autopilot cached state.  HRESULT = %1\r\n
0xb00007d0 | Device rename has been blocked through MDM because machine is domain joined\r\n
0xd0000001 | ProfileState_Unknown\r\n
0xd0000002 | ProfileState_NotProvisioned\r\n
0xd0000003 | ProfileState_TpmAttesting\r\n
0xd0000004 | ProfileState_Available\r\n
0xd0000005 | ProfileState_TpmNotAvailable\r\n
0xd0000006 | Completed\r\n
0xd0000007 | Initial\r\n
0xd0000008 | AADConfigure\r\n
0xd0000009 | AADEnroll\r\n
0xd000000a | DeviceDiscovery\r\n
0xd000000b | AADTicket\r\n
0xd000000c | MDMEnrolling\r\n
0xd000000d | Completed\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Provisioning-Diagnostics-Provider\r\n
0x90000002 | Admin\r\n
0x90000003 | AutoPilot\r\n
0x90000004 | Debug\r\n
0x90000005 | ManagementService\r\n
0xb000000a | Configuring ProvXML with category '%1'.%n%nProvXML data:%n%2\r\n
0xb000000b | ProvXML category '%1' completed successfully. %2\r\n
0xb000000c | ProvXML category '%1' failed with '%2' at CSP node '%3'. %4\r\n
0xb000000d | Setting %1 was ignored because it was not available on this OS build\r\n
0xb0000014 | Applying package '%1' ID: %2.\r\n
0xb0000015 | Package '%1' has completed.\r\n
0xb0000016 | Package '%1' failed with '%2'.\r\n
0xb0000017 | Skipping package '%1' ID: %2.\r\n
0xb0000028 | Registry specified search path is invalid: %1.\r\n
0xb0000029 | InitiateSystemShutdownEx succeeded.\r\n
0xb000002a | InitiateSystemShutdownEx failed. HRESULT = %1.\r\n
0xb000002b | Start RebootSystem ...\r\n
0xb000002c | InitiateSystemShutdownEx succeeded.\r\n
0xb000002d | InitiateSystemShutdownEx failed. HRESULT = %1.\r\n
0xb000003c | AddPackage initiated, pathCount = %1\r\n
0xb000003d | AddPackage succeeded, targetPath = %1\r\n
0xb000003e | AddPackage failed. HRESULT = %1\r\n
0xb000003f | RemovePackage initiated, package id = %1\r\n
0xb0000040 | RemovePackage succeeded, package id = %1\r\n
0xb0000041 | RemovePackage failed. HRESULT = %1, package id = %2, at stage = %3\r\n
0xb0000042 | RemovePackageMetadata succeeded, package id = %1\r\n
0xb0000043 | RemovePackageMetadata failed. HRESULT = %1, package id = %2, at stage = %3\r\n
0xb0000044 | RemoveResourceManagerPackageMetadataForCsp succeeded, package id = %1\r\n
0xb0000045 | RemoveResourceManagerPackageMetadataForCsp failed. HRESULT = %1, package id = %2\r\n
0xb0000046 | ApplyKnownPackages initiated, turn = %1\r\n
0xb0000047 | ApplyKnownPackages succeeded, turn = %1\r\n
0xb0000048 | ApplyKnownPackages failed. turn = %1, HRESULT = %2\r\n
0xb0000050 | GetLastProvisioningResultsAsync succeeded, resultCount = %1\r\n
0xb0000051 | GetLastProvisioningResultsAsync failed. HRESULT = %1\r\n
0xb0000052 | GetLastProvisioningCommandResultsAsync succeeded, resultCount = %1\r\n
0xb0000053 | GetLastProvisioningCommandResultsAsync. HRESULT = %1\r\n
0xb000005a | Settings detail.%nsource = %1.%npackageIdToDelete = %2.%npackagePathsToAdd = %3.\r\n
0xb000005b | RegisterForCspAlerts succeeded. EnrollmentId = %1.\r\n
0xb000005c | RegisterForCspAlerts Failed. HResult = %1, EnrollmentId = %2.\r\n
0xb000005d | UpdatePendingResultInternal succeeded. PackageId = %1.\r\n
0xb000005e | UpdatePendingResultInternal Failed. HResult = %1, PackageId = %2.\r\n
0xb0000064 | AutoPilot policy [%1] not found.\r\n
0xb0000065 | AutoPilotGetPolicyDwordByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000066 | AutoPilotGetPolicyDwordByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000067 | AutoPilotGetPolicyStringByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000068 | AutoPilotGetPolicyStringByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000069 | AutoPilotDisable succeeded.\r\n
0xb000006a | AutoPilotDisable error:  HRESULT = %1.\r\n
0xb000006b | AutoPilot state = %1.\r\n
0xb000006c | AutoPilotIsDisabled error:  HRESULT = %1.\r\n
0xb000006d | AutoPilotGetOobeSettingsOverride succeeded:  OOBE setting = %1; state = %2.\r\n
0xb000006e | AutoPilotGetOobeSettingsOverride error:  OOBE setting = %2; HRESULT = %1.\r\n
0xb000006f | AutoPilotRetrieveSettings succeeded.\r\n
0xb0000070 | AutoPilotRetrieveSettings error:  HRESULT = %1.\r\n
0xb0000071 | AutoPilot reported the DLL was unloaded while there were %1 outstanding calls.\r\n
0xb0000072 | AutoPilotRetrieveSettings was skipped because this version of Windows does not support Azure Active Directory join.\r\n
0xb0000073 | Autopilot discovery failed to find a valid MDM.  Confirm that the AAD tenant is properly provisioned and licensed for exactly one MDM.  HRESULT = %1\r\n
0xb0000096 | AutoPilotManager started the MSA service for TPM attestation identity.\r\n
0xb0000097 | AutoPilotManager started the TPM task to update TPM attestation.\r\n
0xb0000098 | AutoPilotManager reported TPM task is complete.\r\n
0xb0000099 | AutoPilotManager reported the state changed from %1 to %2.\r\n
0xb000009a | AutoPilotManager failed to start MSA service.  HRESULT = %1.\r\n
0xb000009b | AutoPilotManager failed to start TPM task.  HRESULT = %1.\r\n
0xb000009c | AutoPilotManager reported that MSA TPM is not configured for hardware TPM attestation even though the profile indicates it is required.  AutoPilot cannot proceed.\r\n
0xb000009d | AutoPilotManager reported that TPM attestation lasted %1 microseconds.\r\n
0xb00000a0 | AutoPilotRetrieveSettings beginning acquisition.\r\n
0xb00000a1 | AutoPilotManager retrieve settings succeeded.\r\n
0xb00000a2 | AutoPilotManager determined download is not required and the device is not provisioned.  Clean or reset the device to change this.\r\n
0xb00000a3 | AutoPilotManager determined download is not required and the device is already provisioned.  Clean or reset the device to change this.\r\n
0xb00000a4 | AutoPilotManager determined Internet is available to attempt policy download.\r\n
0xb00000a5 | AutoPilotManager determined Internet is not available; policy download will queue when available.\r\n
0xb00000a6 | AutoPilotManager reported Internet is now available.\r\n
0xb00000a7 | AutoPilotManager reported Internet is still not available.\r\n
0xb00000a8 | AutoPilotManager reported MSA TPM device identity was updated.\r\n
0xb00000a9 | AutoPilotManager set TPM identity confirmed.\r\n
0xb00000aa | AutoPilotManager set AutoPilot profile as available.\r\n
0xb00000ab | AutoPilotManager failed to set TPM identity confirmed.  HRESULT = %1.\r\n
0xb00000ac | AutoPilotManager failed to set AutoPilot profile as available.  HRESULT = %1.\r\n
0xb00000ad | AutoPilotManager failed to register for network availability.  HRESULT = %1.\r\n
0xb00000ae | AutoPilotManager failed to register for device identity availability.  HRESULT = %1\r\n
0xb00000af | AutoPilotManager failed to register for device identity task update.  HRESULT = %1\r\n
0xb00000b0 | MSA TPM keystate has been updated.  New server state = %1, new client state = %2\r\n
0xb00000b1 | TPM attestation retry is being attempted.  Current retry attempt %1 of %2 maximum\r\n
0xb00000b2 | AutoPilotManager began device enrollment with internal state %1.\r\n
0xb00000b3 | AutoPilotManager began device enrollment phase %1.\r\n
0xb00000b4 | AutoPilotManager failed during device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b5 | AutoPilotManager completed device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b6 | AutoPilotManager reported that the retry timer event was set to %1 milliseconds.\r\n
0xb00000b7 | AutoPilotManager reported that the retry timer event occurred\r\n
0xb00000b8 | AutoPilotManager failed to register for MSA keystate update availability.  HRESULT = %1\r\n
0xb000012c | AutoPilotManager device enrollment reported an initialization failure.  HRESULT = %1.\r\n
0xb000012d | AutoPilotManager device enrollment reported a blocking failure.  Overall error %2, last reported stage %1.\r\n
0xb000012e | AutoPilotManager device enrollment failed during stage %1 with error %2.\r\n
0xb000012f | AutoPilotManager device enrollment succeeded.  Last valid stage: %1.\r\n
0xb0000136 | AutoPilot configuration file path: %1 %nExpanded path:%2 %nFile path source:%3\r\n
0xb0000137 | Failed to load AutoPilot configuration file, HRESULT = %1.\r\n
0xb0000138 | Failed to parse AutoPilot configuration file, HRESULT = %1.\r\n
0xb0000139 | Invalid ZtdCorrelationId found in Autopilot configuration file, HRESULT = %1. ZtdCorrelationId: '%2'.\r\n
0xb00003e8 | Management service starting.\r\n
0xb00003e9 | Management service started.\r\n
0xb00003ea | Management service failed to start.  HRESULT = %1\r\n
0xb00003eb | Management service failed to register.\r\n
0xb00003ec | Management service shutdown.\r\n
0xb00003ed | Management service WIL error was reported.%nHRESULT: %1%nFile: %2, line %3%nMessage: %4\r\n
0xb00003ee | Management service call %1 is deprecated!\r\n
0xb00003ef | Management service cleared the local Autopilot cached state.\r\n
0xb00003f0 | Management service failed to clear the local Autopilot cached state.  HRESULT = %1\r\n
0xb00007d0 | Device rename has been blocked through MDM because machine is domain joined\r\n
0xd0000001 | ProfileState_Unknown\r\n
0xd0000002 | ProfileState_NotProvisioned\r\n
0xd0000003 | ProfileState_TpmAttesting\r\n
0xd0000004 | ProfileState_Available\r\n
0xd0000005 | ProfileState_TpmNotAvailable\r\n
0xd0000006 | Completed\r\n
0xd0000007 | Initial\r\n
0xd0000008 | AADConfigure\r\n
0xd0000009 | AADEnroll\r\n
0xd000000a | DeviceDiscovery\r\n
0xd000000b | AADTicket\r\n
0xd000000c | MDMEnrolling\r\n
0xd000000d | Completed\r\n
