## psevents.dll

Path: %SystemRoot%\system32\WindowsPowerShell\v1.0\PSEvents.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x10000001 | PowerShell Runspace\r\n
0x10000002 | Pipeline of Commands\r\n
0x10000003 | PowerShell remoting protocol\r\n
0x10000004 | PowerShell remoting transport\r\n
0x10000005 | PowerShell remoting host proxy calls\r\n
0x10000006 | All remoting cmdlets\r\n
0x10000007 | The serialization layer\r\n
0x10000008 | All session layer\r\n
0x10000009 | The managed powershell plugin worker\r\n
0x3000000a | Open (async)\r\n
0x3000000b | Close (Async)\r\n
0x3000000c | connect\r\n
0x3000000d | Disconnect\r\n
0x3000000e | Negotiate\r\n
0x3000000f | On create calls\r\n
0x30000010 | to be used when an object is constructed\r\n
0x30000011 | To be used when an object is disposed\r\n
0x30000012 | To be used when an event handler is raised\r\n
0x30000013 | To be used when an exception is raised\r\n
0x30000014 | To be used when operation is just executing a method\r\n
0x30000015 | Send (Async)\r\n
0x30000016 | Receive (Async)\r\n
0x30000017 | Rehydration\r\n
0x30000018 | Serialization settings\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x50000014 | Debug level defined by PowerShell (which is above Informational defined by system)\r\n
0x70000001 | Connect\r\n
0x70000002 | Execute a Remote Command\r\n
0x70000003 | Serialize or deserialize remoting payload\r\n
0x90000001 | Microsoft-Windows-PowerShell/Operational\r\n
0x90000002 | Microsoft-Windows-PowerShell/Analytic\r\n
0xb0011001 | Computer Name $null or . resolve to LocalHost\r\n
0xb0011002 | Resolving to default scheme http\r\n
0xb0011003 | Remote shell name resolved to default Microsoft.PowerShell\r\n
0xb0012001 | Creating Runspace object %n %t Instance Id: %1\r\n
0xb0012002 | Creating RunspacePool object %n %t InstanceId %1 %n %t MinRunspaces %2 %n %t MaxRunspaces %3\r\n
0xb0012003 | Opening RunspacePool\r\n
0xb0012004 | Modifying activity Id and correlating\r\n
0xb0012f01 | Port resolved to %1\r\n
0xb0012f02 | AppName resolved to %1\r\n
0xb0012f03 | ComputerName resolved to %1\r\n
0xb0012f04 | Scheme is %1\r\n
0xb0012f05 | Test analytic message\r\n
0xb0012f06 | Connection Paramters are %n Connection URI: %1 %n Resource URI: %2 %n User: %3 %n OpenTimeout: %4 %n IdleTimeout: %5 %n CancelTimeout: %6 %n AuthenticationMechanism: %7 %n Thumb Print: %8 %n MaxUriRedirectionCount: %9 %n MaxReceivedDataSizePerCommand: %10 %n MaxReceivedObjectSize: %11\r\n
0xb0012f07 | Modifying activity Id and correlating\r\n
0xb0017001 | Successfully rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Rehydrated object is of type: %3\r\n
0xb0017002 | Failed to rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Type cast exception: %3 %n %t Type cast inner exception: %4\r\n
0xb0017003 | Serialization depth has been overriden. %n %t Serialized type name: %1 %n %t Original depth: %2 %n %t Overriden depth: %3 %n %t Current depth below top level: %4\r\n
0xb0017004 | Serialization mode has been overriden. %n %t Serialized type name: %1 %n %t Overriden mode: %2\r\n
0xb0017005 | Serialization of a script property has been skipped, because there is no runspace to use for evaluation of the property. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Getter script: %3\r\n
0xb0017006 | Serialization of a property has been skipped, because property getter failed. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Exception from property getter: %3 %n %t Inner exception from property getter: %4\r\n
0xb0017007 | Serialization of an enumerable object might not be complete, because object being enumerated threw an exception. %n %t Type of object being enumerated: %1 %n %t Exception: %2\r\n
0xb0017008 | Serialization called object's ToString method which failed. %n %t Type of object: %1 %n %t Exception: %2\r\n
0xb001700a | Maximum depth below top level has been reached, forcing object to be serialized as strings. %n %t Object type at max depth: %1 %n %t Property name at max depth: %2 %n %t Depth: %3\r\n
0xb001700b | XmlException has been thrown by the deserializer (most likely indicating incorrect clixml format). %n %t Line number: %1 Line position: %2 %n %t Exception: %3\r\n
0xb001700c | Serialization of specified properties failed, because one of the specified properties was missing.  %n %t Type of object: %1 %n %t Property name: %2\r\n
0xb0018001 | Received object with Runspace Id: %1 Command Id: %2 Destination: %3 DataType: %4 TargetInterface: %5\r\n
0xb0018007 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018008 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018009 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018010 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018011 | Runspace Id %1. Establishing a connection using WSMan Create Shell\r\n
0xb0018012 | Runspace Id %1. Callback received for WSMan Create Shell\r\n
0xb0018013 | Runspace Id: %1. Closing shell using WSManCloseShell\r\n
0xb0018014 | Runspace Id: %1. Callback received for WSManCloseShell\r\n
0xb0018015 | Runspace Id: %1 Pipeline Id: %2. Sending data of size %3\r\n
0xb0018016 | Runspace Id: %1 Pipeline Id: %2. Callback received for WSManSendShellInputEx\r\n
0xb0018017 | Runspace Id: %1 Pipeline Id: %2. Placing Receive request using WSManReceiveShellOutputEx\r\n
0xb0018018 | Runspace Id: %1 Pipeline Id: %2. Received Data of size %3.\r\n
0xb0018019 | Runspace Id %1 Pipeline Id %2. Establishing a command connection using WSManRunShellCommandEx\r\n
0xb0018020 | Runspace Id %1 Pipeline Id %2. Callback received for command connection\r\n
0xb0018021 | Runspace Id: %1 Pipeline Id %2. Closing transport for command\r\n
0xb0018022 | Runspace Id: %1 Pipeline Id %2. Callback received for command close\r\n
0xb0018023 | Runspace Id: %1 Pipeline Id %2. Sending signal with code %3 using WSManSignalShellEx\r\n
0xb0018024 | Runspace Id: %1 Pipeline Id %2. Callback received for WSManSignalShellEx\r\n
0xb0018025 | Runspace Id: %1. Connection is getting redirected to Uri: %2\r\n
0xb0018051 | Runspace Id: %1 Pipeline Id: %2. Server is sending data of size %3 to client. DataType: %4 TargetInterface: %5\r\n
0xb0018052 | Request %1. Creating a server remote session. UserName: %2 Custome Shell Id: %3\r\n
0xb0018053 | Reporting context for request: %1 Context Reported: %1\r\n
0xb0018054 | Reporting operation complete for request: %1 %n Error Code: %2 %n Error Message: %3 %n StackTrace: %4\r\n
0xb0018055 | Shell Context %1. Request Id %2. Creating a commonad session for running a command.\r\n
0xb0018056 | Shell Context %1 Command Context %2 Request Id %3. Stopping command.\r\n
0xb0018057 | Shell Context %1 Command Context %2 Request Id %3. Received data from client.\r\n
0xb0018058 | Shell Context %1 Command Context %2 Request Id %3. Client sent a receive request so that server can send data.\r\n
0xb0018059 | Shell Context %1 Command Context %2 IsReceiveOperation %3. Got close operation request.\r\n
0xb0018061 | Loading assembly %1 for custom shell with shell Id %2\r\n
0xb0018062 | Loading type %1 for custom shell with shell Id %2\r\n
0xb0018063 | Received remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xb0018064 | Sent remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xd0000001 | AllPublicProperties\r\n
0xd0000002 | String\r\n
0xd0000003 | SpecificProperties\r\n
0xd0000004 | InvalidTargetInterface\r\n
0xd0000005 | Session\r\n
0xd0000006 | RunspacePool\r\n
0xd0000007 | PowerShell\r\n
0xd0000008 | InvalidDataType\r\n
0xd0000009 | ExceptionAsErrorRecord\r\n
0xd000000a | SessionConfiguration\r\n
0xd000000b | SessionConfigurationRequest\r\n
0xd000000c | SessionCapability\r\n
0xd000000d | CloseSession\r\n
0xd000000e | CreateRunspacePool\r\n
0xd000000f | SetMaxRunspaces\r\n
0xd0000010 | SetMinRunspaces\r\n
0xd0000011 | RunspacePoolOperationResponse\r\n
0xd0000012 | RunspacePoolStateInfo\r\n
0xd0000013 | CreatePowerShell\r\n
0xd0000014 | AvailableRunspaces\r\n
0xd0000015 | PSEventArgs\r\n
0xd0000016 | RemoteHostCallUsingRunspaceHost\r\n
0xd0000017 | RemoteRunspaceHostResponseData\r\n
0xd0000018 | PowerShellInput\r\n
0xd0000019 | PowerShellInputEnd\r\n
0xd000001a | PowerShellOutput\r\n
0xd000001b | PowerShellErrorRecord\r\n
0xd000001c | PowerShellStateInfo\r\n
0xd000001d | PowerShellDebug\r\n
0xd000001e | PowerShellVerbose\r\n
0xd000001f | PowerShellWarning\r\n
0xd0000020 | PowerShellProgress\r\n
0xd0000021 | StopPowerShell\r\n
0xd0000022 | RemoteHostCallUsingPowerShellHost\r\n
0xd0000023 | RemotePowerShellHostResponseData\r\n
0xf0000001 | WSMAN_FLAG_NO_AUTHENTICATION\r\n
0xf0000002 | WSMAN_FLAG_AUTH_DIGEST\r\n
0xf0000003 | WSMAN_FLAG_AUTH_NEGOTIATE\r\n
0xf0000004 | WSMAN_FLAG_AUTH_BASIC\r\n
0xf0000005 | WSMAN_FLAG_AUTH_KERBEROS\r\n
0xf0000006 | WSMAN_FLAG_AUTH_CLIENT_CERTIFICATE\r\n
0xf0000007 | WSMAN_FLAG_AUTH_CREDSSP\r\n
0xf0000008 | Client\r\n
0xf0000009 | Server\r\n
0xf000000a | Listener\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x10000001 | PowerShell Runspace\r\n
0x10000002 | Pipeline of Commands\r\n
0x10000003 | PowerShell remoting protocol\r\n
0x10000004 | PowerShell remoting transport\r\n
0x10000005 | PowerShell remoting host proxy calls\r\n
0x10000006 | All remoting cmdlets\r\n
0x10000007 | The serialization layer\r\n
0x10000008 | All session layer\r\n
0x10000009 | The managed PowerShell plugin worker\r\n
0x1000000a | PSWorkflow Hosting And Execution Layer\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | Open (async)\r\n
0x3000000b | Close (Async)\r\n
0x3000000c | connect\r\n
0x3000000d | Disconnect\r\n
0x3000000e | Negotiate\r\n
0x3000000f | On create calls\r\n
0x30000010 | to be used when an object is constructed\r\n
0x30000011 | To be used when an object is disposed\r\n
0x30000012 | To be used when an event handler is raised\r\n
0x30000013 | To be used when an exception is raised\r\n
0x30000014 | To be used when operation is just executing a method\r\n
0x30000015 | Send (Async)\r\n
0x30000016 | Receive (Async)\r\n
0x30000017 | Rehydration\r\n
0x30000018 | Serialization settings\r\n
0x30000019 | Shutting down\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x50000014 | Debug level defined by PowerShell (which is above Informational defined by system)\r\n
0x70000000 | None\r\n
0x70000001 | Connect\r\n
0x70000002 | Execute a Remote Command\r\n
0x70000003 | Serialize or deserialize remoting payload\r\n
0x70000004 | PowerShell Console Startup\r\n
0x70000005 | Workflow Hosting\r\n
0x70000006 | Workflow Execution\r\n
0x70000007 | Workflow Persistence\r\n
0x70000008 | Workflow Validation\r\n
0x70000009 | Configuration\r\n
0x70000064 | Starting Engine\r\n
0x70000065 | Stopping Engine\r\n
0x70000066 | Starting Command\r\n
0x70000067 | Stopping Command\r\n
0x70000068 | Starting Provider\r\n
0x70000069 | Stopping Provider\r\n
0x7000006a | Executing Pipeline\r\n
0x7000006e | PowerShell Scheduled Jobs\r\n
0x90000001 | Microsoft-Windows-PowerShell/Operational\r\n
0x90000002 | Microsoft-Windows-PowerShell/Analytic\r\n
0x90000003 | Microsoft-Windows-PowerShell/Debug\r\n
0x90000004 | Microsoft-Windows-PowerShell/Admin\r\n
0xb0011001 | Computer Name $null or . resolve to LocalHost\r\n
0xb0011002 | Resolving to default scheme http\r\n
0xb0011003 | Remote shell name resolved to default Microsoft.PowerShell\r\n
0xb0011004 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011005 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011006 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011007 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f01 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f02 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f03 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f04 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f05 | Correlating activity id's. %n %t CurrentActivityId: %1 %n %t ParentActivityId: %2\r\n
0xb0011f06 | Class Name = %1%nMethod Name = %2%nWorkflow GUID = %3%nMessage = %4%n%5%nActivity Name = %6%nActivity GUID = %7%nParameters = %8\r\n
0xb0012001 | Creating Runspace object %n %t Instance Id: %1\r\n
0xb0012002 | Creating RunspacePool object %n %t InstanceId %1 %n %t MinRunspaces %2 %n %t MaxRunspaces %3\r\n
0xb0012003 | Opening RunspacePool\r\n
0xb0012004 | Modifying activity Id and correlating\r\n
0xb0012005 | Runspace state changed to %1\r\n
0xb0012f01 | Port resolved to %1\r\n
0xb0012f02 | AppName resolved to %1\r\n
0xb0012f03 | ComputerName resolved to %1\r\n
0xb0012f04 | Scheme is %1\r\n
0xb0012f05 | Test analytic message\r\n
0xb0012f06 | Connection Paramters are %n Connection URI: %1 %n Resource URI: %2 %n User: %3 %n OpenTimeout: %4 %n IdleTimeout: %5 %n CancelTimeout: %6 %n AuthenticationMechanism: %7 %n Thumb Print: %8 %n MaxUriRedirectionCount: %9 %n MaxReceivedDataSizePerCommand: %10 %n MaxReceivedObjectSize: %11\r\n
0xb0012f07 | Modifying activity Id and correlating\r\n
0xb0017001 | Successfully rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Rehydrated object is of type: %3\r\n
0xb0017002 | Failed to rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Type cast exception: %3 %n %t Type cast inner exception: %4\r\n
0xb0017003 | Serialization depth has been overriden. %n %t Serialized type name: %1 %n %t Original depth: %2 %n %t Overriden depth: %3 %n %t Current depth below top level: %4\r\n
0xb0017004 | Serialization mode has been overriden. %n %t Serialized type name: %1 %n %t Overriden mode: %2\r\n
0xb0017005 | Serialization of a script property has been skipped, because there is no runspace to use for evaluation of the property. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Getter script: %3\r\n
0xb0017006 | Serialization of a property has been skipped, because property getter failed. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Exception from property getter: %3 %n %t Inner exception from property getter: %4\r\n
0xb0017007 | Serialization of an enumerable object might not be complete, because object being enumerated threw an exception. %n %t Type of object being enumerated: %1 %n %t Exception: %2\r\n
0xb0017008 | Serialization called object's ToString method which failed. %n %t Type of object: %1 %n %t Exception: %2\r\n
0xb001700a | Maximum depth below top level has been reached, forcing object to be serialized as strings. %n %t Object type at max depth: %1 %n %t Property name at max depth: %2 %n %t Depth: %3\r\n
0xb001700b | XmlException has been thrown by the deserializer (most likely indicating incorrect clixml format). %n %t Line number: %1 Line position: %2 %n %t Exception: %3\r\n
0xb001700c | Serialization of specified properties failed, because one of the specified properties was missing. %n %t Type of object: %1 %n %t Property name: %2\r\n
0xb0018001 | Received object with Runspace Id: %1 Command Id: %2 Destination: %3 DataType: %4 TargetInterface: %5\r\n
0xb0018007 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018008 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018009 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018010 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018011 | Runspace Id %1. Establishing a connection using WSMan Create Shell\r\n
0xb0018012 | Runspace Id %1. Callback received for WSMan Create Shell\r\n
0xb0018013 | Runspace Id: %1. Closing shell using WSManCloseShell\r\n
0xb0018014 | Runspace Id: %1. Callback received for WSManCloseShell\r\n
0xb0018015 | Runspace Id: %1 Pipeline Id: %2. Sending data of size %3\r\n
0xb0018016 | Runspace Id: %1 Pipeline Id: %2. Callback received for WSManSendShellInputEx\r\n
0xb0018017 | Runspace Id: %1 Pipeline Id: %2. Placing Receive request using WSManReceiveShellOutputEx\r\n
0xb0018018 | Runspace Id: %1 Pipeline Id: %2. Received Data of size %3.\r\n
0xb0018019 | Runspace Id %1 Pipeline Id %2. Establishing a command connection using WSManRunShellCommandEx\r\n
0xb0018020 | Runspace Id %1 Pipeline Id %2. Callback received for command connection\r\n
0xb0018021 | Runspace Id: %1 Pipeline Id %2. Closing transport for command\r\n
0xb0018022 | Runspace Id: %1 Pipeline Id %2. Callback received for command close\r\n
0xb0018023 | Runspace Id: %1 Pipeline Id %2. Sending signal with code %3 using WSManSignalShellEx\r\n
0xb0018024 | Runspace Id: %1 Pipeline Id %2. Callback received for WSManSignalShellEx\r\n
0xb0018025 | Runspace Id: %1. Connection is getting redirected to Uri: %2\r\n
0xb0018051 | Runspace Id: %1 Pipeline Id: %2. Server is sending data of size %3 to client. DataType: %4 TargetInterface: %5\r\n
0xb0018052 | Request %1. Creating a server remote session. UserName: %2 Custome Shell Id: %3\r\n
0xb0018053 | Reporting context for request: %1 Context Reported: %1\r\n
0xb0018054 | Reporting operation complete for request: %1 %n Error Code: %2 %n Error Message: %3 %n StackTrace: %4\r\n
0xb0018055 | Shell Context %1. Request Id %2. Creating a commonad session for running a command.\r\n
0xb0018056 | Shell Context %1 Command Context %2 Request Id %3. Stopping command.\r\n
0xb0018057 | Shell Context %1 Command Context %2 Request Id %3. Received data from client.\r\n
0xb0018058 | Shell Context %1 Command Context %2 Request Id %3. Client sent a receive request so that server can send data.\r\n
0xb0018059 | Shell Context %1 Command Context %2 IsReceiveOperation %3. Got close operation request.\r\n
0xb0018061 | Loading assembly %1 for custom shell with shell Id %2\r\n
0xb0018062 | Loading type %1 for custom shell with shell Id %2\r\n
0xb0018063 | Received remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xb0018064 | Sent remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xb0018065 | Shutting down winrm service.\r\n
0xb001a001 | PowerShell console is starting up\r\n
0xb001a002 | PowerShell console is ready for user input\r\n
0xb001b001 | Tracing ErrorRecord: %n Message: %1 %n CategoryInfo.Category: %2 %n CategoryInfo.Reason : %3 %n CategoryInfo.TargetName : %4 %n FullyQualifiedErrorId: %5 %n Exception Details: %n Message : %6 %n Stack Trace: %7 %n InnerException %8 %n\r\n
0xb001b002 | Exception: %n Message: %1 %n StackTrace: %2 %n InnerException : %3 %n\r\n
0xb001b003 | Tracing PSObject\r\n
0xb001b004 | Tracing Job: %n Id: %1 %n InstanceId: %2 %n Name: %3 %n Location: %4 %n State: %5 %n Command: %6 %n\r\n
0xb001b005 | Trace Information: %n %1\r\n
0xb001b007 | Workflow plugin loaded. %n %t EndpointName: %1 %n %t User: %2 %n %t HostingMode: %3 %n %t Protocol: %4 %n %t Configuration: %n %5\r\n
0xb001b008 | Workflow execution started. %n %t WorkflowId: %1 %n %t ManagedNodes: %2\r\n
0xb001b009 | Workflow state changed. %n %t WorkflowId: %1 %n %t NewState: %2 %n %t OldState: %3\r\n
0xb001b010 | Workflow plugin has been requested for a shutdown. %n %t EndpointName: %1\r\n
0xb001b011 | Workflow plugin restarted. %n %t EndpointName: %1\r\n
0xb001b012 | Workflow is resuming. %n %t WorkflowId: %1\r\n
0xb001b013 | A quota limit that was set for the endpoint was exceeded. %n %t EndpointName: %1 %n %t ConfigName: %2 %n %t AllowedValue: %3 %n %t ValueInQuestion: %4\r\n
0xb001b014 | Workflow has resumed. %n %t WorkflowId: %1\r\n
0xb001b016 | Workflow runspace pool was created. %n %t WorkflowId: %1 %n %t ManagedNode: %2\r\n
0xb001b017 | Activity was queued for execution. %n %t WorkflowId: %1 %n %t ActivityName: %2\r\n
0xb001b018 | Activity execution started. %n %t ActivityName: %1 %n %t ActivityTypeName: %2\r\n
0xb001b019 | Workflow is being imported from a XAML file. %n %t WorkflowId: %1 %n %t XamlFile: %2\r\n
0xb001b01a | Workflow has been imported from a XAML file. %n %t WorkflowId: %1 %n %t XamlFile: %2\r\n
0xb001b01b | Workflow could not be imported from a XAML file because of an error. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b01c | Workflow validation started. %n %t WorkflowId: %1\r\n
0xb001b01d | Workflow validation succeeded. %n %t WorkflowId: %1\r\n
0xb001b01e | Workflow validation failed with error. %n %t WorkflowId: %1\r\n
0xb001b01f | Workflow activity validated. %n %t WorkflowId: %1 %n %t ActivityDisplayName: %2 %n %t ActivityTypeName: %3\r\n
0xb001b020 | Workflow activity could not be validated. %n %t WorkflowId: %1 %n %t ActivityDisplayName: %2 %n %t ActivityTypeName: %3\r\n
0xb001b021 | Activity execution failed. %n %t WorkflowId: %1 %n %t ActivityName: %2 %n %t FailureDescription: %3\r\n
0xb001b022 | Runspace availability changed. %n %t RunspaceId: %1 %n %t Availability: %2\r\n
0xb001b023 | Runspace state changed. %n %t RunspaceId: %1 %n %t NewState: %2 %n %t OldState: %3\r\n
0xb001b024 | Workflow loaded for execution. %n %t WorkflowId: %1\r\n
0xb001b025 | Workflow unloaded. %n %t WorkflowId: %1\r\n
0xb001b026 | Workflow execution cancelled. %n %t WorkflowId: %1\r\n
0xb001b027 | Workflow execution aborted. %n %t WorkflowId: %1\r\n
0xb001b028 | Workflow cleanup operation executed. %n %t WorkflowId: %1\r\n
0xb001b029 | Persisted workflow loaded from disk. %n %t WorkflowId: %1 %n %t Path: %2\r\n
0xb001b02a | Workflow data was deleted from disk. %n %t WorkflowId: %1 %n %t Path: %2\r\n
0xb001b02c | Starting remove job. %n %t JobId: %1\r\n
0xb001b02d | Job state changed. %n %t JobId: %1 %n %t WorkflowId: %2 %n %t NewState: %3 %n %t OldState: %4\r\n
0xb001b02e | Job error. %n %t JobId: %1 %n %t WorkflowId: %2 %n %t ErrorDescription: %3\r\n
0xb001b030 | Job created for workflow (child job). %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t ChildWorkflowId: %3\r\n
0xb001b031 | Parent job created for workflow. %n %t JobId: %1\r\n
0xb001b032 | All required jobs were created for workflow execution. %n %t JobId: %1 %n %t WorkflowId: %2\r\n
0xb001b033 | Child job removed for workflow. %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t WorkflowId: %3\r\n
0xb001b034 | An error occurred while removing job. %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t WorkflowId: %3 %n %t Error: %4\r\n
0xb001b035 | Loading workflow for execution. %n %t WorkflowId: %1\r\n
0xb001b036 | Workflow execution finished. %n %t WorkflowId: %1\r\n
0xb001b037 | Cancelling workflow execution. %n %t WorkflowId: %1\r\n
0xb001b038 | Aborting workflow execution. %n %t WorkflowId: %1 %n %t Reason: %2\r\n
0xb001b039 | Unloading workflow. %n %t WorkflowId: %1\r\n
0xb001b03a | Forced workflow shutdown started. %n %t WorkflowId: %1\r\n
0xb001b03b | Forced workflow shutdown finished. %n %t WorkflowId: %1\r\n
0xb001b03c | An error occurred while forcefully shutting down a workflow. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b03d | Persisting workflow to disk. %n %t WorkflowId: %1 %n %t PersistPath: %2\r\n
0xb001b03e | Workflow persisted to disk. %n %t WorkflowId: %1\r\n
0xb001b03f | Activity execution finished. %n %t ActivityName: %1\r\n
0xb001b040 | Workflow execution error. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b041 | A new PowerShell endpoint was registered. %n %t EndpointName: %1 %n %t EndpointType: %2 %n %t RegisteredBy: %3\r\n
0xb001b042 | Endpoint configuration modified. %n %t EndpointName: %1 %n %t ModifiedBy: %2\r\n
0xb001b043 | Endpoint configuration unregistered. %n %t EndpointName: %1 %n %t UnregisteredBy: %2\r\n
0xb001b044 | Endpoint configuration disabled. %n %t EndpointName: %1 %n %t DisabledBy: %2\r\n
0xb001b045 | Endpoint configuration enabled. %n %t EndpointName: %1 %n %t EnabledBy: %2\r\n
0xb001b046 | Out of process runspace started. %n %t Command: %1\r\n
0xb001b047 | Parameter splatting was performed during workflow execution. %n %t Parameters: %1 %n %t Computers: %2\r\n
0xb001b048 | Workflow engine started. %n %t EndpointName: %1\r\n
0xb001b049 | Workflow manager instantiated with %n %t CheckpointPath: %1 %n %t ConfigProviderId: %2 %n %t UserName: %3 %n %t Path: %4\r\n
0xb001b501 | BEGIN ImportWorkflowCommand::StartWorkflowApplication. Starting invocation of workflow function. Tracking Guid %1\r\n
0xb001b502 | END ImportWorkflowCommand::StartWorkflowApplication. Ending invocation of workflow function. Tracking Guid %1\r\n
0xb001b503 | BEGIN Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1\r\n
0xb001b504 | END Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1\r\n
0xb001b505 | END Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1 : ContainerParentJob Guid %2\r\n
0xb001b506 | BEGIN JobLogic ContainerParentJob Guid %1\r\n
0xb001b507 | END JobLogic ContainerParentJob Guid %1\r\n
0xb001b508 | BEGIN WorkflowExecution ContainerParentJob Guid %1\r\n
0xb001b509 | END WorkflowExecution ContainerParentJob Guid %1\r\n
0xb001b50a | WorkflowJob with Guid %1 added to ContainerParentJob with Guid %2\r\n
0xb001b50b | ProxyJob with Guid %1 associated with remote ContainerParentJob with Guid %2\r\n
0xb001b50c | BEGIN Execution of ContainerParentJob with Guid %1\r\n
0xb001b50d | END Execution of ContainerParentJob with Guid %1\r\n
0xb001b50e | BEGIN Execution of Proxy Job with Guid %1\r\n
0xb001b50f | END Execution of Proxy Job with Guid %1\r\n
0xb001b510 | BEGIN StateChanged event handler for Proxy Job with Guid %1\r\n
0xb001b511 | END StateChanged event handler for Proxy Job with Guid %1\r\n
0xb001b512 | BEGIN StateChanged event handler for Proxy Child Job with Guid %1\r\n
0xb001b513 | END StateChanged event handler for Proxy Child Job with Guid %1\r\n
0xb001b514 | BEGIN Running garbage collection\r\n
0xb001b515 | END Running garbage collection\r\n
0xb001b516 | Persistence store has reached its maximum specified size\r\n
0xb001c000 | %1\r\n
0xb001c001 | Trace Information: %n %1 %2\r\n
0xb001d001 | Scheduled Job %1 started at %2 %n\r\n
0xb001d002 | Scheduled Job %1 completed at %2 with state %3 %n\r\n
0xb001d003 | Scheduled Job Exception %1: %n Message: %2 %n StackTrace: %3 %n InnerException: %4 %n\r\n
0xd0000001 | AllPublicProperties\r\n
0xd0000002 | String\r\n
0xd0000003 | SpecificProperties\r\n
0xd0000004 | InvalidTargetInterface\r\n
0xd0000005 | Session\r\n
0xd0000006 | RunspacePool\r\n
0xd0000007 | PowerShell\r\n
0xd0000008 | InvalidDataType\r\n
0xd0000009 | ExceptionAsErrorRecord\r\n
0xd000000a | SessionConfiguration\r\n
0xd000000b | SessionConfigurationRequest\r\n
0xd000000c | SessionCapability\r\n
0xd000000d | CloseSession\r\n
0xd000000e | CreateRunspacePool\r\n
0xd000000f | SetMaxRunspaces\r\n
0xd0000010 | SetMinRunspaces\r\n
0xd0000011 | RunspacePoolOperationResponse\r\n
0xd0000012 | RunspacePoolStateInfo\r\n
0xd0000013 | CreatePowerShell\r\n
0xd0000014 | AvailableRunspaces\r\n
0xd0000015 | PSEventArgs\r\n
0xd0000016 | RemoteHostCallUsingRunspaceHost\r\n
0xd0000017 | RemoteRunspaceHostResponseData\r\n
0xd0000018 | PowerShellInput\r\n
0xd0000019 | PowerShellInputEnd\r\n
0xd000001a | PowerShellOutput\r\n
0xd000001b | PowerShellErrorRecord\r\n
0xd000001c | PowerShellStateInfo\r\n
0xd000001d | PowerShellDebug\r\n
0xd000001e | PowerShellVerbose\r\n
0xd000001f | PowerShellWarning\r\n
0xd0000020 | PowerShellProgress\r\n
0xd0000021 | StopPowerShell\r\n
0xd0000022 | RemoteHostCallUsingPowerShellHost\r\n
0xd0000023 | RemotePowerShellHostResponseData\r\n
0xf0000001 | WSMAN_FLAG_NO_AUTHENTICATION\r\n
0xf0000002 | WSMAN_FLAG_AUTH_DIGEST\r\n
0xf0000003 | WSMAN_FLAG_AUTH_NEGOTIATE\r\n
0xf0000004 | WSMAN_FLAG_AUTH_BASIC\r\n
0xf0000005 | WSMAN_FLAG_AUTH_KERBEROS\r\n
0xf0000006 | WSMAN_FLAG_AUTH_CLIENT_CERTIFICATE\r\n
0xf0000007 | WSMAN_FLAG_AUTH_CREDSSP\r\n
0xf0000008 | Client\r\n
0xf0000009 | Server\r\n
0xf000000a | Listener\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x10000001 | PowerShell Runspace\r\n
0x10000002 | Pipeline of Commands\r\n
0x10000003 | PowerShell remoting protocol\r\n
0x10000004 | PowerShell remoting transport\r\n
0x10000005 | PowerShell remoting host proxy calls\r\n
0x10000006 | All remoting cmdlets\r\n
0x10000007 | The serialization layer\r\n
0x10000008 | All session layer\r\n
0x10000009 | The managed PowerShell plugin worker\r\n
0x1000000a | PSWorkflow Hosting And Execution Layer\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | Open (async)\r\n
0x3000000b | Close (Async)\r\n
0x3000000c | connect\r\n
0x3000000d | Disconnect\r\n
0x3000000e | Negotiate\r\n
0x3000000f | On create calls\r\n
0x30000010 | to be used when an object is constructed\r\n
0x30000011 | To be used when an object is disposed\r\n
0x30000012 | To be used when an event handler is raised\r\n
0x30000013 | To be used when an exception is raised\r\n
0x30000014 | To be used when operation is just executing a method\r\n
0x30000015 | Send (Async)\r\n
0x30000016 | Receive (Async)\r\n
0x30000017 | Rehydration\r\n
0x30000018 | Serialization settings\r\n
0x30000019 | Shutting down\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x50000014 | Debug level defined by PowerShell (which is above Informational defined by system)\r\n
0x70000000 | None\r\n
0x70000001 | Connect\r\n
0x70000002 | Execute a Remote Command\r\n
0x70000003 | Serialize or deserialize remoting payload\r\n
0x70000004 | PowerShell Console Startup\r\n
0x70000005 | Workflow Hosting\r\n
0x70000006 | Workflow Execution\r\n
0x70000007 | Workflow Persistence\r\n
0x70000008 | Workflow Validation\r\n
0x70000009 | Configuration\r\n
0x70000064 | Starting Engine\r\n
0x70000065 | Stopping Engine\r\n
0x70000066 | Starting Command\r\n
0x70000067 | Stopping Command\r\n
0x70000068 | Starting Provider\r\n
0x70000069 | Stopping Provider\r\n
0x7000006a | Executing Pipeline\r\n
0x7000006e | PowerShell Scheduled Jobs\r\n
0x70000078 | PowerShell ISE Operation\r\n
0x90000001 | Microsoft-Windows-PowerShell/Operational\r\n
0x90000002 | Microsoft-Windows-PowerShell/Analytic\r\n
0x90000003 | Microsoft-Windows-PowerShell/Debug\r\n
0x90000004 | Microsoft-Windows-PowerShell/Admin\r\n
0xb0011001 | Computer Name $null or . resolve to LocalHost\r\n
0xb0011002 | Resolving to default scheme http\r\n
0xb0011003 | Remote shell name resolved to default Microsoft.PowerShell\r\n
0xb0011004 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011005 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011006 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011007 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f01 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f02 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f03 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f04 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f05 | Correlating activity id's. %n %t CurrentActivityId: %1 %n %t ParentActivityId: %2\r\n
0xb0011f06 | Class Name = %1%nMethod Name = %2%nWorkflow GUID = %3%nMessage = %4%n%5%nActivity Name = %6%nActivity GUID = %7%nParameters = %8\r\n
0xb0012001 | Creating Runspace object %n %t Instance Id: %1\r\n
0xb0012002 | Creating RunspacePool object %n %t InstanceId %1 %n %t MinRunspaces %2 %n %t MaxRunspaces %3\r\n
0xb0012003 | Opening RunspacePool\r\n
0xb0012004 | Modifying activity Id and correlating\r\n
0xb0012005 | Runspace state changed to %1\r\n
0xb0012f01 | Port resolved to %1\r\n
0xb0012f02 | AppName resolved to %1\r\n
0xb0012f03 | ComputerName resolved to %1\r\n
0xb0012f04 | Scheme is %1\r\n
0xb0012f05 | Test analytic message\r\n
0xb0012f06 | Connection Paramters are %n Connection URI: %1 %n Resource URI: %2 %n User: %3 %n OpenTimeout: %4 %n IdleTimeout: %5 %n CancelTimeout: %6 %n AuthenticationMechanism: %7 %n Thumb Print: %8 %n MaxUriRedirectionCount: %9 %n MaxReceivedDataSizePerCommand: %10 %n MaxReceivedObjectSize: %11\r\n
0xb0012f07 | Modifying activity Id and correlating\r\n
0xb0016001 | Windows PowerShell ISE has started to run script file %1.\r\n
0xb0016002 | Windows PowerShell ISE has started to run a user-selected script from file %1.\r\n
0xb0016003 | Windows PowerShell ISE is stopping the current command.\r\n
0xb0016004 | Windows PowerShell ISE is resuming the debugger.\r\n
0xb0016005 | Windows PowerShell ISE is stopping the debugger.\r\n
0xb0016006 | Windows PowerShell ISE is stepping into debugging.\r\n
0xb0016007 | Windows PowerShell ISE is stepping over debugging.\r\n
0xb0016008 | Windows PowerShell ISE is stepping out of debugging.\r\n
0xb0016010 | Windows PowerShell ISE is enabling all breakpoints.\r\n
0xb0016011 | Windows PowerShell ISE is disabling all breakpoints.\r\n
0xb0016012 | Windows PowerShell ISE is removing all breakpoints.\r\n
0xb0016013 | Windows PowerShell ISE is setting the breakpoint at line #: %1 of file %2.\r\n
0xb0016014 | Windows PowerShell ISE is removing the breakpoint on line #: %1 of file %2.\r\n
0xb0016015 | Windows PowerShell ISE is enabling the breakpoint on line #: %1 of file %2.\r\n
0xb0016016 | Windows PowerShell ISE is disabling the breakpoint on line #: %1 of file %2.\r\n
0xb0016017 | Windows PowerShell ISE has hit a breakpoint on line #: %1 of file %2.\r\n
0xb0017001 | Successfully rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Rehydrated object is of type: %3\r\n
0xb0017002 | Failed to rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Type cast exception: %3 %n %t Type cast inner exception: %4\r\n
0xb0017003 | Serialization depth has been overriden. %n %t Serialized type name: %1 %n %t Original depth: %2 %n %t Overriden depth: %3 %n %t Current depth below top level: %4\r\n
0xb0017004 | Serialization mode has been overriden. %n %t Serialized type name: %1 %n %t Overriden mode: %2\r\n
0xb0017005 | Serialization of a script property has been skipped, because there is no runspace to use for evaluation of the property. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Getter script: %3\r\n
0xb0017006 | Serialization of a property has been skipped, because property getter failed. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Exception from property getter: %3 %n %t Inner exception from property getter: %4\r\n
0xb0017007 | Serialization of an enumerable object might not be complete, because object being enumerated threw an exception. %n %t Type of object being enumerated: %1 %n %t Exception: %2\r\n
0xb0017008 | Serialization called object's ToString method which failed. %n %t Type of object: %1 %n %t Exception: %2\r\n
0xb001700a | Maximum depth below top level has been reached, forcing object to be serialized as strings. %n %t Object type at max depth: %1 %n %t Property name at max depth: %2 %n %t Depth: %3\r\n
0xb001700b | XmlException has been thrown by the deserializer (most likely indicating incorrect clixml format). %n %t Line number: %1 Line position: %2 %n %t Exception: %3\r\n
0xb001700c | Serialization of specified properties failed, because one of the specified properties was missing. %n %t Type of object: %1 %n %t Property name: %2\r\n
0xb0018001 | Received object with Runspace Id: %1 Command Id: %2 Destination: %3 DataType: %4 TargetInterface: %5\r\n
0xb0018007 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018008 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018009 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018010 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018011 | Runspace Id %1. Establishing a connection using WSMan Create Shell\r\n
0xb0018012 | Runspace Id %1. Callback received for WSMan Create Shell\r\n
0xb0018013 | Runspace Id: %1. Closing shell using WSManCloseShell\r\n
0xb0018014 | Runspace Id: %1. Callback received for WSManCloseShell\r\n
0xb0018015 | Runspace Id: %1 Pipeline Id: %2. Sending data of size %3\r\n
0xb0018016 | Runspace Id: %1 Pipeline Id: %2. Callback received for WSManSendShellInputEx\r\n
0xb0018017 | Runspace Id: %1 Pipeline Id: %2. Placing Receive request using WSManReceiveShellOutputEx\r\n
0xb0018018 | Runspace Id: %1 Pipeline Id: %2. Received Data of size %3.\r\n
0xb0018019 | Runspace Id %1 Pipeline Id %2. Establishing a command connection using WSManRunShellCommandEx\r\n
0xb0018020 | Runspace Id %1 Pipeline Id %2. Callback received for command connection\r\n
0xb0018021 | Runspace Id: %1 Pipeline Id %2. Closing transport for command\r\n
0xb0018022 | Runspace Id: %1 Pipeline Id %2. Callback received for command close\r\n
0xb0018023 | Runspace Id: %1 Pipeline Id %2. Sending signal with code %3 using WSManSignalShellEx\r\n
0xb0018024 | Runspace Id: %1 Pipeline Id %2. Callback received for WSManSignalShellEx\r\n
0xb0018025 | Runspace Id: %1. Connection is getting redirected to Uri: %2\r\n
0xb0018051 | Runspace Id: %1 Pipeline Id: %2. Server is sending data of size %3 to client. DataType: %4 TargetInterface: %5\r\n
0xb0018052 | Request %1. Creating a server remote session. UserName: %2 Custome Shell Id: %3\r\n
0xb0018053 | Reporting context for request: %1 Context Reported: %1\r\n
0xb0018054 | Reporting operation complete for request: %1 %n Error Code: %2 %n Error Message: %3 %n StackTrace: %4\r\n
0xb0018055 | Shell Context %1. Request Id %2. Creating a commonad session for running a command.\r\n
0xb0018056 | Shell Context %1 Command Context %2 Request Id %3. Stopping command.\r\n
0xb0018057 | Shell Context %1 Command Context %2 Request Id %3. Received data from client.\r\n
0xb0018058 | Shell Context %1 Command Context %2 Request Id %3. Client sent a receive request so that server can send data.\r\n
0xb0018059 | Shell Context %1 Command Context %2 IsReceiveOperation %3. Got close operation request.\r\n
0xb0018061 | Loading assembly %1 for custom shell with shell Id %2\r\n
0xb0018062 | Loading type %1 for custom shell with shell Id %2\r\n
0xb0018063 | Received remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xb0018064 | Sent remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xb0018065 | Shutting down winrm service.\r\n
0xb001a001 | PowerShell console is starting up\r\n
0xb001a002 | PowerShell console is ready for user input\r\n
0xb001b001 | Tracing ErrorRecord: %n Message: %1 %n CategoryInfo.Category: %2 %n CategoryInfo.Reason : %3 %n CategoryInfo.TargetName : %4 %n FullyQualifiedErrorId: %5 %n Exception Details: %n Message : %6 %n Stack Trace: %7 %n InnerException %8 %n\r\n
0xb001b002 | Exception: %n Message: %1 %n StackTrace: %2 %n InnerException : %3 %n\r\n
0xb001b003 | Tracing PSObject\r\n
0xb001b004 | Tracing Job: %n Id: %1 %n InstanceId: %2 %n Name: %3 %n Location: %4 %n State: %5 %n Command: %6 %n\r\n
0xb001b005 | Trace Information: %n %1\r\n
0xb001b007 | Workflow plugin loaded. %n %t EndpointName: %1 %n %t User: %2 %n %t HostingMode: %3 %n %t Protocol: %4 %n %t Configuration: %n %5\r\n
0xb001b008 | Workflow execution started. %n %t WorkflowId: %1 %n %t ManagedNodes: %2\r\n
0xb001b009 | Workflow state changed. %n %t WorkflowId: %1 %n %t NewState: %2 %n %t OldState: %3\r\n
0xb001b010 | Workflow plugin has been requested for a shutdown. %n %t EndpointName: %1\r\n
0xb001b011 | Workflow plugin restarted. %n %t EndpointName: %1\r\n
0xb001b012 | Workflow is resuming. %n %t WorkflowId: %1\r\n
0xb001b013 | A quota limit that was set for the endpoint was exceeded. %n %t EndpointName: %1 %n %t ConfigName: %2 %n %t AllowedValue: %3 %n %t ValueInQuestion: %4\r\n
0xb001b014 | Workflow has resumed. %n %t WorkflowId: %1\r\n
0xb001b016 | Workflow runspace pool was created. %n %t WorkflowId: %1 %n %t ManagedNode: %2\r\n
0xb001b017 | Activity was queued for execution. %n %t WorkflowId: %1 %n %t ActivityName: %2\r\n
0xb001b018 | Activity execution started. %n %t ActivityName: %1 %n %t ActivityTypeName: %2\r\n
0xb001b019 | Workflow is being imported from a XAML file. %n %t WorkflowId: %1 %n %t XamlFile: %2\r\n
0xb001b01a | Workflow has been imported from a XAML file. %n %t WorkflowId: %1 %n %t XamlFile: %2\r\n
0xb001b01b | Workflow could not be imported from a XAML file because of an error. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b01c | Workflow validation started. %n %t WorkflowId: %1\r\n
0xb001b01d | Workflow validation succeeded. %n %t WorkflowId: %1\r\n
0xb001b01e | Workflow validation failed with error. %n %t WorkflowId: %1\r\n
0xb001b01f | Workflow activity validated. %n %t WorkflowId: %1 %n %t ActivityDisplayName: %2 %n %t ActivityTypeName: %3\r\n
0xb001b020 | Workflow activity could not be validated. %n %t WorkflowId: %1 %n %t ActivityDisplayName: %2 %n %t ActivityTypeName: %3\r\n
0xb001b021 | Activity execution failed. %n %t WorkflowId: %1 %n %t ActivityName: %2 %n %t FailureDescription: %3\r\n
0xb001b022 | Runspace availability changed. %n %t RunspaceId: %1 %n %t Availability: %2\r\n
0xb001b023 | Runspace state changed. %n %t RunspaceId: %1 %n %t NewState: %2 %n %t OldState: %3\r\n
0xb001b024 | Workflow loaded for execution. %n %t WorkflowId: %1\r\n
0xb001b025 | Workflow unloaded. %n %t WorkflowId: %1\r\n
0xb001b026 | Workflow execution cancelled. %n %t WorkflowId: %1\r\n
0xb001b027 | Workflow execution aborted. %n %t WorkflowId: %1\r\n
0xb001b028 | Workflow cleanup operation executed. %n %t WorkflowId: %1\r\n
0xb001b029 | Persisted workflow loaded from disk. %n %t WorkflowId: %1 %n %t Path: %2\r\n
0xb001b02a | Workflow data was deleted from disk. %n %t WorkflowId: %1 %n %t Path: %2\r\n
0xb001b02c | Starting remove job. %n %t JobId: %1\r\n
0xb001b02d | Job state changed. %n %t JobId: %1 %n %t WorkflowId: %2 %n %t NewState: %3 %n %t OldState: %4\r\n
0xb001b02e | Job error. %n %t JobId: %1 %n %t WorkflowId: %2 %n %t ErrorDescription: %3\r\n
0xb001b030 | Job created for workflow (child job). %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t ChildWorkflowId: %3\r\n
0xb001b031 | Parent job created for workflow. %n %t JobId: %1\r\n
0xb001b032 | All required jobs were created for workflow execution. %n %t JobId: %1 %n %t WorkflowId: %2\r\n
0xb001b033 | Child job removed for workflow. %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t WorkflowId: %3\r\n
0xb001b034 | An error occurred while removing job. %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t WorkflowId: %3 %n %t Error: %4\r\n
0xb001b035 | Loading workflow for execution. %n %t WorkflowId: %1\r\n
0xb001b036 | Workflow execution finished. %n %t WorkflowId: %1\r\n
0xb001b037 | Cancelling workflow execution. %n %t WorkflowId: %1\r\n
0xb001b038 | Aborting workflow execution. %n %t WorkflowId: %1 %n %t Reason: %2\r\n
0xb001b039 | Unloading workflow. %n %t WorkflowId: %1\r\n
0xb001b03a | Forced workflow shutdown started. %n %t WorkflowId: %1\r\n
0xb001b03b | Forced workflow shutdown finished. %n %t WorkflowId: %1\r\n
0xb001b03c | An error occurred while forcefully shutting down a workflow. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b03d | Persisting workflow to disk. %n %t WorkflowId: %1 %n %t PersistPath: %2\r\n
0xb001b03e | Workflow persisted to disk. %n %t WorkflowId: %1\r\n
0xb001b03f | Activity execution finished. %n %t ActivityName: %1\r\n
0xb001b040 | Workflow execution error. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b041 | A new PowerShell endpoint was registered. %n %t EndpointName: %1 %n %t EndpointType: %2 %n %t RegisteredBy: %3\r\n
0xb001b042 | Endpoint configuration modified. %n %t EndpointName: %1 %n %t ModifiedBy: %2\r\n
0xb001b043 | Endpoint configuration unregistered. %n %t EndpointName: %1 %n %t UnregisteredBy: %2\r\n
0xb001b044 | Endpoint configuration disabled. %n %t EndpointName: %1 %n %t DisabledBy: %2\r\n
0xb001b045 | Endpoint configuration enabled. %n %t EndpointName: %1 %n %t EnabledBy: %2\r\n
0xb001b046 | Out of process runspace started. %n %t Command: %1\r\n
0xb001b047 | Parameter splatting was performed during workflow execution. %n %t Parameters: %1 %n %t Computers: %2\r\n
0xb001b048 | Workflow engine started. %n %t EndpointName: %1\r\n
0xb001b049 | Workflow manager instantiated with %n %t CheckpointPath: %1 %n %t ConfigProviderId: %2 %n %t UserName: %3 %n %t Path: %4\r\n
0xb001b501 | BEGIN ImportWorkflowCommand::StartWorkflowApplication. Starting invocation of workflow function. Tracking Guid %1\r\n
0xb001b502 | END ImportWorkflowCommand::StartWorkflowApplication. Ending invocation of workflow function. Tracking Guid %1\r\n
0xb001b503 | BEGIN Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1\r\n
0xb001b504 | END Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1\r\n
0xb001b505 | END Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1 : ContainerParentJob Guid %2\r\n
0xb001b506 | BEGIN JobLogic ContainerParentJob Guid %1\r\n
0xb001b507 | END JobLogic ContainerParentJob Guid %1\r\n
0xb001b508 | BEGIN WorkflowExecution ContainerParentJob Guid %1\r\n
0xb001b509 | END WorkflowExecution ContainerParentJob Guid %1\r\n
0xb001b50a | WorkflowJob with Guid %1 added to ContainerParentJob with Guid %2\r\n
0xb001b50b | ProxyJob with Guid %1 associated with remote ContainerParentJob with Guid %2\r\n
0xb001b50c | BEGIN Execution of ContainerParentJob with Guid %1\r\n
0xb001b50d | END Execution of ContainerParentJob with Guid %1\r\n
0xb001b50e | BEGIN Execution of Proxy Job with Guid %1\r\n
0xb001b50f | END Execution of Proxy Job with Guid %1\r\n
0xb001b510 | BEGIN StateChanged event handler for Proxy Job with Guid %1\r\n
0xb001b511 | END StateChanged event handler for Proxy Job with Guid %1\r\n
0xb001b512 | BEGIN StateChanged event handler for Proxy Child Job with Guid %1\r\n
0xb001b513 | END StateChanged event handler for Proxy Child Job with Guid %1\r\n
0xb001b514 | BEGIN Running garbage collection\r\n
0xb001b515 | END Running garbage collection\r\n
0xb001b516 | Persistence store has reached its maximum specified size\r\n
0xb001c000 | %1\r\n
0xb001c001 | Trace Information: %n %1 %2\r\n
0xb001d001 | Scheduled Job %1 started at %2 %n\r\n
0xb001d002 | Scheduled Job %1 completed at %2 with state %3 %n\r\n
0xb001d003 | Scheduled Job Exception %1: %n Message: %2 %n StackTrace: %3 %n InnerException: %4 %n\r\n
0xd0000001 | AllPublicProperties\r\n
0xd0000002 | String\r\n
0xd0000003 | SpecificProperties\r\n
0xd0000004 | InvalidTargetInterface\r\n
0xd0000005 | Session\r\n
0xd0000006 | RunspacePool\r\n
0xd0000007 | PowerShell\r\n
0xd0000008 | InvalidDataType\r\n
0xd0000009 | ExceptionAsErrorRecord\r\n
0xd000000a | SessionConfiguration\r\n
0xd000000b | SessionConfigurationRequest\r\n
0xd000000c | SessionCapability\r\n
0xd000000d | CloseSession\r\n
0xd000000e | CreateRunspacePool\r\n
0xd000000f | SetMaxRunspaces\r\n
0xd0000010 | SetMinRunspaces\r\n
0xd0000011 | RunspacePoolOperationResponse\r\n
0xd0000012 | RunspacePoolStateInfo\r\n
0xd0000013 | CreatePowerShell\r\n
0xd0000014 | AvailableRunspaces\r\n
0xd0000015 | PSEventArgs\r\n
0xd0000016 | RemoteHostCallUsingRunspaceHost\r\n
0xd0000017 | RemoteRunspaceHostResponseData\r\n
0xd0000018 | PowerShellInput\r\n
0xd0000019 | PowerShellInputEnd\r\n
0xd000001a | PowerShellOutput\r\n
0xd000001b | PowerShellErrorRecord\r\n
0xd000001c | PowerShellStateInfo\r\n
0xd000001d | PowerShellDebug\r\n
0xd000001e | PowerShellVerbose\r\n
0xd000001f | PowerShellWarning\r\n
0xd0000020 | PowerShellProgress\r\n
0xd0000021 | StopPowerShell\r\n
0xd0000022 | RemoteHostCallUsingPowerShellHost\r\n
0xd0000023 | RemotePowerShellHostResponseData\r\n
0xf0000001 | WSMAN_FLAG_NO_AUTHENTICATION\r\n
0xf0000002 | WSMAN_FLAG_AUTH_DIGEST\r\n
0xf0000003 | WSMAN_FLAG_AUTH_NEGOTIATE\r\n
0xf0000004 | WSMAN_FLAG_AUTH_BASIC\r\n
0xf0000005 | WSMAN_FLAG_AUTH_KERBEROS\r\n
0xf0000006 | WSMAN_FLAG_AUTH_CLIENT_CERTIFICATE\r\n
0xf0000007 | WSMAN_FLAG_AUTH_CREDSSP\r\n
0xf0000008 | Client\r\n
0xf0000009 | Server\r\n
0xf000000a | Listener\r\n

### 6.3.9600.17399

Message identifier | Message string
--- | ---
0x10000001 | PowerShell Runspace\r\n
0x10000002 | Pipeline of Commands\r\n
0x10000003 | PowerShell remoting protocol\r\n
0x10000004 | PowerShell remoting transport\r\n
0x10000005 | PowerShell remoting host proxy calls\r\n
0x10000006 | All remoting cmdlets\r\n
0x10000007 | The serialization layer\r\n
0x10000008 | All session layer\r\n
0x10000009 | The managed PowerShell plugin worker\r\n
0x1000000a | PSWorkflow Hosting And Execution Layer\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | Open (async)\r\n
0x3000000b | Close (Async)\r\n
0x3000000c | connect\r\n
0x3000000d | Disconnect\r\n
0x3000000e | Negotiate\r\n
0x3000000f | On create calls\r\n
0x30000010 | to be used when an object is constructed\r\n
0x30000011 | To be used when an object is disposed\r\n
0x30000012 | To be used when an event handler is raised\r\n
0x30000013 | To be used when an exception is raised\r\n
0x30000014 | To be used when operation is just executing a method\r\n
0x30000015 | Send (Async)\r\n
0x30000016 | Receive (Async)\r\n
0x30000017 | Rehydration\r\n
0x30000018 | Serialization settings\r\n
0x30000019 | Shutting down\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x50000014 | Debug level defined by PowerShell (which is above Informational defined by system)\r\n
0x70000000 | None\r\n
0x70000001 | Connect\r\n
0x70000002 | Execute a Remote Command\r\n
0x70000003 | Serialize or deserialize remoting payload\r\n
0x70000004 | PowerShell Console Startup\r\n
0x70000005 | Workflow Hosting\r\n
0x70000006 | Workflow Execution\r\n
0x70000007 | Workflow Persistence\r\n
0x70000008 | Workflow Validation\r\n
0x70000009 | Configuration\r\n
0x70000064 | Starting Engine\r\n
0x70000065 | Stopping Engine\r\n
0x70000066 | Starting Command\r\n
0x70000067 | Stopping Command\r\n
0x70000068 | Starting Provider\r\n
0x70000069 | Stopping Provider\r\n
0x7000006a | Executing Pipeline\r\n
0x7000006e | PowerShell Scheduled Jobs\r\n
0x70000078 | PowerShell ISE Operation\r\n
0x90000001 | Microsoft-Windows-PowerShell/Operational\r\n
0x90000002 | Microsoft-Windows-PowerShell/Analytic\r\n
0x90000003 | Microsoft-Windows-PowerShell/Debug\r\n
0x90000004 | Microsoft-Windows-PowerShell/Admin\r\n
0xb0011001 | Computer Name $null or . resolve to LocalHost\r\n
0xb0011002 | Resolving to default scheme http\r\n
0xb0011003 | Remote shell name resolved to default Microsoft.PowerShell\r\n
0xb0011004 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011005 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011006 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011007 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011008 | Creating Scriptblock text (%1 of %2):%n%3%n%nScriptBlock ID: %4\r\n
0xb0011009 | Started invocation of ScriptBlock ID: %1%nRunspace ID: %2\r\n
0xb001100a | Completed invocation of ScriptBlock ID: %1%nRunspace ID: %2\r\n
0xb0011f01 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f02 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f03 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f04 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f05 | Correlating activity id's. %n %t CurrentActivityId: %1 %n %t ParentActivityId: %2\r\n
0xb0011f06 | Class Name = %1%nMethod Name = %2%nWorkflow GUID = %3%nMessage = %4%n%5%nActivity Name = %6%nActivity GUID = %7%nParameters = %8\r\n
0xb0012001 | Creating Runspace object %n %t Instance Id: %1\r\n
0xb0012002 | Creating RunspacePool object %n %t InstanceId %1 %n %t MinRunspaces %2 %n %t MaxRunspaces %3\r\n
0xb0012003 | Opening RunspacePool\r\n
0xb0012004 | Modifying activity Id and correlating\r\n
0xb0012005 | Runspace state changed to %1\r\n
0xb0012f01 | Port resolved to %1\r\n
0xb0012f02 | AppName resolved to %1\r\n
0xb0012f03 | ComputerName resolved to %1\r\n
0xb0012f04 | Scheme is %1\r\n
0xb0012f05 | Test analytic message\r\n
0xb0012f06 | Connection Paramters are %n Connection URI: %1 %n Resource URI: %2 %n User: %3 %n OpenTimeout: %4 %n IdleTimeout: %5 %n CancelTimeout: %6 %n AuthenticationMechanism: %7 %n Thumb Print: %8 %n MaxUriRedirectionCount: %9 %n MaxReceivedDataSizePerCommand: %10 %n MaxReceivedObjectSize: %11\r\n
0xb0012f07 | Modifying activity Id and correlating\r\n
0xb0016001 | Windows PowerShell ISE has started to run script file %1.\r\n
0xb0016002 | Windows PowerShell ISE has started to run a user-selected script from file %1.\r\n
0xb0016003 | Windows PowerShell ISE is stopping the current command.\r\n
0xb0016004 | Windows PowerShell ISE is resuming the debugger.\r\n
0xb0016005 | Windows PowerShell ISE is stopping the debugger.\r\n
0xb0016006 | Windows PowerShell ISE is stepping into debugging.\r\n
0xb0016007 | Windows PowerShell ISE is stepping over debugging.\r\n
0xb0016008 | Windows PowerShell ISE is stepping out of debugging.\r\n
0xb0016010 | Windows PowerShell ISE is enabling all breakpoints.\r\n
0xb0016011 | Windows PowerShell ISE is disabling all breakpoints.\r\n
0xb0016012 | Windows PowerShell ISE is removing all breakpoints.\r\n
0xb0016013 | Windows PowerShell ISE is setting the breakpoint at line #: %1 of file %2.\r\n
0xb0016014 | Windows PowerShell ISE is removing the breakpoint on line #: %1 of file %2.\r\n
0xb0016015 | Windows PowerShell ISE is enabling the breakpoint on line #: %1 of file %2.\r\n
0xb0016016 | Windows PowerShell ISE is disabling the breakpoint on line #: %1 of file %2.\r\n
0xb0016017 | Windows PowerShell ISE has hit a breakpoint on line #: %1 of file %2.\r\n
0xb0017001 | Successfully rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Rehydrated object is of type: %3\r\n
0xb0017002 | Failed to rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Type cast exception: %3 %n %t Type cast inner exception: %4\r\n
0xb0017003 | Serialization depth has been overriden. %n %t Serialized type name: %1 %n %t Original depth: %2 %n %t Overriden depth: %3 %n %t Current depth below top level: %4\r\n
0xb0017004 | Serialization mode has been overriden. %n %t Serialized type name: %1 %n %t Overriden mode: %2\r\n
0xb0017005 | Serialization of a script property has been skipped, because there is no runspace to use for evaluation of the property. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Getter script: %3\r\n
0xb0017006 | Serialization of a property has been skipped, because property getter failed. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Exception from property getter: %3 %n %t Inner exception from property getter: %4\r\n
0xb0017007 | Serialization of an enumerable object might not be complete, because object being enumerated threw an exception. %n %t Type of object being enumerated: %1 %n %t Exception: %2\r\n
0xb0017008 | Serialization called object's ToString method which failed. %n %t Type of object: %1 %n %t Exception: %2\r\n
0xb001700a | Maximum depth below top level has been reached, forcing object to be serialized as strings. %n %t Object type at max depth: %1 %n %t Property name at max depth: %2 %n %t Depth: %3\r\n
0xb001700b | XmlException has been thrown by the deserializer (most likely indicating incorrect clixml format). %n %t Line number: %1 Line position: %2 %n %t Exception: %3\r\n
0xb001700c | Serialization of specified properties failed, because one of the specified properties was missing. %n %t Type of object: %1 %n %t Property name: %2\r\n
0xb0018001 | Received object with Runspace Id: %1 Command Id: %2 Destination: %3 DataType: %4 TargetInterface: %5\r\n
0xb0018007 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018008 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018009 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018010 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018011 | Runspace Id %1. Establishing a connection using WSMan Create Shell\r\n
0xb0018012 | Runspace Id %1. Callback received for WSMan Create Shell\r\n
0xb0018013 | Runspace Id: %1. Closing shell using WSManCloseShell\r\n
0xb0018014 | Runspace Id: %1. Callback received for WSManCloseShell\r\n
0xb0018015 | Runspace Id: %1 Pipeline Id: %2. Sending data of size %3\r\n
0xb0018016 | Runspace Id: %1 Pipeline Id: %2. Callback received for WSManSendShellInputEx\r\n
0xb0018017 | Runspace Id: %1 Pipeline Id: %2. Placing Receive request using WSManReceiveShellOutputEx\r\n
0xb0018018 | Runspace Id: %1 Pipeline Id: %2. Received Data of size %3.\r\n
0xb0018019 | Runspace Id %1 Pipeline Id %2. Establishing a command connection using WSManRunShellCommandEx\r\n
0xb0018020 | Runspace Id %1 Pipeline Id %2. Callback received for command connection\r\n
0xb0018021 | Runspace Id: %1 Pipeline Id %2. Closing transport for command\r\n
0xb0018022 | Runspace Id: %1 Pipeline Id %2. Callback received for command close\r\n
0xb0018023 | Runspace Id: %1 Pipeline Id %2. Sending signal with code %3 using WSManSignalShellEx\r\n
0xb0018024 | Runspace Id: %1 Pipeline Id %2. Callback received for WSManSignalShellEx\r\n
0xb0018025 | Runspace Id: %1. Connection is getting redirected to Uri: %2\r\n
0xb0018051 | Runspace Id: %1 Pipeline Id: %2. Server is sending data of size %3 to client. DataType: %4 TargetInterface: %5\r\n
0xb0018052 | Request %1. Creating a server remote session. UserName: %2 Custome Shell Id: %3\r\n
0xb0018053 | Reporting context for request: %1 Context Reported: %1\r\n
0xb0018054 | Reporting operation complete for request: %1 %n Error Code: %2 %n Error Message: %3 %n StackTrace: %4\r\n
0xb0018055 | Shell Context %1. Request Id %2. Creating a commonad session for running a command.\r\n
0xb0018056 | Shell Context %1 Command Context %2 Request Id %3. Stopping command.\r\n
0xb0018057 | Shell Context %1 Command Context %2 Request Id %3. Received data from client.\r\n
0xb0018058 | Shell Context %1 Command Context %2 Request Id %3. Client sent a receive request so that server can send data.\r\n
0xb0018059 | Shell Context %1 Command Context %2 IsReceiveOperation %3. Got close operation request.\r\n
0xb0018061 | Loading assembly %1 for custom shell with shell Id %2\r\n
0xb0018062 | Loading type %1 for custom shell with shell Id %2\r\n
0xb0018063 | Received remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xb0018064 | Sent remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xb0018065 | Shutting down winrm service.\r\n
0xb001a001 | PowerShell console is starting up\r\n
0xb001a002 | PowerShell console is ready for user input\r\n
0xb001b001 | Tracing ErrorRecord: %n Message: %1 %n CategoryInfo.Category: %2 %n CategoryInfo.Reason : %3 %n CategoryInfo.TargetName : %4 %n FullyQualifiedErrorId: %5 %n Exception Details: %n Message : %6 %n Stack Trace: %7 %n InnerException %8 %n\r\n
0xb001b002 | Exception: %n Message: %1 %n StackTrace: %2 %n InnerException : %3 %n\r\n
0xb001b003 | Tracing PSObject\r\n
0xb001b004 | Tracing Job: %n Id: %1 %n InstanceId: %2 %n Name: %3 %n Location: %4 %n State: %5 %n Command: %6 %n\r\n
0xb001b005 | Trace Information: %n %1\r\n
0xb001b007 | Workflow plugin loaded. %n %t EndpointName: %1 %n %t User: %2 %n %t HostingMode: %3 %n %t Protocol: %4 %n %t Configuration: %n %5\r\n
0xb001b008 | Workflow execution started. %n %t WorkflowId: %1 %n %t ManagedNodes: %2\r\n
0xb001b009 | Workflow state changed. %n %t WorkflowId: %1 %n %t NewState: %2 %n %t OldState: %3\r\n
0xb001b010 | Workflow plugin has been requested for a shutdown. %n %t EndpointName: %1\r\n
0xb001b011 | Workflow plugin restarted. %n %t EndpointName: %1\r\n
0xb001b012 | Workflow is resuming. %n %t WorkflowId: %1\r\n
0xb001b013 | A quota limit that was set for the endpoint was exceeded. %n %t EndpointName: %1 %n %t ConfigName: %2 %n %t AllowedValue: %3 %n %t ValueInQuestion: %4\r\n
0xb001b014 | Workflow has resumed. %n %t WorkflowId: %1\r\n
0xb001b016 | Workflow runspace pool was created. %n %t WorkflowId: %1 %n %t ManagedNode: %2\r\n
0xb001b017 | Activity was queued for execution. %n %t WorkflowId: %1 %n %t ActivityName: %2\r\n
0xb001b018 | Activity execution started. %n %t ActivityName: %1 %n %t ActivityTypeName: %2\r\n
0xb001b019 | Workflow is being imported from a XAML file. %n %t WorkflowId: %1 %n %t XamlFile: %2\r\n
0xb001b01a | Workflow has been imported from a XAML file. %n %t WorkflowId: %1 %n %t XamlFile: %2\r\n
0xb001b01b | Workflow could not be imported from a XAML file because of an error. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b01c | Workflow validation started. %n %t WorkflowId: %1\r\n
0xb001b01d | Workflow validation succeeded. %n %t WorkflowId: %1\r\n
0xb001b01e | Workflow validation failed with error. %n %t WorkflowId: %1\r\n
0xb001b01f | Workflow activity validated. %n %t WorkflowId: %1 %n %t ActivityDisplayName: %2 %n %t ActivityTypeName: %3\r\n
0xb001b020 | Workflow activity could not be validated. %n %t WorkflowId: %1 %n %t ActivityDisplayName: %2 %n %t ActivityTypeName: %3\r\n
0xb001b021 | Activity execution failed. %n %t WorkflowId: %1 %n %t ActivityName: %2 %n %t FailureDescription: %3\r\n
0xb001b022 | Runspace availability changed. %n %t RunspaceId: %1 %n %t Availability: %2\r\n
0xb001b023 | Runspace state changed. %n %t RunspaceId: %1 %n %t NewState: %2 %n %t OldState: %3\r\n
0xb001b024 | Workflow loaded for execution. %n %t WorkflowId: %1\r\n
0xb001b025 | Workflow unloaded. %n %t WorkflowId: %1\r\n
0xb001b026 | Workflow execution cancelled. %n %t WorkflowId: %1\r\n
0xb001b027 | Workflow execution aborted. %n %t WorkflowId: %1\r\n
0xb001b028 | Workflow cleanup operation executed. %n %t WorkflowId: %1\r\n
0xb001b029 | Persisted workflow loaded from disk. %n %t WorkflowId: %1 %n %t Path: %2\r\n
0xb001b02a | Workflow data was deleted from disk. %n %t WorkflowId: %1 %n %t Path: %2\r\n
0xb001b02c | Starting remove job. %n %t JobId: %1\r\n
0xb001b02d | Job state changed. %n %t JobId: %1 %n %t WorkflowId: %2 %n %t NewState: %3 %n %t OldState: %4\r\n
0xb001b02e | Job error. %n %t JobId: %1 %n %t WorkflowId: %2 %n %t ErrorDescription: %3\r\n
0xb001b030 | Job created for workflow (child job). %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t ChildWorkflowId: %3\r\n
0xb001b031 | Parent job created for workflow. %n %t JobId: %1\r\n
0xb001b032 | All required jobs were created for workflow execution. %n %t JobId: %1 %n %t WorkflowId: %2\r\n
0xb001b033 | Child job removed for workflow. %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t WorkflowId: %3\r\n
0xb001b034 | An error occurred while removing job. %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t WorkflowId: %3 %n %t Error: %4\r\n
0xb001b035 | Loading workflow for execution. %n %t WorkflowId: %1\r\n
0xb001b036 | Workflow execution finished. %n %t WorkflowId: %1\r\n
0xb001b037 | Cancelling workflow execution. %n %t WorkflowId: %1\r\n
0xb001b038 | Aborting workflow execution. %n %t WorkflowId: %1 %n %t Reason: %2\r\n
0xb001b039 | Unloading workflow. %n %t WorkflowId: %1\r\n
0xb001b03a | Forced workflow shutdown started. %n %t WorkflowId: %1\r\n
0xb001b03b | Forced workflow shutdown finished. %n %t WorkflowId: %1\r\n
0xb001b03c | An error occurred while forcefully shutting down a workflow. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b03d | Persisting workflow to disk. %n %t WorkflowId: %1 %n %t PersistPath: %2\r\n
0xb001b03e | Workflow persisted to disk. %n %t WorkflowId: %1\r\n
0xb001b03f | Activity execution finished. %n %t ActivityName: %1\r\n
0xb001b040 | Workflow execution error. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b041 | A new PowerShell endpoint was registered. %n %t EndpointName: %1 %n %t EndpointType: %2 %n %t RegisteredBy: %3\r\n
0xb001b042 | Endpoint configuration modified. %n %t EndpointName: %1 %n %t ModifiedBy: %2\r\n
0xb001b043 | Endpoint configuration unregistered. %n %t EndpointName: %1 %n %t UnregisteredBy: %2\r\n
0xb001b044 | Endpoint configuration disabled. %n %t EndpointName: %1 %n %t DisabledBy: %2\r\n
0xb001b045 | Endpoint configuration enabled. %n %t EndpointName: %1 %n %t EnabledBy: %2\r\n
0xb001b046 | Out of process runspace started. %n %t Command: %1\r\n
0xb001b047 | Parameter splatting was performed during workflow execution. %n %t Parameters: %1 %n %t Computers: %2\r\n
0xb001b048 | Workflow engine started. %n %t EndpointName: %1\r\n
0xb001b049 | Workflow manager instantiated with %n %t CheckpointPath: %1 %n %t ConfigProviderId: %2 %n %t UserName: %3 %n %t Path: %4\r\n
0xb001b501 | BEGIN ImportWorkflowCommand::StartWorkflowApplication. Starting invocation of workflow function. Tracking Guid %1\r\n
0xb001b502 | END ImportWorkflowCommand::StartWorkflowApplication. Ending invocation of workflow function. Tracking Guid %1\r\n
0xb001b503 | BEGIN Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1\r\n
0xb001b504 | END Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1\r\n
0xb001b505 | END Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1 : ContainerParentJob Guid %2\r\n
0xb001b506 | BEGIN JobLogic ContainerParentJob Guid %1\r\n
0xb001b507 | END JobLogic ContainerParentJob Guid %1\r\n
0xb001b508 | BEGIN WorkflowExecution ContainerParentJob Guid %1\r\n
0xb001b509 | END WorkflowExecution ContainerParentJob Guid %1\r\n
0xb001b50a | WorkflowJob with Guid %1 added to ContainerParentJob with Guid %2\r\n
0xb001b50b | ProxyJob with Guid %1 associated with remote ContainerParentJob with Guid %2\r\n
0xb001b50c | BEGIN Execution of ContainerParentJob with Guid %1\r\n
0xb001b50d | END Execution of ContainerParentJob with Guid %1\r\n
0xb001b50e | BEGIN Execution of Proxy Job with Guid %1\r\n
0xb001b50f | END Execution of Proxy Job with Guid %1\r\n
0xb001b510 | BEGIN StateChanged event handler for Proxy Job with Guid %1\r\n
0xb001b511 | END StateChanged event handler for Proxy Job with Guid %1\r\n
0xb001b512 | BEGIN StateChanged event handler for Proxy Child Job with Guid %1\r\n
0xb001b513 | END StateChanged event handler for Proxy Child Job with Guid %1\r\n
0xb001b514 | BEGIN Running garbage collection\r\n
0xb001b515 | END Running garbage collection\r\n
0xb001b516 | Persistence store has reached its maximum specified size\r\n
0xb001c000 | %1\r\n
0xb001c001 | Trace Information: %n %1 %2\r\n
0xb001d001 | Scheduled Job %1 started at %2 %n\r\n
0xb001d002 | Scheduled Job %1 completed at %2 with state %3 %n\r\n
0xb001d003 | Scheduled Job Exception %1: %n Message: %2 %n StackTrace: %3 %n InnerException: %4 %n\r\n
0xd0000001 | AllPublicProperties\r\n
0xd0000002 | String\r\n
0xd0000003 | SpecificProperties\r\n
0xd0000004 | InvalidTargetInterface\r\n
0xd0000005 | Session\r\n
0xd0000006 | RunspacePool\r\n
0xd0000007 | PowerShell\r\n
0xd0000008 | InvalidDataType\r\n
0xd0000009 | ExceptionAsErrorRecord\r\n
0xd000000a | SessionConfiguration\r\n
0xd000000b | SessionConfigurationRequest\r\n
0xd000000c | SessionCapability\r\n
0xd000000d | CloseSession\r\n
0xd000000e | CreateRunspacePool\r\n
0xd000000f | SetMaxRunspaces\r\n
0xd0000010 | SetMinRunspaces\r\n
0xd0000011 | RunspacePoolOperationResponse\r\n
0xd0000012 | RunspacePoolStateInfo\r\n
0xd0000013 | CreatePowerShell\r\n
0xd0000014 | AvailableRunspaces\r\n
0xd0000015 | PSEventArgs\r\n
0xd0000016 | RemoteHostCallUsingRunspaceHost\r\n
0xd0000017 | RemoteRunspaceHostResponseData\r\n
0xd0000018 | PowerShellInput\r\n
0xd0000019 | PowerShellInputEnd\r\n
0xd000001a | PowerShellOutput\r\n
0xd000001b | PowerShellErrorRecord\r\n
0xd000001c | PowerShellStateInfo\r\n
0xd000001d | PowerShellDebug\r\n
0xd000001e | PowerShellVerbose\r\n
0xd000001f | PowerShellWarning\r\n
0xd0000020 | PowerShellProgress\r\n
0xd0000021 | StopPowerShell\r\n
0xd0000022 | RemoteHostCallUsingPowerShellHost\r\n
0xd0000023 | RemotePowerShellHostResponseData\r\n
0xf0000001 | WSMAN_FLAG_NO_AUTHENTICATION\r\n
0xf0000002 | WSMAN_FLAG_AUTH_DIGEST\r\n
0xf0000003 | WSMAN_FLAG_AUTH_NEGOTIATE\r\n
0xf0000004 | WSMAN_FLAG_AUTH_BASIC\r\n
0xf0000005 | WSMAN_FLAG_AUTH_KERBEROS\r\n
0xf0000006 | WSMAN_FLAG_AUTH_CLIENT_CERTIFICATE\r\n
0xf0000007 | WSMAN_FLAG_AUTH_CREDSSP\r\n
0xf0000008 | Client\r\n
0xf0000009 | Server\r\n
0xf000000a | Listener\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000001 | PowerShell Runspace\r\n
0x10000002 | Pipeline of Commands\r\n
0x10000003 | PowerShell remoting protocol\r\n
0x10000004 | PowerShell remoting transport\r\n
0x10000005 | PowerShell remoting host proxy calls\r\n
0x10000006 | All remoting cmdlets\r\n
0x10000007 | The serialization layer\r\n
0x10000008 | All session layer\r\n
0x10000009 | The managed PowerShell plugin worker\r\n
0x1000000a | PSWorkflow Hosting And Execution Layer\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3000000a | Open (async)\r\n
0x3000000b | Close (Async)\r\n
0x3000000c | connect\r\n
0x3000000d | Disconnect\r\n
0x3000000e | Negotiate\r\n
0x3000000f | On create calls\r\n
0x30000010 | to be used when an object is constructed\r\n
0x30000011 | To be used when an object is disposed\r\n
0x30000012 | To be used when an event handler is raised\r\n
0x30000013 | To be used when an exception is raised\r\n
0x30000014 | To be used when operation is just executing a method\r\n
0x30000015 | Send (Async)\r\n
0x30000016 | Receive (Async)\r\n
0x30000017 | Rehydration\r\n
0x30000018 | Serialization settings\r\n
0x30000019 | Shutting down\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x50000014 | Debug level defined by PowerShell (which is above Informational defined by system)\r\n
0x70000000 | None\r\n
0x70000001 | Connect\r\n
0x70000002 | Execute a Remote Command\r\n
0x70000003 | Serialize or deserialize remoting payload\r\n
0x70000004 | PowerShell Console Startup\r\n
0x70000005 | Workflow Hosting\r\n
0x70000006 | Workflow Execution\r\n
0x70000007 | Workflow Persistence\r\n
0x70000008 | Workflow Validation\r\n
0x70000009 | Configuration\r\n
0x70000064 | Starting Engine\r\n
0x70000065 | Stopping Engine\r\n
0x70000066 | Starting Command\r\n
0x70000067 | Stopping Command\r\n
0x70000068 | Starting Provider\r\n
0x70000069 | Stopping Provider\r\n
0x7000006a | Executing Pipeline\r\n
0x7000006e | PowerShell Scheduled Jobs\r\n
0x7000006f | PowerShell Named Pipe IPC\r\n
0x70000078 | PowerShell ISE Operation\r\n
0x90000001 | Microsoft-Windows-PowerShell/Operational\r\n
0x90000002 | Microsoft-Windows-PowerShell/Analytic\r\n
0x90000003 | Microsoft-Windows-PowerShell/Debug\r\n
0x90000004 | Microsoft-Windows-PowerShell/Admin\r\n
0xb0011001 | Computer Name $null or . resolve to LocalHost\r\n
0xb0011002 | Resolving to default scheme http\r\n
0xb0011003 | Remote shell name resolved to default Microsoft.PowerShell\r\n
0xb0011004 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011005 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011006 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011007 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011008 | Creating Scriptblock text (%1 of %2):%n%3%n%nScriptBlock ID: %4%nPath: %5\r\n
0xb0011009 | Started invocation of ScriptBlock ID: %1%nRunspace ID: %2\r\n
0xb001100a | Completed invocation of ScriptBlock ID: %1%nRunspace ID: %2\r\n
0xb0011f01 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f02 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f03 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f04 | %3%n%nContext:%n%1%n%nUser Data:%n%2%n\r\n
0xb0011f05 | Correlating activity id's. %n %t CurrentActivityId: %1 %n %t ParentActivityId: %2\r\n
0xb0011f06 | Class Name = %1%nMethod Name = %2%nWorkflow GUID = %3%nMessage = %4%n%5%nActivity Name = %6%nActivity GUID = %7%nParameters = %8\r\n
0xb0012001 | Creating Runspace object %n %t Instance Id: %1\r\n
0xb0012002 | Creating RunspacePool object %n %t InstanceId %1 %n %t MinRunspaces %2 %n %t MaxRunspaces %3\r\n
0xb0012003 | Opening RunspacePool\r\n
0xb0012004 | Modifying activity Id and correlating\r\n
0xb0012005 | Runspace state changed to %1\r\n
0xb0012006 | Attempting session creation retry %1 for error code %2 on session Id %3\r\n
0xb0012f01 | Port resolved to %1\r\n
0xb0012f02 | AppName resolved to %1\r\n
0xb0012f03 | ComputerName resolved to %1\r\n
0xb0012f04 | Scheme is %1\r\n
0xb0012f05 | Test analytic message\r\n
0xb0012f06 | Connection Paramters are %n Connection URI: %1 %n Resource URI: %2 %n User: %3 %n OpenTimeout: %4 %n IdleTimeout: %5 %n CancelTimeout: %6 %n AuthenticationMechanism: %7 %n Thumb Print: %8 %n MaxUriRedirectionCount: %9 %n MaxReceivedDataSizePerCommand: %10 %n MaxReceivedObjectSize: %11\r\n
0xb0012f07 | Modifying activity Id and correlating\r\n
0xb0016001 | Windows PowerShell ISE has started to run script file %1.\r\n
0xb0016002 | Windows PowerShell ISE has started to run a user-selected script from file %1.\r\n
0xb0016003 | Windows PowerShell ISE is stopping the current command.\r\n
0xb0016004 | Windows PowerShell ISE is resuming the debugger.\r\n
0xb0016005 | Windows PowerShell ISE is stopping the debugger.\r\n
0xb0016006 | Windows PowerShell ISE is stepping into debugging.\r\n
0xb0016007 | Windows PowerShell ISE is stepping over debugging.\r\n
0xb0016008 | Windows PowerShell ISE is stepping out of debugging.\r\n
0xb0016010 | Windows PowerShell ISE is enabling all breakpoints.\r\n
0xb0016011 | Windows PowerShell ISE is disabling all breakpoints.\r\n
0xb0016012 | Windows PowerShell ISE is removing all breakpoints.\r\n
0xb0016013 | Windows PowerShell ISE is setting the breakpoint at line #: %1 of file %2.\r\n
0xb0016014 | Windows PowerShell ISE is removing the breakpoint on line #: %1 of file %2.\r\n
0xb0016015 | Windows PowerShell ISE is enabling the breakpoint on line #: %1 of file %2.\r\n
0xb0016016 | Windows PowerShell ISE is disabling the breakpoint on line #: %1 of file %2.\r\n
0xb0016017 | Windows PowerShell ISE has hit a breakpoint on line #: %1 of file %2.\r\n
0xb0017001 | Successfully rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Rehydrated object is of type: %3\r\n
0xb0017002 | Failed to rehydrated an object. %n %t Deserialized type name: %1 %n %t Rehydrated by casting to type: %2 %n %t Type cast exception: %3 %n %t Type cast inner exception: %4\r\n
0xb0017003 | Serialization depth has been overriden. %n %t Serialized type name: %1 %n %t Original depth: %2 %n %t Overriden depth: %3 %n %t Current depth below top level: %4\r\n
0xb0017004 | Serialization mode has been overriden. %n %t Serialized type name: %1 %n %t Overriden mode: %2\r\n
0xb0017005 | Serialization of a script property has been skipped, because there is no runspace to use for evaluation of the property. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Getter script: %3\r\n
0xb0017006 | Serialization of a property has been skipped, because property getter failed. %n %t Property name: %1 %n %t Property owner's type name: %2 %n %t Exception from property getter: %3 %n %t Inner exception from property getter: %4\r\n
0xb0017007 | Serialization of an enumerable object might not be complete, because object being enumerated threw an exception. %n %t Type of object being enumerated: %1 %n %t Exception: %2\r\n
0xb0017008 | Serialization called object's ToString method which failed. %n %t Type of object: %1 %n %t Exception: %2\r\n
0xb001700a | Maximum depth below top level has been reached, forcing object to be serialized as strings. %n %t Object type at max depth: %1 %n %t Property name at max depth: %2 %n %t Depth: %3\r\n
0xb001700b | XmlException has been thrown by the deserializer (most likely indicating incorrect clixml format). %n %t Line number: %1 Line position: %2 %n %t Exception: %3\r\n
0xb001700c | Serialization of specified properties failed, because one of the specified properties was missing. %n %t Type of object: %1 %n %t Property name: %2\r\n
0xb0018001 | Received object with Runspace Id: %1 Command Id: %2 Destination: %3 DataType: %4 TargetInterface: %5\r\n
0xb0018007 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018008 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018009 | An unhandled exception occurred in the appdomain. %nException Type: %1 %nException Message: %2 %nException StackTrace: %3\r\n
0xb0018010 | Runspace Id: %1 Pipeline Id: %2. WSMan reported an error with error code: %3. %n Error message: %4 %n StackTrace: %5\r\n
0xb0018011 | Runspace Id %1. Establishing a connection using WSMan Create Shell\r\n
0xb0018012 | Runspace Id %1. Callback received for WSMan Create Shell\r\n
0xb0018013 | Runspace Id: %1. Closing shell using WSManCloseShell\r\n
0xb0018014 | Runspace Id: %1. Callback received for WSManCloseShell\r\n
0xb0018015 | Runspace Id: %1 Pipeline Id: %2. Sending data of size %3\r\n
0xb0018016 | Runspace Id: %1 Pipeline Id: %2. Callback received for WSManSendShellInputEx\r\n
0xb0018017 | Runspace Id: %1 Pipeline Id: %2. Placing Receive request using WSManReceiveShellOutputEx\r\n
0xb0018018 | Runspace Id: %1 Pipeline Id: %2. Received Data of size %3.\r\n
0xb0018019 | Runspace Id %1 Pipeline Id %2. Establishing a command connection using WSManRunShellCommandEx\r\n
0xb0018020 | Runspace Id %1 Pipeline Id %2. Callback received for command connection\r\n
0xb0018021 | Runspace Id: %1 Pipeline Id %2. Closing transport for command\r\n
0xb0018022 | Runspace Id: %1 Pipeline Id %2. Callback received for command close\r\n
0xb0018023 | Runspace Id: %1 Pipeline Id %2. Sending signal with code %3 using WSManSignalShellEx\r\n
0xb0018024 | Runspace Id: %1 Pipeline Id %2. Callback received for WSManSignalShellEx\r\n
0xb0018025 | Runspace Id: %1. Connection is getting redirected to Uri: %2\r\n
0xb0018051 | Runspace Id: %1 Pipeline Id: %2. Server is sending data of size %3 to client. DataType: %4 TargetInterface: %5\r\n
0xb0018052 | Request %1. Creating a server remote session. UserName: %2 Custome Shell Id: %3\r\n
0xb0018053 | Reporting context for request: %1 Context Reported: %1\r\n
0xb0018054 | Reporting operation complete for request: %1 %n Error Code: %2 %n Error Message: %3 %n StackTrace: %4\r\n
0xb0018055 | Shell Context %1. Request Id %2. Creating a commonad session for running a command.\r\n
0xb0018056 | Shell Context %1 Command Context %2 Request Id %3. Stopping command.\r\n
0xb0018057 | Shell Context %1 Command Context %2 Request Id %3. Received data from client.\r\n
0xb0018058 | Shell Context %1 Command Context %2 Request Id %3. Client sent a receive request so that server can send data.\r\n
0xb0018059 | Shell Context %1 Command Context %2 IsReceiveOperation %3. Got close operation request.\r\n
0xb0018061 | Loading assembly %1 for custom shell with shell Id %2\r\n
0xb0018062 | Loading type %1 for custom shell with shell Id %2\r\n
0xb0018063 | Received remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xb0018064 | Sent remoting fragment. %n %t Object Id: %1 %n %t Fragment Id: %2 %n %t Start Flag: %3 %n %t End Flag: %4 %n %t Payload Length: %5 %n %t Payload Data: %6\r\n
0xb0018065 | Shutting down winrm service.\r\n
0xb001a001 | PowerShell console is starting up\r\n
0xb001a002 | PowerShell console is ready for user input\r\n
0xb001b001 | Tracing ErrorRecord: %n Message: %1 %n CategoryInfo.Category: %2 %n CategoryInfo.Reason : %3 %n CategoryInfo.TargetName : %4 %n FullyQualifiedErrorId: %5 %n Exception Details: %n Message : %6 %n Stack Trace: %7 %n InnerException %8 %n\r\n
0xb001b002 | Exception: %n Message: %1 %n StackTrace: %2 %n InnerException : %3 %n\r\n
0xb001b003 | Tracing PSObject\r\n
0xb001b004 | Tracing Job: %n Id: %1 %n InstanceId: %2 %n Name: %3 %n Location: %4 %n State: %5 %n Command: %6 %n\r\n
0xb001b005 | Trace Information: %n %1\r\n
0xb001b007 | Workflow plugin loaded. %n %t EndpointName: %1 %n %t User: %2 %n %t HostingMode: %3 %n %t Protocol: %4 %n %t Configuration: %n %5\r\n
0xb001b008 | Workflow execution started. %n %t WorkflowId: %1 %n %t ManagedNodes: %2\r\n
0xb001b009 | Workflow state changed. %n %t WorkflowId: %1 %n %t NewState: %2 %n %t OldState: %3\r\n
0xb001b010 | Workflow plugin has been requested for a shutdown. %n %t EndpointName: %1\r\n
0xb001b011 | Workflow plugin restarted. %n %t EndpointName: %1\r\n
0xb001b012 | Workflow is resuming. %n %t WorkflowId: %1\r\n
0xb001b013 | A quota limit that was set for the endpoint was exceeded. %n %t EndpointName: %1 %n %t ConfigName: %2 %n %t AllowedValue: %3 %n %t ValueInQuestion: %4\r\n
0xb001b014 | Workflow has resumed. %n %t WorkflowId: %1\r\n
0xb001b016 | Workflow runspace pool was created. %n %t WorkflowId: %1 %n %t ManagedNode: %2\r\n
0xb001b017 | Activity was queued for execution. %n %t WorkflowId: %1 %n %t ActivityName: %2\r\n
0xb001b018 | Activity execution started. %n %t ActivityName: %1 %n %t ActivityTypeName: %2\r\n
0xb001b019 | Workflow is being imported from a XAML file. %n %t WorkflowId: %1 %n %t XamlFile: %2\r\n
0xb001b01a | Workflow has been imported from a XAML file. %n %t WorkflowId: %1 %n %t XamlFile: %2\r\n
0xb001b01b | Workflow could not be imported from a XAML file because of an error. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b01c | Workflow validation started. %n %t WorkflowId: %1\r\n
0xb001b01d | Workflow validation succeeded. %n %t WorkflowId: %1\r\n
0xb001b01e | Workflow validation failed with error. %n %t WorkflowId: %1\r\n
0xb001b01f | Workflow activity validated. %n %t WorkflowId: %1 %n %t ActivityDisplayName: %2 %n %t ActivityTypeName: %3\r\n
0xb001b020 | Workflow activity could not be validated. %n %t WorkflowId: %1 %n %t ActivityDisplayName: %2 %n %t ActivityTypeName: %3\r\n
0xb001b021 | Activity execution failed. %n %t WorkflowId: %1 %n %t ActivityName: %2 %n %t FailureDescription: %3\r\n
0xb001b022 | Runspace availability changed. %n %t RunspaceId: %1 %n %t Availability: %2\r\n
0xb001b023 | Runspace state changed. %n %t RunspaceId: %1 %n %t NewState: %2 %n %t OldState: %3\r\n
0xb001b024 | Workflow loaded for execution. %n %t WorkflowId: %1\r\n
0xb001b025 | Workflow unloaded. %n %t WorkflowId: %1\r\n
0xb001b026 | Workflow execution cancelled. %n %t WorkflowId: %1\r\n
0xb001b027 | Workflow execution aborted. %n %t WorkflowId: %1\r\n
0xb001b028 | Workflow cleanup operation executed. %n %t WorkflowId: %1\r\n
0xb001b029 | Persisted workflow loaded from disk. %n %t WorkflowId: %1 %n %t Path: %2\r\n
0xb001b02a | Workflow data was deleted from disk. %n %t WorkflowId: %1 %n %t Path: %2\r\n
0xb001b02c | Starting remove job. %n %t JobId: %1\r\n
0xb001b02d | Job state changed. %n %t JobId: %1 %n %t WorkflowId: %2 %n %t NewState: %3 %n %t OldState: %4\r\n
0xb001b02e | Job error. %n %t JobId: %1 %n %t WorkflowId: %2 %n %t ErrorDescription: %3\r\n
0xb001b030 | Job created for workflow (child job). %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t ChildWorkflowId: %3\r\n
0xb001b031 | Parent job created for workflow. %n %t JobId: %1\r\n
0xb001b032 | All required jobs were created for workflow execution. %n %t JobId: %1 %n %t WorkflowId: %2\r\n
0xb001b033 | Child job removed for workflow. %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t WorkflowId: %3\r\n
0xb001b034 | An error occurred while removing job. %n %t ParentJobId: %1 %n %t ChildJobId: %2 %n %t WorkflowId: %3 %n %t Error: %4\r\n
0xb001b035 | Loading workflow for execution. %n %t WorkflowId: %1\r\n
0xb001b036 | Workflow execution finished. %n %t WorkflowId: %1\r\n
0xb001b037 | Cancelling workflow execution. %n %t WorkflowId: %1\r\n
0xb001b038 | Aborting workflow execution. %n %t WorkflowId: %1 %n %t Reason: %2\r\n
0xb001b039 | Unloading workflow. %n %t WorkflowId: %1\r\n
0xb001b03a | Forced workflow shutdown started. %n %t WorkflowId: %1\r\n
0xb001b03b | Forced workflow shutdown finished. %n %t WorkflowId: %1\r\n
0xb001b03c | An error occurred while forcefully shutting down a workflow. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b03d | Persisting workflow to disk. %n %t WorkflowId: %1 %n %t PersistPath: %2\r\n
0xb001b03e | Workflow persisted to disk. %n %t WorkflowId: %1\r\n
0xb001b03f | Activity execution finished. %n %t ActivityName: %1\r\n
0xb001b040 | Workflow execution error. %n %t WorkflowId: %1 %n %t ErrorDescription: %2\r\n
0xb001b041 | A new PowerShell endpoint was registered. %n %t EndpointName: %1 %n %t EndpointType: %2 %n %t RegisteredBy: %3\r\n
0xb001b042 | Endpoint configuration modified. %n %t EndpointName: %1 %n %t ModifiedBy: %2\r\n
0xb001b043 | Endpoint configuration unregistered. %n %t EndpointName: %1 %n %t UnregisteredBy: %2\r\n
0xb001b044 | Endpoint configuration disabled. %n %t EndpointName: %1 %n %t DisabledBy: %2\r\n
0xb001b045 | Endpoint configuration enabled. %n %t EndpointName: %1 %n %t EnabledBy: %2\r\n
0xb001b046 | Out of process runspace started. %n %t Command: %1\r\n
0xb001b047 | Parameter splatting was performed during workflow execution. %n %t Parameters: %1 %n %t Computers: %2\r\n
0xb001b048 | Workflow engine started. %n %t EndpointName: %1\r\n
0xb001b049 | Workflow manager instantiated with %n %t CheckpointPath: %1 %n %t ConfigProviderId: %2 %n %t UserName: %3 %n %t Path: %4\r\n
0xb001b501 | BEGIN ImportWorkflowCommand::StartWorkflowApplication. Starting invocation of workflow function. Tracking Guid %1\r\n
0xb001b502 | END ImportWorkflowCommand::StartWorkflowApplication. Ending invocation of workflow function. Tracking Guid %1\r\n
0xb001b503 | BEGIN Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1\r\n
0xb001b504 | END Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1\r\n
0xb001b505 | END Creating new job in ImportWorkflowCommand::StartWorkflowApplication. Tracking Guid %1 : ContainerParentJob Guid %2\r\n
0xb001b506 | BEGIN JobLogic ContainerParentJob Guid %1\r\n
0xb001b507 | END JobLogic ContainerParentJob Guid %1\r\n
0xb001b508 | BEGIN WorkflowExecution ContainerParentJob Guid %1\r\n
0xb001b509 | END WorkflowExecution ContainerParentJob Guid %1\r\n
0xb001b50a | WorkflowJob with Guid %1 added to ContainerParentJob with Guid %2\r\n
0xb001b50b | ProxyJob with Guid %1 associated with remote ContainerParentJob with Guid %2\r\n
0xb001b50c | BEGIN Execution of ContainerParentJob with Guid %1\r\n
0xb001b50d | END Execution of ContainerParentJob with Guid %1\r\n
0xb001b50e | BEGIN Execution of Proxy Job with Guid %1\r\n
0xb001b50f | END Execution of Proxy Job with Guid %1\r\n
0xb001b510 | BEGIN StateChanged event handler for Proxy Job with Guid %1\r\n
0xb001b511 | END StateChanged event handler for Proxy Job with Guid %1\r\n
0xb001b512 | BEGIN StateChanged event handler for Proxy Child Job with Guid %1\r\n
0xb001b513 | END StateChanged event handler for Proxy Child Job with Guid %1\r\n
0xb001b514 | BEGIN Running garbage collection\r\n
0xb001b515 | END Running garbage collection\r\n
0xb001b516 | Persistence store has reached its maximum specified size\r\n
0xb001c000 | %1\r\n
0xb001c001 | Trace Information: %n %1 %2\r\n
0xb001d001 | Scheduled Job %1 started at %2 %n\r\n
0xb001d002 | Scheduled Job %1 completed at %2 with state %3 %n\r\n
0xb001d003 | Scheduled Job Exception %1: %n Message: %2 %n StackTrace: %3 %n InnerException: %4 %n\r\n
0xb001d100 | Windows PowerShell has started an IPC listening thread on process: %1 in AppDomain: %2.\r\n
0xb001d101 | Windows PowerShell has ended an IPC listening thread on process: %1 in AppDomain: %2.\r\n
0xb001d102 | An error has occurred in Windows PowerShell IPC listening thread on process: %1 in AppDomain: %2.  Error Message: %3.\r\n
0xb001d103 | Windows PowerShell IPC connect on process: %1 in AppDomain: %2 for User: %3.\r\n
0xb001d104 | Windows PowerShell IPC disconnect on process: %1 in AppDomain: %2 for User: %3.\r\n
0xd0000001 | AllPublicProperties\r\n
0xd0000002 | String\r\n
0xd0000003 | SpecificProperties\r\n
0xd0000004 | InvalidTargetInterface\r\n
0xd0000005 | Session\r\n
0xd0000006 | RunspacePool\r\n
0xd0000007 | PowerShell\r\n
0xd0000008 | InvalidDataType\r\n
0xd0000009 | ExceptionAsErrorRecord\r\n
0xd000000a | SessionConfiguration\r\n
0xd000000b | SessionConfigurationRequest\r\n
0xd000000c | SessionCapability\r\n
0xd000000d | CloseSession\r\n
0xd000000e | CreateRunspacePool\r\n
0xd000000f | SetMaxRunspaces\r\n
0xd0000010 | SetMinRunspaces\r\n
0xd0000011 | RunspacePoolOperationResponse\r\n
0xd0000012 | RunspacePoolStateInfo\r\n
0xd0000013 | CreatePowerShell\r\n
0xd0000014 | AvailableRunspaces\r\n
0xd0000015 | PSEventArgs\r\n
0xd0000016 | RemoteHostCallUsingRunspaceHost\r\n
0xd0000017 | RemoteRunspaceHostResponseData\r\n
0xd0000018 | PowerShellInput\r\n
0xd0000019 | PowerShellInputEnd\r\n
0xd000001a | PowerShellOutput\r\n
0xd000001b | PowerShellErrorRecord\r\n
0xd000001c | PowerShellStateInfo\r\n
0xd000001d | PowerShellDebug\r\n
0xd000001e | PowerShellVerbose\r\n
0xd000001f | PowerShellWarning\r\n
0xd0000020 | PowerShellProgress\r\n
0xd0000021 | StopPowerShell\r\n
0xd0000022 | RemoteHostCallUsingPowerShellHost\r\n
0xd0000023 | RemotePowerShellHostResponseData\r\n
0xf0000001 | WSMAN_FLAG_NO_AUTHENTICATION\r\n
0xf0000002 | WSMAN_FLAG_AUTH_DIGEST\r\n
0xf0000003 | WSMAN_FLAG_AUTH_NEGOTIATE\r\n
0xf0000004 | WSMAN_FLAG_AUTH_BASIC\r\n
0xf0000005 | WSMAN_FLAG_AUTH_KERBEROS\r\n
0xf0000006 | WSMAN_FLAG_AUTH_CLIENT_CERTIFICATE\r\n
0xf0000007 | WSMAN_FLAG_AUTH_CREDSSP\r\n
0xf0000008 | Client\r\n
0xf0000009 | Server\r\n
0xf000000a | Listener\r\n
