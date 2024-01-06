## microsoft-windows-appmodelexecevents.dll

Path: %SystemRoot%\system32\Microsoft-Windows-AppModelExecEvents.dll

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x10000006 | ExecMan\r\n
0x10000009 | TaskHost\r\n
0x1000000d | Sqm\r\n
0x1000000f | Lifetime Manager\r\n
0x10000010 | ForegroundManager\r\n
0x10000011 | Background Manager\r\n
0x10000012 | Production Circular\r\n
0x10000013 | Production Critical\r\n
0x10000014 | SelfHost Circular\r\n
0x10000015 | SelfHost Critical\r\n
0x10000016 | DevPlat Circular\r\n
0x10000017 | VOIP\r\n
0x1000001b | Activation Manager\r\n
0x1000001c | AgHost\r\n
0x10000020 | Telemetry\r\n
0x10000021 | ExtendedExecutionClient\r\n
0x10000022 | OnDemandBroker\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000007 | Resume\r\n
0x30000008 | Suspend\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-AppModelExecEvents\r\n
0xb0000064 | DepMgr: Removed suspension group from the graph, PsmKey=%1\r\n
0xb0000065 | Not set app %1 into halted state because it should wait for other apps in the package halted first\r\n
0xb0000066 | Not set app %1 into halted state because other app in the package have not finished quiescing\r\n
0xb0000067 | Not terminate app %1, because target app %2 state = %3\r\n
0xb0000068 | Updated current dependency graph (Removal : %1) with Source %2 and Target %3 for type %4 in return %5\r\n
0xb0000069 | Default time for %1 overridden to %2 ms\r\n
0xb000006a | Creating hang report\r\n
0xb000006b | Window %1 is hung in foreground\r\n
0xb000006c | Window %1 is no longer hung in foreground\r\n
0xb000006d | Waiting for WER reporting to finish on app %1\r\n
0xb000006e | Hang reporting finished on app %1.  App termination status: %2\r\n
0xb000006f | Hung reporting finished on window %1 with result %2\r\n
0xb0000070 | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb0000071 | _SubmitActivationHangWerReport(stop): Aumid=%1, result=%2\r\n
0xb0000072 | _UnregisterForStateChanges: fPackageLevel=%1, HRESULT is %2. Cookie is %3\r\n
0xb0000073 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000074 | Canceled launch grace timer, PsmKey=%1\r\n
0xb0000075 | _InitializeLaunchGraceContext: Aumid=%1, fExtendedLaunch=%2, fEventExists=%3\r\n
0xb0000076 | App %1 successfully launched and its launch grace period expired: removing suspend exemption\r\n
0xb0000077 | Forcefully terminating app, Aumid=%1 flags=%2, reason=%3\r\n
0xb0000078 | CheckTerminationBeforeSwitch: Should terminate: %1, Aumid=%2, HRESULT=%3, reason=%4, fIsMisbehaving=%5\r\n
0xb0000079 | Termination requested for %1 - flags %2\r\n
0xb000007a | Failing TerminateApp due to pending task completions: %1\r\n
0xb000007b | Terminating %1 immediately\r\n
0xb000007c | Uninstalling background work items for %1\r\n
0xb000007d | Termination of %1 scheduled for %2 ms in future\r\n
0xb000007e | Sent window message to the default immersive browser with HRESULT %1\r\n
0xb000007f | Attempting to terminate app %1 prior to new app launch due to pending termination\r\n
0xb0000080 | EvaluateAndTerminatePid: PID: %1. HRESULT: %2. Package State: %3\r\n
0xb0000081 | Exempting application %1 from suspend while it is being launched\r\n
0xb0000082 | Exemption manager %1 is requesting a higher minimum priority %2 for %3\r\n
0xb0000083 | Debug mode is enabled for %1, so it will run at %2 priority\r\n
0xb0000084 | Handling logoff, %1 will run at %2 priority\r\n
0xb0000085 | Throttling has been disabled, so %1 will run at %2 priority\r\n
0xb0000086 | Suspend denied due to new key debounce, PsmKey=%1\r\n
0xb0000087 | Suspend denied due to debug mode, PsmKey=%1\r\n
0xb0000088 | Not suspending application %1 due to exemption %2\r\n
0xb0000089 | _EvaluateAndSuspendApplication: PsmKey=%1, fIsSuspendAllowed=%2, HRESULT=%3\r\n
0xb000008a | _ReevaluatePolicy: Ignoring debug mode app, PsmKey=%1\r\n
0xb000008b | ManagePreExistingApps(start)\r\n
0xb000008c | ManagePreExistingApps: PsmKey=%1, Aumid=%2, hr=%3\r\n
0xb000008d | ManagePreExistingApps(stop)\r\n
0xb000008e | RequestSuspendTimeout called for application %1 and timeout %2\r\n
0xb000008f | Debug mode enabled, PkgFamilyName=%1\r\n
0xb0000090 | Debug mode disabled, PkgFamilyName=%1\r\n
0xb0000091 | Set Package %1, Timeout to %2\r\n
0xb0000092 | ResumeDebugModePackage(start): package=%1\r\n
0xb0000093 | ResumeDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000094 | SuspendDebugModePackage(start): package=%1\r\n
0xb0000095 | SuspendDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000096 | MultiAppSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000097 | MultiAppSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb0000098 | MultiPackageSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000099 | MultiPackageSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009a | MultiPackageSuspendAndPendTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb000009b | MultiPackageSuspendAndPendTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009c | TerminateSync(start): PsmKey=%1, type=%2, reason=%3\r\n
0xb000009d | TerminateSync(stop): PsmKey=%1, hrLogReason=%2, hrTermination=%3\r\n
0xb000009e | TerminatePackageSync(start): Package=%1, type=%2, reason=%3\r\n
0xb000009f | TerminatePackageSync(stop): Package=%1, fPlmKnowsPackage=%2, HRESULT=%3\r\n
0xb00000a0 | _TerminateAllSuspendedApplications(start)\r\n
0xb00000a1 | _TerminateAllSuspendedApplications(stop): HRESULT=%1\r\n
0xb00000a2 | Application %1 is blocking Connected Standby\r\n
0xb00000a3 | Exiting Connected Standby\r\n
0xb00000a4 | All packages have been suspended or terminated. Notify PDC. Call to PdcNotificationClientAcknowledge() returned %1\r\n
0xb00000a5 | Kernel State Change Callback: There were %1 PIDs present in the callback data\r\n
0xb00000a6 | Kernel State Change Callback: The state source was %1\r\n
0xb00000a7 | PDC_CONTROL_ABORT: PdcNotificationClientAcknowledge(STATUS_SUCCESS) returned %1\r\n
0xb00000a8 | Not terminating application %1 in _EvaluateAndTerminateApplication because it contains a running IImmersiveApplication\r\n
0xb00000a9 | Not terminating application %1 in _EvaluateAndTerminateApplication because it is a long running app\r\n
0xb00000aa | Not terminating application %1 in _EvaluateAndTerminateApplication due to pending task completion\r\n
0xb00000ab | Not terminating application %1 in _EvaluateAndTerminateApplication due to Launch Grace\r\n
0xb00000ac | Not terminating application %1 in _EvaluateAndTerminateApplication due to debug mode\r\n
0xb00000ad | Not terminating application %1 in _EvaluateAndTerminateApplication due to application had already been terminated\r\n
0xb00000ae | _EvaluateAndTerminateApplication: Skipping child suspension group, PsmKey=%1\r\n
0xb00000af | An empty application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b0 | Parent allowed suspension for child app, childPsmKey=%1\r\n
0xb00000b1 | GroupChildWithParent: ChildPsmKey=%1, HRESULT=%2\r\n
0xb00000b2 | Call a command line '%1' to notify default browser with result %2\r\n
0xb00000b3 | Read executable path from registry with result %1\r\n
0xb00000b4 | Application %1 was added to PLM Data Store and registering for PSM notification\r\n
0xb00000b5 | Resume the PPLE app %1 when receiving the PSM new key notification\r\n
0xb00000b6 | An orphaned prereq application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b7 | Not terminating dependent application %1 in _EvaluateAndTerminateDependentApplication due other dependency applications\r\n
0xb00000b8 | _EvaluateAndTerminateSourceApplication: Aumid=%1, exemption=%2\r\n
0xb00000b9 | An force termination exemption Application was detected. Setting pending termination for application %1\r\n
0xb00000ba | StateMgr: State queued, PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000bb | StateMgr: OnApplicationStarted set to active, PsmKey=%1\r\n
0xb00000bc | StateMgr: OnApplicationStarted finished, PsmKey=%1, HRESULT=%2\r\n
0xb00000bd | StateMgr: App's current state has changed, PsmKey=%1, state=%2\r\n
0xb00000be | StateMgr: OnApplicationTerminated(start), PsmKey=%1\r\n
0xb00000bf | StateMgr: Application terminated signaled, PsmKey=%1\r\n
0xb00000c0 | StateMgr: OnApplicationTerminated(stop), PsmKey=%1\r\n
0xb00000c1 | StateMgr: GetTerminateSyncData, PsmKey=%1, hr=%2\r\n
0xb00000c2 | StateMgr: _ProcessStateQueue(start): PsmKey=%1, state=%2\r\n
0xb00000c3 | StateMgr: _ProcessStateQueue(stop): PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000c4 | StateMgr: Queue's pause state has changed to %2, PsmKey=%1\r\n
0xb00000c5 | StateMgr: App's committed state has changed, PsmKey=%1, state=%2\r\n
0xb00000c6 | Enabling debug mode on package %1\r\n
0xb00000c7 | Disabling debug mode on package %1\r\n
0xb00000c8 | Suspending package %1 via debug API. HRESULT: %2\r\n
0xb00000c9 | Resuming package %1 via debug API. HRESULT: %2\r\n
0xb00000ca | Terminating package %1 via debug API. HRESULT: %2\r\n
0xb00000cb | Default time for %1 overridden to %2 ms\r\n
0xb00000cc | ReportActivationHangSync: Halt application Aumid=%1, result=%2\r\n
0xb00000cd | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb00000ce | _SubmitActivationHangWerReport(stop): Aumid=%1 canceled(%2) result=%3\r\n
0xb00000cf | PLM doesn't swap out application %1 due to its swap state %2\r\n
0xb00000d0 | PLM termination policy started on background thread because application %1 failed to outswap\r\n
0xb00000d1 | PLM termination policy finished. Outswapping returned status %1\r\n
0xb00000d2 | PLM memory policy will be aggressive because this is a disconnected session\r\n
0xb00000d3 | PLM termination policy start\r\n
0xb00000d4 | PLM termination policy stop\r\n
0xb00000d5 | PLM termination policy triggered by in use memory of %1 MiB\r\n
0xb00000d6 | PLM termination policy triggered by commit charge of %1 MiB\r\n
0xb00000d7 | MemoryPolicyWatcherTerminateCommitCharge\r\n
0xb00000d8 | PLM empty policy triggered by in use memory of %1 MB\r\n
0xb00000d9 | PLM memory policy does not allow termination of application %1 for reason %2\r\n
0xb00000da | PLM memory policy allows termination of application %1\r\n
0xb00000db | Application %1 was hidden %2 seconds ago\r\n
0xb00000dc | Application %1 is the clipboard owner\r\n
0xb00000dd | PLM empty policy start\r\n
0xb00000de | PLM empty policy ignoring application %1 with error code %2\r\n
0xb00000df | PLM empty policy finished after emptying %1 MiB\r\n
0xb00000e0 | PLM termination policy enumerated %1 applications\r\n
0xb00000e1 | PLM memory policy chose application %1 as its termination candidate, over old candidate application %2\r\n
0xb00000e2 | PLM memory policy will terminate application %1 with memory size %2 MiB and score %3\r\n
0xb00000e3 | PLM memory policy received MemWatcher event\r\n
0xb00000e4 | PLM memory policy received MemWatcher event\r\n
0xb00000e5 | Package exemption manager denied suspend for %1.  Ref counts are LAUNCH=%2, PSMREG=%3, PSMPENDING=%4\r\n
0xb00000e6 | Package Exemption Manager: ReferenceAdded:%1, %2 ref to application %3. The ref counts are now LAUNCH=%4, PSMREG=%5, and PSMREGPENDING=%6\r\n
0xb00000e7 | Package %1 added to the package data store\r\n
0xb00000e8 | Resetting priority to unpause the suspension group, PsmKey=%1\r\n
0xb00000e9 | Changed the priority of %1 to %2\r\n
0xb00000ea | AllowServiceOfPackages(start): cPackages=%1, fNotifyBi=%2\r\n
0xb00000eb | AllowServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ec | FinishedServiceOfPackages(start): cPackages=%1\r\n
0xb00000ed | FinishedServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ee | AllowUninstallOfPackage(start): package=%1\r\n
0xb00000ef | AllowUninstallOfPackage(stop): package=%1, HRESULT=%2\r\n
0xb00000f0 | Forcefully terminating misbehaving app %1 due to activation failure %2\r\n
0xb00000f1 | App %1: Change = %2\r\n
0xb00000f2 | PsmKey %1 has state %2\r\n
0xb00000f3 | Changing app state through BI, PsmKey=%1, state=%2 terminate action=%3\r\n
0xb00000f4 | Changing the package state of %1 through BI to %2\r\n
0xb00000f5 | OnAfterQuiescing: Quiesce began for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f6 | _CompleteQuiesceHelper: Queued termination for timed-out PsmKey %1\r\n
0xb00000f7 | Quiesce completed for PsmKey=%1, reason=%2, suspendTrigger=%3\r\n
0xb00000f8 | Suspend trigger updated for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f9 | ExtendQuiesceTimeout: PsmKey=%1, request=%2 ms, HRESULT=%3\r\n
0xb00000fa | _CompleteQuiesceHelper: Ignore timed-out PsmKey %1 as is being debugged\r\n
0xb00000fb | ResumeHelper: Application resume(start), PsmKey=%1, reason=%2\r\n
0xb00000fc | ResumeHelper: Application resume(stop), PsmKey=%1, reason=%2, HRESULT=%3\r\n
0xb00000fd | Resume reason updated for PsmKey=%1, reason=%2\r\n
0xb00000fe | RPC 0->1 transition detected for %1\r\n
0xb00000ff | RPC exemption was granted for application %1. KernelRequest Value: %2. Runaway RPC: %3.  RPC Debounce %4\r\n
0xb0000100 | RPC debounce received for package %1\r\n
0xb0000101 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000102 | Application %1 termination is blocked. PreserverProcessRequest = %2, TaskCompletionCategory = %3\r\n
0xb0000103 | PdcSystem activation (Activate = %1). Result = %2\r\n
0xb0000104 | NetworkAudio entries: %1, IsNetworkReferenced: %2\r\n
0xb0000105 | App %1 is Sharing\r\n
0xb0000106 | Share %1 has started in app %2\r\n
0xb0000107 | Share %1 in app %2 has stopped\r\n
0xb0000108 | Queued termination reason updated for PsmKey=%1, reason=%2\r\n
0xb0000109 | ClearTerminationTypesForForgottenPackage(start): PkgFamilyName=%1\r\n
0xb000010a | Cleared termination type for forgotten app, Aumid=%1, HRESULT=%2\r\n
0xb000010b | ClearTerminationTypesForForgottenPackage(stop): PkgFamilyName=%1, HRESULT=%2\r\n
0xb000010c | Writing to termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010d | Reading termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010e | _ExtendForResourceStarvation: PsmKey=%1, TimerType=%2, newRelativeExpirationTimeMs=%3, ElapsedMs=%4, CpuRunningMs=%5, CpuReadyMs=%6, IoNormalMs=%7\r\n
0xb000010f | Foreground resume delay %1 milliseconds\r\n
0xb0000110 | Suspend allowed for %1 - Session not active\r\n
0xb0000111 | Suspend denied due to a visible window or visibility debounce, PsmKey=%1\r\n
0xb0000112 | Suspend denied for %1 - UserRequest non-zero\r\n
0xb0000113 | Suspend denied for %1- failure %2\r\n
0xb0000114 | OnWindowChanged: Aumid=%1, Hwnd=%2, change=%3, fDeferredVisibility=%4, HRESULT=%5\r\n
0xb0000115 | Starting Session Idle Debounce\r\n
0xb0000116 | Session is active\r\n
0xb0000117 | Session is idle\r\n
0xb0000118 | PlmGetPackageFullNameFromAppId, Aumid=%1, HRESULT=%2\r\n
0xb0000119 | Session idle state change -- calling _ReevaluatePolicy\r\n
0xb000011a | RegisterForActivationStateChanges: Act:%1 App:%2 HRESULT is %3. Cookie is %4\r\n
0xb000011b | UnregisterForActivationStateChanges: Cookie is %1\r\n
0xb000011c | Can Auto Terminate app %1 %2\r\n
0xb000011d | TerminateApplicationBeforeActivation(start): Aumid=%1\r\n
0xb000011e | TerminateApplicationBeforeActivation: wait for terminate, Aumid=%1, HRESULT=%2\r\n
0xb000011f | TerminateApplicationBeforeActivation(stop): Aumid=%1, reason=%2, HRESULT=%3\r\n
0xb0000120 | s_SuspendPackagesAtLogOff(start)\r\n
0xb0000121 | s_SuspendPackagesAtLogOff(stop): HRESULT=%1\r\n
0xb0000122 | StateMgr: OnApplicationStarted still halted, PsmKey=%1\r\n
0xb0000123 | Added Task Completion under %1 for application %2\r\n
0xb0000124 | Removed Task Completion under %1 for application %2\r\n
0xb0000125 | Illegal state change happened to App: %1\r\n
0xb0000126 | EnableDebugMode failed: %1\r\n
0xb0000127 | DisableDebugMode: RoDisableDebuggingForPackage failed with result %1\r\n
0xb0000128 | DisableDebugMode: OnDebugModeDisabled failed with result %1\r\n
0xb0000129 | DisableDebugMode: Enabling activation timeout failed with result %1\r\n
0xb000012a | DisableDebugMode failed: %1\r\n
0xb000012b | Couldn't open process: %1\r\n
0xb000012c | PLM failed to process a hang for window %1 with error code %2\r\n
0xb000012d | PLM outswap application %1 failed to invoke with error code %2\r\n
0xb000012e | PLM couldn't find any process for application %1, and handle it as non-large app\r\n
0xb000012f | PLM failed to decide application %1 is large or not with error code %2\r\n
0xb0000130 | PLM empty policy failed to process application %1 with error code %2.  Ignoring the application\r\n
0xb0000131 | PLM empty policy failed to empty application %1 with error code %2\r\n
0xb0000132 | PLM failed to terminate application %1 as empty policy with error code %2\r\n
0xb0000133 | PLM empty policy failed to enumerate applications with error code %1\r\n
0xb0000134 | PLM termination policy skipping application %1, which is not registered with PLM\r\n
0xb0000135 | PLM memory policy failed to queue work with error code %1\r\n
0xb0000136 | GetPackageData called on a Package %1, which is not in the PLM Package Data Store\r\n
0xb0000137 | ERROR: Failed to set priority to %1, PsmKey=%2, NTSTATUS=%3\r\n
0xb0000138 | AllowServiceOfPackages: Failed to terminate package=%1, type=%2, HRESULT=%3\r\n
0xb0000139 | _CheckServicingPackages: Failed to enumerate app, PsmKey=%1, HRESULT=%2\r\n
0xb000013a | _CheckServicingPackages: Failed to enumerate package, PkgFullName=%1, HRESULT=%2\r\n
0xb000013b | GetImmersiveApplicationCount failed with error code %1\r\n
0xb000013c | Background workitems were force terminated, PsmKey=%1\r\n
0xb000013d | ChangeApplicationBiState failed: %1\r\n
0xb000013e | Background workitems for package %1 were force terminated\r\n
0xb000013f | ChangePackageBiState failed: %1\r\n
0xb0000140 | ApplicationProcesses failed to track process ID %1 with error code %2\r\n
0xb0000141 | OnBeforeQuiescing: Failed to allocate memory for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000142 | OnAfterQuiescing: Quiesce failed for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000143 | ERROR: _CompleteQuiesceHelper: Failed to terminate timed-out PsmKey %1 with result %2\r\n
0xb0000144 | ERROR: QuiesceHelper: App forgotten while still Quiescing, PsmKey=%1, suspendTrigger=%2\r\n
0xb0000145 | Failed to query the wake counters associated with application %1. NTSTATUS: %2\r\n
0xb0000146 | _AllAppSyncOperationHelper: Failed to allocate memory for PsmKey=%1, HRESULT=%2\r\n
0xb0000147 | _MultiAppSyncOperationHelper: Failed to perform operation on PsmKey=%1, HRESULT=%2\r\n
0xb0000148 | _MultiAppSyncOperationHelper: Failed in wait, HRESULT=%1\r\n
0xb0000149 | _MultiPackageSyncOperationHelper: Failed to enumerate PsmKey=%1, HRESULT=%2\r\n
0xb000014a | _MultiPackageSyncOperationHelper: Failed to find package in data store, PkgFullName=1%, HRESULT=%2\r\n
0xb000014b | Failed to suspend and terminate apps, cPsmKeys=%1\r\n
0xb000014c | Could not initialize an extended launch grace period for app %1 with HRESULT %2 -- falling back to normal launch grace\r\n
0xb000014d | App %1 failed to show a window after launch. Will attempt to terminate it now\r\n
0xb000014e | Failed to get a window for an app; assuming that the app's window is not hung, Aumid=%1, HRESULT=%2\r\n
0xb000014f | Failed to query hidden time for visibility debounce for app %1 with error code %2\r\n
0xb0000150 | _StartNewKeyDebounce: Error Result=%2, PsmKey=%1\r\n
0xb0000151 | StartTrackingNewApp failed with %1. The application launch is not protected and the app might potentially get suspended inappropriately\r\n
0xb0000152 | ERROR: Failed to enumerate exemption targets starting from PsmKey=%1\r\n
0xb0000153 | Failed to enumerate existing applications from PSM with error code %1\r\n
0xb0000154 | PsmRegisterApplicationNotification failed for application %1 with status %2.  PLM's cache says that the application's registration is: %3\r\n
0xb0000155 | ERROR: Failed to enumerate force termination targets starting from PsmKey=%1, HRESULT=%2\r\n
0xb0000156 | Application %1 failed to be added in PLM Data Store\r\n
0xb0000157 | Failed to initialize string to send app notification %1 state %2\r\n
0xb0000158 | Failed to initialize string to remove app %1\r\n
0xb0000159 | Failed to add %1 for application %2. The application doesn't have BTC_AUDIO background task capability\r\n
0xb000015a | Failed to initialize CmApi\r\n
0xb000015b | Task completion manager failed to add %1 to its sharing cache with error code %2\r\n
0xb000015c | ClearTerminationTypesForForgottenPackage: Failed to clear termination type for app, Aumid=%1, HRESULT=%2\r\n
0xb000015d | ERROR: Failed to schedule the visibility debounce, PsmKey=%1, HRESULT=%2\r\n
0xb000015e | OnWindowChanged ERROR: Failed to queue thread for Aumid=%1, Hwnd=%2, change=%3, HRESULT=%4\r\n
0xb000015f | ERROR: Failed to schedule deferred visibility timer, PsmKey=%1, HRESULT=%2\r\n
0xb00001f9 | BM: Queued evaluate WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fa | BM: Evaluate returned WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fb | BM: TaskActivated WorkItem: %1 Instance: %2\r\n
0xb00001fc | BM: TaskCompleted WorkItem: %1 Instance: %2\r\n
0xb00001fd | BM: TaskCanceled WorkItem: %1 Instance: %2\r\n
0xb00001fe | BM: Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb00001ff | BM: TaskActivating WorkItem: %1 Instance: %2\r\n
0xb0000200 | BM: Enter %1\r\n
0xb0000201 | BM: Exit %1, HR=%2\r\n
0xb0000202 | BM: TerminateHost WorkItem: %1\r\n
0xb0000203 | BM: ResourceSet invalidated for WorkItem: %1 Instance: %2.  This usually means the host has crashed before a ResourceSet could be applied.\r\n
0xb0000204 | BM: OnAcquired ignoring invalid CallbackId (%1).\r\n
0xb0000205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1'; WorkItemId='%2;' CallbackId='%3'.\r\n
0xb0000206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1'.\r\n
0xb0000207 | BM: OnApplicationStateChanged returning State='%2' PsmKey='%1' HR='%3'.\r\n
0xb0000208 | BM: OnAcquired received for CallbackId: %1\r\n
0xb0000209 | BM: OnAcquired request ignored for CallbackId: %1\r\n
0xb000020a | BM: ActivateDeferredWorkItem WorkItem: %1\r\n
0xb000020b | BM: ActivateDeferredWorkItem discarded WorkItem: %1 because of Status: %2\r\n
0xb000020c | BM: Enter %1 WorkItem: %2\r\n
0xb000020d | BM: Enter %1 WorkItem: %2 TaskInstanceId: %3\r\n
0xb000020e | BM: Exit %1\r\n
0xb000020f | BM: Failed to load settings for event %1.\r\n
0xb0000210 | BM: Failed to load settings for event %1 with error %2.\r\n
0xb0000211 | BM: Failed to load policy for CLSID: %1, for EventType %2 with error %3.\r\n
0xb0000212 | BM: Failed to load the policies with error %1.\r\n
0xb0000213 | BM: Evaluate returned WorkItem: %3 EventType: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb0000214 | BM: TaskWallClockActive WorkItem: %1 Instance: %2\r\n
0xb0000215 | BM: TaskWallClockExpired WorkItem: %1 Instance: %2\r\n
0xb0000216 | BM: Policy returned HRESULT: %3 for WorkItem: %2 PsmKey: %1.\r\n
0xb0000217 | BM: Canceling task for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000218 | BM: Ignoring cancelation request (whitelisted) for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000219 | BM: Session(%1) started, session initialization returned %2.\r\n
0xb000021a | BM: Session(%1) ended.\r\n
0xb000021b | BM: Activation ignored due to no Session(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb000021c | BM: Failed to acquire a ResourceSet for WorkItem: %1 with error %2.\r\n
0xb000021d | BM: WorkItem: %1 is being debugged. Setting wallclock limit to 0.\r\n
0xb000021e | BM: EvaluateActivationAction for WorkItem: %1 HRESULT: %2.\r\n
0xb000021f | BM: Skipped Buffering Exempted task with SQMId: %1 PsmKey: %2.\r\n
0xb0000220 | BM: Dropped Exempted task that came before SessionReady with SQMId: %1 PsmKey: %2.\r\n
0xb0000221 | BM: Activation ignored due to no User(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb0000222 | BM: User Logon Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000223 | BM: User Logoff Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000224 | BM: Pending activation discarded for work item (%1).\r\n
0xb0000225 | BM: Flushing ignored EvaluationState: %1 for WorkItem: %2.\r\n
0xb0000226 | BM: Flushing buffered activations.\r\n
0xb0000227 | BM: Global Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb0000228 | BM: A Session object for Session(%1) already exists.\r\n
0xb0000229 | BM: ShellSuspendState changed, oldState: %1 newState: %2\r\n
0xb000022a | BM: DPLKeyState changed, oldState: %1 newState: %2\r\n
0xb000022b | BM: Canceling WorkItem: %1 due to DPL policy.\r\n
0xb000022c | BM: Dropping activation for WorkItem: %1 due to DPL policy.\r\n
0xb0000258 | AM: Failed to read activation plugin registry with error code %1.\r\n
0xb0000259 | AM: Failed to CoCreate activation plugin with error code %1 and CLSID %2.\r\n
0xb000025a | AM: Successfully created activation plugin with CLSID %1 from the registry.\r\n
0xb00002bc | BAM: Added Package: %1 UserSid: %2.\r\n
0xb00002bd | BAM: Removed Package: %1 UserSid: %2.\r\n
0xb00002be | BAM: Added Application: %1 UserSid: %2.\r\n
0xb00002bf | BAM: Removed Application: %1 UserSid: %2.\r\n
0xb00002c0 | BAM: AccessState Changed for Package: %1 OldState: %2 NewState: %3 UserSid: %4.\r\n
0xb00002c1 | BAM: BackgroundExecutionManager::RequestAccessAsync called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c2 | BAM: BackgroundExecutionManager::GetStatus called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c3 | BAM: BackgroundExecutionManager::RemoveAccess called for Application: %1.\r\n
0xb00002c4 | BAM: Sanitizing data for package: %1 HRESULT: %2.\r\n
0xb00002c5 | BAM: ReregisteredPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002c6 | BAM: UnregisterPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002ee | FAM: NotifyTaskInstanceCompleted, TaskID:%1, hr:%2\r\n
0xb00002ef | FAM: NotifyTaskInstanceRunning, TaskID:%1 Timer - %2\r\n
0xb00002f0 | FAM: RegisterForegroundAgentManagerProxy:PID=%1, ConsumerTaskId=%2, Option=%3, hr=%4\r\n
0xb00002f1 | FAM: UiForeground:Memory:%1MB, CPU:%2%%\r\n
0xb00002f2 | FAM: CreateAgentLaunchRequest, TaskID:%1, Queue:%2, hr:%3\r\n
0xb00002f3 | FAM: CancelAgentRequest, TaskID:%1, CancelType=%2, hr:%3\r\n
0xb00002f4 | FAM: AbortAgentRequestsInternal, hr:%1\r\n
0xb00002f5 | FAM: CompleteAgent, TaskID:%1, hr:%2\r\n
0xb00002f6 | FAM: PrioritizeAgentRequest, TaskID:%1, hr:%2\r\n
0xb00002f7 | FAM: OnForegroundAppChanged()-Abort agents\r\n
0xb00002f8 | FAM: OnRelease()\r\n
0xb00002f9 | FAM: NotifyConsumer, Notification:%1, TaskID:%2, hrResult:%3\r\n
0xb00002fa | FAM: AcquireSharedResourceSet, ProductID:%1, ConsumerPid:%2, Pending:%3, hr:%4\r\n
0xb00002fb | FAM: ReleaseResourceSet, #%1, hr:%2\r\n
0xb00002fc | FAM: TimerExpired:TerminateHost[PID=%1]\r\n
0xb00002fd | FAM: AcquireResourceSet, #%1, Mem:%2MB, CPU:%3%%, hr:%4\r\n
0xb00002fe | FAM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000321 | OTM: Read settings. First retry timeout = %1 ms, Second retry timeout = %2 ms, Third retry timeout = %3 ms, Maximum Retry Timeout = %4 ms\r\n
0xb0000322 | OTM: Task instance %2 of product %1 completed\r\n
0xb0000323 | OTM: TaskHost of product %1 has crashed\r\n
0xb0000324 | OTM: TaskHost of product %1 has been completed by PacMan\r\n
0xb0000325 | OTM: Launching OEM boot agents\r\n
0xb0000326 | OTM: Launching boot agents for product %1 failed with error %2\r\n
0xb0000327 | OTM: Launch boot agents for product %1\r\n
0xb0000328 | OTM: Running OnUpdateStarted for product %1\r\n
0xb0000329 | OTM: Restarting boot agents for product %1 after update\r\n
0xb000032a | OTM: Start menu is ready.\r\n
0xb000032b | OTM: Could not launch OEM boot agents. QueueUserWorkItem failed with error %1.\r\n
0xb000032c | OTM: Could not process update notification for OEM application. QueueUserWorkItem failed with error %1.\r\n
0xb000032d | OTM: Could not process update notification for OEM application. ProcessUpdateNotification failed with error %1.\r\n
0xb000032e | OTM: OemTaskManager::NotifyTaskInstanceCompleted failed with error %1.\r\n
0xb000032f | OTM: OemTaskManager::NotifyTaskHostCompleted failed with error %1.\r\n
0xb0000330 | OTM: OemApp::DumpAgents failed with error %1.\r\n
0xb0000331 | OTM: An error occurred. Hr = %1\r\n
0xb0000332 | OTM: No apps with ServiceAgents were found.\r\n
0xb0000333 | OTM: No ServiceAgent task found for product %1.\r\n
0xb0000334 | OTM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb000035d | PLM: Start tracking new app user %1 app %2, contract %3, hr = %4\r\n
0xb000035e | PLM: Application launched %1 in app %2, hr = %3\r\n
0xb000035f | PLM: Application resume %1 in app %2, hr = %3\r\n
0xb0000360 | PLM: Suspend-Terminate(%3) task %1 in app %2\r\n
0xb0000361 | PLM: Suspend-Terminate suspend of task %1 in app %2 exemption %3\r\n
0xb0000362 | PLM: Suspend-Terminate auto terminate(%3) task %1 in app %2\r\n
0xb0000363 | PLM: Suspend-Terminate task %1 in app %2, hr %3\r\n
0xb0000364 | PLM: Halt app %1, hr %2\r\n
0xb0000365 | PLM: Task resume %1 in app %2\r\n
0xb0000366 | PLM: Task cancel %1 in app %2\r\n
0xb0000367 | PLM: Task remove %1 in app %2\r\n
0xb0000368 | PLM: Queue Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000369 | PLM: Queue Activation State Change Notification %1 state %2\r\n
0xb000036a | PLM: Before Activate task %1 for user %2 in app %3, contract %4, hostid %5, hr = %6\r\n
0xb000036b | PLM: After Activate task %1 with result %2, hr = %3\r\n
0xb000036c | PLM: ApplicationLayer=%1 Set Foreground new task %2, prev task %3\r\n
0xb000036d | PLM: Add task %1 to user %2 and app %3, hr = %4\r\n
0xb000036e | PLM: Create app for user %1, %2, new [app(%3) pkg(%4)], hr = %5\r\n
0xb000036f | PLM: Add task %1 to user %2 and app %3, new [app(%4) pkg(%5)], hr = %6\r\n
0xb0000370 | PLM: Remove task %1, was found(%2)\r\n
0xb0000371 | PLM: Remove app if empty from user %1, %2, hr = %3\r\n
0xb0000372 | PLM: Remove pkg if empty from user %1, %2, hr = %3\r\n
0xb0000373 | PLM: Send Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000374 | PLM: Send Activation State Change Notification %1 state %2\r\n
0xb0000376 | PLM: Timer Started duration %1ms, hr %2\r\n
0xb0000377 | PLM: Timer Expired duration %1ms, hr %2\r\n
0xb0000378 | PLM: Abort task %1 reason %2, dump(%3)\r\n
0xb0000379 | PLM: Task rehydrate %1 in app %2 contract %3\r\n
0xb000037a | PLM: Start RPC suspension timer PSMKey=%1 WakeCounters=%2, hr = %3\r\n
0xb000037b | PLM: Cancel RPC suspension timer PSMKey=%1 app state=%2\r\n
0xb000037c | PLM: Terminate application PSMKey=%1 due to expired RPC suspension timeout\r\n
0xb000037d | PLM: Application %1 cannot be terminated due to %2 exemption\r\n
0xb000037e | PLM: Application %1 can be terminated\r\n
0xb000037f | PLM: EvaluateAndTerminateApplication %1 cannot be terminated due to %2\r\n
0xb0000380 | PLM: EvaluateAndTerminateApplication %1, terminate hr = %2\r\n
0xb0000381 | PLM: Terminate debounce app %1 current state %2 ultimate state %3\r\n
0xb0000382 | PLM: Terminate debounce app %1, hr = %2\r\n
0xb0000383 | PLM: Terminate reason was cleared\r\n
0xb0000384 | PLM: Abort app user %1 app %2 reason %3, dump(%4)\r\n
0xb0000385 | PLM: Watson dump NOT generated for user %1 app %2, process count %3\r\n
0xb0000386 | PLM: Watson dump start for user %1 app %2 reason %3 description %4, process %5 (%6)\r\n
0xb0000387 | PLM: Watson dump information for user %1 app %2 product Id %3 title %4 version %5\r\n
0xb0000388 | PLM: Watson dump end for user %1 app %2, hr %3\r\n
0xb0000389 | PLM: Add Watson dump to user %1 app %2 process %3, hr %4\r\n
0xb000038a | PLM: Failed to add Watson process info for process %1 user %2 app %3\r\n
0xb000038b | PLM: Watson dump status changed pids(%1)\r\n
0xb000038c | PLM: Watson dump status changed, add process %1 user %2 app %3\r\n
0xb000038d | PLM: Watson dump status changed, remove process %1 user %2 app %3\r\n
0xb000038e | PLM: Watson dump status changed, unknown process %1 app %2\r\n
0xb000038f | PLM: Watson add/remove(%2) error report task completion to process %1 (signaled %4), hr %3\r\n
0xb0000390 | PLM: Watson in progress for PSMKey %1, waiting...\r\n
0xb0000391 | PLM: Watson in progress finished for PSMKey %1\r\n
0xb0000392 | PLM: Extending RPC suspension timer PSMKey=%1\r\n
0xb0000393 | PLM: Acquire network reference failed CM_RESULT=%1\r\n
0xb0000394 | PLM: Release network reference failed CM_RESULT=%1\r\n
0xb0000395 | PLM: Suspend-Terminate(%2) app %1 exemption %3, hr %4\r\n
0xb0000396 | PLM: Suspend-Terminate task %1 while dehydrating\r\n
0xb0000397 | PLM: Add user %1 sid %2 to data store, hr = %3\r\n
0xb0000398 | PLM: Start launch grace for user %1 app %2, hr = %3\r\n
0xb0000399 | PLM: Set Window Id for user %1 app %2 wnd %3\r\n
0xb000039a | PLM: EvaluateLaunchGraceCompleted for user %1 app %2\r\n
0xb000039b | PLM: Terminating reexisting app due to sihost restart with PSMKey %1, status %2\r\n
0xb000039c | PLM: Terminating preexisting applications on sihost startup\r\n
0xb000041b | AAM: Initiate activation for user %1 app %2 contract %3 task %4, hr %5\r\n
0xb000041c | AAM: Initiate activation completed for task %2 (expected %1), hr %3\r\n
0xb000041d | AAM: Initialize activation for user %1 app %2 contract %3 lightup(%5), hr %4\r\n
0xb000041e | AAM: Validate activation, hr %1\r\n
0xb000041f | AAM: Verify license for pkg %1, hr %2\r\n
0xb0000420 | AAM: Activate activation task %1 host %2, hr %3\r\n
0xb0000421 | AAM: Activation shim timer expired %1, hr %2\r\n
0xb0000422 | AAM: Initiate Core UI, hr %1\r\n
0xb0000423 | AAM: Release Core UI\r\n
0xb0000424 | AAM: Create Windows AAM, hr %1\r\n
0xb0000425 | AAM: Attempted remediation, hr %1\r\n
0xb0000426 | AAM: Failed while trying to find a remediation handler, hr %1\r\n
0xb0000427 | AAM: Failed while trying to find the package status, hr %1\r\n
0xb0000428 | AAM: Failed while trying to find the package origin, hr %1\r\n
0xb0000429 | AAM: Failed while trying to verify and initialize the activation, hr %1\r\n
0xb000042f | AAM: Broker created plugins %1, expected %2\r\n
0xb0000430 | AAM: Broker initialize, hr %1\r\n
0xb0000431 | AAM: Broker start activate application %1 (%3 args) arg[0] %2 type %4 caller PID %5 (initialization count %6)\r\n
0xb0000432 | AAM: Broker end activate application %1 launched PID %2 task %3, hr %4\r\n
0xb0000433 | AAM: Broker activate task with result for app %1 caller PID %2 caller task %3\r\n
0xb0000434 | AAM: Broker get result for PID %1 task %2 result %3, hr %4\r\n
0xb0000435 | AAM: Broker get task id for process %1 window %2 = task %3, hr %4\r\n
0xb0000436 | AAM: Broker init session manager, hr %1\r\n
0xb0000437 | AAM: Broker release session manager\r\n
0xb0000438 | AAM: Broker add task with result for parent %1, hr %2\r\n
0xb0000439 | AAM: Broker get task with result for parent %1, hr %2\r\n
0xb000043a | AAM: Broker remove task with result for parent %1, hr %2\r\n
0xb000043b | AAM: Broker create completed event for caller PID %1, hr %2\r\n
0xb000043c | AAM: Broker get task with result for child %1, hr %2\r\n
0xb000043d | AAM: Broker parent task completed %1 with child state %2\r\n
0xb000043e | AAM: Broker child task completed %1 with state %2, hr %3\r\n
0xb000043f | AAM: Broker task event signaled for parent %1 child %2 previous state %3, hr %4\r\n
0xb0000440 | AAM: Broker close task %1, hr %2\r\n
0xb0000441 | AAM: Broker activate application %1 arg[%3] %2\r\n
0xb000044d | FM: Registering callback %1 HRESULT=%2\r\n
0xb000044e | FM: Vacate Foreground ApplicationLayer=%1 HRESULT=%2\r\n
0xb000044f | FM: Generate ActivationInstanceID Id=%1\r\n
0xb0000450 | FM: +ActivationPrerequisitePhase ActivationInstanceId=%1 ApplicationLayer=%2 AUMID=%3 ContractId=%4\r\n
0xb0000451 | FM: -ActivationPrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb0000452 | FM: +Resume_RehydrationPhase ActivationInstanceId=%1\r\n
0xb0000453 | FM: -Resume_RehydrationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000454 | FM: +PostActivationPhase ActivationInstanceId=%1\r\n
0xb0000455 | FM: -PostActivationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000456 | FM: +ResumeActivation ActivationInstanceId=%1 ApplicationLayer=%2 fIsResumed=%3\r\n
0xb0000457 | FM: -ResumeActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000458 | FM: +Resume_ActivationPhase ActivationInstanceId=%1\r\n
0xb0000459 | FM: -Resume_ActivationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000045a | FM: +PauseActivation ActivationInstanceId=%1\r\n
0xb000045b | FM: -PauseActivation HRESULT=%1 PausePending=%2\r\n
0xb000045c | FM: +CancelActivation ActivationInstanceId=%1\r\n
0xb000045d | FM: -CancelActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000045e | FM: +AbortActivation ActivationInstanceId=%1 Reason=%2 fGenerateWER=%3\r\n
0xb000045f | FM: -AbortActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000460 | FM: +GetActivationProcessId ActivationInstanceId=%1\r\n
0xb0000461 | FM: -GetActivationProcessId ActivationInstanceId=%1 PID%2 HRESULT=%3\r\n
0xb0000462 | FM: +SetForegroundActivationInstance ActivationInstanceId=%1 ApplicationLayer=%2 Isforeground=%3\r\n
0xb0000463 | FM: -SetForegroundActivationInstance ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000464 | FM: +SetForeground_ActivationPhase ActivationInstanceId=%1\r\n
0xb0000465 | FM: -SetForeground_ActivationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000466 | FM: SetActivationDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb0000467 | FM: OnActivationStateChanged ActivationInstanceId=%1 state=%2 HRESULT=%3\r\n
0xb0000468 | FM: OnApplicationStateChanged AUMID=%1 state=%2 HRESULT=%3\r\n
0xb0000469 | FM: IsValidActivationProcessId ActivationInstanceID=%1 PID=%2 fValid=%3 HRESULT=%4\r\n
0xb000046a | FM: GetForegroundProductId fIgnoreLockScreen=%1 ProductID=%2 HRESULT=%3\r\n
0xb000046b | FM: GetProductIdFromProcessID ProductID=%1 PID=%2 HRESULT=%3\r\n
0xb000046c | FM: Discarding Application Frozen notification because the application isn't really frozen\r\n
0xb000046d | FM: Dehydrate Application AUMID=%1 HRESULT=%2\r\n
0xb000046e | FM: +ResumePrerequisitePhase ActivationInstanceId=%1 ApplicationLayer=%2\r\n
0xb000046f | FM: -ResumePrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb0000470 | FM: AcquireForegroundResourceSet ActivationInstanceId=%1 AUMID=%2 LaunchFlags=%3 ResourceSet to acquire=%4\r\n
0xb0000471 | FM: OnRelease ForegroundResourceSet ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000472 | FM: GenerateWatsonReport PID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000473 | FM: TaskCompletion New Battery Saver State %1\r\n
0xb0000474 | FM: TaskCompletion Revoke Exemption PID=%1 AUMID=%2 TC=%3\r\n
0xb0000475 | FM: TaskCompletion Apply(%3) Exemption PID=%1 TC=%2 HRESULT=%4\r\n
0xb0000476 | FM: SetContinuation ActivationInstanceID=%1\r\n
0xb0000477 | FM: AbandonContinuation ActivationInstanceID=%1 ApplicationLayer=%2\r\n
0xb0000478 | FM: PerformContinuation ActivationInstanceID=%1 ApplicationLayer=%2\r\n
0xb0000479 | FM: Shutdown HRESULT=%1\r\n
0xb000047a | FM: +PauseActivation ActivationInstanceId=%1 AUMID=%2 PackageFullName=%3\r\n
0xb000047b | FM: +ActivationBypass ActivationInstanceId=%1\r\n
0xb000047c | FM: -ActivationBypass ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000047d | FM: +PostPausePendingResume ActivationInstanceId=%1\r\n
0xb000047e | FM: -PostPausePendingResume ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000047f | FM-ARP: ApplyResourceSet ResourceSet=%1 HRESULT=%2\r\n
0xb0000480 | FM-ARP: ApplyResourceSetType ResourceSetType=%1 User=%2 PSMKey=%3 ResourceSet=%4 HRESULT=%5\r\n
0xb0000481 | FM-ARP: ApplyTerminal ResourceSet=%1 HRESULT=%2\r\n
0xb0000482 | FM-ARP: RemoveInterruptiveUIAccess ResourceSet=%1 HRESULT=%2\r\n
0xb0000483 | FM-ARP: ResetInterruptiveUIAccess ResourceSet=%1 HRESULT=%2\r\n
0xb0000484 | FM-ARP: OnRelease CallbackId=%1 HRESULT=%2\r\n
0xb0000485 | FM-ARP: OnOutOfMemory CallbackId=%1 HRESULT=%2\r\n
0xb0000486 | FM-EEP: CheckProcessBackgroundEligibility ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb0000487 | FM-EEP: ApplyTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb0000488 | FM-EEP: RevokeTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb0000489 | FM-EEP: RequestExtendedExecution ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000048a | FM-EEP: RegisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb000048b | FM-EEP: CompleteExtendedExecution ProcessId=%1 fIsResumed=%2 HRESULT=%3\r\n
0xb000048c | FM-EEP: RevokeSuspensionExtension User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb000048d | FM-ARP: NotifyPendingResourceSetTransition ResourceSetType=%1 ResourceSet=%2 HRESULT=%3\r\n
0xb000048e | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 fTimerExpiredCallback=%2 HRESULT=%3\r\n
0xb000048f | FM-EEP: IsApplicationStateBackgroundEligibile User=%1 PsmKey=%2 fResult=%3\r\n
0xb0000490 | FM-EEP: RevokeTaskCompletionExemption AppUserModelId=%1 HRESULT=%2\r\n
0xb0000491 | FM-EEP: AllowBackgroundExecution User=%1 AppUserModelId=%2 HRESULT=%3\r\n
0xb0000492 | FM-EEP: OnPackageEnergyStateChange PackageFullName=%1 PackageState=%2 HRESULT=%3\r\n
0xb0000493 | FM: SetActivationImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb0000494 | FM: NotifyWindowAdded TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb0000495 | FM: NotifyWindowRemoved TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb0000496 | FTM: Logoff User=%1 HRESULT=%2\r\n
0xb0000497 | FM-EEP: UnregisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb0000498 | FM-EEP: RegisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb0000499 | FM-EEP: UnregisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb000049a | FM: ActivationTimeoutPolicyChanged  TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb000049b | FM-EEP: OnConnectedStandbyStateChanged  State=%1\r\n
0xb000049c | FM-ARP: ApplyResourceBoost User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb000049d | FM: OnAcquired ForegroundResourceSet ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000049e | FM-CAM: OnApplicationStateChangedEx UserContext=%1 PsmKey=%2 state=%3 HRESULT=%4\r\n
0xb000049f | FM-CAM: AcquireForegroundResource UserContext=%1 PsmKey=%2 isPending=%3 CallbackId=%4\r\n
0xb00004a0 | FM-CAM: OnAcquired CallbackId=%1 HRESULT=%2\r\n
0xb00004a1 | FM-CAM: OnRelease CallbackId=%1\r\n
0xb00004a2 | FM-CAM: OnTimerExpired CallbackId=%1\r\n
0xb00004a3 | FM: SendActivationNotification ActivationId=%1 NotificationId=%2\r\n
0xb00007d0 | VoIPPolicy: Evaluate Activation Action for PsmKey = %2, WorkItemId = %1, Action = %3, HRESULT = %4\r\n
0xb00007d1 | VoIPPolicy: Task Activated for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d2 | VoIPPolicy: Task Completed for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d3 | VoIPPolicy: Task Canceled for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d4 | VoIPPolicy: Task Aborted for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d5 | VoIPPolicy: Determine and Apply Resources PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d6 | VOIP: NotifyVoipActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d7 | VOIP: LaunchVoipRtcTask called for PID:%1 PSMKey:{%2} with TaskEntryPoint:{%3} and WNFStateName:{%4} HRESULT:%5.\r\n
0xb00007d8 | VOIP: NotifyVoipActivityCompleted called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d9 | VOIP: HoldActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007da | VOIP: UnholdActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007db | VOIP: NotifyIncomingCallDialogDisplayed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dc | VOIP: NotifyIncomingCallDialogDismissed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dd | VOIP: CallActive called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007de | VOIP: AppLaunchVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007df | VOIP: OnVoipActivityCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e0 | VOIP: AppHoldActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e1 | VOIP: AppUnholdActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e2 | VOIP: OnIncomingCallDialogDisplayed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e3 | VOIP: OnIncomingCallDialogDismissed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e4 | VOIP: AppDetermineAndApplyBestResourceSet called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e5 | VOIP: PolicyEvaluateAction called for WorkItemId:{%1} PSMKey:{%2} ActivationAction:%3 HRESULT:%4.\r\n
0xb00007e6 | VOIP: PolicyTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e7 | VOIP: PolicyTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e8 | VOIP: PolicyTaskCanceled called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e9 | VOIP: PolicyTaskAborted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007ea | VOIP: OnForegroundApplicationChanged called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007eb | VOIP: AppOnTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ec | VOIP: AppOnTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ed | VOIP: AppCancelVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ee | VOIP: CancelVoipRtcTask called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb0000c81 | Task: %1 has started\r\n
0xb0000c82 | Task: %1 has paused\r\n
0xb0000c83 | Task: %1 has resumed\r\n
0xb0000c84 | Task: %1 has completed\r\n
0xb0000c85 | EM: +GetTaskInfo()\r\n
0xb0000c86 | EM: -GetTaskInfo(). HRESULT = %1\r\n
0xb0000c87 | EM: GetAppInfo:%1,%2:%3\r\n
0xb0000c88 | EM: ParseBackgroundAbilities - HRESULT=%1\r\n
0xb0000c89 | EM: +ExecManServerHost::CreateProcess\r\n
0xb0000c8a | EM: -ExecManServerHost::CreateProcess. HRESULT=%1\r\n
0xb0000c8b | Sqm::AppPlatSqmAppDataUsage: %1/%2 - TaskID = %3, Type = %4, NewState = %5, ReasonForStateChange = %6, Duration (ms) = %7, PeakMemory (kb) = %8\r\n
0xb0000c8f | Emc::ExecuteCommand: StartTaskCallbackBegin: TaskID = %1\r\n
0xb0000c90 | Emc::ExecuteCommand: StartTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c91 | Emc::ExecuteCommand: PauseTaskCallbackBegin: TaskID = %1\r\n
0xb0000c92 | Emc::ExecuteCommand: PauseTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c93 | Emc::ExecuteCommand: ResumeTaskCallbackBegin: TaskID = %1\r\n
0xb0000c94 | Emc::ExecuteCommand: ResumeTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c95 | Emc::ExecuteCommand: ControlTaskCallbackBegin: TaskID = %1\r\n
0xb0000c96 | Emc::ExecuteCommand: ControlTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c97 | Emc::ExecuteCommand: CancelTaskCallbackBegin: TaskID = %1\r\n
0xb0000c98 | Emc::ExecuteCommand: CancelTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c99 | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackBegin: TaskID = %1\r\n
0xb0000c9a | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c9e | Emc::RegisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, HR = %3\r\n
0xb0000ca8 | Emc::DeregisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, Reason = %3, HR = %4\r\n
0xb0000ca9 | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleBegin: ProductID = %1\r\n
0xb0000caa | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleEnd: ProductID = %1\r\n
0xb0000cab | EM: Skipping terminate process call for %1\r\n
0xb0000cac | EM: Terminating process: PID = %1, ExitCode = %2\r\n
0xb0000ce4 | AimServer::OnAgentRequestInvoked: AgentRequestID %1 was invoked. PID = %2, HR = %3\r\n
0xb0000ce5 | AimServer::ReadSettings: HR = %1\r\n
0xb0000ce6 | AimServer: Detected server for scope %1 terminated (PID = %2)\r\n
0xb0000ce8 | AimServer::HandleEvent: ProductID %1 received PM LifecyleEvent %2. HR Notification = %3, HR = %4\r\n
0xb0000ce9 | BA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cea | BA::RegisterServiceRequest: AlreadyReserved = %1, SR = %2, HR = %3\r\n
0xb0000ceb | BA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cec | BA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000ced | BA::NotifyTaskInstanceCompleted: Terminating Orphaned Host PID = %1\r\n
0xb0000cee | BA::OrphanAgentRequest: AgentRequestID = %1, HR = %2\r\n
0xb0000cef | BA::UnRegisterServiceRequest: Terminating host PID %1\r\n
0xb0000cf0 | BA::UnRegisterServiceRequest: Orphaning host PID %1\r\n
0xb0000cf1 | BA::UnRegisterServiceRequest: Terminating second old orphaned host PID %1\r\n
0xb0000cf2 | BTM::RecvCallback: Timer expired for AgentRequestID %1\r\n
0xb0000cf3 | BTM::LaunchTask: TaskURI = %1 TaskID = %2, PID = %3, HR = %4\r\n
0xb0000cf4 | GBA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cf5 | GBA::RegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf6 | GBA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf7 | GBA::RegisterAgentRequest: AgentRequestID = %1, type = %2, hr = %3\r\n
0xb0000cf8 | GBA: Cancelling low priority %3 agent because high priority %2 needs to run: Resource was dedicated = %1\r\n
0xb0000cf9 | GBA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000cfa | GBA::TryAcquireResourceSet: pending = %1, type = %2, HR = %3\r\n
0xb0000cfb | GBA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfc | BA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfd | BA::NotifyTaskHostCompleted: ProductID = %1, PID = %2\r\n
0xb0000cfe | BA::RegisterAgentRequest: ProductID = %1, AgentRequestID = %2, HR = %3\r\n
0xb0000dac | FTM: AllowBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dad | FTM: Process is using too much memory for BG Execution. PID=%1, MemUsage=%2, RequiredMemUsage=%3\r\n
0xb0000dae | FTM: Removing BG capability from Task ID %1 due to OOM\r\n
0xb0000daf | FTM: Battery Saver State has change. New state = %1\r\n
0xb0000db0 | FTM: Attempted new BG Execution request due to battery state change. TaskID=%1\r\n
0xb0000db1 | FTM: NotifyTaskInstanceCompleted TaskID=%1 HRESULT=%2\r\n
0xb0000db2 | FTM: NotifyTaskInstancePaused TaskID=%1 HRESULT=%2\r\n
0xb0000db3 | FTM: NotifyTaskInstanceRunning TaskID=%1 HRESULT=%2\r\n
0xb0000db4 | FTM: SendTaskStatusChange TaskID=%1 Status=%2 HRESULT=%3\r\n
0xb0000db5 | FTM: NotifyTaskHostCompleted HRESULT=%1\r\n
0xb0000db6 | FTM: Discarding NotifyTaskHostFrozen notification because the host isn't really frozen\r\n
0xb0000db7 | FTM: NotifyTaskHostFrozen PID=%1 HRESULT=%2\r\n
0xb0000db8 | FTM: NotifyTaskHostDehydrated HRESULT=%1\r\n
0xb0000db9 | FTM: Registering callback %1 HRESULT=%2\r\n
0xb0000dba | FTM: New Task %1 is dehydration-suppressing\r\n
0xb0000dbb | FTM: Applying Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbc | FTM: Revoking Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbd | FTM: +LaunchTask TaskURI=%1 LaunchFlags=%2\r\n
0xb0000dbe | FTM: -LaunchTask TaskURI=%1 TaskID=%2 PID=%3 HRESULT=%4\r\n
0xb0000dbf | FTM: ResumeTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc0 | FTM: Removing Foreground Resources from TaskID=%1\r\n
0xb0000dc1 | FTM: SetForegroundTaskInstanceId TaskID=%1 HRESULT=%2\r\n
0xb0000dc2 | FTM: PauseTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc3 | FTM: CancelTask TaskID=%1 Frozen=%2 HRESULT=%3\r\n
0xb0000dc4 | FTM: AbortTask being ignored because the task is completed TaskID=%1\r\n
0xb0000dc5 | FTM: AbortTask TaskID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000dc6 | FTM: SetTaskDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb0000dc7 | FTM: RequestProcessBackgroundExecution type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc8 | FTM: CancelProcessBackgroundExecutionRequest type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc9 | FTM: TaskRunningInBackground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dca | FTM: TaskRunningInForeground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dcb | FTM: Changing activation policy to resume due to BG Execution for ProductID %1\r\n
0xb0000dcc | FTM: OnShutdownCompleted\r\n
0xb0000dcd | FTM: Ignoring expired watchdog for task %1 because it is being debugged.\r\n
0xb0000dce | FTM: Watchdog fired for task %1 while running in background. Pausing Task.\r\n
0xb0000dcf | FTM: Request BG Execution Denied because it wasn't running. TaskID=%1\r\n
0xb0000dd0 | FTM: Request BG Execution Denied because product was forbidden. TaskID=%1\r\n
0xb0000dd1 | FTM: Request BG Execution Denied because task didn't have BG abilities in its manifest. TaskID=%1\r\n
0xb0000dd2 | FTM: Request BG Execution Denied due to lack of resources. TaskID=%1\r\n
0xb0000dd3 | FTM: Request BG Execution Denied because battery policy prevented it. TaskID=%1\r\n
0xb0000dd4 | FTM: RequestBGAccess IsAllowed=%1 TaskID=%2 HRESULT=%3\r\n
0xb0000dd5 | FTM: RemoveBGRequest RequestedRemoval=%1 ActualRemoval=%2 TaskID=%3 HRESULT=%4\r\n
0xb0000dd6 | FTM: ForbidBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dd7 | FTM: IsValidTaskInstancePid TaskID=%1 Pid=%2 fValid=%3 HRESULT=%4\r\n
0xb0000dd8 | FTM: DetermineBestResourceSet for child ProductID=%1 LaunchFlags=%2 ResourceSetType=%3\r\n
0xb0000dd9 | FTM: OnRelease ResourceSet TaskID=%1 ResouceSet=%2 HRESULT=%3\r\n
0xb0000dda | FTM:UITask Call to Acquire network reference failed CM_RESULT=%1\r\n
0xb0000ddb | FTM:UITask Call to Release network reference failed CM_RESULT=%1\r\n
0xb0000ddc | FTM: SetTaskImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb0000ddd | FTM: +RequestProcessBackgroundExecution type=%1 Pid=%2\r\n
0xb0000dde | FTM: +RequestBackgroundExecution type=%1\r\n
0xb0000ddf | FTM: -RequestBackgroundExecution type=%1 HRESULT=%2\r\n
0xb0000de0 | FTM: +RequestBGAccess TaskInstanceId=%1 type=%2\r\n
0xb0000de1 | FTM: Request BG Execution Denied because DPL policy prevented it. TaskID=%1\r\n
0xb0000de2 | FTM: Edp keys locked state (%1)\r\n
0xb0000e42 | VoIP: Foreground state for product %1 has changed. Is in foreground = %2\r\n
0xb0000e43 | VoIP: Canceling communication agent for product %1\r\n
0xb0000e44 | VoIP: Timer expired for keep-alive agent of product %1\r\n
0xb0000e45 | VoIP: Timer expired for incoming call agent of product %1\r\n
0xb0000e46 | VoIP: Launched agent instance with id %2 and URI %1\r\n
0xb0000e47 | VoIP: Canceled agent instance with id %1\r\n
0xb0000e48 | VoIP: Set active call resource set\r\n
0xb0000e49 | VoIP: Set communication agent resource set\r\n
0xb0000e4a | VoIP: Set VoIP Worker resource set\r\n
0xb0000e4b | VoIP: Applied terminal resource set\r\n
0xb0000e4c | VoIP: Last task instance completed. Releasing the task host ...\r\n
0xb0000e4d | VoIP: Launching active call agent instance for product %1\r\n
0xb0000e4e | VoIP: Canceling active call agent for product %1\r\n
0xb0000e4f | VoIP: Putting an active call on hold for product %1\r\n
0xb0000e50 | VoIP: Taking an active call off hold for product %1\r\n
0xb0000e51 | VoIP: Incoming call dialog has been displayed for product %1\r\n
0xb0000e52 | VoIP: Incoming call dialog has been dismissed for product %1\r\n
0xb0000e53 | VoIP: Launch communication agent request received from process %1 for product %2\r\n
0xb0000e54 | VoIP: Read settings. Keep alive timout = %1 ms, Max agent request queue = %2, Incoming call grace period = %3 ms, Incoming call dismissed grace period = %4 ms\r\n
0xb0000e55 | VoIP: Received request to launch agent type %2 for product %1\r\n
0xb0000e56 | VoIP: Task instance %2 of product %1 completed\r\n
0xb0000e57 | VoIP: Processing request to launch agent type %2 for product %1\r\n
0xb0000e58 | VoIP: Added VoIPApp object to map for product %1\r\n
0xb0000e59 | VoIP: Removed VoIPApp object from map for product %1\r\n
0xb0000e5a | VoIP: Getting VoIPApp object from map for product %1\r\n
0xb0000e5b | VoIP: Publishing WNF_DEVP_VOIP_ACTIVE_CALL_STATE_CHANGE failed with status %1\r\n
0xb0000e5c | VoIP: Subscribing to the WNF_WIFI_CONNECTION_STATUS event failed with status %1\r\n
0xb0000e5d | VoIP: Subscribed to WNF_WIFI_CONNECTION_STATUS? %1\r\n
0xb0000e5e | VoIP: WiFi connection status active/dormat? %1 (hConnection = %2)\r\n
0xb0000e5f | VoIP: RtlQueryWnfStateData failed trying to query the value of WNF_WIFI_CONNECTION_STATUS. NTSTATUS = %1\r\n
0xb0000e60 | VoIP: Could not spin up worker for UpdateWiFiStateHelper. HR =%1\r\n
0xb0000e61 | VoIP: In active call? %1\r\n
0xb0000e62 | VoIP: CmUtilSetWiFiActive was not successful. This could be because WiFi disconnected by the time we were notified of the connection.\r\n
0xb0000e63 | VoIP: WiFi connection status is %1.\r\n
0xb0000e64 | VoIP: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000e65 | VoIP: PhoneServiceRestart: HR = %1\r\n
0xb0000e66 | VoIP: PhoneServiceRestart: Product = %1, HR = %2\r\n
0xb0000e67 | VoIP: Launching call query info agent instance for product %1\r\n
0xb0000e68 | VoIP: Canceling call query info agent instance for product %1\r\n
0xb0000e69 | VoIP: Terminating agents due to low memory for product %1\r\n
0xb0000e6a | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2\r\n
0xb0000e6b | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2, fApplied = %3, HR = %4\r\n
0xb0000e6c | VoIP: Set Network Active for PDC\r\n
0xb0000e6d | VoIP: Set Network Inactive for PDC\r\n
0xb0000e73 | VoIP: An error occurred. Hr = %1\r\n
0xb00017d4 | %1 - [%2 = %3]\n\r\n
0xb00017d5 | %1 - Parsing config file [%2] file size = %3.  Parse = %4\r\n
0xb00017d6 | %1 - OnTaskModelMessage: Dispatching EM message\r\n
0xb00017d7 | %1 - InitializeTaskHost URI=%2, Page=%3, TaskId=%4\r\n
0xb00017d8 | %1 - Resuming Task from dehydration\r\n
0xb00017d9 | %1 - TaskHandler::GetTaskHandler hr=%2\r\n
0xb00017da | %1 - TaskHost Init\r\n
0xb00017db | %1 - TaskHost Init hr = %2\r\n
0xb00017dc | %1 - Host Dispatcher Exiting hr = %2\r\n
0xb00017dd | %1 - TaskHandlerReady received\r\n
0xb00017de | %1 - StartTask TaskId=%2\r\n
0xb00017df | %1 - PauseTask TaskId=%2\r\n
0xb00017e0 | %1 - ResumeTask TaskId=%2\r\n
0xb00017e1 | %1 - OnTaskHandlerVisible received\r\n
0xb00017e2 | %1 - OnTaskHandlerHidden received\r\n
0xb00017e3 | %1 - BackgroundExecutionCallback TaskId[%2] Command[%3]\r\n
0xb00017e4 | %1 - BackgroundExecutionCallback hr=%2\r\n
0xb00017e5 | %1 - OnHostRunning\r\n
0xb00017e6 | %1 - OnHostRunning. hr = %2\r\n
0xb00017e7 | %1 - Dehydrating. dehydrateGracefully = %2\r\n
0xb00017e8 | %1 - Gracefully dehydrating TaskHost\r\n
0xb00017e9 | %1 - TryDehydrateHost. hr = %2\r\n
0xb00017ea | %1 - DehydrateHost event triggered\r\n
0xb00017eb | %1 - WaitForUnfreeze hr = %2\r\n
0xb00017ec | %1 - ReduceMemoryHostCallback hr = %2\r\n
0xb00017ed | %1 - Graceful tear-down failed\r\n
0xb00017ee | %1 - BeforeHostRunningInBackgroundCallback\r\n
0xb00017ef | %1 - BeforeHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f0 | %1 - AfterHostRunningInBackgroundCallback\r\n
0xb00017f1 | %1 - AfterHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f2 | %1 - Unhandled exception occurred. hr = %2\r\n
0xb00017f3 | %1 - State-Transition (%2)->(%3)\r\n
0xb00017f4 | %1 - EnableProfiling = [%2]\r\n
0xb00017f5 | %1 - Profile Dll = [%2]\r\n
0xb00017f6 | %1 - ProfilerCLSID = [%2]\r\n
0xb00017f7 | %1 - TaskHostHelper::SetProfilerSettings hr = %2\r\n
0xb00017f8 | %1 - File path = %2 : %3\r\n
0xb00017f9 | %1 - Parse Element: %2.\r\n
0xb00017fa | %1 - Parse Element Value = %2 with pwszLocalName = %3.\r\n
0xb00017fb | %1 - Parse HResult = %2\r\n
0xb00017fc | %1 - YUTHost: failed to GAC trusted assembly %2\r\n\r\n
0xb00017fd | %1 - UITaskHandler::Initialize. hr = %2\r\n
0xb00017fe | %1 - UITaskHandler::Disconnect done\r\n
0xb00017ff | %1 - UITaskHandler::GoBackground. hr = %2\r\n
0xb0001800 | %1 - UITaskHandler::GoForeground. hr = %2\r\n
0xb0001801 | %1 - Managed Framework Ready. Handling Pending Event:[%2]\r\n
0xb0001802 | %1 - HandlePendingEvents Start TaskId=%2\r\n
0xb0001803 | %1 - HandlePendingEvents Pause TaskId=%2\r\n
0xb0001804 | %1 - HandlePendingEvents Resume TaskId=%2\r\n
0xb0001805 | %1 - Waiting for Siblings...\r\n
0xb0001806 | %1 - Waiting for Siblings done. hr = %2\r\n
0xb0001807 | %1 - UITaskHandler::OnRuntimeHostReady TaskID:[%2]\r\n
0xb0001808 | %1 - UITaskHandler::OnRuntimeHostReady. Processed pending SystemKeyPress [%2]\r\n
0xb0001809 | %1 - UITaskHandler::OnRuntimeHostReady hr = %2\r\n
0xb000180a | %1 - UITaskHandler::RegistrationComplete hr = %2\r\n
0xb000180b | %1 - UITaskHandler::ConnectionComplete received\r\n
0xb000180c | %1 - UITaskHandler::ConnectionComplete hr = %2\r\n
0xb000180d | %1 - UITaskHandler::ProcessActivationData received, reason=%2\r\n
0xb000180e | %1 - UITaskHandler::ProcessActivationData hr = %2\r\n
0xb000180f | %1 - UITaskHandler::Show received. Direction:[%2]\r\n
0xb0001810 | %1 - Navigation in progress. Queuing up the Show\r\n
0xb0001811 | %1 - UITaskHandler::Show hr = %2\r\n
0xb0001812 | %1 - UITaskHandler::ShowInternal. Direction:[%2:NavigationDirection:]\r\n
0xb0001813 | %1 - UITaskHandler::ShowInternal. hr = %2\r\n
0xb0001814 | %1 - UITaskHandler::Hide received. Direction:[%2]\r\n
0xb0001815 | %1 - Navigation in progress. Cancelling Show and ignoring Hide\r\n
0xb0001816 | %1 - UITaskHandler::Hide hr = %2\r\n
0xb0001817 | %1 - UITaskHandler::NavigateTo received TaskID:[%2]\r\n
0xb0001818 | %1 - UITaskHandler::NavigateTo. hr = %2\r\n
0xb0001819 | %1 - UITaskHandler::NavigationComplete TaskID:[%2]\r\n
0xb000181a | %1 - UITaskHandler::NavigationComplete hr = %2\r\n
0xb000181b | %1 - UITaskHandler::NavigateAway received TaskID:[%2]\r\n
0xb000181c | %1 - Navigation interrupted since Task is closing\r\n
0xb000181d | %1 - Navigation in progress. Queuing up the NavigateAway\r\n
0xb000181e | %1 - UITaskHandler::NavigateAway hr = %2\r\n
0xb000181f | %1 - UITaskHandler::NavigateAwayInternal TaskID:[%2]\r\n
0xb0001820 | %1 - UITaskHandler::NavigateAwayInternal hr = %2\r\n
0xb0001821 | %1 - UITaskHandler::RequestClose called TaskID:[%2]\r\n
0xb0001822 | %1 - UITaskHandler::RequestClose hr = %2\r\n
0xb0001823 | %1 - LaunchSession in progress. Cannot add another callback\r\n
0xb0001824 | %1 - UITaskHandler::LaunchSession hr = %2\r\n
0xb0001825 | %1 - LaunchChildTask in progress. Cannot add another callback\r\n
0xb0001826 | %1 - UITaskHandler::LaunchChildTask hr = %2\r\n
0xb0001827 | %1 - UITaskHandler::SetPauseOnLock[%2] called TaskID:[%3]\r\n
0xb0001828 | %1 - UITaskHandler::SetPauseOnLock hr = %2\r\n
0xb0001829 | %1 - UITaskHandler::Close received TaskID:[%2]\r\n
0xb000182a | %1 - UITaskHandler::Close hr = %2\r\n
0xb000182b | %1 - UITaskHandler::SystemKeyPressed received: [%2]\r\n
0xb000182c | %1 - UITaskHandler::SystemKeyPressed processed\r\n
0xb000182d | %1 - UITaskHandler::SystemKeyPressed pending. Will be processed on RuntimeHost ready\r\n
0xb000182e | %1 - UITaskHandler::LaunchChildTaskComplete received with result %2\r\n
0xb000182f | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001830 | %1 - UITaskHandler::LaunchSessionComplete received with result %2\r\n
0xb0001831 | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001832 | %1 - OrientationChanged NewOrientation=%2\r\n
0xb0001833 | %1 - OrientationChange received before RuntimeHostTask is set\r\n
0xb0001834 | %1 - SetSupportedOrientations. SupportedOrientations:[%2]. hr = %3\r\n
0xb0001835 | %1 - GetSupportedOrientations. SupportedOrientations[%2]. hr = %3\r\n
0xb0001836 | %1 - GetCurrentOrientation. CurrentOrientation[%2]. hr = %3\r\n
0xb0001837 | %1 - UITaskHandler::ReplaceTouchEndpoint hr = %2\r\n
0xb0001838 | %1 - UITaskHandler::ReplaceTextEndpoint hr = %2\r\n
0xb0001839 | %1 - UITaskHandler::Get Task State. StateSize[%2]. hr = %3\r\n
0xb000183a | %1 - UITaskHandler::Set Task State. StateSize[%2]. hr = %3\r\n
0xb000183b | %1 - UITaskHandler::OnObscurityChange[%2]. hr = %3\r\n
0xb000183c | %1 - UITaskHandler::OnLockScreenVisibilityChange[%2]. hr = %3\r\n
0xb000183d | %1 - UITaskHandler::OnSipVisibilityChange[%2]. hr = %3\r\n
0xb000183e | %1 - UITaskHandler::OnShowAnimationComplete\r\n
0xb000183f | %1 - UITaskHandler::Window.Visible property changed [%2]\r\n
0xb0001840 | %1 - FreezeHost event triggered\r\n
0xb0001841 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001842 | %1 - CancelTask TaskId=%2\r\n
0xb0001843 | %1 - OnHostPausing\r\n
0xb0001844 | %1 - OnHostPausing failed with hr = %2\r\n
0xb0001845 | %1 - OnHostPaused\r\n
0xb0001846 | %1 - OnHostPaused failed with hr = %2\r\n
0xb0001847 | %1 - FreezeHost event triggered\r\n
0xb0001848 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001849 | %1 - CancelTask received while executing in background\r\n
0xb000184a | %1 - CancelTask received. Ignoring since this is a valid transition only when running in background\r\n
0xb000184b | %1 - CancelTask hr = %2\r\n
0xb000184c | %1 - TPA entry: %2\\%3%4;\r\n
0xb000184d | %1 - Platform Assemblies List: %2\r\n
0xb000184e | %1 - ParseManifestFile HResult = %2\r\n
0xb000184f | %1 - NotifyError ! Unable to disable NI optimizations\r\n
0xb0001850 | %1 - NotifyError ! Unable to set the debugger wait env variable\r\n
0xb0001851 | %1 - TestTrustedPath: %2\r\n
0xb0001852 | %1 - TestAppPaths: %2\r\n
0xb0001853 | %1 - NotifyError ! Failed to set the test settings\r\n
0xb0001854 | %1 - GetAppPaths failed with hr = %2\r\n
0xb0001855 | %1 - NotifyError ! message = %2, source = %3\r\n
0xb0001856 | %1 - NotifyError ! hr=%2. message = %3\r\n
0xb0001857 | %1 - GetIsoStoreAvailableFreeSpace hr = %2\r\n
0xb0001858 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb0001859 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb000185a | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185b | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185c | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb000185d | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb000185e | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb000185f | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb0001860 | %1 - GetQualifiedMutexName returned:[%2]. AllowedMutexCount:[%3]\r\n\r\n
0xb0001861 | %1 - XcpHost::Start() failed with hr = %2\r\n
0xb0001862 | %1 - Shutting down the SL runtime...\r\n
0xb0001863 | %1 - Calling into XcpHost::Pausing %2\r\n
0xb0001864 | %1 - XcpHost::Pausing %2\r\n
0xb0001865 | %1 - Calling into XcpHost::Pause %2\r\n
0xb0001866 | %1 - XcpHost::Pause %2\r\n
0xb0001867 | %1 - Calling into XcpHost::Resume %2\r\n
0xb0001868 | %1 - XcpHost::Resume %2\r\n
0xb0001869 | %1 - Calling into XcpHost::Resumed %2\r\n
0xb000186a | %1 - XcpHost::Resumed %2\r\n
0xb000186b | %1 - XcpHost::CompleteTask called TaskID:[%2]\r\n
0xb000186c | %1 - CompleteTask called when XcpTask is null. This likely indicates CompleteTask getting called twice\r\n
0xb000186d | %1 - Error in OnApplicationStarted\r\n
0xb000186e | %1 - Error in OnApplicationConstructing\r\n
0xb000186f | %1 - LaunchSession hr = %2\r\n
0xb0001870 | %1 - LaunchChildTask hr = %2\r\n
0xb0001871 | %1 - Raising Task.OnLaunching\r\n
0xb0001872 | %1 - Raised Task.OnLaunching\r\n
0xb0001873 | %1 - Raising Task.OnPause. PauseReason[%2]\r\n
0xb0001874 | %1 - Raised Task.OnPause\r\n
0xb0001875 | %1 - Raising Task.OnResume. IsExecutionContextPreserved[%2]\r\n
0xb0001876 | %1 - Raised Task.OnResume\r\n
0xb0001877 | %1 - Raising Task.OnRunningInBackground\r\n
0xb0001878 | %1 - Raised Task.OnRunningInBackground\r\n
0xb0001879 | %1 - Raising Task.OnCancel\r\n
0xb000187a | %1 - Raised Task.OnCancel\r\n
0xb000187b | %1 - Raising Task.OnHostDehydarting\r\n
0xb000187c | %1 - Raised Task.OnHostDehydarting\r\n
0xb000187d | %1 - Raising Task.OnNavigateTo\r\n
0xb000187e | %1 - Raised Task.OnNavigateTo\r\n
0xb000187f | %1 - Raising Task.OnNavigateAway\r\n
0xb0001880 | %1 - Raised Task.OnNavigateAway\r\n
0xb0001881 | %1 - Raising Task.OnShow\r\n
0xb0001882 | %1 - Raised Task.OnShow\r\n
0xb0001883 | %1 - Raising Task.OnHide\r\n
0xb0001884 | %1 - Raised Task.OnHide\r\n
0xb0001885 | %1 - Raising Task.OnSystemKeyPressed\r\n
0xb0001886 | %1 - Raised Task.OnSystemKeyPressed\r\n
0xb0001887 | %1 - Raising Task.OnChildTaskReturned\r\n
0xb0001888 | %1 - Raised Task.OnChildTaskReturned\r\n
0xb0001889 | %1 - Raising Task.OnObscurityChange\r\n
0xb000188a | %1 - Raised Task.OnObscurityChange\r\n
0xb000188b | %1 - Raising Task.OnLockScreenVisibilityChange\r\n
0xb000188c | %1 - Raised Task.OnLockScreenVisibilityChange\r\n
0xb000188d | %1 - Raising Task.OnClosing\r\n
0xb000188e | %1 - Raised Task.OnClosing\r\n
0xb000188f | %1 - RegisterAppCallbacks hr = %2\r\n
0xb0001890 | %1 - RegisterTaskCallbacks hr = %2\r\n
0xb0001891 | %1 - TaskReadyToShow hr = %2\r\n
0xb0001892 | %1 - RequestCloseTask hr = %2\r\n
0xb0001893 | %1 - CompleteTask hr = %2\r\n
0xb0001894 | %1 - DestroyTaskCallbacks hr = %2\r\n
0xb0001895 | %1 - SetHostErrorCode hrHostError = %2, hr = %3\r\n
0xb0001896 | %1 - LaunchSession[%2] hr = %3\r\n
0xb0001897 | %1 - GetTaskState hr = %2\r\n
0xb0001898 | %1 - SetTaskState hr = %2\r\n
0xb0001899 | %1 - LaunchChildTask[%2] hr = %3\r\n
0xb000189a | %1 - GetTaskAppChromeHandle hr = %2\r\n
0xb000189b | %1 - SetTaskPauseOnLock hr = %2\r\n
0xb000189c | %1 - SetHostObscurity[%2] hr = %3\r\n
0xb000189d | %1 - Entering Modal state\r\n
0xb000189e | %1 - Exiting Modal state hr = %2\r\n
0xb000189f | %1 - NotifyError: message=%2, source=%3\r\n
0xb00018a0 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb00018a1 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb00018a2 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a3 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a4 | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb00018a5 | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb00018a6 | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb00018a7 | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb00018a8 | %1 - Raising Task.OnRefresh\r\n
0xb00018a9 | %1 - Raised Task.OnRefresh\r\n
0xb00018aa | %1 - UITaskHandler::RequestNavigateBack called TaskID:[%2]\r\n
0xb00018ab | %1 - UITaskHandler::RequestNavigateBack hr = %2\r\n
0xb00018ac | %1 - RequestNavigateBack hr = %2\r\n
0xb00018ad | %1 - UITaskHandler::SetFullScreen[%2] called TaskID:[%3]\r\n
0xb00018ae | %1 - UITaskHandler::SetFullScreen hr = %2\r\n
0xb00018af | %1 - SetTaskFullScreen hr = %2\r\n
0xb00018b0 | %1 - Raising Task.OnApplicationLayerChange\r\n
0xb00018b1 | %1 - Raised Task.OnApplicationLayerChange\r\n
0xb00018b2 | %1 - Raising Task.OnRequestOverlayStateChange. State=%2\r\n
0xb00018b3 | %1 - Raised Task.OnRequestOverlayStateChange\r\n
0xb00018b4 | %1 - ApplicationLayerChanged NewApplicationLayer=%2\r\n
0xb00018b5 | %1 - ApplicationLayerChange received before RuntimeHostTask is set\r\n
0xb00018b6 | %1 - AgTaskHandler::LaunchSession hr = %2\r\n
0xb00018b7 | %1 - AgTaskHandler::LaunchChildTask hr = %2\r\n
0xb00018b8 | %1 - GetSessionDisplayName. DisplayName=%2 hr = %3\r\n
0xb00018b9 | %1 - AgTaskHandler::ConnectionComplete received\r\n
0xb00018ba | %1 - AgTaskHandler::ConnectionComplete hr = %2\r\n
0xb00018bb | %1 - UITaskHandler::OnNavigationBarVisibilityChange[%2]. hr = %3\r\n
0xb00018bc | %1 - Raising Task.OnModernActivation\r\n
0xb00018bd | %1 - Raised Task.OnModernActivation\r\n
0xb00018be | %1 - UITaskHandler::LaunchModernChooser hr = %2\r\n
0xb00018bf | %1 - LaunchChildTask hr = %2\r\n
0xb00018c0 | %1 - LaunchModernChooser[%2] hr = %3\r\n
0xb00018c1 | %1 - TaskFirstPresentCompleted = %2\r\n
0xb00018c2 | %1 - UITaskHandler::FirstPresentCompleted called TaskID:[%2]\r\n
0xb00018c3 | %1 - UITaskHandler::FirstPresentCompleted hr = %2\r\n
0xb0001fa4 | AgHost - FrameworkView::Initialize HRESULT=%1\r\n
0xb0001fa5 | AgHost - FrameworkView::SetWindow HRESULT=%1\r\n
0xb0001fa6 | AgHost - FrameworkView::Load HRESULT=%1\r\n
0xb0001fa7 | AgHost - FrameworkView::Run HRESULT=%1\r\n
0xb0001fa8 | AgHost - FrameworkView::Uninitialize HRESULT=%1\r\n
0xb0001fa9 | AgHost - FrameworkView::OnActivated PreviousExecutionState=%1 ActivationKind=%2 HRESULT=%3\r\n
0xb0001faa | AgHost - FrameworkView::OnExiting HRESULT=%1\r\n
0xb0001fab | AgHost - FrameworkView::OnResuming HRESULT=%1\r\n
0xb0001fac | AgHost - FrameworkView::OnSuspending HRESULT=%1\r\n
0xb0001fae | AgHostSvcs - EmCancelTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001faf | AgHostSvcs - EmCreateTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb0 | AgHostSvcs - EmExitTaskHost HRESULT=%1\r\n
0xb0001fb1 | AgHostSvcs - EmPauseTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb2 | AgHostSvcs - EmResumeTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb3 | AgHostSvcs - EmSetTaskInstanceApplicationUri TaskID=%1 ApplicationUri=%2 HRESULT=%3\r\n
0xb0001fb4 | AgHostSvcs - EmSetTaskInstanceArguments TaskID=%1 HRESULT=%2\r\n
0xb0001fb5 | AgHostSvcs - EmSetTaskInstanceBackgroundTaskId TaskID=%1 BackgroundTaskID=%2 HRESULT=%3\r\n
0xb0001fb6 | AgHostSvcs - EmSetTaskInstanceNavigationPage TaskID=%1 NavigationPage=%2 HRESULT=%3\r\n
0xb0001fb7 | AgHostSvcs - EmStartTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb8 | AgHostSvcs - TaskCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fb9 | AgHostSvcs - TaskPaused TaskID=%1 HRESULT=%2\r\n
0xb0001fba | AgHostSvcs - TaskRunning TaskID=%1 HRESULT=%2\r\n
0xb0001fbb | AgHostSvcs - TaskRunningInBackground TaskID=%1 HRESULT=%2\r\n
0xb0001fbc | AgHostSvcs - TaskRunningInForeground TaskID=%1 HRESULT=%2\r\n
0xb0001fbd | AgHostSvcs - EmWaitForTaskInstanceCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fbe | AgHostSvcs - OnModernContractActivation TaskID=%1 HRESULT=%2\r\n
0xb0002008 | EEC: GetExtendedExecutionBroker ProcessId=%1 HRESULT=%2\r\n
0xb0002009 | EEC: RegisterRevokedHandler ProcessId=%1 HRESULT=%2\r\n
0xb000200a | EEC: RequestExtendedExecution ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200b | EEC: ExtensionRevokedCallback ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200c | EEC: CompleteExtendedExecution ProcessId=%1 HRESULT=%2\r\n
0xb000206c | ODB: LaunchTask - UserSid: %1 SessionId: %2 PackageFullName: %3 EntryPoint: %4 WorkItemId: %5 HRESULT: %6.\r\n
0xb000206d | ODB: CancelTask - UserSid: %1 SessionId: %2 WorkItemId: %3 RudeTerminate: %4 CancellationReason: %5 HRESULT: %6.\r\n
0xb000206e | ODB: BeforeTaskActivated - WorkItemId: %1 PsmKey: %2 HostJobType: %3 HRESULT: %4.\r\n
0xb000206f | ODB: TaskActivated - WorkItemId: %1 TaskInstanceId: %2 PsmKey: %3 HRESULT: %4.\r\n
0xb0002070 | ODB: TaskCompleted - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002071 | ODB: TaskCanceled - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002072 | ODB: Timeout in WaitForWnfStateQuiescentTimeout.\r\n
0xb0002073 | ODB: CancelBackgroundTaskWithWnf WorkItemId: %1.\r\n
0xb0002710 | %1\r\n
0xb0002711 | %1: %2\r\n
0xb0002712 | *** ExecFailFast ***   %1\r\n
0xb000271a | PreInstallTaskPolicy: Activate task for User = %1 HRESULT = %2\r\n
0xb000271b | PreInstallTaskPolicy: BiActivate WorkItemId = %1 for user = %2, PackageFullName = %3, EntryPoint = %4, HRESULT = %5\r\n
0xd0000001 | Resumed\r\n
0xd0000002 | Quiescing\r\n
0xd0000003 | Quiesced\r\n
0xd0000004 | Frozen\r\n
0xd0000005 | Dehydrated\r\n
0xd0000006 | Terminated\r\n
0xd0000007 | Resumed\r\n
0xd0000008 | Suspending\r\n
0xd0000009 | Suspended\r\n
0xd000000a | Terminated\r\n
0xd000000b | NotBackground\r\n
0xd000000c | MixedHost\r\n
0xd000000d | PureHost\r\n
0xd000000e | SystemHost\r\n
0xd000000f | InvalidType\r\n
0xd0000010 | Permitted\r\n
0xd0000011 | Buffered\r\n
0xd0000012 | Dropped\r\n
0xd0000013 | InvalidType\r\n
0xd0000014 | Invalid\r\n
0xd0000015 | ForegroundApp\r\n
0xd0000016 | Cbe\r\n
0xd0000017 | ForegroundAgent\r\n
0xd0000018 | GbaPeriodic\r\n
0xd0000019 | GbaIdle\r\n
0xd000001a | BackgroundAudio\r\n
0xd000001b | BackgroundWorker\r\n
0xd000001c | Voip\r\n
0xd000001d | Oem\r\n
0xd000001e | Invalid\r\n
0xd000001f | Started\r\n
0xd0000020 | Paused\r\n
0xd0000021 | Resumed\r\n
0xd0000022 | MovedToBackground\r\n
0xd0000023 | RunUnderLock\r\n
0xd0000024 | Invalid\r\n
0xd0000025 | OK\r\n
0xd0000026 | Abort\r\n
0xd0000027 | Unexpected\r\n
0xd0000028 | ExceededRuntime\r\n
0xd0000029 | ResourcesSeized\r\n
0xd000002a | Paused\r\n
0xd000002b | Resumed\r\n
0xd000002c | ScreenLock\r\n
0xd000002d | ScreenUnlocked\r\n
0xd000002e | MovedToBackground\r\n
0xd000002f | CbeExitTimeout\r\n
0xd0000030 | CbeExitBatterySaver\r\n
0xd0000031 | CbeExitParallelAgentPolicy\r\n
0xd0000032 | CbeExitResourcesUnavailable\r\n
0xd0000033 | CbeExitControlPanel\r\n
0xd0000034 | CbeExitBandwidthSavings\r\n
0xd0000035 | HeadlessHost\r\n
0xd0000036 | TaskHost\r\n
0xd0000037 | XcpHost\r\n
0xd0000038 | TaskHostSvcs\r\n
0xd0000039 | TaskHostUnitTests\r\n
0xd000003a | HOST_CREATED\r\n
0xd000003b | HOST_INITIALIZED\r\n
0xd000003c | HOST_RUNNING\r\n
0xd000003d | STARTING_TASK\r\n
0xd000003e | REHYDRATING_TASK\r\n
0xd000003f | HOST_READY\r\n
0xd0000040 | HOST_PAUSING\r\n
0xd0000041 | PAUSING_TASK\r\n
0xd0000042 | PAUSED_TASK\r\n
0xd0000043 | HOST_PAUSED\r\n
0xd0000044 | RESUMING_TASK\r\n
0xd0000045 | HOST_GOING_IN_BACKGROUND\r\n
0xd0000046 | TASK_GOING_IN_BACKGROUND\r\n
0xd0000047 | HOST_IN_BACKGROUND\r\n
0xd0000048 | TASK_GOING_IN_FOREGROUND\r\n
0xd0000049 | GRACEFULLY_DEHYDRATING_HOST\r\n
0xd000004a | HOST_VISIBLE\r\n
0xd000004b | HOST_HIDDEN\r\n
0xd000004c | HOST_FROZEN\r\n
0xd000004d | HOST_THAWED\r\n
0xd000004e | HOST_EXITING\r\n
0xd000004f | HOST_ERROR\r\n
0xd0000050 | Direction_Forward\r\n
0xd0000051 | Direction_Backward\r\n
0xd0000052 | Direction_ForceSize\r\n
0xd0000053 | Resumed\r\n
0xd0000054 | Pausing\r\n
0xd0000055 | Paused\r\n
0xd0000056 | Dehydrated\r\n
0xd0000057 | Completed\r\n
0xd0000058 | none\r\n
0xd0000059 | launch\r\n
0xd000005a | debug\r\n
0xd000005b | task completion\r\n
0xd000005c | dependency\r\n
0xd000005d | multi-view\r\n
0xd000005e | Waiting\r\n
0xd000005f | CompletedWithResult\r\n
0xd0000060 | CompletedWithNoResult\r\n
0xd0000061 | Foreground\r\n
0xd0000062 | Lock\r\n
0xd0000063 | Overlay\r\n
0xd0000064 | ModernForeground\r\n
0xd0000065 | Pausing\r\n
0xd0000066 | PausingLowPri\r\n
0xd0000067 | Paused\r\n
0xd0000068 | PausingHighPri\r\n
0xd0000069 | PausedDNK\r\n
0xd000006a | Frozen\r\n
0xd000006b | FrozenHighPri\r\n
0xd000006c | FrozenDNK\r\n
0xd000006d | LockScreen\r\n
0xd000006e | Overlay\r\n
0xd000006f | 11\r\n
0xd0000070 | CalendarAsChild\r\n
0xd0000071 | VideoTranscode\r\n
0xd0000072 | CBE\r\n
0xd0000073 | ExtendedExecution\r\n
0xd0000074 | ModernForegroundLarge\r\n
0xd0000075 | ShellCustom1\r\n
0xd0000076 | ShellCustom2\r\n
0xd0000077 | ShellCustom3\r\n
0xd0000078 | DebugModeForeground\r\n
0xd0000079 | Invalid\r\n
0xd000007a | Unevaluated\r\n
0xd000007b | EvaluationPending\r\n
0xd000007c | Evaluated\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x10000006 | ExecMan\r\n
0x10000009 | TaskHost\r\n
0x1000000d | Sqm\r\n
0x1000000f | Lifetime Manager\r\n
0x10000010 | ForegroundManager\r\n
0x10000011 | Background Manager\r\n
0x10000012 | Production Circular\r\n
0x10000013 | Production Critical\r\n
0x10000014 | SelfHost Circular\r\n
0x10000015 | SelfHost Critical\r\n
0x10000016 | DevPlat Circular\r\n
0x10000017 | VOIP\r\n
0x1000001b | Activation Manager\r\n
0x1000001c | AgHost\r\n
0x10000020 | Telemetry\r\n
0x10000021 | ExtendedExecutionClient\r\n
0x10000022 | OnDemandBroker\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000007 | Resume\r\n
0x30000008 | Suspend\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-AppModelExecEvents\r\n
0xb0000064 | DepMgr: Removed suspension group from the graph, PsmKey=%1\r\n
0xb0000065 | Not set app %1 into halted state because it should wait for other apps in the package halted first\r\n
0xb0000066 | Not set app %1 into halted state because other app in the package have not finished quiescing\r\n
0xb0000067 | Not terminate app %1, because target app %2 state = %3\r\n
0xb0000068 | Updated current dependency graph (Removal : %1) with Source %2 and Target %3 for type %4 in return %5\r\n
0xb0000069 | Default time for %1 overridden to %2 ms\r\n
0xb000006a | Creating hang report\r\n
0xb000006b | Window %1 is hung in foreground\r\n
0xb000006c | Window %1 is no longer hung in foreground\r\n
0xb000006d | Waiting for WER reporting to finish on app %1\r\n
0xb000006e | Hang reporting finished on app %1.  App termination status: %2\r\n
0xb000006f | Hung reporting finished on window %1 with result %2\r\n
0xb0000070 | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb0000071 | _SubmitActivationHangWerReport(stop): Aumid=%1, result=%2\r\n
0xb0000072 | _UnregisterForStateChanges: fPackageLevel=%1, HRESULT is %2. Cookie is %3\r\n
0xb0000073 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000074 | Canceled launch grace timer, PsmKey=%1\r\n
0xb0000075 | _InitializeLaunchGraceContext: Aumid=%1, fExtendedLaunch=%2, fEventExists=%3\r\n
0xb0000076 | App %1 successfully launched and its launch grace period expired: removing suspend exemption\r\n
0xb0000077 | Forcefully terminating app, Aumid=%1 flags=%2, reason=%3\r\n
0xb0000078 | CheckTerminationBeforeSwitch: Should terminate: %1, Aumid=%2, HRESULT=%3, reason=%4, fIsMisbehaving=%5\r\n
0xb0000079 | Termination requested for %1 - flags %2\r\n
0xb000007a | Failing TerminateApp due to pending task completions: %1\r\n
0xb000007b | Terminating %1 immediately\r\n
0xb000007c | Uninstalling background work items for %1\r\n
0xb000007d | Termination of %1 scheduled for %2 ms in future\r\n
0xb000007e | Sent window message to the default immersive browser with HRESULT %1\r\n
0xb000007f | Attempting to terminate app %1 prior to new app launch due to pending termination\r\n
0xb0000080 | EvaluateAndTerminatePid: PID: %1. HRESULT: %2. Package State: %3\r\n
0xb0000081 | Exempting application %1 from suspend while it is being launched\r\n
0xb0000082 | Exemption manager %1 is requesting a higher minimum priority %2 for %3\r\n
0xb0000083 | Debug mode is enabled for %1, so it will run at %2 priority\r\n
0xb0000084 | Handling logoff, %1 will run at %2 priority\r\n
0xb0000085 | Throttling has been disabled, so %1 will run at %2 priority\r\n
0xb0000086 | Suspend denied due to new key debounce, PsmKey=%1\r\n
0xb0000087 | Suspend denied due to debug mode, PsmKey=%1\r\n
0xb0000088 | Not suspending application %1 due to exemption %2\r\n
0xb0000089 | _EvaluateAndSuspendApplication: PsmKey=%1, fIsSuspendAllowed=%2, HRESULT=%3\r\n
0xb000008a | _ReevaluatePolicy: Ignoring debug mode app, PsmKey=%1\r\n
0xb000008b | ManagePreExistingApps(start)\r\n
0xb000008c | ManagePreExistingApps: PsmKey=%1, Aumid=%2, hr=%3\r\n
0xb000008d | ManagePreExistingApps(stop)\r\n
0xb000008e | RequestSuspendTimeout called for application %1 and timeout %2\r\n
0xb000008f | Debug mode enabled, PkgFamilyName=%1\r\n
0xb0000090 | Debug mode disabled, PkgFamilyName=%1\r\n
0xb0000091 | Set Package %1, Timeout to %2\r\n
0xb0000092 | ResumeDebugModePackage(start): package=%1\r\n
0xb0000093 | ResumeDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000094 | SuspendDebugModePackage(start): package=%1\r\n
0xb0000095 | SuspendDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000096 | MultiAppSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000097 | MultiAppSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb0000098 | MultiPackageSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000099 | MultiPackageSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009a | MultiPackageSuspendAndPendTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb000009b | MultiPackageSuspendAndPendTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009c | TerminateSync(start): PsmKey=%1, type=%2, reason=%3\r\n
0xb000009d | TerminateSync(stop): PsmKey=%1, hrLogReason=%2, hrTermination=%3\r\n
0xb000009e | TerminatePackageSync(start): Package=%1, type=%2, reason=%3\r\n
0xb000009f | TerminatePackageSync(stop): Package=%1, fPlmKnowsPackage=%2, HRESULT=%3\r\n
0xb00000a0 | _TerminateAllSuspendedApplications(start)\r\n
0xb00000a1 | _TerminateAllSuspendedApplications(stop): HRESULT=%1\r\n
0xb00000a2 | Application %1 is blocking Connected Standby\r\n
0xb00000a3 | Exiting Connected Standby\r\n
0xb00000a4 | All packages have been suspended or terminated. Notify PDC. Call to PdcNotificationClientAcknowledge() returned %1\r\n
0xb00000a5 | Kernel State Change Callback: There were %1 PIDs present in the callback data\r\n
0xb00000a6 | Kernel State Change Callback: The state source was %1\r\n
0xb00000a7 | PDC_CONTROL_ABORT: PdcNotificationClientAcknowledge(STATUS_SUCCESS) returned %1\r\n
0xb00000a8 | Not terminating application %1 in _EvaluateAndTerminateApplication because it contains a running IImmersiveApplication\r\n
0xb00000a9 | Not terminating application %1 in _EvaluateAndTerminateApplication because it is a long running app\r\n
0xb00000aa | Not terminating application %1 in _EvaluateAndTerminateApplication due to pending task completion\r\n
0xb00000ab | Not terminating application %1 in _EvaluateAndTerminateApplication due to Launch Grace\r\n
0xb00000ac | Not terminating application %1 in _EvaluateAndTerminateApplication due to debug mode\r\n
0xb00000ad | Not terminating application %1 in _EvaluateAndTerminateApplication due to application had already been terminated\r\n
0xb00000ae | _EvaluateAndTerminateApplication: Skipping child suspension group, PsmKey=%1\r\n
0xb00000af | An empty application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b0 | Parent allowed suspension for child app, childPsmKey=%1\r\n
0xb00000b1 | GroupChildWithParent: ChildPsmKey=%1, HRESULT=%2\r\n
0xb00000b2 | Call a command line '%1' to notify default browser with result %2\r\n
0xb00000b3 | Read executable path from registry with result %1\r\n
0xb00000b4 | Application %1 was added to PLM Data Store and registering for PSM notification\r\n
0xb00000b5 | Resume the PPLE app %1 when receiving the PSM new key notification\r\n
0xb00000b6 | An orphaned prereq application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b7 | Not terminating dependent application %1 in _EvaluateAndTerminateDependentApplication due other dependency applications\r\n
0xb00000b8 | _EvaluateAndTerminateSourceApplication: Aumid=%1, exemption=%2\r\n
0xb00000b9 | An force termination exemption Application was detected. Setting pending termination for application %1\r\n
0xb00000ba | StateMgr: State queued, PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000bb | StateMgr: OnApplicationStarted set to active, PsmKey=%1\r\n
0xb00000bc | StateMgr: OnApplicationStarted finished, PsmKey=%1, HRESULT=%2\r\n
0xb00000bd | StateMgr: App's current state has changed, PsmKey=%1, state=%2\r\n
0xb00000be | StateMgr: OnApplicationTerminated(start), PsmKey=%1\r\n
0xb00000bf | StateMgr: Application terminated signaled, PsmKey=%1\r\n
0xb00000c0 | StateMgr: OnApplicationTerminated(stop), PsmKey=%1\r\n
0xb00000c1 | StateMgr: GetTerminateSyncData, PsmKey=%1, hr=%2\r\n
0xb00000c2 | StateMgr: _ProcessStateQueue(start): PsmKey=%1, state=%2\r\n
0xb00000c3 | StateMgr: _ProcessStateQueue(stop): PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000c4 | StateMgr: Queue's pause state has changed to %2, PsmKey=%1\r\n
0xb00000c5 | StateMgr: App's committed state has changed, PsmKey=%1, state=%2\r\n
0xb00000c6 | Enabling debug mode on package %1\r\n
0xb00000c7 | Disabling debug mode on package %1\r\n
0xb00000c8 | Suspending package %1 via debug API. HRESULT: %2\r\n
0xb00000c9 | Resuming package %1 via debug API. HRESULT: %2\r\n
0xb00000ca | Terminating package %1 via debug API. HRESULT: %2\r\n
0xb00000cb | Default time for %1 overridden to %2 ms\r\n
0xb00000cc | ReportActivationHangSync: Halt application Aumid=%1, result=%2\r\n
0xb00000cd | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb00000ce | _SubmitActivationHangWerReport(stop): Aumid=%1 canceled(%2) result=%3\r\n
0xb00000cf | PLM doesn't swap out application %1 due to its swap state %2\r\n
0xb00000d0 | PLM termination policy started on background thread because application %1 failed to outswap\r\n
0xb00000d1 | PLM termination policy finished. Outswapping returned status %1\r\n
0xb00000d2 | PLM memory policy will be aggressive because this is a disconnected session\r\n
0xb00000d3 | PLM termination policy start\r\n
0xb00000d4 | PLM termination policy stop\r\n
0xb00000d5 | PLM termination policy triggered by in use memory of %1 MiB\r\n
0xb00000d6 | PLM termination policy triggered by commit charge of %1 MiB\r\n
0xb00000d7 | MemoryPolicyWatcherTerminateCommitCharge\r\n
0xb00000d8 | PLM empty policy triggered by in use memory of %1 MB\r\n
0xb00000d9 | PLM memory policy does not allow termination of application %1 for reason %2\r\n
0xb00000da | PLM memory policy allows termination of application %1\r\n
0xb00000db | Application %1 was hidden %2 seconds ago\r\n
0xb00000dc | Application %1 is the clipboard owner\r\n
0xb00000dd | PLM empty policy start\r\n
0xb00000de | PLM empty policy ignoring application %1 with error code %2\r\n
0xb00000df | PLM empty policy finished after emptying %1 MiB\r\n
0xb00000e0 | PLM termination policy enumerated %1 applications\r\n
0xb00000e1 | PLM memory policy chose application %1 as its termination candidate, over old candidate application %2\r\n
0xb00000e2 | PLM memory policy will terminate application %1 with memory size %2 MiB and score %3\r\n
0xb00000e3 | PLM memory policy received MemWatcher event\r\n
0xb00000e4 | PLM memory policy received MemWatcher event\r\n
0xb00000e5 | Package exemption manager denied suspend for %1.  Ref counts are LAUNCH=%2, PSMREG=%3, PSMPENDING=%4\r\n
0xb00000e6 | Package Exemption Manager: ReferenceAdded:%1, %2 ref to application %3. The ref counts are now LAUNCH=%4, PSMREG=%5, and PSMREGPENDING=%6\r\n
0xb00000e7 | Package %1 added to the package data store\r\n
0xb00000e8 | Resetting priority to unpause the suspension group, PsmKey=%1\r\n
0xb00000e9 | Changed the priority of %1 to %2\r\n
0xb00000ea | AllowServiceOfPackages(start): cPackages=%1, fNotifyBi=%2\r\n
0xb00000eb | AllowServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ec | FinishedServiceOfPackages(start): cPackages=%1\r\n
0xb00000ed | FinishedServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ee | AllowUninstallOfPackage(start): package=%1\r\n
0xb00000ef | AllowUninstallOfPackage(stop): package=%1, HRESULT=%2\r\n
0xb00000f0 | Forcefully terminating misbehaving app %1 due to activation failure %2\r\n
0xb00000f1 | App %1: Change = %2\r\n
0xb00000f2 | PsmKey %1 has state %2\r\n
0xb00000f3 | Changing app state through BI, PsmKey=%1, state=%2 terminate action=%3\r\n
0xb00000f4 | Changing the package state of %1 through BI to %2\r\n
0xb00000f5 | OnAfterQuiescing: Quiesce began for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f6 | _CompleteQuiesceHelper: Queued termination for timed-out PsmKey %1\r\n
0xb00000f7 | Quiesce completed for PsmKey=%1, reason=%2, suspendTrigger=%3\r\n
0xb00000f8 | Suspend trigger updated for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f9 | ExtendQuiesceTimeout: PsmKey=%1, request=%2 ms, HRESULT=%3\r\n
0xb00000fa | _CompleteQuiesceHelper: Ignore timed-out PsmKey %1 as is being debugged\r\n
0xb00000fb | ResumeHelper: Application resume(start), PsmKey=%1, reason=%2\r\n
0xb00000fc | ResumeHelper: Application resume(stop), PsmKey=%1, reason=%2, HRESULT=%3\r\n
0xb00000fd | Resume reason updated for PsmKey=%1, reason=%2\r\n
0xb00000fe | RPC 0->1 transition detected for %1\r\n
0xb00000ff | RPC exemption was granted for application %1. KernelRequest Value: %2. Runaway RPC: %3.  RPC Debounce %4\r\n
0xb0000100 | RPC debounce received for package %1\r\n
0xb0000101 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000102 | Application %1 termination is blocked. PreserverProcessRequest = %2, TaskCompletionCategory = %3\r\n
0xb0000103 | PdcSystem activation (Activate = %1). Result = %2\r\n
0xb0000104 | NetworkAudio entries: %1, IsNetworkReferenced: %2\r\n
0xb0000105 | App %1 is Sharing\r\n
0xb0000106 | Share %1 has started in app %2\r\n
0xb0000107 | Share %1 in app %2 has stopped\r\n
0xb0000108 | Queued termination reason updated for PsmKey=%1, reason=%2\r\n
0xb0000109 | ClearTerminationTypesForForgottenPackage(start): PkgFamilyName=%1\r\n
0xb000010a | Cleared termination type for forgotten app, Aumid=%1, HRESULT=%2\r\n
0xb000010b | ClearTerminationTypesForForgottenPackage(stop): PkgFamilyName=%1, HRESULT=%2\r\n
0xb000010c | Writing to termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010d | Reading termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010e | _ExtendForResourceStarvation: PsmKey=%1, TimerType=%2, newRelativeExpirationTimeMs=%3, ElapsedMs=%4, CpuRunningMs=%5, CpuReadyMs=%6, IoNormalMs=%7\r\n
0xb000010f | Foreground resume delay %1 milliseconds\r\n
0xb0000110 | Suspend allowed for %1 - Session not active\r\n
0xb0000111 | Suspend denied due to a visible window or visibility debounce, PsmKey=%1\r\n
0xb0000112 | Suspend denied for %1 - UserRequest non-zero\r\n
0xb0000113 | Suspend denied for %1- failure %2\r\n
0xb0000114 | OnWindowChanged: Aumid=%1, Hwnd=%2, change=%3, fDeferredVisibility=%4, HRESULT=%5\r\n
0xb0000115 | Starting Session Idle Debounce\r\n
0xb0000116 | Session is active\r\n
0xb0000117 | Session is idle\r\n
0xb0000118 | PlmGetPackageFullNameFromAppId, Aumid=%1, HRESULT=%2\r\n
0xb0000119 | Session idle state change -- calling _ReevaluatePolicy\r\n
0xb000011a | RegisterForActivationStateChanges: Act:%1 App:%2 HRESULT is %3. Cookie is %4\r\n
0xb000011b | UnregisterForActivationStateChanges: Cookie is %1\r\n
0xb000011c | Can Auto Terminate app %1 %2\r\n
0xb000011d | TerminateApplicationBeforeActivation(start): Aumid=%1\r\n
0xb000011e | TerminateApplicationBeforeActivation: wait for terminate, Aumid=%1, HRESULT=%2\r\n
0xb000011f | TerminateApplicationBeforeActivation(stop): Aumid=%1, reason=%2, HRESULT=%3\r\n
0xb0000120 | s_SuspendPackagesAtLogOff(start)\r\n
0xb0000121 | s_SuspendPackagesAtLogOff(stop): HRESULT=%1\r\n
0xb0000122 | StateMgr: OnApplicationStarted still halted, PsmKey=%1\r\n
0xb0000123 | Added Task Completion under %1 for application %2\r\n
0xb0000124 | Removed Task Completion under %1 for application %2\r\n
0xb0000125 | Illegal state change happened to App: %1\r\n
0xb0000126 | EnableDebugMode failed: %1\r\n
0xb0000127 | DisableDebugMode: RoDisableDebuggingForPackage failed with result %1\r\n
0xb0000128 | DisableDebugMode: OnDebugModeDisabled failed with result %1\r\n
0xb0000129 | DisableDebugMode: Enabling activation timeout failed with result %1\r\n
0xb000012a | DisableDebugMode failed: %1\r\n
0xb000012b | Couldn't open process: %1\r\n
0xb000012c | PLM failed to process a hang for window %1 with error code %2\r\n
0xb000012d | PLM outswap application %1 failed to invoke with error code %2\r\n
0xb000012e | PLM couldn't find any process for application %1, and handle it as non-large app\r\n
0xb000012f | PLM failed to decide application %1 is large or not with error code %2\r\n
0xb0000130 | PLM empty policy failed to process application %1 with error code %2.  Ignoring the application\r\n
0xb0000131 | PLM empty policy failed to empty application %1 with error code %2\r\n
0xb0000132 | PLM failed to terminate application %1 as empty policy with error code %2\r\n
0xb0000133 | PLM empty policy failed to enumerate applications with error code %1\r\n
0xb0000134 | PLM termination policy skipping application %1, which is not registered with PLM\r\n
0xb0000135 | PLM memory policy failed to queue work with error code %1\r\n
0xb0000136 | GetPackageData called on a Package %1, which is not in the PLM Package Data Store\r\n
0xb0000137 | ERROR: Failed to set priority to %1, PsmKey=%2, NTSTATUS=%3\r\n
0xb0000138 | AllowServiceOfPackages: Failed to terminate package=%1, type=%2, HRESULT=%3\r\n
0xb0000139 | _CheckServicingPackages: Failed to enumerate app, PsmKey=%1, HRESULT=%2\r\n
0xb000013a | _CheckServicingPackages: Failed to enumerate package, PkgFullName=%1, HRESULT=%2\r\n
0xb000013b | GetImmersiveApplicationCount failed with error code %1\r\n
0xb000013c | Background workitems were force terminated, PsmKey=%1\r\n
0xb000013d | ChangeApplicationBiState failed: %1\r\n
0xb000013e | Background workitems for package %1 were force terminated\r\n
0xb000013f | ChangePackageBiState failed: %1\r\n
0xb0000140 | ApplicationProcesses failed to track process ID %1 with error code %2\r\n
0xb0000141 | OnBeforeQuiescing: Failed to allocate memory for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000142 | OnAfterQuiescing: Quiesce failed for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000143 | ERROR: _CompleteQuiesceHelper: Failed to terminate timed-out PsmKey %1 with result %2\r\n
0xb0000144 | ERROR: QuiesceHelper: App forgotten while still Quiescing, PsmKey=%1, suspendTrigger=%2\r\n
0xb0000145 | Failed to query the wake counters associated with application %1. NTSTATUS: %2\r\n
0xb0000146 | _AllAppSyncOperationHelper: Failed to allocate memory for PsmKey=%1, HRESULT=%2\r\n
0xb0000147 | _MultiAppSyncOperationHelper: Failed to perform operation on PsmKey=%1, HRESULT=%2\r\n
0xb0000148 | _MultiAppSyncOperationHelper: Failed in wait, HRESULT=%1\r\n
0xb0000149 | _MultiPackageSyncOperationHelper: Failed to enumerate PsmKey=%1, HRESULT=%2\r\n
0xb000014a | _MultiPackageSyncOperationHelper: Failed to find package in data store, PkgFullName=1%, HRESULT=%2\r\n
0xb000014b | Failed to suspend and terminate apps, cPsmKeys=%1\r\n
0xb000014c | Could not initialize an extended launch grace period for app %1 with HRESULT %2 -- falling back to normal launch grace\r\n
0xb000014d | App %1 failed to show a window after launch. Will attempt to terminate it now\r\n
0xb000014e | Failed to get a window for an app; assuming that the app's window is not hung, Aumid=%1, HRESULT=%2\r\n
0xb000014f | Failed to query hidden time for visibility debounce for app %1 with error code %2\r\n
0xb0000150 | _StartNewKeyDebounce: Error Result=%2, PsmKey=%1\r\n
0xb0000151 | StartTrackingNewApp failed with %1. The application launch is not protected and the app might potentially get suspended inappropriately\r\n
0xb0000152 | ERROR: Failed to enumerate exemption targets starting from PsmKey=%1\r\n
0xb0000153 | Failed to enumerate existing applications from PSM with error code %1\r\n
0xb0000154 | PsmRegisterApplicationNotification failed for application %1 with status %2.  PLM's cache says that the application's registration is: %3\r\n
0xb0000155 | ERROR: Failed to enumerate force termination targets starting from PsmKey=%1, HRESULT=%2\r\n
0xb0000156 | Application %1 failed to be added in PLM Data Store\r\n
0xb0000157 | Failed to initialize string to send app notification %1 state %2\r\n
0xb0000158 | Failed to initialize string to remove app %1\r\n
0xb0000159 | Failed to add %1 for application %2. The application doesn't have BTC_AUDIO background task capability\r\n
0xb000015a | Failed to initialize CmApi\r\n
0xb000015b | Task completion manager failed to add %1 to its sharing cache with error code %2\r\n
0xb000015c | ClearTerminationTypesForForgottenPackage: Failed to clear termination type for app, Aumid=%1, HRESULT=%2\r\n
0xb000015d | ERROR: Failed to schedule the visibility debounce, PsmKey=%1, HRESULT=%2\r\n
0xb000015e | OnWindowChanged ERROR: Failed to queue thread for Aumid=%1, Hwnd=%2, change=%3, HRESULT=%4\r\n
0xb000015f | ERROR: Failed to schedule deferred visibility timer, PsmKey=%1, HRESULT=%2\r\n
0xb0000160 | WaitOnBiNotifyNewSession HRESULT=%1\r\n
0xb0000161 | RegisterKernelNotifications HRESULT=%1\r\n
0xb0000162 | TCExemptionManager CompleteInitialization HRESULT=%1\r\n
0xb0000163 | PlmActivationManager CompleteInitialization HRESULT=%1\r\n
0xb0000164 | Plm CSDiagnostics CompleteInitialization HRESULT=%1\r\n
0xb0000165 | Plm LogOff/LogOn Registration HRESULT=%1\r\n
0xb00001f9 | BM: Queued evaluate WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fa | BM: Evaluate returned WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fb | BM: TaskActivated WorkItem: %1 Instance: %2\r\n
0xb00001fc | BM: TaskCompleted WorkItem: %1 Instance: %2\r\n
0xb00001fd | BM: TaskCanceled WorkItem: %1 Instance: %2\r\n
0xb00001fe | BM: Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb00001ff | BM: TaskActivating WorkItem: %1 Instance: %2\r\n
0xb0000200 | BM: Enter %1\r\n
0xb0000201 | BM: Exit %1, HR=%2\r\n
0xb0000202 | BM: TerminateHost WorkItem: %1\r\n
0xb0000203 | BM: ResourceSet invalidated for WorkItem: %1 Instance: %2.  This usually means the host has crashed before a ResourceSet could be applied.\r\n
0xb0000204 | BM: OnAcquired ignoring invalid CallbackId (%1).\r\n
0xb0000205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1'; WorkItemId='%2;' CallbackId='%3'.\r\n
0xb0000206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1'.\r\n
0xb0000207 | BM: OnApplicationStateChanged returning State='%2' PsmKey='%1' HR='%3'.\r\n
0xb0000208 | BM: OnAcquired received for CallbackId: %1\r\n
0xb0000209 | BM: OnAcquired request ignored for CallbackId: %1\r\n
0xb000020a | BM: ActivateDeferredWorkItem WorkItem: %1\r\n
0xb000020b | BM: ActivateDeferredWorkItem discarded WorkItem: %1 because of Status: %2\r\n
0xb000020c | BM: Enter %1 WorkItem: %2\r\n
0xb000020d | BM: Enter %1 WorkItem: %2 TaskInstanceId: %3\r\n
0xb000020e | BM: Exit %1\r\n
0xb000020f | BM: Failed to load settings for event %1.\r\n
0xb0000210 | BM: Failed to load settings for event %1 with error %2.\r\n
0xb0000211 | BM: Failed to load policy for CLSID: %1, for EventType %2 with error %3.\r\n
0xb0000212 | BM: Failed to load the policies with error %1.\r\n
0xb0000213 | BM: Evaluate returned WorkItem: %3 EventType: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb0000214 | BM: TaskWallClockActive WorkItem: %1 Instance: %2\r\n
0xb0000215 | BM: TaskWallClockExpired WorkItem: %1 Instance: %2\r\n
0xb0000216 | BM: Policy returned HRESULT: %3 for WorkItem: %2 PsmKey: %1.\r\n
0xb0000217 | BM: Canceling task for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000218 | BM: Ignoring cancelation request (whitelisted) for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000219 | BM: Session(%1) started, session initialization returned %2.\r\n
0xb000021a | BM: Session(%1) ended.\r\n
0xb000021b | BM: Activation ignored due to no Session(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb000021c | BM: Failed to acquire a ResourceSet for WorkItem: %1 with error %2.\r\n
0xb000021d | BM: WorkItem: %1 is being debugged. Setting wallclock limit to 0.\r\n
0xb000021e | BM: EvaluateActivationAction for WorkItem: %1 HRESULT: %2.\r\n
0xb000021f | BM: Skipped Buffering Exempted task with SQMId: %1 PsmKey: %2.\r\n
0xb0000220 | BM: Dropped Exempted task that came before SessionReady with SQMId: %1 PsmKey: %2.\r\n
0xb0000221 | BM: Activation ignored due to no User(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb0000222 | BM: User Logon Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000223 | BM: User Logoff Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000224 | BM: Pending activation discarded for work item (%1).\r\n
0xb0000225 | BM: Flushing ignored EvaluationState: %1 for WorkItem: %2.\r\n
0xb0000226 | BM: Flushing buffered activations.\r\n
0xb0000227 | BM: Global Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb0000228 | BM: A Session object for Session(%1) already exists.\r\n
0xb0000229 | BM: ShellSuspendState changed, oldState: %1 newState: %2\r\n
0xb000022a | BM: DPLKeyState changed, oldState: %1 newState: %2\r\n
0xb000022b | BM: Canceling WorkItem: %1 due to DPL policy.\r\n
0xb000022c | BM: Dropping activation for WorkItem: %1 due to DPL policy.\r\n
0xb000022d | BM: Buffered activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022e | BM: Exempted activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022f | BM: Buffered activation for WorkItem: %1 due to Thermal Throttling policy.\r\n
0xb0000258 | AM: Failed to read activation plugin registry with error code %1.\r\n
0xb0000259 | AM: Failed to CoCreate activation plugin with error code %1 and CLSID %2.\r\n
0xb000025a | AM: Successfully created activation plugin with CLSID %1 from the registry.\r\n
0xb000025b | AM: Failed to register package if needed with error %1.\r\n
0xb000025c | AM: Failed trying to register package by family name async during activation with error %1.\r\n
0xb000025d | AM: Failed trying to wait for the completion of the register package by family async during activation with error %1.\r\n
0xb00002bc | BAM: Added Package: %1 UserSid: %2.\r\n
0xb00002bd | BAM: Removed Package: %1 UserSid: %2.\r\n
0xb00002be | BAM: Added Application: %1 UserSid: %2.\r\n
0xb00002bf | BAM: Removed Application: %1 UserSid: %2.\r\n
0xb00002c0 | BAM: AccessState Changed for Package: %1 OldState: %2 NewState: %3 UserSid: %4.\r\n
0xb00002c1 | BAM: BackgroundExecutionManager::RequestAccessAsync called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c2 | BAM: BackgroundExecutionManager::GetStatus called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c3 | BAM: BackgroundExecutionManager::RemoveAccess called for Application: %1.\r\n
0xb00002c4 | BAM: Sanitizing data for package: %1 HRESULT: %2.\r\n
0xb00002c5 | BAM: ReregisteredPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002c6 | BAM: UnregisterPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002ee | FAM: NotifyTaskInstanceCompleted, TaskID:%1, hr:%2\r\n
0xb00002ef | FAM: NotifyTaskInstanceRunning, TaskID:%1 Timer - %2\r\n
0xb00002f0 | FAM: RegisterForegroundAgentManagerProxy:PID=%1, ConsumerTaskId=%2, Option=%3, hr=%4\r\n
0xb00002f1 | FAM: UiForeground:Memory:%1MB, CPU:%2%%\r\n
0xb00002f2 | FAM: CreateAgentLaunchRequest, TaskID:%1, Queue:%2, hr:%3\r\n
0xb00002f3 | FAM: CancelAgentRequest, TaskID:%1, CancelType=%2, hr:%3\r\n
0xb00002f4 | FAM: AbortAgentRequestsInternal, hr:%1\r\n
0xb00002f5 | FAM: CompleteAgent, TaskID:%1, hr:%2\r\n
0xb00002f6 | FAM: PrioritizeAgentRequest, TaskID:%1, hr:%2\r\n
0xb00002f7 | FAM: OnForegroundAppChanged()-Abort agents\r\n
0xb00002f8 | FAM: OnRelease()\r\n
0xb00002f9 | FAM: NotifyConsumer, Notification:%1, TaskID:%2, hrResult:%3\r\n
0xb00002fa | FAM: AcquireSharedResourceSet, ProductID:%1, ConsumerPid:%2, Pending:%3, hr:%4\r\n
0xb00002fb | FAM: ReleaseResourceSet, #%1, hr:%2\r\n
0xb00002fc | FAM: TimerExpired:TerminateHost[PID=%1]\r\n
0xb00002fd | FAM: AcquireResourceSet, #%1, Mem:%2MB, CPU:%3%%, hr:%4\r\n
0xb00002fe | FAM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000321 | OTM: Read settings. First retry timeout = %1 ms, Second retry timeout = %2 ms, Third retry timeout = %3 ms, Maximum Retry Timeout = %4 ms\r\n
0xb0000322 | OTM: Task instance %2 of product %1 completed\r\n
0xb0000323 | OTM: TaskHost of product %1 has crashed\r\n
0xb0000324 | OTM: TaskHost of product %1 has been completed by PacMan\r\n
0xb0000325 | OTM: Launching OEM boot agents\r\n
0xb0000326 | OTM: Launching boot agents for product %1 failed with error %2\r\n
0xb0000327 | OTM: Launch boot agents for product %1\r\n
0xb0000328 | OTM: Running OnUpdateStarted for product %1\r\n
0xb0000329 | OTM: Restarting boot agents for product %1 after update\r\n
0xb000032a | OTM: Start menu is ready.\r\n
0xb000032b | OTM: Could not launch OEM boot agents. QueueUserWorkItem failed with error %1.\r\n
0xb000032c | OTM: Could not process update notification for OEM application. QueueUserWorkItem failed with error %1.\r\n
0xb000032d | OTM: Could not process update notification for OEM application. ProcessUpdateNotification failed with error %1.\r\n
0xb000032e | OTM: OemTaskManager::NotifyTaskInstanceCompleted failed with error %1.\r\n
0xb000032f | OTM: OemTaskManager::NotifyTaskHostCompleted failed with error %1.\r\n
0xb0000330 | OTM: OemApp::DumpAgents failed with error %1.\r\n
0xb0000331 | OTM: An error occurred. Hr = %1\r\n
0xb0000332 | OTM: No apps with ServiceAgents were found.\r\n
0xb0000333 | OTM: No ServiceAgent task found for product %1.\r\n
0xb0000334 | OTM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb000035d | PLM: Start tracking new app user %1 app %2, contract %3, hr = %4\r\n
0xb000035e | PLM: Application launched %1 in app %2, hr = %3\r\n
0xb000035f | PLM: Application resume %1 in app %2, hr = %3\r\n
0xb0000360 | PLM: Suspend-Terminate(%3) task %1 in app %2\r\n
0xb0000361 | PLM: Suspend-Terminate suspend of task %1 in app %2 exemption %3\r\n
0xb0000362 | PLM: Suspend-Terminate auto terminate(%3) task %1 in app %2\r\n
0xb0000363 | PLM: Suspend-Terminate task %1 in app %2, hr %3\r\n
0xb0000364 | PLM: Halt app %1, hr %2\r\n
0xb0000365 | PLM: Task resume %1 in app %2\r\n
0xb0000366 | PLM: Task cancel %1 in app %2\r\n
0xb0000367 | PLM: Task remove %1 in app %2\r\n
0xb0000368 | PLM: Queue Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000369 | PLM: Queue Activation State Change Notification %1 state %2\r\n
0xb000036a | PLM: Before Activate task %1 for user %2 in app %3, contract %4, hostid %5, hr = %6\r\n
0xb000036b | PLM: After Activate task %1 with result %2, hr = %3\r\n
0xb000036c | PLM: ApplicationLayer=%1 Set Foreground new task %2, prev task %3\r\n
0xb000036d | PLM: Add task %1 to user %2 and app %3, hr = %4\r\n
0xb000036e | PLM: Create app for user %1, %2, new [app(%3) pkg(%4)], hr = %5\r\n
0xb000036f | PLM: Add task %1 to user %2 and app %3, new [app(%4) pkg(%5)], hr = %6\r\n
0xb0000370 | PLM: Remove task %1, was found(%2)\r\n
0xb0000371 | PLM: Remove app if empty from user %1, %2, hr = %3\r\n
0xb0000372 | PLM: Remove pkg if empty from user %1, %2, hr = %3\r\n
0xb0000373 | PLM: Send Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000374 | PLM: Send Activation State Change Notification %1 state %2\r\n
0xb0000376 | PLM: Timer Started duration %1ms, hr %2\r\n
0xb0000377 | PLM: Timer Expired duration %1ms, hr %2\r\n
0xb0000378 | PLM: Abort task %1 reason %2, dump(%3)\r\n
0xb0000379 | PLM: Task rehydrate %1 in app %2 contract %3\r\n
0xb000037a | PLM: Start RPC suspension timer PSMKey=%1 WakeCounters=%2, hr = %3\r\n
0xb000037b | PLM: Cancel RPC suspension timer PSMKey=%1 app state=%2\r\n
0xb000037c | PLM: Terminate application PSMKey=%1 due to expired RPC suspension timeout\r\n
0xb000037d | PLM: Application %1 cannot be terminated due to %2 exemption\r\n
0xb000037e | PLM: Application %1 can be terminated\r\n
0xb000037f | PLM: EvaluateAndTerminateApplication %1 cannot be terminated due to %2\r\n
0xb0000380 | PLM: EvaluateAndTerminateApplication %1, terminate hr = %2\r\n
0xb0000381 | PLM: Terminate debounce app %1 current state %2 ultimate state %3\r\n
0xb0000382 | PLM: Terminate debounce app %1, hr = %2\r\n
0xb0000383 | PLM: Terminate reason was cleared\r\n
0xb0000384 | PLM: Abort app user %1 app %2 reason %3, dump(%4)\r\n
0xb0000385 | PLM: Watson dump NOT generated for user %1 app %2, process count %3\r\n
0xb0000386 | PLM: Watson dump start for user %1 app %2 reason %3 description %4, process %5 (%6)\r\n
0xb0000387 | PLM: Watson dump information for user %1 app %2 product Id %3 title %4 version %5\r\n
0xb0000388 | PLM: Watson dump end for user %1 app %2, hr %3\r\n
0xb0000389 | PLM: Add Watson dump to user %1 app %2 process %3, hr %4\r\n
0xb000038a | PLM: Failed to add Watson process info for process %1 user %2 app %3\r\n
0xb000038b | PLM: Watson dump status changed pids(%1)\r\n
0xb000038c | PLM: Watson dump status changed, add process %1 user %2 app %3\r\n
0xb000038d | PLM: Watson dump status changed, remove process %1 user %2 app %3\r\n
0xb000038e | PLM: Watson dump status changed, unknown process %1 app %2\r\n
0xb000038f | PLM: Watson add/remove(%2) error report task completion to process %1 (signaled %4), hr %3\r\n
0xb0000390 | PLM: Watson in progress for PSMKey %1, waiting...\r\n
0xb0000391 | PLM: Watson in progress finished for PSMKey %1\r\n
0xb0000392 | PLM: Extending RPC suspension timer PSMKey=%1\r\n
0xb0000393 | PLM: Acquire network reference failed CM_RESULT=%1\r\n
0xb0000394 | PLM: Release network reference failed CM_RESULT=%1\r\n
0xb0000395 | PLM: Suspend-Terminate(%2) app %1 exemption %3, hr %4\r\n
0xb0000396 | PLM: Suspend-Terminate task %1 while dehydrating\r\n
0xb0000397 | PLM: Add user %1 sid %2 to data store, hr = %3\r\n
0xb0000398 | PLM: Start launch grace for user %1 app %2, hr = %3\r\n
0xb0000399 | PLM: Set Window Id for user %1 app %2 wnd %3\r\n
0xb000039a | PLM: EvaluateLaunchGraceCompleted for user %1 app %2\r\n
0xb000039b | PLM: Terminating reexisting app due to sihost restart with PSMKey %1, status %2\r\n
0xb000039c | PLM: Terminating preexisting applications on sihost startup\r\n
0xb000039d | PLM: Set Pause On Lock for user %1 app %2 value %3\r\n
0xb000041b | AAM: Initiate activation for user %1 app %2 contract %3 task %4, hr %5\r\n
0xb000041c | AAM: Initiate activation completed for task %2 (expected %1), hr %3\r\n
0xb000041d | AAM: Initialize activation for user %1 app %2 contract %3 lightup(%5), hr %4\r\n
0xb000041e | AAM: Validate activation, hr %1\r\n
0xb000041f | AAM: Verify license for pkg %1, hr %2\r\n
0xb0000420 | AAM: Activate activation task %1 host %2, hr %3\r\n
0xb0000421 | AAM: Activation shim timer expired %1, hr %2\r\n
0xb0000422 | AAM: Initiate Core UI, hr %1\r\n
0xb0000423 | AAM: Release Core UI\r\n
0xb0000424 | AAM: Create Windows AAM, hr %1\r\n
0xb0000425 | AAM: Attempted remediation, hr %1\r\n
0xb0000426 | AAM: Failed while trying to find a remediation handler, hr %1\r\n
0xb0000427 | AAM: Failed while trying to find the package status, hr %1\r\n
0xb0000428 | AAM: Failed while trying to find the package origin, hr %1\r\n
0xb0000429 | AAM: Failed while trying to verify and initialize the activation, hr %1\r\n
0xb000042a | AAM: Failed while trying to check roaming data, hr %1\r\n
0xb000042f | AAM: Broker created plugins %1, expected %2\r\n
0xb0000430 | AAM: Broker initialize, hr %1\r\n
0xb0000431 | AAM: Broker start activate application %1 (%3 args) arg[0] %2 type %4 caller PID %5 (initialization count %6)\r\n
0xb0000432 | AAM: Broker end activate application %1 launched PID %2 task %3, hr %4\r\n
0xb0000433 | AAM: Broker activate task with result for app %1 caller PID %2 caller task %3\r\n
0xb0000434 | AAM: Broker get result for PID %1 task %2 result %3, hr %4\r\n
0xb0000435 | AAM: Broker get task id for process %1 window %2 = task %3, hr %4\r\n
0xb0000436 | AAM: Broker init session manager, hr %1\r\n
0xb0000437 | AAM: Broker release session manager\r\n
0xb0000438 | AAM: Broker add task with result for parent %1, hr %2\r\n
0xb0000439 | AAM: Broker get task with result for parent %1, hr %2\r\n
0xb000043a | AAM: Broker remove task with result for parent %1, hr %2\r\n
0xb000043b | AAM: Broker create completed event for caller PID %1, hr %2\r\n
0xb000043c | AAM: Broker get task with result for child %1, hr %2\r\n
0xb000043d | AAM: Broker parent task completed %1 with child state %2\r\n
0xb000043e | AAM: Broker child task completed %1 with state %2, hr %3\r\n
0xb000043f | AAM: Broker task event signaled for parent %1 child %2 previous state %3, hr %4\r\n
0xb0000440 | AAM: Broker close task %1, hr %2\r\n
0xb0000441 | AAM: Broker activate application %1 arg[%3] %2\r\n
0xb000044c | FM-ARP: ApplyResourceSetType ResourceSetType=%1 User=%2 PSMKey=%3 ResourceSet=%4 HRESULT=%5\r\n
0xb000044d | FM-ARP: ApplyTerminal UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044e | FM-ARP: RemoveInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044f | FM-ARP: ResetInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000450 | FM-ARP: OnRelease UserContext=%1 PsmKey=%2 ReleaseAction=%3 ReleasedCachedResource=%4 ReleaseAppliedResource=%5 HRESULT=%6\r\n
0xb0000451 | FM-ARP: OnAcquired UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000452 | FM-ARP: OnOutOfMemory UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000453 | FM-ARP: ApplyResourceBoost User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000454 | FM-ARP: AcquireResourceSet ResourceSetType=%1 Usercontext=%2 PsmKey=%3 HRESULT=%4\r\n
0xb0000455 | FM-ARP: Apply Cached Resource Set Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000456 | FM-ARP: Clear Cached Resource User=%1 PSMKey=%2\r\n
0xb0000457 | FM-ARP: Fire Cached ResourceCallback User=%1 PSMKey=%2\r\n
0xb00004b0 | FM-CAM: OnApplicationStateChangedEx UserContext=%1 PsmKey=%2 state=%3 HRESULT=%4\r\n
0xb00004b1 | FM-CAM: AcquireForegroundResource UserContext=%1 PsmKey=%2 isPending=%3\r\n
0xb00004b2 | FM-CAM: OnResourceAcquired UserContext=%1 PsmKey=%2\r\n
0xb00004b3 | FM-CAM: OnResourceTimerExpired UserContext=%1 PsmKey=%2\r\n
0xb00004e2 | FM: TaskCompletion New Battery Saver State %1\r\n
0xb00004e3 | FM: TaskCompletion Revoke Exemption PID=%1 AUMID=%2 TC=%3\r\n
0xb00004e4 | FM: TaskCompletion Apply(%3) Exemption PID=%1 TC=%2 HRESULT=%4\r\n
0xb00004e5 | FM-EEP: CheckProcessBackgroundEligibility ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e6 | FM-EEP: ApplyTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e7 | FM-EEP: RevokeTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e8 | FM-EEP: RequestExtendedExecution ProcessId=%1 Reason=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004e9 | FM-EEP: RegisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004ea | FM-EEP: CompleteExtendedExecution ProcessId=%1 fIsResumed=%2 HRESULT=%3\r\n
0xb00004eb | FM-EEP: RevokeSuspensionExtension User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00004ec | FM-ARP: NotifyPendingResourceSetTransition ResourceSetType=%1 ResourceSet=%2 HRESULT=%3\r\n
0xb00004ed | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 fTimerExpiredCallback=%2 HRESULT=%3\r\n
0xb00004ee | FM-EEP: IsApplicationStateBackgroundEligibile User=%1 PsmKey=%2 fResult=%3\r\n
0xb00004ef | FM-EEP: RevokeTaskCompletionExemption AppUserModelId=%1 HRESULT=%2\r\n
0xb00004f0 | FM-EEP: AllowBackgroundExecution User=%1 AppUserModelId=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004f1 | FM-EEP: OnPackageEnergyStateChange PackageFullName=%1 PackageState=%2 HRESULT=%3\r\n
0xb00004f2 | FM-EEP: RegisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f3 | FM-EEP: UnregisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f4 | FM-EEP: UnregisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004f5 | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 TC=%2 isResourcePending =%3 HRESULT=%4\r\n
0xb00004f6 | FM-EEP: Task Completion Denied By EDP Policy ProcessId=%1 TC=%2\r\n
0xb00004f7 | FM-EEP: IsForegroundApplication Application=%1 Result=%2\r\n
0xb0000578 | FM: Registering callback %1 HRESULT=%2\r\n
0xb0000579 | FM: Generate ActivationInstanceID Id=%1\r\n
0xb000057a | FM: +ActivationPrerequisitePhase ActivationInstanceId=%1 UserContext=%2 AUMID=%3 ContractId=%4\r\n
0xb000057b | FM: -ActivationPrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb000057c | FM: +Resume_RehydrationPhase ActivationInstanceId=%1\r\n
0xb000057d | FM: -Resume_RehydrationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000057e | FM: +ResumeActivation ActivationInstanceId=%1 fIsResumed=%2\r\n
0xb000057f | FM: -ResumeActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000580 | FM: +Resume_ActivationPhase ActivationInstanceId=%1\r\n
0xb0000581 | FM: -Resume_ActivationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000582 | FM: +PauseActivation ActivationInstanceId=%1\r\n
0xb0000583 | FM: -PauseActivation HRESULT=%1 PausePending=%2\r\n
0xb0000584 | FM: +CancelActivation ActivationInstanceId=%1\r\n
0xb0000585 | FM: -CancelActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000586 | FM: +AbortActivation ActivationInstanceId=%1 Reason=%2 fGenerateWER=%3\r\n
0xb0000587 | FM: -AbortActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000588 | FM: +GetActivationProcessId ActivationInstanceId=%1\r\n
0xb0000589 | FM: -GetActivationProcessId ActivationInstanceId=%1 PID%2 HRESULT=%3\r\n
0xb000058a | FM: +SetForegroundActivationInstance ActivationInstanceId=%1 Isforeground=%2\r\n
0xb000058b | FM: -SetForegroundActivationInstance ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000058c | FM: SetActivationDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb000058d | FM: OnActivationStateChanged ActivationInstanceId=%1 state=%2 HRESULT=%3\r\n
0xb000058e | FM: OnApplicationStateChanged UserContext=%1 PSMKey=%2 state=%3 HRESULT=%4\r\n
0xb000058f | FM: IsValidActivationProcessId ActivationInstanceID=%1 PID=%2 fValid=%3 HRESULT=%4\r\n
0xb0000590 | FM: GetForegroundProductId fIgnoreLockScreen=%1 ProductID=%2 HRESULT=%3\r\n
0xb0000591 | FM: GetProductIdFromProcessID ProductID=%1 PID=%2 HRESULT=%3\r\n
0xb0000592 | FM: Discarding Application Frozen notification because the application isn't really frozen\r\n
0xb0000593 | FM: Dehydrate Application AUMID=%1 HRESULT=%2\r\n
0xb0000594 | FM: +ResumePrerequisitePhase ActivationInstanceId=%1\r\n
0xb0000595 | FM: -ResumePrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb0000596 | FM: GenerateWatsonReport PID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000597 | FM: SetContinuation ActivationInstanceID=%1\r\n
0xb0000598 | FM: AbandonContinuation ActivationInstanceID=%1\r\n
0xb0000599 | FM: PerformContinuation ActivationInstanceID=%1\r\n
0xb000059a | FM: Shutdown HRESULT=%1\r\n
0xb000059b | FM: +PauseActivation ActivationInstanceId=%1 AUMID=%2 PackageFullName=%3\r\n
0xb000059c | FM: +ActivationBypass ActivationInstanceId=%1\r\n
0xb000059d | FM: -ActivationBypass ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000059e | FM: +PostPausePendingResume ActivationInstanceId=%1\r\n
0xb000059f | FM: -PostPausePendingResume ActivationInstanceId=%1 HRESULT=%2\r\n
0xb00005a0 | FM: SetActivationImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb00005a1 | FM: NotifyWindowAdded TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a2 | FM: NotifyWindowRemoved TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a3 | FTM: Logoff User=%1 HRESULT=%2\r\n
0xb00005a4 | FM: ActivationTimeoutPolicyChanged  TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a5 | FM-EEP: OnConnectedStandbyStateChanged  State=%1\r\n
0xb00005a6 | FM: SendActivationNotification ActivationId=%1 NotificationId=%2\r\n
0xb00005a7 | FM: OnResourceAcquired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a8 | FM: OnResourceTimerExpired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a9 | FM: PostPausePendingActivation ActivationId=%1 HRESULT=%2\r\n
0xb00007d0 | VoIPPolicy: Evaluate Activation Action for PsmKey = %2, WorkItemId = %1, Action = %3, HRESULT = %4\r\n
0xb00007d1 | VoIPPolicy: Task Activated for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d2 | VoIPPolicy: Task Completed for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d3 | VoIPPolicy: Task Canceled for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d4 | VoIPPolicy: Task Aborted for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d5 | VoIPPolicy: Determine and Apply Resources PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d6 | VOIP: NotifyVoipActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d7 | VOIP: LaunchVoipRtcTask called for PID:%1 PSMKey:{%2} with TaskEntryPoint:{%3} and WNFStateName:{%4} HRESULT:%5.\r\n
0xb00007d8 | VOIP: NotifyVoipActivityCompleted called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d9 | VOIP: HoldActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007da | VOIP: UnholdActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007db | VOIP: NotifyIncomingCallDialogDisplayed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dc | VOIP: NotifyIncomingCallDialogDismissed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dd | VOIP: CallActive called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007de | VOIP: AppLaunchVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007df | VOIP: OnVoipActivityCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e0 | VOIP: AppHoldActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e1 | VOIP: AppUnholdActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e2 | VOIP: OnIncomingCallDialogDisplayed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e3 | VOIP: OnIncomingCallDialogDismissed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e4 | VOIP: AppDetermineAndApplyBestResourceSet called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e5 | VOIP: PolicyEvaluateAction called for WorkItemId:{%1} PSMKey:{%2} ActivationAction:%3 HRESULT:%4.\r\n
0xb00007e6 | VOIP: PolicyTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e7 | VOIP: PolicyTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e8 | VOIP: PolicyTaskCanceled called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e9 | VOIP: PolicyTaskAborted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007ea | VOIP: OnForegroundApplicationChanged called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007eb | VOIP: AppOnTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ec | VOIP: AppOnTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ed | VOIP: AppCancelVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ee | VOIP: CancelVoipRtcTask called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb0000c81 | Task: %1 has started\r\n
0xb0000c82 | Task: %1 has paused\r\n
0xb0000c83 | Task: %1 has resumed\r\n
0xb0000c84 | Task: %1 has completed\r\n
0xb0000c85 | EM: +GetTaskInfo()\r\n
0xb0000c86 | EM: -GetTaskInfo(). HRESULT = %1\r\n
0xb0000c87 | EM: GetAppInfo:%1,%2:%3\r\n
0xb0000c88 | EM: ParseBackgroundAbilities - HRESULT=%1\r\n
0xb0000c89 | EM: +ExecManServerHost::CreateProcess\r\n
0xb0000c8a | EM: -ExecManServerHost::CreateProcess. HRESULT=%1\r\n
0xb0000c8b | Sqm::AppPlatSqmAppDataUsage: %1/%2 - TaskID = %3, Type = %4, NewState = %5, ReasonForStateChange = %6, Duration (ms) = %7, PeakMemory (kb) = %8\r\n
0xb0000c8f | Emc::ExecuteCommand: StartTaskCallbackBegin: TaskID = %1\r\n
0xb0000c90 | Emc::ExecuteCommand: StartTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c91 | Emc::ExecuteCommand: PauseTaskCallbackBegin: TaskID = %1\r\n
0xb0000c92 | Emc::ExecuteCommand: PauseTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c93 | Emc::ExecuteCommand: ResumeTaskCallbackBegin: TaskID = %1\r\n
0xb0000c94 | Emc::ExecuteCommand: ResumeTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c95 | Emc::ExecuteCommand: ControlTaskCallbackBegin: TaskID = %1\r\n
0xb0000c96 | Emc::ExecuteCommand: ControlTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c97 | Emc::ExecuteCommand: CancelTaskCallbackBegin: TaskID = %1\r\n
0xb0000c98 | Emc::ExecuteCommand: CancelTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c99 | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackBegin: TaskID = %1\r\n
0xb0000c9a | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c9e | Emc::RegisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, HR = %3\r\n
0xb0000ca8 | Emc::DeregisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, Reason = %3, HR = %4\r\n
0xb0000ca9 | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleBegin: ProductID = %1\r\n
0xb0000caa | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleEnd: ProductID = %1\r\n
0xb0000cab | EM: Skipping terminate process call for %1\r\n
0xb0000cac | EM: Terminating process: PID = %1, ExitCode = %2\r\n
0xb0000ce4 | AimServer::OnAgentRequestInvoked: AgentRequestID %1 was invoked. PID = %2, HR = %3\r\n
0xb0000ce5 | AimServer::ReadSettings: HR = %1\r\n
0xb0000ce6 | AimServer: Detected server for scope %1 terminated (PID = %2)\r\n
0xb0000ce8 | AimServer::HandleEvent: ProductID %1 received PM LifecyleEvent %2. HR Notification = %3, HR = %4\r\n
0xb0000ce9 | BA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cea | BA::RegisterServiceRequest: AlreadyReserved = %1, SR = %2, HR = %3\r\n
0xb0000ceb | BA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cec | BA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000ced | BA::NotifyTaskInstanceCompleted: Terminating Orphaned Host PID = %1\r\n
0xb0000cee | BA::OrphanAgentRequest: AgentRequestID = %1, HR = %2\r\n
0xb0000cef | BA::UnRegisterServiceRequest: Terminating host PID %1\r\n
0xb0000cf0 | BA::UnRegisterServiceRequest: Orphaning host PID %1\r\n
0xb0000cf1 | BA::UnRegisterServiceRequest: Terminating second old orphaned host PID %1\r\n
0xb0000cf2 | BTM::RecvCallback: Timer expired for AgentRequestID %1\r\n
0xb0000cf3 | BTM::LaunchTask: TaskURI = %1 TaskID = %2, PID = %3, HR = %4\r\n
0xb0000cf4 | GBA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cf5 | GBA::RegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf6 | GBA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf7 | GBA::RegisterAgentRequest: AgentRequestID = %1, type = %2, hr = %3\r\n
0xb0000cf8 | GBA: Cancelling low priority %3 agent because high priority %2 needs to run: Resource was dedicated = %1\r\n
0xb0000cf9 | GBA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000cfa | GBA::TryAcquireResourceSet: pending = %1, type = %2, HR = %3\r\n
0xb0000cfb | GBA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfc | BA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfd | BA::NotifyTaskHostCompleted: ProductID = %1, PID = %2\r\n
0xb0000cfe | BA::RegisterAgentRequest: ProductID = %1, AgentRequestID = %2, HR = %3\r\n
0xb0000cff | BA::PdcActivationFailed: ProductID = %1, Reason = %2, NTSTATUS = %3\r\n
0xb0000dac | FTM: AllowBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dad | FTM: Process is using too much memory for BG Execution. PID=%1, MemUsage=%2, RequiredMemUsage=%3\r\n
0xb0000dae | FTM: Removing BG capability from Task ID %1 due to OOM\r\n
0xb0000daf | FTM: Battery Saver State has change. New state = %1\r\n
0xb0000db0 | FTM: Attempted new BG Execution request due to battery state change. TaskID=%1\r\n
0xb0000db1 | FTM: NotifyTaskInstanceCompleted TaskID=%1 HRESULT=%2\r\n
0xb0000db2 | FTM: NotifyTaskInstancePaused TaskID=%1 HRESULT=%2\r\n
0xb0000db3 | FTM: NotifyTaskInstanceRunning TaskID=%1 HRESULT=%2\r\n
0xb0000db4 | FTM: SendTaskStatusChange TaskID=%1 Status=%2 HRESULT=%3\r\n
0xb0000db5 | FTM: NotifyTaskHostCompleted HRESULT=%1\r\n
0xb0000db6 | FTM: Discarding NotifyTaskHostFrozen notification because the host isn't really frozen\r\n
0xb0000db7 | FTM: NotifyTaskHostFrozen PID=%1 HRESULT=%2\r\n
0xb0000db8 | FTM: NotifyTaskHostDehydrated HRESULT=%1\r\n
0xb0000db9 | FTM: Registering callback %1 HRESULT=%2\r\n
0xb0000dba | FTM: New Task %1 is dehydration-suppressing\r\n
0xb0000dbb | FTM: Applying Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbc | FTM: Revoking Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbd | FTM: +LaunchTask TaskURI=%1 LaunchFlags=%2\r\n
0xb0000dbe | FTM: -LaunchTask TaskURI=%1 TaskID=%2 PID=%3 HRESULT=%4\r\n
0xb0000dbf | FTM: ResumeTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc0 | FTM: Removing Foreground Resources from TaskID=%1\r\n
0xb0000dc1 | FTM: SetForegroundTaskInstanceId TaskID=%1 HRESULT=%2\r\n
0xb0000dc2 | FTM: PauseTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc3 | FTM: CancelTask TaskID=%1 Frozen=%2 HRESULT=%3\r\n
0xb0000dc4 | FTM: AbortTask being ignored because the task is completed TaskID=%1\r\n
0xb0000dc5 | FTM: AbortTask TaskID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000dc6 | FTM: SetTaskDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb0000dc7 | FTM: RequestProcessBackgroundExecution type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc8 | FTM: CancelProcessBackgroundExecutionRequest type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc9 | FTM: TaskRunningInBackground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dca | FTM: TaskRunningInForeground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dcb | FTM: Changing activation policy to resume due to BG Execution for ProductID %1\r\n
0xb0000dcc | FTM: OnShutdownCompleted\r\n
0xb0000dcd | FTM: Ignoring expired watchdog for task %1 because it is being debugged.\r\n
0xb0000dce | FTM: Watchdog fired for task %1 while running in background. Pausing Task.\r\n
0xb0000dcf | FTM: Request BG Execution Denied because it wasn't running. TaskID=%1\r\n
0xb0000dd0 | FTM: Request BG Execution Denied because product was forbidden. TaskID=%1\r\n
0xb0000dd1 | FTM: Request BG Execution Denied because task didn't have BG abilities in its manifest. TaskID=%1\r\n
0xb0000dd2 | FTM: Request BG Execution Denied due to lack of resources. TaskID=%1\r\n
0xb0000dd3 | FTM: Request BG Execution Denied because battery policy prevented it. TaskID=%1\r\n
0xb0000dd4 | FTM: RequestBGAccess IsAllowed=%1 TaskID=%2 HRESULT=%3\r\n
0xb0000dd5 | FTM: RemoveBGRequest RequestedRemoval=%1 ActualRemoval=%2 TaskID=%3 HRESULT=%4\r\n
0xb0000dd6 | FTM: ForbidBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dd7 | FTM: IsValidTaskInstancePid TaskID=%1 Pid=%2 fValid=%3 HRESULT=%4\r\n
0xb0000dd8 | FTM: DetermineBestResourceSet for child ProductID=%1 LaunchFlags=%2 ResourceSetType=%3\r\n
0xb0000dd9 | FTM: OnRelease ResourceSet TaskID=%1 ResouceSet=%2 HRESULT=%3\r\n
0xb0000dda | FTM:UITask Call to Acquire network reference failed CM_RESULT=%1\r\n
0xb0000ddb | FTM:UITask Call to Release network reference failed CM_RESULT=%1\r\n
0xb0000ddc | FTM: SetTaskImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb0000ddd | FTM: +RequestProcessBackgroundExecution type=%1 Pid=%2\r\n
0xb0000dde | FTM: +RequestBackgroundExecution type=%1\r\n
0xb0000ddf | FTM: -RequestBackgroundExecution type=%1 HRESULT=%2\r\n
0xb0000de0 | FTM: +RequestBGAccess TaskInstanceId=%1 type=%2\r\n
0xb0000de1 | FTM: Request BG Execution Denied because DPL policy prevented it. TaskID=%1\r\n
0xb0000de2 | FTM: Edp keys locked state (%1)\r\n
0xb0000e42 | VoIP: Foreground state for product %1 has changed. Is in foreground = %2\r\n
0xb0000e43 | VoIP: Canceling communication agent for product %1\r\n
0xb0000e44 | VoIP: Timer expired for keep-alive agent of product %1\r\n
0xb0000e45 | VoIP: Timer expired for incoming call agent of product %1\r\n
0xb0000e46 | VoIP: Launched agent instance with id %2 and URI %1\r\n
0xb0000e47 | VoIP: Canceled agent instance with id %1\r\n
0xb0000e48 | VoIP: Set active call resource set\r\n
0xb0000e49 | VoIP: Set communication agent resource set\r\n
0xb0000e4a | VoIP: Set VoIP Worker resource set\r\n
0xb0000e4b | VoIP: Applied terminal resource set\r\n
0xb0000e4c | VoIP: Last task instance completed. Releasing the task host ...\r\n
0xb0000e4d | VoIP: Launching active call agent instance for product %1\r\n
0xb0000e4e | VoIP: Canceling active call agent for product %1\r\n
0xb0000e4f | VoIP: Putting an active call on hold for product %1\r\n
0xb0000e50 | VoIP: Taking an active call off hold for product %1\r\n
0xb0000e51 | VoIP: Incoming call dialog has been displayed for product %1\r\n
0xb0000e52 | VoIP: Incoming call dialog has been dismissed for product %1\r\n
0xb0000e53 | VoIP: Launch communication agent request received from process %1 for product %2\r\n
0xb0000e54 | VoIP: Read settings. Keep alive timout = %1 ms, Max agent request queue = %2, Incoming call grace period = %3 ms, Incoming call dismissed grace period = %4 ms\r\n
0xb0000e55 | VoIP: Received request to launch agent type %2 for product %1\r\n
0xb0000e56 | VoIP: Task instance %2 of product %1 completed\r\n
0xb0000e57 | VoIP: Processing request to launch agent type %2 for product %1\r\n
0xb0000e58 | VoIP: Added VoIPApp object to map for product %1\r\n
0xb0000e59 | VoIP: Removed VoIPApp object from map for product %1\r\n
0xb0000e5a | VoIP: Getting VoIPApp object from map for product %1\r\n
0xb0000e5b | VoIP: Publishing WNF_DEVP_VOIP_ACTIVE_CALL_STATE_CHANGE failed with status %1\r\n
0xb0000e5c | VoIP: Subscribing to the WNF_WIFI_CONNECTION_STATUS event failed with status %1\r\n
0xb0000e5d | VoIP: Subscribed to WNF_WIFI_CONNECTION_STATUS? %1\r\n
0xb0000e5e | VoIP: WiFi connection status active/dormat? %1 (hConnection = %2)\r\n
0xb0000e5f | VoIP: RtlQueryWnfStateData failed trying to query the value of WNF_WIFI_CONNECTION_STATUS. NTSTATUS = %1\r\n
0xb0000e60 | VoIP: Could not spin up worker for UpdateWiFiStateHelper. HR =%1\r\n
0xb0000e61 | VoIP: In active call? %1\r\n
0xb0000e62 | VoIP: CmUtilSetWiFiActive was not successful. This could be because WiFi disconnected by the time we were notified of the connection.\r\n
0xb0000e63 | VoIP: WiFi connection status is %1.\r\n
0xb0000e64 | VoIP: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000e65 | VoIP: PhoneServiceRestart: HR = %1\r\n
0xb0000e66 | VoIP: PhoneServiceRestart: Product = %1, HR = %2\r\n
0xb0000e67 | VoIP: Launching call query info agent instance for product %1\r\n
0xb0000e68 | VoIP: Canceling call query info agent instance for product %1\r\n
0xb0000e69 | VoIP: Terminating agents due to low memory for product %1\r\n
0xb0000e6a | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2\r\n
0xb0000e6b | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2, fApplied = %3, HR = %4\r\n
0xb0000e6c | VoIP: Set PDC Network Active for product = %1, NTSTATUS = %2\r\n
0xb0000e6d | VoIP: Set PDC Network Inactive for product = %1, NTSTATUS = %2\r\n
0xb0000e6e | VoIP: Renew PDC Network activation failed for product = %1, NTSTATUS = %2\r\n
0xb0000e73 | VoIP: An error occurred. Hr = %1\r\n
0xb00017d4 | %1 - [%2 = %3]\n\r\n
0xb00017d5 | %1 - Parsing config file [%2] file size = %3.  Parse = %4\r\n
0xb00017d6 | %1 - OnTaskModelMessage: Dispatching EM message\r\n
0xb00017d7 | %1 - InitializeTaskHost URI=%2, Page=%3, TaskId=%4\r\n
0xb00017d8 | %1 - Resuming Task from dehydration\r\n
0xb00017d9 | %1 - TaskHandler::GetTaskHandler hr=%2\r\n
0xb00017da | %1 - TaskHost Init\r\n
0xb00017db | %1 - TaskHost Init hr = %2\r\n
0xb00017dc | %1 - Host Dispatcher Exiting hr = %2\r\n
0xb00017dd | %1 - TaskHandlerReady received\r\n
0xb00017de | %1 - StartTask TaskId=%2\r\n
0xb00017df | %1 - PauseTask TaskId=%2\r\n
0xb00017e0 | %1 - ResumeTask TaskId=%2\r\n
0xb00017e1 | %1 - OnTaskHandlerVisible received\r\n
0xb00017e2 | %1 - OnTaskHandlerHidden received\r\n
0xb00017e3 | %1 - BackgroundExecutionCallback TaskId[%2] Command[%3]\r\n
0xb00017e4 | %1 - BackgroundExecutionCallback hr=%2\r\n
0xb00017e5 | %1 - OnHostRunning\r\n
0xb00017e6 | %1 - OnHostRunning. hr = %2\r\n
0xb00017e7 | %1 - Dehydrating. dehydrateGracefully = %2\r\n
0xb00017e8 | %1 - Gracefully dehydrating TaskHost\r\n
0xb00017e9 | %1 - TryDehydrateHost. hr = %2\r\n
0xb00017ea | %1 - DehydrateHost event triggered\r\n
0xb00017eb | %1 - WaitForUnfreeze hr = %2\r\n
0xb00017ec | %1 - ReduceMemoryHostCallback hr = %2\r\n
0xb00017ed | %1 - Graceful tear-down failed\r\n
0xb00017ee | %1 - BeforeHostRunningInBackgroundCallback\r\n
0xb00017ef | %1 - BeforeHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f0 | %1 - AfterHostRunningInBackgroundCallback\r\n
0xb00017f1 | %1 - AfterHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f2 | %1 - Unhandled exception occurred. hr = %2\r\n
0xb00017f3 | %1 - State-Transition (%2)->(%3)\r\n
0xb00017f4 | %1 - EnableProfiling = [%2]\r\n
0xb00017f5 | %1 - Profile Dll = [%2]\r\n
0xb00017f6 | %1 - ProfilerCLSID = [%2]\r\n
0xb00017f7 | %1 - TaskHostHelper::SetProfilerSettings hr = %2\r\n
0xb00017f8 | %1 - File path = %2 : %3\r\n
0xb00017f9 | %1 - Parse Element: %2.\r\n
0xb00017fa | %1 - Parse Element Value = %2 with pwszLocalName = %3.\r\n
0xb00017fb | %1 - Parse HResult = %2\r\n
0xb00017fc | %1 - YUTHost: failed to GAC trusted assembly %2\r\n\r\n
0xb00017fd | %1 - UITaskHandler::Initialize. hr = %2\r\n
0xb00017fe | %1 - UITaskHandler::Disconnect done\r\n
0xb00017ff | %1 - UITaskHandler::GoBackground. hr = %2\r\n
0xb0001800 | %1 - UITaskHandler::GoForeground. hr = %2\r\n
0xb0001801 | %1 - Managed Framework Ready. Handling Pending Event:[%2]\r\n
0xb0001802 | %1 - HandlePendingEvents Start TaskId=%2\r\n
0xb0001803 | %1 - HandlePendingEvents Pause TaskId=%2\r\n
0xb0001804 | %1 - HandlePendingEvents Resume TaskId=%2\r\n
0xb0001805 | %1 - Waiting for Siblings...\r\n
0xb0001806 | %1 - Waiting for Siblings done. hr = %2\r\n
0xb0001807 | %1 - UITaskHandler::OnRuntimeHostReady TaskID:[%2]\r\n
0xb0001808 | %1 - UITaskHandler::OnRuntimeHostReady. Processed pending SystemKeyPress [%2]\r\n
0xb0001809 | %1 - UITaskHandler::OnRuntimeHostReady hr = %2\r\n
0xb000180a | %1 - UITaskHandler::RegistrationComplete hr = %2\r\n
0xb000180b | %1 - UITaskHandler::ConnectionComplete received\r\n
0xb000180c | %1 - UITaskHandler::ConnectionComplete hr = %2\r\n
0xb000180d | %1 - UITaskHandler::ProcessActivationData received, reason=%2\r\n
0xb000180e | %1 - UITaskHandler::ProcessActivationData hr = %2\r\n
0xb000180f | %1 - UITaskHandler::Show received. Direction:[%2]\r\n
0xb0001810 | %1 - Navigation in progress. Queuing up the Show\r\n
0xb0001811 | %1 - UITaskHandler::Show hr = %2\r\n
0xb0001812 | %1 - UITaskHandler::ShowInternal. Direction:[%2:NavigationDirection:]\r\n
0xb0001813 | %1 - UITaskHandler::ShowInternal. hr = %2\r\n
0xb0001814 | %1 - UITaskHandler::Hide received. Direction:[%2]\r\n
0xb0001815 | %1 - Navigation in progress. Cancelling Show and ignoring Hide\r\n
0xb0001816 | %1 - UITaskHandler::Hide hr = %2\r\n
0xb0001817 | %1 - UITaskHandler::NavigateTo received TaskID:[%2]\r\n
0xb0001818 | %1 - UITaskHandler::NavigateTo. hr = %2\r\n
0xb0001819 | %1 - UITaskHandler::NavigationComplete TaskID:[%2]\r\n
0xb000181a | %1 - UITaskHandler::NavigationComplete hr = %2\r\n
0xb000181b | %1 - UITaskHandler::NavigateAway received TaskID:[%2]\r\n
0xb000181c | %1 - Navigation interrupted since Task is closing\r\n
0xb000181d | %1 - Navigation in progress. Queuing up the NavigateAway\r\n
0xb000181e | %1 - UITaskHandler::NavigateAway hr = %2\r\n
0xb000181f | %1 - UITaskHandler::NavigateAwayInternal TaskID:[%2]\r\n
0xb0001820 | %1 - UITaskHandler::NavigateAwayInternal hr = %2\r\n
0xb0001821 | %1 - UITaskHandler::RequestClose called TaskID:[%2]\r\n
0xb0001822 | %1 - UITaskHandler::RequestClose hr = %2\r\n
0xb0001823 | %1 - LaunchSession in progress. Cannot add another callback\r\n
0xb0001824 | %1 - UITaskHandler::LaunchSession hr = %2\r\n
0xb0001825 | %1 - LaunchChildTask in progress. Cannot add another callback\r\n
0xb0001826 | %1 - UITaskHandler::LaunchChildTask hr = %2\r\n
0xb0001827 | %1 - UITaskHandler::SetPauseOnLock[%2] called TaskID:[%3]\r\n
0xb0001828 | %1 - UITaskHandler::SetPauseOnLock hr = %2\r\n
0xb0001829 | %1 - UITaskHandler::Close received TaskID:[%2]\r\n
0xb000182a | %1 - UITaskHandler::Close hr = %2\r\n
0xb000182b | %1 - UITaskHandler::SystemKeyPressed received: [%2]\r\n
0xb000182c | %1 - UITaskHandler::SystemKeyPressed processed\r\n
0xb000182d | %1 - UITaskHandler::SystemKeyPressed pending. Will be processed on RuntimeHost ready\r\n
0xb000182e | %1 - UITaskHandler::LaunchChildTaskComplete received with result %2\r\n
0xb000182f | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001830 | %1 - UITaskHandler::LaunchSessionComplete received with result %2\r\n
0xb0001831 | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001832 | %1 - OrientationChanged NewOrientation=%2\r\n
0xb0001833 | %1 - OrientationChange received before RuntimeHostTask is set\r\n
0xb0001834 | %1 - SetSupportedOrientations. SupportedOrientations:[%2]. hr = %3\r\n
0xb0001835 | %1 - GetSupportedOrientations. SupportedOrientations[%2]. hr = %3\r\n
0xb0001836 | %1 - GetCurrentOrientation. CurrentOrientation[%2]. hr = %3\r\n
0xb0001837 | %1 - UITaskHandler::ReplaceTouchEndpoint hr = %2\r\n
0xb0001838 | %1 - UITaskHandler::ReplaceTextEndpoint hr = %2\r\n
0xb0001839 | %1 - UITaskHandler::Get Task State. StateSize[%2]. hr = %3\r\n
0xb000183a | %1 - UITaskHandler::Set Task State. StateSize[%2]. hr = %3\r\n
0xb000183b | %1 - UITaskHandler::OnObscurityChange[%2]. hr = %3\r\n
0xb000183c | %1 - UITaskHandler::OnLockScreenVisibilityChange[%2]. hr = %3\r\n
0xb000183d | %1 - UITaskHandler::OnSipVisibilityChange[%2]. hr = %3\r\n
0xb000183e | %1 - UITaskHandler::OnShowAnimationComplete\r\n
0xb000183f | %1 - UITaskHandler::Window.Visible property changed [%2]\r\n
0xb0001840 | %1 - FreezeHost event triggered\r\n
0xb0001841 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001842 | %1 - CancelTask TaskId=%2\r\n
0xb0001843 | %1 - OnHostPausing\r\n
0xb0001844 | %1 - OnHostPausing failed with hr = %2\r\n
0xb0001845 | %1 - OnHostPaused\r\n
0xb0001846 | %1 - OnHostPaused failed with hr = %2\r\n
0xb0001847 | %1 - FreezeHost event triggered\r\n
0xb0001848 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001849 | %1 - CancelTask received while executing in background\r\n
0xb000184a | %1 - CancelTask received. Ignoring since this is a valid transition only when running in background\r\n
0xb000184b | %1 - CancelTask hr = %2\r\n
0xb000184c | %1 - TPA entry: %2\\%3%4;\r\n
0xb000184d | %1 - Platform Assemblies List: %2\r\n
0xb000184e | %1 - ParseManifestFile HResult = %2\r\n
0xb000184f | %1 - NotifyError ! Unable to disable NI optimizations\r\n
0xb0001850 | %1 - NotifyError ! Unable to set the debugger wait env variable\r\n
0xb0001851 | %1 - TestTrustedPath: %2\r\n
0xb0001852 | %1 - TestAppPaths: %2\r\n
0xb0001853 | %1 - NotifyError ! Failed to set the test settings\r\n
0xb0001854 | %1 - GetAppPaths failed with hr = %2\r\n
0xb0001855 | %1 - NotifyError ! message = %2, source = %3\r\n
0xb0001856 | %1 - NotifyError ! hr=%2. message = %3\r\n
0xb0001857 | %1 - GetIsoStoreAvailableFreeSpace hr = %2\r\n
0xb0001858 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb0001859 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb000185a | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185b | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185c | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb000185d | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb000185e | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb000185f | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb0001860 | %1 - GetQualifiedMutexName returned:[%2]. AllowedMutexCount:[%3]\r\n\r\n
0xb0001861 | %1 - XcpHost::Start() failed with hr = %2\r\n
0xb0001862 | %1 - Shutting down the SL runtime...\r\n
0xb0001863 | %1 - Calling into XcpHost::Pausing %2\r\n
0xb0001864 | %1 - XcpHost::Pausing %2\r\n
0xb0001865 | %1 - Calling into XcpHost::Pause %2\r\n
0xb0001866 | %1 - XcpHost::Pause %2\r\n
0xb0001867 | %1 - Calling into XcpHost::Resume %2\r\n
0xb0001868 | %1 - XcpHost::Resume %2\r\n
0xb0001869 | %1 - Calling into XcpHost::Resumed %2\r\n
0xb000186a | %1 - XcpHost::Resumed %2\r\n
0xb000186b | %1 - XcpHost::CompleteTask called TaskID:[%2]\r\n
0xb000186c | %1 - CompleteTask called when XcpTask is null. This likely indicates CompleteTask getting called twice\r\n
0xb000186d | %1 - Error in OnApplicationStarted\r\n
0xb000186e | %1 - Error in OnApplicationConstructing\r\n
0xb000186f | %1 - LaunchSession hr = %2\r\n
0xb0001870 | %1 - LaunchChildTask hr = %2\r\n
0xb0001871 | %1 - Raising Task.OnLaunching\r\n
0xb0001872 | %1 - Raised Task.OnLaunching\r\n
0xb0001873 | %1 - Raising Task.OnPause. PauseReason[%2]\r\n
0xb0001874 | %1 - Raised Task.OnPause\r\n
0xb0001875 | %1 - Raising Task.OnResume. IsExecutionContextPreserved[%2]\r\n
0xb0001876 | %1 - Raised Task.OnResume\r\n
0xb0001877 | %1 - Raising Task.OnRunningInBackground\r\n
0xb0001878 | %1 - Raised Task.OnRunningInBackground\r\n
0xb0001879 | %1 - Raising Task.OnCancel\r\n
0xb000187a | %1 - Raised Task.OnCancel\r\n
0xb000187b | %1 - Raising Task.OnHostDehydarting\r\n
0xb000187c | %1 - Raised Task.OnHostDehydarting\r\n
0xb000187d | %1 - Raising Task.OnNavigateTo\r\n
0xb000187e | %1 - Raised Task.OnNavigateTo\r\n
0xb000187f | %1 - Raising Task.OnNavigateAway\r\n
0xb0001880 | %1 - Raised Task.OnNavigateAway\r\n
0xb0001881 | %1 - Raising Task.OnShow\r\n
0xb0001882 | %1 - Raised Task.OnShow\r\n
0xb0001883 | %1 - Raising Task.OnHide\r\n
0xb0001884 | %1 - Raised Task.OnHide\r\n
0xb0001885 | %1 - Raising Task.OnSystemKeyPressed\r\n
0xb0001886 | %1 - Raised Task.OnSystemKeyPressed\r\n
0xb0001887 | %1 - Raising Task.OnChildTaskReturned\r\n
0xb0001888 | %1 - Raised Task.OnChildTaskReturned\r\n
0xb0001889 | %1 - Raising Task.OnObscurityChange\r\n
0xb000188a | %1 - Raised Task.OnObscurityChange\r\n
0xb000188b | %1 - Raising Task.OnLockScreenVisibilityChange\r\n
0xb000188c | %1 - Raised Task.OnLockScreenVisibilityChange\r\n
0xb000188d | %1 - Raising Task.OnClosing\r\n
0xb000188e | %1 - Raised Task.OnClosing\r\n
0xb000188f | %1 - RegisterAppCallbacks hr = %2\r\n
0xb0001890 | %1 - RegisterTaskCallbacks hr = %2\r\n
0xb0001891 | %1 - TaskReadyToShow hr = %2\r\n
0xb0001892 | %1 - RequestCloseTask hr = %2\r\n
0xb0001893 | %1 - CompleteTask hr = %2\r\n
0xb0001894 | %1 - DestroyTaskCallbacks hr = %2\r\n
0xb0001895 | %1 - SetHostErrorCode hrHostError = %2, hr = %3\r\n
0xb0001896 | %1 - LaunchSession[%2] hr = %3\r\n
0xb0001897 | %1 - GetTaskState hr = %2\r\n
0xb0001898 | %1 - SetTaskState hr = %2\r\n
0xb0001899 | %1 - LaunchChildTask[%2] hr = %3\r\n
0xb000189a | %1 - GetTaskAppChromeHandle hr = %2\r\n
0xb000189b | %1 - SetTaskPauseOnLock hr = %2\r\n
0xb000189c | %1 - SetHostObscurity[%2] hr = %3\r\n
0xb000189d | %1 - Entering Modal state\r\n
0xb000189e | %1 - Exiting Modal state hr = %2\r\n
0xb000189f | %1 - NotifyError: message=%2, source=%3\r\n
0xb00018a0 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb00018a1 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb00018a2 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a3 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a4 | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb00018a5 | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb00018a6 | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb00018a7 | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb00018a8 | %1 - Raising Task.OnRefresh\r\n
0xb00018a9 | %1 - Raised Task.OnRefresh\r\n
0xb00018aa | %1 - UITaskHandler::RequestNavigateBack called TaskID:[%2]\r\n
0xb00018ab | %1 - UITaskHandler::RequestNavigateBack hr = %2\r\n
0xb00018ac | %1 - RequestNavigateBack hr = %2\r\n
0xb00018ad | %1 - UITaskHandler::SetFullScreen[%2] called TaskID:[%3]\r\n
0xb00018ae | %1 - UITaskHandler::SetFullScreen hr = %2\r\n
0xb00018af | %1 - SetTaskFullScreen hr = %2\r\n
0xb00018b0 | %1 - Raising Task.OnApplicationLayerChange\r\n
0xb00018b1 | %1 - Raised Task.OnApplicationLayerChange\r\n
0xb00018b2 | %1 - Raising Task.OnRequestOverlayStateChange. State=%2\r\n
0xb00018b3 | %1 - Raised Task.OnRequestOverlayStateChange\r\n
0xb00018b4 | %1 - ApplicationLayerChanged NewApplicationLayer=%2\r\n
0xb00018b5 | %1 - ApplicationLayerChange received before RuntimeHostTask is set\r\n
0xb00018b6 | %1 - AgTaskHandler::LaunchSession hr = %2\r\n
0xb00018b7 | %1 - AgTaskHandler::LaunchChildTask hr = %2\r\n
0xb00018b8 | %1 - GetSessionDisplayName. DisplayName=%2 hr = %3\r\n
0xb00018b9 | %1 - AgTaskHandler::ConnectionComplete received\r\n
0xb00018ba | %1 - AgTaskHandler::ConnectionComplete hr = %2\r\n
0xb00018bb | %1 - UITaskHandler::OnNavigationBarVisibilityChange[%2]. hr = %3\r\n
0xb00018bc | %1 - Raising Task.OnModernActivation\r\n
0xb00018bd | %1 - Raised Task.OnModernActivation\r\n
0xb00018be | %1 - UITaskHandler::LaunchModernChooser hr = %2\r\n
0xb00018bf | %1 - LaunchChildTask hr = %2\r\n
0xb00018c0 | %1 - LaunchModernChooser[%2] hr = %3\r\n
0xb00018c1 | %1 - TaskFirstPresentCompleted = %2\r\n
0xb00018c2 | %1 - UITaskHandler::FirstPresentCompleted called TaskID:[%2]\r\n
0xb00018c3 | %1 - UITaskHandler::FirstPresentCompleted hr = %2\r\n
0xb0001fa4 | AgHost - FrameworkView::Initialize HRESULT=%1\r\n
0xb0001fa5 | AgHost - FrameworkView::SetWindow HRESULT=%1\r\n
0xb0001fa6 | AgHost - FrameworkView::Load HRESULT=%1\r\n
0xb0001fa7 | AgHost - FrameworkView::Run HRESULT=%1\r\n
0xb0001fa8 | AgHost - FrameworkView::Uninitialize HRESULT=%1\r\n
0xb0001fa9 | AgHost - FrameworkView::OnActivated PreviousExecutionState=%1 ActivationKind=%2 HRESULT=%3\r\n
0xb0001faa | AgHost - FrameworkView::OnExiting HRESULT=%1\r\n
0xb0001fab | AgHost - FrameworkView::OnResuming HRESULT=%1\r\n
0xb0001fac | AgHost - FrameworkView::OnSuspending HRESULT=%1\r\n
0xb0001fae | AgHostSvcs - EmCancelTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001faf | AgHostSvcs - EmCreateTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb0 | AgHostSvcs - EmExitTaskHost HRESULT=%1\r\n
0xb0001fb1 | AgHostSvcs - EmPauseTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb2 | AgHostSvcs - EmResumeTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb3 | AgHostSvcs - EmSetTaskInstanceApplicationUri TaskID=%1 ApplicationUri=%2 HRESULT=%3\r\n
0xb0001fb4 | AgHostSvcs - EmSetTaskInstanceArguments TaskID=%1 HRESULT=%2\r\n
0xb0001fb5 | AgHostSvcs - EmSetTaskInstanceBackgroundTaskId TaskID=%1 BackgroundTaskID=%2 HRESULT=%3\r\n
0xb0001fb6 | AgHostSvcs - EmSetTaskInstanceNavigationPage TaskID=%1 NavigationPage=%2 HRESULT=%3\r\n
0xb0001fb7 | AgHostSvcs - EmStartTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb8 | AgHostSvcs - TaskCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fb9 | AgHostSvcs - TaskPaused TaskID=%1 HRESULT=%2\r\n
0xb0001fba | AgHostSvcs - TaskRunning TaskID=%1 HRESULT=%2\r\n
0xb0001fbb | AgHostSvcs - TaskRunningInBackground TaskID=%1 HRESULT=%2\r\n
0xb0001fbc | AgHostSvcs - TaskRunningInForeground TaskID=%1 HRESULT=%2\r\n
0xb0001fbd | AgHostSvcs - EmWaitForTaskInstanceCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fbe | AgHostSvcs - OnModernContractActivation TaskID=%1 HRESULT=%2\r\n
0xb0002008 | EEC: GetExtendedExecutionBroker ProcessId=%1 HRESULT=%2\r\n
0xb0002009 | EEC: RegisterRevokedHandler ProcessId=%1 HRESULT=%2\r\n
0xb000200a | EEC: RequestExtendedExecution ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200b | EEC: ExtensionRevokedCallback ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200c | EEC: CompleteExtendedExecution ProcessId=%1 HRESULT=%2\r\n
0xb000206c | ODB: LaunchTask - UserSid: %1 SessionId: %2 PackageFullName: %3 EntryPoint: %4 WorkItemId: %5 HRESULT: %6.\r\n
0xb000206d | ODB: CancelTask - UserSid: %1 SessionId: %2 WorkItemId: %3 RudeTerminate: %4 CancellationReason: %5 HRESULT: %6.\r\n
0xb000206e | ODB: BeforeTaskActivated - WorkItemId: %1 PsmKey: %2 HostJobType: %3 HRESULT: %4.\r\n
0xb000206f | ODB: TaskActivated - WorkItemId: %1 TaskInstanceId: %2 PsmKey: %3 HRESULT: %4.\r\n
0xb0002070 | ODB: TaskCompleted - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002071 | ODB: TaskCanceled - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002072 | ODB: Timeout in WaitForWnfStateQuiescentTimeout.\r\n
0xb0002073 | ODB: CancelBackgroundTaskWithWnf WorkItemId: %1.\r\n
0xb0002710 | %1\r\n
0xb0002711 | %1: %2\r\n
0xb0002712 | *** ExecFailFast ***   %1\r\n
0xb000271a | PreInstallTaskPolicy: Activate task for User = %1 HRESULT = %2\r\n
0xb000271b | PreInstallTaskPolicy: BiActivate WorkItemId = %1 for user = %2, PackageFullName = %3, EntryPoint = %4, HRESULT = %5\r\n
0xb0010205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1' WorkItemId='%2;' CallbackId='%3' HostId='%5' ResourceSetId='%6'.\r\n
0xb0010206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1' HostId='%3' ResourceSetId='%4'.\r\n
0xd0000001 | Resumed\r\n
0xd0000002 | Quiescing\r\n
0xd0000003 | Quiesced\r\n
0xd0000004 | Frozen\r\n
0xd0000005 | Dehydrated\r\n
0xd0000006 | Terminated\r\n
0xd0000007 | Resumed\r\n
0xd0000008 | Suspending\r\n
0xd0000009 | Suspended\r\n
0xd000000a | Terminated\r\n
0xd000000b | NotBackground\r\n
0xd000000c | MixedHost\r\n
0xd000000d | PureHost\r\n
0xd000000e | SystemHost\r\n
0xd000000f | InvalidType\r\n
0xd0000010 | Permitted\r\n
0xd0000011 | Buffered\r\n
0xd0000012 | Dropped\r\n
0xd0000013 | InvalidType\r\n
0xd0000014 | Invalid\r\n
0xd0000015 | ForegroundApp\r\n
0xd0000016 | Cbe\r\n
0xd0000017 | ForegroundAgent\r\n
0xd0000018 | GbaPeriodic\r\n
0xd0000019 | GbaIdle\r\n
0xd000001a | BackgroundAudio\r\n
0xd000001b | BackgroundWorker\r\n
0xd000001c | Voip\r\n
0xd000001d | Oem\r\n
0xd000001e | Invalid\r\n
0xd000001f | Started\r\n
0xd0000020 | Paused\r\n
0xd0000021 | Resumed\r\n
0xd0000022 | MovedToBackground\r\n
0xd0000023 | RunUnderLock\r\n
0xd0000024 | Invalid\r\n
0xd0000025 | OK\r\n
0xd0000026 | Abort\r\n
0xd0000027 | Unexpected\r\n
0xd0000028 | ExceededRuntime\r\n
0xd0000029 | ResourcesSeized\r\n
0xd000002a | Paused\r\n
0xd000002b | Resumed\r\n
0xd000002c | ScreenLock\r\n
0xd000002d | ScreenUnlocked\r\n
0xd000002e | MovedToBackground\r\n
0xd000002f | CbeExitTimeout\r\n
0xd0000030 | CbeExitBatterySaver\r\n
0xd0000031 | CbeExitParallelAgentPolicy\r\n
0xd0000032 | CbeExitResourcesUnavailable\r\n
0xd0000033 | CbeExitControlPanel\r\n
0xd0000034 | CbeExitBandwidthSavings\r\n
0xd0000035 | HeadlessHost\r\n
0xd0000036 | TaskHost\r\n
0xd0000037 | XcpHost\r\n
0xd0000038 | TaskHostSvcs\r\n
0xd0000039 | TaskHostUnitTests\r\n
0xd000003a | HOST_CREATED\r\n
0xd000003b | HOST_INITIALIZED\r\n
0xd000003c | HOST_RUNNING\r\n
0xd000003d | STARTING_TASK\r\n
0xd000003e | REHYDRATING_TASK\r\n
0xd000003f | HOST_READY\r\n
0xd0000040 | HOST_PAUSING\r\n
0xd0000041 | PAUSING_TASK\r\n
0xd0000042 | PAUSED_TASK\r\n
0xd0000043 | HOST_PAUSED\r\n
0xd0000044 | RESUMING_TASK\r\n
0xd0000045 | HOST_GOING_IN_BACKGROUND\r\n
0xd0000046 | TASK_GOING_IN_BACKGROUND\r\n
0xd0000047 | HOST_IN_BACKGROUND\r\n
0xd0000048 | TASK_GOING_IN_FOREGROUND\r\n
0xd0000049 | GRACEFULLY_DEHYDRATING_HOST\r\n
0xd000004a | HOST_VISIBLE\r\n
0xd000004b | HOST_HIDDEN\r\n
0xd000004c | HOST_FROZEN\r\n
0xd000004d | HOST_THAWED\r\n
0xd000004e | HOST_EXITING\r\n
0xd000004f | HOST_ERROR\r\n
0xd0000050 | Direction_Forward\r\n
0xd0000051 | Direction_Backward\r\n
0xd0000052 | Direction_ForceSize\r\n
0xd0000053 | Resumed\r\n
0xd0000054 | Pausing\r\n
0xd0000055 | Paused\r\n
0xd0000056 | Dehydrated\r\n
0xd0000057 | Completed\r\n
0xd0000058 | none\r\n
0xd0000059 | launch\r\n
0xd000005a | debug\r\n
0xd000005b | task completion\r\n
0xd000005c | dependency\r\n
0xd000005d | multi-view\r\n
0xd000005e | Waiting\r\n
0xd000005f | CompletedWithResult\r\n
0xd0000060 | CompletedWithNoResult\r\n
0xd0000061 | Foreground\r\n
0xd0000062 | Lock\r\n
0xd0000063 | Overlay\r\n
0xd0000064 | ModernForeground\r\n
0xd0000065 | Pausing\r\n
0xd0000066 | PausingLowPri\r\n
0xd0000067 | Paused\r\n
0xd0000068 | PausedHighPri\r\n
0xd0000069 | PausedDNK\r\n
0xd000006a | Frozen\r\n
0xd000006b | FrozenHighPri\r\n
0xd000006c | FrozenDNK\r\n
0xd000006d | FrozenDNCS\r\n
0xd000006e | LockScreen\r\n
0xd000006f | Overlay\r\n
0xd0000070 | 11\r\n
0xd0000071 | CalendarAsChild\r\n
0xd0000072 | VideoTranscode\r\n
0xd0000073 | CBE\r\n
0xd0000074 | GenericExtendedExecution\r\n
0xd0000075 | ModernForegroundExtended\r\n
0xd0000076 | TaskCompletionHighPriority\r\n
0xd0000077 | ModernForegroundLarge\r\n
0xd0000078 | ShellCustom1\r\n
0xd0000079 | ShellCustom2\r\n
0xd000007a | ShellCustom3\r\n
0xd000007b | DebugModeForeground\r\n
0xd000007c | ComponentTarget\r\n
0xd000007d | Invalid\r\n
0xd000007e | Unevaluated\r\n
0xd000007f | EvaluationPending\r\n
0xd0000080 | Evaluated\r\n

### 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x10000006 | ExecMan\r\n
0x10000009 | TaskHost\r\n
0x1000000d | Sqm\r\n
0x1000000f | Lifetime Manager\r\n
0x10000010 | ForegroundManager\r\n
0x10000011 | Background Manager\r\n
0x10000012 | Production Circular\r\n
0x10000013 | Production Critical\r\n
0x10000014 | SelfHost Circular\r\n
0x10000015 | SelfHost Critical\r\n
0x10000016 | DevPlat Circular\r\n
0x10000017 | VOIP\r\n
0x1000001b | Activation Manager\r\n
0x1000001c | AgHost\r\n
0x10000020 | Telemetry\r\n
0x10000021 | ExtendedExecutionClient\r\n
0x10000022 | OnDemandBroker\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000007 | Resume\r\n
0x30000008 | Suspend\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-AppModelExecEvents\r\n
0xb0000064 | DepMgr: Removed suspension group from the graph, PsmKey=%1\r\n
0xb0000065 | Not set app %1 into halted state because it should wait for other apps in the package halted first\r\n
0xb0000066 | Not set app %1 into halted state because other app in the package have not finished quiescing\r\n
0xb0000067 | Not terminate app %1, because target app %2 state = %3\r\n
0xb0000068 | Updated current dependency graph (Removal : %1) with Source %2 and Target %3 for type %4 in return %5\r\n
0xb0000069 | Default time for %1 overridden to %2 ms\r\n
0xb000006a | Creating hang report\r\n
0xb000006b | Window %1 is hung in foreground\r\n
0xb000006c | Window %1 is no longer hung in foreground\r\n
0xb000006d | Waiting for WER reporting to finish on app %1\r\n
0xb000006e | Hang reporting finished on app %1.  App termination status: %2\r\n
0xb000006f | Hung reporting finished on window %1 with result %2\r\n
0xb0000070 | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb0000071 | _SubmitActivationHangWerReport(stop): Aumid=%1, result=%2\r\n
0xb0000072 | _UnregisterForStateChanges: fPackageLevel=%1, HRESULT is %2. Cookie is %3\r\n
0xb0000073 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000074 | Canceled launch grace timer, PsmKey=%1\r\n
0xb0000075 | _InitializeLaunchGraceContext: Aumid=%1, fExtendedLaunch=%2, fEventExists=%3\r\n
0xb0000076 | App %1 successfully launched and its launch grace period expired: removing suspend exemption\r\n
0xb0000077 | Forcefully terminating app, Aumid=%1 flags=%2, reason=%3\r\n
0xb0000078 | CheckTerminationBeforeSwitch: Should terminate: %1, Aumid=%2, HRESULT=%3, reason=%4, fIsMisbehaving=%5\r\n
0xb0000079 | Termination requested for %1 - flags %2\r\n
0xb000007a | Failing TerminateApp due to pending task completions: %1\r\n
0xb000007b | Terminating %1 immediately\r\n
0xb000007c | Uninstalling background work items for %1\r\n
0xb000007d | Termination of %1 scheduled for %2 ms in future\r\n
0xb000007e | Sent window message to the default immersive browser with HRESULT %1\r\n
0xb000007f | Attempting to terminate app %1 prior to new app launch due to pending termination\r\n
0xb0000080 | EvaluateAndTerminatePid: PID: %1. HRESULT: %2. Package State: %3\r\n
0xb0000081 | Exempting application %1 from suspend while it is being launched\r\n
0xb0000082 | Exemption manager %1 is requesting a higher minimum priority %2 for %3\r\n
0xb0000083 | Debug mode is enabled for %1, so it will run at %2 priority\r\n
0xb0000084 | Handling logoff, %1 will run at %2 priority\r\n
0xb0000085 | Throttling has been disabled, so %1 will run at %2 priority\r\n
0xb0000086 | Suspend denied due to new key debounce, PsmKey=%1\r\n
0xb0000087 | Suspend denied due to debug mode, PsmKey=%1\r\n
0xb0000088 | Not suspending application %1 due to exemption %2\r\n
0xb0000089 | _EvaluateAndSuspendApplication: PsmKey=%1, fIsSuspendAllowed=%2, HRESULT=%3\r\n
0xb000008a | _ReevaluatePolicy: Ignoring debug mode app, PsmKey=%1\r\n
0xb000008b | ManagePreExistingApps(start)\r\n
0xb000008c | ManagePreExistingApps: PsmKey=%1, Aumid=%2, hr=%3\r\n
0xb000008d | ManagePreExistingApps(stop)\r\n
0xb000008e | RequestSuspendTimeout called for application %1 and timeout %2\r\n
0xb000008f | Debug mode enabled, PkgFamilyName=%1\r\n
0xb0000090 | Debug mode disabled, PkgFamilyName=%1\r\n
0xb0000091 | Set Package %1, Timeout to %2\r\n
0xb0000092 | ResumeDebugModePackage(start): package=%1\r\n
0xb0000093 | ResumeDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000094 | SuspendDebugModePackage(start): package=%1\r\n
0xb0000095 | SuspendDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000096 | MultiAppSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000097 | MultiAppSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb0000098 | MultiPackageSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000099 | MultiPackageSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009a | MultiPackageSuspendAndPendTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb000009b | MultiPackageSuspendAndPendTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009c | TerminateSync(start): PsmKey=%1, type=%2, reason=%3\r\n
0xb000009d | TerminateSync(stop): PsmKey=%1, hrLogReason=%2, hrTermination=%3\r\n
0xb000009e | TerminatePackageSync(start): Package=%1, type=%2, reason=%3\r\n
0xb000009f | TerminatePackageSync(stop): Package=%1, fPlmKnowsPackage=%2, HRESULT=%3\r\n
0xb00000a0 | _TerminateAllSuspendedApplications(start)\r\n
0xb00000a1 | _TerminateAllSuspendedApplications(stop): HRESULT=%1\r\n
0xb00000a2 | Application %1 is blocking Connected Standby\r\n
0xb00000a3 | Exiting Connected Standby\r\n
0xb00000a4 | All packages have been suspended or terminated. Notify PDC. Call to PdcNotificationClientAcknowledge() returned %1\r\n
0xb00000a5 | Kernel State Change Callback: There were %1 PIDs present in the callback data\r\n
0xb00000a6 | Kernel State Change Callback: The state source was %1\r\n
0xb00000a7 | PDC_CONTROL_ABORT: PdcNotificationClientAcknowledge(STATUS_SUCCESS) returned %1\r\n
0xb00000a8 | Not terminating application %1 in _EvaluateAndTerminateApplication because it contains a running IImmersiveApplication\r\n
0xb00000a9 | Not terminating application %1 in _EvaluateAndTerminateApplication because it is a long running app\r\n
0xb00000aa | Not terminating application %1 in _EvaluateAndTerminateApplication due to pending task completion\r\n
0xb00000ab | Not terminating application %1 in _EvaluateAndTerminateApplication due to Launch Grace\r\n
0xb00000ac | Not terminating application %1 in _EvaluateAndTerminateApplication due to debug mode\r\n
0xb00000ad | Not terminating application %1 in _EvaluateAndTerminateApplication due to application had already been terminated\r\n
0xb00000ae | _EvaluateAndTerminateApplication: Skipping child suspension group, PsmKey=%1\r\n
0xb00000af | An empty application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b0 | Parent allowed suspension for child app, childPsmKey=%1\r\n
0xb00000b1 | GroupChildWithParent: ChildPsmKey=%1, HRESULT=%2\r\n
0xb00000b2 | Call a command line '%1' to notify default browser with result %2\r\n
0xb00000b3 | Read executable path from registry with result %1\r\n
0xb00000b4 | Application %1 was added to PLM Data Store and registering for PSM notification\r\n
0xb00000b5 | Resume the PPLE app %1 when receiving the PSM new key notification\r\n
0xb00000b6 | An orphaned prereq application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b7 | Not terminating dependent application %1 in _EvaluateAndTerminateDependentApplication due other dependency applications\r\n
0xb00000b8 | _EvaluateAndTerminateSourceApplication: Aumid=%1, exemption=%2\r\n
0xb00000b9 | An force termination exemption Application was detected. Setting pending termination for application %1\r\n
0xb00000ba | StateMgr: State queued, PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000bb | StateMgr: OnApplicationStarted set to active, PsmKey=%1\r\n
0xb00000bc | StateMgr: OnApplicationStarted finished, PsmKey=%1, HRESULT=%2\r\n
0xb00000bd | StateMgr: App's current state has changed, PsmKey=%1, state=%2\r\n
0xb00000be | StateMgr: OnApplicationTerminated(start), PsmKey=%1\r\n
0xb00000bf | StateMgr: Application terminated signaled, PsmKey=%1\r\n
0xb00000c0 | StateMgr: OnApplicationTerminated(stop), PsmKey=%1\r\n
0xb00000c1 | StateMgr: GetTerminateSyncData, PsmKey=%1, hr=%2\r\n
0xb00000c2 | StateMgr: _ProcessStateQueue(start): PsmKey=%1, state=%2\r\n
0xb00000c3 | StateMgr: _ProcessStateQueue(stop): PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000c4 | StateMgr: Queue's pause state has changed to %2, PsmKey=%1\r\n
0xb00000c5 | StateMgr: App's committed state has changed, PsmKey=%1, state=%2\r\n
0xb00000c6 | Enabling debug mode on package %1\r\n
0xb00000c7 | Disabling debug mode on package %1\r\n
0xb00000c8 | Suspending package %1 via debug API. HRESULT: %2\r\n
0xb00000c9 | Resuming package %1 via debug API. HRESULT: %2\r\n
0xb00000ca | Terminating package %1 via debug API. HRESULT: %2\r\n
0xb00000cb | Default time for %1 overridden to %2 ms\r\n
0xb00000cc | ReportActivationHangSync: Halt application Aumid=%1, result=%2\r\n
0xb00000cd | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb00000ce | _SubmitActivationHangWerReport(stop): Aumid=%1 canceled(%2) result=%3\r\n
0xb00000cf | PLM doesn't swap out application %1 due to its swap state %2\r\n
0xb00000d0 | PLM termination policy started on background thread because application %1 failed to outswap\r\n
0xb00000d1 | PLM termination policy finished. Outswapping returned status %1\r\n
0xb00000d2 | PLM memory policy will be aggressive because this is a disconnected session\r\n
0xb00000d3 | PLM termination policy start\r\n
0xb00000d4 | PLM termination policy stop\r\n
0xb00000d5 | PLM termination policy triggered by in use memory of %1 MiB\r\n
0xb00000d6 | PLM termination policy triggered by commit charge of %1 MiB\r\n
0xb00000d7 | MemoryPolicyWatcherTerminateCommitCharge\r\n
0xb00000d8 | PLM empty policy triggered by in use memory of %1 MB\r\n
0xb00000d9 | PLM memory policy does not allow termination of application %1 for reason %2\r\n
0xb00000da | PLM memory policy allows termination of application %1\r\n
0xb00000db | Application %1 was hidden %2 seconds ago\r\n
0xb00000dc | Application %1 is the clipboard owner\r\n
0xb00000dd | PLM empty policy start\r\n
0xb00000de | PLM empty policy ignoring application %1 with error code %2\r\n
0xb00000df | PLM empty policy finished after emptying %1 MiB\r\n
0xb00000e0 | PLM termination policy enumerated %1 applications\r\n
0xb00000e1 | PLM memory policy chose application %1 as its termination candidate, over old candidate application %2\r\n
0xb00000e2 | PLM memory policy will terminate application %1 with memory size %2 MiB and score %3\r\n
0xb00000e3 | PLM memory policy received MemWatcher event\r\n
0xb00000e4 | PLM memory policy received MemWatcher event\r\n
0xb00000e5 | Package exemption manager denied suspend for %1.  Ref counts are LAUNCH=%2, PSMREG=%3, PSMPENDING=%4\r\n
0xb00000e6 | Package Exemption Manager: ReferenceAdded:%1, %2 ref to application %3. The ref counts are now LAUNCH=%4, PSMREG=%5, and PSMREGPENDING=%6\r\n
0xb00000e7 | Package %1 added to the package data store\r\n
0xb00000e8 | Resetting priority to unpause the suspension group, PsmKey=%1\r\n
0xb00000e9 | Changed the priority of %1 to %2\r\n
0xb00000ea | AllowServiceOfPackages(start): cPackages=%1, fNotifyBi=%2\r\n
0xb00000eb | AllowServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ec | FinishedServiceOfPackages(start): cPackages=%1\r\n
0xb00000ed | FinishedServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ee | AllowUninstallOfPackage(start): package=%1\r\n
0xb00000ef | AllowUninstallOfPackage(stop): package=%1, HRESULT=%2\r\n
0xb00000f0 | Forcefully terminating misbehaving app %1 due to activation failure %2\r\n
0xb00000f1 | App %1: Change = %2\r\n
0xb00000f2 | PsmKey %1 has state %2\r\n
0xb00000f3 | Changing app state through BI, PsmKey=%1, state=%2 terminate action=%3\r\n
0xb00000f4 | Changing the package state of %1 through BI to %2\r\n
0xb00000f5 | OnAfterQuiescing: Quiesce began for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f6 | _CompleteQuiesceHelper: Queued termination for timed-out PsmKey %1\r\n
0xb00000f7 | Quiesce completed for PsmKey=%1, reason=%2, suspendTrigger=%3\r\n
0xb00000f8 | Suspend trigger updated for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f9 | ExtendQuiesceTimeout: PsmKey=%1, request=%2 ms, HRESULT=%3\r\n
0xb00000fa | _CompleteQuiesceHelper: Ignore timed-out PsmKey %1 as is being debugged\r\n
0xb00000fb | ResumeHelper: Application resume(start), PsmKey=%1, reason=%2\r\n
0xb00000fc | ResumeHelper: Application resume(stop), PsmKey=%1, reason=%2, HRESULT=%3\r\n
0xb00000fd | Resume reason updated for PsmKey=%1, reason=%2\r\n
0xb00000fe | RPC 0->1 transition detected for %1\r\n
0xb00000ff | RPC exemption was granted for application %1. KernelRequest Value: %2. Runaway RPC: %3.  RPC Debounce %4\r\n
0xb0000100 | RPC debounce received for package %1\r\n
0xb0000101 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000102 | Application %1 termination is blocked. PreserverProcessRequest = %2, TaskCompletionCategory = %3\r\n
0xb0000103 | PdcSystem activation (Activate = %1). Result = %2\r\n
0xb0000104 | NetworkAudio entries: %1, IsNetworkReferenced: %2\r\n
0xb0000105 | App %1 is Sharing\r\n
0xb0000106 | Share %1 has started in app %2\r\n
0xb0000107 | Share %1 in app %2 has stopped\r\n
0xb0000108 | Queued termination reason updated for PsmKey=%1, reason=%2\r\n
0xb0000109 | ClearTerminationTypesForForgottenPackage(start): PkgFamilyName=%1\r\n
0xb000010a | Cleared termination type for forgotten app, Aumid=%1, HRESULT=%2\r\n
0xb000010b | ClearTerminationTypesForForgottenPackage(stop): PkgFamilyName=%1, HRESULT=%2\r\n
0xb000010c | Writing to termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010d | Reading termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010e | _ExtendForResourceStarvation: PsmKey=%1, TimerType=%2, newRelativeExpirationTimeMs=%3, ElapsedMs=%4, CpuRunningMs=%5, CpuReadyMs=%6, IoNormalMs=%7\r\n
0xb000010f | Foreground resume delay %1 milliseconds\r\n
0xb0000110 | Suspend allowed for %1 - Session not active\r\n
0xb0000111 | Suspend denied due to a visible window or visibility debounce, PsmKey=%1\r\n
0xb0000112 | Suspend denied for %1 - UserRequest non-zero\r\n
0xb0000113 | Suspend denied for %1- failure %2\r\n
0xb0000114 | OnWindowChanged: Aumid=%1, Hwnd=%2, change=%3, fDeferredVisibility=%4, HRESULT=%5\r\n
0xb0000115 | Starting Session Idle Debounce\r\n
0xb0000116 | Session is active\r\n
0xb0000117 | Session is idle\r\n
0xb0000118 | PlmGetPackageFullNameFromAppId, Aumid=%1, HRESULT=%2\r\n
0xb0000119 | Session idle state change -- calling _ReevaluatePolicy\r\n
0xb000011a | RegisterForActivationStateChanges: Act:%1 App:%2 HRESULT is %3. Cookie is %4\r\n
0xb000011b | UnregisterForActivationStateChanges: Cookie is %1\r\n
0xb000011c | Can Auto Terminate app %1 %2\r\n
0xb000011d | TerminateApplicationBeforeActivation(start): Aumid=%1\r\n
0xb000011e | TerminateApplicationBeforeActivation: wait for terminate, Aumid=%1, HRESULT=%2\r\n
0xb000011f | TerminateApplicationBeforeActivation(stop): Aumid=%1, reason=%2, HRESULT=%3\r\n
0xb0000120 | s_SuspendPackagesAtLogOff(start)\r\n
0xb0000121 | s_SuspendPackagesAtLogOff(stop): HRESULT=%1\r\n
0xb0000122 | StateMgr: OnApplicationStarted still halted, PsmKey=%1\r\n
0xb0000123 | Added Task Completion under %1 for application %2\r\n
0xb0000124 | Removed Task Completion under %1 for application %2\r\n
0xb0000125 | Illegal state change happened to App: %1\r\n
0xb0000126 | EnableDebugMode failed: %1\r\n
0xb0000127 | DisableDebugMode: RoDisableDebuggingForPackage failed with result %1\r\n
0xb0000128 | DisableDebugMode: OnDebugModeDisabled failed with result %1\r\n
0xb0000129 | DisableDebugMode: Enabling activation timeout failed with result %1\r\n
0xb000012a | DisableDebugMode failed: %1\r\n
0xb000012b | Couldn't open process: %1\r\n
0xb000012c | PLM failed to process a hang for window %1 with error code %2\r\n
0xb000012d | PLM outswap application %1 failed to invoke with error code %2\r\n
0xb000012e | PLM couldn't find any process for application %1, and handle it as non-large app\r\n
0xb000012f | PLM failed to decide application %1 is large or not with error code %2\r\n
0xb0000130 | PLM empty policy failed to process application %1 with error code %2.  Ignoring the application\r\n
0xb0000131 | PLM empty policy failed to empty application %1 with error code %2\r\n
0xb0000132 | PLM failed to terminate application %1 as empty policy with error code %2\r\n
0xb0000133 | PLM empty policy failed to enumerate applications with error code %1\r\n
0xb0000134 | PLM termination policy skipping application %1, which is not registered with PLM\r\n
0xb0000135 | PLM memory policy failed to queue work with error code %1\r\n
0xb0000136 | GetPackageData called on a Package %1, which is not in the PLM Package Data Store\r\n
0xb0000137 | ERROR: Failed to set priority to %1, PsmKey=%2, NTSTATUS=%3\r\n
0xb0000138 | AllowServiceOfPackages: Failed to terminate package=%1, type=%2, HRESULT=%3\r\n
0xb0000139 | _CheckServicingPackages: Failed to enumerate app, PsmKey=%1, HRESULT=%2\r\n
0xb000013a | _CheckServicingPackages: Failed to enumerate package, PkgFullName=%1, HRESULT=%2\r\n
0xb000013b | GetImmersiveApplicationCount failed with error code %1\r\n
0xb000013c | Background workitems were force terminated, PsmKey=%1\r\n
0xb000013d | ChangeApplicationBiState failed: %1\r\n
0xb000013e | Background workitems for package %1 were force terminated\r\n
0xb000013f | ChangePackageBiState failed: %1\r\n
0xb0000140 | ApplicationProcesses failed to track process ID %1 with error code %2\r\n
0xb0000141 | OnBeforeQuiescing: Failed to allocate memory for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000142 | OnAfterQuiescing: Quiesce failed for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000143 | ERROR: _CompleteQuiesceHelper: Failed to terminate timed-out PsmKey %1 with result %2\r\n
0xb0000144 | ERROR: QuiesceHelper: App forgotten while still Quiescing, PsmKey=%1, suspendTrigger=%2\r\n
0xb0000145 | Failed to query the wake counters associated with application %1. NTSTATUS: %2\r\n
0xb0000146 | _AllAppSyncOperationHelper: Failed to allocate memory for PsmKey=%1, HRESULT=%2\r\n
0xb0000147 | _MultiAppSyncOperationHelper: Failed to perform operation on PsmKey=%1, HRESULT=%2\r\n
0xb0000148 | _MultiAppSyncOperationHelper: Failed in wait, HRESULT=%1\r\n
0xb0000149 | _MultiPackageSyncOperationHelper: Failed to enumerate PsmKey=%1, HRESULT=%2\r\n
0xb000014a | _MultiPackageSyncOperationHelper: Failed to find package in data store, PkgFullName=1%, HRESULT=%2\r\n
0xb000014b | Failed to suspend and terminate apps, cPsmKeys=%1\r\n
0xb000014c | Could not initialize an extended launch grace period for app %1 with HRESULT %2 -- falling back to normal launch grace\r\n
0xb000014d | App %1 failed to show a window after launch. Will attempt to terminate it now\r\n
0xb000014e | Failed to get a window for an app; assuming that the app's window is not hung, Aumid=%1, HRESULT=%2\r\n
0xb000014f | Failed to query hidden time for visibility debounce for app %1 with error code %2\r\n
0xb0000150 | _StartNewKeyDebounce: Error Result=%2, PsmKey=%1\r\n
0xb0000151 | StartTrackingNewApp failed with %1. The application launch is not protected and the app might potentially get suspended inappropriately\r\n
0xb0000152 | ERROR: Failed to enumerate exemption targets starting from PsmKey=%1\r\n
0xb0000153 | Failed to enumerate existing applications from PSM with error code %1\r\n
0xb0000154 | PsmRegisterApplicationNotification failed for application %1 with status %2.  PLM's cache says that the application's registration is: %3\r\n
0xb0000155 | ERROR: Failed to enumerate force termination targets starting from PsmKey=%1, HRESULT=%2\r\n
0xb0000156 | Application %1 failed to be added in PLM Data Store\r\n
0xb0000157 | Failed to initialize string to send app notification %1 state %2\r\n
0xb0000158 | Failed to initialize string to remove app %1\r\n
0xb0000159 | Failed to add %1 for application %2. The application doesn't have BTC_AUDIO background task capability\r\n
0xb000015a | Failed to initialize CmApi\r\n
0xb000015b | Task completion manager failed to add %1 to its sharing cache with error code %2\r\n
0xb000015c | ClearTerminationTypesForForgottenPackage: Failed to clear termination type for app, Aumid=%1, HRESULT=%2\r\n
0xb000015d | ERROR: Failed to schedule the visibility debounce, PsmKey=%1, HRESULT=%2\r\n
0xb000015e | OnWindowChanged ERROR: Failed to queue thread for Aumid=%1, Hwnd=%2, change=%3, HRESULT=%4\r\n
0xb000015f | ERROR: Failed to schedule deferred visibility timer, PsmKey=%1, HRESULT=%2\r\n
0xb0000160 | WaitOnBiNotifyNewSession HRBiNotifyNewSession=%1 HRBiNotifyNewUser=%2\r\n
0xb0000161 | RegisterKernelNotifications HRESULT=%1\r\n
0xb0000162 | TCExemptionManager CompleteInitialization HRESULT=%1\r\n
0xb0000163 | PlmActivationManager CompleteInitialization HRESULT=%1\r\n
0xb0000164 | Plm CSDiagnostics CompleteInitialization HRESULT=%1\r\n
0xb0000165 | Plm LogOff/LogOn Registration HRESULT=%1\r\n
0xb00001f9 | BM: Queued evaluate WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fa | BM: Evaluate returned WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fb | BM: TaskActivated WorkItem: %1 Instance: %2\r\n
0xb00001fc | BM: TaskCompleted WorkItem: %1 Instance: %2\r\n
0xb00001fd | BM: TaskCanceled WorkItem: %1 Instance: %2\r\n
0xb00001fe | BM: Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb00001ff | BM: TaskActivating WorkItem: %1 Instance: %2\r\n
0xb0000200 | BM: Enter %1\r\n
0xb0000201 | BM: Exit %1, HR=%2\r\n
0xb0000202 | BM: TerminateHost WorkItem: %1\r\n
0xb0000203 | BM: ResourceSet invalidated for WorkItem: %1 Instance: %2.  This usually means the host has crashed before a ResourceSet could be applied.\r\n
0xb0000204 | BM: OnAcquired ignoring invalid CallbackId (%1).\r\n
0xb0000205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1'; WorkItemId='%2;' CallbackId='%3'.\r\n
0xb0000206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1'.\r\n
0xb0000207 | BM: OnApplicationStateChanged returning State='%2' PsmKey='%1' HR='%3'.\r\n
0xb0000208 | BM: OnAcquired received for CallbackId: %1\r\n
0xb0000209 | BM: OnAcquired request ignored for CallbackId: %1\r\n
0xb000020a | BM: ActivateDeferredWorkItem WorkItem: %1\r\n
0xb000020b | BM: ActivateDeferredWorkItem discarded WorkItem: %1 because of Status: %2\r\n
0xb000020c | BM: Enter %1 WorkItem: %2\r\n
0xb000020d | BM: Enter %1 WorkItem: %2 TaskInstanceId: %3\r\n
0xb000020e | BM: Exit %1\r\n
0xb000020f | BM: Failed to load settings for event %1.\r\n
0xb0000210 | BM: Failed to load settings for event %1 with error %2.\r\n
0xb0000211 | BM: Failed to load policy for CLSID: %1, for EventType %2 with error %3.\r\n
0xb0000212 | BM: Failed to load the policies with error %1.\r\n
0xb0000213 | BM: Evaluate returned WorkItem: %3 EventType: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb0000214 | BM: TaskWallClockActive WorkItem: %1 Instance: %2\r\n
0xb0000215 | BM: TaskWallClockExpired WorkItem: %1 Instance: %2\r\n
0xb0000216 | BM: Policy returned HRESULT: %3 for WorkItem: %2 PsmKey: %1.\r\n
0xb0000217 | BM: Canceling task for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000218 | BM: Ignoring cancelation request (whitelisted) for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000219 | BM: Session(%1) started, session initialization returned %2.\r\n
0xb000021a | BM: Session(%1) ended.\r\n
0xb000021b | BM: Activation ignored due to no Session(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb000021c | BM: Failed to acquire a ResourceSet for WorkItem: %1 with error %2.\r\n
0xb000021d | BM: WorkItem: %1 is being debugged. Setting wallclock limit to 0.\r\n
0xb000021e | BM: EvaluateActivationAction for WorkItem: %1 HRESULT: %2.\r\n
0xb000021f | BM: Skipped Buffering Exempted task with SQMId: %1 PsmKey: %2.\r\n
0xb0000220 | BM: Dropped Exempted task that came before SessionReady with SQMId: %1 PsmKey: %2.\r\n
0xb0000221 | BM: Activation ignored due to no User(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb0000222 | BM: User Logon Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000223 | BM: User Logoff Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000224 | BM: Pending activation discarded for work item (%1).\r\n
0xb0000225 | BM: Flushing ignored EvaluationState: %1 for WorkItem: %2.\r\n
0xb0000226 | BM: Flushing buffered activations.\r\n
0xb0000227 | BM: Global Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb0000228 | BM: A Session object for Session(%1) already exists.\r\n
0xb0000229 | BM: ShellSuspendState changed, oldState: %1 newState: %2\r\n
0xb000022a | BM: DPLKeyState changed, oldState: %1 newState: %2\r\n
0xb000022b | BM: Canceling WorkItem: %1 due to DPL policy.\r\n
0xb000022c | BM: Dropping activation for WorkItem: %1 due to DPL policy.\r\n
0xb000022d | BM: Buffered activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022e | BM: Exempted activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022f | BM: Buffered activation for WorkItem: %1 due to Thermal Throttling policy.\r\n
0xb0000258 | AM: Failed to read activation plugin registry with error code %1.\r\n
0xb0000259 | AM: Failed to CoCreate activation plugin with error code %1 and CLSID %2.\r\n
0xb000025a | AM: Successfully created activation plugin with CLSID %1 from the registry.\r\n
0xb000025b | AM: Failed to register package if needed with error %1.\r\n
0xb000025c | AM: Failed trying to register package by family name async during activation with error %1.\r\n
0xb000025d | AM: Failed trying to wait for the completion of the register package by family async during activation with error %1.\r\n
0xb00002bc | BAM: Added Package: %1 UserSid: %2.\r\n
0xb00002bd | BAM: Removed Package: %1 UserSid: %2.\r\n
0xb00002be | BAM: Added Application: %1 UserSid: %2.\r\n
0xb00002bf | BAM: Removed Application: %1 UserSid: %2.\r\n
0xb00002c0 | BAM: AccessState Changed for Package: %1 OldState: %2 NewState: %3 UserSid: %4.\r\n
0xb00002c1 | BAM: BackgroundExecutionManager::RequestAccessAsync called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c2 | BAM: BackgroundExecutionManager::GetStatus called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c3 | BAM: BackgroundExecutionManager::RemoveAccess called for Application: %1.\r\n
0xb00002c4 | BAM: Sanitizing data for package: %1 HRESULT: %2.\r\n
0xb00002c5 | BAM: ReregisteredPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002c6 | BAM: UnregisterPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002ee | FAM: NotifyTaskInstanceCompleted, TaskID:%1, hr:%2\r\n
0xb00002ef | FAM: NotifyTaskInstanceRunning, TaskID:%1 Timer - %2\r\n
0xb00002f0 | FAM: RegisterForegroundAgentManagerProxy:PID=%1, ConsumerTaskId=%2, Option=%3, hr=%4\r\n
0xb00002f1 | FAM: UiForeground:Memory:%1MB, CPU:%2%%\r\n
0xb00002f2 | FAM: CreateAgentLaunchRequest, TaskID:%1, Queue:%2, hr:%3\r\n
0xb00002f3 | FAM: CancelAgentRequest, TaskID:%1, CancelType=%2, hr:%3\r\n
0xb00002f4 | FAM: AbortAgentRequestsInternal, hr:%1\r\n
0xb00002f5 | FAM: CompleteAgent, TaskID:%1, hr:%2\r\n
0xb00002f6 | FAM: PrioritizeAgentRequest, TaskID:%1, hr:%2\r\n
0xb00002f7 | FAM: OnForegroundAppChanged()-Abort agents\r\n
0xb00002f8 | FAM: OnRelease()\r\n
0xb00002f9 | FAM: NotifyConsumer, Notification:%1, TaskID:%2, hrResult:%3\r\n
0xb00002fa | FAM: AcquireSharedResourceSet, ProductID:%1, ConsumerPid:%2, Pending:%3, hr:%4\r\n
0xb00002fb | FAM: ReleaseResourceSet, #%1, hr:%2\r\n
0xb00002fc | FAM: TimerExpired:TerminateHost[PID=%1]\r\n
0xb00002fd | FAM: AcquireResourceSet, #%1, Mem:%2MB, CPU:%3%%, hr:%4\r\n
0xb00002fe | FAM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000321 | OTM: Read settings. First retry timeout = %1 ms, Second retry timeout = %2 ms, Third retry timeout = %3 ms, Maximum Retry Timeout = %4 ms\r\n
0xb0000322 | OTM: Task instance %2 of product %1 completed\r\n
0xb0000323 | OTM: TaskHost of product %1 has crashed\r\n
0xb0000324 | OTM: TaskHost of product %1 has been completed by PacMan\r\n
0xb0000325 | OTM: Launching OEM boot agents\r\n
0xb0000326 | OTM: Launching boot agents for product %1 failed with error %2\r\n
0xb0000327 | OTM: Launch boot agents for product %1\r\n
0xb0000328 | OTM: Running OnUpdateStarted for product %1\r\n
0xb0000329 | OTM: Restarting boot agents for product %1 after update\r\n
0xb000032a | OTM: Start menu is ready.\r\n
0xb000032b | OTM: Could not launch OEM boot agents. QueueUserWorkItem failed with error %1.\r\n
0xb000032c | OTM: Could not process update notification for OEM application. QueueUserWorkItem failed with error %1.\r\n
0xb000032d | OTM: Could not process update notification for OEM application. ProcessUpdateNotification failed with error %1.\r\n
0xb000032e | OTM: OemTaskManager::NotifyTaskInstanceCompleted failed with error %1.\r\n
0xb000032f | OTM: OemTaskManager::NotifyTaskHostCompleted failed with error %1.\r\n
0xb0000330 | OTM: OemApp::DumpAgents failed with error %1.\r\n
0xb0000331 | OTM: An error occurred. Hr = %1\r\n
0xb0000332 | OTM: No apps with ServiceAgents were found.\r\n
0xb0000333 | OTM: No ServiceAgent task found for product %1.\r\n
0xb0000334 | OTM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb000035d | PLM: Start tracking new app user %1 app %2, contract %3, hr = %4\r\n
0xb000035e | PLM: Application launched %1 in app %2, hr = %3\r\n
0xb000035f | PLM: Application resume %1 in app %2, hr = %3\r\n
0xb0000360 | PLM: Suspend-Terminate(%3) task %1 in app %2\r\n
0xb0000361 | PLM: Suspend-Terminate suspend of task %1 in app %2 exemption %3\r\n
0xb0000362 | PLM: Suspend-Terminate auto terminate(%3) task %1 in app %2\r\n
0xb0000363 | PLM: Suspend-Terminate task %1 in app %2, hr %3\r\n
0xb0000364 | PLM: Halt app %1, hr %2\r\n
0xb0000365 | PLM: Task resume %1 in app %2\r\n
0xb0000366 | PLM: Task cancel %1 in app %2\r\n
0xb0000367 | PLM: Task remove %1 in app %2\r\n
0xb0000368 | PLM: Queue Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000369 | PLM: Queue Activation State Change Notification %1 state %2\r\n
0xb000036a | PLM: Before Activate task %1 for user %2 in app %3, contract %4, hostid %5, hr = %6\r\n
0xb000036b | PLM: After Activate task %1 with result %2, hr = %3\r\n
0xb000036c | PLM: ApplicationLayer=%1 Set Foreground new task %2, prev task %3\r\n
0xb000036d | PLM: Add task %1 to user %2 and app %3, hr = %4\r\n
0xb000036e | PLM: Create app for user %1, %2, new [app(%3) pkg(%4)], hr = %5\r\n
0xb000036f | PLM: Add task %1 to user %2 and app %3, new [app(%4) pkg(%5)], hr = %6\r\n
0xb0000370 | PLM: Remove task %1, was found(%2)\r\n
0xb0000371 | PLM: Remove app if empty from user %1, %2, hr = %3\r\n
0xb0000372 | PLM: Remove pkg if empty from user %1, %2, hr = %3\r\n
0xb0000373 | PLM: Send Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000374 | PLM: Send Activation State Change Notification %1 state %2\r\n
0xb0000376 | PLM: Timer Started duration %1ms, hr %2\r\n
0xb0000377 | PLM: Timer Expired duration %1ms, hr %2\r\n
0xb0000378 | PLM: Abort task %1 reason %2, dump(%3)\r\n
0xb0000379 | PLM: Task rehydrate %1 in app %2 contract %3\r\n
0xb000037a | PLM: Start RPC suspension timer PSMKey=%1 WakeCounters=%2, hr = %3\r\n
0xb000037b | PLM: Cancel RPC suspension timer PSMKey=%1 app state=%2\r\n
0xb000037c | PLM: Terminate application PSMKey=%1 due to expired RPC suspension timeout\r\n
0xb000037d | PLM: Application %1 cannot be terminated due to %2 exemption\r\n
0xb000037e | PLM: Application %1 can be terminated\r\n
0xb000037f | PLM: EvaluateAndTerminateApplication %1 cannot be terminated due to %2\r\n
0xb0000380 | PLM: EvaluateAndTerminateApplication %1, terminate hr = %2\r\n
0xb0000381 | PLM: Terminate debounce app %1 current state %2 ultimate state %3\r\n
0xb0000382 | PLM: Terminate debounce app %1, hr = %2\r\n
0xb0000383 | PLM: Terminate reason was cleared\r\n
0xb0000384 | PLM: Abort app user %1 app %2 reason %3, dump(%4)\r\n
0xb0000385 | PLM: Watson dump NOT generated for user %1 app %2, process count %3\r\n
0xb0000386 | PLM: Watson dump start for user %1 app %2 reason %3 description %4, process %5 (%6)\r\n
0xb0000387 | PLM: Watson dump information for user %1 app %2 product Id %3 title %4 version %5\r\n
0xb0000388 | PLM: Watson dump end for user %1 app %2, hr %3\r\n
0xb0000389 | PLM: Add Watson dump to user %1 app %2 process %3, hr %4\r\n
0xb000038a | PLM: Failed to add Watson process info for process %1 user %2 app %3\r\n
0xb000038b | PLM: Watson dump status changed pids(%1)\r\n
0xb000038c | PLM: Watson dump status changed, add process %1 user %2 app %3\r\n
0xb000038d | PLM: Watson dump status changed, remove process %1 user %2 app %3\r\n
0xb000038e | PLM: Watson dump status changed, unknown process %1 app %2\r\n
0xb000038f | PLM: Watson add/remove(%2) error report task completion to process %1 (signaled %4), hr %3\r\n
0xb0000390 | PLM: Watson in progress for PSMKey %1, waiting...\r\n
0xb0000391 | PLM: Watson in progress finished for PSMKey %1\r\n
0xb0000392 | PLM: Extending RPC suspension timer PSMKey=%1\r\n
0xb0000393 | PLM: Acquire network reference failed CM_RESULT=%1\r\n
0xb0000394 | PLM: Release network reference failed CM_RESULT=%1\r\n
0xb0000395 | PLM: Suspend-Terminate(%2) app %1 exemption %3, hr %4\r\n
0xb0000396 | PLM: Suspend-Terminate task %1 while dehydrating\r\n
0xb0000397 | PLM: Add user %1 sid %2 to data store, hr = %3\r\n
0xb0000398 | PLM: Start launch grace for user %1 app %2, hr = %3\r\n
0xb0000399 | PLM: Set Window Id for user %1 app %2 wnd %3\r\n
0xb000039a | PLM: EvaluateLaunchGraceCompleted for user %1 app %2\r\n
0xb000039b | PLM: Terminating reexisting app due to sihost restart with PSMKey %1, status %2\r\n
0xb000039c | PLM: Terminating preexisting applications on sihost startup\r\n
0xb000039d | PLM: Set Pause On Lock for user %1 app %2 value %3\r\n
0xb000041b | AAM: Initiate activation for user %1 app %2 contract %3 task %4, hr %5\r\n
0xb000041c | AAM: Initiate activation completed for task %2 (expected %1), hr %3\r\n
0xb000041d | AAM: Initialize activation for user %1 app %2 contract %3 lightup(%5), hr %4\r\n
0xb000041e | AAM: Validate activation, hr %1\r\n
0xb000041f | AAM: Verify license for pkg %1, hr %2\r\n
0xb0000420 | AAM: Activate activation task %1 host %2, hr %3\r\n
0xb0000421 | AAM: Activation shim timer expired %1, hr %2\r\n
0xb0000422 | AAM: Initiate Core UI, hr %1\r\n
0xb0000423 | AAM: Release Core UI\r\n
0xb0000424 | AAM: Create Windows AAM, hr %1\r\n
0xb0000425 | AAM: Attempted remediation, hr %1\r\n
0xb0000426 | AAM: Failed while trying to find a remediation handler, hr %1\r\n
0xb0000427 | AAM: Failed while trying to find the package status, hr %1\r\n
0xb0000428 | AAM: Failed while trying to find the package origin, hr %1\r\n
0xb0000429 | AAM: Failed while trying to verify and initialize the activation, hr %1\r\n
0xb000042a | AAM: Failed while trying to check roaming data, hr %1\r\n
0xb000042f | AAM: Broker created plugins %1, expected %2\r\n
0xb0000430 | AAM: Broker initialize, hr %1\r\n
0xb0000431 | AAM: Broker start activate application %1 (%3 args) arg[0] %2 type %4 caller PID %5 (initialization count %6)\r\n
0xb0000432 | AAM: Broker end activate application %1 launched PID %2 task %3, hr %4\r\n
0xb0000433 | AAM: Broker activate task with result for app %1 caller PID %2 caller task %3\r\n
0xb0000434 | AAM: Broker get result for PID %1 task %2 result %3, hr %4\r\n
0xb0000435 | AAM: Broker get task id for process %1 window %2 = task %3, hr %4\r\n
0xb0000436 | AAM: Broker init session manager, hr %1\r\n
0xb0000437 | AAM: Broker release session manager\r\n
0xb0000438 | AAM: Broker add task with result for parent %1, hr %2\r\n
0xb0000439 | AAM: Broker get task with result for parent %1, hr %2\r\n
0xb000043a | AAM: Broker remove task with result for parent %1, hr %2\r\n
0xb000043b | AAM: Broker create completed event for caller PID %1, hr %2\r\n
0xb000043c | AAM: Broker get task with result for child %1, hr %2\r\n
0xb000043d | AAM: Broker parent task completed %1 with child state %2\r\n
0xb000043e | AAM: Broker child task completed %1 with state %2, hr %3\r\n
0xb000043f | AAM: Broker task event signaled for parent %1 child %2 previous state %3, hr %4\r\n
0xb0000440 | AAM: Broker close task %1, hr %2\r\n
0xb0000441 | AAM: Broker activate application %1 arg[%3] %2\r\n
0xb000044c | FM-ARP: ApplyResourceSetType ResourceSetType=%1 User=%2 PSMKey=%3 ResourceSet=%4 HRESULT=%5\r\n
0xb000044d | FM-ARP: ApplyTerminal UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044e | FM-ARP: RemoveInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044f | FM-ARP: ResetInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000450 | FM-ARP: OnRelease UserContext=%1 PsmKey=%2 ReleaseAction=%3 ReleasedCachedResource=%4 ReleaseAppliedResource=%5 HRESULT=%6\r\n
0xb0000451 | FM-ARP: OnAcquired UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000452 | FM-ARP: OnOutOfMemory UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000453 | FM-ARP: ApplyResourceBoost User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000454 | FM-ARP: AcquireResourceSet ResourceSetType=%1 Usercontext=%2 PsmKey=%3 HRESULT=%4\r\n
0xb0000455 | FM-ARP: Apply Cached Resource Set Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000456 | FM-ARP: Clear Cached Resource User=%1 PSMKey=%2\r\n
0xb0000457 | FM-ARP: Fire Cached ResourceCallback User=%1 PSMKey=%2\r\n
0xb00004b0 | FM-CAM: OnApplicationStateChangedEx UserContext=%1 PsmKey=%2 state=%3 HRESULT=%4\r\n
0xb00004b1 | FM-CAM: AcquireForegroundResource UserContext=%1 PsmKey=%2 isPending=%3\r\n
0xb00004b2 | FM-CAM: OnResourceAcquired UserContext=%1 PsmKey=%2\r\n
0xb00004b3 | FM-CAM: OnResourceTimerExpired UserContext=%1 PsmKey=%2\r\n
0xb00004e2 | FM: TaskCompletion New Battery Saver State %1\r\n
0xb00004e3 | FM: TaskCompletion Revoke Exemption PID=%1 AUMID=%2 TC=%3\r\n
0xb00004e4 | FM: TaskCompletion Apply(%3) Exemption PID=%1 TC=%2 HRESULT=%4\r\n
0xb00004e5 | FM-EEP: CheckProcessBackgroundEligibility ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e6 | FM-EEP: ApplyTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e7 | FM-EEP: RevokeTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e8 | FM-EEP: RequestExtendedExecution ProcessId=%1 Reason=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004e9 | FM-EEP: RegisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004ea | FM-EEP: CompleteExtendedExecution ProcessId=%1 fIsResumed=%2 HRESULT=%3\r\n
0xb00004eb | FM-EEP: RevokeSuspensionExtension User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00004ec | FM-ARP: NotifyPendingResourceSetTransition ResourceSetType=%1 ResourceSet=%2 HRESULT=%3\r\n
0xb00004ed | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 fTimerExpiredCallback=%2 HRESULT=%3\r\n
0xb00004ee | FM-EEP: IsApplicationStateBackgroundEligibile User=%1 PsmKey=%2 fResult=%3\r\n
0xb00004ef | FM-EEP: RevokeTaskCompletionExemption AppUserModelId=%1 HRESULT=%2\r\n
0xb00004f0 | FM-EEP: AllowBackgroundExecution User=%1 AppUserModelId=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004f1 | FM-EEP: OnPackageEnergyStateChange PackageFullName=%1 PackageState=%2 HRESULT=%3\r\n
0xb00004f2 | FM-EEP: RegisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f3 | FM-EEP: UnregisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f4 | FM-EEP: UnregisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004f5 | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 TC=%2 isResourcePending =%3 HRESULT=%4\r\n
0xb00004f6 | FM-EEP: Task Completion Denied By EDP Policy ProcessId=%1 TC=%2\r\n
0xb00004f7 | FM-EEP: IsForegroundApplication Application=%1 Result=%2\r\n
0xb0000578 | FM: Registering callback %1 HRESULT=%2\r\n
0xb0000579 | FM: Generate ActivationInstanceID Id=%1\r\n
0xb000057a | FM: +ActivationPrerequisitePhase ActivationInstanceId=%1 UserContext=%2 AUMID=%3 ContractId=%4\r\n
0xb000057b | FM: -ActivationPrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb000057c | FM: +Resume_RehydrationPhase ActivationInstanceId=%1\r\n
0xb000057d | FM: -Resume_RehydrationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000057e | FM: +ResumeActivation ActivationInstanceId=%1 fIsResumed=%2\r\n
0xb000057f | FM: -ResumeActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000580 | FM: +Resume_ActivationPhase ActivationInstanceId=%1\r\n
0xb0000581 | FM: -Resume_ActivationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000582 | FM: +PauseActivation ActivationInstanceId=%1\r\n
0xb0000583 | FM: -PauseActivation HRESULT=%1 PausePending=%2\r\n
0xb0000584 | FM: +CancelActivation ActivationInstanceId=%1\r\n
0xb0000585 | FM: -CancelActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000586 | FM: +AbortActivation ActivationInstanceId=%1 Reason=%2 fGenerateWER=%3\r\n
0xb0000587 | FM: -AbortActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000588 | FM: +GetActivationProcessId ActivationInstanceId=%1\r\n
0xb0000589 | FM: -GetActivationProcessId ActivationInstanceId=%1 PID%2 HRESULT=%3\r\n
0xb000058a | FM: +SetForegroundActivationInstance ActivationInstanceId=%1 Isforeground=%2\r\n
0xb000058b | FM: -SetForegroundActivationInstance ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000058c | FM: SetActivationDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb000058d | FM: OnActivationStateChanged ActivationInstanceId=%1 state=%2 HRESULT=%3\r\n
0xb000058e | FM: OnApplicationStateChanged UserContext=%1 PSMKey=%2 state=%3 HRESULT=%4\r\n
0xb000058f | FM: IsValidActivationProcessId ActivationInstanceID=%1 PID=%2 fValid=%3 HRESULT=%4\r\n
0xb0000590 | FM: GetForegroundProductId fIgnoreLockScreen=%1 ProductID=%2 HRESULT=%3\r\n
0xb0000591 | FM: GetProductIdFromProcessID ProductID=%1 PID=%2 HRESULT=%3\r\n
0xb0000592 | FM: Discarding Application Frozen notification because the application isn't really frozen\r\n
0xb0000593 | FM: Dehydrate Application AUMID=%1 HRESULT=%2\r\n
0xb0000594 | FM: +ResumePrerequisitePhase ActivationInstanceId=%1\r\n
0xb0000595 | FM: -ResumePrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb0000596 | FM: GenerateWatsonReport PID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000597 | FM: SetContinuation ActivationInstanceID=%1\r\n
0xb0000598 | FM: AbandonContinuation ActivationInstanceID=%1\r\n
0xb0000599 | FM: PerformContinuation ActivationInstanceID=%1\r\n
0xb000059a | FM: Shutdown HRESULT=%1\r\n
0xb000059b | FM: +PauseActivation ActivationInstanceId=%1 AUMID=%2 PackageFullName=%3\r\n
0xb000059c | FM: +ActivationBypass ActivationInstanceId=%1\r\n
0xb000059d | FM: -ActivationBypass ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000059e | FM: +PostPausePendingResume ActivationInstanceId=%1\r\n
0xb000059f | FM: -PostPausePendingResume ActivationInstanceId=%1 HRESULT=%2\r\n
0xb00005a0 | FM: SetActivationImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb00005a1 | FM: NotifyWindowAdded TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a2 | FM: NotifyWindowRemoved TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a3 | FTM: Logoff User=%1 HRESULT=%2\r\n
0xb00005a4 | FM: ActivationTimeoutPolicyChanged  TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a5 | FM-EEP: OnConnectedStandbyStateChanged  State=%1\r\n
0xb00005a6 | FM: SendActivationNotification ActivationId=%1 NotificationId=%2\r\n
0xb00005a7 | FM: OnResourceAcquired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a8 | FM: OnResourceTimerExpired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a9 | FM: PostPausePendingActivation ActivationId=%1 HRESULT=%2\r\n
0xb00007d0 | VoIPPolicy: Evaluate Activation Action for PsmKey = %2, WorkItemId = %1, Action = %3, HRESULT = %4\r\n
0xb00007d1 | VoIPPolicy: Task Activated for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d2 | VoIPPolicy: Task Completed for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d3 | VoIPPolicy: Task Canceled for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d4 | VoIPPolicy: Task Aborted for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d5 | VoIPPolicy: Determine and Apply Resources PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d6 | VOIP: NotifyVoipActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d7 | VOIP: LaunchVoipRtcTask called for PID:%1 PSMKey:{%2} with TaskEntryPoint:{%3} and WNFStateName:{%4} HRESULT:%5.\r\n
0xb00007d8 | VOIP: NotifyVoipActivityCompleted called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d9 | VOIP: HoldActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007da | VOIP: UnholdActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007db | VOIP: NotifyIncomingCallDialogDisplayed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dc | VOIP: NotifyIncomingCallDialogDismissed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dd | VOIP: CallActive called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007de | VOIP: AppLaunchVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007df | VOIP: OnVoipActivityCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e0 | VOIP: AppHoldActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e1 | VOIP: AppUnholdActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e2 | VOIP: OnIncomingCallDialogDisplayed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e3 | VOIP: OnIncomingCallDialogDismissed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e4 | VOIP: AppDetermineAndApplyBestResourceSet called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e5 | VOIP: PolicyEvaluateAction called for WorkItemId:{%1} PSMKey:{%2} ActivationAction:%3 HRESULT:%4.\r\n
0xb00007e6 | VOIP: PolicyTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e7 | VOIP: PolicyTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e8 | VOIP: PolicyTaskCanceled called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e9 | VOIP: PolicyTaskAborted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007ea | VOIP: OnForegroundApplicationChanged called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007eb | VOIP: AppOnTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ec | VOIP: AppOnTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ed | VOIP: AppCancelVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ee | VOIP: CancelVoipRtcTask called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb0000c81 | Task: %1 has started\r\n
0xb0000c82 | Task: %1 has paused\r\n
0xb0000c83 | Task: %1 has resumed\r\n
0xb0000c84 | Task: %1 has completed\r\n
0xb0000c85 | EM: +GetTaskInfo()\r\n
0xb0000c86 | EM: -GetTaskInfo(). HRESULT = %1\r\n
0xb0000c87 | EM: GetAppInfo:%1,%2:%3\r\n
0xb0000c88 | EM: ParseBackgroundAbilities - HRESULT=%1\r\n
0xb0000c89 | EM: +ExecManServerHost::CreateProcess\r\n
0xb0000c8a | EM: -ExecManServerHost::CreateProcess. HRESULT=%1\r\n
0xb0000c8b | Sqm::AppPlatSqmAppDataUsage: %1/%2 - TaskID = %3, Type = %4, NewState = %5, ReasonForStateChange = %6, Duration (ms) = %7, PeakMemory (kb) = %8\r\n
0xb0000c8f | Emc::ExecuteCommand: StartTaskCallbackBegin: TaskID = %1\r\n
0xb0000c90 | Emc::ExecuteCommand: StartTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c91 | Emc::ExecuteCommand: PauseTaskCallbackBegin: TaskID = %1\r\n
0xb0000c92 | Emc::ExecuteCommand: PauseTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c93 | Emc::ExecuteCommand: ResumeTaskCallbackBegin: TaskID = %1\r\n
0xb0000c94 | Emc::ExecuteCommand: ResumeTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c95 | Emc::ExecuteCommand: ControlTaskCallbackBegin: TaskID = %1\r\n
0xb0000c96 | Emc::ExecuteCommand: ControlTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c97 | Emc::ExecuteCommand: CancelTaskCallbackBegin: TaskID = %1\r\n
0xb0000c98 | Emc::ExecuteCommand: CancelTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c99 | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackBegin: TaskID = %1\r\n
0xb0000c9a | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c9e | Emc::RegisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, HR = %3\r\n
0xb0000ca8 | Emc::DeregisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, Reason = %3, HR = %4\r\n
0xb0000ca9 | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleBegin: ProductID = %1\r\n
0xb0000caa | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleEnd: ProductID = %1\r\n
0xb0000cab | EM: Skipping terminate process call for %1\r\n
0xb0000cac | EM: Terminating process: PID = %1, ExitCode = %2\r\n
0xb0000ce4 | AimServer::OnAgentRequestInvoked: AgentRequestID %1 was invoked. PID = %2, HR = %3\r\n
0xb0000ce5 | AimServer::ReadSettings: HR = %1\r\n
0xb0000ce6 | AimServer: Detected server for scope %1 terminated (PID = %2)\r\n
0xb0000ce8 | AimServer::HandleEvent: ProductID %1 received PM LifecyleEvent %2. HR Notification = %3, HR = %4\r\n
0xb0000ce9 | BA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cea | BA::RegisterServiceRequest: AlreadyReserved = %1, SR = %2, HR = %3\r\n
0xb0000ceb | BA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cec | BA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000ced | BA::NotifyTaskInstanceCompleted: Terminating Orphaned Host PID = %1\r\n
0xb0000cee | BA::OrphanAgentRequest: AgentRequestID = %1, HR = %2\r\n
0xb0000cef | BA::UnRegisterServiceRequest: Terminating host PID %1\r\n
0xb0000cf0 | BA::UnRegisterServiceRequest: Orphaning host PID %1\r\n
0xb0000cf1 | BA::UnRegisterServiceRequest: Terminating second old orphaned host PID %1\r\n
0xb0000cf2 | BTM::RecvCallback: Timer expired for AgentRequestID %1\r\n
0xb0000cf3 | BTM::LaunchTask: TaskURI = %1 TaskID = %2, PID = %3, HR = %4\r\n
0xb0000cf4 | GBA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cf5 | GBA::RegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf6 | GBA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf7 | GBA::RegisterAgentRequest: AgentRequestID = %1, type = %2, hr = %3\r\n
0xb0000cf8 | GBA: Cancelling low priority %3 agent because high priority %2 needs to run: Resource was dedicated = %1\r\n
0xb0000cf9 | GBA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000cfa | GBA::TryAcquireResourceSet: pending = %1, type = %2, HR = %3\r\n
0xb0000cfb | GBA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfc | BA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfd | BA::NotifyTaskHostCompleted: ProductID = %1, PID = %2\r\n
0xb0000cfe | BA::RegisterAgentRequest: ProductID = %1, AgentRequestID = %2, HR = %3\r\n
0xb0000cff | BA::PdcActivationFailed: ProductID = %1, Reason = %2, NTSTATUS = %3\r\n
0xb0000dac | FTM: AllowBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dad | FTM: Process is using too much memory for BG Execution. PID=%1, MemUsage=%2, RequiredMemUsage=%3\r\n
0xb0000dae | FTM: Removing BG capability from Task ID %1 due to OOM\r\n
0xb0000daf | FTM: Battery Saver State has change. New state = %1\r\n
0xb0000db0 | FTM: Attempted new BG Execution request due to battery state change. TaskID=%1\r\n
0xb0000db1 | FTM: NotifyTaskInstanceCompleted TaskID=%1 HRESULT=%2\r\n
0xb0000db2 | FTM: NotifyTaskInstancePaused TaskID=%1 HRESULT=%2\r\n
0xb0000db3 | FTM: NotifyTaskInstanceRunning TaskID=%1 HRESULT=%2\r\n
0xb0000db4 | FTM: SendTaskStatusChange TaskID=%1 Status=%2 HRESULT=%3\r\n
0xb0000db5 | FTM: NotifyTaskHostCompleted HRESULT=%1\r\n
0xb0000db6 | FTM: Discarding NotifyTaskHostFrozen notification because the host isn't really frozen\r\n
0xb0000db7 | FTM: NotifyTaskHostFrozen PID=%1 HRESULT=%2\r\n
0xb0000db8 | FTM: NotifyTaskHostDehydrated HRESULT=%1\r\n
0xb0000db9 | FTM: Registering callback %1 HRESULT=%2\r\n
0xb0000dba | FTM: New Task %1 is dehydration-suppressing\r\n
0xb0000dbb | FTM: Applying Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbc | FTM: Revoking Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbd | FTM: +LaunchTask TaskURI=%1 LaunchFlags=%2\r\n
0xb0000dbe | FTM: -LaunchTask TaskURI=%1 TaskID=%2 PID=%3 HRESULT=%4\r\n
0xb0000dbf | FTM: ResumeTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc0 | FTM: Removing Foreground Resources from TaskID=%1\r\n
0xb0000dc1 | FTM: SetForegroundTaskInstanceId TaskID=%1 HRESULT=%2\r\n
0xb0000dc2 | FTM: PauseTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc3 | FTM: CancelTask TaskID=%1 Frozen=%2 HRESULT=%3\r\n
0xb0000dc4 | FTM: AbortTask being ignored because the task is completed TaskID=%1\r\n
0xb0000dc5 | FTM: AbortTask TaskID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000dc6 | FTM: SetTaskDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb0000dc7 | FTM: RequestProcessBackgroundExecution type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc8 | FTM: CancelProcessBackgroundExecutionRequest type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc9 | FTM: TaskRunningInBackground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dca | FTM: TaskRunningInForeground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dcb | FTM: Changing activation policy to resume due to BG Execution for ProductID %1\r\n
0xb0000dcc | FTM: OnShutdownCompleted\r\n
0xb0000dcd | FTM: Ignoring expired watchdog for task %1 because it is being debugged.\r\n
0xb0000dce | FTM: Watchdog fired for task %1 while running in background. Pausing Task.\r\n
0xb0000dcf | FTM: Request BG Execution Denied because it wasn't running. TaskID=%1\r\n
0xb0000dd0 | FTM: Request BG Execution Denied because product was forbidden. TaskID=%1\r\n
0xb0000dd1 | FTM: Request BG Execution Denied because task didn't have BG abilities in its manifest. TaskID=%1\r\n
0xb0000dd2 | FTM: Request BG Execution Denied due to lack of resources. TaskID=%1\r\n
0xb0000dd3 | FTM: Request BG Execution Denied because battery policy prevented it. TaskID=%1\r\n
0xb0000dd4 | FTM: RequestBGAccess IsAllowed=%1 TaskID=%2 HRESULT=%3\r\n
0xb0000dd5 | FTM: RemoveBGRequest RequestedRemoval=%1 ActualRemoval=%2 TaskID=%3 HRESULT=%4\r\n
0xb0000dd6 | FTM: ForbidBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dd7 | FTM: IsValidTaskInstancePid TaskID=%1 Pid=%2 fValid=%3 HRESULT=%4\r\n
0xb0000dd8 | FTM: DetermineBestResourceSet for child ProductID=%1 LaunchFlags=%2 ResourceSetType=%3\r\n
0xb0000dd9 | FTM: OnRelease ResourceSet TaskID=%1 ResouceSet=%2 HRESULT=%3\r\n
0xb0000dda | FTM:UITask Call to Acquire network reference failed CM_RESULT=%1\r\n
0xb0000ddb | FTM:UITask Call to Release network reference failed CM_RESULT=%1\r\n
0xb0000ddc | FTM: SetTaskImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb0000ddd | FTM: +RequestProcessBackgroundExecution type=%1 Pid=%2\r\n
0xb0000dde | FTM: +RequestBackgroundExecution type=%1\r\n
0xb0000ddf | FTM: -RequestBackgroundExecution type=%1 HRESULT=%2\r\n
0xb0000de0 | FTM: +RequestBGAccess TaskInstanceId=%1 type=%2\r\n
0xb0000de1 | FTM: Request BG Execution Denied because DPL policy prevented it. TaskID=%1\r\n
0xb0000de2 | FTM: Windows Information Protection keys locked state (%1)\r\n
0xb0000e42 | VoIP: Foreground state for product %1 has changed. Is in foreground = %2\r\n
0xb0000e43 | VoIP: Canceling communication agent for product %1\r\n
0xb0000e44 | VoIP: Timer expired for keep-alive agent of product %1\r\n
0xb0000e45 | VoIP: Timer expired for incoming call agent of product %1\r\n
0xb0000e46 | VoIP: Launched agent instance with id %2 and URI %1\r\n
0xb0000e47 | VoIP: Canceled agent instance with id %1\r\n
0xb0000e48 | VoIP: Set active call resource set\r\n
0xb0000e49 | VoIP: Set communication agent resource set\r\n
0xb0000e4a | VoIP: Set VoIP Worker resource set\r\n
0xb0000e4b | VoIP: Applied terminal resource set\r\n
0xb0000e4c | VoIP: Last task instance completed. Releasing the task host ...\r\n
0xb0000e4d | VoIP: Launching active call agent instance for product %1\r\n
0xb0000e4e | VoIP: Canceling active call agent for product %1\r\n
0xb0000e4f | VoIP: Putting an active call on hold for product %1\r\n
0xb0000e50 | VoIP: Taking an active call off hold for product %1\r\n
0xb0000e51 | VoIP: Incoming call dialog has been displayed for product %1\r\n
0xb0000e52 | VoIP: Incoming call dialog has been dismissed for product %1\r\n
0xb0000e53 | VoIP: Launch communication agent request received from process %1 for product %2\r\n
0xb0000e54 | VoIP: Read settings. Keep alive timout = %1 ms, Max agent request queue = %2, Incoming call grace period = %3 ms, Incoming call dismissed grace period = %4 ms\r\n
0xb0000e55 | VoIP: Received request to launch agent type %2 for product %1\r\n
0xb0000e56 | VoIP: Task instance %2 of product %1 completed\r\n
0xb0000e57 | VoIP: Processing request to launch agent type %2 for product %1\r\n
0xb0000e58 | VoIP: Added VoIPApp object to map for product %1\r\n
0xb0000e59 | VoIP: Removed VoIPApp object from map for product %1\r\n
0xb0000e5a | VoIP: Getting VoIPApp object from map for product %1\r\n
0xb0000e5b | VoIP: Publishing WNF_DEVP_VOIP_ACTIVE_CALL_STATE_CHANGE failed with status %1\r\n
0xb0000e5c | VoIP: Subscribing to the WNF_WIFI_CONNECTION_STATUS event failed with status %1\r\n
0xb0000e5d | VoIP: Subscribed to WNF_WIFI_CONNECTION_STATUS? %1\r\n
0xb0000e5e | VoIP: WiFi connection status active/dormat? %1 (hConnection = %2)\r\n
0xb0000e5f | VoIP: RtlQueryWnfStateData failed trying to query the value of WNF_WIFI_CONNECTION_STATUS. NTSTATUS = %1\r\n
0xb0000e60 | VoIP: Could not spin up worker for UpdateWiFiStateHelper. HR =%1\r\n
0xb0000e61 | VoIP: In active call? %1\r\n
0xb0000e62 | VoIP: CmUtilSetWiFiActive was not successful. This could be because WiFi disconnected by the time we were notified of the connection.\r\n
0xb0000e63 | VoIP: WiFi connection status is %1.\r\n
0xb0000e64 | VoIP: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000e65 | VoIP: PhoneServiceRestart: HR = %1\r\n
0xb0000e66 | VoIP: PhoneServiceRestart: Product = %1, HR = %2\r\n
0xb0000e67 | VoIP: Launching call query info agent instance for product %1\r\n
0xb0000e68 | VoIP: Canceling call query info agent instance for product %1\r\n
0xb0000e69 | VoIP: Terminating agents due to low memory for product %1\r\n
0xb0000e6a | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2\r\n
0xb0000e6b | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2, fApplied = %3, HR = %4\r\n
0xb0000e6c | VoIP: Set PDC Network Active for product = %1, NTSTATUS = %2\r\n
0xb0000e6d | VoIP: Set PDC Network Inactive for product = %1, NTSTATUS = %2\r\n
0xb0000e6e | VoIP: Renew PDC Network activation failed for product = %1, NTSTATUS = %2\r\n
0xb0000e73 | VoIP: An error occurred. Hr = %1\r\n
0xb00017d4 | %1 - [%2 = %3]\n\r\n
0xb00017d5 | %1 - Parsing config file [%2] file size = %3.  Parse = %4\r\n
0xb00017d6 | %1 - OnTaskModelMessage: Dispatching EM message\r\n
0xb00017d7 | %1 - InitializeTaskHost URI=%2, Page=%3, TaskId=%4\r\n
0xb00017d8 | %1 - Resuming Task from dehydration\r\n
0xb00017d9 | %1 - TaskHandler::GetTaskHandler hr=%2\r\n
0xb00017da | %1 - TaskHost Init\r\n
0xb00017db | %1 - TaskHost Init hr = %2\r\n
0xb00017dc | %1 - Host Dispatcher Exiting hr = %2\r\n
0xb00017dd | %1 - TaskHandlerReady received\r\n
0xb00017de | %1 - StartTask TaskId=%2\r\n
0xb00017df | %1 - PauseTask TaskId=%2\r\n
0xb00017e0 | %1 - ResumeTask TaskId=%2\r\n
0xb00017e1 | %1 - OnTaskHandlerVisible received\r\n
0xb00017e2 | %1 - OnTaskHandlerHidden received\r\n
0xb00017e3 | %1 - BackgroundExecutionCallback TaskId[%2] Command[%3]\r\n
0xb00017e4 | %1 - BackgroundExecutionCallback hr=%2\r\n
0xb00017e5 | %1 - OnHostRunning\r\n
0xb00017e6 | %1 - OnHostRunning. hr = %2\r\n
0xb00017e7 | %1 - Dehydrating. dehydrateGracefully = %2\r\n
0xb00017e8 | %1 - Gracefully dehydrating TaskHost\r\n
0xb00017e9 | %1 - TryDehydrateHost. hr = %2\r\n
0xb00017ea | %1 - DehydrateHost event triggered\r\n
0xb00017eb | %1 - WaitForUnfreeze hr = %2\r\n
0xb00017ec | %1 - ReduceMemoryHostCallback hr = %2\r\n
0xb00017ed | %1 - Graceful tear-down failed\r\n
0xb00017ee | %1 - BeforeHostRunningInBackgroundCallback\r\n
0xb00017ef | %1 - BeforeHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f0 | %1 - AfterHostRunningInBackgroundCallback\r\n
0xb00017f1 | %1 - AfterHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f2 | %1 - Unhandled exception occurred. hr = %2\r\n
0xb00017f3 | %1 - State-Transition (%2)->(%3)\r\n
0xb00017f4 | %1 - EnableProfiling = [%2]\r\n
0xb00017f5 | %1 - Profile Dll = [%2]\r\n
0xb00017f6 | %1 - ProfilerCLSID = [%2]\r\n
0xb00017f7 | %1 - TaskHostHelper::SetProfilerSettings hr = %2\r\n
0xb00017f8 | %1 - File path = %2 : %3\r\n
0xb00017f9 | %1 - Parse Element: %2.\r\n
0xb00017fa | %1 - Parse Element Value = %2 with pwszLocalName = %3.\r\n
0xb00017fb | %1 - Parse HResult = %2\r\n
0xb00017fc | %1 - YUTHost: failed to GAC trusted assembly %2\r\n\r\n
0xb00017fd | %1 - UITaskHandler::Initialize. hr = %2\r\n
0xb00017fe | %1 - UITaskHandler::Disconnect done\r\n
0xb00017ff | %1 - UITaskHandler::GoBackground. hr = %2\r\n
0xb0001800 | %1 - UITaskHandler::GoForeground. hr = %2\r\n
0xb0001801 | %1 - Managed Framework Ready. Handling Pending Event:[%2]\r\n
0xb0001802 | %1 - HandlePendingEvents Start TaskId=%2\r\n
0xb0001803 | %1 - HandlePendingEvents Pause TaskId=%2\r\n
0xb0001804 | %1 - HandlePendingEvents Resume TaskId=%2\r\n
0xb0001805 | %1 - Waiting for Siblings...\r\n
0xb0001806 | %1 - Waiting for Siblings done. hr = %2\r\n
0xb0001807 | %1 - UITaskHandler::OnRuntimeHostReady TaskID:[%2]\r\n
0xb0001808 | %1 - UITaskHandler::OnRuntimeHostReady. Processed pending SystemKeyPress [%2]\r\n
0xb0001809 | %1 - UITaskHandler::OnRuntimeHostReady hr = %2\r\n
0xb000180a | %1 - UITaskHandler::RegistrationComplete hr = %2\r\n
0xb000180b | %1 - UITaskHandler::ConnectionComplete received\r\n
0xb000180c | %1 - UITaskHandler::ConnectionComplete hr = %2\r\n
0xb000180d | %1 - UITaskHandler::ProcessActivationData received, reason=%2\r\n
0xb000180e | %1 - UITaskHandler::ProcessActivationData hr = %2\r\n
0xb000180f | %1 - UITaskHandler::Show received. Direction:[%2]\r\n
0xb0001810 | %1 - Navigation in progress. Queuing up the Show\r\n
0xb0001811 | %1 - UITaskHandler::Show hr = %2\r\n
0xb0001812 | %1 - UITaskHandler::ShowInternal. Direction:[%2:NavigationDirection:]\r\n
0xb0001813 | %1 - UITaskHandler::ShowInternal. hr = %2\r\n
0xb0001814 | %1 - UITaskHandler::Hide received. Direction:[%2]\r\n
0xb0001815 | %1 - Navigation in progress. Cancelling Show and ignoring Hide\r\n
0xb0001816 | %1 - UITaskHandler::Hide hr = %2\r\n
0xb0001817 | %1 - UITaskHandler::NavigateTo received TaskID:[%2]\r\n
0xb0001818 | %1 - UITaskHandler::NavigateTo. hr = %2\r\n
0xb0001819 | %1 - UITaskHandler::NavigationComplete TaskID:[%2]\r\n
0xb000181a | %1 - UITaskHandler::NavigationComplete hr = %2\r\n
0xb000181b | %1 - UITaskHandler::NavigateAway received TaskID:[%2]\r\n
0xb000181c | %1 - Navigation interrupted since Task is closing\r\n
0xb000181d | %1 - Navigation in progress. Queuing up the NavigateAway\r\n
0xb000181e | %1 - UITaskHandler::NavigateAway hr = %2\r\n
0xb000181f | %1 - UITaskHandler::NavigateAwayInternal TaskID:[%2]\r\n
0xb0001820 | %1 - UITaskHandler::NavigateAwayInternal hr = %2\r\n
0xb0001821 | %1 - UITaskHandler::RequestClose called TaskID:[%2]\r\n
0xb0001822 | %1 - UITaskHandler::RequestClose hr = %2\r\n
0xb0001823 | %1 - LaunchSession in progress. Cannot add another callback\r\n
0xb0001824 | %1 - UITaskHandler::LaunchSession hr = %2\r\n
0xb0001825 | %1 - LaunchChildTask in progress. Cannot add another callback\r\n
0xb0001826 | %1 - UITaskHandler::LaunchChildTask hr = %2\r\n
0xb0001827 | %1 - UITaskHandler::SetPauseOnLock[%2] called TaskID:[%3]\r\n
0xb0001828 | %1 - UITaskHandler::SetPauseOnLock hr = %2\r\n
0xb0001829 | %1 - UITaskHandler::Close received TaskID:[%2]\r\n
0xb000182a | %1 - UITaskHandler::Close hr = %2\r\n
0xb000182b | %1 - UITaskHandler::SystemKeyPressed received: [%2]\r\n
0xb000182c | %1 - UITaskHandler::SystemKeyPressed processed\r\n
0xb000182d | %1 - UITaskHandler::SystemKeyPressed pending. Will be processed on RuntimeHost ready\r\n
0xb000182e | %1 - UITaskHandler::LaunchChildTaskComplete received with result %2\r\n
0xb000182f | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001830 | %1 - UITaskHandler::LaunchSessionComplete received with result %2\r\n
0xb0001831 | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001832 | %1 - OrientationChanged NewOrientation=%2\r\n
0xb0001833 | %1 - OrientationChange received before RuntimeHostTask is set\r\n
0xb0001834 | %1 - SetSupportedOrientations. SupportedOrientations:[%2]. hr = %3\r\n
0xb0001835 | %1 - GetSupportedOrientations. SupportedOrientations[%2]. hr = %3\r\n
0xb0001836 | %1 - GetCurrentOrientation. CurrentOrientation[%2]. hr = %3\r\n
0xb0001837 | %1 - UITaskHandler::ReplaceTouchEndpoint hr = %2\r\n
0xb0001838 | %1 - UITaskHandler::ReplaceTextEndpoint hr = %2\r\n
0xb0001839 | %1 - UITaskHandler::Get Task State. StateSize[%2]. hr = %3\r\n
0xb000183a | %1 - UITaskHandler::Set Task State. StateSize[%2]. hr = %3\r\n
0xb000183b | %1 - UITaskHandler::OnObscurityChange[%2]. hr = %3\r\n
0xb000183c | %1 - UITaskHandler::OnLockScreenVisibilityChange[%2]. hr = %3\r\n
0xb000183d | %1 - UITaskHandler::OnSipVisibilityChange[%2]. hr = %3\r\n
0xb000183e | %1 - UITaskHandler::OnShowAnimationComplete\r\n
0xb000183f | %1 - UITaskHandler::Window.Visible property changed [%2]\r\n
0xb0001840 | %1 - FreezeHost event triggered\r\n
0xb0001841 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001842 | %1 - CancelTask TaskId=%2\r\n
0xb0001843 | %1 - OnHostPausing\r\n
0xb0001844 | %1 - OnHostPausing failed with hr = %2\r\n
0xb0001845 | %1 - OnHostPaused\r\n
0xb0001846 | %1 - OnHostPaused failed with hr = %2\r\n
0xb0001847 | %1 - FreezeHost event triggered\r\n
0xb0001848 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001849 | %1 - CancelTask received while executing in background\r\n
0xb000184a | %1 - CancelTask received. Ignoring since this is a valid transition only when running in background\r\n
0xb000184b | %1 - CancelTask hr = %2\r\n
0xb000184c | %1 - TPA entry: %2\\%3%4;\r\n
0xb000184d | %1 - Platform Assemblies List: %2\r\n
0xb000184e | %1 - ParseManifestFile HResult = %2\r\n
0xb000184f | %1 - NotifyError ! Unable to disable NI optimizations\r\n
0xb0001850 | %1 - NotifyError ! Unable to set the debugger wait env variable\r\n
0xb0001851 | %1 - TestTrustedPath: %2\r\n
0xb0001852 | %1 - TestAppPaths: %2\r\n
0xb0001853 | %1 - NotifyError ! Failed to set the test settings\r\n
0xb0001854 | %1 - GetAppPaths failed with hr = %2\r\n
0xb0001855 | %1 - NotifyError ! message = %2, source = %3\r\n
0xb0001856 | %1 - NotifyError ! hr=%2. message = %3\r\n
0xb0001857 | %1 - GetIsoStoreAvailableFreeSpace hr = %2\r\n
0xb0001858 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb0001859 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb000185a | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185b | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185c | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb000185d | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb000185e | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb000185f | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb0001860 | %1 - GetQualifiedMutexName returned:[%2]. AllowedMutexCount:[%3]\r\n\r\n
0xb0001861 | %1 - XcpHost::Start() failed with hr = %2\r\n
0xb0001862 | %1 - Shutting down the SL runtime...\r\n
0xb0001863 | %1 - Calling into XcpHost::Pausing %2\r\n
0xb0001864 | %1 - XcpHost::Pausing %2\r\n
0xb0001865 | %1 - Calling into XcpHost::Pause %2\r\n
0xb0001866 | %1 - XcpHost::Pause %2\r\n
0xb0001867 | %1 - Calling into XcpHost::Resume %2\r\n
0xb0001868 | %1 - XcpHost::Resume %2\r\n
0xb0001869 | %1 - Calling into XcpHost::Resumed %2\r\n
0xb000186a | %1 - XcpHost::Resumed %2\r\n
0xb000186b | %1 - XcpHost::CompleteTask called TaskID:[%2]\r\n
0xb000186c | %1 - CompleteTask called when XcpTask is null. This likely indicates CompleteTask getting called twice\r\n
0xb000186d | %1 - Error in OnApplicationStarted\r\n
0xb000186e | %1 - Error in OnApplicationConstructing\r\n
0xb000186f | %1 - LaunchSession hr = %2\r\n
0xb0001870 | %1 - LaunchChildTask hr = %2\r\n
0xb0001871 | %1 - Raising Task.OnLaunching\r\n
0xb0001872 | %1 - Raised Task.OnLaunching\r\n
0xb0001873 | %1 - Raising Task.OnPause. PauseReason[%2]\r\n
0xb0001874 | %1 - Raised Task.OnPause\r\n
0xb0001875 | %1 - Raising Task.OnResume. IsExecutionContextPreserved[%2]\r\n
0xb0001876 | %1 - Raised Task.OnResume\r\n
0xb0001877 | %1 - Raising Task.OnRunningInBackground\r\n
0xb0001878 | %1 - Raised Task.OnRunningInBackground\r\n
0xb0001879 | %1 - Raising Task.OnCancel\r\n
0xb000187a | %1 - Raised Task.OnCancel\r\n
0xb000187b | %1 - Raising Task.OnHostDehydarting\r\n
0xb000187c | %1 - Raised Task.OnHostDehydarting\r\n
0xb000187d | %1 - Raising Task.OnNavigateTo\r\n
0xb000187e | %1 - Raised Task.OnNavigateTo\r\n
0xb000187f | %1 - Raising Task.OnNavigateAway\r\n
0xb0001880 | %1 - Raised Task.OnNavigateAway\r\n
0xb0001881 | %1 - Raising Task.OnShow\r\n
0xb0001882 | %1 - Raised Task.OnShow\r\n
0xb0001883 | %1 - Raising Task.OnHide\r\n
0xb0001884 | %1 - Raised Task.OnHide\r\n
0xb0001885 | %1 - Raising Task.OnSystemKeyPressed\r\n
0xb0001886 | %1 - Raised Task.OnSystemKeyPressed\r\n
0xb0001887 | %1 - Raising Task.OnChildTaskReturned\r\n
0xb0001888 | %1 - Raised Task.OnChildTaskReturned\r\n
0xb0001889 | %1 - Raising Task.OnObscurityChange\r\n
0xb000188a | %1 - Raised Task.OnObscurityChange\r\n
0xb000188b | %1 - Raising Task.OnLockScreenVisibilityChange\r\n
0xb000188c | %1 - Raised Task.OnLockScreenVisibilityChange\r\n
0xb000188d | %1 - Raising Task.OnClosing\r\n
0xb000188e | %1 - Raised Task.OnClosing\r\n
0xb000188f | %1 - RegisterAppCallbacks hr = %2\r\n
0xb0001890 | %1 - RegisterTaskCallbacks hr = %2\r\n
0xb0001891 | %1 - TaskReadyToShow hr = %2\r\n
0xb0001892 | %1 - RequestCloseTask hr = %2\r\n
0xb0001893 | %1 - CompleteTask hr = %2\r\n
0xb0001894 | %1 - DestroyTaskCallbacks hr = %2\r\n
0xb0001895 | %1 - SetHostErrorCode hrHostError = %2, hr = %3\r\n
0xb0001896 | %1 - LaunchSession[%2] hr = %3\r\n
0xb0001897 | %1 - GetTaskState hr = %2\r\n
0xb0001898 | %1 - SetTaskState hr = %2\r\n
0xb0001899 | %1 - LaunchChildTask[%2] hr = %3\r\n
0xb000189a | %1 - GetTaskAppChromeHandle hr = %2\r\n
0xb000189b | %1 - SetTaskPauseOnLock hr = %2\r\n
0xb000189c | %1 - SetHostObscurity[%2] hr = %3\r\n
0xb000189d | %1 - Entering Modal state\r\n
0xb000189e | %1 - Exiting Modal state hr = %2\r\n
0xb000189f | %1 - NotifyError: message=%2, source=%3\r\n
0xb00018a0 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb00018a1 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb00018a2 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a3 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a4 | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb00018a5 | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb00018a6 | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb00018a7 | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb00018a8 | %1 - Raising Task.OnRefresh\r\n
0xb00018a9 | %1 - Raised Task.OnRefresh\r\n
0xb00018aa | %1 - UITaskHandler::RequestNavigateBack called TaskID:[%2]\r\n
0xb00018ab | %1 - UITaskHandler::RequestNavigateBack hr = %2\r\n
0xb00018ac | %1 - RequestNavigateBack hr = %2\r\n
0xb00018ad | %1 - UITaskHandler::SetFullScreen[%2] called TaskID:[%3]\r\n
0xb00018ae | %1 - UITaskHandler::SetFullScreen hr = %2\r\n
0xb00018af | %1 - SetTaskFullScreen hr = %2\r\n
0xb00018b0 | %1 - Raising Task.OnApplicationLayerChange\r\n
0xb00018b1 | %1 - Raised Task.OnApplicationLayerChange\r\n
0xb00018b2 | %1 - Raising Task.OnRequestOverlayStateChange. State=%2\r\n
0xb00018b3 | %1 - Raised Task.OnRequestOverlayStateChange\r\n
0xb00018b4 | %1 - ApplicationLayerChanged NewApplicationLayer=%2\r\n
0xb00018b5 | %1 - ApplicationLayerChange received before RuntimeHostTask is set\r\n
0xb00018b6 | %1 - AgTaskHandler::LaunchSession hr = %2\r\n
0xb00018b7 | %1 - AgTaskHandler::LaunchChildTask hr = %2\r\n
0xb00018b8 | %1 - GetSessionDisplayName. DisplayName=%2 hr = %3\r\n
0xb00018b9 | %1 - AgTaskHandler::ConnectionComplete received\r\n
0xb00018ba | %1 - AgTaskHandler::ConnectionComplete hr = %2\r\n
0xb00018bb | %1 - UITaskHandler::OnNavigationBarVisibilityChange[%2]. hr = %3\r\n
0xb00018bc | %1 - Raising Task.OnModernActivation\r\n
0xb00018bd | %1 - Raised Task.OnModernActivation\r\n
0xb00018be | %1 - UITaskHandler::LaunchModernChooser hr = %2\r\n
0xb00018bf | %1 - LaunchChildTask hr = %2\r\n
0xb00018c0 | %1 - LaunchModernChooser[%2] hr = %3\r\n
0xb00018c1 | %1 - TaskFirstPresentCompleted = %2\r\n
0xb00018c2 | %1 - UITaskHandler::FirstPresentCompleted called TaskID:[%2]\r\n
0xb00018c3 | %1 - UITaskHandler::FirstPresentCompleted hr = %2\r\n
0xb0001fa4 | AgHost - FrameworkView::Initialize HRESULT=%1\r\n
0xb0001fa5 | AgHost - FrameworkView::SetWindow HRESULT=%1\r\n
0xb0001fa6 | AgHost - FrameworkView::Load HRESULT=%1\r\n
0xb0001fa7 | AgHost - FrameworkView::Run HRESULT=%1\r\n
0xb0001fa8 | AgHost - FrameworkView::Uninitialize HRESULT=%1\r\n
0xb0001fa9 | AgHost - FrameworkView::OnActivated PreviousExecutionState=%1 ActivationKind=%2 HRESULT=%3\r\n
0xb0001faa | AgHost - FrameworkView::OnExiting HRESULT=%1\r\n
0xb0001fab | AgHost - FrameworkView::OnResuming HRESULT=%1\r\n
0xb0001fac | AgHost - FrameworkView::OnSuspending HRESULT=%1\r\n
0xb0001fae | AgHostSvcs - EmCancelTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001faf | AgHostSvcs - EmCreateTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb0 | AgHostSvcs - EmExitTaskHost HRESULT=%1\r\n
0xb0001fb1 | AgHostSvcs - EmPauseTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb2 | AgHostSvcs - EmResumeTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb3 | AgHostSvcs - EmSetTaskInstanceApplicationUri TaskID=%1 ApplicationUri=%2 HRESULT=%3\r\n
0xb0001fb4 | AgHostSvcs - EmSetTaskInstanceArguments TaskID=%1 HRESULT=%2\r\n
0xb0001fb5 | AgHostSvcs - EmSetTaskInstanceBackgroundTaskId TaskID=%1 BackgroundTaskID=%2 HRESULT=%3\r\n
0xb0001fb6 | AgHostSvcs - EmSetTaskInstanceNavigationPage TaskID=%1 NavigationPage=%2 HRESULT=%3\r\n
0xb0001fb7 | AgHostSvcs - EmStartTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb8 | AgHostSvcs - TaskCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fb9 | AgHostSvcs - TaskPaused TaskID=%1 HRESULT=%2\r\n
0xb0001fba | AgHostSvcs - TaskRunning TaskID=%1 HRESULT=%2\r\n
0xb0001fbb | AgHostSvcs - TaskRunningInBackground TaskID=%1 HRESULT=%2\r\n
0xb0001fbc | AgHostSvcs - TaskRunningInForeground TaskID=%1 HRESULT=%2\r\n
0xb0001fbd | AgHostSvcs - EmWaitForTaskInstanceCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fbe | AgHostSvcs - OnModernContractActivation TaskID=%1 HRESULT=%2\r\n
0xb0002008 | EEC: GetExtendedExecutionBroker ProcessId=%1 HRESULT=%2\r\n
0xb0002009 | EEC: RegisterRevokedHandler ProcessId=%1 HRESULT=%2\r\n
0xb000200a | EEC: RequestExtendedExecution ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200b | EEC: ExtensionRevokedCallback ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200c | EEC: CompleteExtendedExecution ProcessId=%1 HRESULT=%2\r\n
0xb000206c | ODB: LaunchTask - UserSid: %1 SessionId: %2 PackageFullName: %3 EntryPoint: %4 WorkItemId: %5 HRESULT: %6.\r\n
0xb000206d | ODB: CancelTask - UserSid: %1 SessionId: %2 WorkItemId: %3 RudeTerminate: %4 CancellationReason: %5 HRESULT: %6.\r\n
0xb000206e | ODB: BeforeTaskActivated - WorkItemId: %1 PsmKey: %2 HostJobType: %3 HRESULT: %4.\r\n
0xb000206f | ODB: TaskActivated - WorkItemId: %1 TaskInstanceId: %2 PsmKey: %3 HRESULT: %4.\r\n
0xb0002070 | ODB: TaskCompleted - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002071 | ODB: TaskCanceled - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002072 | ODB: Timeout in WaitForWnfStateQuiescentTimeout.\r\n
0xb0002073 | ODB: CancelBackgroundTaskWithWnf WorkItemId: %1.\r\n
0xb0002710 | %1\r\n
0xb0002711 | %1: %2\r\n
0xb0002712 | *** ExecFailFast ***   %1\r\n
0xb000271a | PreInstallTaskPolicy: Activate task for User = %1 HRESULT = %2\r\n
0xb000271b | PreInstallTaskPolicy: BiActivate WorkItemId = %1 for user = %2, PackageFullName = %3, EntryPoint = %4, HRESULT = %5\r\n
0xb0010205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1' WorkItemId='%2;' CallbackId='%3' HostId='%5' ResourceSetId='%6'.\r\n
0xb0010206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1' HostId='%3' ResourceSetId='%4'.\r\n
0xd0000001 | Resumed\r\n
0xd0000002 | Quiescing\r\n
0xd0000003 | Quiesced\r\n
0xd0000004 | Frozen\r\n
0xd0000005 | Dehydrated\r\n
0xd0000006 | Terminated\r\n
0xd0000007 | Resumed\r\n
0xd0000008 | Suspending\r\n
0xd0000009 | Suspended\r\n
0xd000000a | Terminated\r\n
0xd000000b | NotBackground\r\n
0xd000000c | MixedHost\r\n
0xd000000d | PureHost\r\n
0xd000000e | SystemHost\r\n
0xd000000f | InvalidType\r\n
0xd0000010 | Permitted\r\n
0xd0000011 | Buffered\r\n
0xd0000012 | Dropped\r\n
0xd0000013 | InvalidType\r\n
0xd0000014 | Invalid\r\n
0xd0000015 | ForegroundApp\r\n
0xd0000016 | Cbe\r\n
0xd0000017 | ForegroundAgent\r\n
0xd0000018 | GbaPeriodic\r\n
0xd0000019 | GbaIdle\r\n
0xd000001a | BackgroundAudio\r\n
0xd000001b | BackgroundWorker\r\n
0xd000001c | Voip\r\n
0xd000001d | Oem\r\n
0xd000001e | Invalid\r\n
0xd000001f | Started\r\n
0xd0000020 | Paused\r\n
0xd0000021 | Resumed\r\n
0xd0000022 | MovedToBackground\r\n
0xd0000023 | RunUnderLock\r\n
0xd0000024 | Invalid\r\n
0xd0000025 | OK\r\n
0xd0000026 | Abort\r\n
0xd0000027 | Unexpected\r\n
0xd0000028 | ExceededRuntime\r\n
0xd0000029 | ResourcesSeized\r\n
0xd000002a | Paused\r\n
0xd000002b | Resumed\r\n
0xd000002c | ScreenLock\r\n
0xd000002d | ScreenUnlocked\r\n
0xd000002e | MovedToBackground\r\n
0xd000002f | CbeExitTimeout\r\n
0xd0000030 | CbeExitBatterySaver\r\n
0xd0000031 | CbeExitParallelAgentPolicy\r\n
0xd0000032 | CbeExitResourcesUnavailable\r\n
0xd0000033 | CbeExitControlPanel\r\n
0xd0000034 | CbeExitBandwidthSavings\r\n
0xd0000035 | HeadlessHost\r\n
0xd0000036 | TaskHost\r\n
0xd0000037 | XcpHost\r\n
0xd0000038 | TaskHostSvcs\r\n
0xd0000039 | TaskHostUnitTests\r\n
0xd000003a | HOST_CREATED\r\n
0xd000003b | HOST_INITIALIZED\r\n
0xd000003c | HOST_RUNNING\r\n
0xd000003d | STARTING_TASK\r\n
0xd000003e | REHYDRATING_TASK\r\n
0xd000003f | HOST_READY\r\n
0xd0000040 | HOST_PAUSING\r\n
0xd0000041 | PAUSING_TASK\r\n
0xd0000042 | PAUSED_TASK\r\n
0xd0000043 | HOST_PAUSED\r\n
0xd0000044 | RESUMING_TASK\r\n
0xd0000045 | HOST_GOING_IN_BACKGROUND\r\n
0xd0000046 | TASK_GOING_IN_BACKGROUND\r\n
0xd0000047 | HOST_IN_BACKGROUND\r\n
0xd0000048 | TASK_GOING_IN_FOREGROUND\r\n
0xd0000049 | GRACEFULLY_DEHYDRATING_HOST\r\n
0xd000004a | HOST_VISIBLE\r\n
0xd000004b | HOST_HIDDEN\r\n
0xd000004c | HOST_FROZEN\r\n
0xd000004d | HOST_THAWED\r\n
0xd000004e | HOST_EXITING\r\n
0xd000004f | HOST_ERROR\r\n
0xd0000050 | Direction_Forward\r\n
0xd0000051 | Direction_Backward\r\n
0xd0000052 | Direction_ForceSize\r\n
0xd0000053 | Resumed\r\n
0xd0000054 | Pausing\r\n
0xd0000055 | Paused\r\n
0xd0000056 | Dehydrated\r\n
0xd0000057 | Completed\r\n
0xd0000058 | none\r\n
0xd0000059 | launch\r\n
0xd000005a | debug\r\n
0xd000005b | task completion\r\n
0xd000005c | dependency\r\n
0xd000005d | multi-view\r\n
0xd000005e | Waiting\r\n
0xd000005f | CompletedWithResult\r\n
0xd0000060 | CompletedWithNoResult\r\n
0xd0000061 | Foreground\r\n
0xd0000062 | Lock\r\n
0xd0000063 | Overlay\r\n
0xd0000064 | ModernForeground\r\n
0xd0000065 | Pausing\r\n
0xd0000066 | PausingLowPri\r\n
0xd0000067 | Paused\r\n
0xd0000068 | PausedHighPri\r\n
0xd0000069 | PausedDNK\r\n
0xd000006a | Frozen\r\n
0xd000006b | FrozenHighPri\r\n
0xd000006c | FrozenDNK\r\n
0xd000006d | FrozenDNCS\r\n
0xd000006e | LockScreen\r\n
0xd000006f | Overlay\r\n
0xd0000070 | 11\r\n
0xd0000071 | CalendarAsChild\r\n
0xd0000072 | VideoTranscode\r\n
0xd0000073 | CBE\r\n
0xd0000074 | GenericExtendedExecution\r\n
0xd0000075 | ModernForegroundExtended\r\n
0xd0000076 | TaskCompletionHighPriority\r\n
0xd0000077 | ModernForegroundLarge\r\n
0xd0000078 | ShellCustom1\r\n
0xd0000079 | ShellCustom2\r\n
0xd000007a | ShellCustom3\r\n
0xd000007b | ShellCustom4\r\n
0xd000007c | Composer\r\n
0xd000007d | DebugModeForeground\r\n
0xd000007e | ComponentTarget\r\n
0xd000007f | PiP\r\n
0xd0000080 | Balloon\r\n
0xd0000081 | Invalid\r\n
0xd0000082 | Unevaluated\r\n
0xd0000083 | EvaluationPending\r\n
0xd0000084 | Evaluated\r\n

### 10.0.17134.1, 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x10000006 | ExecMan\r\n
0x10000009 | TaskHost\r\n
0x1000000d | Sqm\r\n
0x1000000f | Lifetime Manager\r\n
0x10000010 | ForegroundManager\r\n
0x10000011 | Background Manager\r\n
0x10000012 | Production Circular\r\n
0x10000013 | Production Critical\r\n
0x10000014 | SelfHost Circular\r\n
0x10000015 | SelfHost Critical\r\n
0x10000016 | DevPlat Circular\r\n
0x10000017 | VOIP\r\n
0x1000001b | Activation Manager\r\n
0x1000001c | AgHost\r\n
0x10000020 | Telemetry\r\n
0x10000021 | ExtendedExecutionClient\r\n
0x10000022 | OnDemandBroker\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000007 | Resume\r\n
0x30000008 | Suspend\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-AppModelExecEvents\r\n
0xb0000064 | DepMgr: Removed suspension group from the graph, PsmKey=%1\r\n
0xb0000065 | Not set app %1 into halted state because it should wait for other apps in the package halted first\r\n
0xb0000066 | Not set app %1 into halted state because other app in the package have not finished quiescing\r\n
0xb0000067 | Not terminate app %1, because target app %2 state = %3\r\n
0xb0000068 | Updated current dependency graph (Removal : %1) with Source %2 and Target %3 for type %4 in return %5\r\n
0xb0000069 | Default time for %1 overridden to %2 ms\r\n
0xb000006a | Creating hang report\r\n
0xb000006b | Window %1 is hung in foreground\r\n
0xb000006c | Window %1 is no longer hung in foreground\r\n
0xb000006d | Waiting for WER reporting to finish on app %1\r\n
0xb000006e | Hang reporting finished on app %1.  App termination status: %2\r\n
0xb000006f | Hung reporting finished on window %1 with result %2\r\n
0xb0000070 | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb0000071 | _SubmitActivationHangWerReport(stop): Aumid=%1, result=%2\r\n
0xb0000072 | _UnregisterForStateChanges: fPackageLevel=%1, HRESULT is %2. Cookie is %3\r\n
0xb0000073 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000074 | Canceled launch grace timer, PsmKey=%1\r\n
0xb0000075 | _InitializeLaunchGraceContext: Aumid=%1, fExtendedLaunch=%2, fEventExists=%3\r\n
0xb0000076 | App %1 successfully launched and its launch grace period expired: removing suspend exemption\r\n
0xb0000077 | Forcefully terminating app, Aumid=%1 flags=%2, reason=%3\r\n
0xb0000078 | CheckTerminationBeforeSwitch: Should terminate: %1, Aumid=%2, HRESULT=%3, reason=%4, fIsMisbehaving=%5\r\n
0xb0000079 | Termination requested for %1 - flags %2\r\n
0xb000007a | Failing TerminateApp due to pending task completions: %1\r\n
0xb000007b | Terminating %1 immediately\r\n
0xb000007c | Uninstalling background work items for %1\r\n
0xb000007d | Termination of %1 scheduled for %2 ms in future\r\n
0xb000007e | Sent window message to the default immersive browser with HRESULT %1\r\n
0xb000007f | Attempting to terminate app %1 prior to new app launch due to pending termination\r\n
0xb0000080 | EvaluateAndTerminatePid: PID: %1. HRESULT: %2. Package State: %3\r\n
0xb0000081 | Exempting application %1 from suspend while it is being launched\r\n
0xb0000082 | Exemption manager %1 is requesting a higher minimum priority %2 for %3\r\n
0xb0000083 | Debug mode is enabled for %1, so it will run at %2 priority\r\n
0xb0000084 | Handling logoff, %1 will run at %2 priority\r\n
0xb0000085 | Throttling has been disabled, so %1 will run at %2 priority\r\n
0xb0000086 | Suspend denied due to new key debounce, PsmKey=%1\r\n
0xb0000087 | Suspend denied due to debug mode, PsmKey=%1\r\n
0xb0000088 | Not suspending application %1 due to exemption %2\r\n
0xb0000089 | _EvaluateAndSuspendApplication: PsmKey=%1, fIsSuspendAllowed=%2, HRESULT=%3\r\n
0xb000008a | _ReevaluatePolicy: Ignoring debug mode app, PsmKey=%1\r\n
0xb000008b | ManagePreExistingApps(start)\r\n
0xb000008c | ManagePreExistingApps: PsmKey=%1, Aumid=%2, hr=%3\r\n
0xb000008d | ManagePreExistingApps(stop)\r\n
0xb000008e | RequestSuspendTimeout called for application %1 and timeout %2\r\n
0xb000008f | Debug mode enabled, PkgFamilyName=%1\r\n
0xb0000090 | Debug mode disabled, PkgFamilyName=%1\r\n
0xb0000091 | Set Package %1, Timeout to %2\r\n
0xb0000092 | ResumeDebugModePackage(start): package=%1\r\n
0xb0000093 | ResumeDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000094 | SuspendDebugModePackage(start): package=%1\r\n
0xb0000095 | SuspendDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000096 | MultiAppSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000097 | MultiAppSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb0000098 | MultiPackageSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000099 | MultiPackageSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009a | MultiPackageSuspendAndPendTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb000009b | MultiPackageSuspendAndPendTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009c | TerminateSync(start): PsmKey=%1, type=%2, reason=%3\r\n
0xb000009d | TerminateSync(stop): PsmKey=%1, hrLogReason=%2, hrTermination=%3\r\n
0xb000009e | TerminatePackageSync(start): Package=%1, type=%2, reason=%3\r\n
0xb000009f | TerminatePackageSync(stop): Package=%1, fPlmKnowsPackage=%2, HRESULT=%3\r\n
0xb00000a0 | _TerminateAllSuspendedApplications(start)\r\n
0xb00000a1 | _TerminateAllSuspendedApplications(stop): HRESULT=%1\r\n
0xb00000a2 | Application %1 is blocking Connected Standby\r\n
0xb00000a3 | Exiting Connected Standby\r\n
0xb00000a4 | All packages have been suspended or terminated. Notify PDC. Call to PdcNotificationClientAcknowledge() returned %1\r\n
0xb00000a5 | Kernel State Change Callback: There were %1 PIDs present in the callback data\r\n
0xb00000a6 | Kernel State Change Callback: The state source was %1\r\n
0xb00000a7 | PDC_CONTROL_ABORT: PdcNotificationClientAcknowledge(STATUS_SUCCESS) returned %1\r\n
0xb00000a8 | Not terminating application %1 in _EvaluateAndTerminateApplication because it contains a running IImmersiveApplication\r\n
0xb00000a9 | Not terminating application %1 in _EvaluateAndTerminateApplication because it is a long running app\r\n
0xb00000aa | Not terminating application %1 in _EvaluateAndTerminateApplication due to pending task completion\r\n
0xb00000ab | Not terminating application %1 in _EvaluateAndTerminateApplication due to Launch Grace\r\n
0xb00000ac | Not terminating application %1 in _EvaluateAndTerminateApplication due to debug mode\r\n
0xb00000ad | Not terminating application %1 in _EvaluateAndTerminateApplication due to application had already been terminated\r\n
0xb00000ae | _EvaluateAndTerminateApplication: Skipping child suspension group, PsmKey=%1\r\n
0xb00000af | An empty application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b0 | Parent allowed suspension for child app, childPsmKey=%1\r\n
0xb00000b1 | GroupChildWithParent: ChildPsmKey=%1, HRESULT=%2\r\n
0xb00000b2 | Call a command line '%1' to notify default browser with result %2\r\n
0xb00000b3 | Read executable path from registry with result %1\r\n
0xb00000b4 | Application %1 was added to PLM Data Store and registering for PSM notification\r\n
0xb00000b5 | Resume the PPLE app %1 when receiving the PSM new key notification\r\n
0xb00000b6 | An orphaned prereq application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b7 | Not terminating dependent application %1 in _EvaluateAndTerminateDependentApplication due other dependency applications\r\n
0xb00000b8 | _EvaluateAndTerminateSourceApplication: Aumid=%1, exemption=%2\r\n
0xb00000b9 | An force termination exemption Application was detected. Setting pending termination for application %1\r\n
0xb00000ba | StateMgr: State queued, PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000bb | StateMgr: OnApplicationStarted set to active, PsmKey=%1\r\n
0xb00000bc | StateMgr: OnApplicationStarted finished, PsmKey=%1, HRESULT=%2\r\n
0xb00000bd | StateMgr: App's current state has changed, PsmKey=%1, state=%2\r\n
0xb00000be | StateMgr: OnApplicationTerminated(start), PsmKey=%1\r\n
0xb00000bf | StateMgr: Application terminated signaled, PsmKey=%1\r\n
0xb00000c0 | StateMgr: OnApplicationTerminated(stop), PsmKey=%1\r\n
0xb00000c1 | StateMgr: GetTerminateSyncData, PsmKey=%1, hr=%2\r\n
0xb00000c2 | StateMgr: _ProcessStateQueue(start): PsmKey=%1, state=%2\r\n
0xb00000c3 | StateMgr: _ProcessStateQueue(stop): PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000c4 | StateMgr: Queue's pause state has changed to %2, PsmKey=%1\r\n
0xb00000c5 | StateMgr: App's committed state has changed, PsmKey=%1, state=%2\r\n
0xb00000c6 | Enabling debug mode on package %1\r\n
0xb00000c7 | Disabling debug mode on package %1\r\n
0xb00000c8 | Suspending package %1 via debug API. HRESULT: %2\r\n
0xb00000c9 | Resuming package %1 via debug API. HRESULT: %2\r\n
0xb00000ca | Terminating package %1 via debug API. HRESULT: %2\r\n
0xb00000cb | Default time for %1 overridden to %2 ms\r\n
0xb00000cc | ReportActivationHangSync: Halt application Aumid=%1, result=%2\r\n
0xb00000cd | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb00000ce | _SubmitActivationHangWerReport(stop): Aumid=%1 canceled(%2) result=%3\r\n
0xb00000cf | PLM doesn't swap out application %1 due to its swap state %2\r\n
0xb00000d0 | PLM termination policy started on background thread because application %1 failed to outswap\r\n
0xb00000d1 | PLM termination policy finished. Outswapping returned status %1\r\n
0xb00000d2 | PLM memory policy will be aggressive because this is a disconnected session\r\n
0xb00000d3 | PLM termination policy start\r\n
0xb00000d4 | PLM termination policy stop\r\n
0xb00000d5 | PLM termination policy triggered by in use memory of %1 MiB\r\n
0xb00000d6 | PLM termination policy triggered by commit charge of %1 MiB\r\n
0xb00000d7 | MemoryPolicyWatcherTerminateCommitCharge\r\n
0xb00000d8 | PLM empty policy triggered by in use memory of %1 MB\r\n
0xb00000d9 | PLM memory policy does not allow termination of application %1 for reason %2\r\n
0xb00000da | PLM memory policy allows termination of application %1\r\n
0xb00000db | Application %1 was hidden %2 seconds ago\r\n
0xb00000dc | Application %1 is the clipboard owner\r\n
0xb00000dd | PLM empty policy start\r\n
0xb00000de | PLM empty policy ignoring application %1 with error code %2\r\n
0xb00000df | PLM empty policy finished after emptying %1 MiB\r\n
0xb00000e0 | PLM termination policy enumerated %1 applications\r\n
0xb00000e1 | PLM memory policy chose application %1 as its termination candidate, over old candidate application %2\r\n
0xb00000e2 | PLM memory policy will terminate application %1 with memory size %2 MiB and score %3\r\n
0xb00000e3 | PLM memory policy received MemWatcher event\r\n
0xb00000e4 | PLM memory policy received MemWatcher event\r\n
0xb00000e5 | Package exemption manager denied suspend for %1.  Ref counts are LAUNCH=%2, PSMREG=%3, PSMPENDING=%4\r\n
0xb00000e6 | Package Exemption Manager: ReferenceAdded:%1, %2 ref to application %3. The ref counts are now LAUNCH=%4, PSMREG=%5, and PSMREGPENDING=%6\r\n
0xb00000e7 | Package %1 added to the package data store\r\n
0xb00000e8 | Resetting priority to unpause the suspension group, PsmKey=%1\r\n
0xb00000e9 | Changed the priority of %1 to %2\r\n
0xb00000ea | AllowServiceOfPackages(start): cPackages=%1, fNotifyBi=%2\r\n
0xb00000eb | AllowServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ec | FinishedServiceOfPackages(start): cPackages=%1\r\n
0xb00000ed | FinishedServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ee | AllowUninstallOfPackage(start): package=%1\r\n
0xb00000ef | AllowUninstallOfPackage(stop): package=%1, HRESULT=%2\r\n
0xb00000f0 | Forcefully terminating misbehaving app %1 due to activation failure %2\r\n
0xb00000f1 | App %1: Change = %2\r\n
0xb00000f2 | PsmKey %1 has state %2\r\n
0xb00000f3 | Changing app state through BI, PsmKey=%1, state=%2 terminate action=%3\r\n
0xb00000f4 | Changing the package state of %1 through BI to %2\r\n
0xb00000f5 | OnAfterQuiescing: Quiesce began for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f6 | _CompleteQuiesceHelper: Queued termination for timed-out PsmKey %1\r\n
0xb00000f7 | Quiesce completed for PsmKey=%1, reason=%2, suspendTrigger=%3\r\n
0xb00000f8 | Suspend trigger updated for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f9 | ExtendQuiesceTimeout: PsmKey=%1, request=%2 ms, HRESULT=%3\r\n
0xb00000fa | _CompleteQuiesceHelper: Ignore timed-out PsmKey %1 as is being debugged\r\n
0xb00000fb | ResumeHelper: Application resume(start), PsmKey=%1, reason=%2\r\n
0xb00000fc | ResumeHelper: Application resume(stop), PsmKey=%1, reason=%2, HRESULT=%3\r\n
0xb00000fd | Resume reason updated for PsmKey=%1, reason=%2\r\n
0xb00000fe | RPC 0->1 transition detected for %1\r\n
0xb00000ff | RPC exemption was granted for application %1. KernelRequest Value: %2. Runaway RPC: %3.  RPC Debounce %4\r\n
0xb0000100 | RPC debounce received for package %1\r\n
0xb0000101 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000102 | Application %1 termination is blocked. PreserverProcessRequest = %2, TaskCompletionCategory = %3\r\n
0xb0000103 | PdcSystem activation (Activate = %1). Result = %2\r\n
0xb0000104 | NetworkAudio entries: %1, IsNetworkReferenced: %2\r\n
0xb0000105 | App %1 is Sharing\r\n
0xb0000106 | Share %1 has started in app %2\r\n
0xb0000107 | Share %1 in app %2 has stopped\r\n
0xb0000108 | Queued termination reason updated for PsmKey=%1, reason=%2\r\n
0xb0000109 | ClearTerminationTypesForForgottenPackage(start): PkgFamilyName=%1\r\n
0xb000010a | Cleared termination type for forgotten app, Aumid=%1, HRESULT=%2\r\n
0xb000010b | ClearTerminationTypesForForgottenPackage(stop): PkgFamilyName=%1, HRESULT=%2\r\n
0xb000010c | Writing to termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010d | Reading termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010e | _ExtendForResourceStarvation: PsmKey=%1, TimerType=%2, newRelativeExpirationTimeMs=%3, ElapsedMs=%4, CpuRunningMs=%5, CpuReadyMs=%6, IoNormalMs=%7\r\n
0xb000010f | Foreground resume delay %1 milliseconds\r\n
0xb0000110 | Suspend allowed for %1 - Session not active\r\n
0xb0000111 | Suspend denied due to a visible window or visibility debounce, PsmKey=%1\r\n
0xb0000112 | Suspend denied for %1 - UserRequest non-zero\r\n
0xb0000113 | Suspend denied for %1- failure %2\r\n
0xb0000114 | OnWindowChanged: Aumid=%1, Hwnd=%2, change=%3, fDeferredVisibility=%4, HRESULT=%5\r\n
0xb0000115 | Starting Session Idle Debounce\r\n
0xb0000116 | Session is active\r\n
0xb0000117 | Session is idle\r\n
0xb0000118 | PlmGetPackageFullNameFromAppId, Aumid=%1, HRESULT=%2\r\n
0xb0000119 | Session idle state change -- calling _ReevaluatePolicy\r\n
0xb000011a | RegisterForActivationStateChanges: Act:%1 App:%2 HRESULT is %3. Cookie is %4\r\n
0xb000011b | UnregisterForActivationStateChanges: Cookie is %1\r\n
0xb000011c | Can Auto Terminate app %1 %2\r\n
0xb000011d | TerminateApplicationBeforeActivation(start): Aumid=%1\r\n
0xb000011e | TerminateApplicationBeforeActivation: wait for terminate, Aumid=%1, HRESULT=%2\r\n
0xb000011f | TerminateApplicationBeforeActivation(stop): Aumid=%1, reason=%2, HRESULT=%3\r\n
0xb0000120 | s_SuspendPackagesAtLogOff(start)\r\n
0xb0000121 | s_SuspendPackagesAtLogOff(stop): HRESULT=%1\r\n
0xb0000122 | StateMgr: OnApplicationStarted still halted, PsmKey=%1\r\n
0xb0000123 | Added Task Completion under %1 for application %2\r\n
0xb0000124 | Removed Task Completion under %1 for application %2\r\n
0xb0000125 | Illegal state change happened to App: %1\r\n
0xb0000126 | EnableDebugMode failed: %1\r\n
0xb0000127 | DisableDebugMode: RoDisableDebuggingForPackage failed with result %1\r\n
0xb0000128 | DisableDebugMode: OnDebugModeDisabled failed with result %1\r\n
0xb0000129 | DisableDebugMode: Enabling activation timeout failed with result %1\r\n
0xb000012a | DisableDebugMode failed: %1\r\n
0xb000012b | Couldn't open process: %1\r\n
0xb000012c | PLM failed to process a hang for window %1 with error code %2\r\n
0xb000012d | PLM outswap application %1 failed to invoke with error code %2\r\n
0xb000012e | PLM couldn't find any process for application %1, and handle it as non-large app\r\n
0xb000012f | PLM failed to decide application %1 is large or not with error code %2\r\n
0xb0000130 | PLM empty policy failed to process application %1 with error code %2.  Ignoring the application\r\n
0xb0000131 | PLM empty policy failed to empty application %1 with error code %2\r\n
0xb0000132 | PLM failed to terminate application %1 as empty policy with error code %2\r\n
0xb0000133 | PLM empty policy failed to enumerate applications with error code %1\r\n
0xb0000134 | PLM termination policy skipping application %1, which is not registered with PLM\r\n
0xb0000135 | PLM memory policy failed to queue work with error code %1\r\n
0xb0000136 | GetPackageData called on a Package %1, which is not in the PLM Package Data Store\r\n
0xb0000137 | ERROR: Failed to set priority to %1, PsmKey=%2, NTSTATUS=%3\r\n
0xb0000138 | AllowServiceOfPackages: Failed to terminate package=%1, type=%2, HRESULT=%3\r\n
0xb0000139 | _CheckServicingPackages: Failed to enumerate app, PsmKey=%1, HRESULT=%2\r\n
0xb000013a | _CheckServicingPackages: Failed to enumerate package, PkgFullName=%1, HRESULT=%2\r\n
0xb000013b | GetImmersiveApplicationCount failed with error code %1\r\n
0xb000013c | Background workitems were force terminated, PsmKey=%1\r\n
0xb000013d | ChangeApplicationBiState failed: %1\r\n
0xb000013e | Background workitems for package %1 were force terminated\r\n
0xb000013f | ChangePackageBiState failed: %1\r\n
0xb0000140 | ApplicationProcesses failed to track process ID %1 with error code %2\r\n
0xb0000141 | OnBeforeQuiescing: Failed to allocate memory for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000142 | OnAfterQuiescing: Quiesce failed for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000143 | ERROR: _CompleteQuiesceHelper: Failed to terminate timed-out PsmKey %1 with result %2\r\n
0xb0000144 | ERROR: QuiesceHelper: App forgotten while still Quiescing, PsmKey=%1, suspendTrigger=%2\r\n
0xb0000145 | Failed to query the wake counters associated with application %1. NTSTATUS: %2\r\n
0xb0000146 | _AllAppSyncOperationHelper: Failed to allocate memory for PsmKey=%1, HRESULT=%2\r\n
0xb0000147 | _MultiAppSyncOperationHelper: Failed to perform operation on PsmKey=%1, HRESULT=%2\r\n
0xb0000148 | _MultiAppSyncOperationHelper: Failed in wait, HRESULT=%1\r\n
0xb0000149 | _MultiPackageSyncOperationHelper: Failed to enumerate PsmKey=%1, HRESULT=%2\r\n
0xb000014a | _MultiPackageSyncOperationHelper: Failed to find package in data store, PkgFullName=1%, HRESULT=%2\r\n
0xb000014b | Failed to suspend and terminate apps, cPsmKeys=%1\r\n
0xb000014c | Could not initialize an extended launch grace period for app %1 with HRESULT %2 -- falling back to normal launch grace\r\n
0xb000014d | App %1 failed to show a window after launch. Will attempt to terminate it now\r\n
0xb000014e | Failed to get a window for an app; assuming that the app's window is not hung, Aumid=%1, HRESULT=%2\r\n
0xb000014f | Failed to query hidden time for visibility debounce for app %1 with error code %2\r\n
0xb0000150 | _StartNewKeyDebounce: Error Result=%2, PsmKey=%1\r\n
0xb0000151 | StartTrackingNewApp failed with %1. The application launch is not protected and the app might potentially get suspended inappropriately\r\n
0xb0000152 | ERROR: Failed to enumerate exemption targets starting from PsmKey=%1\r\n
0xb0000153 | Failed to enumerate existing applications from PSM with error code %1\r\n
0xb0000154 | PsmRegisterApplicationNotification failed for application %1 with status %2.  PLM's cache says that the application's registration is: %3\r\n
0xb0000155 | ERROR: Failed to enumerate force termination targets starting from PsmKey=%1, HRESULT=%2\r\n
0xb0000156 | Application %1 failed to be added in PLM Data Store\r\n
0xb0000157 | Failed to initialize string to send app notification %1 state %2\r\n
0xb0000158 | Failed to initialize string to remove app %1\r\n
0xb0000159 | Failed to add %1 for application %2. The application doesn't have BTC_AUDIO background task capability\r\n
0xb000015a | Failed to initialize CmApi\r\n
0xb000015b | Task completion manager failed to add %1 to its sharing cache with error code %2\r\n
0xb000015c | ClearTerminationTypesForForgottenPackage: Failed to clear termination type for app, Aumid=%1, HRESULT=%2\r\n
0xb000015d | ERROR: Failed to schedule the visibility debounce, PsmKey=%1, HRESULT=%2\r\n
0xb000015e | OnWindowChanged ERROR: Failed to queue thread for Aumid=%1, Hwnd=%2, change=%3, HRESULT=%4\r\n
0xb000015f | ERROR: Failed to schedule deferred visibility timer, PsmKey=%1, HRESULT=%2\r\n
0xb0000160 | WaitOnBiNotifyNewSession HRBiNotifyNewSession=%1 HRBiNotifyNewUser=%2\r\n
0xb0000161 | RegisterKernelNotifications HRESULT=%1\r\n
0xb0000162 | TCExemptionManager CompleteInitialization HRESULT=%1\r\n
0xb0000163 | PlmActivationManager CompleteInitialization HRESULT=%1\r\n
0xb0000164 | Plm CSDiagnostics CompleteInitialization HRESULT=%1\r\n
0xb0000165 | Plm LogOff/LogOn Registration HRESULT=%1\r\n
0xb00001f9 | BM: Queued evaluate WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fa | BM: Evaluate returned WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fb | BM: TaskActivated WorkItem: %1 Instance: %2\r\n
0xb00001fc | BM: TaskCompleted WorkItem: %1 Instance: %2\r\n
0xb00001fd | BM: TaskCanceled WorkItem: %1 Instance: %2\r\n
0xb00001fe | BM: Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb00001ff | BM: TaskActivating WorkItem: %1 Instance: %2\r\n
0xb0000200 | BM: Enter %1\r\n
0xb0000201 | BM: Exit %1, HR=%2\r\n
0xb0000202 | BM: TerminateHost WorkItem: %1\r\n
0xb0000203 | BM: ResourceSet invalidated for WorkItem: %1 Instance: %2.  This usually means the host has crashed before a ResourceSet could be applied.\r\n
0xb0000204 | BM: OnAcquired ignoring invalid CallbackId (%1).\r\n
0xb0000205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1'; WorkItemId='%2;' CallbackId='%3'.\r\n
0xb0000206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1'.\r\n
0xb0000207 | BM: OnApplicationStateChanged returning State='%2' PsmKey='%1' HR='%3'.\r\n
0xb0000208 | BM: OnAcquired received for CallbackId: %1\r\n
0xb0000209 | BM: OnAcquired request ignored for CallbackId: %1\r\n
0xb000020a | BM: ActivateDeferredWorkItem WorkItem: %1\r\n
0xb000020b | BM: ActivateDeferredWorkItem discarded WorkItem: %1 because of Status: %2\r\n
0xb000020c | BM: Enter %1 WorkItem: %2\r\n
0xb000020d | BM: Enter %1 WorkItem: %2 TaskInstanceId: %3\r\n
0xb000020e | BM: Exit %1\r\n
0xb000020f | BM: Failed to load settings for event %1.\r\n
0xb0000210 | BM: Failed to load settings for event %1 with error %2.\r\n
0xb0000211 | BM: Failed to load policy for CLSID: %1, for EventType %2 with error %3.\r\n
0xb0000212 | BM: Failed to load the policies with error %1.\r\n
0xb0000213 | BM: Evaluate returned WorkItem: %3 EventType: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb0000214 | BM: TaskWallClockActive WorkItem: %1 Instance: %2\r\n
0xb0000215 | BM: TaskWallClockExpired WorkItem: %1 Instance: %2\r\n
0xb0000216 | BM: Policy returned HRESULT: %3 for WorkItem: %2 PsmKey: %1.\r\n
0xb0000217 | BM: Canceling task for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000218 | BM: Ignoring cancelation request (whitelisted) for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000219 | BM: Session(%1) started, session initialization returned %2.\r\n
0xb000021a | BM: Session(%1) ended.\r\n
0xb000021b | BM: Activation ignored due to no Session(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb000021c | BM: Failed to acquire a ResourceSet for WorkItem: %1 with error %2.\r\n
0xb000021d | BM: WorkItem: %1 is being debugged. Setting wallclock limit to 0.\r\n
0xb000021e | BM: EvaluateActivationAction for WorkItem: %1 HRESULT: %2.\r\n
0xb000021f | BM: Skipped Buffering Exempted task with SQMId: %1 PsmKey: %2.\r\n
0xb0000220 | BM: Dropped Exempted task that came before SessionReady with SQMId: %1 PsmKey: %2.\r\n
0xb0000221 | BM: Activation ignored due to no User(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb0000222 | BM: User Logon Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000223 | BM: User Logoff Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000224 | BM: Pending activation discarded for work item (%1).\r\n
0xb0000225 | BM: Flushing ignored EvaluationState: %1 for WorkItem: %2.\r\n
0xb0000226 | BM: Flushing buffered activations.\r\n
0xb0000227 | BM: Global Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb0000228 | BM: A Session object for Session(%1) already exists.\r\n
0xb0000229 | BM: ShellSuspendState changed, oldState: %1 newState: %2\r\n
0xb000022a | BM: DPLKeyState changed, oldState: %1 newState: %2\r\n
0xb000022b | BM: Canceling WorkItem: %1 due to DPL policy.\r\n
0xb000022c | BM: Dropping activation for WorkItem: %1 due to DPL policy.\r\n
0xb000022d | BM: Buffered activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022e | BM: Exempted activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022f | BM: Buffered activation for WorkItem: %1 due to Thermal Throttling policy.\r\n
0xb0000258 | AM: Failed to read activation plugin registry with error code %1.\r\n
0xb0000259 | AM: Failed to CoCreate activation plugin with error code %1 and CLSID %2.\r\n
0xb000025a | AM: Successfully created activation plugin with CLSID %1 from the registry.\r\n
0xb000025b | AM: Failed to register package if needed with error %1.\r\n
0xb000025c | AM: Failed trying to register package by family name async during activation with error %1.\r\n
0xb000025d | AM: Failed trying to wait for the completion of the register package by family async during activation with error %1.\r\n
0xb00002bc | BAM: Added Package: %1 UserSid: %2.\r\n
0xb00002bd | BAM: Removed Package: %1 UserSid: %2.\r\n
0xb00002be | BAM: Added Application: %1 UserSid: %2.\r\n
0xb00002bf | BAM: Removed Application: %1 UserSid: %2.\r\n
0xb00002c0 | BAM: AccessState Changed for Package: %1 OldState: %2 NewState: %3 UserSid: %4.\r\n
0xb00002c1 | BAM: BackgroundExecutionManager::RequestAccessAsync called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c2 | BAM: BackgroundExecutionManager::GetStatus called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c3 | BAM: BackgroundExecutionManager::RemoveAccess called for Application: %1.\r\n
0xb00002c4 | BAM: Sanitizing data for package: %1 HRESULT: %2.\r\n
0xb00002c5 | BAM: ReregisteredPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002c6 | BAM: UnregisterPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002c7 | BAM: BackgroundExecutionManager::RequestAccessKindAsync called for Application: %1 Requested_AccessKind: %2 Returned: %3.\r\n
0xb00002ee | FAM: NotifyTaskInstanceCompleted, TaskID:%1, hr:%2\r\n
0xb00002ef | FAM: NotifyTaskInstanceRunning, TaskID:%1 Timer - %2\r\n
0xb00002f0 | FAM: RegisterForegroundAgentManagerProxy:PID=%1, ConsumerTaskId=%2, Option=%3, hr=%4\r\n
0xb00002f1 | FAM: UiForeground:Memory:%1MB, CPU:%2%%\r\n
0xb00002f2 | FAM: CreateAgentLaunchRequest, TaskID:%1, Queue:%2, hr:%3\r\n
0xb00002f3 | FAM: CancelAgentRequest, TaskID:%1, CancelType=%2, hr:%3\r\n
0xb00002f4 | FAM: AbortAgentRequestsInternal, hr:%1\r\n
0xb00002f5 | FAM: CompleteAgent, TaskID:%1, hr:%2\r\n
0xb00002f6 | FAM: PrioritizeAgentRequest, TaskID:%1, hr:%2\r\n
0xb00002f7 | FAM: OnForegroundAppChanged()-Abort agents\r\n
0xb00002f8 | FAM: OnRelease()\r\n
0xb00002f9 | FAM: NotifyConsumer, Notification:%1, TaskID:%2, hrResult:%3\r\n
0xb00002fa | FAM: AcquireSharedResourceSet, ProductID:%1, ConsumerPid:%2, Pending:%3, hr:%4\r\n
0xb00002fb | FAM: ReleaseResourceSet, #%1, hr:%2\r\n
0xb00002fc | FAM: TimerExpired:TerminateHost[PID=%1]\r\n
0xb00002fd | FAM: AcquireResourceSet, #%1, Mem:%2MB, CPU:%3%%, hr:%4\r\n
0xb00002fe | FAM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000321 | OTM: Read settings. First retry timeout = %1 ms, Second retry timeout = %2 ms, Third retry timeout = %3 ms, Maximum Retry Timeout = %4 ms\r\n
0xb0000322 | OTM: Task instance %2 of product %1 completed\r\n
0xb0000323 | OTM: TaskHost of product %1 has crashed\r\n
0xb0000324 | OTM: TaskHost of product %1 has been completed by PacMan\r\n
0xb0000325 | OTM: Launching OEM boot agents\r\n
0xb0000326 | OTM: Launching boot agents for product %1 failed with error %2\r\n
0xb0000327 | OTM: Launch boot agents for product %1\r\n
0xb0000328 | OTM: Running OnUpdateStarted for product %1\r\n
0xb0000329 | OTM: Restarting boot agents for product %1 after update\r\n
0xb000032a | OTM: Start menu is ready.\r\n
0xb000032b | OTM: Could not launch OEM boot agents. QueueUserWorkItem failed with error %1.\r\n
0xb000032c | OTM: Could not process update notification for OEM application. QueueUserWorkItem failed with error %1.\r\n
0xb000032d | OTM: Could not process update notification for OEM application. ProcessUpdateNotification failed with error %1.\r\n
0xb000032e | OTM: OemTaskManager::NotifyTaskInstanceCompleted failed with error %1.\r\n
0xb000032f | OTM: OemTaskManager::NotifyTaskHostCompleted failed with error %1.\r\n
0xb0000330 | OTM: OemApp::DumpAgents failed with error %1.\r\n
0xb0000331 | OTM: An error occurred. Hr = %1\r\n
0xb0000332 | OTM: No apps with ServiceAgents were found.\r\n
0xb0000333 | OTM: No ServiceAgent task found for product %1.\r\n
0xb0000334 | OTM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb000035d | PLM: Start tracking new app user %1 app %2, contract %3, hr = %4\r\n
0xb000035e | PLM: Application launched %1 in app %2, hr = %3\r\n
0xb000035f | PLM: Application resume %1 in app %2, hr = %3\r\n
0xb0000360 | PLM: Suspend-Terminate(%3) task %1 in app %2\r\n
0xb0000361 | PLM: Suspend-Terminate suspend of task %1 in app %2 exemption %3\r\n
0xb0000362 | PLM: Suspend-Terminate auto terminate(%3) task %1 in app %2\r\n
0xb0000363 | PLM: Suspend-Terminate task %1 in app %2, hr %3\r\n
0xb0000364 | PLM: Halt app %1, hr %2\r\n
0xb0000365 | PLM: Task resume %1 in app %2\r\n
0xb0000366 | PLM: Task cancel %1 in app %2\r\n
0xb0000367 | PLM: Task remove %1 in app %2\r\n
0xb0000368 | PLM: Queue Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000369 | PLM: Queue Activation State Change Notification %1 state %2\r\n
0xb000036a | PLM: Before Activate task %1 for user %2 in app %3, contract %4, hostid %5, hr = %6\r\n
0xb000036b | PLM: After Activate task %1 with result %2, hr = %3\r\n
0xb000036c | PLM: ApplicationLayer=%1 Set Foreground new task %2, prev task %3\r\n
0xb000036d | PLM: Add task %1 to user %2 and app %3, hr = %4\r\n
0xb000036e | PLM: Create app for user %1, %2, new [app(%3) pkg(%4)], hr = %5\r\n
0xb000036f | PLM: Add task %1 to user %2 and app %3, new [app(%4) pkg(%5)], hr = %6\r\n
0xb0000370 | PLM: Remove task %1, was found(%2)\r\n
0xb0000371 | PLM: Remove app if empty from user %1, %2, hr = %3\r\n
0xb0000372 | PLM: Remove pkg if empty from user %1, %2, hr = %3\r\n
0xb0000373 | PLM: Send Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000374 | PLM: Send Activation State Change Notification %1 state %2\r\n
0xb0000376 | PLM: Timer Started duration %1ms, hr %2\r\n
0xb0000377 | PLM: Timer Expired duration %1ms, hr %2\r\n
0xb0000378 | PLM: Abort task %1 reason %2, dump(%3)\r\n
0xb0000379 | PLM: Task rehydrate %1 in app %2 contract %3\r\n
0xb000037a | PLM: Start RPC suspension timer PSMKey=%1 WakeCounters=%2, hr = %3\r\n
0xb000037b | PLM: Cancel RPC suspension timer PSMKey=%1 app state=%2\r\n
0xb000037c | PLM: Terminate application PSMKey=%1 due to expired RPC suspension timeout\r\n
0xb000037d | PLM: Application %1 cannot be terminated due to %2 exemption\r\n
0xb000037e | PLM: Application %1 can be terminated\r\n
0xb000037f | PLM: EvaluateAndTerminateApplication %1 cannot be terminated due to %2\r\n
0xb0000380 | PLM: EvaluateAndTerminateApplication %1, terminate hr = %2\r\n
0xb0000381 | PLM: Terminate debounce app %1 current state %2 ultimate state %3\r\n
0xb0000382 | PLM: Terminate debounce app %1, hr = %2\r\n
0xb0000383 | PLM: Terminate reason was cleared\r\n
0xb0000384 | PLM: Abort app user %1 app %2 reason %3, dump(%4)\r\n
0xb0000385 | PLM: Watson dump NOT generated for user %1 app %2, process count %3\r\n
0xb0000386 | PLM: Watson dump start for user %1 app %2 reason %3 description %4, process %5 (%6)\r\n
0xb0000387 | PLM: Watson dump information for user %1 app %2 product Id %3 title %4 version %5\r\n
0xb0000388 | PLM: Watson dump end for user %1 app %2, hr %3\r\n
0xb0000389 | PLM: Add Watson dump to user %1 app %2 process %3, hr %4\r\n
0xb000038a | PLM: Failed to add Watson process info for process %1 user %2 app %3\r\n
0xb000038b | PLM: Watson dump status changed pids(%1)\r\n
0xb000038c | PLM: Watson dump status changed, add process %1 user %2 app %3\r\n
0xb000038d | PLM: Watson dump status changed, remove process %1 user %2 app %3\r\n
0xb000038e | PLM: Watson dump status changed, unknown process %1 app %2\r\n
0xb000038f | PLM: Watson add/remove(%2) error report task completion to process %1 (signaled %4), hr %3\r\n
0xb0000390 | PLM: Watson in progress for PSMKey %1, waiting...\r\n
0xb0000391 | PLM: Watson in progress finished for PSMKey %1\r\n
0xb0000392 | PLM: Extending RPC suspension timer PSMKey=%1\r\n
0xb0000393 | PLM: Acquire network reference failed CM_RESULT=%1\r\n
0xb0000394 | PLM: Release network reference failed CM_RESULT=%1\r\n
0xb0000395 | PLM: Suspend-Terminate(%2) app %1 exemption %3, hr %4\r\n
0xb0000396 | PLM: Suspend-Terminate task %1 while dehydrating\r\n
0xb0000397 | PLM: Add user %1 sid %2 to data store, hr = %3\r\n
0xb0000398 | PLM: Start launch grace for user %1 app %2, hr = %3\r\n
0xb0000399 | PLM: Set Window Id for user %1 app %2 wnd %3\r\n
0xb000039a | PLM: EvaluateLaunchGraceCompleted for user %1 app %2\r\n
0xb000039b | PLM: Terminating reexisting app due to sihost restart with PSMKey %1, status %2\r\n
0xb000039c | PLM: Terminating preexisting applications on sihost startup\r\n
0xb000039d | PLM: Set Pause On Lock for user %1 app %2 value %3\r\n
0xb000041b | AAM: Initiate activation for user %1 app %2 contract %3 task %4, hr %5\r\n
0xb000041c | AAM: Initiate activation completed for task %2 (expected %1), hr %3\r\n
0xb000041d | AAM: Initialize activation for user %1 app %2 contract %3 lightup(%5), hr %4\r\n
0xb000041e | AAM: Validate activation, hr %1\r\n
0xb000041f | AAM: Verify license for pkg %1, hr %2\r\n
0xb0000420 | AAM: Activate activation task %1 host %2, hr %3\r\n
0xb0000421 | AAM: Activation shim timer expired %1, hr %2\r\n
0xb0000422 | AAM: Initiate Core UI, hr %1\r\n
0xb0000423 | AAM: Release Core UI\r\n
0xb0000424 | AAM: Create Windows AAM, hr %1\r\n
0xb0000425 | AAM: Attempted remediation, hr %1\r\n
0xb0000426 | AAM: Failed while trying to find a remediation handler, hr %1\r\n
0xb0000427 | AAM: Failed while trying to find the package status, hr %1\r\n
0xb0000428 | AAM: Failed while trying to find the package origin, hr %1\r\n
0xb0000429 | AAM: Failed while trying to verify and initialize the activation, hr %1\r\n
0xb000042a | AAM: Failed while trying to check roaming data, hr %1\r\n
0xb000042f | AAM: Broker created plugins %1, expected %2\r\n
0xb0000430 | AAM: Broker initialize, hr %1\r\n
0xb0000431 | AAM: Broker start activate application %1 (%3 args) arg[0] %2 type %4 caller PID %5 (initialization count %6)\r\n
0xb0000432 | AAM: Broker end activate application %1 launched PID %2 task %3, hr %4\r\n
0xb0000433 | AAM: Broker activate task with result for app %1 caller PID %2 caller task %3\r\n
0xb0000434 | AAM: Broker get result for PID %1 task %2 result %3, hr %4\r\n
0xb0000435 | AAM: Broker get task id for process %1 window %2 = task %3, hr %4\r\n
0xb0000436 | AAM: Broker init session manager, hr %1\r\n
0xb0000437 | AAM: Broker release session manager\r\n
0xb0000438 | AAM: Broker add task with result for parent %1, hr %2\r\n
0xb0000439 | AAM: Broker get task with result for parent %1, hr %2\r\n
0xb000043a | AAM: Broker remove task with result for parent %1, hr %2\r\n
0xb000043b | AAM: Broker create completed event for caller PID %1, hr %2\r\n
0xb000043c | AAM: Broker get task with result for child %1, hr %2\r\n
0xb000043d | AAM: Broker parent task completed %1 with child state %2\r\n
0xb000043e | AAM: Broker child task completed %1 with state %2, hr %3\r\n
0xb000043f | AAM: Broker task event signaled for parent %1 child %2 previous state %3, hr %4\r\n
0xb0000440 | AAM: Broker close task %1, hr %2\r\n
0xb0000441 | AAM: Broker activate application %1 arg[%3] %2\r\n
0xb000044c | FM-ARP: ApplyResourceSetType ResourceSetType=%1 User=%2 PSMKey=%3 ResourceSet=%4 HRESULT=%5\r\n
0xb000044d | FM-ARP: ApplyTerminal UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044e | FM-ARP: RemoveInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044f | FM-ARP: ResetInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000450 | FM-ARP: OnRelease UserContext=%1 PsmKey=%2 ReleaseAction=%3 ReleasedCachedResource=%4 ReleaseAppliedResource=%5 HRESULT=%6\r\n
0xb0000451 | FM-ARP: OnAcquired UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000452 | FM-ARP: OnOutOfMemory UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000453 | FM-ARP: ApplyResourceBoost User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000454 | FM-ARP: AcquireResourceSet ResourceSetType=%1 Usercontext=%2 PsmKey=%3 HRESULT=%4\r\n
0xb0000455 | FM-ARP: Apply Cached Resource Set Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000456 | FM-ARP: Clear Cached Resource User=%1 PSMKey=%2\r\n
0xb0000457 | FM-ARP: Fire Cached ResourceCallback User=%1 PSMKey=%2\r\n
0xb00004b0 | FM-CAM: OnApplicationStateChangedEx UserContext=%1 PsmKey=%2 state=%3 HRESULT=%4\r\n
0xb00004b1 | FM-CAM: AcquireForegroundResource UserContext=%1 PsmKey=%2 isPending=%3\r\n
0xb00004b2 | FM-CAM: OnResourceAcquired UserContext=%1 PsmKey=%2\r\n
0xb00004b3 | FM-CAM: OnResourceTimerExpired UserContext=%1 PsmKey=%2\r\n
0xb00004e2 | FM: TaskCompletion New Battery Saver State %1\r\n
0xb00004e3 | FM: TaskCompletion Revoke Exemption PID=%1 AUMID=%2 TC=%3\r\n
0xb00004e4 | FM: TaskCompletion Apply(%3) Exemption PID=%1 TC=%2 HRESULT=%4\r\n
0xb00004e5 | FM-EEP: CheckProcessBackgroundEligibility ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e6 | FM-EEP: ApplyTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e7 | FM-EEP: RevokeTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e8 | FM-EEP: RequestExtendedExecution ProcessId=%1 Reason=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004e9 | FM-EEP: RegisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004ea | FM-EEP: CompleteExtendedExecution ProcessId=%1 fIsResumed=%2 HRESULT=%3\r\n
0xb00004eb | FM-EEP: RevokeSuspensionExtension User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00004ec | FM-ARP: NotifyPendingResourceSetTransition ResourceSetType=%1 ResourceSet=%2 HRESULT=%3\r\n
0xb00004ed | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 fTimerExpiredCallback=%2 HRESULT=%3\r\n
0xb00004ee | FM-EEP: IsApplicationStateBackgroundEligibile User=%1 PsmKey=%2 fResult=%3\r\n
0xb00004ef | FM-EEP: RevokeTaskCompletionExemption AppUserModelId=%1 HRESULT=%2\r\n
0xb00004f0 | FM-EEP: AllowBackgroundExecution User=%1 AppUserModelId=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004f1 | FM-EEP: OnPackageEnergyStateChange PackageFullName=%1 PackageState=%2 HRESULT=%3\r\n
0xb00004f2 | FM-EEP: RegisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f3 | FM-EEP: UnregisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f4 | FM-EEP: UnregisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004f5 | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 TC=%2 isResourcePending =%3 HRESULT=%4\r\n
0xb00004f6 | FM-EEP: Task Completion Denied By EDP Policy ProcessId=%1 TC=%2\r\n
0xb00004f7 | FM-EEP: IsForegroundApplication Application=%1 Result=%2\r\n
0xb0000578 | FM: Registering callback %1 HRESULT=%2\r\n
0xb0000579 | FM: Generate ActivationInstanceID Id=%1\r\n
0xb000057a | FM: +ActivationPrerequisitePhase ActivationInstanceId=%1 UserContext=%2 AUMID=%3 ContractId=%4\r\n
0xb000057b | FM: -ActivationPrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb000057c | FM: +Resume_RehydrationPhase ActivationInstanceId=%1\r\n
0xb000057d | FM: -Resume_RehydrationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000057e | FM: +ResumeActivation ActivationInstanceId=%1 fIsResumed=%2\r\n
0xb000057f | FM: -ResumeActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000580 | FM: +Resume_ActivationPhase ActivationInstanceId=%1\r\n
0xb0000581 | FM: -Resume_ActivationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000582 | FM: +PauseActivation ActivationInstanceId=%1\r\n
0xb0000583 | FM: -PauseActivation HRESULT=%1 PausePending=%2\r\n
0xb0000584 | FM: +CancelActivation ActivationInstanceId=%1\r\n
0xb0000585 | FM: -CancelActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000586 | FM: +AbortActivation ActivationInstanceId=%1 Reason=%2 fGenerateWER=%3\r\n
0xb0000587 | FM: -AbortActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000588 | FM: +GetActivationProcessId ActivationInstanceId=%1\r\n
0xb0000589 | FM: -GetActivationProcessId ActivationInstanceId=%1 PID%2 HRESULT=%3\r\n
0xb000058a | FM: +SetForegroundActivationInstance ActivationInstanceId=%1 Isforeground=%2\r\n
0xb000058b | FM: -SetForegroundActivationInstance ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000058c | FM: SetActivationDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb000058d | FM: OnActivationStateChanged ActivationInstanceId=%1 state=%2 HRESULT=%3\r\n
0xb000058e | FM: OnApplicationStateChanged UserContext=%1 PSMKey=%2 state=%3 HRESULT=%4\r\n
0xb000058f | FM: IsValidActivationProcessId ActivationInstanceID=%1 PID=%2 fValid=%3 HRESULT=%4\r\n
0xb0000590 | FM: GetForegroundProductId fIgnoreLockScreen=%1 ProductID=%2 HRESULT=%3\r\n
0xb0000591 | FM: GetProductIdFromProcessID ProductID=%1 PID=%2 HRESULT=%3\r\n
0xb0000592 | FM: Discarding Application Frozen notification because the application isn't really frozen\r\n
0xb0000593 | FM: Dehydrate Application AUMID=%1 HRESULT=%2\r\n
0xb0000594 | FM: +ResumePrerequisitePhase ActivationInstanceId=%1\r\n
0xb0000595 | FM: -ResumePrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb0000596 | FM: GenerateWatsonReport PID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000597 | FM: SetContinuation ActivationInstanceID=%1\r\n
0xb0000598 | FM: AbandonContinuation ActivationInstanceID=%1\r\n
0xb0000599 | FM: PerformContinuation ActivationInstanceID=%1\r\n
0xb000059a | FM: Shutdown HRESULT=%1\r\n
0xb000059b | FM: +PauseActivation ActivationInstanceId=%1 AUMID=%2 PackageFullName=%3\r\n
0xb000059c | FM: +ActivationBypass ActivationInstanceId=%1\r\n
0xb000059d | FM: -ActivationBypass ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000059e | FM: +PostPausePendingResume ActivationInstanceId=%1\r\n
0xb000059f | FM: -PostPausePendingResume ActivationInstanceId=%1 HRESULT=%2\r\n
0xb00005a0 | FM: SetActivationImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb00005a1 | FM: NotifyWindowAdded TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a2 | FM: NotifyWindowRemoved TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a3 | FTM: Logoff User=%1 HRESULT=%2\r\n
0xb00005a4 | FM: ActivationTimeoutPolicyChanged  TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a5 | FM-EEP: OnConnectedStandbyStateChanged  State=%1\r\n
0xb00005a6 | FM: SendActivationNotification ActivationId=%1 NotificationId=%2\r\n
0xb00005a7 | FM: OnResourceAcquired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a8 | FM: OnResourceTimerExpired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a9 | FM: PostPausePendingActivation ActivationId=%1 HRESULT=%2\r\n
0xb00007d0 | VoIPPolicy: Evaluate Activation Action for PsmKey = %2, WorkItemId = %1, Action = %3, HRESULT = %4\r\n
0xb00007d1 | VoIPPolicy: Task Activated for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d2 | VoIPPolicy: Task Completed for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d3 | VoIPPolicy: Task Canceled for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d4 | VoIPPolicy: Task Aborted for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d5 | VoIPPolicy: Determine and Apply Resources PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d6 | VOIP: NotifyVoipActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d7 | VOIP: LaunchVoipRtcTask called for PID:%1 PSMKey:{%2} with TaskEntryPoint:{%3} and WNFStateName:{%4} HRESULT:%5.\r\n
0xb00007d8 | VOIP: NotifyVoipActivityCompleted called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d9 | VOIP: HoldActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007da | VOIP: UnholdActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007db | VOIP: NotifyIncomingCallDialogDisplayed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dc | VOIP: NotifyIncomingCallDialogDismissed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dd | VOIP: CallActive called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007de | VOIP: AppLaunchVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007df | VOIP: OnVoipActivityCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e0 | VOIP: AppHoldActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e1 | VOIP: AppUnholdActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e2 | VOIP: OnIncomingCallDialogDisplayed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e3 | VOIP: OnIncomingCallDialogDismissed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e4 | VOIP: AppDetermineAndApplyBestResourceSet called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e5 | VOIP: PolicyEvaluateAction called for WorkItemId:{%1} PSMKey:{%2} ActivationAction:%3 HRESULT:%4.\r\n
0xb00007e6 | VOIP: PolicyTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e7 | VOIP: PolicyTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e8 | VOIP: PolicyTaskCanceled called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e9 | VOIP: PolicyTaskAborted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007ea | VOIP: OnForegroundApplicationChanged called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007eb | VOIP: AppOnTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ec | VOIP: AppOnTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ed | VOIP: AppCancelVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ee | VOIP: CancelVoipRtcTask called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb0000c81 | Task: %1 has started\r\n
0xb0000c82 | Task: %1 has paused\r\n
0xb0000c83 | Task: %1 has resumed\r\n
0xb0000c84 | Task: %1 has completed\r\n
0xb0000c85 | EM: +GetTaskInfo()\r\n
0xb0000c86 | EM: -GetTaskInfo(). HRESULT = %1\r\n
0xb0000c87 | EM: GetAppInfo:%1,%2:%3\r\n
0xb0000c88 | EM: ParseBackgroundAbilities - HRESULT=%1\r\n
0xb0000c89 | EM: +ExecManServerHost::CreateProcess\r\n
0xb0000c8a | EM: -ExecManServerHost::CreateProcess. HRESULT=%1\r\n
0xb0000c8b | Sqm::AppPlatSqmAppDataUsage: %1/%2 - TaskID = %3, Type = %4, NewState = %5, ReasonForStateChange = %6, Duration (ms) = %7, PeakMemory (kb) = %8\r\n
0xb0000c8f | Emc::ExecuteCommand: StartTaskCallbackBegin: TaskID = %1\r\n
0xb0000c90 | Emc::ExecuteCommand: StartTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c91 | Emc::ExecuteCommand: PauseTaskCallbackBegin: TaskID = %1\r\n
0xb0000c92 | Emc::ExecuteCommand: PauseTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c93 | Emc::ExecuteCommand: ResumeTaskCallbackBegin: TaskID = %1\r\n
0xb0000c94 | Emc::ExecuteCommand: ResumeTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c95 | Emc::ExecuteCommand: ControlTaskCallbackBegin: TaskID = %1\r\n
0xb0000c96 | Emc::ExecuteCommand: ControlTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c97 | Emc::ExecuteCommand: CancelTaskCallbackBegin: TaskID = %1\r\n
0xb0000c98 | Emc::ExecuteCommand: CancelTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c99 | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackBegin: TaskID = %1\r\n
0xb0000c9a | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c9e | Emc::RegisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, HR = %3\r\n
0xb0000ca8 | Emc::DeregisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, Reason = %3, HR = %4\r\n
0xb0000ca9 | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleBegin: ProductID = %1\r\n
0xb0000caa | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleEnd: ProductID = %1\r\n
0xb0000cab | EM: Skipping terminate process call for %1\r\n
0xb0000cac | EM: Terminating process: PID = %1, ExitCode = %2\r\n
0xb0000ce4 | AimServer::OnAgentRequestInvoked: AgentRequestID %1 was invoked. PID = %2, HR = %3\r\n
0xb0000ce5 | AimServer::ReadSettings: HR = %1\r\n
0xb0000ce6 | AimServer: Detected server for scope %1 terminated (PID = %2)\r\n
0xb0000ce8 | AimServer::HandleEvent: ProductID %1 received PM LifecyleEvent %2. HR Notification = %3, HR = %4\r\n
0xb0000ce9 | BA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cea | BA::RegisterServiceRequest: AlreadyReserved = %1, SR = %2, HR = %3\r\n
0xb0000ceb | BA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cec | BA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000ced | BA::NotifyTaskInstanceCompleted: Terminating Orphaned Host PID = %1\r\n
0xb0000cee | BA::OrphanAgentRequest: AgentRequestID = %1, HR = %2\r\n
0xb0000cef | BA::UnRegisterServiceRequest: Terminating host PID %1\r\n
0xb0000cf0 | BA::UnRegisterServiceRequest: Orphaning host PID %1\r\n
0xb0000cf1 | BA::UnRegisterServiceRequest: Terminating second old orphaned host PID %1\r\n
0xb0000cf2 | BTM::RecvCallback: Timer expired for AgentRequestID %1\r\n
0xb0000cf3 | BTM::LaunchTask: TaskURI = %1 TaskID = %2, PID = %3, HR = %4\r\n
0xb0000cf4 | GBA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cf5 | GBA::RegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf6 | GBA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf7 | GBA::RegisterAgentRequest: AgentRequestID = %1, type = %2, hr = %3\r\n
0xb0000cf8 | GBA: Cancelling low priority %3 agent because high priority %2 needs to run: Resource was dedicated = %1\r\n
0xb0000cf9 | GBA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000cfa | GBA::TryAcquireResourceSet: pending = %1, type = %2, HR = %3\r\n
0xb0000cfb | GBA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfc | BA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfd | BA::NotifyTaskHostCompleted: ProductID = %1, PID = %2\r\n
0xb0000cfe | BA::RegisterAgentRequest: ProductID = %1, AgentRequestID = %2, HR = %3\r\n
0xb0000cff | BA::PdcActivationFailed: ProductID = %1, Reason = %2, NTSTATUS = %3\r\n
0xb0000dac | FTM: AllowBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dad | FTM: Process is using too much memory for BG Execution. PID=%1, MemUsage=%2, RequiredMemUsage=%3\r\n
0xb0000dae | FTM: Removing BG capability from Task ID %1 due to OOM\r\n
0xb0000daf | FTM: Battery Saver State has change. New state = %1\r\n
0xb0000db0 | FTM: Attempted new BG Execution request due to battery state change. TaskID=%1\r\n
0xb0000db1 | FTM: NotifyTaskInstanceCompleted TaskID=%1 HRESULT=%2\r\n
0xb0000db2 | FTM: NotifyTaskInstancePaused TaskID=%1 HRESULT=%2\r\n
0xb0000db3 | FTM: NotifyTaskInstanceRunning TaskID=%1 HRESULT=%2\r\n
0xb0000db4 | FTM: SendTaskStatusChange TaskID=%1 Status=%2 HRESULT=%3\r\n
0xb0000db5 | FTM: NotifyTaskHostCompleted HRESULT=%1\r\n
0xb0000db6 | FTM: Discarding NotifyTaskHostFrozen notification because the host isn't really frozen\r\n
0xb0000db7 | FTM: NotifyTaskHostFrozen PID=%1 HRESULT=%2\r\n
0xb0000db8 | FTM: NotifyTaskHostDehydrated HRESULT=%1\r\n
0xb0000db9 | FTM: Registering callback %1 HRESULT=%2\r\n
0xb0000dba | FTM: New Task %1 is dehydration-suppressing\r\n
0xb0000dbb | FTM: Applying Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbc | FTM: Revoking Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbd | FTM: +LaunchTask TaskURI=%1 LaunchFlags=%2\r\n
0xb0000dbe | FTM: -LaunchTask TaskURI=%1 TaskID=%2 PID=%3 HRESULT=%4\r\n
0xb0000dbf | FTM: ResumeTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc0 | FTM: Removing Foreground Resources from TaskID=%1\r\n
0xb0000dc1 | FTM: SetForegroundTaskInstanceId TaskID=%1 HRESULT=%2\r\n
0xb0000dc2 | FTM: PauseTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc3 | FTM: CancelTask TaskID=%1 Frozen=%2 HRESULT=%3\r\n
0xb0000dc4 | FTM: AbortTask being ignored because the task is completed TaskID=%1\r\n
0xb0000dc5 | FTM: AbortTask TaskID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000dc6 | FTM: SetTaskDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb0000dc7 | FTM: RequestProcessBackgroundExecution type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc8 | FTM: CancelProcessBackgroundExecutionRequest type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc9 | FTM: TaskRunningInBackground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dca | FTM: TaskRunningInForeground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dcb | FTM: Changing activation policy to resume due to BG Execution for ProductID %1\r\n
0xb0000dcc | FTM: OnShutdownCompleted\r\n
0xb0000dcd | FTM: Ignoring expired watchdog for task %1 because it is being debugged.\r\n
0xb0000dce | FTM: Watchdog fired for task %1 while running in background. Pausing Task.\r\n
0xb0000dcf | FTM: Request BG Execution Denied because it wasn't running. TaskID=%1\r\n
0xb0000dd0 | FTM: Request BG Execution Denied because product was forbidden. TaskID=%1\r\n
0xb0000dd1 | FTM: Request BG Execution Denied because task didn't have BG abilities in its manifest. TaskID=%1\r\n
0xb0000dd2 | FTM: Request BG Execution Denied due to lack of resources. TaskID=%1\r\n
0xb0000dd3 | FTM: Request BG Execution Denied because battery policy prevented it. TaskID=%1\r\n
0xb0000dd4 | FTM: RequestBGAccess IsAllowed=%1 TaskID=%2 HRESULT=%3\r\n
0xb0000dd5 | FTM: RemoveBGRequest RequestedRemoval=%1 ActualRemoval=%2 TaskID=%3 HRESULT=%4\r\n
0xb0000dd6 | FTM: ForbidBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dd7 | FTM: IsValidTaskInstancePid TaskID=%1 Pid=%2 fValid=%3 HRESULT=%4\r\n
0xb0000dd8 | FTM: DetermineBestResourceSet for child ProductID=%1 LaunchFlags=%2 ResourceSetType=%3\r\n
0xb0000dd9 | FTM: OnRelease ResourceSet TaskID=%1 ResouceSet=%2 HRESULT=%3\r\n
0xb0000dda | FTM:UITask Call to Acquire network reference failed CM_RESULT=%1\r\n
0xb0000ddb | FTM:UITask Call to Release network reference failed CM_RESULT=%1\r\n
0xb0000ddc | FTM: SetTaskImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb0000ddd | FTM: +RequestProcessBackgroundExecution type=%1 Pid=%2\r\n
0xb0000dde | FTM: +RequestBackgroundExecution type=%1\r\n
0xb0000ddf | FTM: -RequestBackgroundExecution type=%1 HRESULT=%2\r\n
0xb0000de0 | FTM: +RequestBGAccess TaskInstanceId=%1 type=%2\r\n
0xb0000de1 | FTM: Request BG Execution Denied because DPL policy prevented it. TaskID=%1\r\n
0xb0000de2 | FTM: Windows Information Protection keys locked state (%1)\r\n
0xb0000e42 | VoIP: Foreground state for product %1 has changed. Is in foreground = %2\r\n
0xb0000e43 | VoIP: Canceling communication agent for product %1\r\n
0xb0000e44 | VoIP: Timer expired for keep-alive agent of product %1\r\n
0xb0000e45 | VoIP: Timer expired for incoming call agent of product %1\r\n
0xb0000e46 | VoIP: Launched agent instance with id %2 and URI %1\r\n
0xb0000e47 | VoIP: Canceled agent instance with id %1\r\n
0xb0000e48 | VoIP: Set active call resource set\r\n
0xb0000e49 | VoIP: Set communication agent resource set\r\n
0xb0000e4a | VoIP: Set VoIP Worker resource set\r\n
0xb0000e4b | VoIP: Applied terminal resource set\r\n
0xb0000e4c | VoIP: Last task instance completed. Releasing the task host ...\r\n
0xb0000e4d | VoIP: Launching active call agent instance for product %1\r\n
0xb0000e4e | VoIP: Canceling active call agent for product %1\r\n
0xb0000e4f | VoIP: Putting an active call on hold for product %1\r\n
0xb0000e50 | VoIP: Taking an active call off hold for product %1\r\n
0xb0000e51 | VoIP: Incoming call dialog has been displayed for product %1\r\n
0xb0000e52 | VoIP: Incoming call dialog has been dismissed for product %1\r\n
0xb0000e53 | VoIP: Launch communication agent request received from process %1 for product %2\r\n
0xb0000e54 | VoIP: Read settings. Keep alive timout = %1 ms, Max agent request queue = %2, Incoming call grace period = %3 ms, Incoming call dismissed grace period = %4 ms\r\n
0xb0000e55 | VoIP: Received request to launch agent type %2 for product %1\r\n
0xb0000e56 | VoIP: Task instance %2 of product %1 completed\r\n
0xb0000e57 | VoIP: Processing request to launch agent type %2 for product %1\r\n
0xb0000e58 | VoIP: Added VoIPApp object to map for product %1\r\n
0xb0000e59 | VoIP: Removed VoIPApp object from map for product %1\r\n
0xb0000e5a | VoIP: Getting VoIPApp object from map for product %1\r\n
0xb0000e5b | VoIP: Publishing WNF_DEVP_VOIP_ACTIVE_CALL_STATE_CHANGE failed with status %1\r\n
0xb0000e5c | VoIP: Subscribing to the WNF_WIFI_CONNECTION_STATUS event failed with status %1\r\n
0xb0000e5d | VoIP: Subscribed to WNF_WIFI_CONNECTION_STATUS? %1\r\n
0xb0000e5e | VoIP: WiFi connection status active/dormat? %1 (hConnection = %2)\r\n
0xb0000e5f | VoIP: RtlQueryWnfStateData failed trying to query the value of WNF_WIFI_CONNECTION_STATUS. NTSTATUS = %1\r\n
0xb0000e60 | VoIP: Could not spin up worker for UpdateWiFiStateHelper. HR =%1\r\n
0xb0000e61 | VoIP: In active call? %1\r\n
0xb0000e62 | VoIP: CmUtilSetWiFiActive was not successful. This could be because WiFi disconnected by the time we were notified of the connection.\r\n
0xb0000e63 | VoIP: WiFi connection status is %1.\r\n
0xb0000e64 | VoIP: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000e65 | VoIP: PhoneServiceRestart: HR = %1\r\n
0xb0000e66 | VoIP: PhoneServiceRestart: Product = %1, HR = %2\r\n
0xb0000e67 | VoIP: Launching call query info agent instance for product %1\r\n
0xb0000e68 | VoIP: Canceling call query info agent instance for product %1\r\n
0xb0000e69 | VoIP: Terminating agents due to low memory for product %1\r\n
0xb0000e6a | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2\r\n
0xb0000e6b | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2, fApplied = %3, HR = %4\r\n
0xb0000e6c | VoIP: Set PDC Network Active for product = %1, NTSTATUS = %2\r\n
0xb0000e6d | VoIP: Set PDC Network Inactive for product = %1, NTSTATUS = %2\r\n
0xb0000e6e | VoIP: Renew PDC Network activation failed for product = %1, NTSTATUS = %2\r\n
0xb0000e73 | VoIP: An error occurred. Hr = %1\r\n
0xb00017d4 | %1 - [%2 = %3]\n\r\n
0xb00017d5 | %1 - Parsing config file [%2] file size = %3.  Parse = %4\r\n
0xb00017d6 | %1 - OnTaskModelMessage: Dispatching EM message\r\n
0xb00017d7 | %1 - InitializeTaskHost URI=%2, Page=%3, TaskId=%4\r\n
0xb00017d8 | %1 - Resuming Task from dehydration\r\n
0xb00017d9 | %1 - TaskHandler::GetTaskHandler hr=%2\r\n
0xb00017da | %1 - TaskHost Init\r\n
0xb00017db | %1 - TaskHost Init hr = %2\r\n
0xb00017dc | %1 - Host Dispatcher Exiting hr = %2\r\n
0xb00017dd | %1 - TaskHandlerReady received\r\n
0xb00017de | %1 - StartTask TaskId=%2\r\n
0xb00017df | %1 - PauseTask TaskId=%2\r\n
0xb00017e0 | %1 - ResumeTask TaskId=%2\r\n
0xb00017e1 | %1 - OnTaskHandlerVisible received\r\n
0xb00017e2 | %1 - OnTaskHandlerHidden received\r\n
0xb00017e3 | %1 - BackgroundExecutionCallback TaskId[%2] Command[%3]\r\n
0xb00017e4 | %1 - BackgroundExecutionCallback hr=%2\r\n
0xb00017e5 | %1 - OnHostRunning\r\n
0xb00017e6 | %1 - OnHostRunning. hr = %2\r\n
0xb00017e7 | %1 - Dehydrating. dehydrateGracefully = %2\r\n
0xb00017e8 | %1 - Gracefully dehydrating TaskHost\r\n
0xb00017e9 | %1 - TryDehydrateHost. hr = %2\r\n
0xb00017ea | %1 - DehydrateHost event triggered\r\n
0xb00017eb | %1 - WaitForUnfreeze hr = %2\r\n
0xb00017ec | %1 - ReduceMemoryHostCallback hr = %2\r\n
0xb00017ed | %1 - Graceful tear-down failed\r\n
0xb00017ee | %1 - BeforeHostRunningInBackgroundCallback\r\n
0xb00017ef | %1 - BeforeHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f0 | %1 - AfterHostRunningInBackgroundCallback\r\n
0xb00017f1 | %1 - AfterHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f2 | %1 - Unhandled exception occurred. hr = %2\r\n
0xb00017f3 | %1 - State-Transition (%2)->(%3)\r\n
0xb00017f4 | %1 - EnableProfiling = [%2]\r\n
0xb00017f5 | %1 - Profile Dll = [%2]\r\n
0xb00017f6 | %1 - ProfilerCLSID = [%2]\r\n
0xb00017f7 | %1 - TaskHostHelper::SetProfilerSettings hr = %2\r\n
0xb00017f8 | %1 - File path = %2 : %3\r\n
0xb00017f9 | %1 - Parse Element: %2.\r\n
0xb00017fa | %1 - Parse Element Value = %2 with pwszLocalName = %3.\r\n
0xb00017fb | %1 - Parse HResult = %2\r\n
0xb00017fc | %1 - YUTHost: failed to GAC trusted assembly %2\r\n\r\n
0xb00017fd | %1 - UITaskHandler::Initialize. hr = %2\r\n
0xb00017fe | %1 - UITaskHandler::Disconnect done\r\n
0xb00017ff | %1 - UITaskHandler::GoBackground. hr = %2\r\n
0xb0001800 | %1 - UITaskHandler::GoForeground. hr = %2\r\n
0xb0001801 | %1 - Managed Framework Ready. Handling Pending Event:[%2]\r\n
0xb0001802 | %1 - HandlePendingEvents Start TaskId=%2\r\n
0xb0001803 | %1 - HandlePendingEvents Pause TaskId=%2\r\n
0xb0001804 | %1 - HandlePendingEvents Resume TaskId=%2\r\n
0xb0001805 | %1 - Waiting for Siblings...\r\n
0xb0001806 | %1 - Waiting for Siblings done. hr = %2\r\n
0xb0001807 | %1 - UITaskHandler::OnRuntimeHostReady TaskID:[%2]\r\n
0xb0001808 | %1 - UITaskHandler::OnRuntimeHostReady. Processed pending SystemKeyPress [%2]\r\n
0xb0001809 | %1 - UITaskHandler::OnRuntimeHostReady hr = %2\r\n
0xb000180a | %1 - UITaskHandler::RegistrationComplete hr = %2\r\n
0xb000180b | %1 - UITaskHandler::ConnectionComplete received\r\n
0xb000180c | %1 - UITaskHandler::ConnectionComplete hr = %2\r\n
0xb000180d | %1 - UITaskHandler::ProcessActivationData received, reason=%2\r\n
0xb000180e | %1 - UITaskHandler::ProcessActivationData hr = %2\r\n
0xb000180f | %1 - UITaskHandler::Show received. Direction:[%2]\r\n
0xb0001810 | %1 - Navigation in progress. Queuing up the Show\r\n
0xb0001811 | %1 - UITaskHandler::Show hr = %2\r\n
0xb0001812 | %1 - UITaskHandler::ShowInternal. Direction:[%2:NavigationDirection:]\r\n
0xb0001813 | %1 - UITaskHandler::ShowInternal. hr = %2\r\n
0xb0001814 | %1 - UITaskHandler::Hide received. Direction:[%2]\r\n
0xb0001815 | %1 - Navigation in progress. Cancelling Show and ignoring Hide\r\n
0xb0001816 | %1 - UITaskHandler::Hide hr = %2\r\n
0xb0001817 | %1 - UITaskHandler::NavigateTo received TaskID:[%2]\r\n
0xb0001818 | %1 - UITaskHandler::NavigateTo. hr = %2\r\n
0xb0001819 | %1 - UITaskHandler::NavigationComplete TaskID:[%2]\r\n
0xb000181a | %1 - UITaskHandler::NavigationComplete hr = %2\r\n
0xb000181b | %1 - UITaskHandler::NavigateAway received TaskID:[%2]\r\n
0xb000181c | %1 - Navigation interrupted since Task is closing\r\n
0xb000181d | %1 - Navigation in progress. Queuing up the NavigateAway\r\n
0xb000181e | %1 - UITaskHandler::NavigateAway hr = %2\r\n
0xb000181f | %1 - UITaskHandler::NavigateAwayInternal TaskID:[%2]\r\n
0xb0001820 | %1 - UITaskHandler::NavigateAwayInternal hr = %2\r\n
0xb0001821 | %1 - UITaskHandler::RequestClose called TaskID:[%2]\r\n
0xb0001822 | %1 - UITaskHandler::RequestClose hr = %2\r\n
0xb0001823 | %1 - LaunchSession in progress. Cannot add another callback\r\n
0xb0001824 | %1 - UITaskHandler::LaunchSession hr = %2\r\n
0xb0001825 | %1 - LaunchChildTask in progress. Cannot add another callback\r\n
0xb0001826 | %1 - UITaskHandler::LaunchChildTask hr = %2\r\n
0xb0001827 | %1 - UITaskHandler::SetPauseOnLock[%2] called TaskID:[%3]\r\n
0xb0001828 | %1 - UITaskHandler::SetPauseOnLock hr = %2\r\n
0xb0001829 | %1 - UITaskHandler::Close received TaskID:[%2]\r\n
0xb000182a | %1 - UITaskHandler::Close hr = %2\r\n
0xb000182b | %1 - UITaskHandler::SystemKeyPressed received: [%2]\r\n
0xb000182c | %1 - UITaskHandler::SystemKeyPressed processed\r\n
0xb000182d | %1 - UITaskHandler::SystemKeyPressed pending. Will be processed on RuntimeHost ready\r\n
0xb000182e | %1 - UITaskHandler::LaunchChildTaskComplete received with result %2\r\n
0xb000182f | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001830 | %1 - UITaskHandler::LaunchSessionComplete received with result %2\r\n
0xb0001831 | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001832 | %1 - OrientationChanged NewOrientation=%2\r\n
0xb0001833 | %1 - OrientationChange received before RuntimeHostTask is set\r\n
0xb0001834 | %1 - SetSupportedOrientations. SupportedOrientations:[%2]. hr = %3\r\n
0xb0001835 | %1 - GetSupportedOrientations. SupportedOrientations[%2]. hr = %3\r\n
0xb0001836 | %1 - GetCurrentOrientation. CurrentOrientation[%2]. hr = %3\r\n
0xb0001837 | %1 - UITaskHandler::ReplaceTouchEndpoint hr = %2\r\n
0xb0001838 | %1 - UITaskHandler::ReplaceTextEndpoint hr = %2\r\n
0xb0001839 | %1 - UITaskHandler::Get Task State. StateSize[%2]. hr = %3\r\n
0xb000183a | %1 - UITaskHandler::Set Task State. StateSize[%2]. hr = %3\r\n
0xb000183b | %1 - UITaskHandler::OnObscurityChange[%2]. hr = %3\r\n
0xb000183c | %1 - UITaskHandler::OnLockScreenVisibilityChange[%2]. hr = %3\r\n
0xb000183d | %1 - UITaskHandler::OnSipVisibilityChange[%2]. hr = %3\r\n
0xb000183e | %1 - UITaskHandler::OnShowAnimationComplete\r\n
0xb000183f | %1 - UITaskHandler::Window.Visible property changed [%2]\r\n
0xb0001840 | %1 - FreezeHost event triggered\r\n
0xb0001841 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001842 | %1 - CancelTask TaskId=%2\r\n
0xb0001843 | %1 - OnHostPausing\r\n
0xb0001844 | %1 - OnHostPausing failed with hr = %2\r\n
0xb0001845 | %1 - OnHostPaused\r\n
0xb0001846 | %1 - OnHostPaused failed with hr = %2\r\n
0xb0001847 | %1 - FreezeHost event triggered\r\n
0xb0001848 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001849 | %1 - CancelTask received while executing in background\r\n
0xb000184a | %1 - CancelTask received. Ignoring since this is a valid transition only when running in background\r\n
0xb000184b | %1 - CancelTask hr = %2\r\n
0xb000184c | %1 - TPA entry: %2\\%3%4;\r\n
0xb000184d | %1 - Platform Assemblies List: %2\r\n
0xb000184e | %1 - ParseManifestFile HResult = %2\r\n
0xb000184f | %1 - NotifyError ! Unable to disable NI optimizations\r\n
0xb0001850 | %1 - NotifyError ! Unable to set the debugger wait env variable\r\n
0xb0001851 | %1 - TestTrustedPath: %2\r\n
0xb0001852 | %1 - TestAppPaths: %2\r\n
0xb0001853 | %1 - NotifyError ! Failed to set the test settings\r\n
0xb0001854 | %1 - GetAppPaths failed with hr = %2\r\n
0xb0001855 | %1 - NotifyError ! message = %2, source = %3\r\n
0xb0001856 | %1 - NotifyError ! hr=%2. message = %3\r\n
0xb0001857 | %1 - GetIsoStoreAvailableFreeSpace hr = %2\r\n
0xb0001858 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb0001859 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb000185a | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185b | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185c | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb000185d | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb000185e | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb000185f | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb0001860 | %1 - GetQualifiedMutexName returned:[%2]. AllowedMutexCount:[%3]\r\n\r\n
0xb0001861 | %1 - XcpHost::Start() failed with hr = %2\r\n
0xb0001862 | %1 - Shutting down the SL runtime...\r\n
0xb0001863 | %1 - Calling into XcpHost::Pausing %2\r\n
0xb0001864 | %1 - XcpHost::Pausing %2\r\n
0xb0001865 | %1 - Calling into XcpHost::Pause %2\r\n
0xb0001866 | %1 - XcpHost::Pause %2\r\n
0xb0001867 | %1 - Calling into XcpHost::Resume %2\r\n
0xb0001868 | %1 - XcpHost::Resume %2\r\n
0xb0001869 | %1 - Calling into XcpHost::Resumed %2\r\n
0xb000186a | %1 - XcpHost::Resumed %2\r\n
0xb000186b | %1 - XcpHost::CompleteTask called TaskID:[%2]\r\n
0xb000186c | %1 - CompleteTask called when XcpTask is null. This likely indicates CompleteTask getting called twice\r\n
0xb000186d | %1 - Error in OnApplicationStarted\r\n
0xb000186e | %1 - Error in OnApplicationConstructing\r\n
0xb000186f | %1 - LaunchSession hr = %2\r\n
0xb0001870 | %1 - LaunchChildTask hr = %2\r\n
0xb0001871 | %1 - Raising Task.OnLaunching\r\n
0xb0001872 | %1 - Raised Task.OnLaunching\r\n
0xb0001873 | %1 - Raising Task.OnPause. PauseReason[%2]\r\n
0xb0001874 | %1 - Raised Task.OnPause\r\n
0xb0001875 | %1 - Raising Task.OnResume. IsExecutionContextPreserved[%2]\r\n
0xb0001876 | %1 - Raised Task.OnResume\r\n
0xb0001877 | %1 - Raising Task.OnRunningInBackground\r\n
0xb0001878 | %1 - Raised Task.OnRunningInBackground\r\n
0xb0001879 | %1 - Raising Task.OnCancel\r\n
0xb000187a | %1 - Raised Task.OnCancel\r\n
0xb000187b | %1 - Raising Task.OnHostDehydarting\r\n
0xb000187c | %1 - Raised Task.OnHostDehydarting\r\n
0xb000187d | %1 - Raising Task.OnNavigateTo\r\n
0xb000187e | %1 - Raised Task.OnNavigateTo\r\n
0xb000187f | %1 - Raising Task.OnNavigateAway\r\n
0xb0001880 | %1 - Raised Task.OnNavigateAway\r\n
0xb0001881 | %1 - Raising Task.OnShow\r\n
0xb0001882 | %1 - Raised Task.OnShow\r\n
0xb0001883 | %1 - Raising Task.OnHide\r\n
0xb0001884 | %1 - Raised Task.OnHide\r\n
0xb0001885 | %1 - Raising Task.OnSystemKeyPressed\r\n
0xb0001886 | %1 - Raised Task.OnSystemKeyPressed\r\n
0xb0001887 | %1 - Raising Task.OnChildTaskReturned\r\n
0xb0001888 | %1 - Raised Task.OnChildTaskReturned\r\n
0xb0001889 | %1 - Raising Task.OnObscurityChange\r\n
0xb000188a | %1 - Raised Task.OnObscurityChange\r\n
0xb000188b | %1 - Raising Task.OnLockScreenVisibilityChange\r\n
0xb000188c | %1 - Raised Task.OnLockScreenVisibilityChange\r\n
0xb000188d | %1 - Raising Task.OnClosing\r\n
0xb000188e | %1 - Raised Task.OnClosing\r\n
0xb000188f | %1 - RegisterAppCallbacks hr = %2\r\n
0xb0001890 | %1 - RegisterTaskCallbacks hr = %2\r\n
0xb0001891 | %1 - TaskReadyToShow hr = %2\r\n
0xb0001892 | %1 - RequestCloseTask hr = %2\r\n
0xb0001893 | %1 - CompleteTask hr = %2\r\n
0xb0001894 | %1 - DestroyTaskCallbacks hr = %2\r\n
0xb0001895 | %1 - SetHostErrorCode hrHostError = %2, hr = %3\r\n
0xb0001896 | %1 - LaunchSession[%2] hr = %3\r\n
0xb0001897 | %1 - GetTaskState hr = %2\r\n
0xb0001898 | %1 - SetTaskState hr = %2\r\n
0xb0001899 | %1 - LaunchChildTask[%2] hr = %3\r\n
0xb000189a | %1 - GetTaskAppChromeHandle hr = %2\r\n
0xb000189b | %1 - SetTaskPauseOnLock hr = %2\r\n
0xb000189c | %1 - SetHostObscurity[%2] hr = %3\r\n
0xb000189d | %1 - Entering Modal state\r\n
0xb000189e | %1 - Exiting Modal state hr = %2\r\n
0xb000189f | %1 - NotifyError: message=%2, source=%3\r\n
0xb00018a0 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb00018a1 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb00018a2 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a3 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a4 | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb00018a5 | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb00018a6 | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb00018a7 | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb00018a8 | %1 - Raising Task.OnRefresh\r\n
0xb00018a9 | %1 - Raised Task.OnRefresh\r\n
0xb00018aa | %1 - UITaskHandler::RequestNavigateBack called TaskID:[%2]\r\n
0xb00018ab | %1 - UITaskHandler::RequestNavigateBack hr = %2\r\n
0xb00018ac | %1 - RequestNavigateBack hr = %2\r\n
0xb00018ad | %1 - UITaskHandler::SetFullScreen[%2] called TaskID:[%3]\r\n
0xb00018ae | %1 - UITaskHandler::SetFullScreen hr = %2\r\n
0xb00018af | %1 - SetTaskFullScreen hr = %2\r\n
0xb00018b0 | %1 - Raising Task.OnApplicationLayerChange\r\n
0xb00018b1 | %1 - Raised Task.OnApplicationLayerChange\r\n
0xb00018b2 | %1 - Raising Task.OnRequestOverlayStateChange. State=%2\r\n
0xb00018b3 | %1 - Raised Task.OnRequestOverlayStateChange\r\n
0xb00018b4 | %1 - ApplicationLayerChanged NewApplicationLayer=%2\r\n
0xb00018b5 | %1 - ApplicationLayerChange received before RuntimeHostTask is set\r\n
0xb00018b6 | %1 - AgTaskHandler::LaunchSession hr = %2\r\n
0xb00018b7 | %1 - AgTaskHandler::LaunchChildTask hr = %2\r\n
0xb00018b8 | %1 - GetSessionDisplayName. DisplayName=%2 hr = %3\r\n
0xb00018b9 | %1 - AgTaskHandler::ConnectionComplete received\r\n
0xb00018ba | %1 - AgTaskHandler::ConnectionComplete hr = %2\r\n
0xb00018bb | %1 - UITaskHandler::OnNavigationBarVisibilityChange[%2]. hr = %3\r\n
0xb00018bc | %1 - Raising Task.OnModernActivation\r\n
0xb00018bd | %1 - Raised Task.OnModernActivation\r\n
0xb00018be | %1 - UITaskHandler::LaunchModernChooser hr = %2\r\n
0xb00018bf | %1 - LaunchChildTask hr = %2\r\n
0xb00018c0 | %1 - LaunchModernChooser[%2] hr = %3\r\n
0xb00018c1 | %1 - TaskFirstPresentCompleted = %2\r\n
0xb00018c2 | %1 - UITaskHandler::FirstPresentCompleted called TaskID:[%2]\r\n
0xb00018c3 | %1 - UITaskHandler::FirstPresentCompleted hr = %2\r\n
0xb0001fa4 | AgHost - FrameworkView::Initialize HRESULT=%1\r\n
0xb0001fa5 | AgHost - FrameworkView::SetWindow HRESULT=%1\r\n
0xb0001fa6 | AgHost - FrameworkView::Load HRESULT=%1\r\n
0xb0001fa7 | AgHost - FrameworkView::Run HRESULT=%1\r\n
0xb0001fa8 | AgHost - FrameworkView::Uninitialize HRESULT=%1\r\n
0xb0001fa9 | AgHost - FrameworkView::OnActivated PreviousExecutionState=%1 ActivationKind=%2 HRESULT=%3\r\n
0xb0001faa | AgHost - FrameworkView::OnExiting HRESULT=%1\r\n
0xb0001fab | AgHost - FrameworkView::OnResuming HRESULT=%1\r\n
0xb0001fac | AgHost - FrameworkView::OnSuspending HRESULT=%1\r\n
0xb0001fae | AgHostSvcs - EmCancelTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001faf | AgHostSvcs - EmCreateTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb0 | AgHostSvcs - EmExitTaskHost HRESULT=%1\r\n
0xb0001fb1 | AgHostSvcs - EmPauseTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb2 | AgHostSvcs - EmResumeTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb3 | AgHostSvcs - EmSetTaskInstanceApplicationUri TaskID=%1 ApplicationUri=%2 HRESULT=%3\r\n
0xb0001fb4 | AgHostSvcs - EmSetTaskInstanceArguments TaskID=%1 HRESULT=%2\r\n
0xb0001fb5 | AgHostSvcs - EmSetTaskInstanceBackgroundTaskId TaskID=%1 BackgroundTaskID=%2 HRESULT=%3\r\n
0xb0001fb6 | AgHostSvcs - EmSetTaskInstanceNavigationPage TaskID=%1 NavigationPage=%2 HRESULT=%3\r\n
0xb0001fb7 | AgHostSvcs - EmStartTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb8 | AgHostSvcs - TaskCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fb9 | AgHostSvcs - TaskPaused TaskID=%1 HRESULT=%2\r\n
0xb0001fba | AgHostSvcs - TaskRunning TaskID=%1 HRESULT=%2\r\n
0xb0001fbb | AgHostSvcs - TaskRunningInBackground TaskID=%1 HRESULT=%2\r\n
0xb0001fbc | AgHostSvcs - TaskRunningInForeground TaskID=%1 HRESULT=%2\r\n
0xb0001fbd | AgHostSvcs - EmWaitForTaskInstanceCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fbe | AgHostSvcs - OnModernContractActivation TaskID=%1 HRESULT=%2\r\n
0xb0002008 | EEC: GetExtendedExecutionBroker ProcessId=%1 HRESULT=%2\r\n
0xb0002009 | EEC: RegisterRevokedHandler ProcessId=%1 HRESULT=%2\r\n
0xb000200a | EEC: RequestExtendedExecution ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200b | EEC: ExtensionRevokedCallback ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200c | EEC: CompleteExtendedExecution ProcessId=%1 HRESULT=%2\r\n
0xb000206c | ODB: LaunchTask - UserSid: %1 SessionId: %2 PackageFullName: %3 EntryPoint: %4 WorkItemId: %5 HRESULT: %6.\r\n
0xb000206d | ODB: CancelTask - UserSid: %1 SessionId: %2 WorkItemId: %3 RudeTerminate: %4 CancellationReason: %5 HRESULT: %6.\r\n
0xb000206e | ODB: BeforeTaskActivated - WorkItemId: %1 PsmKey: %2 HostJobType: %3 HRESULT: %4.\r\n
0xb000206f | ODB: TaskActivated - WorkItemId: %1 TaskInstanceId: %2 PsmKey: %3 HRESULT: %4.\r\n
0xb0002070 | ODB: TaskCompleted - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002071 | ODB: TaskCanceled - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002072 | ODB: Timeout in WaitForWnfStateQuiescentTimeout.\r\n
0xb0002073 | ODB: CancelBackgroundTaskWithWnf WorkItemId: %1.\r\n
0xb0002710 | %1\r\n
0xb0002711 | %1: %2\r\n
0xb0002712 | *** ExecFailFast ***   %1\r\n
0xb000271a | PreInstallTaskPolicy: Activate task for User = %1 HRESULT = %2\r\n
0xb000271b | PreInstallTaskPolicy: BiActivate WorkItemId = %1 for user = %2, PackageFullName = %3, EntryPoint = %4, HRESULT = %5\r\n
0xb0010205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1' WorkItemId='%2;' CallbackId='%3' HostId='%5' ResourceSetId='%6'.\r\n
0xb0010206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1' HostId='%3' ResourceSetId='%4'.\r\n
0xd0000001 | Resumed\r\n
0xd0000002 | Quiescing\r\n
0xd0000003 | Quiesced\r\n
0xd0000004 | Frozen\r\n
0xd0000005 | Dehydrated\r\n
0xd0000006 | Terminated\r\n
0xd0000007 | Resumed\r\n
0xd0000008 | Suspending\r\n
0xd0000009 | Suspended\r\n
0xd000000a | Terminated\r\n
0xd000000b | NotBackground\r\n
0xd000000c | MixedHost\r\n
0xd000000d | PureHost\r\n
0xd000000e | SystemHost\r\n
0xd000000f | InvalidType\r\n
0xd0000010 | Permitted\r\n
0xd0000011 | Buffered\r\n
0xd0000012 | Dropped\r\n
0xd0000013 | InvalidType\r\n
0xd0000014 | Invalid\r\n
0xd0000015 | ForegroundApp\r\n
0xd0000016 | Cbe\r\n
0xd0000017 | ForegroundAgent\r\n
0xd0000018 | GbaPeriodic\r\n
0xd0000019 | GbaIdle\r\n
0xd000001a | BackgroundAudio\r\n
0xd000001b | BackgroundWorker\r\n
0xd000001c | Voip\r\n
0xd000001d | Oem\r\n
0xd000001e | Invalid\r\n
0xd000001f | Started\r\n
0xd0000020 | Paused\r\n
0xd0000021 | Resumed\r\n
0xd0000022 | MovedToBackground\r\n
0xd0000023 | RunUnderLock\r\n
0xd0000024 | Invalid\r\n
0xd0000025 | OK\r\n
0xd0000026 | Abort\r\n
0xd0000027 | Unexpected\r\n
0xd0000028 | ExceededRuntime\r\n
0xd0000029 | ResourcesSeized\r\n
0xd000002a | Paused\r\n
0xd000002b | Resumed\r\n
0xd000002c | ScreenLock\r\n
0xd000002d | ScreenUnlocked\r\n
0xd000002e | MovedToBackground\r\n
0xd000002f | CbeExitTimeout\r\n
0xd0000030 | CbeExitBatterySaver\r\n
0xd0000031 | CbeExitParallelAgentPolicy\r\n
0xd0000032 | CbeExitResourcesUnavailable\r\n
0xd0000033 | CbeExitControlPanel\r\n
0xd0000034 | CbeExitBandwidthSavings\r\n
0xd0000035 | HeadlessHost\r\n
0xd0000036 | TaskHost\r\n
0xd0000037 | XcpHost\r\n
0xd0000038 | TaskHostSvcs\r\n
0xd0000039 | TaskHostUnitTests\r\n
0xd000003a | HOST_CREATED\r\n
0xd000003b | HOST_INITIALIZED\r\n
0xd000003c | HOST_RUNNING\r\n
0xd000003d | STARTING_TASK\r\n
0xd000003e | REHYDRATING_TASK\r\n
0xd000003f | HOST_READY\r\n
0xd0000040 | HOST_PAUSING\r\n
0xd0000041 | PAUSING_TASK\r\n
0xd0000042 | PAUSED_TASK\r\n
0xd0000043 | HOST_PAUSED\r\n
0xd0000044 | RESUMING_TASK\r\n
0xd0000045 | HOST_GOING_IN_BACKGROUND\r\n
0xd0000046 | TASK_GOING_IN_BACKGROUND\r\n
0xd0000047 | HOST_IN_BACKGROUND\r\n
0xd0000048 | TASK_GOING_IN_FOREGROUND\r\n
0xd0000049 | GRACEFULLY_DEHYDRATING_HOST\r\n
0xd000004a | HOST_VISIBLE\r\n
0xd000004b | HOST_HIDDEN\r\n
0xd000004c | HOST_FROZEN\r\n
0xd000004d | HOST_THAWED\r\n
0xd000004e | HOST_EXITING\r\n
0xd000004f | HOST_ERROR\r\n
0xd0000050 | Direction_Forward\r\n
0xd0000051 | Direction_Backward\r\n
0xd0000052 | Direction_ForceSize\r\n
0xd0000053 | Resumed\r\n
0xd0000054 | Pausing\r\n
0xd0000055 | Paused\r\n
0xd0000056 | Dehydrated\r\n
0xd0000057 | Completed\r\n
0xd0000058 | none\r\n
0xd0000059 | launch\r\n
0xd000005a | debug\r\n
0xd000005b | task completion\r\n
0xd000005c | dependency\r\n
0xd000005d | multi-view\r\n
0xd000005e | Waiting\r\n
0xd000005f | CompletedWithResult\r\n
0xd0000060 | CompletedWithNoResult\r\n
0xd0000061 | Foreground\r\n
0xd0000062 | Lock\r\n
0xd0000063 | Overlay\r\n
0xd0000064 | ModernForeground\r\n
0xd0000065 | Pausing\r\n
0xd0000066 | PausingLowPri\r\n
0xd0000067 | Paused\r\n
0xd0000068 | PausedHighPri\r\n
0xd0000069 | PausedDNK\r\n
0xd000006a | Frozen\r\n
0xd000006b | FrozenHighPri\r\n
0xd000006c | FrozenDNK\r\n
0xd000006d | FrozenDNCS\r\n
0xd000006e | LockScreen\r\n
0xd000006f | Overlay\r\n
0xd0000070 | 11\r\n
0xd0000071 | CalendarAsChild\r\n
0xd0000072 | VideoTranscode\r\n
0xd0000073 | CBE\r\n
0xd0000074 | GenericExtendedExecution\r\n
0xd0000075 | ModernForegroundExtended\r\n
0xd0000076 | TaskCompletionHighPriority\r\n
0xd0000077 | ModernForegroundLarge\r\n
0xd0000078 | ShellCustom1\r\n
0xd0000079 | ShellCustom2\r\n
0xd000007a | ShellCustom3\r\n
0xd000007b | ShellCustom4\r\n
0xd000007c | Composer\r\n
0xd000007d | DebugModeForeground\r\n
0xd000007e | ComponentTarget\r\n
0xd000007f | PiP\r\n
0xd0000080 | Balloon\r\n
0xd0000081 | Invalid\r\n
0xd0000082 | Unevaluated\r\n
0xd0000083 | EvaluationPending\r\n
0xd0000084 | Evaluated\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x10000006 | ExecMan\r\n
0x10000009 | TaskHost\r\n
0x1000000d | Sqm\r\n
0x1000000f | Lifetime Manager\r\n
0x10000010 | ForegroundManager\r\n
0x10000011 | Background Manager\r\n
0x10000012 | Production Circular\r\n
0x10000013 | Production Critical\r\n
0x10000014 | SelfHost Circular\r\n
0x10000015 | SelfHost Critical\r\n
0x10000016 | DevPlat Circular\r\n
0x10000017 | VOIP\r\n
0x1000001b | Activation Manager\r\n
0x1000001c | AgHost\r\n
0x10000020 | Telemetry\r\n
0x10000021 | ExtendedExecutionClient\r\n
0x10000022 | OnDemandBroker\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000007 | Resume\r\n
0x30000008 | Suspend\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000048 | Background Access User State Changed\r\n
0x70000049 | Background Access Package State Changed\r\n
0x90000001 | Microsoft-Windows-AppModelExecEvents\r\n
0xb0000064 | DepMgr: Removed suspension group from the graph, PsmKey=%1\r\n
0xb0000065 | Not set app %1 into halted state because it should wait for other apps in the package halted first\r\n
0xb0000066 | Not set app %1 into halted state because other app in the package have not finished quiescing\r\n
0xb0000067 | Not terminate app %1, because target app %2 state = %3\r\n
0xb0000068 | Updated current dependency graph (Removal : %1) with Source %2 and Target %3 for type %4 in return %5\r\n
0xb0000069 | Default time for %1 overridden to %2 ms\r\n
0xb000006a | Creating hang report\r\n
0xb000006b | Window %1 is hung in foreground\r\n
0xb000006c | Window %1 is no longer hung in foreground\r\n
0xb000006d | Waiting for WER reporting to finish on app %1\r\n
0xb000006e | Hang reporting finished on app %1.  App termination status: %2\r\n
0xb000006f | Hung reporting finished on window %1 with result %2\r\n
0xb0000070 | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb0000071 | _SubmitActivationHangWerReport(stop): Aumid=%1, result=%2\r\n
0xb0000072 | _UnregisterForStateChanges: fPackageLevel=%1, HRESULT is %2. Cookie is %3\r\n
0xb0000073 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000074 | Canceled launch grace timer, PsmKey=%1\r\n
0xb0000075 | _InitializeLaunchGraceContext: Aumid=%1, fExtendedLaunch=%2, fEventExists=%3\r\n
0xb0000076 | App %1 successfully launched and its launch grace period expired: removing suspend exemption\r\n
0xb0000077 | Forcefully terminating app, Aumid=%1 flags=%2, reason=%3\r\n
0xb0000078 | CheckTerminationBeforeSwitch: Should terminate: %1, Aumid=%2, HRESULT=%3, reason=%4, fIsMisbehaving=%5\r\n
0xb0000079 | Termination requested for %1 - flags %2\r\n
0xb000007a | Failing TerminateApp due to pending task completions: %1\r\n
0xb000007b | Terminating %1 immediately\r\n
0xb000007c | Uninstalling background work items for %1\r\n
0xb000007d | Termination of %1 scheduled for %2 ms in future\r\n
0xb000007e | Sent window message to the default immersive browser with HRESULT %1\r\n
0xb000007f | Attempting to terminate app %1 prior to new app launch due to pending termination\r\n
0xb0000080 | EvaluateAndTerminatePid: PID: %1. HRESULT: %2. Package State: %3\r\n
0xb0000081 | Exempting application %1 from suspend while it is being launched\r\n
0xb0000082 | Exemption manager %1 is requesting a higher minimum priority %2 for %3\r\n
0xb0000083 | Debug mode is enabled for %1, so it will run at %2 priority\r\n
0xb0000084 | Handling logoff, %1 will run at %2 priority\r\n
0xb0000085 | Throttling has been disabled, so %1 will run at %2 priority\r\n
0xb0000086 | Suspend denied due to new key debounce, PsmKey=%1\r\n
0xb0000087 | Suspend denied due to debug mode, PsmKey=%1\r\n
0xb0000088 | Not suspending application %1 due to exemption %2\r\n
0xb0000089 | _EvaluateAndSuspendApplication: PsmKey=%1, fIsSuspendAllowed=%2, HRESULT=%3\r\n
0xb000008a | _ReevaluatePolicy: Ignoring debug mode app, PsmKey=%1\r\n
0xb000008b | ManagePreExistingApps(start)\r\n
0xb000008c | ManagePreExistingApps: PsmKey=%1, Aumid=%2, hr=%3\r\n
0xb000008d | ManagePreExistingApps(stop)\r\n
0xb000008e | RequestSuspendTimeout called for application %1 and timeout %2\r\n
0xb000008f | Debug mode enabled, PkgFamilyName=%1\r\n
0xb0000090 | Debug mode disabled, PkgFamilyName=%1\r\n
0xb0000091 | Set Package %1, Timeout to %2\r\n
0xb0000092 | ResumeDebugModePackage(start): package=%1\r\n
0xb0000093 | ResumeDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000094 | SuspendDebugModePackage(start): package=%1\r\n
0xb0000095 | SuspendDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000096 | MultiAppSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000097 | MultiAppSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb0000098 | MultiPackageSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000099 | MultiPackageSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009a | MultiPackageSuspendAndPendTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb000009b | MultiPackageSuspendAndPendTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009c | TerminateSync(start): PsmKey=%1, type=%2, reason=%3\r\n
0xb000009d | TerminateSync(stop): PsmKey=%1, hrLogReason=%2, hrTermination=%3\r\n
0xb000009e | TerminatePackageSync(start): Package=%1, type=%2, reason=%3\r\n
0xb000009f | TerminatePackageSync(stop): Package=%1, fPlmKnowsPackage=%2, HRESULT=%3\r\n
0xb00000a0 | _TerminateAllSuspendedApplications(start)\r\n
0xb00000a1 | _TerminateAllSuspendedApplications(stop): HRESULT=%1\r\n
0xb00000a2 | Application %1 is blocking Connected Standby\r\n
0xb00000a3 | Exiting Connected Standby\r\n
0xb00000a4 | All packages have been suspended or terminated. Notify PDC. Call to PdcNotificationClientAcknowledge() returned %1\r\n
0xb00000a5 | Kernel State Change Callback: There were %1 PIDs present in the callback data\r\n
0xb00000a6 | Kernel State Change Callback: The state source was %1\r\n
0xb00000a7 | PDC_CONTROL_ABORT: PdcNotificationClientAcknowledge(STATUS_SUCCESS) returned %1\r\n
0xb00000a8 | Not terminating application %1 in _EvaluateAndTerminateApplication because it contains a running IImmersiveApplication\r\n
0xb00000a9 | Not terminating application %1 in _EvaluateAndTerminateApplication because it is a long running app\r\n
0xb00000aa | Not terminating application %1 in _EvaluateAndTerminateApplication due to pending task completion\r\n
0xb00000ab | Not terminating application %1 in _EvaluateAndTerminateApplication due to Launch Grace\r\n
0xb00000ac | Not terminating application %1 in _EvaluateAndTerminateApplication due to debug mode\r\n
0xb00000ad | Not terminating application %1 in _EvaluateAndTerminateApplication due to application had already been terminated\r\n
0xb00000ae | _EvaluateAndTerminateApplication: Skipping child suspension group, PsmKey=%1\r\n
0xb00000af | An empty application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b0 | Parent allowed suspension for child app, childPsmKey=%1\r\n
0xb00000b1 | GroupChildWithParent: ChildPsmKey=%1, HRESULT=%2\r\n
0xb00000b2 | Call a command line '%1' to notify default browser with result %2\r\n
0xb00000b3 | Read executable path from registry with result %1\r\n
0xb00000b4 | Application %1 was added to PLM Data Store and registering for PSM notification\r\n
0xb00000b5 | Resume the PPLE app %1 when receiving the PSM new key notification\r\n
0xb00000b6 | An orphaned prereq application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b7 | Not terminating dependent application %1 in _EvaluateAndTerminateDependentApplication due other dependency applications\r\n
0xb00000b8 | _EvaluateAndTerminateSourceApplication: Aumid=%1, exemption=%2\r\n
0xb00000b9 | An force termination exemption Application was detected. Setting pending termination for application %1\r\n
0xb00000ba | StateMgr: State queued, PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000bb | StateMgr: OnApplicationStarted set to active, PsmKey=%1\r\n
0xb00000bc | StateMgr: OnApplicationStarted finished, PsmKey=%1, HRESULT=%2\r\n
0xb00000bd | StateMgr: App's current state has changed, PsmKey=%1, state=%2\r\n
0xb00000be | StateMgr: OnApplicationTerminated(start), PsmKey=%1\r\n
0xb00000bf | StateMgr: Application terminated signaled, PsmKey=%1\r\n
0xb00000c0 | StateMgr: OnApplicationTerminated(stop), PsmKey=%1\r\n
0xb00000c1 | StateMgr: GetTerminateSyncData, PsmKey=%1, hr=%2\r\n
0xb00000c2 | StateMgr: _ProcessStateQueue(start): PsmKey=%1, state=%2\r\n
0xb00000c3 | StateMgr: _ProcessStateQueue(stop): PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000c4 | StateMgr: Queue's pause state has changed to %2, PsmKey=%1\r\n
0xb00000c5 | StateMgr: App's committed state has changed, PsmKey=%1, state=%2\r\n
0xb00000c6 | Enabling debug mode on package %1\r\n
0xb00000c7 | Disabling debug mode on package %1\r\n
0xb00000c8 | Suspending package %1 via debug API. HRESULT: %2\r\n
0xb00000c9 | Resuming package %1 via debug API. HRESULT: %2\r\n
0xb00000ca | Terminating package %1 via debug API. HRESULT: %2\r\n
0xb00000cb | Default time for %1 overridden to %2 ms\r\n
0xb00000cc | ReportActivationHangSync: Halt application Aumid=%1, result=%2\r\n
0xb00000cd | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb00000ce | _SubmitActivationHangWerReport(stop): Aumid=%1 canceled(%2) result=%3\r\n
0xb00000cf | PLM doesn't swap out application %1 due to its swap state %2\r\n
0xb00000d0 | PLM termination policy started on background thread because application %1 failed to outswap\r\n
0xb00000d1 | PLM termination policy finished. Outswapping returned status %1\r\n
0xb00000d2 | PLM memory policy will be aggressive because this is a disconnected session\r\n
0xb00000d3 | PLM termination policy start\r\n
0xb00000d4 | PLM termination policy stop\r\n
0xb00000d5 | PLM termination policy triggered by in use memory of %1 MiB\r\n
0xb00000d6 | PLM termination policy triggered by commit charge of %1 MiB\r\n
0xb00000d7 | MemoryPolicyWatcherTerminateCommitCharge\r\n
0xb00000d8 | PLM empty policy triggered by in use memory of %1 MB\r\n
0xb00000d9 | PLM memory policy does not allow termination of application %1 for reason %2\r\n
0xb00000da | PLM memory policy allows termination of application %1\r\n
0xb00000db | Application %1 was hidden %2 seconds ago\r\n
0xb00000dc | Application %1 is the clipboard owner\r\n
0xb00000dd | PLM empty policy start\r\n
0xb00000de | PLM empty policy ignoring application %1 with error code %2\r\n
0xb00000df | PLM empty policy finished after emptying %1 MiB\r\n
0xb00000e0 | PLM termination policy enumerated %1 applications\r\n
0xb00000e1 | PLM memory policy chose application %1 as its termination candidate, over old candidate application %2\r\n
0xb00000e2 | PLM memory policy will terminate application %1 with memory size %2 MiB and score %3\r\n
0xb00000e3 | PLM memory policy received MemWatcher event\r\n
0xb00000e4 | PLM memory policy received MemWatcher event\r\n
0xb00000e5 | Package exemption manager denied suspend for %1.  Ref counts are LAUNCH=%2, PSMREG=%3, PSMPENDING=%4\r\n
0xb00000e6 | Package Exemption Manager: ReferenceAdded:%1, %2 ref to application %3. The ref counts are now LAUNCH=%4, PSMREG=%5, and PSMREGPENDING=%6\r\n
0xb00000e7 | Package %1 added to the package data store\r\n
0xb00000e8 | Resetting priority to unpause the suspension group, PsmKey=%1\r\n
0xb00000e9 | Changed the priority of %1 to %2\r\n
0xb00000ea | AllowServiceOfPackages(start): cPackages=%1, fNotifyBi=%2\r\n
0xb00000eb | AllowServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ec | FinishedServiceOfPackages(start): cPackages=%1\r\n
0xb00000ed | FinishedServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ee | AllowUninstallOfPackage(start): package=%1\r\n
0xb00000ef | AllowUninstallOfPackage(stop): package=%1, HRESULT=%2\r\n
0xb00000f0 | Forcefully terminating misbehaving app %1 due to activation failure %2\r\n
0xb00000f1 | App %1: Change = %2\r\n
0xb00000f2 | PsmKey %1 has state %2\r\n
0xb00000f3 | Changing app state through BI, PsmKey=%1, state=%2 terminate action=%3\r\n
0xb00000f4 | Changing the package state of %1 through BI to %2\r\n
0xb00000f5 | OnAfterQuiescing: Quiesce began for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f6 | _CompleteQuiesceHelper: Queued termination for timed-out PsmKey %1\r\n
0xb00000f7 | Quiesce completed for PsmKey=%1, reason=%2, suspendTrigger=%3\r\n
0xb00000f8 | Suspend trigger updated for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f9 | ExtendQuiesceTimeout: PsmKey=%1, request=%2 ms, HRESULT=%3\r\n
0xb00000fa | _CompleteQuiesceHelper: Ignore timed-out PsmKey %1 as is being debugged\r\n
0xb00000fb | ResumeHelper: Application resume(start), PsmKey=%1, reason=%2\r\n
0xb00000fc | ResumeHelper: Application resume(stop), PsmKey=%1, reason=%2, HRESULT=%3\r\n
0xb00000fd | Resume reason updated for PsmKey=%1, reason=%2\r\n
0xb00000fe | RPC 0->1 transition detected for %1\r\n
0xb00000ff | RPC exemption was granted for application %1. KernelRequest Value: %2. Runaway RPC: %3.  RPC Debounce %4\r\n
0xb0000100 | RPC debounce received for package %1\r\n
0xb0000101 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000102 | Application %1 termination is blocked. PreserverProcessRequest = %2, TaskCompletionCategory = %3\r\n
0xb0000103 | PdcSystem activation (Activate = %1). Result = %2\r\n
0xb0000104 | NetworkAudio entries: %1, IsNetworkReferenced: %2\r\n
0xb0000105 | App %1 is Sharing\r\n
0xb0000106 | Share %1 has started in app %2\r\n
0xb0000107 | Share %1 in app %2 has stopped\r\n
0xb0000108 | Queued termination reason updated for PsmKey=%1, reason=%2\r\n
0xb0000109 | ClearTerminationTypesForForgottenPackage(start): PkgFamilyName=%1\r\n
0xb000010a | Cleared termination type for forgotten app, Aumid=%1, HRESULT=%2\r\n
0xb000010b | ClearTerminationTypesForForgottenPackage(stop): PkgFamilyName=%1, HRESULT=%2\r\n
0xb000010c | Writing to termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010d | Reading termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010e | _ExtendForResourceStarvation: PsmKey=%1, TimerType=%2, newRelativeExpirationTimeMs=%3, ElapsedMs=%4, CpuRunningMs=%5, CpuReadyMs=%6, IoNormalMs=%7\r\n
0xb000010f | Foreground resume delay %1 milliseconds\r\n
0xb0000110 | Suspend allowed for %1 - Session not active\r\n
0xb0000111 | Suspend denied due to a visible window or visibility debounce, PsmKey=%1\r\n
0xb0000112 | Suspend denied for %1 - UserRequest non-zero\r\n
0xb0000113 | Suspend denied for %1- failure %2\r\n
0xb0000114 | OnWindowChanged: Aumid=%1, Hwnd=%2, change=%3, fDeferredVisibility=%4, HRESULT=%5\r\n
0xb0000115 | Starting Session Idle Debounce\r\n
0xb0000116 | Session is active\r\n
0xb0000117 | Session is idle\r\n
0xb0000118 | PlmGetPackageFullNameFromAppId, Aumid=%1, HRESULT=%2\r\n
0xb0000119 | Session idle state change -- calling _ReevaluatePolicy\r\n
0xb000011a | RegisterForActivationStateChanges: Act:%1 App:%2 HRESULT is %3. Cookie is %4\r\n
0xb000011b | UnregisterForActivationStateChanges: Cookie is %1\r\n
0xb000011c | Can Auto Terminate app %1 %2\r\n
0xb000011d | TerminateApplicationBeforeActivation(start): Aumid=%1\r\n
0xb000011e | TerminateApplicationBeforeActivation: wait for terminate, Aumid=%1, HRESULT=%2\r\n
0xb000011f | TerminateApplicationBeforeActivation(stop): Aumid=%1, reason=%2, HRESULT=%3\r\n
0xb0000120 | s_SuspendPackagesAtLogOff(start)\r\n
0xb0000121 | s_SuspendPackagesAtLogOff(stop): HRESULT=%1\r\n
0xb0000122 | StateMgr: OnApplicationStarted still halted, PsmKey=%1\r\n
0xb0000123 | Added Task Completion under %1 for application %2\r\n
0xb0000124 | Removed Task Completion under %1 for application %2\r\n
0xb0000125 | Illegal state change happened to App: %1\r\n
0xb0000126 | EnableDebugMode failed: %1\r\n
0xb0000127 | DisableDebugMode: RoDisableDebuggingForPackage failed with result %1\r\n
0xb0000128 | DisableDebugMode: OnDebugModeDisabled failed with result %1\r\n
0xb0000129 | DisableDebugMode: Enabling activation timeout failed with result %1\r\n
0xb000012a | DisableDebugMode failed: %1\r\n
0xb000012b | Couldn't open process: %1\r\n
0xb000012c | PLM failed to process a hang for window %1 with error code %2\r\n
0xb000012d | PLM outswap application %1 failed to invoke with error code %2\r\n
0xb000012e | PLM couldn't find any process for application %1, and handle it as non-large app\r\n
0xb000012f | PLM failed to decide application %1 is large or not with error code %2\r\n
0xb0000130 | PLM empty policy failed to process application %1 with error code %2.  Ignoring the application\r\n
0xb0000131 | PLM empty policy failed to empty application %1 with error code %2\r\n
0xb0000132 | PLM failed to terminate application %1 as empty policy with error code %2\r\n
0xb0000133 | PLM empty policy failed to enumerate applications with error code %1\r\n
0xb0000134 | PLM termination policy skipping application %1, which is not registered with PLM\r\n
0xb0000135 | PLM memory policy failed to queue work with error code %1\r\n
0xb0000136 | GetPackageData called on a Package %1, which is not in the PLM Package Data Store\r\n
0xb0000137 | ERROR: Failed to set priority to %1, PsmKey=%2, NTSTATUS=%3\r\n
0xb0000138 | AllowServiceOfPackages: Failed to terminate package=%1, type=%2, HRESULT=%3\r\n
0xb0000139 | _CheckServicingPackages: Failed to enumerate app, PsmKey=%1, HRESULT=%2\r\n
0xb000013a | _CheckServicingPackages: Failed to enumerate package, PkgFullName=%1, HRESULT=%2\r\n
0xb000013b | GetImmersiveApplicationCount failed with error code %1\r\n
0xb000013c | Background workitems were force terminated, PsmKey=%1\r\n
0xb000013d | ChangeApplicationBiState failed: %1\r\n
0xb000013e | Background workitems for package %1 were force terminated\r\n
0xb000013f | ChangePackageBiState failed: %1\r\n
0xb0000140 | ApplicationProcesses failed to track process ID %1 with error code %2\r\n
0xb0000141 | OnBeforeQuiescing: Failed to allocate memory for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000142 | OnAfterQuiescing: Quiesce failed for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000143 | ERROR: _CompleteQuiesceHelper: Failed to terminate timed-out PsmKey %1 with result %2\r\n
0xb0000144 | ERROR: QuiesceHelper: App forgotten while still Quiescing, PsmKey=%1, suspendTrigger=%2\r\n
0xb0000145 | Failed to query the wake counters associated with application %1. NTSTATUS: %2\r\n
0xb0000146 | _AllAppSyncOperationHelper: Failed to allocate memory for PsmKey=%1, HRESULT=%2\r\n
0xb0000147 | _MultiAppSyncOperationHelper: Failed to perform operation on PsmKey=%1, HRESULT=%2\r\n
0xb0000148 | _MultiAppSyncOperationHelper: Failed in wait, HRESULT=%1\r\n
0xb0000149 | _MultiPackageSyncOperationHelper: Failed to enumerate PsmKey=%1, HRESULT=%2\r\n
0xb000014a | _MultiPackageSyncOperationHelper: Failed to find package in data store, PkgFullName=1%, HRESULT=%2\r\n
0xb000014b | Failed to suspend and terminate apps, cPsmKeys=%1\r\n
0xb000014c | Could not initialize an extended launch grace period for app %1 with HRESULT %2 -- falling back to normal launch grace\r\n
0xb000014d | App %1 failed to show a window after launch. Will attempt to terminate it now\r\n
0xb000014e | Failed to get a window for an app; assuming that the app's window is not hung, Aumid=%1, HRESULT=%2\r\n
0xb000014f | Failed to query hidden time for visibility debounce for app %1 with error code %2\r\n
0xb0000150 | _StartNewKeyDebounce: Error Result=%2, PsmKey=%1\r\n
0xb0000151 | StartTrackingNewApp failed with %1. The application launch is not protected and the app might potentially get suspended inappropriately\r\n
0xb0000152 | ERROR: Failed to enumerate exemption targets starting from PsmKey=%1\r\n
0xb0000153 | Failed to enumerate existing applications from PSM with error code %1\r\n
0xb0000154 | PsmRegisterApplicationNotification failed for application %1 with status %2.  PLM's cache says that the application's registration is: %3\r\n
0xb0000155 | ERROR: Failed to enumerate force termination targets starting from PsmKey=%1, HRESULT=%2\r\n
0xb0000156 | Application %1 failed to be added in PLM Data Store\r\n
0xb0000157 | Failed to initialize string to send app notification %1 state %2\r\n
0xb0000158 | Failed to initialize string to remove app %1\r\n
0xb0000159 | Failed to add %1 for application %2. The application doesn't have BTC_AUDIO background task capability\r\n
0xb000015a | Failed to initialize CmApi\r\n
0xb000015b | Task completion manager failed to add %1 to its sharing cache with error code %2\r\n
0xb000015c | ClearTerminationTypesForForgottenPackage: Failed to clear termination type for app, Aumid=%1, HRESULT=%2\r\n
0xb000015d | ERROR: Failed to schedule the visibility debounce, PsmKey=%1, HRESULT=%2\r\n
0xb000015e | OnWindowChanged ERROR: Failed to queue thread for Aumid=%1, Hwnd=%2, change=%3, HRESULT=%4\r\n
0xb000015f | ERROR: Failed to schedule deferred visibility timer, PsmKey=%1, HRESULT=%2\r\n
0xb0000160 | WaitOnBiNotifyNewSession HRBiNotifyNewSession=%1 HRBiNotifyNewUser=%2\r\n
0xb0000161 | RegisterKernelNotifications HRESULT=%1\r\n
0xb0000162 | TCExemptionManager CompleteInitialization HRESULT=%1\r\n
0xb0000163 | PlmActivationManager CompleteInitialization HRESULT=%1\r\n
0xb0000164 | Plm CSDiagnostics CompleteInitialization HRESULT=%1\r\n
0xb0000165 | Plm LogOff/LogOn Registration HRESULT=%1\r\n
0xb00001f9 | BM: Queued evaluate WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fa | BM: Evaluate returned WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fb | BM: TaskActivated WorkItem: %1 Instance: %2\r\n
0xb00001fc | BM: TaskCompleted WorkItem: %1 Instance: %2\r\n
0xb00001fd | BM: TaskCanceled WorkItem: %1 Instance: %2\r\n
0xb00001fe | BM: Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb00001ff | BM: TaskActivating WorkItem: %1 Instance: %2\r\n
0xb0000200 | BM: Enter %1\r\n
0xb0000201 | BM: Exit %1, HR=%2\r\n
0xb0000202 | BM: TerminateHost WorkItem: %1\r\n
0xb0000203 | BM: ResourceSet invalidated for WorkItem: %1 Instance: %2.  This usually means the host has crashed before a ResourceSet could be applied.\r\n
0xb0000204 | BM: OnAcquired ignoring invalid CallbackId (%1).\r\n
0xb0000205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1'; WorkItemId='%2;' CallbackId='%3'.\r\n
0xb0000206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1'.\r\n
0xb0000207 | BM: OnApplicationStateChanged returning State='%2' PsmKey='%1' HR='%3'.\r\n
0xb0000208 | BM: OnAcquired received for CallbackId: %1\r\n
0xb0000209 | BM: OnAcquired request ignored for CallbackId: %1\r\n
0xb000020a | BM: ActivateDeferredWorkItem WorkItem: %1\r\n
0xb000020b | BM: ActivateDeferredWorkItem discarded WorkItem: %1 because of Status: %2\r\n
0xb000020c | BM: Enter %1 WorkItem: %2\r\n
0xb000020d | BM: Enter %1 WorkItem: %2 TaskInstanceId: %3\r\n
0xb000020e | BM: Exit %1\r\n
0xb000020f | BM: Failed to load settings for event %1.\r\n
0xb0000210 | BM: Failed to load settings for event %1 with error %2.\r\n
0xb0000211 | BM: Failed to load policy for CLSID: %1, for EventType %2 with error %3.\r\n
0xb0000212 | BM: Failed to load the policies with error %1.\r\n
0xb0000213 | BM: Evaluate returned WorkItem: %3 EventType: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb0000214 | BM: TaskWallClockActive WorkItem: %1 Instance: %2\r\n
0xb0000215 | BM: TaskWallClockExpired WorkItem: %1 Instance: %2\r\n
0xb0000216 | BM: Policy returned HRESULT: %3 for WorkItem: %2 PsmKey: %1.\r\n
0xb0000217 | BM: Canceling task for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000218 | BM: Ignoring cancelation request (whitelisted) for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000219 | BM: Session(%1) started, session initialization returned %2.\r\n
0xb000021a | BM: Session(%1) ended.\r\n
0xb000021b | BM: Activation ignored due to no Session(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb000021c | BM: Failed to acquire a ResourceSet for WorkItem: %1 with error %2.\r\n
0xb000021d | BM: WorkItem: %1 is being debugged. Setting wallclock limit to 0.\r\n
0xb000021e | BM: EvaluateActivationAction for WorkItem: %1 HRESULT: %2.\r\n
0xb000021f | BM: Skipped Buffering Exempted task with SQMId: %1 PsmKey: %2.\r\n
0xb0000220 | BM: Dropped Exempted task that came before SessionReady with SQMId: %1 PsmKey: %2.\r\n
0xb0000221 | BM: Activation ignored due to no User(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb0000222 | BM: User Logon Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000223 | BM: User Logoff Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000224 | BM: Pending activation discarded for work item (%1).\r\n
0xb0000225 | BM: Flushing ignored EvaluationState: %1 for WorkItem: %2.\r\n
0xb0000226 | BM: Flushing buffered activations.\r\n
0xb0000227 | BM: Global Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb0000228 | BM: A Session object for Session(%1) already exists.\r\n
0xb0000229 | BM: ShellSuspendState changed, oldState: %1 newState: %2\r\n
0xb000022a | BM: DPLKeyState changed, oldState: %1 newState: %2\r\n
0xb000022b | BM: Canceling WorkItem: %1 due to DPL policy.\r\n
0xb000022c | BM: Dropping activation for WorkItem: %1 due to DPL policy.\r\n
0xb000022d | BM: Buffered activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022e | BM: Exempted activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022f | BM: Buffered activation for WorkItem: %1 due to Thermal Throttling policy.\r\n
0xb0000258 | AM: Failed to read activation plugin registry with error code %1.\r\n
0xb0000259 | AM: Failed to CoCreate activation plugin with error code %1 and CLSID %2.\r\n
0xb000025a | AM: Successfully created activation plugin with CLSID %1 from the registry.\r\n
0xb000025b | AM: Failed to register package if needed with error %1.\r\n
0xb000025c | AM: Failed trying to register package by family name async during activation with error %1.\r\n
0xb000025d | AM: Failed trying to wait for the completion of the register package by family async during activation with error %1.\r\n
0xb00002bc | BAM: Added Package: %1 UserSid: %2.\r\n
0xb00002bd | BAM: Removed Package: %1 UserSid: %2.\r\n
0xb00002be | BAM: Added Application: %1 UserSid: %2.\r\n
0xb00002bf | BAM: Removed Application: %1 UserSid: %2.\r\n
0xb00002c0 | BAM: AccessState Changed for Package: %1 OldState: %2 NewState: %3 UserSid: %4.\r\n
0xb00002c1 | BAM: BackgroundExecutionManager::RequestAccessAsync called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c2 | BAM: BackgroundExecutionManager::GetStatus called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c3 | BAM: BackgroundExecutionManager::RemoveAccess called for Application: %1.\r\n
0xb00002c4 | BAM: Sanitizing data for package: %1 HRESULT: %2.\r\n
0xb00002c5 | BAM: ReregisteredPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002c6 | BAM: UnregisterPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002c7 | BAM: BackgroundExecutionManager::RequestAccessKindAsync called for Application: %1 Requested_AccessKind: %2 Returned: %3.\r\n
0xb00002c8 | Background Access State For User Modified CallerUserSid = %1 CallerProcessName = %2 CallerPackageFamilyName = %3 \r\n            OldConsentValue = %4 NewConsentValue = %5 IsSetByHigherAuthority = %6 EffectiveConsentValue = %7 TargetUserSid = %8 HRESULT = %9\r\n
0xb00002c9 | Background Access State For Package Modified CallerUserSid = %1 CallerProcessName = %2 CallerPackageFamilyName = %3 \r\n            OldConsentValue = %4 NewConsentValue = %5 IsSetByHigherAuthority = %6 EffectiveConsentValue = %7 TargetUserSid = %8 \r\n            TargetPackageFamilyName = %9 HRESULT = %10\r\n
0xb00002ee | FAM: NotifyTaskInstanceCompleted, TaskID:%1, hr:%2\r\n
0xb00002ef | FAM: NotifyTaskInstanceRunning, TaskID:%1 Timer - %2\r\n
0xb00002f0 | FAM: RegisterForegroundAgentManagerProxy:PID=%1, ConsumerTaskId=%2, Option=%3, hr=%4\r\n
0xb00002f1 | FAM: UiForeground:Memory:%1MB, CPU:%2%%\r\n
0xb00002f2 | FAM: CreateAgentLaunchRequest, TaskID:%1, Queue:%2, hr:%3\r\n
0xb00002f3 | FAM: CancelAgentRequest, TaskID:%1, CancelType=%2, hr:%3\r\n
0xb00002f4 | FAM: AbortAgentRequestsInternal, hr:%1\r\n
0xb00002f5 | FAM: CompleteAgent, TaskID:%1, hr:%2\r\n
0xb00002f6 | FAM: PrioritizeAgentRequest, TaskID:%1, hr:%2\r\n
0xb00002f7 | FAM: OnForegroundAppChanged()-Abort agents\r\n
0xb00002f8 | FAM: OnRelease()\r\n
0xb00002f9 | FAM: NotifyConsumer, Notification:%1, TaskID:%2, hrResult:%3\r\n
0xb00002fa | FAM: AcquireSharedResourceSet, ProductID:%1, ConsumerPid:%2, Pending:%3, hr:%4\r\n
0xb00002fb | FAM: ReleaseResourceSet, #%1, hr:%2\r\n
0xb00002fc | FAM: TimerExpired:TerminateHost[PID=%1]\r\n
0xb00002fd | FAM: AcquireResourceSet, #%1, Mem:%2MB, CPU:%3%%, hr:%4\r\n
0xb00002fe | FAM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000321 | OTM: Read settings. First retry timeout = %1 ms, Second retry timeout = %2 ms, Third retry timeout = %3 ms, Maximum Retry Timeout = %4 ms\r\n
0xb0000322 | OTM: Task instance %2 of product %1 completed\r\n
0xb0000323 | OTM: TaskHost of product %1 has crashed\r\n
0xb0000324 | OTM: TaskHost of product %1 has been completed by PacMan\r\n
0xb0000325 | OTM: Launching OEM boot agents\r\n
0xb0000326 | OTM: Launching boot agents for product %1 failed with error %2\r\n
0xb0000327 | OTM: Launch boot agents for product %1\r\n
0xb0000328 | OTM: Running OnUpdateStarted for product %1\r\n
0xb0000329 | OTM: Restarting boot agents for product %1 after update\r\n
0xb000032a | OTM: Start menu is ready.\r\n
0xb000032b | OTM: Could not launch OEM boot agents. QueueUserWorkItem failed with error %1.\r\n
0xb000032c | OTM: Could not process update notification for OEM application. QueueUserWorkItem failed with error %1.\r\n
0xb000032d | OTM: Could not process update notification for OEM application. ProcessUpdateNotification failed with error %1.\r\n
0xb000032e | OTM: OemTaskManager::NotifyTaskInstanceCompleted failed with error %1.\r\n
0xb000032f | OTM: OemTaskManager::NotifyTaskHostCompleted failed with error %1.\r\n
0xb0000330 | OTM: OemApp::DumpAgents failed with error %1.\r\n
0xb0000331 | OTM: An error occurred. Hr = %1\r\n
0xb0000332 | OTM: No apps with ServiceAgents were found.\r\n
0xb0000333 | OTM: No ServiceAgent task found for product %1.\r\n
0xb0000334 | OTM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb000035d | PLM: Start tracking new app user %1 app %2, contract %3, hr = %4\r\n
0xb000035e | PLM: Application launched %1 in app %2, hr = %3\r\n
0xb000035f | PLM: Application resume %1 in app %2, hr = %3\r\n
0xb0000360 | PLM: Suspend-Terminate(%3) task %1 in app %2\r\n
0xb0000361 | PLM: Suspend-Terminate suspend of task %1 in app %2 exemption %3\r\n
0xb0000362 | PLM: Suspend-Terminate auto terminate(%3) task %1 in app %2\r\n
0xb0000363 | PLM: Suspend-Terminate task %1 in app %2, hr %3\r\n
0xb0000364 | PLM: Halt app %1, hr %2\r\n
0xb0000365 | PLM: Task resume %1 in app %2\r\n
0xb0000366 | PLM: Task cancel %1 in app %2\r\n
0xb0000367 | PLM: Task remove %1 in app %2\r\n
0xb0000368 | PLM: Queue Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000369 | PLM: Queue Activation State Change Notification %1 state %2\r\n
0xb000036a | PLM: Before Activate task %1 for user %2 in app %3, contract %4, hostid %5, hr = %6\r\n
0xb000036b | PLM: After Activate task %1 with result %2, hr = %3\r\n
0xb000036c | PLM: ApplicationLayer=%1 Set Foreground new task %2, prev task %3\r\n
0xb000036d | PLM: Add task %1 to user %2 and app %3, hr = %4\r\n
0xb000036e | PLM: Create app for user %1, %2, new [app(%3) pkg(%4)], hr = %5\r\n
0xb000036f | PLM: Add task %1 to user %2 and app %3, new [app(%4) pkg(%5)], hr = %6\r\n
0xb0000370 | PLM: Remove task %1, was found(%2)\r\n
0xb0000371 | PLM: Remove app if empty from user %1, %2, hr = %3\r\n
0xb0000372 | PLM: Remove pkg if empty from user %1, %2, hr = %3\r\n
0xb0000373 | PLM: Send Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000374 | PLM: Send Activation State Change Notification %1 state %2\r\n
0xb0000376 | PLM: Timer Started duration %1ms, hr %2\r\n
0xb0000377 | PLM: Timer Expired duration %1ms, hr %2\r\n
0xb0000378 | PLM: Abort task %1 reason %2, dump(%3)\r\n
0xb0000379 | PLM: Task rehydrate %1 in app %2 contract %3\r\n
0xb000037a | PLM: Start RPC suspension timer PSMKey=%1 WakeCounters=%2, hr = %3\r\n
0xb000037b | PLM: Cancel RPC suspension timer PSMKey=%1 app state=%2\r\n
0xb000037c | PLM: Terminate application PSMKey=%1 due to expired RPC suspension timeout\r\n
0xb000037d | PLM: Application %1 cannot be terminated due to %2 exemption\r\n
0xb000037e | PLM: Application %1 can be terminated\r\n
0xb000037f | PLM: EvaluateAndTerminateApplication %1 cannot be terminated due to %2\r\n
0xb0000380 | PLM: EvaluateAndTerminateApplication %1, terminate hr = %2\r\n
0xb0000381 | PLM: Terminate debounce app %1 current state %2 ultimate state %3\r\n
0xb0000382 | PLM: Terminate debounce app %1, hr = %2\r\n
0xb0000383 | PLM: Terminate reason was cleared\r\n
0xb0000384 | PLM: Abort app user %1 app %2 reason %3, dump(%4)\r\n
0xb0000385 | PLM: Watson dump NOT generated for user %1 app %2, process count %3\r\n
0xb0000386 | PLM: Watson dump start for user %1 app %2 reason %3 description %4, process %5 (%6)\r\n
0xb0000387 | PLM: Watson dump information for user %1 app %2 product Id %3 title %4 version %5\r\n
0xb0000388 | PLM: Watson dump end for user %1 app %2, hr %3\r\n
0xb0000389 | PLM: Add Watson dump to user %1 app %2 process %3, hr %4\r\n
0xb000038a | PLM: Failed to add Watson process info for process %1 user %2 app %3\r\n
0xb000038b | PLM: Watson dump status changed pids(%1)\r\n
0xb000038c | PLM: Watson dump status changed, add process %1 user %2 app %3\r\n
0xb000038d | PLM: Watson dump status changed, remove process %1 user %2 app %3\r\n
0xb000038e | PLM: Watson dump status changed, unknown process %1 app %2\r\n
0xb000038f | PLM: Watson add/remove(%2) error report task completion to process %1 (signaled %4), hr %3\r\n
0xb0000390 | PLM: Watson in progress for PSMKey %1, waiting...\r\n
0xb0000391 | PLM: Watson in progress finished for PSMKey %1\r\n
0xb0000392 | PLM: Extending RPC suspension timer PSMKey=%1\r\n
0xb0000393 | PLM: Acquire network reference failed CM_RESULT=%1\r\n
0xb0000394 | PLM: Release network reference failed CM_RESULT=%1\r\n
0xb0000395 | PLM: Suspend-Terminate(%2) app %1 exemption %3, hr %4\r\n
0xb0000396 | PLM: Suspend-Terminate task %1 while dehydrating\r\n
0xb0000397 | PLM: Add user %1 sid %2 to data store, hr = %3\r\n
0xb0000398 | PLM: Start launch grace for user %1 app %2, hr = %3\r\n
0xb0000399 | PLM: Set Window Id for user %1 app %2 wnd %3\r\n
0xb000039a | PLM: EvaluateLaunchGraceCompleted for user %1 app %2\r\n
0xb000039b | PLM: Terminating reexisting app due to sihost restart with PSMKey %1, status %2\r\n
0xb000039c | PLM: Terminating preexisting applications on sihost startup\r\n
0xb000039d | PLM: Set Pause On Lock for user %1 app %2 value %3\r\n
0xb000041b | AAM: Initiate activation for user %1 app %2 contract %3 task %4, hr %5\r\n
0xb000041c | AAM: Initiate activation completed for task %2 (expected %1), hr %3\r\n
0xb000041d | AAM: Initialize activation for user %1 app %2 contract %3 lightup(%5), hr %4\r\n
0xb000041e | AAM: Validate activation, hr %1\r\n
0xb000041f | AAM: Verify license for pkg %1, hr %2\r\n
0xb0000420 | AAM: Activate activation task %1 host %2, hr %3\r\n
0xb0000421 | AAM: Activation shim timer expired %1, hr %2\r\n
0xb0000422 | AAM: Initiate Core UI, hr %1\r\n
0xb0000423 | AAM: Release Core UI\r\n
0xb0000424 | AAM: Create Windows AAM, hr %1\r\n
0xb0000425 | AAM: Attempted remediation, hr %1\r\n
0xb0000426 | AAM: Failed while trying to find a remediation handler, hr %1\r\n
0xb0000427 | AAM: Failed while trying to find the package status, hr %1\r\n
0xb0000428 | AAM: Failed while trying to find the package origin, hr %1\r\n
0xb0000429 | AAM: Failed while trying to verify and initialize the activation, hr %1\r\n
0xb000042a | AAM: Failed while trying to check roaming data, hr %1\r\n
0xb000042f | AAM: Broker created plugins %1, expected %2\r\n
0xb0000430 | AAM: Broker initialize, hr %1\r\n
0xb0000431 | AAM: Broker start activate application %1 (%3 args) arg[0] %2 type %4 caller PID %5 (initialization count %6)\r\n
0xb0000432 | AAM: Broker end activate application %1 launched PID %2 task %3, hr %4\r\n
0xb0000433 | AAM: Broker activate task with result for app %1 caller PID %2 caller task %3\r\n
0xb0000434 | AAM: Broker get result for PID %1 task %2 result %3, hr %4\r\n
0xb0000435 | AAM: Broker get task id for process %1 window %2 = task %3, hr %4\r\n
0xb0000436 | AAM: Broker init session manager, hr %1\r\n
0xb0000437 | AAM: Broker release session manager\r\n
0xb0000438 | AAM: Broker add task with result for parent %1, hr %2\r\n
0xb0000439 | AAM: Broker get task with result for parent %1, hr %2\r\n
0xb000043a | AAM: Broker remove task with result for parent %1, hr %2\r\n
0xb000043b | AAM: Broker create completed event for caller PID %1, hr %2\r\n
0xb000043c | AAM: Broker get task with result for child %1, hr %2\r\n
0xb000043d | AAM: Broker parent task completed %1 with child state %2\r\n
0xb000043e | AAM: Broker child task completed %1 with state %2, hr %3\r\n
0xb000043f | AAM: Broker task event signaled for parent %1 child %2 previous state %3, hr %4\r\n
0xb0000440 | AAM: Broker close task %1, hr %2\r\n
0xb0000441 | AAM: Broker activate application %1 arg[%3] %2\r\n
0xb000044c | FM-ARP: ApplyResourceSetType ResourceSetType=%1 User=%2 PSMKey=%3 ResourceSet=%4 HRESULT=%5\r\n
0xb000044d | FM-ARP: ApplyTerminal UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044e | FM-ARP: RemoveInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044f | FM-ARP: ResetInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000450 | FM-ARP: OnRelease UserContext=%1 PsmKey=%2 ReleaseAction=%3 ReleasedCachedResource=%4 ReleaseAppliedResource=%5 HRESULT=%6\r\n
0xb0000451 | FM-ARP: OnAcquired UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000452 | FM-ARP: OnOutOfMemory UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000453 | FM-ARP: ApplyResourceBoost User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000454 | FM-ARP: AcquireResourceSet ResourceSetType=%1 Usercontext=%2 PsmKey=%3 HRESULT=%4\r\n
0xb0000455 | FM-ARP: Apply Cached Resource Set Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000456 | FM-ARP: Clear Cached Resource User=%1 PSMKey=%2\r\n
0xb0000457 | FM-ARP: Fire Cached ResourceCallback User=%1 PSMKey=%2\r\n
0xb00004b0 | FM-CAM: OnApplicationStateChangedEx UserContext=%1 PsmKey=%2 state=%3 HRESULT=%4\r\n
0xb00004b1 | FM-CAM: AcquireForegroundResource UserContext=%1 PsmKey=%2 isPending=%3\r\n
0xb00004b2 | FM-CAM: OnResourceAcquired UserContext=%1 PsmKey=%2\r\n
0xb00004b3 | FM-CAM: OnResourceTimerExpired UserContext=%1 PsmKey=%2\r\n
0xb00004e2 | FM: TaskCompletion New Battery Saver State %1\r\n
0xb00004e3 | FM: TaskCompletion Revoke Exemption PID=%1 AUMID=%2 TC=%3\r\n
0xb00004e4 | FM: TaskCompletion Apply(%3) Exemption PID=%1 TC=%2 HRESULT=%4\r\n
0xb00004e5 | FM-EEP: CheckProcessBackgroundEligibility ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e6 | FM-EEP: ApplyTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e7 | FM-EEP: RevokeTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e8 | FM-EEP: RequestExtendedExecution ProcessId=%1 Reason=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004e9 | FM-EEP: RegisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004ea | FM-EEP: CompleteExtendedExecution ProcessId=%1 fIsResumed=%2 HRESULT=%3\r\n
0xb00004eb | FM-EEP: RevokeSuspensionExtension User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00004ec | FM-ARP: NotifyPendingResourceSetTransition ResourceSetType=%1 ResourceSet=%2 HRESULT=%3\r\n
0xb00004ed | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 fTimerExpiredCallback=%2 HRESULT=%3\r\n
0xb00004ee | FM-EEP: IsApplicationStateBackgroundEligibile User=%1 PsmKey=%2 fResult=%3\r\n
0xb00004ef | FM-EEP: RevokeTaskCompletionExemption AppUserModelId=%1 HRESULT=%2\r\n
0xb00004f0 | FM-EEP: AllowBackgroundExecution User=%1 AppUserModelId=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004f1 | FM-EEP: OnPackageEnergyStateChange PackageFullName=%1 PackageState=%2 HRESULT=%3\r\n
0xb00004f2 | FM-EEP: RegisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f3 | FM-EEP: UnregisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f4 | FM-EEP: UnregisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004f5 | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 TC=%2 isResourcePending =%3 HRESULT=%4\r\n
0xb00004f6 | FM-EEP: Task Completion Denied By EDP Policy ProcessId=%1 TC=%2\r\n
0xb00004f7 | FM-EEP: IsForegroundApplication Application=%1 Result=%2\r\n
0xb0000578 | FM: Registering callback %1 HRESULT=%2\r\n
0xb0000579 | FM: Generate ActivationInstanceID Id=%1\r\n
0xb000057a | FM: +ActivationPrerequisitePhase ActivationInstanceId=%1 UserContext=%2 AUMID=%3 ContractId=%4\r\n
0xb000057b | FM: -ActivationPrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb000057c | FM: +Resume_RehydrationPhase ActivationInstanceId=%1\r\n
0xb000057d | FM: -Resume_RehydrationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000057e | FM: +ResumeActivation ActivationInstanceId=%1 fIsResumed=%2\r\n
0xb000057f | FM: -ResumeActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000580 | FM: +Resume_ActivationPhase ActivationInstanceId=%1\r\n
0xb0000581 | FM: -Resume_ActivationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000582 | FM: +PauseActivation ActivationInstanceId=%1\r\n
0xb0000583 | FM: -PauseActivation HRESULT=%1 PausePending=%2\r\n
0xb0000584 | FM: +CancelActivation ActivationInstanceId=%1\r\n
0xb0000585 | FM: -CancelActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000586 | FM: +AbortActivation ActivationInstanceId=%1 Reason=%2 fGenerateWER=%3\r\n
0xb0000587 | FM: -AbortActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000588 | FM: +GetActivationProcessId ActivationInstanceId=%1\r\n
0xb0000589 | FM: -GetActivationProcessId ActivationInstanceId=%1 PID%2 HRESULT=%3\r\n
0xb000058a | FM: +SetForegroundActivationInstance ActivationInstanceId=%1 Isforeground=%2\r\n
0xb000058b | FM: -SetForegroundActivationInstance ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000058c | FM: SetActivationDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb000058d | FM: OnActivationStateChanged ActivationInstanceId=%1 state=%2 HRESULT=%3\r\n
0xb000058e | FM: OnApplicationStateChanged UserContext=%1 PSMKey=%2 state=%3 HRESULT=%4\r\n
0xb000058f | FM: IsValidActivationProcessId ActivationInstanceID=%1 PID=%2 fValid=%3 HRESULT=%4\r\n
0xb0000590 | FM: GetForegroundProductId fIgnoreLockScreen=%1 ProductID=%2 HRESULT=%3\r\n
0xb0000591 | FM: GetProductIdFromProcessID ProductID=%1 PID=%2 HRESULT=%3\r\n
0xb0000592 | FM: Discarding Application Frozen notification because the application isn't really frozen\r\n
0xb0000593 | FM: Dehydrate Application AUMID=%1 HRESULT=%2\r\n
0xb0000594 | FM: +ResumePrerequisitePhase ActivationInstanceId=%1\r\n
0xb0000595 | FM: -ResumePrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb0000596 | FM: GenerateWatsonReport PID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000597 | FM: SetContinuation ActivationInstanceID=%1\r\n
0xb0000598 | FM: AbandonContinuation ActivationInstanceID=%1\r\n
0xb0000599 | FM: PerformContinuation ActivationInstanceID=%1\r\n
0xb000059a | FM: Shutdown HRESULT=%1\r\n
0xb000059b | FM: +PauseActivation ActivationInstanceId=%1 AUMID=%2 PackageFullName=%3\r\n
0xb000059c | FM: +ActivationBypass ActivationInstanceId=%1\r\n
0xb000059d | FM: -ActivationBypass ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000059e | FM: +PostPausePendingResume ActivationInstanceId=%1\r\n
0xb000059f | FM: -PostPausePendingResume ActivationInstanceId=%1 HRESULT=%2\r\n
0xb00005a0 | FM: SetActivationImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb00005a1 | FM: NotifyWindowAdded TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a2 | FM: NotifyWindowRemoved TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a3 | FTM: Logoff User=%1 HRESULT=%2\r\n
0xb00005a4 | FM: ActivationTimeoutPolicyChanged  TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a5 | FM-EEP: OnConnectedStandbyStateChanged  State=%1\r\n
0xb00005a6 | FM: SendActivationNotification ActivationId=%1 NotificationId=%2\r\n
0xb00005a7 | FM: OnResourceAcquired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a8 | FM: OnResourceTimerExpired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a9 | FM: PostPausePendingActivation ActivationId=%1 HRESULT=%2\r\n
0xb00007d0 | VoIPPolicy: Evaluate Activation Action for PsmKey = %2, WorkItemId = %1, Action = %3, HRESULT = %4\r\n
0xb00007d1 | VoIPPolicy: Task Activated for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d2 | VoIPPolicy: Task Completed for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d3 | VoIPPolicy: Task Canceled for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d4 | VoIPPolicy: Task Aborted for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d5 | VoIPPolicy: Determine and Apply Resources PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d6 | VOIP: NotifyVoipActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d7 | VOIP: LaunchVoipRtcTask called for PID:%1 PSMKey:{%2} with TaskEntryPoint:{%3} and WNFStateName:{%4} HRESULT:%5.\r\n
0xb00007d8 | VOIP: NotifyVoipActivityCompleted called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d9 | VOIP: HoldActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007da | VOIP: UnholdActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007db | VOIP: NotifyIncomingCallDialogDisplayed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dc | VOIP: NotifyIncomingCallDialogDismissed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dd | VOIP: CallActive called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007de | VOIP: AppLaunchVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007df | VOIP: OnVoipActivityCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e0 | VOIP: AppHoldActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e1 | VOIP: AppUnholdActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e2 | VOIP: OnIncomingCallDialogDisplayed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e3 | VOIP: OnIncomingCallDialogDismissed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e4 | VOIP: AppDetermineAndApplyBestResourceSet called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e5 | VOIP: PolicyEvaluateAction called for WorkItemId:{%1} PSMKey:{%2} ActivationAction:%3 HRESULT:%4.\r\n
0xb00007e6 | VOIP: PolicyTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e7 | VOIP: PolicyTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e8 | VOIP: PolicyTaskCanceled called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e9 | VOIP: PolicyTaskAborted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007ea | VOIP: OnForegroundApplicationChanged called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007eb | VOIP: AppOnTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ec | VOIP: AppOnTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ed | VOIP: AppCancelVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ee | VOIP: CancelVoipRtcTask called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb0000c81 | Task: %1 has started\r\n
0xb0000c82 | Task: %1 has paused\r\n
0xb0000c83 | Task: %1 has resumed\r\n
0xb0000c84 | Task: %1 has completed\r\n
0xb0000c85 | EM: +GetTaskInfo()\r\n
0xb0000c86 | EM: -GetTaskInfo(). HRESULT = %1\r\n
0xb0000c87 | EM: GetAppInfo:%1,%2:%3\r\n
0xb0000c88 | EM: ParseBackgroundAbilities - HRESULT=%1\r\n
0xb0000c89 | EM: +ExecManServerHost::CreateProcess\r\n
0xb0000c8a | EM: -ExecManServerHost::CreateProcess. HRESULT=%1\r\n
0xb0000c8b | Sqm::AppPlatSqmAppDataUsage: %1/%2 - TaskID = %3, Type = %4, NewState = %5, ReasonForStateChange = %6, Duration (ms) = %7, PeakMemory (kb) = %8\r\n
0xb0000c8f | Emc::ExecuteCommand: StartTaskCallbackBegin: TaskID = %1\r\n
0xb0000c90 | Emc::ExecuteCommand: StartTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c91 | Emc::ExecuteCommand: PauseTaskCallbackBegin: TaskID = %1\r\n
0xb0000c92 | Emc::ExecuteCommand: PauseTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c93 | Emc::ExecuteCommand: ResumeTaskCallbackBegin: TaskID = %1\r\n
0xb0000c94 | Emc::ExecuteCommand: ResumeTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c95 | Emc::ExecuteCommand: ControlTaskCallbackBegin: TaskID = %1\r\n
0xb0000c96 | Emc::ExecuteCommand: ControlTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c97 | Emc::ExecuteCommand: CancelTaskCallbackBegin: TaskID = %1\r\n
0xb0000c98 | Emc::ExecuteCommand: CancelTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c99 | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackBegin: TaskID = %1\r\n
0xb0000c9a | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c9e | Emc::RegisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, HR = %3\r\n
0xb0000ca8 | Emc::DeregisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, Reason = %3, HR = %4\r\n
0xb0000ca9 | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleBegin: ProductID = %1\r\n
0xb0000caa | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleEnd: ProductID = %1\r\n
0xb0000cab | EM: Skipping terminate process call for %1\r\n
0xb0000cac | EM: Terminating process: PID = %1, ExitCode = %2\r\n
0xb0000ce4 | AimServer::OnAgentRequestInvoked: AgentRequestID %1 was invoked. PID = %2, HR = %3\r\n
0xb0000ce5 | AimServer::ReadSettings: HR = %1\r\n
0xb0000ce6 | AimServer: Detected server for scope %1 terminated (PID = %2)\r\n
0xb0000ce8 | AimServer::HandleEvent: ProductID %1 received PM LifecyleEvent %2. HR Notification = %3, HR = %4\r\n
0xb0000ce9 | BA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cea | BA::RegisterServiceRequest: AlreadyReserved = %1, SR = %2, HR = %3\r\n
0xb0000ceb | BA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cec | BA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000ced | BA::NotifyTaskInstanceCompleted: Terminating Orphaned Host PID = %1\r\n
0xb0000cee | BA::OrphanAgentRequest: AgentRequestID = %1, HR = %2\r\n
0xb0000cef | BA::UnRegisterServiceRequest: Terminating host PID %1\r\n
0xb0000cf0 | BA::UnRegisterServiceRequest: Orphaning host PID %1\r\n
0xb0000cf1 | BA::UnRegisterServiceRequest: Terminating second old orphaned host PID %1\r\n
0xb0000cf2 | BTM::RecvCallback: Timer expired for AgentRequestID %1\r\n
0xb0000cf3 | BTM::LaunchTask: TaskURI = %1 TaskID = %2, PID = %3, HR = %4\r\n
0xb0000cf4 | GBA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cf5 | GBA::RegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf6 | GBA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf7 | GBA::RegisterAgentRequest: AgentRequestID = %1, type = %2, hr = %3\r\n
0xb0000cf8 | GBA: Cancelling low priority %3 agent because high priority %2 needs to run: Resource was dedicated = %1\r\n
0xb0000cf9 | GBA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000cfa | GBA::TryAcquireResourceSet: pending = %1, type = %2, HR = %3\r\n
0xb0000cfb | GBA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfc | BA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfd | BA::NotifyTaskHostCompleted: ProductID = %1, PID = %2\r\n
0xb0000cfe | BA::RegisterAgentRequest: ProductID = %1, AgentRequestID = %2, HR = %3\r\n
0xb0000cff | BA::PdcActivationFailed: ProductID = %1, Reason = %2, NTSTATUS = %3\r\n
0xb0000dac | FTM: AllowBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dad | FTM: Process is using too much memory for BG Execution. PID=%1, MemUsage=%2, RequiredMemUsage=%3\r\n
0xb0000dae | FTM: Removing BG capability from Task ID %1 due to OOM\r\n
0xb0000daf | FTM: Battery Saver State has change. New state = %1\r\n
0xb0000db0 | FTM: Attempted new BG Execution request due to battery state change. TaskID=%1\r\n
0xb0000db1 | FTM: NotifyTaskInstanceCompleted TaskID=%1 HRESULT=%2\r\n
0xb0000db2 | FTM: NotifyTaskInstancePaused TaskID=%1 HRESULT=%2\r\n
0xb0000db3 | FTM: NotifyTaskInstanceRunning TaskID=%1 HRESULT=%2\r\n
0xb0000db4 | FTM: SendTaskStatusChange TaskID=%1 Status=%2 HRESULT=%3\r\n
0xb0000db5 | FTM: NotifyTaskHostCompleted HRESULT=%1\r\n
0xb0000db6 | FTM: Discarding NotifyTaskHostFrozen notification because the host isn't really frozen\r\n
0xb0000db7 | FTM: NotifyTaskHostFrozen PID=%1 HRESULT=%2\r\n
0xb0000db8 | FTM: NotifyTaskHostDehydrated HRESULT=%1\r\n
0xb0000db9 | FTM: Registering callback %1 HRESULT=%2\r\n
0xb0000dba | FTM: New Task %1 is dehydration-suppressing\r\n
0xb0000dbb | FTM: Applying Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbc | FTM: Revoking Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbd | FTM: +LaunchTask TaskURI=%1 LaunchFlags=%2\r\n
0xb0000dbe | FTM: -LaunchTask TaskURI=%1 TaskID=%2 PID=%3 HRESULT=%4\r\n
0xb0000dbf | FTM: ResumeTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc0 | FTM: Removing Foreground Resources from TaskID=%1\r\n
0xb0000dc1 | FTM: SetForegroundTaskInstanceId TaskID=%1 HRESULT=%2\r\n
0xb0000dc2 | FTM: PauseTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc3 | FTM: CancelTask TaskID=%1 Frozen=%2 HRESULT=%3\r\n
0xb0000dc4 | FTM: AbortTask being ignored because the task is completed TaskID=%1\r\n
0xb0000dc5 | FTM: AbortTask TaskID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000dc6 | FTM: SetTaskDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb0000dc7 | FTM: RequestProcessBackgroundExecution type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc8 | FTM: CancelProcessBackgroundExecutionRequest type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc9 | FTM: TaskRunningInBackground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dca | FTM: TaskRunningInForeground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dcb | FTM: Changing activation policy to resume due to BG Execution for ProductID %1\r\n
0xb0000dcc | FTM: OnShutdownCompleted\r\n
0xb0000dcd | FTM: Ignoring expired watchdog for task %1 because it is being debugged.\r\n
0xb0000dce | FTM: Watchdog fired for task %1 while running in background. Pausing Task.\r\n
0xb0000dcf | FTM: Request BG Execution Denied because it wasn't running. TaskID=%1\r\n
0xb0000dd0 | FTM: Request BG Execution Denied because product was forbidden. TaskID=%1\r\n
0xb0000dd1 | FTM: Request BG Execution Denied because task didn't have BG abilities in its manifest. TaskID=%1\r\n
0xb0000dd2 | FTM: Request BG Execution Denied due to lack of resources. TaskID=%1\r\n
0xb0000dd3 | FTM: Request BG Execution Denied because battery policy prevented it. TaskID=%1\r\n
0xb0000dd4 | FTM: RequestBGAccess IsAllowed=%1 TaskID=%2 HRESULT=%3\r\n
0xb0000dd5 | FTM: RemoveBGRequest RequestedRemoval=%1 ActualRemoval=%2 TaskID=%3 HRESULT=%4\r\n
0xb0000dd6 | FTM: ForbidBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dd7 | FTM: IsValidTaskInstancePid TaskID=%1 Pid=%2 fValid=%3 HRESULT=%4\r\n
0xb0000dd8 | FTM: DetermineBestResourceSet for child ProductID=%1 LaunchFlags=%2 ResourceSetType=%3\r\n
0xb0000dd9 | FTM: OnRelease ResourceSet TaskID=%1 ResouceSet=%2 HRESULT=%3\r\n
0xb0000dda | FTM:UITask Call to Acquire network reference failed CM_RESULT=%1\r\n
0xb0000ddb | FTM:UITask Call to Release network reference failed CM_RESULT=%1\r\n
0xb0000ddc | FTM: SetTaskImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb0000ddd | FTM: +RequestProcessBackgroundExecution type=%1 Pid=%2\r\n
0xb0000dde | FTM: +RequestBackgroundExecution type=%1\r\n
0xb0000ddf | FTM: -RequestBackgroundExecution type=%1 HRESULT=%2\r\n
0xb0000de0 | FTM: +RequestBGAccess TaskInstanceId=%1 type=%2\r\n
0xb0000de1 | FTM: Request BG Execution Denied because DPL policy prevented it. TaskID=%1\r\n
0xb0000de2 | FTM: Windows Information Protection keys locked state (%1)\r\n
0xb0000e42 | VoIP: Foreground state for product %1 has changed. Is in foreground = %2\r\n
0xb0000e43 | VoIP: Canceling communication agent for product %1\r\n
0xb0000e44 | VoIP: Timer expired for keep-alive agent of product %1\r\n
0xb0000e45 | VoIP: Timer expired for incoming call agent of product %1\r\n
0xb0000e46 | VoIP: Launched agent instance with id %2 and URI %1\r\n
0xb0000e47 | VoIP: Canceled agent instance with id %1\r\n
0xb0000e48 | VoIP: Set active call resource set\r\n
0xb0000e49 | VoIP: Set communication agent resource set\r\n
0xb0000e4a | VoIP: Set VoIP Worker resource set\r\n
0xb0000e4b | VoIP: Applied terminal resource set\r\n
0xb0000e4c | VoIP: Last task instance completed. Releasing the task host ...\r\n
0xb0000e4d | VoIP: Launching active call agent instance for product %1\r\n
0xb0000e4e | VoIP: Canceling active call agent for product %1\r\n
0xb0000e4f | VoIP: Putting an active call on hold for product %1\r\n
0xb0000e50 | VoIP: Taking an active call off hold for product %1\r\n
0xb0000e51 | VoIP: Incoming call dialog has been displayed for product %1\r\n
0xb0000e52 | VoIP: Incoming call dialog has been dismissed for product %1\r\n
0xb0000e53 | VoIP: Launch communication agent request received from process %1 for product %2\r\n
0xb0000e54 | VoIP: Read settings. Keep alive timout = %1 ms, Max agent request queue = %2, Incoming call grace period = %3 ms, Incoming call dismissed grace period = %4 ms\r\n
0xb0000e55 | VoIP: Received request to launch agent type %2 for product %1\r\n
0xb0000e56 | VoIP: Task instance %2 of product %1 completed\r\n
0xb0000e57 | VoIP: Processing request to launch agent type %2 for product %1\r\n
0xb0000e58 | VoIP: Added VoIPApp object to map for product %1\r\n
0xb0000e59 | VoIP: Removed VoIPApp object from map for product %1\r\n
0xb0000e5a | VoIP: Getting VoIPApp object from map for product %1\r\n
0xb0000e5b | VoIP: Publishing WNF_DEVP_VOIP_ACTIVE_CALL_STATE_CHANGE failed with status %1\r\n
0xb0000e5c | VoIP: Subscribing to the WNF_WIFI_CONNECTION_STATUS event failed with status %1\r\n
0xb0000e5d | VoIP: Subscribed to WNF_WIFI_CONNECTION_STATUS? %1\r\n
0xb0000e5e | VoIP: WiFi connection status active/dormat? %1 (hConnection = %2)\r\n
0xb0000e5f | VoIP: RtlQueryWnfStateData failed trying to query the value of WNF_WIFI_CONNECTION_STATUS. NTSTATUS = %1\r\n
0xb0000e60 | VoIP: Could not spin up worker for UpdateWiFiStateHelper. HR =%1\r\n
0xb0000e61 | VoIP: In active call? %1\r\n
0xb0000e62 | VoIP: CmUtilSetWiFiActive was not successful. This could be because WiFi disconnected by the time we were notified of the connection.\r\n
0xb0000e63 | VoIP: WiFi connection status is %1.\r\n
0xb0000e64 | VoIP: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000e65 | VoIP: PhoneServiceRestart: HR = %1\r\n
0xb0000e66 | VoIP: PhoneServiceRestart: Product = %1, HR = %2\r\n
0xb0000e67 | VoIP: Launching call query info agent instance for product %1\r\n
0xb0000e68 | VoIP: Canceling call query info agent instance for product %1\r\n
0xb0000e69 | VoIP: Terminating agents due to low memory for product %1\r\n
0xb0000e6a | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2\r\n
0xb0000e6b | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2, fApplied = %3, HR = %4\r\n
0xb0000e6c | VoIP: Set PDC Network Active for product = %1, NTSTATUS = %2\r\n
0xb0000e6d | VoIP: Set PDC Network Inactive for product = %1, NTSTATUS = %2\r\n
0xb0000e6e | VoIP: Renew PDC Network activation failed for product = %1, NTSTATUS = %2\r\n
0xb0000e73 | VoIP: An error occurred. Hr = %1\r\n
0xb00017d4 | %1 - [%2 = %3]\n\r\n
0xb00017d5 | %1 - Parsing config file [%2] file size = %3.  Parse = %4\r\n
0xb00017d6 | %1 - OnTaskModelMessage: Dispatching EM message\r\n
0xb00017d7 | %1 - InitializeTaskHost URI=%2, Page=%3, TaskId=%4\r\n
0xb00017d8 | %1 - Resuming Task from dehydration\r\n
0xb00017d9 | %1 - TaskHandler::GetTaskHandler hr=%2\r\n
0xb00017da | %1 - TaskHost Init\r\n
0xb00017db | %1 - TaskHost Init hr = %2\r\n
0xb00017dc | %1 - Host Dispatcher Exiting hr = %2\r\n
0xb00017dd | %1 - TaskHandlerReady received\r\n
0xb00017de | %1 - StartTask TaskId=%2\r\n
0xb00017df | %1 - PauseTask TaskId=%2\r\n
0xb00017e0 | %1 - ResumeTask TaskId=%2\r\n
0xb00017e1 | %1 - OnTaskHandlerVisible received\r\n
0xb00017e2 | %1 - OnTaskHandlerHidden received\r\n
0xb00017e3 | %1 - BackgroundExecutionCallback TaskId[%2] Command[%3]\r\n
0xb00017e4 | %1 - BackgroundExecutionCallback hr=%2\r\n
0xb00017e5 | %1 - OnHostRunning\r\n
0xb00017e6 | %1 - OnHostRunning. hr = %2\r\n
0xb00017e7 | %1 - Dehydrating. dehydrateGracefully = %2\r\n
0xb00017e8 | %1 - Gracefully dehydrating TaskHost\r\n
0xb00017e9 | %1 - TryDehydrateHost. hr = %2\r\n
0xb00017ea | %1 - DehydrateHost event triggered\r\n
0xb00017eb | %1 - WaitForUnfreeze hr = %2\r\n
0xb00017ec | %1 - ReduceMemoryHostCallback hr = %2\r\n
0xb00017ed | %1 - Graceful tear-down failed\r\n
0xb00017ee | %1 - BeforeHostRunningInBackgroundCallback\r\n
0xb00017ef | %1 - BeforeHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f0 | %1 - AfterHostRunningInBackgroundCallback\r\n
0xb00017f1 | %1 - AfterHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f2 | %1 - Unhandled exception occurred. hr = %2\r\n
0xb00017f3 | %1 - State-Transition (%2)->(%3)\r\n
0xb00017f4 | %1 - EnableProfiling = [%2]\r\n
0xb00017f5 | %1 - Profile Dll = [%2]\r\n
0xb00017f6 | %1 - ProfilerCLSID = [%2]\r\n
0xb00017f7 | %1 - TaskHostHelper::SetProfilerSettings hr = %2\r\n
0xb00017f8 | %1 - File path = %2 : %3\r\n
0xb00017f9 | %1 - Parse Element: %2.\r\n
0xb00017fa | %1 - Parse Element Value = %2 with pwszLocalName = %3.\r\n
0xb00017fb | %1 - Parse HResult = %2\r\n
0xb00017fc | %1 - YUTHost: failed to GAC trusted assembly %2\r\n\r\n
0xb00017fd | %1 - UITaskHandler::Initialize. hr = %2\r\n
0xb00017fe | %1 - UITaskHandler::Disconnect done\r\n
0xb00017ff | %1 - UITaskHandler::GoBackground. hr = %2\r\n
0xb0001800 | %1 - UITaskHandler::GoForeground. hr = %2\r\n
0xb0001801 | %1 - Managed Framework Ready. Handling Pending Event:[%2]\r\n
0xb0001802 | %1 - HandlePendingEvents Start TaskId=%2\r\n
0xb0001803 | %1 - HandlePendingEvents Pause TaskId=%2\r\n
0xb0001804 | %1 - HandlePendingEvents Resume TaskId=%2\r\n
0xb0001805 | %1 - Waiting for Siblings...\r\n
0xb0001806 | %1 - Waiting for Siblings done. hr = %2\r\n
0xb0001807 | %1 - UITaskHandler::OnRuntimeHostReady TaskID:[%2]\r\n
0xb0001808 | %1 - UITaskHandler::OnRuntimeHostReady. Processed pending SystemKeyPress [%2]\r\n
0xb0001809 | %1 - UITaskHandler::OnRuntimeHostReady hr = %2\r\n
0xb000180a | %1 - UITaskHandler::RegistrationComplete hr = %2\r\n
0xb000180b | %1 - UITaskHandler::ConnectionComplete received\r\n
0xb000180c | %1 - UITaskHandler::ConnectionComplete hr = %2\r\n
0xb000180d | %1 - UITaskHandler::ProcessActivationData received, reason=%2\r\n
0xb000180e | %1 - UITaskHandler::ProcessActivationData hr = %2\r\n
0xb000180f | %1 - UITaskHandler::Show received. Direction:[%2]\r\n
0xb0001810 | %1 - Navigation in progress. Queuing up the Show\r\n
0xb0001811 | %1 - UITaskHandler::Show hr = %2\r\n
0xb0001812 | %1 - UITaskHandler::ShowInternal. Direction:[%2:NavigationDirection:]\r\n
0xb0001813 | %1 - UITaskHandler::ShowInternal. hr = %2\r\n
0xb0001814 | %1 - UITaskHandler::Hide received. Direction:[%2]\r\n
0xb0001815 | %1 - Navigation in progress. Cancelling Show and ignoring Hide\r\n
0xb0001816 | %1 - UITaskHandler::Hide hr = %2\r\n
0xb0001817 | %1 - UITaskHandler::NavigateTo received TaskID:[%2]\r\n
0xb0001818 | %1 - UITaskHandler::NavigateTo. hr = %2\r\n
0xb0001819 | %1 - UITaskHandler::NavigationComplete TaskID:[%2]\r\n
0xb000181a | %1 - UITaskHandler::NavigationComplete hr = %2\r\n
0xb000181b | %1 - UITaskHandler::NavigateAway received TaskID:[%2]\r\n
0xb000181c | %1 - Navigation interrupted since Task is closing\r\n
0xb000181d | %1 - Navigation in progress. Queuing up the NavigateAway\r\n
0xb000181e | %1 - UITaskHandler::NavigateAway hr = %2\r\n
0xb000181f | %1 - UITaskHandler::NavigateAwayInternal TaskID:[%2]\r\n
0xb0001820 | %1 - UITaskHandler::NavigateAwayInternal hr = %2\r\n
0xb0001821 | %1 - UITaskHandler::RequestClose called TaskID:[%2]\r\n
0xb0001822 | %1 - UITaskHandler::RequestClose hr = %2\r\n
0xb0001823 | %1 - LaunchSession in progress. Cannot add another callback\r\n
0xb0001824 | %1 - UITaskHandler::LaunchSession hr = %2\r\n
0xb0001825 | %1 - LaunchChildTask in progress. Cannot add another callback\r\n
0xb0001826 | %1 - UITaskHandler::LaunchChildTask hr = %2\r\n
0xb0001827 | %1 - UITaskHandler::SetPauseOnLock[%2] called TaskID:[%3]\r\n
0xb0001828 | %1 - UITaskHandler::SetPauseOnLock hr = %2\r\n
0xb0001829 | %1 - UITaskHandler::Close received TaskID:[%2]\r\n
0xb000182a | %1 - UITaskHandler::Close hr = %2\r\n
0xb000182b | %1 - UITaskHandler::SystemKeyPressed received: [%2]\r\n
0xb000182c | %1 - UITaskHandler::SystemKeyPressed processed\r\n
0xb000182d | %1 - UITaskHandler::SystemKeyPressed pending. Will be processed on RuntimeHost ready\r\n
0xb000182e | %1 - UITaskHandler::LaunchChildTaskComplete received with result %2\r\n
0xb000182f | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001830 | %1 - UITaskHandler::LaunchSessionComplete received with result %2\r\n
0xb0001831 | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001832 | %1 - OrientationChanged NewOrientation=%2\r\n
0xb0001833 | %1 - OrientationChange received before RuntimeHostTask is set\r\n
0xb0001834 | %1 - SetSupportedOrientations. SupportedOrientations:[%2]. hr = %3\r\n
0xb0001835 | %1 - GetSupportedOrientations. SupportedOrientations[%2]. hr = %3\r\n
0xb0001836 | %1 - GetCurrentOrientation. CurrentOrientation[%2]. hr = %3\r\n
0xb0001837 | %1 - UITaskHandler::ReplaceTouchEndpoint hr = %2\r\n
0xb0001838 | %1 - UITaskHandler::ReplaceTextEndpoint hr = %2\r\n
0xb0001839 | %1 - UITaskHandler::Get Task State. StateSize[%2]. hr = %3\r\n
0xb000183a | %1 - UITaskHandler::Set Task State. StateSize[%2]. hr = %3\r\n
0xb000183b | %1 - UITaskHandler::OnObscurityChange[%2]. hr = %3\r\n
0xb000183c | %1 - UITaskHandler::OnLockScreenVisibilityChange[%2]. hr = %3\r\n
0xb000183d | %1 - UITaskHandler::OnSipVisibilityChange[%2]. hr = %3\r\n
0xb000183e | %1 - UITaskHandler::OnShowAnimationComplete\r\n
0xb000183f | %1 - UITaskHandler::Window.Visible property changed [%2]\r\n
0xb0001840 | %1 - FreezeHost event triggered\r\n
0xb0001841 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001842 | %1 - CancelTask TaskId=%2\r\n
0xb0001843 | %1 - OnHostPausing\r\n
0xb0001844 | %1 - OnHostPausing failed with hr = %2\r\n
0xb0001845 | %1 - OnHostPaused\r\n
0xb0001846 | %1 - OnHostPaused failed with hr = %2\r\n
0xb0001847 | %1 - FreezeHost event triggered\r\n
0xb0001848 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001849 | %1 - CancelTask received while executing in background\r\n
0xb000184a | %1 - CancelTask received. Ignoring since this is a valid transition only when running in background\r\n
0xb000184b | %1 - CancelTask hr = %2\r\n
0xb000184c | %1 - TPA entry: %2\\%3%4;\r\n
0xb000184d | %1 - Platform Assemblies List: %2\r\n
0xb000184e | %1 - ParseManifestFile HResult = %2\r\n
0xb000184f | %1 - NotifyError ! Unable to disable NI optimizations\r\n
0xb0001850 | %1 - NotifyError ! Unable to set the debugger wait env variable\r\n
0xb0001851 | %1 - TestTrustedPath: %2\r\n
0xb0001852 | %1 - TestAppPaths: %2\r\n
0xb0001853 | %1 - NotifyError ! Failed to set the test settings\r\n
0xb0001854 | %1 - GetAppPaths failed with hr = %2\r\n
0xb0001855 | %1 - NotifyError ! message = %2, source = %3\r\n
0xb0001856 | %1 - NotifyError ! hr=%2. message = %3\r\n
0xb0001857 | %1 - GetIsoStoreAvailableFreeSpace hr = %2\r\n
0xb0001858 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb0001859 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb000185a | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185b | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185c | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb000185d | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb000185e | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb000185f | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb0001860 | %1 - GetQualifiedMutexName returned:[%2]. AllowedMutexCount:[%3]\r\n\r\n
0xb0001861 | %1 - XcpHost::Start() failed with hr = %2\r\n
0xb0001862 | %1 - Shutting down the SL runtime...\r\n
0xb0001863 | %1 - Calling into XcpHost::Pausing %2\r\n
0xb0001864 | %1 - XcpHost::Pausing %2\r\n
0xb0001865 | %1 - Calling into XcpHost::Pause %2\r\n
0xb0001866 | %1 - XcpHost::Pause %2\r\n
0xb0001867 | %1 - Calling into XcpHost::Resume %2\r\n
0xb0001868 | %1 - XcpHost::Resume %2\r\n
0xb0001869 | %1 - Calling into XcpHost::Resumed %2\r\n
0xb000186a | %1 - XcpHost::Resumed %2\r\n
0xb000186b | %1 - XcpHost::CompleteTask called TaskID:[%2]\r\n
0xb000186c | %1 - CompleteTask called when XcpTask is null. This likely indicates CompleteTask getting called twice\r\n
0xb000186d | %1 - Error in OnApplicationStarted\r\n
0xb000186e | %1 - Error in OnApplicationConstructing\r\n
0xb000186f | %1 - LaunchSession hr = %2\r\n
0xb0001870 | %1 - LaunchChildTask hr = %2\r\n
0xb0001871 | %1 - Raising Task.OnLaunching\r\n
0xb0001872 | %1 - Raised Task.OnLaunching\r\n
0xb0001873 | %1 - Raising Task.OnPause. PauseReason[%2]\r\n
0xb0001874 | %1 - Raised Task.OnPause\r\n
0xb0001875 | %1 - Raising Task.OnResume. IsExecutionContextPreserved[%2]\r\n
0xb0001876 | %1 - Raised Task.OnResume\r\n
0xb0001877 | %1 - Raising Task.OnRunningInBackground\r\n
0xb0001878 | %1 - Raised Task.OnRunningInBackground\r\n
0xb0001879 | %1 - Raising Task.OnCancel\r\n
0xb000187a | %1 - Raised Task.OnCancel\r\n
0xb000187b | %1 - Raising Task.OnHostDehydarting\r\n
0xb000187c | %1 - Raised Task.OnHostDehydarting\r\n
0xb000187d | %1 - Raising Task.OnNavigateTo\r\n
0xb000187e | %1 - Raised Task.OnNavigateTo\r\n
0xb000187f | %1 - Raising Task.OnNavigateAway\r\n
0xb0001880 | %1 - Raised Task.OnNavigateAway\r\n
0xb0001881 | %1 - Raising Task.OnShow\r\n
0xb0001882 | %1 - Raised Task.OnShow\r\n
0xb0001883 | %1 - Raising Task.OnHide\r\n
0xb0001884 | %1 - Raised Task.OnHide\r\n
0xb0001885 | %1 - Raising Task.OnSystemKeyPressed\r\n
0xb0001886 | %1 - Raised Task.OnSystemKeyPressed\r\n
0xb0001887 | %1 - Raising Task.OnChildTaskReturned\r\n
0xb0001888 | %1 - Raised Task.OnChildTaskReturned\r\n
0xb0001889 | %1 - Raising Task.OnObscurityChange\r\n
0xb000188a | %1 - Raised Task.OnObscurityChange\r\n
0xb000188b | %1 - Raising Task.OnLockScreenVisibilityChange\r\n
0xb000188c | %1 - Raised Task.OnLockScreenVisibilityChange\r\n
0xb000188d | %1 - Raising Task.OnClosing\r\n
0xb000188e | %1 - Raised Task.OnClosing\r\n
0xb000188f | %1 - RegisterAppCallbacks hr = %2\r\n
0xb0001890 | %1 - RegisterTaskCallbacks hr = %2\r\n
0xb0001891 | %1 - TaskReadyToShow hr = %2\r\n
0xb0001892 | %1 - RequestCloseTask hr = %2\r\n
0xb0001893 | %1 - CompleteTask hr = %2\r\n
0xb0001894 | %1 - DestroyTaskCallbacks hr = %2\r\n
0xb0001895 | %1 - SetHostErrorCode hrHostError = %2, hr = %3\r\n
0xb0001896 | %1 - LaunchSession[%2] hr = %3\r\n
0xb0001897 | %1 - GetTaskState hr = %2\r\n
0xb0001898 | %1 - SetTaskState hr = %2\r\n
0xb0001899 | %1 - LaunchChildTask[%2] hr = %3\r\n
0xb000189a | %1 - GetTaskAppChromeHandle hr = %2\r\n
0xb000189b | %1 - SetTaskPauseOnLock hr = %2\r\n
0xb000189c | %1 - SetHostObscurity[%2] hr = %3\r\n
0xb000189d | %1 - Entering Modal state\r\n
0xb000189e | %1 - Exiting Modal state hr = %2\r\n
0xb000189f | %1 - NotifyError: message=%2, source=%3\r\n
0xb00018a0 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb00018a1 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb00018a2 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a3 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a4 | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb00018a5 | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb00018a6 | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb00018a7 | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb00018a8 | %1 - Raising Task.OnRefresh\r\n
0xb00018a9 | %1 - Raised Task.OnRefresh\r\n
0xb00018aa | %1 - UITaskHandler::RequestNavigateBack called TaskID:[%2]\r\n
0xb00018ab | %1 - UITaskHandler::RequestNavigateBack hr = %2\r\n
0xb00018ac | %1 - RequestNavigateBack hr = %2\r\n
0xb00018ad | %1 - UITaskHandler::SetFullScreen[%2] called TaskID:[%3]\r\n
0xb00018ae | %1 - UITaskHandler::SetFullScreen hr = %2\r\n
0xb00018af | %1 - SetTaskFullScreen hr = %2\r\n
0xb00018b0 | %1 - Raising Task.OnApplicationLayerChange\r\n
0xb00018b1 | %1 - Raised Task.OnApplicationLayerChange\r\n
0xb00018b2 | %1 - Raising Task.OnRequestOverlayStateChange. State=%2\r\n
0xb00018b3 | %1 - Raised Task.OnRequestOverlayStateChange\r\n
0xb00018b4 | %1 - ApplicationLayerChanged NewApplicationLayer=%2\r\n
0xb00018b5 | %1 - ApplicationLayerChange received before RuntimeHostTask is set\r\n
0xb00018b6 | %1 - AgTaskHandler::LaunchSession hr = %2\r\n
0xb00018b7 | %1 - AgTaskHandler::LaunchChildTask hr = %2\r\n
0xb00018b8 | %1 - GetSessionDisplayName. DisplayName=%2 hr = %3\r\n
0xb00018b9 | %1 - AgTaskHandler::ConnectionComplete received\r\n
0xb00018ba | %1 - AgTaskHandler::ConnectionComplete hr = %2\r\n
0xb00018bb | %1 - UITaskHandler::OnNavigationBarVisibilityChange[%2]. hr = %3\r\n
0xb00018bc | %1 - Raising Task.OnModernActivation\r\n
0xb00018bd | %1 - Raised Task.OnModernActivation\r\n
0xb00018be | %1 - UITaskHandler::LaunchModernChooser hr = %2\r\n
0xb00018bf | %1 - LaunchChildTask hr = %2\r\n
0xb00018c0 | %1 - LaunchModernChooser[%2] hr = %3\r\n
0xb00018c1 | %1 - TaskFirstPresentCompleted = %2\r\n
0xb00018c2 | %1 - UITaskHandler::FirstPresentCompleted called TaskID:[%2]\r\n
0xb00018c3 | %1 - UITaskHandler::FirstPresentCompleted hr = %2\r\n
0xb0001fa4 | AgHost - FrameworkView::Initialize HRESULT=%1\r\n
0xb0001fa5 | AgHost - FrameworkView::SetWindow HRESULT=%1\r\n
0xb0001fa6 | AgHost - FrameworkView::Load HRESULT=%1\r\n
0xb0001fa7 | AgHost - FrameworkView::Run HRESULT=%1\r\n
0xb0001fa8 | AgHost - FrameworkView::Uninitialize HRESULT=%1\r\n
0xb0001fa9 | AgHost - FrameworkView::OnActivated PreviousExecutionState=%1 ActivationKind=%2 HRESULT=%3\r\n
0xb0001faa | AgHost - FrameworkView::OnExiting HRESULT=%1\r\n
0xb0001fab | AgHost - FrameworkView::OnResuming HRESULT=%1\r\n
0xb0001fac | AgHost - FrameworkView::OnSuspending HRESULT=%1\r\n
0xb0001fae | AgHostSvcs - EmCancelTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001faf | AgHostSvcs - EmCreateTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb0 | AgHostSvcs - EmExitTaskHost HRESULT=%1\r\n
0xb0001fb1 | AgHostSvcs - EmPauseTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb2 | AgHostSvcs - EmResumeTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb3 | AgHostSvcs - EmSetTaskInstanceApplicationUri TaskID=%1 ApplicationUri=%2 HRESULT=%3\r\n
0xb0001fb4 | AgHostSvcs - EmSetTaskInstanceArguments TaskID=%1 HRESULT=%2\r\n
0xb0001fb5 | AgHostSvcs - EmSetTaskInstanceBackgroundTaskId TaskID=%1 BackgroundTaskID=%2 HRESULT=%3\r\n
0xb0001fb6 | AgHostSvcs - EmSetTaskInstanceNavigationPage TaskID=%1 NavigationPage=%2 HRESULT=%3\r\n
0xb0001fb7 | AgHostSvcs - EmStartTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb8 | AgHostSvcs - TaskCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fb9 | AgHostSvcs - TaskPaused TaskID=%1 HRESULT=%2\r\n
0xb0001fba | AgHostSvcs - TaskRunning TaskID=%1 HRESULT=%2\r\n
0xb0001fbb | AgHostSvcs - TaskRunningInBackground TaskID=%1 HRESULT=%2\r\n
0xb0001fbc | AgHostSvcs - TaskRunningInForeground TaskID=%1 HRESULT=%2\r\n
0xb0001fbd | AgHostSvcs - EmWaitForTaskInstanceCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fbe | AgHostSvcs - OnModernContractActivation TaskID=%1 HRESULT=%2\r\n
0xb0002008 | EEC: GetExtendedExecutionBroker ProcessId=%1 HRESULT=%2\r\n
0xb0002009 | EEC: RegisterRevokedHandler ProcessId=%1 HRESULT=%2\r\n
0xb000200a | EEC: RequestExtendedExecution ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200b | EEC: ExtensionRevokedCallback ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200c | EEC: CompleteExtendedExecution ProcessId=%1 HRESULT=%2\r\n
0xb000206c | ODB: LaunchTask - UserSid: %1 SessionId: %2 PackageFullName: %3 EntryPoint: %4 WorkItemId: %5 HRESULT: %6.\r\n
0xb000206d | ODB: CancelTask - UserSid: %1 SessionId: %2 WorkItemId: %3 RudeTerminate: %4 CancellationReason: %5 HRESULT: %6.\r\n
0xb000206e | ODB: BeforeTaskActivated - WorkItemId: %1 PsmKey: %2 HostJobType: %3 HRESULT: %4.\r\n
0xb000206f | ODB: TaskActivated - WorkItemId: %1 TaskInstanceId: %2 PsmKey: %3 HRESULT: %4.\r\n
0xb0002070 | ODB: TaskCompleted - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002071 | ODB: TaskCanceled - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002072 | ODB: Timeout in WaitForWnfStateQuiescentTimeout.\r\n
0xb0002073 | ODB: CancelBackgroundTaskWithWnf WorkItemId: %1.\r\n
0xb0002710 | %1\r\n
0xb0002711 | %1: %2\r\n
0xb0002712 | *** ExecFailFast ***   %1\r\n
0xb000271a | PreInstallTaskPolicy: Activate task for User = %1 HRESULT = %2\r\n
0xb000271b | PreInstallTaskPolicy: BiActivate WorkItemId = %1 for user = %2, PackageFullName = %3, EntryPoint = %4, HRESULT = %5\r\n
0xb0010205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1' WorkItemId='%2;' CallbackId='%3' HostId='%5' ResourceSetId='%6'.\r\n
0xb0010206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1' HostId='%3' ResourceSetId='%4'.\r\n
0xd0000001 | Resumed\r\n
0xd0000002 | Quiescing\r\n
0xd0000003 | Quiesced\r\n
0xd0000004 | Frozen\r\n
0xd0000005 | Dehydrated\r\n
0xd0000006 | Terminated\r\n
0xd0000007 | Resumed\r\n
0xd0000008 | Suspending\r\n
0xd0000009 | Suspended\r\n
0xd000000a | Terminated\r\n
0xd000000b | NotBackground\r\n
0xd000000c | MixedHost\r\n
0xd000000d | PureHost\r\n
0xd000000e | SystemHost\r\n
0xd000000f | InvalidType\r\n
0xd0000010 | Permitted\r\n
0xd0000011 | Buffered\r\n
0xd0000012 | Dropped\r\n
0xd0000013 | InvalidType\r\n
0xd0000014 | Invalid\r\n
0xd0000015 | ForegroundApp\r\n
0xd0000016 | Cbe\r\n
0xd0000017 | ForegroundAgent\r\n
0xd0000018 | GbaPeriodic\r\n
0xd0000019 | GbaIdle\r\n
0xd000001a | BackgroundAudio\r\n
0xd000001b | BackgroundWorker\r\n
0xd000001c | Voip\r\n
0xd000001d | Oem\r\n
0xd000001e | Invalid\r\n
0xd000001f | Started\r\n
0xd0000020 | Paused\r\n
0xd0000021 | Resumed\r\n
0xd0000022 | MovedToBackground\r\n
0xd0000023 | RunUnderLock\r\n
0xd0000024 | Invalid\r\n
0xd0000025 | OK\r\n
0xd0000026 | Abort\r\n
0xd0000027 | Unexpected\r\n
0xd0000028 | ExceededRuntime\r\n
0xd0000029 | ResourcesSeized\r\n
0xd000002a | Paused\r\n
0xd000002b | Resumed\r\n
0xd000002c | ScreenLock\r\n
0xd000002d | ScreenUnlocked\r\n
0xd000002e | MovedToBackground\r\n
0xd000002f | CbeExitTimeout\r\n
0xd0000030 | CbeExitBatterySaver\r\n
0xd0000031 | CbeExitParallelAgentPolicy\r\n
0xd0000032 | CbeExitResourcesUnavailable\r\n
0xd0000033 | CbeExitControlPanel\r\n
0xd0000034 | CbeExitBandwidthSavings\r\n
0xd0000035 | HeadlessHost\r\n
0xd0000036 | TaskHost\r\n
0xd0000037 | XcpHost\r\n
0xd0000038 | TaskHostSvcs\r\n
0xd0000039 | TaskHostUnitTests\r\n
0xd000003a | HOST_CREATED\r\n
0xd000003b | HOST_INITIALIZED\r\n
0xd000003c | HOST_RUNNING\r\n
0xd000003d | STARTING_TASK\r\n
0xd000003e | REHYDRATING_TASK\r\n
0xd000003f | HOST_READY\r\n
0xd0000040 | HOST_PAUSING\r\n
0xd0000041 | PAUSING_TASK\r\n
0xd0000042 | PAUSED_TASK\r\n
0xd0000043 | HOST_PAUSED\r\n
0xd0000044 | RESUMING_TASK\r\n
0xd0000045 | HOST_GOING_IN_BACKGROUND\r\n
0xd0000046 | TASK_GOING_IN_BACKGROUND\r\n
0xd0000047 | HOST_IN_BACKGROUND\r\n
0xd0000048 | TASK_GOING_IN_FOREGROUND\r\n
0xd0000049 | GRACEFULLY_DEHYDRATING_HOST\r\n
0xd000004a | HOST_VISIBLE\r\n
0xd000004b | HOST_HIDDEN\r\n
0xd000004c | HOST_FROZEN\r\n
0xd000004d | HOST_THAWED\r\n
0xd000004e | HOST_EXITING\r\n
0xd000004f | HOST_ERROR\r\n
0xd0000050 | Direction_Forward\r\n
0xd0000051 | Direction_Backward\r\n
0xd0000052 | Direction_ForceSize\r\n
0xd0000053 | Resumed\r\n
0xd0000054 | Pausing\r\n
0xd0000055 | Paused\r\n
0xd0000056 | Dehydrated\r\n
0xd0000057 | Completed\r\n
0xd0000058 | none\r\n
0xd0000059 | launch\r\n
0xd000005a | debug\r\n
0xd000005b | task completion\r\n
0xd000005c | dependency\r\n
0xd000005d | multi-view\r\n
0xd000005e | Waiting\r\n
0xd000005f | CompletedWithResult\r\n
0xd0000060 | CompletedWithNoResult\r\n
0xd0000061 | Foreground\r\n
0xd0000062 | Lock\r\n
0xd0000063 | Overlay\r\n
0xd0000064 | ModernForeground\r\n
0xd0000065 | Pausing\r\n
0xd0000066 | PausingLowPri\r\n
0xd0000067 | Paused\r\n
0xd0000068 | PausedHighPri\r\n
0xd0000069 | PausedDNK\r\n
0xd000006a | Frozen\r\n
0xd000006b | FrozenHighPri\r\n
0xd000006c | FrozenDNK\r\n
0xd000006d | FrozenDNCS\r\n
0xd000006e | LockScreen\r\n
0xd000006f | Overlay\r\n
0xd0000070 | 11\r\n
0xd0000071 | CalendarAsChild\r\n
0xd0000072 | VideoTranscode\r\n
0xd0000073 | CBE\r\n
0xd0000074 | GenericExtendedExecution\r\n
0xd0000075 | ModernForegroundExtended\r\n
0xd0000076 | TaskCompletionHighPriority\r\n
0xd0000077 | ModernForegroundLarge\r\n
0xd0000078 | ShellCustom1\r\n
0xd0000079 | ShellCustom2\r\n
0xd000007a | ShellCustom3\r\n
0xd000007b | ShellCustom4\r\n
0xd000007c | Composer\r\n
0xd000007d | DebugModeForeground\r\n
0xd000007e | ComponentTarget\r\n
0xd000007f | PiP\r\n
0xd0000080 | Balloon\r\n
0xd0000081 | Invalid\r\n
0xd0000082 | Unevaluated\r\n
0xd0000083 | EvaluationPending\r\n
0xd0000084 | Evaluated\r\n
0xd0000085 | BACKGROUND_ACCESS_USER_STATE_ALLOWED\r\n
0xd0000086 | BACKGROUND_ACCESS_USER_STATE_DISABLED\r\n
0xd0000087 | BACKGROUND_ACCESS_USER_STATE_LOCKED_BY_DEVICE_MANAGEMENT\r\n
0xd0000088 | BACKGROUND_ACCESS_STATE_DEFAULT\r\n
0xd0000089 | BACKGROUND_ACCESS_STATE_DISABLED\r\n
0xd000008a | BACKGROUND_ACCESS_STATE_ALWAYS_ALLOWED\r\n
0xd000008b | BACKGROUND_ACCESS_STATE_LOCKED_BY_DEVICE_MANAGEMENT\r\n
0xd000008c | BACKGROUND_ACCESS_STATE_NCB_ENABLED\r\n
0xd000008d | BACKGROUND_ACCESS_STATE_DISABLED_BY_SYSTEM\r\n
0xd000008e | BACKGROUND_ACCESS_STATE_DISABLED_BY_USER\r\n
0xd000008f | BACKGROUND_ACCESS_STATE_HIGH_PRIORITY_HOST\r\n
0xd0000090 | BACKGROUND_ACCESS_STATE_UNLIMITED_LIFETIME\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000006 | ExecMan\r\n
0x10000009 | TaskHost\r\n
0x1000000d | Sqm\r\n
0x1000000f | Lifetime Manager\r\n
0x10000010 | ForegroundManager\r\n
0x10000011 | Background Manager\r\n
0x10000012 | Production Circular\r\n
0x10000013 | Production Critical\r\n
0x10000014 | SelfHost Circular\r\n
0x10000015 | SelfHost Critical\r\n
0x10000016 | DevPlat Circular\r\n
0x10000017 | VOIP\r\n
0x1000001b | Activation Manager\r\n
0x1000001c | AgHost\r\n
0x10000020 | Telemetry\r\n
0x10000021 | ExtendedExecutionClient\r\n
0x10000022 | OnDemandBroker\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000007 | Resume\r\n
0x30000008 | Suspend\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000048 | Background Access User State Changed\r\n
0x70000049 | Background Access Package State Changed\r\n
0x90000001 | Microsoft-Windows-AppModelExecEvents\r\n
0xb0000064 | DepMgr: Removed suspension group from the graph, PsmKey=%1\r\n
0xb0000065 | Not set app %1 into halted state because it should wait for other apps in the package halted first\r\n
0xb0000066 | Not set app %1 into halted state because other app in the package have not finished quiescing\r\n
0xb0000067 | Not terminate app %1, because target app %2 state = %3\r\n
0xb0000068 | Updated current dependency graph (Removal : %1) with Source %2 and Target %3 for type %4 in return %5\r\n
0xb0000069 | Default time for %1 overridden to %2 ms\r\n
0xb000006a | Creating hang report\r\n
0xb000006b | Window %1 is hung in foreground\r\n
0xb000006c | Window %1 is no longer hung in foreground\r\n
0xb000006d | Waiting for WER reporting to finish on app %1\r\n
0xb000006e | Hang reporting finished on app %1.  App termination status: %2\r\n
0xb000006f | Hung reporting finished on window %1 with result %2\r\n
0xb0000070 | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb0000071 | _SubmitActivationHangWerReport(stop): Aumid=%1, result=%2\r\n
0xb0000072 | _UnregisterForStateChanges: fPackageLevel=%1, HRESULT is %2. Cookie is %3\r\n
0xb0000073 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000074 | Canceled launch grace timer, PsmKey=%1\r\n
0xb0000075 | _InitializeLaunchGraceContext: Aumid=%1, fExtendedLaunch=%2, fEventExists=%3\r\n
0xb0000076 | App %1 successfully launched and its launch grace period expired: removing suspend exemption\r\n
0xb0000077 | Forcefully terminating app, Aumid=%1 flags=%2, reason=%3\r\n
0xb0000078 | CheckTerminationBeforeSwitch: Should terminate: %1, Aumid=%2, HRESULT=%3, reason=%4, fIsMisbehaving=%5\r\n
0xb0000079 | Termination requested for %1 - flags %2\r\n
0xb000007a | Failing TerminateApp due to pending task completions: %1\r\n
0xb000007b | Terminating %1 immediately\r\n
0xb000007c | Uninstalling background work items for %1\r\n
0xb000007d | Termination of %1 scheduled for %2 ms in future\r\n
0xb000007e | Sent window message to the default immersive browser with HRESULT %1\r\n
0xb000007f | Attempting to terminate app %1 prior to new app launch due to pending termination\r\n
0xb0000080 | EvaluateAndTerminatePid: PID: %1. HRESULT: %2. Package State: %3\r\n
0xb0000081 | Exempting application %1 from suspend while it is being launched\r\n
0xb0000082 | Exemption manager %1 is requesting a higher minimum priority %2 for %3\r\n
0xb0000083 | Debug mode is enabled for %1, so it will run at %2 priority\r\n
0xb0000084 | Handling logoff, %1 will run at %2 priority\r\n
0xb0000085 | Throttling has been disabled, so %1 will run at %2 priority\r\n
0xb0000086 | Suspend denied due to new key debounce, PsmKey=%1\r\n
0xb0000087 | Suspend denied due to debug mode, PsmKey=%1\r\n
0xb0000088 | Not suspending application %1 due to exemption %2\r\n
0xb0000089 | _EvaluateAndSuspendApplication: PsmKey=%1, fIsSuspendAllowed=%2, HRESULT=%3\r\n
0xb000008a | _ReevaluatePolicy: Ignoring debug mode app, PsmKey=%1\r\n
0xb000008b | ManagePreExistingApps(start)\r\n
0xb000008c | ManagePreExistingApps: PsmKey=%1, Aumid=%2, hr=%3\r\n
0xb000008d | ManagePreExistingApps(stop)\r\n
0xb000008e | RequestSuspendTimeout called for application %1 and timeout %2\r\n
0xb000008f | Debug mode enabled, PkgFamilyName=%1\r\n
0xb0000090 | Debug mode disabled, PkgFamilyName=%1\r\n
0xb0000091 | Set Package %1, Timeout to %2\r\n
0xb0000092 | ResumeDebugModePackage(start): package=%1\r\n
0xb0000093 | ResumeDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000094 | SuspendDebugModePackage(start): package=%1\r\n
0xb0000095 | SuspendDebugModePackage(stop): package=%1, HRESULT=%2\r\n
0xb0000096 | MultiAppSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000097 | MultiAppSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb0000098 | MultiPackageSuspendAndTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb0000099 | MultiPackageSuspendAndTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009a | MultiPackageSuspendAndPendTerminateSync(start): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3\r\n
0xb000009b | MultiPackageSuspendAndPendTerminateSync(stop): cPsmKeys=%1, suspendTrigger=%2, terminateReason=%3, HRESULT=%4\r\n
0xb000009c | TerminateSync(start): PsmKey=%1, type=%2, reason=%3\r\n
0xb000009d | TerminateSync(stop): PsmKey=%1, hrLogReason=%2, hrTermination=%3\r\n
0xb000009e | TerminatePackageSync(start): Package=%1, type=%2, reason=%3\r\n
0xb000009f | TerminatePackageSync(stop): Package=%1, fPlmKnowsPackage=%2, HRESULT=%3\r\n
0xb00000a0 | _TerminateAllSuspendedApplications(start)\r\n
0xb00000a1 | _TerminateAllSuspendedApplications(stop): HRESULT=%1\r\n
0xb00000a2 | Application %1 is blocking Connected Standby\r\n
0xb00000a3 | Exiting Connected Standby\r\n
0xb00000a4 | All packages have been suspended or terminated. Notify PDC. Call to PdcNotificationClientAcknowledge() returned %1\r\n
0xb00000a5 | Kernel State Change Callback: There were %1 PIDs present in the callback data\r\n
0xb00000a6 | Kernel State Change Callback: The state source was %1\r\n
0xb00000a7 | PDC_CONTROL_ABORT: PdcNotificationClientAcknowledge(STATUS_SUCCESS) returned %1\r\n
0xb00000a8 | Not terminating application %1 in _EvaluateAndTerminateApplication because it contains a running IImmersiveApplication\r\n
0xb00000a9 | Not terminating application %1 in _EvaluateAndTerminateApplication because it is a long running app\r\n
0xb00000aa | Not terminating application %1 in _EvaluateAndTerminateApplication due to pending task completion\r\n
0xb00000ab | Not terminating application %1 in _EvaluateAndTerminateApplication due to Launch Grace\r\n
0xb00000ac | Not terminating application %1 in _EvaluateAndTerminateApplication due to debug mode\r\n
0xb00000ad | Not terminating application %1 in _EvaluateAndTerminateApplication due to application had already been terminated\r\n
0xb00000ae | _EvaluateAndTerminateApplication: Skipping child suspension group, PsmKey=%1\r\n
0xb00000af | An empty application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b0 | Parent allowed suspension for child app, childPsmKey=%1\r\n
0xb00000b1 | GroupChildWithParent: ChildPsmKey=%1, HRESULT=%2\r\n
0xb00000b2 | Call a command line '%1' to notify default browser with result %2\r\n
0xb00000b3 | Read executable path from registry with result %1\r\n
0xb00000b4 | Application %1 was added to PLM Data Store and registering for PSM notification\r\n
0xb00000b5 | Resume the PPLE app %1 when receiving the PSM new key notification\r\n
0xb00000b6 | An orphaned prereq application was detected. Setting pending termination for application %1, HRESULT %2\r\n
0xb00000b7 | Not terminating dependent application %1 in _EvaluateAndTerminateDependentApplication due other dependency applications\r\n
0xb00000b8 | _EvaluateAndTerminateSourceApplication: Aumid=%1, exemption=%2\r\n
0xb00000b9 | An force termination exemption Application was detected. Setting pending termination for application %1\r\n
0xb00000ba | StateMgr: State queued, PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000bb | StateMgr: OnApplicationStarted set to active, PsmKey=%1\r\n
0xb00000bc | StateMgr: OnApplicationStarted finished, PsmKey=%1, HRESULT=%2\r\n
0xb00000bd | StateMgr: App's current state has changed, PsmKey=%1, state=%2\r\n
0xb00000be | StateMgr: OnApplicationTerminated(start), PsmKey=%1\r\n
0xb00000bf | StateMgr: Application terminated signaled, PsmKey=%1\r\n
0xb00000c0 | StateMgr: OnApplicationTerminated(stop), PsmKey=%1\r\n
0xb00000c1 | StateMgr: GetTerminateSyncData, PsmKey=%1, hr=%2\r\n
0xb00000c2 | StateMgr: _ProcessStateQueue(start): PsmKey=%1, state=%2\r\n
0xb00000c3 | StateMgr: _ProcessStateQueue(stop): PsmKey=%1, state=%2, HRESULT=%3\r\n
0xb00000c4 | StateMgr: Queue's pause state has changed to %2, PsmKey=%1\r\n
0xb00000c5 | StateMgr: App's committed state has changed, PsmKey=%1, state=%2\r\n
0xb00000c6 | Enabling debug mode on package %1\r\n
0xb00000c7 | Disabling debug mode on package %1\r\n
0xb00000c8 | Suspending package %1 via debug API. HRESULT: %2\r\n
0xb00000c9 | Resuming package %1 via debug API. HRESULT: %2\r\n
0xb00000ca | Terminating package %1 via debug API. HRESULT: %2\r\n
0xb00000cb | Default time for %1 overridden to %2 ms\r\n
0xb00000cc | ReportActivationHangSync: Halt application Aumid=%1, result=%2\r\n
0xb00000cd | _SubmitActivationHangWerReport(start): Aumid=%1, PIDs=%2 count=%3\r\n
0xb00000ce | _SubmitActivationHangWerReport(stop): Aumid=%1 canceled(%2) result=%3\r\n
0xb00000cf | PLM doesn't swap out application %1 due to its swap state %2\r\n
0xb00000d0 | PLM termination policy started on background thread because application %1 failed to outswap\r\n
0xb00000d1 | PLM termination policy finished. Outswapping returned status %1\r\n
0xb00000d2 | PLM memory policy will be aggressive because this is a disconnected session\r\n
0xb00000d3 | PLM termination policy start\r\n
0xb00000d4 | PLM termination policy stop\r\n
0xb00000d5 | PLM termination policy triggered by in use memory of %1 MiB\r\n
0xb00000d6 | PLM termination policy triggered by commit charge of %1 MiB\r\n
0xb00000d7 | MemoryPolicyWatcherTerminateCommitCharge\r\n
0xb00000d8 | PLM empty policy triggered by in use memory of %1 MB\r\n
0xb00000d9 | PLM memory policy does not allow termination of application %1 for reason %2\r\n
0xb00000da | PLM memory policy allows termination of application %1\r\n
0xb00000db | Application %1 was hidden %2 seconds ago\r\n
0xb00000dc | Application %1 is the clipboard owner\r\n
0xb00000dd | PLM empty policy start\r\n
0xb00000de | PLM empty policy ignoring application %1 with error code %2\r\n
0xb00000df | PLM empty policy finished after emptying %1 MiB\r\n
0xb00000e0 | PLM termination policy enumerated %1 applications\r\n
0xb00000e1 | PLM memory policy chose application %1 as its termination candidate, over old candidate application %2\r\n
0xb00000e2 | PLM memory policy will terminate application %1 with memory size %2 MiB and score %3\r\n
0xb00000e3 | PLM memory policy received MemWatcher event\r\n
0xb00000e4 | PLM memory policy received MemWatcher event\r\n
0xb00000e5 | Package exemption manager denied suspend for %1.  Ref counts are LAUNCH=%2, PSMREG=%3, PSMPENDING=%4\r\n
0xb00000e6 | Package Exemption Manager: ReferenceAdded:%1, %2 ref to application %3. The ref counts are now LAUNCH=%4, PSMREG=%5, and PSMREGPENDING=%6\r\n
0xb00000e7 | Package %1 added to the package data store\r\n
0xb00000e8 | Resetting priority to unpause the suspension group, PsmKey=%1\r\n
0xb00000e9 | Changed the priority of %1 to %2\r\n
0xb00000ea | AllowServiceOfPackages(start): cPackages=%1, fNotifyBi=%2\r\n
0xb00000eb | AllowServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ec | FinishedServiceOfPackages(start): cPackages=%1\r\n
0xb00000ed | FinishedServiceOfPackages(stop): HRESULT=%1\r\n
0xb00000ee | AllowUninstallOfPackage(start): package=%1\r\n
0xb00000ef | AllowUninstallOfPackage(stop): package=%1, HRESULT=%2\r\n
0xb00000f0 | Forcefully terminating misbehaving app %1 due to activation failure %2\r\n
0xb00000f1 | App %1: Change = %2\r\n
0xb00000f2 | PsmKey %1 has state %2\r\n
0xb00000f3 | Changing app state through BI, PsmKey=%1, state=%2 terminate action=%3\r\n
0xb00000f4 | Changing the package state of %1 through BI to %2\r\n
0xb00000f5 | OnAfterQuiescing: Quiesce began for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f6 | _CompleteQuiesceHelper: Queued termination for timed-out PsmKey %1\r\n
0xb00000f7 | Quiesce completed for PsmKey=%1, reason=%2, suspendTrigger=%3\r\n
0xb00000f8 | Suspend trigger updated for PsmKey=%1, suspendTrigger=%2\r\n
0xb00000f9 | ExtendQuiesceTimeout: PsmKey=%1, request=%2 ms, HRESULT=%3\r\n
0xb00000fa | _CompleteQuiesceHelper: Ignore timed-out PsmKey %1 as is being debugged\r\n
0xb00000fb | ResumeHelper: Application resume(start), PsmKey=%1, reason=%2\r\n
0xb00000fc | ResumeHelper: Application resume(stop), PsmKey=%1, reason=%2, HRESULT=%3\r\n
0xb00000fd | Resume reason updated for PsmKey=%1, reason=%2\r\n
0xb00000fe | RPC 0->1 transition detected for %1\r\n
0xb00000ff | RPC exemption was granted for application %1. KernelRequest Value: %2. Runaway RPC: %3.  RPC Debounce %4\r\n
0xb0000100 | RPC debounce received for package %1\r\n
0xb0000101 | Application %1 has successfully launched. HRESULT %2\r\n
0xb0000102 | Application %1 termination is blocked. PreserverProcessRequest = %2, TaskCompletionCategory = %3\r\n
0xb0000103 | PdcSystem activation (Activate = %1). Result = %2\r\n
0xb0000104 | NetworkAudio entries: %1, IsNetworkReferenced: %2\r\n
0xb0000105 | App %1 is Sharing\r\n
0xb0000106 | Share %1 has started in app %2\r\n
0xb0000107 | Share %1 in app %2 has stopped\r\n
0xb0000108 | Queued termination reason updated for PsmKey=%1, reason=%2\r\n
0xb0000109 | ClearTerminationTypesForForgottenPackage(start): PkgFamilyName=%1\r\n
0xb000010a | Cleared termination type for forgotten app, Aumid=%1, HRESULT=%2\r\n
0xb000010b | ClearTerminationTypesForForgottenPackage(stop): PkgFamilyName=%1, HRESULT=%2\r\n
0xb000010c | Writing to termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010d | Reading termination type reg key for Aumid=%1, type=%2, HRESULT=%3\r\n
0xb000010e | _ExtendForResourceStarvation: PsmKey=%1, TimerType=%2, newRelativeExpirationTimeMs=%3, ElapsedMs=%4, CpuRunningMs=%5, CpuReadyMs=%6, IoNormalMs=%7\r\n
0xb000010f | Foreground resume delay %1 milliseconds\r\n
0xb0000110 | Suspend allowed for %1 - Session not active\r\n
0xb0000111 | Suspend denied due to a visible window or visibility debounce, PsmKey=%1\r\n
0xb0000112 | Suspend denied for %1 - UserRequest non-zero\r\n
0xb0000113 | Suspend denied for %1- failure %2\r\n
0xb0000114 | OnWindowChanged: Aumid=%1, Hwnd=%2, change=%3, fDeferredVisibility=%4, HRESULT=%5\r\n
0xb0000115 | Starting Session Idle Debounce\r\n
0xb0000116 | Session is active\r\n
0xb0000117 | Session is idle\r\n
0xb0000118 | PlmGetPackageFullNameFromAppId, Aumid=%1, HRESULT=%2\r\n
0xb0000119 | Session idle state change -- calling _ReevaluatePolicy\r\n
0xb000011a | RegisterForActivationStateChanges: Act:%1 App:%2 HRESULT is %3. Cookie is %4\r\n
0xb000011b | UnregisterForActivationStateChanges: Cookie is %1\r\n
0xb000011c | Can Auto Terminate app %1 %2\r\n
0xb000011d | TerminateApplicationBeforeActivation(start): Aumid=%1\r\n
0xb000011e | TerminateApplicationBeforeActivation: wait for terminate, Aumid=%1, HRESULT=%2\r\n
0xb000011f | TerminateApplicationBeforeActivation(stop): Aumid=%1, reason=%2, HRESULT=%3\r\n
0xb0000120 | s_SuspendPackagesAtLogOff(start)\r\n
0xb0000121 | s_SuspendPackagesAtLogOff(stop): HRESULT=%1\r\n
0xb0000122 | StateMgr: OnApplicationStarted still halted, PsmKey=%1\r\n
0xb0000123 | Added Task Completion under %1 for application %2\r\n
0xb0000124 | Removed Task Completion under %1 for application %2\r\n
0xb0000125 | Illegal state change happened to App: %1\r\n
0xb0000126 | EnableDebugMode failed: %1\r\n
0xb0000127 | DisableDebugMode: RoDisableDebuggingForPackage failed with result %1\r\n
0xb0000128 | DisableDebugMode: OnDebugModeDisabled failed with result %1\r\n
0xb0000129 | DisableDebugMode: Enabling activation timeout failed with result %1\r\n
0xb000012a | DisableDebugMode failed: %1\r\n
0xb000012b | Couldn't open process: %1\r\n
0xb000012c | PLM failed to process a hang for window %1 with error code %2\r\n
0xb000012d | PLM outswap application %1 failed to invoke with error code %2\r\n
0xb000012e | PLM couldn't find any process for application %1, and handle it as non-large app\r\n
0xb000012f | PLM failed to decide application %1 is large or not with error code %2\r\n
0xb0000130 | PLM empty policy failed to process application %1 with error code %2.  Ignoring the application\r\n
0xb0000131 | PLM empty policy failed to empty application %1 with error code %2\r\n
0xb0000132 | PLM failed to terminate application %1 as empty policy with error code %2\r\n
0xb0000133 | PLM empty policy failed to enumerate applications with error code %1\r\n
0xb0000134 | PLM termination policy skipping application %1, which is not registered with PLM\r\n
0xb0000135 | PLM memory policy failed to queue work with error code %1\r\n
0xb0000136 | GetPackageData called on a Package %1, which is not in the PLM Package Data Store\r\n
0xb0000137 | ERROR: Failed to set priority to %1, PsmKey=%2, NTSTATUS=%3\r\n
0xb0000138 | AllowServiceOfPackages: Failed to terminate package=%1, type=%2, HRESULT=%3\r\n
0xb0000139 | _CheckServicingPackages: Failed to enumerate app, PsmKey=%1, HRESULT=%2\r\n
0xb000013a | _CheckServicingPackages: Failed to enumerate package, PkgFullName=%1, HRESULT=%2\r\n
0xb000013b | GetImmersiveApplicationCount failed with error code %1\r\n
0xb000013c | Background workitems were force terminated, PsmKey=%1\r\n
0xb000013d | ChangeApplicationBiState failed: %1\r\n
0xb000013e | Background workitems for package %1 were force terminated\r\n
0xb000013f | ChangePackageBiState failed: %1\r\n
0xb0000140 | ApplicationProcesses failed to track process ID %1 with error code %2\r\n
0xb0000141 | OnBeforeQuiescing: Failed to allocate memory for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000142 | OnAfterQuiescing: Quiesce failed for PsmKey=%1, suspendTrigger=%2, HRESULT=%3\r\n
0xb0000143 | ERROR: _CompleteQuiesceHelper: Failed to terminate timed-out PsmKey %1 with result %2\r\n
0xb0000144 | ERROR: QuiesceHelper: App forgotten while still Quiescing, PsmKey=%1, suspendTrigger=%2\r\n
0xb0000145 | Failed to query the wake counters associated with application %1. NTSTATUS: %2\r\n
0xb0000146 | _AllAppSyncOperationHelper: Failed to allocate memory for PsmKey=%1, HRESULT=%2\r\n
0xb0000147 | _MultiAppSyncOperationHelper: Failed to perform operation on PsmKey=%1, HRESULT=%2\r\n
0xb0000148 | _MultiAppSyncOperationHelper: Failed in wait, HRESULT=%1\r\n
0xb0000149 | _MultiPackageSyncOperationHelper: Failed to enumerate PsmKey=%1, HRESULT=%2\r\n
0xb000014a | _MultiPackageSyncOperationHelper: Failed to find package in data store, PkgFullName=1%, HRESULT=%2\r\n
0xb000014b | Failed to suspend and terminate apps, cPsmKeys=%1\r\n
0xb000014c | Could not initialize an extended launch grace period for app %1 with HRESULT %2 -- falling back to normal launch grace\r\n
0xb000014d | App %1 failed to show a window after launch. Will attempt to terminate it now\r\n
0xb000014e | Failed to get a window for an app; assuming that the app's window is not hung, Aumid=%1, HRESULT=%2\r\n
0xb000014f | Failed to query hidden time for visibility debounce for app %1 with error code %2\r\n
0xb0000150 | _StartNewKeyDebounce: Error Result=%2, PsmKey=%1\r\n
0xb0000151 | StartTrackingNewApp failed with %1. The application launch is not protected and the app might potentially get suspended inappropriately\r\n
0xb0000152 | ERROR: Failed to enumerate exemption targets starting from PsmKey=%1\r\n
0xb0000153 | Failed to enumerate existing applications from PSM with error code %1\r\n
0xb0000154 | PsmRegisterApplicationNotification failed for application %1 with status %2.  PLM's cache says that the application's registration is: %3\r\n
0xb0000155 | ERROR: Failed to enumerate force termination targets starting from PsmKey=%1, HRESULT=%2\r\n
0xb0000156 | Application %1 failed to be added in PLM Data Store\r\n
0xb0000157 | Failed to initialize string to send app notification %1 state %2\r\n
0xb0000158 | Failed to initialize string to remove app %1\r\n
0xb0000159 | Failed to add %1 for application %2. The application doesn't have BTC_AUDIO background task capability\r\n
0xb000015a | Failed to initialize CmApi\r\n
0xb000015b | Task completion manager failed to add %1 to its sharing cache with error code %2\r\n
0xb000015c | ClearTerminationTypesForForgottenPackage: Failed to clear termination type for app, Aumid=%1, HRESULT=%2\r\n
0xb000015d | ERROR: Failed to schedule the visibility debounce, PsmKey=%1, HRESULT=%2\r\n
0xb000015e | OnWindowChanged ERROR: Failed to queue thread for Aumid=%1, Hwnd=%2, change=%3, HRESULT=%4\r\n
0xb000015f | ERROR: Failed to schedule deferred visibility timer, PsmKey=%1, HRESULT=%2\r\n
0xb0000160 | WaitOnBiNotifyNewSession HRBiNotifyNewSession=%1 HRBiNotifyNewUser=%2\r\n
0xb0000161 | RegisterKernelNotifications HRESULT=%1\r\n
0xb0000162 | TCExemptionManager CompleteInitialization HRESULT=%1\r\n
0xb0000163 | PlmActivationManager CompleteInitialization HRESULT=%1\r\n
0xb0000164 | Plm CSDiagnostics CompleteInitialization HRESULT=%1\r\n
0xb0000165 | Plm LogOff/LogOn Registration HRESULT=%1\r\n
0xb00001f9 | BM: Queued evaluate WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fa | BM: Evaluate returned WorkItem: %3 EventType: %5 Action: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb00001fb | BM: TaskActivated WorkItem: %1 Instance: %2\r\n
0xb00001fc | BM: TaskCompleted WorkItem: %1 Instance: %2\r\n
0xb00001fd | BM: TaskCanceled WorkItem: %1 Instance: %2\r\n
0xb00001fe | BM: Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb00001ff | BM: TaskActivating WorkItem: %1 Instance: %2\r\n
0xb0000200 | BM: Enter %1\r\n
0xb0000201 | BM: Exit %1, HR=%2\r\n
0xb0000202 | BM: TerminateHost WorkItem: %1\r\n
0xb0000203 | BM: ResourceSet invalidated for WorkItem: %1 Instance: %2.  This usually means the host has crashed before a ResourceSet could be applied.\r\n
0xb0000204 | BM: OnAcquired ignoring invalid CallbackId (%1).\r\n
0xb0000205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1'; WorkItemId='%2;' CallbackId='%3'.\r\n
0xb0000206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1'.\r\n
0xb0000207 | BM: OnApplicationStateChanged returning State='%2' PsmKey='%1' HR='%3'.\r\n
0xb0000208 | BM: OnAcquired received for CallbackId: %1\r\n
0xb0000209 | BM: OnAcquired request ignored for CallbackId: %1\r\n
0xb000020a | BM: ActivateDeferredWorkItem WorkItem: %1\r\n
0xb000020b | BM: ActivateDeferredWorkItem discarded WorkItem: %1 because of Status: %2\r\n
0xb000020c | BM: Enter %1 WorkItem: %2\r\n
0xb000020d | BM: Enter %1 WorkItem: %2 TaskInstanceId: %3\r\n
0xb000020e | BM: Exit %1\r\n
0xb000020f | BM: Failed to load settings for event %1.\r\n
0xb0000210 | BM: Failed to load settings for event %1 with error %2.\r\n
0xb0000211 | BM: Failed to load policy for CLSID: %1, for EventType %2 with error %3.\r\n
0xb0000212 | BM: Failed to load the policies with error %1.\r\n
0xb0000213 | BM: Evaluate returned WorkItem: %3 EventType: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2 EntryPoint: %4\r\n
0xb0000214 | BM: TaskWallClockActive WorkItem: %1 Instance: %2\r\n
0xb0000215 | BM: TaskWallClockExpired WorkItem: %1 Instance: %2\r\n
0xb0000216 | BM: Policy returned HRESULT: %3 for WorkItem: %2 PsmKey: %1.\r\n
0xb0000217 | BM: Canceling task for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000218 | BM: Ignoring cancelation request (whitelisted) for high energy usage PsmKey: %1 WorkItem: %2.\r\n
0xb0000219 | BM: Session(%1) started, session initialization returned %2.\r\n
0xb000021a | BM: Session(%1) ended.\r\n
0xb000021b | BM: Activation ignored due to no Session(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb000021c | BM: Failed to acquire a ResourceSet for WorkItem: %1 with error %2.\r\n
0xb000021d | BM: WorkItem: %1 is being debugged. Setting wallclock limit to 0.\r\n
0xb000021e | BM: EvaluateActivationAction for WorkItem: %1 HRESULT: %2.\r\n
0xb000021f | BM: Skipped Buffering Exempted task with SQMId: %1 PsmKey: %2.\r\n
0xb0000220 | BM: Dropped Exempted task that came before SessionReady with SQMId: %1 PsmKey: %2.\r\n
0xb0000221 | BM: Activation ignored due to no User(%1): PsmKey: %2 WorkItem: %3.\r\n
0xb0000222 | BM: User Logon Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000223 | BM: User Logoff Session: %1 User: %2 HRESULT: %3.\r\n
0xb0000224 | BM: Pending activation discarded for work item (%1).\r\n
0xb0000225 | BM: Flushing ignored EvaluationState: %1 for WorkItem: %2.\r\n
0xb0000226 | BM: Flushing buffered activations.\r\n
0xb0000227 | BM: Global Policy evaluate returned WorkItem: %3 EventType: %4 Action: %5 WallClockLimit: %6 PsmKey: %1 HostJobType: %2\r\n
0xb0000228 | BM: A Session object for Session(%1) already exists.\r\n
0xb0000229 | BM: ShellSuspendState changed, oldState: %1 newState: %2\r\n
0xb000022a | BM: DPLKeyState changed, oldState: %1 newState: %2\r\n
0xb000022b | BM: Canceling WorkItem: %1 due to DPL policy.\r\n
0xb000022c | BM: Dropping activation for WorkItem: %1 due to DPL policy.\r\n
0xb000022d | BM: Buffered activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022e | BM: Exempted activation for WorkItem: %1 due to Shell Ready policy.\r\n
0xb000022f | BM: Buffered activation for WorkItem: %1 due to Thermal Throttling policy.\r\n
0xb0000258 | AM: Failed to read activation plugin registry with error code %1.\r\n
0xb0000259 | AM: Failed to CoCreate activation plugin with error code %1 and CLSID %2.\r\n
0xb000025a | AM: Successfully created activation plugin with CLSID %1 from the registry.\r\n
0xb000025b | AM: Failed to register package if needed with error %1.\r\n
0xb000025c | AM: Failed trying to register package by family name async during activation with error %1.\r\n
0xb000025d | AM: Failed trying to wait for the completion of the register package by family async during activation with error %1.\r\n
0xb00002bc | BAM: Added Package: %1 UserSid: %2.\r\n
0xb00002bd | BAM: Removed Package: %1 UserSid: %2.\r\n
0xb00002be | BAM: Added Application: %1 UserSid: %2.\r\n
0xb00002bf | BAM: Removed Application: %1 UserSid: %2.\r\n
0xb00002c0 | BAM: AccessState Changed for Package: %1 OldState: %2 NewState: %3 UserSid: %4.\r\n
0xb00002c1 | BAM: BackgroundExecutionManager::RequestAccessAsync called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c2 | BAM: BackgroundExecutionManager::GetStatus called for Application: %1 Returned_AccessState: %2.\r\n
0xb00002c3 | BAM: BackgroundExecutionManager::RemoveAccess called for Application: %1.\r\n
0xb00002c4 | BAM: Sanitizing data for package: %1 HRESULT: %2.\r\n
0xb00002c5 | BAM: ReregisteredPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002c6 | BAM: UnregisterPackage called during _SanitizeStore for package: %1 HRESULT: %2.\r\n
0xb00002c7 | BAM: BackgroundExecutionManager::RequestAccessKindAsync called for Application: %1 Requested_AccessKind: %2 Returned: %3.\r\n
0xb00002c8 | Background Access State For User Modified CallerUserSid = %1 CallerProcessName = %2 CallerPackageFamilyName = %3 \r\n            OldConsentValue = %4 NewConsentValue = %5 IsSetByHigherAuthority = %6 EffectiveConsentValue = %7 TargetUserSid = %8 HRESULT = %9\r\n
0xb00002c9 | Background Access State For Package Modified CallerUserSid = %1 CallerProcessName = %2 CallerPackageFamilyName = %3 \r\n            OldConsentValue = %4 NewConsentValue = %5 IsSetByHigherAuthority = %6 EffectiveConsentValue = %7 TargetUserSid = %8 \r\n            TargetPackageFamilyName = %9 HRESULT = %10\r\n
0xb00002ee | FAM: NotifyTaskInstanceCompleted, TaskID:%1, hr:%2\r\n
0xb00002ef | FAM: NotifyTaskInstanceRunning, TaskID:%1 Timer - %2\r\n
0xb00002f0 | FAM: RegisterForegroundAgentManagerProxy:PID=%1, ConsumerTaskId=%2, Option=%3, hr=%4\r\n
0xb00002f1 | FAM: UiForeground:Memory:%1MB, CPU:%2%%\r\n
0xb00002f2 | FAM: CreateAgentLaunchRequest, TaskID:%1, Queue:%2, hr:%3\r\n
0xb00002f3 | FAM: CancelAgentRequest, TaskID:%1, CancelType=%2, hr:%3\r\n
0xb00002f4 | FAM: AbortAgentRequestsInternal, hr:%1\r\n
0xb00002f5 | FAM: CompleteAgent, TaskID:%1, hr:%2\r\n
0xb00002f6 | FAM: PrioritizeAgentRequest, TaskID:%1, hr:%2\r\n
0xb00002f7 | FAM: OnForegroundAppChanged()-Abort agents\r\n
0xb00002f8 | FAM: OnRelease()\r\n
0xb00002f9 | FAM: NotifyConsumer, Notification:%1, TaskID:%2, hrResult:%3\r\n
0xb00002fa | FAM: AcquireSharedResourceSet, ProductID:%1, ConsumerPid:%2, Pending:%3, hr:%4\r\n
0xb00002fb | FAM: ReleaseResourceSet, #%1, hr:%2\r\n
0xb00002fc | FAM: TimerExpired:TerminateHost[PID=%1]\r\n
0xb00002fd | FAM: AcquireResourceSet, #%1, Mem:%2MB, CPU:%3%%, hr:%4\r\n
0xb00002fe | FAM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000321 | OTM: Read settings. First retry timeout = %1 ms, Second retry timeout = %2 ms, Third retry timeout = %3 ms, Maximum Retry Timeout = %4 ms\r\n
0xb0000322 | OTM: Task instance %2 of product %1 completed\r\n
0xb0000323 | OTM: TaskHost of product %1 has crashed\r\n
0xb0000324 | OTM: TaskHost of product %1 has been completed by PacMan\r\n
0xb0000325 | OTM: Launching OEM boot agents\r\n
0xb0000326 | OTM: Launching boot agents for product %1 failed with error %2\r\n
0xb0000327 | OTM: Launch boot agents for product %1\r\n
0xb0000328 | OTM: Running OnUpdateStarted for product %1\r\n
0xb0000329 | OTM: Restarting boot agents for product %1 after update\r\n
0xb000032a | OTM: Start menu is ready.\r\n
0xb000032b | OTM: Could not launch OEM boot agents. QueueUserWorkItem failed with error %1.\r\n
0xb000032c | OTM: Could not process update notification for OEM application. QueueUserWorkItem failed with error %1.\r\n
0xb000032d | OTM: Could not process update notification for OEM application. ProcessUpdateNotification failed with error %1.\r\n
0xb000032e | OTM: OemTaskManager::NotifyTaskInstanceCompleted failed with error %1.\r\n
0xb000032f | OTM: OemTaskManager::NotifyTaskHostCompleted failed with error %1.\r\n
0xb0000330 | OTM: OemApp::DumpAgents failed with error %1.\r\n
0xb0000331 | OTM: An error occurred. Hr = %1\r\n
0xb0000332 | OTM: No apps with ServiceAgents were found.\r\n
0xb0000333 | OTM: No ServiceAgent task found for product %1.\r\n
0xb0000334 | OTM: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb000035d | PLM: Start tracking new app user %1 app %2, contract %3, hr = %4\r\n
0xb000035e | PLM: Application launched %1 in app %2, hr = %3\r\n
0xb000035f | PLM: Application resume %1 in app %2, hr = %3\r\n
0xb0000360 | PLM: Suspend-Terminate(%3) task %1 in app %2\r\n
0xb0000361 | PLM: Suspend-Terminate suspend of task %1 in app %2 exemption %3\r\n
0xb0000362 | PLM: Suspend-Terminate auto terminate(%3) task %1 in app %2\r\n
0xb0000363 | PLM: Suspend-Terminate task %1 in app %2, hr %3\r\n
0xb0000364 | PLM: Halt app %1, hr %2\r\n
0xb0000365 | PLM: Task resume %1 in app %2\r\n
0xb0000366 | PLM: Task cancel %1 in app %2\r\n
0xb0000367 | PLM: Task remove %1 in app %2\r\n
0xb0000368 | PLM: Queue Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000369 | PLM: Queue Activation State Change Notification %1 state %2\r\n
0xb000036a | PLM: Before Activate task %1 for user %2 in app %3, contract %4, hostid %5, hr = %6\r\n
0xb000036b | PLM: After Activate task %1 with result %2, hr = %3\r\n
0xb000036c | PLM: ApplicationLayer=%1 Set Foreground new task %2, prev task %3\r\n
0xb000036d | PLM: Add task %1 to user %2 and app %3, hr = %4\r\n
0xb000036e | PLM: Create app for user %1, %2, new [app(%3) pkg(%4)], hr = %5\r\n
0xb000036f | PLM: Add task %1 to user %2 and app %3, new [app(%4) pkg(%5)], hr = %6\r\n
0xb0000370 | PLM: Remove task %1, was found(%2)\r\n
0xb0000371 | PLM: Remove app if empty from user %1, %2, hr = %3\r\n
0xb0000372 | PLM: Remove pkg if empty from user %1, %2, hr = %3\r\n
0xb0000373 | PLM: Send Application State Change Notification for user %1 app %2 state %3\r\n
0xb0000374 | PLM: Send Activation State Change Notification %1 state %2\r\n
0xb0000376 | PLM: Timer Started duration %1ms, hr %2\r\n
0xb0000377 | PLM: Timer Expired duration %1ms, hr %2\r\n
0xb0000378 | PLM: Abort task %1 reason %2, dump(%3)\r\n
0xb0000379 | PLM: Task rehydrate %1 in app %2 contract %3\r\n
0xb000037a | PLM: Start RPC suspension timer PSMKey=%1 WakeCounters=%2, hr = %3\r\n
0xb000037b | PLM: Cancel RPC suspension timer PSMKey=%1 app state=%2\r\n
0xb000037c | PLM: Terminate application PSMKey=%1 due to expired RPC suspension timeout\r\n
0xb000037d | PLM: Application %1 cannot be terminated due to %2 exemption\r\n
0xb000037e | PLM: Application %1 can be terminated\r\n
0xb000037f | PLM: EvaluateAndTerminateApplication %1 cannot be terminated due to %2\r\n
0xb0000380 | PLM: EvaluateAndTerminateApplication %1, terminate hr = %2\r\n
0xb0000381 | PLM: Terminate debounce app %1 current state %2 ultimate state %3\r\n
0xb0000382 | PLM: Terminate debounce app %1, hr = %2\r\n
0xb0000383 | PLM: Terminate reason was cleared\r\n
0xb0000384 | PLM: Abort app user %1 app %2 reason %3, dump(%4)\r\n
0xb0000385 | PLM: Watson dump NOT generated for user %1 app %2, process count %3\r\n
0xb0000386 | PLM: Watson dump start for user %1 app %2 reason %3 description %4, process %5 (%6)\r\n
0xb0000387 | PLM: Watson dump information for user %1 app %2 product Id %3 title %4 version %5\r\n
0xb0000388 | PLM: Watson dump end for user %1 app %2, hr %3\r\n
0xb0000389 | PLM: Add Watson dump to user %1 app %2 process %3, hr %4\r\n
0xb000038a | PLM: Failed to add Watson process info for process %1 user %2 app %3\r\n
0xb000038b | PLM: Watson dump status changed pids(%1)\r\n
0xb000038c | PLM: Watson dump status changed, add process %1 user %2 app %3\r\n
0xb000038d | PLM: Watson dump status changed, remove process %1 user %2 app %3\r\n
0xb000038e | PLM: Watson dump status changed, unknown process %1 app %2\r\n
0xb000038f | PLM: Watson add/remove(%2) error report task completion to process %1 (signaled %4), hr %3\r\n
0xb0000390 | PLM: Watson in progress for PSMKey %1, waiting...\r\n
0xb0000391 | PLM: Watson in progress finished for PSMKey %1\r\n
0xb0000392 | PLM: Extending RPC suspension timer PSMKey=%1\r\n
0xb0000393 | PLM: Acquire network reference failed CM_RESULT=%1\r\n
0xb0000394 | PLM: Release network reference failed CM_RESULT=%1\r\n
0xb0000395 | PLM: Suspend-Terminate(%2) app %1 exemption %3, hr %4\r\n
0xb0000396 | PLM: Suspend-Terminate task %1 while dehydrating\r\n
0xb0000397 | PLM: Add user %1 sid %2 to data store, hr = %3\r\n
0xb0000398 | PLM: Start launch grace for user %1 app %2, hr = %3\r\n
0xb0000399 | PLM: Set Window Id for user %1 app %2 wnd %3\r\n
0xb000039a | PLM: EvaluateLaunchGraceCompleted for user %1 app %2\r\n
0xb000039b | PLM: Terminating reexisting app due to sihost restart with PSMKey %1, status %2\r\n
0xb000039c | PLM: Terminating preexisting applications on sihost startup\r\n
0xb000039d | PLM: Set Pause On Lock for user %1 app %2 value %3\r\n
0xb000041b | AAM: Initiate activation for user %1 app %2 contract %3 task %4, hr %5\r\n
0xb000041c | AAM: Initiate activation completed for task %2 (expected %1), hr %3\r\n
0xb000041d | AAM: Initialize activation for user %1 app %2 contract %3 lightup(%5), hr %4\r\n
0xb000041e | AAM: Validate activation, hr %1\r\n
0xb000041f | AAM: Verify license for pkg %1, hr %2\r\n
0xb0000420 | AAM: Activate activation task %1 host %2, hr %3\r\n
0xb0000421 | AAM: Activation shim timer expired %1, hr %2\r\n
0xb0000422 | AAM: Initiate Core UI, hr %1\r\n
0xb0000423 | AAM: Release Core UI\r\n
0xb0000424 | AAM: Create Windows AAM, hr %1\r\n
0xb0000425 | AAM: Attempted remediation, hr %1\r\n
0xb0000426 | AAM: Failed while trying to find a remediation handler, hr %1\r\n
0xb0000427 | AAM: Failed while trying to find the package status, hr %1\r\n
0xb0000428 | AAM: Failed while trying to find the package origin, hr %1\r\n
0xb0000429 | AAM: Failed while trying to verify and initialize the activation, hr %1\r\n
0xb000042a | AAM: Failed while trying to check roaming data, hr %1\r\n
0xb000042f | AAM: Broker created plugins %1, expected %2\r\n
0xb0000430 | AAM: Broker initialize, hr %1\r\n
0xb0000431 | AAM: Broker start activate application %1 (%3 args) arg[0] %2 type %4 caller PID %5 (initialization count %6)\r\n
0xb0000432 | AAM: Broker end activate application %1 launched PID %2 task %3, hr %4\r\n
0xb0000433 | AAM: Broker activate task with result for app %1 caller PID %2 caller task %3\r\n
0xb0000434 | AAM: Broker get result for PID %1 task %2 result %3, hr %4\r\n
0xb0000435 | AAM: Broker get task id for process %1 window %2 = task %3, hr %4\r\n
0xb0000436 | AAM: Broker init session manager, hr %1\r\n
0xb0000437 | AAM: Broker release session manager\r\n
0xb0000438 | AAM: Broker add task with result for parent %1, hr %2\r\n
0xb0000439 | AAM: Broker get task with result for parent %1, hr %2\r\n
0xb000043a | AAM: Broker remove task with result for parent %1, hr %2\r\n
0xb000043b | AAM: Broker create completed event for caller PID %1, hr %2\r\n
0xb000043c | AAM: Broker get task with result for child %1, hr %2\r\n
0xb000043d | AAM: Broker parent task completed %1 with child state %2\r\n
0xb000043e | AAM: Broker child task completed %1 with state %2, hr %3\r\n
0xb000043f | AAM: Broker task event signaled for parent %1 child %2 previous state %3, hr %4\r\n
0xb0000440 | AAM: Broker close task %1, hr %2\r\n
0xb0000441 | AAM: Broker activate application %1 arg[%3] %2\r\n
0xb000044c | FM-ARP: ApplyResourceSetType ResourceSetType=%1 User=%2 PSMKey=%3 ResourceSet=%4 HRESULT=%5\r\n
0xb000044d | FM-ARP: ApplyTerminal UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044e | FM-ARP: RemoveInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb000044f | FM-ARP: ResetInterruptiveUIAccess UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000450 | FM-ARP: OnRelease UserContext=%1 PsmKey=%2 ReleaseAction=%3 ReleasedCachedResource=%4 ReleaseAppliedResource=%5 HRESULT=%6\r\n
0xb0000451 | FM-ARP: OnAcquired UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000452 | FM-ARP: OnOutOfMemory UserContext=%1 PsmKey=%2 ResourceSet=%3 HRESULT=%4\r\n
0xb0000453 | FM-ARP: ApplyResourceBoost User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000454 | FM-ARP: AcquireResourceSet ResourceSetType=%1 Usercontext=%2 PsmKey=%3 HRESULT=%4\r\n
0xb0000455 | FM-ARP: Apply Cached Resource Set Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb0000456 | FM-ARP: Clear Cached Resource User=%1 PSMKey=%2\r\n
0xb0000457 | FM-ARP: Fire Cached ResourceCallback User=%1 PSMKey=%2\r\n
0xb00004b0 | FM-CAM: OnApplicationStateChangedEx UserContext=%1 PsmKey=%2 state=%3 HRESULT=%4\r\n
0xb00004b1 | FM-CAM: AcquireForegroundResource UserContext=%1 PsmKey=%2 isPending=%3\r\n
0xb00004b2 | FM-CAM: OnResourceAcquired UserContext=%1 PsmKey=%2\r\n
0xb00004b3 | FM-CAM: OnResourceTimerExpired UserContext=%1 PsmKey=%2\r\n
0xb00004e2 | FM: TaskCompletion New Battery Saver State %1\r\n
0xb00004e3 | FM: TaskCompletion Revoke Exemption PID=%1 AUMID=%2 TC=%3\r\n
0xb00004e4 | FM: TaskCompletion Apply(%3) Exemption PID=%1 TC=%2 HRESULT=%4\r\n
0xb00004e5 | FM-EEP: CheckProcessBackgroundEligibility ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e6 | FM-EEP: ApplyTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e7 | FM-EEP: RevokeTaskCompletion ProcessId=%1 TaskCompletionCategory=%2 HRESULT=%3\r\n
0xb00004e8 | FM-EEP: RequestExtendedExecution ProcessId=%1 Reason=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004e9 | FM-EEP: RegisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004ea | FM-EEP: CompleteExtendedExecution ProcessId=%1 fIsResumed=%2 HRESULT=%3\r\n
0xb00004eb | FM-EEP: RevokeSuspensionExtension User=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00004ec | FM-ARP: NotifyPendingResourceSetTransition ResourceSetType=%1 ResourceSet=%2 HRESULT=%3\r\n
0xb00004ed | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 fTimerExpiredCallback=%2 HRESULT=%3\r\n
0xb00004ee | FM-EEP: IsApplicationStateBackgroundEligibile User=%1 PsmKey=%2 fResult=%3\r\n
0xb00004ef | FM-EEP: RevokeTaskCompletionExemption AppUserModelId=%1 HRESULT=%2\r\n
0xb00004f0 | FM-EEP: AllowBackgroundExecution User=%1 AppUserModelId=%2 DeniedReason=%3 HRESULT=%4\r\n
0xb00004f1 | FM-EEP: OnPackageEnergyStateChange PackageFullName=%1 PackageState=%2 HRESULT=%3\r\n
0xb00004f2 | FM-EEP: RegisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f3 | FM-EEP: UnregisterExtendedExecutionClient ProcessId=%1 HRESULT=%2\r\n
0xb00004f4 | FM-EEP: UnregisterForExtensionRevokedEvent ProcessId=%1 HRESULT=%2\r\n
0xb00004f5 | FM-EEP: ApplyTaskCompletionResourceSet AppUserModelId=%1 TC=%2 isResourcePending =%3 HRESULT=%4\r\n
0xb00004f6 | FM-EEP: Task Completion Denied By EDP Policy ProcessId=%1 TC=%2\r\n
0xb00004f7 | FM-EEP: IsForegroundApplication Application=%1 Result=%2\r\n
0xb0000578 | FM: Registering callback %1 HRESULT=%2\r\n
0xb0000579 | FM: Generate ActivationInstanceID Id=%1\r\n
0xb000057a | FM: +ActivationPrerequisitePhase ActivationInstanceId=%1 UserContext=%2 AUMID=%3 ContractId=%4\r\n
0xb000057b | FM: -ActivationPrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb000057c | FM: +Resume_RehydrationPhase ActivationInstanceId=%1\r\n
0xb000057d | FM: -Resume_RehydrationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000057e | FM: +ResumeActivation ActivationInstanceId=%1 fIsResumed=%2\r\n
0xb000057f | FM: -ResumeActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000580 | FM: +Resume_ActivationPhase ActivationInstanceId=%1\r\n
0xb0000581 | FM: -Resume_ActivationPhase ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000582 | FM: +PauseActivation ActivationInstanceId=%1\r\n
0xb0000583 | FM: -PauseActivation HRESULT=%1 PausePending=%2\r\n
0xb0000584 | FM: +CancelActivation ActivationInstanceId=%1\r\n
0xb0000585 | FM: -CancelActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000586 | FM: +AbortActivation ActivationInstanceId=%1 Reason=%2 fGenerateWER=%3\r\n
0xb0000587 | FM: -AbortActivation ActivationInstanceId=%1 HRESULT=%2\r\n
0xb0000588 | FM: +GetActivationProcessId ActivationInstanceId=%1\r\n
0xb0000589 | FM: -GetActivationProcessId ActivationInstanceId=%1 PID%2 HRESULT=%3\r\n
0xb000058a | FM: +SetForegroundActivationInstance ActivationInstanceId=%1 Isforeground=%2\r\n
0xb000058b | FM: -SetForegroundActivationInstance ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000058c | FM: SetActivationDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb000058d | FM: OnActivationStateChanged ActivationInstanceId=%1 state=%2 HRESULT=%3\r\n
0xb000058e | FM: OnApplicationStateChanged UserContext=%1 PSMKey=%2 state=%3 HRESULT=%4\r\n
0xb000058f | FM: IsValidActivationProcessId ActivationInstanceID=%1 PID=%2 fValid=%3 HRESULT=%4\r\n
0xb0000590 | FM: GetForegroundProductId fIgnoreLockScreen=%1 ProductID=%2 HRESULT=%3\r\n
0xb0000591 | FM: GetProductIdFromProcessID ProductID=%1 PID=%2 HRESULT=%3\r\n
0xb0000592 | FM: Discarding Application Frozen notification because the application isn't really frozen\r\n
0xb0000593 | FM: Dehydrate Application AUMID=%1 HRESULT=%2\r\n
0xb0000594 | FM: +ResumePrerequisitePhase ActivationInstanceId=%1\r\n
0xb0000595 | FM: -ResumePrerequisitePhase HRESULT=%1 fPending=%2\r\n
0xb0000596 | FM: GenerateWatsonReport PID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000597 | FM: SetContinuation ActivationInstanceID=%1\r\n
0xb0000598 | FM: AbandonContinuation ActivationInstanceID=%1\r\n
0xb0000599 | FM: PerformContinuation ActivationInstanceID=%1\r\n
0xb000059a | FM: Shutdown HRESULT=%1\r\n
0xb000059b | FM: +PauseActivation ActivationInstanceId=%1 AUMID=%2 PackageFullName=%3\r\n
0xb000059c | FM: +ActivationBypass ActivationInstanceId=%1\r\n
0xb000059d | FM: -ActivationBypass ActivationInstanceId=%1 HRESULT=%2\r\n
0xb000059e | FM: +PostPausePendingResume ActivationInstanceId=%1\r\n
0xb000059f | FM: -PostPausePendingResume ActivationInstanceId=%1 HRESULT=%2\r\n
0xb00005a0 | FM: SetActivationImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb00005a1 | FM: NotifyWindowAdded TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a2 | FM: NotifyWindowRemoved TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a3 | FTM: Logoff User=%1 HRESULT=%2\r\n
0xb00005a4 | FM: ActivationTimeoutPolicyChanged  TaskID=%1 WindowInstanceId=%2 HRESULT=%3\r\n
0xb00005a5 | FM-EEP: OnConnectedStandbyStateChanged  State=%1\r\n
0xb00005a6 | FM: SendActivationNotification ActivationId=%1 NotificationId=%2\r\n
0xb00005a7 | FM: OnResourceAcquired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a8 | FM: OnResourceTimerExpired Usercontext=%1 PsmKey=%2 HRESULT=%3\r\n
0xb00005a9 | FM: PostPausePendingActivation ActivationId=%1 HRESULT=%2\r\n
0xb00007d0 | VoIPPolicy: Evaluate Activation Action for PsmKey = %2, WorkItemId = %1, Action = %3, HRESULT = %4\r\n
0xb00007d1 | VoIPPolicy: Task Activated for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d2 | VoIPPolicy: Task Completed for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d3 | VoIPPolicy: Task Canceled for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d4 | VoIPPolicy: Task Aborted for PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d5 | VoIPPolicy: Determine and Apply Resources PsmKey = %2, WorkItemId = %1, HRESULT = %3\r\n
0xb00007d6 | VOIP: NotifyVoipActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d7 | VOIP: LaunchVoipRtcTask called for PID:%1 PSMKey:{%2} with TaskEntryPoint:{%3} and WNFStateName:{%4} HRESULT:%5.\r\n
0xb00007d8 | VOIP: NotifyVoipActivityCompleted called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007d9 | VOIP: HoldActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007da | VOIP: UnholdActiveCall called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007db | VOIP: NotifyIncomingCallDialogDisplayed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dc | VOIP: NotifyIncomingCallDialogDismissed called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb00007dd | VOIP: CallActive called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007de | VOIP: AppLaunchVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007df | VOIP: OnVoipActivityCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e0 | VOIP: AppHoldActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e1 | VOIP: AppUnholdActiveCall called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e2 | VOIP: OnIncomingCallDialogDisplayed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e3 | VOIP: OnIncomingCallDialogDismissed called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007e4 | VOIP: AppDetermineAndApplyBestResourceSet called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e5 | VOIP: PolicyEvaluateAction called for WorkItemId:{%1} PSMKey:{%2} ActivationAction:%3 HRESULT:%4.\r\n
0xb00007e6 | VOIP: PolicyTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e7 | VOIP: PolicyTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e8 | VOIP: PolicyTaskCanceled called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007e9 | VOIP: PolicyTaskAborted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3.\r\n
0xb00007ea | VOIP: OnForegroundApplicationChanged called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007eb | VOIP: AppOnTaskActivated called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ec | VOIP: AppOnTaskCompleted called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ed | VOIP: AppCancelVoipRtcTask called for WorkItemId:{%1} PSMKey:{%2} HRESULT:%3 {InActiveCall:%4, HasRTCTask:%5 OnHold:%6 TaskCompletionApplied:%7 InForeground:%8}.\r\n
0xb00007ee | VOIP: CancelVoipRtcTask called for PID:%1 PSMKey:{%2} HRESULT:%3.\r\n
0xb0000c81 | Task: %1 has started\r\n
0xb0000c82 | Task: %1 has paused\r\n
0xb0000c83 | Task: %1 has resumed\r\n
0xb0000c84 | Task: %1 has completed\r\n
0xb0000c85 | EM: +GetTaskInfo()\r\n
0xb0000c86 | EM: -GetTaskInfo(). HRESULT = %1\r\n
0xb0000c87 | EM: GetAppInfo:%1,%2:%3\r\n
0xb0000c88 | EM: ParseBackgroundAbilities - HRESULT=%1\r\n
0xb0000c89 | EM: +ExecManServerHost::CreateProcess\r\n
0xb0000c8a | EM: -ExecManServerHost::CreateProcess. HRESULT=%1\r\n
0xb0000c8b | Sqm::AppPlatSqmAppDataUsage: %1/%2 - TaskID = %3, Type = %4, NewState = %5, ReasonForStateChange = %6, Duration (ms) = %7, PeakMemory (kb) = %8\r\n
0xb0000c8f | Emc::ExecuteCommand: StartTaskCallbackBegin: TaskID = %1\r\n
0xb0000c90 | Emc::ExecuteCommand: StartTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c91 | Emc::ExecuteCommand: PauseTaskCallbackBegin: TaskID = %1\r\n
0xb0000c92 | Emc::ExecuteCommand: PauseTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c93 | Emc::ExecuteCommand: ResumeTaskCallbackBegin: TaskID = %1\r\n
0xb0000c94 | Emc::ExecuteCommand: ResumeTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c95 | Emc::ExecuteCommand: ControlTaskCallbackBegin: TaskID = %1\r\n
0xb0000c96 | Emc::ExecuteCommand: ControlTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c97 | Emc::ExecuteCommand: CancelTaskCallbackBegin: TaskID = %1\r\n
0xb0000c98 | Emc::ExecuteCommand: CancelTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c99 | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackBegin: TaskID = %1\r\n
0xb0000c9a | Emc::ExecuteCommand: BackgroundExecutionTaskCallbackEnd: TaskID = %1, HR = %2\r\n
0xb0000c9e | Emc::RegisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, HR = %3\r\n
0xb0000ca8 | Emc::DeregisterBackgroundExecutionRequest: TaskID = %1, ExecutionType = %2, Reason = %3, HR = %4\r\n
0xb0000ca9 | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleBegin: ProductID = %1\r\n
0xb0000caa | Emc::EnsureXbfForCurrentLocale: EnsureXbfForCurrentLocaleEnd: ProductID = %1\r\n
0xb0000cab | EM: Skipping terminate process call for %1\r\n
0xb0000cac | EM: Terminating process: PID = %1, ExitCode = %2\r\n
0xb0000ce4 | AimServer::OnAgentRequestInvoked: AgentRequestID %1 was invoked. PID = %2, HR = %3\r\n
0xb0000ce5 | AimServer::ReadSettings: HR = %1\r\n
0xb0000ce6 | AimServer: Detected server for scope %1 terminated (PID = %2)\r\n
0xb0000ce8 | AimServer::HandleEvent: ProductID %1 received PM LifecyleEvent %2. HR Notification = %3, HR = %4\r\n
0xb0000ce9 | BA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cea | BA::RegisterServiceRequest: AlreadyReserved = %1, SR = %2, HR = %3\r\n
0xb0000ceb | BA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cec | BA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000ced | BA::NotifyTaskInstanceCompleted: Terminating Orphaned Host PID = %1\r\n
0xb0000cee | BA::OrphanAgentRequest: AgentRequestID = %1, HR = %2\r\n
0xb0000cef | BA::UnRegisterServiceRequest: Terminating host PID %1\r\n
0xb0000cf0 | BA::UnRegisterServiceRequest: Orphaning host PID %1\r\n
0xb0000cf1 | BA::UnRegisterServiceRequest: Terminating second old orphaned host PID %1\r\n
0xb0000cf2 | BTM::RecvCallback: Timer expired for AgentRequestID %1\r\n
0xb0000cf3 | BTM::LaunchTask: TaskURI = %1 TaskID = %2, PID = %3, HR = %4\r\n
0xb0000cf4 | GBA::NotifyTaskInstanceCompleted: AgentRequestID = %1\r\n
0xb0000cf5 | GBA::RegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf6 | GBA::UnRegisterServiceRequest: SR = %1, HR = %2\r\n
0xb0000cf7 | GBA::RegisterAgentRequest: AgentRequestID = %1, type = %2, hr = %3\r\n
0xb0000cf8 | GBA: Cancelling low priority %3 agent because high priority %2 needs to run: Resource was dedicated = %1\r\n
0xb0000cf9 | GBA::CancelAgentRequest: AgentRequestID = %1, CancelType = %2, PID = %3, HR = %4\r\n
0xb0000cfa | GBA::TryAcquireResourceSet: pending = %1, type = %2, HR = %3\r\n
0xb0000cfb | GBA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfc | BA::AbortTask: AgentRequestID = %1, HR = %2\r\n
0xb0000cfd | BA::NotifyTaskHostCompleted: ProductID = %1, PID = %2\r\n
0xb0000cfe | BA::RegisterAgentRequest: ProductID = %1, AgentRequestID = %2, HR = %3\r\n
0xb0000cff | BA::PdcActivationFailed: ProductID = %1, Reason = %2, NTSTATUS = %3\r\n
0xb0000dac | FTM: AllowBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dad | FTM: Process is using too much memory for BG Execution. PID=%1, MemUsage=%2, RequiredMemUsage=%3\r\n
0xb0000dae | FTM: Removing BG capability from Task ID %1 due to OOM\r\n
0xb0000daf | FTM: Battery Saver State has change. New state = %1\r\n
0xb0000db0 | FTM: Attempted new BG Execution request due to battery state change. TaskID=%1\r\n
0xb0000db1 | FTM: NotifyTaskInstanceCompleted TaskID=%1 HRESULT=%2\r\n
0xb0000db2 | FTM: NotifyTaskInstancePaused TaskID=%1 HRESULT=%2\r\n
0xb0000db3 | FTM: NotifyTaskInstanceRunning TaskID=%1 HRESULT=%2\r\n
0xb0000db4 | FTM: SendTaskStatusChange TaskID=%1 Status=%2 HRESULT=%3\r\n
0xb0000db5 | FTM: NotifyTaskHostCompleted HRESULT=%1\r\n
0xb0000db6 | FTM: Discarding NotifyTaskHostFrozen notification because the host isn't really frozen\r\n
0xb0000db7 | FTM: NotifyTaskHostFrozen PID=%1 HRESULT=%2\r\n
0xb0000db8 | FTM: NotifyTaskHostDehydrated HRESULT=%1\r\n
0xb0000db9 | FTM: Registering callback %1 HRESULT=%2\r\n
0xb0000dba | FTM: New Task %1 is dehydration-suppressing\r\n
0xb0000dbb | FTM: Applying Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbc | FTM: Revoking Dehydration-Suppressing Policy to Host PID %1\r\n
0xb0000dbd | FTM: +LaunchTask TaskURI=%1 LaunchFlags=%2\r\n
0xb0000dbe | FTM: -LaunchTask TaskURI=%1 TaskID=%2 PID=%3 HRESULT=%4\r\n
0xb0000dbf | FTM: ResumeTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc0 | FTM: Removing Foreground Resources from TaskID=%1\r\n
0xb0000dc1 | FTM: SetForegroundTaskInstanceId TaskID=%1 HRESULT=%2\r\n
0xb0000dc2 | FTM: PauseTask TaskID=%1 HRESULT=%2\r\n
0xb0000dc3 | FTM: CancelTask TaskID=%1 Frozen=%2 HRESULT=%3\r\n
0xb0000dc4 | FTM: AbortTask being ignored because the task is completed TaskID=%1\r\n
0xb0000dc5 | FTM: AbortTask TaskID=%1 Reason=%2 HRESULT=%3\r\n
0xb0000dc6 | FTM: SetTaskDehydrationEligibility TaskID=%1 State=%2 HRESULT=%3\r\n
0xb0000dc7 | FTM: RequestProcessBackgroundExecution type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc8 | FTM: CancelProcessBackgroundExecutionRequest type=%1 Pid=%2 HRESULT=%3\r\n
0xb0000dc9 | FTM: TaskRunningInBackground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dca | FTM: TaskRunningInForeground TaskID=%1 PID=%2  HRESULT=%3\r\n
0xb0000dcb | FTM: Changing activation policy to resume due to BG Execution for ProductID %1\r\n
0xb0000dcc | FTM: OnShutdownCompleted\r\n
0xb0000dcd | FTM: Ignoring expired watchdog for task %1 because it is being debugged.\r\n
0xb0000dce | FTM: Watchdog fired for task %1 while running in background. Pausing Task.\r\n
0xb0000dcf | FTM: Request BG Execution Denied because it wasn't running. TaskID=%1\r\n
0xb0000dd0 | FTM: Request BG Execution Denied because product was forbidden. TaskID=%1\r\n
0xb0000dd1 | FTM: Request BG Execution Denied because task didn't have BG abilities in its manifest. TaskID=%1\r\n
0xb0000dd2 | FTM: Request BG Execution Denied due to lack of resources. TaskID=%1\r\n
0xb0000dd3 | FTM: Request BG Execution Denied because battery policy prevented it. TaskID=%1\r\n
0xb0000dd4 | FTM: RequestBGAccess IsAllowed=%1 TaskID=%2 HRESULT=%3\r\n
0xb0000dd5 | FTM: RemoveBGRequest RequestedRemoval=%1 ActualRemoval=%2 TaskID=%3 HRESULT=%4\r\n
0xb0000dd6 | FTM: ForbidBackgroundExecution for ProductID %1. HRESULT=%2\r\n
0xb0000dd7 | FTM: IsValidTaskInstancePid TaskID=%1 Pid=%2 fValid=%3 HRESULT=%4\r\n
0xb0000dd8 | FTM: DetermineBestResourceSet for child ProductID=%1 LaunchFlags=%2 ResourceSetType=%3\r\n
0xb0000dd9 | FTM: OnRelease ResourceSet TaskID=%1 ResouceSet=%2 HRESULT=%3\r\n
0xb0000dda | FTM:UITask Call to Acquire network reference failed CM_RESULT=%1\r\n
0xb0000ddb | FTM:UITask Call to Release network reference failed CM_RESULT=%1\r\n
0xb0000ddc | FTM: SetTaskImportanceVector TaskID=%1 Vector=%2 HRESULT=%3\r\n
0xb0000ddd | FTM: +RequestProcessBackgroundExecution type=%1 Pid=%2\r\n
0xb0000dde | FTM: +RequestBackgroundExecution type=%1\r\n
0xb0000ddf | FTM: -RequestBackgroundExecution type=%1 HRESULT=%2\r\n
0xb0000de0 | FTM: +RequestBGAccess TaskInstanceId=%1 type=%2\r\n
0xb0000de1 | FTM: Request BG Execution Denied because DPL policy prevented it. TaskID=%1\r\n
0xb0000de2 | FTM: Windows Information Protection keys locked state (%1)\r\n
0xb0000e42 | VoIP: Foreground state for product %1 has changed. Is in foreground = %2\r\n
0xb0000e43 | VoIP: Canceling communication agent for product %1\r\n
0xb0000e44 | VoIP: Timer expired for keep-alive agent of product %1\r\n
0xb0000e45 | VoIP: Timer expired for incoming call agent of product %1\r\n
0xb0000e46 | VoIP: Launched agent instance with id %2 and URI %1\r\n
0xb0000e47 | VoIP: Canceled agent instance with id %1\r\n
0xb0000e48 | VoIP: Set active call resource set\r\n
0xb0000e49 | VoIP: Set communication agent resource set\r\n
0xb0000e4a | VoIP: Set VoIP Worker resource set\r\n
0xb0000e4b | VoIP: Applied terminal resource set\r\n
0xb0000e4c | VoIP: Last task instance completed. Releasing the task host ...\r\n
0xb0000e4d | VoIP: Launching active call agent instance for product %1\r\n
0xb0000e4e | VoIP: Canceling active call agent for product %1\r\n
0xb0000e4f | VoIP: Putting an active call on hold for product %1\r\n
0xb0000e50 | VoIP: Taking an active call off hold for product %1\r\n
0xb0000e51 | VoIP: Incoming call dialog has been displayed for product %1\r\n
0xb0000e52 | VoIP: Incoming call dialog has been dismissed for product %1\r\n
0xb0000e53 | VoIP: Launch communication agent request received from process %1 for product %2\r\n
0xb0000e54 | VoIP: Read settings. Keep alive timout = %1 ms, Max agent request queue = %2, Incoming call grace period = %3 ms, Incoming call dismissed grace period = %4 ms\r\n
0xb0000e55 | VoIP: Received request to launch agent type %2 for product %1\r\n
0xb0000e56 | VoIP: Task instance %2 of product %1 completed\r\n
0xb0000e57 | VoIP: Processing request to launch agent type %2 for product %1\r\n
0xb0000e58 | VoIP: Added VoIPApp object to map for product %1\r\n
0xb0000e59 | VoIP: Removed VoIPApp object from map for product %1\r\n
0xb0000e5a | VoIP: Getting VoIPApp object from map for product %1\r\n
0xb0000e5b | VoIP: Publishing WNF_DEVP_VOIP_ACTIVE_CALL_STATE_CHANGE failed with status %1\r\n
0xb0000e5c | VoIP: Subscribing to the WNF_WIFI_CONNECTION_STATUS event failed with status %1\r\n
0xb0000e5d | VoIP: Subscribed to WNF_WIFI_CONNECTION_STATUS? %1\r\n
0xb0000e5e | VoIP: WiFi connection status active/dormat? %1 (hConnection = %2)\r\n
0xb0000e5f | VoIP: RtlQueryWnfStateData failed trying to query the value of WNF_WIFI_CONNECTION_STATUS. NTSTATUS = %1\r\n
0xb0000e60 | VoIP: Could not spin up worker for UpdateWiFiStateHelper. HR =%1\r\n
0xb0000e61 | VoIP: In active call? %1\r\n
0xb0000e62 | VoIP: CmUtilSetWiFiActive was not successful. This could be because WiFi disconnected by the time we were notified of the connection.\r\n
0xb0000e63 | VoIP: WiFi connection status is %1.\r\n
0xb0000e64 | VoIP: AbortTask: TaskInstanceID = %1, HR = %2\r\n
0xb0000e65 | VoIP: PhoneServiceRestart: HR = %1\r\n
0xb0000e66 | VoIP: PhoneServiceRestart: Product = %1, HR = %2\r\n
0xb0000e67 | VoIP: Launching call query info agent instance for product %1\r\n
0xb0000e68 | VoIP: Canceling call query info agent instance for product %1\r\n
0xb0000e69 | VoIP: Terminating agents due to low memory for product %1\r\n
0xb0000e6a | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2\r\n
0xb0000e6b | VoIP: Acquired Pending ResourceSet for product = %1, Resourceset = %2, fApplied = %3, HR = %4\r\n
0xb0000e6c | VoIP: Set PDC Network Active for product = %1, NTSTATUS = %2\r\n
0xb0000e6d | VoIP: Set PDC Network Inactive for product = %1, NTSTATUS = %2\r\n
0xb0000e6e | VoIP: Renew PDC Network activation failed for product = %1, NTSTATUS = %2\r\n
0xb0000e73 | VoIP: An error occurred. Hr = %1\r\n
0xb00017d4 | %1 - [%2 = %3]\n\r\n
0xb00017d5 | %1 - Parsing config file [%2] file size = %3.  Parse = %4\r\n
0xb00017d6 | %1 - OnTaskModelMessage: Dispatching EM message\r\n
0xb00017d7 | %1 - InitializeTaskHost URI=%2, Page=%3, TaskId=%4\r\n
0xb00017d8 | %1 - Resuming Task from dehydration\r\n
0xb00017d9 | %1 - TaskHandler::GetTaskHandler hr=%2\r\n
0xb00017da | %1 - TaskHost Init\r\n
0xb00017db | %1 - TaskHost Init hr = %2\r\n
0xb00017dc | %1 - Host Dispatcher Exiting hr = %2\r\n
0xb00017dd | %1 - TaskHandlerReady received\r\n
0xb00017de | %1 - StartTask TaskId=%2\r\n
0xb00017df | %1 - PauseTask TaskId=%2\r\n
0xb00017e0 | %1 - ResumeTask TaskId=%2\r\n
0xb00017e1 | %1 - OnTaskHandlerVisible received\r\n
0xb00017e2 | %1 - OnTaskHandlerHidden received\r\n
0xb00017e3 | %1 - BackgroundExecutionCallback TaskId[%2] Command[%3]\r\n
0xb00017e4 | %1 - BackgroundExecutionCallback hr=%2\r\n
0xb00017e5 | %1 - OnHostRunning\r\n
0xb00017e6 | %1 - OnHostRunning. hr = %2\r\n
0xb00017e7 | %1 - Dehydrating. dehydrateGracefully = %2\r\n
0xb00017e8 | %1 - Gracefully dehydrating TaskHost\r\n
0xb00017e9 | %1 - TryDehydrateHost. hr = %2\r\n
0xb00017ea | %1 - DehydrateHost event triggered\r\n
0xb00017eb | %1 - WaitForUnfreeze hr = %2\r\n
0xb00017ec | %1 - ReduceMemoryHostCallback hr = %2\r\n
0xb00017ed | %1 - Graceful tear-down failed\r\n
0xb00017ee | %1 - BeforeHostRunningInBackgroundCallback\r\n
0xb00017ef | %1 - BeforeHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f0 | %1 - AfterHostRunningInBackgroundCallback\r\n
0xb00017f1 | %1 - AfterHostRunningInBackgroundCallback. hr = %2\r\n
0xb00017f2 | %1 - Unhandled exception occurred. hr = %2\r\n
0xb00017f3 | %1 - State-Transition (%2)->(%3)\r\n
0xb00017f4 | %1 - EnableProfiling = [%2]\r\n
0xb00017f5 | %1 - Profile Dll = [%2]\r\n
0xb00017f6 | %1 - ProfilerCLSID = [%2]\r\n
0xb00017f7 | %1 - TaskHostHelper::SetProfilerSettings hr = %2\r\n
0xb00017f8 | %1 - File path = %2 : %3\r\n
0xb00017f9 | %1 - Parse Element: %2.\r\n
0xb00017fa | %1 - Parse Element Value = %2 with pwszLocalName = %3.\r\n
0xb00017fb | %1 - Parse HResult = %2\r\n
0xb00017fc | %1 - YUTHost: failed to GAC trusted assembly %2\r\n\r\n
0xb00017fd | %1 - UITaskHandler::Initialize. hr = %2\r\n
0xb00017fe | %1 - UITaskHandler::Disconnect done\r\n
0xb00017ff | %1 - UITaskHandler::GoBackground. hr = %2\r\n
0xb0001800 | %1 - UITaskHandler::GoForeground. hr = %2\r\n
0xb0001801 | %1 - Managed Framework Ready. Handling Pending Event:[%2]\r\n
0xb0001802 | %1 - HandlePendingEvents Start TaskId=%2\r\n
0xb0001803 | %1 - HandlePendingEvents Pause TaskId=%2\r\n
0xb0001804 | %1 - HandlePendingEvents Resume TaskId=%2\r\n
0xb0001805 | %1 - Waiting for Siblings...\r\n
0xb0001806 | %1 - Waiting for Siblings done. hr = %2\r\n
0xb0001807 | %1 - UITaskHandler::OnRuntimeHostReady TaskID:[%2]\r\n
0xb0001808 | %1 - UITaskHandler::OnRuntimeHostReady. Processed pending SystemKeyPress [%2]\r\n
0xb0001809 | %1 - UITaskHandler::OnRuntimeHostReady hr = %2\r\n
0xb000180a | %1 - UITaskHandler::RegistrationComplete hr = %2\r\n
0xb000180b | %1 - UITaskHandler::ConnectionComplete received\r\n
0xb000180c | %1 - UITaskHandler::ConnectionComplete hr = %2\r\n
0xb000180d | %1 - UITaskHandler::ProcessActivationData received, reason=%2\r\n
0xb000180e | %1 - UITaskHandler::ProcessActivationData hr = %2\r\n
0xb000180f | %1 - UITaskHandler::Show received. Direction:[%2]\r\n
0xb0001810 | %1 - Navigation in progress. Queuing up the Show\r\n
0xb0001811 | %1 - UITaskHandler::Show hr = %2\r\n
0xb0001812 | %1 - UITaskHandler::ShowInternal. Direction:[%2:NavigationDirection:]\r\n
0xb0001813 | %1 - UITaskHandler::ShowInternal. hr = %2\r\n
0xb0001814 | %1 - UITaskHandler::Hide received. Direction:[%2]\r\n
0xb0001815 | %1 - Navigation in progress. Cancelling Show and ignoring Hide\r\n
0xb0001816 | %1 - UITaskHandler::Hide hr = %2\r\n
0xb0001817 | %1 - UITaskHandler::NavigateTo received TaskID:[%2]\r\n
0xb0001818 | %1 - UITaskHandler::NavigateTo. hr = %2\r\n
0xb0001819 | %1 - UITaskHandler::NavigationComplete TaskID:[%2]\r\n
0xb000181a | %1 - UITaskHandler::NavigationComplete hr = %2\r\n
0xb000181b | %1 - UITaskHandler::NavigateAway received TaskID:[%2]\r\n
0xb000181c | %1 - Navigation interrupted since Task is closing\r\n
0xb000181d | %1 - Navigation in progress. Queuing up the NavigateAway\r\n
0xb000181e | %1 - UITaskHandler::NavigateAway hr = %2\r\n
0xb000181f | %1 - UITaskHandler::NavigateAwayInternal TaskID:[%2]\r\n
0xb0001820 | %1 - UITaskHandler::NavigateAwayInternal hr = %2\r\n
0xb0001821 | %1 - UITaskHandler::RequestClose called TaskID:[%2]\r\n
0xb0001822 | %1 - UITaskHandler::RequestClose hr = %2\r\n
0xb0001823 | %1 - LaunchSession in progress. Cannot add another callback\r\n
0xb0001824 | %1 - UITaskHandler::LaunchSession hr = %2\r\n
0xb0001825 | %1 - LaunchChildTask in progress. Cannot add another callback\r\n
0xb0001826 | %1 - UITaskHandler::LaunchChildTask hr = %2\r\n
0xb0001827 | %1 - UITaskHandler::SetPauseOnLock[%2] called TaskID:[%3]\r\n
0xb0001828 | %1 - UITaskHandler::SetPauseOnLock hr = %2\r\n
0xb0001829 | %1 - UITaskHandler::Close received TaskID:[%2]\r\n
0xb000182a | %1 - UITaskHandler::Close hr = %2\r\n
0xb000182b | %1 - UITaskHandler::SystemKeyPressed received: [%2]\r\n
0xb000182c | %1 - UITaskHandler::SystemKeyPressed processed\r\n
0xb000182d | %1 - UITaskHandler::SystemKeyPressed pending. Will be processed on RuntimeHost ready\r\n
0xb000182e | %1 - UITaskHandler::LaunchChildTaskComplete received with result %2\r\n
0xb000182f | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001830 | %1 - UITaskHandler::LaunchSessionComplete received with result %2\r\n
0xb0001831 | %1 - UITaskHandler::LaunchChildTaskComplete result:%2 hr = %3\r\n
0xb0001832 | %1 - OrientationChanged NewOrientation=%2\r\n
0xb0001833 | %1 - OrientationChange received before RuntimeHostTask is set\r\n
0xb0001834 | %1 - SetSupportedOrientations. SupportedOrientations:[%2]. hr = %3\r\n
0xb0001835 | %1 - GetSupportedOrientations. SupportedOrientations[%2]. hr = %3\r\n
0xb0001836 | %1 - GetCurrentOrientation. CurrentOrientation[%2]. hr = %3\r\n
0xb0001837 | %1 - UITaskHandler::ReplaceTouchEndpoint hr = %2\r\n
0xb0001838 | %1 - UITaskHandler::ReplaceTextEndpoint hr = %2\r\n
0xb0001839 | %1 - UITaskHandler::Get Task State. StateSize[%2]. hr = %3\r\n
0xb000183a | %1 - UITaskHandler::Set Task State. StateSize[%2]. hr = %3\r\n
0xb000183b | %1 - UITaskHandler::OnObscurityChange[%2]. hr = %3\r\n
0xb000183c | %1 - UITaskHandler::OnLockScreenVisibilityChange[%2]. hr = %3\r\n
0xb000183d | %1 - UITaskHandler::OnSipVisibilityChange[%2]. hr = %3\r\n
0xb000183e | %1 - UITaskHandler::OnShowAnimationComplete\r\n
0xb000183f | %1 - UITaskHandler::Window.Visible property changed [%2]\r\n
0xb0001840 | %1 - FreezeHost event triggered\r\n
0xb0001841 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001842 | %1 - CancelTask TaskId=%2\r\n
0xb0001843 | %1 - OnHostPausing\r\n
0xb0001844 | %1 - OnHostPausing failed with hr = %2\r\n
0xb0001845 | %1 - OnHostPaused\r\n
0xb0001846 | %1 - OnHostPaused failed with hr = %2\r\n
0xb0001847 | %1 - FreezeHost event triggered\r\n
0xb0001848 | %1 - FreezeHostCallback failed with hr = %2\r\n
0xb0001849 | %1 - CancelTask received while executing in background\r\n
0xb000184a | %1 - CancelTask received. Ignoring since this is a valid transition only when running in background\r\n
0xb000184b | %1 - CancelTask hr = %2\r\n
0xb000184c | %1 - TPA entry: %2\\%3%4;\r\n
0xb000184d | %1 - Platform Assemblies List: %2\r\n
0xb000184e | %1 - ParseManifestFile HResult = %2\r\n
0xb000184f | %1 - NotifyError ! Unable to disable NI optimizations\r\n
0xb0001850 | %1 - NotifyError ! Unable to set the debugger wait env variable\r\n
0xb0001851 | %1 - TestTrustedPath: %2\r\n
0xb0001852 | %1 - TestAppPaths: %2\r\n
0xb0001853 | %1 - NotifyError ! Failed to set the test settings\r\n
0xb0001854 | %1 - GetAppPaths failed with hr = %2\r\n
0xb0001855 | %1 - NotifyError ! message = %2, source = %3\r\n
0xb0001856 | %1 - NotifyError ! hr=%2. message = %3\r\n
0xb0001857 | %1 - GetIsoStoreAvailableFreeSpace hr = %2\r\n
0xb0001858 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb0001859 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb000185a | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185b | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb000185c | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb000185d | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb000185e | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb000185f | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb0001860 | %1 - GetQualifiedMutexName returned:[%2]. AllowedMutexCount:[%3]\r\n\r\n
0xb0001861 | %1 - XcpHost::Start() failed with hr = %2\r\n
0xb0001862 | %1 - Shutting down the SL runtime...\r\n
0xb0001863 | %1 - Calling into XcpHost::Pausing %2\r\n
0xb0001864 | %1 - XcpHost::Pausing %2\r\n
0xb0001865 | %1 - Calling into XcpHost::Pause %2\r\n
0xb0001866 | %1 - XcpHost::Pause %2\r\n
0xb0001867 | %1 - Calling into XcpHost::Resume %2\r\n
0xb0001868 | %1 - XcpHost::Resume %2\r\n
0xb0001869 | %1 - Calling into XcpHost::Resumed %2\r\n
0xb000186a | %1 - XcpHost::Resumed %2\r\n
0xb000186b | %1 - XcpHost::CompleteTask called TaskID:[%2]\r\n
0xb000186c | %1 - CompleteTask called when XcpTask is null. This likely indicates CompleteTask getting called twice\r\n
0xb000186d | %1 - Error in OnApplicationStarted\r\n
0xb000186e | %1 - Error in OnApplicationConstructing\r\n
0xb000186f | %1 - LaunchSession hr = %2\r\n
0xb0001870 | %1 - LaunchChildTask hr = %2\r\n
0xb0001871 | %1 - Raising Task.OnLaunching\r\n
0xb0001872 | %1 - Raised Task.OnLaunching\r\n
0xb0001873 | %1 - Raising Task.OnPause. PauseReason[%2]\r\n
0xb0001874 | %1 - Raised Task.OnPause\r\n
0xb0001875 | %1 - Raising Task.OnResume. IsExecutionContextPreserved[%2]\r\n
0xb0001876 | %1 - Raised Task.OnResume\r\n
0xb0001877 | %1 - Raising Task.OnRunningInBackground\r\n
0xb0001878 | %1 - Raised Task.OnRunningInBackground\r\n
0xb0001879 | %1 - Raising Task.OnCancel\r\n
0xb000187a | %1 - Raised Task.OnCancel\r\n
0xb000187b | %1 - Raising Task.OnHostDehydarting\r\n
0xb000187c | %1 - Raised Task.OnHostDehydarting\r\n
0xb000187d | %1 - Raising Task.OnNavigateTo\r\n
0xb000187e | %1 - Raised Task.OnNavigateTo\r\n
0xb000187f | %1 - Raising Task.OnNavigateAway\r\n
0xb0001880 | %1 - Raised Task.OnNavigateAway\r\n
0xb0001881 | %1 - Raising Task.OnShow\r\n
0xb0001882 | %1 - Raised Task.OnShow\r\n
0xb0001883 | %1 - Raising Task.OnHide\r\n
0xb0001884 | %1 - Raised Task.OnHide\r\n
0xb0001885 | %1 - Raising Task.OnSystemKeyPressed\r\n
0xb0001886 | %1 - Raised Task.OnSystemKeyPressed\r\n
0xb0001887 | %1 - Raising Task.OnChildTaskReturned\r\n
0xb0001888 | %1 - Raised Task.OnChildTaskReturned\r\n
0xb0001889 | %1 - Raising Task.OnObscurityChange\r\n
0xb000188a | %1 - Raised Task.OnObscurityChange\r\n
0xb000188b | %1 - Raising Task.OnLockScreenVisibilityChange\r\n
0xb000188c | %1 - Raised Task.OnLockScreenVisibilityChange\r\n
0xb000188d | %1 - Raising Task.OnClosing\r\n
0xb000188e | %1 - Raised Task.OnClosing\r\n
0xb000188f | %1 - RegisterAppCallbacks hr = %2\r\n
0xb0001890 | %1 - RegisterTaskCallbacks hr = %2\r\n
0xb0001891 | %1 - TaskReadyToShow hr = %2\r\n
0xb0001892 | %1 - RequestCloseTask hr = %2\r\n
0xb0001893 | %1 - CompleteTask hr = %2\r\n
0xb0001894 | %1 - DestroyTaskCallbacks hr = %2\r\n
0xb0001895 | %1 - SetHostErrorCode hrHostError = %2, hr = %3\r\n
0xb0001896 | %1 - LaunchSession[%2] hr = %3\r\n
0xb0001897 | %1 - GetTaskState hr = %2\r\n
0xb0001898 | %1 - SetTaskState hr = %2\r\n
0xb0001899 | %1 - LaunchChildTask[%2] hr = %3\r\n
0xb000189a | %1 - GetTaskAppChromeHandle hr = %2\r\n
0xb000189b | %1 - SetTaskPauseOnLock hr = %2\r\n
0xb000189c | %1 - SetHostObscurity[%2] hr = %3\r\n
0xb000189d | %1 - Entering Modal state\r\n
0xb000189e | %1 - Exiting Modal state hr = %2\r\n
0xb000189f | %1 - NotifyError: message=%2, source=%3\r\n
0xb00018a0 | %1 - NotifyEvent XcpHostEvent_ApplicationStarted\r\n
0xb00018a1 | %1 - NotifyEvent XcpHostEvent_ApplicationStarting\r\n
0xb00018a2 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructing: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a3 | %1 - NotifyEvent XcpHostEvent_ApplicationConstructed: Assembly = %2, NotifyEvent Type = %3\r\n
0xb00018a4 | %1 - NotifyEvent XcpHostEvent_AssemblyLoading: Assembly = %2\r\n
0xb00018a5 | %1 - NotifyEvent XcpHostEvent_AssemblyLoaded: Assembly = %2\r\n
0xb00018a6 | %1 - NotifyEvent XcpHostEvent_SourceLoading: XAP = %2\r\n
0xb00018a7 | %1 - NotifyEvent XcpHostEvent_SourceLoaded: XAP = %2\r\n
0xb00018a8 | %1 - Raising Task.OnRefresh\r\n
0xb00018a9 | %1 - Raised Task.OnRefresh\r\n
0xb00018aa | %1 - UITaskHandler::RequestNavigateBack called TaskID:[%2]\r\n
0xb00018ab | %1 - UITaskHandler::RequestNavigateBack hr = %2\r\n
0xb00018ac | %1 - RequestNavigateBack hr = %2\r\n
0xb00018ad | %1 - UITaskHandler::SetFullScreen[%2] called TaskID:[%3]\r\n
0xb00018ae | %1 - UITaskHandler::SetFullScreen hr = %2\r\n
0xb00018af | %1 - SetTaskFullScreen hr = %2\r\n
0xb00018b0 | %1 - Raising Task.OnApplicationLayerChange\r\n
0xb00018b1 | %1 - Raised Task.OnApplicationLayerChange\r\n
0xb00018b2 | %1 - Raising Task.OnRequestOverlayStateChange. State=%2\r\n
0xb00018b3 | %1 - Raised Task.OnRequestOverlayStateChange\r\n
0xb00018b4 | %1 - ApplicationLayerChanged NewApplicationLayer=%2\r\n
0xb00018b5 | %1 - ApplicationLayerChange received before RuntimeHostTask is set\r\n
0xb00018b6 | %1 - AgTaskHandler::LaunchSession hr = %2\r\n
0xb00018b7 | %1 - AgTaskHandler::LaunchChildTask hr = %2\r\n
0xb00018b8 | %1 - GetSessionDisplayName. DisplayName=%2 hr = %3\r\n
0xb00018b9 | %1 - AgTaskHandler::ConnectionComplete received\r\n
0xb00018ba | %1 - AgTaskHandler::ConnectionComplete hr = %2\r\n
0xb00018bb | %1 - UITaskHandler::OnNavigationBarVisibilityChange[%2]. hr = %3\r\n
0xb00018bc | %1 - Raising Task.OnModernActivation\r\n
0xb00018bd | %1 - Raised Task.OnModernActivation\r\n
0xb00018be | %1 - UITaskHandler::LaunchModernChooser hr = %2\r\n
0xb00018bf | %1 - LaunchChildTask hr = %2\r\n
0xb00018c0 | %1 - LaunchModernChooser[%2] hr = %3\r\n
0xb00018c1 | %1 - TaskFirstPresentCompleted = %2\r\n
0xb00018c2 | %1 - UITaskHandler::FirstPresentCompleted called TaskID:[%2]\r\n
0xb00018c3 | %1 - UITaskHandler::FirstPresentCompleted hr = %2\r\n
0xb0001fa4 | AgHost - FrameworkView::Initialize HRESULT=%1\r\n
0xb0001fa5 | AgHost - FrameworkView::SetWindow HRESULT=%1\r\n
0xb0001fa6 | AgHost - FrameworkView::Load HRESULT=%1\r\n
0xb0001fa7 | AgHost - FrameworkView::Run HRESULT=%1\r\n
0xb0001fa8 | AgHost - FrameworkView::Uninitialize HRESULT=%1\r\n
0xb0001fa9 | AgHost - FrameworkView::OnActivated PreviousExecutionState=%1 ActivationKind=%2 HRESULT=%3\r\n
0xb0001faa | AgHost - FrameworkView::OnExiting HRESULT=%1\r\n
0xb0001fab | AgHost - FrameworkView::OnResuming HRESULT=%1\r\n
0xb0001fac | AgHost - FrameworkView::OnSuspending HRESULT=%1\r\n
0xb0001fae | AgHostSvcs - EmCancelTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001faf | AgHostSvcs - EmCreateTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb0 | AgHostSvcs - EmExitTaskHost HRESULT=%1\r\n
0xb0001fb1 | AgHostSvcs - EmPauseTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb2 | AgHostSvcs - EmResumeTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb3 | AgHostSvcs - EmSetTaskInstanceApplicationUri TaskID=%1 ApplicationUri=%2 HRESULT=%3\r\n
0xb0001fb4 | AgHostSvcs - EmSetTaskInstanceArguments TaskID=%1 HRESULT=%2\r\n
0xb0001fb5 | AgHostSvcs - EmSetTaskInstanceBackgroundTaskId TaskID=%1 BackgroundTaskID=%2 HRESULT=%3\r\n
0xb0001fb6 | AgHostSvcs - EmSetTaskInstanceNavigationPage TaskID=%1 NavigationPage=%2 HRESULT=%3\r\n
0xb0001fb7 | AgHostSvcs - EmStartTaskInstance TaskID=%1 HRESULT=%2\r\n
0xb0001fb8 | AgHostSvcs - TaskCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fb9 | AgHostSvcs - TaskPaused TaskID=%1 HRESULT=%2\r\n
0xb0001fba | AgHostSvcs - TaskRunning TaskID=%1 HRESULT=%2\r\n
0xb0001fbb | AgHostSvcs - TaskRunningInBackground TaskID=%1 HRESULT=%2\r\n
0xb0001fbc | AgHostSvcs - TaskRunningInForeground TaskID=%1 HRESULT=%2\r\n
0xb0001fbd | AgHostSvcs - EmWaitForTaskInstanceCompleted TaskID=%1 CompletionCode=%2 HRESULT=%3\r\n
0xb0001fbe | AgHostSvcs - OnModernContractActivation TaskID=%1 HRESULT=%2\r\n
0xb0002008 | EEC: GetExtendedExecutionBroker ProcessId=%1 HRESULT=%2\r\n
0xb0002009 | EEC: RegisterRevokedHandler ProcessId=%1 HRESULT=%2\r\n
0xb000200a | EEC: RequestExtendedExecution ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200b | EEC: ExtensionRevokedCallback ProcessId=%1 Reason=%2 HRESULT=%3\r\n
0xb000200c | EEC: CompleteExtendedExecution ProcessId=%1 HRESULT=%2\r\n
0xb000206c | ODB: LaunchTask - UserSid: %1 SessionId: %2 PackageFullName: %3 EntryPoint: %4 WorkItemId: %5 HRESULT: %6.\r\n
0xb000206d | ODB: CancelTask - UserSid: %1 SessionId: %2 WorkItemId: %3 RudeTerminate: %4 CancellationReason: %5 HRESULT: %6.\r\n
0xb000206e | ODB: BeforeTaskActivated - WorkItemId: %1 PsmKey: %2 HostJobType: %3 HRESULT: %4.\r\n
0xb000206f | ODB: TaskActivated - WorkItemId: %1 TaskInstanceId: %2 PsmKey: %3 HRESULT: %4.\r\n
0xb0002070 | ODB: TaskCompleted - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002071 | ODB: TaskCanceled - WorkItemId: %1 TaskInstanceId: %2 HRESULT: %3.\r\n
0xb0002072 | ODB: Timeout in WaitForWnfStateQuiescentTimeout.\r\n
0xb0002073 | ODB: CancelBackgroundTaskWithWnf WorkItemId: %1.\r\n
0xb0002710 | %1\r\n
0xb0002711 | %1: %2\r\n
0xb0002712 | *** ExecFailFast ***   %1\r\n
0xb000271a | PreInstallTaskPolicy: Activate task for User = %1 HRESULT = %2\r\n
0xb000271b | PreInstallTaskPolicy: BiActivate WorkItemId = %1 for user = %2, PackageFullName = %3, EntryPoint = %4, HRESULT = %5\r\n
0xb0010205 | BM: TryAcquireResourceSet returning HR='%4' PsmKey='%1' WorkItemId='%2;' CallbackId='%3' HostId='%5' ResourceSetId='%6'.\r\n
0xb0010206 | BM: TryAcquireHostResourceSet returning HR='%2' PsmKey='%1' HostId='%3' ResourceSetId='%4'.\r\n
0xd0000001 | Resumed\r\n
0xd0000002 | Quiescing\r\n
0xd0000003 | Quiesced\r\n
0xd0000004 | Frozen\r\n
0xd0000005 | Dehydrated\r\n
0xd0000006 | Terminated\r\n
0xd0000007 | Resumed\r\n
0xd0000008 | Suspending\r\n
0xd0000009 | Suspended\r\n
0xd000000a | Terminated\r\n
0xd000000b | NotBackground\r\n
0xd000000c | MixedHost\r\n
0xd000000d | PureHost\r\n
0xd000000e | SystemHost\r\n
0xd000000f | InvalidType\r\n
0xd0000010 | Permitted\r\n
0xd0000011 | Buffered\r\n
0xd0000012 | Dropped\r\n
0xd0000013 | InvalidType\r\n
0xd0000014 | Invalid\r\n
0xd0000015 | ForegroundApp\r\n
0xd0000016 | Cbe\r\n
0xd0000017 | ForegroundAgent\r\n
0xd0000018 | GbaPeriodic\r\n
0xd0000019 | GbaIdle\r\n
0xd000001a | BackgroundAudio\r\n
0xd000001b | BackgroundWorker\r\n
0xd000001c | Voip\r\n
0xd000001d | Oem\r\n
0xd000001e | Invalid\r\n
0xd000001f | Started\r\n
0xd0000020 | Paused\r\n
0xd0000021 | Resumed\r\n
0xd0000022 | MovedToBackground\r\n
0xd0000023 | RunUnderLock\r\n
0xd0000024 | Invalid\r\n
0xd0000025 | OK\r\n
0xd0000026 | Abort\r\n
0xd0000027 | Unexpected\r\n
0xd0000028 | ExceededRuntime\r\n
0xd0000029 | ResourcesSeized\r\n
0xd000002a | Paused\r\n
0xd000002b | Resumed\r\n
0xd000002c | ScreenLock\r\n
0xd000002d | ScreenUnlocked\r\n
0xd000002e | MovedToBackground\r\n
0xd000002f | CbeExitTimeout\r\n
0xd0000030 | CbeExitBatterySaver\r\n
0xd0000031 | CbeExitParallelAgentPolicy\r\n
0xd0000032 | CbeExitResourcesUnavailable\r\n
0xd0000033 | CbeExitControlPanel\r\n
0xd0000034 | CbeExitBandwidthSavings\r\n
0xd0000035 | HeadlessHost\r\n
0xd0000036 | TaskHost\r\n
0xd0000037 | XcpHost\r\n
0xd0000038 | TaskHostSvcs\r\n
0xd0000039 | TaskHostUnitTests\r\n
0xd000003a | HOST_CREATED\r\n
0xd000003b | HOST_INITIALIZED\r\n
0xd000003c | HOST_RUNNING\r\n
0xd000003d | STARTING_TASK\r\n
0xd000003e | REHYDRATING_TASK\r\n
0xd000003f | HOST_READY\r\n
0xd0000040 | HOST_PAUSING\r\n
0xd0000041 | PAUSING_TASK\r\n
0xd0000042 | PAUSED_TASK\r\n
0xd0000043 | HOST_PAUSED\r\n
0xd0000044 | RESUMING_TASK\r\n
0xd0000045 | HOST_GOING_IN_BACKGROUND\r\n
0xd0000046 | TASK_GOING_IN_BACKGROUND\r\n
0xd0000047 | HOST_IN_BACKGROUND\r\n
0xd0000048 | TASK_GOING_IN_FOREGROUND\r\n
0xd0000049 | GRACEFULLY_DEHYDRATING_HOST\r\n
0xd000004a | HOST_VISIBLE\r\n
0xd000004b | HOST_HIDDEN\r\n
0xd000004c | HOST_FROZEN\r\n
0xd000004d | HOST_THAWED\r\n
0xd000004e | HOST_EXITING\r\n
0xd000004f | HOST_ERROR\r\n
0xd0000050 | Direction_Forward\r\n
0xd0000051 | Direction_Backward\r\n
0xd0000052 | Direction_ForceSize\r\n
0xd0000053 | Resumed\r\n
0xd0000054 | Pausing\r\n
0xd0000055 | Paused\r\n
0xd0000056 | Dehydrated\r\n
0xd0000057 | Completed\r\n
0xd0000058 | none\r\n
0xd0000059 | launch\r\n
0xd000005a | debug\r\n
0xd000005b | task completion\r\n
0xd000005c | dependency\r\n
0xd000005d | multi-view\r\n
0xd000005e | Waiting\r\n
0xd000005f | CompletedWithResult\r\n
0xd0000060 | CompletedWithNoResult\r\n
0xd0000061 | Foreground\r\n
0xd0000062 | Lock\r\n
0xd0000063 | Overlay\r\n
0xd0000064 | ModernForeground\r\n
0xd0000065 | Pausing\r\n
0xd0000066 | PausingLowPri\r\n
0xd0000067 | Paused\r\n
0xd0000068 | PausedHighPri\r\n
0xd0000069 | PausedDNK\r\n
0xd000006a | Frozen\r\n
0xd000006b | FrozenHighPri\r\n
0xd000006c | FrozenDNK\r\n
0xd000006d | FrozenDNCS\r\n
0xd000006e | LockScreen\r\n
0xd000006f | Overlay\r\n
0xd0000070 | 11\r\n
0xd0000071 | CalendarAsChild\r\n
0xd0000072 | VideoTranscode\r\n
0xd0000073 | CBE\r\n
0xd0000074 | GenericExtendedExecution\r\n
0xd0000075 | ModernForegroundExtended\r\n
0xd0000076 | TaskCompletionHighPriority\r\n
0xd0000077 | ModernForegroundLarge\r\n
0xd0000078 | ShellCustom1\r\n
0xd0000079 | ShellCustom2\r\n
0xd000007a | ShellCustom3\r\n
0xd000007b | ShellCustom4\r\n
0xd000007c | Composer\r\n
0xd000007d | DebugModeForeground\r\n
0xd000007e | ComponentTarget\r\n
0xd000007f | PiP\r\n
0xd0000080 | Balloon\r\n
0xd0000081 | Invalid\r\n
0xd0000082 | Unevaluated\r\n
0xd0000083 | EvaluationPending\r\n
0xd0000084 | Evaluated\r\n
0xd0000085 | BACKGROUND_ACCESS_USER_STATE_ALLOWED\r\n
0xd0000086 | BACKGROUND_ACCESS_USER_STATE_DISABLED\r\n
0xd0000087 | BACKGROUND_ACCESS_USER_STATE_LOCKED_BY_DEVICE_MANAGEMENT\r\n
0xd0000088 | BACKGROUND_ACCESS_STATE_DEFAULT\r\n
0xd0000089 | BACKGROUND_ACCESS_STATE_DISABLED\r\n
0xd000008a | BACKGROUND_ACCESS_STATE_ALWAYS_ALLOWED\r\n
0xd000008b | BACKGROUND_ACCESS_STATE_LOCKED_BY_DEVICE_MANAGEMENT\r\n
0xd000008c | BACKGROUND_ACCESS_STATE_NCB_ENABLED\r\n
0xd000008d | BACKGROUND_ACCESS_STATE_DISABLED_BY_SYSTEM\r\n
0xd000008e | BACKGROUND_ACCESS_STATE_DISABLED_BY_USER\r\n
0xd000008f | BACKGROUND_ACCESS_STATE_HIGH_PRIORITY_HOST\r\n
0xd0000090 | BACKGROUND_ACCESS_STATE_UNLIMITED_LIFETIME\r\n
0xd0000091 | BACKGROUND_ACCESS_STATE_SLEEP_ALWAYS_ALLOWED\r\n
0xd0000092 | BACKGROUND_ACCESS_STATE_SLEEP_DISABLED\r\n
0xd0000093 | BACKGROUND_ACCESS_STATE_SLEEP_DISABLED_BY_USER\r\n
0xd0000094 | BACKGROUND_ACCESS_STATE_SLEEP_DISABLED_BY_SYSTEM\r\n
