## winmgmtr.dll

Path: %SystemRoot%\system32\wbem\WinMgmtR.dll

### 1.50.1085.0

Message identifier | Message string
--- | ---
0x40000001 | CIM Object Manager Service is starting.\r\n
0x40000002 | CIM Object Manager Service is stopping.\r\n
0x40000022 | WMI ADAP was unable to load the %1 performance library because it timed out on a call: %2\r\n
0x40000036 | WMI ADAP is starting\r\n
0x40000037 | WMI ADAP is stopping\r\n
0x80000006 | Repository corruption detected and recovered.\r\n
0x80000008 | Failed to create a backup repository for use when recovering a corrupt repository.  Check there is enough disk space.\r\n
0x8000000c | Failed to CoGetClassObject for provider "%1". Class not registered (%2).\r\n
0x8000000d | Failed to CoGetClassObject for provider "%1". No class factory available (%2).\r\n
0x8000000e | Failed to CoGetClassObject for provider "%1". Error reading the registration database (%2).\r\n
0x8000000f | Failed to CoGetClassObject for provider "%1". DLL not found (%2).\r\n
0x80000010 | Failed to CoGetClassObject for provider "%1". EXE not found (%2).\r\n
0x80000011 | Failed to CoGetClassObject for provider "%1". Access denied (%2).\r\n
0x80000012 | Failed to CoGetClassObject for provider "%1". EXE has error in image (%2).\r\n
0x80000013 | Failed to CoGetClassObject for provider "%1".EXE was launched, but it didn't register class object (%2).\r\n
0x80000014 | Failed to CoGetClassObject for provider "%1". Error code %2 was returned.\r\n
0x8000001a | WinMgmt core is already running. Multiple copies are not supported. This copy will terminate.\r\n
0x8000001d | The repository file was not the size we expected it to be.  This could have been because WinMgmt crashed, the system crashed, or you did not shut your machine down cleanly.  We had to delete the repository and create a new one.\r\n
0x8000001e | A WMI/WBEM client executed an asynchronous operation and failed to return from its implementation of IWbemObjectSink.\r\n
0x8000001f | An attempt was made to marshal a CIM object larger than 1 megabyte across process boundaries.  Objects must be less than 1 megabyte in encoded length.\r\n
0xc0000003 | CIM Object Manager cannot recognize repository file --- version mismatch.\r\n
0xc0000004 | Failed to load MOF %1 while recovering repository file.\r\n
0xc0000005 | Failed to open repository.\r\n
0xc0000007 | Repository corruption detected and recovery failed.\r\n
0xc0000009 | Several providers and/or the static database returned definitions\r\nfor class "%1".\r\nOnly one definition was reported. Until this misconfiguration is corrected,\r\nclients may receive incorrect class defition for "%1"\r\n
0xc000000a | Event filter with query "%2" could not be (re)activated in namespace "%1"\r\nbecause of error %3. Events may not be delivered through this filter until the\r\nproblem is corrected.\r\n
0xc000000b | Class provider "%1" installed in namespace "%2" failed to enumerate classes,\r\nreturning error code %3. Operations will continue as if the class provider\r\nhad no classes.  This provider-specific error condition needs to be corrected\r\nbefore this class provider can contribute to this namespace.\r\n
0xc0000015 | Event provider attempted to register a syntactically invalid query "%1".\r\nThe query will be ignored.\r\n
0xc0000016 | Event provider attempted to register an intrinsic event query "%1" for which\r\nthe set of target object classes could not be determined.\r\nThe query will be ignored.\r\n
0xc0000017 | Event provider attempted to register query "%1" which is too broad.  Event\r\nproviders cannot provide events that are provided by the system.\r\nThe query will be ignored.\r\n
0xc0000018 | Event provider attempted to register query "%1" whose target class "%2"\r\ndoes not exist.\r\nThe query will be ignored.\r\n
0xc0000019 | Event provider attempted to register query "%1" whose target class "%2"\r\nis not an event class.\r\nThe query will be ignored.\r\n
0xc000001b | WinMgmt could not open the repository file.  This could be due to insufficient security access to the "<%SystemRoot%>\System32\WBEM\Repository", insufficient disk space or insufficient memory.\r\n
0xc000001c | WinMgmt could not not initialise the core parts.  This could be due to a badly installed version of WinMgmt, insufficient disk space or insufficient memory.\r\n
0xc0000020 | WMI ADAP was unable to load the %1 performance library because it corrupted memory: %2\r\n
0xc0000021 | WMI ADAP was unable to load the %1 performance library because it threw an exception: %2\r\n
0xc0000023 | WMI ADAP was unable to load the %1 performance library because it returned invalid data: %2\r\n
0xc0000024 | WMI ADAP was unable to load the %1 performance library because it returned an invalid return code: %2\r\n
0xc0000025 | WMI ADAP was unable to load the %1 performance library due to an unknown problem within the library: %2\r\n
0xc0000026 | WMI ADAP was unable to create the object %1 for Performance Library %2 because an object of that name already exists\r\n
0xc0000027 | WMI ADAP was unable to create the object %1 for Performance Library %2 because property %3 already exists\r\n
0xc0000028 | WMI ADAP was unable to create the object %1 for Performance Library %2 because error %3 was returned\r\n
0xc0000029 | WMI ADAP was unable to create object index %1 for Performance Library %2 because no value was found in the 009 subkey\r\n
0xc000002a | WMI ADAP was unable to create object %1 for Performance Library %2 because no value was found for property index %3 in the 009 subkey\r\n
0xc000002b | WMI ADAP failed to connect to namespace %1 with the following error: %2\r\n
0xc000002c | WMI ADAP failed to get the class Win32_PerfRawData from the namespace %1 with the following error: %2\r\n
0xc000002d | WMI ADAP failed to enumerate subclasses of Win32_PerfRawData in the namespace %1 with the following error: %2\r\n
0xc000002e | WMI ADAP was unable to retrieve data from the PerfLib localization subkey: %1, error code: %2\r\n
0xc000002f | WMI ADAP was unable to retrieve data from the PerfLib subkey: %1, error code: %2\r\n
0xc0000030 | WMI ADAP was unable to save object %1 in namespace %2 due to the following error: %3\r\n
0xc0000031 | WMI ADAP was unable to remove object %1 from namespace %3 due to the following error: %3\r\n
0xc0000032 | WMI ADAP was unable to load the following performance library: %1, due to invalid entry point: %2\r\n
0xc0000033 | WMI ADAP was unable to load the following performance library: %1, with the following error: %2\r\n
0xc0000034 | WMI ADAP was unable to create the object %1 for Performance Library %2 because of an invalid property type at index %3\r\n
0xc0000035 | WMI ADAP was unable to create the name database for language id %1\r\n
0xc0000038 | WMI ADAP was unable to create a provider instance for the Generic Perf Counter Provider %1\r\n
0xc0000039 | WMI ADAP was unable to create the provider registration for the Generic Perf Couter Provider %1\r\n
0xc000003a | WMI ADAP was unable to create the Win32_Perf base class in %1: %2\r\n
0xc000003b | WMI ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc000003c | WMI ADAP was unable to process the performance libraries: %1\r\n
0xc000003d | WMI ADAP was unable to process the %1 performance library due to a time violation in the %2 function\r\n
0xc000003e | WMI ADAP was unable to process the %1 performance library since one of the data blobs reported to have classes but had zero size\r\n

### 5.1.2600.0, 5.2.3790.0

Message identifier | Message string
--- | ---
0x40000001 | CIM Object Manager Service is starting.\r\n
0x40000002 | CIM Object Manager Service is stopping.\r\n
0x40000022 | WMI ADAP was unable to load the %1 performance library because it timed out on a call: %2\r\n
0x40000036 | WMI ADAP is starting\r\n
0x40000037 | WMI ADAP is stopping\r\n
0x80000006 | Repository corruption detected and recovered.\r\n
0x80000008 | Failed to create a backup repository for use when recovering a corrupt repository.  Check there is enough disk space.\r\n
0x8000000c | Failed to CoGetClassObject for provider "%1". Class not registered (%2).\r\n
0x8000000d | Failed to CoGetClassObject for provider "%1". No class factory available (%2).\r\n
0x8000000e | Failed to CoGetClassObject for provider "%1". Error reading the registration database (%2).\r\n
0x8000000f | Failed to CoGetClassObject for provider "%1". DLL not found (%2).\r\n
0x80000010 | Failed to CoGetClassObject for provider "%1". EXE not found (%2).\r\n
0x80000011 | Failed to CoGetClassObject for provider "%1". Access denied (%2).\r\n
0x80000012 | Failed to CoGetClassObject for provider "%1". EXE has error in image (%2).\r\n
0x80000013 | Failed to CoGetClassObject for provider "%1".EXE was launched, but it didn't register class object (%2).\r\n
0x80000014 | Failed to CoGetClassObject for provider "%1". Error code %2 was returned.\r\n
0x8000001a | WinMgmt core is already running. Multiple copies are not supported. This copy will terminate.\r\n
0x8000001d | The repository file was not the size we expected it to be.  This could have been because WinMgmt crashed, the system crashed, or you did not shut your machine down cleanly.  We had to delete the repository and create a new one.\r\n
0x8000001e | A WMI/WBEM client executed an asynchronous operation and failed to return from its implementation of IWbemObjectSink.\r\n
0x8000001f | An attempt was made to marshal a CIM object larger than 1 megabyte across process boundaries.  Objects must be less than 1 megabyte in encoded length.\r\n
0x8000003f | A provider, %1, has been registered in the WMI namespace, %2, to use the LocalSystem account.  This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x80000040 | The named section %1, was created with insufficient size, this could constitute a Denial of Service attack.\r\n\r\n\r\n
0xc0000003 | CIM Object Manager cannot recognize repository file --- version mismatch.\r\n
0xc0000004 | Failed to load MOF %1 while recovering repository file.\r\n
0xc0000005 | Failed to open repository.\r\n
0xc0000007 | Repository corruption detected and recovery failed.\r\n
0xc0000009 | Several providers and/or the static database returned definitions\r\nfor class "%1".\r\nOnly one definition was reported. Until this misconfiguration is corrected,\r\nclients may receive incorrect class defition for "%1"\r\n
0xc000000a | Event filter with query "%2" could not be (re)activated in namespace "%1"\r\nbecause of error %3. Events may not be delivered through this filter until the\r\nproblem is corrected.\r\n
0xc000000b | Class provider "%1" installed in namespace "%2" failed to enumerate classes,\r\nreturning error code %3. Operations will continue as if the class provider\r\nhad no classes.  This provider-specific error condition needs to be corrected\r\nbefore this class provider can contribute to this namespace.\r\n
0xc0000015 | Event provider attempted to register a syntactically invalid query "%1".\r\nThe query will be ignored.\r\n
0xc0000016 | Event provider attempted to register an intrinsic event query "%1" for which\r\nthe set of target object classes could not be determined.\r\nThe query will be ignored.\r\n
0xc0000017 | Event provider attempted to register query "%1" which is too broad.  Event\r\nproviders cannot provide events that are provided by the system.\r\nThe query will be ignored.\r\n
0xc0000018 | Event provider attempted to register query "%1" whose target class "%2"\r\ndoes not exist.\r\nThe query will be ignored.\r\n
0xc0000019 | Event provider attempted to register query "%1" whose target class "%2"\r\nis not an event class.\r\nThe query will be ignored.\r\n
0xc000001b | WinMgmt could not open the repository file.  This could be due to insufficient security access to the "<%SystemRoot%>\System32\WBEM\Repository", insufficient disk space or insufficient memory.\r\n
0xc000001c | WinMgmt could not initialize the core parts.  This could be due to a badly installed version of WinMgmt, WinMgmt repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc0000020 | WMI ADAP was unable to load the %1 performance library because it corrupted memory: %2\r\n
0xc0000021 | WMI ADAP was unable to load the %1 performance library because it threw an exception: %2\r\n
0xc0000023 | WMI ADAP was unable to load the %1 performance library because it returned invalid data: %2\r\n
0xc0000024 | WMI ADAP was unable to load the %1 performance library because it returned an invalid return code: %2\r\n
0xc0000025 | WMI ADAP was unable to load the %1 performance library due to an unknown problem within the library: %2\r\n
0xc0000026 | WMI ADAP was unable to create the object %1 for Performance Library %2 because an object of that name already exists\r\n
0xc0000027 | WMI ADAP was unable to create the object %1 for Performance Library %2 because property %3 already exists\r\n
0xc0000028 | WMI ADAP was unable to create the object %1 for Performance Library %2 because error %3 was returned\r\n
0xc0000029 | WMI ADAP was unable to create object index %1 for Performance Library %2 because no value was found in the 009 subkey\r\n
0xc000002a | WMI ADAP was unable to create object %1 for Performance Library %2 because no value was found for property index %3 in the 009 subkey\r\n
0xc000002b | WMI ADAP failed to connect to namespace %1 with the following error: %2\r\n
0xc000002c | WMI ADAP failed to get the class Win32_PerfRawData from the namespace %1 with the following error: %2\r\n
0xc000002d | WMI ADAP failed to enumerate subclasses of Win32_PerfRawData in the namespace %1 with the following error: %2\r\n
0xc000002e | WMI ADAP was unable to retrieve data from the PerfLib localization subkey: %1, error code: %2\r\n
0xc000002f | WMI ADAP was unable to retrieve data from the PerfLib subkey: %1, error code: %2\r\n
0xc0000030 | WMI ADAP was unable to save object %1 in namespace %2 due to the following error: %3\r\n
0xc0000031 | WMI ADAP was unable to remove object %1 from namespace %2 due to the following error: %3\r\n
0xc0000032 | WMI ADAP was unable to load the following performance library: %1, due to invalid entry point: %2\r\n
0xc0000033 | WMI ADAP was unable to load the following performance library: %1, with the following error: %2\r\n
0xc0000034 | WMI ADAP was unable to create the object %1 for Performance Library %2 because of an invalid property type for property %3\r\n
0xc0000035 | WMI ADAP was unable to create the name database for language id %1\r\n
0xc0000038 | WMI ADAP was unable to create a provider instance for the Generic Perf Counter Provider %1\r\n
0xc0000039 | WMI ADAP was unable to create the provider registration for the Generic Perf Couter Provider %1\r\n
0xc000003a | WMI ADAP was unable to create the Win32_Perf base class in %1: %2\r\n
0xc000003b | WMI ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc000003c | WMI ADAP was unable to process the performance libraries: %1\r\n
0xc000003d | WMI ADAP was unable to process the %1 performance library due to a time violation in the %2 function\r\n
0xc000003e | WMI ADAP was unable to process the %1 performance library since one of the data blobs reported to have classes but had zero size\r\n

### 5.2.3790.1830

Message identifier | Message string
--- | ---
0x40000001 | CIM Object Manager Service is starting.\r\n
0x40000002 | CIM Object Manager Service is stopping.\r\n
0x40000022 | WMI ADAP was unable to load the %1 performance library because it timed out on a call: %2\r\n
0x40000036 | WMI ADAP is starting\r\n
0x40000037 | WMI ADAP is stopping\r\n
0x80000006 | Repository corruption detected and recovered.\r\n
0x80000008 | Failed to create a backup repository for use when recovering a corrupt repository.  Check there is enough disk space.\r\n
0x8000000c | Failed to CoGetClassObject for provider "%1". Class not registered (%2).\r\n
0x8000000d | Failed to CoGetClassObject for provider "%1". No class factory available (%2).\r\n
0x8000000e | Failed to CoGetClassObject for provider "%1". Error reading the registration database (%2).\r\n
0x8000000f | Failed to CoGetClassObject for provider "%1". DLL not found (%2).\r\n
0x80000010 | Failed to CoGetClassObject for provider "%1". EXE not found (%2).\r\n
0x80000011 | Failed to CoGetClassObject for provider "%1". Access denied (%2).\r\n
0x80000012 | Failed to CoGetClassObject for provider "%1". EXE has error in image (%2).\r\n
0x80000013 | Failed to CoGetClassObject for provider "%1".EXE was launched, but it didn't register class object (%2).\r\n
0x80000014 | Failed to CoGetClassObject for provider "%1". Error code %2 was returned.\r\n
0x8000001a | WinMgmt core is already running. Multiple copies are not supported. This copy will terminate.\r\n
0x8000001d | The repository file was not the size we expected it to be.  This could have been because WinMgmt crashed, the system crashed, or you did not shut your machine down cleanly.  We had to delete the repository and create a new one.\r\n
0x8000001e | A WMI/WBEM client executed an asynchronous operation and failed to return from its implementation of IWbemObjectSink.\r\n
0x8000001f | An attempt was made to marshal a CIM object larger than 1 megabyte across process boundaries.  Objects must be less than 1 megabyte in encoded length.\r\n
0x8000003f | A provider, %1, has been registered in the WMI namespace, %2, to use the LocalSystem account.  This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x80000040 | The named section %1, was created with insufficient size, this could constitute a Denial of Service attack.\r\n\r\n
0xc0000003 | CIM Object Manager cannot recognize repository file --- version mismatch.\r\n
0xc0000004 | Failed to load MOF %1 while recovering repository file.\r\n
0xc0000005 | Failed to open repository.\r\n
0xc0000007 | Repository corruption detected and recovery failed.\r\n
0xc0000009 | Several providers and/or the static database returned definitions\r\nfor class "%1".\r\nOnly one definition was reported. Until this misconfiguration is corrected,\r\nclients may receive incorrect class defition for "%1"\r\n
0xc000000a | Event filter with query "%2" could not be (re)activated in namespace "%1"\r\nbecause of error %3. Events may not be delivered through this filter until the\r\nproblem is corrected.\r\n
0xc000000b | Class provider "%1" installed in namespace "%2" failed to enumerate classes,\r\nreturning error code %3. Operations will continue as if the class provider\r\nhad no classes.  This provider-specific error condition needs to be corrected\r\nbefore this class provider can contribute to this namespace.\r\n
0xc0000015 | Event provider attempted to register a syntactically invalid query "%1".\r\nThe query will be ignored.\r\n
0xc0000016 | Event provider attempted to register an intrinsic event query "%1" for which\r\nthe set of target object classes could not be determined.\r\nThe query will be ignored.\r\n
0xc0000017 | Event provider attempted to register query "%1" which is too broad.  Event\r\nproviders cannot provide events that are provided by the system.\r\nThe query will be ignored.\r\n
0xc0000018 | Event provider attempted to register query "%1" whose target class "%2"\r\ndoes not exist.\r\nThe query will be ignored.\r\n
0xc0000019 | Event provider attempted to register query "%1" whose target class "%2"\r\nis not an event class.\r\nThe query will be ignored.\r\n
0xc000001b | WinMgmt could not open the repository file.  This could be due to insufficient security access to the "<%SystemRoot%>\System32\WBEM\Repository", insufficient disk space or insufficient memory.\r\n
0xc000001c | WinMgmt could not initialize the core parts.  This could be due to a badly installed version of WinMgmt, WinMgmt repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc0000020 | WMI ADAP was unable to load the %1 performance library because it corrupted memory: %2\r\n
0xc0000021 | WMI ADAP was unable to load the %1 performance library because it threw an exception: %2\r\n
0xc0000023 | WMI ADAP was unable to load the %1 performance library because it returned invalid data: %2\r\n
0xc0000024 | WMI ADAP was unable to load the %1 performance library because it returned an invalid return code: %2\r\n
0xc0000025 | WMI ADAP was unable to load the %1 performance library due to an unknown problem within the library: %2\r\n
0xc0000026 | WMI ADAP was unable to create the object %1 for Performance Library %2 because an object of that name already exists\r\n
0xc0000027 | WMI ADAP was unable to create the object %1 for Performance Library %2 because property %3 already exists\r\n
0xc0000028 | WMI ADAP was unable to create the object %1 for Performance Library %2 because error %3 was returned\r\n
0xc0000029 | WMI ADAP was unable to create object index %1 for Performance Library %2 because no value was found in the 009 subkey\r\n
0xc000002a | WMI ADAP was unable to create object %1 for Performance Library %2 because no value was found for property index %3 in the 009 subkey\r\n
0xc000002b | WMI ADAP failed to connect to namespace %1 with the following error: %2\r\n
0xc000002c | WMI ADAP failed to get the class Win32_PerfRawData from the namespace %1 with the following error: %2\r\n
0xc000002d | WMI ADAP failed to enumerate subclasses of Win32_PerfRawData in the namespace %1 with the following error: %2\r\n
0xc000002e | WMI ADAP was unable to retrieve data from the PerfLib localization subkey: %1, error code: %2\r\n
0xc000002f | WMI ADAP was unable to retrieve data from the PerfLib subkey: %1, error code: %2\r\n
0xc0000030 | WMI ADAP was unable to save object %1 in namespace %2 due to the following error: %3\r\n
0xc0000031 | WMI ADAP was unable to remove object %1 from namespace %2 due to the following error: %3\r\n
0xc0000032 | WMI ADAP was unable to load the following performance library: %1, due to invalid entry point: %2\r\n
0xc0000033 | WMI ADAP was unable to load the following performance library: %1, with the following error: %2\r\n
0xc0000034 | WMI ADAP was unable to create the object %1 for Performance Library %2 because of an invalid property type for property %3\r\n
0xc0000035 | WMI ADAP was unable to create the name database for language id %1\r\n
0xc0000038 | WMI ADAP was unable to create a provider instance for the Generic Perf Counter Provider %1\r\n
0xc0000039 | WMI ADAP was unable to create the provider registration for the Generic Perf Couter Provider %1\r\n
0xc000003a | WMI ADAP was unable to create the Win32_Perf base class in %1: %2\r\n
0xc000003b | WMI ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc000003c | WMI ADAP was unable to process the performance libraries: %1\r\n
0xc000003d | WMI ADAP was unable to process the %1 performance library due to a time violation in the %2 function\r\n
0xc000003e | WMI ADAP was unable to process the %1 performance library since one of the data blobs reported to have classes but had zero size\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x400015e0 | The Windows Management Instrumentation Service detected an inconsistency with the WMI repository in the directory %windir%\system32\wbem\repository and was not able to recover it.  The WMI repository will now be deleted, A new repository will be created based on the auto-recovery mechanism.\r\n
0x8000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x90000001 | Microsoft-Windows-WMI\r\n
0xb1000001 | GroupOperationId = %1; OperationId = %2; Operation = %3; ClientMachine = %4; User = %5; ClientProcessId = %6; NamespaceName = %7\r\n
0xb1000002 | ProviderInfo for GroupOperationId = %1; Operation = %2; ProviderName = %3; ProviderGuid = %4; Path = %5\r\n
0xb1000003 | Stop OperationId = %1\r\n
0xc0000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0xc000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0xc0000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0xc0000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0xc0000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0xc0000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0xc0000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0xc000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0xc0000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0xc000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0xc000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc00015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0xc00015e5 | Access to the %1 namespace was denied because the namespace is marked with RequiresEncryption but the script or application attempted to connect to this namespace with an authentication level below Pkt_Privacy. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0xc00015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0xc00015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4\r\n
0xc00015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0xc00015ef | Windows Management Instrumentation Service started sucessfully\r\n
0xc00015f0 | Windows Management Instrumentation Repository successfully recreated using Autorecovery mechanism.\r\n
0xc00015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x10000038 | Classic\r\n
0x400015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x51000004 | Information\r\n
0x8000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x90000001 | Microsoft-Windows-WMI\r\n
0x91000001 | Microsoft-Windows-WMI-Activity\r\n
0xb1000001 | GroupOperationId = %1; OperationId = %2; Operation = %3; ClientMachine = %4; User = %5; ClientProcessId = %6; NamespaceName = %7\r\n
0xb1000002 | ProviderInfo for GroupOperationId = %1; Operation = %2; ProviderName = %3; ProviderGuid = %4; Path = %5\r\n
0xb1000003 | Stop OperationId = %1\r\n
0xc0000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0xc000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0xc0000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0xc0000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0xc0000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0xc0000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0xc0000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0xc000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0xc0000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0xc000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0xc000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc0000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0xc0000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0xc0000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0xc0000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0xc00015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0xc00015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0xc00015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0xc00015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0xc00015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0xc00015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0xc00015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4\r\n
0xc00015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0xc00015ef | Windows Management Instrumentation Service started sucessfully\r\n
0xc00015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0xc00015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0xc00015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n

### 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0x0000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0x00000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0x00000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0x00000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0x00000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0x00000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0x0000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0x00000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0x0000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0x0000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0x0000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x00000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0x00000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0x00000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0x00000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0x000015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x000015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0x000015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0x000015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0x000015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0x000015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0x000015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0x000015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0x000015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0x000015ef | Windows Management Instrumentation Service started sucessfully\r\n
0x000015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0x000015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0x000015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n
0x10000038 | Classic\r\n
0x400015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x8000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x90000001 | Microsoft-Windows-WMI\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-WMI-Activity\r\n
0xb1000001 | GroupOperationId = %1; OperationId = %2; Operation = %3; ClientMachine = %4; User = %5; ClientProcessId = %6; NamespaceName = %7\r\n
0xb1000002 | ProviderInfo for GroupOperationId = %1; Operation = %2; ProviderName = %3; ProviderGuid = %4; Path = %5\r\n
0xb1000003 | Stop OperationId = %1\r\n
0xb100000b | CorrelationId = %1; GroupOperationId = %2; OperationId = %3; Operation = %4; ClientMachine = %5; User = %6; ClientProcessId = %7; NamespaceName = %8\r\n
0xb100000c | ProviderInfo for GroupOperationId = %1; Operation = %2; HostID = %3; ProviderName = %4; ProviderGuid = %5; Path = %6\r\n
0xb100000d | Stop OperationId = %1; ResultCode = %2\r\n
0xb100000e | OperationId = %1; Operation = %2; Channel = %3; Message = %4\r\n
0xb100000f | OperationId = %1; Operation = %2; ErrorID = %3; ErrorCategory = %4; Message = %5; TargetName = %6\r\n
0xb1000010 | OperationId = %1; Operation = %2; ErrorID = %3; Message = %4\r\n
0xb1000011 | CorrelationId = %1; ProcessId = %2; Protocol = %3; Operation = %4; User = %5; Namespace = %6\r\n
0xb1000012 | WMI Events were dropped. ConsumerType = %1;Possiblecause = %2\r\n
0xb1000013 | Performing delete operation on the WMI repository. OperationID = %1; Operation = %2\r\n
0xb1000014 | Performing Update operation on the WMI repository. OperationID = %1; Operation = %2; Flags = %3\r\n
0xb1000032 | Activity Transfer\r\n
0xb1000064 | ComponentName = %1; MessageDetail = %2; FileName = %3\r\n
0xb1000065 | ComponentName = %1; ErrorId = %2; ErrorDetail = %3; FileName = %4\r\n
0xb10016e1 | %1 provider started with result code %2. HostProcess = %3; ProcessID = %4; ProviderPath = %5\r\n
0xb10016e2 | Id = %1; ClientMachine = %2; User = %3; ClientProcessId = %4; Component = %5; Operation = %6; ResultCode = %7; PossibleCause = %8\r\n
0xc0000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0xc000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0xc0000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0xc0000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0xc0000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0xc0000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0xc0000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0xc000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0xc0000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0xc000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0xc000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc0000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0xc0000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0xc0000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0xc0000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0xc00015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0xc00015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0xc00015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0xc00015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0xc00015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0xc00015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0xc00015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0xc00015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0xc00015ef | Windows Management Instrumentation Service started sucessfully\r\n
0xc00015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0xc00015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0xc00015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x00000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0x0000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0x00000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0x00000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0x00000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0x00000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0x00000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0x0000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0x00000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0x0000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0x0000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0x0000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x00000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0x00000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0x00000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0x00000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0x000015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x000015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0x000015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0x000015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0x000015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0x000015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0x000015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0x000015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0x000015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0x000015ef | Windows Management Instrumentation Service started sucessfully\r\n
0x000015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0x000015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0x000015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n
0x10000038 | Classic\r\n
0x400015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x8000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x90000001 | Microsoft-Windows-WMI\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-WMI-Activity\r\n
0xb1000001 | GroupOperationId = %1; OperationId = %2; Operation = %3; ClientMachine = %4; User = %5; ClientProcessId = %6; NamespaceName = %7\r\n
0xb1000002 | ProviderInfo for GroupOperationId = %1; Operation = %2; ProviderName = %3; ProviderGuid = %4; Path = %5\r\n
0xb1000003 | Stop OperationId = %1\r\n
0xb100000b | CorrelationId = %1; GroupOperationId = %2; OperationId = %3; Operation = %4; ClientMachine = %5; User = %6; ClientProcessId = %7; NamespaceName = %8\r\n
0xb100000c | ProviderInfo for GroupOperationId = %1; Operation = %2; HostID = %3; ProviderName = %4; ProviderGuid = %5; Path = %6\r\n
0xb100000d | Stop OperationId = %1; ResultCode = %2\r\n
0xb100000e | OperationId = %1; Operation = %2; Channel = %3; Message = %4\r\n
0xb100000f | OperationId = %1; Operation = %2; ErrorID = %3; ErrorCategory = %4; Message = %5; TargetName = %6\r\n
0xb1000010 | OperationId = %1; Operation = %2; ErrorID = %3; Message = %4\r\n
0xb1000011 | CorrelationId = %1; ProcessId = %2; Protocol = %3; Operation = %4; User = %5; Namespace = %6\r\n
0xb1000012 | WMI Events were dropped. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000013 | Performing delete operation on the WMI repository. OperationID = %1; Operation = %2\r\n
0xb1000014 | Performing Update operation on the WMI repository. OperationID = %1; Operation = %2; Flags = %3\r\n
0xb1000015 | WMI Events were bound. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000032 | Activity Transfer\r\n
0xb1000064 | ComponentName = %1; MessageDetail = %2; FileName = %3\r\n
0xb1000065 | ComponentName = %1; ErrorId = %2; ErrorDetail = %3; FileName = %4\r\n
0xb10016e1 | %1 provider started with result code %2. HostProcess = %3; ProcessID = %4; ProviderPath = %5\r\n
0xb10016e2 | Id = %1; ClientMachine = %2; User = %3; ClientProcessId = %4; Component = %5; Operation = %6; ResultCode = %7; PossibleCause = %8\r\n
0xb10016e3 | Namespace = %1; NotificationQuery = %2; OwnerName = %3; HostProcessID = %4;  Provider= %5, queryID = %6; PossibleCause = %7\r\n
0xb10016e4 | Namespace = %1; NotificationQuery = %2; UserName = %3; ClientProcessID = %4, ClientMachine = %5; PossibleCause = %6\r\n
0xc0000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0xc000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0xc0000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0xc0000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0xc0000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0xc0000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0xc0000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0xc000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0xc0000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0xc000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0xc000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc0000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0xc0000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0xc0000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0xc0000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0xc00015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0xc00015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0xc00015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0xc00015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0xc00015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0xc00015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0xc00015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0xc00015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0xc00015ef | Windows Management Instrumentation Service started sucessfully\r\n
0xc00015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0xc00015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0xc00015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n

### 10.0.14393.0, 10.0.15063.0

Message identifier | Message string
--- | ---
0x00000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0x0000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0x00000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0x00000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0x00000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0x00000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0x00000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0x0000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0x00000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0x0000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0x0000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0x0000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x00000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0x00000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0x00000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0x00000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0x000015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x000015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0x000015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0x000015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0x000015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0x000015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0x000015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0x000015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0x000015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0x000015ef | Windows Management Instrumentation Service started sucessfully\r\n
0x000015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0x000015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0x000015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n
0x10000038 | Classic\r\n
0x400015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x8000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x90000001 | Microsoft-Windows-WMI\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-WMI-Activity\r\n
0xb1000001 | GroupOperationId = %1; OperationId = %2; Operation = %3; ClientMachine = %4; User = %5; ClientProcessId = %6; NamespaceName = %7\r\n
0xb1000002 | ProviderInfo for GroupOperationId = %1; Operation = %2; ProviderName = %3; ProviderGuid = %4; Path = %5\r\n
0xb1000003 | Stop OperationId = %1\r\n
0xb100000b | CorrelationId = %1; GroupOperationId = %2; OperationId = %3; Operation = %4; ClientMachine = %5; User = %6; ClientProcessId = %7; NamespaceName = %8\r\n
0xb100000c | ProviderInfo for GroupOperationId = %1; Operation = %2; HostID = %3; ProviderName = %4; ProviderGuid = %5; Path = %6\r\n
0xb100000d | Stop OperationId = %1; ResultCode = %2\r\n
0xb100000e | OperationId = %1; Operation = %2; Channel = %3; Message = %4\r\n
0xb100000f | OperationId = %1; Operation = %2; ErrorID = %3; ErrorCategory = %4; Message = %5; TargetName = %6\r\n
0xb1000010 | OperationId = %1; Operation = %2; ErrorID = %3; Message = %4\r\n
0xb1000011 | CorrelationId = %1; ProcessId = %2; Protocol = %3; Operation = %4; User = %5; Namespace = %6\r\n
0xb1000012 | WMI Events were dropped. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000013 | Performing delete operation on the WMI repository. OperationID = %1; Operation = %2\r\n
0xb1000014 | Performing Update operation on the WMI repository. OperationID = %1; Operation = %2; Flags = %3\r\n
0xb1000015 | WMI Events were bound. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000032 | Activity Transfer\r\n
0xb1000064 | ComponentName = %1; MessageDetail = %2; FileName = %3\r\n
0xb1000065 | ComponentName = %1; ErrorId = %2; ErrorDetail = %3; FileName = %4\r\n
0xb10016e1 | %1 provider started with result code %2. HostProcess = %3; ProcessID = %4; ProviderPath = %5\r\n
0xb10016e2 | Id = %1; ClientMachine = %2; User = %3; ClientProcessId = %4; Component = %5; Operation = %6; ResultCode = %7; PossibleCause = %8\r\n
0xb10016e3 | Namespace = %1; NotificationQuery = %2; OwnerName = %3; HostProcessID = %4;  Provider= %5, queryID = %6; PossibleCause = %7\r\n
0xb10016e4 | Namespace = %1; NotificationQuery = %2; UserName = %3; ClientProcessID = %4, ClientMachine = %5; PossibleCause = %6\r\n
0xb10016e5 | Namespace = %1; Eventfilter = %2 (refer to its activate eventid:5859); Consumer = %3; PossibleCause = %4\r\n
0xc0000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0xc000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0xc0000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0xc0000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0xc0000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0xc0000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0xc0000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0xc000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0xc0000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0xc000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0xc000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc0000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0xc0000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0xc0000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0xc0000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0xc00015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0xc00015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0xc00015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0xc00015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0xc00015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0xc00015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0xc00015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0xc00015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0xc00015ef | Windows Management Instrumentation Service started sucessfully\r\n
0xc00015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0xc00015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0xc00015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x00000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0x0000000a | Event filter with query "%1" could not be reactivated in namespace "%2" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0x00000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0x00000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0x00000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0x00000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0x00000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0x0000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0x00000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0x0000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0x0000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0x0000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x00000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0x00000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0x00000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0x00000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0x000015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x000015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0x000015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0x000015e4 | The Windows Management Instrumentation service encountered the error %1 and was not able to restore from the following backup repository: %2.\r\n
0x000015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0x000015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0x000015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0x000015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0x000015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0x000015ef | Windows Management Instrumentation Service started sucessfully\r\n
0x000015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0x000015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0x000015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n
0x10000038 | Classic\r\n
0x400015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x8000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x90000001 | Microsoft-Windows-WMI\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-WMI-Activity\r\n
0xb1000001 | GroupOperationId = %1; OperationId = %2; Operation = %3; ClientMachine = %4; User = %5; ClientProcessId = %6; NamespaceName = %7\r\n
0xb1000002 | ProviderInfo for GroupOperationId = %1; Operation = %2; ProviderName = %3; ProviderGuid = %4; Path = %5\r\n
0xb1000003 | Stop OperationId = %1\r\n
0xb100000b | CorrelationId = %1; GroupOperationId = %2; OperationId = %3; Operation = %4; ClientMachine = %5; User = %6; ClientProcessId = %7; NamespaceName = %8\r\n
0xb100000c | ProviderInfo for GroupOperationId = %1; Operation = %2; HostID = %3; ProviderName = %4; ProviderGuid = %5; Path = %6\r\n
0xb100000d | Stop OperationId = %1; ResultCode = %2\r\n
0xb100000e | OperationId = %1; Operation = %2; Channel = %3; Message = %4\r\n
0xb100000f | OperationId = %1; Operation = %2; ErrorID = %3; ErrorCategory = %4; Message = %5; TargetName = %6\r\n
0xb1000010 | OperationId = %1; Operation = %2; ErrorID = %3; Message = %4\r\n
0xb1000011 | CorrelationId = %1; ProcessId = %2; Protocol = %3; Operation = %4; User = %5; Namespace = %6\r\n
0xb1000012 | WMI Events were dropped. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000013 | Performing delete operation on the WMI repository. OperationID = %1; Operation = %2\r\n
0xb1000014 | Performing Update operation on the WMI repository. OperationID = %1; Operation = %2; Flags = %3\r\n
0xb1000015 | WMI Events were bound. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000032 | Activity Transfer\r\n
0xb1000064 | ComponentName = %1; MessageDetail = %2; FileName = %3\r\n
0xb1000065 | ComponentName = %1; ErrorId = %2; ErrorDetail = %3; FileName = %4\r\n
0xb10016e1 | %1 provider started with result code %2. HostProcess = %3; ProcessID = %4; ProviderPath = %5\r\n
0xb10016e2 | Id = %1; ClientMachine = %2; User = %3; ClientProcessId = %4; Component = %5; Operation = %6; ResultCode = %7; PossibleCause = %8\r\n
0xb10016e3 | Namespace = %1; NotificationQuery = %2; OwnerName = %3; HostProcessID = %4;  Provider= %5, queryID = %6; PossibleCause = %7\r\n
0xb10016e4 | Namespace = %1; NotificationQuery = %2; UserName = %3; ClientProcessID = %4, ClientMachine = %5; PossibleCause = %6\r\n
0xb10016e5 | Namespace = %1; Eventfilter = %2 (refer to its activate eventid:5859); Consumer = %3; PossibleCause = %4\r\n
0xc0000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0xc000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0xc0000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0xc0000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0xc0000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0xc0000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0xc0000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0xc000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0xc0000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0xc000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0xc000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc0000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0xc0000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0xc0000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0xc0000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0xc00015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0xc00015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0xc00015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0xc00015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0xc00015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0xc00015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0xc00015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0xc00015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0xc00015ef | Windows Management Instrumentation Service started sucessfully\r\n
0xc00015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0xc00015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0xc00015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x00000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0x0000000a | Event filter with query "%1" could not be reactivated in namespace "%2" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0x00000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0x00000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0x00000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0x00000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0x00000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0x0000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0x00000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0x0000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0x0000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0x0000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x00000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0x00000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0x00000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0x00000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0x000015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x000015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0x000015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0x000015e4 | The Windows Management Instrumentation service encountered the error %1 and was not able to restore from the following backup repository: %2.\r\n
0x000015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0x000015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0x000015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0x000015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0x000015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0x000015ef | Windows Management Instrumentation Service started sucessfully\r\n
0x000015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0x000015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0x000015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n
0x10000038 | Classic\r\n
0x400015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x8000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x90000001 | Microsoft-Windows-WMI\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-WMI-Activity\r\n
0xb1000001 | GroupOperationId = %1; OperationId = %2; Operation = %3; ClientMachine = %4; User = %5; ClientProcessId = %6; NamespaceName = %7\r\n
0xb1000002 | ProviderInfo for GroupOperationId = %1; Operation = %2; ProviderName = %3; ProviderGuid = %4; Path = %5\r\n
0xb1000003 | Stop OperationId = %1\r\n
0xb100000b | CorrelationId = %1; GroupOperationId = %2; OperationId = %3; Operation = %4; ClientMachine = %5; User = %7; ClientProcessId = %8; NamespaceName = %9\r\n
0xb100000c | ProviderInfo for GroupOperationId = %1; Operation = %2; HostID = %3; ProviderName = %4; ProviderGuid = %5; Path = %6\r\n
0xb100000d | Stop OperationId = %1; ResultCode = %2\r\n
0xb100000e | OperationId = %1; Operation = %2; Channel = %3; Message = %4\r\n
0xb100000f | OperationId = %1; Operation = %2; ErrorID = %3; ErrorCategory = %4; Message = %5; TargetName = %6\r\n
0xb1000010 | OperationId = %1; Operation = %2; ErrorID = %3; Message = %4\r\n
0xb1000011 | CorrelationId = %1; ProcessId = %2; Protocol = %3; Operation = %4; User = %5; Namespace = %6\r\n
0xb1000012 | WMI Events were dropped. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000013 | Performing delete operation on the WMI repository. OperationID = %1; Operation = %2\r\n
0xb1000014 | Performing Update operation on the WMI repository. OperationID = %1; Operation = %2; Flags = %3\r\n
0xb1000015 | WMI Events were bound. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000016 | CorrelationId = %1; GroupOperationId = %2; OperationId = %3; ClassName= %4; MethodName = %5; ImplementationClass = %6; ClientMachine = %7; User = %9; ClientProcessId = %10; NamespaceName = %12\r\n
0xb1000032 | Activity Transfer\r\n
0xb1000064 | ComponentName = %1; MessageDetail = %2; FileName = %3\r\n
0xb1000065 | ComponentName = %1; ErrorId = %2; ErrorDetail = %3; FileName = %4\r\n
0xb10016e1 | %1 provider started with result code %2. HostProcess = %3; ProcessID = %4; ProviderPath = %5\r\n
0xb10016e2 | Id = %1; ClientMachine = %2; User = %3; ClientProcessId = %4; Component = %5; Operation = %6; ResultCode = %7; PossibleCause = %8\r\n
0xb10016e3 | Namespace = %1; NotificationQuery = %2; OwnerName = %3; HostProcessID = %4;  Provider= %5, queryID = %6; PossibleCause = %7\r\n
0xb10016e4 | Namespace = %1; NotificationQuery = %2; UserName = %3; ClientProcessID = %4, ClientMachine = %5; PossibleCause = %6\r\n
0xb10016e5 | Namespace = %1; Eventfilter = %2 (refer to its activate eventid:5859); Consumer = %3; PossibleCause = %4\r\n
0xc0000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0xc000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0xc0000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0xc0000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0xc0000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0xc0000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0xc0000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0xc000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0xc0000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0xc000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0xc000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc0000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0xc0000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0xc0000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0xc0000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0xc00015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0xc00015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0xc00015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0xc00015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0xc00015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0xc00015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0xc00015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0xc00015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0xc00015ef | Windows Management Instrumentation Service started sucessfully\r\n
0xc00015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0xc00015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0xc00015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n

### 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0x0000000a | Event filter with query "%1" could not be reactivated in namespace "%2" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0x00000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0x00000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0x00000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0x00000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0x00000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0x0000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0x0000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0x00000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0x0000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0x0000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0x0000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x00000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0x00000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0x00000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0x00000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0x000015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x000015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0x000015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0x000015e4 | The Windows Management Instrumentation service encountered the error %1 and was not able to restore from the following backup repository: %2.\r\n
0x000015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0x000015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0x000015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0x000015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0x000015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0x000015ef | Windows Management Instrumentation Service started sucessfully\r\n
0x000015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0x000015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0x000015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n
0x10000038 | Classic\r\n
0x400015e0 | The Windows Management Instrumentation (WMI) service detected an inconsistency with the WMI repository in the following directory: %windir%\system32\wbem\repository. The WMI service was not able to recover the repository.  The WMI repository will now be deleted and a new repository will be created based on the auto-recovery mechanism.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x8000003f | A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.\r\n
0x90000001 | Microsoft-Windows-WMI\r\n
0x90000002 | Application\r\n
0x91000001 | Microsoft-Windows-WMI-Activity\r\n
0xb1000001 | GroupOperationId = %1; OperationId = %2; Operation = %3; ClientMachine = %4; User = %5; ClientProcessId = %6; NamespaceName = %7\r\n
0xb1000002 | ProviderInfo for GroupOperationId = %1; Operation = %2; ProviderName = %3; ProviderGuid = %4; Path = %5\r\n
0xb1000003 | Stop OperationId = %1\r\n
0xb100000b | CorrelationId = %1; GroupOperationId = %2; OperationId = %3; Operation = %4; ClientMachine = %5; User = %7; ClientProcessId = %8; NamespaceName = %9\r\n
0xb100000c | ProviderInfo for GroupOperationId = %1; Operation = %2; HostID = %3; ProviderName = %4; ProviderGuid = %5; Path = %6\r\n
0xb100000d | Stop OperationId = %1; ResultCode = %2\r\n
0xb100000e | OperationId = %1; Operation = %2; Channel = %3; Message = %4\r\n
0xb100000f | OperationId = %1; Operation = %2; ErrorID = %3; ErrorCategory = %4; Message = %5; TargetName = %6\r\n
0xb1000010 | OperationId = %1; Operation = %2; ErrorID = %3; Message = %4\r\n
0xb1000011 | CorrelationId = %1; ProcessId = %2; Protocol = %3; Operation = %4; User = %5; Namespace = %6\r\n
0xb1000012 | WMI Events were dropped. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000013 | Performing delete operation on the WMI repository. OperationID = %1; Operation = %2\r\n
0xb1000014 | Performing Update operation on the WMI repository. OperationID = %1; Operation = %2; Flags = %3\r\n
0xb1000015 | WMI Events were bound. ConsumerType = %1; Possiblecause = %2\r\n
0xb1000016 | CorrelationId = %1; GroupOperationId = %2; OperationId = %3; ClassName= %4; MethodName = %5; ImplementationClass = %6; ClientMachine = %7; User = %9; ClientProcessId = %10; NamespaceName = %12\r\n
0xb1000017 | CorrelationId = %1; GroupOperationId = %2; OperationId = %3; Commandline= %4; CreatedProcessId = %5; ClientMachine = %6; User = %8; ClientProcessId = %9\r\n
0xb1000032 | Activity Transfer\r\n
0xb1000064 | ComponentName = %1; MessageDetail = %2; FileName = %3\r\n
0xb1000065 | ComponentName = %1; ErrorId = %2; ErrorDetail = %3; FileName = %4\r\n
0xb10016e1 | %1 provider started with result code %2. HostProcess = %3; ProcessID = %4; ProviderPath = %5\r\n
0xb10016e2 | Id = %1; ClientMachine = %2; User = %3; ClientProcessId = %4; Component = %5; Operation = %6; ResultCode = %7; PossibleCause = %8\r\n
0xb10016e3 | Namespace = %1; NotificationQuery = %2; OwnerName = %3; HostProcessID = %4;  Provider= %5, queryID = %6; PossibleCause = %7\r\n
0xb10016e4 | Namespace = %1; NotificationQuery = %2; UserName = %3; ClientProcessID = %4, ClientMachine = %5; PossibleCause = %6\r\n
0xb10016e5 | Namespace = %1; Eventfilter = %2 (refer to its activate eventid:5859); Consumer = %3; PossibleCause = %4\r\n
0xc0000004 | Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.\r\n
0xc000000a | Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.\r\n
0xc0000015 | Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.\r\n
0xc0000016 | Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.\r\n
0xc0000017 | Event provider %1 attempted to register query "%2" in %3 namespace which is too broad.  Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.\r\n
0xc0000018 | Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.\r\n
0xc0000019 | Event provider %1 attempted to register query "%2" whose target class "%3" is not an event class. The query will be ignored. Contact the application vendor.\r\n
0xc000001c | Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000001d | Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.\r\n
0xc000002b | Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2\r\n
0xc0000030 | Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3\r\n
0xc000003a | Windows Management Instrumentation ADAP was unable to create the Win32_Perf base class in %1:Result=%2\r\n
0xc000003b | Windows Management Instrumentation ADAP was unable to create the Win32_PerfRawData base class %1\r\n
0xc0000041 | Windows Management Instrumentation (WMI) Service is starting to restore the WMI repository\r\n
0xc0000042 | The Windows Management Instrumentation Service has recovered from the following backup repository: %1.\r\n
0xc0000043 | The Windows Management Instrumentation (WMI) Service is starting the backup operation for the WMI repository and is copying data to the following file: %1\r\n
0xc0000044 | The Windows Management Instrumentation repository backup operation completed copying data to %1 with error %2.\r\n
0xc00015e1 | The Windows Management Instrumentation Service failed to load the repository files under the directory %windir%\system32\wbem\repository.  This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues like lack of memory.  If this error happens every time the machine is rebooted then the administrator on this machine may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation\r\n
0xc00015e2 | The Windows Management Instrumentation service detected an inconsistency in the following backup file: %1.\r\n
0xc00015e4 | The Windows Management Instrumentation service encountered the error %2 and was not able to restore from the following backup repository: %1.\r\n
0xc00015e5 | The %1 namespace is marked with the RequiresEncryption flag. Access to this namespace might be denied if the script or application does not have the appropriate authentication level. Change the authentication level to Pkt_Privacy and run the script or application again.\r\n
0xc00015e6 | Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace.  The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer.  Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.\r\n
0xc00015eb | The Windows Management Instrumentation service has detected an inconsistent system shutdown.\r\n
0xc00015ec | Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1  Value: %2 Maximum value: %3 WMIPRVSE PID: %4 Providers hosted in this process: %5\r\n
0xc00015ee | During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.\r\n
0xc00015ef | Windows Management Instrumentation Service started sucessfully\r\n
0xc00015f0 | The Windows Management Instrumentation (WMI) repository was successfully re-created by the auto-recovery mechanism.\r\n
0xc00015f1 | Windows Management Instrumentation Service subsystems initialized successfully\r\n
0xc00015ff | WMI interop namespace class "%1" has been overwritten. Some of the Interop scenarios might not work properly. Please issue following commands from elevated command prompt to restore the behavior."mofcomp %windir%\system32\wbem\interop.mof" and similarly mofcomp all the interop.mfl under %windir%\system32\wbem and its subdirectories.\r\n
