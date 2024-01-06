## qagentrt.dll

Path: %SystemRoot%\system32\qagentrt.dll

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x00000004 | The System Health Agent %1 successfully initialized.\r\n
0x00000005 | The System Health Agent %1 successfully uninitialized.\r\n
0x00000009 | The enforcement client %1 successfully initialized.\r\n
0x0000000a | The enforcement client %1 successfully uninitialized.\r\n
0x40000012 | System Isolation State Change.%n Previous : %n    State          : %1 (%2)%n    Extended State : %3 (%4)%n    Probation Time : %5%n    Help URL       : %6%n Current : %n    State          : %7 (%8)%n    Extended State : %9 (%10)%n    Probation Time : %11%n    Help URL       : %12%n\r\n
0x40000016 | The Network Access Protection Agent successfully acquired a certificate for the request with the correlation-id %2 from %1.%n The certificate can be identified by its thumbprint of %3%n\r\n
0x40000017 | The Network Access Protection Agent successfully deleted the certificate with the thumbprint of %1.%n The certificate has expired or the health state of the client has changed or a replacement certificate has been acquired.%n See the administrator for more information.%n\r\n
0x40000019 | The client loaded NAP group policy.%n\r\n
0x4000001a | The NAP service has started.%n NAP has the following information for this computer:%n Computer name is %1.%n Domain status is: %2.%n The OS SKU is: %4.%n The service pack version is: %6.%n The processor type is: %5.%n\r\n
0x4000001b | A Statement of Health with correlation ID %1 was received from the System Health Agent %2. %n The duration to check the client's health was %3 ms.\r\n
0x4000001c | A Statement of Health with correlation ID %1 was sent to the enforcment client %2.\r\n
0x4000001d | A Statement of Health Response with correlation ID %1 was received from the enforcement client %2.%n The current client state is %3. %n The current client extended state is %4. %n The following SHAs report this client non-compliant: %5%n The following error categories were encountered: %6%n The probation expiration time is: %7%n The help URL is: %8%n The duration of health check was %9 ms.%n\r\n
0x40000028 | The Network Access Protection Agent has dynamically discovered the following HRAs for this network (using the query %1):%n%2%nThe DNS servers in your configuration at the time this discovery took place included:%n%3\r\n
0x8000000f | A Statement of Health Request with correlation ID %1 could not include the following System Health Agents in the statement of Health: %2\r\n
0x80000027 | The Network Access Protection Agent was unable to determine which HRAs to request a health certificate from.%nA network change or if GP is configured, a configuration change will prompt further attempts to acquire a health certificate. Otherwise no further attempts will be made.%nContact the HRA administrator for more information.\r\n
0xc0000001 | The System Health Agent %1 is installed but not registered with the NAP agent.\r\n
0xc0000002 | The System Health Agent %1 attempted to initialize, but failed because it has initialized already.\r\n
0xc0000003 | The System Health Agent %1 attempted to uninitialize but failed because it was not initialized. \r\n
0xc0000006 | The enforcement client %1 attempted to initialize but failed because it is not registered with the NAP agent.\r\n
0xc0000007 | The enforcement client %1 attempted to initialize but failed because it has already initialized. \r\n
0xc0000008 | The enforcement client %1 attempted to uninitialize but failed because it was not initialized.\r\n
0xc000000b | The System Health Agent %1 failed the call to %2.\r\n
0xc000000c | The enforcement client %1 failed the call to %2.\r\n
0xc000000d | The Network Access Protection Agent failed to load the peripheral component %1. The error code was %2.%n See the administrator for more information.%n\r\n
0xc000000e | A Statement of Health with correlation ID %1 could not be created because the maximum size of the connection is too small.\r\n
0xc0000010 | A packet has been received with an unexpected correlation of %1 instead of %2.\r\n
0xc0000011 | The Statement of Health Response received configuration for the following SHAs that are not installed on this computer: %1\r\n
0xc0000013 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The server was not available to service the request (%3). This server will not be tried again for %4 minutes.%n See the HRA administrator for more information.%n\r\n
0xc0000014 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The server denied access to the request (%3). This server will not be tried again for %4 minutes.%n See the HRA administrator for more information.%n\r\n
0xc0000015 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The request failed with the error code (%3). This server will not be tried again for %4 minutes.%n See the HRA administrator for more information.%n\r\n
0xc0000018 | The Network Access Protection Agent failed to delete the certificate with the thumbprint of %1.%n The certificate could not be found or the Network Access Protection Agent has insufficient privileges to delete the certificate (%2).%n See the administrator for more information.%n\r\n
0xc000001e | The System Health Agent %1 has returned an error code %2.\r\n
0xc000001f | The Network Access Protection agent failed to initialize the following enrollment configuration.%n    HRA Group           : %1%n    CSP Name            : %2%n    Key Specification   : %3%n    Key Length          : %4%n    Signature Algorithm : %5%nThe intialization failed with the error code (%6).%nSee the HRA administrator for more information.%n\r\n
0xc0000020 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The server was not available to service the request (%3).%n See the HRA administrator for more information.%n\r\n
0xc0000021 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The server denied access to the request (%3).%n See the HRA administrator for more information.%n\r\n
0xc0000022 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The request failed with the error code (%3).%n See the HRA administrator for more information.%n\r\n
0xc0000023 | The Network Access Protection agent failed to get a certificate for the request with correlation-id %2 from %1.%n\r\nThe server presented a certificate that is not trusted for Enterprise authentication. This server will not be tried again for %4 minutes.%n\r\nContact the HRA administrator for more information.%n\r\n
0xc0000024 | The Network Access Protection agent failed to get a certificate for the request with correlation-id %2 from %1.%n\r\nThe validation of the server certificate for SSL resulted in an error %3, the certificate is not appropriate for SSL. This server will not be tried again for %4 minutes.%n\r\nContact the HRA administrator for more information.%n\r\n
0xc0000025 | The Network Access Protection agent failed to get a certificate for the request with correlation-id %2 from %1.%n\r\nThe server presented a certificate that is not trusted for Enterprise authentication.%n\r\nContact the HRA administrator for more information.%n\r\n
0xc0000026 | The Network Access Protection agent failed to get a certificate for the request with correlation-id %2 from %1.%n\r\nThe validation of the server certificate for SSL resulted in an error %3, the certificate is not appropriate for SSL.%n\r\nContact the HRA administrator for more information.%n\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x90000001 | Microsoft-Windows-Network Access Protection\r\n
0x90000002 | Microsoft-Windows-NetworkAccessProtection/Operational\r\n
0xb0000001 | The System Health Agent %1 is installed but not registered with the NAP agent.\r\n
0xb0000002 | The System Health Agent %1 attempted to initialize, but failed because it has initialized already.\r\n
0xb0000003 | The System Health Agent %1 attempted to uninitialize but failed because it was not initialized.\r\n
0xb0000004 | The System Health Agent %1 successfully initialized.\r\n
0xb0000005 | The System Health Agent %1 successfully uninitialized.\r\n
0xb0000006 | The enforcement client %1 attempted to initialize but failed because it is not registered with the NAP agent.\r\n
0xb0000007 | The enforcement client %1 attempted to initialize but failed because it has already initialized.\r\n
0xb0000008 | The enforcement client %1 attempted to uninitialize but failed because it was not initialized.\r\n
0xb0000009 | The enforcement client %1 successfully initialized.\r\n
0xb000000a | The enforcement client %1 successfully uninitialized.\r\n
0xb000000b | The System Health Agent %1 failed the call to %2.\r\n
0xb000000c | The enforcement client %1 failed the call to %2.\r\n
0xb000000d | The Network Access Protection Agent failed to load the peripheral component %1. The error code was %2.%n See the administrator for more information.%n\r\n
0xb000000e | A Statement of Health with correlation ID %1 could not be created because the maximum size of the connection is too small.\r\n
0xb000000f | A Statement of Health Request with correlation ID %1 could not include the following System Health Agents in the statement of Health: %2\r\n
0xb0000010 | A packet has been received with an unexpected correlation of %1 instead of %2.\r\n
0xb0000011 | The Statement of Health Response received configuration for the following SHAs that are not installed on this computer: %1\r\n
0xb0000012 | System Isolation State Change.%n Previous : %n    State          : %1 (%2)%n    Probation Time : %3%n    Help URL       : %4%n Current : %n    State          : %5 (%6)%n    Probation Time : %7%n    Help URL       : %8%n\r\n
0xb0000013 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The server was not available to service the request (%3). This server will not be tried again for %4 minutes.%n See the HRA administrator for more information.%n\r\n
0xb0000014 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The server denied access to the request (%3). This server will not be tried again for %4 minutes.%n See the HRA administrator for more information.%n\r\n
0xb0000015 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The request failed with the error code (%3). This server will not be tried again for %4 minutes.%n See the HRA administrator for more information.%n\r\n
0xb0000016 | The Network Access Protection Agent successfully acquired a certificate for the request with the correlation-id %2 from %1.%n The certificate can be identified by its thumbprint of %3%n\r\n
0xb0000017 | The Network Access Protection Agent successfully deleted the certificate with the thumbprint of %1.%n The certificate has expired or the health state of the client has changed or a replacement certificate has been acquired.%n See the administrator for more information.%n\r\n
0xb0000018 | The Network Access Protection Agent failed to delete the certificate with the thumbprint of %1.%n The certificate could not be found or the Network Access Protection Agent has insufficient privileges to delete the certificate (%2).%n See the administrator for more information.%n\r\n
0xb0000019 | The client loaded NAP group policy.%n\r\n
0xb000001a | The NAP service has started.%n NAP has the following information for this computer:%n Computer name is %1.%n Domain status is: %2.%n The OS SKU is: %4.%n The service pack version is: %6.%n The processor type is: %5.%n\r\n
0xb000001b | A Statement of Health with correlation ID %1 was received from the System Health Agent %2. %n The duration to check the client's health was %3 ms.\r\n
0xb000001c | A Statement of Health with correlation ID %1 was sent to the enforcment client %2.\r\n
0xb000001d | A Statement of Health Response with correlation ID %1 was received from the enforcement client %2.%n The current client state is %3. %n The following SHAs report this client non-compliant: %4%n The following error categories were encountered: %5%n The probation expiration time is: %6%n The help URL is: %7%n The duration of health check was %8 ms.%n\r\n
0xb000001e | The System Health Agent %1 has returned an error code %2.\r\n
0xb000001f | The Network Access Protection agent failed to initialize the following enrollment configuration.%n    HRA Group           : %1%n    CSP Name            : %2%n    Key Specification   : %3%n    Key Length          : %4%n    Signature Algorithm : %5%nThe intialization failed with the error code (%6).%nSee the HRA administrator for more information.%n\r\n
0xb0000020 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The server was not available to service the request (%3).%n See the HRA administrator for more information.%n\r\n
0xb0000021 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The server denied access to the request (%3).%n See the HRA administrator for more information.%n\r\n
0xb0000022 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%n The request failed with the error code (%3).%n See the HRA administrator for more information.%n\r\n

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Network Access Protection\r\n
0x90000002 | Microsoft-Windows-NetworkAccessProtection/Operational\r\n
0x90000003 | Microsoft-Windows-NetworkAccessProtection/WHC\r\n
0xb0000001 | The System Health Agent %1 is installed but not registered with the NAP agent.\r\n
0xb0000002 | The System Health Agent %1 attempted to initialize, but failed because it has initialized already.\r\n
0xb0000003 | The System Health Agent %1 attempted to uninitialize but failed because it was not initialized.\r\n
0xb0000004 | The System Health Agent %1 successfully initialized.\r\n
0xb0000005 | The System Health Agent %1 successfully uninitialized.\r\n
0xb0000006 | The enforcement client %1 attempted to initialize but failed because it is not registered with the NAP agent.\r\n
0xb0000007 | The enforcement client %1 attempted to initialize but failed because it has already initialized.\r\n
0xb0000008 | The enforcement client %1 attempted to uninitialize but failed because it was not initialized.\r\n
0xb0000009 | The enforcement client %1 successfully initialized.\r\n
0xb000000a | The enforcement client %1 successfully uninitialized.\r\n
0xb000000b | Call to %2 on System Health Agent %1 failed with error %3.%nContact the administrator for more information.%n\r\n
0xb000000c | The enforcement client %1 failed the call to %2.\r\n
0xb000000d | The Network Access Protection Agent failed to load the peripheral component %1. The error code was %2.%nContact the administrator for more information.%n\r\n
0xb000000e | A Statement of Health with correlation ID %1 could not be created because the maximum size of the connection is too small.\r\n
0xb000000f | A Statement of Health Request with correlation ID %1 could not include the following System Health Agents in the statement of Health: %2\r\n
0xb0000010 | A packet has been received with an unexpected correlation of %1 instead of %2.\r\n
0xb0000011 | The Statement of Health Response received configuration for the following SHAs that are not installed on this computer: %1\r\n
0xb0000012 | System Isolation State Change.%n Previous : %n    State          : %1 (%2)%n    Probation Time : %3%n    Help URL       : %4%n Current : %n    State          : %5 (%6)%n    Probation Time : %7%n    Help URL       : %8%n\r\n
0xb0000013 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%nThe server was not available to service the request (%3). This server will not be tried again for %4 minutes.%nContact the HRA administrator for more information.%n\r\n
0xb0000014 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%nThe server denied access to the request (%3). This server will not be tried again for %4 minutes.%nContact the HRA administrator for more information.%n\r\n
0xb0000015 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%nThe request failed with the error code (%3). This server will not be tried again for %4 minutes.%nContact the HRA administrator for more information.%n\r\n
0xb0000016 | The Network Access Protection Agent successfully acquired a certificate for the request with the correlation-id %2 from %1.%nThe certificate can be identified by its thumbprint of %3%n\r\n
0xb0000017 | The Network Access Protection Agent successfully deleted the certificate with the thumbprint of %1.%nThe certificate has expired or the health state of the client has changed or a replacement certificate has been acquired.%nContact the administrator for more information.%n\r\n
0xb0000018 | The Network Access Protection Agent failed to delete the certificate with the thumbprint of %1.%nThe certificate could not be found or the Network Access Protection Agent has insufficient privileges to delete the certificate (%2).%nContact the administrator for more information.%n\r\n
0xb0000019 | The client loaded NAP group policy.%n\r\n
0xb000001a | The NAP service has started.%nNAP has the following information for this computer:%n Computer name is %1.%nDomain status is: %2.%nThe OS SKU is: %4.%nThe service pack version is: %6.%nThe processor type is: %5.%n\r\n
0xb000001b | A Statement of Health with correlation ID %1 was received from the System Health Agent %2. %n The duration to check the client's health was %3 ms.\r\n
0xb000001c | A Statement of Health with correlation ID %1 was sent to the enforcment client %2.\r\n
0xb000001d | A Statement of Health Response with correlation ID %1 was received from the enforcement client %2.%nThe current client state is %3. %n The following SHAs report this client non-compliant: %4%n The following error categories were encountered: %5%n The probation expiration time is: %6%n The help URL is: %7%n The duration of health check was %8 ms.%n\r\n
0xb000001e | The System Health Agent %1 has returned an error code %2.\r\n
0xb000001f | The Network Access Protection agent failed to initialize the following enrollment configuration.%n    HRA Group           : %1%n    CSP Name            : %2%n    Key Specification   : %3%n    Key Length          : %4%n    Signature Algorithm : %5%nThe intialization failed with the error code (%6).%nContact the HRA administrator for more information.%n\r\n
0xb0000020 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%nThe server was not available to service the request (%3).%nContact the HRA administrator for more information.%n\r\n
0xb0000021 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%nThe server denied access to the request (%3).%nContact the HRA administrator for more information.%n\r\n
0xb0000022 | The Network Access Protection Agent failed to acquire a certificate for the request with the correlation-id %2 from %1.%nThe request failed with the error code (%3).%nContact the HRA administrator for more information.%n\r\n
0xb0000023 | The Network Access Protection agent failed to get a certificate for the request with correlation-id %2 from %1.%nThe server presented a certificate that is not trusted for Enterprise authentication. This server will not be tried again for %4 minutes.%nContact the HRA administrator for more information.\r\n
0xb0000024 | The Network Access Protection agent failed to get a certificate for the request with correlation-id %2 from %1.%nThe validation of the server certificate for SSL resulted in an error %3, the certificate is not appropriate for SSL. This server will not be tried again for %4 minutes.%nContact the HRA administrator for more information.\r\n
0xb0000025 | The Network Access Protection agent failed to get a certificate for the request with correlation-id %2 from %1.%nThe server presented a certificate that is not trusted for Enterprise authentication.%nContact the HRA administrator for more information.\r\n
0xb0000026 | The Network Access Protection agent failed to get a certificate for the request with correlation-id %2 from %1.%nThe validation of the server certificate for SSL resulted in an error %3, the certificate is not appropriate for SSL.%nContact the HRA administrator for more information.\r\n
0xb0000027 | The Network Access Protection Agent was unable to determine which HRAs to request a health certificate from.%nA network change or if GP is configured, a configuration change will prompt further attempts to acquire a health certificate. Otherwise no further attempts will be made.%nContact the HRA administrator for more information.\r\n
0xb0000028 | The Network Access Protection Agent has dynamically discovered the following HRAs for this network (using the query %1):%n%2%nThe DNS servers in your configuration at the time this discovery took place included:%n%3\r\n
0xb0000029 | System Isolation State Change. Extended State details:%n Previous : %n    Extended State          : %1 (%2)%n Current : %n    Extended State          : %3 (%4)%n\r\n
0xb000002a | A Statement of Health Response with correlation ID %1 was just received from the enforcement client %2.%nThe extended state in that Statement of Health Response was %3.%n\r\n
0xb000002b | The Network Access Protection Agent failed to deposit a certificate for the request with the correlation-id %2 from %1.%nValidityPeriod of the certificate is below threshold (%3).%nContact the HRA administrator for more information.\r\n
0xb000002c | The Network Access Protection Agent received a Statement of Health Response with correlation ID %1, that specified a probation end time of %2. The probation end time is in the past, which indicates improper synchronization of the clocks on this machine and the server.\r\n
0xb0000064 | Sending Health Information to WHC: %2(%1)\r\n
0xb001001a | The NAP service has started.%nNAP has the following information for this computer:%n Computer name is %1.%nDomain status is: %2.%nThe build number is: %3.%nThe OS SKU is: %4.%nThe service pack version is: %5.%nThe processor type is: %6.%n\r\n
