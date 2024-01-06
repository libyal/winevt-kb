## fveapi.dll

Path: %SystemRoot%\system32\fveapi.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %1%nProtector GUID: %2%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %1%nProtector GUID: %2%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported. To enable this functionality, upgrade your operating system to Windows 7 Enterprise. %nErrorcode: %1%nVolume GUID: %2\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0xb0000300 | BitLocker encryption was started for volume %3.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0001000 | Device Encryption could not be enabled.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without TPM-based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0x90000004 | Operational\r\n
0xb0000300 | BitLocker encryption was started for volume %3.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0000348 | A trusted WIM file has been added for volume %3.%nThe SHA-256 hash of the WIM file is: %5\r\n
0xb0000349 | BitLocker was unable to update a key for volume %3 due to the following error: %4\r\n
0xb000034a | BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034b | BitLocker was suspended from within the Windows Recovery Environment.%nSuspend time: %2\r\n
0xb000034c | BitLocker was unable to recover from device lock in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb0001000 | Device Encryption could not be initialized.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without hardware based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xb0001014 | Device Encryption initialization for volume %3 start.\r\n
0xb0001015 | Device Encryption initialization for volume %3 stop.\r\n
0xb0001016 | Volume %3 could not be initialized for Device Encryption.%n%nError: %4.\r\n
0xb0001017 | Windows RE is not correctly configured for device encryption. Make sure that Windows RE is enabled and is not installed on the OS drive.\r\n
0xb0001018 | The TPM is not provisioned for device encryption. To set up the TPM use the TPM management console (Start->tpm.msc) and use the action to make the TPM ready.\r\n
0xb0001019 | Sign in with a Microsoft account to finish provisioning device encryption.\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0x90000004 | Operational\r\n
0xb0000300 | BitLocker encryption was started for volume %3.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0000348 | A trusted WIM file has been added for volume %3.%nThe SHA-256 hash of the WIM file is: %5\r\n
0xb0000349 | BitLocker was unable to update a key for volume %3 due to the following error: %4\r\n
0xb000034a | BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034b | BitLocker was suspended from within the Windows Recovery Environment.%nSuspend time: %2\r\n
0xb000034c | BitLocker was unable to recover from device lock in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034d | BitLocker Drive Encryption recovery information for volume %1 was backed up successfully to your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xb000034e | Failed to backup BitLocker Drive Encryption recovery information for volume %1 to your Azure AD.%nTraceId: %2%n%nError: %3\r\n
0xb000034f | Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0001000 | Device Encryption could not be initialized.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without hardware based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xb0001014 | Device Encryption initialization for volume %3 start.\r\n
0xb0001015 | Device Encryption initialization for volume %3 stop.\r\n
0xb0001016 | Volume %3 could not be initialized for Device Encryption.%n%nError: %4.\r\n
0xb0001017 | Windows RE is not correctly configured for device encryption. Make sure that Windows RE is enabled and is not installed on the OS drive.\r\n
0xb0001018 | The TPM is not provisioned for device encryption. To set up the TPM use the TPM management console (Start->tpm.msc) and use the action to make the TPM ready.\r\n
0xb0001019 | Sign in with a Microsoft account to finish provisioning device encryption.\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0x90000004 | Operational\r\n
0xb0000300 | BitLocker encryption was started for volume %3.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0000348 | A trusted WIM file has been added for volume %3.%nThe SHA-256 hash of the WIM file is: %5\r\n
0xb0000349 | BitLocker was unable to update a key for volume %3 due to the following error: %4\r\n
0xb000034a | BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034b | BitLocker was suspended from within the Windows Recovery Environment.%nSuspend time: %2\r\n
0xb000034c | BitLocker was unable to recover from device lock in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034d | BitLocker Drive Encryption recovery information for volume %1 was backed up successfully to your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xb000034e | Failed to backup BitLocker Drive Encryption recovery information for volume %1 to your Azure AD.%nTraceId: %2%n%nError: %3\r\n
0xb000034f | Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000350 | Failed to update BCD store with the Recovery URL for OS volume.%n%nError: %1\r\n
0xb0000351 | Failed to set the TPM dictionary attack parameters to the legacy behavior.%n%nError: %1.\r\n
0xb0000352 | Successfully set the TPM dictionary attack parameters to the legacy behavior.\r\n
0xb0001000 | Device Encryption could not be initialized.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without hardware based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xb0001014 | Device Encryption initialization for volume %3 start.\r\n
0xb0001015 | Device Encryption initialization for volume %3 stop.\r\n
0xb0001016 | Volume %3 could not be initialized for Device Encryption.%n%nError: %4.\r\n
0xb0001017 | Windows RE is not correctly configured for device encryption. Make sure that Windows RE is enabled and is not installed on the OS drive.\r\n
0xb0001018 | The TPM is not provisioned for device encryption. To set up the TPM use the TPM management console (Start->tpm.msc) and use the action to make the TPM ready.\r\n
0xb0001019 | Sign in with a Microsoft account to finish provisioning device encryption.\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0x90000004 | Operational\r\n
0xb0000300 | BitLocker encryption was started for volume %3.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0000348 | A trusted WIM file has been added for volume %3.%nThe SHA-256 hash of the WIM file is: %5\r\n
0xb0000349 | BitLocker was unable to update a key for volume %3 due to the following error: %4\r\n
0xb000034a | BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034b | BitLocker was suspended from within the Windows Recovery Environment.%nSuspend time: %2\r\n
0xb000034c | BitLocker was unable to recover from device lock in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034d | BitLocker Drive Encryption recovery information for volume %1 was backed up successfully to your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xb000034e | Failed to backup BitLocker Drive Encryption recovery information for volume %1 to your Azure AD.%nTraceId: %2%n%nError: %3\r\n
0xb000034f | Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000350 | Failed to update BCD store with the Recovery URL for OS volume.%n%nError: %1\r\n
0xb0000351 | Failed to set the TPM dictionary attack parameters to the legacy behavior.%n%nError: %1.\r\n
0xb0000352 | Successfully set the TPM dictionary attack parameters to the legacy behavior.\r\n
0xb0000353 | Failed to enable Silent Encryption. %n%nError: %1.\r\n
0xb0000354 | Failed to enable Silent Encryption. Device is not AAD joined. %n%nError: %1.\r\n
0xb0000355 | Failed to enable Silent Encryption. TPM is not available. %n%nError: %1.\r\n
0xb0000356 | Failed to enable Silent Encryption. WinRe is not configured. %n%nError: %1.\r\n
0xb0001000 | Device Encryption could not be initialized.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without hardware based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xb0001014 | Device Encryption initialization for volume %3 start.\r\n
0xb0001015 | Device Encryption initialization for volume %3 stop.\r\n
0xb0001016 | Volume %3 could not be initialized for Device Encryption.%n%nError: %4.\r\n
0xb0001017 | Windows RE is not correctly configured for device encryption. Make sure that Windows RE is enabled and is not installed on the OS drive.\r\n
0xb0001018 | The TPM is not provisioned for device encryption. To set up the TPM use the TPM management console (Start->tpm.msc) and use the action to make the TPM ready.\r\n
0xb0001019 | Sign in with a Microsoft account to finish provisioning device encryption.\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n

### 10.0.17763.1

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0x90000004 | Operational\r\n
0xb0000300 | BitLocker encryption was started for volume %3 using %4 algorithm.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted using %4 algorithm.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3 using %4 algorithm.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0000348 | A trusted WIM file has been added for volume %3.%nThe SHA-256 hash of the WIM file is: %5\r\n
0xb0000349 | BitLocker was unable to update a key for volume %3 due to the following error: %4\r\n
0xb000034a | BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034b | BitLocker was suspended from within the Windows Recovery Environment.%nSuspend time: %2\r\n
0xb000034c | BitLocker was unable to recover from device lock in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034d | BitLocker Drive Encryption recovery information for volume %1 was backed up successfully to your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xb000034e | Failed to backup BitLocker Drive Encryption recovery information for volume %1 to your Azure AD.%nTraceId: %2%n%nError: %3\r\n
0xb000034f | Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000350 | Failed to update BCD store with the Recovery URL for OS volume.%n%nError: %1\r\n
0xb0000351 | Failed to set the TPM dictionary attack parameters to the legacy behavior.%n%nError: %1.\r\n
0xb0000352 | Successfully set the TPM dictionary attack parameters to the legacy behavior.\r\n
0xb0000353 | Failed to enable Silent Encryption. %n%nError: %1.\r\n
0xb0000354 | Failed to enable Silent Encryption. Device is not AAD joined. %n%nError: %1.\r\n
0xb0000355 | Failed to enable Silent Encryption. TPM is not available. %n%nError: %1.\r\n
0xb0000356 | Failed to enable Silent Encryption. WinRe is not configured. %n%nError: %1.\r\n
0xb0001000 | Device Encryption could not be initialized.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without hardware based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xb0001014 | Device Encryption initialization for volume %3 start.\r\n
0xb0001015 | Device Encryption initialization for volume %3 stop.\r\n
0xb0001016 | Volume %3 could not be initialized for Device Encryption.%n%nError: %4.\r\n
0xb0001017 | Windows RE is not correctly configured for device encryption. Make sure that Windows RE is enabled and is not installed on the OS drive.\r\n
0xb0001018 | The TPM is not provisioned for device encryption. To set up the TPM use the TPM management console (Start->tpm.msc) and use the action to make the TPM ready.\r\n
0xb0001019 | Sign in with a Microsoft account to finish provisioning device encryption.\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xd0000007 | default\r\n
0xd0000008 | AES-CBC 128 with Diffuser\r\n
0xd0000009 | AES-CBC 256 with Diffuser\r\n
0xd000000a | AES-CBC 128\r\n
0xd000000b | AES-CBC 256\r\n
0xd000000c | XTS-AES 128\r\n
0xd000000d | XTS-AES 256\r\n
0xd000000e | unknown\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n

### 10.0.18362.1

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0x90000004 | Operational\r\n
0xb0000300 | BitLocker encryption was started for volume %3 using %4 algorithm.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted using %4 algorithm.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3 using %4 algorithm.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0000348 | A trusted WIM file has been added for volume %3.%nThe SHA-256 hash of the WIM file is: %5\r\n
0xb0000349 | BitLocker was unable to update a key for volume %3 due to the following error: %4\r\n
0xb000034a | BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034b | BitLocker was suspended from within the Windows Recovery Environment.%nSuspend time: %2\r\n
0xb000034c | BitLocker was unable to recover from device lock in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034d | BitLocker Drive Encryption recovery information for volume %1 was backed up successfully to your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xb000034e | Failed to backup BitLocker Drive Encryption recovery information for volume %1 to your Azure AD.%nTraceId: %2%n%nError: %3\r\n
0xb000034f | Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000350 | Failed to update BCD store with the Recovery URL for OS volume.%n%nError: %1\r\n
0xb0000351 | Failed to set the TPM dictionary attack parameters to the legacy behavior.%n%nError: %1.\r\n
0xb0000352 | Successfully set the TPM dictionary attack parameters to the legacy behavior.\r\n
0xb0000353 | Failed to enable Silent Encryption. %n%nError: %1.\r\n
0xb0000354 | Failed to enable Silent Encryption. Device is not AAD joined. %n%nError: %1.\r\n
0xb0000355 | Failed to enable Silent Encryption. TPM is not available. %n%nError: %1.\r\n
0xb0000356 | Failed to enable Silent Encryption. WinRe is not configured. %n%nError: %1.\r\n
0xb0000357 | Recovery Password Rotation initiated.\r\n
0xb0000358 | Failed to initiate the Recovery Password Rotation %n%nError:%1.\r\n
0xb0000359 | Recovery Passwords Rotation done successfully\r\n
0xb000035a | Recovery Password Rotation failed. %n%nError: %1.\r\n
0xb000035b | Recovery Password Rotation failed for Volume %2.%n%n Error:%5.Will retry again.\r\n
0xb000035c | Failed to delete recovery password from AAD for Volume %2. %n%n Error:%5. Will retry again.\r\n
0xb000035d | Failed to create Recovery Password Rotation request for the volume %2. %n%n Error:%5.\r\n
0xb000035e | Failed to Create AAD recovery Password Delete request for the volume %2. %n%n Error:%5.\r\n
0xb000035f | Failed to initiate the Recovery Password Rotation and AAD Deletion requests processing %n%nError:%1.\r\n
0xb0000360 | Recovery Passwords Rotation and AAD Deletion requests processing initiated successfully\r\n
0xb0001000 | Device Encryption could not be initialized.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without hardware based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xb0001014 | Device Encryption initialization for volume %3 start.\r\n
0xb0001015 | Device Encryption initialization for volume %3 stop.\r\n
0xb0001016 | Volume %3 could not be initialized for Device Encryption.%n%nError: %4.\r\n
0xb0001017 | Windows RE is not correctly configured for device encryption. Make sure that Windows RE is enabled and is not installed on the OS drive.\r\n
0xb0001018 | The TPM is not provisioned for device encryption. To set up the TPM use the TPM management console (Start->tpm.msc) and use the action to make the TPM ready.\r\n
0xb0001019 | Sign in with a Microsoft account to finish provisioning device encryption.\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xd0000007 | default\r\n
0xd0000008 | AES-CBC 128 with Diffuser\r\n
0xd0000009 | AES-CBC 256 with Diffuser\r\n
0xd000000a | AES-CBC 128\r\n
0xd000000b | AES-CBC 256\r\n
0xd000000c | XTS-AES 128\r\n
0xd000000d | XTS-AES 256\r\n
0xd000000e | unknown\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n

### 10.0.18362.329

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0x90000004 | Operational\r\n
0xb0000300 | BitLocker encryption was started for volume %3 using %4 algorithm.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted using %4 algorithm.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3 using %4 algorithm.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0000348 | A trusted WIM file has been added for volume %3.%nThe SHA-256 hash of the WIM file is: %5\r\n
0xb0000349 | BitLocker was unable to update a key for volume %3 due to the following error: %4\r\n
0xb000034a | BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034b | BitLocker was suspended from within the Windows Recovery Environment.%nSuspend time: %2\r\n
0xb000034c | BitLocker was unable to recover from device lock in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034d | BitLocker Drive Encryption recovery information for volume %1 was backed up successfully to your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xb000034e | Failed to backup BitLocker Drive Encryption recovery information for volume %1 to your Azure AD.%nTraceId: %2%n%nError: %3\r\n
0xb000034f | Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000350 | Failed to update BCD store with the Recovery URL for OS volume.%n%nError: %1\r\n
0xb0000351 | Failed to set the TPM dictionary attack parameters to the legacy behavior.%n%nError: %1.\r\n
0xb0000352 | Successfully set the TPM dictionary attack parameters to the legacy behavior.\r\n
0xb0000353 | Failed to enable Silent Encryption. %n%nError: %1.\r\n
0xb0000354 | Failed to enable Silent Encryption. Device is not AAD joined. %n%nError: %1.\r\n
0xb0000355 | Failed to enable Silent Encryption. TPM is not available. %n%nError: %1.\r\n
0xb0000356 | Failed to enable Silent Encryption. WinRe is not configured. %n%nError: %1.\r\n
0xb0000357 | Recovery Password Rotation initiated.\r\n
0xb0000358 | Failed to initiate the Recovery Password Rotation %n%nError:%1.\r\n
0xb0000359 | Recovery Passwords Rotation done successfully\r\n
0xb000035a | Recovery Password Rotation failed. %n%nError: %1.\r\n
0xb000035b | Recovery Password Rotation failed.%nVolume: %1%nMount: %2%nReqID: %3%nError:%4.\r\n
0xb000035c | Failed to delete recovery password from AAD.%nError:%1.\r\n
0xb000035d | Failed to create clinet recovery password rotation request. %nvolume: %1%nMount: %2%nReqId: %3%nError: %4.\r\n
0xb000035e | Failed to Create AAD recovery Password Delete request.%nVolume: %1%nMount: %2%nReqID: %3%nError:%4.\r\n
0xb000035f | Failed to initiate the Recovery Password Rotation and AAD Deletion requests processing %n%nError:%1.\r\n
0xb0000360 | Recovery Passwords Rotation and AAD Deletion requests processing initiated successfully\r\n
0xb0001000 | Device Encryption could not be initialized.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without hardware based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xb0001014 | Device Encryption initialization for volume %3 start.\r\n
0xb0001015 | Device Encryption initialization for volume %3 stop.\r\n
0xb0001016 | Volume %3 could not be initialized for Device Encryption.%n%nError: %4.\r\n
0xb0001017 | Windows RE is not correctly configured for device encryption. Make sure that Windows RE is enabled and is not installed on the OS drive.\r\n
0xb0001018 | The TPM is not provisioned for device encryption. To set up the TPM use the TPM management console (Start->tpm.msc) and use the action to make the TPM ready.\r\n
0xb0001019 | Sign in with a Microsoft account to finish provisioning device encryption.\r\n
0xb000101b | BitLocker Drive Encryption recovery information for volume %1 was deleted successfully from your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xd0000007 | default\r\n
0xd0000008 | AES-CBC 128 with Diffuser\r\n
0xd0000009 | AES-CBC 256 with Diffuser\r\n
0xd000000a | AES-CBC 128\r\n
0xd000000b | AES-CBC 256\r\n
0xd000000c | XTS-AES 128\r\n
0xd000000d | XTS-AES 256\r\n
0xd000000e | unknown\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0x90000004 | Operational\r\n
0xb0000300 | BitLocker encryption was started for volume %3 using %4 algorithm.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted using %4 algorithm.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3 using %4 algorithm.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0000348 | A trusted WIM file has been added for volume %3.%nThe SHA-256 hash of the WIM file is: %5\r\n
0xb0000349 | BitLocker was unable to update a key for volume %3 due to the following error: %4\r\n
0xb000034a | BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034b | BitLocker was suspended from within the Windows Recovery Environment.%nSuspend time: %2\r\n
0xb000034c | BitLocker was unable to recover from device lock in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034d | BitLocker Drive Encryption recovery information for volume %1 was backed up successfully to your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xb000034e | Failed to backup BitLocker Drive Encryption recovery information for volume %1 to your Azure AD.%nTraceId: %2%n%nError: %3\r\n
0xb000034f | Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000350 | Failed to update BCD store with the Recovery URL for OS volume.%n%nError: %1\r\n
0xb0000351 | Failed to set the TPM dictionary attack parameters to the legacy behavior.%n%nError: %1.\r\n
0xb0000352 | Successfully set the TPM dictionary attack parameters to the legacy behavior.\r\n
0xb0000353 | Failed to enable Silent Encryption. %n%nError: %1.\r\n
0xb0000354 | Failed to enable Silent Encryption. Device is not AAD joined. %n%nError: %1.\r\n
0xb0000355 | Failed to enable Silent Encryption. TPM is not available. %n%nError: %1.\r\n
0xb0000356 | Failed to enable Silent Encryption. WinRe is not configured. %n%nError: %1.\r\n
0xb0000357 | Recovery Password Rotation initiated.\r\n
0xb0000358 | Failed to initiate the Recovery Password Rotation %n%nError:%1.\r\n
0xb0000359 | Recovery Passwords Rotation done successfully\r\n
0xb000035a | Recovery Password Rotation failed. %n%nError: %1.\r\n
0xb000035b | Recovery Password Rotation failed.%nVolume: %1%nMount: %2%nReqID: %3%nError:%4.\r\n
0xb000035c | Failed to delete recovery password from AAD.%nError:%1.\r\n
0xb000035d | Failed to create clinet recovery password rotation request. %nvolume: %1%nMount: %2%nReqId: %3%nError: %4.\r\n
0xb000035e | Failed to Create AAD recovery Password Delete request.%nVolume: %1%nMount: %2%nReqID: %3%nError:%4.\r\n
0xb000035f | Failed to initiate the Recovery Password Rotation and AAD Deletion requests processing %n%nError:%1.\r\n
0xb0000360 | Recovery Passwords Rotation and AAD Deletion requests processing initiated successfully\r\n
0xb0001000 | Device Encryption could not be initialized.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without hardware based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xb0001014 | Device Encryption initialization for volume %3 start.\r\n
0xb0001015 | Device Encryption initialization for volume %3 stop.\r\n
0xb0001016 | Volume %3 could not be initialized for Device Encryption.%n%nError: %4.\r\n
0xb0001017 | Windows RE is not correctly configured for device encryption. Make sure that Windows RE is enabled and is not installed on the OS drive.\r\n
0xb0001018 | The TPM is not provisioned for device encryption. To set up the TPM use the TPM management console (Start->tpm.msc) and use the action to make the TPM ready.\r\n
0xb0001019 | Sign in with a Microsoft account to finish provisioning device encryption.\r\n
0xb000101a | The following DMA (Direct Memory Access) capable devices are not declared as protected from external access, which can block security features such as BitLocker automatic device encryption:%n%n%1%n\r\n
0xb000101b | BitLocker Drive Encryption recovery information for volume %1 was deleted successfully from your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xd0000007 | default\r\n
0xd0000008 | AES-CBC 128 with Diffuser\r\n
0xd0000009 | AES-CBC 256 with Diffuser\r\n
0xd000000a | AES-CBC 128\r\n
0xd000000b | AES-CBC 256\r\n
0xd000000c | XTS-AES 128\r\n
0xd000000d | XTS-AES 256\r\n
0xd000000e | unknown\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000201 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000202 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nErrorcode: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000203 | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %1%nVolume GUID: %2\r\n
0x00000204 | A BitLocker certificate data recovery agent was created, because it was missing on the volume or added to the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000205 | A BitLocker certificate data recovery agent was removed, because is no longer in the list of data recovery agents.%nCertificate thumbprint: %2%nProtector GUID: %1%nVolume GUID: %3\r\n
0x00000206 | The attempt to create a data recovery agent protector on the BitLocker volume failed.%nErrorcode: %1%nCertificate thumbprint: %2%nVolume GUID: %3\r\n
0x00000207 | The servicing of the data recovery agents on the volume failed.%nErrorcode: %1%nVolume GUID: %2\r\n
0x00000208 | The management of the data recovery agents failed on this drive because this feature of BitLocker Drive Encryption is not supported in this edition of the Windows operating system. %nErrorcode: %1%nVolume GUID: %2\r\n
0x00000209 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because the PCRs did not match.\r\n
0x0000020a | Bootmgr determined that the following boot application has changed: %1\r\n
0x0000020b | Bootmgr determined that the boot configuration data setting %1 has changed for the following boot application: %2\r\n
0x0000020c | Bootmgr determined that the authorization data for the SRK of the TPM is incompatible with BitLocker.\r\n
0x0000020d | Bootmgr determined that the TPM is disabled.\r\n
0x0000020e | Bootmgr determined that the TPM is not accessible.\r\n
0x0000020f | The partition size specified in the partition table is smaller than the size of the file system contained by that partition.  BitLocker TPM based keys cannot be used until the size of the partition calculated from the partition table is consistent with the size of the file system calculated from the bytes per sector and number of sectors fields in the boot sector.\r\n
0x00000210 | Boot debugging is enabled on Bootmgr so TPM based keys cannot be obtained.\r\n
0x00000211 | Bootmgr determined that driver signature enforcement has been disabled.\r\n
0x00000212 | Bootmgr determined that the device was locked out due to too many failed password attempts.\r\n
0x00000213 | Bootmgr determined that the device was locked out due to Device Lockout state validation failure.\r\n
0x00000337 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot was disabled.\r\n
0x00000338 | Bootmgr failed to obtain the BitLocker volume master key from the TPM because Secure Boot configuration changed unexpectedly.\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | BitLocker PIN Modification Task\r\n
0x70000065 | BitLocker Password Modification Task\r\n
0x90000001 | Microsoft-Windows-BitLocker-API\r\n
0x90000002 | System\r\n
0x90000003 | Management\r\n
0x90000004 | Operational\r\n
0xb0000300 | BitLocker encryption was started for volume %3 using %4 algorithm.\r\n
0xb0000301 | BitLocker encryption will occur for volume %3 when the computer is restarted using %4 algorithm.\r\n
0xb0000302 | BitLocker decryption was started for volume %3.\r\n
0xb0000303 | BitLocker encryption was stopped for volume %3.\r\n
0xb0000304 | BitLocker encryption was restarted for volume %3 using %4 algorithm.\r\n
0xb0000305 | BitLocker was suspended for volume %3.\r\n
0xb0000306 | BitLocker was resumed for volume %3.\r\n
0xb0000307 | A BitLocker key protector was created.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000308 | A BitLocker key protector was removed.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000309 | The PIN was updated for the operating system volume.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030a | The BitLocker volume %3 was reverted to an unprotected state.\r\n
0xb000030b | The BitLocker volume %3 was erased.\r\n
0xb000030c | The identification field was changed. %nIdentification GUID: %1\r\n
0xb000030d | The BitLocker protected volume %3 was locked. %nIdentification GUID: %1\r\n
0xb000030e | The BitLocker protected volume %3 was unlocked.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb000030f | BitLocker Drive Encryption recovery information for the specified protector is already present in Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000310 | BitLocker Drive Encryption recovery information was backed up successfully to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000311 | Failed to backup BitLocker Drive Encryption recovery information to Active Directory Domain Services.%nProtector GUID: %4%nIdentification GUID: %1\r\n
0xb0000312 | BitLocker free space wiping was started for volume %3.\r\n
0xb0000313 | BitLocker free space wiping was stopped for volume %3.\r\n
0xb0000314 | BitLocker free space wiping was restarted for volume %3.\r\n
0xb0000315 | The PIN was changed.\r\n
0xb0000316 | A PIN change attempt failed.%nError message: %1\r\n
0xb0000317 | The BitLocker Service (BdeSvc) PIN and password change facility is locked out due to too many failed PIN or password change attempts.\r\n
0xb0000318 | BitLocker encountered a failure to commit metadata changes for volume %3.\r\n
0xb0000319 | BitLocker resealed boot settings to the TPM for volume %3.\r\n
0xb000031a | BitLocker failed to reseal boot settings to the TPM.%nError message: %1.\r\n
0xb000031b | BitLocker failed to initialize hardware encryption for volume %3 due to group policy.\r\n
0xb000031c | BitLocker Drive Encryption is using software-based encryption to protect volume %3.\r\n
0xb000031d | Group Policy settings prevented BitLocker Drive Encryption from reverting to BitLocker software-based encryption. Volume %3 is not protected by BitLocker.\r\n
0xb000031e | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is not activated on this drive.\r\n
0xb000031f | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe hardware-based encryption of this drive does not allow BitLocker to cryptographically protect the drive's media encryption key.\r\n
0xb0000320 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption is either not configured or has been configured improperly on this volume.\r\n
0xb0000321 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nHardware-based encryption cannot be used with this drive because the hardware encryption method used by this drive does not comply with the Group Policy requirement for drive encryption.\r\n
0xb0000322 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is below the minimum key length supported by the drive: %4.\r\n
0xb0000323 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nThe key length, %5 bits, required to enable hardware-based encryption is above the maximum key length supported by the drive: %4.\r\n
0xb0000324 | The target drive (%3) cannot be managed by BitLocker because the drive's hardware encryption feature is already in use.\r\n
0xb0000325 | The BitLocker protected volume was unlocked in the Windows Recovery Environment.%nProtector GUID: %2%nIdentification GUID: %1%nUnlock time: %4\r\n
0xb0000326 | BitLocker resealed boot settings to the TPM in the Windows Recovery Environment.%nReseal time: %2\r\n
0xb0000327 | BitLocker free space wiping was canceled for volume %3.\r\n
0xb0000328 | BitLocker failed to initialize hardware encryption for volume %3.%nDrive is not provisioned for use with BitLocker hardware encryption:%nSID authority is not disabled on this drive.\r\n
0xb0000329 | BitLocker cannot use Secure Boot for integrity because it is disabled in Group Policy.\r\n
0xb000032a | BitLocker cannot use Secure Boot for integrity because it is disabled.\r\n
0xb000032b | BitLocker cannot use Secure Boot for integrity because the required UEFI variable '%1' is not present.\r\n
0xb000032c | BitLocker cannot use Secure Boot for integrity because the UEFI variable '%1' could not be read.%n%nError Message: %2\r\n
0xb000032d | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for variable '%1' is missing or invalid.\r\n
0xb000032e | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is missing or invalid.\r\n
0xb000032f | BitLocker cannot use Secure Boot for integrity because the expected TCG Log separator entry is missing or invalid.\r\n
0xb0000330 | BitLocker cannot use Secure Boot for integrity because the TCG Log for PCR [7] contains invalid entries.\r\n
0xb0000331 | BitLocker successfully sealed a key to the TPM.%n%nPCRs measured include [%1].%n%nThe source for these PCRs was: %2.\r\n
0xb0000332 | BitLocker encountered a failure attempting to configure network unlock for volume %3.\r\n
0xb0000333 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Bootable media in the drive.\r\n
0xb0000334 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: TPM is locked out.\r\n
0xb0000335 | The BitLocker service could not resume protection on the OS volume %3, due to the following error: Group policy conflict.\r\n
0xb0000336 | The BitLocker service could not resume protection on the OS volume %3, due to the following error code: %4.\r\n
0xb0000339 | BitLocker failed to initialize hardware encryption for volume %3.%nThis PC's firmware is not capable of supporting hardware encryption.\r\n
0xb000033a | The password was changed.\r\n
0xb000033b | A password change attempt failed.%nError message: %1\r\n
0xb000033c | BitLocker Drive Encryption recovery information for volume %3 was backed up successfully to your Microsoft account.%nProtector GUID: %4\r\n
0xb000033d | Failed to backup BitLocker Drive Encryption recovery information for volume %3 to your Microsoft account.%n%nError: %4\r\n
0xb000033e | The BitLocker Drive Encryption recovery information already exists in your Microsoft account.\r\n
0xb000033f | Failed to save BitLocker Drive Encryption recovery information to your Microsoft account due to an error.%n%nError Code: %1%nLocalized Error Message: %2\r\n
0xb0000340 | TCG Log parsing failure.%n%nError: %1.\r\n
0xb0000341 | BitLocker detected that custom Secure Boot policy is installed, and will seal to this configuration. Sealing to a custom policy may reduce the integrity provided by Secure Boot.\r\n
0xb0000342 | BitLocker determined that the TCG log is invalid for use of Secure Boot. The filtered TCG log for PCR[7] is included in this event.\r\n
0xb0000343 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority has invalid structure.%n%nThe event is expected to be an EV_EFI_VARIABLE_AUTHORITY event. The event data must be formatted as an EFI_VARIABLE_DATA structure with VariableName set to EFI_IMAGE_SECURITY_DATABASEGUID and UnicodeName set to 'db'.\r\n
0xb0000344 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe contents of the EFI_VARIABLE_DATA.VariableData field should be an EFI_SIGNATURE_DATA structure with SignatureOwner set to the GUID {77fa9abd-0359-4d32-bd60-28f4e78f784b} (Microsoft).\r\n
0xb0000345 | BitLocker cannot use Secure Boot for integrity because the expected TCG Log entry for the OS Loader Authority is invalid.%n%nThe EFI_SIGNATURE_DATA structure contained in the OS authority event could not be found in the Secure Boot 'db' signature database.\r\n
0xb0000346 | BitLocker cannot use Secure Boot for integrity because the signature of the boot loader could not be validated as a Windows signature chained to a trusted Microsoft root certificate.\r\n
0xb0000347 | BitLocker cannot use Secure Boot for integrity because the TCG Log entry for the OS Loader Authority is invalid.%n%nThe signature contained in the EFI_SIGNATURE_DATA structure from the OS authority event could not be found in the verified certificate chain for the boot loader.\r\n
0xb0000348 | A trusted WIM file has been added for volume %3.%nThe SHA-256 hash of the WIM file is: %5\r\n
0xb0000349 | BitLocker was unable to update a key for volume %3 due to the following error: %4\r\n
0xb000034a | BitLocker was unable to reseal boot settings to the TPM in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034b | BitLocker was suspended from within the Windows Recovery Environment.%nSuspend time: %2\r\n
0xb000034c | BitLocker was unable to recover from device lock in the Windows Recovery Environment.%n%nError: %1%n%nProtection has been temporarily suspended.\r\n
0xb000034d | BitLocker Drive Encryption recovery information for volume %1 was backed up successfully to your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xb000034e | Failed to backup BitLocker Drive Encryption recovery information for volume %1 to your Azure AD.%nTraceId: %2%n%nError: %3\r\n
0xb000034f | Failed to save BitLocker Drive Encryption recovery information to your Azure AD due to an error.%n%n Request Id: %1%n Response Time: %2%nError Code: %3%nError Subcode: %4%nError message: %5\r\n
0xb0000350 | Failed to update BCD store with the Recovery URL for OS volume.%n%nError: %1\r\n
0xb0000351 | Failed to set the TPM dictionary attack parameters to the legacy behavior.%n%nError: %1.\r\n
0xb0000352 | Successfully set the TPM dictionary attack parameters to the legacy behavior.\r\n
0xb0000353 | Failed to enable Silent Encryption. %n%nError: %1.\r\n
0xb0000354 | Failed to enable Silent Encryption. Device is not AAD joined. %n%nError: %1.\r\n
0xb0000355 | Failed to enable Silent Encryption. TPM is not available. %n%nError: %1.\r\n
0xb0000356 | Failed to enable Silent Encryption. WinRe is not configured. %n%nError: %1.\r\n
0xb0000357 | Recovery Password Rotation initiated.\r\n
0xb0000358 | Failed to initiate the Recovery Password Rotation %n%nError:%1.\r\n
0xb0000359 | Recovery Passwords Rotation done successfully\r\n
0xb000035a | Recovery Password Rotation failed. %n%nError: %1.\r\n
0xb000035b | Recovery Password Rotation failed.%nVolume: %1%nMount: %2%nReqID: %3%nError:%4.\r\n
0xb000035c | Failed to delete recovery password from AAD.%nError:%1.\r\n
0xb000035d | Failed to create clinet recovery password rotation request. %nvolume: %1%nMount: %2%nReqId: %3%nError: %4.\r\n
0xb000035e | Failed to Create AAD recovery Password Delete request.%nVolume: %1%nMount: %2%nReqID: %3%nError:%4.\r\n
0xb000035f | Failed to initiate the Recovery Password Rotation and AAD Deletion requests processing %n%nError:%1.\r\n
0xb0000360 | Recovery Passwords Rotation and AAD Deletion requests processing initiated successfully\r\n
0xb0001000 | Device Encryption could not be initialized.%n%nError: %1.\r\n
0xb0001001 | Device Encryption initialization start.\r\n
0xb0001002 | Device Encryption initialization stop.\r\n
0xb0001003 | Device Encryption failed to process user logon event.%n%nError: %1.\r\n
0xb0001004 | Beginning Device Encryption user logon processing.\r\n
0xb0001005 | Ending Device Encryption user logon processing.\r\n
0xb0001006 | BitLocker failed to recover after Device Lock.%nError message: %1.\r\n
0xb0001007 | Failed to automatically enable Device Encryption.%n%nError Message: %1\r\n
0xb0001008 | Begin Enable Protection.\r\n
0xb0001009 | End Enable Protection.\r\n
0xb000100a | Failed to automatically back up recovery password to your Microsoft account.%n%nError Message: %1\r\n
0xb000100b | Begin Recovery Password Backup.\r\n
0xb000100c | End Recovery Password Backup.\r\n
0xb000100d | Begin Query Protection Status.\r\n
0xb000100e | End Query Protection Status.\r\n
0xb000100f | Device Lock recovery event initiated for volume %3.\r\n
0xb0001010 | MaxPasswordRetry policy enforced with TPM-based hardening for volume %3.\r\n
0xb0001011 | MaxPasswordRetry policy enforced without hardware based hardening for volume %3.\r\n
0xb0001012 | Device Lock recovery event initiated due to protected state mismatch for volume %3.\r\n
0xb0001014 | Device Encryption initialization for volume %3 start.\r\n
0xb0001015 | Device Encryption initialization for volume %3 stop.\r\n
0xb0001016 | Volume %3 could not be initialized for Device Encryption.%n%nError: %4.\r\n
0xb0001017 | Windows RE is not correctly configured for device encryption. Make sure that Windows RE is enabled and is not installed on the OS drive.\r\n
0xb0001018 | The TPM is not provisioned for device encryption. To set up the TPM use the TPM management console (Start->tpm.msc) and use the action to make the TPM ready.\r\n
0xb0001019 | Sign in with a Microsoft account to finish provisioning device encryption.\r\n
0xb000101a | The following DMA (Direct Memory Access) capable devices are not declared as protected from external access, which can block security features such as BitLocker automatic device encryption:%n%n%1%n\r\n
0xb000101b | BitLocker Drive Encryption recovery information for volume %1 was deleted successfully from your Azure AD.%nProtector GUID: %2.%nTraceId: %3\r\n
0xb000101c | HSTI is not supported on this device\r\n
0xb000101d | Failed to query HSTI data size. Error: %1\r\n
0xb000101e | Actual HSTI data size: %1.%nExpected HSTI data size to be at least: %2\r\n
0xb000101f | HSTI provider count: %1\r\n
0xb0001020 | HSTI data version: %1.%nExpected HSTI data version: %2\r\n
0xb0001021 | HSTI security features size mismatch for HSTI provider %1: expected %2, actual %3\r\n
0xb0001022 | HSTI provider %1 found with unknown version %2. This provider will not be processed\r\n
0xb0001023 | HSTI provider %1 found. Has PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE: %2.%n(Note: there should only be one provider with this role.)\r\n
0xb0001024 | HSTI provider %1 found. Has PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE: %2.%nSince the platform was reported to have at least one other provider with PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE, HSTI is deemed unsafe\r\n
0xb0001025 | No HSTI provider with PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE found\r\n
0xb0001026 | HSTI provider %1 (which is not PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE) set SecurityFeaturesRequired\r\n
0xb0001027 | HSTI combined results report secure Intel Thunderbolt configuration bit: %1\r\n
0xb0001028 | Required HSTI features were not verified by any provider. For byte %1, the mask of missing features is: %2\r\n
0xb0001029 | HSTI tests failed. Error messages from HSTI Provider %1: %2\r\n
0xb000102a | Successfully setup TPM API callback.\r\n
0xb000102b | Failed to setup TPM API callback. Error Code: %1\r\n
0xb000102c | Successfully added predicted TPM protector.\r\n
0xb000102d | Failed to add predicted TPM protector. Error Code: %4.\r\n
0xb000102e | Predicted PCR4 value for TPM info based protector. Predicted Value: %5.\r\n
0xb000102f | Failed to evaluate PCR4 predicted value from TPM info. Error Code: %1\r\n
0xb0001030 | Predicted PCR7 value for TPM info based protector. Predicted Value: %5.\r\n
0xb0001031 | Failed to evaluate PCR7 predicted value from TPM info. Error Code: %1\r\n
0xd0000001 | Group Policy\r\n
0xd0000002 | Caller Supplied\r\n
0xd0000003 | Secure Boot\r\n
0xd0000004 | Existing Protector\r\n
0xd0000005 | Default for PCs with UEFI firmware\r\n
0xd0000006 | Default for PCs with BIOS firmware\r\n
0xd0000007 | default\r\n
0xd0000008 | AES-CBC 128 with Diffuser\r\n
0xd0000009 | AES-CBC 256 with Diffuser\r\n
0xd000000a | AES-CBC 128\r\n
0xd000000b | AES-CBC 256\r\n
0xd000000c | XTS-AES 128\r\n
0xd000000d | XTS-AES 256\r\n
0xd000000e | unknown\r\n
0xf0000001 | 0\r\n
0xf0000002 | 1\r\n
0xf0000003 | 2\r\n
0xf0000004 | 3\r\n
0xf0000005 | 4\r\n
0xf0000006 | 5\r\n
0xf0000007 | 6\r\n
0xf0000008 | 7\r\n
0xf0000009 | 8\r\n
0xf000000a | 9\r\n
0xf000000b | 10\r\n
0xf000000c | 11\r\n
