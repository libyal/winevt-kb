## http.sys

Path: %SystemRoot%\system32\drivers\http.sys

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occuring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling ssl interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x300b0000 | RecvReq\r\n
0x300c0000 | Parse\r\n
0x300d0000 | Deliver\r\n
0x300e0000 | RecvResp\r\n
0x300f0000 | RecvRespLast\r\n
0x30100000 | RecvBody\r\n
0x30110000 | RecvBodyLast\r\n
0x30120000 | FastRespLast\r\n
0x30130000 | FastResp\r\n
0x30140000 | CachedAndSend\r\n
0x30150000 | FastSend\r\n
0x30160000 | ZeroSend\r\n
0x30170000 | SndError\r\n
0x30180000 | LastSndError\r\n
0x30190000 | SrvdFrmCache\r\n
0x301a0000 | CachedNotModified\r\n
0x301b0000 | ResvUrl\r\n
0x301c0000 | ConnConnect\r\n
0x301d0000 | ConnClose\r\n
0x301e0000 | ConnCleanup\r\n
0x301f0000 | ChgUrlGrpProp\r\n
0x30200000 | ChgSrvSesProp\r\n
0x30210000 | ChgReqQueueProp\r\n
0x30220000 | AddUrl\r\n
0x30230000 | RemUrl\r\n
0x30240000 | RemAllUrls\r\n
0x30250000 | AddedCacheEntry\r\n
0x30260000 | AddCacheEntryFailed\r\n
0x30270000 | FlushedCache\r\n
0x30280000 | SslConnEvent\r\n
0x30290000 | SslInitiateHandshake\r\n
0x302a0000 | SslHandshakeComplete\r\n
0x302b0000 | SslInititateSslRcvClientCert\r\n
0x302c0000 | SslRcvClientCertFailed\r\n
0x302d0000 | SslRcvdRawData\r\n
0x302e0000 | SslDlvrdStreamData\r\n
0x302f0000 | SslAcceptStreamData\r\n
0x30310000 | ReadIpListEntry\r\n
0x30320000 | CreatedSslCred\r\n
0x30330000 | SendComplete\r\n
0x30340000 | SspiCall\r\n
0x30350000 | AuthCacheEntryAdded\r\n
0x30360000 | AuthCacheEntryFreed\r\n
0x30370000 | ConnIdAssgn\r\n
0x30380000 | QosFlowSetReset\r\n
0x30390000 | LoggingConfigFailed\r\n
0x303a0000 | LoggingConfig\r\n
0x303b0000 | LogFileCreateFailed\r\n
0x303c0000 | LogFileCreate\r\n
0x303d0000 | LogFileWrite\r\n
0x303e0000 | ParseRequestFailed\r\n
0x303f0000 | ConnTimedOut\r\n
0x30420000 | SslEndpointCreationFailed\r\n
0x30430000 | SslDisconnEvent\r\n
0x30440000 | SslDisconnReq\r\n
0x30450000 | SslUnsealMsg\r\n
0x30460000 | SslQueryConnInfoFailed\r\n
0x30470000 | SslEndpointConfigNotFound\r\n
0x30480000 | SslAsc\r\n
0x30490000 | SslSealMsg\r\n
0x304a0000 | RequestRejected\r\n
0x304b0000 | RequestCancelled\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x80003bc4 | SSL Certificate Settings deleted for Port : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for Port : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x91000001 | Microsoft-Windows-HttpEvent\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Resent will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client failed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occured while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0xc0003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0xc0003aad | An error occured while using SSL configuration for socket address %2.  The error status code is contained within the returned data.\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n

### 6.1.7600.16385, 6.1.7601.17514

Message identifier | Message string
--- | ---
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occuring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling ssl interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x1000000e | Flagged on all HTTP events dealing with global driver settings\r\n
0x1000000f | Flagged on all HTTP events in thread pool\r\n
0x11000038 | Classic\r\n
0x12000034 | SQM\r\n
0x3000000b | RecvReq\r\n
0x3000000c | Parse\r\n
0x3000000d | Deliver\r\n
0x3000000e | RecvResp\r\n
0x3000000f | RecvRespLast\r\n
0x30000010 | RecvBody\r\n
0x30000011 | RecvBodyLast\r\n
0x30000012 | FastRespLast\r\n
0x30000013 | FastResp\r\n
0x30000014 | CachedAndSend\r\n
0x30000015 | FastSend\r\n
0x30000016 | ZeroSend\r\n
0x30000017 | SndError\r\n
0x30000018 | LastSndError\r\n
0x30000019 | SrvdFrmCache\r\n
0x3000001a | CachedNotModified\r\n
0x3000001b | ResvUrl\r\n
0x3000001c | ConnConnect\r\n
0x3000001d | ConnClose\r\n
0x3000001e | ConnCleanup\r\n
0x3000001f | ChgUrlGrpProp\r\n
0x30000020 | ChgSrvSesProp\r\n
0x30000021 | ChgReqQueueProp\r\n
0x30000022 | AddUrl\r\n
0x30000023 | RemUrl\r\n
0x30000024 | RemAllUrls\r\n
0x30000025 | AddedCacheEntry\r\n
0x30000026 | AddCacheEntryFailed\r\n
0x30000027 | FlushedCache\r\n
0x30000028 | SslConnEvent\r\n
0x30000029 | SslInitiateHandshake\r\n
0x3000002a | SslHandshakeComplete\r\n
0x3000002b | SslInititateSslRcvClientCert\r\n
0x3000002c | SslRcvClientCertFailed\r\n
0x3000002d | SslRcvdRawData\r\n
0x3000002e | SslDlvrdStreamData\r\n
0x3000002f | SslAcceptStreamData\r\n
0x30000031 | ReadIpListEntry\r\n
0x30000032 | CreatedSslCred\r\n
0x30000033 | SendComplete\r\n
0x30000034 | SspiCall\r\n
0x30000035 | AuthCacheEntryAdded\r\n
0x30000036 | AuthCacheEntryFreed\r\n
0x30000037 | ConnIdAssgn\r\n
0x30000038 | QosFlowSetReset\r\n
0x30000039 | LoggingConfigFailed\r\n
0x3000003a | LoggingConfig\r\n
0x3000003b | LogFileCreateFailed\r\n
0x3000003c | LogFileCreate\r\n
0x3000003d | LogFileWrite\r\n
0x3000003e | ParseRequestFailed\r\n
0x3000003f | ConnTimedOut\r\n
0x30000042 | SslEndpointCreationFailed\r\n
0x30000043 | SslDisconnEvent\r\n
0x30000044 | SslDisconnReq\r\n
0x30000045 | SslUnsealMsg\r\n
0x30000046 | SslQueryConnInfoFailed\r\n
0x30000047 | SslEndpointConfigNotFound\r\n
0x30000048 | SslAsc\r\n
0x30000049 | SslSealMsg\r\n
0x3000004a | RequestRejected\r\n
0x3000004b | RequestCancelled\r\n
0x3000004c | HotAddProcFailed\r\n
0x3000004d | HotAddProcSucceeded\r\n
0x3000004e | UserResponseFlowInit\r\n
0x3000004f | CachedResponseFlowInit\r\n
0x30000050 | FlowInitFailed\r\n
0x30000051 | SetConnectionFlow\r\n
0x30000052 | RequestAssociatedToConfigurationFlow\r\n
0x30000053 | ConnectionFlowFailed\r\n
0x30000054 | ResponseRangeProcessingOK\r\n
0x30000055 | BeginBuildingSlices\r\n
0x30000056 | SendSliceCacheContent\r\n
0x30000057 | CachedSlicesMatchContent\r\n
0x30000058 | MergeSlicesToCache\r\n
0x30000059 | FlatCacheRangeSend\r\n
0x3000005a | ChannelBindAscParams\r\n
0x3000005b | ServiceBindCheckComplete\r\n
0x3000005c | ChannelBindConfigCapture\r\n
0x3000005d | ChannelBindPerResponseConfig\r\n
0x3000005e | UsePolicyBasedQoSFlow\r\n
0x3000005f | ThreadPoolExtension\r\n
0x30000060 | ThreadReady\r\n
0x30000061 | ThreadPoolTrim\r\n
0x30000062 | ThreadGone\r\n
0x32000002 | Stop\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x7000000b | HTTP Driver Global Settings Task\r\n
0x7000000c | HTTP Thread Pool\r\n
0x80003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0x80003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0x80003bc4 | SSL Certificate Settings deleted for Port : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for Port : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x91000001 | Microsoft-Windows-HttpEvent\r\n
0x91000002 | System\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Reset will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client completed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xb0000042 | Http.sys failed to process CPU hot-add. Processor number: %1, reason: %2, status: %3.\r\n
0xb0000043 | Hot-add information: Current UxNumberOfProcessors: %1, comment: %2.\r\n
0xb0000044 | Initialized QoS flow: FlowHandle %1, bandwidth %2, peak bandwidth %3, burst size %4\r\n
0xb0000046 | QoS flow initialization failed: bandwidth %1, peak bandwidth %2, burst size %3, status %4\r\n
0xb0000047 | Setting flow: Connection %1, FlowHandle %2\r\n
0xb0000048 | Assign to Configuration QoS Flow: FlowHandle %1\r\n
0xb0000049 | [re]Setting QoS Flow failed: Connection %1, FlowHandle %2, status %3\r\n
0xb000004a | Response range processing done. Req. %1, response content size %2, ranges %3 (%4-%5, %6-%7,...)\r\n
0xb000004b | Begin building slices. Req. %1, slices %2 (%3,%4,...), ranges %5 (%6-%7, %8-%9,...)\r\n
0xb000004c | Send cached slices. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004d | Cached slices match content. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004e | Merge slices to cache. CacheEntry %1, slices to merge %2, slices to cache %3\r\n
0xb000004f | Sending range from flat cache entry. CacheEntry %1, range %2-%3\r\n
0xb0000050 | Channel bind ASC parameters: connection %1, buffers %2, flags %3\r\n
0xb0000051 | Service bind check done. Connection %1, Context %2-%3, status %4, target %5\r\n
0xb0000052 | Captured channel bind config. Hardening %1, flags %2, service count %3\r\n
0xb0000053 | Channel bind response config overwrites %1\r\n
0xb0000054 | Policy-Based QoS: Connection %1, FlowHandle %2\r\n
0xb0000055 | Thread pool extension. Pool type: %1, active pools: %2.\r\n
0xb0000056 | Thread ready. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000057 | Thread pool trim. Pool type: %1, active pools: %2.\r\n
0xb0000058 | Thread gone. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0010010 | Response (request pointer %1, corresponding to request ID %4, site ID %2, number of bytes %3, endoding %5) queued for sending from the cache.\r\n
0xb0010011 | Response (request pointer %1, site ID %2, number of bytes %3, encoding %5) queued for sending with status code 304 (cache not modified).\r\n
0xb0010019 | Successfully added entry (URI %1) to cache (Encoding %7).\r\n
0xb001001a | Failed to add an entry (URI %1) to the cache. Status: %2. Encoding: %3.\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occured while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aad | An error occured while using SSL configuration for socket address %2.  The error status code is contained within the returned data.\r\n
0xc0003aae | Http.sys failed to process a CPU hot-add event. Status: %2 .\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occurring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling SSL interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x1000000e | Flagged on all HTTP events dealing with global driver settings\r\n
0x1000000f | Flagged on all HTTP events in thread pool\r\n
0x11000038 | Classic\r\n
0x12000034 | SQM\r\n
0x3000000b | RecvReq\r\n
0x3000000c | Parse\r\n
0x3000000d | Deliver\r\n
0x3000000e | RecvResp\r\n
0x3000000f | RecvRespLast\r\n
0x30000010 | RecvBody\r\n
0x30000011 | RecvBodyLast\r\n
0x30000012 | FastRespLast\r\n
0x30000013 | FastResp\r\n
0x30000014 | CachedAndSend\r\n
0x30000015 | FastSend\r\n
0x30000016 | ZeroSend\r\n
0x30000017 | SndError\r\n
0x30000018 | LastSndError\r\n
0x30000019 | SrvdFrmCache\r\n
0x3000001a | CachedNotModified\r\n
0x3000001b | ResvUrl\r\n
0x3000001c | ConnConnect\r\n
0x3000001d | ConnClose\r\n
0x3000001e | ConnCleanup\r\n
0x3000001f | ChgUrlGrpProp\r\n
0x30000020 | ChgSrvSesProp\r\n
0x30000021 | ChgReqQueueProp\r\n
0x30000022 | AddUrl\r\n
0x30000023 | RemUrl\r\n
0x30000024 | RemAllUrls\r\n
0x30000025 | AddedCacheEntry\r\n
0x30000026 | AddCacheEntryFailed\r\n
0x30000027 | FlushedCache\r\n
0x30000028 | SslConnEvent\r\n
0x30000029 | SslInitiateHandshake\r\n
0x3000002a | SslHandshakeComplete\r\n
0x3000002b | SslInititateSslRcvClientCert\r\n
0x3000002c | SslRcvClientCertFailed\r\n
0x3000002d | SslRcvdRawData\r\n
0x3000002e | SslDlvrdStreamData\r\n
0x3000002f | SslAcceptStreamData\r\n
0x30000031 | ReadIpListEntry\r\n
0x30000032 | CreatedSslCred\r\n
0x30000033 | SendComplete\r\n
0x30000034 | SspiCall\r\n
0x30000035 | AuthCacheEntryAdded\r\n
0x30000036 | AuthCacheEntryFreed\r\n
0x30000037 | ConnIdAssgn\r\n
0x30000038 | QosFlowSetReset\r\n
0x30000039 | LoggingConfigFailed\r\n
0x3000003a | LoggingConfig\r\n
0x3000003b | LogFileCreateFailed\r\n
0x3000003c | LogFileCreate\r\n
0x3000003d | LogFileWrite\r\n
0x3000003e | ParseRequestFailed\r\n
0x3000003f | ConnTimedOut\r\n
0x30000042 | SslEndpointCreationFailed\r\n
0x30000043 | SslDisconnEvent\r\n
0x30000044 | SslDisconnReq\r\n
0x30000045 | SslUnsealMsg\r\n
0x30000046 | SslQueryConnInfoFailed\r\n
0x30000047 | SslEndpointConfigNotFound\r\n
0x30000048 | SslAsc\r\n
0x30000049 | SslSealMsg\r\n
0x3000004a | RequestRejected\r\n
0x3000004b | RequestCancelled\r\n
0x3000004c | HotAddProcFailed\r\n
0x3000004d | HotAddProcSucceeded\r\n
0x3000004e | UserResponseFlowInit\r\n
0x3000004f | CachedResponseFlowInit\r\n
0x30000050 | FlowInitFailed\r\n
0x30000051 | SetConnectionFlow\r\n
0x30000052 | RequestAssociatedToConfigurationFlow\r\n
0x30000053 | ConnectionFlowFailed\r\n
0x30000054 | ResponseRangeProcessingOK\r\n
0x30000055 | BeginBuildingSlices\r\n
0x30000056 | SendSliceCacheContent\r\n
0x30000057 | CachedSlicesMatchContent\r\n
0x30000058 | MergeSlicesToCache\r\n
0x30000059 | FlatCacheRangeSend\r\n
0x3000005a | ChannelBindAscParams\r\n
0x3000005b | ServiceBindCheckComplete\r\n
0x3000005c | ChannelBindConfigCapture\r\n
0x3000005d | ChannelBindPerResponseConfig\r\n
0x3000005e | UsePolicyBasedQoSFlow\r\n
0x3000005f | ThreadPoolExtension\r\n
0x30000060 | ThreadReady\r\n
0x30000061 | ThreadPoolTrim\r\n
0x30000062 | ThreadGone\r\n
0x30000063 | SniParsed\r\n
0x30000064 | InitiateOpaqueMode\r\n
0x30000065 | EndpointAutoGenerated\r\n
0x30000066 | AutoGeneratedEndpointDeleted\r\n
0x30000067 | SslEndpointConfigFound\r\n
0x32000002 | Stop\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x7000000b | HTTP Driver Global Settings Task\r\n
0x7000000c | HTTP Thread Pool\r\n
0x80003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0x80003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0x80003bc4 | SSL Certificate Settings deleted for endpoint : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for endpoint : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x91000001 | Microsoft-Windows-HttpEvent\r\n
0x91000002 | System\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Reset will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client completed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xb0000042 | Http.sys failed to process CPU hot-add. Processor number: %1, reason: %2, status: %3.\r\n
0xb0000043 | Hot-add information: Current UxNumberOfProcessors: %1, comment: %2.\r\n
0xb0000044 | Initialized QoS flow: FlowHandle %1, bandwidth %2, peak bandwidth %3, burst size %4\r\n
0xb0000046 | QoS flow initialization failed: bandwidth %1, peak bandwidth %2, burst size %3, status %4\r\n
0xb0000047 | Setting flow: Connection %1, FlowHandle %2\r\n
0xb0000048 | Assign to Configuration QoS Flow: FlowHandle %1\r\n
0xb0000049 | [re]Setting QoS Flow failed: Connection %1, FlowHandle %2, status %3\r\n
0xb000004a | Response range processing done. Req. %1, response content size %2, ranges %3 (%4-%5, %6-%7,...)\r\n
0xb000004b | Begin building slices. Req. %1, slices %2 (%3,%4,...), ranges %5 (%6-%7, %8-%9,...)\r\n
0xb000004c | Send cached slices. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004d | Cached slices match content. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004e | Merge slices to cache. CacheEntry %1, slices to merge %2, slices to cache %3\r\n
0xb000004f | Sending range from flat cache entry. CacheEntry %1, range %2-%3\r\n
0xb0000050 | Channel bind ASC parameters: connection %1, buffers %2, flags %3\r\n
0xb0000051 | Service bind check done. Connection %1, Context %2-%3, status %4, target %5\r\n
0xb0000052 | Captured channel bind config. Hardening %1, flags %2, service count %3\r\n
0xb0000053 | Channel bind response config overwrites %1\r\n
0xb0000054 | Policy-Based QoS: Connection %1, FlowHandle %2\r\n
0xb0000055 | Thread pool extension. Pool type: %1, active pools: %2.\r\n
0xb0000056 | Thread ready. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000057 | Thread pool trim. Pool type: %1, active pools: %2.\r\n
0xb0000058 | Thread gone. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000059 | SNI parsed for connection: %1 with status: %2\r\n
0xb000005a | Request %1 has initated opaque mode\r\n
0xb000005b | Endpoint auto-generated for %2\r\n
0xb000005c | Deleted auto-generated endpoint for %2\r\n
0xb000005d | Inbound connection for IP: %3, SNI: %4. SSL endpoint found: %5\r\n
0xb0010010 | Response (request pointer %1, corresponding to request ID %4, site ID %2, number of bytes %3, encoding %5) queued for sending from the cache.\r\n
0xb0010011 | Response (request pointer %1, site ID %2, number of bytes %3, encoding %5) queued for sending with status code 304 (cache not modified).\r\n
0xb0010014 | SSL credentials for endpoint %2 successfully created.\r\n
0xb0010019 | Successfully added entry (URI %1) to cache (Encoding %7).\r\n
0xb001001a | Failed to add an entry (URI %1) to the cache. Status: %2. Encoding: %3.\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occurred while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aad | An error occurred while using SSL configuration for endpoint %2.  The error status code is contained within the returned data.\r\n
0xc0003aae | Http.sys failed to process a CPU hot-add event. Status: %2 .\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n

### 6.3.9600.16384, 6.3.9600.18819

Message identifier | Message string
--- | ---
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occurring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling SSL interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x1000000e | Flagged on all HTTP events dealing with global driver settings\r\n
0x1000000f | Flagged on all HTTP events in thread pool\r\n
0x11000001 | Flagged on all HTTP transactions\r\n
0x1100002a | Flagged on all HTTP events dealing with potential personally identifiable information\r\n
0x12000038 | Classic\r\n
0x13000034 | SQM\r\n
0x3000000b | RecvReq\r\n
0x3000000c | Parse\r\n
0x3000000d | Deliver\r\n
0x3000000e | RecvResp\r\n
0x3000000f | RecvRespLast\r\n
0x30000010 | RecvBody\r\n
0x30000011 | RecvBodyLast\r\n
0x30000012 | FastRespLast\r\n
0x30000013 | FastResp\r\n
0x30000014 | CachedAndSend\r\n
0x30000015 | FastSend\r\n
0x30000016 | ZeroSend\r\n
0x30000017 | SndError\r\n
0x30000018 | LastSndError\r\n
0x30000019 | SrvdFrmCache\r\n
0x3000001a | CachedNotModified\r\n
0x3000001b | ResvUrl\r\n
0x3000001c | ConnConnect\r\n
0x3000001d | ConnClose\r\n
0x3000001e | ConnCleanup\r\n
0x3000001f | ChgUrlGrpProp\r\n
0x30000020 | ChgSrvSesProp\r\n
0x30000021 | ChgReqQueueProp\r\n
0x30000022 | AddUrl\r\n
0x30000023 | RemUrl\r\n
0x30000024 | RemAllUrls\r\n
0x30000025 | AddedCacheEntry\r\n
0x30000026 | AddCacheEntryFailed\r\n
0x30000027 | FlushedCache\r\n
0x30000028 | SslConnEvent\r\n
0x30000029 | SslInitiateHandshake\r\n
0x3000002a | SslHandshakeComplete\r\n
0x3000002b | SslInititateSslRcvClientCert\r\n
0x3000002c | SslRcvClientCertFailed\r\n
0x3000002d | SslRcvdRawData\r\n
0x3000002e | SslDlvrdStreamData\r\n
0x3000002f | SslAcceptStreamData\r\n
0x30000031 | ReadIpListEntry\r\n
0x30000032 | CreatedSslCred\r\n
0x30000033 | SendComplete\r\n
0x30000034 | SspiCall\r\n
0x30000035 | AuthCacheEntryAdded\r\n
0x30000036 | AuthCacheEntryFreed\r\n
0x30000037 | ConnIdAssgn\r\n
0x30000038 | QosFlowSetReset\r\n
0x30000039 | LoggingConfigFailed\r\n
0x3000003a | LoggingConfig\r\n
0x3000003b | LogFileCreateFailed\r\n
0x3000003c | LogFileCreate\r\n
0x3000003d | LogFileWrite\r\n
0x3000003e | ParseRequestFailed\r\n
0x3000003f | ConnTimedOut\r\n
0x30000042 | SslEndpointCreationFailed\r\n
0x30000043 | SslDisconnEvent\r\n
0x30000044 | SslDisconnReq\r\n
0x30000045 | SslUnsealMsg\r\n
0x30000046 | SslQueryConnInfoFailed\r\n
0x30000047 | SslEndpointConfigNotFound\r\n
0x30000048 | SslAsc\r\n
0x30000049 | SslSealMsg\r\n
0x3000004a | RequestRejected\r\n
0x3000004b | RequestCancelled\r\n
0x3000004c | HotAddProcFailed\r\n
0x3000004d | HotAddProcSucceeded\r\n
0x3000004e | UserResponseFlowInit\r\n
0x3000004f | CachedResponseFlowInit\r\n
0x30000050 | FlowInitFailed\r\n
0x30000051 | SetConnectionFlow\r\n
0x30000052 | RequestAssociatedToConfigurationFlow\r\n
0x30000053 | ConnectionFlowFailed\r\n
0x30000054 | ResponseRangeProcessingOK\r\n
0x30000055 | BeginBuildingSlices\r\n
0x30000056 | SendSliceCacheContent\r\n
0x30000057 | CachedSlicesMatchContent\r\n
0x30000058 | MergeSlicesToCache\r\n
0x30000059 | FlatCacheRangeSend\r\n
0x3000005a | ChannelBindAscParams\r\n
0x3000005b | ServiceBindCheckComplete\r\n
0x3000005c | ChannelBindConfigCapture\r\n
0x3000005d | ChannelBindPerResponseConfig\r\n
0x3000005e | UsePolicyBasedQoSFlow\r\n
0x3000005f | ThreadPoolExtension\r\n
0x30000060 | ThreadReady\r\n
0x30000061 | ThreadPoolTrim\r\n
0x30000062 | ThreadGone\r\n
0x30000063 | SniParsed\r\n
0x30000064 | InitiateOpaqueMode\r\n
0x30000065 | EndpointAutoGenerated\r\n
0x30000066 | AutoGeneratedEndpointDeleted\r\n
0x30000067 | SslEndpointConfigFound\r\n
0x33000002 | Stop\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x7000000b | HTTP Driver Global Settings Task\r\n
0x7000000c | HTTP Thread Pool\r\n
0x80003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0x80003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0x80003bc4 | SSL Certificate Settings deleted for endpoint : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for endpoint : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x91000001 | Microsoft-Windows-HttpLog\r\n
0x91000002 | HTTP Log Channel\r\n
0x92000001 | Microsoft-Windows-HttpEvent\r\n
0x92000002 | System\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Reset will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client completed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xb0000042 | Http.sys failed to process CPU hot-add. Processor number: %1, reason: %2, status: %3.\r\n
0xb0000043 | Hot-add information: Current UxNumberOfProcessors: %1, comment: %2.\r\n
0xb0000044 | Initialized QoS flow: FlowHandle %1, bandwidth %2, peak bandwidth %3, burst size %4\r\n
0xb0000046 | QoS flow initialization failed: bandwidth %1, peak bandwidth %2, burst size %3, status %4\r\n
0xb0000047 | Setting flow: Connection %1, FlowHandle %2\r\n
0xb0000048 | Assign to Configuration QoS Flow: FlowHandle %1\r\n
0xb0000049 | [re]Setting QoS Flow failed: Connection %1, FlowHandle %2, status %3\r\n
0xb000004a | Response range processing done. Req. %1, response content size %2, ranges %3 (%4-%5, %6-%7,...)\r\n
0xb000004b | Begin building slices. Req. %1, slices %2 (%3,%4,...), ranges %5 (%6-%7, %8-%9,...)\r\n
0xb000004c | Send cached slices. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004d | Cached slices match content. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004e | Merge slices to cache. CacheEntry %1, slices to merge %2, slices to cache %3\r\n
0xb000004f | Sending range from flat cache entry. CacheEntry %1, range %2-%3\r\n
0xb0000050 | Channel bind ASC parameters: connection %1, buffers %2, flags %3\r\n
0xb0000051 | Service bind check done. Connection %1, Context %2-%3, status %4, target %5\r\n
0xb0000052 | Captured channel bind config. Hardening %1, flags %2, service count %3\r\n
0xb0000053 | Channel bind response config overwrites %1\r\n
0xb0000054 | Policy-Based QoS: Connection %1, FlowHandle %2\r\n
0xb0000055 | Thread pool extension. Pool type: %1, active pools: %2.\r\n
0xb0000056 | Thread ready. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000057 | Thread pool trim. Pool type: %1, active pools: %2.\r\n
0xb0000058 | Thread gone. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000059 | SNI parsed for connection: %1 with status: %2\r\n
0xb000005a | Request %1 has initated opaque mode\r\n
0xb000005b | Endpoint auto-generated for %2\r\n
0xb000005c | Deleted auto-generated endpoint for %2\r\n
0xb000005d | Inbound connection for IP: %3, SNI: %4. SSL endpoint found: %5\r\n
0xb0010010 | Response (request pointer %1, corresponding to request ID %4, site ID %2, number of bytes %3, encoding %5) queued for sending from the cache.\r\n
0xb0010011 | Response (request pointer %1, site ID %2, number of bytes %3, encoding %5) queued for sending with status code 304 (cache not modified).\r\n
0xb0010014 | SSL credentials for endpoint %2 successfully created.\r\n
0xb0010019 | Successfully added entry (URI %1) to cache (Encoding %7).\r\n
0xb001001a | Failed to add an entry (URI %1) to the cache. Status: %2. Encoding: %3.\r\n
0xb1000001 | HTTP transaction log\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occurred while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aad | An error occurred while using SSL configuration for endpoint %2.  The error status code is contained within the returned data.\r\n
0xc0003aae | Http.sys failed to process a CPU hot-add event. Status: %2 .\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.14393.351

Message identifier | Message string
--- | ---
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occurring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling SSL interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x1000000e | Flagged on all HTTP events dealing with global driver settings\r\n
0x1000000f | Flagged on all HTTP events in thread pool\r\n
0x11000001 | Flagged on all HTTP transactions\r\n
0x1100002a | Flagged on all HTTP events dealing with potential personally identifiable information\r\n
0x12000038 | Classic\r\n
0x13000034 | SQM\r\n
0x3000000b | RecvReq\r\n
0x3000000c | Parse\r\n
0x3000000d | Deliver\r\n
0x3000000e | RecvResp\r\n
0x3000000f | RecvRespLast\r\n
0x30000010 | RecvBody\r\n
0x30000011 | RecvBodyLast\r\n
0x30000012 | FastRespLast\r\n
0x30000013 | FastResp\r\n
0x30000014 | CachedAndSend\r\n
0x30000015 | FastSend\r\n
0x30000016 | ZeroSend\r\n
0x30000017 | SndError\r\n
0x30000018 | LastSndError\r\n
0x30000019 | SrvdFrmCache\r\n
0x3000001a | CachedNotModified\r\n
0x3000001b | ResvUrl\r\n
0x3000001c | ConnConnect\r\n
0x3000001d | ConnClose\r\n
0x3000001e | ConnCleanup\r\n
0x3000001f | ChgUrlGrpProp\r\n
0x30000020 | ChgSrvSesProp\r\n
0x30000021 | ChgReqQueueProp\r\n
0x30000022 | AddUrl\r\n
0x30000023 | RemUrl\r\n
0x30000024 | RemAllUrls\r\n
0x30000025 | AddedCacheEntry\r\n
0x30000026 | AddCacheEntryFailed\r\n
0x30000027 | FlushedCache\r\n
0x30000028 | SslConnEvent\r\n
0x30000029 | SslInitiateHandshake\r\n
0x3000002a | SslHandshakeComplete\r\n
0x3000002b | SslInititateSslRcvClientCert\r\n
0x3000002c | SslRcvClientCertFailed\r\n
0x3000002d | SslRcvdRawData\r\n
0x3000002e | SslDlvrdStreamData\r\n
0x3000002f | SslAcceptStreamData\r\n
0x30000031 | ReadIpListEntry\r\n
0x30000032 | CreatedSslCred\r\n
0x30000033 | SendComplete\r\n
0x30000034 | SspiCall\r\n
0x30000035 | AuthCacheEntryAdded\r\n
0x30000036 | AuthCacheEntryFreed\r\n
0x30000037 | ConnIdAssgn\r\n
0x30000038 | QosFlowSetReset\r\n
0x30000039 | LoggingConfigFailed\r\n
0x3000003a | LoggingConfig\r\n
0x3000003b | LogFileCreateFailed\r\n
0x3000003c | LogFileCreate\r\n
0x3000003d | LogFileWrite\r\n
0x3000003e | ParseRequestFailed\r\n
0x3000003f | ConnTimedOut\r\n
0x30000042 | SslEndpointCreationFailed\r\n
0x30000043 | SslDisconnEvent\r\n
0x30000044 | SslDisconnReq\r\n
0x30000045 | SslUnsealMsg\r\n
0x30000046 | SslQueryConnInfoFailed\r\n
0x30000047 | SslEndpointConfigNotFound\r\n
0x30000048 | SslAsc\r\n
0x30000049 | SslSealMsg\r\n
0x3000004a | RequestRejected\r\n
0x3000004b | RequestCancelled\r\n
0x3000004c | HotAddProcFailed\r\n
0x3000004d | HotAddProcSucceeded\r\n
0x3000004e | UserResponseFlowInit\r\n
0x3000004f | CachedResponseFlowInit\r\n
0x30000050 | FlowInitFailed\r\n
0x30000051 | SetConnectionFlow\r\n
0x30000052 | RequestAssociatedToConfigurationFlow\r\n
0x30000053 | ConnectionFlowFailed\r\n
0x30000054 | ResponseRangeProcessingOK\r\n
0x30000055 | BeginBuildingSlices\r\n
0x30000056 | SendSliceCacheContent\r\n
0x30000057 | CachedSlicesMatchContent\r\n
0x30000058 | MergeSlicesToCache\r\n
0x30000059 | FlatCacheRangeSend\r\n
0x3000005a | ChannelBindAscParams\r\n
0x3000005b | ServiceBindCheckComplete\r\n
0x3000005c | ChannelBindConfigCapture\r\n
0x3000005d | ChannelBindPerResponseConfig\r\n
0x3000005e | UsePolicyBasedQoSFlow\r\n
0x3000005f | ThreadPoolExtension\r\n
0x30000060 | ThreadReady\r\n
0x30000061 | ThreadPoolTrim\r\n
0x30000062 | ThreadGone\r\n
0x30000063 | SniParsed\r\n
0x30000064 | InitiateOpaqueMode\r\n
0x30000065 | EndpointAutoGenerated\r\n
0x30000066 | AutoGeneratedEndpointDeleted\r\n
0x30000067 | SslEndpointConfigFound\r\n
0x30000068 | SslEndpointConfigRejected\r\n
0x33000002 | Stop\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x7000000b | HTTP Driver Global Settings Task\r\n
0x7000000c | HTTP Thread Pool\r\n
0x80003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0x80003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0x80003bc4 | SSL Certificate Settings deleted for endpoint : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for endpoint : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x91000001 | Microsoft-Windows-HttpLog\r\n
0x91000002 | HTTP Log Channel\r\n
0x92000001 | Microsoft-Windows-HttpEvent\r\n
0x92000002 | System\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Reset will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client completed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xb0000042 | Http.sys failed to process CPU hot-add. Processor number: %1, reason: %2, status: %3.\r\n
0xb0000043 | Hot-add information: Current UxNumberOfProcessors: %1, comment: %2.\r\n
0xb0000044 | Initialized QoS flow: FlowHandle %1, bandwidth %2, peak bandwidth %3, burst size %4\r\n
0xb0000046 | QoS flow initialization failed: bandwidth %1, peak bandwidth %2, burst size %3, status %4\r\n
0xb0000047 | Setting flow: Connection %1, FlowHandle %2\r\n
0xb0000048 | Assign to Configuration QoS Flow: FlowHandle %1\r\n
0xb0000049 | [re]Setting QoS Flow failed: Connection %1, FlowHandle %2, status %3\r\n
0xb000004a | Response range processing done. Req. %1, response content size %2, ranges %3 (%4-%5, %6-%7,...)\r\n
0xb000004b | Begin building slices. Req. %1, slices %2 (%3,%4,...), ranges %5 (%6-%7, %8-%9,...)\r\n
0xb000004c | Send cached slices. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004d | Cached slices match content. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004e | Merge slices to cache. CacheEntry %1, slices to merge %2, slices to cache %3\r\n
0xb000004f | Sending range from flat cache entry. CacheEntry %1, range %2-%3\r\n
0xb0000050 | Channel bind ASC parameters: connection %1, buffers %2, flags %3\r\n
0xb0000051 | Service bind check done. Connection %1, Context %2-%3, status %4, target %5\r\n
0xb0000052 | Captured channel bind config. Hardening %1, flags %2, service count %3\r\n
0xb0000053 | Channel bind response config overwrites %1\r\n
0xb0000054 | Policy-Based QoS: Connection %1, FlowHandle %2\r\n
0xb0000055 | Thread pool extension. Pool type: %1, active pools: %2.\r\n
0xb0000056 | Thread ready. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000057 | Thread pool trim. Pool type: %1, active pools: %2.\r\n
0xb0000058 | Thread gone. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000059 | SNI parsed for connection: %1 with status: %2\r\n
0xb000005a | Request %1 has initated opaque mode\r\n
0xb000005b | Endpoint auto-generated for %2\r\n
0xb000005c | Deleted auto-generated endpoint for %2\r\n
0xb000005d | Inbound connection for IP: %3, SNI: %4. SSL endpoint found: %5\r\n
0xb000005e | SSL connection with local IP address and port %2 rejected due to configuration policy.\r\n
0xb0010010 | Response (request pointer %1, corresponding to request ID %4, site ID %2, number of bytes %3, encoding %5) queued for sending from the cache.\r\n
0xb0010011 | Response (request pointer %1, site ID %2, number of bytes %3, encoding %5) queued for sending with status code 304 (cache not modified).\r\n
0xb0010014 | SSL credentials for endpoint %2 successfully created.\r\n
0xb0010019 | Successfully added entry (URI %1) to cache (Encoding %7).\r\n
0xb001001a | Failed to add an entry (URI %1) to the cache. Status: %2. Encoding: %3.\r\n
0xb1000001 | HTTP transaction log\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occurred while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aad | An error occurred while using SSL configuration for endpoint %2.  The error status code is contained within the returned data.\r\n
0xc0003aae | Http.sys failed to process a CPU hot-add event. Status: %2 .\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n

### 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occurring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling SSL interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x1000000e | Flagged on all HTTP events dealing with global driver settings\r\n
0x1000000f | Flagged on all HTTP events in thread pool\r\n
0x11000001 | Flagged on all HTTP transactions\r\n
0x1100002a | Flagged on all HTTP events dealing with potential personally identifiable information\r\n
0x12000038 | Classic\r\n
0x13000034 | SQM\r\n
0x3000000b | RecvReq\r\n
0x3000000c | Parse\r\n
0x3000000d | Deliver\r\n
0x3000000e | RecvResp\r\n
0x3000000f | RecvRespLast\r\n
0x30000010 | RecvBody\r\n
0x30000011 | RecvBodyLast\r\n
0x30000012 | FastRespLast\r\n
0x30000013 | FastResp\r\n
0x30000014 | CachedAndSend\r\n
0x30000015 | FastSend\r\n
0x30000016 | ZeroSend\r\n
0x30000017 | SndError\r\n
0x30000018 | LastSndError\r\n
0x30000019 | SrvdFrmCache\r\n
0x3000001a | CachedNotModified\r\n
0x3000001b | ResvUrl\r\n
0x3000001c | ConnConnect\r\n
0x3000001d | ConnClose\r\n
0x3000001e | ConnCleanup\r\n
0x3000001f | ChgUrlGrpProp\r\n
0x30000020 | ChgSrvSesProp\r\n
0x30000021 | ChgReqQueueProp\r\n
0x30000022 | AddUrl\r\n
0x30000023 | RemUrl\r\n
0x30000024 | RemAllUrls\r\n
0x30000025 | AddedCacheEntry\r\n
0x30000026 | AddCacheEntryFailed\r\n
0x30000027 | FlushedCache\r\n
0x30000028 | SslConnEvent\r\n
0x30000029 | SslInitiateHandshake\r\n
0x3000002a | SslHandshakeComplete\r\n
0x3000002b | SslInititateSslRcvClientCert\r\n
0x3000002c | SslRcvClientCertFailed\r\n
0x3000002d | SslRcvdRawData\r\n
0x3000002e | SslDlvrdStreamData\r\n
0x3000002f | SslAcceptStreamData\r\n
0x30000031 | ReadIpListEntry\r\n
0x30000032 | CreatedSslCred\r\n
0x30000033 | SendComplete\r\n
0x30000034 | SspiCall\r\n
0x30000035 | AuthCacheEntryAdded\r\n
0x30000036 | AuthCacheEntryFreed\r\n
0x30000037 | ConnIdAssgn\r\n
0x30000038 | QosFlowSetReset\r\n
0x30000039 | LoggingConfigFailed\r\n
0x3000003a | LoggingConfig\r\n
0x3000003b | LogFileCreateFailed\r\n
0x3000003c | LogFileCreate\r\n
0x3000003d | LogFileWrite\r\n
0x3000003e | ParseRequestFailed\r\n
0x3000003f | ConnTimedOut\r\n
0x30000042 | SslEndpointCreationFailed\r\n
0x30000043 | SslDisconnEvent\r\n
0x30000044 | SslDisconnReq\r\n
0x30000045 | SslUnsealMsg\r\n
0x30000046 | SslQueryConnInfoFailed\r\n
0x30000047 | SslEndpointConfigNotFound\r\n
0x30000048 | SslAsc\r\n
0x30000049 | SslSealMsg\r\n
0x3000004a | RequestRejected\r\n
0x3000004b | RequestCancelled\r\n
0x3000004c | HotAddProcFailed\r\n
0x3000004d | HotAddProcSucceeded\r\n
0x3000004e | UserResponseFlowInit\r\n
0x3000004f | CachedResponseFlowInit\r\n
0x30000050 | FlowInitFailed\r\n
0x30000051 | SetConnectionFlow\r\n
0x30000052 | RequestAssociatedToConfigurationFlow\r\n
0x30000053 | ConnectionFlowFailed\r\n
0x30000054 | ResponseRangeProcessingOK\r\n
0x30000055 | BeginBuildingSlices\r\n
0x30000056 | SendSliceCacheContent\r\n
0x30000057 | CachedSlicesMatchContent\r\n
0x30000058 | MergeSlicesToCache\r\n
0x30000059 | FlatCacheRangeSend\r\n
0x3000005a | ChannelBindAscParams\r\n
0x3000005b | ServiceBindCheckComplete\r\n
0x3000005c | ChannelBindConfigCapture\r\n
0x3000005d | ChannelBindPerResponseConfig\r\n
0x3000005e | UsePolicyBasedQoSFlow\r\n
0x3000005f | ThreadPoolExtension\r\n
0x30000060 | ThreadReady\r\n
0x30000061 | ThreadPoolTrim\r\n
0x30000062 | ThreadGone\r\n
0x30000063 | SniParsed\r\n
0x30000064 | InitiateOpaqueMode\r\n
0x30000065 | EndpointAutoGenerated\r\n
0x30000066 | AutoGeneratedEndpointDeleted\r\n
0x30000067 | SslEndpointConfigFound\r\n
0x30000068 | SslEndpointConfigRejected\r\n
0x33000002 | Stop\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x7000000b | HTTP Driver Global Settings Task\r\n
0x7000000c | HTTP Thread Pool\r\n
0x80003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0x80003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0x80003bc4 | SSL Certificate Settings deleted for endpoint : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for endpoint : %2 .\r\n
0x80003bc6 | SSL Certificate Settings updated by an admin process for endpoint : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x91000001 | Microsoft-Windows-HttpLog\r\n
0x91000002 | HTTP Log Channel\r\n
0x92000001 | Microsoft-Windows-HttpEvent\r\n
0x92000002 | System\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Reset will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client completed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xb0000042 | Http.sys failed to process CPU hot-add. Processor number: %1, reason: %2, status: %3.\r\n
0xb0000043 | Hot-add information: Current UxNumberOfProcessors: %1, comment: %2.\r\n
0xb0000044 | Initialized QoS flow: FlowHandle %1, bandwidth %2, peak bandwidth %3, burst size %4\r\n
0xb0000046 | QoS flow initialization failed: bandwidth %1, peak bandwidth %2, burst size %3, status %4\r\n
0xb0000047 | Setting flow: Connection %1, FlowHandle %2\r\n
0xb0000048 | Assign to Configuration QoS Flow: FlowHandle %1\r\n
0xb0000049 | [re]Setting QoS Flow failed: Connection %1, FlowHandle %2, status %3\r\n
0xb000004a | Response range processing done. Req. %1, response content size %2, ranges %3 (%4-%5, %6-%7,...)\r\n
0xb000004b | Begin building slices. Req. %1, slices %2 (%3,%4,...), ranges %5 (%6-%7, %8-%9,...)\r\n
0xb000004c | Send cached slices. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004d | Cached slices match content. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004e | Merge slices to cache. CacheEntry %1, slices to merge %2, slices to cache %3\r\n
0xb000004f | Sending range from flat cache entry. CacheEntry %1, range %2-%3\r\n
0xb0000050 | Channel bind ASC parameters: connection %1, buffers %2, flags %3\r\n
0xb0000051 | Service bind check done. Connection %1, Context %2-%3, status %4, target %5\r\n
0xb0000052 | Captured channel bind config. Hardening %1, flags %2, service count %3\r\n
0xb0000053 | Channel bind response config overwrites %1\r\n
0xb0000054 | Policy-Based QoS: Connection %1, FlowHandle %2\r\n
0xb0000055 | Thread pool extension. Pool type: %1, active pools: %2.\r\n
0xb0000056 | Thread ready. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000057 | Thread pool trim. Pool type: %1, active pools: %2.\r\n
0xb0000058 | Thread gone. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000059 | SNI parsed for connection: %1 with status: %2\r\n
0xb000005a | Request %1 has initated opaque mode\r\n
0xb000005b | Endpoint auto-generated for %2\r\n
0xb000005c | Deleted auto-generated endpoint for %2\r\n
0xb000005d | Inbound connection for IP: %3, SNI: %4. SSL endpoint found: %5\r\n
0xb000005e | SSL connection with local IP address and port %2 rejected due to configuration policy.\r\n
0xb0010010 | Response (request pointer %1, corresponding to request ID %4, site ID %2, number of bytes %3, encoding %5) queued for sending from the cache.\r\n
0xb0010011 | Response (request pointer %1, site ID %2, number of bytes %3, encoding %5) queued for sending with status code 304 (cache not modified).\r\n
0xb0010014 | SSL credentials for endpoint %2 successfully created.\r\n
0xb0010019 | Successfully added entry (URI %1) to cache (Encoding %7).\r\n
0xb001001a | Failed to add an entry (URI %1) to the cache. Status: %2. Encoding: %3.\r\n
0xb1000001 | HTTP transaction log\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occurred while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aad | An error occurred while using SSL configuration for endpoint %2.  The error status code is contained within the returned data.\r\n
0xc0003aae | Http.sys failed to process a CPU hot-add event. Status: %2 .\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n

### 10.0.17134.619, 10.0.17763.404

Message identifier | Message string
--- | ---
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occurring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling SSL interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x1000000e | Flagged on all HTTP events dealing with global driver settings\r\n
0x1000000f | Flagged on all HTTP events in thread pool\r\n
0x11000001 | Flagged on all HTTP transactions\r\n
0x1100002a | Flagged on all HTTP events dealing with potential personally identifiable information\r\n
0x12000038 | Classic\r\n
0x13000034 | SQM\r\n
0x3000000b | RecvReq\r\n
0x3000000c | Parse\r\n
0x3000000d | Deliver\r\n
0x3000000e | RecvResp\r\n
0x3000000f | RecvRespLast\r\n
0x30000010 | RecvBody\r\n
0x30000011 | RecvBodyLast\r\n
0x30000012 | FastRespLast\r\n
0x30000013 | FastResp\r\n
0x30000014 | CachedAndSend\r\n
0x30000015 | FastSend\r\n
0x30000016 | ZeroSend\r\n
0x30000017 | SndError\r\n
0x30000018 | LastSndError\r\n
0x30000019 | SrvdFrmCache\r\n
0x3000001a | CachedNotModified\r\n
0x3000001b | ResvUrl\r\n
0x3000001c | ConnConnect\r\n
0x3000001d | ConnClose\r\n
0x3000001e | ConnCleanup\r\n
0x3000001f | ChgUrlGrpProp\r\n
0x30000020 | ChgSrvSesProp\r\n
0x30000021 | ChgReqQueueProp\r\n
0x30000022 | AddUrl\r\n
0x30000023 | RemUrl\r\n
0x30000024 | RemAllUrls\r\n
0x30000025 | AddedCacheEntry\r\n
0x30000026 | AddCacheEntryFailed\r\n
0x30000027 | FlushedCache\r\n
0x30000028 | SslConnEvent\r\n
0x30000029 | SslInitiateHandshake\r\n
0x3000002a | SslHandshakeComplete\r\n
0x3000002b | SslInititateSslRcvClientCert\r\n
0x3000002c | SslRcvClientCertFailed\r\n
0x3000002d | SslRcvdRawData\r\n
0x3000002e | SslDlvrdStreamData\r\n
0x3000002f | SslAcceptStreamData\r\n
0x30000031 | ReadIpListEntry\r\n
0x30000032 | CreatedSslCred\r\n
0x30000033 | SendComplete\r\n
0x30000034 | SspiCall\r\n
0x30000035 | AuthCacheEntryAdded\r\n
0x30000036 | AuthCacheEntryFreed\r\n
0x30000037 | ConnIdAssgn\r\n
0x30000038 | QosFlowSetReset\r\n
0x30000039 | LoggingConfigFailed\r\n
0x3000003a | LoggingConfig\r\n
0x3000003b | LogFileCreateFailed\r\n
0x3000003c | LogFileCreate\r\n
0x3000003d | LogFileWrite\r\n
0x3000003e | ParseRequestFailed\r\n
0x3000003f | ConnTimedOut\r\n
0x30000042 | SslEndpointCreationFailed\r\n
0x30000043 | SslDisconnEvent\r\n
0x30000044 | SslDisconnReq\r\n
0x30000045 | SslUnsealMsg\r\n
0x30000046 | SslQueryConnInfoFailed\r\n
0x30000047 | SslEndpointConfigNotFound\r\n
0x30000048 | SslAsc\r\n
0x30000049 | SslSealMsg\r\n
0x3000004a | RequestRejected\r\n
0x3000004b | RequestCancelled\r\n
0x3000004c | HotAddProcFailed\r\n
0x3000004d | HotAddProcSucceeded\r\n
0x3000004e | UserResponseFlowInit\r\n
0x3000004f | CachedResponseFlowInit\r\n
0x30000050 | FlowInitFailed\r\n
0x30000051 | SetConnectionFlow\r\n
0x30000052 | RequestAssociatedToConfigurationFlow\r\n
0x30000053 | ConnectionFlowFailed\r\n
0x30000054 | ResponseRangeProcessingOK\r\n
0x30000055 | BeginBuildingSlices\r\n
0x30000056 | SendSliceCacheContent\r\n
0x30000057 | CachedSlicesMatchContent\r\n
0x30000058 | MergeSlicesToCache\r\n
0x30000059 | FlatCacheRangeSend\r\n
0x3000005a | ChannelBindAscParams\r\n
0x3000005b | ServiceBindCheckComplete\r\n
0x3000005c | ChannelBindConfigCapture\r\n
0x3000005d | ChannelBindPerResponseConfig\r\n
0x3000005e | UsePolicyBasedQoSFlow\r\n
0x3000005f | ThreadPoolExtension\r\n
0x30000060 | ThreadReady\r\n
0x30000061 | ThreadPoolTrim\r\n
0x30000062 | ThreadGone\r\n
0x30000063 | SniParsed\r\n
0x30000064 | InitiateOpaqueMode\r\n
0x30000065 | EndpointAutoGenerated\r\n
0x30000066 | AutoGeneratedEndpointDeleted\r\n
0x30000067 | SslEndpointConfigFound\r\n
0x30000068 | SslEndpointConfigRejected\r\n
0x33000002 | Stop\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x7000000b | HTTP Driver Global Settings Task\r\n
0x7000000c | HTTP Thread Pool\r\n
0x7000000d | HTTP Response Trace Task\r\n
0x80003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0x80003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0x80003bc4 | SSL Certificate Settings deleted for endpoint : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for endpoint : %2 .\r\n
0x80003bc6 | SSL Certificate Settings updated by an admin process for endpoint : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x91000001 | Microsoft-Windows-HttpLog\r\n
0x91000002 | HTTP Log Channel\r\n
0x92000001 | Microsoft-Windows-HttpEvent\r\n
0x92000002 | System\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Reset will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client completed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xb0000042 | Http.sys failed to process CPU hot-add. Processor number: %1, reason: %2, status: %3.\r\n
0xb0000043 | Hot-add information: Current UxNumberOfProcessors: %1, comment: %2.\r\n
0xb0000044 | Initialized QoS flow: FlowHandle %1, bandwidth %2, peak bandwidth %3, burst size %4\r\n
0xb0000046 | QoS flow initialization failed: bandwidth %1, peak bandwidth %2, burst size %3, status %4\r\n
0xb0000047 | Setting flow: Connection %1, FlowHandle %2\r\n
0xb0000048 | Assign to Configuration QoS Flow: FlowHandle %1\r\n
0xb0000049 | [re]Setting QoS Flow failed: Connection %1, FlowHandle %2, status %3\r\n
0xb000004a | Response range processing done. Req. %1, response content size %2, ranges %3 (%4-%5, %6-%7,...)\r\n
0xb000004b | Begin building slices. Req. %1, slices %2 (%3,%4,...), ranges %5 (%6-%7, %8-%9,...)\r\n
0xb000004c | Send cached slices. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004d | Cached slices match content. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004e | Merge slices to cache. CacheEntry %1, slices to merge %2, slices to cache %3\r\n
0xb000004f | Sending range from flat cache entry. CacheEntry %1, range %2-%3\r\n
0xb0000050 | Channel bind ASC parameters: connection %1, buffers %2, flags %3\r\n
0xb0000051 | Service bind check done. Connection %1, Context %2-%3, status %4, target %5\r\n
0xb0000052 | Captured channel bind config. Hardening %1, flags %2, service count %3\r\n
0xb0000053 | Channel bind response config overwrites %1\r\n
0xb0000054 | Policy-Based QoS: Connection %1, FlowHandle %2\r\n
0xb0000055 | Thread pool extension. Pool type: %1, active pools: %2.\r\n
0xb0000056 | Thread ready. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000057 | Thread pool trim. Pool type: %1, active pools: %2.\r\n
0xb0000058 | Thread gone. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000059 | SNI parsed for connection: %1 with status: %2\r\n
0xb000005a | Request %1 has initated opaque mode\r\n
0xb000005b | Endpoint auto-generated for %2\r\n
0xb000005c | Deleted auto-generated endpoint for %2\r\n
0xb000005d | Inbound connection for IP: %3, SNI: %4. SSL endpoint found: %5\r\n
0xb000005e | SSL connection with local IP address and port %2 rejected due to configuration policy.\r\n
0xb000005f | Parsing of response (response ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0010010 | Response (request pointer %1, corresponding to request ID %4, site ID %2, number of bytes %3, encoding %5) queued for sending from the cache.\r\n
0xb0010011 | Response (request pointer %1, site ID %2, number of bytes %3, encoding %5) queued for sending with status code 304 (cache not modified).\r\n
0xb0010014 | SSL credentials for endpoint %2 successfully created.\r\n
0xb0010019 | Successfully added entry (URI %1) to cache (Encoding %7).\r\n
0xb001001a | Failed to add an entry (URI %1) to the cache. Status: %2. Encoding: %3.\r\n
0xb1000001 | HTTP transaction log\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occurred while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aad | An error occurred while using SSL configuration for endpoint %2.  The error status code is contained within the returned data.\r\n
0xc0003aae | Http.sys failed to process a CPU hot-add event. Status: %2 .\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n

### 10.0.18362.1, 10.0.18362.752

Message identifier | Message string
--- | ---
0x00000060 | SSL handshake failed. Local IP: %2, Remote IP: %4, SNI: %5, Thumbprint: %7, Client Initiated Disconnect: %8, Abortive Disconnect: %9, Connection Status: %10\r\n
0x00000061 | HTTP error response sent. Url: %1, Verb: %2, Status Code: %3, Cache Send: %4, Request Queue: %5, PID: %6, TID: %7, Image Name: %8, Working Set(Bytes): %9, Send Status: %10, Thread Count: %11, Reason Phrase: %12, Error Cause: %13, Verbosity: %14\r\n
0x00000062 | SSL renegotiate timed out. Local IP: %2, Remote IP: %4, SNI: %5, Thumbprint: %7, Connection Buffer Full: %8\r\n
0x00000063 | HTTP 11 Required. Verb: %1, Fault Code: %2\r\n
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occurring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling SSL interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x1000000e | Flagged on all HTTP events dealing with global driver settings\r\n
0x1000000f | Flagged on all HTTP events in thread pool\r\n
0x11000001 | Flagged on all HTTP transactions\r\n
0x1100002a | Flagged on all HTTP events dealing with potential personally identifiable information\r\n
0x12000038 | Classic\r\n
0x13000034 | SQM\r\n
0x3000000b | RecvReq\r\n
0x3000000c | Parse\r\n
0x3000000d | Deliver\r\n
0x3000000e | RecvResp\r\n
0x3000000f | RecvRespLast\r\n
0x30000010 | RecvBody\r\n
0x30000011 | RecvBodyLast\r\n
0x30000012 | FastRespLast\r\n
0x30000013 | FastResp\r\n
0x30000014 | CachedAndSend\r\n
0x30000015 | FastSend\r\n
0x30000016 | ZeroSend\r\n
0x30000017 | SndError\r\n
0x30000018 | LastSndError\r\n
0x30000019 | SrvdFrmCache\r\n
0x3000001a | CachedNotModified\r\n
0x3000001b | ResvUrl\r\n
0x3000001c | ConnConnect\r\n
0x3000001d | ConnClose\r\n
0x3000001e | ConnCleanup\r\n
0x3000001f | ChgUrlGrpProp\r\n
0x30000020 | ChgSrvSesProp\r\n
0x30000021 | ChgReqQueueProp\r\n
0x30000022 | AddUrl\r\n
0x30000023 | RemUrl\r\n
0x30000024 | RemAllUrls\r\n
0x30000025 | AddedCacheEntry\r\n
0x30000026 | AddCacheEntryFailed\r\n
0x30000027 | FlushedCache\r\n
0x30000028 | SslConnEvent\r\n
0x30000029 | SslInitiateHandshake\r\n
0x3000002a | SslHandshakeComplete\r\n
0x3000002b | SslInititateSslRcvClientCert\r\n
0x3000002c | SslRcvClientCertFailed\r\n
0x3000002d | SslRcvdRawData\r\n
0x3000002e | SslDlvrdStreamData\r\n
0x3000002f | SslAcceptStreamData\r\n
0x30000031 | ReadIpListEntry\r\n
0x30000032 | CreatedSslCred\r\n
0x30000033 | SendComplete\r\n
0x30000034 | SspiCall\r\n
0x30000035 | AuthCacheEntryAdded\r\n
0x30000036 | AuthCacheEntryFreed\r\n
0x30000037 | ConnIdAssgn\r\n
0x30000038 | QosFlowSetReset\r\n
0x30000039 | LoggingConfigFailed\r\n
0x3000003a | LoggingConfig\r\n
0x3000003b | LogFileCreateFailed\r\n
0x3000003c | LogFileCreate\r\n
0x3000003d | LogFileWrite\r\n
0x3000003e | ParseRequestFailed\r\n
0x3000003f | ConnTimedOut\r\n
0x30000042 | SslEndpointCreationFailed\r\n
0x30000043 | SslDisconnEvent\r\n
0x30000044 | SslDisconnReq\r\n
0x30000045 | SslUnsealMsg\r\n
0x30000046 | SslQueryConnInfoFailed\r\n
0x30000047 | SslEndpointConfigNotFound\r\n
0x30000048 | SslAsc\r\n
0x30000049 | SslSealMsg\r\n
0x3000004a | RequestRejected\r\n
0x3000004b | RequestCancelled\r\n
0x3000004c | HotAddProcFailed\r\n
0x3000004d | HotAddProcSucceeded\r\n
0x3000004e | UserResponseFlowInit\r\n
0x3000004f | CachedResponseFlowInit\r\n
0x30000050 | FlowInitFailed\r\n
0x30000051 | SetConnectionFlow\r\n
0x30000052 | RequestAssociatedToConfigurationFlow\r\n
0x30000053 | ConnectionFlowFailed\r\n
0x30000054 | ResponseRangeProcessingOK\r\n
0x30000055 | BeginBuildingSlices\r\n
0x30000056 | SendSliceCacheContent\r\n
0x30000057 | CachedSlicesMatchContent\r\n
0x30000058 | MergeSlicesToCache\r\n
0x30000059 | FlatCacheRangeSend\r\n
0x3000005a | ChannelBindAscParams\r\n
0x3000005b | ServiceBindCheckComplete\r\n
0x3000005c | ChannelBindConfigCapture\r\n
0x3000005d | ChannelBindPerResponseConfig\r\n
0x3000005e | UsePolicyBasedQoSFlow\r\n
0x3000005f | ThreadPoolExtension\r\n
0x30000060 | ThreadReady\r\n
0x30000061 | ThreadPoolTrim\r\n
0x30000062 | ThreadGone\r\n
0x30000063 | SniParsed\r\n
0x30000064 | InitiateOpaqueMode\r\n
0x30000065 | EndpointAutoGenerated\r\n
0x30000066 | AutoGeneratedEndpointDeleted\r\n
0x30000067 | SslEndpointConfigFound\r\n
0x30000068 | SslEndpointConfigRejected\r\n
0x30000069 | SslHandshakeFailure\r\n
0x3000006a | HttpErrorResponseSent\r\n
0x3000006b | SslRenegotiateTimedOut\r\n
0x3000006c | Http11Required\r\n
0x33000002 | Stop\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x7000000b | HTTP Driver Global Settings Task\r\n
0x7000000c | HTTP Thread Pool\r\n
0x7000000d | HTTP Response Trace Task\r\n
0x80003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0x80003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0x80003bc4 | SSL Certificate Settings deleted for endpoint : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for endpoint : %2 .\r\n
0x80003bc6 | SSL Certificate Settings updated by an admin process for endpoint : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x90000003 | System\r\n
0x91000001 | Microsoft-Windows-HttpLog\r\n
0x91000002 | HTTP Log Channel\r\n
0x92000001 | Microsoft-Windows-HttpEvent\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Reset will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client completed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xb0000042 | Http.sys failed to process CPU hot-add. Processor number: %1, reason: %2, status: %3.\r\n
0xb0000043 | Hot-add information: Current UxNumberOfProcessors: %1, comment: %2.\r\n
0xb0000044 | Initialized QoS flow: FlowHandle %1, bandwidth %2, peak bandwidth %3, burst size %4\r\n
0xb0000046 | QoS flow initialization failed: bandwidth %1, peak bandwidth %2, burst size %3, status %4\r\n
0xb0000047 | Setting flow: Connection %1, FlowHandle %2\r\n
0xb0000048 | Assign to Configuration QoS Flow: FlowHandle %1\r\n
0xb0000049 | [re]Setting QoS Flow failed: Connection %1, FlowHandle %2, status %3\r\n
0xb000004a | Response range processing done. Req. %1, response content size %2, ranges %3 (%4-%5, %6-%7,...)\r\n
0xb000004b | Begin building slices. Req. %1, slices %2 (%3,%4,...), ranges %5 (%6-%7, %8-%9,...)\r\n
0xb000004c | Send cached slices. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004d | Cached slices match content. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004e | Merge slices to cache. CacheEntry %1, slices to merge %2, slices to cache %3\r\n
0xb000004f | Sending range from flat cache entry. CacheEntry %1, range %2-%3\r\n
0xb0000050 | Channel bind ASC parameters: connection %1, buffers %2, flags %3\r\n
0xb0000051 | Service bind check done. Connection %1, Context %2-%3, status %4, target %5\r\n
0xb0000052 | Captured channel bind config. Hardening %1, flags %2, service count %3\r\n
0xb0000053 | Channel bind response config overwrites %1\r\n
0xb0000054 | Policy-Based QoS: Connection %1, FlowHandle %2\r\n
0xb0000055 | Thread pool extension. Pool type: %1, active pools: %2.\r\n
0xb0000056 | Thread ready. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000057 | Thread pool trim. Pool type: %1, active pools: %2.\r\n
0xb0000058 | Thread gone. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000059 | SNI parsed for connection: %1 with status: %2\r\n
0xb000005a | Request %1 has initated opaque mode\r\n
0xb000005b | Endpoint auto-generated for %2\r\n
0xb000005c | Deleted auto-generated endpoint for %2\r\n
0xb000005d | Inbound connection for IP: %3, SNI: %4. SSL endpoint found: %5\r\n
0xb000005e | SSL connection with local IP address and port %2 rejected due to configuration policy.\r\n
0xb000005f | Parsing of response (response ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0010010 | Response (request pointer %1, corresponding to request ID %4, site ID %2, number of bytes %3, encoding %5) queued for sending from the cache.\r\n
0xb0010011 | Response (request pointer %1, site ID %2, number of bytes %3, encoding %5) queued for sending with status code 304 (cache not modified).\r\n
0xb0010014 | SSL credentials for endpoint %2 successfully created.\r\n
0xb0010019 | Successfully added entry (URI %1) to cache (Encoding %7).\r\n
0xb001001a | Failed to add an entry (URI %1) to the cache. Status: %2. Encoding: %3.\r\n
0xb1000001 | HTTP transaction log\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occurred while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aad | An error occurred while using SSL configuration for endpoint %2.  The error status code is contained within the returned data.\r\n
0xc0003aae | Http.sys failed to process a CPU hot-add event. Status: %2 .\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000060 | SSL handshake failed. Local IP: %2, Remote IP: %4, SNI: %5, Thumbprint: %7, Client Initiated Disconnect: %8, Abortive Disconnect: %9, Connection Status: %10\r\n
0x00000061 | HTTP error response sent. Url: %1, Verb: %2, Status Code: %3, Cache Send: %4, Request Queue: %5, PID: %6, TID: %7, Image Name: %8, Working Set(Bytes): %9, Send Status: %10, Thread Count: %11, Reason Phrase: %12, Error Cause: %13, Verbosity: %14\r\n
0x00000062 | SSL renegotiate timed out. Local IP: %2, Remote IP: %4, SNI: %5, Thumbprint: %7, Connection Buffer Full: %8\r\n
0x00000063 | HTTP 11 Required. Verb: %1, Fault Code: %2\r\n
0x0000006d | QUIC Registration Failed. Status: %1\r\n
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occurring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling SSL interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x1000000e | Flagged on all HTTP events dealing with global driver settings\r\n
0x1000000f | Flagged on all HTTP events in thread pool\r\n
0x11000001 | Flagged on all HTTP transactions\r\n
0x1100002a | Flagged on all HTTP events dealing with potential personally identifiable information\r\n
0x12000038 | Classic\r\n
0x13000034 | SQM\r\n
0x3000000b | RecvReq\r\n
0x3000000c | Parse\r\n
0x3000000d | Deliver\r\n
0x3000000e | RecvResp\r\n
0x3000000f | RecvRespLast\r\n
0x30000010 | RecvBody\r\n
0x30000011 | RecvBodyLast\r\n
0x30000012 | FastRespLast\r\n
0x30000013 | FastResp\r\n
0x30000014 | CachedAndSend\r\n
0x30000015 | FastSend\r\n
0x30000016 | ZeroSend\r\n
0x30000017 | SndError\r\n
0x30000018 | LastSndError\r\n
0x30000019 | SrvdFrmCache\r\n
0x3000001a | CachedNotModified\r\n
0x3000001b | ResvUrl\r\n
0x3000001c | ConnConnect\r\n
0x3000001d | ConnClose\r\n
0x3000001e | ConnCleanup\r\n
0x3000001f | ChgUrlGrpProp\r\n
0x30000020 | ChgSrvSesProp\r\n
0x30000021 | ChgReqQueueProp\r\n
0x30000022 | AddUrl\r\n
0x30000023 | RemUrl\r\n
0x30000024 | RemAllUrls\r\n
0x30000025 | AddedCacheEntry\r\n
0x30000026 | AddCacheEntryFailed\r\n
0x30000027 | FlushedCache\r\n
0x30000028 | SslConnEvent\r\n
0x30000029 | SslInitiateHandshake\r\n
0x3000002a | SslHandshakeComplete\r\n
0x3000002b | SslInititateSslRcvClientCert\r\n
0x3000002c | SslRcvClientCertFailed\r\n
0x3000002d | SslRcvdRawData\r\n
0x3000002e | SslDlvrdStreamData\r\n
0x3000002f | SslAcceptStreamData\r\n
0x30000031 | ReadIpListEntry\r\n
0x30000032 | CreatedSslCred\r\n
0x30000033 | SendComplete\r\n
0x30000034 | SspiCall\r\n
0x30000035 | AuthCacheEntryAdded\r\n
0x30000036 | AuthCacheEntryFreed\r\n
0x30000037 | ConnIdAssgn\r\n
0x30000038 | QosFlowSetReset\r\n
0x30000039 | LoggingConfigFailed\r\n
0x3000003a | LoggingConfig\r\n
0x3000003b | LogFileCreateFailed\r\n
0x3000003c | LogFileCreate\r\n
0x3000003d | LogFileWrite\r\n
0x3000003e | ParseRequestFailed\r\n
0x3000003f | ConnTimedOut\r\n
0x30000042 | SslEndpointCreationFailed\r\n
0x30000043 | SslDisconnEvent\r\n
0x30000044 | SslDisconnReq\r\n
0x30000045 | SslUnsealMsg\r\n
0x30000046 | SslQueryConnInfoFailed\r\n
0x30000047 | SslEndpointConfigNotFound\r\n
0x30000048 | SslAsc\r\n
0x30000049 | SslSealMsg\r\n
0x3000004a | RequestRejected\r\n
0x3000004b | RequestCancelled\r\n
0x3000004c | HotAddProcFailed\r\n
0x3000004d | HotAddProcSucceeded\r\n
0x3000004e | UserResponseFlowInit\r\n
0x3000004f | CachedResponseFlowInit\r\n
0x30000050 | FlowInitFailed\r\n
0x30000051 | SetConnectionFlow\r\n
0x30000052 | RequestAssociatedToConfigurationFlow\r\n
0x30000053 | ConnectionFlowFailed\r\n
0x30000054 | ResponseRangeProcessingOK\r\n
0x30000055 | BeginBuildingSlices\r\n
0x30000056 | SendSliceCacheContent\r\n
0x30000057 | CachedSlicesMatchContent\r\n
0x30000058 | MergeSlicesToCache\r\n
0x30000059 | FlatCacheRangeSend\r\n
0x3000005a | ChannelBindAscParams\r\n
0x3000005b | ServiceBindCheckComplete\r\n
0x3000005c | ChannelBindConfigCapture\r\n
0x3000005d | ChannelBindPerResponseConfig\r\n
0x3000005e | UsePolicyBasedQoSFlow\r\n
0x3000005f | ThreadPoolExtension\r\n
0x30000060 | ThreadReady\r\n
0x30000061 | ThreadPoolTrim\r\n
0x30000062 | ThreadGone\r\n
0x30000063 | SniParsed\r\n
0x30000064 | InitiateOpaqueMode\r\n
0x30000065 | EndpointAutoGenerated\r\n
0x30000066 | AutoGeneratedEndpointDeleted\r\n
0x30000067 | SslEndpointConfigFound\r\n
0x30000068 | SslEndpointConfigRejected\r\n
0x30000069 | SslHandshakeFailure\r\n
0x3000006a | HttpErrorResponseSent\r\n
0x3000006b | SslRenegotiateTimedOut\r\n
0x3000006c | Http11Required\r\n
0x30000073 | QuicConnection\r\n
0x30000074 | QuicConnectionCallback\r\n
0x30000075 | QuicStream\r\n
0x30000076 | QuicStreamCallback\r\n
0x30000077 | QuicRegistration\r\n
0x33000002 | Stop\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x7000000b | HTTP Driver Global Settings Task\r\n
0x7000000c | HTTP Thread Pool\r\n
0x7000000d | HTTP Response Trace Task\r\n
0x80003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0x80003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0x80003bc4 | SSL Certificate Settings deleted for endpoint : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for endpoint : %2 .\r\n
0x80003bc6 | SSL Certificate Settings updated by an admin process for endpoint : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x90000003 | System\r\n
0x91000001 | Microsoft-Windows-HttpLog\r\n
0x91000002 | HTTP Log Channel\r\n
0x92000001 | Microsoft-Windows-HttpEvent\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Reset will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client completed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xb0000042 | Http.sys failed to process CPU hot-add. Processor number: %1, reason: %2, status: %3.\r\n
0xb0000043 | Hot-add information: Current UxNumberOfProcessors: %1, comment: %2.\r\n
0xb0000044 | Initialized QoS flow: FlowHandle %1, bandwidth %2, peak bandwidth %3, burst size %4\r\n
0xb0000046 | QoS flow initialization failed: bandwidth %1, peak bandwidth %2, burst size %3, status %4\r\n
0xb0000047 | Setting flow: Connection %1, FlowHandle %2\r\n
0xb0000048 | Assign to Configuration QoS Flow: FlowHandle %1\r\n
0xb0000049 | [re]Setting QoS Flow failed: Connection %1, FlowHandle %2, status %3\r\n
0xb000004a | Response range processing done. Req. %1, response content size %2, ranges %3 (%4-%5, %6-%7,...)\r\n
0xb000004b | Begin building slices. Req. %1, slices %2 (%3,%4,...), ranges %5 (%6-%7, %8-%9,...)\r\n
0xb000004c | Send cached slices. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004d | Cached slices match content. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004e | Merge slices to cache. CacheEntry %1, slices to merge %2, slices to cache %3\r\n
0xb000004f | Sending range from flat cache entry. CacheEntry %1, range %2-%3\r\n
0xb0000050 | Channel bind ASC parameters: connection %1, buffers %2, flags %3\r\n
0xb0000051 | Service bind check done. Connection %1, Context %2-%3, status %4, target %5\r\n
0xb0000052 | Captured channel bind config. Hardening %1, flags %2, service count %3\r\n
0xb0000053 | Channel bind response config overwrites %1\r\n
0xb0000054 | Policy-Based QoS: Connection %1, FlowHandle %2\r\n
0xb0000055 | Thread pool extension. Pool type: %1, active pools: %2.\r\n
0xb0000056 | Thread ready. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000057 | Thread pool trim. Pool type: %1, active pools: %2.\r\n
0xb0000058 | Thread gone. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000059 | SNI parsed for connection: %1 with status: %2\r\n
0xb000005a | Request %1 has initated opaque mode\r\n
0xb000005b | Endpoint auto-generated for %2\r\n
0xb000005c | Deleted auto-generated endpoint for %2\r\n
0xb000005d | Inbound connection for IP: %3, SNI: %4. SSL endpoint found: %5\r\n
0xb000005e | SSL connection with local IP address and port %2 rejected due to configuration policy.\r\n
0xb000005f | Parsing of response (response ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000069 | QUIC Connection. QuicConnectionId: %1, Connection: %2, Local IP: %4, Remote IP: %6, SNI: %8, ErrorCode: %9, Status: %10\r\n
0xb000006a | QUIC Connection Callback. Connection: %1, Event: %2, EventParam: %3\r\n
0xb000006b | QUIC Stream. QuicStreamId: %1, Connection: %2, Stream: %3\r\n
0xb000006c | QUIC Stream Callback. Stream: %1, Connection: %2, StreamType: %3, Event: %4, EventParam: %5\r\n
0xb0010010 | Response (request pointer %1, corresponding to request ID %4, site ID %2, number of bytes %3, encoding %5) queued for sending from the cache.\r\n
0xb0010011 | Response (request pointer %1, site ID %2, number of bytes %3, encoding %5) queued for sending with status code 304 (cache not modified).\r\n
0xb0010014 | SSL credentials for endpoint %2 successfully created.\r\n
0xb0010019 | Successfully added entry (URI %1) to cache (Encoding %7).\r\n
0xb001001a | Failed to add an entry (URI %1) to the cache. Status: %2. Encoding: %3.\r\n
0xb1000001 | HTTP transaction log\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occurred while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aad | An error occurred while using SSL configuration for endpoint %2.  The error status code is contained within the returned data.\r\n
0xc0003aae | Http.sys failed to process a CPU hot-add event. Status: %2 .\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000060 | SSL handshake failed. Local IP: %2, Remote IP: %4, SNI: %5, Thumbprint: %7, Client Initiated Disconnect: %8, Abortive Disconnect: %9, Connection Status: %10\r\n
0x00000061 | HTTP error response sent. Url: %1, Verb: %2, Status Code: %3, Cache Send: %4, Request Queue: %5, PID: %6, TID: %7, Image Name: %8, Working Set(Bytes): %9, Send Status: %10, Thread Count: %11, Reason Phrase: %12, Error Cause: %13, Verbosity: %14\r\n
0x00000062 | SSL renegotiate timed out. Local IP: %2, Remote IP: %4, SNI: %5, Thumbprint: %7, Connection Buffer Full: %8\r\n
0x00000063 | HTTP 11 Required. Verb: %1, Fault Code: %2\r\n
0x00000064 | Version: %1 Counts: %2\r\n
0x00000065 | Version: %1 Counts: %2\r\n
0x0000006d | QUIC Registration Failed. Status: %1\r\n
0x10000001 | Flagged on all HTTP events dealing with service setup\r\n
0x10000002 | Flagged on all HTTP events dealing with request processing\r\n
0x10000003 | Flagged on all HTTP events dealing with response handling\r\n
0x10000004 | Flagged on all HTTP events dealing with endpoints\r\n
0x10000005 | Flagged on all HTTP events occurring on a connection\r\n
0x10000006 | Flagged on all HTTP events dealing with URI cache\r\n
0x10000007 | Flagged on all HTTP events triggered on a URL group\r\n
0x10000008 | Flagged on all HTTP events triggered on a server session\r\n
0x10000009 | Flagged on all HTTP events triggered on a request queue\r\n
0x1000000a | Flagged on all HTTP events handling SSL interactions\r\n
0x1000000b | Flagged on all HTTP events handling authentication (SSPI) and authentication cache\r\n
0x1000000c | Flagged on all HTTP events dealing with error log activities\r\n
0x1000000d | Flagged on all HTTP events setting/resetting/triggering timeouts\r\n
0x1000000e | Flagged on all HTTP events dealing with global driver settings\r\n
0x1000000f | Flagged on all HTTP events in thread pool\r\n
0x11000001 | Flagged on all HTTP transactions\r\n
0x1100002a | Flagged on all HTTP events dealing with potential personally identifiable information\r\n
0x12000038 | Classic\r\n
0x13000034 | SQM\r\n
0x3000000b | RecvReq\r\n
0x3000000c | Parse\r\n
0x3000000d | Deliver\r\n
0x3000000e | RecvResp\r\n
0x3000000f | RecvRespLast\r\n
0x30000010 | RecvBody\r\n
0x30000011 | RecvBodyLast\r\n
0x30000012 | FastRespLast\r\n
0x30000013 | FastResp\r\n
0x30000014 | CachedAndSend\r\n
0x30000015 | FastSend\r\n
0x30000016 | ZeroSend\r\n
0x30000017 | SndError\r\n
0x30000018 | LastSndError\r\n
0x30000019 | SrvdFrmCache\r\n
0x3000001a | CachedNotModified\r\n
0x3000001b | ResvUrl\r\n
0x3000001c | ConnConnect\r\n
0x3000001d | ConnClose\r\n
0x3000001e | ConnCleanup\r\n
0x3000001f | ChgUrlGrpProp\r\n
0x30000020 | ChgSrvSesProp\r\n
0x30000021 | ChgReqQueueProp\r\n
0x30000022 | AddUrl\r\n
0x30000023 | RemUrl\r\n
0x30000024 | RemAllUrls\r\n
0x30000025 | AddedCacheEntry\r\n
0x30000026 | AddCacheEntryFailed\r\n
0x30000027 | FlushedCache\r\n
0x30000028 | SslConnEvent\r\n
0x30000029 | SslInitiateHandshake\r\n
0x3000002a | SslHandshakeComplete\r\n
0x3000002b | SslInititateSslRcvClientCert\r\n
0x3000002c | SslRcvClientCertFailed\r\n
0x3000002d | SslRcvdRawData\r\n
0x3000002e | SslDlvrdStreamData\r\n
0x3000002f | SslAcceptStreamData\r\n
0x30000031 | ReadIpListEntry\r\n
0x30000032 | CreatedSslCred\r\n
0x30000033 | SendComplete\r\n
0x30000034 | SspiCall\r\n
0x30000035 | AuthCacheEntryAdded\r\n
0x30000036 | AuthCacheEntryFreed\r\n
0x30000037 | ConnIdAssgn\r\n
0x30000038 | QosFlowSetReset\r\n
0x30000039 | LoggingConfigFailed\r\n
0x3000003a | LoggingConfig\r\n
0x3000003b | LogFileCreateFailed\r\n
0x3000003c | LogFileCreate\r\n
0x3000003d | LogFileWrite\r\n
0x3000003e | ParseRequestFailed\r\n
0x3000003f | ConnTimedOut\r\n
0x30000042 | SslEndpointCreationFailed\r\n
0x30000043 | SslDisconnEvent\r\n
0x30000044 | SslDisconnReq\r\n
0x30000045 | SslUnsealMsg\r\n
0x30000046 | SslQueryConnInfoFailed\r\n
0x30000047 | SslEndpointConfigNotFound\r\n
0x30000048 | SslAsc\r\n
0x30000049 | SslSealMsg\r\n
0x3000004a | RequestRejected\r\n
0x3000004b | RequestCancelled\r\n
0x3000004c | HotAddProcFailed\r\n
0x3000004d | HotAddProcSucceeded\r\n
0x3000004e | UserResponseFlowInit\r\n
0x3000004f | CachedResponseFlowInit\r\n
0x30000050 | FlowInitFailed\r\n
0x30000051 | SetConnectionFlow\r\n
0x30000052 | RequestAssociatedToConfigurationFlow\r\n
0x30000053 | ConnectionFlowFailed\r\n
0x30000054 | ResponseRangeProcessingOK\r\n
0x30000055 | BeginBuildingSlices\r\n
0x30000056 | SendSliceCacheContent\r\n
0x30000057 | CachedSlicesMatchContent\r\n
0x30000058 | MergeSlicesToCache\r\n
0x30000059 | FlatCacheRangeSend\r\n
0x3000005a | ChannelBindAscParams\r\n
0x3000005b | ServiceBindCheckComplete\r\n
0x3000005c | ChannelBindConfigCapture\r\n
0x3000005d | ChannelBindPerResponseConfig\r\n
0x3000005e | UsePolicyBasedQoSFlow\r\n
0x3000005f | ThreadPoolExtension\r\n
0x30000060 | ThreadReady\r\n
0x30000061 | ThreadPoolTrim\r\n
0x30000062 | ThreadGone\r\n
0x30000063 | SniParsed\r\n
0x30000064 | InitiateOpaqueMode\r\n
0x30000065 | EndpointAutoGenerated\r\n
0x30000066 | AutoGeneratedEndpointDeleted\r\n
0x30000067 | SslEndpointConfigFound\r\n
0x30000068 | SslEndpointConfigRejected\r\n
0x30000069 | SslHandshakeFailure\r\n
0x3000006a | HttpErrorResponseSent\r\n
0x3000006b | SslRenegotiateTimedOut\r\n
0x3000006c | Http11Required\r\n
0x3000006d | QuicCounts\r\n
0x3000006e | WskCounts\r\n
0x30000073 | QuicConnection\r\n
0x30000074 | QuicConnectionCallback\r\n
0x30000075 | QuicStream\r\n
0x30000076 | QuicStreamCallback\r\n
0x30000077 | QuicRegistration\r\n
0x30000078 | ClientCorrelation\r\n
0x33000002 | Stop\r\n
0x40003a9f | Reservation for namespace identified by URL prefix %2 was successfully added.\r\n
0x40003aa0 | Reservation for namespace identified by URL prefix %2 was successfully deleted.\r\n
0x40003aa7 | Unable to convert all entries on IP Listen-Only list.  Driver will listen on all available interfaces.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | HTTP Request Trace Task\r\n
0x70000003 | HTTP Setup Trace Task\r\n
0x70000004 | HTTP Connection Trace Task\r\n
0x70000005 | HTTP Configuration Property Trace Task\r\n
0x70000006 | HTTP Authentication Trace Task\r\n
0x70000007 | HTTP SSL Trace Task\r\n
0x70000008 | HTTP Cache Trace Task\r\n
0x70000009 | HTTP Logging Trace Task\r\n
0x7000000a | HTTP Timeout Trace Task\r\n
0x7000000b | HTTP Driver Global Settings Task\r\n
0x7000000c | HTTP Thread Pool\r\n
0x7000000d | HTTP Response Trace Task\r\n
0x80003aab | The host %2 has gone down as a result of the change in the IP Listen-Only list.\r\n
0x80003aac | The host %2 has come up as a result of the change in the IP Listen-Only list.\r\n
0x80003bc4 | SSL Certificate Settings deleted for endpoint : %2 .\r\n
0x80003bc5 | SSL Certificate Settings created by an admin process for endpoint : %2 .\r\n
0x80003bc6 | SSL Certificate Settings updated by an admin process for endpoint : %2 .\r\n
0x90000001 | Microsoft-Windows-HttpService\r\n
0x90000002 | HTTP Service Channel\r\n
0x90000003 | System\r\n
0x91000001 | Microsoft-Windows-HttpLog\r\n
0x91000002 | HTTP Log Channel\r\n
0x92000001 | Microsoft-Windows-HttpEvent\r\n
0xb0000001 | Request received (request ID %1) on connection (connection ID %2) from remote address %4.\r\n
0xb0000002 | Parsed request (request pointer %1, method %2) with URI %3.\r\n
0xb0000003 | Delivered request to server application (request pointer %1, request ID %2, site ID %3) from request queue %4 for URI %5 with status %6.\r\n
0xb0000004 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000005 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb0000006 | Server application passed entity body for request ID %1 (connection ID %2).\r\n
0xb0000007 | Server application passed the last entity body for request ID %1.\r\n
0xb0000008 | Server application passed response (request ID %1, connection ID %2, method %4, header length %5, number of entity chunks %6, cache policy %7) with status code %3.\r\n
0xb0000009 | Server application passed the last response (corresponding to request ID %1).\r\n
0xb000000a | Response ready for send (corresponding to request ID %1) with status code %2.\r\n
0xb000000b | Cached the response (corresponding to request ID %1) with status code %2. Response to be sent.\r\n
0xb000000c | Queued last response (corresponding to request ID %1) for sending. Status code is %2.\r\n
0xb000000d | Response sent (corresponding to request ID %1) with status code %2. If disconnect is required, a TCP FIN has been sent.\r\n
0xb000000e | Error occurred while sending the last response (corresponding to request ID %1) with status code %2. A TCP Reset has been sent.\r\n
0xb000000f | Error %3 occurred while sending (corresponding to request ID %1). A TCP Reset will be sent.\r\n
0xb0000010 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending from the cache.\r\n
0xb0000011 | Response (request pointer %1, site ID %2, number of bytes %3) queued for sending with status code 304 (cache not modified).\r\n
0xb0000012 | Attempted to reserve URL (%1). Status %2.\r\n
0xb0000013 | Successfully read the IP listen list for IP address %1.\r\n
0xb0000014 | SSL credentials for IP address and port %3 successfully created.\r\n
0xb0000015 | New connection created (local IP address %3 and remote address %5).\r\n
0xb0000016 | Connection ID (%2) assigned to connection and request (request ID %1) will be parsed.\r\n
0xb0000017 | Client closed the connection (connection pointer %1). Status of whether closed by TCP Reset: %2.\r\n
0xb0000018 | Connection (connection pointer %1) cleanup started due to either the sending of a TCP Reset, receiving of a TCP Reset, or after the mutual exchange of TCP Fins.\r\n
0xb0000019 | Successfully added entry (URI %1) to cache.\r\n
0xb000001a | Failed to add an entry (URI %1) to the cache. Status: %2.\r\n
0xb000001b | Flushed entry (URI %1) from the cache.\r\n
0xb000001c | Attempted to set URL group property: %1. Status: %2.\r\n
0xb000001d | Attempted to set server session property: %1. Status: %2.\r\n
0xb000001e | Attempted to set request queue property: %1. Status: %2.\r\n
0xb000001f | Attempted to add URL (%2) to URL group (%1). Status: %3.\r\n
0xb0000020 | Removed URL (%2) from URL group (%1).\r\n
0xb0000021 | Removed all URLs from URL group %1.\r\n
0xb0000022 | Initiating SSL connection.\r\n
0xb0000023 | Initiating SSL handshake.\r\n
0xb0000024 | SSL handshake completed with status: %1.\r\n
0xb0000025 | Server application is attempting to receive the SSL client certificate, which will be provided if available. If the client certificate is not available, a renegotiation will be initiated.\r\n
0xb0000026 | Attempt by server application to receive client certificate failed with status: %1.\r\n
0xb0000027 | Raw SSL data is available for processing.\r\n
0xb0000028 | Decrypted SSL data is available for processing.\r\n
0xb0000029 | Passed plaintext data for encryption.\r\n
0xb000002b | Attempt (on connection ID %1) to authenticate client completed. Authentication type %2. Security status: %3.\r\n
0xb000002c | Attempted to add entry to the %2 authentication cache. Status: %4.\r\n
0xb000002d | Entry successfully removed from the authentication cache.\r\n
0xb000002e | Successfully associated QoS flow with connection (connection ID %1). Bandwidth throttled to: %2 Bytes per second.\r\n
0xb000002f | Failed to configure the %2 logging (directory %4), Status: %1.\r\n
0xb0000030 | Successfully configured %2 logging (directory %5).\r\n
0xb0000031 | Failed to create %2 log file %5. Status: %1.\r\n
0xb0000032 | Successfully created new %2 log file %5.\r\n
0xb0000033 | Entry has been written to %3 log file.\r\n
0xb0000034 | Parsing of request (request ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000035 | HTTP timer %3 expired. The connection will be reset.\r\n
0xb0000038 | Failed to acquire handle for SSL credentials. Failure will be event logged. Security status: %2.\r\n
0xb0000039 | SSL connection will be disconnected as initiated by the client.\r\n
0xb000003a | SSL connection will be disconnected as initiated by the server application. Status: %2.\r\n
0xb000003b | Attempt to decrypt SSL data failed. Security status: %2.\r\n
0xb000003c | Query for SSL connection parameters failed. Security status: %2. Connection will be reset.\r\n
0xb000003d | Cannot find SSL endpoint for inbound connection for local IP address and port %3.\r\n
0xb000003e | Attempt to perform SSL handshake failed. Security status: %2.\r\n
0xb000003f | Attempt to encrypt SSL data failed. Security status: %2.\r\n
0xb0000040 | Request (request ID %1) rejected due to reason: %2.\r\n
0xb0000041 | Server application canceled the processing of its request (request ID %1).\r\n
0xb0000042 | Http.sys failed to process CPU hot-add. Processor number: %1, reason: %2, status: %3.\r\n
0xb0000043 | Hot-add information: Current UxNumberOfProcessors: %1, comment: %2.\r\n
0xb0000044 | Initialized QoS flow: FlowHandle %1, bandwidth %2, peak bandwidth %3, burst size %4\r\n
0xb0000046 | QoS flow initialization failed: bandwidth %1, peak bandwidth %2, burst size %3, status %4\r\n
0xb0000047 | Setting flow: Connection %1, FlowHandle %2\r\n
0xb0000048 | Assign to Configuration QoS Flow: FlowHandle %1\r\n
0xb0000049 | [re]Setting QoS Flow failed: Connection %1, FlowHandle %2, status %3\r\n
0xb000004a | Response range processing done. Req. %1, response content size %2, ranges %3 (%4-%5, %6-%7,...)\r\n
0xb000004b | Begin building slices. Req. %1, slices %2 (%3,%4,...), ranges %5 (%6-%7, %8-%9,...)\r\n
0xb000004c | Send cached slices. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004d | Cached slices match content. Req. %1, CacheEntry %2, slices %3 (%4,%5,...), ranges %6 (%7-%8, %9-%10,...)\r\n
0xb000004e | Merge slices to cache. CacheEntry %1, slices to merge %2, slices to cache %3\r\n
0xb000004f | Sending range from flat cache entry. CacheEntry %1, range %2-%3\r\n
0xb0000050 | Channel bind ASC parameters: connection %1, buffers %2, flags %3\r\n
0xb0000051 | Service bind check done. Connection %1, Context %2-%3, status %4, target %5\r\n
0xb0000052 | Captured channel bind config. Hardening %1, flags %2, service count %3\r\n
0xb0000053 | Channel bind response config overwrites %1\r\n
0xb0000054 | Policy-Based QoS: Connection %1, FlowHandle %2\r\n
0xb0000055 | Thread pool extension. Pool type: %1, active pools: %2.\r\n
0xb0000056 | Thread ready. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000057 | Thread pool trim. Pool type: %1, active pools: %2.\r\n
0xb0000058 | Thread gone. Pool type: %1, active pools: %2, thread count: %3\r\n
0xb0000059 | SNI parsed for connection: %1 with status: %2\r\n
0xb000005a | Request %1 has initated opaque mode\r\n
0xb000005b | Endpoint auto-generated for %2\r\n
0xb000005c | Deleted auto-generated endpoint for %2\r\n
0xb000005d | Inbound connection for IP: %3, SNI: %4. SSL endpoint found: %5\r\n
0xb000005e | SSL connection with local IP address and port %2 rejected due to configuration policy.\r\n
0xb000005f | Parsing of response (response ID %2) failed due to reason: %3. Request may not be compliant with HTTP/1.1.\r\n
0xb0000069 | QUIC Connection. QuicConnectionId: %1, Connection: %2, Local IP: %4, Remote IP: %6, SNI: %8, ErrorCode: %9, Status: %10\r\n
0xb000006a | QUIC Connection Callback. Connection: %1, Event: %2, EventParam: %3\r\n
0xb000006b | QUIC Stream. QuicStreamId: %1, Connection: %2, Stream: %3\r\n
0xb000006c | QUIC Stream Callback. Stream: %1, Connection: %2, StreamType: %3, Event: %4, EventParam: %5\r\n
0xb000006e | Correlation ID for request %1: %2\r\n
0xb0010010 | Response (request pointer %1, corresponding to request ID %4, site ID %2, number of bytes %3, encoding %5) queued for sending from the cache.\r\n
0xb0010011 | Response (request pointer %1, site ID %2, number of bytes %3, encoding %5) queued for sending with status code 304 (cache not modified).\r\n
0xb0010014 | SSL credentials for endpoint %2 successfully created.\r\n
0xb0010019 | Successfully added entry (URI %1) to cache (Encoding %7).\r\n
0xb001001a | Failed to add an entry (URI %1) to the cache. Status: %2. Encoding: %3.\r\n
0xb1000001 | HTTP transaction log\r\n
0xc0003a98 | Unable to create log file %2. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a99 | Unable to create the log file for site W3SVC%2. Make sure that the logging directory for the site is correct and this computer has write access to that directory.\r\n
0xc0003a9a | Unable to write to the log file %2 for site W3SVC%3. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9b | Unable to create the centralized binary log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003a9c | Unable to write to the centralized binary log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003a9d | Unable to bind to the underlying transport for %2. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.\r\n
0xc0003a9e | Owner of the log file or directory %2 is invalid. This could be because another user has already created the log file or the directory.\r\n
0xc0003aa1 | An error occurred while initializing namespace reservations.  The error status code is contained within the returned data.\r\n
0xc0003aa2 | An error occured while initializing namespace reservation identified by URL prefix %2.  The error status code is contained within the returned data.\r\n
0xc0003aa3 | Unable to create the error log file. Make sure that the error logging directory is correct.\r\n
0xc0003aa4 | Unable to write to the error log file. Disk may be full. The data field contains the error number.\r\n
0xc0003aa5 | Error logging configuration failed. The data field contains the error number.\r\n
0xc0003aa6 | Unable to convert IP Listen-Only list entry %2.  The data field contains the error number.\r\n
0xc0003aa8 | Unable to initialize the security package %2 for server side authentication.  The data field contains the error number.\r\n
0xc0003aa9 | Unable to create the centralized W3C log file. Make sure that the logging directory is correct and this computer has write access to that directory.\r\n
0xc0003aaa | Unable to write to the centralized W3C log file %2. Disk may be full. If this is a network path, make sure that network connectivity is not broken.\r\n
0xc0003aad | An error occurred while using SSL configuration for endpoint %2.  The error status code is contained within the returned data.\r\n
0xc0003aae | Http.sys failed to process a CPU hot-add event. Status: %2 .\r\n
0xd0000001 | W3C\r\n
0xd0000002 | IIS\r\n
0xd0000003 | NCSA\r\n
0xd0000004 | Binary\r\n
0xd0000005 | Site\r\n
0xd0000006 | Centralized\r\n
0xd0000007 | ResponseLogging\r\n
0xd0000008 | ErrorLogging\r\n
