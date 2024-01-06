## msdtcvsp1res.dll

Path: %SystemRoot%\system32\msdtcVSp1res.dll

### 2001.12.8530.16385

Message identifier | Message string
--- | ---
0x10000038 | Classic\r\n
0x40001001 | Failed to clean up the default DTC cluster resource setting. The default DTC cluster resource setting might be invalid. The error code returned: %1 %0\r\n
0x40001002 | Contact = %1 was deleted successfully. Attempt to copy the new contact = %2 over it failed. The DTC configuration may be corrupted. The operation that failed must be retried. The error code returned: %3 %0\r\n
0x40001003 | Failed to create DTC cluster resource. DTC cluster resource GUID specified = %1. The error code returned: %2 %0\r\n
0x40001004 | Attempt to find the drive letter corresponding to the cluster DTC's dependent disk resource has failed. The error code returned: %1 %0\r\n
0x40001005 | The DTC cluster resource's log file path was originally configured at: %1. Attempting to change that to: %2. This indicates a change in the path of the DTC cluster resource's dependent disk resource. This is not supported. The error code returned: %3 %0\r\n
0x40001006 | Application specified a cluster resource ID: %1, but no DTC cluster resource could be returned. Instead, the local DTC instance was returned%0\r\n
0x40001007 | Service: %1 is still running. Attempt to cleanup the service has failed%0\r\n
0x40001008 | Failed trying to get the state of the cluster node: %1.The error code returned: %2 %0\r\n
0x4000106a | MSDTC started with the following settings:%r%r Security Configuration (OFF = 0 and ON = 1):%r Allow Remote Administrator = %1,%r Network Clients = %2,%r Trasaction Manager Communication: %r Allow Inbound Transactions = %3,%r Allow Outbound Transactions = %4,%r Transaction Internet Protocol (TIP) = %5,%r  Enable XA Transactions = %6,%r  Enable SNA LU 6.2 Transactions = %12,%r  MSDTC Communications Security = %8,%r Account = %9,%r  Firewall Exclusion Detected = %10%r%r Transaction Bridge Installed = %11%r Filtering Duplicate Events = %7%r%0\r\n
0x70000001 | DTC Shared Utility%0\r\n
0x70000002 | TM%0\r\n
0x70000003 | CM%0\r\n
0x70000005 | XATM%0\r\n
0x7000000e | Cluster%0\r\n
0x7100000a | MSDTC Proxy%0\r\n
0x80001308 | A caller has attempted to register an XA resource while XA transactions are disabled. Please review the MSDTC configuration settings.%0\r\n
0x80001309 | An XA transaction manager has attempted to open the MSDTC XA resource while XA transactions are disabled. Please review the MSDTC configuration settings.%0\r\n
0x8000130a | A caller has attempted to propagate a transaction to a remote system, but MSDTC network DTC access is currently disabled on machine '%1'. Please review the MS DTC configuration settings.%0\r\n
0x8000130b | A caller has attempted to import a transaction from a remote system, but MSDTC is currently configured to disallow inbound transaction manager communication on machine '%1'. Please review the MS DTC configuration settings.%0\r\n
0x8000130c | A caller has attempted to export a transaction to a remote system, but MSDTC is currently configured to disallow outbound transaction manager communication on machine '%1'. Please review the MS DTC configuration settings.%0\r\n
0x8000130e | MSDTC encountered an error (HR=0x%1) while attempting to authenticate an incoming connection from system '%2'. The principal name is %3.%0\r\n
0x8000130f | MSDTC encountered an error (HR=0x%1) while attempting to establish a secure connection with system %2.%0\r\n
0x80001310 | MS DTC encountered an error while attempting to process a message from a connection with system '%1'. The incoming message should be from another MSDTC, but has not been authenticated as such. The principal name is '%2'.%0\r\n
0x80001311 | A caller has attempted to connect to a remote MSDTC on machine '%1'.  The attempt failed because the remote machine is configured to disallow remote clients.%0\r\n
0x8000d04b | The MSDTC XA Transaction Manager called the xa_rollback function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d04c | The MSDTC XA Transaction Manager called the xa_commit function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d04d | The MSDTC XA Transaction Manager called the xa_open function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d04f | The MSDTC XA Transaction Manager called the 'GetXaSwitch' function in the XA resource manager DLL '%1'. The call to the 'GetXaSwitch' function failed with error %2: File=%3 Line=%4.%0\r\n
0x8000d050 | The MSDTC XA Transaction Manager attempted to perform recovery with the XA resource manager DLL '%1'. The XA resource manager reported that recovery was unsuccessful (XA return code=%2).%0 \r\n
0x8000d051 | The MSDTC XA Transaction Manager called the xa_open function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d052 | The MSDTC XA Transaction Manager called the xa_close function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d053 | The MSDTC XA Transaction Manager called the xa_recover function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d054 | The MSDTC XA Transaction Manager called the xa_commit function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d055 | The MSDTC XA Transaction Manager called the xa_rollback function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d056 | The MSDTC XA Transaction Manager called the xa_prepare function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d057 | The MSDTC XA Transaction Manager called the GetXaSwitch function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d058 | The MSDTC XA Transaction Manager called the xa_prepare function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d059 | The MSDTC XA Transaction Manager called the xa_commit function with the TMONEPHASE flag set for the XA resource manager '%1'. The call to the xa_commit function failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d05a | The MSDTC XA Transaction Manager attempted to locate the 'GetXaSwitch' function in the XA resource manager DLL. The 'GetXaSwitch' function is missing from the XA resource manager DLL %1 : Error=%2 File=%3 Line=%4.%0\r\n
0x8000d05b | The MS DTC XA Transaction Manager called the xa_close function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x90000001 | Microsoft-Windows-MSDTC 2\r\n
0x91000001 | Microsoft-Windows-MSDTC Client 2\r\n

### 2001.12.10130.16384, 2001.12.10530.16384

Message identifier | Message string
--- | ---
0x10000038 | Classic\r\n
0x40001001 | Failed to clean up the default DTC cluster resource setting. The default DTC cluster resource setting might be invalid. The error code returned: %1 %0\r\n
0x40001002 | Contact = %1 was deleted successfully. Attempt to copy the new contact = %2 over it failed. The DTC configuration may be corrupted. The operation that failed must be retried. The error code returned: %3 %0\r\n
0x40001003 | Failed to create DTC cluster resource. DTC cluster resource GUID specified = %1. The error code returned: %2 %0\r\n
0x40001004 | Attempt to find the drive letter or Volume Guid corresponding to the cluster DTC's dependent disk resource has failed. If the dependent disk resource does not support Volume Guid information, please configure at least one dependent disk partition with a drive letter. The error code returned: %1 %0\r\n
0x40001005 | Attempting to change the DTC cluster resource's log file path to %1 has failed. Please verify if log path is configured to a valid dependent disk partition. The error code returned: %2 %0\r\n
0x40001006 | Application specified a cluster resource ID: %1, but no DTC cluster resource could be returned. Instead, the local DTC instance was returned%0\r\n
0x40001007 | Service: %1 is still running. Attempt to cleanup the service has failed%0\r\n
0x40001008 | Failed trying to get the state of the cluster node: %1.The error code returned: %2 %0\r\n
0x4000106a | MSDTC started with the following settings:%r%r Security Configuration (OFF = 0 and ON = 1):%r Allow Remote Administrator = %1,%r Network Clients = %2,%r Transaction Manager Communication: %r Allow Inbound Transactions = %3,%r Allow Outbound Transactions = %4,%r Transaction Internet Protocol (TIP) = %5,%r  Enable XA Transactions = %6,%r  Enable SNA LU 6.2 Transactions = %12,%r  MSDTC Communications Security = %8,%r Account = %9,%r  Firewall Exclusion Detected = %10%r%r Transaction Bridge Installed = %11%r Filtering Duplicate Events = %7%r%0\r\n
0x70000001 | DTC Shared Utility%0\r\n
0x70000002 | TM%0\r\n
0x70000003 | CM%0\r\n
0x70000005 | XATM%0\r\n
0x7000000e | Cluster%0\r\n
0x7100000a | MSDTC Proxy%0\r\n
0x80001308 | A caller has attempted to register an XA resource while XA transactions are disabled. Please review the MSDTC configuration settings.%0\r\n
0x80001309 | An XA transaction manager has attempted to open the MSDTC XA resource while XA transactions are disabled. Please review the MSDTC configuration settings.%0\r\n
0x8000130a | A caller has attempted to propagate a transaction to a remote system, but MSDTC network DTC access is currently disabled on machine '%1'. Please review the MS DTC configuration settings.%0\r\n
0x8000130b | A caller has attempted to import a transaction from a remote system, but MSDTC is currently configured to disallow inbound transaction manager communication on machine '%1'. Please review the MS DTC configuration settings.%0\r\n
0x8000130c | A caller has attempted to export a transaction to a remote system, but MSDTC is currently configured to disallow outbound transaction manager communication on machine '%1'. Please review the MS DTC configuration settings.%0\r\n
0x8000130e | MSDTC encountered an error (HR=0x%1) while attempting to authenticate an incoming connection from system '%2'. The principal name is %3.%0\r\n
0x8000130f | MSDTC encountered an error (HR=0x%1) while attempting to establish a secure connection with system %2.%0\r\n
0x80001310 | MS DTC encountered an error while attempting to process a message from a connection with system '%1'. The incoming message should be from another MSDTC, but has not been authenticated as such. The principal name is '%2'.%0\r\n
0x80001311 | A caller has attempted to connect to a remote MSDTC on machine '%1'.  The attempt failed because the remote machine is configured to disallow remote clients.%0\r\n
0x8000d04b | The MSDTC XA Transaction Manager called the xa_rollback function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d04c | The MSDTC XA Transaction Manager called the xa_commit function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d04d | The MSDTC XA Transaction Manager called the xa_open function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d04f | The MSDTC XA Transaction Manager called the 'GetXaSwitch' function in the XA resource manager DLL '%1'. The call to the 'GetXaSwitch' function failed with error %2: File=%3 Line=%4.%0\r\n
0x8000d050 | The MSDTC XA Transaction Manager attempted to perform recovery with the XA resource manager DLL '%1'. The XA resource manager reported that recovery was unsuccessful (XA return code=%2).%0 \r\n
0x8000d051 | The MSDTC XA Transaction Manager called the xa_open function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d052 | The MSDTC XA Transaction Manager called the xa_close function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d053 | The MSDTC XA Transaction Manager called the xa_recover function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d054 | The MSDTC XA Transaction Manager called the xa_commit function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d055 | The MSDTC XA Transaction Manager called the xa_rollback function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d056 | The MSDTC XA Transaction Manager called the xa_prepare function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d057 | The MSDTC XA Transaction Manager called the GetXaSwitch function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d058 | The MSDTC XA Transaction Manager called the xa_prepare function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d059 | The MSDTC XA Transaction Manager called the xa_commit function with the TMONEPHASE flag set for the XA resource manager '%1'. The call to the xa_commit function failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d05a | The MSDTC XA Transaction Manager attempted to locate the 'GetXaSwitch' function in the XA resource manager DLL. The 'GetXaSwitch' function is missing from the XA resource manager DLL %1 : Error=%2 File=%3 Line=%4.%0\r\n
0x8000d05b | The MS DTC XA Transaction Manager called the xa_close function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x90000001 | Microsoft-Windows-MSDTC 2\r\n
0x91000001 | Microsoft-Windows-MSDTC Client 2\r\n

### 2001.12.10941.16384

Message identifier | Message string
--- | ---
0x10000038 | Classic\r\n
0x40001001 | Failed to clean up the default DTC cluster resource setting. The default DTC cluster resource setting might be invalid. The error code returned: %1 %0\r\n
0x40001002 | Contact = %1 was deleted successfully. Attempt to copy the new contact = %2 over it failed. The DTC configuration may be corrupted. The operation that failed must be retried. The error code returned: %3 %0\r\n
0x40001003 | Failed to create DTC cluster resource. DTC cluster resource GUID specified = %1. The error code returned: %2 %0\r\n
0x40001004 | Attempt to find the drive letter or Volume Guid corresponding to the cluster DTC's dependent disk resource has failed. If the dependent disk resource does not support Volume Guid information, please configure at least one dependent disk partition with a drive letter. The error code returned: %1 %0\r\n
0x40001005 | Attempting to change the DTC cluster resource's log file path to %1 has failed. Please verify if log path is configured to a valid dependent disk partition. The error code returned: %2 %0\r\n
0x40001006 | Application specified a cluster resource ID: %1, but no DTC cluster resource could be returned. Instead, the local DTC instance was returned%0\r\n
0x40001007 | Service: %1 is still running. Attempt to cleanup the service has failed%0\r\n
0x40001008 | Failed trying to get the state of the cluster node: %1.The error code returned: %2 %0\r\n
0x4000106a | MSDTC started with the following settings:%r%r Security Configuration (OFF = 0 and ON = 1):%r Allow Remote Administrator = %1,%r Network Clients = %2,%r Transaction Manager Communication: %r Allow Inbound Transactions = %3,%r Allow Outbound Transactions = %4,%r Transaction Internet Protocol (TIP) = %5,%r  Enable XA Transactions = %6,%r  Enable SNA LU 6.2 Transactions = %12,%r  MSDTC Communications Security = %8,%r Account = %9,%r  Firewall Exclusion Detected = %10%r%r Transaction Bridge Installed = %11%r Filtering Duplicate Events = %7%r%0\r\n
0x400010fe | Cluster API call failed with error code: %1. Cluster API function: %2 Arguments: %3 %0\r\n
0x70000001 | DTC Shared Utility%0\r\n
0x70000002 | TM%0\r\n
0x70000003 | CM%0\r\n
0x70000005 | XATM%0\r\n
0x7000000e | Cluster%0\r\n
0x7100000a | MSDTC Proxy%0\r\n
0x80001308 | A caller has attempted to register an XA resource while XA transactions are disabled. Please review the MSDTC configuration settings.%0\r\n
0x80001309 | An XA transaction manager has attempted to open the MSDTC XA resource while XA transactions are disabled. Please review the MSDTC configuration settings.%0\r\n
0x8000130a | A caller has attempted to propagate a transaction to a remote system, but MSDTC network DTC access is currently disabled on machine '%1'. Please review the MS DTC configuration settings.%0\r\n
0x8000130b | A caller has attempted to import a transaction from a remote system, but MSDTC is currently configured to disallow inbound transaction manager communication on machine '%1'. Please review the MS DTC configuration settings.%0\r\n
0x8000130c | A caller has attempted to export a transaction to a remote system, but MSDTC is currently configured to disallow outbound transaction manager communication on machine '%1'. Please review the MS DTC configuration settings.%0\r\n
0x8000130e | MSDTC encountered an error (HR=0x%1) while attempting to authenticate an incoming connection from system '%2'. The principal name is %3.%0\r\n
0x8000130f | MSDTC encountered an error (HR=0x%1) while attempting to establish a secure connection with system %2.%0\r\n
0x80001310 | MS DTC encountered an error while attempting to process a message from a connection with system '%1'. The incoming message should be from another MSDTC, but has not been authenticated as such. The principal name is '%2'.%0\r\n
0x80001311 | A caller has attempted to connect to a remote MSDTC on machine '%1'.  The attempt failed because the remote machine is configured to disallow remote clients.%0\r\n
0x8000d04b | The MSDTC XA Transaction Manager called the xa_rollback function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d04c | The MSDTC XA Transaction Manager called the xa_commit function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d04d | The MSDTC XA Transaction Manager called the xa_open function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d04f | The MSDTC XA Transaction Manager called the 'GetXaSwitch' function in the XA resource manager DLL '%1'. The call to the 'GetXaSwitch' function failed with error %2: File=%3 Line=%4.%0\r\n
0x8000d050 | The MSDTC XA Transaction Manager attempted to perform recovery with the XA resource manager DLL '%1'. The XA resource manager reported that recovery was unsuccessful (XA return code=%2).%0 \r\n
0x8000d051 | The MSDTC XA Transaction Manager called the xa_open function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d052 | The MSDTC XA Transaction Manager called the xa_close function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d053 | The MSDTC XA Transaction Manager called the xa_recover function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d054 | The MSDTC XA Transaction Manager called the xa_commit function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d055 | The MSDTC XA Transaction Manager called the xa_rollback function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d056 | The MSDTC XA Transaction Manager called the xa_prepare function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d057 | The MSDTC XA Transaction Manager called the GetXaSwitch function in the XA resource manager DLL '%1'. This call failed with a user exception: File=%2 Line=%3.%0\r\n
0x8000d058 | The MSDTC XA Transaction Manager called the xa_prepare function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d059 | The MSDTC XA Transaction Manager called the xa_commit function with the TMONEPHASE flag set for the XA resource manager '%1'. The call to the xa_commit function failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x8000d05a | The MSDTC XA Transaction Manager attempted to locate the 'GetXaSwitch' function in the XA resource manager DLL. The 'GetXaSwitch' function is missing from the XA resource manager DLL %1 : Error=%2 File=%3 Line=%4.%0\r\n
0x8000d05b | The MS DTC XA Transaction Manager called the xa_close function for XA resource manager '%1'. This call failed with an unexpected return code (%2): File=%3 Line=%4.%0\r\n
0x90000001 | Microsoft-Windows-MSDTC 2\r\n
0x91000001 | Microsoft-Windows-MSDTC Client 2\r\n
