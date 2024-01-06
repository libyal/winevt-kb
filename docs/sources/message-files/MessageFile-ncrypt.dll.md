## ncrypt.dll

Path: %SystemRoot%\System32\ncrypt.dll

### 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x10000001 | NCrypt Operation\r\n
0x10000002 | Secret Protection\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x70000001 | Operation Failure\r\n
0x70000002 | Open Provider Failure\r\n
0x70000003 | Open Key Failure\r\n
0x70000004 | Key Creation Failure\r\n
0x90000001 | Microsoft-Windows-Crypto-NCrypt\r\n
0x90000002 | Microsoft-Windows-Crypto-NCrypt/Operational\r\n
0xb0000001 | Cryptographic Operation failed.%n%n Cryptographic Parameters:%n %tOperationType:%t%1%n %tProvider Name:%t%2%n %tKey Name:%t%3%n %tKey Type:%t%4%n %tAlgorithm Name:%t%5%n %nFailure Information:%n %tReturn Code:%t%6\r\n
0xb0000002 | Open Provider operation failed.%n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n Failure Information:%n %tReturn Code:%t%3\r\n
0xb0000003 | Open Key operation failed.%n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n %tKey Name:%t%2%n Failure Information:%n %tReturn Code:%t%3\r\n
0xb0000004 | Create Key operation failed.%n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n %tKey Name:%t%2%n %tAlgorithm Name:%t%3%n %tFlags:%t%t%4%n Failure Information:%n  %tReturn Code:%t%5\r\n
0xb0000005 | Protect Key operation failed.%n%n Cryptographic Parameters:%n %tProtector Name:%t%1%n %tProtector Attributes:%n%t%t%t%2%n %tFlags:%t%t%3%n Failure Information:%n %tReturn Code:%t%4\r\n
0xb0000006 | Unprotect Key operation failed.%n%n Cryptographic Parameters:%n %tProtector Name:%t%1%n %tRecipient Type:%t%2%n %tFlags:%t%t%3%n Failure Information:%n %tReturn Code:%t%4\r\n
0xb0000007 | Protect Secret operation failed.%n%n Cryptographic Parameters:%n %tFlags:%t%t%1%n Failure Information:%n %tReturn Code:%t%2\r\n
0xb0000008 | Unprotect Secret operation failed.%n%n Cryptographic Parameters:%n %tFlags:%t%t%1%n Failure Information:%n %tReturn Code:%t%2\r\n
0xd0000001 | KEY TRANSPORT\r\n
0xd0000002 | KEY AGREEMENT\r\n
0xd0000003 | SYMMETRIC KEY ENCRYPTION\r\n
0xd0000004 | PASSWORD ENCRYPTION\r\n
0xd0000005 | OTHER\r\n
0xd0000006 | SUCCESS\r\n
0xd0000007 | FAILURE\r\n
0xd0000008 | CREATE KEY\r\n
0xd0000009 | OPEN KEY\r\n
0xd000000a | DELETE KEY\r\n
0xd000000b | ENCRYPT\r\n
0xd000000c | DECRYPT\r\n
0xd000000d | SIGN HASH\r\n
0xd000000e | VERIFY SIGNATURE\r\n
0xd000000f | SECRET AGREEMENT\r\n
0xd0000010 | DERIVE KEY\r\n
0xd0000011 | KEY DERIVATION\r\n
0xd0000012 | KEY FINALIZE\r\n
0xd0000013 | EXPORT KEY\r\n
0xd0000014 | IMPORT KEY\r\n

### 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000001 | NCrypt Operation\r\n
0x10000002 | Secret Protection\r\n
0x10000003 | BCrypt ISO Operation keyword failure\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000005 | Verbose\r\n
0x70000001 | Operation Failure\r\n
0x70000002 | Open Provider Failure\r\n
0x70000003 | Open Key Failure\r\n
0x70000004 | Key Creation Failure\r\n
0x70000009 | Key write succeeded\r\n
0x7000000a | Key write failed\r\n
0x7000000b | Delete key succeeded\r\n
0x7000000c | Delete key failed\r\n
0x7000000d | BCrypt ISO Operation task failure\r\n
0x90000001 | Microsoft-Windows-Crypto-NCrypt\r\n
0x90000002 | Microsoft-Windows-Crypto-NCrypt/Operational\r\n
0xb0000001 | Cryptographic Operation failed.%n%n Cryptographic Parameters:%n %tOperationType:%t%1%n %tProvider Name:%t%2%n %tKey Name:%t%3%n %tKey Type:%t%4%n %tAlgorithm Name:%t%5%n %nFailure Information:%n %tReturn Code:%t%6\r\n
0xb0000002 | Open Provider operation failed.%n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n Failure Information:%n %tReturn Code:%t%3\r\n
0xb0000003 | Open Key operation failed.%n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n %tKey Name:%t%2%n Failure Information:%n %tReturn Code:%t%3\r\n
0xb0000004 | Create Key operation failed.%n%n Cryptographic Parameters:%n %tProvider Name:%t%1%n %tKey Name:%t%2%n %tAlgorithm Name:%t%3%n %tFlags:%t%t%4%n Failure Information:%n  %tReturn Code:%t%5\r\n
0xb0000005 | Protect Key operation failed.%n%n Cryptographic Parameters:%n %tProtector Name:%t%1%n %tProtector Attributes:%n%t%t%t%2%n %tFlags:%t%t%3%n Failure Information:%n %tReturn Code:%t%4\r\n
0xb0000006 | Unprotect Key operation failed.%n%n Cryptographic Parameters:%n %tProtector Name:%t%1%n %tRecipient Type:%t%2%n %tFlags:%t%t%3%n Failure Information:%n %tReturn Code:%t%4\r\n
0xb0000007 | Protect Secret operation failed.%n%n Cryptographic Parameters:%n %tFlags:%t%t%1%n Failure Information:%n %tReturn Code:%t%2\r\n
0xb0000008 | Unprotect Secret operation failed.%n%n Cryptographic Parameters:%n %tFlags:%t%t%1%n Failure Information:%n %tReturn Code:%t%2\r\n
0xb0000009 | Key write succeeded.%n%n Provider Name:%t%1%n ModificationType: %t%t%2%n Flags:%t%t%3%n Key Name:%t%4%n Key File Name:%t%5%n ProcessName:%t%6%n ProcessId:%t%7%n ServerThreadId:%t%8%n UserId:%t%9%n ServiceTag:%t%10%n Return Code:%t%11\r\n
0xb000000a | Key write failed.%n%n Provider Name:%t%1%n ModificationType: %t%t%2%n Flags:%t%t%3%n Key Name:%t%4%n Key File Name:%t%5%n ProcessName:%t%6%n ProcessId:%t%7%n ServerThreadId:%t%8%n UserId:%t%9%n ServiceTag:%t%10%n Return Code:%t%11\r\n
0xb000000b | Delete key succeeded.%n%n Provider Name:%t%1%n Flags:%t%t%2%n DeletionType: %t%t%3%n Key Name:%t%4%n Key File Name:%t%5%n ProcessName:%t%6%n ProcessId:%t%7%n ServerThreadId:%t%8%n UserId:%t%9%n ServiceTag:%t%10%n Return Code:%t%11\r\n
0xb000000c | Delete key failed.%n%n Provider Name:%t%1%n Flags:%t%t%2%n DeletionType: %t%t%3%n Key Name:%t%4%n Key File Name:%t%5%n ProcessName:%t%6%n ProcessId:%t%7%n ServerThreadId:%t%8%n UserId:%t%9%n ServiceTag:%t%10%n Return Code:%t%11\r\n
0xb000000d | BCrypt ISO operation failed%nFunction: %1%nInfo: %2%nStatus: %3. %4\r\n
0xd0000001 | KEY TRANSPORT\r\n
0xd0000002 | KEY AGREEMENT\r\n
0xd0000003 | SYMMETRIC KEY ENCRYPTION\r\n
0xd0000004 | PASSWORD ENCRYPTION\r\n
0xd0000005 | OTHER\r\n
0xd0000006 | SUCCESS\r\n
0xd0000007 | FAILURE\r\n
0xd0000008 | CREATE KEY\r\n
0xd0000009 | OPEN KEY\r\n
0xd000000a | DELETE KEY\r\n
0xd000000b | ENCRYPT\r\n
0xd000000c | DECRYPT\r\n
0xd000000d | SIGN HASH\r\n
0xd000000e | VERIFY SIGNATURE\r\n
0xd000000f | SECRET AGREEMENT\r\n
0xd0000010 | DERIVE KEY\r\n
0xd0000011 | KEY DERIVATION\r\n
0xd0000012 | KEY FINALIZE\r\n
0xd0000013 | EXPORT KEY\r\n
0xd0000014 | IMPORT KEY\r\n
