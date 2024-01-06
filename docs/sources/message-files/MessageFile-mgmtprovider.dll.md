## mgmtprovider.dll

Path: %SystemRoot%\system32\wbem\MgmtProvider.dll

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Provider initialization\r\n
0x70000005 | The error checking task\r\n
0x70000006 | Get performance collector state task\r\n
0x70000007 | Set performance collector state task\r\n
0x7000000a | Get counter samples in time range task\r\n
0x7000000b | Get counter samples at time task\r\n
0x7000000d | Get server inventory task\r\n
0x7000000e | Get server feature task\r\n
0x7000000f | Get server event detail task\r\n
0x70000010 | Get server bpa result task\r\n
0x70000011 | Get server cluster name task\r\n
0x70000012 | Get server service detail task\r\n
0x70000013 | Remove server performance log task\r\n
0x70000014 | Elevated Operation\r\n
0x70000015 | WMI Operation\r\n
0x90000001 | Microsoft-Windows-ServerManager-ManagementProvider\r\n
0x90000002 | Operational\r\n
0x90000003 | Debug\r\n
0xb0000001 | Loading the management provider\r\n
0xb0000002 | Unloading the management provider\r\n
0xb000000c | Condition %1 failed, throwing %2.\r\n
0xb000000e | Get performance collector state task start.\r\n
0xb000000f | Get performance collector state task complete.\r\n
0xb0000010 | Get performance collector state task generated an error (%1).\r\n
0xb0000011 | Set performance collector state task start.\r\n
0xb0000012 | Set performance collector state task complete.\r\n
0xb0000013 | Set performance collector state task generated an error (%1).\r\n
0xb000001a | Get counter sample in time range task start.\r\n
0xb000001b | Get counter samples in time range task complete.\r\n
0xb000001c | Get counter samples in time range task generated an error (%1).\r\n
0xb000001d | Unable to process log file: %1, error: %2, last error: %3.\r\n
0xb000001e | Get counter samples at time task start.\r\n
0xb000001f | Get counter samples at time task complete.\r\n
0xb0000020 | Get counter samples at time task generated an error (%1).\r\n
0xb0000021 | Unable to process log file: %1, error: %2, last error: %3\r\n
0xb0000029 | Get server inventory task started.\r\n
0xb000002a | Get server inventory task complete.\r\n
0xb000002b | Get server inventory task failed.\r\n
0xb000002c | Get server inventory task failed to query information from facility: %1, error code: %2, last error: %3.\r\n
0xb000002d | Failure opening metadata of the owning provider for channel: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000002e | Generic failure querying the localized name for channel: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000002f | Get server feature task started, flags: %1.\r\n
0xb0000030 | Get server feature task complete, total features returned: %1.\r\n
0xb0000031 | Get server feature task failed, error: %1.\r\n
0xb0000032 | The feature returned by the ceip provider is not found in the static feature information xml. Id: %1, Name: %2.\r\n
0xb0000033 | The feature's parent id returned by the ceip provider is not found in the static feature information xml. Feature Id: %1, Parent Id: %2\r\n
0xb0000034 | Get server event detail task started, number of logs: %1.\r\n
0xb0000035 | Get server event detail task complete, number of results: %1.\r\n
0xb0000036 | Get server event detail task failed, error: %1.\r\n
0xb0000037 | Server event detail query: %1.\r\n
0xb0000038 | Couldn't find event query file: %1 [hResult: %2, hLastResult: %3].\r\n
0xb0000039 | Server event detail task failed to process the query file: %1, error code: %2, last error: %3.\r\n
0xb000003a | Server event detail task failed to open the provider's metadata, name: %1.\r\n
0xb000003d | The Uxd feature enumeration delay value was not found, using default delay.\r\n
0xb000003e | Get bpa result task start: %1.\r\n
0xb000003f | Get bpa result task complete: %1.\r\n
0xb0000040 | Get bpa result task generated an error: %1, last error: %2\r\n
0xb0000041 | Get cluster name task start.\r\n
0xb0000042 | Get cluster name task complete.\r\n
0xb0000043 | Get cluster name task generated an error.\r\n
0xb0000044 | Events were queried from ADAM (ADAM.Events.xml) but the provider was not able to find any instances [hResult = %1, hLastResult = %2].\r\n
0xb0000045 | Get server service detail task start. Number of service requested: %1\r\n
0xb0000046 | Get server service detail task complete. Number of services returned: %1\r\n
0xb0000047 | Get server service detail task generated an error [hResult: %1, hLastResult = %2].\r\n
0xb0000048 | Couldn't open service: %1 [hResult = %2, hLastResult = %3].\r\n
0xb0000049 | Can't get description of service: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000004a | Can't get config information of service: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000004b | Generic failure querying service details of service: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000004c | Generic failure querying delayed auto start property of serice: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000004d | Remove server performance log task start. Collector name: %1, CutOff time in milliseconds: %2.\r\n
0xb000004e | Remove server performance log task complete. Number of logs removed: %1.\r\n
0xb000004f | Remove server performance log task generated an error '%1' [hResult: %2, hLastResult = %3].\r\n
0xb0000050 | Remove server performance log task encountered an error processing log: %1 [hResult: %2, hLastResult = %3].\r\n
0xb0000051 | Elevated operation %1 failed to revert to network service token. error: %2.\r\n
0xb0000052 | Elevated operation %2 failed to impersonate the client back. error: %2.\r\n
0xb0000053 | The task thread is not impersonating the client after running a elevated operation %1.\r\n
0xb0000054 | The wmi enumeration operation [%1] is being closed without completely enumerating the result. This is not supported in wmi API and will result in unpredictable results.\r\n
0xb0000055 | Failed to query the results of bpa xpath: %1. error: %2, last error: %3.\r\n
0xb0000056 | Failed to get/query the resource of type %1 at index %2. error: %3, last error: %4.\r\n
0xb0000057 | Generic failure querying trigger information of serice: %1 [hResult = %2, hLastResult = %3].\r\n
0xb0000058 | Failed to get the performance data with error code PDH_LOG_TYPE_NOT_FOUND. Error: %1, Qfe Check: %2\r\n
0xb0000059 | Failed to check the status of the performance counter DL QFE, error: %1, last error: %2\r\n

### 10.0.14393.0, 10.0.17763.1

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Provider initialization\r\n
0x70000005 | The error checking task\r\n
0x70000006 | Get performance collector state task\r\n
0x70000007 | Set performance collector state task\r\n
0x7000000a | Get counter samples in time range task\r\n
0x7000000b | Get counter samples at time task\r\n
0x7000000d | Get server inventory task\r\n
0x7000000e | Get server feature task\r\n
0x7000000f | Get server event detail task\r\n
0x70000010 | Get server bpa result task\r\n
0x70000011 | Get server cluster name task\r\n
0x70000012 | Get server service detail task\r\n
0x70000013 | Remove server performance log task\r\n
0x70000014 | Elevated Operation\r\n
0x70000015 | WMI Operation\r\n
0x70000016 | Get server event detail extended task\r\n
0x90000001 | Microsoft-Windows-ServerManager-ManagementProvider\r\n
0x90000002 | Operational\r\n
0x90000003 | Debug\r\n
0xb0000001 | Loading the management provider\r\n
0xb0000002 | Unloading the management provider\r\n
0xb000000c | Condition %1 failed, throwing %2.\r\n
0xb000000e | Get performance collector state task start.\r\n
0xb000000f | Get performance collector state task complete.\r\n
0xb0000010 | Get performance collector state task generated an error (%1).\r\n
0xb0000011 | Set performance collector state task start.\r\n
0xb0000012 | Set performance collector state task complete.\r\n
0xb0000013 | Set performance collector state task generated an error (%1).\r\n
0xb000001a | Get counter sample in time range task start.\r\n
0xb000001b | Get counter samples in time range task complete.\r\n
0xb000001c | Get counter samples in time range task generated an error (%1).\r\n
0xb000001d | Unable to process log file: %1, error: %2, last error: %3.\r\n
0xb000001e | Get counter samples at time task start.\r\n
0xb000001f | Get counter samples at time task complete.\r\n
0xb0000020 | Get counter samples at time task generated an error (%1).\r\n
0xb0000021 | Unable to process log file: %1, error: %2, last error: %3\r\n
0xb0000029 | Get server inventory task started.\r\n
0xb000002a | Get server inventory task complete.\r\n
0xb000002b | Get server inventory task failed.\r\n
0xb000002c | Get server inventory task failed to query information from facility: %1, error code: %2, last error: %3.\r\n
0xb000002d | Failure opening metadata of the owning provider for channel: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000002e | Generic failure querying the localized name for channel: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000002f | Get server feature task started, flags: %1.\r\n
0xb0000030 | Get server feature task complete, total features returned: %1.\r\n
0xb0000031 | Get server feature task failed, error: %1.\r\n
0xb0000032 | The feature returned by the ceip provider is not found in the static feature information xml. Id: %1, Name: %2.\r\n
0xb0000033 | The feature's parent id returned by the ceip provider is not found in the static feature information xml. Feature Id: %1, Parent Id: %2\r\n
0xb0000034 | Get server event detail task started, number of logs: %1.\r\n
0xb0000035 | Get server event detail task complete, number of results: %1.\r\n
0xb0000036 | Get server event detail task failed, error: %1.\r\n
0xb0000037 | Server event detail query: %1.\r\n
0xb0000038 | Couldn't find event query file: %1 [hResult: %2, hLastResult: %3].\r\n
0xb0000039 | Server event detail task failed to process the query file: %1, error code: %2, last error: %3.\r\n
0xb000003a | Server event detail task failed to open the provider's metadata, name: %1.\r\n
0xb000003d | The Uxd feature enumeration delay value was not found, using default delay.\r\n
0xb000003e | Get bpa result task start: %1.\r\n
0xb000003f | Get bpa result task complete: %1.\r\n
0xb0000040 | Get bpa result task generated an error: %1, last error: %2\r\n
0xb0000041 | Get cluster name task start.\r\n
0xb0000042 | Get cluster name task complete.\r\n
0xb0000043 | Get cluster name task generated an error.\r\n
0xb0000044 | Events were queried from ADAM (ADAM.Events.xml) but the provider was not able to find any instances [hResult = %1, hLastResult = %2].\r\n
0xb0000045 | Get server service detail task start. Number of service requested: %1\r\n
0xb0000046 | Get server service detail task complete. Number of services returned: %1\r\n
0xb0000047 | Get server service detail task generated an error [hResult: %1, hLastResult = %2].\r\n
0xb0000048 | Couldn't open service: %1 [hResult = %2, hLastResult = %3].\r\n
0xb0000049 | Can't get description of service: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000004a | Can't get config information of service: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000004b | Generic failure querying service details of service: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000004c | Generic failure querying delayed auto start property of serice: %1 [hResult = %2, hLastResult = %3].\r\n
0xb000004d | Remove server performance log task start. Collector name: %1, CutOff time in milliseconds: %2.\r\n
0xb000004e | Remove server performance log task complete. Number of logs removed: %1.\r\n
0xb000004f | Remove server performance log task generated an error '%1' [hResult: %2, hLastResult = %3].\r\n
0xb0000050 | Remove server performance log task encountered an error processing log: %1 [hResult: %2, hLastResult = %3].\r\n
0xb0000051 | Elevated operation %1 failed to revert to network service token. error: %2.\r\n
0xb0000052 | Elevated operation %2 failed to impersonate the client back. error: %2.\r\n
0xb0000053 | The task thread is not impersonating the client after running a elevated operation %1.\r\n
0xb0000054 | The wmi enumeration operation [%1] is being closed without completely enumerating the result. This is not supported in wmi API and will result in unpredictable results.\r\n
0xb0000055 | Failed to query the results of bpa xpath: %1. error: %2, last error: %3.\r\n
0xb0000056 | Failed to get/query the resource of type %1 at index %2. error: %3, last error: %4.\r\n
0xb0000057 | Generic failure querying trigger information of serice: %1 [hResult = %2, hLastResult = %3].\r\n
0xb0000058 | Failed to get the performance data with error code PDH_LOG_TYPE_NOT_FOUND. Error: %1, Qfe Check: %2\r\n
0xb0000059 | Failed to check the status of the performance counter DL QFE, error: %1, last error: %2\r\n
0xb000005a | Get server event detail extended task started.\r\n
0xb000005b | Get server event detail extended task complete, number of results: %1.\r\n
0xb000005c | Get server event detail extended task failed, error: %1, extended error: %2.\r\n
0xb000005d | Server event detail extended query: %1.\r\n
0xb000005e | Server event detail extended task failed to process the query: error: %1, last error: %2\r\n
0xb000005f | Server event detail extended task failed to open the provider's metadata, name: %1.\r\n
