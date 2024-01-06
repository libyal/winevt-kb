## kdcsvc.dll

Path: %SystemRoot%\System32\kdcsvc.dll

### 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00000001 | KDC\r\n
0x00000002 | Max\r\n
0x00000009 | The password on the KRBTGT account was changed.\r\n
0x40000018 | A service ticket request by client %1 for %2 was rejected because User2User was \r\nrequired. The KDC responds with this error when a client requests a service ticket \r\nfor a user principal (a security risk). The client must support User2User in order \r\nto obtain a service ticket for the requested service principal\r\n
0x80000003 | Could not find principal %1\r\n
0x80000004 | Domain %1 propagated to us but did not authenticate\r\n
0x8000000c | A request failed from client realm %1 for a ticket in realm %2.\r\nThis failed because a trust link between the realms is non transitive.\r\n
0x80000013 | This event indicates an attempt was made to use smartcard logon,\r\nbut the KDC is unable to use the PKINIT protocol because it is missing a\r\nsuitable certificate.\r\n
0x80000014 | The currently selected KDC certificate was once valid, but now is invalid\r\nand no suitable replacement was found.  Smartcard logon may not function correctly\r\nif this problem is not remedied.  Have the system administrator check on the\r\nstate of the domain's public key infrastructure.  The chain status is in\r\nthe error data.\r\n
0x80000015 | The client certificate for the user %1\%2 is not valid, and resulted in a\r\nfailed smartcard logon.  Please contact the user for more information\r\nabout the certificate they're attempting to use for smartcard logon. The\r\nchain status was : %3\r\n
0x80000016 | The KDC encountered a trust loop when building a list of trusted domains.\r\nThis indicates that the route to the domain %1 from this KDC has more than\r\none possible trust path.\r\n
0x80000017 | The KDC received invalid messages of type %1.\r\n
0x80000019 | The account %1 from domain %2 is attempting to use S4USelf for the target client %3, \r\nbut is not allowed to perform group expansion on this client's user object.  \r\nIt may be necessary to adjust the ACL on the TokenGroupsGlobalAndUniversal\r\nattribute on the target client's user object to allow S4USelf to function correctly.  \r\nThis can also be accomplished by adding %1 to the Windows Authorization Access Group.\r\n
0xc0000005 | The KDC failed to update policy class %1. The error is in the data.\r\n
0xc0000006 | The KDC failed to update the trusted domain list. The error is in the data.\r\n
0xc0000007 | The Security Account Manager failed a KDC request in an unexpected way. The\r\nerror is in the data field. The account name was %1 and lookup type %2.\r\n
0xc0000008 | The account %1 did not have a suitable key for generating a Kerberos ticket.\r\nIf the encryption type is supported, changing or setting the password will\r\ngenerate a proper key.  The missing key type may be in the data field.\r\n
0xc000000a | The attempt to change the password on the KRBTGT account failed. The error\r\ncode is in the data field\r\n
0xc000000b | There are multiple accounts with name %1 of type %2.\r\n
0xc000000d | The account for %1 has corrupt keys stored in the DS.  Changing\r\nor setting the password should restore correct keys.\r\n
0xc000000e | While processing an AS request for target service %1, the account %2 did not \r\nhave a suitable key for generating a Kerberos ticket (the missing key has an ID\r\nof %3).  The requested etypes were %4.  The accounts available etypes were %5.  \r\nChanging or resetting the password of %6 will generate a proper key.\r\n
0xc000000f | The request for an AS ticket for client %1 was forwarded to the PDC.  An\r\ninvalid response to this forwarded request was detected and could indicate an\r\nattempt to spoof your PDC. There may be additional information in the data field.\r\n
0xc0000010 | While processing a TGS request for the target server %1, the account %2 did not\r\nhave a suitable key for generating a Kerberos ticket (the missing key has an ID\r\nof %3).  The requested etypes were %4.  The accounts available etypes were %5.  \r\nChanging or resetting the password of %6 will generate a proper key.\r\n
0xc0000011 | When updating policy class %1, the KDC encountered invalid policy data\r\nand has failed to update the policy.\r\n
0xc0000012 | During TGS processing, the KDC was unable to verify the signature on the\r\nPAC from %1. This indicates the PAC was modified.\r\n
0xc000001a | While processing an AS request for target service %1, the account %2 did not \r\nhave a suitable key for generating a Kerberos ticket (the missing key has an ID\r\nof %3). The requested etypes were %4.  The accounts available etypes were %5. \r\n
0xc000001b | While processing a TGS request for the target server %1, the account %2 did not\r\nhave a suitable key for generating a Kerberos ticket (the missing key has an ID\r\nof %3). The requested etypes were %4.  The accounts available etypes were %5. \r\n
