## fvevol.sys

Path: %SystemRoot%\system32\drivers\fvevol.sys

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x00006001 | Encryption of volume %2 started.\r\n
0x00006002 | Encryption of volume %2 stopped.\r\n
0x00006003 | Encryption of volume %2 completed.\r\n
0x00006004 | Decryption of volume %2 started.\r\n
0x00006005 | Decryption of volume %2 stopped.\r\n
0x00006006 | Decryption of volume %2 completed.\r\n
0x00006007 | Conversion worker thread for volume %2 was started.\r\n
0x00006008 | Conversion worker thread for volume %2 was temporarily stopped.\r\n
0x00006009 | Auto-unlock enabled for volume %2.\r\n
0x0000600a | An error was encountered converting volume %2.\r\n
0x0000600b | Auto-unlock disabled for volume %2.\r\n
0x0000600c | The conversion operation on volume %2 encountered a bad sector error. Please validate the data on this volume.\r\n
0x0000600d | Failed to enable auto-unlock for volume %2.\r\n
0x0000600e | Failed to disable auto-unlock for volume %2.\r\n
0x0000600f | Auto-unlocking failed for volume %2.\r\n
0x00006010 | An attempt to automatically restart conversion on volume %2 failed.\r\n
0x00006011 | Metadata write: Volume %2 returning errors while trying to modify metadata. If failures continue, decrypt volume.\r\n
0x00006012 | Metadata rebuild: An attempt to write a copy of metadata on volume %2 failed and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x00006013 | Volume %2 contains bad clusters. These clusters will be skipped during conversion.\r\n
0x00006014 | No key file was found for Volume %2 during restart.\r\n
0x00006015 | A corrupt key file was encountered for Volume %2 during restart.\r\n
0x00006016 | No volume master key was retrieved in a key file during restart.\r\n
0x00006017 | The TPM was not enabled during restart.\r\n
0x00006018 | The SRK was found to be invalid during restart.\r\n
0x00006019 | The PCRs did not match during restart.\r\n
0x0000601a | No volume master key was retrieved from a key file during restart.\r\n
0x0000601b | A boot application hash did not match expected value during restart.\r\n
0x0000601c | The boot configuration options did not match expected values during restart.\r\n
0x0000601d | No volume master key was retrieved from a PIN during restart.\r\n
0x0000601e | No volume master key was retrieved from a recovery password during restart.\r\n
0x0000601f | A valid key was found during the last restart.\r\n
0x00006020 | An unexpected error was encountered attempting to retrieve the volume master key during restart.\r\n
0x00006021 | A key was not available from required sources during restart.\r\n
0x00006022 | Metadata commit: Not all copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006023 | Metadata commit: No copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006024 | Metadata commit: Metadata update could not be flushed.\r\n
0x00006025 | Metadata commit: An attempt to verify metadata update on volume %2 failed at read. If failures continue, decrypt volume.\r\n
0x00006026 | Metadata commit: Update verification of metadata on volume %2 failed. If failures continue, decrypt volume.\r\n
0x00006027 | Metadata initial read: Primary metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006028 | Metadata initial read: Failover metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006029 | Metadata initial read: Failover metadata record on volume %2 used. If failures continue, decrypt volume.\r\n
0x0000602a | Metadata check: Metadata record on volume %2 could not be read and has been marked for rebuild. If failures continue, decrypt volume.\r\n
0x0000602b | Metadata rebuild: An attempt build a new set of metadata on %2 failed at commit and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x0000602c | Encrypted volume check: Volume information on %2 cannot be read.\r\n
0x0000602d | Initial state check: Rolling volume conversion transaction on %2.\r\n
0x0000602e | BIOS/TCG Memory Overwrite Control: Error finding TPM driver.\r\n
0x0000602f | BIOS/TCG Memory Overwrite Control: Error registering TPM device interface.\r\n
0x00006030 | BIOS/TCG Memory Overwrite Control: Error changing value.\r\n
0x00006031 | A valid BitLocker key was found during the last restart.\r\n
0x00006032 | The auto-unlock master key was not available from the operating system volume.  Retry the operation via the BitLocker WMI interface.\r\n
0x00006033 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00006034 | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00006035 | The system firmware failed to enable overwriting of system memory on restart. The firmware should be upgraded.\r\n
0x00006036 | Bootmgr failed to find a BitLocker key file for Volume %2.\r\n
0x00006037 | Bootmgr detected corruption in the BitLocker key file for Volume %2.\r\n
0x00006038 | Bootmgr failed to obtain the BitLocker volume master key from the key file contents.\r\n
0x00006039 | Bootmgr determined that the TPM is disabled.\r\n
0x0000603a | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000603b | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000603c | Bootmgr failed to obtain the BitLocker volume master key from the TPM.\r\n
0x0000603d | A boot application hash did not match the expected value during restart.\r\n
0x0000603e | Bootmgr failed to obtain the BitLocker volume master key from the TPM + PIN.\r\n
0x0000603f | Bootmgr failed to obtain the BitLocker volume master key from the recovery password.\r\n
0x00006040 | A valid BitLocker key was found during the last restart.\r\n
0x00006041 | An unexpected error was encountered attempting to retrieve the BitLocker volume master key during restart.\r\n
0x00006042 | An internal BitLocker self-test failed for drive %2. BitLocker cannot continue encrypting data. Contact your system administrator.\r\n
0x00006043 | Bootmgr failed to obtain the BitLocker volume master key from the TPM + enhanced PIN.\r\n
0x00006044 | An internal BitLocker self-test failed for drive %2 when switching from raw mode to filtering mode. BitLocker cannot continue encrypting data on this drive. Contact your system administrator.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BitLocker-Driver\r\n
0x90000002 | System\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00006001 | Encryption of volume %2 started.\r\n
0x00006002 | Encryption of volume %2 stopped.\r\n
0x00006003 | Encryption of volume %2 completed.\r\n
0x00006004 | Decryption of volume %2 started.\r\n
0x00006005 | Decryption of volume %2 stopped.\r\n
0x00006006 | Decryption of volume %2 completed.\r\n
0x00006007 | Conversion worker thread for volume %2 was started.\r\n
0x00006008 | Conversion worker thread for volume %2 was temporarily stopped.\r\n
0x00006009 | Auto-unlock enabled for volume %2.\r\n
0x0000600a | An error was encountered converting volume %2.\r\n
0x0000600b | Auto-unlock disabled for volume %2.\r\n
0x0000600c | The conversion operation on volume %2 encountered a bad sector error. Please validate the data on this volume.\r\n
0x0000600d | Failed to enable auto-unlock for volume %2.\r\n
0x0000600e | Failed to disable auto-unlock for volume %2.\r\n
0x0000600f | Auto-unlocking failed for volume %2.\r\n
0x00006010 | An attempt to automatically restart conversion on volume %2 failed.\r\n
0x00006011 | Metadata write: Volume %2 returning errors while trying to modify metadata. If failures continue, decrypt volume.\r\n
0x00006012 | Metadata rebuild: An attempt to write a copy of metadata on volume %2 failed and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x00006013 | Volume %2 contains bad clusters. These clusters will be skipped during conversion.\r\n
0x00006014 | No key file was found for Volume %2 during restart.\r\n
0x00006015 | A corrupt key file was encountered for Volume %2 during restart.\r\n
0x00006016 | No volume master key was retrieved in a key file during restart.\r\n
0x00006017 | The TPM was not enabled during restart.\r\n
0x00006018 | The SRK was found to be invalid during restart.\r\n
0x00006019 | The PCRs did not match during restart.\r\n
0x0000601a | No volume master key was retrieved from a key file during restart.\r\n
0x0000601b | A boot application hash did not match expected value during restart.\r\n
0x0000601c | The boot configuration options did not match expected values during restart.\r\n
0x0000601d | No volume master key was retrieved from a PIN during restart.\r\n
0x0000601e | No volume master key was retrieved from a recovery password during restart.\r\n
0x0000601f | A valid key was found during the last restart.\r\n
0x00006020 | An unexpected error was encountered attempting to retrieve the volume master key during restart.\r\n
0x00006021 | A key was not available from required sources during restart.\r\n
0x00006022 | Metadata commit: Not all copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006023 | Metadata commit: No copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006024 | Metadata commit: Metadata update could not be flushed.\r\n
0x00006025 | Metadata commit: An attempt to verify metadata update on volume %2 failed at read. If failures continue, decrypt volume.\r\n
0x00006026 | Metadata commit: Update verification of metadata on volume %2 failed. If failures continue, decrypt volume.\r\n
0x00006027 | Metadata initial read: Primary metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006028 | Metadata initial read: Failover metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006029 | Metadata initial read: Failover metadata record on volume %2 used. If failures continue, decrypt volume.\r\n
0x0000602a | Metadata check: Metadata record on volume %2 could not be read and has been marked for rebuild. If failures continue, decrypt volume.\r\n
0x0000602b | Metadata rebuild: An attempt build a new set of metadata on %2 failed at commit and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x0000602c | Encrypted volume check: Volume information on %2 cannot be read.\r\n
0x0000602d | Initial state check: Rolling volume conversion transaction on %2.\r\n
0x0000602e | BIOS/TCG Memory Overwrite Control: Error finding TPM driver.\r\n
0x0000602f | BIOS/TCG Memory Overwrite Control: Error registering TPM device interface.\r\n
0x00006030 | BIOS/TCG Memory Overwrite Control: Error changing value.\r\n
0x00006031 | A valid BitLocker key was found during the last restart.\r\n
0x00006032 | The auto-unlock master key was not available from the operating system volume.  Retry the operation via the BitLocker WMI interface.\r\n
0x00006033 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00006034 | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00006035 | The system firmware failed to enable overwriting of system memory on restart. The firmware should be upgraded.\r\n
0x00006036 | Bootmgr failed to find a BitLocker key file for Volume %2.\r\n
0x00006037 | Bootmgr detected corruption in the BitLocker key file for Volume %2.\r\n
0x00006038 | Bootmgr failed to obtain the BitLocker volume master key from the key file contents.\r\n
0x00006039 | Bootmgr determined that the TPM is disabled.\r\n
0x0000603a | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000603b | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000603c | Bootmgr failed to obtain the BitLocker volume master key from the TPM.\r\n
0x0000603d | A boot application hash did not match the expected value during restart.\r\n
0x0000603e | Bootmgr failed to obtain the BitLocker volume master key from the TPM + PIN.\r\n
0x0000603f | Bootmgr failed to obtain the BitLocker volume master key from the recovery password.\r\n
0x00006040 | A valid BitLocker key was found during the last restart.\r\n
0x00006041 | An unexpected error was encountered attempting to retrieve the BitLocker volume master key during restart.\r\n
0x00006042 | An internal BitLocker self-test failed for drive %2. BitLocker cannot continue encrypting data. Contact your system administrator.\r\n
0x00006043 | Bootmgr failed to obtain the BitLocker volume master key from the TPM + enhanced PIN.\r\n
0x00006044 | An internal BitLocker self-test failed for drive %2 when switching from raw mode to filtering mode. BitLocker cannot continue encrypting data on this drive. Contact your system administrator.\r\n
0x00006045 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector.\r\n
0x00006046 | Encryption of the used space on volume %2 started.\r\n
0x00006047 | Encryption of the used space on volume %2 stopped.\r\n
0x00006048 | Encryption of the used space on volume %2 completed.\r\n
0x00006049 | Wiping of free space on volume %2 started.\r\n
0x0000604a | Wiping of free space on volume %2 stopped.\r\n
0x0000604b | Wiping of free space on volume %2 completed.\r\n
0x0000604c | A recovery password was used to start Windows.%nProtector ID: %5.\r\n
0x0000604d | Bootmgr failed to obtain the BitLocker volume master key from the password.\r\n
0x0000604e | A recovery key was used to start Windows.%nProtector ID: %5.\r\n
0x0000604f | The BitLocker driver has started a self-healing operation on the metadata of volume %2.\r\n
0x00006050 | The BitLocker driver has successfully completed a self-healing operation on the metadata of volume %2.\r\n
0x00006051 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00006052 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x00006053 | Device Lock was triggered due to too many incorrect password attempts.\r\n
0x00006054 | BitLocker encryption on write started for volume %2.\r\n
0x00006055 | BitLocker free space sweep started for volume %2.\r\n
0x00006056 | BitLocker free space sweep stopped for volume %2.\r\n
0x00006057 | BitLocker free space sweep completed for volume %2.\r\n
0x00006058 | BitLocker finalization sweep started for volume %2.\r\n
0x00006059 | BitLocker finalization sweep paused for volume %2.\r\n
0x0000605a | BitLocker finalization sweep resumed for volume %2.\r\n
0x0000605b | BitLocker finalization sweep completed for volume %2.\r\n
0x0000605c | BitLocker encryption on write failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605d | BitLocker finalization sweep failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605e | Disk containing volume %2 is employing non-volatile caching software which does not support control over its caching policies. This may temporarily impact BitLocker's ability to fully secure your data.\r\n
0x0000605f | Disk containing volume %2 is employing non-volatile caching software which is experiencing problems. This may temporarily impact BitLocker's ability to fully secure your data. Contact disk manufacturer for an updated software.\r\n
0x00006060 | Device Lock was triggered due to Device Lockout state validation failure.\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BitLocker-Driver\r\n
0x90000002 | System\r\n
0x91000001 | Microsoft-Windows-BitLocker-Driver-Performance\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00006001 | Encryption of volume %2 started.\r\n
0x00006002 | Encryption of volume %2 stopped.\r\n
0x00006003 | Encryption of volume %2 completed.\r\n
0x00006004 | Decryption of volume %2 started.\r\n
0x00006005 | Decryption of volume %2 stopped.\r\n
0x00006006 | Decryption of volume %2 completed.\r\n
0x00006007 | Conversion worker thread for volume %2 was started.\r\n
0x00006008 | Conversion worker thread for volume %2 was temporarily stopped.\r\n
0x00006009 | Auto-unlock enabled for volume %2.\r\n
0x0000600a | An error was encountered converting volume %2.\r\n
0x0000600b | Auto-unlock disabled for volume %2.\r\n
0x0000600c | The conversion operation on volume %2 encountered a bad sector error. Please validate the data on this volume.\r\n
0x0000600d | Failed to enable auto-unlock for volume %2.\r\n
0x0000600e | Failed to disable auto-unlock for volume %2.\r\n
0x0000600f | Auto-unlocking failed for volume %2.\r\n
0x00006010 | An attempt to automatically restart conversion on volume %2 failed.\r\n
0x00006011 | Metadata write: Volume %2 returning errors while trying to modify metadata. If failures continue, decrypt volume.\r\n
0x00006012 | Metadata rebuild: An attempt to write a copy of metadata on volume %2 failed and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x00006013 | Volume %2 contains bad clusters. These clusters will be skipped during conversion.\r\n
0x00006014 | No key file was found for Volume %2 during restart.\r\n
0x00006015 | A corrupt key file was encountered for Volume %2 during restart.\r\n
0x00006016 | No volume master key was retrieved in a key file during restart.\r\n
0x00006017 | The TPM was not enabled during restart.\r\n
0x00006018 | The SRK was found to be invalid during restart.\r\n
0x00006019 | The PCRs did not match during restart.\r\n
0x0000601a | No volume master key was retrieved from a key file during restart.\r\n
0x0000601b | A boot application hash did not match expected value during restart.\r\n
0x0000601c | The boot configuration options did not match expected values during restart.\r\n
0x0000601d | No volume master key was retrieved from a PIN during restart.\r\n
0x0000601e | No volume master key was retrieved from a recovery password during restart.\r\n
0x0000601f | A valid key was found during the last restart.\r\n
0x00006020 | An unexpected error was encountered attempting to retrieve the volume master key during restart.\r\n
0x00006021 | A key was not available from required sources during restart.\r\n
0x00006022 | Metadata commit: Not all copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006023 | Metadata commit: No copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006024 | Metadata commit: Metadata update could not be flushed.\r\n
0x00006025 | Metadata commit: An attempt to verify metadata update on volume %2 failed at read. If failures continue, decrypt volume.\r\n
0x00006026 | Metadata commit: Update verification of metadata on volume %2 failed. If failures continue, decrypt volume.\r\n
0x00006027 | Metadata initial read: Primary metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006028 | Metadata initial read: Failover metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006029 | Metadata initial read: Failover metadata record on volume %2 used. If failures continue, decrypt volume.\r\n
0x0000602a | Metadata check: Metadata record on volume %2 could not be read and has been marked for rebuild. If failures continue, decrypt volume.\r\n
0x0000602b | Metadata rebuild: An attempt build a new set of metadata on %2 failed at commit and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x0000602c | Encrypted volume check: Volume information on %2 cannot be read.\r\n
0x0000602d | Initial state check: Rolling volume conversion transaction on %2.\r\n
0x0000602e | BIOS/TCG Memory Overwrite Control: Error finding TPM driver.\r\n
0x0000602f | BIOS/TCG Memory Overwrite Control: Error registering TPM device interface.\r\n
0x00006030 | BIOS/TCG Memory Overwrite Control: Error changing value.\r\n
0x00006031 | A valid BitLocker key was found during the last restart.\r\n
0x00006032 | The auto-unlock master key was not available from the operating system volume.  Retry the operation via the BitLocker WMI interface.\r\n
0x00006033 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00006034 | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00006035 | The system firmware failed to enable overwriting of system memory on restart. The firmware should be upgraded.\r\n
0x00006036 | Bootmgr failed to find a BitLocker key file for Volume %2.\r\n
0x00006037 | Bootmgr detected corruption in the BitLocker key file for Volume %2.\r\n
0x00006038 | Bootmgr failed to obtain the BitLocker volume master key from the key file contents.\r\n
0x00006039 | Bootmgr determined that the TPM is disabled.\r\n
0x0000603a | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000603b | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000603c | Bootmgr failed to obtain the BitLocker volume master key from the TPM.\r\n
0x0000603d | A boot application hash did not match the expected value during restart.\r\n
0x0000603e | Bootmgr failed to obtain the BitLocker volume master key from the TPM + PIN.\r\n
0x0000603f | Bootmgr failed to obtain the BitLocker volume master key from the recovery password.\r\n
0x00006040 | A valid BitLocker key was found during the last restart.\r\n
0x00006041 | An unexpected error was encountered attempting to retrieve the BitLocker volume master key during restart.\r\n
0x00006042 | An internal BitLocker self-test failed for drive %2. BitLocker cannot continue encrypting data. Contact your system administrator.\r\n
0x00006043 | Bootmgr failed to obtain the BitLocker volume master key from the TPM + enhanced PIN.\r\n
0x00006044 | An internal BitLocker self-test failed for drive %2 when switching from raw mode to filtering mode. BitLocker cannot continue encrypting data on this drive. Contact your system administrator.\r\n
0x00006045 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector.\r\n
0x00006046 | Encryption of the used space on volume %2 started.\r\n
0x00006047 | Encryption of the used space on volume %2 stopped.\r\n
0x00006048 | Encryption of the used space on volume %2 completed.\r\n
0x00006049 | Wiping of free space on volume %2 started.\r\n
0x0000604a | Wiping of free space on volume %2 stopped.\r\n
0x0000604b | Wiping of free space on volume %2 completed.\r\n
0x0000604c | A recovery password was used to start Windows.%nProtector ID: %5.\r\n
0x0000604d | Bootmgr failed to obtain the BitLocker volume master key from the password.\r\n
0x0000604e | A recovery key was used to start Windows.%nProtector ID: %5.\r\n
0x0000604f | The BitLocker driver has started a self-healing operation on the metadata of volume %2.\r\n
0x00006050 | The BitLocker driver has successfully completed a self-healing operation on the metadata of volume %2.\r\n
0x00006051 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00006052 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x00006053 | Device Lock was triggered due to too many incorrect password attempts.\r\n
0x00006054 | BitLocker encryption on write started for volume %2.\r\n
0x00006055 | BitLocker free space sweep started for volume %2.\r\n
0x00006056 | BitLocker free space sweep stopped for volume %2.\r\n
0x00006057 | BitLocker free space sweep completed for volume %2.\r\n
0x00006058 | BitLocker finalization sweep started for volume %2.\r\n
0x00006059 | BitLocker finalization sweep paused for volume %2.\r\n
0x0000605a | BitLocker finalization sweep resumed for volume %2.\r\n
0x0000605b | BitLocker finalization sweep completed for volume %2.\r\n
0x0000605c | BitLocker encryption on write failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605d | BitLocker finalization sweep failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605e | Disk containing volume %2 is employing non-volatile caching software which does not support control over its caching policies. This may temporarily impact BitLocker's ability to fully secure your data.\r\n
0x0000605f | Disk containing volume %2 is employing non-volatile caching software which is experiencing problems. This may temporarily impact BitLocker's ability to fully secure your data. Contact disk manufacturer for an updated software.\r\n
0x00006060 | Device Lock was triggered due to Device Lockout state validation failure.\r\n
0x00006061 | Drive %2 is no longer automatically managed by device encryption.\r\n
0x00006062 | Drive %2 is now automatically managed by device encryption.\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BitLocker-Driver\r\n
0x90000002 | System\r\n
0x91000001 | Microsoft-Windows-BitLocker-Driver-Performance\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x00006001 | Encryption of volume %2 started.\r\n
0x00006002 | Encryption of volume %2 stopped.\r\n
0x00006003 | Encryption of volume %2 completed.\r\n
0x00006004 | Decryption of volume %2 started.\r\n
0x00006005 | Decryption of volume %2 stopped.\r\n
0x00006006 | Decryption of volume %2 completed.\r\n
0x00006007 | Conversion worker thread for volume %2 was started.\r\n
0x00006008 | Conversion worker thread for volume %2 was temporarily stopped.\r\n
0x00006009 | Auto-unlock enabled for volume %2.\r\n
0x0000600a | An error was encountered converting volume %2.\r\n
0x0000600b | Auto-unlock disabled for volume %2.\r\n
0x0000600c | The conversion operation on volume %2 encountered a bad sector error. Please validate the data on this volume.\r\n
0x0000600d | Failed to enable auto-unlock for volume %2.\r\n
0x0000600e | Failed to disable auto-unlock for volume %2.\r\n
0x0000600f | Auto-unlocking failed for volume %2.\r\n
0x00006010 | An attempt to automatically restart conversion on volume %2 failed.\r\n
0x00006011 | Metadata write: Volume %2 returning errors while trying to modify metadata. If failures continue, decrypt volume.\r\n
0x00006012 | Metadata rebuild: An attempt to write a copy of metadata on volume %2 failed and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x00006013 | Volume %2 contains bad clusters. These clusters will be skipped during conversion.\r\n
0x00006014 | No key file was found for Volume %2 during restart.\r\n
0x00006015 | A corrupt key file was encountered for Volume %2 during restart.\r\n
0x00006016 | No volume master key was retrieved in a key file during restart.\r\n
0x00006017 | The TPM was not enabled during restart.\r\n
0x00006018 | The SRK was found to be invalid during restart.\r\n
0x00006019 | The PCRs did not match during restart.\r\n
0x0000601a | No volume master key was retrieved from a key file during restart.\r\n
0x0000601b | A boot application hash did not match expected value during restart.\r\n
0x0000601c | The boot configuration options did not match expected values during restart.\r\n
0x0000601d | No volume master key was retrieved from a PIN during restart.\r\n
0x0000601e | No volume master key was retrieved from a recovery password during restart.\r\n
0x0000601f | A valid key was found during the last restart.\r\n
0x00006020 | An unexpected error was encountered attempting to retrieve the volume master key during restart.\r\n
0x00006021 | A key was not available from required sources during restart.\r\n
0x00006022 | Metadata commit: Not all copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006023 | Metadata commit: No copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006024 | Metadata commit: Metadata update could not be flushed.\r\n
0x00006025 | Metadata commit: An attempt to verify metadata update on volume %2 failed at read. If failures continue, decrypt volume.\r\n
0x00006026 | Metadata commit: Update verification of metadata on volume %2 failed. If failures continue, decrypt volume.\r\n
0x00006027 | Metadata initial read: Primary metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006028 | Metadata initial read: Failover metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006029 | Metadata initial read: Failover metadata record on volume %2 used. If failures continue, decrypt volume.\r\n
0x0000602a | Metadata check: Metadata record on volume %2 could not be read and has been marked for rebuild. If failures continue, decrypt volume.\r\n
0x0000602b | Metadata rebuild: An attempt build a new set of metadata on %2 failed at commit and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x0000602c | Encrypted volume check: Volume information on %2 cannot be read.\r\n
0x0000602d | Initial state check: Rolling volume conversion transaction on %2.\r\n
0x0000602e | BIOS/TCG Memory Overwrite Control: Error finding TPM driver.\r\n
0x0000602f | BIOS/TCG Memory Overwrite Control: Error registering TPM device interface.\r\n
0x00006030 | BIOS/TCG Memory Overwrite Control: Error changing value.\r\n
0x00006031 | A valid BitLocker key was found during the last restart.\r\n
0x00006032 | The auto-unlock master key was not available from the operating system volume.  Retry the operation via the BitLocker WMI interface.\r\n
0x00006033 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00006034 | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00006035 | The system firmware failed to enable overwriting of system memory on restart. The firmware should be upgraded.\r\n
0x00006036 | Bootmgr failed to find a BitLocker key file for Volume %2.\r\n
0x00006037 | Bootmgr detected corruption in the BitLocker key file for Volume %2.\r\n
0x00006038 | Bootmgr failed to obtain the BitLocker volume master key from the key file contents.\r\n
0x00006039 | Bootmgr determined that the TPM is disabled.\r\n
0x0000603a | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000603b | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000603c | Bootmgr failed to obtain the BitLocker volume master key from the TPM.\r\n
0x0000603d | A boot application hash did not match the expected value during restart.\r\n
0x0000603e | Bootmgr failed to obtain the BitLocker volume master key from the TPM + PIN.\r\n
0x0000603f | Bootmgr failed to obtain the BitLocker volume master key from the recovery password.\r\n
0x00006040 | A valid BitLocker key was found during the last restart.\r\n
0x00006041 | An unexpected error was encountered attempting to retrieve the BitLocker volume master key during restart.\r\n
0x00006042 | An internal BitLocker self-test failed for drive %2. BitLocker cannot continue encrypting data. Contact your system administrator.\r\n
0x00006043 | Bootmgr failed to obtain the BitLocker volume master key from the TPM + enhanced PIN.\r\n
0x00006044 | An internal BitLocker self-test failed for drive %2 when switching from raw mode to filtering mode. BitLocker cannot continue encrypting data on this drive. Contact your system administrator.\r\n
0x00006045 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector.\r\n
0x00006046 | Encryption of the used space on volume %2 started.\r\n
0x00006047 | Encryption of the used space on volume %2 stopped.\r\n
0x00006048 | Encryption of the used space on volume %2 completed.\r\n
0x00006049 | Wiping of free space on volume %2 started.\r\n
0x0000604a | Wiping of free space on volume %2 stopped.\r\n
0x0000604b | Wiping of free space on volume %2 completed.\r\n
0x0000604c | A recovery password was used to start Windows.%nProtector ID: %5.\r\n
0x0000604d | Bootmgr failed to obtain the BitLocker volume master key from the password.\r\n
0x0000604e | A recovery key was used to start Windows.%nProtector ID: %5.\r\n
0x0000604f | The BitLocker driver has started a self-healing operation on the metadata of volume %2.\r\n
0x00006050 | The BitLocker driver has successfully completed a self-healing operation on the metadata of volume %2.\r\n
0x00006051 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00006052 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x00006053 | Device Lock was triggered due to too many incorrect password attempts.\r\n
0x00006054 | BitLocker encryption on write started for volume %2.\r\n
0x00006055 | BitLocker free space sweep started for volume %2.\r\n
0x00006056 | BitLocker free space sweep stopped for volume %2.\r\n
0x00006057 | BitLocker free space sweep completed for volume %2.\r\n
0x00006058 | BitLocker finalization sweep started for volume %2.\r\n
0x00006059 | BitLocker finalization sweep paused for volume %2.\r\n
0x0000605a | BitLocker finalization sweep resumed for volume %2.\r\n
0x0000605b | BitLocker finalization sweep completed for volume %2.\r\n
0x0000605c | BitLocker encryption on write failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605d | BitLocker finalization sweep failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605e | Disk containing volume %2 is employing non-volatile caching software which does not support control over its caching policies. This may temporarily impact BitLocker's ability to fully secure your data.\r\n
0x0000605f | Disk containing volume %2 is employing non-volatile caching software which is experiencing problems. This may temporarily impact BitLocker's ability to fully secure your data. Contact disk manufacturer for an updated software.\r\n
0x00006060 | Device Lock was triggered due to Device Lockout state validation failure.\r\n
0x00006061 | Drive %2 is no longer automatically managed by device encryption.\r\n
0x00006062 | Drive %2 is now automatically managed by device encryption.\r\n
0x00006063 | WIM hash generation paused for volume %2.\r\n
0x00006064 | WIM hash generation resumed for volume %2.\r\n
0x00006065 | WIM hash generation completed for volume %2.\r\n
0x00006066 | WIM hash generation failed for volume %2.\r\n
0x00006067 | WIM hashes will be deleted for volume %2.\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BitLocker-Driver\r\n
0x90000002 | System\r\n
0x91000001 | Microsoft-Windows-BitLocker-Driver-Performance\r\n

### 10.0.14393.206

Message identifier | Message string
--- | ---
0x00006001 | Encryption of volume %2 started.\r\n
0x00006002 | Encryption of volume %2 stopped.\r\n
0x00006003 | Encryption of volume %2 completed.\r\n
0x00006004 | Decryption of volume %2 started.\r\n
0x00006005 | Decryption of volume %2 stopped.\r\n
0x00006006 | Decryption of volume %2 completed.\r\n
0x00006007 | Conversion worker thread for volume %2 was started.\r\n
0x00006008 | Conversion worker thread for volume %2 was temporarily stopped.\r\n
0x00006009 | Auto-unlock enabled for volume %2.\r\n
0x0000600a | An error was encountered converting volume %2.\r\n
0x0000600b | Auto-unlock disabled for volume %2.\r\n
0x0000600c | The conversion operation on volume %2 encountered a bad sector error. Please validate the data on this volume.\r\n
0x0000600d | Failed to enable auto-unlock for volume %2.\r\n
0x0000600e | Failed to disable auto-unlock for volume %2.\r\n
0x0000600f | Auto-unlocking failed for volume %2.\r\n
0x00006010 | An attempt to automatically restart conversion on volume %2 failed.\r\n
0x00006011 | Metadata write: Volume %2 returning errors while trying to modify metadata. If failures continue, decrypt volume.\r\n
0x00006012 | Metadata rebuild: An attempt to write a copy of metadata on volume %2 failed and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x00006013 | Volume %2 contains bad clusters. These clusters will be skipped during conversion.\r\n
0x00006014 | No key file was found for Volume %2 during restart.\r\n
0x00006015 | A corrupt key file was encountered for Volume %2 during restart.\r\n
0x00006016 | No volume master key was retrieved in a key file during restart.\r\n
0x00006017 | The TPM was not enabled during restart.\r\n
0x00006018 | The SRK was found to be invalid during restart.\r\n
0x00006019 | The PCRs did not match during restart.\r\n
0x0000601a | No volume master key was retrieved from a key file during restart.\r\n
0x0000601b | A boot application hash did not match expected value during restart.\r\n
0x0000601c | The boot configuration options did not match expected values during restart.\r\n
0x0000601d | No volume master key was retrieved from a PIN during restart.\r\n
0x0000601e | No volume master key was retrieved from a recovery password during restart.\r\n
0x0000601f | A valid key was found during the last restart.\r\n
0x00006020 | An unexpected error was encountered attempting to retrieve the volume master key during restart.\r\n
0x00006021 | A key was not available from required sources during restart.\r\n
0x00006022 | Metadata commit: Not all copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006023 | Metadata commit: No copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006024 | Metadata commit: Metadata update could not be flushed.\r\n
0x00006025 | Metadata commit: An attempt to verify metadata update on volume %2 failed at read. If failures continue, decrypt volume.\r\n
0x00006026 | Metadata commit: Update verification of metadata on volume %2 failed. If failures continue, decrypt volume.\r\n
0x00006027 | Metadata initial read: Primary metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006028 | Metadata initial read: Failover metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006029 | Metadata initial read: Failover metadata record on volume %2 used. If failures continue, decrypt volume.\r\n
0x0000602a | Metadata check: Metadata record on volume %2 could not be read and has been marked for rebuild. If failures continue, decrypt volume.\r\n
0x0000602b | Metadata rebuild: An attempt build a new set of metadata on %2 failed at commit and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x0000602c | Encrypted volume check: Volume information on %2 cannot be read.\r\n
0x0000602d | Initial state check: Rolling volume conversion transaction on %2.\r\n
0x0000602e | BIOS/TCG Memory Overwrite Control: Error finding TPM driver.\r\n
0x0000602f | BIOS/TCG Memory Overwrite Control: Error registering TPM device interface.\r\n
0x00006030 | BIOS/TCG Memory Overwrite Control: Error changing value.\r\n
0x00006031 | A valid BitLocker key was found during the last restart.\r\n
0x00006032 | The auto-unlock master key was not available from the operating system volume.  Retry the operation via the BitLocker WMI interface.\r\n
0x00006033 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00006034 | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00006035 | The system firmware failed to enable overwriting of system memory on restart. The firmware should be upgraded.\r\n
0x00006036 | Bootmgr failed to find a BitLocker key file for Volume %2.\r\n
0x00006037 | Bootmgr detected corruption in the BitLocker key file for Volume %2.\r\n
0x00006038 | Bootmgr failed to obtain the BitLocker volume master key from the key file contents.\r\n
0x00006039 | Bootmgr determined that the TPM is disabled.\r\n
0x0000603a | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000603b | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000603c | Bootmgr failed to obtain the BitLocker volume master key from the TPM.\r\n
0x0000603d | A boot application hash did not match the expected value during restart.\r\n
0x0000603e | Bootmgr failed to obtain the BitLocker volume master key from the TPM + PIN.\r\n
0x0000603f | Bootmgr failed to obtain the BitLocker volume master key from the recovery password.\r\n
0x00006040 | A valid BitLocker key was found during the last restart.\r\n
0x00006041 | An unexpected error was encountered attempting to retrieve the BitLocker volume master key during restart.\r\n
0x00006042 | An internal BitLocker self-test failed for drive %2. BitLocker cannot continue encrypting data. Contact your system administrator.\r\n
0x00006043 | Bootmgr failed to obtain the BitLocker volume master key from the TPM + enhanced PIN.\r\n
0x00006044 | An internal BitLocker self-test failed for drive %2 when switching from raw mode to filtering mode. BitLocker cannot continue encrypting data on this drive. Contact your system administrator.\r\n
0x00006045 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector.\r\n
0x00006046 | Encryption of the used space on volume %2 started.\r\n
0x00006047 | Encryption of the used space on volume %2 stopped.\r\n
0x00006048 | Encryption of the used space on volume %2 completed.\r\n
0x00006049 | Wiping of free space on volume %2 started.\r\n
0x0000604a | Wiping of free space on volume %2 stopped.\r\n
0x0000604b | Wiping of free space on volume %2 completed.\r\n
0x0000604c | A recovery password was used to start Windows.%nProtector ID: %5.\r\n
0x0000604d | Bootmgr failed to obtain the BitLocker volume master key from the password.\r\n
0x0000604e | A recovery key was used to start Windows.%nProtector ID: %5.\r\n
0x0000604f | The BitLocker driver has started a self-healing operation on the metadata of volume %2.\r\n
0x00006050 | The BitLocker driver has successfully completed a self-healing operation on the metadata of volume %2.\r\n
0x00006051 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00006052 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x00006053 | Device Lock was triggered due to too many incorrect password attempts.\r\n
0x00006054 | BitLocker encryption on write started for volume %2.\r\n
0x00006055 | BitLocker free space sweep started for volume %2.\r\n
0x00006056 | BitLocker free space sweep stopped for volume %2.\r\n
0x00006057 | BitLocker free space sweep completed for volume %2.\r\n
0x00006058 | BitLocker finalization sweep started for volume %2.\r\n
0x00006059 | BitLocker finalization sweep paused for volume %2.\r\n
0x0000605a | BitLocker finalization sweep resumed for volume %2.\r\n
0x0000605b | BitLocker finalization sweep completed for volume %2.\r\n
0x0000605c | BitLocker encryption on write failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605d | BitLocker finalization sweep failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605e | Disk containing volume %2 is employing non-volatile caching software which does not support control over its caching policies. This may temporarily impact BitLocker's ability to fully secure your data.\r\n
0x0000605f | Disk containing volume %2 is employing non-volatile caching software which is experiencing problems. This may temporarily impact BitLocker's ability to fully secure your data. Contact disk manufacturer for an updated software.\r\n
0x00006060 | Device Lock was triggered due to Device Lockout state validation failure.\r\n
0x00006061 | Drive %2 is no longer automatically managed by device encryption.\r\n
0x00006062 | Drive %2 is now automatically managed by device encryption.\r\n
0x00006063 | WIM hash generation paused for volume %2.\r\n
0x00006064 | WIM hash generation resumed for volume %2.\r\n
0x00006065 | WIM hash generation completed for volume %2.\r\n
0x00006066 | WIM hash generation failed for volume %2.\r\n
0x00006067 | WIM hashes will be deleted for volume %2.\r\n
0x00006068 | Bootmgr failed to unseal VMK using the TPM\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BitLocker-Driver\r\n
0x90000002 | System\r\n
0x91000001 | Microsoft-Windows-BitLocker-Driver-Performance\r\n

### 10.0.15063.0, 10.0.16299.15, 10.0.17134.441, 10.0.17763.1

Message identifier | Message string
--- | ---
0x00006001 | Encryption of volume %2 started.\r\n
0x00006002 | Encryption of volume %2 stopped.\r\n
0x00006003 | Encryption of volume %2 completed.\r\n
0x00006004 | Decryption of volume %2 started.\r\n
0x00006005 | Decryption of volume %2 stopped.\r\n
0x00006006 | Decryption of volume %2 completed.\r\n
0x00006007 | Conversion worker thread for volume %2 was started.\r\n
0x00006008 | Conversion worker thread for volume %2 was temporarily stopped.\r\n
0x00006009 | Auto-unlock enabled for volume %2.\r\n
0x0000600a | An error was encountered converting volume %2.\r\n
0x0000600b | Auto-unlock disabled for volume %2.\r\n
0x0000600c | The conversion operation on volume %2 encountered a bad sector error. Please validate the data on this volume.\r\n
0x0000600d | Failed to enable auto-unlock for volume %2.\r\n
0x0000600e | Failed to disable auto-unlock for volume %2.\r\n
0x0000600f | Auto-unlocking failed for volume %2.\r\n
0x00006010 | An attempt to automatically restart conversion on volume %2 failed.\r\n
0x00006011 | Metadata write: Volume %2 returning errors while trying to modify metadata. If failures continue, decrypt volume.\r\n
0x00006012 | Metadata rebuild: An attempt to write a copy of metadata on volume %2 failed and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x00006013 | Volume %2 contains bad clusters. These clusters will be skipped during conversion.\r\n
0x00006014 | No key file was found for Volume %2 during restart.\r\n
0x00006015 | A corrupt key file was encountered for Volume %2 during restart.\r\n
0x00006016 | No volume master key was retrieved in a key file during restart.\r\n
0x00006017 | The TPM was not enabled during restart.\r\n
0x00006018 | The SRK was found to be invalid during restart.\r\n
0x00006019 | The PCRs did not match during restart.\r\n
0x0000601a | No volume master key was retrieved from a key file during restart.\r\n
0x0000601b | A boot application hash did not match expected value during restart.\r\n
0x0000601c | The boot configuration options did not match expected values during restart.\r\n
0x0000601d | No volume master key was retrieved from a PIN during restart.\r\n
0x0000601e | No volume master key was retrieved from a recovery password during restart.\r\n
0x0000601f | A valid key was found during the last restart.\r\n
0x00006020 | An unexpected error was encountered attempting to retrieve the volume master key during restart.\r\n
0x00006021 | A key was not available from required sources during restart.\r\n
0x00006022 | Metadata commit: Not all copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006023 | Metadata commit: No copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006024 | Metadata commit: Metadata update could not be flushed.\r\n
0x00006025 | Metadata commit: An attempt to verify metadata update on volume %2 failed at read. If failures continue, decrypt volume.\r\n
0x00006026 | Metadata commit: Update verification of metadata on volume %2 failed. If failures continue, decrypt volume.\r\n
0x00006027 | Metadata initial read: Primary metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006028 | Metadata initial read: Failover metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006029 | Metadata initial read: Failover metadata record on volume %2 used. If failures continue, decrypt volume.\r\n
0x0000602a | Metadata check: Metadata record on volume %2 could not be read and has been marked for rebuild. If failures continue, decrypt volume.\r\n
0x0000602b | Metadata rebuild: An attempt build a new set of metadata on %2 failed at commit and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x0000602c | Encrypted volume check: Volume information on %2 cannot be read.\r\n
0x0000602d | Initial state check: Rolling volume conversion transaction on %2.\r\n
0x0000602e | BIOS/TCG Memory Overwrite Control: Error finding TPM driver.\r\n
0x0000602f | BIOS/TCG Memory Overwrite Control: Error registering TPM device interface.\r\n
0x00006030 | BIOS/TCG Memory Overwrite Control: Error changing value.\r\n
0x00006031 | A valid BitLocker key was found during the last restart.\r\n
0x00006032 | The auto-unlock master key was not available from the operating system volume.  Retry the operation via the BitLocker WMI interface.\r\n
0x00006033 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00006034 | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00006035 | The system firmware failed to enable overwriting of system memory on restart. The firmware should be upgraded.\r\n
0x00006036 | Bootmgr failed to find a BitLocker key file for Volume %2.\r\n
0x00006037 | Bootmgr detected corruption in the BitLocker key file for Volume %2.\r\n
0x00006038 | Bootmgr failed to obtain the BitLocker volume master key from the key file contents.\r\n
0x00006039 | Bootmgr determined that the TPM is disabled.\r\n
0x0000603a | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000603b | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000603c | Bootmgr failed to obtain the BitLocker volume master key from the TPM.\r\n
0x0000603d | A boot application hash did not match the expected value during restart.\r\n
0x0000603e | Bootmgr failed to obtain the BitLocker volume master key from the TPM + PIN.\r\n
0x0000603f | Bootmgr failed to obtain the BitLocker volume master key from the recovery password.\r\n
0x00006040 | A valid BitLocker key was found during the last restart.\r\n
0x00006041 | An unexpected error was encountered attempting to retrieve the BitLocker volume master key during restart.\r\n
0x00006042 | An internal BitLocker self-test failed for drive %2. BitLocker cannot continue encrypting data. Contact your system administrator.\r\n
0x00006043 | Bootmgr failed to obtain the BitLocker volume master key from the TPM + enhanced PIN.\r\n
0x00006044 | An internal BitLocker self-test failed for drive %2 when switching from raw mode to filtering mode. BitLocker cannot continue encrypting data on this drive. Contact your system administrator.\r\n
0x00006045 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector.\r\n
0x00006046 | Encryption of the used space on volume %2 started.\r\n
0x00006047 | Encryption of the used space on volume %2 stopped.\r\n
0x00006048 | Encryption of the used space on volume %2 completed.\r\n
0x00006049 | Wiping of free space on volume %2 started.\r\n
0x0000604a | Wiping of free space on volume %2 stopped.\r\n
0x0000604b | Wiping of free space on volume %2 completed.\r\n
0x0000604c | A recovery password was used to start Windows.%nProtector ID: %5.\r\n
0x0000604d | Bootmgr failed to obtain the BitLocker volume master key from the password.\r\n
0x0000604e | A recovery key was used to start Windows.%nProtector ID: %5.\r\n
0x0000604f | The BitLocker driver has started a self-healing operation on the metadata of volume %2.\r\n
0x00006050 | The BitLocker driver has successfully completed a self-healing operation on the metadata of volume %2.\r\n
0x00006051 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00006052 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x00006053 | Device Lock was triggered due to too many incorrect password attempts.\r\n
0x00006054 | BitLocker encryption on write started for volume %2.\r\n
0x00006055 | BitLocker free space sweep started for volume %2.\r\n
0x00006056 | BitLocker free space sweep stopped for volume %2.\r\n
0x00006057 | BitLocker free space sweep completed for volume %2.\r\n
0x00006058 | BitLocker finalization sweep started for volume %2.\r\n
0x00006059 | BitLocker finalization sweep paused for volume %2.\r\n
0x0000605a | BitLocker finalization sweep resumed for volume %2.\r\n
0x0000605b | BitLocker finalization sweep completed for volume %2.\r\n
0x0000605c | BitLocker encryption on write failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605d | BitLocker finalization sweep failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605e | Disk containing volume %2 is employing non-volatile caching software which does not support control over its caching policies. This may temporarily impact BitLocker's ability to fully secure your data.\r\n
0x0000605f | Disk containing volume %2 is employing non-volatile caching software which is experiencing problems. This may temporarily impact BitLocker's ability to fully secure your data. Contact disk manufacturer for an updated software.\r\n
0x00006060 | Device Lock was triggered due to Device Lockout state validation failure.\r\n
0x00006061 | Drive %2 is no longer automatically managed by device encryption.\r\n
0x00006062 | Drive %2 is now automatically managed by device encryption.\r\n
0x00006063 | WIM hash generation paused for volume %2.\r\n
0x00006064 | WIM hash generation resumed for volume %2.\r\n
0x00006065 | WIM hash generation completed for volume %2.\r\n
0x00006066 | WIM hash generation failed for volume %2.\r\n
0x00006067 | WIM hashes will be deleted for volume %2.\r\n
0x00006068 | Bootmgr failed to unseal VMK using the TPM\r\n
0x00006069 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to acquire protocol handle.\r\n
0x0000606a | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to get IP address.\r\n
0x0000606b | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to create request.\r\n
0x0000606c | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to send request.\r\n
0x0000606d | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: invalid response.\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BitLocker-Driver\r\n
0x90000002 | System\r\n
0x91000001 | Microsoft-Windows-BitLocker-Driver-Performance\r\n

### 10.0.18362.1, 10.0.18362.267, 10.0.19041.1, 10.0.19041.546

Message identifier | Message string
--- | ---
0x00006001 | Encryption of volume %2 started.\r\n
0x00006002 | Encryption of volume %2 stopped.\r\n
0x00006003 | Encryption of volume %2 completed.\r\n
0x00006004 | Decryption of volume %2 started.\r\n
0x00006005 | Decryption of volume %2 stopped.\r\n
0x00006006 | Decryption of volume %2 completed.\r\n
0x00006007 | Conversion worker thread for volume %2 was started.\r\n
0x00006008 | Conversion worker thread for volume %2 was temporarily stopped.\r\n
0x00006009 | Auto-unlock enabled for volume %2.\r\n
0x0000600a | An error was encountered converting volume %2.\r\n
0x0000600b | Auto-unlock disabled for volume %2.\r\n
0x0000600c | The conversion operation on volume %2 encountered a bad sector error. Please validate the data on this volume.\r\n
0x0000600d | Failed to enable auto-unlock for volume %2.\r\n
0x0000600e | Failed to disable auto-unlock for volume %2.\r\n
0x0000600f | Auto-unlocking failed for volume %2.\r\n
0x00006010 | An attempt to automatically restart conversion on volume %2 failed.\r\n
0x00006011 | Metadata write: Volume %2 returning errors while trying to modify metadata. If failures continue, decrypt volume.\r\n
0x00006012 | Metadata rebuild: An attempt to write a copy of metadata on volume %2 failed and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x00006013 | Volume %2 contains bad clusters. These clusters will be skipped during conversion.\r\n
0x00006014 | No key file was found for Volume %2 during restart.\r\n
0x00006015 | A corrupt key file was encountered for Volume %2 during restart.\r\n
0x00006016 | No volume master key was retrieved in a key file during restart.\r\n
0x00006017 | The TPM was not enabled during restart.\r\n
0x00006018 | The SRK was found to be invalid during restart.\r\n
0x00006019 | The PCRs did not match during restart.\r\n
0x0000601a | No volume master key was retrieved from a key file during restart.\r\n
0x0000601b | A boot application hash did not match expected value during restart.\r\n
0x0000601c | The boot configuration options did not match expected values during restart.\r\n
0x0000601d | No volume master key was retrieved from a PIN during restart.\r\n
0x0000601e | No volume master key was retrieved from a recovery password during restart.\r\n
0x0000601f | A valid key was found during the last restart.\r\n
0x00006020 | An unexpected error was encountered attempting to retrieve the volume master key during restart.\r\n
0x00006021 | A key was not available from required sources during restart.\r\n
0x00006022 | Metadata commit: Not all copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006023 | Metadata commit: No copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006024 | Metadata commit: Metadata update could not be flushed.\r\n
0x00006025 | Metadata commit: An attempt to verify metadata update on volume %2 failed at read. If failures continue, decrypt volume.\r\n
0x00006026 | Metadata commit: Update verification of metadata on volume %2 failed. If failures continue, decrypt volume.\r\n
0x00006027 | Metadata initial read: Primary metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006028 | Metadata initial read: Failover metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006029 | Metadata initial read: Failover metadata record on volume %2 used. If failures continue, decrypt volume.\r\n
0x0000602a | Metadata check: Metadata record on volume %2 could not be read and has been marked for rebuild. If failures continue, decrypt volume.\r\n
0x0000602b | Metadata rebuild: An attempt build a new set of metadata on %2 failed at commit and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x0000602c | Encrypted volume check: Volume information on %2 cannot be read.\r\n
0x0000602d | Initial state check: Rolling volume conversion transaction on %2.\r\n
0x0000602e | BIOS/TCG Memory Overwrite Control: Error finding TPM driver.\r\n
0x0000602f | BIOS/TCG Memory Overwrite Control: Error registering TPM device interface.\r\n
0x00006030 | BIOS/TCG Memory Overwrite Control: Error changing value.\r\n
0x00006031 | A valid BitLocker key was found during the last restart.\r\n
0x00006032 | The auto-unlock master key was not available from the operating system volume.  Retry the operation via the BitLocker WMI interface.\r\n
0x00006033 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00006034 | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00006035 | The system firmware failed to enable overwriting of system memory on restart. The firmware should be upgraded.\r\n
0x00006036 | Bootmgr failed to find a BitLocker key file for Volume %2.\r\n
0x00006037 | Bootmgr detected corruption in the BitLocker key file for Volume %2.\r\n
0x00006038 | Bootmgr failed to obtain the BitLocker volume master key from the key file contents.\r\n
0x00006039 | Bootmgr determined that the TPM is disabled.\r\n
0x0000603a | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000603b | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000603c | Bootmgr failed to obtain the BitLocker volume master key from the TPM.\r\n
0x0000603d | A boot application hash did not match the expected value during restart.\r\n
0x0000603e | Bootmgr failed to obtain the BitLocker volume master key from the TPM + PIN.\r\n
0x0000603f | Bootmgr failed to obtain the BitLocker volume master key from the recovery password.\r\n
0x00006040 | A valid BitLocker key was found during the last restart.\r\n
0x00006041 | An unexpected error was encountered attempting to retrieve the BitLocker volume master key during restart.\r\n
0x00006042 | An internal BitLocker self-test failed for drive %2. BitLocker cannot continue encrypting data. Contact your system administrator.\r\n
0x00006043 | Bootmgr failed to obtain the BitLocker volume master key from the TPM + enhanced PIN.\r\n
0x00006044 | An internal BitLocker self-test failed for drive %2 when switching from raw mode to filtering mode. BitLocker cannot continue encrypting data on this drive. Contact your system administrator.\r\n
0x00006045 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector.\r\n
0x00006046 | Encryption of the used space on volume %2 started.\r\n
0x00006047 | Encryption of the used space on volume %2 stopped.\r\n
0x00006048 | Encryption of the used space on volume %2 completed.\r\n
0x00006049 | Wiping of free space on volume %2 started.\r\n
0x0000604a | Wiping of free space on volume %2 stopped.\r\n
0x0000604b | Wiping of free space on volume %2 completed.\r\n
0x0000604c | A recovery password was used to start Windows.%nProtector ID: %5.\r\n
0x0000604d | Bootmgr failed to obtain the BitLocker volume master key from the password.\r\n
0x0000604e | A recovery key was used to start Windows.%nProtector ID: %5.\r\n
0x0000604f | The BitLocker driver has started a self-healing operation on the metadata of volume %2.\r\n
0x00006050 | The BitLocker driver has successfully completed a self-healing operation on the metadata of volume %2.\r\n
0x00006051 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00006052 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x00006053 | Device Lock was triggered due to too many incorrect password attempts.\r\n
0x00006054 | BitLocker encryption on write started for volume %2.\r\n
0x00006055 | BitLocker free space sweep started for volume %2.\r\n
0x00006056 | BitLocker free space sweep stopped for volume %2.\r\n
0x00006057 | BitLocker free space sweep completed for volume %2.\r\n
0x00006058 | BitLocker finalization sweep started for volume %2.\r\n
0x00006059 | BitLocker finalization sweep paused for volume %2.\r\n
0x0000605a | BitLocker finalization sweep resumed for volume %2.\r\n
0x0000605b | BitLocker finalization sweep completed for volume %2.\r\n
0x0000605c | BitLocker encryption on write failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605d | BitLocker finalization sweep failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605e | Disk containing volume %2 is employing non-volatile caching software which does not support control over its caching policies. This may temporarily impact BitLocker's ability to fully secure your data.\r\n
0x0000605f | Disk containing volume %2 is employing non-volatile caching software which is experiencing problems. This may temporarily impact BitLocker's ability to fully secure your data. Contact disk manufacturer for an updated software.\r\n
0x00006060 | Device Lock was triggered due to Device Lockout state validation failure.\r\n
0x00006061 | Drive %2 is no longer automatically managed by device encryption.\r\n
0x00006062 | Drive %2 is now automatically managed by device encryption.\r\n
0x00006063 | WIM hash generation paused for volume %2.\r\n
0x00006064 | WIM hash generation resumed for volume %2.\r\n
0x00006065 | WIM hash generation completed for volume %2.\r\n
0x00006066 | WIM hash generation failed for volume %2.\r\n
0x00006067 | WIM hashes will be deleted for volume %2.\r\n
0x00006068 | Bootmgr failed to unseal VMK using the TPM\r\n
0x00006069 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to acquire protocol handle.\r\n
0x0000606a | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to get IP address.\r\n
0x0000606b | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to create request.\r\n
0x0000606c | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to send request.\r\n
0x0000606d | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: invalid response.\r\n
0x0000606e | Bootmgr failed to obtain the BitLocker volume master key from the network boot protector.\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BitLocker-Driver\r\n
0x90000002 | System\r\n
0x91000001 | Microsoft-Windows-BitLocker-Driver-Performance\r\n

### 10.0.22000.132

Message identifier | Message string
--- | ---
0x00006001 | Encryption of volume %2 started.\r\n
0x00006002 | Encryption of volume %2 stopped.\r\n
0x00006003 | Encryption of volume %2 completed.\r\n
0x00006004 | Decryption of volume %2 started.\r\n
0x00006005 | Decryption of volume %2 stopped.\r\n
0x00006006 | Decryption of volume %2 completed.\r\n
0x00006007 | Conversion worker thread for volume %2 was started.\r\n
0x00006008 | Conversion worker thread for volume %2 was temporarily stopped.\r\n
0x00006009 | Auto-unlock enabled for volume %2.\r\n
0x0000600a | An error was encountered converting volume %2.\r\n
0x0000600b | Auto-unlock disabled for volume %2.\r\n
0x0000600c | The conversion operation on volume %2 encountered a bad sector error. Please validate the data on this volume.\r\n
0x0000600d | Failed to enable auto-unlock for volume %2.\r\n
0x0000600e | Failed to disable auto-unlock for volume %2.\r\n
0x0000600f | Auto-unlocking failed for volume %2.\r\n
0x00006010 | An attempt to automatically restart conversion on volume %2 failed.\r\n
0x00006011 | Metadata write: Volume %2 returning errors while trying to modify metadata. If failures continue, decrypt volume.\r\n
0x00006012 | Metadata rebuild: An attempt to write a copy of metadata on volume %2 failed and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x00006013 | Volume %2 contains bad clusters. These clusters will be skipped during conversion.\r\n
0x00006014 | No key file was found for Volume %2 during restart.\r\n
0x00006015 | A corrupt key file was encountered for Volume %2 during restart.\r\n
0x00006016 | No volume master key was retrieved in a key file during restart.\r\n
0x00006017 | The TPM was not enabled during restart.\r\n
0x00006018 | The SRK was found to be invalid during restart.\r\n
0x00006019 | The PCRs did not match during restart.\r\n
0x0000601a | No volume master key was retrieved from a key file during restart.\r\n
0x0000601b | A boot application hash did not match expected value during restart.\r\n
0x0000601c | The boot configuration options did not match expected values during restart.\r\n
0x0000601d | No volume master key was retrieved from a PIN during restart.\r\n
0x0000601e | No volume master key was retrieved from a recovery password during restart.\r\n
0x0000601f | A valid key was found during the last restart.\r\n
0x00006020 | An unexpected error was encountered attempting to retrieve the volume master key during restart.\r\n
0x00006021 | A key was not available from required sources during restart.\r\n
0x00006022 | Metadata commit: Not all copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006023 | Metadata commit: No copies of metadata on volume %2 could be written. If failures continue, decrypt volume.\r\n
0x00006024 | Metadata commit: Metadata update could not be flushed.\r\n
0x00006025 | Metadata commit: An attempt to verify metadata update on volume %2 failed at read. If failures continue, decrypt volume.\r\n
0x00006026 | Metadata commit: Update verification of metadata on volume %2 failed. If failures continue, decrypt volume.\r\n
0x00006027 | Metadata initial read: Primary metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006028 | Metadata initial read: Failover metadata record on volume %2 could not be found. Volume needs recovery.\r\n
0x00006029 | Metadata initial read: Failover metadata record on volume %2 used. If failures continue, decrypt volume.\r\n
0x0000602a | Metadata check: Metadata record on volume %2 could not be read and has been marked for rebuild. If failures continue, decrypt volume.\r\n
0x0000602b | Metadata rebuild: An attempt build a new set of metadata on %2 failed at commit and may appear as disk corruption. If failures continue, decrypt volume.\r\n
0x0000602c | Encrypted volume check: Volume information on %2 cannot be read.\r\n
0x0000602d | Initial state check: Rolling volume conversion transaction on %2.\r\n
0x0000602e | BIOS/TCG Memory Overwrite Control: Error finding TPM driver.\r\n
0x0000602f | BIOS/TCG Memory Overwrite Control: Error registering TPM device interface.\r\n
0x00006030 | BIOS/TCG Memory Overwrite Control: Error changing value.\r\n
0x00006031 | A valid BitLocker key was found during the last restart.\r\n
0x00006032 | The auto-unlock master key was not available from the operating system volume.  Retry the operation via the BitLocker WMI interface.\r\n
0x00006033 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00006034 | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00006035 | The system firmware failed to enable overwriting of system memory on restart. The firmware should be upgraded.\r\n
0x00006036 | Bootmgr failed to find a BitLocker key file for Volume %2.\r\n
0x00006037 | Bootmgr detected corruption in the BitLocker key file for Volume %2.\r\n
0x00006038 | Bootmgr failed to obtain the BitLocker volume master key from the key file contents.\r\n
0x00006039 | Bootmgr determined that the TPM is disabled.\r\n
0x0000603a | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000603b | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000603c | Bootmgr failed to obtain the BitLocker volume master key from the TPM.\r\n
0x0000603d | A boot application hash did not match the expected value during restart.\r\n
0x0000603e | Bootmgr failed to obtain the BitLocker volume master key from the TPM + PIN.\r\n
0x0000603f | Bootmgr failed to obtain the BitLocker volume master key from the recovery password.\r\n
0x00006040 | A valid BitLocker key was found during the last restart.\r\n
0x00006041 | An unexpected error was encountered attempting to retrieve the BitLocker volume master key during restart.\r\n
0x00006042 | An internal BitLocker self-test failed for drive %2. BitLocker cannot continue encrypting data. Contact your system administrator.\r\n
0x00006043 | Bootmgr failed to obtain the BitLocker volume master key from the TPM + enhanced PIN.\r\n
0x00006044 | An internal BitLocker self-test failed for drive %2 when switching from raw mode to filtering mode. BitLocker cannot continue encrypting data on this drive. Contact your system administrator.\r\n
0x00006045 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector.\r\n
0x00006046 | Encryption of the used space on volume %2 started.\r\n
0x00006047 | Encryption of the used space on volume %2 stopped.\r\n
0x00006048 | Encryption of the used space on volume %2 completed.\r\n
0x00006049 | Wiping of free space on volume %2 started.\r\n
0x0000604a | Wiping of free space on volume %2 stopped.\r\n
0x0000604b | Wiping of free space on volume %2 completed.\r\n
0x0000604c | A recovery password was used to start Windows.%nProtector ID: %5.\r\n
0x0000604d | Bootmgr failed to obtain the BitLocker volume master key from the password.\r\n
0x0000604e | A recovery key was used to start Windows.%nProtector ID: %5.\r\n
0x0000604f | The BitLocker driver has started a self-healing operation on the metadata of volume %2.\r\n
0x00006050 | The BitLocker driver has successfully completed a self-healing operation on the metadata of volume %2.\r\n
0x00006051 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00006052 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x00006053 | Device Lock was triggered due to too many incorrect password attempts.\r\n
0x00006054 | BitLocker encryption on write started for volume %2.\r\n
0x00006055 | BitLocker free space sweep started for volume %2.\r\n
0x00006056 | BitLocker free space sweep stopped for volume %2.\r\n
0x00006057 | BitLocker free space sweep completed for volume %2.\r\n
0x00006058 | BitLocker finalization sweep started for volume %2.\r\n
0x00006059 | BitLocker finalization sweep paused for volume %2.\r\n
0x0000605a | BitLocker finalization sweep resumed for volume %2.\r\n
0x0000605b | BitLocker finalization sweep completed for volume %2.\r\n
0x0000605c | BitLocker encryption on write failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605d | BitLocker finalization sweep failed for volume %2 due to disk I/O error. Check the disk for bad sectors.\r\n
0x0000605e | Disk containing volume %2 is employing non-volatile caching software which does not support control over its caching policies. This may temporarily impact BitLocker's ability to fully secure your data.\r\n
0x0000605f | Disk containing volume %2 is employing non-volatile caching software which is experiencing problems. This may temporarily impact BitLocker's ability to fully secure your data. Contact disk manufacturer for an updated software.\r\n
0x00006060 | Device Lock was triggered due to Device Lockout state validation failure.\r\n
0x00006061 | Drive %2 is no longer automatically managed by device encryption.\r\n
0x00006062 | Drive %2 is now automatically managed by device encryption.\r\n
0x00006063 | WIM hash generation paused for volume %2.\r\n
0x00006064 | WIM hash generation resumed for volume %2.\r\n
0x00006065 | WIM hash generation completed for volume %2.\r\n
0x00006066 | WIM hash generation failed for volume %2.\r\n
0x00006067 | WIM hashes will be deleted for volume %2.\r\n
0x00006068 | Bootmgr failed to unseal VMK using the TPM\r\n
0x00006069 | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to acquire protocol handle.\r\n
0x0000606a | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to get IP address.\r\n
0x0000606b | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to create request.\r\n
0x0000606c | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: failed to send request.\r\n
0x0000606d | Bootmgr failed to obtain the BitLocker volume master key from the network key protector: invalid response.\r\n
0x0000606e | Bootmgr failed to obtain the BitLocker volume master key from the network boot protector.\r\n
0x0000606f | BitLocker timed out attempting to enumerate bands during volume discovery on this hardware encrypting drive.\r\n
0x00006070 | Failed to read metadata from logical copy. Volume: %2, Start Offset: %3, Read Length: %4, Copy: %5, Number of Copies:%6\r\n
0x00006071 | Attempted to read metadata from logical copy. Volume: %2, Start Offset: %3, Read Length: %4, Copy: %5, Number of Copies:%6\r\n
0x00006072 | Attempted to fix metadata logical copies. Volume: %2, ManageFlags: %3\r\n
0x00006073 | Failed to verify metadata logical copy against Primary. Volume: %2, Start Offset: %3, Read Length: %4, Copy: %5, Number of Copies:%6\r\n
0x00006074 | Failed to verify metadata file against Primary copy. Volume: %2, Start Offset: %3, Read Length: %4, Copy: %5, Number of Copies:%6\r\n
0x00006075 | Failed to register metadata check worker. Volume: %2\r\n
0x00006076 | Metadata check worker started. Volume: %2\r\n
0x00006077 | Metadata check worker completed. Volume: %2\r\n
0x00006078 | Successfully created metadata file. Volume: %2, Offset: %3, Read Length: %4, Copy: %5, Number of Copies: %6, TpAllocationSize: %7\r\n
0x00006079 | Failed to read a valid metadata copy. Volume: %2, Start Offset: %3, Index: %5\r\n
0x0000607a | Failed to fix metadata logical copy. Volume: %2, Start Offset: %3,  Read Length: %4, Source Index: %5, Number of Copies: %6, TpAllocationSize: %7\r\n
0x0000607b | Attempted to check metadata logical copies. Volume: %2, ManageFlags: %3\r\n
0x0000607c | Successfully fixed metadata logical copy. Volume: %2, Start Offset: %3,  Read Length: %4, Source Index: %5, Number of Copies: %6, TpAllocationSize: %7\r\n
0x31000000 | Info\r\n
0x31000001 | Start\r\n
0x31000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BitLocker-Driver\r\n
0x90000002 | System\r\n
0x91000001 | Microsoft-Windows-BitLocker-Driver-Performance\r\n
