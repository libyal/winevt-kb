## autopilotdiag.dll

Path: %SystemRoot%\system32\autopilotdiag.dll

### 10.0.18362.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-ModernDeployment-Diagnostics-Provider\r\n
0x90000002 | Admin\r\n
0x90000003 | Autopilot\r\n
0x90000004 | Debug\r\n
0x90000005 | ManagementService\r\n
0xb0000064 | Autopilot policy [%1] not found.\r\n
0xb0000065 | AutopilotGetPolicyDwordByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000066 | AutopilotGetPolicyDwordByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000067 | AutopilotGetPolicyStringByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000068 | AutopilotGetPolicyStringByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000069 | AutopilotDisable succeeded.\r\n
0xb000006a | AutopilotDisable error:  HRESULT = %1.\r\n
0xb000006b | Autopilot state = %1.\r\n
0xb000006c | AutopilotIsDisabled error:  HRESULT = %1.\r\n
0xb000006d | AutopilotGetOobeSettingsOverride succeeded:  OOBE setting = %1; state = %2.\r\n
0xb000006e | AutopilotGetOobeSettingsOverride error:  OOBE setting = %2; HRESULT = %1.\r\n
0xb000006f | AutopilotRetrieveSettings succeeded.\r\n
0xb0000070 | AutopilotRetrieveSettings error:  HRESULT = %1.\r\n
0xb0000071 | Autopilot reported the DLL was unloaded while there were %1 outstanding calls.\r\n
0xb0000072 | AutopilotRetrieveSettings was skipped because this version of Windows does not support Azure Active Directory join.\r\n
0xb0000073 | Autopilot discovery failed to find a valid MDM.  Confirm that the AAD tenant is properly provisioned and licensed for exactly one MDM.  HRESULT = %1\r\n
0xb0000096 | AutopilotManager started the MSA service for TPM attestation identity.\r\n
0xb0000097 | AutopilotManager started the TPM maintenance task to update TPM attestation.\r\n
0xb0000098 | AutopilotManager reported TPM maintenance task is complete.\r\n
0xb0000099 | AutopilotManager reported the state changed from %1 to %2.\r\n
0xb000009a | AutopilotManager failed to start MSA service.  HRESULT = %1.\r\n
0xb000009b | AutopilotManager failed to start TPM task.  HRESULT = %1.\r\n
0xb000009c | AutopilotManager reported that MSA TPM is not configured for hardware TPM attestation even though the profile indicates it is required.  Autopilot cannot proceed.\r\n
0xb000009d | AutopilotManager reported that TPM attestation lasted %1 microseconds.\r\n
0xb000009e | AutopilotManager reported that TPM enhanced diagnostics logging was enabled for %1 providers.\r\n
0xb00000a0 | AutopilotRetrieveSettings beginning acquisition.\r\n
0xb00000a1 | AutopilotManager retrieve settings succeeded.\r\n
0xb00000a2 | AutopilotManager determined download is not required and the device is not provisioned.  Clean or reset the device to change this.\r\n
0xb00000a3 | AutopilotManager determined download is not required and the device is already provisioned.  Clean or reset the device to change this.\r\n
0xb00000a4 | AutopilotManager determined Internet is available to attempt policy download.\r\n
0xb00000a5 | AutopilotManager determined Internet is not available; policy download will queue when available.\r\n
0xb00000a6 | AutopilotManager reported Internet is now available.\r\n
0xb00000a7 | AutopilotManager reported Internet is still not available.\r\n
0xb00000a8 | AutopilotManager reported MSA TPM device identity was updated.\r\n
0xb00000a9 | AutopilotManager set TPM identity confirmed.\r\n
0xb00000aa | AutopilotManager reported that Autopilot profile download is now complete.\r\n
0xb00000ab | AutopilotManager failed to set TPM identity confirmed.  HRESULT = %1.\r\n
0xb00000ac | AutopilotManager failed to set Autopilot profile as available.  HRESULT = %1.\r\n
0xb00000ad | AutopilotManager failed to register for network availability.  HRESULT = %1.\r\n
0xb00000ae | AutopilotManager failed to register for device identity availability.  HRESULT = %1\r\n
0xb00000af | AutopilotManager failed to register for device identity task update.  HRESULT = %1\r\n
0xb00000b0 | MSA TPM keystate has been updated.  New server state = %1, new client state = %2\r\n
0xb00000b1 | Configuring TPM for attestation.  Current attempt %1 of %2 maximum.\r\n
0xb00000b2 | AutopilotManager began device enrollment with internal state %1.\r\n
0xb00000b3 | AutopilotManager began device enrollment phase %1.\r\n
0xb00000b4 | AutopilotManager failed during device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b5 | AutopilotManager completed device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b6 | AutopilotManager reported that the retry timer event was set to %1 milliseconds.\r\n
0xb00000b7 | AutopilotManager reported that the retry timer event occurred\r\n
0xb00000b8 | AutopilotManager failed to register for MSA keystate update availability.  HRESULT = %1\r\n
0xb00000b9 | AutopilotManager failed to retrieve settings.  HRESULT = %1\r\n
0xb00000ba | AutopilotManager TPM configuration already in progress.\r\n
0xb00000bb | AutopilotManager TPM configuration occurred before retry timer ready.\r\n
0xb00000bd | Configuring TPM exceeded maximum number of attempts.\r\n
0xb00000be | Windows AIK certificate enrollment task was triggered.\r\n
0xb00000bf | Windows TPM maintenance task is being skipped since AIK certificate is already present.\r\n
0xb00000c0 | Autopilot device enrollment failed with error HRESULT = %1. Waiting %2 milliseconds then retrying.%nCurrent attempt %3 of %4.\r\n
0xb00000c1 | Autopilot manager is attempting profile download retry.  Current attempt %1 of %2.\r\n
0xb00000c2 | Autopilot manager will re-attempt the download after %1 milliseconds.\r\n
0xb00000c8 | Windows AIK object could not be loaded.  HRESULT = %1\r\n
0xb00000c9 | Windows AIK key not found by name.\r\n
0xb00000ca | Windows AIK certificate download failed. HRESULT = %1\r\n
0xb00000cb | Windows AIK alternative load failed. HRESULT = %1\r\n
0xb00000cc | Windows AIK certificate request did not result in a new certificate.\r\n
0xb00000cd | Windows AIK certificate request succeeded and a new certificate is available.\r\n
0xb00000ce | Windows AIK key could not be opened. HRESULT = %1\r\n
0xb00000cf | Windows AIK key failed certificate request. HRESULT = %1\r\n
0xb00000fa | AutopilotManager started AIK certificate acquisition task.\r\n
0xb00000fb | AutopilotManager reported AIK certificate acquisition task returned HRESULT = %1.%nElapsed time: %2 microseconds (maximum allowed time was %3 milliseconds).\r\n
0xb00000fc | AutopilotManager reported AIK key was located.\r\n
0xb00000fd | AutopilotManager reported AIK certificate was located.\r\n
0xb00000fe | AutopilotManager reported AIK certificate was not located.\r\n
0xb000012c | AutopilotManager device enrollment reported an initialization failure.  HRESULT = %1.\r\n
0xb000012d | AutopilotManager device enrollment reported a blocking failure.  Overall error %2, last reported stage %1.\r\n
0xb000012e | AutopilotManager device enrollment failed during stage %1 with error %2.\r\n
0xb000012f | AutopilotManager device enrollment succeeded.  Last valid stage: %1.\r\n
0xb0000136 | Autopilot configuration file path: %1 %nExpanded path:%2\r\n
0xb0000137 | Failed to load Autopilot configuration file, HRESULT = %1.\r\n
0xb0000138 | Failed to parse Autopilot configuration file, HRESULT = %1.\r\n
0xb0000139 | Invalid ZtdCorrelationId found in Autopilot configuration file, HRESULT = %1. ZtdCorrelationId: '%2'.\r\n
0xb00001f4 | Invalid data specified in Autopilot policy override configuration.%nHRESULT = %1%nPolicy name: %2.\r\n
0xb00001f5 | AutopilotManager failed to load Json for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f6 | AutopilotManager failed to clear for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f7 | AutopilotManager failed to delete Json for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f8 | AutopilotManager deleted configuration file %1.\r\n
0xb00001f9 | AutopilotManager loaded configuration file %1.\r\n
0xb00001fa | AutopilotManager failed to expand path for %2.%nHRESULT = %1.\r\n
0xb00001fb | AutopilotManager explictly disabled TPM required due to registry setting.\r\n
0xb00001fc | AutopilotManager explictly enabled TPM required due to registry setting.\r\n
0xb00001fd | AutopilotManager enabled TPM requirement due to WhiteGlove policy value %1\r\n
0xb00002bc | Autopilot downloader failed to load override registsry data for %2.%nHRESULT = %1.\r\n
0xb00002bd | Autopilot downloader did not save new profile information because the new profile was empty.\r\n
0xb00002be | Autopilot downloader saved the new profile to %1.\r\n
0xb00002bf | Autopilot downloader retrieved a new profile for %1.\r\n
0xb00002c0 | Autopilot downloader retrieved an empty profile for %1.\r\n
0xb00002c1 | Autopilot downloader cleared the local profile for %1.\r\n
0xb00002c2 | Autopilot downloader failed to download profile for %2.%nHRESULT = %1.%nCorrelation vector: %3\r\n
0xb00002c3 | Autopilot downloader failed to download profile for %2.%nHRESULT = %1.%nCorrelation vector: %3\r\n
0xb00002c4 | Autopilot downloader failed to extract additional error details from response. Response data: %2.%nExtraction failure HRESULT = %1.\r\n
0xb00002c5 | Autopilot failed to download data.  Response code: %1%nDetail message:%n%2\r\n
0xb00002c6 | Autopilot failed to acquire a device ticket for target URL %2.%nHRESULT = %1.\r\n
0xb00002c7 | Autopilot downloader failed to parse target URL:%n%1\r\n
0xb00002c8 | Autopilot downloader failed to convert time %2%nHRESULT = %1.\r\n
0xb00002c9 | Autopilot downloader will use MSA Pre-production environment. This will result in Autopilot failures if production device identities were used.\r\n
0xb00002ca | Autopilot downloader reported a failure acquiring the MSA device ticket. This most likely occurred because MSA and CXH environments do not match (production versus PPE).\r\n
0xb00003e8 | Management service starting.\r\n
0xb00003e9 | Management service started.\r\n
0xb00003ea | Management service failed to start.  HRESULT = %1\r\n
0xb00003eb | Management service failed to register.\r\n
0xb00003ec | Management service shutdown.\r\n
0xb00003ed | Management service WIL error was reported.%nHRESULT: %1%nFile: %2, line %3%nMessage: %4\r\n
0xb00003ee | Management service call %1 is deprecated!\r\n
0xb00003ef | Management service cleared the local Autopilot cached state.\r\n
0xb00003f0 | Management service failed to clear the local Autopilot cached state.  HRESULT = %1\r\n
0xb000044c | Management service will use %1 for persisted storage\r\n
0xb000044d | Management service did not find %1.  Attempting to create it.\r\n
0xb000044e | Management service created %1.\r\n
0xb000044f | Management service found ProcMon.exe for startup profiling.\r\n
0xb0000450 | Management service determined ProcMon.exe startup profiling is not enabled in the registry.\r\n
0xb0000451 | Management service determined ProcMon.exe startup profiling is enabled in the registry.\r\n
0xb0000452 | Management service is beginning ProcMon.exe startup profiling.\r\n
0xb0000453 | Management service is began ProcMon.exe startup profiling.\r\n
0xb0000454 | Management service is stopping ProcMon.exe startup profiling.\r\n
0xb0000455 | Management service has stopped ProcMon.exe startup profiling.\r\n
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
0xd000000e | no key\r\n
0xd000000f | invalid key\r\n
0xd0000010 | software key\r\n
0xd0000011 | unattested key\r\n
0xd0000012 | attested key\r\n
0xd0000013 | revoked\r\n
0xd0000014 | disabled\r\n
0xd0000015 | no key\r\n
0xd0000016 | machine has no capable TPM\r\n
0xd0000017 | machine has a capable TPM\r\n
0xd0000018 | unknown attestation status\r\n
0xd0000019 | no attestation capability\r\n
0xd000001a | temporary attestation failure\r\n
0xd000001b | long-term attestation failure\r\n
0xd000001c | attested key\r\n

### 10.0.18362.693

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-ModernDeployment-Diagnostics-Provider\r\n
0x90000002 | Admin\r\n
0x90000003 | Autopilot\r\n
0x90000004 | Debug\r\n
0x90000005 | ManagementService\r\n
0xb0000064 | Autopilot policy [%1] not found.\r\n
0xb0000065 | AutopilotGetPolicyDwordByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000066 | AutopilotGetPolicyDwordByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000067 | AutopilotGetPolicyStringByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000068 | AutopilotGetPolicyStringByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000069 | AutopilotDisable succeeded.\r\n
0xb000006a | AutopilotDisable error:  HRESULT = %1.\r\n
0xb000006b | Autopilot state = %1.\r\n
0xb000006c | AutopilotIsDisabled error:  HRESULT = %1.\r\n
0xb000006d | AutopilotGetOobeSettingsOverride succeeded:  OOBE setting = %1; state = %2.\r\n
0xb000006e | AutopilotGetOobeSettingsOverride error:  OOBE setting = %2; HRESULT = %1.\r\n
0xb000006f | AutopilotRetrieveSettings succeeded.\r\n
0xb0000070 | AutopilotRetrieveSettings error:  HRESULT = %1.\r\n
0xb0000071 | Autopilot reported the DLL was unloaded while there were %1 outstanding calls.\r\n
0xb0000072 | AutopilotRetrieveSettings was skipped because this version of Windows does not support Azure Active Directory join.\r\n
0xb0000073 | Autopilot discovery failed to find a valid MDM.  Confirm that the AAD tenant is properly provisioned and licensed for exactly one MDM.  HRESULT = %1\r\n
0xb0000074 | Autopilot Device ESP Domain Controller override was not set.\r\n
0xb0000075 | Autopilot Device ESP Domain Controller override was set by state %1\r\n
0xb0000096 | AutopilotManager started the MSA service for TPM attestation identity.\r\n
0xb0000097 | AutopilotManager started the TPM maintenance task to update TPM attestation.\r\n
0xb0000098 | AutopilotManager reported TPM maintenance task is complete.\r\n
0xb0000099 | AutopilotManager reported the state changed from %1 to %2.\r\n
0xb000009a | AutopilotManager failed to start MSA service.  HRESULT = %1.\r\n
0xb000009b | AutopilotManager failed to start TPM task.  HRESULT = %1.\r\n
0xb000009c | AutopilotManager reported that MSA TPM is not configured for hardware TPM attestation even though the profile indicates it is required.  Autopilot cannot proceed.\r\n
0xb000009d | AutopilotManager reported that TPM attestation lasted %1 microseconds.\r\n
0xb000009e | AutopilotManager reported that TPM enhanced diagnostics logging was enabled for %1 providers.\r\n
0xb00000a0 | AutopilotRetrieveSettings beginning acquisition.\r\n
0xb00000a1 | AutopilotManager retrieve settings succeeded.\r\n
0xb00000a2 | AutopilotManager determined download is not required and the device is not provisioned.  Clean or reset the device to change this.\r\n
0xb00000a3 | AutopilotManager determined download is not required and the device is already provisioned.  Clean or reset the device to change this.\r\n
0xb00000a4 | AutopilotManager determined Internet is available to attempt policy download.\r\n
0xb00000a5 | AutopilotManager determined Internet is not available; policy download will queue when available.\r\n
0xb00000a6 | AutopilotManager reported Internet is now available.\r\n
0xb00000a7 | AutopilotManager reported Internet is still not available.\r\n
0xb00000a8 | AutopilotManager reported MSA TPM device identity was updated.\r\n
0xb00000a9 | AutopilotManager set TPM identity confirmed.\r\n
0xb00000aa | AutopilotManager reported that Autopilot profile download is now complete.\r\n
0xb00000ab | AutopilotManager failed to set TPM identity confirmed.  HRESULT = %1.\r\n
0xb00000ac | AutopilotManager failed to set Autopilot profile as available.  HRESULT = %1.\r\n
0xb00000ad | AutopilotManager failed to register for network availability.  HRESULT = %1.\r\n
0xb00000ae | AutopilotManager failed to register for device identity availability.  HRESULT = %1\r\n
0xb00000af | AutopilotManager failed to register for device identity task update.  HRESULT = %1\r\n
0xb00000b0 | MSA TPM keystate has been updated.  New server state = %1, new client state = %2\r\n
0xb00000b1 | Configuring TPM for attestation.  Current attempt %1 of %2 maximum.\r\n
0xb00000b2 | AutopilotManager began device enrollment with internal state %1.\r\n
0xb00000b3 | AutopilotManager began device enrollment phase %1.\r\n
0xb00000b4 | AutopilotManager failed during device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b5 | AutopilotManager completed device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b6 | AutopilotManager reported that the retry timer event was set to %1 milliseconds.\r\n
0xb00000b7 | AutopilotManager reported that the retry timer event occurred\r\n
0xb00000b8 | AutopilotManager failed to register for MSA keystate update availability.  HRESULT = %1\r\n
0xb00000b9 | AutopilotManager failed to retrieve settings.  HRESULT = %1\r\n
0xb00000ba | AutopilotManager TPM configuration already in progress.\r\n
0xb00000bb | AutopilotManager TPM configuration occurred before retry timer ready.\r\n
0xb00000bd | Configuring TPM exceeded maximum number of attempts.\r\n
0xb00000be | Windows AIK certificate enrollment task was triggered.\r\n
0xb00000bf | Windows TPM maintenance task is being skipped since AIK certificate is already present.\r\n
0xb00000c0 | Autopilot device enrollment failed with error HRESULT = %1. Waiting %2 milliseconds then retrying.%nCurrent attempt %3 of %4.\r\n
0xb00000c1 | Autopilot manager is attempting profile download retry.  Current attempt %1 of %2.\r\n
0xb00000c2 | Autopilot manager will re-attempt the download after %1 milliseconds.\r\n
0xb00000c3 | AutopilotManager began device unenrollment\r\n
0xb00000c4 | AutopilotManager completed device unenrollment.  HRESULT = %1\r\n
0xb00000c5 | AutopilotManager failed device unenrollment.  HRESULT = %1\r\n
0xb00000c8 | Windows AIK object could not be loaded.  HRESULT = %1\r\n
0xb00000c9 | Windows AIK key not found by name.\r\n
0xb00000ca | Windows AIK certificate download failed. HRESULT = %1\r\n
0xb00000cb | Windows AIK alternative load failed. HRESULT = %1\r\n
0xb00000cc | Windows AIK certificate request did not result in a new certificate.\r\n
0xb00000cd | Windows AIK certificate request succeeded and a new certificate is available.\r\n
0xb00000ce | Windows AIK key could not be opened. HRESULT = %1\r\n
0xb00000cf | Windows AIK key failed certificate request. HRESULT = %1\r\n
0xb00000d0 | Windows EK certificate is present.\r\n
0xb00000d1 | Windows EK certificate is not present.\r\n
0xb00000d2 | Windows AIK key was found even though the Windows EK certificate is not present. Attempting to re-initialize the TPM task.\r\n
0xb00000fa | AutopilotManager started AIK certificate acquisition task.\r\n
0xb00000fb | AutopilotManager reported AIK certificate acquisition task returned HRESULT = %1.%nElapsed time: %2 microseconds (maximum allowed time was %3 milliseconds).\r\n
0xb00000fc | AutopilotManager reported AIK key was located.\r\n
0xb00000fd | AutopilotManager reported AIK certificate was located.\r\n
0xb00000fe | AutopilotManager reported AIK certificate was not located.\r\n
0xb000012c | AutopilotManager device enrollment reported an initialization failure.  HRESULT = %1.\r\n
0xb000012d | AutopilotManager device enrollment reported a blocking failure.  Overall error %2, last reported stage %1.\r\n
0xb000012e | AutopilotManager device enrollment failed during stage %1 with error %2.\r\n
0xb000012f | AutopilotManager device enrollment succeeded.  Last valid stage: %1.\r\n
0xb0000136 | Autopilot configuration file path: %1 %nExpanded path:%2\r\n
0xb0000137 | Failed to load Autopilot configuration file, HRESULT = %1.\r\n
0xb0000138 | Failed to parse Autopilot configuration file, HRESULT = %1.\r\n
0xb0000139 | Invalid ZtdCorrelationId found in Autopilot configuration file, HRESULT = %1. ZtdCorrelationId: '%2'.\r\n
0xb000013a | AutopilotManager reported that the Autopilot profile data could not be downloaded. Any Autopilot settings will not be used and the device will not be managed.\r\n
0xb000013b | AutopilotManager failed to record the setting for Autopilot device not managed, HRESULT = %1.\r\n
0xb00001f4 | Invalid data specified in Autopilot policy override configuration.%nHRESULT = %1%nPolicy name: %2.\r\n
0xb00001f5 | AutopilotManager failed to load Json for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f6 | AutopilotManager failed to clear for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f7 | AutopilotManager failed to delete Json for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f8 | AutopilotManager deleted configuration file %1.\r\n
0xb00001f9 | AutopilotManager loaded configuration file %1.\r\n
0xb00001fa | AutopilotManager failed to expand path for %2.%nHRESULT = %1.\r\n
0xb00001fb | AutopilotManager explictly disabled TPM required due to registry setting.\r\n
0xb00001fc | AutopilotManager explictly enabled TPM required due to registry setting.\r\n
0xb00001fd | AutopilotManager enabled TPM requirement due to WhiteGlove policy value %1\r\n
0xb00002bc | Autopilot downloader failed to load override registsry data for %2.%nHRESULT = %1.\r\n
0xb00002bd | Autopilot downloader did not save new profile information because the new profile was empty.\r\n
0xb00002be | Autopilot downloader saved the new profile to %1.\r\n
0xb00002bf | Autopilot downloader retrieved a new profile for %1.\r\n
0xb00002c0 | Autopilot downloader retrieved an empty profile for %1.\r\n
0xb00002c1 | Autopilot downloader cleared the local profile for %1.\r\n
0xb00002c2 | Autopilot downloader failed to download profile for %2.%nHRESULT = %1.%nCorrelation vector: %3\r\n
0xb00002c3 | Autopilot downloader failed to download profile for %2.%nHRESULT = %1.%nCorrelation vector: %3\r\n
0xb00002c4 | Autopilot downloader failed to extract additional error details from response. Response data: %2.%nExtraction failure HRESULT = %1.\r\n
0xb00002c5 | Autopilot failed to download data.  Response code: %1%nDetail message:%n%2\r\n
0xb00002c6 | Autopilot failed to acquire a device ticket for target URL %2.%nHRESULT = %1.\r\n
0xb00002c7 | Autopilot downloader failed to parse target URL:%n%1\r\n
0xb00002c8 | Autopilot downloader failed to convert time %2%nHRESULT = %1.\r\n
0xb00002c9 | Autopilot downloader will use MSA Pre-production environment. This will result in Autopilot failures if production device identities were used.\r\n
0xb00002ca | Autopilot downloader reported a failure acquiring the MSA device ticket. This most likely occurred because MSA and CXH environments do not match (production versus PPE).\r\n
0xb00003e8 | Management service starting.\r\n
0xb00003e9 | Management service started.\r\n
0xb00003ea | Management service failed to start.  HRESULT = %1\r\n
0xb00003eb | Management service failed to register.\r\n
0xb00003ec | Management service shutdown.\r\n
0xb00003ed | Management service WIL error was reported.%nHRESULT: %1%nFile: %2, line %3%nMessage: %4\r\n
0xb00003ee | Management service call %1 is deprecated!\r\n
0xb00003ef | Management service cleared the local Autopilot cached state.\r\n
0xb00003f0 | Management service failed to clear the local Autopilot cached state.  HRESULT = %1\r\n
0xb000044c | Management service will use %1 for persisted storage\r\n
0xb000044d | Management service did not find %1.  Attempting to create it.\r\n
0xb000044e | Management service created %1.\r\n
0xb000044f | Management service found ProcMon.exe for startup profiling.\r\n
0xb0000450 | Management service determined ProcMon.exe startup profiling is not enabled in the registry.\r\n
0xb0000451 | Management service determined ProcMon.exe startup profiling is enabled in the registry.\r\n
0xb0000452 | Management service is beginning ProcMon.exe startup profiling.\r\n
0xb0000453 | Management service is began ProcMon.exe startup profiling.\r\n
0xb0000454 | Management service is stopping ProcMon.exe startup profiling.\r\n
0xb0000455 | Management service has stopped ProcMon.exe startup profiling.\r\n
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
0xd000000e | no key\r\n
0xd000000f | invalid key\r\n
0xd0000010 | software key\r\n
0xd0000011 | unattested key\r\n
0xd0000012 | attested key\r\n
0xd0000013 | revoked\r\n
0xd0000014 | disabled\r\n
0xd0000015 | no key\r\n
0xd0000016 | machine has no capable TPM\r\n
0xd0000017 | machine has a capable TPM\r\n
0xd0000018 | unknown attestation status\r\n
0xd0000019 | no attestation capability\r\n
0xd000001a | temporary attestation failure\r\n
0xd000001b | long-term attestation failure\r\n
0xd000001c | attested key\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-ModernDeployment-Diagnostics-Provider\r\n
0x90000002 | Admin\r\n
0x90000003 | Autopilot\r\n
0x90000004 | Debug\r\n
0x90000005 | ManagementService\r\n
0xb0000064 | Autopilot policy [%1] not found.\r\n
0xb0000065 | AutopilotGetPolicyDwordByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000066 | AutopilotGetPolicyDwordByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000067 | AutopilotGetPolicyStringByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000068 | AutopilotGetPolicyStringByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000069 | AutopilotDisable succeeded.\r\n
0xb000006a | AutopilotDisable error:  HRESULT = %1.\r\n
0xb000006b | Autopilot state = %1.\r\n
0xb000006c | AutopilotIsDisabled error:  HRESULT = %1.\r\n
0xb000006d | AutopilotGetOobeSettingsOverride succeeded:  OOBE setting = %1; state = %2.\r\n
0xb000006e | AutopilotGetOobeSettingsOverride error:  OOBE setting = %2; HRESULT = %1.\r\n
0xb000006f | AutopilotRetrieveSettings succeeded.\r\n
0xb0000070 | AutopilotRetrieveSettings error:  HRESULT = %1.\r\n
0xb0000071 | Autopilot reported the DLL was unloaded while there were %1 outstanding calls.\r\n
0xb0000072 | AutopilotRetrieveSettings was skipped because this version of Windows does not support Azure Active Directory join.\r\n
0xb0000073 | Autopilot discovery failed to find a valid MDM.  Confirm that the AAD tenant is properly provisioned and licensed for exactly one MDM.  HRESULT = %1\r\n
0xb0000074 | Autopilot Device ESP Domain Controller override was not set.\r\n
0xb0000075 | Autopilot Device ESP Domain Controller override was set by state %1\r\n
0xb0000096 | AutopilotManager started the MSA service for TPM attestation identity.\r\n
0xb0000097 | AutopilotManager started the TPM maintenance task to update TPM attestation.\r\n
0xb0000098 | AutopilotManager reported TPM maintenance task is complete.\r\n
0xb0000099 | AutopilotManager reported the state changed from %1 to %2.\r\n
0xb000009a | AutopilotManager failed to start MSA service.  HRESULT = %1.\r\n
0xb000009b | AutopilotManager failed to start TPM task.  HRESULT = %1.\r\n
0xb000009c | AutopilotManager reported that MSA TPM is not configured for hardware TPM attestation even though the profile indicates it is required.  Autopilot cannot proceed.\r\n
0xb000009d | AutopilotManager reported that TPM attestation lasted %1 microseconds.\r\n
0xb000009e | AutopilotManager reported that TPM enhanced diagnostics logging was enabled for %1 providers.\r\n
0xb00000a0 | AutopilotRetrieveSettings beginning acquisition.\r\n
0xb00000a1 | AutopilotManager retrieve settings succeeded.\r\n
0xb00000a2 | AutopilotManager determined download is not required and the device is not provisioned.  Clean or reset the device to change this.\r\n
0xb00000a3 | AutopilotManager determined download is not required and the device is already provisioned.  Clean or reset the device to change this.\r\n
0xb00000a4 | AutopilotManager determined Internet is available to attempt policy download.\r\n
0xb00000a5 | AutopilotManager determined Internet is not available; policy download will queue when available.\r\n
0xb00000a6 | AutopilotManager reported Internet is now available.\r\n
0xb00000a7 | AutopilotManager reported Internet is still not available.\r\n
0xb00000a8 | AutopilotManager reported MSA TPM device identity was updated.\r\n
0xb00000a9 | AutopilotManager set TPM identity confirmed.\r\n
0xb00000aa | AutopilotManager reported that Autopilot profile download is now complete.\r\n
0xb00000ab | AutopilotManager failed to set TPM identity confirmed.  HRESULT = %1.\r\n
0xb00000ac | AutopilotManager failed to set Autopilot profile as available.  HRESULT = %1.\r\n
0xb00000ad | AutopilotManager failed to register for network availability.  HRESULT = %1.\r\n
0xb00000ae | AutopilotManager failed to register for device identity availability.  HRESULT = %1\r\n
0xb00000af | AutopilotManager failed to register for device identity task update.  HRESULT = %1\r\n
0xb00000b0 | MSA TPM keystate has been updated.  New server state = %1, new client state = %2\r\n
0xb00000b1 | Configuring TPM for attestation.  Current attempt %1 of %2 maximum.\r\n
0xb00000b2 | AutopilotManager began device enrollment with internal state %1.\r\n
0xb00000b3 | AutopilotManager began device enrollment phase %1.\r\n
0xb00000b4 | AutopilotManager failed during device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b5 | AutopilotManager completed device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b6 | AutopilotManager reported that the retry timer event was set to %1 milliseconds.\r\n
0xb00000b7 | AutopilotManager reported that the retry timer event occurred\r\n
0xb00000b8 | AutopilotManager failed to register for MSA keystate update availability.  HRESULT = %1\r\n
0xb00000b9 | AutopilotManager failed to retrieve settings.  HRESULT = %1\r\n
0xb00000ba | AutopilotManager TPM configuration already in progress.\r\n
0xb00000bb | AutopilotManager TPM configuration occurred before retry timer ready.\r\n
0xb00000bd | Configuring TPM exceeded maximum number of attempts.\r\n
0xb00000be | Windows AIK certificate enrollment task was triggered.\r\n
0xb00000bf | Windows TPM maintenance task is being skipped since AIK certificate is already present.\r\n
0xb00000c0 | Autopilot device enrollment failed with error HRESULT = %1. Waiting %2 milliseconds then retrying.%nCurrent attempt %3 of %4.\r\n
0xb00000c1 | Autopilot manager is attempting profile download retry.  Current attempt %1 of %2.\r\n
0xb00000c2 | Autopilot manager will re-attempt the download after %1 milliseconds.\r\n
0xb00000c3 | AutopilotManager began device unenrollment\r\n
0xb00000c4 | AutopilotManager completed device unenrollment.  HRESULT = %1\r\n
0xb00000c5 | AutopilotManager failed device unenrollment.  HRESULT = %1\r\n
0xb00000c8 | Windows AIK object could not be loaded.  HRESULT = %1\r\n
0xb00000c9 | Windows AIK key not found by name.\r\n
0xb00000ca | Windows AIK certificate download failed. HRESULT = %1\r\n
0xb00000cb | Windows AIK alternative load failed. HRESULT = %1\r\n
0xb00000cc | Windows AIK certificate request did not result in a new certificate.\r\n
0xb00000cd | Windows AIK certificate request succeeded and a new certificate is available.\r\n
0xb00000ce | Windows AIK key could not be opened. HRESULT = %1\r\n
0xb00000cf | Windows AIK key failed certificate request. HRESULT = %1\r\n
0xb00000d0 | Windows EK certificate is present.\r\n
0xb00000d1 | Windows EK certificate is not present.\r\n
0xb00000d2 | Windows AIK key was found even though the Windows EK certificate is not present. Attempting to re-initialize the TPM task.\r\n
0xb00000d3 | AutopilotManager reported that a TPM was required but the TPM failed an attestation capability check.  HRESULT = %1\r\n
0xb00000fa | AutopilotManager started AIK certificate acquisition task.\r\n
0xb00000fb | AutopilotManager reported AIK certificate acquisition task returned HRESULT = %1.%nElapsed time: %2 microseconds (maximum allowed time was %3 milliseconds).\r\n
0xb00000fc | AutopilotManager reported AIK key was located.\r\n
0xb00000fd | AutopilotManager reported AIK certificate was located.\r\n
0xb00000fe | AutopilotManager reported AIK certificate was not located.\r\n
0xb000012c | AutopilotManager device enrollment reported an initialization failure.  HRESULT = %1.\r\n
0xb000012d | AutopilotManager device enrollment reported a blocking failure.  Overall error %2, last reported stage %1.\r\n
0xb000012e | AutopilotManager device enrollment failed during stage %1 with error %2.\r\n
0xb000012f | AutopilotManager device enrollment succeeded.  Last valid stage: %1.\r\n
0xb0000136 | Autopilot configuration file path: %1 %nExpanded path:%2\r\n
0xb0000137 | Failed to load Autopilot configuration file, HRESULT = %1.\r\n
0xb0000138 | Failed to parse Autopilot configuration file, HRESULT = %1.\r\n
0xb0000139 | Invalid ZtdCorrelationId found in Autopilot configuration file, HRESULT = %1. ZtdCorrelationId: '%2'.\r\n
0xb000013a | AutopilotManager reported that the Autopilot profile data could not be downloaded. Any Autopilot settings will not be used and the device will not be managed.\r\n
0xb000013b | AutopilotManager failed to record the setting for Autopilot device not managed, HRESULT = %1.\r\n
0xb00001f4 | Invalid data specified in Autopilot policy override configuration.%nHRESULT = %1%nPolicy name: %2.\r\n
0xb00001f5 | AutopilotManager failed to load Json for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f6 | AutopilotManager failed to clear for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f7 | AutopilotManager failed to delete Json for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f8 | AutopilotManager deleted configuration file %1.\r\n
0xb00001f9 | AutopilotManager loaded configuration file %1.\r\n
0xb00001fa | AutopilotManager failed to expand path for %2.%nHRESULT = %1.\r\n
0xb00001fb | AutopilotManager explictly disabled TPM required due to registry setting.\r\n
0xb00001fc | AutopilotManager explictly enabled TPM required due to registry setting.\r\n
0xb00001fd | AutopilotManager enabled TPM requirement due to WhiteGlove policy value %1\r\n
0xb00002bc | Autopilot downloader failed to load override registsry data for %2.%nHRESULT = %1.\r\n
0xb00002bd | Autopilot downloader did not save new profile information because the new profile was empty.\r\n
0xb00002be | Autopilot downloader saved the new profile to %1.\r\n
0xb00002bf | Autopilot downloader retrieved a new profile for %1.\r\n
0xb00002c0 | Autopilot downloader retrieved an empty profile for %1.\r\n
0xb00002c1 | Autopilot downloader cleared the local profile for %1.\r\n
0xb00002c2 | Autopilot downloader failed to download profile for %2.%nHRESULT = %1.%nCorrelation vector: %3\r\n
0xb00002c3 | Autopilot downloader failed to download profile for %2.%nHRESULT = %1.%nCorrelation vector: %3\r\n
0xb00002c4 | Autopilot downloader failed to extract additional error details from response. Response data: %2.%nExtraction failure HRESULT = %1.\r\n
0xb00002c5 | Autopilot failed to download data.  Response code: %1%nDetail message:%n%2\r\n
0xb00002c6 | Autopilot failed to acquire a device ticket for target URL %2.%nHRESULT = %1.\r\n
0xb00002c7 | Autopilot downloader failed to parse target URL:%n%1\r\n
0xb00002c8 | Autopilot downloader failed to convert time %2%nHRESULT = %1.\r\n
0xb00002c9 | Autopilot downloader will use MSA Pre-production environment. This will result in Autopilot failures if production device identities were used.\r\n
0xb00002ca | Autopilot downloader reported a failure acquiring the MSA device ticket. This most likely occurred because MSA and CXH environments do not match (production versus PPE).\r\n
0xb00002ee | Autopilot downloader reported a failure acquiring the MSA device ticket due to certificate errors. This may be caused by the wrong clock time on the machine so a forced time sync will be attempted.\r\n
0xb00002ef | Autopilot downloader reported time sync succeeded.\r\n
0xb00002f0 | Autopilot downloader reported time sync failed with error = %1.\r\n
0xb00002f1 | Autopilot downloader reported that the machine clock is too far off the server time and a forced time sync will be attempted.%nServer time: %1%nClient time: %2%nSync attempt %3 of %4\r\n
0xb00003e8 | Management service starting.\r\n
0xb00003e9 | Management service started.\r\n
0xb00003ea | Management service failed to start.  HRESULT = %1\r\n
0xb00003eb | Management service failed to register.\r\n
0xb00003ec | Management service shutdown.\r\n
0xb00003ed | Management service WIL error was reported.%nHRESULT: %1%nFile: %2, line %3%nMessage: %4\r\n
0xb00003ee | Management service call %1 is deprecated!\r\n
0xb00003ef | Management service cleared the local Autopilot cached state.\r\n
0xb00003f0 | Management service failed to clear the local Autopilot cached state.  HRESULT = %1\r\n
0xb000044c | Management service will use %1 for persisted storage\r\n
0xb000044d | Management service did not find %1.  Attempting to create it.\r\n
0xb000044e | Management service created %1.\r\n
0xb000044f | Management service found ProcMon.exe for startup profiling.\r\n
0xb0000450 | Management service determined ProcMon.exe startup profiling is not enabled in the registry.\r\n
0xb0000451 | Management service determined ProcMon.exe startup profiling is enabled in the registry.\r\n
0xb0000452 | Management service is beginning ProcMon.exe startup profiling.\r\n
0xb0000453 | Management service is began ProcMon.exe startup profiling.\r\n
0xb0000454 | Management service is stopping ProcMon.exe startup profiling.\r\n
0xb0000455 | Management service has stopped ProcMon.exe startup profiling.\r\n
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
0xd000000e | no key\r\n
0xd000000f | invalid key\r\n
0xd0000010 | software key\r\n
0xd0000011 | unattested key\r\n
0xd0000012 | attested key\r\n
0xd0000013 | revoked\r\n
0xd0000014 | disabled\r\n
0xd0000015 | no key\r\n
0xd0000016 | machine has no capable TPM\r\n
0xd0000017 | machine has a capable TPM\r\n
0xd0000018 | unknown attestation status\r\n
0xd0000019 | no attestation capability\r\n
0xd000001a | temporary attestation failure\r\n
0xd000001b | long-term attestation failure\r\n
0xd000001c | attested key\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-ModernDeployment-Diagnostics-Provider\r\n
0x90000002 | Admin\r\n
0x90000003 | Autopilot\r\n
0x90000004 | Debug\r\n
0x90000005 | ManagementService\r\n
0x90000006 | Diagnostics\r\n
0xb0000064 | Autopilot policy [%1] not found.\r\n
0xb0000065 | AutopilotGetPolicyDwordByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000066 | AutopilotGetPolicyDwordByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000067 | AutopilotGetPolicyStringByName succeeded:  policy name = %1; policy value = %2.\r\n
0xb0000068 | AutopilotGetPolicyStringByName error:  policy name = %2; HRESULT = %1.\r\n
0xb0000069 | AutopilotDisable succeeded.\r\n
0xb000006a | AutopilotDisable error:  HRESULT = %1.\r\n
0xb000006b | Autopilot state = %1.\r\n
0xb000006c | AutopilotIsDisabled error:  HRESULT = %1.\r\n
0xb000006d | AutopilotGetOobeSettingsOverride succeeded:  OOBE setting = %1; state = %2.\r\n
0xb000006e | AutopilotGetOobeSettingsOverride error:  OOBE setting = %2; HRESULT = %1.\r\n
0xb000006f | AutopilotRetrieveSettings succeeded.\r\n
0xb0000070 | AutopilotRetrieveSettings error:  HRESULT = %1.\r\n
0xb0000071 | Autopilot reported the DLL was unloaded while there were %1 outstanding calls.\r\n
0xb0000072 | AutopilotRetrieveSettings was skipped because this version of Windows does not support Azure Active Directory join.\r\n
0xb0000073 | Autopilot discovery failed to find a valid MDM.  Confirm that the AAD tenant is properly provisioned and licensed for exactly one MDM.  HRESULT = %1\r\n
0xb0000074 | Autopilot Device ESP Domain Controller override was not set.\r\n
0xb0000075 | Autopilot Device ESP Domain Controller override was set by state %1\r\n
0xb0000096 | AutopilotManager started the MSA service for TPM attestation identity.\r\n
0xb0000097 | AutopilotManager started the TPM maintenance task to update TPM attestation.\r\n
0xb0000098 | AutopilotManager reported TPM maintenance task is complete.\r\n
0xb0000099 | AutopilotManager reported the state changed from %1 to %2.\r\n
0xb000009a | AutopilotManager failed to start MSA service.  HRESULT = %1.\r\n
0xb000009b | AutopilotManager failed to start TPM task.  HRESULT = %1.\r\n
0xb000009c | AutopilotManager reported that MSA TPM is not configured for hardware TPM attestation even though the profile indicates it is required.  Autopilot cannot proceed.\r\n
0xb000009d | AutopilotManager reported that TPM attestation lasted %1 microseconds.\r\n
0xb000009e | AutopilotManager reported that TPM enhanced diagnostics logging was enabled for %1 providers.\r\n
0xb00000a0 | AutopilotRetrieveSettings beginning acquisition.\r\n
0xb00000a1 | AutopilotManager retrieve settings succeeded.\r\n
0xb00000a2 | AutopilotManager determined download is not required and the device is not provisioned.  Clean or reset the device to change this.\r\n
0xb00000a3 | AutopilotManager determined download is not required and the device is already provisioned.  Clean or reset the device to change this.\r\n
0xb00000a4 | AutopilotManager determined Internet is available to attempt policy download.\r\n
0xb00000a5 | AutopilotManager determined Internet is not available; policy download will queue when available.\r\n
0xb00000a6 | AutopilotManager reported Internet is now available.\r\n
0xb00000a7 | AutopilotManager reported Internet is still not available.\r\n
0xb00000a8 | AutopilotManager reported MSA TPM device identity was updated.\r\n
0xb00000a9 | AutopilotManager set TPM identity confirmed.\r\n
0xb00000aa | AutopilotManager reported that Autopilot profile download is now complete.\r\n
0xb00000ab | AutopilotManager failed to set TPM identity confirmed.  HRESULT = %1.\r\n
0xb00000ac | AutopilotManager failed to set Autopilot profile as available.  HRESULT = %1.\r\n
0xb00000ad | AutopilotManager failed to register for network availability.  HRESULT = %1.\r\n
0xb00000ae | AutopilotManager failed to register for device identity availability.  HRESULT = %1\r\n
0xb00000af | AutopilotManager failed to register for device identity task update.  HRESULT = %1\r\n
0xb00000b0 | MSA TPM keystate has been updated.  New server state = %1, new client state = %2\r\n
0xb00000b1 | Configuring TPM for attestation.  Current attempt %1 of %2 maximum.\r\n
0xb00000b2 | AutopilotManager began device enrollment with internal state %1.\r\n
0xb00000b3 | AutopilotManager began device enrollment phase %1.\r\n
0xb00000b4 | AutopilotManager failed during device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b5 | AutopilotManager completed device enrollment phase %1.  HRESULT = %2\r\n
0xb00000b6 | AutopilotManager reported that the retry timer event was set to %1 milliseconds.\r\n
0xb00000b7 | AutopilotManager reported that the retry timer event occurred\r\n
0xb00000b8 | AutopilotManager failed to register for MSA keystate update availability.  HRESULT = %1\r\n
0xb00000b9 | AutopilotManager failed to retrieve settings.  HRESULT = %1\r\n
0xb00000ba | AutopilotManager TPM configuration already in progress.\r\n
0xb00000bb | AutopilotManager TPM configuration occurred before retry timer ready.\r\n
0xb00000bd | Configuring TPM exceeded maximum number of attempts.\r\n
0xb00000be | Windows AIK certificate enrollment task was triggered.\r\n
0xb00000bf | Windows TPM maintenance task is being skipped since AIK certificate is already present.\r\n
0xb00000c0 | Autopilot device enrollment failed with error HRESULT = %1. Waiting %2 milliseconds then retrying.%nCurrent attempt %3 of %4.\r\n
0xb00000c1 | Autopilot manager is attempting profile download retry.  Current attempt %1 of %2.\r\n
0xb00000c2 | Autopilot manager will re-attempt the download after %1 milliseconds.\r\n
0xb00000c3 | AutopilotManager began device unenrollment\r\n
0xb00000c4 | AutopilotManager completed device unenrollment.  HRESULT = %1\r\n
0xb00000c5 | AutopilotManager failed device unenrollment.  HRESULT = %1\r\n
0xb00000c8 | Windows AIK object could not be loaded.  HRESULT = %1\r\n
0xb00000c9 | Windows AIK key not found by name.\r\n
0xb00000ca | Windows AIK certificate download failed. HRESULT = %1\r\n
0xb00000cb | Windows AIK alternative load failed. HRESULT = %1\r\n
0xb00000cc | Windows AIK certificate request did not result in a new certificate.\r\n
0xb00000cd | Windows AIK certificate request succeeded and a new certificate is available.\r\n
0xb00000ce | Windows AIK key could not be opened. HRESULT = %1\r\n
0xb00000cf | Windows AIK key failed certificate request. HRESULT = %1\r\n
0xb00000d0 | Windows EK certificate is present.\r\n
0xb00000d1 | Windows EK certificate is not present.\r\n
0xb00000d2 | Windows AIK key was found even though the Windows EK certificate is not present. Attempting to re-initialize the TPM task.\r\n
0xb00000d3 | AutopilotManager reported that a TPM was required but the TPM failed an attestation capability check.  HRESULT = %1\r\n
0xb00000fa | AutopilotManager started AIK certificate acquisition task.\r\n
0xb00000fb | AutopilotManager reported AIK certificate acquisition task returned HRESULT = %1.%nElapsed time: %2 microseconds (maximum allowed time was %3 milliseconds).\r\n
0xb00000fc | AutopilotManager reported AIK key was located.\r\n
0xb00000fd | AutopilotManager reported AIK certificate was located.\r\n
0xb00000fe | AutopilotManager reported AIK certificate was not located.\r\n
0xb000011d | AutopilotManager is determining whether device has internet access.\r\n
0xb000011e | AutopilotManager is determining Autopilot profile availability.\r\n
0xb000011f | Tracking resource type %1. Starting installation of policy provider '%2'.\r\n
0xb0000120 | Tracking resource type %1. Policy provider '%2' installation completed successfully.\r\n
0xb0000121 | Tracking resource type %1. Policy provider '%2' installation timed out after %3 minutes.\r\n
0xb0000122 | Tracking resource type %1. An error occured while installing policy provider '%2'. Error: %3\r\n
0xb0000123 | Tracking resource type %1. Installation of policy provider '%2' not required.\r\n
0xb0000124 | Tracking resource type %1. Retrieving tracking list from policy provider '%2'.\r\n
0xb0000125 | Tracking resource type %1. Policy provider '%2' provided a list of %3 policies to track.\r\n
0xb0000126 | Tracking resource type %1. Policy provider '%2' encountered an error and the tracking list could not be completed. Error: %3\r\n
0xb0000127 | Tracking resource type %1. Policy provider '%2' provided an empty list of policies.\r\n
0xb0000128 | Tracking resource type %1. App '%2' installation completed successfully. \r\n
0xb0000129 | Tracking resource type %1. Starting installation tracking app '%2'.\r\n
0xb000012a | Tracking resource type %1. An error occurred while installing app '%2'.\r\n
0xb000012b | Tracking resource type %1. Reboot required to complete installation of app '%2'.\r\n
0xb000012c | AutopilotManager device enrollment reported an initialization failure.  HRESULT = %1.\r\n
0xb000012d | AutopilotManager device enrollment reported a blocking failure.  Overall error %2, last reported stage %1.\r\n
0xb000012e | AutopilotManager device enrollment failed during stage %1 with error %2.\r\n
0xb000012f | AutopilotManager device enrollment succeeded.  Last valid stage: %1.\r\n
0xb0000136 | Autopilot configuration file path: %1 %nExpanded path:%2\r\n
0xb0000137 | Failed to load Autopilot configuration file, HRESULT = %1.\r\n
0xb0000138 | Failed to parse Autopilot configuration file, HRESULT = %1.\r\n
0xb0000139 | Invalid ZtdCorrelationId found in Autopilot configuration file, HRESULT = %1. ZtdCorrelationId: '%2'.\r\n
0xb000013a | AutopilotManager reported that the Autopilot profile data could not be downloaded. Any Autopilot settings will not be used and the device will not be managed.\r\n
0xb000013b | AutopilotManager failed to record the setting for Autopilot device not managed, HRESULT = %1.\r\n
0xb00001f4 | Invalid data specified in Autopilot policy override configuration.%nHRESULT = %1%nPolicy name: %2.\r\n
0xb00001f5 | AutopilotManager failed to load Json for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f6 | AutopilotManager failed to clear for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f7 | AutopilotManager failed to delete Json for %2.%nHRESULT = %1%nPath: %3.\r\n
0xb00001f8 | AutopilotManager deleted configuration file %1.\r\n
0xb00001f9 | AutopilotManager loaded configuration file %1.\r\n
0xb00001fa | AutopilotManager failed to expand path for %2.%nHRESULT = %1.\r\n
0xb00001fb | AutopilotManager explictly disabled TPM required due to registry setting.\r\n
0xb00001fc | AutopilotManager explictly enabled TPM required due to registry setting.\r\n
0xb00001fd | AutopilotManager enabled TPM requirement due to WhiteGlove policy value %1\r\n
0xb00002bc | Autopilot downloader failed to load override registsry data for %2.%nHRESULT = %1.\r\n
0xb00002bd | Autopilot downloader did not save new profile information because the new profile was empty.\r\n
0xb00002be | Autopilot downloader saved the new profile to %1.\r\n
0xb00002bf | Autopilot downloader retrieved a new profile for %1.\r\n
0xb00002c0 | Autopilot downloader retrieved an empty profile for %1.\r\n
0xb00002c1 | Autopilot downloader cleared the local profile for %1.\r\n
0xb00002c2 | Autopilot downloader failed to download profile for %2.%nHRESULT = %1.%nCorrelation vector: %3\r\n
0xb00002c3 | Autopilot downloader failed to download profile for %2.%nHRESULT = %1.%nCorrelation vector: %3\r\n
0xb00002c4 | Autopilot downloader failed to extract additional error details from response. Response data: %2.%nExtraction failure HRESULT = %1.\r\n
0xb00002c5 | Autopilot failed to download data.  Response code: %1%nDetail message:%n%2\r\n
0xb00002c6 | Autopilot failed to acquire a device ticket for target URL %2.%nHRESULT = %1.\r\n
0xb00002c7 | Autopilot downloader failed to parse target URL:%n%1\r\n
0xb00002c8 | Autopilot downloader failed to convert time %2%nHRESULT = %1.\r\n
0xb00002c9 | Autopilot downloader will use MSA Pre-production environment. This will result in Autopilot failures if production device identities were used.\r\n
0xb00002ca | Autopilot downloader reported a failure acquiring the MSA device ticket. This most likely occurred because MSA and CXH environments do not match (production versus PPE).\r\n
0xb00002ee | Autopilot downloader reported a failure acquiring the MSA device ticket due to certificate errors. This may be caused by the wrong clock time on the machine so a forced time sync will be attempted.\r\n
0xb00002ef | Autopilot downloader reported time sync succeeded.\r\n
0xb00002f0 | Autopilot downloader reported time sync failed with error = %1.\r\n
0xb00002f1 | Autopilot downloader reported that the machine clock is too far off the server time and a forced time sync will be attempted.%nServer time: %1%nClient time: %2%nSync attempt %3 of %4\r\n
0xb00003e8 | Management service starting.\r\n
0xb00003e9 | Management service started.\r\n
0xb00003ea | Management service failed to start.  HRESULT = %1\r\n
0xb00003eb | Management service failed to register.\r\n
0xb00003ec | Management service shutdown.\r\n
0xb00003ed | Management service WIL error was reported.%nHRESULT: %1%nFile: %2, line %3%nMessage: %4\r\n
0xb00003ee | Management service call %1 is deprecated!\r\n
0xb00003ef | Management service cleared the local Autopilot cached state.\r\n
0xb00003f0 | Management service failed to clear the local Autopilot cached state.  HRESULT = %1\r\n
0xb00003f1 | Management InProc Objects WIL error was reported.%nHRESULT: %1%nFile: %2, line %3%nMessage: %4\r\n
0xb000044c | Management service will use %1 for persisted storage\r\n
0xb000044d | Management service did not find %1.  Attempting to create it.\r\n
0xb000044e | Management service created %1.\r\n
0xb000044f | Management service found ProcMon.exe for startup profiling.\r\n
0xb0000450 | Management service determined ProcMon.exe startup profiling is not enabled in the registry.\r\n
0xb0000451 | Management service determined ProcMon.exe startup profiling is enabled in the registry.\r\n
0xb0000452 | Management service is beginning ProcMon.exe startup profiling.\r\n
0xb0000453 | Management service is began ProcMon.exe startup profiling.\r\n
0xb0000454 | Management service is stopping ProcMon.exe startup profiling.\r\n
0xb0000455 | Management service has stopped ProcMon.exe startup profiling.\r\n
0xb00005dc | [Unit Tests] This is a test event string.\r\n
0xb00005dd | [Unit Tests] This is a test CXH event string.\r\n
0xb00005de | [Unit Tests] This is a test Resource event string.\r\n
0xb00005df | Failed to export logs for ETW channel '%2'. [Error Code: %1]\r\n
0xb00005e0 | ETW decoder failed to read next block of events.\r\n
0xb00005e1 | Abstraction of exported ETW record failed.\r\n
0xb00005e2 | An error occurred while extracting the registry value for diagnostic data '%2'. [Error Code: %1]\r\n
0xb00005e3 | Expected channel '%1' could not be found in the EtwProcessingData JSON object.\r\n
0xb00005e4 | Expected EtwProcessingData entry corresponding to event '%1' could not be found.\r\n
0xb00005e5 | Expected diagnostic data '%1' could not be found.\r\n
0xb00005e6 | CXH event was malformed. [Name: '%1']\r\n
0xb00005e7 | Expected required diagnostic data '%1' from the extracted data list was missing some expected data.\r\n
0xb00005e8 | The API executed all actions successfully.\r\n
0xb00005e9 | The API encountered an error at state '%3'. [Error Code: %1]\r\n
0xb00005ea | The expected key '%1' was not found in the '%2' map.\r\n
0xb00005eb | The expected diagnostic data '%1' was missing.\r\n
0xb00005ec | Resource event was malformed. [Event ID: %1, Channel: '%2']\r\n
0xb00005ed | CXH event was missing data. [Event ID: %1, Channel: '%2']\r\n
0xb00005ee | The API is entering the '%1' state.\r\n
0xb00005ef | The API completed the '%1' state successfully.\r\n
0xb00005f0 | The API successfully retrieved the serialized JSON from the '%1' file.\r\n
0xb00005f1 | The API successfully deserialized the '%1' file JSON string.\r\n
0xb00005f2 | The API successfully aggregated the source data.\r\n
0xb00005f3 | The '%1' concurrent worker has begun.\r\n
0xb00005f4 | The '%1' concurrent worker completed successfully.\r\n
0xb00005f5 | An exception occurred while processing diagnostic data. Error code: %1%nTrace:%2\r\n
0xb00005f6 | Diagnostic extraction failed. Error: %1, State: %2\r\n
0xb00005f7 | The localized string for '%1' could not be loaded.\r\n
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
0xd000000e | no key\r\n
0xd000000f | invalid key\r\n
0xd0000010 | software key\r\n
0xd0000011 | unattested key\r\n
0xd0000012 | attested key\r\n
0xd0000013 | revoked\r\n
0xd0000014 | disabled\r\n
0xd0000015 | no key\r\n
0xd0000016 | machine has no capable TPM\r\n
0xd0000017 | machine has a capable TPM\r\n
0xd0000018 | unknown attestation status\r\n
0xd0000019 | no attestation capability\r\n
0xd000001a | temporary attestation failure\r\n
0xd000001b | long-term attestation failure\r\n
0xd000001c | attested key\r\n
