## volsnap.sys

Path: %SystemRoot%\system32\drivers\volsnap.sys

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0xc0060001 | The shadow copy of volume %2 could not create a diff area file on volume %3.\r\n
0xc0060002 | The shadow copy of volume %2 could not be created because volume %3, which is specified as part of the diff area, is not an NTFS volume or an error was encountered while trying to determine the file system type of this volume.\r\n
0xc0060003 | The shadow copy of volume %2 could not lock down the location of the diff area file on volume %3.\r\n
0xc0060004 | The shadow copy of volume %2 could not be created due to insufficient resources for worker threads.\r\n
0xc0060005 | The shadow copy of volume %2 could not be created due to insufficient non-paged memory pool for a bitmap structure.\r\n
0xc0060006 | The shadow copy of volume %2 could not create a new paged heap.  The system may be low on virtual memory.\r\n
0xc0060007 | The shadow copy of volume %2 failed to query the diff area file mappings on volume %3.\r\n
0xc0060008 | The flush and hold writes operation on volume %2 timed out while waiting for a release writes command.\r\n
0xc0060009 | The flush and hold writes operation on volume %2 timed out while waiting for file system cleanup.\r\n
0xc006000a | The shadow copy of volume %2 took too long to install.\r\n
0xc006000b | The shadow copy of volume %2 is aborted because of insufficient memory pool.\r\n
0xc006000c | The shadow copy of volume %2 became low on diff area space before it was properly installed.\r\n
0xc006000d | The shadow copy of volume %2 could not grow its diff area file on volume %3.\r\n
0xc006000e | The shadow copy of volume %2 was aborted because of an IO failure.\r\n
0xc006000f | The shadow copy of volume %2 was aborted because of insufficient paged heap.\r\n
0xc0060010 | The shadow copy of volume %2 was aborted because volume %3, which contains a diff area file for this shadow copy, was force dismounted.\r\n
0xc0060011 | An attempt to flush and hold writes on volume %2 was attempted while another flush and hold was already in progress.\r\n
0xc0060014 | The shadow copy of volume %2 was aborted because of a failed free space computation.\r\n
0xc0060015 | The flush and hold operation for volume %2 was aborted because of low available system memory.\r\n
0xc0060016 | The diff area volume specified for shadow copies on volume %2 could not be added.\r\n
0xc0060017 | There was insufficient disk space on volume %3 to create the shadow copy of volume %2.  Diff area file creation failed.\r\n
0xc0060018 | There was insufficient disk space on volume %3 to persist the shadow copy of volume %2.  Diff area file growth failed.\r\n
0xc0060019 | The shadow copy of volume %2 was aborted because the diff area file could\r\nnot grow in time.  Consider reducing the IO load on this system to avoid\r\nthis problem in the future.\r\n
0xc006001a | The shadow copy of volume %2 was aborted because the original volume for this\r\nshadow copy was removed.\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x40060021 | The oldest shadow copy of volume %2 was deleted to keep disk space usage for shadow copies of volume %2 below the user defined limit.\r\n
0x4006003a | The oldest shadow copy of volume %2 was deleted to keep the total number of shadow copies of volume %2 below a limit.\r\n
0x80060018 | There was insufficient disk space on volume %3 to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006001e | An unfinished create of a shadow copy of volume %2 was deleted.\r\n
0x80060026 | There was a user imposed limit that prevented disk space on volume %3 from being used to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0xc0060001 | The shadow copy of volume %2 could not create shadow copy storage on volume %3.\r\n
0xc0060002 | The shadow copy of volume %2 could not be created because volume %3, which is specified as the location for shadow copy storage, is not an NTFS volume or an error was encountered while trying to determine the file system type of this volume.\r\n
0xc0060003 | The shadow copy of volume %2 could not lock down the location of the shadow copy storage on volume %3.\r\n
0xc0060004 | The shadow copy of volume %2 could not be created due to insufficient resources for worker threads.\r\n
0xc0060005 | The shadow copy of volume %2 could not be created due to insufficient non-paged memory pool for a bitmap structure.\r\n
0xc0060006 | The shadow copy of volume %2 could not create a new paged heap.  The system may be low on virtual memory.\r\n
0xc0060007 | The shadow copy of volume %2 failed to query the shadow copy storage mappings on volume %3.\r\n
0xc0060008 | The flush and hold writes operation on volume %2 timed out while waiting for a release writes command.\r\n
0xc0060009 | The flush and hold writes operation on volume %2 timed out while waiting for file system cleanup.\r\n
0xc006000a | The shadow copy of volume %2 took too long to install.\r\n
0xc006000c | The shadow copy of volume %2 became low on shadow copy storage before it was properly installed.\r\n
0xc006000d | The shadow copy of volume %2 could not grow its shadow copy storage on volume %3.\r\n
0xc006000e | The shadow copies of volume %2 were aborted because of an IO failure on volume %3.\r\n
0xc006000f | The shadow copies of volume %2 were aborted because of insufficient paged heap.\r\n
0xc0060010 | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, was force dismounted.\r\n
0xc0060011 | An attempt to flush and hold writes on volume %2 was attempted while another flush and hold was already in progress.\r\n
0xc0060014 | The shadow copies of volume %2 were aborted because of a failed free space computation.\r\n
0xc0060015 | The flush and hold operation for volume %2 was aborted because of low available system memory.\r\n
0xc0060016 | The shadow copy storage volume specified for shadow copies on volume %2 could not be added.\r\n
0xc0060017 | There was insufficient disk space on volume %3 to create the shadow copy of volume %2.  Shadow copy storage creation failed.\r\n
0xc0060019 | The shadow copies of volume %2 were deleted because the shadow copy storage could not grow in time.  Consider reducing the IO load on the system or choose a shadow copy storage volume that is not being shadow copied.\r\n
0xc006001b | The shadow copies of volume %2 were aborted during detection because a critical control file could not be opened.\r\n
0xc006001c | The shadow copy of volume %2 could not be created due to a failure in creating the necessary on disk structures.\r\n
0xc006001d | The shadow copies of volume %2 were aborted during detection.\r\n
0xc006001f | A control item for shadow copies of volume %2 was lost during detection.\r\n
0xc0060020 | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present.\r\n
0xc0060022 | The shadow copies of volume %2 were aborted because of a failure to ensure crash dump or hibernate consistency.\r\n
0xc0060023 | The shadow copies of volume %2 were aborted because the shadow copy storage failed to grow.\r\n
0xc0060024 | The shadow copies of volume %2 were aborted because the shadow copy storage could not grow due to a user imposed limit.\r\n
0xc0060025 | The shadow copies of volume %2 were aborted in preparation for hibernation because this volume is used for hibernation and is not an NTFS volume.\r\n
0xc0060027 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 could not be located in non-critical space.  Consider using a shadow copy storage volume that does not have any shadow copies.\r\n
0xc0060028 | The shadow copies of volume %2 were aborted because volume %3 has been dismounted.\r\n
0xc0060029 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  Consider deleting unnecessary files on the shadow copy storage volume or use a different shadow copy storage volume.\r\n
0xc0060030 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  A shadow copy create computation is in progress to find more contiguous blocks.\r\n
0xc006003b | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present in time during a previous session.\r\n
0xc006003c | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, has been taken offline.\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x40060021 | The oldest shadow copy of volume %2 was deleted to keep disk space usage for shadow copies of volume %2 below the user defined limit.\r\n
0x4006003a | The oldest shadow copy of volume %2 was deleted to keep the total number of shadow copies of volume %2 below a limit.\r\n
0x40060040 | Volume %2 is being reverted to the state of a previous shadow copy.\r\n
0x40060041 | The reverting of volume %2 is being restarted.  This is most likely because of a system shutdown or a system crash.\r\n
0x40060042 | The reverting of volume %2 to the state of a previous shadow copy is complete.\r\n
0x80060018 | There was insufficient disk space on volume %3 to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006001e | An unfinished create of a shadow copy of volume %2 was deleted.\r\n
0x80060026 | There was a user imposed limit that prevented disk space on volume %3 from being used to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006003d | The revert operation on volume %2 encountered a bad sector error.  Please validate the data on this volume.\r\n
0x8006003e | The revert operation on volume %2 stopped because of the loss of a volume.  When the volume is re-introduced, the revert will continue.  You may have to reboot to trigger the revert.\r\n
0x90000001 | Microsoft-Windows-VolumeSnapshot-Driver\r\n
0xc0060001 | The shadow copy of volume %2 could not create shadow copy storage on volume %3.\r\n
0xc0060002 | The shadow copy of volume %2 could not be created because volume %3, which is specified as the location for shadow copy storage, is not an NTFS volume or an error was encountered while trying to determine the file system type of this volume.\r\n
0xc0060003 | The shadow copy of volume %2 could not lock down the location of the shadow copy storage on volume %3.\r\n
0xc0060004 | The shadow copy of volume %2 could not be created due to insufficient resources for worker threads.\r\n
0xc0060005 | The shadow copy of volume %2 could not be created due to insufficient non-paged memory pool for a bitmap structure.\r\n
0xc0060006 | The shadow copy of volume %2 could not create a new paged heap.  The system may be low on virtual memory.\r\n
0xc0060007 | The shadow copy of volume %2 failed to query the shadow copy storage mappings on volume %3.\r\n
0xc0060008 | The flush and hold writes operation on volume %2 timed out while waiting for a release writes command.\r\n
0xc0060009 | The flush and hold writes operation on volume %2 timed out while waiting for file system cleanup.\r\n
0xc006000a | The shadow copy of volume %2 took too long to install.\r\n
0xc006000c | The shadow copy of volume %2 became low on shadow copy storage before it was properly installed.\r\n
0xc006000d | The shadow copy of volume %2 could not grow its shadow copy storage on volume %3.\r\n
0xc006000e | The shadow copies of volume %2 were aborted because of an IO failure on volume %3.\r\n
0xc006000f | The shadow copies of volume %2 were aborted because of insufficient paged heap.\r\n
0xc0060010 | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, was force dismounted.\r\n
0xc0060011 | An attempt to flush and hold writes on volume %2 was attempted while another flush and hold was already in progress.\r\n
0xc0060014 | The shadow copies of volume %2 were aborted because of a failed free space computation.\r\n
0xc0060015 | The flush and hold operation for volume %2 was aborted because of low available system memory.\r\n
0xc0060016 | The shadow copy storage volume specified for shadow copies on volume %2 could not be added.\r\n
0xc0060017 | There was insufficient disk space on volume %3 to create the shadow copy of volume %2.  Shadow copy storage creation failed.\r\n
0xc0060019 | The shadow copies of volume %2 were deleted because the shadow copy storage could not grow in time.  Consider reducing the IO load on the system or choose a shadow copy storage volume that is not being shadow copied.\r\n
0xc006001b | The shadow copies of volume %2 were aborted during detection because a critical control file could not be opened.\r\n
0xc006001c | The shadow copy of volume %2 could not be created due to a failure in creating the necessary on disk structures.\r\n
0xc006001d | The shadow copies of volume %2 were aborted during detection.\r\n
0xc006001f | A control item for shadow copies of volume %2 was lost during detection.\r\n
0xc0060020 | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present.\r\n
0xc0060022 | The shadow copies of volume %2 were aborted because of a failure to ensure crash dump or hibernate consistency.\r\n
0xc0060023 | The shadow copies of volume %2 were aborted because the shadow copy storage failed to grow.\r\n
0xc0060024 | The shadow copies of volume %2 were aborted because the shadow copy storage could not grow due to a user imposed limit.\r\n
0xc0060025 | The shadow copies of volume %2 were aborted in preparation for hibernation because this volume is used for hibernation and is not an NTFS volume.\r\n
0xc0060027 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 could not be located in non-critical space.  Consider using a shadow copy storage volume that does not have any shadow copies.\r\n
0xc0060028 | The shadow copies of volume %2 were aborted because volume %3 has been dismounted.\r\n
0xc0060029 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  Consider deleting unnecessary files on the shadow copy storage volume or use a different shadow copy storage volume.\r\n
0xc0060030 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  A shadow copy create computation is in progress to find more contiguous blocks.\r\n
0xc006003b | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present in time during a previous session.\r\n
0xc006003c | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, has been taken offline.\r\n
0xc006003f | An error occurred while trying to delete a snapshot of %2.  The delete will be retried at a later time.\r\n
0xc0060043 | The shadow copy of volume %2 being created failed to install.\r\n

### 6.1.7600.16385, 6.1.7601.17514, 6.2.9200.16384, 6.3.9600.16384, 6.3.9600.18265

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-VolumeSnapshot-Driver\r\n
0x40060021 | The oldest shadow copy of volume %2 was deleted to keep disk space usage for shadow copies of volume %2 below the user defined limit.\r\n
0x4006003a | The oldest shadow copy of volume %2 was deleted to keep the total number of shadow copies of volume %2 below a limit.\r\n
0x40060040 | Volume %2 is being reverted to the state of a previous shadow copy.\r\n
0x40060041 | The reverting of volume %2 is being restarted.  This is most likely because of a system shutdown or a system crash.\r\n
0x40060042 | The reverting of volume %2 to the state of a previous shadow copy is complete.\r\n
0x80060018 | There was insufficient disk space on volume %3 to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006001e | An unfinished create of a shadow copy of volume %2 was deleted.\r\n
0x80060026 | There was a user imposed limit that prevented disk space on volume %3 from being used to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006003d | The revert operation on volume %2 encountered a bad sector error.  Please validate the data on this volume.\r\n
0x8006003e | The revert operation on volume %2 stopped because of the loss of a volume.  When the volume is re-introduced, the revert will continue.  You may have to reboot to trigger the revert.\r\n
0xc0060001 | The shadow copy of volume %2 could not create shadow copy storage on volume %3.\r\n
0xc0060002 | The shadow copy of volume %2 could not be created because volume %3, which is specified as the location for shadow copy storage, is not an NTFS volume or an error was encountered while trying to determine the file system type of this volume.\r\n
0xc0060003 | The shadow copy of volume %2 could not lock down the location of the shadow copy storage on volume %3.\r\n
0xc0060004 | The shadow copy of volume %2 could not be created due to insufficient resources for worker threads.\r\n
0xc0060005 | The shadow copy of volume %2 could not be created due to insufficient non-paged memory pool for a bitmap structure.\r\n
0xc0060006 | The shadow copy of volume %2 could not create a new paged heap.  The system may be low on virtual memory.\r\n
0xc0060007 | The shadow copy of volume %2 failed to query the shadow copy storage mappings on volume %3.\r\n
0xc0060008 | The flush and hold writes operation on volume %2 timed out while waiting for a release writes command.\r\n
0xc0060009 | The flush and hold writes operation on volume %2 timed out while waiting for file system cleanup.\r\n
0xc006000a | The shadow copy of volume %2 took too long to install.\r\n
0xc006000d | The shadow copy of volume %2 could not grow its shadow copy storage on volume %3.\r\n
0xc006000e | The shadow copies of volume %2 were aborted because of an IO failure on volume %3.\r\n
0xc006000f | The shadow copies of volume %2 were aborted because of insufficient paged heap.\r\n
0xc0060010 | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, was force dismounted.\r\n
0xc0060011 | An attempt to flush and hold writes on volume %2 was attempted while another flush and hold was already in progress.\r\n
0xc0060014 | The shadow copies of volume %2 were aborted because of a failed free space computation.\r\n
0xc0060015 | The flush and hold operation for volume %2 was aborted because of low available system memory.\r\n
0xc0060016 | The shadow copy storage volume specified for shadow copies on volume %2 could not be added.\r\n
0xc0060017 | There was insufficient disk space on volume %3 to create the shadow copy of volume %2.  Shadow copy storage creation failed.\r\n
0xc0060019 | The shadow copies of volume %2 were deleted because the shadow copy storage could not grow in time.  Consider reducing the IO load on the system or choose a shadow copy storage volume that is not being shadow copied.\r\n
0xc006001b | The shadow copies of volume %2 were aborted during detection because a critical control file could not be opened.\r\n
0xc006001c | The shadow copy of volume %2 could not be created due to a failure in creating the necessary on disk structures.\r\n
0xc006001d | The shadow copies of volume %2 were aborted during detection.\r\n
0xc006001f | A control item for shadow copies of volume %2 was lost during detection.\r\n
0xc0060020 | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present.\r\n
0xc0060023 | The shadow copies of volume %2 were aborted because the shadow copy storage failed to grow.\r\n
0xc0060024 | The shadow copies of volume %2 were aborted because the shadow copy storage could not grow due to a user imposed limit.\r\n
0xc0060027 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 could not be located in non-critical space.  Consider using a shadow copy storage volume that does not have any shadow copies.\r\n
0xc0060028 | The shadow copies of volume %2 were aborted because volume %3 has been dismounted.\r\n
0xc0060029 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  Consider deleting unnecessary files on the shadow copy storage volume or use a different shadow copy storage volume.\r\n
0xc0060030 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  A shadow copy create computation is in progress to find more contiguous blocks.\r\n
0xc006003b | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present in time during a previous session.\r\n
0xc006003c | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, has been taken offline.\r\n
0xc006003f | An error occurred while trying to delete a snapshot of %2.  The delete will be retried at a later time.\r\n
0xc0060043 | The shadow copy of volume %2 being created failed to install.\r\n
0xc0060050 | Volume %2 is offline for shadow copy protection.  The shadow copy storage is not present.  This volume will go online and its shadow copies will become available once the shadow copy storage is introduced in the system.  Revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060051 | Volume %2 is offline for shadow copy protection.  An IO error occurred during shadow copy discovery.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060052 | Volume %2 is offline for shadow copy protection.  A shadow copy meta data corruption was detected.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060053 | Volume %2 is offline for shadow copy protection.  A memory allocation failed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060054 | Volume %2 is offline for shadow copy protection.  A memory mapping failed.  Consider increasing the size of the page file.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060055 | Volume %2 is offline for shadow copy protection.  A read failure occurred during a shadow copy on write operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060056 | Volume %2 is offline for shadow copy protection.  A read or write failure to shadow copy storage occurred.  Please ensure that the shadow copy storage is still present in the system.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060057 | Volume %2 is offline for shadow copy protection.  The shadow copy storage has been exhausted.  Please try clearing the protection fault or restart the computer followed by an increase of the shadow copy storage or a removal of unneeded shadow copies.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060058 | Volume %2 is offline for shadow copy protection.  The shadow copy storage was exhausted before conditions permitted it to grow.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060059 | Volume %2 is offline for shadow copy protection.  The shadow copy storage could not be increased as needed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005a | Volume %2 is offline for shadow copy protection.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005b | Volume %2 is offline for shadow copy protection.  An error occurred when doing a file system operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005c | Volume %2 is offline for shadow copy protection.  A read or write error occurred.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005d | Volume %2 is offline for shadow copy protection.  The shadow copy storage was made inaccessible or removed from the system.  Please ensure that the shadow copy storage is present.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005e | Volume %2 is offline for shadow copy protection.  An application attempted to write to the shadow copy meta data.  If this program was run intentionally then turn off protection mode for this volume in order to allow the application (which may be FORMAT) to run.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x10000038 | Classic\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x40060021 | The oldest shadow copy of volume %2 was deleted to keep disk space usage for shadow copies of volume %2 below the user defined limit.\r\n
0x4006003a | The oldest shadow copy of volume %2 was deleted to keep the total number of shadow copies of volume %2 below a limit.\r\n
0x40060040 | Volume %2 is being reverted to the state of a previous shadow copy.\r\n
0x40060041 | The reverting of volume %2 is being restarted.  This is most likely because of a system shutdown or a system crash.\r\n
0x40060042 | The reverting of volume %2 to the state of a previous shadow copy is complete.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80060018 | There was insufficient disk space on volume %3 to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006001e | An unfinished create of a shadow copy of volume %2 was deleted.\r\n
0x80060026 | There was a user imposed limit that prevented disk space on volume %3 from being used to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006003d | The revert operation on volume %2 encountered a bad sector error.  Please validate the data on this volume.\r\n
0x8006003e | The revert operation on volume %2 stopped because of the loss of a volume.  When the volume is re-introduced, the revert will continue.  You may have to reboot to trigger the revert.\r\n
0x90000001 | System\r\n
0x91000001 | Microsoft-Windows-VolumeSnapshot-Driver\r\n
0xb1000064 | The volume snapshot driver has begun processing for volume online.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online the volume snapshot driver scans for any persistent snapshots that may be on the volume.%n%nYou should expect this event when a volume is brought online.  No user action is required.\r\n
0xb1000065 | The volume snapshot driver has completed processing for volume online.%n%nVolume GUID: %1%n%nGuidance:%nThe volume snapshot driver was able to scan for any persistent snapshots on this volume.%n%nYou should expect this event when a volume is brought online.  No user action is required.\r\n
0xb1000066 | The volume snapshot driver encountered an error while performing processing for volume online.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online the volume snapshot driver scans for any persistent snapshots that may be on the volume.  In case of an error this scan is not performed.  The error may have originated in storage drivers beneath the volume snapshot driver; check their logs.%n%nIf the error is STATUS_DEVICE_NOT_CONNECTED this means the volume is in snapshot protection mode and has been taken offline to prevent loss of snapshots.\r\n
0xb1000067 | Activation of discovered snapshots began.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.%n%nYou should expect this event when a volume is brought online or reverted to a snapshot.  No user action is required.\r\n
0xb1000068 | Activation of discovered snapshots completed.%n%nVolume GUID: %1%nTotal Number of Snapshots Found: %2%nNumber of Snapshots Marked for Delete: %3%nNumber of Visible Snapshots Found: %4%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  Some snapshots may be marked 'visible', meaning they were exposed as a local volume or file share.  Some detected snapshots may be marked 'deleted', meaning they are no longer available for use and their diff area space will be reclaimed when all older snapshots are deleted.  Look for instances of event 106 to see each snapshot that was discovered and whether it was 'visible' or 'deleted'.%n%nYou should expect this event when a volume is brought online or reverted to a snapshot.  No user action is required.\r\n
0xb1000069 | Activation of discovered snapshots encountered an error.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  Unless the volume is in snapshot protection mode or the error code indicates the volume is offline, a failure during this process results in loss of all snapshots on the volume.\r\n
0xb100006a | A persistent snapshot was activated.%n%nVolume GUID: %1%nSnapshot GUID: %2%nSnapshot Marked Deleted: %3%nSnapshot Visible: %4%nSnapshot Commit Timestamp: %5%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  If the snapshot is 'visible', it was exposed as a local volume or file share.  If the snapshot is 'deleted', it is no longer available for use and its diff area space will be reclaimed when all older snapshots are deleted.%n%nYou should expect this event when a volume containing persistent snapshots is brought online or reverted to a snapshot.  If all discovered snapshots are successfully activated you should expect event 104, otherwise you will see event 105.  No user action is required.\r\n
0xb100006b | Reading of a snapshot diff area's metadata began.%n%nVolume GUID: %1%nSnapshot GUID: %2%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.%n%nYou should expect this event when a volume is brought online, reverted to a snapshot, or when reading from a persistent snapshot for the first time after bringing a volume online.  This event may also occur if a volume is dismounted that contains snapshots that have not been read since the volume was brought online.  No user action is required.\r\n
0xb100006e | Validation of diff area files began.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.%n%nYou should expect this event when mounting a volume.  No user action is required.\r\n
0xb100006f | Validation of diff area files completed.%n%nNumber of Diff Areas: %2%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.%n%nYou should expect this event when mounting a volume.  No user action is required.\r\n
0xb1000070 | Validation of diff area files encountered an error.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.  A failure during this process results in loss of all snapshots whose diff area files are located on the volume, unless those snapshots are of volumes that are in snapshot protection mode.\r\n
0xb1000071 | The volume is preparing to be taken offline.%n%nVolume GUID: %1%n%nGuidance:%nSome system services, such as the cluster service, inform the volume snapshot driver when they are about to take the volume offline.%n%nYou should expect this event when an entity such as the cluster service prepares to take a volume offline.  No user action is required.\r\n
0xb1000072 | The volume snapshot driver has begun processing for dismount.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nYou should expect this event when a volume dismounts.  No user action is required.\r\n
0xb1000073 | The volume snapshot driver has completed processing for dismount.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nYou should expect this event when a volume dismounts.  No user action is required.\r\n
0xb1000074 | The volume snapshot driver has begun processing for volume offline.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nYou should expect this event when a volume is taken offline.  No user action is required.\r\n
0xb1000075 | The volume snapshot driver has completed processing for volume offline.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nYou should expect this event when a volume is taken offline.  No user action is required.\r\n
0xb1000076 | The volume snapshot driver encountered an error while performing processing for volume offline.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nIf the error is STATUS_INSUFFICIENT_RESOURCES (0xc000009a), the volume snapshot driver may have been unable to allocate memory.  Other error codes originate from lower drivers.  Please check their log(s) for further information.\r\n
0xb1000077 | The volume snapshot driver encountered an error while performing processing for dismount.%n%nError: %3%nError Details: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nA failure during this process results in loss of all snapshots whose diff area files are located on the volume, unless those snapshots are of volumes that are in snapshot protection mode.\r\n
0xb1000078 | Activation of discovered snapshots took too long and was aborted.%n%nVolume GUID: %1%nTimeout Value (in seconds): %2%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  This process took longer than the amount of time allowed on this system, so activation has been aborted.  Unless the volume is in snapshot protection mode, all snapshots on this volume have been deleted.\r\n
0xb1000079 | The volume snapshot driver was unable to log an event to the legacy System event log.%n%nVolume Name: %2%nDiff Volume Name (if applicable): %4%nOriginal Error Event Code: %5%nOriginal Error Status: %6%nCause of Logging Failure:%10\r\n
0xb10003e8 | PrepareForSnapshot (Enter)\r\n
0xb10003e9 | PrepareForSnapshot (Leave)\r\n
0xb10003ea | PreExposure (Enter)\r\n
0xb10003eb | PreExposure (Leave)\r\n
0xb10003ec | AdjustBitmap (Enter)\r\n
0xb10003ed | AdjustBitmap (Leave)\r\n
0xb10003ee | EndCommit (Enter)\r\n
0xb10003ef | EndCommit (Leave)\r\n
0xb10003f0 | Activate (Enter)\r\n
0xb10003f1 | Activate (Leave)\r\n
0xb10003f2 | SetIgnorable (Enter)\r\n
0xb10003f3 | SetIgnorable (Leave)\r\n
0xb10003f4 | ComputeIgnorableProduct (Enter)\r\n
0xb10003f5 | ComputeIgnorableProduct (Leave)\r\n
0xb10003f6 | Dismount (Enter)\r\n
0xb10003f7 | Dismount (Leave)\r\n
0xb10003f8 | Remount (Enter)\r\n
0xb10003f9 | Remount (Leave)\r\n
0xb10003fa | DeleteProcess (Enter)\r\n
0xb10003fb | DeleteProcess (Leave)\r\n
0xb10003fc | Revert (Enter)\r\n
0xb10003fd | Revert (Leave)\r\n
0xb10003fe | ComputeProtectedBitmap (Enter)\r\n
0xb10003ff | ComputeProtectedBitmap (Leave)\r\n
0xb1000400 | FlushHoldFs (Enter)\r\n
0xb1000401 | FlushHoldFs (Leave)\r\n
0xb1000402 | ActivateLoop (Enter)\r\n
0xb1000403 | ActivateLoop (Leave)\r\n
0xb1000404 | ValidateDiffAreaFiles (Enter)\r\n
0xb1000405 | ValidateDiffAreaFiles (Leave)\r\n
0xb1000406 | VolumesSafeForWrite (Enter)\r\n
0xb1000407 | VolumesSafeForWrite (Leave)\r\n
0xb1000408 | DiscoverSnapshots (Enter)\r\n
0xb1000409 | DiscoverSnapshots (Leave)\r\n
0xb102006c | Reading of a snapshot diff area's metadata completed.%n%nVolume GUID: %1%nSnapshot GUID: %2%nCount of 1MB Reads: %3%nCount of 16KB Reads: %4%nDiff Area Metadata Size: %5 Bytes%nTotal Data Read: %6 Bytes%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.  The size of the diff area metadata may be less than the total number of bytes read if the diff area is discontiguous on disk.%n%nYou should expect this event when a volume is brought online, reverted to a snapshot, or when reading from a persistent snapshot for the first time after bringing a volume online.  This event may also occur if a volume is dismounted that contains snapshots that have not been read since the volume was brought online.  No user action is required.\r\n
0xb102006d | Reading of a snapshot diff area's metadata encountered an error.%n%nError: %3%n%nVolume GUID: %1%nSnapshot GUID: %2%nCount of 1MB Reads: %4%nCount of 16KB Reads: %5%nAmount of Diff Area Metadata Read: %6 Bytes%nTotal Data Read: %7 Bytes%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.  Unless the volume is in snapshot protection mode, a failure during this process results in loss of all snapshots on the volume.\r\n
0xc0060001 | The shadow copy of volume %2 could not create shadow copy storage on volume %3.\r\n
0xc0060002 | The shadow copy of volume %2 could not be created because volume %3, which is specified as the location for shadow copy storage, is not an NTFS volume or an error was encountered while trying to determine the file system type of this volume.\r\n
0xc0060003 | The shadow copy of volume %2 could not lock down the location of the shadow copy storage on volume %3.\r\n
0xc0060004 | The shadow copy of volume %2 could not be created due to insufficient resources for worker threads.\r\n
0xc0060005 | The shadow copy of volume %2 could not be created due to insufficient non-paged memory pool for a bitmap structure.\r\n
0xc0060006 | The shadow copy of volume %2 could not create a new paged heap.  The system may be low on virtual memory.\r\n
0xc0060007 | The shadow copy of volume %2 failed to query the shadow copy storage mappings on volume %3.\r\n
0xc0060008 | The flush and hold writes operation on volume %2 timed out while waiting for a release writes command.\r\n
0xc0060009 | The flush and hold writes operation on volume %2 timed out while waiting for file system cleanup.\r\n
0xc006000a | The shadow copy of volume %2 took too long to install.\r\n
0xc006000d | The shadow copy of volume %2 could not grow its shadow copy storage on volume %3.\r\n
0xc006000e | The shadow copies of volume %2 were aborted because of an IO failure on volume %3.\r\n
0xc006000f | The shadow copies of volume %2 were aborted because of insufficient paged heap.\r\n
0xc0060010 | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, was force dismounted.\r\n
0xc0060011 | An attempt to flush and hold writes on volume %2 was attempted while another flush and hold was already in progress.\r\n
0xc0060014 | The shadow copies of volume %2 were aborted because of a failed free space computation.\r\n
0xc0060015 | The flush and hold operation for volume %2 was aborted because of low available system memory.\r\n
0xc0060016 | The shadow copy storage volume specified for shadow copies on volume %2 could not be added.\r\n
0xc0060017 | There was insufficient disk space on volume %3 to create the shadow copy of volume %2.  Shadow copy storage creation failed.\r\n
0xc0060019 | The shadow copies of volume %2 were deleted because the shadow copy storage could not grow in time.  Consider reducing the IO load on the system or choose a shadow copy storage volume that is not being shadow copied.\r\n
0xc006001b | The shadow copies of volume %2 were aborted during detection because a critical control file could not be opened.\r\n
0xc006001c | The shadow copy of volume %2 could not be created due to a failure in creating the necessary on disk structures.\r\n
0xc006001d | The shadow copies of volume %2 were aborted during detection.\r\n
0xc006001f | A control item for shadow copies of volume %2 was lost during detection.\r\n
0xc0060020 | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present.\r\n
0xc0060023 | The shadow copies of volume %2 were aborted because the shadow copy storage failed to grow.\r\n
0xc0060024 | The shadow copies of volume %2 were aborted because the shadow copy storage could not grow due to a user imposed limit.\r\n
0xc0060027 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 could not be located in non-critical space.  Consider using a shadow copy storage volume that does not have any shadow copies.\r\n
0xc0060028 | The shadow copies of volume %2 were aborted because volume %3 has been dismounted.\r\n
0xc0060029 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  Consider deleting unnecessary files on the shadow copy storage volume or use a different shadow copy storage volume.\r\n
0xc0060030 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  A shadow copy create computation is in progress to find more contiguous blocks.\r\n
0xc006003b | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present in time during a previous session.\r\n
0xc006003c | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, has been taken offline.\r\n
0xc006003f | An error occurred while trying to delete a snapshot of %2.  The delete will be retried at a later time.\r\n
0xc0060043 | The shadow copy of volume %2 being created failed to install.\r\n
0xc0060050 | Volume %2 is offline for shadow copy protection.  The shadow copy storage is not present.  This volume will go online and its shadow copies will become available once the shadow copy storage is introduced in the system.  Revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060051 | Volume %2 is offline for shadow copy protection.  An IO error occurred during shadow copy discovery.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060052 | Volume %2 is offline for shadow copy protection.  A shadow copy meta data corruption was detected.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060053 | Volume %2 is offline for shadow copy protection.  A memory allocation failed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060054 | Volume %2 is offline for shadow copy protection.  A memory mapping failed.  Consider increasing the size of the page file.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060055 | Volume %2 is offline for shadow copy protection.  A read failure occurred during a shadow copy on write operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060056 | Volume %2 is offline for shadow copy protection.  A read or write failure to shadow copy storage occurred.  Please ensure that the shadow copy storage is still present in the system.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060057 | Volume %2 is offline for shadow copy protection.  The shadow copy storage has been exhausted.  Please try clearing the protection fault or restart the computer followed by an increase of the shadow copy storage or a removal of unneeded shadow copies.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060058 | Volume %2 is offline for shadow copy protection.  The shadow copy storage was exhausted before conditions permitted it to grow.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060059 | Volume %2 is offline for shadow copy protection.  The shadow copy storage could not be increased as needed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005a | Volume %2 is offline for shadow copy protection.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005b | Volume %2 is offline for shadow copy protection.  An error occurred when doing a file system operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005c | Volume %2 is offline for shadow copy protection.  A read or write error occurred.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005d | Volume %2 is offline for shadow copy protection.  The shadow copy storage was made inaccessible or removed from the system.  Please ensure that the shadow copy storage is present.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005e | Volume %2 is offline for shadow copy protection.  An application attempted to write to the shadow copy meta data.  If this program was run intentionally then turn off protection mode for this volume in order to allow the application (which may be FORMAT) to run.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xd1000001 | Not applicable.\r\n
0xd1000002 | An volume offline for cluster failover was expected, but a mount request arrived instead.  A failure occurred attempting to take the volume offline to compensate.\r\n
0xd1000003 | Error validating diff area files.\r\n
0xd1000004 | There were no persistent snapshots on the volume.\r\n
0xd1000005 | Error calculating the protected blocks bitmap.\r\n
0xd1000006 | Could not allocate the protected blocks bitmap.\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1

Message identifier | Message string
--- | ---
0x10000038 | Classic\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x40060021 | The oldest shadow copy of volume %2 was deleted to keep disk space usage for shadow copies of volume %2 below the user defined limit.\r\n
0x4006003a | The oldest shadow copy of volume %2 was deleted to keep the total number of shadow copies of volume %2 below a limit.\r\n
0x40060040 | Volume %2 is being reverted to the state of a previous shadow copy.\r\n
0x40060041 | The reverting of volume %2 is being restarted.  This is most likely because of a system shutdown or a system crash.\r\n
0x40060042 | The reverting of volume %2 to the state of a previous shadow copy is complete.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80060018 | There was insufficient disk space on volume %3 to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006001e | An unfinished create of a shadow copy of volume %2 was deleted.\r\n
0x80060026 | There was a user imposed limit that prevented disk space on volume %3 from being used to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006003d | The revert operation on volume %2 encountered a bad sector error.  Please validate the data on this volume.\r\n
0x8006003e | The revert operation on volume %2 stopped because of the loss of a volume.  When the volume is re-introduced, the revert will continue.  You may have to reboot to trigger the revert.\r\n
0x90000001 | System\r\n
0x91000001 | Microsoft-Windows-VolumeSnapshot-Driver\r\n
0xb1000064 | The volume snapshot driver has begun processing for volume online.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online the volume snapshot driver scans for any persistent snapshots that may be on the volume.%n%nYou should expect this event when a volume is brought online.  No user action is required.\r\n
0xb1000065 | The volume snapshot driver has completed processing for volume online.%n%nVolume GUID: %1%n%nGuidance:%nThe volume snapshot driver was able to scan for any persistent snapshots on this volume.%n%nYou should expect this event when a volume is brought online.  No user action is required.\r\n
0xb1000066 | The volume snapshot driver encountered an error while performing processing for volume online.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online the volume snapshot driver scans for any persistent snapshots that may be on the volume.  In case of an error this scan is not performed.  The error may have originated in storage drivers beneath the volume snapshot driver; check their logs.%n%nIf the error is STATUS_DEVICE_NOT_CONNECTED this means the volume is in snapshot protection mode and has been taken offline to prevent loss of snapshots.\r\n
0xb1000067 | Activation of discovered snapshots began.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.%n%nYou should expect this event when a volume is brought online or reverted to a snapshot.  No user action is required.\r\n
0xb1000068 | Activation of discovered snapshots completed.%n%nVolume GUID: %1%nTotal Number of Snapshots Found: %2%nNumber of Snapshots Marked for Delete: %3%nNumber of Visible Snapshots Found: %4%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  Some snapshots may be marked 'visible', meaning they were exposed as a local volume or file share.  Some detected snapshots may be marked 'deleted', meaning they are no longer available for use and their diff area space will be reclaimed when all older snapshots are deleted.  Look for instances of event 106 to see each snapshot that was discovered and whether it was 'visible' or 'deleted'.%n%nYou should expect this event when a volume is brought online or reverted to a snapshot.  No user action is required.\r\n
0xb1000069 | Activation of discovered snapshots encountered an error.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  Unless the volume is in snapshot protection mode or the error code indicates the volume is offline, a failure during this process results in loss of all snapshots on the volume.\r\n
0xb100006a | A persistent snapshot was activated.%n%nVolume GUID: %1%nSnapshot GUID: %2%nSnapshot Marked Deleted: %3%nSnapshot Visible: %4%nSnapshot Commit Timestamp: %5%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  If the snapshot is 'visible', it was exposed as a local volume or file share.  If the snapshot is 'deleted', it is no longer available for use and its diff area space will be reclaimed when all older snapshots are deleted.%n%nYou should expect this event when a volume containing persistent snapshots is brought online or reverted to a snapshot.  If all discovered snapshots are successfully activated you should expect event 104, otherwise you will see event 105.  No user action is required.\r\n
0xb100006b | Reading of a snapshot diff area's metadata began.%n%nVolume GUID: %1%nSnapshot GUID: %2%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.%n%nYou should expect this event when a volume is brought online, reverted to a snapshot, or when reading from a persistent snapshot for the first time after bringing a volume online.  This event may also occur if a volume is dismounted that contains snapshots that have not been read since the volume was brought online.  No user action is required.\r\n
0xb100006e | Validation of diff area files began.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.%n%nYou should expect this event when mounting a volume.  No user action is required.\r\n
0xb100006f | Validation of diff area files completed.%n%nNumber of Diff Areas: %2%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.%n%nYou should expect this event when mounting a volume.  No user action is required.\r\n
0xb1000070 | Validation of diff area files encountered an error.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.  A failure during this process results in loss of all snapshots whose diff area files are located on the volume, unless those snapshots are of volumes that are in snapshot protection mode.\r\n
0xb1000071 | The volume is preparing to be taken offline.%n%nVolume GUID: %1%n%nGuidance:%nSome system services, such as the cluster service, inform the volume snapshot driver when they are about to take the volume offline.%n%nYou should expect this event when an entity such as the cluster service prepares to take a volume offline.  No user action is required.\r\n
0xb1000072 | The volume snapshot driver has begun processing for dismount.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nYou should expect this event when a volume dismounts.  No user action is required.\r\n
0xb1000073 | The volume snapshot driver has completed processing for dismount.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nYou should expect this event when a volume dismounts.  No user action is required.\r\n
0xb1000074 | The volume snapshot driver has begun processing for volume offline.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nYou should expect this event when a volume is taken offline.  No user action is required.\r\n
0xb1000075 | The volume snapshot driver has completed processing for volume offline.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nYou should expect this event when a volume is taken offline.  No user action is required.\r\n
0xb1000076 | The volume snapshot driver encountered an error while performing processing for volume offline.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nIf the error is STATUS_INSUFFICIENT_RESOURCES (0xc000009a), the volume snapshot driver may have been unable to allocate memory.  Other error codes originate from lower drivers.  Please check their log(s) for further information.\r\n
0xb1000077 | The volume snapshot driver encountered an error while performing processing for dismount.%n%nError: %3%nError Details: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nA failure during this process results in loss of all snapshots whose diff area files are located on the volume, unless those snapshots are of volumes that are in snapshot protection mode.\r\n
0xb1000078 | Activation of discovered snapshots took too long and was aborted.%n%nVolume GUID: %1%nTimeout Value (in seconds): %2%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  This process took longer than the amount of time allowed on this system, so activation has been aborted.  Unless the volume is in snapshot protection mode, all snapshots on this volume have been deleted.\r\n
0xb1000079 | The volume snapshot driver was unable to log an event to the legacy System event log.%n%nVolume Name: %2%nDiff Volume Name (if applicable): %4%nOriginal Error Event Code: %5%nOriginal Error Status: %6%nCause of Logging Failure:%10\r\n
0xb100007a | The volume snapshot driver encountered an error when attempting to determine whether the volume is clustered.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  This process attempts to determine whether the volume is part of a cluster shared resource, but the query to determine this failed.%n%nThis error does not indicate that any snapshots have been deleted.  You should expect this event if the volume is on a dynamic disk or is managed by a third-party volume manager.\r\n
0xb10003e8 | PrepareForSnapshot (Enter)\r\n
0xb10003e9 | PrepareForSnapshot (Leave)\r\n
0xb10003ea | PreExposure (Enter)\r\n
0xb10003eb | PreExposure (Leave)\r\n
0xb10003ec | AdjustBitmap (Enter)\r\n
0xb10003ed | AdjustBitmap (Leave)\r\n
0xb10003ee | EndCommit (Enter)\r\n
0xb10003ef | EndCommit (Leave)\r\n
0xb10003f0 | Activate (Enter)\r\n
0xb10003f1 | Activate (Leave)\r\n
0xb10003f2 | SetIgnorable (Enter)\r\n
0xb10003f3 | SetIgnorable (Leave)\r\n
0xb10003f4 | ComputeIgnorableProduct (Enter)\r\n
0xb10003f5 | ComputeIgnorableProduct (Leave)\r\n
0xb10003f6 | Dismount (Enter)\r\n
0xb10003f7 | Dismount (Leave)\r\n
0xb10003f8 | Remount (Enter)\r\n
0xb10003f9 | Remount (Leave)\r\n
0xb10003fa | DeleteProcess (Enter)\r\n
0xb10003fb | DeleteProcess (Leave)\r\n
0xb10003fc | Revert (Enter)\r\n
0xb10003fd | Revert (Leave)\r\n
0xb10003fe | ComputeProtectedBitmap (Enter)\r\n
0xb10003ff | ComputeProtectedBitmap (Leave)\r\n
0xb1000400 | FlushHoldFs (Enter)\r\n
0xb1000401 | FlushHoldFs (Leave)\r\n
0xb1000402 | ActivateLoop (Enter)\r\n
0xb1000403 | ActivateLoop (Leave)\r\n
0xb1000404 | ValidateDiffAreaFiles (Enter)\r\n
0xb1000405 | ValidateDiffAreaFiles (Leave)\r\n
0xb1000406 | VolumesSafeForWrite (Enter)\r\n
0xb1000407 | VolumesSafeForWrite (Leave)\r\n
0xb1000408 | DiscoverSnapshots (Enter)\r\n
0xb1000409 | DiscoverSnapshots (Leave)\r\n
0xb102006c | Reading of a snapshot diff area's metadata completed.%n%nVolume GUID: %1%nSnapshot GUID: %2%nCount of 1MB Reads: %3%nCount of 16KB Reads: %4%nDiff Area Metadata Size: %5 Bytes%nTotal Data Read: %6 Bytes%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.  The size of the diff area metadata may be less than the total number of bytes read if the diff area is discontiguous on disk.%n%nYou should expect this event when a volume is brought online, reverted to a snapshot, or when reading from a persistent snapshot for the first time after bringing a volume online.  This event may also occur if a volume is dismounted that contains snapshots that have not been read since the volume was brought online.  No user action is required.\r\n
0xb102006d | Reading of a snapshot diff area's metadata encountered an error.%n%nError: %3%n%nVolume GUID: %1%nSnapshot GUID: %2%nCount of 1MB Reads: %4%nCount of 16KB Reads: %5%nAmount of Diff Area Metadata Read: %6 Bytes%nTotal Data Read: %7 Bytes%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.  Unless the volume is in snapshot protection mode, a failure during this process results in loss of all snapshots on the volume.\r\n
0xc0060001 | The shadow copy of volume %2 could not create shadow copy storage on volume %3.\r\n
0xc0060002 | The shadow copy of volume %2 could not be created because volume %3, which is specified as the location for shadow copy storage, is not an NTFS volume or an error was encountered while trying to determine the file system type of this volume.\r\n
0xc0060003 | The shadow copy of volume %2 could not lock down the location of the shadow copy storage on volume %3.\r\n
0xc0060004 | The shadow copy of volume %2 could not be created due to insufficient resources for worker threads.\r\n
0xc0060005 | The shadow copy of volume %2 could not be created due to insufficient non-paged memory pool for a bitmap structure.\r\n
0xc0060006 | The shadow copy of volume %2 could not create a new paged heap.  The system may be low on virtual memory.\r\n
0xc0060007 | The shadow copy of volume %2 failed to query the shadow copy storage mappings on volume %3.\r\n
0xc0060008 | The flush and hold writes operation on volume %2 timed out while waiting for a release writes command.\r\n
0xc0060009 | The flush and hold writes operation on volume %2 timed out while waiting for file system cleanup.\r\n
0xc006000a | The shadow copy of volume %2 took too long to install.\r\n
0xc006000d | The shadow copy of volume %2 could not grow its shadow copy storage on volume %3.\r\n
0xc006000e | The shadow copies of volume %2 were aborted because of an IO failure on volume %3.\r\n
0xc006000f | The shadow copies of volume %2 were aborted because of insufficient paged heap.\r\n
0xc0060010 | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, was force dismounted.\r\n
0xc0060011 | An attempt to flush and hold writes on volume %2 was attempted while another flush and hold was already in progress.\r\n
0xc0060014 | The shadow copies of volume %2 were aborted because of a failed free space computation.\r\n
0xc0060015 | The flush and hold operation for volume %2 was aborted because of low available system memory.\r\n
0xc0060016 | The shadow copy storage volume specified for shadow copies on volume %2 could not be added.\r\n
0xc0060017 | There was insufficient disk space on volume %3 to create the shadow copy of volume %2.  Shadow copy storage creation failed.\r\n
0xc0060019 | The shadow copies of volume %2 were deleted because the shadow copy storage could not grow in time.  Consider reducing the IO load on the system or choose a shadow copy storage volume that is not being shadow copied.\r\n
0xc006001b | The shadow copies of volume %2 were aborted during detection because a critical control file could not be opened.\r\n
0xc006001c | The shadow copy of volume %2 could not be created due to a failure in creating the necessary on disk structures.\r\n
0xc006001d | The shadow copies of volume %2 were aborted during detection.\r\n
0xc006001f | A control item for shadow copies of volume %2 was lost during detection.\r\n
0xc0060020 | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present.\r\n
0xc0060023 | The shadow copies of volume %2 were aborted because the shadow copy storage failed to grow.\r\n
0xc0060024 | The shadow copies of volume %2 were aborted because the shadow copy storage could not grow due to a user imposed limit.\r\n
0xc0060027 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 could not be located in non-critical space.  Consider using a shadow copy storage volume that does not have any shadow copies.\r\n
0xc0060028 | The shadow copies of volume %2 were aborted because volume %3 has been dismounted.\r\n
0xc0060029 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  Consider deleting unnecessary files on the shadow copy storage volume or use a different shadow copy storage volume.\r\n
0xc0060030 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  A shadow copy create computation is in progress to find more contiguous blocks.\r\n
0xc006003b | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present in time during a previous session.\r\n
0xc006003c | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, has been taken offline.\r\n
0xc006003f | An error occurred while trying to delete a snapshot of %2.  The delete will be retried at a later time.\r\n
0xc0060043 | The shadow copy of volume %2 being created failed to install.\r\n
0xc0060050 | Volume %2 is offline for shadow copy protection.  The shadow copy storage is not present.  This volume will go online and its shadow copies will become available once the shadow copy storage is introduced in the system.  Revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060051 | Volume %2 is offline for shadow copy protection.  An IO error occurred during shadow copy discovery.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060052 | Volume %2 is offline for shadow copy protection.  A shadow copy meta data corruption was detected.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060053 | Volume %2 is offline for shadow copy protection.  A memory allocation failed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060054 | Volume %2 is offline for shadow copy protection.  A memory mapping failed.  Consider increasing the size of the page file.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060055 | Volume %2 is offline for shadow copy protection.  A read failure occurred during a shadow copy on write operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060056 | Volume %2 is offline for shadow copy protection.  A read or write failure to shadow copy storage occurred.  Please ensure that the shadow copy storage is still present in the system.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060057 | Volume %2 is offline for shadow copy protection.  The shadow copy storage has been exhausted.  Please try clearing the protection fault or restart the computer followed by an increase of the shadow copy storage or a removal of unneeded shadow copies.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060058 | Volume %2 is offline for shadow copy protection.  The shadow copy storage was exhausted before conditions permitted it to grow.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060059 | Volume %2 is offline for shadow copy protection.  The shadow copy storage could not be increased as needed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005a | Volume %2 is offline for shadow copy protection.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005b | Volume %2 is offline for shadow copy protection.  An error occurred when doing a file system operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005c | Volume %2 is offline for shadow copy protection.  A read or write error occurred.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005d | Volume %2 is offline for shadow copy protection.  The shadow copy storage was made inaccessible or removed from the system.  Please ensure that the shadow copy storage is present.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005e | Volume %2 is offline for shadow copy protection.  An application attempted to write to the shadow copy meta data.  If this program was run intentionally then turn off protection mode for this volume in order to allow the application (which may be FORMAT) to run.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xd1000001 | Not applicable.\r\n
0xd1000002 | An volume offline for cluster failover was expected, but a mount request arrived instead.  A failure occurred attempting to take the volume offline to compensate.\r\n
0xd1000003 | Error validating diff area files.\r\n
0xd1000004 | There were no persistent snapshots on the volume.\r\n
0xd1000005 | Error calculating the protected blocks bitmap.\r\n
0xd1000006 | Could not allocate the protected blocks bitmap.\r\n

### 10.0.17763.1, 10.0.18362.1, 10.0.18362.693, 10.0.19041.1, 10.0.19041.488

Message identifier | Message string
--- | ---
0x10000038 | Classic\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x40060021 | The oldest shadow copy of volume %2 was deleted to keep disk space usage for shadow copies of volume %2 below the user defined limit.\r\n
0x4006003a | The oldest shadow copy of volume %2 was deleted to keep the total number of shadow copies of volume %2 below a limit.\r\n
0x40060040 | Volume %2 is being reverted to the state of a previous shadow copy.\r\n
0x40060041 | The reverting of volume %2 is being restarted.  This is most likely because of a system shutdown or a system crash.\r\n
0x40060042 | The reverting of volume %2 to the state of a previous shadow copy is complete.\r\n
0x4006005f | The oldest shadow copy of volume %2 was deleted to allow shadow copies created afterward and marked for delete to be deleted.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80060018 | There was insufficient disk space on volume %3 to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006001e | An unfinished create of a shadow copy of volume %2 was deleted.\r\n
0x80060026 | There was a user imposed limit that prevented disk space on volume %3 from being used to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006003d | The revert operation on volume %2 encountered a bad sector error.  Please validate the data on this volume.\r\n
0x8006003e | The revert operation on volume %2 stopped because of the loss of a volume.  When the volume is re-introduced, the revert will continue.  You may have to reboot to trigger the revert.\r\n
0x90000001 | System\r\n
0x91000001 | Microsoft-Windows-VolumeSnapshot-Driver\r\n
0xb1000064 | The volume snapshot driver has begun processing for volume online.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online the volume snapshot driver scans for any persistent snapshots that may be on the volume.%n%nYou should expect this event when a volume is brought online.  No user action is required.\r\n
0xb1000065 | The volume snapshot driver has completed processing for volume online.%n%nVolume GUID: %1%n%nGuidance:%nThe volume snapshot driver was able to scan for any persistent snapshots on this volume.%n%nYou should expect this event when a volume is brought online.  No user action is required.\r\n
0xb1000066 | The volume snapshot driver encountered an error while performing processing for volume online.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online the volume snapshot driver scans for any persistent snapshots that may be on the volume.  In case of an error this scan is not performed.  The error may have originated in storage drivers beneath the volume snapshot driver; check their logs.%n%nIf the error is STATUS_DEVICE_NOT_CONNECTED this means the volume is in snapshot protection mode and has been taken offline to prevent loss of snapshots.\r\n
0xb1000067 | Activation of discovered snapshots began.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.%n%nYou should expect this event when a volume is brought online or reverted to a snapshot.  No user action is required.\r\n
0xb1000068 | Activation of discovered snapshots completed.%n%nVolume GUID: %1%nTotal Number of Snapshots Found: %2%nNumber of Snapshots Marked for Delete: %3%nNumber of Visible Snapshots Found: %4%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  Some snapshots may be marked 'visible', meaning they were exposed as a local volume or file share.  Some detected snapshots may be marked 'deleted', meaning they are no longer available for use and their diff area space will be reclaimed when all older snapshots are deleted.  Look for instances of event 106 to see each snapshot that was discovered and whether it was 'visible' or 'deleted'.%n%nYou should expect this event when a volume is brought online or reverted to a snapshot.  No user action is required.\r\n
0xb1000069 | Activation of discovered snapshots encountered an error.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  Unless the volume is in snapshot protection mode or the error code indicates the volume is offline, a failure during this process results in loss of all snapshots on the volume.\r\n
0xb100006a | A persistent snapshot was activated.%n%nVolume GUID: %1%nSnapshot GUID: %2%nSnapshot Marked Deleted: %3%nSnapshot Visible: %4%nSnapshot Commit Timestamp: %5%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  If the snapshot is 'visible', it was exposed as a local volume or file share.  If the snapshot is 'deleted', it is no longer available for use and its diff area space will be reclaimed when all older snapshots are deleted.%n%nYou should expect this event when a volume containing persistent snapshots is brought online or reverted to a snapshot.  If all discovered snapshots are successfully activated you should expect event 104, otherwise you will see event 105.  No user action is required.\r\n
0xb100006b | Reading of a snapshot diff area's metadata began.%n%nVolume GUID: %1%nSnapshot GUID: %2%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.%n%nYou should expect this event when a volume is brought online, reverted to a snapshot, or when reading from a persistent snapshot for the first time after bringing a volume online.  This event may also occur if a volume is dismounted that contains snapshots that have not been read since the volume was brought online.  No user action is required.\r\n
0xb100006e | Validation of diff area files began.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.%n%nYou should expect this event when mounting a volume.  No user action is required.\r\n
0xb100006f | Validation of diff area files completed.%n%nNumber of Diff Areas: %2%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.%n%nYou should expect this event when mounting a volume.  No user action is required.\r\n
0xb1000070 | Validation of diff area files encountered an error.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.  A failure during this process results in loss of all snapshots whose diff area files are located on the volume, unless those snapshots are of volumes that are in snapshot protection mode.\r\n
0xb1000071 | The volume is preparing to be taken offline.%n%nVolume GUID: %1%n%nGuidance:%nSome system services, such as the cluster service, inform the volume snapshot driver when they are about to take the volume offline.%n%nYou should expect this event when an entity such as the cluster service prepares to take a volume offline.  No user action is required.\r\n
0xb1000072 | The volume snapshot driver has begun processing for dismount.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nYou should expect this event when a volume dismounts.  No user action is required.\r\n
0xb1000073 | The volume snapshot driver has completed processing for dismount.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nYou should expect this event when a volume dismounts.  No user action is required.\r\n
0xb1000074 | The volume snapshot driver has begun processing for volume offline.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nYou should expect this event when a volume is taken offline.  No user action is required.\r\n
0xb1000075 | The volume snapshot driver has completed processing for volume offline.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nYou should expect this event when a volume is taken offline.  No user action is required.\r\n
0xb1000076 | The volume snapshot driver encountered an error while performing processing for volume offline.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nIf the error is STATUS_INSUFFICIENT_RESOURCES (0xc000009a), the volume snapshot driver may have been unable to allocate memory.  Other error codes originate from lower drivers.  Please check their log(s) for further information.\r\n
0xb1000077 | The volume snapshot driver encountered an error while performing processing for dismount.%n%nError: %3%nError Details: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nA failure during this process results in loss of all snapshots whose diff area files are located on the volume, unless those snapshots are of volumes that are in snapshot protection mode.\r\n
0xb1000078 | Activation of discovered snapshots took too long and was aborted.%n%nVolume GUID: %1%nTimeout Value (in seconds): %2%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  This process took longer than the amount of time allowed on this system, so activation has been aborted.  Unless the volume is in snapshot protection mode, all snapshots on this volume have been deleted.\r\n
0xb1000079 | The volume snapshot driver was unable to log an event to the legacy System event log.%n%nVolume Name: %2%nDiff Volume Name (if applicable): %4%nOriginal Error Event Code: %5%nOriginal Error Status: %6%nCause of Logging Failure:%10\r\n
0xb100007a | The volume snapshot driver encountered an error when attempting to determine whether the volume is clustered.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  This process attempts to determine whether the volume is part of a cluster shared resource, but the query to determine this failed.%n%nThis error does not indicate that any snapshots have been deleted.  You should expect this event if the volume is on a dynamic disk or is managed by a third-party volume manager.\r\n
0xb10003e8 | PrepareForSnapshot (Enter)\r\n
0xb10003e9 | PrepareForSnapshot (Leave)\r\n
0xb10003ea | PreExposure (Enter)\r\n
0xb10003eb | PreExposure (Leave)\r\n
0xb10003ec | AdjustBitmap (Enter)\r\n
0xb10003ed | AdjustBitmap (Leave)\r\n
0xb10003ee | EndCommit (Enter)\r\n
0xb10003ef | EndCommit (Leave)\r\n
0xb10003f0 | Activate (Enter)\r\n
0xb10003f1 | Activate (Leave)\r\n
0xb10003f2 | SetIgnorable (Enter)\r\n
0xb10003f3 | SetIgnorable (Leave)\r\n
0xb10003f4 | ComputeIgnorableProduct (Enter)\r\n
0xb10003f5 | ComputeIgnorableProduct (Leave)\r\n
0xb10003f6 | Dismount (Enter)\r\n
0xb10003f7 | Dismount (Leave)\r\n
0xb10003f8 | Remount (Enter)\r\n
0xb10003f9 | Remount (Leave)\r\n
0xb10003fa | DeleteProcess (Enter)\r\n
0xb10003fb | DeleteProcess (Leave)\r\n
0xb10003fc | Revert (Enter)\r\n
0xb10003fd | Revert (Leave)\r\n
0xb10003fe | ComputeProtectedBitmap (Enter)\r\n
0xb10003ff | ComputeProtectedBitmap (Leave)\r\n
0xb1000400 | FlushHoldFs (Enter)\r\n
0xb1000401 | FlushHoldFs (Leave)\r\n
0xb1000402 | ActivateLoop (Enter)\r\n
0xb1000403 | ActivateLoop (Leave)\r\n
0xb1000404 | ValidateDiffAreaFiles (Enter)\r\n
0xb1000405 | ValidateDiffAreaFiles (Leave)\r\n
0xb1000406 | VolumesSafeForWrite (Enter)\r\n
0xb1000407 | VolumesSafeForWrite (Leave)\r\n
0xb1000408 | DiscoverSnapshots (Enter)\r\n
0xb1000409 | DiscoverSnapshots (Leave)\r\n
0xb102006c | Reading of a snapshot diff area's metadata completed.%n%nVolume GUID: %1%nSnapshot GUID: %2%nCount of 1MB Reads: %3%nCount of 16KB Reads: %4%nDiff Area Metadata Size: %5 Bytes%nTotal Data Read: %6 Bytes%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.  The size of the diff area metadata may be less than the total number of bytes read if the diff area is discontiguous on disk.%n%nYou should expect this event when a volume is brought online, reverted to a snapshot, or when reading from a persistent snapshot for the first time after bringing a volume online.  This event may also occur if a volume is dismounted that contains snapshots that have not been read since the volume was brought online.  No user action is required.\r\n
0xb102006d | Reading of a snapshot diff area's metadata encountered an error.%n%nError: %3%n%nVolume GUID: %1%nSnapshot GUID: %2%nCount of 1MB Reads: %4%nCount of 16KB Reads: %5%nAmount of Diff Area Metadata Read: %6 Bytes%nTotal Data Read: %7 Bytes%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.  Unless the volume is in snapshot protection mode, a failure during this process results in loss of all snapshots on the volume.\r\n
0xc0060001 | The shadow copy of volume %2 could not create shadow copy storage on volume %3.\r\n
0xc0060002 | The shadow copy of volume %2 could not be created because volume %3, which is specified as the location for shadow copy storage, is not an NTFS volume or an error was encountered while trying to determine the file system type of this volume.\r\n
0xc0060003 | The shadow copy of volume %2 could not lock down the location of the shadow copy storage on volume %3.\r\n
0xc0060004 | The shadow copy of volume %2 could not be created due to insufficient resources for worker threads.\r\n
0xc0060005 | The shadow copy of volume %2 could not be created due to insufficient non-paged memory pool for a bitmap structure.\r\n
0xc0060006 | The shadow copy of volume %2 could not create a new paged heap.  The system may be low on virtual memory.\r\n
0xc0060007 | The shadow copy of volume %2 failed to query the shadow copy storage mappings on volume %3.\r\n
0xc0060008 | The flush and hold writes operation on volume %2 timed out while waiting for a release writes command.\r\n
0xc0060009 | The flush and hold writes operation on volume %2 timed out while waiting for file system cleanup.\r\n
0xc006000a | The shadow copy of volume %2 took too long to install.\r\n
0xc006000d | The shadow copy of volume %2 could not grow its shadow copy storage on volume %3.\r\n
0xc006000e | The shadow copies of volume %2 were aborted because of an IO failure on volume %3.\r\n
0xc006000f | The shadow copies of volume %2 were aborted because of insufficient paged heap.\r\n
0xc0060010 | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, was force dismounted.\r\n
0xc0060011 | An attempt to flush and hold writes on volume %2 was attempted while another flush and hold was already in progress.\r\n
0xc0060014 | The shadow copies of volume %2 were aborted because of a failed free space computation.\r\n
0xc0060015 | The flush and hold operation for volume %2 was aborted because of low available system memory.\r\n
0xc0060016 | The shadow copy storage volume specified for shadow copies on volume %2 could not be added.\r\n
0xc0060017 | There was insufficient disk space on volume %3 to create the shadow copy of volume %2.  Shadow copy storage creation failed.\r\n
0xc0060019 | The shadow copies of volume %2 were deleted because the shadow copy storage could not grow in time.  Consider reducing the IO load on the system or choose a shadow copy storage volume that is not being shadow copied.\r\n
0xc006001b | The shadow copies of volume %2 were aborted during detection because a critical control file could not be opened.\r\n
0xc006001c | The shadow copy of volume %2 could not be created due to a failure in creating the necessary on disk structures.\r\n
0xc006001d | The shadow copies of volume %2 were aborted during detection.\r\n
0xc006001f | A control item for shadow copies of volume %2 was lost during detection.\r\n
0xc0060020 | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present.\r\n
0xc0060023 | The shadow copies of volume %2 were aborted because the shadow copy storage failed to grow.\r\n
0xc0060024 | The shadow copies of volume %2 were aborted because the shadow copy storage could not grow due to a user imposed limit.\r\n
0xc0060027 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 could not be located in non-critical space.  Consider using a shadow copy storage volume that does not have any shadow copies.\r\n
0xc0060028 | The shadow copies of volume %2 were aborted because volume %3 has been dismounted.\r\n
0xc0060029 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  Consider deleting unnecessary files on the shadow copy storage volume or use a different shadow copy storage volume.\r\n
0xc0060030 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  A shadow copy create computation is in progress to find more contiguous blocks.\r\n
0xc006003b | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present in time during a previous session.\r\n
0xc006003c | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, has been taken offline.\r\n
0xc006003f | An error occurred while trying to delete a snapshot of %2.  The delete will be retried at a later time.\r\n
0xc0060043 | The shadow copy of volume %2 being created failed to install.\r\n
0xc0060050 | Volume %2 is offline for shadow copy protection.  The shadow copy storage is not present.  This volume will go online and its shadow copies will become available once the shadow copy storage is introduced in the system.  Revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060051 | Volume %2 is offline for shadow copy protection.  An IO error occurred during shadow copy discovery.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060052 | Volume %2 is offline for shadow copy protection.  A shadow copy meta data corruption was detected.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060053 | Volume %2 is offline for shadow copy protection.  A memory allocation failed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060054 | Volume %2 is offline for shadow copy protection.  A memory mapping failed.  Consider increasing the size of the page file.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060055 | Volume %2 is offline for shadow copy protection.  A read failure occurred during a shadow copy on write operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060056 | Volume %2 is offline for shadow copy protection.  A read or write failure to shadow copy storage occurred.  Please ensure that the shadow copy storage is still present in the system.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060057 | Volume %2 is offline for shadow copy protection.  The shadow copy storage has been exhausted.  Please try clearing the protection fault or restart the computer followed by an increase of the shadow copy storage or a removal of unneeded shadow copies.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060058 | Volume %2 is offline for shadow copy protection.  The shadow copy storage was exhausted before conditions permitted it to grow.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060059 | Volume %2 is offline for shadow copy protection.  The shadow copy storage could not be increased as needed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005a | Volume %2 is offline for shadow copy protection.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005b | Volume %2 is offline for shadow copy protection.  An error occurred when doing a file system operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005c | Volume %2 is offline for shadow copy protection.  A read or write error occurred.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005d | Volume %2 is offline for shadow copy protection.  The shadow copy storage was made inaccessible or removed from the system.  Please ensure that the shadow copy storage is present.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005e | Volume %2 is offline for shadow copy protection.  An application attempted to write to the shadow copy meta data.  If this program was run intentionally then turn off protection mode for this volume in order to allow the application (which may be FORMAT) to run.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xd1000001 | Not applicable.\r\n
0xd1000002 | An volume offline for cluster failover was expected, but a mount request arrived instead.  A failure occurred attempting to take the volume offline to compensate.\r\n
0xd1000003 | Error validating diff area files.\r\n
0xd1000004 | There were no persistent snapshots on the volume.\r\n
0xd1000005 | Error calculating the protected blocks bitmap.\r\n
0xd1000006 | Could not allocate the protected blocks bitmap.\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000038 | Classic\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x40060021 | The oldest shadow copy of volume %2 was deleted to keep disk space usage for shadow copies of volume %2 below the user defined limit.\r\n
0x4006003a | The oldest shadow copy of volume %2 was deleted to keep the total number of shadow copies of volume %2 below a limit.\r\n
0x40060040 | Volume %2 is being reverted to the state of a previous shadow copy.\r\n
0x40060041 | The reverting of volume %2 is being restarted.  This is most likely because of a system shutdown or a system crash.\r\n
0x40060042 | The reverting of volume %2 to the state of a previous shadow copy is complete.\r\n
0x4006005f | The oldest shadow copy of volume %2 was deleted to allow shadow copies created afterward and marked for delete to be deleted.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80060018 | There was insufficient disk space on volume %3 to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006001e | An unfinished create of a shadow copy of volume %2 was deleted.\r\n
0x80060026 | There was a user imposed limit that prevented disk space on volume %3 from being used to grow the shadow copy storage for shadow copies of %2.  As a result of this failure all shadow copies of volume %2 are at risk of being deleted.\r\n
0x8006003d | The revert operation on volume %2 encountered a bad sector error.  Please validate the data on this volume.\r\n
0x8006003e | The revert operation on volume %2 stopped because of the loss of a volume.  When the volume is re-introduced, the revert will continue.  You may have to reboot to trigger the revert.\r\n
0x90000001 | System\r\n
0x91000001 | Microsoft-Windows-VolumeSnapshot-Driver\r\n
0xb1000064 | The volume snapshot driver has begun processing for volume online.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online the volume snapshot driver scans for any persistent snapshots that may be on the volume.%n%nYou should expect this event when a volume is brought online.  No user action is required.\r\n
0xb1000065 | The volume snapshot driver has completed processing for volume online.%n%nVolume GUID: %1%n%nGuidance:%nThe volume snapshot driver was able to scan for any persistent snapshots on this volume.%n%nYou should expect this event when a volume is brought online.  No user action is required.\r\n
0xb1000066 | The volume snapshot driver encountered an error while performing processing for volume online.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online the volume snapshot driver scans for any persistent snapshots that may be on the volume.  In case of an error this scan is not performed.  The error may have originated in storage drivers beneath the volume snapshot driver; check their logs.%n%nIf the error is STATUS_DEVICE_NOT_CONNECTED this means the volume is in snapshot protection mode and has been taken offline to prevent loss of snapshots.\r\n
0xb1000067 | Activation of discovered snapshots began.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.%n%nYou should expect this event when a volume is brought online or reverted to a snapshot.  No user action is required.\r\n
0xb1000068 | Activation of discovered snapshots completed.%n%nVolume GUID: %1%nTotal Number of Snapshots Found: %2%nNumber of Snapshots Marked for Delete: %3%nNumber of Visible Snapshots Found: %4%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  Some snapshots may be marked 'visible', meaning they were exposed as a local volume or file share.  Some detected snapshots may be marked 'deleted', meaning they are no longer available for use and their diff area space will be reclaimed when all older snapshots are deleted.  Look for instances of event 106 to see each snapshot that was discovered and whether it was 'visible' or 'deleted'.%n%nYou should expect this event when a volume is brought online or reverted to a snapshot.  No user action is required.\r\n
0xb1000069 | Activation of discovered snapshots encountered an error.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  Unless the volume is in snapshot protection mode or the error code indicates the volume is offline, a failure during this process results in loss of all snapshots on the volume.\r\n
0xb100006a | A persistent snapshot was activated.%n%nVolume GUID: %1%nSnapshot GUID: %2%nSnapshot Marked Deleted: %3%nSnapshot Visible: %4%nSnapshot Commit Timestamp: %5%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  If the snapshot is 'visible', it was exposed as a local volume or file share.  If the snapshot is 'deleted', it is no longer available for use and its diff area space will be reclaimed when all older snapshots are deleted.%n%nYou should expect this event when a volume containing persistent snapshots is brought online or reverted to a snapshot.  If all discovered snapshots are successfully activated you should expect event 104, otherwise you will see event 105.  No user action is required.\r\n
0xb100006b | Reading of a snapshot diff area's metadata began.%n%nVolume GUID: %1%nSnapshot GUID: %2%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.%n%nYou should expect this event when a volume is brought online, reverted to a snapshot, or when reading from a persistent snapshot for the first time after bringing a volume online.  This event may also occur if a volume is dismounted that contains snapshots that have not been read since the volume was brought online.  No user action is required.\r\n
0xb100006e | Validation of diff area files began.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.%n%nYou should expect this event when mounting a volume.  No user action is required.\r\n
0xb100006f | Validation of diff area files completed.%n%nNumber of Diff Areas: %2%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.%n%nYou should expect this event when mounting a volume.  No user action is required.\r\n
0xb1000070 | Validation of diff area files encountered an error.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is mounted, the volume snapshot driver reads and validates all the diff area files located on the volume.  These diff area files may be for persistent snapshots of the volume being mounted, or for persistent snapshots of other volumes.  A failure during this process results in loss of all snapshots whose diff area files are located on the volume, unless those snapshots are of volumes that are in snapshot protection mode.\r\n
0xb1000071 | The volume is preparing to be taken offline.%n%nVolume GUID: %1%n%nGuidance:%nSome system services, such as the cluster service, inform the volume snapshot driver when they are about to take the volume offline.%n%nYou should expect this event when an entity such as the cluster service prepares to take a volume offline.  No user action is required.\r\n
0xb1000072 | The volume snapshot driver has begun processing for dismount.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nYou should expect this event when a volume dismounts.  No user action is required.\r\n
0xb1000073 | The volume snapshot driver has completed processing for dismount.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nYou should expect this event when a volume dismounts.  No user action is required.\r\n
0xb1000074 | The volume snapshot driver has begun processing for volume offline.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nYou should expect this event when a volume is taken offline.  No user action is required.\r\n
0xb1000075 | The volume snapshot driver has completed processing for volume offline.%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nYou should expect this event when a volume is taken offline.  No user action is required.\r\n
0xb1000076 | The volume snapshot driver encountered an error while performing processing for volume offline.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is taken offline, the volume snapshot driver disables any persistent snapshots that still exist for the volume (autorelease snapshots were deleted when the volume was dismounted).  Snapshots of other volumes whose diff areas are on the offlining volume are destroyed, unless those volumes are in snapshot protection mode.  In that case those volumes are taken offline.%n%nIf the error is STATUS_INSUFFICIENT_RESOURCES (0xc000009a), the volume snapshot driver may have been unable to allocate memory.  Other error codes originate from lower drivers.  Please check their log(s) for further information.\r\n
0xb1000077 | The volume snapshot driver encountered an error while performing processing for dismount.%n%nError: %3%nError Details: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is dismounted, the volume snapshot driver closes any handles it may have open on the dismounting volume, such as handles to diff areas.  All auto-release snapshots that have diff areas on the dismounting volume are deleted at this time. The volume snapshot driver may also perform some work to detect whether any future direct writes to the volume are to diff area space for persistent snapshots.  If such writes occur this detection work allows the volume snapshot driver to destroy the snapshots, since the direct volume writes may corrupt them.%n%nA failure during this process results in loss of all snapshots whose diff area files are located on the volume, unless those snapshots are of volumes that are in snapshot protection mode.\r\n
0xb1000078 | Activation of discovered snapshots took too long and was aborted.%n%nVolume GUID: %1%nTimeout Value (in seconds): %2%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  This process took longer than the amount of time allowed on this system, so activation has been aborted.  Unless the volume is in snapshot protection mode, all snapshots on this volume have been deleted.\r\n
0xb1000079 | The volume snapshot driver was unable to log an event to the legacy System event log.%n%nVolume Name: %2%nDiff Volume Name (if applicable): %4%nOriginal Error Event Code: %5%nOriginal Error Status: %6%nCause of Logging Failure:%10\r\n
0xb100007a | The volume snapshot driver encountered an error when attempting to determine whether the volume is clustered.%n%nError: %2%n%nVolume GUID: %1%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver scans for and activates any persistent snapshots that may be on the volume.  This process attempts to determine whether the volume is part of a cluster shared resource, but the query to determine this failed.%n%nThis error does not indicate that any snapshots have been deleted.  You should expect this event if the volume is on a dynamic disk or is managed by a third-party volume manager.\r\n
0xb100007b | Persistent snapshots are not supported on this edition of Windows.%n%nGuidance:%nThis edition of Windows does not support creation of persistent snapshots.  Autorelease snapshots are supported.\r\n
0xb10003e8 | PrepareForSnapshot (Enter)\r\n
0xb10003e9 | PrepareForSnapshot (Leave)\r\n
0xb10003ea | PreExposure (Enter)\r\n
0xb10003eb | PreExposure (Leave)\r\n
0xb10003ec | AdjustBitmap (Enter)\r\n
0xb10003ed | AdjustBitmap (Leave)\r\n
0xb10003ee | EndCommit (Enter)\r\n
0xb10003ef | EndCommit (Leave)\r\n
0xb10003f0 | Activate (Enter)\r\n
0xb10003f1 | Activate (Leave)\r\n
0xb10003f2 | SetIgnorable (Enter)\r\n
0xb10003f3 | SetIgnorable (Leave)\r\n
0xb10003f4 | ComputeIgnorableProduct (Enter)\r\n
0xb10003f5 | ComputeIgnorableProduct (Leave)\r\n
0xb10003f6 | Dismount (Enter)\r\n
0xb10003f7 | Dismount (Leave)\r\n
0xb10003f8 | Remount (Enter)\r\n
0xb10003f9 | Remount (Leave)\r\n
0xb10003fa | DeleteProcess (Enter)\r\n
0xb10003fb | DeleteProcess (Leave)\r\n
0xb10003fc | Revert (Enter)\r\n
0xb10003fd | Revert (Leave)\r\n
0xb10003fe | ComputeProtectedBitmap (Enter)\r\n
0xb10003ff | ComputeProtectedBitmap (Leave)\r\n
0xb1000400 | FlushHoldFs (Enter)\r\n
0xb1000401 | FlushHoldFs (Leave)\r\n
0xb1000402 | ActivateLoop (Enter)\r\n
0xb1000403 | ActivateLoop (Leave)\r\n
0xb1000404 | ValidateDiffAreaFiles (Enter)\r\n
0xb1000405 | ValidateDiffAreaFiles (Leave)\r\n
0xb1000406 | VolumesSafeForWrite (Enter)\r\n
0xb1000407 | VolumesSafeForWrite (Leave)\r\n
0xb1000408 | DiscoverSnapshots (Enter)\r\n
0xb1000409 | DiscoverSnapshots (Leave)\r\n
0xb102006c | Reading of a snapshot diff area's metadata completed.%n%nVolume GUID: %1%nSnapshot GUID: %2%nCount of 1MB Reads: %3%nCount of 16KB Reads: %4%nDiff Area Metadata Size: %5 Bytes%nTotal Data Read: %6 Bytes%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.  The size of the diff area metadata may be less than the total number of bytes read if the diff area is discontiguous on disk.%n%nYou should expect this event when a volume is brought online, reverted to a snapshot, or when reading from a persistent snapshot for the first time after bringing a volume online.  This event may also occur if a volume is dismounted that contains snapshots that have not been read since the volume was brought online.  No user action is required.\r\n
0xb102006d | Reading of a snapshot diff area's metadata encountered an error.%n%nError: %3%n%nVolume GUID: %1%nSnapshot GUID: %2%nCount of 1MB Reads: %4%nCount of 16KB Reads: %5%nAmount of Diff Area Metadata Read: %6 Bytes%nTotal Data Read: %7 Bytes%n%nGuidance:%nWhen a volume is brought online or reverted to a snapshot, the volume snapshot driver reads the diff area for the most-recent persistent snapshot (if any).  The diff area for earlier persistent snapshots is typically read the first time the snapshot is read from.  Unless the volume is in snapshot protection mode, a failure during this process results in loss of all snapshots on the volume.\r\n
0xc0060001 | The shadow copy of volume %2 could not create shadow copy storage on volume %3.\r\n
0xc0060002 | The shadow copy of volume %2 could not be created because volume %3, which is specified as the location for shadow copy storage, is not an NTFS volume or an error was encountered while trying to determine the file system type of this volume.\r\n
0xc0060003 | The shadow copy of volume %2 could not lock down the location of the shadow copy storage on volume %3.\r\n
0xc0060004 | The shadow copy of volume %2 could not be created due to insufficient resources for worker threads.\r\n
0xc0060005 | The shadow copy of volume %2 could not be created due to insufficient non-paged memory pool for a bitmap structure.\r\n
0xc0060006 | The shadow copy of volume %2 could not create a new paged heap.  The system may be low on virtual memory.\r\n
0xc0060007 | The shadow copy of volume %2 failed to query the shadow copy storage mappings on volume %3.\r\n
0xc0060008 | The flush and hold writes operation on volume %2 timed out while waiting for a release writes command.\r\n
0xc0060009 | The flush and hold writes operation on volume %2 timed out while waiting for file system cleanup.\r\n
0xc006000a | The shadow copy of volume %2 took too long to install.\r\n
0xc006000d | The shadow copy of volume %2 could not grow its shadow copy storage on volume %3.\r\n
0xc006000e | The shadow copies of volume %2 were aborted because of an IO failure on volume %3.\r\n
0xc006000f | The shadow copies of volume %2 were aborted because of insufficient paged heap.\r\n
0xc0060010 | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, was force dismounted.\r\n
0xc0060011 | An attempt to flush and hold writes on volume %2 was attempted while another flush and hold was already in progress.\r\n
0xc0060014 | The shadow copies of volume %2 were aborted because of a failed free space computation.\r\n
0xc0060015 | The flush and hold operation for volume %2 was aborted because of low available system memory.\r\n
0xc0060016 | The shadow copy storage volume specified for shadow copies on volume %2 could not be added.\r\n
0xc0060017 | There was insufficient disk space on volume %3 to create the shadow copy of volume %2.  Shadow copy storage creation failed.\r\n
0xc0060019 | The shadow copies of volume %2 were deleted because the shadow copy storage could not grow in time.  Consider reducing the IO load on the system or choose a shadow copy storage volume that is not being shadow copied.\r\n
0xc006001b | The shadow copies of volume %2 were aborted during detection because a critical control file could not be opened.\r\n
0xc006001c | The shadow copy of volume %2 could not be created due to a failure in creating the necessary on disk structures.\r\n
0xc006001d | The shadow copies of volume %2 were aborted during detection.\r\n
0xc006001f | A control item for shadow copies of volume %2 was lost during detection.\r\n
0xc0060020 | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present.\r\n
0xc0060023 | The shadow copies of volume %2 were aborted because the shadow copy storage failed to grow.\r\n
0xc0060024 | The shadow copies of volume %2 were aborted because the shadow copy storage could not grow due to a user imposed limit.\r\n
0xc0060027 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 could not be located in non-critical space.  Consider using a shadow copy storage volume that does not have any shadow copies.\r\n
0xc0060028 | The shadow copies of volume %2 were aborted because volume %3 has been dismounted.\r\n
0xc0060029 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  Consider deleting unnecessary files on the shadow copy storage volume or use a different shadow copy storage volume.\r\n
0xc0060030 | When preparing a new volume shadow copy for volume %2, the shadow copy storage on volume %3 did not have sufficiently large contiguous blocks.  A shadow copy create computation is in progress to find more contiguous blocks.\r\n
0xc006003b | The shadow copies of volume %2 were aborted because the shadow copy storage volume was not present in time during a previous session.\r\n
0xc006003c | The shadow copies of volume %2 were aborted because volume %3, which contains shadow copy storage for this shadow copy, has been taken offline.\r\n
0xc006003f | An error occurred while trying to delete a snapshot of %2.  The delete will be retried at a later time.\r\n
0xc0060043 | The shadow copy of volume %2 being created failed to install.\r\n
0xc0060050 | Volume %2 is offline for shadow copy protection.  The shadow copy storage is not present.  This volume will go online and its shadow copies will become available once the shadow copy storage is introduced in the system.  Revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060051 | Volume %2 is offline for shadow copy protection.  An IO error occurred during shadow copy discovery.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060052 | Volume %2 is offline for shadow copy protection.  A shadow copy meta data corruption was detected.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060053 | Volume %2 is offline for shadow copy protection.  A memory allocation failed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060054 | Volume %2 is offline for shadow copy protection.  A memory mapping failed.  Consider increasing the size of the page file.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060055 | Volume %2 is offline for shadow copy protection.  A read failure occurred during a shadow copy on write operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060056 | Volume %2 is offline for shadow copy protection.  A read or write failure to shadow copy storage occurred.  Please ensure that the shadow copy storage is still present in the system.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060057 | Volume %2 is offline for shadow copy protection.  The shadow copy storage has been exhausted.  Please try clearing the protection fault or restart the computer followed by an increase of the shadow copy storage or a removal of unneeded shadow copies.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060058 | Volume %2 is offline for shadow copy protection.  The shadow copy storage was exhausted before conditions permitted it to grow.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc0060059 | Volume %2 is offline for shadow copy protection.  The shadow copy storage could not be increased as needed.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005a | Volume %2 is offline for shadow copy protection.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005b | Volume %2 is offline for shadow copy protection.  An error occurred when doing a file system operation.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005c | Volume %2 is offline for shadow copy protection.  A read or write error occurred.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005d | Volume %2 is offline for shadow copy protection.  The shadow copy storage was made inaccessible or removed from the system.  Please ensure that the shadow copy storage is present.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xc006005e | Volume %2 is offline for shadow copy protection.  An application attempted to write to the shadow copy meta data.  If this program was run intentionally then turn off protection mode for this volume in order to allow the application (which may be FORMAT) to run.  Please try clearing the protection fault or restart the computer.  If all else fails, revert out of shadow copy protection mode to reclaim the use of the volume while losing the shadow copies.\r\n
0xd1000001 | Not applicable.\r\n
0xd1000002 | An volume offline for cluster failover was expected, but a mount request arrived instead.  A failure occurred attempting to take the volume offline to compensate.\r\n
0xd1000003 | Error validating diff area files.\r\n
0xd1000004 | There were no persistent snapshots on the volume.\r\n
0xd1000005 | Error calculating the protected blocks bitmap.\r\n
0xd1000006 | Could not allocate the protected blocks bitmap.\r\n
