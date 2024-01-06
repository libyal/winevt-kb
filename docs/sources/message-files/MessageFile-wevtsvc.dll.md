## wevtsvc.dll

Path: %SystemRoot%\System32\wevtsvc.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x10000012 | Service availability\r\n
0x10000013 | Service configuration\r\n
0x70000064 | Service startup\r\n
0x70000065 | Event processing\r\n
0x70000067 | Service shutdown\r\n
0x70000068 | Log clear\r\n
0x70000069 | Log automatic backup\r\n
0x90000001 | Microsoft-Windows-Eventlog\r\n
0x90000002 | Setup\r\n
0x90000003 | Debug\r\n
0x90000004 | Analytic\r\n
0xb0000014 | The event logging service encountered an error %1 while obtaining or processing configuration for channel %2.\r\n
0xb0000015 | The event logging service encountered a configuration-related error (res=%1) for channel %2. The error was encountered while processing the %3 configuration property.\r\n
0xb0000016 | The event logging service encountered an error while initializing publishing resources for channel %2. If channel type is Analytic or Debug, then this could mean there was an error initializing logging resources as well.\r\n
0xb0000017 | The event logging service encountered an error (res=%1) while initializing logging resources for channel %2.\r\n
0xb0000019 | The event logging service encountered a corrupt log file for channel %1. The log was renamed with a .corrupt extension.\r\n
0xb000001a | The event logging service encountered a log file for channel %1 which is an unsupported version. The log was renamed with a .UnsupportedVer extension.\r\n
0xb000001b | The event logging service encountered an error (res=%1) while opening log file for channel %2. Trying again using default log file path %3.\r\n
0xb000001c | The event logging service encountered an error (res=%1) while parsing filter for channel %2. Will continue without filter.\r\n
0xb000001d | The event logging service encountered a fatal error (res=%1) when applying settings to the %2 channel. The service is shutting down since this channel is vital to its operation.\r\n
0xb000001e | The event logging service encountered an error (%1) while enabling publisher %3 to channel %2. This doesn't affect operation of the channel, but does affect the ability for the publisher to raise events to the channel. One common reason for this error is that Provider is using ETW Provider Security and has not granted enable permissions to the Eventlog service identity.\r\n
0xb000001f | The event logging service encountered an error (res=%1) while opening configuration for primary channel %2. Trying again using default configuration. This problem usually occurs if registry has been corrupted or explicitly misconfigured.\r\n
0xb0000028 | The event logging service encountered an error when attempting to apply one or more policy settings.\r\n
0xb0000064 | The event logging service encountered an error while processing an incoming event published from %3.\r\n
0xb0000066 | The event logging service encountered an error while processing an incoming event from publisher %3 and trying to process the metadata for it.\r\n
0xb0000067 | Events have been dropped by the transport.  The session name is %2 and the reason code is %1.\r\n
0xb0000068 | The %3 log file was cleared.\r\n
0xb0000069 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0xb000006a | Corruption was detected in the log for the %1 channel and some data was erased.\r\n
0xb000044c | The event logging service has shut down.\r\n
0xb000044d | Audit events have been dropped by the transport.  %1\r\n
0xb000044e | The audit log was cleared.%nSubject:%n%tSecurity ID:%t%1%n%tAccount Name:%t%2%n%tDomain Name:%t%3%n%tLogon ID:%t%4\r\n
0xb000044f | The security log is now %1 percent full.\r\n
0xb0000450 | The security log is now full.\r\n
0xb0000452 | Events have been dropped by the event logging service. The reason code is %1.\r\n
0xb0001770 | The %1 log file is full.\r\n
0xd0000001 | Events were lost because there were no free buffers. Flushing to disk could not catch up with incoming events.\r\n
0xd0000002 | One or more buffers were dropped because a real time consumer could not catch up.\r\n
0xd0000003 | The real time backup file was corrupt due to improper shutdown.\r\n

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00000014 | The event logging service encountered an error %1 while obtaining or processing configuration for channel %2.\r\n
0x00000015 | The event logging service encountered a configuration-related error (res=%1) for channel %2. The error was encountered while processing the %3 configuration property.\r\n
0x00000016 | The event logging service encountered an error while initializing publishing resources for channel %2. If channel type is Analytic or Debug, then this could mean there was an error initializing logging resources as well.\r\n
0x00000017 | The event logging service encountered an error (res=%1) while initializing logging resources for channel %2.\r\n
0x00000019 | The event logging service encountered a corrupt log file for channel %1. The log was renamed with a .corrupt extension.\r\n
0x0000001a | The event logging service encountered a log file for channel %1 which is an unsupported version. The log was renamed with a .UnsupportedVer extension.\r\n
0x0000001b | The event logging service encountered an error (res=%1) while opening log file for channel %2. Trying again using default log file path %3.\r\n
0x0000001c | The event logging service encountered an error (res=%1) while parsing filter for channel %2. Will continue without filter.\r\n
0x0000001d | The event logging service encountered a fatal error (res=%1) when applying settings to the %2 channel. The service is shutting down since this channel is vital to its operation.\r\n
0x0000001e | The event logging service encountered an error (%1) while enabling publisher %3 to channel %2. This does not affect channel operation, but does affect the ability of the publisher to raise events to the channel. One common reason for this error is that the Provider is using ETW Provider Security and has not granted enable permissions to the Event Log service identity.\r\n
0x0000001f | The event logging service encountered an error (res=%1) while opening configuration for primary channel %2. Trying again using default configuration. This problem usually occurs if registry has been corrupted or explicitly misconfigured.\r\n
0x00000028 | The event logging service encountered an error when attempting to apply one or more policy settings.\r\n
0x00000068 | The %3 log file was cleared.\r\n
0x00000069 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x0000006a | Corruption was detected in the log for the %1 channel and some data was erased.\r\n
0x0000044c | The event logging service has shut down.\r\n
0x0000044d | Audit events have been dropped by the transport.  %1\r\n
0x0000044e | The audit log was cleared.%nSubject:%n%tSecurity ID:%t%1%n%tAccount Name:%t%2%n%tDomain Name:%t%3%n%tLogon ID:%t%4\r\n
0x0000044f | The security log is now %1 percent full.\r\n
0x00000450 | The security log is now full.\r\n
0x00000451 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x00000452 | Events have been dropped by the event logging service. The reason code is %1.\r\n
0x00000453 | The event logging service encountered an error while processing an incoming event from publisher %3 and trying to process the metadata for it.\r\n
0x00000454 | The event logging service encountered an error while processing an incoming event published from %3.\r\n
0x00001770 | The %1 log file is full.\r\n
0x10000012 | Service availability\r\n
0x10000013 | Service configuration\r\n
0x10000036 | Audit Success\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000064 | Service startup\r\n
0x70000065 | Event processing\r\n
0x70000067 | Service shutdown\r\n
0x70000068 | Log clear\r\n
0x70000069 | Log automatic backup\r\n
0x90000001 | Microsoft-Windows-Eventlog\r\n
0x90000002 | System\r\n
0x90000003 | Security\r\n
0x90000004 | Setup\r\n
0x90000005 | Debug\r\n
0x90000006 | Analytic\r\n
0xb0000067 | Events have been dropped by the transport.  The session name is %2 and the reason code is %1.\r\n
0xb000006b | The event logging service encountered an error %1 while going through publisher configuration. The publisher %2 is already installed with GUID %3.\r\n
0xd0000001 | Events were lost because there were no free buffers. Flushing to disk could not catch up with incoming events.\r\n
0xd0000002 | One or more buffers were dropped because a real time consumer could not catch up.\r\n
0xd0000003 | The real time backup file was corrupt due to improper shutdown.\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15

Message identifier | Message string
--- | ---
0x00000014 | The event logging service encountered an error %1 while obtaining or processing configuration for channel %2.\r\n
0x00000015 | The event logging service encountered a configuration-related error (res=%1) for channel %2. The error was encountered while processing the %3 configuration property.\r\n
0x00000016 | The event logging service encountered an error while initializing publishing resources for channel %2. If channel type is Analytic or Debug, then this could mean there was an error initializing logging resources as well.\r\n
0x00000017 | The event logging service encountered an error (res=%1) while initializing logging resources for channel %2.\r\n
0x00000019 | The event logging service encountered a corrupt log file for channel %1. The log was renamed with a .corrupt extension.\r\n
0x0000001a | The event logging service encountered a log file for channel %1 which is an unsupported version. The log was renamed with a .UnsupportedVer extension.\r\n
0x0000001b | The event logging service encountered an error (res=%1) while opening log file for channel %2. Trying again using default log file path %3.\r\n
0x0000001c | The event logging service encountered an error (res=%1) while parsing filter for channel %2. Will continue without filter.\r\n
0x0000001d | The event logging service encountered a fatal error (res=%1) when applying settings to the %2 channel. The service is shutting down since this channel is vital to its operation.\r\n
0x0000001e | The event logging service encountered an error (%1) while enabling publisher %3 to channel %2. This does not affect channel operation, but does affect the ability of the publisher to raise events to the channel. One common reason for this error is that the Provider is using ETW Provider Security and has not granted enable permissions to the Event Log service identity.\r\n
0x0000001f | The event logging service encountered an error (res=%1) while opening configuration for primary channel %2. Trying again using default configuration. This problem usually occurs if registry has been corrupted or explicitly misconfigured.\r\n
0x00000028 | The event logging service encountered an error when attempting to apply one or more policy settings.\r\n
0x00000068 | The %3 log file was cleared.\r\n
0x00000069 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x0000006a | Corruption was detected in the log for the %1 channel and some data was erased.\r\n
0x0000006c | The previous system shutdown was unexpected.\r\n
0x0000044c | The event logging service has shut down.\r\n
0x0000044d | Audit events have been dropped by the transport.  %1\r\n
0x0000044e | The audit log was cleared.%nSubject:%n%tSecurity ID:%t%1%n%tAccount Name:%t%2%n%tDomain Name:%t%3%n%tLogon ID:%t%4\r\n
0x0000044f | The security log is now %1 percent full.\r\n
0x00000450 | The security log is now full.\r\n
0x00000451 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x00000452 | Events have been dropped by the event logging service. The reason code is %1.\r\n
0x00000453 | The event logging service encountered an error while processing an incoming event from publisher %3 and trying to process the metadata for it.\r\n
0x00000454 | The event logging service encountered an error while processing an incoming event published from %3.\r\n
0x00001770 | The %1 log file is full.\r\n
0x10000012 | Service availability\r\n
0x10000013 | Service configuration\r\n
0x10000014 | System availability\r\n
0x10000036 | Audit Success\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000064 | Service startup\r\n
0x70000065 | Event processing\r\n
0x70000067 | Service shutdown\r\n
0x70000068 | Log clear\r\n
0x70000069 | Log automatic backup\r\n
0x7000006c | System Abnormal Shutdown\r\n
0x90000001 | Microsoft-Windows-Eventlog\r\n
0x90000002 | System\r\n
0x90000003 | Security\r\n
0x90000004 | Setup\r\n
0x90000005 | Debug\r\n
0x90000006 | Analytic\r\n
0xb0000067 | Events have been dropped by the transport.  The session name is %2 and the reason code is %1.\r\n
0xb000006b | The event logging service encountered an error %1 while going through publisher configuration. The publisher %2 is already installed with GUID %3.\r\n
0xb000006e | Loading metadata for publisher %2 (%1) and trying to process the metadata for it.\r\n
0xb000006f | Finished loading metadata for publisher %2 (%1), with %3 event metadatas processed.\r\n
0xb0000070 | Failed to load metadata for publisher %2 (%1). The reason code is %3.\r\n
0xd0000001 | Events were lost because there were no free buffers. Flushing to disk could not catch up with incoming events.\r\n
0xd0000002 | One or more buffers were dropped because a real time consumer could not catch up.\r\n
0xd0000003 | The real time backup file was corrupt due to improper shutdown.\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x00000014 | The event logging service encountered an error %1 while obtaining or processing configuration for channel %2.\r\n
0x00000015 | The event logging service encountered a configuration-related error (res=%1) for channel %2. The error was encountered while processing the %3 configuration property.\r\n
0x00000016 | The event logging service encountered an error while initializing publishing resources for channel %2. If channel type is Analytic or Debug, then this could mean there was an error initializing logging resources as well.\r\n
0x00000017 | The event logging service encountered an error (res=%1) while initializing logging resources for channel %2.\r\n
0x00000019 | The event logging service encountered a corrupt log file for channel %1. The log was renamed with a .corrupt extension.\r\n
0x0000001a | The event logging service encountered a log file for channel %1 which is an unsupported version. The log was renamed with a .UnsupportedVer extension.\r\n
0x0000001b | The event logging service encountered an error (res=%1) while opening log file for channel %2 at %3. Trying again using default log file path %4.\r\n
0x0000001c | The event logging service encountered an error (res=%1) while parsing filter for channel %2. Will continue without filter.\r\n
0x0000001d | The event logging service encountered a fatal error (res=%1) when applying settings to the %2 channel. The service is shutting down since this channel is vital to its operation.\r\n
0x0000001e | The event logging service encountered an error (%1) while enabling publisher %3 to channel %2. This does not affect channel operation, but does affect the ability of the publisher to raise events to the channel. One common reason for this error is that the Provider is using ETW Provider Security and has not granted enable permissions to the Event Log service identity.\r\n
0x0000001f | The event logging service encountered an error (res=%1) while opening configuration for primary channel %2. Trying again using default configuration. This problem usually occurs if registry has been corrupted or explicitly misconfigured.\r\n
0x00000028 | The event logging service encountered an error when attempting to apply one or more policy settings.\r\n
0x00000068 | The %3 log file was cleared.\r\n
0x00000069 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x0000006a | Corruption was detected in the log for the %1 channel and some data was erased.\r\n
0x0000006c | The previous system shutdown was unexpected.\r\n
0x0000044c | The event logging service has shut down.\r\n
0x0000044d | Audit events have been dropped by the transport.  %1\r\n
0x0000044e | The audit log was cleared.%nSubject:%n%tSecurity ID:%t%1%n%tAccount Name:%t%2%n%tDomain Name:%t%3%n%tLogon ID:%t%4\r\n
0x0000044f | The security log is now %1 percent full.\r\n
0x00000450 | The security log is now full.\r\n
0x00000451 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x00000452 | Events have been dropped by the event logging service. The reason code is %1.\r\n
0x00000453 | The event logging service encountered an error while processing an incoming event from publisher %3 and trying to process the metadata for it.\r\n
0x00000454 | The event logging service encountered an error while processing an incoming event published from %3.\r\n
0x00001770 | The %1 log file is full.\r\n
0x10000012 | Service availability\r\n
0x10000013 | Service configuration\r\n
0x10000014 | System availability\r\n
0x10000036 | Audit Success\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000064 | Service startup\r\n
0x70000065 | Event processing\r\n
0x70000067 | Service shutdown\r\n
0x70000068 | Log clear\r\n
0x70000069 | Log automatic backup\r\n
0x7000006c | System Abnormal Shutdown\r\n
0x90000001 | Microsoft-Windows-Eventlog\r\n
0x90000002 | System\r\n
0x90000003 | Security\r\n
0x90000004 | Setup\r\n
0x90000005 | Debug\r\n
0x90000006 | Analytic\r\n
0xb000001b | The event logging service encountered an error (res=%1) while opening log file for channel %2. Trying again using default log file path %3.\r\n
0xb0000067 | Events have been dropped by the transport.  The session name is %2 and the reason code is %1.\r\n
0xb000006b | The event logging service encountered an error %1 while going through publisher configuration. The publisher %2 is already installed with GUID %3.\r\n
0xb000006e | Loading metadata for publisher %2 (%1) and trying to process the metadata for it.\r\n
0xb000006f | Finished loading metadata for publisher %2 (%1), with %3 event metadatas processed.\r\n
0xb0000070 | Failed to load metadata for publisher %2 (%1). The reason code is %3.\r\n
0xd0000001 | Events were lost because there were no free buffers. Flushing to disk could not catch up with incoming events.\r\n
0xd0000002 | One or more buffers were dropped because a real time consumer could not catch up.\r\n
0xd0000003 | The real time backup file was corrupt due to improper shutdown.\r\n

### 10.0.17763.1

Message identifier | Message string
--- | ---
0x00000014 | The event logging service encountered an error %1 while obtaining or processing configuration for channel %2.\r\n
0x00000015 | The event logging service encountered a configuration-related error (res=%1) for channel %2. The error was encountered while processing the %3 configuration property.\r\n
0x00000016 | The event logging service encountered an error while initializing publishing resources for channel %2. If channel type is Analytic or Debug, then this could mean there was an error initializing logging resources as well.\r\n
0x00000017 | The event logging service encountered an error (res=%1) while initializing logging resources for channel %2.\r\n
0x00000019 | The event logging service encountered a corrupt log file for channel %1. The log was renamed with a .corrupt extension.\r\n
0x0000001a | The event logging service encountered a log file for channel %1 which is an unsupported version. The log was renamed with a .UnsupportedVer extension.\r\n
0x0000001b | The event logging service encountered an error (res=%1) while opening log file for channel %2 at %3. Trying again using default log file path %4.\r\n
0x0000001c | The event logging service encountered an error (res=%1) while parsing filter for channel %2. Will continue without filter.\r\n
0x0000001d | The event logging service encountered a fatal error (res=%1) when applying settings to the %2 channel. The service is shutting down since this channel is vital to its operation.\r\n
0x0000001e | The event logging service encountered an error (%1) while enabling publisher %3 to channel %2. This does not affect channel operation, but does affect the ability of the publisher to raise events to the channel. One common reason for this error is that the Provider is using ETW Provider Security and has not granted enable permissions to the Event Log service identity.\r\n
0x0000001f | The event logging service encountered an error (res=%1) while opening configuration for primary channel %2. Trying again using default configuration. This problem usually occurs if registry has been corrupted or explicitly misconfigured.\r\n
0x00000028 | The event logging service encountered an error when attempting to apply one or more policy settings.\r\n
0x00000068 | The %3 log file was cleared.\r\n
0x00000069 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x0000006a | Corruption was detected in the log for the %1 channel and some data was erased.\r\n
0x0000006c | The previous system shutdown was unexpected.\r\n
0x0000044c | The event logging service has shut down.\r\n
0x0000044d | Audit events have been dropped by the transport.  %1\r\n
0x0000044e | The audit log was cleared.%nSubject:%n%tSecurity ID:%t%1%n%tAccount Name:%t%2%n%tDomain Name:%t%3%n%tLogon ID:%t%4\r\n
0x0000044f | The security log is now %1 percent full.\r\n
0x00000450 | The security log is now full.\r\n
0x00000451 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x00000452 | Events have been dropped by the event logging service. The reason code is %1.\r\n
0x00000453 | The event logging service encountered an error while processing an incoming event from publisher %3 and trying to process the metadata for it.\r\n
0x00000454 | The event logging service encountered an error while processing an incoming event published from %3.\r\n
0x00001770 | The %1 log file is full.\r\n
0x10000012 | Service availability\r\n
0x10000013 | Service configuration\r\n
0x10000014 | System availability\r\n
0x10000015 | API Usage Audit\r\n
0x10000036 | Audit Success\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000064 | Service startup\r\n
0x70000065 | Event processing\r\n
0x70000067 | Service shutdown\r\n
0x70000068 | Log clear\r\n
0x70000069 | Log automatic backup\r\n
0x7000006c | System Abnormal Shutdown\r\n
0x7000006d | Service Usage Audit\r\n
0x90000001 | Microsoft-Windows-Eventlog\r\n
0x90000002 | System\r\n
0x90000003 | Security\r\n
0x90000004 | Setup\r\n
0x90000005 | Debug\r\n
0x90000006 | Analytic\r\n
0xb000001b | The event logging service encountered an error (res=%1) while opening log file for channel %2. Trying again using default log file path %3.\r\n
0xb0000067 | Events have been dropped by the transport.  The session name is %2 and the reason code is %1.\r\n
0xb000006b | The event logging service encountered an error %1 while going through publisher configuration. The publisher %2 is already installed with GUID %3.\r\n
0xb000006e | Loading metadata for publisher %2 (%1) and trying to process the metadata for it.\r\n
0xb000006f | Finished loading metadata for publisher %2 (%1), with %3 event metadatas processed.\r\n
0xb0000070 | Failed to load metadata for publisher %2 (%1). The reason code is %3.\r\n
0xb00000c8 | Channel %1 (%2) was enabled (%3) programmatically.\r\n
0xb00000c9 | A push subscription was created for %1.\r\n
0xb00000ca | A pull subscription was created for %1.\r\n
0xb00000cb | OpenEventLog legacy API was used to open %2.\r\n
0xb00000cc | RegisterEventSource legacy API was used to register %2.\r\n
0xb00000cd | ReportEvent legacy API was used to write an event to %2.\r\n
0xd0000001 | Events were lost because there were no free buffers. Flushing to disk could not catch up with incoming events.\r\n
0xd0000002 | One or more buffers were dropped because a real time consumer could not catch up.\r\n
0xd0000003 | The real time backup file was corrupt due to improper shutdown.\r\n
0xd0000004 | Admin\r\n
0xd0000005 | Operational\r\n

### 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000014 | The event logging service encountered an error %1 while obtaining or processing configuration for channel %2.\r\n
0x00000015 | The event logging service encountered a configuration-related error (res=%1) for channel %2. The error was encountered while processing the %3 configuration property.\r\n
0x00000016 | The event logging service encountered an error while initializing publishing resources for channel %2. If channel type is Analytic or Debug, then this could mean there was an error initializing logging resources as well.\r\n
0x00000017 | The event logging service encountered an error (res=%1) while initializing logging resources for channel %2.\r\n
0x00000019 | The event logging service encountered a corrupt log file for channel %1. The log was renamed with a .corrupt extension.\r\n
0x0000001a | The event logging service encountered a log file for channel %1 which is an unsupported version. The log was renamed with a .UnsupportedVer extension.\r\n
0x0000001b | The event logging service encountered an error (res=%1) while opening log file for channel %2 at %3. Trying again using default log file path %4.\r\n
0x0000001c | The event logging service encountered an error (res=%1) while parsing filter for channel %2. Will continue without filter.\r\n
0x0000001d | The event logging service encountered a fatal error (res=%1) when applying settings to the %2 channel. The service is shutting down since this channel is vital to its operation.\r\n
0x0000001e | The event logging service encountered an error (%1) while enabling publisher %3 to channel %2. This does not affect channel operation, but does affect the ability of the publisher to raise events to the channel. One common reason for this error is that the Provider is using ETW Provider Security and has not granted enable permissions to the Event Log service identity.\r\n
0x0000001f | The event logging service encountered an error (res=%1) while opening configuration for primary channel %2. Trying again using default configuration. This problem usually occurs if registry has been corrupted or explicitly misconfigured.\r\n
0x00000028 | The event logging service encountered an error when attempting to apply one or more policy settings.\r\n
0x00000068 | The %3 log file was cleared.\r\n
0x00000069 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x0000006a | Corruption was detected in the log for the %1 channel and some data was erased.\r\n
0x0000006c | The previous system shutdown was unexpected.\r\n
0x0000044c | The event logging service has shut down.\r\n
0x0000044d | Audit events have been dropped by the transport.  %1\r\n
0x0000044e | The audit log was cleared.%nSubject:%n%tSecurity ID:%t%1%n%tAccount Name:%t%2%n%tDomain Name:%t%3%n%tLogon ID:%t%4\r\n
0x0000044f | The security log is now %1 percent full.\r\n
0x00000450 | The security log is now full.\r\n
0x00000451 | Event log automatic backup%n%tLog:%t%1%n%tFile:%t%2%n\r\n
0x00000452 | Events have been dropped by the event logging service. The reason code is %1.\r\n
0x00000453 | The event logging service encountered an error while processing an incoming event from publisher %3 and trying to process the metadata for it.\r\n
0x00000454 | The event logging service encountered an error while processing an incoming event published from %3.\r\n
0x00001770 | The %1 log file is full.\r\n
0x10000012 | Service availability\r\n
0x10000013 | Service configuration\r\n
0x10000014 | System availability\r\n
0x10000015 | API Usage Audit\r\n
0x10000036 | Audit Success\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000064 | Service startup\r\n
0x70000065 | Event processing\r\n
0x70000067 | Service shutdown\r\n
0x70000068 | Log clear\r\n
0x70000069 | Log automatic backup\r\n
0x7000006c | System Abnormal Shutdown\r\n
0x7000006d | Service Usage Audit\r\n
0x90000001 | Microsoft-Windows-Eventlog\r\n
0x90000002 | System\r\n
0x90000003 | Security\r\n
0x90000004 | Setup\r\n
0x90000005 | Debug\r\n
0x90000006 | Analytic\r\n
0xb000001b | The event logging service encountered an error (res=%1) while opening log file for channel %2. Trying again using default log file path %3.\r\n
0xb0000067 | Events have been dropped by the transport.  The session name is %2 and the reason code is %1.\r\n
0xb000006b | The event logging service encountered an error %1 while going through publisher configuration. The publisher %2 is already installed with GUID %3.\r\n
0xb000006e | Loading metadata for publisher %2 (%1) and trying to process the metadata for it.\r\n
0xb000006f | Finished loading metadata for publisher %2 (%1), with %3 event metadatas processed.\r\n
0xb0000070 | Failed to load metadata for publisher %2 (%1). The reason code is %3.\r\n
0xb00000c8 | Channel %1 (%2) was enabled (%3) programmatically.\r\n
0xb00000c9 | A push subscription was created for %1.\r\n
0xb00000ca | A pull subscription was created for %1.\r\n
0xb00000cb | OpenEventLog legacy API was used to open %2.\r\n
0xb00000cc | RegisterEventSource legacy API was used to register %2.\r\n
0xb00100cd | ReportEvent legacy API was used to write an event to %2.\r\n
0xd0000001 | Events were lost because there were no free buffers. Flushing to disk could not catch up with incoming events.\r\n
0xd0000002 | One or more buffers were dropped because a real time consumer could not catch up.\r\n
0xd0000003 | The real time backup file was corrupt due to improper shutdown.\r\n
0xd0000004 | Admin\r\n
0xd0000005 | Operational\r\n
