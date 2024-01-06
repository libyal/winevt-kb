## kerberos.dll

Path: %SystemRoot%\System32\kerberos.dll

### 5.0.2195.6666

Message identifier | Message string
--- | ---
0x00000002 | Kerberos\r\n
0x00000003 | Max\r\n
0x80000004 | The function %1 received a Kerberos Error Message:%n\r\n        on logon session %2%n\r\nClient Time: %3%n\r\nServer Time: %4%n\r\nError Code: %5 %6%n\r\nClient Realm: %7%n\r\nClient Name: %8%n\r\nServer Realm: %9%n\r\nServer Name: %10%n\r\nTarget Name: %11%n\r\nError Text: %12%n\r\nFile: %13%n\r\nLine: %14%n\r\nError Data is in record data.\r\n
0xc0000001 | Process %1 attempted to negotiate Kerberos authentication with the\r\ndirectory service using Local System credentials but the %2 authentication\r\npackage was used instead.  This may result in significantly reduced\r\nrights when accessing the directory service.\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x00000001 | Kerberos\r\n
0x00000002 | Max\r\n
0x40000004 | The kerberos client received a KRB_AP_ERR_MODIFIED error from the\r\nserver %1.  This indicates that the password used to encrypt the kerberos service ticket\r\nis different than that on the target server. Commonly, this is due to identically named \r\nmachine accounts in the target realm (%2), and the client realm.  \r\nPlease contact your system administrator.\r\n
0x40000005 | The kerberos client received a KRB_AP_ERR_TKT_NYV error from the\r\nserver %1.  This indicates that the ticket used against that server is not yet\r\nvalid (in relationship to that server time).  Contact your system administrator \r\nto make sure the client and server times are in sync, and that the KDC in realm %2 is \r\nin sync with the KDC in the client realm.\r\n
0x80000003 | The function %1 received a Kerberos Error Message:%n\r\n        on logon session %2%n\r\nClient Time: %3%n\r\nServer Time: %4%n\r\nError Code: %5 %6%n\r\nClient Realm: %7%n\r\nClient Name: %8%n\r\nServer Realm: %9%n\r\nServer Name: %10%n\r\nTarget Name: %11%n\r\nError Text: %12%n\r\nFile: %13%n\r\nLine: %14%n\r\nError Data is in record data.\r\n
0x80000006 | The kerberos SSPI package generated an output token of size %1 bytes, which was too\r\nlarge to fit in the %2 buffer buffer provided by process id %3.  If the condition persists,\r\nplease contact your system administrator.\r\n
0xc0000007 | The kerberos subsystem encountered a PAC verification failure. \r\nThis indicates that the PAC from the client %1 in realm %2 had a PAC which failed to\r\nverify or was modified.  Contact your system administrator.\r\n
0xc0000008 | The Domain Controller rejected the client certificate used for smartcard logon. \r\nThe error data contains the information returned from the certificate \r\nvalidation process. Contact your system administrator to determine why\r\nyour smartcard logon certificate is invalid.\r\n
0xc0000009 | The client has failed to validate the Domain Controller certificate for %1.\r\nThe error data contains the information returned from the certificate \r\nvalidation process. Contact your system administrator to determine why\r\nthe Domain Controller certificate is invalid.\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00000001 | Kerberos\r\n
0x00000002 | Max\r\n
0x40000004 | The kerberos client received a KRB_AP_ERR_MODIFIED error from the\r\nserver %1.  The target name used was %3. This\r\nindicates that the password used to encrypt the kerberos service ticket\r\nis different than that on the target server. Commonly, this is due to identically named \r\nmachine accounts in the target realm (%2), and the client realm.  \r\nPlease contact your system administrator.\r\n
0x40000005 | The kerberos client received a KRB_AP_ERR_TKT_NYV error from the\r\nserver %1.  This indicates that the ticket used against that server is not yet\r\nvalid (in relationship to that server time).  Contact your system administrator \r\nto make sure the client and server times are in sync, and that the KDC in realm %2 is \r\nin sync with the KDC in the client realm.\r\n
0x80000003 | A Kerberos Error Message was received:%n\r\n        on logon session %1%n\r\nClient Time: %2%n\r\nServer Time: %3%n\r\nError Code: %4 %5%n\r\nExtended Error: %6%n\r\nClient Realm: %7%n\r\nClient Name: %8%n\r\nServer Realm: %9%n\r\nServer Name: %10%n\r\nTarget Name: %11%n\r\nError Text: %12%n\r\nFile: %13%n\r\nLine: %14%n\r\nError Data is in record data.\r\n
0x80000006 | The kerberos SSPI package generated an output token of size %1 bytes, which was too\r\nlarge to fit in the %2 buffer provided by process id %3.  If the condition persists,\r\nplease contact your system administrator.\r\n
0x8000000a | The kerberos subsystem is having problems fetching tickets from\r\nyour domain controller using the UDP network protocol.  This is \r\ntypically due to network problems.  Please contact your system \r\nadministrator.\r\n
0x8000000c | While using your smartcard over a VPN connection, the Kerberos subsystem \r\nencountered an error.  Typically, this indicates the card has been pulled\r\nfrom the reader during the VPN session.  One possible solution is to close\r\nthe VPN connection, reinsert the card, and restablish the connection.\r\n
0x8000000d | While using your smartcard for the Credential Manager the Kerberos \r\nsubsystem encountered an error that appears to be from a \r\nmissing or incorrect smartcard PIN.  To remedy, launch the Stored User Names and Passwords\r\ncontrol panel applet, and reenter the pin for the credential for %1%2%3.\r\n
0x8000000e | There were password errors using the Credential Manager.\r\nTo remedy, launch the Stored User Names and Passwords control panel\r\napplet, and reenter the password for the credential %1%2%3.\r\n
0xc0000007 | The kerberos subsystem encountered a PAC verification failure. \r\nThis indicates that the PAC from the client %1 in realm %2 had a PAC which failed to\r\nverify or was modified.  Contact your system administrator.\r\n
0xc0000008 | The Domain Controller rejected the client certificate used for smartcard logon. \r\nThe following error was returned from the certificate validation process: \r\n%1. Contact your system administrator to determine why\r\nyour smartcard logon certificate is invalid.\r\n
0xc0000009 | The client has failed to validate the Domain Controller certificate for \r\n%2. The following error was returned from the certificate \r\nvalidation process: %1.  Contact your system administrator to \r\ndetermine why the Domain Controller certificate is invalid.\r\n
0xc000000b | The Distinguished Name in the subject field of your smartcard logon \r\ncertificate does not contain enough information to locate the appropriate\r\ndomain on an unjoined machine.  Please contact your system administrator. \r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x0000000d | An error occurred while initializing the smart card logon library: %1\r\n
0x00010005 | An error occurred while retrieving a digital certificate from the inserted smart card. %1\r\n
0x00010006 | An error occurred in while attempting to verify the inserted smart card: %1\r\n
0x00010007 | An error occurred while signing a message using the inserted smart card: %1\r\n
0x00010008 | An error occurred while verifying a signed message using the inserted smart card: %1\r\n
0x00010009 | An error occurred while verifying the digital certificate retrieved from the inserted smart card: %1\r\n
0x0001000a | An error occurred while encrypting a message using the inserted smart card: %1\r\n
0x0001000b | An error occurred while decrypting a message using the inserted smart card: %1\r\n
0x0001000c | An error occurred while building a certificate context: %1\r\n
0x0001000e | An error occurred while signing a message: %1\r\n
0x0001000f | An error occurred while verifying a signed message: %1\r\n
0x00010010 | An error occurred while encrypting a message: %1\r\n
0x00010011 | An error occurred while decrypting a message: %1\r\n
0x00010012 | An error occurred while getting some provider parameter: %1\r\n
0x00010013 | An error occurred while generating a random number: %1\r\n
0x40000004 | The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server %1. The target name used was %3. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Please ensure that the target SPN is registered on, and only registered on, the account used by the server. This error can also happen when the target service is using a different password for the target service account than what the Kerberos Key Distribution Center (KDC) has for the target service account. Please ensure that the service on the server and the KDC are both updated to use the current password. If the server name is not fully qualified, and the target domain (%2) is different from the client domain (%4), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.\r\n
0x40000005 | The kerberos client received a KRB_AP_ERR_TKT_NYV error from the server %1. This indicates that the ticket used against that server is not yet valid (in relationship to that server time).  Contact your system administrator to make sure the client and server times are in sync, and that the KDC in realm %2 is in sync with the KDC in the client realm.\r\n
0x70000001 | Kerberos\r\n
0x70000002 | Max\r\n
0x80000003 | A Kerberos Error Message was received:%n on logon session %1%n Client Time: %2%n Server Time: %3%n Error Code: %4 %5%n Extended Error: %6%n Client Realm: %7%n Client Name: %8%n Server Realm: %9%n Server Name: %10%n Target Name: %11%n Error Text: %12%n File: %13%n Line: %14%n Error Data is in record data.\r\n
0x80000006 | The kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The output SSPI token being too large is probably the result of the user %4 being a member of a large number of groups.%n %n It is recommended to minimize the number of groups a user belongs to. If the problem can not be corrected by reduction of the group memberships of this user, please contact your system administrator to increase the maximum token size, which in term is configured machine-wide via the following registry value: HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\MaxTokenSize.\r\n
0x8000000a | The kerberos subsystem is having problems fetching tickets from your domain controller using the UDP network protocol. This is typically due to network problems. Please contact your system administrator.\r\n
0x8000000c | While using your smartcard over a VPN connection, the Kerberos subsystem encountered an error. Typically, this indicates the card has been pulled from the reader during the VPN session. One possible solution is to close the VPN connection, reinsert the card, and restablish the connection.\r\n
0x8000000d | While using your smartcard for the Credential Manager the Kerberos subsystem encountered an error that appears to be from a missing or incorrect smartcard PIN. To remedy, launch the Stored User Names and Passwords control panel applet, and reenter the pin for the credential for %1.\r\n
0x8000000e | There were password errors using the Credential Manager. To remedy, launch the Stored User Names and Passwords control panel applet, and reenter the password for the credential %1.\r\n
0x8000000f | The kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The application needs to be fixed to supply a token buffer of size at least %4 bytes.\r\n
0x90000001 | Microsoft-Windows-Security-Kerberos\r\n
0xc0000007 | The digitally signed Privilege Attribute Certificate (PAC) that contains the authorization information for client %1 in realm %2 could not be validated.%n %n This error is usually caused by domain trust failures; please contact your system administrator.\r\n
0xc0000008 | The Domain Controller rejected the client certificate of user %2, used for smartcard logon. The following error was returned from the certificate validation process: %1.\r\n
0xc0000009 | The client has failed to validate the Domain Controller certificate for %2. The following error was returned from the certificate validation process: %1.\r\n
0xc000000b | The Distinguished Name in the subject field of your smartcard logon certificate does not contain enough information to locate the appropriate domain on an unjoined machine. Please contact your system administrator.\r\n
0xc0000010 | The kerberos SSPI package failed to find the smartcard certificate in the certificate store. To remedy, logon as user %1 and insert the smartcard into your smartcard reader, then use the Certificates snap-in to verify that the smartcard certificate is in the user's personal certificate store.\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x0000000d | An error occurred while initializing the smart card logon library: %1\r\n
0x00010005 | An error occurred while retrieving a digital certificate from the inserted smart card. %1\r\n
0x00010006 | An error occurred in while attempting to verify the inserted smart card: %1\r\n
0x00010007 | An error occurred while signing a message using the inserted smart card: %1\r\n
0x00010008 | An error occurred while verifying a signed message using the inserted smart card: %1\r\n
0x00010009 | An error occurred while verifying the digital certificate retrieved from the inserted smart card: %1\r\n
0x0001000a | An error occurred while encrypting a message using the inserted smart card: %1\r\n
0x0001000b | An error occurred while decrypting a message using the inserted smart card: %1\r\n
0x0001000c | An error occurred while building a certificate context: %1\r\n
0x0001000e | An error occurred while signing a message: %1\r\n
0x0001000f | An error occurred while verifying a signed message: %1\r\n
0x00010010 | An error occurred while encrypting a message: %1\r\n
0x00010011 | An error occurred while decrypting a message: %1\r\n
0x00010012 | An error occurred while getting some provider parameter: %1\r\n
0x00010013 | An error occurred while generating a random number: %1\r\n
0x10000038 | Classic\r\n
0x40000004 | The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server %1. The target name used was %3. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Please ensure that the target SPN is registered on, and only registered on, the account used by the server. This error can also happen when the target service is using a different password for the target service account than what the Kerberos Key Distribution Center (KDC) has for the target service account. Please ensure that the service on the server and the KDC are both updated to use the current password. If the server name is not fully qualified, and the target domain (%2) is different from the client domain (%4), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.\r\n
0x40000005 | The kerberos client received a KRB_AP_ERR_TKT_NYV error from the server %1. This indicates that the ticket used against that server is not yet valid (in relationship to that server time).  Contact your system administrator to make sure the client and server times are in sync, and that the KDC in realm %2 is in sync with the KDC in the client realm.\r\n
0x70000001 | Kerberos\r\n
0x70000002 | Max\r\n
0x80000003 | A Kerberos Error Message was received:%n on logon session %1%n Client Time: %2%n Server Time: %3%n Error Code: %4 %5%n Extended Error: %6%n Client Realm: %7%n Client Name: %8%n Server Realm: %9%n Server Name: %10%n Target Name: %11%n Error Text: %12%n File: %13%n Line: %14%n Error Data is in record data.\r\n
0x80000006 | The kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The output SSPI token being too large is probably the result of the user %4 being a member of a large number of groups.%n %n It is recommended to minimize the number of groups a user belongs to. If the problem can not be corrected by reduction of the group memberships of this user, please contact your system administrator to increase the maximum token size, which in term is configured machine-wide via the following registry value: HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\MaxTokenSize.\r\n
0x8000000a | The kerberos subsystem is having problems fetching tickets from your domain controller using the UDP network protocol. This is typically due to network problems. Please contact your system administrator.\r\n
0x8000000c | While using your smartcard over a VPN connection, the Kerberos subsystem encountered an error. Typically, this indicates the card has been pulled from the reader during the VPN session. One possible solution is to close the VPN connection, reinsert the card, and restablish the connection.\r\n
0x8000000d | The smartcard PIN stored in Credential Manager is missing or invalid. The smartcard PIN is stored in memory only for the current interactive logon session, and is deleted if the card is removed from the reader or when the user logs off. To resolve this error, keep the card in the reader, open Credential Manager in Control Panel, and reenter the PIN for the credential %1.\r\n
0x8000000e | The password stored in Credential Manager is invalid. This might be caused by the user changing the password from this computer or a different computer. To resolve this error, open Credential Manager in Control Panel, and reenter the password for the credential %1.\r\n
0x8000000f | The kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The application needs to be fixed to supply a token buffer of size at least %4 bytes.\r\n
0x90000001 | Microsoft-Windows-Security-Kerberos\r\n
0xc0000007 | The digitally signed Privilege Attribute Certificate (PAC) that contains the authorization information for client %1 in realm %2 could not be validated.%n %n This error is usually caused by domain trust failures; please contact your system administrator.\r\n
0xc0000008 | The Domain Controller rejected the client certificate of user %2, used for smartcard logon. The following error was returned from the certificate validation process: %1.\r\n
0xc0000009 | The client has failed to validate the Domain Controller certificate for %2. The following error was returned from the certificate validation process: %1.\r\n
0xc000000b | The Distinguished Name in the subject field of your smartcard logon certificate does not contain enough information to locate the appropriate domain on an unjoined machine. Please contact your system administrator.\r\n
0xc0000010 | The kerberos SSPI package failed to find the smartcard certificate in the certificate store. To remedy, logon as user %1 and insert the smartcard into your smartcard reader, then use the Certificates snap-in to verify that the smartcard certificate is in the user's personal certificate store.\r\n
0xc0000011 | The kerberos SSPI package failed to locate the forest or domain %1 to search.  Please ensure that the forest search order policy is correctly configured, and that this forest or domain is available.\r\n

### 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x0000000d | An error occurred while initializing the smart card logon library: %1\r\n
0x00010005 | An error occurred while retrieving a digital certificate from the inserted smart card. %1\r\n
0x00010006 | An error occurred in while attempting to verify the inserted smart card: %1\r\n
0x00010007 | An error occurred while signing a message using the inserted smart card: %1\r\n
0x00010008 | An error occurred while verifying a signed message using the inserted smart card: %1\r\n
0x00010009 | An error occurred while verifying the digital certificate retrieved from the inserted smart card: %1\r\n
0x0001000a | An error occurred while encrypting a message using the inserted smart card: %1\r\n
0x0001000b | An error occurred while decrypting a message using the inserted smart card: %1\r\n
0x0001000c | An error occurred while building a certificate context: %1\r\n
0x0001000e | An error occurred while signing a message: %1\r\n
0x0001000f | An error occurred while verifying a signed message: %1\r\n
0x00010010 | An error occurred while encrypting a message: %1\r\n
0x00010011 | An error occurred while decrypting a message: %1\r\n
0x00010012 | An error occurred while retrieving some provider parameter: %1\r\n
0x00010013 | An error occurred while generating a random number: %1\r\n
0x10000038 | Classic\r\n
0x40000004 | The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server %1. The target name used was %3. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (%2) is different from the client domain (%4), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.\r\n
0x40000005 | The Kerberos client received a KRB_AP_ERR_TKT_NYV error from the server %1. This indicates that the ticket presented to that server is not yet valid (due to a discrepancy between ticket and server time. Contact your system administrator to make sure the client and server times are synchronized, and that the time for the Key Distribution Center Service (KDC) in realm %2 is synchronized with the KDC in the client realm.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Kerberos\r\n
0x70000002 | Max\r\n
0x80000003 | A Kerberos error message was received:%n on logon session %1%n Client Time: %2%n Server Time: %3%n Error Code: %4 %5%n Extended Error: %6%n Client Realm: %7%n Client Name: %8%n Server Realm: %9%n Server Name: %10%n Target Name: %11%n Error Text: %12%n File: %13%n Line: %14%n Error Data is in record data.\r\n
0x80000006 | The Kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The output SSPI token size is probably the result of the user %4 being a member of a large number of groups.%n %n It is recommended to minimize the number of groups a user belongs to. If the problem can not be corrected by reducing the group memberships of this user, contact your system administrator to increase the maximum token size, which is configured on each computer individually using the registry value: HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\MaxTokenSize.\r\n
0x8000000a | The Kerberos subsystem currently cannot retrieve tickets from your domain controller using the UDP network protocol. This is typically due to network problems. Contact your system administrator.\r\n
0x8000000c | While using your smart card over a VPN connection, the Kerberos subsystem encountered an error. Typically, this indicates the card has been pulled from the card reader during the VPN session. One possible solution is to close the VPN connection, reinsert the card, and establish the connection again.\r\n
0x8000000d | The smart card PIN stored in Credential Manager is missing or invalid. The smart card PIN is stored in memory only for the current interactive logon session, and is deleted if the card is removed from the card reader or when the user logs off. To resolve this error, keep the card in the reader, open Credential Manager in Control Panel, and reenter the PIN for the credential %1.\r\n
0x8000000e | The password stored in Credential Manager is invalid. This might be caused by the logged on user changing the password from this computer or a different computer. To resolve this error, open Credential Manager in Control Panel, and reenter the password for the credential %1.\r\n
0x8000000f | The Kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The application needs to be modified to supply a token buffer of size at least %4 bytes.\r\n
0x80000012 | The delegated TGT for the user (%2) has expired. A renewal was attempted and failed with error %8. The server logon session (%1) has stopped delegating the user's credential. For future unconstrained delegation to succeed, the user needs to authenticate again to the server. %n%nTGT Details:%n    Client: %2%n    Server: %3%n    Flags: %4%n    Start Time: %5%n    End Time: %6%n    Renew Until: %7\r\n
0x80000013 | The KDC certificate for the domain controller does not contain the KDC Extended Key Usage (EKU): 1.3.6.1.5.2.3.5: Error Code %1. The domain administrator will need to obtain a certificate with the KDC EKU for the domain controller to resolve this error. When using Windows Server Certificate Services create a certificated based on the Kerberos Authentication Template.\r\n
0x80000014 | The KDC certificate for the domain controller does not have the DNS name of domain %1 in the Subject Alternative Name (SAN) attribute: Error Code %2. The domain administrator will need to obtain a KDC certificate with the DNS domain name in the SAN attribute for the domain controller to resolve this error. When using Windows Server Certificate Services create a certificated based on the Kerberos Authentication Template.\r\n
0x90000001 | Microsoft-Windows-Security-Kerberos\r\n
0x90000002 | Operational\r\n
0xb0000064 | The service principal name (SPN) %1 is not registered, which caused Kerberos authentication to fail: %2. Use the setspn command-line tool to register the SPN.\r\n
0xb0000065 | The service principal name (SPN) %1 is registered on multiple accounts which caused Kerberos authentication to fail: %2. Use the setspn command-line tool to identify the accounts and remove the duplicate registrations.\r\n
0xb0000066 | Trust validation of the certificate for the Kerberos Key Distribution Center (KDC) %1 failed: %2. Use the CAPI2 diagnostic traces to identify the reason for the validation failure.\r\n
0xb0000067 | Trust validation of the client certificate for %1 failed: %2 on KDC. Use the CAPI2 diagnostic traces to identify the reason for the validation failure.\r\n
0xb0000068 | The Kerberos Key Distribution Center (KDC) for the domain %1 does not have a certificate installed or does not support logon using certificates: %2\r\n
0xb0000069 | The Kerberos client could not retrieve passwords for the group managed service account.%n%nLogonId: %1:%2%nDomainName: %3%nUserName: %4%nRefresh: %5%nCurrent File Time: %6%nError Code: %7%n\r\n
0xb000006a | The Kerberos client received a KDC certificate that does not have KDC EKU (not based on Kerberos Authentication Template).%n%nError Code: %1%n\r\n
0xb000006b | The Kerberos client received a KDC certificate that does not have a matched domain name.%n%nExpected Domain Name: %1%nError Code: %2%n\r\n
0xb000006c | The Kerberos client could not send a Kerberos proxy request.%n%nProxyServer:%n  ServerName: %1%n  ServerPort: %2%n  ServerVdir:  %3%nError Code: %4%nStatus Code: %5%n\r\n
0xb000006d | The Kerberos client could not find a suitable credential to use with the authentication proxy:%n%nAuthProxy:%n  Proxy: %1%n  ProxyBypass: %2%n  Epoch: %3%n  Supported Schemes: %4%n  First Scheme: %5%nDigest Credential:%n  Initialized: %6%n  DomainAndUserName: %7%n  Epoch: %8%nBasic Credential:%n  Initialized: %9%n  DomainAndUserName: %10%n  Epoch: %11%n\r\n
0xb00000c8 | The Kerberos client could not locate a domain controller for domain %1: %2. Kerberos authentication requires communicating with a domain controller.\r\n
0xb000012c | The Kerberos client discovered domain controller %1 for the domain %2.\r\n
0xb000012d | The Kerberos client used credentials from the Credential Manager for the target: '%1'.\r\n
0xb000012e | The Kerberos client was bound to domain controller %1 for the domain %2 but could not access this domain controller at the time.%n%n    DesiredFlags: %3%n    CacheFlags: %4%n    ErrorCode: %5\r\n
0xb000012f | The Kerberos client updated passwords for the group managed service account.%n%nLogonId: %1:%2%nDomainName: %3%nUserName: %4%nUpdate Current Passwords: %5%nUpdate Old Passwords: %6%nRefresh: %7%nPrevious File Time: %8%nCurrent File Time: %9%n\r\n
0xc0000007 | The digitally signed Privilege Attribute Certificate (PAC) that contains the authorization information for client %1 in realm %2 could not be validated.%n %n This error is usually caused by domain trust failures; Contact your system administrator.\r\n
0xc0000008 | The domain controller rejected the client certificate of user %2, used for smart card logon. The following error was returned from the certificate validation process: %1.\r\n
0xc0000009 | The client has failed to validate the domain controller certificate for %2. The following error was returned from the certificate validation process: %1.\r\n
0xc000000b | The Distinguished Name in the subject field of your smart card logon certificate does not contain enough information to identify the appropriate domain on an non-domain joined computer. Contact your system administrator.\r\n
0xc0000010 | The Kerberos SSPI package failed to find the smart card certificate in the certificate store. To remedy this failure, logon as user %1 and insert the smart card into the smart card reader, then use the Certificates snap-in to verify that the smart card certificate is in the user's personal certificate store.\r\n
0xc0000011 | The Kerberos SSPI package failed to locate the forest or domain %1 to search.  Ensure that the Use forest search order Group Policy is correctly configured, and that this forest or domain is available.\r\n

### 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x0000000d | An error occurred while initializing the smart card logon library: %1\r\n
0x00010005 | An error occurred while retrieving a digital certificate from the inserted smart card. %1\r\n
0x00010006 | An error occurred in while attempting to verify the inserted smart card: %1\r\n
0x00010007 | An error occurred while signing a message using the inserted smart card: %1\r\n
0x00010008 | An error occurred while verifying a signed message using the inserted smart card: %1\r\n
0x00010009 | An error occurred while verifying the digital certificate retrieved from the inserted smart card: %1\r\n
0x0001000a | An error occurred while encrypting a message using the inserted smart card: %1\r\n
0x0001000b | An error occurred while decrypting a message using the inserted smart card: %1\r\n
0x0001000c | An error occurred while building a certificate context: %1\r\n
0x0001000e | An error occurred while signing a message: %1\r\n
0x0001000f | An error occurred while verifying a signed message: %1\r\n
0x00010010 | An error occurred while encrypting a message: %1\r\n
0x00010011 | An error occurred while decrypting a message: %1\r\n
0x00010012 | An error occurred while retrieving some provider parameter: %1\r\n
0x00010013 | An error occurred while generating a random number: %1\r\n
0x10000038 | Classic\r\n
0x40000004 | The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server %1. The target name used was %3. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (%2) is different from the client domain (%4), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.\r\n
0x40000005 | The Kerberos client received a KRB_AP_ERR_TKT_NYV error from the server %1. This indicates that the ticket presented to that server is not yet valid (due to a discrepancy between ticket and server time. Contact your system administrator to make sure the client and server times are synchronized, and that the time for the Key Distribution Center Service (KDC) in realm %2 is synchronized with the KDC in the client realm.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Kerberos\r\n
0x70000002 | Max\r\n
0x80000003 | A Kerberos error message was received:%n on logon session %1%n Client Time: %2%n Server Time: %3%n Error Code: %4 %5%n Extended Error: %6%n Client Realm: %7%n Client Name: %8%n Server Realm: %9%n Server Name: %10%n Target Name: %11%n Error Text: %12%n File: %13%n Line: %14%n Error Data is in record data.\r\n
0x80000006 | The Kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The output SSPI token size is probably the result of the user %4 being a member of a large number of groups.%n %n It is recommended to minimize the number of groups a user belongs to. If the problem can not be corrected by reducing the group memberships of this user, contact your system administrator to increase the maximum token size, which is configured on each computer individually using the registry value: HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\MaxTokenSize.\r\n
0x8000000a | The Kerberos subsystem currently cannot retrieve tickets from your domain controller using the UDP network protocol. This is typically due to network problems. Contact your system administrator.\r\n
0x8000000c | While using your smart card over a VPN connection, the Kerberos subsystem encountered an error. Typically, this indicates the card has been pulled from the card reader during the VPN session. One possible solution is to close the VPN connection, reinsert the card, and establish the connection again.\r\n
0x8000000d | The smart card PIN stored in Credential Manager is missing or invalid. The smart card PIN is stored in memory only for the current interactive logon session, and is deleted if the card is removed from the card reader or when the user logs off. To resolve this error, keep the card in the reader, open Credential Manager in Control Panel, and reenter the PIN for the credential %1.\r\n
0x8000000e | The password stored in Credential Manager is invalid. This might be caused by the logged on user changing the password from this computer or a different computer. To resolve this error, open Credential Manager in Control Panel, and reenter the password for the credential %1.\r\n
0x8000000f | The Kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The application needs to be modified to supply a token buffer of size at least %4 bytes.\r\n
0x80000012 | The delegated TGT for the user (%2) has expired. A renewal was attempted and failed with error %8. The server logon session (%1) has stopped delegating the user's credential. For future unconstrained delegation to succeed, the user needs to authenticate again to the server. %n%nTGT Details:%n    Client: %2%n    Server: %3%n    Flags: %4%n    Start Time: %5%n    End Time: %6%n    Renew Until: %7\r\n
0x80000013 | The KDC certificate for the domain controller does not contain the KDC Extended Key Usage (EKU): 1.3.6.1.5.2.3.5: Error Code %1. The domain administrator will need to obtain a certificate with the KDC EKU for the domain controller to resolve this error. When using Windows Server Certificate Services create a certificated based on the Kerberos Authentication Template.\r\n
0x80000014 | The KDC certificate for the domain controller does not have the DNS name of domain %1 in the Subject Alternative Name (SAN) attribute: Error Code %2. The domain administrator will need to obtain a KDC certificate with the DNS domain name in the SAN attribute for the domain controller to resolve this error. When using Windows Server Certificate Services create a certificated based on the Kerberos Authentication Template.\r\n
0x90000001 | Microsoft-Windows-Security-Kerberos\r\n
0x90000002 | Operational\r\n
0xb0000064 | The service principal name (SPN) %1 is not registered, which caused Kerberos authentication to fail: %2. Use the setspn command-line tool to register the SPN.\r\n
0xb0000065 | The service principal name (SPN) %1 is registered on multiple accounts which caused Kerberos authentication to fail: %2. Use the setspn command-line tool to identify the accounts and remove the duplicate registrations.\r\n
0xb0000066 | Trust validation of the certificate for the Kerberos Key Distribution Center (KDC) %1 failed: %2. Use the CAPI2 diagnostic traces to identify the reason for the validation failure.\r\n
0xb0000067 | Trust validation of the client certificate for %1 failed: %2 on KDC. Use the CAPI2 diagnostic traces to identify the reason for the validation failure.\r\n
0xb0000068 | The Kerberos Key Distribution Center (KDC) for the domain %1 does not have a certificate installed or does not support logon using certificates: %2\r\n
0xb0000069 | The Kerberos client could not retrieve passwords for the group managed service account.%n%nLogonId: %1:%2%nDomainName: %3%nUserName: %4%nRefresh: %5%nCurrent File Time: %6%nError Code: %7%n\r\n
0xb000006a | The Kerberos client received a KDC certificate that does not have KDC EKU (not based on Kerberos Authentication Template).%n%nError Code: %1%n\r\n
0xb000006b | The Kerberos client received a KDC certificate that does not have a matched domain name.%n%nExpected Domain Name: %1%nError Code: %2%n\r\n
0xb000006c | The Kerberos client could not send a Kerberos proxy request.%n%nProxyServer:%n  ServerName: %1%n  ServerPort: %2%n  ServerVdir:  %3%nError Code: %4%nStatus Code: %5%n\r\n
0xb000006d | The Kerberos client could not find a suitable credential to use with the authentication proxy:%n%nAuthProxy:%n  Proxy: %1%n  ProxyBypass: %2%n  Epoch: %3%n  Supported Schemes: %4%n  First Scheme: %5%nDigest Credential:%n  Initialized: %6%n  DomainAndUserName: %7%n  Epoch: %8%nBasic Credential:%n  Initialized: %9%n  DomainAndUserName: %10%n  Epoch: %11%n\r\n
0xb00000c8 | The Kerberos client could not locate a domain controller for domain %1: %2. Kerberos authentication requires communicating with a domain controller.\r\n
0xb00000c9 | Attempt to use Kerberos unconstrained delegation failed.%n%nTarget server: %1%nSupplied user: %2%nSupplied domain: %3%nPID of client process: %4%nName of client process: %5%nLUID of client process: %6%nUser identity of client process: %7%nDomain name of user identity of client process: %8%nMechanism OID: %9%n%nKerberos unconstrained delegation is not allowed for this user. For more information, see https://go.microsoft.com/fwlink/?linkid=856824.\r\n
0xb00000ca | Attempt to export TGT session key failed.%n%nTarget server: %1%nSupplied user: %2%nSupplied domain: %3%nPID of client process: %4%nName of client process: %5%nLUID of client process: %6%nUser identity of client process: %7%nDomain name of user identity of client process: %8%nMechanism OID: %9%n%nThis device does not allow exporting TGT session keys. For more information, see https://go.microsoft.com/fwlink/?linkid=856825.\r\n
0xb00000cb | When Credential Guard is enabled, Kerberos does not accept PKINIT KDC replies using public key encryption to ensure Kerberos tickets cannot be exported from the device. For more information, see https://go.microsoft.com/fwlink/?linkid=856823.\r\n
0xb000012c | The Kerberos client discovered domain controller %1 for the domain %2.\r\n
0xb000012d | The Kerberos client used credentials from the Credential Manager for the target: '%1'.\r\n
0xb000012e | The Kerberos client was bound to domain controller %1 for the domain %2 but could not access this domain controller at the time.%n%n    DesiredFlags: %3%n    CacheFlags: %4%n    ErrorCode: %5\r\n
0xb000012f | The Kerberos client updated passwords for the group managed service account.%n%nLogonId: %1:%2%nDomainName: %3%nUserName: %4%nUpdate Current Passwords: %5%nUpdate Old Passwords: %6%nRefresh: %7%nPrevious File Time: %8%nCurrent File Time: %9%n\r\n
0xc0000007 | The digitally signed Privilege Attribute Certificate (PAC) that contains the authorization information for client %1 in realm %2 could not be validated.%n %n This error is usually caused by domain trust failures; Contact your system administrator.\r\n
0xc0000008 | The domain controller rejected the client certificate of user %2, used for smart card logon. The following error was returned from the certificate validation process: %1.\r\n
0xc0000009 | The client has failed to validate the domain controller certificate for %2. The following error was returned from the certificate validation process: %1.\r\n
0xc000000b | The Distinguished Name in the subject field of your smart card logon certificate does not contain enough information to identify the appropriate domain on an non-domain joined computer. Contact your system administrator.\r\n
0xc0000010 | The Kerberos SSPI package failed to find the smart card certificate in the certificate store. To remedy this failure, logon as user %1 and insert the smart card into the smart card reader, then use the Certificates snap-in to verify that the smart card certificate is in the user's personal certificate store.\r\n
0xc0000011 | The Kerberos SSPI package failed to locate the forest or domain %1 to search.  Ensure that the Use forest search order Group Policy is correctly configured, and that this forest or domain is available.\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x0000000d | An error occurred while initializing the smart card logon library: %1\r\n
0x00010005 | An error occurred while retrieving a digital certificate from the inserted smart card. %1\r\n
0x00010006 | An error occurred in while attempting to verify the inserted smart card: %1\r\n
0x00010007 | An error occurred while signing a message using the inserted smart card: %1\r\n
0x00010008 | An error occurred while verifying a signed message using the inserted smart card: %1\r\n
0x00010009 | An error occurred while verifying the digital certificate retrieved from the inserted smart card: %1\r\n
0x0001000a | An error occurred while encrypting a message using the inserted smart card: %1\r\n
0x0001000b | An error occurred while decrypting a message using the inserted smart card: %1\r\n
0x0001000c | An error occurred while building a certificate context: %1\r\n
0x0001000e | An error occurred while signing a message: %1\r\n
0x0001000f | An error occurred while verifying a signed message: %1\r\n
0x00010010 | An error occurred while encrypting a message: %1\r\n
0x00010011 | An error occurred while decrypting a message: %1\r\n
0x00010012 | An error occurred while retrieving some provider parameter: %1\r\n
0x00010013 | An error occurred while generating a random number: %1\r\n
0x10000038 | Classic\r\n
0x40000004 | The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server %1. The target name used was %3. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (%2) is different from the client domain (%4), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.\r\n
0x40000005 | The Kerberos client received a KRB_AP_ERR_TKT_NYV error from the server %1. This indicates that the ticket presented to that server is not yet valid (due to a discrepancy between ticket and server time. Contact your system administrator to make sure the client and server times are synchronized, and that the time for the Key Distribution Center Service (KDC) in realm %2 is synchronized with the KDC in the client realm.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Kerberos\r\n
0x70000002 | Max\r\n
0x80000003 | A Kerberos error message was received:%n on logon session %1%n Client Time: %2%n Server Time: %3%n Error Code: %4 %5%n Extended Error: %6%n Client Realm: %7%n Client Name: %8%n Server Realm: %9%n Server Name: %10%n Target Name: %11%n Error Text: %12%n File: %13%n Line: %14%n Error Data is in record data.\r\n
0x80000006 | The Kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The output SSPI token size is probably the result of the user %4 being a member of a large number of groups.%n %n It is recommended to minimize the number of groups a user belongs to. If the problem can not be corrected by reducing the group memberships of this user, contact your system administrator to increase the maximum token size, which is configured on each computer individually using the registry value: HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters\MaxTokenSize.\r\n
0x8000000a | The Kerberos subsystem currently cannot retrieve tickets from your domain controller using the UDP network protocol. This is typically due to network problems. Contact your system administrator.\r\n
0x8000000c | While using your smart card over a VPN connection, the Kerberos subsystem encountered an error. Typically, this indicates the card has been pulled from the card reader during the VPN session. One possible solution is to close the VPN connection, reinsert the card, and establish the connection again.\r\n
0x8000000d | The smart card PIN stored in Credential Manager is missing or invalid. The smart card PIN is stored in memory only for the current interactive logon session, and is deleted if the card is removed from the card reader or when the user logs off. To resolve this error, keep the card in the reader, open Credential Manager in Control Panel, and reenter the PIN for the credential %1.\r\n
0x8000000e | The password stored in Credential Manager is invalid. This might be caused by the logged on user changing the password from this computer or a different computer. To resolve this error, open Credential Manager in Control Panel, and reenter the password for the credential %1.\r\n
0x8000000f | The Kerberos SSPI package generated an output token of size %1 bytes, which was too large to fit in the token buffer of size %2 bytes, provided by process id %3.%n %n The application needs to be modified to supply a token buffer of size at least %4 bytes.\r\n
0x80000012 | The delegated TGT for the user (%2) has expired. A renewal was attempted and failed with error %8. The server logon session (%1) has stopped delegating the user's credential. For future unconstrained delegation to succeed, the user needs to authenticate again to the server. %n%nTGT Details:%n    Client: %2%n    Server: %3%n    Flags: %4%n    Start Time: %5%n    End Time: %6%n    Renew Until: %7\r\n
0x80000013 | The KDC certificate for the domain controller does not contain the KDC Extended Key Usage (EKU): 1.3.6.1.5.2.3.5: Error Code %1. The domain administrator will need to obtain a certificate with the KDC EKU for the domain controller to resolve this error. When using Windows Server Certificate Services create a certificated based on the Kerberos Authentication Template.\r\n
0x80000014 | The KDC certificate for the domain controller does not have the DNS name of domain %1 in the Subject Alternative Name (SAN) attribute: Error Code %2. The domain administrator will need to obtain a KDC certificate with the DNS domain name in the SAN attribute for the domain controller to resolve this error. When using Windows Server Certificate Services create a certificated based on the Kerberos Authentication Template.\r\n
0x90000001 | Microsoft-Windows-Security-Kerberos\r\n
0x90000002 | Operational\r\n
0xb0000064 | The service principal name (SPN) %1 is not registered, which caused Kerberos authentication to fail: %2. Use the setspn command-line tool to register the SPN.\r\n
0xb0000065 | The service principal name (SPN) %1 is registered on multiple accounts which caused Kerberos authentication to fail: %2. Use the setspn command-line tool to identify the accounts and remove the duplicate registrations.\r\n
0xb0000066 | Trust validation of the certificate for the Kerberos Key Distribution Center (KDC) %1 failed: %2. Use the CAPI2 diagnostic traces to identify the reason for the validation failure.\r\n
0xb0000067 | Trust validation of the client certificate for %1 failed: %2 on KDC. Use the CAPI2 diagnostic traces to identify the reason for the validation failure.\r\n
0xb0000068 | The Kerberos Key Distribution Center (KDC) for the domain %1 does not have a certificate installed or does not support logon using certificates: %2\r\n
0xb0000069 | The Kerberos client could not retrieve passwords for the group managed service account.%n%nLogonId: %1:%2%nDomainName: %3%nUserName: %4%nRefresh: %5%nCurrent File Time: %6%nError Code: %7%n\r\n
0xb000006a | The Kerberos client received a KDC certificate that does not have KDC EKU (not based on Kerberos Authentication Template).%n%nError Code: %1%n\r\n
0xb000006b | The Kerberos client received a KDC certificate that does not have a matched domain name.%n%nExpected Domain Name: %1%nError Code: %2%n\r\n
0xb000006c | The Kerberos client could not send a Kerberos proxy request.%n%nProxyServer:%n  ServerName: %1%n  ServerPort: %2%n  ServerVdir:  %3%nError Code: %4%nStatus Code: %5%n\r\n
0xb000006d | The Kerberos client could not find a suitable credential to use with the authentication proxy:%n%nAuthProxy:%n  Proxy: %1%n  ProxyBypass: %2%n  Epoch: %3%n  Supported Schemes: %4%n  First Scheme: %5%nDigest Credential:%n  Initialized: %6%n  DomainAndUserName: %7%n  Epoch: %8%nBasic Credential:%n  Initialized: %9%n  DomainAndUserName: %10%n  Epoch: %11%n\r\n
0xb00000c8 | The Kerberos client could not locate a domain controller for domain %1: %2. Kerberos authentication requires communicating with a domain controller.\r\n
0xb00000c9 | Attempt to use Kerberos unconstrained delegation failed.%n%nTarget server: %1%nSupplied user: %2%nSupplied domain: %3%nPID of client process: %4%nName of client process: %5%nLUID of client process: %6%nUser identity of client process: %7%nDomain name of user identity of client process: %8%nMechanism OID: %9%n%nKerberos unconstrained delegation is not allowed for this user. For more information, see https://go.microsoft.com/fwlink/?linkid=856824.\r\n
0xb00000ca | Attempt to export TGT session key failed.%n%nTarget server: %1%nSupplied user: %2%nSupplied domain: %3%nPID of client process: %4%nName of client process: %5%nLUID of client process: %6%nUser identity of client process: %7%nDomain name of user identity of client process: %8%nMechanism OID: %9%n%nThis device does not allow exporting TGT session keys. For more information, see https://go.microsoft.com/fwlink/?linkid=856825.\r\n
0xb00000cb | When Credential Guard is enabled, Kerberos does not accept PKINIT KDC replies using public key encryption to ensure Kerberos tickets cannot be exported from the device. For more information, see https://go.microsoft.com/fwlink/?linkid=856823.\r\n
0xb00000cc | Kerberos does not accept PKINIT KDC replies using public key encryption.\r\n
0xb000012c | The Kerberos client discovered domain controller %1 for the domain %2.\r\n
0xb000012d | The Kerberos client used credentials from the Credential Manager for the target: '%1'.\r\n
0xb000012e | The Kerberos client was bound to domain controller %1 for the domain %2 but could not access this domain controller at the time.%n%n    DesiredFlags: %3%n    CacheFlags: %4%n    ErrorCode: %5\r\n
0xb000012f | The Kerberos client updated passwords for the group managed service account.%n%nLogonId: %1:%2%nDomainName: %3%nUserName: %4%nUpdate Current Passwords: %5%nUpdate Old Passwords: %6%nRefresh: %7%nPrevious File Time: %8%nCurrent File Time: %9%n\r\n
0xc0000007 | The digitally signed Privilege Attribute Certificate (PAC) that contains the authorization information for client %1 in realm %2 could not be validated.%n %n This error is usually caused by domain trust failures; Contact your system administrator.\r\n
0xc0000008 | The domain controller rejected the client certificate of user %2, used for smart card logon. The following error was returned from the certificate validation process: %1.\r\n
0xc0000009 | The client has failed to validate the domain controller certificate for %2. The following error was returned from the certificate validation process: %1.\r\n
0xc000000b | The Distinguished Name in the subject field of your smart card logon certificate does not contain enough information to identify the appropriate domain on an non-domain joined computer. Contact your system administrator.\r\n
0xc0000010 | The Kerberos SSPI package failed to find the smart card certificate in the certificate store. To remedy this failure, logon as user %1 and insert the smart card into the smart card reader, then use the Certificates snap-in to verify that the smart card certificate is in the user's personal certificate store.\r\n
0xc0000011 | The Kerberos SSPI package failed to locate the forest or domain %1 to search.  Ensure that the Use forest search order Group Policy is correctly configured, and that this forest or domain is available.\r\n
