## ddputils.dll

Path: %SystemRoot%\System32\ddputils.dll

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00565301 | Reconciliation of chunk store is due.\r\n
0x00565302 | There are no actions associated with this job.\r\n
0x10000001 | Reporting\r\n
0x10000002 | Filter\r\n
0x10000003 | Kernel mode stream store\r\n
0x10000004 | Kernel mode chunk store\r\n
0x10000005 | Kernel mode chunk container\r\n
0x10000006 | Kernel mode file cache\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Data Deduplication Optimization Task\r\n
0x70000002 | Data Deduplication Garbage Collection Task\r\n
0x70000003 | Data Deduplication Scrubbing Task\r\n
0x70000004 | Data Deduplication Unoptimization Task\r\n
0x70000005 | Open stream store stream\r\n
0x70000006 | Prepare for paging IO\r\n
0x70000007 | Read stream map\r\n
0x70000008 | Read chunks\r\n
0x70000009 | Compute checksum\r\n
0x7000000a | Get container entry\r\n
0x7000000b | Get maximum generation for container\r\n
0x7000000c | Open chunk container\r\n
0x7000000d | Initialize chunk container redirection table\r\n
0x7000000e | Validate chunk container redirection table\r\n
0x7000000f | Get chunk container valid data length\r\n
0x70000010 | Get offset from chunk container redirection table\r\n
0x70000011 | Read chunk container block\r\n
0x70000012 | Clear chunk container block\r\n
0x70000013 | Copy chunk\r\n
0x70000014 | Initialize file cache\r\n
0x70000015 | Map file cache data\r\n
0x70000016 | Unpin file cache data\r\n
0x70000017 | Copy file cache data\r\n
0x70000018 | Read underlying file cache data\r\n
0x70000019 | Get chunk container file size\r\n
0x7000001a | Pin stream map\r\n
0x7000001b | Pin chunk container\r\n
0x7000001c | Pin chunk\r\n
0x7000001d | Allocate pool buffer\r\n
0x7000001e | Unpin chunk container\r\n
0x7000001f | Unpin chunk\r\n
0x70000020 | Dedup read processing\r\n
0x70000021 | Get first stream map entry\r\n
0x70000022 | Read chunk metadata\r\n
0x70000023 | Read chunk data\r\n
0x70000024 | Reference TlCache data\r\n
0x70000025 | Read chunk data from stream store\r\n
0x70000026 | Assemble chunk data\r\n
0x70000027 | Decompress chunk data\r\n
0x70000028 | Copy chunk data in to user buffer\r\n
0x70000029 | Insert chunk data in to tlcache\r\n
0x7000002a | Read data from dedup reparse point file\r\n
0x7000002b | Prepare stream map\r\n
0x7000002c | Patch clean ranges\r\n
0x7000002d | Writing data to dedup file\r\n
0x7000002e | Queue write request on dedup file\r\n
0x7000002f | Do copy on write work on dedup file\r\n
0x70000030 | Do full recall on dedup file\r\n
0x70000031 | Do partial recall on dedup file\r\n
0x70000032 | Do dummy paging read on dedup file\r\n
0x70000033 | Read clean data for recalling file\r\n
0x70000034 | Write clean data to dedup file normally\r\n
0x70000035 | Write clean data to dedup file paged\r\n
0x70000036 | Recall dedup file using paging Io\r\n
0x70000037 | Flush dedup file after recall\r\n
0x70000038 | Update bitmap after recall on dedup file\r\n
0x70000039 | Delete dedup reparse point\r\n
0x7000003a | Open dedup file\r\n
0x7000003b | Locking user buffer for read\r\n
0x7000003c | Get system address for MDL\r\n
0x7000003d | Read clean dedup file\r\n
0x7000003e | Get range state\r\n
0x7000003f | Get chunk body\r\n
0x70000040 | Release chunk\r\n
0x70000041 | Release decompress chunk context\r\n
0x70000042 | Prepare decompress chunk context\r\n
0x70000043 | Copy data to compressed buffer\r\n
0x70000044 | Release data from TL Cache\r\n
0x70000045 | Queue async read request\r\n
0x80565301 | The requested object was not found.\r\n
0x80565302 | One (or more) of the arguments given to the task scheduler is not valid.\r\n
0x80565303 | The specified object already exists.\r\n
0x80565304 | The specified path was not found.\r\n
0x80565305 | The specified user is invalid.\r\n
0x80565306 | The specified path is invalid.\r\n
0x80565307 | The specified name is invalid.\r\n
0x80565308 | The specified property is out of range.\r\n
0x80565309 | A required filter driver is either not installed, not loaded, or not ready for service.\r\n
0x8056530a | There is insufficient disk space to perform the requested operation.\r\n
0x8056530b | The specified volume type is not supported. Deduplication is supported on fixed, write-enabled NTFS data volumes.\r\n
0x8056530c | Data deduplication encountered an unexpected error. Check the Data Deduplication Operational event log for more information.\r\n
0x8056530d | The specified scan log cursor has expired.\r\n
0x8056530e | The file system might be corrupted.  Please run the CHKDSK utility.\r\n
0x8056530f | A volume shadow copy could not be created or was unexpectedly deleted.\r\n
0x80565310 | Data deduplication encountered a corrupted XML configuration file.\r\n
0x80565311 | The Data Deduplication service could not access the global configuration because the Cluster service is not running.\r\n
0x80565312 | The Data Deduplication service could not access the global configuration because it has not been installed yet.\r\n
0x80565313 | Data deduplication failed to access the volume. It may be offline.\r\n
0x80565314 | The module encountered an invalid parameter or a valid parameter with an invalid value, or an expected module parameter was not found. Check the operational event log for more information.\r\n
0x80565315 | An attempt was made to perform an initialization operation when initialization has already been completed.\r\n
0x80565316 | An attempt was made to perform an uninitialization operation when that operation has already been completed.\r\n
0x80565317 | The Data Deduplication service detected an internal folder that is not secure. To secure the folder, reinstall deduplication on the volume.\r\n
0x80565318 | Data chunking has already been initiated.\r\n
0x80565319 | An attempt was made to perform an operation from an invalid state.\r\n
0x8056531a | An attempt was made to perform an operation before initialization.\r\n
0x8056531b | Call ::PushBuffer to continue chunking or ::Drain to enumerate any partial chunks.\r\n
0x8056531c | The Data Deduplication service detected multiple chunk store folders; however, only one chunk store folder is permitted. To fix this issue, reinstall deduplication on the volume.\r\n
0x8056531d | The data is invalid.\r\n
0x8056531e | The process is in an unknown state.\r\n
0x8056531f | The process is not running.\r\n
0x80565320 | There was an error while opening the file.\r\n
0x80565321 | The job process could not start because the job was not found.\r\n
0x80565322 | The client process ID does not match the ID of the host process that was started.\r\n
0x80565323 | The specified volume is not enabled for deduplication.\r\n
0x80565324 | A zero-character chunk ID is not valid.\r\n
0x80565325 | The index is filled to capacity.\r\n
0x80565327 | Session already exists.\r\n
0x80565328 | The compression format selected is not supported.\r\n
0x80565329 | The compressed buffer is larger than the uncompressed buffer.\r\n
0x80565330 | The buffer is not large enough.\r\n
0x8056533a | Index Scratch Log Error in: Seek, Read, Write, or Create\r\n
0x8056533b | The job type is invalid.\r\n
0x8056533c | Persistence layer enumeration error.\r\n
0x8056533d | The operation was cancelled.\r\n
0x8056533e | This job will not run at the scheduled time because it requires more memory than is currently available.\r\n
0x80565341 | The job was terminated while in a cancel or pending state.\r\n
0x80565342 | The job was terminated while in a handshake pending state.\r\n
0x80565343 | The job was terminated due to a service shutdown.\r\n
0x80565344 | The job was abandoned before starting.\r\n
0x80565345 | The job process exited unexpectedly.\r\n
0x80565346 | The Data Deduplication service detected that the container cannot be compacted or updated because it has reached the maximum generation version. \r\n
0x80565347 | The corruption log has reached its maximum size.\r\n
0x80565348 | The data deduplication scrubbing job failed to process the corruption logs.\r\n
0x80565349 | Data deduplication failed to create new chunk store container files. Allocate more space to the volume.\r\n
0x80565350 | An error occurred while opening the file because the file was in use. \r\n
0x80565351 | An error was discovered while deduplicating the file. The file is now skipped.\r\n
0x80565352 | File Server Deduplication encountered corruption while enumerating chunks in a chunk store.\r\n
0x80565353 | The scan log is not valid.\r\n
0x80565354 | The data is invalid due to checksum (CRC) mismatch error.\r\n
0x80565355 | Data deduplication encountered file corruption error.\r\n
0x80565356 | Job completed with some errors. Check event logs for more details.\r\n
0x80565357 | Data deduplication is not supported on the version of the chunk store found on this volume.\r\n
0x80565358 | Data deduplication encountered an unknown version of chunk store on this volume.\r\n
0x80565359 | The job was assigned less memory than the minimum it needs to run.\r\n
0x8056535a | The data deduplication job schedule cannot be modified.\r\n
0x8056535b | The valid data length of chunk store container is misaligned.\r\n
0x8056535c | File access is denied.\r\n
0x8056535d | Data deduplication job stopped due to too many corrupted files.\r\n
0x8056535e | Data deduplication job stopped due to an internal error in the BCrypt SHA-512 provider.\r\n
0x8056535f | Data deduplication job stopped for store reconciliation.\r\n
0x80565360 | File skipped for deduplication due to its size.\r\n
0x80565361 | File skipped due to deduplication retry limit.\r\n
0x90000001 | Data Deduplication\r\n
0x90000002 | Application\r\n
0x91000001 | Data Deduplication Change Events\r\n
0xb0001000 | Volume "%1" appears as disconnected and it is ignored by the service.  You may want to rescan disks.   Error: %2.%n%3\r\n
0xb0001001 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3". Most likely the CPU is under heavy load.  Error: %4.%n%5\r\n
0xb0001002 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3".  Error: %4.%n%5\r\n
0xb0001003 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3" during Safe Mode. The Data Deduplication service cannot start while in safe mode.  Error: %4.%n%5\r\n
0xb0001004 | A critical component required by Data Deduplication is not registered. This might happen if an error occurred during Windows setup, or if the computer does not have the Windows Server 2012 or later version of Deduplication service installed. The error returned from CoCreateInstance on class with CLSID %1 and Name "%2" on machine "%3" is %4.%n%5\r\n
0xb0001005 | Data Deduplication service is shutting down due to idle timeout.%n%1\r\n
0xb0001006 | Data Deduplication service is shutting down due to shutdown event from the Service Control Manager.%n%1\r\n
0xb0001007 | Data Deduplication job of type "%1" on volume "%2" has completed with return code: %3%n%4\r\n
0xb0001008 | Data Deduplication error: Unexpected error calling routine %1.  hr = %2.%n%3\r\n
0xb0001009 | Data Deduplication error: Unexpected error.%n%1\r\n
0xb000100a | Data Deduplication warning: %1%nError: %2.%n%3\r\n
0xb000100b | Data Deduplication error: Unexpected COM error %1: %2.  Error code: %3.%n%4\r\n
0xb000100c | Data Deduplication was unable to access the following file or volume: "%1".  This file or volume might be locked by another application right now, or you might need to give Local System access to it.%n%2\r\n
0xb000100d | Data Deduplication encountered an unexpected error during volume scan of volumes mounted at "%1" ("%2"). To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100e | Data Deduplication was unable to create or access the shadow copy for volumes mounted at "%1" ("%2"). Possible causes include an improper Shadow Copy configuration, insufficient disk space, or extreme memory, I/O or CPU load of the system. To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100f | Data Deduplication was unable to access volumes mounted at "%1" ("%2"). Make sure that dismount or format operations do not happen while running deduplication.%n%3\r\n
0xb0001010 | Data Deduplication was unable to access a file or volume. Details:%n%n%1%n The volume may be inaccessible for I/O operations or marked read-only. In case of a cluster volume, this may be a transient failure during failover.%n%2\r\n
0xb0001011 | Data Deduplication was unable to scan volume "%1" ("%2").%n%3\r\n
0xb0001012 | Data Deduplication detected a corruption on file "%1" at offset ("%2").  If this condition persists then please restore the data from a previous backup.  Corruption details: Structure=%3, Corruption type = %4, Additional data = %5%n%6\r\n
0xb0001013 | Data Deduplication encountered failure while reconciling chunk store on volume "%1". The error code was %2. Reconciliation is disabled for the current optimization job.%n%3\r\n
0xb0001016 | Data Deduplication encountered corrupted chunk container %1 while performing full garbage collection. The corrupted chunk container is skipped.%n%2\r\n
0xb0001017 | Data Deduplication could not initialize change log under %1. The error code was %2.%n%3\r\n
0xb0001018 | Data Deduplication service could not mark chunk container %1 as reconciled. The error code was %2.%n%3\r\n
0xb0001019 | A Data Deduplication configuration file is corrupted. The system or volume may need to be restored from backup.%n%1\r\n
0xb000101a | Data Deduplication was unable to save one of the configuration stores on volume "%1" due to a disk-full error: If the disk is full, please clean it up (extend the volume or delete some files). If the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.%n%2\r\n
0xb000101b | Data Deduplication could not access global configuration since the cluster service is not running. Please start the cluster service and retry the operation.%n%1\r\n
0xb000101c | Shadow copy "%1" was deleted during storage report generation.  Volume "%2" might be configured with inadequate shadow copy storage area. Data Deduplication could not process this volume.%n%3\r\n
0xb000101d | Shadow copy creation failed for volume "%1" after retrying for %2 minutes because other shadow copies were being created.  Reschedule the Data Deduplication for a less busy time.%n%3\r\n
0xb000101e | Volume "%1" is not supported for shadow copy.  It is possible that the volume was removed from the system.  Data Deduplication service could not process this volume.%n%2\r\n
0xb000101f | The volume "%1" has been deleted or removed from the system.%n%2\r\n
0xb0001020 | Shadow copy creation failed for volume "%1" with error %2.  The volume might be configured with inadequate shadow copy storage area.  File Serve Deduplication service could not process this volume.%n%3\r\n
0xb0001021 | The file system on volume "%1" is potentially corrupted.  Please run the CHKDSK utility to verify and fix the file system.%n%2\r\n
0xb0001022 | Data Deduplication detected an insecure internal folder. To secure the folder, reinstall deduplication on the volume again.%n%1\r\n
0xb0001023 | Data Deduplication could not find a chunk store on the volume.%n%1\r\n
0xb0001024 | Data Deduplication detected multiple chunk store folders. To recover, reinstall deduplication on the volume.%n%1\r\n
0xb0001025 | Data Deduplication detected conflicting chunk store folders: "%1" and "%2".%n%3\r\n
0xb0001026 | The data is invalid.%n%1\r\n
0xb0001027 | Data Deduplication scheduler failed to initialize with error "%1".%n%2\r\n
0xb0001028 | Data Deduplication failed to validate job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb0001029 | Data Deduplication failed to start job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb000102c | Data Deduplication detected job type "%1" on volume "%2" uses too much memory. %3 MB is assigned. %4 MB is used.%n%5\r\n
0xb000102d | Data Deduplication detected job type "%1" on volume "%2" memory usage has dropped to desirable level.%n%3\r\n
0xb000102e | Data Deduplication cancelled job type "%1" on volume "%2". It uses too much memory than the amount assigned to it.%n%3\r\n
0xb000102f | Data Deduplication cancelled job type "%1" on volume "%2". Memory resource is running low on the machine or in the job.%n%3\r\n
0xb0001030 | Data Deduplication job type "%1" on volume "%2" failed to report completion to the service with error: %3.%n%4\r\n
0xb0001031 | Data Deduplication detected a container cannot be compacted or updated because it has reached the maximum generation.%n%1\r\n
0xb0001032 | Data Deduplication corruption log "%1" is corrupted.%n%2\r\n
0xb0001033 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". Please run scrubbing job to process corruption log. No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001034 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001035 | Data Deduplication scheduler failed to uninitialize with error "%1".%n%2\r\n
0xb0001036 | Data Deduplication detected a new container could not be created in a chunk store because it ran out of available container Id.%n%1\r\n
0xb0001037 | Data Deduplication full garbage collection phase 1 (cleaning file related metadata) on volume "%1" failed with error: %2.  The job will continue with phase 2 execution (data chunk cleanup).%n%3\r\n
0xb0001039 | Data Deduplication full garbage collection could not achieve maximum space reclamation because delete logs for data container %1 could not be cleaned up.%n%2\r\n
0xb000103a | Some files could not be deduplicated because of FSRM Quota violations on volume %1. Files skipped are likely compressed or sparse files in folders which are at quota or close to their quota limit. Please consider increasing the quota limit for folders that are at their quota limit or close to it.%n%2\r\n
0xb000103b | Data Deduplication failed to dedup file %1 "%2" due to fatal error %3%n%4\r\n
0xb000103c | Data Deduplication encountered corruption while accessing a file in chunk store.%n%1\r\n
0xb000103d | Data Deduplication encountered corruption while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103e | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103f | Data Deduplication is unable to access file %1 because the file is in use.%n%2\r\n
0xb0001040 | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store.%n%1\r\n
0xb0001041 | Data Deduplication cannot run the job on volume %1 because the dedup store version compatiblity check failed with error %2.%n%3\r\n
0xb0001042 | Data Deduplication has disabled the volume %1 because it has discovered too many corruptions. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001043 | Data Deduplication has detected a corrupt corruption metadata file on the store at %1. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001045 | Data Deduplication cannot be enabled on SIS volume "%1". Error: %2.%n%3\r\n
0xb0001046 | File-system is configured for case-sensitive file/folder names. Data Deduplication does not support case-sensitive file-system mode.%n%1\r\n
0xb0001049 | Data Deduplication changed scrubbing job to read-only due to insufficient disk space.%n%1\r\n
0xb000104b | Data Deduplication has disabled the volume %1 because there are missing or corrupt containers. Please run deep scrubbing on the volume.%n%2\r\n
0xb000104d | Data Deduplication encountered a disk-full error.%n%1\r\n
0xb000104e | Data Deduplication job cannot run on volume "%1" due to insufficient disk space.%n%2\r\n
0xb000104f | Data Deduplication job cannot run on offline volume "%1".%n%2\r\n
0xb0001050 | Data Deduplication recovered a corrupt or missing file.%n%1\r\n
0xb0001051 | Data Deduplication encountered a corrupted metadata file. To correct the problem, schedule or manually run a Garbage Collection job on the affected volume with the -Full option.%n%1\r\n
0xb0001052 | Data Deduplication encountered chunk %1 with corrupted header while updating container. The corrupted chunk is replicated to the new container %2.%n%3\r\n
0xb0001053 | Data Deduplication encountered chunk %1 with transient header corruption while updating container. The corrupted chunk is NOT replicated to the new container %2.%n%3\r\n
0xb0001054 | Data Deduplication failed to read chunk container redirection table from file %1 with error %2.%n%3\r\n
0xb0001055 | Data Deduplication failed to initialize reparse point index table for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001056 | Data Deduplication failed to deep scrub container file %1 on volume %2 with error %3.%n%4\r\n
0xb0001057 | Data Deduplication failed to load stream map log for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001058 | Data Deduplication found a duplicate local chunk id %1 in container file %2.%n%3\r\n
0xb0001059 | Data Deduplication job type "%1" on volume "%2" was cancelled manually.%n%3\r\n
0xb000105a | Scheduled data Deduplication job type "%1" on volume "%2" was cancelled.%n%3\r\n
0xb000105d | The Data Deduplication chunk store statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105e | The Data Deduplication volume statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105f | Data Deduplication failed to append to deep scrubbing log file %1 with error %2.%n%3\r\n
0xb0001060 | Data Deduplication encountered a failure during deep scrubbing on store %1 with error %2.%n%3\r\n
0xb0001800 | Data Deduplication service could not unoptimize file "%5%6%7". Error %8, "%9".\r\n
0xb0001801 | Data Deduplication service failed to unoptimize too many files %3. Some files are not reported.\r\n
0xb0001802 | Data Deduplication service has finished unoptimization on volume %3 with no errors.\r\n
0xb0001803 | Data Deduplication service has finished unoptimization on volume %3 with %4 errors.\r\n
0xb0001804 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6\r\n
0xb0001805 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6%nFull: %7\r\n
0xb0001806 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6%nFull: %7%nRead-only: %8\r\n
0xb0001809 | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate: %7%nSaved space: %8%nVolume used space: %9%nVolume free space: %10%nOptimized file count: %11%nIn-policy file count: %12%nJob processed space (bytes): %13%nJob elapsed time (seconds): %14%nJob throughput (MB/second): %15\r\n
0xb000180a | %1 job has completed.%n%nFull: %2%nVolume: %5 (%4)%nError code: %6%nError message: %7\r\n
0xb000180b | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6\r\n
0xb000180c | %1 job has completed.%n%nFull: %2%nRead-only: %3%nVolume: %6 (%5)%nError code: %7%nError message: %8\r\n
0xb000180e | %1 job has been queued.%n%nVolume: %4 (%3)%nSystem memory percent: %5 %nPriority: %6%nSchedule mode: %7\r\n
0xb000181c | Restore of deduplicated file "%1" failed with the following error: %2, "%3".\r\n
0xb0002000 | Data Deduplication detected job type "%1" on volume "%2" working set is low. Ratio to commit size is %3.%n%4\r\n
0xb0002001 | Data Deduplication detected job type "%1" on volume "%2" working set has recovered to desirable level.%n%3\r\n
0xb0002002 | Data Deduplication detected job type "%1" on volume "%2" page fault rate is high. The rate is %3 page faults per second.%n%4\r\n
0xb0002003 | Data Deduplication detected job type "%1" on volume "%2" page fault rate has lowered to desirable level. The rate is %3 page faults per second.%n%4\r\n
0xb0002004 | Data Deduplication failed to dedup file "%1" with file ID %2 due to non-fatal error %3%n%4.%n%nNote: You can retrieve the file name by running the command FSUTIL FILE QUERYFILENAMEBYID on the file in question.\r\n
0xb000200c | Data Deduplication has aborted a group commit session.%n%nFile count: %1%nError: %2%n%3\r\n
0xb000201c | Fail to open dedup setting registry key\r\n
0xb000201d | Data Deduplication failed to dedup file "%1" with file ID %2 due to oplock break%n%3\r\n
0xb000201e | Data Deduplication failed to load hotspot table from file %1 due to error %2.%n%3\r\n
0xb000201f | Data Deduplication failed to initialize oplock.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb0002020 | Data Deduplication while running job on volume %1 detected invalid physical sector size %2. Using default value %3.%n%4\r\n
0xb0002021 | Data Deduplication detected an unsupported chunk store container.%n%1\r\n
0xb0002022 | Data Deduplication could not create window to receive task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002023 | Data Deduplication could not create thread to poll for task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002024 | An attempt was made to perform an initialization operation when initialization has already been completed.%n%1\r\n
0xb0002028 | Data Deduplication created emergency file %1.%n%3\r\n
0xb0002029 | Data Deduplication failed to create emergency file %1 with error %2.%n%3\r\n
0xb000202a | Data Deduplication deleted emergency file %1.%n%3\r\n
0xb000202b | Data Deduplication failed to delete emergency file %1 with error %2.%n%3\r\n
0xb000202c | Data Deduplication detected a chunk store container with misaligned valid data length.%n%1\r\n
0xb000202d | Data Deduplication Garbage Collection encountered a delete log entry with an invalid stream map signature for stream map Id %1.%n%2\r\n
0xb000202e | Data Deduplication failed to initialize oplock as the file appears to be missing.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb000202f | Data Deduplication skipped too many file-level errors. We will not log more than %1 file-level errors per job.%n%2\r\n
0xb0002030 | Data Deduplication diagnostic warning.%n%n%1%n%2\r\n
0xb0002031 | Data Deduplication diagnostic information.%n%n%1%n%2\r\n
0xb0002032 | Data Deduplication found file %1 with a stream map id %2 in container file %3 marked for deletion.%n%4\r\n
0xb0002033 | Failed to enqueue job of type "%1" on volume "%2".%n%3\r\n
0xb0002034 | Error terminating job host process for job type "%1" on volume "%2" (process id: %3).%n%4\r\n
0xb0002035 | Data Deduplication encountered corrupted chunk %1 while updating container. Corrupted data that cannot be repaired will be copied as-is to the new container %2.%n%3\r\n
0xb0002036 | Data Deduplication job type "%1" on volume "%2" failed to exit gracefully.%n%3\r\n
0xb0002037 | Data Deduplication job host for job type "%1" on volume "%2" exited unexpectedly.%n%3\r\n
0xb0002038 | Data Deduplication has failed to load corruption metadata file on the store at %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb0002039 | Data Deduplication full garbage collection phase 1 on volume "%1" encountered an error %2 while processing file %3. Phase 1 will need to be aborted since garbage collection of file-related metadata is unsafe to continue on file errors.%n%4\r\n
0xb000203a | Data Deduplication has failed to process corruption metadata file %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb000203b | Data Deduplication has failed to load a corrupted metadata file %1 due to error %2. Deleting the file and continuing.%n%3\r\n
0xb000203c | Data Deduplication has failed to set NTFS allocation size for container file %1 due to error %2.%n%3\r\n
0xb000203d | Data Deduplication configured to use BCrypt provider '%1' for hash algorithm %2.%n%3\r\n
0xb000203e | Data Deduplication could not use BCrypt provider '%1' for hash algorithm %2 due to an error in operation %3. Reverting to the Microsoft primitive CNG provider.%n%4\r\n
0xb000203f | Data Deduplication failed to include file "%1" in file metadata analysis calculations.%n%2\r\n
0xb0002040 | Data Deduplication failed to include stream map %1 in file metadata analysis calculations.%n%2\r\n
0xb0002041 | Data Deduplication encountered an error for file "%1" while scanning files and folders.%n%2\r\n
0xb0002042 | Data Deduplication encountered an error while attempting to resume processing. Please consult the event log parameters for more details about the current file being processed.%n%1\r\n
0xb0002800 | %1 job memory requirements.%n%nVolume: %4 (%3)%nMinimum memory: %5 MB%nMaximum memory: %6 MB%nMinimum disk: %7 MB\r\n
0xb0002801 | %1 reconciliation has started.%n%nVolume: %4 (%3)\r\n
0xb0002802 | %1 reconciliation has completed.%n%nVolume: %4 (%3)%nReconciled containers: %5%nUnreconciled containers: %6%nMerged containers: %7%nTotal reconciled references: %8%nError code: %9%nError message: %10\r\n
0xb0002803 | %1 job on volume %4 (%3) was configured with insufficient memory.%n%nSystem memory percentage: %5%nAvailable memory: %8 MB%nMinimum required memory: %6 MB\r\n
0xb0003200 | Data Deduplication service detected corruption in "%5%6%7". The corruption cannot be repaired.\r\n
0xb0003201 | Data Deduplication service detected corruption (%7) in "%6". See the event details for more information.\r\n
0xb0003202 | Data Deduplication service detected a corrupted item (%11 - %13, %8, %9, %10, %12) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003203 | Data Deduplication service has finished scrubbing on volume %3. It did not find any corruption since the last scrubbing.\r\n
0xb0003204 | Data Deduplication service found %4 corruption(s) on volume %3. All corruptions are fixed.\r\n
0xb0003205 | Data Deduplication service found %4 corruption(s) on volume %3. %5 corruption(s) are fixed. %6 user file(s) are corrupted. %7 user file(s) are fixed. For the corrupted file list, see the Microsoft/Windows/Deduplication/Scrubbing events.\r\n
0xb0003206 | Data Deduplication service found too many corruptions on volume %3. Some corruptions are not reported.\r\n
0xb0003211 | Data Deduplication service has finished scrubbing on volume %3. See the event details for more information.\r\n
0xb0003212 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003213 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003214 | Data Deduplication service encountered error while detecting corruptions in chunk store on volume %3. The error was %4. The job is aborted.\r\n
0xb0003216 | Data Deduplication service encountered error while loading corruption logs on volume %3. The error was %4. The job continues. Some corruptions may not be detected.\r\n
0xb0003217 | Data Deduplication service encountered error while cleaning up corruption logs on volume %3. The error was %4. Some corruptions may be reported again next time.\r\n
0xb0003218 | Data Deduplication service encountered error while loading hotspots mapping from chunk store on volume %3. The error was %4. Some corruptions may not be repaired.\r\n
0xb0003219 | Data Deduplication service encountered error while determining corrupted user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb000321a | Data Deduplication service found %4 corruption(s) on volume %3. %6 user file(s) are corrupted. %7 user file(s) are fixable. Please run scrubbing job in read-write mode to attempt fixing reported corruptions.\r\n
0xb000321b | Data Deduplication service fixed corruption in "%5%6%7".\r\n
0xb000321c | Data Deduplication service detected fixable corruption in "%5%6%7". Please run scrubbing job in read-write mode to fix this corruption.\r\n
0xb000321e | Data Deduplication service encountered error while repairing corruptions on volume %3. The error was %4. The repair is unsuccessful.\r\n
0xb000321f | Data Deduplication service detected a corrupted item (%6, %7, %8, %9) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003220 | Container (%8,%9) with user data is missing from the chunk store. Missing container may result from incomplete restore, incomplete migration or file-system corruption. Volume is disabled from further optimization. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0003221 | Data Deduplication service encountered error while scaning dedup user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb0003222 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003223 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003224 | Data Deduplication service detected potential data loss (%9) in "%6" due to sharing reparse data with file "%8". See the event details for more information.\r\n
0xb0003225 | Container (%8,%9) with user data is corrupt in the chunk store. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0005000 | Open stream store stream (StartingChunkId %1, FileId %2)\r\n
0xb0005001 | Open stream store stream completed %1\r\n
0xb0005002 | Prepare for paging IO (Stream %1, FileId %2)\r\n
0xb0005003 | Prepare for paging IO completed %1\r\n
0xb0005005 | Read stream map completed %1\r\n
0xb0005006 | Read chunks (Stream %1, FileId %2, IoType %3, FirstRequestChunkId %4, NextRequest %5)\r\n
0xb0005007 | Read chunks completed %1\r\n
0xb0005008 | Compute checksum (ItemType %1, DataSize %2)\r\n
0xb0005009 | Compute checksum completed %1\r\n
0xb000500a | Get container entry (ContainerId %1, Generation %2)\r\n
0xb000500b | Get container entry completed %1\r\n
0xb000500c | Get maximum generation for container (ContainerId %1, Generation %2)\r\n
0xb000500d | Get maximum generation for container completed %1\r\n
0xb000500e | Open chunk container (ContainerId %1, Generation %2, RootPath %4)\r\n
0xb000500f | Open chunk container completed %1\r\n
0xb0005010 | Initialize chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005011 | Initialize chunk container redirection table completed %1\r\n
0xb0005012 | Validate chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005013 | Validate chunk container redirection table completed %1\r\n
0xb0005014 | Get chunk container valid data length (ContainerId %1, Generation %2)\r\n
0xb0005015 | Get chunk container valid data length completed %1\r\n
0xb0005016 | Get offset from chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005017 | Get offset from chunk container redirection table completed %1\r\n
0xb0005018 | Read chunk container block (ContainerId %1, Generation %2, Buffer %3, Offset %4, Length %5, IoType %6, Synchronous %7)\r\n
0xb0005019 | Read chunk container block completed %1\r\n
0xb000501a | Clear chunk container block (Buffer %1, Size %2, BufferType %3)\r\n
0xb000501b | Clear chunk container block completed %1\r\n
0xb000501c | Copy chunk (Buffer %1, Size %2, BufferType %3, BufferOffset %4, OutputCapacity %5)\r\n
0xb000501d | Copy chunk completed %1\r\n
0xb000501e | Initialize file cache (UnderlyingFileObject %1, CacheFileSize %2)\r\n
0xb000501f | Initialize file cache completed %1\r\n
0xb0005020 | Map file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005021 | Map file cache data completed %1\r\n
0xb0005022 | Unpin file cache data(Bcb %1)\r\n
0xb0005023 | Unpin file cache data completed %1\r\n
0xb0005024 | Copy file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005025 | Copy file cache data completed %1\r\n
0xb0005026 | Read underlying file cache data (CacheFileObject %1, UnderlyingFileObject %2, Offset %3, Length %4)\r\n
0xb0005027 | Read underlying file cache data completed %1\r\n
0xb0005028 | Get chunk container file size (ContainerId %1, Generation %2)\r\n
0xb0005029 | Get chunk container file size completed %1\r\n
0xb000502a | Pin stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb000502b | Pin stream map completed %1\r\n
0xb000502c | Pin chunk container (ContainerId %1, Generation %2)\r\n
0xb000502d | Pin chunk container completed %1\r\n
0xb000502e | Pin chunk (ContainerId %1, Generation %2)\r\n
0xb000502f | Pin chunk completed %1\r\n
0xb0005030 | Allocate pool buffer (ReadLength %1, PagingIo %2)\r\n
0xb0005031 | Allocate pool buffer completed %1\r\n
0xb0005032 | Unpin chunk container (ContainerId %1, Generation %2)\r\n
0xb0005033 | Unpin chunk container completed %1\r\n
0xb0005034 | Unpin chunk (ContainerId %1, Generation %2)\r\n
0xb0005035 | Unpin chunk completed %1\r\n
0xb0006028 | Dedup read processing (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006029 | Dedup read processing completed %1\r\n
0xb000602a | Get first stream map entry (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602b | Get first stream map entry completed %1\r\n
0xb000602c | Read chunk metadata (Stream %1, CurrentOffset %2, AdjustedFinalOffset %3, FirstChunkByteOffset %4, ChunkRequestsEndOffset %5, TlCache %6)\r\n
0xb000602d | Read chunk metadata completed %1\r\n
0xb000602e | Read chunk data (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602f | Read chunk data completed %1\r\n
0xb0006030 | Reference TlCache data (TlCache %1, Stream %2)\r\n
0xb0006031 | Reference TlCache data completed %1\r\n
0xb0006032 | Read chunk data from stream store (Stream %1)\r\n
0xb0006033 | Read chunk data from stream store completed %1\r\n
0xb0006034 | Assemble chunk data\r\n
0xb0006035 | Assemble chunk data completed %1\r\n
0xb0006036 | Decompress chunk data\r\n
0xb0006037 | Decompress chunk data completed %1\r\n
0xb0006038 | Copy chunk data in to user buffer (BytesCopied %1)\r\n
0xb0006039 | Copy chunk data in to user buffer completed %1\r\n
0xb000603a | Insert chunk data in to tlcache\r\n
0xb000603b | Insert chunk data in to tlcache completed %1\r\n
0xb000603c | Read data from dedup reparse point file (FileObject %1, Offset %2, Length %3)\r\n
0xb000603d | Read underlying file cache data completed %1\r\n
0xb000603e | Prepare stream map (StreamContext %1)\r\n
0xb000603f | Prepare stream map completed %1\r\n
0xb0006040 | Patch clean ranges (FileObject %1, Offset %2, Length %3)\r\n
0xb0006041 | Patch clean ranges completed %1\r\n
0xb0006042 | Writing data to dedup file (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006043 | Writing data to dedup file completed %1\r\n
0xb0006044 | Queue write request on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006045 | Queue write request on dedup file completed %1\r\n
0xb0006046 | Do copy on write work on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006047 | Do copy on write work on dedup file completed %1\r\n
0xb0006048 | Do full recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006049 | Do full recall on dedup file completed %1\r\n
0xb000604a | Do partial recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604b | Do partial recall on dedup file completed %1\r\n
0xb000604c | Do dummy paging read on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604d | Do dummy paging read on dedup file completed %1\r\n
0xb000604e | Read clean data for recalling file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604f | Read clean data for recalling file completed %1\r\n
0xb0006050 | Write clean data to dedup file normally (FileObject %1, Offset %2, Length %3)\r\n
0xb0006051 | Write clean data to dedup file completed %1\r\n
0xb0006052 | Write clean data to dedup file paged (FileObject %1, Offset %2, Length %3)\r\n
0xb0006053 | Write clean data to dedup file paged completed %1\r\n
0xb0006054 | Recall dedup file using paging Io (FileObject %1, Offset %2, Length %3)\r\n
0xb0006055 | Recall dedup file using paging Io completed %1\r\n
0xb0006056 | Flush dedup file after recall (FileObject %1)\r\n
0xb0006057 | Flush dedup file after recall completed %1\r\n
0xb0006058 | Update bitmap after recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006059 | Update bitmap after recall on dedup file completed %1\r\n
0xb000605a | Delete dedup reparse point (FileObject %1)\r\n
0xb000605b | Delete dedup reparse point completed %1\r\n
0xb000605c | Open dedup file (FilePath %1)\r\n
0xb000605d | Open dedup file completed %1\r\n
0xb000605e | Locking user buffer for read\r\n
0xb000605f | Locking user buffer for read completed %1\r\n
0xb0006060 | Get system address for MDL\r\n
0xb0006061 | Get system address for MDL completed %1\r\n
0xb0006062 | Read clean dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006063 | Read clean dedup file completed %1\r\n
0xb0006064 | Get range state (Offset %1, Length %2)\r\n
0xb0006065 | Get range state completed %1\r\n
0xb0006066 | Get chunk body\r\n
0xb0006067 | Get chunk body completed %1\r\n
0xb0006068 | Release chunk\r\n
0xb0006069 | Release chunk completed %1\r\n
0xb000606a | Release decompress chunk context (BufferSize %1)\r\n
0xb000606b | Release decompress chunk context completed %1\r\n
0xb000606c | Prepare decompress chunk context (BufferSize %1)\r\n
0xb000606d | Prepare decompress chunk context completed %1\r\n
0xb000606e | Copy data to compressed buffer (BufferSize %1)\r\n
0xb000606f | Copy data to compressed buffer completed %1\r\n
0xb0006070 | Release data from TL Cache\r\n
0xb0006071 | Release data from TL Cache completed %1\r\n
0xb0006072 | Queue async read request (FileObject %1, Offset %2, Length %3)\r\n
0xb0006073 | Queue async read request complete %1\r\n
0xb0015004 | Read stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb1004000 | Create chunk container (%1 - %2.%3.ccc)\r\n
0xb1004001 | Create chunk container completed %1\r\n
0xb1004002 | Copy chunk container (%1 - %2.%3.ccc)\r\n
0xb1004003 | Copy chunk container completed %1\r\n
0xb1004004 | Delete chunk container (%1 - %2.%3.ccc)\r\n
0xb1004005 | Delete chunk container completed %1\r\n
0xb1004006 | Rename chunk container (%1 - %2.%3.ccc%4)\r\n
0xb1004007 | Rename chunk container completed %1\r\n
0xb1004008 | Flush chunk container (%1 - %2.%3.ccc)\r\n
0xb1004009 | Flush chunk container completed %1\r\n
0xb100400a | Rollback chunk container (%1 - %2.%3.ccc)\r\n
0xb100400b | Rollback chunk container completed %1\r\n
0xb100400c | Mark chunk container (%1 - %2.%3.ccc) read-only\r\n
0xb100400d | Mark chunk container read-only completed %1\r\n
0xb100400e | Write chunk container (%1 - %2.%3.ccc) redirection table at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb100400f | Write chunk container redirection table completed %1\r\n
0xb1004011 | Write chunk container header completed %1\r\n
0xb1004013 | Insert data chunk header completed %1\r\n
0xb1004015 | Insert data chunk body completed %1 with ChunkId %2\r\n
0xb1004019 | Write delete log header completed %1\r\n
0xb100401b | Append delete log entries completed %1\r\n
0xb100401d | Delete delete log completed %1\r\n
0xb100401f | Rename delete log completed %1\r\n
0xb1004021 | Write chunk container bitmap completed %1\r\n
0xb1004023 | Delete chunk container bitmap completed %1\r\n
0xb1004024 | Write merge log (%5 - %6.%7.merge.log) header\r\n
0xb1004025 | Write merge log header completed %1\r\n
0xb1004027 | Insert hotspot chunk header completed %1\r\n
0xb1004029 | Insert hotspot chunk body completed %1 with ChunkId %2\r\n
0xb100402b | Insert stream map chunk header completed %1\r\n
0xb100402d | Insert stream map chunk body completed %1 with ChunkId %2\r\n
0xb100402f | Append merge log entries completed %1\r\n
0xb1004030 | Delete merge log (%1 - %2.%3.merge.log)\r\n
0xb1004031 | Delete merge log completed %1\r\n
0xb1004032 | Flush merge log (%1 - %2.%3.merge.log)\r\n
0xb1004033 | Flush merge log completed %1\r\n
0xb1004034 | Update file list entries (Remove: %1, Add: %2)\r\n
0xb1004035 | Update file list entries completed %1\r\n
0xb1004036 | Set dedup reparse point on %2 (FileId %1) (ReparsePoint: SizeBackedByChunkStore %3, StreamMapInfoSize %4, StreamMapInfo %5)\r\n
0xb1004037 | Set dedup reparse point completed %1 (%2)\r\n
0xb1004038 | Set dedup zero data on %2 (FileId %1)\r\n
0xb1004039 | Set dedup zero data completed %1\r\n
0xb100403a | Flush reparse point files\r\n
0xb100403b | Flush reparse point files completed %1\r\n
0xb100403c | Set sparse on file id %1\r\n
0xb100403d | Set sparse completed %1\r\n
0xb100403e | FSCTL_SET_ZERO_DATA on file id %1 at offset %2 and BeyondFinalZero %3\r\n
0xb100403f | FSCTL_SET_ZERO_DATA completed %1\r\n
0xb1004040 | Rename chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1004041 | Rename chunk container bitmap completed %1\r\n
0xb1004042 | Insert padding chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1004043 | Insert padding chunk header completed %1\r\n
0xb1004044 | Insert padding chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1004045 | Insert padding chunk body completed %1 with ChunkId %2\r\n
0xb1004046 | Insert batch of chunks to chunk container (%1 - %2.%3.ccc) at offset %4 (BatchChunkCount %5, BatchDataSize %6)\r\n
0xb1004047 | Insert batch of chunks completed %1\r\n
0xb1004049 | Write chunk container directory completed %1\r\n
0xb100404b | Delete chunk container directory completed %1\r\n
0xb100404c | Rename chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb100404d | Rename chunk container directory completed %1\r\n
0xb1014010 | Write chunk container (%5 - %6.%7.ccc) header at offset %8 (Header: USN %9, VDL %10, #Chunk %11, NextLocalId %12, Flags %13, LastAppendTime %14, BackupRedirectionTableOfset %15, LastReconciliationLocalId %16)\r\n
0xb1014012 | Insert data chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1014014 | Insert data chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014018 | Write delete log (%5 - %6.%7.delete.log) header\r\n
0xb101401a | Append delete log (%1 - %2.%3.delete.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb101401c | Delete delete log (%1 - %2.%3.delete.log)\r\n
0xb101401e | Rename delete log (%1 - %2.%3.delete.log)\r\n
0xb1014020 | Write chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4) (Bitmap: BitLength %5, StartIndex %6, Count %7)\r\n
0xb1014022 | Delete chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1014026 | Insert hotspot chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014028 | Insert hotspot chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb101402a | Insert stream map chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014048 | Write chunk container directory (%1 - %2) for chunk container (%1 - %3.%4) (Directory: EntryCount %5)\r\n
0xb101404a | Delete chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb102402e | Append merge log (%1 - %2.%3.merge.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb103402c | Insert stream map chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7) (Entries: StartIndex %8, Count %9)\r\n
0xd0000001 | Chunk header\r\n
0xd0000002 | Chunk body\r\n
0xd0000003 | Container header\r\n
0xd0000004 | Container redirection table\r\n
0xd0000005 | Hotspot table\r\n
0xd0000006 | Delete log header\r\n
0xd0000007 | Delete log entry\r\n
0xd0000008 | GC bitmap header\r\n
0xd0000009 | GC bitmap entry\r\n
0xd000000a | Merge log header\r\n
0xd000000b | Merge log entry\r\n
0xd000000c | Data\r\n
0xd000000d | Stream map\r\n
0xd000000e | Hotspot\r\n
0xd000000f | Optimization\r\n
0xd0000010 | Garbage Collection\r\n
0xd0000011 | Scrubbing\r\n
0xd0000012 | Unoptimization\r\n
0xd0000013 | Analysis\r\n
0xd0000014 | Low\r\n
0xd0000015 | Normal\r\n
0xd0000016 | High\r\n
0xd0000017 | Cache\r\n
0xd0000018 | Non-cache\r\n
0xd0000019 | Paging\r\n
0xd000001a | Memory map\r\n
0xd000001b | Paging memory map\r\n
0xd000001c | None\r\n
0xd000001d | Pool\r\n
0xd000001e | PoolAligned\r\n
0xd000001f | MDL\r\n
0xd0000020 | Map\r\n
0xd0000021 | Cached\r\n
0xd0000022 | NonCached\r\n
0xd0000023 | Paged\r\n
0xd0000024 | container file\r\n
0xd0000025 | file list file\r\n
0xd0000026 | file list header\r\n
0xd0000027 | file list entry\r\n
0xd0000028 | primary file list file\r\n
0xd0000029 | backup file list file\r\n
0xd000002a | Scheduled\r\n
0xd000002b | Manual\r\n
0xd1000001 | None\r\n
0xd1000002 | LZNT1\r\n
0xd1000003 | Xpress\r\n
0xd1000004 | Xpreff Huff\r\n
0xd1000005 | None\r\n
0xd1000006 | Standard\r\n
0xd1000007 | Max\r\n
0xd1000008 | Hybrid\r\n
0xf0000001 | None\r\n
0xf0000002 | Bad checksum\r\n
0xf0000003 | Inconsistent metadata\r\n
0xf0000004 | Invalid header metadata\r\n
0xf0000005 | Missing file\r\n
0xf0000006 | Bad checksum (storage subsystem)\r\n
0xf0000007 | Corruption (storage subsystem)\r\n
0xf0000008 | Corruption (missing metadata)\r\n
0xf0000009 | Possible data loss (duplicate reparse data)\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00565301 | Reconciliation of chunk store is due.\r\n
0x00565302 | There are no actions associated with this job.\r\n
0x00565303 | Data deduplication cannot runing this job on this Csv volume on this node.\r\n
0x10000001 | Reporting\r\n
0x10000002 | Filter\r\n
0x10000003 | Kernel mode stream store\r\n
0x10000004 | Kernel mode chunk store\r\n
0x10000005 | Kernel mode chunk container\r\n
0x10000006 | Kernel mode file cache\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Data Deduplication Optimization Task\r\n
0x70000002 | Data Deduplication Garbage Collection Task\r\n
0x70000003 | Data Deduplication Scrubbing Task\r\n
0x70000004 | Data Deduplication Unoptimization Task\r\n
0x70000005 | Open stream store stream\r\n
0x70000006 | Prepare for paging IO\r\n
0x70000007 | Read stream map\r\n
0x70000008 | Read chunks\r\n
0x70000009 | Compute checksum\r\n
0x7000000a | Get container entry\r\n
0x7000000b | Get maximum generation for container\r\n
0x7000000c | Open chunk container\r\n
0x7000000d | Initialize chunk container redirection table\r\n
0x7000000e | Validate chunk container redirection table\r\n
0x7000000f | Get chunk container valid data length\r\n
0x70000010 | Get offset from chunk container redirection table\r\n
0x70000011 | Read chunk container block\r\n
0x70000012 | Clear chunk container block\r\n
0x70000013 | Copy chunk\r\n
0x70000014 | Initialize file cache\r\n
0x70000015 | Map file cache data\r\n
0x70000016 | Unpin file cache data\r\n
0x70000017 | Copy file cache data\r\n
0x70000018 | Read underlying file cache data\r\n
0x70000019 | Get chunk container file size\r\n
0x7000001a | Pin stream map\r\n
0x7000001b | Pin chunk container\r\n
0x7000001c | Pin chunk\r\n
0x7000001d | Allocate pool buffer\r\n
0x7000001e | Unpin chunk container\r\n
0x7000001f | Unpin chunk\r\n
0x70000020 | Dedup read processing\r\n
0x70000021 | Get first stream map entry\r\n
0x70000022 | Read chunk metadata\r\n
0x70000023 | Read chunk data\r\n
0x70000024 | Reference TlCache data\r\n
0x70000025 | Read chunk data from stream store\r\n
0x70000026 | Assemble chunk data\r\n
0x70000027 | Decompress chunk data\r\n
0x70000028 | Copy chunk data in to user buffer\r\n
0x70000029 | Insert chunk data in to tlcache\r\n
0x7000002a | Read data from dedup reparse point file\r\n
0x7000002b | Prepare stream map\r\n
0x7000002c | Patch clean ranges\r\n
0x7000002d | Writing data to dedup file\r\n
0x7000002e | Queue write request on dedup file\r\n
0x7000002f | Do copy on write work on dedup file\r\n
0x70000030 | Do full recall on dedup file\r\n
0x70000031 | Do partial recall on dedup file\r\n
0x70000032 | Do dummy paging read on dedup file\r\n
0x70000033 | Read clean data for recalling file\r\n
0x70000034 | Write clean data to dedup file normally\r\n
0x70000035 | Write clean data to dedup file paged\r\n
0x70000036 | Recall dedup file using paging Io\r\n
0x70000037 | Flush dedup file after recall\r\n
0x70000038 | Update bitmap after recall on dedup file\r\n
0x70000039 | Delete dedup reparse point\r\n
0x7000003a | Open dedup file\r\n
0x7000003b | Locking user buffer for read\r\n
0x7000003c | Get system address for MDL\r\n
0x7000003d | Read clean dedup file\r\n
0x7000003e | Get range state\r\n
0x7000003f | Get chunk body\r\n
0x70000040 | Release chunk\r\n
0x70000041 | Release decompress chunk context\r\n
0x70000042 | Prepare decompress chunk context\r\n
0x70000043 | Copy data to compressed buffer\r\n
0x70000044 | Release data from TL Cache\r\n
0x70000045 | Queue async read request\r\n
0x80565301 | The requested object was not found.\r\n
0x80565302 | One (or more) of the arguments given to the task scheduler is not valid.\r\n
0x80565303 | The specified object already exists.\r\n
0x80565304 | The specified path was not found.\r\n
0x80565305 | The specified user is invalid.\r\n
0x80565306 | The specified path is invalid.\r\n
0x80565307 | The specified name is invalid.\r\n
0x80565308 | The specified property is out of range.\r\n
0x80565309 | A required filter driver is either not installed, not loaded, or not ready for service.\r\n
0x8056530a | There is insufficient disk space to perform the requested operation.\r\n
0x8056530b | The specified volume type is not supported. Deduplication is supported on fixed, write-enabled NTFS data volumes and CSV backed by NTFS data volumes.\r\n
0x8056530c | Data deduplication encountered an unexpected error. Check the Data Deduplication Operational event log for more information.\r\n
0x8056530d | The specified scan log cursor has expired.\r\n
0x8056530e | The file system might be corrupted.  Please run the CHKDSK utility.\r\n
0x8056530f | A volume shadow copy could not be created or was unexpectedly deleted.\r\n
0x80565310 | Data deduplication encountered a corrupted XML configuration file.\r\n
0x80565311 | The Data Deduplication service could not access the global configuration because the Cluster service is not running.\r\n
0x80565312 | The Data Deduplication service could not access the global configuration because it has not been installed yet.\r\n
0x80565313 | Data deduplication failed to access the volume. It may be offline.\r\n
0x80565314 | The module encountered an invalid parameter or a valid parameter with an invalid value, or an expected module parameter was not found. Check the operational event log for more information.\r\n
0x80565315 | An attempt was made to perform an initialization operation when initialization has already been completed.\r\n
0x80565316 | An attempt was made to perform an uninitialization operation when that operation has already been completed.\r\n
0x80565317 | The Data Deduplication service detected an internal folder that is not secure. To secure the folder, reinstall deduplication on the volume.\r\n
0x80565318 | Data chunking has already been initiated.\r\n
0x80565319 | An attempt was made to perform an operation from an invalid state.\r\n
0x8056531a | An attempt was made to perform an operation before initialization.\r\n
0x8056531b | Call ::PushBuffer to continue chunking or ::Drain to enumerate any partial chunks.\r\n
0x8056531c | The Data Deduplication service detected multiple chunk store folders; however, only one chunk store folder is permitted. To fix this issue, reinstall deduplication on the volume.\r\n
0x8056531d | The data is invalid.\r\n
0x8056531e | The process is in an unknown state.\r\n
0x8056531f | The process is not running.\r\n
0x80565320 | There was an error while opening the file.\r\n
0x80565321 | The job process could not start because the job was not found.\r\n
0x80565322 | The client process ID does not match the ID of the host process that was started.\r\n
0x80565323 | The specified volume is not enabled for deduplication.\r\n
0x80565324 | A zero-character chunk ID is not valid.\r\n
0x80565325 | The index is filled to capacity.\r\n
0x80565327 | Session already exists.\r\n
0x80565328 | The compression format selected is not supported.\r\n
0x80565329 | The compressed buffer is larger than the uncompressed buffer.\r\n
0x80565330 | The buffer is not large enough.\r\n
0x8056533a | Index Scratch Log Error in: Seek, Read, Write, or Create\r\n
0x8056533b | The job type is invalid.\r\n
0x8056533c | Persistence layer enumeration error.\r\n
0x8056533d | The operation was cancelled.\r\n
0x8056533e | This job will not run at the scheduled time because it requires more memory than is currently available.\r\n
0x80565341 | The job was terminated while in a cancel or pending state.\r\n
0x80565342 | The job was terminated while in a handshake pending state.\r\n
0x80565343 | The job was terminated due to a service shutdown.\r\n
0x80565344 | The job was abandoned before starting.\r\n
0x80565345 | The job process exited unexpectedly.\r\n
0x80565346 | The Data Deduplication service detected that the container cannot be compacted or updated because it has reached the maximum generation version. \r\n
0x80565347 | The corruption log has reached its maximum size.\r\n
0x80565348 | The data deduplication scrubbing job failed to process the corruption logs.\r\n
0x80565349 | Data deduplication failed to create new chunk store container files. Allocate more space to the volume.\r\n
0x80565350 | An error occurred while opening the file because the file was in use. \r\n
0x80565351 | An error was discovered while deduplicating the file. The file is now skipped.\r\n
0x80565352 | File Server Deduplication encountered corruption while enumerating chunks in a chunk store.\r\n
0x80565353 | The scan log is not valid.\r\n
0x80565354 | The data is invalid due to checksum (CRC) mismatch error.\r\n
0x80565355 | Data deduplication encountered file corruption error.\r\n
0x80565356 | Job completed with some errors. Check event logs for more details.\r\n
0x80565357 | Data deduplication is not supported on the version of the chunk store found on this volume.\r\n
0x80565358 | Data deduplication encountered an unknown version of chunk store on this volume.\r\n
0x80565359 | The job was assigned less memory than the minimum it needs to run.\r\n
0x8056535a | The data deduplication job schedule cannot be modified.\r\n
0x8056535b | The valid data length of chunk store container is misaligned.\r\n
0x8056535c | File access is denied.\r\n
0x8056535d | Data deduplication job stopped due to too many corrupted files.\r\n
0x8056535e | Data deduplication job stopped due to an internal error in the BCrypt SHA-512 provider.\r\n
0x8056535f | Data deduplication job stopped for store reconciliation.\r\n
0x80565360 | File skipped for deduplication due to its size.\r\n
0x80565361 | File skipped due to deduplication retry limit.\r\n
0x80565362 | The pipeline buffer cache is full.\r\n
0x80565363 | Another Data deduplication job already running on this volume.\r\n
0x80565364 | Data deduplication cannot run this job on this Csv volume on this node. Try running the job on the Csv volume resource owner node.\r\n
0x80565365 | Data deduplication failed to initialize cluster state on this node.\r\n
0x80565366 | Optimization of the file was aborted by the dedup filter driver.\r\n
0x80565367 | The operation could not be performed because of a concurrent IO operation.\r\n
0x80565368 | Data deduplication encountered an unexpected error. Verify deduplication is enabled on all nodes if in a cluster configuration. Check the Data Deduplication Operational event log for more information.\r\n
0x80565369 | Data access for data deduplicated CSV volumes can only be disabled when in maintenance mode. Check the Data Deduplication Operational event log for more information.\r\n
0x8056536a | Data Deduplication encountered an IO device error that may indicate a hardware fault in the storage subsystem.\r\n
0x90000001 | Data Deduplication\r\n
0x90000002 | Application\r\n
0x91000001 | Data Deduplication Change Events\r\n
0xb0001000 | Volume "%1" appears as disconnected and it is ignored by the service.  You may want to rescan disks.   Error: %2.%n%3\r\n
0xb0001001 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3". Most likely the CPU is under heavy load.  Error: %4.%n%5\r\n
0xb0001002 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3".  Error: %4.%n%5\r\n
0xb0001003 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3" during Safe Mode. The Data Deduplication service cannot start while in safe mode.  Error: %4.%n%5\r\n
0xb0001004 | A critical component required by Data Deduplication is not registered. This might happen if an error occurred during Windows setup, or if the computer does not have the Windows Server 2012 or later version of Deduplication service installed. The error returned from CoCreateInstance on class with CLSID %1 and Name "%2" on machine "%3" is %4.%n%5\r\n
0xb0001005 | Data Deduplication service is shutting down due to idle timeout.%n%1\r\n
0xb0001006 | Data Deduplication service is shutting down due to shutdown event from the Service Control Manager.%n%1\r\n
0xb0001007 | Data Deduplication job of type "%1" on volume "%2" has completed with return code: %3%n%4\r\n
0xb0001008 | Data Deduplication error: Unexpected error calling routine %1.  hr = %2.%n%3\r\n
0xb0001009 | Data Deduplication error: Unexpected error.%n%1\r\n
0xb000100a | Data Deduplication warning: %1%nError: %2.%n%3\r\n
0xb000100b | Data Deduplication error: Unexpected COM error %1: %2.  Error code: %3.%n%4\r\n
0xb000100c | Data Deduplication was unable to access the following file or volume: "%1".  This file or volume might be locked by another application right now, or you might need to give Local System access to it.%n%2\r\n
0xb000100d | Data Deduplication encountered an unexpected error during volume scan of volumes mounted at "%1" ("%2"). To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100e | Data Deduplication was unable to create or access the shadow copy for volumes mounted at "%1" ("%2"). Possible causes include an improper Shadow Copy configuration, insufficient disk space, or extreme memory, I/O or CPU load of the system. To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100f | Data Deduplication was unable to access volumes mounted at "%1" ("%2"). Make sure that dismount or format operations do not happen while running deduplication.%n%3\r\n
0xb0001010 | Data Deduplication was unable to access a file or volume. Details:%n%n%1%n The volume may be inaccessible for I/O operations or marked read-only. In case of a cluster volume, this may be a transient failure during failover.%n%2\r\n
0xb0001011 | Data Deduplication was unable to scan volume "%1" ("%2").%n%3\r\n
0xb0001012 | Data Deduplication detected a corruption on file "%1" at offset ("%2").  If this condition persists then please restore the data from a previous backup.  Corruption details: Structure=%3, Corruption type = %4, Additional data = %5%n%6\r\n
0xb0001013 | Data Deduplication encountered failure while reconciling chunk store on volume "%1". The error code was %2. Reconciliation is disabled for the current optimization job.%n%3\r\n
0xb0001016 | Data Deduplication encountered corrupted chunk container %1 while performing full garbage collection. The corrupted chunk container is skipped.%n%2\r\n
0xb0001017 | Data Deduplication could not initialize change log under %1. The error code was %2.%n%3\r\n
0xb0001018 | Data Deduplication service could not mark chunk container %1 as reconciled. The error code was %2.%n%3\r\n
0xb0001019 | A Data Deduplication configuration file is corrupted. The system or volume may need to be restored from backup.%n%1\r\n
0xb000101a | Data Deduplication was unable to save one of the configuration stores on volume "%1" due to a disk-full error: If the disk is full, please clean it up (extend the volume or delete some files). If the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.%n%2\r\n
0xb000101b | Data Deduplication could not access global configuration since the cluster service is not running. Please start the cluster service and retry the operation.%n%1\r\n
0xb000101c | Shadow copy "%1" was deleted during storage report generation.  Volume "%2" might be configured with inadequate shadow copy storage area. Data Deduplication could not process this volume.%n%3\r\n
0xb000101d | Shadow copy creation failed for volume "%1" after retrying for %2 minutes because other shadow copies were being created.  Reschedule the Data Deduplication for a less busy time.%n%3\r\n
0xb000101e | Volume "%1" is not supported for shadow copy.  It is possible that the volume was removed from the system.  Data Deduplication service could not process this volume.%n%2\r\n
0xb000101f | The volume "%1" has been deleted or removed from the system.%n%2\r\n
0xb0001020 | Shadow copy creation failed for volume "%1" with error %2.  The volume might be configured with inadequate shadow copy storage area.  File Serve Deduplication service could not process this volume.%n%3\r\n
0xb0001021 | The file system on volume "%1" is potentially corrupted.  Please run the CHKDSK utility to verify and fix the file system.%n%2\r\n
0xb0001022 | Data Deduplication detected an insecure internal folder. To secure the folder, reinstall deduplication on the volume again.%n%1\r\n
0xb0001023 | Data Deduplication could not find a chunk store on the volume.%n%1\r\n
0xb0001024 | Data Deduplication detected multiple chunk store folders. To recover, reinstall deduplication on the volume.%n%1\r\n
0xb0001025 | Data Deduplication detected conflicting chunk store folders: "%1" and "%2".%n%3\r\n
0xb0001026 | The data is invalid.%n%1\r\n
0xb0001027 | Data Deduplication scheduler failed to initialize with error "%1".%n%2\r\n
0xb0001028 | Data Deduplication failed to validate job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb0001029 | Data Deduplication failed to start job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb000102c | Data Deduplication detected job type "%1" on volume "%2" uses too much memory. %3 MB is assigned. %4 MB is used.%n%5\r\n
0xb000102d | Data Deduplication detected job type "%1" on volume "%2" memory usage has dropped to desirable level.%n%3\r\n
0xb000102e | Data Deduplication cancelled job type "%1" on volume "%2". It uses too much memory than the amount assigned to it.%n%3\r\n
0xb000102f | Data Deduplication cancelled job type "%1" on volume "%2". Memory resource is running low on the machine or in the job.%n%3\r\n
0xb0001030 | Data Deduplication job type "%1" on volume "%2" failed to report completion to the service with error: %3.%n%4\r\n
0xb0001031 | Data Deduplication detected a container cannot be compacted or updated because it has reached the maximum generation.%n%1\r\n
0xb0001032 | Data Deduplication corruption log "%1" is corrupted.%n%2\r\n
0xb0001033 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". Please run scrubbing job to process corruption log. No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001034 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001035 | Data Deduplication scheduler failed to uninitialize with error "%1".%n%2\r\n
0xb0001036 | Data Deduplication detected a new container could not be created in a chunk store because it ran out of available container Id.%n%1\r\n
0xb0001037 | Data Deduplication full garbage collection phase 1 (cleaning file related metadata) on volume "%1" failed with error: %2.  The job will continue with phase 2 execution (data chunk cleanup).%n%3\r\n
0xb0001039 | Data Deduplication full garbage collection could not achieve maximum space reclamation because delete logs for data container %1 could not be cleaned up.%n%2\r\n
0xb000103a | Some files could not be deduplicated because of FSRM Quota violations on volume %1. Files skipped are likely compressed or sparse files in folders which are at quota or close to their quota limit. Please consider increasing the quota limit for folders that are at their quota limit or close to it.%n%2\r\n
0xb000103b | Data Deduplication failed to dedup file %1 "%2" due to fatal error %3%n%4\r\n
0xb000103c | Data Deduplication encountered corruption while accessing a file in chunk store.%n%1\r\n
0xb000103d | Data Deduplication encountered corruption while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103e | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103f | Data Deduplication is unable to access file %1 because the file is in use.%n%2\r\n
0xb0001040 | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store.%n%1\r\n
0xb0001041 | Data Deduplication cannot run the job on volume %1 because the dedup store version compatiblity check failed with error %2.%n%3\r\n
0xb0001042 | Data Deduplication has disabled the volume %1 because it has discovered too many corruptions. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001043 | Data Deduplication has detected a corrupt corruption metadata file on the store at %1. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001045 | Data Deduplication cannot be enabled on SIS volume "%1". Error: %2.%n%3\r\n
0xb0001046 | File-system is configured for case-sensitive file/folder names. Data Deduplication does not support case-sensitive file-system mode.%n%1\r\n
0xb0001049 | Data Deduplication changed scrubbing job to read-only due to insufficient disk space.%n%1\r\n
0xb000104b | Data Deduplication has disabled the volume %1 because there are missing or corrupt containers. Please run deep scrubbing on the volume.%n%2\r\n
0xb000104d | Data Deduplication encountered a disk-full error.%n%1\r\n
0xb000104e | Data Deduplication job cannot run on volume "%1" due to insufficient disk space.%n%2\r\n
0xb000104f | Data Deduplication job cannot run on offline volume "%1".%n%2\r\n
0xb0001050 | Data Deduplication recovered a corrupt or missing file.%n%1\r\n
0xb0001051 | Data Deduplication encountered a corrupted metadata file. To correct the problem, schedule or manually run a Garbage Collection job on the affected volume with the -Full option.%n%1\r\n
0xb0001052 | Data Deduplication encountered chunk %1 with corrupted header while updating container. The corrupted chunk is replicated to the new container %2.%n%3\r\n
0xb0001053 | Data Deduplication encountered chunk %1 with transient header corruption while updating container. The corrupted chunk is NOT replicated to the new container %2.%n%3\r\n
0xb0001054 | Data Deduplication failed to read chunk container redirection table from file %1 with error %2.%n%3\r\n
0xb0001055 | Data Deduplication failed to initialize reparse point index table for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001056 | Data Deduplication failed to deep scrub container file %1 on volume %2 with error %3.%n%4\r\n
0xb0001057 | Data Deduplication failed to load stream map log for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001058 | Data Deduplication found a duplicate local chunk id %1 in container file %2.%n%3\r\n
0xb0001059 | Data Deduplication job type "%1" on volume "%2" was cancelled manually.%n%3\r\n
0xb000105a | Scheduled data Deduplication job type "%1" on volume "%2" was cancelled.%n%3\r\n
0xb000105d | The Data Deduplication chunk store statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105e | The Data Deduplication volume statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105f | Data Deduplication failed to append to deep scrubbing log file %1 with error %2.%n%3\r\n
0xb0001060 | Data Deduplication encountered a failure during deep scrubbing on store %1 with error %2.%n%3\r\n
0xb0001061 | Data Deduplication cancelled job type "%1" on volume "%2". The job violated Csv dedup job placement policy.%n%3\r\n
0xb0001062 | Data Deduplication cancelled job type "%1" on volume "%2". The csv job monitor has been uninitialized.%n%3\r\n
0xb0001063 | Data Deduplication encountered a IO device error while accessing a file on the volume. This is likely a hardware fault in the storage subsystem.%n%1\r\n
0xb0001064 | Data Deduplication encountered an unexpected error. If this is a cluster, verify Data Deduplication is enabled on all nodes of the cluster.%n%1\r\n
0xb0001065 | Attempted to disable data access for data deduplicated CSV volume "%1" without maintenance mode. Data access can only be disabled for a CSV volume when in maintenance mode. Place volume into maintenance mode and retry.%n%2\r\n
0xb0001800 | Data Deduplication service could not unoptimize file "%5%6%7". Error %8, "%9".\r\n
0xb0001801 | Data Deduplication service failed to unoptimize too many files %3. Some files are not reported.\r\n
0xb0001802 | Data Deduplication service has finished unoptimization on volume %3 with no errors.\r\n
0xb0001803 | Data Deduplication service has finished unoptimization on volume %3 with %4 errors.\r\n
0xb0001804 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6\r\n
0xb0001805 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6%nFull: %7\r\n
0xb0001806 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6%nFull: %7%nRead-only: %8\r\n
0xb0001809 | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate: %7%nSaved space: %8%nVolume used space: %9%nVolume free space: %10%nOptimized file count: %11%nIn-policy file count: %12%nJob processed space (bytes): %13%nJob elapsed time (seconds): %14%nJob throughput (MB/second): %15\r\n
0xb000180a | %1 job has completed.%n%nFull: %2%nVolume: %5 (%4)%nError code: %6%nError message: %7\r\n
0xb000180b | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6\r\n
0xb000180c | %1 job has completed.%n%nFull: %2%nRead-only: %3%nVolume: %6 (%5)%nError code: %7%nError message: %8\r\n
0xb000180e | %1 job has been queued.%n%nVolume: %4 (%3)%nSystem memory percent: %5 %nPriority: %6%nSchedule mode: %7\r\n
0xb000181c | Restore of deduplicated file "%1" failed with the following error: %2, "%3".\r\n
0xb0002000 | Data Deduplication detected job type "%1" on volume "%2" working set is low. Ratio to commit size is %3.%n%4\r\n
0xb0002001 | Data Deduplication detected job type "%1" on volume "%2" working set has recovered to desirable level.%n%3\r\n
0xb0002002 | Data Deduplication detected job type "%1" on volume "%2" page fault rate is high. The rate is %3 page faults per second.%n%4\r\n
0xb0002003 | Data Deduplication detected job type "%1" on volume "%2" page fault rate has lowered to desirable level. The rate is %3 page faults per second.%n%4\r\n
0xb0002004 | Data Deduplication failed to dedup file "%1" with file ID %2 due to non-fatal error %3%n%4.%n%nNote: You can retrieve the file name by running the command FSUTIL FILE QUERYFILENAMEBYID on the file in question.\r\n
0xb000200c | Data Deduplication has aborted a group commit session.%n%nFile count: %1%nError: %2%n%3\r\n
0xb000201c | Fail to open dedup setting registry key\r\n
0xb000201d | Data Deduplication failed to dedup file "%1" with file ID %2 due to oplock break%n%3\r\n
0xb000201e | Data Deduplication failed to load hotspot table from file %1 due to error %2.%n%3\r\n
0xb000201f | Data Deduplication failed to initialize oplock.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb0002020 | Data Deduplication while running job on volume %1 detected invalid physical sector size %2. Using default value %3.%n%4\r\n
0xb0002021 | Data Deduplication detected an unsupported chunk store container.%n%1\r\n
0xb0002022 | Data Deduplication could not create window to receive task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002023 | Data Deduplication could not create thread to poll for task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002024 | An attempt was made to perform an initialization operation when initialization has already been completed.%n%1\r\n
0xb0002028 | Data Deduplication created emergency file %1.%n%3\r\n
0xb0002029 | Data Deduplication failed to create emergency file %1 with error %2.%n%3\r\n
0xb000202a | Data Deduplication deleted emergency file %1.%n%3\r\n
0xb000202b | Data Deduplication failed to delete emergency file %1 with error %2.%n%3\r\n
0xb000202c | Data Deduplication detected a chunk store container with misaligned valid data length.%n%1\r\n
0xb000202d | Data Deduplication Garbage Collection encountered a delete log entry with an invalid stream map signature for stream map Id %1.%n%2\r\n
0xb000202e | Data Deduplication failed to initialize oplock as the file appears to be missing.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb000202f | Data Deduplication skipped too many file-level errors. We will not log more than %1 file-level errors per job.%n%2\r\n
0xb0002030 | Data Deduplication diagnostic warning.%n%n%1%n%2\r\n
0xb0002031 | Data Deduplication diagnostic information.%n%n%1%n%2\r\n
0xb0002032 | Data Deduplication found file %1 with a stream map id %2 in container file %3 marked for deletion.%n%4\r\n
0xb0002033 | Failed to enqueue job of type "%1" on volume "%2".%n%3\r\n
0xb0002034 | Error terminating job host process for job type "%1" on volume "%2" (process id: %3).%n%4\r\n
0xb0002035 | Data Deduplication encountered corrupted chunk %1 while updating container. Corrupted data that cannot be repaired will be copied as-is to the new container %2.%n%3\r\n
0xb0002036 | Data Deduplication job type "%1" on volume "%2" failed to exit gracefully.%n%3\r\n
0xb0002037 | Data Deduplication job host for job type "%1" on volume "%2" exited unexpectedly.%n%3\r\n
0xb0002038 | Data Deduplication has failed to load corruption metadata file on the store at %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb0002039 | Data Deduplication full garbage collection phase 1 on volume "%1" encountered an error %2 while processing file %3. Phase 1 will need to be aborted since garbage collection of file-related metadata is unsafe to continue on file errors.%n%4\r\n
0xb000203a | Data Deduplication has failed to process corruption metadata file %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb000203b | Data Deduplication has failed to load a corrupted metadata file %1 due to error %2. Deleting the file and continuing.%n%3\r\n
0xb000203c | Data Deduplication has failed to set NTFS allocation size for container file %1 due to error %2.%n%3\r\n
0xb000203d | Data Deduplication configured to use BCrypt provider '%1' for hash algorithm %2.%n%3\r\n
0xb000203e | Data Deduplication could not use BCrypt provider '%1' for hash algorithm %2 due to an error in operation %3. Reverting to the Microsoft primitive CNG provider.%n%4\r\n
0xb000203f | Data Deduplication failed to include file "%1" in file metadata analysis calculations.%n%2\r\n
0xb0002040 | Data Deduplication failed to include stream map %1 in file metadata analysis calculations.%n%2\r\n
0xb0002041 | Data Deduplication encountered an error for file "%1" while scanning files and folders.%n%2\r\n
0xb0002042 | Data Deduplication encountered an error while attempting to resume processing. Please consult the event log parameters for more details about the current file being processed.%n%1\r\n
0xb0002043 | Data Deduplication encountered an error %1 whle scanning usn journal on volume %2 for updating hot range tracking.%n%3\r\n
0xb0002044 | Data Deduplication could not truncate the stream of an optimized file. No action is required. Error: %1%n%n%2\r\n
0xb0002800 | %1 job memory requirements.%n%nVolume: %4 (%3)%nMinimum memory: %5 MB%nMaximum memory: %6 MB%nMinimum disk: %7 MB\r\n
0xb0002801 | %1 reconciliation has started.%n%nVolume: %4 (%3)\r\n
0xb0002802 | %1 reconciliation has completed.%n%nVolume: %4 (%3)%nReconciled containers: %5%nUnreconciled containers: %6%nMerged containers: %7%nTotal reconciled references: %8%nError code: %9%nError message: %10\r\n
0xb0002803 | %1 job on volume %4 (%3) was configured with insufficient memory.%n%nSystem memory percentage: %5%nAvailable memory: %8 MB%nMinimum required memory: %6 MB\r\n
0xb0002804 | Optimization memory details for %1 job on volume %3 (%2).\r\n
0xb0002805 | An open file was skipped during optimization. No action is required.%n%nFileId: %2%nSkip Reason: %1\r\n
0xb0002806 | An operation succeeded after one or more retries. Operation: %1; FileId: %3; Number of retries: %2\r\n
0xb0003200 | Data Deduplication service detected corruption in "%5%6%7". The corruption cannot be repaired.\r\n
0xb0003201 | Data Deduplication service detected corruption (%7) in "%6". See the event details for more information.\r\n
0xb0003202 | Data Deduplication service detected a corrupted item (%11 - %13, %8, %9, %10, %12) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003203 | Data Deduplication service has finished scrubbing on volume %3. It did not find any corruption since the last scrubbing.\r\n
0xb0003204 | Data Deduplication service found %4 corruption(s) on volume %3. All corruptions are fixed.\r\n
0xb0003205 | Data Deduplication service found %4 corruption(s) on volume %3. %5 corruption(s) are fixed. %6 user file(s) are corrupted. %7 user file(s) are fixed. For the corrupted file list, see the Microsoft/Windows/Deduplication/Scrubbing events.\r\n
0xb0003206 | Data Deduplication service found too many corruptions on volume %3. Some corruptions are not reported.\r\n
0xb0003211 | Data Deduplication service has finished scrubbing on volume %3. See the event details for more information.\r\n
0xb0003212 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003213 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003214 | Data Deduplication service encountered error while detecting corruptions in chunk store on volume %3. The error was %4. The job is aborted.\r\n
0xb0003216 | Data Deduplication service encountered error while loading corruption logs on volume %3. The error was %4. The job continues. Some corruptions may not be detected.\r\n
0xb0003217 | Data Deduplication service encountered error while cleaning up corruption logs on volume %3. The error was %4. Some corruptions may be reported again next time.\r\n
0xb0003218 | Data Deduplication service encountered error while loading hotspots mapping from chunk store on volume %3. The error was %4. Some corruptions may not be repaired.\r\n
0xb0003219 | Data Deduplication service encountered error while determining corrupted user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb000321a | Data Deduplication service found %4 corruption(s) on volume %3. %6 user file(s) are corrupted. %7 user file(s) are fixable. Please run scrubbing job in read-write mode to attempt fixing reported corruptions.\r\n
0xb000321b | Data Deduplication service fixed corruption in "%5%6%7".\r\n
0xb000321c | Data Deduplication service detected fixable corruption in "%5%6%7". Please run scrubbing job in read-write mode to fix this corruption.\r\n
0xb000321e | Data Deduplication service encountered error while repairing corruptions on volume %3. The error was %4. The repair is unsuccessful.\r\n
0xb000321f | Data Deduplication service detected a corrupted item (%6, %7, %8, %9) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003220 | Container (%8,%9) with user data is missing from the chunk store. Missing container may result from incomplete restore, incomplete migration or file-system corruption. Volume is disabled from further optimization. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0003221 | Data Deduplication service encountered error while scaning dedup user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb0003222 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003223 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003224 | Data Deduplication service detected potential data loss (%9) in "%6" due to sharing reparse data with file "%8". See the event details for more information.\r\n
0xb0003225 | Container (%8,%9) with user data is corrupt in the chunk store. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0005000 | Open stream store stream (StartingChunkId %1, FileId %2)\r\n
0xb0005001 | Open stream store stream completed %1\r\n
0xb0005002 | Prepare for paging IO (Stream %1, FileId %2)\r\n
0xb0005003 | Prepare for paging IO completed %1\r\n
0xb0005005 | Read stream map completed %1\r\n
0xb0005006 | Read chunks (Stream %1, FileId %2, IoType %3, FirstRequestChunkId %4, NextRequest %5)\r\n
0xb0005007 | Read chunks completed %1\r\n
0xb0005008 | Compute checksum (ItemType %1, DataSize %2)\r\n
0xb0005009 | Compute checksum completed %1\r\n
0xb000500a | Get container entry (ContainerId %1, Generation %2)\r\n
0xb000500b | Get container entry completed %1\r\n
0xb000500c | Get maximum generation for container (ContainerId %1, Generation %2)\r\n
0xb000500d | Get maximum generation for container completed %1\r\n
0xb000500e | Open chunk container (ContainerId %1, Generation %2, RootPath %4)\r\n
0xb000500f | Open chunk container completed %1\r\n
0xb0005010 | Initialize chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005011 | Initialize chunk container redirection table completed %1\r\n
0xb0005012 | Validate chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005013 | Validate chunk container redirection table completed %1\r\n
0xb0005014 | Get chunk container valid data length (ContainerId %1, Generation %2)\r\n
0xb0005015 | Get chunk container valid data length completed %1\r\n
0xb0005016 | Get offset from chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005017 | Get offset from chunk container redirection table completed %1\r\n
0xb0005018 | Read chunk container block (ContainerId %1, Generation %2, Buffer %3, Offset %4, Length %5, IoType %6, Synchronous %7)\r\n
0xb0005019 | Read chunk container block completed %1\r\n
0xb000501a | Clear chunk container block (Buffer %1, Size %2, BufferType %3)\r\n
0xb000501b | Clear chunk container block completed %1\r\n
0xb000501c | Copy chunk (Buffer %1, Size %2, BufferType %3, BufferOffset %4, OutputCapacity %5)\r\n
0xb000501d | Copy chunk completed %1\r\n
0xb000501e | Initialize file cache (UnderlyingFileObject %1, CacheFileSize %2)\r\n
0xb000501f | Initialize file cache completed %1\r\n
0xb0005020 | Map file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005021 | Map file cache data completed %1\r\n
0xb0005022 | Unpin file cache data(Bcb %1)\r\n
0xb0005023 | Unpin file cache data completed %1\r\n
0xb0005024 | Copy file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005025 | Copy file cache data completed %1\r\n
0xb0005026 | Read underlying file cache data (CacheFileObject %1, UnderlyingFileObject %2, Offset %3, Length %4)\r\n
0xb0005027 | Read underlying file cache data completed %1\r\n
0xb0005028 | Get chunk container file size (ContainerId %1, Generation %2)\r\n
0xb0005029 | Get chunk container file size completed %1\r\n
0xb000502a | Pin stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb000502b | Pin stream map completed %1\r\n
0xb000502c | Pin chunk container (ContainerId %1, Generation %2)\r\n
0xb000502d | Pin chunk container completed %1\r\n
0xb000502e | Pin chunk (ContainerId %1, Generation %2)\r\n
0xb000502f | Pin chunk completed %1\r\n
0xb0005030 | Allocate pool buffer (ReadLength %1, PagingIo %2)\r\n
0xb0005031 | Allocate pool buffer completed %1\r\n
0xb0005032 | Unpin chunk container (ContainerId %1, Generation %2)\r\n
0xb0005033 | Unpin chunk container completed %1\r\n
0xb0005034 | Unpin chunk (ContainerId %1, Generation %2)\r\n
0xb0005035 | Unpin chunk completed %1\r\n
0xb0006028 | Dedup read processing (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006029 | Dedup read processing completed %1\r\n
0xb000602a | Get first stream map entry (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602b | Get first stream map entry completed %1\r\n
0xb000602c | Read chunk metadata (Stream %1, CurrentOffset %2, AdjustedFinalOffset %3, FirstChunkByteOffset %4, ChunkRequestsEndOffset %5, TlCache %6)\r\n
0xb000602d | Read chunk metadata completed %1\r\n
0xb000602e | Read chunk data (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602f | Read chunk data completed %1\r\n
0xb0006030 | Reference TlCache data (TlCache %1, Stream %2)\r\n
0xb0006031 | Reference TlCache data completed %1\r\n
0xb0006032 | Read chunk data from stream store (Stream %1)\r\n
0xb0006033 | Read chunk data from stream store completed %1\r\n
0xb0006034 | Assemble chunk data\r\n
0xb0006035 | Assemble chunk data completed %1\r\n
0xb0006036 | Decompress chunk data\r\n
0xb0006037 | Decompress chunk data completed %1\r\n
0xb0006038 | Copy chunk data in to user buffer (BytesCopied %1)\r\n
0xb0006039 | Copy chunk data in to user buffer completed %1\r\n
0xb000603a | Insert chunk data in to tlcache\r\n
0xb000603b | Insert chunk data in to tlcache completed %1\r\n
0xb000603c | Read data from dedup reparse point file (FileObject %1, Offset %2, Length %3)\r\n
0xb000603d | Read underlying file cache data completed %1\r\n
0xb000603e | Prepare stream map (StreamContext %1)\r\n
0xb000603f | Prepare stream map completed %1\r\n
0xb0006040 | Patch clean ranges (FileObject %1, Offset %2, Length %3)\r\n
0xb0006041 | Patch clean ranges completed %1\r\n
0xb0006042 | Writing data to dedup file (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006043 | Writing data to dedup file completed %1\r\n
0xb0006044 | Queue write request on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006045 | Queue write request on dedup file completed %1\r\n
0xb0006046 | Do copy on write work on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006047 | Do copy on write work on dedup file completed %1\r\n
0xb0006048 | Do full recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006049 | Do full recall on dedup file completed %1\r\n
0xb000604a | Do partial recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604b | Do partial recall on dedup file completed %1\r\n
0xb000604c | Do dummy paging read on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604d | Do dummy paging read on dedup file completed %1\r\n
0xb000604e | Read clean data for recalling file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604f | Read clean data for recalling file completed %1\r\n
0xb0006050 | Write clean data to dedup file normally (FileObject %1, Offset %2, Length %3)\r\n
0xb0006051 | Write clean data to dedup file completed %1\r\n
0xb0006052 | Write clean data to dedup file paged (FileObject %1, Offset %2, Length %3)\r\n
0xb0006053 | Write clean data to dedup file paged completed %1\r\n
0xb0006054 | Recall dedup file using paging Io (FileObject %1, Offset %2, Length %3)\r\n
0xb0006055 | Recall dedup file using paging Io completed %1\r\n
0xb0006056 | Flush dedup file after recall (FileObject %1)\r\n
0xb0006057 | Flush dedup file after recall completed %1\r\n
0xb0006058 | Update bitmap after recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006059 | Update bitmap after recall on dedup file completed %1\r\n
0xb000605a | Delete dedup reparse point (FileObject %1)\r\n
0xb000605b | Delete dedup reparse point completed %1\r\n
0xb000605c | Open dedup file (FilePath %1)\r\n
0xb000605d | Open dedup file completed %1\r\n
0xb000605e | Locking user buffer for read\r\n
0xb000605f | Locking user buffer for read completed %1\r\n
0xb0006060 | Get system address for MDL\r\n
0xb0006061 | Get system address for MDL completed %1\r\n
0xb0006062 | Read clean dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006063 | Read clean dedup file completed %1\r\n
0xb0006064 | Get range state (Offset %1, Length %2)\r\n
0xb0006065 | Get range state completed %1\r\n
0xb0006066 | Get chunk body\r\n
0xb0006067 | Get chunk body completed %1\r\n
0xb0006068 | Release chunk\r\n
0xb0006069 | Release chunk completed %1\r\n
0xb000606a | Release decompress chunk context (BufferSize %1)\r\n
0xb000606b | Release decompress chunk context completed %1\r\n
0xb000606c | Prepare decompress chunk context (BufferSize %1)\r\n
0xb000606d | Prepare decompress chunk context completed %1\r\n
0xb000606e | Copy data to compressed buffer (BufferSize %1)\r\n
0xb000606f | Copy data to compressed buffer completed %1\r\n
0xb0006070 | Release data from TL Cache\r\n
0xb0006071 | Release data from TL Cache completed %1\r\n
0xb0006072 | Queue async read request (FileObject %1, Offset %2, Length %3)\r\n
0xb0006073 | Queue async read request complete %1\r\n
0xb0015004 | Read stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb1004000 | Create chunk container (%1 - %2.%3.ccc)\r\n
0xb1004001 | Create chunk container completed %1\r\n
0xb1004002 | Copy chunk container (%1 - %2.%3.ccc)\r\n
0xb1004003 | Copy chunk container completed %1\r\n
0xb1004004 | Delete chunk container (%1 - %2.%3.ccc)\r\n
0xb1004005 | Delete chunk container completed %1\r\n
0xb1004006 | Rename chunk container (%1 - %2.%3.ccc%4)\r\n
0xb1004007 | Rename chunk container completed %1\r\n
0xb1004008 | Flush chunk container (%1 - %2.%3.ccc)\r\n
0xb1004009 | Flush chunk container completed %1\r\n
0xb100400a | Rollback chunk container (%1 - %2.%3.ccc)\r\n
0xb100400b | Rollback chunk container completed %1\r\n
0xb100400c | Mark chunk container (%1 - %2.%3.ccc) read-only\r\n
0xb100400d | Mark chunk container read-only completed %1\r\n
0xb100400e | Write chunk container (%1 - %2.%3.ccc) redirection table at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb100400f | Write chunk container redirection table completed %1\r\n
0xb1004011 | Write chunk container header completed %1\r\n
0xb1004013 | Insert data chunk header completed %1\r\n
0xb1004015 | Insert data chunk body completed %1 with ChunkId %2\r\n
0xb1004019 | Write delete log header completed %1\r\n
0xb100401b | Append delete log entries completed %1\r\n
0xb100401d | Delete delete log completed %1\r\n
0xb100401f | Rename delete log completed %1\r\n
0xb1004021 | Write chunk container bitmap completed %1\r\n
0xb1004023 | Delete chunk container bitmap completed %1\r\n
0xb1004024 | Write merge log (%5 - %6.%7.merge.log) header\r\n
0xb1004025 | Write merge log header completed %1\r\n
0xb1004027 | Insert hotspot chunk header completed %1\r\n
0xb1004029 | Insert hotspot chunk body completed %1 with ChunkId %2\r\n
0xb100402b | Insert stream map chunk header completed %1\r\n
0xb100402d | Insert stream map chunk body completed %1 with ChunkId %2\r\n
0xb100402f | Append merge log entries completed %1\r\n
0xb1004030 | Delete merge log (%1 - %2.%3.merge.log)\r\n
0xb1004031 | Delete merge log completed %1\r\n
0xb1004032 | Flush merge log (%1 - %2.%3.merge.log)\r\n
0xb1004033 | Flush merge log completed %1\r\n
0xb1004034 | Update file list entries (Remove: %1, Add: %2)\r\n
0xb1004035 | Update file list entries completed %1\r\n
0xb1004036 | Set dedup reparse point on %2 (FileId %1) (ReparsePoint: SizeBackedByChunkStore %3, StreamMapInfoSize %4, StreamMapInfo %5)\r\n
0xb1004037 | Set dedup reparse point completed %1 (%2)\r\n
0xb1004038 | Set dedup zero data on %2 (FileId %1)\r\n
0xb1004039 | Set dedup zero data completed %1\r\n
0xb100403a | Flush reparse point files\r\n
0xb100403b | Flush reparse point files completed %1\r\n
0xb100403c | Set sparse on file id %1\r\n
0xb100403d | Set sparse completed %1\r\n
0xb100403e | FSCTL_SET_ZERO_DATA on file id %1 at offset %2 and BeyondFinalZero %3\r\n
0xb100403f | FSCTL_SET_ZERO_DATA completed %1\r\n
0xb1004040 | Rename chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1004041 | Rename chunk container bitmap completed %1\r\n
0xb1004042 | Insert padding chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1004043 | Insert padding chunk header completed %1\r\n
0xb1004044 | Insert padding chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1004045 | Insert padding chunk body completed %1 with ChunkId %2\r\n
0xb1004046 | Insert batch of chunks to chunk container (%1 - %2.%3.ccc) at offset %4 (BatchChunkCount %5, BatchDataSize %6)\r\n
0xb1004047 | Insert batch of chunks completed %1\r\n
0xb1004049 | Write chunk container directory completed %1\r\n
0xb100404b | Delete chunk container directory completed %1\r\n
0xb100404c | Rename chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb100404d | Rename chunk container directory completed %1\r\n
0xb1014010 | Write chunk container (%5 - %6.%7.ccc) header at offset %8 (Header: USN %9, VDL %10, #Chunk %11, NextLocalId %12, Flags %13, LastAppendTime %14, BackupRedirectionTableOfset %15, LastReconciliationLocalId %16)\r\n
0xb1014012 | Insert data chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1014014 | Insert data chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014018 | Write delete log (%5 - %6.%7.delete.log) header\r\n
0xb101401a | Append delete log (%1 - %2.%3.delete.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb101401c | Delete delete log (%1 - %2.%3.delete.log)\r\n
0xb101401e | Rename delete log (%1 - %2.%3.delete.log)\r\n
0xb1014020 | Write chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4) (Bitmap: BitLength %5, StartIndex %6, Count %7)\r\n
0xb1014022 | Delete chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1014026 | Insert hotspot chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014028 | Insert hotspot chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb101402a | Insert stream map chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014048 | Write chunk container directory (%1 - %2) for chunk container (%1 - %3.%4) (Directory: EntryCount %5)\r\n
0xb101404a | Delete chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb102402e | Append merge log (%1 - %2.%3.merge.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb103402c | Insert stream map chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7) (Entries: StartIndex %8, Count %9)\r\n
0xd0000001 | Chunk header\r\n
0xd0000002 | Chunk body\r\n
0xd0000003 | Container header\r\n
0xd0000004 | Container redirection table\r\n
0xd0000005 | Hotspot table\r\n
0xd0000006 | Delete log header\r\n
0xd0000007 | Delete log entry\r\n
0xd0000008 | GC bitmap header\r\n
0xd0000009 | GC bitmap entry\r\n
0xd000000a | Merge log header\r\n
0xd000000b | Merge log entry\r\n
0xd000000c | Data\r\n
0xd000000d | Stream map\r\n
0xd000000e | Hotspot\r\n
0xd000000f | Optimization\r\n
0xd0000010 | Garbage Collection\r\n
0xd0000011 | Scrubbing\r\n
0xd0000012 | Unoptimization\r\n
0xd0000013 | Analysis\r\n
0xd0000014 | Low\r\n
0xd0000015 | Normal\r\n
0xd0000016 | High\r\n
0xd0000017 | Cache\r\n
0xd0000018 | Non-cache\r\n
0xd0000019 | Paging\r\n
0xd000001a | Memory map\r\n
0xd000001b | Paging memory map\r\n
0xd000001c | None\r\n
0xd000001d | Pool\r\n
0xd000001e | PoolAligned\r\n
0xd000001f | MDL\r\n
0xd0000020 | Map\r\n
0xd0000021 | Cached\r\n
0xd0000022 | NonCached\r\n
0xd0000023 | Paged\r\n
0xd0000024 | container file\r\n
0xd0000025 | file list file\r\n
0xd0000026 | file list header\r\n
0xd0000027 | file list entry\r\n
0xd0000028 | primary file list file\r\n
0xd0000029 | backup file list file\r\n
0xd000002a | Scheduled\r\n
0xd000002b | Manual\r\n
0xd000002c | recall bitmap header\r\n
0xd000002d | recall bitmap body\r\n
0xd000002e | recall bitmap missing\r\n
0xd000002f | Recall bitmap\r\n
0xd0000030 | Unknown\r\n
0xd0000031 | The pipeline handle was closed\r\n
0xd0000032 | The file was deleted\r\n
0xd0000033 | The file was overwritten\r\n
0xd0000034 | The file was recalled\r\n
0xd0000035 | A transaction was started on the file\r\n
0xd0000036 | The file was encrypted\r\n
0xd0000037 | The file was compressed\r\n
0xd0000038 | Set Zero Data was called on the file\r\n
0xd0000039 | Extended Attributes were set on the file\r\n
0xd000003a | A section was created on the file\r\n
0xd000003b | The file was shrunk\r\n
0xd000003c | A long-running IO operation prevented optimization\r\n
0xd000003d | An IO operation failed\r\n
0xd000003e | Notifying Optimization\r\n
0xd000003f | Setting the Reparse Point\r\n
0xd0000040 | Truncating the file\r\n
0xd1000001 | None\r\n
0xd1000002 | LZNT1\r\n
0xd1000003 | Xpress\r\n
0xd1000004 | Xpreff Huff\r\n
0xd1000005 | None\r\n
0xd1000006 | Standard\r\n
0xd1000007 | Max\r\n
0xd1000008 | Hybrid\r\n
0xf0000001 | None\r\n
0xf0000002 | Bad checksum\r\n
0xf0000003 | Inconsistent metadata\r\n
0xf0000004 | Invalid header metadata\r\n
0xf0000005 | Missing file\r\n
0xf0000006 | Bad checksum (storage subsystem)\r\n
0xf0000007 | Corruption (storage subsystem)\r\n
0xf0000008 | Corruption (missing metadata)\r\n
0xf0000009 | Possible data loss (duplicate reparse data)\r\n

### 10.0.10586.0, 10.0.14393.0

Message identifier | Message string
--- | ---
0x00565301 | Reconciliation of chunk store is due.\r\n
0x00565302 | There are no actions associated with this job.\r\n
0x00565303 | Data deduplication cannot runing this job on this Csv volume on this node.\r\n
0x00565304 | Data deduplication cannot runing this cmdlet on this Csv volume on this node.\r\n
0x10000001 | Reporting\r\n
0x10000002 | Filter\r\n
0x10000003 | Kernel mode stream store\r\n
0x10000004 | Kernel mode chunk store\r\n
0x10000005 | Kernel mode chunk container\r\n
0x10000006 | Kernel mode file cache\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Data Deduplication Optimization Task\r\n
0x70000002 | Data Deduplication Garbage Collection Task\r\n
0x70000003 | Data Deduplication Scrubbing Task\r\n
0x70000004 | Data Deduplication Unoptimization Task\r\n
0x70000005 | Open stream store stream\r\n
0x70000006 | Prepare for paging IO\r\n
0x70000007 | Read stream map\r\n
0x70000008 | Read chunks\r\n
0x70000009 | Compute checksum\r\n
0x7000000a | Get container entry\r\n
0x7000000b | Get maximum generation for container\r\n
0x7000000c | Open chunk container\r\n
0x7000000d | Initialize chunk container redirection table\r\n
0x7000000e | Validate chunk container redirection table\r\n
0x7000000f | Get chunk container valid data length\r\n
0x70000010 | Get offset from chunk container redirection table\r\n
0x70000011 | Read chunk container block\r\n
0x70000012 | Clear chunk container block\r\n
0x70000013 | Copy chunk\r\n
0x70000014 | Initialize file cache\r\n
0x70000015 | Map file cache data\r\n
0x70000016 | Unpin file cache data\r\n
0x70000017 | Copy file cache data\r\n
0x70000018 | Read underlying file cache data\r\n
0x70000019 | Get chunk container file size\r\n
0x7000001a | Pin stream map\r\n
0x7000001b | Pin chunk container\r\n
0x7000001c | Pin chunk\r\n
0x7000001d | Allocate pool buffer\r\n
0x7000001e | Unpin chunk container\r\n
0x7000001f | Unpin chunk\r\n
0x70000020 | Dedup read processing\r\n
0x70000021 | Get first stream map entry\r\n
0x70000022 | Read chunk metadata\r\n
0x70000023 | Read chunk data\r\n
0x70000024 | Reference TlCache data\r\n
0x70000025 | Read chunk data from stream store\r\n
0x70000026 | Assemble chunk data\r\n
0x70000027 | Decompress chunk data\r\n
0x70000028 | Copy chunk data in to user buffer\r\n
0x70000029 | Insert chunk data in to tlcache\r\n
0x7000002a | Read data from dedup reparse point file\r\n
0x7000002b | Prepare stream map\r\n
0x7000002c | Patch clean ranges\r\n
0x7000002d | Writing data to dedup file\r\n
0x7000002e | Queue write request on dedup file\r\n
0x7000002f | Do copy on write work on dedup file\r\n
0x70000030 | Do full recall on dedup file\r\n
0x70000031 | Do partial recall on dedup file\r\n
0x70000032 | Do dummy paging read on dedup file\r\n
0x70000033 | Read clean data for recalling file\r\n
0x70000034 | Write clean data to dedup file normally\r\n
0x70000035 | Write clean data to dedup file paged\r\n
0x70000036 | Recall dedup file using paging Io\r\n
0x70000037 | Flush dedup file after recall\r\n
0x70000038 | Update bitmap after recall on dedup file\r\n
0x70000039 | Delete dedup reparse point\r\n
0x7000003a | Open dedup file\r\n
0x7000003b | Locking user buffer for read\r\n
0x7000003c | Get system address for MDL\r\n
0x7000003d | Read clean dedup file\r\n
0x7000003e | Get range state\r\n
0x7000003f | Get chunk body\r\n
0x70000040 | Release chunk\r\n
0x70000041 | Release decompress chunk context\r\n
0x70000042 | Prepare decompress chunk context\r\n
0x70000043 | Copy data to compressed buffer\r\n
0x70000044 | Release data from TL Cache\r\n
0x70000045 | Queue async read request\r\n
0x80565301 | The requested object was not found.\r\n
0x80565302 | One (or more) of the arguments given to the task scheduler is not valid.\r\n
0x80565303 | The specified object already exists.\r\n
0x80565304 | The specified path was not found.\r\n
0x80565305 | The specified user is invalid.\r\n
0x80565306 | The specified path is invalid.\r\n
0x80565307 | The specified name is invalid.\r\n
0x80565308 | The specified property is out of range.\r\n
0x80565309 | A required filter driver is either not installed, not loaded, or not ready for service.\r\n
0x8056530a | There is insufficient disk space to perform the requested operation.\r\n
0x8056530b | The specified volume type is not supported. Deduplication is supported on fixed, write-enabled NTFS data volumes and CSV backed by NTFS data volumes.\r\n
0x8056530c | Data deduplication encountered an unexpected error. Check the Data Deduplication Operational event log for more information.\r\n
0x8056530d | The specified scan log cursor has expired.\r\n
0x8056530e | The file system might be corrupted.  Please run the CHKDSK utility.\r\n
0x8056530f | A volume shadow copy could not be created or was unexpectedly deleted.\r\n
0x80565310 | Data deduplication encountered a corrupted XML configuration file.\r\n
0x80565311 | The Data Deduplication service could not access the global configuration because the Cluster service is not running.\r\n
0x80565312 | The Data Deduplication service could not access the global configuration because it has not been installed yet.\r\n
0x80565313 | Data deduplication failed to access the volume. It may be offline.\r\n
0x80565314 | The module encountered an invalid parameter or a valid parameter with an invalid value, or an expected module parameter was not found. Check the operational event log for more information.\r\n
0x80565315 | An attempt was made to perform an initialization operation when initialization has already been completed.\r\n
0x80565316 | An attempt was made to perform an uninitialization operation when that operation has already been completed.\r\n
0x80565317 | The Data Deduplication service detected an internal folder that is not secure. To secure the folder, reinstall deduplication on the volume.\r\n
0x80565318 | Data chunking has already been initiated.\r\n
0x80565319 | An attempt was made to perform an operation from an invalid state.\r\n
0x8056531a | An attempt was made to perform an operation before initialization.\r\n
0x8056531b | Call ::PushBuffer to continue chunking or ::Drain to enumerate any partial chunks.\r\n
0x8056531c | The Data Deduplication service detected multiple chunk store folders; however, only one chunk store folder is permitted. To fix this issue, reinstall deduplication on the volume.\r\n
0x8056531d | The data is invalid.\r\n
0x8056531e | The process is in an unknown state.\r\n
0x8056531f | The process is not running.\r\n
0x80565320 | There was an error while opening the file.\r\n
0x80565321 | The job process could not start because the job was not found.\r\n
0x80565322 | The client process ID does not match the ID of the host process that was started.\r\n
0x80565323 | The specified volume is not enabled for deduplication.\r\n
0x80565324 | A zero-character chunk ID is not valid.\r\n
0x80565325 | The index is filled to capacity.\r\n
0x80565327 | Session already exists.\r\n
0x80565328 | The compression format selected is not supported.\r\n
0x80565329 | The compressed buffer is larger than the uncompressed buffer.\r\n
0x80565330 | The buffer is not large enough.\r\n
0x8056533a | Index Scratch Log Error in: Seek, Read, Write, or Create\r\n
0x8056533b | The job type is invalid.\r\n
0x8056533c | Persistence layer enumeration error.\r\n
0x8056533d | The operation was cancelled.\r\n
0x8056533e | This job will not run at the scheduled time because it requires more memory than is currently available.\r\n
0x80565341 | The job was terminated while in a cancel or pending state.\r\n
0x80565342 | The job was terminated while in a handshake pending state.\r\n
0x80565343 | The job was terminated due to a service shutdown.\r\n
0x80565344 | The job was abandoned before starting.\r\n
0x80565345 | The job process exited unexpectedly.\r\n
0x80565346 | The Data Deduplication service detected that the container cannot be compacted or updated because it has reached the maximum generation version. \r\n
0x80565347 | The corruption log has reached its maximum size.\r\n
0x80565348 | The data deduplication scrubbing job failed to process the corruption logs.\r\n
0x80565349 | Data deduplication failed to create new chunk store container files. Allocate more space to the volume.\r\n
0x80565350 | An error occurred while opening the file because the file was in use. \r\n
0x80565351 | An error was discovered while deduplicating the file. The file is now skipped.\r\n
0x80565352 | File Server Deduplication encountered corruption while enumerating chunks in a chunk store.\r\n
0x80565353 | The scan log is not valid.\r\n
0x80565354 | The data is invalid due to checksum (CRC) mismatch error.\r\n
0x80565355 | Data deduplication encountered file corruption error.\r\n
0x80565356 | Job completed with some errors. Check event logs for more details.\r\n
0x80565357 | Data deduplication is not supported on the version of the chunk store found on this volume.\r\n
0x80565358 | Data deduplication encountered an unknown version of chunk store on this volume.\r\n
0x80565359 | The job was assigned less memory than the minimum it needs to run.\r\n
0x8056535a | The data deduplication job schedule cannot be modified.\r\n
0x8056535b | The valid data length of chunk store container is misaligned.\r\n
0x8056535c | File access is denied.\r\n
0x8056535d | Data deduplication job stopped due to too many corrupted files.\r\n
0x8056535e | Data deduplication job stopped due to an internal error in the BCrypt SHA-512 provider.\r\n
0x8056535f | Data deduplication job stopped for store reconciliation.\r\n
0x80565360 | File skipped for deduplication due to its size.\r\n
0x80565361 | File skipped due to deduplication retry limit.\r\n
0x80565362 | The pipeline buffer cache is full.\r\n
0x80565363 | Another Data deduplication job already running on this volume.\r\n
0x80565364 | Data deduplication cannot run this job on this Csv volume on this node. Try running the job on the Csv volume resource owner node.\r\n
0x80565365 | Data deduplication failed to initialize cluster state on this node.\r\n
0x80565366 | Optimization of the range was aborted by the dedup filter driver.\r\n
0x80565367 | The operation could not be performed because of a concurrent IO operation.\r\n
0x80565368 | Data deduplication encountered an unexpected error. Verify deduplication is enabled on all nodes if in a cluster configuration. Check the Data Deduplication Operational event log for more information.\r\n
0x80565369 | Data access for data deduplicated CSV volumes can only be disabled when in maintenance mode. Check the Data Deduplication Operational event log for more information.\r\n
0x8056536a | Data Deduplication encountered an IO device error that may indicate a hardware fault in the storage subsystem.\r\n
0x8056536b | Data deduplication cannot run this cmdlet on this Csv volume on this node. Try running the cmdlet on the Csv volume resource owner node.\r\n
0x8056536c | Deduplication job not supported during rolling cluster upgrade.\r\n
0x8056536d | Deduplication setting not supported during rolling cluster upgrade.\r\n
0x90000001 | Data Deduplication\r\n
0x90000002 | Application\r\n
0x91000001 | Data Deduplication Change Events\r\n
0xb0001000 | Volume "%1" appears as disconnected and it is ignored by the service.  You may want to rescan disks.   Error: %2.%n%3\r\n
0xb0001001 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3". Most likely the CPU is under heavy load.  Error: %4.%n%5\r\n
0xb0001002 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3".  Error: %4.%n%5\r\n
0xb0001003 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3" during Safe Mode. The Data Deduplication service cannot start while in safe mode.  Error: %4.%n%5\r\n
0xb0001004 | A critical component required by Data Deduplication is not registered. This might happen if an error occurred during Windows setup, or if the computer does not have the Windows Server 2012 or later version of Deduplication service installed. The error returned from CoCreateInstance on class with CLSID %1 and Name "%2" on machine "%3" is %4.%n%5\r\n
0xb0001005 | Data Deduplication service is shutting down due to idle timeout.%n%1\r\n
0xb0001006 | Data Deduplication service is shutting down due to shutdown event from the Service Control Manager.%n%1\r\n
0xb0001007 | Data Deduplication job of type "%1" on volume "%2" has completed with return code: %3%n%4\r\n
0xb0001008 | Data Deduplication error: Unexpected error calling routine %1.  hr = %2.%n%3\r\n
0xb0001009 | Data Deduplication error: Unexpected error.%n%1\r\n
0xb000100a | Data Deduplication warning: %1%nError: %2.%n%3\r\n
0xb000100b | Data Deduplication error: Unexpected COM error %1: %2.  Error code: %3.%n%4\r\n
0xb000100c | Data Deduplication was unable to access the following file or volume: "%1".  This file or volume might be locked by another application right now, or you might need to give Local System access to it.%n%2\r\n
0xb000100d | Data Deduplication encountered an unexpected error during volume scan of volumes mounted at "%1" ("%2"). To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100e | Data Deduplication was unable to create or access the shadow copy for volumes mounted at "%1" ("%2"). Possible causes include an improper Shadow Copy configuration, insufficient disk space, or extreme memory, I/O or CPU load of the system. To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100f | Data Deduplication was unable to access volumes mounted at "%1" ("%2"). Make sure that dismount or format operations do not happen while running deduplication.%n%3\r\n
0xb0001010 | Data Deduplication was unable to access a file or volume. Details:%n%n%1%n The volume may be inaccessible for I/O operations or marked read-only. In case of a cluster volume, this may be a transient failure during failover.%n%2\r\n
0xb0001011 | Data Deduplication was unable to scan volume "%1" ("%2").%n%3\r\n
0xb0001012 | Data Deduplication detected a corruption on file "%1" at offset ("%2").  If this condition persists then please restore the data from a previous backup.  Corruption details: Structure=%3, Corruption type = %4, Additional data = %5%n%6\r\n
0xb0001013 | Data Deduplication encountered failure while reconciling chunk store on volume "%1". The error code was %2. Reconciliation is disabled for the current optimization job.%n%3\r\n
0xb0001016 | Data Deduplication encountered corrupted chunk container %1 while performing full garbage collection. The corrupted chunk container is skipped.%n%2\r\n
0xb0001017 | Data Deduplication could not initialize change log under %1. The error code was %2.%n%3\r\n
0xb0001018 | Data Deduplication service could not mark chunk container %1 as reconciled. The error code was %2.%n%3\r\n
0xb0001019 | A Data Deduplication configuration file is corrupted. The system or volume may need to be restored from backup.%n%1\r\n
0xb000101a | Data Deduplication was unable to save one of the configuration stores on volume "%1" due to a disk-full error: If the disk is full, please clean it up (extend the volume or delete some files). If the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.%n%2\r\n
0xb000101b | Data Deduplication could not access global configuration since the cluster service is not running. Please start the cluster service and retry the operation.%n%1\r\n
0xb000101c | Shadow copy "%1" was deleted during storage report generation.  Volume "%2" might be configured with inadequate shadow copy storage area. Data Deduplication could not process this volume.%n%3\r\n
0xb000101d | Shadow copy creation failed for volume "%1" after retrying for %2 minutes because other shadow copies were being created.  Reschedule the Data Deduplication for a less busy time.%n%3\r\n
0xb000101e | Volume "%1" is not supported for shadow copy.  It is possible that the volume was removed from the system.  Data Deduplication service could not process this volume.%n%2\r\n
0xb000101f | The volume "%1" has been deleted or removed from the system.%n%2\r\n
0xb0001020 | Shadow copy creation failed for volume "%1" with error %2.  The volume might be configured with inadequate shadow copy storage area.  File Serve Deduplication service could not process this volume.%n%3\r\n
0xb0001021 | The file system on volume "%1" is potentially corrupted.  Please run the CHKDSK utility to verify and fix the file system.%n%2\r\n
0xb0001022 | Data Deduplication detected an insecure internal folder. To secure the folder, reinstall deduplication on the volume again.%n%1\r\n
0xb0001023 | Data Deduplication could not find a chunk store on the volume.%n%1\r\n
0xb0001024 | Data Deduplication detected multiple chunk store folders. To recover, reinstall deduplication on the volume.%n%1\r\n
0xb0001025 | Data Deduplication detected conflicting chunk store folders: "%1" and "%2".%n%3\r\n
0xb0001026 | The data is invalid.%n%1\r\n
0xb0001027 | Data Deduplication scheduler failed to initialize with error "%1".%n%2\r\n
0xb0001028 | Data Deduplication failed to validate job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb0001029 | Data Deduplication failed to start job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb000102c | Data Deduplication detected job type "%1" on volume "%2" uses too much memory. %3 MB is assigned. %4 MB is used.%n%5\r\n
0xb000102d | Data Deduplication detected job type "%1" on volume "%2" memory usage has dropped to desirable level.%n%3\r\n
0xb000102e | Data Deduplication cancelled job type "%1" on volume "%2". It uses too much memory than the amount assigned to it.%n%3\r\n
0xb000102f | Data Deduplication cancelled job type "%1" on volume "%2". Memory resource is running low on the machine or in the job.%n%3\r\n
0xb0001030 | Data Deduplication job type "%1" on volume "%2" failed to report completion to the service with error: %3.%n%4\r\n
0xb0001031 | Data Deduplication detected a container cannot be compacted or updated because it has reached the maximum generation.%n%1\r\n
0xb0001032 | Data Deduplication corruption log "%1" is corrupted.%n%2\r\n
0xb0001033 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". Please run scrubbing job to process corruption log. No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001034 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001035 | Data Deduplication scheduler failed to uninitialize with error "%1".%n%2\r\n
0xb0001036 | Data Deduplication detected a new container could not be created in a chunk store because it ran out of available container Id.%n%1\r\n
0xb0001037 | Data Deduplication full garbage collection phase 1 (cleaning file related metadata) on volume "%1" failed with error: %2.  The job will continue with phase 2 execution (data chunk cleanup).%n%3\r\n
0xb0001039 | Data Deduplication full garbage collection could not achieve maximum space reclamation because delete logs for data container %1 could not be cleaned up.%n%2\r\n
0xb000103a | Some files could not be deduplicated because of FSRM Quota violations on volume %1. Files skipped are likely compressed or sparse files in folders which are at quota or close to their quota limit. Please consider increasing the quota limit for folders that are at their quota limit or close to it.%n%2\r\n
0xb000103b | Data Deduplication failed to dedup file %1 "%2" due to fatal error %3%n%4\r\n
0xb000103c | Data Deduplication encountered corruption while accessing a file in chunk store.%n%1\r\n
0xb000103d | Data Deduplication encountered corruption while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103e | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103f | Data Deduplication is unable to access file %1 because the file is in use.%n%2\r\n
0xb0001040 | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store.%n%1\r\n
0xb0001041 | Data Deduplication cannot run the job on volume %1 because the dedup store version compatiblity check failed with error %2.%n%3\r\n
0xb0001042 | Data Deduplication has disabled the volume %1 because it has discovered too many corruptions. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001043 | Data Deduplication has detected a corrupt corruption metadata file on the store at %1. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001044 | Volume "%1" cannot be enabled for Data Deduplication. Data Deduplication does not support volumes larger than 64TB. Error: %2.%n%3\r\n
0xb0001045 | Data Deduplication cannot be enabled on SIS volume "%1". Error: %2.%n%3\r\n
0xb0001046 | File-system is configured for case-sensitive file/folder names. Data Deduplication does not support case-sensitive file-system mode.%n%1\r\n
0xb0001049 | Data Deduplication changed scrubbing job to read-only due to insufficient disk space.%n%1\r\n
0xb000104b | Data Deduplication has disabled the volume %1 because there are missing or corrupt containers. Please run deep scrubbing on the volume.%n%2\r\n
0xb000104d | Data Deduplication encountered a disk-full error.%n%1\r\n
0xb000104e | Data Deduplication job cannot run on volume "%1" due to insufficient disk space.%n%2\r\n
0xb000104f | Data Deduplication job cannot run on offline volume "%1".%n%2\r\n
0xb0001050 | Data Deduplication recovered a corrupt or missing file.%n%1\r\n
0xb0001051 | Data Deduplication encountered a corrupted metadata file. To correct the problem, schedule or manually run a Garbage Collection job on the affected volume with the -Full option.%n%1\r\n
0xb0001052 | Data Deduplication encountered chunk %1 with corrupted header while updating container. The corrupted chunk is replicated to the new container %2.%n%3\r\n
0xb0001053 | Data Deduplication encountered chunk %1 with transient header corruption while updating container. The corrupted chunk is NOT replicated to the new container %2.%n%3\r\n
0xb0001054 | Data Deduplication failed to read chunk container redirection table from file %1 with error %2.%n%3\r\n
0xb0001055 | Data Deduplication failed to initialize reparse point index table for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001056 | Data Deduplication failed to deep scrub container file %1 on volume %2 with error %3.%n%4\r\n
0xb0001057 | Data Deduplication failed to load stream map log for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001058 | Data Deduplication found a duplicate local chunk id %1 in container file %2.%n%3\r\n
0xb0001059 | Data Deduplication job type "%1" on volume "%2" was cancelled manually.%n%3\r\n
0xb000105a | Scheduled data Deduplication job type "%1" on volume "%2" was cancelled.%n%3\r\n
0xb000105d | The Data Deduplication chunk store statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105e | The Data Deduplication volume statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105f | Data Deduplication failed to append to deep scrubbing log file %1 with error %2.%n%3\r\n
0xb0001060 | Data Deduplication encountered a failure during deep scrubbing on store %1 with error %2.%n%3\r\n
0xb0001061 | Data Deduplication cancelled job type "%1" on volume "%2". The job violated Csv dedup job placement policy.%n%3\r\n
0xb0001062 | Data Deduplication cancelled job type "%1" on volume "%2". The csv job monitor has been uninitialized.%n%3\r\n
0xb0001063 | Data Deduplication encountered a IO device error while accessing a file on the volume. This is likely a hardware fault in the storage subsystem.%n%1\r\n
0xb0001064 | Data Deduplication encountered an unexpected error. If this is a cluster, verify Data Deduplication is enabled on all nodes of the cluster.%n%1\r\n
0xb0001065 | Attempted to disable data access for data deduplicated CSV volume "%1" without maintenance mode. Data access can only be disabled for a CSV volume when in maintenance mode. Place volume into maintenance mode and retry.%n%2\r\n
0xb0001800 | Data Deduplication service could not unoptimize file "%5%6%7". Error %8, "%9".\r\n
0xb0001801 | Data Deduplication service failed to unoptimize too many files %3. Some files are not reported.\r\n
0xb0001802 | Data Deduplication service has finished unoptimization on volume %3 with no errors.\r\n
0xb0001803 | Data Deduplication service has finished unoptimization on volume %3 with %4 errors.\r\n
0xb0001804 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb0001805 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nPriority: %7%nFull: %8%nVolume free space (MB): %9\r\n
0xb0001806 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6%nFull: %7%nRead-only: %8\r\n
0xb0001807 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6\r\n
0xb0001809 | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate (percent): %7%nSaved space (MB): %8%nVolume used space (MB): %9%nVolume free space (MB): %10%nOptimized file count: %11%nIn-policy file count: %12%nJob processed space (MB): %13%nJob elapsed time (seconds): %18%nJob throughput (MB/second): %19%nChurn processing throughput (MB/second): %20\r\n
0xb000180a | %1 job has completed.%n%nFull: %2%nVolume: %5 (%4)%nError code: %6%nError message: %7%nFreed up space (MB): %8%nVolume free space (MB): %9%nJob elapsed time (seconds): %10%nJob throughput (MB/second): %11\r\n
0xb000180b | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6\r\n
0xb000180c | %1 job has completed.%n%nFull: %2%nRead-only: %3%nVolume: %6 (%5)%nError code: %7%nError message: %8%nTotal corruption count: %9%nFixable corruption count: %10%n%nWhen corruptions are found, check more details in Scrubbing event channel.\r\n
0xb000180d | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nUnoptimized file count: %7%nJob processed space (MB): %8%nJob elapsed time (seconds): %9%nJob throughput (MB/second): %10\r\n
0xb000180e | %1 job has been queued.%n%nVolume: %4 (%3)%nSystem memory percent: %5 %nPriority: %6%nSchedule mode: %7\r\n
0xb000181c | Restore of deduplicated file "%1" failed with the following error: %2, "%3".\r\n
0xb000181d | Priority %1 job has started.%n%nVolume: %4 (%3)%nFile ID: %11%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb0002000 | Data Deduplication detected job type "%1" on volume "%2" working set is low. Ratio to commit size is %3.%n%4\r\n
0xb0002001 | Data Deduplication detected job type "%1" on volume "%2" working set has recovered to desirable level.%n%3\r\n
0xb0002002 | Data Deduplication detected job type "%1" on volume "%2" page fault rate is high. The rate is %3 page faults per second.%n%4\r\n
0xb0002003 | Data Deduplication detected job type "%1" on volume "%2" page fault rate has lowered to desirable level. The rate is %3 page faults per second.%n%4\r\n
0xb0002004 | Data Deduplication failed to dedup file "%1" with file ID %2 due to non-fatal error %3%n%4.%n%nNote: You can retrieve the file name by running the command FSUTIL FILE QUERYFILENAMEBYID on the file in question.\r\n
0xb000200c | Data Deduplication has aborted a group commit session.%n%nFile count: %1%nError: %2%n%3\r\n
0xb000201c | Fail to open dedup setting registry key\r\n
0xb000201d | Data Deduplication failed to dedup file "%1" with file ID %2 due to oplock break%n%3\r\n
0xb000201e | Data Deduplication failed to load hotspot table from file %1 due to error %2.%n%3\r\n
0xb000201f | Data Deduplication failed to initialize oplock.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb0002020 | Data Deduplication while running job on volume %1 detected invalid physical sector size %2. Using default value %3.%n%4\r\n
0xb0002021 | Data Deduplication detected an unsupported chunk store container.%n%1\r\n
0xb0002022 | Data Deduplication could not create window to receive task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002023 | Data Deduplication could not create thread to poll for task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002024 | An attempt was made to perform an initialization operation when initialization has already been completed.%n%1\r\n
0xb0002028 | Data Deduplication created emergency file %1.%n%3\r\n
0xb0002029 | Data Deduplication failed to create emergency file %1 with error %2.%n%3\r\n
0xb000202a | Data Deduplication deleted emergency file %1.%n%3\r\n
0xb000202b | Data Deduplication failed to delete emergency file %1 with error %2.%n%3\r\n
0xb000202c | Data Deduplication detected a chunk store container with misaligned valid data length.%n%1\r\n
0xb000202d | Data Deduplication Garbage Collection encountered a delete log entry with an invalid stream map signature for stream map Id %1.%n%2\r\n
0xb000202e | Data Deduplication failed to initialize oplock as the file appears to be missing.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb000202f | Data Deduplication skipped too many file-level errors. We will not log more than %1 file-level errors per job.%n%2\r\n
0xb0002030 | Data Deduplication diagnostic warning.%n%n%1%n%2\r\n
0xb0002031 | Data Deduplication diagnostic information.%n%n%1%n%2\r\n
0xb0002032 | Data Deduplication found file %1 with a stream map id %2 in container file %3 marked for deletion.%n%4\r\n
0xb0002033 | Failed to enqueue job of type "%1" on volume "%2".%n%3\r\n
0xb0002034 | Error terminating job host process for job type "%1" on volume "%2" (process id: %3).%n%4\r\n
0xb0002035 | Data Deduplication encountered corrupted chunk %1 while updating container. Corrupted data that cannot be repaired will be copied as-is to the new container %2.%n%3\r\n
0xb0002036 | Data Deduplication job type "%1" on volume "%2" failed to exit gracefully.%n%3\r\n
0xb0002037 | Data Deduplication job host for job type "%1" on volume "%2" exited unexpectedly.%n%3\r\n
0xb0002038 | Data Deduplication has failed to load corruption metadata file on the store at %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb0002039 | Data Deduplication full garbage collection phase 1 on volume "%1" encountered an error %2 while processing file %3. Phase 1 will need to be aborted since garbage collection of file-related metadata is unsafe to continue on file errors.%n%4\r\n
0xb000203a | Data Deduplication has failed to process corruption metadata file %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb000203b | Data Deduplication has failed to load a corrupted metadata file %1 due to error %2. Deleting the file and continuing.%n%3\r\n
0xb000203c | Data Deduplication has failed to set NTFS allocation size for container file %1 due to error %2.%n%3\r\n
0xb000203d | Data Deduplication configured to use BCrypt provider '%1' for hash algorithm %2.%n%3\r\n
0xb000203e | Data Deduplication could not use BCrypt provider '%1' for hash algorithm %2 due to an error in operation %3. Reverting to the Microsoft primitive CNG provider.%n%4\r\n
0xb000203f | Data Deduplication failed to include file "%1" in file metadata analysis calculations.%n%2\r\n
0xb0002040 | Data Deduplication failed to include stream map %1 in file metadata analysis calculations.%n%2\r\n
0xb0002041 | Data Deduplication encountered an error for file "%1" while scanning files and folders.%n%2\r\n
0xb0002042 | Data Deduplication encountered an error while attempting to resume processing. Please consult the event log parameters for more details about the current file being processed.%n%1\r\n
0xb0002043 | Data Deduplication encountered an error %1 whle scanning usn journal on volume %2 for updating hot range tracking.%n%3\r\n
0xb0002044 | Data Deduplication could not truncate the stream of an optimized file. No action is required. Error: %1%n%n%2\r\n
0xb0002800 | %1 job memory requirements.%n%nVolume: %4 (%3)%nMinimum memory: %5 MB%nMaximum memory: %6 MB%nMinimum disk: %7 MB%nMaximum cores: %8\r\n
0xb0002801 | %1 reconciliation has started.%n%nVolume: %4 (%3)\r\n
0xb0002802 | %1 reconciliation has completed.%n%nVolume: %4 (%3)%nReconciled containers: %5%nUnreconciled containers: %6%nCatchup references: %7%nCatchup containers: %8%nReconciled references: %9%nReconciled containers: %10%nCross-reconciled references: %11%nCross-reconciled containers: %12%nError code: %13%nError message: %14\r\n
0xb0002803 | %1 job on volume %4 (%3) was configured with insufficient memory.%n%nSystem memory percentage: %5%nAvailable memory: %8 MB%nMinimum required memory: %6 MB\r\n
0xb0002804 | Optimization memory details for %1 job on volume %3 (%2).\r\n
0xb0002805 | An open file was skipped during optimization. No action is required.%n%nFileId: %2%nSkip Reason: %1\r\n
0xb0002806 | An operation succeeded after one or more retries. Operation: %1; FileId: %3; Number of retries: %2\r\n
0xb0002807 | Data Deduplication aborted the optimization pipeline.%nVolumePath: %1%nErrorCode: %2%nErrorMessage: %3Details: %4\r\n
0xb0002808 | Data Deduplication aborted a file.%nFileId: %1%nFilePath: %2%nFileSize: %3%nFlags: %4%nTotalRanges: %5%nSkippedRanges: %6%nAbortedRanges: %7%nCommittedRanges: %8%nErrorCode: %9%nErrorMessage: %10Details: %11\r\n
0xb0002809 | Data Deduplication aborted a file range.%nFileId: %1%nFilePath: %2%nRangeOffset: %3%nRangeLength: %4%nErrorCode: %5%nErrorMessage: %6Details: %7\r\n
0xb000280a | Data Deduplication aborted a session.%nMaxSize: %1%nCurrentSize: %2%nRemainingRanges: %3%nErrorCode: %4%nErrorMessage: %5Details: %6\r\n
0xb000280b | USN journal created.%n%nVolume: %2 (%1)%nMaximum size %3 MB%nAllocation size %4 MB\r\n
0xb0003200 | Data Deduplication service detected corruption in "%5%6%7". The corruption cannot be repaired.\r\n
0xb0003201 | Data Deduplication service detected corruption (%7) in "%6". See the event details for more information.\r\n
0xb0003202 | Data Deduplication service detected a corrupted item (%11 - %13, %8, %9, %10, %12) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003203 | Data Deduplication service has finished scrubbing on volume %3. It did not find any corruption since the last scrubbing.\r\n
0xb0003204 | Data Deduplication service found %4 corruption(s) on volume %3. All corruptions are fixed.\r\n
0xb0003205 | Data Deduplication service found %4 corruption(s) on volume %3. %5 corruption(s) are fixed. %6 user file(s) are corrupted. %7 user file(s) are fixed. For the corrupted file list, see the Microsoft/Windows/Deduplication/Scrubbing events.\r\n
0xb0003206 | Data Deduplication service found too many corruptions on volume %3. Some corruptions are not reported.\r\n
0xb0003211 | Data Deduplication service has finished scrubbing on volume %3. See the event details for more information.\r\n
0xb0003212 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003213 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003214 | Data Deduplication service encountered error while detecting corruptions in chunk store on volume %3. The error was %4. The job is aborted.\r\n
0xb0003216 | Data Deduplication service encountered error while loading corruption logs on volume %3. The error was %4. The job continues. Some corruptions may not be detected.\r\n
0xb0003217 | Data Deduplication service encountered error while cleaning up corruption logs on volume %3. The error was %4. Some corruptions may be reported again next time.\r\n
0xb0003218 | Data Deduplication service encountered error while loading hotspots mapping from chunk store on volume %3. The error was %4. Some corruptions may not be repaired.\r\n
0xb0003219 | Data Deduplication service encountered error while determining corrupted user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb000321a | Data Deduplication service found %4 corruption(s) on volume %3. %6 user file(s) are corrupted. %7 user file(s) are fixable. Please run scrubbing job in read-write mode to attempt fixing reported corruptions.\r\n
0xb000321b | Data Deduplication service fixed corruption in "%5%6%7".\r\n
0xb000321c | Data Deduplication service detected fixable corruption in "%5%6%7". Please run scrubbing job in read-write mode to fix this corruption.\r\n
0xb000321e | Data Deduplication service encountered error while repairing corruptions on volume %3. The error was %4. The repair is unsuccessful.\r\n
0xb000321f | Data Deduplication service detected a corrupted item (%6, %7, %8, %9) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003220 | Container (%8,%9) with user data is missing from the chunk store. Missing container may result from incomplete restore, incomplete migration or file-system corruption. Volume is disabled from further optimization. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0003221 | Data Deduplication service encountered error while scaning dedup user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb0003222 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003223 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003224 | Data Deduplication service detected potential data loss (%9) in "%6" due to sharing reparse data with file "%8". See the event details for more information.\r\n
0xb0003225 | Container (%8,%9) with user data is corrupt in the chunk store. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0005000 | Open stream store stream (StartingChunkId %1, FileId %2)\r\n
0xb0005001 | Open stream store stream completed %1\r\n
0xb0005002 | Prepare for paging IO (Stream %1, FileId %2)\r\n
0xb0005003 | Prepare for paging IO completed %1\r\n
0xb0005005 | Read stream map completed %1\r\n
0xb0005006 | Read chunks (Stream %1, FileId %2, IoType %3, FirstRequestChunkId %4, NextRequest %5)\r\n
0xb0005007 | Read chunks completed %1\r\n
0xb0005008 | Compute checksum (ItemType %1, DataSize %2)\r\n
0xb0005009 | Compute checksum completed %1\r\n
0xb000500a | Get container entry (ContainerId %1, Generation %2)\r\n
0xb000500b | Get container entry completed %1\r\n
0xb000500c | Get maximum generation for container (ContainerId %1, Generation %2)\r\n
0xb000500d | Get maximum generation for container completed %1\r\n
0xb000500e | Open chunk container (ContainerId %1, Generation %2, RootPath %4)\r\n
0xb000500f | Open chunk container completed %1\r\n
0xb0005010 | Initialize chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005011 | Initialize chunk container redirection table completed %1\r\n
0xb0005012 | Validate chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005013 | Validate chunk container redirection table completed %1\r\n
0xb0005014 | Get chunk container valid data length (ContainerId %1, Generation %2)\r\n
0xb0005015 | Get chunk container valid data length completed %1\r\n
0xb0005016 | Get offset from chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005017 | Get offset from chunk container redirection table completed %1\r\n
0xb0005018 | Read chunk container block (ContainerId %1, Generation %2, Buffer %3, Offset %4, Length %5, IoType %6, Synchronous %7)\r\n
0xb0005019 | Read chunk container block completed %1\r\n
0xb000501a | Clear chunk container block (Buffer %1, Size %2, BufferType %3)\r\n
0xb000501b | Clear chunk container block completed %1\r\n
0xb000501c | Copy chunk (Buffer %1, Size %2, BufferType %3, BufferOffset %4, OutputCapacity %5)\r\n
0xb000501d | Copy chunk completed %1\r\n
0xb000501e | Initialize file cache (UnderlyingFileObject %1, CacheFileSize %2)\r\n
0xb000501f | Initialize file cache completed %1\r\n
0xb0005020 | Map file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005021 | Map file cache data completed %1\r\n
0xb0005022 | Unpin file cache data(Bcb %1)\r\n
0xb0005023 | Unpin file cache data completed %1\r\n
0xb0005024 | Copy file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005025 | Copy file cache data completed %1\r\n
0xb0005026 | Read underlying file cache data (CacheFileObject %1, UnderlyingFileObject %2, Offset %3, Length %4)\r\n
0xb0005027 | Read underlying file cache data completed %1\r\n
0xb0005028 | Get chunk container file size (ContainerId %1, Generation %2)\r\n
0xb0005029 | Get chunk container file size completed %1\r\n
0xb000502a | Pin stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb000502b | Pin stream map completed %1\r\n
0xb000502c | Pin chunk container (ContainerId %1, Generation %2)\r\n
0xb000502d | Pin chunk container completed %1\r\n
0xb000502e | Pin chunk (ContainerId %1, Generation %2)\r\n
0xb000502f | Pin chunk completed %1\r\n
0xb0005030 | Allocate pool buffer (ReadLength %1, PagingIo %2)\r\n
0xb0005031 | Allocate pool buffer completed %1\r\n
0xb0005032 | Unpin chunk container (ContainerId %1, Generation %2)\r\n
0xb0005033 | Unpin chunk container completed %1\r\n
0xb0005034 | Unpin chunk (ContainerId %1, Generation %2)\r\n
0xb0005035 | Unpin chunk completed %1\r\n
0xb0006028 | Dedup read processing (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006029 | Dedup read processing completed %1\r\n
0xb000602a | Get first stream map entry (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602b | Get first stream map entry completed %1\r\n
0xb000602c | Read chunk metadata (Stream %1, CurrentOffset %2, AdjustedFinalOffset %3, FirstChunkByteOffset %4, ChunkRequestsEndOffset %5, TlCache %6)\r\n
0xb000602d | Read chunk metadata completed %1\r\n
0xb000602e | Read chunk data (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602f | Read chunk data completed %1\r\n
0xb0006030 | Reference TlCache data (TlCache %1, Stream %2)\r\n
0xb0006031 | Reference TlCache data completed %1\r\n
0xb0006032 | Read chunk data from stream store (Stream %1)\r\n
0xb0006033 | Read chunk data from stream store completed %1\r\n
0xb0006034 | Assemble chunk data\r\n
0xb0006035 | Assemble chunk data completed %1\r\n
0xb0006036 | Decompress chunk data\r\n
0xb0006037 | Decompress chunk data completed %1\r\n
0xb0006038 | Copy chunk data in to user buffer (BytesCopied %1)\r\n
0xb0006039 | Copy chunk data in to user buffer completed %1\r\n
0xb000603a | Insert chunk data in to tlcache\r\n
0xb000603b | Insert chunk data in to tlcache completed %1\r\n
0xb000603c | Read data from dedup reparse point file (FileObject %1, Offset %2, Length %3)\r\n
0xb000603d | Read underlying file cache data completed %1\r\n
0xb000603e | Prepare stream map (StreamContext %1)\r\n
0xb000603f | Prepare stream map completed %1\r\n
0xb0006040 | Patch clean ranges (FileObject %1, Offset %2, Length %3)\r\n
0xb0006041 | Patch clean ranges completed %1\r\n
0xb0006042 | Writing data to dedup file (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006043 | Writing data to dedup file completed %1\r\n
0xb0006044 | Queue write request on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006045 | Queue write request on dedup file completed %1\r\n
0xb0006046 | Do copy on write work on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006047 | Do copy on write work on dedup file completed %1\r\n
0xb0006048 | Do full recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006049 | Do full recall on dedup file completed %1\r\n
0xb000604a | Do partial recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604b | Do partial recall on dedup file completed %1\r\n
0xb000604c | Do dummy paging read on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604d | Do dummy paging read on dedup file completed %1\r\n
0xb000604e | Read clean data for recalling file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604f | Read clean data for recalling file completed %1\r\n
0xb0006050 | Write clean data to dedup file normally (FileObject %1, Offset %2, Length %3)\r\n
0xb0006051 | Write clean data to dedup file completed %1\r\n
0xb0006052 | Write clean data to dedup file paged (FileObject %1, Offset %2, Length %3)\r\n
0xb0006053 | Write clean data to dedup file paged completed %1\r\n
0xb0006054 | Recall dedup file using paging Io (FileObject %1, Offset %2, Length %3)\r\n
0xb0006055 | Recall dedup file using paging Io completed %1\r\n
0xb0006056 | Flush dedup file after recall (FileObject %1)\r\n
0xb0006057 | Flush dedup file after recall completed %1\r\n
0xb0006058 | Update bitmap after recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006059 | Update bitmap after recall on dedup file completed %1\r\n
0xb000605a | Delete dedup reparse point (FileObject %1)\r\n
0xb000605b | Delete dedup reparse point completed %1\r\n
0xb000605c | Open dedup file (FilePath %1)\r\n
0xb000605d | Open dedup file completed %1\r\n
0xb000605e | Locking user buffer for read\r\n
0xb000605f | Locking user buffer for read completed %1\r\n
0xb0006060 | Get system address for MDL\r\n
0xb0006061 | Get system address for MDL completed %1\r\n
0xb0006062 | Read clean dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006063 | Read clean dedup file completed %1\r\n
0xb0006064 | Get range state (Offset %1, Length %2)\r\n
0xb0006065 | Get range state completed %1\r\n
0xb0006066 | Get chunk body\r\n
0xb0006067 | Get chunk body completed %1\r\n
0xb0006068 | Release chunk\r\n
0xb0006069 | Release chunk completed %1\r\n
0xb000606a | Release decompress chunk context (BufferSize %1)\r\n
0xb000606b | Release decompress chunk context completed %1\r\n
0xb000606c | Prepare decompress chunk context (BufferSize %1)\r\n
0xb000606d | Prepare decompress chunk context completed %1\r\n
0xb000606e | Copy data to compressed buffer (BufferSize %1)\r\n
0xb000606f | Copy data to compressed buffer completed %1\r\n
0xb0006070 | Release data from TL Cache\r\n
0xb0006071 | Release data from TL Cache completed %1\r\n
0xb0006072 | Queue async read request (FileObject %1, Offset %2, Length %3)\r\n
0xb0006073 | Queue async read request complete %1\r\n
0xb0015004 | Read stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb1004000 | Create chunk container (%1 - %2.%3.ccc)\r\n
0xb1004001 | Create chunk container completed %1\r\n
0xb1004002 | Copy chunk container (%1 - %2.%3.ccc)\r\n
0xb1004003 | Copy chunk container completed %1\r\n
0xb1004004 | Delete chunk container (%1 - %2.%3.ccc)\r\n
0xb1004005 | Delete chunk container completed %1\r\n
0xb1004006 | Rename chunk container (%1 - %2.%3.ccc%4)\r\n
0xb1004007 | Rename chunk container completed %1\r\n
0xb1004008 | Flush chunk container (%1 - %2.%3.ccc)\r\n
0xb1004009 | Flush chunk container completed %1\r\n
0xb100400a | Rollback chunk container (%1 - %2.%3.ccc)\r\n
0xb100400b | Rollback chunk container completed %1\r\n
0xb100400c | Mark chunk container (%1 - %2.%3.ccc) read-only\r\n
0xb100400d | Mark chunk container read-only completed %1\r\n
0xb100400e | Write chunk container (%1 - %2.%3.ccc) redirection table at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb100400f | Write chunk container redirection table completed %1\r\n
0xb1004011 | Write chunk container header completed %1\r\n
0xb1004013 | Insert data chunk header completed %1\r\n
0xb1004015 | Insert data chunk body completed %1 with ChunkId %2\r\n
0xb1004019 | Write delete log header completed %1\r\n
0xb100401b | Append delete log entries completed %1\r\n
0xb100401d | Delete delete log completed %1\r\n
0xb100401f | Rename delete log completed %1\r\n
0xb1004021 | Write chunk container bitmap completed %1\r\n
0xb1004023 | Delete chunk container bitmap completed %1\r\n
0xb1004024 | Write merge log (%5 - %6.%7.merge.log) header\r\n
0xb1004025 | Write merge log header completed %1\r\n
0xb1004027 | Insert hotspot chunk header completed %1\r\n
0xb1004029 | Insert hotspot chunk body completed %1 with ChunkId %2\r\n
0xb100402b | Insert stream map chunk header completed %1\r\n
0xb100402d | Insert stream map chunk body completed %1 with ChunkId %2\r\n
0xb100402f | Append merge log entries completed %1\r\n
0xb1004030 | Delete merge log (%1 - %2.%3.merge.log)\r\n
0xb1004031 | Delete merge log completed %1\r\n
0xb1004032 | Flush merge log (%1 - %2.%3.merge.log)\r\n
0xb1004033 | Flush merge log completed %1\r\n
0xb1004034 | Update file list entries (Remove: %1, Add: %2)\r\n
0xb1004035 | Update file list entries completed %1\r\n
0xb1004036 | Set dedup reparse point on %2 (FileId %1) (ReparsePoint: SizeBackedByChunkStore %3, StreamMapInfoSize %4, StreamMapInfo %5)\r\n
0xb1004037 | Set dedup reparse point completed %1 (%2)\r\n
0xb1004038 | Set dedup zero data on %2 (FileId %1)\r\n
0xb1004039 | Set dedup zero data completed %1\r\n
0xb100403a | Flush reparse point files\r\n
0xb100403b | Flush reparse point files completed %1\r\n
0xb100403c | Set sparse on file id %1\r\n
0xb100403d | Set sparse completed %1\r\n
0xb100403e | FSCTL_SET_ZERO_DATA on file id %1 at offset %2 and BeyondFinalZero %3\r\n
0xb100403f | FSCTL_SET_ZERO_DATA completed %1\r\n
0xb1004040 | Rename chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1004041 | Rename chunk container bitmap completed %1\r\n
0xb1004042 | Insert padding chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1004043 | Insert padding chunk header completed %1\r\n
0xb1004044 | Insert padding chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1004045 | Insert padding chunk body completed %1 with ChunkId %2\r\n
0xb1004046 | Insert batch of chunks to chunk container (%1 - %2.%3.ccc) at offset %4 (BatchChunkCount %5, BatchDataSize %6)\r\n
0xb1004047 | Insert batch of chunks completed %1\r\n
0xb1004049 | Write chunk container directory completed %1\r\n
0xb100404b | Delete chunk container directory completed %1\r\n
0xb100404c | Rename chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb100404d | Rename chunk container directory completed %1\r\n
0xb1014010 | Write chunk container (%5 - %6.%7.ccc) header at offset %8 (Header: USN %9, VDL %10, #Chunk %11, NextLocalId %12, Flags %13, LastAppendTime %14, BackupRedirectionTableOfset %15, LastReconciliationLocalId %16)\r\n
0xb1014012 | Insert data chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1014014 | Insert data chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014018 | Write delete log (%5 - %6.%7.delete.log) header\r\n
0xb101401a | Append delete log (%1 - %2.%3.delete.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb101401c | Delete delete log (%1 - %2.%3.delete.log)\r\n
0xb101401e | Rename delete log (%1 - %2.%3.delete.log)\r\n
0xb1014020 | Write chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4) (Bitmap: BitLength %5, StartIndex %6, Count %7)\r\n
0xb1014022 | Delete chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1014026 | Insert hotspot chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014028 | Insert hotspot chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb101402a | Insert stream map chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014048 | Write chunk container directory (%1 - %2) for chunk container (%1 - %3.%4) (Directory: EntryCount %5)\r\n
0xb101404a | Delete chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb102402e | Append merge log (%1 - %2.%3.merge.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb103402c | Insert stream map chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7) (Entries: StartIndex %8, Count %9)\r\n
0xd0000001 | Chunk header\r\n
0xd0000002 | Chunk body\r\n
0xd0000003 | Container header\r\n
0xd0000004 | Container redirection table\r\n
0xd0000005 | Hotspot table\r\n
0xd0000006 | Delete log header\r\n
0xd0000007 | Delete log entry\r\n
0xd0000008 | GC bitmap header\r\n
0xd0000009 | GC bitmap entry\r\n
0xd000000a | Merge log header\r\n
0xd000000b | Merge log entry\r\n
0xd000000c | Data\r\n
0xd000000d | Stream map\r\n
0xd000000e | Hotspot\r\n
0xd000000f | Optimization\r\n
0xd0000010 | Garbage Collection\r\n
0xd0000011 | Scrubbing\r\n
0xd0000012 | Unoptimization\r\n
0xd0000013 | Analysis\r\n
0xd0000014 | Low\r\n
0xd0000015 | Normal\r\n
0xd0000016 | High\r\n
0xd0000017 | Cache\r\n
0xd0000018 | Non-cache\r\n
0xd0000019 | Paging\r\n
0xd000001a | Memory map\r\n
0xd000001b | Paging memory map\r\n
0xd000001c | None\r\n
0xd000001d | Pool\r\n
0xd000001e | PoolAligned\r\n
0xd000001f | MDL\r\n
0xd0000020 | Map\r\n
0xd0000021 | Cached\r\n
0xd0000022 | NonCached\r\n
0xd0000023 | Paged\r\n
0xd0000024 | container file\r\n
0xd0000025 | file list file\r\n
0xd0000026 | file list header\r\n
0xd0000027 | file list entry\r\n
0xd0000028 | primary file list file\r\n
0xd0000029 | backup file list file\r\n
0xd000002a | Scheduled\r\n
0xd000002b | Manual\r\n
0xd000002c | recall bitmap header\r\n
0xd000002d | recall bitmap body\r\n
0xd000002e | recall bitmap missing\r\n
0xd000002f | Recall bitmap\r\n
0xd0000030 | Unknown\r\n
0xd0000031 | The pipeline handle was closed\r\n
0xd0000032 | The file was deleted\r\n
0xd0000033 | The file was overwritten\r\n
0xd0000034 | The file was recalled\r\n
0xd0000035 | A transaction was started on the file\r\n
0xd0000036 | The file was encrypted\r\n
0xd0000037 | The file was compressed\r\n
0xd0000038 | Set Zero Data was called on the file\r\n
0xd0000039 | Extended Attributes were set on the file\r\n
0xd000003a | A section was created on the file\r\n
0xd000003b | The file was shrunk\r\n
0xd000003c | A long-running IO operation prevented optimization\r\n
0xd000003d | An IO operation failed\r\n
0xd000003e | Notifying Optimization\r\n
0xd000003f | Setting the Reparse Point\r\n
0xd0000040 | Truncating the file\r\n
0xd1000001 | None\r\n
0xd1000002 | LZNT1\r\n
0xd1000003 | Xpress\r\n
0xd1000004 | Xpreff Huff\r\n
0xd1000005 | None\r\n
0xd1000006 | Standard\r\n
0xd1000007 | Max\r\n
0xd1000008 | Hybrid\r\n
0xf0000001 | None\r\n
0xf0000002 | Bad checksum\r\n
0xf0000003 | Inconsistent metadata\r\n
0xf0000004 | Invalid header metadata\r\n
0xf0000005 | Missing file\r\n
0xf0000006 | Bad checksum (storage subsystem)\r\n
0xf0000007 | Corruption (storage subsystem)\r\n
0xf0000008 | Corruption (missing metadata)\r\n
0xf0000009 | Possible data loss (duplicate reparse data)\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x00565301 | Reconciliation of chunk store is due.\r\n
0x00565302 | There are no actions associated with this job.\r\n
0x00565303 | Data deduplication cannot runing this job on this Csv volume on this node.\r\n
0x00565304 | Data deduplication cannot runing this cmdlet on this Csv volume on this node.\r\n
0x10000001 | Reporting\r\n
0x10000002 | Filter\r\n
0x10000003 | Kernel mode stream store\r\n
0x10000004 | Kernel mode chunk store\r\n
0x10000005 | Kernel mode chunk container\r\n
0x10000006 | Kernel mode file cache\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Data Deduplication Optimization Task\r\n
0x70000002 | Data Deduplication Garbage Collection Task\r\n
0x70000003 | Data Deduplication Scrubbing Task\r\n
0x70000004 | Data Deduplication Unoptimization Task\r\n
0x70000005 | Open stream store stream\r\n
0x70000006 | Prepare for paging IO\r\n
0x70000007 | Read stream map\r\n
0x70000008 | Read chunks\r\n
0x70000009 | Compute checksum\r\n
0x7000000a | Get container entry\r\n
0x7000000b | Get maximum generation for container\r\n
0x7000000c | Open chunk container\r\n
0x7000000d | Initialize chunk container redirection table\r\n
0x7000000e | Validate chunk container redirection table\r\n
0x7000000f | Get chunk container valid data length\r\n
0x70000010 | Get offset from chunk container redirection table\r\n
0x70000011 | Read chunk container block\r\n
0x70000012 | Clear chunk container block\r\n
0x70000013 | Copy chunk\r\n
0x70000014 | Initialize file cache\r\n
0x70000015 | Map file cache data\r\n
0x70000016 | Unpin file cache data\r\n
0x70000017 | Copy file cache data\r\n
0x70000018 | Read underlying file cache data\r\n
0x70000019 | Get chunk container file size\r\n
0x7000001a | Pin stream map\r\n
0x7000001b | Pin chunk container\r\n
0x7000001c | Pin chunk\r\n
0x7000001d | Allocate pool buffer\r\n
0x7000001e | Unpin chunk container\r\n
0x7000001f | Unpin chunk\r\n
0x70000020 | Dedup read processing\r\n
0x70000021 | Get first stream map entry\r\n
0x70000022 | Read chunk metadata\r\n
0x70000023 | Read chunk data\r\n
0x70000024 | Reference TlCache data\r\n
0x70000025 | Read chunk data from stream store\r\n
0x70000026 | Assemble chunk data\r\n
0x70000027 | Decompress chunk data\r\n
0x70000028 | Copy chunk data in to user buffer\r\n
0x70000029 | Insert chunk data in to tlcache\r\n
0x7000002a | Read data from dedup reparse point file\r\n
0x7000002b | Prepare stream map\r\n
0x7000002c | Patch clean ranges\r\n
0x7000002d | Writing data to dedup file\r\n
0x7000002e | Queue write request on dedup file\r\n
0x7000002f | Do copy on write work on dedup file\r\n
0x70000030 | Do full recall on dedup file\r\n
0x70000031 | Do partial recall on dedup file\r\n
0x70000032 | Do dummy paging read on dedup file\r\n
0x70000033 | Read clean data for recalling file\r\n
0x70000034 | Write clean data to dedup file normally\r\n
0x70000035 | Write clean data to dedup file paged\r\n
0x70000036 | Recall dedup file using paging Io\r\n
0x70000037 | Flush dedup file after recall\r\n
0x70000038 | Update bitmap after recall on dedup file\r\n
0x70000039 | Delete dedup reparse point\r\n
0x7000003a | Open dedup file\r\n
0x7000003b | Locking user buffer for read\r\n
0x7000003c | Get system address for MDL\r\n
0x7000003d | Read clean dedup file\r\n
0x7000003e | Get range state\r\n
0x7000003f | Get chunk body\r\n
0x70000040 | Release chunk\r\n
0x70000041 | Release decompress chunk context\r\n
0x70000042 | Prepare decompress chunk context\r\n
0x70000043 | Copy data to compressed buffer\r\n
0x70000044 | Release data from TL Cache\r\n
0x70000045 | Queue async read request\r\n
0x80565301 | The requested object was not found.\r\n
0x80565302 | One (or more) of the arguments given to the task scheduler is not valid.\r\n
0x80565303 | The specified object already exists.\r\n
0x80565304 | The specified path was not found.\r\n
0x80565305 | The specified user is invalid.\r\n
0x80565306 | The specified path is invalid.\r\n
0x80565307 | The specified name is invalid.\r\n
0x80565308 | The specified property is out of range.\r\n
0x80565309 | A required filter driver is either not installed, not loaded, or not ready for service.\r\n
0x8056530a | There is insufficient disk space to perform the requested operation.\r\n
0x8056530b | The specified volume type is not supported. Deduplication is supported on fixed, write-enabled NTFS data volumes and CSV backed by NTFS data volumes.\r\n
0x8056530c | Data deduplication encountered an unexpected error. Check the Data Deduplication Operational event log for more information.\r\n
0x8056530d | The specified scan log cursor has expired.\r\n
0x8056530e | The file system might be corrupted.  Please run the CHKDSK utility.\r\n
0x8056530f | A volume shadow copy could not be created or was unexpectedly deleted.\r\n
0x80565310 | Data deduplication encountered a corrupted XML configuration file.\r\n
0x80565311 | The Data Deduplication service could not access the global configuration because the Cluster service is not running.\r\n
0x80565312 | The Data Deduplication service could not access the global configuration because it has not been installed yet.\r\n
0x80565313 | Data deduplication failed to access the volume. It may be offline.\r\n
0x80565314 | The module encountered an invalid parameter or a valid parameter with an invalid value, or an expected module parameter was not found. Check the operational event log for more information.\r\n
0x80565315 | An attempt was made to perform an initialization operation when initialization has already been completed.\r\n
0x80565316 | An attempt was made to perform an uninitialization operation when that operation has already been completed.\r\n
0x80565317 | The Data Deduplication service detected an internal folder that is not secure. To secure the folder, reinstall deduplication on the volume.\r\n
0x80565318 | Data chunking has already been initiated.\r\n
0x80565319 | An attempt was made to perform an operation from an invalid state.\r\n
0x8056531a | An attempt was made to perform an operation before initialization.\r\n
0x8056531b | Call ::PushBuffer to continue chunking or ::Drain to enumerate any partial chunks.\r\n
0x8056531c | The Data Deduplication service detected multiple chunk store folders; however, only one chunk store folder is permitted. To fix this issue, reinstall deduplication on the volume.\r\n
0x8056531d | The data is invalid.\r\n
0x8056531e | The process is in an unknown state.\r\n
0x8056531f | The process is not running.\r\n
0x80565320 | There was an error while opening the file.\r\n
0x80565321 | The job process could not start because the job was not found.\r\n
0x80565322 | The client process ID does not match the ID of the host process that was started.\r\n
0x80565323 | The specified volume is not enabled for deduplication.\r\n
0x80565324 | A zero-character chunk ID is not valid.\r\n
0x80565325 | The index is filled to capacity.\r\n
0x80565327 | Session already exists.\r\n
0x80565328 | The compression format selected is not supported.\r\n
0x80565329 | The compressed buffer is larger than the uncompressed buffer.\r\n
0x80565330 | The buffer is not large enough.\r\n
0x8056533a | Index Scratch Log Error in: Seek, Read, Write, or Create\r\n
0x8056533b | The job type is invalid.\r\n
0x8056533c | Persistence layer enumeration error.\r\n
0x8056533d | The operation was cancelled.\r\n
0x8056533e | This job will not run at the scheduled time because it requires more memory than is currently available.\r\n
0x80565341 | The job was terminated while in a cancel or pending state.\r\n
0x80565342 | The job was terminated while in a handshake pending state.\r\n
0x80565343 | The job was terminated due to a service shutdown.\r\n
0x80565344 | The job was abandoned before starting.\r\n
0x80565345 | The job process exited unexpectedly.\r\n
0x80565346 | The Data Deduplication service detected that the container cannot be compacted or updated because it has reached the maximum generation version. \r\n
0x80565347 | The corruption log has reached its maximum size.\r\n
0x80565348 | The data deduplication scrubbing job failed to process the corruption logs.\r\n
0x80565349 | Data deduplication failed to create new chunk store container files. Allocate more space to the volume.\r\n
0x80565350 | An error occurred while opening the file because the file was in use. \r\n
0x80565351 | An error was discovered while deduplicating the file. The file is now skipped.\r\n
0x80565352 | File Server Deduplication encountered corruption while enumerating chunks in a chunk store.\r\n
0x80565353 | The scan log is not valid.\r\n
0x80565354 | The data is invalid due to checksum (CRC) mismatch error.\r\n
0x80565355 | Data deduplication encountered file corruption error.\r\n
0x80565356 | Job completed with some errors. Check event logs for more details.\r\n
0x80565357 | Data deduplication is not supported on the version of the chunk store found on this volume.\r\n
0x80565358 | Data deduplication encountered an unknown version of chunk store on this volume.\r\n
0x80565359 | The job was assigned less memory than the minimum it needs to run.\r\n
0x8056535a | The data deduplication job schedule cannot be modified.\r\n
0x8056535b | The valid data length of chunk store container is misaligned.\r\n
0x8056535c | File access is denied.\r\n
0x8056535d | Data deduplication job stopped due to too many corrupted files.\r\n
0x8056535e | Data deduplication job stopped due to an internal error in the BCrypt SHA-512 provider.\r\n
0x8056535f | Data deduplication job stopped for store reconciliation.\r\n
0x80565360 | File skipped for deduplication due to its size.\r\n
0x80565361 | File skipped due to deduplication retry limit.\r\n
0x80565362 | The pipeline buffer cache is full.\r\n
0x80565363 | Another Data deduplication job already running on this volume.\r\n
0x80565364 | Data deduplication cannot run this job on this Csv volume on this node. Try running the job on the Csv volume resource owner node.\r\n
0x80565365 | Data deduplication failed to initialize cluster state on this node.\r\n
0x80565366 | Optimization of the range was aborted by the dedup filter driver.\r\n
0x80565367 | The operation could not be performed because of a concurrent IO operation.\r\n
0x80565368 | Data deduplication encountered an unexpected error. Verify deduplication is enabled on all nodes if in a cluster configuration. Check the Data Deduplication Operational event log for more information.\r\n
0x80565369 | Data access for data deduplicated CSV volumes can only be disabled when in maintenance mode. Check the Data Deduplication Operational event log for more information.\r\n
0x8056536a | Data Deduplication encountered an IO device error that may indicate a hardware fault in the storage subsystem.\r\n
0x8056536b | Data deduplication cannot run this cmdlet on this Csv volume on this node. Try running the cmdlet on the Csv volume resource owner node.\r\n
0x8056536c | Deduplication job not supported during rolling cluster upgrade.\r\n
0x8056536d | Deduplication setting not supported during rolling cluster upgrade.\r\n
0x8056536e | Data port job is not ready to accept requests.\r\n
0x8056536f | Data port request not accepted due to request count/size limit exceeded.\r\n
0x80565370 | Data port request completed with some errors. Check event logs for more details.\r\n
0x80565371 | Data port request failed. Check event logs for more details.\r\n
0x80565372 | Data port error accessing the hash index. Check event logs for more details.\r\n
0x80565373 | Data port error accessing the stream store. Check event logs for more details.\r\n
0x80565374 | Data port file stub error. Check event logs for more details.\r\n
0x80565375 | Data port encountered a deduplication filter error. Check event logs for more details.\r\n
0x80565376 | Data port cannot commit stream map due to missing chunk. Check event logs for more details.\r\n
0x80565377 | Data port cannot commit stream map due to invalid stream map metadata. Check event logs for more details.\r\n
0x80565378 | Data port cannot commit stream map due to invalid stream map entry. Check event logs for more details.\r\n
0x80565379 | Data port cannot retrieve job interface for volume. Check event logs for more details.\r\n
0x8056537a | The specified path is not supported.\r\n
0x8056537b | // Data port cannot decompress chunk. Check event logs for more details.\r\n
0x8056537c | Data port cannot calculate chunk hash. Check event logs for more details.\r\n
0x8056537d | Data port cannot read chunk stream. Check event logs for more details.\r\n
0x8056537e | The target file is not a deduplicated file. Check event logs for more details.\r\n
0x8056537f | The target file is partially recalled. Check event logs for more details.\r\n
0x90000001 | Data Deduplication\r\n
0x90000002 | Application\r\n
0x91000001 | Data Deduplication Change Events\r\n
0xb0001000 | Volume "%1" appears as disconnected and it is ignored by the service.  You may want to rescan disks.   Error: %2.%n%3\r\n
0xb0001001 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3". Most likely the CPU is under heavy load.  Error: %4.%n%5\r\n
0xb0001002 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3".  Error: %4.%n%5\r\n
0xb0001003 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3" during Safe Mode. The Data Deduplication service cannot start while in safe mode.  Error: %4.%n%5\r\n
0xb0001004 | A critical component required by Data Deduplication is not registered. This might happen if an error occurred during Windows setup, or if the computer does not have the Windows Server 2012 or later version of Deduplication service installed. The error returned from CoCreateInstance on class with CLSID %1 and Name "%2" on machine "%3" is %4.%n%5\r\n
0xb0001005 | Data Deduplication service is shutting down due to idle timeout.%n%1\r\n
0xb0001006 | Data Deduplication service is shutting down due to shutdown event from the Service Control Manager.%n%1\r\n
0xb0001007 | Data Deduplication job of type "%1" on volume "%2" has completed with return code: %3%n%4\r\n
0xb0001008 | Data Deduplication error: Unexpected error calling routine %1.  hr = %2.%n%3\r\n
0xb0001009 | Data Deduplication error: Unexpected error.%n%1\r\n
0xb000100a | Data Deduplication warning: %1%nError: %2.%n%3\r\n
0xb000100b | Data Deduplication error: Unexpected COM error %1: %2.  Error code: %3.%n%4\r\n
0xb000100c | Data Deduplication was unable to access the following file or volume: "%1".  This file or volume might be locked by another application right now, or you might need to give Local System access to it.%n%2\r\n
0xb000100d | Data Deduplication encountered an unexpected error during volume scan of volumes mounted at "%1" ("%2"). To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100e | Data Deduplication was unable to create or access the shadow copy for volumes mounted at "%1" ("%2"). Possible causes include an improper Shadow Copy configuration, insufficient disk space, or extreme memory, I/O or CPU load of the system. To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100f | Data Deduplication was unable to access volumes mounted at "%1" ("%2"). Make sure that dismount or format operations do not happen while running deduplication.%n%3\r\n
0xb0001010 | Data Deduplication was unable to access a file or volume. Details:%n%n%1%n The volume may be inaccessible for I/O operations or marked read-only. In case of a cluster volume, this may be a transient failure during failover.%n%2\r\n
0xb0001011 | Data Deduplication was unable to scan volume "%1" ("%2").%n%3\r\n
0xb0001012 | Data Deduplication detected a corruption on file "%1" at offset ("%2").  If this condition persists then please restore the data from a previous backup.  Corruption details: Structure=%3, Corruption type = %4, Additional data = %5%n%6\r\n
0xb0001013 | Data Deduplication encountered failure while reconciling chunk store on volume "%1". The error code was %2. Reconciliation is disabled for the current optimization job.%n%3\r\n
0xb0001016 | Data Deduplication encountered corrupted chunk container %1 while performing full garbage collection. The corrupted chunk container is skipped.%n%2\r\n
0xb0001017 | Data Deduplication could not initialize change log under %1. The error code was %2.%n%3\r\n
0xb0001018 | Data Deduplication service could not mark chunk container %1 as reconciled. The error code was %2.%n%3\r\n
0xb0001019 | A Data Deduplication configuration file is corrupted. The system or volume may need to be restored from backup.%n%1\r\n
0xb000101a | Data Deduplication was unable to save one of the configuration stores on volume "%1" due to a disk-full error: If the disk is full, please clean it up (extend the volume or delete some files). If the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.%n%2\r\n
0xb000101b | Data Deduplication could not access global configuration since the cluster service is not running. Please start the cluster service and retry the operation.%n%1\r\n
0xb000101c | Shadow copy "%1" was deleted during storage report generation.  Volume "%2" might be configured with inadequate shadow copy storage area. Data Deduplication could not process this volume.%n%3\r\n
0xb000101d | Shadow copy creation failed for volume "%1" after retrying for %2 minutes because other shadow copies were being created.  Reschedule the Data Deduplication for a less busy time.%n%3\r\n
0xb000101e | Volume "%1" is not supported for shadow copy.  It is possible that the volume was removed from the system.  Data Deduplication service could not process this volume.%n%2\r\n
0xb000101f | The volume "%1" has been deleted or removed from the system.%n%2\r\n
0xb0001020 | Shadow copy creation failed for volume "%1" with error %2.  The volume might be configured with inadequate shadow copy storage area.  File Serve Deduplication service could not process this volume.%n%3\r\n
0xb0001021 | The file system on volume "%1" is potentially corrupted.  Please run the CHKDSK utility to verify and fix the file system.%n%2\r\n
0xb0001022 | Data Deduplication detected an insecure internal folder. To secure the folder, reinstall deduplication on the volume again.%n%1\r\n
0xb0001023 | Data Deduplication could not find a chunk store on the volume.%n%1\r\n
0xb0001024 | Data Deduplication detected multiple chunk store folders. To recover, reinstall deduplication on the volume.%n%1\r\n
0xb0001025 | Data Deduplication detected conflicting chunk store folders: "%1" and "%2".%n%3\r\n
0xb0001026 | The data is invalid.%n%1\r\n
0xb0001027 | Data Deduplication scheduler failed to initialize with error "%1".%n%2\r\n
0xb0001028 | Data Deduplication failed to validate job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb0001029 | Data Deduplication failed to start job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb000102c | Data Deduplication detected job type "%1" on volume "%2" uses too much memory. %3 MB is assigned. %4 MB is used.%n%5\r\n
0xb000102d | Data Deduplication detected job type "%1" on volume "%2" memory usage has dropped to desirable level.%n%3\r\n
0xb000102e | Data Deduplication cancelled job type "%1" on volume "%2". It uses too much memory than the amount assigned to it.%n%3\r\n
0xb000102f | Data Deduplication cancelled job type "%1" on volume "%2". Memory resource is running low on the machine or in the job.%n%3\r\n
0xb0001030 | Data Deduplication job type "%1" on volume "%2" failed to report completion to the service with error: %3.%n%4\r\n
0xb0001031 | Data Deduplication detected a container cannot be compacted or updated because it has reached the maximum generation.%n%1\r\n
0xb0001032 | Data Deduplication corruption log "%1" is corrupted.%n%2\r\n
0xb0001033 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". Please run scrubbing job to process corruption log. No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001034 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001035 | Data Deduplication scheduler failed to uninitialize with error "%1".%n%2\r\n
0xb0001036 | Data Deduplication detected a new container could not be created in a chunk store because it ran out of available container Id.%n%1\r\n
0xb0001037 | Data Deduplication full garbage collection phase 1 (cleaning file related metadata) on volume "%1" failed with error: %2.  The job will continue with phase 2 execution (data chunk cleanup).%n%3\r\n
0xb0001039 | Data Deduplication full garbage collection could not achieve maximum space reclamation because delete logs for data container %1 could not be cleaned up.%n%2\r\n
0xb000103a | Some files could not be deduplicated because of FSRM Quota violations on volume %1. Files skipped are likely compressed or sparse files in folders which are at quota or close to their quota limit. Please consider increasing the quota limit for folders that are at their quota limit or close to it.%n%2\r\n
0xb000103b | Data Deduplication failed to dedup file %1 "%2" due to fatal error %3%n%4\r\n
0xb000103c | Data Deduplication encountered corruption while accessing a file in chunk store.%n%1\r\n
0xb000103d | Data Deduplication encountered corruption while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103e | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103f | Data Deduplication is unable to access file %1 because the file is in use.%n%2\r\n
0xb0001040 | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store.%n%1\r\n
0xb0001041 | Data Deduplication cannot run the job on volume %1 because the dedup store version compatiblity check failed with error %2.%n%3\r\n
0xb0001042 | Data Deduplication has disabled the volume %1 because it has discovered too many corruptions. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001043 | Data Deduplication has detected a corrupt corruption metadata file on the store at %1. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001044 | Volume "%1" cannot be enabled for Data Deduplication. Data Deduplication does not support volumes larger than 64TB. Error: %2.%n%3\r\n
0xb0001045 | Data Deduplication cannot be enabled on SIS volume "%1". Error: %2.%n%3\r\n
0xb0001046 | File-system is configured for case-sensitive file/folder names. Data Deduplication does not support case-sensitive file-system mode.%n%1\r\n
0xb0001049 | Data Deduplication changed scrubbing job to read-only due to insufficient disk space.%n%1\r\n
0xb000104b | Data Deduplication has disabled the volume %1 because there are missing or corrupt containers. Please run deep scrubbing on the volume.%n%2\r\n
0xb000104d | Data Deduplication encountered a disk-full error.%n%1\r\n
0xb000104e | Data Deduplication job cannot run on volume "%1" due to insufficient disk space.%n%2\r\n
0xb000104f | Data Deduplication job cannot run on offline volume "%1".%n%2\r\n
0xb0001050 | Data Deduplication recovered a corrupt or missing file.%n%1\r\n
0xb0001051 | Data Deduplication encountered a corrupted metadata file. To correct the problem, schedule or manually run a Garbage Collection job on the affected volume with the -Full option.%n%1\r\n
0xb0001052 | Data Deduplication encountered chunk %1 with corrupted header while updating container. The corrupted chunk is replicated to the new container %2.%n%3\r\n
0xb0001053 | Data Deduplication encountered chunk %1 with transient header corruption while updating container. The corrupted chunk is NOT replicated to the new container %2.%n%3\r\n
0xb0001054 | Data Deduplication failed to read chunk container redirection table from file %1 with error %2.%n%3\r\n
0xb0001055 | Data Deduplication failed to initialize reparse point index table for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001056 | Data Deduplication failed to deep scrub container file %1 on volume %2 with error %3.%n%4\r\n
0xb0001057 | Data Deduplication failed to load stream map log for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001058 | Data Deduplication found a duplicate local chunk id %1 in container file %2.%n%3\r\n
0xb0001059 | Data Deduplication job type "%1" on volume "%2" was cancelled manually.%n%3\r\n
0xb000105a | Scheduled data Deduplication job type "%1" on volume "%2" was cancelled.%n%3\r\n
0xb000105d | The Data Deduplication chunk store statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105e | The Data Deduplication volume statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105f | Data Deduplication failed to append to deep scrubbing log file %1 with error %2.%n%3\r\n
0xb0001060 | Data Deduplication encountered a failure during deep scrubbing on store %1 with error %2.%n%3\r\n
0xb0001061 | Data Deduplication cancelled job type "%1" on volume "%2". The job violated Csv dedup job placement policy.%n%3\r\n
0xb0001062 | Data Deduplication cancelled job type "%1" on volume "%2". The csv job monitor has been uninitialized.%n%3\r\n
0xb0001063 | Data Deduplication encountered a IO device error while accessing a file on the volume. This is likely a hardware fault in the storage subsystem.%n%1\r\n
0xb0001064 | Data Deduplication encountered an unexpected error. If this is a cluster, verify Data Deduplication is enabled on all nodes of the cluster.%n%1\r\n
0xb0001065 | Attempted to disable data access for data deduplicated CSV volume "%1" without maintenance mode. Data access can only be disabled for a CSV volume when in maintenance mode. Place volume into maintenance mode and retry.%n%2\r\n
0xb0001800 | Data Deduplication service could not unoptimize file "%5%6%7". Error %8, "%9".\r\n
0xb0001801 | Data Deduplication service failed to unoptimize too many files %3. Some files are not reported.\r\n
0xb0001802 | Data Deduplication service has finished unoptimization on volume %3 with no errors.\r\n
0xb0001803 | Data Deduplication service has finished unoptimization on volume %3 with %4 errors.\r\n
0xb0001804 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb0001805 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nPriority: %7%nFull: %8%nVolume free space (MB): %9\r\n
0xb0001806 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6%nFull: %7%nRead-only: %8\r\n
0xb0001807 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6\r\n
0xb0001809 | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate (percent): %7%nSaved space (MB): %8%nVolume used space (MB): %9%nVolume free space (MB): %10%nOptimized file count: %11%nIn-policy file count: %12%nJob processed space (MB): %13%nJob elapsed time (seconds): %18%nJob throughput (MB/second): %19%nChurn processing throughput (MB/second): %20\r\n
0xb000180a | %1 job has completed.%n%nFull: %2%nVolume: %5 (%4)%nError code: %6%nError message: %7%nFreed up space (MB): %8%nVolume free space (MB): %9%nJob elapsed time (seconds): %10%nJob throughput (MB/second): %11\r\n
0xb000180b | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6\r\n
0xb000180c | %1 job has completed.%n%nFull: %2%nRead-only: %3%nVolume: %6 (%5)%nError code: %7%nError message: %8%nTotal corruption count: %9%nFixable corruption count: %10%n%nWhen corruptions are found, check more details in Scrubbing event channel.\r\n
0xb000180d | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nUnoptimized file count: %7%nJob processed space (MB): %8%nJob elapsed time (seconds): %9%nJob throughput (MB/second): %10\r\n
0xb000180e | %1 job has been queued.%n%nVolume: %4 (%3)%nSystem memory percent: %5 %nPriority: %6%nSchedule mode: %7\r\n
0xb000181c | Restore of deduplicated file "%1" failed with the following error: %2, "%3".\r\n
0xb000181d | Priority %1 job has started.%n%nVolume: %4 (%3)%nFile ID: %11%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb000181e | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable threads: %6%nPriority: %7\r\n
0xb000181f | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate (percent): %7%nSaved space (MB): %8%nVolume used space (MB): %9%nVolume free space (MB): %10%nOptimized file count: %11%nChunk lookup count: %12%nInserted chunk count: %13%nInserted chunks logical data (MB): %14%nInserted chunks physical data (MB): %15%nCommitted stream count: %16%nCommitted stream entry count: %17%nCommitted stream logical data (MB): %18%nRetrieved chunks physical data (MB): %19%nRetrieved stream logical data (MB): %20%nDataPort time (seconds): %21%nJob elapsed time (seconds): %22%nIngress throughput (MB/second): %23%nEgress throughput (MB/second): %24\r\n
0xb0001821 | Data Deduplication detected a non-clustered volume specified for the chunk index cache volume in a clustered deployment. The configuration is not recommended because it may result in job failures after failover.%n%nVolume: %3 (%2)\r\n
0xb0002000 | Data Deduplication detected job type "%1" on volume "%2" working set is low. Ratio to commit size is %3.%n%4\r\n
0xb0002001 | Data Deduplication detected job type "%1" on volume "%2" working set has recovered to desirable level.%n%3\r\n
0xb0002002 | Data Deduplication detected job type "%1" on volume "%2" page fault rate is high. The rate is %3 page faults per second.%n%4\r\n
0xb0002003 | Data Deduplication detected job type "%1" on volume "%2" page fault rate has lowered to desirable level. The rate is %3 page faults per second.%n%4\r\n
0xb0002004 | Data Deduplication failed to dedup file "%1" with file ID %2 due to non-fatal error %3%n%4.%n%nNote: You can retrieve the file name by running the command FSUTIL FILE QUERYFILENAMEBYID on the file in question.\r\n
0xb000200c | Data Deduplication has aborted a group commit session.%n%nFile count: %1%nError: %2%n%3\r\n
0xb000201c | Fail to open dedup setting registry key\r\n
0xb000201d | Data Deduplication failed to dedup file "%1" with file ID %2 due to oplock break%n%3\r\n
0xb000201e | Data Deduplication failed to load hotspot table from file %1 due to error %2.%n%3\r\n
0xb000201f | Data Deduplication failed to initialize oplock.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb0002020 | Data Deduplication while running job on volume %1 detected invalid physical sector size %2. Using default value %3.%n%4\r\n
0xb0002021 | Data Deduplication detected an unsupported chunk store container.%n%1\r\n
0xb0002022 | Data Deduplication could not create window to receive task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002023 | Data Deduplication could not create thread to poll for task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002024 | An attempt was made to perform an initialization operation when initialization has already been completed.%n%1\r\n
0xb0002028 | Data Deduplication created emergency file %1.%n%3\r\n
0xb0002029 | Data Deduplication failed to create emergency file %1 with error %2.%n%3\r\n
0xb000202a | Data Deduplication deleted emergency file %1.%n%3\r\n
0xb000202b | Data Deduplication failed to delete emergency file %1 with error %2.%n%3\r\n
0xb000202c | Data Deduplication detected a chunk store container with misaligned valid data length.%n%1\r\n
0xb000202d | Data Deduplication Garbage Collection encountered a delete log entry with an invalid stream map signature for stream map Id %1.%n%2\r\n
0xb000202e | Data Deduplication failed to initialize oplock as the file appears to be missing.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb000202f | Data Deduplication skipped too many file-level errors. We will not log more than %1 file-level errors per job.%n%2\r\n
0xb0002030 | Data Deduplication diagnostic warning.%n%n%1%n%2\r\n
0xb0002031 | Data Deduplication diagnostic information.%n%n%1%n%2\r\n
0xb0002032 | Data Deduplication found file %1 with a stream map id %2 in container file %3 marked for deletion.%n%4\r\n
0xb0002033 | Failed to enqueue job of type "%1" on volume "%2".%n%3\r\n
0xb0002034 | Error terminating job host process for job type "%1" on volume "%2" (process id: %3).%n%4\r\n
0xb0002035 | Data Deduplication encountered corrupted chunk %1 while updating container. Corrupted data that cannot be repaired will be copied as-is to the new container %2.%n%3\r\n
0xb0002036 | Data Deduplication job type "%1" on volume "%2" failed to exit gracefully.%n%3\r\n
0xb0002037 | Data Deduplication job host for job type "%1" on volume "%2" exited unexpectedly.%n%3\r\n
0xb0002038 | Data Deduplication has failed to load corruption metadata file on the store at %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb0002039 | Data Deduplication full garbage collection phase 1 on volume "%1" encountered an error %2 while processing file %3. Phase 1 will need to be aborted since garbage collection of file-related metadata is unsafe to continue on file errors.%n%4\r\n
0xb000203a | Data Deduplication has failed to process corruption metadata file %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb000203b | Data Deduplication has failed to load a corrupted metadata file %1 due to error %2. Deleting the file and continuing.%n%3\r\n
0xb000203c | Data Deduplication has failed to set NTFS allocation size for container file %1 due to error %2.%n%3\r\n
0xb000203d | Data Deduplication configured to use BCrypt provider '%1' for hash algorithm %2.%n%3\r\n
0xb000203e | Data Deduplication could not use BCrypt provider '%1' for hash algorithm %2 due to an error in operation %3. Reverting to the Microsoft primitive CNG provider.%n%4\r\n
0xb000203f | Data Deduplication failed to include file "%1" in file metadata analysis calculations.%n%2\r\n
0xb0002040 | Data Deduplication failed to include stream map %1 in file metadata analysis calculations.%n%2\r\n
0xb0002041 | Data Deduplication encountered an error for file "%1" while scanning files and folders.%n%2\r\n
0xb0002042 | Data Deduplication encountered an error while attempting to resume processing. Please consult the event log parameters for more details about the current file being processed.%n%1\r\n
0xb0002043 | Data Deduplication encountered an error %1 whle scanning usn journal on volume %2 for updating hot range tracking.%n%3\r\n
0xb0002044 | Data Deduplication could not truncate the stream of an optimized file. No action is required. Error: %1%n%n%2\r\n
0xb0002800 | %1 job memory requirements.%n%nVolume: %4 (%3)%nMinimum memory: %5 MB%nMaximum memory: %6 MB%nMinimum disk: %7 MB%nMaximum cores: %8\r\n
0xb0002801 | %1 reconciliation has started.%n%nVolume: %4 (%3)\r\n
0xb0002802 | %1 reconciliation has completed.%n%nGuidance: This event is expected when Reconciliation has completed, there is no recommended or required action. Reconciliation is an internal process that allows Optimization and DataPort jobs to run when the entire Deduplication chunk index cannot be loaded into memory. %n%nVolume: %4 (%3)%nReconciled containers: %5%nUnreconciled containers: %6%nCatchup references: %7%nCatchup containers: %8%nReconciled references: %9%nReconciled containers: %10%nCross-reconciled references: %11%nCross-reconciled containers: %12%nError code: %13%nError message: %14\r\n
0xb0002803 | %1 job on volume %4 (%3) was configured with insufficient memory.%n%nSystem memory percentage: %5%nAvailable memory: %8 MB%nMinimum required memory: %6 MB\r\n
0xb0002804 | Optimization memory details for %1 job on volume %3 (%2).\r\n
0xb0002805 | An open file was skipped during optimization. No action is required.%n%nFileId: %2%nSkip Reason: %1\r\n
0xb0002806 | An operation succeeded after one or more retries. Operation: %1; FileId: %3; Number of retries: %2\r\n
0xb0002807 | Data Deduplication aborted the optimization pipeline.%nVolumePath: %1%nErrorCode: %2%nErrorMessage: %3Details: %4\r\n
0xb0002808 | Data Deduplication aborted a file.%nFileId: %1%nFilePath: %2%nFileSize: %3%nFlags: %4%nTotalRanges: %5%nSkippedRanges: %6%nAbortedRanges: %7%nCommittedRanges: %8%nErrorCode: %9%nErrorMessage: %10Details: %11\r\n
0xb0002809 | Data Deduplication aborted a file range.%nFileId: %1%nFilePath: %2%nRangeOffset: %3%nRangeLength: %4%nErrorCode: %5%nErrorMessage: %6Details: %7\r\n
0xb000280a | Data Deduplication aborted a session.%nMaxSize: %1%nCurrentSize: %2%nRemainingRanges: %3%nErrorCode: %4%nErrorMessage: %5Details: %6\r\n
0xb000280b | USN journal created.%n%nVolume: %2 (%1)%nMaximum size %3 MB%nAllocation size %4 MB\r\n
0xb000280c | DataPort memory details for %1 job on volume %3 (%2).\r\n
0xb000280d | Data deduplication detected a file with an ID that is not supported.  Files with identifiers unpackable into 64-bits will be skipped. FileId: %1 FileName: %2\r\n
0xb000280e | Reconciliation should be run to ensure optimal savings.%n%nGuidance: This event is expected when Reconciliation is turned off for the DataPort job. Reconciliation is an internal process that allows Optimization and DataPort jobs to run when the entire Deduplication chunk index cannot be loaded into memory. When Reconciliation would require 50% or more of the memory on the system, it is recommended that you (temporarily) cease running a DataPort job against this volume, and run an Optimization job. If Reconciliation is not run through an Optimization job before Reconciliation would require more than 100% of system memory, Reconciliation will not be able to be run again (unless more memory is added). This would result in permanent decreased space efficiency on this volume.%n%nVolume: %2 (%1)%nMemory percentage required: %3\r\n
0xb000280f | Data Deduplication optimization job will not run the reconciliation step due to inadequate memory.%n%nGuidance: Deduplication savings will be suboptimal until the optimization job is provided more memory, or more more memory is added to the system.%n%nVolume: %2 (%1)%nMemory percentage required: %3\r\n
0xb0003200 | Data Deduplication service detected corruption in "%5%6%7". The corruption cannot be repaired.\r\n
0xb0003201 | Data Deduplication service detected corruption (%7) in "%6". See the event details for more information.\r\n
0xb0003202 | Data Deduplication service detected a corrupted item (%11 - %13, %8, %9, %10, %12) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003203 | Data Deduplication service has finished scrubbing on volume %3. It did not find any corruption since the last scrubbing.\r\n
0xb0003204 | Data Deduplication service found %4 corruption(s) on volume %3. All corruptions are fixed.\r\n
0xb0003205 | Data Deduplication service found %4 corruption(s) on volume %3. %5 corruption(s) are fixed. %6 user file(s) are corrupted. %7 user file(s) are fixed. For the corrupted file list, see the Microsoft/Windows/Deduplication/Scrubbing events.\r\n
0xb0003206 | Data Deduplication service found too many corruptions on volume %3. Some corruptions are not reported.\r\n
0xb0003211 | Data Deduplication service has finished scrubbing on volume %3. See the event details for more information.\r\n
0xb0003212 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003213 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003214 | Data Deduplication service encountered error while detecting corruptions in chunk store on volume %3. The error was %4. The job is aborted.\r\n
0xb0003216 | Data Deduplication service encountered error while loading corruption logs on volume %3. The error was %4. The job continues. Some corruptions may not be detected.\r\n
0xb0003217 | Data Deduplication service encountered error while cleaning up corruption logs on volume %3. The error was %4. Some corruptions may be reported again next time.\r\n
0xb0003218 | Data Deduplication service encountered error while loading hotspots mapping from chunk store on volume %3. The error was %4. Some corruptions may not be repaired.\r\n
0xb0003219 | Data Deduplication service encountered error while determining corrupted user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb000321a | Data Deduplication service found %4 corruption(s) on volume %3. %6 user file(s) are corrupted. %7 user file(s) are fixable. Please run scrubbing job in read-write mode to attempt fixing reported corruptions.\r\n
0xb000321b | Data Deduplication service fixed corruption in "%5%6%7".\r\n
0xb000321c | Data Deduplication service detected fixable corruption in "%5%6%7". Please run scrubbing job in read-write mode to fix this corruption.\r\n
0xb000321e | Data Deduplication service encountered error while repairing corruptions on volume %3. The error was %4. The repair is unsuccessful.\r\n
0xb000321f | Data Deduplication service detected a corrupted item (%6, %7, %8, %9) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003220 | Container (%8,%9) with user data is missing from the chunk store. Missing container may result from incomplete restore, incomplete migration or file-system corruption. Volume is disabled from further optimization. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0003221 | Data Deduplication service encountered error while scaning dedup user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb0003222 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003223 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003224 | Data Deduplication service detected potential data loss (%9) in "%6" due to sharing reparse data with file "%8". See the event details for more information.\r\n
0xb0003225 | Container (%8,%9) with user data is corrupt in the chunk store. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0005000 | Open stream store stream (StartingChunkId %1, FileId %2)\r\n
0xb0005001 | Open stream store stream completed %1\r\n
0xb0005002 | Prepare for paging IO (Stream %1, FileId %2)\r\n
0xb0005003 | Prepare for paging IO completed %1\r\n
0xb0005005 | Read stream map completed %1\r\n
0xb0005006 | Read chunks (Stream %1, FileId %2, IoType %3, FirstRequestChunkId %4, NextRequest %5)\r\n
0xb0005007 | Read chunks completed %1\r\n
0xb0005008 | Compute checksum (ItemType %1, DataSize %2)\r\n
0xb0005009 | Compute checksum completed %1\r\n
0xb000500a | Get container entry (ContainerId %1, Generation %2)\r\n
0xb000500b | Get container entry completed %1\r\n
0xb000500c | Get maximum generation for container (ContainerId %1, Generation %2)\r\n
0xb000500d | Get maximum generation for container completed %1\r\n
0xb000500e | Open chunk container (ContainerId %1, Generation %2, RootPath %4)\r\n
0xb000500f | Open chunk container completed %1\r\n
0xb0005010 | Initialize chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005011 | Initialize chunk container redirection table completed %1\r\n
0xb0005012 | Validate chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005013 | Validate chunk container redirection table completed %1\r\n
0xb0005014 | Get chunk container valid data length (ContainerId %1, Generation %2)\r\n
0xb0005015 | Get chunk container valid data length completed %1\r\n
0xb0005016 | Get offset from chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005017 | Get offset from chunk container redirection table completed %1\r\n
0xb0005018 | Read chunk container block (ContainerId %1, Generation %2, Buffer %3, Offset %4, Length %5, IoType %6, Synchronous %7)\r\n
0xb0005019 | Read chunk container block completed %1\r\n
0xb000501a | Clear chunk container block (Buffer %1, Size %2, BufferType %3)\r\n
0xb000501b | Clear chunk container block completed %1\r\n
0xb000501c | Copy chunk (Buffer %1, Size %2, BufferType %3, BufferOffset %4, OutputCapacity %5)\r\n
0xb000501d | Copy chunk completed %1\r\n
0xb000501e | Initialize file cache (UnderlyingFileObject %1, CacheFileSize %2)\r\n
0xb000501f | Initialize file cache completed %1\r\n
0xb0005020 | Map file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005021 | Map file cache data completed %1\r\n
0xb0005022 | Unpin file cache data(Bcb %1)\r\n
0xb0005023 | Unpin file cache data completed %1\r\n
0xb0005024 | Copy file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005025 | Copy file cache data completed %1\r\n
0xb0005026 | Read underlying file cache data (CacheFileObject %1, UnderlyingFileObject %2, Offset %3, Length %4)\r\n
0xb0005027 | Read underlying file cache data completed %1\r\n
0xb0005028 | Get chunk container file size (ContainerId %1, Generation %2)\r\n
0xb0005029 | Get chunk container file size completed %1\r\n
0xb000502a | Pin stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb000502b | Pin stream map completed %1\r\n
0xb000502c | Pin chunk container (ContainerId %1, Generation %2)\r\n
0xb000502d | Pin chunk container completed %1\r\n
0xb000502e | Pin chunk (ContainerId %1, Generation %2)\r\n
0xb000502f | Pin chunk completed %1\r\n
0xb0005030 | Allocate pool buffer (ReadLength %1, PagingIo %2)\r\n
0xb0005031 | Allocate pool buffer completed %1\r\n
0xb0005032 | Unpin chunk container (ContainerId %1, Generation %2)\r\n
0xb0005033 | Unpin chunk container completed %1\r\n
0xb0005034 | Unpin chunk (ContainerId %1, Generation %2)\r\n
0xb0005035 | Unpin chunk completed %1\r\n
0xb0006028 | Dedup read processing (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006029 | Dedup read processing completed %1\r\n
0xb000602a | Get first stream map entry (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602b | Get first stream map entry completed %1\r\n
0xb000602c | Read chunk metadata (Stream %1, CurrentOffset %2, AdjustedFinalOffset %3, FirstChunkByteOffset %4, ChunkRequestsEndOffset %5, TlCache %6)\r\n
0xb000602d | Read chunk metadata completed %1\r\n
0xb000602e | Read chunk data (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602f | Read chunk data completed %1\r\n
0xb0006030 | Reference TlCache data (TlCache %1, Stream %2)\r\n
0xb0006031 | Reference TlCache data completed %1\r\n
0xb0006032 | Read chunk data from stream store (Stream %1)\r\n
0xb0006033 | Read chunk data from stream store completed %1\r\n
0xb0006034 | Assemble chunk data\r\n
0xb0006035 | Assemble chunk data completed %1\r\n
0xb0006036 | Decompress chunk data\r\n
0xb0006037 | Decompress chunk data completed %1\r\n
0xb0006038 | Copy chunk data in to user buffer (BytesCopied %1)\r\n
0xb0006039 | Copy chunk data in to user buffer completed %1\r\n
0xb000603a | Insert chunk data in to tlcache\r\n
0xb000603b | Insert chunk data in to tlcache completed %1\r\n
0xb000603c | Read data from dedup reparse point file (FileObject %1, Offset %2, Length %3)\r\n
0xb000603d | Read underlying file cache data completed %1\r\n
0xb000603e | Prepare stream map (StreamContext %1)\r\n
0xb000603f | Prepare stream map completed %1\r\n
0xb0006040 | Patch clean ranges (FileObject %1, Offset %2, Length %3)\r\n
0xb0006041 | Patch clean ranges completed %1\r\n
0xb0006042 | Writing data to dedup file (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006043 | Writing data to dedup file completed %1\r\n
0xb0006044 | Queue write request on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006045 | Queue write request on dedup file completed %1\r\n
0xb0006046 | Do copy on write work on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006047 | Do copy on write work on dedup file completed %1\r\n
0xb0006048 | Do full recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006049 | Do full recall on dedup file completed %1\r\n
0xb000604a | Do partial recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604b | Do partial recall on dedup file completed %1\r\n
0xb000604c | Do dummy paging read on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604d | Do dummy paging read on dedup file completed %1\r\n
0xb000604e | Read clean data for recalling file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604f | Read clean data for recalling file completed %1\r\n
0xb0006050 | Write clean data to dedup file normally (FileObject %1, Offset %2, Length %3)\r\n
0xb0006051 | Write clean data to dedup file completed %1\r\n
0xb0006052 | Write clean data to dedup file paged (FileObject %1, Offset %2, Length %3)\r\n
0xb0006053 | Write clean data to dedup file paged completed %1\r\n
0xb0006054 | Recall dedup file using paging Io (FileObject %1, Offset %2, Length %3)\r\n
0xb0006055 | Recall dedup file using paging Io completed %1\r\n
0xb0006056 | Flush dedup file after recall (FileObject %1)\r\n
0xb0006057 | Flush dedup file after recall completed %1\r\n
0xb0006058 | Update bitmap after recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006059 | Update bitmap after recall on dedup file completed %1\r\n
0xb000605a | Delete dedup reparse point (FileObject %1)\r\n
0xb000605b | Delete dedup reparse point completed %1\r\n
0xb000605c | Open dedup file (FilePath %1)\r\n
0xb000605d | Open dedup file completed %1\r\n
0xb000605e | Locking user buffer for read\r\n
0xb000605f | Locking user buffer for read completed %1\r\n
0xb0006060 | Get system address for MDL\r\n
0xb0006061 | Get system address for MDL completed %1\r\n
0xb0006062 | Read clean dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006063 | Read clean dedup file completed %1\r\n
0xb0006064 | Get range state (Offset %1, Length %2)\r\n
0xb0006065 | Get range state completed %1\r\n
0xb0006066 | Get chunk body\r\n
0xb0006067 | Get chunk body completed %1\r\n
0xb0006068 | Release chunk\r\n
0xb0006069 | Release chunk completed %1\r\n
0xb000606a | Release decompress chunk context (BufferSize %1)\r\n
0xb000606b | Release decompress chunk context completed %1\r\n
0xb000606c | Prepare decompress chunk context (BufferSize %1)\r\n
0xb000606d | Prepare decompress chunk context completed %1\r\n
0xb000606e | Copy data to compressed buffer (BufferSize %1)\r\n
0xb000606f | Copy data to compressed buffer completed %1\r\n
0xb0006070 | Release data from TL Cache\r\n
0xb0006071 | Release data from TL Cache completed %1\r\n
0xb0006072 | Queue async read request (FileObject %1, Offset %2, Length %3)\r\n
0xb0006073 | Queue async read request complete %1\r\n
0xb0015004 | Read stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb1004000 | Create chunk container (%1 - %2.%3.ccc)\r\n
0xb1004001 | Create chunk container completed %1\r\n
0xb1004002 | Copy chunk container (%1 - %2.%3.ccc)\r\n
0xb1004003 | Copy chunk container completed %1\r\n
0xb1004004 | Delete chunk container (%1 - %2.%3.ccc)\r\n
0xb1004005 | Delete chunk container completed %1\r\n
0xb1004006 | Rename chunk container (%1 - %2.%3.ccc%4)\r\n
0xb1004007 | Rename chunk container completed %1\r\n
0xb1004008 | Flush chunk container (%1 - %2.%3.ccc)\r\n
0xb1004009 | Flush chunk container completed %1\r\n
0xb100400a | Rollback chunk container (%1 - %2.%3.ccc)\r\n
0xb100400b | Rollback chunk container completed %1\r\n
0xb100400c | Mark chunk container (%1 - %2.%3.ccc) read-only\r\n
0xb100400d | Mark chunk container read-only completed %1\r\n
0xb100400e | Write chunk container (%1 - %2.%3.ccc) redirection table at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb100400f | Write chunk container redirection table completed %1\r\n
0xb1004011 | Write chunk container header completed %1\r\n
0xb1004013 | Insert data chunk header completed %1\r\n
0xb1004015 | Insert data chunk body completed %1 with ChunkId %2\r\n
0xb1004019 | Write delete log header completed %1\r\n
0xb100401b | Append delete log entries completed %1\r\n
0xb100401d | Delete delete log completed %1\r\n
0xb100401f | Rename delete log completed %1\r\n
0xb1004021 | Write chunk container bitmap completed %1\r\n
0xb1004023 | Delete chunk container bitmap completed %1\r\n
0xb1004024 | Write merge log (%5 - %6.%7.merge.log) header\r\n
0xb1004025 | Write merge log header completed %1\r\n
0xb1004027 | Insert hotspot chunk header completed %1\r\n
0xb1004029 | Insert hotspot chunk body completed %1 with ChunkId %2\r\n
0xb100402b | Insert stream map chunk header completed %1\r\n
0xb100402d | Insert stream map chunk body completed %1 with ChunkId %2\r\n
0xb100402f | Append merge log entries completed %1\r\n
0xb1004030 | Delete merge log (%1 - %2.%3.merge.log)\r\n
0xb1004031 | Delete merge log completed %1\r\n
0xb1004032 | Flush merge log (%1 - %2.%3.merge.log)\r\n
0xb1004033 | Flush merge log completed %1\r\n
0xb1004034 | Update file list entries (Remove: %1, Add: %2)\r\n
0xb1004035 | Update file list entries completed %1\r\n
0xb1004036 | Set dedup reparse point on %2 (FileId %1) (ReparsePoint: SizeBackedByChunkStore %3, StreamMapInfoSize %4, StreamMapInfo %5)\r\n
0xb1004037 | Set dedup reparse point completed %1 (%2)\r\n
0xb1004038 | Set dedup zero data on %2 (FileId %1)\r\n
0xb1004039 | Set dedup zero data completed %1\r\n
0xb100403a | Flush reparse point files\r\n
0xb100403b | Flush reparse point files completed %1\r\n
0xb100403c | Set sparse on file id %1\r\n
0xb100403d | Set sparse completed %1\r\n
0xb100403e | FSCTL_SET_ZERO_DATA on file id %1 at offset %2 and BeyondFinalZero %3\r\n
0xb100403f | FSCTL_SET_ZERO_DATA completed %1\r\n
0xb1004040 | Rename chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1004041 | Rename chunk container bitmap completed %1\r\n
0xb1004042 | Insert padding chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1004043 | Insert padding chunk header completed %1\r\n
0xb1004044 | Insert padding chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1004045 | Insert padding chunk body completed %1 with ChunkId %2\r\n
0xb1004046 | Insert batch of chunks to chunk container (%1 - %2.%3.ccc) at offset %4 (BatchChunkCount %5, BatchDataSize %6)\r\n
0xb1004047 | Insert batch of chunks completed %1\r\n
0xb1004049 | Write chunk container directory completed %1\r\n
0xb100404b | Delete chunk container directory completed %1\r\n
0xb100404c | Rename chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb100404d | Rename chunk container directory completed %1\r\n
0xb1014010 | Write chunk container (%5 - %6.%7.ccc) header at offset %8 (Header: USN %9, VDL %10, #Chunk %11, NextLocalId %12, Flags %13, LastAppendTime %14, BackupRedirectionTableOfset %15, LastReconciliationLocalId %16)\r\n
0xb1014012 | Insert data chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1014014 | Insert data chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014018 | Write delete log (%5 - %6.%7.delete.log) header\r\n
0xb101401a | Append delete log (%1 - %2.%3.delete.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb101401c | Delete delete log (%1 - %2.%3.delete.log)\r\n
0xb101401e | Rename delete log (%1 - %2.%3.delete.log)\r\n
0xb1014020 | Write chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4) (Bitmap: BitLength %5, StartIndex %6, Count %7)\r\n
0xb1014022 | Delete chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1014026 | Insert hotspot chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014028 | Insert hotspot chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb101402a | Insert stream map chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014048 | Write chunk container directory (%1 - %2) for chunk container (%1 - %3.%4) (Directory: EntryCount %5)\r\n
0xb101404a | Delete chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb102402e | Append merge log (%1 - %2.%3.merge.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb103402c | Insert stream map chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7) (Entries: StartIndex %8, Count %9)\r\n
0xd0000001 | Chunk header\r\n
0xd0000002 | Chunk body\r\n
0xd0000003 | Container header\r\n
0xd0000004 | Container redirection table\r\n
0xd0000005 | Hotspot table\r\n
0xd0000006 | Delete log header\r\n
0xd0000007 | Delete log entry\r\n
0xd0000008 | GC bitmap header\r\n
0xd0000009 | GC bitmap entry\r\n
0xd000000a | Merge log header\r\n
0xd000000b | Merge log entry\r\n
0xd000000c | Data\r\n
0xd000000d | Stream map\r\n
0xd000000e | Hotspot\r\n
0xd000000f | Optimization\r\n
0xd0000010 | Garbage Collection\r\n
0xd0000011 | Scrubbing\r\n
0xd0000012 | Unoptimization\r\n
0xd0000013 | Analysis\r\n
0xd0000014 | Low\r\n
0xd0000015 | Normal\r\n
0xd0000016 | High\r\n
0xd0000017 | Cache\r\n
0xd0000018 | Non-cache\r\n
0xd0000019 | Paging\r\n
0xd000001a | Memory map\r\n
0xd000001b | Paging memory map\r\n
0xd000001c | None\r\n
0xd000001d | Pool\r\n
0xd000001e | PoolAligned\r\n
0xd000001f | MDL\r\n
0xd0000020 | Map\r\n
0xd0000021 | Cached\r\n
0xd0000022 | NonCached\r\n
0xd0000023 | Paged\r\n
0xd0000024 | container file\r\n
0xd0000025 | file list file\r\n
0xd0000026 | file list header\r\n
0xd0000027 | file list entry\r\n
0xd0000028 | primary file list file\r\n
0xd0000029 | backup file list file\r\n
0xd000002a | Scheduled\r\n
0xd000002b | Manual\r\n
0xd000002c | recall bitmap header\r\n
0xd000002d | recall bitmap body\r\n
0xd000002e | recall bitmap missing\r\n
0xd000002f | Recall bitmap\r\n
0xd0000030 | Unknown\r\n
0xd0000031 | The pipeline handle was closed\r\n
0xd0000032 | The file was deleted\r\n
0xd0000033 | The file was overwritten\r\n
0xd0000034 | The file was recalled\r\n
0xd0000035 | A transaction was started on the file\r\n
0xd0000036 | The file was encrypted\r\n
0xd0000037 | The file was compressed\r\n
0xd0000038 | Set Zero Data was called on the file\r\n
0xd0000039 | Extended Attributes were set on the file\r\n
0xd000003a | A section was created on the file\r\n
0xd000003b | The file was shrunk\r\n
0xd000003c | A long-running IO operation prevented optimization\r\n
0xd000003d | An IO operation failed\r\n
0xd000003e | Notifying Optimization\r\n
0xd000003f | Setting the Reparse Point\r\n
0xd0000040 | Truncating the file\r\n
0xd0000041 | DataPort\r\n
0xd1000001 | None\r\n
0xd1000002 | LZNT1\r\n
0xd1000003 | Xpress\r\n
0xd1000004 | Xpreff Huff\r\n
0xd1000005 | None\r\n
0xd1000006 | Standard\r\n
0xd1000007 | Max\r\n
0xd1000008 | Hybrid\r\n
0xf0000001 | None\r\n
0xf0000002 | Bad checksum\r\n
0xf0000003 | Inconsistent metadata\r\n
0xf0000004 | Invalid header metadata\r\n
0xf0000005 | Missing file\r\n
0xf0000006 | Bad checksum (storage subsystem)\r\n
0xf0000007 | Corruption (storage subsystem)\r\n
0xf0000008 | Corruption (missing metadata)\r\n
0xf0000009 | Possible data loss (duplicate reparse data)\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x00565301 | Reconciliation of chunk store is due.\r\n
0x00565302 | There are no actions associated with this job.\r\n
0x00565303 | Data deduplication cannot runing this job on this Csv volume on this node.\r\n
0x00565304 | Data deduplication cannot runing this cmdlet on this Csv volume on this node.\r\n
0x10000001 | Reporting\r\n
0x10000002 | Filter\r\n
0x10000003 | Kernel mode stream store\r\n
0x10000004 | Kernel mode chunk store\r\n
0x10000005 | Kernel mode chunk container\r\n
0x10000006 | Kernel mode file cache\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Data Deduplication Optimization Task\r\n
0x70000002 | Data Deduplication Garbage Collection Task\r\n
0x70000003 | Data Deduplication Scrubbing Task\r\n
0x70000004 | Data Deduplication Unoptimization Task\r\n
0x70000005 | Open stream store stream\r\n
0x70000006 | Prepare for paging IO\r\n
0x70000007 | Read stream map\r\n
0x70000008 | Read chunks\r\n
0x70000009 | Compute checksum\r\n
0x7000000a | Get container entry\r\n
0x7000000b | Get maximum generation for container\r\n
0x7000000c | Open chunk container\r\n
0x7000000d | Initialize chunk container redirection table\r\n
0x7000000e | Validate chunk container redirection table\r\n
0x7000000f | Get chunk container valid data length\r\n
0x70000010 | Get offset from chunk container redirection table\r\n
0x70000011 | Read chunk container block\r\n
0x70000012 | Clear chunk container block\r\n
0x70000013 | Copy chunk\r\n
0x70000014 | Initialize file cache\r\n
0x70000015 | Map file cache data\r\n
0x70000016 | Unpin file cache data\r\n
0x70000017 | Copy file cache data\r\n
0x70000018 | Read underlying file cache data\r\n
0x70000019 | Get chunk container file size\r\n
0x7000001a | Pin stream map\r\n
0x7000001b | Pin chunk container\r\n
0x7000001c | Pin chunk\r\n
0x7000001d | Allocate pool buffer\r\n
0x7000001e | Unpin chunk container\r\n
0x7000001f | Unpin chunk\r\n
0x70000020 | Dedup read processing\r\n
0x70000021 | Get first stream map entry\r\n
0x70000022 | Read chunk metadata\r\n
0x70000023 | Read chunk data\r\n
0x70000024 | Reference TlCache data\r\n
0x70000025 | Read chunk data from stream store\r\n
0x70000026 | Assemble chunk data\r\n
0x70000027 | Decompress chunk data\r\n
0x70000028 | Copy chunk data in to user buffer\r\n
0x70000029 | Insert chunk data in to tlcache\r\n
0x7000002a | Read data from dedup reparse point file\r\n
0x7000002b | Prepare stream map\r\n
0x7000002c | Patch clean ranges\r\n
0x7000002d | Writing data to dedup file\r\n
0x7000002e | Queue write request on dedup file\r\n
0x7000002f | Do copy on write work on dedup file\r\n
0x70000030 | Do full recall on dedup file\r\n
0x70000031 | Do partial recall on dedup file\r\n
0x70000032 | Do dummy paging read on dedup file\r\n
0x70000033 | Read clean data for recalling file\r\n
0x70000034 | Write clean data to dedup file normally\r\n
0x70000035 | Write clean data to dedup file paged\r\n
0x70000036 | Recall dedup file using paging Io\r\n
0x70000037 | Flush dedup file after recall\r\n
0x70000038 | Update bitmap after recall on dedup file\r\n
0x70000039 | Delete dedup reparse point\r\n
0x7000003a | Open dedup file\r\n
0x7000003b | Locking user buffer for read\r\n
0x7000003c | Get system address for MDL\r\n
0x7000003d | Read clean dedup file\r\n
0x7000003e | Get range state\r\n
0x7000003f | Get chunk body\r\n
0x70000040 | Release chunk\r\n
0x70000041 | Release decompress chunk context\r\n
0x70000042 | Prepare decompress chunk context\r\n
0x70000043 | Copy data to compressed buffer\r\n
0x70000044 | Release data from TL Cache\r\n
0x70000045 | Queue async read request\r\n
0x80565301 | The requested object was not found.\r\n
0x80565302 | One (or more) of the arguments given to the task scheduler is not valid.\r\n
0x80565303 | The specified object already exists.\r\n
0x80565304 | The specified path was not found.\r\n
0x80565305 | The specified user is invalid.\r\n
0x80565306 | The specified path is invalid.\r\n
0x80565307 | The specified name is invalid.\r\n
0x80565308 | The specified property is out of range.\r\n
0x80565309 | A required filter driver is either not installed, not loaded, or not ready for service.\r\n
0x8056530a | There is insufficient disk space to perform the requested operation.\r\n
0x8056530b | The specified volume type is not supported. Deduplication is supported on fixed, write-enabled NTFS data volumes and CSV backed by NTFS data volumes.\r\n
0x8056530c | Data deduplication encountered an unexpected error. Check the Data Deduplication Operational event log for more information.\r\n
0x8056530d | The specified scan log cursor has expired.\r\n
0x8056530e | The file system might be corrupted.  Please run the CHKDSK utility.\r\n
0x8056530f | A volume shadow copy could not be created or was unexpectedly deleted.\r\n
0x80565310 | Data deduplication encountered a corrupted XML configuration file.\r\n
0x80565311 | The Data Deduplication service could not access the global configuration because the Cluster service is not running.\r\n
0x80565312 | The Data Deduplication service could not access the global configuration because it has not been installed yet.\r\n
0x80565313 | Data deduplication failed to access the volume. It may be offline.\r\n
0x80565314 | The module encountered an invalid parameter or a valid parameter with an invalid value, or an expected module parameter was not found. Check the operational event log for more information.\r\n
0x80565315 | An attempt was made to perform an initialization operation when initialization has already been completed.\r\n
0x80565316 | An attempt was made to perform an uninitialization operation when that operation has already been completed.\r\n
0x80565317 | The Data Deduplication service detected an internal folder that is not secure. To secure the folder, reinstall deduplication on the volume.\r\n
0x80565318 | Data chunking has already been initiated.\r\n
0x80565319 | An attempt was made to perform an operation from an invalid state.\r\n
0x8056531a | An attempt was made to perform an operation before initialization.\r\n
0x8056531b | Call ::PushBuffer to continue chunking or ::Drain to enumerate any partial chunks.\r\n
0x8056531c | The Data Deduplication service detected multiple chunk store folders; however, only one chunk store folder is permitted. To fix this issue, reinstall deduplication on the volume.\r\n
0x8056531d | The data is invalid.\r\n
0x8056531e | The process is in an unknown state.\r\n
0x8056531f | The process is not running.\r\n
0x80565320 | There was an error while opening the file.\r\n
0x80565321 | The job process could not start because the job was not found.\r\n
0x80565322 | The client process ID does not match the ID of the host process that was started.\r\n
0x80565323 | The specified volume is not enabled for deduplication.\r\n
0x80565324 | A zero-character chunk ID is not valid.\r\n
0x80565325 | The index is filled to capacity.\r\n
0x80565327 | Session already exists.\r\n
0x80565328 | The compression format selected is not supported.\r\n
0x80565329 | The compressed buffer is larger than the uncompressed buffer.\r\n
0x80565330 | The buffer is not large enough.\r\n
0x8056533a | Index Scratch Log Error in: Seek, Read, Write, or Create\r\n
0x8056533b | The job type is invalid.\r\n
0x8056533c | Persistence layer enumeration error.\r\n
0x8056533d | The operation was cancelled.\r\n
0x8056533e | This job will not run at the scheduled time because it requires more memory than is currently available.\r\n
0x80565341 | The job was terminated while in a cancel or pending state.\r\n
0x80565342 | The job was terminated while in a handshake pending state.\r\n
0x80565343 | The job was terminated due to a service shutdown.\r\n
0x80565344 | The job was abandoned before starting.\r\n
0x80565345 | The job process exited unexpectedly.\r\n
0x80565346 | The Data Deduplication service detected that the container cannot be compacted or updated because it has reached the maximum generation version. \r\n
0x80565347 | The corruption log has reached its maximum size.\r\n
0x80565348 | The data deduplication scrubbing job failed to process the corruption logs.\r\n
0x80565349 | Data deduplication failed to create new chunk store container files. Allocate more space to the volume.\r\n
0x80565350 | An error occurred while opening the file because the file was in use. \r\n
0x80565351 | An error was discovered while deduplicating the file. The file is now skipped.\r\n
0x80565352 | File Server Deduplication encountered corruption while enumerating chunks in a chunk store.\r\n
0x80565353 | The scan log is not valid.\r\n
0x80565354 | The data is invalid due to checksum (CRC) mismatch error.\r\n
0x80565355 | Data deduplication encountered file corruption error.\r\n
0x80565356 | Job completed with some errors. Check event logs for more details.\r\n
0x80565357 | Data deduplication is not supported on the version of the chunk store found on this volume.\r\n
0x80565358 | Data deduplication encountered an unknown version of chunk store on this volume.\r\n
0x80565359 | The job was assigned less memory than the minimum it needs to run.\r\n
0x8056535a | The data deduplication job schedule cannot be modified.\r\n
0x8056535b | The valid data length of chunk store container is misaligned.\r\n
0x8056535c | File access is denied.\r\n
0x8056535d | Data deduplication job stopped due to too many corrupted files.\r\n
0x8056535e | Data deduplication job stopped due to an internal error in the BCrypt SHA-512 provider.\r\n
0x8056535f | Data deduplication job stopped for store reconciliation.\r\n
0x80565360 | File skipped for deduplication due to its size.\r\n
0x80565361 | File skipped due to deduplication retry limit.\r\n
0x80565362 | The pipeline buffer cache is full.\r\n
0x80565363 | Another Data deduplication job already running on this volume.\r\n
0x80565364 | Data deduplication cannot run this job on this Csv volume on this node. Try running the job on the Csv volume resource owner node.\r\n
0x80565365 | Data deduplication failed to initialize cluster state on this node.\r\n
0x80565366 | Optimization of the range was aborted by the dedup filter driver.\r\n
0x80565367 | The operation could not be performed because of a concurrent IO operation.\r\n
0x80565368 | Data deduplication encountered an unexpected error. Verify deduplication is enabled on all nodes if in a cluster configuration. Check the Data Deduplication Operational event log for more information.\r\n
0x80565369 | Data access for data deduplicated CSV volumes can only be disabled when in maintenance mode. Check the Data Deduplication Operational event log for more information.\r\n
0x8056536a | Data Deduplication encountered an IO device error that may indicate a hardware fault in the storage subsystem.\r\n
0x8056536b | Data deduplication cannot run this cmdlet on this Csv volume on this node. Try running the cmdlet on the Csv volume resource owner node.\r\n
0x8056536c | Deduplication job not supported during rolling cluster upgrade.\r\n
0x8056536d | Deduplication setting not supported during rolling cluster upgrade.\r\n
0x8056536e | Data port job is not ready to accept requests.\r\n
0x8056536f | Data port request not accepted due to request count/size limit exceeded.\r\n
0x80565370 | Data port request completed with some errors. Check event logs for more details.\r\n
0x80565371 | Data port request failed. Check event logs for more details.\r\n
0x80565372 | Data port error accessing the hash index. Check event logs for more details.\r\n
0x80565373 | Data port error accessing the stream store. Check event logs for more details.\r\n
0x80565374 | Data port file stub error. Check event logs for more details.\r\n
0x80565375 | Data port encountered a deduplication filter error. Check event logs for more details.\r\n
0x80565376 | Data port cannot commit stream map due to missing chunk. Check event logs for more details.\r\n
0x80565377 | Data port cannot commit stream map due to invalid stream map metadata. Check event logs for more details.\r\n
0x80565378 | Data port cannot commit stream map due to invalid stream map entry. Check event logs for more details.\r\n
0x80565379 | Data port cannot retrieve job interface for volume. Check event logs for more details.\r\n
0x8056537a | The specified path is not supported.\r\n
0x8056537b | // Data port cannot decompress chunk. Check event logs for more details.\r\n
0x8056537c | Data port cannot calculate chunk hash. Check event logs for more details.\r\n
0x8056537d | Data port cannot read chunk stream. Check event logs for more details.\r\n
0x8056537e | The target file is not a deduplicated file. Check event logs for more details.\r\n
0x8056537f | The target file is partially recalled. Check event logs for more details.\r\n
0x90000001 | Data Deduplication\r\n
0x90000002 | Application\r\n
0x91000001 | Data Deduplication Change Events\r\n
0xb0001000 | Volume "%1" appears as disconnected and it is ignored by the service.  You may want to rescan disks.   Error: %2.%n%3\r\n
0xb0001001 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3". Most likely the CPU is under heavy load.  Error: %4.%n%5\r\n
0xb0001002 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3".  Error: %4.%n%5\r\n
0xb0001003 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3" during Safe Mode. The Data Deduplication service cannot start while in safe mode.  Error: %4.%n%5\r\n
0xb0001004 | A critical component required by Data Deduplication is not registered. This might happen if an error occurred during Windows setup, or if the computer does not have the Windows Server 2012 or later version of Deduplication service installed. The error returned from CoCreateInstance on class with CLSID %1 and Name "%2" on machine "%3" is %4.%n%5\r\n
0xb0001005 | Data Deduplication service is shutting down due to idle timeout.%n%1\r\n
0xb0001006 | Data Deduplication service is shutting down due to shutdown event from the Service Control Manager.%n%1\r\n
0xb0001007 | Data Deduplication job of type "%1" on volume "%2" has completed with return code: %3%n%4\r\n
0xb0001008 | Data Deduplication error: Unexpected error calling routine %1.  hr = %2.%n%3\r\n
0xb0001009 | Data Deduplication error: Unexpected error.%n%1\r\n
0xb000100a | Data Deduplication warning: %1%nError: %2.%n%3\r\n
0xb000100b | Data Deduplication error: Unexpected COM error %1: %2.  Error code: %3.%n%4\r\n
0xb000100c | Data Deduplication was unable to access the following file or volume: "%1".  This file or volume might be locked by another application right now, or you might need to give Local System access to it.%n%2\r\n
0xb000100d | Data Deduplication encountered an unexpected error during volume scan of volumes mounted at "%1" ("%2"). To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100e | Data Deduplication was unable to create or access the shadow copy for volumes mounted at "%1" ("%2"). Possible causes include an improper Shadow Copy configuration, insufficient disk space, or extreme memory, I/O or CPU load of the system. To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100f | Data Deduplication was unable to access volumes mounted at "%1" ("%2"). Make sure that dismount or format operations do not happen while running deduplication.%n%3\r\n
0xb0001010 | Data Deduplication was unable to access a file or volume. Details:%n%n%1%n The volume may be inaccessible for I/O operations or marked read-only. In case of a cluster volume, this may be a transient failure during failover.%n%2\r\n
0xb0001011 | Data Deduplication was unable to scan volume "%1" ("%2").%n%3\r\n
0xb0001012 | Data Deduplication detected a corruption on file "%1" at offset ("%2").  If this condition persists then please restore the data from a previous backup.  Corruption details: Structure=%3, Corruption type = %4, Additional data = %5%n%6\r\n
0xb0001013 | Data Deduplication encountered failure while reconciling chunk store on volume "%1". The error code was %2. Reconciliation is disabled for the current optimization job.%n%3\r\n
0xb0001016 | Data Deduplication encountered corrupted chunk container %1 while performing full garbage collection. The corrupted chunk container is skipped.%n%2\r\n
0xb0001017 | Data Deduplication could not initialize change log under %1. The error code was %2.%n%3\r\n
0xb0001018 | Data Deduplication service could not mark chunk container %1 as reconciled. The error code was %2.%n%3\r\n
0xb0001019 | A Data Deduplication configuration file is corrupted. The system or volume may need to be restored from backup.%n%1\r\n
0xb000101a | Data Deduplication was unable to save one of the configuration stores on volume "%1" due to a disk-full error: If the disk is full, please clean it up (extend the volume or delete some files). If the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.%n%2\r\n
0xb000101b | Data Deduplication could not access global configuration since the cluster service is not running. Please start the cluster service and retry the operation.%n%1\r\n
0xb000101c | Shadow copy "%1" was deleted during storage report generation.  Volume "%2" might be configured with inadequate shadow copy storage area. Data Deduplication could not process this volume.%n%3\r\n
0xb000101d | Shadow copy creation failed for volume "%1" after retrying for %2 minutes because other shadow copies were being created.  Reschedule the Data Deduplication for a less busy time.%n%3\r\n
0xb000101e | Volume "%1" is not supported for shadow copy.  It is possible that the volume was removed from the system.  Data Deduplication service could not process this volume.%n%2\r\n
0xb000101f | The volume "%1" has been deleted or removed from the system.%n%2\r\n
0xb0001020 | Shadow copy creation failed for volume "%1" with error %2.  The volume might be configured with inadequate shadow copy storage area.  File Serve Deduplication service could not process this volume.%n%3\r\n
0xb0001021 | The file system on volume "%1" is potentially corrupted.  Please run the CHKDSK utility to verify and fix the file system.%n%2\r\n
0xb0001022 | Data Deduplication detected an insecure internal folder. To secure the folder, reinstall deduplication on the volume again.%n%1\r\n
0xb0001023 | Data Deduplication could not find a chunk store on the volume.%n%1\r\n
0xb0001024 | Data Deduplication detected multiple chunk store folders. To recover, reinstall deduplication on the volume.%n%1\r\n
0xb0001025 | Data Deduplication detected conflicting chunk store folders: "%1" and "%2".%n%3\r\n
0xb0001026 | The data is invalid.%n%1\r\n
0xb0001027 | Data Deduplication scheduler failed to initialize with error "%1".%n%2\r\n
0xb0001028 | Data Deduplication failed to validate job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb0001029 | Data Deduplication failed to start job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb000102c | Data Deduplication detected job type "%1" on volume "%2" uses too much memory. %3 MB is assigned. %4 MB is used.%n%5\r\n
0xb000102d | Data Deduplication detected job type "%1" on volume "%2" memory usage has dropped to desirable level.%n%3\r\n
0xb000102e | Data Deduplication cancelled job type "%1" on volume "%2". It uses too much memory than the amount assigned to it.%n%3\r\n
0xb000102f | Data Deduplication cancelled job type "%1" on volume "%2". Memory resource is running low on the machine or in the job.%n%3\r\n
0xb0001030 | Data Deduplication job type "%1" on volume "%2" failed to report completion to the service with error: %3.%n%4\r\n
0xb0001031 | Data Deduplication detected a container cannot be compacted or updated because it has reached the maximum generation.%n%1\r\n
0xb0001032 | Data Deduplication corruption log "%1" is corrupted.%n%2\r\n
0xb0001033 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". Please run scrubbing job to process corruption log. No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001034 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001035 | Data Deduplication scheduler failed to uninitialize with error "%1".%n%2\r\n
0xb0001036 | Data Deduplication detected a new container could not be created in a chunk store because it ran out of available container Id.%n%1\r\n
0xb0001037 | Data Deduplication full garbage collection phase 1 (cleaning file related metadata) on volume "%1" failed with error: %2.  The job will continue with phase 2 execution (data chunk cleanup).%n%3\r\n
0xb0001039 | Data Deduplication full garbage collection could not achieve maximum space reclamation because delete logs for data container %1 could not be cleaned up.%n%2\r\n
0xb000103a | Some files could not be deduplicated because of FSRM Quota violations on volume %1. Files skipped are likely compressed or sparse files in folders which are at quota or close to their quota limit. Please consider increasing the quota limit for folders that are at their quota limit or close to it.%n%2\r\n
0xb000103b | Data Deduplication failed to dedup file %1 "%2" due to fatal error %3%n%4\r\n
0xb000103c | Data Deduplication encountered corruption while accessing a file in chunk store.%n%1\r\n
0xb000103d | Data Deduplication encountered corruption while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103e | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103f | Data Deduplication is unable to access file %1 because the file is in use.%n%2\r\n
0xb0001040 | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store.%n%1\r\n
0xb0001041 | Data Deduplication cannot run the job on volume %1 because the dedup store version compatiblity check failed with error %2.%n%3\r\n
0xb0001042 | Data Deduplication has disabled the volume %1 because it has discovered too many corruptions. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001043 | Data Deduplication has detected a corrupt corruption metadata file on the store at %1. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001044 | Volume "%1" cannot be enabled for Data Deduplication. Data Deduplication does not support volumes larger than 64TB. Error: %2.%n%3\r\n
0xb0001045 | Data Deduplication cannot be enabled on SIS volume "%1". Error: %2.%n%3\r\n
0xb0001046 | File-system is configured for case-sensitive file/folder names. Data Deduplication does not support case-sensitive file-system mode.%n%1\r\n
0xb0001049 | Data Deduplication changed scrubbing job to read-only due to insufficient disk space.%n%1\r\n
0xb000104b | Data Deduplication has disabled the volume %1 because there are missing or corrupt containers. Please run deep scrubbing on the volume.%n%2\r\n
0xb000104d | Data Deduplication encountered a disk-full error.%n%1\r\n
0xb000104e | Data Deduplication job cannot run on volume "%1" due to insufficient disk space.%n%2\r\n
0xb000104f | Data Deduplication job cannot run on offline volume "%1".%n%2\r\n
0xb0001050 | Data Deduplication recovered a corrupt or missing file.%n%1\r\n
0xb0001051 | Data Deduplication encountered a corrupted metadata file. To correct the problem, schedule or manually run a Garbage Collection job on the affected volume with the -Full option.%n%1\r\n
0xb0001052 | Data Deduplication encountered chunk %1 with corrupted header while updating container. The corrupted chunk is replicated to the new container %2.%n%3\r\n
0xb0001053 | Data Deduplication encountered chunk %1 with transient header corruption while updating container. The corrupted chunk is NOT replicated to the new container %2.%n%3\r\n
0xb0001054 | Data Deduplication failed to read chunk container redirection table from file %1 with error %2.%n%3\r\n
0xb0001055 | Data Deduplication failed to initialize reparse point index table for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001056 | Data Deduplication failed to deep scrub container file %1 on volume %2 with error %3.%n%4\r\n
0xb0001057 | Data Deduplication failed to load stream map log for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001058 | Data Deduplication found a duplicate local chunk id %1 in container file %2.%n%3\r\n
0xb0001059 | Data Deduplication job type "%1" on volume "%2" was cancelled manually.%n%3\r\n
0xb000105a | Scheduled data Deduplication job type "%1" on volume "%2" was cancelled.%n%3\r\n
0xb000105d | The Data Deduplication chunk store statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105e | The Data Deduplication volume statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105f | Data Deduplication failed to append to deep scrubbing log file %1 with error %2.%n%3\r\n
0xb0001060 | Data Deduplication encountered a failure during deep scrubbing on store %1 with error %2.%n%3\r\n
0xb0001061 | Data Deduplication cancelled job type "%1" on volume "%2". The job violated Csv dedup job placement policy.%n%3\r\n
0xb0001062 | Data Deduplication cancelled job type "%1" on volume "%2". The csv job monitor has been uninitialized.%n%3\r\n
0xb0001063 | Data Deduplication encountered a IO device error while accessing a file on the volume. This is likely a hardware fault in the storage subsystem.%n%1\r\n
0xb0001064 | Data Deduplication encountered an unexpected error. If this is a cluster, verify Data Deduplication is enabled on all nodes of the cluster.%n%1\r\n
0xb0001065 | Attempted to disable data access for data deduplicated CSV volume "%1" without maintenance mode. Data access can only be disabled for a CSV volume when in maintenance mode. Place volume into maintenance mode and retry.%n%2\r\n
0xb0001800 | Data Deduplication service could not unoptimize file "%5%6%7". Error %8, "%9".\r\n
0xb0001801 | Data Deduplication service failed to unoptimize too many files %3. Some files are not reported.\r\n
0xb0001802 | Data Deduplication service has finished unoptimization on volume %3 with no errors.\r\n
0xb0001803 | Data Deduplication service has finished unoptimization on volume %3 with %4 errors.\r\n
0xb0001804 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb0001805 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nPriority: %7%nFull: %8%nVolume free space (MB): %9\r\n
0xb0001806 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6%nFull: %7%nRead-only: %8\r\n
0xb0001807 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6\r\n
0xb0001809 | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate (percent): %7%nSaved space (MB): %8%nVolume used space (MB): %9%nVolume free space (MB): %10%nOptimized file count: %11%nIn-policy file count: %12%nJob processed space (MB): %13%nJob elapsed time (seconds): %18%nJob throughput (MB/second): %19%nChurn processing throughput (MB/second): %20\r\n
0xb000180a | %1 job has completed.%n%nFull: %2%nVolume: %5 (%4)%nError code: %6%nError message: %7%nFreed up space (MB): %8%nVolume free space (MB): %9%nJob elapsed time (seconds): %10%nJob throughput (MB/second): %11\r\n
0xb000180b | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6\r\n
0xb000180c | %1 job has completed.%n%nFull: %2%nRead-only: %3%nVolume: %6 (%5)%nError code: %7%nError message: %8%nTotal corruption count: %9%nFixable corruption count: %10%n%nWhen corruptions are found, check more details in Scrubbing event channel.\r\n
0xb000180d | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nUnoptimized file count: %7%nJob processed space (MB): %8%nJob elapsed time (seconds): %9%nJob throughput (MB/second): %10\r\n
0xb000180e | %1 job has been queued.%n%nVolume: %4 (%3)%nSystem memory percent: %5 %nPriority: %6%nSchedule mode: %7\r\n
0xb000181c | Restore of deduplicated file "%1" failed with the following error: %2, "%3".\r\n
0xb000181d | Priority %1 job has started.%n%nVolume: %4 (%3)%nFile ID: %11%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb000181e | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable threads: %6%nPriority: %7\r\n
0xb000181f | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate (percent): %7%nSaved space (MB): %8%nVolume used space (MB): %9%nVolume free space (MB): %10%nOptimized file count: %11%nChunk lookup count: %12%nInserted chunk count: %13%nInserted chunks logical data (MB): %14%nInserted chunks physical data (MB): %15%nCommitted stream count: %16%nCommitted stream entry count: %17%nCommitted stream logical data (MB): %18%nRetrieved chunks physical data (MB): %19%nRetrieved stream logical data (MB): %20%nDataPort time (seconds): %21%nJob elapsed time (seconds): %22%nIngress throughput (MB/second): %23%nEgress throughput (MB/second): %24\r\n
0xb0001821 | Data Deduplication detected a non-clustered volume specified for the chunk index cache volume in a clustered deployment. The configuration is not recommended because it may result in job failures after failover.%n%nVolume: %3 (%2)\r\n
0xb0001822 | DataPort status update.  %n%nVolume: %2%nSavings rate (percent): %3%nSaved space (MB): %4%nVolume used space (MB): %5%nVolume free space (MB): %6%nOptimized file count: %7%nChunk lookup count: %8%nInserted chunk count: %9%nInserted chunks logical data (MB): %10%nInserted chunks physical data (MB): %11%nCommitted stream count: %12%nCommitted stream entry count: %13%nCommitted stream logical data (MB): %14%nRetrieved chunks physical data (MB): %15%nRetrieved stream logical data (MB): %16%nDataPort time (seconds): %17%nJob elapsed time (seconds): %18%nIngress throughput (MB/second): %19%nEgress throughput (MB/second): %20\r\n
0xb0002000 | Data Deduplication detected job type "%1" on volume "%2" working set is low. Ratio to commit size is %3.%n%4\r\n
0xb0002001 | Data Deduplication detected job type "%1" on volume "%2" working set has recovered to desirable level.%n%3\r\n
0xb0002002 | Data Deduplication detected job type "%1" on volume "%2" page fault rate is high. The rate is %3 page faults per second.%n%4\r\n
0xb0002003 | Data Deduplication detected job type "%1" on volume "%2" page fault rate has lowered to desirable level. The rate is %3 page faults per second.%n%4\r\n
0xb0002004 | Data Deduplication failed to dedup file "%1" with file ID %2 due to non-fatal error %3%n%4.%n%nNote: You can retrieve the file name by running the command FSUTIL FILE QUERYFILENAMEBYID on the file in question.\r\n
0xb000200c | Data Deduplication has aborted a group commit session.%n%nFile count: %1%nError: %2%n%3\r\n
0xb000201c | Fail to open dedup setting registry key\r\n
0xb000201d | Data Deduplication failed to dedup file "%1" with file ID %2 due to oplock break%n%3\r\n
0xb000201e | Data Deduplication failed to load hotspot table from file %1 due to error %2.%n%3\r\n
0xb000201f | Data Deduplication failed to initialize oplock.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb0002020 | Data Deduplication while running job on volume %1 detected invalid physical sector size %2. Using default value %3.%n%4\r\n
0xb0002021 | Data Deduplication detected an unsupported chunk store container.%n%1\r\n
0xb0002022 | Data Deduplication could not create window to receive task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002023 | Data Deduplication could not create thread to poll for task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002024 | An attempt was made to perform an initialization operation when initialization has already been completed.%n%1\r\n
0xb0002028 | Data Deduplication created emergency file %1.%n%3\r\n
0xb0002029 | Data Deduplication failed to create emergency file %1 with error %2.%n%3\r\n
0xb000202a | Data Deduplication deleted emergency file %1.%n%3\r\n
0xb000202b | Data Deduplication failed to delete emergency file %1 with error %2.%n%3\r\n
0xb000202c | Data Deduplication detected a chunk store container with misaligned valid data length.%n%1\r\n
0xb000202d | Data Deduplication Garbage Collection encountered a delete log entry with an invalid stream map signature for stream map Id %1.%n%2\r\n
0xb000202e | Data Deduplication failed to initialize oplock as the file appears to be missing.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb000202f | Data Deduplication skipped too many file-level errors. We will not log more than %1 file-level errors per job.%n%2\r\n
0xb0002030 | Data Deduplication diagnostic warning.%n%n%1%n%2\r\n
0xb0002031 | Data Deduplication diagnostic information.%n%n%1%n%2\r\n
0xb0002032 | Data Deduplication found file %1 with a stream map id %2 in container file %3 marked for deletion.%n%4\r\n
0xb0002033 | Failed to enqueue job of type "%1" on volume "%2".%n%3\r\n
0xb0002034 | Error terminating job host process for job type "%1" on volume "%2" (process id: %3).%n%4\r\n
0xb0002035 | Data Deduplication encountered corrupted chunk %1 while updating container. Corrupted data that cannot be repaired will be copied as-is to the new container %2.%n%3\r\n
0xb0002036 | Data Deduplication job type "%1" on volume "%2" failed to exit gracefully.%n%3\r\n
0xb0002037 | Data Deduplication job host for job type "%1" on volume "%2" exited unexpectedly.%n%3\r\n
0xb0002038 | Data Deduplication has failed to load corruption metadata file on the store at %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb0002039 | Data Deduplication full garbage collection phase 1 on volume "%1" encountered an error %2 while processing file %3. Phase 1 will need to be aborted since garbage collection of file-related metadata is unsafe to continue on file errors.%n%4\r\n
0xb000203a | Data Deduplication has failed to process corruption metadata file %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb000203b | Data Deduplication has failed to load a corrupted metadata file %1 due to error %2. Deleting the file and continuing.%n%3\r\n
0xb000203c | Data Deduplication has failed to set NTFS allocation size for container file %1 due to error %2.%n%3\r\n
0xb000203d | Data Deduplication configured to use BCrypt provider '%1' for hash algorithm %2.%n%3\r\n
0xb000203e | Data Deduplication could not use BCrypt provider '%1' for hash algorithm %2 due to an error in operation %3. Reverting to the Microsoft primitive CNG provider.%n%4\r\n
0xb000203f | Data Deduplication failed to include file "%1" in file metadata analysis calculations.%n%2\r\n
0xb0002040 | Data Deduplication failed to include stream map %1 in file metadata analysis calculations.%n%2\r\n
0xb0002041 | Data Deduplication encountered an error for file "%1" while scanning files and folders.%n%2\r\n
0xb0002042 | Data Deduplication encountered an error while attempting to resume processing. Please consult the event log parameters for more details about the current file being processed.%n%1\r\n
0xb0002043 | Data Deduplication encountered an error %1 whle scanning usn journal on volume %2 for updating hot range tracking.%n%3\r\n
0xb0002044 | Data Deduplication could not truncate the stream of an optimized file. No action is required. Error: %1%n%n%2\r\n
0xb0002800 | %1 job memory requirements.%n%nVolume: %4 (%3)%nMinimum memory: %5 MB%nMaximum memory: %6 MB%nMinimum disk: %7 MB%nMaximum cores: %8\r\n
0xb0002801 | %1 reconciliation has started.%n%nVolume: %4 (%3)\r\n
0xb0002802 | %1 reconciliation has completed.%n%nGuidance: This event is expected when Reconciliation has completed, there is no recommended or required action. Reconciliation is an internal process that allows Optimization and DataPort jobs to run when the entire Deduplication chunk index cannot be loaded into memory. %n%nVolume: %4 (%3)%nReconciled containers: %5%nUnreconciled containers: %6%nCatchup references: %7%nCatchup containers: %8%nReconciled references: %9%nReconciled containers: %10%nCross-reconciled references: %11%nCross-reconciled containers: %12%nError code: %13%nError message: %14\r\n
0xb0002803 | %1 job on volume %4 (%3) was configured with insufficient memory.%n%nSystem memory percentage: %5%nAvailable memory: %8 MB%nMinimum required memory: %6 MB\r\n
0xb0002804 | Optimization memory details for %1 job on volume %3 (%2).\r\n
0xb0002805 | An open file was skipped during optimization. No action is required.%n%nFileId: %2%nSkip Reason: %1\r\n
0xb0002806 | An operation succeeded after one or more retries. Operation: %1; FileId: %3; Number of retries: %2\r\n
0xb0002807 | Data Deduplication aborted the optimization pipeline.%nVolumePath: %1%nErrorCode: %2%nErrorMessage: %3Details: %4\r\n
0xb0002808 | Data Deduplication aborted a file.%nFileId: %1%nFilePath: %2%nFileSize: %3%nFlags: %4%nTotalRanges: %5%nSkippedRanges: %6%nAbortedRanges: %7%nCommittedRanges: %8%nErrorCode: %9%nErrorMessage: %10Details: %11\r\n
0xb0002809 | Data Deduplication aborted a file range.%nFileId: %1%nFilePath: %2%nRangeOffset: %3%nRangeLength: %4%nErrorCode: %5%nErrorMessage: %6Details: %7\r\n
0xb000280a | Data Deduplication aborted a session.%nMaxSize: %1%nCurrentSize: %2%nRemainingRanges: %3%nErrorCode: %4%nErrorMessage: %5Details: %6\r\n
0xb000280b | USN journal created.%n%nVolume: %2 (%1)%nMaximum size %3 MB%nAllocation size %4 MB\r\n
0xb000280c | DataPort memory details for %1 job on volume %3 (%2).\r\n
0xb000280d | Data deduplication detected a file with an ID that is not supported.  Files with identifiers unpackable into 64-bits will be skipped. FileId: %1 FileName: %2\r\n
0xb000280e | Reconciliation should be run to ensure optimal savings.%n%nGuidance: This event is expected when Reconciliation is turned off for the DataPort job. Reconciliation is an internal process that allows Optimization and DataPort jobs to run when the entire Deduplication chunk index cannot be loaded into memory. When Reconciliation would require 50% or more of the memory on the system, it is recommended that you (temporarily) cease running a DataPort job against this volume, and run an Optimization job. If Reconciliation is not run through an Optimization job before Reconciliation would require more than 100% of system memory, Reconciliation will not be able to be run again (unless more memory is added). This would result in permanent decreased space efficiency on this volume.%n%nVolume: %2 (%1)%nMemory percentage required: %3\r\n
0xb000280f | Data Deduplication optimization job will not run the reconciliation step due to inadequate memory.%n%nGuidance: Deduplication savings will be suboptimal until the optimization job is provided more memory, or more more memory is added to the system.%n%nVolume: %2 (%1)%nMemory percentage required: %3\r\n
0xb0003200 | Data Deduplication service detected corruption in "%5%6%7". The corruption cannot be repaired.\r\n
0xb0003201 | Data Deduplication service detected corruption (%7) in "%6". See the event details for more information.\r\n
0xb0003202 | Data Deduplication service detected a corrupted item (%11 - %13, %8, %9, %10, %12) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003203 | Data Deduplication service has finished scrubbing on volume %3. It did not find any corruption since the last scrubbing.\r\n
0xb0003204 | Data Deduplication service found %4 corruption(s) on volume %3. All corruptions are fixed.\r\n
0xb0003205 | Data Deduplication service found %4 corruption(s) on volume %3. %5 corruption(s) are fixed. %6 user file(s) are corrupted. %7 user file(s) are fixed. For the corrupted file list, see the Microsoft/Windows/Deduplication/Scrubbing events.\r\n
0xb0003206 | Data Deduplication service found too many corruptions on volume %3. Some corruptions are not reported.\r\n
0xb0003211 | Data Deduplication service has finished scrubbing on volume %3. See the event details for more information.\r\n
0xb0003212 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003213 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003214 | Data Deduplication service encountered error while detecting corruptions in chunk store on volume %3. The error was %4. The job is aborted.\r\n
0xb0003216 | Data Deduplication service encountered error while loading corruption logs on volume %3. The error was %4. The job continues. Some corruptions may not be detected.\r\n
0xb0003217 | Data Deduplication service encountered error while cleaning up corruption logs on volume %3. The error was %4. Some corruptions may be reported again next time.\r\n
0xb0003218 | Data Deduplication service encountered error while loading hotspots mapping from chunk store on volume %3. The error was %4. Some corruptions may not be repaired.\r\n
0xb0003219 | Data Deduplication service encountered error while determining corrupted user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb000321a | Data Deduplication service found %4 corruption(s) on volume %3. %6 user file(s) are corrupted. %7 user file(s) are fixable. Please run scrubbing job in read-write mode to attempt fixing reported corruptions.\r\n
0xb000321b | Data Deduplication service fixed corruption in "%5%6%7".\r\n
0xb000321c | Data Deduplication service detected fixable corruption in "%5%6%7". Please run scrubbing job in read-write mode to fix this corruption.\r\n
0xb000321e | Data Deduplication service encountered error while repairing corruptions on volume %3. The error was %4. The repair is unsuccessful.\r\n
0xb000321f | Data Deduplication service detected a corrupted item (%6, %7, %8, %9) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003220 | Container (%8,%9) with user data is missing from the chunk store. Missing container may result from incomplete restore, incomplete migration or file-system corruption. Volume is disabled from further optimization. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0003221 | Data Deduplication service encountered error while scaning dedup user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb0003222 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003223 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003224 | Data Deduplication service detected potential data loss (%9) in "%6" due to sharing reparse data with file "%8". See the event details for more information.\r\n
0xb0003225 | Container (%8,%9) with user data is corrupt in the chunk store. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0005000 | Open stream store stream (StartingChunkId %1, FileId %2)\r\n
0xb0005001 | Open stream store stream completed %1\r\n
0xb0005002 | Prepare for paging IO (Stream %1, FileId %2)\r\n
0xb0005003 | Prepare for paging IO completed %1\r\n
0xb0005005 | Read stream map completed %1\r\n
0xb0005006 | Read chunks (Stream %1, FileId %2, IoType %3, FirstRequestChunkId %4, NextRequest %5)\r\n
0xb0005007 | Read chunks completed %1\r\n
0xb0005008 | Compute checksum (ItemType %1, DataSize %2)\r\n
0xb0005009 | Compute checksum completed %1\r\n
0xb000500a | Get container entry (ContainerId %1, Generation %2)\r\n
0xb000500b | Get container entry completed %1\r\n
0xb000500c | Get maximum generation for container (ContainerId %1, Generation %2)\r\n
0xb000500d | Get maximum generation for container completed %1\r\n
0xb000500e | Open chunk container (ContainerId %1, Generation %2, RootPath %4)\r\n
0xb000500f | Open chunk container completed %1\r\n
0xb0005010 | Initialize chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005011 | Initialize chunk container redirection table completed %1\r\n
0xb0005012 | Validate chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005013 | Validate chunk container redirection table completed %1\r\n
0xb0005014 | Get chunk container valid data length (ContainerId %1, Generation %2)\r\n
0xb0005015 | Get chunk container valid data length completed %1\r\n
0xb0005016 | Get offset from chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005017 | Get offset from chunk container redirection table completed %1\r\n
0xb0005018 | Read chunk container block (ContainerId %1, Generation %2, Buffer %3, Offset %4, Length %5, IoType %6, Synchronous %7)\r\n
0xb0005019 | Read chunk container block completed %1\r\n
0xb000501a | Clear chunk container block (Buffer %1, Size %2, BufferType %3)\r\n
0xb000501b | Clear chunk container block completed %1\r\n
0xb000501c | Copy chunk (Buffer %1, Size %2, BufferType %3, BufferOffset %4, OutputCapacity %5)\r\n
0xb000501d | Copy chunk completed %1\r\n
0xb000501e | Initialize file cache (UnderlyingFileObject %1, CacheFileSize %2)\r\n
0xb000501f | Initialize file cache completed %1\r\n
0xb0005020 | Map file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005021 | Map file cache data completed %1\r\n
0xb0005022 | Unpin file cache data(Bcb %1)\r\n
0xb0005023 | Unpin file cache data completed %1\r\n
0xb0005024 | Copy file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005025 | Copy file cache data completed %1\r\n
0xb0005026 | Read underlying file cache data (CacheFileObject %1, UnderlyingFileObject %2, Offset %3, Length %4)\r\n
0xb0005027 | Read underlying file cache data completed %1\r\n
0xb0005028 | Get chunk container file size (ContainerId %1, Generation %2)\r\n
0xb0005029 | Get chunk container file size completed %1\r\n
0xb000502a | Pin stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb000502b | Pin stream map completed %1\r\n
0xb000502c | Pin chunk container (ContainerId %1, Generation %2)\r\n
0xb000502d | Pin chunk container completed %1\r\n
0xb000502e | Pin chunk (ContainerId %1, Generation %2)\r\n
0xb000502f | Pin chunk completed %1\r\n
0xb0005030 | Allocate pool buffer (ReadLength %1, PagingIo %2)\r\n
0xb0005031 | Allocate pool buffer completed %1\r\n
0xb0005032 | Unpin chunk container (ContainerId %1, Generation %2)\r\n
0xb0005033 | Unpin chunk container completed %1\r\n
0xb0005034 | Unpin chunk (ContainerId %1, Generation %2)\r\n
0xb0005035 | Unpin chunk completed %1\r\n
0xb0006028 | Dedup read processing (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006029 | Dedup read processing completed %1\r\n
0xb000602a | Get first stream map entry (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602b | Get first stream map entry completed %1\r\n
0xb000602c | Read chunk metadata (Stream %1, CurrentOffset %2, AdjustedFinalOffset %3, FirstChunkByteOffset %4, ChunkRequestsEndOffset %5, TlCache %6)\r\n
0xb000602d | Read chunk metadata completed %1\r\n
0xb000602e | Read chunk data (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602f | Read chunk data completed %1\r\n
0xb0006030 | Reference TlCache data (TlCache %1, Stream %2)\r\n
0xb0006031 | Reference TlCache data completed %1\r\n
0xb0006032 | Read chunk data from stream store (Stream %1)\r\n
0xb0006033 | Read chunk data from stream store completed %1\r\n
0xb0006034 | Assemble chunk data\r\n
0xb0006035 | Assemble chunk data completed %1\r\n
0xb0006036 | Decompress chunk data\r\n
0xb0006037 | Decompress chunk data completed %1\r\n
0xb0006038 | Copy chunk data in to user buffer (BytesCopied %1)\r\n
0xb0006039 | Copy chunk data in to user buffer completed %1\r\n
0xb000603a | Insert chunk data in to tlcache\r\n
0xb000603b | Insert chunk data in to tlcache completed %1\r\n
0xb000603c | Read data from dedup reparse point file (FileObject %1, Offset %2, Length %3)\r\n
0xb000603d | Read underlying file cache data completed %1\r\n
0xb000603e | Prepare stream map (StreamContext %1)\r\n
0xb000603f | Prepare stream map completed %1\r\n
0xb0006040 | Patch clean ranges (FileObject %1, Offset %2, Length %3)\r\n
0xb0006041 | Patch clean ranges completed %1\r\n
0xb0006042 | Writing data to dedup file (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006043 | Writing data to dedup file completed %1\r\n
0xb0006044 | Queue write request on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006045 | Queue write request on dedup file completed %1\r\n
0xb0006046 | Do copy on write work on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006047 | Do copy on write work on dedup file completed %1\r\n
0xb0006048 | Do full recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006049 | Do full recall on dedup file completed %1\r\n
0xb000604a | Do partial recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604b | Do partial recall on dedup file completed %1\r\n
0xb000604c | Do dummy paging read on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604d | Do dummy paging read on dedup file completed %1\r\n
0xb000604e | Read clean data for recalling file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604f | Read clean data for recalling file completed %1\r\n
0xb0006050 | Write clean data to dedup file normally (FileObject %1, Offset %2, Length %3)\r\n
0xb0006051 | Write clean data to dedup file completed %1\r\n
0xb0006052 | Write clean data to dedup file paged (FileObject %1, Offset %2, Length %3)\r\n
0xb0006053 | Write clean data to dedup file paged completed %1\r\n
0xb0006054 | Recall dedup file using paging Io (FileObject %1, Offset %2, Length %3)\r\n
0xb0006055 | Recall dedup file using paging Io completed %1\r\n
0xb0006056 | Flush dedup file after recall (FileObject %1)\r\n
0xb0006057 | Flush dedup file after recall completed %1\r\n
0xb0006058 | Update bitmap after recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006059 | Update bitmap after recall on dedup file completed %1\r\n
0xb000605a | Delete dedup reparse point (FileObject %1)\r\n
0xb000605b | Delete dedup reparse point completed %1\r\n
0xb000605c | Open dedup file (FilePath %1)\r\n
0xb000605d | Open dedup file completed %1\r\n
0xb000605e | Locking user buffer for read\r\n
0xb000605f | Locking user buffer for read completed %1\r\n
0xb0006060 | Get system address for MDL\r\n
0xb0006061 | Get system address for MDL completed %1\r\n
0xb0006062 | Read clean dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006063 | Read clean dedup file completed %1\r\n
0xb0006064 | Get range state (Offset %1, Length %2)\r\n
0xb0006065 | Get range state completed %1\r\n
0xb0006066 | Get chunk body\r\n
0xb0006067 | Get chunk body completed %1\r\n
0xb0006068 | Release chunk\r\n
0xb0006069 | Release chunk completed %1\r\n
0xb000606a | Release decompress chunk context (BufferSize %1)\r\n
0xb000606b | Release decompress chunk context completed %1\r\n
0xb000606c | Prepare decompress chunk context (BufferSize %1)\r\n
0xb000606d | Prepare decompress chunk context completed %1\r\n
0xb000606e | Copy data to compressed buffer (BufferSize %1)\r\n
0xb000606f | Copy data to compressed buffer completed %1\r\n
0xb0006070 | Release data from TL Cache\r\n
0xb0006071 | Release data from TL Cache completed %1\r\n
0xb0006072 | Queue async read request (FileObject %1, Offset %2, Length %3)\r\n
0xb0006073 | Queue async read request complete %1\r\n
0xb0015004 | Read stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb1004000 | Create chunk container (%1 - %2.%3.ccc)\r\n
0xb1004001 | Create chunk container completed %1\r\n
0xb1004002 | Copy chunk container (%1 - %2.%3.ccc)\r\n
0xb1004003 | Copy chunk container completed %1\r\n
0xb1004004 | Delete chunk container (%1 - %2.%3.ccc)\r\n
0xb1004005 | Delete chunk container completed %1\r\n
0xb1004006 | Rename chunk container (%1 - %2.%3.ccc%4)\r\n
0xb1004007 | Rename chunk container completed %1\r\n
0xb1004008 | Flush chunk container (%1 - %2.%3.ccc)\r\n
0xb1004009 | Flush chunk container completed %1\r\n
0xb100400a | Rollback chunk container (%1 - %2.%3.ccc)\r\n
0xb100400b | Rollback chunk container completed %1\r\n
0xb100400c | Mark chunk container (%1 - %2.%3.ccc) read-only\r\n
0xb100400d | Mark chunk container read-only completed %1\r\n
0xb100400e | Write chunk container (%1 - %2.%3.ccc) redirection table at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb100400f | Write chunk container redirection table completed %1\r\n
0xb1004011 | Write chunk container header completed %1\r\n
0xb1004013 | Insert data chunk header completed %1\r\n
0xb1004015 | Insert data chunk body completed %1 with ChunkId %2\r\n
0xb1004019 | Write delete log header completed %1\r\n
0xb100401b | Append delete log entries completed %1\r\n
0xb100401d | Delete delete log completed %1\r\n
0xb100401f | Rename delete log completed %1\r\n
0xb1004021 | Write chunk container bitmap completed %1\r\n
0xb1004023 | Delete chunk container bitmap completed %1\r\n
0xb1004024 | Write merge log (%5 - %6.%7.merge.log) header\r\n
0xb1004025 | Write merge log header completed %1\r\n
0xb1004027 | Insert hotspot chunk header completed %1\r\n
0xb1004029 | Insert hotspot chunk body completed %1 with ChunkId %2\r\n
0xb100402b | Insert stream map chunk header completed %1\r\n
0xb100402d | Insert stream map chunk body completed %1 with ChunkId %2\r\n
0xb100402f | Append merge log entries completed %1\r\n
0xb1004030 | Delete merge log (%1 - %2.%3.merge.log)\r\n
0xb1004031 | Delete merge log completed %1\r\n
0xb1004032 | Flush merge log (%1 - %2.%3.merge.log)\r\n
0xb1004033 | Flush merge log completed %1\r\n
0xb1004034 | Update file list entries (Remove: %1, Add: %2)\r\n
0xb1004035 | Update file list entries completed %1\r\n
0xb1004036 | Set dedup reparse point on %2 (FileId %1) (ReparsePoint: SizeBackedByChunkStore %3, StreamMapInfoSize %4, StreamMapInfo %5)\r\n
0xb1004037 | Set dedup reparse point completed %1 (%2)\r\n
0xb1004038 | Set dedup zero data on %2 (FileId %1)\r\n
0xb1004039 | Set dedup zero data completed %1\r\n
0xb100403a | Flush reparse point files\r\n
0xb100403b | Flush reparse point files completed %1\r\n
0xb100403c | Set sparse on file id %1\r\n
0xb100403d | Set sparse completed %1\r\n
0xb100403e | FSCTL_SET_ZERO_DATA on file id %1 at offset %2 and BeyondFinalZero %3\r\n
0xb100403f | FSCTL_SET_ZERO_DATA completed %1\r\n
0xb1004040 | Rename chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1004041 | Rename chunk container bitmap completed %1\r\n
0xb1004042 | Insert padding chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1004043 | Insert padding chunk header completed %1\r\n
0xb1004044 | Insert padding chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1004045 | Insert padding chunk body completed %1 with ChunkId %2\r\n
0xb1004046 | Insert batch of chunks to chunk container (%1 - %2.%3.ccc) at offset %4 (BatchChunkCount %5, BatchDataSize %6)\r\n
0xb1004047 | Insert batch of chunks completed %1\r\n
0xb1004049 | Write chunk container directory completed %1\r\n
0xb100404b | Delete chunk container directory completed %1\r\n
0xb100404c | Rename chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb100404d | Rename chunk container directory completed %1\r\n
0xb1014010 | Write chunk container (%5 - %6.%7.ccc) header at offset %8 (Header: USN %9, VDL %10, #Chunk %11, NextLocalId %12, Flags %13, LastAppendTime %14, BackupRedirectionTableOfset %15, LastReconciliationLocalId %16)\r\n
0xb1014012 | Insert data chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1014014 | Insert data chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014018 | Write delete log (%5 - %6.%7.delete.log) header\r\n
0xb101401a | Append delete log (%1 - %2.%3.delete.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb101401c | Delete delete log (%1 - %2.%3.delete.log)\r\n
0xb101401e | Rename delete log (%1 - %2.%3.delete.log)\r\n
0xb1014020 | Write chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4) (Bitmap: BitLength %5, StartIndex %6, Count %7)\r\n
0xb1014022 | Delete chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1014026 | Insert hotspot chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014028 | Insert hotspot chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb101402a | Insert stream map chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014048 | Write chunk container directory (%1 - %2) for chunk container (%1 - %3.%4) (Directory: EntryCount %5)\r\n
0xb101404a | Delete chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb102402e | Append merge log (%1 - %2.%3.merge.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb103402c | Insert stream map chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7) (Entries: StartIndex %8, Count %9)\r\n
0xd0000001 | Chunk header\r\n
0xd0000002 | Chunk body\r\n
0xd0000003 | Container header\r\n
0xd0000004 | Container redirection table\r\n
0xd0000005 | Hotspot table\r\n
0xd0000006 | Delete log header\r\n
0xd0000007 | Delete log entry\r\n
0xd0000008 | GC bitmap header\r\n
0xd0000009 | GC bitmap entry\r\n
0xd000000a | Merge log header\r\n
0xd000000b | Merge log entry\r\n
0xd000000c | Data\r\n
0xd000000d | Stream map\r\n
0xd000000e | Hotspot\r\n
0xd000000f | Optimization\r\n
0xd0000010 | Garbage Collection\r\n
0xd0000011 | Scrubbing\r\n
0xd0000012 | Unoptimization\r\n
0xd0000013 | Analysis\r\n
0xd0000014 | Low\r\n
0xd0000015 | Normal\r\n
0xd0000016 | High\r\n
0xd0000017 | Cache\r\n
0xd0000018 | Non-cache\r\n
0xd0000019 | Paging\r\n
0xd000001a | Memory map\r\n
0xd000001b | Paging memory map\r\n
0xd000001c | None\r\n
0xd000001d | Pool\r\n
0xd000001e | PoolAligned\r\n
0xd000001f | MDL\r\n
0xd0000020 | Map\r\n
0xd0000021 | Cached\r\n
0xd0000022 | NonCached\r\n
0xd0000023 | Paged\r\n
0xd0000024 | container file\r\n
0xd0000025 | file list file\r\n
0xd0000026 | file list header\r\n
0xd0000027 | file list entry\r\n
0xd0000028 | primary file list file\r\n
0xd0000029 | backup file list file\r\n
0xd000002a | Scheduled\r\n
0xd000002b | Manual\r\n
0xd000002c | recall bitmap header\r\n
0xd000002d | recall bitmap body\r\n
0xd000002e | recall bitmap missing\r\n
0xd000002f | Recall bitmap\r\n
0xd0000030 | Unknown\r\n
0xd0000031 | The pipeline handle was closed\r\n
0xd0000032 | The file was deleted\r\n
0xd0000033 | The file was overwritten\r\n
0xd0000034 | The file was recalled\r\n
0xd0000035 | A transaction was started on the file\r\n
0xd0000036 | The file was encrypted\r\n
0xd0000037 | The file was compressed\r\n
0xd0000038 | Set Zero Data was called on the file\r\n
0xd0000039 | Extended Attributes were set on the file\r\n
0xd000003a | A section was created on the file\r\n
0xd000003b | The file was shrunk\r\n
0xd000003c | A long-running IO operation prevented optimization\r\n
0xd000003d | An IO operation failed\r\n
0xd000003e | Notifying Optimization\r\n
0xd000003f | Setting the Reparse Point\r\n
0xd0000040 | Truncating the file\r\n
0xd0000041 | DataPort\r\n
0xd1000001 | None\r\n
0xd1000002 | LZNT1\r\n
0xd1000003 | Xpress\r\n
0xd1000004 | Xpreff Huff\r\n
0xd1000005 | None\r\n
0xd1000006 | Standard\r\n
0xd1000007 | Max\r\n
0xd1000008 | Hybrid\r\n
0xf0000001 | None\r\n
0xf0000002 | Bad checksum\r\n
0xf0000003 | Inconsistent metadata\r\n
0xf0000004 | Invalid header metadata\r\n
0xf0000005 | Missing file\r\n
0xf0000006 | Bad checksum (storage subsystem)\r\n
0xf0000007 | Corruption (storage subsystem)\r\n
0xf0000008 | Corruption (missing metadata)\r\n
0xf0000009 | Possible data loss (duplicate reparse data)\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x00565301 | Reconciliation of chunk store is due.\r\n
0x00565302 | There are no actions associated with this job.\r\n
0x00565303 | Data deduplication cannot runing this job on this Csv volume on this node.\r\n
0x00565304 | Data deduplication cannot runing this cmdlet on this Csv volume on this node.\r\n
0x10000001 | Reporting\r\n
0x10000002 | Filter\r\n
0x10000003 | Kernel mode stream store\r\n
0x10000004 | Kernel mode chunk store\r\n
0x10000005 | Kernel mode chunk container\r\n
0x10000006 | Kernel mode file cache\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Data Deduplication Optimization Task\r\n
0x70000002 | Data Deduplication Garbage Collection Task\r\n
0x70000003 | Data Deduplication Scrubbing Task\r\n
0x70000004 | Data Deduplication Unoptimization Task\r\n
0x70000005 | Open stream store stream\r\n
0x70000006 | Prepare for paging IO\r\n
0x70000007 | Read stream map\r\n
0x70000008 | Read chunks\r\n
0x70000009 | Compute checksum\r\n
0x7000000a | Get container entry\r\n
0x7000000b | Get maximum generation for container\r\n
0x7000000c | Open chunk container\r\n
0x7000000d | Initialize chunk container redirection table\r\n
0x7000000e | Validate chunk container redirection table\r\n
0x7000000f | Get chunk container valid data length\r\n
0x70000010 | Get offset from chunk container redirection table\r\n
0x70000011 | Read chunk container block\r\n
0x70000012 | Clear chunk container block\r\n
0x70000013 | Copy chunk\r\n
0x70000014 | Initialize file cache\r\n
0x70000015 | Map file cache data\r\n
0x70000016 | Unpin file cache data\r\n
0x70000017 | Copy file cache data\r\n
0x70000018 | Read underlying file cache data\r\n
0x70000019 | Get chunk container file size\r\n
0x7000001a | Pin stream map\r\n
0x7000001b | Pin chunk container\r\n
0x7000001c | Pin chunk\r\n
0x7000001d | Allocate pool buffer\r\n
0x7000001e | Unpin chunk container\r\n
0x7000001f | Unpin chunk\r\n
0x70000020 | Dedup read processing\r\n
0x70000021 | Get first stream map entry\r\n
0x70000022 | Read chunk metadata\r\n
0x70000023 | Read chunk data\r\n
0x70000024 | Reference TlCache data\r\n
0x70000025 | Read chunk data from stream store\r\n
0x70000026 | Assemble chunk data\r\n
0x70000027 | Decompress chunk data\r\n
0x70000028 | Copy chunk data in to user buffer\r\n
0x70000029 | Insert chunk data in to tlcache\r\n
0x7000002a | Read data from dedup reparse point file\r\n
0x7000002b | Prepare stream map\r\n
0x7000002c | Patch clean ranges\r\n
0x7000002d | Writing data to dedup file\r\n
0x7000002e | Queue write request on dedup file\r\n
0x7000002f | Do copy on write work on dedup file\r\n
0x70000030 | Do full recall on dedup file\r\n
0x70000031 | Do partial recall on dedup file\r\n
0x70000032 | Do dummy paging read on dedup file\r\n
0x70000033 | Read clean data for recalling file\r\n
0x70000034 | Write clean data to dedup file normally\r\n
0x70000035 | Write clean data to dedup file paged\r\n
0x70000036 | Recall dedup file using paging Io\r\n
0x70000037 | Flush dedup file after recall\r\n
0x70000038 | Update bitmap after recall on dedup file\r\n
0x70000039 | Delete dedup reparse point\r\n
0x7000003a | Open dedup file\r\n
0x7000003b | Locking user buffer for read\r\n
0x7000003c | Get system address for MDL\r\n
0x7000003d | Read clean dedup file\r\n
0x7000003e | Get range state\r\n
0x7000003f | Get chunk body\r\n
0x70000040 | Release chunk\r\n
0x70000041 | Release decompress chunk context\r\n
0x70000042 | Prepare decompress chunk context\r\n
0x70000043 | Copy data to compressed buffer\r\n
0x70000044 | Release data from TL Cache\r\n
0x70000045 | Queue async read request\r\n
0x80565301 | The requested object was not found.\r\n
0x80565302 | One (or more) of the arguments given to the task scheduler is not valid.\r\n
0x80565303 | The specified object already exists.\r\n
0x80565304 | The specified path was not found.\r\n
0x80565305 | The specified user is invalid.\r\n
0x80565306 | The specified path is invalid.\r\n
0x80565307 | The specified name is invalid.\r\n
0x80565308 | The specified property is out of range.\r\n
0x80565309 | A required filter driver is either not installed, not loaded, or not ready for service.\r\n
0x8056530a | There is insufficient disk space to perform the requested operation.\r\n
0x8056530b | Deduplication could not be enabled on the specified volume. This might be because the volume uses an unsupported file system, is larger than the maximum supported volume size, is read-only, is formatted with an unsupported cluster size, or is not a fixed drive. Deduplication is supported on fixed, write-enabled ReFS, NTFS, CSVFS_ReFS, or CSVFS_NTFS volumes smaller than or equal to 64 TB, with cluster sizes less than or equal to 64 KB.\r\n
0x8056530c | Data deduplication encountered an unexpected error. Check the Data Deduplication Operational event log for more information.\r\n
0x8056530d | The specified scan log cursor has expired.\r\n
0x8056530e | The file system might be corrupted.  Please run the CHKDSK utility.\r\n
0x8056530f | A volume shadow copy could not be created or was unexpectedly deleted.\r\n
0x80565310 | Data deduplication encountered a corrupted XML configuration file.\r\n
0x80565311 | The Data Deduplication service could not access the global configuration because the Cluster service is not running.\r\n
0x80565312 | The Data Deduplication service could not access the global configuration because it has not been installed yet.\r\n
0x80565313 | Data deduplication failed to access the volume. It may be offline.\r\n
0x80565314 | The module encountered an invalid parameter or a valid parameter with an invalid value, or an expected module parameter was not found. Check the operational event log for more information.\r\n
0x80565315 | An attempt was made to perform an initialization operation when initialization has already been completed.\r\n
0x80565316 | An attempt was made to perform an uninitialization operation when that operation has already been completed.\r\n
0x80565317 | The Data Deduplication service detected an internal folder that is not secure. To secure the folder, reinstall deduplication on the volume.\r\n
0x80565318 | Data chunking has already been initiated.\r\n
0x80565319 | An attempt was made to perform an operation from an invalid state.\r\n
0x8056531a | An attempt was made to perform an operation before initialization.\r\n
0x8056531b | Call ::PushBuffer to continue chunking or ::Drain to enumerate any partial chunks.\r\n
0x8056531c | The Data Deduplication service detected multiple chunk store folders; however, only one chunk store folder is permitted. To fix this issue, reinstall deduplication on the volume.\r\n
0x8056531d | The data is invalid.\r\n
0x8056531e | The process is in an unknown state.\r\n
0x8056531f | The process is not running.\r\n
0x80565320 | There was an error while opening the file.\r\n
0x80565321 | The job process could not start because the job was not found.\r\n
0x80565322 | The client process ID does not match the ID of the host process that was started.\r\n
0x80565323 | The specified volume is not enabled for deduplication.\r\n
0x80565324 | A zero-character chunk ID is not valid.\r\n
0x80565325 | The index is filled to capacity.\r\n
0x80565327 | Session already exists.\r\n
0x80565328 | The compression format selected is not supported.\r\n
0x80565329 | The compressed buffer is larger than the uncompressed buffer.\r\n
0x80565330 | The buffer is not large enough.\r\n
0x8056533a | Index Scratch Log Error in: Seek, Read, Write, or Create\r\n
0x8056533b | The job type is invalid.\r\n
0x8056533c | Persistence layer enumeration error.\r\n
0x8056533d | The operation was cancelled.\r\n
0x8056533e | This job will not run at the scheduled time because it requires more memory than is currently available.\r\n
0x80565341 | The job was terminated while in a cancel or pending state.\r\n
0x80565342 | The job was terminated while in a handshake pending state.\r\n
0x80565343 | The job was terminated due to a service shutdown.\r\n
0x80565344 | The job was abandoned before starting.\r\n
0x80565345 | The job process exited unexpectedly.\r\n
0x80565346 | The Data Deduplication service detected that the container cannot be compacted or updated because it has reached the maximum generation version. \r\n
0x80565347 | The corruption log has reached its maximum size.\r\n
0x80565348 | The data deduplication scrubbing job failed to process the corruption logs.\r\n
0x80565349 | Data deduplication failed to create new chunk store container files. Allocate more space to the volume.\r\n
0x80565350 | An error occurred while opening the file because the file was in use. \r\n
0x80565351 | An error was discovered while deduplicating the file. The file is now skipped.\r\n
0x80565352 | File Server Deduplication encountered corruption while enumerating chunks in a chunk store.\r\n
0x80565353 | The scan log is not valid.\r\n
0x80565354 | The data is invalid due to checksum (CRC) mismatch error.\r\n
0x80565355 | Data deduplication encountered file corruption error.\r\n
0x80565356 | Job completed with some errors. Check event logs for more details.\r\n
0x80565357 | Data deduplication is not supported on the version of the chunk store found on this volume.\r\n
0x80565358 | Data deduplication encountered an unknown version of chunk store on this volume.\r\n
0x80565359 | The job was assigned less memory than the minimum it needs to run.\r\n
0x8056535a | The data deduplication job schedule cannot be modified.\r\n
0x8056535b | The valid data length of chunk store container is misaligned.\r\n
0x8056535c | File access is denied.\r\n
0x8056535d | Data deduplication job stopped due to too many corrupted files.\r\n
0x8056535e | Data deduplication job stopped due to an internal error in the BCrypt SHA-512 provider.\r\n
0x8056535f | Data deduplication job stopped for store reconciliation.\r\n
0x80565360 | File skipped for deduplication due to its size.\r\n
0x80565361 | File skipped due to deduplication retry limit.\r\n
0x80565362 | The pipeline buffer cache is full.\r\n
0x80565363 | Another Data deduplication job already running on this volume.\r\n
0x80565364 | Data deduplication cannot run this job on this Csv volume on this node. Try running the job on the Csv volume resource owner node.\r\n
0x80565365 | Data deduplication failed to initialize cluster state on this node.\r\n
0x80565366 | Optimization of the range was aborted by the dedup filter driver.\r\n
0x80565367 | The operation could not be performed because of a concurrent IO operation.\r\n
0x80565368 | Data deduplication encountered an unexpected error. Verify deduplication is enabled on all nodes if in a cluster configuration. Check the Data Deduplication Operational event log for more information.\r\n
0x80565369 | Data access for data deduplicated CSV volumes can only be disabled when in maintenance mode. Check the Data Deduplication Operational event log for more information.\r\n
0x8056536a | Data Deduplication encountered an IO device error that may indicate a hardware fault in the storage subsystem.\r\n
0x8056536b | Data deduplication cannot run this cmdlet on this Csv volume on this node. Try running the cmdlet on the Csv volume resource owner node.\r\n
0x8056536c | Deduplication job not supported during rolling cluster upgrade.\r\n
0x8056536d | Deduplication setting not supported during rolling cluster upgrade.\r\n
0x8056536e | Data port job is not ready to accept requests.\r\n
0x8056536f | Data port request not accepted due to request count/size limit exceeded.\r\n
0x80565370 | Data port request completed with some errors. Check event logs for more details.\r\n
0x80565371 | Data port request failed. Check event logs for more details.\r\n
0x80565372 | Data port error accessing the hash index. Check event logs for more details.\r\n
0x80565373 | Data port error accessing the stream store. Check event logs for more details.\r\n
0x80565374 | Data port file stub error. Check event logs for more details.\r\n
0x80565375 | Data port encountered a deduplication filter error. Check event logs for more details.\r\n
0x80565376 | Data port cannot commit stream map due to missing chunk. Check event logs for more details.\r\n
0x80565377 | Data port cannot commit stream map due to invalid stream map metadata. Check event logs for more details.\r\n
0x80565378 | Data port cannot commit stream map due to invalid stream map entry. Check event logs for more details.\r\n
0x80565379 | Data port cannot retrieve job interface for volume. Check event logs for more details.\r\n
0x8056537a | The specified path is not supported.\r\n
0x8056537b | // Data port cannot decompress chunk. Check event logs for more details.\r\n
0x8056537c | Data port cannot calculate chunk hash. Check event logs for more details.\r\n
0x8056537d | Data port cannot read chunk stream. Check event logs for more details.\r\n
0x8056537e | The target file is not a deduplicated file. Check event logs for more details.\r\n
0x8056537f | The target file is partially recalled. Check event logs for more details.\r\n
0x90000001 | Data Deduplication\r\n
0x90000002 | Application\r\n
0x91000001 | Data Deduplication Change Events\r\n
0xb0001000 | Volume "%1" appears as disconnected and it is ignored by the service.  You may want to rescan disks.   Error: %2.%n%3\r\n
0xb0001001 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3". Most likely the CPU is under heavy load.  Error: %4.%n%5\r\n
0xb0001002 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3".  Error: %4.%n%5\r\n
0xb0001003 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3" during Safe Mode. The Data Deduplication service cannot start while in safe mode.  Error: %4.%n%5\r\n
0xb0001004 | A critical component required by Data Deduplication is not registered. This might happen if an error occurred during Windows setup, or if the computer does not have the Windows Server 2012 or later version of Deduplication service installed. The error returned from CoCreateInstance on class with CLSID %1 and Name "%2" on machine "%3" is %4.%n%5\r\n
0xb0001005 | Data Deduplication service is shutting down due to idle timeout.%n%1\r\n
0xb0001006 | Data Deduplication service is shutting down due to shutdown event from the Service Control Manager.%n%1\r\n
0xb0001007 | Data Deduplication job of type "%1" on volume "%2" has completed with return code: %3%n%4\r\n
0xb0001008 | Data Deduplication error: Unexpected error calling routine %1.  hr = %2.%n%3\r\n
0xb0001009 | Data Deduplication error: Unexpected error.%n%1\r\n
0xb000100a | Data Deduplication warning: %1%nError: %2.%n%3\r\n
0xb000100b | Data Deduplication error: Unexpected COM error %1: %2.  Error code: %3.%n%4\r\n
0xb000100c | Data Deduplication was unable to access the following file or volume: "%1".  This file or volume might be locked by another application right now, or you might need to give Local System access to it.%n%2\r\n
0xb000100d | Data Deduplication encountered an unexpected error during volume scan of volumes mounted at "%1" ("%2"). To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100e | Data Deduplication was unable to create or access the shadow copy for volumes mounted at "%1" ("%2"). Possible causes include an improper Shadow Copy configuration, insufficient disk space, or extreme memory, I/O or CPU load of the system. To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100f | Data Deduplication was unable to access volumes mounted at "%1" ("%2"). Make sure that dismount or format operations do not happen while running deduplication.%n%3\r\n
0xb0001010 | Data Deduplication was unable to access a file or volume. Details:%n%n%1%n The volume may be inaccessible for I/O operations or marked read-only. In case of a cluster volume, this may be a transient failure during failover.%n%2\r\n
0xb0001011 | Data Deduplication was unable to scan volume "%1" ("%2").%n%3\r\n
0xb0001012 | Data Deduplication detected a corruption on file "%1" at offset ("%2").  If this condition persists then please restore the data from a previous backup.  Corruption details: Structure=%3, Corruption type = %4, Additional data = %5%n%6\r\n
0xb0001013 | Data Deduplication encountered failure while reconciling chunk store on volume "%1". The error code was %2. Reconciliation is disabled for the current optimization job.%n%3\r\n
0xb0001016 | Data Deduplication encountered corrupted chunk container %1 while performing full garbage collection. The corrupted chunk container is skipped.%n%2\r\n
0xb0001017 | Data Deduplication could not initialize change log under %1. The error code was %2.%n%3\r\n
0xb0001018 | Data Deduplication service could not mark chunk container %1 as reconciled. The error code was %2.%n%3\r\n
0xb0001019 | A Data Deduplication configuration file is corrupted. The system or volume may need to be restored from backup.%n%1\r\n
0xb000101a | Data Deduplication was unable to save one of the configuration stores on volume "%1" due to a disk-full error: If the disk is full, please clean it up (extend the volume or delete some files). If the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.%n%2\r\n
0xb000101b | Data Deduplication could not access global configuration since the cluster service is not running. Please start the cluster service and retry the operation.%n%1\r\n
0xb000101c | Shadow copy "%1" was deleted during storage report generation.  Volume "%2" might be configured with inadequate shadow copy storage area. Data Deduplication could not process this volume.%n%3\r\n
0xb000101d | Shadow copy creation failed for volume "%1" after retrying for %2 minutes because other shadow copies were being created.  Reschedule the Data Deduplication for a less busy time.%n%3\r\n
0xb000101e | Volume "%1" is not supported for shadow copy.  It is possible that the volume was removed from the system.  Data Deduplication service could not process this volume.%n%2\r\n
0xb000101f | The volume "%1" has been deleted or removed from the system.%n%2\r\n
0xb0001020 | Shadow copy creation failed for volume "%1" with error %2.  The volume might be configured with inadequate shadow copy storage area.  File Serve Deduplication service could not process this volume.%n%3\r\n
0xb0001021 | The file system on volume "%1" is potentially corrupted.  Please run the CHKDSK utility to verify and fix the file system.%n%2\r\n
0xb0001022 | Data Deduplication detected an insecure internal folder. To secure the folder, reinstall deduplication on the volume again.%n%1\r\n
0xb0001023 | Data Deduplication could not find a chunk store on the volume.%n%1\r\n
0xb0001024 | Data Deduplication detected multiple chunk store folders. To recover, reinstall deduplication on the volume.%n%1\r\n
0xb0001025 | Data Deduplication detected conflicting chunk store folders: "%1" and "%2".%n%3\r\n
0xb0001026 | The data is invalid.%n%1\r\n
0xb0001027 | Data Deduplication scheduler failed to initialize with error "%1".%n%2\r\n
0xb0001028 | Data Deduplication failed to validate job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb0001029 | Data Deduplication failed to start job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb000102c | Data Deduplication detected job type "%1" on volume "%2" uses too much memory. %3 MB is assigned. %4 MB is used.%n%5\r\n
0xb000102d | Data Deduplication detected job type "%1" on volume "%2" memory usage has dropped to desirable level.%n%3\r\n
0xb000102e | Data Deduplication cancelled job type "%1" on volume "%2". It uses too much memory than the amount assigned to it.%n%3\r\n
0xb000102f | Data Deduplication cancelled job type "%1" on volume "%2". Memory resource is running low on the machine or in the job.%n%3\r\n
0xb0001030 | Data Deduplication job type "%1" on volume "%2" failed to report completion to the service with error: %3.%n%4\r\n
0xb0001031 | Data Deduplication detected a container cannot be compacted or updated because it has reached the maximum generation.%n%1\r\n
0xb0001032 | Data Deduplication corruption log "%1" is corrupted.%n%2\r\n
0xb0001033 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". Please run scrubbing job to process corruption log. No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001034 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001035 | Data Deduplication scheduler failed to uninitialize with error "%1".%n%2\r\n
0xb0001036 | Data Deduplication detected a new container could not be created in a chunk store because it ran out of available container Id.%n%1\r\n
0xb0001037 | Data Deduplication full garbage collection phase 1 (cleaning file related metadata) on volume "%1" failed with error: %2.  The job will continue with phase 2 execution (data chunk cleanup).%n%3\r\n
0xb0001039 | Data Deduplication full garbage collection could not achieve maximum space reclamation because delete logs for data container %1 could not be cleaned up.%n%2\r\n
0xb000103a | Some files could not be deduplicated because of FSRM Quota violations on volume %1. Files skipped are likely compressed or sparse files in folders which are at quota or close to their quota limit. Please consider increasing the quota limit for folders that are at their quota limit or close to it.%n%2\r\n
0xb000103b | Data Deduplication failed to dedup file %1 "%2" due to fatal error %3%n%4\r\n
0xb000103c | Data Deduplication encountered corruption while accessing a file in chunk store.%n%1\r\n
0xb000103d | Data Deduplication encountered corruption while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103e | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103f | Data Deduplication is unable to access file %1 because the file is in use.%n%2\r\n
0xb0001040 | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store.%n%1\r\n
0xb0001041 | Data Deduplication cannot run the job on volume %1 because the dedup store version compatiblity check failed with error %2.%n%3\r\n
0xb0001042 | Data Deduplication has disabled the volume %1 because it has discovered too many corruptions. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001043 | Data Deduplication has detected a corrupt corruption metadata file on the store at %1. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001044 | Volume "%1" cannot be enabled for Data Deduplication. Data Deduplication does not support volumes larger than 64TB. Error: %2.%n%3\r\n
0xb0001045 | Data Deduplication cannot be enabled on SIS volume "%1". Error: %2.%n%3\r\n
0xb0001046 | File-system is configured for case-sensitive file/folder names. Data Deduplication does not support case-sensitive file-system mode.%n%1\r\n
0xb0001049 | Data Deduplication changed scrubbing job to read-only due to insufficient disk space.%n%1\r\n
0xb000104b | Data Deduplication has disabled the volume %1 because there are missing or corrupt containers. Please run deep scrubbing on the volume.%n%2\r\n
0xb000104d | Data Deduplication encountered a disk-full error.%n%1\r\n
0xb000104e | Data Deduplication job cannot run on volume "%1" due to insufficient disk space.%n%2\r\n
0xb000104f | Data Deduplication job cannot run on offline volume "%1".%n%2\r\n
0xb0001050 | Data Deduplication recovered a corrupt or missing file.%n%1\r\n
0xb0001051 | Data Deduplication encountered a corrupted metadata file. To correct the problem, schedule or manually run a Garbage Collection job on the affected volume with the -Full option.%n%1\r\n
0xb0001052 | Data Deduplication encountered chunk %1 with corrupted header while updating container. The corrupted chunk is replicated to the new container %2.%n%3\r\n
0xb0001053 | Data Deduplication encountered chunk %1 with transient header corruption while updating container. The corrupted chunk is NOT replicated to the new container %2.%n%3\r\n
0xb0001054 | Data Deduplication failed to read chunk container redirection table from file %1 with error %2.%n%3\r\n
0xb0001055 | Data Deduplication failed to initialize reparse point index table for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001056 | Data Deduplication failed to deep scrub container file %1 on volume %2 with error %3.%n%4\r\n
0xb0001057 | Data Deduplication failed to load stream map log for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001058 | Data Deduplication found a duplicate local chunk id %1 in container file %2.%n%3\r\n
0xb0001059 | Data Deduplication job type "%1" on volume "%2" was cancelled manually.%n%3\r\n
0xb000105a | Scheduled data Deduplication job type "%1" on volume "%2" was cancelled.%n%3\r\n
0xb000105d | The Data Deduplication chunk store statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105e | The Data Deduplication volume statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105f | Data Deduplication failed to append to deep scrubbing log file %1 with error %2.%n%3\r\n
0xb0001060 | Data Deduplication encountered a failure during deep scrubbing on store %1 with error %2.%n%3\r\n
0xb0001061 | Data Deduplication cancelled job type "%1" on volume "%2". The job violated Csv dedup job placement policy.%n%3\r\n
0xb0001062 | Data Deduplication cancelled job type "%1" on volume "%2". The csv job monitor has been uninitialized.%n%3\r\n
0xb0001063 | Data Deduplication encountered a IO device error while accessing a file on the volume. This is likely a hardware fault in the storage subsystem.%n%1\r\n
0xb0001064 | Data Deduplication encountered an unexpected error. If this is a cluster, verify Data Deduplication is enabled on all nodes of the cluster.%n%1\r\n
0xb0001065 | Attempted to disable data access for data deduplicated CSV volume "%1" without maintenance mode. Data access can only be disabled for a CSV volume when in maintenance mode. Place volume into maintenance mode and retry.%n%2\r\n
0xb0001800 | Data Deduplication service could not unoptimize file "%5%6%7". Error %8, "%9".\r\n
0xb0001801 | Data Deduplication service failed to unoptimize too many files %3. Some files are not reported.\r\n
0xb0001802 | Data Deduplication service has finished unoptimization on volume %3 with no errors.\r\n
0xb0001803 | Data Deduplication service has finished unoptimization on volume %3 with %4 errors.\r\n
0xb0001804 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb0001805 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nPriority: %7%nFull: %8%nVolume free space (MB): %9\r\n
0xb0001806 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6%nFull: %7%nRead-only: %8\r\n
0xb0001807 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6\r\n
0xb0001809 | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate (percent): %7%nSaved space (MB): %8%nVolume used space (MB): %9%nVolume free space (MB): %10%nOptimized file count: %11%nIn-policy file count: %12%nJob processed space (MB): %13%nJob elapsed time (seconds): %18%nJob throughput (MB/second): %19%nChurn processing throughput (MB/second): %20\r\n
0xb000180a | %1 job has completed.%n%nFull: %2%nVolume: %5 (%4)%nError code: %6%nError message: %7%nFreed up space (MB): %8%nVolume free space (MB): %9%nJob elapsed time (seconds): %10%nJob throughput (MB/second): %11\r\n
0xb000180b | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6\r\n
0xb000180c | %1 job has completed.%n%nFull: %2%nRead-only: %3%nVolume: %6 (%5)%nError code: %7%nError message: %8%nTotal corruption count: %9%nFixable corruption count: %10%n%nWhen corruptions are found, check more details in Scrubbing event channel.\r\n
0xb000180d | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nUnoptimized file count: %7%nJob processed space (MB): %8%nJob elapsed time (seconds): %9%nJob throughput (MB/second): %10\r\n
0xb000180e | %1 job has been queued.%n%nVolume: %4 (%3)%nSystem memory percent: %5 %nPriority: %6%nSchedule mode: %7\r\n
0xb000181c | Restore of deduplicated file "%1" failed with the following error: %2, "%3".\r\n
0xb000181d | Priority %1 job has started.%n%nVolume: %4 (%3)%nFile ID: %11%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb000181e | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable threads: %6%nPriority: %7\r\n
0xb000181f | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate (percent): %7%nSaved space (MB): %8%nVolume used space (MB): %9%nVolume free space (MB): %10%nOptimized file count: %11%nChunk lookup count: %12%nInserted chunk count: %13%nInserted chunks logical data (MB): %14%nInserted chunks physical data (MB): %15%nCommitted stream count: %16%nCommitted stream entry count: %17%nCommitted stream logical data (MB): %18%nRetrieved chunks physical data (MB): %19%nRetrieved stream logical data (MB): %20%nDataPort time (seconds): %21%nJob elapsed time (seconds): %22%nIngress throughput (MB/second): %23%nEgress throughput (MB/second): %24\r\n
0xb0001821 | Data Deduplication detected a non-clustered volume specified for the chunk index cache volume in a clustered deployment. The configuration is not recommended because it may result in job failures after failover.%n%nVolume: %3 (%2)\r\n
0xb0001822 | DataPort status update.  %n%nVolume: %2%nSavings rate (percent): %3%nSaved space (MB): %4%nVolume used space (MB): %5%nVolume free space (MB): %6%nOptimized file count: %7%nChunk lookup count: %8%nInserted chunk count: %9%nInserted chunks logical data (MB): %10%nInserted chunks physical data (MB): %11%nCommitted stream count: %12%nCommitted stream entry count: %13%nCommitted stream logical data (MB): %14%nRetrieved chunks physical data (MB): %15%nRetrieved stream logical data (MB): %16%nDataPort time (seconds): %17%nJob elapsed time (seconds): %18%nIngress throughput (MB/second): %19%nEgress throughput (MB/second): %20\r\n
0xb0002000 | Data Deduplication detected job type "%1" on volume "%2" working set is low. Ratio to commit size is %3.%n%4\r\n
0xb0002001 | Data Deduplication detected job type "%1" on volume "%2" working set has recovered to desirable level.%n%3\r\n
0xb0002002 | Data Deduplication detected job type "%1" on volume "%2" page fault rate is high. The rate is %3 page faults per second.%n%4\r\n
0xb0002003 | Data Deduplication detected job type "%1" on volume "%2" page fault rate has lowered to desirable level. The rate is %3 page faults per second.%n%4\r\n
0xb0002004 | Data Deduplication failed to dedup file "%1" with file ID %2 due to non-fatal error %3%n%4.%n%nNote: You can retrieve the file name by running the command FSUTIL FILE QUERYFILENAMEBYID on the file in question.\r\n
0xb000200c | Data Deduplication has aborted a group commit session.%n%nFile count: %1%nError: %2%n%3\r\n
0xb000201c | Fail to open dedup setting registry key\r\n
0xb000201d | Data Deduplication failed to dedup file "%1" with file ID %2 due to oplock break%n%3\r\n
0xb000201e | Data Deduplication failed to load hotspot table from file %1 due to error %2.%n%3\r\n
0xb000201f | Data Deduplication failed to initialize oplock.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb0002020 | Data Deduplication while running job on volume %1 detected invalid physical sector size %2. Using default value %3.%n%4\r\n
0xb0002021 | Data Deduplication detected an unsupported chunk store container.%n%1\r\n
0xb0002022 | Data Deduplication could not create window to receive task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002023 | Data Deduplication could not create thread to poll for task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002024 | An attempt was made to perform an initialization operation when initialization has already been completed.%n%1\r\n
0xb0002028 | Data Deduplication created emergency file %1.%n%3\r\n
0xb0002029 | Data Deduplication failed to create emergency file %1 with error %2.%n%3\r\n
0xb000202a | Data Deduplication deleted emergency file %1.%n%3\r\n
0xb000202b | Data Deduplication failed to delete emergency file %1 with error %2.%n%3\r\n
0xb000202c | Data Deduplication detected a chunk store container with misaligned valid data length.%n%1\r\n
0xb000202d | Data Deduplication Garbage Collection encountered a delete log entry with an invalid stream map signature for stream map Id %1.%n%2\r\n
0xb000202e | Data Deduplication failed to initialize oplock as the file appears to be missing.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb000202f | Data Deduplication skipped too many file-level errors. We will not log more than %1 file-level errors per job.%n%2\r\n
0xb0002030 | Data Deduplication diagnostic warning.%n%n%1%n%2\r\n
0xb0002031 | Data Deduplication diagnostic information.%n%n%1%n%2\r\n
0xb0002032 | Data Deduplication found file %1 with a stream map id %2 in container file %3 marked for deletion.%n%4\r\n
0xb0002033 | Failed to enqueue job of type "%1" on volume "%2".%n%3\r\n
0xb0002034 | Error terminating job host process for job type "%1" on volume "%2" (process id: %3).%n%4\r\n
0xb0002035 | Data Deduplication encountered corrupted chunk %1 while updating container. Corrupted data that cannot be repaired will be copied as-is to the new container %2.%n%3\r\n
0xb0002036 | Data Deduplication job type "%1" on volume "%2" failed to exit gracefully.%n%3\r\n
0xb0002037 | Data Deduplication job host for job type "%1" on volume "%2" exited unexpectedly.%n%3\r\n
0xb0002038 | Data Deduplication has failed to load corruption metadata file on the store at %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb0002039 | Data Deduplication full garbage collection phase 1 on volume "%1" encountered an error %2 while processing file %3. Phase 1 will need to be aborted since garbage collection of file-related metadata is unsafe to continue on file errors.%n%4\r\n
0xb000203a | Data Deduplication has failed to process corruption metadata file %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb000203b | Data Deduplication has failed to load a corrupted metadata file %1 due to error %2. Deleting the file and continuing.%n%3\r\n
0xb000203c | Data Deduplication has failed to set NTFS allocation size for container file %1 due to error %2.%n%3\r\n
0xb000203d | Data Deduplication configured to use BCrypt provider '%1' for hash algorithm %2.%n%3\r\n
0xb000203e | Data Deduplication could not use BCrypt provider '%1' for hash algorithm %2 due to an error in operation %3. Reverting to the Microsoft primitive CNG provider.%n%4\r\n
0xb000203f | Data Deduplication failed to include file "%1" in file metadata analysis calculations.%n%2\r\n
0xb0002040 | Data Deduplication failed to include stream map %1 in file metadata analysis calculations.%n%2\r\n
0xb0002041 | Data Deduplication encountered an error for file "%1" while scanning files and folders.%n%2\r\n
0xb0002042 | Data Deduplication encountered an error while attempting to resume processing. Please consult the event log parameters for more details about the current file being processed.%n%1\r\n
0xb0002043 | Data Deduplication encountered an error %1 whle scanning usn journal on volume %2 for updating hot range tracking.%n%3\r\n
0xb0002044 | Data Deduplication could not truncate the stream of an optimized file. No action is required. Error: %1%n%n%2\r\n
0xb0002800 | %1 job memory requirements.%n%nVolume: %4 (%3)%nMinimum memory: %5 MB%nMaximum memory: %6 MB%nMinimum disk: %7 MB%nMaximum cores: %8\r\n
0xb0002801 | %1 reconciliation has started.%n%nVolume: %4 (%3)\r\n
0xb0002802 | %1 reconciliation has completed.%n%nGuidance: This event is expected when Reconciliation has completed, there is no recommended or required action. Reconciliation is an internal process that allows Optimization and DataPort jobs to run when the entire Deduplication chunk index cannot be loaded into memory. %n%nVolume: %4 (%3)%nReconciled containers: %5%nUnreconciled containers: %6%nCatchup references: %7%nCatchup containers: %8%nReconciled references: %9%nReconciled containers: %10%nCross-reconciled references: %11%nCross-reconciled containers: %12%nError code: %13%nError message: %14\r\n
0xb0002803 | %1 job on volume %4 (%3) was configured with insufficient memory.%n%nSystem memory percentage: %5%nAvailable memory: %8 MB%nMinimum required memory: %6 MB\r\n
0xb0002804 | Optimization memory details for %1 job on volume %3 (%2).\r\n
0xb0002805 | An open file was skipped during optimization. No action is required.%n%nFileId: %2%nSkip Reason: %1\r\n
0xb0002806 | An operation succeeded after one or more retries. Operation: %1; FileId: %3; Number of retries: %2\r\n
0xb0002807 | Data Deduplication aborted the optimization pipeline.%nVolumePath: %1%nErrorCode: %2%nErrorMessage: %3Details: %4\r\n
0xb0002808 | Data Deduplication aborted a file.%nFileId: %1%nFilePath: %2%nFileSize: %3%nFlags: %4%nTotalRanges: %5%nSkippedRanges: %6%nAbortedRanges: %7%nCommittedRanges: %8%nErrorCode: %9%nErrorMessage: %10Details: %11\r\n
0xb0002809 | Data Deduplication aborted a file range.%nFileId: %1%nFilePath: %2%nRangeOffset: %3%nRangeLength: %4%nErrorCode: %5%nErrorMessage: %6Details: %7\r\n
0xb000280a | Data Deduplication aborted a session.%nMaxSize: %1%nCurrentSize: %2%nRemainingRanges: %3%nErrorCode: %4%nErrorMessage: %5Details: %6\r\n
0xb000280b | USN journal created.%n%nVolume: %2 (%1)%nMaximum size %3 MB%nAllocation size %4 MB\r\n
0xb000280c | DataPort memory details for %1 job on volume %3 (%2).\r\n
0xb000280d | Data deduplication detected a file with an ID that is not supported.  Files with identifiers unpackable into 64-bits will be skipped. FileId: %1 FileName: %2\r\n
0xb000280e | Reconciliation should be run to ensure optimal savings.%n%nGuidance: This event is expected when Reconciliation is turned off for the DataPort job. Reconciliation is an internal process that allows Optimization and DataPort jobs to run when the entire Deduplication chunk index cannot be loaded into memory. When Reconciliation would require 50% or more of the memory on the system, it is recommended that you (temporarily) cease running a DataPort job against this volume, and run an Optimization job. If Reconciliation is not run through an Optimization job before Reconciliation would require more than 100% of system memory, Reconciliation will not be able to be run again (unless more memory is added). This would result in permanent decreased space efficiency on this volume.%n%nVolume: %2 (%1)%nMemory percentage required: %3\r\n
0xb000280f | Data Deduplication optimization job will not run the reconciliation step due to inadequate memory.%n%nGuidance: Deduplication savings will be suboptimal until the optimization job is provided more memory, or more more memory is added to the system.%n%nVolume: %2 (%1)%nMemory percentage required: %3\r\n
0xb0003200 | Data Deduplication service detected corruption in "%5%6%7". The corruption cannot be repaired.\r\n
0xb0003201 | Data Deduplication service detected corruption (%7) in "%6". See the event details for more information.\r\n
0xb0003202 | Data Deduplication service detected a corrupted item (%11 - %13, %8, %9, %10, %12) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003203 | Data Deduplication service has finished scrubbing on volume %3. It did not find any corruption since the last scrubbing.\r\n
0xb0003204 | Data Deduplication service found %4 corruption(s) on volume %3. All corruptions are fixed.\r\n
0xb0003205 | Data Deduplication service found %4 corruption(s) on volume %3. %5 corruption(s) are fixed. %6 user file(s) are corrupted. %7 user file(s) are fixed. For the corrupted file list, see the Microsoft/Windows/Deduplication/Scrubbing events.\r\n
0xb0003206 | Data Deduplication service found too many corruptions on volume %3. Some corruptions are not reported.\r\n
0xb0003211 | Data Deduplication service has finished scrubbing on volume %3. See the event details for more information.\r\n
0xb0003212 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003213 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003214 | Data Deduplication service encountered error while detecting corruptions in chunk store on volume %3. The error was %4. The job is aborted.\r\n
0xb0003216 | Data Deduplication service encountered error while loading corruption logs on volume %3. The error was %4. The job continues. Some corruptions may not be detected.\r\n
0xb0003217 | Data Deduplication service encountered error while cleaning up corruption logs on volume %3. The error was %4. Some corruptions may be reported again next time.\r\n
0xb0003218 | Data Deduplication service encountered error while loading hotspots mapping from chunk store on volume %3. The error was %4. Some corruptions may not be repaired.\r\n
0xb0003219 | Data Deduplication service encountered error while determining corrupted user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb000321a | Data Deduplication service found %4 corruption(s) on volume %3. %6 user file(s) are corrupted. %7 user file(s) are fixable. Please run scrubbing job in read-write mode to attempt fixing reported corruptions.\r\n
0xb000321b | Data Deduplication service fixed corruption in "%5%6%7".\r\n
0xb000321c | Data Deduplication service detected fixable corruption in "%5%6%7". Please run scrubbing job in read-write mode to fix this corruption.\r\n
0xb000321e | Data Deduplication service encountered error while repairing corruptions on volume %3. The error was %4. The repair is unsuccessful.\r\n
0xb000321f | Data Deduplication service detected a corrupted item (%6, %7, %8, %9) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003220 | Container (%8,%9) with user data is missing from the chunk store. Missing container may result from incomplete restore, incomplete migration or file-system corruption. Volume is disabled from further optimization. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0003221 | Data Deduplication service encountered error while scaning dedup user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb0003222 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003223 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003224 | Data Deduplication service detected potential data loss (%9) in "%6" due to sharing reparse data with file "%8". See the event details for more information.\r\n
0xb0003225 | Container (%8,%9) with user data is corrupt in the chunk store. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0005000 | Open stream store stream (StartingChunkId %1, FileId %2)\r\n
0xb0005001 | Open stream store stream completed %1\r\n
0xb0005002 | Prepare for paging IO (Stream %1, FileId %2)\r\n
0xb0005003 | Prepare for paging IO completed %1\r\n
0xb0005005 | Read stream map completed %1\r\n
0xb0005006 | Read chunks (Stream %1, FileId %2, IoType %3, FirstRequestChunkId %4, NextRequest %5)\r\n
0xb0005007 | Read chunks completed %1\r\n
0xb0005008 | Compute checksum (ItemType %1, DataSize %2)\r\n
0xb0005009 | Compute checksum completed %1\r\n
0xb000500a | Get container entry (ContainerId %1, Generation %2)\r\n
0xb000500b | Get container entry completed %1\r\n
0xb000500c | Get maximum generation for container (ContainerId %1, Generation %2)\r\n
0xb000500d | Get maximum generation for container completed %1\r\n
0xb000500e | Open chunk container (ContainerId %1, Generation %2, RootPath %4)\r\n
0xb000500f | Open chunk container completed %1\r\n
0xb0005010 | Initialize chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005011 | Initialize chunk container redirection table completed %1\r\n
0xb0005012 | Validate chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005013 | Validate chunk container redirection table completed %1\r\n
0xb0005014 | Get chunk container valid data length (ContainerId %1, Generation %2)\r\n
0xb0005015 | Get chunk container valid data length completed %1\r\n
0xb0005016 | Get offset from chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005017 | Get offset from chunk container redirection table completed %1\r\n
0xb0005018 | Read chunk container block (ContainerId %1, Generation %2, Buffer %3, Offset %4, Length %5, IoType %6, Synchronous %7)\r\n
0xb0005019 | Read chunk container block completed %1\r\n
0xb000501a | Clear chunk container block (Buffer %1, Size %2, BufferType %3)\r\n
0xb000501b | Clear chunk container block completed %1\r\n
0xb000501c | Copy chunk (Buffer %1, Size %2, BufferType %3, BufferOffset %4, OutputCapacity %5)\r\n
0xb000501d | Copy chunk completed %1\r\n
0xb000501e | Initialize file cache (UnderlyingFileObject %1, CacheFileSize %2)\r\n
0xb000501f | Initialize file cache completed %1\r\n
0xb0005020 | Map file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005021 | Map file cache data completed %1\r\n
0xb0005022 | Unpin file cache data(Bcb %1)\r\n
0xb0005023 | Unpin file cache data completed %1\r\n
0xb0005024 | Copy file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005025 | Copy file cache data completed %1\r\n
0xb0005026 | Read underlying file cache data (CacheFileObject %1, UnderlyingFileObject %2, Offset %3, Length %4)\r\n
0xb0005027 | Read underlying file cache data completed %1\r\n
0xb0005028 | Get chunk container file size (ContainerId %1, Generation %2)\r\n
0xb0005029 | Get chunk container file size completed %1\r\n
0xb000502a | Pin stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb000502b | Pin stream map completed %1\r\n
0xb000502c | Pin chunk container (ContainerId %1, Generation %2)\r\n
0xb000502d | Pin chunk container completed %1\r\n
0xb000502e | Pin chunk (ContainerId %1, Generation %2)\r\n
0xb000502f | Pin chunk completed %1\r\n
0xb0005030 | Allocate pool buffer (ReadLength %1, PagingIo %2)\r\n
0xb0005031 | Allocate pool buffer completed %1\r\n
0xb0005032 | Unpin chunk container (ContainerId %1, Generation %2)\r\n
0xb0005033 | Unpin chunk container completed %1\r\n
0xb0005034 | Unpin chunk (ContainerId %1, Generation %2)\r\n
0xb0005035 | Unpin chunk completed %1\r\n
0xb0006028 | Dedup read processing (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006029 | Dedup read processing completed %1\r\n
0xb000602a | Get first stream map entry (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602b | Get first stream map entry completed %1\r\n
0xb000602c | Read chunk metadata (Stream %1, CurrentOffset %2, AdjustedFinalOffset %3, FirstChunkByteOffset %4, ChunkRequestsEndOffset %5, TlCache %6)\r\n
0xb000602d | Read chunk metadata completed %1\r\n
0xb000602e | Read chunk data (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602f | Read chunk data completed %1\r\n
0xb0006030 | Reference TlCache data (TlCache %1, Stream %2)\r\n
0xb0006031 | Reference TlCache data completed %1\r\n
0xb0006032 | Read chunk data from stream store (Stream %1)\r\n
0xb0006033 | Read chunk data from stream store completed %1\r\n
0xb0006034 | Assemble chunk data\r\n
0xb0006035 | Assemble chunk data completed %1\r\n
0xb0006036 | Decompress chunk data\r\n
0xb0006037 | Decompress chunk data completed %1\r\n
0xb0006038 | Copy chunk data in to user buffer (BytesCopied %1)\r\n
0xb0006039 | Copy chunk data in to user buffer completed %1\r\n
0xb000603a | Insert chunk data in to tlcache\r\n
0xb000603b | Insert chunk data in to tlcache completed %1\r\n
0xb000603c | Read data from dedup reparse point file (FileObject %1, Offset %2, Length %3)\r\n
0xb000603d | Read underlying file cache data completed %1\r\n
0xb000603e | Prepare stream map (StreamContext %1)\r\n
0xb000603f | Prepare stream map completed %1\r\n
0xb0006040 | Patch clean ranges (FileObject %1, Offset %2, Length %3)\r\n
0xb0006041 | Patch clean ranges completed %1\r\n
0xb0006042 | Writing data to dedup file (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006043 | Writing data to dedup file completed %1\r\n
0xb0006044 | Queue write request on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006045 | Queue write request on dedup file completed %1\r\n
0xb0006046 | Do copy on write work on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006047 | Do copy on write work on dedup file completed %1\r\n
0xb0006048 | Do full recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006049 | Do full recall on dedup file completed %1\r\n
0xb000604a | Do partial recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604b | Do partial recall on dedup file completed %1\r\n
0xb000604c | Do dummy paging read on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604d | Do dummy paging read on dedup file completed %1\r\n
0xb000604e | Read clean data for recalling file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604f | Read clean data for recalling file completed %1\r\n
0xb0006050 | Write clean data to dedup file normally (FileObject %1, Offset %2, Length %3)\r\n
0xb0006051 | Write clean data to dedup file completed %1\r\n
0xb0006052 | Write clean data to dedup file paged (FileObject %1, Offset %2, Length %3)\r\n
0xb0006053 | Write clean data to dedup file paged completed %1\r\n
0xb0006054 | Recall dedup file using paging Io (FileObject %1, Offset %2, Length %3)\r\n
0xb0006055 | Recall dedup file using paging Io completed %1\r\n
0xb0006056 | Flush dedup file after recall (FileObject %1)\r\n
0xb0006057 | Flush dedup file after recall completed %1\r\n
0xb0006058 | Update bitmap after recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006059 | Update bitmap after recall on dedup file completed %1\r\n
0xb000605a | Delete dedup reparse point (FileObject %1)\r\n
0xb000605b | Delete dedup reparse point completed %1\r\n
0xb000605c | Open dedup file (FilePath %1)\r\n
0xb000605d | Open dedup file completed %1\r\n
0xb000605e | Locking user buffer for read\r\n
0xb000605f | Locking user buffer for read completed %1\r\n
0xb0006060 | Get system address for MDL\r\n
0xb0006061 | Get system address for MDL completed %1\r\n
0xb0006062 | Read clean dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006063 | Read clean dedup file completed %1\r\n
0xb0006064 | Get range state (Offset %1, Length %2)\r\n
0xb0006065 | Get range state completed %1\r\n
0xb0006066 | Get chunk body\r\n
0xb0006067 | Get chunk body completed %1\r\n
0xb0006068 | Release chunk\r\n
0xb0006069 | Release chunk completed %1\r\n
0xb000606a | Release decompress chunk context (BufferSize %1)\r\n
0xb000606b | Release decompress chunk context completed %1\r\n
0xb000606c | Prepare decompress chunk context (BufferSize %1)\r\n
0xb000606d | Prepare decompress chunk context completed %1\r\n
0xb000606e | Copy data to compressed buffer (BufferSize %1)\r\n
0xb000606f | Copy data to compressed buffer completed %1\r\n
0xb0006070 | Release data from TL Cache\r\n
0xb0006071 | Release data from TL Cache completed %1\r\n
0xb0006072 | Queue async read request (FileObject %1, Offset %2, Length %3)\r\n
0xb0006073 | Queue async read request complete %1\r\n
0xb0015004 | Read stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb1004000 | Create chunk container (%1 - %2.%3.ccc)\r\n
0xb1004001 | Create chunk container completed %1\r\n
0xb1004002 | Copy chunk container (%1 - %2.%3.ccc)\r\n
0xb1004003 | Copy chunk container completed %1\r\n
0xb1004004 | Delete chunk container (%1 - %2.%3.ccc)\r\n
0xb1004005 | Delete chunk container completed %1\r\n
0xb1004006 | Rename chunk container (%1 - %2.%3.ccc%4)\r\n
0xb1004007 | Rename chunk container completed %1\r\n
0xb1004008 | Flush chunk container (%1 - %2.%3.ccc)\r\n
0xb1004009 | Flush chunk container completed %1\r\n
0xb100400a | Rollback chunk container (%1 - %2.%3.ccc)\r\n
0xb100400b | Rollback chunk container completed %1\r\n
0xb100400c | Mark chunk container (%1 - %2.%3.ccc) read-only\r\n
0xb100400d | Mark chunk container read-only completed %1\r\n
0xb100400e | Write chunk container (%1 - %2.%3.ccc) redirection table at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb100400f | Write chunk container redirection table completed %1\r\n
0xb1004011 | Write chunk container header completed %1\r\n
0xb1004013 | Insert data chunk header completed %1\r\n
0xb1004015 | Insert data chunk body completed %1 with ChunkId %2\r\n
0xb1004019 | Write delete log header completed %1\r\n
0xb100401b | Append delete log entries completed %1\r\n
0xb100401d | Delete delete log completed %1\r\n
0xb100401f | Rename delete log completed %1\r\n
0xb1004021 | Write chunk container bitmap completed %1\r\n
0xb1004023 | Delete chunk container bitmap completed %1\r\n
0xb1004024 | Write merge log (%5 - %6.%7.merge.log) header\r\n
0xb1004025 | Write merge log header completed %1\r\n
0xb1004027 | Insert hotspot chunk header completed %1\r\n
0xb1004029 | Insert hotspot chunk body completed %1 with ChunkId %2\r\n
0xb100402b | Insert stream map chunk header completed %1\r\n
0xb100402d | Insert stream map chunk body completed %1 with ChunkId %2\r\n
0xb100402f | Append merge log entries completed %1\r\n
0xb1004030 | Delete merge log (%1 - %2.%3.merge.log)\r\n
0xb1004031 | Delete merge log completed %1\r\n
0xb1004032 | Flush merge log (%1 - %2.%3.merge.log)\r\n
0xb1004033 | Flush merge log completed %1\r\n
0xb1004034 | Update file list entries (Remove: %1, Add: %2)\r\n
0xb1004035 | Update file list entries completed %1\r\n
0xb1004036 | Set dedup reparse point on %2 (FileId %1) (ReparsePoint: SizeBackedByChunkStore %3, StreamMapInfoSize %4, StreamMapInfo %5)\r\n
0xb1004037 | Set dedup reparse point completed %1 (%2)\r\n
0xb1004038 | Set dedup zero data on %2 (FileId %1)\r\n
0xb1004039 | Set dedup zero data completed %1\r\n
0xb100403a | Flush reparse point files\r\n
0xb100403b | Flush reparse point files completed %1\r\n
0xb100403c | Set sparse on file id %1\r\n
0xb100403d | Set sparse completed %1\r\n
0xb100403e | FSCTL_SET_ZERO_DATA on file id %1 at offset %2 and BeyondFinalZero %3\r\n
0xb100403f | FSCTL_SET_ZERO_DATA completed %1\r\n
0xb1004040 | Rename chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1004041 | Rename chunk container bitmap completed %1\r\n
0xb1004042 | Insert padding chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1004043 | Insert padding chunk header completed %1\r\n
0xb1004044 | Insert padding chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1004045 | Insert padding chunk body completed %1 with ChunkId %2\r\n
0xb1004046 | Insert batch of chunks to chunk container (%1 - %2.%3.ccc) at offset %4 (BatchChunkCount %5, BatchDataSize %6)\r\n
0xb1004047 | Insert batch of chunks completed %1\r\n
0xb1004049 | Write chunk container directory completed %1\r\n
0xb100404b | Delete chunk container directory completed %1\r\n
0xb100404c | Rename chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb100404d | Rename chunk container directory completed %1\r\n
0xb1014010 | Write chunk container (%5 - %6.%7.ccc) header at offset %8 (Header: USN %9, VDL %10, #Chunk %11, NextLocalId %12, Flags %13, LastAppendTime %14, BackupRedirectionTableOfset %15, LastReconciliationLocalId %16)\r\n
0xb1014012 | Insert data chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1014014 | Insert data chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014018 | Write delete log (%5 - %6.%7.delete.log) header\r\n
0xb101401a | Append delete log (%1 - %2.%3.delete.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb101401c | Delete delete log (%1 - %2.%3.delete.log)\r\n
0xb101401e | Rename delete log (%1 - %2.%3.delete.log)\r\n
0xb1014020 | Write chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4) (Bitmap: BitLength %5, StartIndex %6, Count %7)\r\n
0xb1014022 | Delete chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1014026 | Insert hotspot chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014028 | Insert hotspot chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb101402a | Insert stream map chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014048 | Write chunk container directory (%1 - %2) for chunk container (%1 - %3.%4) (Directory: EntryCount %5)\r\n
0xb101404a | Delete chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb102402e | Append merge log (%1 - %2.%3.merge.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb103402c | Insert stream map chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7) (Entries: StartIndex %8, Count %9)\r\n
0xd0000001 | Chunk header\r\n
0xd0000002 | Chunk body\r\n
0xd0000003 | Container header\r\n
0xd0000004 | Container redirection table\r\n
0xd0000005 | Hotspot table\r\n
0xd0000006 | Delete log header\r\n
0xd0000007 | Delete log entry\r\n
0xd0000008 | GC bitmap header\r\n
0xd0000009 | GC bitmap entry\r\n
0xd000000a | Merge log header\r\n
0xd000000b | Merge log entry\r\n
0xd000000c | Data\r\n
0xd000000d | Stream map\r\n
0xd000000e | Hotspot\r\n
0xd000000f | Optimization\r\n
0xd0000010 | Garbage Collection\r\n
0xd0000011 | Scrubbing\r\n
0xd0000012 | Unoptimization\r\n
0xd0000013 | Analysis\r\n
0xd0000014 | Low\r\n
0xd0000015 | Normal\r\n
0xd0000016 | High\r\n
0xd0000017 | Cache\r\n
0xd0000018 | Non-cache\r\n
0xd0000019 | Paging\r\n
0xd000001a | Memory map\r\n
0xd000001b | Paging memory map\r\n
0xd000001c | None\r\n
0xd000001d | Pool\r\n
0xd000001e | PoolAligned\r\n
0xd000001f | MDL\r\n
0xd0000020 | Map\r\n
0xd0000021 | Cached\r\n
0xd0000022 | NonCached\r\n
0xd0000023 | Paged\r\n
0xd0000024 | container file\r\n
0xd0000025 | file list file\r\n
0xd0000026 | file list header\r\n
0xd0000027 | file list entry\r\n
0xd0000028 | primary file list file\r\n
0xd0000029 | backup file list file\r\n
0xd000002a | Scheduled\r\n
0xd000002b | Manual\r\n
0xd000002c | recall bitmap header\r\n
0xd000002d | recall bitmap body\r\n
0xd000002e | recall bitmap missing\r\n
0xd000002f | Recall bitmap\r\n
0xd0000030 | Unknown\r\n
0xd0000031 | The pipeline handle was closed\r\n
0xd0000032 | The file was deleted\r\n
0xd0000033 | The file was overwritten\r\n
0xd0000034 | The file was recalled\r\n
0xd0000035 | A transaction was started on the file\r\n
0xd0000036 | The file was encrypted\r\n
0xd0000037 | The file was compressed\r\n
0xd0000038 | Set Zero Data was called on the file\r\n
0xd0000039 | Extended Attributes were set on the file\r\n
0xd000003a | A section was created on the file\r\n
0xd000003b | The file was shrunk\r\n
0xd000003c | A long-running IO operation prevented optimization\r\n
0xd000003d | An IO operation failed\r\n
0xd000003e | Notifying Optimization\r\n
0xd000003f | Setting the Reparse Point\r\n
0xd0000040 | Truncating the file\r\n
0xd0000041 | DataPort\r\n
0xd1000001 | None\r\n
0xd1000002 | LZNT1\r\n
0xd1000003 | Xpress\r\n
0xd1000004 | Xpreff Huff\r\n
0xd1000005 | None\r\n
0xd1000006 | Standard\r\n
0xd1000007 | Max\r\n
0xd1000008 | Hybrid\r\n
0xf0000001 | None\r\n
0xf0000002 | Bad checksum\r\n
0xf0000003 | Inconsistent metadata\r\n
0xf0000004 | Invalid header metadata\r\n
0xf0000005 | Missing file\r\n
0xf0000006 | Bad checksum (storage subsystem)\r\n
0xf0000007 | Corruption (storage subsystem)\r\n
0xf0000008 | Corruption (missing metadata)\r\n
0xf0000009 | Possible data loss (duplicate reparse data)\r\n

### 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x00565301 | Reconciliation of chunk store is due.\r\n
0x00565302 | There are no actions associated with this job.\r\n
0x00565303 | Data deduplication cannot runing this job on this Csv volume on this node.\r\n
0x00565304 | Data deduplication cannot runing this cmdlet on this Csv volume on this node.\r\n
0x10000001 | Reporting\r\n
0x10000002 | Filter\r\n
0x10000003 | Kernel mode stream store\r\n
0x10000004 | Kernel mode chunk store\r\n
0x10000005 | Kernel mode chunk container\r\n
0x10000006 | Kernel mode file cache\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Data Deduplication Optimization Task\r\n
0x70000002 | Data Deduplication Garbage Collection Task\r\n
0x70000003 | Data Deduplication Scrubbing Task\r\n
0x70000004 | Data Deduplication Unoptimization Task\r\n
0x70000005 | Open stream store stream\r\n
0x70000006 | Prepare for paging IO\r\n
0x70000007 | Read stream map\r\n
0x70000008 | Read chunks\r\n
0x70000009 | Compute checksum\r\n
0x7000000a | Get container entry\r\n
0x7000000b | Get maximum generation for container\r\n
0x7000000c | Open chunk container\r\n
0x7000000d | Initialize chunk container redirection table\r\n
0x7000000e | Validate chunk container redirection table\r\n
0x7000000f | Get chunk container valid data length\r\n
0x70000010 | Get offset from chunk container redirection table\r\n
0x70000011 | Read chunk container block\r\n
0x70000012 | Clear chunk container block\r\n
0x70000013 | Copy chunk\r\n
0x70000014 | Initialize file cache\r\n
0x70000015 | Map file cache data\r\n
0x70000016 | Unpin file cache data\r\n
0x70000017 | Copy file cache data\r\n
0x70000018 | Read underlying file cache data\r\n
0x70000019 | Get chunk container file size\r\n
0x7000001a | Pin stream map\r\n
0x7000001b | Pin chunk container\r\n
0x7000001c | Pin chunk\r\n
0x7000001d | Allocate pool buffer\r\n
0x7000001e | Unpin chunk container\r\n
0x7000001f | Unpin chunk\r\n
0x70000020 | Dedup read processing\r\n
0x70000021 | Get first stream map entry\r\n
0x70000022 | Read chunk metadata\r\n
0x70000023 | Read chunk data\r\n
0x70000024 | Reference TlCache data\r\n
0x70000025 | Read chunk data from stream store\r\n
0x70000026 | Assemble chunk data\r\n
0x70000027 | Decompress chunk data\r\n
0x70000028 | Copy chunk data in to user buffer\r\n
0x70000029 | Insert chunk data in to tlcache\r\n
0x7000002a | Read data from dedup reparse point file\r\n
0x7000002b | Prepare stream map\r\n
0x7000002c | Patch clean ranges\r\n
0x7000002d | Writing data to dedup file\r\n
0x7000002e | Queue write request on dedup file\r\n
0x7000002f | Do copy on write work on dedup file\r\n
0x70000030 | Do full recall on dedup file\r\n
0x70000031 | Do partial recall on dedup file\r\n
0x70000032 | Do dummy paging read on dedup file\r\n
0x70000033 | Read clean data for recalling file\r\n
0x70000034 | Write clean data to dedup file normally\r\n
0x70000035 | Write clean data to dedup file paged\r\n
0x70000036 | Recall dedup file using paging Io\r\n
0x70000037 | Flush dedup file after recall\r\n
0x70000038 | Update bitmap after recall on dedup file\r\n
0x70000039 | Delete dedup reparse point\r\n
0x7000003a | Open dedup file\r\n
0x7000003b | Locking user buffer for read\r\n
0x7000003c | Get system address for MDL\r\n
0x7000003d | Read clean dedup file\r\n
0x7000003e | Get range state\r\n
0x7000003f | Get chunk body\r\n
0x70000040 | Release chunk\r\n
0x70000041 | Release decompress chunk context\r\n
0x70000042 | Prepare decompress chunk context\r\n
0x70000043 | Copy data to compressed buffer\r\n
0x70000044 | Release data from TL Cache\r\n
0x70000045 | Queue async read request\r\n
0x80565301 | The requested object was not found.\r\n
0x80565302 | One (or more) of the arguments given to the task scheduler is not valid.\r\n
0x80565303 | The specified object already exists.\r\n
0x80565304 | The specified path was not found.\r\n
0x80565305 | The specified user is invalid.\r\n
0x80565306 | The specified path is invalid.\r\n
0x80565307 | The specified name is invalid.\r\n
0x80565308 | The specified property is out of range.\r\n
0x80565309 | A required filter driver is either not installed, not loaded, or not ready for service.\r\n
0x8056530a | There is insufficient disk space to perform the requested operation.\r\n
0x8056530b | Deduplication could not be enabled on the specified volume. This might be because the volume uses an unsupported file system, is larger than the maximum supported volume size, is read-only, is formatted with an unsupported cluster size, or is not a fixed drive. Deduplication is supported on fixed, write-enabled ReFS, NTFS, CSVFS_ReFS, or CSVFS_NTFS volumes smaller than or equal to 64 TB, with cluster sizes less than or equal to 64 KB.\r\n
0x8056530c | Data deduplication encountered an unexpected error. Check the Data Deduplication Operational event log for more information.\r\n
0x8056530d | The specified scan log cursor has expired.\r\n
0x8056530e | The file system might be corrupted.  Please run the CHKDSK utility.\r\n
0x8056530f | A volume shadow copy could not be created or was unexpectedly deleted.\r\n
0x80565310 | Data deduplication encountered a corrupted XML configuration file.\r\n
0x80565311 | The Data Deduplication service could not access the global configuration because the Cluster service is not running.\r\n
0x80565312 | The Data Deduplication service could not access the global configuration because it has not been installed yet.\r\n
0x80565313 | Data deduplication failed to access the volume. It may be offline.\r\n
0x80565314 | The module encountered an invalid parameter or a valid parameter with an invalid value, or an expected module parameter was not found. Check the operational event log for more information.\r\n
0x80565315 | An attempt was made to perform an initialization operation when initialization has already been completed.\r\n
0x80565316 | An attempt was made to perform an uninitialization operation when that operation has already been completed.\r\n
0x80565317 | The Data Deduplication service detected an internal folder that is not secure. To secure the folder, reinstall deduplication on the volume.\r\n
0x80565318 | Data chunking has already been initiated.\r\n
0x80565319 | An attempt was made to perform an operation from an invalid state.\r\n
0x8056531a | An attempt was made to perform an operation before initialization.\r\n
0x8056531b | Call ::PushBuffer to continue chunking or ::Drain to enumerate any partial chunks.\r\n
0x8056531c | The Data Deduplication service detected multiple chunk store folders; however, only one chunk store folder is permitted. To fix this issue, reinstall deduplication on the volume.\r\n
0x8056531d | The data is invalid.\r\n
0x8056531e | The process is in an unknown state.\r\n
0x8056531f | The process is not running.\r\n
0x80565320 | There was an error while opening the file.\r\n
0x80565321 | The job process could not start because the job was not found.\r\n
0x80565322 | The client process ID does not match the ID of the host process that was started.\r\n
0x80565323 | The specified volume is not enabled for deduplication.\r\n
0x80565324 | A zero-character chunk ID is not valid.\r\n
0x80565325 | The index is filled to capacity.\r\n
0x80565327 | Session already exists.\r\n
0x80565328 | The compression format selected is not supported.\r\n
0x80565329 | The compressed buffer is larger than the uncompressed buffer.\r\n
0x80565330 | The buffer is not large enough.\r\n
0x8056533a | Index Scratch Log Error in: Seek, Read, Write, or Create\r\n
0x8056533b | The job type is invalid.\r\n
0x8056533c | Persistence layer enumeration error.\r\n
0x8056533d | The operation was cancelled.\r\n
0x8056533e | This job will not run at the scheduled time because it requires more memory than is currently available.\r\n
0x80565341 | The job was terminated while in a cancel or pending state.\r\n
0x80565342 | The job was terminated while in a handshake pending state.\r\n
0x80565343 | The job was terminated due to a service shutdown.\r\n
0x80565344 | The job was abandoned before starting.\r\n
0x80565345 | The job process exited unexpectedly.\r\n
0x80565346 | The Data Deduplication service detected that the container cannot be compacted or updated because it has reached the maximum generation version. \r\n
0x80565347 | The corruption log has reached its maximum size.\r\n
0x80565348 | The data deduplication scrubbing job failed to process the corruption logs.\r\n
0x80565349 | Data deduplication failed to create new chunk store container files. Allocate more space to the volume.\r\n
0x80565350 | An error occurred while opening the file because the file was in use. \r\n
0x80565351 | An error was discovered while deduplicating the file. The file is now skipped.\r\n
0x80565352 | File Server Deduplication encountered corruption while enumerating chunks in a chunk store.\r\n
0x80565353 | The scan log is not valid.\r\n
0x80565354 | The data is invalid due to checksum (CRC) mismatch error.\r\n
0x80565355 | Data deduplication encountered file corruption error.\r\n
0x80565356 | Job completed with some errors. Check event logs for more details.\r\n
0x80565357 | Data deduplication is not supported on the version of the chunk store found on this volume.\r\n
0x80565358 | Data deduplication encountered an unknown version of chunk store on this volume.\r\n
0x80565359 | The job was assigned less memory than the minimum it needs to run.\r\n
0x8056535a | The data deduplication job schedule cannot be modified.\r\n
0x8056535b | The valid data length of chunk store container is misaligned.\r\n
0x8056535c | File access is denied.\r\n
0x8056535d | Data deduplication job stopped due to too many corrupted files.\r\n
0x8056535e | Data deduplication job stopped due to an internal error in the BCrypt SHA-512 provider.\r\n
0x8056535f | Data deduplication job stopped for store reconciliation.\r\n
0x80565360 | File skipped for deduplication due to its size.\r\n
0x80565361 | File skipped due to deduplication retry limit.\r\n
0x80565362 | The pipeline buffer cache is full.\r\n
0x80565363 | Another Data deduplication job already running on this volume.\r\n
0x80565364 | Data deduplication cannot run this job on this Csv volume on this node. Try running the job on the Csv volume resource owner node.\r\n
0x80565365 | Data deduplication failed to initialize cluster state on this node.\r\n
0x80565366 | Optimization of the range was aborted by the dedup filter driver.\r\n
0x80565367 | The operation could not be performed because of a concurrent IO operation.\r\n
0x80565368 | Data deduplication encountered an unexpected error. Verify deduplication is enabled on all nodes if in a cluster configuration. Check the Data Deduplication Operational event log for more information.\r\n
0x80565369 | Data access for data deduplicated CSV volumes can only be disabled when in maintenance mode. Check the Data Deduplication Operational event log for more information.\r\n
0x8056536a | Data Deduplication encountered an IO device error that may indicate a hardware fault in the storage subsystem.\r\n
0x8056536b | Data deduplication cannot run this cmdlet on this Csv volume on this node. Try running the cmdlet on the Csv volume resource owner node.\r\n
0x8056536c | Deduplication job not supported during rolling cluster upgrade.\r\n
0x8056536d | Deduplication setting not supported during rolling cluster upgrade.\r\n
0x8056536e | Data port job is not ready to accept requests.\r\n
0x8056536f | Data port request not accepted due to request count/size limit exceeded.\r\n
0x80565370 | Data port request completed with some errors. Check event logs for more details.\r\n
0x80565371 | Data port request failed. Check event logs for more details.\r\n
0x80565372 | Data port error accessing the hash index. Check event logs for more details.\r\n
0x80565373 | Data port error accessing the stream store. Check event logs for more details.\r\n
0x80565374 | Data port file stub error. Check event logs for more details.\r\n
0x80565375 | Data port encountered a deduplication filter error. Check event logs for more details.\r\n
0x80565376 | Data port cannot commit stream map due to missing chunk. Check event logs for more details.\r\n
0x80565377 | Data port cannot commit stream map due to invalid stream map metadata. Check event logs for more details.\r\n
0x80565378 | Data port cannot commit stream map due to invalid stream map entry. Check event logs for more details.\r\n
0x80565379 | Data port cannot retrieve job interface for volume. Check event logs for more details.\r\n
0x8056537a | The specified path is not supported.\r\n
0x8056537b | // Data port cannot decompress chunk. Check event logs for more details.\r\n
0x8056537c | Data port cannot calculate chunk hash. Check event logs for more details.\r\n
0x8056537d | Data port cannot read chunk stream. Check event logs for more details.\r\n
0x8056537e | The target file is not a deduplicated file. Check event logs for more details.\r\n
0x8056537f | The target file is partially recalled. Check event logs for more details.\r\n
0x80565380 | Near inline deduplication can only be enabled on ReFS tiered volumes.\r\n
0x90000001 | Data Deduplication\r\n
0x90000002 | Application\r\n
0x91000001 | Data Deduplication Change Events\r\n
0xb0001000 | Volume "%1" appears as disconnected and it is ignored by the service.  You may want to rescan disks.   Error: %2.%n%3\r\n
0xb0001001 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3". Most likely the CPU is under heavy load.  Error: %4.%n%5\r\n
0xb0001002 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3".  Error: %4.%n%5\r\n
0xb0001003 | The COM Server with CLSID %1 and name "%2" cannot be started on machine "%3" during Safe Mode. The Data Deduplication service cannot start while in safe mode.  Error: %4.%n%5\r\n
0xb0001004 | A critical component required by Data Deduplication is not registered. This might happen if an error occurred during Windows setup, or if the computer does not have the Windows Server 2012 or later version of Deduplication service installed. The error returned from CoCreateInstance on class with CLSID %1 and Name "%2" on machine "%3" is %4.%n%5\r\n
0xb0001005 | Data Deduplication service is shutting down due to idle timeout.%n%1\r\n
0xb0001006 | Data Deduplication service is shutting down due to shutdown event from the Service Control Manager.%n%1\r\n
0xb0001007 | Data Deduplication job of type "%1" on volume "%2" has completed with return code: %3%n%4\r\n
0xb0001008 | Data Deduplication error: Unexpected error calling routine %1.  hr = %2.%n%3\r\n
0xb0001009 | Data Deduplication error: Unexpected error.%n%1\r\n
0xb000100a | Data Deduplication warning: %1%nError: %2.%n%3\r\n
0xb000100b | Data Deduplication error: Unexpected COM error %1: %2.  Error code: %3.%n%4\r\n
0xb000100c | Data Deduplication was unable to access the following file or volume: "%1".  This file or volume might be locked by another application right now, or you might need to give Local System access to it.%n%2\r\n
0xb000100d | Data Deduplication encountered an unexpected error during volume scan of volumes mounted at "%1" ("%2"). To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100e | Data Deduplication was unable to create or access the shadow copy for volumes mounted at "%1" ("%2"). Possible causes include an improper Shadow Copy configuration, insufficient disk space, or extreme memory, I/O or CPU load of the system. To find out more information about the root cause for this error please consult the Application/System event log for other Deduplication service, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:%n%3\r\n
0xb000100f | Data Deduplication was unable to access volumes mounted at "%1" ("%2"). Make sure that dismount or format operations do not happen while running deduplication.%n%3\r\n
0xb0001010 | Data Deduplication was unable to access a file or volume. Details:%n%n%1%n The volume may be inaccessible for I/O operations or marked read-only. In case of a cluster volume, this may be a transient failure during failover.%n%2\r\n
0xb0001011 | Data Deduplication was unable to scan volume "%1" ("%2").%n%3\r\n
0xb0001012 | Data Deduplication detected a corruption on file "%1" at offset ("%2").  If this condition persists then please restore the data from a previous backup.  Corruption details: Structure=%3, Corruption type = %4, Additional data = %5%n%6\r\n
0xb0001013 | Data Deduplication encountered failure while reconciling chunk store on volume "%1". The error code was %2. Reconciliation is disabled for the current optimization job.%n%3\r\n
0xb0001016 | Data Deduplication encountered corrupted chunk container %1 while performing full garbage collection. The corrupted chunk container is skipped.%n%2\r\n
0xb0001017 | Data Deduplication could not initialize change log under %1. The error code was %2.%n%3\r\n
0xb0001018 | Data Deduplication service could not mark chunk container %1 as reconciled. The error code was %2.%n%3\r\n
0xb0001019 | A Data Deduplication configuration file is corrupted. The system or volume may need to be restored from backup.%n%1\r\n
0xb000101a | Data Deduplication was unable to save one of the configuration stores on volume "%1" due to a disk-full error: If the disk is full, please clean it up (extend the volume or delete some files). If the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.%n%2\r\n
0xb000101b | Data Deduplication could not access global configuration since the cluster service is not running. Please start the cluster service and retry the operation.%n%1\r\n
0xb000101c | Shadow copy "%1" was deleted during storage report generation.  Volume "%2" might be configured with inadequate shadow copy storage area. Data Deduplication could not process this volume.%n%3\r\n
0xb000101d | Shadow copy creation failed for volume "%1" after retrying for %2 minutes because other shadow copies were being created.  Reschedule the Data Deduplication for a less busy time.%n%3\r\n
0xb000101e | Volume "%1" is not supported for shadow copy.  It is possible that the volume was removed from the system.  Data Deduplication service could not process this volume.%n%2\r\n
0xb000101f | The volume "%1" has been deleted or removed from the system.%n%2\r\n
0xb0001020 | Shadow copy creation failed for volume "%1" with error %2.  The volume might be configured with inadequate shadow copy storage area.  File Serve Deduplication service could not process this volume.%n%3\r\n
0xb0001021 | The file system on volume "%1" is potentially corrupted.  Please run the CHKDSK utility to verify and fix the file system.%n%2\r\n
0xb0001022 | Data Deduplication detected an insecure internal folder. To secure the folder, reinstall deduplication on the volume again.%n%1\r\n
0xb0001023 | Data Deduplication could not find a chunk store on the volume.%n%1\r\n
0xb0001024 | Data Deduplication detected multiple chunk store folders. To recover, reinstall deduplication on the volume.%n%1\r\n
0xb0001025 | Data Deduplication detected conflicting chunk store folders: "%1" and "%2".%n%3\r\n
0xb0001026 | The data is invalid.%n%1\r\n
0xb0001027 | Data Deduplication scheduler failed to initialize with error "%1".%n%2\r\n
0xb0001028 | Data Deduplication failed to validate job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb0001029 | Data Deduplication failed to start job type "%1" on volume "%2" with error "%3".%n%4\r\n
0xb000102c | Data Deduplication detected job type "%1" on volume "%2" uses too much memory. %3 MB is assigned. %4 MB is used.%n%5\r\n
0xb000102d | Data Deduplication detected job type "%1" on volume "%2" memory usage has dropped to desirable level.%n%3\r\n
0xb000102e | Data Deduplication cancelled job type "%1" on volume "%2". It uses too much memory than the amount assigned to it.%n%3\r\n
0xb000102f | Data Deduplication cancelled job type "%1" on volume "%2". Memory resource is running low on the machine or in the job.%n%3\r\n
0xb0001030 | Data Deduplication job type "%1" on volume "%2" failed to report completion to the service with error: %3.%n%4\r\n
0xb0001031 | Data Deduplication detected a container cannot be compacted or updated because it has reached the maximum generation.%n%1\r\n
0xb0001032 | Data Deduplication corruption log "%1" is corrupted.%n%2\r\n
0xb0001033 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". Please run scrubbing job to process corruption log. No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001034 | Data Deduplication corruption log "%1" has reached maximum allowed size "%2". No more corruptions will be reported until the log is processed.%n%3\r\n
0xb0001035 | Data Deduplication scheduler failed to uninitialize with error "%1".%n%2\r\n
0xb0001036 | Data Deduplication detected a new container could not be created in a chunk store because it ran out of available container Id.%n%1\r\n
0xb0001037 | Data Deduplication full garbage collection phase 1 (cleaning file related metadata) on volume "%1" failed with error: %2.  The job will continue with phase 2 execution (data chunk cleanup).%n%3\r\n
0xb0001039 | Data Deduplication full garbage collection could not achieve maximum space reclamation because delete logs for data container %1 could not be cleaned up.%n%2\r\n
0xb000103a | Some files could not be deduplicated because of FSRM Quota violations on volume %1. Files skipped are likely compressed or sparse files in folders which are at quota or close to their quota limit. Please consider increasing the quota limit for folders that are at their quota limit or close to it.%n%2\r\n
0xb000103b | Data Deduplication failed to dedup file %1 "%2" due to fatal error %3%n%4\r\n
0xb000103c | Data Deduplication encountered corruption while accessing a file in chunk store.%n%1\r\n
0xb000103d | Data Deduplication encountered corruption while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103e | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store. Please run scrubbing job for diagnosis and repair.%n%1\r\n
0xb000103f | Data Deduplication is unable to access file %1 because the file is in use.%n%2\r\n
0xb0001040 | Data Deduplication encountered checksum (CRC) mismatch error while accessing a file in chunk store.%n%1\r\n
0xb0001041 | Data Deduplication cannot run the job on volume %1 because the dedup store version compatiblity check failed with error %2.%n%3\r\n
0xb0001042 | Data Deduplication has disabled the volume %1 because it has discovered too many corruptions. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001043 | Data Deduplication has detected a corrupt corruption metadata file on the store at %1. Please run deep scrubbing on the volume.%n%2\r\n
0xb0001044 | Volume "%1" cannot be enabled for Data Deduplication. Data Deduplication does not support volumes larger than 64TB. Error: %2.%n%3\r\n
0xb0001045 | Data Deduplication cannot be enabled on SIS volume "%1". Error: %2.%n%3\r\n
0xb0001046 | File-system is configured for case-sensitive file/folder names. Data Deduplication does not support case-sensitive file-system mode.%n%1\r\n
0xb0001049 | Data Deduplication changed scrubbing job to read-only due to insufficient disk space.%n%1\r\n
0xb000104b | Data Deduplication has disabled the volume %1 because there are missing or corrupt containers. Please run deep scrubbing on the volume.%n%2\r\n
0xb000104d | Data Deduplication encountered a disk-full error.%n%1\r\n
0xb000104e | Data Deduplication job cannot run on volume "%1" due to insufficient disk space.%n%2\r\n
0xb000104f | Data Deduplication job cannot run on offline volume "%1".%n%2\r\n
0xb0001050 | Data Deduplication recovered a corrupt or missing file.%n%1\r\n
0xb0001051 | Data Deduplication encountered a corrupted metadata file. To correct the problem, schedule or manually run a Garbage Collection job on the affected volume with the -Full option.%n%1\r\n
0xb0001052 | Data Deduplication encountered chunk %1 with corrupted header while updating container. The corrupted chunk is replicated to the new container %2.%n%3\r\n
0xb0001053 | Data Deduplication encountered chunk %1 with transient header corruption while updating container. The corrupted chunk is NOT replicated to the new container %2.%n%3\r\n
0xb0001054 | Data Deduplication failed to read chunk container redirection table from file %1 with error %2.%n%3\r\n
0xb0001055 | Data Deduplication failed to initialize reparse point index table for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001056 | Data Deduplication failed to deep scrub container file %1 on volume %2 with error %3.%n%4\r\n
0xb0001057 | Data Deduplication failed to load stream map log for deep scrubbing from file %1 with error %2.%n%3\r\n
0xb0001058 | Data Deduplication found a duplicate local chunk id %1 in container file %2.%n%3\r\n
0xb0001059 | Data Deduplication job type "%1" on volume "%2" was cancelled manually.%n%3\r\n
0xb000105a | Scheduled data Deduplication job type "%1" on volume "%2" was cancelled.%n%3\r\n
0xb000105d | The Data Deduplication chunk store statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105e | The Data Deduplication volume statistics file on volume "%1" is corrupted and will be reset. Statistics will be updated by a subsequent job and can be updated manually by running the Update-DedupStatus cmdlet.%n%2\r\n
0xb000105f | Data Deduplication failed to append to deep scrubbing log file %1 with error %2.%n%3\r\n
0xb0001060 | Data Deduplication encountered a failure during deep scrubbing on store %1 with error %2.%n%3\r\n
0xb0001061 | Data Deduplication cancelled job type "%1" on volume "%2". The job violated Csv dedup job placement policy.%n%3\r\n
0xb0001062 | Data Deduplication cancelled job type "%1" on volume "%2". The csv job monitor has been uninitialized.%n%3\r\n
0xb0001063 | Data Deduplication encountered a IO device error while accessing a file on the volume. This is likely a hardware fault in the storage subsystem.%n%1\r\n
0xb0001064 | Data Deduplication encountered an unexpected error. If this is a cluster, verify Data Deduplication is enabled on all nodes of the cluster.%n%1\r\n
0xb0001065 | Attempted to disable data access for data deduplicated CSV volume "%1" without maintenance mode. Data access can only be disabled for a CSV volume when in maintenance mode. Place volume into maintenance mode and retry.%n%2\r\n
0xb0001800 | Data Deduplication service could not unoptimize file "%5%6%7". Error %8, "%9".\r\n
0xb0001801 | Data Deduplication service failed to unoptimize too many files %3. Some files are not reported.\r\n
0xb0001802 | Data Deduplication service has finished unoptimization on volume %3 with no errors.\r\n
0xb0001803 | Data Deduplication service has finished unoptimization on volume %3 with %4 errors.\r\n
0xb0001804 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb0001805 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable cores: %6%nPriority: %7%nFull: %8%nVolume free space (MB): %9\r\n
0xb0001806 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6%nFull: %7%nRead-only: %8\r\n
0xb0001807 | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nPriority: %6\r\n
0xb0001809 | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate (percent): %7%nSaved space (MB): %8%nVolume used space (MB): %9%nVolume free space (MB): %10%nOptimized file count: %11%nIn-policy file count: %12%nJob processed space (MB): %13%nJob elapsed time (seconds): %18%nJob throughput (MB/second): %19%nChurn processing throughput (MB/second): %20\r\n
0xb000180a | %1 job has completed.%n%nFull: %2%nVolume: %5 (%4)%nError code: %6%nError message: %7%nFreed up space (MB): %8%nVolume free space (MB): %9%nJob elapsed time (seconds): %10%nJob throughput (MB/second): %11\r\n
0xb000180b | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6\r\n
0xb000180c | %1 job has completed.%n%nFull: %2%nRead-only: %3%nVolume: %6 (%5)%nError code: %7%nError message: %8%nTotal corruption count: %9%nFixable corruption count: %10%n%nWhen corruptions are found, check more details in Scrubbing event channel.\r\n
0xb000180d | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nUnoptimized file count: %7%nJob processed space (MB): %8%nJob elapsed time (seconds): %9%nJob throughput (MB/second): %10\r\n
0xb000180e | %1 job has been queued.%n%nVolume: %4 (%3)%nSystem memory percent: %5 %nPriority: %6%nSchedule mode: %7\r\n
0xb000181c | Restore of deduplicated file "%1" failed with the following error: %2, "%3".\r\n
0xb000181d | Priority %1 job has started.%n%nVolume: %4 (%3)%nFile ID: %11%nAvailable memory: %5 MB%nAvailable cores: %6%nInstances: %7%nReaders per instance: %8%nPriority: %9%nIoThrottle: %10\r\n
0xb000181e | %1 job has started.%n%nVolume: %4 (%3)%nAvailable memory: %5 MB%nAvailable threads: %6%nPriority: %7\r\n
0xb000181f | %1 job has completed.%n%nVolume: %4 (%3)%nError code: %5%nError message: %6%nSavings rate (percent): %7%nSaved space (MB): %8%nVolume used space (MB): %9%nVolume free space (MB): %10%nOptimized file count: %11%nChunk lookup count: %12%nInserted chunk count: %13%nInserted chunks logical data (MB): %14%nInserted chunks physical data (MB): %15%nCommitted stream count: %16%nCommitted stream entry count: %17%nCommitted stream logical data (MB): %18%nRetrieved chunks physical data (MB): %19%nRetrieved stream logical data (MB): %20%nDataPort time (seconds): %21%nJob elapsed time (seconds): %22%nIngress throughput (MB/second): %23%nEgress throughput (MB/second): %24\r\n
0xb0001821 | Data Deduplication detected a non-clustered volume specified for the chunk index cache volume in a clustered deployment. The configuration is not recommended because it may result in job failures after failover.%n%nVolume: %3 (%2)\r\n
0xb0001822 | DataPort status update.  %n%nVolume: %2%nSavings rate (percent): %3%nSaved space (MB): %4%nVolume used space (MB): %5%nVolume free space (MB): %6%nOptimized file count: %7%nChunk lookup count: %8%nInserted chunk count: %9%nInserted chunks logical data (MB): %10%nInserted chunks physical data (MB): %11%nCommitted stream count: %12%nCommitted stream entry count: %13%nCommitted stream logical data (MB): %14%nRetrieved chunks physical data (MB): %15%nRetrieved stream logical data (MB): %16%nDataPort time (seconds): %17%nJob elapsed time (seconds): %18%nIngress throughput (MB/second): %19%nEgress throughput (MB/second): %20\r\n
0xb0002000 | Data Deduplication detected job type "%1" on volume "%2" working set is low. Ratio to commit size is %3.%n%4\r\n
0xb0002001 | Data Deduplication detected job type "%1" on volume "%2" working set has recovered to desirable level.%n%3\r\n
0xb0002002 | Data Deduplication detected job type "%1" on volume "%2" page fault rate is high. The rate is %3 page faults per second.%n%4\r\n
0xb0002003 | Data Deduplication detected job type "%1" on volume "%2" page fault rate has lowered to desirable level. The rate is %3 page faults per second.%n%4\r\n
0xb0002004 | Data Deduplication failed to dedup file "%1" with file ID %2 due to non-fatal error %3%n%4.%n%nNote: You can retrieve the file name by running the command FSUTIL FILE QUERYFILENAMEBYID on the file in question.\r\n
0xb000200c | Data Deduplication has aborted a group commit session.%n%nFile count: %1%nError: %2%n%3\r\n
0xb000201c | Fail to open dedup setting registry key\r\n
0xb000201d | Data Deduplication failed to dedup file "%1" with file ID %2 due to oplock break%n%3\r\n
0xb000201e | Data Deduplication failed to load hotspot table from file %1 due to error %2.%n%3\r\n
0xb000201f | Data Deduplication failed to initialize oplock.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb0002020 | Data Deduplication while running job on volume %1 detected invalid physical sector size %2. Using default value %3.%n%4\r\n
0xb0002021 | Data Deduplication detected an unsupported chunk store container.%n%1\r\n
0xb0002022 | Data Deduplication could not create window to receive task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002023 | Data Deduplication could not create thread to poll for task scheduler stop message due to error %1. Task(s) may not stop after duration limit.%n%2\r\n
0xb0002024 | An attempt was made to perform an initialization operation when initialization has already been completed.%n%1\r\n
0xb0002028 | Data Deduplication created emergency file %1.%n%3\r\n
0xb0002029 | Data Deduplication failed to create emergency file %1 with error %2.%n%3\r\n
0xb000202a | Data Deduplication deleted emergency file %1.%n%3\r\n
0xb000202b | Data Deduplication failed to delete emergency file %1 with error %2.%n%3\r\n
0xb000202c | Data Deduplication detected a chunk store container with misaligned valid data length.%n%1\r\n
0xb000202d | Data Deduplication Garbage Collection encountered a delete log entry with an invalid stream map signature for stream map Id %1.%n%2\r\n
0xb000202e | Data Deduplication failed to initialize oplock as the file appears to be missing.%n%nFile ID: %1%nFile name: "%2"%nError: %3%n%4\r\n
0xb000202f | Data Deduplication skipped too many file-level errors. We will not log more than %1 file-level errors per job.%n%2\r\n
0xb0002030 | Data Deduplication diagnostic warning.%n%n%1%n%2\r\n
0xb0002031 | Data Deduplication diagnostic information.%n%n%1%n%2\r\n
0xb0002032 | Data Deduplication found file %1 with a stream map id %2 in container file %3 marked for deletion.%n%4\r\n
0xb0002033 | Failed to enqueue job of type "%1" on volume "%2".%n%3\r\n
0xb0002034 | Error terminating job host process for job type "%1" on volume "%2" (process id: %3).%n%4\r\n
0xb0002035 | Data Deduplication encountered corrupted chunk %1 while updating container. Corrupted data that cannot be repaired will be copied as-is to the new container %2.%n%3\r\n
0xb0002036 | Data Deduplication job type "%1" on volume "%2" failed to exit gracefully.%n%3\r\n
0xb0002037 | Data Deduplication job host for job type "%1" on volume "%2" exited unexpectedly.%n%3\r\n
0xb0002038 | Data Deduplication has failed to load corruption metadata file on the store at %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb0002039 | Data Deduplication full garbage collection phase 1 on volume "%1" encountered an error %2 while processing file %3. Phase 1 will need to be aborted since garbage collection of file-related metadata is unsafe to continue on file errors.%n%4\r\n
0xb000203a | Data Deduplication has failed to process corruption metadata file %1 due to error %2. Please run deep scrubbing on the volume.%n%3\r\n
0xb000203b | Data Deduplication has failed to load a corrupted metadata file %1 due to error %2. Deleting the file and continuing.%n%3\r\n
0xb000203c | Data Deduplication has failed to set NTFS allocation size for container file %1 due to error %2.%n%3\r\n
0xb000203d | Data Deduplication configured to use BCrypt provider '%1' for hash algorithm %2.%n%3\r\n
0xb000203e | Data Deduplication could not use BCrypt provider '%1' for hash algorithm %2 due to an error in operation %3. Reverting to the Microsoft primitive CNG provider.%n%4\r\n
0xb000203f | Data Deduplication failed to include file "%1" in file metadata analysis calculations.%n%2\r\n
0xb0002040 | Data Deduplication failed to include stream map %1 in file metadata analysis calculations.%n%2\r\n
0xb0002041 | Data Deduplication encountered an error for file "%1" while scanning files and folders.%n%2\r\n
0xb0002042 | Data Deduplication encountered an error while attempting to resume processing. Please consult the event log parameters for more details about the current file being processed.%n%1\r\n
0xb0002043 | Data Deduplication encountered an error %1 whle scanning usn journal on volume %2 for updating hot range tracking.%n%3\r\n
0xb0002044 | Data Deduplication could not truncate the stream of an optimized file. No action is required. Error: %1%n%n%2\r\n
0xb0002800 | %1 job memory requirements.%n%nVolume: %4 (%3)%nMinimum memory: %5 MB%nMaximum memory: %6 MB%nMinimum disk: %7 MB%nMaximum cores: %8\r\n
0xb0002801 | %1 reconciliation has started.%n%nVolume: %4 (%3)\r\n
0xb0002802 | %1 reconciliation has completed.%n%nGuidance: This event is expected when Reconciliation has completed, there is no recommended or required action. Reconciliation is an internal process that allows Optimization and DataPort jobs to run when the entire Deduplication chunk index cannot be loaded into memory. %n%nVolume: %4 (%3)%nReconciled containers: %5%nUnreconciled containers: %6%nCatchup references: %7%nCatchup containers: %8%nReconciled references: %9%nReconciled containers: %10%nCross-reconciled references: %11%nCross-reconciled containers: %12%nError code: %13%nError message: %14\r\n
0xb0002803 | %1 job on volume %4 (%3) was configured with insufficient memory.%n%nSystem memory percentage: %5%nAvailable memory: %8 MB%nMinimum required memory: %6 MB\r\n
0xb0002804 | Optimization memory details for %1 job on volume %3 (%2).\r\n
0xb0002805 | An open file was skipped during optimization. No action is required.%n%nFileId: %2%nSkip Reason: %1\r\n
0xb0002806 | An operation succeeded after one or more retries. Operation: %1; FileId: %3; Number of retries: %2\r\n
0xb0002807 | Data Deduplication aborted the optimization pipeline.%nVolumePath: %1%nErrorCode: %2%nErrorMessage: %3Details: %4\r\n
0xb0002808 | Data Deduplication aborted a file.%nFileId: %1%nFilePath: %2%nFileSize: %3%nFlags: %4%nTotalRanges: %5%nSkippedRanges: %6%nAbortedRanges: %7%nCommittedRanges: %8%nErrorCode: %9%nErrorMessage: %10Details: %11\r\n
0xb0002809 | Data Deduplication aborted a file range.%nFileId: %1%nFilePath: %2%nRangeOffset: %3%nRangeLength: %4%nErrorCode: %5%nErrorMessage: %6Details: %7\r\n
0xb000280a | Data Deduplication aborted a session.%nMaxSize: %1%nCurrentSize: %2%nRemainingRanges: %3%nErrorCode: %4%nErrorMessage: %5Details: %6\r\n
0xb000280b | USN journal created.%n%nVolume: %2 (%1)%nMaximum size %3 MB%nAllocation size %4 MB\r\n
0xb000280c | DataPort memory details for %1 job on volume %3 (%2).\r\n
0xb000280d | Data deduplication detected a file with an ID that is not supported.  Files with identifiers unpackable into 64-bits will be skipped. FileId: %1 FileName: %2\r\n
0xb000280e | Reconciliation should be run to ensure optimal savings.%n%nGuidance: This event is expected when Reconciliation is turned off for the DataPort job. Reconciliation is an internal process that allows Optimization and DataPort jobs to run when the entire Deduplication chunk index cannot be loaded into memory. When Reconciliation would require 50% or more of the memory on the system, it is recommended that you (temporarily) cease running a DataPort job against this volume, and run an Optimization job. If Reconciliation is not run through an Optimization job before Reconciliation would require more than 100% of system memory, Reconciliation will not be able to be run again (unless more memory is added). This would result in permanent decreased space efficiency on this volume.%n%nVolume: %2 (%1)%nMemory percentage required: %3\r\n
0xb000280f | Data Deduplication optimization job will not run the reconciliation step due to inadequate memory.%n%nGuidance: Deduplication savings will be suboptimal until the optimization job is provided more memory, or more more memory is added to the system.%n%nVolume: %2 (%1)%nMemory percentage required: %3\r\n
0xb0003200 | Data Deduplication service detected corruption in "%5%6%7". The corruption cannot be repaired.\r\n
0xb0003201 | Data Deduplication service detected corruption (%7) in "%6". See the event details for more information.\r\n
0xb0003202 | Data Deduplication service detected a corrupted item (%11 - %13, %8, %9, %10, %12) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003203 | Data Deduplication service has finished scrubbing on volume %3. It did not find any corruption since the last scrubbing.\r\n
0xb0003204 | Data Deduplication service found %4 corruption(s) on volume %3. All corruptions are fixed.\r\n
0xb0003205 | Data Deduplication service found %4 corruption(s) on volume %3. %5 corruption(s) are fixed. %6 user file(s) are corrupted. %7 user file(s) are fixed. For the corrupted file list, see the Microsoft/Windows/Deduplication/Scrubbing events.\r\n
0xb0003206 | Data Deduplication service found too many corruptions on volume %3. Some corruptions are not reported.\r\n
0xb0003211 | Data Deduplication service has finished scrubbing on volume %3. See the event details for more information.\r\n
0xb0003212 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003213 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003214 | Data Deduplication service encountered error while detecting corruptions in chunk store on volume %3. The error was %4. The job is aborted.\r\n
0xb0003216 | Data Deduplication service encountered error while loading corruption logs on volume %3. The error was %4. The job continues. Some corruptions may not be detected.\r\n
0xb0003217 | Data Deduplication service encountered error while cleaning up corruption logs on volume %3. The error was %4. Some corruptions may be reported again next time.\r\n
0xb0003218 | Data Deduplication service encountered error while loading hotspots mapping from chunk store on volume %3. The error was %4. Some corruptions may not be repaired.\r\n
0xb0003219 | Data Deduplication service encountered error while determining corrupted user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb000321a | Data Deduplication service found %4 corruption(s) on volume %3. %6 user file(s) are corrupted. %7 user file(s) are fixable. Please run scrubbing job in read-write mode to attempt fixing reported corruptions.\r\n
0xb000321b | Data Deduplication service fixed corruption in "%5%6%7".\r\n
0xb000321c | Data Deduplication service detected fixable corruption in "%5%6%7". Please run scrubbing job in read-write mode to fix this corruption.\r\n
0xb000321e | Data Deduplication service encountered error while repairing corruptions on volume %3. The error was %4. The repair is unsuccessful.\r\n
0xb000321f | Data Deduplication service detected a corrupted item (%6, %7, %8, %9) in Deduplication Chunk Store on volume %4. See the event details for more information.\r\n
0xb0003220 | Container (%8,%9) with user data is missing from the chunk store. Missing container may result from incomplete restore, incomplete migration or file-system corruption. Volume is disabled from further optimization. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0003221 | Data Deduplication service encountered error while scaning dedup user files on volume %3. The error was %4. Some user file corruptions may not be reported.\r\n
0xb0003222 | Data Deduplication service encountered error while processing file "%5%6%7". The error was %8.\r\n
0xb0003223 | Data Deduplication service encountered too many errors while processing file on volume %3. The threshold was %4. Some user file corruptions may not be reported.\r\n
0xb0003224 | Data Deduplication service detected potential data loss (%9) in "%6" due to sharing reparse data with file "%8". See the event details for more information.\r\n
0xb0003225 | Container (%8,%9) with user data is corrupt in the chunk store. It is recommended to restore the volume prior to enabling the volume for further optimization.\r\n
0xb0005000 | Open stream store stream (StartingChunkId %1, FileId %2)\r\n
0xb0005001 | Open stream store stream completed %1\r\n
0xb0005002 | Prepare for paging IO (Stream %1, FileId %2)\r\n
0xb0005003 | Prepare for paging IO completed %1\r\n
0xb0005005 | Read stream map completed %1\r\n
0xb0005006 | Read chunks (Stream %1, FileId %2, IoType %3, FirstRequestChunkId %4, NextRequest %5)\r\n
0xb0005007 | Read chunks completed %1\r\n
0xb0005008 | Compute checksum (ItemType %1, DataSize %2)\r\n
0xb0005009 | Compute checksum completed %1\r\n
0xb000500a | Get container entry (ContainerId %1, Generation %2)\r\n
0xb000500b | Get container entry completed %1\r\n
0xb000500c | Get maximum generation for container (ContainerId %1, Generation %2)\r\n
0xb000500d | Get maximum generation for container completed %1\r\n
0xb000500e | Open chunk container (ContainerId %1, Generation %2, RootPath %4)\r\n
0xb000500f | Open chunk container completed %1\r\n
0xb0005010 | Initialize chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005011 | Initialize chunk container redirection table completed %1\r\n
0xb0005012 | Validate chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005013 | Validate chunk container redirection table completed %1\r\n
0xb0005014 | Get chunk container valid data length (ContainerId %1, Generation %2)\r\n
0xb0005015 | Get chunk container valid data length completed %1\r\n
0xb0005016 | Get offset from chunk container redirection table (ContainerId %1, Generation %2)\r\n
0xb0005017 | Get offset from chunk container redirection table completed %1\r\n
0xb0005018 | Read chunk container block (ContainerId %1, Generation %2, Buffer %3, Offset %4, Length %5, IoType %6, Synchronous %7)\r\n
0xb0005019 | Read chunk container block completed %1\r\n
0xb000501a | Clear chunk container block (Buffer %1, Size %2, BufferType %3)\r\n
0xb000501b | Clear chunk container block completed %1\r\n
0xb000501c | Copy chunk (Buffer %1, Size %2, BufferType %3, BufferOffset %4, OutputCapacity %5)\r\n
0xb000501d | Copy chunk completed %1\r\n
0xb000501e | Initialize file cache (UnderlyingFileObject %1, CacheFileSize %2)\r\n
0xb000501f | Initialize file cache completed %1\r\n
0xb0005020 | Map file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005021 | Map file cache data completed %1\r\n
0xb0005022 | Unpin file cache data(Bcb %1)\r\n
0xb0005023 | Unpin file cache data completed %1\r\n
0xb0005024 | Copy file cache data (CacheFileObject %1, Offset %2, Length %3)\r\n
0xb0005025 | Copy file cache data completed %1\r\n
0xb0005026 | Read underlying file cache data (CacheFileObject %1, UnderlyingFileObject %2, Offset %3, Length %4)\r\n
0xb0005027 | Read underlying file cache data completed %1\r\n
0xb0005028 | Get chunk container file size (ContainerId %1, Generation %2)\r\n
0xb0005029 | Get chunk container file size completed %1\r\n
0xb000502a | Pin stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb000502b | Pin stream map completed %1\r\n
0xb000502c | Pin chunk container (ContainerId %1, Generation %2)\r\n
0xb000502d | Pin chunk container completed %1\r\n
0xb000502e | Pin chunk (ContainerId %1, Generation %2)\r\n
0xb000502f | Pin chunk completed %1\r\n
0xb0005030 | Allocate pool buffer (ReadLength %1, PagingIo %2)\r\n
0xb0005031 | Allocate pool buffer completed %1\r\n
0xb0005032 | Unpin chunk container (ContainerId %1, Generation %2)\r\n
0xb0005033 | Unpin chunk container completed %1\r\n
0xb0005034 | Unpin chunk (ContainerId %1, Generation %2)\r\n
0xb0005035 | Unpin chunk completed %1\r\n
0xb0006028 | Dedup read processing (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006029 | Dedup read processing completed %1\r\n
0xb000602a | Get first stream map entry (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602b | Get first stream map entry completed %1\r\n
0xb000602c | Read chunk metadata (Stream %1, CurrentOffset %2, AdjustedFinalOffset %3, FirstChunkByteOffset %4, ChunkRequestsEndOffset %5, TlCache %6)\r\n
0xb000602d | Read chunk metadata completed %1\r\n
0xb000602e | Read chunk data (TlCache %1, Stream %2, RequestStartOffset %3, RequestEndOffset %4)\r\n
0xb000602f | Read chunk data completed %1\r\n
0xb0006030 | Reference TlCache data (TlCache %1, Stream %2)\r\n
0xb0006031 | Reference TlCache data completed %1\r\n
0xb0006032 | Read chunk data from stream store (Stream %1)\r\n
0xb0006033 | Read chunk data from stream store completed %1\r\n
0xb0006034 | Assemble chunk data\r\n
0xb0006035 | Assemble chunk data completed %1\r\n
0xb0006036 | Decompress chunk data\r\n
0xb0006037 | Decompress chunk data completed %1\r\n
0xb0006038 | Copy chunk data in to user buffer (BytesCopied %1)\r\n
0xb0006039 | Copy chunk data in to user buffer completed %1\r\n
0xb000603a | Insert chunk data in to tlcache\r\n
0xb000603b | Insert chunk data in to tlcache completed %1\r\n
0xb000603c | Read data from dedup reparse point file (FileObject %1, Offset %2, Length %3)\r\n
0xb000603d | Read underlying file cache data completed %1\r\n
0xb000603e | Prepare stream map (StreamContext %1)\r\n
0xb000603f | Prepare stream map completed %1\r\n
0xb0006040 | Patch clean ranges (FileObject %1, Offset %2, Length %3)\r\n
0xb0006041 | Patch clean ranges completed %1\r\n
0xb0006042 | Writing data to dedup file (FileObject %1, Offset %2, Length %3, IoType %4)\r\n
0xb0006043 | Writing data to dedup file completed %1\r\n
0xb0006044 | Queue write request on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006045 | Queue write request on dedup file completed %1\r\n
0xb0006046 | Do copy on write work on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006047 | Do copy on write work on dedup file completed %1\r\n
0xb0006048 | Do full recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006049 | Do full recall on dedup file completed %1\r\n
0xb000604a | Do partial recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604b | Do partial recall on dedup file completed %1\r\n
0xb000604c | Do dummy paging read on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604d | Do dummy paging read on dedup file completed %1\r\n
0xb000604e | Read clean data for recalling file (FileObject %1, Offset %2, Length %3)\r\n
0xb000604f | Read clean data for recalling file completed %1\r\n
0xb0006050 | Write clean data to dedup file normally (FileObject %1, Offset %2, Length %3)\r\n
0xb0006051 | Write clean data to dedup file completed %1\r\n
0xb0006052 | Write clean data to dedup file paged (FileObject %1, Offset %2, Length %3)\r\n
0xb0006053 | Write clean data to dedup file paged completed %1\r\n
0xb0006054 | Recall dedup file using paging Io (FileObject %1, Offset %2, Length %3)\r\n
0xb0006055 | Recall dedup file using paging Io completed %1\r\n
0xb0006056 | Flush dedup file after recall (FileObject %1)\r\n
0xb0006057 | Flush dedup file after recall completed %1\r\n
0xb0006058 | Update bitmap after recall on dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006059 | Update bitmap after recall on dedup file completed %1\r\n
0xb000605a | Delete dedup reparse point (FileObject %1)\r\n
0xb000605b | Delete dedup reparse point completed %1\r\n
0xb000605c | Open dedup file (FilePath %1)\r\n
0xb000605d | Open dedup file completed %1\r\n
0xb000605e | Locking user buffer for read\r\n
0xb000605f | Locking user buffer for read completed %1\r\n
0xb0006060 | Get system address for MDL\r\n
0xb0006061 | Get system address for MDL completed %1\r\n
0xb0006062 | Read clean dedup file (FileObject %1, Offset %2, Length %3)\r\n
0xb0006063 | Read clean dedup file completed %1\r\n
0xb0006064 | Get range state (Offset %1, Length %2)\r\n
0xb0006065 | Get range state completed %1\r\n
0xb0006066 | Get chunk body\r\n
0xb0006067 | Get chunk body completed %1\r\n
0xb0006068 | Release chunk\r\n
0xb0006069 | Release chunk completed %1\r\n
0xb000606a | Release decompress chunk context (BufferSize %1)\r\n
0xb000606b | Release decompress chunk context completed %1\r\n
0xb000606c | Prepare decompress chunk context (BufferSize %1)\r\n
0xb000606d | Prepare decompress chunk context completed %1\r\n
0xb000606e | Copy data to compressed buffer (BufferSize %1)\r\n
0xb000606f | Copy data to compressed buffer completed %1\r\n
0xb0006070 | Release data from TL Cache\r\n
0xb0006071 | Release data from TL Cache completed %1\r\n
0xb0006072 | Queue async read request (FileObject %1, Offset %2, Length %3)\r\n
0xb0006073 | Queue async read request complete %1\r\n
0xb0015004 | Read stream map (Stream %1, FileId %2, StartIndex %3, EntryCount %4)\r\n
0xb1004000 | Create chunk container (%1 - %2.%3.ccc)\r\n
0xb1004001 | Create chunk container completed %1\r\n
0xb1004002 | Copy chunk container (%1 - %2.%3.ccc)\r\n
0xb1004003 | Copy chunk container completed %1\r\n
0xb1004004 | Delete chunk container (%1 - %2.%3.ccc)\r\n
0xb1004005 | Delete chunk container completed %1\r\n
0xb1004006 | Rename chunk container (%1 - %2.%3.ccc%4)\r\n
0xb1004007 | Rename chunk container completed %1\r\n
0xb1004008 | Flush chunk container (%1 - %2.%3.ccc)\r\n
0xb1004009 | Flush chunk container completed %1\r\n
0xb100400a | Rollback chunk container (%1 - %2.%3.ccc)\r\n
0xb100400b | Rollback chunk container completed %1\r\n
0xb100400c | Mark chunk container (%1 - %2.%3.ccc) read-only\r\n
0xb100400d | Mark chunk container read-only completed %1\r\n
0xb100400e | Write chunk container (%1 - %2.%3.ccc) redirection table at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb100400f | Write chunk container redirection table completed %1\r\n
0xb1004011 | Write chunk container header completed %1\r\n
0xb1004013 | Insert data chunk header completed %1\r\n
0xb1004015 | Insert data chunk body completed %1 with ChunkId %2\r\n
0xb1004019 | Write delete log header completed %1\r\n
0xb100401b | Append delete log entries completed %1\r\n
0xb100401d | Delete delete log completed %1\r\n
0xb100401f | Rename delete log completed %1\r\n
0xb1004021 | Write chunk container bitmap completed %1\r\n
0xb1004023 | Delete chunk container bitmap completed %1\r\n
0xb1004024 | Write merge log (%5 - %6.%7.merge.log) header\r\n
0xb1004025 | Write merge log header completed %1\r\n
0xb1004027 | Insert hotspot chunk header completed %1\r\n
0xb1004029 | Insert hotspot chunk body completed %1 with ChunkId %2\r\n
0xb100402b | Insert stream map chunk header completed %1\r\n
0xb100402d | Insert stream map chunk body completed %1 with ChunkId %2\r\n
0xb100402f | Append merge log entries completed %1\r\n
0xb1004030 | Delete merge log (%1 - %2.%3.merge.log)\r\n
0xb1004031 | Delete merge log completed %1\r\n
0xb1004032 | Flush merge log (%1 - %2.%3.merge.log)\r\n
0xb1004033 | Flush merge log completed %1\r\n
0xb1004034 | Update file list entries (Remove: %1, Add: %2)\r\n
0xb1004035 | Update file list entries completed %1\r\n
0xb1004036 | Set dedup reparse point on %2 (FileId %1) (ReparsePoint: SizeBackedByChunkStore %3, StreamMapInfoSize %4, StreamMapInfo %5)\r\n
0xb1004037 | Set dedup reparse point completed %1 (%2)\r\n
0xb1004038 | Set dedup zero data on %2 (FileId %1)\r\n
0xb1004039 | Set dedup zero data completed %1\r\n
0xb100403a | Flush reparse point files\r\n
0xb100403b | Flush reparse point files completed %1\r\n
0xb100403c | Set sparse on file id %1\r\n
0xb100403d | Set sparse completed %1\r\n
0xb100403e | FSCTL_SET_ZERO_DATA on file id %1 at offset %2 and BeyondFinalZero %3\r\n
0xb100403f | FSCTL_SET_ZERO_DATA completed %1\r\n
0xb1004040 | Rename chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1004041 | Rename chunk container bitmap completed %1\r\n
0xb1004042 | Insert padding chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1004043 | Insert padding chunk header completed %1\r\n
0xb1004044 | Insert padding chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1004045 | Insert padding chunk body completed %1 with ChunkId %2\r\n
0xb1004046 | Insert batch of chunks to chunk container (%1 - %2.%3.ccc) at offset %4 (BatchChunkCount %5, BatchDataSize %6)\r\n
0xb1004047 | Insert batch of chunks completed %1\r\n
0xb1004049 | Write chunk container directory completed %1\r\n
0xb100404b | Delete chunk container directory completed %1\r\n
0xb100404c | Rename chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb100404d | Rename chunk container directory completed %1\r\n
0xb1014010 | Write chunk container (%5 - %6.%7.ccc) header at offset %8 (Header: USN %9, VDL %10, #Chunk %11, NextLocalId %12, Flags %13, LastAppendTime %14, BackupRedirectionTableOfset %15, LastReconciliationLocalId %16)\r\n
0xb1014012 | Insert data chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorupted %6, DataSize %7)\r\n
0xb1014014 | Insert data chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014018 | Write delete log (%5 - %6.%7.delete.log) header\r\n
0xb101401a | Append delete log (%1 - %2.%3.delete.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb101401c | Delete delete log (%1 - %2.%3.delete.log)\r\n
0xb101401e | Rename delete log (%1 - %2.%3.delete.log)\r\n
0xb1014020 | Write chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4) (Bitmap: BitLength %5, StartIndex %6, Count %7)\r\n
0xb1014022 | Delete chunk container bitmap (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb1014026 | Insert hotspot chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014028 | Insert hotspot chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb101402a | Insert stream map chunk header to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7)\r\n
0xb1014048 | Write chunk container directory (%1 - %2) for chunk container (%1 - %3.%4) (Directory: EntryCount %5)\r\n
0xb101404a | Delete chunk container directory (%1 - %2) for chunk container (%1 - %3.%4)\r\n
0xb102402e | Append merge log (%1 - %2.%3.merge.log) entries at offset %4 (Entries: StartIndex %5, Count %6)\r\n
0xb103402c | Insert stream map chunk body to chunk container (%1 - %2.%3.ccc) at offset %4 (Chunk: IsBatched %5 IsCorrupted %6, DataSize %7) (Entries: StartIndex %8, Count %9)\r\n
0xd0000001 | Chunk header\r\n
0xd0000002 | Chunk body\r\n
0xd0000003 | Container header\r\n
0xd0000004 | Container redirection table\r\n
0xd0000005 | Hotspot table\r\n
0xd0000006 | Delete log header\r\n
0xd0000007 | Delete log entry\r\n
0xd0000008 | GC bitmap header\r\n
0xd0000009 | GC bitmap entry\r\n
0xd000000a | Merge log header\r\n
0xd000000b | Merge log entry\r\n
0xd000000c | Data\r\n
0xd000000d | Stream map\r\n
0xd000000e | Hotspot\r\n
0xd000000f | Optimization\r\n
0xd0000010 | Garbage Collection\r\n
0xd0000011 | Scrubbing\r\n
0xd0000012 | Unoptimization\r\n
0xd0000013 | Analysis\r\n
0xd0000014 | Low\r\n
0xd0000015 | Normal\r\n
0xd0000016 | High\r\n
0xd0000017 | Cache\r\n
0xd0000018 | Non-cache\r\n
0xd0000019 | Paging\r\n
0xd000001a | Memory map\r\n
0xd000001b | Paging memory map\r\n
0xd000001c | None\r\n
0xd000001d | Pool\r\n
0xd000001e | PoolAligned\r\n
0xd000001f | MDL\r\n
0xd0000020 | Map\r\n
0xd0000021 | Cached\r\n
0xd0000022 | NonCached\r\n
0xd0000023 | Paged\r\n
0xd0000024 | container file\r\n
0xd0000025 | file list file\r\n
0xd0000026 | file list header\r\n
0xd0000027 | file list entry\r\n
0xd0000028 | primary file list file\r\n
0xd0000029 | backup file list file\r\n
0xd000002a | Scheduled\r\n
0xd000002b | Manual\r\n
0xd000002c | recall bitmap header\r\n
0xd000002d | recall bitmap body\r\n
0xd000002e | recall bitmap missing\r\n
0xd000002f | Recall bitmap\r\n
0xd0000030 | Unknown\r\n
0xd0000031 | The pipeline handle was closed\r\n
0xd0000032 | The file was deleted\r\n
0xd0000033 | The file was overwritten\r\n
0xd0000034 | The file was recalled\r\n
0xd0000035 | A transaction was started on the file\r\n
0xd0000036 | The file was encrypted\r\n
0xd0000037 | The file was compressed\r\n
0xd0000038 | Set Zero Data was called on the file\r\n
0xd0000039 | Extended Attributes were set on the file\r\n
0xd000003a | A section was created on the file\r\n
0xd000003b | The file was shrunk\r\n
0xd000003c | A long-running IO operation prevented optimization\r\n
0xd000003d | An IO operation failed\r\n
0xd000003e | Notifying Optimization\r\n
0xd000003f | Setting the Reparse Point\r\n
0xd0000040 | Truncating the file\r\n
0xd0000041 | DataPort\r\n
0xd1000001 | None\r\n
0xd1000002 | LZNT1\r\n
0xd1000003 | Xpress\r\n
0xd1000004 | Xpreff Huff\r\n
0xd1000005 | None\r\n
0xd1000006 | Standard\r\n
0xd1000007 | Max\r\n
0xd1000008 | Hybrid\r\n
0xf0000001 | None\r\n
0xf0000002 | Bad checksum\r\n
0xf0000003 | Inconsistent metadata\r\n
0xf0000004 | Invalid header metadata\r\n
0xf0000005 | Missing file\r\n
0xf0000006 | Bad checksum (storage subsystem)\r\n
0xf0000007 | Corruption (storage subsystem)\r\n
0xf0000008 | Corruption (missing metadata)\r\n
0xf0000009 | Possible data loss (duplicate reparse data)\r\n
