## mup.sys

Path: %SystemRoot%\system32\drivers\mup.sys

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.18362.207, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000009 | UNC Hardening\r\n
0x300b000b | Unsupported Registry Value Type\r\n
0x300b000c | Invalid UNC Path\r\n
0x300b000d | Unsupported UNC Path\r\n
0x300b000e | Invalid Syntax\r\n
0x300b000f | Unsupported Property Name\r\n
0x300b0010 | Unsupported Property Value\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x7000000b | UNC Hardening Configuration\r\n
0x90000001 | Microsoft-Windows-NetworkProvider\r\n
0x90000002 | Microsoft-Windows-NetworkProvider/Operational\r\n
0xb00003e8 | Ignoring UNC Hardening Configuration Entry: Unsupported registry value type.%n%nRegistry Value Path: %2@%4%n%nRegistry Value Type: %5%n%nGuidance:%nUNC Hardening configuration only supports registry values of types REG_SZ and REG_MULTI_SZ.%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb00003e9 | Ignoring UNC Hardening Configuration Entry: Unable to parse UNC Path.%n%nUNC Path: %2%n%nUNC Hardening Configuration: %4%n%nGuidance:%nThe registry value name is not a valid UNC path.%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb00003ea | Ignoring UNC Hardening Configuration Entry: Unsupported UNC Path.%n%nUNC Path: %2%n%nUNC Hardening Configuration: %4%n%nGuidance:%nUNC Hardening is only supported at server or share granularity. If only a fraction of the resources available on a share require additional security, consider relocating contents that require additional security to a different share.%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb00003eb | Ignoring UNC Hardening Configuration Property: Unsupported property name.%n%nUNC Path: %2%n%nUNC Hardening Configuration: %4%n%nProperty Name: %6%n%nProperty Value: %7%n%nGuidance:%nThe specified property name does not match a UNC Hardening property supported on the current version of Windows and will be ignored.%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb00003ec | Ignoring UNC Hardening Configuration Property: Unsupported property name.%n%nUNC Path: %2%n%nUNC Hardening Configuration: %4%n%nProperty Name: %6%n%nProperty Value: '%8'%n%nGuidance:%nThe specified property name does not match a UNC Hardening property supported on the current version of Windows and will be ignored.%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb00003ed | Ignoring UNC Hardening Configuration Property: Unsupported property value.%n%nUNC Path: %2%n%nUNC Hardening Configuration: %4%n%nProperty Name: %6%n%nProperty Value: '%8'%n%nGuidance:%nThe specified property name expects a boolean value should be assigned a value of 0 (disabled) or 1 (enabled).%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb00003ee | Unable to parse UNC Hardening Configuration Entry: Unknown Error.%n%nUNC Path: %2%n%nUNC Hardening Configuration: %4%n%nGuidance:%nThe UNC Hardening configuration for the path contains invalid syntax and may be ignored.%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb00003ef | Unable to parse UNC Hardening Configuration Entry: Unexpected token.%n%nUNC Path: %2%n%nUNC Hardening Configuration: %4%n%nExpected Token: %5%n%nFound Token: %7%n%nGuidance: The UNC Hardening configuration for the path contains invalid syntax and may be ignored.%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb00003f0 | Unable to parse UNC Hardening Configuration Entry: Unable to parse integer.%n%nUNC Path: %2%n%nUNC Hardening Configuration: %4%n%nExpected Token: %5%n%nFound Token: %7%n%nGuidance: The UNC Hardening configuration for the path contains invalid syntax and may be ignored. The value found token was parsed as an integer, but was found to contain illegal digits.%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xb00003f1 | Unable to parse UNC Hardening Configuration Entry: Unable to parse string.%n%nUNC Path: %2%n%nUNC Hardening Configuration: %4%n%nExpected Token: %5%n%nFound Token: %7%n%nGuidance: The UNC Hardening configuration for the path contains invalid syntax and may be ignored. The value found token was parsed as an string, but was not terminated or exceeded the maximum allowable string length.%n%nFor details on configuring Windows computers to require additional security when accessing specific UNC paths, visit http://support.microsoft.com/kb/3000483.\r\n
0xd0000001 | REG_NONE\r\n
0xd0000002 | REG_SZ\r\n
0xd0000003 | REG_EXPAND_SZ\r\n
0xd0000004 | REG_BINARY\r\n
0xd0000005 | REG_DWORD\r\n
0xd0000006 | REG_MULTI_SZ\r\n
0xd0000007 | REG_QWORD\r\n
0xd0000008 | <Property>\r\n
0xd0000009 | =\r\n
0xd000000a | <Value>\r\n
0xd000000b | <Integer>\r\n
0xd000000c | <Quoted String>\r\n
0xd000000d | ,\r\n
