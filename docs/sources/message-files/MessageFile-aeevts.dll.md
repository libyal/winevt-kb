## aeevts.dll

Path: %SystemRoot%\system32\aeevts.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x000000c8 | The Program Compatibility Assistant service was stopped successfully.\r\n
0x000000c9 | The Program Compatibility Assistant service started successfully.\r\n
0x000000ca | The Program Compatibility Assistant service failed to initialize.\r\n
0x000000cb | The Program Compatibility Assistant service failed to start.\r\n
0x000000cc | The Program Compatibility Assistant service failed to stop.\r\n
0x000000cd | The Program Compatibility Assistant service failed to perform the phase two initialization.\r\n
0x000000ce | The Program Compatibility Assistant service successfully performed phase two initialization.\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Application-Experience\r\n
0x90000002 | System\r\n
0x90000003 | Application\r\n
0x90000004 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant\r\n
0x90000005 | Microsoft-Windows-Application-Experience/Program-Telemetry\r\n
0x90000006 | Microsoft-Windows-Application-Experience/Program-Inventory\r\n
0x90000007 | Microsoft-Windows-Application-Experience/Problem-Steps-Recorder\r\n
0x90000008 | Microsoft-Windows-Application-Experience/Program-Compatibility-Troubleshooter\r\n
0x90000009 | Microsoft-Windows-Application-Experience/Program-Inventory/Debug\r\n
0xb0000064 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nUser action ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n
0xb0000065 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nUser action ID: %6%nCompatibility layer: %7%nDeprecated component: %8%nFileID: %9%nProgramID: %10\r\n
0xb0000066 | The Program Compatibility Assistant was invoked due to an unsigned driver install. This version of Windows requires all drivers to have a valid digital signature. Information about the driver is below.%n%nDriver: %1%nService: %2%nPublisher: %3%nLocation: %4%nVersion: %5%n%nThis driver is unavailable and the program that uses this driver might not work correctly.\r\n
0xb0000067 | The Program Compatibility Assistant was not invoked because the application has been already handled previously. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb0000068 | The Program Compatibility Assistant was not invoked as the application executed correctly. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb00000cf | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is excluded in the registry.\r\n
0xb00000d0 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because of the extension of the executable.\r\n
0xb00000d1 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a UAC manifest.\r\n
0xb00000d2 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has a compatibility fix applied to it.\r\n
0xb00000d3 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application depends on the Windows Installer service (MSI).\r\n
0xb00000d4 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a current SwitchBack context.\r\n
0xb000012c | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the PCA is disabled by group policy.\r\n
0xb000012d | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application already exists within a job object.\r\n
0xb000012e | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is a 64-bit application.\r\n
0xb000012f | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is on a network path.\r\n
0xb0000130 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application compatibility infrastructure is disabled.\r\n
0xb0000131 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is protected by Windows Resource Protection.\r\n
0xb0000132 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has been excluded from the PCA by Microsoft.\r\n
0xb0000190 | The Program Compatibility Assistant attempted to connect an event for process ID %1, but the Program Compatibility Assistant service was unable to locate the process.\r\n
0xb00001f4 | Compatibility fix applied to %5.%nFix information: %6, %3, %4.\r\n
0xb00001f6 | Compatibility fix applied to %7.%nFix information: %8, %3, %4.\r\n
0xb0000258 | An instance of the Problem Steps Recorder ran with the following information:%n%nStartTime: %1%nStopTime: %2%nAction Count: %3%nMissed Action Count: %4%nOutput file location: %5\r\n
0xb0000259 | An instance of the Problem Steps Recorder terminated with the following error code: %1\r\n
0xb00002bc | The Application Impact Telemetry (AIT) Agent terminated with the following error code: %1\r\n
0xb00002bd | The Application Impact Telemetry (AIT) Agent is not running because AIT is disabled.\r\n
0xb00002be | The Application Impact Telemetry (AIT) Agent is stopping because another instance is already running.\r\n
0xb00002bf | The Application Impact Telemetry (AIT) Agent was unable to parse the command-line options with error code: %1.\r\n
0xb00002c0 | The Application Impact Telemetry (AIT) Agent was unable to process the logs files with error code: %1.\r\n
0xb00002c1 | The Application Impact Telemetry (AIT) Agent was unable to start application impact SQM with error code: %1.\r\n
0xb00002c2 | The Application Impact Telemetry (AIT) Agent was unable to log application impact data to SQM with error code: %1.\r\n
0xb00002c3 | The Application Impact Telemetry (AIT) Agent was unable to start system telemetry with error code: %1.\r\n
0xb00002c4 | The Application Impact Telemetry (AIT) Agent was unable to log system telemetry data to SQM with error code: %1.\r\n
0xb0000320 | An instance of Program Data Updater (PDU) ran with the following information: StartTime: %1, StopTime: %2, ExitCode: %3, Number of new programs: %4, Number of removed programs: %5, Number of updated programs: %6, Number of installed programs: %7, Number of new orphan files: %8, Number of new add-ons: %9, Number of removed add-ons: %10, Number of updated add-ons: %11, Number of installed add-ons: %12, Number of new installations: %13\r\n
0xb0000384 | An Internet Explorer add-on was installed on the system. For details, please examine the event data.%n%nName: %1%nType: %2%nPublisher: %3%nCLSID: %4%n\r\n
0xb0000385 | An Internet Explorer add-on was updated on the system. For details, please examine the event data.%n%nName: %1%nType: %2%nPublisher: %3%nCLSID: %4%n\r\n
0xb0000386 | An Internet Explorer add-on was removed from the system. For details, please examine the event data.%n%nName: %1%nType: %2%nPublisher: %3%nCLSID: %4%n\r\n
0xb0000387 | A program was installed on the system. For details, please examine the event data.%n%nName: %1%nVersion: %2%nPublisher: %3%n\r\n
0xb0000389 | A program was updated on the system. For details, please examine the event data.%n%nName: %1%nVersion: %2%nPublisher: %3%n\r\n
0xb000038b | A program was removed from the system. For details, please examine the event data.%n%nName: %1%nVersion: %2%nPublisher: %3%n\r\n
0xb000038d | SysCache update failure.%n%nFile path: %1%nFile ID: %2%nProgram ID: %3%nError Code: %4%n\r\n
0xb0001389 | The Program Compatibility Troubleshooter was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nResult: %5%nResult ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Application-Experience\r\n
0x90000002 | Microsoft-Windows-Application-Experience/Compatibility-Infrastructure-Debug\r\n
0x90000003 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant/Analytic\r\n
0x90000004 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant/Trace\r\n
0x90000005 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant\r\n
0x90000006 | Microsoft-Windows-Application-Experience/Program-Telemetry\r\n
0x90000007 | Microsoft-Windows-Application-Experience/Program-Inventory\r\n
0x90000008 | Microsoft-Windows-Application-Experience/Steps-Recorder\r\n
0x90000009 | Microsoft-Windows-Application-Experience/Program-Compatibility-Troubleshooter\r\n
0xb0000032 | PCA was requested to refresh the program cache.\r\n
0xb0000033 | PCA was informed that the program cache was refreshed.\r\n
0xb000003c | PCA dialog button response %2.\r\n
0xb0000064 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nUser action ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n
0xb0000067 | The Program Compatibility Assistant was not invoked because the application has been already handled previously. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb0000068 | The Program Compatibility Assistant was not invoked as the application executed correctly. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb0000069 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenarios code: %4%nDeprecated Components: %5%nUser action ID: %6%nCompatibility layers recommended: %7%nFileID: %8%nProgramID: %9\r\n
0xb00000cf | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is excluded in the registry.\r\n
0xb00000d0 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because of the extension of the executable.\r\n
0xb00000d1 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a UAC manifest.\r\n
0xb00000d2 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has a compatibility fix applied to it.\r\n
0xb00000d3 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application depends on the Windows Installer service (MSI).\r\n
0xb00000d4 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a current SwitchBack context.\r\n
0xb00000d5 | The Program Compatibility Assistant has added %1 to quarantine.\r\n
0xb00000d6 | The Program Compatibility Assistant has removed %1 from quarantine.\r\n
0xb00000d7 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a UAC manifest.\r\n
0xb000012c | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the PCA is disabled by group policy.\r\n
0xb000012d | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application already exists within a job object.\r\n
0xb000012e | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is a 64-bit application.\r\n
0xb000012f | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is on a network path.\r\n
0xb0000130 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application compatibility infrastructure is disabled.\r\n
0xb0000131 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is protected by Windows Resource Protection.\r\n
0xb0000132 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has been excluded from the PCA by Microsoft.\r\n
0xb0000190 | The Program Compatibility Assistant attempted to connect an event for process ID %1, but the Program Compatibility Assistant service was unable to locate the process.\r\n
0xb00001f4 | Compatibility fix applied to %5.%nFix information: %6, %3, %4.\r\n
0xb00001f6 | Compatibility fix applied to %7.%nFix information: %8, %3, %4.\r\n
0xb00001f8 | PCA was informed about fix %2 applied to process.\r\n
0xb0000258 | An instance of the Steps Recorder ran with the following information:%n%nStartTime: %1%nStopTime: %2%nAction Count: %3%nMissed Action Count: %4%nOutput file location: %5\r\n
0xb0000259 | An instance of the Steps Recorder terminated with the following error code: %1\r\n
0xb00002bc | The Application Impact Telemetry (AIT) Agent terminated with the following error code: %1\r\n
0xb00002bd | The Application Impact Telemetry (AIT) Agent is not running because AIT is disabled.\r\n
0xb00002be | The Application Impact Telemetry (AIT) Agent is stopping because another instance is already running.\r\n
0xb00002bf | The Application Impact Telemetry (AIT) Agent was unable to parse the command-line options with error code: %1.\r\n
0xb00002c0 | The Application Impact Telemetry (AIT) Agent was unable to process the logs files with error code: %1.\r\n
0xb00002c1 | The Application Impact Telemetry (AIT) Agent was unable to start application impact SQM with error code: %1.\r\n
0xb00002c2 | The Application Impact Telemetry (AIT) Agent was unable to log application impact data to SQM with error code: %1.\r\n
0xb00002c3 | The Application Impact Telemetry (AIT) Agent was unable to start system telemetry with error code: %1.\r\n
0xb00002c4 | The Application Impact Telemetry (AIT) Agent was unable to log system telemetry data to SQM with error code: %1.\r\n
0xb0000320 | An instance of Program Data Updater (PDU) ran with the following information: StartTime: %1, StopTime: %2, ExitCode: %3, Number of new programs: %4, Number of removed programs: %5, Number of updated programs: %6, Number of installed programs: %7, Number of new orphan files: %8, Number of new add-ons: %9, Number of removed add-ons: %10, Number of updated add-ons: %11, Number of installed add-ons: %12, Number of new installations: %13\r\n
0xb000038d | AMI cache update failure.%n%nFile path: %1%nFile ID: %2%nProgram ID: %3%nError Code: %4%n\r\n
0xb00003eb | Installer cancel click detected.\r\n
0xb00003ec | InstallerShield detected.\r\n
0xb00003ed | File installed.\r\n
0xb00003ee | New arp key.\r\n
0xb000044c | DirectX detection: HighDPIAware.\r\n
0xb000044d | DirectX detection: MaximizedWindowedMode.\r\n
0xb00007d1 | The Application Impact Telemetry (AIT) Static Analysis tool ran with the following results:%n%nStart time: %7%nStop time: %8%nRuntime: %9%nExit code: %3%nType of analysis: %4%nNumber of files analyzed: %5%nNumber of files failed: %6%nAnalysis command: %10%nProgram ID: %11\r\n
0xb00007d2 | %1\r\n
0xb0001389 | The Program Compatibility Troubleshooter was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nResult: %5%nResult ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n
0xb0001f40 | Detector shim: SHORT_RUN_TIME.\r\n
0xb0001f41 | Detector shim: ACCESS_DENIED.\r\n
0xb0001f42 | Detector shim: BLACK_SCREEN.\r\n
0xb0001f43 | Detector shim: WIN32_EXCEPTION: %3.\r\n
0xb0001f44 | Detector shim: GLOBAL_OBJECT.\r\n
0xb0001f45 | Detector shim: PRIVILEGE_CHECK.\r\n
0xb0001f46 | Detector shim: MESSAGE_BOX_VERSION.\r\n
0xb0001f47 | Detector shim: MESSAGE_BOX_PRIVILEGE.\r\n
0xb0001f48 | Detector shim: MESSAGE_BOX_ERROR_ICON.\r\n
0xb0001f4a | Detector shim: REG_EXPAND_SZ.\r\n
0xb0001f4b | Detector shim: DWM_8AND16_MODE.\r\n
0xb0007ffd | Chain: %1, Process: %2, Type: %3%nComponent: %4%nMessage: %5\r\n
0xb0007ffe | Message: %1\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Application-Experience\r\n
0x90000002 | Microsoft-Windows-Application-Experience/Compatibility-Infrastructure-Debug\r\n
0x90000003 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant/Analytic\r\n
0x90000004 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant/Trace\r\n
0x90000005 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant\r\n
0x90000006 | Microsoft-Windows-Application-Experience/Program-Telemetry\r\n
0x90000007 | Microsoft-Windows-Application-Experience/Program-Inventory\r\n
0x90000008 | Microsoft-Windows-Application-Experience/Steps-Recorder\r\n
0x90000009 | Microsoft-Windows-Application-Experience/Program-Compatibility-Troubleshooter\r\n
0xb0000032 | PCA was requested to refresh the program cache.\r\n
0xb0000033 | PCA was informed that the program cache was refreshed.\r\n
0xb000003c | PCA dialog button response %2.\r\n
0xb0000064 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nUser action ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n
0xb0000067 | The Program Compatibility Assistant was not invoked because the application has been already handled previously. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb0000068 | The Program Compatibility Assistant was not invoked as the application executed correctly. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb0000069 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenarios code: %4%nDeprecated Components: %5%nUser action ID: %6%nCompatibility layers recommended: %7%nFileID: %8%nProgramID: %9\r\n
0xb00000cf | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is excluded in the registry.\r\n
0xb00000d0 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because of the extension of the executable.\r\n
0xb00000d1 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a UAC manifest.\r\n
0xb00000d2 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has a compatibility fix applied to it.\r\n
0xb00000d3 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application depends on the Windows Installer service (MSI).\r\n
0xb00000d4 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a current SwitchBack context.\r\n
0xb00000d5 | The Program Compatibility Assistant has added %1 to quarantine.\r\n
0xb00000d6 | The Program Compatibility Assistant has removed %1 from quarantine.\r\n
0xb00000d7 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a UAC manifest.\r\n
0xb000012c | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the PCA is disabled by group policy.\r\n
0xb000012d | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application already exists within a job object.\r\n
0xb000012e | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is a 64-bit application.\r\n
0xb000012f | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is on a network path.\r\n
0xb0000130 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application compatibility infrastructure is disabled.\r\n
0xb0000131 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is protected by Windows Resource Protection.\r\n
0xb0000132 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has been excluded from the PCA by Microsoft.\r\n
0xb0000190 | The Program Compatibility Assistant attempted to connect an event for process ID %1, but the Program Compatibility Assistant service was unable to locate the process.\r\n
0xb00001f4 | Compatibility fix applied to %5.%nFix information: %6, %3, %4.\r\n
0xb00001f6 | Compatibility fix applied to %7.%nFix information: %8, %3, %4.\r\n
0xb00001f8 | PCA was informed about fix %2 applied to process.\r\n
0xb0000258 | An instance of the Steps Recorder ran with the following information:%n%nStartTime: %1%nStopTime: %2%nAction Count: %3%nMissed Action Count: %4%nOutput file location: %5\r\n
0xb0000259 | An instance of the Steps Recorder terminated with the following error code: %1\r\n
0xb00002bc | The Application Impact Telemetry (AIT) Agent terminated with the following error code: %1\r\n
0xb00002bd | The Application Impact Telemetry (AIT) Agent is not running because AIT is disabled.\r\n
0xb00002be | The Application Impact Telemetry (AIT) Agent is stopping because another instance is already running.\r\n
0xb00002bf | The Application Impact Telemetry (AIT) Agent was unable to parse the command-line options with error code: %1.\r\n
0xb00002c0 | The Application Impact Telemetry (AIT) Agent was unable to process the logs files with error code: %1.\r\n
0xb00002c1 | The Application Impact Telemetry (AIT) Agent was unable to start application impact SQM with error code: %1.\r\n
0xb00002c2 | The Application Impact Telemetry (AIT) Agent was unable to log application impact data to SQM with error code: %1.\r\n
0xb00002c3 | The Application Impact Telemetry (AIT) Agent was unable to start system telemetry with error code: %1.\r\n
0xb00002c4 | The Application Impact Telemetry (AIT) Agent was unable to log system telemetry data to SQM with error code: %1.\r\n
0xb0000320 | An instance of Program Data Updater (PDU) ran with the following information: StartTime: %1, StopTime: %2, ExitCode: %3, Number of new programs: %4, Number of removed programs: %5, Number of updated programs: %6, Number of installed programs: %7, Number of new orphan files: %8, Number of new add-ons: %9, Number of removed add-ons: %10, Number of updated add-ons: %11, Number of installed add-ons: %12, Number of new installations: %13\r\n
0xb000038d | AMI cache update failure.%n%nFile path: %1%nFile ID: %2%nProgram ID: %3%nError Code: %4%n\r\n
0xb00003eb | Installer cancel click detected.\r\n
0xb00003ec | InstallerShield detected.\r\n
0xb00003ed | File installed.\r\n
0xb00003ee | New arp key.\r\n
0xb000044c | DirectX detection: HighDPIAware.\r\n
0xb000044d | DirectX detection: MaximizedWindowedMode.\r\n
0xb00007d1 | The Application Impact Telemetry (AIT) Static Analysis tool ran with the following results:%n%nStart time: %7%nStop time: %8%nRuntime: %9%nExit code: %3%nType of analysis: %4%nNumber of files analyzed: %5%nNumber of files failed: %6%nAnalysis command: %10%nProgram ID: %11\r\n
0xb00007d2 | %1\r\n
0xb00007d5 | %3\r\n
0xb0001389 | The Program Compatibility Troubleshooter was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nResult: %5%nResult ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n
0xb000138a | The Program Compatibility Troubleshooter queried the Compatibility Online Service for information about an application. Results are below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nRecommended layer: %4%nURL: %5%nCompatibility status: %6%nFileID: %7%nProgramID: %8\r\n
0xb000138b | The Program Compatibility Troubleshooter queried the application genome for information about an application. Results are below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nRecommended layer: %4%nVista+: %5%nFileID: %6%nProgramID: %7\r\n
0xb000138c | Program Compatibility Troubleshooter debug event:%n%1%n%2\r\n
0xb0001f40 | Detector shim: SHORT_RUN_TIME.\r\n
0xb0001f41 | Detector shim: ACCESS_DENIED.\r\n
0xb0001f42 | Detector shim: BLACK_SCREEN.\r\n
0xb0001f43 | Detector shim: WIN32_EXCEPTION: %3.\r\n
0xb0001f44 | Detector shim: GLOBAL_OBJECT.\r\n
0xb0001f45 | Detector shim: PRIVILEGE_CHECK.\r\n
0xb0001f46 | Detector shim: MESSAGE_BOX_VERSION.\r\n
0xb0001f47 | Detector shim: MESSAGE_BOX_PRIVILEGE.\r\n
0xb0001f48 | Detector shim: MESSAGE_BOX_ERROR_ICON.\r\n
0xb0001f4a | Detector shim: REG_EXPAND_SZ.\r\n
0xb0001f4b | Detector shim: DWM_8AND16_MODE.\r\n
0xb0007ffd | Chain: %1, Process: %2, Type: %3%nComponent: %4%nMessage: %5\r\n
0xb0007ffe | Message: %1\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Application-Experience\r\n
0x90000002 | Microsoft-Windows-Application-Experience/Compatibility-Infrastructure-Debug\r\n
0x90000003 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant/Analytic\r\n
0x90000004 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant/Trace\r\n
0x90000005 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant\r\n
0x90000006 | Microsoft-Windows-Application-Experience/Program-Telemetry\r\n
0x90000007 | Microsoft-Windows-Application-Experience/Program-Inventory\r\n
0x90000008 | Microsoft-Windows-Application-Experience/Steps-Recorder\r\n
0x90000009 | Microsoft-Windows-Application-Experience/Program-Compatibility-Troubleshooter\r\n
0xb0000032 | PCA was requested to refresh the program cache.\r\n
0xb0000033 | PCA was informed that the program cache was refreshed.\r\n
0xb000003c | PCA dialog button response %2.\r\n
0xb0000046 | PCA triggered SIUF question was asked.\r\n
0xb0000051 | PCA triggered SIUF question was answered.\r\n
0xb0000064 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nUser action ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n
0xb0000067 | The Program Compatibility Assistant was not invoked because the application has been already handled previously. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb0000068 | The Program Compatibility Assistant was not invoked as the application executed correctly. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb0000069 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenarios code: %4%nDeprecated Components: %5%nUser action ID: %6%nCompatibility layers recommended: %7%nFileID: %8%nProgramID: %9\r\n
0xb00000cf | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is excluded in the registry.\r\n
0xb00000d0 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because of the extension of the executable.\r\n
0xb00000d1 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a UAC manifest.\r\n
0xb00000d2 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has a compatibility fix applied to it.\r\n
0xb00000d3 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application depends on the Windows Installer service (MSI).\r\n
0xb00000d4 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a current SwitchBack context.\r\n
0xb00000d5 | The Program Compatibility Assistant has added %1 to quarantine.\r\n
0xb00000d6 | The Program Compatibility Assistant has removed %1 from quarantine.\r\n
0xb00000d7 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a UAC manifest.\r\n
0xb000012c | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the PCA is disabled by group policy.\r\n
0xb000012d | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application already exists within a job object.\r\n
0xb000012e | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is a 64-bit application.\r\n
0xb000012f | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is on a network path.\r\n
0xb0000130 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application compatibility infrastructure is disabled.\r\n
0xb0000131 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is protected by Windows Resource Protection.\r\n
0xb0000132 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has been excluded from the PCA by Microsoft.\r\n
0xb0000190 | The Program Compatibility Assistant attempted to connect an event for process ID %1, but the Program Compatibility Assistant service was unable to locate the process.\r\n
0xb00001f4 | Compatibility fix applied to %5.%nFix information: %6, %3, %4.\r\n
0xb00001f6 | Compatibility fix applied to %7.%nFix information: %8, %3, %4.\r\n
0xb00001f8 | PCA was informed about fix %2 applied to process.\r\n
0xb0000258 | An instance of the Steps Recorder ran with the following information:%n%nStartTime: %1%nStopTime: %2%nAction Count: %3%nMissed Action Count: %4%nOutput file location: %5\r\n
0xb0000259 | An instance of the Steps Recorder terminated with the following error code: %1\r\n
0xb00002bc | The Application Impact Telemetry (AIT) Agent terminated with the following error code: %1\r\n
0xb00002bd | The Application Impact Telemetry (AIT) Agent is not running because AIT is disabled.\r\n
0xb00002be | The Application Impact Telemetry (AIT) Agent is stopping because another instance is already running.\r\n
0xb00002bf | The Application Impact Telemetry (AIT) Agent was unable to parse the command-line options with error code: %1.\r\n
0xb00002c0 | The Application Impact Telemetry (AIT) Agent was unable to process the logs files with error code: %1.\r\n
0xb00002c1 | The Application Impact Telemetry (AIT) Agent was unable to start application impact SQM with error code: %1.\r\n
0xb00002c2 | The Application Impact Telemetry (AIT) Agent was unable to log application impact data to SQM with error code: %1.\r\n
0xb00002c3 | The Application Impact Telemetry (AIT) Agent was unable to start system telemetry with error code: %1.\r\n
0xb00002c4 | The Application Impact Telemetry (AIT) Agent was unable to log system telemetry data to SQM with error code: %1.\r\n
0xb00003eb | Installer cancel click detected.\r\n
0xb00003ec | InstallerShield detected.\r\n
0xb00003ed | File installed.\r\n
0xb00003ee | New arp key.\r\n
0xb000044c | DirectX detection: HighDPIAware.\r\n
0xb000044d | DirectX detection: MaximizedWindowedMode.\r\n
0xb00007d1 | The Application Impact Telemetry (AIT) Static Analysis tool ran with the following results:%n%nStart time: %7%nStop time: %8%nRuntime: %9%nExit code: %3%nType of analysis: %4%nNumber of files analyzed: %5%nNumber of files failed: %6%nAnalysis command: %10%nProgram ID: %11\r\n
0xb00007d2 | %1\r\n
0xb00007d5 | %3\r\n
0xb0001389 | The Program Compatibility Troubleshooter was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nResult: %5%nResult ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n
0xb000138a | The Program Compatibility Troubleshooter queried the Compatibility Online Service for information about an application. Results are below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nRecommended layer: %4%nURL: %5%nCompatibility status: %6%nFileID: %7%nProgramID: %8\r\n
0xb000138b | The Program Compatibility Troubleshooter queried the application genome for information about an application. Results are below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nRecommended layer: %4%nVista+: %5%nFileID: %6%nProgramID: %7\r\n
0xb000138c | Program Compatibility Troubleshooter debug event:%n%1%n%2\r\n
0xb0001f40 | Detector shim: SHORT_RUN_TIME.\r\n
0xb0001f41 | Detector shim: ACCESS_DENIED.\r\n
0xb0001f42 | Detector shim: BLACK_SCREEN.\r\n
0xb0001f43 | Detector shim: WIN32_EXCEPTION: %3.\r\n
0xb0001f44 | Detector shim: GLOBAL_OBJECT.\r\n
0xb0001f45 | Detector shim: PRIVILEGE_CHECK.\r\n
0xb0001f46 | Detector shim: MESSAGE_BOX_VERSION.\r\n
0xb0001f47 | Detector shim: MESSAGE_BOX_PRIVILEGE.\r\n
0xb0001f48 | Detector shim: MESSAGE_BOX_ERROR_ICON.\r\n
0xb0001f4a | Detector shim: REG_EXPAND_SZ.\r\n
0xb0001f4b | Detector shim: DWM_8AND16_MODE.\r\n
0xb0007ffd | Chain: %1, Process: %2, Type: %3%nComponent: %4%nMessage: %5\r\n
0xb0007ffe | Message: %1\r\n

### 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Application-Experience\r\n
0x90000002 | Microsoft-Windows-Application-Experience/Compatibility-Infrastructure-Debug\r\n
0x90000003 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant/Analytic\r\n
0x90000004 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant/Trace\r\n
0x90000005 | Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant\r\n
0x90000006 | Microsoft-Windows-Application-Experience/Program-Telemetry\r\n
0x90000007 | Microsoft-Windows-Application-Experience/Program-Inventory\r\n
0x90000008 | Microsoft-Windows-Application-Experience/Steps-Recorder\r\n
0x90000009 | Microsoft-Windows-Application-Experience/Program-Compatibility-Troubleshooter\r\n
0xb0000032 | PCA was requested to refresh the program cache.\r\n
0xb0000033 | PCA was informed that the program cache was refreshed.\r\n
0xb000003c | PCA dialog button response %2.\r\n
0xb0000046 | PCA triggered SIUF question was asked.\r\n
0xb0000051 | PCA triggered SIUF question was answered.\r\n
0xb0000064 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nUser action ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n
0xb0000067 | The Program Compatibility Assistant was not invoked because the application has been already handled previously. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb0000068 | The Program Compatibility Assistant was not invoked as the application executed correctly. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nUser action: %5%nCompatibility layer: %6\r\n
0xb0000069 | The Program Compatibility Assistant was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenarios code: %4%nDeprecated Components: %5%nUser action ID: %6%nCompatibility layers recommended: %7%nFileID: %8%nProgramID: %9\r\n
0xb00000cf | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is excluded in the registry.\r\n
0xb00000d0 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because of the extension of the executable.\r\n
0xb00000d1 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a UAC manifest.\r\n
0xb00000d2 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has a compatibility fix applied to it.\r\n
0xb00000d3 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application depends on the Windows Installer service (MSI).\r\n
0xb00000d4 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a current SwitchBack context.\r\n
0xb00000d5 | The Program Compatibility Assistant has added %1 to quarantine.\r\n
0xb00000d6 | The Program Compatibility Assistant has removed %1 from quarantine.\r\n
0xb00000d7 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the executable has a UAC manifest.\r\n
0xb000012c | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the PCA is disabled by group policy.\r\n
0xb000012d | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application already exists within a job object.\r\n
0xb000012e | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is a 64-bit application.\r\n
0xb000012f | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is on a network path.\r\n
0xb0000130 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application compatibility infrastructure is disabled.\r\n
0xb0000131 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application is protected by Windows Resource Protection.\r\n
0xb0000132 | The Program Compatibility Assistant was requested to monitor %1, but ignored the request because the application has been excluded from the PCA by Microsoft.\r\n
0xb0000190 | The Program Compatibility Assistant attempted to connect an event for process ID %1, but the Program Compatibility Assistant service was unable to locate the process.\r\n
0xb00001f4 | Compatibility fix applied to %5.%nFix information: %6, %3, %4.\r\n
0xb00001f6 | Compatibility fix applied to %7.%nFix information: %8, %3, %4.\r\n
0xb00001f8 | PCA was informed about fix %2 applied to process.\r\n
0xb0000258 | An instance of the Steps Recorder ran with the following information:%n%nStartTime: %1%nStopTime: %2%nAction Count: %3%nMissed Action Count: %4%nOutput file location: %5\r\n
0xb0000259 | An instance of the Steps Recorder terminated with the following error code: %1\r\n
0xb00002bc | The Application Impact Telemetry (AIT) Agent terminated with the following error code: %1\r\n
0xb00002bd | The Application Impact Telemetry (AIT) Agent is not running because AIT is disabled.\r\n
0xb00002be | The Application Impact Telemetry (AIT) Agent is stopping because another instance is already running.\r\n
0xb00002bf | The Application Impact Telemetry (AIT) Agent was unable to parse the command-line options with error code: %1.\r\n
0xb00002c0 | The Application Impact Telemetry (AIT) Agent was unable to process the logs files with error code: %1.\r\n
0xb00002c1 | The Application Impact Telemetry (AIT) Agent was unable to start application impact SQM with error code: %1.\r\n
0xb00002c2 | The Application Impact Telemetry (AIT) Agent was unable to log application impact data to SQM with error code: %1.\r\n
0xb00002c3 | The Application Impact Telemetry (AIT) Agent was unable to start system telemetry with error code: %1.\r\n
0xb00002c4 | The Application Impact Telemetry (AIT) Agent was unable to log system telemetry data to SQM with error code: %1.\r\n
0xb00003eb | Installer cancel click detected.\r\n
0xb00003ec | InstallerShield detected.\r\n
0xb00003ed | File installed.\r\n
0xb00003ee | New arp key.\r\n
0xb000044c | DirectX detection: HighDPIAware.\r\n
0xb000044d | DirectX detection: MaximizedWindowedMode.\r\n
0xb000044e | DirectX detection: AdaptWindowToDisplayMode.\r\n
0xb00007d1 | The Application Impact Telemetry (AIT) Static Analysis tool ran with the following results:%n%nStart time: %7%nStop time: %8%nRuntime: %9%nExit code: %3%nType of analysis: %4%nNumber of files analyzed: %5%nNumber of files failed: %6%nAnalysis command: %10%nProgram ID: %11\r\n
0xb00007d2 | %1\r\n
0xb00007d5 | %3\r\n
0xb0001389 | The Program Compatibility Troubleshooter was invoked to correct a compatibility problem. Information about the application is below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nScenario ID: %4%nResult: %5%nResult ID: %6%nCompatibility layer: %7%nFileID: %8%nProgramID: %9\r\n
0xb000138a | The Program Compatibility Troubleshooter queried the Compatibility Online Service for information about an application. Results are below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nRecommended layer: %4%nURL: %5%nCompatibility status: %6%nFileID: %7%nProgramID: %8\r\n
0xb000138b | The Program Compatibility Troubleshooter queried the application genome for information about an application. Results are below.%n%nApplication name: %1%nApplication version: %2%nExecutable path: %3%nRecommended layer: %4%nVista+: %5%nFileID: %6%nProgramID: %7\r\n
0xb000138c | Program Compatibility Troubleshooter debug event:%n%1%n%2\r\n
0xb0001f40 | Detector shim: SHORT_RUN_TIME.\r\n
0xb0001f41 | Detector shim: ACCESS_DENIED.\r\n
0xb0001f42 | Detector shim: BLACK_SCREEN.\r\n
0xb0001f43 | Detector shim: WIN32_EXCEPTION: %3.\r\n
0xb0001f44 | Detector shim: GLOBAL_OBJECT.\r\n
0xb0001f45 | Detector shim: PRIVILEGE_CHECK.\r\n
0xb0001f46 | Detector shim: MESSAGE_BOX_VERSION.\r\n
0xb0001f47 | Detector shim: MESSAGE_BOX_PRIVILEGE.\r\n
0xb0001f48 | Detector shim: MESSAGE_BOX_ERROR_ICON.\r\n
0xb0001f4a | Detector shim: REG_EXPAND_SZ.\r\n
0xb0001f4b | Detector shim: DWM_8AND16_MODE.\r\n
0xb0007ffd | Chain: %1, Process: %2, Type: %3%nComponent: %4%nMessage: %5\r\n
0xb0007ffe | Message: %1\r\n
