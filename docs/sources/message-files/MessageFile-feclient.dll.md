## feclient.dll

Path: %SystemRoot%\system32\feclient.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x90000001 | Encrypting File System\r\n
0xb0000001 | An API call failed at %1.%2.  Error code: %3\r\n
0xb0000002 | An API call failed at %1.%2.  Error code: %3, Data: %4\r\n
0xb0000003 | An API call failed at %1.%2.  Error code: %3, Data: %4, %5\r\n
0xb0000004 | %1.%2: Failed to allocate %3 bytes.\r\n
0xb0000100 | EFS key promoted from current key.  CertValidated: %1, cbHash: %2, pbHash: %3, ContainerName: %4, ProviderName: %5, DisplayInformation: %6, dwCapabilities: %7, bIsCurrentKey: %8, eKeyType: %9\r\n
0xb0000101 | EFS key demoted from current key.  CertValidated: %1, cbHash: %2, pbHash: %3, ContainerName: %4, ProviderName: %5, DisplayInformation: %6, dwCapabilities: %7, bIsCurrentKey: %8, eKeyType: %9\r\n
0xb0000102 | EFS key flushed from cache.  CertValidated: %1, cbHash: %2, pbHash: %3, ContainerName: %4, ProviderName: %5, DisplayInformation: %6, dwCapabilities: %7, bIsCurrentKey: %8, eKeyType: %9\r\n
0xb0000103 | %1.%2: The specified key is not valid for EFS\r\n
0xb0000104 | %1.%2: Attempt to create a new EFS key\r\n
0xb0000105 | %1.%2: A new EFS key was successfully created\r\n
0xb0000106 | %1.%2: Begin searching the MY store for a valid EFS key\r\n
0xb0000108 | %1.%2: Deleting currentkey from registry\r\n
0xb0000109 | %1.%2: The EFS cert is self-signed, but self-signed certs are disabled by policy\r\n
0xb0000110 | %1.%2: RSA is required by policy, but the key does not support RSA encryption\r\n
0xb0000111 | %1.%2: MASTERKEY is required by policy, but the key does not support MASTERKEY encryption\r\n
0xb0000112 | %1.%2: SMARTCARDS are required by policy, but the key is not SMARTCARD-based\r\n
0xb0000113 | %1.%2: key is expired\r\n
0xb0000114 | %1.%2: key is valid\r\n
0xb0000115 | %1.%2: try and locate the matching key based on cert hash\r\n
0xb0000116 | %1.%2: key successfully loaded from registry\r\n
0xb0000117 | %1.%2: try and locate the matching key in cache\r\n
0xb0000118 | %1.%2: trying to load the masterkey history\r\n
0xb0000119 | %1.%2: masterkey history loaded\r\n
0xb0000120 | %1.%2: failed to encrypt: SIS or HSM file\r\n
0xb0000200 | %1.%2: releasing user cache object.  Refcount: %3\r\n
0xb0000201 | %1.%2: trying to stop cache polling thread\r\n
0xb0000202 | %1.%2: no decryption status in cache\r\n
0xb0000203 | %1.%2: found matching decryption status in cache\r\n
0xb0000204 | %1.%2: attempting to add key to user cache\r\n
0xb0000205 | EFS key added to user cache.  CertValidated: %1, cbHash: %2, pbHash: %3, ContainerName: %4, ProviderName: %5, DisplayInformation: %6, dwCapabilities: %7, bIsCurrentKey: %8, eKeyType: %9\r\n
0xb0000206 | %1.%2: ensuring user has cache node\r\n
0xb0000207 | %1.%2: found cache node in user info\r\n
0xb0000208 | %1.%2: found cache node in global cache\r\n
0xb0000209 | %1.%2: creating new cache node for user\r\n
0xb0000300 | %1.%2: Policy settings specified flush on card removal.  Starting the polling thread...\r\n
0xb0000301 | %1.%2: Policy settings specified NO flush on timeout.  Stopping the polling thread...\r\n
0xb0000302 | %1.%2: Policy settings specified flush on timeout.  Starting the polling thread...\r\n
0xb0000303 | %1.%2: Policy settings specified new cache flush interval: %3.  Stop polling (will restart if there are active user caches)\r\n
0xb0000304 | %1.%2: Polling thread stopped\r\n
0xb0000305 | %1.%2: Flush cache specified by policy, and we have active user caches.  Start polling.\r\n
0xb0000306 | %1.%2: Polling thread started\r\n
0xb0000307 | %1.%2: User logon detected.  Beginning SSO processing.\r\n
0xb0000308 | %1.%2: User logon detected, but is not smartcard-based.  No SSO processing required.\r\n
0xb0000309 | %1.%2: Smartcard notification detected.  Beginning SSO processing.\r\n
0xb0000310 | %1.%2: Smartcard notification detected, but the logon cert is already cached.  No processing required.\r\n
0xb0000311 | %1.%2: Current key matches the logon cert.  Setting up the PIN cache.\r\n
0xb0000312 | %1.%2: User does not yet have a current key.  If smartcard is required by policy, the logon cert and PIN will be cached.\r\n
0xb0000313 | %1.%2: Logon notification detected on DC.  Beginning DRA install.\r\n
0xb0000314 | %1.%2: user does not already have a cache: generating one now\r\n
0xb0000315 | %1.%2: generating pre-cache for PIN and logon cert\r\n
0xb0000316 | %1.%2: tried to install logon cert, but it's not available (not a smartcard logon, or the smartcard was removed)\r\n
0xb0000317 | %1.%2: logon cert successfully installed\r\n
0xb0000318 | %1.%2: trying to install logon cert\r\n
0xb0000319 | %1.%2: User lock detected.  Beginning SSO processing.\r\n
0xb0000320 | %1.%2: User logoff detected.  Beginning SSO processing.\r\n
0xb0000321 | %1.%2: Flushing the user cache\r\n
0xb0000322 | %1.%2: User has locked workstation, but policy says not to flush cache\r\n
0xb0000323 | %1.%2: Checking for expired cache entries\r\n
0xb0000324 | %1.%2: Expired certificate in recovery policy\r\n
0xb0000325 | %1.%2: Certificate in recovery policy is not yet valid\r\n
0xb0000400 | %1.%2: SL policy successfully updated\r\n
0xb0000410 | %1.%2: EFS is disabled by SL policy\r\n
0xb0000411 | %1.%2: EFS is not yet initialized\r\n
0xb0000412 | %1.%2: EFS is disabled\r\n
0xb0000500 | %1.%2: the data received by the API was too large.  Expected: %3, Actual: %4\r\n
0xb0000501 | %1.%2: the data received by the API was too small.  Expected: %3, Actual: %4\r\n
0xb0000502 | %1.%2: POSSIBLE EFS ATTACK DETECTED: %3, %4, %5\r\n
0xb0000503 | %1.%2: attempting to validate EFS stream\r\n
0xb0000504 | %1.%2: EFS stream validated\r\n
0xb0000600 | PIN prompt dialog has closed\r\n
0xb0000601 | Prompt the user to select a smartcard-based EFS cert\r\n
0xb0000602 | Smartcard-based EFS cert successfully selected by the user\r\n
0xb0000603 | Prompt the user for PIN\r\n
0xb0000604 | PIN successfully acquired from the user\r\n
0xb0000605 | Perfect match found in cache.\r\n
0xb0000606 | Masterkey history already loaded\r\n
0xb0000607 | Current key loaded from cache\r\n
0xb0000608 | Current key loaded from registry\r\n
0xb0000609 | %1.%2: Masterkey history: failed size consistency check.  %3, %4, %5\r\n
0xb0001000 | %1.%2: Encrypted keys not equal\r\n
0xb0001001 | %1.%2: doing a REKEY, but the DDF entry already exists\r\n
0xb0001002 | %1.%2: replace operation added a DDF (unexpected)\r\n
0xb0001003 | %1.%2: user is modifying a DDF entry not matching the PoP entry.  Require WRITE_ATTRIBUTES\r\n
0xb0001004 | %1.%2: user is modifying a DDF matching the PoP entry, or the DRF.  Don't require WRITE_ATTRIBUTES\r\n
0xb0001005 | %1.%2: UNEXPECTED condition: no ENCRYPTED_KEY for SC failure\r\n
0xb0001006 | %1.%2: Plug-n-Play service not ready. EFS server will not try to detect interrupted encryption/decryption operation(s).\r\n
0xb0001101 | %1.%2: Cannot open log file. Encryption/decryption operation(s) cannot be recovered.\r\n
0xb0001102 | %1.%2: Cannot read log file. Encryption/decryption operation(s) cannot be recovered.\r\n
0xb0001103 | %1.%2: A corrupted or different format log file has been found. No action was taken.\r\n
0xb0001104 | %1.%2: The log file cannot be opened as non-cached IO. No action was taken.\r\n
0xb0001105 | %1.%2: Interrupted encryption/decryption operation(s) found on a volume. Recovery procedure started.\r\n
0xb0001106 | %1.%2: EFS recovery service cannot open the file %3. The interrupted encryption/decryption operation cannot be recovered.\r\n
0xb0001107 | %1.%2: EFS service recovered %3 successfully.\r\n
0xb0001108 | %1.%2: EFS service could not open all the streams on file %3  The file was not recovered.\r\n
0xb0001109 | %1.%2: %3 could not be recovered Completely.  EFS driver may be missing.\r\n
0xb0001110 | %1.%2: IO Error occurred during stream recovery.  %3 was not recovered.\r\n
0xb0001111 | %1.%2: EFS recovery service cannot open the backup file %3 by name. The interrupted encryption/decryption operation (on file %4) may be recovered.  The backup file will not be deleted. User should delete the backup file if the recovery operation is done successfully.\r\n
0xb0001112 | %1.%2: %3 was opened by File ID successfully the first time but not the second time. No recovery operation was tried on file %4. This is an internal error.\r\n
0xb0001113 | %1.%2: EFS recovery service cannot get the backup file name. The interrupted encryption/decryption operation (on file %3) may be recovered.  The temporary backup file %4 is not deleted.  User should delete the backup file if the recovery operation is done successfully.\r\n
0xb0001114 | %1.%2: %3 could not be opened. %4 was not recovered.\r\n
0xb0001115 | %1.%2: Stream Information could be got from %3. %4 was not recovered.\r\n
0xb0001116 | %1.%2: EFS service could not open all the streams on file %3.  %4 was not recovered.\r\n
