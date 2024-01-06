## davsyncprovider.dll

Path: %SystemRoot%\System32\DavSyncProvider.dll

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
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
0xb0000065 | DavSyncProvider: Ignoring unsolicited item in a multi-get response (id: %1).\r\n
0xb0000066 | DavSyncProvider: Requested item missing from the multi-get response (id: %1).\r\n
0xb0000067 | DavSyncProvider: Handling download result for an existing item (id: %1, tag: %2, status %3, item data available: %4).\r\n
0xb0000068 | DavSyncProvider: The download result for an existing item has successful status and empty data (id: %1, status %2).\r\n
0xb0000069 | DavSyncProvider: Handled download result with item not found status by deleting the local item (id: %1, status: %2).\r\n
0xb000006a | DavSyncProvider: Handled download result for an existing item (id: %1, new tag: %2, result %3).\r\n
0xb000006b | DavSyncProvider: Handling download result for a new item (id: %1, tag: %2, status %3, item data available: %4).\r\n
0xb000006c | DavSyncProvider: The download result for a new item has successful status and empty data (id: %1, status %2).\r\n
0xb000006d | DavSyncProvider: Handled download result for an existing item (id: %1, new tag: %2, result %3).\r\n
0xb000006e | DavSyncProvider: Item added to the download batch (id: %1, server tag: %2, local tag: %3, new item: %4).\r\n
0xb000006f | DavSyncProvider: Collection tag changed, downloading server changes (id: %1, server tag: %2, local tag: %3, session id: %4).\r\n
0xb0000070 | DavSyncProvider: Downloading changed items batch (id: %1, size: %2).\r\n
0xb0000071 | DavSyncProvider: Deleting all local items which no longer exist on the server (collection id: %1, session id: %2).\r\n
0xb0000072 | DavSyncProvider: Local item deleted because it no longer exists on the server (id: %1).\r\n
0xb0000073 | DavSyncProvider: Successfully deleted all local items which no longer exist on the server (collection id: %1, session id: %2).\r\n
0xb0000074 | DavSyncProvider: Successfully downloaded server changes (id: %1, new tag: %2, session id: %3).\r\n
0xb0000075 | DavSyncProvider: Deleting the local collection with id: %1.\r\n
0xb0000076 | DavSyncProvider: Deleted local collection (last collection: %2, id: %1)\r\n
0xb0000077 | DavSyncProvider: Purging the local collection with id: %1.\r\n
0xb0000078 | DavSyncProvider: Purged local collection (id: %1).\r\n
0xb0000079 | DavSyncProvider: Synchronizing the list of collections (session id: %1).\r\n
0xb000007a | DavSyncProvider: Local collection created (collection id: %1, description: %2, session id: %3).\r\n
0xb000007b | DavSyncProvider: Local collection updated (collection id: %1, description: %2, session id: %3).\r\n
0xb000007c | DavSyncProvider: Deleting all local collections which no longer exist on the server (session id: %1).\r\n
0xb000007d | DavSyncProvider: Local collection deleted because it no longer exists on the server (collection id: %1).\r\n
0xb000007e | DavSyncProvider: Successfully deleted all local collections which no longer exist on the server (session id: %1).\r\n
0xb000007f | DavSyncProvider: Successfully synchronized the list of collections (session id: %1).\r\n
0xb0000080 | DavSyncProvider: The property status %1 returned for a null property is invalid and was coreced to 404.\r\n
0xb0000081 | DavSyncProvider: Received a non-successful ctag property response (collection id: %1, status %2).\r\n
0xb0000082 | DavSyncProvider: Uploading change (item id: %1, type: %2).\r\n
0xb0000083 | DavSyncProvider: Uploaded change (item id: %1, type: %2, status: %3).\r\n
0xb0000084 | DavSyncProvider: Deleted successfuly uploaded item because it has the same Uri as a previously downloaded item (item id: %1).\r\n
0xb0000085 | DavSyncProvider: Failed to upload change (item id: %1, retry: %2).\r\n
0xb0000086 | DavSyncProvider: Deleted local tombstone (item id: %1).\r\n
0xb0000087 | DavSyncProvider: Modification change uploaded successfully (item id: %1, tag: %2).\r\n
0xb0000088 | DavSyncProvider: New item uploaded successfully (uid: %1, item id: %2, tag: %3).\r\n
0xb0000089 | DavSyncProvider: Uploading local changes (collection id: %1).\r\n
0xb000008a | DavSyncProvider: Finished uploading the local changes (collection id: %1, uploaded changes: %2).\r\n
0xb00000a1 | DavSyncProvider: Loading CardDav engine.\r\n
0xb00000a2 | DavSyncProvider: Loading CalDav engine.\r\n
0xb00000a6 | DavSyncProvider: Stopping Dav engines.\r\n
0xb00000ab | DavSyncProvider: Failed to fetch attachment, uri hash %1.\r\n
0xb00000ac | DavSyncProvider: Delay uploading item (uri hash: %1) changes.\r\n
0xb00000c9 | DavSyncProvider: [Start Marker] [DavSyncProvider_SPERF_TAG_DAV_ATTACHMENT_FETCHING_START] The attachment fetching\r\n
0xb00000ca | DavSyncProvider: [Stop Marker] [DavSyncProvider_SPERF_TAG_DAV_ATTACHMENT_FETCHING_STOP] The attachment fetching\r\n
0xd0000001 | Addition\r\n
0xd0000002 | Modification\r\n
0xd0000003 | Deletion\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
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
0xb0000065 | DavSyncProvider: Ignoring unsolicited item in a multi-get response (id: %1).\r\n
0xb0000066 | DavSyncProvider: Requested item missing from the multi-get response (id: %1).\r\n
0xb0000067 | DavSyncProvider: Handling download result for an existing item (id: %1, tag: %2, status %3, item data available: %4).\r\n
0xb0000068 | DavSyncProvider: The download result for an existing item has successful status and empty data (id: %1, status %2).\r\n
0xb0000069 | DavSyncProvider: Handled download result with item not found status by deleting the local item (id: %1, status: %2).\r\n
0xb000006a | DavSyncProvider: Handled download result for an existing item (id: %1, new tag: %2, result %3).\r\n
0xb000006b | DavSyncProvider: Handling download result for a new item (id: %1, tag: %2, status %3, item data available: %4).\r\n
0xb000006c | DavSyncProvider: The download result for a new item has successful status and empty data (id: %1, status %2).\r\n
0xb000006d | DavSyncProvider: Handled download result for an existing item (id: %1, new tag: %2, result %3).\r\n
0xb000006e | DavSyncProvider: Item added to the download batch (id: %1, server tag: %2, local tag: %3, new item: %4).\r\n
0xb000006f | DavSyncProvider: Collection tag changed, downloading server changes (id: %1, server tag: %2, local tag: %3, session id: %4).\r\n
0xb0000070 | DavSyncProvider: Downloading changed items batch (id: %1, size: %2).\r\n
0xb0000071 | DavSyncProvider: Deleting all local items which no longer exist on the server (collection id: %1, session id: %2).\r\n
0xb0000072 | DavSyncProvider: Local item deleted because it no longer exists on the server (id: %1).\r\n
0xb0000073 | DavSyncProvider: Successfully deleted all local items which no longer exist on the server (collection id: %1, session id: %2).\r\n
0xb0000074 | DavSyncProvider: Successfully downloaded server changes (id: %1, new tag: %2, session id: %3).\r\n
0xb0000075 | DavSyncProvider: Deleting the local collection with id: %1.\r\n
0xb0000076 | DavSyncProvider: Deleted local collection (last collection: %2, id: %1)\r\n
0xb0000077 | DavSyncProvider: Purging the local collection with id: %1.\r\n
0xb0000078 | DavSyncProvider: Purged local collection (id: %1).\r\n
0xb0000079 | DavSyncProvider: Synchronizing the list of collections (session id: %1).\r\n
0xb000007a | DavSyncProvider: Local collection created (collection id: %1, description: %2, session id: %3).\r\n
0xb000007b | DavSyncProvider: Local collection updated (collection id: %1, description: %2, session id: %3).\r\n
0xb000007c | DavSyncProvider: Deleting all local collections which no longer exist on the server (session id: %1).\r\n
0xb000007d | DavSyncProvider: Local collection deleted because it no longer exists on the server (collection id: %1).\r\n
0xb000007e | DavSyncProvider: Successfully deleted all local collections which no longer exist on the server (session id: %1).\r\n
0xb000007f | DavSyncProvider: Successfully synchronized the list of collections (session id: %1).\r\n
0xb0000080 | DavSyncProvider: The property status %1 returned for a null property is invalid and was coreced to 404.\r\n
0xb0000081 | DavSyncProvider: Received a non-successful ctag property response (collection id: %1, status %2).\r\n
0xb0000082 | DavSyncProvider: Uploading change (item id: %1, type: %2).\r\n
0xb0000083 | DavSyncProvider: Uploaded change (item id: %1, type: %2, status: %3).\r\n
0xb0000084 | DavSyncProvider: Deleted successfuly uploaded item because it has the same Uri as a previously downloaded item (item id: %1).\r\n
0xb0000085 | DavSyncProvider: Failed to upload change (item id: %1, retry: %2).\r\n
0xb0000086 | DavSyncProvider: Deleted local tombstone (item id: %1).\r\n
0xb0000087 | DavSyncProvider: Modification change uploaded successfully (item id: %1, tag: %2).\r\n
0xb0000088 | DavSyncProvider: New item uploaded successfully (uid: %1, item id: %2, tag: %3).\r\n
0xb0000089 | DavSyncProvider: Uploading local changes (collection id: %1).\r\n
0xb000008a | DavSyncProvider: Finished uploading the local changes (collection id: %1, uploaded changes: %2).\r\n
0xb00000a1 | DavSyncProvider: Loading CardDav engine.\r\n
0xb00000a2 | DavSyncProvider: Loading CalDav engine.\r\n
0xb00000a6 | DavSyncProvider: Stopping Dav engines.\r\n
0xb00000a8 | DavSyncProvider: Stop syncing Dav account %1 content type: %2.\r\n
0xb00000ab | DavSyncProvider: Failed to fetch attachment, uri hash %1.\r\n
0xb00000ac | DavSyncProvider: Delay uploading item (uri hash: %1) changes.\r\n
0xb00000c9 | DavSyncProvider: [Start Marker] [DavSyncProvider_SPERF_TAG_DAV_ATTACHMENT_FETCHING_START] The attachment fetching\r\n
0xb00000ca | DavSyncProvider: [Stop Marker] [DavSyncProvider_SPERF_TAG_DAV_ATTACHMENT_FETCHING_STOP] The attachment fetching\r\n
0xd0000001 | Addition\r\n
0xd0000002 | Modification\r\n
0xd0000003 | Deletion\r\n
