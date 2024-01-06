## oakley.dll

Path: %SystemRoot%\System32\oakley.dll

### 5.0.2195.6662

Message identifier | Message string
--- | ---
0x4bad01fb | Failed to obtain Kerberos server credentials for ISAKMP/Oakley service.  Kerberos authentication will not function.  The most likely reason for this is lack of domain membership.  This is normal if your computer is a member of a workgroup.\r\n
0x4bad021e | The IP Security policy for ISAKMP/Oakley specified an encryption algorithm that is invalid due to export cryptography restrictions.  All 3DES encryption used by ISAKMP/Oakley is weakened to standard DES encyption.  Generally, this is benign.  ISAKMP/Oakley will still be able to negotiate IP security parameters, and protect that negotiation with DES encryption.  This should only be of concern if you demand that the ISAKMP/Oakley negotiation be protected with 3DES encryption.  If this is the case, please contact your network administrator.     \r\n
0x4bad0233 | Formatting audit failed.  Dumping as bytes.\r\n
0x4bad025a | Source IP Address %1\r\nSource IP Address Mask %2\r\nDestination IP Address %3\r\nDestination IP Address Mask %4\r\nProtocol %5\r\nSource Port %6\r\nDestination Port %7\r\n
0x4bad025b | ESP Algorithm %1\r\nHMAC Algorithm %2\r\nAH Algorithm %3\r\nEncapsulation %4\r\nInboundSpi %5\r\nOutBoundSpi %6\r\nLifetime (sec) %7\r\nLifetime (kb) %8\r\n
0x4bad025c | Certificate based Identity.  \r\nSubject %1\r\nIssuing Certificate Authority %2\r\nRoot Certificate Authority %3\r\nPeer IP Address: %4\r\n
0x4bad025d | Kerberos based Identity: %1\r\nPeer IP Address: %2\r\n
0x4bad025e | Preshared key ID.\r\nPeer IP Address: %1\r\n
0x4bad025f | Security association negotiation failure because of attribute mismatch. \r\nAttribute: %1\r\nExpected Value: %2\r\nReceived Value: %3\r\n
0x4bad0262 | Phase I Encryption Algorithm%0\r\n
0x4bad0263 | DES CBC%0\r\n
0x4bad0264 | 40 bit DES CBC%0\r\n
0x4bad0265 | Triple DES CBC%0\r\n
0x4bad0266 | Phase I Hash Algorithm%0\r\n
0x4bad0267 | MD5%0\r\n
0x4bad0268 | SHA%0\r\n
0x4bad0269 | Authentication Method%0\r\n
0x4bad026a | Preshared Key%0\r\n
0x4bad026b | RSA Signature with Certificates%0\r\n
0x4bad026c | Kerberos (GSSAPI)%0\r\n
0x4bad026d | Phase I Diffie-Hellman Group%0\r\n
0x4bad026e | Phase I Diffie-Hellman Group type%0\r\n
0x4bad026f | Length (in bytes) of Phase I Diffie-Hellman prime (P)%0\r\n
0x4bad0270 | Length (in bytes) of Phase I Diffie-Hellman generator (G)%0\r\n
0x4bad0271 | Phase I Lifetime type%0\r\n
0x4bad0272 | Phase I Lifetime duration%0\r\n
0x4bad0273 | Phase I pseudo-random function%0\r\n
0x4bad0274 | Phase I key length%0\r\n
0x4bad0275 | Peer identity for Kerberos (GSSAPI)%0\r\n
0x4bad0276 | Phase II life type%0\r\n
0x4bad0277 | Phase II life duration%0\r\n
0x4bad0278 | Phase II Diffie-Hellman group descriptor%0\r\n
0x4bad0279 | Phase II Encapsulation Mode%0\r\n
0x4bad027a | Transport Mode%0\r\n
0x4bad027b | Tunnel Mode%0\r\n
0x4bad027c | Phase II HMAC Algorithm%0\r\n
0x4bad027f | Phase II Key length%0\r\n
0x4bad0280 | Phase II Key rounds%0\r\n
0x4bad0281 | Phase II encryption and/or authentication algorithm(s)%0\r\n
0x4bad0282 | NULL DES%0\r\n
0x4bad0283 | NULL%0\r\n
0x4bad0284 | Phase II Protocol%0\r\n
0x4bad0285 | None%0\r\n
0x4bad0288 | Me\r\n
0x4bad0289 | Peer\r\n
0x4bad028a | Key Exchange Mode (Main Mode)\r\n
0x4bad028b | Data Protection Mode (Quick Mode)\r\n
0x4bad028c | ESP Algorithm %1\r\nHMAC Algorithm %2\r\nLifetime (sec) %3\r\n
0x8bad0212 | More data available via this call\r\n
0x8bad021b | Failed to tell IPSec Driver that Security Association has expired: %1\r\n
0x8bad021f | Failed to add Security Association to IPSec Driver.  The most common cause for this is if the IKE negotiation took too long to complete.  If the problem persists, reduce the load on the faulting machine.\r\n
0x8bad0221 | Failed to find RSA Cryptographic Service provider.  Certificate based Authentication will fail.  \r\n
0x8bad0222 | Failed to find Diffie-Hellman Cryptographic Service provider.\r\n
0x8bad0223 | Invalid policy\r\n
0x8bad0224 | Invalid DOI\r\n
0x8bad0225 | Invalid situation\r\n
0x8bad0226 | Diffie-Hellman failure\r\n
0x8bad0227 | Invalid Diffie-Hellman group\r\n
0x8bad0228 | Error encrypting payload\r\n
0x8bad0229 | Error decrypting payload\r\n
0x8bad022a | Policy match error\r\n
0x8bad022b | Unsupported ID\r\n
0x8bad022c | Hash verification failed\r\n
0x8bad022d | Invalid hash algorithm\r\n
0x8bad022e | Invalid hash size \r\n
0x8bad022f | Invalid encryption algorithm\r\n
0x8bad0230 | Invalid authentication algorithm\r\n
0x8bad0231 | Invalid certificate signature\r\n
0x8bad0232 | Load failed\r\n
0xcbad01f6 | Initialization failed.\r\n
0xcbad01f7 | Failed to enabled TCB privilege.\r\n
0xcbad01f8 | Failed to load SECURITY.DLL.\r\n
0xcbad01f9 | Failed to obtain security function table dispatch address from SSPI.\r\n
0xcbad01fa | Failed to query Kerberos package to obtain max token size.\r\n
0xcbad01fc | Failed to create Receive heap.\r\n
0xcbad01ff | Failed to create I/O completion port.\r\n
0xcbad0208 | Failed to Bind to ISAKMP/Oakley port (500).\r\n
0xcbad0209 | Failed to initialize Winsock 2.\r\n
0xcbad020a | Failed to initialize Acquire thread.\r\n
0xcbad020e | Failed to determine SSPI principal name for ISAKMP/Oakley service (QueryCredentialsAttributes).\r\n
0xcbad020f | Failed to queue AcquireSa call to the Ipsec driver.\r\n
0xcbad0210 | Failed to obtain new SPI for the inbound SA from Ipsec driver.  The most common cause for this is that the driver does not have the correct filter.  Check your policy to verify the filters.\r\n
0xcbad0211 | Failed to bind with RPC server.\r\n
0xcbad0213 | Already serving the maximum number of Notify Clients\r\n
0xcbad0214 | Given filter is invalid\r\n
0xcbad0215 | IOCTL failed\r\n
0xcbad0217 | Memory allocation failed.  \r\n
0xcbad0235 | OAKLEY_STATUS_SET\r\n
0xcbad0236 | OAKLEY_REINIT_NEEDED\r\n
0xcbad0237 | OAKLEY_STATUS_INACTIVE\r\n
0xcbad0320 | OAKLEY_NEG_STATUS_BEGIN\r\n
0xcbad0321 | IKE authentication credentials are unacceptable\r\n
0xcbad0322 | IKE security attributes are unacceptable\r\n
0xcbad0323 | IKE Negotiation in progress\r\n
0xcbad0324 | General processing error\r\n
0xcbad0325 | Negotiation timed out\r\n
0xcbad0326 | IKE failed to find valid machine certificate\r\n
0xcbad0327 | IKE SA deleted by peer before establishment completed\r\n
0xcbad0328 | IKE SA deleted before establishment completed\r\n
0xcbad0329 | Negotiation request sat in Queue too long\r\n
0xcbad032a | Negotiation request sat in Queue too long\r\n
0xcbad032b | Negotiation request sat in Queue too long\r\n
0xcbad032c | Negotiation request sat in Queue too long\r\n
0xcbad032d | No response from peer\r\n
0xcbad032e | Negotiation took too long\r\n
0xcbad032f | Negotiation took too long\r\n
0xcbad0330 | Unknown error occurred\r\n
0xcbad0331 | Certificate Revocation Check failed\r\n
0xcbad0332 | Invalid certificate key usage\r\n
0xcbad0333 | Invalid certificate type\r\n
0xcbad0334 | No private key associated with machine certificate\r\n
0xcbad0336 | Failure in Diffie-Helman computation\r\n
0xcbad0338 | Invalid header\r\n
0xcbad0339 | No policy configured\r\n
0xcbad033a | Failed to verify signature\r\n
0xcbad033b | Failed to authenticate using kerberos\r\n
0xcbad033c | Peer's certificate did not have a public key\r\n
0xcbad033d | Error processing error payload\r\n
0xcbad033e | Error processing SA payload\r\n
0xcbad033f | Error processing Proposal payload\r\n
0xcbad0340 | Error processing Transform payload\r\n
0xcbad0341 | Error processing KE payload\r\n
0xcbad0342 | Error processing ID payload\r\n
0xcbad0343 | Error processing Cert payload\r\n
0xcbad0344 | Error processing Certificate Request payload\r\n
0xcbad0345 | Error processing Hash payload\r\n
0xcbad0346 | Error processing Signature payload\r\n
0xcbad0347 | Error processing Nonce payload\r\n
0xcbad0348 | Error processing Notify payload\r\n
0xcbad0349 | Error processing Delete Payload\r\n
0xcbad034a | Error processing VendorId payload\r\n
0xcbad034b | Invalid payload received\r\n
0xcbad034c | Soft SA loaded\r\n
0xcbad034d | Soft SA torn down\r\n
0xcbad034e | Invalid cookie received.\r\n
0xcbad034f | Peer failed to send valid machine certificate\r\n
0xcbad0350 | Certification Revocation check of peer's certificate failed\r\n
0xcbad0351 | New policy invalidated SAs formed with old policy\r\n
0xcbad0352 | OAKLEY_NEG_STATUS_END\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x4bad025a | Source IP Address %1\r\nSource IP Address Mask %2\r\nDestination IP Address %3\r\nDestination IP Address Mask %4\r\nProtocol %5\r\nSource Port %6\r\nDestination Port %7\r\nIKE Local Addr %8\r\nIKE Peer Addr %9\r\n
0x4bad025b | ESP Algorithm %1\r\nHMAC Algorithm %2\r\nAH Algorithm %3\r\nEncapsulation %4\r\nInboundSpi %5\r\nOutBoundSpi %6\r\nLifetime (sec) %7\r\nLifetime (kb) %8\r\n
0x4bad025c | Certificate based Identity.  \r\nPeer Subject %1\r\nPeer SHA Thumbprint %2\r\nPeer Issuing Certificate Authority %3\r\nRoot Certificate Authority %4\r\nMy Subject %5\r\nMy SHA Thumbprint %6\r\nPeer IP Address: %7\r\n
0x4bad025d | Kerberos based Identity: %1\r\nPeer IP Address: %2\r\n
0x4bad025e | Preshared key ID.\r\nPeer IP Address: %1\r\n
0x4bad025f | Security association negotiation failure because of attribute mismatch. \r\nAttribute: %1\r\nExpected Value: %2\r\nReceived Value: %3\r\n
0x4bad0262 | Phase I Encryption Algorithm%0\r\n
0x4bad0263 | DES CBC%0\r\n
0x4bad0265 | Triple DES CBC%0\r\n
0x4bad0266 | Phase I Hash Algorithm%0\r\n
0x4bad0267 | MD5%0\r\n
0x4bad0268 | SHA%0\r\n
0x4bad0269 | Authentication Method%0\r\n
0x4bad026a | Preshared Key%0\r\n
0x4bad026b | RSA Signature with Certificates%0\r\n
0x4bad026c | Kerberos (GSSAPI)%0\r\n
0x4bad026d | Phase I Diffie-Hellman Group%0\r\n
0x4bad026e | Phase I Diffie-Hellman Group type%0\r\n
0x4bad026f | Length (in bytes) of Phase I Diffie-Hellman prime (P)%0\r\n
0x4bad0270 | Length (in bytes) of Phase I Diffie-Hellman generator (G)%0\r\n
0x4bad0271 | Phase I Lifetime type%0\r\n
0x4bad0272 | Phase I Lifetime duration%0\r\n
0x4bad0273 | Phase I pseudo-random function%0\r\n
0x4bad0274 | Phase I key length%0\r\n
0x4bad0275 | Peer identity for Kerberos (GSSAPI)%0\r\n
0x4bad0276 | Phase II life type%0\r\n
0x4bad0277 | Phase II life duration%0\r\n
0x4bad0278 | Phase II Diffie-Hellman group descriptor%0\r\n
0x4bad0279 | Phase II Encapsulation Mode%0\r\n
0x4bad027a | Transport Mode%0\r\n
0x4bad027b | Tunnel Mode%0\r\n
0x4bad027c | Phase II HMAC Algorithm%0\r\n
0x4bad027f | Phase II Key length%0\r\n
0x4bad0280 | Phase II Key rounds%0\r\n
0x4bad0281 | Phase II encryption and/or authentication algorithm(s)%0\r\n
0x4bad0282 | NULL DES%0\r\n
0x4bad0283 | NULL%0\r\n
0x4bad0284 | Phase II Protocol%0\r\n
0x4bad0285 | None%0\r\n
0x4bad0288 | Me\r\n
0x4bad0289 | Peer\r\n
0x4bad028a | Key Exchange Mode (Main Mode)\r\n
0x4bad028b | Data Protection Mode (Quick Mode)\r\n
0x4bad028c | ESP Algorithm %1\r\nHMAC Algorithm %2\r\nLifetime (sec) %3\r\n
0x4bad028d | Invalid spi size\r\n
0x4bad028e | IKE has a large number of pending Security Association establishment requests, and is beginning denial of service prevention mode.  This could be normal, caused by high machine loads, and/or a large number of client connection attempts.  It also could be the result of a denial of service attack against IKE.  If this is a denial of service attack, there will usually be many audits for failed IKE negotiations to spoofed IP addresses.  Otherwise, the machine is just extremely heavily loaded.  \r\n
0x4bad028f | IKE has recovered from denial of service prevention mode and has resumed normal operation.\r\n
0x4bad0290 | Certificate based Identity.  \r\nPeer IP Address: %1\r\n
0x4bad02a4 | Formatting audit failed.  Dumping as bytes.\r\n
0xcbad02a5 | OAKLEY_STATUS_SET\r\n
0xcbad02a6 | OAKLEY_REINIT_NEEDED\r\n
0xcbad02a7 | OAKLEY_STATUS_INACTIVE\r\n
0xcbad02a8 | OAKLEY_POLICY_TOO_GENERAL\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x4bad025a | Source IP Address %1\r\nSource IP Address Mask %2\r\nDestination IP Address %3\r\nDestination IP Address Mask %4\r\nProtocol %5\r\nSource Port %6\r\nDestination Port %7\r\nIKE Local Addr %8\r\nIKE Peer Addr %9\r\nIKE Source Port %10\r\nIKE Destination Port %11\r\nPeer Private Addr %12\r\n
0x4bad025b | ESP Algorithm %1\r\nHMAC Algorithm %2\r\nAH Algorithm %3\r\nEncapsulation %4\r\nInboundSpi %5\r\nOutBoundSpi %6\r\nLifetime (sec) %7\r\nLifetime (kb) %8\r\nQM delta time (sec) %9\r\nTotal delta time (sec) %10\r\n
0x4bad025c | Certificate based Identity.  \r\nPeer Subject %1\r\nPeer SHA Thumbprint %2\r\nPeer Issuing Certificate Authority %3\r\nRoot Certificate Authority %4\r\nMy Subject %5\r\nMy SHA Thumbprint %6\r\nPeer IP Address: %7\r\n
0x4bad025d | Kerberos based Identity: %1\r\nPeer IP Address: %2\r\n
0x4bad025e | Preshared key ID.\r\nPeer IP Address: %1\r\n
0x4bad025f | Security association negotiation failure because of attribute mismatch. \r\nAttribute: %1\r\nExpected Value: %2\r\nReceived Value: %3\r\n
0x4bad0262 | Phase I Encryption Algorithm%0\r\n
0x4bad0263 | DES CBC%0\r\n
0x4bad0265 | Triple DES CBC%0\r\n
0x4bad0266 | Phase I Hash Algorithm%0\r\n
0x4bad0267 | MD5%0\r\n
0x4bad0268 | SHA%0\r\n
0x4bad0269 | Authentication Method%0\r\n
0x4bad026a | Preshared Key%0\r\n
0x4bad026b | RSA Signature with Certificates%0\r\n
0x4bad026c | Kerberos (GSSAPI)%0\r\n
0x4bad026d | Phase I Diffie-Hellman Group%0\r\n
0x4bad026e | Phase I Diffie-Hellman Group type%0\r\n
0x4bad026f | Length (in bytes) of Phase I Diffie-Hellman prime (P)%0\r\n
0x4bad0270 | Length (in bytes) of Phase I Diffie-Hellman generator (G)%0\r\n
0x4bad0271 | Phase I Lifetime type%0\r\n
0x4bad0272 | Phase I Lifetime duration%0\r\n
0x4bad0273 | Phase I pseudo-random function%0\r\n
0x4bad0274 | Phase I key length%0\r\n
0x4bad0275 | Peer identity for Kerberos (GSSAPI)%0\r\n
0x4bad0276 | Phase II life type%0\r\n
0x4bad0277 | Phase II life duration%0\r\n
0x4bad0278 | Phase II Diffie-Hellman group descriptor%0\r\n
0x4bad0279 | Phase II Encapsulation Mode%0\r\n
0x4bad027a | Transport Mode%0\r\n
0x4bad027b | Tunnel Mode%0\r\n
0x4bad027c | Phase II HMAC Algorithm%0\r\n
0x4bad027d | Transport Mode with UDP encapsulation\r\n
0x4bad027e | Tunnel Mode with UDP encapsulation\r\n
0x4bad027f | Phase II Key length%0\r\n
0x4bad0280 | Phase II Key rounds%0\r\n
0x4bad0281 | Phase II encryption and/or authentication algorithm(s)%0\r\n
0x4bad0282 | NULL DES%0\r\n
0x4bad0283 | NULL%0\r\n
0x4bad0284 | Phase II Protocol%0\r\n
0x4bad0285 | None%0\r\n
0x4bad0288 | Me\r\n
0x4bad0289 | Peer\r\n
0x4bad028a | Key Exchange Mode (Main Mode)\r\n
0x4bad028b | Data Protection Mode (Quick Mode)\r\n
0x4bad028c | ESP Algorithm %1\r\nHMAC Algorithm %2\r\nLifetime (sec) %3\r\nMM delta time (sec) %4\r\n
0x4bad028d | Invalid spi size\r\n
0x4bad028e | IKE has a large number of pending Security Association establishment requests, and is beginning denial of service prevention mode.  This could be normal, caused by high machine loads, and/or a large number of client connection attempts.  It also could be the result of a denial of service attack against IKE.  If this is a denial of service attack, there will usually be many audits for failed IKE negotiations to spoofed IP addresses.  Otherwise, the machine is just extremely heavily loaded.  \r\n
0x4bad028f | IKE has recovered from denial of service prevention mode and has resumed normal operation.\r\n
0x4bad0290 | Certificate based Identity.  \r\nPeer IP Address: %1\r\n
0x4bad0291 | Sent first (SA) payload\r\n
0x4bad0292 | Processed first (SA) payload\r\n
0x4bad0293 | Processed second (KE) payload\r\n
0x4bad0294 | Processed third (ID) payload\r\n
0x4bad0295 | Processed second (KE) payload, need extra round trip\r\n
0x4bad0296 | Processed Quick Mode payload\r\n
0x4bad0297 | Quick Mode finished\r\n
0x4bad0298 | Unknown state\r\n
0x4bad0299 | Initiator.  Delta Time %1\r\n
0x4bad029a | Responder.  Delta Time %1\r\n
0x4bad029b | Initiator(Internal).  Delta Time %1\r\n
0x4bad029c | Floated-Port IKE Exempt %1%0\r\n
0x4bad02a4 | Formatting audit failed.  Dumping as bytes.\r\n
0xcbad02a5 | OAKLEY_STATUS_SET\r\n
0xcbad02a6 | OAKLEY_REINIT_NEEDED\r\n
0xcbad02a7 | OAKLEY_STATUS_INACTIVE\r\n
0xcbad02a8 | OAKLEY_POLICY_TOO_GENERAL\r\n
0xcbad02a9 | ERROR_IPSEC_IKE_DOS_REQUIRED\r\n
