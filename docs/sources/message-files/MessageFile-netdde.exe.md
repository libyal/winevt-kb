## netdde.exe

Path: %SystemRoot%\System32\netdde.exe

### 5.0.2195.6601, 5.1.2600.5512, 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00000001 | NetDDE Service on node "%1" started.\r\n
0x00000002 | NetDDE Service on node "%1" has been stopped.\r\n
0x00000003 | Invalid COPYDATA size %1 received.\r\n
0x00000004 | Invalid COPYDATA command %1 received.\r\n
0x00000005 | Failed creating new server packetizer for connection id %d\r\n
0x00000006 | NetDDE Agent %1 Coming Alive\r\n
0x00000007 | NetDDE Agent %1 Dying\r\n
0x00000008 | Cannot load function address of "%1" from "%2" DLL\r\n
0x00000009 | Error loading "%1" DLL: %2\r\n
0x0000000a | Error loading "%1" DLL functions\r\n
0x0000000b | Wrong version of "%1" DLL: %2\r\nDisabling this interface.\r\n
0x0000000c | Initialization of "%1" DLL failed\r\n
0x0000000d | Cannot close while DDE conversations are in progress. WM_CLOSE ignored.\r\n
0x0000000e | DdeGetQualityOfService() failed: %1\r\n
0x0000000f | WM_DDE_ACK received, WinInfo in unknown state: %1\r\n
0x00000010 | Too many terminates received or wrong window:\r\n%1\r\n%2\r\n
0x00000011 | Invalid network node name: "%1" from "%2"\r\n
0x00000012 | No application name: "%1"\r\n
0x00000013 | Invalid application name: "%1" from "%2"\r\n
0x00000014 | Could not create client-side agent window for "%1" client\r\n
0x00000015 | Extraneous %1 from DDE Client "%2"\r\n
0x00000016 | WM_DDE_ACK from DDE Client "%1" not matching DATA: %2\r\n
0x00000017 | Extraneous WM_DDE_DATA response from DDE Server "%1"\r\n
0x00000018 | %1 from DDE Server "%2" not matching %3: %4\r\n
0x00000019 | NULL hData from WM_DDE_ADVISE Client: "%1"\r\n
0x0000001a | Overflow of queue (%1) while waiting for initial advise\r\n
0x0000001b | Error adding atom: "%1" ==> %2,\r\nAtom retrieved: "%3"\r\n
0x0000001c | Unable to add atom "%1" ==> NULL\r\n
0x0000001d | RequestExec(): Command Line non-existent.\r\n
0x0000001e | GetShareInfo Error: %1\r\n
0x0000001f | Share "%1" not shareable with remote nodes\r\n
0x00000020 | GetShareInfo "%1" Size Error: %2 / %3\r\n
0x00000021 | Access Denied. Granted access = %1, Error code: %2\r\n
0x00000022 | Unknown Share Type: %1\r\n
0x00000023 | Could not create server-side agent window\r\nfor client app "%1" on node "%2"\r\n
0x00000024 | IpcInitConversation: null App "%1" or Topic "%2" atoms\r\n
0x00000025 | EXEC of "%1" failed: status = %2\r\n
0x00000026 | EXEC of "%1" failed: unknown status!\r\n
0x00000027 | Message: %1 to a non-existent window: %2\r\n
0x00000028 | INTERNAL ERROR -- DDE ACK to an unknown DDE Command: %1\r\n
0x00000029 | INTERNAL ERROR -- IpcXmitPacket %1 hDder handle should match %2\r\n
0x0000002a | Lock failed for %1 memory alloc\r\n
0x0000002b | Not enough memory for %1 bytes msg: WM_DDE_EXECUTE\r\n
0x0000002c | IpcXmitPacket(%1): null Item atom for "%2"\r\n
0x0000002d | Extraneous ACK apparently to an %1\r\nFrom "%2" client -> "%3" app\r\n
0x0000002e | %1 ACK not to an %1 [%2]\r\nFrom "%3" client -> "%4" app\r\n
0x0000002f | IpcXmitPkt() UNKNOWN CMD: %1\r\n
0x00000030 | Not enough memory for metafile copy: %1\r\n
0x00000031 | No metafile in metafilepict\r\n
0x00000032 | Could not lock metafilepict\r\n
0x00000033 | Could not lock memory for metafile handle\r\n
0x00000034 | Not enough memory for metafilepict: %1\r\n
0x00000035 | Not enough memory for bitmap copy: %1\r\n
0x00000036 | Could not lock bitmap\r\n
0x00000037 | Could not lock memory for bitmap handle\r\n
0x00000038 | Unable to add to DDE msg queue. Newest: %1, Oldest: %2, Entries: %3\r\n
0x00000039 | DDEQFree() releasing invalid msg handle %1\r\n
0x0000003a | Internal Error -- Unknown Security Type %1\r\n
0x0000003b | Could not create password dialog box: %1\r\n
0x0000003c | Invalid share type request: %1\r\n
0x0000003d | Unable to open current thread or process token: %1\r\n
0x0000003e | Unable to get user account info from open token: %1\r\n
0x0000003f | Unable to get user token info: %1\r\n
0x00000040 | Unable to impersonate DDE client: %1\r\n
0x00000041 | Cannot add "%1" DLL.\r\nAlready have maximum number of network interface DLLs\r\n
0x00000042 | Cannot add "%1" DLL.\r\nNetwork Interface DLL table exceeded maximum\r\n
0x00000043 | Unable to launch NetDDE main thread from service: %1\r\n
0x00000044 | Unable to launch DSDM main thread from service: %1\r\n
0x00000045 | StartServiceCtrlDispatcher() Failed: %1\r\n
0x00000046 | SetServiceStatus() Failed: %1\r\n
0x00000047 | ServiceControlManagerStop() to NetDDE\r\n
0x00000048 | ServiceControlManagerStop() to NetDDEdsdm\r\n
0x00000049 | NetDDE Agent is not running in user context.\r\nCannot initiate conversation.\r\n
0x0000004a | GetMetaFileBitsEx() failed: %1\r\n
0x0000004b | SetMetaFileBitsEx() failed: %1\r\n
0x0000004c | GetEnhMetaFileBits() failed: %1\r\n
0x0000004d | SetEnhMetaFileBits() failed: %1\r\n
0x0000004e | GetPaletteEntries() failed: %1\r\n
0x0000004f | CreatePalette() failed: %1\r\n
0x00000050 | Unable to allocate enough memory [%1] for %2 conversion: %3\r\n
0x00000051 | GlobalSize() for indirect object failed: %1\r\n
0x00000064 | Unable to allocate enough (%2) memory for a %1 packet\r\n
0x00000065 | Unable to allocate enough (%1) memory for packet copy\r\n
0x00000066 | SECURITY VIOLATION: %1 on "%2"\r\n
0x00000067 | SECURITY VIOLATION: DDE_EXECUTE\r\n
0x00000068 | %1 will not auto-close ... not enough timers\r\n
0x00000069 | Packet out of sequence from "%1"\r\nReceived: %2, Expecting %3, Status: %4\r\n
0x0000006a | Transmit timeout (%2 secs) to "%1" ... closing connection\r\n
0x0000006b | No connect commnad for (%2 secs) from "%1" ... closing connection\r\n
0x0000006c | No connect commnad response for (%2 secs) from "%1" ... closing connection\r\n
0x0000006d | Pausing (%2 secs) for remote side "%1" to get memory ... retrying\r\n
0x0000006e | No response %2/%3 from remote side "%1" for pktid %4\r\n
0x0000006f | Too many no response retries (%2) for same packet from "%1" ... closing connection\r\n
0x00000070 | "%1" node does not speak any of our protocols\r\n
0x00000071 | "%1" node selected an invalid protocol: %2\r\n
0x00000072 | "%1" their name was not "%2"\r\n
0x00000073 | Unusual connect name error %2 from %1\r\n
0x00000074 | Unusual connect error from %1. Class: %2, Error: %3\r\n
0x00000075 | Too many transmit retries (%2) for same packet to "%1" ... closing connection\r\n
0x00000076 | Transmit error on pktid %2 to "%1"\r\n
0x00000077 | Too many retries to "%1" for xmit errors (%2) ... closing connection\r\n
0x00000078 | Memory error on pktid %2 xmitted to "%1"\r\n
0x00000079 | Too many xmit retries to "%1" for memory errors (%2) ... closing connection\r\n
0x0000007a | Out of timers to start a memory pause for a xmit to "%1"\r\n
0x0000007b | Unexpectedly got a NULL router in ProcessHopBroken!\r\n
0x0000007c | Exceeded 100 expands in routing lookup!\r\nRoute info bogus: %1\r\n
0x00000082 | ROUTE ERROR %1: "%2"->"%3" @ "%4":\r\nUnknown route error!\r\n
0x00000083 | "%1" their name is the same as ours "%2"\r\n
0x000000c8 | Connect failed to "%1": %2\r\n
0x000000c9 | Receive error. Session to %1 closed abnormally: %2\r\n
0x000000ca | Send error. Session to %1 closed abonormally: %2\r\n
0x000000cb | Not enough memory for Listen NCB\r\n
0x000000cc | Attempt to determine the number of Lanas failed.\r\n
0x000000cd | Unable to delete our name "%1" from interface: status = %2\r\n
0x000000ce | Listen failed: %1\r\n
0x000000cf | Node name too long for connect on NetBIOS: "%1"\r\n
0x000000d0 | Local node name too long for use on NetBIOS: "%1"\r\n
0x000000d1 | NetBIOS Reset Adapter Command on Lana number %1 failed: %2\r\n
0x000000d2 | Int 5C Vector set but NetBIOS not installed.\r\n
0x000000d3 | NetBIOS Adapter Status Query on Lana number %1 failed: %2\r\n
0x000000d4 | Node name "%1" already in use on Lana number %2\r\n
0x000000d5 | Unknown Error Code returned by Lana number %1 while adding node name to network: %2\r\n
0x000000d6 | Setting up initial listen failed.\r\n
0x00000190 | Cannot impersonate client: %1\r\n
0x00000191 | NDdeShareDel RegDeleteKey error (%1)(%2) LE:%3\r\n
0x00000192 | NDdeApiInit - could not build the ShareDatabase SD\r\n
0x00000193 | LocalAlloc failed: %1\r\n
0x00000194 | InitializeAcl failed: %1\r\n
0x00000195 | AddAccessAllowedAce failed: %1\r\n
0x00000196 | GetAce failed: %1\r\n
0x00000197 | AllocateAndInitializeSid failed: %1\r\n
0x00000198 | SetSecurityDescriptorOwner failed: %1\r\n
0x00000199 | SetSecurityDescriptorGroup failed: %1\r\n
0x0000019a | SetSecurityDescriptorDacl failed: %1\r\n
0x0000019b | MakeSelfRelative failed: %1\r\n
0x0000019c | Could not read the ShareName Security Descriptor: %1\r\n
0x0000019d | Unable to add %1 to DDE msg queue.  Conversation terminated.\r\n
0x0000019e | Memory failure at line %1 of file %2.\r\n
