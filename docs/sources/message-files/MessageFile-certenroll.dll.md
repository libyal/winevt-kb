## certenroll.dll

Path: %SystemRoot%\system32\certenroll.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x025a000e | Certificate enrollment for %1 received a %2 certificate from %3 when retrieving pending requests.\r\n
0x025a0015 | Certificate enrollment for %1 attempted to enroll for a %2 certificate from certification authority %3.  The request is pending.\r\n
0x025a0016 | Certificate enrollment for %1 attempted to renew a %2 certificate from certification authority %3.  The request is pending.\r\n
0x025a001c | Certificate enrollment for %1 successfully installed a %2 certificate when retrieving pending requests.  User interaction was required.\r\n
0x025a001d | Certificate enrollment for %1 reused the private key when requesting a %2 certificate.\r\n
0x025a0031 | Certificate enrollment for %1 successfully received a %2 certificate.\r\n
0x425a0004 | Certificate enrollment for %1 could not access local resources or retrieve %2 certificate template information (%3).  Enrollment was not performed.\r\n
0x425a0005 | Certificate enrollment for %1 could not find any valid certificate templates.  Enrollment was not performed.\r\n
0x425a0008 | Certificate enrollment for %1 removed pending certificate requests that have expired or are obsolete.\r\n
0x425a000a | Certificate enrollment for %1 archived or deleted, from the Personal certificate store, certificates that have expired, or been revoked or superseded.\r\n
0x425a0013 | Certificate enrollment for %1 successfully received a %2 certificate from certification authority %3.\r\n
0x425a0014 | Certificate enrollment for %1 successfully renewed a %2 certificate from certification authority %3.\r\n
0x425a0019 | Certificate enrollment for %1 failed to update the %2 certificate in the Personal certificate store due to one of the following: %n %tCannot find %2 certificate template from Active Directory.%n %tEnrollment access to this template is not allowed.\r\n
0x425a001b | Certificate enrollment for %1 was cancelled by the user.\r\n
0x425a001e | Certificate enrollment for %1 was cancelled by the user when requesting a %2 certificate.\r\n
0x425a0020 | Certificate enrollment for %1 attempted to retrieve a %2 certificate from %3.  The certificate request is still pending.\r\n
0x425a0021 | Certificate enrollment for %1 deleted certificates that have expired, or have been revoked or superseded from the user object in Active Directory.\r\n
0x425a0029 | To prevent simultaneous renewal or enrollment from another computer, certificate enrollment for %1 to renew or enroll for a %2 certificate has been skipped.\r\n
0x825a000b | Certificate enrollment for %1 could not find a certification authority in the enterprise.  Enrollment was not performed.\r\n
0x825a000c | Certificate enrollment for %1 encountered errors while retrieving information about the certification authority from Active Directory (%2). Enrollment was not performed.\r\n
0x825a000f | Certificate enrollment for %1 failed to retrieve certificate template information from the Active Directory (%2). Enrollment was not performed.\r\n
0x825a0011 | Certificate enrollment for %1 failed to enroll for a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0012 | Certificate enrollment for %1 failed to renew a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0022 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because the certificate template is used for smart cards and the cryptographic service provider (CSP) list is empty.\r\n
0x825a0025 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because strong private key protection is required on the new private key that will be generated and computer certificates do not support strong private key protection.\r\n
0x825a0026 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because user interaction is required on the %2 template in Active Directory.\r\n
0x825a0027 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because a password is required to access the associated private key of a valid signing certificate and computer certificates do not support strong private key protection.\r\n
0x825a0028 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because a password is required to access the associated private key of a valid signing certificate and the user interaction requirement is not enabled on the %2 template in Active Directory.\r\n
0x825a002a | Certificate enrollment for %1 for the %2 template must be performed by using the machine context.\r\n
0x825a002b | Certificate enrollment for %1 failed to find a smart card reader for the %2 template.  Enrollment will not be performed.\r\n
0x825a002c | Certificate enrollment for %1 failed to open the user interface (%2).\r\n
0x825a002e | Certificate enrollment for %1 could not enroll for a %2 certificate.  Read or enrollment access is not allowed for this template.\r\n
0x825a002f | Certificate enrollment for %1 could not enroll for a %2 certificate.  A valid certification authority cannot be found to issue this template.\r\n
0x825a0030 | Certificate enrollment for %1 could not enroll for a %2 certificate.  Signature requirements for the certificate cannot be met.\r\n
0x825a0032 | Certificate enrollment for %1 failed to install the certificate response for a %2 certificate (%3).\r\n
0x825a0033 | Certificate enrollment for %1 for the %2 certificate must be performed under the user context.\r\n
0x825a0034 | The CA certificate for %3 is not trusted. Certificate enrollment for %1 for a %2 certificate failed.\r\n
0x825a0035 | Certificate enrollment for %1 failed to retrieve a %2 certificate from certification authority %3, and the error returned from the server is %4.  Another certification authority will be contacted.\r\n
0x825a0036 | Certificate enrollment for %1 failed to retrieve a pending %2 certificate from certification authority %3 (%4). The enrollment process will be attempted again later.\r\n
0x825a0037 | Certificate enrollment for %1 for the %2 template could not find specified CSPs on the local machine.  Enrollment will not be performed.\r\n
0x90000001 | Microsoft-Windows-CertificateServicesClient-CertEnroll\r\n
0xc25a0006 | Certificate enrollment for %1 could not find a valid certificate template to match %2.  Enrollment was not performed.\r\n
0xc25a0009 | Certificate enrollment for %1 was denied by %3 when retrieving the pending request for a %2 certificate.\r\n
0xc25a000d | Certificate enrollment for %1 failed to enroll for a %2 certificate from %3 (%4).\r\n
0xc25a0010 | Certificate enrollment for %1 failed to renew a %2 certificate (%3).\r\n
0xc25a0017 | Certificate enrollment for %1 failed to renew a %2 certificate because it cannot find a certification authority to issue the certificate template.\r\n
0xc25a0018 | Certificate enrollment for %1 failed to enroll for a %2 certificate because it cannot find a certification authority to issue the certificate.\r\n
0xc25a001a | Certificate enrollment for %1 failed to show the user notification balloon (%2).\r\n
0xc25a001f | Certificate enrollment for %1 failed to install a %2 certificate when retrieving pending requests (%3).\r\n
0xc25a0023 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  A new enrollment for a %2 certificate will be attempted in %3 hours.\r\n
0xc25a0024 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  No more enrollments for %2 certificates will be attempted until the current certificate is revoked or expires because the same error has occurred %3 times.\r\n
0xc25a002d | Certificate enrollment for %1 failed to create an enrollment request for a %2 certificate (%3).\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x025a000e | Certificate enrollment for %1 received a %2 certificate with request ID %4 from %3 when retrieving pending requests.\r\n
0x025a0015 | Certificate enrollment for %1 attempted to enroll for a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x025a0016 | Certificate enrollment for %1 attempted to renew a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x025a001c | Certificate enrollment for %1 successfully installed a %2 certificate when retrieving pending requests.  User interaction was required.\r\n
0x025a001d | Certificate enrollment for %1 reused the private key when requesting a %2 certificate.\r\n
0x025a0031 | Certificate enrollment for %1 successfully received a %2 certificate.\r\n
0x10000038 | Classic\r\n
0x425a0004 | Certificate enrollment for %1 could not access local resources or retrieve %2 certificate template information (%3).  Enrollment was not performed.\r\n
0x425a0005 | Certificate enrollment for %1 could not find any valid certificate templates.  Enrollment was not performed.\r\n
0x425a0008 | Certificate enrollment for %1 removed pending certificate requests that have expired or are obsolete.\r\n
0x425a000a | Certificate enrollment for %1 archived or deleted, from the Personal certificate store, certificates that have expired, or been revoked or superseded.\r\n
0x425a0013 | Certificate enrollment for %1 successfully received a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0014 | Certificate enrollment for %1 successfully renewed a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0019 | Certificate enrollment for %1 failed to update the %2 certificate in the Personal certificate store due to one of the following: %n %tCannot find %2 certificate template from Active Directory.%n %tEnrollment access to this template is not allowed.\r\n
0x425a001b | Certificate enrollment for %1 was cancelled by the user.\r\n
0x425a001e | Certificate enrollment for %1 was cancelled by the user when requesting a %2 certificate.\r\n
0x425a0020 | Certificate enrollment for %1 attempted to retrieve a %2 certificate from %3.  The certificate request is still pending.\r\n
0x425a0021 | Certificate enrollment for %1 deleted certificates that have expired, or have been revoked or superseded from the user object in Active Directory.\r\n
0x425a0029 | To prevent simultaneous renewal or enrollment from another computer, certificate enrollment for %1 to renew or enroll for a %2 certificate has been skipped.\r\n
0x425a0038 | Certificate enrollment for %1 for the template %2 was not performed because this template has been superseded.\r\n
0x825a000b | Certificate enrollment for %1 could not find a certification authority in the enterprise.  Enrollment was not performed.\r\n
0x825a000c | Certificate enrollment for %1 encountered errors while retrieving information about the certification authority from Active Directory (%2). Enrollment was not performed.\r\n
0x825a000f | Certificate enrollment for %1 failed to retrieve certificate template information from the Active Directory (%2). Enrollment was not performed.\r\n
0x825a0011 | Certificate enrollment for %1 failed to enroll for a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0012 | Certificate enrollment for %1 failed to renew a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0022 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because the certificate template is used for smart cards and the cryptographic service provider (CSP) list is empty.\r\n
0x825a0025 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because strong private key protection is required on the new private key that will be generated and computer certificates do not support strong private key protection.\r\n
0x825a0026 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because user interaction is required on the %2 template in Active Directory.\r\n
0x825a0027 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because a password is required to access the associated private key of a valid signing certificate and computer certificates do not support strong private key protection.\r\n
0x825a0028 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because a password is required to access the associated private key of a valid signing certificate and the user interaction requirement is not enabled on the %2 template in Active Directory.\r\n
0x825a002a | Certificate enrollment for %1 for the %2 template must be performed by using the machine context.\r\n
0x825a002b | Certificate enrollment for %1 failed to find a smart card reader for the %2 template.  Enrollment will not be performed.\r\n
0x825a002c | Certificate enrollment for %1 failed to open the user interface (%2).\r\n
0x825a002e | Certificate enrollment for %1 could not enroll for a %2 certificate.  Read or enrollment access is not allowed for this template.\r\n
0x825a002f | Certificate enrollment for %1 could not enroll for a %2 certificate.  A valid certification authority cannot be found to issue this template.\r\n
0x825a0030 | Certificate enrollment for %1 could not enroll for a %2 certificate.  Signature requirements for the certificate cannot be met.\r\n
0x825a0032 | Certificate enrollment for %1 failed to install the certificate response for a %2 certificate with request ID %3 (%4).\r\n
0x825a0033 | Certificate enrollment for %1 for the %2 certificate must be performed under the user context.\r\n
0x825a0034 | The CA certificate for %3 is not trusted. Certificate enrollment for %1 for a %2 certificate failed.\r\n
0x825a0035 | Certificate enrollment for %1 failed to retrieve a %2 certificate from certification authority %3 with request ID %4, and the error returned from the server is %5.  Another certification authority will be contacted.\r\n
0x825a0036 | Certificate enrollment for %1 failed to retrieve a pending %2 certificate with request ID %4 from certification authority %3 (%5). The enrollment process will be attempted again later.\r\n
0x825a0037 | Certificate enrollment for %1 for the %2 template could not find specified CSPs on the local machine.  Enrollment will not be performed.\r\n
0x825a0039 | The "%2" provider was not loaded because initialization failed.\r\n
0x825a003a | The "%3" algorithm for the "%2" provider was not loaded because initialization failed.\r\n
0x825a003b | Could not determine the signature algorithm for %2 to sign an enrollment request.\r\n
0x825a003c | Could not find a registered public key algorithm OID for %2 for an enrollment request.\r\n
0x825a003d | Could not find a registered signature algorithm OID for %1 and %2 to sign an enrollment request.\r\n
0x825a003e | Could not encode signature parameters for a %2 signature for an enrollment request.\r\n
0x825a003f | Enrollment Policy Server %2 returned an error when retrieving templates for %1: %3\r\n
0x825a0040 | Certificate enrollment for %1 successfully load policy from policy server %2\r\n
0x825a0041 | Certificate enrollment for %1 is successfully authenticated by policy server %2\r\n
0x825a0042 | Certificate enrollment for %1 is successfully authenticated by enrollment server %2\r\n
0x825a0043 | Certificate enrollment for %1 failed to load policy from policy servers with ID  %2 (%3)\r\n
0x825a0044 | Certificate enrollment for %1 failed in authentication to policy servers with ID %2  (%3)\r\n
0x825a0046 | Certificate enrollment for %1 failed because no valid policy can be obtained from policy servers with ID %2\r\n
0x825a0047 | Certificate enrollment for %1 failed in adding credential to Vault for %2 (%3)\r\n
0x825a0048 | Certificate enrollment for %1 failed because the loaded policy from the policy server %2 is invalid (%3)\r\n
0x825a0049 | Certificate auto enrollment for %1 cannot be done because the policy server %2 turns it off.\r\n
0x825a004a | Certificate enrollment for %1 failed to load policy from policy server %2 with ID  %3 (%4)\r\n
0x825a004b | Certificate enrollment for %1 failed in authentication to policy server %2 with ID  %3 (%4)\r\n
0x825a004c | Certificate enrollment for %1 failed in authentication to enrollment server %2 (%3)\r\n
0x825a004d | Certificate enrollment for %1 cannot enroll from user configured enrollment policy server since it is disabled by group policy\r\n
0x825a004e | Certificate enrollment for %1 sent a request for template %2 to a ROBO certificate enrollment server %3\r\n
0x825a004f | Certificate enrollment for %1 sent a request for templae %2 to a ANONYMOUS certificate enrollment server %3\r\n
0x825a0050 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ROBO and only renewal is supported\r\n
0x825a0051 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ANONYMOUS and only renewal is supported\r\n
0x90000001 | Microsoft-Windows-CertificateServicesClient-CertEnroll\r\n
0x90000002 | Application\r\n
0xc25a0006 | Certificate enrollment for %1 could not find a valid certificate template to match %2.  Enrollment was not performed.\r\n
0xc25a0009 | Certificate enrollment for %1 was denied by %3 when retrieving the pending request for a %2 certificate with request ID %4.\r\n
0xc25a000d | Certificate enrollment for %1 failed to enroll for a %2 certificate with request ID %4 from %3 (%5).\r\n
0xc25a0010 | Certificate enrollment for %1 failed to renew a %2 certificate with request ID %4 from %3 (%5).\r\n
0xc25a0017 | Certificate enrollment for %1 failed to renew a %2 certificate because it cannot find a certification authority to issue the certificate template.\r\n
0xc25a0018 | Certificate enrollment for %1 failed to enroll for a %2 certificate because it cannot find a certification authority to issue the certificate.\r\n
0xc25a001a | Certificate enrollment for %1 failed to show the user notification balloon (%2).\r\n
0xc25a001f | Certificate enrollment for %1 failed to install a %2 certificate when retrieving pending requests (%3).\r\n
0xc25a0023 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  A new enrollment for a %2 certificate will be attempted in %3 hours.\r\n
0xc25a0024 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  No more enrollments for %2 certificates will be attempted until the current certificate is revoked or expires because the same error has occurred %3 times.\r\n
0xc25a002d | Certificate enrollment for %1 failed to create an enrollment request for a %2 certificate (%3).\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x025a000e | Certificate enrollment for %1 received a %2 certificate with request ID %4 from %3 when retrieving pending requests.\r\n
0x025a0015 | Certificate enrollment for %1 attempted to enroll for a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x025a0016 | Certificate enrollment for %1 attempted to renew a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x10000038 | Classic\r\n
0x425a0004 | Certificate enrollment for %1 could not access local resources or retrieve %2 certificate template information (%3).  Enrollment was not performed.\r\n
0x425a0005 | Certificate enrollment for %1 could not find any valid certificate templates.  Enrollment was not performed.\r\n
0x425a000a | Certificate enrollment for %1 archived or deleted, from the Personal certificate store, certificates that have expired, or been revoked or superseded.\r\n
0x425a0013 | Certificate enrollment for %1 successfully received a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0014 | Certificate enrollment for %1 successfully renewed a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0019 | Certificate enrollment for %1 failed to update the %2 certificate in the Personal certificate store due to one of the following: %n %tCannot find %2 certificate template from Active Directory.%n %tEnrollment access to this template is not allowed.\r\n
0x425a001b | Certificate enrollment for %1 was cancelled by the user.\r\n
0x425a001e | Certificate enrollment for %1 was cancelled by the user when requesting a %2 certificate.\r\n
0x425a0020 | Certificate enrollment for %1 attempted to retrieve a %2 certificate from %3.  The certificate request is still pending.\r\n
0x425a0021 | Certificate enrollment for %1 deleted certificates that have expired, or have been revoked or superseded from the user object in Active Directory.\r\n
0x425a0029 | To prevent simultaneous renewal or enrollment from another computer, certificate enrollment for %1 to renew or enroll for a %2 certificate has been skipped.\r\n
0x425a0038 | Certificate enrollment for %1 for the template %2 was not performed because this template has been superseded.\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x825a000b | Certificate enrollment for %1 could not find a certification authority in the enterprise.  Enrollment was not performed.\r\n
0x825a000f | Certificate enrollment for %1 failed to retrieve certificate template information from the Active Directory (%2). Enrollment was not performed.\r\n
0x825a0011 | Certificate enrollment for %1 failed to enroll for a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0012 | Certificate enrollment for %1 failed to renew a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0026 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because user interaction is required on the %2 template in Active Directory.\r\n
0x825a002a | Certificate enrollment for %1 for the %2 template must be performed by using the machine context.\r\n
0x825a002b | Certificate enrollment for %1 failed to find a smart card reader for the %2 template.  Enrollment will not be performed.\r\n
0x825a002c | Certificate enrollment for %1 failed to open the user interface (%2).\r\n
0x825a002e | Certificate enrollment for %1 could not enroll for a %2 certificate.  Read or enrollment access is not allowed for this template.\r\n
0x825a002f | Certificate enrollment for %1 could not enroll for a %2 certificate.  A valid certification authority cannot be found to issue this template.\r\n
0x825a0030 | Certificate enrollment for %1 could not enroll for a %2 certificate.  Signature requirements for the certificate cannot be met.\r\n
0x825a0032 | Certificate enrollment for %1 failed to install the certificate response for a %2 certificate with request ID %3 (%4).\r\n
0x825a0033 | Certificate enrollment for %1 for the %2 certificate must be performed under the user context.\r\n
0x825a0034 | The CA certificate for %3 is not trusted. Certificate enrollment for %1 for a %2 certificate failed.\r\n
0x825a0035 | Certificate enrollment for %1 failed to retrieve a %2 certificate from certification authority %3 with request ID %4, and the error returned from the server is %5.  Another certification authority will be contacted.\r\n
0x825a0036 | Certificate enrollment for %1 failed to retrieve a pending %2 certificate with request ID %4 from certification authority %3 (%5). The enrollment process will be attempted again later.\r\n
0x825a0037 | Certificate enrollment for %1 for the %2 template could not find specified CSPs on the local machine.  Enrollment will not be performed.\r\n
0x825a0039 | The "%2" provider was not loaded because initialization failed.\r\n
0x825a003a | The "%3" algorithm for the "%2" provider was not loaded because initialization failed.\r\n
0x825a003b | Could not determine the signature algorithm for %2 to sign an enrollment request.\r\n
0x825a003c | Could not find a registered public key algorithm OID for %2 for an enrollment request.\r\n
0x825a003d | Could not find a registered signature algorithm OID for %1 and %2 to sign an enrollment request.\r\n
0x825a003e | Could not encode signature parameters for a %2 signature for an enrollment request.\r\n
0x825a003f | Enrollment Policy Server %2 returned an error when retrieving templates for %1: %3\r\n
0x825a0040 | Certificate enrollment for %1 successfully load policy from policy server %2\r\n
0x825a0041 | Certificate enrollment for %1 is successfully authenticated by policy server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0042 | Certificate enrollment for %1 is successfully authenticated by enrollment server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0043 | Certificate enrollment for %1 failed to load policy from policy servers with ID  %2 (%3)\r\n
0x825a0044 | Certificate enrollment for %1 failed in authentication to policy servers with ID %2  (%3)\r\n
0x825a0046 | Certificate enrollment for %1 failed because no valid policy can be obtained from policy servers with ID %2\r\n
0x825a0047 | Certificate enrollment for %1 failed in adding credential to Vault for %2 (%3)\r\n
0x825a0048 | Certificate enrollment for %1 failed because the loaded policy from the policy server %2 is invalid (%3)\r\n
0x825a0049 | Certificate auto enrollment for %1 cannot be done because the policy server %2 turns it off.\r\n
0x825a004a | Certificate enrollment for %1 failed to load policy from policy server %2 with ID  %3 (%4)\r\n
0x825a004b | Certificate enrollment for %1 failed in authentication to policy server %2 with ID  %3 (%6). Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004c | Certificate enrollment for %1 failed in authentication to enrollment server %2 (%6). Policy Id: %3. Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004d | Certificate enrollment for %1 cannot enroll from user configured enrollment policy server since it is disabled by group policy\r\n
0x825a004e | Certificate enrollment for %1 sent a request for template %2 to a ROBO certificate enrollment server %3\r\n
0x825a004f | Certificate enrollment for %1 sent a request for template %2 to a ANONYMOUS certificate enrollment server %3\r\n
0x825a0050 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ROBO and only renewal is supported\r\n
0x825a0051 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ANONYMOUS and only renewal is supported\r\n
0x825a0052 | Certificate enrollment for %1 failed in authentication to all urls for enrollment server associated with policy id: %2 (%4). Failed to enroll for template: %3\r\n
0x825a0053 | Certificate enrollment for %1 cannot find a credential that meets the selection criteria for url %2 with id %3 (%4)\r\n
0x825a0054 | The credential for URL %2 has been updated from certificate (%4) to certificate (%3) in context %1\r\n
0x90000001 | Microsoft-Windows-CertificateServicesClient-CertEnroll\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-System\r\n
0x92000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-User\r\n
0xb10003e9 | A certificate has been replaced. Please refer to the "Details" section for more information.\r\n
0xb10003ea | A certificate has expired. Please refer to the "Details" section for more information.\r\n
0xb10003eb | A certificate is about to expire. Please refer to the "Details" section for more information.\r\n
0xb10003ec | A certificate has been deleted. Please refer to the "Details" section for more information.\r\n
0xb10003ed | A certificate has been archived. Please refer to the "Details" section for more information.\r\n
0xb10003ee | A new certificate has been installed. Please refer to the "Details" section for more information.\r\n
0xb10003ef | A certificate has been exported. Please refer to the "Details" section for more information.\r\n
0xb10003f0 | A certificate has been associated with its private key. Please refer to the "Details" section for more information.\r\n
0xb10003f1 | A certificate could not be associated with its private key. Please refer to the "Details" section for more information.\r\n
0xc25a0006 | Certificate enrollment for %1 could not find a valid certificate template to match %2.  Enrollment was not performed.\r\n
0xc25a0009 | Certificate enrollment for %1 was denied by %3 when retrieving the pending request for a %2 certificate with request ID %4.\r\n
0xc25a000d | Certificate enrollment for %1 failed to enroll for a %2 certificate with request ID %4 from %3 (%5).\r\n
0xc25a0010 | Certificate enrollment for %1 failed to renew a %2 certificate with request ID %4 from %3 (%6). The certificate which failed to renew is %5\r\n
0xc25a0023 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  A new enrollment for a %2 certificate will be attempted in %3 hours.\r\n
0xc25a0024 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  No more enrollments for %2 certificates will be attempted until the current certificate is revoked or expires because the same error has occurred %3 times.\r\n
0xc25a002d | Certificate enrollment for %1 failed to create an enrollment request for a %2 certificate (%3).\r\n

### 6.3.9600.16384, 10.0.10586.0

Message identifier | Message string
--- | ---
0x025a000e | Certificate enrollment for %1 received a %2 certificate with request ID %4 from %3 when retrieving pending requests.\r\n
0x025a0015 | Certificate enrollment for %1 attempted to enroll for a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x025a0016 | Certificate enrollment for %1 attempted to renew a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x10000038 | Classic\r\n
0x425a0004 | Certificate enrollment for %1 could not access local resources or retrieve %2 certificate template information (%3).  Enrollment was not performed.\r\n
0x425a0005 | Certificate enrollment for %1 could not find any valid certificate templates.  Enrollment was not performed.\r\n
0x425a000a | Certificate enrollment for %1 archived or deleted, from the Personal certificate store, certificates that have expired, or been revoked or superseded.\r\n
0x425a0013 | Certificate enrollment for %1 successfully received a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0014 | Certificate enrollment for %1 successfully renewed a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0019 | Certificate enrollment for %1 failed to update the %2 certificate in the Personal certificate store due to one of the following: %n %tCannot find %2 certificate template from Active Directory.%n %tEnrollment access to this template is not allowed.\r\n
0x425a001b | Certificate enrollment for %1 was cancelled by the user.\r\n
0x425a001e | Certificate enrollment for %1 was cancelled by the user when requesting a %2 certificate.\r\n
0x425a0020 | Certificate enrollment for %1 attempted to retrieve a %2 certificate from %3.  The certificate request is still pending.\r\n
0x425a0021 | Certificate enrollment for %1 deleted certificates that have expired, or have been revoked or superseded from the user object in Active Directory.\r\n
0x425a0029 | To prevent simultaneous renewal or enrollment from another computer, certificate enrollment for %1 to renew or enroll for a %2 certificate has been skipped.\r\n
0x425a0038 | Certificate enrollment for %1 for the template %2 was not performed because this template has been superseded.\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x825a000b | Certificate enrollment for %1 could not find a certification authority in the enterprise.  Enrollment was not performed.\r\n
0x825a000f | Certificate enrollment for %1 failed to retrieve certificate template information from the Active Directory (%2). Enrollment was not performed.\r\n
0x825a0011 | Certificate enrollment for %1 failed to enroll for a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0012 | Certificate enrollment for %1 failed to renew a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0026 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because user interaction is required on the %2 template in Active Directory.\r\n
0x825a002a | Certificate enrollment for %1 for the %2 template must be performed by using the machine context.\r\n
0x825a002b | Certificate enrollment for %1 failed to find a smart card reader for the %2 template.  Enrollment will not be performed.\r\n
0x825a002c | Certificate enrollment for %1 failed to open the user interface (%2).\r\n
0x825a002e | Certificate enrollment for %1 could not enroll for a %2 certificate.  Read or enrollment access is not allowed for this template.\r\n
0x825a002f | Certificate enrollment for %1 could not enroll for a %2 certificate.  A valid certification authority cannot be found to issue this template.\r\n
0x825a0030 | Certificate enrollment for %1 could not enroll for a %2 certificate.  Signature requirements for the certificate cannot be met.\r\n
0x825a0032 | Certificate enrollment for %1 failed to install the certificate response for a %2 certificate with request ID %3 (%4).\r\n
0x825a0033 | Certificate enrollment for %1 for the %2 certificate must be performed under the user context.\r\n
0x825a0034 | The CA certificate for %3 is not trusted. Certificate enrollment for %1 for a %2 certificate failed.\r\n
0x825a0035 | Certificate enrollment for %1 failed to retrieve a %2 certificate from certification authority %3 with request ID %4, and the error returned from the server is %5.  Another certification authority will be contacted.\r\n
0x825a0036 | Certificate enrollment for %1 failed to retrieve a pending %2 certificate with request ID %4 from certification authority %3 (%5). The enrollment process will be attempted again later.\r\n
0x825a0037 | Certificate enrollment for %1 for the %2 template could not find specified CSPs on the local machine.  Enrollment will not be performed.\r\n
0x825a0039 | The "%2" provider was not loaded because initialization failed.\r\n
0x825a003a | The "%3" algorithm for the "%2" provider was not loaded because initialization failed.\r\n
0x825a003b | Could not determine the signature algorithm for %2 to sign an enrollment request.\r\n
0x825a003c | Could not find a registered public key algorithm OID for %2 for an enrollment request.\r\n
0x825a003d | Could not find a registered signature algorithm OID for %1 and %2 to sign an enrollment request.\r\n
0x825a003e | Could not encode signature parameters for a %2 signature for an enrollment request.\r\n
0x825a003f | Enrollment Policy Server %2 returned an error when retrieving templates for %1: %3\r\n
0x825a0040 | Certificate enrollment for %1 successfully load policy from policy server %2\r\n
0x825a0041 | Certificate enrollment for %1 is successfully authenticated by policy server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0042 | Certificate enrollment for %1 is successfully authenticated by enrollment server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0043 | Certificate enrollment for %1 failed to load policy from policy servers with ID  %2 (%3)\r\n
0x825a0044 | Certificate enrollment for %1 failed in authentication to policy servers with ID %2  (%3)\r\n
0x825a0046 | Certificate enrollment for %1 failed because no valid policy can be obtained from policy servers with ID %2\r\n
0x825a0047 | Certificate enrollment for %1 failed in adding credential to Vault for %2 (%3)\r\n
0x825a0048 | Certificate enrollment for %1 failed because the loaded policy from the policy server %2 is invalid (%3)\r\n
0x825a0049 | Certificate auto enrollment for %1 cannot be done because the policy server %2 turns it off.\r\n
0x825a004a | Certificate enrollment for %1 failed to load policy from policy server %2 with ID  %3 (%4)\r\n
0x825a004b | Certificate enrollment for %1 failed in authentication to policy server %2 with ID  %3 (%6). Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004c | Certificate enrollment for %1 failed in authentication to enrollment server %2 (%6). Policy Id: %3. Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004d | Certificate enrollment for %1 cannot enroll from user configured enrollment policy server since it is disabled by group policy\r\n
0x825a004e | Certificate enrollment for %1 sent a request for template %2 to a ROBO certificate enrollment server %3\r\n
0x825a004f | Certificate enrollment for %1 sent a request for template %2 to a ANONYMOUS certificate enrollment server %3\r\n
0x825a0050 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ROBO and only renewal is supported\r\n
0x825a0051 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ANONYMOUS and only renewal is supported\r\n
0x825a0052 | Certificate enrollment for %1 failed in authentication to all urls for enrollment server associated with policy id: %2 (%4). Failed to enroll for template: %3\r\n
0x825a0053 | Certificate enrollment for %1 cannot find a credential that meets the selection criteria for url %2 with id %3 (%4)\r\n
0x825a0054 | The credential for URL %2 has been updated from certificate (%4) to certificate (%3) in context %1\r\n
0x825a0055 | Certificate enrollment for %1 for the %2 template could not perform attestation due to an error with the cryptographic hardware using the provider: %3. Request Id: %4.%5\r\n
0x90000001 | Microsoft-Windows-CertificateServicesClient-CertEnroll\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-System\r\n
0x92000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-User\r\n
0xb10003e9 | A certificate has been replaced. Please refer to the "Details" section for more information.\r\n
0xb10003ea | A certificate has expired. Please refer to the "Details" section for more information.\r\n
0xb10003eb | A certificate is about to expire. Please refer to the "Details" section for more information.\r\n
0xb10003ec | A certificate has been deleted. Please refer to the "Details" section for more information.\r\n
0xb10003ed | A certificate has been archived. Please refer to the "Details" section for more information.\r\n
0xb10003ee | A new certificate has been installed. Please refer to the "Details" section for more information.\r\n
0xb10003ef | A certificate has been exported. Please refer to the "Details" section for more information.\r\n
0xb10003f0 | A certificate has been associated with its private key. Please refer to the "Details" section for more information.\r\n
0xb10003f1 | A certificate could not be associated with its private key. Please refer to the "Details" section for more information.\r\n
0xc25a0006 | Certificate enrollment for %1 could not find a valid certificate template to match %2.  Enrollment was not performed.\r\n
0xc25a0009 | Certificate enrollment for %1 was denied by %3 when retrieving the pending request for a %2 certificate with request ID %4.\r\n
0xc25a000d | Certificate enrollment for %1 failed to enroll for a %2 certificate with request ID %4 from %3 (%5).\r\n
0xc25a0010 | Certificate enrollment for %1 failed to renew a %2 certificate with request ID %4 from %3 (%6). The certificate which failed to renew is %5\r\n
0xc25a0023 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  A new enrollment for a %2 certificate will be attempted in %3 hours.\r\n
0xc25a0024 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  No more enrollments for %2 certificates will be attempted until the current certificate is revoked or expires because the same error has occurred %3 times.\r\n
0xc25a002d | Certificate enrollment for %1 failed to create an enrollment request for a %2 certificate (%3).\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x025a000e | Certificate enrollment for %1 received a %2 certificate with request ID %4 from %3 when retrieving pending requests.\r\n
0x025a0015 | Certificate enrollment for %1 attempted to enroll for a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x025a0016 | Certificate enrollment for %1 attempted to renew a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x10000038 | Classic\r\n
0x425a0004 | Certificate enrollment for %1 could not access local resources or retrieve %2 certificate template information (%3).  Enrollment was not performed.\r\n
0x425a0005 | Certificate enrollment for %1 could not find any valid certificate templates.  Enrollment was not performed.\r\n
0x425a000a | Certificate enrollment for %1 archived or deleted, from the Personal certificate store, certificates that have expired, or been revoked or superseded.\r\n
0x425a0013 | Certificate enrollment for %1 successfully received a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0014 | Certificate enrollment for %1 successfully renewed a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0019 | Certificate enrollment for %1 failed to update the %2 certificate in the Personal certificate store due to one of the following: %n %tCannot find %2 certificate template from Active Directory.%n %tEnrollment access to this template is not allowed.\r\n
0x425a001b | Certificate enrollment for %1 was cancelled by the user.\r\n
0x425a001e | Certificate enrollment for %1 was cancelled by the user when requesting a %2 certificate.\r\n
0x425a0020 | Certificate enrollment for %1 attempted to retrieve a %2 certificate from %3.  The certificate request is still pending.\r\n
0x425a0021 | Certificate enrollment for %1 deleted certificates that have expired, or have been revoked or superseded from the user object in Active Directory.\r\n
0x425a0029 | To prevent simultaneous renewal or enrollment from another computer, certificate enrollment for %1 to renew or enroll for a %2 certificate has been skipped.\r\n
0x425a0038 | Certificate enrollment for %1 for the template %2 was not performed because this template has been superseded.\r\n
0x425a0058 | SCEP Certificate enrollment for %1 via %2 succeeded:%n%n%3%nMethod: %4%nStage: %5\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x825a000b | Certificate enrollment for %1 could not find a certification authority in the enterprise.  Enrollment was not performed.\r\n
0x825a000f | Certificate enrollment for %1 failed to retrieve certificate template information from the Active Directory (%2). Enrollment was not performed.\r\n
0x825a0011 | Certificate enrollment for %1 failed to enroll for a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0012 | Certificate enrollment for %1 failed to renew a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0026 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because user interaction is required on the %2 template in Active Directory.\r\n
0x825a002a | Certificate enrollment for %1 for the %2 template must be performed by using the machine context.\r\n
0x825a002b | Certificate enrollment for %1 failed to find a smart card reader for the %2 template.  Enrollment will not be performed.\r\n
0x825a002c | Certificate enrollment for %1 failed to open the user interface (%2).\r\n
0x825a002e | Certificate enrollment for %1 could not enroll for a %2 certificate.  Read or enrollment access is not allowed for this template.\r\n
0x825a002f | Certificate enrollment for %1 could not enroll for a %2 certificate.  A valid certification authority cannot be found to issue this template.\r\n
0x825a0030 | Certificate enrollment for %1 could not enroll for a %2 certificate.  Signature requirements for the certificate cannot be met.\r\n
0x825a0032 | Certificate enrollment for %1 failed to install the certificate response for a %2 certificate with request ID %3 (%4).\r\n
0x825a0033 | Certificate enrollment for %1 for the %2 certificate must be performed under the user context.\r\n
0x825a0034 | The CA certificate for %3 is not trusted. Certificate enrollment for %1 for a %2 certificate failed.\r\n
0x825a0035 | Certificate enrollment for %1 failed to retrieve a %2 certificate from certification authority %3 with request ID %4, and the error returned from the server is %5.  Another certification authority will be contacted.\r\n
0x825a0036 | Certificate enrollment for %1 failed to retrieve a pending %2 certificate with request ID %4 from certification authority %3 (%5). The enrollment process will be attempted again later.\r\n
0x825a0037 | Certificate enrollment for %1 for the %2 template could not find specified CSPs on the local machine.  Enrollment will not be performed.\r\n
0x825a0039 | The "%2" provider was not loaded because initialization failed.\r\n
0x825a003a | The "%3" algorithm for the "%2" provider was not loaded because initialization failed.\r\n
0x825a003b | Could not determine the signature algorithm for %2 to sign an enrollment request.\r\n
0x825a003c | Could not find a registered public key algorithm OID for %2 for an enrollment request.\r\n
0x825a003d | Could not find a registered signature algorithm OID for %1 and %2 to sign an enrollment request.\r\n
0x825a003e | Could not encode signature parameters for a %2 signature for an enrollment request.\r\n
0x825a003f | Enrollment Policy Server %2 returned an error when retrieving templates for %1: %3\r\n
0x825a0040 | Certificate enrollment for %1 successfully load policy from policy server %2\r\n
0x825a0041 | Certificate enrollment for %1 is successfully authenticated by policy server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0042 | Certificate enrollment for %1 is successfully authenticated by enrollment server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0043 | Certificate enrollment for %1 failed to load policy from policy servers with ID  %2 (%3)\r\n
0x825a0044 | Certificate enrollment for %1 failed in authentication to policy servers with ID %2  (%3)\r\n
0x825a0046 | Certificate enrollment for %1 failed because no valid policy can be obtained from policy servers with ID %2\r\n
0x825a0047 | Certificate enrollment for %1 failed in adding credential to Vault for %2 (%3)\r\n
0x825a0048 | Certificate enrollment for %1 failed because the loaded policy from the policy server %2 is invalid (%3)\r\n
0x825a0049 | Certificate auto enrollment for %1 cannot be done because the policy server %2 turns it off.\r\n
0x825a004a | Certificate enrollment for %1 failed to load policy from policy server %2 with ID  %3 (%4)\r\n
0x825a004b | Certificate enrollment for %1 failed in authentication to policy server %2 with ID  %3 (%6). Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004c | Certificate enrollment for %1 failed in authentication to enrollment server %2 (%6). Policy Id: %3. Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004d | Certificate enrollment for %1 cannot enroll from user configured enrollment policy server since it is disabled by group policy\r\n
0x825a004e | Certificate enrollment for %1 sent a request for template %2 to a ROBO certificate enrollment server %3\r\n
0x825a004f | Certificate enrollment for %1 sent a request for template %2 to a ANONYMOUS certificate enrollment server %3\r\n
0x825a0050 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ROBO and only renewal is supported\r\n
0x825a0051 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ANONYMOUS and only renewal is supported\r\n
0x825a0052 | Certificate enrollment for %1 failed in authentication to all urls for enrollment server associated with policy id: %2 (%4). Failed to enroll for template: %3\r\n
0x825a0053 | Certificate enrollment for %1 cannot find a credential that meets the selection criteria for url %2 with id %3 (%4)\r\n
0x825a0054 | The credential for URL %2 has been updated from certificate (%4) to certificate (%3) in context %1\r\n
0x825a0055 | Certificate enrollment for %1 for the %2 template could not perform attestation due to an error with the cryptographic hardware using the provider: %3. Request Id: %4.%5\r\n
0x90000001 | Microsoft-Windows-CertificateServicesClient-CertEnroll\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-System\r\n
0x92000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-User\r\n
0xb10003e9 | A certificate has been replaced. Please refer to the "Details" section for more information.\r\n
0xb10003ea | A certificate has expired. Please refer to the "Details" section for more information.\r\n
0xb10003eb | A certificate is about to expire. Please refer to the "Details" section for more information.\r\n
0xb10003ec | A certificate has been deleted. Please refer to the "Details" section for more information.\r\n
0xb10003ed | A certificate has been archived. Please refer to the "Details" section for more information.\r\n
0xb10003ee | A new certificate has been installed. Please refer to the "Details" section for more information.\r\n
0xb10003ef | A certificate has been exported. Please refer to the "Details" section for more information.\r\n
0xb10003f0 | A certificate has been associated with its private key. Please refer to the "Details" section for more information.\r\n
0xb10003f1 | A certificate could not be associated with its private key. Please refer to the "Details" section for more information.\r\n
0xc25a0006 | Certificate enrollment for %1 could not find a valid certificate template to match %2.  Enrollment was not performed.\r\n
0xc25a0009 | Certificate enrollment for %1 was denied by %3 when retrieving the pending request for a %2 certificate with request ID %4.\r\n
0xc25a000d | Certificate enrollment for %1 failed to enroll for a %2 certificate with request ID %4 from %3 (%5).\r\n
0xc25a0010 | Certificate enrollment for %1 failed to renew a %2 certificate with request ID %4 from %3 (%6). The certificate which failed to renew is %5\r\n
0xc25a0023 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  A new enrollment for a %2 certificate will be attempted in %3 hours.\r\n
0xc25a0024 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  No more enrollments for %2 certificates will be attempted until the current certificate is revoked or expires because the same error has occurred %3 times.\r\n
0xc25a002d | Certificate enrollment for %1 failed to create an enrollment request for a %2 certificate (%3).\r\n
0xc25a0056 | SCEP Certificate enrollment initialization for %1 via %2 failed:%n%n%3%nMethod: %4%nStage: %5%n%6\r\n
0xc25a0057 | SCEP Certificate enrollment for %1 via %2 failed:%n%n%3%nMethod: %4%nStage: %5%n%6\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x025a000e | Certificate enrollment for %1 received a %2 certificate with request ID %4 from %3 when retrieving pending requests.\r\n
0x025a0015 | Certificate enrollment for %1 attempted to enroll for a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x025a0016 | Certificate enrollment for %1 attempted to renew a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x10000038 | Classic\r\n
0x425a0004 | Certificate enrollment for %1 could not access local resources or retrieve %2 certificate template information (%3).  Enrollment was not performed.\r\n
0x425a0005 | Certificate enrollment for %1 could not find any valid certificate templates.  Enrollment was not performed.\r\n
0x425a000a | Certificate enrollment for %1 archived or deleted, from the Personal certificate store, certificates that have expired, or been revoked or superseded.\r\n
0x425a0013 | Certificate enrollment for %1 successfully received a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0014 | Certificate enrollment for %1 successfully renewed a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0019 | Certificate enrollment for %1 failed to update the %2 certificate in the Personal certificate store due to one of the following: %n %tCannot find %2 certificate template from Active Directory.%n %tEnrollment access to this template is not allowed.\r\n
0x425a001b | Certificate enrollment for %1 was cancelled by the user.\r\n
0x425a001e | Certificate enrollment for %1 was cancelled by the user when requesting a %2 certificate.\r\n
0x425a0020 | Certificate enrollment for %1 attempted to retrieve a %2 certificate from %3.  The certificate request is still pending.\r\n
0x425a0021 | Certificate enrollment for %1 deleted certificates that have expired, or have been revoked or superseded from the user object in Active Directory.\r\n
0x425a0029 | To prevent simultaneous renewal or enrollment from another computer, certificate enrollment for %1 to renew or enroll for a %2 certificate has been skipped.\r\n
0x425a0038 | Certificate enrollment for %1 for the template %2 was not performed because this template has been superseded.\r\n
0x425a0058 | SCEP Certificate enrollment for %1 via %2 succeeded:%n%n%3%nMethod: %4%nStage: %5\r\n
0x425a005b | Successfully found Logon Certificate Template for %1%nTemplate: %2%nState: %3%nProcess: %4\r\n
0x425a005d | Logon Certificate Request creation for %1 succeeded for the %2 template for key %3%nRequest thumbprint: %4%nProcess: %5\r\n
0x425a005f | Successfully installed Logon Certificate for %1%nRequest thumbprint: %2%nThumbprint: %3%nProcess: %4\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x825a000b | Certificate enrollment for %1 could not find a certification authority in the enterprise.  Enrollment was not performed.\r\n
0x825a000f | Certificate enrollment for %1 failed to retrieve certificate template information from the Policy Server. Enrollment was not performed.\r\n
0x825a0011 | Certificate enrollment for %1 failed to enroll for a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0012 | Certificate enrollment for %1 failed to renew a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0026 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because user interaction is required on the %2 template in Active Directory.\r\n
0x825a002a | Certificate enrollment for %1 for the %2 template must be performed by using the machine context.\r\n
0x825a002b | Certificate enrollment for %1 failed to find a smart card reader for the %2 template.  Enrollment will not be performed.\r\n
0x825a002c | Certificate enrollment for %1 failed to open the user interface (%2).\r\n
0x825a002e | Certificate enrollment for %1 could not enroll for a %2 certificate.  Read or enrollment access is not allowed for this template.\r\n
0x825a002f | Certificate enrollment for %1 could not enroll for a %2 certificate.  A valid certification authority cannot be found to issue this template.\r\n
0x825a0030 | Certificate enrollment for %1 could not enroll for a %2 certificate.  Signature requirements for the certificate cannot be met.\r\n
0x825a0032 | Certificate enrollment for %1 failed to install the certificate response for a %2 certificate with request ID %3 (%4).\r\n
0x825a0033 | Certificate enrollment for %1 for the %2 certificate must be performed under the user context.\r\n
0x825a0034 | The CA certificate for %3 is not trusted. Certificate enrollment for %1 for a %2 certificate failed.\r\n
0x825a0035 | Certificate enrollment for %1 failed to retrieve a %2 certificate from certification authority %3 with request ID %4, and the error returned from the server is %5.  Another certification authority will be contacted.\r\n
0x825a0036 | Certificate enrollment for %1 failed to retrieve a pending %2 certificate with request ID %4 from certification authority %3 (%5). The enrollment process will be attempted again later.\r\n
0x825a0037 | Certificate enrollment for %1 for the %2 template could not find specified CSPs on the local machine.  Enrollment will not be performed.\r\n
0x825a0039 | The "%2" provider was not loaded because initialization failed.\r\n
0x825a003a | The "%3" algorithm for the "%2" provider was not loaded because initialization failed.\r\n
0x825a003b | Could not determine the signature algorithm for %2 to sign an enrollment request.\r\n
0x825a003c | Could not find a registered public key algorithm OID for %2 for an enrollment request.\r\n
0x825a003d | Could not find a registered signature algorithm OID for %1 and %2 to sign an enrollment request.\r\n
0x825a003e | Could not encode signature parameters for a %2 signature for an enrollment request.\r\n
0x825a003f | Enrollment Policy Server %2 returned an error when retrieving templates for %1: %3\r\n
0x825a0040 | Certificate enrollment for %1 successfully load policy from policy server %2\r\n
0x825a0041 | Certificate enrollment for %1 is successfully authenticated by policy server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0042 | Certificate enrollment for %1 is successfully authenticated by enrollment server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0043 | Certificate enrollment for %1 failed to load policy from policy servers with ID  %2 (%3)\r\n
0x825a0044 | Certificate enrollment for %1 failed in authentication to policy servers with ID %2  (%3)\r\n
0x825a0046 | Certificate enrollment for %1 failed because no valid policy can be obtained from policy servers with ID %2\r\n
0x825a0047 | Certificate enrollment for %1 failed in adding credential to Vault for %2 (%3)\r\n
0x825a0048 | Certificate enrollment for %1 failed because the loaded policy from the policy server %2 is invalid (%3)\r\n
0x825a0049 | Certificate auto enrollment for %1 cannot be done because the policy server %2 turns it off.\r\n
0x825a004a | Certificate enrollment for %1 failed to load policy from policy server %2 with ID  %3 (%4)\r\n
0x825a004b | Certificate enrollment for %1 failed in authentication to policy server %2 with ID  %3 (%6). Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004c | Certificate enrollment for %1 failed in authentication to enrollment server %2 (%6). Policy Id: %3. Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004d | Certificate enrollment for %1 cannot enroll from user configured enrollment policy server since it is disabled by group policy\r\n
0x825a004e | Certificate enrollment for %1 sent a request for template %2 to a ROBO certificate enrollment server %3\r\n
0x825a004f | Certificate enrollment for %1 sent a request for template %2 to a ANONYMOUS certificate enrollment server %3\r\n
0x825a0050 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ROBO and only renewal is supported\r\n
0x825a0051 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ANONYMOUS and only renewal is supported\r\n
0x825a0052 | Certificate enrollment for %1 failed in authentication to all urls for enrollment server associated with policy id: %2 (%4). Failed to enroll for template: %3\r\n
0x825a0053 | Certificate enrollment for %1 cannot find a credential that meets the selection criteria for url %2 with id %3 (%4)\r\n
0x825a0054 | The credential for URL %2 has been updated from certificate (%4) to certificate (%3) in context %1\r\n
0x825a0055 | Certificate enrollment for %1 for the %2 template could not perform attestation due to an error with the cryptographic hardware using the provider: %3. Request Id: %4.%5\r\n
0x825a0061 | Successfully removed Logon Certificate request for %1%nRequest thumbprint: %2%nProcess: %3\r\n
0x90000001 | Microsoft-Windows-CertificateServicesClient-CertEnroll\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-System\r\n
0x92000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-User\r\n
0xb10003e9 | A certificate has been replaced. Please refer to the "Details" section for more information.\r\n
0xb10003ea | A certificate has expired. Please refer to the "Details" section for more information.\r\n
0xb10003eb | A certificate is about to expire. Please refer to the "Details" section for more information.\r\n
0xb10003ec | A certificate has been deleted. Please refer to the "Details" section for more information.\r\n
0xb10003ed | A certificate has been archived. Please refer to the "Details" section for more information.\r\n
0xb10003ee | A new certificate has been installed. Please refer to the "Details" section for more information.\r\n
0xb10003ef | A certificate has been exported. Please refer to the "Details" section for more information.\r\n
0xb10003f0 | A certificate has been associated with its private key. Please refer to the "Details" section for more information.\r\n
0xb10003f1 | A certificate could not be associated with its private key. Please refer to the "Details" section for more information.\r\n
0xb10003f2 | A certificate has been deleted from Active Directory. Please refer to the "Details" section for more information.\r\n
0xc25a0006 | Certificate enrollment for %1 could not find a valid certificate template to match %2.  Enrollment was not performed.\r\n
0xc25a0009 | Certificate enrollment for %1 was denied by %3 when retrieving the pending request for a %2 certificate with request ID %4.\r\n
0xc25a000d | Certificate enrollment for %1 failed to enroll for a %2 certificate with request ID %4 from %3 (%5).\r\n
0xc25a0010 | Certificate enrollment for %1 failed to renew a %2 certificate with request ID %4 from %3 (%6). The certificate which failed to renew is %5\r\n
0xc25a0023 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  A new enrollment for a %2 certificate will be attempted in %3 hours.\r\n
0xc25a0024 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  No more enrollments for %2 certificates will be attempted until the current certificate is revoked or expires because the same error has occurred %3 times.\r\n
0xc25a002d | Certificate enrollment for %1 failed to create an enrollment request for a %2 certificate (%3).\r\n
0xc25a0056 | SCEP Certificate enrollment initialization for %1 via %2 failed:%n%n%3%nMethod: %4%nStage: %5%n%6\r\n
0xc25a0057 | SCEP Certificate enrollment for %1 via %2 failed:%n%n%3%nMethod: %4%nStage: %5%n%6\r\n
0xc25a0059 | Could not find a Logon Certificate Template for %1%nState: %3%nProcess: %4%n%5\r\n
0xc25a005a | Found multiple Logon Certificate Templates for %1%nTemplates: %2%nState: %3%nProcess: %4%n%5\r\n
0xc25a005c | Logon Certificate Request creation for %1 failed for the %2 template for key %3%n%4%nProcess: %5%n%6\r\n
0xc25a005e | Failed to install Logon Certificate for %1 failed%nRequest thumbprint: %2%nThumbprint: %3%n%4%nProcess: %5%n%6\r\n
0xc25a0060 | Failed to remove Logon Certificate request for %1%nRequest thumbprint: %2%nProcess: %3%n%4\r\n
0xc25a0062 | Failed to import PFX Certificate for %1%nFlags: %2%nProvider: %3%nContainer: %4%nProcess: %5%n%6\r\n

### 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x025a000e | Certificate enrollment for %1 received a %2 certificate with request ID %4 from %3 when retrieving pending requests.\r\n
0x025a0015 | Certificate enrollment for %1 attempted to enroll for a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x025a0016 | Certificate enrollment for %1 attempted to renew a %2 certificate with request ID %4 from certification authority %3.  The request is pending.\r\n
0x10000038 | Classic\r\n
0x425a0004 | Certificate enrollment for %1 could not access local resources or retrieve %2 certificate template information (%3).  Enrollment was not performed.\r\n
0x425a0005 | Certificate enrollment for %1 could not find any valid certificate templates.  Enrollment was not performed.\r\n
0x425a000a | Certificate enrollment for %1 archived or deleted, from the Personal certificate store, certificates that have expired, or been revoked or superseded.\r\n
0x425a0013 | Certificate enrollment for %1 successfully received a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0014 | Certificate enrollment for %1 successfully renewed a %2 certificate with request ID %4 from certification authority %3.\r\n
0x425a0019 | Certificate enrollment for %1 failed to update the %2 certificate in the Personal certificate store due to one of the following: %n %tCannot find %2 certificate template from Active Directory.%n %tEnrollment access to this template is not allowed.\r\n
0x425a001b | Certificate enrollment for %1 was cancelled by the user.\r\n
0x425a001e | Certificate enrollment for %1 was cancelled by the user when requesting a %2 certificate.\r\n
0x425a0020 | Certificate enrollment for %1 attempted to retrieve a %2 certificate from %3.  The certificate request is still pending.\r\n
0x425a0021 | Certificate enrollment for %1 deleted certificates that have expired, or have been revoked or superseded from the user object in Active Directory.\r\n
0x425a0029 | To prevent simultaneous renewal or enrollment from another computer, certificate enrollment for %1 to renew or enroll for a %2 certificate has been skipped.\r\n
0x425a0038 | Certificate enrollment for %1 for the template %2 was not performed because this template has been superseded.\r\n
0x425a0058 | SCEP Certificate enrollment for %1 via %2 succeeded:%n%n%3%nMethod: %4%nStage: %5\r\n
0x425a005b | Successfully found Logon Certificate Template for %1%nTemplate: %2%nState: %3%nProcess: %4\r\n
0x425a005d | Logon Certificate Request creation for %1 succeeded for the %2 template for key %3%nRequest thumbprint: %4%nProcess: %5\r\n
0x425a005f | Successfully installed Logon Certificate for %1%nRequest thumbprint: %2%nThumbprint: %3%nProcess: %4\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0x825a000b | Certificate enrollment for %1 could not find a certification authority in the enterprise.  Enrollment was not performed.\r\n
0x825a000f | Certificate enrollment for %1 failed to retrieve certificate template information from the Policy Server. Enrollment was not performed.\r\n
0x825a0011 | Certificate enrollment for %1 failed to enroll for a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0012 | Certificate enrollment for %1 failed to renew a %2 certificate from certification authority %3 (%4). Another certification authority will be contacted.\r\n
0x825a0026 | Certificate enrollment for %1 cannot enroll or renew %2 certificate because user interaction is required on the %2 template in Active Directory.\r\n
0x825a002a | Certificate enrollment for %1 for the %2 template must be performed by using the machine context.\r\n
0x825a002b | Certificate enrollment for %1 failed to find a smart card reader for the %2 template.  Enrollment will not be performed.\r\n
0x825a002c | Certificate enrollment for %1 failed to open the user interface (%2).\r\n
0x825a002e | Certificate enrollment for %1 could not enroll for a %2 certificate.  Read or enrollment access is not allowed for this template.\r\n
0x825a002f | Certificate enrollment for %1 could not enroll for a %2 certificate.  A valid certification authority cannot be found to issue this template.\r\n
0x825a0030 | Certificate enrollment for %1 could not enroll for a %2 certificate.  Signature requirements for the certificate cannot be met.\r\n
0x825a0032 | Certificate enrollment for %1 failed to install the certificate response for a %2 certificate with request ID %3 (%4).\r\n
0x825a0033 | Certificate enrollment for %1 for the %2 certificate must be performed under the user context.\r\n
0x825a0034 | The CA certificate for %3 is not trusted. Certificate enrollment for %1 for a %2 certificate failed.\r\n
0x825a0035 | Certificate enrollment for %1 failed to retrieve a %2 certificate from certification authority %3 with request ID %4, and the error returned from the server is %5.  Another certification authority will be contacted.\r\n
0x825a0036 | Certificate enrollment for %1 failed to retrieve a pending %2 certificate with request ID %4 from certification authority %3 (%5). The enrollment process will be attempted again later.\r\n
0x825a0037 | Certificate enrollment for %1 for the %2 template could not find specified CSPs on the local machine.  Enrollment will not be performed.\r\n
0x825a0039 | The "%2" provider was not loaded because initialization failed.\r\n
0x825a003a | The "%3" algorithm for the "%2" provider was not loaded because initialization failed.\r\n
0x825a003b | Could not determine the signature algorithm for %2 to sign an enrollment request.\r\n
0x825a003c | Could not find a registered public key algorithm OID for %2 for an enrollment request.\r\n
0x825a003d | Could not find a registered signature algorithm OID for %1 and %2 to sign an enrollment request.\r\n
0x825a003e | Could not encode signature parameters for a %2 signature for an enrollment request.\r\n
0x825a003f | Enrollment Policy Server %2 returned an error when retrieving templates for %1: %3\r\n
0x825a0040 | Certificate enrollment for %1 successfully load policy from policy server %2\r\n
0x825a0041 | Certificate enrollment for %1 is successfully authenticated by policy server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0042 | Certificate enrollment for %1 is successfully authenticated by enrollment server %2 using authentication mechanism %5 (Credential: %4). Policy Id: %3\r\n
0x825a0043 | Certificate enrollment for %1 failed to load policy from policy servers with ID  %2 (%3)\r\n
0x825a0044 | Certificate enrollment for %1 failed in authentication to policy servers with ID %2  (%3)\r\n
0x825a0046 | Certificate enrollment for %1 failed because no valid policy can be obtained from policy servers with ID %2\r\n
0x825a0047 | Certificate enrollment for %1 failed in adding credential to Vault for %2 (%3)\r\n
0x825a0048 | Certificate enrollment for %1 failed because the loaded policy from the policy server %2 is invalid (%3)\r\n
0x825a0049 | Certificate auto enrollment for %1 cannot be done because the policy server %2 turns it off.\r\n
0x825a004a | Certificate enrollment for %1 failed to load policy from policy server %2 with ID  %3 (%4)\r\n
0x825a004b | Certificate enrollment for %1 failed in authentication to policy server %2 with ID  %3 (%6). Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004c | Certificate enrollment for %1 failed in authentication to enrollment server %2 (%6). Policy Id: %3. Authentication mechanism was %5 (Credential: %4)\r\n
0x825a004d | Certificate enrollment for %1 cannot enroll from user configured enrollment policy server since it is disabled by group policy\r\n
0x825a004e | Certificate enrollment for %1 sent a request for template %2 to a ROBO certificate enrollment server %3\r\n
0x825a004f | Certificate enrollment for %1 sent a request for template %2 to a ANONYMOUS certificate enrollment server %3\r\n
0x825a0050 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ROBO and only renewal is supported\r\n
0x825a0051 | Certificate enrollment for %1 cannot enroll for a %2 certificate because the certificate enrollment server %3 is ANONYMOUS and only renewal is supported\r\n
0x825a0052 | Certificate enrollment for %1 failed in authentication to all urls for enrollment server associated with policy id: %2 (%4). Failed to enroll for template: %3\r\n
0x825a0053 | Certificate enrollment for %1 cannot find a credential that meets the selection criteria for url %2 with id %3 (%4)\r\n
0x825a0054 | The credential for URL %2 has been updated from certificate (%4) to certificate (%3) in context %1\r\n
0x825a0055 | Certificate enrollment for %1 for the %2 template could not perform attestation due to an error with the cryptographic hardware using the provider: %3. Request Id: %4.%5\r\n
0x825a0061 | Successfully removed Logon Certificate request for %1%nRequest thumbprint: %2%nProcess: %3\r\n
0x90000001 | Microsoft-Windows-CertificateServicesClient-CertEnroll\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-System\r\n
0x92000001 | Microsoft-Windows-CertificateServicesClient-Lifecycle-User\r\n
0xb10003e9 | A certificate has been replaced. Please refer to the "Details" section for more information.\r\n
0xb10003ea | A certificate has expired. Please refer to the "Details" section for more information.\r\n
0xb10003eb | A certificate is about to expire. Please refer to the "Details" section for more information.\r\n
0xb10003ec | A certificate has been deleted. Please refer to the "Details" section for more information.\r\n
0xb10003ed | A certificate has been archived. Please refer to the "Details" section for more information.\r\n
0xb10003ee | A new certificate has been installed. Please refer to the "Details" section for more information.\r\n
0xb10003ef | A certificate has been exported. Please refer to the "Details" section for more information.\r\n
0xb10003f0 | A certificate has been associated with its private key. Please refer to the "Details" section for more information.\r\n
0xb10003f1 | A certificate could not be associated with its private key. Please refer to the "Details" section for more information.\r\n
0xb10003f2 | A certificate has been deleted from Active Directory. Please refer to the "Details" section for more information.\r\n
0xc25a0006 | Certificate enrollment for %1 could not find a valid certificate template to match %2.  Enrollment was not performed.\r\n
0xc25a0009 | Certificate enrollment for %1 was denied by %3 when retrieving the pending request for a %2 certificate with request ID %4.\r\n
0xc25a000d | Certificate enrollment for %1 failed to enroll for a %2 certificate with request ID %4 from %3 (%5).\r\n
0xc25a0010 | Certificate enrollment for %1 failed to renew a %2 certificate with request ID %4 from %3 (%6). The certificate which failed to renew is %5\r\n
0xc25a0023 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  A new enrollment for a %2 certificate will be attempted in %3 hours.\r\n
0xc25a0024 | Certificate enrollment for %1 detected that the DNS name in the %2 certificate does not match the DNS name of the local computer.  No more enrollments for %2 certificates will be attempted until the current certificate is revoked or expires because the same error has occurred %3 times.\r\n
0xc25a002d | Certificate enrollment for %1 failed to create an enrollment request for a %2 certificate (%3).\r\n
0xc25a0056 | SCEP Certificate enrollment initialization for %1 via %2 failed:%n%n%3%nMethod: %4%nStage: %5%n%6\r\n
0xc25a0057 | SCEP Certificate enrollment for %1 via %2 failed:%n%n%3%nMethod: %4%nStage: %5%n%6\r\n
0xc25a0059 | Could not find a Logon Certificate Template for %1%nTemplate: %2%nState: %3%nProcess: %4%n%5\r\n
0xc25a005a | Found multiple Logon Certificate Templates for %1%nTemplates: %2%nState: %3%nProcess: %4%n%5\r\n
0xc25a005c | Logon Certificate Request creation for %1 failed for the %2 template for key %3%n%4%nProcess: %5%n%6\r\n
0xc25a005e | Failed to install Logon Certificate for %1 failed%nRequest thumbprint: %2%nThumbprint: %3%n%4%nProcess: %5%n%6\r\n
0xc25a0060 | Failed to remove Logon Certificate request for %1%nRequest thumbprint: %2%nProcess: %3%n%4\r\n
0xc25a0062 | Failed to import PFX Certificate for %1%nFlags: %2%nProvider: %3%nContainer: %4%nProcess: %5%n%6\r\n
