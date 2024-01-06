## netvsc.sys

Path: %SystemRoot%\system32\drivers\netvsc.sys

### 10.0.14393.0, 10.0.14393.351

Message identifier | Message string
--- | ---
0x00000001 | The VM and host networking components successfully negotiated protocol version '%2'\r\n
0x00000002 | The VM and host networking components failed to negotiate protocol version '%2'\r\n
0x00000003 | The miniport '%2' was successfully initialized\r\n
0x00000004 | Failed to initialize miniport '%2', Status = '%3'\r\n
0x00000005 | Failed to set config parameters on miniport NIC '%2', Status = '%5'\r\n
0x00000006 | Miniport NIC '%2' is halting\r\n
0x00000007 | Miniport NIC '%2' reset\r\n
0x00000008 | Miniport NIC '%2' hung\r\n
0x00000009 | Miniport NIC '%2' halted\r\n
0x0000000a | Miniport NIC '%2' paused\r\n
0x0000000b | Miniport NIC '%2' restarted\r\n
0x0000000c | Miniport NIC '%2' connected\r\n
0x0000000d | Miniport NIC '%2' disconnected\r\n
0x0000000e | Miniport NIC '%2' network has changed\r\n
0x0000000f | Microport initialization failed, reason = %1\r\n
0x00000022 | PD initialization succeeded. \r\n
0x00000023 | PD initialization failed. \r\n
0x00000024 | PD cleanup succeeded. \r\n
0x00000025 | Open NDK adapter failed. FailureReason: %2 MsgStatus: %1. \r\n
0x00000026 | NDK PnP event failed. FailureReason: %2 MsgStatus: %1. \r\n
0x00000027 | VF adapter bind failed. FailureReason: %2 MsgStatus: %1.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000010 | NBL %2 miniport NIC '%5' is dropped. Reason: %3. Status - %1. \r\n
0xb0000011 | Failed to send packet at the microport. Reason: %2. Status - %1. \r\n
0xd0000001 | Unknown\r\n
0xd0000002 | sent from\r\n
0xd0000003 | received by\r\n
0xd0000004 | Unknown\r\n
0xd0000005 | Packet was dropped at microport\r\n
0xd0000006 | Adapter is halting\r\n
0xd0000007 | Not enough resources to allocate message frame\r\n
0xd0000008 | The adapter has reached the maximum number of outstanding packets\r\n
0xd0000009 | VF adapter is not running\r\n
0xd000000a | Adapter is paused\r\n
0xd000000b | Failed to convert MDL to NBL\r\n
0xd000000c | Not enough resources to allocate NBL context\r\n
0xd000000d | The device did not start up properly, or the device has been surprised removed\r\n
0xd000000e | No VMBUS packets available\r\n
0xd000000f | Failed to allocate and prepare the send message\r\n
0xd0000010 | VMBUS could not transmit the packet\r\n
0xd0000011 | Unknown.\r\n
0xd0000012 | Invalid parameters.\r\n
0xd0000013 | RDMA is not supported on the VF adapter.\r\n
0xd0000014 | NDK adapter call failed on the VF protocol driver.\r\n
0xd0000015 | Null NDK adapter returned even though the call might have succeeded.\r\n
0xd0000016 | Insufficient resources.\r\n
0xd0000017 | Unknown.\r\n
0xd0000018 | Null parameters.\r\n
0xd0000019 | Invalid header type.\r\n
0xd000001a | Invalid header revision.\r\n
0xd000001b | Invalid header size for revision 1 PnP event.\r\n
0xd000001c | Invalid header size for revision 2 PnP event.\r\n
0xd000001d | Invalid flags for revision 2 PnP event.\r\n
0xd000001e | Invalid PnP event. For NDK, only NetEventNDKEnable and NetEventNDKDisable are allowed.\r\n
0xd000001f | Invalid buffer for NetEventNDKEnable.\r\n
0xd0000020 | NdkInfo passed in NDK capabilities was NULL for NetEventNDKEnable.\r\n
0xd0000021 | Invalid buffer for NetEventNDKDisable.\r\n
0xd0000022 | NDIS call to send NDK PnP event up failed.\r\n
0xd0000023 | Unknown.\r\n
0xd0000024 | Insufficient system resources.\r\n
0xd0000025 | Cannot open VF adapter.\r\n
0xd0000026 | Cannot retrieve VF serial number.\r\n
0xd0000027 | VF MTU mismatch.\r\n
0xd0000028 | Invalid VF device state.\r\n
0xd0000029 | VF media disconnected.\r\n
0xd000002a | Cannot switch to VF data path.\r\n
0xd000002b | Cannot set VF packet filter.\r\n

### 10.0.15063.0, 10.0.16299.15, 10.0.17134.1

Message identifier | Message string
--- | ---
0x00000001 | The VM and host networking components successfully negotiated protocol version '%2'\r\n
0x00000002 | The VM and host networking components failed to negotiate protocol version '%2'\r\n
0x00000003 | The miniport '%2' was successfully initialized\r\n
0x00000004 | Failed to initialize miniport '%2', Status = '%3'\r\n
0x00000005 | Failed to set config parameters on miniport NIC '%2', Status = '%5'\r\n
0x00000006 | Miniport NIC '%2' is halting\r\n
0x00000007 | Miniport NIC '%2' reset\r\n
0x00000008 | Miniport NIC '%2' hung\r\n
0x00000009 | Miniport NIC '%2' halted\r\n
0x0000000a | Miniport NIC '%2' paused\r\n
0x0000000b | Miniport NIC '%2' restarted\r\n
0x0000000c | Miniport NIC '%2' connected\r\n
0x0000000d | Miniport NIC '%2' disconnected\r\n
0x0000000e | Miniport NIC '%2' network has changed\r\n
0x0000000f | Microport initialization failed, reason = %1\r\n
0x00000022 | PD initialization succeeded. \r\n
0x00000023 | PD initialization failed. \r\n
0x00000024 | PD cleanup succeeded. \r\n
0x00000025 | Open NDK adapter failed on Miniport '%4'. FailureReason: %2 Status: %1. \r\n
0x00000026 | NDK PnP event failed. PnPEvent: %2 Miniport: '%5' FailureReason: %3 Status: %1.\r\n
0x00000027 | VF adapter bind failed. FailureReason: %2 MsgStatus: %1.\r\n
0x00000028 | Task, %1, failed because of low memory. %2 bytes of memory was required\r\n
0x00000029 | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' succeeded.\r\n
0x0000002a | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' failed. Status = %1. RequestHandled = %2. RDMA cannot be enabled on the adapter\r\n
0x0000002b | NDK PnP event succeeded. PnPEvent: %2 Miniport: '%5' \r\n
0x0000002c | Miniport '%4' reported NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002d | Miniport '%4' failed to report NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002e | VF adapter '%2' did not report NDK capabilities.\r\n
0x0000002f | VF adapter '%2' reported NDK capabilities in enabled operational state.\r\n
0x00000030 | VF adapter '%2' reported NDK capabilities in disabled operational state.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000010 | NBL %2 miniport NIC '%5' is dropped. Reason: %3. Status - %1. \r\n
0xb0000011 | Failed to send packet at the microport. Reason: %2. Status - %1. \r\n
0xd0000001 | Unknown\r\n
0xd0000002 | sent from\r\n
0xd0000003 | received by\r\n
0xd0000004 | Unknown\r\n
0xd0000005 | Packet was dropped at microport\r\n
0xd0000006 | Adapter is halting\r\n
0xd0000007 | Not enough resources to allocate message frame\r\n
0xd0000008 | The adapter has reached the maximum number of outstanding packets\r\n
0xd0000009 | VF adapter is not running\r\n
0xd000000a | Adapter is paused\r\n
0xd000000b | Failed to convert MDL to NBL\r\n
0xd000000c | Not enough resources to allocate NBL context\r\n
0xd000000d | The device did not start up properly, or the device has been surprised removed\r\n
0xd000000e | No VMBUS packets available\r\n
0xd000000f | Failed to allocate and prepare the send message\r\n
0xd0000010 | VMBUS could not transmit the packet\r\n
0xd0000011 | Unknown.\r\n
0xd0000012 | Invalid parameters.\r\n
0xd0000013 | RDMA is not supported on the VF adapter.\r\n
0xd0000014 | NDK adapter call failed on the VF protocol driver.\r\n
0xd0000015 | Null NDK adapter returned even though the call might have succeeded.\r\n
0xd0000016 | Insufficient resources.\r\n
0xd0000017 | Unknown.\r\n
0xd0000018 | Null parameters.\r\n
0xd0000019 | Invalid header type.\r\n
0xd000001a | Invalid header revision.\r\n
0xd000001b | Invalid header size for revision 1 PnP event.\r\n
0xd000001c | Invalid header size for revision 2 PnP event.\r\n
0xd000001d | Invalid flags for revision 2 PnP event.\r\n
0xd000001e | Invalid PnP event. For NDK, only NetEventNDKEnable and NetEventNDKDisable are allowed.\r\n
0xd000001f | Invalid buffer for NetEventNDKEnable.\r\n
0xd0000020 | NdkInfo passed in NDK capabilities was NULL for NetEventNDKEnable.\r\n
0xd0000021 | Invalid buffer for NetEventNDKDisable.\r\n
0xd0000022 | NDIS call to send NDK PnP event up failed.\r\n
0xd0000023 | Unknown.\r\n
0xd0000024 | Insufficient system resources.\r\n
0xd0000025 | Cannot open VF adapter.\r\n
0xd0000026 | Cannot retrieve VF serial number.\r\n
0xd0000027 | VF MTU mismatch.\r\n
0xd0000028 | Invalid VF device state.\r\n
0xd0000029 | VF media disconnected.\r\n
0xd000002a | Cannot switch to VF data path.\r\n
0xd000002b | Cannot set VF packet filter.\r\n
0xd000002c | Unknown\r\n
0xd000002d | Status indication object allocation\r\n
0xd000002e | Status indication buffer allocation\r\n
0xd000002f | Unknown NDK PnP event\r\n
0xd0000030 | NDK enable PnP event\r\n
0xd0000031 | NDK disable PnP event\r\n

### 10.0.17763.404

Message identifier | Message string
--- | ---
0x00000001 | The VM and host networking components successfully negotiated protocol version '%2'\r\n
0x00000002 | The VM and host networking components failed to negotiate protocol version '%2'\r\n
0x00000003 | The miniport '%2' was successfully initialized\r\n
0x00000004 | Failed to initialize miniport '%2', Status = '%3'\r\n
0x00000005 | Failed to set config parameters on miniport NIC '%2', Status = '%5'\r\n
0x00000006 | Miniport NIC '%2' is halting\r\n
0x00000007 | Miniport NIC '%2' reset\r\n
0x00000008 | Miniport NIC '%2' hung\r\n
0x00000009 | Miniport NIC '%2' halted\r\n
0x0000000a | Miniport NIC '%2' paused\r\n
0x0000000b | Miniport NIC '%2' restarted\r\n
0x0000000c | Miniport NIC '%2' connected\r\n
0x0000000d | Miniport NIC '%2' disconnected\r\n
0x0000000e | Miniport NIC '%2' network has changed\r\n
0x0000000f | Microport initialization failed, reason = %1\r\n
0x00000022 | PD initialization succeeded. \r\n
0x00000023 | PD initialization failed. \r\n
0x00000024 | PD cleanup succeeded. \r\n
0x00000025 | Open NDK adapter failed on Miniport '%4'. FailureReason: %2 Status: %1. \r\n
0x00000026 | NDK PnP event failed. PnPEvent: %2 Miniport: '%5' FailureReason: %3 Status: %1.\r\n
0x00000027 | VF adapter bind failed. FailureReason: %2 MsgStatus: %1.\r\n
0x00000028 | Task, %1, failed because of low memory. %2 bytes of memory was required\r\n
0x00000029 | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' succeeded.\r\n
0x0000002a | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' failed. Status = %1. RequestHandled = %2. RDMA cannot be enabled on the adapter\r\n
0x0000002b | NDK PnP event succeeded. PnPEvent: %2 Miniport: '%5' \r\n
0x0000002c | Miniport '%4' reported NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002d | Miniport '%4' failed to report NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002e | VF adapter '%2' did not report NDK capabilities.\r\n
0x0000002f | VF adapter '%2' reported NDK capabilities in enabled operational state.\r\n
0x00000030 | VF adapter '%2' reported NDK capabilities in disabled operational state.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000010 | NBL %2 miniport NIC '%5' is dropped. Reason: %3. Status - %1. \r\n
0xb0000011 | Failed to send packet at the microport. Reason: %2. Status - %1. \r\n
0xb0000012 | NBL %4 CorrelationID %5 on IfIndex %6 direction %2 dropped reason %3 status %1\r\n
0xb0000013 | NBL %2 CorrelationID %3 on IfIndex %4 direction %1 Synthetic\r\n
0xb0000014 | NBL %2 CorrelationID %3 on IfIndex %4 direction %1 VF\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | sent from\r\n
0xd0000003 | received by\r\n
0xd0000004 | Unknown\r\n
0xd0000005 | Packet was dropped at microport\r\n
0xd0000006 | Adapter is halting\r\n
0xd0000007 | Not enough resources to allocate message frame\r\n
0xd0000008 | The adapter has reached the maximum number of outstanding packets\r\n
0xd0000009 | VF adapter is not running\r\n
0xd000000a | Adapter is paused\r\n
0xd000000b | Failed to convert MDL to NBL\r\n
0xd000000c | Not enough resources to allocate NBL context\r\n
0xd000000d | The device did not start up properly, or the device has been surprised removed\r\n
0xd000000e | No VMBUS packets available\r\n
0xd000000f | Failed to allocate and prepare the send message\r\n
0xd0000010 | VMBUS could not transmit the packet\r\n
0xd0000011 | Unknown.\r\n
0xd0000012 | Invalid parameters.\r\n
0xd0000013 | RDMA is not supported on the VF adapter.\r\n
0xd0000014 | NDK adapter call failed on the VF protocol driver.\r\n
0xd0000015 | Null NDK adapter returned even though the call might have succeeded.\r\n
0xd0000016 | Insufficient resources.\r\n
0xd0000017 | Unknown.\r\n
0xd0000018 | Null parameters.\r\n
0xd0000019 | Invalid header type.\r\n
0xd000001a | Invalid header revision.\r\n
0xd000001b | Invalid header size for revision 1 PnP event.\r\n
0xd000001c | Invalid header size for revision 2 PnP event.\r\n
0xd000001d | Invalid flags for revision 2 PnP event.\r\n
0xd000001e | Invalid PnP event. For NDK, only NetEventNDKEnable and NetEventNDKDisable are allowed.\r\n
0xd000001f | Invalid buffer for NetEventNDKEnable.\r\n
0xd0000020 | NdkInfo passed in NDK capabilities was NULL for NetEventNDKEnable.\r\n
0xd0000021 | Invalid buffer for NetEventNDKDisable.\r\n
0xd0000022 | NDIS call to send NDK PnP event up failed.\r\n
0xd0000023 | Unknown.\r\n
0xd0000024 | Insufficient system resources.\r\n
0xd0000025 | Cannot open VF adapter.\r\n
0xd0000026 | Cannot retrieve VF serial number.\r\n
0xd0000027 | VF MTU mismatch.\r\n
0xd0000028 | Invalid VF device state.\r\n
0xd0000029 | VF media disconnected.\r\n
0xd000002a | Cannot switch to VF data path.\r\n
0xd000002b | Cannot set VF packet filter.\r\n
0xd000002c | Unknown\r\n
0xd000002d | Status indication object allocation\r\n
0xd000002e | Status indication buffer allocation\r\n
0xd000002f | Unknown NDK PnP event\r\n
0xd0000030 | NDK enable PnP event\r\n
0xd0000031 | NDK disable PnP event\r\n

### 10.0.18362.1

Message identifier | Message string
--- | ---
0x00000001 | The VM and host networking components successfully negotiated protocol version '%2'\r\n
0x00000002 | The VM and host networking components failed to negotiate protocol version '%2'\r\n
0x00000003 | The miniport '%2' was successfully initialized\r\n
0x00000004 | Failed to initialize miniport '%2', Status = '%3'\r\n
0x00000005 | Failed to set config parameters on miniport NIC '%2', Status = '%5'\r\n
0x00000006 | Miniport NIC '%2' is halting\r\n
0x00000007 | Miniport NIC '%2' reset\r\n
0x00000008 | Miniport NIC '%2' hung\r\n
0x00000009 | Miniport NIC '%2' halted\r\n
0x0000000a | Miniport NIC '%2' paused\r\n
0x0000000b | Miniport NIC '%2' restarted\r\n
0x0000000c | Miniport NIC '%2' connected\r\n
0x0000000d | Miniport NIC '%2' disconnected\r\n
0x0000000e | Miniport NIC '%2' network has changed\r\n
0x0000000f | Failed to initialize microport for miniport '%2', Status = '%3'\r\n
0x00000022 | PD initialization succeeded. \r\n
0x00000023 | PD initialization failed. \r\n
0x00000024 | PD cleanup succeeded. \r\n
0x00000025 | Open NDK adapter failed on Miniport '%4'. FailureReason: %2 Status: %1. \r\n
0x00000026 | NDK PnP event failed. PnPEvent: %2 Miniport: '%5' FailureReason: %3 Status: %1.\r\n
0x00000027 | VF adapter bind failed. FailureReason: %2 MsgStatus: %1.\r\n
0x00000028 | Task, %1, failed because of low memory. %2 bytes of memory was required\r\n
0x00000029 | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' succeeded.\r\n
0x0000002a | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' failed. Status = %1. RequestHandled = %2. RDMA cannot be enabled on the adapter\r\n
0x0000002b | NDK PnP event succeeded. PnPEvent: %2 Miniport: '%5' \r\n
0x0000002c | Miniport '%4' reported NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002d | Miniport '%4' failed to report NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002e | VF adapter '%2' did not report NDK capabilities.\r\n
0x0000002f | VF adapter '%2' reported NDK capabilities in enabled operational state.\r\n
0x00000030 | VF adapter '%2' reported NDK capabilities in disabled operational state.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000010 | NBL %2 miniport NIC '%5' is dropped. Reason: %3. Status - %1. \r\n
0xb0000011 | Failed to send packet at the microport. Reason: %2. Status - %1. \r\n
0xb0000012 | NBL %4 CorrelationID %5 on IfIndex %6 direction %2 dropped reason %3 status %1\r\n
0xb0000013 | NBL %2 CorrelationID %3 on IfIndex %4 direction %1 Synthetic\r\n
0xb0000014 | NBL %2 CorrelationID %3 on IfIndex %4 direction %1 VF\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | sent from\r\n
0xd0000003 | received by\r\n
0xd0000004 | Unknown\r\n
0xd0000005 | Packet was dropped at microport\r\n
0xd0000006 | Adapter is halting\r\n
0xd0000007 | Not enough resources to allocate message frame\r\n
0xd0000008 | The adapter has reached the maximum number of outstanding packets\r\n
0xd0000009 | VF adapter is not running\r\n
0xd000000a | Adapter is paused\r\n
0xd000000b | Failed to convert MDL to NBL\r\n
0xd000000c | Not enough resources to allocate NBL context\r\n
0xd000000d | The device did not start up properly, or the device has been surprised removed\r\n
0xd000000e | No VMBUS packets available\r\n
0xd000000f | Failed to allocate and prepare the send message\r\n
0xd0000010 | VMBUS could not transmit the packet\r\n
0xd0000011 | Unknown.\r\n
0xd0000012 | Invalid parameters.\r\n
0xd0000013 | RDMA is not supported on the VF adapter.\r\n
0xd0000014 | NDK adapter call failed on the VF protocol driver.\r\n
0xd0000015 | Null NDK adapter returned even though the call might have succeeded.\r\n
0xd0000016 | Insufficient resources.\r\n
0xd0000017 | Unknown.\r\n
0xd0000018 | Null parameters.\r\n
0xd0000019 | Invalid header type.\r\n
0xd000001a | Invalid header revision.\r\n
0xd000001b | Invalid header size for revision 1 PnP event.\r\n
0xd000001c | Invalid header size for revision 2 PnP event.\r\n
0xd000001d | Invalid flags for revision 2 PnP event.\r\n
0xd000001e | Invalid PnP event. For NDK, only NetEventNDKEnable and NetEventNDKDisable are allowed.\r\n
0xd000001f | Invalid buffer for NetEventNDKEnable.\r\n
0xd0000020 | NdkInfo passed in NDK capabilities was NULL for NetEventNDKEnable.\r\n
0xd0000021 | Invalid buffer for NetEventNDKDisable.\r\n
0xd0000022 | NDIS call to send NDK PnP event up failed.\r\n
0xd0000023 | Unknown.\r\n
0xd0000024 | Insufficient system resources.\r\n
0xd0000025 | Cannot open VF adapter.\r\n
0xd0000026 | Cannot retrieve VF serial number.\r\n
0xd0000027 | VF MTU mismatch.\r\n
0xd0000028 | Invalid VF device state.\r\n
0xd0000029 | VF media disconnected.\r\n
0xd000002a | Cannot switch to VF data path.\r\n
0xd000002b | Cannot set VF packet filter.\r\n
0xd000002c | Unknown\r\n
0xd000002d | Status indication object allocation\r\n
0xd000002e | Status indication buffer allocation\r\n
0xd000002f | Unknown NDK PnP event\r\n
0xd0000030 | NDK enable PnP event\r\n
0xd0000031 | NDK disable PnP event\r\n

### 10.0.19041.1, 10.0.19041.630

Message identifier | Message string
--- | ---
0x00000001 | The VM and host networking components successfully negotiated protocol version '%2'\r\n
0x00000002 | The VM and host networking components failed to negotiate protocol version '%2'\r\n
0x00000003 | The miniport '%2' was successfully initialized\r\n
0x00000004 | Failed to initialize miniport '%2', Status = '%3'\r\n
0x00000005 | Failed to set config parameters on miniport NIC '%2', Status = '%5'\r\n
0x00000006 | Miniport NIC '%2' is halting\r\n
0x00000007 | Miniport NIC '%2' reset\r\n
0x00000008 | Miniport NIC '%2' hung\r\n
0x00000009 | Miniport NIC '%2' halted\r\n
0x0000000a | Miniport NIC '%2' paused\r\n
0x0000000b | Miniport NIC '%2' restarted\r\n
0x0000000c | Miniport NIC '%2' connected\r\n
0x0000000d | Miniport NIC '%2' disconnected\r\n
0x0000000e | Miniport NIC '%2' network has changed\r\n
0x0000000f | Failed to initialize microport for miniport '%2', Status = '%3'\r\n
0x00000022 | PD initialization succeeded. \r\n
0x00000023 | PD initialization failed. \r\n
0x00000024 | PD cleanup succeeded. \r\n
0x00000025 | Open NDK adapter failed on Miniport '%4'. FailureReason: %2 Status: %1. \r\n
0x00000026 | NDK PnP event failed. PnPEvent: %2 Miniport: '%5' FailureReason: %3 Status: %1.\r\n
0x00000027 | VF adapter bind failed. FailureReason: %2 MsgStatus: %1.\r\n
0x00000028 | Task, %1, failed because of low memory. %2 bytes of memory was required\r\n
0x00000029 | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' succeeded.\r\n
0x0000002a | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' failed. Status = %1. RequestHandled = %2. RDMA cannot be enabled on the adapter\r\n
0x0000002b | NDK PnP event succeeded. PnPEvent: %2 Miniport: '%5' \r\n
0x0000002c | Miniport '%4' reported NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002d | Miniport '%4' failed to report NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002e | VF adapter '%2' did not report NDK capabilities.\r\n
0x0000002f | VF adapter '%2' reported NDK capabilities in enabled operational state.\r\n
0x00000030 | VF adapter '%2' reported NDK capabilities in disabled operational state.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000010 | NBL %2 miniport NIC '%5' is dropped. Reason: %3. Status - %1. \r\n
0xb0000011 | Failed to send packet at the microport. Reason: %2. Status - %1. \r\n
0xb0000012 | NBL %4 CorrelationID %5 on IfIndex %6 direction %2 dropped reason %3 status %1\r\n
0xb0000013 | NBL %2 CorrelationID %3 on IfIndex %4 direction %1 Synthetic\r\n
0xb0000014 | NBL %2 CorrelationID %3 on IfIndex %4 direction %1 VF\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | sent from\r\n
0xd0000003 | received by\r\n
0xd0000004 | Unknown\r\n
0xd0000005 | Packet was dropped at microport\r\n
0xd0000006 | Adapter is halting\r\n
0xd0000007 | Not enough resources to allocate message frame\r\n
0xd0000008 | The adapter has reached the maximum number of outstanding packets\r\n
0xd0000009 | VF adapter is not running\r\n
0xd000000a | Adapter is paused\r\n
0xd000000b | Failed to convert MDL to NBL\r\n
0xd000000c | Not enough resources to allocate NBL context\r\n
0xd000000d | The device did not start up properly, or the device has been surprised removed\r\n
0xd000000e | No VMBUS packets available\r\n
0xd000000f | Failed to allocate and prepare the send message\r\n
0xd0000010 | VMBUS could not transmit the packet\r\n
0xd0000011 | Unknown.\r\n
0xd0000012 | Invalid parameters.\r\n
0xd0000013 | RDMA is not supported on the VF adapter.\r\n
0xd0000014 | NDK adapter call failed on the VF protocol driver.\r\n
0xd0000015 | Null NDK adapter returned even though the call might have succeeded.\r\n
0xd0000016 | Insufficient resources.\r\n
0xd0000017 | Unknown.\r\n
0xd0000018 | Null parameters.\r\n
0xd0000019 | Invalid header type.\r\n
0xd000001a | Invalid header revision.\r\n
0xd000001b | Invalid header size for revision 1 PnP event.\r\n
0xd000001c | Invalid header size for revision 2 PnP event.\r\n
0xd000001d | Invalid flags for revision 2 PnP event.\r\n
0xd000001e | Invalid PnP event. For NDK, only NetEventNDKEnable and NetEventNDKDisable are allowed.\r\n
0xd000001f | Invalid buffer for NetEventNDKEnable.\r\n
0xd0000020 | NdkInfo passed in NDK capabilities was NULL for NetEventNDKEnable.\r\n
0xd0000021 | Invalid buffer for NetEventNDKDisable.\r\n
0xd0000022 | NDIS call to send NDK PnP event up failed.\r\n
0xd0000023 | Unknown.\r\n
0xd0000024 | Insufficient system resources.\r\n
0xd0000025 | Cannot open VF adapter.\r\n
0xd0000026 | Cannot retrieve VF serial number.\r\n
0xd0000027 | VF MTU mismatch.\r\n
0xd0000028 | Invalid VF device state.\r\n
0xd0000029 | VF media disconnected.\r\n
0xd000002a | Cannot switch to VF data path.\r\n
0xd000002b | Cannot set VF packet filter.\r\n
0xd000002c | Cannot set VF TCP offload parameters.\r\n
0xd000002d | Unknown\r\n
0xd000002e | Status indication object allocation\r\n
0xd000002f | Status indication buffer allocation\r\n
0xd0000030 | Unknown NDK PnP event\r\n
0xd0000031 | NDK enable PnP event\r\n
0xd0000032 | NDK disable PnP event\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000001 | The VM and host networking components successfully negotiated protocol version '%2'\r\n
0x00000002 | The VM and host networking components failed to negotiate protocol version '%2'\r\n
0x00000003 | The miniport '%2' was successfully initialized\r\n
0x00000004 | Failed to initialize miniport '%2', Status = '%3'\r\n
0x00000005 | Failed to set config parameters on miniport NIC '%2', Status = '%5'\r\n
0x00000006 | Miniport NIC '%2' is halting\r\n
0x00000007 | Miniport NIC '%2' reset\r\n
0x00000008 | Miniport NIC '%2' hung\r\n
0x00000009 | Miniport NIC '%2' halted\r\n
0x0000000a | Miniport NIC '%2' paused\r\n
0x0000000b | Miniport NIC '%2' restarted\r\n
0x0000000c | Miniport NIC '%2' connected\r\n
0x0000000d | Miniport NIC '%2' disconnected\r\n
0x0000000e | Miniport NIC '%2' network has changed\r\n
0x0000000f | Failed to initialize microport for miniport '%2', Status = '%3'\r\n
0x00000022 | PD initialization succeeded. \r\n
0x00000023 | PD initialization failed. \r\n
0x00000024 | PD cleanup succeeded. \r\n
0x00000025 | Open NDK adapter failed on Miniport '%4'. FailureReason: %2 Status: %1. \r\n
0x00000026 | NDK PnP event failed. PnPEvent: %2 Miniport: '%5' FailureReason: %3 Status: %1.\r\n
0x00000027 | VF adapter bind failed. FailureReason: %2 MsgStatus: %1.\r\n
0x00000028 | Task, %1, failed because of low memory. %2 bytes of memory was required\r\n
0x00000029 | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' succeeded.\r\n
0x0000002a | Sending Interface Index (IfIndex %3)of RNDIS miniport '%5' to VF adapter '%7' failed. Status = %1. RequestHandled = %2. RDMA cannot be enabled on the adapter\r\n
0x0000002b | NDK PnP event succeeded. PnPEvent: %2 Miniport: '%5' \r\n
0x0000002c | Miniport '%4' reported NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002d | Miniport '%4' failed to report NDK capabilities. Operation NDK enabled - %2.\r\n
0x0000002e | VF adapter '%2' did not report NDK capabilities.\r\n
0x0000002f | VF adapter '%2' reported NDK capabilities in enabled operational state.\r\n
0x00000030 | VF adapter '%2' reported NDK capabilities in disabled operational state.\r\n
0x00000031 | A VF connection failed due to isolated VM restriction. Status: %1\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | System\r\n
0xb0000010 | NBL %2 miniport NIC '%5' is dropped. Reason: %3. Status - %1. \r\n
0xb0000011 | Failed to send packet at the microport. Reason: %2. Status - %1. \r\n
0xb0000012 | NBL %4 CorrelationID %5 on IfIndex %6 direction %2 dropped reason %3 status %1\r\n
0xb0000013 | NBL %2 CorrelationID %3 on IfIndex %4 direction %1 Synthetic\r\n
0xb0000014 | NBL %2 CorrelationID %3 on IfIndex %4 direction %1 VF\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | sent from\r\n
0xd0000003 | received by\r\n
0xd0000004 | Unknown\r\n
0xd0000005 | Packet was dropped at microport\r\n
0xd0000006 | Adapter is halting\r\n
0xd0000007 | Not enough resources to allocate message frame\r\n
0xd0000008 | The adapter has reached the maximum number of outstanding packets\r\n
0xd0000009 | VF adapter is not running\r\n
0xd000000a | Adapter is paused\r\n
0xd000000b | Failed to convert MDL to NBL\r\n
0xd000000c | Not enough resources to allocate NBL context\r\n
0xd000000d | The device did not start up properly, or the device has been surprised removed\r\n
0xd000000e | No VMBUS packets available\r\n
0xd000000f | Failed to allocate and prepare the send message\r\n
0xd0000010 | VMBUS could not transmit the packet\r\n
0xd0000011 | Unknown.\r\n
0xd0000012 | Invalid parameters.\r\n
0xd0000013 | RDMA is not supported on the VF adapter.\r\n
0xd0000014 | NDK adapter call failed on the VF protocol driver.\r\n
0xd0000015 | Null NDK adapter returned even though the call might have succeeded.\r\n
0xd0000016 | Insufficient resources.\r\n
0xd0000017 | Unknown.\r\n
0xd0000018 | Null parameters.\r\n
0xd0000019 | Invalid header type.\r\n
0xd000001a | Invalid header revision.\r\n
0xd000001b | Invalid header size for revision 1 PnP event.\r\n
0xd000001c | Invalid header size for revision 2 PnP event.\r\n
0xd000001d | Invalid flags for revision 2 PnP event.\r\n
0xd000001e | Invalid PnP event. For NDK, only NetEventNDKEnable and NetEventNDKDisable are allowed.\r\n
0xd000001f | Invalid buffer for NetEventNDKEnable.\r\n
0xd0000020 | NdkInfo passed in NDK capabilities was NULL for NetEventNDKEnable.\r\n
0xd0000021 | Invalid buffer for NetEventNDKDisable.\r\n
0xd0000022 | NDIS call to send NDK PnP event up failed.\r\n
0xd0000023 | Unknown.\r\n
0xd0000024 | Insufficient system resources.\r\n
0xd0000025 | Cannot open VF adapter.\r\n
0xd0000026 | Cannot retrieve VF serial number.\r\n
0xd0000027 | VF MTU mismatch.\r\n
0xd0000028 | Invalid VF device state.\r\n
0xd0000029 | VF media disconnected.\r\n
0xd000002a | Cannot switch to VF data path.\r\n
0xd000002b | Cannot set VF packet filter.\r\n
0xd000002c | Cannot set VF TCP offload parameters.\r\n
0xd000002d | Unknown\r\n
0xd000002e | Status indication object allocation\r\n
0xd000002f | Status indication buffer allocation\r\n
0xd0000030 | Unknown NDK PnP event\r\n
0xd0000031 | NDK enable PnP event\r\n
0xd0000032 | NDK disable PnP event\r\n
