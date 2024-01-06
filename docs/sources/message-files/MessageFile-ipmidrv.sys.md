## ipmidrv.sys

Path: %SystemRoot%\System32\drivers\ipmidrv.sys

### 6.0.6000.16386, 6.1.7600.16385, 6.1.7601.17514, 6.2.9200.16384, 6.3.9600.16384, 6.3.9600.18227, 10.0.10586.0, 10.0.14393.0

Message identifier | Message string
--- | ---
0x800503ea | The IPMI device driver read an administrator supplied parameter that is invalid. The device driver will use a system defined default value in its place.\r\n
0x800503ec | The IPMI device driver attempted to communicate with the IPMI BMC device during normal operation. However the communication failed due to a timeout. You can increase the timeouts associated with the IPMI device driver.\r\n
0xc00503e8 | During communication with the IPMI BMC device, the system detected that the BMC entered an error state. The driver attempted to set the BMC state to a working state but failed to do so. After 20 successive attempts, the driver has set the IPMI device to a non working state. It is recommended that you seek assistance from the BMC device manufacturer. You can return the device instance to the working state by disabling and enabling the IPMI device instance labeled æIPMI Device DriverÆ. You can locate the IPMI device instance within the Device Manager user interface.\r\n
0xc00503e9 | The IPMI device driver attempted to determine if the system supported an IPMI BMC device. The driver attempted to detect the presence of the IPMI BMC by searching the SMBIOS for a Type38 record.  But either no record was found or the record was not compatible with the version of the device driver. If a SMBIOS Type 38 record was detected, the Dump Data field of the event contains a binary representation of the record.\r\n
0xc00503eb | The IPMI device driver attempted to communicate with the IPMI BMC device during device creation. However the communication failed due to a timeout. Either the configured timeouts are too small and the IPMI BMC device responses take longer than the timeouts or the BMC has a technical fault. You can increase the timeouts associated with the IPMI device driver or seek assistance from the BMC device manufacturer.\r\n

### 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x800503ea | The IPMI device driver read an administrator supplied parameter that is invalid. The device driver will use a system defined default value in its place.\r\n
0x800503ec | The IPMI device driver attempted to communicate with the IPMI BMC device during normal operation. However the communication failed due to a timeout. You can increase the timeouts associated with the IPMI device driver.\r\n
0xc00503e8 | During communication with the IPMI BMC device, the system detected that the BMC entered an error state. The driver attempted to set the BMC state to a working state but failed to do so. After 20 successive attempts, the driver has set the IPMI device to a non working state. It is recommended that you seek assistance from the BMC device manufacturer. You can return the device instance to the working state by disabling and enabling the IPMI device instance labeled ‘IPMI Device Driver’. You can locate the IPMI device instance within the Device Manager user interface.\r\n
0xc00503e9 | The IPMI device driver attempted to determine if the system supported an IPMI BMC device. The driver attempted to detect the presence of the IPMI BMC by searching the SMBIOS for a Type38 record.  But either no record was found or the record was not compatible with the version of the device driver. If a SMBIOS Type 38 record was detected, the Dump Data field of the event contains a binary representation of the record.\r\n
0xc00503eb | The IPMI device driver attempted to communicate with the IPMI BMC device during device creation. However the communication failed due to a timeout. Either the configured timeouts are too small and the IPMI BMC device responses take longer than the timeouts or the BMC has a technical fault. You can increase the timeouts associated with the IPMI device driver or seek assistance from the BMC device manufacturer.\r\n

### 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x800503ea | The IPMI device driver read an administrator supplied parameter that is invalid. The device driver will use a system defined default value in its place.\r\n
0x800503ec | The IPMI device driver attempted to communicate with the IPMI BMC device during normal operation. However the communication failed due to a timeout. You can increase the timeouts associated with the IPMI device driver.\r\n
0x800503ed | The SEL cache attempted to send IPMI messages to the BMC; however, they repeatedly failed. The worker will quit after 10 minutes of consecutive failed messages.\r\n
0x800503ee | The SEL cache repeatedly failed to query the BMC for 10 minutes and has now shut down.\r\n
0x800503ef | The SEL cache initialization detected that SEL caching was already running.\r\n
0xc00503e8 | During communication with the IPMI BMC device, the system detected that the BMC entered an error state. The driver attempted to set the BMC state to a working state but failed to do so. After 20 successive attempts, the driver has set the IPMI device to a non working state. It is recommended that you seek assistance from the BMC device manufacturer. You can return the device instance to the working state by disabling and enabling the IPMI device instance labeled 'IPMI Device Driver'. You can locate the IPMI device instance within the Device Manager user interface.\r\n
0xc00503e9 | The IPMI device driver attempted to determine if the system supported an IPMI BMC device. The driver attempted to detect the presence of the IPMI BMC by searching the SMBIOS for a Type38 record.  But either no record was found or the record was not compatible with the version of the device driver. If a SMBIOS Type 38 record was detected, the Dump Data field of the event contains a binary representation of the record.\r\n
0xc00503eb | The IPMI device driver attempted to communicate with the IPMI BMC device during device creation. However the communication failed due to a timeout. Either the configured timeouts are too small and the IPMI BMC device responses take longer than the timeouts or the BMC has a technical fault. You can increase the timeouts associated with the IPMI device driver or seek assistance from the BMC device manufacturer.\r\n
