## coremessaging.dll

Path: %SystemRoot%\system32\CoreMessaging.dll

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000016 | CUI CoreUIService\r\n
0x10000021 | CUI MessagingPerformance\r\n
0x10000022 | CUI Session\r\n
0x10000023 | CUI Dispatcher\r\n
0x10000024 | CUI RegistrarClient\r\n
0x10000025 | CUI Messaging\r\n
0x10000026 | CUI Proxy\r\n
0x1000002b | CUI SelfHostInfo\r\n
0x1000002c | CUI SelfHostError\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb00003e8 | CoreUI ETW - Initialized (pid=%1)\r\n
0xb00003e9 | CoreUI ETW - Uninitialized (pid=%1)\r\n
0xb000041a | CoreUI System - Out of Memory!\r\n
0xb0000b54 | CoreUI Service server-thread started (serviceType=%1)\r\n
0xb0000b55 | CoreUI Service server-thread exiting (serviceType=%1)\r\n
0xb0000b56 | CoreUI InitializeService called (serviceType=%1)\r\n
0xb0000b57 | CoreUI UninitializeService called (serviceType=%1)\r\n
0xb0000b58 | CoreUI ServiceObjectCreated called (serviceType=%1)\r\n
0xb0000b59 | CoreUI ServiceObjectDestroyed called (serviceType=%1)\r\n
0xb0000b5a | CoreUI UpdateServiceStatus called (serviceType=%1)\r\n
0xb0000b5b | CoreUI ServiceObjectServiceMain called (serviceType=%1)\r\n
0xb0000b5c | CoreUI CoreUI ServiceMain called with unknown service name %1\r\n
0xb0000c1c | Session - CoreUICreate - Start\r\n
0xb0000c1d | Session - CoreUICreate - Stop\r\n
0xb0000c8e | Dispatcher - DispatchItem - Start (internalPriority=%1)\r\n
0xb0000c8f | Dispatcher - DispatchItem - Stop (internalPriority=%1)\r\n
0xb0000c90 | Dispatcher - WakeLevel - UpdateWakeLevel (bits=%1 old=%2 new=%3)\r\n
0xb0000c94 | Dispatcher - DoWait - Start (timeout=%1)\r\n
0xb0000c95 | Dispatcher - DoWait - Stop (status=%1 handle=%2)\r\n
0xb0000c96 | Dispatcher - CallDispatchCallback - Start (awake=%1 reference=%2)\r\n
0xb0000c97 | Dispatcher - CallDispatchCallback - Stop            (timeout=%1)\r\n
0xb0000c98 | UserAdapter - ScheduleDispatch (userPriority=%1)\r\n
0xb0000c99 | UserAdapter - HostModeRun - Start (runMode=%1 stopping=%2)\r\n
0xb0000c9a | UserAdapter - HostModeRun - Stop (stopCookie=%1)\r\n
0xb0000c9b | UserAdapter - OnUserDispatch - Start (priority=%1)\r\n
0xb0000c9c | UserAdapter - OnUserDispatch - Stop (discarded? %1)\r\n
0xb0000c9d | UserAdapter - IntegratedLoopWait - Start\r\n
0xb0000c9e | UserAdapter - IntegratedLoopWait - Stop\r\n
0xb0000c9f | UserAdapter - PostMessage - Failed due to post message queue full\r\n
0xb0000ce4 | RegistrarClient - Initialize - Start\r\n
0xb0000ce5 | RegistrarClient - Initialize - Stop\r\n
0xb0000faa | Messaging - CreateConnection - Start (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fab | Messaging - CreateConnection - Stop (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fb4 | Messaging - AllocatedMessage (externalPriority=%1; size=%2; destProcessId=%3; destThreadId=%4)\r\n
0xb0000fb6 | Messaging - FlushPendingStreams - Start (externalPriority=%1)\r\n
0xb0000fb7 | Messaging - FlushPendingStreams - Stop\r\n
0xb0000fbf | Messaging - LocalReceive - Statistics (messages=%1; size=%2)\r\n
0xb0000fc9 | Messaging - InterconnectSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fca | Messaging - InterconnectFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcb | Messaging - InterconnectFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcd | Messaging - InterconnectReceive - Statistics (senderTid=%1; messages=%2; size=%3)\r\n
0xb0000fd3 | Messaging - AlpcSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fd4 | Messaging - AlpcFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd5 | Messaging - AlpcFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd7 | Messaging - AlpcReceive - Statistics (senderPid=%1; senderTid=%2; messages=%3; size=%4)\r\n
0xb00013ba | Proxy - Message Method (%1)\r\n
0xb00013bc | Proxy - Message Event (%1)\r\n
0xb00013be | Proxy - Property Update (%1)\r\n
0xb0001b58 | CoreMessagingRegistrar ObjectRegistered '%1'(scope %2 pid %3 tid %4 object type %5)\r\n
0xb0001b59 | CoreMessagingRegistrar ObjectRevoked '%1' (scope %2 pid %3 tid %4 Orphaned=%5)\r\n
0xb0001b5a | CoreUI server disconnected pid %1 tid %2 id %3\r\n
0xb0001b5b | Conversation %1 has run out of PeerID handles to allocate\r\n
0xb0001b5c | Client connection to conversation '%1' failed, max clients already connected\r\n
0xb0004e20 | CoreUI SelfHostError - ThrownException (type=%1; hr=%2; message=%3)\r\n
0xb0004e21 | CoreMessagingRegistrar Object '%1' not found (scope=%2)\r\n
0xb0004e22 | CoreUI Connection failed to pid %1 tid %2 id %3\r\n
0xb0004e23 | CoreUI forcibly disconnecting client pid %1 tid %2\r\n
0xb0004e24 | CoreUI NtAlpcConnectPort '%1' failed with hr=%2\r\n
0xb0004e25 | CoreMessagingRegistrar Conversation '%1' not found\r\n
0xd0000001 | Invalid\r\n
0xd0000002 | Registrar\r\n
0xd0000003 | Dormant\r\n
0xd0000004 | WaitForNewEvents\r\n
0xd0000005 | SynchronizeWait\r\n
0xd0000006 | SendMessagesLow\r\n
0xd0000007 | Low\r\n
0xd0000008 | SendMessagesNormal\r\n
0xd0000009 | SynchronizeOutput\r\n
0xd000000a | Normal\r\n
0xd000000b | SynchronizeInput\r\n
0xd000000c | ReceiveMessages\r\n
0xd000000d | DeliverTimeouts\r\n
0xd000000e | SendMessagesHigh\r\n
0xd000000f | High\r\n
0xd0000010 | Infinite\r\n
0xd0000011 | Dormant\r\n
0xd0000012 | Low\r\n
0xd0000013 | SynchronizeOutput\r\n
0xd0000014 | Normal\r\n
0xd0000015 | High\r\n
0xd0000016 | None\r\n
0xd0000017 | RunUntilExit\r\n
0xd0000018 | RunAllIfPresent\r\n
0xd0000019 | RunToIdle\r\n
0xd000001a | RunSendOnly\r\n
0xd000001b | FlushAtShutdown\r\n
0xd000001c | Dormant\r\n
0xd000001d | Timer\r\n
0xd000001e | Paint\r\n
0xd000001f | Input\r\n
0xd0000020 | Post\r\n
0xd0000021 | Send\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000016 | CoreMessaging CoreUIService\r\n
0x10000021 | CoreMessaging MessagingPerformance\r\n
0x10000022 | CoreMessaging Session\r\n
0x10000023 | CoreMessaging Dispatcher\r\n
0x10000024 | CoreMessaging RegistrarClient\r\n
0x10000025 | CoreMessaging Messaging\r\n
0x10000026 | CoreMessaging Formatting\r\n
0x1000002b | CoreMessaging SelfHostInfo\r\n
0x1000002c | CoreMessaging SelfHostError\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb00003e8 | CoreUI ETW - Initialized (pid=%1)\r\n
0xb00003e9 | CoreUI ETW - Uninitialized (pid=%1)\r\n
0xb000041a | CoreUI System - Out of Memory!\r\n
0xb0000b54 | CoreUI Service server-thread started (serviceType=%1)\r\n
0xb0000b55 | CoreUI Service server-thread exiting (serviceType=%1)\r\n
0xb0000b56 | CoreUI InitializeService called (serviceType=%1)\r\n
0xb0000b57 | CoreUI UninitializeService called (serviceType=%1)\r\n
0xb0000b58 | CoreUI ServiceObjectCreated called (serviceType=%1)\r\n
0xb0000b59 | CoreUI ServiceObjectDestroyed called (serviceType=%1)\r\n
0xb0000b5a | CoreUI UpdateServiceStatus called (serviceType=%1)\r\n
0xb0000b5b | CoreUI ServiceObjectServiceMain called (serviceType=%1)\r\n
0xb0000b5c | CoreUI CoreUI ServiceMain called with unknown service name %1\r\n
0xb0000c1c | Session - CoreUICreate - Start\r\n
0xb0000c1d | Session - CoreUICreate - Stop\r\n
0xb0000c8e | Dispatcher - DispatchItem - Start (internalPriority=%1)\r\n
0xb0000c8f | Dispatcher - DispatchItem - Stop (internalPriority=%1)\r\n
0xb0000c90 | Dispatcher - WakeLevel - UpdateWakeLevel (bits=%1 old=%2 new=%3)\r\n
0xb0000c94 | Dispatcher - DoWait - Start (timeout=%1)\r\n
0xb0000c95 | Dispatcher - DoWait - Stop (status=%1 handle=%2)\r\n
0xb0000c96 | Dispatcher - CallDispatchCallback - Start (awake=%1 reference=%2)\r\n
0xb0000c97 | Dispatcher - CallDispatchCallback - Stop            (timeout=%1)\r\n
0xb0000c98 | UserAdapter - ScheduleDispatch (threadid=%1 userPriority=%2)\r\n
0xb0000c99 | UserAdapter - HostModeRun - Start (runMode=%1 stopping=%2)\r\n
0xb0000c9a | UserAdapter - HostModeRun - Stop (stopCookie=%1)\r\n
0xb0000c9b | UserAdapter - OnUserDispatch - Start (priority=%1)\r\n
0xb0000c9c | UserAdapter - OnUserDispatch - Stop (discarded? %1)\r\n
0xb0000c9d | UserAdapter - IntegratedLoopWait - Start\r\n
0xb0000c9e | UserAdapter - IntegratedLoopWait - Stop\r\n
0xb0000c9f | UserAdapter - PostMessage - Failed due to post message queue full\r\n
0xb0000ce4 | RegistrarClient - Initialize - Start\r\n
0xb0000ce5 | RegistrarClient - Initialize - Stop\r\n
0xb0000faa | Messaging - CreateConnection - Start (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fab | Messaging - CreateConnection - Stop (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fb4 | Messaging - AllocatedMessage (externalPriority=%1; size=%2; destProcessId=%3; destThreadId=%4)\r\n
0xb0000fb5 | Messaging - Message stream dirty (processId=%1 threadId=%2)\r\n
0xb0000fb6 | Messaging - FlushPendingStreams - Start (externalPriority=%1)\r\n
0xb0000fb7 | Messaging - FlushPendingStreams - Stop\r\n
0xb0000fbf | Messaging - LocalReceive - Statistics (messages=%1; size=%2)\r\n
0xb0000fc9 | Messaging - InterconnectSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fca | Messaging - InterconnectFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcb | Messaging - InterconnectFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcd | Messaging - InterconnectReceive - Statistics (senderTid=%1; messages=%2; size=%3)\r\n
0xb0000fd3 | Messaging - AlpcSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fd4 | Messaging - AlpcFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd5 | Messaging - AlpcFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd7 | Messaging - AlpcReceive - Statistics (senderPid=%1; senderTid=%2; messages=%3; size=%4)\r\n
0xb00013ba | Formatting - Message Method (%1)\r\n
0xb0001b58 | CoreMessagingRegistrar ObjectRegistered '%1' (type %2 scope %3 pid %4 tid %5)\r\n
0xb0001b59 | CoreMessagingRegistrar ObjectRevoked '%1' (type %2 scope %3 pid %4 tid %5 Orphaned=%6)\r\n
0xb0001b5a | CoreUI server disconnected pid %1 tid %2 id %3\r\n
0xb0001b5b | Conversation %1 has run out of PeerID handles to allocate\r\n
0xb0001b5c | Client connection to conversation '%1' failed, max clients already connected\r\n
0xb0004e20 | CoreUI SelfHostError - ThrownException (type=%1; hr=%2; message=%3)\r\n
0xb0004e21 | CoreMessagingRegistrar Object '%1' not found (type=%2; scope=%3)\r\n
0xb0004e22 | CoreUI Connection failed to pid %1 tid %2 id %3\r\n
0xb0004e23 | CoreUI forcibly disconnecting client pid %1 tid %2\r\n
0xb0004e24 | CoreUI NtAlpcConnectPort '%1' failed with hr=%2\r\n
0xb0004e25 | CoreMessagingRegistrar Conversation '%1' not found\r\n
0xd0000001 | Invalid\r\n
0xd0000002 | Registrar\r\n
0xd0000003 | Dormant\r\n
0xd0000004 | WaitForNewEvents\r\n
0xd0000005 | SynchronizeWait\r\n
0xd0000006 | SendMessagesLow\r\n
0xd0000007 | Low\r\n
0xd0000008 | SendMessagesNormal\r\n
0xd0000009 | SynchronizeOutput\r\n
0xd000000a | Normal\r\n
0xd000000b | SynchronizeInput\r\n
0xd000000c | ReceiveMessages\r\n
0xd000000d | DeliverTimeouts\r\n
0xd000000e | SendMessagesHigh\r\n
0xd000000f | High\r\n
0xd0000010 | Infinite\r\n
0xd0000011 | Dormant\r\n
0xd0000012 | Low\r\n
0xd0000013 | SynchronizeOutput\r\n
0xd0000014 | Normal\r\n
0xd0000015 | High\r\n
0xd0000016 | None\r\n
0xd0000017 | RunUntilExit\r\n
0xd0000018 | RunAllIfPresent\r\n
0xd0000019 | RunToIdle\r\n
0xd000001a | RunSendOnly\r\n
0xd000001b | FlushAtShutdown\r\n
0xd000001c | Dormant\r\n
0xd000001d | Timer\r\n
0xd000001e | Paint\r\n
0xd000001f | Input\r\n
0xd0000020 | Post\r\n
0xd0000021 | Send\r\n
0xd0000022 | Endpoint\r\n
0xd0000023 | CrossProcessReceivePort\r\n
0xd0000024 | Conversation\r\n
0xd0000025 | MessageObject\r\n
0xd0000026 | Local\r\n
0xd0000027 | System\r\n
0xd0000028 | Process\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000016 | CoreMessaging CoreUIService\r\n
0x10000021 | CoreMessaging MessagingPerformance\r\n
0x10000022 | CoreMessaging Session\r\n
0x10000023 | CoreMessaging Dispatcher\r\n
0x10000024 | CoreMessaging RegistrarClient\r\n
0x10000025 | CoreMessaging Messaging\r\n
0x10000026 | CoreMessaging Formatting\r\n
0x1000002b | CoreMessaging SelfHostInfo\r\n
0x1000002c | CoreMessaging SelfHostError\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb00003e8 | CoreUI ETW - Initialized (pid=%1)\r\n
0xb00003e9 | CoreUI ETW - Uninitialized (pid=%1)\r\n
0xb000041a | CoreUI System - Out of Memory!\r\n
0xb0000b54 | CoreUI Service server-thread started (serviceType=%1)\r\n
0xb0000b55 | CoreUI Service server-thread exiting (serviceType=%1)\r\n
0xb0000b56 | CoreUI InitializeService called (serviceType=%1)\r\n
0xb0000b57 | CoreUI UninitializeService called (serviceType=%1)\r\n
0xb0000b58 | CoreUI ServiceObjectCreated called (serviceType=%1)\r\n
0xb0000b59 | CoreUI ServiceObjectDestroyed called (serviceType=%1)\r\n
0xb0000b5a | CoreUI UpdateServiceStatus called (serviceType=%1)\r\n
0xb0000b5b | CoreUI ServiceObjectServiceMain called (serviceType=%1)\r\n
0xb0000b5c | CoreUI CoreUI ServiceMain called with unknown service name %1\r\n
0xb0000c1c | Session - CoreUICreate - Start\r\n
0xb0000c1d | Session - CoreUICreate - Stop\r\n
0xb0000c8e | Dispatcher - DispatchItem - Start (internalPriority=%1)\r\n
0xb0000c8f | Dispatcher - DispatchItem - Stop (internalPriority=%1)\r\n
0xb0000c90 | Dispatcher - WakeLevel - UpdateWakeLevel (bits=%1 old=%2 new=%3)\r\n
0xb0000c94 | Dispatcher - DoWait - Start (timeout=%1)\r\n
0xb0000c95 | Dispatcher - DoWait - Stop (status=%1 handle=%2)\r\n
0xb0000c96 | Dispatcher - CallDispatchCallback - Start (awake=%1 reference=%2)\r\n
0xb0000c97 | Dispatcher - CallDispatchCallback - Stop            (timeout=%1)\r\n
0xb0000c98 | UserAdapter - ScheduleDispatch (threadid=%1 userPriority=%2)\r\n
0xb0000c99 | UserAdapter - HostModeRun - Start (runMode=%1 stopping=%2)\r\n
0xb0000c9a | UserAdapter - HostModeRun - Stop (stopCookie=%1)\r\n
0xb0000c9b | UserAdapter - OnUserDispatch - Start (priority=%1)\r\n
0xb0000c9c | UserAdapter - OnUserDispatch - Stop (discarded? %1)\r\n
0xb0000c9d | UserAdapter - IntegratedLoopWait - Start\r\n
0xb0000c9e | UserAdapter - IntegratedLoopWait - Stop\r\n
0xb0000c9f | UserAdapter - PostMessage - Failed due to post message queue full\r\n
0xb0000ca0 | UserAdapter - PostMessage - User failed to schedule an asynchronous DISPATCHNOTIFY_COMPLETION\r\n
0xb0000ce4 | RegistrarClient - Initialize - Start\r\n
0xb0000ce5 | RegistrarClient - Initialize - Stop\r\n
0xb0000faa | Messaging - CreateConnection - Start (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fab | Messaging - CreateConnection - Stop (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fb4 | Messaging - AllocatedMessage (externalPriority=%1; size=%2; destProcessId=%3; destThreadId=%4)\r\n
0xb0000fb5 | Messaging - Message stream dirty (processId=%1 threadId=%2)\r\n
0xb0000fb6 | Messaging - FlushPendingStreams - Start (externalPriority=%1)\r\n
0xb0000fb7 | Messaging - FlushPendingStreams - Stop\r\n
0xb0000fbf | Messaging - LocalReceive - Statistics (messages=%1; size=%2)\r\n
0xb0000fc9 | Messaging - InterconnectSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fca | Messaging - InterconnectFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcb | Messaging - InterconnectFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcd | Messaging - InterconnectReceive - Statistics (senderTid=%1; messages=%2; size=%3)\r\n
0xb0000fd3 | Messaging - AlpcSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fd4 | Messaging - AlpcFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd5 | Messaging - AlpcFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd7 | Messaging - AlpcReceive - Statistics (senderPid=%1; senderTid=%2; messages=%3; size=%4)\r\n
0xb00013ba | Formatting - Message Method (%1)\r\n
0xb0001b58 | CoreMessagingRegistrar ObjectRegistered '%1' (type %2 scope %3 pid %4 tid %5)\r\n
0xb0001b59 | CoreMessagingRegistrar ObjectRevoked '%1' (type %2 scope %3 pid %4 tid %5 Orphaned=%6)\r\n
0xb0001b5a | CoreUI server disconnected pid %1 tid %2 id %3\r\n
0xb0001b5b | Conversation %1 has run out of PeerID handles to allocate\r\n
0xb0001b5c | Client connection to conversation '%1' failed, max clients already connected\r\n
0xb0001f40 | NtAssociateWaitCompletionPacket succeeded: packet %1 target %2 context %3\r\n
0xb0001f41 | NtAssociateWaitCompletionPacket failed, packet %1 port %2 handle %3 status %4\r\n
0xb0001f42 | NtCancelWaitCompletionPacket results: packet %1 status %2 signaled %3 canceled %4\r\n
0xb0001f43 | Created RegisteredWait: packet %1 target %2 cloned %3\r\n
0xb0001f44 | UserAdapter HandleCompletion: packet %1 target %2\r\n
0xb0004e20 | CoreUI SelfHostError - ThrownException (type=%1; hr=%2; message=%3)\r\n
0xb0004e21 | CoreMessagingRegistrar Object '%1' not found (type=%2; scope=%3)\r\n
0xb0004e22 | CoreUI Connection failed to pid %1 tid %2 id %3\r\n
0xb0004e23 | CoreUI forcibly disconnecting client pid %1 tid %2\r\n
0xb0004e24 | CoreUI NtAlpcConnectPort '%1' failed with hr=%2\r\n
0xb0004e25 | CoreMessagingRegistrar Conversation '%1' not found\r\n
0xd0000001 | Invalid\r\n
0xd0000002 | Registrar\r\n
0xd0000003 | Dormant\r\n
0xd0000004 | WaitForNewEvents\r\n
0xd0000005 | SynchronizeWait\r\n
0xd0000006 | SendMessagesLow\r\n
0xd0000007 | Low\r\n
0xd0000008 | SendMessagesNormal\r\n
0xd0000009 | SynchronizeOutput\r\n
0xd000000a | Normal\r\n
0xd000000b | SynchronizeInput\r\n
0xd000000c | ReceiveMessagesNormal\r\n
0xd000000d | ReceiveMessagesHigh\r\n
0xd000000e | DeliverTimeouts\r\n
0xd000000f | SendMessagesHigh\r\n
0xd0000010 | High\r\n
0xd0000011 | Infinite\r\n
0xd0000012 | Dormant\r\n
0xd0000013 | Low\r\n
0xd0000014 | SynchronizeOutput\r\n
0xd0000015 | Normal\r\n
0xd0000016 | High\r\n
0xd0000017 | None\r\n
0xd0000018 | RunUntilExit\r\n
0xd0000019 | RunAllIfPresent\r\n
0xd000001a | RunToIdle\r\n
0xd000001b | RunSendOnly\r\n
0xd000001c | FlushAtShutdown\r\n
0xd000001d | Dormant\r\n
0xd000001e | Timer\r\n
0xd000001f | Paint\r\n
0xd0000020 | Input\r\n
0xd0000021 | Post\r\n
0xd0000022 | Send\r\n
0xd0000023 | Endpoint\r\n
0xd0000024 | CrossProcessReceivePort\r\n
0xd0000025 | Conversation\r\n
0xd0000026 | MessageObject\r\n
0xd0000027 | Local\r\n
0xd0000028 | System\r\n
0xd0000029 | Process\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000016 | CoreMessaging CoreUIService\r\n
0x10000021 | CoreMessaging MessagingPerformance\r\n
0x10000022 | CoreMessaging Session\r\n
0x10000023 | CoreMessaging Dispatcher\r\n
0x10000024 | CoreMessaging RegistrarClient\r\n
0x10000025 | CoreMessaging Messaging\r\n
0x10000026 | CoreMessaging Formatting\r\n
0x1000002b | CoreMessaging SelfHostInfo\r\n
0x1000002c | CoreMessaging SelfHostError\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb00003e8 | CoreUI ETW - Initialized (pid=%1)\r\n
0xb00003e9 | CoreUI ETW - Uninitialized (pid=%1)\r\n
0xb000041a | CoreUI System - Out of Memory!\r\n
0xb0000b54 | CoreUI Service server-thread started (serviceType=%1)\r\n
0xb0000b55 | CoreUI Service server-thread exiting (serviceType=%1)\r\n
0xb0000b56 | CoreUI InitializeService called (serviceType=%1)\r\n
0xb0000b57 | CoreUI UninitializeService called (serviceType=%1)\r\n
0xb0000b58 | CoreUI ServiceObjectCreated called (serviceType=%1)\r\n
0xb0000b59 | CoreUI ServiceObjectDestroyed called (serviceType=%1)\r\n
0xb0000b5a | CoreUI UpdateServiceStatus called (serviceType=%1)\r\n
0xb0000b5b | CoreUI ServiceObjectServiceMain called (serviceType=%1)\r\n
0xb0000b5c | CoreUI CoreUI ServiceMain called with unknown service name %1\r\n
0xb0000c1c | Session - CoreUICreate - Start\r\n
0xb0000c1d | Session - CoreUICreate - Stop\r\n
0xb0000c8e | Dispatcher - DispatchItem - Start (internalPriority=%1)\r\n
0xb0000c8f | Dispatcher - DispatchItem - Stop (internalPriority=%1)\r\n
0xb0000c90 | Dispatcher - WakeLevel - UpdateWakeLevel (bits=%1 old=%2 new=%3)\r\n
0xb0000c94 | Dispatcher - DoWait - Start (timeout=%1)\r\n
0xb0000c95 | Dispatcher - DoWait - Stop (status=%1 handle=%2)\r\n
0xb0000c96 | Dispatcher - CallDispatchCallback - Start (awake=%1 reference=%2)\r\n
0xb0000c97 | Dispatcher - CallDispatchCallback - Stop            (timeout=%1)\r\n
0xb0000c98 | UserAdapter - ScheduleDispatch (threadid=%1 userPriority=%2)\r\n
0xb0000c99 | UserAdapter - HostModeRun - Start (runMode=%1 stopping=%2)\r\n
0xb0000c9a | UserAdapter - HostModeRun - Stop (stopCookie=%1)\r\n
0xb0000c9b | UserAdapter - OnUserDispatch - Start (priority=%1)\r\n
0xb0000c9c | UserAdapter - OnUserDispatch - Stop (discarded? %1)\r\n
0xb0000c9d | UserAdapter - IntegratedLoopWait - Start\r\n
0xb0000c9e | UserAdapter - IntegratedLoopWait - Stop\r\n
0xb0000c9f | UserAdapter - PostMessage - Failed due to post message queue full\r\n
0xb0000ca0 | UserAdapter - PostMessage - User failed to schedule an asynchronous DISPATCHNOTIFY_COMPLETION\r\n
0xb0000ce4 | RegistrarClient - Initialize - Start\r\n
0xb0000ce5 | RegistrarClient - Initialize - Stop\r\n
0xb0000faa | Messaging - CreateConnection - Start (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fab | Messaging - CreateConnection - Stop (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fb4 | Messaging - AllocatedMessage (externalPriority=%1; size=%2; destProcessId=%3; destThreadId=%4)\r\n
0xb0000fb5 | Messaging - Message stream dirty (processId=%1 threadId=%2)\r\n
0xb0000fb6 | Messaging - FlushPendingStreams - Start (externalPriority=%1)\r\n
0xb0000fb7 | Messaging - FlushPendingStreams - Stop\r\n
0xb0000fbf | Messaging - LocalReceive - Statistics (messages=%1; size=%2)\r\n
0xb0000fc9 | Messaging - InterconnectSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fca | Messaging - InterconnectFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcb | Messaging - InterconnectFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcd | Messaging - InterconnectReceive - Statistics (senderTid=%1; messages=%2; size=%3)\r\n
0xb0000fd3 | Messaging - AlpcSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fd4 | Messaging - AlpcFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd5 | Messaging - AlpcFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd7 | Messaging - AlpcReceive - Statistics (senderPid=%1; senderTid=%2; messages=%3; size=%4)\r\n
0xb00013ba | Formatting - Message Method (%1)\r\n
0xb0001b58 | CoreMessagingRegistrar ObjectRegistered '%1' (type %2 scope %3 session %4 pid %5 tid %6)\r\n
0xb0001b59 | CoreMessagingRegistrar ObjectRevoked '%1' (type %2 scope %3 session %4 pid %5 tid %6 Orphaned=%7)\r\n
0xb0001b5a | CoreUI server disconnected pid %1 tid %2 id %3\r\n
0xb0001b5b | Conversation %1 has run out of PeerID handles to allocate\r\n
0xb0001b5c | Client connection to conversation '%1' failed, max clients already connected\r\n
0xb0001b5d | IdentityTable uniqueness bits protected us: index %1  requestedUniq %2  currentUniq %3\r\n
0xb0001b5e | IdentityTable uniqueness bits reached max for slot index %1\r\n
0xb0001b5f | IdentityTable slot %1 passed over (diff: %2)\r\n
0xb0001b60 | IdentityTable grown to max index %1 (after %2 times through the loop).\r\n
0xb0001f40 | NtAssociateWaitCompletionPacket succeeded: packet %1 target %2 context %3\r\n
0xb0001f41 | NtAssociateWaitCompletionPacket failed, packet %1 port %2 handle %3 status %4\r\n
0xb0001f42 | NtCancelWaitCompletionPacket results: packet %1 status %2 signaled %3 canceled %4\r\n
0xb0001f43 | Created RegisteredWait: packet %1 target %2 cloned %3\r\n
0xb0001f44 | UserAdapter HandleCompletion: packet %1 target %2\r\n
0xb0004e20 | CoreUI SelfHostError - ThrownException (type=%1; hr=%2; message=%3)\r\n
0xb0004e21 | CoreMessagingRegistrar Object '%1' not found (type=%2; scope=%3)\r\n
0xb0004e22 | CoreUI Connection failed to pid %1 tid %2 id %3\r\n
0xb0004e23 | CoreUI forcibly disconnecting client pid %1 tid %2\r\n
0xb0004e24 | CoreUI NtAlpcConnectPort '%1' failed with hr=%2\r\n
0xb0004e25 | CoreMessagingRegistrar Conversation '%1' not found\r\n
0xd0000001 | Invalid\r\n
0xd0000002 | Registrar\r\n
0xd0000003 | Dormant\r\n
0xd0000004 | WaitForNewEvents\r\n
0xd0000005 | SendMessagesLow\r\n
0xd0000006 | Low\r\n
0xd0000007 | SendMessagesNormal\r\n
0xd0000008 | SynchronizeOutput\r\n
0xd0000009 | Normal\r\n
0xd000000a | SynchronizeInput\r\n
0xd000000b | ReceiveMessagesNormal\r\n
0xd000000c | ReceiveDeferredMessagesNormal\r\n
0xd000000d | DeliverTimeouts\r\n
0xd000000e | SendMessagesHigh\r\n
0xd000000f | High\r\n
0xd0000010 | ReceiveMessagesHigh\r\n
0xd0000011 | ReceiveDeferredMessagesHigh\r\n
0xd0000012 | Infinite\r\n
0xd0000013 | Dormant\r\n
0xd0000014 | Low\r\n
0xd0000015 | SynchronizeOutput\r\n
0xd0000016 | Normal\r\n
0xd0000017 | High\r\n
0xd0000018 | None\r\n
0xd0000019 | RunUntilExit\r\n
0xd000001a | RunAllIfPresent\r\n
0xd000001b | RunToIdle\r\n
0xd000001c | RunSendOnly\r\n
0xd000001d | FlushAtShutdown\r\n
0xd000001e | Dormant\r\n
0xd000001f | Timer\r\n
0xd0000020 | Paint\r\n
0xd0000021 | Input\r\n
0xd0000022 | Post\r\n
0xd0000023 | Send\r\n
0xd0000024 | Endpoint\r\n
0xd0000025 | CrossProcessReceivePort\r\n
0xd0000026 | Conversation\r\n
0xd0000027 | MessageObject\r\n
0xd0000028 | Local\r\n
0xd0000029 | System\r\n
0xd000002a | Process\r\n

### 10.0.17134.1, 10.0.17763.194

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000016 | CoreMessaging CoreUIService\r\n
0x10000021 | CoreMessaging MessagingPerformance\r\n
0x10000022 | CoreMessaging Session\r\n
0x10000023 | CoreMessaging Dispatcher\r\n
0x10000024 | CoreMessaging RegistrarClient\r\n
0x10000025 | CoreMessaging Messaging\r\n
0x10000026 | CoreMessaging Formatting\r\n
0x1000002b | CoreMessaging SelfHostInfo\r\n
0x1000002c | CoreMessaging SelfHostError\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb00003e8 | CoreUI ETW - Initialized (pid=%1)\r\n
0xb00003e9 | CoreUI ETW - Uninitialized (pid=%1)\r\n
0xb000041a | CoreUI System - Out of Memory!\r\n
0xb0000b54 | CoreUI Service server-thread started (serviceType=%1)\r\n
0xb0000b55 | CoreUI Service server-thread exiting (serviceType=%1)\r\n
0xb0000b56 | CoreUI InitializeService called (serviceType=%1)\r\n
0xb0000b57 | CoreUI UninitializeService called (serviceType=%1)\r\n
0xb0000b58 | CoreUI ServiceObjectCreated called (serviceType=%1)\r\n
0xb0000b59 | CoreUI ServiceObjectDestroyed called (serviceType=%1)\r\n
0xb0000b5a | CoreUI UpdateServiceStatus called (serviceType=%1)\r\n
0xb0000b5b | CoreUI ServiceObjectServiceMain called (serviceType=%1)\r\n
0xb0000b5c | CoreUI CoreUI ServiceMain called with unknown service name %1\r\n
0xb0000c1c | Session - CoreUICreate - Start\r\n
0xb0000c1d | Session - CoreUICreate - Stop\r\n
0xb0000c8e | Dispatcher - DispatchItem - Start (internalPriority=%1)\r\n
0xb0000c8f | Dispatcher - DispatchItem - Stop (internalPriority=%1)\r\n
0xb0000c90 | Dispatcher - WakeLevel - UpdateWakeLevel (bits=%1 old=%2 new=%3)\r\n
0xb0000c94 | Dispatcher - DoWait - Start (timeout=%1)\r\n
0xb0000c95 | Dispatcher - DoWait - Stop (status=%1 handle=%2)\r\n
0xb0000c96 | Dispatcher - CallDispatchCallback - Start (awake=%1 reference=%2)\r\n
0xb0000c97 | Dispatcher - CallDispatchCallback - Stop            (timeout=%1)\r\n
0xb0000c98 | UserAdapter - ScheduleDispatch (threadid=%1 userPriority=%2)\r\n
0xb0000c99 | UserAdapter - HostModeRun - Start (runMode=%1 stopping=%2)\r\n
0xb0000c9a | UserAdapter - HostModeRun - Stop (stopCookie=%1)\r\n
0xb0000c9b | UserAdapter - OnUserDispatch - Start (priority=%1)\r\n
0xb0000c9c | UserAdapter - OnUserDispatch - Stop (discarded? %1)\r\n
0xb0000c9d | UserAdapter - IntegratedLoopWait - Start\r\n
0xb0000c9e | UserAdapter - IntegratedLoopWait - Stop\r\n
0xb0000c9f | UserAdapter - PostMessage - Failed due to post message queue full\r\n
0xb0000ca0 | UserAdapter - PostMessage - User failed to schedule an asynchronous DISPATCHNOTIFY_COMPLETION\r\n
0xb0000ce4 | RegistrarClient - Initialize - Start\r\n
0xb0000ce5 | RegistrarClient - Initialize - Stop\r\n
0xb0000faa | Messaging - CreateConnection - Start (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fab | Messaging - CreateConnection - Stop (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fb4 | Messaging - AllocatedMessage (externalPriority=%1; size=%2; destProcessId=%3; destThreadId=%4)\r\n
0xb0000fb5 | Messaging - Message stream dirty (processId=%1 threadId=%2)\r\n
0xb0000fb6 | Messaging - FlushPendingStreams - Start (externalPriority=%1)\r\n
0xb0000fb7 | Messaging - FlushPendingStreams - Stop\r\n
0xb0000fbf | Messaging - LocalReceive - Statistics (messages=%1; size=%2)\r\n
0xb0000fc9 | Messaging - InterconnectSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fca | Messaging - InterconnectFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcb | Messaging - InterconnectFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcd | Messaging - InterconnectReceive - Statistics (senderTid=%1; messages=%2; size=%3)\r\n
0xb0000fd3 | Messaging - AlpcSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fd4 | Messaging - AlpcFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd5 | Messaging - AlpcFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd7 | Messaging - AlpcReceive - Statistics (senderPid=%1; senderTid=%2; messages=%3; size=%4)\r\n
0xb00013ba | Formatting - Message Method (%1)\r\n
0xb0001b58 | CoreMessagingRegistrar ObjectRegistered '%1' (type %2 scope %3 session %4 pid %5 tid %6)\r\n
0xb0001b59 | CoreMessagingRegistrar ObjectRevoked '%1' (type %2 scope %3 session %4 pid %5 tid %6 Orphaned=%7)\r\n
0xb0001b5a | CoreUI server disconnected pid %1 tid %2 id %3\r\n
0xb0001b5b | Conversation %1 has run out of PeerID handles to allocate\r\n
0xb0001b5c | Client connection to conversation '%1' failed, max clients already connected\r\n
0xb0001b5d | IdentityTable uniqueness bits protected us: index %1  requestedUniq %2  currentUniq %3\r\n
0xb0001b5e | IdentityTable uniqueness bits reached max for slot index %1\r\n
0xb0001b5f | IdentityTable slot %1 passed over (diff: %2)\r\n
0xb0001b60 | IdentityTable grown to max index %1 (after %2 times through the loop).\r\n
0xb0001f40 | NtAssociateWaitCompletionPacket succeeded: packet %1 target %2 context %3\r\n
0xb0001f41 | NtAssociateWaitCompletionPacket failed, packet %1 port %2 handle %3 status %4\r\n
0xb0001f42 | NtCancelWaitCompletionPacket results: packet %1 status %2 signaled %3 canceled %4\r\n
0xb0001f43 | Created RegisteredWait: packet %1 target %2 cloned %3\r\n
0xb0001f44 | UserAdapter HandleCompletion: packet %1 target %2\r\n
0xb0001f45 | Calling completion handler: ApcContext %1 KeyContext %2\r\n
0xb0001f46 | Removed end of batch completion.\r\n
0xb0001f47 | Removed completion: ApcContext %1 KeyContext %2\r\n
0xb0004e20 | CoreUI SelfHostError - ThrownException (type=%1; hr=%2; message=%3)\r\n
0xb0004e21 | CoreMessagingRegistrar Object '%1' not found (type=%2; scope=%3)\r\n
0xb0004e22 | CoreUI Connection failed to pid %1 tid %2 id %3\r\n
0xb0004e23 | CoreUI forcibly disconnecting client pid %1 tid %2\r\n
0xb0004e24 | CoreUI NtAlpcConnectPort '%1' failed with hr=%2\r\n
0xb0004e25 | CoreMessagingRegistrar Conversation '%1' not found\r\n
0xd0000001 | Invalid\r\n
0xd0000002 | Registrar\r\n
0xd0000003 | Dormant\r\n
0xd0000004 | WaitForNewEvents\r\n
0xd0000005 | SendMessagesLow\r\n
0xd0000006 | Low\r\n
0xd0000007 | SendMessagesNormal\r\n
0xd0000008 | SynchronizeOutput\r\n
0xd0000009 | Normal\r\n
0xd000000a | SynchronizeInput\r\n
0xd000000b | ReceiveMessagesNormal\r\n
0xd000000c | ReceiveDeferredMessagesNormal\r\n
0xd000000d | DeliverTimeouts\r\n
0xd000000e | SendMessagesHigh\r\n
0xd000000f | High\r\n
0xd0000010 | ReceiveMessagesHigh\r\n
0xd0000011 | ReceiveDeferredMessagesHigh\r\n
0xd0000012 | Infinite\r\n
0xd0000013 | Dormant\r\n
0xd0000014 | Low\r\n
0xd0000015 | SynchronizeOutput\r\n
0xd0000016 | Normal\r\n
0xd0000017 | High\r\n
0xd0000018 | None\r\n
0xd0000019 | RunUntilExit\r\n
0xd000001a | RunAllIfPresent\r\n
0xd000001b | RunToIdle\r\n
0xd000001c | RunSendOnly\r\n
0xd000001d | FlushAtShutdown\r\n
0xd000001e | Dormant\r\n
0xd000001f | Timer\r\n
0xd0000020 | Paint\r\n
0xd0000021 | Input\r\n
0xd0000022 | Post\r\n
0xd0000023 | Send\r\n
0xd0000024 | Endpoint\r\n
0xd0000025 | CrossProcessReceivePort\r\n
0xd0000026 | Conversation\r\n
0xd0000027 | Local\r\n
0xd0000028 | System\r\n
0xd0000029 | Process\r\n

### 10.0.18362.1, 10.0.18362.836

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000016 | CoreMessaging CoreUIService\r\n
0x10000021 | CoreMessaging MessagingPerformance\r\n
0x10000022 | CoreMessaging Session\r\n
0x10000023 | CoreMessaging Dispatcher\r\n
0x10000024 | CoreMessaging RegistrarClient\r\n
0x10000025 | CoreMessaging Messaging\r\n
0x10000026 | CoreMessaging Formatting\r\n
0x1000002b | CoreMessaging SelfHostInfo\r\n
0x1000002c | CoreMessaging SelfHostError\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb00003e8 | CoreUI ETW - Initialized (pid=%1)\r\n
0xb00003e9 | CoreUI ETW - Uninitialized (pid=%1)\r\n
0xb000041a | CoreUI System - Out of Memory!\r\n
0xb0000b54 | CoreUI Service server-thread started\r\n
0xb0000b55 | CoreUI Service server-thread exiting\r\n
0xb0000b56 | CoreUI InitializeService called\r\n
0xb0000b57 | CoreUI UninitializeService called\r\n
0xb0000b58 | CoreUI ServiceObjectCreated called\r\n
0xb0000b59 | CoreUI ServiceObjectDestroyed called\r\n
0xb0000b5a | CoreUI UpdateServiceStatus called\r\n
0xb0000b5b | CoreUI ServiceObjectServiceMain called\r\n
0xb0000b5c | CoreUI CoreUI ServiceMain called with unknown service name %1\r\n
0xb0000c1c | Session - CoreUICreate - Start\r\n
0xb0000c1d | Session - CoreUICreate - Stop\r\n
0xb0000c8e | Dispatcher - DispatchItem - Start (internalPriority=%1)\r\n
0xb0000c8f | Dispatcher - DispatchItem - Stop (internalPriority=%1)\r\n
0xb0000c90 | Dispatcher - WakeLevel - UpdateWakeLevel (bits=%1 old=%2 new=%3)\r\n
0xb0000c94 | Dispatcher - DoWait - Start (timeout=%1)\r\n
0xb0000c95 | Dispatcher - DoWait - Stop (status=%1 handle=%2)\r\n
0xb0000c96 | Dispatcher - CallDispatchCallback - Start (awake=%1 reference=%2)\r\n
0xb0000c97 | Dispatcher - CallDispatchCallback - Stop            (timeout=%1)\r\n
0xb0000c98 | UserAdapter - ScheduleDispatch (threadid=%1 userPriority=%2)\r\n
0xb0000c99 | UserAdapter - HostModeRun - Start (runMode=%1 stopping=%2)\r\n
0xb0000c9a | UserAdapter - HostModeRun - Stop (stopCookie=%1)\r\n
0xb0000c9b | UserAdapter - OnUserDispatch - Start (priority=%1)\r\n
0xb0000c9c | UserAdapter - OnUserDispatch - Stop (discarded? %1)\r\n
0xb0000c9d | UserAdapter - IntegratedLoopWait - Start\r\n
0xb0000c9e | UserAdapter - IntegratedLoopWait - Stop\r\n
0xb0000c9f | UserAdapter - PostMessage - Failed due to post message queue full\r\n
0xb0000ca0 | UserAdapter - PostMessage - User failed to schedule an asynchronous DISPATCHNOTIFY_COMPLETION\r\n
0xb0000ce4 | RegistrarClient - Initialize - Start\r\n
0xb0000ce5 | RegistrarClient - Initialize - Stop\r\n
0xb0000faa | Messaging - CreateConnection - Start (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fab | Messaging - CreateConnection - Stop (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fb4 | Messaging - AllocatedMessage (externalPriority=%1; size=%2; destProcessId=%3; destThreadId=%4)\r\n
0xb0000fb5 | Messaging - Message stream dirty (processId=%1 threadId=%2)\r\n
0xb0000fb6 | Messaging - FlushPendingStreams - Start (externalPriority=%1)\r\n
0xb0000fb7 | Messaging - FlushPendingStreams - Stop\r\n
0xb0000fbf | Messaging - LocalReceive - Statistics (messages=%1; size=%2)\r\n
0xb0000fc9 | Messaging - InterconnectSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fca | Messaging - InterconnectFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcb | Messaging - InterconnectFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcd | Messaging - InterconnectReceive - Statistics (senderTid=%1; messages=%2; size=%3)\r\n
0xb0000fd3 | Messaging - AlpcSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fd4 | Messaging - AlpcFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd5 | Messaging - AlpcFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd7 | Messaging - AlpcReceive - Statistics (senderPid=%1; senderTid=%2; messages=%3; size=%4)\r\n
0xb00013ba | Formatting - Message Method (%1)\r\n
0xb0001b58 | CoreMessagingRegistrar ObjectRegistered '%1' (type %2 scope %3 session %4 pid %5 tid %6)\r\n
0xb0001b59 | CoreMessagingRegistrar ObjectRevoked '%1' (type %2 scope %3 session %4 pid %5 tid %6 Orphaned=%7)\r\n
0xb0001b5a | CoreUI server disconnected pid %1 tid %2 id %3\r\n
0xb0001b5b | Conversation %1 has run out of PeerID handles to allocate\r\n
0xb0001b5c | Client connection to conversation '%1' failed, max clients already connected\r\n
0xb0001b5d | IdentityTable uniqueness bits protected us: index %1  requestedUniq %2  currentUniq %3\r\n
0xb0001b5e | IdentityTable uniqueness bits reached max for slot index %1\r\n
0xb0001b5f | IdentityTable slot %1 passed over (diff: %2)\r\n
0xb0001b60 | IdentityTable grown to max index %1 (after %2 times through the loop).\r\n
0xb0001f40 | NtAssociateWaitCompletionPacket succeeded: packet %1 target %2 context %3\r\n
0xb0001f41 | NtAssociateWaitCompletionPacket failed, packet %1 port %2 handle %3 status %4\r\n
0xb0001f42 | NtCancelWaitCompletionPacket results: packet %1 status %2 signaled %3 canceled %4\r\n
0xb0001f43 | Created RegisteredWait: packet %1 target %2 cloned %3\r\n
0xb0001f44 | UserAdapter HandleCompletion: packet %1 target %2\r\n
0xb0001f45 | Calling completion handler: ApcContext %1 KeyContext %2\r\n
0xb0001f46 | Removed end of batch completion.\r\n
0xb0001f47 | Removed completion: ApcContext %1 KeyContext %2\r\n
0xb0004e20 | CoreUI SelfHostError - ThrownException (type=%1; hr=%2; message=%3)\r\n
0xb0004e21 | CoreMessagingRegistrar Object '%1' not found (type=%2; scope=%3)\r\n
0xb0004e22 | CoreUI Connection failed to pid %1 tid %2 id %3\r\n
0xb0004e23 | CoreUI forcibly disconnecting client pid %1 tid %2\r\n
0xb0004e24 | CoreUI NtAlpcConnectPort '%1' failed with hr=%2\r\n
0xb0004e25 | CoreMessagingRegistrar Conversation '%1' not found\r\n
0xd0000001 | Dormant\r\n
0xd0000002 | WaitForNewEvents\r\n
0xd0000003 | SendMessagesLow\r\n
0xd0000004 | Low\r\n
0xd0000005 | SendMessagesNormal\r\n
0xd0000006 | SynchronizeOutput\r\n
0xd0000007 | Normal\r\n
0xd0000008 | SynchronizeInput\r\n
0xd0000009 | ReceiveMessagesNormal\r\n
0xd000000a | ReceiveDeferredMessagesNormal\r\n
0xd000000b | DeliverTimeouts\r\n
0xd000000c | SendMessagesHigh\r\n
0xd000000d | High\r\n
0xd000000e | ReceiveMessagesHigh\r\n
0xd000000f | ReceiveDeferredMessagesHigh\r\n
0xd0000010 | Infinite\r\n
0xd0000011 | Dormant\r\n
0xd0000012 | Low\r\n
0xd0000013 | SynchronizeOutput\r\n
0xd0000014 | Normal\r\n
0xd0000015 | High\r\n
0xd0000016 | None\r\n
0xd0000017 | RunUntilExit\r\n
0xd0000018 | RunAllIfPresent\r\n
0xd0000019 | RunToIdle\r\n
0xd000001a | RunSendOnly\r\n
0xd000001b | FlushAtShutdown\r\n
0xd000001c | Dormant\r\n
0xd000001d | Timer\r\n
0xd000001e | Paint\r\n
0xd000001f | Input\r\n
0xd0000020 | Post\r\n
0xd0000021 | Send\r\n
0xd0000022 | Endpoint\r\n
0xd0000023 | CrossProcessReceivePort\r\n
0xd0000024 | Conversation\r\n
0xd0000025 | Local\r\n
0xd0000026 | System\r\n
0xd0000027 | Process\r\n

### 10.0.19041.1, 10.0.19041.610

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000016 | CoreMessaging CoreUIService\r\n
0x10000021 | CoreMessaging MessagingPerformance\r\n
0x10000022 | CoreMessaging Session\r\n
0x10000023 | CoreMessaging Dispatcher\r\n
0x10000024 | CoreMessaging RegistrarClient\r\n
0x10000025 | CoreMessaging Messaging\r\n
0x10000026 | CoreMessaging Formatting\r\n
0x1000002b | CoreMessaging SelfHostInfo\r\n
0x1000002c | CoreMessaging SelfHostError\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb00003e8 | CoreUI ETW - Initialized (pid=%1)\r\n
0xb00003e9 | CoreUI ETW - Uninitialized (pid=%1)\r\n
0xb000041a | CoreUI System - Out of Memory!\r\n
0xb0000b54 | CoreUI Service server-thread started\r\n
0xb0000b55 | CoreUI Service server-thread exiting\r\n
0xb0000b56 | CoreUI InitializeService called\r\n
0xb0000b57 | CoreUI UninitializeService called\r\n
0xb0000b58 | CoreUI ServiceObjectCreated called\r\n
0xb0000b59 | CoreUI ServiceObjectDestroyed called\r\n
0xb0000b5a | CoreUI UpdateServiceStatus called\r\n
0xb0000b5b | CoreUI ServiceObjectServiceMain called\r\n
0xb0000b5c | CoreUI CoreUI ServiceMain called with unknown service name %1\r\n
0xb0000c1c | Session - CoreUICreate - Start\r\n
0xb0000c1d | Session - CoreUICreate - Stop\r\n
0xb0000c8e | Dispatcher - DispatchItem - Start (internalPriority=%1)\r\n
0xb0000c8f | Dispatcher - DispatchItem - Stop (internalPriority=%1)\r\n
0xb0000c90 | Dispatcher - WakeLevel - UpdateWakeLevel (bits=%1 old=%2 new=%3)\r\n
0xb0000c94 | Dispatcher - DoWait - Start (timeout=%1)\r\n
0xb0000c95 | Dispatcher - DoWait - Stop (status=%1 handle=%2)\r\n
0xb0000c96 | Dispatcher - CallDispatchCallback - Start (awake=%1 reference=%2)\r\n
0xb0000c97 | Dispatcher - CallDispatchCallback - Stop            (timeout=%1)\r\n
0xb0000c98 | UserAdapter - ScheduleDispatch (threadid=%1 userPriority=%2)\r\n
0xb0000c99 | UserAdapter - HostModeRun - Start (runMode=%1 stopping=%2)\r\n
0xb0000c9a | UserAdapter - HostModeRun - Stop (stopCookie=%1)\r\n
0xb0000c9b | UserAdapter - OnUserDispatch - Start (priority=%1)\r\n
0xb0000c9c | UserAdapter - OnUserDispatch - Stop (discarded? %1)\r\n
0xb0000c9d | UserAdapter - IntegratedLoopWait - Start\r\n
0xb0000c9e | UserAdapter - IntegratedLoopWait - Stop\r\n
0xb0000c9f | UserAdapter - PostMessage - Failed due to post message queue full\r\n
0xb0000ca0 | UserAdapter - PostMessage - User failed to schedule an asynchronous DISPATCHNOTIFY_COMPLETION\r\n
0xb0000ce4 | RegistrarClient - Initialize - Start\r\n
0xb0000ce5 | RegistrarClient - Initialize - Stop\r\n
0xb0000faa | Messaging - CreateConnection - Start (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fab | Messaging - CreateConnection - Stop (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fb4 | Messaging - AllocatedMessage (externalPriority=%1; size=%2; destProcessId=%3; destThreadId=%4)\r\n
0xb0000fb5 | Messaging - Message stream dirty (processId=%1 threadId=%2)\r\n
0xb0000fb6 | Messaging - FlushPendingStreams - Start (externalPriority=%1)\r\n
0xb0000fb7 | Messaging - FlushPendingStreams - Stop\r\n
0xb0000fbf | Messaging - LocalReceive - Statistics (messages=%1; size=%2)\r\n
0xb0000fc9 | Messaging - InterconnectSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fca | Messaging - InterconnectFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcb | Messaging - InterconnectFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcd | Messaging - InterconnectReceive - Statistics (senderTid=%1; messages=%2; size=%3)\r\n
0xb0000fd3 | Messaging - AlpcSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fd4 | Messaging - AlpcFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd5 | Messaging - AlpcFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd7 | Messaging - AlpcReceive - Statistics (senderPid=%1; senderTid=%2; messages=%3; size=%4)\r\n
0xb00013ba | Formatting - Message Method (%1)\r\n
0xb0001b58 | CoreMessagingRegistrar ObjectRegistered '%1' (type %2 scope %3 session %4 pid %5 tid %6)\r\n
0xb0001b59 | CoreMessagingRegistrar ObjectRevoked '%1' (type %2 scope %3 session %4 pid %5 tid %6 Orphaned=%7)\r\n
0xb0001b5a | CoreUI server disconnected pid %1 tid %2 id %3\r\n
0xb0001b5b | Conversation %1 has run out of PeerID handles to allocate\r\n
0xb0001b5c | Client connection to conversation '%1' failed, max clients already connected\r\n
0xb0001b5d | IdentityTable uniqueness bits protected us: index %1  requestedUniq %2  currentUniq %3\r\n
0xb0001b5e | IdentityTable uniqueness bits reached max for slot index %1\r\n
0xb0001b5f | IdentityTable slot %1 passed over (diff: %2)\r\n
0xb0001b60 | IdentityTable grown to max index %1 (after %2 times through the loop).\r\n
0xb0001f40 | NtAssociateWaitCompletionPacket succeeded: packet %1 target %2 context %3\r\n
0xb0001f41 | NtAssociateWaitCompletionPacket failed, packet %1 port %2 handle %3 status %4\r\n
0xb0001f42 | NtCancelWaitCompletionPacket results: packet %1 status %2 signaled %3 canceled %4\r\n
0xb0001f43 | Created RegisteredWait: packet %1 target %2 cloned %3\r\n
0xb0001f44 | UserAdapter HandleCompletion: packet %1 target %2\r\n
0xb0001f45 | Calling completion handler: ApcContext %1 KeyContext %2\r\n
0xb0001f46 | Removed end of batch completion.\r\n
0xb0001f47 | Removed completion: ApcContext %1 KeyContext %2\r\n
0xb0004e20 | CoreUI SelfHostError - ThrownException (type=%1; hr=%2; message=%3)\r\n
0xb0004e21 | CoreMessagingRegistrar Object '%1' not found (type=%2; scope=%3)\r\n
0xb0004e22 | CoreUI Connection failed to pid %1 tid %2 id %3\r\n
0xb0004e23 | CoreUI forcibly disconnecting client pid %1 tid %2\r\n
0xb0004e24 | CoreUI NtAlpcConnectPort '%1' failed with hr=%2\r\n
0xb0004e25 | CoreMessagingRegistrar Conversation '%1' not found\r\n
0xb0004e26 | CoreUI Conversation ignoring client pid %1 errorCode %2 errorMessage %3\r\n
0xd0000001 | Dormant\r\n
0xd0000002 | WaitForNewEvents\r\n
0xd0000003 | SendMessagesLow\r\n
0xd0000004 | Low\r\n
0xd0000005 | SendMessagesNormal\r\n
0xd0000006 | SynchronizeOutput\r\n
0xd0000007 | Normal\r\n
0xd0000008 | SynchronizeInput\r\n
0xd0000009 | ReceiveMessagesNormal\r\n
0xd000000a | ReceiveDeferredMessagesNormal\r\n
0xd000000b | DeliverTimeouts\r\n
0xd000000c | SendMessagesHigh\r\n
0xd000000d | High\r\n
0xd000000e | ReceiveMessagesHigh\r\n
0xd000000f | ReceiveDeferredMessagesHigh\r\n
0xd0000010 | Infinite\r\n
0xd0000011 | Dormant\r\n
0xd0000012 | Low\r\n
0xd0000013 | SynchronizeOutput\r\n
0xd0000014 | Normal\r\n
0xd0000015 | High\r\n
0xd0000016 | None\r\n
0xd0000017 | RunUntilExit\r\n
0xd0000018 | RunAllIfPresent\r\n
0xd0000019 | RunToIdle\r\n
0xd000001a | RunSendOnly\r\n
0xd000001b | FlushAtShutdown\r\n
0xd000001c | Dormant\r\n
0xd000001d | Timer\r\n
0xd000001e | Paint\r\n
0xd000001f | Input\r\n
0xd0000020 | Post\r\n
0xd0000021 | Send\r\n
0xd0000022 | Endpoint\r\n
0xd0000023 | CrossProcessReceivePort\r\n
0xd0000024 | Conversation\r\n
0xd0000025 | Local\r\n
0xd0000026 | System\r\n
0xd0000027 | Process\r\n

### 10.0.22000.71

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000016 | CoreMessaging CoreUIService\r\n
0x10000021 | CoreMessaging MessagingPerformance\r\n
0x10000022 | CoreMessaging Session\r\n
0x10000023 | CoreMessaging Dispatcher\r\n
0x10000024 | CoreMessaging RegistrarClient\r\n
0x10000025 | CoreMessaging Messaging\r\n
0x10000026 | CoreMessaging Formatting\r\n
0x1000002b | CoreMessaging SelfHostInfo\r\n
0x1000002c | CoreMessaging SelfHostError\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb00003e8 | CoreUI ETW - Initialized (pid=%1)\r\n
0xb00003e9 | CoreUI ETW - Uninitialized (pid=%1)\r\n
0xb000041a | CoreUI System - Out of Memory!\r\n
0xb0000b54 | CoreUI Service server-thread started\r\n
0xb0000b55 | CoreUI Service server-thread exiting\r\n
0xb0000b56 | CoreUI InitializeService called\r\n
0xb0000b57 | CoreUI UninitializeService called\r\n
0xb0000b59 | CoreUI ServiceObjectDestroyed called\r\n
0xb0000b5a | CoreUI UpdateServiceStatus called\r\n
0xb0000b5b | CoreUI ServiceObjectServiceMain called\r\n
0xb0000b5c | CoreUI CoreUI ServiceMain called with unknown service name %1\r\n
0xb0000c1c | Session - CoreUICreate - Start\r\n
0xb0000c1d | Session - CoreUICreate - Stop\r\n
0xb0000c8e | Dispatcher - DispatchItem - Start (internalPriority=%1)\r\n
0xb0000c8f | Dispatcher - DispatchItem - Stop (internalPriority=%1)\r\n
0xb0000c90 | Dispatcher - WakeLevel - UpdateWakeLevel (bits=%1 old=%2 new=%3)\r\n
0xb0000c94 | Dispatcher - DoWait - Start (timeout=%1)\r\n
0xb0000c95 | Dispatcher - DoWait - Stop (status=%1 handle=%2)\r\n
0xb0000c96 | Dispatcher - CallDispatchCallback - Start (awake=%1 reference=%2)\r\n
0xb0000c97 | Dispatcher - CallDispatchCallback - Stop            (timeout=%1)\r\n
0xb0000c98 | UserAdapter - ScheduleDispatch (threadid=%1 userPriority=%2)\r\n
0xb0000c99 | UserAdapter - HostModeRun - Start (runMode=%1 stopping=%2)\r\n
0xb0000c9a | UserAdapter - HostModeRun - Stop\r\n
0xb0000c9b | UserAdapter - OnUserDispatch - Start (priority=%1)\r\n
0xb0000c9c | UserAdapter - OnUserDispatch - Stop (discarded? %1)\r\n
0xb0000c9d | UserAdapter - IntegratedLoopWait - Start\r\n
0xb0000c9e | UserAdapter - IntegratedLoopWait - Stop\r\n
0xb0000c9f | UserAdapter - PostMessage - Failed due to post message queue full\r\n
0xb0000ca0 | UserAdapter - PostMessage - User failed to schedule an asynchronous DISPATCHNOTIFY_COMPLETION\r\n
0xb0000ce4 | RegistrarClient - Initialize - Start\r\n
0xb0000ce5 | RegistrarClient - Initialize - Stop\r\n
0xb0000faa | Messaging - CreateConnection - Start (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fab | Messaging - CreateConnection - Stop (destProcessId=%1; destThreadId=%2)\r\n
0xb0000fb4 | Messaging - AllocatedMessage (externalPriority=%1; size=%2; destProcessId=%3; destThreadId=%4)\r\n
0xb0000fb5 | Messaging - Message stream dirty (processId=%1 threadId=%2)\r\n
0xb0000fb6 | Messaging - FlushPendingStreams - Start (externalPriority=%1)\r\n
0xb0000fb7 | Messaging - FlushPendingStreams - Stop\r\n
0xb0000fbf | Messaging - LocalReceive - Statistics (messages=%1; size=%2)\r\n
0xb0000fc9 | Messaging - InterconnectSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fca | Messaging - InterconnectFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcb | Messaging - InterconnectFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fcd | Messaging - InterconnectReceive - Statistics (senderTid=%1; messages=%2; size=%3)\r\n
0xb0000fd3 | Messaging - AlpcSend - Statistics (buffers=%1; size=%2)\r\n
0xb0000fd4 | Messaging - AlpcFlush - Start (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd5 | Messaging - AlpcFlush - Stop (externalPriority=%1; destProcessId=%2; destThreadId=%3)\r\n
0xb0000fd7 | Messaging - AlpcReceive - Statistics (senderPid=%1; senderTid=%2; messages=%3; size=%4)\r\n
0xb0001b58 | CoreMessagingRegistrar ObjectRegistered '%1' (type %2 scope %3 session %4 pid %5 tid %6)\r\n
0xb0001b59 | CoreMessagingRegistrar ObjectRevoked '%1' (type %2 scope %3 session %4 pid %5 tid %6 Orphaned=%7)\r\n
0xb0001b5a | CoreUI server disconnected pid %1 tid %2 id %3\r\n
0xb0001b5b | Conversation %1 has run out of PeerID handles to allocate\r\n
0xb0001b5c | Client connection to conversation '%1' failed, max clients already connected\r\n
0xb0001b5d | IdentityTable uniqueness bits protected us: index %1  requestedUniq %2  currentUniq %3\r\n
0xb0001f40 | NtAssociateWaitCompletionPacket succeeded: packet %1 target %2 context %3\r\n
0xb0001f41 | NtAssociateWaitCompletionPacket failed, packet %1 port %2 handle %3 status %4\r\n
0xb0001f42 | NtCancelWaitCompletionPacket results: packet %1 status %2 signaled %3 canceled %4\r\n
0xb0001f43 | Created RegisteredWait: packet %1 target %2 cloned %3\r\n
0xb0001f44 | UserAdapter HandleCompletion: packet %1 target %2\r\n
0xb0001f45 | Calling completion handler: ApcContext %1 KeyContext %2\r\n
0xb0001f46 | Removed end of batch completion.\r\n
0xb0001f47 | Removed completion: ApcContext %1 KeyContext %2\r\n
0xb0004e20 | CoreUI SelfHostError - ThrownException (type=%1; hr=%2; message=%3)\r\n
0xb0004e21 | CoreMessagingRegistrar Object '%1' not found (type=%2; scope=%3)\r\n
0xb0004e22 | CoreUI Connection failed to pid %1 tid %2 id %3\r\n
0xb0004e23 | CoreUI forcibly disconnecting client pid %1 tid %2\r\n
0xb0004e24 | CoreUI NtAlpcConnectPort '%1' failed with hr=%2\r\n
0xb0004e26 | CoreUI Conversation ignoring client pid %1 errorCode %2 errorMessage %3\r\n
0xd0000001 | Dormant\r\n
0xd0000002 | WaitForNewEvents\r\n
0xd0000003 | SendMessagesLow\r\n
0xd0000004 | Low\r\n
0xd0000005 | SendMessagesNormal\r\n
0xd0000006 | SynchronizeOutput\r\n
0xd0000007 | Normal\r\n
0xd0000008 | SynchronizeInput\r\n
0xd0000009 | ReceiveMessagesNormal\r\n
0xd000000a | ReceiveDeferredMessagesNormal\r\n
0xd000000b | DeliverTimeouts\r\n
0xd000000c | SendMessagesHigh\r\n
0xd000000d | High\r\n
0xd000000e | ReceiveMessagesHigh\r\n
0xd000000f | ReceiveDeferredMessagesHigh\r\n
0xd0000010 | Infinite\r\n
0xd0000011 | Dormant\r\n
0xd0000012 | Low\r\n
0xd0000013 | SynchronizeOutput\r\n
0xd0000014 | Normal\r\n
0xd0000015 | High\r\n
0xd0000016 | None\r\n
0xd0000017 | RunUntilExit\r\n
0xd0000018 | RunAllIfPresent\r\n
0xd0000019 | RunToIdle\r\n
0xd000001a | RunSendOnly\r\n
0xd000001b | FlushAtShutdown\r\n
0xd000001c | Dormant\r\n
0xd000001d | Timer\r\n
0xd000001e | Paint\r\n
0xd000001f | Input\r\n
0xd0000020 | Post\r\n
0xd0000021 | Send\r\n
0xd0000022 | Endpoint\r\n
0xd0000023 | CrossProcessReceivePort\r\n
0xd0000024 | Conversation\r\n
0xd0000025 | Local\r\n
0xd0000026 | System\r\n
0xd0000027 | Process\r\n
0xd0000028 | Port\r\n
0xd0000029 | CrossPartition\r\n
