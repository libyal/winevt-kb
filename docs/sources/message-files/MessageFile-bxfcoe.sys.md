## bxfcoe.sys

Path: %SystemRoot%\System32\drivers\bxfcoe.sys

### 7.4.6.0, 7.14.4.1, 7.14.15.2

Message identifier | Message string
--- | ---
0x40000003 | A new target with port WWN %2 detected on the fabric WWN %3\r\n
0x40000005 | Login to target port WWN %2 succeeded.\r\n
0x40000007 | The HBA starts with session offload disabled by registry. Running L2 path only.\r\n
0x40000008 | The SAN link is up for port WWN %2.\r\n
0x4000001c | Fabric login for local port WWN %3 to fabric WWN %2 succeeded.\r\n
0x4000001d | The target with port WWN %2 re-appeared in the fabric %3 directory list.\r\n
0x80000001 | The directory server for fabric WWN %3 returned no FCP targets for port WWN %2.\r\n
0x80000002 | The target with port WWN %2 disappeared from the fabric %3 directory list.\r\n
0x80000004 | The FCF with fabric WWN %2 disappeared from the network (periodic advertisements not seen anymore).\r\n
0x80000006 | Login to target port WWN %2 failed.\r\n
0x80000009 | The SAN link is down for port WWN %2.  Check to make sure the network cable is properly connected. \r\n
0x8000000c | A FIP Clear Virtual Link message received for the HBA port WWN %2; dropping all sessions and logging back to the FCF fabric WWN %3.\r\n
0x80000010 | Unable to offload target port WWN %2 I/O to the chip because of too many targets present. The target will not be accessible to OS.\r\n
0x80000013 | PLOGI LS_ACC from node WWN %2 is not compliant with FC-LS. See event log data for the LS_ACC payload.\r\n
0x80000014 | PRLI LS_ACC from node WWN %2 is not compliant with FC-LS. See event log data for the LS_ACC payload.\r\n
0x80000015 | FLOGI LS_ACC from FCF fabric WWN %2 is not compliant with FC-LS. See event log data for the LS_ACC payload.\r\n
0x80000017 | Stop chip access event received from lower layer driver.\r\n
0x80000018 | Restart chip access event received from lower layer driver.\r\n
0x80000019 | Current FCF changed fabric WWN from %2 to %3.  This can be due to fabric reconfiguration.\r\n
0x8000001b | Received logout(s) from target port WWN %2; will attempt to recover connection.\r\n
0x8000001d | Fabric login fabric name mismatch detected; will restart discovery.  Advertised WWN %2, FLOGI WWN %3.\r\n
0xc000000a | A request to the directory service was rejected. The response payload is in the log data.\r\n
0xc000000b | A SCR request failed. The response payload is in the log data.\r\n
0xc000000d | Fabric login to fabric WWN %2 rejected. Will retry 2 more times. See event log data for the RJT payload.\r\n
0xc000000e | NPIV fabric login for virtual port WWN %3 to fabric WWN %2 rejected. Will retry 2 more times. See event log data for the RJT payload.\r\n
0xc000000f | Assertion %2\r\n
0xc0000011 | Authentication node WWN %2 failed.\r\n
0xc0000012 | Authentication node WWN %2 rejected. Will retry 2 more times. See event log data for the RJT payload.\r\n
0xc0000016 | The FCoE FW failed to initialize.  Failure status is contained in the dump data.\r\n
0xc000001a | Another FCF is advertising a conflicting fabric WWN %2 on this VLAN.  Possible invalid FCF configuration.\r\n
0xc000001e | The FCoE driver failed to initialize.  Failure status is contained in the dump data.\r\n
