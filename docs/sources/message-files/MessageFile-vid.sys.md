## vid.sys

Path: %SystemRoot%\system32\drivers\vid.sys

### 10.0.17763.194

Message identifier | Message string
--- | ---
0x10000001 | Hyper-V performance traces (outer operations)\r\n
0x10000002 | Hyper-V performance traces (inner operations)\r\n
0x10000003 | Hyper-V performance traces (verbose)\r\n
0x1000000d | Hyper-V performance traces\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000600 | VID - reserve pages\r\n
0x70000601 | VID - release pages\r\n
0x70000602 | VID - balloon pages\r\n
0x70000603 | VID - un balloon pages\r\n
0x70000604 | VID - hot add\r\n
0x70000605 | VID - hot add undo\r\n
0x70000606 | VID - create memory block\r\n
0x70000612 | VID - create DAX file backed memory block\r\n
0x90000001 | Microsoft-Windows-Hyper-V-VID\r\n
0xb000044d | Failed to reserve %2 pages: %3. (Partition ID %1)\r\n
0xb000044e | Failed to reserve %2 pages: %3. (Partition ID %1)\r\n
0xb000044f | Failed to allocate %2 pages: %3. (Partition ID %1)\r\n
0xb0000450 | Failed to release %2 pages: %3. (Partition ID %1)\r\n
0xb0000451 | Failed to withdraw pages from bucket: %2. (Partition ID %1)\r\n
0xb0000452 | Failed to balloon %2 page ranges: %3. (Partition ID %1)\r\n
0xb0000453 | Failed to un-balloon %2 pages: %3. (Partition ID %1)\r\n
0xb0000454 | Failed to hot add %2 pages: %3. (Partition ID %1)\r\n
0xb0000455 | Failed to hot add undo %2 pages: %3. (Partition ID %1)\r\n
0xb0000456 | Failed to create mem block with %2 pages: %3. (Partition ID %1)\r\n
0xb0000457 | Failed to create DAX file backed mem block with %2 pages: %3. (Partition ID %1)\r\n
0xb0000bb8 | Created partition with ID %2 and name %1.\r\n
0xb0001389 | Started reserving %2 pages. (Partition ID %1)\r\n
0xb000138a | Finished reserving pages with status = %3. %2 pages reserved. %4 LargeLocal, %5 SmallLocal, %6 LargeRemote, %7 SmallRemote. (Partition ID %1)\r\n
0xb000138b | Started reserving bucket pages. Reserving %2 pages. (Partition ID %1)\r\n
0xb000138c | Finished reserving bucket pages with status = %3. %2 pages reserved. (Partition ID %1)\r\n
0xb000138d | Started allocating %2 pages. (Partition ID %1)\r\n
0xb000138e | Finished allocating pages with status = %3. %2 pages allocated. (Partition ID %1)\r\n
0xb000138f | Started depositing pages. (Partition ID %1)\r\n
0xb0001390 | Finished depositing pages. (Partition ID %1)\r\n
0xb0001391 | Started releasing %2 pages. (Partition ID %1)\r\n
0xb0001392 | Finished releasing %2 pages with status = %3. (Partition ID %1)\r\n
0xb0001393 | Started releasing bucket %2 pages. (Partition ID %1)\r\n
0xb0001394 | Finished releasing bucket %2 pages with status = %3. (Partition ID %1)\r\n
0xb0001395 | Started withdrawing pages from bucket. (Partition ID %1)\r\n
0xb0001396 | Finished withdrawing pages from bucket with status = %2. (Partition ID %1)\r\n
0xb0001399 | Started depositing pages to bucket from page list. (Partition ID %1)\r\n
0xb000139a | Finished depositing pages to bucket from page list. (Partition ID %1)\r\n
0xb000139b | Started ballooning %2 page ranges. (Partition ID %1)\r\n
0xb000139c | Finished ballooning %2 page ranges with status %3. (Partition ID %1)\r\n
0xb000139d | Started de-committing GPAs - %2 pages. (Partition ID %1)\r\n
0xb000139e | Finished de-committing GPAs - %2 pages with status %3. (Partition ID %1)\r\n
0xb000139f | Started un-ballooning %2 pages. (Partition ID %1)\r\n
0xb00013a0 | Finished un-ballooning %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a1 | Started committing %2 pages. (Partition ID %1)\r\n
0xb00013a2 | Finished committing %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a5 | Started hot adding %2 pages. (Partition ID %1)\r\n
0xb00013a6 | Finished hot adding %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a7 | Started hot add undoing %2 pages. (Partition ID %1)\r\n
0xb00013a8 | Finished hot add undoing %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a9 | Started creating memory block with %2 pages. (Partition ID %1)\r\n
0xb00013aa | Finished creating memory block with %2 pages with status %3. (Partition ID %1)\r\n
0xb00013ab | Started un-ballooning %2 pages. Contiguous = %3. (Partition ID %1)\r\n
0xb00013ac | Finished un-ballooning %2 pages with status %3. Contiguous = %4. (Partition ID %1)\r\n
0xb00013ad | An uncorrected memory error occurred at physical address %1. This page was not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013ae | '%3' was reset because an uncorrected memory error occured at physical address %1, which was used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2)\r\n
0xb00013af | An uncorrected memory error occurred at physical address %1 which is used by virtual machine '%3'. The affected page has been released. A machine check event correpsonding to this memory error was injected into the virtual machine for handling by the virtual machine's operating system. (Virtual Machine: %4, Platform Directed: %2)\r\n
0xb00013b0 | An uncorrected memory error occurred at physical address %1. The virtual machine that was using the page is no longer valid. No action was taken. (Platform Directed: %2)\r\n
0xb00013b1 | One or more corrected memory error occurred at physical address %1. This page was not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013b2 | One or more corrected memory error occurred at physical address %1, which is used by virtual machine '%3'. The page could not be replaced. No action was taken. The virtual machine will continue operating normally. (Virtual Machine: %4, Platform Directed: %2)\r\n
0xb00013b3 | One or more corrected memory error occurred at physical address %1, which is used by virtual machine '%3'. The page has been replaced. The virtual machine will continue operating normally. (Virtual Machine: %4, Platform Directed: %2)\r\n
0xb00013b4 | Failed to retrieve memory from the kernel with error %2 during a fast restore operation. (Virtual Machine %1)\r\n
0xb00013b5 | Failed to persist memory with the kernel with error %2 during a fast save operation. (Virtual Machine %1)\r\n
0xb00013cc | Started creating DAX file backed memory block with %2 pages. (Partition ID %1)\r\n
0xb00013cd | Finished creating DAX file backed memory block with %2 pages with status %3. (Partition ID %1)\r\n

### 10.0.18362.1, 10.0.18362.476

Message identifier | Message string
--- | ---
0x10000001 | Hyper-V performance traces (outer operations)\r\n
0x10000002 | Hyper-V performance traces (inner operations)\r\n
0x10000003 | Hyper-V performance traces (verbose)\r\n
0x1000000d | Hyper-V performance traces\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000600 | VID - reserve pages\r\n
0x70000601 | VID - release pages\r\n
0x70000602 | VID - balloon pages\r\n
0x70000603 | VID - un balloon pages\r\n
0x70000604 | VID - hot add\r\n
0x70000605 | VID - hot add undo\r\n
0x70000606 | VID - create memory block\r\n
0x70000612 | VID - create DAX file backed memory block\r\n
0x90000001 | Microsoft-Windows-Hyper-V-VID\r\n
0xb000044d | Failed to reserve %2 pages: %3. (Partition ID %1)\r\n
0xb000044e | Failed to reserve %2 pages: %3. (Partition ID %1)\r\n
0xb000044f | Failed to allocate %2 pages: %3. (Partition ID %1)\r\n
0xb0000450 | Failed to release %2 pages: %3. (Partition ID %1)\r\n
0xb0000451 | Failed to withdraw pages from bucket: %2. (Partition ID %1)\r\n
0xb0000452 | Failed to balloon %2 page ranges: %3. (Partition ID %1)\r\n
0xb0000453 | Failed to un-balloon %2 pages: %3. (Partition ID %1)\r\n
0xb0000454 | Failed to hot add %2 pages: %3. (Partition ID %1)\r\n
0xb0000455 | Failed to hot add undo %2 pages: %3. (Partition ID %1)\r\n
0xb0000456 | Failed to create mem block with %2 pages: %3. (Partition ID %1)\r\n
0xb0000457 | Failed to create DAX file backed mem block with %2 pages: %3. (Partition ID %1)\r\n
0xb0000bb8 | Created partition with ID %2 and name %1.\r\n
0xb0001389 | Started reserving %2 pages. (Partition ID %1)\r\n
0xb000138a | Finished reserving pages with status = %3. %2 pages reserved. %4 LargeLocal, %5 SmallLocal, %6 LargeRemote, %7 SmallRemote. (Partition ID %1)\r\n
0xb000138b | Started reserving bucket pages. Reserving %2 pages. (Partition ID %1)\r\n
0xb000138c | Finished reserving bucket pages with status = %3. %2 pages reserved. (Partition ID %1)\r\n
0xb000138d | Started allocating %2 pages. (Partition ID %1)\r\n
0xb000138e | Finished allocating pages with status = %3. %2 pages allocated. (Partition ID %1)\r\n
0xb000138f | Started depositing pages. (Partition ID %1)\r\n
0xb0001390 | Finished depositing pages. (Partition ID %1)\r\n
0xb0001391 | Started releasing %2 pages. (Partition ID %1)\r\n
0xb0001392 | Finished releasing %2 pages with status = %3. (Partition ID %1)\r\n
0xb0001393 | Started releasing bucket %2 pages. (Partition ID %1)\r\n
0xb0001394 | Finished releasing bucket %2 pages with status = %3. (Partition ID %1)\r\n
0xb0001395 | Started withdrawing pages from bucket. (Partition ID %1)\r\n
0xb0001396 | Finished withdrawing pages from bucket with status = %2. (Partition ID %1)\r\n
0xb0001399 | Started depositing pages to bucket from page list. (Partition ID %1)\r\n
0xb000139a | Finished depositing pages to bucket from page list. (Partition ID %1)\r\n
0xb000139b | Started ballooning %2 page ranges. (Partition ID %1)\r\n
0xb000139c | Finished ballooning %2 page ranges with status %3. (Partition ID %1)\r\n
0xb000139d | Started de-committing GPAs - %2 pages. (Partition ID %1)\r\n
0xb000139e | Finished de-committing GPAs - %2 pages with status %3. (Partition ID %1)\r\n
0xb000139f | Started un-ballooning %2 pages. (Partition ID %1)\r\n
0xb00013a0 | Finished un-ballooning %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a1 | Started committing %2 pages. (Partition ID %1)\r\n
0xb00013a2 | Finished committing %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a5 | Started hot adding %2 pages. (Partition ID %1)\r\n
0xb00013a6 | Finished hot adding %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a7 | Started hot add undoing %2 pages. (Partition ID %1)\r\n
0xb00013a8 | Finished hot add undoing %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a9 | Started creating memory block with %2 pages. (Partition ID %1)\r\n
0xb00013aa | Finished creating memory block with %2 pages with status %3. (Partition ID %1)\r\n
0xb00013ab | Started un-ballooning %2 pages. Contiguous = %3. (Partition ID %1)\r\n
0xb00013ac | Finished un-ballooning %2 pages with status %3. Contiguous = %4. (Partition ID %1)\r\n
0xb00013ad | An uncorrected memory error occurred at physical address %1. This page was not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013ae | '%3' was reset because an uncorrected memory error occured at physical address %1, which was used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013af | An uncorrected memory error occurred at physical address %1 which is used by virtual machine '%3'. The affected page has been released. A machine check event correpsonding to this memory error was injected into the virtual machine for handling by the virtual machine's operating system. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013b0 | An uncorrected memory error occurred at physical address %1. The virtual machine that was using the page is no longer valid. No action was taken. (Platform Directed: %2)\r\n
0xb00013b1 | One or more corrected memory error occurred at physical address %1. This page was not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013b2 | One or more corrected memory error occurred at physical address %1, which is used by virtual machine '%3'. The page could not be replaced. No action was taken. The virtual machine will continue operating normally. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013b3 | One or more corrected memory error occurred at physical address %1, which is used by virtual machine '%3'. The page has been replaced. The virtual machine will continue operating normally. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013b4 | Failed to retrieve memory from the kernel with error %2 during a fast restore operation. (Virtual Machine %1)\r\n
0xb00013b5 | Failed to persist memory with the kernel with error %2 during a fast save operation. (Virtual Machine %1)\r\n
0xb00013cc | Started creating DAX file backed memory block with %2 pages. (Partition ID %1)\r\n
0xb00013cd | Finished creating DAX file backed memory block with %2 pages with status %3. (Partition ID %1)\r\n
0xb00013d0 | One or more uncorrected persistent memory errors (%1 pages) occurred. These pages were not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013d1 | '%3' was reset because an uncorrected persistent memory error occured at physical address %1, which was used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013d2 | '%3' was reset because one or more uncorrected persistent memory errors (%1 pages) occured, which were used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013d3 | An uncorrected persistent memory error occurred at physical address %1 which is used by virtual machine '%3'. The affected page has been released. A machine check event correpsonding to this persistent memory error was injected into the virtual machine for handling by the virtual machine's operating system. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013d4 | An uncorrected persistent memory error occurred at physical address %1. The virtual machine that was using the page is no longer valid. No action was taken. (Platform Directed: %2)\r\n
0xb00013d5 | One or more uncorrected persistent memory errors (%1 pages) occurred, which were used by virtual machine '%3'. ARS notification generated. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n

### 10.0.19041.1, 10.0.19041.423

Message identifier | Message string
--- | ---
0x10000001 | Hyper-V performance traces (outer operations)\r\n
0x10000002 | Hyper-V performance traces (inner operations)\r\n
0x10000003 | Hyper-V performance traces (verbose)\r\n
0x1000000d | Hyper-V performance traces\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000600 | VID - reserve pages\r\n
0x70000601 | VID - release pages\r\n
0x70000602 | VID - balloon pages\r\n
0x70000603 | VID - un balloon pages\r\n
0x70000604 | VID - hot add\r\n
0x70000605 | VID - hot add undo\r\n
0x70000606 | VID - create memory block\r\n
0x70000612 | VID - create DAX file backed memory block\r\n
0x90000001 | Microsoft-Windows-Hyper-V-VID\r\n
0xb000044d | Failed to reserve %2 pages: %3. (Partition ID %1)\r\n
0xb000044e | Failed to reserve %2 pages: %3. (Partition ID %1)\r\n
0xb000044f | Failed to allocate %2 pages: %3. (Partition ID %1)\r\n
0xb0000450 | Failed to release %2 pages: %3. (Partition ID %1)\r\n
0xb0000451 | Failed to withdraw pages from bucket: %2. (Partition ID %1)\r\n
0xb0000452 | Failed to balloon %2 page ranges: %3. (Partition ID %1)\r\n
0xb0000453 | Failed to un-balloon %2 pages: %3. (Partition ID %1)\r\n
0xb0000454 | Failed to hot add %2 pages: %3. (Partition ID %1)\r\n
0xb0000455 | Failed to hot add undo %2 pages: %3. (Partition ID %1)\r\n
0xb0000456 | Failed to create mem block with %2 pages: %3. (Partition ID %1)\r\n
0xb0000457 | Failed to create DAX file backed mem block with %2 pages: %3. (Partition ID %1)\r\n
0xb0000bb8 | Created partition with ID %2 and name %1.\r\n
0xb0001389 | Started reserving %2 pages. (Partition ID %1)\r\n
0xb000138a | Finished reserving pages with status = %3. %2 pages reserved. %4 LargeLocal, %5 SmallLocal, %6 LargeRemote, %7 SmallRemote. (Partition ID %1)\r\n
0xb000138b | Started reserving bucket pages. Reserving %2 pages. (Partition ID %1)\r\n
0xb000138c | Finished reserving bucket pages with status = %3. %2 pages reserved. (Partition ID %1)\r\n
0xb000138d | Started allocating %2 pages. (Partition ID %1)\r\n
0xb000138e | Finished allocating pages with status = %3. %2 pages allocated. (Partition ID %1)\r\n
0xb000138f | Started depositing pages. (Partition ID %1)\r\n
0xb0001390 | Finished depositing pages. (Partition ID %1)\r\n
0xb0001391 | Started releasing %2 pages. (Partition ID %1)\r\n
0xb0001392 | Finished releasing %2 pages with status = %3. (Partition ID %1)\r\n
0xb0001393 | Started releasing bucket %2 pages. (Partition ID %1)\r\n
0xb0001394 | Finished releasing bucket %2 pages with status = %3. (Partition ID %1)\r\n
0xb0001395 | Started withdrawing pages from bucket. (Partition ID %1)\r\n
0xb0001396 | Finished withdrawing pages from bucket with status = %2. (Partition ID %1)\r\n
0xb0001399 | Started depositing pages to bucket from page list. (Partition ID %1)\r\n
0xb000139a | Finished depositing pages to bucket from page list. (Partition ID %1)\r\n
0xb000139b | Started ballooning %2 page ranges. (Partition ID %1)\r\n
0xb000139c | Finished ballooning %2 page ranges with status %3. (Partition ID %1)\r\n
0xb000139d | Started de-committing GPAs - %2 pages. (Partition ID %1)\r\n
0xb000139e | Finished de-committing GPAs - %2 pages with status %3. (Partition ID %1)\r\n
0xb000139f | Started un-ballooning %2 pages. (Partition ID %1)\r\n
0xb00013a0 | Finished un-ballooning %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a1 | Started committing %2 pages. (Partition ID %1)\r\n
0xb00013a2 | Finished committing %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a5 | Started hot adding %2 pages. (Partition ID %1)\r\n
0xb00013a6 | Finished hot adding %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a7 | Started hot add undoing %2 pages. (Partition ID %1)\r\n
0xb00013a8 | Finished hot add undoing %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a9 | Started creating memory block with %2 pages. (Partition ID %1)\r\n
0xb00013aa | Finished creating memory block with %2 pages with status %3. (Partition ID %1)\r\n
0xb00013ab | Started un-ballooning %2 pages. Contiguous = %3. (Partition ID %1)\r\n
0xb00013ac | Finished un-ballooning %2 pages with status %3. Contiguous = %4. (Partition ID %1)\r\n
0xb00013ad | An uncorrected memory error occurred at physical address %1. This page was not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013ae | '%3' was reset because an uncorrected memory error occured at physical address %1, which was used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013af | An uncorrected memory error occurred at physical address %1 which is used by virtual machine '%3'. The affected page has been released. A machine check event correpsonding to this memory error was injected into the virtual machine for handling by the virtual machine's operating system. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013b0 | An uncorrected memory error occurred at physical address %1. The virtual machine that was using the page is no longer valid. No action was taken. (Platform Directed: %2)\r\n
0xb00013b1 | One or more corrected memory error occurred at physical address %1. This page was not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013b2 | One or more corrected memory error occurred at physical address %1, which is used by virtual machine '%3'. The page could not be replaced. No action was taken. The virtual machine will continue operating normally. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013b3 | One or more corrected memory error occurred at physical address %1, which is used by virtual machine '%3'. The page has been replaced. The virtual machine will continue operating normally. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013b4 | Failed to retrieve memory from the kernel with error %2 during a fast restore operation. (Virtual Machine %1)\r\n
0xb00013b5 | Failed to persist memory with the kernel with error %2 during a fast save operation. (Virtual Machine %1)\r\n
0xb00013cc | Started creating DAX file backed memory block with %2 pages. (Partition ID %1)\r\n
0xb00013cd | Finished creating DAX file backed memory block with %2 pages with status %3. (Partition ID %1)\r\n
0xb00013d0 | One or more uncorrected persistent memory errors (%1 pages) occurred. These pages were not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013d1 | '%3' was reset because an uncorrected persistent memory error occured at physical address %1, which was used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013d2 | '%3' was reset because one or more uncorrected persistent memory errors (%1 pages) occured, which were used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013d3 | An uncorrected persistent memory error occurred at physical address %1 which is used by virtual machine '%3'. The affected page has been released. A machine check event correpsonding to this persistent memory error was injected into the virtual machine for handling by the virtual machine's operating system. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013d4 | An uncorrected persistent memory error occurred at physical address %1. The virtual machine that was using the page is no longer valid. No action was taken. (Platform Directed: %2)\r\n
0xb00013d5 | One or more uncorrected persistent memory errors (%1 pages) occurred, which were used by virtual machine '%3'. ARS notification generated. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013db | Memory partition: Both Percentage(%3) and SizeInMB(%2) are specified for NUMA node %1. Percentage(%3) is ignored.\r\n
0xb00013dc | Memory partition: Both Percentage and SizeInMB are specified on the host. Percentage is ignored.\r\n
0xb00013dd | Memory partition: Both NUMA node settings and host settings are specified. The host settings are ignored.\r\n
0xb00013de | Memory partition: Primary settings are different than the legacy settings. The legacy settings are ignored.\r\n
0xb00013df | Memory partition: Legacy memory reserve percentage setting was used.\r\n
0xb00013e0 | Memory partition not created due to 0 partition size. This maybe caused by invalid percentage or unaligned size.\r\n
0xb00013e1 | Memory partition creation failed (%2 MB) with status = %1.\r\n
0xb00013e2 | Memory partition: Percentage(%1) is invalid.\r\n
0xb00013e3 | Memory partition target could not be read from the registry.\r\n
0xb00013e4 | Memory partition target could not be written to the registry.\r\n
0xb00013e5 | A non-zero memory partition target size was associated with a memoryless and processorless NUMA node. Node Number %1.\r\n
0xb00013e6 | Memory partition target number of nodes (%1) did not match the number of NUMA nodes on the system (%2).\r\n

### 10.0.22000.71

Message identifier | Message string
--- | ---
0x10000001 | Hyper-V performance traces (outer operations)\r\n
0x10000002 | Hyper-V performance traces (inner operations)\r\n
0x10000003 | Hyper-V performance traces (verbose)\r\n
0x1000000d | Hyper-V performance traces\r\n
0x10000031 | Response Time\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000600 | VID - reserve pages\r\n
0x70000601 | VID - release pages\r\n
0x70000602 | VID - balloon pages\r\n
0x70000603 | VID - un balloon pages\r\n
0x70000604 | VID - hot add\r\n
0x70000605 | VID - hot add undo\r\n
0x70000606 | VID - create memory block\r\n
0x70000612 | VID - create DAX file backed memory block\r\n
0x90000001 | Microsoft-Windows-Hyper-V-VID\r\n
0xb000044d | Failed to reserve %2 pages: %3. (Partition ID %1)\r\n
0xb000044e | Failed to reserve %2 pages: %3. (Partition ID %1)\r\n
0xb000044f | Failed to allocate %2 pages: %3. (Partition ID %1)\r\n
0xb0000450 | Failed to release %2 pages: %3. (Partition ID %1)\r\n
0xb0000451 | Failed to withdraw pages from bucket: %2. (Partition ID %1)\r\n
0xb0000452 | Failed to balloon %2 page ranges: %3. (Partition ID %1)\r\n
0xb0000453 | Failed to un-balloon %2 pages: %3. (Partition ID %1)\r\n
0xb0000454 | Failed to hot add %2 pages: %3. (Partition ID %1)\r\n
0xb0000455 | Failed to hot add undo %2 pages: %3. (Partition ID %1)\r\n
0xb0000456 | Failed to create mem block with %2 pages: %3. (Partition ID %1)\r\n
0xb0000457 | Failed to create DAX file backed mem block with %2 pages: %3. (Partition ID %1)\r\n
0xb0000bb8 | Created partition with ID %2 and name %1.\r\n
0xb0001389 | Started reserving %2 pages. (Partition ID %1)\r\n
0xb000138a | Finished reserving pages with status = %3. %2 pages reserved. %4 HugeLocal, %5 LargeLocal, %6 SmallLocal, %7 HugeRemote, %8 LargeRemote, %9 SmallRemote. (Partition ID %1)\r\n
0xb000138b | Started reserving bucket pages. Reserving %2 pages. (Partition ID %1)\r\n
0xb000138c | Finished reserving bucket pages with status = %3. %2 pages reserved. (Partition ID %1)\r\n
0xb000138d | Started allocating %2 pages. (Partition ID %1)\r\n
0xb000138e | Finished allocating pages with status = %3. %2 pages allocated. (Partition ID %1)\r\n
0xb000138f | Started depositing pages. (Partition ID %1)\r\n
0xb0001390 | Finished depositing pages. (Partition ID %1)\r\n
0xb0001391 | Started releasing %2 pages. (Partition ID %1)\r\n
0xb0001392 | Finished releasing %2 pages with status = %3. (Partition ID %1)\r\n
0xb0001393 | Started releasing bucket %2 pages. (Partition ID %1)\r\n
0xb0001394 | Finished releasing bucket %2 pages with status = %3. (Partition ID %1)\r\n
0xb0001395 | Started withdrawing pages from bucket. (Partition ID %1)\r\n
0xb0001396 | Finished withdrawing pages from bucket with status = %2. (Partition ID %1)\r\n
0xb0001399 | Started depositing pages to bucket from page list. (Partition ID %1)\r\n
0xb000139a | Finished depositing pages to bucket from page list. (Partition ID %1)\r\n
0xb000139b | Started ballooning %2 page ranges. (Partition ID %1)\r\n
0xb000139c | Finished ballooning %2 page ranges with status %3. (Partition ID %1)\r\n
0xb000139d | Started de-committing GPAs - %2 pages. (Partition ID %1)\r\n
0xb000139e | Finished de-committing GPAs - %2 pages with status %3. (Partition ID %1)\r\n
0xb000139f | Started un-ballooning %2 pages. (Partition ID %1)\r\n
0xb00013a0 | Finished un-ballooning %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a1 | Started committing %2 pages. (Partition ID %1)\r\n
0xb00013a2 | Finished committing %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a5 | Started hot adding %2 pages. (Partition ID %1)\r\n
0xb00013a6 | Finished hot adding %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a7 | Started hot add undoing %2 pages. (Partition ID %1)\r\n
0xb00013a8 | Finished hot add undoing %2 pages with status %3. (Partition ID %1)\r\n
0xb00013a9 | Started creating memory block with %2 pages. (Partition ID %1)\r\n
0xb00013aa | Finished creating memory block with %2 pages with status %3. (Partition ID %1)\r\n
0xb00013ab | Started un-ballooning %2 pages. Contiguous = %3. (Partition ID %1)\r\n
0xb00013ac | Finished un-ballooning %2 pages with status %3. Contiguous = %4. (Partition ID %1)\r\n
0xb00013ad | An uncorrected memory error occurred at physical address %1. This page was not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013ae | '%3' was reset because an uncorrected memory error occured at physical address %1, which was used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013af | An uncorrected memory error occurred at physical address %1 which is used by virtual machine '%3'. The affected page has been released. A machine check event correpsonding to this memory error was injected into the virtual machine for handling by the virtual machine's operating system. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013b0 | An uncorrected memory error occurred at physical address %1. The virtual machine that was using the page is no longer valid. No action was taken. (Platform Directed: %2)\r\n
0xb00013b1 | One or more corrected memory error occurred at physical address %1. This page was not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013b2 | One or more corrected memory error occurred at physical address %1, which is used by virtual machine '%3'. The page could not be replaced. No action was taken. The virtual machine will continue operating normally. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013b3 | One or more corrected memory error occurred at physical address %1, which is used by virtual machine '%3'. The page has been replaced. The virtual machine will continue operating normally. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013b4 | Failed to retrieve memory from the kernel with error %2 during a fast restore operation. (Virtual Machine %1)\r\n
0xb00013b5 | Failed to persist memory with the kernel with error %2 during a fast save operation. (Virtual Machine %1)\r\n
0xb00013cc | Started creating DAX file backed memory block with %2 pages. (Partition ID %1)\r\n
0xb00013cd | Finished creating DAX file backed memory block with %2 pages with status %3. (Partition ID %1)\r\n
0xb00013d0 | One or more uncorrected persistent memory errors (%1 pages) occurred. These pages were not found in a virtual machine. No action was taken. (Platform Directed: %2)\r\n
0xb00013d1 | '%3' was reset because an uncorrected persistent memory error occured at physical address %1, which was used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013d2 | '%3' was reset because one or more uncorrected persistent memory errors (%1 pages) occured, which were used by this virtual machine. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013d3 | An uncorrected persistent memory error occurred at physical address %1 which is used by virtual machine '%3'. The affected page has been released. A machine check event correpsonding to this persistent memory error was injected into the virtual machine for handling by the virtual machine's operating system. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013d4 | An uncorrected persistent memory error occurred at physical address %1. The virtual machine that was using the page is no longer valid. No action was taken. (Platform Directed: %2)\r\n
0xb00013d5 | One or more uncorrected persistent memory errors (%1 pages) occurred, which were used by virtual machine '%3'. ARS notification generated. (Virtual Machine: %4, Platform Directed: %2, Consumed: %5)\r\n
0xb00013db | Memory partition: Both Percentage(%3) and SizeInMB(%2) are specified for NUMA node %1. Percentage(%3) is ignored.\r\n
0xb00013dc | Memory partition: Both Percentage and SizeInMB are specified on the host. Percentage is ignored.\r\n
0xb00013dd | Memory partition: Both NUMA node settings and host settings are specified. The host settings are ignored.\r\n
0xb00013de | Memory partition: Primary settings are different than the legacy settings. The legacy settings are ignored.\r\n
0xb00013df | Memory partition: Legacy memory reserve percentage setting was used.\r\n
0xb00013e0 | Memory partition not created due to 0 partition size. This maybe caused by invalid percentage or unaligned size.\r\n
0xb00013e1 | Memory partition creation failed (%2 MB) with status = %1.\r\n
0xb00013e2 | Memory partition host percentage(%1) is invalid.\r\n
0xb00013e3 | Memory partition target could not be read from the registry.\r\n
0xb00013e4 | Memory partition target could not be written to the registry.\r\n
0xb00013e5 | A non-zero memory partition target size was associated with a memoryless and processorless NUMA node. Node Number %1.\r\n
0xb00013e6 | Memory partition target number of nodes (%1) did not match the number of NUMA nodes on the system (%2).\r\n
0xb00013e8 | Memory partition per NUMA node (%1) IO space size (%2) unaligned.\r\n
0xb00013e9 | Memory partition per NUMA node (%1) IO space size (%2) is bigger than size (%3).\r\n
0xb00013ea | Memory partition host IO space size (%1) unaligned.\r\n
0xb00013eb | Memory partition host IO space size (%1) is too big for size (%2).\r\n
0xb00013ec | Memory partition per NUMA node (%1) size (%2) unaligned.\r\n
0xb00013ed | Memory partition host size (%1) unaligned.\r\n
0xb00013ee | Memory partition per NUMA node (%1) percentage(%2) is invalid.\r\n
0xb00013ef | Memory partition legacy percentage(%1) is invalid.\r\n
0xb00013f0 | Failed to retrieve memory block from the kernel with error %2 during a fast restore operation. (Virtual Machine %1)\r\n
0xb00013f1 | Failed to persist memory block with the kernel with error %2 during a fast save operation. (Virtual Machine %1)\r\n
