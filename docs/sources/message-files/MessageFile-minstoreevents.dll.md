## minstoreevents.dll

Path: %SystemRoot%\System32\minstoreevents.dll

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x3000000d | Bucket Split\r\n
0x3000000e | Bucket Merge\r\n
0x3000000f | Write B+ tree\r\n
0x30000010 | Checkpoint\r\n
0x30000011 | LFF: Redo Log\r\n
0x30000012 | LFF: Protected Space\r\n
0x30000013 | Allocation range\r\n
0x30000014 | Started writing B+ tree\r\n
0x30000015 | Finished writing B+ tree\r\n
0x30000016 | Log tail advance\r\n
0x30000017 | Log Redo\r\n
0x30000018 | Log pulse lazy writer\r\n
0x30000019 | Container move\r\n
0x30000032 | Bucket read collision\r\n
0x30000033 | Bucket lock collision\r\n
0x30000034 | Bucket cow collision\r\n
0x30000064 | B+ node CRC mismatch\r\n
0x30000065 | B+ node repaired via redundant copy\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Minstore Event Provider\r\n
0x90000002 | Minstore Analytic Channel\r\n
0x90000003 | Minstore Debug Channel\r\n
0xb0010001 | Bucket split\r\n
0xb0010002 | Bucket merge\r\n
0xb001000a | Tree update\r\n
0xb001000b | Tree update\r\n
0xb001000c | Start tree update\r\n
0xb001000d | End tree update\r\n
0xb0010014 | LFF: Redo log\r\n
0xb0010015 | LFF: Protected space\r\n
0xb0010016 | Allocation range:%n%tMetadata allocation: %1 %n%tRequested tier: %2, actual tier: %3 %n%tRequested allocation start: %4, count: %5 %n%tActual allocation start: %6, count: %7\r\n
0xb0010017 | Log tail advance from %3 to %4.%nLog is %2 percent full.\r\n
0xb0010018 | Log pulse lazy writer. Log is %2 percent full.\r\n
0xb0010019 | Container move:%n%tSource tier: %1, Target tier: %2 %n%tSource start of range: %3, count: %4 %n%t Target physical offset: %5 %n%tSSD Fill Ratio %6, HDD Fill Ratio %7 %n%tReserved: %8%n%tDestaged allocation count: %9%n%tFailed SSD Destage: %10\r\n
0xb0010032 | Two threads tried to read bucket %1 (table %2) for level %0 simultaneously.\r\n
0xb0010033 | A thread had to wait to lock bucket %1 (table %2) for level %0.\r\n
0xb0010034 | A thread had to wait for a copy of bucket %1 (table %2) for level %0 to finish.\r\n
0xb0010064 | B+ node CRC mismatch\r\n
0xb0010065 | B+ node repaired via redundant copy\r\n
0xb00203e8 | B+ tree node started splitting\r\n
0xb00203ea | B+ tree node finished splitting\r\n
0xb00203eb | B+ tree nodes started merging\r\n
0xb00203ec | B+ tree nodes finished merging\r\n
0xb00203ed | B+ tree starting pushing its root\r\n
0xb00203ee | B+ tree finished pushing its root\r\n
0xb00203ef | B+ tree starting popping its root\r\n
0xb00203f0 | B+ tree finished popping its root\r\n
0xb00203f3 | Analyze pass start\r\n
0xb00203f4 | Analyze pass end\r\n
0xb00203f5 | Redo pass start\r\n
0xb00203f6 | Redo pass end\r\n
0xb00203f7 | Flush And Checkpoint start\r\n
0xb00203f8 | Flush And Checkpoint end\r\n
0xb00203f9 | First redo transaction found\r\n
0xb00203fa | Tree Update Record found\r\n
0xb00203fb | Open Table for redo\r\n
0xb00203fc | Reserve ranges for redo\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x3000000d | Bucket Split\r\n
0x3000000e | Bucket Merge\r\n
0x3000000f | Write B+ tree\r\n
0x30000010 | Checkpoint\r\n
0x30000011 | LFF: Redo Log\r\n
0x30000012 | LFF: Protected Space\r\n
0x30000013 | Allocation range\r\n
0x30000014 | Started writing B+ tree\r\n
0x30000015 | Finished writing B+ tree\r\n
0x30000016 | Log tail advance\r\n
0x30000017 | Log Redo\r\n
0x30000018 | Log pulse lazy writer\r\n
0x30000019 | Container move\r\n
0x3000001a | Log skip replay\r\n
0x3000001b | Log replay failure\r\n
0x30000032 | Bucket read collision\r\n
0x30000033 | Bucket lock collision\r\n
0x30000034 | Bucket cow collision\r\n
0x30000064 | B+ node CRC mismatch\r\n
0x30000065 | B+ node repaired via redundant copy\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Minstore Event Provider\r\n
0x90000002 | Minstore Analytic Channel\r\n
0x90000003 | Minstore Debug Channel\r\n
0xb0010001 | Bucket split\r\n
0xb0010002 | Bucket merge\r\n
0xb001000a | Tree update\r\n
0xb001000b | Tree update\r\n
0xb001000c | Start tree update\r\n
0xb001000d | End tree update\r\n
0xb0010014 | LFF: Redo log\r\n
0xb0010015 | LFF: Protected space\r\n
0xb0010016 | Allocation range:%n%tMetadata allocation: %1 %n%tRequested tier: %2, actual tier: %3 %n%tRequested allocation start: %4, count: %5 %n%tActual allocation start: %6, count: %7\r\n
0xb0010017 | Log tail advance from %3 to %4.%nLog is %2 percent full.\r\n
0xb0010018 | Log pulse lazy writer. Log is %2 percent full.\r\n
0xb0010019 | Container move:%n%tSource tier: %1, Target tier: %2 %n%tSource start of range: %3, count: %4 %n%t Target physical offset: %5 %n%tSSD Fill Ratio %6, HDD Fill Ratio %7 %n%tReserved: %8%n%tDestaged allocation count: %9%n%tFailed SSD Destage: %10\r\n
0xb001001a | Minstore Redo Log application has been skipped. Minstore will now mount the volume without applying the redo log.\r\n
0xb001001b | An error %0 was encountered while replaying the redo log. Minstore will now mount the volume without applying the redo log.\r\n
0xb0010032 | Two threads tried to read bucket %1 (table %2) for level %0 simultaneously.\r\n
0xb0010033 | A thread had to wait to lock bucket %1 (table %2) for level %0.\r\n
0xb0010034 | A thread had to wait for a copy of bucket %1 (table %2) for level %0 to finish.\r\n
0xb0010064 | B+ node CRC mismatch\r\n
0xb0010065 | B+ node repaired via redundant copy\r\n
0xb00203e8 | B+ tree node started splitting\r\n
0xb00203ea | B+ tree node finished splitting\r\n
0xb00203eb | B+ tree nodes started merging\r\n
0xb00203ec | B+ tree nodes finished merging\r\n
0xb00203ed | B+ tree starting pushing its root\r\n
0xb00203ee | B+ tree finished pushing its root\r\n
0xb00203ef | B+ tree starting popping its root\r\n
0xb00203f0 | B+ tree finished popping its root\r\n
0xb00203f3 | Analyze pass start\r\n
0xb00203f4 | Analyze pass end\r\n
0xb00203f5 | Redo pass start\r\n
0xb00203f6 | Redo pass end\r\n
0xb00203f7 | Flush And Checkpoint start\r\n
0xb00203f8 | Flush And Checkpoint end\r\n
0xb00203f9 | First redo transaction found\r\n
0xb00203fa | Tree Update Record found\r\n
0xb00203fb | Open Table for redo\r\n
0xb00203fc | Reserve ranges for redo\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x3000000d | Bucket Split\r\n
0x3000000e | Bucket Merge\r\n
0x3000000f | Write B+ tree\r\n
0x30000010 | Checkpoint\r\n
0x30000011 | LFF: Redo Log\r\n
0x30000012 | LFF: Protected Space\r\n
0x30000013 | Allocation range\r\n
0x30000014 | Started writing B+ tree\r\n
0x30000015 | Finished writing B+ tree\r\n
0x30000016 | Log tail advance\r\n
0x30000017 | Log Redo\r\n
0x30000018 | Log pulse lazy writer\r\n
0x30000019 | Container move\r\n
0x3000001a | Log skip replay\r\n
0x3000001b | Log replay failure\r\n
0x30000032 | Bucket read collision\r\n
0x30000033 | Bucket lock collision\r\n
0x30000034 | Bucket cow collision\r\n
0x3000003c | Lazy Writer\r\n
0x30000064 | B+ node CRC mismatch\r\n
0x30000065 | B+ node repaired via redundant copy\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Minstore Event Provider\r\n
0x90000002 | Minstore Analytic Channel\r\n
0x90000003 | Minstore Debug Channel\r\n
0xb0010001 | Bucket split\r\n
0xb0010002 | Bucket merge\r\n
0xb001000a | Tree update\r\n
0xb001000b | Tree update\r\n
0xb001000c | Start tree update\r\n
0xb001000d | End tree update\r\n
0xb0010014 | LFF: Redo log\r\n
0xb0010015 | LFF: Protected space\r\n
0xb0010016 | Allocation range:%n%tMetadata allocation: %1 %n%tRequested tier: %2, actual tier: %3 %n%tRequested allocation start: %4, count: %5 %n%tActual allocation start: %6, count: %7\r\n
0xb0010017 | Log tail advance from %3 to %4.%nLog is %2 percent full.\r\n
0xb0010018 | Log pulse lazy writer. Log is %2 percent full.\r\n
0xb0010019 | Container move:%n%tSource tier: %1, Target tier: %2 %n%tSource start of range: %3, count: %4 %n%t Target physical offset: %5 %n%tSSD Fill Ratio %6, HDD Fill Ratio %7 %n%tReserved: %8%n%tDestaged allocation count: %9%n%tFailed SSD Destage: %10\r\n
0xb001001a | Minstore Redo Log application has been skipped. Minstore will now mount the volume without applying the redo log.\r\n
0xb001001b | An error %0 was encountered while replaying the redo log. Minstore will now mount the volume without applying the redo log.\r\n
0xb0010032 | Two threads tried to read bucket %1 (table %2) for level %0 simultaneously.\r\n
0xb0010033 | A thread had to wait to lock bucket %1 (table %2) for level %0.\r\n
0xb0010034 | A thread had to wait for a copy of bucket %1 (table %2) for level %0 to finish.\r\n
0xb0010064 | B+ node CRC mismatch\r\n
0xb0010065 | B+ node repaired via redundant copy\r\n
0xb00203e8 | B+ tree node started splitting\r\n
0xb00203ea | B+ tree node finished splitting\r\n
0xb00203eb | B+ tree nodes started merging\r\n
0xb00203ec | B+ tree nodes finished merging\r\n
0xb00203ed | B+ tree starting pushing its root\r\n
0xb00203ee | B+ tree finished pushing its root\r\n
0xb00203ef | B+ tree starting popping its root\r\n
0xb00203f0 | B+ tree finished popping its root\r\n
0xb00203f3 | Analyze pass start\r\n
0xb00203f4 | Analyze pass end\r\n
0xb00203f5 | Redo pass start\r\n
0xb00203f6 | Redo pass end\r\n
0xb00203f7 | Flush And Checkpoint start\r\n
0xb00203f8 | Flush And Checkpoint end\r\n
0xb00203f9 | First redo transaction found\r\n
0xb00203fa | Tree Update Record found\r\n
0xb00203fb | Open Table for redo\r\n
0xb00203fc | Reserve ranges for redo\r\n
0xb0020406 | Binding %1.%2 was added to lazy writer list\r\n
0xb0020407 | Binding %1.%2 was removed from lazy writer list\r\n
0xb0020408 | Binding %1.%2 was queued by rule %3\r\n
0xb0020409 | Binding %1.%2 write starts\r\n
