## unistore.dll

Path: %SystemRoot%\System32\unistore.dll

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x10000009 | Debug\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000000a | Trace\r\n
0xb0000001 | Error: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: %1 Location: %2 Line Number: %3\r\n
0xb00007d0 | Tombstone cleanup completed: store [%1], iterations [%2], duration [%3 s]\r\n
0xb0000bb8 | Updating DB LCID, Invalidating all open sessions and handles\r\n
0xb0000bb9 | Unified store lock was held for %1 seconds. ReleaseFunc = %2\r\n
0xb0000bba | Unified store lock type %1 was not released even after %2 seconds. Lock Owner Process Id: %3\r\n
0xb0000bbb | CeSeekDatabaseEx failed, Handle: %1, HR: %2 SeekType: %3\r\n
0xb0000bbc | CeWriteRecordProps failed, Handle: %1, HR: %2, OIDRecord: %3\r\n
0xb0000bbd | CeReadRecordPropsEx failed, Handle: %1, HR: %2, Flags: %3\r\n
0xb0000bbe | Closed handle before refcount was 0, Handle: %1, Outstanding refCount: %2\r\n
0xb0000bbf | Missed Event Notification Dispatched\r\n
0xb0000bc1 | Mutex acquire failed, WaitResult = %1, HR = %2\r\n
0xb0000bc2 | Deserialize Knowledge failed, HR = %1, cbKnowledge = %2, cbKnowledgeLogged = %3\r\n
0xb0000bc3 | Opening Table %1 without any index.\r\n
0xb0000bc4 | Restriction Type = %1\r\n
0xb0000bc5 | PropertyRestriction: Operation %1, Property id %2.\r\n
0xb0000bc6 | BitMaskRestriction: Operation %1, Property id %2\r\n
0xb0000bc7 | Seeked and read %1 rows before finding row with matching index\r\n
0xb0000bc8 | Count %1: Property ids: %2\r\n
0xb0000bc9 | MountDeviceVolume Error: %1\r\n
0xb0000bca | Remote notification dispatched, Event type: %1, Object type: %2, Object Id: %3\r\n
0xb0000bcb | Remote notification published, Event type: %1, Object type: %2, Object Id: %3\r\n
0xb0000bcc | Missed Event Notification Published\r\n
0xb0000bcd | UnifiedStore delete store id = %1\r\n
0xb0000bce | UnifiedStore delete folder types = %1, store = %2, id = %3\r\n
0xb0000bcf | Table: %1\r\n
0xb0000bd0 | Failed to commit transaction, attempting rollback recovery (error %1, session %2)\r\n
0xb0000bd1 | Failed to rollback transaction (error %1, session %2)\r\n
0xb0000bd2 | Recovery complete (error %1, session %2)\r\n
0xb0000bd3 | Failed to open table handle\r\n
0xb0000bd4 | Unified Store RPC Call: %1\r\n
0xb0000bd5 | Failed to set property ID %1, error %2\r\n
0xb0000bd6 | Process %1 underflowed its suspend/resume count, now is %2\r\n
0xb0000bd7 | Process %1 suspended its message queue, count %2\r\n
0xb0000bd8 | Process %1 resumed its message queue, count %2\r\n
0xb0000bd9 | Process with rundown identifier %1 aborted %2 transactions\r\n
0xb0000bda | Client process %1 has lost events\r\n
0xb0000bdb | Client process %1 has resumed fetching events\r\n
0xb0000bdc | Property should be added in schema. table: %1, id: %2\r\n
0xb0000bdd | Advisee in service process (vtable %1) has lost events\r\n
0xb0000bde | Notification Queue lost events\r\n
0xb0000bdf | Final transaction rollback attempt failed, Error: %1\r\n
0xb0000be0 | Closing active table id: %1\r\n
0xb0000be3 | Unified store process identifier %1 created for process\r\n
0xb0000be4 | Process exit callback for process with identifier %1\r\n
0xb0000be5 | Unified store rundown for process %1 with identifier %2\r\n
0xb0000be6 | Store id: %1 Supported Types changed to: %2\r\n
0xb0000be7 | DBSession::_UpgradeDatabase Error: %1\r\n
0xb0000be8 | JetAttachDatabase Error: %1\r\n
0xb0000be9 | Upgrading database, lcidChanged: %1, storeVersionChanged: %2, isIndexCorrupt: %3\r\n
0xb0000bea | Creating Missing indexes, table ID: %1, count: %2\r\n
0xb0000beb | Number of indexes changed unexpectedly, table ID: %1, numExistingIndex: %2\r\n
0xb0000bfe | Attempting to defragment scope knowledge. Partner id: %1, scope id: %2, exceptions: %3 positive and %4 negative, min vector size: %5, max vector size: %6, starting tick count: %7\r\n
0xb0000bff | Defragmented scope knowledge. Partner id: %1, scope id: %2, original size: %3, defragmented size: %4, exceptions: %5\r\n
0xb0000c00 | Done defragmenting scope knowledge. Partner id: %1, scope id: %2, succeeded: %3\r\n
0xb0000c01 | Attempting to defragment partner knowledge. Partner id: %1, size: %2, defragmentation threshold: %3\r\n
0xb0000c02 | The knowldege for partner id %1 has %2 scopes, %3 positive exceptions, %4 negative exceptions, min vector size: %5 and max vector size: %6\r\n
0xb0000c03 | Successfully defragmented %2 scopes out of %3 for partner id %1.\r\n
0xb0000c04 | Defragmented partner knowledge. Partner id: %1, original size: %2, defragmented size: %3\r\n
0xb0000c05 | Done defragmenting partner knowledge. Partner id: %1, succeeded: %2\r\n
0xb0000c06 | Failed to reduce the knowledge size for partner id %1 below %2%% of the maximum size (size: %2, maximum size: %4).\r\n
0xb0000c07 | The knowledge size for partner id %1 exceeds %3%% of the maximum size (size: %2, maximum size: %4). The synchronization may exhibit degraded performance\r\n
0xb0000c08 | The knowledge size for partner id %1 exceeds %3%% of the maximum size (size: %2, maximum size: %4). The synchronization may start failing if the knowledge size keeps increasing\r\n
0xb0000c09 | The knowledge size for partner id %1 exceeds the maximum size (size: %2, maximum size: %3). The synchronization will fail\r\n
0xb0000c1c | Closing stale notify context %2 on behalf of rundown id %1\r\n
0xb0000c1d | Closing stale object %2 on behalf of rundown id %1\r\n
0xb0000c26 | [store upgrade] The current store version is %1\r\n
0xb0000c28 | [store upgrade] Performing upgrade task %1\r\n
0xb0000c29 | [store upgrade] %1 appointments updated\r\n
0xd0000001 | UpgradeStoreFilters\r\n
0xd0000002 | UpgradeAppStoreMask\r\n
0xd0000003 | UpgradeApptRemoteId\r\n
0xd0000004 | UpgradeMoveAggregateContactsToDefaultStore\r\n
0xd0000005 | UpgradeMoveUseAppSummaryToCalendar\r\n
0xd0000006 | UpgradeMoveAppAccessModeToCalendar\r\n
0xd0000007 | UpgradeRoomAlbums\r\n
0xd0000008 | UpgradeCalendarColors\r\n
0xd0000009 | UpgradeStoreContactCloak\r\n
0xd000000a | UpgradeStoreChangeTracking\r\n
0xd000000b | UpgradeSmsStoreToCloaked\r\n
0xd000000c | UpgradeStoresWithGroupings\r\n
0xd000000d | UpgradeAppStoreNames\r\n
0xd000000e | UpgradeProductIdToPackageName\r\n
0xd000000f | UpgradeAppEmailCalendarDeleteChangeTracking\r\n
0xd0000010 | UpgradeAppointmentRecurringData\r\n
0xd0000011 | UpgradeRemoveAggregatesWithNoComponents\r\n
0xd0000012 | UpgradeDeviceStoreRequiredTypes\r\n
0xd0000013 | UpgradeStoreDataProtection\r\n
0xd0000014 | UpgradeMeetingTimezones\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x10000009 | Debug\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000000a | Trace\r\n
0xb0000001 | Error: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: %1 Location: %2 Line Number: %3\r\n
0xb0000032 | Info: %1 Location: %2 Line Number: %3\r\n
0xb00007d0 | Tombstone cleanup completed: store [%1], iterations [%2], duration [%3 s]\r\n
0xb00007d1 | Terminated suspended app [%2]: result [%1]\r\n
0xb00007d2 | App lost change tracking [%1]: current rev [%2], deleted item rev [%3]\r\n
0xb0000bb8 | Updating DB LCID, Invalidating all open sessions and handles\r\n
0xb0000bb9 | Unified store lock was held for %1 seconds. ReleaseFunc = %2\r\n
0xb0000bba | Unified store lock type %1 was not released even after %2 seconds. Lock Owner Process Id: %3\r\n
0xb0000bbb | CeSeekDatabaseEx failed, Handle: %1, HR: %2 SeekType: %3\r\n
0xb0000bbc | CeWriteRecordProps failed, Handle: %1, HR: %2, OIDRecord: %3\r\n
0xb0000bbd | CeReadRecordPropsEx failed, Handle: %1, HR: %2, Flags: %3\r\n
0xb0000bbe | Closed handle before refcount was 0, Handle: %1, Outstanding refCount: %2\r\n
0xb0000bbf | Missed Event Notification Dispatched\r\n
0xb0000bc1 | Mutex acquire failed, WaitResult = %1, HR = %2\r\n
0xb0000bc2 | Deserialize Knowledge failed, HR = %1, cbKnowledge = %2, cbKnowledgeLogged = %3\r\n
0xb0000bc3 | Opening Table %1 without any index.\r\n
0xb0000bc4 | Restriction Type = %1\r\n
0xb0000bc5 | PropertyRestriction: Operation %1, Property id %2.\r\n
0xb0000bc6 | BitMaskRestriction: Operation %1, Property id %2\r\n
0xb0000bc7 | Seeked and read %1 rows before finding row with matching index\r\n
0xb0000bc8 | Count %1: Property ids: %2\r\n
0xb0000bc9 | MountDeviceVolume Error: %1\r\n
0xb0000bca | Remote notification dispatched, Event type: %1, Object type: %2, Object Id: %3\r\n
0xb0000bcb | Remote notification published, Event type: %1, Object type: %2, Object Id: %3\r\n
0xb0000bcc | Missed Event Notification Published\r\n
0xb0000bcd | UnifiedStore delete store id = %1\r\n
0xb0000bce | UnifiedStore delete folder types = %1, store = %2, id = %3\r\n
0xb0000bcf | Table: %1\r\n
0xb0000bd0 | Failed to commit transaction, attempting rollback recovery (error %1, session %2)\r\n
0xb0000bd1 | Failed to rollback transaction (error %1, session %2)\r\n
0xb0000bd2 | Recovery complete (error %1, session %2)\r\n
0xb0000bd3 | Failed to open table handle\r\n
0xb0000bd4 | Unified Store RPC Call: %1\r\n
0xb0000bd5 | Failed to set property ID %1, error %2\r\n
0xb0000bd6 | Process %1 underflowed its suspend/resume count, now is %2\r\n
0xb0000bd7 | Process %1 suspended its message queue, count %2\r\n
0xb0000bd8 | Process %1 resumed its message queue, count %2\r\n
0xb0000bd9 | Process with rundown identifier %1 aborted %2 transactions\r\n
0xb0000bda | Client process %1 has lost events\r\n
0xb0000bdb | Client process %1 has resumed fetching events\r\n
0xb0000bdc | Property should be added in schema. table: %1, id: %2\r\n
0xb0000bdd | Advisee in service process (vtable %1) has lost events\r\n
0xb0000bde | Notification Queue lost events\r\n
0xb0000bdf | Final transaction rollback attempt failed, Error: %1\r\n
0xb0000be0 | Closing active table id: %1\r\n
0xb0000be3 | Unified store process identifier %1 created for process\r\n
0xb0000be4 | Process exit callback for process with identifier %1\r\n
0xb0000be5 | Unified store rundown for process %1 with identifier %2\r\n
0xb0000be6 | Store id: %1 Supported Types changed to: %2\r\n
0xb0000be7 | DBSession::_UpgradeDatabase Error: %1\r\n
0xb0000be8 | JetAttachDatabase Error: %1\r\n
0xb0000be9 | Upgrading database, lcidChanged: %1, storeVersionChanged: %2, isIndexCorrupt: %3\r\n
0xb0000bea | Creating Missing indexes, table ID: %1, count: %2\r\n
0xb0000beb | Number of indexes changed unexpectedly, table ID: %1, numExistingIndex: %2\r\n
0xb0000bec | The database was corrupted, and recovered\r\n
0xb0000bed | Simulation of database corruption\r\n
0xb0000bfe | Attempting to defragment scope knowledge. Partner id: %1, scope id: %2, exceptions: %3 positive and %4 negative, min vector size: %5, max vector size: %6, starting tick count: %7\r\n
0xb0000bff | Defragmented scope knowledge. Partner id: %1, scope id: %2, original size: %3, defragmented size: %4, exceptions: %5\r\n
0xb0000c00 | Done defragmenting scope knowledge. Partner id: %1, scope id: %2, succeeded: %3\r\n
0xb0000c01 | Attempting to defragment partner knowledge. Partner id: %1, size: %2, defragmentation threshold: %3\r\n
0xb0000c02 | The knowledge for partner id %1 has %2 scopes, %3 positive exceptions, %4 negative exceptions, min vector size: %5 and max vector size: %6\r\n
0xb0000c03 | Successfully defragmented %2 scopes out of %3 for partner id %1.\r\n
0xb0000c04 | Defragmented partner knowledge. Partner id: %1, original size: %2, defragmented size: %3\r\n
0xb0000c05 | Done defragmenting partner knowledge. Partner id: %1, succeeded: %2\r\n
0xb0000c06 | Failed to reduce the knowledge size for partner id %1 below %2%% of the maximum size (size: %3, maximum size: %4).\r\n
0xb0000c07 | The knowledge size for partner id %1 exceeds %3%% of the maximum size (size: %2, maximum size: %4). The synchronization may exhibit degraded performance\r\n
0xb0000c08 | The knowledge size for partner id %1 exceeds %3%% of the maximum size (size: %2, maximum size: %4). The synchronization may start failing if the knowledge size keeps increasing\r\n
0xb0000c09 | The knowledge size for partner id %1 exceeds the maximum size (size: %2, maximum size: %3). The synchronization will fail\r\n
0xb0000c1c | Closing stale notify context %2 on behalf of rundown id %1\r\n
0xb0000c1d | Closing stale object %2 on behalf of rundown id %1\r\n
0xb0000c26 | [store upgrade] The current store version is %1\r\n
0xb0000c28 | [store upgrade] Performing upgrade task %1\r\n
0xb0000c29 | [store upgrade] %1 appointments updated\r\n
0xd0000001 | UpgradeStoreFilters\r\n
0xd0000002 | UpgradeAppStoreMask\r\n
0xd0000003 | UpgradeApptRemoteId\r\n
0xd0000004 | UpgradeMoveAggregateContactsToDefaultStore\r\n
0xd0000005 | UpgradeMoveUseAppSummaryToCalendar\r\n
0xd0000006 | UpgradeMoveAppAccessModeToCalendar\r\n
0xd0000007 | UpgradeRoomAlbums\r\n
0xd0000008 | UpgradeCalendarColors\r\n
0xd0000009 | UpgradeStoreContactCloak\r\n
0xd000000a | UpgradeStoreChangeTracking\r\n
0xd000000b | UpgradeSmsStoreToCloaked\r\n
0xd000000c | UpgradeStoresWithGroupings\r\n
0xd000000d | UpgradeAppStoreNames\r\n
0xd000000e | UpgradeProductIdToPackageName\r\n
0xd000000f | UpgradeAppEmailCalendarDeleteChangeTracking\r\n
0xd0000010 | UpgradeAppointmentRecurringData\r\n
0xd0000011 | UpgradeRemoveAggregatesWithNoComponents\r\n
0xd0000012 | UpgradeDeviceStoreRequiredTypes\r\n
0xd0000013 | UpgradeStoreDataProtection\r\n
0xd0000014 | UpgradeMeetingTimezones\r\n
0xd0000015 | UpgradeMediaStorageGuid\r\n
0xd0000016 | UpgradeDeviceStoreEnsureNotSuppressed\r\n
0xd0000017 | UpgradeIrmTemplateDescriptions\r\n
0xd0000018 | CleanupChangeTrackingData\r\n
0xd0000019 | UpgradeCalendarWriteAccess\r\n
0xd000001a | UpgradeLastStoreId\r\n
0xd000001b | UpgradeContactDatesToUtcMidnight\r\n
0xd000001c | UpgradeCleanupAggregateContactMismatch\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x10000009 | Debug\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000000a | Trace\r\n
0xb0000001 | Error: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: %1 Location: %2 Line Number: %3\r\n
0xb0000032 | Info: %1 Location: %2 Line Number: %3\r\n
0xb00007d0 | Tombstone cleanup completed: store [%1], iterations [%2], duration [%3 s]\r\n
0xb00007d1 | Terminated suspended app [%2]: result [%1]\r\n
0xb00007d2 | App lost change tracking [%1]: current rev [%2], deleted item rev [%3]\r\n
0xb0000bb8 | Updating DB LCID, Invalidating all open sessions and handles\r\n
0xb0000bb9 | Unified store lock was held for %1 seconds. ReleaseFunc = %2\r\n
0xb0000bba | Unified store lock type %1 was not released even after %2 seconds. Lock Owner Process Id: %3\r\n
0xb0000bbb | CeSeekDatabaseEx failed, Handle: %1, HR: %2 SeekType: %3\r\n
0xb0000bbc | CeWriteRecordProps failed, Handle: %1, HR: %2, OIDRecord: %3\r\n
0xb0000bbd | CeReadRecordPropsEx failed, Handle: %1, HR: %2, Flags: %3\r\n
0xb0000bbe | Closed handle before refcount was 0, Handle: %1, Outstanding refCount: %2\r\n
0xb0000bbf | Missed Event Notification Dispatched\r\n
0xb0000bc1 | Mutex acquire failed, WaitResult = %1, HR = %2\r\n
0xb0000bc2 | Deserialize Knowledge failed, HR = %1, cbKnowledge = %2, cbKnowledgeLogged = %3\r\n
0xb0000bc3 | Opening Table %1 without any index.\r\n
0xb0000bc4 | Restriction Type = %1\r\n
0xb0000bc5 | PropertyRestriction: Operation %1, Property id %2.\r\n
0xb0000bc6 | BitMaskRestriction: Operation %1, Property id %2\r\n
0xb0000bc7 | Seeked and read %1 rows before finding row with matching index\r\n
0xb0000bc8 | Count %1: Property ids: %2\r\n
0xb0000bc9 | MountDeviceVolume Error: %1\r\n
0xb0000bca | Remote notification dispatched, Event type: %1, Object type: %2, Object Id: %3\r\n
0xb0000bcb | Remote notification published, Event type: %1, Object type: %2, Object Id: %3\r\n
0xb0000bcc | Missed Event Notification Published\r\n
0xb0000bcd | UnifiedStore delete store id = %1\r\n
0xb0000bce | UnifiedStore delete folder types = %1, store = %2, id = %3\r\n
0xb0000bcf | Table: %1\r\n
0xb0000bd0 | Failed to commit transaction, attempting rollback recovery (error %1, session %2)\r\n
0xb0000bd1 | Failed to rollback transaction (error %1, session %2)\r\n
0xb0000bd2 | Recovery complete (error %1, session %2)\r\n
0xb0000bd3 | Failed to open table handle\r\n
0xb0000bd4 | Unified Store RPC Call: %1\r\n
0xb0000bd5 | Failed to set property ID %1, error %2\r\n
0xb0000bd6 | Process %1 underflowed its suspend/resume count, now is %2\r\n
0xb0000bd7 | Process %1 suspended its message queue, count %2\r\n
0xb0000bd8 | Process %1 resumed its message queue, count %2\r\n
0xb0000bd9 | Process with rundown identifier %1 aborted %2 transactions\r\n
0xb0000bda | Client process %1 has lost events\r\n
0xb0000bdb | Client process %1 has resumed fetching events\r\n
0xb0000bdc | Property should be added in schema. table: %1, id: %2\r\n
0xb0000bdd | Advisee in service process (vtable %1) has lost events\r\n
0xb0000bde | Notification Queue lost events\r\n
0xb0000bdf | Final transaction rollback attempt failed, Error: %1\r\n
0xb0000be0 | Closing active table id: %1\r\n
0xb0000be3 | Unified store process identifier %1 created for process\r\n
0xb0000be4 | Process exit callback for process with identifier %1\r\n
0xb0000be5 | Unified store rundown for process %1 with identifier %2\r\n
0xb0000be6 | Store id: %1 Supported Types changed to: %2\r\n
0xb0000be7 | DBSession::_UpgradeDatabase Error: %1\r\n
0xb0000be8 | JetAttachDatabase Error: %1\r\n
0xb0000be9 | Upgrading database, lcidChanged: %1, storeVersionChanged: %2, isIndexCorrupt: %3\r\n
0xb0000bea | Creating Missing indexes, table ID: %1, count: %2\r\n
0xb0000beb | Number of indexes changed unexpectedly, table ID: %1, numExistingIndex: %2\r\n
0xb0000bec | The database was corrupted, and recovered\r\n
0xb0000bed | Simulation of database corruption\r\n
0xb0000bfe | Attempting to defragment scope knowledge. Partner id: %1, scope id: %2, exceptions: %3 positive and %4 negative, min vector size: %5, max vector size: %6, starting tick count: %7\r\n
0xb0000bff | Defragmented scope knowledge. Partner id: %1, scope id: %2, original size: %3, defragmented size: %4, exceptions: %5\r\n
0xb0000c00 | Done defragmenting scope knowledge. Partner id: %1, scope id: %2, succeeded: %3\r\n
0xb0000c01 | Attempting to defragment partner knowledge. Partner id: %1, size: %2, defragmentation threshold: %3\r\n
0xb0000c02 | The knowledge for partner id %1 has %2 scopes, %3 positive exceptions, %4 negative exceptions, min vector size: %5 and max vector size: %6\r\n
0xb0000c03 | Successfully defragmented %2 scopes out of %3 for partner id %1.\r\n
0xb0000c04 | Defragmented partner knowledge. Partner id: %1, original size: %2, defragmented size: %3\r\n
0xb0000c05 | Done defragmenting partner knowledge. Partner id: %1, succeeded: %2\r\n
0xb0000c06 | Failed to reduce the knowledge size for partner id %1 below %2%% of the maximum size (size: %3, maximum size: %4).\r\n
0xb0000c07 | The knowledge size for partner id %1 exceeds %3%% of the maximum size (size: %2, maximum size: %4). The synchronization may exhibit degraded performance\r\n
0xb0000c08 | The knowledge size for partner id %1 exceeds %3%% of the maximum size (size: %2, maximum size: %4). The synchronization may start failing if the knowledge size keeps increasing\r\n
0xb0000c09 | The knowledge size for partner id %1 exceeds the maximum size (size: %2, maximum size: %3). The synchronization will fail\r\n
0xb0000c1c | Closing stale notify context %2 on behalf of rundown id %1\r\n
0xb0000c1d | Closing stale object %2 on behalf of rundown id %1\r\n
0xb0000c26 | [store upgrade] The current store version is %1\r\n
0xb0000c28 | [store upgrade] Performing upgrade task %1\r\n
0xb0000c29 | [store upgrade] %1 appointments updated\r\n
0xd0000001 | UpgradeStoreFilters\r\n
0xd0000002 | UpgradeAppStoreMask\r\n
0xd0000003 | UpgradeApptRemoteId\r\n
0xd0000004 | UpgradeMoveAggregateContactsToDefaultStore\r\n
0xd0000005 | UpgradeMoveUseAppSummaryToCalendar\r\n
0xd0000006 | UpgradeMoveAppAccessModeToCalendar\r\n
0xd0000007 | UpgradeRoomAlbums\r\n
0xd0000008 | UpgradeCalendarColors\r\n
0xd0000009 | UpgradeStoreContactCloak\r\n
0xd000000a | UpgradeStoreChangeTracking\r\n
0xd000000b | UpgradeSmsStoreToCloaked\r\n
0xd000000c | UpgradeStoresWithGroupings\r\n
0xd000000d | UpgradeAppStoreNames\r\n
0xd000000e | UpgradeProductIdToPackageName\r\n
0xd000000f | UpgradeAppEmailCalendarDeleteChangeTracking\r\n
0xd0000010 | UpgradeAppointmentRecurringData\r\n
0xd0000011 | UpgradeRemoveAggregatesWithNoComponents\r\n
0xd0000012 | UpgradeDeviceStoreRequiredTypes\r\n
0xd0000013 | UpgradeStoreDataProtection\r\n
0xd0000014 | UpgradeMeetingTimezones\r\n
0xd0000015 | UpgradeMediaStorageGuid\r\n
0xd0000016 | UpgradeDeviceStoreEnsureNotSuppressed\r\n
0xd0000017 | UpgradeIrmTemplateDescriptions\r\n
0xd0000018 | CleanupChangeTrackingData\r\n
0xd0000019 | UpgradeCalendarWriteAccess\r\n
0xd000001a | UpgradeLastStoreId\r\n
0xd000001b | UpgradeContactDatesToUtcMidnight\r\n
0xd000001c | UpgradeCleanupAggregateContactMismatch\r\n
0xd000001d | UpgradeRemoveUdmAutoResolverSyncPartner\r\n
0xd000001e | UpgradeAddCompletedTaskFlag\r\n
0xd000001f | UpgradeContactMiddleName\r\n
0xd0000020 | UpgradeDefectExternalContactChangeTracking\r\n

### 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000009 | Debug\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000000a | Trace\r\n
0xb0000001 | Error: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: %1 Location: %2 Line Number: %3\r\n
0xb0000032 | Info: %1 Location: %2 Line Number: %3\r\n
0xb00007d0 | Tombstone cleanup completed: store [%1], iterations [%2], duration [%3 s]\r\n
0xb00007d1 | Terminated suspended app [%2]: result [%1]\r\n
0xb00007d2 | App lost change tracking [%1]: current rev [%2], deleted item rev [%3]\r\n
0xb0000bb8 | Updating DB LCID, Invalidating all open sessions and handles\r\n
0xb0000bb9 | Unified store lock was held for %1 seconds. ReleaseFunc = %2\r\n
0xb0000bba | Unified store lock type %1 was not released even after %2 seconds. Lock Owner Process Id: %3\r\n
0xb0000bbb | CeSeekDatabaseEx failed, Handle: %1, HR: %2 SeekType: %3\r\n
0xb0000bbc | CeWriteRecordProps failed, Handle: %1, HR: %2, OIDRecord: %3\r\n
0xb0000bbd | CeReadRecordPropsEx failed, Handle: %1, HR: %2, Flags: %3\r\n
0xb0000bbe | Closed handle before refcount was 0, Handle: %1, Outstanding refCount: %2\r\n
0xb0000bbf | Missed Event Notification Dispatched\r\n
0xb0000bc1 | Mutex acquire failed, WaitResult = %1, HR = %2\r\n
0xb0000bc2 | Deserialize Knowledge failed, HR = %1, cbKnowledge = %2, cbKnowledgeLogged = %3\r\n
0xb0000bc3 | Opening Table %1 without any index.\r\n
0xb0000bc4 | Restriction Type = %1\r\n
0xb0000bc5 | PropertyRestriction: Operation %1, Property id %2.\r\n
0xb0000bc6 | BitMaskRestriction: Operation %1, Property id %2\r\n
0xb0000bc7 | Seeked and read %1 rows before finding row with matching index\r\n
0xb0000bc8 | Count %1: Property ids: %2\r\n
0xb0000bc9 | MountDeviceVolume Error: %1\r\n
0xb0000bca | Remote notification dispatched, Event type: %1, Object type: %2, Object Id: %3\r\n
0xb0000bcb | Remote notification published, Event type: %1, Object type: %2, Object Id: %3\r\n
0xb0000bcc | Missed Event Notification Published\r\n
0xb0000bcd | UnifiedStore delete store id = %1\r\n
0xb0000bce | UnifiedStore delete folder types = %1, store = %2, id = %3\r\n
0xb0000bcf | Table: %1\r\n
0xb0000bd0 | Failed to commit transaction, attempting rollback recovery (error %1, session %2)\r\n
0xb0000bd1 | Failed to rollback transaction (error %1, session %2)\r\n
0xb0000bd2 | Recovery complete (error %1, session %2)\r\n
0xb0000bd3 | Failed to open table handle\r\n
0xb0000bd4 | Unified Store RPC Call: %1\r\n
0xb0000bd5 | Failed to set property ID %1, error %2\r\n
0xb0000bd6 | Process %1 underflowed its suspend/resume count, now is %2\r\n
0xb0000bd7 | Process %1 suspended its message queue, count %2\r\n
0xb0000bd8 | Process %1 resumed its message queue, count %2\r\n
0xb0000bd9 | Process with rundown identifier %1 aborted %2 transactions\r\n
0xb0000bda | Client process %1 has lost events\r\n
0xb0000bdb | Client process %1 has resumed fetching events\r\n
0xb0000bdc | Property should be added in schema. table: %1, id: %2\r\n
0xb0000bdd | Advisee in service process (vtable %1) has lost events\r\n
0xb0000bde | Notification Queue lost events\r\n
0xb0000bdf | Final transaction rollback attempt failed, Error: %1\r\n
0xb0000be0 | Closing active table id: %1\r\n
0xb0000be3 | Unified store process identifier %1 created for process\r\n
0xb0000be4 | Process exit callback for process with identifier %1\r\n
0xb0000be5 | Unified store rundown for process %1 with identifier %2\r\n
0xb0000be6 | Store id: %1 Supported Types changed to: %2\r\n
0xb0000be7 | DBSession::_UpgradeDatabase Error: %1\r\n
0xb0000be8 | JetAttachDatabase Error: %1\r\n
0xb0000be9 | Upgrading database, lcidChanged: %1, storeVersionChanged: %2, isIndexCorrupt: %3\r\n
0xb0000bea | Creating Missing indexes, table ID: %1, count: %2\r\n
0xb0000beb | Number of indexes changed unexpectedly, table ID: %1, numExistingIndex: %2\r\n
0xb0000bec | The database was corrupted, and recovered\r\n
0xb0000bed | Simulation of database corruption\r\n
0xb0000bfe | Attempting to defragment scope knowledge. Partner id: %1, scope id: %2, exceptions: %3 positive and %4 negative, min vector size: %5, max vector size: %6, starting tick count: %7\r\n
0xb0000bff | Defragmented scope knowledge. Partner id: %1, scope id: %2, original size: %3, defragmented size: %4, exceptions: %5\r\n
0xb0000c00 | Done defragmenting scope knowledge. Partner id: %1, scope id: %2, succeeded: %3\r\n
0xb0000c01 | Attempting to defragment partner knowledge. Partner id: %1, size: %2, defragmentation threshold: %3\r\n
0xb0000c02 | The knowledge for partner id %1 has %2 scopes, %3 positive exceptions, %4 negative exceptions, min vector size: %5 and max vector size: %6\r\n
0xb0000c03 | Successfully defragmented %2 scopes out of %3 for partner id %1.\r\n
0xb0000c04 | Defragmented partner knowledge. Partner id: %1, original size: %2, defragmented size: %3\r\n
0xb0000c05 | Done defragmenting partner knowledge. Partner id: %1, succeeded: %2\r\n
0xb0000c06 | Failed to reduce the knowledge size for partner id %1 below %2%% of the maximum size (size: %3, maximum size: %4).\r\n
0xb0000c07 | The knowledge size for partner id %1 exceeds %3%% of the maximum size (size: %2, maximum size: %4). The synchronization may exhibit degraded performance\r\n
0xb0000c08 | The knowledge size for partner id %1 exceeds %3%% of the maximum size (size: %2, maximum size: %4). The synchronization may start failing if the knowledge size keeps increasing\r\n
0xb0000c09 | The knowledge size for partner id %1 exceeds the maximum size (size: %2, maximum size: %3). The synchronization will fail\r\n
0xb0000c1c | Closing stale notify context %2 on behalf of rundown id %1\r\n
0xb0000c1d | Closing stale object %2 on behalf of rundown id %1\r\n
0xb0000c26 | [store upgrade] The current store version is %1\r\n
0xb0000c28 | [store upgrade] Performing upgrade task %1\r\n
0xb0000c29 | [store upgrade] %1 appointments updated\r\n
0xd0000001 | UpgradeStoreFilters\r\n
0xd0000002 | UpgradeAppStoreMask\r\n
0xd0000003 | UpgradeApptRemoteId\r\n
0xd0000004 | UpgradeMoveAggregateContactsToDefaultStore\r\n
0xd0000005 | UpgradeMoveUseAppSummaryToCalendar\r\n
0xd0000006 | UpgradeMoveAppAccessModeToCalendar\r\n
0xd0000007 | UpgradeRoomAlbums\r\n
0xd0000008 | UpgradeCalendarColors\r\n
0xd0000009 | UpgradeStoreContactCloak\r\n
0xd000000a | UpgradeStoreChangeTracking\r\n
0xd000000b | UpgradeSmsStoreToCloaked\r\n
0xd000000c | UpgradeStoresWithGroupings\r\n
0xd000000d | UpgradeAppStoreNames\r\n
0xd000000e | UpgradeProductIdToPackageName\r\n
0xd000000f | UpgradeAppEmailCalendarDeleteChangeTracking\r\n
0xd0000010 | UpgradeAppointmentRecurringData\r\n
0xd0000011 | UpgradeRemoveAggregatesWithNoComponents\r\n
0xd0000012 | UpgradeDeviceStoreRequiredTypes\r\n
0xd0000013 | UpgradeStoreDataProtection\r\n
0xd0000014 | UpgradeMeetingTimezones\r\n
0xd0000015 | UpgradeMediaStorageGuid\r\n
0xd0000016 | UpgradeDeviceStoreEnsureNotSuppressed\r\n
0xd0000017 | UpgradeIrmTemplateDescriptions\r\n
0xd0000018 | CleanupChangeTrackingData\r\n
0xd0000019 | UpgradeCalendarWriteAccess\r\n
0xd000001a | UpgradeLastStoreId\r\n
0xd000001b | UpgradeContactDatesToUtcMidnight\r\n
0xd000001c | UpgradeCleanupAggregateContactMismatch\r\n
0xd000001d | UpgradeRemoveUdmAutoResolverSyncPartner\r\n
0xd000001e | UpgradeAddCompletedTaskFlag\r\n
0xd000001f | UpgradeContactMiddleName\r\n
0xd0000020 | UpgradeDefectExternalContactChangeTracking\r\n
0xd0000021 | UpgradeDeleteExternalStore\r\n
0xd0000022 | UpgradeSyncCalendarsToLimited\r\n
