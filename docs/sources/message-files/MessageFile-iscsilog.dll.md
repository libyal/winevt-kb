## iscsilog.dll

Path: %SystemRoot%\System32\iscsilog.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x40000020 | Initiator received an asynchronous logout message. The Target name is given in the dump data.\r\n
0x40000022 | A connection to the target was lost, but Initiator successfully reconnected to the target. Dump data contains the target name.\r\n
0x40000040 | Attempt to bootstrap Windows using iSCSI NIC Boot (iBF)\r\n
0xc0000001 | Initiator failed to connect to the target. Target IP address and TCP Port number are given in dump data.\r\n
0xc0000002 | The initiator could not allocate resources for an iSCSI session.\r\n
0xc0000003 | Maximum command sequence number is not serially greater than expected command sequence number in login response.\r\nDump data contains Expected Command Sequence number followed by Maximum Command Sequence number.\r\n
0xc0000004 | MaxBurstLength is not serially greater than FirstBurstLength.\r\nDump data contains FirstBurstLength followed by MaxBurstLength.\r\n
0xc0000005 | Failed to setup initiator portal. Error status is given in the dump data.\r\n
0xc0000006 | The initiator could not allocate resources for an iSCSI connection\r\n
0xc0000007 | The initiator could not send an iSCSI PDU. Error status is given in the dump data.\r\n
0xc0000008 | Target or discovery service did not respond in time for an iSCSI request sent by the initiator. \r\niSCSI Function code is given in the dump data. For details about iSCSI Function code please refer \r\nto iSCSI User's Guide.\r\n
0xc0000009 | Target did not respond in time for a SCSI request. The CDB is given in the dump data.\r\n
0xc000000a | Login request failed. The login response packet is given in the dump data.\r\n
0xc000000b | Target returned an invalid login response packet. The login response packet is given in the dump data.\r\n
0xc000000c | Target provided invalid data for login redirect. Dump data contains the data returned by the target.\r\n
0xc000000d | Target offered an unknown AuthMethod. Dump data contains the data returned by the target.\r\n
0xc000000e | Target offered an unknown digest algorithm for CHAP. Dump data contains the data returned by the target.\r\n
0xc000000f | CHAP challenge given by the target contains invalid characters. Dump data contains the challenge given.\r\n
0xc0000010 | An invalid key was received during CHAP negotiation. The key=value pair is given in the dump data.\r\n
0xc0000011 | CHAP Response given by the target did not match the expected one. Dump data contains the CHAP response.\r\n
0xc0000012 | Header Digest is required by the initiator, but target did not offer it.\r\n
0xc0000013 | Data Digest is required by the initiator, but target did not offer it.\r\n
0xc0000014 | Connection to the target was lost. The initiator will attempt to retry the connection.\r\n
0xc0000015 | Data Segment Length given in the header exceeds MaxRecvDataSegmentLength declared by the target.\r\n
0xc0000016 | Header digest error was detected for the given PDU. Dump data contains the header and digest.\r\n
0xc0000017 | Target sent an invalid iSCSI PDU. Dump data contains the entire iSCSI header.\r\n
0xc0000018 | Target sent an iSCSI PDU with an invalid opcode. Dump data contains the entire iSCSI header.\r\n
0xc0000019 | Data digest error was detected. Dump data contains the calculated checksum followed by the given checksum.\r\n
0xc000001a | Target trying to send more data than requested by the initiator.\r\n
0xc000001b | Initiator could not find a match for the initiator task tag in the received PDU. Dump data contains the entire iSCSI header.\r\n
0xc000001c | Initiator received an invalid R2T packet. Dump data contains the entire iSCSI header.\r\n
0xc000001d | Target rejected an iSCSI PDU sent by the initiator. Dump data contains the rejected PDU.\r\n
0xc000001e | Initiator could not allocate a workitem for processing a request.\r\n
0xc000001f | Initiator could not allocate resource for processing a request.\r\n
0xc0000021 | Challenge size given by the target exceeds the maximum specified in iSCSI specification.\r\n
0xc0000023 | Target CHAP secret is smaller than the minimum size (12 bytes) required by the spec. \r\n
0xc0000024 | Initiator CHAP secret is smaller than the minimum size (12 bytes) required by the spec. Dump data contains the given CHAP secret.\r\n
0xc0000025 | FIPS service could not be initialized. Persistent logons will not be processed.\r\n
0xc0000026 | Initiator requires CHAP for logon authentication, but target did not offer CHAP.\r\n
0xc0000027 | Initiator sent a task management command to reset the target. The target name is given in the dump data.\r\n
0xc0000028 | Target requires logon authentication via CHAP, but Initiator is not configured to perform CHAP.\r\n
0xc0000029 | Target did not send AuthMethod key during security negotiation phase.\r\n
0xc000002a | Target sent an invalid status sequence number for a connection. Dump data contains \r\nExpected Status Sequence number followed by the given status sequence number.\r\n
0xc000002b | Target failed to respond in time for a login request.\r\n
0xc000002c | Target failed to respond in time for a logout request.\r\n
0xc000002d | Target failed to respond in time for a login request. This login request was for adding a new connection to a session.\r\n
0xc000002e | Target failed to respond in time for a SendTargets command.\r\n
0xc000002f | Target failed to respond in time for a SCSI command sent through a WMI request.\r\n
0xc0000030 | Target failed to respond in time to a NOP request.\r\n
0xc0000031 | Target failed to respond in time to a Task Management request.\r\n
0xc0000032 | Target failed to respond in time to a Text Command sent to renegotiate iSCSI parameters.\r\n
0xc0000033 | Target failed to respond in time to a logout request sent in response to an asynchronous message from the target.\r\n
0xc0000034 | Initiator Service failed to respond in time to a request to configure IPSec resources for an iSCSI connection.\r\n
0xc0000035 | Initiator Service failed to respond in time to a request to release IPSec resources allocated for an iSCSI connection.\r\n
0xc0000036 | Initiator Service failed to respond in time to a request to encrypt or decrypt data.\r\n
0xc0000037 | Initiator failed to allocate resources to send data to target.\r\n
0xc0000038 | Initiator could not map an user virtual address to kernel virtual address resulting in I/O failure. \r\n
0xc0000039 | Initiator could not allocate required resources for processing a request resulting in I/O failure. \r\n
0xc000003a | Initiator could not allocate a tag for processing a request resulting in I/O failure. \r\n
0xc000003b | Target dropped the connection before the initiator could transition to Full Feature Phase.\r\n
0xc000003c | Target sent data in SCSI Response PDU instead of Data_IN PDU. Only Sense Data can be sent in SCSI Response.\r\n
0xc000003d | Target set DataPduInOrder to NO when initiator requested YES. Login will be failed.\r\n
0xc000003e | Target set DataSequenceInOrder to NO when initiator requested YES. Login will be failed.\r\n
0xc000003f | Can not Reset the Target or LUN. Will attempt session recovery.\r\n

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.18362.449, 10.0.19041.1, 10.0.19041.610, 10.0.22000.1

Message identifier | Message string
--- | ---
0x40000020 | Initiator received an asynchronous logout message. The Target name is given in the dump data.\r\n
0x40000022 | A connection to the target was lost, but Initiator successfully reconnected to the target. Dump data contains the target name.\r\n
0x40000040 | Attempt to bootstrap Windows using iSCSI NIC Boot (iBF)\r\n
0x40000043 | If Digest support selected for iSCSI Session, Will use Processor support for Digest computation.\r\n
0x40000047 | Initiator did not start a session recovery upon receiving the request. Dump data contains the error status.\r\n
0xc0000001 | Initiator failed to connect to the target. Target IP address and TCP Port number are given in dump data.\r\n
0xc0000002 | The initiator could not allocate resources for an iSCSI session.\r\n
0xc0000003 | Maximum command sequence number is not serially greater than expected command sequence number in login response.\r\nDump data contains Expected Command Sequence number followed by Maximum Command Sequence number.\r\n
0xc0000004 | MaxBurstLength is not serially greater than FirstBurstLength.\r\nDump data contains FirstBurstLength followed by MaxBurstLength.\r\n
0xc0000005 | Failed to setup initiator portal. Error status is given in the dump data.\r\n
0xc0000006 | The initiator could not allocate resources for an iSCSI connection\r\n
0xc0000007 | The initiator could not send an iSCSI PDU. Error status is given in the dump data.\r\n
0xc0000008 | Target or discovery service did not respond in time for an iSCSI request sent by the initiator. \r\niSCSI Function code is given in the dump data. For details about iSCSI Function code please refer \r\nto iSCSI User's Guide.\r\n
0xc0000009 | Target did not respond in time for a SCSI request. The CDB is given in the dump data.\r\n
0xc000000a | Login request failed. The login response packet is given in the dump data.\r\n
0xc000000b | Target returned an invalid login response packet. The login response packet is given in the dump data.\r\n
0xc000000c | Target provided invalid data for login redirect. Dump data contains the data returned by the target.\r\n
0xc000000d | Target offered an unknown AuthMethod. Dump data contains the data returned by the target.\r\n
0xc000000e | Target offered an unknown digest algorithm for CHAP. Dump data contains the data returned by the target.\r\n
0xc000000f | CHAP challenge given by the target contains invalid characters. Dump data contains the challenge given.\r\n
0xc0000010 | An invalid key was received during CHAP negotiation. The key=value pair is given in the dump data.\r\n
0xc0000011 | CHAP Response given by the target did not match the expected one. Dump data contains the CHAP response.\r\n
0xc0000012 | Header Digest is required by the initiator, but target did not offer it.\r\n
0xc0000013 | Data Digest is required by the initiator, but target did not offer it.\r\n
0xc0000014 | Connection to the target was lost. The initiator will attempt to retry the connection.\r\n
0xc0000015 | Data Segment Length given in the header exceeds MaxRecvDataSegmentLength declared by the target.\r\n
0xc0000016 | Header digest error was detected for the given PDU. Dump data contains the header and digest.\r\n
0xc0000017 | Target sent an invalid iSCSI PDU. Dump data contains the entire iSCSI header.\r\n
0xc0000018 | Target sent an iSCSI PDU with an invalid opcode. Dump data contains the entire iSCSI header.\r\n
0xc0000019 | Data digest error was detected. Dump data contains the calculated checksum followed by the given checksum.\r\n
0xc000001a | Target trying to send more data than requested by the initiator.\r\n
0xc000001b | Initiator could not find a match for the initiator task tag in the received PDU. Dump data contains the entire iSCSI header.\r\n
0xc000001c | Initiator received an invalid R2T packet. Dump data contains the entire iSCSI header.\r\n
0xc000001d | Target rejected an iSCSI PDU sent by the initiator. Dump data contains the rejected PDU.\r\n
0xc000001e | Initiator could not allocate a workitem for processing a request.\r\n
0xc000001f | Initiator could not allocate resource for processing a request.\r\n
0xc0000021 | Challenge size given by the target exceeds the maximum specified in iSCSI specification.\r\n
0xc0000023 | Target CHAP secret is smaller than the minimum size (12 bytes) required by the spec. \r\n
0xc0000024 | Initiator CHAP secret is smaller than the minimum size (12 bytes) required by the spec. Dump data contains the given CHAP secret.\r\n
0xc0000025 | FIPS service could not be initialized. Persistent logons will not be processed.\r\n
0xc0000026 | Initiator requires CHAP for logon authentication, but target did not offer CHAP.\r\n
0xc0000027 | Initiator sent a task management command to reset the target. The target name is given in the dump data.\r\n
0xc0000028 | Target requires logon authentication via CHAP, but Initiator is not configured to perform CHAP.\r\n
0xc0000029 | Target did not send AuthMethod key during security negotiation phase.\r\n
0xc000002a | Target sent an invalid status sequence number for a connection. Dump data contains \r\nExpected Status Sequence number followed by the given status sequence number.\r\n
0xc000002b | Target failed to respond in time for a login request.\r\n
0xc000002c | Target failed to respond in time for a logout request.\r\n
0xc000002d | Target failed to respond in time for a login request. This login request was for adding a new connection to a session.\r\n
0xc000002e | Target failed to respond in time for a SendTargets command.\r\n
0xc000002f | Target failed to respond in time for a SCSI command sent through a WMI request.\r\n
0xc0000030 | Target failed to respond in time to a NOP request.\r\n
0xc0000031 | Target failed to respond in time to a Task Management request.\r\n
0xc0000032 | Target failed to respond in time to a Text Command sent to renegotiate iSCSI parameters.\r\n
0xc0000033 | Target failed to respond in time to a logout request sent in response to an asynchronous message from the target.\r\n
0xc0000034 | Initiator Service failed to respond in time to a request to configure IPSec resources for an iSCSI connection.\r\n
0xc0000035 | Initiator Service failed to respond in time to a request to release IPSec resources allocated for an iSCSI connection.\r\n
0xc0000036 | Initiator Service failed to respond in time to a request to encrypt or decrypt data.\r\n
0xc0000037 | Initiator failed to allocate resources to send data to target.\r\n
0xc0000038 | Initiator could not map an user virtual address to kernel virtual address resulting in I/O failure. \r\n
0xc0000039 | Initiator could not allocate required resources for processing a request resulting in I/O failure. \r\n
0xc000003a | Initiator could not allocate a tag for processing a request resulting in I/O failure. \r\n
0xc000003b | Target dropped the connection before the initiator could transition to Full Feature Phase.\r\n
0xc000003c | Target sent data in SCSI Response PDU instead of Data_IN PDU. Only Sense Data can be sent in SCSI Response.\r\n
0xc000003d | Target set DataPduInOrder to NO when initiator requested YES. Login will be failed.\r\n
0xc000003e | Target set DataSequenceInOrder to NO when initiator requested YES. Login will be failed.\r\n
0xc000003f | Can not Reset the Target or LUN. Will attempt session recovery.\r\n
0xc0000041 | Booting from iSCSI, but Could not set any NIC in Paging Path.\r\n
0xc0000042 | Attempt to disable the Nagle Algorithm for iSCSI connection failed.\r\n
0xc0000044 | After receiving an async logout from the target, attempt to relogin the session failed.  Error status is given in the dump data.\r\n
0xc0000045 | Attempt to recover an unexpected terminated session failed. Error status is given in the dump data.\r\n
0xc0000046 | Error occurred when processing iSCSI logon request. The request was not retried. Error status is given in the dump data.\r\n
0xc0000048 | Unexpected target portal IP types. Dump data contains the expected IP type.\r\n
