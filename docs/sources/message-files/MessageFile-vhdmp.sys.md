## vhdmp.sys

Path: %SystemRoot%\system32\drivers\vhdmp.sys

### 6.1.7600.16385, 6.1.7601.17514

Message identifier | Message string
--- | ---
0x10000034 | SQM\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-VHDMP\r\n
0x90000002 | Microsoft-Windows-VHDMP/Operational\r\n
0x91000001 | Microsoft-Windows-VDRVROOT\r\n
0x91000002 | Microsoft-Windows-VDRVROOT/Operational\r\n
0xb0000001 | The VHD %1 has come online (surfaced) as disk number %2.\r\n
0xb0000002 | The VHD %1 has been removed (unsurfaced) as disk number %2.\r\n
0xb0000003 | Failed to surface VHD %1. Error status %2.\r\n
0xb0000004 | Failed to surface VHD %1. Surface attempt was cancelled.\r\n
0xb0000005 | Failed to %1 VHD %2. Error status %3.\r\n
0xb0000006 | Failed to %1 VHD %2. Error status %3.\r\n
0xb1000001 | The VHD HBA driver is registered with the root enumerator.\r\n
0xb1000002 | The VHD HBA driver is unregistered with the root enumerator.\r\n
0xd0000001 | write data to\r\n
0xd0000002 | read data from\r\n
0xd0000003 | Flush data to\r\n
0xd0000004 | Write block allocation table to\r\n
0xd0000005 | write sector bitmap to\r\n
0xd0000006 | read sector bitmap from\r\n

### 6.2.9200.16384, 6.3.9600.16384, 6.3.9600.18512

Message identifier | Message string
--- | ---
0x10000034 | SQM\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-VHDMP\r\n
0x90000002 | Microsoft-Windows-VHDMP/Operational\r\n
0x91000001 | Microsoft-Windows-VDRVROOT\r\n
0x91000002 | Microsoft-Windows-VDRVROOT/Operational\r\n
0xb0000001 | The VHD %1 has come online (surfaced) as disk number %2.\r\n
0xb0000002 | The VHD %1 has been removed (unsurfaced) as disk number %2.\r\n
0xb0000003 | Failed to surface VHD %1. Error status %2.\r\n
0xb0000004 | Failed to surface VHD %1. Surface attempt was cancelled.\r\n
0xb0000005 | Failed to %1 VHD %2. Error status %3.\r\n
0xb0000006 | Operation failed on VHD %2. %1 Error status %3.\r\n
0xb0000008 | Change Tracking has been enabled for the VHD %1 (%2) with log file %3.\r\n
0xb0000009 | Change Tracking has been disabled for the VHD %1 (%2).\r\n
0xb000000a | Change Tracking for the VHD %1 to the log file %2 has been stopped due to the error %3.\r\n
0xb000000b | Flushing of the header of the log file %1 has failed due to error %2.\r\n
0xb000000c | Flushing of the buffers to the log file %1 has failed due to error %2.\r\n
0xb000000d | Opening the log file %1 for tracking has failed due to error %2.\r\n
0xb000000e | Offline changes are detected for VHD %2. Log file: %1, VHD time: %4, Log file time: %5\r\n
0xb1000001 | The VHD HBA driver is registered with the root enumerator.\r\n
0xb1000002 | The VHD HBA driver is unregistered with the root enumerator.\r\n
0xd0000001 | Write failed.\r\n
0xd0000002 | Read failed.\r\n
0xd0000003 | Flush failed.\r\n
0xd0000004 | Offload write failed.\r\n
0xd0000005 | Offload read failed.\r\n
0xd0000006 | Offload abort failed.\r\n
0xd0000007 | Unmap failed.\r\n
0xd0000008 | Unable to get LBA status.\r\n
0xd0000009 | Unable to maintain write access during access check to network-backed virtual disk.\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x300000c8 | Starting an IO.\r\n
0x300000c9 | Completing an IO.\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000044d | IO request\r\n
0x90000001 | Microsoft-Windows-VHDMP\r\n
0x90000002 | Microsoft-Windows-VHDMP/Operational\r\n
0x91000001 | Microsoft-Windows-VDRVROOT\r\n
0x91000002 | Microsoft-Windows-VDRVROOT/Operational\r\n
0xb0000001 | The VHD %1 has come online (surfaced) as disk number %2.\r\n
0xb0000002 | The VHD %1 has been removed (unsurfaced) as disk number %2.\r\n
0xb0000003 | Failed to surface VHD %1. Error status %2.\r\n
0xb0000004 | Failed to surface VHD %1. Surface attempt was cancelled.\r\n
0xb0000005 | Failed to %1 VHD %2. Error status %3.\r\n
0xb0000006 | Operation failed on VHD %2. Operation type %1. Error status %3.\r\n
0xb0000007 | The Vhd Chain for VHD %4 is corrupted. The expected LastWriteGUID %2 (%3) did not match the parent's actual LastWriteGUID (%1).\r\n
0xb0000008 | The change tracking file for VHD %1 is corrupted and cannot be read. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb0000009 | The VHD file %1 has been modified without updating its associated change tracking file. Because the consistency of the change tracking information cannot be ensured, the change tracking data has been reset. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb000000a | Error %2 occured when attempting to update the change tracking file for VHD %1. This will invalidate the file's change tracking information. Change tracking will not be available for this VHD until change tracking is enabled again.\r\n
0xb000000b | Surface for VHD %2 is invalidated and will be removed (unsurfaced) because of a %1 operation failure with status %3.\r\n
0xb0000032 | Performing %1 VHD for %2 (target '%3').\r\n
0xb0000033 | Successfully performed %1 VHD %2.\r\n
0xb0000064 | Vhd resiliency initiated for %1 (VM ID: %2). A %3 IO failed with error %4.\r\n
0xb0000065 | Vhd resiliency successfully recovered %1 (VM ID: %2).\r\n
0xb0000066 | Vhd resiliency failed to recover %1 (VM ID: %2) with error %3.\r\n
0xb000006e | Recovery initiated for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb000006f | Recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000070 | Recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000071 | File %1 is invalidated (VM ID: %2) from current mode %3 with error %4. Any recovery in process will be failed and the virtual disk will be invalidated as well.\r\n
0xb0000072 | Waiting on file (%4) recovery for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb0000073 | Waiting on file (%4) recovery for %1 (VM ID: %2) completed with status %3.\r\n
0xb0000074 | File (%3) recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000075 | File (%4) recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb00000d0 | Change Tracking has been enabled for the VHD %1 (%2) with log file %3.\r\n
0xb00000d1 | Change Tracking has been disabled for the VHD %1 (%2).\r\n
0xb00000d2 | Change Tracking for the VHD %1 to the log file %2 has been stopped due to the error %3.\r\n
0xb00000d3 | Flushing of the header of the log file %1 has failed due to error %2.\r\n
0xb00000d4 | Flushing of the buffers to the log file %1 has failed due to error %2.\r\n
0xb00000d5 | Opening the log file %1 for tracking has failed due to error %2.\r\n
0xb00000d6 | Offline changes are detected for VHD %2. Log file: %1, VHD time: %4, Log file time: %5\r\n
0xb00003e9 | Starting an IO.\r\n
0xb00003ea | Completing an IO.\r\n
0xb00003f2 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery of this virtual disk has been initiated. If this IO was initiated by a VM then it will be internally retried later when the virtual disk has successfully recovered.\r\n
0xb00003f3 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery for this virtual disk could not be initiated either because this is not a recoverable failure or recovery has failed or the virtual disk is in an invalid state.\r\n
0xb1000001 | The VHD HBA driver is registered with the root enumerator.\r\n
0xb1000002 | The VHD HBA driver is unregistered with the root enumerator.\r\n
0xd0000001 | Write\r\n
0xd0000002 | Read\r\n
0xd0000003 | Flush\r\n
0xd0000004 | Offload write\r\n
0xd0000005 | Offload read\r\n
0xd0000006 | Project read\r\n
0xd0000007 | Project write\r\n
0xd0000008 | Unmap\r\n
0xd0000009 | Get LBA status\r\n
0xd000000a | File wrapper access check\r\n
0xd000000b | Storport\r\n
0xd000000c | Private\r\n
0xd000000d | Internal\r\n
0xd000000e | Mirror\r\n
0xd000000f | Read-only, shared\r\n
0xd0000010 | Read-only, exclusive\r\n
0xd0000011 | Read-write, exclusive\r\n
0xd0000012 | Invalid\r\n
0xd0000013 | Shared Reference\r\n
0xd0000014 | Exclusive Reference\r\n
0xd0000015 | QoS Reference\r\n

### 10.0.14393.0, 10.0.14393.447, 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x300000c8 | Starting an IO.\r\n
0x300000c9 | Completing an IO.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000044d | IO request\r\n
0x90000001 | Microsoft-Windows-VHDMP\r\n
0x90000002 | Microsoft-Windows-VHDMP/Operational\r\n
0x91000001 | Microsoft-Windows-VDRVROOT\r\n
0x91000002 | Microsoft-Windows-VDRVROOT/Operational\r\n
0xb0000001 | The VHD %1 has come online (surfaced) as disk number %2.\r\n
0xb0000002 | The VHD %1 has been removed (unsurfaced) as disk number %2.\r\n
0xb0000003 | Failed to surface VHD %1. Error status %2.\r\n
0xb0000004 | Failed to surface VHD %1. Surface attempt was cancelled.\r\n
0xb0000005 | Failed to %1 VHD %2. Error status %3.\r\n
0xb0000006 | Operation failed on VHD %2. Operation type %1. Error status %3.\r\n
0xb0000007 | The Vhd Chain for VHD %4 is corrupted. The expected LastWriteGUID %2 (%3) did not match the parent's actual LastWriteGUID (%1).\r\n
0xb0000008 | The change tracking file for VHD %1 is corrupted and cannot be read. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb0000009 | The VHD file %1 has been modified without updating its associated change tracking file. Because the consistency of the change tracking information cannot be ensured, the change tracking data has been reset. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb000000a | Error %2 occured when attempting to update the change tracking file for VHD %1. This will invalidate the file's change tracking information. Change tracking will not be available for this VHD until change tracking is enabled again.\r\n
0xb000000b | Surface for VHD %2 is invalidated and will be removed (unsurfaced) because of a %1 operation failure with status %3.\r\n
0xb0000032 | Performing %1 VHD for %2 (target '%3').\r\n
0xb0000033 | Successfully performed %1 VHD %2.\r\n
0xb0000064 | Vhd resiliency initiated for %1 (VM ID: %2). A %3 IO failed with error %4.\r\n
0xb0000065 | Vhd resiliency successfully recovered %1 (VM ID: %2).\r\n
0xb0000066 | Vhd resiliency failed to recover %1 (VM ID: %2) with error %3.\r\n
0xb000006e | Recovery initiated for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb000006f | Recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000070 | Recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000071 | File %1 is invalidated (VM ID: %2) from current mode %3 with error %4. Any recovery in process will be failed and the virtual disk will be invalidated as well.\r\n
0xb0000072 | Waiting on file (%4) recovery for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb0000073 | Waiting on file (%4) recovery for %1 (VM ID: %2) completed with status %3.\r\n
0xb0000074 | File (%3) recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000075 | File (%4) recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000076 | Failed to open file %1 with error %3. The file handle was previously invalidated due to a critical error. This operation will be retried periodically. (VM ID: %2).\r\n
0xb00000d0 | Change Tracking has been enabled for the VHD %1 (%2) with log file %3.\r\n
0xb00000d1 | Change Tracking has been disabled for the VHD %1 (%2).\r\n
0xb00000d2 | Change Tracking for the VHD %1 to the log file %2 has been stopped due to the error %3.\r\n
0xb00000d3 | Flushing of the header of the log file %1 has failed due to error %2.\r\n
0xb00000d4 | Flushing of the buffers to the log file %1 has failed due to error %2.\r\n
0xb00000d5 | Opening the log file %1 for tracking has failed due to error %2.\r\n
0xb00000d6 | Offline changes are detected for VHD %2. Log file: %1, VHD time: %4, Log file time: %5\r\n
0xb00003e9 | Starting an IO.\r\n
0xb00003ea | Completing an IO.\r\n
0xb00003f2 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery of this virtual disk has been initiated. If this IO was initiated by a VM then it will be internally retried later when the virtual disk has successfully recovered.\r\n
0xb00003f3 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery for this virtual disk could not be initiated either because this is not a recoverable failure or recovery has failed or the virtual disk is in an invalid state.\r\n
0xb1000001 | The VHD HBA driver is registered with the root enumerator.\r\n
0xb1000002 | The VHD HBA driver is unregistered with the root enumerator.\r\n
0xd0000001 | Write\r\n
0xd0000002 | Read\r\n
0xd0000003 | Flush\r\n
0xd0000004 | Offload write\r\n
0xd0000005 | Offload read\r\n
0xd0000006 | Project read\r\n
0xd0000007 | Project write\r\n
0xd0000008 | Unmap\r\n
0xd0000009 | Get LBA status\r\n
0xd000000a | File wrapper access check\r\n
0xd000000b | Storport\r\n
0xd000000c | Private\r\n
0xd000000d | Internal\r\n
0xd000000e | Mirror\r\n
0xd000000f | Read-only, shared\r\n
0xd0000010 | Read-only, exclusive\r\n
0xd0000011 | Read-write, exclusive\r\n
0xd0000012 | Invalid\r\n
0xd0000013 | Shared Reference\r\n
0xd0000014 | Exclusive Reference\r\n
0xd0000015 | QoS Reference\r\n

### 10.0.17134.619, 10.0.17763.292, 10.0.17763.557

Message identifier | Message string
--- | ---
0x300000c8 | Starting an IO.\r\n
0x300000c9 | Completing an IO.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000044d | IO request\r\n
0x90000001 | Microsoft-Windows-VHDMP\r\n
0x90000002 | Microsoft-Windows-VHDMP/Operational\r\n
0x91000001 | Microsoft-Windows-VDRVROOT\r\n
0x91000002 | Microsoft-Windows-VDRVROOT/Operational\r\n
0xb0000001 | The VHD %1 has come online (surfaced) as disk number %2.\r\n
0xb0000002 | The VHD %1 has been removed (unsurfaced) as disk number %2.\r\n
0xb0000003 | Failed to surface VHD %1. Error status %2.\r\n
0xb0000004 | Failed to surface VHD %1. Surface attempt was cancelled.\r\n
0xb0000005 | Failed to %1 VHD %2. Error status %3.\r\n
0xb0000006 | Operation failed on VHD %2. Operation type %1. Error status %3.\r\n
0xb0000007 | The Vhd Chain for VHD %4 is corrupted. The expected LastWriteGUID %2 (%3) did not match the parent's actual LastWriteGUID (%1).\r\n
0xb0000008 | The change tracking file for VHD %1 is corrupted and cannot be read. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb0000009 | The VHD file %1 has been modified without updating its associated change tracking file. Because the consistency of the change tracking information cannot be ensured, the change tracking data has been reset. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb000000a | Error %2 occured when attempting to update the change tracking file for VHD %1. This will invalidate the file's change tracking information. Change tracking will not be available for this VHD until change tracking is enabled again.\r\n
0xb000000b | Surface for VHD %2 is invalidated and will be removed (unsurfaced) because of a %1 operation failure with status %3.\r\n
0xb0000032 | Performing %1 VHD for %2 (target '%3').\r\n
0xb0000033 | Successfully performed %1 VHD %2.\r\n
0xb0000064 | Vhd resiliency initiated for %1 (VM ID: %2). A %3 IO failed with error %4.\r\n
0xb0000065 | Vhd resiliency successfully recovered %1 (VM ID: %2).\r\n
0xb0000066 | Vhd resiliency failed to recover %1 (VM ID: %2) with error %3.\r\n
0xb000006e | Recovery initiated for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb000006f | Recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000070 | Recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000071 | File %1 is invalidated (VM ID: %2) from current mode %3 with error %4. Any recovery in process will be failed and the virtual disk will be invalidated as well.\r\n
0xb0000072 | Waiting on file (%4) recovery for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb0000073 | Waiting on file (%4) recovery for %1 (VM ID: %2) completed with status %3.\r\n
0xb0000074 | File (%3) recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000075 | File (%4) recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000076 | Failed to open file %1 with error %3. The file handle was previously invalidated due to a critical error. This operation will be retried periodically. (VM ID: %2).\r\n
0xb0000077 | File %1 has been closed before initiating a recovery attempt. The file was open in mode %3. (VM ID: %2).\r\n
0xb0000078 | Recovery attempt initiated for virtual disk %1 (VM ID: %2).\r\n
0xb0000079 | Recovery attempt completed successfully for virtual disk %1 (VM ID: %2).\r\n
0xb000007a | Recovery attempt for virtual disk %1 failed with status %3 (VM ID: %2).\r\n
0xb000007b | Reopening handles to file %1 (VM ID: %2).\r\n
0xb000007c | Waiting for handles to file %1 to be reactivated (VM ID: %2).\r\n
0xb000007d | Recovery attempt completed for file %1 with status %3 (VM ID: %2).\r\n
0xb000007e | I/O failed with status %3 on file %1 (VM ID: %2).\r\n
0xb00000d0 | Change Tracking has been enabled for the VHD %1 (%2) with log file %3.\r\n
0xb00000d1 | Change Tracking has been disabled for the VHD %1 (%2).\r\n
0xb00000d2 | Change Tracking for the VHD %1 to the log file %2 has been stopped due to the error %3.\r\n
0xb00000d3 | Flushing of the header of the log file %1 has failed due to error %2.\r\n
0xb00000d4 | Flushing of the buffers to the log file %1 has failed due to error %2.\r\n
0xb00000d5 | Opening the log file %1 for tracking has failed due to error %2.\r\n
0xb00000d6 | Offline changes are detected for VHD %2. Log file: %1, VHD time: %4, Log file time: %5\r\n
0xb00003e9 | Starting an IO.\r\n
0xb00003ea | Completing an IO.\r\n
0xb00003f2 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery of this virtual disk has been initiated. If this IO was initiated by a VM then it will be internally retried later when the virtual disk has successfully recovered.\r\n
0xb00003f3 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery for this virtual disk could not be initiated either because this is not a recoverable failure or recovery has failed or the virtual disk is in an invalid state.\r\n
0xb1000001 | The VHD HBA driver is registered with the root enumerator.\r\n
0xb1000002 | The VHD HBA driver is unregistered with the root enumerator.\r\n
0xd0000001 | Write\r\n
0xd0000002 | Read\r\n
0xd0000003 | Flush\r\n
0xd0000004 | Offload write\r\n
0xd0000005 | Offload read\r\n
0xd0000006 | Project read\r\n
0xd0000007 | Project write\r\n
0xd0000008 | Unmap\r\n
0xd0000009 | Get LBA status\r\n
0xd000000a | File wrapper access check\r\n
0xd000000b | Storport\r\n
0xd000000c | Private\r\n
0xd000000d | Internal\r\n
0xd000000e | Mirror\r\n
0xd000000f | Read-only, shared\r\n
0xd0000010 | Read-only, exclusive\r\n
0xd0000011 | Read-write, exclusive\r\n
0xd0000012 | Invalid\r\n
0xd0000013 | Shared Reference\r\n
0xd0000014 | Exclusive Reference\r\n
0xd0000015 | QoS Reference\r\n

### 10.0.18362.1, 10.0.18362.657

Message identifier | Message string
--- | ---
0x300000c8 | Starting an IO.\r\n
0x300000c9 | Completing an IO.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000044d | IO request\r\n
0x90000001 | Microsoft-Windows-VHDMP\r\n
0x90000002 | Microsoft-Windows-VHDMP/Operational\r\n
0x91000001 | Microsoft-Windows-VDRVROOT\r\n
0x91000002 | Microsoft-Windows-VDRVROOT/Operational\r\n
0xb0000001 | The VHD %1 has come online (surfaced) as disk number %2.\r\n
0xb0000002 | The VHD %1 has been removed (unsurfaced) as disk number %2.\r\n
0xb0000003 | Failed to surface VHD %1. Error status %2.\r\n
0xb0000004 | Failed to surface VHD %1. Surface attempt was cancelled.\r\n
0xb0000005 | Failed to %1 VHD %2. Error status %3.\r\n
0xb0000006 | Operation failed on VHD %2. Operation type %1. Error status %3.\r\n
0xb0000007 | The Vhd Chain for VHD %4 is corrupted. The expected LastWriteGUID %2 (%3) did not match the parent's actual LastWriteGUID (%1).\r\n
0xb0000008 | The change tracking file for VHD %1 is corrupted and cannot be read. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb0000009 | The VHD file %1 has been modified without updating its associated change tracking file. Because the consistency of the change tracking information cannot be ensured, the change tracking data has been reset. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb000000a | Error %2 occured when attempting to update the change tracking file for VHD %1. This will invalidate the file's change tracking information. Change tracking will not be available for this VHD until change tracking is enabled again.\r\n
0xb000000b | Surface for VHD %2 is invalidated and will be removed (unsurfaced) because of a %1 operation failure with status %3.\r\n
0xb000000c | Handle for virtual disk '%2' created successfully. VM ID = %3, Type = %4, Version = %5, Flags = %6, AccessMask = %7, WriteDepth = %8, GetInfoOnly = %9, ReadOnly = %10, HandleContext = %11, VirtualDisk = %12.\r\n
0xb000000d | Failed to create handle for virtual disk '%2'. Status = %1, VM ID = %3, Type = %4, Version = %5, Flags = %6, AccessMask = %7, WriteDepth = %8, GetInfoOnly = %9, ReadOnly = %10, HandleContext = %11, VirtualDisk = %12.\r\n
0xb000000e | Virtual disk handle closed: HandleContext = %1, VirtualDisk = %2.\r\n
0xb000000f | Virtual disk object created: %1.\r\n
0xb0000010 | Virtual disk object destroyed: %1.\r\n
0xb0000011 | Virtual disk '%1' (no host access) has been surfaced.\r\n
0xb0000012 | Virtual disk '%1' (no host access) has been unsurfaced.\r\n
0xb0000032 | Performing %1 VHD for %2 (target '%3').\r\n
0xb0000033 | Successfully performed %1 VHD %2.\r\n
0xb0000064 | Vhd resiliency initiated for %1 (VM ID: %2). A %3 IO failed with error %4.\r\n
0xb0000065 | Vhd resiliency successfully recovered %1 (VM ID: %2).\r\n
0xb0000066 | Vhd resiliency failed to recover %1 (VM ID: %2) with error %3.\r\n
0xb000006e | Recovery initiated for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb000006f | Recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000070 | Recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000071 | File %1 is invalidated (VM ID: %2) from current mode %3 with error %4. Any recovery in process will be failed and the virtual disk will be invalidated as well.\r\n
0xb0000072 | Waiting on file (%4) recovery for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb0000073 | Waiting on file (%4) recovery for %1 (VM ID: %2) completed with status %3.\r\n
0xb0000074 | File (%3) recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000075 | File (%4) recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000076 | Failed to open file %1 with error %3. The file handle was previously invalidated due to a critical error. This operation will be retried periodically. (VM ID: %2).\r\n
0xb0000077 | File %1 has been closed before initiating a recovery attempt. The file was open in mode %3. (VM ID: %2).\r\n
0xb0000078 | Recovery attempt initiated for virtual disk %1 (VM ID: %2).\r\n
0xb0000079 | Recovery attempt completed successfully for virtual disk %1 (VM ID: %2).\r\n
0xb000007a | Recovery attempt for virtual disk %1 failed with status %3 (VM ID: %2).\r\n
0xb000007b | Reopening handles to file %1 (VM ID: %2).\r\n
0xb000007c | Waiting for handles to file %1 to be reactivated (VM ID: %2).\r\n
0xb000007d | Recovery attempt completed for file %1 with status %3 (VM ID: %2).\r\n
0xb000007e | I/O failed with status %3 on file %1 (VM ID: %2).\r\n
0xb00000d0 | Change Tracking has been enabled for the VHD %1 (%2) with log file %3.\r\n
0xb00000d1 | Change Tracking has been disabled for the VHD %1 (%2).\r\n
0xb00000d2 | Change Tracking for the VHD %1 to the log file %2 has been stopped due to the error %3.\r\n
0xb00000d3 | Flushing of the header of the log file %1 has failed due to error %2.\r\n
0xb00000d4 | Flushing of the buffers to the log file %1 has failed due to error %2.\r\n
0xb00000d5 | Opening the log file %1 for tracking has failed due to error %2.\r\n
0xb00000d6 | Offline changes are detected for VHD %2. Log file: %1, VHD time: %4, Log file time: %5\r\n
0xb00003e9 | Starting an IO.\r\n
0xb00003ea | Completing an IO.\r\n
0xb00003f2 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery of this virtual disk has been initiated. If this IO was initiated by a VM then it will be internally retried later when the virtual disk has successfully recovered.\r\n
0xb00003f3 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery for this virtual disk could not be initiated either because this is not a recoverable failure or recovery has failed or the virtual disk is in an invalid state.\r\n
0xb1000001 | The VHD HBA driver is registered with the root enumerator.\r\n
0xb1000002 | The VHD HBA driver is unregistered with the root enumerator.\r\n
0xd0000001 | Write\r\n
0xd0000002 | Read\r\n
0xd0000003 | Flush\r\n
0xd0000004 | Offload write\r\n
0xd0000005 | Offload read\r\n
0xd0000006 | Project read\r\n
0xd0000007 | Project write\r\n
0xd0000008 | Unmap\r\n
0xd0000009 | Get LBA status\r\n
0xd000000a | File wrapper access check\r\n
0xd000000b | Storport\r\n
0xd000000c | Private\r\n
0xd000000d | Internal\r\n
0xd000000e | Mirror\r\n
0xd000000f | Read-only, shared\r\n
0xd0000010 | Read-only, exclusive\r\n
0xd0000011 | Read-write, exclusive\r\n
0xd0000012 | Invalid\r\n
0xd0000013 | Shared Reference\r\n
0xd0000014 | Exclusive Reference\r\n
0xd0000015 | QoS Reference\r\n
0xd0000016 | Undefined\r\n
0xd0000017 | VHD\r\n
0xd0000018 | VHDX\r\n
0xd0000019 | ISO\r\n
0xd000001a | VHDSET\r\n

### 10.0.19041.84, 10.0.19041.610

Message identifier | Message string
--- | ---
0x10000001 | Activity\r\n
0x10000002 | IO\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000c8 | Starting an IO.\r\n
0x300000c9 | Completing an IO.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000044d | IO request\r\n
0x700004b1 | Virtual Disk Handle Create\r\n
0x700004b2 | Virtual Disk Handle Close\r\n
0x700004b3 | Filewrapper Handle Create\r\n
0x700004b4 | Filewrapper Handle Create\r\n
0x700004b5 | Surface Virtual Disk\r\n
0x700004b6 | Unsurface Virtual Disk\r\n
0x700004b7 | Cleanup Backing Store\r\n
0x700004b8 | Cleanup Backing Store Flush\r\n
0x90000001 | Microsoft-Windows-VHDMP\r\n
0x90000002 | Microsoft-Windows-VHDMP/Operational\r\n
0x91000001 | Microsoft-Windows-VDRVROOT\r\n
0x91000002 | Microsoft-Windows-VDRVROOT/Operational\r\n
0xb0000001 | The VHD %1 has come online (surfaced) as disk number %2.\r\n
0xb0000002 | The VHD %1 has been removed (unsurfaced) as disk number %2.\r\n
0xb0000003 | Failed to surface VHD %1. Error status %2.\r\n
0xb0000004 | Failed to surface VHD %1. Surface attempt was cancelled.\r\n
0xb0000005 | Failed to %1 VHD %2. Error status %3.\r\n
0xb0000006 | Operation failed on VHD %2. Operation type %1. Error status %3.\r\n
0xb0000007 | The Vhd Chain for VHD %4 is corrupted. The expected LastWriteGUID %2 (%3) did not match the parent's actual LastWriteGUID (%1).\r\n
0xb0000008 | The change tracking file for VHD %1 is corrupted and cannot be read. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb0000009 | The VHD file %1 has been modified without updating its associated change tracking file. Because the consistency of the change tracking information cannot be ensured, the change tracking data has been reset. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb000000a | Error %2 occured when attempting to update the change tracking file for VHD %1. This will invalidate the file's change tracking information. Change tracking will not be available for this VHD until change tracking is enabled again.\r\n
0xb000000b | Surface for VHD %2 is invalidated and will be removed (unsurfaced) because of a %1 operation failure with status %3.\r\n
0xb000000c | Handle for virtual disk '%2' created successfully. VM ID = %3, Type = %4, Version = %5, Flags = %6, AccessMask = %7, WriteDepth = %8, GetInfoOnly = %9, ReadOnly = %10, HandleContext = %11, VirtualDisk = %12.\r\n
0xb000000d | Failed to create handle for virtual disk '%2'. Status = %1, VM ID = %3, Type = %4, Version = %5, Flags = %6, AccessMask = %7, WriteDepth = %8, GetInfoOnly = %9, ReadOnly = %10, HandleContext = %11, VirtualDisk = %12.\r\n
0xb000000e | Virtual disk handle closed: HandleContext = %1, VirtualDisk = %2.\r\n
0xb000000f | Virtual disk object created: %1.\r\n
0xb0000010 | Virtual disk object destroyed: %1.\r\n
0xb0000011 | Virtual disk '%1' (no host access) has been surfaced.\r\n
0xb0000012 | Virtual disk '%1' (no host access) has been unsurfaced.\r\n
0xb0000015 | Starting to open handle for virtual disk.\r\n
0xb0000016 | Starting to create the handle for the file backing virtual disk '%1'.\r\n
0xb0000017 | Handle for the file backing virtual disk '%1' created successfully.\r\n
0xb0000018 | Failed to create handle for the file backing virtual disk '%1'. Status = %2.\r\n
0xb0000019 | Beginning to bring the VHD %1 online (surface).\r\n
0xb000001a | Beginning to remove the VHD %1 (unsurface).\r\n
0xb000001b | Starting to close the handle for the file backing virtual disk '%1'.\r\n
0xb000001c | Handle for the file backing virtual disk '%1' closed successfully.\r\n
0xb000001e | Starting to close virtual disk handle: HandleContext = %1, VirtualDisk = %2.\r\n
0xb000001f | Starting to cleanup the backing store for virtual disk '%1'.\r\n
0xb0000020 | Finished cleaning up the backing store for virtual disk '%1'.\r\n
0xb0000021 | Starting to flush the backing store footer for virtual disk '%1'.\r\n
0xb0000022 | Finished flushing the backing store footer for virtual disk '%1'.\r\n
0xb0000032 | Performing %1 VHD for %2 (target '%3').\r\n
0xb0000033 | Successfully performed %1 VHD %2.\r\n
0xb0000064 | Vhd resiliency initiated for %1 (VM ID: %2). A %3 IO failed with error %4.\r\n
0xb0000065 | Vhd resiliency successfully recovered %1 (VM ID: %2).\r\n
0xb0000066 | Vhd resiliency failed to recover %1 (VM ID: %2) with error %3.\r\n
0xb000006e | Recovery initiated for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb000006f | Recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000070 | Recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000071 | File %1 is invalidated (VM ID: %2) from current mode %3 with error %4. Any recovery in process will be failed and the virtual disk will be invalidated as well.\r\n
0xb0000072 | Waiting on file (%4) recovery for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb0000073 | Waiting on file (%4) recovery for %1 (VM ID: %2) completed with status %3.\r\n
0xb0000074 | File (%3) recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000075 | File (%4) recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000076 | Failed to open file %1 with error %3. The file handle was previously invalidated due to a critical error. This operation will be retried periodically. (VM ID: %2).\r\n
0xb0000077 | File %1 has been closed before initiating a recovery attempt. The file was open in mode %3. (VM ID: %2).\r\n
0xb0000078 | Recovery attempt initiated for virtual disk %1 (VM ID: %2).\r\n
0xb0000079 | Recovery attempt completed successfully for virtual disk %1 (VM ID: %2).\r\n
0xb000007a | Recovery attempt for virtual disk %1 failed with status %3 (VM ID: %2).\r\n
0xb000007b | Reopening handles to file %1 (VM ID: %2).\r\n
0xb000007c | Waiting for handles to file %1 to be reactivated (VM ID: %2).\r\n
0xb000007d | Recovery attempt completed for file %1 with status %3 (VM ID: %2).\r\n
0xb000007e | I/O failed with status %3 on file %1 (VM ID: %2).\r\n
0xb00000d0 | Change Tracking has been enabled for the VHD %1 (%2) with log file %3.\r\n
0xb00000d1 | Change Tracking has been disabled for the VHD %1 (%2).\r\n
0xb00000d2 | Change Tracking for the VHD %1 to the log file %2 has been stopped due to the error %3.\r\n
0xb00000d3 | Flushing of the header of the log file %1 has failed due to error %2.\r\n
0xb00000d4 | Flushing of the buffers to the log file %1 has failed due to error %2.\r\n
0xb00000d5 | Opening the log file %1 for tracking has failed due to error %2.\r\n
0xb00000d6 | Offline changes are detected for VHD %2. Log file: %1, VHD time: %4, Log file time: %5\r\n
0xb00003e9 | Starting an IO.\r\n
0xb00003ea | Completing an IO.\r\n
0xb00003f2 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery of this virtual disk has been initiated. If this IO was initiated by a VM then it will be internally retried later when the virtual disk has successfully recovered.\r\n
0xb00003f3 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery for this virtual disk could not be initiated either because this is not a recoverable failure or recovery has failed or the virtual disk is in an invalid state.\r\n
0xb1000001 | The VHD HBA driver is registered with the root enumerator.\r\n
0xb1000002 | The VHD HBA driver is unregistered with the root enumerator.\r\n
0xd0000001 | Write\r\n
0xd0000002 | Read\r\n
0xd0000003 | Flush\r\n
0xd0000004 | Offload write\r\n
0xd0000005 | Offload read\r\n
0xd0000006 | Project read\r\n
0xd0000007 | Project write\r\n
0xd0000008 | Unmap\r\n
0xd0000009 | Get LBA status\r\n
0xd000000a | File wrapper access check\r\n
0xd000000b | Storport\r\n
0xd000000c | Private\r\n
0xd000000d | Internal\r\n
0xd000000e | Mirror\r\n
0xd000000f | Read-only, shared\r\n
0xd0000010 | Read-only, exclusive\r\n
0xd0000011 | Read-write, exclusive\r\n
0xd0000012 | Invalid\r\n
0xd0000013 | Shared Reference\r\n
0xd0000014 | Exclusive Reference\r\n
0xd0000015 | QoS Reference\r\n
0xd0000016 | Undefined\r\n
0xd0000017 | VHD\r\n
0xd0000018 | VHDX\r\n
0xd0000019 | ISO\r\n
0xd000001a | VHDSET\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x10000001 | Activity\r\n
0x10000002 | IO\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x300000c8 | Starting an IO.\r\n
0x300000c9 | Completing an IO.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000044d | IO request\r\n
0x700004b1 | Virtual Disk Handle Create\r\n
0x700004b2 | Virtual Disk Handle Close\r\n
0x700004b3 | Filewrapper Handle Create\r\n
0x700004b4 | Filewrapper Handle Create\r\n
0x700004b5 | Surface Virtual Disk\r\n
0x700004b6 | Unsurface Virtual Disk\r\n
0x700004b7 | Cleanup Backing Store\r\n
0x700004b8 | Cleanup Backing Store Flush\r\n
0x90000001 | Microsoft-Windows-VHDMP\r\n
0x90000002 | Microsoft-Windows-VHDMP/Operational\r\n
0x91000001 | Microsoft-Windows-VDRVROOT\r\n
0x91000002 | Microsoft-Windows-VDRVROOT/Operational\r\n
0xb0000001 | The VHD %1 has come online (surfaced) as disk number %2.\r\n
0xb0000002 | The VHD %1 has been removed (unsurfaced) as disk number %2.\r\n
0xb0000003 | Failed to surface VHD %1. Error status %2.\r\n
0xb0000004 | Failed to surface VHD %1. Surface attempt was cancelled.\r\n
0xb0000005 | Failed to %1 VHD %2. Error status %3.\r\n
0xb0000006 | Operation failed on VHD %2. Operation type %1. Error status %3.\r\n
0xb0000007 | The Vhd Chain for VHD %4 is corrupted. The expected LastWriteGUID %2 (%3) did not match the parent's actual LastWriteGUID (%1).\r\n
0xb0000008 | The change tracking file for VHD %1 is corrupted and cannot be read. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb0000009 | The VHD file %1 has been modified without updating its associated change tracking file. Because the consistency of the change tracking information cannot be ensured, the change tracking data has been reset. No change tracking information will be available for this VHD, and change tracking will need to be enabled again before changed are tracked.\r\n
0xb000000a | Error %2 occured when attempting to update the change tracking file for VHD %1. This will invalidate the file's change tracking information. Change tracking will not be available for this VHD until change tracking is enabled again.\r\n
0xb000000b | Surface for VHD %2 is invalidated and will be removed (unsurfaced) because of a %1 operation failure with status %3.\r\n
0xb000000c | Handle for virtual disk '%2' created successfully. VM ID = %3, Type = %4, Version = %5, Flags = %6, AccessMask = %7, WriteDepth = %8, GetInfoOnly = %9, ReadOnly = %10, HandleContext = %11, VirtualDisk = %12.\r\n
0xb000000d | Failed to create handle for virtual disk '%2'. Status = %1, VM ID = %3, Type = %4, Version = %5, Flags = %6, AccessMask = %7, WriteDepth = %8, GetInfoOnly = %9, ReadOnly = %10, HandleContext = %11, VirtualDisk = %12.\r\n
0xb000000e | Virtual disk handle closed: HandleContext = %1, VirtualDisk = %2.\r\n
0xb000000f | Virtual disk object created: %1.\r\n
0xb0000010 | Virtual disk object destroyed: %1.\r\n
0xb0000011 | Virtual disk '%1' (no host access) has been surfaced.\r\n
0xb0000012 | Virtual disk '%1' (no host access) has been unsurfaced.\r\n
0xb0000015 | Starting to open handle for virtual disk.\r\n
0xb0000016 | Starting to create the handle for the file backing virtual disk '%1'.\r\n
0xb0000017 | Handle for the file backing virtual disk '%1' created successfully.\r\n
0xb0000018 | Failed to create handle for the file backing virtual disk '%1'. Status = %2.\r\n
0xb0000019 | Beginning to bring the VHD %1 online (surface).\r\n
0xb000001a | Beginning to remove the VHD %1 (unsurface).\r\n
0xb000001b | Starting to close the handle for the file backing virtual disk '%1'.\r\n
0xb000001c | Handle for the file backing virtual disk '%1' closed successfully.\r\n
0xb000001e | Starting to close virtual disk handle: HandleContext = %1, VirtualDisk = %2.\r\n
0xb000001f | Starting to cleanup the backing store for virtual disk '%1'.\r\n
0xb0000020 | Finished cleaning up the backing store for virtual disk '%1'.\r\n
0xb0000021 | Starting to flush the backing store footer for virtual disk '%1'.\r\n
0xb0000022 | Finished flushing the backing store footer for virtual disk '%1'.\r\n
0xb0000023 | Virtual disk '%1' (no host access) has been unsurfaced with unflushed data. Data corruption is possible if the virtual disk is surfaced again.\r\n
0xb0000024 | I/O cancellation (FastClose) started for file '%1'. (VM ID: %2)\r\n
0xb0000032 | Performing %1 VHD for %2 (target '%3').\r\n
0xb0000033 | Successfully performed %1 VHD %2.\r\n
0xb0000064 | Vhd resiliency initiated for %1 (VM ID: %2). A %3 IO failed with error %4.\r\n
0xb0000065 | Vhd resiliency successfully recovered %1 (VM ID: %2).\r\n
0xb0000066 | Vhd resiliency failed to recover %1 (VM ID: %2) with error %3.\r\n
0xb000006e | Recovery initiated for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb000006f | Recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000070 | Recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000071 | File %1 is invalidated (VM ID: %2) from current mode %3 with error %4. Any recovery in process will be failed and the virtual disk will be invalidated as well.\r\n
0xb0000072 | Waiting on file (%4) recovery for %1 (VM ID: %2) due to an IO failure with error %3.\r\n
0xb0000073 | Waiting on file (%4) recovery for %1 (VM ID: %2) completed with status %3.\r\n
0xb0000074 | File (%3) recovery succeeded for %1 (VM ID: %2).\r\n
0xb0000075 | File (%4) recovery failed for %1 (VM ID: %2) with error %3.\r\n
0xb0000076 | Failed to open file %1 with error %3. The file handle was previously invalidated due to a critical error. This operation will be retried periodically. (VM ID: %2).\r\n
0xb0000077 | File %1 has been closed before initiating a recovery attempt. The file was open in mode %3. (VM ID: %2).\r\n
0xb0000078 | Recovery attempt initiated for virtual disk %1 (VM ID: %2).\r\n
0xb0000079 | Recovery attempt completed successfully for virtual disk %1 (VM ID: %2).\r\n
0xb000007a | Recovery attempt for virtual disk %1 failed with status %3 (VM ID: %2).\r\n
0xb000007b | Reopening handles to file %1 (VM ID: %2).\r\n
0xb000007c | Waiting for handles to file %1 to be reactivated (VM ID: %2).\r\n
0xb000007d | Recovery attempt completed for file %1 with status %3 (VM ID: %2).\r\n
0xb000007e | I/O failed with status %3 on file %1 (VM ID: %2).\r\n
0xb00000d0 | Change Tracking has been enabled for the VHD %1 (%2) with log file %3.\r\n
0xb00000d1 | Change Tracking has been disabled for the VHD %1 (%2).\r\n
0xb00000d2 | Change Tracking for the VHD %1 to the log file %2 has been stopped due to the error %3.\r\n
0xb00000d3 | Flushing of the header of the log file %1 has failed due to error %2.\r\n
0xb00000d4 | Flushing of the buffers to the log file %1 has failed due to error %2.\r\n
0xb00000d5 | Opening the log file %1 for tracking has failed due to error %2.\r\n
0xb00000d6 | Offline changes are detected for VHD %2. Log file: %1, VHD time: %4, Log file time: %5\r\n
0xb00003e9 | Starting an IO.\r\n
0xb00003ea | Completing an IO.\r\n
0xb00003f2 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery of this virtual disk has been initiated. If this IO was initiated by a VM then it will be internally retried later when the virtual disk has successfully recovered.\r\n
0xb00003f3 | A %4 %3 IO to %1 (VM ID: %2) failed with error %7. Recovery for this virtual disk could not be initiated either because this is not a recoverable failure or recovery has failed or the virtual disk is in an invalid state.\r\n
0xb1000001 | The VHD HBA driver is registered with the root enumerator.\r\n
0xb1000002 | The VHD HBA driver is unregistered with the root enumerator.\r\n
0xd0000001 | Write\r\n
0xd0000002 | Read\r\n
0xd0000003 | Flush\r\n
0xd0000004 | Offload write\r\n
0xd0000005 | Offload read\r\n
0xd0000006 | Project read\r\n
0xd0000007 | Project write\r\n
0xd0000008 | Unmap\r\n
0xd0000009 | Get LBA status\r\n
0xd000000a | File wrapper access check\r\n
0xd000000b | Storport\r\n
0xd000000c | Private\r\n
0xd000000d | Internal\r\n
0xd000000e | Mirror\r\n
0xd000000f | Read-only, shared\r\n
0xd0000010 | Read-only, exclusive\r\n
0xd0000011 | Read-write, exclusive\r\n
0xd0000012 | Invalid\r\n
0xd0000013 | Shared Reference\r\n
0xd0000014 | Exclusive Reference\r\n
0xd0000015 | QoS Reference\r\n
0xd0000016 | Undefined\r\n
0xd0000017 | VHD\r\n
0xd0000018 | VHDX\r\n
0xd0000019 | ISO\r\n
0xd000001a | VHDSET\r\n
