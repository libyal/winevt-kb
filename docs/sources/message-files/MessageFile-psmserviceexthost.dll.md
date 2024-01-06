## psmserviceexthost.dll

Path: %SystemRoot%\system32\PsmServiceExtHost.dll

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x11000003 | Information\r\n
0x11000005 | Error\r\n
0x11000012 | Production Circular\r\n
0x11000013 | Production Critical\r\n
0x11000015 | SelfHost Critical\r\n
0x11000016 | DevPlat Circular\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x31000065 | Error\r\n
0x51000001 | Critical\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x51000005 | Verbose\r\n
0x91000001 | Microsoft-Windows-ResourceManager\r\n
0xb1000064 | Resource Enforcer Set Apply Status=%1, ProcessId=%2, Priority=%3, CpuReserve=%4, CpuHardLimit=%5, FreezeProcess=%6, MemoryLimit=%7, NoCpuReservation=%8\r\n
0xb1000067 | Resource Enforcer Message, Flags=%1, ProcessId=%2, ProcessCommit=%3 \r\n
0xb1000069 | Resource Enforcer NT Error, Function=%1, Line=%2, NTSTATUS Error=%3 \r\n
0xb100006a | Resource Swap Job, Status=%1, ProcessId=%2, JobHandle=%3\r\n
0xb100006b | Resource Empty Process, Win32 Code=%1, ProcessId=%2, Flags=%3\r\n
0xb1000190 | Resource Manager: Low Memory Handler: Available Physical memory is low.\r\n
0xb1000191 | Resource Manager: Low Memory Handler: Available Physical memory is healthy.\r\n
0xb1000192 | Resource Manager: Low Memory Handler: Commit memory is low.\r\n
0xb1000193 | Resource Manager: Low Memory Handler: Commit memory is healthy.\r\n
0xb1000194 | Resource Manager: Low Memory Handler: Starting.\r\n
0xb1000195 | Resource Manager: Low Memory Handler: Waiting.\r\n
0xb1000196 | Resource Manager: Low Memory Handler: Terminating pid %1.\r\n
0xb1000197 | Resource Manager: Low Memory Handler: Memory is low but there is no one to terminate.\r\n
0xb1000198 | Resource Manager: SHTerminateProcessForOOM pid=%1 cbAllocation=%2 fReboot=%3.\r\n
0xb1000199 | Resource Manager: Low Memory Handler: Commit memory is low. Rebooting. Commit=[%1] CommitPeak=[%2] CommitLimit=[%3] SharedCommit=[%4] NonPagedPool=[%5] PagedPool=[%6]\r\n
0xb100019a | Resource Manager: Low Memory Handler: NonPaged pool memory is low.\r\n
0xb100019b | Resource Manager: Low Memory Handler: NonPaged pool memory is healthy.\r\n
0xb100019c | Resource Manager: Process being applied is already dead - PID=%1\r\n
0xb100019d | Resource Manager: ApplyResourceSet - pResSet=%1, HR=%2, MemLimit=%3, PriorityClass=%4, PID=%5, Type=%6, Terminal=%7\r\n
0xb100019e | Resource Manager: UnapplyResourceSet - pResSet=%1, HR=%2, PID=%3, Type=%4, Terminal=%5\r\n
0xb100019f | Resource Manager: OnProcessTerminated - PID=%1\r\n
0xb10001a0 | Resource Manager: OnProcessCommitWarning - PID=%1, HR=%2, cbCommit=%3\r\n
0xb10001a1 | Resource Manager: TerminateProcessForOom - PID=%1, cbFailed=%2, fReboot=%3\r\n
0xb10001a2 | Resource Manager: ResourceSet::CreateInstance - pResSet=%1, HR=%2, Type=%3, Pending=%4\r\n
0xb10001a3 | Resource Manager: ReleaseResources - pResSet=%1, HR=%2, Type=%3, Terminal=%4\r\n
0xb10001a4 | Resource Manager: Low Memory Handler: NeedCommit=%1\r\n
0xb10001a5 | Resource Manager: Low Memory Handler: NeedPhysical=%1\r\n
0xb10001a6 | Resource Manager: Low Memory Handler: NeedNonPagedPool=%1\r\n
0xb10001a7 | Resource Manager: Low Memory Handler: NeedMemory=%1, NeedCommit=%2, NeedPhysical=%3, NeedNonPagedPool=%4\r\n
0xb10001a8 | Resource Manager: Low Memory Handler: CommitMemory critically low, and there are no processes to terminate. Rebooting.\r\n
0xb10001aa | Resource Manager: AcquireResourceSet - pResSet=%1, HR=%2, Type=%3, Pending=%4, Previous=%5\r\n
0xb10001ac | Resource Manager: AcquireResources - cRequests=%1, priority=%2, cmsAcquireDelay=%3, pidRequesting=%4, fForcePending=%5, pendtype=%6, HR=%7\r\n
0xb10001b3 | External Resource Manager: RegisterResources - ResourceType=%1, Amount=%2, HR=%3\r\n
0xb10001b4 | External Resource Manager: RMAccessCheck - ResourceType=%1, PID=%2, HR=%3\r\n
0xb10001b5 | External Resource Manager: AcquireResources_ServerThunk - pResourceHandle=%1, cRequests=%2, priority=%3, callerPid=%4, pidRequesting=%5, grfFlags=%6, pendtype=%7, fPending=%8, HR=%9\r\n
0xb10001b6 | External Resource Manager: RMAvailabilityCheck - cRequests=%1, priority=%2, pidRequesting=%3, HR=%4\r\n
0xb10001b7 | External Resource Manager: RMGetNotification - pResourceHandle=%1, HR=%2\r\n
0xb10001b8 | External Resource Manager: RMReleaseResources_Manager - pResourceHandle=%1, HR=%2\r\n
0xb10001b9 | External Resource Manager: RMQueueMessages - pResourceHandle=%1, ExternalNotificationType=%2, ResourceType=%3, ReleaseReason=%4, HR=%5\r\n
0xb10001ba | Resource Manager: Block resource set (%2) for product %1 with mask %3 block(%4), HR=%5\r\n
0xb10001bb | Resource Manager: Can Block resource set (%2) for product %1 with mask %3 block(%4), HR=%5\r\n
0xb10001bc | Resource Manager: Check and Revoke resource set for product %1 revoke(%2), HR=%3\r\n
0xb10001bd | Resource Manager: Check and Revoke resource set for PFM %1\r\n
0xb10001be | Resource Manager: Check and Revoke resource set by type for PFM %1(%2), HR=%3\r\n
0xb10001bf | Resource Manager: OnApplicationTerminated - PSMKey=%1, ActivationType=%2\r\n
0xb10001c0 | Resource Manager: ReclaimMemory - pResSet=%1, HR=%2\r\n
0xb10001c1 | External Resource Manager: Watchdog Expired. pResourceHandle=%1, App PID=%2\r\n
0xb10001c2 | Resource Manager: AcquireAdditionalResources - pResSet=%1, Cpu=%2, Mem=%3, Io=%4, HR=%5, Pending=%6, TempRS=%7\r\n
0xb10001c3 | Resource Manager: CompleteAcquireAdditionalResources - pResSet=%1, TempRS=%2\r\n
0xb10001c4 | Resource Manager: RevokeResources - PSMKey=%1, ActivationType=%2\r\n
0xb10001c5 | Resource Manager: MemoryLimitNotification - PSMKey=%1, Sid=%2, Session=%3, ActivationType=%4, PrivUsage=%5, SharedUsage=%6, Adjustment=%9, Cap=%10, LowLimit=%7, HighLimit=%8\r\n
0xb10001c6 | Resource Manager: ForceReleaseExternalResources - PID=%1\r\n
0xb10001c7 | Resource Manager: Acquiring Memory for FG sharing. FG Resource Set = %1, Amount = %2, HR = %3\r\n
0xb10001c8 | Resource Manager: Releasing Memory for FG sharing. FG Resource Set = %1, Amount = %2, HR = %3\r\n
0xb10001c9 | Resource Manager: Host terminated due to quota exhaustion - PSMKey=%1 ActivationType=%2\r\n
0xb10001ca | Resource Manager: Failed to transition FG memory sharing. New Resource Set = %1, HR = %2\r\n
0xb10001cb | Resource Manager: ModernResourceEnforcer failed! - PSMKey=%1, ActivationType=%2  HR = %3\r\n
0xb10001cd | Resource Manager: OnAcquired - pResSet=%1, IsLegacy=%2, CallbackId=%3 HR=%4\r\n
0xb10001ce | Resource Manager: MemoryLimitNotification - PSMKey=%1, ActivationType=%2, Sid=%3, Session=%4, Cap=%6, LowLimit=%7, HighLimit=%8, HR=%5\r\n
0xb10001cf | Resource Manager: TerminateModernAppForOOM PSMKey=%1, UserSid=%2, SessionId=%3, ActivationType=%4, AllocationSize=%6, ShouldReboot=%7  HR=%5\r\n
0xb10001d0 | Resource Manager: RevokeResources - pResSet=%1, PID=%2\r\n
0xb10001d1 | Resource Manager: ReleaseTerminal - pResSet=%1 PID=%2 Product=%3 ActivationType=%4 HR=%5\r\n
0xb10001d2 | Resource Manager: UnapplyResourceSet_Modern - pResSet=%1, HR=%2\r\n
0xb1000226 | PsmServiceExtHost: Failed in call to BiTerminateApplicationHost - Status=%1, PsmKey=%2, HostJobType=%3, Action=%4, Force=%5\r\n
0xb1002007 | [Info]: %1\r\n
0xb1002008 | Modern Enforcer: Failed to call SetApplicationProperties - Status=%1, PsmKey=%2, User=%3, Session=%4, HostJobType=%5: (%11, %12, %13, %14, %15) - CpuRate=%6, HardMemoryLimit=%7, NotifyMemoryLowLimit=%8, NotifyMemoryHighLimit=%9, Priority=%10\r\n
0xb1002009 | Modern Enforcer: Failed to call QueryApplicationProperties - Status=%1, PsmKey=%2, User=%3, Session=%4, HostJobType=%5, CpuRate=%6, HardMemoryLimit=%7, NotifyMemoryLowLimit=%8, NotifyMemoryHighLimit=%9, Priority=%10\r\n
0xb100200a | Modern Enforcer: Failed to call QueryMemoryUsage - Status=%1, PsmKey=%2, User=%3, Session=%4, HostJobType=%5, MemoryUsage=%6\r\n
0xb100200b | Modern Enforcer: Failed to call QuerySharedCommit- Status=%1, PsmKey=%2, User=%3, Session=%4, HostJobType=%5, SharedMemoryUsage=%6\r\n
0xb100200c | Modern Enforcer: SetApplicationProperties - Status=%1, PsmKey=%2, User=%3, Session=%4, HostJobType=%5: (%11, %12, %13, %14, %15) - CpuRate=%6, HardMemoryLimit=%7, NotifyMemoryLowLimit=%8, NotifyMemoryHighLimit=%9, Priority=%10\r\n
0xb100200d | Modern Enforcer: QueryApplicationProperties - Status=%1, PsmKey=%2, User=%3, Session=%4, HostJobType=%5, CpuRate=%6, HardMemoryLimit=%7, NotifyMemoryLowLimit=%8, NotifyMemoryHighLimit=%9, Priority=%10\r\n
0xb1002012 | Modern Enforcer: PSM GroupOwnershipNotification - Status=%1, PsmKey=%2, User=%3, Session=%4, HostJobType=%5, %6, fUpdateRate=%7\r\n
0xb1002013 | Modern Enforcer: PSM HostEmpty Notification - PsmKey=%1, User=%2, Session=%3, HostJobType=%4\r\n
0xb1002014 | Modern Enforcer: PsmApplicationStateNotification - User=%1, Session=%2, PsmKey=%3, State=%4\r\n
0xb1002015 | Modern Enforcer: PsmHostStateNotification - User=%1, Session=%2, PsmKey=%3, HostJobType=%4, State=%5\r\n
0xb1002016 | Modern Enforcer: SwapModernApplication - Status=%1, PsmKey=%2, User=%3, Session=%4\r\n
0xb1002017 | Modern Enforcer: EmptyModernApplication - Status=%1, PsmKey=%2, User=%3, Session=%4, ProcessId=%5, EmptyFlags=%6\r\n
0xb10101d7 | Resource Manager: AcquireAdditionalResources - pResSet=%1, Mem=%2, HR=%3, Pending=%4, TempRS=%5\r\n
0xd1000001 | UiForeground\r\n
0xd1000002 | HighPriorityBackgroundAgent\r\n
0xd1000003 | HighPriorityBackgroundTransfer\r\n
0xd1000004 | BackgroundWorker\r\n
0xd1000005 | BackgroundAudioPlayer\r\n
0xd1000006 | VoipActiveCallLegacy\r\n
0xd1000007 | VoipActiveCallForeground\r\n
0xd1000008 | VoipActiveCallBackground\r\n
0xd1000009 | VoipForegroundWorker\r\n
0xd100000a | VoipWorker\r\n
0xd100000b | ContinuousBackgroundExecution\r\n
0xd100000c | UiPausing\r\n
0xd100000d | UiPaused\r\n
0xd100000e | UiFrozen\r\n
0xd100000f | OemBackgroundAgent\r\n
0xd1000010 | EmCreateProcess\r\n
0xd1000011 | EmCreateProcessNormalPriority\r\n
0xd1000012 | PushTriggerTask\r\n
0xd1000013 | GeofenceTask\r\n
0xd1000014 | BackgroundTask\r\n
0xd1000015 | FileProviderTarget\r\n
0xd1000016 | ShareDataPackageHost\r\n
0xd1000017 | LongRunningBluetooth\r\n
0xd1000018 | LongRunningControlChannel\r\n
0xd1000019 | SMSNABSync\r\n
0xd100001a | VideoTranscoding\r\n
0xd100001b | WebAuthSignIn\r\n
0xd100001c | BackgroundTransfer\r\n
0xd100001d | OemTask\r\n
0xd100001e | ResourceIntensive\r\n
0xd100001f | ForegroundAgent\r\n
0xd1000020 | DefaultPPLE\r\n
0xd1000021 | UiLockScreen\r\n
0xd1000022 | UiOverlay\r\n
0xd1000023 | UiForegroundDNK\r\n
0xd1000024 | UiPausedDNK\r\n
0xd1000025 | UiFrozenDNK\r\n
0xd1000026 | PendingDefaultPPLE\r\n
0xd1000027 | CalendarProviderAsChild\r\n
0xd1000028 | UiPausedHighPriority\r\n
0xd1000029 | UiFrozenHighPriority\r\n
0xd100002a | UiModernForeground\r\n
0xd100002b | BackgroundTaskDebug\r\n
0xd100002c | Vpn\r\n
0xd100002d | ForegroundCachedFileUpdater\r\n
0xd100002e | BackgroundCachedFileUpdater\r\n
0xd100002f | PreinstallTask\r\n
0xd1000030 | ShortRunningBluetooth\r\n
0xd1000031 | LongRunningSensor\r\n
0xd1000032 | DefaultModernBackgroundTask\r\n
0xd1000033 | ForegroundTaskCompletion\r\n
0xd1000034 | BackgroundTaskCompletion\r\n
0xd1000035 | JumboForegroundAgent\r\n
0xd1000036 | VoipSuspendedBackground\r\n
0xd1000037 | ApplicationService\r\n
0xd1000038 | UiPausingLowPriority\r\n
0xd1000039 | GenericExtendedExecution\r\n
0xd100003a | Child\r\n
0xd100003b | Cpu\r\n
0xd100003c | CommitMemory\r\n
0xd100003d | InputOutput\r\n
0xd100003e | Microphone\r\n
0xd100003f | Camera\r\n
0xd1000040 | Proximity\r\n
0xd1000041 | BrowserControl\r\n
0xd1000042 | SensorFusion\r\n
0xd1000043 | Gyro\r\n
0xd1000044 | Compass\r\n
0xd1000045 | Accelerometer\r\n
0xd1000046 | Vibrator\r\n
0xd1000047 | CameraButton\r\n
0xd1000048 | Token\r\n
0xd1000049 | Push\r\n
0xd100004a | SpeechSynthesis\r\n
0xd100004b | SpeechRecognition\r\n
0xd100004c | CoreAudioOut\r\n
0xd100004d | CoreAudioIn\r\n
0xd100004e | CoreAudioVoip\r\n
0xd100004f | InterruptiveAudio\r\n
0xd1000050 | TelephonyHardware\r\n
0xd1000051 | MultimediaAudioOut\r\n
0xd1000052 | MultimediaAudioProcessor\r\n
0xd1000053 | MultimediaVideoOut\r\n
0xd1000054 | MultimediaVideoIn\r\n
0xd1000055 | MultimediaVideoProcessor\r\n
0xd1000056 | InterruptiveUI\r\n
0xd1000057 | CanSponsor\r\n
0xd1000058 | AppService\r\n
0xd1000059 | HighPriorityNetworking\r\n
0xd100005a | AudioPlaceholder1\r\n
0xd100005b | AudioPlaceholder2\r\n
0xd100005c | AudioPlaceholder3\r\n
0xd100005d | AudioPlaceholder4\r\n
0xd100005e | AudioPlaceholder5\r\n
0xd100005f | AudioPlaceholder6\r\n
0xd1000060 | AudioPlaceholder7\r\n
0xd1000061 | AudioPlaceholder8\r\n
0xd1000062 | AudioPlaceholder9\r\n
0xd1000063 | AudioPlaceholder10\r\n
0xd1000064 | AudioPlaceholder11\r\n
0xd1000065 | AudioPlaceholder12\r\n
0xd1000066 | AudioPlaceholder13\r\n
0xd1000067 | AudioPlaceholder14\r\n
0xd1000068 | AudioPlaceholder15\r\n
0xd1000069 | LegacyNetworkingPowerManagement\r\n
0xd100006a | Max\r\n
0xd100006b | OnAcquired\r\n
0xd100006c | Release\r\n
0xd100006d | OnHold\r\n
0xd100006e | OnUnHold\r\n
0xd100006f | OnAccessLost\r\n
0xd1000070 | LostAccess\r\n
0xd1000071 | Preempted\r\n
0xd1000072 | ProcessTerminated\r\n
0xd1000073 | Release\r\n
0xd1000074 | Acquire\r\n
0xd1000075 | Active\r\n
0xd1000076 | Brokered\r\n
0xd1000077 | Sandboxed\r\n
0xd1000078 | Quiescing\r\n
0xd1000079 | Halted\r\n
0xd100007a | TerminatePending\r\n
0xd100007b | Terminated\r\n
0xd100007c | HaltPending\r\n
0xd100007d | Deleted\r\n
0xd100007e | Initialized\r\n
0xd100007f | OutSwapped\r\n
0xd1000080 | Invalid\r\n
0xd1000081 | Empty\r\n
0xd1000082 | AcquireGroupScheduling\r\n
0xd1000083 | ReleaseGroupScheduling\r\n
0xd1000084 | QuotaPolicySuspend\r\n
0xd1000085 | QuotaPolicyResume\r\n
0xd1000086 | Invalid\r\n
0xd1000087 | TerminateHostWithCancel\r\n
0xd1000088 | TerminateHostWithoutCancel\r\n
0xd1000089 | TerminateHostIfNoActiveTasks\r\n
