## netsetupsvc.dll

Path: %SystemRoot%\system32\NetSetupSvc.dll

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Run service\r\n
0x70000002 | Transaction\r\n
0x70000003 | External API\r\n
0x70000004 | Plugin callback\r\n
0x70000005 | Calculate bindings\r\n
0x70000006 | Commit changes\r\n
0x70000007 | Operation\r\n
0x70000008 | INetCfg API\r\n
0x70000009 | INetCfg Notify Object\r\n
0x90000001 | Microsoft-Windows-Network-Setup\r\n
0x90000002 | Microsoft-Windows-Network-Setup/Diagnostic\r\n
0xb0000064 | The Network Setup service is starting\r\n
0xb0000065 | The Network Setup service has started\r\n
0xb0000066 | The Network Setup service failed to start with error %1\r\n
0xb000006e | The Network Setup service will stop due to inactivity\r\n
0xb000006f | The Network Setup service will stop due to a user request\r\n
0xb0000070 | The Network Setup service is stopping\r\n
0xb0000071 | The Network Setup service has stopped\r\n
0xb00000c8 | A new transaction has started\r\n
0xb00000c9 | A transaction has been closed\r\n
0xb00000ca | Network Setup has begun calculating new driver bindings\r\n
0xb00000cb | Network Setup has finished calculating new driver bindings\r\n
0xb00000cc | Network Setup has begun committing changes to the registry\r\n
0xb00000cd | Network Setup has finished committing changes to the registry\r\n
0xb000012c | Begin API %2 on transaction %1\r\n
0xb000012d | End API %2 on transaction %1\r\n
0xb0000190 | Begin calling into plugin %3\r\n
0xb0000191 | End calling into plugin\r\n
0xb00001f4 | Begin operation %2 on %3 in transaction %1: %4 on %5:%6\r\n
0xb00001f5 | Operation %1 ended with code %2\r\n
0xb0000258 | Begin API %1\r\n
0xb0000259 | End API with status code %1\r\n
0xb00002bc | Invoking API %2 on Notify Object for %1\r\n
0xb00002bd | The Notify Object returned with status: %1\r\n
0xb00002be | An error occurred while invoking the Notify Object.  The call was aborted with status: %1.\r\n
0xd0000001 | NetSetupInitialize\r\n
0xd0000002 | NetSetupRollback\r\n
0xd0000003 | NetSetupCommit\r\n
0xd0000004 | NetSetupClose\r\n
0xd0000005 | NetSetupCreateObject\r\n
0xd0000006 | NetSetupDeleteObject\r\n
0xd0000007 | NetSetupGetObjectPropertyKeys\r\n
0xd0000008 | NetSetupGetObjectProperties\r\n
0xd0000009 | NetSetupFreeObjectProperties\r\n
0xd000000a | NetSetupSetObjectProperties\r\n
0xd000000b | NetSetupGetObjects\r\n
0xd000000c | NetSetupFreeObjects\r\n
0xd000000d | NetSetupValidateTransaction\r\n
0xd000000e | TransactionEventSink::OnInitialize\r\n
0xd000000f | TransactionEventSink::OnPrepareTransaction\r\n
0xd0000010 | TransactionEventSink::OnCommitTransaction\r\n
0xd0000011 | TransactionEventSink::OnRollbackTransaction\r\n
0xd0000012 | TransactionEventSink::OnValidateTransaction\r\n
0xd0000013 | PolicyProvider::OnCreateObject\r\n
0xd0000014 | PolicyProvider::OnModifyObject\r\n
0xd0000015 | ObjectEventSink::OnCreateObject\r\n
0xd0000016 | ObjectEventSink::OnModifyObject\r\n
0xd0000017 | ObjectEventSink::OnDeleteObject\r\n
0xd0000018 | BindController::OnBindPathAdded\r\n
0xd0000019 | BindPathEventSink::OnCreateBindPath\r\n
0xd000001a | BindPathEventSink::OnDeleteBindPath\r\n
0xd000001b | BindPathEventSink::OnEnableBindPath\r\n
0xd000001c | BindPathEventSink::OnDisableBindPath\r\n
0xd000001d | ObjectProvider::LoadAllObjects\r\n
0xd000001e | Initialize transaction\r\n
0xd000001f | Prepare transaction\r\n
0xd0000020 | Commit transaction\r\n
0xd0000021 | Rollback transaction\r\n
0xd0000022 | Validate transaction\r\n
0xd0000023 | Create object\r\n
0xd0000024 | Delete object\r\n
0xd0000025 | Modify object\r\n
0xd0000026 | the system-wide store\r\n
0xd0000027 | network interface\r\n
0xd0000028 | NDIS light-weight filter driver\r\n
0xd0000029 | NDIS protocol driver\r\n
0xd000002a | TDI network service driver\r\n
0xd000002b | TDI network client driver\r\n
0xd000002c | network binding path\r\n
0xd000002d | Mux\r\n
0xd000002e | netsetup transaction\r\n
0xd000002f | reflected property\r\n
0xd0000030 | network binding rule\r\n
0xd0000031 | INetCfg::Initialize\r\n
0xd0000032 | INetCfg::Uninitialize\r\n
0xd0000033 | INetCfg::Apply\r\n
0xd0000034 | INetCfg::Cancel\r\n
0xd0000035 | INetCfg::EnumComponents\r\n
0xd0000036 | INetCfg::FindComponent\r\n
0xd0000037 | INetCfg::QueryNetCfgClass\r\n
0xd0000038 | INetCfgLock::AcquireWriteLock\r\n
0xd0000039 | INetCfgLock::ReleaseWriteLock\r\n
0xd000003a | INetCfgLock::IsWriteLocked\r\n
0xd000003b | INetCfgBindingInterface::GetName\r\n
0xd000003c | INetCfgBindingInterface::GetUpperComponent\r\n
0xd000003d | INetCfgBindingInterface::GetLowerComponent\r\n
0xd000003e | INetCfgBindingPath::IsSamePathAs\r\n
0xd000003f | INetCfgBindingPath::IsSubPathOf\r\n
0xd0000040 | INetCfgBindingPath::IsEnabled\r\n
0xd0000041 | INetCfgBindingPath::Enable\r\n
0xd0000042 | INetCfgBindingPath::GetPathToken\r\n
0xd0000043 | INetCfgBindingPath::GetOwner\r\n
0xd0000044 | INetCfgBindingPath::GetDepth\r\n
0xd0000045 | INetCfgBindingPath::EnumBindingInterfaces\r\n
0xd0000046 | INetCfgClass::FindComponent\r\n
0xd0000047 | INetCfgClass::EnumComponents\r\n
0xd0000048 | INetCfgClassSetup::SelectAndInstall\r\n
0xd0000049 | INetCfgClassSetup::Install\r\n
0xd000004a | INetCfgClassSetup::DeInstall\r\n
0xd000004b | INetCfgClassSetup2::UpdateNonEnumeratedComponent\r\n
0xd000004c | INetCfgComponent::GetDisplayName\r\n
0xd000004d | INetCfgComponent::SetDisplayName\r\n
0xd000004e | INetCfgComponent::GetHelpText\r\n
0xd000004f | INetCfgComponent::GetId\r\n
0xd0000050 | INetCfgComponent::GetCharacteristics\r\n
0xd0000051 | INetCfgComponent::GetInstanceGuid\r\n
0xd0000052 | INetCfgComponent::GetPnpDevNodeId\r\n
0xd0000053 | INetCfgComponent::GetClassGuid\r\n
0xd0000054 | INetCfgComponent::GetBindName\r\n
0xd0000055 | INetCfgComponent::GetDeviceStatus\r\n
0xd0000056 | INetCfgComponent::OpenParamKey\r\n
0xd0000057 | INetCfgComponent::RaisePropertyUi\r\n
0xd0000058 | INetCfgComponentBindings::BindTo\r\n
0xd0000059 | INetCfgComponentBindings::UnbindFrom\r\n
0xd000005a | INetCfgComponentBindings::SupportsBindingInterface\r\n
0xd000005b | INetCfgComponentBindings::IsBoundTo\r\n
0xd000005c | INetCfgComponentBindings::IsBindableTo\r\n
0xd000005d | INetCfgComponentBindings::EnumBindingPaths\r\n
0xd000005e | INetCfgComponentBindings::MoveBefore\r\n
0xd000005f | INetCfgComponentBindings::MoveAfter\r\n
0xd0000060 | INetCfgSysPrep::HrSetupSetFirstDword\r\n
0xd0000061 | INetCfgSysPrep::HrSetupSetFirstString\r\n
0xd0000062 | INetCfgSysPrep::HrSetupSetFirstStringAsBool\r\n
0xd0000063 | INetCfgSysPrep::HrSetupSetFirstMultiSzField\r\n
0xd0000064 | IEnumNetCfgBindingInterface::Next\r\n
0xd0000065 | IEnumNetCfgBindingInterface::Skip\r\n
0xd0000066 | IEnumNetCfgBindingInterface::Reset\r\n
0xd0000067 | IEnumNetCfgBindingInterface::Clone\r\n
0xd0000068 | IEnumNetCfgBindingPath::Next\r\n
0xd0000069 | IEnumNetCfgBindingPath::Skip\r\n
0xd000006a | IEnumNetCfgBindingPath::Reset\r\n
0xd000006b | IEnumNetCfgBindingPath::Clone\r\n
0xd000006c | IEnumNetCfgComponent::Next\r\n
0xd000006d | IEnumNetCfgComponent::Skip\r\n
0xd000006e | IEnumNetCfgComponent::Reset\r\n
0xd000006f | IEnumNetCfgComponent::Clone\r\n
0xd0000070 | INetCfgPnpReconfigCallback::SendPnpReconfig\r\n
0xd0000071 | INetCfgClassSetupDirect::InstallDirect\r\n
0xd0000072 | INetCfgInternalSetup::BeginBatchOperation\r\n
0xd0000073 | INetCfgInternalSetup::CommitBatchOperation\r\n
0xd0000074 | INetCfgInternalSetup::SelectWithFilterAndInstall\r\n
0xd0000075 | INetCfgInternalSetup::EnumeratedComponentInstalled\r\n
0xd0000076 | INetCfgInternalSetup::EnumeratedComponentUpdated\r\n
0xd0000077 | INetCfgInternalSetup::UpdateNonEnumeratedComponent\r\n
0xd0000078 | INetCfgInternalSetup::EnumeratedComponentRemoved\r\n
0xd0000079 | INetCfgSpecialCase::GetAdapterOrder\r\n
0xd000007a | INetCfgSpecialCase::SetAdapterOrder\r\n
0xd000007b | INetCfgSpecialCase::GetWanAdaptersFirst\r\n
0xd000007c | INetCfgSpecialCase::SetWanAdaptersFirst\r\n
0xd000007d | DllRegisterServer\r\n
0xd000007e | DllUnregisterServer\r\n
0xd000007f | WSHGetWinsockMapping\r\n
0xd0000080 | IUnknown::QueryInterface\r\n
0xd0000081 | INetCfgComponentControl::Initialize\r\n
0xd0000082 | INetCfgComponentControl::ApplyRegistryChanges\r\n
0xd0000083 | INetCfgComponentControl::ApplyPnpChanges\r\n
0xd0000084 | INetCfgComponentControl::CancelChanges\r\n
0xd0000085 | INetCfgComponentSetup::Install\r\n
0xd0000086 | INetCfgComponentSetup::Upgrade\r\n
0xd0000087 | INetCfgComponentSetup::ReadAnswerFile\r\n
0xd0000088 | INetCfgComponentSetup::Removing\r\n
0xd0000089 | INetCfgComponentPropertyUi::QueryPropertyUi\r\n
0xd000008a | INetCfgComponentPropertyUi::SetContext\r\n
0xd000008b | INetCfgComponentPropertyUi::MergePropPages\r\n
0xd000008c | INetCfgComponentPropertyUi::ValidateProperties\r\n
0xd000008d | INetCfgComponentPropertyUi::ApplyProperties\r\n
0xd000008e | INetCfgComponentPropertyUi::CancelProperties\r\n
0xd000008f | INetCfgComponentNotifyBinding::QueryBindingPath\r\n
0xd0000090 | INetCfgComponentNotifyBinding::NotifyBindingPath\r\n
0xd0000091 | INetCfgComponentNotifyGlobal::GetSupportedNotifications\r\n
0xd0000092 | INetCfgComponentNotifyGlobal::SysQueryBindingPath\r\n
0xd0000093 | INetCfgComponentNotifyGlobal::SysNotifyBindingPath\r\n
0xd0000094 | INetCfgComponentNotifyGlobal::SysNotifyComponent\r\n
