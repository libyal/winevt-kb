## webio.dll

Path: %SystemRoot%\system32\webio.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000021 | SEND\r\n
0x10000022 | RECEIVE\r\n
0x10000023 | L3_CONNECT\r\n
0x10000025 | CLOSE\r\n
0x10000026 | SECURITY\r\n
0x10000027 | CONFIGURATION\r\n
0x10000028 | GLOBAL\r\n
0x10000029 | DROPPED\r\n
0x1000002a | PII_PRESENT\r\n
0x1000002b | PACKET\r\n
0x1000002c | ADDRESS\r\n
0x1000002d | CONTEXT_EVENT\r\n
0x1000002e | STATE_TRANSITION\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | NOOP\r\n
0x3000000b | Queue\r\n
0x3000000c | Cancel\r\n
0x3000000d | Get\r\n
0x3000000e | Set\r\n
0x3000000f | Reallocate\r\n
0x30000010 | Reset\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000006d | WebIOAPI\r\n
0x7000006e | WebIODebug\r\n
0x7000006f | ApiInit\r\n
0x70000070 | ApiTerminate\r\n
0x70000071 | Session Create\r\n
0x70000072 | SessionClose\r\n
0x70000073 | SyncApiWait\r\n
0x700000c8 | RequestCreate\r\n
0x700000c9 | RequestConfiguration\r\n
0x700000ca | RequestClose\r\n
0x70000190 | RequestHeader\r\n
0x70000191 | ProxyResolution\r\n
0x70000193 | Endpoint\r\n
0x70000194 | RequestGenerateHeaders\r\n
0x70000195 | RequestSendEntity\r\n
0x70000196 | RequestEntityTracker\r\n
0x70000197 | RequestEntityCompleteCallback\r\n
0x70000198 | ResponseRecieveEntity\r\n
0x70000199 | ResponseEntityCompleteCallback\r\n
0x7000019a | RequestWaitingForConnection\r\n
0x7000019b | ResponseParser\r\n
0x7000019c | ResponseDirectReceiveEntity\r\n
0x7000019d | RequestSend\r\n
0x7000019e | ResponseReceive\r\n
0x7000019f | ResponseConnectionBufferReceive\r\n
0x700001a0 | RequestCancel\r\n
0x700001a1 | ConnectionSocketConnect\r\n
0x700001a2 | ConnectionSocketCreate\r\n
0x700001a3 | ConnectionSocketClose\r\n
0x700001a4 | ConnectionNameResolution\r\n
0x700001a5 | ConnectionSocketSend\r\n
0x700001a7 | ConnectionSocketReceive\r\n
0x700001a8 | SSLEncryptMessage\r\n
0x700001a9 | SSLInitializeSecurityContext\r\n
0x700001aa | SSLSendEntity\r\n
0x700001ab | SSLCertValidation\r\n
0x700001ac | SSLReceiveEntity\r\n
0x700001ad | SSLDecryptMessage\r\n
0x700001ae | SSLConnectionBufferReceive\r\n
0x700001af | ThreadToken\r\n
0x700001b0 | ResponseReceiveCompleteCallback\r\n
0x700001b1 | ThreadAction\r\n
0x700001b2 | Information\r\n
0x700001b3 | ConnectionNameResolutionRequest\r\n
0x700001b4 | SSLAcquireCredentialsHandle\r\n
0x70000385 | RequestState\r\n
0xb0000001 | %1: WebInitialize completed successfully (ApiVersion %3) (Flags %4) -> (API Handle = %2).\r\n
0xb0000002 | WebInitialize failed with an error = %5 (ApiVersion %3) (Flags %4)\r\n
0xb0000003 | %1 WebTerminate completed successfully. (Handle %2) (Flags %3)\r\n
0xb0000004 | %1 WebTerminate failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000005 | %3: WebCreateSession completed successfully. (ApiHandle %1[%2]) (Flags: %5) -> (Session Handle: %4)\r\n
0xb0000006 | %1: WebCreateSession failed with an error = %6. (ApiHandle %1[%2]) (Flags: %5)\r\n
0xb0000007 | %1: WebCloseSession called (Handle %2) (Flags %3)\r\n
0xb0000008 | %1: WebCloseSession failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000009 | %2(%1) API called.\r\n
0xb000000a | %2(%1) API returned successfully.\r\n
0xb000000b | %2(%1) API failed with an error = %3.\r\n
0xb000000c | %2(%1) API pending completion.\r\n
0xb000000d | %2(%1) API completed.\r\n
0xb000000e | %2(%1) API completed with an error = %3.\r\n
0xb000000f | %1: Set Request Option %3 (Handle %2) (Error %6) (Length %4) (Value %5) \r\n
0xb0000011 | %1: WebCreateHttpRequest completed successfully. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8) -> (Request Handle %2) \r\n
0xb0000012 | %3: WebCreateHttpRequest failed with error: %9. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8)\r\n
0xb0000013 | %1: WebCloseHttpRequest called (Handle %2) (Flags %3) \r\n
0xb0000014 | %1 WebCloseHttpRequest failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000015 | Synchronous API Event Handle Signall (Event %2) (Error %3) (Information %4)\r\n
0xb0000016 | Synchronous API Event Handle Wait Completed (Handle %1) (Event %2) (Error %3) (Information %4)\r\n
0xb0000017 | %1: WebSetHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000018 | %1: WebSetHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000019 | %1: WebRemoveHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001a | %1: WebRemoveHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3)\r\n
0xb000001b | %1: Indicating informational callback to request. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001c | %1: Informational callback to request complete. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001d | %1: WebCloseSession completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001e | %1: WebCloseHttpRequest completed sucessfully error = %4. (Handle %2) (Flags %3)\r\n
0xb0000064 | %1: Sending Headers: %3\r\n
0xb0000065 | %1: Received Headers: %3\r\n
0xb0000066 | %1: Starting Proxy Resolution\r\n
0xb0000067 | %1: Completed Proxy Resolution\r\n
0xb0000068 | %1: Acquired a connection slot (ConnMgr: %2), (Connection: %3)\r\n
0xb0000069 | %1: Request on Endpoint (Server Endpoint: %2) (Proxy Endpoint: %3) (Connection Manager: %4)\r\n
0xb000006a | %1: Request Message Generated (DataChunk %2[%3])\r\n
0xb000006b | %1: WebSendHttpRequestEntity (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006c | %1: WebSendHttpRequestEntity Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006d | %1: HTTP Queuing Entity for Sending (DataChunks %2) (ChunkLength %3) (IsEntity %4) (All Entity Posted? %5)\r\n
0xb000006e | %1: HTTP Sending Entity (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb000006f | %1: HTTP Send Entity Details (Connection: %2) (DataChunks %3) (Index %4) (Buffer %5 [%6]) Data: %7\r\n
0xb0000070 | %1: HTTP Sending Entity Complete (Error %6) (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb0000071 | %1: Completing WebSendHttpRequest(Entity) (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000072 | %1: Completing WebSendHttpRequest(Entity) Complete (DataChunks %2)\r\n
0xb0000073 | %1: WebHttpReceiveEntityBody (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000074 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000075 | %1: Completing WebHttpReceiveEntityBody (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000076 | %1: Completing WebHttpReceiveEntityBody Complete (DataChunks %2)\r\n
0xb0000077 | %1: HTTP Connection changing Buffer (OldBuffer %2 [%3]) (NewBuffer %5 [%6]) (Carryover %4)\r\n
0xb0000078 | %1: HTTP Connection Buffer Posting Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6])\r\n
0xb0000079 | %1: HTTP Connection Buffer Completing Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6]) (Error %7)  (CompletionInformation %8)\r\n
0xb000007a | %1: HTTP Connection Buffer Receive Details (DataChunks %2) (Length %3) Data: %4\r\n
0xb000007b | %1: HTTP Parser (Connection %2) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007c | %1: HTTP Parser Complete (Connection %2) (Error %9) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007d | %1: HTTP Parser Reset (Buffer %2) (HttpResponseCode %3)\r\n
0xb000007e | %1: HTTP Receive From Parser (DataChunk %2) (ParserChunk %3 [%4]) (Error %5) (Context %6) (Information %7)\r\n
0xb000007f | %1: HTTP Receive (DataChunk %2) (BytesToRecv %3)\r\n
0xb0000080 | %1: HTTP Receive Complete (DataChunk %2) (BytesToRecv %3) (Error %4) (Context %5) (Information %6)\r\n
0xb0000081 | %1: HTTP Receive Entity Details (DataChunk %2) (Index %3) (Length %4) Data %5\r\n
0xb0000082 | %1: WebSendHttpRequest (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000083 | %1: WebSendHttpRequest Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000084 | %1: WebHttpReceiveResponse (Handle: %2) (Flags %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000085 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %6) (Flags: %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000086 | %1: Completing WebHttpReceiveEntityBody (Error %3) (ResponseFlags %2) (CompletionInformation %4)\r\n
0xb0000087 | %1: Completing WebHttpReceiveEntityBody Complete\r\n
0xb0000088 | %1: WebCancelHttpRequest (Handle: %2) (Flags %3)\r\n
0xb0000089 | %1: WebCancelHttpRequest Complete (Error: %4) (Handle: %2) (Flags %3)\r\n
0xb00000c8 | %1: Connecting (Socket %2) (Context %5) (RemaingAddress %6) Address: %4.\r\n
0xb00000c9 | %1: Connection established (Socket %2) (Context %5)\r\n
0xb00000ca | %1: Connect failed with error %7 (Socket %2) (Context %5) (RemaingAddress %6)\r\n
0xb00000cb | Socket %2 created on Endpoint %1.\r\n
0xb00000cc | %1: Socket %2 Closed (Reason = %3, Status = %4).\r\n
0xb00000cd | %1: Name Resolution Request (Name %2) (Timeout %3) (CompletionContext: %4)\r\n
0xb00000ce | %1: Name Resolution Request Completed (FQDN %2) (Canonical %3) (AddressCount: %4) AddressData: %6\r\n
0xb00000cf | %1: Name Resolution Request Failed (Error %2)\r\n
0xb00000d0 | %1: Name Resolution Request queued to %2\r\n
0xb00000d1 | %1: Name Resolution Request is cancelled\r\n
0xb00000d2 | %1: Name Resolution Request Timed-out\r\n
0xb00000d3 | %1: Resolving addresses (Host %2) (Flags: %3)\r\n
0xb00000d4 | %1: Address resolution completed (Error = %4) (Host %2) (Flags: %3).(AddressCount %5)\r\n
0xb00000d5 | %1: Winsock Send Entity Start(DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d6 | %1: Winsock Send Entity Complete (Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d7 | %1: Winsock Recv Entity Start (DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d8 | %1: Winsock Recv Entity Complete(Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00002bc | %1: InitializeSecurityContext - Credential Handle(%2:%3) Context Handle (%4:%5) (Hostname %6) (InputFlags %7) (Buffer %8 [%9/%10])\r\n
0xb00002bf | %1: InitializeSecurityContext returned - (%14) Credential Handle(%2:%3) Context Handle (%4:%5) (OutputFlags %11) (Buffer %8 [%9/%10]) (DataChunk %12 [%13])\r\n
0xb00002c0 | %1: InitializeSecurityContext Details (Pre) - Credential Handle(%2:%3) (Buffer %4 [%5/%6]) Data: %7\r\n
0xb00002c1 | %1: InitializeSecurityContext Details (Post) - Credential Handle(%2:%3) (DataChunk %4 [%5]) Data: %6\r\n
0xb00002c2 | %1: SSL Encryption (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c3 | %1: SSL Encryption Complete (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (InBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c4 | %1: SSL Encryption Failed (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (Flags %9) \r\n
0xb00002c5 | %1: SSL Encryption Details (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9) Data:%10\r\n
0xb00002c6 | %1: SSL Queue Send Entity (SSLIOContext %2) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c7 | %1: SSL Send Entity Complete (SSLIOContext: %2) (Error: %5) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c8 | %1: SSL Cert Validation - (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002c9 | %1: SSL Cert Validation Failure - %7 (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002d0 | %1: SSL Queue Recv Entity Data Chunk (SSLIOContext %2) (DataChunks: %3)\r\n
0xb00002d1 | %1: SSL Filling Up Recv Entity Data Chunk (SSLIOContext: %2) (DataChunks: %3) (PlainData %4[%5]) (Information: %6)\r\n
0xb00002d2 | %1: SSL Decryption - Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d3 | %1: SSL Decryption Complete (SecStatus %9) (Error %10) Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d4 | %1: SSL Receive Buffer Posting Receive (DataChunk %2) (Buffer %3[%4/%5])\r\n
0xb00002d5 | %1: SSL Receive Buffer Receive Complete (DataChunk %2) (Error %7) (Information %6) (Buffer %3[%4/%5])\r\n
0xb00002d6 | %1: SSL Receive Buffer Details: (Buffer %2[%3/%4]) Data: %5\r\n
0xb00002d7 | %1: SSL Receive Buffer Posting Receive (Buffer %2) (NewBuffer: %3)\r\n
0xb00002d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002d9 | %1: SSL AcquireCredentialsHandle returned - (%7) Credential Handle(%5:%6) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002da | %1: SSL AcquireCredentialsHandle failed - (%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb0000834 | %1: =====Request Initialize===================\r\n
0xb0000835 | %1: =====Query Endpoints======================\r\n
0xb0000836 | %1: =====Waiting For Available Connection=====\r\n
0xb000083f | %1: =====Request Connect======================\r\n
0xb0000840 | %1: =====Name Resolution======================\r\n
0xb0000841 | %1: =====TCP Connect==========================\r\n
0xb0000842 | %1: =====SSL Negotiation======================\r\n
0xb0000848 | %1: =====Generate Headers=====================\r\n
0xb0000849 | %1: =====Send Headers=========================\r\n
0xb000084a | %1: =====Send Entity==========================\r\n
0xb000084b | %1: =====Send Complete========================\r\n
0xb0000852 | %1: =====Receive Headers======================\r\n
0xb0000853 | %1: =====Receive Entity=======================\r\n
0xb0000854 | %1: =====Receive Complete=====================\r\n
0xb000085c | %1: =====Request Restart======================\r\n
0xb000085d | %1: =====Request Done=========================\r\n
0xb000ea58 | Restore Thread Token %1 (Error: %2)\r\n
0xb000ea59 | Set Thread Token %1 (OldToken %2) (Error: %3)\r\n
0xb000ea5a | Get Thread Token %1 (Error: %3) (SID: %2)\r\n
0xb000ea5b | Canceling %2 Thread Action (Context: %1)\r\n
0xb000ea5c | Queue %2 Thread Action (Context: %1)\r\n
0xb000ea5d | Stopping %2 Thread Action (Context: %1)\r\n
0xb000ea5e | Starting %2 Thread Action (Context: %1)\r\n
0xb000ea5f | %2\r\n
0xd0000001 | STATUS_SUCCESS\r\n
0xd0000002 | SEC_E_INSUFFICIENT_MEMORY\r\n
0xd0000003 | SEC_E_INVALID_HANDLE\r\n
0xd0000004 | SEC_E_UNSUPPORTED_FUNCTION\r\n
0xd0000005 | SEC_E_TARGET_UNKNOWN\r\n
0xd0000006 | SEC_E_INTERNAL_ERROR\r\n
0xd0000007 | SEC_E_SECPKG_NOT_FOUND\r\n
0xd0000008 | SEC_E_NOT_OWNER\r\n
0xd0000009 | SEC_E_CANNOT_INSTALL\r\n
0xd000000a | SEC_E_INVALID_TOKEN\r\n
0xd000000b | SEC_E_CANNOT_PACK\r\n
0xd000000c | SEC_E_QOP_NOT_SUPPORTED\r\n
0xd000000d | SEC_E_NO_IMPERSONATION\r\n
0xd000000e | SEC_E_LOGON_DENIED\r\n
0xd000000f | SEC_E_UNKNOWN_CREDENTIALS\r\n
0xd0000010 | SEC_E_NO_CREDENTIALS\r\n
0xd0000011 | SEC_E_MESSAGE_ALTERED\r\n
0xd0000012 | SEC_E_OUT_OF_SEQUENCE\r\n
0xd0000013 | SEC_E_NO_AUTHENTICATING_AUTHORITY\r\n
0xd0000014 | SEC_I_CONTINUE_NEEDED\r\n
0xd0000015 | SEC_I_COMPLETE_NEEDED\r\n
0xd0000016 | SEC_I_COMPLETE_AND_CONTINUE\r\n
0xd0000017 | SEC_I_LOCAL_LOGON\r\n
0xd0000018 | SEC_E_BAD_PKGID\r\n
0xd0000019 | SEC_E_CONTEXT_EXPIRED\r\n
0xd000001a | SEC_E_INCOMPLETE_MESSAGE\r\n
0xd000001b | CERT_E_EXPIRED\r\n
0xd000001c | CERT_E_VALIDITYPERIODNESTING\r\n
0xd000001d | CERT_E_UNTRUSTEDROOT\r\n
0xd000001e | CERT_E_CHAINING\r\n
0xd000001f | CERT_E_CN_NO_MATCH\r\n
0xd0000020 | CERT_E_INVALID_NAME\r\n
0xd0000021 | CERT_E_WRONG_USAGE\r\n
0xd0000022 | CRYPT_E_REVOKED\r\n
0xd0000023 | TRUST_E_EXPLICIT_DISTRUST\r\n
0xd0000024 | CRYPT_E_NO_REVOCATION_CHECK\r\n
0xd0000025 | CRYPT_E_REVOCATION_OFFLINE\r\n
0xd0000026 | CERT_E_ROLE\r\n
0xd0000027 | CERT_E_PATHLENCONST\r\n
0xd0000028 | CERT_E_CRITICAL\r\n
0xd0000029 | CERT_E_PURPOSE\r\n
0xd000002a | CERT_E_ISSUERCHAINING\r\n
0xd000002b | CERT_E_MALFORMED\r\n
0xd000002c | TRUST_E_CERT_SIGNATURE\r\n
0xd000002d | CERT_E_INVALID_POLICY\r\n
0xd000002e | TRUST_E_BASIC_CONSTRAINTS\r\n
0xd000002f | Local Graceful\r\n
0xd0000030 | Remote Graceful\r\n
0xd0000031 | Local Reset\r\n
0xd0000032 | Remote Reset\r\n
0xd0000033 | Connect Timeout\r\n
0xd0000034 | Send Timeout\r\n
0xd0000035 | Receive Timeout\r\n
0xd0000036 | Scavenged\r\n
0xd0000037 | No Reason\r\n
0xd0000038 | Cleanup after hitting an error condition\r\n
0xd0000039 | Timer\r\n
0xd000003a | WorkItem\r\n
0xd000003b | Overlapped IO\r\n
0xd000003c | No Error\r\n
0xd000003d | Unable to Get Cert\r\n
0xd000003e | NULL cert context\r\n
0xd000003f | Unable to Get Cert Chain\r\n
0xd0000040 | Unable to Process URL to Hostname\r\n
0xd0000041 | Cert Validation Failure\r\n
0xd0000042 | Unable to get Stream Sizes\r\n
0xd0000043 | Unable to get Endpoint Bindings\r\n
0xd0000044 | Unable to get secure connection information\r\n
0xd0000045 | AuthSchemeState\r\n
0xd0000046 | DisableAuthentication\r\n
0xd0000047 | ClientCertificate\r\n
0xd0000048 | ClientCertificateIssuerList\r\n
0xd0000049 | ChannelBindingToken\r\n
0xd000004a | IgnoredServerCertErrors\r\n
0xd000004b | SecureProtocols\r\n
0xd000004c | ProxyAuthSchemes\r\n
0xd000004d | ProxyAuthState\r\n
0xd000004e | ProxyAutoLogonState\r\n
0xd000004f | ProxyConfig\r\n
0xd0000050 | ProxyConnectHeaders\r\n
0xd0000051 | ProxyCreds\r\n
0xd0000052 | ProxySpnUsage\r\n
0xd0000053 | RedirectionLimit\r\n
0xd0000054 | SecureProtocolInformation\r\n
0xd0000055 | ServerAuthSchemes\r\n
0xd0000056 | ServerAuthState\r\n
0xd0000057 | ServerAutoLogonState\r\n
0xd0000058 | ServerCert\r\n
0xd0000059 | ServerCreds\r\n
0xd000005a | ServerSpnUsage\r\n
0xd000005b | SocketAddress\r\n
0xd000005c | ThirdPartyCookies\r\n
0xd000005d | PathCodePage\r\n
0xd000005e | ExtraInfoCodePage\r\n
0xd000005f | ServerCertErrors\r\n
0xd0000060 | CookiesEnabled\r\n
0xd0000061 | ResponseHeadersSizeLimit\r\n
0xd0000062 | ServerSpnUsed\r\n
0xd0000063 | ProxySpnUsed\r\n
0xd0000064 | ConnectTimeout\r\n
0xd0000065 | ResolveTimeout\r\n
0xd0000066 | SendTimeout\r\n
0xd0000067 | ReceiveTimeout\r\n
0xd0000068 | ConnectRetryCount\r\n
0xd0000069 | RevertToSelfClientCertificate\r\n
0xd000006a | NetworkInterfaceAffinity\r\n
0xd000006b | TcpAutoTuningRestricted\r\n
0xd000006c | DnsIdnTransformDisabled\r\n
0xd000006d | PeerDistExtension\r\n
0xd000006e | MaximumConnectCount\r\n
0xd000006f | GlobalKeepAlivePoolState\r\n
0xd0000070 | ConnectionState\r\n
0xd0000071 | ExceededResponseHeaderSizeLimit\r\n
0xf0000001 | SP_PROT_PCT1_SERVER\r\n
0xf0000002 | SP_PROT_PCT1_CLIENT\r\n
0xf0000003 | SP_PROT_SSL2_SERVER\r\n
0xf0000004 | SP_PROT_SSL2_CLIENT\r\n
0xf0000005 | SP_PROT_SSL3_SERVER\r\n
0xf0000006 | SP_PROT_SSL3_CLIENT\r\n
0xf0000007 | SP_PROT_TLS1_SERVER\r\n
0xf0000008 | SP_PROT_TLS1_CLIENT\r\n
0xf0000009 | SP_PROT_TLS1_1_SERVER\r\n
0xf000000a | SP_PROT_TLS1_1_CLIENT\r\n
0xf000000b | SP_PROT_TLS1_2_SERVER\r\n
0xf000000c | SP_PROT_TLS1_2_CLIENT\r\n
0xf000000d | SP_PROT_UNI_SERVER\r\n
0xf000000e | SP_PROT_UNI_CLIENT\r\n

### 6.1.7601.17514

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000021 | SEND\r\n
0x10000022 | RECEIVE\r\n
0x10000023 | L3_CONNECT\r\n
0x10000025 | CLOSE\r\n
0x10000026 | SECURITY\r\n
0x10000027 | CONFIGURATION\r\n
0x10000028 | GLOBAL\r\n
0x10000029 | DROPPED\r\n
0x1000002a | PII_PRESENT\r\n
0x1000002b | PACKET\r\n
0x1000002c | ADDRESS\r\n
0x1000002d | CONTEXT_EVENT\r\n
0x1000002e | STATE_TRANSITION\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | NOOP\r\n
0x3000000b | Queue\r\n
0x3000000c | Cancel\r\n
0x3000000d | Get\r\n
0x3000000e | Set\r\n
0x3000000f | Reallocate\r\n
0x30000010 | Reset\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000006d | WebIOAPI\r\n
0x7000006e | WebIODebug\r\n
0x7000006f | ApiInit\r\n
0x70000070 | ApiTerminate\r\n
0x70000071 | Session Create\r\n
0x70000072 | SessionClose\r\n
0x70000073 | SyncApiWait\r\n
0x700000c8 | RequestCreate\r\n
0x700000c9 | RequestConfiguration\r\n
0x700000ca | RequestClose\r\n
0x70000190 | RequestHeader\r\n
0x70000191 | ProxyResolution\r\n
0x70000193 | Endpoint\r\n
0x70000194 | RequestGenerateHeaders\r\n
0x70000195 | RequestSendEntity\r\n
0x70000196 | RequestEntityTracker\r\n
0x70000197 | RequestEntityCompleteCallback\r\n
0x70000198 | ResponseRecieveEntity\r\n
0x70000199 | ResponseEntityCompleteCallback\r\n
0x7000019a | RequestWaitingForConnection\r\n
0x7000019b | ResponseParser\r\n
0x7000019c | ResponseDirectReceiveEntity\r\n
0x7000019d | RequestSend\r\n
0x7000019e | ResponseReceive\r\n
0x7000019f | ResponseConnectionBufferReceive\r\n
0x700001a0 | RequestCancel\r\n
0x700001a1 | ConnectionSocketConnect\r\n
0x700001a2 | ConnectionSocketCreate\r\n
0x700001a3 | ConnectionSocketClose\r\n
0x700001a4 | ConnectionNameResolution\r\n
0x700001a5 | ConnectionSocketSend\r\n
0x700001a7 | ConnectionSocketReceive\r\n
0x700001a8 | SSLEncryptMessage\r\n
0x700001a9 | SSLInitializeSecurityContext\r\n
0x700001aa | SSLSendEntity\r\n
0x700001ab | SSLCertValidation\r\n
0x700001ac | SSLReceiveEntity\r\n
0x700001ad | SSLDecryptMessage\r\n
0x700001ae | SSLConnectionBufferReceive\r\n
0x700001af | ThreadToken\r\n
0x700001b0 | ResponseReceiveCompleteCallback\r\n
0x700001b1 | ThreadAction\r\n
0x700001b2 | Information\r\n
0x700001b3 | ConnectionNameResolutionRequest\r\n
0x700001b4 | SSLAcquireCredentialsHandle\r\n
0x70000385 | RequestState\r\n
0xb0000001 | %1: WebInitialize completed successfully (ApiVersion %3) (Flags %4) -> (API Handle = %2).\r\n
0xb0000002 | WebInitialize failed with an error = %5 (ApiVersion %3) (Flags %4)\r\n
0xb0000003 | %1 WebTerminate completed successfully. (Handle %2) (Flags %3)\r\n
0xb0000004 | %1 WebTerminate failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000005 | %3: WebCreateSession completed successfully. (ApiHandle %1[%2]) (Flags: %5) -> (Session Handle: %4)\r\n
0xb0000006 | %1: WebCreateSession failed with an error = %6. (ApiHandle %1[%2]) (Flags: %5)\r\n
0xb0000007 | %1: WebCloseSession called (Handle %2) (Flags %3)\r\n
0xb0000008 | %1: WebCloseSession failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000009 | %2(%1) API called.\r\n
0xb000000a | %2(%1) API returned successfully.\r\n
0xb000000b | %2(%1) API failed with an error = %3.\r\n
0xb000000c | %2(%1) API pending completion.\r\n
0xb000000d | %2(%1) API completed.\r\n
0xb000000e | %2(%1) API completed with an error = %3.\r\n
0xb000000f | %1: Set Request Option %3 (Handle %2) (Error %6) (Length %4) (Value %5) \r\n
0xb0000011 | %1: WebCreateHttpRequest completed successfully. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8) -> (Request Handle %2) \r\n
0xb0000012 | %3: WebCreateHttpRequest failed with error: %9. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8)\r\n
0xb0000013 | %1: WebCloseHttpRequest called (Handle %2) (Flags %3) \r\n
0xb0000014 | %1 WebCloseHttpRequest failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000015 | Synchronous API Event Handle Signall (Event %2) (Error %3) (Information %4)\r\n
0xb0000016 | Synchronous API Event Handle Wait Completed (Handle %1) (Event %2) (Error %3) (Information %4)\r\n
0xb0000017 | %1: WebSetHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000018 | %1: WebSetHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000019 | %1: WebRemoveHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001a | %1: WebRemoveHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3)\r\n
0xb000001b | %1: Indicating informational callback to request. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001c | %1: Informational callback to request complete. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001d | %1: WebCloseSession completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001e | %1: WebCloseHttpRequest completed sucessfully error = %4. (Handle %2) (Flags %3)\r\n
0xb0000064 | %1: Sending Headers: %3\r\n
0xb0000065 | %1: Received Headers: %3\r\n
0xb0000066 | %1: Starting Proxy Resolution\r\n
0xb0000067 | %1: Completed Proxy Resolution\r\n
0xb0000068 | %1: Acquired a connection slot (ConnMgr: %2), (Connection: %3)\r\n
0xb0000069 | %1: Request on Endpoint (Server Endpoint: %2) (Proxy Endpoint: %3) (Connection Manager: %4)\r\n
0xb000006a | %1: Request Message Generated (DataChunk %2[%3])\r\n
0xb000006b | %1: WebSendHttpRequestEntity (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006c | %1: WebSendHttpRequestEntity Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006d | %1: HTTP Queuing Entity for Sending (DataChunks %2) (ChunkLength %3) (IsEntity %4) (All Entity Posted? %5)\r\n
0xb000006e | %1: HTTP Sending Entity (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb000006f | %1: HTTP Send Entity Details (Connection: %2) (DataChunks %3) (Index %4) (Buffer %5 [%6]) Data: %7\r\n
0xb0000070 | %1: HTTP Sending Entity Complete (Error %6) (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb0000071 | %1: Completing WebSendHttpRequest(Entity) (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000072 | %1: Completing WebSendHttpRequest(Entity) Complete (DataChunks %2)\r\n
0xb0000073 | %1: WebHttpReceiveEntityBody (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000074 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000075 | %1: Completing WebHttpReceiveEntityBody (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000076 | %1: Completing WebHttpReceiveEntityBody Complete (DataChunks %2)\r\n
0xb0000077 | %1: HTTP Connection changing Buffer (OldBuffer %2 [%3]) (NewBuffer %5 [%6]) (Carryover %4)\r\n
0xb0000078 | %1: HTTP Connection Buffer Posting Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6])\r\n
0xb0000079 | %1: HTTP Connection Buffer Completing Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6]) (Error %7)  (CompletionInformation %8)\r\n
0xb000007a | %1: HTTP Connection Buffer Receive Details (DataChunks %2) (Length %3) Data: %4\r\n
0xb000007b | %1: HTTP Parser (Connection %2) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007c | %1: HTTP Parser Complete (Connection %2) (Error %9) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007d | %1: HTTP Parser Reset (Buffer %2) (HttpResponseCode %3)\r\n
0xb000007e | %1: HTTP Receive From Parser (DataChunk %2) (ParserChunk %3 [%4]) (Error %5) (Context %6) (Information %7)\r\n
0xb000007f | %1: HTTP Receive (DataChunk %2) (BytesToRecv %3)\r\n
0xb0000080 | %1: HTTP Receive Complete (DataChunk %2) (BytesToRecv %3) (Error %4) (Context %5) (Information %6)\r\n
0xb0000081 | %1: HTTP Receive Entity Details (DataChunk %2) (Index %3) (Length %4) Data %5\r\n
0xb0000082 | %1: WebSendHttpRequest (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000083 | %1: WebSendHttpRequest Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000084 | %1: WebHttpReceiveResponse (Handle: %2) (Flags %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000085 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %6) (Flags: %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000086 | %1: Completing WebHttpReceiveEntityBody (Error %3) (ResponseFlags %2) (CompletionInformation %4)\r\n
0xb0000087 | %1: Completing WebHttpReceiveEntityBody Complete\r\n
0xb0000088 | %1: WebCancelHttpRequest (Handle: %2) (Flags %3)\r\n
0xb0000089 | %1: WebCancelHttpRequest Complete (Error: %4) (Handle: %2) (Flags %3)\r\n
0xb00000c8 | %1: Connecting (Socket %2) (Context %5) (RemaingAddress %6) Address: %4.\r\n
0xb00000c9 | %1: Connection established (Socket %2) (Context %5)\r\n
0xb00000ca | %1: Connect failed with error %7 (Socket %2) (Context %5) (RemaingAddress %6)\r\n
0xb00000cb | Socket %2 created on Endpoint %1.\r\n
0xb00000cc | %1: Socket %2 Closed (Reason = %3, Status = %4).\r\n
0xb00000cd | %1: Name Resolution Request (Name %2) (Timeout %3) (CompletionContext: %4)\r\n
0xb00000ce | %1: Name Resolution Request Completed (FQDN %2) (Canonical %3) (AddressCount: %4) AddressData: %6\r\n
0xb00000cf | %1: Name Resolution Request Failed (Error %2)\r\n
0xb00000d0 | %1: Name Resolution Request queued to %2\r\n
0xb00000d1 | %1: Name Resolution Request is cancelled\r\n
0xb00000d2 | %1: Name Resolution Request Timed-out\r\n
0xb00000d3 | %1: Resolving addresses (Host %2) (Flags: %3)\r\n
0xb00000d4 | %1: Address resolution completed (Error = %4) (Host %2) (Flags: %3).(AddressCount %5)\r\n
0xb00000d5 | %1: Winsock Send Entity Start(DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d6 | %1: Winsock Send Entity Complete (Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d7 | %1: Winsock Recv Entity Start (DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d8 | %1: Winsock Recv Entity Complete(Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00002bc | %1: InitializeSecurityContext - Credential Handle(%2:%3) Context Handle (%4:%5) (Hostname %6) (InputFlags %7) (Buffer %8 [%9/%10])\r\n
0xb00002bf | %1: InitializeSecurityContext returned - (%14) Credential Handle(%2:%3) Context Handle (%4:%5) (OutputFlags %11) (Buffer %8 [%9/%10]) (DataChunk %12 [%13])\r\n
0xb00002c0 | %1: InitializeSecurityContext Details (Pre) - Credential Handle(%2:%3) (Buffer %4 [%5/%6]) Data: %7\r\n
0xb00002c1 | %1: InitializeSecurityContext Details (Post) - Credential Handle(%2:%3) (DataChunk %4 [%5]) Data: %6\r\n
0xb00002c2 | %1: SSL Encryption (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c3 | %1: SSL Encryption Complete (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (InBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c4 | %1: SSL Encryption Failed (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (Flags %9) \r\n
0xb00002c5 | %1: SSL Encryption Details (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9) Data:%10\r\n
0xb00002c6 | %1: SSL Queue Send Entity (SSLIOContext %2) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c7 | %1: SSL Send Entity Complete (SSLIOContext: %2) (Error: %5) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c8 | %1: SSL Cert Validation - (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002c9 | %1: SSL Cert Validation Failure - %7 (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002d0 | %1: SSL Queue Recv Entity Data Chunk (SSLIOContext %2) (DataChunks: %3)\r\n
0xb00002d1 | %1: SSL Filling Up Recv Entity Data Chunk (SSLIOContext: %2) (DataChunks: %3) (PlainData %4[%5]) (Information: %6)\r\n
0xb00002d2 | %1: SSL Decryption - Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d3 | %1: SSL Decryption Complete (SecStatus %9) (Error %10) Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d4 | %1: SSL Receive Buffer Posting Receive (DataChunk %2) (Buffer %3[%4/%5])\r\n
0xb00002d5 | %1: SSL Receive Buffer Receive Complete (DataChunk %2) (Error %7) (Information %6) (Buffer %3[%4/%5])\r\n
0xb00002d6 | %1: SSL Receive Buffer Details: (Buffer %2[%3/%4]) Data: %5\r\n
0xb00002d7 | %1: SSL Receive Buffer Posting Receive (Buffer %2) (NewBuffer: %3)\r\n
0xb00002d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002d9 | %1: SSL AcquireCredentialsHandle returned - (%7) Credential Handle(%5:%6) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002da | %1: SSL AcquireCredentialsHandle failed - (%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb0000834 | %1: =====Request Initialize===================\r\n
0xb0000835 | %1: =====Query Endpoints======================\r\n
0xb0000836 | %1: =====Waiting For Available Connection=====\r\n
0xb000083f | %1: =====Request Connect======================\r\n
0xb0000840 | %1: =====Name Resolution======================\r\n
0xb0000841 | %1: =====TCP Connect==========================\r\n
0xb0000842 | %1: =====SSL Negotiation======================\r\n
0xb0000848 | %1: =====Generate Headers=====================\r\n
0xb0000849 | %1: =====Send Headers=========================\r\n
0xb000084a | %1: =====Send Entity==========================\r\n
0xb000084b | %1: =====Send Complete========================\r\n
0xb0000852 | %1: =====Receive Headers======================\r\n
0xb0000853 | %1: =====Receive Entity=======================\r\n
0xb0000854 | %1: =====Receive Complete=====================\r\n
0xb000085c | %1: =====Request Restart======================\r\n
0xb000085d | %1: =====Request Done=========================\r\n
0xb000ea58 | Restore Thread Token %1 (Error: %2)\r\n
0xb000ea59 | Set Thread Token %1 (OldToken %2) (Error: %3)\r\n
0xb000ea5a | Get Thread Token %1 (Error: %3) (SID: %2)\r\n
0xb000ea5b | Canceling %2 Thread Action (Context: %1)\r\n
0xb000ea5c | Queue %2 Thread Action (Context: %1)\r\n
0xb000ea5d | Stopping %2 Thread Action (Context: %1)\r\n
0xb000ea5e | Starting %2 Thread Action (Context: %1)\r\n
0xb000ea5f | %2\r\n
0xd0000001 | STATUS_SUCCESS\r\n
0xd0000002 | SEC_E_INSUFFICIENT_MEMORY\r\n
0xd0000003 | SEC_E_INVALID_HANDLE\r\n
0xd0000004 | SEC_E_UNSUPPORTED_FUNCTION\r\n
0xd0000005 | SEC_E_TARGET_UNKNOWN\r\n
0xd0000006 | SEC_E_INTERNAL_ERROR\r\n
0xd0000007 | SEC_E_SECPKG_NOT_FOUND\r\n
0xd0000008 | SEC_E_NOT_OWNER\r\n
0xd0000009 | SEC_E_CANNOT_INSTALL\r\n
0xd000000a | SEC_E_INVALID_TOKEN\r\n
0xd000000b | SEC_E_CANNOT_PACK\r\n
0xd000000c | SEC_E_QOP_NOT_SUPPORTED\r\n
0xd000000d | SEC_E_NO_IMPERSONATION\r\n
0xd000000e | SEC_E_LOGON_DENIED\r\n
0xd000000f | SEC_E_UNKNOWN_CREDENTIALS\r\n
0xd0000010 | SEC_E_NO_CREDENTIALS\r\n
0xd0000011 | SEC_E_MESSAGE_ALTERED\r\n
0xd0000012 | SEC_E_OUT_OF_SEQUENCE\r\n
0xd0000013 | SEC_E_NO_AUTHENTICATING_AUTHORITY\r\n
0xd0000014 | SEC_I_CONTINUE_NEEDED\r\n
0xd0000015 | SEC_I_COMPLETE_NEEDED\r\n
0xd0000016 | SEC_I_COMPLETE_AND_CONTINUE\r\n
0xd0000017 | SEC_I_LOCAL_LOGON\r\n
0xd0000018 | SEC_E_BAD_PKGID\r\n
0xd0000019 | SEC_E_CONTEXT_EXPIRED\r\n
0xd000001a | SEC_E_INCOMPLETE_MESSAGE\r\n
0xd000001b | CERT_E_EXPIRED\r\n
0xd000001c | CERT_E_VALIDITYPERIODNESTING\r\n
0xd000001d | CERT_E_UNTRUSTEDROOT\r\n
0xd000001e | CERT_E_CHAINING\r\n
0xd000001f | CERT_E_CN_NO_MATCH\r\n
0xd0000020 | CERT_E_INVALID_NAME\r\n
0xd0000021 | CERT_E_WRONG_USAGE\r\n
0xd0000022 | CRYPT_E_REVOKED\r\n
0xd0000023 | TRUST_E_EXPLICIT_DISTRUST\r\n
0xd0000024 | CRYPT_E_NO_REVOCATION_CHECK\r\n
0xd0000025 | CRYPT_E_REVOCATION_OFFLINE\r\n
0xd0000026 | CERT_E_ROLE\r\n
0xd0000027 | CERT_E_PATHLENCONST\r\n
0xd0000028 | CERT_E_CRITICAL\r\n
0xd0000029 | CERT_E_PURPOSE\r\n
0xd000002a | CERT_E_ISSUERCHAINING\r\n
0xd000002b | CERT_E_MALFORMED\r\n
0xd000002c | TRUST_E_CERT_SIGNATURE\r\n
0xd000002d | CERT_E_INVALID_POLICY\r\n
0xd000002e | TRUST_E_BASIC_CONSTRAINTS\r\n
0xd000002f | Local Graceful\r\n
0xd0000030 | Remote Graceful\r\n
0xd0000031 | Local Reset\r\n
0xd0000032 | Remote Reset\r\n
0xd0000033 | Connect Timeout\r\n
0xd0000034 | Send Timeout\r\n
0xd0000035 | Receive Timeout\r\n
0xd0000036 | Scavenged\r\n
0xd0000037 | No Reason\r\n
0xd0000038 | Cleanup after hitting an error condition\r\n
0xd0000039 | Timer\r\n
0xd000003a | WorkItem\r\n
0xd000003b | Overlapped IO\r\n
0xd000003c | No Error\r\n
0xd000003d | Unable to Get Cert\r\n
0xd000003e | NULL cert context\r\n
0xd000003f | Unable to Get Cert Chain\r\n
0xd0000040 | Unable to Process URL to Hostname\r\n
0xd0000041 | Cert Validation Failure\r\n
0xd0000042 | Unable to get Stream Sizes\r\n
0xd0000043 | Unable to get Endpoint Bindings\r\n
0xd0000044 | Unable to get secure connection information\r\n
0xd0000045 | AuthSchemeState\r\n
0xd0000046 | DisableAuthentication\r\n
0xd0000047 | ClientCertificate\r\n
0xd0000048 | ClientCertificateIssuerList\r\n
0xd0000049 | ChannelBindingToken\r\n
0xd000004a | IgnoredServerCertErrors\r\n
0xd000004b | SecureProtocols\r\n
0xd000004c | ProxyAuthSchemes\r\n
0xd000004d | ProxyAuthState\r\n
0xd000004e | ProxyAutoLogonState\r\n
0xd000004f | ProxyConfig\r\n
0xd0000050 | ProxyConnectHeaders\r\n
0xd0000051 | ProxyCreds\r\n
0xd0000052 | ProxySpnUsage\r\n
0xd0000053 | RedirectionLimit\r\n
0xd0000054 | SecureProtocolInformation\r\n
0xd0000055 | ServerAuthSchemes\r\n
0xd0000056 | ServerAuthState\r\n
0xd0000057 | ServerAutoLogonState\r\n
0xd0000058 | ServerCert\r\n
0xd0000059 | ServerCreds\r\n
0xd000005a | ServerSpnUsage\r\n
0xd000005b | SocketAddress\r\n
0xd000005c | ThirdPartyCookies\r\n
0xd000005d | PathCodePage\r\n
0xd000005e | ExtraInfoCodePage\r\n
0xd000005f | ServerCertErrors\r\n
0xd0000060 | CookiesEnabled\r\n
0xd0000061 | ResponseHeadersSizeLimit\r\n
0xd0000062 | ServerSpnUsed\r\n
0xd0000063 | ProxySpnUsed\r\n
0xd0000064 | ConnectTimeout\r\n
0xd0000065 | ResolveTimeout\r\n
0xd0000066 | SendTimeout\r\n
0xd0000067 | ReceiveTimeout\r\n
0xd0000068 | ConnectRetryCount\r\n
0xd0000069 | UnsafeHeaderParsing\r\n
0xd000006a | RevertToSelfClientCertificate\r\n
0xd000006b | NetworkInterfaceAffinity\r\n
0xd000006c | TcpAutoTuningRestricted\r\n
0xd000006d | DnsIdnTransformDisabled\r\n
0xd000006e | PeerDistExtension\r\n
0xd000006f | MaximumConnectCount\r\n
0xd0000070 | GlobalKeepAlivePoolState\r\n
0xd0000071 | ConnectionState\r\n
0xd0000072 | ExceededResponseHeaderSizeLimit\r\n
0xf0000001 | SP_PROT_PCT1_SERVER\r\n
0xf0000002 | SP_PROT_PCT1_CLIENT\r\n
0xf0000003 | SP_PROT_SSL2_SERVER\r\n
0xf0000004 | SP_PROT_SSL2_CLIENT\r\n
0xf0000005 | SP_PROT_SSL3_SERVER\r\n
0xf0000006 | SP_PROT_SSL3_CLIENT\r\n
0xf0000007 | SP_PROT_TLS1_SERVER\r\n
0xf0000008 | SP_PROT_TLS1_CLIENT\r\n
0xf0000009 | SP_PROT_TLS1_1_SERVER\r\n
0xf000000a | SP_PROT_TLS1_1_CLIENT\r\n
0xf000000b | SP_PROT_TLS1_2_SERVER\r\n
0xf000000c | SP_PROT_TLS1_2_CLIENT\r\n
0xf000000d | SP_PROT_UNI_SERVER\r\n
0xf000000e | SP_PROT_UNI_CLIENT\r\n

### 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000021 | SEND\r\n
0x10000022 | RECEIVE\r\n
0x10000023 | L3_CONNECT\r\n
0x10000025 | CLOSE\r\n
0x10000026 | SECURITY\r\n
0x10000027 | CONFIGURATION\r\n
0x10000028 | GLOBAL\r\n
0x10000029 | DROPPED\r\n
0x1000002a | PII_PRESENT\r\n
0x1000002b | PACKET\r\n
0x1000002c | ADDRESS\r\n
0x1000002d | CONTEXT_EVENT\r\n
0x1000002e | STATE_TRANSITION\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | NOOP\r\n
0x3000000b | Queue\r\n
0x3000000c | Cancel\r\n
0x3000000d | Get\r\n
0x3000000e | Set\r\n
0x3000000f | Reallocate\r\n
0x30000010 | Reset\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000006d | WebIOAPI\r\n
0x7000006e | WebIODebug\r\n
0x7000006f | ApiInit\r\n
0x70000070 | ApiTerminate\r\n
0x70000071 | Session Create\r\n
0x70000072 | SessionClose\r\n
0x70000073 | SyncApiWait\r\n
0x700000c8 | RequestCreate\r\n
0x700000c9 | RequestConfiguration\r\n
0x700000ca | RequestClose\r\n
0x70000190 | RequestHeader\r\n
0x70000191 | ProxyResolution\r\n
0x70000193 | Endpoint\r\n
0x70000194 | RequestGenerateHeaders\r\n
0x70000195 | RequestSendEntity\r\n
0x70000196 | RequestEntityTracker\r\n
0x70000197 | RequestEntityCompleteCallback\r\n
0x70000198 | ResponseRecieveEntity\r\n
0x70000199 | ResponseEntityCompleteCallback\r\n
0x7000019a | RequestWaitingForConnection\r\n
0x7000019b | ResponseParser\r\n
0x7000019c | ResponseDirectReceiveEntity\r\n
0x7000019d | RequestSend\r\n
0x7000019e | ResponseReceive\r\n
0x7000019f | ResponseConnectionBufferReceive\r\n
0x700001a0 | RequestCancel\r\n
0x700001a1 | ConnectionSocketConnect\r\n
0x700001a2 | ConnectionSocketCreate\r\n
0x700001a3 | ConnectionSocketClose\r\n
0x700001a4 | ConnectionNameResolution\r\n
0x700001a5 | ConnectionSocketSend\r\n
0x700001a7 | ConnectionSocketReceive\r\n
0x700001a8 | SSLEncryptMessage\r\n
0x700001a9 | SSLInitializeSecurityContext\r\n
0x700001aa | SSLSendEntity\r\n
0x700001ab | SSLCertValidation\r\n
0x700001ac | SSLReceiveEntity\r\n
0x700001ad | SSLDecryptMessage\r\n
0x700001ae | SSLConnectionBufferReceive\r\n
0x700001af | ThreadToken\r\n
0x700001b0 | ResponseReceiveCompleteCallback\r\n
0x700001b1 | ThreadAction\r\n
0x700001b2 | Information\r\n
0x700001b3 | ConnectionNameResolutionRequest\r\n
0x700001b4 | SSLAcquireCredentialsHandle\r\n
0x700001f4 | ProtocolSendData\r\n
0x700001f5 | ProtocolSendDataCallback\r\n
0x700001f6 | ProtocolReceiveData\r\n
0x700001f7 | ProtocolReceiveDataCallback\r\n
0x700001f8 | ProtocolCancelHandle\r\n
0x700001f9 | ProtocolConfiguration\r\n
0x700001fa | CompleteProtocolUpgrade\r\n
0x700001fb | CloseProtocolHandle\r\n
0x70000385 | RequestState\r\n
0xb0000001 | %1: WebInitialize completed successfully (ApiVersion %3) (Flags %4) -> (API Handle = %2).\r\n
0xb0000002 | WebInitialize failed with an error = %5 (ApiVersion %3) (Flags %4)\r\n
0xb0000003 | %1 WebTerminate completed successfully. (Handle %2) (Flags %3)\r\n
0xb0000004 | %1 WebTerminate failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000005 | %3: WebCreateSession completed successfully. (ApiHandle %1[%2]) (Flags: %5) -> (Session Handle: %4)\r\n
0xb0000006 | %1: WebCreateSession failed with an error = %6. (ApiHandle %1[%2]) (Flags: %5)\r\n
0xb0000007 | %1: WebCloseSession called (Handle %2) (Flags %3)\r\n
0xb0000008 | %1: WebCloseSession failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000009 | %2(%1) API called.\r\n
0xb000000a | %2(%1) API returned successfully.\r\n
0xb000000b | %2(%1) API failed with an error = %3.\r\n
0xb000000c | %2(%1) API pending completion.\r\n
0xb000000d | %2(%1) API completed.\r\n
0xb000000e | %2(%1) API completed with an error = %3.\r\n
0xb000000f | %1: Set Request Option %3 (Handle %2) (Error %6) (Length %4) (Value %5)\r\n
0xb0000011 | %1: WebCreateHttpRequest completed successfully. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8) -> (Request Handle %2)\r\n
0xb0000012 | %3: WebCreateHttpRequest failed with error: %9. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8)\r\n
0xb0000013 | %1: WebCloseHttpRequest called (Handle %2) (Flags %3)\r\n
0xb0000014 | %1 WebCloseHttpRequest failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000015 | Synchronous API Event Handle Signall (Event %2) (Error %3) (Information %4)\r\n
0xb0000016 | Synchronous API Event Handle Wait Completed (Handle %1) (Event %2) (Error %3) (Information %4)\r\n
0xb0000017 | %1: WebSetHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000018 | %1: WebSetHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000019 | %1: WebRemoveHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001a | %1: WebRemoveHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3)\r\n
0xb000001b | %1: Indicating informational callback to request. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001c | %1: Informational callback to request complete. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001d | %1: WebCloseSession completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001e | %1: WebCloseHttpRequest completed sucessfully error = %4. (Handle %2) (Flags %3)\r\n
0xb0000064 | %1: Sending Headers: %3\r\n
0xb0000065 | %1: Received Headers: %3\r\n
0xb0000066 | %1: Starting Proxy Resolution\r\n
0xb0000067 | %1: Completed Proxy Resolution\r\n
0xb0000068 | %1: Acquired a connection slot (ConnMgr: %2), (Connection: %3)\r\n
0xb0000069 | %1: Request on Endpoint (Server Endpoint: %2) (Proxy Endpoint: %3) (Connection Manager: %4)\r\n
0xb000006a | %1: Request Message Generated (DataChunk %2[%3])\r\n
0xb000006b | %1: WebSendHttpRequestEntity (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006c | %1: WebSendHttpRequestEntity Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006d | %1: HTTP Queuing Entity for Sending (DataChunks %2) (ChunkLength %3) (IsEntity %4) (All Entity Posted? %5)\r\n
0xb000006e | %1: HTTP Sending Entity (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb000006f | %1: HTTP Send Entity Details (Connection: %2) (DataChunks %3) (Index %4) (Buffer %5 [%6]) Data: %7\r\n
0xb0000070 | %1: HTTP Sending Entity Complete (Error %6) (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb0000071 | %1: Completing WebSendHttpRequest(Entity) (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000072 | %1: Completing WebSendHttpRequest(Entity) Complete (DataChunks %2)\r\n
0xb0000073 | %1: WebHttpReceiveEntityBody (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000074 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000075 | %1: Completing WebHttpReceiveEntityBody (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000076 | %1: Completing WebHttpReceiveEntityBody Complete (DataChunks %2)\r\n
0xb0000077 | %1: HTTP Connection changing Buffer (OldBuffer %2 [%3]) (NewBuffer %5 [%6]) (Carryover %4)\r\n
0xb0000078 | %1: HTTP Connection Buffer Posting Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6])\r\n
0xb0000079 | %1: HTTP Connection Buffer Completing Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6]) (Error %7)  (CompletionInformation %8)\r\n
0xb000007a | %1: HTTP Connection Buffer Receive Details (DataChunks %2) (Length %3) Data: %4\r\n
0xb000007b | %1: HTTP Parser (Connection %2) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007c | %1: HTTP Parser Complete (Connection %2) (Error %9) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007d | %1: HTTP Parser Reset (Buffer %2) (HttpResponseCode %3)\r\n
0xb000007e | %1: HTTP Receive From Parser (DataChunk %2) (ParserChunk %3 [%4]) (Error %5) (Context %6) (Information %7)\r\n
0xb000007f | %1: HTTP Receive (DataChunk %2) (BytesToRecv %3)\r\n
0xb0000080 | %1: HTTP Receive Complete (DataChunk %2) (BytesToRecv %3) (Error %4) (Context %5) (Information %6)\r\n
0xb0000081 | %1: HTTP Receive Entity Details (DataChunk %2) (Index %3) (Length %4) Data %5\r\n
0xb0000082 | %1: WebSendHttpRequest (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000083 | %1: WebSendHttpRequest Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000084 | %1: WebHttpReceiveResponse (Handle: %2) (Flags %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000085 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %6) (Flags: %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000086 | %1: Completing WebHttpReceiveEntityBody (Error %3) (ResponseFlags %2) (CompletionInformation %4)\r\n
0xb0000087 | %1: Completing WebHttpReceiveEntityBody Complete\r\n
0xb0000088 | %1: WebCancelHttpRequest (Handle: %2) (Flags %3)\r\n
0xb0000089 | %1: WebCancelHttpRequest Complete (Error: %4) (Handle: %2) (Flags %3)\r\n
0xb00000c8 | %1: Connecting (Socket %2) (Context %5) (RemaingAddress %6) Address: %4.\r\n
0xb00000c9 | %1: Connection established (Socket %2) (Context %5)\r\n
0xb00000ca | %1: Connect failed with error %7 (Socket %2) (Context %5) (RemaingAddress %6)\r\n
0xb00000cb | Socket %2 created on Endpoint %1.\r\n
0xb00000cc | %1: Socket %2 Closed (Reason = %3, Status = %4).\r\n
0xb00000cd | %1: Name Resolution Request (Name %2) (Timeout %3) (CompletionContext: %4)\r\n
0xb00000ce | %1: Name Resolution Request Completed (FQDN %2) (Canonical %3) (AddressCount: %4) AddressData: %6\r\n
0xb00000cf | %1: Name Resolution Request Failed (Error %2)\r\n
0xb00000d0 | %1: Name Resolution Request queued to %2\r\n
0xb00000d1 | %1: Name Resolution Request is cancelled\r\n
0xb00000d2 | %1: Name Resolution Request Timed-out\r\n
0xb00000d3 | %1: Resolving addresses (Host %2) (Flags: %3)\r\n
0xb00000d4 | %1: Address resolution completed (Error = %4) (Host %2) (Flags: %3).(AddressCount %5)\r\n
0xb00000d5 | %1: Winsock Send Entity Start(DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d6 | %1: Winsock Send Entity Complete (Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d7 | %1: Winsock Recv Entity Start (DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d8 | %1: Winsock Recv Entity Complete(Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00002bc | %1: InitializeSecurityContext - Credential Handle(%2:%3) Context Handle (%4:%5) (Hostname %6) (InputFlags %7) (Buffer %8 [%9/%10])\r\n
0xb00002bf | %1: InitializeSecurityContext returned - (%14) Credential Handle(%2:%3) Context Handle (%4:%5) (OutputFlags %11) (Buffer %8 [%9/%10]) (DataChunk %12 [%13])\r\n
0xb00002c0 | %1: InitializeSecurityContext Details (Pre) - Credential Handle(%2:%3) (Buffer %4 [%5/%6]) Data: %7\r\n
0xb00002c1 | %1: InitializeSecurityContext Details (Post) - Credential Handle(%2:%3) (DataChunk %4 [%5]) Data: %6\r\n
0xb00002c2 | %1: SSL Encryption (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c3 | %1: SSL Encryption Complete (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (InBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c4 | %1: SSL Encryption Failed (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (Flags %9) \r\n
0xb00002c5 | %1: SSL Encryption Details (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9) Data:%10\r\n
0xb00002c6 | %1: SSL Queue Send Entity (SSLIOContext %2) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c7 | %1: SSL Send Entity Complete (SSLIOContext: %2) (Error: %5) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c8 | %1: SSL Cert Validation - (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002c9 | %1: SSL Cert Validation Failure - %7 (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002d0 | %1: SSL Queue Recv Entity Data Chunk (SSLIOContext %2) (DataChunks: %3)\r\n
0xb00002d1 | %1: SSL Filling Up Recv Entity Data Chunk (SSLIOContext: %2) (DataChunks: %3) (PlainData %4[%5]) (Information: %6)\r\n
0xb00002d2 | %1: SSL Decryption - Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d3 | %1: SSL Decryption Complete (SecStatus %9) (Error %10) Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d4 | %1: SSL Receive Buffer Posting Receive (DataChunk %2) (Buffer %3[%4/%5])\r\n
0xb00002d5 | %1: SSL Receive Buffer Receive Complete (DataChunk %2) (Error %7) (Information %6) (Buffer %3[%4/%5])\r\n
0xb00002d6 | %1: SSL Receive Buffer Details: (Buffer %2[%3/%4]) Data: %5\r\n
0xb00002d7 | %1: SSL Receive Buffer Posting Receive (Buffer %2) (NewBuffer: %3)\r\n
0xb00002d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002d9 | %1: SSL AcquireCredentialsHandle returned - (%7) Credential Handle(%5:%6) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002da | %1: SSL AcquireCredentialsHandle failed - (%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb0000384 | %1: WebCompleteProtocolUpgrade completed successfully. (Handle %2) (Request %3[%4]) (Session %5[%6])\r\n
0xb0000385 | %1: WebCompleteProtocolUpgrade failed with error: %7. (Handle %2) (Request %3[%4]) (Session %5[%6])\r\n
0xb0000386 | %1: WebProtocolCancelHandle (Handle: %2)\r\n
0xb0000387 | %1: WebProtocolCancelHandle Complete (Error: %3) (Handle: %2)\r\n
0xb0000388 | %1: WebCloseProtocolHandle called (Handle %2)\r\n
0xb0000389 | %1: WebCloseProtocolHandle completed (Error %4) (Handle %2)\r\n
0xb000038a | %1: Set Protocol Option %3 (Handle %2) (Error %6) (Length %4) (Value %5)\r\n
0xb000038b | %1: WebProtocolSendData (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000038c | %1: WebProtocolSendData Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000038d | %1: Completing WebProtocolSendData (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb000038e | %1: Completing WebProtocolSendData Complete (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb000038f | %1: WebProtocolReceiveData (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000390 | %1: WebProtocolReceiveData Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000391 | %1: Completing WebProtocolReceiveData (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb0000392 | %1: Completing WebProtocolReceiveData Complete (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb0000834 | %1: =====Request Initialize===================\r\n
0xb0000835 | %1: =====Query Endpoints======================\r\n
0xb0000836 | %1: =====Waiting For Available Connection=====\r\n
0xb000083f | %1: =====Request Connect======================\r\n
0xb0000840 | %1: =====Name Resolution======================\r\n
0xb0000841 | %1: =====TCP Connect==========================\r\n
0xb0000842 | %1: =====SSL Negotiation======================\r\n
0xb0000848 | %1: =====Generate Headers=====================\r\n
0xb0000849 | %1: =====Send Headers=========================\r\n
0xb000084a | %1: =====Send Entity==========================\r\n
0xb000084b | %1: =====Send Complete========================\r\n
0xb0000852 | %1: =====Receive Headers======================\r\n
0xb0000853 | %1: =====Receive Entity=======================\r\n
0xb0000854 | %1: =====Receive Complete=====================\r\n
0xb000085c | %1: =====Request Restart======================\r\n
0xb000085d | %1: =====Request Done=========================\r\n
0xb000ea58 | Restore Thread Token %1 (Error: %2)\r\n
0xb000ea59 | Set Thread Token %1 (OldToken %2) (Error: %3)\r\n
0xb000ea5a | Get Thread Token %1 (Error: %3) (SID: %2)\r\n
0xb000ea5b | Canceling %2 Thread Action (Context: %1)\r\n
0xb000ea5c | Queue %2 Thread Action (Context: %1)\r\n
0xb000ea5d | Stopping %2 Thread Action (Context: %1)\r\n
0xb000ea5e | Starting %2 Thread Action (Context: %1)\r\n
0xb000ea5f | %2\r\n
0xb00102d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xb00102d9 | %1: SSL AcquireCredentialsHandle returned - (%8) Credential Handle(%6:%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xb00102da | %1: SSL AcquireCredentialsHandle failed - (%8) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xd0000001 | STATUS_SUCCESS\r\n
0xd0000002 | SEC_E_INSUFFICIENT_MEMORY\r\n
0xd0000003 | SEC_E_INVALID_HANDLE\r\n
0xd0000004 | SEC_E_UNSUPPORTED_FUNCTION\r\n
0xd0000005 | SEC_E_TARGET_UNKNOWN\r\n
0xd0000006 | SEC_E_INTERNAL_ERROR\r\n
0xd0000007 | SEC_E_SECPKG_NOT_FOUND\r\n
0xd0000008 | SEC_E_NOT_OWNER\r\n
0xd0000009 | SEC_E_CANNOT_INSTALL\r\n
0xd000000a | SEC_E_INVALID_TOKEN\r\n
0xd000000b | SEC_E_CANNOT_PACK\r\n
0xd000000c | SEC_E_QOP_NOT_SUPPORTED\r\n
0xd000000d | SEC_E_NO_IMPERSONATION\r\n
0xd000000e | SEC_E_LOGON_DENIED\r\n
0xd000000f | SEC_E_UNKNOWN_CREDENTIALS\r\n
0xd0000010 | SEC_E_NO_CREDENTIALS\r\n
0xd0000011 | SEC_E_MESSAGE_ALTERED\r\n
0xd0000012 | SEC_E_OUT_OF_SEQUENCE\r\n
0xd0000013 | SEC_E_NO_AUTHENTICATING_AUTHORITY\r\n
0xd0000014 | SEC_I_CONTINUE_NEEDED\r\n
0xd0000015 | SEC_I_COMPLETE_NEEDED\r\n
0xd0000016 | SEC_I_COMPLETE_AND_CONTINUE\r\n
0xd0000017 | SEC_I_LOCAL_LOGON\r\n
0xd0000018 | SEC_E_BAD_PKGID\r\n
0xd0000019 | SEC_E_CONTEXT_EXPIRED\r\n
0xd000001a | SEC_E_INCOMPLETE_MESSAGE\r\n
0xd000001b | CERT_E_EXPIRED\r\n
0xd000001c | CERT_E_VALIDITYPERIODNESTING\r\n
0xd000001d | CERT_E_UNTRUSTEDROOT\r\n
0xd000001e | CERT_E_CHAINING\r\n
0xd000001f | CERT_E_CN_NO_MATCH\r\n
0xd0000020 | CERT_E_INVALID_NAME\r\n
0xd0000021 | CERT_E_WRONG_USAGE\r\n
0xd0000022 | CRYPT_E_REVOKED\r\n
0xd0000023 | TRUST_E_EXPLICIT_DISTRUST\r\n
0xd0000024 | CRYPT_E_NO_REVOCATION_CHECK\r\n
0xd0000025 | CRYPT_E_REVOCATION_OFFLINE\r\n
0xd0000026 | CERT_E_ROLE\r\n
0xd0000027 | CERT_E_PATHLENCONST\r\n
0xd0000028 | CERT_E_CRITICAL\r\n
0xd0000029 | CERT_E_PURPOSE\r\n
0xd000002a | CERT_E_ISSUERCHAINING\r\n
0xd000002b | CERT_E_MALFORMED\r\n
0xd000002c | TRUST_E_CERT_SIGNATURE\r\n
0xd000002d | CERT_E_INVALID_POLICY\r\n
0xd000002e | TRUST_E_BASIC_CONSTRAINTS\r\n
0xd000002f | Local Graceful\r\n
0xd0000030 | Remote Graceful\r\n
0xd0000031 | Local Reset\r\n
0xd0000032 | Remote Reset\r\n
0xd0000033 | Connect Timeout\r\n
0xd0000034 | Send Timeout\r\n
0xd0000035 | Receive Timeout\r\n
0xd0000036 | Scavenged\r\n
0xd0000037 | No Reason\r\n
0xd0000038 | Cleanup after hitting an error condition\r\n
0xd0000039 | Timer\r\n
0xd000003a | WorkItem\r\n
0xd000003b | Overlapped IO\r\n
0xd000003c | No Error\r\n
0xd000003d | Unable to Get Cert\r\n
0xd000003e | NULL cert context\r\n
0xd000003f | Unable to Get Cert Chain\r\n
0xd0000040 | Unable to Process URL to Hostname\r\n
0xd0000041 | Cert Validation Failure\r\n
0xd0000042 | Unable to get Stream Sizes\r\n
0xd0000043 | Unable to get Endpoint Bindings\r\n
0xd0000044 | Unable to get secure connection information\r\n
0xd0000045 | AuthSchemeState\r\n
0xd0000046 | DisableAuthentication\r\n
0xd0000047 | ClientCertificate\r\n
0xd0000048 | ClientCertificateIssuerList\r\n
0xd0000049 | ChannelBindingToken\r\n
0xd000004a | IgnoredServerCertErrors\r\n
0xd000004b | SecureProtocols\r\n
0xd000004c | ProxyAuthSchemes\r\n
0xd000004d | ProxyAuthState\r\n
0xd000004e | ProxyAutoLogonState\r\n
0xd000004f | ProxyConfig\r\n
0xd0000050 | ProxyConnectHeaders\r\n
0xd0000051 | ProxyCreds\r\n
0xd0000052 | ProxySpnUsage\r\n
0xd0000053 | RedirectionLimit\r\n
0xd0000054 | SecureProtocolInformation\r\n
0xd0000055 | ServerAuthSchemes\r\n
0xd0000056 | ServerAuthState\r\n
0xd0000057 | ServerAutoLogonState\r\n
0xd0000058 | ServerCert\r\n
0xd0000059 | ServerCreds\r\n
0xd000005a | ServerSpnUsage\r\n
0xd000005b | SocketAddress\r\n
0xd000005c | ThirdPartyCookies\r\n
0xd000005d | PathCodePage\r\n
0xd000005e | ExtraInfoCodePage\r\n
0xd000005f | ServerCertErrors\r\n
0xd0000060 | CookiesEnabled\r\n
0xd0000061 | ResponseHeadersSizeLimit\r\n
0xd0000062 | ServerSpnUsed\r\n
0xd0000063 | ProxySpnUsed\r\n
0xd0000064 | ConnectTimeout\r\n
0xd0000065 | ResolveTimeout\r\n
0xd0000066 | SendTimeout\r\n
0xd0000067 | ReceiveTimeout\r\n
0xd0000068 | ConnectRetryCount\r\n
0xd0000069 | UnsafeHeaderParsing\r\n
0xd000006a | RevertToSelfClientCertificate\r\n
0xd000006b | NetworkInterfaceAffinity\r\n
0xd000006c | TcpAutoTuningRestricted\r\n
0xd000006d | DnsIdnTransformDisabled\r\n
0xd000006e | PeerDistExtension\r\n
0xd000006f | MaximumConnectCount\r\n
0xd0000070 | GlobalKeepAlivePoolState\r\n
0xd0000071 | ConnectionState\r\n
0xd0000072 | ExceededResponseHeaderSizeLimit\r\n
0xd0000073 | DnsInterfaceAffinity\r\n
0xf0000001 | SP_PROT_PCT1_SERVER\r\n
0xf0000002 | SP_PROT_PCT1_CLIENT\r\n
0xf0000003 | SP_PROT_SSL2_SERVER\r\n
0xf0000004 | SP_PROT_SSL2_CLIENT\r\n
0xf0000005 | SP_PROT_SSL3_SERVER\r\n
0xf0000006 | SP_PROT_SSL3_CLIENT\r\n
0xf0000007 | SP_PROT_TLS1_SERVER\r\n
0xf0000008 | SP_PROT_TLS1_CLIENT\r\n
0xf0000009 | SP_PROT_TLS1_1_SERVER\r\n
0xf000000a | SP_PROT_TLS1_1_CLIENT\r\n
0xf000000b | SP_PROT_TLS1_2_SERVER\r\n
0xf000000c | SP_PROT_TLS1_2_CLIENT\r\n
0xf000000d | SP_PROT_UNI_SERVER\r\n
0xf000000e | SP_PROT_UNI_CLIENT\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000021 | SEND\r\n
0x10000022 | RECEIVE\r\n
0x10000023 | L3_CONNECT\r\n
0x10000025 | CLOSE\r\n
0x10000026 | SECURITY\r\n
0x10000027 | CONFIGURATION\r\n
0x10000028 | GLOBAL\r\n
0x10000029 | DROPPED\r\n
0x1000002a | PII_PRESENT\r\n
0x1000002b | PACKET\r\n
0x1000002c | ADDRESS\r\n
0x1000002d | CONTEXT_EVENT\r\n
0x1000002e | STATE_TRANSITION\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | NOOP\r\n
0x3000000b | Queue\r\n
0x3000000c | Cancel\r\n
0x3000000d | Get\r\n
0x3000000e | Set\r\n
0x3000000f | Reallocate\r\n
0x30000010 | Reset\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000006d | WebIOAPI\r\n
0x7000006e | WebIODebug\r\n
0x7000006f | ApiInit\r\n
0x70000070 | ApiTerminate\r\n
0x70000071 | Session Create\r\n
0x70000072 | SessionClose\r\n
0x70000073 | SyncApiWait\r\n
0x700000c8 | RequestCreate\r\n
0x700000c9 | RequestConfiguration\r\n
0x700000ca | RequestClose\r\n
0x70000190 | RequestHeader\r\n
0x70000191 | ProxyResolution\r\n
0x70000193 | Endpoint\r\n
0x70000194 | RequestGenerateHeaders\r\n
0x70000195 | RequestSendEntity\r\n
0x70000196 | RequestEntityTracker\r\n
0x70000197 | RequestEntityCompleteCallback\r\n
0x70000198 | ResponseRecieveEntity\r\n
0x70000199 | ResponseEntityCompleteCallback\r\n
0x7000019a | RequestWaitingForConnection\r\n
0x7000019b | ResponseParser\r\n
0x7000019c | ResponseDirectReceiveEntity\r\n
0x7000019d | RequestSend\r\n
0x7000019e | ResponseReceive\r\n
0x7000019f | ResponseConnectionBufferReceive\r\n
0x700001a0 | RequestCancel\r\n
0x700001a1 | ConnectionSocketConnect\r\n
0x700001a2 | ConnectionSocketCreate\r\n
0x700001a3 | ConnectionSocketClose\r\n
0x700001a4 | ConnectionNameResolution\r\n
0x700001a5 | ConnectionSocketSend\r\n
0x700001a7 | ConnectionSocketReceive\r\n
0x700001a8 | SSLEncryptMessage\r\n
0x700001a9 | SSLInitializeSecurityContext\r\n
0x700001aa | SSLSendEntity\r\n
0x700001ab | SSLCertValidation\r\n
0x700001ac | SSLReceiveEntity\r\n
0x700001ad | SSLDecryptMessage\r\n
0x700001ae | SSLConnectionBufferReceive\r\n
0x700001af | ThreadToken\r\n
0x700001b0 | ResponseReceiveCompleteCallback\r\n
0x700001b1 | ThreadAction\r\n
0x700001b2 | Information\r\n
0x700001b3 | ConnectionNameResolutionRequest\r\n
0x700001b4 | SSLAcquireCredentialsHandle\r\n
0x700001f4 | ProtocolSendData\r\n
0x700001f5 | ProtocolSendDataCallback\r\n
0x700001f6 | ProtocolReceiveData\r\n
0x700001f7 | ProtocolReceiveDataCallback\r\n
0x700001f8 | ProtocolCancelHandle\r\n
0x700001f9 | ProtocolConfiguration\r\n
0x700001fa | CompleteProtocolUpgrade\r\n
0x700001fb | CloseProtocolHandle\r\n
0x70000385 | RequestState\r\n
0xb0000001 | %1: WebInitialize completed successfully (ApiVersion %3) (Flags %4) -> (API Handle = %2).\r\n
0xb0000002 | WebInitialize failed with an error = %5 (ApiVersion %3) (Flags %4)\r\n
0xb0000003 | %1 WebTerminate completed successfully. (Handle %2) (Flags %3)\r\n
0xb0000004 | %1 WebTerminate failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000005 | %3: WebCreateSession completed successfully. (ApiHandle %1[%2]) (Flags: %5) -> (Session Handle: %4)\r\n
0xb0000006 | %1: WebCreateSession failed with an error = %6. (ApiHandle %1[%2]) (Flags: %5)\r\n
0xb0000007 | %1: WebCloseSession called (Handle %2) (Flags %3)\r\n
0xb0000008 | %1: WebCloseSession failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000009 | %2(%1) API called.\r\n
0xb000000a | %2(%1) API returned successfully.\r\n
0xb000000b | %2(%1) API failed with an error = %3.\r\n
0xb000000c | %2(%1) API pending completion.\r\n
0xb000000d | %2(%1) API completed.\r\n
0xb000000e | %2(%1) API completed with an error = %3.\r\n
0xb000000f | %1: Set Request Option %3 (Handle %2) (Error %6) (Length %4) (Value %5)\r\n
0xb0000011 | %1: WebCreateHttpRequest completed successfully. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8) -> (Request Handle %2)\r\n
0xb0000012 | %3: WebCreateHttpRequest failed with error: %9. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8)\r\n
0xb0000013 | %1: WebCloseHttpRequest called (Handle %2) (Flags %3)\r\n
0xb0000014 | %1 WebCloseHttpRequest failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000015 | Synchronous API Event Handle Signall (Event %2) (Error %3) (Information %4)\r\n
0xb0000016 | Synchronous API Event Handle Wait Completed (Handle %1) (Event %2) (Error %3) (Information %4)\r\n
0xb0000017 | %1: WebSetHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000018 | %1: WebSetHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000019 | %1: WebRemoveHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001a | %1: WebRemoveHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3)\r\n
0xb000001b | %1: Indicating informational callback to request. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001c | %1: Informational callback to request complete. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001d | %1: WebCloseSession completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001e | %1: WebCloseHttpRequest completed sucessfully error = %4. (Handle %2) (Flags %3)\r\n
0xb0000064 | %1: Sending Headers: %3\r\n
0xb0000065 | %1: Received Headers: %3\r\n
0xb0000066 | %1: Starting Proxy Resolution\r\n
0xb0000067 | %1: Completed Proxy Resolution\r\n
0xb0000068 | %1: Acquired a connection slot (ConnMgr: %2), (Connection: %3)\r\n
0xb0000069 | %1: Request on Endpoint (Server Endpoint: %2) (Proxy Endpoint: %3) (Connection Manager: %4)\r\n
0xb000006a | %1: Request Message Generated (DataChunk %2[%3])\r\n
0xb000006b | %1: WebSendHttpRequestEntity (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006c | %1: WebSendHttpRequestEntity Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006d | %1: HTTP Queuing Entity for Sending (DataChunks %2) (ChunkLength %3) (IsEntity %4) (All Entity Posted? %5)\r\n
0xb000006e | %1: HTTP Sending Entity (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb000006f | %1: HTTP Send Entity Details (Connection: %2) (DataChunks %3) (Index %4) (Buffer %5 [%6]) Data: %7\r\n
0xb0000070 | %1: HTTP Sending Entity Complete (Error %6) (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb0000071 | %1: Completing WebSendHttpRequest(Entity) (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000072 | %1: Completing WebSendHttpRequest(Entity) Complete (DataChunks %2)\r\n
0xb0000073 | %1: WebHttpReceiveEntityBody (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000074 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000075 | %1: Completing WebHttpReceiveEntityBody (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000076 | %1: Completing WebHttpReceiveEntityBody Complete (DataChunks %2)\r\n
0xb0000077 | %1: HTTP Connection changing Buffer (OldBuffer %2 [%3]) (NewBuffer %5 [%6]) (Carryover %4)\r\n
0xb0000078 | %1: HTTP Connection Buffer Posting Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6])\r\n
0xb0000079 | %1: HTTP Connection Buffer Completing Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6]) (Error %7)  (CompletionInformation %8)\r\n
0xb000007a | %1: HTTP Connection Buffer Receive Details (DataChunks %2) (Length %3) Data: %4\r\n
0xb000007b | %1: HTTP Parser (Connection %2) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007c | %1: HTTP Parser Complete (Connection %2) (Error %9) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007d | %1: HTTP Parser Reset (Buffer %2) (HttpResponseCode %3)\r\n
0xb000007e | %1: HTTP Receive From Parser (DataChunk %2) (ParserChunk %3 [%4]) (Error %5) (Context %6) (Information %7)\r\n
0xb000007f | %1: HTTP Receive (DataChunk %2) (BytesToRecv %3)\r\n
0xb0000080 | %1: HTTP Receive Complete (DataChunk %2) (BytesToRecv %3) (Error %4) (Context %5) (Information %6)\r\n
0xb0000081 | %1: HTTP Receive Entity Details (DataChunk %2) (Index %3) (Length %4) Data %5\r\n
0xb0000082 | %1: WebSendHttpRequest (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000083 | %1: WebSendHttpRequest Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000084 | %1: WebHttpReceiveResponse (Handle: %2) (Flags %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000085 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %6) (Flags: %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000086 | %1: Completing WebHttpReceiveEntityBody (Error %3) (ResponseFlags %2) (CompletionInformation %4)\r\n
0xb0000087 | %1: Completing WebHttpReceiveEntityBody Complete\r\n
0xb0000088 | %1: WebCancelHttpRequest (Handle: %2) (Flags %3)\r\n
0xb0000089 | %1: WebCancelHttpRequest Complete (Error: %4) (Handle: %2) (Flags %3)\r\n
0xb00000c8 | %1: Connecting (Socket %2) (Context %5) (RemaingAddress %6) Address: %4.\r\n
0xb00000c9 | %1: Connection established (Socket %2) (Context %5)\r\n
0xb00000ca | %1: Connect failed with error %7 (Socket %2) (Context %5) (RemaingAddress %6)\r\n
0xb00000cb | Socket %2 created on Endpoint %1.\r\n
0xb00000cc | %1: Socket %2 Closed (Reason = %3, Status = %4).\r\n
0xb00000cd | %1: Name Resolution Request (Name %2) (Timeout %3) (CompletionContext: %4)\r\n
0xb00000ce | %1: Name Resolution Request Completed (FQDN %2) (Canonical %3) (AddressCount: %4) AddressData: %6\r\n
0xb00000cf | %1: Name Resolution Request Failed (Error %2)\r\n
0xb00000d0 | %1: Name Resolution Request queued to %2\r\n
0xb00000d1 | %1: Name Resolution Request is cancelled\r\n
0xb00000d2 | %1: Name Resolution Request Timed-out\r\n
0xb00000d3 | %1: Resolving addresses (Host %2) (Flags: %3)\r\n
0xb00000d4 | %1: Address resolution completed (Error = %4) (Host %2) (Flags: %3).(AddressCount %5)\r\n
0xb00000d5 | %1: Winsock Send Entity Start(DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d6 | %1: Winsock Send Entity Complete (Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d7 | %1: Winsock Recv Entity Start (DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d8 | %1: Winsock Recv Entity Complete(Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00002bc | %1: InitializeSecurityContext - Credential Handle(%2:%3) Context Handle (%4:%5) (Hostname %6) (InputFlags %7) (Buffer %8 [%9/%10])\r\n
0xb00002bf | %1: InitializeSecurityContext returned - (%14) Credential Handle(%2:%3) Context Handle (%4:%5) (OutputFlags %11) (Buffer %8 [%9/%10]) (DataChunk %12 [%13])\r\n
0xb00002c0 | %1: InitializeSecurityContext Details (Pre) - Credential Handle(%2:%3) (Buffer %4 [%5/%6]) Data: %7\r\n
0xb00002c1 | %1: InitializeSecurityContext Details (Post) - Credential Handle(%2:%3) (DataChunk %4 [%5]) Data: %6\r\n
0xb00002c2 | %1: SSL Encryption (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c3 | %1: SSL Encryption Complete (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (InBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c4 | %1: SSL Encryption Failed (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (Flags %9) \r\n
0xb00002c5 | %1: SSL Encryption Details (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9) Data:%10\r\n
0xb00002c6 | %1: SSL Queue Send Entity (SSLIOContext %2) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c7 | %1: SSL Send Entity Complete (SSLIOContext: %2) (Error: %5) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c8 | %1: SSL Cert Validation - (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002c9 | %1: SSL Cert Validation Failure - %7 (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002d0 | %1: SSL Queue Recv Entity Data Chunk (SSLIOContext %2) (DataChunks: %3)\r\n
0xb00002d1 | %1: SSL Filling Up Recv Entity Data Chunk (SSLIOContext: %2) (DataChunks: %3) (PlainData %4[%5]) (Information: %6)\r\n
0xb00002d2 | %1: SSL Decryption - Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d3 | %1: SSL Decryption Complete (SecStatus %9) (Error %10) Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d4 | %1: SSL Receive Buffer Posting Receive (DataChunk %2) (Buffer %3[%4/%5])\r\n
0xb00002d5 | %1: SSL Receive Buffer Receive Complete (DataChunk %2) (Error %7) (Information %6) (Buffer %3[%4/%5])\r\n
0xb00002d6 | %1: SSL Receive Buffer Details: (Buffer %2[%3/%4]) Data: %5\r\n
0xb00002d7 | %1: SSL Receive Buffer Posting Receive (Buffer %2) (NewBuffer: %3)\r\n
0xb00002d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002d9 | %1: SSL AcquireCredentialsHandle returned - (%7) Credential Handle(%5:%6) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002da | %1: SSL AcquireCredentialsHandle failed - (%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb0000384 | %1: WebCompleteProtocolUpgrade completed successfully. (Handle %2) (Request %3[%4]) (Session %5[%6])\r\n
0xb0000385 | %1: WebCompleteProtocolUpgrade failed with error: %7. (Handle %2) (Request %3[%4]) (Session %5[%6])\r\n
0xb0000386 | %1: WebProtocolCancelHandle (Handle: %2)\r\n
0xb0000387 | %1: WebProtocolCancelHandle Complete (Error: %3) (Handle: %2)\r\n
0xb0000388 | %1: WebCloseProtocolHandle called (Handle %2)\r\n
0xb0000389 | %1: WebCloseProtocolHandle completed (Error %4) (Handle %2)\r\n
0xb000038a | %1: Set Protocol Option %3 (Handle %2) (Error %6) (Length %4) (Value %5)\r\n
0xb000038b | %1: WebProtocolSendData (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000038c | %1: WebProtocolSendData Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000038d | %1: Completing WebProtocolSendData (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb000038e | %1: Completing WebProtocolSendData Complete (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb000038f | %1: WebProtocolReceiveData (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000390 | %1: WebProtocolReceiveData Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000391 | %1: Completing WebProtocolReceiveData (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb0000392 | %1: Completing WebProtocolReceiveData Complete (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb0000834 | %1: =====Request Initialize===================\r\n
0xb0000835 | %1: =====Query Endpoints======================\r\n
0xb0000836 | %1: =====Waiting For Available Connection=====\r\n
0xb000083f | %1: =====Request Connect======================\r\n
0xb0000840 | %1: =====Name Resolution======================\r\n
0xb0000841 | %1: =====TCP Connect==========================\r\n
0xb0000842 | %1: =====SSL Negotiation======================\r\n
0xb0000848 | %1: =====Generate Headers=====================\r\n
0xb0000849 | %1: =====Send Headers=========================\r\n
0xb000084a | %1: =====Send Entity==========================\r\n
0xb000084b | %1: =====Send Complete========================\r\n
0xb0000852 | %1: =====Receive Headers======================\r\n
0xb0000853 | %1: =====Receive Entity=======================\r\n
0xb0000854 | %1: =====Receive Complete=====================\r\n
0xb000085c | %1: =====Request Restart======================\r\n
0xb000085d | %1: =====Request Done=========================\r\n
0xb000ea58 | Restore Thread Token %1 (Error: %2)\r\n
0xb000ea59 | Set Thread Token %1 (OldToken %2) (Error: %3)\r\n
0xb000ea5a | Get Thread Token %1 (Error: %3) (SID: %2)\r\n
0xb000ea5b | Canceling %2 Thread Action (Context: %1)\r\n
0xb000ea5c | Queue %2 Thread Action (Context: %1)\r\n
0xb000ea5d | Stopping %2 Thread Action (Context: %1)\r\n
0xb000ea5e | Starting %2 Thread Action (Context: %1)\r\n
0xb000ea5f | %2\r\n
0xb00102d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xb00102d9 | %1: SSL AcquireCredentialsHandle returned - (%8) Credential Handle(%6:%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xb00102da | %1: SSL AcquireCredentialsHandle failed - (%8) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xd0000001 | STATUS_SUCCESS\r\n
0xd0000002 | SEC_E_INSUFFICIENT_MEMORY\r\n
0xd0000003 | SEC_E_INVALID_HANDLE\r\n
0xd0000004 | SEC_E_UNSUPPORTED_FUNCTION\r\n
0xd0000005 | SEC_E_TARGET_UNKNOWN\r\n
0xd0000006 | SEC_E_INTERNAL_ERROR\r\n
0xd0000007 | SEC_E_SECPKG_NOT_FOUND\r\n
0xd0000008 | SEC_E_NOT_OWNER\r\n
0xd0000009 | SEC_E_CANNOT_INSTALL\r\n
0xd000000a | SEC_E_INVALID_TOKEN\r\n
0xd000000b | SEC_E_CANNOT_PACK\r\n
0xd000000c | SEC_E_QOP_NOT_SUPPORTED\r\n
0xd000000d | SEC_E_NO_IMPERSONATION\r\n
0xd000000e | SEC_E_LOGON_DENIED\r\n
0xd000000f | SEC_E_UNKNOWN_CREDENTIALS\r\n
0xd0000010 | SEC_E_NO_CREDENTIALS\r\n
0xd0000011 | SEC_E_MESSAGE_ALTERED\r\n
0xd0000012 | SEC_E_OUT_OF_SEQUENCE\r\n
0xd0000013 | SEC_E_NO_AUTHENTICATING_AUTHORITY\r\n
0xd0000014 | SEC_I_CONTINUE_NEEDED\r\n
0xd0000015 | SEC_I_COMPLETE_NEEDED\r\n
0xd0000016 | SEC_I_COMPLETE_AND_CONTINUE\r\n
0xd0000017 | SEC_I_LOCAL_LOGON\r\n
0xd0000018 | SEC_E_BAD_PKGID\r\n
0xd0000019 | SEC_E_CONTEXT_EXPIRED\r\n
0xd000001a | SEC_E_INCOMPLETE_MESSAGE\r\n
0xd000001b | CERT_E_EXPIRED\r\n
0xd000001c | CERT_E_VALIDITYPERIODNESTING\r\n
0xd000001d | CERT_E_UNTRUSTEDROOT\r\n
0xd000001e | CERT_E_CHAINING\r\n
0xd000001f | CERT_E_CN_NO_MATCH\r\n
0xd0000020 | CERT_E_INVALID_NAME\r\n
0xd0000021 | CERT_E_WRONG_USAGE\r\n
0xd0000022 | CRYPT_E_REVOKED\r\n
0xd0000023 | TRUST_E_EXPLICIT_DISTRUST\r\n
0xd0000024 | CRYPT_E_NO_REVOCATION_CHECK\r\n
0xd0000025 | CRYPT_E_REVOCATION_OFFLINE\r\n
0xd0000026 | CERT_E_ROLE\r\n
0xd0000027 | CERT_E_PATHLENCONST\r\n
0xd0000028 | CERT_E_CRITICAL\r\n
0xd0000029 | CERT_E_PURPOSE\r\n
0xd000002a | CERT_E_ISSUERCHAINING\r\n
0xd000002b | CERT_E_MALFORMED\r\n
0xd000002c | TRUST_E_CERT_SIGNATURE\r\n
0xd000002d | CERT_E_INVALID_POLICY\r\n
0xd000002e | TRUST_E_BASIC_CONSTRAINTS\r\n
0xd000002f | Local Graceful\r\n
0xd0000030 | Remote Graceful\r\n
0xd0000031 | Local Reset\r\n
0xd0000032 | Remote Reset\r\n
0xd0000033 | Connect Timeout\r\n
0xd0000034 | Send Timeout\r\n
0xd0000035 | Receive Timeout\r\n
0xd0000036 | Scavenged\r\n
0xd0000037 | No Reason\r\n
0xd0000038 | Cleanup after hitting an error condition\r\n
0xd0000039 | Timer\r\n
0xd000003a | WorkItem\r\n
0xd000003b | Overlapped IO\r\n
0xd000003c | No Error\r\n
0xd000003d | Unable to Get Cert\r\n
0xd000003e | NULL cert context\r\n
0xd000003f | Unable to Get Cert Chain\r\n
0xd0000040 | Unable to Process URL to Hostname\r\n
0xd0000041 | Cert Validation Failure\r\n
0xd0000042 | Unable to get Stream Sizes\r\n
0xd0000043 | Unable to get Endpoint Bindings\r\n
0xd0000044 | Unable to get secure connection information\r\n
0xd0000045 | AuthSchemeState\r\n
0xd0000046 | DisableAuthentication\r\n
0xd0000047 | ClientCertificate\r\n
0xd0000048 | ClientCertificateIssuerList\r\n
0xd0000049 | ChannelBindingToken\r\n
0xd000004a | IgnoredServerCertErrors\r\n
0xd000004b | SecureProtocols\r\n
0xd000004c | ProxyAuthSchemes\r\n
0xd000004d | ProxyAuthState\r\n
0xd000004e | ProxyAutoLogonState\r\n
0xd000004f | ProxyConfig\r\n
0xd0000050 | ProxyConnectHeaders\r\n
0xd0000051 | ProxyCreds\r\n
0xd0000052 | ProxySpnUsage\r\n
0xd0000053 | RedirectionLimit\r\n
0xd0000054 | SecureProtocolInformation\r\n
0xd0000055 | ServerAuthSchemes\r\n
0xd0000056 | ServerAuthState\r\n
0xd0000057 | ServerAutoLogonState\r\n
0xd0000058 | ServerCert\r\n
0xd0000059 | ServerCreds\r\n
0xd000005a | ServerSpnUsage\r\n
0xd000005b | SocketAddress\r\n
0xd000005c | ThirdPartyCookies\r\n
0xd000005d | PathCodePage\r\n
0xd000005e | ExtraInfoCodePage\r\n
0xd000005f | ServerCertErrors\r\n
0xd0000060 | CookiesEnabled\r\n
0xd0000061 | ResponseHeadersSizeLimit\r\n
0xd0000062 | ServerSpnUsed\r\n
0xd0000063 | ProxySpnUsed\r\n
0xd0000064 | ConnectTimeout\r\n
0xd0000065 | ResolveTimeout\r\n
0xd0000066 | SendTimeout\r\n
0xd0000067 | ReceiveTimeout\r\n
0xd0000068 | ConnectRetryCount\r\n
0xd0000069 | UnsafeHeaderParsing\r\n
0xd000006a | RevertToSelfClientCertificate\r\n
0xd000006b | NetworkInterfaceAffinity\r\n
0xd000006c | TcpAutoTuningRestricted\r\n
0xd000006d | DnsIdnTransformDisabled\r\n
0xd000006e | PeerDistExtension\r\n
0xd000006f | MaximumConnectCount\r\n
0xd0000070 | GlobalKeepAlivePoolState\r\n
0xd0000071 | ConnectionState\r\n
0xd0000072 | ExceededResponseHeaderSizeLimit\r\n
0xd0000073 | DnsInterfaceAffinity\r\n
0xd0000074 | ConnectionIdleTimeout\r\n
0xf0000001 | SP_PROT_PCT1_SERVER\r\n
0xf0000002 | SP_PROT_PCT1_CLIENT\r\n
0xf0000003 | SP_PROT_SSL2_SERVER\r\n
0xf0000004 | SP_PROT_SSL2_CLIENT\r\n
0xf0000005 | SP_PROT_SSL3_SERVER\r\n
0xf0000006 | SP_PROT_SSL3_CLIENT\r\n
0xf0000007 | SP_PROT_TLS1_SERVER\r\n
0xf0000008 | SP_PROT_TLS1_CLIENT\r\n
0xf0000009 | SP_PROT_TLS1_1_SERVER\r\n
0xf000000a | SP_PROT_TLS1_1_CLIENT\r\n
0xf000000b | SP_PROT_TLS1_2_SERVER\r\n
0xf000000c | SP_PROT_TLS1_2_CLIENT\r\n
0xf000000d | SP_PROT_UNI_SERVER\r\n
0xf000000e | SP_PROT_UNI_CLIENT\r\n

### 10.0.18362.1

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000021 | SEND\r\n
0x10000022 | RECEIVE\r\n
0x10000023 | L3_CONNECT\r\n
0x10000025 | CLOSE\r\n
0x10000026 | SECURITY\r\n
0x10000027 | CONFIGURATION\r\n
0x10000028 | GLOBAL\r\n
0x10000029 | DROPPED\r\n
0x1000002a | PII_PRESENT\r\n
0x1000002b | PACKET\r\n
0x1000002c | ADDRESS\r\n
0x1000002d | CONTEXT_EVENT\r\n
0x1000002e | STATE_TRANSITION\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | NOOP\r\n
0x3000000b | Queue\r\n
0x3000000c | Cancel\r\n
0x3000000d | Get\r\n
0x3000000e | Set\r\n
0x3000000f | Reallocate\r\n
0x30000010 | Reset\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000006d | WebIOAPI\r\n
0x7000006e | WebIODebug\r\n
0x7000006f | ApiInit\r\n
0x70000070 | ApiTerminate\r\n
0x70000071 | Session Create\r\n
0x70000072 | SessionClose\r\n
0x70000073 | SyncApiWait\r\n
0x700000c8 | RequestCreate\r\n
0x700000c9 | RequestConfiguration\r\n
0x700000ca | RequestClose\r\n
0x70000190 | RequestHeader\r\n
0x70000191 | ProxyResolution\r\n
0x70000193 | Endpoint\r\n
0x70000194 | RequestGenerateHeaders\r\n
0x70000195 | RequestSendEntity\r\n
0x70000196 | RequestEntityTracker\r\n
0x70000197 | RequestEntityCompleteCallback\r\n
0x70000198 | ResponseRecieveEntity\r\n
0x70000199 | ResponseEntityCompleteCallback\r\n
0x7000019a | RequestWaitingForConnection\r\n
0x7000019b | ResponseParser\r\n
0x7000019c | ResponseDirectReceiveEntity\r\n
0x7000019d | RequestSend\r\n
0x7000019e | ResponseReceive\r\n
0x7000019f | ResponseConnectionBufferReceive\r\n
0x700001a0 | RequestCancel\r\n
0x700001a1 | ConnectionSocketConnect\r\n
0x700001a2 | ConnectionSocketCreate\r\n
0x700001a3 | ConnectionSocketClose\r\n
0x700001a4 | ConnectionNameResolution\r\n
0x700001a5 | ConnectionSocketSend\r\n
0x700001a7 | ConnectionSocketReceive\r\n
0x700001a8 | SSLEncryptMessage\r\n
0x700001a9 | SSLInitializeSecurityContext\r\n
0x700001aa | SSLSendEntity\r\n
0x700001ab | SSLCertValidation\r\n
0x700001ac | SSLReceiveEntity\r\n
0x700001ad | SSLDecryptMessage\r\n
0x700001ae | SSLConnectionBufferReceive\r\n
0x700001af | ThreadToken\r\n
0x700001b0 | ResponseReceiveCompleteCallback\r\n
0x700001b1 | ThreadAction\r\n
0x700001b2 | Information\r\n
0x700001b3 | ConnectionNameResolutionRequest\r\n
0x700001b4 | SSLAcquireCredentialsHandle\r\n
0x700001f4 | ProtocolSendData\r\n
0x700001f5 | ProtocolSendDataCallback\r\n
0x700001f6 | ProtocolReceiveData\r\n
0x700001f7 | ProtocolReceiveDataCallback\r\n
0x700001f8 | ProtocolCancelHandle\r\n
0x700001f9 | ProtocolConfiguration\r\n
0x700001fa | CompleteProtocolUpgrade\r\n
0x700001fb | CloseProtocolHandle\r\n
0x70000385 | RequestState\r\n
0xb0000001 | %1: WebInitialize completed successfully (ApiVersion %3) (Flags %4) -> (API Handle = %2).\r\n
0xb0000002 | WebInitialize failed with an error = %5 (ApiVersion %3) (Flags %4)\r\n
0xb0000003 | %1 WebTerminate completed successfully. (Handle %2) (Flags %3)\r\n
0xb0000004 | %1 WebTerminate failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000005 | %3: WebCreateSession completed successfully. (ApiHandle %1[%2]) (Flags: %5) -> (Session Handle: %4)\r\n
0xb0000006 | %1: WebCreateSession failed with an error = %6. (ApiHandle %1[%2]) (Flags: %5)\r\n
0xb0000007 | %1: WebCloseSession called (Handle %2) (Flags %3)\r\n
0xb0000008 | %1: WebCloseSession failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000009 | %2(%1) API called.\r\n
0xb000000a | %2(%1) API returned successfully.\r\n
0xb000000b | %2(%1) API failed with an error = %3.\r\n
0xb000000c | %2(%1) API pending completion.\r\n
0xb000000d | %2(%1) API completed.\r\n
0xb000000e | %2(%1) API completed with an error = %3.\r\n
0xb000000f | %1: Set Request Option %3 (Handle %2) (Error %6) (Length %4) (Value %5)\r\n
0xb0000011 | %1: WebCreateHttpRequest completed successfully. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8) -> (Request Handle %2)\r\n
0xb0000012 | %3: WebCreateHttpRequest failed with error: %9. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8)\r\n
0xb0000013 | %1: WebCloseHttpRequest called (Handle %2) (Flags %3)\r\n
0xb0000014 | %1 WebCloseHttpRequest failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000015 | Synchronous API Event Handle Signall (Event %2) (Error %3) (Information %4)\r\n
0xb0000016 | Synchronous API Event Handle Wait Completed (Handle %1) (Event %2) (Error %3) (Information %4)\r\n
0xb0000017 | %1: WebSetHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000018 | %1: WebSetHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000019 | %1: WebRemoveHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001a | %1: WebRemoveHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3)\r\n
0xb000001b | %1: Indicating informational callback to request. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001c | %1: Informational callback to request complete. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001d | %1: WebCloseSession completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001e | %1: WebCloseHttpRequest completed sucessfully error = %4. (Handle %2) (Flags %3)\r\n
0xb0000064 | %1: Sending Headers: %3\r\n
0xb0000065 | %1: Received Headers: %3\r\n
0xb0000066 | %1: Starting Proxy Resolution\r\n
0xb0000067 | %1: Completed Proxy Resolution\r\n
0xb0000068 | %1: Acquired a connection slot (ConnMgr: %2), (Connection: %3)\r\n
0xb0000069 | %1: Request on Endpoint (Server Endpoint: %2) (Proxy Endpoint: %3) (Connection Manager: %4)\r\n
0xb000006a | %1: Request Message Generated (DataChunk %2[%3])\r\n
0xb000006b | %1: WebSendHttpRequestEntity (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006c | %1: WebSendHttpRequestEntity Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006d | %1: HTTP Queuing Entity for Sending (DataChunks %2) (ChunkLength %3) (IsEntity %4) (All Entity Posted? %5)\r\n
0xb000006e | %1: HTTP Sending Entity (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb000006f | %1: HTTP Send Entity Details (Connection: %2) (DataChunks %3) (Index %4) (Buffer %5 [%6]) Data: %7\r\n
0xb0000070 | %1: HTTP Sending Entity Complete (Error %6) (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb0000071 | %1: Completing WebSendHttpRequest(Entity) (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000072 | %1: Completing WebSendHttpRequest(Entity) Complete (DataChunks %2)\r\n
0xb0000073 | %1: WebHttpReceiveEntityBody (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000074 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000075 | %1: Completing WebHttpReceiveEntityBody (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000076 | %1: Completing WebHttpReceiveEntityBody Complete (DataChunks %2)\r\n
0xb0000077 | %1: HTTP Connection changing Buffer (OldBuffer %2 [%3]) (NewBuffer %5 [%6]) (Carryover %4)\r\n
0xb0000078 | %1: HTTP Connection Buffer Posting Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6])\r\n
0xb0000079 | %1: HTTP Connection Buffer Completing Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6]) (Error %7)  (CompletionInformation %8)\r\n
0xb000007a | %1: HTTP Connection Buffer Receive Details (DataChunks %2) (Length %3) Data: %4\r\n
0xb000007b | %1: HTTP Parser (Connection %2) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007c | %1: HTTP Parser Complete (Connection %2) (Error %9) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007d | %1: HTTP Parser Reset (Buffer %2) (HttpResponseCode %3)\r\n
0xb000007e | %1: HTTP Receive From Parser (DataChunk %2) (ParserChunk %3 [%4]) (Error %5) (Context %6) (Information %7)\r\n
0xb000007f | %1: HTTP Receive (DataChunk %2) (BytesToRecv %3)\r\n
0xb0000080 | %1: HTTP Receive Complete (DataChunk %2) (BytesToRecv %3) (Error %4) (Context %5) (Information %6)\r\n
0xb0000081 | %1: HTTP Receive Entity Details (DataChunk %2) (Index %3) (Length %4) Data %5\r\n
0xb0000082 | %1: WebSendHttpRequest (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000083 | %1: WebSendHttpRequest Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000084 | %1: WebHttpReceiveResponse (Handle: %2) (Flags %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000085 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %6) (Flags: %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000086 | %1: Completing WebHttpReceiveEntityBody (Error %3) (ResponseFlags %2) (CompletionInformation %4)\r\n
0xb0000087 | %1: Completing WebHttpReceiveEntityBody Complete\r\n
0xb0000088 | %1: WebCancelHttpRequest (Handle: %2) (Flags %3)\r\n
0xb0000089 | %1: WebCancelHttpRequest Complete (Error: %4) (Handle: %2) (Flags %3)\r\n
0xb00000c8 | %1: Connecting (Socket %2) (Context %5) (RemaingAddress %6) Address: %4.\r\n
0xb00000c9 | %1: Connection established (Socket %2) (Context %5)\r\n
0xb00000ca | %1: Connect failed with error %7 (Socket %2) (Context %5) (RemaingAddress %6)\r\n
0xb00000cb | Socket %2 created on Endpoint %1.\r\n
0xb00000cc | %1: Socket %2 Closed (Reason = %3, Status = %4).\r\n
0xb00000cd | %1: Name Resolution Request (Name %2) (Timeout %3) (CompletionContext: %4)\r\n
0xb00000ce | %1: Name Resolution Request Completed (FQDN %2) (Canonical %3) (AddressCount: %4) AddressData: %6\r\n
0xb00000cf | %1: Name Resolution Request Failed (Error %2)\r\n
0xb00000d0 | %1: Name Resolution Request queued to %2\r\n
0xb00000d1 | %1: Name Resolution Request is cancelled\r\n
0xb00000d2 | %1: Name Resolution Request Timed-out\r\n
0xb00000d3 | %1: Resolving addresses (Host %2) (Flags: %3)\r\n
0xb00000d4 | %1: Address resolution completed (Error = %4) (Host %2) (Flags: %3).(AddressCount %5)\r\n
0xb00000d5 | %1: Winsock Send Entity Start(DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d6 | %1: Winsock Send Entity Complete (Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d7 | %1: Winsock Recv Entity Start (DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d8 | %1: Winsock Recv Entity Complete(Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00002bc | %1: InitializeSecurityContext - Credential Handle(%2:%3) Context Handle (%4:%5) (Hostname %6) (InputFlags %7) (Buffer %8 [%9/%10])\r\n
0xb00002bf | %1: InitializeSecurityContext returned - (%14) Credential Handle(%2:%3) Context Handle (%4:%5) (OutputFlags %11) (Buffer %8 [%9/%10]) (DataChunk %12 [%13])\r\n
0xb00002c0 | %1: InitializeSecurityContext Details (Pre) - Credential Handle(%2:%3) (Buffer %4 [%5/%6]) Data: %7\r\n
0xb00002c1 | %1: InitializeSecurityContext Details (Post) - Credential Handle(%2:%3) (DataChunk %4 [%5]) Data: %6\r\n
0xb00002c2 | %1: SSL Encryption (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c3 | %1: SSL Encryption Complete (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (InBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c4 | %1: SSL Encryption Failed (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (Flags %9) \r\n
0xb00002c5 | %1: SSL Encryption Details (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9) Data:%10\r\n
0xb00002c6 | %1: SSL Queue Send Entity (SSLIOContext %2) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c7 | %1: SSL Send Entity Complete (SSLIOContext: %2) (Error: %5) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c8 | %1: SSL Cert Validation - (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002c9 | %1: SSL Cert Validation Failure - %7 (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002d0 | %1: SSL Queue Recv Entity Data Chunk (SSLIOContext %2) (DataChunks: %3)\r\n
0xb00002d1 | %1: SSL Filling Up Recv Entity Data Chunk (SSLIOContext: %2) (DataChunks: %3) (PlainData %4[%5]) (Information: %6)\r\n
0xb00002d2 | %1: SSL Decryption - Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d3 | %1: SSL Decryption Complete (SecStatus %9) (Error %10) Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d4 | %1: SSL Receive Buffer Posting Receive (DataChunk %2) (Buffer %3[%4/%5])\r\n
0xb00002d5 | %1: SSL Receive Buffer Receive Complete (DataChunk %2) (Error %7) (Information %6) (Buffer %3[%4/%5])\r\n
0xb00002d6 | %1: SSL Receive Buffer Details: (Buffer %2[%3/%4]) Data: %5\r\n
0xb00002d7 | %1: SSL Receive Buffer Posting Receive (Buffer %2) (NewBuffer: %3)\r\n
0xb00002d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002d9 | %1: SSL AcquireCredentialsHandle returned - (%7) Credential Handle(%5:%6) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002da | %1: SSL AcquireCredentialsHandle failed - (%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb0000384 | %1: WebCompleteProtocolUpgrade completed successfully. (Handle %2) (Request %3[%4]) (Session %5[%6])\r\n
0xb0000385 | %1: WebCompleteProtocolUpgrade failed with error: %7. (Handle %2) (Request %3[%4]) (Session %5[%6])\r\n
0xb0000386 | %1: WebProtocolCancelHandle (Handle: %2)\r\n
0xb0000387 | %1: WebProtocolCancelHandle Complete (Error: %3) (Handle: %2)\r\n
0xb0000388 | %1: WebCloseProtocolHandle called (Handle %2)\r\n
0xb0000389 | %1: WebCloseProtocolHandle completed (Error %4) (Handle %2)\r\n
0xb000038a | %1: Set Protocol Option %3 (Handle %2) (Error %6) (Length %4) (Value %5)\r\n
0xb000038b | %1: WebProtocolSendData (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000038c | %1: WebProtocolSendData Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000038d | %1: Completing WebProtocolSendData (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb000038e | %1: Completing WebProtocolSendData Complete (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb000038f | %1: WebProtocolReceiveData (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000390 | %1: WebProtocolReceiveData Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000391 | %1: Completing WebProtocolReceiveData (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb0000392 | %1: Completing WebProtocolReceiveData Complete (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb0000834 | %1: =====Request Initialize===================\r\n
0xb0000835 | %1: =====Query Endpoints======================\r\n
0xb0000836 | %1: =====Waiting For Available Connection=====\r\n
0xb000083f | %1: =====Request Connect======================\r\n
0xb0000840 | %1: =====Name Resolution======================\r\n
0xb0000841 | %1: =====TCP Connect==========================\r\n
0xb0000842 | %1: =====SSL Negotiation======================\r\n
0xb0000848 | %1: =====Generate Headers=====================\r\n
0xb0000849 | %1: =====Send Headers=========================\r\n
0xb000084a | %1: =====Send Entity==========================\r\n
0xb000084b | %1: =====Send Complete========================\r\n
0xb0000852 | %1: =====Receive Headers======================\r\n
0xb0000853 | %1: =====Receive Entity=======================\r\n
0xb0000854 | %1: =====Receive Complete=====================\r\n
0xb000085c | %1: =====Request Restart======================\r\n
0xb000085d | %1: =====Request Done=========================\r\n
0xb000ea58 | Restore Thread Token %1 (Error: %2)\r\n
0xb000ea59 | Set Thread Token %1 (OldToken %2) (Error: %3)\r\n
0xb000ea5a | Get Thread Token %1 (Error: %3) (SID: %2)\r\n
0xb000ea5b | Canceling %2 Thread Action (Context: %1)\r\n
0xb000ea5c | Queue %2 Thread Action (Context: %1)\r\n
0xb000ea5d | Stopping %2 Thread Action (Context: %1)\r\n
0xb000ea5e | Starting %2 Thread Action (Context: %1)\r\n
0xb000ea5f | %2\r\n
0xb00102d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xb00102d9 | %1: SSL AcquireCredentialsHandle returned - (%8) Credential Handle(%6:%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xb00102da | %1: SSL AcquireCredentialsHandle failed - (%8) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xd0000001 | STATUS_SUCCESS\r\n
0xd0000002 | SEC_E_INSUFFICIENT_MEMORY\r\n
0xd0000003 | SEC_E_INVALID_HANDLE\r\n
0xd0000004 | SEC_E_UNSUPPORTED_FUNCTION\r\n
0xd0000005 | SEC_E_TARGET_UNKNOWN\r\n
0xd0000006 | SEC_E_INTERNAL_ERROR\r\n
0xd0000007 | SEC_E_SECPKG_NOT_FOUND\r\n
0xd0000008 | SEC_E_NOT_OWNER\r\n
0xd0000009 | SEC_E_CANNOT_INSTALL\r\n
0xd000000a | SEC_E_INVALID_TOKEN\r\n
0xd000000b | SEC_E_CANNOT_PACK\r\n
0xd000000c | SEC_E_QOP_NOT_SUPPORTED\r\n
0xd000000d | SEC_E_NO_IMPERSONATION\r\n
0xd000000e | SEC_E_LOGON_DENIED\r\n
0xd000000f | SEC_E_UNKNOWN_CREDENTIALS\r\n
0xd0000010 | SEC_E_NO_CREDENTIALS\r\n
0xd0000011 | SEC_E_MESSAGE_ALTERED\r\n
0xd0000012 | SEC_E_OUT_OF_SEQUENCE\r\n
0xd0000013 | SEC_E_NO_AUTHENTICATING_AUTHORITY\r\n
0xd0000014 | SEC_I_CONTINUE_NEEDED\r\n
0xd0000015 | SEC_I_COMPLETE_NEEDED\r\n
0xd0000016 | SEC_I_COMPLETE_AND_CONTINUE\r\n
0xd0000017 | SEC_I_LOCAL_LOGON\r\n
0xd0000018 | SEC_E_BAD_PKGID\r\n
0xd0000019 | SEC_E_CONTEXT_EXPIRED\r\n
0xd000001a | SEC_E_INCOMPLETE_MESSAGE\r\n
0xd000001b | CERT_E_EXPIRED\r\n
0xd000001c | CERT_E_VALIDITYPERIODNESTING\r\n
0xd000001d | CERT_E_UNTRUSTEDROOT\r\n
0xd000001e | CERT_E_CHAINING\r\n
0xd000001f | CERT_E_CN_NO_MATCH\r\n
0xd0000020 | CERT_E_INVALID_NAME\r\n
0xd0000021 | CERT_E_WRONG_USAGE\r\n
0xd0000022 | CRYPT_E_REVOKED\r\n
0xd0000023 | TRUST_E_EXPLICIT_DISTRUST\r\n
0xd0000024 | CRYPT_E_NO_REVOCATION_CHECK\r\n
0xd0000025 | CRYPT_E_REVOCATION_OFFLINE\r\n
0xd0000026 | CERT_E_ROLE\r\n
0xd0000027 | CERT_E_PATHLENCONST\r\n
0xd0000028 | CERT_E_CRITICAL\r\n
0xd0000029 | CERT_E_PURPOSE\r\n
0xd000002a | CERT_E_ISSUERCHAINING\r\n
0xd000002b | CERT_E_MALFORMED\r\n
0xd000002c | TRUST_E_CERT_SIGNATURE\r\n
0xd000002d | CERT_E_INVALID_POLICY\r\n
0xd000002e | TRUST_E_BASIC_CONSTRAINTS\r\n
0xd000002f | Local Graceful\r\n
0xd0000030 | Remote Graceful\r\n
0xd0000031 | Local Reset\r\n
0xd0000032 | Remote Reset\r\n
0xd0000033 | Connect Timeout\r\n
0xd0000034 | Send Timeout\r\n
0xd0000035 | Receive Timeout\r\n
0xd0000036 | Scavenged\r\n
0xd0000037 | No Reason\r\n
0xd0000038 | Cleanup after hitting an error condition\r\n
0xd0000039 | Timer\r\n
0xd000003a | WorkItem\r\n
0xd000003b | Overlapped IO\r\n
0xd000003c | No Error\r\n
0xd000003d | Unable to Get Cert\r\n
0xd000003e | NULL cert context\r\n
0xd000003f | Unable to Get Cert Chain\r\n
0xd0000040 | Unable to Process URL to Hostname\r\n
0xd0000041 | Cert Validation Failure\r\n
0xd0000042 | Unable to get Stream Sizes\r\n
0xd0000043 | Unable to get Endpoint Bindings\r\n
0xd0000044 | Unable to get secure connection information\r\n
0xd0000045 | AuthSchemeState\r\n
0xd0000046 | DisableAuthentication\r\n
0xd0000047 | ClientCertificate\r\n
0xd0000048 | ClientCertificateIssuerList\r\n
0xd0000049 | ChannelBindingToken\r\n
0xd000004a | IgnoredServerCertErrors\r\n
0xd000004b | SecureProtocols\r\n
0xd000004c | ProxyAuthSchemes\r\n
0xd000004d | ProxyAuthState\r\n
0xd000004e | ProxyAutoLogonState\r\n
0xd000004f | ProxyConfig\r\n
0xd0000050 | ProxyConnectHeaders\r\n
0xd0000051 | ProxyCreds\r\n
0xd0000052 | ProxySpnUsage\r\n
0xd0000053 | RedirectionLimit\r\n
0xd0000054 | SecureProtocolInformation\r\n
0xd0000055 | ServerAuthSchemes\r\n
0xd0000056 | ServerAuthState\r\n
0xd0000057 | ServerAutoLogonState\r\n
0xd0000058 | ServerCert\r\n
0xd0000059 | ServerCreds\r\n
0xd000005a | ServerSpnUsage\r\n
0xd000005b | SocketAddress\r\n
0xd000005c | ThirdPartyCookies\r\n
0xd000005d | PathCodePage\r\n
0xd000005e | ExtraInfoCodePage\r\n
0xd000005f | ServerCertErrors\r\n
0xd0000060 | CookiesEnabled\r\n
0xd0000061 | ResponseHeadersSizeLimit\r\n
0xd0000062 | ServerSpnUsed\r\n
0xd0000063 | ProxySpnUsed\r\n
0xd0000064 | ConnectTimeout\r\n
0xd0000065 | ResolveTimeout\r\n
0xd0000066 | SendTimeout\r\n
0xd0000067 | ReceiveTimeout\r\n
0xd0000068 | ConnectRetryCount\r\n
0xd0000069 | UnsafeHeaderParsing\r\n
0xd000006a | RevertToSelfClientCertificate\r\n
0xd000006b | NetworkInterfaceAffinity\r\n
0xd000006c | TcpAutoTuningRestricted\r\n
0xd000006d | DnsIdnTransformDisabled\r\n
0xd000006e | PeerDistExtension\r\n
0xd000006f | MaximumConnectCount\r\n
0xd0000070 | GlobalKeepAlivePoolState\r\n
0xd0000071 | ConnectionState\r\n
0xd0000072 | ExceededResponseHeaderSizeLimit\r\n
0xd0000073 | DnsInterfaceAffinity\r\n
0xd0000074 | ConnectionIdleTimeout\r\n
0xf0000001 | SP_PROT_PCT1_SERVER\r\n
0xf0000002 | SP_PROT_PCT1_CLIENT\r\n
0xf0000003 | SP_PROT_SSL2_SERVER\r\n
0xf0000004 | SP_PROT_SSL2_CLIENT\r\n
0xf0000005 | SP_PROT_SSL3_SERVER\r\n
0xf0000006 | SP_PROT_SSL3_CLIENT\r\n
0xf0000007 | SP_PROT_TLS1_SERVER\r\n
0xf0000008 | SP_PROT_TLS1_CLIENT\r\n
0xf0000009 | SP_PROT_TLS1_1_SERVER\r\n
0xf000000a | SP_PROT_TLS1_1_CLIENT\r\n
0xf000000b | SP_PROT_TLS1_2_SERVER\r\n
0xf000000c | SP_PROT_TLS1_2_CLIENT\r\n
0xf000000d | SP_PROT_TLS1_3_SERVER\r\n
0xf000000e | SP_PROT_TLS1_3_CLIENT\r\n
0xf000000f | SP_PROT_UNI_SERVER\r\n
0xf0000010 | SP_PROT_UNI_CLIENT\r\n

### 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000001 | API\r\n
0x10000021 | SEND\r\n
0x10000022 | RECEIVE\r\n
0x10000023 | L3_CONNECT\r\n
0x10000025 | CLOSE\r\n
0x10000026 | SECURITY\r\n
0x10000027 | CONFIGURATION\r\n
0x10000028 | GLOBAL\r\n
0x10000029 | DROPPED\r\n
0x1000002a | PII_PRESENT\r\n
0x1000002b | PACKET\r\n
0x1000002c | ADDRESS\r\n
0x1000002d | CONTEXT_EVENT\r\n
0x1000002e | STATE_TRANSITION\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | NOOP\r\n
0x3000000b | Queue\r\n
0x3000000c | Cancel\r\n
0x3000000d | Get\r\n
0x3000000e | Set\r\n
0x3000000f | Reallocate\r\n
0x30000010 | Reset\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000006d | WebIOAPI\r\n
0x7000006e | WebIODebug\r\n
0x7000006f | ApiInit\r\n
0x70000070 | ApiTerminate\r\n
0x70000071 | Session Create\r\n
0x70000072 | SessionClose\r\n
0x70000073 | SyncApiWait\r\n
0x700000c8 | RequestCreate\r\n
0x700000c9 | RequestConfiguration\r\n
0x700000ca | RequestClose\r\n
0x70000190 | RequestHeader\r\n
0x70000191 | ProxyResolution\r\n
0x70000193 | Endpoint\r\n
0x70000194 | RequestGenerateHeaders\r\n
0x70000195 | RequestSendEntity\r\n
0x70000196 | RequestEntityTracker\r\n
0x70000197 | RequestEntityCompleteCallback\r\n
0x70000198 | ResponseRecieveEntity\r\n
0x70000199 | ResponseEntityCompleteCallback\r\n
0x7000019a | RequestWaitingForConnection\r\n
0x7000019b | ResponseParser\r\n
0x7000019c | ResponseDirectReceiveEntity\r\n
0x7000019d | RequestSend\r\n
0x7000019e | ResponseReceive\r\n
0x7000019f | ResponseConnectionBufferReceive\r\n
0x700001a0 | RequestCancel\r\n
0x700001a1 | ConnectionSocketConnect\r\n
0x700001a2 | ConnectionSocketCreate\r\n
0x700001a3 | ConnectionSocketClose\r\n
0x700001a4 | ConnectionNameResolution\r\n
0x700001a5 | ConnectionSocketSend\r\n
0x700001a7 | ConnectionSocketReceive\r\n
0x700001a8 | SSLEncryptMessage\r\n
0x700001a9 | SSLInitializeSecurityContext\r\n
0x700001aa | SSLSendEntity\r\n
0x700001ab | SSLCertValidation\r\n
0x700001ac | SSLReceiveEntity\r\n
0x700001ad | SSLDecryptMessage\r\n
0x700001ae | SSLConnectionBufferReceive\r\n
0x700001af | ThreadToken\r\n
0x700001b0 | ResponseReceiveCompleteCallback\r\n
0x700001b1 | ThreadAction\r\n
0x700001b2 | Information\r\n
0x700001b3 | ConnectionNameResolutionRequest\r\n
0x700001b4 | SSLAcquireCredentialsHandle\r\n
0x700001f4 | ProtocolSendData\r\n
0x700001f5 | ProtocolSendDataCallback\r\n
0x700001f6 | ProtocolReceiveData\r\n
0x700001f7 | ProtocolReceiveDataCallback\r\n
0x700001f8 | ProtocolCancelHandle\r\n
0x700001f9 | ProtocolConfiguration\r\n
0x700001fa | CompleteProtocolUpgrade\r\n
0x700001fb | CloseProtocolHandle\r\n
0x70000385 | RequestState\r\n
0xb0000001 | %1: WebInitialize completed successfully (ApiVersion %3) (Flags %4) -> (API Handle = %2).\r\n
0xb0000002 | WebInitialize failed with an error = %5 (ApiVersion %3) (Flags %4)\r\n
0xb0000003 | %1 WebTerminate completed successfully. (Handle %2) (Flags %3)\r\n
0xb0000004 | %1 WebTerminate failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000005 | %3: WebCreateSession completed successfully. (ApiHandle %1[%2]) (Flags: %5) -> (Session Handle: %4)\r\n
0xb0000006 | %1: WebCreateSession failed with an error = %6. (ApiHandle %1[%2]) (Flags: %5)\r\n
0xb0000007 | %1: WebCloseSession called (Handle %2) (Flags %3)\r\n
0xb0000008 | %1: WebCloseSession failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000009 | %2(%1) API called.\r\n
0xb000000a | %2(%1) API returned successfully.\r\n
0xb000000b | %2(%1) API failed with an error = %3.\r\n
0xb000000c | %2(%1) API pending completion.\r\n
0xb000000d | %2(%1) API completed.\r\n
0xb000000e | %2(%1) API completed with an error = %3.\r\n
0xb000000f | %1: Set Request Option %3 (Handle %2) (Error %6) (Length %4) (Value %5)\r\n
0xb0000011 | %1: WebCreateHttpRequest completed successfully. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8) -> (Request Handle %2)\r\n
0xb0000012 | %3: WebCreateHttpRequest failed with error: %9. (Session %3[%4]) (Method %5) (URI %6) (Version %7.%8)\r\n
0xb0000013 | %1: WebCloseHttpRequest called (Handle %2) (Flags %3)\r\n
0xb0000014 | %1 WebCloseHttpRequest failed with an error = %4. (Handle %2) (Flags %3)\r\n
0xb0000015 | Synchronous API Event Handle Signall (Event %2) (Error %3) (Information %4)\r\n
0xb0000016 | Synchronous API Event Handle Wait Completed (Handle %1) (Event %2) (Error %3) (Information %4)\r\n
0xb0000017 | %1: WebSetHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000018 | %1: WebSetHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3) (InformationRoutine %4) (InformationContext %5)\r\n
0xb0000019 | %1: WebRemoveHttpRequestInformationRoutine completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001a | %1: WebRemoveHttpRequestInformationRoutine failed with an error = %6. (Handle %2) (Flags %3)\r\n
0xb000001b | %1: Indicating informational callback to request. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001c | %1: Informational callback to request complete. (PendingCount %2) (InformationRoutine %3) (InformationContext %4) (Type %5) (Information %6) (InformationLength %7\r\n
0xb000001d | %1: WebCloseSession completed successfully. (Handle %2) (Flags %3)\r\n
0xb000001e | %1: WebCloseHttpRequest completed sucessfully error = %4. (Handle %2) (Flags %3)\r\n
0xb0000064 | %1: Sending Headers: %3\r\n
0xb0000065 | %1: Received Headers: %3\r\n
0xb0000066 | %1: Starting Proxy Resolution\r\n
0xb0000067 | %1: Completed Proxy Resolution\r\n
0xb0000068 | %1: Acquired a connection slot (ConnMgr: %2), (Connection: %3)\r\n
0xb0000069 | %1: Request on Endpoint (Server Endpoint: %2) (Proxy Endpoint: %3) (Connection Manager: %4)\r\n
0xb000006a | %1: Request Message Generated (DataChunk %2[%3])\r\n
0xb000006b | %1: WebSendHttpRequestEntity (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006c | %1: WebSendHttpRequestEntity Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000006d | %1: HTTP Queuing Entity for Sending (DataChunks %2) (ChunkLength %3) (IsEntity %4) (All Entity Posted? %5)\r\n
0xb000006e | %1: HTTP Sending Entity (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb000006f | %1: HTTP Send Entity Details (Connection: %2) (DataChunks %3) (Index %4) (Buffer %5 [%6]) Data: %7\r\n
0xb0000070 | %1: HTTP Sending Entity Complete (Error %6) (Connection: %2) (DataChunks %3) (PendingSendCount %4) (LastSend? %5)\r\n
0xb0000071 | %1: Completing WebSendHttpRequest(Entity) (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000072 | %1: Completing WebSendHttpRequest(Entity) Complete (DataChunks %2)\r\n
0xb0000073 | %1: WebHttpReceiveEntityBody (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000074 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000075 | %1: Completing WebHttpReceiveEntityBody (DataChunks %2) (Error %3) (CompletionContext %4) (CompletionInformation %5)\r\n
0xb0000076 | %1: Completing WebHttpReceiveEntityBody Complete (DataChunks %2)\r\n
0xb0000077 | %1: HTTP Connection changing Buffer (OldBuffer %2 [%3]) (NewBuffer %5 [%6]) (Carryover %4)\r\n
0xb0000078 | %1: HTTP Connection Buffer Posting Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6])\r\n
0xb0000079 | %1: HTTP Connection Buffer Completing Receive (DataChunks %2) (Buffer: %3 [%4/%5/%6]) (Error %7)  (CompletionInformation %8)\r\n
0xb000007a | %1: HTTP Connection Buffer Receive Details (DataChunks %2) (Length %3) Data: %4\r\n
0xb000007b | %1: HTTP Parser (Connection %2) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007c | %1: HTTP Parser Complete (Connection %2) (Error %9) (Buffer: %3 [%4/%5/%6]) (ParserChunk %7 [%8])\r\n
0xb000007d | %1: HTTP Parser Reset (Buffer %2) (HttpResponseCode %3)\r\n
0xb000007e | %1: HTTP Receive From Parser (DataChunk %2) (ParserChunk %3 [%4]) (Error %5) (Context %6) (Information %7)\r\n
0xb000007f | %1: HTTP Receive (DataChunk %2) (BytesToRecv %3)\r\n
0xb0000080 | %1: HTTP Receive Complete (DataChunk %2) (BytesToRecv %3) (Error %4) (Context %5) (Information %6)\r\n
0xb0000081 | %1: HTTP Receive Entity Details (DataChunk %2) (Index %3) (Length %4) Data %5\r\n
0xb0000082 | %1: WebSendHttpRequest (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000083 | %1: WebSendHttpRequest Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000084 | %1: WebHttpReceiveResponse (Handle: %2) (Flags %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000085 | %1: WebHttpReceiveEntityBody Inline Completion (Handle: %2) (Error: %6) (Flags: %3) (ResponseFlags %4) CompletionContext (%5)\r\n
0xb0000086 | %1: Completing WebHttpReceiveEntityBody (Error %3) (ResponseFlags %2) (CompletionInformation %4)\r\n
0xb0000087 | %1: Completing WebHttpReceiveEntityBody Complete\r\n
0xb0000088 | %1: WebCancelHttpRequest (Handle: %2) (Flags %3)\r\n
0xb0000089 | %1: WebCancelHttpRequest Complete (Error: %4) (Handle: %2) (Flags %3)\r\n
0xb00000c8 | %1: Connecting (Socket %2) (Context %5) (RemaingAddress %6) Address: %4.\r\n
0xb00000c9 | %1: Connection established (Socket %2) (Context %5)\r\n
0xb00000ca | %1: Connect failed with error %7 (Socket %2) (Context %5) (RemaingAddress %6)\r\n
0xb00000cb | Socket %2 created on Endpoint %1.\r\n
0xb00000cc | %1: Socket %2 Closed (Reason = %3, Status = %4).\r\n
0xb00000cd | %1: Name Resolution Request (Name %2) (Timeout %3) (CompletionContext: %4)\r\n
0xb00000ce | %1: Name Resolution Request Completed (FQDN %2) (Canonical %3) (AddressCount: %4) AddressData: %6\r\n
0xb00000cf | %1: Name Resolution Request Failed (Error %2)\r\n
0xb00000d0 | %1: Name Resolution Request queued to %2\r\n
0xb00000d1 | %1: Name Resolution Request is cancelled\r\n
0xb00000d2 | %1: Name Resolution Request Timed-out\r\n
0xb00000d3 | %1: Resolving addresses (Host %2) (Flags: %3)\r\n
0xb00000d4 | %1: Address resolution completed (Error = %4) (Host %2) (Flags: %3).(AddressCount %5)\r\n
0xb00000d5 | %1: Winsock Send Entity Start(DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d6 | %1: Winsock Send Entity Complete (Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d7 | %1: Winsock Recv Entity Start (DataChunks %2) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00000d8 | %1: Winsock Recv Entity Complete(Error %6) (Information %7) (Socket %3) (Buffers %4) (Context %5)\r\n
0xb00002bc | %1: InitializeSecurityContext - Credential Handle(%2:%3) Context Handle (%4:%5) (Hostname %6) (InputFlags %7) (Buffer %8 [%9/%10])\r\n
0xb00002bf | %1: InitializeSecurityContext returned - (%14) Credential Handle(%2:%3) Context Handle (%4:%5) (OutputFlags %11) (Buffer %8 [%9/%10]) (DataChunk %12 [%13])\r\n
0xb00002c0 | %1: InitializeSecurityContext Details (Pre) - Credential Handle(%2:%3) (Buffer %4 [%5/%6]) Data: %7\r\n
0xb00002c1 | %1: InitializeSecurityContext Details (Post) - Credential Handle(%2:%3) (DataChunk %4 [%5]) Data: %6\r\n
0xb00002c2 | %1: SSL Encryption (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c3 | %1: SSL Encryption Complete (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (InBuffer: %7[%8]) (Flags %9)\r\n
0xb00002c4 | %1: SSL Encryption Failed (SSLIOContext %2) (ErrorCode: %10) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (Flags %9) \r\n
0xb00002c5 | %1: SSL Encryption Details (SSLIOContext %2) Context Handle(%3:%4) (DataChunks: %5) (Index: %6) (OutBuffer: %7[%8]) (Flags %9) Data:%10\r\n
0xb00002c6 | %1: SSL Queue Send Entity (SSLIOContext %2) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c7 | %1: SSL Send Entity Complete (SSLIOContext: %2) (Error: %5) (DataChunks: %3) (RequestDisconnect? %4)\r\n
0xb00002c8 | %1: SSL Cert Validation - (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002c9 | %1: SSL Cert Validation Failure - %7 (Error: %6) Context Handle(%2:%3) (IgnoredServerCertErrors %4) (CertErrors %5)\r\n
0xb00002d0 | %1: SSL Queue Recv Entity Data Chunk (SSLIOContext %2) (DataChunks: %3)\r\n
0xb00002d1 | %1: SSL Filling Up Recv Entity Data Chunk (SSLIOContext: %2) (DataChunks: %3) (PlainData %4[%5]) (Information: %6)\r\n
0xb00002d2 | %1: SSL Decryption - Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d3 | %1: SSL Decryption Complete (SecStatus %9) (Error %10) Context Handle(%2:%3) (Buffer %4[%5/%6]) (PlainData %7[%8])\r\n
0xb00002d4 | %1: SSL Receive Buffer Posting Receive (DataChunk %2) (Buffer %3[%4/%5])\r\n
0xb00002d5 | %1: SSL Receive Buffer Receive Complete (DataChunk %2) (Error %7) (Information %6) (Buffer %3[%4/%5])\r\n
0xb00002d6 | %1: SSL Receive Buffer Details: (Buffer %2[%3/%4]) Data: %5\r\n
0xb00002d7 | %1: SSL Receive Buffer Posting Receive (Buffer %2) (NewBuffer: %3)\r\n
0xb00002d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002d9 | %1: SSL AcquireCredentialsHandle returned - (%7) Credential Handle(%5:%6) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb00002da | %1: SSL AcquireCredentialsHandle failed - (%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4)\r\n
0xb0000384 | %1: WebCompleteProtocolUpgrade completed successfully. (Handle %2) (Request %3[%4]) (Session %5[%6])\r\n
0xb0000385 | %1: WebCompleteProtocolUpgrade failed with error: %7. (Handle %2) (Request %3[%4]) (Session %5[%6])\r\n
0xb0000386 | %1: WebProtocolCancelHandle (Handle: %2)\r\n
0xb0000387 | %1: WebProtocolCancelHandle Complete (Error: %3) (Handle: %2)\r\n
0xb0000388 | %1: WebCloseProtocolHandle called (Handle %2)\r\n
0xb0000389 | %1: WebCloseProtocolHandle completed (Error %4) (Handle %2)\r\n
0xb000038a | %1: Set Protocol Option %3 (Handle %2) (Error %6) (Length %4) (Value %5)\r\n
0xb000038b | %1: WebProtocolSendData (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000038c | %1: WebProtocolSendData Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb000038d | %1: Completing WebProtocolSendData (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb000038e | %1: Completing WebProtocolSendData Complete (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb000038f | %1: WebProtocolReceiveData (Handle: %2) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000390 | %1: WebProtocolReceiveData Inline Completion (Handle: %2) (Error: %7) (Flags: %3) (DataChunks %4 [%5]) CompletionContext (%6)\r\n
0xb0000391 | %1: Completing WebProtocolReceiveData (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb0000392 | %1: Completing WebProtocolReceiveData Complete (Handle: %2) (Error: %3) CompletionContext (%4)\r\n
0xb0000834 | %1: =====Request Initialize===================\r\n
0xb0000835 | %1: =====Query Endpoints======================\r\n
0xb0000836 | %1: =====Waiting For Available Connection=====\r\n
0xb000083f | %1: =====Request Connect======================\r\n
0xb0000840 | %1: =====Name Resolution======================\r\n
0xb0000841 | %1: =====TCP Connect==========================\r\n
0xb0000842 | %1: =====SSL Negotiation======================\r\n
0xb0000848 | %1: =====Generate Headers=====================\r\n
0xb0000849 | %1: =====Send Headers=========================\r\n
0xb000084a | %1: =====Send Entity==========================\r\n
0xb000084b | %1: =====Send Complete========================\r\n
0xb0000852 | %1: =====Receive Headers======================\r\n
0xb0000853 | %1: =====Receive Entity=======================\r\n
0xb0000854 | %1: =====Receive Complete=====================\r\n
0xb000085c | %1: =====Request Restart======================\r\n
0xb000085d | %1: =====Request Done=========================\r\n
0xb000ea58 | Restore Thread Token %1 (Error: %2)\r\n
0xb000ea59 | Set Thread Token %1 (OldToken %2) (Error: %3)\r\n
0xb000ea5a | Get Thread Token %1 (Error: %3) (SID: %2)\r\n
0xb000ea5b | Canceling %2 Thread Action (Context: %1)\r\n
0xb000ea5c | Queue %2 Thread Action (Context: %1)\r\n
0xb000ea5d | Stopping %2 Thread Action (Context: %1)\r\n
0xb000ea5e | Starting %2 Thread Action (Context: %1)\r\n
0xb000ea5f | %2\r\n
0xb00102d8 | %1: SSL AcquireCredentialsHandle - (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xb00102d9 | %1: SSL AcquireCredentialsHandle returned - (%8) Credential Handle(%6:%7) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xb00102da | %1: SSL AcquireCredentialsHandle failed - (%8) (EnabledProtocols %2) (ClientCert %3) (EnableRevertToSelfClientCertificate %4) (CipherConfig %5)\r\n
0xd0000001 | STATUS_SUCCESS\r\n
0xd0000002 | SEC_E_INSUFFICIENT_MEMORY\r\n
0xd0000003 | SEC_E_INVALID_HANDLE\r\n
0xd0000004 | SEC_E_UNSUPPORTED_FUNCTION\r\n
0xd0000005 | SEC_E_TARGET_UNKNOWN\r\n
0xd0000006 | SEC_E_INTERNAL_ERROR\r\n
0xd0000007 | SEC_E_SECPKG_NOT_FOUND\r\n
0xd0000008 | SEC_E_NOT_OWNER\r\n
0xd0000009 | SEC_E_CANNOT_INSTALL\r\n
0xd000000a | SEC_E_INVALID_TOKEN\r\n
0xd000000b | SEC_E_CANNOT_PACK\r\n
0xd000000c | SEC_E_QOP_NOT_SUPPORTED\r\n
0xd000000d | SEC_E_NO_IMPERSONATION\r\n
0xd000000e | SEC_E_LOGON_DENIED\r\n
0xd000000f | SEC_E_UNKNOWN_CREDENTIALS\r\n
0xd0000010 | SEC_E_NO_CREDENTIALS\r\n
0xd0000011 | SEC_E_MESSAGE_ALTERED\r\n
0xd0000012 | SEC_E_OUT_OF_SEQUENCE\r\n
0xd0000013 | SEC_E_NO_AUTHENTICATING_AUTHORITY\r\n
0xd0000014 | SEC_I_CONTINUE_NEEDED\r\n
0xd0000015 | SEC_I_COMPLETE_NEEDED\r\n
0xd0000016 | SEC_I_COMPLETE_AND_CONTINUE\r\n
0xd0000017 | SEC_I_LOCAL_LOGON\r\n
0xd0000018 | SEC_E_BAD_PKGID\r\n
0xd0000019 | SEC_E_CONTEXT_EXPIRED\r\n
0xd000001a | SEC_E_INCOMPLETE_MESSAGE\r\n
0xd000001b | CERT_E_EXPIRED\r\n
0xd000001c | CERT_E_VALIDITYPERIODNESTING\r\n
0xd000001d | CERT_E_UNTRUSTEDROOT\r\n
0xd000001e | CERT_E_CHAINING\r\n
0xd000001f | CERT_E_CN_NO_MATCH\r\n
0xd0000020 | CERT_E_INVALID_NAME\r\n
0xd0000021 | CERT_E_WRONG_USAGE\r\n
0xd0000022 | CRYPT_E_REVOKED\r\n
0xd0000023 | TRUST_E_EXPLICIT_DISTRUST\r\n
0xd0000024 | CRYPT_E_NO_REVOCATION_CHECK\r\n
0xd0000025 | CRYPT_E_REVOCATION_OFFLINE\r\n
0xd0000026 | CERT_E_ROLE\r\n
0xd0000027 | CERT_E_PATHLENCONST\r\n
0xd0000028 | CERT_E_CRITICAL\r\n
0xd0000029 | CERT_E_PURPOSE\r\n
0xd000002a | CERT_E_ISSUERCHAINING\r\n
0xd000002b | CERT_E_MALFORMED\r\n
0xd000002c | TRUST_E_CERT_SIGNATURE\r\n
0xd000002d | CERT_E_INVALID_POLICY\r\n
0xd000002e | TRUST_E_BASIC_CONSTRAINTS\r\n
0xd000002f | Local Graceful\r\n
0xd0000030 | Remote Graceful\r\n
0xd0000031 | Local Reset\r\n
0xd0000032 | Remote Reset\r\n
0xd0000033 | Connect Timeout\r\n
0xd0000034 | Send Timeout\r\n
0xd0000035 | Receive Timeout\r\n
0xd0000036 | Scavenged\r\n
0xd0000037 | No Reason\r\n
0xd0000038 | Cleanup after hitting an error condition\r\n
0xd0000039 | Timer\r\n
0xd000003a | WorkItem\r\n
0xd000003b | Overlapped IO\r\n
0xd000003c | No Error\r\n
0xd000003d | Unable to Get Cert\r\n
0xd000003e | NULL cert context\r\n
0xd000003f | Unable to Get Cert Chain\r\n
0xd0000040 | Unable to Process URL to Hostname\r\n
0xd0000041 | Cert Validation Failure\r\n
0xd0000042 | Unable to get Stream Sizes\r\n
0xd0000043 | Unable to get Endpoint Bindings\r\n
0xd0000044 | Unable to get secure connection information\r\n
0xd0000045 | Unable to get secure cipher information\r\n
0xd0000046 | AuthSchemeState\r\n
0xd0000047 | DisableAuthentication\r\n
0xd0000048 | ClientCertificate\r\n
0xd0000049 | ClientCertificateIssuerList\r\n
0xd000004a | ChannelBindingToken\r\n
0xd000004b | IgnoredServerCertErrors\r\n
0xd000004c | SecureProtocols\r\n
0xd000004d | ProxyAuthSchemes\r\n
0xd000004e | ProxyAuthState\r\n
0xd000004f | ProxyAutoLogonState\r\n
0xd0000050 | ProxyConfig\r\n
0xd0000051 | ProxyConnectHeaders\r\n
0xd0000052 | ProxyCreds\r\n
0xd0000053 | ProxySpnUsage\r\n
0xd0000054 | RedirectionLimit\r\n
0xd0000055 | SecureProtocolInformation\r\n
0xd0000056 | ServerAuthSchemes\r\n
0xd0000057 | ServerAuthState\r\n
0xd0000058 | ServerAutoLogonState\r\n
0xd0000059 | ServerCert\r\n
0xd000005a | ServerCreds\r\n
0xd000005b | ServerSpnUsage\r\n
0xd000005c | SocketAddress\r\n
0xd000005d | ThirdPartyCookies\r\n
0xd000005e | PathCodePage\r\n
0xd000005f | ExtraInfoCodePage\r\n
0xd0000060 | ServerCertErrors\r\n
0xd0000061 | CookiesEnabled\r\n
0xd0000062 | ResponseHeadersSizeLimit\r\n
0xd0000063 | ServerSpnUsed\r\n
0xd0000064 | ProxySpnUsed\r\n
0xd0000065 | ConnectTimeout\r\n
0xd0000066 | ResolveTimeout\r\n
0xd0000067 | SendTimeout\r\n
0xd0000068 | ReceiveTimeout\r\n
0xd0000069 | ConnectRetryCount\r\n
0xd000006a | UnsafeHeaderParsing\r\n
0xd000006b | RevertToSelfClientCertificate\r\n
0xd000006c | NetworkInterfaceAffinity\r\n
0xd000006d | TcpAutoTuningRestricted\r\n
0xd000006e | DnsIdnTransformDisabled\r\n
0xd000006f | PeerDistExtension\r\n
0xd0000070 | MaximumConnectCount\r\n
0xd0000071 | GlobalKeepAlivePoolState\r\n
0xd0000072 | ConnectionState\r\n
0xd0000073 | ExceededResponseHeaderSizeLimit\r\n
0xd0000074 | DnsInterfaceAffinity\r\n
0xd0000075 | ConnectionIdleTimeout\r\n
0xf0000001 | SP_PROT_PCT1_SERVER\r\n
0xf0000002 | SP_PROT_PCT1_CLIENT\r\n
0xf0000003 | SP_PROT_SSL2_SERVER\r\n
0xf0000004 | SP_PROT_SSL2_CLIENT\r\n
0xf0000005 | SP_PROT_SSL3_SERVER\r\n
0xf0000006 | SP_PROT_SSL3_CLIENT\r\n
0xf0000007 | SP_PROT_TLS1_SERVER\r\n
0xf0000008 | SP_PROT_TLS1_CLIENT\r\n
0xf0000009 | SP_PROT_TLS1_1_SERVER\r\n
0xf000000a | SP_PROT_TLS1_1_CLIENT\r\n
0xf000000b | SP_PROT_TLS1_2_SERVER\r\n
0xf000000c | SP_PROT_TLS1_2_CLIENT\r\n
0xf000000d | SP_PROT_TLS1_3_SERVER\r\n
0xf000000e | SP_PROT_TLS1_3_CLIENT\r\n
0xf000000f | SP_PROT_UNI_SERVER\r\n
0xf0000010 | SP_PROT_UNI_CLIENT\r\n
