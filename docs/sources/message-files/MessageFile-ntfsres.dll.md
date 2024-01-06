## ntfsres.dll

Path: %SystemRoot%\system32\ntfsres.dll

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb000000a | NtfsLookupRealAllocation: Vcn %1!I64x!, LowestVcn %2!I64x!, HighestVcn %3!I64x!, AllocationClusters %4!I64x!\r\n
0xb000000b | NtfsAllocateAttribute MaxAlloc for Mft's AttrList IC:%1!p!, Scb:%2!p!\r\n
0xb000000c | FileObject: %1!p!, Scb: %2!p!, StaringVcn: %3!I64x!, ClusterCount: %4!I64x!, Flags: %5!08x!, CcbForWriteExtend: %6!p!\r\n
0xb000000d | NtfsAddAllocation IC:%1!p!, FileObject:%2!p!, Scb:%3!p!, StaringVcn:%4!I64x!, ClusterCount:%5!I64x!, Flags:%6!08x!, CcbForWriteExtend:%7!p!\r\n
0xb000000e | Purge failed: Scb: %1!p!, PurgeOffset: 0x%2!016I64x!\r\n
0xb000000f | Purge failed: Scb: %1!p!, PurgeOffset: 0x%2!016I64x!, PurgeChunkLength: 0x%3!x!\r\n
0xb0000010 | NtfsGetLastVcnForNewMappingPairSize IC:%1!p!, Using LastVcn:%2!4I64x!, InstanceId:%3!x!\r\n
0xb0000011 | Can't find StdInfo in FileRef %1!I64x!\r\n
0xb0000013 | NtfsCreateNonresidentWithValue Create Mft's NonResident Attribute List IC:%1!p!ValueLength:%2!x!, AttrFlags=%3!x!\r\n
0xb0000014 | NtfsAddAttributeAllocation(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, LastVcn %5!I64x!, NewHighestVcn %6!I64x!, PassCount %7!x! - step 6\r\n
0xb0000015 | NtfsAddAttributeAllocation(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, LowestVcn %5!I64x!, HighestVcn %6!I64x!, ALE.LowestVcn %7!I64x! - try to merge backward\r\n
0xb0000016 | NtfsAddAttributeAllocation(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, LowestVcn %5!I64x!, HighestVcn %6!I64x!, ALE.LowestVcn %7!I64x! - after merge backward\r\n
0xb0000017 | NtfsAddAttributeAllocation(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, LowestVcn %5!I64x!, HighestVcn %6!I64x!, ALE.LowestVcn %7!I64x!, PassCount %8!x! - before last merge after step 6\r\n
0xb0000018 | NtfsAddAttributeAllocation(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, LowestVcn %5!I64x!, HighestVcn %6!I64x!, ALE.LowestVcn %7!I64x! - after last merge after step 6\r\n
0xb0000019 | NtfsAddAttributeAllocation(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, MergeSkipCt %5!x! - done\r\n
0xb000001a | NtfsRestartRemoveAttribute FileRef:0x%1!04x!_%2!08x!, BaseFRS:0x%3!012I64x!, Attrib:0x%4!x!\r\n
0xb000001b | NtfsRestartChangeValue FileRef:0x%1!04x!_%2!08x!, BaseFRS:0x%3!012I64x!, Attrib:0x%4!x!\r\n
0xb000001c | AddToAttributeList(%1!p!,%2!p!): FRef %3!I64x!, OldSig %4!x!, OldLCS %5!x!, NewLCS %6!x!\r\n
0xb000001d | DeleteFromAttributeList(%1!p!,%2!p!): FRef %3!I64x!, OldSig %4!x!, OldLCS %5!x!, NewLCS %6!x!\r\n
0xb000001e | MakeRoomForAttribute Moving Mft's attribute IC:%1!p!, Moving Attrib %2!x!/%3!x!, Type=%4!x!, RecLengh=%5!x!, Instance:%6!x!\r\n
0xb000001f | MoveAttributeToOwnRecord Moving Mft's $BITMAP IC:%1!p!, SizeNeeded:%2!x!, TypeCode:%3!x!, RecLen:%4!x!, Form:%5!x!, Instance:%6!x!\r\n
0xb0000020 | MoveAttributeToOwnRecord IC:%1!p!, SizeNeeded:%2!x!, Bytes2Free:%3!x!, OldMappingSize:%4!x!, NewMappingSize:%5!x!\r\n
0xb0000021 | NtfsRestartZeroEndOfFileRecord FileRef:0x%1!04x!_%2!08x!, BaseFRS:0x%3!012I64x!, Start:0x%4!x!, Len:0x%5!x!\r\n
0xb0000022 | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, TypeCode %5!x!, AttrName %6!S!, LowVcn %7!I64x!, HalfWayVcn %8!I64x!, FinalVcn %9!I64x!, PackedMode %10!x!, TryPrior %11!x! - about to merge\r\n
0xb0000023 | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, TypeCode %5!x!, AttrName %6!S!, DeleteFileRef %7!x!0000%8!08x!, LowVcn %9!I64x!, LastVcn %10!I64x!, FinalVcn %11!I64x! - all fit in one so get rid of the second one\r\n
0xb0000024 | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, TypeCode %5!x!, AttrName %6!S!, DeleteFileRef %7!x!0000%8!08x!, LowVcn %9!I64x!, LastVcn %10!I64x!, FinalVcn %11!I64x! - should all fit into one so get rid of the second one FIRST\r\n
0xb0000025 | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, Vcn %5!I64x! - initial RangePtr query\r\n
0xb0000026 | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, Vcn %5!I64x!, Rptr %6!p! - secondary RangePtr query\r\n
0xb0000027 | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, Vcn %5!I64x!, Rptr %6!p! - calling lookup runs range\r\n
0xb0000028 | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, McbArray %5!p! (%6!I64x!, %7!I64x!) - current McbArray\r\n
0xb0000029 | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, McbArray %5!p! (%6!I64x!, %7!I64x!) - previous McbArray\r\n
0xb000002a | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, McbArray %5!p! (%6!I64x!, %7!I64x!) - prev prev McbArray\r\n
0xb000002b | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, McbArray %5!p! (%6!I64x!, %7!I64x!) - next McbArray\r\n
0xb000002c | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, NewFinalVcnInMcb %5!I64x! > NewFinalVcn %6!I64x! - NewFinalVcn is smaller\r\n
0xb000002d | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, NewStartVcn %5!I64x!, LastVcn %6!I64x!, NewFinalVcn %7!I64x!, NewFinalVcnInMcb %8!I64x!, #Ranges %9!x!, DeletedNextAttribute %10!x!, Mcb1(%11!x!,%12!x!), Mcb2(%13!x!,%14!x!), McbArraySizeInUseChange %15!d! - final vcn in mcb\r\n
0xb000002e | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, StartingVcn %5!I64x!, EndingVcn %6!I64x! - redefined mcb range1\r\n
0xb000002f | MergeFRS2(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, StartingVcn %5!I64x!, EndingVcn %6!I64x! - redefined mcb range2\r\n
0xb0000030 | RedoAttribute(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, TypeCode %5!x!, AttrName %6!S!, FileRef %7!I64x!, OldLowVcn %8!I64x!, NewLowVcn %9!I64x!, Instance %10!x! - updating LowestVcn in attribute list entry\r\n
0xb0000031 | RedoAttribute(%1!p!,%2!p!): Scb %3!p!, FileRef %4!I64x!, TypeCode %5!x!, AttrName %6!S!, OldLowVcn %7!I64x!, NewLowVcn %8!I64x!, OldHighVcn %9!I64x!, NewHighVcn %10!I64x!, ChildRef %11!x!0000%12!08x! - done\r\n
0xb0000032 | NtfsConsolidateAllFileRecords: Invalid Vcb. Thread: %1!p!.\r\n
0xb0000033 | NtfsConsolidateAllFileRecords: Volume is locked. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Volume Id: %5!S!, Vcb State: 0x%6!08x!.\r\n
0xb0000034 | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x!, FirstRequest %5!x! - opened fcb\r\n
0xb0000035 | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x! - already in progress so get out\r\n
0xb0000036 | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x! - set in progress flag\r\n
0xb0000037 | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x!, RstrTypeCode %5!x!, RstrAttrName %6!S!, RstrVcn %7!I64x!, RstrAttrListEntryOffset %8!x!, AttrListEntryOffset %9!x!, AttrListLength %10!I64x!, AttrListGrowBy %11!x!(%12!d!) - adjust FinalCompactedSizeDeduction\r\n
0xb0000038 | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x!, TypeCode %5!x!, AttrName %6!S!, Vcn %7!I64x!, Instance %8!x!, RstrAttrListEntryOffset %9!x!, AttrListLength %10!I64x! - breaking up 1\r\n
0xb0000039 | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x!, TypeCode %5!x!, AttrName %6!S!, Vcn %7!I64x!, Instance %8!x!, RstrAttrListEntryOffset %9!x!, AttrListLength %10!I64x! - breaking up 2\r\n
0xb000003a | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x!, Scb %5!p! - completed this Scb\r\n
0xb000003b | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x! - going into finally\r\n
0xb000003c | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): FileRef %3!I64x!, Status %4!x! - Abnormal Termination\r\n
0xb000003d | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x! - decremented close counts\r\n
0xb000003e | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x! - clearing in progress flag\r\n
0xb000003f | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x!, ExceptionStatus %5!x!- released\r\n
0xb0000040 | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): Fcb %3!p!, FileRef %4!I64x!, RemovedFcb %5!x!, AllFlags.FcbAcquired %6!x!, TransId %7!x! - no release\r\n
0xb0000041 | NtfsConsolidateAllFileRecords(%1!p!,%2!p!): DeltaTime %3!I64d! (ms), TotalTime %4!I64d! (ms)\r\n
0xb0000042 | UpdateLCS: Vcb %1!p!, IC %2!p!, FRef %3!I64x!, OldSig %4!x!, OldLCS %5!x!, NewLCS %6!x!\r\n
0xb0000043 | NtfsAllocateClustersPriv IC: %1!p!, Vcb: %2!p!, Scb: %3!p!, Mcb: %4!p!, Vcn: 0x%5!I64x!, Length: 0x%6!I64x!, AllocateAll: %7!S!, TargetLcn: 0x%8!I64x!, PreAllocated: %9!S!, DelayedAllocation: %10!S!\r\n
0xb0000045 | NtfsAllocateClustersPriv: Incremented TotalAllocated by 0x%1!I64x! clusters, Scb: %2!p!, TotalAllocated: 0x%3!I64x!\r\n
0xb0000046 | NtfsAllocateClustersPriv: Skipped incrementing TotalAllocated by 0x%1!I64x! clusters, Scb: %2!p!, TotalAllocated: 0x%3!I64x!ScbState: %4!08x!, IrpContextState2: %5!08x!, AllocateWithNoHole: %6!d!\r\n
0xb0000047 | NtfsAllocateClustersPriv IC: %1!p!, ClustersAllocated: %2!S!\r\n
0xb0000049 | NtfsDeallocateClusters IC: %1!p!, Vcb: %2!p!, Scb: %3!p!, Mcb: %4!p!, StartVcn: 0x%5!I64x!, EndVcn: 0x%6!I64x!\r\n
0xb000004a | NtfsDeallocateClusters: Vcb %1!p! - deleting FR %2!I64x! from clusters %3!I64x! to %4!I64x!\r\n
0xb000004c | NtfsDeallocateClusters: Vcb %1!p! - deleting FR %2!I64x! starting at %3!I64x! for %4!I64x! clusters\r\n
0xb000004d | NtfsDeallocateClusters: Vcb %1!p! - raising logfile full\r\n
0xb000004e | NtfsDeallocateClusters: Vcb %1!p! - adding clusters to DeallocatedClusters: %2!p! ==> Lsn: %3!I64x!, ClusterCount: %4!I64x!, Flags: %5!08x!; Vcb's DeallocatedClustersCount old: %6!I64x! new: %7!I64x!\r\n
0xb000004f | NtfsDeallocateClusters: Decremented TotalAllocated by 0x%1!I64x! clusters, Scb: %2!p!, TotalAllocated: 0x%3!I64x!Addr(TotalAllocated): %4!p!\r\n
0xb0000050 | NtfsDeallocateClusters: Skipped decrementing TotalAllocated by 0x%1!I64x! clusters, Scb: %2!p!Addr(TotalAllocated): %3!p!, ScbState: %4!08x!, IrpContextState2: %5!08x!\r\n
0xb0000051 | NtfsDeallocateClusters: Vcb %1!p! - Undoing some changes to DeallocatedClustersCount from %2!I64x! to %3!I64x!\r\n
0xb0000052 | NtfsDeallocateClusters IC: %1!p!, ClustersDeallocated: %2!S!\r\n
0xb0000054 | NtfsModifyBitsInBitmap IC: %1!p!, Vcb: %2!p!, FirstBit: 0x%3!I64x!, BeyondLastBit: 0x%4!I64x!, Redo: 0x%5!x!, Undo: 0x%6!x!\r\n
0xb0000055 | NtfsModifyBitsInBitmap IC: %1!p!, Bitmap: %2!p!, BaseLcn: 0x%3!I64x!, CurrentLcn: 0x%4!I64x!\r\n
0xb0000056 | NtfsAllocateBitmapRun IC: %1!p!, Vcb: %2!p!, StartingLcn: 0x%3!I64x!, ClusterCount: 0x%4!I64x!\r\n
0xb0000057 | NtfsAllocateBitmapRun IC: %1!p!, Bitmap: %2!p!, BaseLcn: 0x%3!I64x!, StartingLcn: 0x%4!I64x!\r\n
0xb0000058 | NtfsRestartSetBitsInBitMap IC: %1!p!, Bitmap: %2!p!, BitMapOffset: 0x%3!08x!, NumBits: 0x%4!08x!\r\n
0xb0000059 | NtfsFreeBitmapRun IC: %1!p!, Vcb: %2!p!, StartingLcn: 0x%3!I64x!, ClusterCount: 0x%4!I64x!\r\n
0xb000005a | NtfsFreeBitmapRun IC: %1!p!, Bitmap: %2!p!, BaseLcn: 0x%3!I64x!, StartingLcn: 0x%4!I64x!\r\n
0xb000005b | NtfsRestartClearBitsInBitMap IC: %1!p!, Bitmap: %2!p!, BitMapOffset: 0x%3!08x!, NumBits: 0x%4!08x!\r\n
0xb000005c | NtfsSetOrClearBitsUsingBaseMcb IC: %1!p!, Vcb: %2!p!, Bitmap: %3!p!, StartingBitmapLcn: 0x%4!I64x!, SetBits: %5!S!\r\n
0xb000005d | NtfsSetOrClearBitsUsingBaseMcb IC: %1!p!, Bitmap: %2!p!, StartLcn: 0x%3!I64x!, EndLcn: 0x%4!I64x!\r\n
0xb000005e | NtfsSetOrClearBitsUsingBaseMcb IC: %1!p!, Result: %2!S!\r\n
0xb000005f | System files not marked as in use in the MFT bitmap.  DWord offset %1!x!, value %2!x!.\r\n
0xb0000060 | Length:        0 --> BinIndex :        0    - Unexpected length\r\n
0xb0000061 | Length: %1!8I64d! --> BinIndex : %2!8u!    - Key: %3!u!, BitPosition: %4!ld!, GroupIndex: %5!ld!, GroupShiftFactor: %6!ld!\r\n
0xb0000062 | Length: %1!8I64d! --> BinIndex : %2!8u!    - BinIndex was beyond TotalBins: %3!u! hence brought down\r\n
0xb0000063 | BinIndex: %1!8u! --> MaxLength: %2!8I64d!  - BinIndex is set to last bin or beyond, TotalBins: %3!u!\r\n
0xb0000064 | BinIndex: %1!8u! --> MaxLength: %2!8I64d!  - GroupIndex: %3!ld!, RelativeBinIndex: %4!ld!, MaxKey: %5!u!\r\n
0xb0000065 | BinGroupShift: %1!8ld!, BinGroupSize: %2!8u!, BinGroupMask: %3!8x!\r\n
0xb0000066 | BinIndex: %1!8u! --> MaxLength: %2!8I64u! (0x%3!8I64x!)\r\n
0xb0000067 | Searched committed allocations but didnt find enough free space.  StartingCluster %1!I64x!, ClusterCount %2!I64x!, Committed %3!I64x!, Total %4!I64x!, Free %5!I64x!\r\n
0xb0000068 | NtfsRemoveClustersFromTPMap: Vcb %1!p! - Clearing TP map bit(s): first bit 0x%2!X!, last bit 0x%3!X!\r\n
0xb0000069 | NtfsRemoveClustersFromTPMap: Vcb %1!p! - Clearing TP map bit(s): no leading partial slab\r\n
0xb000006a | NtfsRemoveClustersFromTPMap: Vcb %1!p! - Clearing TP map bit(s): leading partial slab returned - LCN %2!I64X!, len %3!I64X!\r\n
0xb000006b | NtfsRemoveClustersFromTPMap: Vcb %1!p! - Clearing TP map bit(s): no trailing partial slab\r\n
0xb000006c | NtfsRemoveClustersFromTPMap: Vcb %1!p! - Clearing TP map bit(s): trailing partial slab returned - lcn %2!I64X!, len %3!I64X!\r\n
0xb000006d | NtfsValidateTotalClustersCommitted(%1!p!,%2!p!): TCC %3!I64x!, TC %4!I64x!, BMSize %5!x!\r\n
0xb000006e | Illegal MDL Complete for major code %1!u!\r\n
0xb000006f | Entering: Scb: %1!p!, StartingZero: 0x%2!016I64x!, ByteCount: 0x%3!016I64x!, ExtentsDescriptor: %4!p!, ExtentsDescriptorIndex: %5!d!, ExtentsDescriptorStartOffset: 0x%6!016I64x!, Offset: 0x%7!016I64x!, MaxRuns: %8!d!,\r\n
0xb0000070 | RunEntry ==> %1!4d!: [0x%2!016I64x!, 0x%3!016I64x!], ExtentLength: 0x%4!016I64x!, Offset: 0x%5!016I64x!, RunIndexStartOffset: 0x%6!016I64x!\r\n
0xb0000071 | Offset is beyond this extent skipping the extent.\r\n
0xb0000072 | Shrinking LengthInExtent (0x%1!016I64x!) to ByteCount (0x%2!016I64x!) that we have to zero\r\n
0xb0000073 | Zeroing: StartingPhysicalAddr: 0x%1!016I64x!, LengthInExtent: 0x%2!016I64x!\r\n
0xb0000074 | Exiting: ExtentsDescriptorIndex: %1!d! ExtentsDescriptorStartOffset: 0x%2!016I64x!\r\n
0xb0000075 | Entering: Scb: %1!p!, StartingZero: 0x%2!016I64x!, BeyondEndOffset: 0x%3!016I64x!\r\n
0xb0000076 | Dsm Ranges[%1!d!]: StartingOffset: 0x%2!016I64x!, LengthInBytes: 0x%3!016I64x!\r\n
0xb0000077 | RemainingClusterCount: 0x%1!I64x!, DataSetRangeIndex: %2!d!\r\n
0xb0000078 | Dsm: TotalNumberOfRanges: %1!d!, NumberOfRangesReturned: %2!d!\r\n
0xb0000079 | DsmOut Ranges[%1!d!]: StartingAddress: 0x%2!016I64x!, LengthInBytes: 0x%3!016I64x!\r\n
0xb000007b | Updating ExtentsDescriptor Index and StartOffset from Locals: ExtentsDescriptorIndex: %1!d!, ExtentsDescriptorStartOffset: 0x%2!016I64x!\r\n
0xb000007c | Entering: Scb: %1!p!, StartingZero: 0x%2!016I64x!, BeyondEndOffset: 0x%3!016I64x!, ByteCount: 0x%4!016I64x!, ExtentsDescriptor: %5!p!, ExtentsDescriptorIndex: %6!d!, ExtentsDescriptorStartOffset: 0x%7!016I64x!\r\n
0xb000007e | IrpContext: %1!p!; Scb: %2!p!; StartOffset: 0x%3!I64x!; ByteCount: 0x%4!x!\r\n
0xb000007f | Return. IrpContext: %1!p!\r\n
0xb0000080 | Unexpected open type received: %1!u!\r\n
0xb0000081 | Raising STATUS_SUCCESS from NtfsCommonCleanup: %1!S!\r\n
0xb0000082 | Raising STATUS_SUCCESS from NtfsCommonCleanup: 0x%1!X!\r\n
0xb0000084 | Irp: %1!p!, IC: %2!p!, Vcb: %3!p!, FileObject: %4!p!, RelatedFileObject: %5!p!, FileIdBuffer: %6!S!, Options: 0x%7!08x!, FileAttributes: 0x%8!04x!, ShareAccess: 0x%9!04x!, EaLength: 0x%10!08x!\r\n
0xb0000085 | Irp: %1!p!, IC: %2!p!, Vcb: %3!p!, FileObject: %4!p!, RelatedFileObject: %5!p!, Path: %6!S!, Options: 0x%7!08x!, FileAttributes: 0x%8!04x!, ShareAccess: 0x%9!04x!, EaLength: 0x%10!08x!\r\n
0xb0000086 | NtfsCommonCreate: Volume is locked or we have performed a dismount. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Vcb State: %5!x!.\r\n
0xb0000087 | NtfsCommonVolumeOpen: Invalid create disposition for volume open. Thread: %1!p!, CreateDisposition: 0x%2!x!.\r\n
0xb0000088 | NtfsCommonVolumeOpen: Volume is locked or we have performed a dismount. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Vcb State: 0x%5!08x!.\r\n
0xb0000089 | NtfsCommonVolumeOpen: Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Requested ShareAccess: 0x%5!08x!, Vcb->CleanupCount: %6!d!, BiasedCleanupCount: %7!d!.\r\n
0xb000008a | NtfsCommonVolumeOpen: Volume is locked or we have performed a dismount.Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Vcb State: 0x%5!08x!.\r\n
0xb000008b | NtfsCommonVolumeOpen: Conlicting file objects. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Requested ShareAccess: 0x%5!08x!, Vcb->ReadOnlyCloseCount: %6!d!, Vcb->CloseCount: %7!d!, Vcb->SystemFileCloseCount: %8!d!.\r\n
0xb000008c | NtfsHandlePagingFile: Paging file already open, paging files can only be opened once. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Fcb->CleanupCount: %7!d!, Fcb->FcbState: 0x%8!08x!, IrpSp->Flags: 0x%9!08x!.\r\n
0xb000008d | NtfsHandlePagingFile: Cannot open system file as paging file. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Fcb->FcbState: 0x%7!08x!, IrpSp->Flags: 0x%8!08x!.\r\n
0xb000008e | NtfsHandlePagingFile: Persisted paging file already exists. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, IrpContext->State: 0x%7!08x!, IrpSp->Flags: 0x%8!08x!.\r\n
0xb000008f | NtfsOpenFcbById: Invalid system file access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!, CreateDisposition: 0x%8!08x!, DesiredAccess: 0x%9!08x!.\r\n
0xb0000090 | NtfsOpenExistingPrefixFcb: Can not directly open txf directory. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FileAttributes: 0x%7!08x!, Rmstate: 0x%8!08x!.\r\n
0xb0000091 | NtfsOpenExistingPrefixFcb: Invalid system file access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!, CreateDisposition: 0x%8!08x!, DesiredAccess: 0x%9!08x!.\r\n
0xb0000092 | NtfsOpenFile: Unsafe to acquire parent directory after acquiring a txf-system file. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!.\r\n
0xb0000093 | NtfsOpenFile: Invalid system file access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!, CreateDisposition: 0x%8!08x!, DesiredAccess: 0x%9!08x!.\r\n
0xb0000094 | NtfsOpenFile: Deny open when txf rm is active. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, TxfRmcb Rmstate: 0x%7!08x!.\r\n
0xb0000095 | NtfsCreateNewFile: Deny creation in system directory (except root). Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, (Parent Fcb): Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!, TxfRmcb state: 0x%8!08x!, AttrTypeCode: 0x%9!x!.\r\n
0xb0000096 | NtfsCreateNewFile: Unable to create Ea for the file. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Create options: 0x%7!08x!, Ccb flags: 0x%8!08x!.\r\n
0xb0000097 | NtfsCreateNewFile: Unable to create in the $txf directory. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, (Parent Fcb) Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!, TxfRmcb state: 0x%8!08x!.\r\n
0xb0000098 | NtfsOpenSubdirectory: Denying access to $Txf file when the RM is active. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, TxfRmcb state: 0x%7!08x!.\r\n
0xb0000099 | NtfsOpenAttributeInExistingFile: Denying access due to caller being Ea blind. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, NeedEaCount: %7!d!, CreateOptions: 0x%8!08x!, CcbFlags: 0x%9!08x!.\r\n
0xb000009a | NtfsOpenAttributeInExistingFile: Fail to find $INDEX_ROOT attribute. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, AttrTypeCode to create: 0x%7!x!, CreateDisposition: 0x%8!08x!.\r\n
0xb000009b | NtfsOpenAttributeInExistingFile: Denying access for volume root directory. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, CreateDisposition: 0x%7!08x!.\r\n
0xb000009c | NtfsCreateNewFile: Not allowed to create streams on system files. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!, AttrTypeCode: 0x%8!x!.\r\n
0xb000009d | NtfsOverwriteAttr: Cannot overwrite hidden or system attribute for a non-paging file. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, DuplicateInfo attributes: 0x%7!08x!, FileAttributes: 0x%8!08x!.\r\n
0xb000009e | NtfsOverwriteAttr: Denying access due to user being Ea blind. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Create options: 0x%7!08x!.\r\n
0xb000009f | NtfsOverwriteAttr: Deny access due to encryption happening on the stream. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, AttributeTypeCode: 0x%7!x!, Scb state: 0x%8!08x!, Scb HighWaterMark: %9!I64d!.\r\n
0xb00000a0 | NtfsCheckValidAttributeAccess: Supersede or overwrite is not allowed on this type of named attribute. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, AttributeTypeCode: 0x%5!x!, CreateDisposition: 0x%6!08x!.\r\n
0xb00000a1 | NtfsCheckValidAttributeAccess: Only read attributes access is supported on this attribute. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, AttributeTypeCode: 0x%5!x!, DesiredAccess: 0x%6!08x!.\r\n
0xb00000a2 | NtfsCheckValidAttributeAccess: Deny access for protected system attributes. Thread: %1!p!, AttributeTypeCode: %2!x!.\r\n
0xb00000a3 | NtfsOpenAttributeCheck: File already has user writable references. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Requested ShareAccess: 0x%10!08x!, Previously granted access: 0x%11!08x!.\r\n
0xb00000a4 | NtfsOpenAttributeCheck: Deny access for online encryption backup data stream. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, AttributeTypeCode: 0x%8!x!, Attribute Name: %9!S!.\r\n
0xb00000a5 | NtfsOpenAttributeCheck: File was granted write access but has image section. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Previously granted access: 0x%10!08x!.\r\n
0xb00000a6 | NtfsOpenAttribute: Denying write access on disallowed writes. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Disallow write count: %8!d!, Desired Access: 0x%9!08x!.\r\n
0xb00000a7 | NtfsOpenAttribute: File already has user writable references. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Requested ShareAccess: 0x%10!08x!, Previously granted access: 0x%11!08x!.\r\n
0xb00000a8 | NtfsOpenAttribute: Open for exclusive read access is not allowed. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Requested share access: 0x%7!08x!, FO flags: 0x%8!08x!.\r\n
0xb00000ab | NtfsCheckExistingFile: Desired access conflicts with read-only state. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Desired Access: 0x%7!08x!, FileAttributes: 0x%8!08x!, SL control flags: 0x%9!08x!.\r\n
0xb00000ac | NtfsOpenExistingEncryptedStream: No encryption driver found. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FileAttributes: 0x%7!08x!, NtfsData flags: 0x%8!08x!.\r\n
0xb00000ad | NtfsOpenExistingEncryptedStream: Opening for read/write access not allowed on compressed file. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FileAttributes: 0x%7!08x!, Stream attribute flags: 0x%8!08x!.\r\n
0xb00000ae | NtfsEncryptionCreateCallback: Encrytion engine fail to encrypt all streams for file with open handle. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Fcb cleanup count: %7!d!, EncryptionCallBackTable flags: 0x%8!08x!.\r\n
0xb00000af | NtfsFindStartingNode: Opening not allowed for txf name when RM is active. Thread: %1!p!, Fcb: %2!p!, FileRef: 0x%3!I64x!, TxfRmcb RM state: %4!x!.\r\n
0xb00000b0 | NtfsCheckShareAccess: IoCheckLinkShareAccess failed with sharing violation. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Link Name: %7!S!, DesiredAccess: 0x%8!08x!, DesiredShareAccess: 0x%9!08x!, IoShareAccessFlags: 0x%10!08x!, LinkShareAccess->OpenCount: %11!d!, LinkShareAccess->Deleters: %12!d!, LinkShareAccess->SharedDelete: %13!d!.\r\n
0xb00000b1 | NtfsCheckShareAccess: IoCheckLinkShareAccess failed with sharing violation. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb Type Code: 0x%7!x!, Scb Name: %8!S!, DesiredAccess: 0x%9!08x!, DesiredShareAccess: 0x%10!08x!, IoShareAccessFlags: 0x%11!08x!, ShareAccess->OpenCount: %12!d!, ShareAccess->Readers: %13!d!, ShareAccess->Writers: %14!d!, ShareAccess->->Deleters: %15!d!, ShareAccess->SharedRead: %16!d!, ShareAccess->SharedWrite: %17!d!, ShareAccess->SharedDelete: %18!d!.\r\n
0xb00000b2 | NtfsCheckShareAccess: IoCheckLinkShareAccess failed with sharing violation. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb Type Code: 0x%7!x!, Scb Name: %8!S!, Link Name: %9!S!, DesiredAccess: 0x%10!08x!, DesiredShareAccess: 0x%11!08x!, IoShareAccessFlags: 0x%12!08x!, ShareAccess->OpenCount: %13!d!, ShareAccess->Readers: %14!d!, ShareAccess->Writers: %15!d!, ShareAccess->->Deleters: %16!d!, ShareAccess->SharedRead: %17!d!, ShareAccess->SharedWrite: %18!d!, ShareAccess->SharedDelete: %19!d!, LinkShareAccess->OpenCount: %20!d!, LinkShareAccess->Deleters: %21!d!, LinkShareAccess->SharedDelete: %22!d!.\r\n
0xb00000b3 | NtfsReCheckShareAccess: Does not meet allow open requirement. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb Type Code: 0x%7!x!, Scb Name: %8!S!, Link Name: %9!S!, Previously granted access: 0x%10!08x!, AccessState->Flags: 0x%11!08x!, DesiredShareAccess: 0x%12!08x!, CreateDisposition: 0x%13!08x!, OpenCount: %14!d!, Readers: %15!d!, Writers: %16!d!, Deleters: %17!d!, SharedRead: %18!d!, Lcb Deleters: %19!d!.\r\n
0xb00000b4 | %1!S!:%2!d! Status: %3!S! ProcessName: %4!S!\r\n
0xb00000b8 | NtfsSendUnusedClustersHint: Vcb %1!p! - Will tell storage we are freeing at %2!I64x! for %3!x! clusters\r\n
0xb00000b9 | NtfsSendUnusedClustersHint: Vcb %1!p! - Flush requested\r\n
0xb00000ba | NtfsSendUnusedClustersHint: Vcb %1!p! -  Created new MarkUnusedContext %2!p!, DEALLOCATED_CLUSTERS %3!p!, MCB %4!p!\r\n
0xb00000bb | NtfsSendUnusedClustersHint: Vcb %1!p! - Successfully added clusters starting at %2!I64x! for %3!x! into MCB %4!p!\r\n
0xb00000bc | NtfsSendUnusedClustersHint: Vcb %1!p! - MCB %2!p! is full\r\n
0xb00000bd | NtfsSendUnusedClustersHint: Vcb %1!p! - Queuing request to IC pre-trim list, MUC %2!p!, IC %3!p!\r\n
0xb00000be | NtfsSendUnusedClustersHint: Vcb %1!p! -  Failed to allocate/initial MarkUnusedContext\r\n
0xb00000bf | NtfsTransferMaxDataSetRanges: Src %1!p!, Dst %2!p!, SrcRemainClusCt %3!I64x!, SrcOrigClusCt %4!I64x!, SrcDSRL %5!x! - Entering\r\n
0xb00000c0 | NtfsTransferMaxDataSetRanges: Src %1!p!, Dst %2!p!, SrcRemainClusCt %3!I64x!, DstClusCt %4!I64x!, DstDSRL %5!x!, DstLIB %6!I64x!, DstSOff %7!I64x! - Leaving\r\n
0xb00000c1 | NtfsMarkUnusedContextPostTrimProcessing: Entering\r\n
0xb00000c2 | NtfsMarkUnusedContextPostTrimProcessing: Vcb %1!p!, MUC %2!p! - DC %3!I64x!, DCIT %4!x!, DCTD %5!x!, CC %6!I64x!, IR %7!x!\r\n
0xb00000c3 | NtfsMarkUnusedContextPostTrimProcessing: Vcb %1!p!, MUC %2!p! - Removed interior slab(s) from TP map - [LCN %3!I64X!, len %4!I64X!] => [LCN %5!I64X!, len %6!I64X!], [LCN %7!I64X!, len %8!I64X!]\r\n
0xb00000c4 | NtfsMarkUnusedContextPostTrimProcessing: Vcb %1!p! - Releasing bitmap\r\n
0xb00000c5 | NtfsMarkUnusedContextPostTrimProcessing: Vcb %1!p! - CloseCount %2!x!\r\n
0xb00000c6 | NtfsMarkUnusedContextPostTrimProcessing: Vcb %1!p! - failed to try deleting Vcb\r\n
0xb00000c7 | NtfsMarkUnusedContextPostTrimProcessing: Leaving\r\n
0xb00000c8 | NtfsAsyncSendUnusedClustersHintCompletionRoutine: Irp %1!p!\r\n
0xb00000c9 | NtfsMarkUnusedContextPreTrimProcessing: Vcb %1!p!, IC %2!p! - Entering\r\n
0xb00000ca | NtfsMarkUnusedContextPreTrimProcessing: Vcb %1!p! - Kicked off DelayedWorkQueue\r\n
0xb00000cb | NtfsMarkUnusedContextPreTrimProcessing: Vcb %1!p! - Leaving\r\n
0xb00000cc | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Entering Vcb %1!p!\r\n
0xb00000cd | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Vcb %1!p! - Small MUC %2!p! instead of MUC %3!p!\r\n
0xb00000ce | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Vcb %1!p! - Failed to allocate small MUC so use MUC %2!p!\r\n
0xb00000cf | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Vcb %1!p! - Sending storage ioctl down.  MUC %2!p!\r\n
0xb00000d0 | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Vcb %1!p!, MUC %2!p! - [%3!x!] Offset %4!I64x!, Length %5!I64x! - trim entry\r\n
0xb00000d1 | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Vcb %1!p!, MUC %2!p!, Irp %3!p! - Completed\r\n
0xb00000d2 | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Vcb %1!p!, MUC %2!p! - %3!x! - failed to send\r\n
0xb00000d3 | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Vcb %1!p! - Add MUC %2!p! to post trim list\r\n
0xb00000d4 | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Vcb %1!p! - Free small MUC %2!p!\r\n
0xb00000d5 | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Vcb %1!p! - Sending storage ioctl down failed with %2!x!.  MUC %3!p!, Count %4!I64x!\r\n
0xb00000d6 | NtfsMarkUnusedContextPreTrimWorkItemProcessing: Leaving\r\n
0xb00000d7 | NtfsWakeupDeallocatedClustersWaiters: Vcb %1!p! - There are waiters for DC %2!p!\r\n
0xb00000d8 | NtfsWakeupDeallocatedClustersWaiters: Vcb %1!p! - Waking up waiter for DC %2!p!\r\n
0xb00000d9 | NtfsWakeupDeallocatedClustersWaiters: Vcb %1!p! - Done waking up DC %2!p!\r\n
0xb00000da | NtfsWaitForDeallocatedClustersToDrain: Vcb %1!p!, All %2!x! - Entering\r\n
0xb00000db | NtfsWaitForDeallocatedClustersToDrain: Vcb %1!p! - Waiting to drain\r\n
0xb00000dc | NtfsWaitForDeallocatedClustersToDrain: Vcb %1!p! - Waiting for partial drain\r\n
0xb00000dd | NtfsWaitForDeallocatedClustersToDrain: Vcb %1!p! - Leaving\r\n
0xb00000de | NtfsPrepareToWaitForDeallocatedClustersToDrain: Vcb %1!p! - Entering\r\n
0xb00000df | NtfsPrepareToWaitForDeallocatedClustersToDrain: Vcb %1!p! - Inserted %2!p!\r\n
0xb00000e0 | NtfsPrepareToWaitForDeallocatedClustersToDrain: Vcb %1!p! - Leaving\r\n
0xb00000e1 | NtfsWaitForDeallocatedClustersToDrainAfterPrepare: Vcb %1!p! - Wait for DC %2!p!\r\n
0xb00000e2 | NtfsWaitForDeallocatedClustersToDrainAfterPrepare: Waited for %1!d! (s), Exceeded by %2!d! (s), IC %3!p!, Vcb %4!p!, DC %5!p!\r\n
0xb00000e4 | NtfsCheckForTrimThrottling: Vcb %1!p! - hitting trim threshold %2!d!\r\n
0xb00000e5 | NtfsUpdateSmartTrimState: Vcb %1!p! - Entering\r\n
0xb00000e6 | NtfsUpdateSmartTrimState: Vcb %1!p! - Precondition checks failed\r\n
0xb00000e7 | NtfsUpdateSmartTrimState: Vcb %1!p! - Precondition checks failed; AcquiredSyncResource %2!u!\r\n
0xb00000e8 | NtfsUpdateSmartTrimState: Vcb %1!p!, MUC %2!p! - Skipping deallocated clusters gen'd by smart trim\r\n
0xb00000e9 | NtfsUpdateSmartTrimState: Vcb %1!p!, MUC %2!p! - MCB run %3!u!; offs 0x%4!I64X!, len 0x%5!I64X!\r\n
0xb00000ea | NtfsUpdateSmartTrimState: Vcb %1!p! - MUC %2!p!, DSR count %3!u!, MCB count %4!u!, ST free slots %5!u!\r\n
0xb00000eb | NtfsUpdateSmartTrimState: Vcb %1!p!, MUC %2!p! - DSR range %3!u!; offs 0x%4!I64X!, len 0x%5!I64X!\r\n
0xb00000ec | NtfsUpdateSmartTrimState: Vcb %1!p! - MCB lcn %2!I64X! len %3!I64X! maps to TP map bits [0x%4!X!, 0x%5!X!]\r\n
0xb00000ed | NtfsUpdateSmartTrimState: Vcb %1!p! - Smart trim state on exit; %2!u! ranges:\r\n
0xb00000ee | NtfsUpdateSmartTrimState: Vcb %1!p! - Range %2!u!: FirstTPMapBit 0x%3!X!, LastTPMapBit 0x%4!X!\r\n
0xb00000ef | NtfsUpdateSmartTrimState: Vcb %1!p! - Leaving\r\n
0xb00000f0 | NtfsEvalSmartTrimState: Vcb %1!p! - Entering\r\n
0xb00000f1 | NtfsEvalSmartTrimState: Vcb %1!p! - Precondition checks failed\r\n
0xb00000f2 | NtfsEvalSmartTrimState: Vcb %1!p! - Precondition checks failed; AcquiredBitmap %2!u!\r\n
0xb00000f3 | NtfsEvalSmartTrimState: Vcb %1!p! - Checking slab 0x%2!X! for allocations\r\n
0xb00000f4 | NtfsEvalSmartTrimState: Vcb %1!p! - Slab 0x%2!X! has allocations, will not trim\r\n
0xb00000f5 | NtfsEvalSmartTrimState: Vcb %1!p! - Free slab found - TP map bit 0x%2!X!, lcn %3!I64X!, len %4!I64X!\r\n
0xb00000f6 | NtfsEvalSmartTrimState: Vcb %1!p! - Leaving\r\n
0xb00000f7 | NtfsCommonDeviceControl: IOCTL_DISK_COPY_DATA is not allowed on unlocked volume. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, VcbState: 0x%5!08x!, SL control flags: 0x%6!08x!.\r\n
0xb00000f8 | NtfsVolumeDasdIo: Data section blocking flush. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Flush status: %5!S!.\r\n
0xb00000f9 | Could not find paging file run.\r\n
0xb00000fa | Could not find paging file MCB entry.\r\n
0xb00000fc | Writing to $Bitmap. Vcb: %1!p!, Offset: 0x%2!I64x!, Length: 0x%3!x!\r\n
0xb00000fd | NTFS: Posting hotfix on file object: %1!p!\r\n
0xb00000fe | NTFS:     Freeing Bad Vcn: %1!08x!, %2!08x!\r\n
0xb00000ff | NTFS:     Retiring Bad Lcn: %1!08x!, %2!08x!\r\n
0xb0000100 | NTFS:     Reallocating Bad Vcn\r\n
0xb0000101 | NTFS:     Bad Cluster replaced\r\n
0xb0000102 | IrpContext: %1!p!; Vcb: %2!p!; NewBufferSize: 0x%3!08x!\r\n
0xb0000103 | Compression buffers are already big enough. NewBufferSize: 0x%1!08x!, ExistingBufferSize: 0x%2!08x!\r\n
0xb0000104 | %1!S!\r\n
0xb0000108 | NtfsDefragFileInternal: Defrag is denied. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Persist flags: 0x%10!08x!, Ccb flags: 0x%11!08x!.\r\n
0xb0000109 | NtfsDefragFileInternal: Vcb %1!p! - Calling FRD\r\n
0xb000010a | NtfsDefragFileInternal: Vcb %1!p! - Done calling FRD\r\n
0xb000010c | NtfsDefragFileInternal(%1!p!,%2!p!): Scb %3!p!, FRef %4!I64x!, Vcn %5!I64x!, CC %6!I64x!, CurrLcn %7!I64x!, NewLcn %8!I64x!, Len %9!x!, DA %10!d!, Status %11!x! - copy offload\r\n
0xb000010d | NtfsDefragFileInternal(%1!p!,%2!p!): Scb %3!p!, FRef %4!I64x!, Vcn %5!I64x!, CC %6!I64x!, CurrLcn %7!I64x!, NewLcn %8!I64x!, Len %9!x!, DA %10!d!, Status %11!x!\r\n
0xb000010e | NtfsDefragFileInternal(%1!p!,%2!p!): Scb %3!p!, FRef %4!I64x!, CurrLcn %5!I64x!, Len %6!x!, Status %7!x! - read completed\r\n
0xb000010f | NtfsDefragFileInternal(%1!p!,%2!p!): Scb %3!p!, FRef %4!I64x!, NewLcn %5!I64x!, Len %6!x!, Status %7!x! - write completed\r\n
0xb0000110 | NtfsDefragFileInternal(%1!p!,%2!p!): Scb %3!p!, FRef %4!I64x!, Vcn %5!I64x!, CC %6!I64x!, CurrLcn %7!I64x!, NewLcn %8!I64x!, DA %9!d!, ValidClusters %10!I64x! - beyond VDL\r\n
0xb0000111 | NtfsDefragFileInternal(%1!p!,%2!p!): Scb %3!p!, FRef %4!I64x!, Vcn %5!I64x!, CC %6!I64x! - committed\r\n
0xb0000112 | NtfsDefragFile: Defrag is denied without manage volume access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Ccb flags: 0x%7!08x!.\r\n
0xb0000113 | NtfsEncryptDecryptOnline: Defrag is denied. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Persist flags: 0x%10!08x!, Ccb flags: 0x%11!08x!.\r\n
0xb0000114 | NtfsEncryptDecryptOnline: Vcb %1!p! - Calling FRD\r\n
0xb0000115 | NtfsEncryptDecryptOnline: Vcb %1!p! - Done calling FRD\r\n
0xb0000117 | SCB: %1!p!, VDL=0x%2!I64x!, FS=0x%3!I64x!, StartOff=0x%4!I64x!, StartVcn=0x%5!I64x!, Length=0x%6!I64x!\r\n
0xb0000118 | StartOff=0x%1!I64x!, Length=0x%2!I64x!, EffectiveLength=0x%3!I64x! StartVcn=0x%4!I64x!, BeyondEndVcn=0x%5!I64x!, Clusters=0x%6!I64x!, LastVcnInFile=0x%7!I64x!\r\n
0xb0000119 | NumberOfValidRuns: 0\r\n
0xb000011a | RemainingClusterCount: 0x%1!I64x!, DataSetRangeIndex: %2!d!, OutputBufferLength: 0x%3!d!\r\n
0xb000011b | STATUS_BUFFER_TOO_SMALL from FsLib. NumberOfValidRuns: 0x%1!x!, MaxRuns: 0x%2!x!, BytesReturned: 0x%3!I64x!\r\n
0xb000011c | Made an educated guess for remaining runs. RemainingClusterCount: 0x%1!I64x!, NumberOfValidRuns: 0x%2!x!\r\n
0xb000011d | Made a wild guess for remaining runs. RemainingClusterCount: 0x%1!I64x!, NumberOfValidRuns: 0x%2!x!\r\n
0xb000011e | NumberOfValidRuns: 0x%1!08x!, MaxRuns: 0x%2!08x!, Status: 0x%3!08x!, BytesReturned: 0x%4!I64x!\r\n
0xb000011f | BasePage: 0x%1!-16I64x!, PageCount: 0x%2!-16I64x!\r\n
0xb0000120 | About to zero range - ZeroStart: 0x%1!016I64x!, ZeroEnd: 0x%2!016I64x!\r\n
0xb0000121 | Zeroed range - ZeroStart: 0x%1!016I64x!, ZeroEnd: 0x%2!016I64x!\r\n
0xb0000122 | NtfsCommonQueryInformation: File information query not allowed as file was opened by ID without traversal privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Ccb flags: 0x%10!08x!.\r\n
0xb0000123 | NtfsQueryCaseSensitiveInfo: Case sensitive info query not allowed without read attributes access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Ccb access flags: 0x%10!08x!, Granted access: 0x%11!08x!.\r\n
0xb0000124 | NtfsQueryNameInfo: Name info query not allowed as file was opened without traverse privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Ccb flags: 0x%10!08x!.\r\n
0xb0000125 | NtfsQueryLinksInfo: Link info query not allowed as file was opened without traverse privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Ccb flags: 0x%7!08x!.\r\n
0xb0000126 | NtfsSetCaseSensitiveInfo: Cannot mark root directory of a volume case-sensitive. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Device Object flags: 0x%10!08x!.\r\n
0xb0000127 | NtfsRemoveSupersededTarget: Can not do a superseding rename over a system file. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Fcb state: %7!x!.\r\n
0xb0000128 | NtfsRemoveSupersededTarget: Can not do a superseding rename over a file with open handles. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, TxfNumWriters count: %7!d!.\r\n
0xb0000129 | NtfsRemoveSupersededTarget: Can not do a superseding rename over a file with open handles. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Lcb: %7!p!, Link name: %8!S!, TxfNumWriters count: %9!d!.\r\n
0xb000012a | NtfsRemoveSupersededTarget: Can not do a superseding rename over a file opened by ID. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Cleanup count: %7!d!.\r\n
0xb000012b | NtfsRemoveSupersededTarget: Can not do a superseding rename over a file with open handles via either part of the long/short pair. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Lcb: %7!p!, Link name: %8!S!, Link cleanup count: %9!d!, SplitPrimaryLcb: %10!p!, Split link name: %11!S!, Split link cleanup count: %12!d!.\r\n
0xb000012c | NtfsSetRenameInfo: Can not rename a file marked for deletion. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Fcb state: 0x%7!08x!, Lcb: %8!p!, link name: %9!S!, link name flag: 0x%10!08x!, link state: 0x%11!08x!.\r\n
0xb000012d | NtfsSetRenameInfo: Can not rename a txf directory. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, File attributes: 0x%7!08x!.\r\n
0xb000012e | NtfsSetRenameInfo: Can not rename a txf directory. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!.\r\n
0xb000012f | NtfsSetRenameInfo: Can not rename a file that is part of a TxF transaction. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FileAttributes: 0x%7!08x!, Rmstate: 0x%8!08x!.\r\n
0xb0000130 | NtfsSetRenameInfo: Can not rename a directory into itself. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!.\r\n
0xb0000131 | NtfsSetRenameInfo: The file should not have in-memory directory descendents. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!.\r\n
0xb0000132 | NtfsSetRenameInfo: Child Scb mismatch. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Potential child FileRef: %7!I64x!.\r\n
0xb0000133 | NtfsSetLinkInfo: Set link info is not allowed on txf directory. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FileName: %7!S!.\r\n
0xb0000134 | NtfsSetLinkInfo: Set link info is not allowed on a file in a TxF transaction. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FileName: %7!S!, TxfVisibleLinks: %8!d!.\r\n
0xb0000135 | NtfsSetLinkInfo: Set link info failed due to caller not having FILE_WRITE_ATTRIBUTES access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FileName: %7!S!, SeAccessCheck status: %8!S!.\r\n
0xb0000136 | NtfsSetLinkInfo: Creating a link in system directory is not allowed. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, NewLinkName: %7!S!.\r\n
0xb0000137 | NtfsSetLinkInfo: Creating a link in $txf is not allowed if the RM is running. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, NewLinkName: %7!S!, Target RM state: %8!x!.\r\n
0xb0000138 | NtfsSetShortNameInfo: Can not set a short name on a deleted file. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Lcb: %7!p!, Link Name: %8!S!.\r\n
0xb0000139 | NtfsSetShortNameInfo: Can not set a short name on a file under the $TxF directory. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Lcb: %7!p!, Link Name: %8!S!, Parent FileRef: %9!I64x!.\r\n
0xb000013a | NtfsCheckScbForLinkRemoval: Existing handles are not allowed if Txf transaction is doing the rename. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Stream cleanup count: %7!d!.\r\n
0xb000013b | NtfsCheckScbForLinkRemoval: Not all open handles for the stream are by-id opens. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, ByID opens: %7!d!, Stream cleanup count: %8!d!.\r\n
0xb000013c | NtfsStreamRename: Deny access due to encryption happening on source stream. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Scb state: 0x%10!08x! Scb HighWaterMark: %11!I64d!.\r\n
0xb000013d | NtfsProcessTreeForRename: Deny access due to number of batch oplocks has grown. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Previous batch oplock count: %7!d!, current batch oplock count: %8!d!.\r\n
0xb000013e | NtfsFlushVolumeFlushSingleFcb: Thread: %1!p!, Vcb: %2!p!, Fcb: %3!p!, LocalFlags: %4!#08x!\r\n
0xb000013f | NtfsFlushVolumeFlushSingleFcb: Thread: %1!p!, Scb: %2!p!\r\n
0xb0000140 | NtfsFlushVolume: Thread: %1!p!, Vcb: %2!p!, LocalFlags: %3!#08x!\r\n
0xb0000141 | NtfsFlushVolume setting SCB_PERSIST_VOLUME_DISMOUNTED on BitmapScb Scb: %1!p! Vcb: %2!p!\r\n
0xb0000142 | NtfsFlushVolume setting SCB_PERSIST_VOLUME_DISMOUNTED on MftScb Scb: %1!p! Vcb: %2!p!\r\n
0xb0000143 | NtfsFlushCompletionRoutine: Vcb %1!p! - Add context %2!p! into completion queue\r\n
0xb0000144 | NtfsFlushCompletionRoutine: Vcb %1!p! - Add context %2!p! into WorkQueue - Flink %3!p!\r\n
0xb0000145 | NtfsDiskFlushContextWorkItemProcessing: Process work item\r\n
0xb0000146 | NtfsDiskFlushContextWorkItemProcessing: Nothing to work on\r\n
0xb0000147 | Irp: %1!p!, IC: %2!p!, Vcb: %3!p!, MinorCode: %4!02x!, FsControlCode: 0x%5!08x!\r\n
0xb0000148 | NtfsLockVolumeInternal: Cannot lock the volume. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Vcb State: 0x%5!08x!, DisallowDismountCount: %6!d!, ExplicitLock: %7!d!, Volume CleanupCount: %8!d!, Handle count: %9!d!.\r\n
0xb0000149 | NtfsLockVolumeInternal: Volume is already locked.Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Vcb State: 0x%5!08x!.\r\n
0xb000014a | NtfsLockVolumeInternal: Failed to flush system files on the volume. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Flush Status: %5!S!.\r\n
0xb000014b | NtfsLockVolumeInternal: Failed to flush system files on the volume.Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Flush Status: %5!S!.\r\n
0xb000014c | NtfsLockVolumeInternal: Outstanding user files open after flush and retry. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Volume close count: %5!d!, System file close count: %6!d!, User handle count: %7!d!.\r\n
0xb000014d | NtfsLockVolume: Cannot lock volume due to caller does not have manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb000014e | NtfsLockVolume: Cannot lock volume due to active secondary RMs on the volume. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Active RM count: %5!d!, Default RM Active: %6!d!.\r\n
0xb000014f | %1!S!: Setting RM at 0x%2!p! ({%3!S!}) up for auto-restart.\r\n
0xb0000150 | NtfsUnlockVolume: Cannot unlock volume due to caller does not have manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb0000151 | NtfsDismountVolume: IC: %1!p!, Vcb: %2!p!, Label: %3!S!, DeviceName: %4!S!\r\n
0xb0000152 | NtfsDismountVolume: Cannot dismount volume due to system/pagefiles being open for write access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb0000153 | NtfsDismountVolume: Cannot dismount volume due to volume being locked. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, VcbState: 0x%5!08x!.\r\n
0xb0000154 | NtfsDismountVolume: Cannot dismount volume due to system/pagefiles being open for write access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, VcbState: 0x%5!08x!, ReadOnlyCloseCount: %6!d!, CloseCount: %7!d!, SystemFileCloseCount: %8!d!.\r\n
0xb0000155 | NtfsMarkVolumeDirty: Cannot mark volume dirty due to caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb0000156 | NtfsGetVolumeBitmap: Cannot get volume bitmap due to caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb0000157 | NtfsGetBootAreaInfo: Cannot get boot area info due to caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb0000158 | NtfsGetRetrievalPointers: Cannot get retrieval pointers due to caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb0000159 | NtfsGetRetrievalPointerBase: Cannot get revrieval pointer base info due to caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb000015a | NtfsGetRetrievalPointerBase: Cannot get revrieval pointer base info due to caller not having manage volume privilege or this is not a volume open. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!, TypeOfOpen: %6!d!.\r\n
0xb000015b | NtfsCreateUsnJournal: Cannot create Usn journal due to caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!, Irp Request Mode: %6!d!.\r\n
0xb000015c | NtfsUsnTrackModifiedRanges: Cannot enable range tracking due to caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb000015d | NtfsEnumerateUsnData: Cannot enumerate Usn data due to caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb000015e | NtfsFindFilesOwnedBySid: Caller not having manage volume privilege, backup access or can bypass traverse checks. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!, Ccb flags: 0x%6!08x!.\r\n
0xb000015f | NtfsFindFilesOwnedBySid: Caller not having manage volume privilege or backup access and is not admin. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!, Ccb flags: 0x%6!08x!, CallerId: %7!d!, Context owner ID: %8!d!.\r\n
0xb0000160 | NtfsSetSparse: Caller does not have appropriate write access to the stream. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FullFileName: %7!S!, Ccb access flags: 0x%8!08x!, FileObject write access: %9!d!.\r\n
0xb0000161 | NtfsSetSparse: Cannot desparse encrypted file without write data access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FullFileName: %7!S!, Ccb access flags: 0x%8!08x!, Scb attributes: 0x%9!08x!.\r\n
0xb0000162 | NtfsZeroRange: User mode caller not allowed. Thread: %1!p!, Zero flags: 0x%2!08x!, Irp Requestor Mode: %3!d!.\r\n
0xb0000163 | IC: %1!p!, Scb: %2!p!, FileObject: %3!p!\r\n
0xb0000164 | IC: %1!p!, EncryptionOperation: 0x%2!08x!\r\n
0xb0000165 | NtfsReadRawEncrypted: Caller does not have backup access or read data access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FullFileName: %7!S!, Ccb access flags: 0x%8!08x!.\r\n
0xb0000166 | NtfsWriteRawEncrypted: Caller does not have write data access or restore access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FullFileName: %7!S!, Ccb access flags: 0x%8!08x!.\r\n
0xb0000167 | NtfsWriteRawEncrypted: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb0000168 | NtfsLookupStreamFromCluster: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb0000169 | NtfsChangeVolumeSize: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb000016a | NtfsChangeVolumeSize (%1!p!): Calling NtfsFreeRecentlyDeallocated\r\n
0xb000016b | NtfsChangeVolumeSize (%1!p!): Done calling NtfsFreeRecentlyDeallocated\r\n
0xb000016c | NtfsMarkHandle: Caller does not have a valid volume handle or manage volume access or is not kernel model caller. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FullFileName: %7!S!, Ccb access flags: 0x%8!08x!, HandleInfo flags: 0x%9!08x!, Irp Requestor Mode: %10!d!.\r\n
0xb000016d | NtfsMarkHandle: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb000016e | NtfsMarkHandle: Cannot deny defrag. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Persist flags: 0x%10!08x!, HandleInfo flags: 0x%11!08x!.\r\n
0xb000016f | NtfsMarkHandle: Cannot deny Frs consolidation. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState2: 0x%7!08x!, Scb: %8!p!, Scb Type Code: 0x%9!x!, Scb Name: %10!S!, Persist flags: 0x%11!08x!, HandleInfo flags: 0x%12!08x!.\r\n
0xb0000170 | NtfsMarkHandle: Cannot filter metadata. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!, Scb: %8!p!, Scb Type Code: 0x%9!x!, Scb Name: %10!S!, Persist flags: 0x%11!08x!, HandleInfo flags: 0x%12!08x!, Irp RequestorMode: %13!d!.\r\n
0xb0000171 | NtfsMarkHandle: Mark handle is not allowed on system files. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FcbState: 0x%7!08x!, HandleInfo flags: %8!x!.\r\n
0xb0000172 | NtfsMarkHandle: File already has user writable references. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, HandleInfo: 0x%10!08x!.\r\n
0xb0000173 | NtfsMarkHandle: File was granted write access previously but no oplocks were broken. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Writers: %10!d!.\r\n
0xb0000174 | NtfsPrefetchFile: Caller not having manage volume privilege. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb0000175 | NtfsSetZeroOnDeallocate: Only allowed on regular user files opened for write. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, TypeOfOpen: %5!d!, WriteAccess: %6!d!, Fcb: %7!p!, FileRef: 0x%8!I64x!, FcbState: %9!x!, Scb AttributeTypeCode: 0x%10!x!, Ccb FullFileName: %11!S!.\r\n
0xb0000176 | NtfsSetShortNameBehavior: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb0000177 | Setting VCB_EXT_CHAR_STATE_ALLOW_EXT_CHAR for volume 0x%1!p! to %2!u!.\r\n
0xb0000178 | NtfsQueryPagefileEncryption: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb000017a | NtfsResetVolsnapBehaviorForVolume: Volsnap hints are disabled by registry. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, NtfsData Flags: %5!x!.\r\n
0xb000017b | NtfsResetVolsnapBehaviorForVolume: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb000017c | Resetting Volsnap behavior for VCB = 0x%1!p!.  New state is 0x%2!x!.\r\n
0xb000017e | NtfsCorruptionHandling: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Ccb access flags: 0x%5!08x!.\r\n
0xb000017f | NtfsGlobalCorruptionHandling: Caller does not have manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!.\r\n
0xb0000180 | Scrub resume from SystemScbIndex: %1!u! Vcn: %2!#I64x! + %3!#x!\r\n
0xb0000181 | Scb:%1!p! Scrub resume from Vcn: %2!#I64x! + %3!#x!\r\n
0xb0000182 | Scrub SystemScbIndex: %1!u!\r\n
0xb0000183 | NtfsScrubData: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, TypeOfOpen: %5!d!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb0000184 | Scrub not supported for Txf file, Scb: %1!p!, TxfScb: %2!p!\r\n
0xb0000185 | Scrub SCRUB_DATA_INPUT_FLAG_SKIP_NON_INTEGRITY_DATA is request. noop\r\n
0xb0000186 | Scb:%1!p! ScrubInternal OperationStatus: %2!S! Repaired: %3!#I64x! Failed: %4!#I64x! FileOffset: %5!#I64x! Length: %6!#I64x! ParityExtentCount: %7!u!\r\n
0xb0000187 | Scb:%1!p! ScrubInternal Status: %2!S! Repaired: %3!#I64x! Failed: %4!#I64x! ParityExtentCount: %5!u!\r\n
0xb0000188 | InternalFileReference: %1!u!\r\n
0xb0000189 | InternalFileReference:%1!u!\r\n
0xb000018a | Scb:%1!p! Incomplete IoCount:%2!u! Cancel:%3!u! ParityExtentCount:%4!u!\r\n
0xb000018b | Scb:%1!p! Scrub skipping resident attribute (d) (%2!S!)\r\n
0xb000018c | Scb:%1!p! Scrub skipping resident attribute (%2!S!)\r\n
0xb000018d | Scb:%1!p! Scrub StartingVcn(%2!#I64d!) is negative\r\n
0xb000018e | Scb:%1!p! Scrub starting vcn is beyond VDL (FileOffset: %2!#I64x!, SectorAlignedVdl: %3!#I64x!)\r\n
0xb000018f | Scb:%1!p! Scrub no more Mcb entries from StartingVcn:%2!#I64x!\r\n
0xb0000190 | Scb:%1!p! Scrub skipping UNUSED_LCN Vcn: %2!#I64x!, ClusterCount: %3!#I64x!\r\n
0xb0000191 | Scb:%1!p! StartingVcn:%2!#I64x! is beyond Vdl\r\n
0xb0000192 | Scb:%1!p! ScrubDsmRange [%2!#I64x!,%3!#I64x!) Length:%4!#I64x! (Bytes) StartingVcn:%5!#I64x! + %6!#x! SectorAlignedVdl:%7!#I64x!\r\n
0xb0000193 | Scrub found problems Scb: %1!p! Vcn %2!#I64x! FileOffset: %3!#I64x! Length: %4!#I64x! Status: %5!S! BytesFailed: %6!#I64x! BytesRepaired: %7!#I64x! NewParityExtents: %8!u!\r\n
0xb0000194 | Scb:%1!p! DsmAction_Scrub call failed, Status: %2!S!\r\n
0xb0000195 | Scb:%1!p! DsmAction_Scrub operation failed, Status: %2!S!\r\n
0xb0000196 | FSCTL_REPAIR_COPIES not supported for Txf file, Scb: %1!p!, TxfScb: %2!p!\r\n
0xb0000197 | Scb:%1!p! FSCTL_REPAIR_COPIES skipping resident attribute (d) (%2!S!)\r\n
0xb0000198 | Scb:%1!p! FSCTL_REPAIR_COPIES skipping resident attribute (%2!S!)\r\n
0xb0000199 | FSCTL_REPAIR_COPIES interrupted by thread termination.\r\n
0xb000019a | FSCTL_REPAIR_COPIES canceled\r\n
0xb000019b | Scb:%1!p! FSCTL_REPAIR_COPIES no more Mcb entries from StartingVcn:%2!#I64x!\r\n
0xb000019c | Scb:%1!p! FSCTL_REPAIR_COPIES No more Mcb entries (unallocated) from StartingVcn:%2!#I64x!\r\n
0xb000019d | Scb:%1!p! FSCTL_REPAIR_COPIES skipping UNUSED_LCN Vcn: %2!#I64x!, ClusterCount: %3!#I64x!\r\n
0xb000019e | Scb:%1!p! RepairDsmRange [%2!#I64x!,%3!#I64x!) Length:%4!#I64x! (Bytes) FileOffset: %5!#I64x!\r\n
0xb000019f | Scb:%1!p! DsmAction_Repair call failed, Status: %2!S!\r\n
0xb00001a0 | Scb:%1!p! DsmAction_Repair operation failed, Status: %2!S!\r\n
0xb00001a1 | Scb:%1!p! DsmAction_Repair completed, IrpStatus: %2!S!\r\n
0xb00001a2 | NtfsQueryCachedRuns: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, TypeOfOpen: %5!d!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb00001a3 | NtfsQueryStorageClasses: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, TypeOfOpen: %5!d!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb00001a4 | NtfsQueryRegionInfo: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, TypeOfOpen: %5!d!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb00001a5 | NtfsUnloadFile: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, TypeOfOpen: %5!d!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb00001a6 | NtfsCheckForSection: File already has image section. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!.\r\n
0xb00001a7 | NtfsShuffleFile: User mode caller is not allowed. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, TypeOfOpen: %5!d!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Ccb FullFileName: %8!S!, Irp RequestorMode: %9!d!.\r\n
0xb00001a8 | NtfsShuffleFile: Denying access due to volume is locked. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: %7!I64x!, Ccb FullFileName: %8!S!, VcbState: 0x%9!08x!.\r\n
0xb00001a9 | NtfsShuffleFile: Defrag is denied. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Persist flags: 0x%10!08x!, Ccb flags: 0x%11!08x!.\r\n
0xb00001aa | NtfsShuffleFile: Denying access due to conflicting with read-only state. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, FileAttributes: 0x%7!08x!, SL control flags: 0x%8!08x!.\r\n
0xb00001ab | NtfsRearrangeFile: User mode caller is not allowed. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Ccb FullFileName: %7!S!, Irp RequestorMode: %8!d!.\r\n
0xb00001ac | NtfsRearrangeFile: Denying access due to volume is locked. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Ccb FullFileName: %7!S!, VcbState: 0x%8!08x!.\r\n
0xb00001ad | NtfsRearrangeFile: Defrag is denied. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Persist flags: 0x%10!08x!, Ccb flags: 0x%11!08x!.\r\n
0xb00001af | NtfsSparseOverAllocate: Caller does not have appropriate write access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, FileRef: %5!I64x!, FullFileName: %6!S!, Ccb access flags: %7!x!.\r\n
0xb00001b0 | NtfsInitiateFileMetadataOptimization: Only allowed on regular user files/directories opened for write. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: %7!I64x!, Scb AttributeTypeCode: %8!x!, FcbState2: %9!x!, Ccb FullFileName: %10!S!, Ccb Access flags: %11!x!, Ccb Flags2: %12!x!.\r\n
0xb00001b1 | NtfsQueryFileMetadataOptimization: Only allowed on regular user files/directories opened for read. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Scb AttributeTypeCode: 0x%8!x!, Ccb FullFileName: %9!S!, Ccb Access flags: 0x%10!08x!.\r\n
0xb00001b2 | NtfsCleanVolumeMetadata: Caller not having manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!.\r\n
0xb00001b3 | NtfsEnumOnMountToDeleteWorker(%1!p!,%2!p!): Open status=0x%3!x!, path="%4!S!"\r\n
0xb00001b4 | NtfsEnumOnMountToDeleteWorker(%1!p!,%2!p!): Enumerate status=0x%3!x!\r\n
0xb00001b5 | NtfsEnumMountWorker(%1!p!,%2!p!): Open status=0x%3!x!, file="%4!S!"\r\n
0xb00001b6 | NtfsEnumMountWorker(%1!p!,%2!p!): Close status=0x%3!x!\r\n
0xb00001b7 | NtfsEnumOnMountToDeleteWorker(%1!p!,%2!p!): Close dir status=0x%3!x!\r\n
0xb00001b8 | NtfsCleanVolumeMetadata: Caller not having manage volume privilege. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!, EffectiveMode: %10!d!.\r\n
0xb00001b9 | SCB: %1!p!, StartOffset: 0x%2!I64x!, Length: 0x%3!I64x!, StartVcn=0x%4!I64x!, BeyondEndVcn=0x%5!I64x!\r\n
0xb00001ba | FsLibGetBadAddressRanges returned Status: %1!S!, NumBadRanges: 0x%2!x!\r\n
0xb00001bb | FsInputRangeIndex: %1!u!, FileOffset: 0x%2!I64x!, VolumeOffset: 0x%3!I64x!, LengthInBytes: 0x%4!I64x!\r\n
0xb00001bc | Scb: %1!p!, Status: %2!S!, AbnormalTermination: %3!S!\r\n
0xb00001bd | Scb: %1!p!, Status: %2!S!\r\n
0xb00001be | NtfsEncryptionKeyCtl: Caller does not have SE_TCB_PRIVILEGE. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!.\r\n
0xb00001bf | Logic error of posting close to work queue.\r\n
0xb00001c0 | NtfsFindPrefixHashEntry: {Hash table: %1!p!} {ParentScb: %2!p!, '%3!S!'} {RemainingName: '%4!S!'}\r\n
0xb00001c1 | NtfsFindPrefixHashEntry: {Lcb: NULL}\r\n
0xb00001c2 | NtfsFindPrefixHashEntry: {Lcb: %1!p!, '%2!S!'}\r\n
0xb00001c3 | NtfsFindPrefixHashEntry: {Lcb not found}\r\n
0xb00001c4 | NtfsInsertHashEntry: {Hash table: %1!p!} {HashValue: %2!08x!} {FullNameLength: %3!d!} {Lcb: %4!p!, '%5!S!'}\r\n
0xb00001c5 | NtfsRemoveHashEntry: {Hash table: %1!p!} {HashValue: %2!08x!} {HashLcb: %3!p!, '%4!S!'}\r\n
0xb00001c6 | Vcb %1!p!.  Checkpoint injection.  Count %2!d!\r\n
0xb00001c7 | Vcb %1!p!.  Injected checkpoint.\r\n
0xb00001c8 | Vcb %1!p!.  Log %2!d!%!PCT! full.  Wait for CC to flush metadata first. Count %3!d!\r\n
0xb00001c9 | Vcb %1!p!.  Done waiting for CC to flush metadata\r\n
0xb00001ca | Vcb %1!p!.  Start of checkpoint\r\n
0xb00001cb | Vcb %1!p!.  Clean checkpoint. Count %2!d!\r\n
0xb00001cc | Vcb %1!p!.  Partial flush starts\r\n
0xb00001cd | Vcb %1!p!.  Partial flush ends\r\n
0xb00001ce | Vcb %1!p!.  Overflowed DPT. Count %2!d!\r\n
0xb00001cf | Vcb %1!p!.  Almost overflowed DPT. Count %2!d!\r\n
0xb00001d0 | Vcb %1!p!.  Fuzzy checkpoint. Count %2!d!\r\n
0xb00001d1 | Vcb %1!p!.  Flush oldest FO.  Count %2!d!\r\n
0xb00001d2 | Vcb %1!p!.  Flush starts with FRef %2!I64x!\r\n
0xb00001d3 | Vcb %1!p!.  Flush ends.  FO %2!p!\r\n
0xb00001d4 | Vcb %1!p!.  Checkpoint completed.\r\n
0xb00001d5 | Vcb %1!p!.  Leaving NtfsCheckpointVolume.\r\n
0xb00001d6 | NtfsCommitCurrentTransaction IC: %1!p!, TransactionId: 0x%2!08x!\r\n
0xb00001d8 | NtfsCommitCurrentTransaction (%1!p!,%2!p!,%3!p!): Pre NtfsWriteLog failure %4!x!\r\n
0xb00001d9 | NtfsCommitCurrentTransaction (%1!p!,%2!p!,%3!p!): Post NtfsWriteLog failure %4!x!\r\n
0xb00001da | NtfsCommitCurrentTransaction (%1!p!,%2!p!,%3!p!): LfsFlushToLsn failure %4!x! Count %5!d!\r\n
0xb00001db | NtfsCommitCurrentTransaction (%1!p!,%2!p!,%3!p!): Pre NtfsProcessNewLengthQueue failure %4!x!\r\n
0xb00001dc | NtfsCommitCurrentTransaction (%1!p!,%2!p!,%3!p!): Post NtfsProcessNewLengthQueue failure %4!x!\r\n
0xb00001dd | NtfsCommitCurrentTransaction IC: %1!p!, TransactionId: 0x%2!08x! Completed\r\n
0xb00001df | NtfsFreeRecentlyDeallocated: Vcb %1!p! - Entering - ActiveLsn: %2!I64x!, ClearAll: %3!S!\r\n
0xb00001e0 | NtfsFreeRecentlyDeallocated: Vcb %1!p! empty list - Leaving\r\n
0xb00001e1 | NtfsFreeRecentlyDeallocated: Vcb %1!p! empty list  - Leaving\r\n
0xb00001e2 | NtfsFreeRecentlyDeallocated: Vcb %1!p! - Found frozen deallocated clusters with %2!I64x! clusters\r\n
0xb00001e3 | NtfsFreeRecentlyDeallocated: Vcb %1!p! - No actionable deallocated clusters\r\n
0xb00001e5 | NtfsFreeRecentlyDeallocated: Vcb %1!p! - Found a deallocated clusters %2!p! with %3!I64x! clusters, Lsn: %4!I64x!, Flags: %5!08x!\r\n
0xb00001e6 | Vcb: %1!p!, Processing range. DeallocatedClusters: %2!p!, RunIndex: %3!d!, StartingLcn: %4!I64x!, ClusterCount: %5!I64x!\r\n
0xb00001e7 | Looking for dangling MDLs\r\n
0xb00001e8 | FsLibGroupSubExtentsByDanglingMdl failed: %1!S!\r\n
0xb00001e9 | FsLibAddBaseMcbEntryEx failed: %1!S!\r\n
0xb00001ea | NtfsAddToMatchingDeallocatedClusters( ExtentsWithoutDanglingMdl ) failed: %1!S!\r\n
0xb00001eb | NtfsAddToMatchingDeallocatedClusters( ExtentsWithDanglingMdl ) failed: %1!S!\r\n
0xb00001ec | No sub extents has dangling MDL\r\n
0xb00001ed | NtfsFreeRecentlyDeallocated: Vcb %1!p! - Telling volsnap freeing at %2!I64x! for %3!x! clusters\r\n
0xb00001ee | NtfsFreeRecentlyDeallocated: Vcb %1!p! - Volsnap responsed with freeing at %2!I64x! for %3!x! clusters\r\n
0xb00001ef | NtfsFreeRecentlyDeallocated: Vcb %1!p! - Got error 0x%2!x! from below\r\n
0xb00001f0 | NtfsFreeRecentlyDeallocated: Vcb %1!p! - Deleting MarkUnusedContext %2!p!\r\n
0xb00001f1 | NtfsFreeRecentlyDeallocated: Vcb %1!p! - Leaving\r\n
0xb00001f2 | NtfsRemoveNtfsMcbEntry Scb: %1!p!, Mcb: %2!p!, Vcn: 0x%3!I64x!, Length: 0x%4!I64x!\r\n
0xb00001f3 | NtfsRemoveNtfsMcbEntry Mcb: %1!p! Completed.\r\n
0xb00001f4 | NtfsAddNtfsMcbEntry Scb: %1!p!, Mcb: %2!p!, Vcn: 0x%3!I64x!, Lcn: 0x%4!I64x!, Length: 0x%5!I64x!\r\n
0xb00001f5 | NtfsAddNtfsMcbEntry Mcb: %1!p!, Result: %2!S!\r\n
0xb00001f6 | NtfsUnloadNtfsMcbRange Scb: %1!p!, Mcb: %2!p!, StartVcn: 0x%3!I64x!, EndVcn: 0x%4!I64x!, TruncateOnly: %5!S!\r\n
0xb00001f7 | NtfsUnloadNtfsMcbRange Mcb: %1!p! Completed.\r\n
0xb00001f8 | Valid NTFS boot sector. Vcb: %1!p!; BootSector: %2!p!\r\n
0xb00001f9 | Not an NTFS boot sector. Vcb: %1!p!; BootSector: %2!p!; CheckNumber: %3!d!\r\n
0xb00001fa | NtfsMountVolume: Vcb:%1!p!, IC:%2!p!, Growing allocation for Mft's Attribute List failed with exception:0x%3!x!\r\n
0xb00001fb | NtfsMountVolume: IC: %1!p!, Vcb: %2!p!, Label: %3!S!, DeviceName: %4!S!\r\n
0xb00001fc | Mounting DAX partition. Vcb: %1!p!\r\n
0xb00001fd | DAX volume mounted without DAX support because storage is not DAX capable. Vcb: %1!p!\r\n
0xb00001fe | NtfsGrowMftsAttributeListAllocation Vcb:%1!p!, IC:%2!p! Mft AttributeList not found, skipping growth\r\n
0xb00001ff | NtfsGrowMftsAttributeListAllocation Vcb:%1!p!, IC:%2!p! Converting Resident AttributeList(size:0x%3!I64x!) to NonResident\r\n
0xb0000200 | NtfsGrowMftsAttributeListAllocation Vcb:%1!p!, IC:%2!p!, AttrListScb:%3!p! Added Allocation for NonResident AttributeList (old size:0x%4!I64x!)\r\n
0xb0000201 | Unexpected exception code of 0x%1!x! received\r\n
0xb0000202 | Exception code of 0x%1!x! received during mount.\r\n
0xb0000203 | Unexpected exception code of 0x%1!x! received.\r\n
0xb0000204 | LogFileFull %1!S! BackTrace: ln %2!p!; ln %3!p!; ln %4!p!; ln %5!p!; ln %6!p!; ln %7!p!; ln %8!p!; ln %9!p!; ln %10!p!; ln %11!p!; ln %12!p!; ln %13!p!; ln %14!p!; ln %15!p!; ln %16!p!; ln %17!p!; ln %18!p!; ln %19!p!; ln %20!p!; ln %21!p!;\r\n
0xb0000205 | Unexpected raise of 0x%1!x! during critical non-raise code\r\n
0xb0000206 | NtfsProcessException IC: %1!p!, ExceptionCode: 0x%2!08x!\r\n
0xb0000208 | Failed to abort - IrpContext %1!p!, Irp %2!p!, Vcb %3!p!, Count %4!x!, Status %5!x!\r\n
0xb0000209 | Failed to abort - IrpContext %1!p!, Irp %2!p!, Vcb %3!p!, Scb %4!p!, FileRef %5!I64x!\r\n
0xb000020a | Setting STATUS_CANT_WAIT in top-level exception status for write @ 0x%1!08x!%2!08x!\r\n
0xb000020b | Setting 0x%1!x! in top-level exception status for write @ 0x%2!08x!%3!08x!\r\n
0xb000020c | [%1!S!, %2!02x!]: Irp: %3!p!, IC: %4!p!, Status: %5!S!\r\n
0xb000020e | Can't handle invalid bitmap in a positive way.\r\n
0xb000020f | NTFS ETW tracing is now active.\r\n
0xb0000210 | Updating NtfsMinTrimTotalSize to %1!x!.\r\n
0xb0000211 | Updating NtfsMaxTrimTotalSize to %1!x!.\r\n
0xb0000212 | NtfsSetObjectId: Caller does not have restore access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!, Irp Minor Function: 0x%9!08x!.\r\n
0xb0000213 | NtfsSetObjectIdExtendedInfo: Caller does not have write access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!, Irp Minor Function: 0x%9!08x!.\r\n
0xb0000214 | NtfsDeleteObjectId: Caller does not have write access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!, Irp Minor Function: 0x%9!08x!.\r\n
0xb0000216 | NtfsFsQuotaSetInfo: Denying access due to administrator limit. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!.\r\n
0xb0000217 | NtfsCommonSetQuota: Caller does not have manage volume privilege and it's not quota file. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: 0x%7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!, Ccb Flags: 0x%10!08x!.\r\n
0xb0000218 | Unexpected Paging-Read on DAX mappable stream, Scb=%1!p!\r\n
0xb0000219 | NtfsSetReparsePoint: Caller does not have write access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb Access flags: 0x%8!08x!, File Object Write Access: %9!d!.\r\n
0xb000021a | NtfsSetReparsePointEx: Caller does not have write access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb Access flags: 0x%8!08x!, File Object Write Access: %9!d!.\r\n
0xb000021b | NtfsDeleteReparsePoint: Caller does not have write access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb Access flags: 0x%8!08x!, File Object Write Access: %9!d!.\r\n
0xb000021c | NtfsAbortTransaction IC: %1!p!, TransactionId: 0x%2!08x!\r\n
0xb000021e | DoAction::InitializeFRS IC:%1!p!, FileRef:0x%2!04x!_%3!08x!, BaseFRS:0x%4!012I64x!\r\n
0xb000021f | DoAction::DeallocateFRS IC:%1!p!, FileRef:0x%2!04x!_%3!08x!, BaseFRS:0x%4!012I64x!\r\n
0xb0000220 | DoAction::WriteEndOfFRS IC:%1!p!, FileRef:0x%2!04x!_%3!08x!, BaseFRS:0x%4!012I64x!, Attrib:0x%5!x! Off:0x%6!x!, Len:0x%7!x!\r\n
0xb0000221 | DoAction::CreateAttribute IC:%1!p!, FileRef:0x%2!04x!_%3!08x!, BaseFRS:0x%4!012I64x!, Attrib:0x%5!x!\r\n
0xb0000222 | NtfsRestartChangeValue IC:%1!p!, FileRef:0x%2!04x!_%3!08x!, BaseFRS:0x%4!012I64x!, FileRef:0x%5!I64x!\r\n
0xb0000223 | DoAction::SetNewAttributeSizes IC:%1!p!, FileRef:0x%2!04x!_%3!08x!, BaseFRS:0x%4!012I64x! OLD: Alloc:%5!I64x!, FileSize:%6!I64x!, VDL:%7!I64x!, TotalAlloc:%8!I64x! NEW: Alloc:%9!I64x!, FileSize:%10!I64x!, VDL:%11!I64x!, TotalAlloc:%12!I64x!\r\n
0xb0000224 | DoAction(SetBitsInNonresidentBitMap) IC: %1!p!, Vcb: %2!p!, Bitmap: %3!p!\r\n
0xb0000225 | DoAction(ClearBitsInNonresidentBitMap) IC: %1!p!, Vcb: %2!p!, Bitmap: %3!p!\r\n
0xb0000226 | NtfsUpgradeFileSecurity: Denying access due to volume does not support Txf. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!.\r\n
0xb0000227 | NtfsCaseSensitiveInfoAccessCheck: Caller does not have write access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb Access flags: 0x%8!08x!.\r\n
0xb0000228 | NtfsCaseSensitiveInfoAccessCheck: Caller does not have appropriate access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!.\r\n
0xb0000229 | NtfsCheckFileForDelete: Denying access due to there are same-tx handles open to this file. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Txf Writers Count: %7!d!.\r\n
0xb000022a | NtfsCheckFileForDelete: Denying access due to TxfCheckForLockConflict failed. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Original status: %7!S!.\r\n
0xb000022b | NtfsCheckFileForDelete: Denying access due to superseding view indexes are not allowed. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, File Attributes: 0x%7!08x!.\r\n
0xb000022c | NtfsCheckFileForDelete: Denying access due to non-posix delete of target directory open is not allowed. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, File Attributes: 0x%7!08x!.\r\n
0xb000022d | NtfsCheckFileForDelete: Denying access due to file is not deleteable. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!.\r\n
0xb000022e | NtfsCheckFileForDelete: Denying access due to target file is read only. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, File Attributes: 0x%7!08x!, IrpSp->Flags: 0x%8!08x!.\r\n
0xb000022f | NtfsCheckFileForDelete: Caller does not have write attributes access (TxfAccessCheck failed). Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb AccessFlags: 0x%7!08x!, TxfAccessCheck access status: %8!S!.\r\n
0xb0000230 | NtfsCheckFileForDelete: Denying access due to failing to remove image section. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Scb: %7!p!, AttributeTypeCode: 0x%8!x!, Attribute Name: %9!S!.\r\n
0xb0000231 | NtfsGlobalSdUpdate: Caller does not have manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!.\r\n
0xb0000232 | NtfsRepairItem: Denying access due to volume is locked. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, VcbState: 0x%5!08x!.\r\n
0xb0000233 | NtfsSetRepairState: Caller does not have manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!.\r\n
0xb0000234 | NtfsInitiateRepair: Caller does not have manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!.\r\n
0xb0000235 | NTFS ETW tracing is shutting down.\r\n
0xb0000236 | NtfsDefineStorageReserve: Caller does not have manage volume privilege. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: %7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb0000237 | NtfsDeleteStorageReserve: Caller does not have manage volume privilege. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: %7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb0000238 | NtfsRepairStorageReserve: Caller does not have manage volume privilege. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: %7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb0000239 | NtfsSetStorageReserveIdInfo: System files are not allowed to be part of a storage reserve. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Fcb State: 0x%7!08x!, Ccb FullFileName: %8!S!.\r\n
0xb000023a | NtfsSetStorageReserveIdInfo: Caller does not have appropriate access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!.\r\n
0xb000023b | NtfsChangeStorageReserveId: Caller does not have manage volume privilege. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!, Operation flags: 0x%9!08x!.\r\n
0xb000023c | NtfsChangeStorageReserveId: Caller does not have manage volume privilege to explicitly setting reserve ID to/from a "restricted area". Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!.\r\n
0xb000023d | Failed to get a non-volatile token for Vcb: %1!p!, Status: %2!S!\r\n
0xb000023e | Failed to free non-volatile token for Vcb: %1!p!, Status: %2!S!\r\n
0xb000023f | NtfsRestoreScbSnapshots: Restored TotalAllocated, Scb: %1!p!, TotalAllocated: 0x%2!I64x!\r\n
0xb0000240 | NtfsGetDeallocatedClusters: Lsn updated for DeallocatedClusters: %1!p!, Lsn: %2!I64x!\r\n
0xb0000241 | ClustersLinkAsHead: %1!p!, FlagsToMatch: 0x%2!x!, InsertAfter: %3!S!\r\n
0xb0000242 | Clusters: %1!p!, Flags: 0x%2!x!\r\n
0xb0000243 | Matching cluster: %1!p!, NumberOfRuns: 0x%2!x!\r\n
0xb0000244 | Clusters: %1!p!\r\n
0xb0000245 | Allocated new deallocated clusters\r\n
0xb0000246 | Need to add Range. DanglingMdl: %1!S!, DeallocatedClusters: %2!p!, Lcn: %3!I64x!, ClusterCount: %4!I64x!\r\n
0xb0000247 | Added range. DanglingMdl: %1!S!, DeallocatedClusters: %2!p!, Lcn: %3!I64x!, ClusterCount: %4!I64x!\r\n
0xb0000248 | TxfCheckForLockConflict: File locked for modify transaction. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!,Fcb: %5!p!, FileRef: 0x%6!I64x!, TxfFcb Flags: 0x%7!08x!, ShareMode: 0x%8!08x!.\r\n
0xb0000249 | TxfCheckForLockConflict: Locking transaction is doomed and caller is non-trans or different trans who wants to modify. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Granted Access: 0x%7!08x!.\r\n
0xb000024a | TxfCheckForLockConflict: Modification access desired. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Granted Access: 0x%7!08x!.\r\n
0xb000024b | TxfCheckForLockConflict: File has user handle opened on one of the versions or user-mapping on a section. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Granted Access: 0x%7!08x!, Reader cleanup count: %8!d!.\r\n
0xb000024c | %1!S!: from %2!S! (%3!S!:%4!d!) RM at 0x%5!p! {%6!S!}, Tx at 0x%7!p! {%8!S!}, Status was 0x%9!x!\r\n
0xb000024e | %1!S!: RM at 0x%2!p! {%3!S!} aborting transaction at 0x%4!p! {%5!S!}\r\n
0xb0000250 | %1!S!: RM at 0x%2!p! {%3!S!}: Unexpected exception code of 0x%4!x! received.\r\n
0xb0000251 | %1!S!: TxfStartRm reports RM will be reset: RM metadata corrupt\r\n
0xb0000252 | %1!S!: TxfStartRm reports RM will be reset: TM could not be initialized\r\n
0xb0000253 | %1!S!: TxfStartRm reports RM will be reset: RM log corrupt\r\n
0xb0000254 | %1!S!: TxfStartRm reports RM will be reset: log version changed\r\n
0xb0000255 | %1!S!: TxfStartRm reports RM will be reset: dedicated log found, need multiplexed\r\n
0xb0000256 | %1!S!: TxfStartRm reports RM will be reset: multiplexed log found, need dedicated\r\n
0xb0000257 | %1!S!: TxfStartRm reports RM will be reset: CLFS log metadata corrupt\r\n
0xb0000258 | %1!S!: TxfStartRm reports RM will be reset: 0x%2!x!\r\n
0xb0000259 | %1!S!: RM did not start and WILL NOT be reset, status code is 0x%2!x!!\r\n
0xb000025a | %1!S!: Could not initialize IrpContext: 0x%2!x!\r\n
0xb000025b | TxfInitializeVolume: Denying access due to Txf start is not allowed (possible racing with dismount or volume shutdown). Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, FxfVcb flags: 0x%5!08x!.\r\n
0xb000025c | %1!S!: IOCTL_VOLUME_GET_GPT_ATTRIBUTES returned 0x%2!x! for default RM on VCB at 0x%3!p!\r\n
0xb000025d | %1!S!: Exception code 0x%2!x!, Status 0x%3!x! for default RM on VCB at 0x%4!p!\r\n
0xb000025e | %1!S!: Couldn't reset default RM on VCB at 0x%2!p! after %3!d! tries: 0x%4!x!\r\n
0xb000025f | %1!S!: Exception 0x%2!x! raised from TxfConvertRmStartFailureStatusCode for default RM on VCB at 0x%3!p!.  RM will NOT be reset.\r\n
0xb0000260 | %1!S!: %2!S! auto-restart of RM at 0x%3!p! ({%4!S!}): 0x%5!x!\r\n
0xb0000261 | %1!S!: Attempting auto-restart of RM at 0x%2!p! ({%3!S!})\r\n
0xb0000262 | %1!S!: Volume too small to start RM at 0x%2!p! ({%3!S!})\r\n
0xb0000263 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: invalid flags in $Tops\r\n
0xb0000264 | TxfStartRm: Denying access due to Txf start is not allowed (possible racing with dismount or volume shutdown). Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, FxfVcb flags: 0x%5!08x!.\r\n
0xb0000265 | %1!S!: Raising to reset RM at 0x%2!p! ({%3!S!}): Explicit reset requested\r\n
0xb0000267 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: no TXF_DATA in root\r\n
0xb0000268 | %1!S!: RM at 0x%2!p! {%3!S!}: Different nesting levels of 0x%4!x! and 0x%5!x!\r\n
0xb0000269 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: restart area already exists\r\n
0xb000026b | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: RmID in restart area does not match {%4!S!}\r\n
0xb000026c | %1!S!: Got %2!d! from ClfsGetLogFileInformation for RM at 0x%3!p! {%4!S!}\r\n
0xb000026d | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Restart LSN is before beginning of log.\r\n
0xb000026e | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: MinRollforwardEndLsn is beyond end of log.\r\n
0xb000026f | %1!S!: TxF RM at 0x%2!p! {%3!S!} started successfully.\r\n
0xb0000270 | %1!S!: TxF RM at 0x%2!p! {%3!S!} failed to start with Status 0x%4!x! %5!S!\r\n
0xb0000271 | %1!S!: Shutting down %2!S! RM at 0x%3!p! {%4!S!}.  Shutdown is %5!S!\r\n
0xb0000272 | %1!S!: Setting RM at 0x%2!p! {%3!S!} up for auto-restart.\r\n
0xb0000273 | TxfFlushAndInvalidateExistingStructures: File has open user handles. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, CleanupCount: %7!d!.\r\n
0xb0000274 | (%1!S!:%2!d!) - TXF_HARD_ERROR on RM at 0x%3!p! ({%4!S!}): %5!S!)\r\n
0xb0000275 | %1!S!: Renamed RM at 0x%2!p! from {%3!S!} to {%4!S!}\r\n
0xb0000276 | %1!S!: RM at 0x%2!p! {%3!S!}, rolling back Tx at 0x%4!p! {%5!S!}, Status was 0x%6!x!\r\n
0xb0000278 | TxfFsctlStartRm: Denying access due starting default RM is not allowed. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, RmRootFcb: %5!p!.\r\n
0xb0000279 | TxfFsctlWriteBackupInformation: Denying access due RM is active. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, BackupInfo flags: 0x%5!08x!.\r\n
0xb000027a | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Found too high of a TxF ID in log\r\n
0xb000027b | %1!S!: Error Setting Delete Disposition: 0x%2!x!  FileObject: 0x%3!p!\r\n
0xb000027c | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Got a RECOVER notification for a transaction that isn't in-doubt\r\n
0xb000027d | TxfSetupTransactionContextFromCcb: Modifying operation is now allowed with a non-TxF modify handle. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Scb: %7!p!, Attribute Type Code: 0x%8!x!, Ccb FullFileName: %9!S!, Ccb flags: 0x%10!08x!.\r\n
0xb000027e | TxfSetupTransactionContextFromCcb: Invalid TxF structure. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Scb: %7!p!, TxfFo: %8!p!, KtmTrans: %9!p!, TxfRmcb: %10!p!, Ccb FullFileName: %11!S!\r\n
0xb000027f | TxfSetupTransactionContextFromCcb: Denying access of modifying operation on a read-only handle. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Scb: %7!p!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!, FO write access: %10!d!, FO delete access: %11!d!.\r\n
0xb0000280 | %1!S!: RM at 0x%2!p! {%3!S!} raising 0x%4!x! to KTM!\r\n
0xb0000281 | %1!S!: Commit (0x%2!x!) of%3!S!tx {%4!S!} on RM at 0x%5!p! {%6!S!} failed with 0x%7!x!\r\n
0xb0000282 | %1!S!: RM at 0x%2!p! {%3!S!} aborting transaction at 0x%4!p! {%5!S!} (notify commit)\r\n
0xb0000283 | %1!S!: RM at 0x%2!p! {%3!S!} aborting transaction at 0x%4!p! {%5!S!} (notify rollback)\r\n
0xb0000284 | %1!S!: Error doing IRP_MJ_FLUSH_BUFFERS on RM at 0x%2!p! {%3!S!}: 0x%4!x!\r\n
0xb0000285 | %1!S!: RM at 0x%2!p! {%3!S!} trying to abort transaction at 0x%4!p! {%5!S!}\r\n
0xb0000286 | %1!S!: Aborting call stack: 0x%2!p! 0x%3!p! 0x%4!p! 0x%5!p! 0x%6!p!\r\n
0xb0000288 | %1!S!: 0x%2!x! initializing IrpContext for tx at %3!p! {%4!S!}, RM at %5!p! {%6!S!}\r\n
0xb0000289 | %1!S!: 0x%2!x! writing log record for RM at 0x%3!p! {%4!S!}, Tx at 0x%5!p! {%6!S!}\r\n
0xb000028a | %1!S!: About to force aborts on RM at 0x%2!p! {%3!S!}.\r\n
0xb000028b | %1!S!: BaseLsn is greater than TargetLsn on RM at 0x%2!p! {%3!S!}.\r\n
0xb000028c | %1!S!: No transactions remain on RM at 0x%2!p! {%3!S!}.\r\n
0xb000028d | %1!S!: Transaction's first undo LSN greater than TargetLsn on RM at 0x%2!p! {%3!S!}.\r\n
0xb000028e | %1!S!: RM at 0x%2!p! {%3!S!} surprise-aborting transaction at 0x%4!p! {%5!S!}\r\n
0xb000028f | %1!S!: RM at 0x%2!p! {%3!S!} got 0x%4!x! from TxfTryAbortTransaction on Tx 0x%5!p! {%6!S!}\r\n
0xb0000290 | %1!S!: Inactive RM at 0x%2!p! {%3!S!}.\r\n
0xb0000291 | %1!S!: Log is pinned on RM at 0x%2!p! {%3!S!}.\r\n
0xb0000292 | %1!S!: RM at 0x%2!p! {%3!S!}, rolling back KTM Tx at 0x%4!p! {%5!S!}, Status was 0x%6!x!\r\n
0xb0000293 | %1!S!: Log pinned trying to advance RestartLsn on RM at 0x%2!p! {%3!S!}.\r\n
0xb0000294 | %1!S!: Log pinned by doomed transaction on RM at 0x%2!p! {%3!S!}.\r\n
0xb0000295 | %1!S!: Reporting 0x%2!X! to CLFS from RM at 0x%3!p! {%4!S!}: 0x%5!x!\r\n
0xb0000296 | %1!S!: Done forcing aborts on RM at 0x%2!p! {%3!S!}.\r\n
0xb0000297 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: $Txf directory is missing in pre-existing RM\r\n
0xb0000298 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Found $Txf without DUP_INDEX_IS_DOLLAR_TXF_DIRECTORY\r\n
0xb0000299 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Found non-empty $Txf but there is no log\r\n
0xb000029a | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Couldn't find $INDEX_ROOT on $Txf\r\n
0xb000029b | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Couldn't find TXF_DATA_ATTR on $Txf\r\n
0xb000029c | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Found TXF_DATA_ATTR for normal file on $Txf\r\n
0xb000029d | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Expected a secondary RM here\r\n
0xb000029e | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: $Tops is missing but $Txf is non-empty\r\n
0xb000029f | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: $Tops is missing but there is already a log\r\n
0xb00002a0 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: $Tops is %4!S!\r\n
0xb00002a1 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Missing $STANDARD_INFORMATION\r\n
0xb00002a2 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Couldn't find file attributes\r\n
0xb00002a3 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: $Tops is corrupt\r\n
0xb00002a4 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Could not find unnamed data stream\r\n
0xb00002a5 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: $Tops metadata is the wrong version or records wrong size\r\n
0xb00002a6 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: $Tops metadata is the wrong size\r\n
0xb00002a7 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Non-NULL RM ID found in $Tops and there is no log\r\n
0xb00002a8 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Epoch in $Tops metadata doesn't match RM\r\n
0xb00002a9 | %1!S!: Corrupt RM at 0x%2!p! {%3!S!}: Couldn't find $T stream\r\n
0xb00002aa | NtfsReadUsnJournal: Caller does not have manage volume privilege. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: %7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb00002ab | TrimUsnJournal (%1!p!, %2!p!): Decided to trim usn journal.  FirstValidUsn %3!I64x!, new FirstValidUsn %4!I64x!, FS %5!I64x!, AS %6!I64x!, MaxSize %7!I64x!, DeltaSize %8!I64x!\r\n
0xb00002ac | TrimUsnJournal (%1!p!, %2!p!): About to delete allocation till %3!I64x!, SavedReserve %4!I64x!, RequiredReserve %5!I64x!\r\n
0xb00002ad | TrimUsnJournal (%1!p!, %2!p!): Before trimming journal AS %3!I64x!, FS %4!I64x!, VDL %5!I64x!, TA %6!I64x!\r\n
0xb00002ae | TrimUsnJournal (%1!p!, %2!p!): After trimming journal AS %3!I64x!, FS %4!I64x!, VDL %5!I64x!, TA %6!I64x!\r\n
0xb00002af | TrimUsnJournal (%1!p!, %2!p!): Mapping pairs validated\r\n
0xb00002b0 | TrimUsnJournal (%1!p!, %2!p!): Checkpointed\r\n
0xb00002b1 | NtfsQueryUsnJournal: Denying access due to NULL Ccb. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: %7!I64x!.\r\n
0xb00002b2 | NtfsDeleteUsnJournal: Caller does not have manage volume access. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: %6!I64x!, Ccb FullFileName: %7!S!, Ccb access flags: 0x%8!08x!.\r\n
0xb00002b3 | NtfsRestartUsnJournal: Caller does not have manage volume privilege. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: %7!I64x!, Ccb FullFileName: %8!S!, Ccb access flags: 0x%9!08x!.\r\n
0xb00002b4 | NtOfsCreateAttributeEx: Stream already has a open user handle. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, Fcb: %5!p!, FileRef: 0x%6!I64x!, Scb: %7!p!, Scb Type Code: 0x%8!x!, Scb Name: %9!S!, Scb CleanupCount: %10!d!.\r\n
0xb00002b5 | OfsSetLength (%1!p!,%2!p!,%3!p!,%4!p!): Extending journal from AS %5!I64x!, FS %6!I64x!, VDL %7!I64x!, to AS %8!I64x!\r\n
0xb00002b6 | OfsSetLength (%1!p!,%2!p!,%3!p!,%4!p!): Done extending journal AS %5!I64x!, FS %6!I64x!, VDL %7!I64x!, TA %8!I64x!\r\n
0xb00002b7 | OfsSetLength (%1!p!,%2!p!,%3!p!,%4!p!): After NtfsWriteFileSizes\r\n
0xb00002b8 | OfsSetLength (%1!p!,%2!p!,%3!p!,%4!p!): After NtfsSetCcFileSizesUsnBiasAware\r\n
0xb00002b9 | NtOfsPostNewLength (%1!p!,%2!p!,%3!p!): Status %4!x! before calling NtfsReadUsnJournal\r\n
0xb00002ba | NtfsIsRegionDangling: RemainingClusterCount: 0x%1!I64x!, Scb: %2!p!, Vcn: 0x%3!I64x!, Lcn: 0x%4!I64x!, Clusters: 0x%5!I64x!\r\n
0xb00002bb | Vcb %1!p! - has *no* active PFNs\r\n
0xb00002bc | Vcb %1!p! - failed to query active PFNs assuming there are some\r\n
0xb00002bd | Vcb %1!p! - has active PFNs\r\n
0xb00002be | NtfsPerformDismountOnVcb: Vcb %1!p! \r\n
0xb00002bf | NtfsPerformDismountOnVcb: Vcb %1!p! - Found frozen deallocated clusters\r\n
0xb00002c0 | NtfsPerformDismountOnVcb: Vcb %1!p! - Wait for any on going trim to finish\r\n
0xb00002c1 | NtfsPerformDismountOnVcb: Vcb %1!p! - No more on going trim\r\n
0xb00002c2 | NtfsPerformDismountOnVcb: IC: %1!p!, Vcb: %2!p!, Label: %3!S!, DeviceName: %4!S!\r\n
0xb00002c3 | NtfsPostVcbIsCorrupt(%1!p!, %2!x!, %3!p!, %4!p!, %5!016I64x!): IrpContext->TopLevelIrpContext->ExceptionStatus == %6!x! before NtfsSetVcbDirtyFlag.\r\n
0xb00002c4 | NtfsPostVcbIsCorrupt: Marking volume dirty.  Vcb %1!p!, WasDirty: %2!x!, FileReference %3!I64x!, Source %4!016I64x!\r\n
0xb00002c5 | NtfsCommonSetVolumeInfo: Operation is only allowed on a VolumeOpen except for IndexOpen of \$Extend\$Quota with FileFsControlInformation. Thread: %1!p!, TypeOfOpen: %2!d!, Vcb: %3!p!, VolumeName: %4!S!, VolumeLabel: %5!S!, Fcb: %6!p!, FileRef: %7!I64x!, FsInformationClass: 0x%8!x!, Scb: %9!p!.\r\n
0xb00002c7 | Succeeding log write @ 0x%1!08x!%2!08x! after getting 0x%3!x! in top-level irpcontext\r\n
0xb00002c8 | Unexpected Paging-Write on stream accessed in Direct-Access mode, Scb=%1!p!\r\n
0xb00002c9 | NtfsCommonWrite: Writing beyond highest writable sector on active volume is not allowed. Thread: %1!p!, Vcb: %2!p!, VolumeName: %3!S!, VolumeLabel: %4!S!, RequestedRange: 0x%5!I64x!, AllowedRange: 0x%6!I64x!.\r\n
0xb00002ca | Ignoring write to 0x%1!I64x!, SCB length is 0x%2!I64x! for SCB 0x%3!Ix!\r\n
0xb00002cb | Truncating write from 0x%1!I64x! to 0x%2!I64x! for SCB 0x%3!Ix!\r\n
0xd0000001 | FALSE\r\n
0xd0000002 | TRUE\r\n
0xd0000003 | false\r\n
0xd0000004 | true\r\n
