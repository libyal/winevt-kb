## phoneproviders.dll

Path: %SystemRoot%\System32\PhoneProviders.dll

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
0xb0000064 | Enqueued verb %1, callid %2 (completion context %3)\r\n
0xb0000065 | Enqueued verb %1, callids %2, %3 (completion context %4)\r\n
0xb0000066 | Enqueued verb Dial, callid %1, callType %2, calleridoption %3 (completion context %4)\r\n
0xb0000067 | Dequeued verb %1, callid %2 (completion context %3)\r\n
0xb0000068 | Dequeued verb %1, callids %2, %3 (completion context %4)\r\n
0xb0000069 | Dequeued verb Dial, callid %1, callType %2, calleridoption %3 (completion context %4)\r\n
0xb000006a | Verb completed with HRESULT %1; host notified (completion context %2)\r\n
0xb000006b | Verb completed with HRESULT %1; host not notified (completion context %2)\r\n
0xb000006c | Began tracking async CellVoice request id %1 (for completion context %2)\r\n
0xb000006d | Stopped tracking async CellVoice request id %1 (for completion context %2)\r\n
0xb000006e | Enqueued async CellVoice request id %1 completion with HRESULT %2\r\n
0xb000006f | Gsm call manager called I3GPPCallModel::%1 with async request id %2 for callid %3 (cellvoice callid %4)\r\n
0xb0000070 | Gsm call manager called I3GPPCallModel::%1 with async request id %2 for callids %3, %4\r\n
0xb0000071 | Gsm call manager called I3GPPCallModel::RequestOutgoingCall with async request id %1 for callid %2, callType %3 (no cellvoice callid)\r\n
0xb0000072 | CallManager got call progress update for cellvoiceId %1; status %2; direction %3; number %4; name %5; party %6; flags %7; type %8; valid params %9; \r\n
0xb0000073 | CellVoice returned failure %1 to get subscriber number\r\n
0xb0000074 | CellVoice returned failure %1 to get voicemail number\r\n
0xb0000075 | CellVoice get IMSI completed with error %1\r\n
0xb0000076 | Resetting VVM state; old MCC/MNC/nameDiff %1 %2 %3\r\n
0xb0000077 | Used RIL system type %1; got signal strength %2\r\n
0xb0000078 | Used RIL system type %1; voice domain %2; got registration status %3\r\n
0xb000007a | No Visual Voicemail provider was loaded for MCC,MNC %1,%2\r\n
0xb000007b | Visual Voicemail action %1 is not currently available on this line\r\n
0xb000007c | Legacy Voicemail message received: %1. Message count: %2\r\n
0xb000007d | Registered to operator: params %1; long name "%2"; short name "%3"; numeric name"%4"; country code "%5"\r\n
0xb000007e | Switched to data registration to get registration info\r\n
0xb000007f | Status %1 from cellcore reading voicemail count %2 from SIM\r\n
0xb0000080 | Status %1 from cellcore writing voicemail count %2 to SIM\r\n
0xb0000083 | [CellularAudio] Muting cellular audio\r\n
0xb0000084 | [CellularAudio] Unmuting cellular audio\r\n
0xb0000085 | CallManager got disconnect notification for cellvoiceId %1; initiator %2; reason %3; group %4; gppdetails [ location %5 cause %6 ]\r\n
0xb0000086 | CallModel3GPP2 invoking %1; callid %2; asyncRequestId %3\r\n
0xb0000087 | CdmaHeuristics invoking %1; callid %2 and %3; asyncRequestId %3; completionContext %4\r\n
0xb000008b | Call manager got call waiting notification for cellvoice callid %1: rilremotepartyinfo: params %2 numberpres %3 namepres %4\r\n
0xb000008c | Call manager got dial id notification for cellvoice callid %1: params %2 numberpres %3 namepres %4\r\n
0xb000008d | CdmaHeuristics started tracking verb %1 asyncRequestId %2 for completionContext %3\r\n
0xb000008e | CdmaHeuristics stopped tracking verb %1 asyncRequestId %2 for completionContext %3\r\n
0xb000008f | Status %1 from cellcore reading call forwarding status %2 from SIM\r\n
0xb0000090 | Status %1 from cellcore reading call forwarding number from SIM\r\n
0xb0000091 | Status %1 from cellcore writing call forwarding status to SIM\r\n
0xb0000092 | Status %1 from cellcore writing call forwarding number to SIM\r\n
0xb0000093 | Sim LockState changed to: %1\r\n
0xb0000094 | Cellvoice UICC Line set; sim swap pending: %1; old/new line ID: %2 / %3\r\n
0xb0000095 | Finished retrieving home MCC/MNC: %1 %2\r\n
0xb0000096 | Set visual voicemail provisioning state to %1\r\n
0xb0000097 | Forced SIM swap based on MCC/MNC: %1 %2 ==> %3 %4\r\n
0xb0000098 | Modem power state changed to %1\r\n
0xb0000099 | Network codes: params %1; MCC %2; MNC %3\r\n
0xb000009a | SIMOM gave LineFactory a duplicate modem (ignored)\r\n
0xb000009b | SIMOM gave LineFactory an unknown modem to remove (ignored)\r\n
0xb000009c | SIMOM gave LineFactory an unknown modem for adding a slot (ignored)\r\n
0xb000009d | SIMOM gave LoneFactory a duplicate slot (ignored)\r\n
0xb000009e | SIMOM gave LineFactory an unknown modem for removing a slot (ignored)\r\n
0xb000009f | SIMOM gave LineFactory an unknown slot to remove (ignored)\r\n
0xb00000a0 | Line not created: modem index %1 or slot index %2 out of bounds (from ISlot %3)\r\n
0xb00000a1 | CallManager new incoming call from %1\r\n
0xb00000a2 | Call forwarding state updated. SupSvcCode: %1; Enable: %2; new m_callForwardingState: %3\r\n
0xb00000a3 | Read call forwarding state from registry. m_callForwardingState: %1; m_callForwardingAddress: %2\r\n
0xb00000a4 | OnSupServiceCallback. ExecutionResult: %1; SvcCode: %2; DialAction: %3\r\n
0xb00000a5 | Legacy Voicemail message ignored due to config setting\r\n
0xb00000a6 | CdmaHeuristics set local hold to %1\r\n
0xb00000a7 | Detected SGLTE config with no GSM RF; using synthesized no-registration status\r\n
0xb00000a8 | Enqueued verb AcceptIncoming, callid %1, callType %2 (completion context %3)\r\n
0xb00000a9 | Dequeued verb AcceptIncoming, callid %1, callType %2 (completion context %3)\r\n
0xb00000aa | Gsm call manager called I3GPPCallModel::AcceptIncomingCall with async request id %1 for callid %2, callType %3 (cellvoice callid %4)\r\n
0xb00000ab | Received an IMS SIP disconnect cause: error-code=%1, reason=%2\r\n
0xb00000ac | Assumed error is XCAP related and enabling show/hide caller id feature\r\n
0xb00000ca | Terminating Active Call Agent %1 due to timeout waiting for Notify callback\r\n
0xb00000cb | Cell Broadcast Listener received message %1\r\n
0xb00000cc | Display text changed: params %1, info type %2, info tag %3, message size %4\r\n
0xb00000cd | Calling IVoIPTaskManagerClient->LaunchActiveCallAgent(%1)\r\n
0xb00000ce | Calling IVoIPTaskManagerClient->CancelActiveCallAgentInstance(%1)\r\n
0xb00000cf | _CancelActiveCallAgent for product id: %1; isForcedShutdown: %2; isActiveCallAgentRunning: %3\r\n
0xb00000d0 | Calling IVoIPTaskManagerClient->HoldActiveCall(%1)\r\n
0xb00000d1 | Calling IVoIPTaskManagerClient->UnholdActiveCall(%1)\r\n
0xb00000d2 | Calling IVoIPTaskManagerClient->OnIncomingCallDialogDisplayed(%1)\r\n
0xb00000d3 | Calling IVoIPTaskManagerClient->OnIncomingCallDialogDismissed(%1)\r\n
0xb00000d4 | InitializedConnectionToAppHost called on VoipProvider. RPC Handle: %1; VoipLine: %2; AgentProcessId: %3; ContextId: %4\r\n
0xb00000d5 | LineFactory->NewIncomingCall(%1, %2)\r\n
0xb00000d6 | LineFactory->NewOutgoingCall(%1, %2)\r\n
0xb00000d7 | LineFactory->CallActive(%1, %2)\r\n
0xb00000d8 | LineFactory->CallHeld(%1, %2)\r\n
0xb00000d9 | LineFactory->CallEnded(%1, %2)\r\n
0xb00000da | LineFactory->SetAudioRouting(%1, %2)\r\n
0xb00000db | LineFactory->GetAudioRouting(%1)\r\n
0xb00000dc | LineFactory->SetMuteState(%1, %2)\r\n
0xb00000dd | LineFactory->UpdateCallContactName(%1, %2)\r\n
0xb00000de | LineFactory->UpdateCallStartTime(%1, %2)\r\n
0xb00000df | LineFactory->GetCallStartTime(%1, %2)\r\n
0xb00000e0 | LineFactory->UpdateCallAttributes(%1, %2, %3)\r\n
0xb00000e1 | VoipAppHostHandle_rundown(%1)\r\n
0xb00000e2 | _PendingRpcCallCompleted(%2, %3) for line: %1; onTime: %4\r\n
0xb00000e3 | Calling %1 on VoipApp for line: %2. Controller callId: %3; VoipApp CallId: %4\r\n
0xb00000e4 | Calling %1 on VoipApp for line: %2.\r\n
0xb00000e5 | Calling OnAudioRouteChanged on VoipApp for line: %1. AudioRoute: %2; Available Paths: %3\r\n
0xb00000e6 | Can %1 entered emergency mode %2\r\n
0xb00000e7 | Modem constraint violated: Illegal CPI %1\r\n
0xb00000e8 | Modem constraint violated: Async dial failure %1 for call in CPI state %2\r\n
0xb00000e9 | Modem constraint violated: Mismatched direction fields; direction %1, CPI state %2\r\n
0xb00000ea | CallManager invoked I3GPP[2]CallModel::%1; asyncRequestId %2\r\n
0xb00000eb | CallManager invoking I3GPP[2]CallModel::%1; asyncRequestId %2\r\n
0xb00000ec | CallModel3GPP2 invoking %1; callid %2 and %3; asyncRequestId %4)\r\n
0xb00000ed | CdmaHeuristics invoking %1; callid %2; asyncRequestId %3; completionContext %4\r\n
0xb00000ee | CdmaHeuristics verb completed: asyncRequestId %1; result %2; verb %3; callid %4; original completionContext %5\r\n
0xb00000ef | CdmaHeuristics verb completed: asyncRequestId %1; result %2\r\n
0xb00000f0 | CallModel3GPP2 verb completed: asyncRequestId %1; result %2; verb %3; callid %4; original completionContext %5\r\n
0xb00000f1 | Dequeued async CellVoice request id %1 completion with HRESULT %2\r\n
0xb00000f2 | CallModel processing call progress update with cellvoiceId %1 for callId %2\r\n
0xb00000f5 | CdmaHeuristics tracking with asyncRequestId %1 not found\r\n
0xb00000f9 | CallModel3GPP2 got unexpected call update for cellvoiceId %1; while having existing cellvoiceId %2\r\n
0xb00000fd | Processed request to clear Voicemail count.\r\n
0xb00000fe | Default voicemail number source is: %1\r\n
0xb00000ff | Modem constraint violated: Illegal 3GPP2 CallWaiting notification\r\n
0xb0000100 | Tone signal received: params %1, %2, %3, %4\r\n
0xb0000101 | LineNotificationWorkItem: instantiated #%1 (%2)\r\n
0xb0000102 | LineNofiticationWorkItem: processing #%1 (%2)\r\n
0xb0000103 | LineNofiticationWorkItem: finished processing #%1 (%2)\r\n
0xb0000104 | LineNofiticationWorkItem: canceled #%1 (%2)\r\n
0xb0000105 | Got subscriber numbers; dwNumSubscribers = %1\r\n
0xb0000106 | Subscriber number entry #%1: params #2, service #3\r\n
0xb0000107 | Subscriber number is missing or empty\r\n
0xb0000108 | Got IMS status change notification. [Params=%1][AvailableServices=%2]\r\n
0xb0000109 | [CallModel3GPP] Call model changing between GSM and IMS, [ims=%1][m_imsOnWiFi=%2]\r\n
0xb000010a | Roaming override number used.  Dialing %1.\r\n
0xb000010b | HandleUICCPersoCheckStatusChange, [dwParams=%1][dwPersoFeature=%2][dwPersoCheckState=%3]\r\n
0xb000010c | Get Perso deactivation state for %1 completed with hr %2; params %3; state %4; unlock remaining %5; unblock remaining %6\r\n
0xb000010d | Deactivate Perso for %1 completed with hr %2; params %3; state %4; unlock remaining %5; unblock remaining %6; async API context %7\r\n
0xb000010e | Initiating SIM PIN operation %1; async completion context = %2\r\n
0xb000010f | Initiating Perso unlock for %1; async completion context = %2\r\n
0xb0000110 | SIM PIN operation '%1' with async completion context %2 complete, result % = 3\r\n
0xb0000111 | 3GPP2CallModel ignored alien call (CellVoice ID %1) due to existing call (CellVoice ID %2).\r\n
0xb0000112 | 3GPPCallModel suppressed call update due to invalid state.\r\n
0xb0000113 | Unsolicited supservice %1 received for CellVoice callid %2\r\n
0xb0000114 | CellVoice Response Received in Method: %1. Async Hresult: %2\r\n
0xb0000115 | dwParams %1; dwNetworkSSErrorCause %2; dwNetworkCCErrorCause %3; dwVendorErrorCause %4\r\n
0xb0000116 | CellVoice reported infoClasses: %1.\r\n
0xb0000117 | CellVoice reported hide ID settings: params %1, status %2, provisioning %3.\r\n
0xb0000118 | CellVoice reported call forwarding settings: params %1, info class %2, delay time %3, status %4.\r\n
0xb0000119 | CellVoice Ussd Data Status: %1.\r\n
0xb000011a | Ussd Session terminated\r\n
0xb000011b | New Ussd Session initiated\r\n
0xb000011c | Invalid Callforwarding delay time parameter: %1. Using default value instead.\r\n
0xb000011d | Using default value for call forwarding delay time\r\n
0xb000011e | CellVoice reported COLR settings: params %1, status %2, provisioning %3.\r\n
0xb000011f | CellVoice reported CLIP settings: params %1, status %2, provisioning %3.\r\n
0xb0000120 | Executing sup service code %1, action %2\r\n
0xb0000121 | Ussd User response truncated\r\n
0xb0000122 | CellVoice reported COLP settings: params %1, status %2, provisioning %3.\r\n
0xb0000123 | Address for unsolicited supservice %1 is %2\r\n
0xb0000124 | Calling %1 on VoipApp for line: %2. VoipApp CallId: %3\r\n
0xb0000127 | RemoteId Request Complete: CallId: %1 RemoteId Exists: %2\r\n
0xb0000128 | Launching Voip app with URI: %1\r\n
0xb0000129 | LineFactory->NewIncomingUpgradeCall(%1, %2)\r\n
0xb000012a | LineFactory->NewOutgoingUpgradeCall(%1, %2). CallUpgradeGuid: %3\r\n
0xb000012b | LineFactory->CallReady(%1, %2)\r\n
0xb000012c | 3GPPCallModel suppressed call update due to ECall Failover.\r\n
0xb000012d | Dialing an Emergency call. PhoneCallId: %1.\r\n
0xb000012e | 3GPPCallModel got surprise outgoing Emergency call notification. Existing ECallId: %1, IgnoreNotification: %2.\r\n
0xb000012f | Modem Radio Config changed to %1\r\n
0xb0000130 | Setting Can Focus for Can: %1\r\n
0xb0000131 | Set Can Focus result: %1\r\n
0xb0000132 | Disconnecting dialed call with callId: %1 for incoming call.\r\n
0xb0000133 | LineFactory->GetNextOperation(%1)\r\n
0xb0000134 | Terminating Call Query Agent %1 due to timeout waiting for Notify callback\r\n
0xb0000135 | lineFactory->VoipAppOperationComplete(%1). Completed operationId: %2. Succeeded: %3. Call upgrade support: %4\r\n
0xb0000136 | Calling IVoIPTaskManagerClient->LaunchCallQueryAgent(%1)\r\n
0xb0000137 | Calling IVoIPTaskManagerClient->CancelCallQueryAgentInstance(%1)\r\n
0xb0000138 | Received async dial completion. CallId: %1, CellVoice CallId: %2\r\n
0xb0000139 | 3GPP2CallModel ignored disconnected call (CellVoice ID %1) due to existing call (CellVoice ID %2).\r\n
0xb000013a | Detected LTE System Type with no network registration and no voice domain.\r\n
0xb000013b | CallManager invoked I3GPP[2]CallModel::%1; asyncRequestId %2, Dialed Number: %3\r\n
0xb000013c | Update to call type or video context.  CallId: %1, CallType: %2, Video Context: %3\r\n
0xb000013d | CallModel3GPP2 CallVerb_SetVideoPaused; CallId: %1; paused: %2; completion context: %3\r\n
0xb000013e | CallModel3GPP CallVerb_SetVideoPaused; CallId: %1; paused: %2; async id: %3\r\n
0xb000013f | Enqueued verb SetVideoPaused, callid %1, paused %2, (completion context %3)\r\n
0xb0000140 | Dequeued verb SetVideoPaused, callid %1, paused %2, (completion context %3)\r\n
0xb0000141 | Video state update.  Params: %1, Action: %2, Direction: %3, State Params: %4, Peer caps: %5, Flags: %6, ContextID: %7\r\n
0xb0000142 | Calling Cellular API in media update for %1.  Async request id: %2, CallId %3, CellVoice CallId: %4)\r\n
0xb0000143 | Requesting video state publish.  Subscriber Number: %1, videoCapable: %2\r\n
0xb0000144 | Line type changed but SupService was not reset.\r\n
0xb0000145 | Registration state according to voice domain, voice domain: %1, registration status: %2, mapped registration state: %3\r\n
0xb0000146 | SubscriptionUpdate OMADM initiated : %1 HR = %2\r\n
0xb0000147 | Video direction override during multitasking, new transmit state: %1\r\n
0xb0000148 | CellularLine SetVideoCallingSetting: [CurrentState=%1][RequestType=%2][CacheSetting=%3][PerSimConfigAvailable=%4][TargetState=%5]\r\n
0xb0000149 | IMS system-type changing from %1 to %2\r\n
0xb000014a | Video media offer answer. Params: %1, Action: %2, Direction: %3, State Params: %4, Peer caps: %5, Flags: %6, ContextID: %7\r\n
0xb000014b | LineFactory->EndUpgradeOriginationCall(%1)\r\n
0xb000014c | LineFactory->CancelUpgrade(%1)\r\n
0xb000014d | ImsHandoverAttempt notify arrives. hrHandOverResult: %1, OldSystemType: %2, NewSystemType: %3\r\n
0xb000014e | GetVideoCapabilitySharingSettings: Queried, [LineId=%1][PerSimConfigAvaiable=%2][IsCapabilitySharingEnabled=%3][LastModifiedTimestamp=%4]\r\n
0xb000014f | SetVideoCapabilitySharingSettings: Updating, [LineId=%1][PerSimConfigAvaiable=%2][IsCapabilitySharingEnabled=%3][CurrentTimestamp=%4]\r\n
0xb0000150 | Applying video calling setting to saved or default user preference.\r\n
0xb0000151 | Unable to determine cached video calling setting.\r\n
0xb0000152 | Updated home MCC value from SIM in line specific data, [LineId=%1][HomeMcc=%2].\r\n
0xb0000153 | CallRecording: Phone service was notified of a Call Recording application whose Package Family Name is too long: '%1'\r\n
0xb0000155 | IMS service voice changed, [imsVoiceAvailable=%1][imsVideoAvailable=%2][videoCallingEnabled=%3]\r\n
0xb0000156 | IMS service video changed, [imsVoiceAvailable=%1][imsVideoAvailable=%2][videoCallingEnabled=%3]\r\n
0xb0000157 | DeterminePhoneSystemType, [imsVoiceSupported=%1][registration0SystemType=%2][registration0VoiceDomain=%3][callPresence=%4]\r\n
0xb0000158 | UpdateLineSystemType, [currentLineSystemType=%1][newLineSystemType=%2]\r\n
0xb0000159 | SetRadioAccessTechnology, [radioAccessTechnology=%1][toIms=%2][toGsm=%3][toCdma=%4][fromIms=%5][fromGsm=%6][fromCdma=%7]\r\n
0xb000015a | SetRadioAccessTechnology, switching call model, [To3GPP=%1]\r\n
0xb000015b | UpdateCallPresence, [currentPresence=%1][aggregatePresence=%2][allSameType=%3]\r\n
0xb000015c | [CallModel3GPP] Updating audio, [audioType=%1][audioActive=%2][anyCallNeedsAudio=%3][anyCallNeedsAudioActive=%4][localHoldSupported=%5]\r\n
0xb000015d | [CallModel3GPP2] Updating audio, [audioType=%1][shouldEnableAudio=%2][audioAllowed=%3]\r\n
0xb000015e | [CellularAudio] Updating audio for handover notification, [inProgress=%1][isHandoverNotification=%2][phase=%3][oldType=%4][newType=%5]\r\n
0xb000015f | ProcessHandoverNotification, [callInfoParams=%1][phase=%2][handoverStateParams=%3][oldType=%4][newType=%5][inProgress=%6]\r\n
0xb0000160 | Reset handover state\r\n
0xb0000161 | Updated video call conference state, [CallId=%1][CellVoiceCallId=%2][ContextId=%3][ConferenceContextId=%4][PreviousState=%5][UpdatedState=%6].\r\n
0xb0000162 | Interpret E_SUPSVCS_INVALIDREMOTEURI as success with call forwarding status disabled.\r\n
0xb0000163 | IR94FeatureDisabled: Disable video calling.\r\n
0xb0000164 | IR94FeatureDisabled: Force disable video calling.\r\n
0xb0000165 | Emergency call failed over. ECallId: %1.\r\n
0xb0000166 | Emergency call DisableAndEnable Audio from 3GPP CallModel. ECallId: %1.\r\n
0xb0000167 | Emergency call DisableAndEnable Audio from 3GPP2 CallModel. ECallId: %1.\r\n
0xb0000168 | HandleUICCPinLockStateChange, [dwParams=%1][dwLockState=%2]\r\n
0xb0000169 | Updating UICC related information from SIM\r\n
0xb000016a | OnSubscriberNumbersChange, [result=%1]\r\n
0xb000016b | [CallModel3GPP] Notified for IMS on Wifi flag, [m_imsOnWiFi=%1][onWiFi=%2]\r\n
0xd0000001 | CallType_AudioOnly\r\n
0xd0000002 | CallType_AudioVideo\r\n
0xd0000003 | CallerIdOption_Default\r\n
0xd0000004 | CallerIdOption_ForceSend\r\n
0xd0000005 | CallerIdOption_ForceBlock\r\n
0xd0000006 | PH_CALLDIRECTION_INCOMING\r\n
0xd0000007 | PH_CALLDIRECTION_OUTGOING\r\n
0xd0000008 | PH_REGISTRATIONSTATE_UNKNOWN\r\n
0xd0000009 | PH_REGISTRATIONSTATE_UNREGISTERED_NO_SIGNAL\r\n
0xd000000a | PH_REGISTRATIONSTATE_UNREGISTERED_WITH_SIGNAL\r\n
0xd000000b | PH_REGISTRATIONSTATE_REGISTERING\r\n
0xd000000c | PH_REGISTRATIONSTATE_REGISTERING_AFTER_DENIED\r\n
0xd000000d | PH_REGISTRATIONSTATE_REGISTERED_HOME\r\n
0xd000000e | PH_REGISTRATIONSTATE_REGISTERED_ROAM\r\n
0xd000000f | PH_REGISTRATIONSTATE_DENIED\r\n
0xd0000010 | PH_REGISTRATIONSTATE_REGISTERED_ROAM_DOMESTIC\r\n
0xd0000011 | RIL_VOICE_DOMAIN_NONE\r\n
0xd0000012 | RIL_VOICE_DOMAIN_3GPP\r\n
0xd0000013 | RIL_VOICE_DOMAIN_3GPP2\r\n
0xd0000014 | RIL_VOICE_DOMAIN_IMS\r\n
0xd0000015 | RIL_CALLDIR_INCOMING\r\n
0xd0000016 | RIL_CALLDIR_OUTGOING\r\n
0xd0000017 | RIL_CPISTAT_UNKNOWN\r\n
0xd0000018 | RIL_CPISTAT_NEW_OUTGOING\r\n
0xd0000019 | RIL_CPISTAT_NEW_INCOMING\r\n
0xd000001a | RIL_CPISTAT_CONNECTED\r\n
0xd000001b | RIL_CPISTAT_DISCONNECTED\r\n
0xd000001c | RIL_CPISTAT_ONHOLD\r\n
0xd000001d | RIL_CPISTAT_MEDIA\r\n
0xd000001e | RIL_CPISTAT_HANDOVER\r\n
0xd000001f | RIL_CALL_SINGLEPARTY\r\n
0xd0000020 | RIL_CALL_MULTIPARTY\r\n
0xd0000021 | RIL_REMOTEPARTYINFO_VALID\r\n
0xd0000022 | RIL_REMOTEPARTYINFO_WITHHELD\r\n
0xd0000023 | RIL_REMOTEPARTYINFO_UNAVAILABLE\r\n
0xd0000024 | RIL_DISCINIT_UNKNOWN\r\n
0xd0000025 | RIL_DISCINIT_LOCAL\r\n
0xd0000026 | RIL_DISCINIT_REMOTE\r\n
0xd0000027 | RIL_DISCREASON_NULL\r\n
0xd0000028 | RIL_DISCREASON_BUSY\r\n
0xd0000029 | RIL_DISCREASON_NETWORKERROR\r\n
0xd000002a | RIL_DISCREASON_RADIOFADE\r\n
0xd000002b | RIL_DISCREASON_CONGESTION\r\n
0xd000002c | RIL_DISCREASON_EMERGENCYONLY\r\n
0xd000002d | RIL_DISCREASON_NOSERVICE\r\n
0xd000002e | RIL_DISCREASON_OTHEREXECUTORBUSY\r\n
0xd000002f | RIL_DISCREASON_EMERGENCYFAILOVER\r\n
0xd0000030 | RIL_DISCREASON_HANDOVER_MERGE\r\n
0xd0000031 | RIL_CALLTYPE_VOICE\r\n
0xd0000032 | RIL_CALLTYPE_DATA\r\n
0xd0000033 | RIL_CALLTYPE_FAX\r\n
0xd0000034 | RIL_CALLTYPE_PTT\r\n
0xd0000035 | RIL_CALLTYPE_VT\r\n
0xd0000036 | RIL_CALLTYPE_USSD\r\n
0xd0000037 | RIL_CALLTYPE_SUPSVC\r\n
0xd0000038 | RIL_CALLTYPE_IMS\r\n
0xd0000039 | RIL_CD_UNKNOWN_CAUSE\r\n
0xd000003a | RIL_CD_AS_CAUSE\r\n
0xd000003b | RIL_CD_3GPP_NETWORK_CAUSE\r\n
0xd000003c | RIL_CD_3GPP2_VENDOR_CAUSE\r\n
0xd000003d | RIL_CD_OTHER_CAUSE\r\n
0xd000003e | RIL_CD_3GPP_REJECT_CAUSE\r\n
0xd000003f | RIL_CD_IMS_SIP_CAUSE\r\n
0xd0000040 | RIL_EXTENDED_DISPLAY_TYPE_NORMAL\r\n
0xd0000041 | RIL_EXTENDED_DISPLAY_TAG_BLANK\r\n
0xd0000042 | RIL_EXTENDED_DISPLAY_TAG_SKIP\r\n
0xd0000043 | RIL_EXTENDED_DISPLAY_TAG_CONTINUATION\r\n
0xd0000044 | RIL_EXTENDED_DISPLAY_TAG_CALLED_ADDRESS\r\n
0xd0000045 | RIL_EXTENDED_DISPLAY_TAG_CAUSE\r\n
0xd0000046 | RIL_EXTENDED_DISPLAY_TAG_PROGRESS_INDICATOR\r\n
0xd0000047 | RIL_EXTENDED_DISPLAY_TAG_NOTIFICATION_INDICATOR\r\n
0xd0000048 | RIL_EXTENDED_DISPLAY_TAG_PROMPT\r\n
0xd0000049 | RIL_EXTENDED_DISPLAY_TAG_ACCUMULATED_DIGITS\r\n
0xd000004a | RIL_EXTENDED_DISPLAY_TAG_STATUS\r\n
0xd000004b | RIL_EXTENDED_DISPLAY_TAG_INBAND\r\n
0xd000004c | RIL_EXTENDED_DISPLAY_TAG_CALLING_ADDRESS\r\n
0xd000004d | RIL_EXTENDED_DISPLAY_TAG_REASON\r\n
0xd000004e | RIL_EXTENDED_DISPLAY_TAG_CALLING_PARTY_NAME\r\n
0xd000004f | RIL_EXTENDED_DISPLAY_TAG_CALLED_PARTY_NAME\r\n
0xd0000050 | RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NAME\r\n
0xd0000051 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NAME\r\n
0xd0000052 | RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NAME\r\n
0xd0000053 | RIL_EXTENDED_DISPLAY_TAG_ORIGINATING_RESTRICT\r\n
0xd0000054 | RIL_EXTENDED_DISPLAY_TAG_DATE_TIME_OF_DAY\r\n
0xd0000055 | RIL_EXTENDED_DISPLAY_TAG_CALL_APPEARANCE_ID\r\n
0xd0000056 | RIL_EXTENDED_DISPLAY_TAG_FEATURE_ADDRESS\r\n
0xd0000057 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NAME\r\n
0xd0000058 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NUMBER\r\n
0xd0000059 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NUMBER\r\n
0xd000005a | RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NUMBER\r\n
0xd000005b | RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NUMBER\r\n
0xd000005c | RIL_EXTENDED_DISPLAY_TAG_TEXT\r\n
0xd000005d | RIL_REGSTAT_UNKNOWN\r\n
0xd000005e | RIL_REGSTAT_UNREGISTERED\r\n
0xd000005f | RIL_REGSTAT_HOME\r\n
0xd0000060 | RIL_REGSTAT_ATTEMPTING\r\n
0xd0000061 | RIL_REGSTAT_DENIED\r\n
0xd0000062 | RIL_REGSTAT_ROAMING\r\n
0xd0000063 | RIL_REGSTAT_ROAMING_DOMESTIC\r\n
0xd0000064 | MODEM_POWER_OFF\r\n
0xd0000065 | MODEM_POWER_GOING_ON\r\n
0xd0000066 | MODEM_POWER_ON\r\n
0xd0000067 | MODEM_POWER_GOING_OFF\r\n
0xd0000068 | MODEM_POWER_SHUTTING_DOWN\r\n
0xd0000069 | RADIO_CONFIG_SINGLE\r\n
0xd000006a | RADIO_CONFIG_MULTI_MODE\r\n
0xd000006b | RADIO_CONFIG_1XCSFB\r\n
0xd000006c | RADIO_CONFIG_SVLTE\r\n
0xd000006d | RADIO_CONFIG_DualStandby\r\n
0xd000006e | RADIO_CONFIG_DualActive\r\n
0xd000006f | RADIO_CONFIG_SGLTE\r\n
0xd0000070 | RADIO_CONFIG_SVLTE_DUALACTIVE\r\n
0xd0000071 | RADIO_CONFIG_SGLTE_DUALACTIVE\r\n
0xd0000072 | RADIO_CONFIG_SRLTE\r\n
0xd0000073 | VoipIpcAudioRoute_Default\r\n
0xd0000074 | VoipIpcAudioRoute_Earpiece\r\n
0xd0000075 | VoipIpcAudioRoute_Speakerphone\r\n
0xd0000076 | VoipIpcAudioRoute_Bluetooth\r\n
0xd0000077 | RpcCallType_SetInitialAppState\r\n
0xd0000078 | RpcCallType_AcceptIncoming\r\n
0xd0000079 | RpcCallType_CallActive\r\n
0xd000007a | RpcCallType_End\r\n
0xd000007b | RpcCallType_Hold\r\n
0xd000007c | RpcCallType_RejectIncoming\r\n
0xd000007d | RpcCallType_Unhold\r\n
0xd000007e | RpcCallType_Mute\r\n
0xd000007f | RpcCallType_Unmute\r\n
0xd0000080 | RpcCallType_ForceEnd\r\n
0xd0000081 | PH_VOICEMAILPROVISIONINGSTATE_LEGACY_ONLY\r\n
0xd0000082 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_SUPPORTED\r\n
0xd0000083 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_CONFIGURED\r\n
0xd0000084 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_ENABLED\r\n
0xd0000085 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_ENABLED_NEW_USER\r\n
0xd0000086 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_NOT_FUNCTIONING\r\n
0xd0000087 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_CREATED\r\n
0xd0000088 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_PASSWORD_RESET\r\n
0xd0000089 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_INITIALIZED\r\n
0xd000008a | RIL_3GPPTONE_TONEOFF\r\n
0xd000008b | RIL_3GPPTONE_RINGBACK\r\n
0xd000008c | RIL_3GPPTONE_BUSY\r\n
0xd000008d | RIL_3GPPTONE_CONGESTION\r\n
0xd000008e | RIL_3GPPTONE_AUTHENTICATIONFAILURE\r\n
0xd000008f | RIL_3GPPTONE_NUMBERUNOBTAINABLE\r\n
0xd0000090 | RIL_3GPPTONE_CALLDROPPED\r\n
0xd0000091 | RIL_3GPP2TONE_TONEOFF\r\n
0xd0000092 | RIL_3GPP2TONE_DIAL\r\n
0xd0000093 | RIL_3GPP2TONE_RINGBACK\r\n
0xd0000094 | RIL_3GPP2TONE_INTERCEPT\r\n
0xd0000095 | RIL_3GPP2TONE_ABRVINTERCEPT\r\n
0xd0000096 | RIL_3GPP2TONE_REORDER\r\n
0xd0000097 | RIL_3GPP2TONE_ABRVREORDER\r\n
0xd0000098 | RIL_3GPP2TONE_BUSY\r\n
0xd0000099 | RIL_3GPP2TONE_CONFIRM\r\n
0xd000009a | RIL_3GPP2TONE_ANSWER\r\n
0xd000009b | RIL_3GPP2TONE_CALLWAITING\r\n
0xd000009c | RIL_3GPP2TONE_PIP\r\n
0xd000009d | RIL_3GPP2ISDNALERTING_ALERTINGOFF\r\n
0xd000009e | RIL_3GPP2ISDNALERTING_NORMAL\r\n
0xd000009f | RIL_3GPP2ISDNALERTING_INTERGROUP\r\n
0xd00000a0 | RIL_3GPP2ISDNALERTING_SPECIAL\r\n
0xd00000a1 | RIL_3GPP2ISDNALERTING_PINGRING\r\n
0xd00000a2 | RIL_PERSOCHECKSTATE_NOTREADY\r\n
0xd00000a3 | RIL_PERSOCHECKSTATE_PASS\r\n
0xd00000a4 | RIL_PERSOCHECKSTATE_FAIL\r\n
0xd00000a5 | RIL_DEPERSOSTATE_READY\r\n
0xd00000a6 | RIL_DEPERSOSTATE_CK_REQUIRED\r\n
0xd00000a7 | RIL_DEPERSOSTATE_PUK_REQUIRED\r\n
0xd00000a8 | RIL_DEPERSOSTATE_PUK_BLOCKED\r\n
0xd00000a9 | No voicemail number found\r\n
0xd00000aa | SIM override key\r\n
0xd00000ab | SIM data\r\n
0xd00000ac | Default number cached in registry\r\n
0xd00000ad | SIM fallback key\r\n
0xd00000ae | Kind_None\r\n
0xd00000af | Kind_EmergencyModeChange\r\n
0xd00000b0 | Kind_ExitEmergencyModeFinished\r\n
0xd00000b1 | Kind_NetworkRegistrationChange\r\n
0xd00000b2 | Kind_SignalStrengthChange\r\n
0xd00000b3 | Kind_ModemPowerStateChange\r\n
0xd00000b4 | Kind_SubscriberNumberChange\r\n
0xd00000b5 | Kind_RegistryConfigChange\r\n
0xd00000b6 | Kind_VoicemailNumberChangeRequest\r\n
0xd00000b7 | Kind_VoicemailNumberSimSetCompleted\r\n
0xd00000b8 | Kind_VoicemailNumberSimGetCompleted\r\n
0xd00000b9 | Kind_Imsi\r\n
0xd00000ba | Kind_SupServiceCallback\r\n
0xd00000bb | Kind_PinLockState\r\n
0xd00000bc | Kind_SlotState\r\n
0xd00000bd | Kind_SetCallerId\r\n
0xd00000be | Kind_ToneNotification\r\n
0xd00000bf | Kind_CellBroadcastMessage\r\n
0xd00000c0 | Kind_GetLineCallForwardingStatusCompletion\r\n
0xd00000c1 | Kind_SetLineCallForwardingStatusCompletion\r\n
0xd00000c2 | Kind_GetLineCallForwardingNumberCompletion\r\n
0xd00000c3 | Kind_ServiceProviderNameChange\r\n
0xd00000c4 | Kind_PersoCheckStatus\r\n
0xd00000c5 | Kind_PersoDeactivationState\r\n
0xd00000c6 | Kind_MuteStateChange\r\n
0xd00000c7 | Kind_SlotCanAssociationsChanged\r\n
0xd00000c8 | Kind_CallPresenceChanged\r\n
0xd00000c9 | Kind_ImsStatusChanged\r\n
0xd00000ca | Kind_ImsSystemTypeChanged\r\n
0xd00000cb | Kind_RefreshVideoCallingSetting\r\n
0xd00000cc | Kind_SetVideoCallingSetting\r\n
0xd00000cd | Kind_SetVideoCallingSettingComplete\r\n
0xd00000ce | Kind_GetVideoCallingSettingComplete\r\n
0xd00000cf | Kind_GetPSMediaPreferencesComplete\r\n
0xd00000d0 | RIL_SERVICE_UNKNOWN\r\n
0xd00000d1 | RIL_SERVICE_VOICE\r\n
0xd00000d2 | RIL_SERVICE_FAX\r\n
0xd00000d3 | RIL_SERVICE_OTHER\r\n
0xd00000d4 | FWDCODE_UNCONDITIONAL\r\n
0xd00000d5 | FWDCODE_BUSY\r\n
0xd00000d6 | FWDCODE_NOREPLY\r\n
0xd00000d7 | FWDCODE_NOTREACHABLE\r\n
0xd00000d8 | FWDCODE_ALL\r\n
0xd00000d9 | FWDCODE_ALLCONDITIONAL\r\n
0xd00000da | FWDCODE_STATECHANGED\r\n
0xd00000db | SimPinOperation_None\r\n
0xd00000dc | SimPinOperation_EnableSimPin\r\n
0xd00000dd | SimPinOperation_DisableSimPin\r\n
0xd00000de | SimPinOperation_ChangeSimPin\r\n
0xd00000df | SimPinOperation_UnlockSim\r\n
0xd00000e0 | SimPinOperation_UnblockSim\r\n
0xd00000e1 | PersoFeature_Unknown\r\n
0xd00000e2 | PersoFeature_None\r\n
0xd00000e3 | PersoFeature_3Gpp_Net\r\n
0xd00000e4 | PersoFeature_3Gpp_NetSub\r\n
0xd00000e5 | PersoFeature_3Gpp_Sp\r\n
0xd00000e6 | PersoFeature_3Gpp_Corp\r\n
0xd00000e7 | PersoFeature_3Gpp_USim\r\n
0xd00000e8 | PersoFeature_3Gpp2_NetType1\r\n
0xd00000e9 | PersoFeature_3Gpp2_NetType2\r\n
0xd00000ea | PersoFeature_3Gpp2_Hrpd\r\n
0xd00000eb | PersoFeature_3Gpp2_Sp\r\n
0xd00000ec | PersoFeature_3Gpp2_Corp\r\n
0xd00000ed | PersoFeature_3Gpp2_Uim\r\n
0xd00000ee | DialAction_None\r\n
0xd00000ef | DialAction_Activation\r\n
0xd00000f0 | DialAction_Deactivation\r\n
0xd00000f1 | DialAction_Interrogation\r\n
0xd00000f2 | DialAction_Registration\r\n
0xd00000f3 | DialAction_Erasure\r\n
0xd00000f4 | RIL_UNSSSCODE_FORWARDEDCALL\r\n
0xd00000f5 | RIL_UNSSSCODE_CUGCALL\r\n
0xd00000f6 | RIL_UNSSSCODE_CALLPUTONHOLD\r\n
0xd00000f7 | RIL_UNSSSCODE_CALLRETRIEVED\r\n
0xd00000f8 | RIL_UNSSSCODE_ENTEREDMULTIPARTY\r\n
0xd00000f9 | RIL_UNSSSCODE_HELDCALLRELEASED\r\n
0xd00000fa | RIL_UNSSSCODE_FORWARDCHECKSS\r\n
0xd00000fb | RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER\r\n
0xd00000fc | RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER\r\n
0xd00000fd | RIL_UNSSSCODE_DEFLECTEDCALL\r\n
0xd00000fe | RIL_UNSSSCODE_ADDITIONALINCOMINGCF\r\n
0xd00000ff | RIL_UNSSSCODE_UNCONDITIONALCFACTIVE\r\n
0xd0000100 | RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE\r\n
0xd0000101 | RIL_UNSSSCODE_CALLWASFORWARDED\r\n
0xd0000102 | RIL_UNSSSCODE_CALLISWAITING\r\n
0xd0000103 | RIL_UNSSSCODE_OUTGOINGCALLSBARRED\r\n
0xd0000104 | RIL_UNSSSCODE_INCOMINGCALLSBARRED\r\n
0xd0000105 | RIL_UNSSSCODE_CLIRSUPPRESSREJECT\r\n
0xd0000106 | RIL_IMSSYSTEMTYPE_UNKNOWN\r\n
0xd0000107 | RIL_IMSSYSTEMTYPE_WIFI\r\n
0xd0000108 | RIL_IMSSYSTEMTYPE_LTE\r\n
0xd0000109 | CallUpgradeSupportLevel_NotSupported\r\n
0xd000010a | CallUpgradeSupportLevel_NonSeamless\r\n
0xd000010b | CallUpgradeSupportLevel_Seamless\r\n
0xd000010c | CallUpgradeSupportLevel_AppDetermined\r\n
0xd000010d | VideoCallingSetting_Disabled\r\n
0xd000010e | VideoCallingSetting_Enabled\r\n
0xd000010f | VideoCallingSetting_CachedValue\r\n
0xd0000110 | RIL_CALLMEDIADIRECTION_NONE\r\n
0xd0000111 | RIL_CALLMEDIADIRECTION_RX\r\n
0xd0000112 | RIL_CALLMEDIADIRECTION_TX\r\n
0xd0000113 | RIL_CALLMEDIADIRECTION_RXTX\r\n
0xd0000114 | RIL_CALLMEDIAOFFERACTION_NONE\r\n
0xd0000115 | RIL_CALLMEDIAOFFERACTION_ERROR\r\n
0xd0000116 | RIL_CALLMEDIAOFFERACTION_REJECT\r\n
0xd0000117 | RIL_CALLMEDIAOFFERACTION_ASK\r\n
0xd0000118 | RIL_CALLMEDIAOFFERACTION_ACCEPT\r\n
0xd0000119 | RIL_CALLMEDIAOFFERACTION_CANCEL\r\n
0xd000011a | None\r\n
0xd000011b | CircuitSwitched\r\n
0xd000011c | PacketSwitched\r\n
0xd000011d | PH_LINESYSTEMTYPE_GSM\r\n
0xd000011e | PH_LINESYSTEMTYPE_CDMA\r\n
0xd000011f | PH_LINESYSTEMTYPE_VOIP\r\n
0xd0000120 | PH_LINESYSTEMTYPE_UNKNOWN\r\n
0xd0000121 | PH_LINESYSTEMTYPE_IMS\r\n
0xd0000122 | CellularAudioType_None\r\n
0xd0000123 | CellularAudioType_CircuitSwitched\r\n
0xd0000124 | CellularAudioType_PacketSwitched\r\n
0xd0000125 | CellularAudioType_PacketSwitched_WiFi\r\n
0xd0000126 | RIL_CALLHANDOVERPHASE_STARTED\r\n
0xd0000127 | RIL_CALLHANDOVERPHASE_COMPLETED\r\n
0xd0000128 | RIL_CALLHANDOVERPHASE_FAILED\r\n
0xd0000129 | RIL_CALLHANDOVERPHASE_CANCELLED\r\n
0xd000012a | None\r\n
0xd000012b | Pending\r\n
0xd000012c | Connected\r\n
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
0xf000001a | Dial\r\n
0xf000001b | End\r\n
0xf000001c | DropActiveAcceptHeld\r\n
0xf000001d | Hold\r\n
0xf000001e | Unhold\r\n
0xf000001f | Swap\r\n
0xf0000020 | Private\r\n
0xf0000021 | Conference\r\n
0xf0000022 | Flash\r\n
0xf0000023 | RejectIncoming\r\n
0xf0000024 | AcceptIncoming\r\n
0xf0000025 | SendDtmf\r\n
0xf0000026 | StartDtmf\r\n
0xf0000027 | StopDtmf\r\n
0xf0000028 | DropFromConference\r\n
0xf0000029 | DisableLocalVideo\r\n
0xf000002a | EnableLocalVideo\r\n
0xf000002b | AddVideo\r\n
0xf000002c | DropVideo\r\n
0xf000002d | AcceptIncomingVideo\r\n
0xf000002e | RejectIncomingVideo\r\n
0xf000002f | SetVideoPaused\r\n
0xf0000030 | StartRecording\r\n
0xf0000031 | PauseRecording\r\n
0xf0000032 | StopRecording\r\n
0xf0000033 | RIL_PARAM_CI_EXECUTOR\r\n
0xf0000034 | RIL_PARAM_CI_ID\r\n
0xf0000035 | RIL_PARAM_CI_DIRECTION\r\n
0xf0000036 | RIL_PARAM_CI_STATUS\r\n
0xf0000037 | RIL_PARAM_CI_TYPE\r\n
0xf0000038 | RIL_PARAM_CI_MULTIPARTY\r\n
0xf0000039 | RIL_PARAM_CI_ADDRESS\r\n
0xf000003a | RIL_PARAM_CI_SUBADDRESS\r\n
0xf000003b | RIL_PARAM_CI_DESCRIPTION\r\n
0xf000003c | RIL_PARAM_CI_NUM_PRES_IND\r\n
0xf000003d | RIL_PARAM_CI_NAME_PRES_IND\r\n
0xf000003e | RIL_PARAM_CI_FLAGS\r\n
0xf000003f | RIL_PARAM_CI_DISCONNECTINITIATOR\r\n
0xf0000040 | RIL_PARAM_CI_DISCONNECTREASON\r\n
0xf0000041 | RIL_PARAM_CI_DISCONNECTDETAILS\r\n
0xf0000042 | RIL_PARAM_CI_OFFERANSWER\r\n
0xf0000043 | RIL_PARAM_CI_HANDOVERSTATE\r\n
0xf0000044 | RIL_PARAM_RPI_EXECUTOR\r\n
0xf0000045 | RIL_PARAM_RPI_ADDRESS\r\n
0xf0000046 | RIL_PARAM_RPI_SUBADDRESS\r\n
0xf0000047 | RIL_PARAM_RPI_DESCRIPTION\r\n
0xf0000048 | RIL_PARAM_RPI_NUM_PRES_IND\r\n
0xf0000049 | RIL_PARAM_RPI_NAME_PRES_IND\r\n
0xf000004a | RIL_PARAM_RPI_ID\r\n
0xf000004b | RIL_PARAM_ON_LONGNAME\r\n
0xf000004c | RIL_PARAM_ON_SHORTNAME\r\n
0xf000004d | RIL_PARAM_ON_NUMNAME\r\n
0xf000004e | RIL_PARAM_ON_COUNTRY_CODE\r\n
0xf000004f | RIL_PARAM_ON_SYSTEMTYPE\r\n
0xf0000050 | RIL_PARAM_NETWORKCODE_EXECUTOR\r\n
0xf0000051 | RIL_PARAM_NETWORKCODE_MCC\r\n
0xf0000052 | RIL_PARAM_NETWORKCODE_MNC\r\n
0xf0000053 | RIL_PARAM_NETWORKCODE_SID\r\n
0xf0000054 | RIL_PARAM_NETWORKCODE_NID\r\n
0xf0000055 | RIL_PARAM_NETWORKCODE_RI\r\n
0xf0000056 | RILCALLINFO_FLAG_ALIENCALL\r\n
0xf0000057 | RILCALLINFO_FLAG_EMERGENCYCALL\r\n
0xf0000058 | RIL_PARAM_DISPLAY_EXECUTOR\r\n
0xf0000059 | RIL_PARAM_DISPLAY_TYPE\r\n
0xf000005a | RIL_PARAM_DISPLAY_TAG\r\n
0xf000005b | RIL_PARAM_DISPLAY_MESSAGESIZE\r\n
0xf000005c | RIL_PARAM_DISPLAY_MESSAGE\r\n
0xf000005d | RIL_SYSTEMTYPE_1XRTT\r\n
0xf000005e | RIL_SYSTEMTYPE_EVDO\r\n
0xf000005f | RIL_SYSTEMTYPE_GSM\r\n
0xf0000060 | RIL_SYSTEMTYPE_UMTS\r\n
0xf0000061 | RIL_SYSTEMTYPE_LTE\r\n
0xf0000062 | RIL_SYSTEMTYPE_TDSCDMA\r\n
0xf0000063 | VoipIpcCallAttributes_VoiceOnly\r\n
0xf0000064 | VoipIpcCallAttributes_Video\r\n
0xf0000065 | RIL_PARAM_TONESIGNAL_GPPTONE\r\n
0xf0000066 | RIL_PARAM_TONESIGNAL_GPPTONE2\r\n
0xf0000067 | RIL_PARAM_TONESIGNAL_GPP2ISDNALERTING\r\n
0xf0000068 | RIL_PARAM_TONESIGNAL_EXECUTOR\r\n
0xf0000069 | RIL_PERSOFEATURE_3GPP_NET\r\n
0xf000006a | RIL_PERSOFEATURE_3GPP_NETSUB\r\n
0xf000006b | RIL_PERSOFEATURE_3GPP_SP\r\n
0xf000006c | RIL_PERSOFEATURE_3GPP_CORP\r\n
0xf000006d | RIL_PERSOFEATURE_3GPP_USIM\r\n
0xf000006e | RIL_PERSOFEATURE_3GPP2_NETTYPE1\r\n
0xf000006f | RIL_PERSOFEATURE_3GPP2_NETTYPE2\r\n
0xf0000070 | RIL_PERSOFEATURE_3GPP2_HRPD\r\n
0xf0000071 | RIL_PERSOFEATURE_3GPP2_SP\r\n
0xf0000072 | RIL_PERSOFEATURE_3GPP2_CORP\r\n
0xf0000073 | RIL_PERSOFEATURE_3GPP2_UIM\r\n
0xf0000074 | RIL_PARAM_PDS_STATE\r\n
0xf0000075 | RIL_PARAM_PDS_CK_ATTEMPTS\r\n
0xf0000076 | RIL_PARAM_PDS_PUK_ATTEMPTS\r\n
0xf0000077 | RIL_PARAM_SI_ADDRESS\r\n
0xf0000078 | RIL_PARAM_SI_DESCRIPTION\r\n
0xf0000079 | RIL_PARAM_SI_SERVICE\r\n
0xf000007a | RIL_PARAM_IMSSTATUS_EXECUTOR\r\n
0xf000007b | RIL_PARAM_IMSSTATUS_HUICCAPP\r\n
0xf000007c | RIL_PARAM_IMSSTATUS_AVAILABLESERVICES\r\n
0xf000007d | RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT\r\n
0xf000007e | RIL_PARAM_IMSSTATUS_SERVINGDOMAIN\r\n
0xf000007f | RIL_PARAM_IMSSTATUS_SYSTEMTYPE\r\n
0xf0000080 | RIL_IMS_SERVICE_SMS\r\n
0xf0000081 | RIL_IMS_SERVICE_VOICE\r\n
0xf0000082 | RIL_IMS_SERVICE_VIDEO\r\n
0xf0000083 | RIL_IMS_SERVICE_CUSTOM\r\n
0xf0000084 | RIL_IMS_SERVICE_SUPSVC\r\n
0xf0000085 | RIL_IMS_SERVICE_RCS\r\n
0xf0000086 | RIL_IMS_SERVICE_USSD\r\n
0xf0000087 | RIL_IMS_SERVICE_E_VOICE\r\n
0xf0000088 | RIL_PARAM_CMOA_ID\r\n
0xf0000089 | RIL_PARAM_CMOA_CHANGE\r\n
0xf000008a | RIL_PARAM_CMOA_ACTION\r\n
0xf000008b | RIL_PARAM_CMOA_OLD_STATE\r\n
0xf000008c | RIL_PARAM_CMOA_NEW_STATE\r\n
0xf000008d | RIL_PARAM_CALLVIDEO_PEERCAPABILITIES\r\n
0xf000008e | RIL_PARAM_CALLVIDEO_FLAGS\r\n
0xf000008f | RIL_CALLMEDIAVIDEOFLAG_CAPABILITY_UNKNOWN\r\n
0xf0000090 | RIL_CALLMEDIAVIDEOFLAG_PAUSE\r\n
0xf0000091 | RIL_PARAM_HANDOVER_PHASE\r\n
0xf0000092 | RIL_PARAM_HANDOVER_OLD_TYPE\r\n
0xf0000093 | RIL_PARAM_HANDOVER_NEW_TYPE\r\n
0xf0000094 | RIL_PARAM_HANDOVER_3GPPCAUSE\r\n
0xf0000095 | RIL_UICCLOCKSTATE_VERIFIED\r\n
0xf0000096 | RIL_UICCLOCKSTATE_ENABLED\r\n
0xf0000097 | RIL_UICCLOCKSTATE_BLOCKED\r\n
0xf0000098 | RIL_PARAM_UICCLOCKSTATE_UICCLOCK\r\n
0xf0000099 | RIL_PARAM_UICCLOCKSTATE_LOCKSTATE\r\n
0xf000009a | RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT\r\n
0xf000009b | RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT\r\n
0xf000009c | RIL_PARAM_UAPCS_HUICCAPP\r\n
0xf000009d | RIL_PARAM_UAPCS_PERSOFEATURE\r\n
0xf000009e | RIL_PARAM_UAPCS_PERSOCHECKSTATE\r\n

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
0xb0000064 | Enqueued verb %1, callid %2 (completion context %3)\r\n
0xb0000065 | Enqueued verb %1, callids %2, %3 (completion context %4)\r\n
0xb0000066 | Enqueued verb Dial, callid %1, callType %2, calleridoption %3 (completion context %4)\r\n
0xb0000067 | Dequeued verb %1, callid %2 (completion context %3)\r\n
0xb0000068 | Dequeued verb %1, callids %2, %3 (completion context %4)\r\n
0xb0000069 | Dequeued verb Dial, callid %1, callType %2, calleridoption %3 (completion context %4)\r\n
0xb000006a | Verb completed with HRESULT %1; host notified (completion context %2)\r\n
0xb000006b | Verb completed with HRESULT %1; host not notified (completion context %2)\r\n
0xb000006c | Began tracking async CellVoice request id %1 (for completion context %2)\r\n
0xb000006d | Stopped tracking async CellVoice request id %1 (for completion context %2)\r\n
0xb000006e | Enqueued async CellVoice request id %1 completion with HRESULT %2\r\n
0xb000006f | Gsm call manager called I3GPPCallModel::%1 with async request id %2 for callid %3 (cellvoice callid %4)\r\n
0xb0000070 | Gsm call manager called I3GPPCallModel::%1 with async request id %2 for callids %3, %4\r\n
0xb0000071 | Gsm call manager called I3GPPCallModel::RequestOutgoingCall with async request id %1 for callid %2, callType %3 (no cellvoice callid)\r\n
0xb0000072 | CallManager got call progress update for cellvoiceId %1; status %2; direction %3; number %4; name %5; party %6; flags %7; type %8; valid params %9; \r\n
0xb0000073 | CellVoice returned failure %1 to get subscriber number\r\n
0xb0000074 | CellVoice returned failure %1 to get voicemail number\r\n
0xb0000075 | CellVoice get IMSI completed with error %1\r\n
0xb0000076 | Resetting VVM state; old MCC/MNC/nameDiff %1 %2 %3\r\n
0xb0000077 | Used RIL system type %1; got signal strength %2\r\n
0xb0000078 | Used RIL system type %1; voice domain %2; got registration status %3\r\n
0xb000007a | No Visual Voicemail provider was loaded for MCC,MNC %1,%2\r\n
0xb000007b | Visual Voicemail action %1 is not currently available on this line\r\n
0xb000007c | Legacy Voicemail message received: %1. Message count: %2\r\n
0xb000007d | Registered to operator: params %1; long name "%2"; short name "%3"; numeric name"%4"; country code "%5"\r\n
0xb000007e | Switched to data registration to get registration info\r\n
0xb000007f | Status %1 from cellcore reading voicemail count %2 from SIM\r\n
0xb0000080 | Status %1 from cellcore writing voicemail count %2 to SIM\r\n
0xb0000083 | [CellularAudio] Muting cellular audio\r\n
0xb0000084 | [CellularAudio] Unmuting cellular audio\r\n
0xb0000085 | CallManager got disconnect notification for cellvoiceId %1; initiator %2; reason %3; group %4; gppdetails [ location %5 cause %6 ]\r\n
0xb0000086 | CallModel3GPP2 invoking %1; callid %2; asyncRequestId %3\r\n
0xb0000087 | CdmaHeuristics invoking %1; callid %2 and %3; asyncRequestId %3; completionContext %4\r\n
0xb000008b | Call manager got call waiting notification for cellvoice callid %1: rilremotepartyinfo: params %2 numberpres %3 namepres %4\r\n
0xb000008c | Call manager got dial id notification for cellvoice callid %1: params %2 numberpres %3 namepres %4\r\n
0xb000008d | CdmaHeuristics started tracking verb %1 asyncRequestId %2 for completionContext %3\r\n
0xb000008e | CdmaHeuristics stopped tracking verb %1 asyncRequestId %2 for completionContext %3\r\n
0xb000008f | Status %1 from cellcore reading call forwarding status %2 from SIM\r\n
0xb0000090 | Status %1 from cellcore reading call forwarding number from SIM\r\n
0xb0000091 | Status %1 from cellcore writing call forwarding status to SIM\r\n
0xb0000092 | Status %1 from cellcore writing call forwarding number to SIM\r\n
0xb0000093 | Sim LockState changed to: %1\r\n
0xb0000094 | Cellvoice UICC Line set; sim swap pending: %1; old/new line ID: %2 / %3\r\n
0xb0000095 | Finished retrieving home MCC/MNC: %1 %2\r\n
0xb0000096 | Set visual voicemail provisioning state to %1\r\n
0xb0000097 | Forced SIM swap based on MCC/MNC: %1 %2 ==> %3 %4\r\n
0xb0000098 | Modem power state changed to %1\r\n
0xb0000099 | Network codes: params %1; MCC %2; MNC %3\r\n
0xb000009a | SIMOM gave LineFactory a duplicate modem (ignored)\r\n
0xb000009b | SIMOM gave LineFactory an unknown modem to remove (ignored)\r\n
0xb000009c | SIMOM gave LineFactory an unknown modem for adding a slot (ignored)\r\n
0xb000009d | SIMOM gave LoneFactory a duplicate slot (ignored)\r\n
0xb000009e | SIMOM gave LineFactory an unknown modem for removing a slot (ignored)\r\n
0xb000009f | SIMOM gave LineFactory an unknown slot to remove (ignored)\r\n
0xb00000a0 | Line not created: modem index %1 or slot index %2 out of bounds (from ISlot %3)\r\n
0xb00000a1 | CallManager new incoming call from %1\r\n
0xb00000a2 | Call forwarding state updated. SupSvcCode: %1; Enable: %2; new m_callForwardingState: %3\r\n
0xb00000a3 | Read call forwarding state from registry. m_callForwardingState: %1; m_callForwardingAddress: %2\r\n
0xb00000a4 | OnSupServiceCallback. ExecutionResult: %1; SvcCode: %2; DialAction: %3\r\n
0xb00000a5 | Legacy Voicemail message ignored due to config setting\r\n
0xb00000a6 | CdmaHeuristics set local hold to %1\r\n
0xb00000a7 | Detected SGLTE config with no GSM RF; using synthesized no-registration status\r\n
0xb00000a8 | Enqueued verb AcceptIncoming, callid %1, callType %2 (completion context %3)\r\n
0xb00000a9 | Dequeued verb AcceptIncoming, callid %1, callType %2 (completion context %3)\r\n
0xb00000aa | Gsm call manager called I3GPPCallModel::AcceptIncomingCall with async request id %1 for callid %2, callType %3 (cellvoice callid %4)\r\n
0xb00000ab | Received an IMS SIP disconnect cause: error-code=%1, reason=%2\r\n
0xb00000ac | Assumed error is XCAP related and enabling show/hide caller id feature\r\n
0xb00000ad | [Voicemail] Timer task for Visual Voicemail configuration changes fired.\r\n
0xb00000ae | [Voicemail] Attempting to queue action for Visual Voicemail configuration changes [isChangePending=%1]\r\n
0xb00000af | [Voicemail] Got notified of Visual Voicemail registry changes\r\n
0xb00000b0 | [Voicemail] Configure Visual Voicemail [homeMcc=%1][homeMnc=%2][dataAffinityExists=%3]\r\n
0xb00000b1 | Can Data affinity change [LineId=%1][dataAffinityCanIndex=%2]\r\n
0xb00000ca | Terminating Active Call Agent %1 due to timeout waiting for Notify callback\r\n
0xb00000cb | Cell Broadcast Listener received message %1\r\n
0xb00000cc | Display text changed: params %1, info type %2, info tag %3, message size %4\r\n
0xb00000cd | Calling IVoIPTaskManagerClient->LaunchActiveCallAgent(%1)\r\n
0xb00000ce | Calling IVoIPTaskManagerClient->CancelActiveCallAgentInstance(%1)\r\n
0xb00000cf | _CancelActiveCallAgent for product id: %1; isForcedShutdown: %2; isActiveCallAgentRunning: %3\r\n
0xb00000d0 | Calling IVoIPTaskManagerClient->HoldActiveCall(%1)\r\n
0xb00000d1 | Calling IVoIPTaskManagerClient->UnholdActiveCall(%1)\r\n
0xb00000d2 | Calling IVoIPTaskManagerClient->OnIncomingCallDialogDisplayed(%1)\r\n
0xb00000d3 | Calling IVoIPTaskManagerClient->OnIncomingCallDialogDismissed(%1)\r\n
0xb00000d4 | InitializedConnectionToAppHost called on VoipProvider. RPC Handle: %1; VoipLine: %2; AgentProcessId: %3; ContextId: %4\r\n
0xb00000d5 | LineFactory->NewIncomingCall(%1, %2)\r\n
0xb00000d6 | LineFactory->NewOutgoingCall(%1, %2)\r\n
0xb00000d7 | LineFactory->CallActive(%1, %2)\r\n
0xb00000d8 | LineFactory->CallHeld(%1, %2)\r\n
0xb00000d9 | LineFactory->CallEnded(%1, %2)\r\n
0xb00000da | LineFactory->SetAudioRouting(%1, %2)\r\n
0xb00000db | LineFactory->GetAudioRouting(%1)\r\n
0xb00000dc | LineFactory->SetMuteState(%1, %2)\r\n
0xb00000dd | LineFactory->UpdateCallContactName(%1, %2)\r\n
0xb00000de | LineFactory->UpdateCallStartTime(%1, %2)\r\n
0xb00000df | LineFactory->GetCallStartTime(%1, %2)\r\n
0xb00000e0 | LineFactory->UpdateCallAttributes(%1, %2, %3)\r\n
0xb00000e1 | VoipAppHostHandle_rundown(%1)\r\n
0xb00000e2 | _PendingRpcCallCompleted(%2, %3) for line: %1; onTime: %4\r\n
0xb00000e3 | Calling %1 on VoipApp for line: %2. Controller callId: %3; VoipApp CallId: %4\r\n
0xb00000e4 | Calling %1 on VoipApp for line: %2.\r\n
0xb00000e5 | Calling OnAudioRouteChanged on VoipApp for line: %1. AudioRoute: %2; Available Paths: %3\r\n
0xb00000e6 | Can %1 entered emergency mode %2\r\n
0xb00000e7 | Modem constraint violated: Illegal CPI %1\r\n
0xb00000e8 | Modem constraint violated: Async dial failure %1 for call in CPI state %2\r\n
0xb00000e9 | Modem constraint violated: Mismatched direction fields; direction %1, CPI state %2\r\n
0xb00000ea | CallManager invoked I3GPP[2]CallModel::%1; asyncRequestId %2\r\n
0xb00000eb | CallManager invoking I3GPP[2]CallModel::%1; asyncRequestId %2\r\n
0xb00000ec | CallModel3GPP2 invoking %1; callid %2 and %3; asyncRequestId %4)\r\n
0xb00000ed | CdmaHeuristics invoking %1; callid %2; asyncRequestId %3; completionContext %4\r\n
0xb00000ee | CdmaHeuristics verb completed: asyncRequestId %1; result %2; verb %3; callid %4; original completionContext %5\r\n
0xb00000ef | CdmaHeuristics verb completed: asyncRequestId %1; result %2\r\n
0xb00000f0 | CallModel3GPP2 verb completed: asyncRequestId %1; result %2; verb %3; callid %4; original completionContext %5\r\n
0xb00000f1 | Dequeued async CellVoice request id %1 completion with HRESULT %2\r\n
0xb00000f2 | CallModel processing call progress update with cellvoiceId %1 for callId %2\r\n
0xb00000f5 | CdmaHeuristics tracking with asyncRequestId %1 not found\r\n
0xb00000f9 | CallModel3GPP2 got unexpected call update for cellvoiceId %1; while having existing cellvoiceId %2\r\n
0xb00000fd | Processed request to clear Voicemail count.\r\n
0xb00000fe | Default voicemail number source is: %1\r\n
0xb00000ff | Modem constraint violated: Illegal 3GPP2 CallWaiting notification\r\n
0xb0000100 | Tone signal received: params %1, %2, %3, %4\r\n
0xb0000101 | LineNotificationWorkItem: instantiated #%1 (%2)\r\n
0xb0000102 | LineNofiticationWorkItem: processing #%1 (%2)\r\n
0xb0000103 | LineNofiticationWorkItem: finished processing #%1 (%2)\r\n
0xb0000104 | LineNofiticationWorkItem: canceled #%1 (%2)\r\n
0xb0000105 | Got subscriber numbers; dwNumSubscribers = %1\r\n
0xb0000106 | Subscriber number entry #%1: params #2, service #3\r\n
0xb0000107 | Subscriber number is missing or empty\r\n
0xb0000108 | Got IMS status change notification. [Params=%1][AvailableServices=%2]\r\n
0xb0000109 | [CallModel3GPP] Call model changing between GSM and IMS, [ims=%1][m_imsOnWiFi=%2]\r\n
0xb000010a | Roaming override number used.  Dialing %1.\r\n
0xb000010b | HandleUICCPersoCheckStatusChange, [dwParams=%1][dwPersoFeature=%2][dwPersoCheckState=%3]\r\n
0xb000010c | Get Perso deactivation state for %1 completed with hr %2; params %3; state %4; unlock remaining %5; unblock remaining %6\r\n
0xb000010d | Deactivate Perso for %1 completed with hr %2; params %3; state %4; unlock remaining %5; unblock remaining %6; async API context %7\r\n
0xb000010e | Initiating SIM PIN operation %1; async completion context = %2\r\n
0xb000010f | Initiating Perso unlock for %1; async completion context = %2\r\n
0xb0000110 | SIM PIN operation '%1' with async completion context %2 complete, result % = 3\r\n
0xb0000111 | 3GPP2CallModel ignored alien call (CellVoice ID %1) due to existing call (CellVoice ID %2).\r\n
0xb0000112 | 3GPPCallModel suppressed call update due to invalid state.\r\n
0xb0000113 | Unsolicited supservice %1 received for CellVoice callid %2\r\n
0xb0000114 | CellVoice Response Received in Method: %1. Async Hresult: %2\r\n
0xb0000115 | dwParams %1; dwNetworkSSErrorCause %2; dwNetworkCCErrorCause %3; dwVendorErrorCause %4\r\n
0xb0000116 | CellVoice reported infoClasses: %1.\r\n
0xb0000117 | CellVoice reported hide ID settings: params %1, status %2, provisioning %3.\r\n
0xb0000118 | CellVoice reported call forwarding settings: params %1, info class %2, delay time %3, status %4.\r\n
0xb0000119 | CellVoice Ussd Data Status: %1.\r\n
0xb000011a | Ussd Session terminated\r\n
0xb000011b | New Ussd Session initiated\r\n
0xb000011c | Invalid Callforwarding delay time parameter: %1. Using default value instead.\r\n
0xb000011d | Using default value for call forwarding delay time\r\n
0xb000011e | CellVoice reported COLR settings: params %1, status %2, provisioning %3.\r\n
0xb000011f | CellVoice reported CLIP settings: params %1, status %2, provisioning %3.\r\n
0xb0000120 | Executing sup service code %1, action %2\r\n
0xb0000121 | Ussd User response truncated\r\n
0xb0000122 | CellVoice reported COLP settings: params %1, status %2, provisioning %3.\r\n
0xb0000123 | Address for unsolicited supservice %1 is %2\r\n
0xb0000124 | Calling %1 on VoipApp for line: %2. VoipApp CallId: %3\r\n
0xb0000127 | RemoteId Request Complete: CallId: %1 RemoteId Exists: %2\r\n
0xb0000128 | Launching Voip app with URI: %1\r\n
0xb0000129 | LineFactory->NewIncomingUpgradeCall(%1, %2)\r\n
0xb000012a | LineFactory->NewOutgoingUpgradeCall(%1, %2). CallUpgradeGuid: %3\r\n
0xb000012b | LineFactory->CallReady(%1, %2)\r\n
0xb000012c | 3GPPCallModel suppressed call update due to ECall Failover.\r\n
0xb000012d | Dialing an Emergency call. PhoneCallId: %1.\r\n
0xb000012e | 3GPPCallModel got surprise outgoing Emergency call notification. Existing ECallId: %1, IgnoreNotification: %2.\r\n
0xb000012f | Modem Radio Config changed to %1\r\n
0xb0000130 | Setting Can Focus for Can: %1\r\n
0xb0000131 | Set Can Focus result: %1\r\n
0xb0000132 | Disconnecting dialed call with callId: %1 for incoming call.\r\n
0xb0000133 | LineFactory->GetNextOperation(%1)\r\n
0xb0000134 | Terminating Call Query Agent %1 due to timeout waiting for Notify callback\r\n
0xb0000135 | lineFactory->VoipAppOperationComplete(%1). Completed operationId: %2. Succeeded: %3. Call upgrade support: %4\r\n
0xb0000136 | Calling IVoIPTaskManagerClient->LaunchCallQueryAgent(%1)\r\n
0xb0000137 | Calling IVoIPTaskManagerClient->CancelCallQueryAgentInstance(%1)\r\n
0xb0000138 | Received async dial completion. CallId: %1, CellVoice CallId: %2\r\n
0xb0000139 | 3GPP2CallModel ignored disconnected call (CellVoice ID %1) due to existing call (CellVoice ID %2).\r\n
0xb000013a | Detected LTE System Type with no network registration and no voice domain.\r\n
0xb000013b | CallManager invoked I3GPP[2]CallModel::%1; asyncRequestId %2, Dialed Number: %3\r\n
0xb000013c | Update to call type or video context.  CallId: %1, CallType: %2, Video Context: %3\r\n
0xb000013d | CallModel3GPP2 CallVerb_SetVideoPaused; CallId: %1; paused: %2; completion context: %3\r\n
0xb000013e | CallModel3GPP CallVerb_SetVideoPaused; CallId: %1; paused: %2; async id: %3\r\n
0xb000013f | Enqueued verb SetVideoPaused, callid %1, paused %2, (completion context %3)\r\n
0xb0000140 | Dequeued verb SetVideoPaused, callid %1, paused %2, (completion context %3)\r\n
0xb0000141 | Video state update.  Params: %1, Action: %2, Direction: %3, State Params: %4, Peer caps: %5, Flags: %6, ContextID: %7\r\n
0xb0000142 | Calling Cellular API in media update for %1.  Async request id: %2, CallId %3, CellVoice CallId: %4)\r\n
0xb0000143 | Requesting video state publish.  Subscriber Number: %1, videoCapable: %2\r\n
0xb0000144 | Line type changed but SupService was not reset.\r\n
0xb0000145 | Registration state according to voice domain, voice domain: %1, registration status: %2, mapped registration state: %3\r\n
0xb0000146 | SubscriptionUpdate OMADM initiated : %1 HR = %2\r\n
0xb0000147 | Video direction override during multitasking, new transmit state: %1\r\n
0xb0000148 | CellularLine SetVideoCallingSetting: [CurrentState=%1][RequestType=%2][CacheSetting=%3][PerSimConfigAvailable=%4][TargetState=%5]\r\n
0xb0000149 | IMS system-type changing from %1 to %2\r\n
0xb000014a | Video media offer answer. Params: %1, Action: %2, Direction: %3, State Params: %4, Peer caps: %5, Flags: %6, ContextID: %7\r\n
0xb000014b | LineFactory->EndUpgradeOriginationCall(%1)\r\n
0xb000014c | LineFactory->CancelUpgrade(%1)\r\n
0xb000014d | ImsHandoverAttempt notify arrives. hrHandOverResult: %1, OldSystemType: %2, NewSystemType: %3\r\n
0xb000014e | GetVideoCapabilitySharingSettings: Queried, [LineId=%1][PerSimConfigAvaiable=%2][IsCapabilitySharingEnabled=%3][LastModifiedTimestamp=%4]\r\n
0xb000014f | SetVideoCapabilitySharingSettings: Updating, [LineId=%1][PerSimConfigAvaiable=%2][IsCapabilitySharingEnabled=%3][CurrentTimestamp=%4]\r\n
0xb0000150 | Applying video calling setting to saved or default user preference.\r\n
0xb0000151 | Unable to determine cached video calling setting.\r\n
0xb0000152 | Updated home MCC value from SIM in line specific data, [LineId=%1][HomeMcc=%2].\r\n
0xb0000153 | CallRecording: Phone service was notified of a Call Recording application whose Package Family Name is too long: '%1'\r\n
0xb0000155 | IMS service voice changed, [imsVoiceAvailable=%1][imsVideoAvailable=%2][videoCallingEnabled=%3]\r\n
0xb0000156 | IMS service video changed, [imsVoiceAvailable=%1][imsVideoAvailable=%2][videoCallingEnabled=%3]\r\n
0xb0000157 | DeterminePhoneSystemType, [imsVoiceSupported=%1][registration0SystemType=%2][registration0VoiceDomain=%3][callPresence=%4]\r\n
0xb0000158 | UpdateLineSystemType, [currentLineSystemType=%1][newLineSystemType=%2]\r\n
0xb0000159 | SetRadioAccessTechnology, [radioAccessTechnology=%1][toIms=%2][toGsm=%3][toCdma=%4][fromIms=%5][fromGsm=%6][fromCdma=%7]\r\n
0xb000015a | SetRadioAccessTechnology, switching call model, [To3GPP=%1]\r\n
0xb000015b | UpdateCallPresence, [currentPresence=%1][aggregatePresence=%2][allSameType=%3]\r\n
0xb000015c | [CallModel3GPP] Updating audio, [audioType=%1][audioActive=%2][anyCallNeedsAudio=%3][anyCallNeedsAudioActive=%4][localHoldSupported=%5]\r\n
0xb000015d | [CallModel3GPP2] Updating audio, [audioType=%1][shouldEnableAudio=%2][audioAllowed=%3]\r\n
0xb000015e | [CellularAudio] Updating audio for handover notification, [inProgress=%1][isHandoverNotification=%2][phase=%3][oldType=%4][newType=%5]\r\n
0xb000015f | ProcessHandoverNotification, [callInfoParams=%1][phase=%2][handoverStateParams=%3][oldType=%4][newType=%5][inProgress=%6]\r\n
0xb0000160 | Reset handover state\r\n
0xb0000161 | Updated video call conference state, [CallId=%1][CellVoiceCallId=%2][ContextId=%3][ConferenceContextId=%4][PreviousState=%5][UpdatedState=%6].\r\n
0xb0000162 | Interpret E_SUPSVCS_INVALIDREMOTEURI as success with call forwarding status disabled.\r\n
0xb0000163 | IR94FeatureDisabled: Disable video calling.\r\n
0xb0000164 | IR94FeatureDisabled: Force disable video calling.\r\n
0xb0000165 | Emergency call failed over. ECallId: %1.\r\n
0xb0000166 | Emergency call DisableAndEnable Audio from 3GPP CallModel. ECallId: %1.\r\n
0xb0000167 | Emergency call DisableAndEnable Audio from 3GPP2 CallModel. ECallId: %1.\r\n
0xb0000168 | HandleUICCPinLockStateChange, [dwParams=%1][dwLockState=%2]\r\n
0xb0000169 | Updating UICC related information from SIM\r\n
0xb000016a | OnSubscriberNumbersChange, [result=%1]\r\n
0xb000016b | [CallModel3GPP] Notified for IMS on Wifi flag, [m_imsOnWiFi=%1][onWiFi=%2]\r\n
0xb000016c | Removed stale pending RPC for line: %1, callid: %2, type: %3\r\n
0xb000016d | Timedout pending RPC for line: %1, callid: %2, type: %3\r\n
0xb000016e | ResetConnectionToApp for line: %1\r\n
0xb000016f | CleanupVoipAppConnectionState for line: %1, pendingRPCCalls: %2, voipAppProcessId: %3\r\n
0xb0000170 | VoIP Line Id: %1 has AboveLock extension: %2\r\n
0xb0000171 | Enqueued verb %1, (completion context %2)\r\n
0xb0000172 | Dequeued verb %1, (completion context %2)\r\n
0xb0000173 | CellularCallModel initiating explicit call transfer; asyncRequestId %1\r\n
0xb0000174 | Ril audio codec %1 mapped to %2 for CallId: %3.\r\n
0xb0000175 | [Voicemail] Stop VVM Invoked [stopReason=%1]\r\n
0xb0000176 | [Voicemail] Start VVM Invoked [last stopReason=%1]\r\n
0xb0000177 | LineFactory->ReserveVoipCallResources(%1, %3, %2) Completed.\r\n
0xb0000178 | LineFactory->CancelVoipCallResourceReservation(%1) Completed.\r\n
0xb0000179 | [VoipLine#%1] Calling LaunchVoipRtcTask(%3, %4, %2)\r\n
0xb000017a | [VoipLine#%1] Calling CancelVoipRtcTask(%2)\r\n
0xb000017b | [VoipLine#%1] Calling NotifyVoipActivityCompleted(%2)\r\n
0xb000017c | CallerId Prefix updated.  Updated number is %1.\r\n
0xb000041b | Received IMS Failure changed, [imsFailureMessageType=%1].\r\n
0xb000041c | Ims failure error string is missing or empty.\r\n
0xb000041d | WiFi call disconnect occured, [errorMessage=%1] .\r\n
0xb000041e | WiFi internet connection status: %1.\r\n
0xb000041f | WiFi calling feature enabled: %1.\r\n
0xb0000420 | WiFi calling upsell suppressed: %1.\r\n
0xb0000421 | Media Configuration Data, Set Index: %1, IMS Service Type: %2, Media Preference: %3.\r\n
0xb0000422 | Placing request for switching cellular audio provider, Executor Index: %1, Old Audio type: %2, New Audio Type: %3.\r\n
0xd0000001 | CallType_AudioOnly\r\n
0xd0000002 | CallType_AudioVideo\r\n
0xd0000003 | CallerIdOption_Default\r\n
0xd0000004 | CallerIdOption_ForceSend\r\n
0xd0000005 | CallerIdOption_ForceBlock\r\n
0xd0000006 | PH_CALLDIRECTION_INCOMING\r\n
0xd0000007 | PH_CALLDIRECTION_OUTGOING\r\n
0xd0000008 | PH_REGISTRATIONSTATE_UNKNOWN\r\n
0xd0000009 | PH_REGISTRATIONSTATE_UNREGISTERED_NO_SIGNAL\r\n
0xd000000a | PH_REGISTRATIONSTATE_UNREGISTERED_WITH_SIGNAL\r\n
0xd000000b | PH_REGISTRATIONSTATE_REGISTERING\r\n
0xd000000c | PH_REGISTRATIONSTATE_REGISTERING_AFTER_DENIED\r\n
0xd000000d | PH_REGISTRATIONSTATE_REGISTERED_HOME\r\n
0xd000000e | PH_REGISTRATIONSTATE_REGISTERED_ROAM\r\n
0xd000000f | PH_REGISTRATIONSTATE_DENIED\r\n
0xd0000010 | PH_REGISTRATIONSTATE_REGISTERED_ROAM_DOMESTIC\r\n
0xd0000011 | RIL_VOICE_DOMAIN_NONE\r\n
0xd0000012 | RIL_VOICE_DOMAIN_3GPP\r\n
0xd0000013 | RIL_VOICE_DOMAIN_3GPP2\r\n
0xd0000014 | RIL_VOICE_DOMAIN_IMS\r\n
0xd0000015 | RIL_CALLDIR_INCOMING\r\n
0xd0000016 | RIL_CALLDIR_OUTGOING\r\n
0xd0000017 | RIL_CPISTAT_UNKNOWN\r\n
0xd0000018 | RIL_CPISTAT_NEW_OUTGOING\r\n
0xd0000019 | RIL_CPISTAT_NEW_INCOMING\r\n
0xd000001a | RIL_CPISTAT_CONNECTED\r\n
0xd000001b | RIL_CPISTAT_DISCONNECTED\r\n
0xd000001c | RIL_CPISTAT_ONHOLD\r\n
0xd000001d | RIL_CPISTAT_MEDIA\r\n
0xd000001e | RIL_CPISTAT_HANDOVER\r\n
0xd000001f | RIL_CALL_SINGLEPARTY\r\n
0xd0000020 | RIL_CALL_MULTIPARTY\r\n
0xd0000021 | RIL_REMOTEPARTYINFO_VALID\r\n
0xd0000022 | RIL_REMOTEPARTYINFO_WITHHELD\r\n
0xd0000023 | RIL_REMOTEPARTYINFO_UNAVAILABLE\r\n
0xd0000024 | RIL_DISCINIT_UNKNOWN\r\n
0xd0000025 | RIL_DISCINIT_LOCAL\r\n
0xd0000026 | RIL_DISCINIT_REMOTE\r\n
0xd0000027 | RIL_DISCREASON_NULL\r\n
0xd0000028 | RIL_DISCREASON_BUSY\r\n
0xd0000029 | RIL_DISCREASON_NETWORKERROR\r\n
0xd000002a | RIL_DISCREASON_RADIOFADE\r\n
0xd000002b | RIL_DISCREASON_CONGESTION\r\n
0xd000002c | RIL_DISCREASON_EMERGENCYONLY\r\n
0xd000002d | RIL_DISCREASON_NOSERVICE\r\n
0xd000002e | RIL_DISCREASON_OTHEREXECUTORBUSY\r\n
0xd000002f | RIL_DISCREASON_EMERGENCYFAILOVER\r\n
0xd0000030 | RIL_DISCREASON_HANDOVER_MERGE\r\n
0xd0000031 | RIL_CALLTYPE_VOICE\r\n
0xd0000032 | RIL_CALLTYPE_DATA\r\n
0xd0000033 | RIL_CALLTYPE_FAX\r\n
0xd0000034 | RIL_CALLTYPE_PTT\r\n
0xd0000035 | RIL_CALLTYPE_VT\r\n
0xd0000036 | RIL_CALLTYPE_USSD\r\n
0xd0000037 | RIL_CALLTYPE_SUPSVC\r\n
0xd0000038 | RIL_CALLTYPE_IMS\r\n
0xd0000039 | RIL_CD_UNKNOWN_CAUSE\r\n
0xd000003a | RIL_CD_AS_CAUSE\r\n
0xd000003b | RIL_CD_3GPP_NETWORK_CAUSE\r\n
0xd000003c | RIL_CD_3GPP2_VENDOR_CAUSE\r\n
0xd000003d | RIL_CD_OTHER_CAUSE\r\n
0xd000003e | RIL_CD_3GPP_REJECT_CAUSE\r\n
0xd000003f | RIL_CD_IMS_SIP_CAUSE\r\n
0xd0000040 | RIL_EXTENDED_DISPLAY_TYPE_NORMAL\r\n
0xd0000041 | RIL_EXTENDED_DISPLAY_TAG_BLANK\r\n
0xd0000042 | RIL_EXTENDED_DISPLAY_TAG_SKIP\r\n
0xd0000043 | RIL_EXTENDED_DISPLAY_TAG_CONTINUATION\r\n
0xd0000044 | RIL_EXTENDED_DISPLAY_TAG_CALLED_ADDRESS\r\n
0xd0000045 | RIL_EXTENDED_DISPLAY_TAG_CAUSE\r\n
0xd0000046 | RIL_EXTENDED_DISPLAY_TAG_PROGRESS_INDICATOR\r\n
0xd0000047 | RIL_EXTENDED_DISPLAY_TAG_NOTIFICATION_INDICATOR\r\n
0xd0000048 | RIL_EXTENDED_DISPLAY_TAG_PROMPT\r\n
0xd0000049 | RIL_EXTENDED_DISPLAY_TAG_ACCUMULATED_DIGITS\r\n
0xd000004a | RIL_EXTENDED_DISPLAY_TAG_STATUS\r\n
0xd000004b | RIL_EXTENDED_DISPLAY_TAG_INBAND\r\n
0xd000004c | RIL_EXTENDED_DISPLAY_TAG_CALLING_ADDRESS\r\n
0xd000004d | RIL_EXTENDED_DISPLAY_TAG_REASON\r\n
0xd000004e | RIL_EXTENDED_DISPLAY_TAG_CALLING_PARTY_NAME\r\n
0xd000004f | RIL_EXTENDED_DISPLAY_TAG_CALLED_PARTY_NAME\r\n
0xd0000050 | RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NAME\r\n
0xd0000051 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NAME\r\n
0xd0000052 | RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NAME\r\n
0xd0000053 | RIL_EXTENDED_DISPLAY_TAG_ORIGINATING_RESTRICT\r\n
0xd0000054 | RIL_EXTENDED_DISPLAY_TAG_DATE_TIME_OF_DAY\r\n
0xd0000055 | RIL_EXTENDED_DISPLAY_TAG_CALL_APPEARANCE_ID\r\n
0xd0000056 | RIL_EXTENDED_DISPLAY_TAG_FEATURE_ADDRESS\r\n
0xd0000057 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NAME\r\n
0xd0000058 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NUMBER\r\n
0xd0000059 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NUMBER\r\n
0xd000005a | RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NUMBER\r\n
0xd000005b | RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NUMBER\r\n
0xd000005c | RIL_EXTENDED_DISPLAY_TAG_TEXT\r\n
0xd000005d | RIL_REGSTAT_UNKNOWN\r\n
0xd000005e | RIL_REGSTAT_UNREGISTERED\r\n
0xd000005f | RIL_REGSTAT_HOME\r\n
0xd0000060 | RIL_REGSTAT_ATTEMPTING\r\n
0xd0000061 | RIL_REGSTAT_DENIED\r\n
0xd0000062 | RIL_REGSTAT_ROAMING\r\n
0xd0000063 | RIL_REGSTAT_ROAMING_DOMESTIC\r\n
0xd0000064 | MODEM_POWER_OFF\r\n
0xd0000065 | MODEM_POWER_GOING_ON\r\n
0xd0000066 | MODEM_POWER_ON\r\n
0xd0000067 | MODEM_POWER_GOING_OFF\r\n
0xd0000068 | MODEM_POWER_SHUTTING_DOWN\r\n
0xd0000069 | RADIO_CONFIG_SINGLE\r\n
0xd000006a | RADIO_CONFIG_MULTI_MODE\r\n
0xd000006b | RADIO_CONFIG_1XCSFB\r\n
0xd000006c | RADIO_CONFIG_SVLTE\r\n
0xd000006d | RADIO_CONFIG_DualStandby\r\n
0xd000006e | RADIO_CONFIG_DualActive\r\n
0xd000006f | RADIO_CONFIG_SGLTE\r\n
0xd0000070 | RADIO_CONFIG_SVLTE_DUALACTIVE\r\n
0xd0000071 | RADIO_CONFIG_SGLTE_DUALACTIVE\r\n
0xd0000072 | RADIO_CONFIG_SRLTE\r\n
0xd0000073 | VoipIpcAudioRoute_Default\r\n
0xd0000074 | VoipIpcAudioRoute_Earpiece\r\n
0xd0000075 | VoipIpcAudioRoute_Speakerphone\r\n
0xd0000076 | VoipIpcAudioRoute_Bluetooth\r\n
0xd0000077 | RpcCallType_SetInitialAppState\r\n
0xd0000078 | RpcCallType_AcceptIncoming\r\n
0xd0000079 | RpcCallType_CallActive\r\n
0xd000007a | RpcCallType_End\r\n
0xd000007b | RpcCallType_Hold\r\n
0xd000007c | RpcCallType_RejectIncoming\r\n
0xd000007d | RpcCallType_Unhold\r\n
0xd000007e | RpcCallType_Mute\r\n
0xd000007f | RpcCallType_Unmute\r\n
0xd0000080 | RpcCallType_ForceEnd\r\n
0xd0000081 | PH_VOICEMAILPROVISIONINGSTATE_LEGACY_ONLY\r\n
0xd0000082 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_SUPPORTED\r\n
0xd0000083 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_CONFIGURED\r\n
0xd0000084 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_ENABLED\r\n
0xd0000085 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_ENABLED_NEW_USER\r\n
0xd0000086 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_NOT_FUNCTIONING\r\n
0xd0000087 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_CREATED\r\n
0xd0000088 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_PASSWORD_RESET\r\n
0xd0000089 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_INITIALIZED\r\n
0xd000008a | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_NO_DATA_AFFINITY\r\n
0xd000008b | StopVvmReason_Default\r\n
0xd000008c | StopVvmReason_DualSim_SingleLineVvm\r\n
0xd000008d | StopVvmReason_DualSim_NoDataAffinity\r\n
0xd000008e | RIL_3GPPTONE_TONEOFF\r\n
0xd000008f | RIL_3GPPTONE_RINGBACK\r\n
0xd0000090 | RIL_3GPPTONE_BUSY\r\n
0xd0000091 | RIL_3GPPTONE_CONGESTION\r\n
0xd0000092 | RIL_3GPPTONE_AUTHENTICATIONFAILURE\r\n
0xd0000093 | RIL_3GPPTONE_NUMBERUNOBTAINABLE\r\n
0xd0000094 | RIL_3GPPTONE_CALLDROPPED\r\n
0xd0000095 | RIL_3GPP2TONE_TONEOFF\r\n
0xd0000096 | RIL_3GPP2TONE_DIAL\r\n
0xd0000097 | RIL_3GPP2TONE_RINGBACK\r\n
0xd0000098 | RIL_3GPP2TONE_INTERCEPT\r\n
0xd0000099 | RIL_3GPP2TONE_ABRVINTERCEPT\r\n
0xd000009a | RIL_3GPP2TONE_REORDER\r\n
0xd000009b | RIL_3GPP2TONE_ABRVREORDER\r\n
0xd000009c | RIL_3GPP2TONE_BUSY\r\n
0xd000009d | RIL_3GPP2TONE_CONFIRM\r\n
0xd000009e | RIL_3GPP2TONE_ANSWER\r\n
0xd000009f | RIL_3GPP2TONE_CALLWAITING\r\n
0xd00000a0 | RIL_3GPP2TONE_PIP\r\n
0xd00000a1 | RIL_3GPP2ISDNALERTING_ALERTINGOFF\r\n
0xd00000a2 | RIL_3GPP2ISDNALERTING_NORMAL\r\n
0xd00000a3 | RIL_3GPP2ISDNALERTING_INTERGROUP\r\n
0xd00000a4 | RIL_3GPP2ISDNALERTING_SPECIAL\r\n
0xd00000a5 | RIL_3GPP2ISDNALERTING_PINGRING\r\n
0xd00000a6 | RIL_PERSOCHECKSTATE_NOTREADY\r\n
0xd00000a7 | RIL_PERSOCHECKSTATE_PASS\r\n
0xd00000a8 | RIL_PERSOCHECKSTATE_FAIL\r\n
0xd00000a9 | RIL_DEPERSOSTATE_READY\r\n
0xd00000aa | RIL_DEPERSOSTATE_CK_REQUIRED\r\n
0xd00000ab | RIL_DEPERSOSTATE_PUK_REQUIRED\r\n
0xd00000ac | RIL_DEPERSOSTATE_PUK_BLOCKED\r\n
0xd00000ad | No voicemail number found\r\n
0xd00000ae | SIM override key\r\n
0xd00000af | SIM data\r\n
0xd00000b0 | Default number cached in registry\r\n
0xd00000b1 | SIM fallback key\r\n
0xd00000b2 | Kind_None\r\n
0xd00000b3 | Kind_EmergencyModeChange\r\n
0xd00000b4 | Kind_ExitEmergencyModeFinished\r\n
0xd00000b5 | Kind_NetworkRegistrationChange\r\n
0xd00000b6 | Kind_SignalStrengthChange\r\n
0xd00000b7 | Kind_ModemPowerStateChange\r\n
0xd00000b8 | Kind_SubscriberNumberChange\r\n
0xd00000b9 | Kind_RegistryConfigChange\r\n
0xd00000ba | Kind_VoicemailNumberChangeRequest\r\n
0xd00000bb | Kind_VoicemailNumberSimSetCompleted\r\n
0xd00000bc | Kind_VoicemailNumberSimGetCompleted\r\n
0xd00000bd | Kind_Imsi\r\n
0xd00000be | Kind_SupServiceCallback\r\n
0xd00000bf | Kind_PinLockState\r\n
0xd00000c0 | Kind_SlotState\r\n
0xd00000c1 | Kind_SetCallerId\r\n
0xd00000c2 | Kind_ToneNotification\r\n
0xd00000c3 | Kind_CellBroadcastMessage\r\n
0xd00000c4 | Kind_GetLineCallForwardingStatusCompletion\r\n
0xd00000c5 | Kind_SetLineCallForwardingStatusCompletion\r\n
0xd00000c6 | Kind_GetLineCallForwardingNumberCompletion\r\n
0xd00000c7 | Kind_ServiceProviderNameChange\r\n
0xd00000c8 | Kind_PersoCheckStatus\r\n
0xd00000c9 | Kind_PersoDeactivationState\r\n
0xd00000ca | Kind_MuteStateChange\r\n
0xd00000cb | Kind_SlotCanAssociationsChanged\r\n
0xd00000cc | Kind_CallPresenceChanged\r\n
0xd00000cd | Kind_ImsStatusChanged\r\n
0xd00000ce | Kind_ImsSystemTypeChanged\r\n
0xd00000cf | Kind_RefreshVideoCallingSetting\r\n
0xd00000d0 | Kind_SetVideoCallingSetting\r\n
0xd00000d1 | Kind_SetVideoCallingSettingComplete\r\n
0xd00000d2 | Kind_GetVideoCallingSettingComplete\r\n
0xd00000d3 | Kind_GetPSMediaPreferencesComplete\r\n
0xd00000d4 | Kind_PSMediaPreferencesChanged\r\n
0xd00000d5 | RIL_SERVICE_UNKNOWN\r\n
0xd00000d6 | RIL_SERVICE_VOICE\r\n
0xd00000d7 | RIL_SERVICE_FAX\r\n
0xd00000d8 | RIL_SERVICE_OTHER\r\n
0xd00000d9 | FWDCODE_UNCONDITIONAL\r\n
0xd00000da | FWDCODE_BUSY\r\n
0xd00000db | FWDCODE_NOREPLY\r\n
0xd00000dc | FWDCODE_NOTREACHABLE\r\n
0xd00000dd | FWDCODE_ALL\r\n
0xd00000de | FWDCODE_ALLCONDITIONAL\r\n
0xd00000df | FWDCODE_STATECHANGED\r\n
0xd00000e0 | SimPinOperation_None\r\n
0xd00000e1 | SimPinOperation_EnableSimPin\r\n
0xd00000e2 | SimPinOperation_DisableSimPin\r\n
0xd00000e3 | SimPinOperation_ChangeSimPin\r\n
0xd00000e4 | SimPinOperation_UnlockSim\r\n
0xd00000e5 | SimPinOperation_UnblockSim\r\n
0xd00000e6 | PersoFeature_Unknown\r\n
0xd00000e7 | PersoFeature_None\r\n
0xd00000e8 | PersoFeature_3Gpp_Net\r\n
0xd00000e9 | PersoFeature_3Gpp_NetSub\r\n
0xd00000ea | PersoFeature_3Gpp_Sp\r\n
0xd00000eb | PersoFeature_3Gpp_Corp\r\n
0xd00000ec | PersoFeature_3Gpp_USim\r\n
0xd00000ed | PersoFeature_3Gpp2_NetType1\r\n
0xd00000ee | PersoFeature_3Gpp2_NetType2\r\n
0xd00000ef | PersoFeature_3Gpp2_Hrpd\r\n
0xd00000f0 | PersoFeature_3Gpp2_Sp\r\n
0xd00000f1 | PersoFeature_3Gpp2_Corp\r\n
0xd00000f2 | PersoFeature_3Gpp2_Uim\r\n
0xd00000f3 | DialAction_None\r\n
0xd00000f4 | DialAction_Activation\r\n
0xd00000f5 | DialAction_Deactivation\r\n
0xd00000f6 | DialAction_Interrogation\r\n
0xd00000f7 | DialAction_Registration\r\n
0xd00000f8 | DialAction_Erasure\r\n
0xd00000f9 | RIL_UNSSSCODE_FORWARDEDCALL\r\n
0xd00000fa | RIL_UNSSSCODE_CUGCALL\r\n
0xd00000fb | RIL_UNSSSCODE_CALLPUTONHOLD\r\n
0xd00000fc | RIL_UNSSSCODE_CALLRETRIEVED\r\n
0xd00000fd | RIL_UNSSSCODE_ENTEREDMULTIPARTY\r\n
0xd00000fe | RIL_UNSSSCODE_HELDCALLRELEASED\r\n
0xd00000ff | RIL_UNSSSCODE_FORWARDCHECKSS\r\n
0xd0000100 | RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER\r\n
0xd0000101 | RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER\r\n
0xd0000102 | RIL_UNSSSCODE_DEFLECTEDCALL\r\n
0xd0000103 | RIL_UNSSSCODE_ADDITIONALINCOMINGCF\r\n
0xd0000104 | RIL_UNSSSCODE_UNCONDITIONALCFACTIVE\r\n
0xd0000105 | RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE\r\n
0xd0000106 | RIL_UNSSSCODE_CALLWASFORWARDED\r\n
0xd0000107 | RIL_UNSSSCODE_CALLISWAITING\r\n
0xd0000108 | RIL_UNSSSCODE_OUTGOINGCALLSBARRED\r\n
0xd0000109 | RIL_UNSSSCODE_INCOMINGCALLSBARRED\r\n
0xd000010a | RIL_UNSSSCODE_CLIRSUPPRESSREJECT\r\n
0xd000010b | RIL_IMSSYSTEMTYPE_UNKNOWN\r\n
0xd000010c | RIL_IMSSYSTEMTYPE_WIFI\r\n
0xd000010d | RIL_IMSSYSTEMTYPE_LTE\r\n
0xd000010e | CallUpgradeSupportLevel_NotSupported\r\n
0xd000010f | CallUpgradeSupportLevel_NonSeamless\r\n
0xd0000110 | CallUpgradeSupportLevel_Seamless\r\n
0xd0000111 | CallUpgradeSupportLevel_AppDetermined\r\n
0xd0000112 | VideoCallingSetting_Disabled\r\n
0xd0000113 | VideoCallingSetting_Enabled\r\n
0xd0000114 | VideoCallingSetting_CachedValue\r\n
0xd0000115 | RIL_CALLMEDIADIRECTION_NONE\r\n
0xd0000116 | RIL_CALLMEDIADIRECTION_RX\r\n
0xd0000117 | RIL_CALLMEDIADIRECTION_TX\r\n
0xd0000118 | RIL_CALLMEDIADIRECTION_RXTX\r\n
0xd0000119 | RIL_CALLMEDIAOFFERACTION_NONE\r\n
0xd000011a | RIL_CALLMEDIAOFFERACTION_ERROR\r\n
0xd000011b | RIL_CALLMEDIAOFFERACTION_REJECT\r\n
0xd000011c | RIL_CALLMEDIAOFFERACTION_ASK\r\n
0xd000011d | RIL_CALLMEDIAOFFERACTION_ACCEPT\r\n
0xd000011e | RIL_CALLMEDIAOFFERACTION_CANCEL\r\n
0xd000011f | None\r\n
0xd0000120 | CircuitSwitched\r\n
0xd0000121 | PacketSwitched\r\n
0xd0000122 | PH_LINESYSTEMTYPE_GSM\r\n
0xd0000123 | PH_LINESYSTEMTYPE_CDMA\r\n
0xd0000124 | PH_LINESYSTEMTYPE_VOIP\r\n
0xd0000125 | PH_LINESYSTEMTYPE_UNKNOWN\r\n
0xd0000126 | PH_LINESYSTEMTYPE_IMS\r\n
0xd0000127 | CellularAudioType_None\r\n
0xd0000128 | CellularAudioType_CircuitSwitched\r\n
0xd0000129 | CellularAudioType_PacketSwitched\r\n
0xd000012a | CellularAudioType_PacketSwitched_WiFi\r\n
0xd000012b | RIL_CALLHANDOVERPHASE_STARTED\r\n
0xd000012c | RIL_CALLHANDOVERPHASE_COMPLETED\r\n
0xd000012d | RIL_CALLHANDOVERPHASE_FAILED\r\n
0xd000012e | RIL_CALLHANDOVERPHASE_CANCELLED\r\n
0xd000012f | None\r\n
0xd0000130 | Pending\r\n
0xd0000131 | Connected\r\n
0xd0000132 | PhoneMediaQuality_Unknown\r\n
0xd0000133 | PhoneMediaQuality_Low\r\n
0xd0000134 | PhoneMediaQuality_Standard\r\n
0xd0000135 | PhoneMediaQuality_High\r\n
0xd0000136 | PhoneMediaQuality_AMR_NB\r\n
0xd0000137 | PhoneMediaQuality_AMR_WB\r\n
0xd0000138 | PhoneMediaQuality_EVRC\r\n
0xd0000139 | PhoneMediaQuality_EVRC_B\r\n
0xd000013a | PhoneMediaQuality_EVRC_NW\r\n
0xd000013b | PhoneMediaQuality_EVRC_WB\r\n
0xd000013c | PhoneMediaQuality_EVS_FB\r\n
0xd000013d | PhoneMediaQuality_EVS_NB\r\n
0xd000013e | PhoneMediaQuality_EVS_SWB\r\n
0xd000013f | PhoneMediaQuality_EVS_WB\r\n
0xd0000140 | PhoneMediaQuality_GSM_EFR\r\n
0xd0000141 | PhoneMediaQuality_GSM_FR\r\n
0xd0000142 | PhoneMediaQuality_GSM_HR\r\n
0xd0000143 | PhoneMediaQuality_QCELP13K\r\n
0xd0000144 | PhoneMediaQuality_G711U\r\n
0xd0000145 | PhoneMediaQuality_G711A\r\n
0xd0000146 | PhoneMediaQuality_G722\r\n
0xd0000147 | PhoneMediaQuality_G723\r\n
0xd0000148 | PhoneMediaQuality_G729\r\n
0xd0000149 | RIL_IMSFAILUREMESSAGETYPE_REGISTER\r\n
0xd000014a | RIL_IMSFAILUREMESSAGETYPE_SUBSCRIBE\r\n
0xd000014b | RIL_IMSFAILUREMESSAGETYPE_INCALL\r\n
0xd000014c | RIL_PSMPREF_UNKNOWN\r\n
0xd000014d | RIL_PSMPREF_WIFIONLY\r\n
0xd000014e | RIL_PSMPREF_WIFIPREFERRED\r\n
0xd000014f | RIL_PSMPREF_CELLONLY\r\n
0xd0000150 | RIL_PSMPREF_CELLPREFERRED\r\n
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
0xf000001a | CallVerb_ExplicitCallTransfer\r\n
0xf000001b | Dial\r\n
0xf000001c | End\r\n
0xf000001d | DropActiveAcceptHeld\r\n
0xf000001e | Hold\r\n
0xf000001f | Unhold\r\n
0xf0000020 | Swap\r\n
0xf0000021 | Private\r\n
0xf0000022 | Conference\r\n
0xf0000023 | Flash\r\n
0xf0000024 | RejectIncoming\r\n
0xf0000025 | AcceptIncoming\r\n
0xf0000026 | SendDtmf\r\n
0xf0000027 | StartDtmf\r\n
0xf0000028 | StopDtmf\r\n
0xf0000029 | DropFromConference\r\n
0xf000002a | DisableLocalVideo\r\n
0xf000002b | EnableLocalVideo\r\n
0xf000002c | AddVideo\r\n
0xf000002d | DropVideo\r\n
0xf000002e | AcceptIncomingVideo\r\n
0xf000002f | RejectIncomingVideo\r\n
0xf0000030 | SetVideoPaused\r\n
0xf0000031 | StartRecording\r\n
0xf0000032 | PauseRecording\r\n
0xf0000033 | StopRecording\r\n
0xf0000034 | ExplicitCallTransfer\r\n
0xf0000035 | RIL_PARAM_CI_EXECUTOR\r\n
0xf0000036 | RIL_PARAM_CI_ID\r\n
0xf0000037 | RIL_PARAM_CI_DIRECTION\r\n
0xf0000038 | RIL_PARAM_CI_STATUS\r\n
0xf0000039 | RIL_PARAM_CI_TYPE\r\n
0xf000003a | RIL_PARAM_CI_MULTIPARTY\r\n
0xf000003b | RIL_PARAM_CI_ADDRESS\r\n
0xf000003c | RIL_PARAM_CI_SUBADDRESS\r\n
0xf000003d | RIL_PARAM_CI_DESCRIPTION\r\n
0xf000003e | RIL_PARAM_CI_NUM_PRES_IND\r\n
0xf000003f | RIL_PARAM_CI_NAME_PRES_IND\r\n
0xf0000040 | RIL_PARAM_CI_FLAGS\r\n
0xf0000041 | RIL_PARAM_CI_DISCONNECTINITIATOR\r\n
0xf0000042 | RIL_PARAM_CI_DISCONNECTREASON\r\n
0xf0000043 | RIL_PARAM_CI_DISCONNECTDETAILS\r\n
0xf0000044 | RIL_PARAM_CI_OFFERANSWER\r\n
0xf0000045 | RIL_PARAM_CI_HANDOVERSTATE\r\n
0xf0000046 | RIL_PARAM_RPI_EXECUTOR\r\n
0xf0000047 | RIL_PARAM_RPI_ADDRESS\r\n
0xf0000048 | RIL_PARAM_RPI_SUBADDRESS\r\n
0xf0000049 | RIL_PARAM_RPI_DESCRIPTION\r\n
0xf000004a | RIL_PARAM_RPI_NUM_PRES_IND\r\n
0xf000004b | RIL_PARAM_RPI_NAME_PRES_IND\r\n
0xf000004c | RIL_PARAM_RPI_ID\r\n
0xf000004d | RIL_PARAM_ON_LONGNAME\r\n
0xf000004e | RIL_PARAM_ON_SHORTNAME\r\n
0xf000004f | RIL_PARAM_ON_NUMNAME\r\n
0xf0000050 | RIL_PARAM_ON_COUNTRY_CODE\r\n
0xf0000051 | RIL_PARAM_ON_SYSTEMTYPE\r\n
0xf0000052 | RIL_PARAM_NETWORKCODE_EXECUTOR\r\n
0xf0000053 | RIL_PARAM_NETWORKCODE_MCC\r\n
0xf0000054 | RIL_PARAM_NETWORKCODE_MNC\r\n
0xf0000055 | RIL_PARAM_NETWORKCODE_SID\r\n
0xf0000056 | RIL_PARAM_NETWORKCODE_NID\r\n
0xf0000057 | RIL_PARAM_NETWORKCODE_RI\r\n
0xf0000058 | RILCALLINFO_FLAG_ALIENCALL\r\n
0xf0000059 | RILCALLINFO_FLAG_EMERGENCYCALL\r\n
0xf000005a | RIL_PARAM_DISPLAY_EXECUTOR\r\n
0xf000005b | RIL_PARAM_DISPLAY_TYPE\r\n
0xf000005c | RIL_PARAM_DISPLAY_TAG\r\n
0xf000005d | RIL_PARAM_DISPLAY_MESSAGESIZE\r\n
0xf000005e | RIL_PARAM_DISPLAY_MESSAGE\r\n
0xf000005f | RIL_SYSTEMTYPE_1XRTT\r\n
0xf0000060 | RIL_SYSTEMTYPE_EVDO\r\n
0xf0000061 | RIL_SYSTEMTYPE_GSM\r\n
0xf0000062 | RIL_SYSTEMTYPE_UMTS\r\n
0xf0000063 | RIL_SYSTEMTYPE_LTE\r\n
0xf0000064 | RIL_SYSTEMTYPE_TDSCDMA\r\n
0xf0000065 | VoipIpcCallAttributes_VoiceOnly\r\n
0xf0000066 | VoipIpcCallAttributes_Video\r\n
0xf0000067 | RIL_PARAM_TONESIGNAL_GPPTONE\r\n
0xf0000068 | RIL_PARAM_TONESIGNAL_GPPTONE2\r\n
0xf0000069 | RIL_PARAM_TONESIGNAL_GPP2ISDNALERTING\r\n
0xf000006a | RIL_PARAM_TONESIGNAL_EXECUTOR\r\n
0xf000006b | RIL_PERSOFEATURE_NONE\r\n
0xf000006c | RIL_PERSOFEATURE_3GPP_NET\r\n
0xf000006d | RIL_PERSOFEATURE_3GPP_NETSUB\r\n
0xf000006e | RIL_PERSOFEATURE_3GPP_SP\r\n
0xf000006f | RIL_PERSOFEATURE_3GPP_CORP\r\n
0xf0000070 | RIL_PERSOFEATURE_3GPP_USIM\r\n
0xf0000071 | RIL_PERSOFEATURE_3GPP2_NETTYPE1\r\n
0xf0000072 | RIL_PERSOFEATURE_3GPP2_NETTYPE2\r\n
0xf0000073 | RIL_PERSOFEATURE_3GPP2_HRPD\r\n
0xf0000074 | RIL_PERSOFEATURE_3GPP2_SP\r\n
0xf0000075 | RIL_PERSOFEATURE_3GPP2_CORP\r\n
0xf0000076 | RIL_PERSOFEATURE_3GPP2_UIM\r\n
0xf0000077 | RIL_PARAM_PDS_STATE\r\n
0xf0000078 | RIL_PARAM_PDS_CK_ATTEMPTS\r\n
0xf0000079 | RIL_PARAM_PDS_PUK_ATTEMPTS\r\n
0xf000007a | RIL_PARAM_SI_ADDRESS\r\n
0xf000007b | RIL_PARAM_SI_DESCRIPTION\r\n
0xf000007c | RIL_PARAM_SI_SERVICE\r\n
0xf000007d | RIL_PARAM_IMSSTATUS_EXECUTOR\r\n
0xf000007e | RIL_PARAM_IMSSTATUS_HUICCAPP\r\n
0xf000007f | RIL_PARAM_IMSSTATUS_AVAILABLESERVICES\r\n
0xf0000080 | RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT\r\n
0xf0000081 | RIL_PARAM_IMSSTATUS_SERVINGDOMAIN\r\n
0xf0000082 | RIL_PARAM_IMSSTATUS_SYSTEMTYPE\r\n
0xf0000083 | RIL_IMS_SERVICE_SMS\r\n
0xf0000084 | RIL_IMS_SERVICE_VOICE\r\n
0xf0000085 | RIL_IMS_SERVICE_VIDEO\r\n
0xf0000086 | RIL_IMS_SERVICE_CUSTOM\r\n
0xf0000087 | RIL_IMS_SERVICE_SUPSVC\r\n
0xf0000088 | RIL_IMS_SERVICE_RCS\r\n
0xf0000089 | RIL_IMS_SERVICE_USSD\r\n
0xf000008a | RIL_IMS_SERVICE_E_VOICE\r\n
0xf000008b | RIL_PARAM_CMOA_ID\r\n
0xf000008c | RIL_PARAM_CMOA_CHANGE\r\n
0xf000008d | RIL_PARAM_CMOA_ACTION\r\n
0xf000008e | RIL_PARAM_CMOA_OLD_STATE\r\n
0xf000008f | RIL_PARAM_CMOA_NEW_STATE\r\n
0xf0000090 | RIL_PARAM_CALLVIDEO_PEERCAPABILITIES\r\n
0xf0000091 | RIL_PARAM_CALLVIDEO_FLAGS\r\n
0xf0000092 | RIL_CALLMEDIAVIDEOFLAG_CAPABILITY_UNKNOWN\r\n
0xf0000093 | RIL_CALLMEDIAVIDEOFLAG_PAUSE\r\n
0xf0000094 | RIL_PARAM_HANDOVER_PHASE\r\n
0xf0000095 | RIL_PARAM_HANDOVER_OLD_TYPE\r\n
0xf0000096 | RIL_PARAM_HANDOVER_NEW_TYPE\r\n
0xf0000097 | RIL_PARAM_HANDOVER_3GPPCAUSE\r\n
0xf0000098 | RIL_UICCLOCKSTATE_VERIFIED\r\n
0xf0000099 | RIL_UICCLOCKSTATE_ENABLED\r\n
0xf000009a | RIL_UICCLOCKSTATE_BLOCKED\r\n
0xf000009b | RIL_PARAM_UICCLOCKSTATE_UICCLOCK\r\n
0xf000009c | RIL_PARAM_UICCLOCKSTATE_LOCKSTATE\r\n
0xf000009d | RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT\r\n
0xf000009e | RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT\r\n
0xf000009f | RIL_PARAM_UAPCS_HUICCAPP\r\n
0xf00000a0 | RIL_PARAM_UAPCS_PERSOFEATURE\r\n
0xf00000a1 | RIL_PARAM_UAPCS_PERSOCHECKSTATE\r\n

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
0xb0000064 | Enqueued verb %1, callid %2 (completion context %3)\r\n
0xb0000065 | Enqueued verb %1, callids %2, %3 (completion context %4)\r\n
0xb0000066 | Enqueued verb Dial, callid %1, callType %2, calleridoption %3 (completion context %4)\r\n
0xb0000067 | Dequeued verb %1, callid %2 (completion context %3)\r\n
0xb0000068 | Dequeued verb %1, callids %2, %3 (completion context %4)\r\n
0xb0000069 | Dequeued verb Dial, callid %1, callType %2, calleridoption %3 (completion context %4)\r\n
0xb000006a | Verb completed with HRESULT %1; host notified (completion context %2)\r\n
0xb000006b | Verb completed with HRESULT %1; host not notified (completion context %2)\r\n
0xb000006c | Began tracking async CellVoice request id %1 (for completion context %2)\r\n
0xb000006d | Stopped tracking async CellVoice request id %1 (for completion context %2)\r\n
0xb000006e | Enqueued async CellVoice request id %1 completion with HRESULT %2\r\n
0xb000006f | Gsm call manager called I3GPPCallModel::%1 with async request id %2 for callid %3 (cellvoice callid %4)\r\n
0xb0000070 | Gsm call manager called I3GPPCallModel::%1 with async request id %2 for callids %3, %4\r\n
0xb0000071 | Gsm call manager called I3GPPCallModel::RequestOutgoingCall with async request id %1 for callid %2, callType %3 (no cellvoice callid)\r\n
0xb0000072 | CallManager got call progress update for cellvoiceId %1; status %2; direction %3; number %4; name %5; party %6; flags %7; type %8; valid params %9; \r\n
0xb0000073 | CellVoice returned failure %1 to get subscriber number\r\n
0xb0000074 | CellVoice returned failure %1 to get voicemail number\r\n
0xb0000075 | CellVoice get IMSI completed with error %1\r\n
0xb0000076 | Resetting VVM state; old MCC/MNC/nameDiff %1 %2 %3\r\n
0xb0000077 | Used RIL system type %1; got signal strength %2\r\n
0xb0000078 | Used RIL system type %1; voice domain %2; got registration status %3\r\n
0xb000007a | No Visual Voicemail provider was loaded for MCC,MNC %1,%2\r\n
0xb000007b | Visual Voicemail action %1 is not currently available on this line\r\n
0xb000007c | Legacy Voicemail message received: %1. Message count: %2\r\n
0xb000007d | Registered to operator: params %1; long name "%2"; short name "%3"; numeric name"%4"; country code "%5"\r\n
0xb000007e | Switched to data registration to get registration info\r\n
0xb000007f | Status %1 from cellcore reading voicemail count %2 from SIM\r\n
0xb0000080 | Status %1 from cellcore writing voicemail count %2 to SIM\r\n
0xb0000083 | [CellularAudio] Muting cellular audio\r\n
0xb0000084 | [CellularAudio] Unmuting cellular audio\r\n
0xb0000085 | CallManager got disconnect notification for cellvoiceId %1; initiator %2; reason %3; group %4; gppdetails [ location %5 cause %6 ]\r\n
0xb0000086 | CallModel3GPP2 invoking %1; callid %2; asyncRequestId %3\r\n
0xb0000087 | CdmaHeuristics invoking %1; callid %2 and %3; asyncRequestId %3; completionContext %4\r\n
0xb000008b | Call manager got call waiting notification for cellvoice callid %1: rilremotepartyinfo: params %2 numberpres %3 namepres %4\r\n
0xb000008c | Call manager got dial id notification for cellvoice callid %1: params %2 numberpres %3 namepres %4\r\n
0xb000008d | CdmaHeuristics started tracking verb %1 asyncRequestId %2 for completionContext %3\r\n
0xb000008e | CdmaHeuristics stopped tracking verb %1 asyncRequestId %2 for completionContext %3\r\n
0xb000008f | Status %1 from cellcore reading call forwarding status %2 from SIM\r\n
0xb0000090 | Status %1 from cellcore reading call forwarding number from SIM\r\n
0xb0000091 | Status %1 from cellcore writing call forwarding status to SIM\r\n
0xb0000092 | Status %1 from cellcore writing call forwarding number to SIM\r\n
0xb0000093 | Sim LockState changed to: %1\r\n
0xb0000094 | Cellvoice UICC Line set; sim swap pending: %1; old/new line ID: %2 / %3\r\n
0xb0000095 | Finished retrieving home MCC/MNC: %1 %2\r\n
0xb0000096 | Set visual voicemail provisioning state to %1\r\n
0xb0000097 | Forced SIM swap based on MCC/MNC: %1 %2 ==> %3 %4\r\n
0xb0000098 | Modem power state changed to %1\r\n
0xb0000099 | Network codes: params %1; MCC %2; MNC %3\r\n
0xb000009a | SIMOM gave LineFactory a duplicate modem (ignored)\r\n
0xb000009b | SIMOM gave LineFactory an unknown modem to remove (ignored)\r\n
0xb000009c | SIMOM gave LineFactory an unknown modem for adding a slot (ignored)\r\n
0xb000009d | SIMOM gave LoneFactory a duplicate slot (ignored)\r\n
0xb000009e | SIMOM gave LineFactory an unknown modem for removing a slot (ignored)\r\n
0xb000009f | SIMOM gave LineFactory an unknown slot to remove (ignored)\r\n
0xb00000a0 | Line not created: modem index %1 or slot index %2 out of bounds (from ISlot %3)\r\n
0xb00000a1 | CallManager new incoming call from %1\r\n
0xb00000a2 | Call forwarding state updated. SupSvcCode: %1; Enable: %2; new m_callForwardingState: %3\r\n
0xb00000a3 | Read call forwarding state from registry. m_callForwardingState: %1; m_callForwardingAddress: %2\r\n
0xb00000a4 | OnSupServiceCallback. ExecutionResult: %1; SvcCode: %2; DialAction: %3\r\n
0xb00000a5 | Legacy Voicemail message ignored due to config setting\r\n
0xb00000a6 | CdmaHeuristics set local hold to %1\r\n
0xb00000a7 | Detected SGLTE config with no GSM RF; using synthesized no-registration status\r\n
0xb00000a8 | Enqueued verb AcceptIncoming, callid %1, callType %2 (completion context %3)\r\n
0xb00000a9 | Dequeued verb AcceptIncoming, callid %1, callType %2 (completion context %3)\r\n
0xb00000aa | Gsm call manager called I3GPPCallModel::AcceptIncomingCall with async request id %1 for callid %2, callType %3 (cellvoice callid %4)\r\n
0xb00000ab | Received an IMS SIP disconnect cause: error-code=%1, reason=%2\r\n
0xb00000ac | Assumed error is XCAP related and enabling show/hide caller id feature\r\n
0xb00000ad | [Voicemail] Timer task for Visual Voicemail configuration changes fired.\r\n
0xb00000ae | [Voicemail] Attempting to queue action for Visual Voicemail configuration changes [isChangePending=%1]\r\n
0xb00000af | [Voicemail] Got notified of Visual Voicemail registry changes\r\n
0xb00000b0 | [Voicemail] Configure Visual Voicemail [homeMcc=%1][homeMnc=%2][dataAffinityExists=%3]\r\n
0xb00000b1 | Can Data affinity change [LineId=%1][dataAffinityCanIndex=%2]\r\n
0xb00000ca | Terminating Active Call Agent %1 due to timeout waiting for Notify callback\r\n
0xb00000cb | Cell Broadcast Listener received message %1\r\n
0xb00000cc | Display text changed: params %1, info type %2, info tag %3, message size %4\r\n
0xb00000cd | Calling IVoIPTaskManagerClient->LaunchActiveCallAgent(%1)\r\n
0xb00000ce | Calling IVoIPTaskManagerClient->CancelActiveCallAgentInstance(%1)\r\n
0xb00000cf | _CancelActiveCallAgent for product id: %1; isForcedShutdown: %2; isActiveCallAgentRunning: %3\r\n
0xb00000d0 | Calling IVoIPTaskManagerClient->HoldActiveCall(%1)\r\n
0xb00000d1 | Calling IVoIPTaskManagerClient->UnholdActiveCall(%1)\r\n
0xb00000d2 | Calling IVoIPTaskManagerClient->OnIncomingCallDialogDisplayed(%1)\r\n
0xb00000d3 | Calling IVoIPTaskManagerClient->OnIncomingCallDialogDismissed(%1)\r\n
0xb00000d4 | InitializedConnectionToAppHost called on VoipProvider. RPC Handle: %1; VoipLine: %2; AgentProcessId: %3; ContextId: %4\r\n
0xb00000d5 | LineFactory->NewIncomingCall(%1, %2)\r\n
0xb00000d6 | LineFactory->NewOutgoingCall(%1, %2)\r\n
0xb00000d7 | LineFactory->CallActive(%1, %2)\r\n
0xb00000d8 | LineFactory->CallHeld(%1, %2)\r\n
0xb00000d9 | LineFactory->CallEnded(%1, %2)\r\n
0xb00000da | LineFactory->SetAudioRouting(%1, %2)\r\n
0xb00000db | LineFactory->GetAudioRouting(%1)\r\n
0xb00000dc | LineFactory->SetMuteState(%1, %2)\r\n
0xb00000dd | LineFactory->UpdateCallContactName(%1, %2)\r\n
0xb00000de | LineFactory->UpdateCallStartTime(%1, %2)\r\n
0xb00000df | LineFactory->GetCallStartTime(%1, %2)\r\n
0xb00000e0 | LineFactory->UpdateCallAttributes(%1, %2, %3)\r\n
0xb00000e1 | VoipAppHostHandle_rundown(%1)\r\n
0xb00000e2 | _PendingRpcCallCompleted(%2, %3) for line: %1; onTime: %4\r\n
0xb00000e3 | Calling %1 on VoipApp for line: %2. Controller callId: %3; VoipApp CallId: %4\r\n
0xb00000e4 | Calling %1 on VoipApp for line: %2.\r\n
0xb00000e5 | Calling OnAudioRouteChanged on VoipApp for line: %1. AudioRoute: %2; Available Paths: %3\r\n
0xb00000e6 | Can %1 entered emergency mode %2\r\n
0xb00000e7 | Modem constraint violated: Illegal CPI %1\r\n
0xb00000e8 | Modem constraint violated: Async dial failure %1 for call in CPI state %2\r\n
0xb00000e9 | Modem constraint violated: Mismatched direction fields; direction %1, CPI state %2\r\n
0xb00000ea | CallManager invoked I3GPP[2]CallModel::%1; asyncRequestId %2\r\n
0xb00000eb | CallManager invoking I3GPP[2]CallModel::%1; asyncRequestId %2\r\n
0xb00000ec | CallModel3GPP2 invoking %1; callid %2 and %3; asyncRequestId %4)\r\n
0xb00000ed | CdmaHeuristics invoking %1; callid %2; asyncRequestId %3; completionContext %4\r\n
0xb00000ee | CdmaHeuristics verb completed: asyncRequestId %1; result %2; verb %3; callid %4; original completionContext %5\r\n
0xb00000ef | CdmaHeuristics verb completed: asyncRequestId %1; result %2\r\n
0xb00000f0 | CallModel3GPP2 verb completed: asyncRequestId %1; result %2; verb %3; callid %4; original completionContext %5\r\n
0xb00000f1 | Dequeued async CellVoice request id %1 completion with HRESULT %2\r\n
0xb00000f2 | CallModel processing call progress update with cellvoiceId %1 for callId %2\r\n
0xb00000f5 | CdmaHeuristics tracking with asyncRequestId %1 not found\r\n
0xb00000f9 | CallModel3GPP2 got unexpected call update for cellvoiceId %1; while having existing cellvoiceId %2\r\n
0xb00000fd | Processed request to clear Voicemail count.\r\n
0xb00000fe | Default voicemail number source is: %1\r\n
0xb00000ff | Modem constraint violated: Illegal 3GPP2 CallWaiting notification\r\n
0xb0000100 | Tone signal received: params %1, %2, %3, %4\r\n
0xb0000101 | LineNotificationWorkItem: instantiated #%1 (%2)\r\n
0xb0000102 | LineNofiticationWorkItem: processing #%1 (%2)\r\n
0xb0000103 | LineNofiticationWorkItem: finished processing #%1 (%2)\r\n
0xb0000104 | LineNofiticationWorkItem: canceled #%1 (%2)\r\n
0xb0000105 | Got subscriber numbers; dwNumSubscribers = %1\r\n
0xb0000106 | Subscriber number entry #%1: params #2, service #3\r\n
0xb0000107 | Subscriber number is missing or empty\r\n
0xb0000108 | Got IMS status change notification. [Params=%1][AvailableServices=%2]\r\n
0xb0000109 | [CallModel3GPP] Call model changing between GSM and IMS, [ims=%1][m_imsOnWiFi=%2]\r\n
0xb000010a | Roaming override number used.  Dialing %1.\r\n
0xb000010b | HandleUICCPersoCheckStatusChange, [dwParams=%1][dwPersoFeature=%2][dwPersoCheckState=%3]\r\n
0xb000010c | Get Perso deactivation state for %1 completed with hr %2; params %3; state %4; unlock remaining %5; unblock remaining %6\r\n
0xb000010d | Deactivate Perso for %1 completed with hr %2; params %3; state %4; unlock remaining %5; unblock remaining %6; async API context %7\r\n
0xb000010e | Initiating SIM PIN operation %1; async completion context = %2\r\n
0xb000010f | Initiating Perso unlock for %1; async completion context = %2\r\n
0xb0000110 | SIM PIN operation '%1' with async completion context %2 complete, result % = 3\r\n
0xb0000111 | 3GPP2CallModel ignored alien call (CellVoice ID %1) due to existing call (CellVoice ID %2).\r\n
0xb0000112 | 3GPPCallModel suppressed call update due to invalid state.\r\n
0xb0000113 | Unsolicited supservice %1 received for CellVoice callid %2\r\n
0xb0000114 | CellVoice Response Received in Method: %1. Async Hresult: %2\r\n
0xb0000115 | dwParams %1; dwNetworkSSErrorCause %2; dwNetworkCCErrorCause %3; dwVendorErrorCause %4\r\n
0xb0000116 | CellVoice reported infoClasses: %1.\r\n
0xb0000117 | CellVoice reported hide ID settings: params %1, status %2, provisioning %3.\r\n
0xb0000118 | CellVoice reported call forwarding settings: params %1, info class %2, delay time %3, status %4.\r\n
0xb0000119 | CellVoice Ussd Data Status: %1.\r\n
0xb000011a | Ussd Session terminated\r\n
0xb000011b | New Ussd Session initiated\r\n
0xb000011c | Invalid Callforwarding delay time parameter: %1. Using default value instead.\r\n
0xb000011d | Using default value for call forwarding delay time\r\n
0xb000011e | CellVoice reported COLR settings: params %1, status %2, provisioning %3.\r\n
0xb000011f | CellVoice reported CLIP settings: params %1, status %2, provisioning %3.\r\n
0xb0000120 | Executing sup service code %1, action %2\r\n
0xb0000121 | Ussd User response truncated\r\n
0xb0000122 | CellVoice reported COLP settings: params %1, status %2, provisioning %3.\r\n
0xb0000123 | Address for unsolicited supservice %1 is %2\r\n
0xb0000124 | Calling %1 on VoipApp for line: %2. VoipApp CallId: %3\r\n
0xb0000127 | RemoteId Request Complete: CallId: %1 RemoteId Exists: %2\r\n
0xb0000128 | Launching Voip app with URI: %1\r\n
0xb0000129 | LineFactory->NewIncomingUpgradeCall(%1, %2)\r\n
0xb000012a | LineFactory->NewOutgoingUpgradeCall(%1, %2). CallUpgradeGuid: %3\r\n
0xb000012b | LineFactory->CallReady(%1, %2)\r\n
0xb000012c | 3GPPCallModel suppressed call update due to ECall Failover.\r\n
0xb000012d | Dialing an Emergency call. PhoneCallId: %1.\r\n
0xb000012e | 3GPPCallModel got surprise outgoing Emergency call notification. Existing ECallId: %1, IgnoreNotification: %2.\r\n
0xb000012f | Modem Radio Config changed to %1\r\n
0xb0000130 | Setting Can Focus for Can: %1\r\n
0xb0000131 | Set Can Focus result: %1\r\n
0xb0000132 | Disconnecting dialed call with callId: %1 for incoming call.\r\n
0xb0000133 | LineFactory->GetNextOperation(%1)\r\n
0xb0000134 | Terminating Call Query Agent %1 due to timeout waiting for Notify callback\r\n
0xb0000135 | lineFactory->VoipAppOperationComplete(%1). Completed operationId: %2. Succeeded: %3. Call upgrade support: %4\r\n
0xb0000136 | Calling IVoIPTaskManagerClient->LaunchCallQueryAgent(%1)\r\n
0xb0000137 | Calling IVoIPTaskManagerClient->CancelCallQueryAgentInstance(%1)\r\n
0xb0000138 | Received async dial completion. CallId: %1, CellVoice CallId: %2\r\n
0xb0000139 | 3GPP2CallModel ignored disconnected call (CellVoice ID %1) due to existing call (CellVoice ID %2).\r\n
0xb000013a | Detected LTE System Type with no network registration and no voice domain.\r\n
0xb000013b | CallManager invoked I3GPP[2]CallModel::%1; asyncRequestId %2, Dialed Number: %3\r\n
0xb000013c | Update to call type or video context.  CallId: %1, CallType: %2, Video Context: %3\r\n
0xb000013d | CallModel3GPP2 CallVerb_SetVideoPaused; CallId: %1; paused: %2; completion context: %3\r\n
0xb000013e | CallModel3GPP CallVerb_SetVideoPaused; CallId: %1; paused: %2; async id: %3\r\n
0xb000013f | Enqueued verb SetVideoPaused, callid %1, paused %2, (completion context %3)\r\n
0xb0000140 | Dequeued verb SetVideoPaused, callid %1, paused %2, (completion context %3)\r\n
0xb0000141 | Video state update.  Params: %1, Action: %2, Direction: %3, State Params: %4, Peer caps: %5, Flags: %6, ContextID: %7\r\n
0xb0000142 | Calling Cellular API in media update for %1.  Async request id: %2, CallId %3, CellVoice CallId: %4)\r\n
0xb0000143 | Requesting video state publish.  Subscriber Number: %1, videoCapable: %2\r\n
0xb0000144 | Line type changed but SupService was not reset.\r\n
0xb0000145 | Registration state according to voice domain, voice domain: %1, registration status: %2, mapped registration state: %3\r\n
0xb0000146 | SubscriptionUpdate OMADM initiated : %1 HR = %2\r\n
0xb0000147 | Video direction override during multitasking, new transmit state: %1\r\n
0xb0000148 | CellularLine SetVideoCallingSetting: [CurrentState=%1][RequestType=%2][CacheSetting=%3][PerSimConfigAvailable=%4][TargetState=%5]\r\n
0xb0000149 | IMS system-type changing from %1 to %2\r\n
0xb000014a | Video media offer answer. Params: %1, Action: %2, Direction: %3, State Params: %4, Peer caps: %5, Flags: %6, ContextID: %7\r\n
0xb000014b | LineFactory->EndUpgradeOriginationCall(%1)\r\n
0xb000014c | LineFactory->CancelUpgrade(%1)\r\n
0xb000014d | ImsHandoverAttempt notify arrives. hrHandOverResult: %1, OldSystemType: %2, NewSystemType: %3\r\n
0xb000014e | GetVideoCapabilitySharingSettings: Queried, [LineId=%1][PerSimConfigAvaiable=%2][IsCapabilitySharingEnabled=%3][LastModifiedTimestamp=%4]\r\n
0xb000014f | SetVideoCapabilitySharingSettings: Updating, [LineId=%1][PerSimConfigAvaiable=%2][IsCapabilitySharingEnabled=%3][CurrentTimestamp=%4]\r\n
0xb0000150 | Applying video calling setting to saved or default user preference.\r\n
0xb0000151 | Unable to determine cached video calling setting.\r\n
0xb0000152 | Updated home MCC value from SIM in line specific data, [LineId=%1][HomeMcc=%2].\r\n
0xb0000153 | CallRecording: Phone service was notified of a Call Recording application whose Package Family Name is too long: '%1'\r\n
0xb0000155 | IMS service voice changed, [imsVoiceAvailable=%1][imsVideoAvailable=%2][videoCallingEnabled=%3]\r\n
0xb0000156 | IMS service video changed, [imsVoiceAvailable=%1][imsVideoAvailable=%2][videoCallingEnabled=%3]\r\n
0xb0000157 | DeterminePhoneSystemType, [imsVoiceSupported=%1][registration0SystemType=%2][registration0VoiceDomain=%3][callPresence=%4]\r\n
0xb0000158 | UpdateLineSystemType, [currentLineSystemType=%1][newLineSystemType=%2]\r\n
0xb0000159 | SetRadioAccessTechnology, [radioAccessTechnology=%1][toIms=%2][toGsm=%3][toCdma=%4][fromIms=%5][fromGsm=%6][fromCdma=%7]\r\n
0xb000015a | SetRadioAccessTechnology, switching call model, [To3GPP=%1]\r\n
0xb000015b | UpdateCallPresence, [currentPresence=%1][aggregatePresence=%2][allSameType=%3]\r\n
0xb000015c | [CallModel3GPP] Updating audio, [audioType=%1][audioActive=%2][anyCallNeedsAudio=%3][anyCallNeedsAudioActive=%4][localHoldSupported=%5]\r\n
0xb000015d | [CallModel3GPP2] Updating audio, [audioType=%1][shouldEnableAudio=%2][audioAllowed=%3]\r\n
0xb000015e | [CellularAudio] Updating audio for handover notification, [inProgress=%1][isHandoverNotification=%2][phase=%3][oldType=%4][newType=%5]\r\n
0xb000015f | ProcessHandoverNotification, [callInfoParams=%1][phase=%2][handoverStateParams=%3][oldType=%4][newType=%5][inProgress=%6]\r\n
0xb0000160 | Reset handover state\r\n
0xb0000161 | Updated video call conference state, [CallId=%1][CellVoiceCallId=%2][ContextId=%3][ConferenceContextId=%4][PreviousState=%5][UpdatedState=%6].\r\n
0xb0000162 | Interpret E_SUPSVCS_INVALIDREMOTEURI as success with call forwarding status disabled.\r\n
0xb0000163 | IR94FeatureDisabled: Disable video calling.\r\n
0xb0000164 | IR94FeatureDisabled: Force disable video calling.\r\n
0xb0000165 | Emergency call failed over. ECallId: %1.\r\n
0xb0000166 | Emergency call DisableAndEnable Audio from 3GPP CallModel. ECallId: %1.\r\n
0xb0000167 | Emergency call DisableAndEnable Audio from 3GPP2 CallModel. ECallId: %1.\r\n
0xb0000168 | HandleUICCPinLockStateChange, [dwParams=%1][dwLockState=%2]\r\n
0xb0000169 | Updating UICC related information from SIM\r\n
0xb000016a | OnSubscriberNumbersChange, [result=%1]\r\n
0xb000016b | [CallModel3GPP] Notified for IMS on Wifi flag, [m_imsOnWiFi=%1][onWiFi=%2]\r\n
0xb000016c | Removed stale pending RPC for line: %1, callid: %2, type: %3\r\n
0xb000016d | Timedout pending RPC for line: %1, callid: %2, type: %3\r\n
0xb000016e | ResetConnectionToApp for line: %1\r\n
0xb000016f | CleanupVoipAppConnectionState for line: %1, pendingRPCCalls: %2, voipAppProcessId: %3\r\n
0xb0000170 | VoIP Line Id: %1 has AboveLock extension: %2\r\n
0xb0000171 | Enqueued verb %1, (completion context %2)\r\n
0xb0000172 | Dequeued verb %1, (completion context %2)\r\n
0xb0000173 | CellularCallModel initiating explicit call transfer; asyncRequestId %1\r\n
0xb0000174 | Ril audio codec %1 mapped to %2 for CallId: %3.\r\n
0xb0000175 | [Voicemail] Stop VVM Invoked [stopReason=%1]\r\n
0xb0000176 | [Voicemail] Start VVM Invoked [last stopReason=%1]\r\n
0xb0000177 | LineFactory->ReserveVoipCallResources(%1, %3, %2) Completed.\r\n
0xb0000178 | LineFactory->CancelVoipCallResourceReservation(%1) Completed.\r\n
0xb0000179 | [VoipLine#%1] Calling LaunchVoipRtcTask(%3, %4, %2)\r\n
0xb000017a | [VoipLine#%1] Calling CancelVoipRtcTask(%2)\r\n
0xb000017b | [VoipLine#%1] Calling NotifyVoipActivityCompleted(%2)\r\n
0xb000017c | CallerId Prefix updated.  Updated number is %1.\r\n
0xb000041b | Received IMS Failure changed, [imsFailureMessageType=%1].\r\n
0xb000041c | Ims failure error string is missing or empty.\r\n
0xb000041d | WiFi call disconnect occured, [errorMessage=%1] .\r\n
0xb000041e | WiFi internet connection status: %1.\r\n
0xb000041f | WiFi calling feature enabled: %1.\r\n
0xb0000420 | WiFi calling upsell suppressed: %1.\r\n
0xb0000421 | Media Configuration Data, Set Index: %1, IMS Service Type: %2, Media Preference: %3.\r\n
0xb0000422 | Placing request for switching cellular audio provider, Executor Index: %1, Old Audio type: %2, New Audio Type: %3.\r\n
0xb0000423 | [SupSvcsManager] Received MWI summary change notification [dwExecutor=%1][dwParams=%2][dwReferenceNumber=%3][dwTotalNumberOfDetailItems=%4][dwNumberOfSummaryItems=%5]\r\n
0xb0000424 | [SupSvcsManager] Received MWI details change notification [dwExecutor=%1][dwParams=%2][dwReferenceNumber=%3][dwNumberOfDetailItems=%4]\r\n
0xb0000425 | [SupSvcsManager] Handling MWI summary change notification [dwMwiType=%1][dwNumberOfNewMessages=%2][dwNumberOfOldMessages=%3][dwNumberOfNewUrgentMessages=%4][dwNumberOfOldUrgentMessages=%5]\r\n
0xb0000426 | [CellularLine] Received MWI summary change notification [dwReferenceNumber=%1][totalNewMessages=%2]\r\n
0xb0000427 | Ignore Caller ID Blocking Prefixes: %1\r\n
0xb0000428 | Caller ID blocking prefixes: %1\r\n
0xb0000429 | Ims Client added handler registered\r\n
0xb000042a | Ims Client added handler unregistered\r\n
0xb000042b | Ims client added: %1\r\n
0xb000042c | Ims Client removed handler registered\r\n
0xb000042d | Ims Client removed handler unregistered\r\n
0xb000042e | Ims client removed: %1\r\n
0xb000042f | Msti service new call handler registered\r\n
0xb0000430 | Msti service new call handler unregistered\r\n
0xb0000431 | MtsiNewCallHandler got new call notification for sipCallId %1; call status %2; direction %3; isConf %4\r\n
0xb0000432 | Msti call state changed handler registered\r\n
0xb0000433 | Msti call state changed handler unregistered\r\n
0xb0000434 | Ims service registered %1\r\n
0xb0000435 | Ims Line Dial outgoing call, callid %1, dial string %2\r\n
0xb0000436 | Ims Line AcceptIncoming, callid %1, (completion context %2)\r\n
0xb0000437 | Ims Line end the call, callid %1, (completion context %2)\r\n
0xb0000438 | Roaming override substitution performed for subscriber number. Roaming override = %1. Subscriber number = %2\r\n
0xb0000439 | Roaming override substitution not performed for subscriber number with international format. Roaming override = %1. Subscriber number = %2\r\n
0xb000043a | Received unsolicited notification, marking call as conference participant [CallId=%2][SupSvcCode=%1]\r\n
0xd0000001 | CallType_AudioOnly\r\n
0xd0000002 | CallType_AudioVideo\r\n
0xd0000003 | CallerIdOption_Default\r\n
0xd0000004 | CallerIdOption_ForceSend\r\n
0xd0000005 | CallerIdOption_ForceBlock\r\n
0xd0000006 | PH_CALLDIRECTION_INCOMING\r\n
0xd0000007 | PH_CALLDIRECTION_OUTGOING\r\n
0xd0000008 | PH_REGISTRATIONSTATE_UNKNOWN\r\n
0xd0000009 | PH_REGISTRATIONSTATE_UNREGISTERED_NO_SIGNAL\r\n
0xd000000a | PH_REGISTRATIONSTATE_UNREGISTERED_WITH_SIGNAL\r\n
0xd000000b | PH_REGISTRATIONSTATE_REGISTERING\r\n
0xd000000c | PH_REGISTRATIONSTATE_REGISTERING_AFTER_DENIED\r\n
0xd000000d | PH_REGISTRATIONSTATE_REGISTERED_HOME\r\n
0xd000000e | PH_REGISTRATIONSTATE_REGISTERED_ROAM\r\n
0xd000000f | PH_REGISTRATIONSTATE_DENIED\r\n
0xd0000010 | PH_REGISTRATIONSTATE_REGISTERED_ROAM_DOMESTIC\r\n
0xd0000011 | RIL_VOICE_DOMAIN_NONE\r\n
0xd0000012 | RIL_VOICE_DOMAIN_3GPP\r\n
0xd0000013 | RIL_VOICE_DOMAIN_3GPP2\r\n
0xd0000014 | RIL_VOICE_DOMAIN_IMS\r\n
0xd0000015 | RIL_CALLDIR_INCOMING\r\n
0xd0000016 | RIL_CALLDIR_OUTGOING\r\n
0xd0000017 | RIL_CPISTAT_UNKNOWN\r\n
0xd0000018 | RIL_CPISTAT_NEW_OUTGOING\r\n
0xd0000019 | RIL_CPISTAT_NEW_INCOMING\r\n
0xd000001a | RIL_CPISTAT_CONNECTED\r\n
0xd000001b | RIL_CPISTAT_DISCONNECTED\r\n
0xd000001c | RIL_CPISTAT_ONHOLD\r\n
0xd000001d | RIL_CPISTAT_MEDIA\r\n
0xd000001e | RIL_CPISTAT_HANDOVER\r\n
0xd000001f | RIL_CALL_SINGLEPARTY\r\n
0xd0000020 | RIL_CALL_MULTIPARTY\r\n
0xd0000021 | RIL_REMOTEPARTYINFO_VALID\r\n
0xd0000022 | RIL_REMOTEPARTYINFO_WITHHELD\r\n
0xd0000023 | RIL_REMOTEPARTYINFO_UNAVAILABLE\r\n
0xd0000024 | RIL_DISCINIT_UNKNOWN\r\n
0xd0000025 | RIL_DISCINIT_LOCAL\r\n
0xd0000026 | RIL_DISCINIT_REMOTE\r\n
0xd0000027 | RIL_DISCREASON_NULL\r\n
0xd0000028 | RIL_DISCREASON_BUSY\r\n
0xd0000029 | RIL_DISCREASON_NETWORKERROR\r\n
0xd000002a | RIL_DISCREASON_RADIOFADE\r\n
0xd000002b | RIL_DISCREASON_CONGESTION\r\n
0xd000002c | RIL_DISCREASON_EMERGENCYONLY\r\n
0xd000002d | RIL_DISCREASON_NOSERVICE\r\n
0xd000002e | RIL_DISCREASON_OTHEREXECUTORBUSY\r\n
0xd000002f | RIL_DISCREASON_EMERGENCYFAILOVER\r\n
0xd0000030 | RIL_DISCREASON_HANDOVER_MERGE\r\n
0xd0000031 | RIL_CALLTYPE_VOICE\r\n
0xd0000032 | RIL_CALLTYPE_DATA\r\n
0xd0000033 | RIL_CALLTYPE_FAX\r\n
0xd0000034 | RIL_CALLTYPE_PTT\r\n
0xd0000035 | RIL_CALLTYPE_VT\r\n
0xd0000036 | RIL_CALLTYPE_USSD\r\n
0xd0000037 | RIL_CALLTYPE_SUPSVC\r\n
0xd0000038 | RIL_CALLTYPE_IMS\r\n
0xd0000039 | RIL_CD_UNKNOWN_CAUSE\r\n
0xd000003a | RIL_CD_AS_CAUSE\r\n
0xd000003b | RIL_CD_3GPP_NETWORK_CAUSE\r\n
0xd000003c | RIL_CD_3GPP2_VENDOR_CAUSE\r\n
0xd000003d | RIL_CD_OTHER_CAUSE\r\n
0xd000003e | RIL_CD_3GPP_REJECT_CAUSE\r\n
0xd000003f | RIL_CD_IMS_SIP_CAUSE\r\n
0xd0000040 | RIL_EXTENDED_DISPLAY_TYPE_NORMAL\r\n
0xd0000041 | RIL_EXTENDED_DISPLAY_TAG_BLANK\r\n
0xd0000042 | RIL_EXTENDED_DISPLAY_TAG_SKIP\r\n
0xd0000043 | RIL_EXTENDED_DISPLAY_TAG_CONTINUATION\r\n
0xd0000044 | RIL_EXTENDED_DISPLAY_TAG_CALLED_ADDRESS\r\n
0xd0000045 | RIL_EXTENDED_DISPLAY_TAG_CAUSE\r\n
0xd0000046 | RIL_EXTENDED_DISPLAY_TAG_PROGRESS_INDICATOR\r\n
0xd0000047 | RIL_EXTENDED_DISPLAY_TAG_NOTIFICATION_INDICATOR\r\n
0xd0000048 | RIL_EXTENDED_DISPLAY_TAG_PROMPT\r\n
0xd0000049 | RIL_EXTENDED_DISPLAY_TAG_ACCUMULATED_DIGITS\r\n
0xd000004a | RIL_EXTENDED_DISPLAY_TAG_STATUS\r\n
0xd000004b | RIL_EXTENDED_DISPLAY_TAG_INBAND\r\n
0xd000004c | RIL_EXTENDED_DISPLAY_TAG_CALLING_ADDRESS\r\n
0xd000004d | RIL_EXTENDED_DISPLAY_TAG_REASON\r\n
0xd000004e | RIL_EXTENDED_DISPLAY_TAG_CALLING_PARTY_NAME\r\n
0xd000004f | RIL_EXTENDED_DISPLAY_TAG_CALLED_PARTY_NAME\r\n
0xd0000050 | RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NAME\r\n
0xd0000051 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NAME\r\n
0xd0000052 | RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NAME\r\n
0xd0000053 | RIL_EXTENDED_DISPLAY_TAG_ORIGINATING_RESTRICT\r\n
0xd0000054 | RIL_EXTENDED_DISPLAY_TAG_DATE_TIME_OF_DAY\r\n
0xd0000055 | RIL_EXTENDED_DISPLAY_TAG_CALL_APPEARANCE_ID\r\n
0xd0000056 | RIL_EXTENDED_DISPLAY_TAG_FEATURE_ADDRESS\r\n
0xd0000057 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NAME\r\n
0xd0000058 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NUMBER\r\n
0xd0000059 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NUMBER\r\n
0xd000005a | RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NUMBER\r\n
0xd000005b | RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NUMBER\r\n
0xd000005c | RIL_EXTENDED_DISPLAY_TAG_TEXT\r\n
0xd000005d | RIL_REGSTAT_UNKNOWN\r\n
0xd000005e | RIL_REGSTAT_UNREGISTERED\r\n
0xd000005f | RIL_REGSTAT_HOME\r\n
0xd0000060 | RIL_REGSTAT_ATTEMPTING\r\n
0xd0000061 | RIL_REGSTAT_DENIED\r\n
0xd0000062 | RIL_REGSTAT_ROAMING\r\n
0xd0000063 | RIL_REGSTAT_ROAMING_DOMESTIC\r\n
0xd0000064 | MODEM_POWER_OFF\r\n
0xd0000065 | MODEM_POWER_GOING_ON\r\n
0xd0000066 | MODEM_POWER_ON\r\n
0xd0000067 | MODEM_POWER_GOING_OFF\r\n
0xd0000068 | MODEM_POWER_SHUTTING_DOWN\r\n
0xd0000069 | RADIO_CONFIG_SINGLE\r\n
0xd000006a | RADIO_CONFIG_MULTI_MODE\r\n
0xd000006b | RADIO_CONFIG_1XCSFB\r\n
0xd000006c | RADIO_CONFIG_SVLTE\r\n
0xd000006d | RADIO_CONFIG_DualStandby\r\n
0xd000006e | RADIO_CONFIG_DualActive\r\n
0xd000006f | RADIO_CONFIG_SGLTE\r\n
0xd0000070 | RADIO_CONFIG_SVLTE_DUALACTIVE\r\n
0xd0000071 | RADIO_CONFIG_SGLTE_DUALACTIVE\r\n
0xd0000072 | RADIO_CONFIG_SRLTE\r\n
0xd0000073 | VoipIpcAudioRoute_Default\r\n
0xd0000074 | VoipIpcAudioRoute_Earpiece\r\n
0xd0000075 | VoipIpcAudioRoute_Speakerphone\r\n
0xd0000076 | VoipIpcAudioRoute_Bluetooth\r\n
0xd0000077 | RpcCallType_SetInitialAppState\r\n
0xd0000078 | RpcCallType_AcceptIncoming\r\n
0xd0000079 | RpcCallType_CallActive\r\n
0xd000007a | RpcCallType_End\r\n
0xd000007b | RpcCallType_Hold\r\n
0xd000007c | RpcCallType_RejectIncoming\r\n
0xd000007d | RpcCallType_Unhold\r\n
0xd000007e | RpcCallType_Mute\r\n
0xd000007f | RpcCallType_Unmute\r\n
0xd0000080 | RpcCallType_ForceEnd\r\n
0xd0000081 | PH_VOICEMAILPROVISIONINGSTATE_LEGACY_ONLY\r\n
0xd0000082 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_SUPPORTED\r\n
0xd0000083 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_CONFIGURED\r\n
0xd0000084 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_ENABLED\r\n
0xd0000085 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_ENABLED_NEW_USER\r\n
0xd0000086 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_NOT_FUNCTIONING\r\n
0xd0000087 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_CREATED\r\n
0xd0000088 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_PASSWORD_RESET\r\n
0xd0000089 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_INITIALIZED\r\n
0xd000008a | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_NO_DATA_AFFINITY\r\n
0xd000008b | StopVvmReason_Default\r\n
0xd000008c | StopVvmReason_DualSim_SingleLineVvm\r\n
0xd000008d | StopVvmReason_DualSim_NoDataAffinity\r\n
0xd000008e | RIL_3GPPTONE_TONEOFF\r\n
0xd000008f | RIL_3GPPTONE_RINGBACK\r\n
0xd0000090 | RIL_3GPPTONE_BUSY\r\n
0xd0000091 | RIL_3GPPTONE_CONGESTION\r\n
0xd0000092 | RIL_3GPPTONE_AUTHENTICATIONFAILURE\r\n
0xd0000093 | RIL_3GPPTONE_NUMBERUNOBTAINABLE\r\n
0xd0000094 | RIL_3GPPTONE_CALLDROPPED\r\n
0xd0000095 | RIL_3GPP2TONE_TONEOFF\r\n
0xd0000096 | RIL_3GPP2TONE_DIAL\r\n
0xd0000097 | RIL_3GPP2TONE_RINGBACK\r\n
0xd0000098 | RIL_3GPP2TONE_INTERCEPT\r\n
0xd0000099 | RIL_3GPP2TONE_ABRVINTERCEPT\r\n
0xd000009a | RIL_3GPP2TONE_REORDER\r\n
0xd000009b | RIL_3GPP2TONE_ABRVREORDER\r\n
0xd000009c | RIL_3GPP2TONE_BUSY\r\n
0xd000009d | RIL_3GPP2TONE_CONFIRM\r\n
0xd000009e | RIL_3GPP2TONE_ANSWER\r\n
0xd000009f | RIL_3GPP2TONE_CALLWAITING\r\n
0xd00000a0 | RIL_3GPP2TONE_PIP\r\n
0xd00000a1 | RIL_3GPP2ISDNALERTING_ALERTINGOFF\r\n
0xd00000a2 | RIL_3GPP2ISDNALERTING_NORMAL\r\n
0xd00000a3 | RIL_3GPP2ISDNALERTING_INTERGROUP\r\n
0xd00000a4 | RIL_3GPP2ISDNALERTING_SPECIAL\r\n
0xd00000a5 | RIL_3GPP2ISDNALERTING_PINGRING\r\n
0xd00000a6 | RIL_PERSOCHECKSTATE_NOTREADY\r\n
0xd00000a7 | RIL_PERSOCHECKSTATE_PASS\r\n
0xd00000a8 | RIL_PERSOCHECKSTATE_FAIL\r\n
0xd00000a9 | RIL_DEPERSOSTATE_READY\r\n
0xd00000aa | RIL_DEPERSOSTATE_CK_REQUIRED\r\n
0xd00000ab | RIL_DEPERSOSTATE_PUK_REQUIRED\r\n
0xd00000ac | RIL_DEPERSOSTATE_PUK_BLOCKED\r\n
0xd00000ad | No voicemail number found\r\n
0xd00000ae | SIM override key\r\n
0xd00000af | SIM data\r\n
0xd00000b0 | Default number cached in registry\r\n
0xd00000b1 | SIM fallback key\r\n
0xd00000b2 | Kind_None\r\n
0xd00000b3 | Kind_EmergencyModeChange\r\n
0xd00000b4 | Kind_ExitEmergencyModeFinished\r\n
0xd00000b5 | Kind_NetworkRegistrationChange\r\n
0xd00000b6 | Kind_SignalStrengthChange\r\n
0xd00000b7 | Kind_ModemPowerStateChange\r\n
0xd00000b8 | Kind_SubscriberNumberChange\r\n
0xd00000b9 | Kind_RegistryConfigChange\r\n
0xd00000ba | Kind_VoicemailNumberChangeRequest\r\n
0xd00000bb | Kind_VoicemailNumberSimSetCompleted\r\n
0xd00000bc | Kind_VoicemailNumberSimGetCompleted\r\n
0xd00000bd | Kind_Imsi\r\n
0xd00000be | Kind_SupServiceCallback\r\n
0xd00000bf | Kind_PinLockState\r\n
0xd00000c0 | Kind_SlotState\r\n
0xd00000c1 | Kind_SetCallerId\r\n
0xd00000c2 | Kind_ToneNotification\r\n
0xd00000c3 | Kind_CellBroadcastMessage\r\n
0xd00000c4 | Kind_GetLineCallForwardingStatusCompletion\r\n
0xd00000c5 | Kind_SetLineCallForwardingStatusCompletion\r\n
0xd00000c6 | Kind_GetLineCallForwardingNumberCompletion\r\n
0xd00000c7 | Kind_ServiceProviderNameChange\r\n
0xd00000c8 | Kind_PersoCheckStatus\r\n
0xd00000c9 | Kind_PersoDeactivationState\r\n
0xd00000ca | Kind_MuteStateChange\r\n
0xd00000cb | Kind_SlotCanAssociationsChanged\r\n
0xd00000cc | Kind_CallPresenceChanged\r\n
0xd00000cd | Kind_ImsStatusChanged\r\n
0xd00000ce | Kind_ImsSystemTypeChanged\r\n
0xd00000cf | Kind_RefreshVideoCallingSetting\r\n
0xd00000d0 | Kind_SetVideoCallingSetting\r\n
0xd00000d1 | Kind_SetVideoCallingSettingComplete\r\n
0xd00000d2 | Kind_GetVideoCallingSettingComplete\r\n
0xd00000d3 | Kind_GetPSMediaPreferencesComplete\r\n
0xd00000d4 | Kind_PSMediaPreferencesChanged\r\n
0xd00000d5 | RIL_SERVICE_UNKNOWN\r\n
0xd00000d6 | RIL_SERVICE_VOICE\r\n
0xd00000d7 | RIL_SERVICE_FAX\r\n
0xd00000d8 | RIL_SERVICE_OTHER\r\n
0xd00000d9 | FWDCODE_UNCONDITIONAL\r\n
0xd00000da | FWDCODE_BUSY\r\n
0xd00000db | FWDCODE_NOREPLY\r\n
0xd00000dc | FWDCODE_NOTREACHABLE\r\n
0xd00000dd | FWDCODE_ALL\r\n
0xd00000de | FWDCODE_ALLCONDITIONAL\r\n
0xd00000df | FWDCODE_STATECHANGED\r\n
0xd00000e0 | SimPinOperation_None\r\n
0xd00000e1 | SimPinOperation_EnableSimPin\r\n
0xd00000e2 | SimPinOperation_DisableSimPin\r\n
0xd00000e3 | SimPinOperation_ChangeSimPin\r\n
0xd00000e4 | SimPinOperation_UnlockSim\r\n
0xd00000e5 | SimPinOperation_UnblockSim\r\n
0xd00000e6 | PersoFeature_Unknown\r\n
0xd00000e7 | PersoFeature_None\r\n
0xd00000e8 | PersoFeature_3Gpp_Net\r\n
0xd00000e9 | PersoFeature_3Gpp_NetSub\r\n
0xd00000ea | PersoFeature_3Gpp_Sp\r\n
0xd00000eb | PersoFeature_3Gpp_Corp\r\n
0xd00000ec | PersoFeature_3Gpp_USim\r\n
0xd00000ed | PersoFeature_3Gpp2_NetType1\r\n
0xd00000ee | PersoFeature_3Gpp2_NetType2\r\n
0xd00000ef | PersoFeature_3Gpp2_Hrpd\r\n
0xd00000f0 | PersoFeature_3Gpp2_Sp\r\n
0xd00000f1 | PersoFeature_3Gpp2_Corp\r\n
0xd00000f2 | PersoFeature_3Gpp2_Uim\r\n
0xd00000f3 | DialAction_None\r\n
0xd00000f4 | DialAction_Activation\r\n
0xd00000f5 | DialAction_Deactivation\r\n
0xd00000f6 | DialAction_Interrogation\r\n
0xd00000f7 | DialAction_Registration\r\n
0xd00000f8 | DialAction_Erasure\r\n
0xd00000f9 | RIL_UNSSSCODE_FORWARDEDCALL\r\n
0xd00000fa | RIL_UNSSSCODE_CUGCALL\r\n
0xd00000fb | RIL_UNSSSCODE_CALLPUTONHOLD\r\n
0xd00000fc | RIL_UNSSSCODE_CALLRETRIEVED\r\n
0xd00000fd | RIL_UNSSSCODE_ENTEREDMULTIPARTY\r\n
0xd00000fe | RIL_UNSSSCODE_HELDCALLRELEASED\r\n
0xd00000ff | RIL_UNSSSCODE_FORWARDCHECKSS\r\n
0xd0000100 | RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER\r\n
0xd0000101 | RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER\r\n
0xd0000102 | RIL_UNSSSCODE_DEFLECTEDCALL\r\n
0xd0000103 | RIL_UNSSSCODE_ADDITIONALINCOMINGCF\r\n
0xd0000104 | RIL_UNSSSCODE_UNCONDITIONALCFACTIVE\r\n
0xd0000105 | RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE\r\n
0xd0000106 | RIL_UNSSSCODE_CALLWASFORWARDED\r\n
0xd0000107 | RIL_UNSSSCODE_CALLISWAITING\r\n
0xd0000108 | RIL_UNSSSCODE_OUTGOINGCALLSBARRED\r\n
0xd0000109 | RIL_UNSSSCODE_INCOMINGCALLSBARRED\r\n
0xd000010a | RIL_UNSSSCODE_CLIRSUPPRESSREJECT\r\n
0xd000010b | RIL_IMSSYSTEMTYPE_UNKNOWN\r\n
0xd000010c | RIL_IMSSYSTEMTYPE_WIFI\r\n
0xd000010d | RIL_IMSSYSTEMTYPE_LTE\r\n
0xd000010e | CallUpgradeSupportLevel_NotSupported\r\n
0xd000010f | CallUpgradeSupportLevel_NonSeamless\r\n
0xd0000110 | CallUpgradeSupportLevel_Seamless\r\n
0xd0000111 | CallUpgradeSupportLevel_AppDetermined\r\n
0xd0000112 | VideoCallingSetting_Disabled\r\n
0xd0000113 | VideoCallingSetting_Enabled\r\n
0xd0000114 | VideoCallingSetting_CachedValue\r\n
0xd0000115 | RIL_CALLMEDIADIRECTION_NONE\r\n
0xd0000116 | RIL_CALLMEDIADIRECTION_RX\r\n
0xd0000117 | RIL_CALLMEDIADIRECTION_TX\r\n
0xd0000118 | RIL_CALLMEDIADIRECTION_RXTX\r\n
0xd0000119 | RIL_CALLMEDIAOFFERACTION_NONE\r\n
0xd000011a | RIL_CALLMEDIAOFFERACTION_ERROR\r\n
0xd000011b | RIL_CALLMEDIAOFFERACTION_REJECT\r\n
0xd000011c | RIL_CALLMEDIAOFFERACTION_ASK\r\n
0xd000011d | RIL_CALLMEDIAOFFERACTION_ACCEPT\r\n
0xd000011e | RIL_CALLMEDIAOFFERACTION_CANCEL\r\n
0xd000011f | None\r\n
0xd0000120 | CircuitSwitched\r\n
0xd0000121 | PacketSwitched\r\n
0xd0000122 | PH_LINESYSTEMTYPE_GSM\r\n
0xd0000123 | PH_LINESYSTEMTYPE_CDMA\r\n
0xd0000124 | PH_LINESYSTEMTYPE_VOIP\r\n
0xd0000125 | PH_LINESYSTEMTYPE_UNKNOWN\r\n
0xd0000126 | PH_LINESYSTEMTYPE_IMS\r\n
0xd0000127 | CellularAudioType_None\r\n
0xd0000128 | CellularAudioType_CircuitSwitched\r\n
0xd0000129 | CellularAudioType_PacketSwitched\r\n
0xd000012a | CellularAudioType_PacketSwitched_WiFi\r\n
0xd000012b | RIL_CALLHANDOVERPHASE_STARTED\r\n
0xd000012c | RIL_CALLHANDOVERPHASE_COMPLETED\r\n
0xd000012d | RIL_CALLHANDOVERPHASE_FAILED\r\n
0xd000012e | RIL_CALLHANDOVERPHASE_CANCELLED\r\n
0xd000012f | None\r\n
0xd0000130 | Pending\r\n
0xd0000131 | Connected\r\n
0xd0000132 | PhoneMediaQuality_Unknown\r\n
0xd0000133 | PhoneMediaQuality_Low\r\n
0xd0000134 | PhoneMediaQuality_Standard\r\n
0xd0000135 | PhoneMediaQuality_High\r\n
0xd0000136 | PhoneMediaQuality_AMR_NB\r\n
0xd0000137 | PhoneMediaQuality_AMR_WB\r\n
0xd0000138 | PhoneMediaQuality_EVRC\r\n
0xd0000139 | PhoneMediaQuality_EVRC_B\r\n
0xd000013a | PhoneMediaQuality_EVRC_NW\r\n
0xd000013b | PhoneMediaQuality_EVRC_WB\r\n
0xd000013c | PhoneMediaQuality_EVS_FB\r\n
0xd000013d | PhoneMediaQuality_EVS_NB\r\n
0xd000013e | PhoneMediaQuality_EVS_SWB\r\n
0xd000013f | PhoneMediaQuality_EVS_WB\r\n
0xd0000140 | PhoneMediaQuality_GSM_EFR\r\n
0xd0000141 | PhoneMediaQuality_GSM_FR\r\n
0xd0000142 | PhoneMediaQuality_GSM_HR\r\n
0xd0000143 | PhoneMediaQuality_QCELP13K\r\n
0xd0000144 | PhoneMediaQuality_G711U\r\n
0xd0000145 | PhoneMediaQuality_G711A\r\n
0xd0000146 | PhoneMediaQuality_G722\r\n
0xd0000147 | PhoneMediaQuality_G723\r\n
0xd0000148 | PhoneMediaQuality_G729\r\n
0xd0000149 | RIL_IMSFAILUREMESSAGETYPE_REGISTER\r\n
0xd000014a | RIL_IMSFAILUREMESSAGETYPE_SUBSCRIBE\r\n
0xd000014b | RIL_IMSFAILUREMESSAGETYPE_INCALL\r\n
0xd000014c | RIL_PSMPREF_UNKNOWN\r\n
0xd000014d | RIL_PSMPREF_WIFIONLY\r\n
0xd000014e | RIL_PSMPREF_WIFIPREFERRED\r\n
0xd000014f | RIL_PSMPREF_CELLONLY\r\n
0xd0000150 | RIL_PSMPREF_CELLPREFERRED\r\n
0xd0000151 | RIL_MSGMWITYPE_NONE\r\n
0xd0000152 | RIL_MSGMWITYPE_VOICEMAIL\r\n
0xd0000153 | RIL_MSGMWITYPE_VIDEOMAIL\r\n
0xd0000154 | RIL_MSGMWITYPE_FAX\r\n
0xd0000155 | RIL_MSGMWITYPE_PAGER\r\n
0xd0000156 | RIL_MSGMWITYPE_MULTIMEDIA\r\n
0xd0000157 | RIL_MSGMWITYPE_TEXT\r\n
0xd0000158 | MtsiCallDirection_Incoming\r\n
0xd0000159 | MtsiCallDirection_Outgoing\r\n
0xd000015a | MtsiCallState_Offering\r\n
0xd000015b | MtsiCallState_Held\r\n
0xd000015c | MtsiCallState_Active\r\n
0xd000015d | MtsiCallState_Terminated\r\n
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
0xf000001a | CallVerb_ExplicitCallTransfer\r\n
0xf000001b | Dial\r\n
0xf000001c | End\r\n
0xf000001d | DropActiveAcceptHeld\r\n
0xf000001e | Hold\r\n
0xf000001f | Unhold\r\n
0xf0000020 | Swap\r\n
0xf0000021 | Private\r\n
0xf0000022 | Conference\r\n
0xf0000023 | Flash\r\n
0xf0000024 | RejectIncoming\r\n
0xf0000025 | AcceptIncoming\r\n
0xf0000026 | SendDtmf\r\n
0xf0000027 | StartDtmf\r\n
0xf0000028 | StopDtmf\r\n
0xf0000029 | DropFromConference\r\n
0xf000002a | DisableLocalVideo\r\n
0xf000002b | EnableLocalVideo\r\n
0xf000002c | AddVideo\r\n
0xf000002d | DropVideo\r\n
0xf000002e | AcceptIncomingVideo\r\n
0xf000002f | RejectIncomingVideo\r\n
0xf0000030 | SetVideoPaused\r\n
0xf0000031 | StartRecording\r\n
0xf0000032 | PauseRecording\r\n
0xf0000033 | StopRecording\r\n
0xf0000034 | ExplicitCallTransfer\r\n
0xf0000035 | RIL_PARAM_CI_EXECUTOR\r\n
0xf0000036 | RIL_PARAM_CI_ID\r\n
0xf0000037 | RIL_PARAM_CI_DIRECTION\r\n
0xf0000038 | RIL_PARAM_CI_STATUS\r\n
0xf0000039 | RIL_PARAM_CI_TYPE\r\n
0xf000003a | RIL_PARAM_CI_MULTIPARTY\r\n
0xf000003b | RIL_PARAM_CI_ADDRESS\r\n
0xf000003c | RIL_PARAM_CI_SUBADDRESS\r\n
0xf000003d | RIL_PARAM_CI_DESCRIPTION\r\n
0xf000003e | RIL_PARAM_CI_NUM_PRES_IND\r\n
0xf000003f | RIL_PARAM_CI_NAME_PRES_IND\r\n
0xf0000040 | RIL_PARAM_CI_FLAGS\r\n
0xf0000041 | RIL_PARAM_CI_DISCONNECTINITIATOR\r\n
0xf0000042 | RIL_PARAM_CI_DISCONNECTREASON\r\n
0xf0000043 | RIL_PARAM_CI_DISCONNECTDETAILS\r\n
0xf0000044 | RIL_PARAM_CI_OFFERANSWER\r\n
0xf0000045 | RIL_PARAM_CI_HANDOVERSTATE\r\n
0xf0000046 | RIL_PARAM_RPI_EXECUTOR\r\n
0xf0000047 | RIL_PARAM_RPI_ADDRESS\r\n
0xf0000048 | RIL_PARAM_RPI_SUBADDRESS\r\n
0xf0000049 | RIL_PARAM_RPI_DESCRIPTION\r\n
0xf000004a | RIL_PARAM_RPI_NUM_PRES_IND\r\n
0xf000004b | RIL_PARAM_RPI_NAME_PRES_IND\r\n
0xf000004c | RIL_PARAM_RPI_ID\r\n
0xf000004d | RIL_PARAM_ON_LONGNAME\r\n
0xf000004e | RIL_PARAM_ON_SHORTNAME\r\n
0xf000004f | RIL_PARAM_ON_NUMNAME\r\n
0xf0000050 | RIL_PARAM_ON_COUNTRY_CODE\r\n
0xf0000051 | RIL_PARAM_ON_SYSTEMTYPE\r\n
0xf0000052 | RIL_PARAM_NETWORKCODE_EXECUTOR\r\n
0xf0000053 | RIL_PARAM_NETWORKCODE_MCC\r\n
0xf0000054 | RIL_PARAM_NETWORKCODE_MNC\r\n
0xf0000055 | RIL_PARAM_NETWORKCODE_SID\r\n
0xf0000056 | RIL_PARAM_NETWORKCODE_NID\r\n
0xf0000057 | RIL_PARAM_NETWORKCODE_RI\r\n
0xf0000058 | RILCALLINFO_FLAG_ALIENCALL\r\n
0xf0000059 | RILCALLINFO_FLAG_EMERGENCYCALL\r\n
0xf000005a | RIL_PARAM_DISPLAY_EXECUTOR\r\n
0xf000005b | RIL_PARAM_DISPLAY_TYPE\r\n
0xf000005c | RIL_PARAM_DISPLAY_TAG\r\n
0xf000005d | RIL_PARAM_DISPLAY_MESSAGESIZE\r\n
0xf000005e | RIL_PARAM_DISPLAY_MESSAGE\r\n
0xf000005f | RIL_SYSTEMTYPE_1XRTT\r\n
0xf0000060 | RIL_SYSTEMTYPE_EVDO\r\n
0xf0000061 | RIL_SYSTEMTYPE_GSM\r\n
0xf0000062 | RIL_SYSTEMTYPE_UMTS\r\n
0xf0000063 | RIL_SYSTEMTYPE_LTE\r\n
0xf0000064 | RIL_SYSTEMTYPE_TDSCDMA\r\n
0xf0000065 | VoipIpcCallAttributes_VoiceOnly\r\n
0xf0000066 | VoipIpcCallAttributes_Video\r\n
0xf0000067 | RIL_PARAM_TONESIGNAL_GPPTONE\r\n
0xf0000068 | RIL_PARAM_TONESIGNAL_GPPTONE2\r\n
0xf0000069 | RIL_PARAM_TONESIGNAL_GPP2ISDNALERTING\r\n
0xf000006a | RIL_PARAM_TONESIGNAL_EXECUTOR\r\n
0xf000006b | RIL_PERSOFEATURE_NONE\r\n
0xf000006c | RIL_PERSOFEATURE_3GPP_NET\r\n
0xf000006d | RIL_PERSOFEATURE_3GPP_NETSUB\r\n
0xf000006e | RIL_PERSOFEATURE_3GPP_SP\r\n
0xf000006f | RIL_PERSOFEATURE_3GPP_CORP\r\n
0xf0000070 | RIL_PERSOFEATURE_3GPP_USIM\r\n
0xf0000071 | RIL_PERSOFEATURE_3GPP2_NETTYPE1\r\n
0xf0000072 | RIL_PERSOFEATURE_3GPP2_NETTYPE2\r\n
0xf0000073 | RIL_PERSOFEATURE_3GPP2_HRPD\r\n
0xf0000074 | RIL_PERSOFEATURE_3GPP2_SP\r\n
0xf0000075 | RIL_PERSOFEATURE_3GPP2_CORP\r\n
0xf0000076 | RIL_PERSOFEATURE_3GPP2_UIM\r\n
0xf0000077 | RIL_PARAM_PDS_STATE\r\n
0xf0000078 | RIL_PARAM_PDS_CK_ATTEMPTS\r\n
0xf0000079 | RIL_PARAM_PDS_PUK_ATTEMPTS\r\n
0xf000007a | RIL_PARAM_SI_ADDRESS\r\n
0xf000007b | RIL_PARAM_SI_DESCRIPTION\r\n
0xf000007c | RIL_PARAM_SI_SERVICE\r\n
0xf000007d | RIL_PARAM_IMSSTATUS_EXECUTOR\r\n
0xf000007e | RIL_PARAM_IMSSTATUS_HUICCAPP\r\n
0xf000007f | RIL_PARAM_IMSSTATUS_AVAILABLESERVICES\r\n
0xf0000080 | RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT\r\n
0xf0000081 | RIL_PARAM_IMSSTATUS_SERVINGDOMAIN\r\n
0xf0000082 | RIL_PARAM_IMSSTATUS_SYSTEMTYPE\r\n
0xf0000083 | RIL_IMS_SERVICE_SMS\r\n
0xf0000084 | RIL_IMS_SERVICE_VOICE\r\n
0xf0000085 | RIL_IMS_SERVICE_VIDEO\r\n
0xf0000086 | RIL_IMS_SERVICE_CUSTOM\r\n
0xf0000087 | RIL_IMS_SERVICE_SUPSVC\r\n
0xf0000088 | RIL_IMS_SERVICE_RCS\r\n
0xf0000089 | RIL_IMS_SERVICE_USSD\r\n
0xf000008a | RIL_IMS_SERVICE_E_VOICE\r\n
0xf000008b | RIL_PARAM_CMOA_ID\r\n
0xf000008c | RIL_PARAM_CMOA_CHANGE\r\n
0xf000008d | RIL_PARAM_CMOA_ACTION\r\n
0xf000008e | RIL_PARAM_CMOA_OLD_STATE\r\n
0xf000008f | RIL_PARAM_CMOA_NEW_STATE\r\n
0xf0000090 | RIL_PARAM_CALLVIDEO_PEERCAPABILITIES\r\n
0xf0000091 | RIL_PARAM_CALLVIDEO_FLAGS\r\n
0xf0000092 | RIL_CALLMEDIAVIDEOFLAG_CAPABILITY_UNKNOWN\r\n
0xf0000093 | RIL_CALLMEDIAVIDEOFLAG_PAUSE\r\n
0xf0000094 | RIL_PARAM_HANDOVER_PHASE\r\n
0xf0000095 | RIL_PARAM_HANDOVER_OLD_TYPE\r\n
0xf0000096 | RIL_PARAM_HANDOVER_NEW_TYPE\r\n
0xf0000097 | RIL_PARAM_HANDOVER_3GPPCAUSE\r\n
0xf0000098 | RIL_UICCLOCKSTATE_VERIFIED\r\n
0xf0000099 | RIL_UICCLOCKSTATE_ENABLED\r\n
0xf000009a | RIL_UICCLOCKSTATE_BLOCKED\r\n
0xf000009b | RIL_PARAM_UICCLOCKSTATE_UICCLOCK\r\n
0xf000009c | RIL_PARAM_UICCLOCKSTATE_LOCKSTATE\r\n
0xf000009d | RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT\r\n
0xf000009e | RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT\r\n
0xf000009f | RIL_PARAM_UAPCS_HUICCAPP\r\n
0xf00000a0 | RIL_PARAM_UAPCS_PERSOFEATURE\r\n
0xf00000a1 | RIL_PARAM_UAPCS_PERSOCHECKSTATE\r\n
0xf00000a2 | RIL_PARAM_MWISUMMARY_EXECUTOR\r\n
0xf00000a3 | RIL_PARAM_MWISUMMARY_REFNUM\r\n
0xf00000a4 | RIL_PARAM_MWISUMMARY_ACCTADDR\r\n
0xf00000a5 | RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS\r\n
0xf00000a6 | RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS\r\n
0xf00000a7 | RIL_PARAM_MWISUMMARY_SUMMARYITEMS\r\n
0xf00000a8 | RIL_PARAM_MWIDETAIL_EXECUTOR\r\n
0xf00000a9 | RIL_PARAM_MWIDETAIL_REFNUM\r\n
0xf00000aa | RIL_PARAM_MWIDETAIL_NUMDETAILITEMS\r\n
0xf00000ab | RIL_PARAM_MWIDETAIL_DETAILITEMS\r\n

### 10.0.16299.15

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
0xb0000064 | Enqueued verb %1, callid %2 (completion context %3)\r\n
0xb0000065 | Enqueued verb %1, callids %2, %3 (completion context %4)\r\n
0xb0000066 | Enqueued verb Dial, callid %1, callType %2, calleridoption %3 (completion context %4)\r\n
0xb0000067 | Dequeued verb %1, callid %2 (completion context %3)\r\n
0xb0000068 | Dequeued verb %1, callids %2, %3 (completion context %4)\r\n
0xb0000069 | Dequeued verb Dial, callid %1, callType %2, calleridoption %3 (completion context %4)\r\n
0xb000006a | Verb completed with HRESULT %1; host notified (completion context %2)\r\n
0xb000006b | Verb completed with HRESULT %1; host not notified (completion context %2)\r\n
0xb000006c | Began tracking async CellVoice request id %1 (for completion context %2)\r\n
0xb000006d | Stopped tracking async CellVoice request id %1 (for completion context %2)\r\n
0xb000006e | Enqueued async CellVoice request id %1 completion with HRESULT %2\r\n
0xb000006f | Gsm call manager called I3GPPCallModel::%1 with async request id %2 for callid %3 (cellvoice callid %4)\r\n
0xb0000070 | Gsm call manager called I3GPPCallModel::%1 with async request id %2 for callids %3, %4\r\n
0xb0000071 | Gsm call manager called I3GPPCallModel::RequestOutgoingCall with async request id %1 for callid %2, callType %3 (no cellvoice callid)\r\n
0xb0000072 | CallManager got call progress update for cellvoiceId %1; status %2; direction %3; number %4; name %5; party %6; flags %7; type %8; valid params %9; \r\n
0xb0000073 | CellVoice returned failure %1 to get subscriber number\r\n
0xb0000074 | CellVoice returned failure %1 to get voicemail number\r\n
0xb0000075 | CellVoice get IMSI completed with error %1\r\n
0xb0000076 | Resetting VVM state; old MCC/MNC/nameDiff %1 %2 %3\r\n
0xb0000077 | Used RIL system type %1; got signal strength %2\r\n
0xb0000078 | Used RIL system type %1; voice domain %2; got registration status %3\r\n
0xb000007a | No Visual Voicemail provider was loaded for MCC,MNC %1,%2\r\n
0xb000007b | Visual Voicemail action %1 is not currently available on this line\r\n
0xb000007c | Legacy Voicemail message received: %1. Message count: %2\r\n
0xb000007d | Registered to operator: params %1; long name "%2"; short name "%3"; numeric name"%4"; country code "%5"\r\n
0xb000007e | Switched to data registration to get registration info\r\n
0xb000007f | Status %1 from cellcore reading voicemail count %2 from SIM\r\n
0xb0000080 | Status %1 from cellcore writing voicemail count %2 to SIM\r\n
0xb0000083 | [CellularAudio] Muting cellular audio\r\n
0xb0000084 | [CellularAudio] Unmuting cellular audio\r\n
0xb0000085 | CallManager got disconnect notification for cellvoiceId %1; initiator %2; reason %3; group %4; gppdetails [ location %5 cause %6 ]\r\n
0xb0000086 | CallModel3GPP2 invoking %1; callid %2; asyncRequestId %3\r\n
0xb0000087 | CdmaHeuristics invoking %1; callid %2 and %3; asyncRequestId %3; completionContext %4\r\n
0xb000008b | Call manager got call waiting notification for cellvoice callid %1: rilremotepartyinfo: params %2 numberpres %3 namepres %4\r\n
0xb000008c | Call manager got dial id notification for cellvoice callid %1: params %2 numberpres %3 namepres %4\r\n
0xb000008d | CdmaHeuristics started tracking verb %1 asyncRequestId %2 for completionContext %3\r\n
0xb000008e | CdmaHeuristics stopped tracking verb %1 asyncRequestId %2 for completionContext %3\r\n
0xb000008f | Status %1 from cellcore reading call forwarding status %2 from SIM\r\n
0xb0000090 | Status %1 from cellcore reading call forwarding number from SIM\r\n
0xb0000091 | Status %1 from cellcore writing call forwarding status to SIM\r\n
0xb0000092 | Status %1 from cellcore writing call forwarding number to SIM\r\n
0xb0000093 | Sim LockState changed to: %1\r\n
0xb0000094 | Cellvoice UICC Line set; sim swap pending: %1; old/new line ID: %2 / %3\r\n
0xb0000095 | Finished retrieving home MCC/MNC: %1 %2\r\n
0xb0000096 | Set visual voicemail provisioning state to %1\r\n
0xb0000097 | Forced SIM swap based on MCC/MNC: %1 %2 ==> %3 %4\r\n
0xb0000098 | Modem power state changed to %1\r\n
0xb0000099 | Network codes: params %1; MCC %2; MNC %3\r\n
0xb000009a | SIMOM gave LineFactory a duplicate modem (ignored)\r\n
0xb000009b | SIMOM gave LineFactory an unknown modem to remove (ignored)\r\n
0xb000009c | SIMOM gave LineFactory an unknown modem for adding a slot (ignored)\r\n
0xb000009d | SIMOM gave LoneFactory a duplicate slot (ignored)\r\n
0xb000009e | SIMOM gave LineFactory an unknown modem for removing a slot (ignored)\r\n
0xb000009f | SIMOM gave LineFactory an unknown slot to remove (ignored)\r\n
0xb00000a0 | Line not created: modem index %1 or slot index %2 out of bounds (from ISlot %3)\r\n
0xb00000a1 | CallManager new incoming call from %1\r\n
0xb00000a2 | Call forwarding state updated. SupSvcCode: %1; Enable: %2; new m_callForwardingState: %3\r\n
0xb00000a3 | Read call forwarding state from registry. m_callForwardingState: %1; m_callForwardingAddress: %2\r\n
0xb00000a4 | OnSupServiceCallback. ExecutionResult: %1; SvcCode: %2; DialAction: %3\r\n
0xb00000a5 | Legacy Voicemail message ignored due to config setting\r\n
0xb00000a6 | CdmaHeuristics set local hold to %1\r\n
0xb00000a7 | Detected SGLTE config with no GSM RF; using synthesized no-registration status\r\n
0xb00000a8 | Enqueued verb AcceptIncoming, callid %1, callType %2 (completion context %3)\r\n
0xb00000a9 | Dequeued verb AcceptIncoming, callid %1, callType %2 (completion context %3)\r\n
0xb00000aa | Gsm call manager called I3GPPCallModel::AcceptIncomingCall with async request id %1 for callid %2, callType %3 (cellvoice callid %4)\r\n
0xb00000ab | Received an IMS SIP disconnect cause: error-code=%1, reason=%2\r\n
0xb00000ac | Assumed error is XCAP related and enabling show/hide caller id feature\r\n
0xb00000ad | [Voicemail] Timer task for Visual Voicemail configuration changes fired.\r\n
0xb00000ae | [Voicemail] Attempting to queue action for Visual Voicemail configuration changes [isChangePending=%1]\r\n
0xb00000af | [Voicemail] Got notified of Visual Voicemail registry changes\r\n
0xb00000b0 | [Voicemail] Configure Visual Voicemail [homeMcc=%1][homeMnc=%2][dataAffinityExists=%3]\r\n
0xb00000b1 | Can Data affinity change [LineId=%1][dataAffinityCanIndex=%2]\r\n
0xb00000ca | Terminating Active Call Agent %1 due to timeout waiting for Notify callback\r\n
0xb00000cb | Cell Broadcast Listener received message %1\r\n
0xb00000cc | Display text changed: params %1, info type %2, info tag %3, message size %4\r\n
0xb00000cd | Calling IVoIPTaskManagerClient->LaunchActiveCallAgent(%1)\r\n
0xb00000ce | Calling IVoIPTaskManagerClient->CancelActiveCallAgentInstance(%1)\r\n
0xb00000cf | _CancelActiveCallAgent for product id: %1; isForcedShutdown: %2; isActiveCallAgentRunning: %3\r\n
0xb00000d0 | Calling IVoIPTaskManagerClient->HoldActiveCall(%1)\r\n
0xb00000d1 | Calling IVoIPTaskManagerClient->UnholdActiveCall(%1)\r\n
0xb00000d2 | Calling IVoIPTaskManagerClient->OnIncomingCallDialogDisplayed(%1)\r\n
0xb00000d3 | Calling IVoIPTaskManagerClient->OnIncomingCallDialogDismissed(%1)\r\n
0xb00000d4 | InitializedConnectionToAppHost called on VoipProvider. RPC Handle: %1; VoipLine: %2; AgentProcessId: %3; ContextId: %4\r\n
0xb00000d5 | LineFactory->NewIncomingCall(%1, %2)\r\n
0xb00000d6 | LineFactory->NewOutgoingCall(%1, %2)\r\n
0xb00000d7 | LineFactory->CallActive(%1, %2)\r\n
0xb00000d8 | LineFactory->CallHeld(%1, %2)\r\n
0xb00000d9 | LineFactory->CallEnded(%1, %2)\r\n
0xb00000da | LineFactory->SetAudioRouting(%1, %2)\r\n
0xb00000db | LineFactory->GetAudioRouting(%1)\r\n
0xb00000dc | LineFactory->SetMuteState(%1, %2)\r\n
0xb00000dd | LineFactory->UpdateCallContactName(%1, %2)\r\n
0xb00000de | LineFactory->UpdateCallStartTime(%1, %2)\r\n
0xb00000df | LineFactory->GetCallStartTime(%1, %2)\r\n
0xb00000e0 | LineFactory->UpdateCallAttributes(%1, %2, %3)\r\n
0xb00000e1 | VoipAppHostHandle_rundown(%1)\r\n
0xb00000e2 | _PendingRpcCallCompleted(%2, %3) for line: %1; onTime: %4\r\n
0xb00000e3 | Calling %1 on VoipApp for line: %2. Controller callId: %3; VoipApp CallId: %4\r\n
0xb00000e4 | Calling %1 on VoipApp for line: %2.\r\n
0xb00000e5 | Calling OnAudioRouteChanged on VoipApp for line: %1. AudioRoute: %2; Available Paths: %3\r\n
0xb00000e6 | Can %1 entered emergency mode %2\r\n
0xb00000e7 | Modem constraint violated: Illegal CPI %1\r\n
0xb00000e8 | Modem constraint violated: Async dial failure %1 for call in CPI state %2\r\n
0xb00000e9 | Modem constraint violated: Mismatched direction fields; direction %1, CPI state %2\r\n
0xb00000ea | CallManager invoked I3GPP[2]CallModel::%1; asyncRequestId %2\r\n
0xb00000eb | CallManager invoking I3GPP[2]CallModel::%1; asyncRequestId %2\r\n
0xb00000ec | CallModel3GPP2 invoking %1; callid %2 and %3; asyncRequestId %4)\r\n
0xb00000ed | CdmaHeuristics invoking %1; callid %2; asyncRequestId %3; completionContext %4\r\n
0xb00000ee | CdmaHeuristics verb completed: asyncRequestId %1; result %2; verb %3; callid %4; original completionContext %5\r\n
0xb00000ef | CdmaHeuristics verb completed: asyncRequestId %1; result %2\r\n
0xb00000f0 | CallModel3GPP2 verb completed: asyncRequestId %1; result %2; verb %3; callid %4; original completionContext %5\r\n
0xb00000f1 | Dequeued async CellVoice request id %1 completion with HRESULT %2\r\n
0xb00000f2 | CallModel processing call progress update with cellvoiceId %1 for callId %2\r\n
0xb00000f5 | CdmaHeuristics tracking with asyncRequestId %1 not found\r\n
0xb00000f9 | CallModel3GPP2 got unexpected call update for cellvoiceId %1; while having existing cellvoiceId %2\r\n
0xb00000fd | Processed request to clear Voicemail count.\r\n
0xb00000fe | Default voicemail number source is: %1\r\n
0xb00000ff | Modem constraint violated: Illegal 3GPP2 CallWaiting notification\r\n
0xb0000100 | Tone signal received: params %1, %2, %3, %4\r\n
0xb0000101 | LineNotificationWorkItem: instantiated #%1 (%2)\r\n
0xb0000102 | LineNofiticationWorkItem: processing #%1 (%2)\r\n
0xb0000103 | LineNofiticationWorkItem: finished processing #%1 (%2)\r\n
0xb0000104 | LineNofiticationWorkItem: canceled #%1 (%2)\r\n
0xb0000105 | Got subscriber numbers; dwNumSubscribers = %1\r\n
0xb0000106 | Subscriber number entry #%1: params #2, service #3\r\n
0xb0000107 | Subscriber number is missing or empty\r\n
0xb0000108 | Got IMS status change notification. [Params=%1][AvailableServices=%2]\r\n
0xb0000109 | [CallModel3GPP] Call model changing between GSM and IMS, [ims=%1][m_imsOnWiFi=%2]\r\n
0xb000010a | Roaming override number used.  Dialing %1.\r\n
0xb000010b | HandleUICCPersoCheckStatusChange, [dwParams=%1][dwPersoFeature=%2][dwPersoCheckState=%3]\r\n
0xb000010c | Get Perso deactivation state for %1 completed with hr %2; params %3; state %4; unlock remaining %5; unblock remaining %6\r\n
0xb000010d | Deactivate Perso for %1 completed with hr %2; params %3; state %4; unlock remaining %5; unblock remaining %6; async API context %7\r\n
0xb000010e | Initiating SIM PIN operation %1; async completion context = %2\r\n
0xb000010f | Initiating Perso unlock for %1; async completion context = %2\r\n
0xb0000110 | SIM PIN operation '%1' with async completion context %2 complete, result % = 3\r\n
0xb0000111 | 3GPP2CallModel ignored alien call (CellVoice ID %1) due to existing call (CellVoice ID %2).\r\n
0xb0000112 | 3GPPCallModel suppressed call update due to invalid state.\r\n
0xb0000113 | Unsolicited supservice %1 received for CellVoice callid %2\r\n
0xb0000114 | CellVoice Response Received in Method: %1. Async Hresult: %2\r\n
0xb0000115 | dwParams %1; dwNetworkSSErrorCause %2; dwNetworkCCErrorCause %3; dwVendorErrorCause %4\r\n
0xb0000116 | CellVoice reported infoClasses: %1.\r\n
0xb0000117 | CellVoice reported hide ID settings: params %1, status %2, provisioning %3.\r\n
0xb0000118 | CellVoice reported call forwarding settings: params %1, info class %2, delay time %3, status %4.\r\n
0xb0000119 | CellVoice Ussd Data Status: %1.\r\n
0xb000011a | Ussd Session terminated\r\n
0xb000011b | New Ussd Session initiated\r\n
0xb000011c | Invalid Callforwarding delay time parameter: %1. Using default value instead.\r\n
0xb000011d | Using default value for call forwarding delay time\r\n
0xb000011e | CellVoice reported COLR settings: params %1, status %2, provisioning %3.\r\n
0xb000011f | CellVoice reported CLIP settings: params %1, status %2, provisioning %3.\r\n
0xb0000120 | Executing sup service code %1, action %2\r\n
0xb0000121 | Ussd User response truncated\r\n
0xb0000122 | CellVoice reported COLP settings: params %1, status %2, provisioning %3.\r\n
0xb0000123 | Address for unsolicited supservice %1 is %2\r\n
0xb0000124 | Calling %1 on VoipApp for line: %2. VoipApp CallId: %3\r\n
0xb0000127 | RemoteId Request Complete: CallId: %1 RemoteId Exists: %2\r\n
0xb0000128 | Launching Voip app with URI: %1\r\n
0xb0000129 | LineFactory->NewIncomingUpgradeCall(%1, %2)\r\n
0xb000012a | LineFactory->NewOutgoingUpgradeCall(%1, %2). CallUpgradeGuid: %3\r\n
0xb000012b | LineFactory->CallReady(%1, %2)\r\n
0xb000012c | 3GPPCallModel suppressed call update due to ECall Failover.\r\n
0xb000012d | Dialing an Emergency call. PhoneCallId: %1.\r\n
0xb000012e | 3GPPCallModel got surprise outgoing Emergency call notification. Existing ECallId: %1, IgnoreNotification: %2.\r\n
0xb000012f | Modem Radio Config changed to %1\r\n
0xb0000130 | Setting Can Focus for Can: %1\r\n
0xb0000131 | Set Can Focus result: %1\r\n
0xb0000132 | Disconnecting dialed call with callId: %1 for incoming call.\r\n
0xb0000133 | LineFactory->GetNextOperation(%1)\r\n
0xb0000134 | Terminating Call Query Agent %1 due to timeout waiting for Notify callback\r\n
0xb0000135 | lineFactory->VoipAppOperationComplete(%1). Completed operationId: %2. Succeeded: %3. Call upgrade support: %4\r\n
0xb0000136 | Calling IVoIPTaskManagerClient->LaunchCallQueryAgent(%1)\r\n
0xb0000137 | Calling IVoIPTaskManagerClient->CancelCallQueryAgentInstance(%1)\r\n
0xb0000138 | Received async dial completion. CallId: %1, CellVoice CallId: %2\r\n
0xb0000139 | 3GPP2CallModel ignored disconnected call (CellVoice ID %1) due to existing call (CellVoice ID %2).\r\n
0xb000013a | Detected LTE System Type with no network registration and no voice domain.\r\n
0xb000013b | CallManager invoked I3GPP[2]CallModel::%1; asyncRequestId %2, Dialed Number: %3\r\n
0xb000013c | Update to call type or video context.  CallId: %1, CallType: %2, Video Context: %3\r\n
0xb000013d | CallModel3GPP2 CallVerb_SetVideoPaused; CallId: %1; paused: %2; completion context: %3\r\n
0xb000013e | CallModel3GPP CallVerb_SetVideoPaused; CallId: %1; paused: %2; async id: %3\r\n
0xb000013f | Enqueued verb SetVideoPaused, callid %1, paused %2, (completion context %3)\r\n
0xb0000140 | Dequeued verb SetVideoPaused, callid %1, paused %2, (completion context %3)\r\n
0xb0000141 | Video state update.  Params: %1, Action: %2, Direction: %3, State Params: %4, Peer caps: %5, Flags: %6, ContextID: %7\r\n
0xb0000142 | Calling Cellular API in media update for %1.  Async request id: %2, CallId %3, CellVoice CallId: %4)\r\n
0xb0000143 | Requesting video state publish.  Subscriber Number: %1, videoCapable: %2\r\n
0xb0000144 | Line type changed but SupService was not reset.\r\n
0xb0000145 | Registration state according to voice domain, voice domain: %1, registration status: %2, mapped registration state: %3\r\n
0xb0000146 | SubscriptionUpdate OMADM initiated : %1 HR = %2\r\n
0xb0000147 | Video direction override during multitasking, new transmit state: %1\r\n
0xb0000148 | CellularLine SetVideoCallingSetting: [CurrentState=%1][RequestType=%2][CacheSetting=%3][PerSimConfigAvailable=%4][TargetState=%5]\r\n
0xb0000149 | IMS system-type changing from %1 to %2\r\n
0xb000014a | Video media offer answer. Params: %1, Action: %2, Direction: %3, State Params: %4, Peer caps: %5, Flags: %6, ContextID: %7\r\n
0xb000014b | LineFactory->EndUpgradeOriginationCall(%1)\r\n
0xb000014c | LineFactory->CancelUpgrade(%1)\r\n
0xb000014d | ImsHandoverAttempt notify arrives. hrHandOverResult: %1, OldSystemType: %2, NewSystemType: %3\r\n
0xb000014e | GetVideoCapabilitySharingSettings: Queried, [LineId=%1][PerSimConfigAvaiable=%2][IsCapabilitySharingEnabled=%3][LastModifiedTimestamp=%4]\r\n
0xb000014f | SetVideoCapabilitySharingSettings: Updating, [LineId=%1][PerSimConfigAvaiable=%2][IsCapabilitySharingEnabled=%3][CurrentTimestamp=%4]\r\n
0xb0000150 | Applying video calling setting to saved or default user preference.\r\n
0xb0000151 | Unable to determine cached video calling setting.\r\n
0xb0000152 | Updated home MCC value from SIM in line specific data, [LineId=%1][HomeMcc=%2].\r\n
0xb0000153 | CallRecording: Phone service was notified of a Call Recording application whose Package Family Name is too long: '%1'\r\n
0xb0000155 | IMS service voice changed, [imsVoiceAvailable=%1][imsVideoAvailable=%2][videoCallingEnabled=%3]\r\n
0xb0000156 | IMS service video changed, [imsVoiceAvailable=%1][imsVideoAvailable=%2][videoCallingEnabled=%3]\r\n
0xb0000157 | DeterminePhoneSystemType, [imsVoiceSupported=%1][registration0SystemType=%2][registration0VoiceDomain=%3][callPresence=%4]\r\n
0xb0000158 | UpdateLineSystemType, [currentLineSystemType=%1][newLineSystemType=%2]\r\n
0xb0000159 | SetRadioAccessTechnology, [radioAccessTechnology=%1][toIms=%2][toGsm=%3][toCdma=%4][fromIms=%5][fromGsm=%6][fromCdma=%7]\r\n
0xb000015a | SetRadioAccessTechnology, switching call model, [To3GPP=%1]\r\n
0xb000015b | UpdateCallPresence, [currentPresence=%1][aggregatePresence=%2][allSameType=%3]\r\n
0xb000015c | [CallModel3GPP] Updating audio, [audioType=%1][audioActive=%2][anyCallNeedsAudio=%3][anyCallNeedsAudioActive=%4][localHoldSupported=%5]\r\n
0xb000015d | [CallModel3GPP2] Updating audio, [audioType=%1][shouldEnableAudio=%2][audioAllowed=%3]\r\n
0xb000015e | [CellularAudio] Updating audio for handover notification, [inProgress=%1][isHandoverNotification=%2][phase=%3][oldType=%4][newType=%5]\r\n
0xb000015f | ProcessHandoverNotification, [callInfoParams=%1][phase=%2][handoverStateParams=%3][oldType=%4][newType=%5][inProgress=%6]\r\n
0xb0000160 | Reset handover state\r\n
0xb0000161 | Updated video call conference state, [CallId=%1][CellVoiceCallId=%2][ContextId=%3][ConferenceContextId=%4][PreviousState=%5][UpdatedState=%6].\r\n
0xb0000162 | Interpret E_SUPSVCS_INVALIDREMOTEURI as success with call forwarding status disabled.\r\n
0xb0000163 | IR94FeatureDisabled: Disable video calling.\r\n
0xb0000164 | IR94FeatureDisabled: Force disable video calling.\r\n
0xb0000165 | Emergency call failed over. ECallId: %1.\r\n
0xb0000166 | Emergency call DisableAndEnable Audio from 3GPP CallModel. ECallId: %1.\r\n
0xb0000167 | Emergency call DisableAndEnable Audio from 3GPP2 CallModel. ECallId: %1.\r\n
0xb0000168 | HandleUICCPinLockStateChange, [dwParams=%1][dwLockState=%2]\r\n
0xb0000169 | Updating UICC related information from SIM\r\n
0xb000016a | OnSubscriberNumbersChange, [result=%1]\r\n
0xb000016b | [CallModel3GPP] Notified for IMS on Wifi flag, [m_imsOnWiFi=%1][onWiFi=%2]\r\n
0xb000016c | Removed stale pending RPC for line: %1, callid: %2, type: %3\r\n
0xb000016d | Timedout pending RPC for line: %1, callid: %2, type: %3\r\n
0xb000016e | ResetConnectionToApp for line: %1\r\n
0xb000016f | CleanupVoipAppConnectionState for line: %1, pendingRPCCalls: %2, voipAppProcessId: %3\r\n
0xb0000170 | VoIP Line Id: %1 has AboveLock extension: %2\r\n
0xb0000171 | Enqueued verb %1, (completion context %2)\r\n
0xb0000172 | Dequeued verb %1, (completion context %2)\r\n
0xb0000173 | CellularCallModel initiating explicit call transfer; asyncRequestId %1\r\n
0xb0000174 | Ril audio codec %1 mapped to %2 for CallId: %3.\r\n
0xb0000175 | [Voicemail] Stop VVM Invoked [stopReason=%1]\r\n
0xb0000176 | [Voicemail] Start VVM Invoked [last stopReason=%1]\r\n
0xb0000177 | LineFactory->ReserveVoipCallResources(%1, %3, %2) Completed.\r\n
0xb0000178 | LineFactory->CancelVoipCallResourceReservation(%1) Completed.\r\n
0xb0000179 | [VoipLine#%1] Calling LaunchVoipRtcTask(%3, %4, %2)\r\n
0xb000017a | [VoipLine#%1] Calling CancelVoipRtcTask(%2)\r\n
0xb000017b | [VoipLine#%1] Calling NotifyVoipActivityCompleted(%2)\r\n
0xb000017c | CallerId Prefix updated.  Updated number is %1.\r\n
0xb000017d | LineFactory->NewAcceptedCall(%1, %2)\r\n
0xb000017e | LineFactory->ShowAppUI(%1, %2)\r\n
0xb000017f | LineFactory->BackgroundVoipRestrictedCapabilityCheckFailed(%1)\r\n
0xb0000180 | Launching Voip app to show UI: VoipApp CallId: %1; Controller callId: %2\r\n
0xb0000181 | LineFactory->BackgroundVoipRestrictedCapabilityCheckAccessDenied(%1)\r\n
0xb000041b | Received IMS Failure changed, [imsFailureMessageType=%1].\r\n
0xb000041c | Ims failure error string is missing or empty.\r\n
0xb000041d | WiFi call disconnect occured, [errorMessage=%1] .\r\n
0xb000041e | WiFi internet connection status: %1.\r\n
0xb000041f | WiFi calling feature enabled: %1.\r\n
0xb0000420 | WiFi calling upsell suppressed: %1.\r\n
0xb0000421 | Media Configuration Data, Set Index: %1, IMS Service Type: %2, Media Preference: %3.\r\n
0xb0000422 | Placing request for switching cellular audio provider, Executor Index: %1, Old Audio type: %2, New Audio Type: %3.\r\n
0xb0000423 | [SupSvcsManager] Received MWI summary change notification [dwExecutor=%1][dwParams=%2][dwReferenceNumber=%3][dwTotalNumberOfDetailItems=%4][dwNumberOfSummaryItems=%5]\r\n
0xb0000424 | [SupSvcsManager] Received MWI details change notification [dwExecutor=%1][dwParams=%2][dwReferenceNumber=%3][dwNumberOfDetailItems=%4]\r\n
0xb0000425 | [SupSvcsManager] Handling MWI summary change notification [dwMwiType=%1][dwNumberOfNewMessages=%2][dwNumberOfOldMessages=%3][dwNumberOfNewUrgentMessages=%4][dwNumberOfOldUrgentMessages=%5]\r\n
0xb0000426 | [CellularLine] Received MWI summary change notification [dwReferenceNumber=%1][totalNewMessages=%2]\r\n
0xb0000427 | Ignore Caller ID Blocking Prefixes: %1\r\n
0xb0000428 | Caller ID blocking prefixes: %1\r\n
0xb0000429 | Ims Client added handler registered\r\n
0xb000042a | Ims Client added handler unregistered\r\n
0xb000042b | Ims client added: %1\r\n
0xb000042c | Ims Client removed handler registered\r\n
0xb000042d | Ims Client removed handler unregistered\r\n
0xb000042e | Ims client removed: %1\r\n
0xb000042f | Msti service new call handler registered\r\n
0xb0000430 | Msti service new call handler unregistered\r\n
0xb0000431 | MtsiNewCallHandler got new call notification for sipCallId %1; call status %2; direction %3; isConf %4\r\n
0xb0000432 | Msti call state changed handler registered\r\n
0xb0000433 | Msti call state changed handler unregistered\r\n
0xb0000434 | Ims service registered %1\r\n
0xb0000435 | Ims Line Dial outgoing call, callid %1, dial string %2\r\n
0xb0000436 | Ims Line AcceptIncoming, callid %1, (completion context %2)\r\n
0xb0000437 | Ims Line end the call, callid %1, (completion context %2)\r\n
0xb0000438 | Roaming override substitution performed for subscriber number. Roaming override = %1. Subscriber number = %2\r\n
0xb0000439 | Roaming override substitution not performed for subscriber number with international format. Roaming override = %1. Subscriber number = %2\r\n
0xb000043a | Received unsolicited notification, marking call as conference participant [CallId=%2][SupSvcCode=%1]\r\n
0xd0000001 | CallType_AudioOnly\r\n
0xd0000002 | CallType_AudioVideo\r\n
0xd0000003 | CallerIdOption_Default\r\n
0xd0000004 | CallerIdOption_ForceSend\r\n
0xd0000005 | CallerIdOption_ForceBlock\r\n
0xd0000006 | PH_CALLDIRECTION_INCOMING\r\n
0xd0000007 | PH_CALLDIRECTION_OUTGOING\r\n
0xd0000008 | PH_REGISTRATIONSTATE_UNKNOWN\r\n
0xd0000009 | PH_REGISTRATIONSTATE_UNREGISTERED_NO_SIGNAL\r\n
0xd000000a | PH_REGISTRATIONSTATE_UNREGISTERED_WITH_SIGNAL\r\n
0xd000000b | PH_REGISTRATIONSTATE_REGISTERING\r\n
0xd000000c | PH_REGISTRATIONSTATE_REGISTERING_AFTER_DENIED\r\n
0xd000000d | PH_REGISTRATIONSTATE_REGISTERED_HOME\r\n
0xd000000e | PH_REGISTRATIONSTATE_REGISTERED_ROAM\r\n
0xd000000f | PH_REGISTRATIONSTATE_DENIED\r\n
0xd0000010 | PH_REGISTRATIONSTATE_REGISTERED_ROAM_DOMESTIC\r\n
0xd0000011 | RIL_VOICE_DOMAIN_NONE\r\n
0xd0000012 | RIL_VOICE_DOMAIN_3GPP\r\n
0xd0000013 | RIL_VOICE_DOMAIN_3GPP2\r\n
0xd0000014 | RIL_VOICE_DOMAIN_IMS\r\n
0xd0000015 | RIL_CALLDIR_INCOMING\r\n
0xd0000016 | RIL_CALLDIR_OUTGOING\r\n
0xd0000017 | RIL_CPISTAT_UNKNOWN\r\n
0xd0000018 | RIL_CPISTAT_NEW_OUTGOING\r\n
0xd0000019 | RIL_CPISTAT_NEW_INCOMING\r\n
0xd000001a | RIL_CPISTAT_CONNECTED\r\n
0xd000001b | RIL_CPISTAT_DISCONNECTED\r\n
0xd000001c | RIL_CPISTAT_ONHOLD\r\n
0xd000001d | RIL_CPISTAT_MEDIA\r\n
0xd000001e | RIL_CPISTAT_HANDOVER\r\n
0xd000001f | RIL_CALL_SINGLEPARTY\r\n
0xd0000020 | RIL_CALL_MULTIPARTY\r\n
0xd0000021 | RIL_REMOTEPARTYINFO_VALID\r\n
0xd0000022 | RIL_REMOTEPARTYINFO_WITHHELD\r\n
0xd0000023 | RIL_REMOTEPARTYINFO_UNAVAILABLE\r\n
0xd0000024 | RIL_DISCINIT_UNKNOWN\r\n
0xd0000025 | RIL_DISCINIT_LOCAL\r\n
0xd0000026 | RIL_DISCINIT_REMOTE\r\n
0xd0000027 | RIL_DISCREASON_NULL\r\n
0xd0000028 | RIL_DISCREASON_BUSY\r\n
0xd0000029 | RIL_DISCREASON_NETWORKERROR\r\n
0xd000002a | RIL_DISCREASON_RADIOFADE\r\n
0xd000002b | RIL_DISCREASON_CONGESTION\r\n
0xd000002c | RIL_DISCREASON_EMERGENCYONLY\r\n
0xd000002d | RIL_DISCREASON_NOSERVICE\r\n
0xd000002e | RIL_DISCREASON_OTHEREXECUTORBUSY\r\n
0xd000002f | RIL_DISCREASON_EMERGENCYFAILOVER\r\n
0xd0000030 | RIL_DISCREASON_HANDOVER_MERGE\r\n
0xd0000031 | RIL_CALLTYPE_VOICE\r\n
0xd0000032 | RIL_CALLTYPE_DATA\r\n
0xd0000033 | RIL_CALLTYPE_FAX\r\n
0xd0000034 | RIL_CALLTYPE_PTT\r\n
0xd0000035 | RIL_CALLTYPE_VT\r\n
0xd0000036 | RIL_CALLTYPE_USSD\r\n
0xd0000037 | RIL_CALLTYPE_SUPSVC\r\n
0xd0000038 | RIL_CALLTYPE_IMS\r\n
0xd0000039 | RIL_CD_UNKNOWN_CAUSE\r\n
0xd000003a | RIL_CD_AS_CAUSE\r\n
0xd000003b | RIL_CD_3GPP_NETWORK_CAUSE\r\n
0xd000003c | RIL_CD_3GPP2_VENDOR_CAUSE\r\n
0xd000003d | RIL_CD_OTHER_CAUSE\r\n
0xd000003e | RIL_CD_3GPP_REJECT_CAUSE\r\n
0xd000003f | RIL_CD_IMS_SIP_CAUSE\r\n
0xd0000040 | RIL_EXTENDED_DISPLAY_TYPE_NORMAL\r\n
0xd0000041 | RIL_EXTENDED_DISPLAY_TAG_BLANK\r\n
0xd0000042 | RIL_EXTENDED_DISPLAY_TAG_SKIP\r\n
0xd0000043 | RIL_EXTENDED_DISPLAY_TAG_CONTINUATION\r\n
0xd0000044 | RIL_EXTENDED_DISPLAY_TAG_CALLED_ADDRESS\r\n
0xd0000045 | RIL_EXTENDED_DISPLAY_TAG_CAUSE\r\n
0xd0000046 | RIL_EXTENDED_DISPLAY_TAG_PROGRESS_INDICATOR\r\n
0xd0000047 | RIL_EXTENDED_DISPLAY_TAG_NOTIFICATION_INDICATOR\r\n
0xd0000048 | RIL_EXTENDED_DISPLAY_TAG_PROMPT\r\n
0xd0000049 | RIL_EXTENDED_DISPLAY_TAG_ACCUMULATED_DIGITS\r\n
0xd000004a | RIL_EXTENDED_DISPLAY_TAG_STATUS\r\n
0xd000004b | RIL_EXTENDED_DISPLAY_TAG_INBAND\r\n
0xd000004c | RIL_EXTENDED_DISPLAY_TAG_CALLING_ADDRESS\r\n
0xd000004d | RIL_EXTENDED_DISPLAY_TAG_REASON\r\n
0xd000004e | RIL_EXTENDED_DISPLAY_TAG_CALLING_PARTY_NAME\r\n
0xd000004f | RIL_EXTENDED_DISPLAY_TAG_CALLED_PARTY_NAME\r\n
0xd0000050 | RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NAME\r\n
0xd0000051 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NAME\r\n
0xd0000052 | RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NAME\r\n
0xd0000053 | RIL_EXTENDED_DISPLAY_TAG_ORIGINATING_RESTRICT\r\n
0xd0000054 | RIL_EXTENDED_DISPLAY_TAG_DATE_TIME_OF_DAY\r\n
0xd0000055 | RIL_EXTENDED_DISPLAY_TAG_CALL_APPEARANCE_ID\r\n
0xd0000056 | RIL_EXTENDED_DISPLAY_TAG_FEATURE_ADDRESS\r\n
0xd0000057 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NAME\r\n
0xd0000058 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NUMBER\r\n
0xd0000059 | RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NUMBER\r\n
0xd000005a | RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NUMBER\r\n
0xd000005b | RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NUMBER\r\n
0xd000005c | RIL_EXTENDED_DISPLAY_TAG_TEXT\r\n
0xd000005d | RIL_REGSTAT_UNKNOWN\r\n
0xd000005e | RIL_REGSTAT_UNREGISTERED\r\n
0xd000005f | RIL_REGSTAT_HOME\r\n
0xd0000060 | RIL_REGSTAT_ATTEMPTING\r\n
0xd0000061 | RIL_REGSTAT_DENIED\r\n
0xd0000062 | RIL_REGSTAT_ROAMING\r\n
0xd0000063 | RIL_REGSTAT_ROAMING_DOMESTIC\r\n
0xd0000064 | MODEM_POWER_OFF\r\n
0xd0000065 | MODEM_POWER_GOING_ON\r\n
0xd0000066 | MODEM_POWER_ON\r\n
0xd0000067 | MODEM_POWER_GOING_OFF\r\n
0xd0000068 | MODEM_POWER_SHUTTING_DOWN\r\n
0xd0000069 | RADIO_CONFIG_SINGLE\r\n
0xd000006a | RADIO_CONFIG_MULTI_MODE\r\n
0xd000006b | RADIO_CONFIG_1XCSFB\r\n
0xd000006c | RADIO_CONFIG_SVLTE\r\n
0xd000006d | RADIO_CONFIG_DualStandby\r\n
0xd000006e | RADIO_CONFIG_DualActive\r\n
0xd000006f | RADIO_CONFIG_SGLTE\r\n
0xd0000070 | RADIO_CONFIG_SVLTE_DUALACTIVE\r\n
0xd0000071 | RADIO_CONFIG_SGLTE_DUALACTIVE\r\n
0xd0000072 | RADIO_CONFIG_SRLTE\r\n
0xd0000073 | VoipIpcAudioRoute_Default\r\n
0xd0000074 | VoipIpcAudioRoute_Earpiece\r\n
0xd0000075 | VoipIpcAudioRoute_Speakerphone\r\n
0xd0000076 | VoipIpcAudioRoute_Bluetooth\r\n
0xd0000077 | RpcCallType_SetInitialAppState\r\n
0xd0000078 | RpcCallType_AcceptIncoming\r\n
0xd0000079 | RpcCallType_CallActive\r\n
0xd000007a | RpcCallType_End\r\n
0xd000007b | RpcCallType_Hold\r\n
0xd000007c | RpcCallType_RejectIncoming\r\n
0xd000007d | RpcCallType_Unhold\r\n
0xd000007e | RpcCallType_Mute\r\n
0xd000007f | RpcCallType_Unmute\r\n
0xd0000080 | RpcCallType_ForceEnd\r\n
0xd0000081 | PH_VOICEMAILPROVISIONINGSTATE_LEGACY_ONLY\r\n
0xd0000082 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_SUPPORTED\r\n
0xd0000083 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_CONFIGURED\r\n
0xd0000084 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_ENABLED\r\n
0xd0000085 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_ENABLED_NEW_USER\r\n
0xd0000086 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_NOT_FUNCTIONING\r\n
0xd0000087 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_CREATED\r\n
0xd0000088 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_PASSWORD_RESET\r\n
0xd0000089 | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_INITIALIZED\r\n
0xd000008a | PH_VOICEMAILPROVISIONINGSTATE_VISUAL_NO_DATA_AFFINITY\r\n
0xd000008b | StopVvmReason_Default\r\n
0xd000008c | StopVvmReason_DualSim_SingleLineVvm\r\n
0xd000008d | StopVvmReason_DualSim_NoDataAffinity\r\n
0xd000008e | RIL_3GPPTONE_TONEOFF\r\n
0xd000008f | RIL_3GPPTONE_RINGBACK\r\n
0xd0000090 | RIL_3GPPTONE_BUSY\r\n
0xd0000091 | RIL_3GPPTONE_CONGESTION\r\n
0xd0000092 | RIL_3GPPTONE_AUTHENTICATIONFAILURE\r\n
0xd0000093 | RIL_3GPPTONE_NUMBERUNOBTAINABLE\r\n
0xd0000094 | RIL_3GPPTONE_CALLDROPPED\r\n
0xd0000095 | RIL_3GPP2TONE_TONEOFF\r\n
0xd0000096 | RIL_3GPP2TONE_DIAL\r\n
0xd0000097 | RIL_3GPP2TONE_RINGBACK\r\n
0xd0000098 | RIL_3GPP2TONE_INTERCEPT\r\n
0xd0000099 | RIL_3GPP2TONE_ABRVINTERCEPT\r\n
0xd000009a | RIL_3GPP2TONE_REORDER\r\n
0xd000009b | RIL_3GPP2TONE_ABRVREORDER\r\n
0xd000009c | RIL_3GPP2TONE_BUSY\r\n
0xd000009d | RIL_3GPP2TONE_CONFIRM\r\n
0xd000009e | RIL_3GPP2TONE_ANSWER\r\n
0xd000009f | RIL_3GPP2TONE_CALLWAITING\r\n
0xd00000a0 | RIL_3GPP2TONE_PIP\r\n
0xd00000a1 | RIL_3GPP2ISDNALERTING_ALERTINGOFF\r\n
0xd00000a2 | RIL_3GPP2ISDNALERTING_NORMAL\r\n
0xd00000a3 | RIL_3GPP2ISDNALERTING_INTERGROUP\r\n
0xd00000a4 | RIL_3GPP2ISDNALERTING_SPECIAL\r\n
0xd00000a5 | RIL_3GPP2ISDNALERTING_PINGRING\r\n
0xd00000a6 | RIL_PERSOCHECKSTATE_NOTREADY\r\n
0xd00000a7 | RIL_PERSOCHECKSTATE_PASS\r\n
0xd00000a8 | RIL_PERSOCHECKSTATE_FAIL\r\n
0xd00000a9 | RIL_DEPERSOSTATE_READY\r\n
0xd00000aa | RIL_DEPERSOSTATE_CK_REQUIRED\r\n
0xd00000ab | RIL_DEPERSOSTATE_PUK_REQUIRED\r\n
0xd00000ac | RIL_DEPERSOSTATE_PUK_BLOCKED\r\n
0xd00000ad | No voicemail number found\r\n
0xd00000ae | SIM override key\r\n
0xd00000af | SIM data\r\n
0xd00000b0 | Default number cached in registry\r\n
0xd00000b1 | SIM fallback key\r\n
0xd00000b2 | Kind_None\r\n
0xd00000b3 | Kind_EmergencyModeChange\r\n
0xd00000b4 | Kind_ExitEmergencyModeFinished\r\n
0xd00000b5 | Kind_NetworkRegistrationChange\r\n
0xd00000b6 | Kind_SignalStrengthChange\r\n
0xd00000b7 | Kind_ModemPowerStateChange\r\n
0xd00000b8 | Kind_SubscriberNumberChange\r\n
0xd00000b9 | Kind_RegistryConfigChange\r\n
0xd00000ba | Kind_VoicemailNumberChangeRequest\r\n
0xd00000bb | Kind_VoicemailNumberSimSetCompleted\r\n
0xd00000bc | Kind_VoicemailNumberSimGetCompleted\r\n
0xd00000bd | Kind_Imsi\r\n
0xd00000be | Kind_SupServiceCallback\r\n
0xd00000bf | Kind_PinLockState\r\n
0xd00000c0 | Kind_SlotState\r\n
0xd00000c1 | Kind_SetCallerId\r\n
0xd00000c2 | Kind_ToneNotification\r\n
0xd00000c3 | Kind_CellBroadcastMessage\r\n
0xd00000c4 | Kind_GetLineCallForwardingStatusCompletion\r\n
0xd00000c5 | Kind_SetLineCallForwardingStatusCompletion\r\n
0xd00000c6 | Kind_GetLineCallForwardingNumberCompletion\r\n
0xd00000c7 | Kind_ServiceProviderNameChange\r\n
0xd00000c8 | Kind_PersoCheckStatus\r\n
0xd00000c9 | Kind_PersoDeactivationState\r\n
0xd00000ca | Kind_MuteStateChange\r\n
0xd00000cb | Kind_SlotCanAssociationsChanged\r\n
0xd00000cc | Kind_CallPresenceChanged\r\n
0xd00000cd | Kind_ImsStatusChanged\r\n
0xd00000ce | Kind_ImsSystemTypeChanged\r\n
0xd00000cf | Kind_RefreshVideoCallingSetting\r\n
0xd00000d0 | Kind_SetVideoCallingSetting\r\n
0xd00000d1 | Kind_SetVideoCallingSettingComplete\r\n
0xd00000d2 | Kind_GetVideoCallingSettingComplete\r\n
0xd00000d3 | Kind_GetPSMediaPreferencesComplete\r\n
0xd00000d4 | Kind_PSMediaPreferencesChanged\r\n
0xd00000d5 | RIL_SERVICE_UNKNOWN\r\n
0xd00000d6 | RIL_SERVICE_VOICE\r\n
0xd00000d7 | RIL_SERVICE_FAX\r\n
0xd00000d8 | RIL_SERVICE_OTHER\r\n
0xd00000d9 | FWDCODE_UNCONDITIONAL\r\n
0xd00000da | FWDCODE_BUSY\r\n
0xd00000db | FWDCODE_NOREPLY\r\n
0xd00000dc | FWDCODE_NOTREACHABLE\r\n
0xd00000dd | FWDCODE_ALL\r\n
0xd00000de | FWDCODE_ALLCONDITIONAL\r\n
0xd00000df | FWDCODE_STATECHANGED\r\n
0xd00000e0 | SimPinOperation_None\r\n
0xd00000e1 | SimPinOperation_EnableSimPin\r\n
0xd00000e2 | SimPinOperation_DisableSimPin\r\n
0xd00000e3 | SimPinOperation_ChangeSimPin\r\n
0xd00000e4 | SimPinOperation_UnlockSim\r\n
0xd00000e5 | SimPinOperation_UnblockSim\r\n
0xd00000e6 | PersoFeature_Unknown\r\n
0xd00000e7 | PersoFeature_None\r\n
0xd00000e8 | PersoFeature_3Gpp_Net\r\n
0xd00000e9 | PersoFeature_3Gpp_NetSub\r\n
0xd00000ea | PersoFeature_3Gpp_Sp\r\n
0xd00000eb | PersoFeature_3Gpp_Corp\r\n
0xd00000ec | PersoFeature_3Gpp_USim\r\n
0xd00000ed | PersoFeature_3Gpp2_NetType1\r\n
0xd00000ee | PersoFeature_3Gpp2_NetType2\r\n
0xd00000ef | PersoFeature_3Gpp2_Hrpd\r\n
0xd00000f0 | PersoFeature_3Gpp2_Sp\r\n
0xd00000f1 | PersoFeature_3Gpp2_Corp\r\n
0xd00000f2 | PersoFeature_3Gpp2_Uim\r\n
0xd00000f3 | DialAction_None\r\n
0xd00000f4 | DialAction_Activation\r\n
0xd00000f5 | DialAction_Deactivation\r\n
0xd00000f6 | DialAction_Interrogation\r\n
0xd00000f7 | DialAction_Registration\r\n
0xd00000f8 | DialAction_Erasure\r\n
0xd00000f9 | RIL_UNSSSCODE_FORWARDEDCALL\r\n
0xd00000fa | RIL_UNSSSCODE_CUGCALL\r\n
0xd00000fb | RIL_UNSSSCODE_CALLPUTONHOLD\r\n
0xd00000fc | RIL_UNSSSCODE_CALLRETRIEVED\r\n
0xd00000fd | RIL_UNSSSCODE_ENTEREDMULTIPARTY\r\n
0xd00000fe | RIL_UNSSSCODE_HELDCALLRELEASED\r\n
0xd00000ff | RIL_UNSSSCODE_FORWARDCHECKSS\r\n
0xd0000100 | RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER\r\n
0xd0000101 | RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER\r\n
0xd0000102 | RIL_UNSSSCODE_DEFLECTEDCALL\r\n
0xd0000103 | RIL_UNSSSCODE_ADDITIONALINCOMINGCF\r\n
0xd0000104 | RIL_UNSSSCODE_UNCONDITIONALCFACTIVE\r\n
0xd0000105 | RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE\r\n
0xd0000106 | RIL_UNSSSCODE_CALLWASFORWARDED\r\n
0xd0000107 | RIL_UNSSSCODE_CALLISWAITING\r\n
0xd0000108 | RIL_UNSSSCODE_OUTGOINGCALLSBARRED\r\n
0xd0000109 | RIL_UNSSSCODE_INCOMINGCALLSBARRED\r\n
0xd000010a | RIL_UNSSSCODE_CLIRSUPPRESSREJECT\r\n
0xd000010b | RIL_IMSSYSTEMTYPE_UNKNOWN\r\n
0xd000010c | RIL_IMSSYSTEMTYPE_WIFI\r\n
0xd000010d | RIL_IMSSYSTEMTYPE_LTE\r\n
0xd000010e | CallUpgradeSupportLevel_NotSupported\r\n
0xd000010f | CallUpgradeSupportLevel_NonSeamless\r\n
0xd0000110 | CallUpgradeSupportLevel_Seamless\r\n
0xd0000111 | CallUpgradeSupportLevel_AppDetermined\r\n
0xd0000112 | VideoCallingSetting_Disabled\r\n
0xd0000113 | VideoCallingSetting_Enabled\r\n
0xd0000114 | VideoCallingSetting_CachedValue\r\n
0xd0000115 | RIL_CALLMEDIADIRECTION_NONE\r\n
0xd0000116 | RIL_CALLMEDIADIRECTION_RX\r\n
0xd0000117 | RIL_CALLMEDIADIRECTION_TX\r\n
0xd0000118 | RIL_CALLMEDIADIRECTION_RXTX\r\n
0xd0000119 | RIL_CALLMEDIAOFFERACTION_NONE\r\n
0xd000011a | RIL_CALLMEDIAOFFERACTION_ERROR\r\n
0xd000011b | RIL_CALLMEDIAOFFERACTION_REJECT\r\n
0xd000011c | RIL_CALLMEDIAOFFERACTION_ASK\r\n
0xd000011d | RIL_CALLMEDIAOFFERACTION_ACCEPT\r\n
0xd000011e | RIL_CALLMEDIAOFFERACTION_CANCEL\r\n
0xd000011f | None\r\n
0xd0000120 | CircuitSwitched\r\n
0xd0000121 | PacketSwitched\r\n
0xd0000122 | PH_LINESYSTEMTYPE_GSM\r\n
0xd0000123 | PH_LINESYSTEMTYPE_CDMA\r\n
0xd0000124 | PH_LINESYSTEMTYPE_VOIP\r\n
0xd0000125 | PH_LINESYSTEMTYPE_UNKNOWN\r\n
0xd0000126 | PH_LINESYSTEMTYPE_IMS\r\n
0xd0000127 | CellularAudioType_None\r\n
0xd0000128 | CellularAudioType_CircuitSwitched\r\n
0xd0000129 | CellularAudioType_PacketSwitched\r\n
0xd000012a | CellularAudioType_PacketSwitched_WiFi\r\n
0xd000012b | RIL_CALLHANDOVERPHASE_STARTED\r\n
0xd000012c | RIL_CALLHANDOVERPHASE_COMPLETED\r\n
0xd000012d | RIL_CALLHANDOVERPHASE_FAILED\r\n
0xd000012e | RIL_CALLHANDOVERPHASE_CANCELLED\r\n
0xd000012f | None\r\n
0xd0000130 | Pending\r\n
0xd0000131 | Connected\r\n
0xd0000132 | PhoneMediaQuality_Unknown\r\n
0xd0000133 | PhoneMediaQuality_Low\r\n
0xd0000134 | PhoneMediaQuality_Standard\r\n
0xd0000135 | PhoneMediaQuality_High\r\n
0xd0000136 | PhoneMediaQuality_AMR_NB\r\n
0xd0000137 | PhoneMediaQuality_AMR_WB\r\n
0xd0000138 | PhoneMediaQuality_EVRC\r\n
0xd0000139 | PhoneMediaQuality_EVRC_B\r\n
0xd000013a | PhoneMediaQuality_EVRC_NW\r\n
0xd000013b | PhoneMediaQuality_EVRC_WB\r\n
0xd000013c | PhoneMediaQuality_EVS_FB\r\n
0xd000013d | PhoneMediaQuality_EVS_NB\r\n
0xd000013e | PhoneMediaQuality_EVS_SWB\r\n
0xd000013f | PhoneMediaQuality_EVS_WB\r\n
0xd0000140 | PhoneMediaQuality_GSM_EFR\r\n
0xd0000141 | PhoneMediaQuality_GSM_FR\r\n
0xd0000142 | PhoneMediaQuality_GSM_HR\r\n
0xd0000143 | PhoneMediaQuality_QCELP13K\r\n
0xd0000144 | PhoneMediaQuality_G711U\r\n
0xd0000145 | PhoneMediaQuality_G711A\r\n
0xd0000146 | PhoneMediaQuality_G722\r\n
0xd0000147 | PhoneMediaQuality_G723\r\n
0xd0000148 | PhoneMediaQuality_G729\r\n
0xd0000149 | RIL_IMSFAILUREMESSAGETYPE_REGISTER\r\n
0xd000014a | RIL_IMSFAILUREMESSAGETYPE_SUBSCRIBE\r\n
0xd000014b | RIL_IMSFAILUREMESSAGETYPE_INCALL\r\n
0xd000014c | RIL_PSMPREF_UNKNOWN\r\n
0xd000014d | RIL_PSMPREF_WIFIONLY\r\n
0xd000014e | RIL_PSMPREF_WIFIPREFERRED\r\n
0xd000014f | RIL_PSMPREF_CELLONLY\r\n
0xd0000150 | RIL_PSMPREF_CELLPREFERRED\r\n
0xd0000151 | RIL_MSGMWITYPE_NONE\r\n
0xd0000152 | RIL_MSGMWITYPE_VOICEMAIL\r\n
0xd0000153 | RIL_MSGMWITYPE_VIDEOMAIL\r\n
0xd0000154 | RIL_MSGMWITYPE_FAX\r\n
0xd0000155 | RIL_MSGMWITYPE_PAGER\r\n
0xd0000156 | RIL_MSGMWITYPE_MULTIMEDIA\r\n
0xd0000157 | RIL_MSGMWITYPE_TEXT\r\n
0xd0000158 | MtsiCallDirection_Incoming\r\n
0xd0000159 | MtsiCallDirection_Outgoing\r\n
0xd000015a | MtsiCallState_Offering\r\n
0xd000015b | MtsiCallState_Held\r\n
0xd000015c | MtsiCallState_Active\r\n
0xd000015d | MtsiCallState_Terminated\r\n
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
0xf000001a | CallVerb_ExplicitCallTransfer\r\n
0xf000001b | Dial\r\n
0xf000001c | End\r\n
0xf000001d | DropActiveAcceptHeld\r\n
0xf000001e | Hold\r\n
0xf000001f | Unhold\r\n
0xf0000020 | Swap\r\n
0xf0000021 | Private\r\n
0xf0000022 | Conference\r\n
0xf0000023 | Flash\r\n
0xf0000024 | RejectIncoming\r\n
0xf0000025 | AcceptIncoming\r\n
0xf0000026 | SendDtmf\r\n
0xf0000027 | StartDtmf\r\n
0xf0000028 | StopDtmf\r\n
0xf0000029 | DropFromConference\r\n
0xf000002a | DisableLocalVideo\r\n
0xf000002b | EnableLocalVideo\r\n
0xf000002c | AddVideo\r\n
0xf000002d | DropVideo\r\n
0xf000002e | AcceptIncomingVideo\r\n
0xf000002f | RejectIncomingVideo\r\n
0xf0000030 | SetVideoPaused\r\n
0xf0000031 | StartRecording\r\n
0xf0000032 | PauseRecording\r\n
0xf0000033 | StopRecording\r\n
0xf0000034 | ExplicitCallTransfer\r\n
0xf0000035 | RIL_PARAM_CI_EXECUTOR\r\n
0xf0000036 | RIL_PARAM_CI_ID\r\n
0xf0000037 | RIL_PARAM_CI_DIRECTION\r\n
0xf0000038 | RIL_PARAM_CI_STATUS\r\n
0xf0000039 | RIL_PARAM_CI_TYPE\r\n
0xf000003a | RIL_PARAM_CI_MULTIPARTY\r\n
0xf000003b | RIL_PARAM_CI_ADDRESS\r\n
0xf000003c | RIL_PARAM_CI_SUBADDRESS\r\n
0xf000003d | RIL_PARAM_CI_DESCRIPTION\r\n
0xf000003e | RIL_PARAM_CI_NUM_PRES_IND\r\n
0xf000003f | RIL_PARAM_CI_NAME_PRES_IND\r\n
0xf0000040 | RIL_PARAM_CI_FLAGS\r\n
0xf0000041 | RIL_PARAM_CI_DISCONNECTINITIATOR\r\n
0xf0000042 | RIL_PARAM_CI_DISCONNECTREASON\r\n
0xf0000043 | RIL_PARAM_CI_DISCONNECTDETAILS\r\n
0xf0000044 | RIL_PARAM_CI_OFFERANSWER\r\n
0xf0000045 | RIL_PARAM_CI_HANDOVERSTATE\r\n
0xf0000046 | RIL_PARAM_RPI_EXECUTOR\r\n
0xf0000047 | RIL_PARAM_RPI_ADDRESS\r\n
0xf0000048 | RIL_PARAM_RPI_SUBADDRESS\r\n
0xf0000049 | RIL_PARAM_RPI_DESCRIPTION\r\n
0xf000004a | RIL_PARAM_RPI_NUM_PRES_IND\r\n
0xf000004b | RIL_PARAM_RPI_NAME_PRES_IND\r\n
0xf000004c | RIL_PARAM_RPI_ID\r\n
0xf000004d | RIL_PARAM_ON_LONGNAME\r\n
0xf000004e | RIL_PARAM_ON_SHORTNAME\r\n
0xf000004f | RIL_PARAM_ON_NUMNAME\r\n
0xf0000050 | RIL_PARAM_ON_COUNTRY_CODE\r\n
0xf0000051 | RIL_PARAM_ON_SYSTEMTYPE\r\n
0xf0000052 | RIL_PARAM_NETWORKCODE_EXECUTOR\r\n
0xf0000053 | RIL_PARAM_NETWORKCODE_MCC\r\n
0xf0000054 | RIL_PARAM_NETWORKCODE_MNC\r\n
0xf0000055 | RIL_PARAM_NETWORKCODE_SID\r\n
0xf0000056 | RIL_PARAM_NETWORKCODE_NID\r\n
0xf0000057 | RIL_PARAM_NETWORKCODE_RI\r\n
0xf0000058 | RILCALLINFO_FLAG_ALIENCALL\r\n
0xf0000059 | RILCALLINFO_FLAG_EMERGENCYCALL\r\n
0xf000005a | RIL_PARAM_DISPLAY_EXECUTOR\r\n
0xf000005b | RIL_PARAM_DISPLAY_TYPE\r\n
0xf000005c | RIL_PARAM_DISPLAY_TAG\r\n
0xf000005d | RIL_PARAM_DISPLAY_MESSAGESIZE\r\n
0xf000005e | RIL_PARAM_DISPLAY_MESSAGE\r\n
0xf000005f | RIL_SYSTEMTYPE_1XRTT\r\n
0xf0000060 | RIL_SYSTEMTYPE_EVDO\r\n
0xf0000061 | RIL_SYSTEMTYPE_GSM\r\n
0xf0000062 | RIL_SYSTEMTYPE_UMTS\r\n
0xf0000063 | RIL_SYSTEMTYPE_LTE\r\n
0xf0000064 | RIL_SYSTEMTYPE_TDSCDMA\r\n
0xf0000065 | VoipIpcCallAttributes_VoiceOnly\r\n
0xf0000066 | VoipIpcCallAttributes_Video\r\n
0xf0000067 | RIL_PARAM_TONESIGNAL_GPPTONE\r\n
0xf0000068 | RIL_PARAM_TONESIGNAL_GPPTONE2\r\n
0xf0000069 | RIL_PARAM_TONESIGNAL_GPP2ISDNALERTING\r\n
0xf000006a | RIL_PARAM_TONESIGNAL_EXECUTOR\r\n
0xf000006b | RIL_PERSOFEATURE_NONE\r\n
0xf000006c | RIL_PERSOFEATURE_3GPP_NET\r\n
0xf000006d | RIL_PERSOFEATURE_3GPP_NETSUB\r\n
0xf000006e | RIL_PERSOFEATURE_3GPP_SP\r\n
0xf000006f | RIL_PERSOFEATURE_3GPP_CORP\r\n
0xf0000070 | RIL_PERSOFEATURE_3GPP_USIM\r\n
0xf0000071 | RIL_PERSOFEATURE_3GPP2_NETTYPE1\r\n
0xf0000072 | RIL_PERSOFEATURE_3GPP2_NETTYPE2\r\n
0xf0000073 | RIL_PERSOFEATURE_3GPP2_HRPD\r\n
0xf0000074 | RIL_PERSOFEATURE_3GPP2_SP\r\n
0xf0000075 | RIL_PERSOFEATURE_3GPP2_CORP\r\n
0xf0000076 | RIL_PERSOFEATURE_3GPP2_UIM\r\n
0xf0000077 | RIL_PARAM_PDS_STATE\r\n
0xf0000078 | RIL_PARAM_PDS_CK_ATTEMPTS\r\n
0xf0000079 | RIL_PARAM_PDS_PUK_ATTEMPTS\r\n
0xf000007a | RIL_PARAM_SI_ADDRESS\r\n
0xf000007b | RIL_PARAM_SI_DESCRIPTION\r\n
0xf000007c | RIL_PARAM_SI_SERVICE\r\n
0xf000007d | RIL_PARAM_IMSSTATUS_EXECUTOR\r\n
0xf000007e | RIL_PARAM_IMSSTATUS_HUICCAPP\r\n
0xf000007f | RIL_PARAM_IMSSTATUS_AVAILABLESERVICES\r\n
0xf0000080 | RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT\r\n
0xf0000081 | RIL_PARAM_IMSSTATUS_SERVINGDOMAIN\r\n
0xf0000082 | RIL_PARAM_IMSSTATUS_SYSTEMTYPE\r\n
0xf0000083 | RIL_IMS_SERVICE_SMS\r\n
0xf0000084 | RIL_IMS_SERVICE_VOICE\r\n
0xf0000085 | RIL_IMS_SERVICE_VIDEO\r\n
0xf0000086 | RIL_IMS_SERVICE_CUSTOM\r\n
0xf0000087 | RIL_IMS_SERVICE_SUPSVC\r\n
0xf0000088 | RIL_IMS_SERVICE_RCS\r\n
0xf0000089 | RIL_IMS_SERVICE_USSD\r\n
0xf000008a | RIL_IMS_SERVICE_E_VOICE\r\n
0xf000008b | RIL_PARAM_CMOA_ID\r\n
0xf000008c | RIL_PARAM_CMOA_CHANGE\r\n
0xf000008d | RIL_PARAM_CMOA_ACTION\r\n
0xf000008e | RIL_PARAM_CMOA_OLD_STATE\r\n
0xf000008f | RIL_PARAM_CMOA_NEW_STATE\r\n
0xf0000090 | RIL_PARAM_CALLVIDEO_PEERCAPABILITIES\r\n
0xf0000091 | RIL_PARAM_CALLVIDEO_FLAGS\r\n
0xf0000092 | RIL_CALLMEDIAVIDEOFLAG_CAPABILITY_UNKNOWN\r\n
0xf0000093 | RIL_CALLMEDIAVIDEOFLAG_PAUSE\r\n
0xf0000094 | RIL_PARAM_HANDOVER_PHASE\r\n
0xf0000095 | RIL_PARAM_HANDOVER_OLD_TYPE\r\n
0xf0000096 | RIL_PARAM_HANDOVER_NEW_TYPE\r\n
0xf0000097 | RIL_PARAM_HANDOVER_3GPPCAUSE\r\n
0xf0000098 | RIL_UICCLOCKSTATE_VERIFIED\r\n
0xf0000099 | RIL_UICCLOCKSTATE_ENABLED\r\n
0xf000009a | RIL_UICCLOCKSTATE_BLOCKED\r\n
0xf000009b | RIL_PARAM_UICCLOCKSTATE_UICCLOCK\r\n
0xf000009c | RIL_PARAM_UICCLOCKSTATE_LOCKSTATE\r\n
0xf000009d | RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT\r\n
0xf000009e | RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT\r\n
0xf000009f | RIL_PARAM_UAPCS_HUICCAPP\r\n
0xf00000a0 | RIL_PARAM_UAPCS_PERSOFEATURE\r\n
0xf00000a1 | RIL_PARAM_UAPCS_PERSOCHECKSTATE\r\n
0xf00000a2 | RIL_PARAM_MWISUMMARY_EXECUTOR\r\n
0xf00000a3 | RIL_PARAM_MWISUMMARY_REFNUM\r\n
0xf00000a4 | RIL_PARAM_MWISUMMARY_ACCTADDR\r\n
0xf00000a5 | RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS\r\n
0xf00000a6 | RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS\r\n
0xf00000a7 | RIL_PARAM_MWISUMMARY_SUMMARYITEMS\r\n
0xf00000a8 | RIL_PARAM_MWIDETAIL_EXECUTOR\r\n
0xf00000a9 | RIL_PARAM_MWIDETAIL_REFNUM\r\n
0xf00000aa | RIL_PARAM_MWIDETAIL_NUMDETAILITEMS\r\n
0xf00000ab | RIL_PARAM_MWIDETAIL_DETAILITEMS\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | [ERROR] originated HRESULT=%1 [%2 @ %3]\r\n
0xb0000002 | [ERROR] propagated HRESULT=%1 [%2 @ %3]\r\n
0xb0000094 | Cellvoice UICC Line set; sim swap pending: %1; old/new line ID: %2 / %3\r\n
0xb00000a3 | Read call forwarding state from registry. m_callForwardingState: %1; m_callForwardingAddress: %2\r\n
0xb00000d9 | LineFactory->CallEnded(%1, %2)\r\n
0xb0000131 | Set Can Focus result: %1\r\n
0xb0000139 | 3GPP2CallModel ignored disconnected call (CellVoice ID %1) due to existing call (CellVoice ID %2).\r\n
0xb000015b | UpdateCallPresence, [currentPresence=%1][aggregatePresence=%2][allSameType=%3]\r\n
0xb0000166 | Emergency call DisableAndEnable Audio from 3GPP CallModel. ECallId: %1.\r\n
0xb000016a | OnSubscriberNumbersChange, [result=%1]\r\n
0xb000016d | Timedout pending RPC for line: %1, callid: %2, type: %3\r\n
0xb000017d | LineFactory->NewAcceptedCall(%1, %2)\r\n
0xd0000001 | RpcCallType_SetInitialAppState\r\n
0xd0000002 | RpcCallType_AcceptIncoming\r\n
0xd0000003 | RpcCallType_CallActive\r\n
0xd0000004 | RpcCallType_End\r\n
0xd0000005 | RpcCallType_Hold\r\n
0xd0000006 | RpcCallType_RejectIncoming\r\n
0xd0000007 | RpcCallType_Unhold\r\n
0xd0000008 | RpcCallType_Mute\r\n
0xd0000009 | RpcCallType_Unmute\r\n
0xd000000a | RpcCallType_ForceEnd\r\n
0xd000000b | None\r\n
0xd000000c | CircuitSwitched\r\n
0xd000000d | PacketSwitched\r\n
