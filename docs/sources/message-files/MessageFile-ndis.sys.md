## ndis.sys

Path: %SystemRoot%\system32\drivers\ndis.sys

### 6.1.7600.16385, 6.1.7601.17514

Message identifier | Message string
--- | ---
0x10000034 | SQM\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %3, Adapter: %1, Result: %4\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Filter %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI or IP1394\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%3) Error %4\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Request %4, bComplete %5, Status %6\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x10000034 | SQM\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %4, Adapter: %1, Result: %5\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Filter %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI, IP1394, or Token Ring\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%4) Error %5\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Request %4, bComplete %5, Status %6\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb000283c | The network adapter is idle and can be suspended now.%nInterface Luid: %1\r\n
0xb000283d | The network adapter declined to enter a suspended state.%nInterface Luid: %1%nStatus code: %2\r\n
0xb000283e | The network adapter must be resumed.%nInterface Luid: %1%nResume reason: %2\r\n
0xb000283f | NIC Active state is acquired.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002840 | NIC Active state is released.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002841 | The network adapter indicated a wake signal.%nInterface Luid: %1%nWake reason: %2\r\n
0xb0002842 | Working power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002843 | Working power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002844 | Low power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002845 | Low power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002846 | Wait Wake IRP is completed for network adapter. %nInterface Luid: %3\r\n
0xb0002847 | Miniport %4, %1, had event %5\r\n
0xb0002848 | Filter %1 entering state %2 (FriendlyName: %7)\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xd0000062 | The system is preparing to remove the device\r\n
0xd0000063 | The device was removed\r\n
0xd0000064 | The device was unexpectedly removed\r\n
0xd0000065 | The system is preparing to stop the device\r\n
0xd0000066 | The device was stopped\r\n
0xd0000067 | The system is entering a low-power state\r\n
0xd0000068 | The NIC is entering a quiet state\r\n
0xd0000069 | The miniport is performing a PNP operation\r\n
0xd000006a | Power save operations are not started yet on the miniport\r\n
0xd000006b | The driver must process a network OID request\r\n
0xd000006c | The network stack must pause operation\r\n
0xd000006d | The network stack must resume operation\r\n
0xd000006e | The driver must be reset\r\n
0xd000006f | The driver must process a PnP event notification\r\n
0xd0000070 | The driver must check for errors\r\n
0xd0000071 | The driver must process a Direct OID request\r\n
0xd0000072 | The driver must cancel a Direct OID request\r\n
0xd0000073 | The driver must transmit network packets\r\n
0xd0000074 | The driver must cancel network packets\r\n
0xd0000075 | The driver must complete the processing of received network packets\r\n
0xd0000076 | Unspecified\r\n
0xd0000077 | Incoming Packet\r\n
0xd0000078 | Media Disconnect\r\n
0xd0000079 | Media Connect\r\n
0xd000007a | Network List Offload Discovery\r\n
0xd000007b | AP Association Lost\r\n
0xd000007c | GTK Handshake Error\r\n
0xd000007d | 4-Way Handshake Request\r\n
0xd000007e | WiFi Direct Invitation Request\r\n
0xd000007f | Register State\r\n
0xd0000080 | SMS Receive\r\n
0xd0000081 | USSD Receive\r\n
0xd0000082 | Vendor Specific\r\n
0xd0000083 | Unspecified Component\r\n
0xd0000084 | IPv6 Auto Config\r\n
0xd0000085 | DHCPv4\r\n
0xd0000086 | DHCPv6\r\n
0xd0000087 | Wireless LAN\r\n
0xd0000088 | Wireless WAN\r\n
0xd0000089 | WCM\r\n
0xd000008a | NCSI\r\n
0xd000008b | Test\r\n
0xd000008c | EAP SIM\r\n
0xd000008d | TCPIP OID\r\n
0xd000008e | TCPIP ACK\r\n
0xd000008f | Unknown\r\n
0xd0000090 | Dx_SystemSleep: NDIS is requesting a low device power state because the system is going to a low power state\r\n
0xd0000091 | Dx_NicQuiet: NDIS is requesting a low device power state due to Connected Standby\r\n
0xd0000092 | Dx_SSIdle: NDIS is requesting a low device power state because the NIC is idle\r\n
0xd0000093 | Dx_D3DTimeout: NDIS is requesting a low device power state because the NIC is disconnected\r\n
0xd0000094 | D0_SystemResume: NDIS is requesting a working device power state due to a system resume\r\n
0xd0000095 | D0_NicActive: NDIS is requesting device working power state due for maintaining connectivity during Connected Standby or due to Connected Standby exit\r\n
0xd0000096 | D0_AoAcWake: NDIS is requesting that the device return to the operational power state because the device has indicated a wake signal\r\n
0xd0000097 | D0_SSResume: NDIS is requesting that the device return to the operational power state because the NIC is no longer idle\r\n
0xd0000098 | D0_D3DCancel: NDIS is requesting that the device return to the operational power state because the D3-on-disconnect has been disabled\r\n
0xd0000099 | D0_D3DWake: NDIS is requesting that the device return to the operational power state because the NIC has indicated a wake\r\n
0xd000009a | D0_D3DResume: NDIS is requesting that the device return to the operational power state because NDIS needed to interact with the miniport driver\r\n
0xd000009b | D0_Complete: The device's bus is ready to return the device to an operational power state\r\n
0xd000009c | D0_SSComplete: The device's bus is ready to return the device to an operational power state\r\n
0xd000009d | Dx_Complete: The device's bus has acknowledged the low-power state\r\n
0xd000009e | Dx_SSComplete: The device's bus has acknowledged the low-power state\r\n
0xd000009f | DeviceAdded: NDIS has successfully processed the enumeration of the miniport's hardware node\r\n
0xd00000a0 | DeviceStart: The PNP subsystem has requested that NDIS start the device\r\n
0xd00000a1 | DeviceQueryRemove: The PNP subsystem has requested that NDIS prepare to remove this device\r\n
0xd00000a2 | DeviceCancelRemove: The PNP subsystem has canceled a remove request\r\n
0xd00000a3 | DeviceRemove: The PNP subsystem has requested that NDIS remove the device\r\n
0xd00000a4 | DeviceSurpriseRemoval: The PNP subsystem has indicated that the device was not enumerated by its bus anymore\r\n
0xd00000a5 | DeviceQueryStop: The PNP subsystem has requested that NDIS prepare to stop the device\r\n
0xd00000a6 | DeviceCancelStop: The PNP subsystem has canceled a pending stop request\r\n
0xd00000a7 | DeviceStop: The PNP subsystem has requested that NDIS stop the miniport device\r\n
0xd00000a8 | MiniportInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000a9 | MiniportHalted: NDIS has halted the miniport\r\n
0xd00000aa | MiniportPaused: NDIS has paused the miniport\r\n
0xd00000ab | MiniportRestarted: NDIS has successfully restarted (unpaused) the miniport\r\n
0xd00000ac | MiniportPmInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n

### 6.3.9600.16384, 6.3.9600.18577

Message identifier | Message string
--- | ---
0x0000284d | Miniport %4, %1, had event %5\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x7000000f | Refcount rundown\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0x90000004 | System\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %4, Adapter: %1, Result: %5\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Miniport %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI, IP1394, or Token Ring\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%4) Error %5\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Request %4, bComplete %5, Status %6\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb00027dc | Miniport %1 on processor %2 has an RST limit change from %5 to %6 NBLs per indication (NumNbls: %3, Duration: %4, Individual: %7, Cummulative: %8)\r\n
0xb000283c | The network adapter is idle and can be suspended now.%nInterface Luid: %1\r\n
0xb000283d | The network adapter declined to enter a suspended state.%nInterface Luid: %1%nStatus code: %2\r\n
0xb000283e | The network adapter must be resumed.%nInterface Luid: %1%nResume reason: %2\r\n
0xb000283f | NIC Active state is acquired.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002840 | NIC Active state is released.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002841 | The network adapter indicated a wake signal.%nInterface Luid: %1%nWake reason: %2\r\n
0xb0002842 | Working power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002843 | Working power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002844 | Low power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002845 | Low power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002846 | Wait/Wake IRP is completed for network adapter. %nInterface Luid: %3\r\n
0xb0002848 | Filter %1 entering state %2 (FriendlyName: %7)\r\n
0xb0002849 | Entering Connected Standby\r\n
0xb000284a | Exiting Connected Standby. Duration %1 sec.\r\n
0xb000284b | Miniport %2: CS active %3 seconds, %4 power transitions.\r\n
0xb000284c | Component %2: CS active %3 seconds, Miniport %1.\r\n
0xb0002850 | Refcount rundown for miniport %3 will follow\r\n
0xb0002851 | Refcount rundown for miniport %1: component %2 has refcount %3\r\n
0xb0002852 | Refcount rundown for miniport %1: stop flags %2%nRundown complete\r\n
0xb0002853 | Power transition for Miniport %2 in CS (%3 to %4). %3 traffic (In-Out): Unicast Packets (%5-%6), Multicast Packets (%7-%8), Broadcast Packets (%9-%10).\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xd0000062 | The system is preparing to remove the device\r\n
0xd0000063 | The device was removed\r\n
0xd0000064 | The device was unexpectedly removed\r\n
0xd0000065 | The system is preparing to stop the device\r\n
0xd0000066 | The device was stopped\r\n
0xd0000067 | The system is entering a low-power state\r\n
0xd0000068 | The NIC is entering a quiet state\r\n
0xd0000069 | The miniport is performing a PNP operation\r\n
0xd000006a | Power save operations are not started yet on the miniport\r\n
0xd000006b | The miniport has encountered a fatal error\r\n
0xd000006c | The driver must process a network OID request\r\n
0xd000006d | The network stack must pause operation\r\n
0xd000006e | The network stack must resume operation\r\n
0xd000006f | The driver must be reset\r\n
0xd0000070 | The driver must process a PnP event notification\r\n
0xd0000071 | The driver must check for errors\r\n
0xd0000072 | The driver must process a Direct OID request\r\n
0xd0000073 | The driver must cancel a Direct OID request\r\n
0xd0000074 | The driver must transmit network packets\r\n
0xd0000075 | The driver must cancel network packets\r\n
0xd0000076 | The driver must complete the processing of received network packets\r\n
0xd0000077 | Unspecified\r\n
0xd0000078 | Incoming Packet\r\n
0xd0000079 | Media Disconnect\r\n
0xd000007a | Media Connect\r\n
0xd000007b | Network List Offload Discovery\r\n
0xd000007c | AP Association Lost\r\n
0xd000007d | GTK Handshake Error\r\n
0xd000007e | 4-Way Handshake Request\r\n
0xd000007f | WiFi Direct Invitation Request\r\n
0xd0000080 | Register State\r\n
0xd0000081 | SMS Receive\r\n
0xd0000082 | USSD Receive\r\n
0xd0000083 | Vendor Specific\r\n
0xd0000084 | Unspecified Component\r\n
0xd0000085 | TCPIP RS\r\n
0xd0000086 | DHCPv4\r\n
0xd0000087 | DHCPv6\r\n
0xd0000088 | Wireless LAN\r\n
0xd0000089 | Wireless WAN\r\n
0xd000008a | WCM\r\n
0xd000008b | NCSI\r\n
0xd000008c | Test\r\n
0xd000008d | EAP SIM\r\n
0xd000008e | TCPIP OID\r\n
0xd000008f | TCPIP Data\r\n
0xd0000090 | TCPIP DAD\r\n
0xd0000091 | Geolocation\r\n
0xd0000092 | Unknown\r\n
0xd0000093 | Dx_SystemSleep: NDIS is requesting a low device power state because the system is going to a low power state\r\n
0xd0000094 | Dx_NicQuiet: NDIS is requesting a low device power state due to Connected Standby\r\n
0xd0000095 | Dx_SSIdle: NDIS is requesting a low device power state because the NIC is idle\r\n
0xd0000096 | Dx_D3DTimeout: NDIS is requesting a low device power state because the NIC is disconnected\r\n
0xd0000097 | D0_SystemResume: NDIS is requesting a working device power state due to a system resume\r\n
0xd0000098 | D0_NicActive: NDIS is requesting device working power state due for maintaining connectivity during Connected Standby or due to Connected Standby exit\r\n
0xd0000099 | D0_AoAcWake: NDIS is requesting that the device return to the operational power state because the device has indicated a wake signal\r\n
0xd000009a | D0_SSResume: NDIS is requesting that the device return to the operational power state because the NIC is no longer idle\r\n
0xd000009b | D0_D3DCancel: NDIS is requesting that the device return to the operational power state because the D3-on-disconnect has been disabled\r\n
0xd000009c | D0_D3DWake: NDIS is requesting that the device return to the operational power state because the NIC has indicated a wake\r\n
0xd000009d | D0_D3DResume: NDIS is requesting that the device return to the operational power state because NDIS needed to interact with the miniport driver\r\n
0xd000009e | D0_Complete: The device's bus is ready to return the device to an operational power state\r\n
0xd000009f | D0_SSComplete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a0 | Dx_Complete: The device's bus has acknowledged the low-power state\r\n
0xd00000a1 | Dx_SSComplete: The device's bus has acknowledged the low-power state\r\n
0xd00000a2 | D0_AoAcSurpriseWake: NDIS is requesting that the device return to the operational power state because the miniport driver indicated a surprise wake\r\n
0xd00000a3 | DeviceAdded: NDIS has successfully processed the enumeration of the miniport's hardware node\r\n
0xd00000a4 | DeviceStart: The PNP subsystem has requested that NDIS start the device\r\n
0xd00000a5 | DeviceQueryRemove: The PNP subsystem has requested that NDIS prepare to remove this device\r\n
0xd00000a6 | DeviceCancelRemove: The PNP subsystem has canceled a remove request\r\n
0xd00000a7 | DeviceRemove: The PNP subsystem has requested that NDIS remove the device\r\n
0xd00000a8 | DeviceSurpriseRemoval: The PNP subsystem has indicated that the device was not enumerated by its bus anymore\r\n
0xd00000a9 | DeviceQueryStop: The PNP subsystem has requested that NDIS prepare to stop the device\r\n
0xd00000aa | DeviceCancelStop: The PNP subsystem has canceled a pending stop request\r\n
0xd00000ab | DeviceStop: The PNP subsystem has requested that NDIS stop the miniport device\r\n
0xd00000ac | MiniportInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000ad | MiniportHalted: NDIS has halted the miniport\r\n
0xd00000ae | MiniportPaused: NDIS has paused the miniport\r\n
0xd00000af | MiniportRestarted: NDIS has successfully restarted (unpaused) the miniport\r\n
0xd00000b0 | MiniportPmInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b1 | Fatal error: The miniport has entered an error state due to a user request\r\n
0xd00000b2 | Fatal error: The miniport has detected an internal error\r\n
0xd00000b3 | Fatal error: The IM miniport has failed to initialize\r\n
0xd00000b4 | Fatal error: The miniport has failed to start by returning an error code from MiniportRestart\r\n
0xd00000b5 | Fatal error: The miniport has failed a power transition to operational power\r\n
0xd00000b6 | Fatal error: The miniport has failed a power transition to low power\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x0000284d | Miniport %4, %1, had event %5\r\n
0x000028a0 | The network interface "%4" has begun resetting.  There will be a momentary disruption in network connectivity while the hardware resets.%nReason: %5.%nThis network interface has reset %6 time(s) since it was last initialized.\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x7000000f | Refcount rundown\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0x90000004 | System\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %4, Adapter: %1, Result: %5\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Miniport %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI, IP1394, or Token Ring\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%4) Error %5\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Oid %7, Completed by NDIS on behalf of miniport with Status %6: %5\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb00027dc | Miniport %1 on processor %2 has an RST limit change from %5 to %6 NBLs per indication (NumNbls: %3, Duration: %4, Individual: %7, Cummulative: %8)\r\n
0xb000283c | The network adapter is idle and can be suspended now.%nInterface Luid: %1\r\n
0xb000283d | The network adapter declined to enter a suspended state.%nInterface Luid: %1%nStatus code: %2\r\n
0xb000283e | The network adapter must be resumed.%nInterface Luid: %1%nResume reason: %2\r\n
0xb000283f | NIC Active state is acquired.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002840 | NIC Active state is released.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002841 | The network adapter indicated a wake signal.%nInterface Luid: %1%nWake reason: %2\r\n
0xb0002842 | Working power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002843 | Working power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002844 | Low power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002845 | Low power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002846 | Wait/Wake IRP is completed for network adapter. %nInterface Luid: %3\r\n
0xb0002848 | Filter %1 entering state %2 (FriendlyName: %7)\r\n
0xb0002849 | Entering Connected Standby\r\n
0xb000284a | Exiting Connected Standby. Duration %1 sec.\r\n
0xb000284b | Miniport %2: CS active %3 seconds, %4 power transitions.\r\n
0xb000284c | Component %2: CS active %3 seconds, Miniport %1.\r\n
0xb0002850 | Refcount rundown for miniport %3 will follow\r\n
0xb0002851 | Refcount rundown for miniport %1: component %2 has refcount %3\r\n
0xb0002852 | Refcount rundown for miniport %1: stop flags %2%nRundown complete\r\n
0xb0002853 | Power transition for Miniport %2 in CS (%3 to %4). %3 traffic (In-Out): Unicast Packets (%5-%6), Multicast Packets (%7-%8), Broadcast Packets (%9-%10).\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xd0000062 | The system is preparing to remove the device\r\n
0xd0000063 | The device was removed\r\n
0xd0000064 | The device was unexpectedly removed\r\n
0xd0000065 | The system is preparing to stop the device\r\n
0xd0000066 | The device was stopped\r\n
0xd0000067 | The system is entering a low-power state\r\n
0xd0000068 | The NIC is entering a quiet state\r\n
0xd0000069 | The miniport is performing a PNP operation\r\n
0xd000006a | Power save operations are not started yet on the miniport\r\n
0xd000006b | The miniport has encountered a fatal error\r\n
0xd000006c | The driver must process a network OID request\r\n
0xd000006d | The network stack must pause operation\r\n
0xd000006e | The network stack must resume operation\r\n
0xd000006f | The driver must be reset\r\n
0xd0000070 | The driver must process a PnP event notification\r\n
0xd0000071 | The driver must check for errors\r\n
0xd0000072 | The driver must process a Direct OID request\r\n
0xd0000073 | The driver must cancel a Direct OID request\r\n
0xd0000074 | The driver must transmit network packets\r\n
0xd0000075 | The driver must cancel network packets\r\n
0xd0000076 | The driver must complete the processing of received network packets\r\n
0xd0000077 | Unspecified\r\n
0xd0000078 | Incoming Packet\r\n
0xd0000079 | Media Disconnect\r\n
0xd000007a | Media Connect\r\n
0xd000007b | Network List Offload Discovery\r\n
0xd000007c | AP Association Lost\r\n
0xd000007d | GTK Handshake Error\r\n
0xd000007e | 4-Way Handshake Request\r\n
0xd000007f | WiFi Direct Invitation Request\r\n
0xd0000080 | Register State\r\n
0xd0000081 | SMS Receive\r\n
0xd0000082 | USSD Receive\r\n
0xd0000083 | Vendor Specific\r\n
0xd0000084 | Unspecified Component\r\n
0xd0000085 | TCPIP RS\r\n
0xd0000086 | DHCPv4\r\n
0xd0000087 | DHCPv6\r\n
0xd0000088 | Wireless LAN\r\n
0xd0000089 | Wireless WAN\r\n
0xd000008a | WCM\r\n
0xd000008b | NCSI\r\n
0xd000008c | Test\r\n
0xd000008d | EAP SIM\r\n
0xd000008e | TCPIP OID\r\n
0xd000008f | TCPIP Data\r\n
0xd0000090 | TCPIP DAD\r\n
0xd0000091 | Geolocation\r\n
0xd0000092 | WLAN Network Manager\r\n
0xd0000093 | Unknown\r\n
0xd0000094 | Dx_SystemSleep: NDIS is requesting a low device power state because the system is going to a low power state\r\n
0xd0000095 | Dx_NicQuiet: NDIS is requesting a low device power state due to Connected Standby\r\n
0xd0000096 | Dx_SSIdle: NDIS is requesting a low device power state because the NIC is idle\r\n
0xd0000097 | Dx_D3DTimeout: NDIS is requesting a low device power state because the NIC is disconnected\r\n
0xd0000098 | D0_SystemResume: NDIS is requesting a working device power state due to a system resume\r\n
0xd0000099 | D0_NicActive: NDIS is requesting device working power state due for maintaining connectivity during Connected Standby or due to Connected Standby exit\r\n
0xd000009a | D0_AoAcWake: NDIS is requesting that the device return to the operational power state because the device has indicated a wake signal\r\n
0xd000009b | D0_SSResume: NDIS is requesting that the device return to the operational power state because the NIC is no longer idle\r\n
0xd000009c | D0_D3DCancel: NDIS is requesting that the device return to the operational power state because the D3-on-disconnect has been disabled\r\n
0xd000009d | D0_D3DWake: NDIS is requesting that the device return to the operational power state because the NIC has indicated a wake\r\n
0xd000009e | D0_D3DResume: NDIS is requesting that the device return to the operational power state because NDIS needed to interact with the miniport driver\r\n
0xd000009f | D0_Complete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a0 | D0_SSComplete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a1 | Dx_Complete: The device's bus has acknowledged the low-power state\r\n
0xd00000a2 | Dx_SSComplete: The device's bus has acknowledged the low-power state\r\n
0xd00000a3 | D0_AoAcSurpriseWake: NDIS is requesting that the device return to the operational power state because the miniport driver indicated a surprise wake\r\n
0xd00000a4 | DeviceAdded: NDIS has successfully processed the enumeration of the miniport's hardware node\r\n
0xd00000a5 | DeviceStart: The PNP subsystem has requested that NDIS start the device\r\n
0xd00000a6 | DeviceQueryRemove: The PNP subsystem has requested that NDIS prepare to remove this device\r\n
0xd00000a7 | DeviceCancelRemove: The PNP subsystem has canceled a remove request\r\n
0xd00000a8 | DeviceRemove: The PNP subsystem has requested that NDIS remove the device\r\n
0xd00000a9 | DeviceSurpriseRemoval: The PNP subsystem has indicated that the device was not enumerated by its bus anymore\r\n
0xd00000aa | DeviceQueryStop: The PNP subsystem has requested that NDIS prepare to stop the device\r\n
0xd00000ab | DeviceCancelStop: The PNP subsystem has canceled a pending stop request\r\n
0xd00000ac | DeviceStop: The PNP subsystem has requested that NDIS stop the miniport device\r\n
0xd00000ad | MiniportInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000ae | MiniportHalted: NDIS has halted the miniport\r\n
0xd00000af | MiniportPaused: NDIS has paused the miniport\r\n
0xd00000b0 | MiniportRestarted: NDIS has successfully restarted (unpaused) the miniport\r\n
0xd00000b1 | MiniportPmInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b2 | Fatal error: The miniport has entered an error state due to a user request\r\n
0xd00000b3 | Fatal error: The miniport has detected an internal error\r\n
0xd00000b4 | Fatal error: The IM miniport has failed to initialize\r\n
0xd00000b5 | Fatal error: The miniport has failed to start by returning an error code from MiniportRestart\r\n
0xd00000b6 | Fatal error: The miniport has failed a power transition to operational power\r\n
0xd00000b7 | Fatal error: The miniport has failed a power transition to low power\r\n
0xd00000b8 | The network driver did not respond to an OID request in a timely fashion\r\n
0xd00000b9 | The network driver detected that its hardware has stopped responding to commands\r\n
0xd00000ba | The network driver requested that it be reset\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n

### 10.0.14393.0, 10.0.14393.321

Message identifier | Message string
--- | ---
0x0000284d | Miniport %4, %1, had event %5\r\n
0x000028a0 | The network interface "%4" has begun resetting.  There will be a momentary disruption in network connectivity while the hardware resets.%nReason: %5.%nThis network interface has reset %6 time(s) since it was last initialized.\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x7000000f | Refcount rundown\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0x90000004 | System\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %4, Adapter: %1, Result: %5\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Miniport %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI, IP1394, or Token Ring\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%4) Error %5\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Oid %7, Completed by NDIS on behalf of miniport with Status %6: %5\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb00027dc | Miniport %1 on processor %2 has an RST limit change from %5 to %6 NBLs per indication (NumNbls: %3, Duration: %4, Individual: %7, Cummulative: %8)\r\n
0xb000283c | The network adapter is idle and can be suspended now.%nInterface Luid: %1\r\n
0xb000283d | The network adapter declined to enter a suspended state.%nInterface Luid: %1%nStatus code: %2\r\n
0xb000283e | The network adapter must be resumed.%nInterface Luid: %1%nResume reason: %2\r\n
0xb000283f | NIC Active state is acquired.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002840 | NIC Active state is released.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002841 | The network adapter indicated a wake signal.%nInterface Luid: %1%nWake reason: %2\r\n
0xb0002842 | Working power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002843 | Working power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002844 | Low power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002845 | Low power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002846 | Wait/Wake IRP is completed for network adapter. %nInterface Luid: %3\r\n
0xb0002848 | Filter %1 entering state %2 (FriendlyName: %7)\r\n
0xb0002849 | Entering Connected Standby\r\n
0xb000284a | Exiting Connected Standby. Duration %1 sec.\r\n
0xb000284b | Miniport %2: CS active %3 seconds, %4 power transitions.\r\n
0xb000284c | Component %2: CS active %3 seconds, Miniport %1.\r\n
0xb0002850 | Refcount rundown for miniport %3 will follow\r\n
0xb0002851 | Refcount rundown for miniport %1: component %2 has refcount %3\r\n
0xb0002852 | Refcount rundown for miniport %1: stop flags %2%nRundown complete\r\n
0xb0002853 | Power transition for Miniport %2 in CS (%3 to %4). %3 traffic (In-Out): Unicast Packets (%5-%6), Multicast Packets (%7-%8), Broadcast Packets (%9-%10).\r\n
0xb0002854 | Miniport PDO information for Sleepstudy\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xd0000062 | The system is preparing to remove the device\r\n
0xd0000063 | The device was removed\r\n
0xd0000064 | The device was unexpectedly removed\r\n
0xd0000065 | The system is preparing to stop the device\r\n
0xd0000066 | The device was stopped\r\n
0xd0000067 | The system is entering a low-power state\r\n
0xd0000068 | The NIC is entering a quiet state\r\n
0xd0000069 | The miniport is performing a PNP operation\r\n
0xd000006a | Power save operations are not started yet on the miniport\r\n
0xd000006b | The miniport has encountered a fatal error\r\n
0xd000006c | Apply interface change after WLAN MAC randomization or L2 MTU update\r\n
0xd000006d | The driver must process a Magic Packet to allow Win32 Management Apps to resume execution\r\n
0xd000006e | The driver must process a network OID request\r\n
0xd000006f | The network stack must pause operation\r\n
0xd0000070 | The network stack must resume operation\r\n
0xd0000071 | The driver must be reset\r\n
0xd0000072 | The driver must process a PnP event notification\r\n
0xd0000073 | The driver must check for errors\r\n
0xd0000074 | The driver must process a Direct OID request\r\n
0xd0000075 | The driver must cancel a Direct OID request\r\n
0xd0000076 | The driver must transmit network packets\r\n
0xd0000077 | The driver must cancel network packets\r\n
0xd0000078 | The driver must complete the processing of received network packets\r\n
0xd0000079 | Unspecified\r\n
0xd000007a | Incoming Packet\r\n
0xd000007b | Media Disconnect\r\n
0xd000007c | Media Connect\r\n
0xd000007d | Network List Offload Discovery\r\n
0xd000007e | AP Association Lost\r\n
0xd000007f | GTK Handshake Error\r\n
0xd0000080 | 4-Way Handshake Request\r\n
0xd0000081 | WiFi Direct Invitation Request\r\n
0xd0000082 | Register State\r\n
0xd0000083 | SMS Receive\r\n
0xd0000084 | USSD Receive\r\n
0xd0000085 | Vendor Specific\r\n
0xd0000086 | Unspecified Component\r\n
0xd0000087 | TCPIP RS\r\n
0xd0000088 | DHCPv4\r\n
0xd0000089 | DHCPv6\r\n
0xd000008a | Wireless LAN\r\n
0xd000008b | Wireless WAN\r\n
0xd000008c | WCM\r\n
0xd000008d | NCSI\r\n
0xd000008e | Test\r\n
0xd000008f | EAP SIM\r\n
0xd0000090 | TCPIP OID\r\n
0xd0000091 | TCPIP Data\r\n
0xd0000092 | TCPIP DAD\r\n
0xd0000093 | Geolocation\r\n
0xd0000094 | WLAN Network Manager\r\n
0xd0000095 | Unknown\r\n
0xd0000096 | Dx_SystemSleep: NDIS is requesting a low device power state because the system is going to a low power state\r\n
0xd0000097 | Dx_NicQuiet: NDIS is requesting a low device power state due to Connected Standby\r\n
0xd0000098 | Dx_SSIdle: NDIS is requesting a low device power state because the NIC is idle\r\n
0xd0000099 | Dx_D3DTimeout: NDIS is requesting a low device power state because the NIC is disconnected\r\n
0xd000009a | D0_SystemResume: NDIS is requesting a working device power state due to a system resume\r\n
0xd000009b | D0_NicActive: NDIS is requesting device working power state due for maintaining connectivity during Connected Standby or due to Connected Standby exit\r\n
0xd000009c | D0_AoAcWake: NDIS is requesting that the device return to the operational power state because the device has indicated a wake signal\r\n
0xd000009d | D0_SSResume: NDIS is requesting that the device return to the operational power state because the NIC is no longer idle\r\n
0xd000009e | D0_D3DCancel: NDIS is requesting that the device return to the operational power state because the D3-on-disconnect has been disabled\r\n
0xd000009f | D0_D3DWake: NDIS is requesting that the device return to the operational power state because the NIC has indicated a wake\r\n
0xd00000a0 | D0_D3DResume: NDIS is requesting that the device return to the operational power state because NDIS needed to interact with the miniport driver\r\n
0xd00000a1 | D0_Complete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a2 | D0_SSComplete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a3 | Dx_Complete: The device's bus has acknowledged the low-power state\r\n
0xd00000a4 | Dx_SSComplete: The device's bus has acknowledged the low-power state\r\n
0xd00000a5 | D0_AoAcSurpriseWake: NDIS is requesting that the device return to the operational power state because the miniport driver indicated a surprise wake\r\n
0xd00000a6 | DeviceAdded: NDIS has successfully processed the enumeration of the miniport's hardware node\r\n
0xd00000a7 | DeviceStart: The PNP subsystem has requested that NDIS start the device\r\n
0xd00000a8 | DeviceQueryRemove: The PNP subsystem has requested that NDIS prepare to remove this device\r\n
0xd00000a9 | DeviceCancelRemove: The PNP subsystem has canceled a remove request\r\n
0xd00000aa | DeviceRemove: The PNP subsystem has requested that NDIS remove the device\r\n
0xd00000ab | DeviceSurpriseRemoval: The PNP subsystem has indicated that the device was not enumerated by its bus anymore\r\n
0xd00000ac | DeviceQueryStop: The PNP subsystem has requested that NDIS prepare to stop the device\r\n
0xd00000ad | DeviceCancelStop: The PNP subsystem has canceled a pending stop request\r\n
0xd00000ae | DeviceStop: The PNP subsystem has requested that NDIS stop the miniport device\r\n
0xd00000af | MiniportInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b0 | MiniportHalted: NDIS has halted the miniport\r\n
0xd00000b1 | MiniportPaused: NDIS has paused the miniport\r\n
0xd00000b2 | MiniportRestarted: NDIS has successfully restarted (unpaused) the miniport\r\n
0xd00000b3 | MiniportPmInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b4 | Fatal error: The miniport has entered an error state due to a user request\r\n
0xd00000b5 | Fatal error: The miniport has detected an internal error\r\n
0xd00000b6 | Fatal error: The IM miniport has failed to initialize\r\n
0xd00000b7 | Fatal error: The miniport has failed to start by returning an error code from MiniportRestart\r\n
0xd00000b8 | Fatal error: The miniport has failed a power transition to operational power\r\n
0xd00000b9 | Fatal error: The miniport has failed a power transition to low power\r\n
0xd00000ba | Network Interface deleted while PNP Device still exists. Note that this event is provided for informational purpose and might not be an error always (Eg: In case of vSwitch which was recently un-installed or a LBFO team was removed)\r\n
0xd00000bb | The network driver did not respond to an OID request in a timely fashion\r\n
0xd00000bc | The network driver detected that its hardware has stopped responding to commands\r\n
0xd00000bd | The network driver requested that it be reset\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x0000284d | Miniport %4, %1, had event %5\r\n
0x000028a0 | The network interface "%4" has begun resetting.  There will be a momentary disruption in network connectivity while the hardware resets.%nReason: %5.%nThis network interface has reset %6 time(s) since it was last initialized.\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x7000000f | Refcount rundown\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0x90000004 | System\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %4, Adapter: %1, Result: %5\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Miniport %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI, IP1394, or Token Ring\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%4) Error %5\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Oid %7, Completed by NDIS on behalf of miniport with Status %6: %5\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb00027dc | Miniport %1 on processor %2 has an RST limit change from %5 to %6 NBLs per indication (NumNbls: %3, Duration: %4, Individual: %7, Cummulative: %8)\r\n
0xb000283c | The network adapter is idle and can be suspended now.%nInterface Luid: %1\r\n
0xb000283d | The network adapter declined to enter a suspended state.%nInterface Luid: %1%nStatus code: %2\r\n
0xb000283e | The network adapter must be resumed.%nInterface Luid: %1%nResume reason: %2\r\n
0xb000283f | NIC Active state is acquired.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002840 | NIC Active state is released.%nInterface Luid: %1%nComponent ID: %2%nComponent Ref Count: %3%nInterface Ref Count: %4\r\n
0xb0002841 | The network adapter indicated a wake signal.%nInterface Luid: %1%nWake reason: %2\r\n
0xb0002842 | Working power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002843 | Working power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002844 | Low power state is requested for network adapter. %nInterface Luid: %3\r\n
0xb0002845 | Low power request is completed for network adapter. %nInterface Luid: %3 %nStatus: %4\r\n
0xb0002846 | Wait/Wake IRP is completed for network adapter. %nInterface Luid: %3\r\n
0xb0002848 | Filter %1 entering state %2 (FriendlyName: %7)\r\n
0xb0002849 | Entering Connected Standby\r\n
0xb000284a | Exiting Connected Standby. Duration %1 sec.\r\n
0xb000284b | Miniport %2: CS active %3 seconds, %4 power transitions.\r\n
0xb000284c | Component %2: CS active %3 seconds, Miniport %1.\r\n
0xb0002850 | Refcount rundown for miniport %3 will follow\r\n
0xb0002851 | Refcount rundown for miniport %1: component %2 has refcount %3\r\n
0xb0002852 | Refcount rundown for miniport %1: stop flags %2%nRundown complete\r\n
0xb0002853 | Power transition for Miniport %2 in CS (%3 to %4). %3 traffic (In-Out): Unicast Packets (%5-%6), Multicast Packets (%7-%8), Broadcast Packets (%9-%10).\r\n
0xb0002854 | Miniport PDO information for Sleepstudy\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xd0000062 | The system is preparing to remove the device\r\n
0xd0000063 | The device was removed\r\n
0xd0000064 | The device was unexpectedly removed\r\n
0xd0000065 | The system is preparing to stop the device\r\n
0xd0000066 | The device was stopped\r\n
0xd0000067 | The system is entering a low-power state\r\n
0xd0000068 | The NIC is entering a quiet state\r\n
0xd0000069 | The miniport is performing a PNP operation\r\n
0xd000006a | Power save operations are not started yet on the miniport\r\n
0xd000006b | The miniport has encountered a fatal error\r\n
0xd000006c | Apply interface change after WLAN MAC randomization or L2 MTU update\r\n
0xd000006d | The driver must process a Magic Packet to allow Win32 Management Apps to resume execution\r\n
0xd000006e | The Miniport is performing Bind Changes.\r\n
0xd000006f | The driver must process a network OID request\r\n
0xd0000070 | The network stack must pause operation\r\n
0xd0000071 | The network stack must resume operation\r\n
0xd0000072 | The driver must be reset\r\n
0xd0000073 | The driver must process a PnP event notification\r\n
0xd0000074 | The driver must check for errors\r\n
0xd0000075 | The driver must process a Direct OID request\r\n
0xd0000076 | The driver must cancel a Direct OID request\r\n
0xd0000077 | The driver must transmit network packets\r\n
0xd0000078 | The driver must cancel network packets\r\n
0xd0000079 | The driver must complete the processing of received network packets\r\n
0xd000007a | Unspecified\r\n
0xd000007b | Incoming Packet\r\n
0xd000007c | Media Disconnect\r\n
0xd000007d | Media Connect\r\n
0xd000007e | Network List Offload Discovery\r\n
0xd000007f | AP Association Lost\r\n
0xd0000080 | GTK Handshake Error\r\n
0xd0000081 | 4-Way Handshake Request\r\n
0xd0000082 | Register State\r\n
0xd0000083 | SMS Receive\r\n
0xd0000084 | USSD Receive\r\n
0xd0000085 | Vendor Specific\r\n
0xd0000086 | Unspecified Component\r\n
0xd0000087 | TCPIP RS\r\n
0xd0000088 | DHCPv4\r\n
0xd0000089 | DHCPv6\r\n
0xd000008a | Wireless LAN\r\n
0xd000008b | Wireless WAN\r\n
0xd000008c | WCM\r\n
0xd000008d | NCSI\r\n
0xd000008e | Test\r\n
0xd000008f | EAP SIM\r\n
0xd0000090 | TCPIP OID\r\n
0xd0000091 | TCPIP Data\r\n
0xd0000092 | TCPIP DAD\r\n
0xd0000093 | Geolocation\r\n
0xd0000094 | WLAN Network Manager\r\n
0xd0000095 | WCM-PDC Network Activation\r\n
0xd0000096 | Unknown\r\n
0xd0000097 | Dx_SystemSleep: NDIS is requesting a low device power state because the system is going to a low power state\r\n
0xd0000098 | Dx_NicQuiet: NDIS is requesting a low device power state due to Connected Standby\r\n
0xd0000099 | Dx_SSIdle: NDIS is requesting a low device power state because the NIC is idle\r\n
0xd000009a | Dx_D3DTimeout: NDIS is requesting a low device power state because the NIC is disconnected\r\n
0xd000009b | D0_SystemResume: NDIS is requesting a working device power state due to a system resume\r\n
0xd000009c | D0_NicActive: NDIS is requesting device working power state due for maintaining connectivity during Connected Standby or due to Connected Standby exit\r\n
0xd000009d | D0_AoAcWake: NDIS is requesting that the device return to the operational power state because the device has indicated a wake signal\r\n
0xd000009e | D0_SSResume: NDIS is requesting that the device return to the operational power state because the NIC is no longer idle\r\n
0xd000009f | D0_D3DCancel: NDIS is requesting that the device return to the operational power state because the D3-on-disconnect has been disabled\r\n
0xd00000a0 | D0_D3DWake: NDIS is requesting that the device return to the operational power state because the NIC has indicated a wake\r\n
0xd00000a1 | D0_D3DResume: NDIS is requesting that the device return to the operational power state because NDIS needed to interact with the miniport driver\r\n
0xd00000a2 | D0_Complete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a3 | D0_SSComplete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a4 | Dx_Complete: The device's bus has acknowledged the low-power state\r\n
0xd00000a5 | Dx_SSComplete: The device's bus has acknowledged the low-power state\r\n
0xd00000a6 | D0_AoAcSurpriseWake: NDIS is requesting that the device return to the operational power state because the miniport driver indicated a surprise wake\r\n
0xd00000a7 | DeviceAdded: NDIS has successfully processed the enumeration of the miniport's hardware node\r\n
0xd00000a8 | DeviceStart: The PNP subsystem has requested that NDIS start the device\r\n
0xd00000a9 | DeviceQueryRemove: The PNP subsystem has requested that NDIS prepare to remove this device\r\n
0xd00000aa | DeviceCancelRemove: The PNP subsystem has canceled a remove request\r\n
0xd00000ab | DeviceRemove: The PNP subsystem has requested that NDIS remove the device\r\n
0xd00000ac | DeviceSurpriseRemoval: The PNP subsystem has indicated that the device was not enumerated by its bus anymore\r\n
0xd00000ad | DeviceQueryStop: The PNP subsystem has requested that NDIS prepare to stop the device\r\n
0xd00000ae | DeviceCancelStop: The PNP subsystem has canceled a pending stop request\r\n
0xd00000af | DeviceStop: The PNP subsystem has requested that NDIS stop the miniport device\r\n
0xd00000b0 | MiniportInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b1 | MiniportHalted: NDIS has halted the miniport\r\n
0xd00000b2 | MiniportPaused: NDIS has paused the miniport\r\n
0xd00000b3 | MiniportRestarted: NDIS has successfully restarted (unpaused) the miniport\r\n
0xd00000b4 | MiniportPmInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b5 | Fatal error: The miniport has entered an error state due to a user request\r\n
0xd00000b6 | Fatal error: The miniport has detected an internal error\r\n
0xd00000b7 | Fatal error: The IM miniport has failed to initialize\r\n
0xd00000b8 | Fatal error: The miniport has failed to start by returning an error code from MiniportRestart\r\n
0xd00000b9 | Fatal error: The miniport has failed a power transition to operational power\r\n
0xd00000ba | Fatal error: The miniport has failed a power transition to low power\r\n
0xd00000bb | Network Interface deleted while PNP Device still exists. Note that this event is provided for informational purpose and might not be an error always (Eg: In case of vSwitch which was recently un-installed or a LBFO team was removed)\r\n
0xd00000bc | The network driver did not respond to an OID request in a timely fashion\r\n
0xd00000bd | The network driver detected that its hardware has stopped responding to commands\r\n
0xd00000be | The network driver requested that it be reset\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n

### 10.0.16299.15, 10.0.17134.619

Message identifier | Message string
--- | ---
0x0000284d | Miniport %4, %1, had event %5\r\n
0x000028a0 | The network interface "%4" has begun resetting.  There will be a momentary disruption in network connectivity while the hardware resets. Reason: %5. This network interface has reset %6 time(s) since it was last initialized.\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x7000000f | Refcount rundown\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0x90000004 | System\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %4, Adapter: %1, Result: %5\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Miniport %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI, IP1394, or Token Ring\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%4) Error %5\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Oid %7, Completed by NDIS on behalf of miniport with Status %6: %5\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb00027dc | Miniport %1 on processor %2 has an RST limit change from %5 to %6 NBLs per indication (NumNbls: %3, Duration: %4, Individual: %7, Cummulative: %8)\r\n
0xb000283c | The network adapter is idle and can be suspended now. Interface Luid: %1\r\n
0xb000283d | The network adapter declined to enter a suspended state. Interface Luid: %1 Status code: %2\r\n
0xb000283e | The network adapter must be resumed. Interface Luid: %1 Resume reason: %2\r\n
0xb000283f | NIC Active state is acquired.Interface Luid: %1 Component ID: %2 Component Ref Count: %3 Interface Ref Count: %4\r\n
0xb0002840 | NIC Active state is released. Interface Luid: %1 Component ID: %2 Component Ref Count: %3 Interface Ref Count: %4\r\n
0xb0002841 | The network adapter indicated a wake signal. Interface Luid: %1 Wake reason: %2\r\n
0xb0002842 | Working power state is requested for network adapter. Interface Luid: %3\r\n
0xb0002843 | Working power request is completed for network adapter. Interface Luid: %3 Status: %4\r\n
0xb0002844 | Low power state is requested for network adapter. Interface Luid: %3\r\n
0xb0002845 | Low power request is completed for network adapter. Interface Luid: %3 Status: %4\r\n
0xb0002846 | Wait/Wake IRP is completed for network adapter. Interface Luid: %3\r\n
0xb0002848 | Filter %1 entering state %2 (FriendlyName: %7)\r\n
0xb0002849 | Entering Connected Standby\r\n
0xb000284a | Exiting Connected Standby. Duration %1 sec.\r\n
0xb000284b | Miniport %2: CS active %3 seconds, %4 power transitions.\r\n
0xb000284c | Component %2: CS active %3 seconds, Miniport %1.\r\n
0xb0002850 | Refcount rundown for miniport %3 will follow\r\n
0xb0002851 | Refcount rundown for miniport %1: component %2 has refcount %3\r\n
0xb0002852 | Refcount rundown for miniport %1: stop flags %2 Rundown complete\r\n
0xb0002853 | Power transition for Miniport %2 in CS (%3 to %4). %3 traffic (In-Out): Unicast Packets (%5-%6), Multicast Packets (%7-%8), Broadcast Packets (%9-%10).\r\n
0xb0002854 | Miniport PDO information for Sleepstudy\r\n
0xb0002855 | Miniport %1 indicated a Wake Packet %3\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xd0000062 | The system is preparing to remove the device\r\n
0xd0000063 | The device was removed\r\n
0xd0000064 | The device was unexpectedly removed\r\n
0xd0000065 | The system is preparing to stop the device\r\n
0xd0000066 | The device was stopped\r\n
0xd0000067 | The system is entering a low-power state\r\n
0xd0000068 | The NIC is entering a quiet state\r\n
0xd0000069 | The miniport is performing a PNP operation\r\n
0xd000006a | Power save operations are not started yet on the miniport\r\n
0xd000006b | The miniport has encountered a fatal error\r\n
0xd000006c | Apply interface change after WLAN MAC randomization or L2 MTU update\r\n
0xd000006d | The driver must process a Magic Packet to allow Win32 Management Apps to resume execution\r\n
0xd000006e | The Miniport is performing Bind Changes.\r\n
0xd000006f | The driver must process a network OID request\r\n
0xd0000070 | The network stack must pause operation\r\n
0xd0000071 | The network stack must resume operation\r\n
0xd0000072 | The driver must be reset\r\n
0xd0000073 | The driver must process a PnP event notification\r\n
0xd0000074 | The driver must check for errors\r\n
0xd0000075 | The driver must process a Direct OID request\r\n
0xd0000076 | The driver must cancel a Direct OID request\r\n
0xd0000077 | The driver must transmit network packets\r\n
0xd0000078 | The driver must cancel network packets\r\n
0xd0000079 | The driver must complete the processing of received network packets\r\n
0xd000007a | Unspecified\r\n
0xd000007b | Incoming Packet\r\n
0xd000007c | Media Disconnect\r\n
0xd000007d | Media Connect\r\n
0xd000007e | Network List Offload Discovery\r\n
0xd000007f | AP Association Lost\r\n
0xd0000080 | GTK Handshake Error\r\n
0xd0000081 | 4-Way Handshake Request\r\n
0xd0000082 | Register State\r\n
0xd0000083 | SMS Receive\r\n
0xd0000084 | USSD Receive\r\n
0xd0000085 | Vendor Specific\r\n
0xd0000086 | Unspecified Component\r\n
0xd0000087 | TCPIP RS\r\n
0xd0000088 | DHCPv4\r\n
0xd0000089 | DHCPv6\r\n
0xd000008a | Wireless LAN\r\n
0xd000008b | Wireless WAN\r\n
0xd000008c | WCM\r\n
0xd000008d | NCSI\r\n
0xd000008e | Test\r\n
0xd000008f | EAP SIM\r\n
0xd0000090 | TCPIP OID\r\n
0xd0000091 | TCPIP Data\r\n
0xd0000092 | TCPIP DAD\r\n
0xd0000093 | Geolocation\r\n
0xd0000094 | WLAN Network Manager\r\n
0xd0000095 | WCM-PDC Network Activation\r\n
0xd0000096 | Unknown\r\n
0xd0000097 | Dx_SystemSleep: NDIS is requesting a low device power state because the system is going to a low power state\r\n
0xd0000098 | Dx_NicQuiet: NDIS is requesting a low device power state due to Connected Standby\r\n
0xd0000099 | Dx_SSIdle: NDIS is requesting a low device power state because the NIC is idle\r\n
0xd000009a | Dx_D3DTimeout: NDIS is requesting a low device power state because the NIC is disconnected\r\n
0xd000009b | D0_SystemResume: NDIS is requesting a working device power state due to a system resume\r\n
0xd000009c | D0_NicActive: NDIS is requesting device working power state due for maintaining connectivity during Connected Standby or due to Connected Standby exit\r\n
0xd000009d | D0_AoAcWake: NDIS is requesting that the device return to the operational power state because the device has indicated a wake signal\r\n
0xd000009e | D0_SSResume: NDIS is requesting that the device return to the operational power state because the NIC is no longer idle\r\n
0xd000009f | D0_D3DCancel: NDIS is requesting that the device return to the operational power state because the D3-on-disconnect has been disabled\r\n
0xd00000a0 | D0_D3DWake: NDIS is requesting that the device return to the operational power state because the NIC has indicated a wake\r\n
0xd00000a1 | D0_D3DResume: NDIS is requesting that the device return to the operational power state because NDIS needed to interact with the miniport driver\r\n
0xd00000a2 | D0_Complete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a3 | D0_SSComplete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a4 | Dx_Complete: The device's bus has acknowledged the low-power state\r\n
0xd00000a5 | Dx_SSComplete: The device's bus has acknowledged the low-power state\r\n
0xd00000a6 | SSIdle_Cancel: Idle Request that was sent down to the miniport is being cancelled\r\n
0xd00000a7 | SSIdle_Complete: The Idle Request has been successfully completed by the miniport driver\r\n
0xd00000a8 | D0_AoAcSurpriseWake: NDIS is requesting that the device return to the operational power state because the miniport driver indicated a surprise wake\r\n
0xd00000a9 | DeviceAdded: NDIS has successfully processed the enumeration of the miniport's hardware node\r\n
0xd00000aa | DeviceStart: The PNP subsystem has requested that NDIS start the device\r\n
0xd00000ab | DeviceQueryRemove: The PNP subsystem has requested that NDIS prepare to remove this device\r\n
0xd00000ac | DeviceCancelRemove: The PNP subsystem has canceled a remove request\r\n
0xd00000ad | DeviceRemove: The PNP subsystem has requested that NDIS remove the device\r\n
0xd00000ae | DeviceSurpriseRemoval: The PNP subsystem has indicated that the device was not enumerated by its bus anymore\r\n
0xd00000af | DeviceQueryStop: The PNP subsystem has requested that NDIS prepare to stop the device\r\n
0xd00000b0 | DeviceCancelStop: The PNP subsystem has canceled a pending stop request\r\n
0xd00000b1 | DeviceStop: The PNP subsystem has requested that NDIS stop the miniport device\r\n
0xd00000b2 | MiniportInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b3 | MiniportHalted: NDIS has halted the miniport\r\n
0xd00000b4 | MiniportPaused: NDIS has paused the miniport\r\n
0xd00000b5 | MiniportRestarted: NDIS has successfully restarted (unpaused) the miniport\r\n
0xd00000b6 | MiniportPmInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b7 | Fatal error: The miniport has entered an error state due to a user request\r\n
0xd00000b8 | Fatal error: The miniport has detected an internal error\r\n
0xd00000b9 | Fatal error: The IM miniport has failed to initialize\r\n
0xd00000ba | Fatal error: The miniport has failed to start by returning an error code from MiniportRestart\r\n
0xd00000bb | Fatal error: The miniport has failed a power transition to operational power\r\n
0xd00000bc | Fatal error: The miniport has failed a power transition to low power\r\n
0xd00000bd | Network Interface deleted while PNP Device still exists. Note that this event is provided for informational purpose and might not be an error always (Eg: In case of vSwitch which was recently un-installed or a LBFO team was removed)\r\n
0xd00000be | The network driver did not respond to an OID request in a timely fashion\r\n
0xd00000bf | The network driver detected that its hardware has stopped responding to commands\r\n
0xd00000c0 | The network driver requested that it be reset\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n

### 10.0.17763.404, 10.0.18362.1, 10.0.18362.693

Message identifier | Message string
--- | ---
0x0000284d | Miniport %4, %1, had event %5\r\n
0x000028a0 | The network interface "%4" has begun resetting.  There will be a momentary disruption in network connectivity while the hardware resets. Reason: %5. This network interface has reset %6 time(s) since it was last initialized.\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x7000000f | Refcount rundown\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0x90000004 | System\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %4, Adapter: %1, Result: %5\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Miniport %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI, IP1394, or Token Ring\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%4) Error %5\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Oid %7, Completed by NDIS on behalf of miniport with Status %6: %5\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb00027dc | Miniport %1 on processor %2 has an RST limit change from %5 to %6 NBLs per indication (NumNbls: %3, Duration: %4, Individual: %7, Cummulative: %8)\r\n
0xb000283c | The network adapter is idle and can be suspended now. Interface Luid: %1\r\n
0xb000283d | The network adapter declined to enter a suspended state. Interface Luid: %1 Status code: %2\r\n
0xb000283e | The network adapter must be resumed. Interface Luid: %1 Resume reason: %2\r\n
0xb000283f | NIC Active state is acquired.Interface Luid: %1 Component ID: %2 Component Ref Count: %3 Interface Ref Count: %4\r\n
0xb0002840 | NIC Active state is released. Interface Luid: %1 Component ID: %2 Component Ref Count: %3 Interface Ref Count: %4\r\n
0xb0002841 | The network adapter indicated a wake signal. Interface Luid: %1 Wake reason: %2\r\n
0xb0002842 | Working power state is requested for network adapter. Interface Luid: %3\r\n
0xb0002843 | Working power request is completed for network adapter. Interface Luid: %3 Status: %4\r\n
0xb0002844 | Low power state is requested for network adapter. Interface Luid: %3\r\n
0xb0002845 | Low power request is completed for network adapter. Interface Luid: %3 Status: %4\r\n
0xb0002846 | Wait/Wake IRP is completed for network adapter. Interface Luid: %3\r\n
0xb0002848 | Filter %1 entering state %2 (FriendlyName: %7)\r\n
0xb0002849 | Entering Connected Standby\r\n
0xb000284a | Exiting Connected Standby. Duration %1 sec.\r\n
0xb000284b | Miniport %2: CS active %3 seconds, %4 power transitions.\r\n
0xb000284c | Component %2: CS active %3 seconds, Miniport %1.\r\n
0xb0002850 | Refcount rundown for miniport %3 will follow\r\n
0xb0002851 | Refcount rundown for miniport %1: component %2 has refcount %3\r\n
0xb0002852 | Refcount rundown for miniport %1: stop flags %2 Rundown complete\r\n
0xb0002853 | Power transition for Miniport %2 in CS (%3 to %4). %3 traffic (In-Out): Unicast Packets (%5-%6), Multicast Packets (%7-%8), Broadcast Packets (%9-%10).\r\n
0xb0002854 | Miniport PDO information for Sleepstudy\r\n
0xb0002855 | Miniport %1 indicated a Wake Packet %3\r\n
0xb00028a1 | Timestamping change notification, interface NetLuid %1\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xd0000062 | The system is preparing to remove the device\r\n
0xd0000063 | The device was removed\r\n
0xd0000064 | The device was unexpectedly removed\r\n
0xd0000065 | The system is preparing to stop the device\r\n
0xd0000066 | The device was stopped\r\n
0xd0000067 | The system is entering a low-power state\r\n
0xd0000068 | The NIC is entering a quiet state\r\n
0xd0000069 | The miniport is performing a PNP operation\r\n
0xd000006a | Power save operations are not started yet on the miniport\r\n
0xd000006b | The miniport has encountered a fatal error\r\n
0xd000006c | Apply interface change after WLAN MAC randomization or L2 MTU update\r\n
0xd000006d | The driver must process a Magic Packet to allow Win32 Management Apps to resume execution\r\n
0xd000006e | The Miniport is performing Bind Changes.\r\n
0xd000006f | The driver must process a network OID request\r\n
0xd0000070 | The network stack must pause operation\r\n
0xd0000071 | The network stack must resume operation\r\n
0xd0000072 | The driver must be reset\r\n
0xd0000073 | The driver must process a PnP event notification\r\n
0xd0000074 | The driver must check for errors\r\n
0xd0000075 | The driver must process a Direct OID request\r\n
0xd0000076 | The driver must cancel a Direct OID request\r\n
0xd0000077 | The driver must transmit network packets\r\n
0xd0000078 | The driver must cancel network packets\r\n
0xd0000079 | The driver must complete the processing of received network packets\r\n
0xd000007a | Unspecified\r\n
0xd000007b | Incoming Packet\r\n
0xd000007c | Media Disconnect\r\n
0xd000007d | Media Connect\r\n
0xd000007e | Network List Offload Discovery\r\n
0xd000007f | AP Association Lost\r\n
0xd0000080 | GTK Handshake Error\r\n
0xd0000081 | 4-Way Handshake Request\r\n
0xd0000082 | Register State\r\n
0xd0000083 | SMS Receive\r\n
0xd0000084 | USSD Receive\r\n
0xd0000085 | Vendor Specific\r\n
0xd0000086 | Unspecified Component\r\n
0xd0000087 | TCPIP RS\r\n
0xd0000088 | DHCPv4\r\n
0xd0000089 | DHCPv6\r\n
0xd000008a | Wireless LAN\r\n
0xd000008b | Wireless WAN\r\n
0xd000008c | WCM\r\n
0xd000008d | NCSI\r\n
0xd000008e | Test\r\n
0xd000008f | EAP SIM\r\n
0xd0000090 | TCPIP OID\r\n
0xd0000091 | TCPIP Data\r\n
0xd0000092 | TCPIP DAD\r\n
0xd0000093 | Geolocation\r\n
0xd0000094 | WLAN Network Manager\r\n
0xd0000095 | WCM-PDC Network Activation\r\n
0xd0000096 | Unknown\r\n
0xd0000097 | Dx_SystemSleep: NDIS is requesting a low device power state because the system is going to a low power state\r\n
0xd0000098 | Dx_NicQuiet: NDIS is requesting a low device power state due to Connected Standby\r\n
0xd0000099 | Dx_SSIdle: NDIS is requesting a low device power state because the NIC is idle\r\n
0xd000009a | Dx_D3DTimeout: NDIS is requesting a low device power state because the NIC is disconnected\r\n
0xd000009b | D0_SystemResume: NDIS is requesting a working device power state due to a system resume\r\n
0xd000009c | D0_NicActive: NDIS is requesting device working power state due for maintaining connectivity during Connected Standby or due to Connected Standby exit\r\n
0xd000009d | D0_AoAcWake: NDIS is requesting that the device return to the operational power state because the device has indicated a wake signal\r\n
0xd000009e | D0_SSResume: NDIS is requesting that the device return to the operational power state because the NIC is no longer idle\r\n
0xd000009f | D0_D3DCancel: NDIS is requesting that the device return to the operational power state because the D3-on-disconnect has been disabled\r\n
0xd00000a0 | D0_D3DWake: NDIS is requesting that the device return to the operational power state because the NIC has indicated a wake\r\n
0xd00000a1 | D0_D3DResume: NDIS is requesting that the device return to the operational power state because NDIS needed to interact with the miniport driver\r\n
0xd00000a2 | D0_Complete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a3 | D0_SSComplete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a4 | Dx_Complete: The device's bus has acknowledged the low-power state\r\n
0xd00000a5 | Dx_SSComplete: The device's bus has acknowledged the low-power state\r\n
0xd00000a6 | SSIdle_Cancel: Idle Request that was sent down to the miniport is being cancelled\r\n
0xd00000a7 | SSIdle_Complete: The Idle Request has been successfully completed by the Miniport Driver\r\n
0xd00000a8 | SSIdle_Request: Idle Request is being sent to the Miniport Driver\r\n
0xd00000a9 | SSIdle_Confirm: The Idle Request has been successfully confirmed by the Miniport Driver\r\n
0xd00000aa | D0_AoAcSurpriseWake: NDIS is requesting that the device return to the operational power state because the miniport driver indicated a surprise wake\r\n
0xd00000ab | DeviceAdded: NDIS has successfully processed the enumeration of the miniport's hardware node\r\n
0xd00000ac | DeviceStart: The PNP subsystem has requested that NDIS start the device\r\n
0xd00000ad | DeviceQueryRemove: The PNP subsystem has requested that NDIS prepare to remove this device\r\n
0xd00000ae | DeviceCancelRemove: The PNP subsystem has canceled a remove request\r\n
0xd00000af | DeviceRemove: The PNP subsystem has requested that NDIS remove the device\r\n
0xd00000b0 | DeviceSurpriseRemoval: The PNP subsystem has indicated that the device was not enumerated by its bus anymore\r\n
0xd00000b1 | DeviceQueryStop: The PNP subsystem has requested that NDIS prepare to stop the device\r\n
0xd00000b2 | DeviceCancelStop: The PNP subsystem has canceled a pending stop request\r\n
0xd00000b3 | DeviceStop: The PNP subsystem has requested that NDIS stop the miniport device\r\n
0xd00000b4 | MiniportInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b5 | MiniportHalted: NDIS has halted the miniport\r\n
0xd00000b6 | MiniportPaused: NDIS has paused the miniport\r\n
0xd00000b7 | MiniportRestarted: NDIS has successfully restarted (unpaused) the miniport\r\n
0xd00000b8 | MiniportPmInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b9 | Fatal error: The miniport has entered an error state due to a user request\r\n
0xd00000ba | Fatal error: The miniport has detected an internal error\r\n
0xd00000bb | Fatal error: The IM miniport has failed to initialize\r\n
0xd00000bc | Fatal error: The miniport has failed to start by returning an error code from MiniportRestart\r\n
0xd00000bd | Fatal error: The miniport has failed a power transition to operational power\r\n
0xd00000be | Fatal error: The miniport has failed a power transition to low power\r\n
0xd00000bf | Network Interface deleted while PNP Device still exists. Note that this event is provided for informational purpose and might not be an error always (Eg: In case of vSwitch which was recently un-installed or a LBFO team was removed)\r\n
0xd00000c0 | The network driver did not respond to an OID request in a timely fashion\r\n
0xd00000c1 | The network driver detected that its hardware has stopped responding to commands\r\n
0xd00000c2 | The network driver requested that it be reset\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n

### 10.0.19041.84, 10.0.19041.630

Message identifier | Message string
--- | ---
0x0000284d | Miniport %4, %1, had event %5\r\n
0x000028a0 | The network interface "%4" has begun resetting.  There will be a momentary disruption in network connectivity while the hardware resets. Reason: %5. This network interface has reset %6 time(s) since it was last initialized.\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x7000000f | Refcount rundown\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0x90000004 | System\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %4, Adapter: %1, Result: %5\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Miniport %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI, IP1394, or Token Ring\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%4) Error %5\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Oid %7, Completed by NDIS on behalf of miniport with Status %6: %5\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb00027dc | Miniport %1 on processor %2 has an RST limit change from %5 to %6 NBLs per indication (NumNbls: %3, Duration: %4, Individual: %7, Cummulative: %8)\r\n
0xb000283c | The network adapter is idle and can be suspended now. Interface Luid: %1\r\n
0xb000283d | The network adapter declined to enter a suspended state. Interface Luid: %1 Status code: %2\r\n
0xb000283e | The network adapter must be resumed. Interface Luid: %1 Resume reason: %2\r\n
0xb000283f | NIC Active state is acquired.Interface Luid: %1 Component ID: %2 Component Ref Count: %3 Interface Ref Count: %4\r\n
0xb0002840 | NIC Active state is released. Interface Luid: %1 Component ID: %2 Component Ref Count: %3 Interface Ref Count: %4\r\n
0xb0002841 | The network adapter indicated a wake signal. Interface Luid: %1 Wake reason: %2\r\n
0xb0002842 | Working power state is requested for network adapter. Interface Luid: %3\r\n
0xb0002843 | Working power request is completed for network adapter. Interface Luid: %3 Status: %4\r\n
0xb0002844 | Low power state is requested for network adapter. Interface Luid: %3\r\n
0xb0002845 | Low power request is completed for network adapter. Interface Luid: %3 Status: %4\r\n
0xb0002846 | Wait/Wake IRP is completed for network adapter. Interface Luid: %3\r\n
0xb0002848 | Filter %1 entering state %2 (FriendlyName: %7)\r\n
0xb0002849 | Entering Connected Standby\r\n
0xb000284a | Exiting Connected Standby. Duration %1 sec.\r\n
0xb000284b | Miniport %2: CS active %3 seconds, %4 power transitions.\r\n
0xb000284c | Component %2: CS active %3 seconds, Miniport %1.\r\n
0xb0002850 | Refcount rundown for miniport %3 will follow\r\n
0xb0002851 | Refcount rundown for miniport %1: component %2 has refcount %3\r\n
0xb0002852 | Refcount rundown for miniport %1: stop flags %2 Rundown complete\r\n
0xb0002853 | Power transition for Miniport %2 in CS (%3 to %4). %3 traffic (In-Out): Unicast Packets (%5-%6), Multicast Packets (%7-%8), Broadcast Packets (%9-%10).\r\n
0xb0002854 | Miniport PDO information for Sleepstudy\r\n
0xb0002855 | Miniport %1 indicated a Wake Packet %3\r\n
0xb00028a1 | Timestamping change notification, interface NetLuid %1\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xd0000062 | The system is preparing to remove the device\r\n
0xd0000063 | The device was removed\r\n
0xd0000064 | The device was unexpectedly removed\r\n
0xd0000065 | The system is preparing to stop the device\r\n
0xd0000066 | The device was stopped\r\n
0xd0000067 | The system is entering a low-power state\r\n
0xd0000068 | The NIC is entering a quiet state\r\n
0xd0000069 | The miniport is performing a PNP operation\r\n
0xd000006a | Power save operations are not started yet on the miniport\r\n
0xd000006b | The miniport has encountered a fatal error\r\n
0xd000006c | Apply interface change after WLAN MAC randomization or L2 MTU update\r\n
0xd000006d | The driver must process a Magic Packet to allow Win32 Management Apps to resume execution\r\n
0xd000006e | The Miniport is performing Bind Changes.\r\n
0xd000006f | The driver must process a network OID request\r\n
0xd0000070 | The network stack must pause operation\r\n
0xd0000071 | The network stack must resume operation\r\n
0xd0000072 | The driver must be reset\r\n
0xd0000073 | The driver must process a PnP event notification\r\n
0xd0000074 | The driver must check for errors\r\n
0xd0000075 | The driver must process a Direct OID request\r\n
0xd0000076 | The driver must cancel a Direct OID request\r\n
0xd0000077 | The driver must transmit network packets\r\n
0xd0000078 | The driver must cancel network packets\r\n
0xd0000079 | The driver must complete the processing of received network packets\r\n
0xd000007a | Unspecified\r\n
0xd000007b | Incoming Packet\r\n
0xd000007c | Media Disconnect\r\n
0xd000007d | Media Connect\r\n
0xd000007e | Network List Offload Discovery\r\n
0xd000007f | AP Association Lost\r\n
0xd0000080 | GTK Handshake Error\r\n
0xd0000081 | 4-Way Handshake Request\r\n
0xd0000082 | Register State\r\n
0xd0000083 | SMS Receive\r\n
0xd0000084 | USSD Receive\r\n
0xd0000085 | Vendor Specific\r\n
0xd0000086 | Packet State\r\n
0xd0000087 | Uicc Change\r\n
0xd0000088 | Unspecified Component\r\n
0xd0000089 | TCPIP RS\r\n
0xd000008a | DHCPv4\r\n
0xd000008b | DHCPv6\r\n
0xd000008c | Wireless LAN\r\n
0xd000008d | Wireless WAN\r\n
0xd000008e | WCM\r\n
0xd000008f | NCSI\r\n
0xd0000090 | Test\r\n
0xd0000091 | EAP SIM\r\n
0xd0000092 | TCPIP OID\r\n
0xd0000093 | TCPIP Data\r\n
0xd0000094 | TCPIP DAD\r\n
0xd0000095 | Geolocation\r\n
0xd0000096 | WLAN Network Manager\r\n
0xd0000097 | WCM-PDC Network Activation\r\n
0xd0000098 | Unknown\r\n
0xd0000099 | Dx_SystemSleep: NDIS is requesting a low device power state because the system is going to a low power state\r\n
0xd000009a | Dx_NicQuiet: NDIS is requesting a low device power state due to Connected Standby\r\n
0xd000009b | Dx_SSIdle: NDIS is requesting a low device power state because the NIC is idle\r\n
0xd000009c | Dx_D3DTimeout: NDIS is requesting a low device power state because the NIC is disconnected\r\n
0xd000009d | D0_SystemResume: NDIS is requesting a working device power state due to a system resume\r\n
0xd000009e | D0_NicActive: NDIS is requesting device working power state due for maintaining connectivity during Connected Standby or due to Connected Standby exit\r\n
0xd000009f | D0_AoAcWake: NDIS is requesting that the device return to the operational power state because the device has indicated a wake signal\r\n
0xd00000a0 | D0_SSResume: NDIS is requesting that the device return to the operational power state because the NIC is no longer idle\r\n
0xd00000a1 | D0_D3DCancel: NDIS is requesting that the device return to the operational power state because the D3-on-disconnect has been disabled\r\n
0xd00000a2 | D0_D3DWake: NDIS is requesting that the device return to the operational power state because the NIC has indicated a wake\r\n
0xd00000a3 | D0_D3DResume: NDIS is requesting that the device return to the operational power state because NDIS needed to interact with the miniport driver\r\n
0xd00000a4 | D0_Complete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a5 | D0_SSComplete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a6 | Dx_Complete: The device's bus has acknowledged the low-power state\r\n
0xd00000a7 | Dx_SSComplete: The device's bus has acknowledged the low-power state\r\n
0xd00000a8 | SSIdle_Cancel: Idle Request that was sent down to the miniport is being cancelled\r\n
0xd00000a9 | SSIdle_Complete: The Idle Request has been successfully completed by the Miniport Driver\r\n
0xd00000aa | SSIdle_Request: Idle Request is being sent to the Miniport Driver\r\n
0xd00000ab | SSIdle_Confirm: The Idle Request has been successfully confirmed by the Miniport Driver\r\n
0xd00000ac | D0_AoAcSurpriseWake: NDIS is requesting that the device return to the operational power state because the miniport driver indicated a surprise wake\r\n
0xd00000ad | DeviceAdded: NDIS has successfully processed the enumeration of the miniport's hardware node\r\n
0xd00000ae | DeviceStart: The PNP subsystem has requested that NDIS start the device\r\n
0xd00000af | DeviceQueryRemove: The PNP subsystem has requested that NDIS prepare to remove this device\r\n
0xd00000b0 | DeviceCancelRemove: The PNP subsystem has canceled a remove request\r\n
0xd00000b1 | DeviceRemove: The PNP subsystem has requested that NDIS remove the device\r\n
0xd00000b2 | DeviceSurpriseRemoval: The PNP subsystem has indicated that the device was not enumerated by its bus anymore\r\n
0xd00000b3 | DeviceQueryStop: The PNP subsystem has requested that NDIS prepare to stop the device\r\n
0xd00000b4 | DeviceCancelStop: The PNP subsystem has canceled a pending stop request\r\n
0xd00000b5 | DeviceStop: The PNP subsystem has requested that NDIS stop the miniport device\r\n
0xd00000b6 | MiniportInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000b7 | MiniportHalted: NDIS has halted the miniport\r\n
0xd00000b8 | MiniportPaused: NDIS has paused the miniport\r\n
0xd00000b9 | MiniportRestarted: NDIS has successfully restarted (unpaused) the miniport\r\n
0xd00000ba | MiniportPmInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000bb | Fatal error: The miniport has entered an error state due to a user request\r\n
0xd00000bc | Fatal error: The miniport has detected an internal error\r\n
0xd00000bd | Fatal error: The IM miniport has failed to initialize\r\n
0xd00000be | Fatal error: The miniport has failed to start by returning an error code from MiniportRestart\r\n
0xd00000bf | Fatal error: The miniport has failed a power transition to operational power\r\n
0xd00000c0 | Fatal error: The miniport has failed a power transition to low power\r\n
0xd00000c1 | Network Interface deleted while PNP Device still exists. Note that this event is provided for informational purpose and might not be an error always (Eg: In case of vSwitch which was recently un-installed or a LBFO team was removed)\r\n
0xd00000c2 | The network driver did not respond to an OID request in a timely fashion\r\n
0xd00000c3 | The network driver detected that its hardware has stopped responding to commands\r\n
0xd00000c4 | The network driver requested that it be reset\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n

### 10.0.22000.65

Message identifier | Message string
--- | ---
0x0000284d | Miniport %4, %1, had event %5\r\n
0x000028a0 | The network interface "%4" has begun resetting.  There will be a momentary disruption in network connectivity while the hardware resets. Reason: %5. This network interface has reset %6 time(s) since it was last initialized.\r\n
0x00002904 | HAL's SupportFlags(value=%1) indicates DMA hybrid passthrough is not supported on system\r\n
0x00002905 | A NDIS object (type=%1, handle=%2) registers hybrid SG_DMA_BLOCK on system that doesn't support hybrid DMA (SupportFlags=%3)\r\n
0x00002906 | AzDmaV3 version NdisAllocateSharedMemory exceeds threshold: State %1, NetworkInterfaceGuid %2, QueueId %3, VPortId %4, NumaNode %5, AllocationSize %6, AllocationTimeUs %7, AllocationTimeThresholdUs %8\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000b4 | Start State\r\n
0x300000b5 | End State\r\n
0x300000b6 | Closed State\r\n
0x300000b7 | Open State\r\n
0x300000b8 | Connect State\r\n
0x300000b9 | Listen State\r\n
0x300000ba | Association State\r\n
0x300000bb | Authentication State\r\n
0x300000bc | Established State\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Request\r\n
0x70000002 | PnP\r\n
0x70000003 | Init\r\n
0x70000004 | Bind\r\n
0x70000005 | Power\r\n
0x70000006 | WMI\r\n
0x70000007 | Interface\r\n
0x70000008 | Port\r\n
0x70000009 | WorkItem\r\n
0x7000000a | Indication\r\n
0x7000000b | SendM\r\n
0x7000000c | Protocol\r\n
0x7000000d | Log\r\n
0x7000000e | ReceiveThrottling\r\n
0x7000000f | Refcount rundown\r\n
0x70000010 | Alloc\r\n
0x90000001 | Microsoft-Windows-NDIS\r\n
0x90000002 | Microsoft-Windows-NDIS/Operational\r\n
0x90000003 | Microsoft-Windows-NDIS/Diagnostic\r\n
0x90000004 | System\r\n
0xb0002710 | Aborting Request %4 on Filter %5\r\n
0xb0002711 | Aborting Request %4 on Miniport %5\r\n
0xb0002712 | Add Device Miniport %1\r\n
0xb0002713 | Add Device Failed %1\r\n
0xb0002714 | Add PnP Device: %1\r\n
0xb0002715 | Allocate Adapter Channel Failed %1\r\n
0xb0002716 | Initialize Binding - Protocol: %4, Adapter: %1, Result: %5\r\n
0xb0002717 | Miniport %1, Calling miniport reset\r\n
0xb0002718 | Filter %1, Aborting Request %4\r\n
0xb0002719 | Miniport %1, Successfully canceled wake irp\r\n
0xb000271a | Miniport %1, Aborting Request %4\r\n
0xb000271b | Miniport %1, Failed to set the new information on the miniport\r\n
0xb000271c | Compartment change notification, compartment %1\r\n
0xb000271d | Interface change notification, interface IfType %1, NetLuid index %2\r\n
0xb000271f | Network change notification, network %1\r\n
0xb0002720 | Request Clearing Processing Request Miniport %1\r\n
0xb0002721 | Protocol %4 is closing Miniport %1\r\n
0xb0002722 | Completing Request %4 to Filter %1\r\n
0xb0002723 | Miniport %1, WaitWakeIrp %4\r\n
0xb0002724 | Miniport %1, activating default port\r\n
0xb0002725 | Miniport %1, deactivating default port\r\n
0xb0002726 | Failed to deregister interface IfBlock %3\r\n
0xb0002727 | DevicePowerStateChange Miniport %1, Going to device state %5\r\n
0xb0002728 | Dispatch PnP Irp Miniport %1, MinorFunction: %4\r\n
0xb0002729 | Dispatch WMI Irp Miniport %1, MinorFunction %4\r\n
0xb000272a | Miniport %1, Failed to execute WMI method (%6) on the miniport\r\n
0xb000272b | Failed to indicate filter arrival\r\n
0xb000272c | Miniport %1, Filter %4 changed media type from %7 to %8\r\n
0xb000272d | Filter Registration Failed %1 - %2\r\n
0xb000272e | Failed to indicate filter removal\r\n
0xb000272f | Failed to indicate adapter removal\r\n
0xb0002730 | Miniport %1, InitializeAdapter status - %4 (%5)\r\n
0xb0002731 | Miniport %1, InitializeAdapter error - %4 (%5)\r\n
0xb0002732 | Could not read Bind/Export for %4: %1\r\n
0xb0002733 | Miniport %1, Not a system state! Type: %4. State: %5.\r\n
0xb0002735 | IoSetDeviceInterfaceState failed: Miniport %1, Status %4\r\n
0xb0002736 | IoWMIWriteEvent failed %1\r\n
0xb0002737 | DeviceObject %3, IRP_MN_SET_POWER failed!\r\n
0xb0002738 | Keeping the fake handlers on Filter %1, State flags %4\r\n
0xb0002739 | Keeping the fake handlers on Miniport %1, State flags %4\r\n
0xb000273a | Open %3 is already getting unbind\r\n
0xb000273b | Miniport %1 is %4\r\n
0xb000273c | Miniport %1 - MiniportInitialize handler failed, Status %4\r\n
0xb000273d | Miniport %1, Ethernet Address %4\r\n
0xb000273e | Miniport %1, DeviceState[%5]\r\n
0xb000273f | Miniport %1, Powering up the Miniport\r\n
0xb0002740 | Miniport %1, SystemPowerState[%4] DevicePowerState[%5]\r\n
0xb0002741 | Miniport %1, SystemState[%5]\r\n
0xb0002742 | Failed to restart miniport %1. Status %4\r\n
0xb0002744 | Error querying %4 : %5\r\n
0xb0002745 | Failing open because the miniport is not started, Miniport %1, Open %4\r\n
0xb0002746 | Port Activation Failed Miniport %1 %4\r\n
0xb0002747 | Miniport %1, Disabling wake-up on the miniport\r\n
0xb0002748 | Miniport %1, Failed to power the device down\r\n
0xb0002749 | Miniport %1, failed to power down but we are not able to reinitialize it.\r\n
0xb000274a | Miniport %1, Halt the miniport\r\n
0xb000274b | Miniport %1, System is either entering hibernate or shutting down.\r\n
0xb000274c | DeviceObject %1, Going to system power state %2\r\n
0xb000274d | Miniport %1 is not started yet.\r\n
0xb000274e | Miniport %1 is being removed\r\n
0xb000274f | Miniport %1, MagicPacket and pattern match are not enabled.\r\n
0xb0002750 | Miniport %1, Place legacy or PM disabled device in D3\r\n
0xb0002751 | Miniport %1, SystemState %4, DeviceState %5\r\n
0xb0002752 | Miniport %1, shutting down\r\n
0xb0002753 | Miniport %1, Device power wake is not enabled (%4)\r\n
0xb0002754 | Miniport %1, Waking up the device\r\n
0xb0002755 | BIND (%1) %2 to %3\r\n
0xb0002756 | UNBIND(%1) %2 to %3\r\n
0xb0002757 | Miniport %1, IRP_MN_QUERY_PNP_DEVICE_STATE device failed\r\n
0xb0002758 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb0002759 | Miniport %1, Bus Driver returned %4 for QueryPower.\r\n
0xb000275a | Miniport %1, failed power Oid %5, Set = %6 with error %4\r\n
0xb000275b | ndisReferenceProtocolByName failed %1\r\n
0xb000275c | Miniport %1 failed to register for interrupts\r\n
0xb000275d | DriverObject %3, Miniport Driver should register both a DirectRequest and CancelDirectRequest handler or neither one\r\n
0xb000275e | SendPacketCompleteToOpen Open %1, Packet %2\r\n
0xb000275f | ndisSetEnableWakeUp Completed\r\n
0xb0002760 | SetMiniportEthMulticastList Failed Miniport %1, Request %6\r\n
0xb0002761 | SetMiniportRSSCaps Failed Miniport %1, Request %6, Status %4\r\n
0xb0002762 | SetOpenEthAddDeleteMulticast Failed, Miniport = %1, Open = %6, Status = %4\r\n
0xb0002763 | SetOpenEthMulticastList failed - Miniport %1, Open %6\r\n
0xb0002764 | SetOpenFunctional - Invalid media type\r\n
0xb0002765 | SetOpenGroupAddress - Invalid media type\r\n
0xb0002766 | SetOpenRSSCaps: Miniport %1, Open %6, Status %4\r\n
0xb0002767 | Miniport %1, Going to system power state %5\r\n
0xb0002768 | Transport %4 failed the PnP event: %5 for Miniport %1 with Status %6\r\n
0xb0002769 | Miniport %1, This version of NDIS does not support Arcnet, FDDI, IP1394, or Token Ring\r\n
0xb000276a | %1, %2\r\n
0xb000276b | Miniport %1, Wake irp was complete due to wake event\r\n
0xb000276c | WaitWakeIrpFailed Miniport %1, WAIT_WAKE irp failed or cancelled. Status %4\r\n
0xb000276d | Miniport %1 woke up the system.\r\n
0xb000276e | Error Log Entry : Miniport %1 (%4) Error %5\r\n
0xb000276f | Aborting Request %4\r\n
0xb0002770 | Port Deactivation Failed Miniport %1 %4\r\n
0xb0002771 | Miniport %1, PoRequestPowerIrp for device state returned %4\r\n
0xb0002772 | Miniport %1, failed query power\r\n
0xb0002773 | DevicePowerOn failed Miniport %1, status %4\r\n
0xb0002774 | Power policy - Unable to enter requested state\r\n
0xb0002775 | Miniport %1: Oid %7, Completed by NDIS on behalf of miniport with Status %6: %5\r\n
0xb0002776 | Completing Request %4 to Miniport %1\r\n
0xb0002777 | Filter %1 entering state %2\r\n
0xb0002778 | Miniport %1, NDIS_STATUS_MEDIA_CONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb0002779 | Miniport %1, NDIS_STATUS_MEDIA_DISCONNECT, Flags: %4, PnpFlags %5, DevicePowerState %6\r\n
0xb000277a | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277b | Miniport %1, NDIS_STATUS_OPER_STATUS, OperationalStatus: %4, OperationalStatusFlags: %5\r\n
0xb000277c | Miniport %1, NDIS_STATUS_NETWORK_CHANGE, Change Type: %4\r\n
0xb00027d8 | DPC/OtherDispatchRoutine Start\r\n
0xb00027d9 | DPC/OtherDispatchRoutine End\r\n
0xb00027da | Queued Receive Indication Start\r\n
0xb00027db | Queued Receive Indication End\r\n
0xb00027dc | Miniport %1 on processor %2 has an RST limit change from %5 to %6 NBLs per indication (NumNbls: %3, Duration: %4, Individual: %7, Cummulative: %8)\r\n
0xb000283c | The network adapter is idle and can be suspended now. Interface Luid: %1\r\n
0xb000283d | The network adapter declined to enter a suspended state. Interface Luid: %1 Status code: %2\r\n
0xb000283e | The network adapter must be resumed. Interface Luid: %1 Resume reason: %2\r\n
0xb000283f | NIC Active state is acquired. Interface Luid: %1 Component ID: %2 Component Ref Count: %3 Interface Ref Count: %4\r\n
0xb0002840 | NIC Active state is released. Interface Luid: %1 Component ID: %2 Component Ref Count: %3 Interface Ref Count: %4\r\n
0xb0002841 | The network adapter indicated a wake signal. Interface Luid: %1 Wake reason: %2\r\n
0xb0002842 | Working power state is requested for network adapter. Interface Luid: %3\r\n
0xb0002843 | Working power request is completed for network adapter. Interface Luid: %3 Status: %4\r\n
0xb0002844 | Low power state is requested for network adapter. Interface Luid: %3\r\n
0xb0002845 | Low power request is completed for network adapter. Interface Luid: %3 Status: %4\r\n
0xb0002846 | Wait/Wake IRP is completed for network adapter. Interface Luid: %3\r\n
0xb0002848 | Filter %1 entering state %2 (FriendlyName: %7)\r\n
0xb0002849 | Entering Connected Standby\r\n
0xb000284a | Exiting Connected Standby. Duration %1 sec.\r\n
0xb000284b | Miniport %2: CS active %3 seconds, %4 power transitions.\r\n
0xb000284c | Component %2: CS active %3 seconds, Miniport %1.\r\n
0xb0002850 | Refcount rundown for miniport %3 will follow\r\n
0xb0002851 | Refcount rundown for miniport %1: component %2 has refcount %3\r\n
0xb0002852 | Refcount rundown for miniport %1: stop flags %2 Rundown complete\r\n
0xb0002853 | Power transition for Miniport %2 in CS (%3 to %4). %3 traffic (In-Out): Unicast Packets (%5-%6), Multicast Packets (%7-%8), Broadcast Packets (%9-%10).\r\n
0xb0002854 | Miniport PDO information for Sleepstudy\r\n
0xb0002855 | Miniport %1 indicated a Wake Packet %3\r\n
0xb00028a1 | Timestamping change notification, interface NetLuid %1\r\n
0xb00028a2 | Miniport %1 Capabilities: Flags %2, SupportedWoLPatterns %3, SupportedProtocolOffloads %4, SupportedWakeUpEvents %5, SupportedMediaWakeUpEvents %6; PmParameter: IdleCondition %7, WolPatterns %8, ProtocolOffloads %9, WakeUpFlags %10, MediaWakeUpEvents %11\r\n
0xb000ea61 | Error: %1 Location: %2 Context: %3\r\n
0xb000ea62 | Warning: %1 Location: %2 Context: %3\r\n
0xb000ea63 | Transitioned to State: %1 Context: %2\r\n
0xb000ea64 | Updated Context: %1 Update Reason: %2\r\n
0xb000eac5 | SourceAddress: %1 SourcePort: %2 DestinationAddress: %3 DestinationPort: %4 Protocol: %5 ReferenceContext: %6\r\n
0xb000eac7 | Interface Guid: %1 IfIndex: %2 Interface Luid: %3 ReferenceContext: %4\r\n
0xd0000001 | InitializeHandler\r\n
0xd0000002 | Error creating Ndis Supported Oid List\r\n
0xd0000003 | WOL not possible on this miniport\r\n
0xd0000004 | Error creating the Ethernet filter database\r\n
0xd0000005 | Error creating the Token Ring filter database\r\n
0xd0000006 | Error creating the NULL filter database\r\n
0xd0000007 | Error creating the NULL bottom most filter database\r\n
0xd0000008 | IoWMIRegistrationControl failed\r\n
0xd0000009 | IoRegisterDeviceClassAssociation failed\r\n
0xd000000a | ndisIfUpdateInterfaceOnInitialize failed\r\n
0xd000000b | ndisQueryOidList failed\r\n
0xd000000c | IRP_MN_QUERY_ALL_DATA\r\n
0xd000000d | IRP_MN_QUERY_SINGLE_INSTANCE\r\n
0xd000000e | IRP_MN_CHANGE_SINGLE_INSTANCE\r\n
0xd000000f | IRP_MN_CHANGE_SINGLE_ITEM\r\n
0xd0000010 | IRP_MN_ENABLE_EVENTS\r\n
0xd0000011 | IRP_MN_DISABLE_EVENTS\r\n
0xd0000012 | IRP_MN_ENABLE_COLLECTION\r\n
0xd0000013 | IRP_MN_DISABLE_COLLECTION\r\n
0xd0000014 | IRP_MN_REGINFO\r\n
0xd0000015 | IRP_MN_EXECUTE_METHOD\r\n
0xd0000016 | IRP_MN_REGINFO_EX\r\n
0xd0000017 | IRP_MN_START_DEVICE\r\n
0xd0000018 | IRP_MN_QUERY_REMOVE_DEVICE\r\n
0xd0000019 | IRP_MN_REMOVE_DEVICE\r\n
0xd000001a | IRP_MN_CANCEL_REMOVE_DEVICE\r\n
0xd000001b | IRP_MN_STOP_DEVICE\r\n
0xd000001c | IRP_MN_QUERY_STOP_DEVICE\r\n
0xd000001d | IRP_MN_CANCEL_STOP_DEVICE\r\n
0xd000001e | IRP_MN_QUERY_DEVICE_RELATIONS\r\n
0xd000001f | IRP_MN_QUERY_INTERFACE\r\n
0xd0000020 | IRP_MN_QUERY_CAPABILITIES\r\n
0xd0000021 | IRP_MN_QUERY_RESOURCES\r\n
0xd0000022 | IRP_MN_QUERY_RESOURCE_REQUIREMENTS\r\n
0xd0000023 | IRP_MN_QUERY_DEVICE_TEXT\r\n
0xd0000024 | IRP_MN_FILTER_RESOURCE_REQUIREMENTS\r\n
0xd0000025 | IRP_MN_READ_CONFIG\r\n
0xd0000026 | IRP_MN_WRITE_CONFIG\r\n
0xd0000027 | IRP_MN_EJECT\r\n
0xd0000028 | IRP_MN_SET_LOCK\r\n
0xd0000029 | IRP_MN_QUERY_ID\r\n
0xd000002a | IRP_MN_QUERY_PNP_DEVICE_STATE\r\n
0xd000002b | IRP_MN_QUERY_BUS_INFORMATION\r\n
0xd000002c | IRP_MN_DEVICE_USAGE_NOTIFICATION\r\n
0xd000002d | IRP_MN_SURPRISE_REMOVAL\r\n
0xd000002e | Halting\r\n
0xd000002f | Reset Requested\r\n
0xd0000030 | Reset Pending\r\n
0xd0000031 | SendNetBufferListsCompleteHandler is invalid\r\n
0xd0000032 | ReceiveNetBufferListsHandler is invalid\r\n
0xd0000033 | OidRequestCompleteHandler is invalid\r\n
0xd0000034 | NULL Port List\r\n
0xd0000035 | invalid port activation request for default port\r\n
0xd0000036 | default port is already activated\r\n
0xd0000037 | port is not found\r\n
0xd0000038 | port is not in allocated state\r\n
0xd0000039 | invalid deactivation request for default port\r\n
0xd000003a | default port is already deactivated\r\n
0xd000003b | port is not in activated state\r\n
0xd000003c | Filter Driver version number is invalid\r\n
0xd000003d | Filter Driver is missing the required Handlers\r\n
0xd000003e | Filter Driver should either register both a Request and RequestComplete Handler or neither of them\r\n
0xd000003f | Filter Driver can only register Cancel Request handler when registering the Request Handler\r\n
0xd0000040 | Filter Driver should either register both a DirectRequest and DirectRequestComplete Handler or neither of them\r\n
0xd0000041 | Filter Driver can only register Cancel Direct Request handler when registering the Direct request Handler\r\n
0xd0000042 | Filter Driver can only register Cancel Send handler when registering the Send Handler\r\n
0xd0000043 | Filter Driver names are too long\r\n
0xd0000044 | OID_GEN_MAXIMUM_LOOKAHEAD\r\n
0xd0000045 | OID_GEN_MAXIMUM_FRAME_SIZE\r\n
0xd0000046 | OID_GEN_MAC_OPTIONS\r\n
0xd0000047 | OID_GEN_MAXIMUM_SEND_PACKETS\r\n
0xd0000048 | OID_802_3_PERMANENT_ADDRESS\r\n
0xd0000049 | OID_802_3_CURRENT_ADDRESS\r\n
0xd000004a | OID_802_3_MAXIMUM_LIST_SIZE\r\n
0xd000004b | OID_802_5_PERMANENT_ADDRESS\r\n
0xd000004c | OID_802_5_CURRENT_ADDRESS\r\n
0xd000004d | OID_WAN_PERMANENT_ADDRESS\r\n
0xd000004e | OID_WAN_CURRENT_ADDRESS\r\n
0xd000004f | OID_PNP_SET_POWER\r\n
0xd0000050 | OID_PNP_QUERY_POWER\r\n
0xd0000051 | Detached\r\n
0xd0000052 | Attaching\r\n
0xd0000053 | Paused\r\n
0xd0000054 | Restarting\r\n
0xd0000055 | Running\r\n
0xd0000056 | Pausing\r\n
0xd0000057 | Detaching\r\n
0xd0000058 | UP\r\n
0xd0000059 | DOWN\r\n
0xd000005a | TESTING\r\n
0xd000005b | UNKNOWN\r\n
0xd000005c | DORMANT\r\n
0xd000005d | NOT_PRESENT\r\n
0xd000005e | LOWER_LAYER_DOWN\r\n
0xd000005f | PossibleNetworkChange\r\n
0xd0000060 | DefinitelyNetworkChange\r\n
0xd0000061 | NetworkChangeFromMediaConnect\r\n
0xd0000062 | The system is preparing to remove the device\r\n
0xd0000063 | The device was removed\r\n
0xd0000064 | The device was unexpectedly removed\r\n
0xd0000065 | The system is preparing to stop the device\r\n
0xd0000066 | The device was stopped\r\n
0xd0000067 | The system is entering a low-power state\r\n
0xd0000068 | The NIC is entering a quiet state\r\n
0xd0000069 | The miniport is performing a PNP operation\r\n
0xd000006a | Power save operations are not started yet on the miniport\r\n
0xd000006b | The miniport has encountered a fatal error\r\n
0xd000006c | Apply interface change after WLAN MAC randomization or L2 MTU update\r\n
0xd000006d | The driver must process a Magic Packet to allow Win32 Management Apps to resume execution\r\n
0xd000006e | The Miniport is performing Bind Changes.\r\n
0xd000006f | The driver must process a network OID request\r\n
0xd0000070 | The network stack must pause operation\r\n
0xd0000071 | The network stack must resume operation\r\n
0xd0000072 | The driver must be reset\r\n
0xd0000073 | The driver must process a PnP event notification\r\n
0xd0000074 | The driver must check for errors\r\n
0xd0000075 | The driver must process a Direct OID request\r\n
0xd0000076 | The driver must cancel a Direct OID request\r\n
0xd0000077 | The driver must transmit network packets\r\n
0xd0000078 | The driver must cancel network packets\r\n
0xd0000079 | The driver must complete the processing of received network packets\r\n
0xd000007a | Unspecified\r\n
0xd000007b | Incoming Packet\r\n
0xd000007c | Media Disconnect\r\n
0xd000007d | Media Connect\r\n
0xd000007e | Network List Offload Discovery\r\n
0xd000007f | AP Association Lost\r\n
0xd0000080 | GTK Handshake Error\r\n
0xd0000081 | 4-Way Handshake Request\r\n
0xd0000082 | Register State\r\n
0xd0000083 | SMS Receive\r\n
0xd0000084 | USSD Receive\r\n
0xd0000085 | Vendor Specific\r\n
0xd0000086 | Packet State\r\n
0xd0000087 | Uicc Change\r\n
0xd0000088 | Unspecified Component\r\n
0xd0000089 | TCPIP RS\r\n
0xd000008a | DHCPv4\r\n
0xd000008b | DHCPv6\r\n
0xd000008c | Wireless LAN\r\n
0xd000008d | Wireless WAN\r\n
0xd000008e | WCM\r\n
0xd000008f | NCSI\r\n
0xd0000090 | Test\r\n
0xd0000091 | EAP SIM\r\n
0xd0000092 | TCPIP OID\r\n
0xd0000093 | TCPIP Data\r\n
0xd0000094 | TCPIP DAD\r\n
0xd0000095 | Geolocation\r\n
0xd0000096 | WLAN Network Manager\r\n
0xd0000097 | WCM-PDC Network Activation\r\n
0xd0000098 | Unknown\r\n
0xd0000099 | Dx_SystemSleep: NDIS is requesting a low device power state because the system is going to a low power state\r\n
0xd000009a | Dx_NicQuiet: NDIS is requesting a low device power state due to Connected Standby\r\n
0xd000009b | Dx_SSIdle: NDIS is requesting a low device power state because the NIC is idle\r\n
0xd000009c | Dx_D3DTimeout: NDIS is requesting a low device power state because the NIC is disconnected\r\n
0xd000009d | D0_SystemResume: NDIS is requesting a working device power state due to a system resume\r\n
0xd000009e | D0_NicActive: NDIS is requesting device working power state due for maintaining connectivity during Connected Standby or due to Connected Standby exit\r\n
0xd000009f | D0_AoAcWake: NDIS is requesting that the device return to the operational power state because the device has indicated a wake signal\r\n
0xd00000a0 | D0_SSResume: NDIS is requesting that the device return to the operational power state because the NIC is no longer idle\r\n
0xd00000a1 | D0_D3DCancel: NDIS is requesting that the device return to the operational power state because the D3-on-disconnect has been disabled\r\n
0xd00000a2 | D0_D3DWake: NDIS is requesting that the device return to the operational power state because the NIC has indicated a wake\r\n
0xd00000a3 | D0_D3DResume: NDIS is requesting that the device return to the operational power state because NDIS needed to interact with the miniport driver\r\n
0xd00000a4 | D0_Complete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a5 | D0_SSComplete: The device's bus is ready to return the device to an operational power state\r\n
0xd00000a6 | Dx_Complete: The device's bus has acknowledged the low-power state\r\n
0xd00000a7 | Dx_SSComplete: The device's bus has acknowledged the low-power state\r\n
0xd00000a8 | SSIdle_Cancel: Idle Request that was sent down to the miniport is being cancelled\r\n
0xd00000a9 | SSIdle_Complete: The Idle Request has been successfully completed by the Miniport Driver\r\n
0xd00000aa | SSIdle_Request: Idle Request is being sent to the Miniport Driver\r\n
0xd00000ab | SSIdle_Confirm: The Idle Request has been successfully confirmed by the Miniport Driver\r\n
0xd00000ac | D0_AoAcSurpriseWake: NDIS is requesting that the device return to the operational power state because the miniport driver indicated a surprise wake\r\n
0xd00000ad | D0_S0Idle: WDF completed a S0-idle power up transition\r\n
0xd00000ae | Dx_S0Idle: WDF completed a S0-idle power down transition\r\n
0xd00000af | D0_Sx: WDF completed a Sx power up transition\r\n
0xd00000b0 | Dx_Sx: WDF completed a Sx power down transition\r\n
0xd00000b1 | DeviceAdded: NDIS has successfully processed the enumeration of the miniport's hardware node\r\n
0xd00000b2 | DeviceStart: The PNP subsystem has requested that NDIS start the device\r\n
0xd00000b3 | DeviceQueryRemove: The PNP subsystem has requested that NDIS prepare to remove this device\r\n
0xd00000b4 | DeviceCancelRemove: The PNP subsystem has canceled a remove request\r\n
0xd00000b5 | DeviceRemove: The PNP subsystem has requested that NDIS remove the device\r\n
0xd00000b6 | DeviceSurpriseRemoval: The PNP subsystem has indicated that the device was not enumerated by its bus anymore\r\n
0xd00000b7 | DeviceQueryStop: The PNP subsystem has requested that NDIS prepare to stop the device\r\n
0xd00000b8 | DeviceCancelStop: The PNP subsystem has canceled a pending stop request\r\n
0xd00000b9 | DeviceStop: The PNP subsystem has requested that NDIS stop the miniport device\r\n
0xd00000ba | MiniportInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000bb | MiniportHalted: NDIS has halted the miniport\r\n
0xd00000bc | MiniportPaused: NDIS has paused the miniport\r\n
0xd00000bd | MiniportRestarted: NDIS has successfully restarted (unpaused) the miniport\r\n
0xd00000be | MiniportPmInitialized: NDIS has successfully initialized the miniport adapter\r\n
0xd00000bf | Fatal error: The miniport has entered an error state due to a user request\r\n
0xd00000c0 | Fatal error: The miniport has detected an internal error\r\n
0xd00000c1 | Fatal error: The IM miniport has failed to initialize\r\n
0xd00000c2 | Fatal error: The miniport has failed to start by returning an error code from MiniportRestart\r\n
0xd00000c3 | Fatal error: The miniport has failed a power transition to operational power\r\n
0xd00000c4 | Fatal error: The miniport has failed a power transition to low power\r\n
0xd00000c5 | Network Interface deleted while PNP Device still exists. Note that this event is provided for informational purpose and might not be an error always (Eg: In case of vSwitch which was recently un-installed or a LBFO team was removed)\r\n
0xd00000c6 | The network driver did not respond to an OID request in a timely fashion\r\n
0xd00000c7 | The network driver detected that its hardware has stopped responding to commands\r\n
0xd00000c8 | The network driver requested that it be reset\r\n
0xf0000001 | DOWN_NOT_AUTHENTICATED\r\n
0xf0000002 | DOWN_NOT_MEDIA_CONNECTED\r\n
0xf0000003 | DORMANT_PAUSED\r\n
0xf0000004 | DORMANT_LOW_POWER\r\n
