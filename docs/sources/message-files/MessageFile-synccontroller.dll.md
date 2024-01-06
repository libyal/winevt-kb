## synccontroller.dll

Path: %SystemRoot%\System32\SyncController.dll

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000003 | State\r\n
0x10000025 | CommsService\r\n
0x10000027 | Warning\r\n
0x10000028 | StateTransition\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | Error: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: %1 Location: %2 Line Number: %3\r\n
0xb0000065 | SyncController:[Consistency] [%1] Registry key for the default live partner is invalid, but will not be deleted.\r\n
0xb0000066 | SyncController:[Consistency] [%1] Registry key for this partner is being deleted because it's invalid.\r\n
0xb0000067 | SyncController:[Consistency] Default Store is invalid, but will not be deleted. There were '%1' stores found.\r\n
0xb0000068 | SyncController:[Consistency] [%1:%2:%3] Store being deleted because it's invalid. There were '%4' stores found.\r\n
0xb0000069 | SyncController:[Consistency] [%1] Registry key for this partner is invalid, the reason is '%2'.\r\n
0xb000006a | SyncController:[Consistency] [%1:%2:%3] Store is invalid, the reason is '%4'.\r\n
0xb0000070 | SimContactsSync [%1:%2] Unexpected Workitem\r\n
0xb0000071 | SimContactsSync [%1:%2] Failed to initialize store\r\n
0xb0000072 | SimContactsSync [%1:%2] Failed add to work item to queue\r\n
0xb0000074 | SimContactsSync [%1:%2] Failed to delete store\r\n
0xb0000075 | SimContactsSync [%1:%2] Failed to do Post boot sync\r\n
0xb0000076 | SimContactsSync [%1:%2] Failed to OnStoreChange sync\r\n
0xb0000078 | SimContactsSync [%1:%2] Failed to OnExportDone sync\r\n
0xb0000079 | SimContactsSync [%1:%2] Failed to set store and contacts access\r\n
0xb000007a | SimContactsSync [%1:%2] Received Phonebook Ready state change. Ready state: %3\r\n
0xb000007b | SimContactsSync [%1:%2] Run (pending work item)\r\n
0xb000007c | SimContactsSync [%1:%2] Adding work item type %3\r\n
0xb000007d | SimContactsSync [%1:%2] Executing work item type %3\r\n
0xb000007e | SimContactsSync [%1:%2] Store change event\r\n
0xb0000080 | SimContactsSync [%1:%2] Export done event\r\n
0xb0000081 | SimContactsSync: Service loaded. Enabled = %1\r\n
0xb0000084 | SimContactsSync [%1:%2] Client request to shut down sync service\r\n
0xb0000085 | SimContactsSync [%1:%2]: Request to cancel setting Fdn Pin2 work, but cancel isn't supported\r\n
0xb0000086 | SimContactsSync [%1:%2]: Request to cancel shutting down Fdn sync work, but cancel isn't supported\r\n
0xb0000087 | SimContactsSync [%1:%2] Found %3 slots\r\n
0xb0000088 | SimContactsSync [%1:%2] CellularApiHelper discovery state updated to: %3\r\n
0xb0000089 | SimContactsSync [%1:%2] Stop requested, releasing phonebook and cellular API helper.\r\n
0xb000008a | SimContactsSync [%1:%2] Checked for a sim swap, and the result is: %3\r\n
0xb000008b | SimSyncServiceWork: Found %1 slots\r\n
0xb000008c | SimContactsSync [%1:%2]: Request to cancel starting Fdn sync work, but cancel isn't supported\r\n
0xb000008d | SimContactsSync [%1:%2]: Responding to a request to start FDN sync\r\n
0xb000008e | SimContactsSync [%1:%2]: Responding to a request to shutdown FDN sync\r\n
0xb000008f | SimContactsSync [%1:%2]: Responding to a request to set the FDN password\r\n
0xb0000090 | SimContactsSync [%1:%2]: Found an updated slot name, setting the store name to: %3\r\n
0xb0000091 | SimSyncServiceWork: Initializing with SIMOM instance %1\r\n
0xb0000092 | SimSyncServiceWork: Discovery state changed to %1, slots ready = %2\r\n
0xb0000093 | SimSyncServiceWork: Requested to enable slot %1\r\n
0xb0000094 | SimSyncServiceWork: Not enabling slot because handlers are not yet initialized\r\n
0xb0000095 | SimSyncServiceWork: EnableSlot: Handler found and already running, evaluating reset\r\n
0xb0000096 | SimSyncServiceWork: Found a handler for this slot, but it is aborted so we will delete and recreate\r\n
0xb0000097 | SimSyncServiceWork: Handler created and stored for slot %1\r\n
0xb0000098 | SimSyncServiceWork: Tearing down. Will stop all handlers and unadvise from SIMOM\r\n
0xb0000099 | SimSyncServiceWork: Not rescheduling because slots and handlers aren't initialized\r\n
0xb000009a | SimSyncServiceWork: Work pending = %1\r\n
0xb000009b | SimSyncServiceWork: Rescheduling - Slot %1 has a handler running\r\n
0xb000009c | SimSyncServiceWork: Rescheduling - Slot %1 has work pending\r\n
0xb000009d | SimSyncServiceWork: Rescheduling - No handlers running, so shutting down\r\n
0xb000009e | SimSyncServiceWork: ExecuteWork\r\n
0xb000009f | SimSyncServiceWork: ExecuteWork - Slots ready\r\n
0xb00000a0 | SimSyncServiceWork: ExecuteWork - Handlers not yet created, initializing for %1 slots\r\n
0xb00000a1 | SimSyncServiceWork: ExecuteWork - Created and stored handler for slot %1\r\n
0xb00000a2 | SimSyncServiceWork: ExecuteWork - Handlers already initialized\r\n
0xb00000a3 | SimSyncServiceWork: ExecuteWork - Running handler for slot %1\r\n
0xb00000a4 | SimSyncServiceWork: ExecuteWork - Handler for slot %1 is aborted\r\n
0xb00000a5 | SimSyncServiceWork: ExecuteWork - Not executing, slots aren't ready yet\r\n
0xb00000a6 | SimSyncServiceWork: Cancelling all handlers\r\n
0xb00000a7 | SimSyncServiceWork: Getting singleton instance\r\n
0xb00000a8 | SimSyncServiceWork: Instance does not exist, creating...\r\n
0xb00000a9 | SimSyncServiceWork: Releasing singleton instance\r\n
0xb00000aa | SimSyncServiceActivityFactory: Factory initialized, SIMOM instance = %1\r\n
0xb00000ab | SimSyncServiceActivityFactory: Service unloaded, releasing service work singletons and SIMOM\r\n
0xb00000ac | SimSyncServiceActivityFactory: Requested Fdn sync for slot %1. Singleton is NOT valid so creating it.\r\n
0xb00000ad | SimSyncServiceActivityFactory: Requested Fdn sync for slot %1. Singleton is running so scheduling a trigger job.\r\n
0xb00000ae | SimContactsSync [%1:%2]: Feature is not supported, so deleting store and aborting\r\n
0xb00000af | SimContactsSync [%1:%2]: Didn't find a slot for our given index, so deleting store and aborting\r\n
0xb00000b0 | SimContactsSync [%1:%2]: App state is %3\r\n
0xb00000b1 | SimContactsSync [%1:%2]: Slot state is %3\r\n
0xb00000b2 | SimContactsSync [%1:%2]: Looking for an app change, checking against current app id: %3\r\n
0xb00000b3 | SimContactsSync [%1:%2]: Found our application in the list\r\n
0xb00000b4 | SimContactsSync [%1:%2]: Current app id: %3, New app id: %4, switch = %5\r\n
0xb00000b5 | SimContactsSync [%1:%2]: Resetting phonebook app, found = %3, switch = %4\r\n
0xb00000b6 | SimContactsSync [%1:%2]: Processing SIM state change\r\n
0xb00000b7 | SimContactsSync [%1:%2]: Enumerating SIM apps: %3\r\n
0xb00000b8 | SimContactsSync [%1:%2]: Looking for an imsi change, current imsi: %3\r\n
0xb00000b9 | SimContactsSync [%1:%2]: Current imsi: %3, new Imsi: %4, Changed: %5\r\n
0xb00000ba | SimContactsSync [%1:%2]: Resetting state, type = %3\r\n
0xb00000bb | SimContactsSync [%1:%2]: Resetting handler flags\r\n
0xb00000bc | SimContactsSync [%1:%2]: Marking handler to evaluate reset.\r\n
0xb00000bd | SimContactsSync [%1:%2]: Sim apps are no longer ready, so ignoring request to reset/load phonebook.\r\n
0xb00000be | SimContactsSync [%1:%2]: EvaluateReset: IMSI and App have not changed, but the feature is now disabled so resetting state.\r\n
0xb00000bf | Sync WNF event: %1\r\n
0xb00000c1 | Sync WNF event: %1 - %2\r\n
0xb00000c9 | Receive WNF event; current mode: %1, current value: %2\r\n
0xb00001f4 | AccountSyncController: Starting scheduled SyncExecutor for account %1, engine %2.\r\n
0xb00001f5 | AccountSyncController: Starting interactive SyncExecutor for account %1, engine %2.\r\n
0xb00001f6 | AccountSyncController: Starting AUTDExecutor for account %1, engine %2.\r\n
0xb00001f7 | AccountSyncController: Finished SyncExecutor work for account %1 with hr=%2, retry level %3, can start AUTD %4, queue empty %5, saver mode %6, engine %7.\r\n
0xb00001f8 | AccountSyncController: Finished AUTDExecutor work for account %1 with hr %2, can start AUTD %3, queue empty %4, saver mode %5, engine %6.\r\n
0xb00001f9 | AccountSyncController: Adding new controller with id %1.\r\n
0xb00001fa | AccountSyncController: Deleting sync controller with id %1.\r\n
0xb00001fb | Handle schedule period changed from %2 min to %3 min for account %1 and engine %4.\r\n
0xb00001fc | Handle content/filter change for account %1 and engine %2.\r\n
0xb00001fd | AccountSyncController: Added new AccountSyncController for account %1.\r\n
0xb00001fe | Started DownloadEmailBodyWork for account %1.\r\n
0xb00001ff | Finished DownloadEmailBodyWork for account %1.\r\n
0xb0000200 | Started AddMeetingResponseWork for account %1.\r\n
0xb0000201 | Finished AddMeetingResponseWork for account %1 with HRESULT %2\r\n
0xb0000204 | Started DownloadEmailAttachmentWork for account %1.\r\n
0xb0000205 | Finished DownloadEmailAttachmentWork for account %1.\r\n
0xb0000206 | Started DownloadSharePointDocumentWork for account %1.\r\n
0xb0000207 | Finished DownloadSharePointDocumentWork for account %1.\r\n
0xb0000208 | Started EmptyEmailFolderWork for account %1.\r\n
0xb0000209 | Finished EmptyEmailFolderWork for account %1.\r\n
0xb000020a | Started GalSearchWork for account %1.\r\n
0xb000020b | Finished GalSearchWork for account %1.\r\n
0xb000020c | Started GetOofWork for account %1.\r\n
0xb000020d | Finished GetOofWork for account %1.\r\n
0xb000020e | Started MailboxSearchWork for account %1.\r\n
0xb000020f | Finished MailboxSearchWork for account %1.\r\n
0xb0000210 | Started PurgeDeletedAccountsWork.\r\n
0xb0000211 | Finished PurgeDeletedAccountsWork.\r\n
0xb0000212 | Started SetFolderSyncStateWork for account %1.\r\n
0xb0000213 | Finished SetFolderSyncStateWork for account %1.\r\n
0xb0000214 | Started SetLivePasswordWork.\r\n
0xb0000215 | Finished SetLivePasswordWork.\r\n
0xb0000216 | Started UpdateContentTypesWork for account %1.\r\n
0xb0000217 | Finished UpdateContentTypesWork for account %1.\r\n
0xb0000218 | Started SetOofWork for account %1.\r\n
0xb0000219 | Finished SetOofWork for account %1.\r\n
0xb000021c | Started FlushAccountSettingsWork for account %1.\r\n
0xb000021d | Finished FlushAccountSettingsWork for account %1.\r\n
0xb000021e | Started PurgeDeletedAccountWork for account %1.\r\n
0xb000021f | Finished PurgeDeletedAccountWork for account %1.\r\n
0xb0000220 | AccountSyncController: Adding new child sync controller with id %1 and engine id %2.\r\n
0xb0000226 | AccountSyncController: Starting ScheduleManager work for account %1, engine %2.\r\n
0xb0000227 | Upgrading account %1 from version %2 to the current version %3.\r\n
0xb0000228 | Ignoring account %1 because its version (%2) doesn't match the current version (%3).\r\n
0xb0000229 | Detected a previous failure in Execute Activity Step for account %1, delaying next run.\r\n
0xb000022b | Account %1 setting schedule trigger requirement %2.\r\n
0xb000022c | Account %1 exiting delay and resetting successive empty sync count to zero.\r\n
0xb0000231 | Aggregate controller has new merged result: engine %1, result %2.\r\n
0xb0000232 | Handle server change for account %1 and engine %2.\r\n
0xb0000233 | Handle login info change for account %1 and engine %2.\r\n
0xb000023a | Executing ScheduleManager work of type %3 for account %1, engine %2.\r\n
0xb000023b | Executing Post OOBE notifications work. Cancelled = %1\r\n
0xb00002bd | Cred Vault: DeletePwd Called. Caller: _PurgeActiveSyncAccount, Partner %1\r\n
0xb00002be | Cred Vault: DeletePwd Called. Caller: ActiveSyncServer_DeletePassword, Partner %1\r\n
0xb0000321 | Setting delayed value of conversation sync enabled to %1\r\n
0xb0000322 | Setting the value of conversation sync if changed - Desired = %1, Current = %2\r\n
0xb0000329 | Schedule for account %1 triggered when the screen was on and the schedule was set to trigger for screen on.\r\n
0xb000032a | Schedule %1 for account %2 triggered with period %3, base period %4, failure count %5, trigger flags %6, engine %7.\r\n
0xb000032b | TokenBucket: Account %1 is throttling for %2 minutes.\r\n
0xb000032c | TokenBucket: Account %1 successfully retrieved a token.\r\n
0xb000032d | TokenBucket: Account %1 was not throttled because the screen was on.\r\n
0xb0000384 | NotificationUtils: Initializing notification utils. IsOobeDone = %1\r\n
0xb0000385 | NotificationUtils: Cleanup.\r\n
0xb0000386 | NotificationUtils: _PostAttentionRequiredNotification(). Account = %1, Toast already sent = %2.\r\n
0xb0000387 | NotificationUtils: _RemoveAttentionRequiredNotification(). Account = %1\r\n
0xd0000001 | none\r\n
0xd0000002 | battery saver on\r\n
0xd0000003 | data saver on\r\n
0xd0000004 | both savers on\r\n
0xd0000005 | batterysaver\r\n
0xd0000006 | datasaver\r\n
0xd0000007 | internet mail sync engine\r\n
0xd0000008 | EAS sync engine\r\n
0xd0000009 | card dav sync engine\r\n
0xd000000a | caldav sync engine\r\n
0xd000000b | smtp sync engine\r\n
0xd000000c | none\r\n
0xd000000d | exit backoff mode\r\n
0xd000000e | sync\r\n
0xd000000f | exit backoff and sync\r\n
0xd0000010 | reset empty sync count\r\n
0xd0000011 | exit backoff and reset empty sync count\r\n
0xd0000012 | remove alternative trigger\r\n
0xd0000013 | remove alternative trigger and sync\r\n
0xd0000014 | schedule changed\r\n
0xd0000015 | saver mode changed\r\n
0xd0000016 | exit backoff mode\r\n
0xd0000017 | remove alternative trigger\r\n
0xd0000018 | Unknown\r\n
0xd0000019 | Active\r\n
0xd000001a | Unlocked\r\n
0xd000001b | PinLocked\r\n
0xd000001c | PukBlocked\r\n
0xd000001d | Disabled\r\n
0xd000001e | Unknown\r\n
0xd000001f | NoSim\r\n
0xd0000020 | InvalidSim\r\n
0xd0000021 | ValidSim\r\n
0xd0000022 | NonSimSwap\r\n
0xd0000023 | SimSwap\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000003 | State\r\n
0x10000025 | CommsService\r\n
0x10000027 | Warning\r\n
0x10000028 | StateTransition\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | Error: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: %1 Location: %2 Line Number: %3\r\n
0xb0000065 | SyncController:[Consistency] [%1] Registry key for the default live partner is invalid, but will not be deleted.\r\n
0xb0000066 | SyncController:[Consistency] [%1] Registry key for this partner is being deleted because it's invalid.\r\n
0xb0000067 | SyncController:[Consistency] Default Store is invalid, but will not be deleted. There were '%1' stores found.\r\n
0xb0000068 | SyncController:[Consistency] [%1:%2:%3] Store being deleted because it's invalid. There were '%4' stores found.\r\n
0xb0000069 | SyncController:[Consistency] [%1] Registry key for this partner is invalid, the reason is '%2'.\r\n
0xb000006a | SyncController:[Consistency] [%1:%2:%3] Store is invalid, the reason is '%4'.\r\n
0xb0000070 | SimContactsSync [%1:%2] Unexpected Workitem\r\n
0xb0000071 | SimContactsSync [%1:%2] Failed to initialize store\r\n
0xb0000072 | SimContactsSync [%1:%2] Failed add to work item to queue\r\n
0xb0000074 | SimContactsSync [%1:%2] Failed to delete store\r\n
0xb0000075 | SimContactsSync [%1:%2] Failed to do Post boot sync\r\n
0xb0000076 | SimContactsSync [%1:%2] Failed to OnStoreChange sync\r\n
0xb0000078 | SimContactsSync [%1:%2] Failed to OnExportDone sync\r\n
0xb0000079 | SimContactsSync [%1:%2] Failed to set store and contacts access\r\n
0xb000007a | SimContactsSync [%1:%2] Received Phonebook Ready state change. Ready state: %3\r\n
0xb000007b | SimContactsSync [%1:%2] Run (pending work item)\r\n
0xb000007c | SimContactsSync [%1:%2] Adding work item type %3\r\n
0xb000007d | SimContactsSync [%1:%2] Executing work item type %3\r\n
0xb000007e | SimContactsSync [%1:%2] Store change event\r\n
0xb0000080 | SimContactsSync [%1:%2] Export done event\r\n
0xb0000081 | SimContactsSync: Service loaded. Enabled = %1\r\n
0xb0000084 | SimContactsSync [%1:%2] Client request to shut down sync service\r\n
0xb0000085 | SimContactsSync [%1:%2]: Request to cancel setting Fdn Pin2 work, but cancel isn't supported\r\n
0xb0000086 | SimContactsSync [%1:%2]: Request to cancel shutting down Fdn sync work, but cancel isn't supported\r\n
0xb0000087 | SimContactsSync [%1:%2] Found %3 slots\r\n
0xb0000088 | SimContactsSync [%1:%2] CellularApiHelper discovery state updated to: %3\r\n
0xb0000089 | SimContactsSync [%1:%2] Stop requested, releasing phonebook and cellular API helper.\r\n
0xb000008a | SimContactsSync [%1:%2] Checked for a sim swap, and the result is: %3\r\n
0xb000008b | SimSyncServiceWork: Found %1 slots\r\n
0xb000008c | SimContactsSync [%1:%2]: Request to cancel starting Fdn sync work, but cancel isn't supported\r\n
0xb000008d | SimContactsSync [%1:%2]: Responding to a request to start FDN sync\r\n
0xb000008e | SimContactsSync [%1:%2]: Responding to a request to shutdown FDN sync\r\n
0xb000008f | SimContactsSync [%1:%2]: Responding to a request to set the FDN password\r\n
0xb0000090 | SimContactsSync [%1:%2]: Found an updated slot name, setting the store name to: %3\r\n
0xb0000091 | SimSyncServiceWork: Initializing with SIMOM instance %1\r\n
0xb0000092 | SimSyncServiceWork: Discovery state changed to %1, slots ready = %2\r\n
0xb0000093 | SimSyncServiceWork: Requested to enable slot %1\r\n
0xb0000094 | SimSyncServiceWork: Not enabling slot because handlers are not yet initialized\r\n
0xb0000095 | SimSyncServiceWork: EnableSlot: Handler found and already running, evaluating reset\r\n
0xb0000096 | SimSyncServiceWork: Found a handler for this slot, but it is aborted so we will delete and recreate\r\n
0xb0000097 | SimSyncServiceWork: Handler created and stored for slot %1\r\n
0xb0000098 | SimSyncServiceWork: Tearing down. Will stop all handlers and unadvise from SIMOM\r\n
0xb0000099 | SimSyncServiceWork: Not rescheduling because slots and handlers aren't initialized\r\n
0xb000009a | SimSyncServiceWork: Work pending = %1\r\n
0xb000009b | SimSyncServiceWork: Rescheduling - Slot %1 has a handler running\r\n
0xb000009c | SimSyncServiceWork: Rescheduling - Slot %1 has work pending\r\n
0xb000009d | SimSyncServiceWork: Rescheduling - No handlers running, so shutting down\r\n
0xb000009e | SimSyncServiceWork: ExecuteWork\r\n
0xb000009f | SimSyncServiceWork: ExecuteWork - Slots ready\r\n
0xb00000a0 | SimSyncServiceWork: ExecuteWork - Handlers not yet created, initializing for %1 slots\r\n
0xb00000a1 | SimSyncServiceWork: ExecuteWork - Created and stored handler for slot %1\r\n
0xb00000a2 | SimSyncServiceWork: ExecuteWork - Handlers already initialized\r\n
0xb00000a3 | SimSyncServiceWork: ExecuteWork - Running handler for slot %1\r\n
0xb00000a4 | SimSyncServiceWork: ExecuteWork - Handler for slot %1 is aborted\r\n
0xb00000a5 | SimSyncServiceWork: ExecuteWork - Not executing, slots aren't ready yet\r\n
0xb00000a6 | SimSyncServiceWork: Cancelling all handlers\r\n
0xb00000a7 | SimSyncServiceWork: Getting singleton instance\r\n
0xb00000a8 | SimSyncServiceWork: Instance does not exist, creating...\r\n
0xb00000a9 | SimSyncServiceWork: Releasing singleton instance\r\n
0xb00000aa | SimSyncServiceActivityFactory: Factory initialized, SIMOM instance = %1\r\n
0xb00000ab | SimSyncServiceActivityFactory: Service unloaded, releasing service work singletons and SIMOM\r\n
0xb00000ac | SimSyncServiceActivityFactory: Requested Fdn sync for slot %1. Singleton is NOT valid so creating it.\r\n
0xb00000ad | SimSyncServiceActivityFactory: Requested Fdn sync for slot %1. Singleton is running so scheduling a trigger job.\r\n
0xb00000ae | SimContactsSync [%1:%2]: Feature is not supported, so deleting store and aborting\r\n
0xb00000af | SimContactsSync [%1:%2]: Didn't find a slot for our given index, so deleting store and aborting\r\n
0xb00000b0 | SimContactsSync [%1:%2]: App state is %3\r\n
0xb00000b1 | SimContactsSync [%1:%2]: Slot state is %3\r\n
0xb00000b2 | SimContactsSync [%1:%2]: Looking for an app change, checking against current app id: %3\r\n
0xb00000b3 | SimContactsSync [%1:%2]: Found our application in the list\r\n
0xb00000b4 | SimContactsSync [%1:%2]: Current app id: %3, New app id: %4, switch = %5\r\n
0xb00000b5 | SimContactsSync [%1:%2]: Resetting phonebook app, found = %3, switch = %4\r\n
0xb00000b6 | SimContactsSync [%1:%2]: Processing SIM state change\r\n
0xb00000b7 | SimContactsSync [%1:%2]: Enumerating SIM apps: %3\r\n
0xb00000b8 | SimContactsSync [%1:%2]: Looking for an imsi change, current imsi: %3\r\n
0xb00000b9 | SimContactsSync [%1:%2]: Current imsi: %3, new Imsi: %4, Changed: %5\r\n
0xb00000ba | SimContactsSync [%1:%2]: Resetting state, type = %3\r\n
0xb00000bb | SimContactsSync [%1:%2]: Resetting handler flags\r\n
0xb00000bc | SimContactsSync [%1:%2]: Marking handler to evaluate reset.\r\n
0xb00000bd | SimContactsSync [%1:%2]: Sim apps are no longer ready, so ignoring request to reset/load phonebook.\r\n
0xb00000be | SimContactsSync [%1:%2]: EvaluateReset: IMSI and App have not changed, but the feature is now disabled so resetting state.\r\n
0xb00000bf | Sync WNF event: %1\r\n
0xb00000c1 | Sync WNF event: %1 - %2\r\n
0xb00000c3 | Sync WNF event %1 not found.\r\n
0xb00000c4 | Notified golden account existence: %1.\r\n
0xb00000c9 | Receive WNF event; current mode: %1, current value: %2\r\n
0xb00001f4 | AccountSyncController: Starting scheduled SyncExecutor for account %1, engine %2.\r\n
0xb00001f5 | AccountSyncController: Starting interactive SyncExecutor for account %1, engine %2.\r\n
0xb00001f6 | AccountSyncController: Starting AUTDExecutor for account %1, engine %2.\r\n
0xb00001f7 | AccountSyncController: Finished SyncExecutor work for account %1 with hr=%2, retry level %3, can start AUTD %4, queue empty %5, saver mode %6, engine %7.\r\n
0xb00001f8 | AccountSyncController: Finished AUTDExecutor work for account %1 with hr %2, can start AUTD %3, queue empty %4, saver mode %5, engine %6.\r\n
0xb00001f9 | AccountSyncController: Adding new controller with id %1.\r\n
0xb00001fa | AccountSyncController: Deleting sync controller with id %1.\r\n
0xb00001fb | Handle schedule period changed from %2 min to %3 min for account %1 and engine %4.\r\n
0xb00001fc | Handle content/filter change for account %1 and engine %2.\r\n
0xb00001fd | AccountSyncController: Added new AccountSyncController for account %1.\r\n
0xb00001fe | Started DownloadEmailBodyWork for account %1.\r\n
0xb00001ff | Finished DownloadEmailBodyWork for account %1.\r\n
0xb0000200 | Started AddMeetingResponseWork for account %1.\r\n
0xb0000201 | Finished AddMeetingResponseWork for account %1 with HRESULT %2\r\n
0xb0000204 | Started DownloadEmailAttachmentWork for account %1.\r\n
0xb0000205 | Finished DownloadEmailAttachmentWork for account %1.\r\n
0xb0000206 | Started DownloadSharePointDocumentWork for account %1.\r\n
0xb0000207 | Finished DownloadSharePointDocumentWork for account %1.\r\n
0xb0000208 | Started EmptyEmailFolderWork for account %1.\r\n
0xb0000209 | Finished EmptyEmailFolderWork for account %1.\r\n
0xb000020a | Started GalSearchWork for account %1.\r\n
0xb000020b | Finished GalSearchWork for account %1.\r\n
0xb000020c | Started GetOofWork for account %1.\r\n
0xb000020d | Finished GetOofWork for account %1.\r\n
0xb000020e | Started MailboxSearchWork for account %1.\r\n
0xb000020f | Finished MailboxSearchWork for account %1.\r\n
0xb0000210 | Started PurgeDeletedAccountsWork.\r\n
0xb0000211 | Finished PurgeDeletedAccountsWork.\r\n
0xb0000212 | Started SetFolderSyncStateWork for account %1.\r\n
0xb0000213 | Finished SetFolderSyncStateWork for account %1.\r\n
0xb0000214 | Started SetLivePasswordWork.\r\n
0xb0000215 | Finished SetLivePasswordWork.\r\n
0xb0000216 | Started UpdateContentTypesWork for account %1.\r\n
0xb0000217 | Finished UpdateContentTypesWork for account %1.\r\n
0xb0000218 | Started SetOofWork for account %1.\r\n
0xb0000219 | Finished SetOofWork for account %1.\r\n
0xb000021c | Started FlushAccountSettingsWork for account %1.\r\n
0xb000021d | Finished FlushAccountSettingsWork for account %1.\r\n
0xb000021e | Started PurgeDeletedAccountWork for account %1.\r\n
0xb000021f | Finished PurgeDeletedAccountWork for account %1.\r\n
0xb0000220 | AccountSyncController: Adding new child sync controller with id %1 and engine id %2.\r\n
0xb0000221 | Delete Account %1: Unknown Store Type %2.\r\n
0xb0000226 | AccountSyncController: Starting ScheduleManager work for account %1, engine %2.\r\n
0xb0000227 | Upgrading account %1 from version %2 to the current version %3.\r\n
0xb0000228 | Ignoring account %1 because its version (%2) doesn't match the current version (%3).\r\n
0xb0000229 | Detected a previous failure in Execute Activity Step for account %1, delaying next run.\r\n
0xb000022b | Account %1 setting schedule trigger requirement %2.\r\n
0xb000022c | Account %1 exiting delay and resetting successive empty sync count to zero.\r\n
0xb0000231 | Aggregate controller has new merged result: engine %1, result %2.\r\n
0xb0000232 | Handle server change for account %1 and engine %2.\r\n
0xb0000233 | Handle login info change for account %1 and engine %2.\r\n
0xb000023a | Executing ScheduleManager work of type %3 for account %1, engine %2.\r\n
0xb000023b | Executing Post OOBE notifications work. Cancelled = %1\r\n
0xb00002bd | Cred Vault: DeletePwd Called. Caller: _PurgeActiveSyncAccount, Partner %1\r\n
0xb00002be | Cred Vault: DeletePwd Called. Caller: ActiveSyncServer_DeletePassword, Partner %1\r\n
0xb0000321 | Setting delayed value of conversation sync enabled to %1\r\n
0xb0000322 | Setting the value of conversation sync if changed - Desired = %1, Current = %2\r\n
0xb0000329 | Schedule for account %1 triggered when the screen was on and the schedule was set to trigger for screen on.\r\n
0xb000032a | Schedule %1 for account %2 triggered with period %3, base period %4, failure count %5, trigger flags %6, engine %7.\r\n
0xb000032b | TokenBucket: Account %1 is throttling for %2 minutes.\r\n
0xb000032c | TokenBucket: Account %1 successfully retrieved a token.\r\n
0xb000032d | TokenBucket: Account %1 was not throttled because the screen was on.\r\n
0xb0000384 | NotificationUtils: Initializing notification utils. IsOobeDone = %1\r\n
0xb0000385 | NotificationUtils: Cleanup.\r\n
0xb0000386 | NotificationUtils: _PostAttentionRequiredNotification(). Account = %1, Toast already sent = %2.\r\n
0xb0000387 | NotificationUtils: _RemoveAttentionRequiredNotification(). Account = %1\r\n
0xd0000001 | none\r\n
0xd0000002 | battery saver on\r\n
0xd0000003 | data saver on\r\n
0xd0000004 | thermal saver on\r\n
0xd0000005 | all savers on\r\n
0xd0000006 | batterysaver\r\n
0xd0000007 | datasaver\r\n
0xd0000008 | thermalsaver\r\n
0xd0000009 | internet mail sync engine\r\n
0xd000000a | EAS sync engine\r\n
0xd000000b | card dav sync engine\r\n
0xd000000c | caldav sync engine\r\n
0xd000000d | smtp sync engine\r\n
0xd000000e | none\r\n
0xd000000f | exit backoff mode\r\n
0xd0000010 | sync\r\n
0xd0000011 | exit backoff and sync\r\n
0xd0000012 | reset empty sync count\r\n
0xd0000013 | exit backoff and reset empty sync count\r\n
0xd0000014 | remove alternative trigger\r\n
0xd0000015 | remove alternative trigger and sync\r\n
0xd0000016 | schedule changed\r\n
0xd0000017 | saver mode changed\r\n
0xd0000018 | exit backoff mode\r\n
0xd0000019 | remove alternative trigger\r\n
0xd000001a | Unknown\r\n
0xd000001b | Active\r\n
0xd000001c | Unlocked\r\n
0xd000001d | PinLocked\r\n
0xd000001e | PukBlocked\r\n
0xd000001f | Disabled\r\n
0xd0000020 | Unknown\r\n
0xd0000021 | NoSim\r\n
0xd0000022 | InvalidSim\r\n
0xd0000023 | ValidSim\r\n
0xd0000024 | NonSimSwap\r\n
0xd0000025 | SimSwap\r\n

### 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000003 | State\r\n
0x10000025 | CommsService\r\n
0x10000027 | Warning\r\n
0x10000028 | StateTransition\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000001 | Error: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: %1 Location: %2 Line Number: %3\r\n
0xb0000066 | SyncController:[Consistency] [%1] Registry key for this partner is being deleted because it's invalid.\r\n
0xb0000067 | SyncController:[Consistency] Default Store is invalid, but will not be deleted. There were '%1' stores found.\r\n
0xb0000068 | SyncController:[Consistency] [%1:%2:%3] Store being deleted because it's invalid. There were '%4' stores found.\r\n
0xb0000069 | SyncController:[Consistency] [%1] Registry key for this partner is invalid, the reason is '%2'.\r\n
0xb000006a | SyncController:[Consistency] [%1:%2:%3] Store is invalid, the reason is '%4'.\r\n
0xb00000bf | Sync WNF event: %1\r\n
0xb00000c1 | Sync WNF event: %1 - %2\r\n
0xb00000c3 | Sync WNF event %1 not found.\r\n
0xb00000c4 | Notified golden account existence: %1.\r\n
0xb00000c9 | Receive WNF event; current mode: %1, current value: %2\r\n
0xb00001f4 | AccountSyncController: Starting scheduled SyncExecutor for account %1, engine %2.\r\n
0xb00001f5 | AccountSyncController: Starting interactive SyncExecutor for account %1, engine %2.\r\n
0xb00001f6 | AccountSyncController: Starting AUTDExecutor for account %1, engine %2.\r\n
0xb00001f7 | AccountSyncController: Finished SyncExecutor work for account %1 with hr=%2, retry level %3, can start AUTD %4, queue empty %5, saver mode %6, engine %7.\r\n
0xb00001f8 | AccountSyncController: Finished AUTDExecutor work for account %1 with hr %2, can start AUTD %3, queue empty %4, saver mode %5, engine %6.\r\n
0xb00001f9 | AccountSyncController: Adding new controller with id %1.\r\n
0xb00001fa | AccountSyncController: Deleting sync controller with id %1.\r\n
0xb00001fb | Handle schedule period changed from %2 min to %3 min for account %1 and engine %4.\r\n
0xb00001fc | Handle content/filter change for account %1 and engine %2.\r\n
0xb00001fd | AccountSyncController: Added new AccountSyncController for account %1.\r\n
0xb00001fe | Started DownloadEmailBodyWork for account %1.\r\n
0xb00001ff | Finished DownloadEmailBodyWork for account %1.\r\n
0xb0000200 | Started AddMeetingResponseWork for account %1.\r\n
0xb0000201 | Finished AddMeetingResponseWork for account %1 with HRESULT %2\r\n
0xb0000204 | Started DownloadEmailAttachmentWork for account %1.\r\n
0xb0000205 | Finished DownloadEmailAttachmentWork for account %1.\r\n
0xb0000206 | Started DownloadSharePointDocumentWork for account %1.\r\n
0xb0000207 | Finished DownloadSharePointDocumentWork for account %1.\r\n
0xb000020a | Started GalSearchWork for account %1.\r\n
0xb000020b | Finished GalSearchWork for account %1.\r\n
0xb000020c | Started GetOofWork for account %1.\r\n
0xb000020d | Finished GetOofWork for account %1.\r\n
0xb000020e | Started MailboxSearchWork for account %1.\r\n
0xb000020f | Finished MailboxSearchWork for account %1.\r\n
0xb0000210 | Started PurgeDeletedAccountsWork.\r\n
0xb0000211 | Finished PurgeDeletedAccountsWork.\r\n
0xb0000212 | Started SetFolderSyncStateWork for account %1.\r\n
0xb0000213 | Finished SetFolderSyncStateWork for account %1.\r\n
0xb0000216 | Started UpdateContentTypesWork for account %1.\r\n
0xb0000217 | Finished UpdateContentTypesWork for account %1.\r\n
0xb0000218 | Started SetOofWork for account %1.\r\n
0xb0000219 | Finished SetOofWork for account %1.\r\n
0xb000021c | Started FlushAccountSettingsWork for account %1.\r\n
0xb000021d | Finished FlushAccountSettingsWork for account %1.\r\n
0xb000021e | Started PurgeDeletedAccountWork for account %1.\r\n
0xb000021f | Finished PurgeDeletedAccountWork for account %1.\r\n
0xb0000220 | AccountSyncController: Adding new child sync controller with id %1 and engine id %2.\r\n
0xb0000221 | Delete Account %1: Unknown Store Type %2.\r\n
0xb0000226 | AccountSyncController: Starting ScheduleManager work for account %1, engine %2.\r\n
0xb0000227 | Upgrading account %1 from version %2 to the current version %3.\r\n
0xb0000228 | Ignoring account %1 because its version (%2) doesn't match the current version (%3).\r\n
0xb0000229 | Detected a previous failure in Execute Activity Step for account %1, delaying next run.\r\n
0xb000022b | Account %1 setting schedule trigger requirement %2.\r\n
0xb000022c | Account %1 exiting delay and resetting successive empty sync count to zero.\r\n
0xb0000231 | Aggregate controller has new merged result: engine %1, result %2.\r\n
0xb0000232 | Handle server change for account %1 and engine %2.\r\n
0xb0000233 | Handle login info change for account %1 and engine %2.\r\n
0xb000023a | Executing ScheduleManager work of type %3 for account %1, engine %2.\r\n
0xb00002bd | Cred Vault: DeletePwd Called. Caller: _PurgeActiveSyncAccount, Partner %1\r\n
0xb00002be | Cred Vault: DeletePwd Called. Caller: ActiveSyncServer_DeletePassword, Partner %1\r\n
0xb0000321 | Setting delayed value of conversation sync enabled to %1\r\n
0xb0000322 | Setting the value of conversation sync if changed - Desired = %1, Current = %2\r\n
0xb0000329 | Schedule for account %1 triggered when the screen was on and the schedule was set to trigger for screen on.\r\n
0xb000032a | Schedule %1 for account %2 triggered with period %3, base period %4, failure count %5, trigger flags %6, engine %7.\r\n
0xb000032b | TokenBucket: Account %1 is throttling for %2 minutes.\r\n
0xb000032c | TokenBucket: Account %1 successfully retrieved a token.\r\n
0xb000032d | TokenBucket: Account %1 was not throttled because the screen was on.\r\n
0xb0000384 | NotificationUtils: Initializing notification utils. IsOobeDone = %1\r\n
0xd0000001 | none\r\n
0xd0000002 | battery saver on\r\n
0xd0000003 | data saver on\r\n
0xd0000004 | thermal saver on\r\n
0xd0000005 | all savers on\r\n
0xd0000006 | batterysaver\r\n
0xd0000007 | datasaver\r\n
0xd0000008 | thermalsaver\r\n
0xd0000009 | EAS sync engine\r\n
0xd000000a | smtp sync engine\r\n
0xd000000b | card dav sync engine\r\n
0xd000000c | caldav sync engine\r\n
0xd000000d | internet mail sync engine\r\n
0xd000000e | none\r\n
0xd000000f | exit backoff mode\r\n
0xd0000010 | sync\r\n
0xd0000011 | exit backoff and sync\r\n
0xd0000012 | reset empty sync count\r\n
0xd0000013 | exit backoff and reset empty sync count\r\n
0xd0000014 | remove alternative trigger\r\n
0xd0000015 | remove alternative trigger and sync\r\n
0xd0000016 | schedule changed\r\n
0xd0000017 | saver mode changed\r\n
0xd0000018 | exit backoff mode\r\n
0xd0000019 | remove alternative trigger\r\n
