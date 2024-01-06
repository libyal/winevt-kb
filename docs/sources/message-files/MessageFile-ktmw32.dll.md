## ktmw32.dll

Path: %SystemRoot%\system32\ktmw32.dll

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384, 6.3.9600.17415, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.19041.546, 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000001 | The Transaction (UOW=%1, Description='%3') was unable to be committed, and instead rolled back; this was due to an error message returned by CLFS while attempting to write a Prepare or Commit record for the Transaction.  The CLFS error returned was: %4.\r\n
0x00000002 | The Transaction (UOW=%1, Description='%3') blocked a Freeze from completing.  Freeze is necessary to ensure that a VSS snapshot is transactionally consistent.  The ResourceManager (RmId=%4, Description='%6') may not be functioning correctly, since it did not allow the transaction to drain in the allotted time.  Contact the vendor for that ResourceManager for assistance.\r\n
0x00000003 | The transaction (UOW=%1, Description='%3') was heuristically aborted and forgotten from the TransactionManager (TmId=%4, LogPath=%6) so that the TransactionManager can continue to make forward progress.  This may cause data corruption in any subordinate ResourceManagers or Transactionmanager.\r\n
0x00000004 | The TransactionManager (TmId=%1, LogPath=%3) has failed to advance its log tail, due to the transaction (UOW=%4, Description='%6') being unresolved for some time.  The transaction must be forced to resolve in order for the TransactionManager to continue to provide transactional services.  Forcing the incorrect outcome may cause data corruption in any subordinate ResourceManagers or Transactionmanagers.\r\n
0x50000003 | Warning\r\n
0x51000004 | Information\r\n
0x90000001 | System\r\n
