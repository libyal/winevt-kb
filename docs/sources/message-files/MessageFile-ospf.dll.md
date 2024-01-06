## ospf.dll

Path: %SystemRoot%\System32\ospf.dll

### 5.2.3790.3959

Message identifier | Message string
--- | ---
0x0000007c | OSPF_LAST_LOG\r\n
0x40000002 | Protocol initializing\r\n
0x40000003 | Protocol terminating\r\n
0x40000004 | Interface %1 up on circuit %2\r\n
0x40000006 | Lookup for %1/%2 failed\r\n
0x40000007 | BCSN:removing unreachable LS_SUM_NET %1 ar %2 area %3\r\n
0x40000008 | BCSN:added LS_SUM_NET %1 ar %2 area %3 cost %4\r\n
0x40000009 | entered BSN: lsId %1 ls-age %2 freeme %3\r\n
0x4000000a |    dist %1 tos %2 route %3 advrtr %4\r\n
0x4000000b | BSN:lsId %1 my_db %2 o_s_i_b %3 r %4 area_sh %5\r\n
0x4000000c | BSN: removing %1 ar %2 from %3\r\n
0x4000000d | BSN:found target: dist %1 age %2 free %3 route %4 hold %5\r\n
0x4000000e | BSN:removing infinity sum %1 ar %2 area %3\r\n
0x4000000f | ospf_die: MIB ensign gate died, call g_i_die()\r\n
0x40000010 | OSPF load gate started\r\n
0x40000011 | ospf_do_nothing received buffer list\r\n
0x40000012 | ospf_do_nothing got unexpected signal\r\n
0x40000013 | Received buffers in ospf_init_act()\r\n
0x40000014 | Ospf_init_act() didn't get INIT Signal\r\n
0x40000015 | Received buffers in ospf_soloist_init_act()\r\n
0x40000016 | Ospf_soloist_init_act() didn't get INIT Signal\r\n
0x40000017 | OSPF Soloist failed to send buffer to OSPF LSDB Gate\r\n
0x40000018 | OSPF detects soloist on this slot\r\n
0x40000019 | soloist also alive on remote slots: 0x%1\r\n
0x4000001a | OSPF terminated on this slot\r\n
0x4000001b | all OSPF soloists died, OSPF terminated on this slot\r\n
0x4000001c | ospf_soloist_proc_bufs rcvd buffer w/ Unknown OSPF type %1\r\n
0x4000001d | ospf_soloist_proc_bufs rcvd UNEXPECTED BUFFER\r\n
0x4000001e | ospf_soloist_act rcvd UNEXPECTED SIGNAL %1\r\n
0x4000001f | OSPF couldn't get a buffer, dying\r\n
0x40000022 | cfg error: ospf_get_mib_recs(): anb_x == Ip_anb_cnt\r\n
0x40000023 | OSPF LSDB MIB Gate received unknown MIB operation\r\n
0x40000024 | OSPF LSDB MIB Gate received unknown buffer\r\n
0x40000025 | Received unexpected input in ospf_lsdb_mib_act()\r\n
0x40000026 | ospf_find_area() could not find area %1\r\n
0x40000027 | DON'T SEND NET_OSPF_FAKE_RT TO IP_RTM !!!\r\n
0x40000028 | ospf_update_ip: dest  %1\r\n
0x40000029 | %1: dest %2 LSID %3 adv_rtr %4 \r\n
0x4000002a |   type %1  cost %2 pref %3 \r\n
0x4000002b | New route is better\r\n
0x4000002c | ospf_update_ip:route to %1 : add over delete. Crashing\r\n
0x4000002d | ospf_update_ip:route to %1 : delete over add. Crashing\r\n
0x4000002e | ospf_update_ip:route to %1 : delete over delete. Crashing\r\n
0x4000002f | addroute, lsdb is null\r\n
0x40000030 | ANR: resum: ar %1 lsId %2 area %3 rnp %4\r\n
0x40000031 | got intra route type %1 from %2 retrans %3\r\n
0x40000032 | g_fwd() to OSPF LSDB MIB Gate failed\r\n
0x40000033 | FLOOD_RECVD: %1 vr %2 a %3 src %4\r\n
0x40000034 |   LS_TYPE %1 metric %2  age %3  seq 0x%4 foundlsa %5 db->route %6 free %7\r\n
0x40000035 | CND: rm %1 a %2\r\n
0x40000036 | Running INTRA for AREA %1\r\n
0x40000037 |   LS_RTR %1  advrtr %2 dist %3 link_cnt %4\r\n
0x40000038 |     CTYPE  %1 lId %2 ldat %3 metric %4\r\n
0x40000039 |   STUB net list for area %1 after intra\r\n
0x4000003a |   lsId %1 advrtr %2 dist %3 db->route %4\r\n
0x4000003b |   NET list for area %1 after intra\r\n
0x4000003c | Running single INTER for lsId %1 ar %2 area %3\r\n
0x4000003d | Running INTER for area %1\r\n
0x4000003e | INTER: removing infinity sum %1 ar %2 area %3\r\n
0x4000003f | SUMNET list for area %1 after INTER\r\n
0x40000040 |   lsId %1 advrtr %2 dist %3 tos %4\r\n
0x40000041 |        db->route %1 age %2 free %3 hold %4\r\n
0x40000042 | BRD:removing sum %1 from area %2\r\n
0x40000043 | bdr_rtr_dwn: IP RNP 0x%2 IS DIFFERENT FROM db->route 0x%2\r\n
0x40000044 | bdr_rtr_dwn: db: net %1 mask %2 adv_rtr %3\r\n
0x40000045 | NDown: could not find nbr on IF\r\n
0x40000046 | DR = %1, BDR = %2\r\n
0x4000004a | T4: Originating new LSA - type %1 LSID %2 router %3\r\n
0x4000004b | T5: Received new LSA - type %1 LSID %2 router %3 neighbor %4\r\n
0x4000004d | T7: ADDED Route to %1 (%2) Type %3. Metric %4 Nexthop %5 (%6)\r\n
0x4000006c | %1\r\n
0x80000005 | Interface %1 down on circuit %2\r\n
0x80000047 | T1: IP Interface %1 Type: %2 Event: %3 State change %4-->%5\r\n
0x80000048 | T2: Neighbor %1 Event: %2 State change %3->%4\r\n
0x80000049 | T3: %1Designated Router changed on network: %2 %3->%4\r\n
0x8000004c | T6: CHANGED Route to %1 (%2) Type %3. Old metric %4 New metric %5 Old Nexthop %6 (%7) New nexthop %8 (%9)\r\n
0x8000004e | T8: DELETED Route to %1 (%2) Type %3. Metric was %4 Nexthop %5 (%6)\r\n
0x8000004f | C1: Packet Rejected: IP Hdr: BAD OSPF TYPE: %1.\r\n    src %2 dst %3 router ID %4\r\n
0x80000050 | C1: Packet Rejected: IP Hdr: BAD IP DEST\r\n    If Type %1 src %2 dst %3 routerId %4\r\n
0x80000051 | C1: Packet Rejected: IP Hdr: PKT SRC = MY IP ADDR\r\n    src %1 dst %2 routerId %3\r\n
0x80000052 | C1: Packet Rejected: BAD OSPF VERSION ver: %1\r\n    src %2 dst %3 routerId %4\r\n
0x80000053 | C1: Packet Rejected: CHECKSUM FAILURE\r\n    src %1 dst %2 routerId %3\r\n
0x80000054 | C1: Packet Rejected: AREA MISMATCH (%1)\r\n    src %2 dst %3 routerId %4\r\n
0x80000055 | C1: Packet Rejected: BAD VIRTUAL INFO\r\n    src %1 dst %2 routerId %3\r\n
0x80000056 | C1: Packet Rejected: AUTH TYPE(%1)\r\n    src %2 dst %3 routerId %4\r\n
0x80000057 | C1: Packet Rejected: AUTH KEY(0x%1 0x%2 0x%3 0x%4 0x%5 0x%6 0x%7 0x%8)\r\n    src %9 dst %10 routerId %11\r\n
0x80000058 | C2: Hello Rejected: NETMASK MISMATCH\r\n    src %1:%2 interface %3:%4\r\n
0x80000059 | C2: Hello Rejected: HELLO INTERVAL MISMATCH\r\n    src %1(%2)  interface %3(%4)\r\n
0x8000005a | C2: Hello Rejected: DEAD INTERVAL MISMATCH\r\n    src %1(%2)  interface %3(%4)\r\n
0x8000005b | C2: Hello Rejected: EXTERN OPTION MISMATCH\r\n    src %1(%2)  interface %3(%4)\r\n
0x8000005c | C2: Hello Rejected: UNKNOWN VIRTUAL NBR\r\n    src %1  interface %2\r\n
0x8000005d | C2: Hello Rejected: UNKNOWN NBMA NBR\r\n    src %1  interface %2\r\n
0x8000005e | C3: Packet Rejected: UNKNOWN NBR\r\n    src %1  type %2\r\n
0x8000005f | C3: Packet Rejected: SOURCE NEIGHBOR IN WRONG STATE\r\n    src %1 state %2 type %3\r\n
0x80000060 | C3: Packet Rejected: NBR's RTR = MY RTRID\r\n    src %1  type %2  rtrId %3\r\n
0x80000061 | C3: Packet Rejected: DD: EXTERN OPTION MISMATCH\r\n    src %1  interface %2\r\n
0x80000062 | C3: Packet Rejected: LS REQ: EMPTY REQUEST\r\n    src %1  type %2\r\n
0x80000063 | C3: Packet Rejected: LS REQ: BAD PACKET\r\n    src %1  interface %2\r\n
0x80000064 | C3: Packet Rejected: LS UPDATE: BAD LS CHECKSUM area %1\r\n    ls_Id %2  adv_rtr %3 type %4  src %5\r\n    ls_seq: %6 ls_age: %7  ls_chksum: %8 orig_chk: %9\r\n
0x80000065 | C3: Packet Rejected: LS UPDATE: LESS RECENT RX (%1)\r\n    src %2  type %3 ls_Id: %4 adv_rtr: %5\r\n    ls_seq: %6  ls_age: %7\r\n    db_seq: %8  db_age: %9 elapse: %10\r\n    freeme:%11 ackcnt:%12 nbr_retrans:%13 nbrEcnt:%14 Fcnt:%15\r\n
0x80000066 | C3: Packet Rejected: %1: UNKNOWN TYPE\r\n    src %2  type %3\r\n
0x80000067 | R3: Received more recent self-orignated LSA: type %1 LSID %2\r\n    router %3 neighbor %4\r\n
0x80000068 | R4: Ack received for non-existent LSA: type %1 LSID %2 neighbor %3\r\n
0x80000069 | N3: LSA of MaxAge flushed: type %1 LSID %2 router %3\r\n
0xc0000001 | System error, service attempting restart\r\n
0xc0000020 | ospf_get_mib_areas(): Invalid configuration. More than 1 area with no backbone area\r\n
0xc0000021 | ospf_get_mib_recs(): Invalid mib_rec_type\r\n
0xc000006a | Rejecting OSPF packet from %1 because it has Router ID of 0.0.0.0\r\n
0xc000006b | OSPF can not run because the router has Router ID of 0.0.0.0. Please change the ID to a non-zero value and restart the router\r\n
0xc000006d | ospf_get_mib_recs() Could not find area %1 for interface %2\r\n
0xc000006e | The OSPF global configuration has %1 global parameter blocks and %2 area parameter blocks. This is an invalid configuration.\r\n
0xc000006f | The OSPF configuration is invalid because it has virtual interfaces but no backbone (0.0.0.0) area record.\r\n
0xc0000070 | The virtual interface with a neighbour router ID of %1 has a transit area ID of 0.0.0.0. This is an invalid configuration because the backbone can not be a transit area.\r\n
0xc0000071 | The virtual interface with a neighbour router ID of %1 has a transit area ID of %2. However area %2 is a stub area and can not be a transit area.\r\n
0xc0000072 | The transit area %1 for the virtual interface with neigbour router ID of %2 does not exist.\r\n
0xc0000073 | The area range specification for area %1 with address %2 and mask %3 is invalid. (MASK & ADDRESS == ADDRESS)\r\n
0xc0000074 | The area range specification for area %1 with address %2 and mask %3 is invalid because the area does not exist.\r\n
0xc0000075 | An attempt was made to set OSPF Global information that deleted the area %1. This could not be completed successfully because the area currently has %2 interfaces attached to it. Please remove the interfaces or change the area they belong to before deleting the area.\r\n
0xc0000076 | Rejected an OSPF packet from %1 to %2 because the IP datagram length was %3. (The header length was %4). This OSPF implementation can not process such a large packet.\r\n
0xc0000077 | Rejected an OSPF packet from %1 to %2 because the IP header has options. The datagram length was %3 and the header length was %4. This OSPF implementation can not process IP packets with options\r\n
0xc0000078 | Rejected an OSPF packet from %1 to %2 because the OSPF data length in the OSPF header was %3 but the length calculated from the IP Header fields was %4.\r\n
0xc0000079 | Rejected a Link State Update from %1 (Router ID %2) because the sum of the lengths of the individual Link State Advertisements was more than the packet length.\r\n
0xc000007a | An attempt was made to add an interface which was to run in area %1. This was rejected because the area does not exist. Either change the area for the interface or add the area to OSPF.\r\n
0xc000007b | An unrecoverable error was made while parsing the interface information.\r\n
