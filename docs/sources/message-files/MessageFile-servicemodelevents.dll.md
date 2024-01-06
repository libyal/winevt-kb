## servicemodelevents.dll

Path: %SystemRoot%\Microsoft.NET\Framework64\v4.0.30319\ServiceModelEvents.dll

### 3.0.4506.25, 3.0.4506.4926, 4.0.30319.1

Message identifier | Message string
--- | ---
0x00000001 | ServiceAuthorization\r\n
0x00000002 | MessageAuthentication\r\n
0x00000003 | ObjectAccess\r\n
0x00000004 | Tracing\r\n
0x00000005 | WebHost\r\n
0x00000006 | FailFast\r\n
0x00000007 | Message Logging\r\n
0x00000008 | Performance Counter\r\n
0x00000009 | WMI\r\n
0x0000000a | COM+\r\n
0x0000000b | State Machine\r\n
0x0000000c | WS-AT\r\n
0x0000000d | Sharing Service\r\n
0x0000000e | Listener Adapter\r\n
0x40060001 | Service authorization succeeded.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nAuthorizationContext: %4%n\r\nActivityId: %5%n\r\nServiceAuthorizationManager: %6\r\n
0x40060003 | Message authentication succeeded.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nActivityId: %4\r\n
0x40060005 | Security negotiation succeeded.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nActivityId: %4%n\r\nNegotiation: %5\r\n
0x40060007 | Transport authentication succeeded.%n\r\nService: %1%n\r\nClientIdentity: %2%n\r\nActivityId: %3%n\r\n
0x40060009 | Impersonation succeeded.%n\r\nMethodName: %1%n\r\nClientIdentity: %2%n\r\nActivityId: %3\r\n
0xc0010064 | Tracing was not set up. Tracing will be disabled.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0010065 | The trace source was not initialized. Tracing will be disabled.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0010066 | FailFast was invoked.%r\r\nMessage: %1%r\r\nStack Trace: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0010067 | An exception was thrown during FailFast.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0010068 | An event or events were not traced.%r\r\nOriginal event string: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0010069 | An event or events were not traced.%r\r\nOriginal event string:%r\r\n%1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc001006a | An invariant assertion is false.%r\r\nMessage: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc001006b | PII logging has been turned on. Sensitive information will be logged in the clear.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc001006c | No known PII is being logged: logging of known PII is not allowed. To allow logging of known PII, please set "enableLoggingKnownPii" to true in machine.config.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc0020001 | A Webhost unhandled exception occurred.%r\r\nSender Information: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020002 | A WebHost HTTP exception occurred.%r\r\nSender Information: %1%r\r\nHtmlErrorMessage:%r\r\n%2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020003 | WebHost failed to process a request.%r\r\nSender Information: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020004 | An error occurred while trying to listen for the URL '%1'. This worker process will be terminated.%r\r\nSender Information: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020005 | A message was not logged.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020006 | A bad message logging filter that was accessing the message body was removed.%r\r\nXPath:%r\r\n%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020007 | Message logging failed to create the trace source.%r\r\nException:%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020008 | Message Logging has been turned on. Sensitive information may be logged in the clear, even if it was encrypted on the wire: for example, message bodies.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc0020009 | Message logging has been turned off.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc002000a | A performance counter was not loaded.%r\r\nCategory Name: %1%r\r\nCounter Name: %2%r\r\nException:%3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc002000b | A performance counter was not removed.%r\r\nCategory Name: %1%r\r\nCounter Name: %2%r\r\nInstance Name: %3%r\r\nException:%4%r\r\nProcess Name: %5%r\r\nProcess ID: %6%r\r\n
0xc002000c | The WMI GetObject request was not processed.%r\r\nWMI Object: %1%r\r\nException:%2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc002000d | The WMI PutInstance request was not processed.%r\r\nWMI Object: %1%r\r\nException:%2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc002000e | The WMI DeleteInstance request was not processed.%r\r\nException:%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc002000f | The WMI CreateInstance request was not processed.%r\r\nClass name: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020010 | The WMI ExecQuery request was not processed.%r\r\nException:%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020011 | The WMI ExecMethod request was not processed.%r\r\nException:%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020012 | The WMI provider was not registered.%r\r\nWMI Object: %1%r\r\nError:%2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020013 | The WMI provider was not unregistered.%r\r\nWMI Object: %1%r\r\nError:%2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020014 | Type mismatch: CIM class %1 property %2 cannot accept value of type %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020015 | Type mismatch: CIM class %1 does not have property %2 of type %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020016 | COM+: An error occurred while starting the service.%r\r\nAppId: %1%r\r\nClsId: %2%r\r\nSurrogate: %3%r\r\nException: %4%r\r\nProcess Name: %5%r\r\nProcess ID: %6%r\r\n
0xc0020017 | COM+: An error occurred while starting the DllHost initializer.%r\r\nAppId: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020018 | COM+: An error occurred while importing the type library.%r\r\nIID: %1%r\r\nType library ID: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020019 | COM+: A method call failed.%r\r\nFrom: %1%r\r\nApp ID: %2%r\r\nCLSID: %3%r\r\nIID: %4%r\r\nAction: %5%r\r\nSurrogate: %6%r\r\nInstance ID: %7%r\r\nManaged Thread ID: %8%r\r\nUnmanaged Thread ID: %9%r\r\nCaller Identity: %10%r\r\nException: %11%r\r\nProcess Name: %12%r\r\nProcess ID: %13%r\r\n
0xc002001a | COM+:An error occurred while creating a COM instance.%r\r\nFrom: %1%r\r\nApp ID: %2%r\r\nCLSID: %3%r\r\nIncoming Transaction ID: %4%r\r\nSurrogate: %5%r\r\nRequesting Identity: %6%r\r\nException: %7%r\r\nProcess Name: %8%r\r\nProcess ID: %9%r\r\n
0xc002001b | ComPlus:Method call transaction mismatch.%r\r\nIncoming Transaction ID: %1%r\r\nCurrent Transaction ID: %2%r\r\nFrom: %3%r\r\nApp ID: %4%r\r\nCLSID: %5%r\r\nIID: %6%r\r\nAction: %7%r\r\nSurrogate: %8%r\r\nInstance ID: %9%r\r\nManaged Thread ID: %10%r\r\nUnmanaged Thread ID: %11%r\r\nCaller Identity: %12%r\r\nException: %13%r\r\nProcess Name: %14%r\r\nProcess ID: %15%r\r\n
0xc0030001 | An unhandled exception was thrown while a state machine was processing an event.%r\r\nTransaction ID: %1%r\r\nState machine name: %2%r\r\nCurrent state: %3%r\r\nHistory: %4%r\r\nEnlistment ID: %5%r\r\nException: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc0030002 | A state machine attempted to process an unexpected event. The event was considered fatal.%r\r\nTransaction ID: %1%r\r\nState machine name: %2%r\r\nCurrent state: %3%r\r\nHistory: %4%r\r\nEvent name: %5%r\r\nEvent details: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc0030003 | A participant recovery log entry was corrupt and could not be deserialized. Data loss may result from this error.%r\r\nTransaction ID: %1%r\r\nRecovery data (Base64 encoded): %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030004 | A coordinator recovery log entry was corrupt and could not be deserialized. Data loss may result from this error.%r\r\nTransaction ID: %1%r\r\nRecovery data (Base64 encoded): %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030005 | A recovery log entry could not be generated for the coordinator enlistment. The transaction will be aborted.%r\r\nTransaction ID: %1%r\r\nReason: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030006 | A recovery log entry could not be generated for a participant enlistment. The transaction will be aborted.%r\r\nTransaction ID: %1%r\r\nEnlistment ID: %2%r\r\nReason: %3%r\r\nException: %4%r\r\nProcess Name: %5%r\r\nProcess ID: %6%r\r\n
0xc0030007 | The WS-AT protocol service failed to initialize. As a result, WS-AT functionality will be disabled.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030008 | The WS-AT protocol service failed to start. As a result, WS-AT functionality will be disabled.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030009 | The MSDTC WS-AT protocol failed at the beginning of recovery. As a result, WS-AT functionality will be disabled.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc003000a | The WS-AT protocol service failed to complete startup and recovery. As a result, WS-AT functionality will be disabled.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc003000b | The MSDTC TransactionBridge failed during recovery. This is a fatal condition, so the MSDTC service was terminated.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc003000c | The WS-AT protocol service failed to stop.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc003000d | A state machine attempted to process an unexpected event. The event was not considered fatal.%r\r\nTransaction ID: %1%r\r\nState machine: %2%r\r\nCurrent state: %3%r\r\nHistory: %4%r\r\nEvent name: %5%r\r\nEvent details: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc003000e | A performance counter failed to initialize.%r\r\nCounter name: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc003000f | The WS-AT protocol service successfully completed startup and recovery.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0030010 | The WS-AT protocol service was stopped.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0030011 | Identity certificate with thumbprint '%1' could not be found.%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0030012 | Identity certificate with thumbprint '%1' could not be validated.%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0030013 | Identity certificate with subject name '%1' and thumbprint '%2' does not have a private key.\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0030014 | Identity certificate with subject name '%1' and thumbprint '%2' does not have an accessible private key.\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0030015 | Identity certificate with subject name '%1' and thumbprint '%2' does not provide '%3' among its KeyUsages.\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030016 | Identity certificate with subject name '%1' and thumbprint '%2' does not provide '%3' among its EnhancedKeyUsages.\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0040001 | The NT service failed to start; the listening endpoint could not be published.%r\r\nError Code: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0040002 | An error occurred while parsing the %1 binding '%2' of the site '%3', thus the protocol is disabled for the site temporarily. See the exception message for more details.%r\r\nBinding: %4%r\r\nSource: %5%r\r\nException: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc0040003 | An error occurred in the Activation Service '%1' of the protocol '%2' while trying to listen for the site '%3', thus the protocol is disabled for the site temporarily. See the exception message for more details.%r\r\nURL: %4%r\r\nStatus: %5%r\r\nException: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc0040004 | An unexpected error occurred in the listener adapter while handling a WAS notification. The process will be terminated.%r\r\nProtocol: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0040005 | WAS was disconnected.%r\r\nHRESULT: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0040006 | A connection that WAS depends on timed out.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc0040007 | A request to start the service failed.%r\r\nError Code: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0040008 | An error occurred while dispatching a duplicated socket: this handle is now leaked in the process.%r\r\nID: %1%r\r\nSource: %2%r\r\nException: %3%r \r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0040009 | An error occurred while dispatching a duplicated named pipe: this handle is now leaked in the process.%r\r\nSource: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0060002 | Service authorization failed.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nAuthorizationContext: %4%n\r\nActivityId: %5%n\r\nServiceAuthorizationManager: %6%n\r\n%7\r\n
0xc0060004 | Message authentication failed.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nActivityId: %4%n\r\n%5\r\n
0xc0060006 | Security negotiation failed.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nActivityId: %4%n\r\nNegotiation: %5%n\r\n%6\r\n
0xc0060008 | Transport authentication failed.%n\r\nService: %1%n\r\nClientIdentity: %2%n\r\nActivityId: %3%n\r\n%4\r\n
0xc006000a | Impersonation failed.%n\r\nMethodName: %1%n\r\nClientIdentity: %2%n\r\nActivityId: %3%n\r\n%4\r\n

### 4.0.30319.17929, 4.0.30319.33440, 4.6.1038.0, 4.6.1586.0, 4.7.2046.0, 4.7.2053.0, 4.7.2556.0, 4.7.3056.0, 4.7.3190.0, 4.8.3752.0, 4.8.4084.0, 4.8.4161.0

Message identifier | Message string
--- | ---
0x00000001 | ServiceAuthorization\r\n
0x00000002 | MessageAuthentication\r\n
0x00000003 | ObjectAccess\r\n
0x00000004 | Tracing\r\n
0x00000005 | WebHost\r\n
0x00000006 | FailFast\r\n
0x00000007 | Message Logging\r\n
0x00000008 | Performance Counter\r\n
0x00000009 | WMI\r\n
0x0000000a | COM+\r\n
0x0000000b | State Machine\r\n
0x0000000c | WS-AT\r\n
0x0000000d | Sharing Service\r\n
0x0000000e | Listener Adapter\r\n
0x40060001 | Service authorization succeeded.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nAuthorizationContext: %4%n\r\nActivityId: %5%n\r\nServiceAuthorizationManager: %6\r\n
0x40060003 | Message authentication succeeded.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nActivityId: %4\r\n
0x40060005 | Security negotiation succeeded.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nActivityId: %4%n\r\nNegotiation: %5\r\n
0x40060007 | Transport authentication succeeded.%n\r\nService: %1%n\r\nClientIdentity: %2%n\r\nActivityId: %3%n\r\n
0x40060009 | Impersonation succeeded.%n\r\nMethodName: %1%n\r\nClientIdentity: %2%n\r\nActivityId: %3\r\n
0x8002001c | %1%r\r\nSender Information: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0010064 | Tracing was not set up. Tracing will be disabled.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0010065 | The trace source was not initialized. Tracing will be disabled.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0010066 | FailFast was invoked.%r\r\nMessage: %1%r\r\nStack Trace: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0010067 | An exception was thrown during FailFast.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0010068 | An event or events were not traced.%r\r\nOriginal event string: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0010069 | An event or events were not traced.%r\r\nOriginal event string:%r\r\n%1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc001006a | An invariant assertion is false.%r\r\nMessage: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc001006b | PII logging has been turned on. Sensitive information will be logged in the clear.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc001006c | No known PII is being logged: logging of known PII is not allowed. To allow logging of known PII, please set "enableLoggingKnownPii" to true in machine.config.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc0020001 | A Webhost unhandled exception occurred.%r\r\nSender Information: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020002 | A WebHost HTTP exception occurred.%r\r\nSender Information: %1%r\r\nHtmlErrorMessage:%r\r\n%2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020003 | WebHost failed to process a request.%r\r\nSender Information: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020004 | An error occurred while trying to listen for the URL '%1'. This worker process will be terminated.%r\r\nSender Information: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020005 | A message was not logged.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020006 | A bad message logging filter that was accessing the message body was removed.%r\r\nXPath:%r\r\n%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020007 | Message logging failed to create the trace source.%r\r\nException:%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020008 | Message Logging has been turned on. Sensitive information may be logged in the clear, even if it was encrypted on the wire: for example, message bodies.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc0020009 | Message logging has been turned off.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc002000a | A performance counter was not loaded.%r\r\nCategory Name: %1%r\r\nCounter Name: %2%r\r\nException:%3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc002000b | A performance counter was not removed.%r\r\nCategory Name: %1%r\r\nCounter Name: %2%r\r\nInstance Name: %3%r\r\nException:%4%r\r\nProcess Name: %5%r\r\nProcess ID: %6%r\r\n
0xc002000c | The WMI GetObject request was not processed.%r\r\nWMI Object: %1%r\r\nException:%2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc002000d | The WMI PutInstance request was not processed.%r\r\nWMI Object: %1%r\r\nException:%2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc002000e | The WMI DeleteInstance request was not processed.%r\r\nException:%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc002000f | The WMI CreateInstance request was not processed.%r\r\nClass name: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020010 | The WMI ExecQuery request was not processed.%r\r\nException:%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020011 | The WMI ExecMethod request was not processed.%r\r\nException:%1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0020012 | The WMI provider was not registered.%r\r\nWMI Object: %1%r\r\nError:%2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020013 | The WMI provider was not unregistered.%r\r\nWMI Object: %1%r\r\nError:%2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020014 | Type mismatch: CIM class %1 property %2 cannot accept value of type %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020015 | Type mismatch: CIM class %1 does not have property %2 of type %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020016 | COM+: An error occurred while starting the service.%r\r\nAppId: %1%r\r\nClsId: %2%r\r\nSurrogate: %3%r\r\nException: %4%r\r\nProcess Name: %5%r\r\nProcess ID: %6%r\r\n
0xc0020017 | COM+: An error occurred while starting the DllHost initializer.%r\r\nAppId: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0020018 | COM+: An error occurred while importing the type library.%r\r\nIID: %1%r\r\nType library ID: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0020019 | COM+: A method call failed.%r\r\nFrom: %1%r\r\nApp ID: %2%r\r\nCLSID: %3%r\r\nIID: %4%r\r\nAction: %5%r\r\nSurrogate: %6%r\r\nInstance ID: %7%r\r\nManaged Thread ID: %8%r\r\nUnmanaged Thread ID: %9%r\r\nCaller Identity: %10%r\r\nException: %11%r\r\nProcess Name: %12%r\r\nProcess ID: %13%r\r\n
0xc002001a | COM+:An error occurred while creating a COM instance.%r\r\nFrom: %1%r\r\nApp ID: %2%r\r\nCLSID: %3%r\r\nIncoming Transaction ID: %4%r\r\nSurrogate: %5%r\r\nRequesting Identity: %6%r\r\nException: %7%r\r\nProcess Name: %8%r\r\nProcess ID: %9%r\r\n
0xc002001b | ComPlus:Method call transaction mismatch.%r\r\nIncoming Transaction ID: %1%r\r\nCurrent Transaction ID: %2%r\r\nFrom: %3%r\r\nApp ID: %4%r\r\nCLSID: %5%r\r\nIID: %6%r\r\nAction: %7%r\r\nSurrogate: %8%r\r\nInstance ID: %9%r\r\nManaged Thread ID: %10%r\r\nUnmanaged Thread ID: %11%r\r\nCaller Identity: %12%r\r\nException: %13%r\r\nProcess Name: %14%r\r\nProcess ID: %15%r\r\n
0xc0030001 | An unhandled exception was thrown while a state machine was processing an event.%r\r\nTransaction ID: %1%r\r\nState machine name: %2%r\r\nCurrent state: %3%r\r\nHistory: %4%r\r\nEnlistment ID: %5%r\r\nException: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc0030002 | A state machine attempted to process an unexpected event. The event was considered fatal.%r\r\nTransaction ID: %1%r\r\nState machine name: %2%r\r\nCurrent state: %3%r\r\nHistory: %4%r\r\nEvent name: %5%r\r\nEvent details: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc0030003 | A participant recovery log entry was corrupt and could not be deserialized. Data loss may result from this error.%r\r\nTransaction ID: %1%r\r\nRecovery data (Base64 encoded): %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030004 | A coordinator recovery log entry was corrupt and could not be deserialized. Data loss may result from this error.%r\r\nTransaction ID: %1%r\r\nRecovery data (Base64 encoded): %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030005 | A recovery log entry could not be generated for the coordinator enlistment. The transaction will be aborted.%r\r\nTransaction ID: %1%r\r\nReason: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030006 | A recovery log entry could not be generated for a participant enlistment. The transaction will be aborted.%r\r\nTransaction ID: %1%r\r\nEnlistment ID: %2%r\r\nReason: %3%r\r\nException: %4%r\r\nProcess Name: %5%r\r\nProcess ID: %6%r\r\n
0xc0030007 | The WS-AT protocol service failed to initialize. As a result, WS-AT functionality will be disabled.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030008 | The WS-AT protocol service failed to start. As a result, WS-AT functionality will be disabled.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030009 | The MSDTC WS-AT protocol failed at the beginning of recovery. As a result, WS-AT functionality will be disabled.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc003000a | The WS-AT protocol service failed to complete startup and recovery. As a result, WS-AT functionality will be disabled.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc003000b | The MSDTC TransactionBridge failed during recovery. This is a fatal condition, so the MSDTC service was terminated.%r\r\nException: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc003000c | The WS-AT protocol service failed to stop.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nException: %3%r\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc003000d | A state machine attempted to process an unexpected event. The event was not considered fatal.%r\r\nTransaction ID: %1%r\r\nState machine: %2%r\r\nCurrent state: %3%r\r\nHistory: %4%r\r\nEvent name: %5%r\r\nEvent details: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc003000e | A performance counter failed to initialize.%r\r\nCounter name: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc003000f | The WS-AT protocol service successfully completed startup and recovery.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0030010 | The WS-AT protocol service was stopped.%r\r\nProtocol ID: %1%r\r\nProtocol Name: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0030011 | Identity certificate with thumbprint '%1' could not be found.%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0030012 | Identity certificate with thumbprint '%1' could not be validated.%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0030013 | Identity certificate with subject name '%1' and thumbprint '%2' does not have a private key.\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0030014 | Identity certificate with subject name '%1' and thumbprint '%2' does not have an accessible private key.\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0030015 | Identity certificate with subject name '%1' and thumbprint '%2' does not provide '%3' among its KeyUsages.\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0030016 | Identity certificate with subject name '%1' and thumbprint '%2' does not provide '%3' among its EnhancedKeyUsages.\r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0040001 | The NT service failed to start; the listening endpoint could not be published.%r\r\nError Code: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0040002 | An error occurred while parsing the %1 binding '%2' of the site '%3', thus the protocol is disabled for the site temporarily. See the exception message for more details.%r\r\nBinding: %4%r\r\nSource: %5%r\r\nException: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc0040003 | An error occurred in the Activation Service '%1' of the protocol '%2' while trying to listen for the site '%3', thus the protocol is disabled for the site temporarily. See the exception message for more details.%r\r\nURL: %4%r\r\nStatus: %5%r\r\nException: %6%r\r\nProcess Name: %7%r\r\nProcess ID: %8%r\r\n
0xc0040004 | An unexpected error occurred in the listener adapter while handling a WAS notification. The process will be terminated.%r\r\nProtocol: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0040005 | WAS was disconnected.%r\r\nHRESULT: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0040006 | A connection that WAS depends on timed out.%r\r\nProcess Name: %1%r\r\nProcess ID: %2%r\r\n
0xc0040007 | A request to start the service failed.%r\r\nError Code: %1%r\r\nProcess Name: %2%r\r\nProcess ID: %3%r\r\n
0xc0040008 | An error occurred while dispatching a duplicated socket: this handle is now leaked in the process.%r\r\nID: %1%r\r\nSource: %2%r\r\nException: %3%r \r\nProcess Name: %4%r\r\nProcess ID: %5%r\r\n
0xc0040009 | An error occurred while dispatching a duplicated named pipe: this handle is now leaked in the process.%r\r\nSource: %1%r\r\nException: %2%r\r\nProcess Name: %3%r\r\nProcess ID: %4%r\r\n
0xc0060002 | Service authorization failed.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nAuthorizationContext: %4%n\r\nActivityId: %5%n\r\nServiceAuthorizationManager: %6%n\r\n%7\r\n
0xc0060004 | Message authentication failed.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nActivityId: %4%n\r\n%5\r\n
0xc0060006 | Security negotiation failed.%n\r\nService: %1%n\r\nAction: %2%n\r\nClientIdentity: %3%n\r\nActivityId: %4%n\r\nNegotiation: %5%n\r\n%6\r\n
0xc0060008 | Transport authentication failed.%n\r\nService: %1%n\r\nClientIdentity: %2%n\r\nActivityId: %3%n\r\n%4\r\n
0xc006000a | Impersonation failed.%n\r\nMethodName: %1%n\r\nClientIdentity: %2%n\r\nActivityId: %3%n\r\n%4\r\n
