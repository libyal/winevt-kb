## spaceport.sys

Path: %SystemRoot%\system32\drivers\spaceport.sys

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000064 | Physical drive %1 failed to read the configuration or returned corrupt data for storage pool %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb0000065 | All physical drives failed to read the configuration or returned corrupt data for storage pool %1. As a result the pool will be inaccessible. Return Code: %2\r\n
0xb0000066 | Majority of the physical drives of storage pool %1 failed a configuration update, which caused the pool to go into a failed state. Return Code: %2\r\n
0xb0000067 | The capacity consumption of the storage pool %1 has exceeded the threshold limit set on the pool. Return Code: %2\r\n
0xb0000068 | The capacity consumption of the storage pool %1 is now below the threshold limit set on the pool. Return Code: %2\r\n
0xb00000c8 | Windows was unable to read the drive header for physical drive %1. If you know the drive is still usable, then resetting the drive health by using command line or GUI may clear this failure condition and enable you to reassign the drive to its storage pool. Return Code: %2\r\n
0xb00000c9 | Physical drive %1 has invalid meta-data. Resetting the health status, using command line or GUI, might bring the physical drive to the primordial pool. Return Code: %2\r\n
0xb00000ca | Physical drive %1 has invalid meta-data. Resetting the health status, using command line or GUI, might resolve the issue. Return Code: %2\r\n
0xb00000cb | An IO failure has occurred on Physical drive %1 Return Code: %2\r\n
0xb000012c | Physical drive %1 failed to read the configuration or returned corrupt data for storage space %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb000012d | All pool drives failed to read the configuration or returned corrupt data for storage space %1. As a result the storage space will not attach. Return Code: %2\r\n
0xb000012e | Majority of the pool drives hosting space meta-data for storage space %1 failed a space meta-data update, which caused the storage pool to go in failed state. Return Code: %2\r\n
0xb000012f | Drives hosting data for storage space %1 have failed or are missing. As a result, no copy of data is available. Return Code: %2\r\n
0xb0000130 | One or more drives hosting data for storage space %1 have failed or are missing. As a result, at least one copy of data is not available. However, at least one copy of data is still available. Return Code: %2\r\n
0xb0000132 | The attempt to map, or allocate more storage for, the storage space %1 has failed. This is because there was a write failure involved in the updating the storage space metadata. Return Code: %2\r\n
0xb0000133 | The attempt to unmap or trim the storage space %1 has failed. Return Code: %2\r\n
0xb0000134 | A repair attempt for storage space %1 was initiated by the driver. Return Code: %2\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000064 | Physical drive %1 failed to read the configuration or returned corrupt data for storage pool %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb0000065 | All physical drives failed to read the configuration or returned corrupt data for storage pool %1. As a result the pool will be inaccessible. Return Code: %2\r\n
0xb0000066 | Majority of the physical drives of storage pool %1 failed a configuration update, which caused the pool to go into a failed state. Return Code: %2\r\n
0xb0000067 | The capacity consumption of the storage pool %1 has exceeded the threshold limit set on the pool. Return Code: %2\r\n
0xb0000068 | The capacity consumption of the storage pool %1 is now below the threshold limit set on the pool. Return Code: %2\r\n
0xb00000c8 | Windows was unable to read the drive header for physical drive %1. If you know the drive is still usable, then resetting the drive health by using command line or GUI may clear this failure condition and enable you to reassign the drive to its storage pool. Return Code: %2\r\n
0xb00000c9 | Physical drive %1 has invalid meta-data. Resetting the health status, using command line or GUI, might bring the physical drive to the primordial pool. Return Code: %2\r\n
0xb00000ca | Physical drive %1 has invalid meta-data. Resetting the health status, using command line or GUI, might resolve the issue. Return Code: %2\r\n
0xb00000cb | Physical drive %1 failed an IO operation. Return Code: %2. Additional related events may be found in the System event log for Disk %3.\n                 %n\n                 %nThis drive may need to be replaced. To view its reliability counters, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\n                 %n\n                 %nThis drive may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %4\n                 %nDrive Model Number: %5\n                 %nDrive Serial Number: %6\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nIf this drive is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %7\n                 %nEnclosure Model Number: %8\n                 %nEnclosure Serial Number: %9\n                 %nEnclosure Slot: %10\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cc | Physical drive %1 is reporting an impending failure. Sense Code (KEY ASC/ASCQ): %2 %3/%4. Additional related events may be found in the System event log for Disk %5.\n                 %n\n                 %nThis drive may need to be replaced. To view its reliability counters, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\n                 %n\n                 %nThis drive may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %6\n                 %nDrive Model Number: %7\n                 %nDrive Serial Number: %8\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nIf this drive is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %9\n                 %nEnclosure Model Number: %10\n                 %nEnclosure Serial Number: %11\n                 %nEnclosure Slot: %12\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb000012c | Physical drive %1 failed to read the configuration or returned corrupt data for storage space %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb000012d | All pool drives failed to read the configuration or returned corrupt data for storage space %1. As a result the storage space will not attach. Return Code: %2\r\n
0xb000012e | Majority of the pool drives hosting space meta-data for storage space %1 failed a space meta-data update, which caused the storage pool to go in failed state. Return Code: %2\r\n
0xb000012f | Drives hosting data for storage space %1 have failed or are missing. As a result, no copy of data is available. Return Code: %2\r\n
0xb0000130 | One or more drives hosting data for storage space %1 have failed or are missing. As a result, at least one copy of data is not available. However, at least one copy of data is still available. Return Code: %2\r\n
0xb0000132 | The attempt to map, or allocate more storage for, the storage space %1 has failed. This is because there was a write failure involved in the updating the storage space metadata. Return Code: %2\r\n
0xb0000133 | The attempt to unmap or trim the storage space %1 has failed. Return Code: %2\r\n
0xb0000134 | A repair attempt for storage space %1 was initiated by the driver. Return Code: %2\r\n
0xb0000135 | Storage space %1 was detached due to an unexpected error. Return Code: %2\r\n
0xb00003e8 | %1 %2 %3 %4 %5 %6 %7 %8\r\n
0xb00003e9 | %1 %2 %3 %4 %5 %6 %7\r\n
0xb00003ea | %1 %2 %3 %4 %5 %6 %7 %8 %9 %10 %11 %12 %13 %14 %15 %16 %17 %18 %19\r\n
0xb00003eb | %1 %2 %3 %4 %5 %6\r\n
0xb00003ec | %1 %2 %3 %4\r\n
0xb000044c | %1 %2 %3 %4 %5 %6 %7 %8\r\n
0xb000044d | %1 %2 %3 %4 %5 %6 %7 %8 %9 %10 %11 %12 %13\r\n
0xb00004b0 | %1 %2 %3\r\n
0xb0000514 | %1 %2 %3\r\n

### 6.3.9600.18573

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000064 | Physical drive %1 failed to read the configuration or returned corrupt data for storage pool %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb0000066 | Majority of the physical disks of storage pool %1 failed a configuration update, which caused the pool to go into a failed state. Return Code: %2\r\n
0xb0000067 | The capacity consumption of the storage pool %1 has exceeded the threshold limit set on the pool. Return Code: %2\r\n
0xb0000068 | The capacity consumption of the storage pool %1 is now below the threshold limit set on the pool. Return Code: %2\r\n
0xb00000c8 | Windows was unable to read the disk header for physical disk %1. If you know the disk is still usable, then resetting the disk health by using command line or GUI may clear this failure condition and enable you to reassign the disk to its storage pool. Return Code: %2\r\n
0xb00000c9 | Physical drive %1 has invalid meta-data. Resetting the health status, using command line or GUI, might bring the physical drive to the primordial pool. Return Code: %2\r\n
0xb00000ca | Physical disk %1 has invalid meta-data. Resetting the health status, using command line or GUI, might resolve the issue. Return Code: %2\r\n
0xb00000cb | Physical disk %1 failed an IO operation. Return Code: %2. Additional related events may be found in the System event log for Disk %3.\n                 %n\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\n                 %n\n                 %nThis disk may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %4\n                 %nDrive Model Number: %5\n                 %nDrive Serial Number: %6\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nIf this disk is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %7\n                 %nEnclosure Model Number: %8\n                 %nEnclosure Serial Number: %9\n                 %nEnclosure Slot: %10\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cc | Physical disk %1 is reporting an impending failure. Sense Code (KEY ASC/ASCQ): %2 %3/%4. Additional related events may be found in the System event log for Disk %5.\n                 %n\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\n                 %n\n                 %nThis disk may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %6\n                 %nDrive Model Number: %7\n                 %nDrive Serial Number: %8\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nIf this disk is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %9\n                 %nEnclosure Model Number: %10\n                 %nEnclosure Serial Number: %11\n                 %nEnclosure Slot: %12\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cd | Windows lost communication with physical disk %1. This can occur if a cable failed or was disconnected, or if the disk itself failed.\n                 %n\n                 %nThis disk may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %2\n                 %nDrive Model Number: %3\n                 %nDrive Serial Number: %4\n                 %n\n                 %nIf this disk is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %5\n                 %nEnclosure Model Number: %6\n                 %nEnclosure Serial Number: %7\n                 %nEnclosure Slot: %8\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nTo view the virtual disks affected, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-VirtualDisk\r\n
0xb00000ce | Physical disk %1 was auto-retired.\r\n
0xb000012c | Physical disk %1 failed to read the configuration or returned corrupt data for virtual disk %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb000012d | All pool disks failed to read the configuration or returned corrupt data for virtual disk %1. As a result the virtual disk will not attach. Return Code: %2\r\n
0xb000012e | Majority of the pool disks hosting space meta-data for virtual disk %1 failed a space meta-data update, which caused the storage pool to go in failed state. Return Code: %2\r\n
0xb000012f | Drives hosting data for virtual disk %1 have failed or are missing. As a result, no copy of data is available. Return Code: %2\r\n
0xb0000130 | The virtual disk %1 is in a degraded state. This can happen when a physical disk hosting the virtual disk fails, is disconnected, or experiences a write error.\n                 %n\n                 %nWindows will attempt to repair the virtual disk. No action is needed at this time.\r\n
0xb0000131 | Virtual disk %1 is now healthy.\r\n
0xb0000132 | The attempt to map, or allocate more storage for, the virtual disk %1 has failed. This is because there was a write failure involved in the updating the virtual disk metadata. Return Code: %2\r\n
0xb0000133 | The attempt to unmap or trim the virtual disk %1 has failed. Return Code: %2\r\n
0xb0000135 | Virtual disk %1 was detached due to an unexpected error. Return Code: %2\r\n
0xb0000136 | The attempt to allocate more storage for the virtual disk %1 has failed.\n                 %n\n                 %nCheck the available capacity of the virutual disk; you may need to add additional\n                 %nphysical capacity to the pool.\n                 %n\n                 %nOnce you have resolved the condition listed above,\n                 %nyou can online the disk by using the following commands in PowerShell: \n                 %n\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000137 | Virtual disk %1 requires a data integrity scan.\n                 %n\n                 %nData on the disk is out-of-sync and a data integrity scan is required.\n                 %nTo start the scan, run the following command:\n                 %n\n                 %nGet-ScheduledTask -TaskName "Data Integrity Scan for Crash Recovery" | Start-ScheduledTask\n                 %n\n                 %nOnce you have resolved the condition listed above,\n                 %nyou can online the disk by using the following commands in PowerShell: \n                 %n\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000138 | Virtual disk %1 has failed a write operation to all its copies.\n                 %n\n                 %nYou can online the disk by using the following commands in PowerShell: \n                 %n\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000139 | Virtual disk %1 could not be repaired because there is not enough free space in the storage pool.\n                 %n\n                 %nReplace any failed or disconnected physical disks. The virtual disk will then be repaired automatically or you can repair it by running this command in PowerShell:\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Repair-VirtualDisk\r\n
0xb0000190 | A path to storage enclosure %1 has been detected. The number of available paths is %2.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %3\n                 %nModel Number: %4\n                 %nSerial Number: %5\n                 %nFirmware Version: %6\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000191 | A path to storage enclosure %1 has been removed. The number of remaining paths is %2.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %3\n                 %nModel Number: %4\n                 %nSerial Number: %5\n                 %nFirmware Version: %6\r\n
0xb0000192 | The health of storage enclosure %1 has changed from %2 to %3.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %4\n                 %nModel Number: %5\n                 %nSerial Number: %6\n                 %nFirmware Version: %7\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000193 | A storage enclosure failed to initialize. Return Code: %1.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %2\n                 %nModel Number: %3\n                 %nSerial Number: %4\n                 %nFirmware Version: %5\r\n
0xb00003e8 | For internal use.\r\n
0xb00003ed | Operation started.\r\n
0xb00003ee | Operation completed.\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | Unhealthy\r\n
0xd0000003 | Warning\r\n
0xd0000004 | Healthy\r\n
0xd0000005 | SpacePrepare\r\n
0xd0000006 | SpaceFlush\r\n
0xd0000007 | SpaceDsm\r\n
0xd0000008 | TaskPrepare\r\n
0xd0000009 | SpanIo\r\n
0xd000000a | RaidRead\r\n
0xd000000b | RaidWrite\r\n
0xd000000c | RaidRegenerate\r\n
0xd000000d | RaidScrub\r\n
0xd000000e | RaidRepair\r\n
0xd000000f | RaidDestageRead\r\n
0xd0000010 | RaidDestageWrite\r\n
0xd0000011 | RaidReplay\r\n
0xd0000012 | Raid1ReadUnit\r\n
0xd0000013 | Raid1PrepareWrite\r\n
0xd0000014 | Raid1WriteCopies\r\n
0xd0000015 | Raid5ReadUnit\r\n
0xd0000016 | Raid5Reconstruct\r\n
0xd0000017 | Raid5WriteUnit\r\n
0xd0000018 | Raid5WriteMultiple\r\n
0xd0000019 | Raid5WriteParity\r\n
0xd000001a | DrtRead\r\n
0xd000001b | DrtWrite\r\n
0xd000001c | LogRead\r\n
0xd000001d | LogWrite\r\n
0xd000001e | 26\r\n
0xd000001f | Normal\r\n
0xd0000020 | NoRecovery\r\n
0xd0000021 | Recover\r\n
0xd0000022 | Repair\r\n
0xd0000023 | Writeback\r\n
0xd0000024 | Log\r\n
0xd0000025 | LogMetadata\r\n
0xd0000026 | LogData\r\n
0xd0000027 | LogDataScan\r\n
0xd0000028 | LogParity\r\n
0xd0000029 | LogParityScan\r\n
0xd000002a | LogCheckpoint\r\n
0xd000002b | LogBitmap\r\n
0xd000002c | Idle\r\n
0xd000002d | Ready\r\n
0xd000002e | Running\r\n
0xd000002f | Paused\r\n
0xd0000030 | Abandoned\r\n
0xd0000031 | Complete\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000066 | Majority of the physical disks of storage pool %1 failed a configuration update, which caused the pool to go into a failed state. Return Code: %2\r\n
0xb0000067 | The capacity consumption of the storage pool %1 has exceeded the threshold limit set on the pool. Return Code: %2\r\n
0xb0000068 | The capacity consumption of the storage pool %1 is now below the threshold limit set on the pool. Return Code: %2\r\n
0xb00000c8 | Windows was unable to read the disk header for physical disk %1. If you know the disk is still usable, then resetting the disk health by using command line or GUI may clear this failure condition and enable you to reassign the disk to its storage pool. Return Code: %2\r\n
0xb00000ca | Physical disk %1 has invalid meta-data. Resetting the health status, using command line or GUI, might resolve the issue. Return Code: %2\r\n
0xb00000cb | Physical disk %1 failed an IO operation. Return Code: %2. Additional related events may be found in the System event log for Disk %3.\n                 %n\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\n                 %n\n                 %nThis disk may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %4\n                 %nDrive Model Number: %5\n                 %nDrive Serial Number: %6\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nIf this disk is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %7\n                 %nEnclosure Model Number: %8\n                 %nEnclosure Serial Number: %9\n                 %nEnclosure Slot: %10\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cc | Physical disk %1 is reporting an impending failure. Sense Code (KEY ASC/ASCQ): %2 %3/%4. Additional related events may be found in the System event log for Disk %5.\n                 %n\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\n                 %n\n                 %nThis disk may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %6\n                 %nDrive Model Number: %7\n                 %nDrive Serial Number: %8\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nIf this disk is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %9\n                 %nEnclosure Model Number: %10\n                 %nEnclosure Serial Number: %11\n                 %nEnclosure Slot: %12\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cd | Windows lost communication with physical disk %1. This can occur if a cable failed or was disconnected, or if the disk itself failed.\n                 %n\n                 %nThis disk may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %2\n                 %nDrive Model Number: %3\n                 %nDrive Serial Number: %4\n                 %n\n                 %nIf this disk is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %5\n                 %nEnclosure Model Number: %6\n                 %nEnclosure Serial Number: %7\n                 %nEnclosure Slot: %8\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nTo view the virtual disks affected, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-VirtualDisk\r\n
0xb00000ce | Physical disk %1 was auto-retired.\r\n
0xb000012c | Physical disk %1 failed to read the configuration or returned corrupt data for virtual disk %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb000012d | All pool disks failed to read the configuration or returned corrupt data for virtual disk %1. As a result the virtual disk will not attach. Return Code: %2\r\n
0xb000012e | Majority of the pool disks hosting space meta-data for virtual disk %1 failed a space meta-data update, which caused the storage pool to go in failed state. Return Code: %2\r\n
0xb000012f | Drives hosting data for virtual disk %1 have failed or are missing. As a result, no copy of data is available at offset %3.\r\n
0xb0000130 | The virtual disk %1 is in a degraded state. This can happen when a physical disk hosting the virtual disk fails, is disconnected, or experiences a write error.\n                 %n\n                 %nWindows will attempt to repair the virtual disk. No action is needed at this time.\r\n
0xb0000131 | Virtual disk %1 is now healthy.\r\n
0xb0000132 | The attempt to map, or allocate more storage for, the virtual disk %1 has failed. This is because there was a write failure involved in the updating the virtual disk metadata. Return Code: %2\r\n
0xb0000133 | The attempt to unmap or trim the virtual disk %1 has failed. Return Code: %2\r\n
0xb0000135 | Virtual disk %1 was detached due to an unexpected error. Return Code: %2\r\n
0xb0000136 | The attempt to allocate more storage for the virtual disk %1 has failed.\n                 %n\n                 %nCheck the available capacity of the virutual disk; you may need to add additional\n                 %nphysical capacity to the pool.\n                 %n\n                 %nOnce you have resolved the condition listed above,\n                 %nyou can online the disk by using the following commands in PowerShell:\n                 %n\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000137 | Virtual disk %1 requires a data integrity scan.\n                 %n\n                 %nData on the disk is out-of-sync and a data integrity scan is required.\n                 %nTo start the scan, run the following command:\n                 %n\n                 %nGet-ScheduledTask -TaskName "Data Integrity Scan for Crash Recovery" | Start-ScheduledTask\n                 %n\n                 %nOnce you have resolved the condition listed above,\n                 %nyou can online the disk by using the following commands in PowerShell:\n                 %n\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000138 | Virtual disk %1 has failed a write operation to all its copies.\n                 %n\n                 %nYou can online the disk by using the following commands in PowerShell:\n                 %n\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000139 | Virtual disk %1 could not be repaired because there is not enough free space in the storage pool.\n                 %n\n                 %nReplace any failed or disconnected physical disks. The virtual disk will then be repaired automatically or you can repair it by running this command in PowerShell:\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Repair-VirtualDisk\r\n
0xb0000190 | A path to storage enclosure %1 has been detected. The number of available paths is %2.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %3\n                 %nModel Number: %4\n                 %nSerial Number: %5\n                 %nFirmware Version: %6\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000191 | A path to storage enclosure %1 has been removed. The number of remaining paths is %2.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %3\n                 %nModel Number: %4\n                 %nSerial Number: %5\n                 %nFirmware Version: %6\r\n
0xb0000192 | The health of storage enclosure %1 has changed from %2 to %3.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %4\n                 %nModel Number: %5\n                 %nSerial Number: %6\n                 %nFirmware Version: %7\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000193 | A storage enclosure failed to initialize. Return Code: %1.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %2\n                 %nModel Number: %3\n                 %nSerial Number: %4\n                 %nFirmware Version: %5\r\n
0xb00003e8 | For internal use.\r\n
0xb00003ed | Operation started.\r\n
0xb00003ee | Operation completed.\r\n
0xb00008fc | Read cache operation completed.\n                 %nId: %1\n                 %nOperation/Function: %2\n                 %nLength: %3\n                 %nDisk Offset: %4\n                 %nRelative Offset: %5\n                 %nCache Offset: %6\n                 %nStatus: %7\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | Unhealthy\r\n
0xd0000003 | Warning\r\n
0xd0000004 | Healthy\r\n
0xd0000005 | Auto\r\n
0xd0000006 | Enabled\r\n
0xd0000007 | Disabled\r\n
0xd0000008 | SpacePrepare\r\n
0xd0000009 | SpaceFlush\r\n
0xd000000a | SpaceDsm\r\n
0xd000000b | TaskPrepare\r\n
0xd000000c | SpanIo\r\n
0xd000000d | RaidRead\r\n
0xd000000e | RaidWrite\r\n
0xd000000f | RaidRegenerate\r\n
0xd0000010 | RaidScrub\r\n
0xd0000011 | RaidRepair\r\n
0xd0000012 | RaidDestageRead\r\n
0xd0000013 | RaidDestageWrite\r\n
0xd0000014 | RaidReplay\r\n
0xd0000015 | Raid1ReadUnit\r\n
0xd0000016 | Raid1PrepareWrite\r\n
0xd0000017 | Raid1WriteCopies\r\n
0xd0000018 | Raid5ReadUnit\r\n
0xd0000019 | Raid5Reconstruct\r\n
0xd000001a | Raid5WriteUnit\r\n
0xd000001b | Raid5WriteMultiple\r\n
0xd000001c | Raid5WriteParity\r\n
0xd000001d | DrtRead\r\n
0xd000001e | DrtWrite\r\n
0xd000001f | LogRead\r\n
0xd0000020 | LogWrite\r\n
0xd0000021 | 26\r\n
0xd0000022 | Normal\r\n
0xd0000023 | NoRecovery\r\n
0xd0000024 | Recover\r\n
0xd0000025 | Repair\r\n
0xd0000026 | Writeback\r\n
0xd0000027 | Log\r\n
0xd0000028 | LogMetadata\r\n
0xd0000029 | LogData\r\n
0xd000002a | LogDataScan\r\n
0xd000002b | LogParity\r\n
0xd000002c | LogParityScan\r\n
0xd000002d | LogCheckpoint\r\n
0xd000002e | LogBitmap\r\n
0xd000002f | Idle\r\n
0xd0000030 | Ready\r\n
0xd0000031 | Running\r\n
0xd0000032 | Paused\r\n
0xd0000033 | Abandoned\r\n
0xd0000034 | Complete\r\n
0xd0000035 | DoubleIncrement\r\n
0xd0000036 | SetPoolInfo\r\n
0xd0000037 | CreatePool\r\n
0xd0000038 | UpgradePool\r\n
0xd0000039 | RebalanceCleanup\r\n
0xd000003a | RebalancePhase1\r\n
0xd000003b | RebalancePhase2\r\n
0xd000003c | ScheduleRebalance\r\n
0xd000003d | SetDriveInfo\r\n
0xd000003e | AddDrives\r\n
0xd000003f | RemoveDrives\r\n
0xd0000040 | RemoveDrivesEstimate\r\n
0xd0000041 | SetDriveMetadata\r\n
0xd0000042 | SetSpaceInfo\r\n
0xd0000043 | CreateSpace\r\n
0xd0000044 | DeleteSpace\r\n
0xd0000045 | RepairPhase2\r\n
0xd0000046 | SetTierInfo\r\n
0xd0000047 | CreateTier\r\n
0xd0000048 | DeleteTier\r\n
0xd0000049 | MapExtents\r\n
0xd000004a | UnmapExtents\r\n
0xd000004b | UpdateSpaces\r\n
0xd000004c | Upgrade\r\n
0xd000004d | ResetDrive\r\n
0xd000004e | UpdateColumnState\r\n
0xd000004f | RepairPhase1\r\n
0xd0000050 | RepairPhase3\r\n
0xd0000051 | AddMetadataDrive\r\n
0xd0000052 | RemoveMetadataDrive\r\n
0xd0000053 | Trim\r\n

### 10.0.14393.0, 10.0.14393.351

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000066 | Majority of the physical disks of storage pool %1 failed a configuration update, which caused the pool to go into a failed state. Return Code: %2\r\n
0xb0000067 | The capacity consumption of the storage pool %1 has exceeded the threshold limit set on the pool. Return Code: %2\r\n
0xb0000068 | The capacity consumption of the storage pool %1 is now below the threshold limit set on the pool. Return Code: %2\r\n
0xb00000c8 | Windows was unable to read the disk header for physical disk %1. If you know the disk is still usable, then resetting the disk health by using command line or GUI may clear this failure condition and enable you to reassign the disk to its storage pool. Return Code: %2\r\n
0xb00000ca | Physical disk %1 has invalid meta-data. Resetting the health status, using command line or GUI, might resolve the issue. Return Code: %2\r\n
0xb00000cb | Physical disk %1 failed an IO operation. Return Code: %2. Additional related events may be found in the System event log for Disk %3.\n                 %n\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\n                 %n\n                 %nThis disk may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %4\n                 %nDrive Model Number: %5\n                 %nDrive Serial Number: %6\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nIf this disk is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %7\n                 %nEnclosure Model Number: %8\n                 %nEnclosure Serial Number: %9\n                 %nEnclosure Slot: %10\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cc | Physical disk %1 is reporting an impending failure. Sense Code (KEY ASC/ASCQ): %2 %3/%4. Additional related events may be found in the System event log for Disk %5.\n                 %n\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\n                 %n\n                 %nThis disk may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %6\n                 %nDrive Model Number: %7\n                 %nDrive Serial Number: %8\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nIf this disk is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %9\n                 %nEnclosure Model Number: %10\n                 %nEnclosure Serial Number: %11\n                 %nEnclosure Slot: %12\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cd | Windows lost communication with physical disk %1. This can occur if a cable failed or was disconnected, or if the disk itself failed.\n                 %n\n                 %nThis disk may be located using the following information:\n                 %n\n                 %nDrive Manufacturer: %2\n                 %nDrive Model Number: %3\n                 %nDrive Serial Number: %4\n                 %n\n                 %nIf this disk is in an enclosure, it may be located using the following information:\n                 %n\n                 %nEnclosure Manufacturer: %5\n                 %nEnclosure Model Number: %6\n                 %nEnclosure Serial Number: %7\n                 %nEnclosure Slot: %8\n                 %n\n                 %nMore information can be obtained using this PowerShell command:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\n                 %n\n                 %nTo view the virtual disks affected, run this command in PowerShell:\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-VirtualDisk\r\n
0xb00000ce | Physical disk %1 was auto-retired.\r\n
0xb000012c | Physical disk %1 failed to read the configuration or returned corrupt data for virtual disk %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb000012d | All pool disks failed to read the configuration or returned corrupt data for virtual disk %1. As a result the virtual disk will not attach. Return Code: %2\r\n
0xb000012e | Majority of the pool disks hosting space meta-data for virtual disk %1 failed a space meta-data update, which caused the storage pool to go in failed state. Return Code: %2\r\n
0xb000012f | Drives hosting data for virtual disk %1 have failed or are missing. As a result, no copy of data is available at offset %3.\r\n
0xb0000130 | The virtual disk %1 is in a degraded state. This can happen when a physical disk hosting the virtual disk fails, is disconnected, or experiences a write error.\n                 %n\n                 %nWindows will attempt to repair the virtual disk. No action is needed at this time.\r\n
0xb0000131 | Virtual disk %1 is now healthy.\r\n
0xb0000132 | The attempt to map, or allocate more storage for, the virtual disk %1 has failed. This is because there was a write failure involved in the updating the virtual disk metadata. Return Code: %2\r\n
0xb0000133 | The attempt to unmap or trim the virtual disk %1 has failed. Return Code: %2\r\n
0xb0000135 | Virtual disk %1 was detached due to an unexpected error. Return Code: %2\r\n
0xb0000136 | The attempt to allocate more storage for the virtual disk %1 has failed.\n                 %n\n                 %nCheck the available capacity of the virutual disk; you may need to add additional\n                 %nphysical capacity to the pool.\n                 %n\n                 %nOnce you have resolved the condition listed above,\n                 %nyou can online the disk by using the following commands in PowerShell:\n                 %n\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000137 | Virtual disk %1 requires a data integrity scan.\n                 %n\n                 %nData on the disk is out-of-sync and a data integrity scan is required.\n                 %nTo start the scan, run the following command:\n                 %n\n                 %nGet-ScheduledTask -TaskName "Data Integrity Scan for Crash Recovery" | Start-ScheduledTask\n                 %n\n                 %nOnce you have resolved the condition listed above,\n                 %nyou can online the disk by using the following commands in PowerShell:\n                 %n\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000138 | Virtual disk %1 has failed a write operation to all its copies.\n                 %n\n                 %nYou can online the disk by using the following commands in PowerShell:\n                 %n\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000139 | Virtual disk %1 could not be repaired because there is not enough free space in the storage pool.\n                 %n\n                 %nReplace any failed or disconnected physical disks. The virtual disk will then be repaired automatically or you can repair it by running this command in PowerShell:\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Repair-VirtualDisk\r\n
0xb0000190 | A path to storage enclosure %1 has been detected. The number of available paths is %2.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %3\n                 %nModel Number: %4\n                 %nSerial Number: %5\n                 %nFirmware Version: %6\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000191 | A path to storage enclosure %1 has been removed. The number of remaining paths is %2.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %3\n                 %nModel Number: %4\n                 %nSerial Number: %5\n                 %nFirmware Version: %6\r\n
0xb0000192 | The health of storage enclosure %1 has changed from %2 to %3.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %4\n                 %nModel Number: %5\n                 %nSerial Number: %6\n                 %nFirmware Version: %7\n                 %n\n                 %nIt may also be located by running this command in PowerShell:\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000193 | A storage enclosure failed to initialize. Return Code: %1.\n                 %nThis enclosure may be located using the following information:\n                 %n\n                 %nManufacturer: %2\n                 %nModel Number: %3\n                 %nSerial Number: %4\n                 %nFirmware Version: %5\r\n
0xb00003e8 | For internal use.\r\n
0xb00003ed | Operation started.\r\n
0xb00003ee | Operation completed.\r\n
0xb00008fc | Read cache operation completed.\n                 %nId: %1\n                 %nOperation/Function: %2\n                 %nLength: %3\n                 %nDisk Offset: %4\n                 %nRelative Offset: %5\n                 %nCache Offset: %6\n                 %nStatus: %7\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | Unhealthy\r\n
0xd0000003 | Warning\r\n
0xd0000004 | Healthy\r\n
0xd0000005 | Auto\r\n
0xd0000006 | Enabled\r\n
0xd0000007 | Disabled\r\n

### 10.0.15063.0, 10.0.16299.15, 10.0.17134.677, 10.0.17763.404, 10.0.17763.529, 10.0.18362.1, 10.0.18362.959

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000066 | Majority of the physical disks of storage pool %1 failed a configuration update, which caused the pool to go into a failed state. Return Code: %2\r\n
0xb0000067 | The capacity consumption of the storage pool %1 has exceeded the threshold limit set on the pool. Return Code: %2\r\n
0xb0000068 | The capacity consumption of the storage pool %1 is now below the threshold limit set on the pool. Return Code: %2\r\n
0xb00000c8 | Windows was unable to read the disk header for physical disk %1. If you know the disk is still usable, then resetting the disk health by using command line or GUI may clear this failure condition and enable you to reassign the disk to its storage pool. Return Code: %2\r\n
0xb00000ca | Physical disk %1 has invalid meta-data. Resetting the health status, using command line or GUI, might resolve the issue. Return Code: %2\r\n
0xb00000cb | Physical disk %1 failed an IO operation. Return Code: %2. Additional related events may be found in the System event log for Disk %3.\r\n                 %n\r\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\r\n                 %n\r\n                 %nThis disk may be located using the following information:\r\n                 %n\r\n                 %nDrive Manufacturer: %4\r\n                 %nDrive Model Number: %5\r\n                 %nDrive Serial Number: %6\r\n                 %n\r\n                 %nMore information can be obtained using this PowerShell command:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\r\n                 %n\r\n                 %nIf this disk is in an enclosure, it may be located using the following information:\r\n                 %n\r\n                 %nEnclosure Manufacturer: %7\r\n                 %nEnclosure Model Number: %8\r\n                 %nEnclosure Serial Number: %9\r\n                 %nEnclosure Slot: %10\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cc | Physical disk %1 is reporting an impending failure. Sense Code (KEY ASC/ASCQ): %2 %3/%4. Additional related events may be found in the System event log for Disk %5.\r\n                 %n\r\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\r\n                 %n\r\n                 %nThis disk may be located using the following information:\r\n                 %n\r\n                 %nDrive Manufacturer: %6\r\n                 %nDrive Model Number: %7\r\n                 %nDrive Serial Number: %8\r\n                 %n\r\n                 %nMore information can be obtained using this PowerShell command:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\r\n                 %n\r\n                 %nIf this disk is in an enclosure, it may be located using the following information:\r\n                 %n\r\n                 %nEnclosure Manufacturer: %9\r\n                 %nEnclosure Model Number: %10\r\n                 %nEnclosure Serial Number: %11\r\n                 %nEnclosure Slot: %12\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cd | Windows lost communication with physical disk %1. This can occur if a cable failed or was disconnected, or if the disk itself failed.\r\n                 %n\r\n                 %nThis disk may be located using the following information:\r\n                 %n\r\n                 %nDrive Manufacturer: %2\r\n                 %nDrive Model Number: %3\r\n                 %nDrive Serial Number: %4\r\n                 %n\r\n                 %nIf this disk is in an enclosure, it may be located using the following information:\r\n                 %n\r\n                 %nEnclosure Manufacturer: %5\r\n                 %nEnclosure Model Number: %6\r\n                 %nEnclosure Serial Number: %7\r\n                 %nEnclosure Slot: %8\r\n                 %n\r\n                 %nMore information can be obtained using this PowerShell command:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\r\n                 %n\r\n                 %nTo view the virtual disks affected, run this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-VirtualDisk\r\n
0xb00000ce | Physical disk %1 was auto-retired.\r\n
0xb000012c | Physical disk %1 failed to read the configuration or returned corrupt data for virtual disk %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb000012d | All pool disks failed to read the configuration or returned corrupt data for virtual disk %1. As a result the virtual disk will not attach. Return Code: %2\r\n
0xb000012e | Majority of the pool disks hosting space meta-data for virtual disk %1 failed a space meta-data update, which caused the storage pool to go in failed state. Return Code: %2\r\n
0xb000012f | Drives hosting data for virtual disk %1 have failed or are missing. As a result, no copy of data is available at offset %3.\r\n
0xb0000130 | The virtual disk %1 is in a degraded state. This can happen when a physical disk hosting the virtual disk fails, is disconnected, or experiences a write error.\r\n                 %n\r\n                 %nWindows will attempt to repair the virtual disk. No action is needed at this time.\r\n
0xb0000131 | Virtual disk %1 is now healthy.\r\n
0xb0000132 | The attempt to map, or allocate more storage for, the virtual disk %1 has failed. This is because there was a write failure involved in the updating the virtual disk metadata. Return Code: %2\r\n
0xb0000133 | The attempt to unmap or trim the virtual disk %1 has failed. Return Code: %2\r\n
0xb0000135 | Virtual disk %1 was detached due to an unexpected error. Return Code: %2\r\n
0xb0000136 | The attempt to allocate more storage for the virtual disk %1 has failed.\r\n                 %n\r\n                 %nCheck the available capacity of the virutual disk; you may need to add additional\r\n                 %nphysical capacity to the pool.\r\n                 %n\r\n                 %nOnce you have resolved the condition listed above,\r\n                 %nyou can online the disk by using the following commands in PowerShell:\r\n                 %n\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000137 | Virtual disk %1 requires a data integrity scan.\r\n                 %n\r\n                 %nData on the disk is out-of-sync and a data integrity scan is required.\r\n                 %nTo start the scan, run the following command:\r\n                 %n\r\n                 %nGet-ScheduledTask -TaskName "Data Integrity Scan for Crash Recovery" | Start-ScheduledTask\r\n                 %n\r\n                 %nOnce you have resolved the condition listed above,\r\n                 %nyou can online the disk by using the following commands in PowerShell:\r\n                 %n\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000138 | Virtual disk %1 has failed a write operation to all its copies.\r\n                 %n\r\n                 %nYou can online the disk by using the following commands in PowerShell:\r\n                 %n\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000139 | Virtual disk %1 could not be repaired because there is not enough free space in the storage pool.\r\n                 %n\r\n                 %nReplace any failed or disconnected physical disks. The virtual disk will then be repaired automatically or you can repair it by running this command in PowerShell:\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Repair-VirtualDisk\r\n
0xb0000190 | A path to storage enclosure %1 has been detected. The number of available paths is %2.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %3\r\n                 %nModel Number: %4\r\n                 %nSerial Number: %5\r\n                 %nFirmware Version: %6\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000191 | A path to storage enclosure %1 has been removed. The number of remaining paths is %2.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %3\r\n                 %nModel Number: %4\r\n                 %nSerial Number: %5\r\n                 %nFirmware Version: %6\r\n
0xb0000192 | The health of storage enclosure %1 has changed from %2 to %3.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %4\r\n                 %nModel Number: %5\r\n                 %nSerial Number: %6\r\n                 %nFirmware Version: %7\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000193 | A storage enclosure failed to initialize. Return Code: %1.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %2\r\n                 %nModel Number: %3\r\n                 %nSerial Number: %4\r\n                 %nFirmware Version: %5\r\n
0xb00003e8 | For internal use.\r\n
0xb00003ed | Operation started.\r\n
0xb00003ee | Operation completed.\r\n
0xb00008fc | Read cache operation completed.\r\n                 %nId: %1\r\n                 %nOperation/Function: %2\r\n                 %nLength: %3\r\n                 %nDisk Offset: %4\r\n                 %nRelative Offset: %5\r\n                 %nCache Offset: %6\r\n                 %nStatus: %7\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | Unhealthy\r\n
0xd0000003 | Warning\r\n
0xd0000004 | Healthy\r\n
0xd0000005 | Auto\r\n
0xd0000006 | Enabled\r\n
0xd0000007 | Disabled\r\n

### 10.0.19041.1, 10.0.19041.423

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000066 | Majority of the physical disks of storage pool %1 failed a configuration update, which caused the pool to go into a failed state. Return Code: %2\r\n
0xb0000067 | The capacity consumption of the storage pool %1 has exceeded the threshold limit set on the pool. Return Code: %2\r\n
0xb0000068 | The capacity consumption of the storage pool %1 is now below the threshold limit set on the pool. Return Code: %2\r\n
0xb00000c8 | Windows was unable to read the disk header for physical disk %1. If you know the disk is still usable, then resetting the disk health by using command line or GUI may clear this failure condition and enable you to reassign the disk to its storage pool. Return Code: %2\r\n
0xb00000ca | Physical disk %1 has invalid meta-data. Resetting the health status, using command line or GUI, might resolve the issue. Return Code: %2\r\n
0xb00000cb | Physical disk %1 failed an IO operation. Return Code: %2. Additional related events may be found in the System event log for Disk %3.\r\n                 %n\r\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\r\n                 %n\r\n                 %nThis disk may be located using the following information:\r\n                 %n\r\n                 %nDrive Manufacturer: %4\r\n                 %nDrive Model Number: %5\r\n                 %nDrive Serial Number: %6\r\n                 %n\r\n                 %nMore information can be obtained using this PowerShell command:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\r\n                 %n\r\n                 %nIf this disk is in an enclosure, it may be located using the following information:\r\n                 %n\r\n                 %nEnclosure Manufacturer: %7\r\n                 %nEnclosure Model Number: %8\r\n                 %nEnclosure Serial Number: %9\r\n                 %nEnclosure Slot: %10\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cc | Physical disk %1 is reporting an impending failure. Sense Code (KEY ASC/ASCQ): %2 %3/%4. Additional related events may be found in the System event log for Disk %5.\r\n                 %n\r\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\r\n                 %n\r\n                 %nThis disk may be located using the following information:\r\n                 %n\r\n                 %nDrive Manufacturer: %6\r\n                 %nDrive Model Number: %7\r\n                 %nDrive Serial Number: %8\r\n                 %n\r\n                 %nMore information can be obtained using this PowerShell command:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\r\n                 %n\r\n                 %nIf this disk is in an enclosure, it may be located using the following information:\r\n                 %n\r\n                 %nEnclosure Manufacturer: %9\r\n                 %nEnclosure Model Number: %10\r\n                 %nEnclosure Serial Number: %11\r\n                 %nEnclosure Slot: %12\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cd | Windows lost communication with physical disk %1. This can occur if a cable failed or was disconnected, or if the disk itself failed.\r\n                 %n\r\n                 %nThis disk may be located using the following information:\r\n                 %n\r\n                 %nDrive Manufacturer: %2\r\n                 %nDrive Model Number: %3\r\n                 %nDrive Serial Number: %4\r\n                 %n\r\n                 %nIf this disk is in an enclosure, it may be located using the following information:\r\n                 %n\r\n                 %nEnclosure Manufacturer: %5\r\n                 %nEnclosure Model Number: %6\r\n                 %nEnclosure Serial Number: %7\r\n                 %nEnclosure Slot: %8\r\n                 %n\r\n                 %nMore information can be obtained using this PowerShell command:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\r\n                 %n\r\n                 %nTo view the virtual disks affected, run this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-VirtualDisk\r\n
0xb00000ce | Physical disk %1 was auto-retired.\r\n
0xb00000cf | Physical disk %1 arrived.\r\n                 %nPool Id: %2\r\n                 %nDrive Number: %3\r\n                 %nDrive Manufacturer: %4\r\n                 %nDrive Model Number: %5\r\n                 %nDrive Serial Number: %6\r\n
0xb00000d0 | Physical disk %2 failed while arriving. Return Code: %1.\r\n                 %nPool Id: %3\r\n                 %nDrive Number: %4\r\n                 %nDrive Manufacturer: %5\r\n                 %nDrive Model Number: %6\r\n                 %nDrive Serial Number: %7\r\n
0xb000012c | Physical disk %1 failed to read the configuration or returned corrupt data for virtual disk %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb000012d | All pool disks failed to read the configuration or returned corrupt data for virtual disk %1. As a result the virtual disk will not attach. Return Code: %2\r\n
0xb000012e | Majority of the pool disks hosting space meta-data for virtual disk %1 failed a space meta-data update, which caused the storage pool to go in failed state. Return Code: %2\r\n
0xb000012f | Drives hosting data for virtual disk %1 have failed or are missing. As a result, no copy of data is available at offset %3.\r\n
0xb0000130 | The virtual disk %1 is in a degraded state. This can happen when a physical disk hosting the virtual disk fails, is disconnected, or experiences a write error.\r\n                 %n\r\n                 %nWindows will attempt to repair the virtual disk. No action is needed at this time.\r\n
0xb0000131 | Virtual disk %1 is now healthy.\r\n
0xb0000132 | The attempt to map, or allocate more storage for, the virtual disk %1 has failed. This is because there was a write failure involved in the updating the virtual disk metadata. Return Code: %2\r\n
0xb0000133 | The attempt to unmap or trim the virtual disk %1 has failed. Return Code: %2\r\n
0xb0000135 | Virtual disk %1 was detached due to an unexpected error. Return Code: %2\r\n
0xb0000136 | The attempt to allocate more storage for the virtual disk %1 has failed.\r\n                 %n\r\n                 %nCheck the available capacity of the virutual disk; you may need to add additional\r\n                 %nphysical capacity to the pool.\r\n                 %n\r\n                 %nOnce you have resolved the condition listed above,\r\n                 %nyou can online the disk by using the following commands in PowerShell:\r\n                 %n\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000137 | Virtual disk %1 requires a data integrity scan.\r\n                 %n\r\n                 %nData on the disk is out-of-sync and a data integrity scan is required.\r\n                 %nTo start the scan, run the following command:\r\n                 %n\r\n                 %nGet-ScheduledTask -TaskName "Data Integrity Scan for Crash Recovery" | Start-ScheduledTask\r\n                 %n\r\n                 %nOnce you have resolved the condition listed above,\r\n                 %nyou can online the disk by using the following commands in PowerShell:\r\n                 %n\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000138 | Virtual disk %1 has failed a write operation to all its copies.\r\n                 %n\r\n                 %nYou can online the disk by using the following commands in PowerShell:\r\n                 %n\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000139 | Virtual disk %1 could not be repaired because there is not enough free space in the storage pool.\r\n                 %n\r\n                 %nReplace any failed or disconnected physical disks. The virtual disk will then be repaired automatically or you can repair it by running this command in PowerShell:\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Repair-VirtualDisk\r\n
0xb0000190 | A path to storage enclosure %1 has been detected. The number of available paths is %2.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %3\r\n                 %nModel Number: %4\r\n                 %nSerial Number: %5\r\n                 %nFirmware Version: %6\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000191 | A path to storage enclosure %1 has been removed. The number of remaining paths is %2.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %3\r\n                 %nModel Number: %4\r\n                 %nSerial Number: %5\r\n                 %nFirmware Version: %6\r\n
0xb0000192 | The health of storage enclosure %1 has changed from %2 to %3.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %4\r\n                 %nModel Number: %5\r\n                 %nSerial Number: %6\r\n                 %nFirmware Version: %7\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000193 | A storage enclosure failed to initialize. Return Code: %1.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %2\r\n                 %nModel Number: %3\r\n                 %nSerial Number: %4\r\n                 %nFirmware Version: %5\r\n
0xb00003e8 | For internal use.\r\n
0xb00003ed | Operation started.\r\n
0xb00003ee | Operation completed.\r\n
0xb0000514 | Scrubbing %3 bytes at offset %2. Resiliency type %1. Out of %4 copies, %5 were in sync and %6 were unreadable due to media failures.\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | Unhealthy\r\n
0xd0000003 | Warning\r\n
0xd0000004 | Healthy\r\n
0xd0000005 | Auto\r\n
0xd0000006 | Enabled\r\n
0xd0000007 | Disabled\r\n
0xd0000008 | Simple\r\n
0xd0000009 | Mirror\r\n
0xd000000a | Parity\r\n

### 10.0.22000.71

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0xb0000066 | Majority of the physical disks of storage pool %1 failed a configuration update, which caused the pool to go into a failed state. Return Code: %2\r\n
0xb0000067 | The capacity consumption of the storage pool %1 has exceeded the threshold limit set on the pool. Return Code: %2\r\n
0xb0000068 | The capacity consumption of the storage pool %1 is now below the threshold limit set on the pool. Return Code: %2\r\n
0xb00000c8 | Windows was unable to read the disk header for physical disk %1. If you know the disk is still usable, then resetting the disk health by using command line or GUI may clear this failure condition and enable you to reassign the disk to its storage pool. Return Code: %2\r\n
0xb00000ca | Physical disk %1 has invalid meta-data. Resetting the health status, using command line or GUI, might resolve the issue. Return Code: %2\r\n
0xb00000cb | Physical disk %1 failed an IO operation. Return Code: %2. Additional related events may be found in the System event log for Disk %3.\r\n                 %n\r\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\r\n                 %n\r\n                 %nThis disk may be located using the following information:\r\n                 %n\r\n                 %nDrive Manufacturer: %4\r\n                 %nDrive Model Number: %5\r\n                 %nDrive Serial Number: %6\r\n                 %n\r\n                 %nMore information can be obtained using this PowerShell command:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\r\n                 %n\r\n                 %nIf this disk is in an enclosure, it may be located using the following information:\r\n                 %n\r\n                 %nEnclosure Manufacturer: %7\r\n                 %nEnclosure Model Number: %8\r\n                 %nEnclosure Serial Number: %9\r\n                 %nEnclosure Slot: %10\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cc | Physical disk %1 is reporting an impending failure. Sense Code (KEY ASC/ASCQ): %2 %3/%4. Additional related events may be found in the System event log for Disk %5.\r\n                 %n\r\n                 %nThis disk may need to be replaced. To view its reliability counters, run this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-StorageReliabilityCounter\r\n                 %n\r\n                 %nThis disk may be located using the following information:\r\n                 %n\r\n                 %nDrive Manufacturer: %6\r\n                 %nDrive Model Number: %7\r\n                 %nDrive Serial Number: %8\r\n                 %n\r\n                 %nMore information can be obtained using this PowerShell command:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\r\n                 %n\r\n                 %nIf this disk is in an enclosure, it may be located using the following information:\r\n                 %n\r\n                 %nEnclosure Manufacturer: %9\r\n                 %nEnclosure Model Number: %10\r\n                 %nEnclosure Serial Number: %11\r\n                 %nEnclosure Slot: %12\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Enable-PhysicalDiskIndication\r\n
0xb00000cd | Windows lost communication with physical disk %1. This can occur if a cable failed or was disconnected, or if the disk itself failed.\r\n                 %n\r\n                 %nThis disk may be located using the following information:\r\n                 %n\r\n                 %nDrive Manufacturer: %2\r\n                 %nDrive Model Number: %3\r\n                 %nDrive Serial Number: %4\r\n                 %n\r\n                 %nIf this disk is in an enclosure, it may be located using the following information:\r\n                 %n\r\n                 %nEnclosure Manufacturer: %5\r\n                 %nEnclosure Model Number: %6\r\n                 %nEnclosure Serial Number: %7\r\n                 %nEnclosure Slot: %8\r\n                 %n\r\n                 %nMore information can be obtained using this PowerShell command:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" }\r\n                 %n\r\n                 %nTo view the virtual disks affected, run this command in PowerShell:\r\n                 %nGet-PhysicalDisk | ?{ $_.ObjectId -Match "%1" } | Get-VirtualDisk\r\n
0xb00000ce | Physical disk %1 was auto-retired.\r\n
0xb00000cf | Physical disk %1 arrived.\r\n                 %nPool Id: %2\r\n                 %nDrive Number: %3\r\n                 %nDrive Manufacturer: %4\r\n                 %nDrive Model Number: %5\r\n                 %nDrive Serial Number: %6\r\n
0xb00000d0 | Physical disk %2 failed while arriving. Return Code: %1.\r\n                 %nPool Id: %3\r\n                 %nDrive Number: %4\r\n                 %nDrive Manufacturer: %5\r\n                 %nDrive Model Number: %6\r\n                 %nDrive Serial Number: %7\r\n
0xb000012c | Physical disk %1 failed to read the configuration or returned corrupt data for virtual disk %2. As a result the in-memory configuration may not be the most recent copy of configuration. Return Code: %3\r\n
0xb000012d | All pool disks failed to read the configuration or returned corrupt data for virtual disk %1. As a result the virtual disk will not attach. Return Code: %2\r\n
0xb000012e | Majority of the pool disks hosting space meta-data for virtual disk %1 failed a space meta-data update, which caused the storage pool to go in failed state. Return Code: %2\r\n
0xb000012f | Drives hosting data for virtual disk %1 have failed or are missing. As a result, no copy of data is available at offset %3.\r\n
0xb0000130 | The virtual disk %1 is in a degraded state. This can happen when a physical disk hosting the virtual disk fails, is disconnected, or experiences a write error.\r\n                 %n\r\n                 %nWindows will attempt to repair the virtual disk. No action is needed at this time.\r\n
0xb0000131 | Virtual disk %1 is now healthy.\r\n
0xb0000132 | The attempt to map, or allocate more storage for, the virtual disk %1 has failed. This is because there was a write failure involved in the updating the virtual disk metadata. Return Code: %2\r\n
0xb0000133 | The attempt to unmap or trim the virtual disk %1 has failed. Return Code: %2\r\n
0xb0000135 | Virtual disk %1 was detached due to an unexpected error. Return Code: %2\r\n
0xb0000136 | The attempt to allocate more storage for the virtual disk %1 has failed.\r\n                 %n\r\n                 %nCheck the available capacity of the virutual disk; you may need to add additional\r\n                 %nphysical capacity to the pool.\r\n                 %n\r\n                 %nOnce you have resolved the condition listed above,\r\n                 %nyou can online the disk by using the following commands in PowerShell:\r\n                 %n\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000137 | Virtual disk %1 requires a data integrity scan.\r\n                 %n\r\n                 %nData on the disk is out-of-sync and a data integrity scan is required.\r\n                 %nTo start the scan, run the following command:\r\n                 %n\r\n                 %nGet-ScheduledTask -TaskName "Data Integrity Scan for Crash Recovery" | Start-ScheduledTask\r\n                 %n\r\n                 %nOnce you have resolved the condition listed above,\r\n                 %nyou can online the disk by using the following commands in PowerShell:\r\n                 %n\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000138 | Virtual disk %1 has failed a write operation to all its copies.\r\n                 %n\r\n                 %nYou can online the disk by using the following commands in PowerShell:\r\n                 %n\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsReadOnly $false\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Get-Disk | Set-Disk -IsOffline  $false\r\n
0xb0000139 | Virtual disk %1 could not be repaired because there is not enough free space in the storage pool.\r\n                 %n\r\n                 %nReplace any failed or disconnected physical disks. The virtual disk will then be repaired automatically or you can repair it by running this command in PowerShell:\r\n                 %nGet-VirtualDisk | ?{ $_.ObjectId -Match "%1" } | Repair-VirtualDisk\r\n
0xb0000190 | A path to storage enclosure %1 has been detected. The number of available paths is %2.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %3\r\n                 %nModel Number: %4\r\n                 %nSerial Number: %5\r\n                 %nFirmware Version: %6\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000191 | A path to storage enclosure %1 has been removed. The number of remaining paths is %2.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %3\r\n                 %nModel Number: %4\r\n                 %nSerial Number: %5\r\n                 %nFirmware Version: %6\r\n
0xb0000192 | The health of storage enclosure %1 has changed from %2 to %3.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %4\r\n                 %nModel Number: %5\r\n                 %nSerial Number: %6\r\n                 %nFirmware Version: %7\r\n                 %n\r\n                 %nIt may also be located by running this command in PowerShell:\r\n                 %nGet-StorageEnclosure | ?{ $_.ObjectId -Match "%1" }\r\n
0xb0000193 | A storage enclosure failed to initialize. Return Code: %1.\r\n                 %nThis enclosure may be located using the following information:\r\n                 %n\r\n                 %nManufacturer: %2\r\n                 %nModel Number: %3\r\n                 %nSerial Number: %4\r\n                 %nFirmware Version: %5\r\n
0xb00001f5 | Spaceport KSR was initiated.\r\n
0xb00001f6 | Spaceport failed to save critical data during KSR. Return Code: %1.\r\n
0xb00001f7 | Spaceport failed to allocate persisted data during KSR.\r\n                 %nId: %1\r\n                 %nLength: %2.\r\n
0xb00001f8 | Spaceport failed to format persisted data during KSR.\r\n                 %nId: %1\r\n                 %nStatus: %2.\r\n
0xb00001f9 | Spaceport KSR was completed.\r\n
0xb00001fa | Spaceport failed to initialize persisted data from KSR.\r\n
0xb00001fb | Spaceport failed to claim persisted data block during KSR.\r\n                 %nBlockId: %1\r\n                 %nStatus: %2.\r\n
0xb00001fc | Spaceport failed to read disk header from persisted data.\r\n                 %nId: %1\r\n                 %nStatus: %2.\r\n
0xb00001fd | Spaceport failed to load configuration from persisted data.\r\n                 %nId: %1\r\n                 %nStatus: %2.\r\n
0xb00001fe | Spaceport failed to initialize DRT from persisted data.\r\n                 %nId: %1\r\n                 %nStatus: %2.\r\n
0xb00003e8 | Space %1 failed to initialize at %2:%3 with status %4.\r\n
0xb00003e9 | Pool %1 is beginning transaction %2 at sequence number %3.\r\n
0xb00003ea | Pool %1 completed transaction %2 with status %3 at sequence number %4.\r\n
0xb00003eb | Space %1 is beginning transaction %2 at sequence number %3.\r\n
0xb00003ec | Space %1 completed transaction %2 with status %3 at sequence number %4.\r\n
0xb00003ed | IOCTL %1 started.\r\n
0xb00003ee | IOCTL %1 completed with status %2.\r\n
0xb00003ef | Space %1 reallocated %2 extents. NeedCapacity: %3.\r\n
0xb00003f0 | Space %1 has started to regenerate.\r\n
0xb00003f1 | Space %1 has completed regenerating. %2 bytes processed, %3 bytes skipped.\r\n
0xb00003f2 | Space %1 failed to regenerate at offset %2, length %3.\r\n
0xb00003f3 | Request to update metadata drives for config %1.\r\n
0xb00003f4 | Updated metadata drives for config %1.\r\n
0xb00003f5 | Space %1 was unable to reallocate at offset %2.\r\n
0xb00003f9 | Waited %1 ms to acquire the global lock.\r\n
0xb00003fa | Held the global lock for %1 ms.\r\n
0xb00003fb | Log scan for space %1 log %2 copy %3 completed at offset %4 with status %5.\r\n
0xb00003fc | IO summary for enclosure %1. See details for additional information.\r\n
0xb00003fd | Space %1 attached at %2 taking %3 us.\r\n
0xb00003fe | Space %1 in pool %2 detached with reason %5 and status %6. This space was attached for %3 us and took %4 us to detach.\r\n
0xb00003ff | Space %1 attached with %2 entries in the DRT. Scrub is required to remove these entries.\r\n
0xb0000400 | Space %1 attached with no entries in the DRT. No scrub is needed.\r\n
0xb0000401 | All clean entries in the DRT for space %1 have been removed.  Current entries: %2. Flush status: %3. Write statuses: %4 %5.\r\n
0xb0000402 | Log advance failed for space %1, log %2, operation %3 with status %4.  Writes to this space may fail as a result.\r\n
0xb0000403 | Space %1 in pool %2 repair summary. See details for more information.\r\n
0xb0000404 | Repair pause state changed. Current pause count: %1, force: %2.\r\n
0xb0000405 | Space %2 in pool %1 failed to attach for reason %5 with status %6.  This space attempted attaching for %3 us and took %4 us to detach.\r\n
0xb0000406 | Space %1 failed to destage on operation %2 with status %3. Writes to this space may fail as a result.\r\n
0xb0000407 | Waited %1 ms to pause tasks, for PoolId: %2, current paused count: %3.\r\n
0xb0000408 | Tasks resumed after %1 ms, for PoolId: %2, current paused count: %3.\r\n
0xb0000409 | Waited %1 ms to acquire rundown exclusive lock, for space with PoolId: %2 and SpaceId: %3.\r\n
0xb000040a | Held the rundown exclusive lock for %1 ms, for space with PoolId: %2 and SpaceId: %3.\r\n
0xb000040b | Waited %1 ms to acquire mutex exclusively, for space with PoolId: %2 and SpaceId: %3.\r\n
0xb000040c | Held the mutex exclusively for %1 ms, for space with PoolId: %2 and SpaceId: %3.\r\n
0xb000044c | Config %1 loaded at sequence %4 with %3 paths present out of %2 total and path %5 as the primary.\r\n                   %nDuration: %6 us\r\n
0xb000044d | Config %1 failed to load with status %2.\r\n
0xb000044e | Path %2 arrived for config %1 with flags: %3.\r\n
0xb000044f | Path %2 removed from config %1.\r\n
0xb0000450 | Path %2 in config %1 synchronized.\r\n
0xb0000451 | Path %2 in config %1 failed to synchronize with status %3.\r\n
0xb0000452 | Path %2 in config %1 failed an IO with status %3.\r\n
0xb0000453 | Config %1 failed to commit a transaction at sequence %4 with status %5. %3 paths out of %2 are present. Witness status: %6.\r\n
0xb0000454 | Config %1 is inquorate. %3 paths out of %2 are present. Current sequence is %4 and witness sequence is %6. Witness status: %5.\r\n
0xb0000834 | For internal use.\r\n
0xb1010001 | Failed to initialize Storage Spaces API.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nCallee: %3\r\n                   %nError: %4\r\n
0xb1010003 | Failed to clean up Storage Spaces API.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nCallee: %3\r\n                   %nError: %4\r\n
0xb1010064 | The pool was created successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nName: %4\r\n                   %nCompatible Version: %5\r\n                   %nDrive Ids: %6\r\n                   %nDuration: %7 us\r\n
0xb1010065 | Failed to create the pool.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nName: %4\r\n                   %nCompatible Version: %5\r\n                   %nDrive Ids: %6\r\n                   %nCallee: %7\r\n                   %nError: %8\r\n
0xb1010066 | The pool was deleted successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nDuration: %4 us\r\n
0xb1010067 | Failed to delete the pool.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nCallee: %4\r\n                   %nError: %5\r\n
0xb1010069 | Failed to refresh the pool.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nCallee: %4\r\n                   %nError: %5\r\n
0xb10100c8 | The drive attributes were set successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nDrive Id: %3\r\n                   %nPersist: %4\r\n                   %nRelinquish Ownership: %5\r\n                   %nAttributes: %6\r\n                   %nAttributes Mask: %7\r\n                   %nOwner: %8\r\n                   %nDuration: %9 us\r\n
0xb10100c9 | Failed to set drive attributes.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nDrive Id: %3\r\n                   %nPersist: %4\r\n                   %nRelinquish Ownership: %5\r\n                   %nAttributes: %6\r\n                   %nAttributes Mask: %7\r\n                   %nOwner: %8\r\n                   %nCallee: %9\r\n                   %nError: %10\r\n
0xb10100ca | Maintenance was set on the drives successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nEnable: %4\r\n                   %nTimeout: %5 s\r\n                   %nDrive Ids: %6\r\n                   %nDuration: %7 us\r\n
0xb10100cb | Failed to set maintenance on the drives.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nEnable: %4\r\n                   %nTimeout: %5 s\r\n                   %nDrive Ids: %6\r\n                   %nCallee: %7\r\n                   %nError: %8\r\n
0xb10100cc | Maintenance was set on the drive successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nEnable: %4\r\n                   %nTimeout: %5 s\r\n                   %nDrive Id: %6\r\n                   %nDuration: %7 us\r\n
0xb10100cd | Failed to set maintenance on the drive.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nEnable: %4\r\n                   %nTimeout: %5 s\r\n                   %nDrive Id: %6\r\n                   %nCallee: %7\r\n                   %nError: %8\r\n
0xb10100ce | The drives were added successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nDrive Ids: %4\r\n                   %nDuration: %5 us\r\n
0xb10100cf | Failed to add the drives.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nDrive Ids: %4\r\n                   %nCallee: %5\r\n                   %nError: %6\r\n
0xb10100d0 | The drives were removed successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nDrive Ids: %4\r\n                   %nDuration: %5 us\r\n
0xb10100d1 | Failed to remove the drives.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nDrive Ids: %4\r\n                   %nCallee: %5\r\n                   %nError: %6\r\n
0xb10100d3 | Failed to refresh the drive.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nDrive Id: %3\r\n                   %nCallee: %4\r\n                   %nError: %5\r\n
0xb10100d4 | The drive was reset successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nDrive Id: %3\r\n                   %nDuration: %4 us\r\n
0xb10100d5 | Failed to reset the drive.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nDrive Id: %3\r\n                   %nCallee: %4\r\n                   %nError: %5\r\n
0xb10100d6 | The drive was prepared successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nDrive Id: %3\r\n                   %nDuration: %4 us\r\n
0xb10100d7 | Failed to prepare the drive.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nDrive Id: %3\r\n                   %nCallee: %4\r\n                   %nError: %5\r\n
0xb10100d8 | The drive was unprepared successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nDrive Id: %3\r\n                   %nDuration: %4 us\r\n
0xb10100d9 | Failed to unprepare the drive.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nDrive Id: %3\r\n                   %nCallee: %4\r\n                   %nError: %5\r\n
0xb101012c | The space was created successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nSpace Id: %4\r\n                   %nName: %5\r\n                   %nUsage: %6\r\n                   %nDuration: %7 us\r\n
0xb101012d | Failed to create the space.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nPool Id: %3\r\n                   %nSpace Id: %4\r\n                   %nName: %5\r\n                   %nUsage: %6\r\n                   %nCallee: %7\r\n                   %nError: %8\r\n
0xb101012e | The space was deleted successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nSpace Id: %3\r\n                   %nDuration: %4 us\r\n
0xb101012f | Failed to delete the space.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nSpace Id: %3\r\n                   %nCallee: %4\r\n                   %nError: %5\r\n
0xb1010130 | The space was attached successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nSpace Id: %3\r\n                   %nOwner Id: %4\r\n                   %nHidden: %5\r\n                   %nDuration: %6 us\r\n
0xb1010131 | Failed to attach the space.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nSpace Id: %3\r\n                   %nOwner Id: %4\r\n                   %nHidden: %5\r\n                   %nCallee: %6\r\n                   %nError: %7\r\n
0xb1010132 | The space was detached successfully.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nSpace Id: %3\r\n                   %nOwner Id: %4\r\n                   %nHidden: %5\r\n                   %nDuration: %6 us\r\n
0xb1010133 | Failed to detach the space.\r\n                   %nModule: %1\r\n                   %nFunction: %2\r\n                   %nSpace Id: %3\r\n                   %nOwner Id: %4\r\n                   %nHidden: %5\r\n                   %nCallee: %6\r\n                   %nError: %7\r\n
0xd0000001 | Unknown\r\n
0xd0000002 | Unhealthy\r\n
0xd0000003 | Warning\r\n
0xd0000004 | Healthy\r\n
0xd0000005 | Auto\r\n
0xd0000006 | Enabled\r\n
0xd0000007 | Disabled\r\n
0xd0000008 | Simple\r\n
0xd0000009 | Mirror\r\n
0xd000000a | Parity\r\n
0xd000000b | Unknown\r\n
0xd000000c | DoubleIncrement\r\n
0xd000000d | SetPoolInfo\r\n
0xd000000e | CreatePool\r\n
0xd000000f | UpgradePool\r\n
0xd0000010 | RebalanceCleanup\r\n
0xd0000011 | RebalancePhase1\r\n
0xd0000012 | RebalancePhase2\r\n
0xd0000013 | ScheduleRebalance\r\n
0xd0000014 | SetDriveInfo\r\n
0xd0000015 | AddDrives\r\n
0xd0000016 | RemoveDrives\r\n
0xd0000017 | RemoveDrivesEstimate\r\n
0xd0000018 | SetDriveMetadata\r\n
0xd0000019 | RetireDrives\r\n
0xd000001a | ReallocateDrives\r\n
0xd000001b | SetSpaceInfo\r\n
0xd000001c | CreateSpace\r\n
0xd000001d | GrowSpace\r\n
0xd000001e | FinalizeSpace\r\n
0xd000001f | DeleteSpace\r\n
0xd0000020 | SnapshotSpace\r\n
0xd0000021 | UnlinkSpace\r\n
0xd0000022 | RepairPhase2\r\n
0xd0000023 | RepairPhase5\r\n
0xd0000024 | SetActiveSpaces\r\n
0xd0000025 | SetSpacesFlags\r\n
0xd0000026 | SetTierInfo\r\n
0xd0000027 | CreateTier\r\n
0xd0000028 | DeleteTier\r\n
0xd0000029 | MapExtents\r\n
0xd000002a | UnmapExtents\r\n
0xd000002b | UpdateSpaces\r\n
0xd000002c | PrepareBoot\r\n
0xd000002d | Unknown\r\n
0xd000002e | DoubleIncrement\r\n
0xd000002f | Upgrade\r\n
0xd0000030 | ResetDrive\r\n
0xd0000031 | UpdateColumnState\r\n
0xd0000032 | RepairPhase0\r\n
0xd0000033 | RepairPhase1\r\n
0xd0000034 | RepairPhase3\r\n
0xd0000035 | RepairPhase6\r\n
0xd0000036 | MapExtents\r\n
0xd0000037 | AddMetadataDrive\r\n
0xd0000038 | RemoveMetadataDrive\r\n
0xd0000039 | Trim\r\n
0xd1000001 | Windows 8\r\n
0xd1000002 | Windows Blue Internal 1\r\n
0xd1000003 | Windows Blue Internal 2\r\n
0xd1000004 | Windows Blue Internal 3\r\n
0xd1000005 | Windows Blue Internal 4\r\n
0xd1000006 | Windows Blue Internal 5\r\n
0xd1000007 | Windows Blue\r\n
0xd1000008 | Windows Threshold Internal 1\r\n
0xd1000009 | Windows Threshold Internal 2\r\n
0xd100000a | Windows Threshold Internal 3\r\n
0xd100000b | ThresholdInternal4\r\n
0xd100000c | Windows Threshold Internal 5\r\n
0xd100000d | Windows Threshold Internal 6\r\n
0xd100000e | Windows Threshold\r\n
0xd100000f | Windows Threshold 2\r\n
0xd1000010 | Windows Redstone 1 Internal 1\r\n
0xd1000011 | Windows Redstone 1 Internal 2\r\n
0xd1000012 | Windows Redstone 1 Internal 3\r\n
0xd1000013 | Wwindows Redstone 1\r\n
0xd1000014 | Windows Redstone 3\r\n
0xd1000015 | Windows Redstone 5 Internal 1\r\n
0xd1000016 | Windows Redstone 5\r\n
0xd1000017 | Windows 19H1 Internal 1\r\n
0xd1000018 | Windows 19H1\r\n
0xd1000019 | Windows Vibranium\r\n
0xd100001a | Windows Manganese\r\n
0xd100001b | Config\r\n
0xd100001c | Data\r\n
0xd100001d | Journal\r\n
0xd100001e | Read Cache\r\n
0xd100001f | Write Cache\r\n
0xd1000020 | Dirty Region Tracking\r\n
0xd1000021 | Stripe State Tracking\r\n
0xd1000022 | Snapshot\r\n
0xd1000023 | Reserve\r\n
