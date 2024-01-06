## dps.dll

Path: %SystemRoot%\system32\dps.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x1000000a | Memory tracing events\r\n
0x10000021 | Timing Events\r\n
0x10000022 | Scenario trigger events\r\n
0x10000023 | Debug events\r\n
0x10000024 | Scenario lifecycle events\r\n
0x10000025 | Diagnostic Module notification events\r\n
0x300a0000 | The Diagnostic Policy Service started\r\n
0x300b0000 | A diagnostic scenario was misconfigured\r\n
0x300c0000 | A diagnostic module detected a problem\r\n
0x300d0000 | A scenario instance was dispatched for troubleshooting\r\n
0x300e0000 | A diagnostic module completed troubleshooting without setting a resolution\r\n
0x300f0000 | A diagnostic module completed troubleshooting and set an immediate resolution\r\n
0x30100000 | A diagnostic module finished troubleshooting and set an queued resolution\r\n
0x30110000 | A scenario instance was dispatched for resolution\r\n
0x30120000 | A diagnostic module queued itself for later invocation\r\n
0x30130000 | A diagnostic module completed resolution\r\n
0x30140000 | The Diagnostic Policy Service was not able to instantiate a diagnostic module host\r\n
0x30150000 | This event is raised when a scenario fails\r\n
0x30160000 | A diagnostic module was moved to a broken state\r\n
0x30170000 | Debug event\r\n
0x30180000 | This event is raised at the ServiceMain for the service\r\n
0x30190000 | This event is raised when the DPS signals its status as RUNNING to the SCM\r\n
0x301a0000 | This event is raised when the service receives a shutdown/stop notification from the SCM\r\n
0x301b0000 | This event is raised when the service is successfully stopped\r\n
0x301c0000 | This event is raised when DPS refreshes group policy\r\n
0x70000001 | Scenario Lifecycle\r\n
0x70000002 | Debug task\r\n
0x70000003 | DPS Initialization\r\n
0x70000004 | Notification task\r\n
0x90000001 | Microsoft-Windows-Diagnosis-DPS\r\n
0x91000001 | Microsoft-Windows-Diagnosis-WDI\r\n
0xb0000001 | The Diagnostic Policy Service started.  This event signals diagnostic modules for delayed processing after the service is initialized.\r\n
0xb0000005 | The scenario %1 has a configuration error in the WDI registry namespace.  The Diagnostic Policy Service will ignore the scenario.\r\n
0xb0000064 | Diagnostic module %5 (%4) detected a problem for scenario %1, instance %2, original activity ID %3.\r\n
0xb0000069 | Diagnostic module %5 (%4) started troubleshooting scenario %1, instance %2, original activity ID %3.\r\n
0xb000006e | Diagnostic module %5 (%4) finished troubleshooting scenario %1, instance %2, original activity ID %3.  No resolution was set by the diagnostic module.\r\n
0xb0000073 | Diagnostic module %9 (%4) finished troubleshooting scenario %1, instance %2, original activity ID %3.  It set resolution %5 for user %6 in session %7 with expiration date %8.  The resolution will be started immediately.\r\n
0xb0000078 | Diagnostic module %9 (%4) finished troubleshooting scenario %1, instance %2, original activity ID %3.  It set resolution %5 for user %6 in session %7 with expiration date %8.  The resolution was queued to start later.\r\n
0xb000007d | Diagnostic module %5 (%4) started resolving scenario %1, instance %2, original activity ID %3.\r\n
0xb000007e | Diagnostic module %5 (%4) was queued to start later for scenario %1, instance %2, original activity ID %3.\r\n
0xb0000082 | Diagnostic module %5 (%4) finished resolving scenario %1, instance %2, original activity ID %3.\r\n
0xb0000087 | The Diagnostic Policy Service could not create a diagnostic module host instance for diagnostic module %6 (%5).  The error code was %4.  The scenario %1, instance %2, original activity ID %3 will be discarded.\r\n
0xb000008c | The Diagnostic Policy Service encountered an error in file %1, function %2, line %3: %4.\r\n
0xb0000091 | This event is raised when the SCM loads the service DLL\r\n
0xb0000096 | This event is raised when the service enters a SERVICE_RUNNING state\r\n
0xb000009b | This event is raised when the SCM signals the service to shut down.\r\n
0xb00000a0 | This event is raised when the service is successfully stopped\r\n
0xb00000a5 | The Diagnostic Policy Service encountered an error while handling scenario %1 with diagnostic module %6 (%5), instance %2, original activity ID %3. The error code was %4.\r\n
0xb00000aa | Diagnostic module %6 (%4) encountered an error while handling scenario %1, instance %2, original activity ID %3.  The error code was %5.\r\n
0xb00000af | Scenario %1, instance %2, original activity ID %3 was dropped by diagnostic module %6 (%4). The error code was %5.\r\n
0xb00000b4 | The Diagnostic Policy Service just refreshed the Group Policy. This event notifies the diagnostic modules about the Group Policy changes.\r\n
0xb00000b9 | Diagnostic module %2 (%1) was moved into a broken state. The error code was %3.\r\n
0xb0001398 | The Diagnostic Policy Service just made a heap allocation\r\n
0xb0001399 | The Diagnostic Policy Service just freed a previously made heap allocation\r\n
0xb1001398 | The Diagnostic Infrastructure just made a heap allocation\r\n
0xb1001399 | The Diagnostic Infrastructure just freed a previously made heap allocation\r\n

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x1000000a | Memory tracing events\r\n
0x10000021 | Timing Events\r\n
0x10000022 | Scenario trigger events\r\n
0x10000023 | Debug events\r\n
0x10000024 | Scenario lifecycle events\r\n
0x10000025 | Diagnostic Module notification events\r\n
0x3000000a | The Diagnostic Policy Service started\r\n
0x3000000b | A diagnostic scenario was misconfigured\r\n
0x3000000c | A diagnostic module detected a problem\r\n
0x3000000d | A scenario instance was dispatched for troubleshooting\r\n
0x3000000e | A diagnostic module completed troubleshooting without setting a resolution\r\n
0x3000000f | A diagnostic module completed troubleshooting and set an immediate resolution\r\n
0x30000010 | A diagnostic module finished troubleshooting and set an queued resolution\r\n
0x30000011 | A scenario instance was dispatched for resolution\r\n
0x30000012 | A diagnostic module queued itself for later invocation\r\n
0x30000013 | A diagnostic module completed resolution\r\n
0x30000014 | The Diagnostic Policy Service was not able to instantiate a diagnostic module host\r\n
0x30000015 | This event is raised when a scenario fails\r\n
0x30000016 | A diagnostic module was moved to a broken state\r\n
0x30000017 | Debug event\r\n
0x30000018 | This event is raised at the ServiceMain for the service\r\n
0x30000019 | This event is raised when the DPS signals its status as RUNNING to the SCM\r\n
0x3000001a | This event is raised when the service receives a shutdown/stop notification from the SCM\r\n
0x3000001b | This event is raised when the service is successfully stopped\r\n
0x3000001c | This event is raised when DPS refreshes group policy\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000001 | Scenario Lifecycle\r\n
0x70000002 | Debug task\r\n
0x70000003 | DPS Initialization\r\n
0x70000004 | Notification task\r\n
0x90000001 | Microsoft-Windows-Diagnosis-DPS\r\n
0x90000002 | Microsoft-Windows-Diagnosis-DPS/Debug\r\n
0x90000003 | Microsoft-Windows-Diagnosis-DPS/Operational\r\n
0x90000004 | Microsoft-Windows-Diagnosis-DPS/Analytic\r\n
0x91000001 | Microsoft-Windows-Diagnosis-WDI\r\n
0x91000002 | Microsoft-Windows-Diagnosis-WDI/Debug\r\n
0xb0000001 | The Diagnostic Policy Service started.  This event signals diagnostic modules for delayed processing after the service is initialized.\r\n
0xb0000002 | The Diagnostic Policy Service started.  This event signals diagnostic modules for immediate processing after the service is initialized.\r\n
0xb0000005 | The scenario %1 has a configuration error or has been explicitly disabled in the WDI registry namespace.  The Diagnostic Policy Service will ignore the scenario.\r\n
0xb0000064 | Diagnostic module %5 (%4) detected a problem for scenario %1, instance %2, original activity ID %3.\r\n
0xb0000069 | Diagnostic module %5 (%4) started troubleshooting scenario %1, instance %2, original activity ID %3.\r\n
0xb000006e | Diagnostic module %5 (%4) finished troubleshooting scenario %1, instance %2, original activity ID %3.  No resolution was set by the diagnostic module.\r\n
0xb0000073 | Diagnostic module %9 (%4) finished troubleshooting scenario %1, instance %2, original activity ID %3.  It set resolution %5 for user %6 in session %7 with expiration date %8.  The resolution will be started immediately.\r\n
0xb0000078 | Diagnostic module %9 (%4) finished troubleshooting scenario %1, instance %2, original activity ID %3.  It set resolution %5 for user %6 in session %7 with expiration date %8.  The resolution was queued to start later.\r\n
0xb000007d | Diagnostic module %5 (%4) started resolving scenario %1, instance %2, original activity ID %3.\r\n
0xb000007e | Diagnostic module %5 (%4) was queued to start later for scenario %1, instance %2, original activity ID %3.\r\n
0xb0000082 | Diagnostic module %5 (%4) finished resolving scenario %1, instance %2, original activity ID %3.\r\n
0xb0000087 | The Diagnostic Policy Service could not create a diagnostic module host instance for diagnostic module %6 (%5).  The error code was %4.  The scenario %1, instance %2, original activity ID %3 will be discarded.\r\n
0xb000008c | The Diagnostic Policy Service encountered an error in file %1, function %2, line %3: %4.\r\n
0xb0000091 | This event is raised when the SCM loads the service DLL\r\n
0xb0000096 | This event is raised when the service enters a SERVICE_RUNNING state\r\n
0xb000009b | This event is raised when the SCM signals the service to shut down.\r\n
0xb00000a0 | This event is raised when the service is successfully stopped\r\n
0xb00000a5 | The Diagnostic Policy Service encountered an error while handling scenario %1 with diagnostic module %6 (%5), instance %2, original activity ID %3. The error code was %4.\r\n
0xb00000aa | Diagnostic module %6 (%4) encountered an error while handling scenario %1, instance %2, original activity ID %3.  The error code was %5.\r\n
0xb00000af | Scenario %1, instance %2, original activity ID %3 was dropped by diagnostic module %6 (%4). The error code was %5.\r\n
0xb00000b4 | The Diagnostic Policy Service just refreshed the Group Policy. This event notifies the diagnostic modules about the Group Policy changes.\r\n
0xb00000b9 | Diagnostic module %2 (%1) was moved into a broken state. The error code was %3.\r\n
0xb0001398 | The Diagnostic Policy Service just made a heap allocation\r\n
0xb0001399 | The Diagnostic Policy Service just freed a previously made heap allocation\r\n
0xb1001398 | The Diagnostic Infrastructure just made a heap allocation\r\n
0xb1001399 | The Diagnostic Infrastructure just freed a previously made heap allocation\r\n
