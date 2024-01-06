## onex.dll

Path: %SystemRoot%\system32\onex.dll

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000002 | EAP\r\n
0x10000003 | EAPPacket\r\n
0x10000004 | OneXUI\r\n
0x10000005 | Profile\r\n
0x10000006 | Semantic\r\n
0x10000007 | Supplicant\r\n
0x10000008 | User\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | API\r\n
0x70000002 | EAP\r\n
0x70000003 | MSM\r\n
0x70000004 | User\r\n
0x70000005 | Supplicant\r\n
0x70000006 | Profile\r\n
0x70000007 | Port\r\n
0x90000001 | Microsoft-Windows-OneX\r\n
0x90000002 | Microsoft-Windows-OneX/Diagnostic\r\n
0xb0000001 | OneXDestroySupplicantPort\r\n
0xb0000002 | OneXStartAuthentication\r\n
0xb0000003 | OneXStopAuthentication\r\n
0xb0000004 | Port(%1): EAP error WinError=%2, ReasonCode=%3, EapMethod(Type=%4), RootCause is %5\r\n
0xb0000005 | Port(%1): Account is disabled and user is non-domain joined. Authentication will be tried with alternate credentials profile.\r\n
0xb0000006 | Port(%1): EAP failure indication with error code %2 and reason code %3\r\n
0xb0000007 | Port(%1): Saving updated user data of size (%2)\r\n
0xb0000008 | Port(%1): Saving updated connection data of size (%2)\r\n
0xb0000009 | Port(%1): Successfully received UI Response\r\n
0xb000000a | Port(%1): EapProcessPacketValidityAndGetResult returned action %2\r\n
0xb000000b | Port(%1): EAP requested authentication restart\r\n
0xb000000c | Port(%3): EapHostPeerInitialize failed, error %1\r\n
0xb000000d | Port(%3): EapHostPeerEndSession failed, error %1\r\n
0xb000000e | Port(%3): OneXGeneratePacketEvent failed, error %1\r\n
0xb000000f | Port(%3): OneXGeneratePeerAuthRestartedEvent failed, error %1\r\n
0xb0000010 | Port(%3): EapHostPeerGetAuthStatus failed, error %1\r\n
0xb0000011 | Port(%3): MSMUIRequest failed, error %1\r\n
0xb0000012 | Port(%3): CompareSessionUserWithOwner failed, error %1\r\n
0xb0000013 | Port(%3): ProcessEapHostTLV failed, error %1\r\n
0xb0000014 | Port(%1): Cannot send UI Request (code=%2) to MSM since UI is disabled for the port\r\n
0xb0000015 | Port(%3): Error %1 in calling WTSQueryUserToken. Proposing machine authentication.\r\n
0xb0000016 | Port(%3): SupplicantGetUserTokenFromRuntimeState failed, error %1\r\n
0xb0000017 | Port(%1): The auth mode is User only but an appropriate user can't be found\r\n
0xb0000018 | Port(%3): CompareOneXCredentials failed, error %1\r\n
0xb0000019 | Port(%3): Failed to conditionally send Eapol start packet. Ignoring error %1\r\n
0xb000001a | Port(%3): OneXGenerateForceAuthenticatedEvent failed, error %1\r\n
0xb000001b | OneXValidateProfile failed, error %1, reason code %3\r\n
0xb000001c | EAP dll requested to show UI, but the UI for the port is not allowed with current credentials\r\n
0xb000001d | The EAP method does not support key derivation and will not be used for discovery\r\n
0xb000001e | The EAP method does not support mutual authentication and will not be used for discovery\r\n
0xb000001f | Done with creating discovery profiles. Created %1 profiles\r\n
0xb0000020 | Created a 1X profile for discovery with eapType=%1 and AuthMode=%2\r\n
0xb0000021 | The EAP method %1 is not allowed for media type %2 and will not be used for discovery\r\n
0xb0000022 | Port(%1): Successfully sent UI Request (code=%2) to MSM\r\n
0xb0000023 | Received a session change event (%1)\r\n
0xb0000024 | Finished initializing a new port with id=%1 and friendly name=%2\r\n
0xb0000025 | Port(%1): MPPE-Send/Recv-Keys have been derived by supplicant\r\n
0xb0000026 | Port(%1): Sending UI Request (code=%2) to MSM\r\n
0xb0000027 | Port(%1): Asking MSM to delete user data for user token\r\n
0xb0000028 | Port(%1): Received an EAP packet length=%2, type=%3, identifier=%4, eapType=%5\r\n
0xb0000029 | Port(%1): Sent an Eapol start packet\r\n
0xb000002a | Port(%1): The supplicant is configured to not send an Eapol start packet\r\n
0xb000002b | Port(%1): Restarting authentication due to reason = %2\r\n
0xb000002c | Port(%1): Authentication Starting\r\n
0xb000002d | Port(%1): Authentication Completed\r\n
0xb000002e | Port(%1): Time taken for this authentication = %2 ms\r\n
0xb000002f | Port(%1): 802.1X user identified. auth identity = %2, sessionId = %3, username=%4, domain=%5\r\n
0xb0000030 | Port(%1): Stopping the current 802.1X authentication\r\n
0xb0000031 | Port(%1): Starting a new 802.1X authentication (%2)\r\n
0xb0000032 | Port(%1): Alternate credentials will be used for this profile\r\n
0xb0000033 | Port(%1): This is a discovery profile being attempted\r\n
0xb0000034 | Port(%1): Trying timely configuration\r\n
0xb0000035 | Port(%1): Completed the 802.1X authentication successfully\r\n
0xb0000036 | Port(%1): Completed the 802.1X authentication because no authenticator was found\r\n
0xb0000037 | Port(%1): The session id (%2) received with the UI response is different than the session id for which the request was sent (%3). Discarding this response\r\n
0xb0000038 | Port(%1): A pending UI request exists size=%2, sessionId=%3\r\n
0xb0000039 | Port(%1): User auth proposed for sessionId=%3 (%2)\r\n
0xb000003a | Port(%1): The machine is in app server mode. Proposing machine auth\r\n
0xb000003b | EapHostPeerInvokeInteractiveUI failed, Error = %2 Reason = %3\r\n
0xb000003c | No EAP Cred fields to display\r\n
0xb000003d | Creds conversion failed (error=%1)\r\n
0xb000003e | EapHostPeerQueryInteractiveUIInputFields failed (error=%1)\r\n
0xb000003f | Displaying the change password dialog - %1\r\n
0xb0000040 | Port(%1): Sending an EAP packet length=%2, type=%3, identifier=%4, eapType=%5\r\n
0xb0000041 | Port(%1): Identity being sent in the ResponseId packet is %2\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | None\r\n
0xd0000002 | Notification\r\n
0xd0000003 | RequestId\r\n
0xd0000004 | Success\r\n
0xd0000005 | Fail\r\n
0xd0000006 | RequestOther\r\n
0xd0000007 | ResponseId\r\n
0xd0000008 | ResponseNak\r\n
0xd0000009 | ResponseOther\r\n
0xd000000a | PacketInvalid\r\n
0xd000000b | Console Connect\r\n
0xd000000c | Console Disconnect\r\n
0xd000000d | Remote Connect\r\n
0xd000000e | Remote Disconnect\r\n
0xd000000f | Session Logon\r\n
0xd0000010 | Session Logoff\r\n
0xd0000011 | Session Lock\r\n
0xd0000012 | Session Unlock\r\n
0xd0000013 | Remote Control\r\n
0xd0000014 | Discard\r\n
0xd0000015 | Send\r\n
0xd0000016 | Result\r\n
0xd0000017 | InvokeUI\r\n
0xd0000018 | Respond\r\n
0xd0000019 | StartAuthentication\r\n
0xd000001a | None\r\n
0xd000001b | Peer Initiated\r\n
0xd000001c | Msm Initiated\r\n
0xd000001d | OneX Held State Timeout\r\n
0xd000001e | OneX Auth Timeout\r\n
0xd000001f | OneX Configuration Changed\r\n
0xd0000020 | OneX User Changed\r\n
0xd0000021 | Quarantine State Changed\r\n
0xd0000022 | Alternate Creds Trial\r\n
0xd0000023 | Invalid\r\n
0xd0000024 | User change\r\n
0xd0000025 | MSM initiated\r\n
0xd0000026 | Config change\r\n
0xd0000027 | PLAP profile\r\n
0xd0000028 | TIMELY profile\r\n
0xd0000029 | User token specified\r\n
0xd000002a | Logged-on user token\r\n
0xd000002b | Success\r\n
0xd000002c | Failure\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000002 | EAP\r\n
0x10000003 | EAPPacket\r\n
0x10000004 | OneXUI\r\n
0x10000005 | Profile\r\n
0x10000006 | Semantic\r\n
0x10000007 | Supplicant\r\n
0x10000008 | User\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | API\r\n
0x70000002 | EAP\r\n
0x70000003 | MSM\r\n
0x70000004 | User\r\n
0x70000005 | Supplicant\r\n
0x70000006 | Profile\r\n
0x70000007 | Port\r\n
0x90000001 | Microsoft-Windows-OneX\r\n
0x90000002 | Microsoft-Windows-OneX/Diagnostic\r\n
0x90000003 | Microsoft-Windows-OneX/Operational\r\n
0xb0000001 | OneXDestroySupplicantPort\r\n
0xb0000002 | OneXStartAuthentication\r\n
0xb0000003 | OneXStopAuthentication\r\n
0xb0000004 | Port(%1): EAP error WinError=%2, ReasonCode=%3, EapMethod(Type=%4), RootCause is %5\r\n
0xb0000005 | Port(%1): Account is disabled and user is non-domain joined. Authentication will be tried with alternate credentials profile.\r\n
0xb0000006 | Port(%1): EAP failure indication with error code %2 and reason code %3\r\n
0xb0000007 | Port(%1): Saving updated user data of size (%2)\r\n
0xb0000008 | Port(%1): Saving updated connection data of size (%2)\r\n
0xb0000009 | Port(%1): Successfully received UI Response\r\n
0xb000000a | Port(%1): EapProcessPacketValidityAndGetResult returned action %2\r\n
0xb000000b | Port(%1): EAP requested authentication restart\r\n
0xb000000c | Port(%3): EapHostPeerInitialize failed, error %1\r\n
0xb000000d | Port(%3): EapHostPeerEndSession failed, error %1\r\n
0xb000000e | Port(%3): OneXGeneratePacketEvent failed, error %1\r\n
0xb000000f | Port(%3): OneXGeneratePeerAuthRestartedEvent failed, error %1\r\n
0xb0000010 | Port(%3): EapHostPeerGetAuthStatus failed, error %1\r\n
0xb0000011 | Port(%3): MSMUIRequest failed, error %1\r\n
0xb0000012 | Port(%3): CompareSessionUserWithOwner failed, error %1\r\n
0xb0000013 | Port(%3): ProcessEapHostTLV failed, error %1\r\n
0xb0000014 | Port(%1): Cannot send UI Request (code=%2) to MSM since UI is disabled for the port\r\n
0xb0000015 | Port(%3): Error %1 in calling WTSQueryUserToken. Proposing machine authentication.\r\n
0xb0000016 | Port(%3): SupplicantGetUserTokenFromRuntimeState failed, error %1\r\n
0xb0000017 | Port(%1): The auth mode is User only but an appropriate user can't be found\r\n
0xb0000018 | Port(%3): CompareOneXCredentials failed, error %1\r\n
0xb0000019 | Port(%3): Failed to conditionally send Eapol start packet. Ignoring error %1\r\n
0xb000001a | Port(%3): OneXGenerateForceAuthenticatedEvent failed, error %1\r\n
0xb000001b | OneXValidateProfile failed, error %1, reason code %3\r\n
0xb000001c | EAP dll requested to show UI, but the UI for the port is not allowed with current credentials\r\n
0xb000001d | The EAP method does not support key derivation and will not be used for discovery\r\n
0xb000001e | The EAP method does not support mutual authentication and will not be used for discovery\r\n
0xb000001f | Done with creating discovery profiles. Created %1 profiles\r\n
0xb0000020 | Created a 1X profile for discovery with eapType=%1 and AuthMode=%2\r\n
0xb0000021 | The EAP method %1 is not allowed for media type %2 and will not be used for discovery\r\n
0xb0000022 | Port(%1): Successfully sent UI Request (code=%2) to MSM\r\n
0xb0000023 | Received a session change event (%1)\r\n
0xb0000024 | Finished initializing a new port with id=%1 and friendly name=%2\r\n
0xb0000025 | Port(%1): MPPE-Send/Recv-Keys have been derived by supplicant\r\n
0xb0000026 | Port(%1): Sending UI Request (code=%2) to MSM\r\n
0xb0000027 | Port(%1): Asking MSM to delete user data for user token\r\n
0xb0000028 | Port(%1): Received an EAP packet length=%2, type=%3, identifier=%4, eapType=%5\r\n
0xb0000029 | Port(%1): Sent an Eapol start packet\r\n
0xb000002a | Port(%1): The supplicant is configured to not send an Eapol start packet\r\n
0xb000002b | Port(%1): Restarting authentication due to reason = %2\r\n
0xb000002c | Port(%1): Authentication Starting\r\n
0xb000002d | Port(%1): Authentication Completed\r\n
0xb000002e | Port(%1): Time taken for this authentication = %2 ms\r\n
0xb000002f | Port(%1): 802.1X user identified. auth identity = %2, sessionId = %3, username=%4, domain=%5\r\n
0xb0000030 | Port(%1): Stopping the current 802.1X authentication\r\n
0xb0000031 | Port(%1): Starting a new 802.1X authentication (%2)\r\n
0xb0000032 | Port(%1): Alternate credentials will be used for this profile\r\n
0xb0000033 | Port(%1): This is a discovery profile being attempted\r\n
0xb0000034 | Port(%1): Trying timely configuration\r\n
0xb0000035 | Port(%1): Completed the 802.1X authentication successfully\r\n
0xb0000036 | Port(%1): Completed the 802.1X authentication because no authenticator was found\r\n
0xb0000037 | Port(%1): The session id (%2) received with the UI response is different than the session id for which the request was sent (%3). Discarding this response\r\n
0xb0000038 | Port(%1): A pending UI request exists size=%2, sessionId=%3\r\n
0xb0000039 | Port(%1): User auth proposed for sessionId=%3 (%2)\r\n
0xb000003a | Port(%1): The machine is in app server mode. Proposing machine auth\r\n
0xb000003b | EapHostPeerInvokeInteractiveUI failed, Error = %2 Reason = %3\r\n
0xb000003c | No EAP Cred fields to display\r\n
0xb000003d | Creds conversion failed (error=%1)\r\n
0xb000003e | EapHostPeerQueryInteractiveUIInputFields failed (error=%1)\r\n
0xb000003f | Displaying the change password dialog - %1\r\n
0xb0000040 | Port(%1): Sending an EAP packet length=%2, type=%3, identifier=%4, eapType=%5\r\n
0xb0000041 | Port(%1): Identity being sent in the ResponseId packet is %2\r\n
0xb0000042 | Port:(%1): Saving/Updating master copy of user data%nSupplicantIsUsingExplicitCreds:(%2)\r\n
0xb0000044 | Port(%1): Flushing User Data from Persistent Store%n%nSupplicantIsUsingExplicitCreds:(%2)\r\n
0xb0000046 | Port(%1):OneX Auth Timeout\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | None\r\n
0xd0000002 | Notification\r\n
0xd0000003 | RequestId\r\n
0xd0000004 | Success\r\n
0xd0000005 | Fail\r\n
0xd0000006 | RequestOther\r\n
0xd0000007 | ResponseId\r\n
0xd0000008 | ResponseNak\r\n
0xd0000009 | ResponseOther\r\n
0xd000000a | PacketInvalid\r\n
0xd000000b | Console Connect\r\n
0xd000000c | Console Disconnect\r\n
0xd000000d | Remote Connect\r\n
0xd000000e | Remote Disconnect\r\n
0xd000000f | Session Logon\r\n
0xd0000010 | Session Logoff\r\n
0xd0000011 | Session Lock\r\n
0xd0000012 | Session Unlock\r\n
0xd0000013 | Remote Control\r\n
0xd0000014 | Discard\r\n
0xd0000015 | Send\r\n
0xd0000016 | Result\r\n
0xd0000017 | InvokeUI\r\n
0xd0000018 | Respond\r\n
0xd0000019 | StartAuthentication\r\n
0xd000001a | None\r\n
0xd000001b | Peer Initiated\r\n
0xd000001c | Msm Initiated\r\n
0xd000001d | OneX Held State Timeout\r\n
0xd000001e | OneX Auth Timeout\r\n
0xd000001f | OneX Configuration Changed\r\n
0xd0000020 | OneX User Changed\r\n
0xd0000021 | Quarantine State Changed\r\n
0xd0000022 | Alternate Creds Trial\r\n
0xd0000023 | Invalid\r\n
0xd0000024 | User change\r\n
0xd0000025 | MSM initiated\r\n
0xd0000026 | Config change\r\n
0xd0000027 | PLAP profile\r\n
0xd0000028 | TIMELY profile\r\n
0xd0000029 | User token specified\r\n
0xd000002a | Logged-on user token\r\n
0xd000002b | Success\r\n
0xd000002c | Failure\r\n
