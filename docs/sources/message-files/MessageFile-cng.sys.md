## cng.sys

Path: %SystemRoot%\System32\drivers\cng.sys

### 6.1.7600.16385, 6.1.7601.17725

Message identifier | Message string
--- | ---
0x10000001 | Source registration\r\n
0x10000002 | Entropy data flow\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x7000000a | Gather entropy for the system random number generator\r\n
0x90000001 | Microsoft-Windows-Crypto-RNG\r\n
0x90000002 | Microsoft-Windows-Crypto-RNG/Analytic\r\n
0xb0000001 | An entropy source was registered.%n%tSource%t%1%n%tName%t%2%n%tType%t%3\r\n
0xb0000002 | Entropy source %1 (%2) was unregistered.\r\n
0xb0000003 | Entropy source %1 provided %2 bytes with %3 millibits of entropy\r\n
0xb0000010 | TPM boot time entropy gathering results:%n%tPolicy%t%1%n%tCode%t%2%n%tStatus%t%3%n%tTime%t%4%n%tBytes%t%5\r\n
0xd0000001 | High entropy push\r\n
0xd0000002 | Default\r\n
0xd0000003 | ForceDisable\r\n
0xd0000004 | ForceEnable\r\n
0xd0000005 | ERROR (uninitialized)\r\n
0xd0000006 | Disabled by policy\r\n
0xd0000007 | No TPM found\r\n
0xd0000008 | TPM error\r\n
0xd0000009 | Success\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x10000001 | Source registration\r\n
0x10000002 | Entropy data flow\r\n
0x10000003 | PRNG\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x51000002 | Error\r\n
0x7000000a | Gather entropy for the system random number generator\r\n
0x70000014 | Prng\r\n
0x90000001 | Microsoft-Windows-Crypto-RNG\r\n
0x90000002 | Microsoft-Windows-Crypto-RNG/Analytic\r\n
0x91000001 | Microsoft-Windows-Crypto-CNG\r\n
0x91000002 | Microsoft-Windows-Crypto-CNG/Analytic\r\n
0xb0000001 | An entropy source was registered.%n%tSource%t%1%n%tName%t%2%n%tType%t%3\r\n
0xb0000002 | Entropy source %1 (%2) was unregistered.\r\n
0xb0000003 | Entropy source %1 provided %2 bytes with %3 millibits of entropy%nData%t%5\r\n
0xb0000004 | Callback to source %1 returned status %2, taking time %3\r\n
0xb0000010 | Boot entropy result:%n%tSource%t%1%n%tPolicy%t%2%n%tCode%t%3%n%tStatus%t%4%n%tTime%t%5%n%tBytesProvided%t%6%n%tBytes%t%8\r\n
0xb0000020 | Pool reseed:%n%tCount%t%1%n%tType%t%2%n%tData%t%4\r\n
0xb0000021 | Pool add:%n%tPool%t%1%n%tData%t%3\r\n
0xb0000030 | Prng (re)seed:%nAddr%t%1%nData%t%3\r\n
0xb0000031 | Prng output:%n%tAddr%t%1%n%tBytes%t%2%n%tData%t%4\r\n
0xb1000001 | Open Provider Failure. %n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n %tAlgorithm Name:%t%2%n %tFlags:%t%3%n Failure Information:%n %tReturn Code:%t%4%n %tFailure Type:%t%5\r\n
0xd0000001 | High entropy push\r\n
0xd0000002 | Low entropy push\r\n
0xd0000003 | High entropy pull\r\n
0xd0000004 | Default\r\n
0xd0000005 | ForceDisable\r\n
0xd0000006 | ForceEnable\r\n
0xd0000007 | ERROR (uninitialized)\r\n
0xd0000008 | Disabled by policy\r\n
0xd0000009 | Source not found\r\n
0xd000000a | Source error\r\n
0xd000000b | Success\r\n
0xd000000c | Unknown\r\n
0xd000000d | Seed File\r\n
0xd000000e | External\r\n
0xd000000f | TPM\r\n
0xd0000010 | RDRAND\r\n
0xd0000011 | Time\r\n
0xd0000012 | Acpi-OEM0\r\n
0xd0000013 | UEFI\r\n
0xd0000014 | One pool\r\n
0xd0000015 | One or more pools\r\n
0xd0000016 | All pools\r\n
0xd1000001 | Failed to resolve the provider.\r\n
0xd1000002 | Failed to load the provider.\r\n
0xd1000003 | Provider did not pass basic validation.\r\n
0xd1000004 | Failed to open the Provider.\r\n

### 6.3.9600.16384, 6.3.9600.18581, 10.0.10586.0, 10.0.14393.0, 10.0.14393.82, 10.0.15063.0, 10.0.16299.15, 10.0.17134.765

Message identifier | Message string
--- | ---
0x10000001 | Source registration\r\n
0x10000002 | Entropy data flow\r\n
0x10000003 | PRNG\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x51000002 | Error\r\n
0x7000000a | Gather entropy for the system random number generator\r\n
0x70000014 | Prng\r\n
0x90000001 | Microsoft-Windows-Crypto-RNG\r\n
0x90000002 | Microsoft-Windows-Crypto-RNG/Analytic\r\n
0x91000001 | Microsoft-Windows-Crypto-CNG\r\n
0x91000002 | Microsoft-Windows-Crypto-CNG/Analytic\r\n
0xb0000001 | An entropy source was registered.%n%tSource%t%1%n%tName%t%2%n%tType%t%3\r\n
0xb0000002 | Entropy source %1 (%2) was unregistered.\r\n
0xb0000003 | Entropy source %1 provided %2 bytes with %3 millibits of entropy%nData%t%5\r\n
0xb0000004 | Callback to source %1 returned status %2, taking time %3\r\n
0xb0000010 | Boot entropy result:%n%tSource%t%1%n%tPolicy%t%2%n%tCode%t%3%n%tStatus%t%4%n%tTime%t%5%n%tBytesProvided%t%6%n%tBytes%t%8\r\n
0xb0000020 | Pool reseed:%n%tCount%t%1%n%tType%t%2%n%tData%t%4\r\n
0xb0000021 | Pool add:%n%tPool%t%1%n%tData%t%3\r\n
0xb0000030 | Prng (re)seed:%nAddr%t%1%nData%t%3\r\n
0xb0000031 | Prng output:%n%tAddr%t%1%n%tBytes%t%2%n%tData%t%4\r\n
0xb1000001 | Open Provider Failure. %n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n %tAlgorithm Name:%t%2%n %tFlags:%t%3%n Failure Information:%n %tReturn Code:%t%4%n %tFailure Type:%t%5\r\n
0xd0000001 | High entropy push\r\n
0xd0000002 | Low entropy push\r\n
0xd0000003 | High entropy pull\r\n
0xd0000004 | Default\r\n
0xd0000005 | ForceDisable\r\n
0xd0000006 | ForceEnable\r\n
0xd0000007 | ERROR (uninitialized)\r\n
0xd0000008 | Disabled by policy\r\n
0xd0000009 | Source not found\r\n
0xd000000a | Source error\r\n
0xd000000b | Success\r\n
0xd000000c | Unknown\r\n
0xd000000d | Seed File\r\n
0xd000000e | External\r\n
0xd000000f | TPM\r\n
0xd0000010 | RDRAND\r\n
0xd0000011 | Time\r\n
0xd0000012 | Acpi-OEM0\r\n
0xd0000013 | UEFI\r\n
0xd0000014 | CNG\r\n
0xd0000015 | One pool\r\n
0xd0000016 | One or more pools\r\n
0xd0000017 | All pools\r\n
0xd1000001 | Failed to resolve the provider.\r\n
0xd1000002 | Failed to load the provider.\r\n
0xd1000003 | Provider did not pass basic validation.\r\n
0xd1000004 | Failed to open the Provider.\r\n

### 10.0.17763.1, 10.0.17763.557, 10.0.18362.1, 10.0.18362.836, 10.0.19041.1, 10.0.19041.630

Message identifier | Message string
--- | ---
0x10000001 | Source registration\r\n
0x10000002 | Entropy data flow\r\n
0x10000003 | PRNG\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x51000002 | Error\r\n
0x7000000a | Gather entropy for the system random number generator\r\n
0x70000014 | Prng\r\n
0x90000001 | Microsoft-Windows-Crypto-RNG\r\n
0x90000002 | Microsoft-Windows-Crypto-RNG/Analytic\r\n
0x91000001 | Microsoft-Windows-Crypto-CNG\r\n
0x91000002 | Microsoft-Windows-Crypto-CNG/Analytic\r\n
0xb0000001 | An entropy source was registered.%n%tSource%t%1%n%tName%t%2%n%tType%t%3\r\n
0xb0000002 | Entropy source %1 (%2) was unregistered.\r\n
0xb0000003 | Entropy source %1 provided %2 bytes with %3 millibits of entropy%nData%t%5\r\n
0xb0000004 | Callback to source %1 returned status %2, taking time %3\r\n
0xb0000010 | Boot entropy result:%n%tSource%t%1%n%tPolicy%t%2%n%tCode%t%3%n%tStatus%t%4%n%tTime%t%5%n%tBytesProvided%t%6%n%tBytes%t%8\r\n
0xb0000020 | Pool reseed:%n%tCount%t%1%n%tType%t%2%n%tData%t%4\r\n
0xb0000021 | Pool add:%n%tPool%t%1%n%tData%t%3\r\n
0xb0000030 | Prng (re)seed:%nAddr%t%1%nData%t%3\r\n
0xb0000031 | Prng output:%n%tAddr%t%1%n%tBytes%t%2%n%tData%t%4\r\n
0xb1000001 | Open Provider Failure. %n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n %tAlgorithm Name:%t%2%n %tFlags:%t%3%n Failure Information:%n %tReturn Code:%t%4%n %tFailure Type:%t%5\r\n
0xd0000001 | High entropy push\r\n
0xd0000002 | Low entropy push\r\n
0xd0000003 | High entropy pull\r\n
0xd0000004 | Default\r\n
0xd0000005 | ForceDisable\r\n
0xd0000006 | ForceEnable\r\n
0xd0000007 | ERROR (uninitialized)\r\n
0xd0000008 | Disabled by policy\r\n
0xd0000009 | Source not found\r\n
0xd000000a | Source error\r\n
0xd000000b | Success\r\n
0xd000000c | Unknown\r\n
0xd000000d | Seed File\r\n
0xd000000e | External\r\n
0xd000000f | TPM\r\n
0xd0000010 | RDRAND\r\n
0xd0000011 | Time\r\n
0xd0000012 | Acpi-OEM0\r\n
0xd0000013 | UEFI\r\n
0xd0000014 | CNG\r\n
0xd0000015 | TCB-TPM\r\n
0xd0000016 | TCB-RDRAND\r\n
0xd0000017 | One pool\r\n
0xd0000018 | One or more pools\r\n
0xd0000019 | All pools\r\n
0xd1000001 | Failed to resolve the provider.\r\n
0xd1000002 | Failed to load the provider.\r\n
0xd1000003 | Provider did not pass basic validation.\r\n
0xd1000004 | Failed to open the Provider.\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000001 | Source registration\r\n
0x10000002 | Entropy data flow\r\n
0x10000003 | PRNG\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000004 | Information\r\n
0x51000002 | Error\r\n
0x7000000a | Gather entropy for the system random number generator\r\n
0x70000014 | Prng\r\n
0x90000001 | Microsoft-Windows-Crypto-RNG\r\n
0x90000002 | Microsoft-Windows-Crypto-RNG/Analytic\r\n
0x91000001 | Microsoft-Windows-Crypto-CNG\r\n
0x91000002 | Microsoft-Windows-Crypto-CNG/Analytic\r\n
0xb0000001 | An entropy source was registered.%n%tSource%t%1%n%tName%t%2%n%tType%t%3\r\n
0xb0000002 | Entropy source %1 (%2) was unregistered.\r\n
0xb0000003 | Entropy source %1 provided %2 bytes with %3 millibits of entropy%nData%t%5\r\n
0xb0000004 | Callback to source %1 returned status %2, taking time %3\r\n
0xb0000010 | Boot entropy result:%n%tSource%t%1%n%tPolicy%t%2%n%tCode%t%3%n%tStatus%t%4%n%tTime%t%5%n%tBytesProvided%t%6%n%tBytes%t%8\r\n
0xb0000020 | Pool reseed:%n%tCount%t%1%n%tType%t%2%n%tData%t%4\r\n
0xb0000021 | Pool add:%n%tPool%t%1%n%tData%t%3\r\n
0xb0000030 | Prng (re)seed:%nAddr%t%1%nData%t%3\r\n
0xb0000031 | Prng output:%n%tAddr%t%1%n%tBytes%t%2%n%tData%t%4\r\n
0xb0000032 | New process created. Old Prng states under this proces ID are no longer valid\r\n
0xb1000001 | Open Provider Failure. %n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n %tAlgorithm Name:%t%2%n %tFlags:%t%3%n Failure Information:%n %tReturn Code:%t%4%n %tFailure Type:%t%5\r\n
0xd0000001 | High entropy push\r\n
0xd0000002 | Low entropy push\r\n
0xd0000003 | High entropy pull\r\n
0xd0000004 | Default\r\n
0xd0000005 | ForceDisable\r\n
0xd0000006 | ForceEnable\r\n
0xd0000007 | ERROR (uninitialized)\r\n
0xd0000008 | Disabled by policy\r\n
0xd0000009 | Source not found\r\n
0xd000000a | Source error\r\n
0xd000000b | Success\r\n
0xd000000c | Unknown\r\n
0xd000000d | Seed File\r\n
0xd000000e | External\r\n
0xd000000f | TPM\r\n
0xd0000010 | RDRAND\r\n
0xd0000011 | Time\r\n
0xd0000012 | Acpi-OEM0\r\n
0xd0000013 | UEFI\r\n
0xd0000014 | CNG\r\n
0xd0000015 | TCB-TPM\r\n
0xd0000016 | TCB-RDRAND\r\n
0xd0000017 | One pool\r\n
0xd0000018 | One or more pools\r\n
0xd0000019 | All pools\r\n
0xd1000001 | Failed to resolve the provider.\r\n
0xd1000002 | Failed to load the provider.\r\n
0xd1000003 | Provider did not pass basic validation.\r\n
0xd1000004 | Failed to open the Provider.\r\n
