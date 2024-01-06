## phoneservice.dll

Path: %SystemRoot%\System32\PhoneService.dll

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
0xb000000a | %1\r\n
0xb0000064 | The Phone service is starting\r\n
0xb0000065 | The Phone service has started\r\n
0xb0000066 | The Phone service failed to start with error %1\r\n
0xb0000067 | The Phone service is stopping\r\n
0xb0000068 | The Phone service has stopped\r\n
0xb0000258 | PH_MSG: %1 with supsvc code or SIM error: %2\r\n
0xb0000259 | USSD Message: %1 suppressed due to emergency call\r\n
0xb000025a | PhoneService: Phone RPC server started. Setting PhoneApiReady.\r\n
0xb000025b | PhoneService: Stopping Phone RPC server.\r\n
0xb00002bc | CallState Change for callId: %1, from %2 to %3\r\n
0xb00002be | Controller request to provider %1: verb %2 id: %3 hr: %4\r\n
0xb00002bf | Controller request result from provider %1: verb %2 id: %3 hr: %4\r\n
0xb00002c0 | Dialing: Got call handle from provider\r\n
0xb00002c1 | Dialing: Failed due to existing outgoing call\r\n
0xb00002c2 | Phone dialing %1\r\n
0xb00002c4 | Fake Call Added: %1\r\n
0xb00002c8 | Controller added call history record with Oid: %1 hr %2\r\n
0xb00002c9 | Dialing rules start\r\n
0xb00002ca | Dialing rules end: modified by rule %1, rule processing time %2 ms.\r\n
0xb00002cb | Dialing: Failed because there are already two calls.\r\n
0xb00002cc | Dialing: Failed because the active call cannot be held.\r\n
0xb00002cd | Controller holding call %1 to accept call %2.\r\n
0xb00002ce | Controller dropping held call %1 to accept call %2.\r\n
0xb00002cf | Controller using DropAccept for incoming, dropping call %1 to accept %2.\r\n
0xb00002d0 | [CellularAudio] Setting audio endpoint to %1\r\n
0xb00002d1 | [CellularAudio] Notified of audio routing endpoint change to %1\r\n
0xb00002d2 | [CellularAudio] Notified of bluetooth state change to %1\r\n
0xb00002d3 | [CellularAudio] Enabling phone call audio to endpoint %1; IsIncoming %2\r\n
0xb00002d4 | [CellularAudio] Disabling phone call audio\r\n
0xb00002d6 | Phone service failed to initialize UDM or CallHistoryItemWriter.  Call history entries will not be written.  HRESULT: %1\r\n
0xb00002d7 | Phone service failed to initialize External VVM manager.  VVM apps will not be able to control audio. HRESULT: %1\r\n
0xb00002d8 | Phone service failed to initialize POOM.  Caller ID information will not be available. HRESULT: %1\r\n
0xb00002d9 | [CellularAudio] Tone Notification: %1, digits %2, on %3, off %4\r\n
0xb00002da | Controller OnFinished called for requestId %1 hr: %2\r\n
0xb00002db | Rejected incoming call. Line id: %1 Call Id: %2 reason: %3 \r\n
0xb00002dc | [CellularAudio] Enabling cellular audio: %1 on executor %2\r\n
0xb00002dd | [CellularAudio] Disabling cellular audio: %1 on executor %2\r\n
0xb00002de | VOIP audio count ref increased\r\n
0xb00002df | VOIP audio count ref Decreased\r\n
0xb00002e0 | VOIP muting audio\r\n
0xb00002e1 | VOIP unmuting audio\r\n
0xb00002e2 | PhoneController - phone line added. id: %1, type: %2\r\n
0xb00002e3 | PhoneController - phone line removed. id: %1\r\n
0xb00002e4 | PhoneController - line property: %2 value: %3 for line ID:%1\r\n
0xb00002e6 | [CellularAudio] ExecutorIndex: %1 already initialized for audio\r\n
0xb00002e7 | [CellularAudio] Muting cellular TX audio: %1 on executor %2, muted: %3\r\n
0xb00002e8 | [CellularAudio] Muting cellular RX audio: %1 on executor %2, muted: %3\r\n
0xb00002e9 | EndUpgradeOriginationCall invoked for upgrade guid %1\r\n
0xb00002ea | CancelUpgrade invoked for upgrade guid %1\r\n
0xb00002eb | [CellularAudio] Enabling cellular provider change, [executorIndex=%1][cellularAudioType=%2][operation=%3]\r\n
0xb00002ec | [CellularAudio] Invalid cellular provider change attempted, [executorIndex=%1][targetAudioType=%2][operation=%3][currentAudioType=%4][isInHandover=%5]\r\n
0xb00002ed | [CellularAudio] Handover in progress, cellular audio type change not allowed [executorIndex=%1][cellularAudioType=%2][audioActive=%3]\r\n
0xb00002ee | Phone call swap was ignored. Call to hold: %1. Call to unhold: %2.\r\n
0xb00002ef | Calculation for time between call swaps was completed. Allow swap is %1. Last successful swap was %2 ms ago. The device is configured to wait at least %3 ms in between swaps.\r\n
0xb00002f0 | CallProgress - Determined sound configuration according to country code, [LineId=%1][CountryCode=%2][EventSndBusy=%3][EventSndRingback=%4]\r\n
0xb00002f1 | Disable and enable cellular audio. Disable Executor Index: %1, Enable Executor Index: %2, Cellular Audio Type: %3, Audio Active: %4\r\n
0xb0000384 | Event sound: %1\r\n
0xb0000418 | Emergency Number: received updated list %1\r\n
0xb0000419 | Emergency Number: Dial request for callid %1\r\n
0xb000041a | Emergency Number list received null argument or empty list.\r\n
0xb000041b | Dialing: Failed because the line attempt to dial is not free.\r\n
0xb000041c | OperationWatchdog: "%1" timed out.  Context: %2.  Timeout value: %3ms.  Still waiting after: %4ms.\r\n
0xb000041d | OperationWatchdog: "%1" completed.  Context: %2.  Actual time: %3ms\r\n
0xb000041e | Async API context %1 completed with result %2\r\n
0xb000041f | Phone service listener added: %1\r\n
0xb0000420 | Phone service listener removed: %1\r\n
0xb0000421 | Phone service listener lost notifications: %1\r\n
0xb0000423 | Phone service listener rundown: %1\r\n
0xb0000424 | Phone notification sent: %1 error: %2\r\n
0xb0000429 | Call Upgrade state for CallId: %1 Changed From: %2 To: %3\r\n
0xb000042a | Data Connectivity State: %1\r\n
0xb000042d | Non-seamless upgrade was cancelled by the user.\r\n
0xb000042e | Seamless upgrade was cancelled by the user.\r\n
0xb000042f | Connection Manager Error. Connection Manager Result: %1.\r\n
0xb0000430 | Call Line Change for CallId: %1 from LineId: %2 to LineId: %3\r\n
0xb0000432 | PhoneTileManager: Creating secondary Phone Tile with id: %1\r\n
0xb0000433 | PhoneTileManager: Setting the primary Phone Tile to be assigned to PhoneLineId: %1\r\n
0xb0000434 | PhoneTileManager: Deleting Phone Tile with id: %1\r\n
0xb0000436 | PhoneTile: Committed an update to the Phone Tile with tile id: %1. Title %2; Tile mode: %3; has voicemail: %4; missed call count: %5; has large content: %6\r\n
0xb0000438 | PhoneTileControllerSink: The PhoneLine (%1) has been removed.  Removing its tile and updating any remaining tiles as necessary.\r\n
0xb000043f | PhoneTileControllerSink: ShellReadyState changed to %1\r\n
0xb0000440 | SystemEventTriggerControllerSink: LineChangedTrigger fired with: LineId %1: PhoneLineChangeKind %2: PhoneLineProperties: %3: hr: %4\r\n
0xb0000441 | SystemEventTriggerControllerSink: NewVoicemailMessageTrigger fired with: LineId %1: voicemailCount %2: VoicemailMessage: %3: hr: %4\r\n
0xb0000442 | SystemEventTriggerControllerSink: CallOriginDataRequestTrigger fired with: RequestId %1: PhoneNumber: %2: hr: %3\r\n
0xb0000443 | SystemEventTriggerControllerSink: CallHistoryChanged fired with: hr: %1\r\n
0xb0000444 | SystemEventTriggerControllerSink: AirplaneModeDisabledForEmergencyCall fired with: hr: %1\r\n
0xb0000445 | SystemEventTriggerControllerSink: OnCallEvent called with: event: %1\r\n
0xb0000446 | SystemEventTriggerControllerSink: Attempted to advise to CallHistorySession with: hr: %1\r\n
0xb0000447 | IR94FeatureDisabled: Returning video capability sharing as disabled.\r\n
0xb0000448 | IR94FeatureDisabled: Returning device not video capable.\r\n
0xb0000449 | IR94FeatureDisabled: Returning video calling switch as not actionable.\r\n
0xb000044a | SystemEventTriggerControllerSink: LineChangedTrigger suppressed [LineId=%1][PhoneLineChangeKind=%2][PhoneLineProperties=%3]\r\n
0xb000044b | SystemEventTriggerControllerSink: Received shell ready notification.\r\n
0xb000044c | SystemEventTriggerControllerSink: OnShellReady started [existingInitialBootSequenceComplete=%1][cachedLineCount=%2]\r\n
0xb000044d | SystemEventTriggerControllerSink: OnShellReady triggering deferred notification [LineId=%1][PhoneLineChangeKind=%2][PhoneLineProperties=%3]\r\n
0xb00004b1 | InteractiveUserNotificationSink: New Incoming Call State Changed [callId=%1].\r\n
0xb00004b2 | InteractiveUserNotificationSink: Show Incoming Call Toast [callId=%1].\r\n
0xb00005dd | Call data collection item added for CallId: [%1]\r\n
0xb00005de | Call data collection item removed for CallId: [%1]\r\n
0xb00005df | Call data collection item dropped an idle call for CallId: [%1]\r\n
0xb00005e0 | CallHistoryItemWriter: Call with id %1 is added.\r\n
0xb00005e1 | CallHistoryItemWriter: Call with id %1 is updated.\r\n
0xb00005e2 | CallAnnotationsLookupConnecting: Establishing RPC connection.  Endpoint: %1\r\n
0xb00005e3 | CallAnnotationsLookup: Querying location.  Phone number: %1\r\n
0xb00005e4 | CallAnnotationsLookup: Completed location query.  Location: %1\r\n
0xb00005e5 | CallAnnotationsLookup: RPC failure, clearing RPC connection.\r\n
0xb00005e6 | CallAnnotationsManager: Call: %1 LookupState: %2\r\n
0xb00005e7 | Shutting down Phone service due to idle stop.\r\n
0xb00005e8 | Service Idle Callback received. Idle status: %1, Phone calls exist: %2\r\n
0xb00005e9 | CallRecording VALID state change from '%2' to '%3' on executor %1\r\n
0xb00005ea | CallRecording: INVALID state change from '%2' to '%3' on executor %1\r\n
0xb00005eb | CallRecording: Recorded call is now idle.  Recording will end.  LineId:%1, CallId:%2, ConferenceCallId:%3\r\n
0xb00005ec | CallRecording: Recorded call is now held.  Recording will pause and may finish.  LineId:%1, CallId:%2, ConferenceCallId:%3\r\n
0xb00005ed | CallRecording: A call that is not being recorded is talking.  Recording will finish.  LineId:%1, CallId:%2, ConferenceCallId:%3\r\n
0xb00005ee | CallRecording: Recorded call no longer exists.  Recording will finish.  LineId:%2, CallId:%1\r\n
0xb00005ef | CallRecording: Preferred recording application changed.  Old Package Family Name: '%1', New Package Family Name: '%2'\r\n
0xb00005f0 | Call [callId=%1] marked as handover merged due to being conferenced with call [callState=%2] that ended with handover merged reason\r\n
0xb0000640 | [RcsPresence] Request Capabilities: %1\r\n
0xb0000641 | [RcsPresence] Received query response, [responseCode=%1][reason=%2]\r\n
0xb0000642 | [RcsPresence] Received %1 capability tuple(s)\r\n
0xb0000643 | [RcsPresence] Tuple %1, MediaType not video capable: %2\r\n
0xb0000644 | [RcsPresence] Tuple %1, ServiceIdentifier not video capable: %2\r\n
0xb0000645 | [RcsPresence] Tuple %1 is video capable.\r\n
0xb0000646 | [RcsPresence] RcsPresenceCache hit, [TelUri string=%1][Capabilities returned=%2]\r\n
0xb0000647 | [RcsPresence] Query suppressed due to capabilities sharing opt-in settings, [TelUri string=%1][Capabilities returned=%2]\r\n
0xb0000648 | Checking for device support of video calling. This service (%1) exists, thus video calling is supported.\r\n
0xb0000649 | Checking for device support of video calling. This service (%2) does NOT exist due to error code %1, thus a different service would have to exist for video calling to be supported.\r\n
0xb000064a | PhoneController - Updating video calling settings, [lineId=%1][videoCallingSetting=%2][cacheVideoCallingSetting=%3][userRequest=%4][TTYEnabled=%5][cellularDataEnabled=%6]\r\n
0xb000064b | CallRecording: Deferred request to disable cellular audio: %1 on executor %2\r\n
0xb000064c | CallRecording: Cancelled request to defer disabling of cellular audio: %3 due to enabling of: %1 on executor %2\r\n
0xb000064d | CallRecording: An audio type change prevented deferring of audio disable.  New audio type: %1, Audio type being disabled: %3 on executor %2\r\n
0xb000064e | CallRecording: Performing deferred request to disable cellular audio: %1 on executor %2\r\n
0xb000064f | [RcsPresence] Received OnPublishRequested\r\n
0xb0000650 | [RcsPresence] Suppressed publishing actual video capability as UCE capability sharing is disabled.\r\n
0xb0000651 | [RcsPresence] Video capability sharing settings update requested [isCapabilitySharingEnabled=%1][previousValue=%2].\r\n
0xb0000652 | [RcsPresence] Cache initialized [cacheExpirationInSeconds=%1]\r\n
0xb0000653 | [RcsPresence] Publishing capabilities [%1]\r\n
0xb0000654 | [RcsPresence] Initializing RCS presence service\r\n
0xb0000655 | [RcsPresence] RCS presence service status queried, [status=%1]\r\n
0xb0000656 | [RcsPresence] Starting RCS presence service\r\n
0xb0000657 | [RcsPresence] Received publish response, [responseCode=%1][reason=%2]\r\n
0xb0000658 | [RcsPresence] Received OnNetworkSupportVideoChanged, [updatedValue=%1][previousValue=%2]\r\n
0xb0000659 | [RcsPresence] Saved last published capabilities, [updatedValue=%1][previousValue=%2]\r\n
0xd0000001 | PH_CALLSTATE_AMBIGUOUS\r\n
0xd0000002 | PH_CALLSTATE_INCOMING\r\n
0xd0000003 | PH_CALLSTATE_CALLING\r\n
0xd0000004 | PH_CALLSTATE_TALKING\r\n
0xd0000005 | PH_CALLSTATE_HOLD\r\n
0xd0000006 | PH_CALLSTATE_IDLE\r\n
0xd0000007 | PH_CALLSTATE_TRANSFERRING\r\n
0xd0000008 | RejectIncomingReason_UserRequest\r\n
0xd0000009 | RejectIncomingReason_OtherIncomingCall\r\n
0xd000000a | RejectIncomingReason_EmergencyMode\r\n
0xd000000b | RejectIncomingReason_Filtered\r\n
0xd000000c | PH_MSG_SIMPHONEBOOKENTRY\r\n
0xd000000d | PH_MSG_SUPSVCEXECUTING\r\n
0xd000000e | PH_MSG_SUPSVCSUCCEEDED\r\n
0xd000000f | PH_MSG_SUPSVCFAILED\r\n
0xd0000010 | PH_MSG_USSDEXECUTING\r\n
0xd0000011 | PH_MSG_USSDEXECUTED_FURTHER_INFO_REQUIRED\r\n
0xd0000012 | PH_MSG_USSDEXECUTED_NO_FURTHER_INFO_REQUIRED\r\n
0xd0000013 | PH_MSG_CALLEE_INCOMING_CALLS_BARRED\r\n
0xd0000014 | PH_MSG_VOICEMAIL\r\n
0xd0000015 | PH_MSG_MISSEDCALL\r\n
0xd0000016 | PH_MSG_SPEAKERPHONEON\r\n
0xd0000017 | PH_MSG_SERVICEAUTOENABLED\r\n
0xd0000018 | PH_MSG_CURRENTLY_IN_ECBM\r\n
0xd0000019 | PH_MSG_ECBMIDLE\r\n
0xd000001a | PH_MSG_NOT_CURRENTLY_IN_ECBM\r\n
0xd000001b | PH_MSG_ERRORCALLDROPPED\r\n
0xd000001c | PH_MSG_ERRORNETWORKDROPPED\r\n
0xd000001d | PH_MSG_ERRORINVALIDDESTADDRESS\r\n
0xd000001e | PH_MSG_ERRORNOTADMIN\r\n
0xd000001f | PH_MSG_ERRORCONFERENCEFAILED\r\n
0xd0000020 | PH_MSG_ERRORVOICEMAILSWITCHLINES\r\n
0xd0000021 | PH_MSG_ERROREND\r\n
0xd0000022 | PH_MSG_ERRORPRIVATE\r\n
0xd0000023 | PH_MSG_ERRORANSWER\r\n
0xd0000024 | PH_MSG_ERRORFLASH\r\n
0xd0000025 | PH_MSG_ERRORHOLD\r\n
0xd0000026 | PH_MSG_ERRORSWAP\r\n
0xd0000027 | PH_MSG_ERRORUNHOLD\r\n
0xd0000028 | PH_MSG_ERRORMUTE\r\n
0xd0000029 | PH_MSG_ERRORUNMUTE\r\n
0xd000002a | PH_MSG_ERRORDIAL\r\n
0xd000002b | PH_MSG_ERRORNODIALTONE\r\n
0xd000002c | PH_MSG_ERRORUNREACHABLE\r\n
0xd000002d | PH_MSG_ERRORBADADDRESS\r\n
0xd000002e | PH_MSG_ERRORSIMBUSY\r\n
0xd000002f | PH_MSG_ERRORNETWORKSERVICENOTAVAILABLE\r\n
0xd0000030 | PH_MSG_ERROREMERGENCYONLY\r\n
0xd0000031 | PH_MSG_ERRORRADIOOFF\r\n
0xd0000032 | PH_MSG_ERROROPERATIONFAILED\r\n
0xd0000033 | PH_MSG_ERROROUTGOINGCALLNOFREELINES\r\n
0xd0000034 | PH_MSG_ERRORNOVMAILNUMBER\r\n
0xd0000035 | PH_MSG_ERRORTRANSFER\r\n
0xd0000036 | PH_MSG_SIMSECNEEDED\r\n
0xd0000037 | PH_MSG_EXT\r\n
0xd0000038 | PH_MSG_ERRORDESTINATIONBARRED\r\n
0xd0000039 | PH_MSG_ERRORFDNRESTRICT\r\n
0xd000003a | PH_MSG_ERRORDTMF\r\n
0xd000003b | PH_MSG_ERRORCHLD1\r\n
0xd000003c | PH_MSG_ERRORCALLFORWARDRETRIEVE\r\n
0xd000003d | PH_MSG_ERRORCALLFORWARDAPPLY\r\n
0xd000003e | PH_MSG_DISMISSSUPSVCS\r\n
0xd000003f | PH_MSG_SIMUNLOCK\r\n
0xd0000040 | PH_MSG_ERRORROAMRESTRICT\r\n
0xd0000041 | PH_MSG_SEAMLESS_UPGRADE\r\n
0xd0000042 | PH_MSG_UPGRADE_ERROR\r\n
0xd0000043 | PH_MSG_ERRORDISABLELOCALVIDEO\r\n
0xd0000044 | PH_MSG_ERRORENABLELOCALVIDEO\r\n
0xd0000045 | PH_MSG_ERRORADDVIDEO\r\n
0xd0000046 | PH_MSG_ERRORDROPVIDEO\r\n
0xd0000047 | PH_MSG_ERRORACCEPTVIDEO\r\n
0xd0000048 | PH_MSG_ERRORREJECTVIDEO\r\n
0xd0000049 | PH_MSG_ERRORSETVIDEOPAUSED\r\n
0xd000004a | PH_MSG_ERRORVIDEOCALLINGOFF\r\n
0xd000004b | PH_MSG_VOIP_INSTALL_PROMPT\r\n
0xd000004c | PH_MSG_ERRORSTARTRECORDING\r\n
0xd000004d | PH_MSG_ERRORPAUSERECORDING\r\n
0xd000004e | PH_MSG_ERRORSTOPRECORDING\r\n
0xd000004f | PH_MSG_VIDEOCHARGESPROMPT\r\n
0xd0000050 | PH_MSG_LAST\r\n
0xd0000051 | PhoneCallAudio_DefaultEndpointPerRoutingPolicy\r\n
0xd0000052 | PhoneCallAudio_Speakerphone\r\n
0xd0000053 | PhoneCallAudio_Handset\r\n
0xd0000054 | PhoneCallAudio_WiredHeadset\r\n
0xd0000055 | PhoneCallAudio_WiredHeadsetWithMicrophone\r\n
0xd0000056 | PhoneCallAudio_BluetoothSco\r\n
0xd0000057 | PhoneCallAudio_BluetoothScoWithNREC\r\n
0xd0000058 | PhoneTone_None\r\n
0xd0000059 | PhoneTone_Off\r\n
0xd000005a | PhoneTone_DTMF_Start\r\n
0xd000005b | PhoneTone_DTMF_Stop\r\n
0xd000005c | PhoneTone_DTMF_Burst\r\n
0xd000005d | PhoneTone_3GPP_RingBack\r\n
0xd000005e | PhoneTone_3GPP2_Reorder\r\n
0xd000005f | PhoneTone_3GPP2_Busy\r\n
0xd0000060 | PhoneTone_3GPP2_CallWaiting\r\n
0xd0000061 | PhoneTone_3GPP2ISDNAlerting_PingRing\r\n
0xd0000062 | PH_CHANGEEVENT_ALL\r\n
0xd0000063 | PH_CHANGEEVENT_PHONESTATE\r\n
0xd0000064 | PH_CHANGEEVENT_ACTIONAVAILABILITY\r\n
0xd0000065 | PH_CHANGEEVENT_MUTE\r\n
0xd0000066 | PH_CHANGEEVENT_SPEAKER\r\n
0xd0000067 | PH_CHANGEEVENT_BLUETOOTHHANDSFREE\r\n
0xd0000068 | PH_CHANGEEVENT_PROVIDERGENERALINFO\r\n
0xd0000069 | PH_CHANGEEVENT_PROVIDERLINESERVICEINFO\r\n
0xd000006a | PH_CHANGEEVENT_PROVIDERLINEINFO\r\n
0xd000006b | PH_CHANGEEVENT_PROVIDERSIGNALSTRENGTH\r\n
0xd000006c | PH_CHANGEEVENT_VVM_CONNECTIVITY_STATE\r\n
0xd000006d | PH_CHANGEEVENT_ERROR\r\n
0xd000006e | PH_CHANGEEVENT_ALERTMSG\r\n
0xd000006f | PH_CHANGEEVENT_MODIFY_VOICEMAILADDRESS\r\n
0xd0000070 | PH_CHANGEEVENT_MODIFY_CALLERID\r\n
0xd0000071 | PH_CHANGEEVENT_MODIFY_CALLFORWARDING\r\n
0xd0000072 | PH_CHANGEEVENT_SIMSEC_UNLOCK\r\n
0xd0000073 | PH_CHANGEEVENT_SIMSEC_ENABLE\r\n
0xd0000074 | PH_CHANGEEVENT_SIMSEC_DISABLE\r\n
0xd0000075 | PH_CHANGEEVENT_SIMSEC_CHANGEPIN\r\n
0xd0000076 | PH_CHANGEEVENT_SIMSEC_FDN_CHANGEPIN2\r\n
0xd0000077 | PH_CHANGEEVENT_SIMSEC_FDN_GETPIN2\r\n
0xd0000078 | PH_CHANGEEVENT_SIMSEC_UICLOSED\r\n
0xd0000079 | PH_CHANGEEVENT_CELLULARLINECOMPONENTSCHANGED\r\n
0xd000007a | PH_CHANGEEVENT_PROVIDERLINELOCKINFO\r\n
0xd000007b | PH_CHANGEEVENT_ASYNC_OPERATION_SUCCESS\r\n
0xd000007c | PH_CHANGEEVENT_ASYNC_OPERATION_FAILURE\r\n
0xd000007d | PH_CHANGEEVENT_DEFAULTOUTGOINGLINE\r\n
0xd000007e | PH_CHANGEEVENT_AGGREGATEBRANDING\r\n
0xd000007f | PH_CHANGEEVENT_BRANDINGTEXT\r\n
0xd0000080 | PH_CHANGEEVENT_MODIFY_VIDEOCALLING\r\n
0xd0000081 | PH_CHANGEEVENT_LINEADDED\r\n
0xd0000082 | PH_CHANGEEVENT_LINEREMOVED\r\n
0xd0000083 | PH_CHANGEEVENT_LAUNCH_EMERGENCY_DIALER\r\n
0xd0000084 | PH_CHANGEEVENT_ENUM_COUNT\r\n
0xd0000085 | PH_ERROR_NONE\r\n
0xd0000086 | PH_ERROR_CALLDROPPED\r\n
0xd0000087 | PH_ERROR_NETWORKDROPPED\r\n
0xd0000088 | PH_ERROR_CONFERENCEFAILED\r\n
0xd0000089 | PH_ERROR_END\r\n
0xd000008a | PH_ERROR_PRIVATE\r\n
0xd000008b | PH_ERROR_ANSWER\r\n
0xd000008c | PH_ERROR_FLASH\r\n
0xd000008d | PH_ERROR_HOLD\r\n
0xd000008e | PH_ERROR_SWAP\r\n
0xd000008f | PH_ERROR_UNHOLD\r\n
0xd0000090 | PH_ERROR_MUTE\r\n
0xd0000091 | PH_ERROR_UNMUTE\r\n
0xd0000092 | PH_ERROR_DIAL\r\n
0xd0000093 | PH_ERROR_BADADDRESS\r\n
0xd0000094 | PH_ERROR_INVALIDSIM\r\n
0xd0000095 | PH_ERROR_NETWORKSERVICENOTAVAILABLE\r\n
0xd0000096 | PH_ERROR_EMERGENCYONLY\r\n
0xd0000097 | PH_ERROR_SERVICEOFF\r\n
0xd0000098 | PH_ERROR_OPERATIONFAILED\r\n
0xd0000099 | PH_ERROR_OUTGOINGCALLNOFREELINES\r\n
0xd000009a | PH_ERROR_TRANSFER\r\n
0xd000009b | UNUSED_PH_ERROR_22\r\n
0xd000009c | PH_ERROR_FDNRESTRICT\r\n
0xd000009d | PH_ERROR_SENDDTMF\r\n
0xd000009e | PH_ERROR_DROPACCEPT\r\n
0xd000009f | UNUSED_PH_ERROR_26\r\n
0xd00000a0 | PH_ERROR_SIMSECNEEDED\r\n
0xd00000a1 | PH_ERROR_CALLFORWARDRETRIEVE\r\n
0xd00000a2 | PH_ERROR_CALLFORWARDAPPLY\r\n
0xd00000a3 | PH_ERROR_ROAMRESTRICT\r\n
0xd00000a4 | PH_ERROR_DISABLELOCALVIDEO\r\n
0xd00000a5 | PH_ERROR_ENABLELOCALVIDEO\r\n
0xd00000a6 | PH_ERROR_ADDVIEO\r\n
0xd00000a7 | PH_ERROR_DROPVIDEO\r\n
0xd00000a8 | PH_ERROR_ACCEPTVIDEO\r\n
0xd00000a9 | PH_ERROR_REJECTVIDEO\r\n
0xd00000aa | PH_ERROR_SETVIDEOPAUSED\r\n
0xd00000ab | PH_ERROR_VIDEOCALLINGOFF\r\n
0xd00000ac | PH_ERROR_COUNT\r\n
0xd00000ad | Critical section held\r\n
0xd00000ae | Waiting on critical section\r\n
0xd00000af | Enable audio routing\r\n
0xd00000b0 | Disable audio routing\r\n
0xd00000b1 | Set audio endpoint\r\n
0xd00000b2 | Enable cellular audio\r\n
0xd00000b3 | Disable cellular audio\r\n
0xd00000b4 | Mute cellular audio rx\r\n
0xd00000b5 | Mute cellular audio tx\r\n
0xd00000b6 | Mute voip audio\r\n
0xd00000b7 | Phone Controller DispatchWork\r\n
0xd00000b8 | CoreUI endpoint find\r\n
0xd00000b9 | CoreUI send message\r\n
0xd00000ba | POOM request while Dialing\r\n
0xd00000bb | Playing an event sound in Call Progress sink\r\n
0xd00000bc | Stopping event sounds\r\n
0xd00000bd | Getting cellular Rx mute state\r\n
0xd00000be | Enumerating audio endpoints\r\n
0xd00000bf | Enable cellular provider change\r\n
0xd00000c0 | Unknown or not possible\r\n
0xd00000c1 | Never possible\r\n
0xd00000c2 | Querying other party availability\r\n
0xd00000c3 | Other Party Unavailable\r\n
0xd00000c4 | Querying Data Connectivity\r\n
0xd00000c5 | Data Connectivity Unavailable\r\n
0xd00000c6 | Other Party and DataConnectivity Available\r\n
0xd00000c7 | Upgrade Available\r\n
0xd00000c8 | Querying Remote Party Seamless Capability\r\n
0xd00000c9 | Non-Seamless Upgrade Initiated\r\n
0xd00000ca | Seamless Upgrade Initiated\r\n
0xd00000cb | Upgrade Complete\r\n
0xd00000cc | App Querying Remote Party Seamless Capability\r\n
0xd00000cd | None\r\n
0xd00000ce | CircuitSwitched\r\n
0xd00000cf | PacketSwitched\r\n
0xd00000d0 | PacketSwitched_WiFi\r\n
0xd00000d1 | FALSE\r\n
0xd00000d2 | TRUE\r\n
0xd00000d3 | SingleLine\r\n
0xd00000d4 | MultiLine-Separate\r\n
0xd00000d5 | MultiLine-Linked\r\n
0xd00000d6 | AlertText\r\n
0xd00000d7 | ServiceOn\r\n
0xd00000d8 | SystemType\r\n
0xd00000d9 | EmergencyCallbackMode\r\n
0xd00000da | Muted\r\n
0xd00000db | SupportsPlusCodeDialing\r\n
0xd00000dc | LocalCallWaitingToneNeeded\r\n
0xd00000dd | SupportsHold\r\n
0xd00000de | LineSettingCapabilities\r\n
0xd00000df | Capabilities\r\n
0xd00000e0 | OperatorName\r\n
0xd00000e1 | OperatorNumericName\r\n
0xd00000e2 | BroadcastText\r\n
0xd00000e3 | CountryCode\r\n
0xd00000e4 | RegistrationState\r\n
0xd00000e5 | RegistrationRejectReason\r\n
0xd00000e6 | SimState\r\n
0xd00000e7 | CurrentMcc\r\n
0xd00000e8 | SimStateLockInfo\r\n
0xd00000e9 | SimUnlockAttemptsRemaining\r\n
0xd00000ea | SimUnblockAttemptsRemaining\r\n
0xd00000eb | PersoFeature\r\n
0xd00000ec | PersoState\r\n
0xd00000ed | PersoUnlockAttemptsRemaining\r\n
0xd00000ee | PersoUnblockAttemptsRemaining\r\n
0xd00000ef | SignalStrength\r\n
0xd00000f0 | SubscriberAddress\r\n
0xd00000f1 | BrandingImagePath\r\n
0xd00000f2 | LineBrandingFlags\r\n
0xd00000f3 | SmallIconPath\r\n
0xd00000f4 | CallForwardingState\r\n
0xd00000f5 | CallForwardingAddress\r\n
0xd00000f6 | CallerIdSetting\r\n
0xd00000f7 | AccountFriendlyName\r\n
0xd00000f8 | SortKey\r\n
0xd00000f9 | IgnoreUssdExclusions\r\n
0xd00000fa | UssdExclusionList\r\n
0xd00000fb | SlotIndex\r\n
0xd00000fc | VoicemailAddress\r\n
0xd00000fd | VoicemailProvisioningState\r\n
0xd00000fe | VoicemailConnectivityState\r\n
0xd00000ff | VoicemailCount\r\n
0xd0000100 | CurrentMnc\r\n
0xd0000101 | VideoCallingEnabled\r\n
0xd0000102 | NotStarted\r\n
0xd0000103 | InProgress\r\n
0xd0000104 | Complete\r\n
0xd0000105 | Initializing\r\n
0xd0000106 | Unavailable\r\n
0xd0000107 | Idle\r\n
0xd0000108 | Starting\r\n
0xd0000109 | Recording\r\n
0xd000010a | Pausing\r\n
0xd000010b | Paused\r\n
0xd000010c | Resuming\r\n
0xd000010d | Finishing\r\n
0xd000010e | End\r\n
0xd000010f | Begin\r\n
0xd0000110 | Cancel\r\n
0xd0000111 | PhoneLineChangeKind_Added\r\n
0xd0000112 | PhoneLineChangeKind_Removed\r\n
0xd0000113 | PhoneLineChangeKind_PropertiesChanged\r\n
0xd0000114 | UdmCallItemEventType_EventMissed\r\n
0xd0000115 | UdmCallItemEventType_EventCreate\r\n
0xd0000116 | UdmCallItemEventType_EventDelete\r\n
0xd0000117 | UdmCallItemEventType_EventDeleteAll\r\n
0xd0000118 | UdmCallItemEventType_EventModify\r\n
0xd0000119 | UdmCallItemEventType_EventConnectionBroken\r\n
0xd000011a | RcsMediaType_None\r\n
0xd000011b | RcsMediaType_AudioOnly\r\n
0xd000011c | RcsMediaType_AudioVideo\r\n
0xd000011d | VideoCallingSetting_Disabled\r\n
0xd000011e | VideoCallingSetting_Enabled\r\n
0xd000011f | VideoCallingSetting_CachedValue\r\n
0xd0000120 | RcsServiceStatus_Stopped\r\n
0xd0000121 | RcsServiceStatus_Started\r\n
0xd0000122 | RcsServiceStatus_Stopping\r\n
0xd0000123 | RcsServiceStatus_Starting\r\n
0xf0000001 | CallVerb_Dial\r\n
0xf0000002 | CallVerb_End\r\n
0xf0000003 | CallVerb_DropActiveAcceptHeld\r\n
0xf0000004 | CallVerb_Hold\r\n
0xf0000005 | CallVerb_Unhold\r\n
0xf0000006 | CallVerb_Swap\r\n
0xf0000007 | CallVerb_Private\r\n
0xf0000008 | CallVerb_Conference\r\n
0xf0000009 | CallVerb_Flash\r\n
0xf000000a | CallVerb_RejectIncoming\r\n
0xf000000b | CallVerb_AcceptIncoming\r\n
0xf000000c | CallVerb_SendDtmf\r\n
0xf000000d | CallVerb_StartDtmf\r\n
0xf000000e | CallVerb_StopDtmf\r\n
0xf000000f | CallVerb_DropFromConference\r\n
0xf0000010 | CallVerb_DisableLocalVideo\r\n
0xf0000011 | CallVerb_EnableLocalVideo\r\n
0xf0000012 | CallVerb_AddVideo\r\n
0xf0000013 | CallVerb_DropVideo\r\n
0xf0000014 | CallVerb_AcceptIncomingVideo\r\n
0xf0000015 | CallVerb_RejectIncomingVideo\r\n
0xf0000016 | CallVerb_SetVideoPaused\r\n
0xf0000017 | CallVerb_StartRecording\r\n
0xf0000018 | CallVerb_PauseRecording\r\n
0xf0000019 | CallVerb_StopRecording\r\n
0xf000001a | BGS_BTCM_RUNNING\r\n
0xf000001b | BGS_RADIO_ENABLED\r\n
0xf000001c | BGS_INQUIRY_IN_PROGRESS\r\n
0xf000001d | BGS_DEVICE_CONNECTED\r\n
0xf000001e | BGS_PHONE_CONNECTED\r\n
0xf000001f | BGS_AUDIO_CONNECTED\r\n
0xf0000020 | VideoCalling\r\n
0xf0000021 | PhoneLineProperties_BrandingOptions\r\n
0xf0000022 | PhoneLineProperties_CanDial\r\n
0xf0000023 | PhoneLineProperties_CellularDetails\r\n
0xf0000024 | PhoneLineProperties_DisplayColor\r\n
0xf0000025 | PhoneLineProperties_DisplayName\r\n
0xf0000026 | PhoneLineProperties_NetworkName\r\n
0xf0000027 | PhoneLineProperties_NetworkState\r\n
0xf0000028 | PhoneLineProperties_Transport\r\n
0xf0000029 | PhoneLineProperties_Voicemail\r\n

### 10.0.14393.0

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
0xb000000a | %1\r\n
0xb0000064 | The Phone service is starting\r\n
0xb0000065 | The Phone service has started\r\n
0xb0000066 | The Phone service failed to start with error %1\r\n
0xb0000067 | The Phone service is stopping\r\n
0xb0000068 | The Phone service has stopped\r\n
0xb0000258 | PH_MSG: %1 with supsvc code or SIM error: %2\r\n
0xb0000259 | USSD Message: %1 suppressed due to emergency call\r\n
0xb000025a | PhoneService: Phone RPC server started. Setting PhoneApiReady.\r\n
0xb000025b | PhoneService: Stopping Phone RPC server.\r\n
0xb00002bc | CallState Change for callId: %1, from %2 to %3\r\n
0xb00002be | Controller request to provider %1: verb %2 id: %3 hr: %4\r\n
0xb00002bf | Controller request result from provider %1: verb %2 id: %3 hr: %4\r\n
0xb00002c0 | Dialing: Got call handle from provider\r\n
0xb00002c1 | Dialing: Failed due to existing outgoing call\r\n
0xb00002c2 | Phone dialing %1\r\n
0xb00002c4 | Fake Call Added: %1\r\n
0xb00002c8 | Controller added call history record with Oid: %1 hr %2\r\n
0xb00002c9 | Dialing rules start\r\n
0xb00002ca | Dialing rules end: modified by rule %1, rule processing time %2 ms.\r\n
0xb00002cb | Dialing: Failed because there are already two calls.\r\n
0xb00002cc | Dialing: Failed because the active call cannot be held.\r\n
0xb00002cd | Controller holding call %1 to accept call %2.\r\n
0xb00002ce | Controller dropping held call %1 to accept call %2.\r\n
0xb00002cf | Controller using DropAccept for incoming, dropping call %1 to accept %2.\r\n
0xb00002d0 | [CellularAudio] Setting audio endpoint to %1\r\n
0xb00002d1 | [CellularAudio] Notified of audio routing endpoint change to %1\r\n
0xb00002d2 | [CellularAudio] Notified of bluetooth state change to %1\r\n
0xb00002d3 | [CellularAudio] Enabling phone call audio to endpoint %1; IsIncoming %2\r\n
0xb00002d4 | [CellularAudio] Disabling phone call audio\r\n
0xb00002d6 | Phone service failed to initialize UDM or CallHistoryItemWriter.  Call history entries will not be written.  HRESULT: %1\r\n
0xb00002d7 | Phone service failed to initialize External VVM manager.  VVM apps will not be able to control audio. HRESULT: %1\r\n
0xb00002d8 | Phone service failed to initialize POOM.  Caller ID information will not be available. HRESULT: %1\r\n
0xb00002d9 | [CellularAudio] Tone Notification: %1, digits %2, on %3, off %4\r\n
0xb00002da | Controller OnFinished called for requestId %1 hr: %2\r\n
0xb00002db | Rejected incoming call. Line id: %1 Call Id: %2 reason: %3 \r\n
0xb00002dc | [CellularAudio] Enabling cellular audio: %1 on executor %2\r\n
0xb00002dd | [CellularAudio] Disabling cellular audio: %1 on executor %2\r\n
0xb00002de | VOIP audio count ref increased\r\n
0xb00002df | VOIP audio count ref Decreased\r\n
0xb00002e0 | VOIP muting audio\r\n
0xb00002e1 | VOIP unmuting audio\r\n
0xb00002e2 | PhoneController - phone line added. id: %1, type: %2\r\n
0xb00002e3 | PhoneController - phone line removed. id: %1\r\n
0xb00002e4 | PhoneController - line property: %2 value: %3 for line ID:%1\r\n
0xb00002e6 | [CellularAudio] ExecutorIndex: %1 already initialized for audio\r\n
0xb00002e7 | [CellularAudio] Muting cellular TX audio: %1 on executor %2, muted: %3\r\n
0xb00002e8 | [CellularAudio] Muting cellular RX audio: %1 on executor %2, muted: %3\r\n
0xb00002e9 | EndUpgradeOriginationCall invoked for upgrade guid %1\r\n
0xb00002ea | CancelUpgrade invoked for upgrade guid %1\r\n
0xb00002eb | [CellularAudio] Enabling cellular provider change, [executorIndex=%1][cellularAudioType=%2][operation=%3]\r\n
0xb00002ec | [CellularAudio] Invalid cellular provider change attempted, [executorIndex=%1][targetAudioType=%2][operation=%3][currentAudioType=%4][isInHandover=%5]\r\n
0xb00002ed | [CellularAudio] Handover in progress, cellular audio type change not allowed [executorIndex=%1][cellularAudioType=%2][audioActive=%3]\r\n
0xb00002ee | Phone call swap was ignored. Call to hold: %1. Call to unhold: %2.\r\n
0xb00002ef | Calculation for time between call swaps was completed. Allow swap is %1. Last successful swap was %2 ms ago. The device is configured to wait at least %3 ms in between swaps.\r\n
0xb00002f0 | CallProgress - Determined sound configuration according to country code, [LineId=%1][CountryCode=%2][InCallToneType=%3][InCallToneName=%4]\r\n
0xb00002f1 | Disable and enable cellular audio. Disable Executor Index: %1, Enable Executor Index: %2, Cellular Audio Type: %3, Audio Active: %4\r\n
0xb00002f2 | CallProgress - Using override country code for determining tone configuration, [CountryCode=%1][OverrideCountryCode=%2]\r\n
0xb00002f3 | CallProgress - Failed to get 3GPP in call tone for type and mcc, [CountryCode=%1][InCallToneType=%2][HRESULT=%3]\r\n
0xb00002f4 | CallProgress - Failed to get 3GPP in call tone, [HRESULT=%1]\r\n
0xb0000384 | Event sound: %1\r\n
0xb0000418 | Emergency Number: received updated list %1\r\n
0xb0000419 | Emergency Number: Dial request for callid %1\r\n
0xb000041a | Emergency Number list received null argument or empty list.\r\n
0xb000041b | Dialing: Failed because the line attempt to dial is not free.\r\n
0xb000041c | OperationWatchdog: "%1" timed out.  Context: %2.  Timeout value: %3ms.  Still waiting after: %4ms.\r\n
0xb000041d | OperationWatchdog: "%1" completed.  Context: %2.  Actual time: %3ms\r\n
0xb000041e | Async API context %1 completed with result %2\r\n
0xb000041f | Phone service listener added: %1\r\n
0xb0000420 | Phone service listener removed: %1\r\n
0xb0000421 | Phone service listener lost notifications: %1\r\n
0xb0000423 | Phone service listener rundown: %1\r\n
0xb0000424 | Phone notification sent: %1 error: %2\r\n
0xb0000429 | Call Upgrade state for CallId: %1 Changed From: %2 To: %3\r\n
0xb000042a | Data Connectivity State: %1\r\n
0xb000042d | Non-seamless upgrade was cancelled by the user.\r\n
0xb000042e | Seamless upgrade was cancelled by the user.\r\n
0xb000042f | Connection Manager Error. Connection Manager Result: %1.\r\n
0xb0000430 | Call Line Change for CallId: %1 from LineId: %2 to LineId: %3\r\n
0xb0000432 | PhoneTileManager: Creating secondary Phone Tile with id: %1\r\n
0xb0000433 | PhoneTileManager: Setting the primary Phone Tile to be assigned to PhoneLineId: %1\r\n
0xb0000434 | PhoneTileManager: Deleting Phone Tile with id: %1\r\n
0xb0000436 | PhoneTile: Committed an update to the Phone Tile with tile id: %1. Title %2; Tile mode: %3; has voicemail: %4; missed call count: %5; has large content: %6\r\n
0xb0000438 | PhoneTileControllerSink: The PhoneLine (%1) has been removed.  Removing its tile and updating any remaining tiles as necessary.\r\n
0xb000043f | PhoneTileControllerSink: ShellReadyState changed to %1\r\n
0xb0000440 | SystemEventTriggerControllerSink: LineChangedTrigger fired with: LineId %1: PhoneLineChangeKind %2: PhoneLineProperties: %3: hr: %4\r\n
0xb0000441 | SystemEventTriggerControllerSink: NewVoicemailMessageTrigger fired with: LineId %1: voicemailCount %2: VoicemailMessage: %3: hr: %4\r\n
0xb0000442 | SystemEventTriggerControllerSink: CallOriginDataRequestTrigger fired with: RequestId %1: PhoneNumber: %2: hr: %3\r\n
0xb0000443 | SystemEventTriggerControllerSink: CallHistoryChanged fired with: hr: %1\r\n
0xb0000444 | SystemEventTriggerControllerSink: AirplaneModeDisabledForEmergencyCall fired with: hr: %1\r\n
0xb0000445 | SystemEventTriggerControllerSink: OnCallEvent called with: event: %1\r\n
0xb0000446 | SystemEventTriggerControllerSink: Attempted to advise to CallHistorySession with: hr: %1\r\n
0xb0000447 | IR94FeatureDisabled: Returning video capability sharing as disabled.\r\n
0xb0000448 | IR94FeatureDisabled: Returning device not video capable.\r\n
0xb0000449 | IR94FeatureDisabled: Returning video calling switch as not actionable.\r\n
0xb000044a | SystemEventTriggerControllerSink: LineChangedTrigger suppressed [LineId=%1][PhoneLineChangeKind=%2][PhoneLineProperties=%3]\r\n
0xb000044b | SystemEventTriggerControllerSink: Received shell ready notification.\r\n
0xb000044c | SystemEventTriggerControllerSink: OnShellReady started [existingInitialBootSequenceComplete=%1][cachedLineCount=%2]\r\n
0xb000044d | SystemEventTriggerControllerSink: OnShellReady triggering deferred notification [LineId=%1][PhoneLineChangeKind=%2][PhoneLineProperties=%3]\r\n
0xb000044e | SystemEventTriggerControllerSink: Received screen state change notification [monitorState=%1].\r\n
0xb000044f | SystemEventTriggerControllerSink: OnScreenStateChange started [existingSuppressLineChangedTrigger=%1][screenIsOn=%2]\r\n
0xb0000450 | SystemEventTriggerControllerSink: OnScreenStateChange triggering deferred notification [LineId=%1][PhoneLineChangeKind=%2][PhoneLineProperties=%3]\r\n
0xb0000451 | SystemEventTriggerControllerSink: LineChangedTrigger skipped [LineId=%1]\r\n
0xb00004b1 | InteractiveUserNotificationSink: New Incoming Call State Changed [callId=%1].\r\n
0xb00004b2 | InteractiveUserNotificationSink: Show Incoming Call Toast [callId=%1].\r\n
0xb00004b3 | Supplementary service code: %1 was converted from erase to deactivate command due override setting.\r\n
0xb00005dd | Call data collection item added for CallId: [%1]\r\n
0xb00005de | Call data collection item removed for CallId: [%1]\r\n
0xb00005df | Call data collection item dropped an idle call for CallId: [%1]\r\n
0xb00005e0 | CallHistoryItemWriter: Call with id %1 is added.\r\n
0xb00005e1 | CallHistoryItemWriter: Call with id %1 is updated.\r\n
0xb00005e2 | CallAnnotationsLookupConnecting: Establishing RPC connection.  Endpoint: %1\r\n
0xb00005e3 | CallAnnotationsLookup: Querying location.  Phone number: %1\r\n
0xb00005e4 | CallAnnotationsLookup: Completed location query.  Location: %1\r\n
0xb00005e5 | CallAnnotationsLookup: RPC failure, clearing RPC connection.\r\n
0xb00005e6 | CallAnnotationsManager: Call: %1 LookupState: %2\r\n
0xb00005e7 | Shutting down Phone service due to idle stop.\r\n
0xb00005e8 | Service Idle Callback received. Idle status: %1, Phone calls exist: %2\r\n
0xb00005e9 | CallRecording VALID state change from '%2' to '%3' on executor %1\r\n
0xb00005ea | CallRecording: INVALID state change from '%2' to '%3' on executor %1\r\n
0xb00005eb | CallRecording: Recorded call is now idle.  Recording will end.  LineId:%1, CallId:%2, ConferenceCallId:%3\r\n
0xb00005ec | CallRecording: Recorded call is now held.  Recording will pause and may finish.  LineId:%1, CallId:%2, ConferenceCallId:%3\r\n
0xb00005ed | CallRecording: A call that is not being recorded is talking.  Recording will finish.  LineId:%1, CallId:%2, ConferenceCallId:%3\r\n
0xb00005ee | CallRecording: Recorded call no longer exists.  Recording will finish.  LineId:%2, CallId:%1\r\n
0xb00005ef | CallRecording: Preferred recording application changed.  Old Package Family Name: '%1', New Package Family Name: '%2'\r\n
0xb00005f0 | Call [callId=%1] marked as handover merged due to being conferenced with call [callState=%2] that ended with handover merged reason\r\n
0xb00005f1 | CallRecordingOff: %1, Preferred Recording app PFN: %2\r\n
0xb00005f2 | CallRecordingApplication %1 detected\r\n
0xb0000640 | [RcsPresence] Request Capabilities: %1\r\n
0xb0000641 | [RcsPresence] Received query response, [responseCode=%1][reason=%2]\r\n
0xb0000642 | [RcsPresence] Received %1 capability tuple(s)\r\n
0xb0000643 | [RcsPresence] Tuple %1, MediaType not video capable: %2\r\n
0xb0000644 | [RcsPresence] Tuple %1, ServiceIdentifier not video capable: %2\r\n
0xb0000645 | [RcsPresence] Tuple %1 is video capable.\r\n
0xb0000646 | [RcsPresence] RcsPresenceCache hit, [TelUri string=%1][Capabilities returned=%2]\r\n
0xb0000647 | [RcsPresence] Query suppressed due to capabilities sharing opt-in settings, [TelUri string=%1][Capabilities returned=%2]\r\n
0xb0000648 | Checking for device support of video calling. This service (%1) exists, thus video calling is supported.\r\n
0xb0000649 | Checking for device support of video calling. This service (%2) does NOT exist due to error code %1, thus a different service would have to exist for video calling to be supported.\r\n
0xb000064a | PhoneController - Updating video calling settings, [lineId=%1][videoCallingSetting=%2][cacheVideoCallingSetting=%3][userRequest=%4][TTYEnabled=%5][cellularDataEnabled=%6]\r\n
0xb000064b | CallRecording: Deferred request to disable cellular audio: %1 on executor %2\r\n
0xb000064c | CallRecording: Cancelled request to defer disabling of cellular audio: %3 due to enabling of: %1 on executor %2\r\n
0xb000064d | CallRecording: An audio type change prevented deferring of audio disable.  New audio type: %1, Audio type being disabled: %3 on executor %2\r\n
0xb000064e | CallRecording: Performing deferred request to disable cellular audio: %1 on executor %2\r\n
0xb000064f | [RcsPresence] Received OnPublishRequested\r\n
0xb0000650 | [RcsPresence] Suppressed publishing actual video capability as UCE capability sharing is disabled.\r\n
0xb0000651 | [RcsPresence] Video capability sharing settings update requested [isCapabilitySharingEnabled=%1][previousValue=%2].\r\n
0xb0000652 | [RcsPresence] Cache initialized [cacheExpirationInSeconds=%1]\r\n
0xb0000653 | [RcsPresence] Publishing capabilities [%1]\r\n
0xb0000654 | [RcsPresence] Initializing RCS presence service\r\n
0xb0000655 | [RcsPresence] RCS presence service status queried, [status=%1]\r\n
0xb0000656 | [RcsPresence] Starting RCS presence service\r\n
0xb0000657 | [RcsPresence] Received publish response, [responseCode=%1][reason=%2]\r\n
0xb0000658 | [RcsPresence] Received OnNetworkSupportVideoChanged, [updatedValue=%1][previousValue=%2]\r\n
0xb0000659 | [RcsPresence] Saved last published capabilities, [updatedValue=%1][previousValue=%2]\r\n
0xb000065a | [RcsPresence] Publish capabilities requested, [reason=%1][networkType=%2]\r\n
0xb000065b | Attempting audio routing {%1} as per settings.\r\n
0xd0000001 | PH_CALLSTATE_AMBIGUOUS\r\n
0xd0000002 | PH_CALLSTATE_INCOMING\r\n
0xd0000003 | PH_CALLSTATE_CALLING\r\n
0xd0000004 | PH_CALLSTATE_TALKING\r\n
0xd0000005 | PH_CALLSTATE_HOLD\r\n
0xd0000006 | PH_CALLSTATE_IDLE\r\n
0xd0000007 | PH_CALLSTATE_TRANSFERRING\r\n
0xd0000008 | RejectIncomingReason_UserRequest\r\n
0xd0000009 | RejectIncomingReason_OtherIncomingCall\r\n
0xd000000a | RejectIncomingReason_EmergencyMode\r\n
0xd000000b | RejectIncomingReason_Filtered\r\n
0xd000000c | PH_MSG_SIMPHONEBOOKENTRY\r\n
0xd000000d | PH_MSG_SUPSVCEXECUTING\r\n
0xd000000e | PH_MSG_SUPSVCSUCCEEDED\r\n
0xd000000f | PH_MSG_SUPSVCFAILED\r\n
0xd0000010 | PH_MSG_USSDEXECUTING\r\n
0xd0000011 | PH_MSG_USSDEXECUTED_FURTHER_INFO_REQUIRED\r\n
0xd0000012 | PH_MSG_USSDEXECUTED_NO_FURTHER_INFO_REQUIRED\r\n
0xd0000013 | PH_MSG_CALLEE_INCOMING_CALLS_BARRED\r\n
0xd0000014 | PH_MSG_VOICEMAIL\r\n
0xd0000015 | PH_MSG_MISSEDCALL\r\n
0xd0000016 | PH_MSG_SPEAKERPHONEON\r\n
0xd0000017 | PH_MSG_SERVICEAUTOENABLED\r\n
0xd0000018 | PH_MSG_CURRENTLY_IN_ECBM\r\n
0xd0000019 | PH_MSG_ECBMIDLE\r\n
0xd000001a | PH_MSG_NOT_CURRENTLY_IN_ECBM\r\n
0xd000001b | PH_MSG_ERRORCALLDROPPED\r\n
0xd000001c | PH_MSG_ERRORNETWORKDROPPED\r\n
0xd000001d | PH_MSG_ERRORINVALIDDESTADDRESS\r\n
0xd000001e | PH_MSG_ERRORNOTADMIN\r\n
0xd000001f | PH_MSG_ERRORCONFERENCEFAILED\r\n
0xd0000020 | PH_MSG_ERRORVOICEMAILSWITCHLINES\r\n
0xd0000021 | PH_MSG_ERROREND\r\n
0xd0000022 | PH_MSG_ERRORPRIVATE\r\n
0xd0000023 | PH_MSG_ERRORANSWER\r\n
0xd0000024 | PH_MSG_ERRORFLASH\r\n
0xd0000025 | PH_MSG_ERRORHOLD\r\n
0xd0000026 | PH_MSG_ERRORSWAP\r\n
0xd0000027 | PH_MSG_ERRORUNHOLD\r\n
0xd0000028 | PH_MSG_ERRORMUTE\r\n
0xd0000029 | PH_MSG_ERRORUNMUTE\r\n
0xd000002a | PH_MSG_ERRORDIAL\r\n
0xd000002b | PH_MSG_ERRORNODIALTONE\r\n
0xd000002c | PH_MSG_ERRORUNREACHABLE\r\n
0xd000002d | PH_MSG_ERRORBADADDRESS\r\n
0xd000002e | PH_MSG_ERRORSIMBUSY\r\n
0xd000002f | PH_MSG_ERRORNETWORKSERVICENOTAVAILABLE\r\n
0xd0000030 | PH_MSG_ERROREMERGENCYONLY\r\n
0xd0000031 | PH_MSG_ERRORRADIOOFF\r\n
0xd0000032 | PH_MSG_ERROROPERATIONFAILED\r\n
0xd0000033 | PH_MSG_ERROROUTGOINGCALLNOFREELINES\r\n
0xd0000034 | PH_MSG_ERRORNOVMAILNUMBER\r\n
0xd0000035 | PH_MSG_ERRORTRANSFER\r\n
0xd0000036 | PH_MSG_SIMSECNEEDED\r\n
0xd0000037 | PH_MSG_EXT\r\n
0xd0000038 | PH_MSG_ERRORDESTINATIONBARRED\r\n
0xd0000039 | PH_MSG_ERRORFDNRESTRICT\r\n
0xd000003a | PH_MSG_ERRORDTMF\r\n
0xd000003b | PH_MSG_ERRORCHLD1\r\n
0xd000003c | PH_MSG_ERRORCALLFORWARDRETRIEVE\r\n
0xd000003d | PH_MSG_ERRORCALLFORWARDAPPLY\r\n
0xd000003e | PH_MSG_DISMISSSUPSVCS\r\n
0xd000003f | PH_MSG_SIMUNLOCK\r\n
0xd0000040 | PH_MSG_ERRORROAMRESTRICT\r\n
0xd0000041 | PH_MSG_SEAMLESS_UPGRADE\r\n
0xd0000042 | PH_MSG_UPGRADE_ERROR\r\n
0xd0000043 | PH_MSG_ERRORDISABLELOCALVIDEO\r\n
0xd0000044 | PH_MSG_ERRORENABLELOCALVIDEO\r\n
0xd0000045 | PH_MSG_ERRORADDVIDEO\r\n
0xd0000046 | PH_MSG_ERRORDROPVIDEO\r\n
0xd0000047 | PH_MSG_ERRORACCEPTVIDEO\r\n
0xd0000048 | PH_MSG_ERRORREJECTVIDEO\r\n
0xd0000049 | PH_MSG_ERRORSETVIDEOPAUSED\r\n
0xd000004a | PH_MSG_ERRORVIDEOCALLINGOFF\r\n
0xd000004b | PH_MSG_VOIP_INSTALL_PROMPT\r\n
0xd000004c | PH_MSG_ERRORSTARTRECORDING\r\n
0xd000004d | PH_MSG_ERRORPAUSERECORDING\r\n
0xd000004e | PH_MSG_ERRORSTOPRECORDING\r\n
0xd000004f | PH_MSG_VIDEOCHARGESPROMPT\r\n
0xd0000050 | PH_MSG_ERROREXPLICITCALLTRANSFER\r\n
0xd0000051 | PH_MSG_WIFICALLINGUPSELLPROMPT\r\n
0xd0000052 | PH_MSG_LAST\r\n
0xd0000053 | PhoneCallAudio_DefaultEndpointPerRoutingPolicy\r\n
0xd0000054 | PhoneCallAudio_Speakerphone\r\n
0xd0000055 | PhoneCallAudio_Handset\r\n
0xd0000056 | PhoneCallAudio_WiredHeadset\r\n
0xd0000057 | PhoneCallAudio_WiredHeadsetWithMicrophone\r\n
0xd0000058 | PhoneCallAudio_BluetoothSco\r\n
0xd0000059 | PhoneCallAudio_BluetoothScoWithNREC\r\n
0xd000005a | PhoneTone_None\r\n
0xd000005b | PhoneTone_Off\r\n
0xd000005c | PhoneTone_DTMF_Start\r\n
0xd000005d | PhoneTone_DTMF_Stop\r\n
0xd000005e | PhoneTone_DTMF_Burst\r\n
0xd000005f | PhoneTone_3GPP_RingBack\r\n
0xd0000060 | PhoneTone_3GPP2_Reorder\r\n
0xd0000061 | PhoneTone_3GPP2_Busy\r\n
0xd0000062 | PhoneTone_3GPP2_CallWaiting\r\n
0xd0000063 | PhoneTone_3GPP2ISDNAlerting_PingRing\r\n
0xd0000064 | PH_CHANGEEVENT_ALL\r\n
0xd0000065 | PH_CHANGEEVENT_PHONESTATE\r\n
0xd0000066 | PH_CHANGEEVENT_ACTIONAVAILABILITY\r\n
0xd0000067 | PH_CHANGEEVENT_MUTE\r\n
0xd0000068 | PH_CHANGEEVENT_SPEAKER\r\n
0xd0000069 | PH_CHANGEEVENT_BLUETOOTHHANDSFREE\r\n
0xd000006a | PH_CHANGEEVENT_PROVIDERGENERALINFO\r\n
0xd000006b | PH_CHANGEEVENT_PROVIDERLINESERVICEINFO\r\n
0xd000006c | PH_CHANGEEVENT_PROVIDERLINEINFO\r\n
0xd000006d | PH_CHANGEEVENT_PROVIDERSIGNALSTRENGTH\r\n
0xd000006e | PH_CHANGEEVENT_VVM_CONNECTIVITY_STATE\r\n
0xd000006f | PH_CHANGEEVENT_ERROR\r\n
0xd0000070 | PH_CHANGEEVENT_ALERTMSG\r\n
0xd0000071 | PH_CHANGEEVENT_MODIFY_VOICEMAILADDRESS\r\n
0xd0000072 | PH_CHANGEEVENT_MODIFY_CALLERID\r\n
0xd0000073 | PH_CHANGEEVENT_MODIFY_CALLFORWARDING\r\n
0xd0000074 | PH_CHANGEEVENT_SIMSEC_UNLOCK\r\n
0xd0000075 | PH_CHANGEEVENT_SIMSEC_ENABLE\r\n
0xd0000076 | PH_CHANGEEVENT_SIMSEC_DISABLE\r\n
0xd0000077 | PH_CHANGEEVENT_SIMSEC_CHANGEPIN\r\n
0xd0000078 | PH_CHANGEEVENT_SIMSEC_FDN_CHANGEPIN2\r\n
0xd0000079 | PH_CHANGEEVENT_SIMSEC_FDN_GETPIN2\r\n
0xd000007a | PH_CHANGEEVENT_SIMSEC_UICLOSED\r\n
0xd000007b | PH_CHANGEEVENT_CELLULARLINECOMPONENTSCHANGED\r\n
0xd000007c | PH_CHANGEEVENT_PROVIDERLINELOCKINFO\r\n
0xd000007d | PH_CHANGEEVENT_ASYNC_OPERATION_SUCCESS\r\n
0xd000007e | PH_CHANGEEVENT_ASYNC_OPERATION_FAILURE\r\n
0xd000007f | PH_CHANGEEVENT_DEFAULTOUTGOINGLINE\r\n
0xd0000080 | PH_CHANGEEVENT_AGGREGATEBRANDING\r\n
0xd0000081 | PH_CHANGEEVENT_BRANDINGTEXT\r\n
0xd0000082 | PH_CHANGEEVENT_MODIFY_VIDEOCALLING\r\n
0xd0000083 | PH_CHANGEEVENT_LINEADDED\r\n
0xd0000084 | PH_CHANGEEVENT_LINEREMOVED\r\n
0xd0000085 | PH_CHANGEEVENT_LAUNCH_EMERGENCY_DIALER\r\n
0xd0000086 | PH_CHANGEEVENT_ENUM_COUNT\r\n
0xd0000087 | PH_ERROR_NONE\r\n
0xd0000088 | PH_ERROR_CALLDROPPED\r\n
0xd0000089 | PH_ERROR_NETWORKDROPPED\r\n
0xd000008a | PH_ERROR_CONFERENCEFAILED\r\n
0xd000008b | PH_ERROR_END\r\n
0xd000008c | PH_ERROR_PRIVATE\r\n
0xd000008d | PH_ERROR_ANSWER\r\n
0xd000008e | PH_ERROR_FLASH\r\n
0xd000008f | PH_ERROR_HOLD\r\n
0xd0000090 | PH_ERROR_SWAP\r\n
0xd0000091 | PH_ERROR_UNHOLD\r\n
0xd0000092 | PH_ERROR_MUTE\r\n
0xd0000093 | PH_ERROR_UNMUTE\r\n
0xd0000094 | PH_ERROR_DIAL\r\n
0xd0000095 | PH_ERROR_BADADDRESS\r\n
0xd0000096 | PH_ERROR_INVALIDSIM\r\n
0xd0000097 | PH_ERROR_NETWORKSERVICENOTAVAILABLE\r\n
0xd0000098 | PH_ERROR_EMERGENCYONLY\r\n
0xd0000099 | PH_ERROR_SERVICEOFF\r\n
0xd000009a | PH_ERROR_OPERATIONFAILED\r\n
0xd000009b | PH_ERROR_OUTGOINGCALLNOFREELINES\r\n
0xd000009c | PH_ERROR_TRANSFER\r\n
0xd000009d | UNUSED_PH_ERROR_22\r\n
0xd000009e | PH_ERROR_FDNRESTRICT\r\n
0xd000009f | PH_ERROR_SENDDTMF\r\n
0xd00000a0 | PH_ERROR_DROPACCEPT\r\n
0xd00000a1 | UNUSED_PH_ERROR_26\r\n
0xd00000a2 | PH_ERROR_SIMSECNEEDED\r\n
0xd00000a3 | PH_ERROR_CALLFORWARDRETRIEVE\r\n
0xd00000a4 | PH_ERROR_CALLFORWARDAPPLY\r\n
0xd00000a5 | PH_ERROR_ROAMRESTRICT\r\n
0xd00000a6 | PH_ERROR_DISABLELOCALVIDEO\r\n
0xd00000a7 | PH_ERROR_ENABLELOCALVIDEO\r\n
0xd00000a8 | PH_ERROR_ADDVIEO\r\n
0xd00000a9 | PH_ERROR_DROPVIDEO\r\n
0xd00000aa | PH_ERROR_ACCEPTVIDEO\r\n
0xd00000ab | PH_ERROR_REJECTVIDEO\r\n
0xd00000ac | PH_ERROR_SETVIDEOPAUSED\r\n
0xd00000ad | PH_ERROR_VIDEOCALLINGOFF\r\n
0xd00000ae | PH_ERROR_COUNT\r\n
0xd00000af | Critical section held\r\n
0xd00000b0 | Waiting on critical section\r\n
0xd00000b1 | Enable audio routing\r\n
0xd00000b2 | Disable audio routing\r\n
0xd00000b3 | Set audio endpoint\r\n
0xd00000b4 | Enable cellular audio\r\n
0xd00000b5 | Disable cellular audio\r\n
0xd00000b6 | Mute cellular audio rx\r\n
0xd00000b7 | Mute cellular audio tx\r\n
0xd00000b8 | Mute voip audio\r\n
0xd00000b9 | Phone Controller DispatchWork\r\n
0xd00000ba | CoreUI endpoint find\r\n
0xd00000bb | CoreUI send message\r\n
0xd00000bc | POOM request while Dialing\r\n
0xd00000bd | Playing an event sound in Call Progress sink\r\n
0xd00000be | Stopping event sounds\r\n
0xd00000bf | Getting cellular Rx mute state\r\n
0xd00000c0 | Enumerating audio endpoints\r\n
0xd00000c1 | Enable cellular provider change\r\n
0xd00000c2 | Unknown or not possible\r\n
0xd00000c3 | Never possible\r\n
0xd00000c4 | Querying other party availability\r\n
0xd00000c5 | Other Party Unavailable\r\n
0xd00000c6 | Querying Data Connectivity\r\n
0xd00000c7 | Data Connectivity Unavailable\r\n
0xd00000c8 | Other Party and DataConnectivity Available\r\n
0xd00000c9 | Upgrade Available\r\n
0xd00000ca | Querying Remote Party Seamless Capability\r\n
0xd00000cb | Non-Seamless Upgrade Initiated\r\n
0xd00000cc | Seamless Upgrade Initiated\r\n
0xd00000cd | Upgrade Complete\r\n
0xd00000ce | App Querying Remote Party Seamless Capability\r\n
0xd00000cf | None\r\n
0xd00000d0 | CircuitSwitched\r\n
0xd00000d1 | PacketSwitched\r\n
0xd00000d2 | PacketSwitched_WiFi\r\n
0xd00000d3 | FALSE\r\n
0xd00000d4 | TRUE\r\n
0xd00000d5 | SingleLine\r\n
0xd00000d6 | MultiLine-Separate\r\n
0xd00000d7 | MultiLine-Linked\r\n
0xd00000d8 | AlertText\r\n
0xd00000d9 | ServiceOn\r\n
0xd00000da | SystemType\r\n
0xd00000db | EmergencyCallbackMode\r\n
0xd00000dc | Muted\r\n
0xd00000dd | SupportsPlusCodeDialing\r\n
0xd00000de | LocalCallWaitingToneNeeded\r\n
0xd00000df | SupportsHold\r\n
0xd00000e0 | LineSettingCapabilities\r\n
0xd00000e1 | Capabilities\r\n
0xd00000e2 | OperatorName\r\n
0xd00000e3 | OperatorNumericName\r\n
0xd00000e4 | BroadcastText\r\n
0xd00000e5 | CountryCode\r\n
0xd00000e6 | RegistrationState\r\n
0xd00000e7 | RegistrationRejectReason\r\n
0xd00000e8 | SimState\r\n
0xd00000e9 | CurrentMcc\r\n
0xd00000ea | SimStateLockInfo\r\n
0xd00000eb | SimUnlockAttemptsRemaining\r\n
0xd00000ec | SimUnblockAttemptsRemaining\r\n
0xd00000ed | PersoFeature\r\n
0xd00000ee | PersoState\r\n
0xd00000ef | PersoUnlockAttemptsRemaining\r\n
0xd00000f0 | PersoUnblockAttemptsRemaining\r\n
0xd00000f1 | SignalStrength\r\n
0xd00000f2 | SubscriberAddress\r\n
0xd00000f3 | BrandingImagePath\r\n
0xd00000f4 | LineBrandingFlags\r\n
0xd00000f5 | SmallIconPath\r\n
0xd00000f6 | CallForwardingState\r\n
0xd00000f7 | CallForwardingAddress\r\n
0xd00000f8 | CallerIdSetting\r\n
0xd00000f9 | AccountFriendlyName\r\n
0xd00000fa | SortKey\r\n
0xd00000fb | IgnoreUssdExclusions\r\n
0xd00000fc | UssdExclusionList\r\n
0xd00000fd | SlotIndex\r\n
0xd00000fe | VoicemailAddress\r\n
0xd00000ff | VoicemailProvisioningState\r\n
0xd0000100 | VoicemailConnectivityState\r\n
0xd0000101 | VoicemailCount\r\n
0xd0000102 | CurrentMnc\r\n
0xd0000103 | VideoCallingEnabled\r\n
0xd0000104 | NotStarted\r\n
0xd0000105 | InProgress\r\n
0xd0000106 | Complete\r\n
0xd0000107 | Initializing\r\n
0xd0000108 | Unavailable\r\n
0xd0000109 | Idle\r\n
0xd000010a | Starting\r\n
0xd000010b | Recording\r\n
0xd000010c | Pausing\r\n
0xd000010d | Paused\r\n
0xd000010e | Resuming\r\n
0xd000010f | Finishing\r\n
0xd0000110 | End\r\n
0xd0000111 | Begin\r\n
0xd0000112 | Cancel\r\n
0xd0000113 | PhoneLineChangeKind_Added\r\n
0xd0000114 | PhoneLineChangeKind_Removed\r\n
0xd0000115 | PhoneLineChangeKind_PropertiesChanged\r\n
0xd0000116 | UdmCallItemEventType_EventMissed\r\n
0xd0000117 | UdmCallItemEventType_EventCreate\r\n
0xd0000118 | UdmCallItemEventType_EventDelete\r\n
0xd0000119 | UdmCallItemEventType_EventDeleteAll\r\n
0xd000011a | UdmCallItemEventType_EventModify\r\n
0xd000011b | UdmCallItemEventType_EventConnectionBroken\r\n
0xd000011c | RcsMediaType_None\r\n
0xd000011d | RcsMediaType_AudioOnly\r\n
0xd000011e | RcsMediaType_AudioVideo\r\n
0xd000011f | VideoCallingSetting_Disabled\r\n
0xd0000120 | VideoCallingSetting_Enabled\r\n
0xd0000121 | VideoCallingSetting_CachedValue\r\n
0xd0000122 | RcsServiceStatus_Stopped\r\n
0xd0000123 | RcsServiceStatus_Started\r\n
0xd0000124 | RcsServiceStatus_Stopping\r\n
0xd0000125 | RcsServiceStatus_Starting\r\n
0xd0000126 | RcsPublishRequestReason_Expired\r\n
0xd0000127 | RcsPublishRequestReason_NetworkChange\r\n
0xd0000128 | RcsNetworkType_Unknown\r\n
0xd0000129 | RcsNetworkType_Lte\r\n
0xd000012a | RcsNetworkType_LteNoVoPS\r\n
0xd000012b | RcsNetworkType_Ehrpd\r\n
0xd000012c | RcsNetworkType_HspaPlus\r\n
0xd000012d | RcsNetworkType_3g\r\n
0xd000012e | RcsNetworkType_2g\r\n
0xd000012f | RcsNetworkType__WLAN\r\n
0xd0000130 | RcsNetworkType__IWLAN\r\n
0xd0000131 | Automatic\r\n
0xd0000132 | BluetoothHeadset\r\n
0xd0000133 | SpeakerPhone\r\n
0xf0000001 | CallVerb_Dial\r\n
0xf0000002 | CallVerb_End\r\n
0xf0000003 | CallVerb_DropActiveAcceptHeld\r\n
0xf0000004 | CallVerb_Hold\r\n
0xf0000005 | CallVerb_Unhold\r\n
0xf0000006 | CallVerb_Swap\r\n
0xf0000007 | CallVerb_Private\r\n
0xf0000008 | CallVerb_Conference\r\n
0xf0000009 | CallVerb_Flash\r\n
0xf000000a | CallVerb_RejectIncoming\r\n
0xf000000b | CallVerb_AcceptIncoming\r\n
0xf000000c | CallVerb_SendDtmf\r\n
0xf000000d | CallVerb_StartDtmf\r\n
0xf000000e | CallVerb_StopDtmf\r\n
0xf000000f | CallVerb_DropFromConference\r\n
0xf0000010 | CallVerb_DisableLocalVideo\r\n
0xf0000011 | CallVerb_EnableLocalVideo\r\n
0xf0000012 | CallVerb_AddVideo\r\n
0xf0000013 | CallVerb_DropVideo\r\n
0xf0000014 | CallVerb_AcceptIncomingVideo\r\n
0xf0000015 | CallVerb_RejectIncomingVideo\r\n
0xf0000016 | CallVerb_SetVideoPaused\r\n
0xf0000017 | CallVerb_StartRecording\r\n
0xf0000018 | CallVerb_PauseRecording\r\n
0xf0000019 | CallVerb_StopRecording\r\n
0xf000001a | BGS_BTCM_RUNNING\r\n
0xf000001b | BGS_RADIO_ENABLED\r\n
0xf000001c | BGS_INQUIRY_IN_PROGRESS\r\n
0xf000001d | BGS_DEVICE_CONNECTED\r\n
0xf000001e | BGS_PHONE_CONNECTED\r\n
0xf000001f | BGS_AUDIO_CONNECTED\r\n
0xf0000020 | VideoCalling\r\n
0xf0000021 | PhoneLineProperties_BrandingOptions\r\n
0xf0000022 | PhoneLineProperties_CanDial\r\n
0xf0000023 | PhoneLineProperties_CellularDetails\r\n
0xf0000024 | PhoneLineProperties_DisplayColor\r\n
0xf0000025 | PhoneLineProperties_DisplayName\r\n
0xf0000026 | PhoneLineProperties_NetworkName\r\n
0xf0000027 | PhoneLineProperties_NetworkState\r\n
0xf0000028 | PhoneLineProperties_Transport\r\n
0xf0000029 | PhoneLineProperties_Voicemail\r\n

### 10.0.15063.0

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
0xb000000a | %1\r\n
0xb0000064 | The Phone service is starting\r\n
0xb0000065 | The Phone service has started\r\n
0xb0000066 | The Phone service failed to start with error %1\r\n
0xb0000067 | The Phone service is stopping\r\n
0xb0000068 | The Phone service has stopped\r\n
0xb0000258 | PH_MSG: %1 with supsvc code or SIM error: %2\r\n
0xb0000259 | USSD Message: %1 suppressed due to emergency call\r\n
0xb000025a | PhoneService: Phone RPC server started. Setting PhoneApiReady.\r\n
0xb000025b | PhoneService: Stopping Phone RPC server.\r\n
0xb00002bc | CallState Change for callId: %1, from %2 to %3\r\n
0xb00002be | Controller request to provider %1: verb %2 id: %3 hr: %4\r\n
0xb00002bf | Controller request result from provider %1: verb %2 id: %3 hr: %4\r\n
0xb00002c0 | Dialing: Got call handle from provider\r\n
0xb00002c1 | Dialing: Failed due to existing outgoing call\r\n
0xb00002c2 | Phone dialing %1\r\n
0xb00002c4 | Fake Call Added: %1\r\n
0xb00002c8 | Controller added call history record with Oid: %1 hr %2\r\n
0xb00002c9 | Dialing rules start\r\n
0xb00002ca | Dialing rules end: modified by rule %1, rule processing time %2 ms.\r\n
0xb00002cb | Dialing: Failed because there are already two calls.\r\n
0xb00002cc | Dialing: Failed because the active call cannot be held.\r\n
0xb00002cd | Controller holding call %1 to accept call %2.\r\n
0xb00002ce | Controller dropping held call %1 to accept call %2.\r\n
0xb00002cf | Controller using DropAccept for incoming, dropping call %1 to accept %2.\r\n
0xb00002d0 | [CellularAudio] Setting audio endpoint to %1\r\n
0xb00002d1 | [CellularAudio] Notified of audio routing endpoint change to %1\r\n
0xb00002d2 | [CellularAudio] Notified of bluetooth state change to %1\r\n
0xb00002d3 | [CellularAudio] Enabling phone call audio to endpoint %1; IsIncoming %2\r\n
0xb00002d4 | [CellularAudio] Disabling phone call audio\r\n
0xb00002d6 | Phone service failed to initialize UDM or CallHistoryItemWriter.  Call history entries will not be written.  HRESULT: %1\r\n
0xb00002d7 | Phone service failed to initialize External VVM manager.  VVM apps will not be able to control audio. HRESULT: %1\r\n
0xb00002d8 | Phone service failed to initialize POOM.  Caller ID information will not be available. HRESULT: %1\r\n
0xb00002d9 | [CellularAudio] Tone Notification: %1, digits %2, on %3, off %4\r\n
0xb00002da | Controller OnFinished called for requestId %1 hr: %2\r\n
0xb00002db | Rejected incoming call. Line id: %1 Call Id: %2 reason: %3 \r\n
0xb00002dc | [CellularAudio] Enabling cellular audio: %1 on executor %2\r\n
0xb00002dd | [CellularAudio] Disabling cellular audio: %1 on executor %2\r\n
0xb00002de | VOIP audio count ref increased\r\n
0xb00002df | VOIP audio count ref Decreased\r\n
0xb00002e0 | VOIP muting audio\r\n
0xb00002e1 | VOIP unmuting audio\r\n
0xb00002e2 | PhoneController - phone line added. id: %1, type: %2\r\n
0xb00002e3 | PhoneController - phone line removed. id: %1\r\n
0xb00002e4 | PhoneController - line property: %2 value: %3 for line ID:%1\r\n
0xb00002e6 | [CellularAudio] ExecutorIndex: %1 already initialized for audio\r\n
0xb00002e7 | [CellularAudio] Muting cellular TX audio: %1 on executor %2, muted: %3\r\n
0xb00002e8 | [CellularAudio] Muting cellular RX audio: %1 on executor %2, muted: %3\r\n
0xb00002e9 | EndUpgradeOriginationCall invoked for upgrade guid %1\r\n
0xb00002ea | CancelUpgrade invoked for upgrade guid %1\r\n
0xb00002eb | [CellularAudio] Enabling cellular provider change, [executorIndex=%1][cellularAudioType=%2][operation=%3]\r\n
0xb00002ec | [CellularAudio] Invalid cellular provider change attempted, [executorIndex=%1][targetAudioType=%2][operation=%3][currentAudioType=%4][isInHandover=%5]\r\n
0xb00002ed | [CellularAudio] Handover in progress, cellular audio type change not allowed [executorIndex=%1][cellularAudioType=%2][audioActive=%3]\r\n
0xb00002ee | Phone call swap was ignored. Call to hold: %1. Call to unhold: %2.\r\n
0xb00002ef | Calculation for time between call swaps was completed. Allow swap is %1. Last successful swap was %2 ms ago. The device is configured to wait at least %3 ms in between swaps.\r\n
0xb00002f0 | CallProgress - Determined sound configuration according to country code, [LineId=%1][CountryCode=%2][InCallToneType=%3][InCallToneName=%4]\r\n
0xb00002f1 | Disable and enable cellular audio. Disable Executor Index: %1, Enable Executor Index: %2, Cellular Audio Type: %3, Audio Active: %4\r\n
0xb00002f2 | CallProgress - Using override country code for determining tone configuration, [CountryCode=%1][OverrideCountryCode=%2]\r\n
0xb00002f3 | CallProgress - Failed to get 3GPP in call tone for type and mcc, [CountryCode=%1][InCallToneType=%2][HRESULT=%3]\r\n
0xb00002f4 | CallProgress - Failed to get 3GPP in call tone, [HRESULT=%1]\r\n
0xb0000384 | Event sound: %1\r\n
0xb0000418 | Emergency Number: received updated list %1\r\n
0xb0000419 | Emergency Number: Dial request for callid %1\r\n
0xb000041a | Emergency Number list received null argument or empty list.\r\n
0xb000041b | Dialing: Failed because the line attempt to dial is not free.\r\n
0xb000041c | OperationWatchdog: "%1" timed out.  Context: %2.  Timeout value: %3ms.  Still waiting after: %4ms.\r\n
0xb000041d | OperationWatchdog: "%1" completed.  Context: %2.  Actual time: %3ms\r\n
0xb000041e | Async API context %1 completed with result %2\r\n
0xb000041f | Phone service listener added: %1\r\n
0xb0000420 | Phone service listener removed: %1\r\n
0xb0000421 | Phone service listener lost notifications: %1\r\n
0xb0000423 | Phone service listener rundown: %1\r\n
0xb0000424 | Phone notification sent: %1 error: %2\r\n
0xb0000429 | Call Upgrade state for CallId: %1 Changed From: %2 To: %3\r\n
0xb000042a | Data Connectivity State: %1\r\n
0xb000042d | Non-seamless upgrade was cancelled by the user.\r\n
0xb000042e | Seamless upgrade was cancelled by the user.\r\n
0xb000042f | Connection Manager Error. Connection Manager Result: %1.\r\n
0xb0000430 | Call Line Change for CallId: %1 from LineId: %2 to LineId: %3\r\n
0xb0000432 | PhoneTileManager: Creating secondary Phone Tile with id: %1\r\n
0xb0000433 | PhoneTileManager: Setting the primary Phone Tile to be assigned to PhoneLineId: %1\r\n
0xb0000434 | PhoneTileManager: Deleting Phone Tile with id: %1\r\n
0xb0000436 | PhoneTile: Committed an update to the Phone Tile with tile id: %1. Title %2; Tile mode: %3; has voicemail: %4; missed call count: %5; has large content: %6\r\n
0xb0000438 | PhoneTileControllerSink: The PhoneLine (%1) has been removed.  Removing its tile and updating any remaining tiles as necessary.\r\n
0xb000043f | PhoneTileControllerSink: ShellReadyState changed to %1\r\n
0xb0000440 | SystemEventTriggerControllerSink: LineChangedTrigger fired with: LineId %1: PhoneLineChangeKind %2: PhoneLineProperties: %3: hr: %4\r\n
0xb0000441 | SystemEventTriggerControllerSink: NewVoicemailMessageTrigger fired with: LineId %1: voicemailCount %2: VoicemailMessage: %3: hr: %4\r\n
0xb0000442 | SystemEventTriggerControllerSink: CallOriginDataRequestTrigger fired with: RequestId %1: PhoneNumber: %2: hr: %3\r\n
0xb0000443 | SystemEventTriggerControllerSink: CallHistoryChanged fired with: hr: %1\r\n
0xb0000444 | SystemEventTriggerControllerSink: AirplaneModeDisabledForEmergencyCall fired with: hr: %1\r\n
0xb0000445 | SystemEventTriggerControllerSink: OnCallEvent called with: event: %1\r\n
0xb0000446 | SystemEventTriggerControllerSink: Attempted to advise to CallHistorySession with: hr: %1\r\n
0xb0000447 | IR94FeatureDisabled: Returning video capability sharing as disabled.\r\n
0xb0000448 | IR94FeatureDisabled: Returning device not video capable.\r\n
0xb0000449 | IR94FeatureDisabled: Returning video calling switch as not actionable.\r\n
0xb000044a | SystemEventTriggerControllerSink: LineChangedTrigger suppressed [LineId=%1][PhoneLineChangeKind=%2][PhoneLineProperties=%3]\r\n
0xb000044b | SystemEventTriggerControllerSink: Received shell ready notification.\r\n
0xb000044c | SystemEventTriggerControllerSink: OnShellReady started [existingInitialBootSequenceComplete=%1][cachedLineCount=%2]\r\n
0xb000044d | SystemEventTriggerControllerSink: OnShellReady triggering deferred notification [LineId=%1][PhoneLineChangeKind=%2][PhoneLineProperties=%3]\r\n
0xb000044e | SystemEventTriggerControllerSink: Received screen state change notification [monitorState=%1].\r\n
0xb000044f | SystemEventTriggerControllerSink: OnScreenStateChange started [existingSuppressLineChangedTrigger=%1][screenIsOn=%2]\r\n
0xb0000450 | SystemEventTriggerControllerSink: OnScreenStateChange triggering deferred notification [LineId=%1][PhoneLineChangeKind=%2][PhoneLineProperties=%3]\r\n
0xb0000451 | SystemEventTriggerControllerSink: LineChangedTrigger skipped [LineId=%1]\r\n
0xb00004b1 | InteractiveUserNotificationSink: New Incoming Call State Changed [callId=%1].\r\n
0xb00004b2 | InteractiveUserNotificationSink: Show Incoming Call Toast [callId=%1].\r\n
0xb00004b3 | Supplementary service code: %1 was converted from erase to deactivate command due override setting.\r\n
0xb00004b4 | InteractiveUserNotificationSink: Call belongs to Win32 app, skipping [callId=%1].\r\n
0xb00005dd | Call data collection item added for CallId: [%1]\r\n
0xb00005de | Call data collection item removed for CallId: [%1]\r\n
0xb00005df | Call data collection item dropped an idle call for CallId: [%1]\r\n
0xb00005e0 | CallHistoryItemWriter: Call with id %1 is added.\r\n
0xb00005e1 | CallHistoryItemWriter: Call with id %1 is updated.\r\n
0xb00005e2 | CallAnnotationsLookupConnecting: Establishing RPC connection.  Endpoint: %1\r\n
0xb00005e3 | CallAnnotationsLookup: Querying location.  Phone number: %1\r\n
0xb00005e4 | CallAnnotationsLookup: Completed location query.  Location: %1\r\n
0xb00005e5 | CallAnnotationsLookup: RPC failure, clearing RPC connection.\r\n
0xb00005e6 | CallAnnotationsManager: Call: %1 LookupState: %2\r\n
0xb00005e7 | Shutting down Phone service due to idle stop.\r\n
0xb00005e8 | Service Idle Callback received. Idle status: %1, Phone calls exist: %2\r\n
0xb00005e9 | CallRecording VALID state change from '%2' to '%3' on executor %1\r\n
0xb00005ea | CallRecording: INVALID state change from '%2' to '%3' on executor %1\r\n
0xb00005eb | CallRecording: Recorded call is now idle.  Recording will end.  LineId:%1, CallId:%2, ConferenceCallId:%3\r\n
0xb00005ec | CallRecording: Recorded call is now held.  Recording will pause and may finish.  LineId:%1, CallId:%2, ConferenceCallId:%3\r\n
0xb00005ed | CallRecording: A call that is not being recorded is talking.  Recording will finish.  LineId:%1, CallId:%2, ConferenceCallId:%3\r\n
0xb00005ee | CallRecording: Recorded call no longer exists.  Recording will finish.  LineId:%2, CallId:%1\r\n
0xb00005ef | CallRecording: Preferred recording application changed.  Old Package Family Name: '%1', New Package Family Name: '%2'\r\n
0xb00005f0 | Call [callId=%1] marked as handover merged due to being conferenced with call [callState=%2] that ended with handover merged reason\r\n
0xb00005f1 | CallRecordingOff: %1, Preferred Recording app PFN: %2\r\n
0xb00005f2 | CallRecordingApplication %1 detected\r\n
0xb0000640 | [RcsPresence] Request Capabilities: %1\r\n
0xb0000641 | [RcsPresence] Received query response, [responseCode=%1][reason=%2]\r\n
0xb0000642 | [RcsPresence] Received %1 capability tuple(s)\r\n
0xb0000643 | [RcsPresence] Tuple %1, MediaType not video capable: %2\r\n
0xb0000644 | [RcsPresence] Tuple %1, ServiceIdentifier not video capable: %2\r\n
0xb0000645 | [RcsPresence] Tuple %1 is video capable.\r\n
0xb0000646 | [RcsPresence] RcsPresenceCache hit, [TelUri string=%1][Capabilities returned=%2]\r\n
0xb0000647 | [RcsPresence] Query suppressed due to capabilities sharing opt-in settings, [TelUri string=%1][Capabilities returned=%2]\r\n
0xb0000648 | Checking for device support of video calling. This service (%1) exists, thus video calling is supported.\r\n
0xb0000649 | Checking for device support of video calling. This service (%2) does NOT exist due to error code %1, thus a different service would have to exist for video calling to be supported.\r\n
0xb000064a | PhoneController - Updating video calling settings, [lineId=%1][videoCallingSetting=%2][cacheVideoCallingSetting=%3][userRequest=%4][TTYEnabled=%5][cellularDataEnabled=%6]\r\n
0xb000064b | CallRecording: Deferred request to disable cellular audio: %1 on executor %2\r\n
0xb000064c | CallRecording: Cancelled request to defer disabling of cellular audio: %3 due to enabling of: %1 on executor %2\r\n
0xb000064d | CallRecording: An audio type change prevented deferring of audio disable.  New audio type: %1, Audio type being disabled: %3 on executor %2\r\n
0xb000064e | CallRecording: Performing deferred request to disable cellular audio: %1 on executor %2\r\n
0xb000064f | [RcsPresence] Received OnPublishRequested\r\n
0xb0000650 | [RcsPresence] Suppressed publishing actual video capability as UCE capability sharing is disabled.\r\n
0xb0000651 | [RcsPresence] Video capability sharing settings update requested [isCapabilitySharingEnabled=%1][previousValue=%2].\r\n
0xb0000652 | [RcsPresence] Cache initialized [cacheExpirationInSeconds=%1]\r\n
0xb0000653 | [RcsPresence] Publishing capabilities [%1]\r\n
0xb0000654 | [RcsPresence] Initializing RCS presence service\r\n
0xb0000655 | [RcsPresence] RCS presence service status queried, [status=%1]\r\n
0xb0000656 | [RcsPresence] Starting RCS presence service\r\n
0xb0000657 | [RcsPresence] Received publish response, [responseCode=%1][reason=%2]\r\n
0xb0000658 | [RcsPresence] Received OnNetworkSupportVideoChanged, [updatedValue=%1][previousValue=%2]\r\n
0xb0000659 | [RcsPresence] Saved last published capabilities, [updatedValue=%1][previousValue=%2]\r\n
0xb000065a | [RcsPresence] Publish capabilities requested, [reason=%1][networkType=%2]\r\n
0xb000065b | Attempting audio routing {%1} as per settings.\r\n
0xb000065c | Updating callInfo with remote party hold status [callId=%1][supSvcCode=%2]\r\n
0xb000065d | Caller ID privacy header set to: {%1}\r\n
0xb000065e | The prefix {%1} was dialed which is prohibited. The call failed.\r\n
0xb000065f | A Wireless Priority Service call failed because of another active IMS call.\r\n
0xb0000660 | Adding call to conference [lineId=%1][callId=%2][conferenceId=%3]\r\n
0xb0000661 | Removing call from conference [lineId=%1][callId=%2][conferenceId=%3]\r\n
0xb0000662 | Updating CallInfo confererence participant property [callId=%1][isParticipant=%2]\r\n
0xd0000001 | PH_CALLSTATE_AMBIGUOUS\r\n
0xd0000002 | PH_CALLSTATE_INCOMING\r\n
0xd0000003 | PH_CALLSTATE_CALLING\r\n
0xd0000004 | PH_CALLSTATE_TALKING\r\n
0xd0000005 | PH_CALLSTATE_HOLD\r\n
0xd0000006 | PH_CALLSTATE_IDLE\r\n
0xd0000007 | PH_CALLSTATE_TRANSFERRING\r\n
0xd0000008 | RejectIncomingReason_UserRequest\r\n
0xd0000009 | RejectIncomingReason_OtherIncomingCall\r\n
0xd000000a | RejectIncomingReason_EmergencyMode\r\n
0xd000000b | RejectIncomingReason_Filtered\r\n
0xd000000c | PH_MSG_SIMPHONEBOOKENTRY\r\n
0xd000000d | PH_MSG_SUPSVCEXECUTING\r\n
0xd000000e | PH_MSG_SUPSVCSUCCEEDED\r\n
0xd000000f | PH_MSG_SUPSVCFAILED\r\n
0xd0000010 | PH_MSG_USSDEXECUTING\r\n
0xd0000011 | PH_MSG_USSDEXECUTED_FURTHER_INFO_REQUIRED\r\n
0xd0000012 | PH_MSG_USSDEXECUTED_NO_FURTHER_INFO_REQUIRED\r\n
0xd0000013 | PH_MSG_CALLEE_INCOMING_CALLS_BARRED\r\n
0xd0000014 | PH_MSG_VOICEMAIL\r\n
0xd0000015 | PH_MSG_MISSEDCALL\r\n
0xd0000016 | PH_MSG_SPEAKERPHONEON\r\n
0xd0000017 | PH_MSG_SERVICEAUTOENABLED\r\n
0xd0000018 | PH_MSG_CURRENTLY_IN_ECBM\r\n
0xd0000019 | PH_MSG_ECBMIDLE\r\n
0xd000001a | PH_MSG_NOT_CURRENTLY_IN_ECBM\r\n
0xd000001b | PH_MSG_ERRORCALLDROPPED\r\n
0xd000001c | PH_MSG_ERRORNETWORKDROPPED\r\n
0xd000001d | PH_MSG_ERRORINVALIDDESTADDRESS\r\n
0xd000001e | PH_MSG_ERRORNOTADMIN\r\n
0xd000001f | PH_MSG_ERRORCONFERENCEFAILED\r\n
0xd0000020 | PH_MSG_ERRORVOICEMAILSWITCHLINES\r\n
0xd0000021 | PH_MSG_ERROREND\r\n
0xd0000022 | PH_MSG_ERRORPRIVATE\r\n
0xd0000023 | PH_MSG_ERRORANSWER\r\n
0xd0000024 | PH_MSG_ERRORFLASH\r\n
0xd0000025 | PH_MSG_ERRORHOLD\r\n
0xd0000026 | PH_MSG_ERRORSWAP\r\n
0xd0000027 | PH_MSG_ERRORUNHOLD\r\n
0xd0000028 | PH_MSG_ERRORMUTE\r\n
0xd0000029 | PH_MSG_ERRORUNMUTE\r\n
0xd000002a | PH_MSG_ERRORDIAL\r\n
0xd000002b | PH_MSG_ERRORNODIALTONE\r\n
0xd000002c | PH_MSG_ERRORUNREACHABLE\r\n
0xd000002d | PH_MSG_ERRORBADADDRESS\r\n
0xd000002e | PH_MSG_ERRORSIMBUSY\r\n
0xd000002f | PH_MSG_ERRORNETWORKSERVICENOTAVAILABLE\r\n
0xd0000030 | PH_MSG_ERROREMERGENCYONLY\r\n
0xd0000031 | PH_MSG_ERRORRADIOOFF\r\n
0xd0000032 | PH_MSG_ERROROPERATIONFAILED\r\n
0xd0000033 | PH_MSG_ERROROUTGOINGCALLNOFREELINES\r\n
0xd0000034 | PH_MSG_ERRORNOVMAILNUMBER\r\n
0xd0000035 | PH_MSG_ERRORTRANSFER\r\n
0xd0000036 | PH_MSG_SIMSECNEEDED\r\n
0xd0000037 | PH_MSG_EXT\r\n
0xd0000038 | PH_MSG_ERRORDESTINATIONBARRED\r\n
0xd0000039 | PH_MSG_ERRORFDNRESTRICT\r\n
0xd000003a | PH_MSG_ERRORDTMF\r\n
0xd000003b | PH_MSG_ERRORCHLD1\r\n
0xd000003c | PH_MSG_ERRORCALLFORWARDRETRIEVE\r\n
0xd000003d | PH_MSG_ERRORCALLFORWARDAPPLY\r\n
0xd000003e | PH_MSG_DISMISSSUPSVCS\r\n
0xd000003f | PH_MSG_SIMUNLOCK\r\n
0xd0000040 | PH_MSG_ERRORROAMRESTRICT\r\n
0xd0000041 | PH_MSG_SEAMLESS_UPGRADE\r\n
0xd0000042 | PH_MSG_UPGRADE_ERROR\r\n
0xd0000043 | PH_MSG_ERRORDISABLELOCALVIDEO\r\n
0xd0000044 | PH_MSG_ERRORENABLELOCALVIDEO\r\n
0xd0000045 | PH_MSG_ERRORADDVIDEO\r\n
0xd0000046 | PH_MSG_ERRORDROPVIDEO\r\n
0xd0000047 | PH_MSG_ERRORACCEPTVIDEO\r\n
0xd0000048 | PH_MSG_ERRORREJECTVIDEO\r\n
0xd0000049 | PH_MSG_ERRORSETVIDEOPAUSED\r\n
0xd000004a | PH_MSG_ERRORVIDEOCALLINGOFF\r\n
0xd000004b | PH_MSG_VOIP_INSTALL_PROMPT\r\n
0xd000004c | PH_MSG_ERRORSTARTRECORDING\r\n
0xd000004d | PH_MSG_ERRORPAUSERECORDING\r\n
0xd000004e | PH_MSG_ERRORSTOPRECORDING\r\n
0xd000004f | PH_MSG_VIDEOCHARGESPROMPT\r\n
0xd0000050 | PH_MSG_ERROREXPLICITCALLTRANSFER\r\n
0xd0000051 | PH_MSG_WIFICALLINGUPSELLPROMPT\r\n
0xd0000052 | PH_MSG_LAST\r\n
0xd0000053 | PhoneCallAudio_DefaultEndpointPerRoutingPolicy\r\n
0xd0000054 | PhoneCallAudio_Speakerphone\r\n
0xd0000055 | PhoneCallAudio_Handset\r\n
0xd0000056 | PhoneCallAudio_WiredHeadset\r\n
0xd0000057 | PhoneCallAudio_WiredHeadsetWithMicrophone\r\n
0xd0000058 | PhoneCallAudio_BluetoothSco\r\n
0xd0000059 | PhoneCallAudio_BluetoothScoWithNREC\r\n
0xd000005a | PhoneTone_None\r\n
0xd000005b | PhoneTone_Off\r\n
0xd000005c | PhoneTone_DTMF_Start\r\n
0xd000005d | PhoneTone_DTMF_Stop\r\n
0xd000005e | PhoneTone_DTMF_Burst\r\n
0xd000005f | PhoneTone_3GPP_RingBack\r\n
0xd0000060 | PhoneTone_3GPP2_Reorder\r\n
0xd0000061 | PhoneTone_3GPP2_Busy\r\n
0xd0000062 | PhoneTone_3GPP2_CallWaiting\r\n
0xd0000063 | PhoneTone_3GPP2ISDNAlerting_PingRing\r\n
0xd0000064 | PH_CHANGEEVENT_ALL\r\n
0xd0000065 | PH_CHANGEEVENT_PHONESTATE\r\n
0xd0000066 | PH_CHANGEEVENT_ACTIONAVAILABILITY\r\n
0xd0000067 | PH_CHANGEEVENT_MUTE\r\n
0xd0000068 | PH_CHANGEEVENT_SPEAKER\r\n
0xd0000069 | PH_CHANGEEVENT_BLUETOOTHHANDSFREE\r\n
0xd000006a | PH_CHANGEEVENT_PROVIDERGENERALINFO\r\n
0xd000006b | PH_CHANGEEVENT_PROVIDERLINESERVICEINFO\r\n
0xd000006c | PH_CHANGEEVENT_PROVIDERLINEINFO\r\n
0xd000006d | PH_CHANGEEVENT_PROVIDERSIGNALSTRENGTH\r\n
0xd000006e | PH_CHANGEEVENT_VVM_CONNECTIVITY_STATE\r\n
0xd000006f | PH_CHANGEEVENT_ERROR\r\n
0xd0000070 | PH_CHANGEEVENT_ALERTMSG\r\n
0xd0000071 | PH_CHANGEEVENT_MODIFY_VOICEMAILADDRESS\r\n
0xd0000072 | PH_CHANGEEVENT_MODIFY_CALLERID\r\n
0xd0000073 | PH_CHANGEEVENT_MODIFY_CALLFORWARDING\r\n
0xd0000074 | PH_CHANGEEVENT_SIMSEC_UNLOCK\r\n
0xd0000075 | PH_CHANGEEVENT_SIMSEC_ENABLE\r\n
0xd0000076 | PH_CHANGEEVENT_SIMSEC_DISABLE\r\n
0xd0000077 | PH_CHANGEEVENT_SIMSEC_CHANGEPIN\r\n
0xd0000078 | PH_CHANGEEVENT_SIMSEC_FDN_CHANGEPIN2\r\n
0xd0000079 | PH_CHANGEEVENT_SIMSEC_FDN_GETPIN2\r\n
0xd000007a | PH_CHANGEEVENT_SIMSEC_UICLOSED\r\n
0xd000007b | PH_CHANGEEVENT_CELLULARLINECOMPONENTSCHANGED\r\n
0xd000007c | PH_CHANGEEVENT_PROVIDERLINELOCKINFO\r\n
0xd000007d | PH_CHANGEEVENT_ASYNC_OPERATION_SUCCESS\r\n
0xd000007e | PH_CHANGEEVENT_ASYNC_OPERATION_FAILURE\r\n
0xd000007f | PH_CHANGEEVENT_DEFAULTOUTGOINGLINE\r\n
0xd0000080 | PH_CHANGEEVENT_AGGREGATEBRANDING\r\n
0xd0000081 | PH_CHANGEEVENT_BRANDINGTEXT\r\n
0xd0000082 | PH_CHANGEEVENT_MODIFY_VIDEOCALLING\r\n
0xd0000083 | PH_CHANGEEVENT_LINEADDED\r\n
0xd0000084 | PH_CHANGEEVENT_LINEREMOVED\r\n
0xd0000085 | PH_CHANGEEVENT_LAUNCH_EMERGENCY_DIALER\r\n
0xd0000086 | PH_CHANGEEVENT_ENUM_COUNT\r\n
0xd0000087 | PH_ERROR_NONE\r\n
0xd0000088 | PH_ERROR_CALLDROPPED\r\n
0xd0000089 | PH_ERROR_NETWORKDROPPED\r\n
0xd000008a | PH_ERROR_CONFERENCEFAILED\r\n
0xd000008b | PH_ERROR_END\r\n
0xd000008c | PH_ERROR_PRIVATE\r\n
0xd000008d | PH_ERROR_ANSWER\r\n
0xd000008e | PH_ERROR_FLASH\r\n
0xd000008f | PH_ERROR_HOLD\r\n
0xd0000090 | PH_ERROR_SWAP\r\n
0xd0000091 | PH_ERROR_UNHOLD\r\n
0xd0000092 | PH_ERROR_MUTE\r\n
0xd0000093 | PH_ERROR_UNMUTE\r\n
0xd0000094 | PH_ERROR_DIAL\r\n
0xd0000095 | PH_ERROR_BADADDRESS\r\n
0xd0000096 | PH_ERROR_INVALIDSIM\r\n
0xd0000097 | PH_ERROR_NETWORKSERVICENOTAVAILABLE\r\n
0xd0000098 | PH_ERROR_EMERGENCYONLY\r\n
0xd0000099 | PH_ERROR_SERVICEOFF\r\n
0xd000009a | PH_ERROR_OPERATIONFAILED\r\n
0xd000009b | PH_ERROR_OUTGOINGCALLNOFREELINES\r\n
0xd000009c | PH_ERROR_TRANSFER\r\n
0xd000009d | UNUSED_PH_ERROR_22\r\n
0xd000009e | PH_ERROR_FDNRESTRICT\r\n
0xd000009f | PH_ERROR_SENDDTMF\r\n
0xd00000a0 | PH_ERROR_DROPACCEPT\r\n
0xd00000a1 | UNUSED_PH_ERROR_26\r\n
0xd00000a2 | PH_ERROR_SIMSECNEEDED\r\n
0xd00000a3 | PH_ERROR_CALLFORWARDRETRIEVE\r\n
0xd00000a4 | PH_ERROR_CALLFORWARDAPPLY\r\n
0xd00000a5 | PH_ERROR_ROAMRESTRICT\r\n
0xd00000a6 | PH_ERROR_DISABLELOCALVIDEO\r\n
0xd00000a7 | PH_ERROR_ENABLELOCALVIDEO\r\n
0xd00000a8 | PH_ERROR_ADDVIEO\r\n
0xd00000a9 | PH_ERROR_DROPVIDEO\r\n
0xd00000aa | PH_ERROR_ACCEPTVIDEO\r\n
0xd00000ab | PH_ERROR_REJECTVIDEO\r\n
0xd00000ac | PH_ERROR_SETVIDEOPAUSED\r\n
0xd00000ad | PH_ERROR_VIDEOCALLINGOFF\r\n
0xd00000ae | PH_ERROR_COUNT\r\n
0xd00000af | Critical section held\r\n
0xd00000b0 | Waiting on critical section\r\n
0xd00000b1 | Enable audio routing\r\n
0xd00000b2 | Disable audio routing\r\n
0xd00000b3 | Set audio endpoint\r\n
0xd00000b4 | Enable cellular audio\r\n
0xd00000b5 | Disable cellular audio\r\n
0xd00000b6 | Mute cellular audio rx\r\n
0xd00000b7 | Mute cellular audio tx\r\n
0xd00000b8 | Mute voip audio\r\n
0xd00000b9 | Phone Controller DispatchWork\r\n
0xd00000ba | CoreUI endpoint find\r\n
0xd00000bb | CoreUI send message\r\n
0xd00000bc | POOM request while Dialing\r\n
0xd00000bd | Playing an event sound in Call Progress sink\r\n
0xd00000be | Stopping event sounds\r\n
0xd00000bf | Getting cellular Rx mute state\r\n
0xd00000c0 | Enumerating audio endpoints\r\n
0xd00000c1 | Enable cellular provider change\r\n
0xd00000c2 | Unknown or not possible\r\n
0xd00000c3 | Never possible\r\n
0xd00000c4 | Querying other party availability\r\n
0xd00000c5 | Other Party Unavailable\r\n
0xd00000c6 | Querying Data Connectivity\r\n
0xd00000c7 | Data Connectivity Unavailable\r\n
0xd00000c8 | Other Party and DataConnectivity Available\r\n
0xd00000c9 | Upgrade Available\r\n
0xd00000ca | Querying Remote Party Seamless Capability\r\n
0xd00000cb | Non-Seamless Upgrade Initiated\r\n
0xd00000cc | Seamless Upgrade Initiated\r\n
0xd00000cd | Upgrade Complete\r\n
0xd00000ce | App Querying Remote Party Seamless Capability\r\n
0xd00000cf | None\r\n
0xd00000d0 | CircuitSwitched\r\n
0xd00000d1 | PacketSwitched\r\n
0xd00000d2 | PacketSwitched_WiFi\r\n
0xd00000d3 | FALSE\r\n
0xd00000d4 | TRUE\r\n
0xd00000d5 | SingleLine\r\n
0xd00000d6 | MultiLine-Separate\r\n
0xd00000d7 | MultiLine-Linked\r\n
0xd00000d8 | AlertText\r\n
0xd00000d9 | ServiceOn\r\n
0xd00000da | SystemType\r\n
0xd00000db | EmergencyCallbackMode\r\n
0xd00000dc | Muted\r\n
0xd00000dd | SupportsPlusCodeDialing\r\n
0xd00000de | LocalCallWaitingToneNeeded\r\n
0xd00000df | SupportsHold\r\n
0xd00000e0 | LineSettingCapabilities\r\n
0xd00000e1 | Capabilities\r\n
0xd00000e2 | OperatorName\r\n
0xd00000e3 | OperatorNumericName\r\n
0xd00000e4 | BroadcastText\r\n
0xd00000e5 | CountryCode\r\n
0xd00000e6 | RegistrationState\r\n
0xd00000e7 | RegistrationRejectReason\r\n
0xd00000e8 | SimState\r\n
0xd00000e9 | CurrentMcc\r\n
0xd00000ea | SimStateLockInfo\r\n
0xd00000eb | SimUnlockAttemptsRemaining\r\n
0xd00000ec | SimUnblockAttemptsRemaining\r\n
0xd00000ed | PersoFeature\r\n
0xd00000ee | PersoState\r\n
0xd00000ef | PersoUnlockAttemptsRemaining\r\n
0xd00000f0 | PersoUnblockAttemptsRemaining\r\n
0xd00000f1 | SignalStrength\r\n
0xd00000f2 | SubscriberAddress\r\n
0xd00000f3 | BrandingImagePath\r\n
0xd00000f4 | LineBrandingFlags\r\n
0xd00000f5 | SmallIconPath\r\n
0xd00000f6 | CallForwardingState\r\n
0xd00000f7 | CallForwardingAddress\r\n
0xd00000f8 | CallerIdSetting\r\n
0xd00000f9 | AccountFriendlyName\r\n
0xd00000fa | SortKey\r\n
0xd00000fb | IgnoreUssdExclusions\r\n
0xd00000fc | UssdExclusionList\r\n
0xd00000fd | SlotIndex\r\n
0xd00000fe | VoicemailAddress\r\n
0xd00000ff | VoicemailProvisioningState\r\n
0xd0000100 | VoicemailConnectivityState\r\n
0xd0000101 | VoicemailCount\r\n
0xd0000102 | CurrentMnc\r\n
0xd0000103 | VideoCallingEnabled\r\n
0xd0000104 | IgnoreCallerIdBlockingPrefix\r\n
0xd0000105 | CallerIdBlockingPrefixList\r\n
0xd0000106 | NotStarted\r\n
0xd0000107 | InProgress\r\n
0xd0000108 | Complete\r\n
0xd0000109 | Initializing\r\n
0xd000010a | Unavailable\r\n
0xd000010b | Idle\r\n
0xd000010c | Starting\r\n
0xd000010d | Recording\r\n
0xd000010e | Pausing\r\n
0xd000010f | Paused\r\n
0xd0000110 | Resuming\r\n
0xd0000111 | Finishing\r\n
0xd0000112 | End\r\n
0xd0000113 | Begin\r\n
0xd0000114 | Cancel\r\n
0xd0000115 | PhoneLineChangeKind_Added\r\n
0xd0000116 | PhoneLineChangeKind_Removed\r\n
0xd0000117 | PhoneLineChangeKind_PropertiesChanged\r\n
0xd0000118 | UdmCallItemEventType_EventMissed\r\n
0xd0000119 | UdmCallItemEventType_EventCreate\r\n
0xd000011a | UdmCallItemEventType_EventDelete\r\n
0xd000011b | UdmCallItemEventType_EventDeleteAll\r\n
0xd000011c | UdmCallItemEventType_EventModify\r\n
0xd000011d | UdmCallItemEventType_EventConnectionBroken\r\n
0xd000011e | RcsMediaType_None\r\n
0xd000011f | RcsMediaType_AudioOnly\r\n
0xd0000120 | RcsMediaType_AudioVideo\r\n
0xd0000121 | VideoCallingSetting_Disabled\r\n
0xd0000122 | VideoCallingSetting_Enabled\r\n
0xd0000123 | VideoCallingSetting_CachedValue\r\n
0xd0000124 | RcsServiceStatus_Stopped\r\n
0xd0000125 | RcsServiceStatus_Started\r\n
0xd0000126 | RcsServiceStatus_Stopping\r\n
0xd0000127 | RcsServiceStatus_Starting\r\n
0xd0000128 | RcsPublishRequestReason_Expired\r\n
0xd0000129 | RcsPublishRequestReason_NetworkChange\r\n
0xd000012a | RcsNetworkType_Unknown\r\n
0xd000012b | RcsNetworkType_Lte\r\n
0xd000012c | RcsNetworkType_LteNoVoPS\r\n
0xd000012d | RcsNetworkType_Ehrpd\r\n
0xd000012e | RcsNetworkType_HspaPlus\r\n
0xd000012f | RcsNetworkType_3g\r\n
0xd0000130 | RcsNetworkType_2g\r\n
0xd0000131 | RcsNetworkType__WLAN\r\n
0xd0000132 | RcsNetworkType__IWLAN\r\n
0xd0000133 | Automatic\r\n
0xd0000134 | BluetoothHeadset\r\n
0xd0000135 | SpeakerPhone\r\n
0xd0000136 | CALLCODE_PUTONHOLD\r\n
0xd0000137 | CALLCODE_RETRIEVED\r\n
0xd0000138 | SendCallerIdSetting_Unknown\r\n
0xd0000139 | SendCallerIdSetting_Never\r\n
0xd000013a | SendCallerIdSetting_ContactsOnly\r\n
0xd000013b | SendCallerIdSetting_Always\r\n
0xd000013c | SendCallerIdSetting_NetworkDefault\r\n
0xf0000001 | CallVerb_Dial\r\n
0xf0000002 | CallVerb_End\r\n
0xf0000003 | CallVerb_DropActiveAcceptHeld\r\n
0xf0000004 | CallVerb_Hold\r\n
0xf0000005 | CallVerb_Unhold\r\n
0xf0000006 | CallVerb_Swap\r\n
0xf0000007 | CallVerb_Private\r\n
0xf0000008 | CallVerb_Conference\r\n
0xf0000009 | CallVerb_Flash\r\n
0xf000000a | CallVerb_RejectIncoming\r\n
0xf000000b | CallVerb_AcceptIncoming\r\n
0xf000000c | CallVerb_SendDtmf\r\n
0xf000000d | CallVerb_StartDtmf\r\n
0xf000000e | CallVerb_StopDtmf\r\n
0xf000000f | CallVerb_DropFromConference\r\n
0xf0000010 | CallVerb_DisableLocalVideo\r\n
0xf0000011 | CallVerb_EnableLocalVideo\r\n
0xf0000012 | CallVerb_AddVideo\r\n
0xf0000013 | CallVerb_DropVideo\r\n
0xf0000014 | CallVerb_AcceptIncomingVideo\r\n
0xf0000015 | CallVerb_RejectIncomingVideo\r\n
0xf0000016 | CallVerb_SetVideoPaused\r\n
0xf0000017 | CallVerb_StartRecording\r\n
0xf0000018 | CallVerb_PauseRecording\r\n
0xf0000019 | CallVerb_StopRecording\r\n
0xf000001a | BGS_BTCM_RUNNING\r\n
0xf000001b | BGS_RADIO_ENABLED\r\n
0xf000001c | BGS_INQUIRY_IN_PROGRESS\r\n
0xf000001d | BGS_DEVICE_CONNECTED\r\n
0xf000001e | BGS_PHONE_CONNECTED\r\n
0xf000001f | BGS_AUDIO_CONNECTED\r\n
0xf0000020 | VideoCalling\r\n
0xf0000021 | PhoneLineProperties_BrandingOptions\r\n
0xf0000022 | PhoneLineProperties_CanDial\r\n
0xf0000023 | PhoneLineProperties_CellularDetails\r\n
0xf0000024 | PhoneLineProperties_DisplayColor\r\n
0xf0000025 | PhoneLineProperties_DisplayName\r\n
0xf0000026 | PhoneLineProperties_NetworkName\r\n
0xf0000027 | PhoneLineProperties_NetworkState\r\n
0xf0000028 | PhoneLineProperties_Transport\r\n
0xf0000029 | PhoneLineProperties_Voicemail\r\n
