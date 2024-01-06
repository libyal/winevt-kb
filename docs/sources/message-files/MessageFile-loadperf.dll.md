## loadperf.dll

Path: %SystemRoot%\system32\loadperf.dll

### 5.0.2195.6601

Message identifier | Message string
--- | ---
0x400003e8 | Performance counters for the %1!s! service were loaded successfully.\r\nThe Record Data contains the new index values assigned\r\nto this service.\r\n
0x400003e9 | Performance counters for the %1!s! service were removed successfully.\r\nThe Record Data contains the new values of the system Last Counter and \r\nLast Help registry entries.\r\n
0x800007d0 | No object list was found in the installation file. Adding an object \r\nlist to the installation file will \r\nimprove performance of the system when measuring performance counters.\r\n
0x800007d1 | No MOF file was created for the %1!s! service. Before the performance\r\ncounters of this service can be collected by WMI a MOF file will need \r\nto be created and loaded manually. Contact the vendor of this service \r\nfor additional information.\r\n
0x800007d2 | The MOF file created for the %1!s! service could not be loaded. The \r\nerror code returned by the MOF Compiler is contained in the Record Data. \r\nBefore the performance counters of this service can be collected by WMI \r\nthe MOF file will need to be loaded manually. Contact the vendor of this \r\nservice for additional information.\r\n
0x800007d3 | The MOF file created for the %1!s! service cannot be deleted as requested. \r\nThe MOF file is required for the autorecover function.\r\n
0xc0000bb8 | The performance strings in the registry do not match the index values \r\nstored in the Perflib key. The Record Data contains the last index value \r\nfrom the Perflib key in DWORD 0 and the index of the last string used as\r\nDWORD 1.\r\n
0xc0000bb9 | The performance counter name string value in the registry is incorrectly \r\nformatted. The last valid index value is DWORD 0 in the Record Data.\r\n
0xc0000bba | The performance counter explain text string value in the registry is \r\nincorrectly formatted. The last valid index value is DWORD 0 in the \r\nRecord Data.\r\n
0xc0000bbb | The %1!s! key could not be opened or accessed in order to install counter \r\nstrings.The Win32 status returned by the call is in the Record Data as \r\nDWORD 0.\r\n
0xc0000bbc | The %1!s! registry value could not be read or was the incorrect data type.\r\nThe Win32 status returned by the call is in the Record Data as DWORD 0.\r\n
0xc0000bbd | Unable to open the registry key for the performance counter strings of \r\nthe %1!s! language ID.\r\nThe Win32 status returned by the call is in the Record Data as DWORD 0.\r\n
0xc0000bbe | Unable to read the performance counter strings of the %1!s! language ID.\r\nThe Win32 status returned by the call is in the Record Data as DWORD 0.\r\n
0xc0000bbf | Unable to read the performance counter explain text strings of the \r\n%1!s! language ID.\r\nThe Win32 status returned by the call is in the Record Data as DWORD 0.\r\n
0xc0000bc0 | Unable to allocate a required memory buffer.\r\n
0xc0000bc1 | Installing the performance counter strings for %1!s! failed. The\r\nError code is DWORD 0 of the Record Data.\r\n
0xc0000bc2 | Updating the performance counter strings failed. The\r\nError code is DWORD 0 of the Record Data.\r\n
0xc0000bc3 | Unloading the performance counter strings for %1!s! failed. The\r\nError code is DWORD 0 of the Record Data.\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x400003e8 | Performance counters for the %1!s! (%2!s!) service were loaded successfully.\r\nThe Record Data contains the new index values assigned\r\nto this service.\r\n
0x400003e9 | Performance counters for the %1!s! (%2!s!) service were removed successfully.\r\nThe Record Data contains the new values of the system Last Counter and\r\nLast Help registry entries.\r\n
0x400003ea | Performance counters for the %1!s! (%2!s!) service are already in Performance\r\nRegistry, no need to re-install again.\r\n
0x800007d1 | No MOF file %2!s! was created for the %1!s! service. Before the performance\r\ncounters of this service can be collected by WMI a MOF file will need\r\nto be created and loaded manually. Contact the vendor of this service\r\nfor additional information.\r\n
0x800007d2 | The MOF file created for the %1!s! service could not be loaded. The\r\nerror code returned by the MOF Compiler is contained in the Record Data.\r\nBefore the performance counters of this service can be collected by WMI\r\nthe MOF file will need to be loaded manually. Contact the vendor of this\r\nservice for additional information.\r\n
0x800007d3 | The MOF file created for the %1!s! service cannot be deleted as requested.\r\nThe MOF file is required for the autorecover function.\r\n
0x800007d4 | The Performance registry value %1!s! string is corrupted. Skip string \"%2!s!\".\r\n
0x800007d5 | No COUNTER/HELP definition for Language %1!s!.\r\n
0x800007d6 | LastCounter and LastHelp values of performance registry is corrupted and\r\nneeds to be updated. The first and second DWORDs in Data Section are the\r\noriginal values while the third and forth DWORDs in Data Section are the\r\nupdated new values.\r\n
0xc0000bb8 | The performance strings in the registry do not match the index values\r\nstored in Performance registry key. The last index value from performance\r\nregistry key in the first DWORD in Data section, and the index of the\r\nlast string used in the second DWORD in Data section.\r\n
0xc0000bb9 | The performance counter name string value in the registry is incorrectly\r\nformatted. The bogus string is %1!s!, the bogus index value is the first\r\nDWORD in Data section while the last valid index values are the second and\r\nthird DWORD in Data section.\r\n
0xc0000bba | The performance counter explain text string value in the registry is\r\nincorrectly formatted. The bogus string is %1!s!, the bogus index value\r\nis the first DWORD in Data section while the last valid index values are\r\nthe second and third DWORD in Data section.\r\n
0xc0000bbb | The %1!s! key could not be opened or accessed in order to install counter\r\nstrings.The Win32 status returned by the call is the first DWORD in Data\r\nsection.\r\n
0xc0000bbc | The %1!s! registry value could not be read or was the incorrect data type.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bbd | Unable to open the registry key for the performance counter strings of\r\nthe %1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bbe | Unable to read the performance counter strings of the %1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bbf | Unable to read the performance counter explain text strings of the\r\n%1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bc0 | Unable to allocate a required memory buffer.\r\n
0xc0000bc1 | Installing the performance counter strings for service %1!s! (%2!s!) failed. The\r\nError code is the first DWORD in Data section.\r\n
0xc0000bc3 | Unloading the performance counter strings for service %1!s! (%2!s!) failed. The\r\nError code is the first DWORD in Data section.\r\n
0xc0000bc4 | The performance strings in the Performance registry value is corrupted when\r\nprocess %1!s! extension counter provider. BaseIndex value from Performance\r\nregistry is the first DWORD in Data section, LastCounter value is the second\r\nDWORD in Data section, and LastHelp value is the third DWORD in Data section.\r\n
0xc0000bc5 | Unable to update the performance counter strings of the %1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bc6 | Unable to update the performance counter explain text strings of the\r\n%1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bc7 | Index for %1!s! is corrupted. The index value is the first DWORD in Data section.\r\n
0xc0000bc8 | Cannot update %1!s! value of %2!s! key. The error code is the first DWORD in\r\nData section, updated value is the second DWORD in Data section.\r\n
0xc0000bc9 | Cannot update %1!s! value of %2!s! key. The error code is the first DWORD in\r\nData section.\r\n
0xc0000bca | %1!s! index range of service %2!s! is corrupted. The first DWORD in Data\r\nsection contains the first index used while the second DWORD in Data section\r\ncontains last index used.\r\n

### 5.2.3790.0, 5.2.3790.1830

Message identifier | Message string
--- | ---
0x400003e8 | Performance counters for the %1!s! (%2!s!) service were loaded successfully.\r\nThe Record Data contains the new index values assigned\r\nto this service.\r\n
0x400003e9 | Performance counters for the %1!s! (%2!s!) service were removed successfully.\r\nThe Record Data contains the new values of the system Last Counter and\r\nLast Help registry entries.\r\n
0x400003ea | Performance counters for the %1!s! (%2!s!) service are already in Performance\r\nRegistry, no need to re-install again.\r\n
0x800007d1 | No MOF file %2!s! was created for the %1!s! service. Before the performance\r\ncounters of this service can be collected by WMI a MOF file will need\r\nto be created and loaded manually. Contact the vendor of this service\r\nfor additional information.\r\n
0x800007d2 | The MOF file created for the %1!s! service could not be loaded. The\r\nerror code returned by the MOF Compiler is contained in the Record Data.\r\nBefore the performance counters of this service can be collected by WMI\r\nthe MOF file will need to be loaded manually. Contact the vendor of this\r\nservice for additional information.\r\n
0x800007d3 | The MOF file created for the %1!s! service cannot be deleted as requested.\r\nThe MOF file is required for the autorecover function.\r\n
0x800007d4 | The Performance registry value %1!s! string is corrupted. Skip string \"%2!s!\".\r\n
0x800007d5 | No COUNTER/HELP definition for Language %1!s!.\r\n
0x800007d6 | LastCounter and LastHelp values of performance registry is corrupted and\r\nneeds to be updated. The first and second DWORDs in Data Section are the\r\noriginal values while the third and forth DWORDs in Data Section are the\r\nupdated new values.\r\n
0x800007d7 | Cannot repair performance counters for %1!s! service. Please re-install\r\nmanually using LODCTR tool.\r\n
0xc0000bb8 | The performance strings in the registry do not match the index values\r\nstored in Performance registry key. The last index value from performance\r\nregistry key in the first DWORD in Data section, and the index of the\r\nlast string used in the second DWORD in Data section.\r\n
0xc0000bb9 | The performance counter name string value in the registry is incorrectly\r\nformatted. The bogus string is %1!s!, the bogus index value is the first\r\nDWORD in Data section while the last valid index values are the second and\r\nthird DWORD in Data section.\r\n
0xc0000bba | The performance counter explain text string value in the registry is\r\nincorrectly formatted. The bogus string is %1!s!, the bogus index value\r\nis the first DWORD in Data section while the last valid index values are\r\nthe second and third DWORD in Data section.\r\n
0xc0000bbb | The %1!s! key could not be opened or accessed in order to install counter\r\nstrings.The Win32 status returned by the call is the first DWORD in Data\r\nsection.\r\n
0xc0000bbc | The %1!s! registry value could not be read or was the incorrect data type.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bbd | Unable to open the registry key for the performance counter strings of\r\nthe %1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bbe | Unable to read the performance counter strings of the %1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bbf | Unable to read the performance counter explain text strings of the\r\n%1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bc0 | Unable to allocate a required memory buffer.\r\n
0xc0000bc1 | Installing the performance counter strings for service %1!s! (%2!s!) failed. The\r\nError code is the first DWORD in Data section.\r\n
0xc0000bc3 | Unloading the performance counter strings for service %1!s! (%2!s!) failed. The\r\nError code is the first DWORD in Data section.\r\n
0xc0000bc4 | The performance strings in the Performance registry value is corrupted when\r\nprocess %1!s! extension counter provider. BaseIndex value from Performance\r\nregistry is the first DWORD in Data section, LastCounter value is the second\r\nDWORD in Data section, and LastHelp value is the third DWORD in Data section.\r\n
0xc0000bc5 | Unable to update the performance counter strings of the %1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bc6 | Unable to update the performance counter explain text strings of the\r\n%1!s! language ID.\r\nThe Win32 status returned by the call is the first DWORD in Data section.\r\n
0xc0000bc7 | Index for %1!s! is corrupted. The index value is the first DWORD in Data section.\r\n
0xc0000bc8 | Cannot update %1!s! value of %2!s! key. The error code is the first DWORD in\r\nData section, updated value is the second DWORD in Data section.\r\n
0xc0000bc9 | Cannot update %1!s! value of %2!s! key. The error code is the first DWORD in\r\nData section.\r\n
0xc0000bca | %1!s! index range of service %2!s! is corrupted. The first DWORD in Data\r\nsection contains the first index used while the second DWORD in Data section\r\ncontains last index used.\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x400003e8 | Performance counters for the %1!s! (%2!s!) service were loaded successfully. The Record Data in the data section contains the new index values assigned to this service.\r\n
0x400003e9 | Performance counters for the %1!s! (%2!s!) service were removed successfully. The Record Data contains the new values of the system Last Counter and Last Help registry entries.\r\n
0x400003ea | Performance counters for the %1!s! (%2!s!) service are already in the registry, no need to reinstall. This only happens when you install the same counter twice. The second time install will generate this event.\r\n
0x800007d1 | No MOF file %2!s! was created for the %1!s! service. Before the performance counters of this service can be collected by WMI, a MOF file will need to be created and loaded manually. Contact the vendor of this service for additional information.\r\n
0x800007d2 | The MOF file created for the %1!s! service could not be loaded. The record data contains the error code returned by the MOF Compiler. Before the performance counters of this service can be collected by WMI, the MOF file will need to be loaded manually. Contact the vendor of this service for additional information.\r\n
0x800007d3 | The MOF file created for the %1!s! service cannot be deleted as requested. The automatic recovery function requires the MOF file.\r\n
0x800007d4 | The Performance registry value %1!s! string is corrupted. Skip string \"%2!s!\".\r\n
0x800007d5 | No COUNTER/HELP definition for Language %1!s!.\r\n
0x800007d6 | The LastCounter and LastHelp values of the performance registry are corrupted and need to be updated. The first and second DWORDs in the Data Section contain the original LastCounter and LastHelp values, respectively, while the third and fourth DWORDs in the Data Section contain the updated new values.\r\n
0x800007d7 | Cannot repair performance counters for %1!s! service. Reinstall the performance counters manually using the LODCTR tool.\r\n
0x90000001 | Microsoft-Windows-LoadPerf\r\n
0xc0000bb8 | The performance strings in the registry do not match the index values stored in Performance registry key. The first DWORD in the Data section contains the last index value from performance registry key and the second DWORD in the Data section contains the index of the last string.\r\n
0xc0000bb9 | The performance counter name string value in the registry is not formatted correctly. The malformed string is %1!s!. The first DWORD in the Data section contains the index value to the malformed string while the second and third DWORDs in the Data section contain the last valid index values.\r\n
0xc0000bba | The performance counter explain text string value in the registry is not formatted correctly. The malformed string is %1!s!. The first DWORD in the Data section contains the index value to the malformed string while the second and third DWORDs in the Data section contain the last valid index values.\r\n
0xc0000bbb | Unable to install counter strings because the %1!s! key could not be opened or accessed. The first DWORD in the Data section contains the Win32 error code.\r\n
0xc0000bbc | Unable to read the %1!s! registry value. The first DWORD in the Data section contains the Win32 error code.\r\n
0xc0000bbd | Unable to open the registry key for the performance counter strings defined for the %1!s! language ID. The first DWORD in the Data section contains the Win32 error code.\r\n
0xc0000bbe | Unable to read the performance counter strings defined for the %1!s! language ID. The first DWORD in the Data section contains the Win32 error code.\r\n
0xc0000bbf | Unable to read the performance counter explain text strings defined for the %1!s! language ID. The first DWORD in the Data section contains the Win32 error code.\r\n
0xc0000bc0 | Unable to allocate a required memory buffer.\r\n
0xc0000bc1 | Installing the performance counter strings for service %1!s! (%2!s!) failed. The first DWORD in the Data section contains the error code.\r\n
0xc0000bc3 | Unloading the performance counter strings for service %1!s! (%2!s!) failed. The first DWORD in the Data section contains the error code.\r\n
0xc0000bc4 | The performance strings in the Performance registry value is corrupted when process %1!s! extension counter provider. The BaseIndex value from the Performance registry is the first DWORD in the Data section, LastCounter value is the second DWORD in the Data section, and LastHelp value is the third DWORD in the Data section.\r\n
0xc0000bc5 | Unable to update the performance counter strings defined for the %1!s! language ID. The first DWORD in the Data section contains the error code.\r\n
0xc0000bc6 | Unable to update the performance counter explain text strings of the %1!s! language ID. The first DWORD in the Data section contains the error code.\r\n
0xc0000bc7 | Index for %1!s! is corrupted. The first DWORD in the Data section contains the index value.\r\n
0xc0000bc8 | Cannot update %1!s! value of %2!s! key. The first DWORD in the Data section contains the error code and the second DWORD contains the updated value.\r\n
0xc0000bc9 | Cannot update %1!s! value of %2!s! key. The first DWORD in the Data section contains the error code.\r\n
0xc0000bca | %1!s! index range of service %2!s! is corrupted. The first DWORD in the Data section contains the first index value used and the second DWORD in the Data section contains last index value used.\r\n

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.17763.1

Message identifier | Message string
--- | ---
0x000003e8 | Performance counters for the %1!s! (%2!s!) service were loaded successfully. The Record Data in the data section contains the new index values assigned to this service.\r\n
0x000003e9 | Performance counters for the %1!s! (%2!s!) service were removed successfully. The Record Data contains the new values of the system Last Counter and Last Help registry entries.\r\n
0x000003ea | Performance counters for the %1!s! (%2!s!) service are already in the registry, no need to reinstall. This only happens when you install the same counter twice. The second time install will generate this event.\r\n
0x000007d1 | No MOF file %2!s! was created for the %1!s! service. Before the performance counters of this service can be collected by WMI, a MOF file will need to be created and loaded manually. Contact the vendor of this service for additional information.\r\n
0x000007d2 | The MOF file created for the %1!s! service could not be loaded. The record data contains the error code returned by the MOF Compiler. Before the performance counters of this service can be collected by WMI, the MOF file will need to be loaded manually. Contact the vendor of this service for additional information.\r\n
0x000007d3 | The MOF file created for the %1!s! service cannot be deleted as requested. The automatic recovery function requires the MOF file.\r\n
0x000007d4 | The Performance registry value %1!s! string is corrupted. Skip string \"%2!s!\".\r\n
0x000007d5 | No COUNTER/HELP definition for Language %1!s!.\r\n
0x000007d6 | The LastCounter and LastHelp values of the performance registry are corrupted and need to be updated. The first and second DWORDs in the Data Section contain the original LastCounter and LastHelp values, respectively, while the third and fourth DWORDs in the Data Section contain the updated new values.\r\n
0x000007d7 | Cannot repair performance counters for %1!s! service. Reinstall the performance counters manually using the LODCTR tool.\r\n
0x00000bb8 | The performance strings in the registry do not match the index values stored in Performance registry key. The first DWORD in the Data section contains the last index value from performance registry key and the second DWORD in the Data section contains the index of the last string.\r\n
0x00000bb9 | The performance counter name string value in the registry is not formatted correctly. The malformed string is %1!s!. The first DWORD in the Data section contains the index value to the malformed string while the second and third DWORDs in the Data section contain the last valid index values.\r\n
0x00000bba | The performance counter explain text string value in the registry is not formatted correctly. The malformed string is %1!s!. The first DWORD in the Data section contains the index value to the malformed string while the second and third DWORDs in the Data section contain the last valid index values.\r\n
0x00000bbb | Unable to install counter strings because the %1!s! key could not be opened or accessed. The first DWORD in the Data section contains the Win32 error code.\r\n
0x00000bbc | Unable to read the %1!s! registry value. The first DWORD in the Data section contains the Win32 error code.\r\n
0x00000bbd | Unable to open the registry key for the performance counter strings defined for the %1!s! language ID. The first DWORD in the Data section contains the Win32 error code.\r\n
0x00000bbe | Unable to read the performance counter strings defined for the %1!s! language ID. The first DWORD in the Data section contains the Win32 error code.\r\n
0x00000bbf | Unable to read the performance counter explain text strings defined for the %1!s! language ID. The first DWORD in the Data section contains the Win32 error code.\r\n
0x00000bc0 | Unable to allocate a required memory buffer.\r\n
0x00000bc1 | Installing the performance counter strings for service %1!s! (%2!s!) failed. The first DWORD in the Data section contains the error code.\r\n
0x00000bc3 | Unloading the performance counter strings for service %1!s! (%2!s!) failed. The first DWORD in the Data section contains the error code.\r\n
0x00000bc4 | The performance strings in the Performance registry value is corrupted when process %1!s! extension counter provider. The BaseIndex value from the Performance registry is the first DWORD in the Data section, LastCounter value is the second DWORD in the Data section, and LastHelp value is the third DWORD in the Data section.\r\n
0x00000bc5 | Unable to update the performance counter strings defined for the %1!s! language ID. The first DWORD in the Data section contains the error code.\r\n
0x00000bc6 | Unable to update the performance counter explain text strings of the %1!s! language ID. The first DWORD in the Data section contains the error code.\r\n
0x00000bc7 | Index for %1!s! is corrupted. The first DWORD in the Data section contains the index value.\r\n
0x00000bc8 | Cannot update %1!s! value of %2!s! key. The first DWORD in the Data section contains the error code and the second DWORD contains the updated value.\r\n
0x00000bc9 | Cannot update %1!s! value of %2!s! key. The first DWORD in the Data section contains the error code.\r\n
0x00000bca | %1!s! index range of service %2!s! is corrupted. The first DWORD in the Data section contains the first index value used and the second DWORD in the Data section contains last index value used.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-LoadPerf\r\n
0x90000002 | Application\r\n
