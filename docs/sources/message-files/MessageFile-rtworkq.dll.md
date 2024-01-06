## rtworkq.dll

Path: %SystemRoot%\system32\rtworkq.dll

### 10.0.14393.0, 10.0.15063.0

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000247 | WorkQueue: Execute\r\n
0x70000248 | WorkQueue: Queue\r\n
0x7000024c | WorkQueue: Thread\r\n
0x70000253 | MMCSS Registration\r\n
0x7000025a | WorkQueue: Queue_Create\r\n
0x7000025b | WorkQueue: Execute callback\r\n
0x7000025c | WorkQueue: MMCSS Transition\r\n
0x7000025d | WorkQueue: UpdateDeadlines\r\n
0x7000025e | WorkQueue: AddDeadline\r\n
0x7000025f | WorkQueue: AddImmediateDeadline\r\n
0x70000260 | WorkQueue: DeadlineYield\r\n
0x70000261 | WorkQueue: UpdateDeadlineQueue\r\n
0x70000262 | WorkQueue: LongRunning\r\n
0x70000263 | WorkQueue: StartTimer\r\n
0x70000264 | WorkQueue: ExecuteTimer\r\n
0x70000266 | Update Select WorkQueues CpuGroupMask\r\n
0x70000267 | SubscribeCpuGroupMaskChangeWNF\r\n
0x70000268 | UpdateWorkqueueCpuGroupMask\r\n
0x70000269 | CpuGroupMaskChangeWnfCallback\r\n
0x7000026a | SetThreadCpuGroupMask\r\n
0x7000026b | WorkQueue: Debounce\r\n
0x7000026c | WorkQueue: Buffering\r\n
0x71000064 | WorkQueue: Queue Extended\r\n
0x71000065 | WorkQueue: Extended LongRunning\r\n
0x90000001 | Microsoft-Windows-RTWorkQueue-Threading\r\n
0x90000002 | RTWorkQueue Threading\r\n
0x91000001 | Microsoft-Windows-RTWorkQueue-Extended\r\n
0x91000002 | RTWorkQueue Extended\r\n
0xb0001153 | WorkQueue Execute: Start workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001154 | WorkQueue Execute: End workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001155 | WorkQueue Queue: WorkQueuePtr=%1 Start threads=%2 AsyncResult=%3\r\n
0xb0001156 | WorkQueue Queue: WorkQueuePtr=%1 End threads=%2 AsyncResult=%3\r\n
0xb0001157 | WorkQueue Thread: Start workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001158 | WorkQueue Thread: End workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001166 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001167 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001178 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001179 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb000117a | WorkQueue Execute Callback: Start workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117b | WorkQueue Execute Callback: End workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117c | WorkQueue MMCSS: Start workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117d | WorkQueue MMCSS: End workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117e | WorkQueue UpdateDeadlines: Start workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb000117f | WorkQueue UpdateDeadlines: End workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb0001180 | WorkQueue AddDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001181 | WorkQueue AddDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001182 | WorkQueue AddImmediateDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001183 | WorkQueue AddImmediateDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001184 | WorkQueue DeadlineYield: Start workQueueID=%1 Delay=%2\r\n
0xb0001185 | WorkQueue DeadlineYield: End workQueueID=%1 Delay=%2\r\n
0xb0001186 | WorkQueue DeadlineQueue: WorkQueuePtr=%1 workQueueID=%2 count=%3 immediateCount=%4 nextDeadline=%5 nextItem=%6\r\n
0xb0001187 | WorkQueue LongRunning: Start workQueueID=%1\r\n
0xb0001188 | WorkQueue LongRunning: End workQueueID=%1\r\n
0xb0001189 | WorkQueue: StartTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3 Timeout=%4 IsPeriodic=%5\r\n
0xb000118a | WorkQueue: ExecuteTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3\r\n
0xb000118d | UpdateSelectWorkQueuesCpuGroupMask Enter ProcessorGroup=%1 ProcessorMask=%2\r\n
0xb000118e | UpdateSelectWorkQueuesCpuGroupMask Leave ProcessorGroup=%1 ProcessorMask=%2 hr=%3\r\n
0xb000118f | SubscribeCpuGroupMaskChangeWNF queryStatus=%1 subscribeStatus=%2 changeStamp=%3\r\n
0xb0001190 | UpdateWorkqueueCpuGroupMask workQueue=%1 Class=%2 ProcesssorGroup=%3 ProcesssorMask=%4\r\n
0xb0001191 | CpuGroupMaskChangeWnfCallback ChangeStamp=%1 CurChangeStamp=%2 ProcessorGroup=%3 ProcessorMask=%4 Length=%5\r\n
0xb0001192 | SetThreadCpuGroupMask pWorkQueue=%1 Class=%2 Priority=%3 ThreadId=%4 CurProcessorGroup=%5 CurProcessorMask=%6 NewProcessorGroup=%7 NewProcessorMask=%8 status=%9\r\n
0xb0001193 | WorkQueue Start Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001194 | WorkQueue End Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001195 | WorkQueue Debounce: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001196 | WorkQueue Debounce: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001197 | WorkQueue Buffering: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001198 | WorkQueue Buffering: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb1000001 | WorkQueue Queue extended: AsyncResult=%1 AsyncResultVTable=%2\r\n
0xb1000002 | WorkQueue Extended LongRunning: RefCount workQueueID=%1 refcount=%2\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000247 | WorkQueue: Execute\r\n
0x70000248 | WorkQueue: Queue\r\n
0x7000024c | WorkQueue: Thread\r\n
0x70000253 | MMCSS Registration\r\n
0x7000025a | WorkQueue: Queue_Create\r\n
0x7000025b | WorkQueue: Execute callback\r\n
0x7000025c | WorkQueue: MMCSS Transition\r\n
0x7000025d | WorkQueue: UpdateDeadlines\r\n
0x7000025e | WorkQueue: AddDeadline\r\n
0x7000025f | WorkQueue: AddImmediateDeadline\r\n
0x70000260 | WorkQueue: DeadlineYield\r\n
0x70000261 | WorkQueue: UpdateDeadlineQueue\r\n
0x70000262 | WorkQueue: LongRunning\r\n
0x70000263 | WorkQueue: StartTimer\r\n
0x70000264 | WorkQueue: ExecuteTimer\r\n
0x70000266 | Update Select WorkQueues CpuGroupMask\r\n
0x70000267 | SubscribeCpuGroupMaskChangeWNF\r\n
0x70000268 | UpdateWorkqueueCpuGroupMask\r\n
0x70000269 | CpuGroupMaskChangeWnfCallback\r\n
0x7000026a | SetThreadCpuGroupMask\r\n
0x7000026b | WorkQueue: Debounce\r\n
0x7000026c | WorkQueue: Buffering\r\n
0x7000026d | WorkQueue: Notification\r\n
0x7000026e | Platform: AllocIndex\r\n
0x7000026f | Platform: Init\r\n
0x70000270 | Platform: Shutdown\r\n
0x70000271 | Platform: Shutdown_WorkQueue\r\n
0x70000272 | WorkQueue: RunLimit\r\n
0x71000064 | WorkQueue: Queue Extended\r\n
0x71000065 | WorkQueue: Extended LongRunning\r\n
0x71000066 | WorkQueue: Extended InvalidUsageAttempt\r\n
0x71000067 | WorkQueue: Extended InvalidCallbackAttempt\r\n
0x71000068 | WorkQueue: PlatformRef\r\n
0x71000069 | WorkQueue: RTLock\r\n
0x7100006a | WorkQueue: SetAVMode\r\n
0x7100006b | WorkQueue: RTLockAcquire\r\n
0x7100006c | WorkQueue: TimerCallback\r\n
0x7100006d | WorkQueue: TimerMode\r\n
0x7100006e | WorkQueue: TimerSet\r\n
0x7100006f | WorkQueue: TimerResChange\r\n
0x90000001 | Microsoft-Windows-RTWorkQueue-Threading\r\n
0x90000002 | RTWorkQueue Threading\r\n
0x91000001 | Microsoft-Windows-RTWorkQueue-Extended\r\n
0x91000002 | RTWorkQueue Extended\r\n
0xb0001153 | WorkQueue Execute: Start workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001154 | WorkQueue Execute: End workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001155 | WorkQueue Queue: WorkQueuePtr=%1 Start threads=%2 AsyncResult=%3\r\n
0xb0001156 | WorkQueue Queue: WorkQueuePtr=%1 End threads=%2 AsyncResult=%3\r\n
0xb0001157 | WorkQueue Thread: Start workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001158 | WorkQueue Thread: End workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001166 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001167 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001178 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001179 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb000117a | WorkQueue Execute Callback: Start workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117b | WorkQueue Execute Callback: End workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117c | WorkQueue MMCSS: Start workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117d | WorkQueue MMCSS: End workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117e | WorkQueue UpdateDeadlines: Start workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb000117f | WorkQueue UpdateDeadlines: End workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb0001180 | WorkQueue AddDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001181 | WorkQueue AddDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001182 | WorkQueue AddImmediateDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001183 | WorkQueue AddImmediateDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001184 | WorkQueue DeadlineYield: Start workQueueID=%1 Delay=%2\r\n
0xb0001185 | WorkQueue DeadlineYield: End workQueueID=%1 Delay=%2\r\n
0xb0001186 | WorkQueue DeadlineQueue: WorkQueuePtr=%1 workQueueID=%2 count=%3 immediateCount=%4 nextDeadline=%5 nextItem=%6\r\n
0xb0001187 | WorkQueue LongRunning: Start workQueueID=%1\r\n
0xb0001188 | WorkQueue LongRunning: End workQueueID=%1\r\n
0xb0001189 | WorkQueue: StartTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3 Timeout=%4 IsPeriodic=%5\r\n
0xb000118a | WorkQueue: ExecuteTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3\r\n
0xb000118d | UpdateSelectWorkQueuesCpuGroupMask Enter ProcessorGroup=%1 ProcessorMask=%2\r\n
0xb000118e | UpdateSelectWorkQueuesCpuGroupMask Leave ProcessorGroup=%1 ProcessorMask=%2 hr=%3\r\n
0xb000118f | SubscribeCpuGroupMaskChangeWNF queryStatus=%1 subscribeStatus=%2 changeStamp=%3\r\n
0xb0001190 | UpdateWorkqueueCpuGroupMask workQueue=%1 Class=%2 ProcesssorGroup=%3 ProcesssorMask=%4\r\n
0xb0001191 | CpuGroupMaskChangeWnfCallback ChangeStamp=%1 CurChangeStamp=%2 ProcessorGroup=%3 ProcessorMask=%4 Length=%5\r\n
0xb0001192 | SetThreadCpuGroupMask pWorkQueue=%1 Class=%2 Priority=%3 ThreadId=%4 CurProcessorGroup=%5 CurProcessorMask=%6 NewProcessorGroup=%7 NewProcessorMask=%8 status=%9\r\n
0xb0001193 | WorkQueue Start Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001194 | WorkQueue End Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001195 | WorkQueue Debounce: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001196 | WorkQueue Debounce: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001197 | WorkQueue Buffering: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001198 | WorkQueue Buffering: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001199 | Platform AllocIndex start: Platform=%1 WorkQueueID=%2 Index=%3\r\n
0xb000119a | Platform AllocIndex stop: Platform=%1 WorkQueueID=%2 Index=%3\r\n
0xb000119b | Platform Init start: Platform=%1\r\n
0xb000119c | Platform Init stop: Platform=%1\r\n
0xb000119d | Platform Shutdown start: Platform=%1\r\n
0xb000119e | Platform Shutdown stop: Platform=%1\r\n
0xb000119f | Platform Shutdown timeout: Platform=%1\r\n
0xb00011a0 | Platform Shutdown_WorkQueue start: Platform=%1 workqueue=%2 index=%3\r\n
0xb00011a1 | Platform Shutdown_WorkQueue stop: Platform=%1 workqueue=%2 index=%3\r\n
0xb00011a2 | WorkQueue RunLimit: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a3 | WorkQueue RunLimit: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a4 | WorkQueue RunLimit: Exceeded workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb1000001 | WorkQueue Queue extended: AsyncResult=%1 AsyncResultVTable=%2\r\n
0xb1000002 | WorkQueue Extended LongRunning: RefCount workQueueID=%1 refcount=%2\r\n
0xb1000003 | WorkQueue extended InvalidUsageAttempt: Platform=%1 WorkQueueID=%2 PrivateQueueIndex=%3\r\n
0xb1000004 | WorkQueue extended InvalidCallbackAttempt: Platform=%1 Callback=%2 WorkQueueID=%3\r\n
0xb1000005 | WorkQueue Extended PlatformRef: Start platform=%1\r\n
0xb1000006 | WorkQueue Extended PlatformRef: Stop platform=%1\r\n
0xb1000007 | WorkQueue Extended PlatformRef: ref platform=%1 ref:%2\r\n
0xb1000008 | WorkQueue Extended RTLock: Start workQueueID=%1\r\n
0xb1000009 | WorkQueue Extended RTLock: Stop workQueueID=%1\r\n
0xb100000a | WorkQueue Extended SetAVMode: Start group=%1 mode=%2\r\n
0xb100000b | WorkQueue Extended SetAVMode: Stop group=%1 mode=%2\r\n
0xb100000c | WorkQueue Extended RTLockAcquire: Start workQueueID=%1\r\n
0xb100000d | WorkQueue Extended RTLockAcquire: Stop workQueueID=%1\r\n
0xb100000e | WorkQueue Extended TimerCallback: Start object=%1 id=%2 mode=%3\r\n
0xb100000f | WorkQueue Extended TimerCallback: Stop object=%1 id=%2 mode=%3\r\n
0xb1000010 | WorkQueue TimerMode: Set workqueue_ptr=%1 workQueueID=%2 Mode=%3\r\n
0xb1000011 | WorkQueue TimerSet: Set workqueue_ptr=%1 workQueueID=%2 Delta=%3\r\n
0xb1000012 | WorkQueue Extended TimerResChange: Start object=%1 id=%2 mode=%3\r\n
0xb1000013 | WorkQueue Extended TimerResChange: Stop object=%1 id=%2 mode=%3\r\n

### 10.0.17134.619, 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000247 | WorkQueue: Execute\r\n
0x70000248 | WorkQueue: Queue\r\n
0x7000024c | WorkQueue: Thread\r\n
0x70000253 | MMCSS Registration\r\n
0x7000025a | WorkQueue: Queue_Create\r\n
0x7000025b | WorkQueue: Execute callback\r\n
0x7000025c | WorkQueue: MMCSS Transition\r\n
0x7000025d | WorkQueue: UpdateDeadlines\r\n
0x7000025e | WorkQueue: AddDeadline\r\n
0x7000025f | WorkQueue: AddImmediateDeadline\r\n
0x70000260 | WorkQueue: DeadlineYield\r\n
0x70000261 | WorkQueue: UpdateDeadlineQueue\r\n
0x70000262 | WorkQueue: LongRunning\r\n
0x70000263 | WorkQueue: StartTimer\r\n
0x70000264 | WorkQueue: ExecuteTimer\r\n
0x70000266 | Update Select WorkQueues CpuGroupMask\r\n
0x70000267 | SubscribeCpuGroupMaskChangeWNF\r\n
0x70000268 | UpdateWorkqueueCpuGroupMask\r\n
0x70000269 | CpuGroupMaskChangeWnfCallback\r\n
0x7000026a | SetThreadCpuGroupMask\r\n
0x7000026b | WorkQueue: Debounce\r\n
0x7000026c | WorkQueue: Buffering\r\n
0x7000026d | WorkQueue: Notification\r\n
0x7000026e | Platform: AllocIndex\r\n
0x7000026f | Platform: Init\r\n
0x70000270 | Platform: Shutdown\r\n
0x70000271 | Platform: Shutdown_WorkQueue\r\n
0x70000272 | WorkQueue: RunLimit\r\n
0x70000273 | TaskGroup\r\n
0x71000064 | WorkQueue: Queue Extended\r\n
0x71000065 | WorkQueue: Extended LongRunning\r\n
0x71000066 | WorkQueue: Extended InvalidUsageAttempt\r\n
0x71000067 | WorkQueue: Extended InvalidCallbackAttempt\r\n
0x71000068 | WorkQueue: PlatformRef\r\n
0x71000069 | WorkQueue: RTLock\r\n
0x7100006a | WorkQueue: SetAVMode\r\n
0x7100006b | WorkQueue: RTLockAcquire\r\n
0x7100006c | WorkQueue: TimerCallback\r\n
0x7100006d | WorkQueue: TimerMode\r\n
0x7100006e | WorkQueue: TimerSet\r\n
0x7100006f | WorkQueue: TimerResChange\r\n
0x90000001 | Microsoft-Windows-RTWorkQueue-Threading\r\n
0x90000002 | RTWorkQueue Threading\r\n
0x91000001 | Microsoft-Windows-RTWorkQueue-Extended\r\n
0x91000002 | RTWorkQueue Extended\r\n
0xb0001153 | WorkQueue Execute: Start workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001154 | WorkQueue Execute: End workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001155 | WorkQueue Queue: WorkQueuePtr=%1 Start threads=%2 AsyncResult=%3\r\n
0xb0001156 | WorkQueue Queue: WorkQueuePtr=%1 End threads=%2 AsyncResult=%3\r\n
0xb0001157 | WorkQueue Thread: Start workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001158 | WorkQueue Thread: End workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001166 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001167 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001178 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001179 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb000117a | WorkQueue Execute Callback: Start workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117b | WorkQueue Execute Callback: End workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117c | WorkQueue MMCSS: Start workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117d | WorkQueue MMCSS: End workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117e | WorkQueue UpdateDeadlines: Start workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb000117f | WorkQueue UpdateDeadlines: End workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb0001180 | WorkQueue AddDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001181 | WorkQueue AddDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001182 | WorkQueue AddImmediateDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001183 | WorkQueue AddImmediateDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001184 | WorkQueue DeadlineYield: Start workQueueID=%1 Delay=%2\r\n
0xb0001185 | WorkQueue DeadlineYield: End workQueueID=%1 Delay=%2\r\n
0xb0001186 | WorkQueue DeadlineQueue: WorkQueuePtr=%1 workQueueID=%2 count=%3 immediateCount=%4 nextDeadline=%5 nextItem=%6\r\n
0xb0001187 | WorkQueue LongRunning: Start workQueueID=%1\r\n
0xb0001188 | WorkQueue LongRunning: End workQueueID=%1\r\n
0xb0001189 | WorkQueue: StartTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3 Timeout=%4 IsPeriodic=%5\r\n
0xb000118a | WorkQueue: ExecuteTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3\r\n
0xb000118d | UpdateSelectWorkQueuesCpuGroupMask Enter ProcessorGroup=%1 ProcessorMask=%2\r\n
0xb000118e | UpdateSelectWorkQueuesCpuGroupMask Leave ProcessorGroup=%1 ProcessorMask=%2 hr=%3\r\n
0xb000118f | SubscribeCpuGroupMaskChangeWNF queryStatus=%1 subscribeStatus=%2 changeStamp=%3\r\n
0xb0001190 | UpdateWorkqueueCpuGroupMask workQueue=%1 Class=%2 ProcesssorGroup=%3 ProcesssorMask=%4\r\n
0xb0001191 | CpuGroupMaskChangeWnfCallback ChangeStamp=%1 CurChangeStamp=%2 ProcessorGroup=%3 ProcessorMask=%4 Length=%5\r\n
0xb0001192 | SetThreadCpuGroupMask pWorkQueue=%1 Class=%2 Priority=%3 ThreadId=%4 CurProcessorGroup=%5 CurProcessorMask=%6 NewProcessorGroup=%7 NewProcessorMask=%8 status=%9\r\n
0xb0001193 | WorkQueue Start Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001194 | WorkQueue End Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001195 | WorkQueue Debounce: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001196 | WorkQueue Debounce: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001197 | WorkQueue Buffering: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001198 | WorkQueue Buffering: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001199 | Platform AllocIndex start: Platform=%1 WorkQueueID=%2 Index=%3\r\n
0xb000119a | Platform AllocIndex stop: Platform=%1 WorkQueueID=%2 Index=%3\r\n
0xb000119b | Platform Init start: Platform=%1\r\n
0xb000119c | Platform Init stop: Platform=%1\r\n
0xb000119d | Platform Shutdown start: Platform=%1\r\n
0xb000119e | Platform Shutdown stop: Platform=%1\r\n
0xb000119f | Platform Shutdown timeout: Platform=%1\r\n
0xb00011a0 | Platform Shutdown_WorkQueue start: Platform=%1 workqueue=%2 index=%3\r\n
0xb00011a1 | Platform Shutdown_WorkQueue stop: Platform=%1 workqueue=%2 index=%3\r\n
0xb00011a2 | WorkQueue RunLimit: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a3 | WorkQueue RunLimit: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a4 | WorkQueue RunLimit: Exceeded workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a5 | TaskGroup: Start TaskGroup=%1\r\n
0xb00011a6 | TaskGroup: End TaskGroup=%1\r\n
0xb00011a7 | TaskGroup RefCount TaskGroup=%1 RefCount=%2\r\n
0xb00011a8 | TaskGroup ObjectCount ObjectCount=%1\r\n
0xb1000001 | WorkQueue Queue extended: AsyncResult=%1 AsyncResultVTable=%2\r\n
0xb1000002 | WorkQueue Extended LongRunning: RefCount workQueueID=%1 refcount=%2\r\n
0xb1000003 | WorkQueue extended InvalidUsageAttempt: Platform=%1 WorkQueueID=%2 PrivateQueueIndex=%3\r\n
0xb1000004 | WorkQueue extended InvalidCallbackAttempt: Platform=%1 Callback=%2 WorkQueueID=%3\r\n
0xb1000005 | WorkQueue Extended PlatformRef: Start platform=%1\r\n
0xb1000006 | WorkQueue Extended PlatformRef: Stop platform=%1\r\n
0xb1000007 | WorkQueue Extended PlatformRef: ref platform=%1 ref:%2\r\n
0xb1000008 | WorkQueue Extended RTLock: Start workQueueID=%1\r\n
0xb1000009 | WorkQueue Extended RTLock: Stop workQueueID=%1\r\n
0xb100000a | WorkQueue Extended SetAVMode: Start group=%1 mode=%2\r\n
0xb100000b | WorkQueue Extended SetAVMode: Stop group=%1 mode=%2\r\n
0xb100000c | WorkQueue Extended RTLockAcquire: Start workQueueID=%1\r\n
0xb100000d | WorkQueue Extended RTLockAcquire: Stop workQueueID=%1\r\n
0xb100000e | WorkQueue Extended TimerCallback: Start object=%1 id=%2 mode=%3\r\n
0xb100000f | WorkQueue Extended TimerCallback: Stop object=%1 id=%2 mode=%3\r\n
0xb1000010 | WorkQueue TimerMode: Set workqueue_ptr=%1 workQueueID=%2 Mode=%3\r\n
0xb1000011 | WorkQueue TimerSet: Set workqueue_ptr=%1 workQueueID=%2 Delta=%3\r\n
0xb1000012 | WorkQueue Extended TimerResChange: Start object=%1 id=%2 mode=%3\r\n
0xb1000013 | WorkQueue Extended TimerResChange: Stop object=%1 id=%2 mode=%3\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000247 | WorkQueue: Execute\r\n
0x70000248 | WorkQueue: Queue\r\n
0x7000024c | WorkQueue: Thread\r\n
0x70000253 | MMCSS Registration\r\n
0x7000025a | WorkQueue: Queue_Create\r\n
0x7000025b | WorkQueue: Execute callback\r\n
0x7000025c | WorkQueue: MMCSS Transition\r\n
0x7000025d | WorkQueue: UpdateDeadlines\r\n
0x7000025e | WorkQueue: AddDeadline\r\n
0x7000025f | WorkQueue: AddImmediateDeadline\r\n
0x70000260 | WorkQueue: DeadlineYield\r\n
0x70000261 | WorkQueue: UpdateDeadlineQueue\r\n
0x70000262 | WorkQueue: LongRunning\r\n
0x70000263 | WorkQueue: StartTimer\r\n
0x70000264 | WorkQueue: ExecuteTimer\r\n
0x70000266 | Update Select WorkQueues CpuGroupMask\r\n
0x70000267 | SubscribeCpuGroupMaskChangeWNF\r\n
0x70000268 | UpdateWorkqueueCpuGroupMask\r\n
0x70000269 | CpuGroupMaskChangeWnfCallback\r\n
0x7000026a | SetThreadCpuGroupMask\r\n
0x7000026b | WorkQueue: Debounce\r\n
0x7000026c | WorkQueue: Buffering\r\n
0x7000026d | WorkQueue: Notification\r\n
0x7000026e | Platform: AllocIndex\r\n
0x7000026f | Platform: Init\r\n
0x70000270 | Platform: Shutdown\r\n
0x70000271 | Platform: Shutdown_WorkQueue\r\n
0x70000272 | WorkQueue: RunLimit\r\n
0x70000273 | TaskGroup\r\n
0x71000064 | WorkQueue: Queue Extended\r\n
0x71000065 | WorkQueue: Extended LongRunning\r\n
0x71000066 | WorkQueue: Extended InvalidUsageAttempt\r\n
0x71000067 | WorkQueue: Extended InvalidCallbackAttempt\r\n
0x71000068 | WorkQueue: PlatformRef\r\n
0x71000069 | WorkQueue: RTLock\r\n
0x7100006a | WorkQueue: SetAVMode\r\n
0x7100006b | WorkQueue: RTLockAcquire\r\n
0x7100006c | WorkQueue: TimerCallback\r\n
0x7100006d | WorkQueue: TimerMode\r\n
0x7100006e | WorkQueue: TimerSet\r\n
0x7100006f | WorkQueue: TimerResChange\r\n
0x90000001 | Microsoft-Windows-RTWorkQueue-Threading\r\n
0x90000002 | RTWorkQueue Threading\r\n
0x91000001 | Microsoft-Windows-RTWorkQueue-Extended\r\n
0x91000002 | RTWorkQueue Extended\r\n
0xb0001153 | WorkQueue Execute: Start workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001154 | WorkQueue Execute: End workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001155 | WorkQueue Queue: WorkQueuePtr=%1 Start threads=%2 AsyncResult=%3\r\n
0xb0001156 | WorkQueue Queue: WorkQueuePtr=%1 End threads=%2 AsyncResult=%3\r\n
0xb0001157 | WorkQueue Thread: Start workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001158 | WorkQueue Thread: End workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001166 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001167 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001178 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001179 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb000117a | WorkQueue Execute Callback: Start workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117b | WorkQueue Execute Callback: End workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117c | WorkQueue MMCSS: Start workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117d | WorkQueue MMCSS: End workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117e | WorkQueue UpdateDeadlines: Start workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb000117f | WorkQueue UpdateDeadlines: End workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb0001180 | WorkQueue AddDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001181 | WorkQueue AddDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001182 | WorkQueue AddImmediateDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001183 | WorkQueue AddImmediateDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001184 | WorkQueue DeadlineYield: Start workQueueID=%1 Delay=%2\r\n
0xb0001185 | WorkQueue DeadlineYield: End workQueueID=%1 Delay=%2\r\n
0xb0001186 | WorkQueue DeadlineQueue: WorkQueuePtr=%1 workQueueID=%2 count=%3 immediateCount=%4 nextDeadline=%5 nextItem=%6\r\n
0xb0001187 | WorkQueue LongRunning: Start workQueueID=%1\r\n
0xb0001188 | WorkQueue LongRunning: End workQueueID=%1\r\n
0xb0001189 | WorkQueue: StartTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3 Timeout=%4 IsPeriodic=%5\r\n
0xb000118a | WorkQueue: ExecuteTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3\r\n
0xb000118d | UpdateSelectWorkQueuesCpuGroupMask Enter ProcessorGroup=%1 ProcessorMask=%2\r\n
0xb000118e | UpdateSelectWorkQueuesCpuGroupMask Leave ProcessorGroup=%1 ProcessorMask=%2 hr=%3\r\n
0xb000118f | SubscribeCpuGroupMaskChangeWNF queryStatus=%1 subscribeStatus=%2 changeStamp=%3\r\n
0xb0001190 | UpdateWorkqueueCpuGroupMask workQueue=%1 Class=%2 ProcesssorGroup=%3 ProcesssorMask=%4\r\n
0xb0001191 | CpuGroupMaskChangeWnfCallback ChangeStamp=%1 CurChangeStamp=%2 ProcessorGroup=%3 ProcessorMask=%4 Length=%5\r\n
0xb0001192 | SetThreadCpuGroupMask pWorkQueue=%1 Class=%2 Priority=%3 ThreadId=%4 CurProcessorGroup=%5 CurProcessorMask=%6 NewProcessorGroup=%7 NewProcessorMask=%8 status=%9\r\n
0xb0001193 | WorkQueue Start Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001194 | WorkQueue End Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001195 | WorkQueue Debounce: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001196 | WorkQueue Debounce: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001197 | WorkQueue Buffering: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001198 | WorkQueue Buffering: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001199 | Platform AllocIndex start: Platform=%1 WorkQueueID=%2 Index=%3\r\n
0xb000119a | Platform AllocIndex stop: Platform=%1 WorkQueueID=%2 Index=%3\r\n
0xb000119b | Platform Init start: Platform=%1\r\n
0xb000119c | Platform Init stop: Platform=%1\r\n
0xb000119d | Platform Shutdown start: Platform=%1\r\n
0xb000119e | Platform Shutdown stop: Platform=%1\r\n
0xb000119f | Platform Shutdown timeout: Platform=%1\r\n
0xb00011a0 | Platform Shutdown_WorkQueue start: Platform=%1 workqueue=%2 index=%3\r\n
0xb00011a1 | Platform Shutdown_WorkQueue stop: Platform=%1 workqueue=%2 index=%3\r\n
0xb00011a2 | WorkQueue RunLimit: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a3 | WorkQueue RunLimit: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a4 | WorkQueue RunLimit: Exceeded workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a5 | TaskGroup: Start TaskGroup=%1\r\n
0xb00011a6 | TaskGroup: End TaskGroup=%1\r\n
0xb00011a7 | TaskGroup RefCount TaskGroup=%1 RefCount=%2\r\n
0xb00011a8 | TaskGroup ObjectCount ObjectCount=%1\r\n
0xb00011a9 | TaskGroup Reinit TaskGroup=%1 TaskID=%2\r\n
0xb1000001 | WorkQueue Queue extended: AsyncResult=%1 AsyncResultVTable=%2\r\n
0xb1000002 | WorkQueue Extended LongRunning: RefCount workQueueID=%1 refcount=%2\r\n
0xb1000003 | WorkQueue extended InvalidUsageAttempt: Platform=%1 WorkQueueID=%2 PrivateQueueIndex=%3\r\n
0xb1000004 | WorkQueue extended InvalidCallbackAttempt: Platform=%1 Callback=%2 WorkQueueID=%3\r\n
0xb1000005 | WorkQueue Extended PlatformRef: Start platform=%1\r\n
0xb1000006 | WorkQueue Extended PlatformRef: Stop platform=%1\r\n
0xb1000007 | WorkQueue Extended PlatformRef: ref platform=%1 ref:%2\r\n
0xb1000008 | WorkQueue Extended RTLock: Start workQueueID=%1\r\n
0xb1000009 | WorkQueue Extended RTLock: Stop workQueueID=%1\r\n
0xb100000a | WorkQueue Extended SetAVMode: Start group=%1 mode=%2\r\n
0xb100000b | WorkQueue Extended SetAVMode: Stop group=%1 mode=%2\r\n
0xb100000c | WorkQueue Extended RTLockAcquire: Start workQueueID=%1\r\n
0xb100000d | WorkQueue Extended RTLockAcquire: Stop workQueueID=%1\r\n
0xb100000e | WorkQueue Extended TimerCallback: Start object=%1 id=%2 mode=%3\r\n
0xb100000f | WorkQueue Extended TimerCallback: Stop object=%1 id=%2 mode=%3\r\n
0xb1000010 | WorkQueue TimerMode: Set workqueue_ptr=%1 workQueueID=%2 Mode=%3\r\n
0xb1000011 | WorkQueue TimerSet: Set workqueue_ptr=%1 workQueueID=%2 Delta=%3\r\n
0xb1000012 | WorkQueue Extended TimerResChange: Start object=%1 id=%2 mode=%3\r\n
0xb1000013 | WorkQueue Extended TimerResChange: Stop object=%1 id=%2 mode=%3\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000247 | WorkQueue: Execute\r\n
0x70000248 | WorkQueue: Queue\r\n
0x7000024c | WorkQueue: Thread\r\n
0x70000253 | MMCSS Registration\r\n
0x7000025a | WorkQueue: Queue_Create\r\n
0x7000025b | WorkQueue: Execute callback\r\n
0x7000025c | WorkQueue: MMCSS Transition\r\n
0x7000025d | WorkQueue: UpdateDeadlines\r\n
0x7000025e | WorkQueue: AddDeadline\r\n
0x7000025f | WorkQueue: AddImmediateDeadline\r\n
0x70000260 | WorkQueue: DeadlineYield\r\n
0x70000261 | WorkQueue: UpdateDeadlineQueue\r\n
0x70000262 | WorkQueue: LongRunning\r\n
0x70000263 | WorkQueue: StartTimer\r\n
0x70000264 | WorkQueue: ExecuteTimer\r\n
0x70000266 | Update Select WorkQueues CpuGroupMask\r\n
0x70000267 | SubscribeCpuGroupMaskChangeWNF\r\n
0x70000268 | UpdateWorkqueueCpuGroupMask\r\n
0x70000269 | CpuGroupMaskChangeWnfCallback\r\n
0x7000026a | SetThreadCpuGroupMask\r\n
0x7000026b | WorkQueue: Debounce\r\n
0x7000026c | WorkQueue: Buffering\r\n
0x7000026d | WorkQueue: Notification\r\n
0x7000026e | Platform: AllocIndex\r\n
0x7000026f | Platform: Init\r\n
0x70000270 | Platform: Shutdown\r\n
0x70000271 | Platform: Shutdown_WorkQueue\r\n
0x70000272 | WorkQueue: RunLimit\r\n
0x70000273 | TaskGroup\r\n
0x71000064 | WorkQueue: Queue Extended\r\n
0x71000065 | WorkQueue: Extended LongRunning\r\n
0x71000066 | WorkQueue: Extended InvalidUsageAttempt\r\n
0x71000067 | WorkQueue: Extended InvalidCallbackAttempt\r\n
0x71000068 | WorkQueue: PlatformRef\r\n
0x71000069 | WorkQueue: RTLock\r\n
0x7100006a | WorkQueue: SetAVMode\r\n
0x7100006b | WorkQueue: RTLockAcquire\r\n
0x7100006c | WorkQueue: TimerCallback\r\n
0x7100006d | WorkQueue: TimerMode\r\n
0x7100006e | WorkQueue: TimerSet\r\n
0x7100006f | WorkQueue: TimerResChange\r\n
0x71000070 | WorkQueue: Lock\r\n
0x90000001 | Microsoft-Windows-RTWorkQueue-Threading\r\n
0x90000002 | RTWorkQueue Threading\r\n
0x91000001 | Microsoft-Windows-RTWorkQueue-Extended\r\n
0x91000002 | RTWorkQueue Extended\r\n
0xb0001153 | WorkQueue Execute: Start workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001154 | WorkQueue Execute: End workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001155 | WorkQueue Queue: WorkQueuePtr=%1 Start threads=%2 AsyncResult=%3\r\n
0xb0001156 | WorkQueue Queue: WorkQueuePtr=%1 End threads=%2 AsyncResult=%3\r\n
0xb0001157 | WorkQueue Thread: Start workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001158 | WorkQueue Thread: End workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001166 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001167 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001178 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001179 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb000117a | WorkQueue Execute Callback: Start workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117b | WorkQueue Execute Callback: End workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117c | WorkQueue MMCSS: Start workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117d | WorkQueue MMCSS: End workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117e | WorkQueue UpdateDeadlines: Start workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb000117f | WorkQueue UpdateDeadlines: End workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb0001180 | WorkQueue AddDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001181 | WorkQueue AddDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001182 | WorkQueue AddImmediateDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001183 | WorkQueue AddImmediateDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001184 | WorkQueue DeadlineYield: Start workQueueID=%1 Delay=%2\r\n
0xb0001185 | WorkQueue DeadlineYield: End workQueueID=%1 Delay=%2\r\n
0xb0001186 | WorkQueue DeadlineQueue: WorkQueuePtr=%1 workQueueID=%2 count=%3 immediateCount=%4 nextDeadline=%5 nextItem=%6\r\n
0xb0001187 | WorkQueue LongRunning: Start workQueueID=%1\r\n
0xb0001188 | WorkQueue LongRunning: End workQueueID=%1\r\n
0xb000118a | WorkQueue: ExecuteTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3\r\n
0xb000118d | UpdateSelectWorkQueuesCpuGroupMask Enter ProcessorGroup=%1 ProcessorMask=%2\r\n
0xb000118e | UpdateSelectWorkQueuesCpuGroupMask Leave ProcessorGroup=%1 ProcessorMask=%2 hr=%3\r\n
0xb000118f | SubscribeCpuGroupMaskChangeWNF queryStatus=%1 subscribeStatus=%2 changeStamp=%3\r\n
0xb0001190 | UpdateWorkqueueCpuGroupMask workQueue=%1 Class=%2 ProcesssorGroup=%3 ProcesssorMask=%4\r\n
0xb0001191 | CpuGroupMaskChangeWnfCallback ChangeStamp=%1 CurChangeStamp=%2 ProcessorGroup=%3 ProcessorMask=%4 Length=%5\r\n
0xb0001192 | SetThreadCpuGroupMask pWorkQueue=%1 Class=%2 Priority=%3 ThreadId=%4 CurProcessorGroup=%5 CurProcessorMask=%6 NewProcessorGroup=%7 NewProcessorMask=%8 status=%9\r\n
0xb0001193 | WorkQueue Start Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001194 | WorkQueue End Notification WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001195 | WorkQueue Debounce: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001196 | WorkQueue Debounce: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001197 | WorkQueue Buffering: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001198 | WorkQueue Buffering: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb0001199 | Platform AllocIndex start: Platform=%1 WorkQueueID=%2 Index=%3\r\n
0xb000119a | Platform AllocIndex stop: Platform=%1 WorkQueueID=%2 Index=%3\r\n
0xb000119b | Platform Init start: Platform=%1\r\n
0xb000119c | Platform Init stop: Platform=%1\r\n
0xb000119d | Platform Shutdown start: Platform=%1\r\n
0xb000119e | Platform Shutdown stop: Platform=%1\r\n
0xb000119f | Platform Shutdown timeout: Platform=%1\r\n
0xb00011a0 | Platform Shutdown_WorkQueue start: Platform=%1 workqueue=%2 index=%3\r\n
0xb00011a1 | Platform Shutdown_WorkQueue stop: Platform=%1 workqueue=%2 index=%3\r\n
0xb00011a2 | WorkQueue RunLimit: Start workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a3 | WorkQueue RunLimit: Stop workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a4 | WorkQueue RunLimit: Exceeded workqueue_ptr=%1 workQueueID=%2 TaskGroup=%3\r\n
0xb00011a5 | TaskGroup: Start TaskGroup=%1\r\n
0xb00011a6 | TaskGroup: End TaskGroup=%1\r\n
0xb00011a7 | TaskGroup RefCount TaskGroup=%1 RefCount=%2\r\n
0xb00011a8 | TaskGroup ObjectCount ObjectCount=%1\r\n
0xb00011a9 | TaskGroup Reinit TaskGroup=%1 TaskID=%2\r\n
0xb00011aa | Platform Init shutdown in progress: Platform=%1\r\n
0xb00011ab | Platform Shutdown aborted: Platform=%1\r\n
0xb0011189 | WorkQueue: StartTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3 Timeout=%4 IsPeriodic=%5\r\n
0xb1000001 | WorkQueue Queue extended: AsyncResult=%1 AsyncResultVTable=%2\r\n
0xb1000002 | WorkQueue Extended LongRunning: RefCount workQueueID=%1 refcount=%2\r\n
0xb1000003 | WorkQueue extended InvalidUsageAttempt: Platform=%1 WorkQueueID=%2 PrivateQueueIndex=%3\r\n
0xb1000004 | WorkQueue extended InvalidCallbackAttempt: Platform=%1 Callback=%2 WorkQueueID=%3\r\n
0xb1000005 | WorkQueue Extended PlatformRef: Start platform=%1\r\n
0xb1000006 | WorkQueue Extended PlatformRef: Stop platform=%1\r\n
0xb1000007 | WorkQueue Extended PlatformRef: ref platform=%1 ref:%2\r\n
0xb1000008 | WorkQueue Extended RTLock: Start workQueueID=%1\r\n
0xb1000009 | WorkQueue Extended RTLock: Stop workQueueID=%1\r\n
0xb100000a | WorkQueue Extended SetAVMode: Start group=%1 mode=%2\r\n
0xb100000b | WorkQueue Extended SetAVMode: Stop group=%1 mode=%2\r\n
0xb100000c | WorkQueue Extended RTLockAcquire: Start workQueueID=%1\r\n
0xb100000d | WorkQueue Extended RTLockAcquire: Stop workQueueID=%1\r\n
0xb100000e | WorkQueue Extended TimerCallback: Start object=%1 id=%2 mode=%3\r\n
0xb100000f | WorkQueue Extended TimerCallback: Stop object=%1 id=%2 mode=%3\r\n
0xb1000010 | WorkQueue TimerMode: Set workqueue_ptr=%1 workQueueID=%2 Mode=%3\r\n
0xb1000011 | WorkQueue TimerSet: Set workqueue_ptr=%1 workQueueID=%2 Delta=%3\r\n
0xb1000012 | WorkQueue Extended TimerResChange: Start object=%1 id=%2 mode=%3\r\n
0xb1000013 | WorkQueue Extended TimerResChange: Stop object=%1 id=%2 mode=%3\r\n
0xb1000014 | WorkQueue Extended Lock: object=%1\r\n
0xb1000015 | WorkQueue Extended Unlock: object=%1\r\n
0xb1000016 | WorkQueue Extended Lock RefCount: object=%1 extRefCount=%2 IntRefCount=%3\r\n

### 12.0.9600.16384

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x31000000 | Info\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000247 | WorkQueue: Execute\r\n
0x70000248 | WorkQueue: Queue\r\n
0x7000024c | WorkQueue: Thread\r\n
0x70000253 | MMCSS Registration\r\n
0x7000025a | WorkQueue: Queue_Create\r\n
0x7000025b | WorkQueue: Execute callback\r\n
0x7000025c | WorkQueue: MMCSS Transition\r\n
0x71000064 | WorkQueue: Queue Extended\r\n
0x90000001 | Microsoft-Windows-RTWorkQueue-Threading\r\n
0x90000002 | RTWorkQueue Threading\r\n
0x91000001 | Microsoft-Windows-RTWorkQueue-Extended\r\n
0x91000002 | RTWorkQueue Extended\r\n
0xb0001153 | WorkQueue Execute: Start workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001154 | WorkQueue Execute: End workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001155 | WorkQueue Queue: WorkQueuePtr=%1 Start threads=%2 AsyncResult=%3\r\n
0xb0001156 | WorkQueue Queue: WorkQueuePtr=%1 End threads=%2 AsyncResult=%3\r\n
0xb0001157 | WorkQueue Thread: Start workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001158 | WorkQueue Thread: End workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001166 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001167 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001178 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001179 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb000117a | WorkQueue Execute Callback: Start workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb000117b | WorkQueue Execute Callback: End workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb000117c | WorkQueue MMCSS: Start workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117d | WorkQueue MMCSS: End workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb1000001 | WorkQueue Queue extended: AsyncResult=%1 AsyncResultVTable=%2\r\n

### 12.0.10586.0

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000247 | WorkQueue: Execute\r\n
0x70000248 | WorkQueue: Queue\r\n
0x7000024c | WorkQueue: Thread\r\n
0x70000253 | MMCSS Registration\r\n
0x7000025a | WorkQueue: Queue_Create\r\n
0x7000025b | WorkQueue: Execute callback\r\n
0x7000025c | WorkQueue: MMCSS Transition\r\n
0x7000025d | WorkQueue: UpdateDeadlines\r\n
0x7000025e | WorkQueue: AddDeadline\r\n
0x7000025f | WorkQueue: AddImmediateDeadline\r\n
0x70000260 | WorkQueue: DeadlineYield\r\n
0x70000261 | WorkQueue: UpdateDeadlineQueue\r\n
0x70000262 | WorkQueue: LongRunning\r\n
0x70000263 | WorkQueue: StartTimer\r\n
0x70000264 | WorkQueue: ExecuteTimer\r\n
0x70000266 | Update Select WorkQueues CpuGroupMask\r\n
0x70000267 | SubscribeCpuGroupMaskChangeWNF\r\n
0x70000268 | UpdateWorkqueueCpuGroupMask\r\n
0x70000269 | CpuGroupMaskChangeWnfCallback\r\n
0x7000026a | SetThreadCpuGroupMask\r\n
0x71000064 | WorkQueue: Queue Extended\r\n
0x90000001 | Microsoft-Windows-RTWorkQueue-Threading\r\n
0x90000002 | RTWorkQueue Threading\r\n
0x91000001 | Microsoft-Windows-RTWorkQueue-Extended\r\n
0x91000002 | RTWorkQueue Extended\r\n
0xb0001153 | WorkQueue Execute: Start workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001154 | WorkQueue Execute: End workqueue_ptr=%1 workQueueID=%2 AsyncResult=%3\r\n
0xb0001155 | WorkQueue Queue: WorkQueuePtr=%1 Start threads=%2 AsyncResult=%3\r\n
0xb0001156 | WorkQueue Queue: WorkQueuePtr=%1 End threads=%2 AsyncResult=%3\r\n
0xb0001157 | WorkQueue Thread: Start workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001158 | WorkQueue Thread: End workqueue_ptr=%1 WorkQueueID=%2 ThreadCount=%3\r\n
0xb0001166 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001167 | MMCSS Registration Enter Queue=%1 ThreadID=%2 Handle=%3 Error=%4 Class=%5 Pri=%6 TaskID=%7\r\n
0xb0001178 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb0001179 | WorkQueue Queue: WorkQueuePtr=%1 WorkQueueID=%2\r\n
0xb000117a | WorkQueue Execute Callback: Start workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117b | WorkQueue Execute Callback: End workqueue_ptr=%1 workQueueID=%2 BaseWorkQueueID=%3 ThreadID=%4 AsyncResult=%5 AsyncResultPtr=%6 LongRunning=%7\r\n
0xb000117c | WorkQueue MMCSS: Start workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117d | WorkQueue MMCSS: End workqueue_ptr=%1 workQueueID=%2 Class=%3 Pri=%4\r\n
0xb000117e | WorkQueue UpdateDeadlines: Start workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb000117f | WorkQueue UpdateDeadlines: End workqueue_ptr=%1 workQueueID=%2 TaskId=%3 Previous=%4 Next=%5 Delay=%6\r\n
0xb0001180 | WorkQueue AddDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001181 | WorkQueue AddDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001182 | WorkQueue AddImmediateDeadline: Start workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001183 | WorkQueue AddImmediateDeadline: End workqueue_ptr=%1 workQueueID=%2 Item=%3 global=%4 delta=%5 \r\n
0xb0001184 | WorkQueue DeadlineYield: Start workQueueID=%1 Delay=%2\r\n
0xb0001185 | WorkQueue DeadlineYield: End workQueueID=%1 Delay=%2\r\n
0xb0001186 | WorkQueue DeadlineQueue: WorkQueuePtr=%1 workQueueID=%2 count=%3 immediateCount=%4 nextDeadline=%5 nextItem=%6\r\n
0xb0001187 | WorkQueue LongRunning: Start workQueueID=%1\r\n
0xb0001188 | WorkQueue LongRunning: End workQueueID=%1\r\n
0xb0001189 | WorkQueue: StartTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3 Timeout=%4 IsPeriodic=%5\r\n
0xb000118a | WorkQueue: ExecuteTimer QueuePtr=%1 QueueID=%2 TimerPtr=%3\r\n
0xb000118d | UpdateSelectWorkQueuesCpuGroupMask Enter ProcessorGroup=%1 ProcessorMask=%2\r\n
0xb000118e | UpdateSelectWorkQueuesCpuGroupMask Leave ProcessorGroup=%1 ProcessorMask=%2 hr=%3\r\n
0xb000118f | SubscribeCpuGroupMaskChangeWNF queryStatus=%1 subscribeStatus=%2 changeStamp=%3\r\n
0xb0001190 | UpdateWorkqueueCpuGroupMask workQueue=%1 Class=%2 ProcesssorGroup=%3 ProcesssorMask=%4\r\n
0xb0001191 | CpuGroupMaskChangeWnfCallback ChangeStamp=%1 CurChangeStamp=%2 ProcessorGroup=%3 ProcessorMask=%4 Length=%5\r\n
0xb0001192 | SetThreadCpuGroupMask pWorkQueue=%1 Class=%2 Priority=%3 ThreadId=%4 CurProcessorGroup=%5 CurProcessorMask=%6 NewProcessorGroup=%7 NewProcessorMask=%8 status=%9\r\n
0xb1000001 | WorkQueue Queue extended: AsyncResult=%1 AsyncResultVTable=%2\r\n
