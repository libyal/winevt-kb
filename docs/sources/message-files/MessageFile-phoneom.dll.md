## phoneom.dll

Path: %SystemRoot%\System32\PhoneOm.dll

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb0000001 | [ERROR] originated HRESULT=%1 [%2 @ %3]\r\n
0xb0000002 | [ERROR] propagated HRESULT=%1 [%2 @ %3]\r\n
0xb0000005 | %1\r\n
0xb0000066 | Phone listener endpoint added. Listener: %1 Endpoint: %2\r\n
0xb0000067 | Phone listener add completed. Listener: %1\r\n
0xb0000068 | Phone listener endpoint removed. Listener: %1 Endpoint: %2\r\n
0xb0000069 | Phone listener remove completed. Listener: %1\r\n
0xb000006a | Phone client has called PhoneWaitForAPIReady.\r\n
0xb000006b | PhoneWaitForAPIReady exiting successfully. The API should be ready to be used now.\r\n
0xb00000db | PhoneOM.dll unloading, but Phone API initialize/uninitialize calls mismatched.  InitCount: %1\r\n
0xb00000e0 | Phone listener added.  HPHONELISTENER: %1\r\n
0xb00000e1 | Phone listener removed.  HPHONELISTENER: %1\r\n
0xb00000e2 | Phone listener detected service restart.  HPHONELISTENER: %1\r\n
0xb00000e3 | Phone listener lost notification.  HPHONELISTENER: %1\r\n
0xb00000e4 | Phone listener failed to retrieve notification.  HPHONELISTENER: %1, result: %2\r\n
0xb00000e5 | Phone Api: %1\r\n
0xb00000e6 | Phone Api: %1, call %2\r\n
0xb00000e7 | Phone Api: %1, call %2, call2 %3\r\n
0xb00000e8 | Phone Api: %1, line %2\r\n
0xb00000e9 | Phone Api: Uninitialize without matching initialize, NOP'd\r\n
0xb00000ea | LoadLocalizedAccountFriendlyName: No aumid found for line %1.\r\n
0xd0000001 | PhoneApiInitialize\r\n
0xd0000002 | PhoneApiUninitialize\r\n
0xd0000003 | PhoneIsEmergencyNumber\r\n
0xd0000004 | PhoneGetDefaultOutgoingLine\r\n
0xd0000005 | PhoneIsImmediateDialString\r\n
0xd0000006 | PhoneIsDtmfWaitPending\r\n
0xd0000007 | PhoneExecutePendingDtmfWait\r\n
0xd0000008 | PhoneCallVoicemail\r\n
0xd0000009 | PhoneGetCellularApiComponentInfo\r\n
0xd000000a | PhoneGetVoicemailNumberAndOverrideInfo\r\n
0xd000000b | PhoneInitiateRetrievalOfCIDRestrictionSupport\r\n
0xd000000c | PhoneRefreshCallForwardingState\r\n
0xd000000d | PhoneDial\r\n
0xd000000e | PhoneEnd\r\n
0xd000000f | PhoneSwap\r\n
0xd0000010 | PhoneSetHold\r\n
0xd0000011 | PhoneFlash\r\n
0xd0000012 | PhoneConference\r\n
0xd0000013 | PhonePrivate\r\n
0xd0000014 | PhoneSetMute\r\n
0xd0000015 | PhoneSetSpeaker\r\n
0xd0000016 | PhoneEnableBluetoothHandsFree\r\n
0xd0000017 | PhoneSendDTMF\r\n
0xd0000018 | PhoneSendDTMFStart\r\n
0xd0000019 | PhoneSendDTMFStop\r\n
0xd000001a | PhoneAcceptIncoming\r\n
0xd000001b | PhoneAcceptIncomingEx\r\n
0xd000001c | PhoneDropAccept\r\n
0xd000001d | PhoneDropAcceptEx\r\n
0xd000001e | PhoneExitEmergencyMode\r\n
0xd000001f | PhoneGetCallInfo\r\n
0xd0000020 | PhoneGetCallState\r\n
0xd0000021 | PhoneGetElapsedTime\r\n
0xd0000022 | PhoneGetSpeaker\r\n
0xd0000023 | PhoneGetBluetoothHandsFreeState\r\n
0xd0000024 | PhoneGetWiredHeadsetState\r\n
0xd0000025 | PhoneGetAvailableActions\r\n
0xd0000026 | PhoneIsActionAvailable\r\n
0xd0000027 | PhoneGetState\r\n
0xd0000028 | PhoneGetCallCounts\r\n
0xd0000029 | PhoneGetMute\r\n
0xd000002a | PhoneGetCallsInConference\r\n
0xd000002b | PhoneGetNetworkAlert\r\n
0xd000002c | PhoneMapPlusToDialingPrefix\r\n
0xd000002d | PhoneMapIddPrefixToPlus\r\n
0xd000002e | PhoneGetAssistedDialNumber\r\n
0xd000002f | PhoneGetAssistedDialSetting\r\n
0xd0000030 | PhoneAddListener\r\n
0xd0000031 | PhoneRemoveListener\r\n
0xd0000032 | PhoneStartVisualVoicemailSync\r\n
0xd0000033 | PhoneSaveVvmPassword\r\n
0xd0000034 | PhoneSupportsLocalVvmConfig\r\n
0xd0000035 | PhoneBeginVvmAudio\r\n
0xd0000036 | PhoneEndVvmAudio\r\n
0xd0000037 | PhoneClearIdleCallsFromController\r\n
0xd0000038 | PhoneSimUnlock\r\n
0xd0000039 | PhoneSimUnlockDebug\r\n
0xd000003a | PhoneSimEnablePinLock\r\n
0xd000003b | PhoneSimDisablePinLock\r\n
0xd000003c | PhoneSimChangePin\r\n
0xd000003d | PhoneSimUIClosed\r\n
0xd000003e | PhoneSimGetPin2\r\n
0xd000003f | PhoneSimChangePin2\r\n
0xd0000040 | PhoneSimNotifyPin2Available\r\n
0xd0000041 | PhoneFormatPhoneNumber\r\n
0xd0000042 | PhoneIsVvmSetupComplete\r\n
0xd0000043 | PhoneMarkVvmSetupComplete\r\n
0xd0000044 | PhoneSpamFilteringEnabled\r\n
0xd0000045 | PhoneReinitiateCallerIdLookup\r\n
0xd0000046 | PhoneGetPreferredCallUpgradeLine\r\n
0xd0000047 | PhoneInitiateCallUpgrade\r\n
0xd0000048 | PhoneRejectIncoming\r\n
0xd0000049 | PhoneIsVoiceRoamingRestrictionActive\r\n
0xd000004a | PhoneSetForegroundLine\r\n
0xd000004b | PhoneGetAggregateBranding\r\n
0xd000004c | PhoneGetBrandingText\r\n
0xd000004d | PhoneSetPreferredCallUpgradeLine\r\n
0xd000004e | PhoneSetReminderInfo\r\n
0xd000004f | PhoneWaitSimSecurityReady\r\n
0xd0000050 | PhoneConfirmNonSeamlessUpgrade\r\n
0xd0000051 | PhoneCancelNonSeamlessUpgrade\r\n
0xd0000052 | PhoneSetLocalVideo\r\n
0xd0000053 | PhoneAddVideo\r\n
0xd0000054 | PhoneDropVideo\r\n
0xd0000055 | PhoneAcceptVideo\r\n
0xd0000056 | PhoneRejectVideo\r\n
0xd0000057 | PhoneSetVideoPaused\r\n
0xd0000058 | PhoneModifyVideoCallingSetting\r\n
0xd0000059 | PhoneRefreshVideoCallingSetting\r\n
0xd000005a | PhoneIsVideoCallingSwitchActionable\r\n
0xd000005b | PhoneIsVideoCallingEnabled\r\n
0xd000005c | PhoneGetLinePublicInfo\r\n
0xd000005d | PhonePublicDial\r\n
0xd000005e | PhoneSetCallOriginInfo\r\n
0xd000005f | PhoneIsPhoneNumberInBlockList\r\n
0xd0000060 | PhoneSetSpecificTypeActiveApp\r\n
0xd0000061 | PhoneGetSpecificTypeActiveApp\r\n
0xd0000062 | PhoneGetSpecificTypeAppList\r\n
0xd0000063 | PhoneSetActiveSpamFilterApp\r\n
0xd0000064 | PhoneGetActiveSpamFilterApp\r\n
0xd0000065 | PhoneHandleAppUninstallByType\r\n
0xd0000066 | PhoneStartRecording\r\n
0xd0000067 | PhonePauseRecording\r\n
0xd0000068 | PhoneFinishRecording\r\n
0xd0000069 | PhoneGetVideoCapabilities\r\n
0xd000006a | PhoneSetBlockPrivateNumbersSetting\r\n
0xd000006b | PhoneGetBlockPrivateNumbersSetting\r\n
0xd000006c | PhoneSetBlockUnknownNumbersSetting\r\n
0xd000006d | PhoneGetBlockUnknownNumbersSetting\r\n
0xd000006e | PhoneSetFilerAppBlockList\r\n
0xd000006f | PhoneGetLinePublicSettings\r\n
0xd0000070 | PhoneRefreshEcbmState\r\n
0xd0000071 | PhoneGetVideoCapabilitySharingSettings\r\n
0xd0000072 | PhoneSetVideoCapabilitySharingSettings\r\n
0xd0000073 | PhoneGetDeviceSupportsVideoCalling\r\n
0xd0000074 | PhoneGetRecordingApplications\r\n
0xd0000075 | PhoneSetRecordingApplication\r\n
0xd0000076 | PhoneGetShouldMuteKeypad\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb0000001 | [ERROR] originated HRESULT=%1 [%2 @ %3]\r\n
0xb0000002 | [ERROR] propagated HRESULT=%1 [%2 @ %3]\r\n
0xb0000005 | %1\r\n
0xb0000066 | Phone listener endpoint added. Listener: %1 Endpoint: %2\r\n
0xb0000067 | Phone listener add completed. Listener: %1\r\n
0xb0000068 | Phone listener endpoint removed. Listener: %1 Endpoint: %2\r\n
0xb0000069 | Phone listener remove completed. Listener: %1\r\n
0xb000006a | Phone client has called PhoneWaitForAPIReady.\r\n
0xb000006b | PhoneWaitForAPIReady exiting successfully. The API should be ready to be used now.\r\n
0xb00000db | PhoneOM.dll unloading, but Phone API initialize/uninitialize calls mismatched.  InitCount: %1\r\n
0xb00000e0 | Phone listener added.  HPHONELISTENER: %1\r\n
0xb00000e1 | Phone listener removed.  HPHONELISTENER: %1\r\n
0xb00000e2 | Phone listener detected service restart.  HPHONELISTENER: %1\r\n
0xb00000e3 | Phone listener lost notification.  HPHONELISTENER: %1\r\n
0xb00000e4 | Phone listener failed to retrieve notification.  HPHONELISTENER: %1, result: %2\r\n
0xb00000e5 | Phone Api: %1\r\n
0xb00000e6 | Phone Api: %1, call %2\r\n
0xb00000e7 | Phone Api: %1, call %2, call2 %3\r\n
0xb00000e8 | Phone Api: %1, line %2\r\n
0xb00000e9 | Phone Api: Uninitialize without matching initialize, NOP'd\r\n
0xb00000ea | LoadLocalizedAccountFriendlyName: No aumid found for line %1.\r\n
0xd0000001 | PhoneApiInitialize\r\n
0xd0000002 | PhoneApiUninitialize\r\n
0xd0000003 | PhoneIsEmergencyNumber\r\n
0xd0000004 | PhoneGetDefaultOutgoingLine\r\n
0xd0000005 | PhoneIsImmediateDialString\r\n
0xd0000006 | PhoneIsDtmfWaitPending\r\n
0xd0000007 | PhoneExecutePendingDtmfWait\r\n
0xd0000008 | PhoneCallVoicemail\r\n
0xd0000009 | PhoneGetCellularApiComponentInfo\r\n
0xd000000a | PhoneGetVoicemailNumberAndOverrideInfo\r\n
0xd000000b | PhoneInitiateRetrievalOfCIDRestrictionSupport\r\n
0xd000000c | PhoneRefreshCallForwardingState\r\n
0xd000000d | PhoneDial\r\n
0xd000000e | PhoneEnd\r\n
0xd000000f | PhoneSwap\r\n
0xd0000010 | PhoneSetHold\r\n
0xd0000011 | PhoneFlash\r\n
0xd0000012 | PhoneConference\r\n
0xd0000013 | PhonePrivate\r\n
0xd0000014 | PhoneSetMute\r\n
0xd0000015 | PhoneSetSpeaker\r\n
0xd0000016 | PhoneEnableBluetoothHandsFree\r\n
0xd0000017 | PhoneSendDTMF\r\n
0xd0000018 | PhoneSendDTMFStart\r\n
0xd0000019 | PhoneSendDTMFStop\r\n
0xd000001a | PhoneAcceptIncoming\r\n
0xd000001b | PhoneAcceptIncomingEx\r\n
0xd000001c | PhoneDropAccept\r\n
0xd000001d | PhoneDropAcceptEx\r\n
0xd000001e | PhoneExitEmergencyMode\r\n
0xd000001f | PhoneGetCallInfo\r\n
0xd0000020 | PhoneGetCallState\r\n
0xd0000021 | PhoneGetElapsedTime\r\n
0xd0000022 | PhoneGetSpeaker\r\n
0xd0000023 | PhoneGetBluetoothHandsFreeState\r\n
0xd0000024 | PhoneGetWiredHeadsetState\r\n
0xd0000025 | PhoneGetAvailableActions\r\n
0xd0000026 | PhoneIsActionAvailable\r\n
0xd0000027 | PhoneGetState\r\n
0xd0000028 | PhoneGetCallCounts\r\n
0xd0000029 | PhoneGetMute\r\n
0xd000002a | PhoneGetCallsInConference\r\n
0xd000002b | PhoneGetNetworkAlert\r\n
0xd000002c | PhoneMapPlusToDialingPrefix\r\n
0xd000002d | PhoneMapIddPrefixToPlus\r\n
0xd000002e | PhoneGetAssistedDialNumber\r\n
0xd000002f | PhoneGetAssistedDialSetting\r\n
0xd0000030 | PhoneAddListener\r\n
0xd0000031 | PhoneRemoveListener\r\n
0xd0000032 | PhoneStartVisualVoicemailSync\r\n
0xd0000033 | PhoneSaveVvmPassword\r\n
0xd0000034 | PhoneSupportsLocalVvmConfig\r\n
0xd0000035 | PhoneClearIdleCallsFromController\r\n
0xd0000036 | PhoneSimUnlock\r\n
0xd0000037 | PhoneSimUnlockDebug\r\n
0xd0000038 | PhoneSimEnablePinLock\r\n
0xd0000039 | PhoneSimDisablePinLock\r\n
0xd000003a | PhoneSimChangePin\r\n
0xd000003b | PhoneSimUIClosed\r\n
0xd000003c | PhoneSimGetPin2\r\n
0xd000003d | PhoneSimChangePin2\r\n
0xd000003e | PhoneSimNotifyPin2Available\r\n
0xd000003f | PhoneFormatPhoneNumber\r\n
0xd0000040 | PhoneIsVvmSetupComplete\r\n
0xd0000041 | PhoneMarkVvmSetupComplete\r\n
0xd0000042 | PhoneSpamFilteringEnabled\r\n
0xd0000043 | PhoneReinitiateCallerIdLookup\r\n
0xd0000044 | PhoneGetPreferredCallUpgradeLine\r\n
0xd0000045 | PhoneInitiateCallUpgrade\r\n
0xd0000046 | PhoneRejectIncoming\r\n
0xd0000047 | PhoneIsVoiceRoamingRestrictionActive\r\n
0xd0000048 | PhoneSetForegroundLine\r\n
0xd0000049 | PhoneGetAggregateBranding\r\n
0xd000004a | PhoneGetBrandingText\r\n
0xd000004b | PhoneSetPreferredCallUpgradeLine\r\n
0xd000004c | PhoneSetReminderInfo\r\n
0xd000004d | PhoneWaitSimSecurityReady\r\n
0xd000004e | PhoneConfirmNonSeamlessUpgrade\r\n
0xd000004f | PhoneCancelNonSeamlessUpgrade\r\n
0xd0000050 | PhoneSetLocalVideo\r\n
0xd0000051 | PhoneAddVideo\r\n
0xd0000052 | PhoneDropVideo\r\n
0xd0000053 | PhoneAcceptVideo\r\n
0xd0000054 | PhoneRejectVideo\r\n
0xd0000055 | PhoneSetVideoPaused\r\n
0xd0000056 | PhoneModifyVideoCallingSetting\r\n
0xd0000057 | PhoneRefreshVideoCallingSetting\r\n
0xd0000058 | PhoneIsVideoCallingSwitchActionable\r\n
0xd0000059 | PhoneIsVideoCallingEnabled\r\n
0xd000005a | PhoneGetLinePublicInfo\r\n
0xd000005b | PhonePublicDial\r\n
0xd000005c | PhoneSetCallOriginInfo\r\n
0xd000005d | PhoneIsPhoneNumberInBlockList\r\n
0xd000005e | PhoneSetSpecificTypeActiveApp\r\n
0xd000005f | PhoneGetSpecificTypeActiveApp\r\n
0xd0000060 | PhoneGetSpecificTypeAppList\r\n
0xd0000061 | PhoneSetActiveSpamFilterApp\r\n
0xd0000062 | PhoneGetActiveSpamFilterApp\r\n
0xd0000063 | PhoneHandleAppUninstallByType\r\n
0xd0000064 | PhoneStartRecording\r\n
0xd0000065 | PhonePauseRecording\r\n
0xd0000066 | PhoneFinishRecording\r\n
0xd0000067 | PhoneGetVideoCapabilities\r\n
0xd0000068 | PhoneSetBlockPrivateNumbersSetting\r\n
0xd0000069 | PhoneGetBlockPrivateNumbersSetting\r\n
0xd000006a | PhoneSetBlockUnknownNumbersSetting\r\n
0xd000006b | PhoneGetBlockUnknownNumbersSetting\r\n
0xd000006c | PhoneSetFilerAppBlockList\r\n
0xd000006d | PhoneGetLinePublicSettings\r\n
0xd000006e | PhoneRefreshEcbmState\r\n
0xd000006f | PhoneGetVideoCapabilitySharingSettings\r\n
0xd0000070 | PhoneSetVideoCapabilitySharingSettings\r\n
0xd0000071 | PhoneGetDeviceSupportsVideoCalling\r\n
0xd0000072 | PhoneGetRecordingApplications\r\n
0xd0000073 | PhoneSetRecordingApplication\r\n
0xd0000074 | PhoneGetShouldMuteKeypad\r\n
0xd0000075 | PhoneExplicitCallTransfer\r\n
0xd0000076 | PhoneMarkDataAffinityNotificationSeen\r\n
0xd0000077 | PhoneCallCapabilityAccessCheck\r\n
0xd0000078 | PhoneSetCallerAsActiveAppByType\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0xb0000001 | [ERROR] originated HRESULT=%1 [%2 @ %3]\r\n
0xb0000002 | [ERROR] propagated HRESULT=%1 [%2 @ %3]\r\n
