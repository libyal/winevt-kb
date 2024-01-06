## cellularapi.dll

Path: %SystemRoot%\System32\CellularAPI.dll

### 10.0.16299.15, 10.0.17134.1

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000003 | Information\r\n
0x10000004 | Trace\r\n
0x10000005 | UICC\r\n
0x10000006 | Reference Count Trace\r\n
0x10000007 | Function Trace\r\n
0x10000008 | OEM configuration\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-WindowsPhone-Net-Cellcore-CellularAPI\r\n
0xb0000064 | [CellularAPI] CellularAPI.dll is loaded\r\n
0xb0000065 | [CellularAPI] CellularAPI.dll is unloaded\r\n
0xb0000066 | [CellularAPI] %1: Unknown iType (%2)\r\n
0xb0000067 | [CellularAPI] Input pointer is NULL at line #%1\r\n
0xb0000068 | [CellularAPI] Out of memory at line #%1\r\n
0xb0000069 | [CellularAPI] %1: %2 fails synchronously with hr = %3\r\n
0xb000006a | [CellularAPI] %1: Invalid input arguments\r\n
0xb000006b | [CellularAPI] %1: Invalid data size (%2)\r\n
0xb000006c | [CellularAPI] %1: RIL API fails with hr = %2\r\n
0xb000006e | [CellularAPI] %1 is called\r\n
0xb000006f | [CellularAPI] %1 was called on %2 with ref=%3\r\n
0xb0000070 | [CellularAPI] %1: refcnt changed on %2 to ref=%3\r\n
0xb0000071 | [CellularAPI] %1: tagged refcnt(%2) changed on %3 to ref=%4\r\n
0xb0000072 | [CellularAPI] %1 was called when modem pointer was %2 with current object ref=%3\r\n
0xb0000073 | [CellularAPI] %1 was called with callback=%2 context=%3\r\n
0xb0000074 | [CellularAPI] OnUnregisterCompleted failed with hr %1. pCallback=%2, riid_of_callback=%3\r\n
0xb0000075 | [CellularAPI] EnableNotifiation for %1 failed wit hr = %2\r\n
0xb0000076 | [CellularAPI] Number of modem port ranges exceeded the RIL limit\r\n
0xb00000be | [CellularAPI] The IHVRIL version command failed with hr:%1\r\n
0xb00000bf | [CellularAPI] The IHVRIL version Major:%1, Minor:%2 is not supported\r\n
0xb00000c0 | [CellularAPI] The IHVRIL version Major:%1, Minor:%2 is supported\r\n
0xb00000c8 | [CellularAPI] CSlot::CSlot is created (%1)\r\n
0xb00000c9 | [CellularAPI] CSlot::CSlot is destructed (%1)\r\n
0xb00000ca | [CellularAPI] CSlot::Dispatch_HandleNotification: Input size (%1) is too small (< %2)\r\n
0xb00000cb | [CellularAPI] CSlot::Dispatch_HandleNotification: Either RILUICCSLOTINFO.dwParams & RIL_PARAM_SLOTINFO_NUMSLOTS) = %1 or input size (cbData = %2) is incorrect (!= %3 (cbSize) or %4 (offsetof))\r\n
0xb00000cc | [CellularAPI] CSlot::Dispatch_HandleNotification: The slot index (= %1) is greater than the number of slots (= %2) in RILUICCSLOTINFO.\r\n
0xb00000cd | [CellularAPI] CSlot::Dispatch_HandleNotification: Receive a notification with the same state %2 for the slot %1.\r\n
0xb000012c | [CellularAPI] CUICC::CUICC is created (%1)\r\n
0xb000012d | [CellularAPI] CUICC::CUICC is destructed (%1)\r\n
0xb000012e | [CellularAPI] CUicc::Dispatch_GetCardInfoCompletion: unknown app type (%1)\r\n
0xb000012f | [CellularAPI] CUicc::OnGetUICCInfoFinished: Invalid dwParams for RILUICCCARDINFO (dwParams = %1, fIsVirtualCard = %2)\r\n
0xb0000190 | [CellularAPI] CUICCApp::GetParametersFromRecordStatus: Invalid record type (%1)\r\n
0xb0000191 | [CellularAPI] %1: Incorrect command (%2)\r\n
0xb0000192 | [CellularAPI] CUICCApp::GetId: buffer length (%1) is too short (< MAXLENGTH_ICCID + MAXLENGTH_APPID + 1)\r\n
0xb0000193 | [CellularAPI] CUICCApp::GetFileMappingIndex: cannot find file mapping index (appType = %1, dwFileId = %2))\r\n
0xb0000194 | [CellularAPI] CUiccApp::GetParametersFromRecordStatus: Invalid operation (%1)\r\n
0xb0000195 | [CellularAPI] CUICCApp: CUICCApp is created (%1)\r\n
0xb0000196 | [CellularAPI] CUICCApp: CUICCApp is destructed (%1)\r\n
0xb00001f4 | [CellularAPI] CLine::CLine is created (%1)\r\n
0xb00001f5 | [CellularAPI] CLine::CLine is destructed (%1)\r\n
0xb00001f7 | [CellularAPI] CLine::OnGetIMSINumberCompletion: RegisterForIMSIChange called twice with callback %1 and context %2.\r\n
0xb00001f8 | [CellularAPI] CLine::OnGetVoicemailNumberCompletion: RegisterForVoicemailChange called twice with callback %1 and context %2.\r\n
0xb00001f9 | [CellularAPI] CLine::OnGetSubscriberNumbersCompletion: RegisterForSubscriberNumbersChange called twice with callback %1 and context %2.\r\n
0xb00001fa | [CellularAPI] CLine::VoiceMail EF returned %1. Trying legacy CPHS EF.\r\n
0xb00001fb | [CellularAPI] CLine::OnModemResetStateChanged: Modem reset state changed to [%1]\r\n
0xb00001fc | [CellularAPI] CLine::OnGetPRLIDCompletion: RegisterForPRLIDChange called twice with callback %1 and context %2.\r\n
0xb00001fd | [CellularAPI] CLine::OnGetPRLIDCompletion: PRLID Attempt [%1]: Modem returned default value [%2]\r\n
0xb00001fe | [CellularAPI] CLine::OnGetPRLIDCompletion: PRLID Attempts failed. Setting default value [%1]\r\n
0xb0000258 | [CellularAPI] CCellular: Initialization for modem at index %1 failed\r\n
0xb0000259 | [CellularAPI] CCellular: CCellular is created (%1)\r\n
0xb000025a | [CellularAPI] CCellular: CCellular is destructed (%1)\r\n
0xb000025b | [CellularAPI] CCellular: CCellular stopped listening for modems. CellularState: %2, ModemState: %3, Line: %1\r\n
0xb000025c | [CellularAPI] CCellular: CCellular UICC Datastore error %1 while accessing registry\r\n
0xb000025d | [CellularAPI] CCellular: OnModemShuttingDown failed with hr = %1 and pCallback = %2\r\n
0xb000025e | [CellularAPI] CCellular: Dispatch_Initialize ERIEnabled: %1, Algorithm:%2\r\n
0xb00002bc | [CellularAPI] RpcBindingCreateW failed with status %1\r\n
0xb00002bd | [CellularAPI] RpcBindingBind failed with status %1\r\n
0xb00002be | [CellularAPI] RpcBindingFree failed with status %1\r\n
0xb00002bf | [CellularAPI] Invalid Transport Security Descriptor\r\n
0xb00002c0 | [CellularAPI] Rpc exception = %1\r\n
0xb0000320 | [CellularAPI] SMS: Send sms message failed with hr %1, current segment count %2, useIms %3\r\n
0xb0000321 | [CellularAPI] SMS: Sending sms message using huiccapp %1, message type %2, useIms %3, executor: %4, options: %5\r\n
0xb0000322 | [CellularAPI] SMS: Loading OEM configuration from registry\r\n
0xb0000323 | [CellularAPI] SMS: Loading OEM registry key: Status: %1, Key: %2 %3, Value: %4\r\n
0xb0000324 | [CellularAPI] SMS: CalculateFragmentsInGSM: MessageLength:%1, DesiredDataEncoding:%2, TotalChars:%3, TotalPages:%4, MaxCharsPerSingleMessageSegment:%5, MaxCharsPerMultipartMessageSegment:%6, ActualOutputEncoding:%7, hrReturn:%8\r\n
0xb0000325 | [CellularAPI] SMS: CalculateFragmentsInCDMA: MessageLength:%1, DesiredDataEncoding:%2, TotalChars:%3, TotalPages:%4, MaxCharsPerSingleMessageSegment:%5, MaxCharsPerMultipartMessageSegment:%6, ActualOutputEncoding:%7, hrReturn:%8\r\n
0xb0000326 | [CellularAPI] SMS: CalcMessageSizeInfo: FragmentHeaderSizeBytes:%1, MaxFragmentSizeBytes:%2, FragmentBodySizeBytes:%3, FragmentBodySizeSeptets:%4\r\n
0xb0000327 | [CellularAPI] SMS: SendMessage: Attempts: %1, UseIms: %3, hr: %2\r\n
0xb0000328 | [CellularAPI] SMS: Registration changed. Current MCC: %1, system type: %2, voice domain: %3, huiccapp: %4, thisptr: %5\r\n
0xb0000329 | [CellularAPI] SMS: Received sms message with executor %1, huiccapp %2, simIndex %3, ackId %4, cbLineId %5, rgbLineId %6, message type %7\r\n
0xb000032a | [CellularAPI] SMS: RIL_SendMsgAck called for sms message with hr %1, executor %2, huiccapp %3, ackId %4, messageStatus %5, smsFormat %6, options %7\r\n
0xb000032b | [CellularAPI] SMS: Handled sms message with hr %1, executor %2, huiccapp %3, simIndex %4, ackId %5\r\n
0xb000032c | [CellularAPI] SMS: message recognized with hr %1, executor %2, ackId %3, partIndex %4, totalParts %5, cbLineId %6, rgbLineId %7, cbUid %8, rgbUid %9, type %10, delayAck %11\r\n
0xb000032d | [CellularAPI] SMS: message saved with hr %1, storelocation %2, partIndex %3, noOfParts %4, cuid %5, uid %6, cuiccappid %7, uiccappid %8, thisptr %9\r\n
0xb000032e | [CellularAPI] SMS: message read with hr %1, storelocation %2, partIndex %3, noOfParts %4, uid %6, cuiccappid %7, uiccappid %8, thisptr %9\r\n
0xb000032f | [CellularAPI] SMS: message is duplicate with partIndex %1, noOfParts %2, cuid %3, uid %4, cuiccappid %5, uiccappid %6, thisptr %7\r\n
0xb0000330 | [CellularAPI] SMS: message changed from ready to delivered clientAckId %1, noOfParts %2, cuid %, uid %4, thisptr %5\r\n
0xb0000331 | [CellularAPI] SMS: message acknowledged with clientAckId %1, thisptr %2\r\n
0xb0000332 | [CellularAPI] SMS: message expired cuid %1, uid %2, thisptr %3\r\n
0xb0000333 | [CellularAPI] SMS: message not acknowledged with clientAckId %1, thisptr %2\r\n
0xb0000334 | [CellularAPI] SMS: SmsModel operation %2 failed with hresult %1, thisptr %3\r\n
0xb0000335 | [CellularAPI] SMS: IMS status update received with executor %1, huiccapp %2, available services %3\r\n
0xb0000336 | [CellularAPI] SMS: Send sms message over IMS failed. Automatically retry. current_segment_count: %1, useIms: %2\r\n
0xb0000337 | [CellularAPI] SMS: Send sms message failed: hr: %1, current_segment_count: %2, useIms: %3, network_type: %4, error_type: %5, friendly_error_class: %6, error_code: %7, error_extended_info: %8\r\n
0xb0000338 | [CellularAPI] SMS: OEM Mapping for error code found in [%2] : error: %3 -> value: %4\r\n
0xb0000339 | [CellularAPI] SMS: Unsupported encoding type %1\r\n
0xb000033a | [CellularAPI] SMS: CalculateFragments: MessageLength:%1, TotalChars:%2, TotalPages:%3, MaxCharsPerSingleMessageSegment:%4, MaxCharsPerMultipartMessageSegment:%5, ActualOutputEncoding:%6, hrReturn:%7\r\n
0xb000033b | [CellularAPI] SMS: HResult: %1, registered for messaged of type: %2, thisPtr: %3, m_psmsstore: %4\r\n
0xb000033c | [CellularAPI] SMS: ThisPtr: %1 unregistered for messaged of type: %2\r\n
0xb000033d | [CellularAPI] SMS: CSMSModel: CSMSModel is created (%1), Executor %2, m_huiccapp %3, uiccid %4\r\n
0xb000033e | [CellularAPI] SMS: CSMSModel: CSMSModel is destructed (%1)\r\n
0xb000033f | [CellularAPI] SMS: CGenericSmsProvider: CGenericSmsProvider is created (%1)\r\n
0xb0000340 | [CellularAPI] SMS: CGenericSmsProvider: CGenericSmsProvider is destructed (%1)\r\n
0xb0000341 | [CellularAPI] SMS: Failure in processing message. hr: %3, Function: %1, Line: %2, ThisPtr: %4 \r\n
0xb0000342 | [CellularAPI] SMS: message with invalid teleservice. encoding(%1), teleservice(%2), executor(%3), partIndex(%4), totalParts(%5), cbLineId(%6), rgbLineId(%7), cbMessageUID(%8), rgbMessageUID(%9), type(%10)\r\n
0xb0000343 | [CellularAPI] SMS: Ack only message, ThisPtr: %1\r\n
0xb0000344 | [CellularAPI] SMS: Dropped App Port Message: Provider(%1), PortNum(%2), thisptr %3\r\n
0xb0000345 | [CellularAPI] SMS: Attemping to process a custom China Telecom (CT) WAP message, ThisPtr: %1.\r\n
0xb0000346 | [CellularAPI] SMS: Unknown RIL_MSGDLVSTATUS 0x%1\r\n
0xb0000347 | [CellularAPI] CCompletionClasses: Radio/Slot Configuration Check  - Function: %1, Checked Parameter: %2\r\n
0xb0000348 | [CellularAPI] CCompletionClasses: Verify Radio/Slot Configuration Check  - Function: %1\r\n
0xb0000349 | [CellularAPI] SMS: SmsStoreOpen. HR %1, ThisPtr %2, Filename %3\r\n
0xb000034a | [CellularAPI] SMS: SmsStoreCose. HR %1, ThisPtr %2\r\n
0xb000034b | [CellularAPI] SMS: Invalid huiccapp for received message. Executor: %1, MsgHuiccapp: %2, MsgIndex: %3, InstanceHuiccapp: %4, ImsHuiccapp: %5, ThisPtr: %6\r\n
0xb000034c | [CellularAPI] SMS: Delivering duplicate message with partIndex %1, noOfParts %2, cuid %3, uid %4, thisptr %5\r\n
0xb000034d | [CellularAPI] SMS: Incomplete message to ready queue with partIndex %1, noOfParts %2, cuid %3, uid %4, thisptr %5\r\n
0xb000034e | [CellularAPI] SMS: Using %1 to create new UID for message with partIndex %2, noOfParts %3, cuid %4, uid %5, thisptr %6\r\n
0xb000034f | [CellularAPI] SMS: Delivering SMS Message with ClientAckId: %1, MessagePtr: %2, Provider: %3\r\n
0xb0000350 | [CellularAPI] SMS: Delivered SMS Message with HRESULT: %1, MessagePtr: %2, Provider: %3\r\n
0xb0000357 | [CellularAPI] SMS: Failure in query of IMSI_CAN (%1) with NtStatus: %2\r\n
0xb0000358 | [CellularAPI] SMS: Failure in query of Line_CONFIG_CAN (%1) with NtStatus: %2\r\n
0xb0000359 | [CellularAPI] SMS: Error in CB for query of IMSI_CAN (%1), Length %2 Buffer %3\r\n
0xb000035a | [CellularAPI] SMS: Error in CB for query of Line_CONFIG_CAN (%1), Length %2 Buffer %3\r\n
0xb000035b | [CellularAPI] SMS: Multivariant WNF change notif with error (Buffer %1 Length %2)\r\n
0xb000035c | [CellularAPI] SMS: Multivariant WNF change notif (cSessions %1)\r\n
0xb000035d | [CellularAPI] SMS: Multivariant WNF change notif (Session# %1 idxSlot %2 State %3)\r\n
0xb000035e | [CellularAPI] SMS: WNF SubscribeError (tStatus: %1) for %2\r\n
0xb000035f | [CellularAPI] SMS: CellcoreSettingMigratorState WNF change notif with error (Buffer %1 Length %2)\r\n
0xb0000360 | [CellularAPI] SMS: CellcoreSettingMigratorState WNF change notif (state %1)\r\n
0xb0000361 | [CellularAPI] SMS: %1 for SMS Model. Client: %2, CCan: %3\r\n
0xb0000362 | [CellularAPI] SMS: %1 Client: %2, CSmsModel: %3, CCan: %4\r\n
0xb0000363 | [CellularAPI] SMS: SmsModel operation %1 succeeded\r\n
0xb0000364 | [CellularAPI] SMS: SetBroadcast retrying attempt (number of retries left %1)\r\n
0xb0000365 | [CellularAPI] SMS: SmsApp message processed: DoNotAckFlag(%1), AckOnlyFlag(%2), MessagePort(%3), Registered Ports(%5), thisptr(%6)\r\n
0xb0000366 | [CellularAPI] SMS: SmsBroadcast message processed: AckOnly(%1), Channel(%2), MCC(%3), Registered Channels(%5), thisptr(%6)\r\n
0xb0000367 | [CellularAPI] SMS: SmsBroadcast config Broadcast Types(%2), Channels(%4), thisptr(%5)\r\n
0xb0000368 | [CellularAPI] SMS: Broadcast message rejected as channel %1 is not enabled\r\n
0xb0000369 | [CellularAPI] SMS: Broadcast message rejected as channel %1 is not enabled. Mobile Country Code: %2\r\n
0xb000036a | [CellularAPI] SMS: Broadcast message rejected as the language (%1) on a multi-language channel (%2) does not match the device UI language (%3).\r\n
0xb000036b | [CellularAPI] SMS: The port (%1) doesn't match the standard WDP port (%2) for wap push.\r\n
0xb000036c | [CellularAPI] SMS: The SmsAppProvider was accepted by the port (%1).\r\n
0xb000036d | [CellularAPI] SMS: SmsAppMessages cannot be received on the standard WDP port (%1).\r\n
0xb000036e | [CellularAPI] SMS: Encoding %1 for CDMA is not currently supported.\r\n
0xb000036f | [CellularAPI] SMS: Encoding %1 is not valid, using % encoding instead.\r\n
0xb00003e8 | [CellularAPI] CCellularModem: Command %2 failed with hresult %1\r\n
0xb00003e9 | [CellularAPI] CCellularModem: CCellularModem is created (%1)\r\n
0xb00003ea | [CellularAPI] CCellularModem: CCellularModem is destructed (%1)\r\n
0xb00003eb | [CellularAPI] CCellularModem: Destroy thread is launched (pModem=%1)\r\n
0xb00003ec | [CellularAPI] CCellularModem: Destroy thread is finished (pModem=%1)\r\n
0xb00003ed | [CellularAPI] CCellularModem: Create Destroy thread (pModem=%1, ref=%2)\r\n
0xb00003ee | [CellularAPI] CCellularModem: Release pModem in Destroy thread (pModem=%1, ref=%2)\r\n
0xb00003ef | [CellularAPI] CCellularModem: QCN ERROR, Device Not Provisioned - OnRadioConfig Failed: hresult %1\r\n
0xb00003f0 | [CellularAPI] CCellularModem: Dispatch_CompleteDestroyModem is done (pModem=%1)\r\n
0xb00003f1 | [CellularAPI] CCellularModem: Attempt to use radio configuration at index [%1] while only [%2] configurations are available.\r\n
0xb00003f2 | [CellularAPI] CCellularModem: WaitForDestroyCompletion is called in Synchronizer.(pModem=%1)\r\n
0xb000044c | [CellularAPI] C3GPPCallModel: Attempt to start a new USSD session while another exists. New session attempted with - dwNetworkCCErrorCause = %1, dwNetworkSSErrorCause = %2, dwVendorErrorCause = %3 and dwStatus = %4\r\n
0xb000044d | [CellularAPI] C3GPPCallModel: Attempt to start a new USSD session while another exists. New session is NULL\r\n
0xb000044e | [CellularAPI] C3GPPCallModel: Started new USSD session with dwNetworkCCErrorCause = %1, dwNetworkSSErrorCause = %2, dwVendorErrorCause = %3 and dwStatus = %4\r\n
0xb000044f | [CellularAPI] C3GPPCallModel: Started new USSD session with NULL SupSvcData\r\n
0xb0000450 | [CellularAPI] C3GPPCallModel: USSD session terminated\r\n
0xb0000451 | [CellularAPI] C3GPPCallModel: Received USSD response with - dwNetworkCCErrorCause = %1, dwNetworkSSErrorCause = %2, dwVendorErrorCause = %3 and dwStatus = %4\r\n
0xb0000452 | [CellularAPI] C3GPPCallModel: C3GPPCallModel is created (%1)\r\n
0xb0000453 | [CellularAPI] C3GPPCallModel: C3GPPCallModel is destructed (%1)\r\n
0xb0000454 | [CellularAPI] C3GPP2CallModel: C3GPP2CallModel is created (%1)\r\n
0xb0000455 | [CellularAPI] C3GPP2CallModel: C3GPP2CallModel is destructed (%1)\r\n
0xb0000456 | [CellularAPI] CUnifiedCallModel: Publishing Call Forwarding state change (reason=%1, status=%2) result (%3).\r\n
0xb0000457 | [CellularAPI] CUnifiedCallModel: RIL_Dial is called successfully with executor %1.\r\n
0xb0000458 | [CellularAPI] CUnifiedCallModel: Duplicate call ID: [%1] while adding new active call.\r\n
0xb00004b0 | [CellularAPI] CCan: CCan is created (%1)\r\n
0xb00004b1 | [CellularAPI] CCan: CCan is destructed (%1)\r\n
0xb00004b2 | [CellularAPI] CCan: Calling SetExecutorConfig with zero HuiccApp\r\n
0xb00004b3 | [CellularAPI] CCan: Gets an error(%1) for SetExecutorConfig, but ignores because we have zero HuiccApp.\r\n
0xb00004b4 | [CellularAPI] CCan: Gets an error(%1) for SetExecutorConfig, but ignores because wmRil is older version.\r\n
0xb00004b5 | [CellularAPI] CCan: Sending registration status [%1] to clients.\r\n
0xb00004b6 | [CellularAPI] CCan: Postponing regStatus information because IMSI is not available.\r\n
0xb00004b7 | [CellularAPI] CCan: Error getting IMSI hresult=[%1].\r\n
0xb00004b8 | [CellularAPI] CCan: Suppressing out-of-order notification. Notification ID:#1, LastProcessed ID:#2.\r\n
0xb0000514 | [CellularAPI] CWnfSubscription: Could not unsubscribe WNF notification due to error (%1)\r\n
0xb0000515 | [CellularAPI] CWnfSubscription: Function: %1, Received Notification: %3, Callback: %4, Context: %5\r\n
0xb0000578 | [CellularAPI] CWnfContainer: Dropping WNF notification, client with callback %1 already unsubscribed\r\n
0xb0000640 | [CellularAPI] CAggregatedSlot::CAggregatedSlot is created (%1)\r\n
0xb0000641 | [CellularAPI] CAggregatedSlot::CAggregatedSlot is destructed (%1)\r\n
0xb0000642 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The virtual slot is empty\r\n
0xb0000643 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: Input size (%1) is too small (< %2)\r\n
0xb0000644 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: Either RILUICCSLOTINFO.dwParams & RIL_PARAM_SLOTINFO_NUMSLOTS) = %1 or input size (cbData = %2) is incorrect (!= %3 (cbSize) or %4 (offsetof))\r\n
0xb0000645 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The number of slots (%1) is not equal to 2\r\n
0xb0000646 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The previous virtual slot state = %1 and the current virtual slot state = %2\r\n
0xb0000647 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The current state of the aggregated slot (= %1) is neither ACTIVE nor NOT_READY\r\n
0xb0000648 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The current physical slot state is NOT_READY and its previous state (= %1) is NOT ACTIVE\r\n
0xb0000649 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The current physical slot state is NOT_READY and its previous state is ACTIVE\r\n
0xb000064a | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The current state of the aggregated slot is set to %1\r\n
0xb00006a4 | [CellularAPI] CAggregatedUICC::CAggregatedUICC is created (%1)\r\n
0xb00006a5 | [CellularAPI] CAggregatedUICC::CAggregatedUICC is destructed (%1)\r\n
0xb00006a6 | [CellularAPI] CAggregatedUICC::EmbeddedDispatch_GetCardInfoCompletion: GetCardInfo returns for slot %1 and m_cInfoCompletion = %2\r\n
0xb00006a7 | [CellularAPI] CAggregatedUICC::EmbeddedDispatch_GetCardInfoCompletion: The virtual card flag of slot %1 is TRUE\r\n
0xb00006a8 | [CellularAPI] CAggregatedUICC::EmbeddedDispatch_GetCardInfoCompletion: m_cInfoCompletion (= %1) != sc_cSlots (= %2) and wait for the apps on all the UICCs to be enumerated\r\n
0xd0000001 | NOINFOREQUIRED\r\n
0xd0000002 | FURTHERINFOREQUIRED\r\n
0xd0000003 | TIMEOUT\r\n
0xd0000004 | ERROR\r\n
0xd0000005 | RIL_FWDREASON_UNCONDITIONAL\r\n
0xd0000006 | RIL_FWDREASON_MOBILEBUSY\r\n
0xd0000007 | RIL_FWDREASON_NOREPLY\r\n
0xd0000008 | RIL_FWDREASON_UNREACHABLE\r\n
0xd0000009 | RIL_FWDREASON_ALLFORWARDING\r\n
0xd000000a | RIL_FWDREASON_ALLCONDITIONAL\r\n
0xd000000b | RIL_SVCSTAT_UNKNOWN\r\n
0xd000000c | RIL_SVCSTAT_DISABLED\r\n
0xd000000d | RIL_SVCSTAT_ENABLED\r\n
0xd000000e | RIL_SVCSTAT_DEFAULT\r\n
0xd000000f | RIL_E_PHONEFAILURE\r\n
0xd0000010 | RIL_E_NOCONNECTION\r\n
0xd0000011 | RIL_E_LINKRESERVED\r\n
0xd0000012 | RIL_E_OPNOTALLOWED\r\n
0xd0000013 | RIL_E_OPNOTSUPPORTED\r\n
0xd0000014 | RIL_E_UICCNOTINSERTED\r\n
0xd0000015 | RIL_E_UICCFAILURE\r\n
0xd0000016 | RIL_E_UICCBUSY\r\n
0xd0000017 | RIL_E_UICCWRONG\r\n
0xd0000018 | RIL_E_INCORRECTPASSWORD\r\n
0xd0000019 | RIL_E_MEMORYFULL\r\n
0xd000001a | RIL_E_INVALIDINDEX\r\n
0xd000001b | RIL_E_NOTFOUND\r\n
0xd000001c | RIL_E_MEMORYFAILURE\r\n
0xd000001d | RIL_E_TEXTSTRINGTOOLONG\r\n
0xd000001e | RIL_E_INVALIDTEXTSTRING\r\n
0xd000001f | RIL_E_DIALSTRINGTOOLONG\r\n
0xd0000020 | RIL_E_INVALIDDIALSTRING\r\n
0xd0000021 | RIL_E_NONETWORKSVC\r\n
0xd0000022 | RIL_E_NETWORKTIMEOUT\r\n
0xd0000023 | RIL_E_EMERGENCYONLY\r\n
0xd0000024 | RIL_E_TELEMATICIWUNSUPPORTED\r\n
0xd0000025 | RIL_E_SMTYPE0UNSUPPORTED\r\n
0xd0000026 | RIL_E_CANTREPLACEMSG\r\n
0xd0000027 | RIL_E_PROTOCOLIDERROR\r\n
0xd0000028 | RIL_E_DCSUNSUPPORTED\r\n
0xd0000029 | RIL_E_MSGCLASSUNSUPPORTED\r\n
0xd000002a | RIL_E_DCSERROR\r\n
0xd000002b | RIL_E_CMDCANTBEACTIONED\r\n
0xd000002c | RIL_E_CMDUNSUPPORTED\r\n
0xd000002d | RIL_E_CMDERROR\r\n
0xd000002e | RIL_E_MSGBODYHEADERERROR\r\n
0xd000002f | RIL_E_SCBUSY\r\n
0xd0000030 | RIL_E_NOSCSUBSCRIPTION\r\n
0xd0000031 | RIL_E_SCSYSTEMFAILURE\r\n
0xd0000032 | RIL_E_INVALIDADDRESS\r\n
0xd0000033 | RIL_E_DESTINATIONBARRED\r\n
0xd0000034 | RIL_E_REJECTEDDUPLICATE\r\n
0xd0000035 | RIL_E_VPFUNSUPPORTED\r\n
0xd0000036 | RIL_E_VPUNSUPPORTED\r\n
0xd0000037 | RIL_E_UICCMSGSTORAGEFULL\r\n
0xd0000038 | RIL_E_NOUICCMSGSTORAGE\r\n
0xd0000039 | RIL_E_UICCTOOLKITBUSY\r\n
0xd000003a | RIL_E_UICCDOWNLOADERROR\r\n
0xd000003b | RIL_E_MSGSVCRESERVED\r\n
0xd000003c | RIL_E_INVALIDMSGPARAM\r\n
0xd000003d | RIL_E_INVALIDSCADDRESS\r\n
0xd000003e | RIL_E_UNASSIGNEDNUMBER\r\n
0xd000003f | RIL_E_MSGBARREDBYOPERATOR\r\n
0xd0000040 | RIL_E_MSGCALLBARRED\r\n
0xd0000041 | RIL_E_MSGXFERREJECTED\r\n
0xd0000042 | RIL_E_DESTINATIONOUTOFSVC\r\n
0xd0000043 | RIL_E_UNIDENTIFIEDSUBCRIBER\r\n
0xd0000044 | RIL_E_SVCUNSUPPORTED\r\n
0xd0000045 | RIL_E_UNKNOWNSUBSCRIBER\r\n
0xd0000046 | RIL_E_NETWKOUTOFORDER\r\n
0xd0000047 | RIL_E_NETWKTEMPFAILURE\r\n
0xd0000048 | RIL_E_CONGESTION\r\n
0xd0000049 | RIL_E_RESOURCESUNAVAILABLE\r\n
0xd000004a | RIL_E_SVCNOTSUBSCRIBED\r\n
0xd000004b | RIL_E_SVCNOTIMPLEMENTED\r\n
0xd000004c | RIL_E_INVALIDMSGREFERENCE\r\n
0xd000004d | RIL_E_INVALIDMSG\r\n
0xd000004e | RIL_E_INVALIDMANDATORYINFO\r\n
0xd000004f | RIL_E_MSGTYPEUNSUPPORTED\r\n
0xd0000050 | RIL_E_ICOMPATIBLEMSG\r\n
0xd0000051 | RIL_E_INFOELEMENTUNSUPPORTED\r\n
0xd0000052 | RIL_E_PROTOCOLERROR\r\n
0xd0000053 | RIL_E_NETWORKERROR\r\n
0xd0000054 | RIL_E_MESSAGINGERROR\r\n
0xd0000055 | RIL_E_NOTREADY\r\n
0xd0000056 | RIL_E_TIMEDOUT\r\n
0xd0000057 | RIL_E_CANCELLED\r\n
0xd0000058 | RIL_E_NONOTIFYCALLBACK\r\n
0xd0000059 | RIL_E_OPFMTUNAVAILABLE\r\n
0xd000005a | RIL_E_NORESPONSETODIAL\r\n
0xd000005b | RIL_E_SECURITYFAILURE\r\n
0xd000005c | RIL_E_RADIOFAILEDINIT\r\n
0xd000005d | RIL_E_DRIVERINITFAILED\r\n
0xd000005e | RIL_E_RADIONOTPRESENT\r\n
0xd000005f | RIL_E_RADIOOFF\r\n
0xd0000060 | RIL_E_ILLEGALMS\r\n
0xd0000061 | RIL_E_ILLEGALME\r\n
0xd0000062 | RIL_E_GPRSSERVICENOTALLOWED\r\n
0xd0000063 | RIL_E_PLMNNOTALLOWED\r\n
0xd0000064 | RIL_E_LOCATIONAREANOTALLOWED\r\n
0xd0000065 | RIL_E_ROAMINGNOTALLOWEDINTHISLOCATIONAREA\r\n
0xd0000066 | RIL_E_SERVICEOPTIONNOTSUPPORTED\r\n
0xd0000067 | RIL_E_REQUESTEDSERVICEOPTIONNOTSUBSCRIBED\r\n
0xd0000068 | RIL_E_SERVICEOPTIONTEMPORARILYOUTOFORDER\r\n
0xd0000069 | RIL_E_PDPAUTHENTICATIONFAILURE\r\n
0xd000006a | RIL_E_INVALIDMOBILECLASS\r\n
0xd000006b | RIL_E_UNSPECIFIEDGPRSERROR\r\n
0xd000006c | RIL_E_RADIOREBOOTED\r\n
0xd000006d | RIL_E_INVALIDCONTEXTSTATE\r\n
0xd000006e | RIL_E_MAXCONTEXTS\r\n
0xd000006f | RIL_E_SYNCHRONOUS_DATA_UNAVAILABLE\r\n
0xd0000070 | RIL_E_FDNRESTRICT\r\n
0xd0000071 | RIL_E_INVALIDASYNCCOMMANDRESPONSE\r\n
0xd0000072 | RIL_E_INCOMPATIBLEPROXYDRIVER\r\n
0xd0000073 | RIL_E_INVALIDDRIVERVERSION\r\n
0xd0000074 | RIL_E_USIMCALLMODIFIED\r\n
0xd0000075 | RIL_E_PASSWORDMISMATCH\r\n
0xd0000076 | RIL_E_INVALIDCONTEXTACTIVATIONSTRING\r\n
0xd0000077 | RIL_E_UICCAPPINACCESSIBLE\r\n
0xd0000078 | RIL_E_UICCPINREQUIRED\r\n
0xd0000079 | RIL_E_UICCPUKREQUIRED\r\n
0xd000007a | RIL_E_UICCPUKBLOCKED\r\n
0xd000007b | RIL_E_EXECUTORNOTREADY\r\n
0xd000007c | RIL_E_INVALIDUICCKEYREF\r\n
0xd000007d | RIL_E_UICCINACTIVE\r\n
0xd000007e | RIL_E_PERSOPUKREQUIRED\r\n
0xd000007f | RIL_E_PERSOPUKBLOCKED\r\n
0xd0000080 | RIL_E_PERSOCHECKFAILED\r\n
0xd0000081 | RIL_E_INVALIDUICCPATH\r\n
0xd0000082 | RIL_E_IMSTEMPFAILURE\r\n
0xd0000083 | RIL_E_UICCNOTREADY\r\n
0xd0000084 | RIL_E_UICCPOWEROFF\r\n
0xd0000085 | RIL_E_CALLISACTIVE\r\n
0xd0000086 | RIL_E_USIMCALLBLOCKED\r\n
0xd0000087 | RIL_E_UICCADMRESTRICTED\r\n
0xd0000088 | RIL_E_DMSERVICENOTREADY\r\n
0xd0000089 | RIL_E_DMGETCONFIGFAILED\r\n
0xd000008a | RIL_E_DMCOMMITFAILED\r\n
0xd000008b | RIL_E_OTHEREXECUTORBUSY\r\n
0xd000008c | RIL_E_IMSNOHANDOVERTARGETFOUND\r\n
0xd000008d | RIL_E_VCCHANDOVERINPROGRESS\r\n
0xd000008e | RIL_E_INVALIDREMOTEURI\r\n
0xd000008f | RIL_MODEMRESETSTATE_STARTED\r\n
0xd0000090 | RIL_MODEMRESETSTATE_RECOVERED\r\n
0xd0000091 | RIL_MODEMRESETSTATE_FAILED\r\n
0xd0000092 | Registered\r\n
0xd0000093 | Unregistered\r\n
0xd0000094 | OFF_EMPTY\r\n
0xd0000095 | OFF\r\n
0xd0000096 | Empty\r\n
0xd0000097 | NOT_READY\r\n
0xd0000098 | ACTIVE\r\n
0xd0000099 | ERROR\r\n

### 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000003 | Information\r\n
0x10000004 | Trace\r\n
0x10000005 | UICC\r\n
0x10000006 | Reference Count Trace\r\n
0x10000007 | Function Trace\r\n
0x10000008 | OEM configuration\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-WindowsPhone-Net-Cellcore-CellularAPI\r\n
0x90000002 | CellularAPI Debug Channel\r\n
0xb0000064 | [CellularAPI] CellularAPI.dll is loaded\r\n
0xb0000065 | [CellularAPI] CellularAPI.dll is unloaded\r\n
0xb0000066 | [CellularAPI] %1: Unknown iType (%2)\r\n
0xb0000067 | [CellularAPI] Input pointer is NULL at line #%1\r\n
0xb0000068 | [CellularAPI] Out of memory at line #%1\r\n
0xb0000069 | [CellularAPI] %1: %2 fails synchronously with hr = %3\r\n
0xb000006a | [CellularAPI] %1: Invalid input arguments\r\n
0xb000006b | [CellularAPI] %1: Invalid data size (%2)\r\n
0xb000006c | [CellularAPI] %1: RIL API fails with hr = %2\r\n
0xb000006e | [CellularAPI] %1 is called\r\n
0xb000006f | [CellularAPI] %1 was called on %2 with ref=%3\r\n
0xb0000070 | [CellularAPI] %1: refcnt changed on %2 to ref=%3\r\n
0xb0000071 | [CellularAPI] %1: tagged refcnt(%2) changed on %3 to ref=%4\r\n
0xb0000072 | [CellularAPI] %1 was called when modem pointer was %2 with current object ref=%3\r\n
0xb0000073 | [CellularAPI] %1 was called with callback=%2 context=%3\r\n
0xb0000074 | [CellularAPI] OnUnregisterCompleted failed with hr %1. pCallback=%2, riid_of_callback=%3\r\n
0xb0000075 | [CellularAPI] EnableNotifiation for %1 failed wit hr = %2\r\n
0xb0000076 | [CellularAPI] Number of modem port ranges exceeded the RIL limit\r\n
0xb00000be | [CellularAPI] The IHVRIL version command failed with hr:%1\r\n
0xb00000bf | [CellularAPI] The IHVRIL version Major:%1, Minor:%2 is not supported\r\n
0xb00000c0 | [CellularAPI] The IHVRIL version Major:%1, Minor:%2 is supported\r\n
0xb00000c8 | [CellularAPI] CSlot::CSlot is created (%1)\r\n
0xb00000c9 | [CellularAPI] CSlot::CSlot is destructed (%1)\r\n
0xb00000ca | [CellularAPI] CSlot::Dispatch_HandleNotification: Input size (%1) is too small (< %2)\r\n
0xb00000cb | [CellularAPI] CSlot::Dispatch_HandleNotification: Either RILUICCSLOTINFO.dwParams & RIL_PARAM_SLOTINFO_NUMSLOTS) = %1 or input size (cbData = %2) is incorrect (!= %3 (cbSize) or %4 (offsetof))\r\n
0xb00000cc | [CellularAPI] CSlot::Dispatch_HandleNotification: The slot index (= %1) is greater than the number of slots (= %2) in RILUICCSLOTINFO.\r\n
0xb00000cd | [CellularAPI] CSlot::Dispatch_HandleNotification: Receive a notification with the same state %2 for the slot %1.\r\n
0xb000012c | [CellularAPI] CUICC::CUICC is created (%1)\r\n
0xb000012d | [CellularAPI] CUICC::CUICC is destructed (%1)\r\n
0xb000012e | [CellularAPI] CUicc::Dispatch_GetCardInfoCompletion: unknown app type (%1)\r\n
0xb000012f | [CellularAPI] CUicc::OnGetUICCInfoFinished: Invalid dwParams for RILUICCCARDINFO (dwParams = %1, fIsVirtualCard = %2)\r\n
0xb0000190 | [CellularAPI] CUICCApp::GetParametersFromRecordStatus: Invalid record type (%1)\r\n
0xb0000191 | [CellularAPI] %1: Incorrect command (%2)\r\n
0xb0000192 | [CellularAPI] CUICCApp::GetId: buffer length (%1) is too short (< MAXLENGTH_ICCID + MAXLENGTH_APPID + 1)\r\n
0xb0000193 | [CellularAPI] CUICCApp::GetFileMappingIndex: cannot find file mapping index (appType = %1, dwFileId = %2))\r\n
0xb0000194 | [CellularAPI] CUiccApp::GetParametersFromRecordStatus: Invalid operation (%1)\r\n
0xb0000195 | [CellularAPI] CUICCApp: CUICCApp is created (%1)\r\n
0xb0000196 | [CellularAPI] CUICCApp: CUICCApp is destructed (%1)\r\n
0xb00001f4 | [CellularAPI] CLine::CLine is created (%1)\r\n
0xb00001f5 | [CellularAPI] CLine::CLine is destructed (%1)\r\n
0xb00001f7 | [CellularAPI] CLine::OnGetIMSINumberCompletion: RegisterForIMSIChange called twice with callback %1 and context %2.\r\n
0xb00001f8 | [CellularAPI] CLine::OnGetVoicemailNumberCompletion: RegisterForVoicemailChange called twice with callback %1 and context %2.\r\n
0xb00001f9 | [CellularAPI] CLine::OnGetSubscriberNumbersCompletion: RegisterForSubscriberNumbersChange called twice with callback %1 and context %2.\r\n
0xb00001fa | [CellularAPI] CLine::VoiceMail EF returned %1. Trying legacy CPHS EF.\r\n
0xb00001fb | [CellularAPI] CLine::OnModemResetStateChanged: Modem reset state changed to [%1]\r\n
0xb00001fc | [CellularAPI] CLine::OnGetPRLIDCompletion: RegisterForPRLIDChange called twice with callback %1 and context %2.\r\n
0xb00001fd | [CellularAPI] CLine::OnGetPRLIDCompletion: PRLID Attempt [%1]: Modem returned default value [%2]\r\n
0xb00001fe | [CellularAPI] CLine::OnGetPRLIDCompletion: PRLID Attempts failed. Setting default value [%1]\r\n
0xb0000258 | [CellularAPI] CCellular: Initialization for modem at index %1 failed\r\n
0xb0000259 | [CellularAPI] CCellular: CCellular is created (%1)\r\n
0xb000025a | [CellularAPI] CCellular: CCellular is destructed (%1)\r\n
0xb000025b | [CellularAPI] CCellular: CCellular stopped listening for modems. CellularState: %2, ModemState: %3, Line: %1\r\n
0xb000025c | [CellularAPI] CCellular: CCellular UICC Datastore error %1 while accessing registry\r\n
0xb000025d | [CellularAPI] CCellular: OnModemShuttingDown failed with hr = %1 and pCallback = %2\r\n
0xb000025e | [CellularAPI] CCellular: Dispatch_Initialize ERIEnabled: %1, Algorithm:%2\r\n
0xb00002bc | [CellularAPI] RpcBindingCreateW failed with status %1\r\n
0xb00002bd | [CellularAPI] RpcBindingBind failed with status %1\r\n
0xb00002be | [CellularAPI] RpcBindingFree failed with status %1\r\n
0xb00002bf | [CellularAPI] Invalid Transport Security Descriptor\r\n
0xb00002c0 | [CellularAPI] Rpc exception = %1\r\n
0xb0000320 | [CellularAPI] SMS: Send sms message failed with hr %1, current segment count %2, useIms %3\r\n
0xb0000321 | [CellularAPI] SMS: Sending sms message using huiccapp %1, message type %2, useIms %3, executor: %4, options: %5\r\n
0xb0000322 | [CellularAPI] SMS: Loading OEM configuration from registry\r\n
0xb0000323 | [CellularAPI] SMS: Loading OEM registry key: Status: %1, Key: %2 %3, Value: %4\r\n
0xb0000324 | [CellularAPI] SMS: CalculateFragmentsInGSM: MessageLength:%1, DesiredDataEncoding:%2, TotalChars:%3, TotalPages:%4, MaxCharsPerSingleMessageSegment:%5, MaxCharsPerMultipartMessageSegment:%6, ActualOutputEncoding:%7, hrReturn:%8\r\n
0xb0000325 | [CellularAPI] SMS: CalculateFragmentsInCDMA: MessageLength:%1, DesiredDataEncoding:%2, TotalChars:%3, TotalPages:%4, MaxCharsPerSingleMessageSegment:%5, MaxCharsPerMultipartMessageSegment:%6, ActualOutputEncoding:%7, hrReturn:%8\r\n
0xb0000326 | [CellularAPI] SMS: CalcMessageSizeInfo: FragmentHeaderSizeBytes:%1, MaxFragmentSizeBytes:%2, FragmentBodySizeBytes:%3, FragmentBodySizeSeptets:%4\r\n
0xb0000327 | [CellularAPI] SMS: SendMessage: Attempts: %1, UseIms: %3, hr: %2\r\n
0xb0000328 | [CellularAPI] SMS: Registration changed. Current MCC: %1, system type: %2, voice domain: %3, huiccapp: %4, thisptr: %5\r\n
0xb0000329 | [CellularAPI] SMS: Received sms message with executor %1, huiccapp %2, simIndex %3, ackId %4, cbLineId %5, rgbLineId %6, message type %7\r\n
0xb000032a | [CellularAPI] SMS: RIL_SendMsgAck called for sms message with hr %1, executor %2, huiccapp %3, ackId %4, messageStatus %5, smsFormat %6, options %7\r\n
0xb000032b | [CellularAPI] SMS: Handled sms message with hr %1, executor %2, huiccapp %3, simIndex %4, ackId %5\r\n
0xb000032c | [CellularAPI] SMS: message recognized with hr %1, executor %2, ackId %3, partIndex %4, totalParts %5, cbLineId %6, rgbLineId %7, cbUid %8, rgbUid %9, type %10, delayAck %11\r\n
0xb000032d | [CellularAPI] SMS: message saved with hr %1, storelocation %2, partIndex %3, noOfParts %4, cuid %5, uid %6, cuiccappid %7, uiccappid %8, thisptr %9\r\n
0xb000032e | [CellularAPI] SMS: message read with hr %1, storelocation %2, partIndex %3, noOfParts %4, uid %6, cuiccappid %7, uiccappid %8, thisptr %9\r\n
0xb000032f | [CellularAPI] SMS: message is duplicate with partIndex %1, noOfParts %2, cuid %3, uid %4, cuiccappid %5, uiccappid %6, thisptr %7\r\n
0xb0000330 | [CellularAPI] SMS: message changed from ready to delivered clientAckId %1, noOfParts %2, cuid %, uid %4, thisptr %5\r\n
0xb0000331 | [CellularAPI] SMS: message acknowledged with clientAckId %1, thisptr %2\r\n
0xb0000332 | [CellularAPI] SMS: message expired cuid %1, uid %2, thisptr %3\r\n
0xb0000333 | [CellularAPI] SMS: message not acknowledged with clientAckId %1, thisptr %2\r\n
0xb0000334 | [CellularAPI] SMS: SmsModel operation %2 failed with hresult %1, thisptr %3\r\n
0xb0000335 | [CellularAPI] SMS: IMS status update received with executor %1, huiccapp %2, available services %3\r\n
0xb0000336 | [CellularAPI] SMS: Send sms message over IMS failed. Automatically retry. current_segment_count: %1, useIms: %2\r\n
0xb0000337 | [CellularAPI] SMS: Send sms message failed: hr: %1, current_segment_count: %2, useIms: %3, network_type: %4, error_type: %5, friendly_error_class: %6, error_code: %7, error_extended_info: %8\r\n
0xb0000338 | [CellularAPI] SMS: OEM Mapping for error code found in [%2] : error: %3 -> value: %4\r\n
0xb0000339 | [CellularAPI] SMS: Unsupported encoding type %1\r\n
0xb000033a | [CellularAPI] SMS: CalculateFragments: MessageLength:%1, TotalChars:%2, TotalPages:%3, MaxCharsPerSingleMessageSegment:%4, MaxCharsPerMultipartMessageSegment:%5, ActualOutputEncoding:%6, hrReturn:%7\r\n
0xb000033b | [CellularAPI] SMS: HResult: %1, registered for messaged of type: %2, thisPtr: %3, m_psmsstore: %4\r\n
0xb000033c | [CellularAPI] SMS: ThisPtr: %1 unregistered for messaged of type: %2\r\n
0xb000033d | [CellularAPI] SMS: CSMSModel: CSMSModel is created (%1), Executor %2, m_huiccapp %3, uiccid %4\r\n
0xb000033e | [CellularAPI] SMS: CSMSModel: CSMSModel is destructed (%1)\r\n
0xb000033f | [CellularAPI] SMS: CGenericSmsProvider: CGenericSmsProvider is created (%1)\r\n
0xb0000340 | [CellularAPI] SMS: CGenericSmsProvider: CGenericSmsProvider is destructed (%1)\r\n
0xb0000341 | [CellularAPI] SMS: Failure in processing message. hr: %3, Function: %1, Line: %2, ThisPtr: %4 \r\n
0xb0000342 | [CellularAPI] SMS: message with invalid teleservice. encoding(%1), teleservice(%2), executor(%3), partIndex(%4), totalParts(%5), cbLineId(%6), rgbLineId(%7), cbMessageUID(%8), rgbMessageUID(%9), type(%10)\r\n
0xb0000343 | [CellularAPI] SMS: Ack only message, ThisPtr: %1\r\n
0xb0000344 | [CellularAPI] SMS: Dropped App Port Message: Provider(%1), PortNum(%2), thisptr %3\r\n
0xb0000345 | [CellularAPI] SMS: Attemping to process a custom China Telecom (CT) WAP message, ThisPtr: %1.\r\n
0xb0000346 | [CellularAPI] SMS: Unknown RIL_MSGDLVSTATUS 0x%1\r\n
0xb0000347 | [CellularAPI] CCompletionClasses: Radio/Slot Configuration Check  - Function: %1, Checked Parameter: %2\r\n
0xb0000348 | [CellularAPI] CCompletionClasses: Verify Radio/Slot Configuration Check  - Function: %1\r\n
0xb0000349 | [CellularAPI] SMS: SmsStoreOpen. HR %1, ThisPtr %2, Filename %3\r\n
0xb000034a | [CellularAPI] SMS: SmsStoreCose. HR %1, ThisPtr %2\r\n
0xb000034b | [CellularAPI] SMS: Invalid huiccapp for received message. Executor: %1, MsgHuiccapp: %2, MsgIndex: %3, InstanceHuiccapp: %4, ImsHuiccapp: %5, ThisPtr: %6\r\n
0xb000034c | [CellularAPI] SMS: Delivering duplicate message with partIndex %1, noOfParts %2, cuid %3, uid %4, thisptr %5\r\n
0xb000034d | [CellularAPI] SMS: Incomplete message to ready queue with partIndex %1, noOfParts %2, cuid %3, uid %4, thisptr %5\r\n
0xb000034e | [CellularAPI] SMS: Using %1 to create new UID for message with partIndex %2, noOfParts %3, cuid %4, uid %5, thisptr %6\r\n
0xb000034f | [CellularAPI] SMS: Delivering SMS Message with ClientAckId: %1, MessagePtr: %2, Provider: %3\r\n
0xb0000350 | [CellularAPI] SMS: Delivered SMS Message with HRESULT: %1, MessagePtr: %2, Provider: %3\r\n
0xb0000357 | [CellularAPI] SMS: Failure in query of IMSI_CAN (%1) with NtStatus: %2\r\n
0xb0000358 | [CellularAPI] SMS: Failure in query of Line_CONFIG_CAN (%1) with NtStatus: %2\r\n
0xb0000359 | [CellularAPI] SMS: Error in CB for query of IMSI_CAN (%1), Length %2 Buffer %3\r\n
0xb000035a | [CellularAPI] SMS: Error in CB for query of Line_CONFIG_CAN (%1), Length %2 Buffer %3\r\n
0xb000035b | [CellularAPI] SMS: Multivariant WNF change notif with error (Buffer %1 Length %2)\r\n
0xb000035c | [CellularAPI] SMS: Multivariant WNF change notif (cSessions %1)\r\n
0xb000035d | [CellularAPI] SMS: Multivariant WNF change notif (Session# %1 idxSlot %2 State %3)\r\n
0xb000035e | [CellularAPI] SMS: WNF SubscribeError (tStatus: %1) for %2\r\n
0xb000035f | [CellularAPI] SMS: CellcoreSettingMigratorState WNF change notif with error (Buffer %1 Length %2)\r\n
0xb0000360 | [CellularAPI] SMS: CellcoreSettingMigratorState WNF change notif (state %1)\r\n
0xb0000361 | [CellularAPI] SMS: %1 for SMS Model. Client: %2, CCan: %3\r\n
0xb0000362 | [CellularAPI] SMS: %1 Client: %2, CSmsModel: %3, CCan: %4\r\n
0xb0000363 | [CellularAPI] SMS: SmsModel operation %1 succeeded\r\n
0xb0000364 | [CellularAPI] SMS: SetBroadcast retrying attempt (number of retries left %1)\r\n
0xb0000365 | [CellularAPI] SMS: SmsApp message processed: DoNotAckFlag(%1), AckOnlyFlag(%2), MessagePort(%3), Registered Ports(%5), thisptr(%6)\r\n
0xb0000366 | [CellularAPI] SMS: SmsBroadcast message processed: AckOnly(%1), Channel(%2), MCC(%3), Registered Channels(%5), thisptr(%6)\r\n
0xb0000367 | [CellularAPI] SMS: SmsBroadcast config Broadcast Types(%2), Channels(%4), thisptr(%5)\r\n
0xb0000368 | [CellularAPI] SMS: Broadcast message rejected as channel %1 is not enabled\r\n
0xb0000369 | [CellularAPI] SMS: Broadcast message rejected as channel %1 is not enabled. Mobile Country Code: %2\r\n
0xb000036a | [CellularAPI] SMS: Broadcast message rejected as the language (%1) on a multi-language channel (%2) does not match the device UI language (%3).\r\n
0xb000036b | [CellularAPI] SMS: The port (%1) doesn't match the standard WDP port (%2) for wap push.\r\n
0xb000036c | [CellularAPI] SMS: The SmsAppProvider was accepted by the port (%1).\r\n
0xb000036d | [CellularAPI] SMS: SmsAppMessages cannot be received on the standard WDP port (%1).\r\n
0xb000036e | [CellularAPI] SMS: Encoding %1 for CDMA is not currently supported.\r\n
0xb000036f | [CellularAPI] SMS: Encoding %1 is not valid, using % encoding instead.\r\n
0xb00003e8 | [CellularAPI] CCellularModem: Command %2 failed with hresult %1\r\n
0xb00003e9 | [CellularAPI] CCellularModem: CCellularModem is created (%1)\r\n
0xb00003ea | [CellularAPI] CCellularModem: CCellularModem is destructed (%1)\r\n
0xb00003eb | [CellularAPI] CCellularModem: Destroy thread is launched (pModem=%1)\r\n
0xb00003ec | [CellularAPI] CCellularModem: Destroy thread is finished (pModem=%1)\r\n
0xb00003ed | [CellularAPI] CCellularModem: Create Destroy thread (pModem=%1, ref=%2)\r\n
0xb00003ee | [CellularAPI] CCellularModem: Release pModem in Destroy thread (pModem=%1, ref=%2)\r\n
0xb00003ef | [CellularAPI] CCellularModem: QCN ERROR, Device Not Provisioned - OnRadioConfig Failed: hresult %1\r\n
0xb00003f0 | [CellularAPI] CCellularModem: Dispatch_CompleteDestroyModem is done (pModem=%1)\r\n
0xb00003f1 | [CellularAPI] CCellularModem: Attempt to use radio configuration at index [%1] while only [%2] configurations are available.\r\n
0xb00003f2 | [CellularAPI] CCellularModem: WaitForDestroyCompletion is called in Synchronizer.(pModem=%1)\r\n
0xb000044c | [CellularAPI] C3GPPCallModel: Attempt to start a new USSD session while another exists. New session attempted with - dwNetworkCCErrorCause = %1, dwNetworkSSErrorCause = %2, dwVendorErrorCause = %3 and dwStatus = %4\r\n
0xb000044d | [CellularAPI] C3GPPCallModel: Attempt to start a new USSD session while another exists. New session is NULL\r\n
0xb000044e | [CellularAPI] C3GPPCallModel: Started new USSD session with dwNetworkCCErrorCause = %1, dwNetworkSSErrorCause = %2, dwVendorErrorCause = %3 and dwStatus = %4\r\n
0xb000044f | [CellularAPI] C3GPPCallModel: Started new USSD session with NULL SupSvcData\r\n
0xb0000450 | [CellularAPI] C3GPPCallModel: USSD session terminated\r\n
0xb0000451 | [CellularAPI] C3GPPCallModel: Received USSD response with - dwNetworkCCErrorCause = %1, dwNetworkSSErrorCause = %2, dwVendorErrorCause = %3 and dwStatus = %4\r\n
0xb0000452 | [CellularAPI] C3GPPCallModel: C3GPPCallModel is created (%1)\r\n
0xb0000453 | [CellularAPI] C3GPPCallModel: C3GPPCallModel is destructed (%1)\r\n
0xb0000454 | [CellularAPI] C3GPP2CallModel: C3GPP2CallModel is created (%1)\r\n
0xb0000455 | [CellularAPI] C3GPP2CallModel: C3GPP2CallModel is destructed (%1)\r\n
0xb0000456 | [CellularAPI] CUnifiedCallModel: Publishing Call Forwarding state change (reason=%1, status=%2) result (%3).\r\n
0xb0000457 | [CellularAPI] CUnifiedCallModel: RIL_Dial is called successfully with executor %1.\r\n
0xb0000458 | [CellularAPI] CUnifiedCallModel: Duplicate call ID: [%1] while adding new active call.\r\n
0xb00004b0 | [CellularAPI] CCan: CCan is created (%1)\r\n
0xb00004b1 | [CellularAPI] CCan: CCan is destructed (%1)\r\n
0xb00004b2 | [CellularAPI] CCan: Calling SetExecutorConfig with zero HuiccApp\r\n
0xb00004b3 | [CellularAPI] CCan: Gets an error(%1) for SetExecutorConfig, but ignores because we have zero HuiccApp.\r\n
0xb00004b4 | [CellularAPI] CCan: Gets an error(%1) for SetExecutorConfig, but ignores because wmRil is older version.\r\n
0xb00004b5 | [CellularAPI] CCan: Sending registration status [%1] to clients.\r\n
0xb00004b6 | [CellularAPI] CCan: Postponing regStatus information because IMSI is not available.\r\n
0xb00004b7 | [CellularAPI] CCan: Error getting IMSI hresult=[%1].\r\n
0xb00004b8 | [CellularAPI] CCan: Suppressing out-of-order notification. Notification ID:#1, LastProcessed ID:#2.\r\n
0xb0000514 | [CellularAPI] CWnfSubscription: Could not unsubscribe WNF notification due to error (%1)\r\n
0xb0000515 | [CellularAPI] CWnfSubscription: Function: %1, Received Notification: %3, Callback: %4, Context: %5\r\n
0xb0000578 | [CellularAPI] CWnfContainer: Dropping WNF notification, client with callback %1 already unsubscribed\r\n
0xb0000640 | [CellularAPI] CAggregatedSlot::CAggregatedSlot is created (%1)\r\n
0xb0000641 | [CellularAPI] CAggregatedSlot::CAggregatedSlot is destructed (%1)\r\n
0xb0000642 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The virtual slot is empty\r\n
0xb0000643 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: Input size (%1) is too small (< %2)\r\n
0xb0000644 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: Either RILUICCSLOTINFO.dwParams & RIL_PARAM_SLOTINFO_NUMSLOTS) = %1 or input size (cbData = %2) is incorrect (!= %3 (cbSize) or %4 (offsetof))\r\n
0xb0000645 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The number of slots (%1) is not equal to 2\r\n
0xb0000646 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The previous virtual slot state = %1 and the current virtual slot state = %2\r\n
0xb0000647 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The current state of the aggregated slot (= %1) is neither ACTIVE nor NOT_READY\r\n
0xb0000648 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The current physical slot state is NOT_READY and its previous state (= %1) is NOT ACTIVE\r\n
0xb0000649 | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The current physical slot state is NOT_READY and its previous state is ACTIVE\r\n
0xb000064a | [CellularAPI] CAggregatedSlot::Dispatch_HandleNotification: The current state of the aggregated slot is set to %1\r\n
0xb00006a4 | [CellularAPI] CAggregatedUICC::CAggregatedUICC is created (%1)\r\n
0xb00006a5 | [CellularAPI] CAggregatedUICC::CAggregatedUICC is destructed (%1)\r\n
0xb00006a6 | [CellularAPI] CAggregatedUICC::EmbeddedDispatch_GetCardInfoCompletion: GetCardInfo returns for slot %1 and m_cInfoCompletion = %2\r\n
0xb00006a7 | [CellularAPI] CAggregatedUICC::EmbeddedDispatch_GetCardInfoCompletion: The virtual card flag of slot %1 is TRUE\r\n
0xb00006a8 | [CellularAPI] CAggregatedUICC::EmbeddedDispatch_GetCardInfoCompletion: m_cInfoCompletion (= %1) != sc_cSlots (= %2) and wait for the apps on all the UICCs to be enumerated\r\n
0xd0000001 | NOINFOREQUIRED\r\n
0xd0000002 | FURTHERINFOREQUIRED\r\n
0xd0000003 | TIMEOUT\r\n
0xd0000004 | ERROR\r\n
0xd0000005 | RIL_FWDREASON_UNCONDITIONAL\r\n
0xd0000006 | RIL_FWDREASON_MOBILEBUSY\r\n
0xd0000007 | RIL_FWDREASON_NOREPLY\r\n
0xd0000008 | RIL_FWDREASON_UNREACHABLE\r\n
0xd0000009 | RIL_FWDREASON_ALLFORWARDING\r\n
0xd000000a | RIL_FWDREASON_ALLCONDITIONAL\r\n
0xd000000b | RIL_SVCSTAT_UNKNOWN\r\n
0xd000000c | RIL_SVCSTAT_DISABLED\r\n
0xd000000d | RIL_SVCSTAT_ENABLED\r\n
0xd000000e | RIL_SVCSTAT_DEFAULT\r\n
0xd000000f | RIL_E_PHONEFAILURE\r\n
0xd0000010 | RIL_E_NOCONNECTION\r\n
0xd0000011 | RIL_E_LINKRESERVED\r\n
0xd0000012 | RIL_E_OPNOTALLOWED\r\n
0xd0000013 | RIL_E_OPNOTSUPPORTED\r\n
0xd0000014 | RIL_E_UICCNOTINSERTED\r\n
0xd0000015 | RIL_E_UICCFAILURE\r\n
0xd0000016 | RIL_E_UICCBUSY\r\n
0xd0000017 | RIL_E_UICCWRONG\r\n
0xd0000018 | RIL_E_INCORRECTPASSWORD\r\n
0xd0000019 | RIL_E_MEMORYFULL\r\n
0xd000001a | RIL_E_INVALIDINDEX\r\n
0xd000001b | RIL_E_NOTFOUND\r\n
0xd000001c | RIL_E_MEMORYFAILURE\r\n
0xd000001d | RIL_E_TEXTSTRINGTOOLONG\r\n
0xd000001e | RIL_E_INVALIDTEXTSTRING\r\n
0xd000001f | RIL_E_DIALSTRINGTOOLONG\r\n
0xd0000020 | RIL_E_INVALIDDIALSTRING\r\n
0xd0000021 | RIL_E_NONETWORKSVC\r\n
0xd0000022 | RIL_E_NETWORKTIMEOUT\r\n
0xd0000023 | RIL_E_EMERGENCYONLY\r\n
0xd0000024 | RIL_E_TELEMATICIWUNSUPPORTED\r\n
0xd0000025 | RIL_E_SMTYPE0UNSUPPORTED\r\n
0xd0000026 | RIL_E_CANTREPLACEMSG\r\n
0xd0000027 | RIL_E_PROTOCOLIDERROR\r\n
0xd0000028 | RIL_E_DCSUNSUPPORTED\r\n
0xd0000029 | RIL_E_MSGCLASSUNSUPPORTED\r\n
0xd000002a | RIL_E_DCSERROR\r\n
0xd000002b | RIL_E_CMDCANTBEACTIONED\r\n
0xd000002c | RIL_E_CMDUNSUPPORTED\r\n
0xd000002d | RIL_E_CMDERROR\r\n
0xd000002e | RIL_E_MSGBODYHEADERERROR\r\n
0xd000002f | RIL_E_SCBUSY\r\n
0xd0000030 | RIL_E_NOSCSUBSCRIPTION\r\n
0xd0000031 | RIL_E_SCSYSTEMFAILURE\r\n
0xd0000032 | RIL_E_INVALIDADDRESS\r\n
0xd0000033 | RIL_E_DESTINATIONBARRED\r\n
0xd0000034 | RIL_E_REJECTEDDUPLICATE\r\n
0xd0000035 | RIL_E_VPFUNSUPPORTED\r\n
0xd0000036 | RIL_E_VPUNSUPPORTED\r\n
0xd0000037 | RIL_E_UICCMSGSTORAGEFULL\r\n
0xd0000038 | RIL_E_NOUICCMSGSTORAGE\r\n
0xd0000039 | RIL_E_UICCTOOLKITBUSY\r\n
0xd000003a | RIL_E_UICCDOWNLOADERROR\r\n
0xd000003b | RIL_E_MSGSVCRESERVED\r\n
0xd000003c | RIL_E_INVALIDMSGPARAM\r\n
0xd000003d | RIL_E_INVALIDSCADDRESS\r\n
0xd000003e | RIL_E_UNASSIGNEDNUMBER\r\n
0xd000003f | RIL_E_MSGBARREDBYOPERATOR\r\n
0xd0000040 | RIL_E_MSGCALLBARRED\r\n
0xd0000041 | RIL_E_MSGXFERREJECTED\r\n
0xd0000042 | RIL_E_DESTINATIONOUTOFSVC\r\n
0xd0000043 | RIL_E_UNIDENTIFIEDSUBCRIBER\r\n
0xd0000044 | RIL_E_SVCUNSUPPORTED\r\n
0xd0000045 | RIL_E_UNKNOWNSUBSCRIBER\r\n
0xd0000046 | RIL_E_NETWKOUTOFORDER\r\n
0xd0000047 | RIL_E_NETWKTEMPFAILURE\r\n
0xd0000048 | RIL_E_CONGESTION\r\n
0xd0000049 | RIL_E_RESOURCESUNAVAILABLE\r\n
0xd000004a | RIL_E_SVCNOTSUBSCRIBED\r\n
0xd000004b | RIL_E_SVCNOTIMPLEMENTED\r\n
0xd000004c | RIL_E_INVALIDMSGREFERENCE\r\n
0xd000004d | RIL_E_INVALIDMSG\r\n
0xd000004e | RIL_E_INVALIDMANDATORYINFO\r\n
0xd000004f | RIL_E_MSGTYPEUNSUPPORTED\r\n
0xd0000050 | RIL_E_ICOMPATIBLEMSG\r\n
0xd0000051 | RIL_E_INFOELEMENTUNSUPPORTED\r\n
0xd0000052 | RIL_E_PROTOCOLERROR\r\n
0xd0000053 | RIL_E_NETWORKERROR\r\n
0xd0000054 | RIL_E_MESSAGINGERROR\r\n
0xd0000055 | RIL_E_NOTREADY\r\n
0xd0000056 | RIL_E_TIMEDOUT\r\n
0xd0000057 | RIL_E_CANCELLED\r\n
0xd0000058 | RIL_E_NONOTIFYCALLBACK\r\n
0xd0000059 | RIL_E_OPFMTUNAVAILABLE\r\n
0xd000005a | RIL_E_NORESPONSETODIAL\r\n
0xd000005b | RIL_E_SECURITYFAILURE\r\n
0xd000005c | RIL_E_RADIOFAILEDINIT\r\n
0xd000005d | RIL_E_DRIVERINITFAILED\r\n
0xd000005e | RIL_E_RADIONOTPRESENT\r\n
0xd000005f | RIL_E_RADIOOFF\r\n
0xd0000060 | RIL_E_ILLEGALMS\r\n
0xd0000061 | RIL_E_ILLEGALME\r\n
0xd0000062 | RIL_E_GPRSSERVICENOTALLOWED\r\n
0xd0000063 | RIL_E_PLMNNOTALLOWED\r\n
0xd0000064 | RIL_E_LOCATIONAREANOTALLOWED\r\n
0xd0000065 | RIL_E_ROAMINGNOTALLOWEDINTHISLOCATIONAREA\r\n
0xd0000066 | RIL_E_SERVICEOPTIONNOTSUPPORTED\r\n
0xd0000067 | RIL_E_REQUESTEDSERVICEOPTIONNOTSUBSCRIBED\r\n
0xd0000068 | RIL_E_SERVICEOPTIONTEMPORARILYOUTOFORDER\r\n
0xd0000069 | RIL_E_PDPAUTHENTICATIONFAILURE\r\n
0xd000006a | RIL_E_INVALIDMOBILECLASS\r\n
0xd000006b | RIL_E_UNSPECIFIEDGPRSERROR\r\n
0xd000006c | RIL_E_RADIOREBOOTED\r\n
0xd000006d | RIL_E_INVALIDCONTEXTSTATE\r\n
0xd000006e | RIL_E_MAXCONTEXTS\r\n
0xd000006f | RIL_E_SYNCHRONOUS_DATA_UNAVAILABLE\r\n
0xd0000070 | RIL_E_FDNRESTRICT\r\n
0xd0000071 | RIL_E_INVALIDASYNCCOMMANDRESPONSE\r\n
0xd0000072 | RIL_E_INCOMPATIBLEPROXYDRIVER\r\n
0xd0000073 | RIL_E_INVALIDDRIVERVERSION\r\n
0xd0000074 | RIL_E_USIMCALLMODIFIED\r\n
0xd0000075 | RIL_E_PASSWORDMISMATCH\r\n
0xd0000076 | RIL_E_INVALIDCONTEXTACTIVATIONSTRING\r\n
0xd0000077 | RIL_E_UICCAPPINACCESSIBLE\r\n
0xd0000078 | RIL_E_UICCPINREQUIRED\r\n
0xd0000079 | RIL_E_UICCPUKREQUIRED\r\n
0xd000007a | RIL_E_UICCPUKBLOCKED\r\n
0xd000007b | RIL_E_EXECUTORNOTREADY\r\n
0xd000007c | RIL_E_INVALIDUICCKEYREF\r\n
0xd000007d | RIL_E_UICCINACTIVE\r\n
0xd000007e | RIL_E_PERSOPUKREQUIRED\r\n
0xd000007f | RIL_E_PERSOPUKBLOCKED\r\n
0xd0000080 | RIL_E_PERSOCHECKFAILED\r\n
0xd0000081 | RIL_E_INVALIDUICCPATH\r\n
0xd0000082 | RIL_E_IMSTEMPFAILURE\r\n
0xd0000083 | RIL_E_UICCNOTREADY\r\n
0xd0000084 | RIL_E_UICCPOWEROFF\r\n
0xd0000085 | RIL_E_CALLISACTIVE\r\n
0xd0000086 | RIL_E_USIMCALLBLOCKED\r\n
0xd0000087 | RIL_E_UICCADMRESTRICTED\r\n
0xd0000088 | RIL_E_DMSERVICENOTREADY\r\n
0xd0000089 | RIL_E_DMGETCONFIGFAILED\r\n
0xd000008a | RIL_E_DMCOMMITFAILED\r\n
0xd000008b | RIL_E_OTHEREXECUTORBUSY\r\n
0xd000008c | RIL_E_IMSNOHANDOVERTARGETFOUND\r\n
0xd000008d | RIL_E_VCCHANDOVERINPROGRESS\r\n
0xd000008e | RIL_E_INVALIDREMOTEURI\r\n
0xd000008f | RIL_MODEMRESETSTATE_STARTED\r\n
0xd0000090 | RIL_MODEMRESETSTATE_RECOVERED\r\n
0xd0000091 | RIL_MODEMRESETSTATE_FAILED\r\n
0xd0000092 | Registered\r\n
0xd0000093 | Unregistered\r\n
0xd0000094 | OFF_EMPTY\r\n
0xd0000095 | OFF\r\n
0xd0000096 | Empty\r\n
0xd0000097 | NOT_READY\r\n
0xd0000098 | ACTIVE\r\n
0xd0000099 | ERROR\r\n
