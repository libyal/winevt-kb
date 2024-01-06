## perfnet.dll

Path: %SystemRoot%\system32\perfnet.dll

### 5.0.2164.1

Message identifier | Message string
--- | ---
0x800003e8 | Unable to open the Network Services performance object. \r\nStatus code returned is data DWORD 0.\r\n
0xc00003e9 | The attempt to collect Network Services Performance data failed \r\nbeause the DLL did not open successfully.\r\n
0xc00007d0 | Unable to open the NETAPI32.DLL for the collection of Browser performance\r\ndata. Browser performance data will not be returned. Error code returned\r\nis in data DWORD 0.\r\n
0xc00007d1 | Unable to locate the Query function for the Browser Performance data in the \r\nNETAPI32.DLL for the collection of Browser performance data. Browser \r\nperformance data will not be returned. Error code returned is in \r\ndata DWORD 0.\r\n
0xc00007d2 | Unable to open the Redirector service. Redirector performance data \r\nwill not be returned. Error code returned is in data DWORD 0.\r\n
0xc00007d3 | Unable to read performance data from the Redirector service. \r\nNo Redirector performance data will be returned in this sample. \r\nError code returned is in data DWORD 0.\r\n
0xc00007d4 | Unable to open the Server service. Server performance data \r\nwill not be returned. Error code returned is in data DWORD 0.\r\n
0xc00007d5 | Unable to read performance data from the Server service. \r\nNo Server performance data will be returned in this sample. \r\nError code returned is in data DWORD 0, IOSB.Status is DWORD 1 and\r\nthe IOSB.Information is DWORD 2.\r\n
0xc00007d6 | Unable to read Server Queue performance data from the Server service. \r\nNo Server Queue performance data will be returned in this sample. \r\nError code returned is in data DWORD 0, IOSB.Status is DWORD 1 and\r\nthe IOSB.Information is DWORD 2.\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x800003e8 | Unable to open the Network Services performance object.\r\nStatus code returned is data DWORD 0.\r\n
0xc00003e9 | The attempt to collect Network Services Performance data failed\r\nbeause the DLL did not open successfully.\r\n
0xc00007d0 | Unable to open the NETAPI32.DLL for the collection of Browser performance\r\ndata. Browser performance data will not be returned. Error code returned\r\nis in data DWORD 0.\r\n
0xc00007d1 | Unable to locate the Query function for the Browser Performance data in the\r\nNETAPI32.DLL for the collection of Browser performance data. Browser\r\nperformance data will not be returned. Error code returned is in\r\ndata DWORD 0.\r\n
0xc00007d2 | Unable to open the Redirector service. Redirector performance data\r\nwill not be returned. Error code returned is in data DWORD 0.\r\n
0xc00007d3 | Unable to read performance data from the Redirector service.\r\nNo Redirector performance data will be returned in this sample.\r\nError code returned is in data DWORD 0.\r\n
0xc00007d4 | Unable to open the Server service. Server performance data\r\nwill not be returned. Error code returned is in data DWORD 0.\r\n
0xc00007d5 | Unable to read performance data from the Server service.\r\nNo Server performance data will be returned in this sample.\r\nError code returned is in data DWORD 0, IOSB.Status is DWORD 1 and\r\nthe IOSB.Information is DWORD 2.\r\n
0xc00007d6 | Unable to read Server Queue performance data from the Server service.\r\nNo Server Queue performance data will be returned in this sample.\r\nError code returned is in data DWORD 0, IOSB.Status is DWORD 1 and\r\nthe IOSB.Information is DWORD 2.\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x800003e8 | Unable to open the Network Services performance object.\r\nStatus code returned is data DWORD 0.\r\n
0xc00003e9 | The attempt to collect Network Services Performance data failed\r\nbeause the DLL did not open successfully.\r\n
0xc00007d0 | Unable to open the NETAPI32.DLL for the collection of Browser performance\r\ndata. Browser performance data will not be returned. The error code returned\r\nis in the first DWORD in the Data section.\r\n
0xc00007d1 | Unable to locate the Query function for the Browser Performance data in the\r\nNETAPI32.DLL for the collection of Browser performance data. Browser\r\nperformance data will not be returned. The error code returned is in\r\nthe first DWORD in the Data section.\r\n
0xc00007d2 | Unable to open the Redirector service. Redirector performance data\r\nwill not be returned. The error code returned is in the first DWORD in\r\nthe Data section.\r\n
0xc00007d3 | Unable to read performance data from the Redirector service.\r\nNo Redirector performance data will be returned in this sample.\r\nThe error code returned is in the first DWORD in the Data section.\r\n
0xc00007d4 | Unable to open the Server service. Server performance data\r\nwill not be returned. The error code returned is in the first DWORD in\r\nthe Data section.\r\n
0xc00007d5 | Unable to read performance data from the Server service.\r\nNo Server performance data will be returned in this sample.\r\nThe error code returned is in first DWORD in the Data section.\r\nThe IOSB.Status is in the second DWORD and the IOSB.Information is\r\nthe third DWORD.\r\n
0xc00007d6 | Unable to read Server Queue performance data from the Server service.\r\nNo Server Queue performance data will be returned in this sample.\r\nThe error code returned is in the first DWORD in the Data section.\r\nThe IOSB.Status is second DWORD and the IOSB.Information is the third DWORD.\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x800003e8 | Unable to open the Network Services performance object. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0x90000001 | Microsoft-Windows-PerfNet\r\n
0xc00003e9 | Unable to collect Network Services performance data. The DLL failed to load because it cannot successfully communicate with network service devices.\r\n
0xc00007d0 | Unable to collect Browser performance data beause the NetApi32.DLL failed to load.  The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d1 | Unable to collect Browser performance data beause the Query function was not found in the NetApi32.DLL.  The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d2 | Unable to open the Redirector service performance object. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d3 | Unable to read performance data for the Redirector service. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d4 | Unable to open the Server service performance object. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d5 | Unable to read performance data for the Server service. The first four bytes (DWORD) of the Data section contains the status code, the second four bytes contains the IOSB.Status and the next four bytes contains the IOSB.Information.\r\n
0xc00007d6 | Unable to read Server Queue performance data from the Server service. The first four bytes (DWORD) of the Data section contains the status code, the second four bytes contains the IOSB.Status and the next four bytes contains the IOSB.Information.\r\n

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1

Message identifier | Message string
--- | ---
0x10000038 | Classic\r\n
0x800003e8 | Unable to open the Network Services performance object. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0x90000001 | Microsoft-Windows-PerfNet\r\n
0x90000002 | Application\r\n
0xc00003e9 | Unable to collect Network Services performance data. The DLL failed to load because it cannot successfully communicate with network service devices.\r\n
0xc00007d0 | Unable to collect Browser performance data because the NetApi32.DLL failed to load.  The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d1 | Unable to collect Browser performance data because the Query function was not found in the NetApi32.DLL.  The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d2 | Unable to open the Redirector service performance object. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d3 | Unable to read performance data for the Redirector service. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d4 | Unable to open the Server service performance object. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0xc00007d5 | Unable to read performance data for the Server service. The first four bytes (DWORD) of the Data section contains the status code, the second four bytes contains the IOSB.Status and the next four bytes contains the IOSB.Information.\r\n
0xc00007d6 | Unable to read Server Queue performance data from the Server service. The first four bytes (DWORD) of the Data section contains the status code, the second four bytes contains the IOSB.Status and the next four bytes contains the IOSB.Information.\r\n

### 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x000003e8 | Unable to open the Network Services performance object. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0x000003e9 | Unable to collect Network Services performance data. The DLL failed to load because it cannot successfully communicate with network service devices.\r\n
0x000007d0 | Unable to collect Browser performance data because the NetApi32.DLL failed to load.  The first four bytes (DWORD) of the Data section contains the status code.\r\n
0x000007d1 | Unable to collect Browser performance data because the Query function was not found in the NetApi32.DLL.  The first four bytes (DWORD) of the Data section contains the status code.\r\n
0x000007d2 | Unable to open the Redirector service performance object. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0x000007d3 | Unable to read performance data for the Redirector service. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0x000007d4 | Unable to open the Server service performance object. The first four bytes (DWORD) of the Data section contains the status code.\r\n
0x000007d5 | Unable to read performance data for the Server service. The first four bytes (DWORD) of the Data section contains the status code, the second four bytes contains the IOSB.Status and the next four bytes contains the IOSB.Information.\r\n
0x000007d6 | Unable to read Server Queue performance data from the Server service. The first four bytes (DWORD) of the Data section contains the status code, the second four bytes contains the IOSB.Status and the next four bytes contains the IOSB.Information.\r\n
0x10000038 | Classic\r\n
0x50000002 | Error\r\n
0x800003e8 | %%1000\r\n
0x90000001 | Microsoft-Windows-PerfNet\r\n
0x90000002 | Application\r\n
0xc00003e9 | %%1001\r\n
0xc00007d0 | %%2000\r\n
0xc00007d1 | %%2001\r\n
0xc00007d2 | %%2002\r\n
0xc00007d3 | %%2003\r\n
0xc00007d4 | %%2004\r\n
0xc00007d5 | %%2005\r\n
0xc00007d6 | %%2006\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x000003e8 | Unable to open the Network Services performance object. Error: %1\r\n
0x000003e9 | Unable to collect Network Services performance data. The DLL failed to load because it cannot successfully communicate with network service devices.\r\n
0x000007d0 | Unable to collect Browser performance data because the NetApi32.DLL failed to load. Error: %1\r\n
0x000007d1 | Unable to collect Browser performance data because the Query function was not found in the NetApi32.DLL. Error: %1\r\n
0x000007d2 | Unable to open the Redirector service performance object. Error: %1\r\n
0x000007d3 | Unable to read performance data for the Redirector service. Error: %1\r\n
0x000007d4 | Unable to open the Server service performance object. Error: %1\r\n
0x000007d5 | Unable to read performance data for the Server service. Error: %1\r\n
0x000007d6 | Unable to read Server Queue performance data from the Server service. Error: %1\r\n
0x000007d7 | Unable to allocate memory for TDI Statistics block. Close one or more applications and retry.\r\n
0x00000c1d | Unable to read IO control information from an NBT device. A network device using the NBT protocol could not be queried.\r\n
0x00000faa | Unable to get the local computer name. The data in the data section contains the error code.\r\n
0x00001019 | SNMP returned a NULL buffer in response to a request for network performance information. This error may be caused by a problem with the SNMP service.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | Microsoft-Windows-PerfNet\r\n
0x90000002 | Application\r\n
0xb0010bb8 | Entered the OpenNbtPerformanceData routine.\r\n
0xb0010c1b | The OpenNbtPerformanceData routine successfully completed.\r\n
0xb0010c1c | Entered the CollectNbtPerformanceData routine.\r\n
0xb0010c1e | Successfully read the NBT device IO Control information.\r\n
0xb0010c1f | The data buffer passed to the collection routine was too small to receive the data from the NBT device. No data was returned to the caller. The bytes available and the bytes required are in the message data.\r\n
0xb0010c7f | The CollectNbtPerformanceData routine successfully completed.\r\n
0xb0010c80 | Entered the CloseNbtPerformanceData routine.\r\n
0xb0010fa0 | Entered the OpenTcpIpPerformanceData routine.\r\n
0xb0010fa1 | NBT Open failed. See NBT error message.\r\n
0xb0010fa2 | NBT Open succeeded.\r\n
0xb0011003 | The OpenTcpIpPerformanceData routine successfully completed.\r\n
0xb0011004 | Entered the CollectTcpIpPerformanceData routine.\r\n
0xb0011009 | The CollectNbtPerformanceData routine returned an error. The error status is in the data section.\r\n
0xb001100a | The OpenTcpIpPerformanceData routine did not establish a SNMP Mgr Session.\r\n
0xb001100c | The SnmpMgrRequest call requesting the TCP, IP, UDP and Interface Counters returned an error. The ErrorStatus and ErrorIndex values are shown in Data.\r\n
0xb001100e | The SnmpMgrRequest call requesting ICMP Counters returned an error. The ErrorStatus and ErrorIndex values are shown in Data.\r\n
0xb001100f | Processing NetInterface entries.\r\n
0xb0011010 | The buffer is not large enough to store the Network Interface data. The returned data contains the available and required buffer size.\r\n
0xb0011011 | The SnmpGet (GETNEXT) request returned an error while processing the Net Interface instances. The ErrorStatus and ErrorIndex are shown in Data.\r\n
0xb0011012 | Copying data from network requests to the Performance Monitor buffer.\r\n
0xb0011014 | The buffer is not large enough to store the Network Protocol (IP, ICMP, TCP & UDP) data. The returned data contains the available and required buffer size.\r\n
0xb0011067 | The CollectTcpIpPerformanceData routine successfully completed.\r\n
0xb0011068 | Entered the CloseTcpIpPerformanceData routine.\r\n
