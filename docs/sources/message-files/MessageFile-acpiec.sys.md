## acpiec.sys

Path: %SystemRoot%\System32\Drivers\acpiec.sys

### 5.1.2600.0, 5.2.3790.0, 5.2.3790.1830

Message identifier | Message string
--- | ---
0x80050003 | %1: The embedded controller (EC) hardware returned data when none was requested.  This may indicate that the BIOS is incorectly trying to access the EC without syncronizing with the OS.  The data is being ignored.\r\n
0xc0050001 | %1: The embedded controller (EC) hardware didn't respond within the timeout period.  This may indicate an error in the EC hardware or firmware, or possibly a poorly designed BIOS which accesses the EC in an unsafe manner.  The EC driver will retry the failed transaction if possible.\r\n
0xc0050002 | %1: The embedded controller (EC) hardware appears to have quit functioning.  Repeated retries have resulted in no forward progress processing requests.  All requests to the EC will fail until reboot.\r\n
