## iologmsg.dll

Path: %SystemRoot%\System32\IoLogMsg.dll

### 5.0.2134.1

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Lost Delayed-Write Data}\r\nThe system was attempting to transfer file data from buffers to %1.\r\nThe write operation failed, and only some of the data may have been\r\nwritten to the file.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail. \r\nImmediately back up your data and replace your hard disk drive. A failure \r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly \r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a \r\ncancel routine for a given IO request packet.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n

### 5.1.2600.0

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %1. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail. \r\nImmediately back up your data and replace your hard disk drive. A failure \r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly \r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a \r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory. \r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | Changing the disk signature of disk %2 because it is equal to the disk\r\nsignature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a non compliant corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a non compliant corrected error.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a non compliant fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a non compliant fatal error.\r\n

### 5.2.3790.0

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %1. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail. \r\nImmediately back up your data and replace your hard disk drive. A failure \r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly \r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a \r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory. \r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | Changing the disk signature of disk %2 because it is equal to the disk\r\nsignature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n

### 5.2.3790.1830

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %1. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail. \r\nImmediately back up your data and replace your hard disk drive. A failure \r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly \r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a \r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory. \r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | Changing the disk signature of disk %2 because it is equal to the disk\r\nsignature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40040085 | Device %1 is locked for exclusive access.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail.\r\nImmediately back up your data and replace your hard disk drive. A failure\r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly\r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a\r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | Changing the disk signature of disk %2 because it is equal to the disk\r\nsignature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x80040082 | The file system structure on volume %2 has now been repaired.\r\n
0x80040084 | Device %1 is not correctly processing some write requests. In Device Manager, ensure that the Write Cache option is disabled for this device or data corruption may occur.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost. \r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.  \r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost. \r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.  \r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost. \r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc0040083 | The file system structure on volume %2 cannot be corrected.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40040085 | Device %1 is locked for exclusive access.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail.\r\nImmediately back up your data and replace your hard disk drive. A failure\r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly\r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a\r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | The disk signature of disk %2 is equal to the disk signature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x80040082 | The file system structure on volume %2 has now been repaired.\r\n
0x80040084 | Device %1 is not correctly processing some write requests. In Device Manager, ensure that the Write Cache option is disabled for this device or data corruption may occur.\r\n
0x80040086 | The transaction resource manager on volume %2 encountered an error during recovery.  The resource manager will continue recovery.\r\n
0x80040088 | The default transaction resource manager on volume %2 encountered an error while starting and its metadata was reset.  The data contains the error code.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost. \r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.  \r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost. \r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.  \r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost. \r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc0040083 | The file system structure on volume %2 cannot be corrected.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc0040087 | The transaction resource manager on volume %2 was unable to create free space in its log due to a non-retryable error.  The data contains the error code.\r\n
0xc0040089 | The default transaction resource manager on volume %2 encountered a non-retryable error and could not start.  The data contains the error code.\r\n
0xc004008a | The transaction resource manager at %2%3 encountered a fatal error and was shut down.  The data contains the error code.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40040085 | Device %1 is locked for exclusive access.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail.\r\nImmediately back up your data and replace your hard disk drive. A failure\r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly\r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a\r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | The disk signature of disk %2 is equal to the disk signature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x80040084 | Device %1 is not correctly processing some write requests. In Device Manager, ensure that the Write Cache option is disabled for this device or data corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x8004008e | Extent %4 on disk %3 that is part of the fault-tolerant volume %2 is no longer accessible.\r\n
0x8004008f | The storage device produced an internal dump.\r\n
0x80040090 | Disk %2 has crossed a capacity utilization threshold.\r\n
0x80040091 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, there were %4 bytes of remaining capacity.\r\n
0x80040092 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the disk had %4 bytes of remaining capacity.\r\n
0x80040093 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the pool had %4 bytes of remaining capacity.\r\n
0x80040094 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the disk had %4 bytes of remaining capacity.\r\n
0x80040095 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the pool had %4 bytes of remaining capacity.\r\n
0x80040097 | The capacity of Disk %2 has changed.\r\n
0x80040098 | The logical block provisioning type for Disk %2 has changed.\r\n
0x80040099 | The IO operation at logical block address %2 for Disk %3 was retried.\r\n
0x8004009b | The IO operation at logical block address %2 for Disk %3 took %4 milliseconds. This was longer than the maximum expected time of %5 milliseconds.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc0040096 | Disk %2 has reached a logical block provisioning permanent resource exhaustion condition.\r\n
0xc004009a | The IO operation at logical block address %2 for Disk %3 failed due to a hardware error.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40040085 | Device %1 is locked for exclusive access.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail.\r\nImmediately back up your data and replace your hard disk drive. A failure\r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly\r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a\r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | The disk signature of disk %2 is equal to the disk signature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x80040084 | Device %1 is not correctly processing some write requests. In Device Manager, ensure that the Write Cache option is disabled for this device or data corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x8004008e | Extent %4 on disk %3 that is part of the fault-tolerant volume %2 is no longer accessible.\r\n
0x8004008f | The storage device produced an internal dump.\r\n
0x80040090 | Disk %2 has crossed a capacity utilization threshold.\r\n
0x80040091 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, there were %4 bytes of remaining capacity.\r\n
0x80040092 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the disk had %4 bytes of remaining capacity.\r\n
0x80040093 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the pool had %4 bytes of remaining capacity.\r\n
0x80040094 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the disk had %4 bytes of remaining capacity.\r\n
0x80040095 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the pool had %4 bytes of remaining capacity.\r\n
0x80040097 | The capacity of Disk %2 has changed.\r\n
0x80040098 | The logical block provisioning type for Disk %2 has changed.\r\n
0x80040099 | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) was retried.\r\n
0x8004009b | The IO operation at logical block address %2 for Disk %3 took %4 milliseconds. This was longer than the maximum expected time of %5 milliseconds.\r\n
0x8004009c | Crash dump is disabled. Crash dump device is not present in the system.\r\n
0x8004009d | Disk %2 has been surprise removed.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc0040096 | Disk %2 has reached a logical block provisioning permanent resource exhaustion condition.\r\n
0xc004009a | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) failed due to a hardware error.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n

### 10.0.10586.0, 10.0.14393.0

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40040085 | Device %1 is locked for exclusive access.\r\n
0x4004009f | Firmware update for Disk %2 is completed.\r\n
0x400400a0 | Firmware update for Adapter %1 is completed.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail.\r\nImmediately back up your data and replace your hard disk drive. A failure\r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly\r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a\r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | The disk signature of disk %2 is equal to the disk signature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x80040084 | Device %1 is not correctly processing some write requests. In Device Manager, ensure that the Write Cache option is disabled for this device or data corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x8004008e | Extent %4 on disk %3 that is part of the fault-tolerant volume %2 is no longer accessible.\r\n
0x8004008f | The storage device produced an internal dump.\r\n
0x80040090 | Disk %2 has crossed a capacity utilization threshold.\r\n
0x80040091 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, there were %4 bytes of remaining capacity.\r\n
0x80040092 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the disk had %4 bytes of remaining capacity.\r\n
0x80040093 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the pool had %4 bytes of remaining capacity.\r\n
0x80040094 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the disk had %4 bytes of remaining capacity.\r\n
0x80040095 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the pool had %4 bytes of remaining capacity.\r\n
0x80040097 | The capacity of Disk %2 has changed.\r\n
0x80040098 | The logical block provisioning type for Disk %2 has changed.\r\n
0x80040099 | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) was retried.\r\n
0x8004009b | The IO operation at logical block address %2 for Disk %3 took %4 milliseconds. This was longer than the maximum expected time of %5 milliseconds.\r\n
0x8004009c | Crash dump is disabled. Crash dump device is not present in the system.\r\n
0x8004009d | Disk %2 has been surprise removed.\r\n
0x8004009e | Disk %2 has the same disk identifiers as one or more disks connected to the system. Go to Microsoft's support website (http://support.microsoft.com) and search for KB2983588 to resolve the issue.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc0040096 | Disk %2 has reached a logical block provisioning permanent resource exhaustion condition.\r\n
0xc004009a | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) failed due to a hardware error.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n

### 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40040085 | Device %1 is locked for exclusive access.\r\n
0x4004009f | Firmware update for Disk %2 is completed.\r\n
0x400400a0 | Firmware update for Adapter %1 is completed.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail.\r\nImmediately back up your data and replace your hard disk drive. A failure\r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly\r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a\r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | The disk signature of disk %2 is equal to the disk signature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x80040084 | Device %1 is not correctly processing some write requests. In Device Manager, ensure that the Write Cache option is disabled for this device or data corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x8004008e | Extent %4 on disk %3 that is part of the fault-tolerant volume %2 is no longer accessible.\r\n
0x8004008f | The storage device produced an internal dump.\r\n
0x80040090 | Disk %2 has crossed a capacity utilization threshold.\r\n
0x80040091 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, there were %4 bytes of remaining capacity.\r\n
0x80040092 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the disk had %4 bytes of remaining capacity.\r\n
0x80040093 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the pool had %4 bytes of remaining capacity.\r\n
0x80040094 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the disk had %4 bytes of remaining capacity.\r\n
0x80040095 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the pool had %4 bytes of remaining capacity.\r\n
0x80040097 | The capacity of Disk %2 has changed.\r\n
0x80040098 | The logical block provisioning type for Disk %2 has changed.\r\n
0x80040099 | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) was retried.\r\n
0x8004009b | The IO operation at logical block address %2 for Disk %3 took %4 milliseconds. This was longer than the maximum expected time of %5 milliseconds.\r\n
0x8004009c | Crash dump is disabled. Crash dump device is not present in the system.\r\n
0x8004009d | Disk %2 has been surprise removed.\r\n
0x8004009e | Disk %2 has the same disk identifiers as one or more disks connected to the system. Go to Microsoft's support website (http://support.microsoft.com) and search for KB2983588 to resolve the issue.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc0040096 | Disk %2 has reached a logical block provisioning permanent resource exhaustion condition.\r\n
0xc004009a | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) failed due to a hardware error.\r\n
0xc00400a1 | Dump file creation failed due to error during dump creation.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n

### 10.0.17134.1, 10.0.17763.1

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40040085 | Device %1 is locked for exclusive access.\r\n
0x4004009f | Firmware update for Disk %2 is completed.\r\n
0x400400a0 | Firmware update for Adapter %1 is completed.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail.\r\nImmediately back up your data and replace your hard disk drive. A failure\r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly\r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a\r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | The disk signature of disk %2 is equal to the disk signature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x80040084 | Device %1 is not correctly processing some write requests. In Device Manager, ensure that the Write Cache option is disabled for this device or data corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x8004008e | Extent %4 on disk %3 that is part of the fault-tolerant volume %2 is no longer accessible.\r\n
0x8004008f | The storage device produced an internal dump.\r\n
0x80040090 | Disk %2 has crossed a capacity utilization threshold.\r\n
0x80040091 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, there were %4 bytes of remaining capacity.\r\n
0x80040092 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the disk had %4 bytes of remaining capacity.\r\n
0x80040093 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the pool had %4 bytes of remaining capacity.\r\n
0x80040094 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the disk had %4 bytes of remaining capacity.\r\n
0x80040095 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the pool had %4 bytes of remaining capacity.\r\n
0x80040097 | The capacity of Disk %2 has changed.\r\n
0x80040098 | The logical block provisioning type for Disk %2 has changed.\r\n
0x80040099 | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) was retried.\r\n
0x8004009b | The IO operation at logical block address %2 for Disk %3 took %4 milliseconds. This was longer than the maximum expected time of %5 milliseconds.\r\n
0x8004009c | Crash dump is disabled. Crash dump device is not present in the system.\r\n
0x8004009d | Disk %2 has been surprise removed.\r\n
0x8004009e | Disk %2 has the same disk identifiers as one or more disks connected to the system. Go to Microsoft's support website (http://support.microsoft.com) and search for KB2983588 to resolve the issue.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device {3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device {3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device {3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device {3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc0040096 | Disk %2 has reached a logical block provisioning permanent resource exhaustion condition.\r\n
0xc004009a | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) failed due to a hardware error.\r\n
0xc00400a1 | Dump file creation failed due to error during dump creation.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n

### 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40040085 | Device %1 is locked for exclusive access.\r\n
0x4004009f | Firmware update for Disk %2 is completed.\r\n
0x400400a0 | Firmware update for Adapter %1 is completed.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail.\r\nImmediately back up your data and replace your hard disk drive. A failure\r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly\r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a\r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | The disk signature of disk %2 is equal to the disk signature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x80040084 | Device %1 is not correctly processing some write requests. In Device Manager, ensure that the Write Cache option is disabled for this device or data corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x8004008e | Extent %4 on disk %3 that is part of the fault-tolerant volume %2 is no longer accessible.\r\n
0x8004008f | The storage device produced an internal dump.\r\n
0x80040090 | Disk %2 has crossed a capacity utilization threshold.\r\n
0x80040091 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, there were %4 bytes of remaining capacity.\r\n
0x80040092 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the disk had %4 bytes of remaining capacity.\r\n
0x80040093 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the pool had %4 bytes of remaining capacity.\r\n
0x80040094 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the disk had %4 bytes of remaining capacity.\r\n
0x80040095 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the pool had %4 bytes of remaining capacity.\r\n
0x80040097 | The capacity of Disk %2 has changed.\r\n
0x80040098 | The logical block provisioning type for Disk %2 has changed.\r\n
0x80040099 | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) was retried.\r\n
0x8004009b | The IO operation at logical block address %2 for Disk %3 took %4 milliseconds. This was longer than the maximum expected time of %5 milliseconds.\r\n
0x8004009c | Crash dump is disabled. Crash dump device is not present in the system.\r\n
0x8004009d | Disk %2 has been surprise removed.\r\n
0x8004009e | Disk %2 has the same disk identifiers as one or more disks connected to the system. Go to Microsoft's support website (http://support.microsoft.com) and search for KB2983588 to resolve the issue.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc0040096 | Disk %2 has reached a logical block provisioning permanent resource exhaustion condition.\r\n
0xc004009a | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) failed due to a hardware error.\r\n
0xc00400a1 | Dump file creation failed due to error during dump creation.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x00040001 | A retry was successful on %1.\r\n
0x000400a2 | Dump file generation succeded.\r\n
0x40040024 | A user hit their quota threshold on volume %2.\r\n
0x40040025 | A user hit their quota limit on volume %2.\r\n
0x40040026 | The system has started rebuilding the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040027 | The system has successfully rebuilt the user disk quota information on\r\ndevice %1 with label "%2".\r\n
0x40040077 | The driver for device %1 delayed non-paging Io requests for %2 ms to recover from a low memory condition.\r\n
0x40040085 | Device %1 is locked for exclusive access.\r\n
0x4004009f | Firmware update for Disk %2 is completed.\r\n
0x400400a0 | Firmware update for Adapter %1 is completed.\r\n
0x40050070 | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has dropped below the temperature limit and throttling has been removed. %2 additional error(s) are contained within the record.\r\n
0x40050073 | The maximum number of Machine Check Event corrected error events that can be saved to the Event Log has been reached. Logging of these events has been disabled.\r\n
0x40050074 | The memory page at physical address %1 has encountered multiple corrected hardware error events. As a result it will no longer be used by Windows.\r\n
0x8004001a | The driver has detected that device %1 has old or out-of-date firmware.\r\nReduced performance may result.\r\n
0x80040020 | The driver detected that the device %1 has its write cache enabled. Data corruption\r\nmay occur.\r\n
0x80040021 | Data was recovered using error correction code on device %1.\r\n
0x80040022 | The driver disabled the write cache on device %1.\r\n
0x80040028 | The system has encounted an error rebuilding the user disk quota\r\ninformation on device %1 with label "%2".\r\n
0x80040032 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0x80040033 | An error was detected on device %1 during a paging operation.\r\n
0x80040034 | The driver has detected that device %1 has predicted that it will fail.\r\nImmediately back up your data and replace your hard disk drive. A failure\r\nmay be imminent.\r\n
0x80040035 | A pending interrupt was detected on device %1 during a timeout operation.  A\r\nlarge number of these warnings may indicate that the system is not correctly\r\nreceiving or processing interrupts from the device.\r\n
0x80040036 | An Io Request to the device %1 did not complete or canceled within the\r\nspecific timeout. This can occur if the device driver does not set a\r\ncancel routine for a given IO request packet.\r\n
0x80040038 | The driver failed to allocate memory.\r\n
0x80040039 | The system failed to flush data to the transaction log. Corruption may occur.\r\n
0x8004003a | The disk signature of disk %2 is equal to the disk signature of disk %3.\r\n
0x8004003b | Disk %2 will not be used because it is a redundant path for disk %3.\r\n
0x80040076 | The driver for device %1 performed a bus reset upon request.\r\n
0x80040081 | Reset to device, %1, was issued.\r\n
0x80040084 | Device %1 is not correctly processing some write requests. In Device Manager, ensure that the Write Cache option is disabled for this device or data corruption may occur.\r\n
0x8004008b | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0x8004008c | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0x8004008d | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %2; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0x8004008e | Extent %4 on disk %3 that is part of the fault-tolerant volume %2 is no longer accessible.\r\n
0x8004008f | The storage device produced an internal dump.\r\n
0x80040090 | Disk %2 has crossed a capacity utilization threshold.\r\n
0x80040091 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, there were %4 bytes of remaining capacity.\r\n
0x80040092 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the disk had %4 bytes of remaining capacity.\r\n
0x80040093 | Disk %2 has crossed a capacity utilization threshold and used %3 bytes. When the threshold was crossed, the pool had %4 bytes of remaining capacity.\r\n
0x80040094 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the disk had %4 bytes of remaining capacity.\r\n
0x80040095 | Disk %2 has crossed a capacity utilization threshold. When the threshold was crossed, %3 bytes from the pool were used and the pool had %4 bytes of remaining capacity.\r\n
0x80040097 | The capacity of Disk %2 has changed.\r\n
0x80040098 | The logical block provisioning type for Disk %2 has changed.\r\n
0x80040099 | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) was retried.\r\n
0x8004009b | The IO operation at logical block address %2 for Disk %3 took %4 milliseconds. This was longer than the maximum expected time of %5 milliseconds.\r\n
0x8004009c | Crash dump is disabled. Crash dump device is not present in the system.\r\n
0x8004009d | Disk %2 has been surprise removed.\r\n
0x8004009e | Disk %2 has the same disk identifiers as one or more disks connected to the system. Go to Microsoft's support website (http://support.microsoft.com) and search for KB2983588 to resolve the issue.\r\n
0x8005003c | Machine Check Event reported is a corrected level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005003e | Machine Check Event reported is a corrected level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050040 | Machine Check Event reported is a corrected External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050042 | Machine Check Event reported is a corrected internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050044 | Machine Check Event reported is a corrected Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050046 | Machine Check Event reported is a corrected ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050048 | Machine Check Event reported is a corrected ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004a | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004c | Machine Check Event reported is a corrected ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005004e | Machine Check Event reported is a corrected System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050050 | Machine Check Event reported is a corrected PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050052 | Machine Check Event reported is a corrected PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050054 | Machine Check Event reported is a corrected PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050056 | Machine Check Event reported is a corrected PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050058 | Machine Check Event reported is a corrected PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005a | Machine Check Event reported is a corrected PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005c | Machine Check Event reported is a corrected PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x8005005e | Machine Check Event reported is a corrected PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050060 | Machine Check Event reported is an unknown corrected PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050062 | Machine Check Event reported is a corrected PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050064 | Machine Check Event reported is a corrected SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050066 | Machine Check Event reported is a corrected Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80050068 | Machine Check Event reported is a corrected error reported to CPU %1.\r\n
0x8005006a | Machine Check Event reported is a corrected error.\r\n
0x8005006d | Corrected Machine Check Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006e | Corrected Platform Error Interrupt threshold exceeded. Interrupt has been disabled. Polling mode has been enabled.\r\n
0x8005006f | Machine Check Event reported is a CPU thermal throttling event reported from CPU %1. The CPU has exceeded the temperature limit and has been throttled down. %2 additional error(s) are contained within the record.\r\n
0x80050071 | Machine Check Event reported is a corrected CPU error reported from CPU %1. %2 additional error(s) are contained within the record.\r\n
0x80380001 | There was an error validating KSR data - operation %2 status %3.\r\n
0x80380002 | Failed to read KSR data - disk %2 sector %3 operation %4 status %5.\r\n
0x80380003 | A %2 operation took place during KSR - disk %3 offset %4.\r\n
0xc0040002 | The driver could not allocate something necessary for the request for %1.\r\n
0xc0040003 | Driver or device is incorrectly configured for %1.\r\n
0xc0040004 | Driver detected an internal error in its data structures for %1.\r\n
0xc0040005 | A parity error was detected on %1.\r\n
0xc0040006 | The device, %1, had a seek error.\r\n
0xc0040007 | The device, %1, has a bad block.\r\n
0xc0040008 | An overrun occurred on %1.\r\n
0xc0040009 | The device, %1, did not respond within the timeout period.\r\n
0xc004000a | The driver detected an unexpected sequence by the device, %1.\r\n
0xc004000b | The driver detected a controller error on %1.\r\n
0xc004000c | The driver detected an internal driver error on %1.\r\n
0xc004000d | The driver was configured with an incorrect interrupt for %1.\r\n
0xc004000e | The driver was configured with an invalid I/O base address for %1.\r\n
0xc004000f | The device, %1, is not ready for access yet.\r\n
0xc0040010 | The request is incorrectly formatted for %1.\r\n
0xc0040011 | The wrong version of the driver has been loaded.\r\n
0xc0040012 | The driver beneath this one has failed in some way for %1.\r\n
0xc0040013 | The device, %1, has been reset.\r\n
0xc0040014 | A transport driver received a frame which violated the protocol.\r\n
0xc0040015 | A conflict has been detected between two drivers which claimed two overlapping\r\nmemory regions.\r\nDriver %2, with device <%3>, claimed a memory range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040016 | A conflict has been detected between two drivers which claimed two overlapping\r\nIo port regions.\r\nDriver %2, with device <%3>, claimed an IO port range with starting address\r\nin data address 0x28 and 0x2c, and length in data address 0x30.\r\n
0xc0040017 | A conflict has been detected between two drivers which claimed equivalent DMA\r\nchannels.\r\nDriver %2, with device <%3>, claimed the DMA Channel in data address 0x28, with\r\noptinal port in data address 0x2c.\r\n
0xc0040018 | A conflict has been detected between two drivers which claimed equivalent IRQs.\r\nDriver %2, with device <%3>, claimed an interrupt with Level in data address\r\n0x28, vector in data address 0x2c and Affinity in data address 0x30.\r\n
0xc0040019 | The driver has detected a device with old or out-of-date firmware.  The\r\ndevice will not be used.\r\n
0xc004001b | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device DMA setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001c | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device interrupt setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001d | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device memory setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001e | The device could not allocate one or more required resources due to conflicts\r\nwith other devices.  The device port setting of '%2' could not be\r\nsatisified due to a conflict with Driver '%3'.\r\n
0xc004001f | The file %2 on device %1 contains a bad disk block.\r\n
0xc0040029 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the device %1 with label "%2".\r\n
0xc004002a | The user disk quota information is unusable.\r\nTo ensure accuracy, the file system quota information on the device %1 with label "%2" will\r\nbe rebuilt.\r\n
0xc004002b | The system sleep operation failed\r\n
0xc004002c | The system could not get file retrieval pointers for the dump file.\r\n
0xc004002d | The system could not sucessfully load the crash dump driver.\r\n
0xc004002e | Crash dump initialization failed!\r\n
0xc004002f | A valid crash dump was found in the paging file while trying to configure\r\na direct dump. Direct dump is disabled! This occurs when the direct dump\r\noption is set in the registry but a stop error occured before configuration\r\ncompleted\r\n
0xc0040030 | Direct dump configuration failed. Validate the filename and make sure the target device\r\nis not a Fault Tolerant set member, remote, or floppy device. The failure may\r\nbe because there is not enough room on the dump device to create the dump file.\r\n
0xc0040031 | Configuring the Page file for crash dump failed. Make sure there is a page\r\nfile on the boot partition and that is large enough to contain all physical\r\nmemory.\r\n
0xc0040037 | The file system structure on the disk is corrupt and unusable.\r\nPlease run the chkdsk utility on the volume %2.\r\n
0xc004006c | The driver %3 for the %2 device %1 got stuck in an infinite loop. This\r\nusually indicates a problem with the device itself or with the device\r\ndriver programming the hardware incorrectly. Please check with your\r\nhardware device vendor for any driver updates.\r\n
0xc0040075 | The driver for device %1 detected a port timeout due to prolonged inactivity. All associated busses were reset in an effort to clear the condition.\r\n
0xc0040096 | Disk %2 has reached a logical block provisioning permanent resource exhaustion condition.\r\n
0xc004009a | The IO operation at logical block address %2 for Disk %3 (PDO name: %4) failed due to a hardware error.\r\n
0xc00400a1 | Dump file creation failed due to error during dump creation.\r\n
0xc00400a3 | A callback exception was logged during dump. See DumpStack.log for details.\r\n
0xc005003d | Machine Check Event reported is a fatal level %3 Cache error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005003f | Machine Check Event reported is a fatal level %3 translation Buffer error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050041 | Machine Check Event reported is a fatal External/Internal bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050043 | Machine Check Event reported is a fatal internal CPU register access error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050045 | Machine Check Event reported is a fatal Micro Architecture Structure error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050047 | Machine Check Event reported is a fatal ECC memory error at an unknown physical address reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050049 | Machine Check Event reported is a fatal ECC memory error at physical address %3 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004b | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004d | Machine Check Event reported is a fatal ECC memory error at physical address %3 on memory module %4 on memory card %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005004f | Machine Check Event reported is a fatal System Event error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050051 | Machine Check Event reported is a fatal PCI bus Parity error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050053 | Machine Check Event reported is a fatal PCI bus Parity error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050055 | Machine Check Event reported is a fatal PCI bus SERR error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050057 | Machine Check Event reported is a fatal PCI bus SERR error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050059 | Machine Check Event reported is a fatal PCI bus Master abort error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005b | Machine Check Event reported is a fatal PCI bus Master abort error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005d | Machine Check Event reported is a fatal PCI bus Timeout error during a transaction type %3 at address %4 on PCI bus %5 reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc005005f | Machine Check Event reported is a fatal PCI bus Timeout error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050061 | Machine Check Event reported is an unknown fatal PCI bus error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050063 | Machine Check Event reported is a fatal PCI component error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050065 | Machine Check Event reported is a fatal SMBIOS Device Type %3 error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050067 | Machine Check Event reported is a fatal Platform Specific error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050069 | Machine Check Event reported is a fatal error reported to CPU %1.\r\n
0xc005006b | Machine Check Event reported is a fatal error.\r\n
0xc0050072 | Machine Check Event reported is a fatal CPU error reported to CPU %1. %2 additional error(s) are contained within the record.\r\n
0xc0050078 | Machine Check Event reported is a fatal memory hierarchy error.%r Trasaction Type: %1%r Memory Hierarchy Level: %2%r Request Type: %3%r Address: %4\r\n
0xc0050079 | Machine Check Event reported is a fatal TLB error.%r Transaction Type: %1%r Memory Hierarchy Level: %2%r Address: %3\r\n
0xc005007a | Machine Check Event reported is a fatal Bus or Interconnect error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007b | Machine Check Event reported is a fatal Bus or Interconnect timeout error.%r Memory Hierarchy Level: %1%r Participation: %2%r Request Type: %3%r Memory/IO: %4%r Address: %5\r\n
0xc005007c | Machine Check Event reported is a fatal internal watchdog timer error.\r\n
0xc005007e | Machine Check Event reported is a fatal microsoft ROM parity error.\r\n
0xc005007f | Machine Check Event reported is a fatal condition. A processor received an external signal that an unrecoverable error has occurred.\r\n
0xc0050080 | Machine Check Event reported is a fatal functional redundancy check error.\r\n
