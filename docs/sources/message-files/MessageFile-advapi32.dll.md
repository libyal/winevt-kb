## advapi32.dll

Path: %SystemRoot%\system32\advapi32.dll

### 5.0.2195.6710, 5.1.2600.5512

Message identifier | Message string
--- | ---
0x400003e8 | An exception occurred while performing Windows 3.1 migration.  Some data\r\nmay not have been migrated.\r\n
0x400003e9 | The entire contents of %1 was migrated into the Windows NT registry.\r\n
0x400003ea | The entire contents of the %1 section of %2 was migrated into the\r\nWindows NT registry.\r\n
0x400003eb | The value of the %1 variable in the %2 section of %3 was migrated into\r\nthe Windows NT registry.\r\n
0x400003ec | The entire contents of the %1 Program Manager group was migrated into the\r\nWindows NT registry.\r\n
0x400003ed | The contents of the Windows 3.X Program Manager group file %1 was not\r\nmigrated into the Windows NT registry, as a group of that name, %2,\r\nalready existed.\r\n
0x400003f5 | Contents of %1 migrated to the Windows NT registry.\r\n
0x800003ee | Unable to migrate all or part of the %1 file into the Windows NT registry.\r\n
0x800003ef | Unable to migrate all or part of the %1 section of %2 into the Windows\r\nNT registry.\r\n
0x800003f0 | Unable to migrate the value of the %1 variable in the %2 section of %3\r\ninto the Windows NT registry.\r\n
0x800003f1 | Unable to migrate the contents of the %1 Program Manager group into\r\nthe Windows NT registry.\r\n
0x800003f2 | Unable to load the contents of the Windows 3.1 Program Manager group file %1.\r\nError Code was %2.  Group not migrated to the Windows NT registry.\r\n
0x800003f3 | Unable to read the value of %1 from the %2 file.  Group not migrated to\r\nthe Windows NT registry.\r\n
0x800003f4 | Unable to convert the contents of the Windows 3.1 Program Manager group\r\nfile %1.  into the Windows NT format.  Error Code was %2.  Group not\r\nmigrated to the Windows NT registry.\r\n
0x800003f6 | Unable to migrate all or part of %1 to the Windows NT registry.\r\n
0x800003f7 | Did not migrate the contents of the %1 Program Manager group into\r\nthe Windows NT registry.  It is incompatible with Windows NT.\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x00000100 | The Transaction (UOW=%1, Description='%3') was unable to be committed, and instead rolled back; this was due to an error message returned by CLFS while attempting to write a Prepare or Commit record for the Transaction.  The CLFS error returned was: %4.\r\n
0x00000101 | The Transaction (UOW=%1, Description='%3') blocked a Freeze from completing.  Freeze is necessary to ensure that a VSS snapshot is transactionally consistent.  The ResourceManager (RmId=%4, Description='%6') may not be functioning correctly, since it did not allow the transaction to drain in the allotted time.  Contact the vendor for that ResourceManager for assistance.\r\n
0x00000102 | The transaction (UOW=%1, Description='%3') was heuristically aborted and forgotten from the TransactionManager (TmId=%4, LogPath=%6) so that the TransactionManager can continue to make forward progress.  This may cause data corruption in any subordinate ResourceManagers or Transactionmanager.\r\n
0x10000021 | Verbose context events\r\n
0x10000022 | Scenario trigger events\r\n
0x11000005 | Time\r\n
0x18000005 | Deprecated dlls\r\n
0x1c000005 | Deprecated COM interfaces\r\n
0x300a0000 | Scenario start enables context providers to the WDI context logger.\r\n
0x300b0000 | Scenario end disables context providers to the WDI context logger.\r\n
0x300c0000 | When a scenario has remained in-flight beyond the maximum time window it is automatically terminated by the SEM.\r\n
0x300d0000 | A scenario start attempt failed in the SEM.\r\n
0x300e0000 | A scenario end attempt failed in the SEM.\r\n
0x300f0000 | The SEM received a request to start a new scenario, but the maximum number of scenarios were already in-flight.\r\n
0x30100000 | There is an invalid configuration parameter in the SEM registry namespace.\r\n
0x30110000 | The SEM is configured with more scenarios than the maximum allowed count.\r\n
0x30120000 | The SEM is configured with a scenario with too many context providers.\r\n
0x30130000 | The SEM is configured with a scenario that has too many end events.\r\n
0x30140000 | The number of providers specified across all scenarios is above the maximum allowed amount.\r\n
0x371e0000 | NLS data table operations\r\n
0x371f0000 | NLS initialization\r\n
0x37200000 | NLS configuration changes\r\n
0x37210000 | NLS operations\r\n
0x37220000 | NLS clean-up operations\r\n
0x3f1e0000 | MUI notify initialization\r\n
0x3f1f0000 | MUI notify operation\r\n
0x70000009 | SEM Scenario Lifecycle\r\n
0x7000000a | SEM Initialization\r\n
0x7700001e | NLS code page functions\r\n
0x77000020 | NLS date/time functions\r\n
0x77000021 | NLS Unattended Regional and Language Options\r\n
0x77000022 | NLS group policy\r\n
0x77000023 | NLS locale functions\r\n
0x7f00001e | MUI NotifyUILanguageChange task\r\n
0x90000001 | Microsoft-Windows-Kernel-WDI\r\n
0x91000001 | Microsoft-Windows-Kernel-General\r\n
0x92000001 | Microsoft-Windows-Kernel-Process\r\n
0x93000001 | Microsoft-Windows-Kernel-Registry\r\n
0x94000001 | Microsoft-Windows-Kernel-Power\r\n
0x96000001 | Microsoft-Windows-Kernel-Acpi\r\n
0x97000001 | Microsoft-Windows-International\r\n
0x98000001 | Microsoft-Windows-User-Loader\r\n
0x99000001 | Microsoft-Windows-Kernel-BootDiagnostics\r\n
0x9b000001 | Microsoft-Windows-UAC\r\n
0x9d000001 | Microsoft-Windows-HAL\r\n
0x9e000001 | Microsoft-Windows-SoftwareRestrictionPolicies\r\n
0x9f000001 | Microsoft-Windows-MUI\r\n
0xb0000020 | The Scenario Event Mapper started a scenario for provider %1 (event ID %2) with %4 context providers.  The context logger dropped event count was %3.\r\n
0xb0000021 | The Scenario Event Mapper stopped a scenario for provider %1 (event ID %2) with %4 context providers.  The context logger dropped event count was %3.\r\n
0xb0000022 | An in-flight scenario from provider %1 (event ID %2) timed out and was stopped automatically by the Scenario Event Mapper.\r\n
0xb0000023 | The Scenario Event Mapper was unable to start a new scenario for provider %1 (event ID %2) because the maximum number of scenarios are already in flight.\r\n
0xb0000024 | The Scenario Event Mapper was unable to start a scenario for provider %1 (event ID %2).  The error code was %3.\r\n
0xb0000025 | The Scenario Event Mapper was unable to stop a scenario for provider %1 (event ID %2).  The error code was %3.\r\n
0xb0000026 | The Scenario Event Mapper is configured with more than the maximum number of scenarios.  The scenario for provider %1 (event ID %2) will be ignored.\r\n
0xb0000027 | The Scenario Event Mapper is configured with more than the maximum number of context providers for the scenario with provider %1 (event ID %2).  The scenario will be ignored.\r\n
0xb0000028 | The Scenario Event Mapper is configured with more than the maximum number of end events for the scenario with provider %1 (event ID %2).  The scenario will be ignored.\r\n
0xb0000029 | The Scenario Event Mapper is configured with more than the maximum number of providers.  The provider %1 will be ignored.\r\n
0xb000002a | The Scenario Event Mapper is configured with an unsupported scenario. The scenario for provider %1 (event ID %2) encountered error code %3 and will be ignored.\r\n
0xb1000001 | The system time has changed to %1 from %2.\r\n
0xb1000002 | License policy-cache corruption detected.\r\n
0xb1000003 | License policy-cache corruption has been fixed.\r\n
0xb1000004 | License policy-cache has been emptied because it was not updated within expected duration.\r\n
0xb1000005 | {Registry Hive Recovered} Registry hive (file): '%3' was corrupted and it has been recovered. Some data might have been lost.\r\n
0xb1000006 | An I/O operation initiated by the Registry failed unrecoverably.The Registry could not flush hive (file): '%3'.\r\n
0xb2000001 | Process %1 started at time %2 by parent %3 running in session %4 with name %5.\r\n
0xb2000002 | Process %1 (which started at time %2) stopped at time %3 with exit code %4.\r\n
0xb2000003 | Thread %2 (in Process %1) started.\r\n
0xb2000004 | Thread %2 (in Process %1) stopped.\r\n
0xb2000005 | Process %3 had an image loaded with name %7.\r\n
0xb2000006 | Process %3 had an image unloaded with name %7.\r\n
0xb4000009 | The application %4 stopped the power transition.\r\n
0xb400000a | The service %3 stopped the power transition.\r\n
0xb4000028 | The driver %2 for device %4 stopped the power transition.\r\n
0xb4000029 | The last sleep transition was unsuccessful. This error could be caused if the system stopped responding, failed, or lost power during the sleep transition.\r\n
0xb400002a | The system is entering sleep.\r\n
0xb400003b | The system is entering Away Mode.\r\n
0xb400003e | The application or service %3 has overridden user power management settings with a code of %1.\r\n
0xb400003f | The application or service %3 is attempting to update the system timer resolution to a value of %1.\r\n
0xb50000e1 | The application %3 with process id %1 stopped the removal or ejection for the device %5.\r\n
0xb6000001 | A memory range descriptor has been marked as reserved.\r\n
0xb70003e9 | The NLS operation failed because the registry key %1 cannot be opened. Error code is %2. Error message: %3\r\n
0xb70003ea | The NLS operation failed because the registry key %1 cannot be opened. Status code is %2.\r\n
0xb70003eb | NLS codepage operation failed for the codepage %1 because the file %2 is missing.  To correct this error, replace this file or repair your Windows installation.\r\n
0xb70003ec | NLS codepage operation failed for the codepage %1 because the file %2 is corrupted. To correct this error, replace this file or repair your Windows installation.\r\n
0xb70003ed | NLS operation failed for %1 locale because the file %2\globalization\%1.nlp is missing.  To fix this problem, reinstall this custom locale.\r\n
0xb70003ee | NLS operation failed for %1 locale because the file %2\globalization\%1.nlp is corrupted.  To fix this problem, reinstall this custom locale.\r\n
0xb70005dc | Group Policy has prevented process number %1 (%2) from changing the standards and format information for the user.\r\n
0xb70005dd | Group Policy has prevented the geographical location from being changed.\r\n
0xb70005de | Group Policy has prevented the user from changing their user locale to "%1".\r\n
0xb70005df | Group Policy does not allow custom user locales for standards and formats. The user was unable to select "%1" as their user locale.\r\n
0xb70007d0 | NLS operation recreated the registry key %1.\r\n
0xb70009c4 | Windows has detected inconsistencies in NLS internal data. To correct this problem, log off of Windows and log on again.\r\n
0xb7000bb8 | Process number %1 (%2) called SetLocaleInfo(%3, %4, "%5")  successfully.\r\n
0xb7000bb9 | Process number %1 (%2) called SetCalendarInfo(%3, %4, %5, "%6")  successfully.\r\n
0xb7000bba | Process number %1 (%2) called SetUserGeoID(%3) successfully.\r\n
0xb7000bbb | The system updated the locale "%1" with flag %2. Process number %3 (%4). Return code is %5.\r\n
0xb7002710 | The user tried to apply an unattended XML file (%1) in an unsupported format. Reason: %3 (Line %2). The system has not been changed.\r\n
0xb7002711 | Unsupported XML in function.\r\n
0xb7002713 | The user locale "%1" (specified by the UserLocale element) is not a supported locale name or is not installed on the system. The user locale was not changed.\r\n
0xb7002714 | Unsupported alternate sort "%1".\r\n
0xb7002715 | "%1" is not a supported sort order for locale "%2".\r\n
0xb7002716 | The selected system locale (specified by the SystemLocale element) is not installed on the system. The system locale was not changed.\r\n
0xb7002717 | Internal error while changing System locale (specified by the SystemLocale element).\r\n
0xb7002718 | Error while changing keyboard/input method for "%1".\r\n
0xb7002719 | Error while changing location preference (geoid): %1. This error may be caused by an unsupported location preference (geoid) or a Group Policy restriction. Error code is %2. Error message: %3\r\n
0xb700271a | Failed to change UI Language to "%1". Status code is: %2.\r\n
0xb700271b | Failed to change UI Language fallback order to "%1". Status code is: %2.\r\n
0xb700271c | The user tried to apply an unattended XML file %1, but the file does not exist.\r\n
0xb700271d | Error while the user changed setting "%1" with value "%2" for the current user locale. Error code is: %3. Error message: %4\r\n
0xb700271e | The selected calendar "%1;" (specified by the Calendar element) is not a supported calendar. The user locale was not changed.\r\n
0xb700271f | The selected TwoDigitYearMax "%1;" (specified by the TwoDigitYearMax element) is not a supported value. The user locale was not changed.\r\n
0xb700277f | The user does not have permission to change the TwoDigitYearMax setting\r\n
0xb7002780 | The user does not have permission to copy current settings to the Default and/or System Account\r\n
0xb7002781 | The user does not have permission to change the system locale (specified by the SystemLocale element).\r\n
0xb7002783 | The user does not have permission to change the calendar.\r\n
0xb70027e8 | Unexpected failure. Stack overflow\r\n
0xb70027ea | Unexpected failure. Unsupported flag\r\n
0xb70027eb | Unexpected failure. Unsupported parameter\r\n
0xb70027ec | Unexpected failure. Unrecoverable error.\r\n
0xb70027ed | Failed when calling internal function. Error code is: %1\r\n
0xb70027ee | The operation timed out.\r\n
0xb700283c | Group Policy has prevented the user from changing the system locale (specified by the SystemLocale element).\r\n
0xb70032c8 | The user changed their user locale (specified by the UserLocale element) to "%1".\r\n
0xb70032c9 | The user reset all customizations for their user locale "%1" (specified by the UserLocale element) to the system default.\r\n
0xb70032ca | The user changed their user locale setting "%1" (specified by the UserLocale element) to "%2".\r\n
0xb70032cb | The locale has to be changed to the current locale in order to make customizations.\r\n
0xb70032cc | The user changed their alternate sort to "%1".\r\n
0xb70032cd | The user changed their calendar to "%1".\r\n
0xb70032ce | The user changed their TwoDigitYearMax to %1.\r\n
0xb70032cf | The user changed their location preference (geoid) to %1.\r\n
0xb70032d0 | The system locale (specified by the SystemLocale element) was changed to "%1".\r\n
0xb70032d1 | The current user settings were copied to the default user account.\r\n
0xb70032d2 | The current user settings were copied to the system accounts.\r\n
0xb70032d3 | The user has changed their UI Language to "%1".\r\n
0xb70032d4 | The user has changed their UI Language fallback order to "%1".\r\n
0xb8000001 | Deprecated module %1.\r\n
0xbb000001 | The process failed to handle ERROR_ELEVATION_REQUIRED during the creation of a child process.\r\n
0xbc000001 | Deprecated COM CLSID %1.\r\n
0xbd000001 | Initialization of the High Precision Event Timer failed due to a BIOS configuration problem.%nThe operating system will use another available platform timer in lieu of the High Precision Event Timer.%n%nContact your system vendor for technical assistance.%nInitialization status: %1.\r\n
0xbd000002 | Initialization of the High Precision Event Timer failed due to unsupported hardware.%nThe operating system will use another available platform timer in lieu of the High Precision Event Timer.%n%nInitialization status: %1.\r\n
0xbd000003 | Initialization of the High Precision Event Timer failed due to an interrupt configuration problem.%nThe operating system will use another available platform timer in lieu of the High Precision Event Timer.%n%nIt may be possible to address this problem with an updated system BIOS.%nContact your system vendor for technical assistance.%nInitialization status: %1.\r\n
0xbe000032 | Access to %1 is monitored by policy rule %2.\r\n
0xbe000361 | Access to %1 has been restricted by your Administrator by the default software restriction policy level.\r\n
0xbe000362 | Access to %1 has been restricted by your Administrator by location with policy rule %2 placed on path %3.\r\n
0xbe000363 | Access to %1 has been restricted by your Administrator by software publisher policy.\r\n
0xbe000364 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0xbe000372 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0xbf0007d0 | MUI notify operation failed with status code %1. No callbacks were invoked.\r\n
0xbf0007d1 | MUI Callback failed for file %1 because it can not be loaded. To correct this error, replace this file or repair your Windows installation.\r\n
0xbf0007d2 | MUI Callback failed for file %1 registered as type %2 because the function %3 does not exist in the dll. To correct this error, replace the file or fix the registry entry.\r\n
0xbf0007d3 | MUI Callback failed for file %1 because it is not signed. To correct this error, replace with a signed file.\r\n
0xbf0007d4 | MUI Callback file %1 cannot be found. To correct this error, repair the registry or copy the file to the specified location.\r\n
0xbf000bb8 | MUI notification for UI Language change has been invoked with flags set to %1 and the new languages set to %2 and the previous languages set to %3. The extended flags is set to %4\r\n
0xbf000bba | MUI notification callback API %2 in %1 returned with code %3.\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x0000012d | Microsoft-Windows-AIT\r\n
0x0000012e | Microsoft-Windows-AeCache\r\n
0x0000012f | Microsoft-Windows-AeSwitchBack\r\n
0x00000130 | Microsoft-Windows-AeLookupServiceTrigger\r\n
0x000001f4 | Microsoft-Windows-Kernel-Network\r\n
0x000001f5 | Data sent.\r\n
0x000001f6 | Data received.\r\n
0x000001f7 | Connection attempted.\r\n
0x000001f8 | Disconnect issued.\r\n
0x000001f9 | Data retransmitted.\r\n
0x000001fa | Connection accepted.\r\n
0x000001fb | Reconnect attempted.\r\n
0x000001fc | TCP connection attempt failed.\r\n
0x000001fd | Protocol copied data on behalf of user.\r\n
0x000001fe | Data sent over UDP protocol.\r\n
0x000001ff | Data received over UDP protocol.\r\n
0x00000200 | UDP connection attempt failed.\r\n
0x00000201 | TCPv4: %2 bytes transmitted from %4:%6 to %3:%5.\r\n
0x00000202 | TCPv4: %2 bytes received from %4:%6 to %3:%5.\r\n
0x00000203 | TCPv4: Connection attempted between %4:%6 and %3:%5.\r\n
0x00000204 | TCPv4: Connection closed between %4:%6 and %3:%5.\r\n
0x00000205 | TCPv4: %2 bytes retransmitted from %4:%6 to %3:%5.\r\n
0x00000206 | TCPv4: Connection established between %4:%6 and %3:%5.\r\n
0x00000207 | TCPv4: Reconnect attempt between %4:%6 and %3:%5.\r\n
0x00000208 | TCPv4: Connection attempt failed with error code %2.\r\n
0x00000209 | TCPv4: %2 bytes copied in protocol on behalf of user for connection between %4:%6 and %3:%5.\r\n
0x0000020a | UDPv4: %2 bytes transmitted from %4:%6 to %3:%5.\r\n
0x0000020b | UDPv4: %2 bytes received from %4:%6 to %3:%5.\r\n
0x0000020c | UDPv4: Connection attempt failed with error code %2.\r\n
0x0000020d | TCPv6: %2 bytes transmitted from %4:%6 to %3:%5.\r\n
0x0000020e | TCPv6: %2 bytes received from %4:%6 to %3:%5.\r\n
0x0000020f | TCPv6: Connection attempted between %4:%6 and %3:%5.\r\n
0x00000210 | TCPv6: Connection closed between %4:%6 and %3:%5.\r\n
0x00000211 | TCPv6: %2 bytes retransmitted from %4:%6 to %3:%5.\r\n
0x00000212 | TCPv6: Connection established between %4:%6 and %3:%5.\r\n
0x00000213 | TCPv6: Reconnect attempt between %4:%6 and %3:%5.\r\n
0x00000214 | TCPv6: %2 bytes copied in protocol on behalf of user for connection between %4:%6 and %3:%5.\r\n
0x00000215 | UDPv6: %2 bytes transmitted from %4:%6 to %3:%5.\r\n
0x00000216 | UDPv6: %2 bytes received from %4:%6 to %3:%5.\r\n
0x00000258 | Microsoft-Windows-Kernel-Disk\r\n
0x00000259 | %3 bytes read from disk %1 at %5.\r\n
0x0000025a | %3 bytes written to disk %1 at %5.\r\n
0x0000025b | Buffers flushed to disk %1.\r\n
0x000002bc | Microsoft-Windows-Kernel-Boot\r\n
0x000002bd | System was booted in %1x%2@%3bpp.\r\n
0x000002be | BootUX screen was displayed in %1x%2@%3bpp.\r\n
0x000002bf | Video bit transfer rate is %1 bytes per ms.\r\n
0x000002c0 | Boot library accessed file %2 on Device %1. Read %3 bytes and wrote %4 bytes.\r\n
0x000002c1 | File IO for boot application %1: Total Bytes Read = %2, Total Bytes Written = %3.\r\n
0x000002c2 | Image %1 failed IntegrityCheck reason is %3. Image flags are %2. Error ignored due to debugger %4.\r\n
0x000002c3 | Bootmgr duration is %1 milliseconds.\r\n
0x000002c4 | Image %1 is not self-signed.\r\n
0x000002c5 | A device (%1) that was enumerated by the BIOS was inaccessible to the boot environment.\r\n
0x00000320 | Microsoft-Windows-Kernel-File\r\n
0x00000321 | File name %2 was associated with key %1.\r\n
0x00000322 | File name %2 was disassociated with key %1.\r\n
0x00000323 | File Create was requested (%1) for file object %3 with name %7.\r\n
0x00000324 | File Cleanup was requested (%1) for file object %3 with key %4.\r\n
0x00000325 | File Close was requested (%1) for file object %3 with key %4.\r\n
0x00000326 | File Read was requested (%2) for file object %4 with key %5 at offset %1 for %6 bytes.\r\n
0x00000327 | File Write was requested (%2) for file object %4 with key %5 at offset %1 for %6 bytes.\r\n
0x00000328 | File Set Information was requested (%1) for file object %3 with key %4 for type %6 with %5 as extra information.\r\n
0x00000329 | File Delete status update was requested (%1) for file object %3 with key %4: delete status %5.\r\n
0x0000032a | File Rename was requested (%1) for file object %3 with key %4.\r\n
0x0000032b | File Directory Enumeration was requested (%1) for file object %3 with key %4 for pattern %8.\r\n
0x0000032c | File Flush was requested (%1) for file object %3 with key %4.\r\n
0x0000032d | File Query Information was requested (%1) for file object %3 with key %4 for type %6.\r\n
0x0000032e | File FSCTL was requested (%1) for file object %3 with key %4 for type %6 with %5 as extra information.\r\n
0x0000032f | File operation request %1 completed with status %3 and extra information %2.\r\n
0x00000330 | File Directory Change Notification was requested (%1) for file object %3 with key %4.\r\n
0x00000331 | File Delete was requested (%1) for file object %3 with path %7.\r\n
0x00000332 | File Rename was requested (%1) for file object %3 with new path %7.\r\n
0x00000333 | File Link was requested (%1) for file object %3 to path %7.\r\n
0x00000334 | File SetLink was requested (%1) for file object %3 with key %4.\r\n
0x00000335 | New File Creation was requested (%1) for file object %3 with name %7.\r\n
0x00000385 | Microsoft-Windows-Kernel-EventTracing\r\n
0x00000386 | Session "%1" failed to write to log file "%2" with the following error: %3\r\n
0x00000387 | The backing-file for the real-time session "%1" has reached its maximum size. As a result, new events will not be logged to this session until space becomes available. This error is often caused by starting a trace session in real-time mode without having any real-time consumers.\r\n
0x00000388 | Session "%1" failed to start with the following error: %3\r\n
0x00000389 | Session "%1" stopped due to the following error: %3\r\n
0x0000038a | The maximum file size for session "%1" has been reached. As a result, events might be lost (not logged) to file "%2". The maximum files size is currently set to %5 bytes.\r\n
0x0000038b | An error was encountered while tracing session "%2" was switching to the "%1" event log file. Error: %3\r\n
0x0000038e | Provider %1 was registered with Event Tracing for Windows.\r\n
0x0000038f | Provider %1 was unregistered from Event Tracing for Windows.\r\n
0x00000390 | Session "%3" was started.\r\n
0x00000391 | Session "%3" was stopped.\r\n
0x00000392 | The configuration of session "%3" has been modified.\r\n
0x00000393 | The events from session "%3" have been flushed.\r\n
0x00000394 | Provider %1 has been enabled to session "%2".\r\n
0x00000395 | Provider %1 is no longer enabled to session "%2".\r\n
0x00000396 | The security settings of provider %1 have been modified from %2 to %3.\r\n
0x00000397 | The security descriptor for session "%3" has been updated.\r\n
0x00000398 | Provider\r\n
0x00000399 | Session\r\n
0x0000039b | Logging\r\n
0x0000039d | Stop\r\n
0x0000039e | Start\r\n
0x0000039f | Disable\r\n
0x000003a0 | Enable\r\n
0x000003a1 | Unregister\r\n
0x000003a2 | Register\r\n
0x000003a3 | Flush\r\n
0x000003a4 | Configure\r\n
0x000003a7 | Write Buffer\r\n
0x000003a8 | File Switch\r\n
0x000003aa | Provider\r\n
0x000003ab | Session\r\n
0x000003ac | Stack correlation event. This event contains a call stack which is associated with a prior event which is correlated by the MatchId.\r\n
0x000003ad | Stack Trace\r\n
0x000003ae | User Mode Stack Trace\r\n
0x000003af | Microsoft-Windows-Kernel-EventTracing/Analytic\r\n
0x000003b0 | Microsoft-Windows-Kernel-EventTracing/Admin\r\n
0x000003c0 | Microsoft-Windows-Kernel-StoreMgr\r\n
0x000003c1 | Microsoft-Windows-Kernel-StoreMgr/Operational\r\n
0x000003c2 | %5%n%nVirtual Address: %2%nPhysical Address: %3%nCorruption Window Size: %4\r\n
0x000003c3 | A memory corruption was detected and handled. Memory diagnostics should be run on this machine and, if necessary, memory chips should be replaced.\r\n
0x000003c4 | A data corruption was detected and handled in a ReadyBoost cache. This corruption was most likely caused by faulty hardware. While ReadyBoost will always detect and handle these errors, seeing a lot of these may mean that the ReadyBoost device has worn out which reduces its performance. You should consider replacing the ReadyBoost cache device.\r\n
0x000003c5 | A ReadyBoost cache failed to persist across boot. This may happen if the cache device was modified on another computer or if this computer was booted into another operating system.\r\n
0x000003c6 | %1%n%nDevice name: %4%nCache path: %6\r\n
0x000003c7 | A ReadyBoost cache was deleted due to repeated data corruption instances on the associated device that have been detected and handled. While ReadyBoost will always detect and handle these errors, repeated corruption instances may mean that the ReadyBoost device has worn out which reduces its performance. You should consider replacing the ReadyBoost device.\r\n
0x000003c8 | A ReadyBoost cache was deleted due to repeated I/O failures on the associated device. This typically happens when the device (e.g. an SD card) is removed, but it may also indicate faulty hardware.\r\n
0x01000001 | The system time has changed to %1 from %2.\r\n
0x01000002 | License policy-cache corruption detected.\r\n
0x01000003 | License policy-cache corruption has been fixed.\r\n
0x01000004 | License policy-cache has expired because it was not updated within expected duration.\r\n
0x01000005 | {Registry Hive Recovered} Registry hive (file): '%3' was corrupted and it has been recovered. Some data might have been lost.\r\n
0x01000006 | An I/O operation initiated by the Registry failed unrecoverably.The Registry could not flush hive (file): '%3'.\r\n
0x0100000b | TxR init phase for hive %2 (TM: %3, RM: %4) finished with result=%5 (Internal code=%6).\r\n
0x0100000c | The operating system started at system time %7.\r\n
0x0100000d | The operating system is shutting down at system time %1.\r\n
0x040000db | The driver %5 failed to load for the device %2.\r\n
0x040000e1 | The application %3 with process id %1 stopped the removal or ejection for the device %5.\r\n
0x040000f0 | A partition unit replace operation has been initiated.\r\n
0x040000f1 | A partition unit replace operation has failed.%n%nCause: %5\r\n
0x040000f2 | A partition unit has been successfully replaced.\r\n
0x0b000032 | Access to %1 is monitored by policy rule %2.\r\n
0x0b000361 | Access to %1 has been restricted by your Administrator by the default software restriction policy level.\r\n
0x0b000362 | Access to %1 has been restricted by your Administrator by location with policy rule %2 placed on path %3.\r\n
0x0b000363 | Access to %1 has been restricted by your Administrator by software publisher policy.\r\n
0x0b000364 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0x0b000372 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0x0d00000a | The system firmware has allocated a memory region previously determined to be unreliable. This has the potential to cause system instability and/or data corruption.\r\n
0x10000021 | Verbose context events\r\n
0x10000022 | Scenario trigger events\r\n
0x10000034 | SQM\r\n
0x11000005 | Time\r\n
0x17000005 | Deprecated dlls\r\n
0x17000006 | Fatal user callback exception\r\n
0x18000031 | Response Time\r\n
0x1a000005 | Deprecated COM interfaces\r\n
0x3000000a | Scenario start enables context providers to the WDI context logger.\r\n
0x3000000b | Scenario end disables context providers to the WDI context logger.\r\n
0x3000000c | When a scenario has remained in-flight beyond the maximum time window it is automatically terminated by the SEM.\r\n
0x3000000d | A scenario start attempt failed in the SEM.\r\n
0x3000000e | A scenario end attempt failed in the SEM.\r\n
0x3000000f | The SEM received a request to start a new scenario, but the maximum number of scenarios were already in-flight.\r\n
0x30000010 | There is an invalid configuration parameter in the SEM registry namespace.\r\n
0x30000011 | The SEM is configured with more scenarios than the maximum allowed count.\r\n
0x30000012 | The SEM is configured with a scenario with too many context providers.\r\n
0x30000013 | The SEM is configured with a scenario that has too many end events.\r\n
0x30000014 | The number of providers specified across all scenarios is above the maximum allowed amount.\r\n
0x31000000 | Info\r\n
0x32000001 | Start\r\n
0x32000002 | Stop\r\n
0x34000008 | Suspend\r\n
0x3600001e | NLS data table operations\r\n
0x3600001f | NLS initialization\r\n
0x36000020 | NLS configuration changes\r\n
0x36000021 | NLS operations\r\n
0x36000022 | NLS clean-up operations\r\n
0x3c00001e | Start\r\n
0x3c00001f | Invoke callback function\r\n
0x3c000020 | Disable live cache\r\n
0x3c000021 | Update resource cache manifest\r\n
0x3c000022 | Build resource cache\r\n
0x3c000023 | Start\r\n
0x3c000024 | End\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x56000001 | Critical\r\n
0x56000005 | Verbose\r\n
0x70000009 | SEM Scenario Lifecycle\r\n
0x7000000a | SEM Initialization\r\n
0x7600001e | NLS code page functions\r\n
0x76000020 | NLS date/time functions\r\n
0x76000021 | NLS Unattended Regional and Language Options\r\n
0x76000022 | NLS group policy\r\n
0x76000023 | NLS locale functions\r\n
0x7c00001e | MUI NotifyUILanguageChange task\r\n
0x7c00001f | MUI resource cache builder\r\n
0x90000001 | Microsoft-Windows-Kernel-WDI\r\n
0x90000002 | Microsoft-Windows-Kernel-WDI/Analytic\r\n
0x90000003 | Microsoft-Windows-Kernel-WDI/Debug\r\n
0x90000004 | Microsoft-Windows-Kernel-WDI/Operational\r\n
0x91000001 | Microsoft-Windows-Kernel-General\r\n
0x91000002 | System\r\n
0x92000001 | Microsoft-Windows-Kernel-Process\r\n
0x93000001 | Microsoft-Windows-Kernel-Registry\r\n
0x94000001 | Microsoft-Windows-Kernel-PnP\r\n
0x95000001 | Microsoft-Windows-Kernel-Acpi\r\n
0x96000001 | Microsoft-Windows-International\r\n
0x96000002 | Microsoft-Windows-International/Operational\r\n
0x97000001 | Microsoft-Windows-User-Loader\r\n
0x98000001 | Microsoft-Windows-Kernel-BootDiagnostics\r\n
0x99000001 | Microsoft-Windows-UAC\r\n
0x99000002 | Microsoft-Windows-UAC/Operational\r\n
0x9a000001 | Microsoft-Windows-COM\r\n
0x9b000001 | Microsoft-Windows-SoftwareRestrictionPolicies\r\n
0x9b000002 | Application\r\n
0x9c000001 | Microsoft-Windows-MUI\r\n
0x9c000002 | Microsoft-Windows-MUI/Operational\r\n
0x9c000003 | Microsoft-Windows-MUI/Admin\r\n
0x9c000004 | Microsoft-Windows-MUI/Analytic\r\n
0x9c000005 | Microsoft-Windows-MUI/Debug\r\n
0x9e000001 | Microsoft-Windows-PCI\r\n
0xb0000020 | The Scenario Event Mapper started a scenario for provider %1 (event ID %2) with %4 context providers.  The context logger dropped event count was %3.\r\n
0xb0000021 | The Scenario Event Mapper stopped a scenario for provider %1 (event ID %2) with %4 context providers.  The context logger dropped event count was %3.\r\n
0xb0000022 | An in-flight scenario from provider %1 (event ID %2) timed out and was stopped automatically by the Scenario Event Mapper.\r\n
0xb0000023 | The Scenario Event Mapper was unable to start a new scenario for provider %1 (event ID %2) because the maximum number of scenarios are already in flight.\r\n
0xb0000024 | The Scenario Event Mapper was unable to start a scenario for provider %1 (event ID %2).  The error code was %3.\r\n
0xb0000025 | The Scenario Event Mapper was unable to stop a scenario for provider %1 (event ID %2).  The error code was %3.\r\n
0xb0000026 | The Scenario Event Mapper is configured with more than the maximum number of scenarios.  The scenario for provider %1 (event ID %2) will be ignored.\r\n
0xb0000027 | The Scenario Event Mapper is configured with more than the maximum number of context providers for the scenario with provider %1 (event ID %2).  The scenario will be ignored.\r\n
0xb0000028 | The Scenario Event Mapper is configured with more than the maximum number of end events for the scenario with provider %1 (event ID %2).  The scenario will be ignored.\r\n
0xb0000029 | The Scenario Event Mapper is configured with more than the maximum number of providers.  The provider %1 will be ignored.\r\n
0xb000002a | The Scenario Event Mapper is configured with an unsupported scenario. The scenario for provider %1 (event ID %2) encountered error code %3 and will be ignored.\r\n
0xb2000001 | Process %1 started at time %2 by parent %3 running in session %4 with name %5.\r\n
0xb2000002 | Process %1 (which started at time %2) stopped at time %3 with exit code %4.\r\n
0xb2000003 | Thread %2 (in Process %1) started.\r\n
0xb2000004 | Thread %2 (in Process %1) stopped.\r\n
0xb2000005 | Process %3 had an image loaded with name %7.\r\n
0xb2000006 | Process %3 had an image unloaded with name %7.\r\n
0xb2000007 | Base CPU priority of thread %2 in process %1 was changed from %3 to %4.\r\n
0xb2000008 | CPU priority of thread %2 in process %1 was changed from %3 to %4.\r\n
0xb2000009 | Page priority of thread %2 in process %1 was changed from %3 to %4.\r\n
0xb200000a | I/O priority of thread %2 in process %1 was changed from %3 to %4.\r\n
0xb40000f1 | A partition unit replace operation has failed.\r\n
0xb5000001 | A memory range descriptor has been marked as reserved.\r\n
0xb5000002 | Unexpected GPE event was fired on GPE bits that should be disabled.\r\n
0xb5000003 | A temperature change notification (Notify(thermal_zone, 0x80)) for ACPI thermal zone %2 has been received.\n            %n_TMP = %3K\n            %n_PSV = %4K\n            %n_AC0 = %5K\n            %n_AC1 = %6K\n            %n_AC2 = %7K\n            %n_AC3 = %8K\n            %n_AC4 = %9K\n            %n_AC5 = %10K\n            %n_AC6 = %11K\n            %n_AC7 = %12K\n            %n_AC8 = %13K\n            %n_AC9 = %14K\n            %n_HOT = %15K\n            %n_CRT = %16K\r\n
0xb5000004 | A trip point change notification (Notify(thermal_zone, 0x81)) for ACPI thermal zone %2 has been received.\n            %n_TMP = %3K\n            %n_PSV = %4K\n            %n_AC0 = %5K\n            %n_AC1 = %6K\n            %n_AC2 = %7K\n            %n_AC3 = %8K\n            %n_AC4 = %9K\n            %n_AC5 = %10K\n            %n_AC6 = %11K\n            %n_AC7 = %12K\n            %n_AC8 = %13K\n            %n_AC9 = %14K\n            %n_HOT = %15K\n            %n_CRT = %16K\r\n
0xb5000005 | The active cooling device %6 has been turned %8.\n            %nThermal zone device instance: %2\n            %nActive cooling package: _AC%3\n            %nNamespace object: _AL%4\r\n
0xb60003e9 | The NLS operation failed because the registry key %1 cannot be opened. Error code is %2. Error message: %3\r\n
0xb60003ea | The NLS operation failed because the registry key %1 cannot be opened. Status code is %2.\r\n
0xb60003eb | NLS codepage operation failed for the codepage %1 because the file %2 is missing.  To correct this error, replace this file or repair your Windows installation.\r\n
0xb60003ec | NLS codepage operation failed for the codepage %1 because the file %2 is corrupted. To correct this error, replace this file or repair your Windows installation.\r\n
0xb60003ed | NLS operation failed for %1 locale because the file %2\globalization\%1.nlp is missing.  To fix this problem, reinstall this custom locale.\r\n
0xb60003ee | NLS operation failed for %1 locale because the file %2\globalization\%1.nlp is corrupted.  To fix this problem, reinstall this custom locale.\r\n
0xb60005dc | Group Policy has prevented process number %1 (%2) from changing the standards and format information for the user.\r\n
0xb60005dd | Group Policy has prevented the geographical location from being changed.\r\n
0xb60005de | Group Policy has prevented the user from changing their user locale to "%1".\r\n
0xb60005df | Group Policy does not allow custom user locales for standards and formats. The user was unable to select "%1" as their user locale.\r\n
0xb60007d0 | NLS operation recreated the registry key %1.\r\n
0xb60009c4 | Windows has detected inconsistencies in NLS internal data. To correct this problem, log off of Windows and log on again.\r\n
0xb6000bb8 | Process number %1 (%2) called SetLocaleInfo(%3, %4, "%5")  successfully.\r\n
0xb6000bb9 | Process number %1 (%2) called SetCalendarInfo(%3, %4, %5, "%6")  successfully.\r\n
0xb6000bba | Process number %1 (%2) called SetUserGeoID(%3) successfully.\r\n
0xb6000bbb | The system updated the locale "%1" with flag %2. Process number %3 (%4). Return code is %5.\r\n
0xb6002710 | The user tried to apply an unattended XML file (%1) in an unsupported format. Reason: %3 (Line %2). The system has not been changed.\r\n
0xb6002711 | Unsupported XML in function.\r\n
0xb6002713 | The user locale "%1" (specified by the UserLocale element) is not a supported locale name or is not installed on the system. The user locale was not changed.\r\n
0xb6002714 | Unsupported alternate sort "%1".\r\n
0xb6002715 | "%1" is not a supported sort order for locale "%2".\r\n
0xb6002716 | The selected system locale (specified by the SystemLocale element) is not installed on the system. The system locale was not changed.\r\n
0xb6002717 | Internal error while changing System locale (specified by the SystemLocale element).\r\n
0xb6002718 | Error while changing keyboard/input method for "%1".\r\n
0xb6002719 | Error while changing location preference (geoid): %1. This error may be caused by an unsupported location preference (geoid) or a Group Policy restriction. Error code is %2. Error message: %3\r\n
0xb600271a | Failed to change UI Language to "%1". Status code is: %2.\r\n
0xb600271b | Failed to change UI Language fallback order to "%1". Status code is: %2.\r\n
0xb600271c | The user tried to apply an unattended XML file %1, but the file does not exist.\r\n
0xb600271d | Error while the user changed setting "%1" with value "%2" for the current user locale. Error code is: %3. Error message: %4\r\n
0xb600271e | The selected calendar "%1;" (specified by the Calendar element) is not a supported calendar. The user locale was not changed.\r\n
0xb600271f | The selected TwoDigitYearMax "%1;" (specified by the TwoDigitYearMax element) is not a supported value. The user locale was not changed.\r\n
0xb600277f | The user does not have permission to change the TwoDigitYearMax setting\r\n
0xb6002780 | The user does not have permission to copy current settings to the Default and/or System Account\r\n
0xb6002781 | The user does not have permission to change the system locale (specified by the SystemLocale element).\r\n
0xb6002783 | The user does not have permission to change the calendar.\r\n
0xb60027e8 | Unexpected failure. Stack overflow\r\n
0xb60027ea | Unexpected failure. Unsupported flag\r\n
0xb60027eb | Unexpected failure. Unsupported parameter\r\n
0xb60027ec | Unexpected failure. Unrecoverable error.\r\n
0xb60027ed | Failed when calling internal function. Error code is: %1\r\n
0xb60027ee | The operation timed out.\r\n
0xb600283c | Group Policy has prevented the user from changing the system locale (specified by the SystemLocale element).\r\n
0xb60032c8 | The user changed their user locale (specified by the UserLocale element) to "%1".\r\n
0xb60032c9 | The user reset all customizations for their user locale "%1" (specified by the UserLocale element) to the system default.\r\n
0xb60032ca | The user changed their user locale setting "%1" (specified by the UserLocale element) to "%2".\r\n
0xb60032cb | The locale has to be changed to the current locale in order to make customizations.\r\n
0xb60032cc | The user changed their alternate sort to "%1".\r\n
0xb60032cd | The user changed their calendar to "%1".\r\n
0xb60032ce | The user changed their TwoDigitYearMax to %1.\r\n
0xb60032cf | The user changed their location preference (geoid) to %1.\r\n
0xb60032d0 | The system locale (specified by the SystemLocale element) was changed to "%1".\r\n
0xb60032d1 | The current user settings were copied to the default user account.\r\n
0xb60032d2 | The current user settings were copied to the system accounts.\r\n
0xb60032d3 | The user has changed their UI Language to "%1".\r\n
0xb60032d4 | The user has changed their UI Language fallback order to "%1".\r\n
0xb7000001 | Deprecated module %1.\r\n
0xb7000002 | Process %2 encountered a fatal user callback exception.\r\n
0xb9000001 | The process failed to handle ERROR_ELEVATION_REQUIRED during the creation of a child process.\r\n
0xba000001 | Deprecated COM CLSID %1.\r\n
0xbc0007d0 | MUI notify operation failed with status code %1. No callbacks were invoked.\r\n
0xbc0007d1 | MUI Callback failed for file %1 because it can not be loaded. To correct this error, replace this file or repair your Windows installation.\r\n
0xbc0007d2 | MUI Callback failed for file %1 registered as type %2 because the function %3 does not exist in the dll. To correct this error, replace the file or fix the registry entry.\r\n
0xbc0007d3 | MUI Callback failed for file %1 because it is not signed by Microsoft. To correct this error, replace with the original file that came with this Windows installation.\r\n
0xbc0007d4 | MUI Callback file %1 cannot be found. To correct this error, repair the registry or copy the file to the specified location.\r\n
0xbc0007d6 | Wow redirection could not be disabled. New resource cache will not be built.\r\n
0xbc0007d7 | Resource cache cannot be opened in writable mode. New resource cache will not be built.\r\n
0xbc0007d8 | Live resource cache could not be disabled.\r\n
0xbc0007d9 | Unable to retrieve language settings from MUI API. New resource cache will not be built.\r\n
0xbc0007da | Unable to parse the cacheable file list or write to the resource cache manifest. If configuration file was specified as command-line parameter, check that file exists and has correct format.  New resource cache will not be built.\r\n
0xbc0007db | Changes made to resource cache manifest cannot be written to disk. New resource cache will not be built.\r\n
0xbc0007dc | New resource cache could not be built due to internal error: %1.\r\n
0xbc0007dd | Newly built resource cache could not be installed on the system.\r\n
0xbc0007de | Resource cache manifest could not be created. New resource cache will not be built.\r\n
0xbc000bb8 | MUI notification for UI Language change has been invoked with flags set to %1 and the new languages set to %2 and the previous languages set to %3. The extended flags is set to %4\r\n
0xbc000bba | MUI notification callback API %2 in %1 returned with code %3.\r\n
0xbc000bbb | MUI resource cache builder has been called with the following parameters: %1.\r\n
0xbc000bbc | MUI resource cache manifest entry for file %1 has been updated. Affinity: '%2', Sequence: %3, and Priority: %4\r\n
0xbc000bbd | Start: %1\r\n
0xbc000bbe | End: %1\r\n
0xbc000bbf | New resource cache built and installed on system. New cache index is %1, live cache index is %2 and config is set to %3.\r\n
0xbc000bc4 | Resource file %1 will not be cached since it is not used frequently in the system.\r\n
0xbc000bc5 | The system is constrained in RAM, total disk space or free disk space, so the MUI resource cache will not be maintained.\r\n
0xbc000fa0 | Unable to parse configuration parameters. The configuration parameters will be ignored.\r\n
0xd4000001 | Unknown failure\r\n
0xd4000002 | General internal failure\r\n
0xd4000003 | Operation is not supported by SKU\r\n
0xd4000004 | Partition unit does not exist\r\n
0xd4000005 | Partition units are not compatible\r\n
0xd4000006 | A partition unit is not ready\r\n
0xd4000007 | Partition unit resources are not supported\r\n
0xd4000008 | System quiesce failure\r\n
0xd4000009 | Chipset driver error\r\n
0xd400000a | Chipset driver capabilities are not supported\r\n
0xd400000b | Memory allocation failure\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x0000012c | Microsoft-Windows-Kernel-AppCompat\r\n
0x0000012d | Microsoft-Windows-AIT\r\n
0x0000012e | Microsoft-Windows-Kernel-ApphelpCache\r\n
0x0000012f | Microsoft-Windows-AeSwitchBack\r\n
0x00000130 | Microsoft-Windows-AeLookupServiceTrigger\r\n
0x00000131 | Lookup counter [%1], Hit counter [%2], File path [%4]\r\n
0x00000132 | Insert counter [%1], Update counter [%2], File path [%5]\r\n
0x00000133 | Remove counter [%1], File path [%3]\r\n
0x00000134 | Clear counter [%1]\r\n
0x00000135 | %1\r\n
0x00000136 | The executable %2 received an access denied error when trying to modify the registry key %4.\r\n
0x000001f4 | Microsoft-Windows-Kernel-Network\r\n
0x000001f5 | Data sent.\r\n
0x000001f6 | Data received.\r\n
0x000001f7 | Connection attempted.\r\n
0x000001f8 | Disconnect issued.\r\n
0x000001f9 | Data retransmitted.\r\n
0x000001fa | Connection accepted.\r\n
0x000001fb | Reconnect attempted.\r\n
0x000001fc | TCP connection attempt failed.\r\n
0x000001fd | Protocol copied data on behalf of user.\r\n
0x000001fe | Data sent over UDP protocol.\r\n
0x000001ff | Data received over UDP protocol.\r\n
0x00000200 | UDP connection attempt failed.\r\n
0x00000201 | TCPv4: %2 bytes transmitted from %4:%6 to %3:%5.\r\n
0x00000202 | TCPv4: %2 bytes received from %4:%6 to %3:%5.\r\n
0x00000203 | TCPv4: Connection attempted between %4:%6 and %3:%5.\r\n
0x00000204 | TCPv4: Connection closed between %4:%6 and %3:%5.\r\n
0x00000205 | TCPv4: %2 bytes retransmitted from %4:%6 to %3:%5.\r\n
0x00000206 | TCPv4: Connection established between %4:%6 and %3:%5.\r\n
0x00000207 | TCPv4: Reconnect attempt between %4:%6 and %3:%5.\r\n
0x00000208 | TCPv4: Connection attempt failed with error code %2.\r\n
0x00000209 | TCPv4: %2 bytes copied in protocol on behalf of user for connection between %4:%6 and %3:%5.\r\n
0x0000020a | UDPv4: %2 bytes transmitted from %4:%6 to %3:%5.\r\n
0x0000020b | UDPv4: %2 bytes received from %4:%6 to %3:%5.\r\n
0x0000020c | UDPv4: Connection attempt failed with error code %2.\r\n
0x0000020d | TCPv6: %2 bytes transmitted from %4:%6 to %3:%5.\r\n
0x0000020e | TCPv6: %2 bytes received from %4:%6 to %3:%5.\r\n
0x0000020f | TCPv6: Connection attempted between %4:%6 and %3:%5.\r\n
0x00000210 | TCPv6: Connection closed between %4:%6 and %3:%5.\r\n
0x00000211 | TCPv6: %2 bytes retransmitted from %4:%6 to %3:%5.\r\n
0x00000212 | TCPv6: Connection established between %4:%6 and %3:%5.\r\n
0x00000213 | TCPv6: Reconnect attempt between %4:%6 and %3:%5.\r\n
0x00000214 | TCPv6: %2 bytes copied in protocol on behalf of user for connection between %4:%6 and %3:%5.\r\n
0x00000215 | UDPv6: %2 bytes transmitted from %4:%6 to %3:%5.\r\n
0x00000216 | UDPv6: %2 bytes received from %4:%6 to %3:%5.\r\n
0x00000258 | Microsoft-Windows-Kernel-Disk\r\n
0x00000259 | %3 bytes read from disk %1 at %5.\r\n
0x0000025a | %3 bytes written to disk %1 at %5.\r\n
0x0000025b | Buffers flushed to disk %1.\r\n
0x000002bc | Microsoft-Windows-Kernel-Boot\r\n
0x000002bd | System was booted in %1x%2@%3bpp.\r\n
0x000002be | BootUX screen was displayed in %1x%2@%3bpp.\r\n
0x000002bf | Video bit transfer rate is %1 bytes per ms.\r\n
0x000002c0 | Boot library accessed file %2 on Device %1. Read %3 bytes and wrote %4 bytes.\r\n
0x000002c1 | File IO for boot application %1: Total Bytes Read = %2, Total Bytes Written = %3.\r\n
0x000002c2 | Image %1 failed IntegrityCheck reason is %3. Image flags are %2. Error ignored due to debugger %4.\r\n
0x000002c3 | Bootmgr duration is %1 milliseconds.\r\n
0x000002c4 | Image %1 is not self-signed.\r\n
0x000002c5 | A device (%1) that was enumerated by the BIOS was inaccessible to the boot environment.\r\n
0x000002c6 | Variable %1 requires %2 bytes and was set with status %3.\r\n
0x000002c7 | Element %2 of application %1 was not in policy.\r\n
0x000002c8 | A Secure Boot Policy update resulted in status %1.\r\n
0x000002c9 | A Secure Boot Revocation List update resulted in status %1.\r\n
0x00000320 | Microsoft-Windows-Kernel-File\r\n
0x00000385 | Microsoft-Windows-Kernel-EventTracing\r\n
0x00000386 | Session "%1" failed to write to log file "%2" with the following error: %3\r\n
0x00000387 | The backing-file for the real-time session "%1" has reached its maximum size. As a result, new events will not be logged to this session until space becomes available. This error is often caused by starting a trace session in real-time mode without having any real-time consumers.\r\n
0x00000388 | Session "%1" failed to start with the following error: %3\r\n
0x00000389 | Session "%1" stopped due to the following error: %3\r\n
0x0000038a | The maximum file size for session "%1" has been reached. As a result, events might be lost (not logged) to file "%2". The maximum files size is currently set to %5 bytes.\r\n
0x0000038b | An error was encountered while tracing session "%2" was switching to the "%1" event log file. Error: %3\r\n
0x0000038e | Provider %1 was registered with Event Tracing for Windows.\r\n
0x0000038f | Provider %1 was unregistered from Event Tracing for Windows.\r\n
0x00000390 | Session "%3" was started.\r\n
0x00000391 | Session "%3" was stopped.\r\n
0x00000392 | The configuration of session "%3" has been modified.\r\n
0x00000393 | The events from session "%3" have been flushed.\r\n
0x00000394 | Provider %1 has been enabled to session "%2".\r\n
0x00000395 | Provider %1 is no longer enabled to session "%2".\r\n
0x00000396 | The security settings of provider %1 have been modified from %2 to %3.\r\n
0x00000397 | The security descriptor for session "%3" has been updated.\r\n
0x00000398 | Provider\r\n
0x00000399 | Session\r\n
0x0000039b | Logging\r\n
0x0000039d | Stop\r\n
0x0000039e | Start\r\n
0x0000039f | Disable\r\n
0x000003a0 | Enable\r\n
0x000003a1 | Unregister\r\n
0x000003a2 | Register\r\n
0x000003a3 | Flush\r\n
0x000003a4 | Configure\r\n
0x000003a7 | Write Buffer\r\n
0x000003a8 | File Switch\r\n
0x000003aa | Provider\r\n
0x000003ab | Session\r\n
0x000003ac | Stack correlation event. This event contains a call stack which is associated with a prior event which is correlated by the MatchId.\r\n
0x000003ad | Stack Trace\r\n
0x000003ae | User Mode Stack Trace\r\n
0x000003af | Microsoft-Windows-Kernel-EventTracing/Analytic\r\n
0x000003b0 | Microsoft-Windows-Kernel-EventTracing/Admin\r\n
0x000003b1 | Lost Event\r\n
0x000003b2 | Lost Event\r\n
0x000003b3 | Logger mode incompatible with Append mode\r\n
0x000003b4 | OS version mismatch\r\n
0x000003b5 | Pointer size mismatch\r\n
0x000003b6 | Unsupported BufferSize\r\n
0x000003b7 | BufferSize mismatch\r\n
0x000003b8 | Preallocate mode is incompatible with Append mode\r\n
0x000003b9 | File size query failed\r\n
0x000003ba | Maximum file size reached\r\n
0x000003bb | Number of buffers written is zero\r\n
0x000003bc | Numberf of processors mismatch\r\n
0x000003c0 | Microsoft-Windows-Kernel-StoreMgr\r\n
0x000003c1 | Microsoft-Windows-Kernel-StoreMgr/Operational\r\n
0x000003c2 | %5%n%nVirtual Address: %2%nPhysical Address: %3%nCorruption Window Size: %4\r\n
0x000003c3 | A memory corruption was detected and handled. Memory diagnostics should be run on this machine and, if necessary, memory chips should be replaced.\r\n
0x000003c4 | A data corruption was detected and handled in a ReadyBoost cache. This corruption was most likely caused by faulty hardware. While ReadyBoost will always detect and handle these errors, seeing a lot of these may mean that the ReadyBoost device has worn out which reduces its performance. You should consider replacing the ReadyBoost cache device.\r\n
0x000003c5 | A ReadyBoost cache failed to persist across boot. This may happen if the cache device was modified on another computer or if this computer was booted into another operating system.\r\n
0x000003c6 | %1%n%nDevice name: %4%nCache path: %6\r\n
0x000003c7 | A ReadyBoost cache was deleted due to repeated data corruption instances on the associated device that have been detected and handled. While ReadyBoost will always detect and handle these errors, repeated corruption instances may mean that the ReadyBoost device has worn out which reduces its performance. You should consider replacing the ReadyBoost device.\r\n
0x000003c8 | A ReadyBoost cache was deleted due to repeated I/O failures on the associated device. This typically happens when the device (e.g. an SD card) is removed, but it may also indicate faulty hardware.\r\n
0x000003e8 | Microsoft-Windows-LicensingStartServiceTrigger\r\n
0x000003f2 | Microsoft-Windows-WSServiceStartServiceTrigger\r\n
0x01000001 | The system time has changed to %1 from %2.%n%nChange Reason: %3.\r\n
0x01000002 | License policy-cache corruption detected.\r\n
0x01000003 | License policy-cache corruption has been fixed.\r\n
0x01000004 | License policy-cache has expired because it was not updated within expected duration.\r\n
0x01000005 | {Registry Hive Recovered} Registry hive (file): '%3' was corrupted and it has been recovered. Some data might have been lost.\r\n
0x01000006 | An I/O operation initiated by the Registry failed unrecoverably.The Registry could not flush hive (file): '%3'.\r\n
0x0100000b | TxR init phase for hive %2 (TM: %3, RM: %4) finished with result=%5 (Internal code=%6).\r\n
0x0100000c | The operating system started at system time %7.\r\n
0x0100000d | The operating system is shutting down at system time %1.\r\n
0x0100000f | Hive %2 was reorganized with a starting size of %3 bytes and an ending size of %4 bytes.\r\n
0x01000010 | The access history in hive %2 was cleared updating %3 keys and creating %4 modified pages.\r\n
0x0a000032 | Access to %1 is monitored by policy rule %2.\r\n
0x0a000361 | Access to %1 has been restricted by your Administrator by the default software restriction policy level.\r\n
0x0a000362 | Access to %1 has been restricted by your Administrator by location with policy rule %2 placed on path %3.\r\n
0x0a000363 | Access to %1 has been restricted by your Administrator by software publisher policy.\r\n
0x0a000364 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0x0a000372 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0x0c00000a | The system firmware has allocated a memory region previously determined to be unreliable. This has the potential to cause system instability and/or data corruption.\r\n
0x0c000010 | Windows failed to resume from hibernate with error status %1.\r\n
0x0c000011 | The boot manager multi OS selection screen was displayed.\r\n
0x0c000012 | There are %1 boot options on this system.\r\n
0x0c000013 | There are %1 boot tool options on this system.\r\n
0x0c000014 | The last shutdown's success status was %1. The last boot's success status was %2.\r\n
0x0c000015 | The OS loader advanced options menu was displayed and the user selected option %1.\r\n
0x0c000016 | The OS loader edit options menu was displayed.\r\n
0x0c000017 | The Windows key was pressed during boot.\r\n
0x0c000018 | The F8 key was pressed during boot.\r\n
0x0c000019 | The boot menu policy was %1.\r\n
0x0c00001a | A one-time boot sequence was used during this boot.\r\n
0x0c00001b | The boot type was %1.\r\n
0x0c00001d | Windows failed fast startup with error status %1.\r\n
0x0c00001e | The firmware reported boot metrics.\r\n
0x0c000020 | The bootmgr spent %1 ms waiting for user input.\r\n
0x0f000009 | App %1 was terminated with error %2 because of an issue with Windows binary %3. This could be because the binary is unsigned, contains an untrusted signature, or has been corrupted or tampered with. Refresh your PC to fix this issue.\r\n
0x10000001 | Structured State\r\n
0x10000002 | Unstructured Reset\r\n
0x10000003 | Out Of Memory\r\n
0x10000004 | Apiset Error\r\n
0x10000005 | WinRT\r\n
0x10000006 | Low-level Data Store Error\r\n
0x10000021 | Verbose context events\r\n
0x10000022 | Scenario trigger events\r\n
0x10000034 | SQM\r\n
0x11000005 | Time\r\n
0x16000005 | Deprecated dlls\r\n
0x16000006 | Fatal user callback exception\r\n
0x16000007 | Module load failure\r\n
0x16000008 | Launch 16bit application\r\n
0x17000031 | Response Time\r\n
0x19000005 | Deprecated COM interfaces\r\n
0x1f000001 | Process\r\n
0x1f000002 | AppContainer\r\n
0x3000000a | Scenario start enables context providers to the WDI context logger.\r\n
0x3000000b | Scenario end disables context providers to the WDI context logger.\r\n
0x3000000c | When a scenario has remained in-flight beyond the maximum time window it is automatically terminated by the SEM.\r\n
0x3000000d | A scenario start attempt failed in the SEM.\r\n
0x3000000e | A scenario end attempt failed in the SEM.\r\n
0x3000000f | The SEM received a request to start a new scenario, but the maximum number of scenarios were already in-flight.\r\n
0x30000010 | There is an invalid configuration parameter in the SEM registry namespace.\r\n
0x30000011 | The SEM is configured with more scenarios than the maximum allowed count.\r\n
0x30000012 | The SEM is configured with a scenario with too many context providers.\r\n
0x30000013 | The SEM is configured with a scenario that has too many end events.\r\n
0x30000014 | The number of providers specified across all scenarios is above the maximum allowed amount.\r\n
0x31000000 | Info\r\n
0x32000001 | Start\r\n
0x32000002 | Stop\r\n
0x3500001e | NLS data table operations\r\n
0x3500001f | NLS initialization\r\n
0x35000020 | NLS configuration changes\r\n
0x35000021 | NLS operations\r\n
0x35000022 | NLS clean-up operations\r\n
0x3b00001e | Start\r\n
0x3b00001f | Invoke callback function\r\n
0x3b000020 | Disable live cache\r\n
0x3b000021 | Update resource cache manifest\r\n
0x3b000022 | Build resource cache\r\n
0x3b000023 | Start\r\n
0x3b000024 | End\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x55000001 | Critical\r\n
0x55000005 | Verbose\r\n
0x70000009 | SEM Scenario Lifecycle\r\n
0x7000000a | SEM Initialization\r\n
0x7500001e | NLS code page functions\r\n
0x75000020 | NLS date/time functions\r\n
0x75000021 | NLS Unattended Regional and Language Options\r\n
0x75000022 | NLS group policy\r\n
0x75000023 | NLS locale functions\r\n
0x7b00001e | MUI NotifyUILanguageChange task\r\n
0x7b00001f | MUI resource cache builder\r\n
0x90000001 | Microsoft-Windows-Kernel-WDI\r\n
0x90000002 | Microsoft-Windows-Kernel-WDI/Analytic\r\n
0x90000003 | Microsoft-Windows-Kernel-WDI/Debug\r\n
0x90000004 | Microsoft-Windows-Kernel-WDI/Operational\r\n
0x90000005 | Microsoft-Windows-AppModel-State\r\n
0x90000006 | Microsoft-Windows-AppModel-State/Debug\r\n
0x90000007 | Microsoft-Windows-AppModel-State/Diagnostic\r\n
0x91000001 | Microsoft-Windows-Kernel-General\r\n
0x91000002 | System\r\n
0x92000001 | Microsoft-Windows-Kernel-Process\r\n
0x93000001 | Microsoft-Windows-Kernel-Registry\r\n
0x94000001 | Microsoft-Windows-Kernel-Acpi\r\n
0x95000001 | Microsoft-Windows-International\r\n
0x95000002 | Microsoft-Windows-International/Operational\r\n
0x96000001 | Microsoft-Windows-User-Loader\r\n
0x97000001 | Microsoft-Windows-Kernel-BootDiagnostics\r\n
0x98000001 | Microsoft-Windows-UAC\r\n
0x98000002 | Microsoft-Windows-UAC/Operational\r\n
0x99000001 | Microsoft-Windows-COM\r\n
0x9a000001 | Microsoft-Windows-SoftwareRestrictionPolicies\r\n
0x9a000002 | Application\r\n
0x9b000001 | Microsoft-Windows-MUI\r\n
0x9b000002 | Microsoft-Windows-MUI/Operational\r\n
0x9b000003 | Microsoft-Windows-MUI/Admin\r\n
0x9b000004 | Microsoft-Windows-MUI/Analytic\r\n
0x9b000005 | Microsoft-Windows-MUI/Debug\r\n
0x9d000001 | Microsoft-Windows-PCI\r\n
0x9e000001 | Microsoft-Windows-Kernel-ShimEngine\r\n
0x9e000002 | Microsoft-Windows-Kernel-ShimEngine/Operational\r\n
0x9f000001 | Microsoft-Windows-AppModel-Runtime\r\n
0x9f000002 | Microsoft-Windows-AppModel-Runtime/Analytic\r\n
0xb0000001 | Error while deleting file: %1. Error Code: %2\r\n
0xb0000002 | Error while deleting directory: %1. Error Code: %2\r\n
0xb0000003 | Error while allocating memory\r\n
0xb0000004 | ApiSet Function: %1 returned with Error Code: %2\r\n
0xb0000005 | Low-level data store access error. Function: %1 returned with Error Code: %2\r\n
0xb0000006 | Cleanup of temporary state has been skipped due to low disk usage.\r\n
0xb0000007 | Cleanup of temporary state has completed.\r\n
0xb0000008 | Cleanup of temporary state was unable to enumerate the user profiles.  Object: %1, Error Code: %2.\r\n
0xb0000009 | Cleanup of temporary state has aborted unexpectedly.\r\n
0xb0000020 | The Scenario Event Mapper started a scenario for provider %1 (event ID %2) with %4 context providers.  The context logger dropped event count was %3.\r\n
0xb0000021 | The Scenario Event Mapper stopped a scenario for provider %1 (event ID %2) with %4 context providers.  The context logger dropped event count was %3.\r\n
0xb0000022 | An in-flight scenario from provider %1 (event ID %2) timed out and was stopped automatically by the Scenario Event Mapper.\r\n
0xb0000023 | The Scenario Event Mapper was unable to start a new scenario for provider %1 (event ID %2) because the maximum number of scenarios are already in flight.\r\n
0xb0000024 | The Scenario Event Mapper was unable to start a scenario for provider %1 (event ID %2).  The error code was %3.\r\n
0xb0000025 | The Scenario Event Mapper was unable to stop a scenario for provider %1 (event ID %2).  The error code was %3.\r\n
0xb0000026 | The Scenario Event Mapper is configured with more than the maximum number of scenarios.  The scenario for provider %1 (event ID %2) will be ignored.\r\n
0xb0000027 | The Scenario Event Mapper is configured with more than the maximum number of context providers for the scenario with provider %1 (event ID %2).  The scenario will be ignored.\r\n
0xb0000028 | The Scenario Event Mapper is configured with more than the maximum number of end events for the scenario with provider %1 (event ID %2).  The scenario will be ignored.\r\n
0xb0000029 | The Scenario Event Mapper is configured with more than the maximum number of providers.  The provider %1 will be ignored.\r\n
0xb000002a | The Scenario Event Mapper is configured with an unsupported scenario. The scenario for provider %1 (event ID %2) encountered error code %3 and will be ignored.\r\n
0xb1000001 | The system time has changed to %1 from %2.\r\n
0xb2000001 | Process %1 started at time %2 by parent %3 running in session %4 with name %5.\r\n
0xb2000002 | Process %1 (which started at time %2) stopped at time %3 with exit code %4.\r\n
0xb2000003 | Thread %2 (in Process %1) started.\r\n
0xb2000004 | Thread %2 (in Process %1) stopped.\r\n
0xb2000005 | Process %3 had an image loaded with name %7.\r\n
0xb2000006 | Process %3 had an image unloaded with name %7.\r\n
0xb2000007 | Base CPU priority of thread %2 in process %1 was changed from %3 to %4.\r\n
0xb2000008 | CPU priority of thread %2 in process %1 was changed from %3 to %4.\r\n
0xb2000009 | Page priority of thread %2 in process %1 was changed from %3 to %4.\r\n
0xb200000a | I/O priority of thread %2 in process %1 was changed from %3 to %4.\r\n
0xb200000b | Execution of the process %1 has been suspended.\r\n
0xb200000c | Execution of the process %1 has been resumed.\r\n
0xb2010001 | Process %1 started at time %2 by parent %3 running in session %4 with name %6.\r\n
0xb4000001 | A memory range descriptor has been marked as reserved.\r\n
0xb4000002 | Unexpected GPE event was fired on GPE bits that should be disabled.\r\n
0xb4000003 | A temperature change notification (Notify(thermal_zone, 0x80)) for ACPI thermal zone %2 has been received.\n            %n_TMP = %3K\n            %n_PSV = %4K\n            %n_AC0 = %5K\n            %n_AC1 = %6K\n            %n_AC2 = %7K\n            %n_AC3 = %8K\n            %n_AC4 = %9K\n            %n_AC5 = %10K\n            %n_AC6 = %11K\n            %n_AC7 = %12K\n            %n_AC8 = %13K\n            %n_AC9 = %14K\n            %n_HOT = %15K\n            %n_CRT = %16K\r\n
0xb4000004 | A trip point change notification (Notify(thermal_zone, 0x81)) for ACPI thermal zone %2 has been received.\n            %n_TMP = %3K\n            %n_PSV = %4K\n            %n_AC0 = %5K\n            %n_AC1 = %6K\n            %n_AC2 = %7K\n            %n_AC3 = %8K\n            %n_AC4 = %9K\n            %n_AC5 = %10K\n            %n_AC6 = %11K\n            %n_AC7 = %12K\n            %n_AC8 = %13K\n            %n_AC9 = %14K\n            %n_HOT = %15K\n            %n_CRT = %16K\r\n
0xb4000005 | The active cooling device %6 has been turned %8.\n            %nThermal zone device instance: %2\n            %nActive cooling package: _AC%3\n            %nNamespace object: _AL%4\r\n
0xb4000006 | The active cooling device %6 has been turned %7.\n            %nThermal zone device instance: %2\n            %nActive cooling package: _AC%3\n            %nNamespace object: _AL%4\r\n
0xb4000007 | ACPI method %2 evaluation has %3.\r\n
0xb4000008 | The active cooling device %2 has been turned %3.\r\n
0xb4000009 | The passive cooling device %2 throttle has changed to %3 percent.\r\n
0xb400000a | The device %2 has the following cooling state.\n            %nActive cooling: %3\n            %nPassive cooling: %4 percent\r\n
0xb50003e9 | The NLS operation failed because the registry key %1 cannot be opened. Error code is %2. Error message: %3\r\n
0xb50003ea | The NLS operation failed because the registry key %1 cannot be opened. Status code is %2.\r\n
0xb50003eb | NLS codepage operation failed for the codepage %1 because the file %2 is missing.  To correct this error, replace this file or repair your Windows installation.\r\n
0xb50003ec | NLS codepage operation failed for the codepage %1 because the file %2 is corrupted. To correct this error, replace this file or repair your Windows installation.\r\n
0xb50003ed | NLS operation failed for %1 locale because the file %2\globalization\%1.nlp is missing.  To fix this problem, reinstall this custom locale.\r\n
0xb50003ee | NLS operation failed for %1 locale because the file %2\globalization\%1.nlp is corrupted.  To fix this problem, reinstall this custom locale.\r\n
0xb50005dc | Group Policy has prevented process number %1 (%2) from changing the standards and format information for the user.\r\n
0xb50005dd | Group Policy has prevented the geographical location from being changed.\r\n
0xb50005de | Group Policy has prevented the user from changing their user locale to "%1".\r\n
0xb50005df | Group Policy does not allow custom user locales for standards and formats. The user was unable to select "%1" as their user locale.\r\n
0xb50007d0 | NLS operation recreated the registry key %1.\r\n
0xb50009c4 | Windows has detected inconsistencies in NLS internal data. To correct this problem, log off of Windows and log on again.\r\n
0xb5000bb8 | Process number %1 (%2) called SetLocaleInfo(%3, %4, "%5")  successfully.\r\n
0xb5000bb9 | Process number %1 (%2) called SetCalendarInfo(%3, %4, %5, "%6")  successfully.\r\n
0xb5000bba | Process number %1 (%2) called SetUserGeoID(%3) successfully.\r\n
0xb5000bbb | The system updated the locale "%1" with flag %2. Process number %3 (%4). Return code is %5.\r\n
0xb5002710 | The user tried to apply an unattended XML file (%1) in an unsupported format. Reason: %3 (Line %2). The system has not been changed.\r\n
0xb5002711 | Unsupported XML in function.\r\n
0xb5002713 | The user locale "%1" (specified by the UserLocale element) is not a supported locale name or is not installed on the system. The user locale was not changed.\r\n
0xb5002714 | Unsupported alternate sort "%1".\r\n
0xb5002715 | "%1" is not a supported sort order for locale "%2".\r\n
0xb5002716 | The selected system locale (specified by the SystemLocale element) is not installed on the system. The system locale was not changed.\r\n
0xb5002717 | Internal error while changing System locale (specified by the SystemLocale element).\r\n
0xb5002718 | Error while changing keyboard/input method for "%1".\r\n
0xb5002719 | Error while changing location preference (geoid): %1. This error may be caused by an unsupported location preference (geoid) or a Group Policy restriction. Error code is %2. Error message: %3\r\n
0xb500271a | Failed to change UI Language to "%1". Status code is: %2.\r\n
0xb500271b | Failed to change UI Language fallback order to "%1". Status code is: %2.\r\n
0xb500271c | The user tried to apply an unattended XML file %1, but the file does not exist.\r\n
0xb500271d | Error while the user changed setting "%1" with value "%2" for the current user locale. Error code is: %3. Error message: %4\r\n
0xb500271e | The selected calendar "%1;" (specified by the Calendar element) is not a supported calendar. The user locale was not changed.\r\n
0xb500271f | The selected TwoDigitYearMax "%1;" (specified by the TwoDigitYearMax element) is not a supported value. The user locale was not changed.\r\n
0xb500277f | The user does not have permission to change the TwoDigitYearMax setting\r\n
0xb5002780 | The user does not have permission to copy current settings to the Default and/or System Account\r\n
0xb5002781 | The user does not have permission to change the system locale (specified by the SystemLocale element).\r\n
0xb5002783 | The user does not have permission to change the calendar.\r\n
0xb50027e8 | Unexpected failure. Stack overflow\r\n
0xb50027ea | Unexpected failure. Unsupported flag\r\n
0xb50027eb | Unexpected failure. Unsupported parameter\r\n
0xb50027ec | Unexpected failure. Unrecoverable error.\r\n
0xb50027ed | Failed when calling internal function. Error code is: %1\r\n
0xb50027ee | The operation timed out.\r\n
0xb500283c | Group Policy has prevented the user from changing the system locale (specified by the SystemLocale element).\r\n
0xb50032c8 | The user changed their user locale (specified by the UserLocale element) to "%1".\r\n
0xb50032c9 | The user reset all customizations for their user locale "%1" (specified by the UserLocale element) to the system default.\r\n
0xb50032ca | The user changed their user locale setting "%1" (specified by the UserLocale element) to "%2".\r\n
0xb50032cb | The locale has to be changed to the current locale in order to make customizations.\r\n
0xb50032cc | The user changed their alternate sort to "%1".\r\n
0xb50032cd | The user changed their calendar to "%1".\r\n
0xb50032ce | The user changed their TwoDigitYearMax to %1.\r\n
0xb50032cf | The user changed their location preference (geoid) to %1.\r\n
0xb50032d0 | The system locale (specified by the SystemLocale element) was changed to "%1".\r\n
0xb50032d1 | The current user settings were copied to the default user account.\r\n
0xb50032d2 | The current user settings were copied to the system accounts.\r\n
0xb50032d3 | The user has changed their UI Language to "%1".\r\n
0xb50032d4 | The user has changed their UI Language fallback order to "%1".\r\n
0xb6000001 | Deprecated module %1.\r\n
0xb6000002 | Process %2 encountered a fatal user callback exception.\r\n
0xb6000003 | Module %3 failed to load [%1].\r\n
0xb6000004 | The process launches a 16 bit process.\r\n
0xb8000001 | The process failed to handle ERROR_ELEVATION_REQUIRED during the creation of a child process.\r\n
0xb9000001 | Deprecated COM CLSID %1.\r\n
0xbb0007d0 | MUI notify operation failed with status code %1. No callbacks were invoked.\r\n
0xbb0007d1 | MUI Callback failed for file %1 because it can not be loaded. To correct this error, replace this file or repair your Windows installation.\r\n
0xbb0007d2 | MUI Callback failed for file %1 registered as type %2 because the function %3 does not exist in the dll. To correct this error, replace the file or fix the registry entry.\r\n
0xbb0007d3 | MUI Callback failed for file %1 because it is not signed by Microsoft. To correct this error, replace with the original file that came with this Windows installation.\r\n
0xbb0007d4 | MUI Callback file %1 cannot be found. To correct this error, repair the registry or copy the file to the specified location.\r\n
0xbb0007d6 | Wow redirection could not be disabled. New resource cache will not be built.\r\n
0xbb0007d7 | Resource cache cannot be opened in writable mode. New resource cache will not be built.\r\n
0xbb0007d8 | Live resource cache could not be disabled.\r\n
0xbb0007d9 | Unable to retrieve language settings from MUI API. New resource cache will not be built.\r\n
0xbb0007da | Unable to parse the cacheable file list or write to the resource cache manifest. If configuration file was specified as command-line parameter, check that file exists and has correct format.  New resource cache will not be built.\r\n
0xbb0007db | Changes made to resource cache manifest cannot be written to disk. New resource cache will not be built.\r\n
0xbb0007dc | New resource cache could not be built due to internal error: %1.\r\n
0xbb0007dd | Newly built resource cache could not be installed on the system.\r\n
0xbb0007de | Resource cache manifest could not be created. New resource cache will not be built.\r\n
0xbb000bb8 | MUI notification for UI Language change has been invoked with flags set to %1 and the new languages set to %2 and the previous languages set to %3. The extended flags is set to %4\r\n
0xbb000bba | MUI notification callback API %2 in %1 returned with code %3.\r\n
0xbb000bbb | MUI resource cache builder has been called with the following parameters: %1.\r\n
0xbb000bbc | MUI resource cache manifest entry for file %1 has been updated. Affinity: '%2', Sequence: %3, and Priority: %4\r\n
0xbb000bbd | Start: %1\r\n
0xbb000bbe | End: %1\r\n
0xbb000bbf | New resource cache built and installed on system. New cache index is %1, live cache index is %2 and config is set to %3.\r\n
0xbb000bc4 | Resource file %1 will not be cached since it is not used frequently in the system.\r\n
0xbb000bc5 | The system is constrained in RAM, total disk space or free disk space, so the MUI resource cache will not be maintained.\r\n
0xbb000fa0 | Unable to parse configuration parameters. The configuration parameters will be ignored.\r\n
0xbc00000b | The time elapsed before Bootmgr, based on the TSC, is %1 ms.\r\n
0xbc00001f | Initialization of the firmware crypto hash provider resulted in status %1.\r\n
0xbc000021 | The firmware update capsule (%1) failed to load with status %2.\r\n
0xbc000022 | The PE/COFF image firmware update capsule (%1) failed to load with status %2.\r\n
0xbc000023 | The Efi UpdateCapsule failed to apply updates with status %1.\r\n
0xbc000024 | Firmware update supported status is %3. The BitLocker device flags are %1 and the PCR bitmap is %2.\r\n
0xbc000025 | The firmware update capsule (%1) code integrity check failed with status %2.\r\n
0xbe010003 | %3 shim(s) were applied to driver [%1].%n%nShim(s) source: %2.%n%nShim GUID(s): %4.\r\n
0xbe010004 | Flags [%4] were applied to device [%1] - class [%2].%n%nFlags source: %3.\r\n
0xbf000001 | Process %1 started at time %2 by parent %3 running as package %4 with executable %5 is application %6.\r\n
0xbf000002 | %2: Cannot create the process for package %1 because an error was encountered. %3\r\n
0xbf000003 | %2: Cannot create the process for package %1 because an error was encountered while querying the fast cache. %3\r\n
0xbf000004 | %2: Cannot create the process for package %1 because an error was encountered while preparing the App credentials. %3\r\n
0xbf000005 | %2: Cannot create the process for package %1 because an error was encountered while checking the user state. %3\r\n
0xbf000006 | %2: Cannot create the process for package %1 because an error was encountered while checking the machine state. %3\r\n
0xbf000007 | %2: Cannot create the process for package %1 because an error was encountered while verifying the App credentials. %3\r\n
0xbf000008 | App %1 was terminated with error %2 because of an issue with application binary %3. This could be because the binary is unsigned, contains an untrusted signature, or has been corrupted or tampered with. Reinstall the application to fix this issue.\r\n
0xbf00000b | App %1 prevented the load of generated binary %3 due to error %2. This could be because the binary is unsigned, contains an untrusted signature, or has been corrupted or tampered with.\r\n
0xbf00000c | An app prevented the load of a binary due to error %1. This could be because the binary is unsigned, contains an untrusted signature, or has been corrupted or tampered with.\r\n
0xbf00000e | %2: Package runtime information %1 is corrupted (address=%5, size=%3, offset=%4, section=%6, processid=%7). Reinstall the package to fix this issue.\r\n
0xbf00000f | %2: Package runtime information %1 is missing expected data (address=%4, size=%3, section=%5, processid=%6). Reinstall the package to fix this issue.\r\n
0xbf000010 | %2: Package runtime information %1 contains conflicting data (address=%5, size=%3, offset=%4, section=%6, processid=%7). Reinstall the package to fix this issue.\r\n
0xbf000011 | %2: Package runtime information %1 contains unexpected data (address=%5, size=%3, offset=%4, section=%6, processid=%7). Reinstall the package to fix this issue.\r\n
0xbf000012 | %2: Package runtime information %1 failed to load (processid=%3).\r\n
0xbf000013 | Package runtime information %1 failed to load because exception %2 occurred.\r\n
0xbf000014 | %2: Cannot create the process for package %1 because an error was encountered while loading the runtime information. %3\r\n
0xbf000015 | CreateAppContainerProfile failed for AppContainer %2 with error %1.\r\n
0xbf000016 | DeleteAppContainerProfile failed for AppContainer %2 with error %1.\r\n
0xbf000017 | UpdateAppContainerProfile failed for AppContainer %2 with error %1.\r\n
0xbf000018 | CreateAppContainerProfile failed with error %1 because it was unable to create registry key %2.\r\n
0xbf000019 | CreateAppContainerProfile failed with error %1 because it was unable to set security on registry key %2.\r\n
0xbf00001a | AppContainer profile failed with error %1 because it was unable to delete registry key %2.\r\n
0xbf00001b | CreateAppContainerProfile failed with error %1 because it was unable to create folder %2.\r\n
0xbf00001c | CreateAppContainerProfile failed with error %1 because it was unable to set attributes on folder %2.\r\n
0xbf00001d | CreateAppContainerProfile failed with error %1 because it was unable to verify the existence of registry key %2.\r\n
0xbf00001e | CreateAppContainerProfile failed with error %1 because it was unable to verify the existence of folder %2.\r\n
0xbf00001f | CreateAppContainerProfile failed with error %1 because it was unable to find the users local app data folder.\r\n
0xbf000020 | AppContainer profile failed with error %1 because it was unable to delete folder %2 or its contents.\r\n
0xbf000021 | AppContainer profile failed with error %1 because it was unable to look up the AppContainer name.\r\n
0xbf000022 | AppContainer profile failed with error %1 because it was unable to look up the AppContainer display name.\r\n
0xbf000023 | CreateAppContainerProfile failed with error %1 because it was unable to register with the firewall.\r\n
0xbf000024 | DeleteAppContainerProfile failed with error %1 because it was unable to unregister with the firewall.\r\n
0xbf000025 | App Container profile failed with error %1 because it was unable to register the AppContainer SID.\r\n
0xbf000026 | DeleteAppContainerProfile failed with error %1 because it was unable to unregister the AppContainer SID.\r\n
0xbf000027 | Successfully created AppContainer %1.\r\n
0xbf000028 | AppContainer %1 was not created because it already exists.\r\n
0xbf000029 | Successfully deleted AppContainer %1.\r\n
0xbf00002a | Successfully updated AppContainer %1.\r\n
0xd1000001 | System time initialized during boot\r\n
0xd1000002 | An application or system component changed the time\r\n
0xd1000003 | System time synchronized with the hardware clock\r\n
0xd1000004 | System time adjusted to the new time zone\r\n
0xd4000001 | on\r\n
0xd4000002 | off\r\n
0xd4000003 | started\r\n
0xd4000004 | finished\r\n
0xde000001 | applied through registry\r\n
0xde000002 | applied through compatibility database\r\n
0xde000003 | applied through registry\r\n
0xde000004 | applied through compatibility database\r\n
0xf2000001 | PackageId\r\n
