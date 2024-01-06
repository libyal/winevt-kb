## esent.dll

Path: %SystemRoot%\system32\esent.dll

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | Snapshot\r\n
0x00000011 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine started a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A snapshot backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from %4 to %5.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Begining the backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are Inconsistent. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are Consistent. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are Inconsistent. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are Consistent. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The logfile %4 is damaged and cannot be used. If this logfile is required for recovery, a good copy of the logfile will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles up to %7.\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Index %4 of table %5 is corrupted (%6).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a consistent state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, please contact PSS for further instructions regarding the steps required in order to allow recovery to proceed without this database.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Please contact PSS for further assistance.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap log in sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap log in sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid or not installed on this machine.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is corrupt. Please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is corrupt. Please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4'.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4'.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a consistent state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Snapshot function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Snapshot %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Snapshot %4 freeze starting error %5.\r\n
0x000007d3 | %1 (%2) %3Snapshot %4 freeze stopped.\r\n
0x000007d4 | %1 (%2) %3Snapshot %4 time-out (%5 ms).\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine started a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A snapshot backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from %4 to %5.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Beginning the backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are Inconsistent. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are Consistent. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are Inconsistent. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are Consistent. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The logfile %4 is damaged and cannot be used. If this logfile is required for recovery, a good copy of the logfile will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles up to %7.\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Index %4 of table %5 is corrupted (%6).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a consistent state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, please contact PSS for further instructions regarding the steps required in order to allow recovery to proceed without this database.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Please contact PSS for further assistance.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap log in sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap log in sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid or not installed on this machine.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4'.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4'.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a consistent state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Snapshot function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy %4 freeze starting error %5.\r\n
0x000007d3 | %1 (%2) %3Shadow copy %4 freeze stopped.\r\n
0x000007d4 | %1 (%2) %3Shadow copy %4 time-out (%5 ms).\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) started a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from %4 to %5.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Beginning the backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The logfile %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this logfile is required for recovery, a good copy of the logfile will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles up to %7.\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n%n%nFor more information, click http://www.microsoft.com/contentredirect.asp.\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n%n%nFor more information, click http://www.microsoft.com/contentredirect.asp.\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch.  The expected timestamp was %6 but the actual timestamp on the page was %7.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The logfile %4 is missing (error %5) and cannot be used. If this logfile is required for recovery, a good copy of the logfile will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of logfiles %4 to %5 is missing (error %6) and cannot be used. If these logfiles are required for recovery, a good copy of these logfiles will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all logfiles required for recovery were succesfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on logfile %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device name "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid or not installed on this machine.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or previous node in a B-Tree (ObjectId: %5, PgnoRoot: %6, Type: %7), the database engine skipped over %8 non-visible nodes in %9 pages. It is likely that these non-visible nodes are nodes which have been marked for deletion but which have yet to be purged. The database may benefit from widening the online maintenance window during off-peak hours in order to purge such nodes and reclaim their space. If this message persists, offline defragmentation may be run to remove all nodes which have been marked for deletion but have yet to be purged from the database.\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or previous node in a B-Tree (ObjectId: %5, PgnoRoot: %6, Type: %7), the database engine skipped over %8 non-visible nodes in %9 pages. In addition, since this message was last reported %10 hours ago, %11 other incidents of excessive non-visible nodes were encountered (a total of %12 nodes in %13 pages were skipped) during navigation in this B-Tree. It is likely that these non-visible nodes are nodes which have been marked for deletion but which have yet to be purged. The database may benefit from widening the online maintenance window during off-peak hours in order to purge such nodes and reclaim their space. If this message persists, offline defragmentation may be run to remove all nodes which have been marked for deletion but have yet to be purged from the database.\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4'.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4'.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n

### 6.1.3940.31

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3\r\n
0x00000001 | General\r\n
0x00000002 | Caché de página de la base de datos\r\n
0x00000003 | Registro y recuperación\r\n
0x00000004 | Administración de espacio\r\n
0x00000005 | Definición de tabla, columna e índice\r\n
0x00000006 | Tratamiento de registros\r\n
0x00000007 | Rendimiento\r\n
0x00000008 | Reparación de base de datos\r\n
0x00000009 | Conversión de base de datos\r\n
0x0000000a | Desfragmentación en pantalla\r\n
0x0000000b | Configuración de parámetros del sistema\r\n
0x0000000c | Dañado de la base de datos\r\n
0x0000000d | Llenado de ceros de la base de datos\r\n
0x0000000e | Administrador de transacciones\r\n
0x0000000f | Simulación de error en los recursos\r\n
0x00000010 | <EOL>\r\n
0x00000064 | %1 (%2) Se inició el motor de base de datos %3.%4.%5.%6.\r\n
0x00000065 | %1 (%2) Se detuvo el motor de base de datos.\r\n
0x00000066 | %1 (%2) El motor de base de datos inició una nueva instancia (%3).\r\n
0x00000067 | %1 (%2) El motor de base de datos detuvo una instancia (%3).\r\n
0x00000068 | %1 (%2) El motor de base de datos detuvo una instancia (%3) con error (%4).\r\n
0x000000c8 | %1 (%2) El motor de base de datos está iniciando una copia de seguridad completa.\r\n
0x000000c9 | %1 (%2) El motor de base de datos está iniciando una copia de seguridad incremental.\r\n
0x000000ca | %1 (%2) El motor de bases de datos completó correctamente el proceso de copia de seguridad.\r\n
0x000000cb | %1 (%2) El motor de base de datos detuvo la copia de seguridad con el error %3.\r\n
0x000000cc | %1 (%2) El motor de base de datos está restaurando desde el directorio de copia de seguridad %3.\r\n
0x000000cd | %1 (%2) El motor de base de datos detuvo la restauración.\r\n
0x000000ce | %1 (%2) La base de datos %3 necesita una copia de seguridad completa antes de una copia de seguridad incremental.\r\n
0x000000cf | %1 (%2) El motor de bases de datos detuvo la copia de seguridad porque la anuló el cliente o se produjo un error en la conexión con el cliente.\r\n
0x0000012c | %1 (%2) El motor de base de datos está iniciando los pasos de recuperación.\r\n
0x0000012d | %1 (%2) El motor de base de datos está reproduciendo el archivo de registro %3.\r\n
0x0000012e | %1 (%2) El motor de base de datos completó correctamente los pasos de recuperación.\r\n
0x0000012f | %1 (%2) Error %3 del motor de base de datos.\r\n
0x00000190 | %1 (%2) Error de tiempo de lectura sincrónica superpuesta de página %3. Restaure las bases de datos de una copia de seguridad anterior.\r\n
0x00000191 | %1 (%2) Error de proceso de escritura sincrónica superpuesta de página %3.\r\n
0x00000192 | %1 (%2) Error de escritura sincrónica superpuesta de página %3.\r\n
0x00000193 | %1 (%2) Error de escritura sincrónica superpuesta de página %3 en archivo de revisión.\r\n
0x00000194 | %1 (%2) Error de suma de comprobación de lectura sincrónica %3. Restaure las bases de datos de una copia de seguridad anterior.\r\n
0x00000195 | %1 (%2) Error de suma de comprobación de lectura previa %3. Restaure las bases de datos de una copia de seguridad anterior.\r\n
0x00000196 | %1 (%2) La lectura directa encontró la página dañada %3 con el error %4. Restaure las bases de datos desde una copia de seguridad anterior.\r\n
0x00000197 | %1 (%2) Error de terminación del subproceso de E/S del búfer %3.\r\n
0x00000198 | %1 (%2) No se puede escribir en el registro. Error %3.\r\n
0x00000199 | %1 (%2) No se puede escribir en el encabezado del registro. Error %3.\r\n
0x0000019a | %1 (%2) No se puede leer el registro. Error %3.\r\n
0x0000019b | %1 (%2) La marca de versión del registro no coincide con la marca de versión del motor de base de datos.\r\n
0x0000019c | %1 (%2) No se puede leer el encabezado del registro. Error %3.\r\n
0x0000019d | %1 (%2) No se puede crear el registro. Puede que la unidad sea de sólo lectura, no tenga espacio disponible, esté incorrectamente configurada o esté dañada. Error %3.\r\n
0x0000019e | %1 (%2) No se puede escribir en la sección 0 al limpiar el registro. Error %3.\r\n
0x0000019f | %1 (%2) No se puede escribir en la sección 1 al limpiar el registro. Error %3.\r\n
0x000001a0 | %1 (%2) No se puede escribir en la sección 2 al limpiar el registro. Error %3.\r\n
0x000001a1 | %1 (%2) No se puede escribir en la sección 3 al limpiar el registro. Error %3.\r\n
0x000001a2 | %1 (%2) Error %3 al abrir un archivo de registro recién creado.\r\n
0x000001a3 | %1 (%2) No se puede leer la página %4 de la base de datos %3. Error %5.\r\n
0x000001a4 | %1 (%2) No se puede leer el encabezado de la base de datos %3. Error %4. Es posible que se moviera la base de datos.\r\n
0x000001a5 | %1 (%2) No se recuperó la base de datos %3 creada a las %4. La base de datos recuperada se creó a las %5.\r\n
0x000001a6 | %1 (%2) No se recuperó la base de datos %3 creada a las %4.\r\n
0x000001a7 | %1 (%2) El motor de base de datos encontró una página errónea.\r\n
0x000001a8 | %1 (%2) El disco de base de datos está lleno.\r\n
0x000001a9 | %1 (%2) La firma de la base de datos no coincide con la firma del registro de la base de datos %3.\r\n
0x000001aa | %1 (%2) El motor de base de datos no puede encontrar el archivo o el directorio llamado %3.\r\n
0x000001ab | %1 (%2) El motor de base de datos no puede tener acceso al archivo llamado %3.\r\n
0x000001ac | %1 (%2) El motor de base de datos está rechazando operaciones de actualización por falta de espacio disponible en el disco de registro.\r\n
0x000001ad | %1 (%2) El disco de registro del motor de base de datos está lleno. Libere espacio en disco y reinicie el motor de base de datos.\r\n
0x000001ae | %1 (%2) La base de datos %3 y su archivo de revisión no coinciden.\r\n
0x000001af | %1 (%2) El registro inicial 0x%3 es demasiado alto. Debe comenzar por 0x%4.\r\n
0x000001b0 | %1 (%2) El registro final 0x%3 es demasiado bajo. Debe terminar en 0x%4.\r\n
0x000001b1 | %1 (%2) El archivo de registro de restauración 0x%3 está dañado.\r\n
0x000001b2 | %1 (%2) La fecha del archivo de registro de restauración 0x%3 no coincide con el registro anterior.\r\n
0x000001b3 | %1 (%2) Falta el archivo de registro de restauración 0x%3.\r\n
0x000001b4 | %1 (%2) El archivo de registro existente 0x%3 está dañado. Se eliminaron los archivos de registro de 0x%4 a 0x%5.\r\n
0x000001b5 | %1 (%2) El archivo de registro existente 0x%3 no está en una secuencia válida. Se eliminaron los archivos de registro de 0x%4 a 0x%5.\r\n
0x000001b6 | %1 (%2) La base de datos de copia de seguridad %3 debe ser un múltiplo de 4 KB.\r\n
0x000001b7 | %1 (%2) No se puede escribir una copia sombra del encabezado para el archivo %3.\r\n
0x000001b8 | %1 (%2) El archivo de registro %3 está dañado.\r\n
0x000001b9 | %1 (%2) Error %4 del sistema de archivos durante operaciones de E/S en la base de datos %3. Restaure las bases de datos de una copia de seguridad anterior.\r\n
0x000001ba | %1 (%2) Error de tamaño de E/S en la base de datos %3, se esperaba un tamaño de %4 y se devolvió %5.\r\n
0x000001bb | %1 (%2) Error %4 del sistema de archivos durante operaciones de E/S en el archivo de registro %3.\r\n
0x000001bc | %1 (%2) Error de tamaño de E/S en el archivo de registro %3, se esperaba un tamaño de %4 y se devolvió %5.\r\n
0x000001bd | %1 (%2) El motor de bases de datos alcanzó el tamaño máximo de la base de datos, %3 MB.\r\n
0x000001be | %1 (%2) Se detuvo abruptamente la recuperación de la base de datos al rehacer el archivo de registro %3 (%4,%5). Los registros tras este punto pueden no ser reconocibles y no se procesarán.\r\n
0x000001bf | %1 (%2) Vínculos de página erróneos en la tabla %3 de la base de datos %4 (%5 => %6, %7).\r\n
0x000001c0 | %1 (%2) Se detectó incoherencia de datos en la tabla %3 de la base de datos %4 (%5,%6).\r\n
0x000001c1 | %1 (%2) Se detectó incoherencia en la asignación de datos de transmisión (%3,%4).\r\n
0x000001c2 | %1 (%2) Se detectó un intervalo en la secuencia del archivo de registro de transacciones. Falta el archivo de registro %3 y posiblemente los archivos de registro siguientes.\r\nRestaure los archivos de registro que faltan para solucionar este problema.\r\n
0x000001c3 | %1 (%2) No se puede escribir en la sección mientras se limpia el registro. Error %3.\r\n
0x000001c4 | %1 (%2) La base de datos %3 requiere los archivos de registro %4-%5, el archivo de registro de rehacer actual para esta base de datos es %6.\r\n
0x000001c5 | %1 (%2) La base de datos %3 requiere los archivos de registro %4-%5, el último archivo de registro de rehacer para esta base de datos es %6.\r\n
0x000001c6 | %1 (%2) Se produjo un error inesperado al recuperar o restaurar la base de datos %3.\r\n
0x000001c7 | %1 (%2) Error %3 al abrir un archivo de registro %4.\r\n
0x000001c8 | %1 (%2) La página de encabezados principal de %3 está dañada. Se utiliza la copia sombra de la página.\r\n
0x000001cc | %1 (%2) Se detectó una escritura rasgada al restaurar de la copia de seguridad el archivo de registro %3. El registro de suma de comprobación fallido se encuentra en la posición %4.\r\n
0x000001cd | %1 (%2) Se detectó una escritura rasgada durante la recuperación total desde el archivo de registro %3. El registro de suma de comprobación fallido se encuentra en la posición %4.\r\n
0x000001ce | %1 (%2) Se detectó una escritura rasgada durante la recuperación parcial en el archivo de registro %3. El registro de suma de comprobación fallido se encuentra en la posición %4.\r\n
0x000001cf | %1 (%2) Se detectaron daños al restaurar a partir del registro de archivo de copia de seguridad %3. El registro de suma de comprobación fallido se encuentra en la posición %4.\r\nLos datos que no coinciden con el modelo de relleno del archivo de registro aparecen por primera vez en el sector %5.\r\n
0x000001d0 | %1 (%2) Se detectaron daños durante la recuperación total en el archivo de registro %3. El registro de suma de comprobación fallido se encuentra en la posición %4.\r\nLos datos que no coinciden con el modelo de relleno del archivo de registro aparecen por primera vez en el sector %5.\r\n
0x000001d1 | %1 (%2) Se detectaron daños durante la recuperación parcial en el archivo de registro %3. El registro de suma de comprobación fallido se encuentra en la posición %4.\r\nLos datos que no coinciden con el modelo de relleno del archivo de registro aparecen por primera vez en el sector %5.\r\n
0x000001d2 | %1 (%2) Se está usando la copia sombra del sector en el archivo de registro %3 para reparar un registro de suma de comprobación no válido.\r\n
0x000001f4 | %1 (%2) El motor de base de datos perdió una página de datos erróneos.\r\n
0x000001f5 | %1 (%2) El motor de base de datos reparó un vínculo de página.\r\n
0x000001f6 | %1 (%2) El motor de base de datos perdió una o más columnas erróneas de datos en un registro.\r\n
0x000001f7 | %1 (%2) El motor de base de datos perdió un registro de datos erróneo.\r\n
0x000001f8 | %1 (%2) El motor de base de datos perdió la tabla llamada %3.\r\n
0x00000258 | %1 (%2) El motor de base de datos encontró una clave duplicada inesperada en la tabla %3. Se quitó un registro.\r\n
0x00000259 | %1 (%2) El motor de base de datos no puede encontrar el punto de entrada %3 en el archivo %4.\r\n
0x0000025a | %1 (%2) La depuración en segundo plano omitió páginas. La base de datos puede aprovechar la desfragmentación con o sin conexión.\r\n
0x0000025b | %1 (%2) Base de datos '%3': el motor de base de datos perdió las páginas no utilizadas %4-%5 mientras intentaba recuperar espacio en un árbol B (Id. de objeto %6). Puede que no se vuelva a recuperar espacio hasta que se realice la desfragmentación sin conexión.\r\n
0x0000025c | %1 (%2) Es necesario instalar la compatibilidad con el Id. de idioma 0x%3.\r\n
0x0000025d | %1 (%2) Se convirtió la columna '%3' de la tabla '%4' en una columna con etiquetas.\r\n
0x0000025e | %1 (%2) Se convirtió la columna '%3' de la tabla '%4' en una columna sin etiquetas.\r\n
0x0000025f | %1 (%2) Se convirtió la columna '%3' de la tabla '%4' de Binary a LongBinary.\r\n
0x00000260 | %1 (%2) Se convirtió la columna '%3' de la tabla '%4' de Text a LongText.\r\n
0x00000261 | %1 (%2) El motor de base de datos está iniciando la limpieza de índices de la base de datos '%3' como resultado de una actualización de versión de NT de %4.%5.%6 SP%7 a %8.%9.%10 SP%11.\r\n
0x00000262 | %1 (%2) El motor de base de datos está iniciando la limpieza de índices de la base de datos '%3' como resultado de una actualización de versión de NT de %4.%5.%6 SP%7.\r\n
0x00000263 | %1 (%2) Base de datos '%3': se volverá a generar el índice secundario '%4' de la tabla '%5' como medida de precaución tras la actualización de versión de NT de este sistema.\r\n
0x00000264 | %1 (%2) El motor de base de datos completó correctamente la limpieza de los índices de la base de datos '%3'.\r\n
0x00000265 | %1 (%2) Base de datos '%3': el índice principal '%4' de la tabla '%5' está dañado. Desfragmente la base de datos para volver a generar el índice.\r\n
0x00000266 | %1 (%2) Base de datos '%3': el índice secundario '%4' de la tabla '%5' está dañado. Desfragmente la base de datos para volver a generar el índice.\r\n
0x00000267 | %1 (%2) El motor de base de datos está convirtiendo la base de datos '%3' del formato %4 al formato %5.\r\n
0x00000268 | %1 (%2) El motor de bases de datos convirtió correctamente la base de datos '%3' del formato %4 al formato %5.\r\n
0x00000269 | %1 (%2) Se intentó utilizar la base de datos '%3', pero no se completó correctamente la conversión. Restaure desde una copia de seguridad y vuelva a ejecutar la conversión de la base de datos.\r\n
0x000002bc | %1 (%2) La desfragmentación con conexión está comenzado un recorrido completo por la base de datos '%3'.\r\n
0x000002bd | %1 (%2) La desfragmentación con conexión completó un recorrido completo por la base de datos '%3'.\r\n
0x000002be | %1 (%2) La desfragmentación con conexión está reanudando el recorrido por la base de datos '%3'.\r\n
0x000002bf | %1 (%2) La desfragmentación con conexión completó el recorrido reanudado por la base de datos '%3'.\r\n
0x000002c0 | %1 (%2) Se interrumpió y terminó la desfragmentación con conexión de la base de datos '%3'. La próxima vez que se inicie la desfragmentación con conexión de la base de datos, se reanudará desde el punto de interrupción.\r\n
0x000002c1 | %1 (%2) La desfragmentación con conexión de la base de datos '%3' terminó prematuramente al encontrarse un error inesperado %4. La próxima vez que se inicie la desfragmentación con conexión de la base de datos, se reanudará desde el punto de interrupción.\r\n
0x000002c2 | %1 (%2) Se inició el llenado con ceros de la base de datos %3\r\n
0x000002c3 | %1 (%2) El llenado con ceros de la base de datos %3 concluyó tras %4 segundos con %5%n errores\r\n%6 páginas%n\r\n%7 páginas en blanco%n\r\n%8 páginas sin modificar desde el último llenado con ceros%n\r\n%9 páginas sin usar llenadas%n\r\n%10 páginas usadas vistas%n\r\n%11 registros eliminados llenados%n\r\n%12 segmentos de datos sin referencias llenados\r\n
0x000002c4 | %1 (%2) La desfragmentación en línea está comenzando un paso completo por el archivo de secuencias '%3'.\r\n
0x000002c5 | %1 (%2) La desfragmentación en línea completó un paso completo por el archivo de secuencias '%3'.\r\n
0x000002c6 | %1 (%2) La desfragmentación en línea del archivo de secuencias '%3' redujo su tamaño en %4 bytes.\r\n
0x000002c7 | %1 (%2) La desfragmentación en línea del archivo de secuencias '%3' terminó antes de tiempo al encontrar un error inesperado %4.\r\n
0x00000320 | %1 (%2) El parámetro del sistema tamaño mínimo de la caché (%3) es menor que 4 veces el número de sesiones (%4).\r\n
0x00000321 | %1 (%2) El parámetro del sistema tamaño máximo de la caché (%3) es menor que el tamaño mínimo de la caché (%4).\r\n
0x00000322 | %1 (%2) El parámetro del sistema tamaño máximo de la caché (%3) es menor que el umbral para detener el vaciado (%4).\r\n
0x00000323 | %1 (%2) El parámetro del sistema umbral para detener el vaciado limpio (%3) es menor que el umbral para iniciar el vaciado (%4).\r\n
0x00000324 | %1 (%2) El parámetro del sistema tamaño del búfer del registro (%3 sectores) es mayor que el tamaño máximo de %4 k bytes (tamaño del archivo de registro menos el espacio reservado).\r\n
0x00000325 | %1 (%2) El parámetro del sistema página de versión máxima (%3) es menor que la página de versión preferida (%4).\r\n
0x00000326 | %1 (%2) El parámetro del sistema páginas de versión preferida se cambió de %3 a %4 por limitación de la memoria física.\r\n
0x00000327 | %1 (%2) El parámetro del sistema número máximo de tablas abiertas (%3) es menor que las tablas abiertas preferidas (%4). Compruebe las opciones del Registro.\r\n
0x00000384 | %1 (%2) Error %3 del motor de bases de datos al intentar registrar la confirmación de una transacción. Para asegurar la coherencia de la base de datos, se terminó el proceso. Reinicie el proceso para forzar la recuperación de la base de datos a un estado coherente.\r\n
0x00000385 | %1 (%2) Traza interna: %3@%4\r\n
0x00000386 | %1 (%2) El motor de base de datos detectó varios subprocesos que utilizan ilegalmente la misma sesión de la base de datos para realizar operaciones. Para asegurar la coherencia de la base de datos, se terminó el proceso. Reinicie el proceso para forzar la recuperación de la base de datos y restaurar la base de datos a un estado coherente.\r\n
0x000003e8 | %1 (%2) Se activó la simulación de error de recursos con la siguiente configuración:\r\n\t\t%3:\t%4\r\n\t\t%5:\t%6\r\n\t\t%7:\t%8\r\n\t\t%9:\t%10\r\n
0x000003e9 | %1 (%2) Se permite la simulación de error de recursos %3.\r\n
0x000003ea | %1 (%2) Se denegó la simulación de error de recursos %3.\r\n
0x000003eb | %1 (%2) La llamada JET %3 devolvió el error %4. %5 (%6)\r\n
0x000003ec | %1 (%2) El error en línea JET %3 salta a la etiqueta %4. %5 (%6)\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) started a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Beginning the backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch.  The expected timestamp was %6 but the actual timestamp on the page was %7.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device name "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7), however lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since this committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file: %4 (generation %5) before detecting an out of sequence logs, and could not locate log generation %6.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %7\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid or not installed on this machine.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine skipped over %7\r\nnon-visible nodes in %8 pages. It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine skipped over %7\r\nnon-visible nodes in %8 pages. In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times over %11 days.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times over %11 days.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3 Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3 Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3 Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n
0x000002dd | %1 (%2) %3 Online Maintenance Database Checksumming background task is NOT finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far on %8 pages.\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n%nSaved Cache: %8\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n%nRevived Cache: %8\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch.  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device with name "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.  If this condition persists, restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine skipped over %7\r\nnon-visible nodes in %8 pages. It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine skipped over %7\r\nnon-visible nodes in %8 pages. In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is NOT finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database shrink file operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database shrink file operation finished successfully and shrunk the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file.  This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nResident cache has fallen by %4 buffers (or %5%) in the last %6 seconds.\r\n%nCurrent Total Percent Resident: %7% (%8 of %9 buffers)\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5)\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nResident cache has restored by %4 buffers (or %5%) in the last %6 seconds.\r\n%nCurrent Total Percent Resident: %7% (%8 of %9 buffers)\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n%nSaved Cache: %8\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n%nRevived Cache: %8\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch.  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the mobile device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.  If this condition persists, restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch.  The 'remote' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch.  The 'remote' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 logical data checksum %6 failed to match logged scan check %7 checksum (seed %8).\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' may be corrupt. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine skipped over %7\r\nnon-visible nodes in %8 pages. It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine skipped over %7\r\nnon-visible nodes in %8 pages. In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is NOT finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database shrink file operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database shrink file operation finished successfully and shrunk the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5)\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x0000006a | %1 (%2) %3The parameter %4 was attempted to be set to %5, but was overridden to %6 by the registry settings (at %7).\r\n
0x0000006b | %1 (%2) %3The parameter %4 was read from the registry settings (at %7), but the ESE engine rejected the value %5 with err %6.\r\n
0x0000006c | %1 (%2) %3The specific ESE configuration store is locked in a read inhibit state, clear the %1 registry value to enable ESE to continue and utilize the config store.\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n%nSaved Cache: %8\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n%nRevived Cache: %8\r\n
0x00000148 | %1 (%2) %3The database engine has fired callback for attach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x00000149 | %1 (%2) %3The database engine has fired callback for detach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the mobile device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.  If this condition persists, restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 logical data checksum %6 failed to match logged scan check %7 checksum (seed %8) at log position %9.\r\n
0x0000021d | %1 (%2) %3Database %4: Page %5 was shown to be uninitialized at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).\r\n
0x0000021e | %1 (%2) %3Database %4: Page %5 (objid %6) has a logical corruption of type '%7'.\r\n
0x0000021f | %1 (%2) %3Previous log's accumulated segment checksum mismatch in logfile %4, Expected: %5, Actual: %6.\r\n
0x00000220 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a persisted lost flush detection timestamp mismatch. The read operation will fail with error %7.  If this condition persists, restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %17 milliseconds (waiting %18 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %19 pages). It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n%n%tDbtime Distrib: %20\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %21 milliseconds (waiting %22 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %23 pages). In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n%n%tDbtime Distrib: %24\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x00000279 | %1 (%2) %3Recovery had to pause (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027a | %1 (%2) %3Recovery had to pause for a long time (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027b | %1 (%2) %3Failed to attach flush map file "%4" with error %5.\r\n
0x0000027c | %1 (%2) %3Flush map file "%4" will be deleted. Reason: %5.\r\n
0x0000027d | %1 (%2) %3New flush map file "%4" will be created to enable persisted lost flush detection.\r\n
0x0000027e | %1 (%2) %3Error %4 validating page %5 on flush map file "%6". The flush type of the database pages will be set to 'unknown' state.\r\n
0x0000027f | %1 (%2) %3Inconsistent timestamp detected on page %4 of flush map file "%5" (empty if flush map persistence in disabled). The maximum timestamp on the flush map is %6, but database page %7 has a timestamp of %8. If flush map persistence is enabled, this problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000280 | %1 (%2) %3Error %4 validating header page on flush map file "%5". The flush map file will be invalidated.\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is not finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database shrink file operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database shrink file operation finished successfully and shrunk the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e9 | %1 (%2) %3Online Maintenance Database Checksumming background task is aborted for database '%4' at page %5, due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last properly completed checksumming task was on %6.\r\n
0x000002ea | %1 (%2) %3Online Maintenance Database Checksumming background task finished an interrupted and incomplete scan for database '%4'. Typical interruptions are due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last fully completed checksumming scan was on %5.\r\n
0x000002eb | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4', and in doing so has skipped %5 pages (%6%%).  prev stop: %7, this start: %8.%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state:  %8% (%9 out of %10 buffers)\r\n%nCurrent cache size vs. target:  %11% (%12 MBs)\r\n%nPhysical Memory / RAM size:     %13 MBs\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5)\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x00000391 | %1 (%2) %3The parameter %4 was not set to one value by the previous ESE application instance, but set to a different value from the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000392 | %1 (%2) %3The parameter %4 was not set via the previous ESE application instance, but is set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000393 | %1 (%2) %3The parameter %4 was set via the previous ESE application instance, but is not set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000394 | %1 (%2) %3The beta feature %4 is enabled in %5 due to the beta site mode settings %6.\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x0000006a | %1 (%2) %3The parameter %4 was attempted to be set to %5, but was overridden to %6 by the registry settings (at %7).\r\n
0x0000006b | %1 (%2) %3The parameter %4 was read from the registry settings (at %7), but the ESE engine rejected the value %5 with err %6.\r\n
0x0000006c | %1 (%2) %3The specific ESE configuration store is locked in a read inhibit state, clear the %1 registry value to enable ESE to continue and utilize the config store.\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n%nSaved Cache: %8\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nInternal Timing Sequence: %7\r\n%nRevived Cache: %8\r\n
0x00000148 | %1 (%2) %3The database engine has fired callback for attach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x00000149 | %1 (%2) %3The database engine has fired callback for detach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x0000014a | %1 (%2) %3The database [%4] format version is being held back to %6 due to application parameter setting of %5.  Current default engine version: %7.\r\n
0x0000014b | %1 (%2) %3The database [%4] version was upgraded from %5 to %6.\r\n
0x0000014c | %1 (%2) %3The database [%4] version %5 is higher than the maximum version understood by the engine %6.\r\n
0x0000014d | %1 (%2) %3The database [%4] version %5 is higher than the maximum version configured by the application %6 (EFV %7, Format Permissive %8).\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 logical data checksum %6 failed to match logged scan check %7 checksum (seed %8) at log position %9.\r\n
0x0000021d | %1 (%2) %3Database %4: Page %5 was shown to be uninitialized at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).\r\n
0x0000021e | %1 (%2) %3Database %4: Page %5 (objid %6) has a logical corruption of type '%7'.\r\n
0x0000021f | %1 (%2) %3Previous log's accumulated segment checksum mismatch in logfile %4, Expected: %5, Actual: %6.\r\n
0x00000220 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a persisted lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000221 | %1 (%2) %3Database %4: Page %5 appears to be uninitialized at log position %10 on the remote node.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000222 | %1 (%2) %3The log generation (%4) is too low (%5) to be supported or replayed by this database engine (min supported %6).\r\n
0x00000223 | %1 (%2) %3The log generation (%4) is too high (%5) to be supported or replayed by this database engine (max supported %6).\r\n
0x00000224 | %1 (%2) %3The log generation's [%4] version %5 is higher than the maximum version configured by the application %6 (EFV %7, Format Permissive %8).\r\n
0x00000225 | %1 (%2) %3A Database %4 has a page (pgno %5) with too few lines, operation attempted on line %6, actual number of lines on page %7.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %17 milliseconds (waiting %18 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %19 pages). It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n%n%tDbtime Distrib: %20\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %21 milliseconds (waiting %22 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %23 pages). In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n%n%tDbtime Distrib: %24\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x00000279 | %1 (%2) %3Recovery had to pause (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027a | %1 (%2) %3Recovery had to pause for a long time (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027b | %1 (%2) %3Failed to attach flush map file "%4" with error %5.\r\n
0x0000027c | %1 (%2) %3Flush map file "%4" will be deleted. Reason: %5.\r\n
0x0000027d | %1 (%2) %3New flush map file "%4" will be created to enable persisted lost flush detection.\r\n
0x0000027e | %1 (%2) %3Error %4 validating page %5 on flush map file "%6". The flush type of the database pages will be set to 'unknown' state.\r\n
0x0000027f | %1 (%2) %3Inconsistent timestamp detected on page %4 of flush map file "%5" (empty if flush map persistence in disabled). The maximum timestamp on the flush map is %6, but database page %7 has a timestamp of %8. If flush map persistence is enabled, this problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000280 | %1 (%2) %3Error %4 validating header page on flush map file "%5". The flush map file will be invalidated.\r\n%nAdditional information: %6\r\n
0x00000281 | %1 (%2) %3The log format feature version %5 could not be used due to the current log format %6, controlled by the parameter %4.\r\n
0x00000282 | %1 (%2) %3The database format feature version %5 could not be used due to the current database format %6, controlled by the parameter %4.\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is not finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database shrink file operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database shrink file operation finished successfully and shrunk the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e9 | %1 (%2) %3Online Maintenance Database Checksumming background task is aborted for database '%4' at page %5, due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last properly completed checksumming task was on %6.\r\n
0x000002ea | %1 (%2) %3Online Maintenance Database Checksumming background task finished an interrupted and incomplete scan for database '%4'. Typical interruptions are due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last fully completed checksumming scan was on %5.\r\n
0x000002eb | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4', and in doing so has skipped %5 pages (%6%%).  prev stop: %7, this start: %8.%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state:  %8% (%9 out of %10 buffers)\r\n%nCurrent cache size vs. target:  %11% (%12 MBs)\r\n%nPhysical Memory / RAM size:     %13 MBs\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5)\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x00000391 | %1 (%2) %3The parameter %4 was not set to one value by the previous ESE application instance, but set to a different value from the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000392 | %1 (%2) %3The parameter %4 was not set via the previous ESE application instance, but is set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000393 | %1 (%2) %3The parameter %4 was set via the previous ESE application instance, but is not set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000394 | %1 (%2) %3The beta feature %4 is enabled in %5 due to the beta site mode settings %6.\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | <EOL>\r\n
0x00000013 | System Device\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nAdditional Data:%n\r\n%7\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x0000006a | %1 (%2) %3The parameter %4 was attempted to be set to %5, but was overridden to %6 by the registry settings (at %7).\r\n
0x0000006b | %1 (%2) %3The parameter %4 was read from the registry settings (at %7), but the ESE engine rejected the value %5 with err %6.\r\n
0x0000006c | %1 (%2) %3The specific ESE configuration store is locked in a read inhibit state, clear the %1 registry value to enable ESE to continue and utilize the config store.\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n%n\r\n%nPrevious Log Processing Stats: %5\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nSaved Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nRevived Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000148 | %1 (%2) %3The database engine has fired callback for attach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x00000149 | %1 (%2) %3The database engine has fired callback for detach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x0000014a | %1 (%2) %3The database [%4] format version is being held back to %6 due to application parameter setting of %5. Current default engine version: %7.\r\n
0x0000014b | %1 (%2) %3The database [%4] version was upgraded from %5 to %6. Current engine format version parameter setting: %7\r\n
0x0000014c | %1 (%2) %3The database [%4] version %5 is higher than the maximum version understood by the engine %6.\r\n
0x0000014d | %1 (%2) %3The database [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x0000014e | %1 (%2) %3The database [%4] has completed incremental reseed page patching operations for %5 pages.\r\n%n\r\n%nDetails:\r\n%nRange of Patching: %6\r\n%nTiming: %7\r\n
0x0000014f | %1 (%2) %3Replay of a %4 for database "%5" at log position %6 was deferred due to %7.  Additional information:  %8\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO or flush on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 logical data checksum %6 failed to match logged scan check %7 checksum (seed %8) at log position %9.\r\n
0x0000021d | %1 (%2) %3Database %4: Page %5 was shown to be uninitialized at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).\r\n
0x0000021e | %1 (%2) %3Database %4: Page %5 (objid %6) has a logical corruption of type '%7'.\r\n%nDetails: %8\r\n
0x0000021f | %1 (%2) %3Previous log's accumulated segment checksum mismatch in logfile %4, Expected: %5, Actual: %6.\r\n
0x00000220 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a persisted lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000221 | %1 (%2) %3Database %4: Page %5 appears to be uninitialized at log position %10 on the remote node.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000222 | %1 (%2) %3The log generation (%4) is too low (%5) to be supported or replayed by this database engine (min supported %6).\r\n
0x00000223 | %1 (%2) %3The log generation (%4) is too high (%5) to be supported or replayed by this database engine (max supported %6).\r\n
0x00000224 | %1 (%2) %3The log generation's [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x00000225 | %1 (%2) %3A Database %4 has a page (pgno %5) with too few lines, operation attempted on line %6, actual number of lines on page %7.\r\n
0x00000226 | %1 (%2) %3Database %4: A compressed LV chunk failed verification during decompression due to a checksum mismatch. This indicates a logical corruption in the compress/decompress pipeline.\r\npgnoFDP = %5. Key = %6.\r\n
0x00000227 | %1 (%2) %3An attempt to flush to the file/disk buffers of "%4" failed after %5 seconds with system error %6: "%7".  The flush operation will fail with error %8.  If this error persists then the file system may be damaged and may need to be restored from a previous backup.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %17 milliseconds (waiting %18 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %19 pages). It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n%n%tDbtime Distrib: %20\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %21 milliseconds (waiting %22 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %23 pages). In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n%n%tDbtime Distrib: %24\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x00000279 | %1 (%2) %3Recovery had to pause (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027a | %1 (%2) %3Recovery had to pause for a long time (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027b | %1 (%2) %3Failed to attach flush map file "%4" with error %5.\r\n
0x0000027c | %1 (%2) %3Flush map file "%4" will be deleted. Reason: %5.\r\n
0x0000027d | %1 (%2) %3New flush map file "%4" will be created to enable persisted lost flush detection.\r\n
0x0000027e | %1 (%2) %3Error %4 validating page %5 on flush map file "%6". The flush type of the database pages will be set to 'unknown' state.\r\n
0x0000027f | %1 (%2) %3Inconsistent timestamp detected on page %4 of flush map file "%5" (empty if flush map persistence in disabled). The maximum timestamp on the flush map is %6, but database page %7 has a timestamp of %8. If flush map persistence is enabled, this problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000280 | %1 (%2) %3Error %4 validating header page on flush map file "%5". The flush map file will be invalidated.\r\n%nAdditional information: %6\r\n
0x00000281 | %1 (%2) %3The log format feature version %5 could not be used due to the current log format %6, controlled by the parameter %4.\r\n
0x00000282 | %1 (%2) %3The database format feature version %5 could not be used due to the current database format %6, controlled by the parameter %4.\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is not finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database shrink file operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database shrink file operation finished successfully and shrunk the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e9 | %1 (%2) %3Online Maintenance Database Checksumming background task is aborted for database '%4' at page %5, due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last properly completed checksumming task was on %6.\r\n
0x000002ea | %1 (%2) %3Online Maintenance Database Checksumming background task finished an interrupted and incomplete scan for database '%4'. Typical interruptions are due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last fully completed checksumming scan was on %5.\r\n
0x000002eb | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4', and in doing so has skipped %5 pages (%6%%).  prev stop: %7, this start: %8.%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state:  %8% (%9 out of %10 buffers)\r\n%nCurrent cache size vs. target:  %11% (%12 MBs)\r\n%nPhysical Memory / RAM size:     %13 MBs\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5)\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x00000391 | %1 (%2) %3The parameter %4 was not set to one value by the previous ESE application instance, but set to a different value from the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000392 | %1 (%2) %3The parameter %4 was not set via the previous ESE application instance, but is set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000393 | %1 (%2) %3The parameter %4 was set via the previous ESE application instance, but is not set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000394 | %1 (%2) %3The beta feature %4 is enabled in %5 due to the beta site mode settings %6.\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x000009c4 | %1 (%2) %3An attempt to initialize the FPGA failed with error %4. Please make sure that the FPGA hardware is present and configured correctly.\r\n
0x000009c5 | %1 (%2) %3An attempt to acquire an FPGA slot during initialization failed. This indicates that there are more processes trying to use the FPGA than the available slots.\r\n
0x000009c6 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a transient failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c7 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a permanent FPGA failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c8 | %1 (%2) %3An attempt to acquire an FPGA slot event during initialization failed with system error %4: "%5".\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | System Device\r\n
0x00000013 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nAdditional Data:%n\r\n%7\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x0000006a | %1 (%2) %3The parameter %4 was attempted to be set to %5, but was overridden to %6 by the registry settings (at %7).\r\n
0x0000006b | %1 (%2) %3The parameter %4 was read from the registry settings (at %7), but the ESE engine rejected the value %5 with err %6.\r\n
0x0000006c | %1 (%2) %3The specific ESE configuration store is locked in a read inhibit state, clear the %1 registry value to enable ESE to continue and utilize the config store.\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n%n\r\n%nPrevious Log Processing Stats: %5\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nSaved Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nRevived Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000148 | %1 (%2) %3The database engine has fired callback for attach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x00000149 | %1 (%2) %3The database engine has fired callback for detach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x0000014a | %1 (%2) %3The database [%4] format version is being held back to %6 due to application parameter setting of %5. Current default engine version: %7.\r\n
0x0000014b | %1 (%2) %3The database [%4] version was upgraded from %5 to %6. Current engine format version parameter setting: %7\r\n
0x0000014c | %1 (%2) %3The database [%4] version %5 is higher than the maximum version understood by the engine %6.\r\n
0x0000014d | %1 (%2) %3The database [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x0000014e | %1 (%2) %3The database [%4] has completed incremental reseed page patching operations for %5 pages.\r\n%n\r\n%nDetails:\r\n%nRange of Patching: %6\r\n%nTiming: %7\r\n
0x0000014f | %1 (%2) %3Replay of a %4 for database "%5" at log position %6 was deferred due to %7.  Additional information:  %8\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO or flush on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page some time in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %11\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 logical data checksum %6 failed to match logged scan check %7 checksum (seed %8) at log position %9.\r\n
0x0000021d | %1 (%2) %3Database %4: Page %5 was shown to be uninitialized at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).\r\n
0x0000021e | %1 (%2) %3Database %4: Page %5 (objid %6) has a logical corruption of type '%7'.\r\n%nDetails: %8\r\n
0x0000021f | %1 (%2) %3Previous log's accumulated segment checksum mismatch in logfile %4, Expected: %5, Actual: %6.\r\n
0x00000220 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a persisted lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000221 | %1 (%2) %3Database %4: Page %5 appears to be uninitialized at log position %10 on the remote node.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000222 | %1 (%2) %3The log generation (%4) is too low (%5) to be supported or replayed by this database engine (min supported %6).\r\n
0x00000223 | %1 (%2) %3The log generation (%4) is too high (%5) to be supported or replayed by this database engine (max supported %6).\r\n
0x00000224 | %1 (%2) %3The log generation's [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x00000225 | %1 (%2) %3A Database %4 has a page (pgno %5) with too few lines, operation attempted on line %6, actual number of lines on page %7.\r\n
0x00000226 | %1 (%2) %3Database %4: A compressed LV chunk failed verification during decompression due to a checksum mismatch. This indicates a logical corruption in the compress/decompress pipeline.\r\npgnoFDP = %5. Key = %6.\r\n
0x00000227 | %1 (%2) %3An attempt to flush to the file/disk buffers of "%4" failed after %5 seconds with system error %6: "%7".  The flush operation will fail with error %8.  If this error persists then the file system may be damaged and may need to be restored from a previous backup.\r\n
0x00000228 | %1 (%2) %3The log file at "%4" is corrupt with reason '%5'. Last valid segment was %6, current segment is %7. The expected checksum was %8 and the actual checksum was %9. The read completed with error-code %10.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %17 milliseconds (waiting %18 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %19 pages). It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n%n%tDbtime Distrib: %20\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %21 milliseconds (waiting %22 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %23 pages). In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n%n%tDbtime Distrib: %24\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x00000279 | %1 (%2) %3Recovery had to pause (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027a | %1 (%2) %3Recovery had to pause for a long time (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027b | %1 (%2) %3Failed to attach flush map file "%4" with error %5.\r\n
0x0000027c | %1 (%2) %3Flush map file "%4" will be deleted. Reason: %5.\r\n
0x0000027d | %1 (%2) %3New flush map file "%4" will be created to enable persisted lost flush detection.\r\n
0x0000027e | %1 (%2) %3Error %4 validating page %5 on flush map file "%6". The flush type of the database pages will be set to 'unknown' state.\r\n
0x0000027f | %1 (%2) %3Inconsistent timestamp detected on page %4 of flush map file "%5" (empty if flush map persistence in disabled). The maximum timestamp on the flush map is %6, but database page %7 has a timestamp of %8. If flush map persistence is enabled, this problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000280 | %1 (%2) %3Error %4 validating header page on flush map file "%5". The flush map file will be invalidated.\r\n%nAdditional information: %6\r\n
0x00000281 | %1 (%2) %3The log format feature version %5 could not be used due to the current log format %6, controlled by the parameter %4.\r\n
0x00000282 | %1 (%2) %3The database format feature version %5 could not be used due to the current database format %6, controlled by the parameter %4.\r\n
0x00000283 | %1 (%2) %3 Out of date NLS sort version detected on the database '%4' for Locale '%5', index sort version: (SortId=%6, Version=%7), current sort version: (SortId=%8, Version=%9).\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is not finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database shrink file operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database shrink file operation finished successfully and shrunk the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e9 | %1 (%2) %3Online Maintenance Database Checksumming background task is aborted for database '%4' at page %5, due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last properly completed checksumming task was on %6.\r\n
0x000002ea | %1 (%2) %3Online Maintenance Database Checksumming background task finished an interrupted and incomplete scan for database '%4'. Typical interruptions are due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last fully completed checksumming scan was on %5.\r\n
0x000002eb | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4', and in doing so has skipped %5 pages (%6%%).  prev stop: %7, this start: %8.%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Internal trace: %4 (%5)\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state:  %8% (%9 out of %10 buffers)\r\n%nCurrent cache size vs. target:  %11% (%12 MBs)\r\n%nPhysical Memory / RAM size:     %13 MBs\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5)\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x00000391 | %1 (%2) %3The parameter %4 was not set to one value by the previous ESE application instance, but set to a different value from the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000392 | %1 (%2) %3The parameter %4 was not set via the previous ESE application instance, but is set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000393 | %1 (%2) %3The parameter %4 was set via the previous ESE application instance, but is not set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000394 | %1 (%2) %3The beta feature %4 is enabled in %5 due to the beta site mode settings %6.\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x000009c4 | %1 (%2) %3An attempt to initialize the FPGA failed with error %4. Please make sure that the FPGA hardware is present and configured correctly.\r\n
0x000009c5 | %1 (%2) %3An attempt to acquire an FPGA slot during initialization failed. This indicates that there are more processes trying to use the FPGA than the available slots.\r\n
0x000009c6 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a transient failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c7 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a permanent FPGA failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c8 | %1 (%2) %3An attempt to acquire an FPGA slot event during initialization failed with system error %4: "%5".\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | System Device\r\n
0x00000013 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nAdditional Data:%n\r\n%7\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x0000006a | %1 (%2) %3The parameter %4 was attempted to be set to %5, but was overridden to %6 by the registry settings (at %7).\r\n
0x0000006b | %1 (%2) %3The parameter %4 was read from the registry settings (at %7), but the ESE engine rejected the value %5 with err %6.\r\n
0x0000006c | %1 (%2) %3The specific ESE configuration store is locked in a read inhibit state, clear the %1 registry value to enable ESE to continue and utilize the config store.\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has begun replaying logfile %4.\r\n%n\r\n%nPrevious Log Processing Stats: %5\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nSaved Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nRevived Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000148 | %1 (%2) %3The database engine has fired callback for attach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x00000149 | %1 (%2) %3The database engine has fired callback for detach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x0000014a | %1 (%2) %3The database [%4] format version is being held back to %6 due to application parameter setting of %5. Current default engine version: %7.\r\n
0x0000014b | %1 (%2) %3The database [%4] version was upgraded from %5 to %6. Current engine format version parameter setting: %7\r\n
0x0000014c | %1 (%2) %3The database [%4] version %5 is higher than the maximum version understood by the engine %6.\r\n
0x0000014d | %1 (%2) %3The database [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x0000014e | %1 (%2) %3The database [%4] has completed incremental reseed page patching operations for %5 pages.\r\n%n\r\n%nDetails:\r\n%nRange of Patching: %6\r\n%nTiming: %7\r\n
0x0000014f | %1 (%2) %3Replay of a %4 for database "%5" at log position %6 was deferred due to %7.  Additional information:  %8\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO or flush on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page some time in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %11\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 logical data checksum %6 failed to match logged scan check %7 checksum (seed %8) at log position %9.\r\n
0x0000021d | %1 (%2) %3Database %4: Page %5 was shown to be uninitialized at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).\r\n
0x0000021e | %1 (%2) %3Database %4: Page %5 (objid %6) has a logical corruption of type '%7'.\r\n%nDetails: %8\r\n
0x0000021f | %1 (%2) %3Previous log's accumulated segment checksum mismatch in logfile %4, Expected: %5, Actual: %6.\r\n
0x00000220 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a persisted lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000221 | %1 (%2) %3Database %4: Page %5 appears to be uninitialized at log position %10 on the remote node.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000222 | %1 (%2) %3The log generation (%4) is too low (%5) to be supported or replayed by this database engine (min supported %6).\r\n
0x00000223 | %1 (%2) %3The log generation (%4) is too high (%5) to be supported or replayed by this database engine (max supported %6).\r\n
0x00000224 | %1 (%2) %3The log generation's [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x00000225 | %1 (%2) %3A Database %4 has a page (pgno %5) with too few lines, operation attempted on line %6, actual number of lines on page %7.\r\n
0x00000226 | %1 (%2) %3Database %4: A compressed LV chunk failed verification during decompression due to a checksum mismatch. This indicates a logical corruption in the compress/decompress pipeline.\r\npgnoFDP = %5. Key = %6.\r\n
0x00000227 | %1 (%2) %3An attempt to flush to the file/disk buffers of "%4" failed after %5 seconds with system error %6: "%7".  The flush operation will fail with error %8.  If this error persists then the file system may be damaged and may need to be restored from a previous backup.\r\n
0x00000228 | %1 (%2) %3The log file at "%4" is corrupt with reason '%5'. Last valid segment was %6, current segment is %7. The expected checksum was %8 and the actual checksum was %9. The read completed with error-code %10.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x00000229 | %1 (%2) %3Failed looking up restore-map entry for database %4 with unexpected error %5.\r\n
0x0000022a | %1 (%2) %3The log segment read from the file "%4" at offset %6 (segment number %5) failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %17 milliseconds (waiting %18 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %19 pages). It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n%n%tDbtime Distrib: %20\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %21 milliseconds (waiting %22 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %23 pages). In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n%n%tDbtime Distrib: %24\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x00000279 | %1 (%2) %3Recovery had to pause (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027a | %1 (%2) %3Recovery had to pause for a long time (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027b | %1 (%2) %3Failed to attach flush map file "%4" with error %5.\r\n
0x0000027c | %1 (%2) %3Flush map file "%4" will be deleted. Reason: %5.\r\n
0x0000027d | %1 (%2) %3New flush map file "%4" will be created to enable persisted lost flush detection.\r\n
0x0000027e | %1 (%2) %3Error %4 validating page %5 on flush map file "%6". The flush type of the database pages will be set to 'unknown' state.\r\n
0x0000027f | %1 (%2) %3Inconsistent timestamp detected on page %4 of flush map file "%5" (empty if flush map persistence in disabled). The maximum timestamp on the flush map is %6, but database page %7 has a timestamp of %8. If flush map persistence is enabled, this problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000280 | %1 (%2) %3Error %4 validating header page on flush map file "%5". The flush map file will be invalidated.\r\n%nAdditional information: %6\r\n
0x00000281 | %1 (%2) %3The log format feature version %5 could not be used due to the current log format %6, controlled by the parameter %4.\r\n
0x00000282 | %1 (%2) %3The database format feature version %5 could not be used due to the current database format %6, controlled by the parameter %4.\r\n
0x00000283 | %1 (%2) %3 Out of date NLS sort version detected on the database '%4' for Locale '%5', index sort version: (SortId=%6, Version=%7), current sort version: (SortId=%8, Version=%9).\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n%n\r\nLast Runtime Scan Stats: %9\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is not finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\nLast Runtime Scan Stats: %10%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\nLast Runtime Scan Stats: %8%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database shrink file operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database shrink file operation finished successfully and shrunk the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database shrink file operation was not able to shrink the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e9 | %1 (%2) %3Online Maintenance Database Checksumming background task is aborted for database '%4' at page %5, due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last properly completed checksumming task was on %6.%n\r\n%n\r\nLast Runtime Scan Stats: %7%n\r\n
0x000002ea | %1 (%2) %3Online Maintenance Database Checksumming background task finished an interrupted and incomplete scan for database '%4'. Typical interruptions are due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last fully completed checksumming scan was on %5.\r\n
0x000002eb | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4', and in doing so has skipped %5 pages (%6%%).  prev stop: %7, this start: %8.%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Tag: %6. Internal trace: %4 (%5).\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state:  %8% (%9 out of %10 buffers)\r\n%nCurrent cache size vs. target:  %11% (%12 MBs)\r\n%nPhysical Memory / RAM size:     %13 MBs\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5). Tag: %6.\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x00000391 | %1 (%2) %3The parameter %4 was not set to one value by the previous ESE application instance, but set to a different value from the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000392 | %1 (%2) %3The parameter %4 was not set via the previous ESE application instance, but is set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000393 | %1 (%2) %3The parameter %4 was set via the previous ESE application instance, but is not set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000394 | %1 (%2) %3The beta feature %4 is enabled in %5 due to the beta site mode settings %6.\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x000009c4 | %1 (%2) %3An attempt to initialize the FPGA failed with error %4. Please make sure that the FPGA hardware is present and configured correctly.\r\n
0x000009c5 | %1 (%2) %3An attempt to acquire an FPGA slot during initialization failed. This indicates that there are more processes trying to use the FPGA than the available slots.\r\n
0x000009c6 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a transient failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c7 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a permanent FPGA failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c8 | %1 (%2) %3An attempt to acquire an FPGA slot event during initialization failed with system error %4: "%5".\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 10.0.17763.1

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | System Device\r\n
0x00000013 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nAdditional Data:%n\r\n%7\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x0000006a | %1 (%2) %3The parameter %4 was attempted to be set to %5, but was overridden to %6 by the registry settings (at %7).\r\n
0x0000006b | %1 (%2) %3The parameter %4 was read from the registry settings (at %7), but the ESE engine rejected the value %5 with err %6.\r\n
0x0000006c | %1 (%2) %3The specific ESE configuration store is locked in a read inhibit state, clear the %1 registry value to enable ESE to continue and utilize the config store.\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has finished replaying logfile %4.\r\n%n\r\n%nProcessing Stats: %5\r\n%nLog record of type '%6' was seen most frequently (%7 times)\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nSaved Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nRevived Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000148 | %1 (%2) %3The database engine has fired callback for attach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x00000149 | %1 (%2) %3The database engine has fired callback for detach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x0000014a | %1 (%2) %3The database [%4] format version is being held back to %6 due to application parameter setting of %5. Current default engine version: %7.\r\n
0x0000014b | %1 (%2) %3The database [%4] version was upgraded from %5 to %6. Current engine format version parameter setting: %7\r\n
0x0000014c | %1 (%2) %3The database [%4] version %5 is higher than the maximum version understood by the engine %6.\r\n
0x0000014d | %1 (%2) %3The database [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x0000014e | %1 (%2) %3The database [%4] has completed incremental reseed page patching operations for %5 pages.\r\n%n\r\n%nDetails:\r\n%nRange of Patching: %6\r\n%nTiming: %7\r\n
0x0000014f | %1 (%2) %3Replay of a %4 for database "%5" at log position %6 was deferred due to %7.  Additional information:  %8\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4. Error %6.\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO or flush on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page some time in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %11\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 logical data checksum %6 failed to match logged scan check %7 checksum (seed %8) at log position %9.\r\n
0x0000021d | %1 (%2) %3Database %4: Page %5 was shown to be uninitialized at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).\r\n
0x0000021e | %1 (%2) %3Database %4: Page %5 (objid %6) has a logical corruption of type '%7'.\r\n%nDetails: %8\r\n
0x0000021f | %1 (%2) %3Previous log's accumulated segment checksum mismatch in logfile %4, Expected: %5, Actual: %6.\r\n
0x00000220 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a persisted lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000221 | %1 (%2) %3Database %4: Page %5 appears to be uninitialized at log position %10 on the remote node.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000222 | %1 (%2) %3The log generation (%4) is too low (%5) to be supported or replayed by this database engine (min supported %6).\r\n
0x00000223 | %1 (%2) %3The log generation (%4) is too high (%5) to be supported or replayed by this database engine (max supported %6).\r\n
0x00000224 | %1 (%2) %3The log generation's [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x00000225 | %1 (%2) %3A Database %4 has a page (pgno %5) with too few lines, operation attempted on line %6, actual number of lines on page %7.\r\n
0x00000226 | %1 (%2) %3Database %4: A compressed LV chunk failed verification during decompression due to a checksum mismatch. This indicates a logical corruption in the compress/decompress pipeline.\r\npgnoFDP = %5. Key = %6.\r\n
0x00000227 | %1 (%2) %3An attempt to flush to the file/disk buffers of "%4" failed after %5 seconds with system error %6: "%7".  The flush operation will fail with error %8.  If this error persists then the file system may be damaged and may need to be restored from a previous backup.\r\n
0x00000228 | %1 (%2) %3The log file at "%4" is corrupt with reason '%5'. Last valid segment was %6, current segment is %7. The expected checksum was %8 and the actual checksum was %9. The read completed with error-code %10.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x00000229 | %1 (%2) %3Failed looking up restore-map entry for database %4 with unexpected error %5.\r\n
0x0000022a | %1 (%2) %3The log segment read from the file "%4" at offset %6 (segment number %5) failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %17 milliseconds (waiting %18 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %19 pages). It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n%n%tDbtime Distrib: %20\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %21 milliseconds (waiting %22 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %23 pages). In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n%n%tDbtime Distrib: %24\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x00000279 | %1 (%2) %3Recovery had to pause (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027a | %1 (%2) %3Recovery had to pause for a long time (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027b | %1 (%2) %3Failed to attach flush map file "%4" with error %5.\r\n
0x0000027c | %1 (%2) %3Flush map file "%4" will be deleted. Reason: %5.\r\n
0x0000027d | %1 (%2) %3New flush map file "%4" will be created to enable persisted lost flush detection.\r\n
0x0000027e | %1 (%2) %3Error %4 validating page %5 on flush map file "%6". The flush type of the database pages will be set to 'unknown' state.\r\n
0x0000027f | %1 (%2) %3Inconsistent timestamp detected on page %4 of flush map file "%5" (empty if flush map persistence in disabled). The maximum timestamp on the flush map is %6, but database page %7 has a timestamp of %8. If flush map persistence is enabled, this problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000280 | %1 (%2) %3Error %4 validating header page on flush map file "%5". The flush map file will be invalidated.\r\n%nAdditional information: %6\r\n
0x00000281 | %1 (%2) %3The log format feature version %5 could not be used due to the current log format %6, controlled by the parameter %4.\r\n
0x00000282 | %1 (%2) %3The database format feature version %5 could not be used due to the current database format %6, controlled by the parameter %4.\r\n
0x00000283 | %1 (%2) %3 Out of date NLS sort version detected on the database '%4' for Locale '%5', index sort version: (SortId=%6, Version=%7), current sort version: (SortId=%8, Version=%9).\r\n
0x00000284 | %1 (%2) %3A session has an outstanding transaction causing the checkpoint depth (of %4 logs) to exceed a quarter of the JET_paramCheckpointTooDeep setting.%n\r\n%n\r\nDetails:%n\r\nTransaction Context Info: %5%n\r\nTransaction Start Times: %6%n\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n%n\r\nLast Runtime Scan Stats: %9\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is not finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\nLast Runtime Scan Stats: %10%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\nLast Runtime Scan Stats: %8%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database file trimming operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database file trimming operation finished successfully and trimmed the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database file trimming operation was not able to trim the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database file trimming operation was not able to trim the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e9 | %1 (%2) %3Online Maintenance Database Checksumming background task is aborted for database '%4' at page %5, due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last properly completed checksumming task was on %6.%n\r\n%n\r\nLast Runtime Scan Stats: %7%n\r\n
0x000002ea | %1 (%2) %3Online Maintenance Database Checksumming background task finished an interrupted and incomplete scan for database '%4'. Typical interruptions are due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last fully completed checksumming scan was on %5.\r\n
0x000002eb | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4', and in doing so has skipped %5 pages (%6%%).  prev stop: %7, this start: %8.%n\r\n
0x000002ec | %1 (%2) %3The database file shrinkage operation completed successfully on database '%4'.%n\r\nDuration: %5 minute(s) and %6 second(s).%n\r\nInitial file size: %7 bytes (%8 page(s)).%n\r\nFinal file size: %9 bytes (%10 page(s)).%n\r\nInitial owned space: %11 bytes (%12 page(s)).%n\r\nFinal owned space: %13 bytes (%14 page(s)).%n\r\nData moved: %15 bytes (%16 page(s)).%n\r\n
0x000002ed | %1 (%2) %3The database file shrinkage operation failed on database '%4'.%n\r\nDuration: %5 minute(s) and %6 second(s).%n\r\nInitial file size: %7 bytes (%8 page(s)).%n\r\nFinal file size: %9 bytes (%10 page(s)).%n\r\nInitial owned space: %11 bytes (%12 page(s)).%n\r\nFinal owned space: %13 bytes (%14 page(s)).%n\r\nData moved: %15 bytes (%16 page(s)).%n\r\nError code: %17.%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Tag: %6. Internal trace: %4 (%5).\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state:  %8% (%9 out of %10 buffers)\r\n%nCurrent cache size vs. target:  %11% (%12 MBs)\r\n%nPhysical Memory / RAM size:     %13 MBs\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5). Tag: %6.\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x00000391 | %1 (%2) %3The parameter %4 was not set to one value by the previous ESE application instance, but set to a different value from the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000392 | %1 (%2) %3The parameter %4 was not set via the previous ESE application instance, but is set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000393 | %1 (%2) %3The parameter %4 was set via the previous ESE application instance, but is not set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000394 | %1 (%2) %3The beta feature %4 is enabled in %5 due to the beta site mode settings %6.\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x000009c4 | %1 (%2) %3An attempt to initialize the FPGA failed with error %4. Please make sure that the FPGA hardware is present and configured correctly.\r\n
0x000009c5 | %1 (%2) %3An attempt to acquire an FPGA slot during initialization failed. This indicates that there are more processes trying to use the FPGA than the available slots.\r\n
0x000009c6 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a transient failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c7 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a permanent FPGA failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c8 | %1 (%2) %3An attempt to acquire an FPGA slot event during initialization failed with system error %4: "%5".\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 10.0.18362.1

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | System Device\r\n
0x00000013 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nAdditional Data:%n\r\n%7\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x0000006a | %1 (%2) %3The parameter %4 was attempted to be set to %5, but was overridden to %6 by the registry settings (at %7).\r\n
0x0000006b | %1 (%2) %3The parameter %4 was read from the registry settings (at %7), but the ESE engine rejected the value %5 with err %6.\r\n
0x0000006c | %1 (%2) %3The specific ESE configuration store is locked in a read inhibit state, clear the %1 registry value to enable ESE to continue and utilize the config store.\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has finished replaying logfile %4.\r\n%n\r\n%nProcessing Stats: %5\r\n%nLog record of type '%6' was seen most frequently (%7 times)\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nSaved Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nRevived Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000148 | %1 (%2) %3The database engine has fired callback for attach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x00000149 | %1 (%2) %3The database engine has fired callback for detach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x0000014a | %1 (%2) %3The database [%4] format version is being held back to %6 due to application parameter setting of %5. Current default engine version: %7.\r\n
0x0000014b | %1 (%2) %3The database [%4] version was upgraded from %5 to %6. Current engine format version parameter setting: %7\r\n
0x0000014c | %1 (%2) %3The database [%4] version %5 is higher than the maximum version understood by the engine %6.\r\n
0x0000014d | %1 (%2) %3The database [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x0000014e | %1 (%2) %3The database [%4] has completed incremental reseed page patching operations for %5 pages.\r\n%n\r\n%nDetails:\r\n%nRange of Patching: %6\r\n%nTiming: %7\r\n
0x0000014f | %1 (%2) %3Replay of a %4 for database "%5" at log position %6 was deferred due to %7.  Additional information:  %8\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4.%n\r\nAdditional information:%n\r\n%tError code: %6%n\r\n%tLog position: %7%n\r\n%tPage timestamp: %8%n\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO or flush on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).%n\r\nTag: %11%n\r\nFatal: %12%n\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10 (currently replaying log position %12).  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page some time in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %11\r\n%n%tTotal number of pages affected: %13\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 logical data checksum %6 failed to match logged scan check %7 checksum (seed %8) at log position %9.\r\n
0x0000021d | %1 (%2) %3Database %4: Page %5 was shown to be uninitialized at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).\r\n
0x0000021e | %1 (%2) %3Database %4: Page %5 (objid %6) has a logical corruption of type '%7'.\r\n%nDetails: %8\r\n
0x0000021f | %1 (%2) %3Previous log's accumulated segment checksum mismatch in logfile %4, Expected: %5, Actual: %6.\r\n
0x00000220 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a persisted lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000221 | %1 (%2) %3Database %4: Page %5 appears to be uninitialized at log position %10 on the remote node.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000222 | %1 (%2) %3The log generation (%4) is too low (%5) to be supported or replayed by this database engine (min supported %6).\r\n
0x00000223 | %1 (%2) %3The log generation (%4) is too high (%5) to be supported or replayed by this database engine (max supported %6).\r\n
0x00000224 | %1 (%2) %3The log generation's [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x00000225 | %1 (%2) %3Database %4 has a page (pgno %5) with too few lines, operation attempted on line %6, actual number of lines on page %7.\r\n
0x00000226 | %1 (%2) %3Database %4: A compressed LV chunk failed verification during decompression due to a checksum mismatch. This indicates a logical corruption in the compress/decompress pipeline.\r\npgnoFDP = %5. Key = %6.\r\n
0x00000227 | %1 (%2) %3An attempt to flush to the file/disk buffers of "%4" failed after %5 seconds with system error %6: "%7".  The flush operation will fail with error %8.  If this error persists then the file system may be damaged and may need to be restored from a previous backup.\r\n
0x00000228 | %1 (%2) %3The log file at "%4" is corrupt with reason '%5'. Last valid segment was %6, current segment is %7. The expected checksum was %8 and the actual checksum was %9. The read completed with error-code %10.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x00000229 | %1 (%2) %3Failed looking up restore-map entry for database %4 with unexpected error %5.\r\n
0x0000022a | %1 (%2) %3The log segment read from the file "%4" at offset %6 (segment number %5) failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000022b | %1 (%2) %3Database %4: Page %5 failed verification due not containing any data at log position %6 (currently replaying log position %7).  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page some time in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %9\r\n%n%tTotal number of pages affected: %10\r\n
0x0000022c | %1 (%2) %3Database %4: Data in line %5 on pgno %6 failed to decompress.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %17 milliseconds (waiting %18 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %19 pages). It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n%n%tDbtime Distrib: %20\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %21 milliseconds (waiting %22 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %23 pages). In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n%n%tDbtime Distrib: %24\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x00000279 | %1 (%2) %3Recovery had to pause (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027a | %1 (%2) %3Recovery had to pause for a long time (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027b | %1 (%2) %3Failed to attach flush map file "%4" with error %5.\r\n
0x0000027c | %1 (%2) %3Flush map file "%4" will be deleted. Reason: %5.\r\n
0x0000027d | %1 (%2) %3New flush map file "%4" will be created to enable persisted lost flush detection.\r\n
0x0000027e | %1 (%2) %3Error %4 validating page %5 on flush map file "%6". The flush type of the database pages will be set to 'unknown' state.\r\n
0x0000027f | %1 (%2) %3Inconsistent timestamp detected on page %4 of flush map file "%5" (empty if flush map persistence in disabled). The maximum timestamp on the flush map is %6, but database page %7 has a timestamp of %8. If flush map persistence is enabled, this problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000280 | %1 (%2) %3Error %4 validating header page on flush map file "%5". The flush map file will be invalidated.\r\n%nAdditional information: %6\r\n
0x00000281 | %1 (%2) %3The log format feature version %5 could not be used due to the current log format %6, controlled by the parameter %4.\r\n
0x00000282 | %1 (%2) %3The database format feature version %5 could not be used due to the current database format %6, controlled by the parameter %4.\r\n
0x00000283 | %1 (%2) %3 Out of date NLS sort version detected on the database '%4' for Locale '%5', index sort version: (SortId=%6, Version=%7), current sort version: (SortId=%8, Version=%9).\r\n
0x00000284 | %1 (%2) %3A session has an outstanding transaction causing the checkpoint depth (of %4 logs) to exceed a quarter of the JET_paramCheckpointTooDeep setting.%n\r\n%n\r\nDetails:%n\r\nTransaction Context Info: %5%n\r\nTransaction Start Times: %6%n\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n%n\r\nLast Runtime Scan Stats: %9\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is not finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\nAverage free space on Record pages: %10 (%11 pages scanned)%n\r\nAverage free space on LV pages: %12 (%13 pages scanned)%n\r\nLast Runtime Scan Stats: %10%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\nAverage free space on Record pages: %9 (%10 pages scanned)%n\r\nAverage free space on LV pages: %11 (%12 pages scanned)%n\r\nLast Runtime Scan Stats: %8%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database file trimming operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database file trimming operation finished successfully and trimmed the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database file trimming operation was not able to trim the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database file trimming operation was not able to trim the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e9 | %1 (%2) %3Online Maintenance Database Checksumming background task is aborted for database '%4' at page %5, due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last properly completed checksumming task was on %6.%n\r\n%n\r\nLast Runtime Scan Stats: %7%n\r\n
0x000002ea | %1 (%2) %3Online Maintenance Database Checksumming background task finished an interrupted and incomplete scan for database '%4'. Typical interruptions are due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last fully completed checksumming scan was on %5.\r\n
0x000002eb | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4', and in doing so has skipped %5 pages (%6%%).  prev stop: %7, this start: %8.%n\r\n
0x000002ec | %1 (%2) %3The database file shrinkage operation completed successfully on database '%4'.%n\r\nDuration: %5 minute(s) and %6 second(s).%n\r\nInitial file size: %7 bytes (%8 page(s)).%n\r\nFinal file size: %9 bytes (%10 page(s)).%n\r\nInitial owned space: %11 bytes (%12 page(s)).%n\r\nFinal owned space: %13 bytes (%14 page(s)).%n\r\nData moved: %15 bytes (%16 page(s)).%n\r\nReturn code: %17%n\r\nStop reason: %18%n\r\n
0x000002ed | %1 (%2) %3The database file shrinkage operation failed on database '%4'.%n\r\nDuration: %5 minute(s) and %6 second(s).%n\r\nInitial file size: %7 bytes (%8 page(s)).%n\r\nFinal file size: %9 bytes (%10 page(s)).%n\r\nInitial owned space: %11 bytes (%12 page(s)).%n\r\nFinal owned space: %13 bytes (%14 page(s)).%n\r\nData moved: %15 bytes (%16 page(s)).%n\r\nError code: %17%n\r\nStop reason: %18%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Tag: %6. Internal trace: %4 (%5).\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state:  %8% (%9 out of %10 buffers)\r\n%nCurrent cache size vs. target:  %11% (%12 MBs)\r\n%nPhysical Memory / RAM size:     %13 MBs\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5). Tag: %6.\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x00000391 | %1 (%2) %3The parameter %4 was not set to one value by the previous ESE application instance, but set to a different value from the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000392 | %1 (%2) %3The parameter %4 was not set via the previous ESE application instance, but is set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000393 | %1 (%2) %3The parameter %4 was set via the previous ESE application instance, but is not set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000394 | %1 (%2) %3The beta feature %4 is enabled in %5 due to the beta site mode settings %6.\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x000009c4 | %1 (%2) %3An attempt to initialize the FPGA failed with error %4. Please make sure that the FPGA hardware is present and configured correctly.\r\n
0x000009c5 | %1 (%2) %3An attempt to acquire an FPGA slot during initialization failed. This indicates that there are more processes trying to use the FPGA than the available slots.\r\n
0x000009c6 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a transient failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c7 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a permanent FPGA failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c8 | %1 (%2) %3An attempt to acquire an FPGA slot event during initialization failed with system error %4: "%5".\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | System Device\r\n
0x00000013 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nAdditional Data:%n\r\n%7\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x0000006a | %1 (%2) %3The parameter %4 was attempted to be set to %5, but was overridden to %6 by the registry settings (at %7).\r\n
0x0000006b | %1 (%2) %3The parameter %4 was read from the registry settings (at %7), but the ESE engine rejected the value %5 with err %6.\r\n
0x0000006c | %1 (%2) %3The specific ESE configuration store is locked in a read inhibit state, clear the %1 registry value to enable ESE to continue and utilize the config store.\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has finished replaying logfile %4.\r\n%n\r\n%nProcessing Stats: %5\r\n%nLog record of type '%6' was seen most frequently (%7 times)\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nSaved Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nRevived Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000148 | %1 (%2) %3The database engine has fired callback for attach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x00000149 | %1 (%2) %3The database engine has fired callback for detach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x0000014a | %1 (%2) %3The database [%4] format version is being held back to %6 due to application parameter setting of %5. Current default engine version: %7.\r\n
0x0000014b | %1 (%2) %3The database [%4] version was upgraded from %5 to %6. Current engine format version parameter setting: %7\r\n
0x0000014c | %1 (%2) %3The database [%4] version %5 is higher than the maximum version understood by the engine %6.\r\n
0x0000014d | %1 (%2) %3The database [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x0000014e | %1 (%2) %3The database [%4] has completed incremental reseed page patching operations for %5 pages.\r\n%n\r\n%nDetails:\r\n%nRange of Patching: %6\r\n%nTiming: %7\r\n
0x0000014f | %1 (%2) %3Replay of a %4 for database "%5" at log position %6 was deferred due to %7.  Additional information:  %8\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4.%n\r\nAdditional information:%n\r\n%tError code: %6%n\r\n%tLog position: %7%n\r\n%tPage timestamp: %8%n\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO or flush on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).%n\r\nTag: %11%n\r\nFatal: %12%n\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10 (currently replaying log position %12).  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on-page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page some time in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %11\r\n%n%tTotal number of pages affected: %13\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7, Flags: %9) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.%n\r\nAdditional information:%n\r\n%tSource: %11%n\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.%n\r\nAdditional information:%n\r\n%tSource: %11%n\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 logical data checksum %6 failed to match logged scan check %7 checksum (seed %8) at log position %9.%n\r\nAdditional information:%n\r\n%tSource: %10%n\r\n
0x0000021d | %1 (%2) %3Database %4: Page %5 was shown to be uninitialized at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).%n\r\nAdditional information:%n\r\n%tSource: %9%n\r\n
0x0000021e | %1 (%2) %3Database %4: Page %5 (objid %6) has a logical corruption of type '%7'.\r\n%nDetails: %8\r\n
0x0000021f | %1 (%2) %3Previous log's accumulated segment checksum mismatch in logfile %4, Expected: %5, Actual: %6.\r\n
0x00000220 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a persisted lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000221 | %1 (%2) %3Database %4: Page %5 appears to be uninitialized at log position %10 on the remote node.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.%n\r\nAdditional information:%n\r\n%tSource: %11%n\r\n
0x00000222 | %1 (%2) %3The log generation (%4) is too low (%5) to be supported or replayed by this database engine (min supported %6).\r\n
0x00000223 | %1 (%2) %3The log generation (%4) is too high (%5) to be supported or replayed by this database engine (max supported %6).\r\n
0x00000224 | %1 (%2) %3The log generation's [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x00000225 | %1 (%2) %3Database %4 has a page (pgno %5) with too few lines, operation attempted on line %6, actual number of lines on page %7.\r\n
0x00000226 | %1 (%2) %3Database %4: A compressed LV chunk failed verification during decompression due to a checksum mismatch. This indicates a logical corruption in the compress/decompress pipeline.\r\npgnoFDP = %5. Key = %6.\r\n
0x00000227 | %1 (%2) %3An attempt to flush to the file/disk buffers of "%4" failed after %5 seconds with system error %6: "%7".  The flush operation will fail with error %8.  If this error persists then the file system may be damaged and may need to be restored from a previous backup.\r\n
0x00000228 | %1 (%2) %3The log file at "%4" is corrupt with reason '%5'. Last valid segment was %6, current segment is %7. The expected checksum was %8 and the actual checksum was %9. The read completed with error-code %10.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x00000229 | %1 (%2) %3Failed looking up restore-map entry for database %4 with unexpected error %5.\r\n
0x0000022a | %1 (%2) %3The log segment read from the file "%4" at offset %6 (segment number %5) failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000022b | %1 (%2) %3Database %4: Page %5 failed verification due not containing any data at log position %6 (currently replaying log position %7).  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page some time in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %9\r\n%n%tTotal number of pages affected: %10\r\n
0x0000022c | %1 (%2) %3Database %4: Data in line %5 on pgno %6 failed to decompress.\r\n
0x0000022d | %1 (%2) %3Database %4: Page %5 was shown to be beyond the end of file at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).%n\r\nAdditional information:%n\r\n%tSource: %9%n\r\n
0x0000022e | %1 (%2) %3There is a gap in sequence number following logfile generation %4. Highest logfile generation present is %5.\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %17 milliseconds (waiting %18 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %19 pages). It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n%n%tDbtime Distrib: %20\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %21 milliseconds (waiting %22 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %23 pages). In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tType: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n%n%tDbtime Distrib: %24\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x00000279 | %1 (%2) %3Recovery had to pause (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027a | %1 (%2) %3Recovery had to pause for a long time (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027b | %1 (%2) %3Failed to attach flush map file "%4" with error %5.\r\n
0x0000027c | %1 (%2) %3Flush map file "%4" will be deleted. Reason: %5.\r\n
0x0000027d | %1 (%2) %3New flush map file "%4" will be created to enable persisted lost flush detection.\r\n
0x0000027e | %1 (%2) %3Error %4 validating page %5 on flush map file "%6". The flush type of the database pages will be set to 'unknown' state.\r\n
0x0000027f | %1 (%2) %3Inconsistent timestamp detected on page %4 of flush map file "%5" (empty if flush map persistence in disabled). The maximum timestamp on the flush map is %6, but database page %7 has a timestamp of %8. If flush map persistence is enabled, this problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000280 | %1 (%2) %3Error %4 validating header page on flush map file "%5". The flush map file will be invalidated.\r\n%nAdditional information: %6\r\n
0x00000281 | %1 (%2) %3The log format feature version %5 could not be used due to the current log format %6, controlled by the parameter %4.\r\n
0x00000282 | %1 (%2) %3The database format feature version %5 could not be used due to the current database format %6, controlled by the parameter %4.\r\n
0x00000283 | %1 (%2) %3 Out of date NLS sort version detected on the database '%4' for Locale '%5', index sort version: (SortId=%6, Version=%7), current sort version: (SortId=%8, Version=%9).\r\n
0x00000284 | %1 (%2) %3A session has an outstanding transaction causing the checkpoint depth (of %4 logs) to exceed a quarter of the JET_paramCheckpointTooDeep setting.%n\r\n%n\r\nDetails:%n\r\nTransaction Context Info: %5%n\r\nTransaction Start Times: %6%n\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n%n\r\nLast Runtime Scan Stats: %9\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is not finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\nAverage free space on Record pages: %10 (%11 pages scanned)%n\r\nAverage free space on LV pages: %12 (%13 pages scanned)%n\r\nLast Runtime Scan Stats: %10%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\nAverage free space on Record pages: %9 (%10 pages scanned)%n\r\nAverage free space on LV pages: %11 (%12 pages scanned)%n\r\nLast Runtime Scan Stats: %8%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database file trimming operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database file trimming operation finished successfully and trimmed the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database file trimming operation was not able to trim the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database file trimming operation was not able to trim the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e9 | %1 (%2) %3Online Maintenance Database Checksumming background task is aborted for database '%4' at page %5, due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last properly completed checksumming task was on %6.%n\r\n%n\r\nLast Runtime Scan Stats: %7%n\r\n
0x000002ea | %1 (%2) %3Online Maintenance Database Checksumming background task finished an interrupted and incomplete scan for database '%4'. Typical interruptions are due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last fully completed checksumming scan was on %5.\r\n
0x000002eb | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4', and in doing so has skipped %5 pages (%6%%).  prev stop: %7, this start: %8.%n\r\n
0x000002ec | %1 (%2) %3The database file shrinkage operation completed successfully on database '%4'.%n\r\nInitial file size: %7 bytes (%8 page(s)).%n\r\nFinal file size: %9 bytes (%10 page(s)).%n\r\nInitial owned space: %11 bytes (%12 page(s)).%n\r\nFinal owned space: %13 bytes (%14 page(s)).%n\r\nData moved: %15 bytes (%16 page(s)).%n\r\nReturn code: %17%n\r\nStop reason: %18%n\r\nTotal time: %5 minute(s) and %6 second(s).%n\r\nPct. time in extent maintenance: %19%%%n\r\nPct. time in file truncation: %20%%%n\r\nPct. time in page categorization: %21%%%n\r\nPct. time in data move: %22%%%n\r\nPct. remaining time: %23%%%n\r\n
0x000002ed | %1 (%2) %3The database file shrinkage operation failed on database '%4'.%n\r\nInitial file size: %7 bytes (%8 page(s)).%n\r\nFinal file size: %9 bytes (%10 page(s)).%n\r\nInitial owned space: %11 bytes (%12 page(s)).%n\r\nFinal owned space: %13 bytes (%14 page(s)).%n\r\nData moved: %15 bytes (%16 page(s)).%n\r\nError code: %17%n\r\nStop reason: %18%n\r\nTotal time: %5 minute(s) and %6 second(s).%n\r\nPct. time in extent maintenance: %19%%%n\r\nPct. time in file truncation: %20%%%n\r\nPct. time in page categorization: %21%%%n\r\nPct. time in data move: %22%%%n\r\nPct. remaining time: %23%%%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Tag: %6. Internal trace: %4 (%5).\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state:  %8% (%9 out of %10 buffers)\r\n%nCurrent cache size vs. target:  %11% (%12 MBs)\r\n%nPhysical Memory / RAM size:     %13 MBs\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5). Tag: %6.\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x00000391 | %1 (%2) %3The parameter %4 was not set to one value by the previous ESE application instance, but set to a different value from the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000392 | %1 (%2) %3The parameter %4 was not set via the previous ESE application instance, but is set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000393 | %1 (%2) %3The parameter %4 was set via the previous ESE application instance, but is not set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000394 | %1 (%2) %3The beta feature %4 is enabled in %5 due to the beta site mode settings %6.\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x000009c4 | %1 (%2) %3An attempt to initialize the FPGA failed with error %4. Please make sure that the FPGA hardware is present and configured correctly.\r\n
0x000009c5 | %1 (%2) %3An attempt to acquire an FPGA slot during initialization failed. This indicates that there are more processes trying to use the FPGA than the available slots.\r\n
0x000009c6 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a transient failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c7 | %1 (%2) %3An FPGA operation failed with error %4. This error was classified as a permanent FPGA failure. The engine has encountered the following FPGA failures since it started:\r\nPermanent = %5, Transient = %6, HEX Resets = %7\r\n
0x000009c8 | %1 (%2) %3An attempt to acquire an FPGA slot event during initialization failed with system error %4: "%5".\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000000 | %1 (%2) %3%4\r\n
0x00000001 | General\r\n
0x00000002 | Database Page Cache\r\n
0x00000003 | Logging/Recovery\r\n
0x00000004 | Space Management\r\n
0x00000005 | Table/Column/Index Definition\r\n
0x00000006 | Record Manipulation\r\n
0x00000007 | Performance\r\n
0x00000008 | Database Repair\r\n
0x00000009 | Database Conversion\r\n
0x0000000a | Online Defragmentation\r\n
0x0000000b | System Parameter Settings\r\n
0x0000000c | Database Corruption\r\n
0x0000000d | Database Zeroing\r\n
0x0000000e | Transaction Manager\r\n
0x0000000f | Resource Failure Simulation\r\n
0x00000010 | ShadowCopy\r\n
0x00000011 | Failure Items\r\n
0x00000012 | System Device\r\n
0x00000013 | System Device\r\n
0x00000014 | <EOL>\r\n
0x00000064 | %1 (%2) %3The database engine %4.%5.%6.%7 started.\r\n
0x00000065 | %1 (%2) %3The database engine stopped.\r\n
0x00000066 | %1 (%2) %3The database engine (%5.%6.%7.%8) is starting a new instance (%4).\r\n
0x00000067 | %1 (%2) %3The database engine stopped the instance (%4).\r\n%n\r\n%nDirty Shutdown: %6\r\n%n\r\n%nInternal Timing Sequence: %5\r\n
0x00000068 | %1 (%2) %3The database engine stopped the instance (%4) with error (%5).\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x00000069 | %1 (%2) %3The database engine started a new instance (%4). (Time=%5 seconds)\r\n%n\r\n%nAdditional Data:%n\r\n%7\r\n%n\r\n%nInternal Timing Sequence: %6\r\n
0x0000006a | %1 (%2) %3The parameter %4 was attempted to be set to %5, but was overridden to %6 by the registry settings (at %7).\r\n
0x0000006b | %1 (%2) %3The parameter %4 was read from the registry settings (at %7), but the ESE engine rejected the value %5 with err %6.\r\n
0x0000006c | %1 (%2) %3The specific ESE configuration store is locked in a read inhibit state, clear the %1 registry value to enable ESE to continue and utilize the config store.\r\n
0x000000c8 | %1 (%2) %3The database engine is starting a full backup.\r\n
0x000000c9 | %1 (%2) %3The database engine is starting an incremental backup.\r\n
0x000000ca | %1 (%2) %3The database engine has completed the backup procedure successfully.\r\n
0x000000cb | %1 (%2) %3The database engine has stopped the backup with error %4.\r\n
0x000000cc | %1 (%2) %3The database engine is restoring from backup. Restore will begin replaying logfiles in folder %4 and continue rolling forward logfiles in folder %5.\r\n
0x000000cd | %1 (%2) %3The database engine has stopped restoring.\r\n
0x000000ce | %1 (%2) %3Database %4 cannot be incrementally backed-up. You must first perform a full backup before performing an incremental backup.\r\n
0x000000cf | %1 (%2) %3The database engine has stopped backup because it was halted by the client or the connection with the client failed.\r\n
0x000000d2 | %1 (%2) %3A full backup is starting.\r\n
0x000000d3 | %1 (%2) %3An incremental backup is starting.\r\n
0x000000d4 | %1 (%2) %3A shadow copy backup is starting.\r\n
0x000000d5 | %1 (%2) %3The backup procedure has been successfully completed.\r\n
0x000000d6 | %1 (%2) %3The backup has stopped with error %4.\r\n
0x000000d7 | %1 (%2) %3The backup has been stopped because it was halted by the client or the connection with the client failed.\r\n
0x000000d8 | %1 (%2) %3A database location change was detected from '%4' to '%5'.\r\n
0x000000d9 | %1 (%2) %3Error (%4) during backup of a database (file %5). The database will be unable to restore.\r\n
0x000000da | %1 (%2) %3Error (%4) during copy or backup of file %5.\r\n
0x000000db | %1 (%2) %3Error (%4) occured during database headers update with the backup information.\r\n
0x000000dc | %1 (%2) %3Starting the copy or backup of the file %4 (size %5).\r\n
0x000000dd | %1 (%2) %3Ending the copy or backup of the file %4.\r\n
0x000000de | %1 (%2) %3Ending the backup of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x000000df | %1 (%2) %3Starting the backup of log files (range %4 - %5). \r\n
0x000000e0 | %1 (%2) %3Deleting log files %4 to %5. \r\n
0x000000e1 | %1 (%2) %3No log files can be truncated. \r\n
0x000000e2 | %1 (%2) %3The backup has been stopped prematurely (possibly because the instance is terminating).\r\n
0x000000e3 | %1 (%2) %3There were %4 log file(s) not found in the log range we attempted to truncate. \r\n
0x000000f0 | %1 (%2) %3An internal copy (for seeding or analysis purposes) is starting. The streaming ESE backup APIs are being used for the transfer method.\r\n
0x000000f3 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) procedure has been successfully completed.\r\n
0x000000f4 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has stopped. Error: %4.\r\n
0x000000f5 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped because it was halted by the client or because the connection with the client failed.\r\n
0x000000fc | %1 (%2) %3Ending the internal copy (for seeding or analysis purposes) of the file %4. Not all data in the file has been read (read %5 bytes out of %6 bytes).\r\n
0x00000100 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) has been stopped prematurely, possibly because the instance is terminating.\r\n
0x00000101 | %1 (%2) %3The internal database copy (for seeding or analysis purposes) of database %4 during recovery has been suspended. It took %5 seconds to wait for client to close the backup context.\r\n
0x0000012c | %1 (%2) %3The database engine is initiating recovery steps.\r\n
0x0000012d | %1 (%2) %3The database engine has finished replaying logfile %4.\r\n%n\r\n%nProcessing Stats: %5\r\n%nLog record of type '%6' was seen most frequently (%7 times)\r\n
0x0000012e | %1 (%2) %3The database engine has successfully completed recovery steps.\r\n
0x0000012f | %1 (%2) %3Database engine error %4 occurred.\r\n
0x00000130 | %1 (%2) %3The database engine has successfully completed replay steps.\r\n
0x00000145 | %1 (%2) %3The database engine created a new database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000146 | %1 (%2) %3The database engine attached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nSaved Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000147 | %1 (%2) %3The database engine detached a database (%4, %5). (Time=%6 seconds)\r\n%n\r\n%nRevived Cache: %8\r\n%nAdditional Data: %9\r\n%n\r\n%nInternal Timing Sequence: %7\r\n
0x00000148 | %1 (%2) %3The database engine has fired callback for attach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x00000149 | %1 (%2) %3The database engine has fired callback for detach of database %4 during recovery at log position %5. The callback returned %6.\r\n
0x0000014a | %1 (%2) %3The database [%4] format version is being held back to %6 due to application parameter setting of %5. Current default engine version: %7.\r\n
0x0000014b | %1 (%2) %3The database [%4] version was upgraded from %5 to %6. Current engine format version parameter setting: %7\r\n
0x0000014c | %1 (%2) %3The database [%4] version %5 is higher than the maximum version understood by the engine %6.\r\n
0x0000014d | %1 (%2) %3The database [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x0000014e | %1 (%2) %3The database [%4] has completed incremental reseed page patching operations for %5 pages.\r\n%n\r\n%nDetails:\r\n%nRange of Patching: %6\r\n%nTiming: %7\r\n
0x0000014f | %1 (%2) %3Replay of a %4 for database "%5" at log position %6 was deferred due to %7.  Additional information:  %8\r\n
0x0000018e | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %9) for %6 bytes failed verification. Bit %8 was corrupted and was corrected but page verification failed with error %7.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000018f | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000190 | %1 (%2) %3Synchronous overlapped read page time error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000191 | %1 (%2) %3Synchronous overlapped write page issue error %4 occurred.\r\n
0x00000192 | %1 (%2) %3Synchronous overlapped write page error %4 occurred.\r\n
0x00000193 | %1 (%2) %3Synchronous overlapped patch file write page error %4 occurred.\r\n
0x00000194 | %1 (%2) %3Synchronous read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000195 | %1 (%2) %3Pre-read page checksum error %4 occurred. If this error persists, please restore the database from a previous backup.\r\n
0x00000196 | %1 (%2) %3Direct read found corrupted page %4 with error %5. If this error persists, please restore the database from a previous backup.\r\n
0x00000197 | %1 (%2) %3Buffer I/O thread termination error %4 occurred.\r\n
0x00000198 | %1 (%2) %3Unable to write to logfile %4. Error %5.\r\n
0x00000199 | %1 (%2) %3Unable to write to the header of logfile %4. Error %5.\r\n
0x0000019a | %1 (%2) %3Unable to read logfile %4. Error %5.\r\n
0x0000019b | %1 (%2) %3The log version stamp of logfile %4 does not match the database engine version stamp. The logfiles may be the wrong version for the database.\r\n
0x0000019c | %1 (%2) %3Unable to read the header of logfile %4. Error %5.\r\n
0x0000019d | %1 (%2) %3Unable to create a new logfile because the database cannot write to the log drive. The drive may be read-only, out of disk space, misconfigured, or corrupted. Error %4.\r\n
0x0000019e | %1 (%2) %3Unable to write to section 0 while flushing logfile %4. Error %5.\r\n
0x0000019f | %1 (%2) %3Unable to write to section 1 while flushing logfile %4. Error %5.\r\n
0x000001a0 | %1 (%2) %3Unable to write to section 2 while flushing logfile %4. Error %5.\r\n
0x000001a1 | %1 (%2) %3Unable to write to section 3 while flushing logfile %4. Error %5.\r\n
0x000001a2 | %1 (%2) %3Error %5 occurred while opening a newly-created logfile %4.\r\n
0x000001a3 | %1 (%2) %3Unable to read page %5 of database %4.%n\r\nAdditional information:%n\r\n%tError code: %6%n\r\n%tLog position: %7%n\r\n%tPage timestamp: %8%n\r\n
0x000001a4 | %1 (%2) %3Unable to read the header of database %4. Error %5. The database may have been moved and therefore may no longer be located where the logs expect it to be.\r\n
0x000001a5 | %1 (%2) %3The database %4 created at %5 was not recovered. The recovered database was created at %5.\r\n
0x000001a6 | %1 (%2) %3The database %4 created at %5 was not recovered.\r\n
0x000001a7 | %1 (%2) %3The database engine found a bad page.\r\n
0x000001a8 | %1 (%2) %3The database disk is full. Deleting logfiles to recover disk space may make the database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001a9 | %1 (%2) %3The database signature does not match the log signature for database %4.\r\n
0x000001aa | %1 (%2) %3The database engine could not find the file or folder called %4.\r\n
0x000001ab | %1 (%2) %3The database engine could not access the file called %4.\r\n
0x000001ac | %1 (%2) %3The database engine is rejecting update operations due to low free disk space on the log disk.\r\n
0x000001ad | %1 (%2) %3The database engine log disk is full. Deleting logfiles to recover disk space may make your database unstartable if the database file(s) are not in a Clean Shutdown state. Numbered logfiles may be moved, but not deleted, if and only if the database file(s) are in a Clean Shutdown state. Do not move %4.\r\n
0x000001ae | %1 (%2) %3Database %4 and its patch file do not match.\r\n
0x000001af | %1 (%2) %3The starting restored logfile %4 is too high. It should start from logfile %5.\r\n
0x000001b0 | %1 (%2) %3The ending restored logfile %4 is too low. It should end at logfile %5.\r\n
0x000001b1 | %1 (%2) %3The restored logfile %4 does not have the correct log signature.\r\n
0x000001b2 | %1 (%2) %3The timestamp for restored logfile %4 does not match the timestamp recorded in the logfile previous to it.\r\n
0x000001b3 | %1 (%2) %3The restored logfile %4 is missing.\r\n
0x000001b4 | %1 (%2) %3The signature of logfile %4 does not match other logfiles. Recovery cannot succeed unless all signatures match. Logfiles %5 to %6 have been deleted.\r\n
0x000001b5 | %1 (%2) %3There is a gap in sequence number between logfile %4 and the logfiles previous to it. Logfiles %5 to 0x%6 have been deleted so that recovery can complete.\r\n
0x000001b6 | %1 (%2) %3The backup database %4 must be a multiple of 4 KB.\r\n
0x000001b7 | %1 (%2) %3Unable to write a shadowed header for file %4. Error %5.\r\n
0x000001b8 | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x000001b9 | %1 (%2) %3File system error %5 during IO on database %4. If this error persists, the database file may be damaged and may need to be restored from a previous backup.\r\n
0x000001ba | %1 (%2) %3IO size mismatch on database %4, IO size %5 expected while returned size is %6.\r\n
0x000001bb | %1 (%2) %3File system error %5 during IO or flush on logfile %4.\r\n
0x000001bc | %1 (%2) %3IO size mismatch on logfile %4, IO size %5 expected while returned size is %6.\r\n
0x000001bd | %1 (%2) %3The database %4 has reached its maximum size of %5 MB. If the database cannot be restarted, an offline defragmentation may be performed to reduce its size.\r\n
0x000001be | %1 (%2) %3Database recovery stopped abruptly while redoing logfile %4 (%5,%6). The logs after this point may not be recognizable and will not be processed.\r\n
0x000001bf | %1 (%2) %3A bad page link (error %4) has been detected in a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %7 (%8 => %9, %10).%n\r\nTag: %11%n\r\nFatal: %12%n\r\n
0x000001c0 | %1 (%2) %3Data inconsistency detected in table %4 of database %5 (%6,%7).\r\n
0x000001c1 | %1 (%2) %3Streaming data allocation inconsistency detected (%4,%5).\r\n
0x000001c2 | %1 (%2) %3A gap in the logfile sequence was detected. Logfile %4 is missing.  Other logfiles past this one may also be required. This message may appear again if the missing logfiles are not restored.\r\n
0x000001c3 | %1 (%2) %3Unable to write to section 4 while flushing logfile %4. Error %5.\r\n
0x000001c4 | %1 (%2) %3Database %4 requires logfiles %5-%6 in order to recover successfully. Recovery could only locate logfiles starting at %7.\r\n
0x000001c5 | %1 (%2) %3Database %4 requires logfiles %5-%6 (%8 - %9) in order to recover successfully. Recovery could only locate logfiles up to %7 (%10).\r\n
0x000001c6 | %1 (%2) %3Database recovery/restore failed with unexpected error %4.\r\n
0x000001c7 | %1 (%2) %3Error %5 occurred while opening logfile %4.\r\n
0x000001c8 | %1 (%2) %3The primary header page of file %4 was damaged. The shadow header page (%5 bytes) was used instead.\r\n
0x000001c9 | %1 (%2) %3The log signature of the existing logfile %4 doesn't match the logfiles from the backup set. Logfile replay cannot succeed unless all signatures match.\r\n
0x000001ca | %1 (%2) %3The logfiles %4 and %5 are not in a valid sequence. Logfile replay cannot succeed if there are gaps in the sequence of available logfiles.\r\n
0x000001cb | %1 (%2) %3The file %4 is missing and could not be backed-up.\r\n
0x000001cc | %1 (%2) %3A torn-write was detected while restoring from backup in logfile %4 of the backup set. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001cd | %1 (%2) %3A torn-write was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. This logfile has been damaged and is unusable.\r\n
0x000001ce | %1 (%2) %3A torn-write was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. The logfile damage will be repaired and recovery will continue to proceed.\r\n
0x000001cf | %1 (%2) %3Corruption was detected while restoring from backup logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d0 | %1 (%2) %3Corruption was detected during hard recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d1 | %1 (%2) %3Corruption was detected during soft recovery in logfile %4. The failing checksum record is located at position %5. Data not matching the log-file fill pattern first appeared in sector %6. This logfile has been damaged and is unusable.\r\n
0x000001d2 | %1 (%2) %3An invalid checksum record in logfile %4 was patched using its shadow sector copy.\r\n
0x000001d3 | %1 (%2) %3Database %6: Index %4 of table %5 is corrupted (%7).\r\n
0x000001d4 | %1 (%2) %3Unable to write to section 5 while flushing logfile %4. Error %5.\r\n
0x000001d6 | %1 (%2) %3Database %4 is partially attached. Attachment stage: %5. Error: %6.\r\n
0x000001d7 | %1 (%2) %3Unable to rollback operation #%4 on database %5. Error: %6. All future database updates will be rejected.\r\n
0x000001d8 | %1 (%2) %3The shadow header page of file %4 was damaged. The primary header page (%5 bytes) was used instead.\r\n
0x000001d9 | %1 (%2) %3Database %4 was partially detached.  Error %5 encountered updating database headers.\r\n
0x000001da | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %10) for %6 bytes failed verification due to a page checksum mismatch.  The stored checksum was %8 and the computed checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.  This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001db | %1 (%2) %3The database page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the stored page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dc | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification because it contains no page data.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001dd | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a range checksum mismatch.  The expected checksum was %8 and the actual checksum was %9. The read operation will fail with error %7.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x000001de | %1 (%2) %3The streaming page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore the database from a previous backup.\r\n
0x000001df | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page checksum mismatch.  The expected checksum was %8 and the actual checksum was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e0 | %1 (%2) %3The patch page read from the file "%4" at offset %5 for %6 bytes failed verification due to a page number mismatch.  The expected page number was %8 and the actual page number was %9.  The read operation will fail with error %7.  If this condition persists then please restore using an earlier backup set.\r\n
0x000001e1 | %1 (%2) %3An attempt to read from the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The read operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e2 | %1 (%2) %3An attempt to write to the file "%4" at offset %5 for %6 bytes failed after %10 seconds with system error %8: "%9".  The write operation will fail with error %7.  If this error persists then the file may be damaged and may need to be restored from a previous backup.\r\n
0x000001e3 | %1 (%2) %3An attempt to create the folder "%4" failed with system error %6: "%7".  The create folder operation will fail with error %5.\r\n
0x000001e4 | %1 (%2) %3An attempt to remove the folder "%4" failed with system error %6: "%7".  The remove folder operation will fail with error %5.\r\n
0x000001e5 | %1 (%2) %3An attempt to delete the file "%4" failed with system error %6: "%7".  The delete file operation will fail with error %5.\r\n
0x000001e6 | %1 (%2) %3An attempt to move the file "%4" to "%5" failed with system error %7: "%8".  The move file operation will fail with error %6.\r\n
0x000001e7 | %1 (%2) %3An attempt to copy the file "%4" to "%5" failed with system error %7: "%8".  The copy file operation will fail with error %6.\r\n
0x000001e8 | %1 (%2) %3An attempt to create the file "%4" failed with system error %6: "%7".  The create file operation will fail with error %5.\r\n
0x000001e9 | %1 (%2) %3An attempt to open the file "%4" for read only access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001ea | %1 (%2) %3An attempt to open the file "%4" for read / write access failed with system error %6: "%7".  The open file operation will fail with error %5.\r\n
0x000001eb | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001ec | %1 (%2) %3The logfile sequence in "%4" has been halted due to a fatal error.  No further updates are possible for the databases that use this logfile sequence.  Please correct the problem and restart or restore from backup.\r\n
0x000001ed | %1 (%2) %3A read operation on the file "%4" at offset %5 for %6 bytes failed %7 times over an interval of %8 seconds before finally succeeding.  More specific information on these failures was reported previously.  Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.\r\n
0x000001ee | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which is no longer present. The database was not brought to a Clean Shutdown state before it was removed (or possibly moved or renamed). The database engine will not permit recovery to complete for this instance until the missing database is re-instated. If the database is truly no longer available and no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001ef | %1 (%2) %3Database recovery on '%5' failed with error %4. The database is not in the state expected at the first reference of this database in the log files. It is likely that a file copy of this database was restored, but not all log files since the file copy was made are currently available. Procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x000001f0 | %1 (%2) %3Database %4 requires logfile %5 created at %6 in order to recover successfully. Recovery found the logfile created at %7.\r\n
0x000001f1 | %1 (%2) %3From information provided by the headers of %4, the file is not a database file. The headers of the file may be corrupted.\r\n
0x000001f2 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfiles %5 to %6 have been deleted so that recovery can complete.\r\n
0x000001f3 | %1 (%2) %3There is a gap in log sequence numbers, last used log file has generation %4. Logfile %5 (generation %6) have been deleted so that recovery can complete.\r\n
0x000001f4 | %1 (%2) %3The database engine lost one page of bad data. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f5 | %1 (%2) %3The database engine repaired one page link.\r\n
0x000001f6 | %1 (%2) %3The database engine lost one or more bad columns of data in one record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f7 | %1 (%2) %3The database engine lost one bad data record. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f8 | %1 (%2) %3The database engine lost one table called %4. It is highly recommended that an application-level integrity check of the database be run to ensure application-level data integrity.\r\n
0x000001f9 | %1 (%2) %3An attempt to open the compressed file "%4" for read / write access failed because it could not be converted to a normal file.  The open file operation will fail with error %5.  To prevent this error in the future you can manually decompress the file and change the compression state of the containing folder to uncompressed.  Writing to this file when it is compressed is not supported.\r\n
0x000001fa | %1 (%2) %3An attempt to determine the amount of free/total space for the volume "%4" containing "%5" failed with system error %7: "%8".  The operation will fail with error %6.\r\n
0x000001fb | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fc | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fd | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000001fe | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes succeeded, but took an abnormally long time (%7 seconds) to be serviced by the OS. In addition, %8 other I/O requests to this file have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %9 seconds ago. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000200 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed).\r\n\r\n
0x00000201 | %1 (%2) %3The system has serviced a %4 task but it took an abnormally long time (%5 seconds to be dispatched, %6 seconds to be executed). In addition, %7 other %4 tasks have also taken an abnormally long time to be serviced since the last message regarding this problem was posted %8 seconds ago. \r\n\r\n
0x00000202 | %1 (%2) %3Log sequence numbers for this instance have almost been completely consumed. The current log generation is %4 which is approaching the maximum log generation of %5, there are %6 log generations left to be used. To begin renumbering from generation 1, the instance must be shutdown cleanly and all log files must be deleted. Backups will be invalidated.\r\n
0x00000203 | %1 (%2) %3Database %4: Page %5 failed verification due to a flush-order dependency mismatch.  This page should have flushed before page %6, but the latter page has instead flushed first. Recovery/restore will fail with error %7. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on one or both of these pages sometime in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000204 | %1 (%2) %3Database %4: Page %5 failed verification due to a timestamp mismatch at log position %10 (currently replaying log position %12).  The 'before' timestamp persisted to the log record was %6 but the actual timestamp on the page was %7.  The 'after' update timestamp %9 that would have updated the on-page timestamp.  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page some time in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %11\r\n%n%tTotal number of pages affected: %13\r\n
0x00000205 | %1 (%2) %3Database recovery failed with error %4 because it encountered references to a database, '%5', which does not match the current set of logs. The database engine will not permit recovery to complete for this instance until the mismatching database is re-instated. If the database is truly no longer available or no longer required, procedures for recovering from this error are available in the Microsoft Knowledge Base or by following the "more information" link at the bottom of this message.\r\n
0x00000206 | %1 (%2) %3The log file %4 is missing (error %5) and cannot be used. If this log file is required for recovery, a good copy of the log file will be needed for recovery to complete successfully.\r\n
0x00000207 | %1 (%2) %3The range of log files %4 to %5 is missing (error %6) and cannot be used. If these log files are required for recovery, a good copy of these log files will be needed for recovery to complete successfully.\r\n
0x00000208 | %1 (%2) %3Log truncation failed because not all log files required for recovery were successfully copied.\r\n
0x00000209 | %1 (%2) %3Unable to schedule a log write on log file %4. Error %5.\r\n
0x0000020a | %1 (%2) %3An attempt to open the device with name "%4" containing "%5" failed with system error %7: "%8". The operation will fail with error %6.\r\n
0x0000020b | %1 (%2) %3Database %4 requires log files %5-%6 in order to recover all committed data.  Recovery could only locate up to log file: %7, and could not locate log generation %8.  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020c | %1 (%2) %3Database %4 has lost %5 committed log files (%6-%7). However, lost log resilience has allowed ESE to recover this database to a consistent state, but with data loss.  Recovery could only locate log files up to %8.\r\n%nDetails:\r\n%n%tLog directory: %9\r\n
0x0000020d | %1 (%2) %3The log file %4 is damaged, invalid, or inaccessible (error %5) and cannot be used. If the log file cannot be found, the database(s) can still be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %6\r\n
0x0000020e | %1 (%2) %3The log file %5 (generation %6) has damaged or invalid log (%7), ESE has removed the portion of log corrupted since these committed logs are specified as unneeded, so that ESE can recover (through generation %4) any attached databases to a consistent state, but with data loss.\r\n
0x0000020f | %1 (%2) %3ESE has removed %4 committed log files (%5-%6) to maintain an in order log stream.  However lost log resilience has allowed ESE to recover to a consistent state, but with data loss.  Recovery could only recover through log files up to %7.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000210 | %1 (%2) %3Recovery could only locate up to log file %4 (generation %5) before detecting an out of sequence logs, and could not locate log file %6 (generation %7).  If the log file cannot be found, the database(s) can be recovered manually, but will result in losing committed data.\r\n%nDetails:\r\n%n%tLog directory: %8\r\n
0x00000211 | %1 (%2) %3The log range read from the file "%4" at offset %5 for %6 bytes failed verification due to a corrupted checksum log record. The read operation will fail with error %7.  If this condition persists, restore the logfile from a previous backup.\r\n
0x00000212 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nContext: %12.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000213 | %1 (%2) %3The database engine attempted a clean write operation on page %4 of database %5. This action was performed in an attempt to correct a previous problem reading from the page.\r\n
0x00000214 | %1 (%2) %3A request to read from the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000215 | %1 (%2) %3A request to write to the file "%4" at offset %5 for %6 bytes has not completed for %7 second(s). This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000216 | %1 (%2) %3A patch request for file "%4" at page number "%5" has failed to be issued with error %6. If this condition persists then please restore using an earlier backup set.\r\n
0x00000217 | %1 (%2) %3An attempt to determine the minimum I/O block size for the volume containing "%4" failed.  The default sector-size of 512 bytes will be used.\r\n
0x00000218 | %1 (%2) %3An attempt to create temporary database %4 failed with error %5.\r\n
0x00000219 | %1 (%2) %3A request for a node on an empty page (Pgno: %7, Flags: %9) has been made (error %4) for a B-Tree (ObjectId: %5, PgnoRoot: %6) of database %8. This is typically due to a lost I/O from \r\nstorage hardware. Please check with your hardware vendor for latest firmware revisions, make changes to your controller's caching parameters, use crash consistent hardware with Forced\r\nUnit Access support, and/or replace faulty hardware.\r\n
0x0000021a | %1 (%2) %3Database %4: Page %5 in a B-Tree (ObjectId: %12) failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.%n\r\nAdditional information:%n\r\n%tSource: %11%n\r\n
0x0000021b | %1 (%2) %3Database %4: Page %5 in a B-Tree (ObjectId: %12) failed verification due to a timestamp mismatch at log position %10.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the passive node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.%n\r\nAdditional information:%n\r\n%tSource: %11%n\r\n
0x0000021c | %1 (%2) %3Database %4: Page %5 in a B-Tree (ObjectId: %11) logical data checksum %6 failed to match logged scan check %7 checksum (seed %8) at log position %9.%n\r\nAdditional information:%n\r\n%tSource: %10%n\r\n
0x0000021d | %1 (%2) %3Database %4: Page %5 appears to be uninitialized at log position %8 on the current node.  The remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7). This indicates the passive node lost a flush. This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the passive node. Please contact your hardware vendor for further assistance diagnosing the problem.%n\r\nAdditional information:%n\r\n%tSource: %9%n\r\n
0x0000021e | %1 (%2) %3Database %4: Page %5 (ObjectId: %6) has a logical corruption of type '%7'.\r\n%nDetails: %8\r\n
0x0000021f | %1 (%2) %3Previous log's accumulated segment checksum mismatch in logfile %4, Expected: %5, Actual: %6.\r\n
0x00000220 | %1 (%2) %3The database page read from the file "%4" at offset %5 (database page %8) for %6 bytes failed verification due to a persisted lost flush detection timestamp mismatch. The read operation will fail with error %7.\r\n%nThe flush state on database page %8 was %9 while the flush state on flush map page %10 was %11.\r\n%nContext: %12.\r\n%nIf this condition persists, restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000221 | %1 (%2) %3Database %4: Page %5 in a B-Tree (ObjectId: %12) appears to be uninitialized at log position %10 on the remote node.  The remote ("before") timestamp persisted to the log record was %6 but the actual timestamp on the page was %7 (note: DbtimeCurrent = %9). This indicates the active node lost a flush (error %8). This problem is likely due to faulty hardware "losing" one or more flushes on this page sometime in the past on the active node. Please contact your hardware vendor for further assistance diagnosing the problem.%n\r\nAdditional information:%n\r\n%tSource: %11%n\r\n
0x00000222 | %1 (%2) %3The log generation (%4) is too low (%5) to be supported or replayed by this database engine (min supported %6).\r\n
0x00000223 | %1 (%2) %3The log generation (%4) is too high (%5) to be supported or replayed by this database engine (max supported %6).\r\n
0x00000224 | %1 (%2) %3The log generation's [%4] version %5 is higher than the maximum version configured by the application %6. Current engine format version parameter setting: %7\r\n
0x00000225 | %1 (%2) %3Database %4 has a page (pgno %5) with too few lines in a B-Tree (ObjectId: %6, PgnoRoot: %7), operation attempted on line %8, actual number of lines on page %9.\r\n
0x00000226 | %1 (%2) %3Database %4: A compressed LV chunk failed verification during decompression due to a checksum mismatch. This indicates a logical corruption in the compress/decompress pipeline.\r\npgnoFDP = %5. Key = %6.\r\n
0x00000227 | %1 (%2) %3An attempt to flush to the file/disk buffers of "%4" failed after %5 seconds with system error %6: "%7".  The flush operation will fail with error %8.  If this error persists then the file system may be damaged and may need to be restored from a previous backup.\r\n
0x00000228 | %1 (%2) %3The log file at "%4" is corrupt with reason '%5'. Last valid segment was %6, current segment is %7. The expected checksum was %8 and the actual checksum was %9. The read completed with error-code %10.  If this condition persists then please restore the logfile from a previous backup.\r\n
0x00000229 | %1 (%2) %3Failed looking up restore-map entry for database %4 with unexpected error %5.\r\n
0x0000022a | %1 (%2) %3The log segment read from the file "%4" at offset %6 (segment number %5) failed verification. Bit %7 was corrupted and has been corrected.  This problem is likely due to faulty hardware and may continue. Transient failures such as these can be a precursor to a catastrophic failure in the storage subsystem containing this file.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000022b | %1 (%2) %3Database %4: Page %5 failed verification due not containing any data at log position %6 (currently replaying log position %7).  Recovery/restore will fail with error %8.  If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware "losing" one or more flushes on this page some time in the past. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %9\r\n%n%tTotal number of pages affected: %10\r\n
0x0000022c | %1 (%2) %3Database %4: Data in line %5 on pgno %6 in a B-Tree (ObjectId: %7, PgnoRoot: %8) failed to decompress.\r\n
0x0000022d | %1 (%2) %3Database %4: Page %5 was shown to be beyond the end of file at log position %8, while the remote ("before") timestamp persisted to the log record was %6 (note: DbtimeCurrent = %7).%n\r\nAdditional information:%n\r\n%tSource: %9%n\r\n
0x0000022e | %1 (%2) %3There is a gap in sequence number following logfile generation %4. Highest logfile generation present is %5.\r\n
0x0000022f | %1 (%2) %3Database %4: A timestamp inconsistency has been detected while scanning page %5 (ObjectId: %10) on the active node at log position %6.  The timestamp on the page is too advanced.\r\nAdditional information:%n\r\n%tTimestamp persisted to the page: %7%n\r\n%tGlobal timestamp of the database: %8%n\r\n%tSource: %9%n\r\n
0x00000230 | %1 (%2) %3Database %4: A timestamp inconsistency has been detected while verifying page %5 in a B-Tree (ObjectId: %12) at log position %10.  The timestamp on the page is too advanced.\r\nAdditional information:%n\r\n%tTimestamp persisted to the page: %7%n\r\n%tGlobal timestamp of the database: %9%n\r\n%tTimestamp persisted to the log record: %6%n\r\n%tError code: %8%n\r\n%tSource: %11%n\r\n
0x00000231 | %1 (%2) %3Corsica device failed to initialize with status code '%4' with reason '%5'.\r\n
0x00000232 | %1 (%2) %3A request to corsica device for '%7' failed with status code '%4', engine code '%5' with reason '%6'.\r\n
0x00000233 | %1 (%2) %3Database '%4' encountered error %5 while releasing space to the database root (ObjectId %6). A total of %7 page(s) (%8 - %9) will be leaked. The leaked space may be reclaimed by running offline defragmentation on the database.%n\r\nTag: %10%n\r\n
0x00000234 | %1 (%2) %3Database '%4' encountered error %5 while releasing space to ObjectId %6. A total of %7 page(s) (%8 - %9) will be leaked. The leaked space may be reclaimed by either running offline defragmentation on the database or deleting and re-creating the object.%n\r\nTag: %10%n\r\n
0x00000235 | %1 (%2) %3Database %4: Page %5 failed verification due to being reverted to a new page using revert snapshot, but the log record at log position %6 expected the page to not be a new page (currently replaying log position %7).  Recovery/restore will fail with error %8.  This problem is likely due to a bad revert operation.\r\n%nAdditional information:\r\n%n%tWithin initial required range: %9\r\n%n%tTotal number of pages affected: %10\r\n
0x00000258 | %1 (%2) %3The database engine encountered an unexpected duplicate key on the table %4. One record has been dropped.\r\n
0x00000259 | %1 (%2) %3The database engine could not find the entrypoint %4 in the file %5.\r\n
0x0000025a | %1 (%2) %3Database '%4': Background clean-up skipped pages. The database may benefit from widening the online maintenance window during off-peak hours. If this message persists, offline defragmentation may be run to remove all skipped pages from the database. Discarded RCE id:%5, trxBegin0:%6, trxCommit0: %7, last trxNewest: %8, current trxNewest: %9.\r\n
0x0000025b | %1 (%2) %3Database '%4': The database engine lost unused pages %5-%6 while attempting space reclamation on a B-Tree (ObjectId %7). The space may not be reclaimed again until offline defragmentation is performed.\r\n
0x0000025c | %1 (%2) %3Locale ID %4 (%5 %6) is either invalid, not installed on this machine or could not be validated with system error %7: "%8". The operation will fail with error %9.\r\n
0x0000025d | %1 (%2) %3Column '%4' of Table '%5' was converted to a Tagged column.\r\n
0x0000025e | %1 (%2) %3Column '%4' of Table '%5' was converted to a non-Tagged column.\r\n
0x0000025f | %1 (%2) %3Column '%4' of Table '%5' was converted from Binary to LongBinary.\r\n
0x00000260 | %1 (%2) %3Column '%4' of Table '%5' was converted from Text to LongText.\r\n
0x00000261 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade from %5.%6.%7 SP%8 to %9.%10.%11 SP%12. This message is informational and does not indicate a problem in the database.\r\n
0x00000262 | %1 (%2) %3The database engine is initiating index cleanup of database '%4' as a result of a Windows version upgrade to %5.%6.%7 SP%8. This message is informational and does not indicate a problem in the database.\r\n
0x00000263 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' will be rebuilt as a precautionary measure after the Windows version upgrade of this system. This message is informational and does not indicate a problem in the database.\r\n
0x00000264 | %1 (%2) %3The database engine has successfully completed index cleanup on database '%4'.\r\n
0x00000265 | %1 (%2) %3Database '%4': The primary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000266 | %1 (%2) %3Database '%4': The secondary index '%5' of table '%6' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.\r\n
0x00000267 | %1 (%2) %3The database engine is converting the database '%4' from format %5 to format %6.\r\n
0x00000268 | %1 (%2) %3The database engine has successfully converted the database '%4' from format %5 to format %6.\r\n
0x00000269 | %1 (%2) %3Attempted to use database '%4', but conversion did not complete successfully on this database. Please restore from backup and re-run database conversion.\r\n
0x0000026a | %1 (%2) %3Database '%4': The database engine has built an in-memory cache of %5 space tree nodes on a B-Tree (ObjectId: %6, PgnoRoot: %7) to optimize space requests for that B-Tree. The space cache was built in %8 milliseconds. This message is informational and does not indicate a problem in the database.\r\n
0x0000026b | %1 (%2) %3Attempted to attach database '%4' but it is a database restored from a backup set on which hard recovery was not started or did not complete successfully.\r\n
0x0000026c | %1 (%2) %3Unable to convert record format for record %4:%5:%6.\r\n
0x0000026d | %1 (%2) %3Database '%4': Out of B-Tree IDs (ObjectIDs). Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026e | %1 (%2) %3Database '%4': Available B-Tree IDs (ObjectIDs) have almost been completely consumed. Freed/unused B-Tree IDs may be reclaimed by performing an offline defragmentation of the database.\r\n
0x0000026f | %1 (%2) %3The version store for this instance (%4) has reached its maximum size of %5Mb. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %6\r\n%n%tSession-context: %7\r\n%n%tSession-context ThreadId: %8\r\n%n%tCleanup: %9\r\n%n%tSession-trace:\r\n%n%10\r\n
0x00000270 | %1 (%2) %3The version store for this instance (%4) cannot grow because it is receiving Out-Of-Memory errors from the OS. It is likely that a long-running transaction is preventing cleanup of the version store and causing it to build up in size. Updates will be rejected until the long-running transaction has been completely committed or rolled back.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum version store size for this instance: %6Mb\r\n%nGlobal memory pre-reserved for all version stores: %7Mb\r\n%nPossible long-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000271 | %1 (%2) %3The database engine does not support the LCMapString() flags %4.\r\n
0x00000272 | %1 (%2) %3The database engine updated %4 index entries in database %5 because of a change in the NLS version. This message is informational and does not indicate a problem in the database.\r\n
0x00000273 | %1 (%2) %3The database engine was unable to updated index entries in database %5 because the database is read-only.\r\n
0x00000274 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %17 milliseconds (waiting %18 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %19 pages). It is likely that these non-visible\r\nnodes are nodes which have been marked for deletion but which are\r\nyet to be purged. The database may benefit from widening the online\r\nmaintenance window during off-peak hours in order to purge such nodes\r\nand reclaim their space. If this message persists, offline\r\ndefragmentation may be run to remove all nodes which have been marked\r\nfor deletion but are yet to be purged from the database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tTCE: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %16\r\n%n%tDbtime Distrib: %20\r\n
0x00000275 | %1 (%2) %3Database '%4': While attempting to move to the next or\r\nprevious node in a B-Tree, the database engine took %21 milliseconds (waiting %22 milliseconds on faults) to skip over %7\r\nnon-visible nodes in %8 pages (faulting in %23 pages). In addition, since this message was\r\nlast reported %16 hours ago, %17 other incidents of excessive\r\nnon-visible nodes were encountered (a total of %18 nodes in %19 pages\r\nwere skipped) during navigation in this B-Tree. It is likely that\r\nthese non-visible nodes are nodes which have been marked for deletion\r\nbut which are yet to be purged. The database may benefit from\r\nwidening the online maintenance window during off-peak hours in order\r\nto purge such nodes and reclaim their space. If this message\r\npersists, offline defragmentation may be run to remove all nodes\r\nwhich have been marked for deletion but have yet to be purged from\r\nthe database.\r\n%n%tName: %5\r\n%n%tOwning Table: %6\r\n%n%tObjectId: %9\r\n%n%tPgnoRoot: %10\r\n%n%tTCE: %11\r\n%n%tUnversioned Deletes: %12\r\n%n%tUncommitted Deletes: %13\r\n%n%tCommitted Deletes: %14\r\n%n%tNon-Visible Inserts: %15\r\n%n%tFiltered: %20\r\n%n%tDbtime Distrib: %24\r\n
0x00000276 | %1 (%2) %3The version store for this instance (%4) has a long-running transaction that exceeds the maximum transaction size.\r\n%nCurrent version store size for this instance: %5Mb\r\n%nMaximum transaction size for this instance: %6Mb\r\n%nMaximum version store size for this instance: %7Mb\r\n%nLong-running transaction:\r\n%n%tSessionId: %8\r\n%n%tSession-context: %9\r\n%n%tSession-context ThreadId: %10\r\n%n%tCleanup: %11\r\n%n%tSession-trace:\r\n%n%12\r\n
0x00000277 | %1 (%2) %3The file system reports that the database file at %4 has a sector size of %5 which is greater than the page size of %6.  This may result in higher torn write corruption incidence and/or in database corruption via lost flushes.\r\n
0x00000278 | %1 (%2) %3The file system reports that the log file at %4 has a sector size of %5 which is unsupported, using a sector size of 4096 instead.  This may result in transaction durability being lost.\r\n
0x00000279 | %1 (%2) %3Recovery had to pause (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027a | %1 (%2) %3Recovery had to pause for a long time (%4 ms) to allow an older read-only transaction to complete. If this condition persists, it can result in stale copies.\r\n
0x0000027b | %1 (%2) %3Failed to attach flush map file "%4" with error %5.\r\n
0x0000027c | %1 (%2) %3Flush map file "%4" will be deleted. Reason: %5.\r\n
0x0000027d | %1 (%2) %3New flush map file "%4" will be created to enable persisted lost flush detection.\r\n
0x0000027e | %1 (%2) %3Error %4 validating page %5 on flush map file "%6". The flush type of the database pages will be set to 'unknown' state.\r\n
0x0000027f | %1 (%2) %3Inconsistent timestamp detected on page %4 of flush map file "%5" (empty if flush map persistence in disabled). The maximum timestamp on the flush map is %6, but database page %7 has a timestamp of %8. If flush map persistence is enabled, this problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000280 | %1 (%2) %3Error %4 validating header page on flush map file "%5". The flush map file will be invalidated.\r\n%nAdditional information: %6\r\n
0x00000281 | %1 (%2) %3The log format feature version %5 could not be used due to the current log format %6, controlled by the parameter %4.\r\n
0x00000282 | %1 (%2) %3The database format feature version %5 could not be used due to the current database format %6, controlled by the parameter %4.\r\n
0x00000283 | %1 (%2) %3 Out of date NLS sort version detected on the database '%4' for Locale '%5', index sort version: (SortId=%6, Version=%7), current sort version: (SortId=%8, Version=%9).\r\n
0x00000284 | %1 (%2) %3A session has an outstanding transaction causing the checkpoint depth (of %4 logs) to exceed a quarter of the JET_paramCheckpointTooDeep setting.%n\r\n%n\r\nDetails:%n\r\nTransaction Context Info: %5%n\r\nTransaction Start Times: %6%n\r\n
0x00000285 | %1 (%2) %3Attempted to use trailer page to patch header in database '%4' but it was found to be corrupt. This may indicate an incomplete backup and a missing trailer page.\r\n
0x00000286 | %1 (%2) %3The revert snapshot file at "%4" is corrupt with reason '%5' at offset %6, segment %7. The expected checksum was %8 and the actual checksum was %9.\r\n
0x00000287 | %1 (%2) %3The Extent Page Count Cache is enabled in database %4 for reason %5.\r\n
0x00000288 | %1 (%2) %3The Extent Page Count Cache is disabled in database %4 for reason %5.\r\n
0x00000289 | %1 (%2) %3The Extent Page Count Cache table was created in database %4 for reason %5.\r\n
0x0000028a | %1 (%2) %3The Extent Page Count Cache table was deleted in database %4 for reason %5.\r\n
0x0000028b | %1 (%2) %3Newly created tables will be tracked immediately by the Extent Page Count Cache.\r\n
0x0000028c | %1 (%2) %3Extra validation of the Extent Page Count Cache table is enabled.  This is resource intensive and will adversely affect performance.\r\n
0x0000028d | %1 (%2) %3An operation in the Extent Page Count Cache table failed.%n\r\nDatabase: %4%n\r\nOperation: %5%n\r\nNote: %6%n\r\nErr: %7%n\r\nObjidFDP: %8%n\r\nPgnoFDP: %9%n\r\n
0x0000028e | %1 (%2) %3Preparing a row in the Extent Page Count Cache table failed.  The cached value may be incorrect.%n\r\nDatabase: %4%n\r\nObjid: %5%n\r\nPgnoFDP: %6%n\r\nErr: %7%n\r\n
0x0000028f | %1 (%2) %3Extra validation of the Extent Page Count Cache table failed.%n\r\nDatabase: %4%n\r\nObjid: %5%n\r\nPgnoFDP: %6%n\r\nCounted CpgOE: %7%n\r\nCounted CpgAE: %8%n\r\nCached CpgOE: %9%n\r\nCached CpgAE: %10%n\r\n
0x000002bc | %1 (%2) %3Online defragmentation is beginning a full pass on database '%4'.\r\n
0x000002bd | %1 (%2) %3Online defragmentation has completed a full pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002be | %1 (%2) %3Online defragmentation is resuming its pass on database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002bf | %1 (%2) %3Online defragmentation has completed the resumed pass on database '%4', freeing %5 pages. This pass started on %6 and ran for a total of %7 seconds, requiring %8 invocations over %9 days. Since the database was created it has been fully defragmented %10 times.\r\n
0x000002c0 | %1 (%2) %3Online defragmentation of database '%4' was interrupted and terminated. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c1 | %1 (%2) %3Online defragmentation of database '%4' terminated prematurely after encountering unexpected error %5. The next time online defragmentation is started on this database, it will resume from the point of interruption.\r\n
0x000002c2 | %1 (%2) %3Online zeroing of database %4 started\r\n
0x000002c3 | %1 (%2) %3Online zeroing of database %4 finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 blank pages%n\r\n%9 pages unchanged since last zero%n\r\n%10 unused pages zeroed%n\r\n%11 used pages seen%n\r\n%12 deleted records zeroed%n\r\n%13 unreferenced data chunks zeroed\r\n
0x000002c4 | %1 (%2) %3Online defragmentation is beginning a full pass on streaming file '%4'.\r\n
0x000002c5 | %1 (%2) %3Online defragmentation has completed a full pass on streaming file '%4'.\r\n
0x000002c6 | %1 (%2) %3Online defragmentation of streaming file '%4' has shrunk the file by %5 bytes.\r\n
0x000002c7 | %1 (%2) %3Online defragmentation of streaming file '%4' terminated prematurely after encountering unexpected error %5.\r\n
0x000002c8 | %1 (%2) %3Online zeroing of streaming file '%4' started.\r\n
0x000002c9 | %1 (%2) %3Online zeroing of streaming file '%4' finished after %5 seconds with err %6%n\r\n%7 pages%n\r\n%8 unused pages zeroed%n\r\n
0x000002ca | %1 (%2) %3Online defragmentation has successfully been stopped on streaming file '%4'.\r\n
0x000002cb | %1 (%2) %3Online defragmentation has been paused one or more times in the last 60 minutes for the following databases: '%4'.  The ESE Database Cache is not large enough to simultaneously run online defragmentation against the listed databases.  Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002cc | %1 (%2) %3Online defragmentation has resumed one or more times in the last 60 minutes for the following databases: "%4'.\r\n
0x000002cd | %1 (%2) %3Online Maintenance is starting Database Checksumming background task for database '%4'.\r\n
0x000002ce | %1 (%2) %3Online Maintenance is starting Database Page Zeroing background task for database '%4'.\r\n
0x000002cf | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d0 | %1 (%2) %3Online Maintenance is resuming Database Zeroing background task for database '%4'. This pass started on %5 and has been running for %6 days.\r\n
0x000002d1 | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages\r\n
0x000002d2 | %1 (%2) %3Online Maintenance Database Zeroing background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds, requiring %7 invocations over %8 days. Operation summary:\r\n%n\r\n%9 pages seen%n\r\n%10 bad checksums%n\r\n%11 uninitialized pages%n\r\n%12 pages unchanged since last zero%n\r\n%13 unused pages zeroed%n\r\n%14 used pages seen%n\r\n%15 deleted records zeroed%n\r\n%16 unreferenced data chunks zeroed\r\n
0x000002d3 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d4 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' encountered error %5 after %6 seconds.\r\n
0x000002d5 | %1 (%2) %3Online Maintenance Database Checksumming background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d6 | %1 (%2) %3Online Maintenance Database Zeroing background task for database '%4' was interrupted and terminated. The next time Online Maintenance Database Checksumming is started on this database, it will resume from the point of interruption.\r\n
0x000002d7 | %1 (%2) %3The database page read from the file '%4' at offset %5 (database page %6) failed verification due to a page checksum mismatch. If this condition persists then please restore the database from a previous backup. This problem is likely due to faulty hardware. Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x000002d8 | %1 (%2) %3\r\nOnline defragmentation has defragmented index '%6' of table '%5' in database '%4'. This pass started on %7.%n\r\n%8 pages visited%n\r\n%9 pages freed%n\r\n%10 partial merges%n\r\n%11 pages moved\r\n
0x000002d9 | %1 (%2) %3Online maintenance database zeroing has been paused one or more times in the last 60 minutes for the following databases: '%4'. The ESE database cache is not large enough to simultaneously run online page zeroing against the listed databases. Action: Stagger the online maintenance time windows for the listed databases or increase the amount of physical RAM in the server.\r\n
0x000002da | %1 (%2) %3Online maintenance database zeroing has resumed one or more times in the last 60 minutes for the following databases: '%4'.\r\n
0x000002dc | %1 (%2) %3Online Maintenance Database Checksumming background task has completed for database '%4'. This pass started on %5 and ran for a total of %6 seconds (over %7 days) on %8 pages.\r\n%n\r\nLast Runtime Scan Stats: %9\r\n
0x000002dd | %1 (%2) %3Online Maintenance Database Checksumming background task is not finishing on time for database '%4'. This pass started on %5 and has been running for %6 seconds (over %7 days) so far.\r\n
0x000002de | %1 (%2) %3Database Maintenance background task for database '%4' failed to start with error %5.  \r\n
0x000002df | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds (%7 days).  This database maintenance task exceeded the %8 day maintenance completion threshold.  One or more of the following actions should be taken:  increase the IO performance/throughput of the volume hosting the database, reduce the database size, and/or reduce non-database maintenance IO.\r\n%n\r\n%9 pages seen%n\r\nAverage free space on Record pages: %10 (%11 pages scanned)%n\r\nAverage free space on LV pages: %12 (%13 pages scanned)%n\r\nLast Runtime Scan Stats: %10%n\r\n
0x000002e0 | %1 (%2) %3Database Maintenance is starting for database '%4'.\r\n
0x000002e1 | %1 (%2) %3Database Maintenance has completed a full pass on database '%4'. This pass started on %5 and ran for a total of %6 seconds.\r\n%n\r\n%7 pages seen%n\r\nAverage free space on Record pages: %9 (%10 pages scanned)%n\r\nAverage free space on LV pages: %11 (%12 pages scanned)%n\r\nLast Runtime Scan Stats: %8%n\r\n
0x000002e2 | %1 (%2) %3Database Maintenance is resuming for database '%4', starting from page %5. This pass started on %6 and has been running for %7 days.\r\n
0x000002e3 | %1 (%2) %3The NTFS file attributes size for database '%4' is %5 bytes, which exceeds the threshold of %6 bytes. The database file must be reseeded or restored from a copy or backup to prevent the database file from being unable to grow because of  a file system limitation. \r\n
0x000002e4 | %1 (%2) %3The periodic database file trimming operation started.\r\n
0x000002e5 | %1 (%2) %3The periodic database file trimming operation finished successfully and trimmed the database file by %4 pages.\r\n
0x000002e6 | %1 (%2) %3The periodic database file trimming operation was not able to trim the database file because there is not enough internal free space available.\r\n
0x000002e7 | %1 (%2) %3The periodic database file trimming operation was not able to trim the database file. Result %4.\r\n
0x000002e8 | %1 (%2) %3Database Maintenance is running on database '%4'. This pass started on %5 and has been running for %6 hours.\r\n%n\r\n%7 pages seen%n\r\n
0x000002e9 | %1 (%2) %3Online Maintenance Database Checksumming background task is aborted for database '%4' at page %5, due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last properly completed checksumming task was on %6.%n\r\n%n\r\nLast Runtime Scan Stats: %7%n\r\n
0x000002ea | %1 (%2) %3Online Maintenance Database Checksumming background task finished an interrupted and incomplete scan for database '%4'. Typical interruptions are due to client request (typically because of critical redo activity must be done quickly).%n\r\nThe last fully completed checksumming scan was on %5.\r\n
0x000002eb | %1 (%2) %3Online Maintenance is resuming Database Checksumming background task for database '%4', and in doing so has skipped %5 pages (%6%%).  prev stop: %7, this start: %8.%n\r\n
0x000002ec | %1 (%2) %3The database file shrinkage operation completed successfully on database '%4'.%n\r\nInitial file size: %7 bytes (%8 page(s)).%n\r\nFinal file size: %9 bytes (%10 page(s)).%n\r\nInitial owned space: %11 bytes (%12 page(s)).%n\r\nFinal owned space: %13 bytes (%14 page(s)).%n\r\nData moved: %15 bytes (%16 page(s)).%n\r\nPages shelved: %24 page(s).%n\r\nPages unleaked: %25 page(s).%n\r\nReturn code: %17%n\r\nStop reason: %18%n\r\nTotal time: %5 minute(s) and %6 second(s).%n\r\nPct. time in extent maintenance: %19%%%n\r\nPct. time in file truncation: %20%%%n\r\nPct. time in page categorization: %21%%%n\r\nPct. time in data move: %22%%%n\r\nPct. remaining time: %23%%%n\r\n
0x000002ed | %1 (%2) %3The database file shrinkage operation failed on database '%4'.%n\r\nInitial file size: %7 bytes (%8 page(s)).%n\r\nFinal file size: %9 bytes (%10 page(s)).%n\r\nInitial owned space: %11 bytes (%12 page(s)).%n\r\nFinal owned space: %13 bytes (%14 page(s)).%n\r\nData moved: %15 bytes (%16 page(s)).%n\r\nPages shelved: %24 page(s).%n\r\nPages unleaked: %25 page(s).%n\r\nError code: %17%n\r\nStop reason: %18%n\r\nTotal time: %5 minute(s) and %6 second(s).%n\r\nPct. time in extent maintenance: %19%%%n\r\nPct. time in file truncation: %20%%%n\r\nPct. time in page categorization: %21%%%n\r\nPct. time in data move: %22%%%n\r\nPct. remaining time: %23%%%n\r\n
0x000002ee | %1 (%2) %3The space leakage reclaimer completed successfully on database '%4'.%n\r\nStop reason: %5%n\r\nTotal time: %6 minute(s) and %7 second(s).%n\r\nReturn code: %8%n\r\nInitial owned space: %9 bytes (%10 page(s)).%n\r\nFinal owned space: %11 bytes (%12 page(s)).%n\r\nLeaked pages reclaimed: %13 page(s).%n\r\nReclaimed page number range: %14 - %15%n\r\nShelved page count: %16 page(s).%n\r\nShelved page number range: %17 - %18%n\r\n
0x000002ef | %1 (%2) %3The space leakage reclaimer failed on database '%4'.%n\r\nStop reason: %5%n\r\nTotal time: %6 minute(s) and %7 second(s).%n\r\nReturn code: %8%n\r\nInitial owned space: %9 bytes (%10 page(s)).%n\r\nFinal owned space: %11 bytes (%12 page(s)).%n\r\nLeaked pages reclaimed: %13 page(s).%n\r\nReclaimed page number range: %14 - %15%n\r\nShelved page count: %16 page(s).%n\r\nShelved page number range: %17 - %18%n\r\n
0x000002f0 | %1 (%2) %3There are %4 outstanding tasks in the online defragmentation table for database %5.%n\r\n%6 of those outstanding tasks have not started.%n\r\n
0x00000320 | %1 (%2) %3System parameter minimum cache size (%4) is less than 4 times the number of sessions (%5).\r\n
0x00000321 | %1 (%2) %3System parameter maximum cache size (%4) is less than minimum cache size (%5).\r\n
0x00000322 | %1 (%2) %3System parameter maximum cache size (%4) is less than stop clean flush threshold (%5).\r\n
0x00000323 | %1 (%2) %3System parameter stop clean flush threshold (%4) is less than start clean flush threshold (%5).\r\n
0x00000324 | %1 (%2) %3System parameter log buffer size (%4 sectors) is greater than the maximum size of %5 k bytes (logfile size minus reserved space).\r\n
0x00000325 | %1 (%2) %3System parameter max version pages (%4) is less than preferred version pages (%5).\r\n
0x00000326 | %1 (%2) %3System parameter preferred version pages was changed from %4 to %5 due to physical memory limitation.\r\n
0x00000327 | %1 (%2) %3System parameter max open tables (%4) is less than preferred opentables (%5). Please check registry settings.\r\n
0x00000328 | %1 (%2) %3System parameter preferred version pages (%4) is greater than max version pages (%5). Preferred version pages was changed from %6 to %7.\r\n
0x00000384 | %1 (%2) %3The database engine failed with error %4 while trying to log the commit of a transaction. To ensure database consistency, the process was terminated. Simply restart the process to force database recovery and return the database to a Clean Shutdown state.\r\n
0x00000385 | %1 (%2) %3Tag: %6. Internal trace: %4 (%5).\r\n
0x00000386 | %1 (%2) %3The database engine detected multiple threads illegally using the same database session to perform database operations.\r\n%n%tSessionId: %4\r\n%n%tSession-context: %5\r\n%n%tSession-context ThreadId: %6\r\n%n%tCurrent ThreadId: %7\r\n%n%tSession-trace:\r\n%n%8\r\n
0x00000387 | %1 (%2) %3The database engine detected two different cursors of the same session illegally trying to update the same record at the same time.\r\n%n%tSessionId: %4\r\n%n%tThreadId: %5\r\n%n%tDatabase: %6\r\n%n%tTable: %7\r\n%n%tCurrent cursor: %8\r\n%n%tCursor owning original update: %9\r\n%n%tBookmark size (prefix/suffix): %10\r\n%n%tSession-trace:\r\n%n%11\r\n
0x00000388 | %1 (%2) %3A test API has been used to corrupt page %4 of database '%5'.\r\n
0x00000389 | %1 (%2) %3The database engine repaired corruption on page %4 of database '%5'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x0000038a | %1 (%2) %3A significant portion of the database buffer cache has been written out to the system paging file. This may result in severe performance degradation.\r\n%nSee help link for complete details of possible causes.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state:  %8% (%9 out of %10 buffers)\r\n%nCurrent cache size vs. target:  %11% (%12 MBs)\r\n%nPhysical Memory / RAM size:     %13 MBs\r\n
0x0000038b | %1 (%2) %3A transient memory corruption was detected.  Please run the Windows Memory Diagnostics Tool and/or investigate hardware issues.\r\n
0x0000038c | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5). Tag: %6.\r\n
0x0000038d | %1 (%2) %3Terminating process due to non-recoverable failure: %4 (%5) in operation on database '%6'.\r\n
0x0000038e | %1 (%2) %3The database cache size maintenance task has taken %4 seconds without completing. This may result in severe performance degradation.\r\nCurrent cache size is %5 buffers above the configured cache limit (%6 percent of target).\r\nCache size maintenance evicted %7 buffers, made %8 flush attempts, and successfully flushed %9 buffers. It has run %10 times since maintenance was triggered.\r\n
0x0000038f | %1 (%2) %3The database engine repaired corruption on pages %4 - %5 of database '%6'. Although the corruption has been repaired, the source of the corruption is likely due to faulty hardware and should be investigated.  Please contact your hardware vendor for further assistance diagnosing the problem.\r\n
0x00000390 | %1 (%2) %3A portion of the database buffer cache has been restored from the system paging file and is now resident again in memory. Prior to this, a portion of the database buffer cache had been written out to the system paging file resulting in performance degradation.\r\n%nPrevious cache residency state: %4% (%5 out of %6 buffers) (%7 seconds ago)\r\n%nCurrent cache residency state: %8% (%9 out of %10 buffers)\r\n
0x00000391 | %1 (%2) %3The parameter %4 was not set to one value by the previous ESE application instance, but set to a different value from the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000392 | %1 (%2) %3The parameter %4 was not set via the previous ESE application instance, but is set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000393 | %1 (%2) %3The parameter %4 was set via the previous ESE application instance, but is not set in the current ESE application. This is a system parameter mismatch, all ESE applications must agree on all global system parameters.\r\n
0x00000394 | %1 (%2) %3The beta feature %4 is enabled in %5 due to the beta site mode settings %6.\r\n
0x000003e8 | %1 (%2) %3Resource failure simulation was activated with the following settings:\r\n\t\t%4:\t%5\r\n\t\t%6:\t%7\r\n\t\t%8:\t%9\r\n\t\t%10:\t%11\r\n
0x000003e9 | %1 (%2) %3Resource failure simulation %4 is permitted.\r\n
0x000003ea | %1 (%2) %3Resource Failure Simulation %4 is denied.\r\n
0x000003eb | %1 (%2) %3JET call %4 returned error %5. %6 (%7)\r\n
0x000003ec | %1 (%2) %3JET inline error %4 jumps to label %5. %6 (%7)\r\n
0x000007d0 | %1 (%2) %3Shadow copy function %4() = %5.\r\n
0x000007d1 | %1 (%2) %3Shadow copy instance %4 freeze started.\r\n
0x000007d2 | %1 (%2) %3Shadow copy instance %4 encountered error %5 on freeze.\r\n
0x000007d3 | %1 (%2) %3Shadow copy instance %4 freeze ended.\r\n
0x000007d4 | %1 (%2) %3Shadow copy instance %4 freeze timed-out (%5 ms).\r\n
0x000007d5 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Full shadow copy.\r\n
0x000007d6 | %1 (%2) %3Shadow copy instance %4 completed successfully.\r\n
0x000007d7 | %1 (%2) %3Shadow copy instance %4 aborted.\r\n
0x000007d8 | %1 (%2) %3Shadow copy instance %4 starting. This will be an Incremental shadow copy.\r\n
0x000007d9 | %1 (%2) %3Shadow copy instance %4 starting. This will be a Copy shadow copy.\r\n
0x000007da | %1 (%2) %3Shadow copy instance %4 starting. This will be a Differential shadow copy.\r\n
0x00000bb8 | NOOP_FAILURE_TAG_ID\r\n
0x00000bb9 | %1 (%2) %3A configuration error is preventing proper operation of database '%4' ('%5').  The error may occur because of a database misconfiguration, a permission problem, or a storage-related problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bba | %1 (%2) %3A read verification or I/O error is preventing proper operation of database '%4' ('%5'). Review the event logs and other log data to determine if your system is experiencing storage-related problems.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbb | %1 (%2) %3Lack of free space for the database or log files is preventing proper operation of database '%4' ('%5').  Review the database and log volume's free space to identify the specific problem.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbc | %1 (%2) %3An I/O error is preventing proper operation of database '%4' ('%5').  Review events logs and other log data to determine if your system is experiencing storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbd | %1 (%2) %3A passive copy has detected a corruption in the mounted copy of database '%4' ('%5'). This error might be the result of a storage-related problem.%n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbe | %1 (%2) %3Corruption has been detected in database '%4' ('%5').  The error may occur because of human errors, system, or storage problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bbf | %1 (%2) %3Resources or an operating error is preventing proper functioning of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc0 | %1 (%2) %3A serious error is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc1 | %1 (%2) %3Problems are preventing proper operation of database '%4' ('%5').  The failure may be corrected by remounting the database.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc2 | %1 (%2) %3In a log shipping environment, a passive copy has detected an error that is preventing proper operation of database '%4' ('%5').  Review the application and system event logs for failures of the database or its required system components.\r\n
0x00000bc3 | %1 (%2) %3A performance problem is affecting proper operation of database '%4' ('%5').  The error may occur due to misconfiguration, storage problems, or performance problems on the computer.  Review the performance counters and application event logs associated with the database, its storage, and the computer to identify the specific problems.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc4 | %1 (%2) %3An unusually large amount of normal load is preventing proper operation of database '%4' ('%5').  The load on this database should be reduced to restore proper operation.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc5 | %1 (%2) %3The system is experiencing memory allocation failures that are preventing proper operation of database '%4' ('%5').  The error could occur due to a mis-configuration or excessive memory consumption on the machine.\r\n%n\r\n%nAdditional diagnostic information:  %6 %7\r\n
0x00000bc6 | CATALOGRESEED_FAILURE_TAG_ID\r\n
0x00000bc7 | MAX_FAILURE_TAG_ID\r\n
0x00000fa0 | %1 (%2) %3The caching file with the requested physical ids could not be found.%n\r\n%n\r\nVolume id=%4%n\r\nFile id=%5%n\r\nUnique id=%6%n\r\n
0x00000fa1 | %1 (%2) %3The caching file at '%4' could not be opened due to error %5.  Caching cannot be performed for files backed by this cache.%n\r\n
0x00000fa2 | %1 (%2) %3The file '%4' has a different file id than expected.%n\r\n%n\r\nExpected Volume id=%5%n\r\nExpected File id=%6%n\r\n%n\r\nActual Volume id=%7%n\r\nActual File id=%8%n\r\n
0x00000fa3 | %1 (%2) %3The cached file with the requested physical ids could not be found.%n\r\n%n\r\nVolume id=%4%n\r\nFile id=%5%n\r\nFile serial=%6%n\r\n
0x00001388 | %1 (%2) %3The revert snapshot file at "%4" was "%5" successfully.\r\n
0x00001389 | %1 (%2) %3The revert snapshot file at "%4" failed to be "%5" with error "%6".\r\n
0x0000138a | %1 (%2) %3The revert snapshot directory "%4" was removed by RBS cleaner. Reason: "%5".\r\n
0x0000138b | %1 (%2) %3Databases were reverted from "%4" to "%5" successfully.\r\n
0x0000138c | %1 (%2) %3Databases were failed to be reverted from "%4" to "%5" with error "%6".\r\n
0x0000138d | %1 (%2) %3The creation of revert snapshot file at "%4" was skipped due to "%5". Load failed with error "%6".\r\n
0x0000138e | %1 (%2) %3The revert snapshot file "%4" created on "%5" has grown by "%6 bytes" since "%7". Number of logs generated during this period was "%8".\r\n
