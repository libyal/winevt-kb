## w32time.dll

Path: %SystemRoot%\system32\w32time.dll

### 5.0.2195.6601

Message identifier | Message string
--- | ---
0x40000000 | Time set (offset < .5 second)\r\n
0x40000001 | Registry LanmanServer\Parameters\timesource is not set, maybe it should be\r\n
0x40000002 | Changing TimeAdjustment from default increment (to compensate for skew)\r\n
0x40000004 | Potential for skew compensation disabled because period is too frequent\r\n
0x40000005 | A leap second seemed to be inserted within the last 24 hours\r\n
0x40000006 | Time set (offset > .5 second)\r\n
0x40000007 | Skew >15 seconds per day, compensation not attempted\r\n
0x40000037 | New DomainController time source is %1 (%2) located in %3\r\n
0x8000000a | Couldn't reach USNO or NIST by Internet (maybe blocked by a firewall)\r\n
0x8000000b | The NTP server %1 didn't respond\r\n
0x8000000c | The NTP server %1 isn't sync'd, time not set\r\n
0x8000000e | Attempt to set time which differs by more than 12 hours aborted\r\n
0x8000000f | The reference and system don't appear in sync with DST change, time not set\r\n
0x80000016 | NetRemoteTOD failed for each PrimarySource\r\n
0x80000017 | Couldn't find a timesource in SecondaryDomain\r\n
0x80000018 | NetRemoteTOD failed\r\n
0x80000019 | It has been over 24 hours since we got a network success\r\n
0x8000001a | Couldn't measure the line delay (accuracy is reduced)\r\n
0x8000001c | Difficulty measuring network delay, check the link to your server(s)\r\n
0x8000001f | Attempt to set date prior to 1995 aborted\r\n
0x8000003c | The time server %1 (%2) returned an insecure (unsigned) time stamp. This likely means that the server experienced an error attempting to validate this client's computer account. Please check the event log on the server.\r\n
0x8000003d | The Time service synced time from time source %1 (%2) .\r\n
0x8000003e | This Machine is a PDC of the domain at the root of the forest. Configure to sync from External time source using the net command,  'net time /setsntp:<server name>'.\r\n
0x8000003f | The time service cannot provide secure (signed) time to client %2 because the attempt to validate its computer account failed with error %1. Falling back to insecure (unsigned) time for this client.\r\n
0x80000040 | Because of repeated network problems, the time service has not been able to find a domain controller to synchronize with for a long time. To reduce network traffic, the time service will wait %1 minutes before trying again. No synchronization will take place during this interval, even if network connectivity is restored. Accumulated time errors may cause certain network operations to fail. To tell the time service that network connectivity has been restored and that it should resynchronize, execute "w32tm /s" from the command line.\r\n
0xc0000020 | Could not create EventLog registry key (higher privilege needed?)\r\n
0xc0000021 | Could not set event message file\r\n
0xc0000022 | Could not set supported event types\r\n
0xc0000023 | OpenSCManager failed\r\n
0xc0000024 | CreateService failed\r\n
0xc0000025 | OpenProcessToken failed\r\n
0xc0000026 | AdjustTokenPrivileges enable failed (higher privilege needed)\r\n
0xc0000027 | AdjustTokenPrivileges disable failed\r\n
0xc000002d | SetLocalTime failed\r\n
0xc000002e | SetSystemTime failed\r\n
0xc0000030 | SetServiceStatus failed\r\n
0xc0000031 | An unexpected error occured while trying to start the server. The port may already be in use.\r\n
0xc0000032 | WNetOpenEnum failed\r\n
0xc0000033 | Invalid socket (TCP/IP might not be loaded)\r\n
0xc0000034 | gethostbyname failed for server %1 (NTP or USNO)\r\n
0xc0000035 | NTP server %1 (%2) returned an incorrectly signed time stamp.\r\n
0xc0000036 | The Windows Time Service was not able to find a Domain Controller. A time and date update was not possible.\r\n
0xc0000038 | The Domain Controller %1 (%2) in %3 returned an incorrectly signed time stamp. If this DC is from the machine's parent domain then the trust link between the domains may be broken and must be fixed. If the DC is from this machine's own domain, then the machine password for this machine is incorrect and should be corrected.\r\n
0xc0000039 | Service configuration is for a third-party DLL but the DLL name is not in the registry.\r\n
0xc000003a | The DLL for time sync does not have the proper entry point.\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x425a0003 | The time provider '%1' logged the following message: %2\r\n
0x425a0023 | The time service is now synchronizing the system time with the time\r\nsource %1.\r\n
0x425a0025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x425a0026 | The time provider NtpClient cannot reach or is currently receiving invalid time data from %1.\r\n
0x825a0002 | The time provider '%1' logged the following warning: %2\r\n
0x825a0006 | The time service encountered an error while reading its configuration\r\nfrom the registry, and will continue running with its previous\r\nconfiguration. The error was: %1\r\n
0x825a0007 | The time provider '%1' returned an error while updating its\r\nconfiguration. The error will be ignored. The error was: %2\r\n
0x825a0008 | The time provider '%1' returned an error when notified of a polling\r\ninterval change. The error will be ignored. The error was: %2\r\n
0x825a0009 | The time provider '%1' returned an error when notified of a time jump.\r\nThe error will be ignored. The error was: %2\r\n
0x825a000a | The time provider '%1' returned an error when asked for time samples.\r\nThe error will be ignored. The error was: %2\r\n
0x825a000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to\r\ndetermine its time source, but it is not a member of a domain.\r\nNtpClient will attempt to use an alternate configured external time \r\nsource if available.  If an external time source is not configured \r\nor used for this computer, you may choose to disable the NtpClient.\r\n
0x825a000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to\r\ndetermine its time source, but it is the PDC emulator for the domain\r\nat the root of the forest, so there is no machine above it in the\r\ndomain hierarchy to use as a time source. \r\nNtpClient will attempt to use an alternate configured external time \r\nsource if available.  If an external time source is not configured \r\nor used for this computer, you may choose to disable the NtpClient.\r\n
0x825a000d | Time Provider NtpClient:  This machine is configured to use the domain hierarchy to \r\ndetermine its time source, but the computer is joined to a \r\nWindows NT 4.0 domain. Windows NT 4.0 domain controllers do not have \r\na time service and do not support domain hierarchy as a time source.  \r\nNtpClient will attempt to use an alternate configured external time \r\nsource if available.  If an external time source is not configured \r\nor used for this computer, you may choose to disable the NtpClient.\r\n
0x825a000e | The time provider NtpClient was unable to find a domain controller to use as a time\r\nsource. NtpClient will try again in %1 minutes.\r\n
0x825a0010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually\r\nconfigured peer '%1'. This peer will not be used as a\r\ntime source.\r\nThe error was: %2\r\n
0x825a0011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually\r\nconfigured peer '%1'. NtpClient will try the DNS lookup again in %3\r\nminutes.\r\nThe error was: %2\r\n
0x825a0012 | The time provider NtpClient failed to establish a trust relationship between this\r\ncomputer and the %1 domain in order to securely synchronize time.\r\nNtpClient will try again in %3 minutes.\r\nThe error was: %2\r\n
0x825a0016 | The time provider NtpServer encountered an error while digitally signing the \r\nNTP response.  NtpServer cannot provide secure (signed) time to the\r\nclient and will ignore the request.\r\nThe error was: %2\r\n
0x825a0017 | The time provider NtpServer encountered an error while digitally signing the \r\nNTP response for symmetric peer %1. NtpServer cannot provide \r\nsecure (signed) time to the peer and will not send a packet.\r\nThe error was: %2\r\n
0x825a0018 | Time Provider NtpClient: No valid response has been received from domain controller %1\r\nafter 8 attempts to contact it. This domain controller will be\r\ndiscarded as a time source and NtpClient will attempt to discover a \r\nnew domain controller from which to synchronize.\r\n
0x825a0019 | The time provider NtpClient cannot determine whether the response received from %1 has \r\na valid signature. The response will be ignored.\r\nThe error was: %2\r\n
0x825a001a | Time Provider NtpClient: The response received from domain controller %1\r\nhas a bad signature. The response may have been tampered with\r\nand will be ignored.\r\n
0x825a001b | Time Provider NtpClient: The response received from domain controller %1 is \r\nmissing the signature. The response may have been tampered with\r\nand will be ignored.\r\n
0x825a001f | The time service discovered that the system time zone information was\r\ncorrupted. Because many system components require valid time zone\r\ninformation, the time service has reset the system time zone to GMT.\r\nUse the Date/Time control panel to set the correct time zone.\r\n
0x825a0021 | The time service has made a discontinuous change in the system clock.\r\nThe system time has been changed by %1 seconds.\r\n
0x825a0024 | The time service has not been able to synchronize the system time\r\nfor %1 seconds because none of the time providers has been able to\r\nprovide a usable time stamp. The system clock is unsynchronized.\r\n
0x825a0027 | The time service is unable to register for network configuration \r\nchange events.  This may occur when TCP/IP is not correctly\r\nconfigured.  The time service will be unable to sync time from \r\nnetwork providers, but will still use locally installed hardware\r\nprovdiers, if any are available. \r\n
0x825a0028 | The time provider '%1' was stopped with error %2. \r\n
0x825a002b | The time provider '%1' returned an error when notified of a \r\nnetwork configuration change. The error will be ignored. \r\nThe error was: %2\r\n
0xc25a0001 | The time provider '%1' logged the following error: %2\r\n
0xc25a0004 | The time provider '%1' failed to start due to the following error: %2\r\n
0xc25a0005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0xc25a000f | The time provider NtpClient was unable to find a domain controller to use as a time\r\nsource.  NtpClient will fall back to the remaining configured time \r\nsources, if any are available.\r\nThe error was: %1\r\n
0xc25a0013 | Logging was requested, but the time service encountered an error\r\nwhile trying to set up the log file: %1.\r\nThe error was: %2\r\n
0xc25a0014 | Logging was requested, but the time service encountered an error\r\nwhile trying to write to the log file: %1. \r\nThe error was: %2\r\n
0xc25a0015 | The time service is configured to use one or more input\r\nproviders, however, none of the input providers are available.\r\nThe time service has no source of accurate time. \r\n
0xc25a001c | The time provider NtpClient is configured to acquire time from one or more\r\ntime sources, however none of the sources are accessible.\r\nNtpClient has no source of accurate time. \r\n
0xc25a001d | The time provider NtpClient is configured to acquire time from one or more\r\ntime sources, however none of the sources are currently accessible. \r\nNo attempt to contact a source will be made for %1 minutes.\r\nNtpClient has no source of accurate time. \r\n
0xc25a001e | The time service encountered an error while reading its configuration\r\nfrom the registry and cannot start. The error was: %1\r\n
0xc25a0020 | The time service discovered that the system time zone information was\r\ncorrupted. The time service tried to reset the system time zone to\r\nGMT, but failed. The time service cannot start.\r\nThe error was: %1\r\n
0xc25a0022 | The time service has detected that the system time needs to be \r\nchanged by %1 seconds. The time service will not change the system \r\ntime by more than %2 seconds. Verify that your time and time zone \r\nare correct, and that the time source %3 is working properly.\r\n
0xc25a0029 | The time service has been configured to use one or more input\r\nproviders, however, none of the input providers are still running. \r\nThe time service has no source of accurate time. \r\n
0xc25a002a | The time service attempted to create a named event which was already\r\nopened.  This could be the result of an attempt to compromise your system's\r\nsecurity.\r\n
0xc25a002c | The time provider NtpClient encountered an error and was forced to shut down.  The error was: %1\r\n
0xc25a002d | The time provider NtpServer encountered an error and was forced to shut down.  The error was: %1\r\n
0xc25a002e | The time service encountered an error and was forced to shut down.  The error was: %1\r\n
0xc25a005a | NoAuth\r\n
0xc25a005b | NtDigest\r\n
0xc25a005c | The peer is unreachable. \r\n
0xc25a005e | The time sample was rejected because: Duplicate timestamps were received from this peer. \r\n
0xc25a005f | The time sample was rejected because: Message was received out-of-order. \r\n
0xc25a0060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions.  This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response. \r\n
0xc25a0061 | The time sample was rejected because: Round-trip delay too large.  \r\n
0xc25a0062 | The time sample was rejected because: Packet not authenticated. \r\n
0xc25a0063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization. \r\n
0xc25a0064 | The time sample was rejected because: The peer's stratum is less than the host's stratum. \r\n
0xc25a0065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values.  This may be caused by poor network conditions.\r\n
0xc25a0066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x425a0003 | The time provider '%1' logged the following message: %2\r\n
0x425a0023 | The time service is now synchronizing the system time with the time\r\nsource %1.\r\n
0x425a0025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x425a0026 | The time provider NtpClient cannot reach or is currently receiving invalid time data from %1.\r\n
0x825a0002 | The time provider '%1' logged the following warning: %2\r\n
0x825a0006 | The time service encountered an error while reading its configuration\r\nfrom the registry, and will continue running with its previous\r\nconfiguration. The error was: %1\r\n
0x825a0007 | The time provider '%1' returned an error while updating its\r\nconfiguration. The error will be ignored. The error was: %2\r\n
0x825a0008 | The time provider '%1' returned an error when notified of a polling\r\ninterval change. The error will be ignored. The error was: %2\r\n
0x825a0009 | The time provider '%1' returned an error when notified of a time jump.\r\nThe error will be ignored. The error was: %2\r\n
0x825a000a | The time provider '%1' returned an error when asked for time samples.\r\nThe error will be ignored. The error was: %2\r\n
0x825a000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to\r\ndetermine its time source, but it is not a member of a domain.\r\nNtpClient will attempt to use an alternate configured external time \r\nsource if available.  If an external time source is not configured \r\nor used for this computer, you may choose to disable the NtpClient.\r\n
0x825a000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to\r\ndetermine its time source, but it is the PDC emulator for the domain\r\nat the root of the forest, so there is no machine above it in the\r\ndomain hierarchy to use as a time source.  It is recommended that you either\r\nconfigure a reliable time service in the root domain, or manually configure\r\nthe PDC to synchronize with an external time source.  Otherwise, this machine will \r\nfunction as the authoritative time source in the domain hierarchy.  If an external \r\ntime source is not configured or used for this computer, you may choose to disable \r\nthe NtpClient.\r\n
0x825a000d | Time Provider NtpClient:  This machine is configured to use the domain hierarchy to \r\ndetermine its time source, but the computer is joined to a \r\nWindows NT 4.0 domain. Windows NT 4.0 domain controllers do not have \r\na time service and do not support domain hierarchy as a time source.  \r\nNtpClient will attempt to use an alternate configured external time \r\nsource if available.  If an external time source is not configured \r\nor used for this computer, you may choose to disable the NtpClient.\r\n
0x825a000e | The time provider NtpClient was unable to find a domain controller to use as a time\r\nsource. NtpClient will try again in %1 minutes.\r\n
0x825a0010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually\r\nconfigured peer '%1'. This peer will not be used as a\r\ntime source.\r\nThe error was: %2\r\n
0x825a0011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually\r\nconfigured peer '%1'. NtpClient will try the DNS lookup again in %3\r\nminutes.\r\nThe error was: %2\r\n
0x825a0012 | The time provider NtpClient failed to establish a trust relationship between this\r\ncomputer and the %1 domain in order to securely synchronize time.\r\nNtpClient will try again in %3 minutes.\r\nThe error was: %2\r\n
0x825a0016 | The time provider NtpServer encountered an error while digitally signing the \r\nNTP response for peer %1.  NtpServer cannot provide secure (signed) time to the\r\nclient and will ignore the request.\r\nThe error was: %2\r\n
0x825a0017 | The time provider NtpServer encountered an error while digitally signing the \r\nNTP response for symmetric peer %1. NtpServer cannot provide \r\nsecure (signed) time to the peer and will not send a packet.\r\nThe error was: %2\r\n
0x825a0018 | Time Provider NtpClient: No valid response has been received from domain controller %1\r\nafter 8 attempts to contact it. This domain controller will be\r\ndiscarded as a time source and NtpClient will attempt to discover a \r\nnew domain controller from which to synchronize.\r\n
0x825a0019 | The time provider NtpClient cannot determine whether the response received from %1 has \r\na valid signature. The response will be ignored.\r\nThe error was: %2\r\n
0x825a001a | Time Provider NtpClient: The response received from domain controller %1\r\nhas a bad signature. The response may have been tampered with\r\nand will be ignored.\r\n
0x825a001b | Time Provider NtpClient: The response received from domain controller %1 is \r\nmissing the signature. The response may have been tampered with\r\nand will be ignored.\r\n
0x825a001f | The time service discovered that the system time zone information was\r\ncorrupted. Because many system components require valid time zone\r\ninformation, the time service has reset the system time zone to GMT.\r\nUse the Date/Time control panel to set the correct time zone.\r\n
0x825a0021 | The time service has made a discontinuous change in the system clock.\r\nThe system time has been changed by %1 seconds.\r\n
0x825a0024 | The time service has not synchronized the system time for %1 seconds \r\nbecause none of the time service providers provided a usable time \r\nstamp. The time service is no longer synchronized and cannot provide \r\nthe time to other clients or update the system clock. Monitor the \r\nsystem events displayed in the Event  Viewer to make sure that a more \r\nserious problem does not exist. \r\n
0x825a0027 | The time service is unable to register for network configuration \r\nchange events.  This may occur when TCP/IP is not correctly\r\nconfigured.  The time service will be unable to sync time from \r\nnetwork providers, but will still use locally installed hardware\r\nprovdiers, if any are available. \r\n
0x825a0028 | The time provider '%1' was stopped with error %2. \r\n
0x825a002b | The time provider '%1' returned an error when notified of a \r\nnetwork configuration change. The error will be ignored. \r\nThe error was: %2\r\n
0x825a002f | Time Provider NtpClient: No valid response has been received from \r\nmanually configured peer %1 after 8 attempts to contact it. This peer will be\r\ndiscarded as a time source and NtpClient will attempt to discover a new peer \r\nwith this DNS name.  \r\n
0x825a0030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually\r\nconfigured peer '%1'. NtpClient will continue to try the DNS lookup every\r\n%3 minutes.  This message will not be logged again until a successful lookup \r\nof this manually configured peer occurs. \r\nThe error was: %2\r\n
0x825a0031 | The time provider NtpClient was unable to find a domain controller to use as a time\r\nsource. NtpClient will continue trying to locate a DC every %1 minutes.  This message\r\nwill not be logged again until after a domain controller is found.  \r\n
0x825a0032 | The time service detected a time difference of greater than %1 milliseconds \r\nfor %2 seconds. The time difference might be caused by synchronization with \r\nlow-accuracy time sources or by suboptimal network conditions. The time service\r\nis no longer synchronized and cannot provide the time to other clients or update \r\nthe system clock. When a valid time stamp is received from a time service \r\nprovider, the time service will correct itself.   \r\n
0x825a0033 | Time Provider NtpClient: The time sample received from peer %1 differs from \r\nthe local time by %2 seconds.  The observed transmission delay from the server\r\nwas %3 milliseconds. \r\n
0x825a005a | NoAuth\r\n
0x825a005b | NtDigest\r\n
0x825a005c | The peer is unreachable. \r\n
0x825a005e | The time sample was rejected because: Duplicate timestamps were received from this peer. \r\n
0x825a005f | The time sample was rejected because: Message was received out-of-order. \r\n
0x825a0060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions.  This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response. \r\n
0x825a0061 | The time sample was rejected because: Round-trip delay too large.  \r\n
0x825a0062 | The time sample was rejected because: Packet not authenticated. \r\n
0x825a0063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization. \r\n
0x825a0064 | The time sample was rejected because: The peer's stratum is less than the host's stratum. \r\n
0x825a0065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values.  This may be caused by poor network conditions.\r\n
0x825a0066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.\r\n
0xc25a0001 | The time provider '%1' logged the following error: %2\r\n
0xc25a0004 | The time provider '%1' failed to start due to the following error: %2\r\n
0xc25a0005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0xc25a000f | The time provider NtpClient was unable to find a domain controller to use as a time\r\nsource.  NtpClient will fall back to the remaining configured time \r\nsources, if any are available.\r\nThe error was: %1\r\n
0xc25a0013 | Logging was requested, but the time service encountered an error\r\nwhile trying to set up the log file: %1.\r\nThe error was: %2\r\n
0xc25a0014 | Logging was requested, but the time service encountered an error\r\nwhile trying to write to the log file: %1. \r\nThe error was: %2\r\n
0xc25a0015 | The time service is configured to use one or more input\r\nproviders, however, none of the input providers are available.\r\nThe time service has no source of accurate time. \r\n
0xc25a001c | The time provider NtpClient is configured to acquire time from one or more\r\ntime sources, however none of the sources are accessible.\r\nNtpClient has no source of accurate time. \r\n
0xc25a001d | The time provider NtpClient is configured to acquire time from one or more\r\ntime sources, however none of the sources are currently accessible. \r\nNo attempt to contact a source will be made for %1 minutes.\r\nNtpClient has no source of accurate time. \r\n
0xc25a001e | The time service encountered an error while reading its configuration\r\nfrom the registry and cannot start. The error was: %1\r\n
0xc25a0020 | The time service discovered that the system time zone information was\r\ncorrupted. The time service tried to reset the system time zone to\r\nGMT, but failed. The time service cannot start.\r\nThe error was: %1\r\n
0xc25a0022 | The time service has detected that the system time needs to be \r\nchanged by %1 seconds. The time service will not change the system \r\ntime by more than %2 seconds. Verify that your time and time zone \r\nare correct, and that the time source %3 is working properly.\r\n
0xc25a0029 | The time service has been configured to use one or more input\r\nproviders, however, none of the input providers are still running. \r\nThe time service has no source of accurate time. \r\n
0xc25a002a | The time service attempted to create a named event which was already\r\nopened.  This could be the result of an attempt to compromise your system's\r\nsecurity.\r\n
0xc25a002c | The time provider NtpClient encountered an error and was forced to shut down.  The error was: %1\r\n
0xc25a002d | The time provider NtpServer encountered an error and was forced to shut down.  The error was: %1\r\n
0xc25a002e | The time service encountered an error and was forced to shut down.  The error was: %1\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x0000005a | NoAuth\r\n
0x0000005b | NtDigest\r\n
0x0000005c | The peer is unreachable.\r\n
0x0000005e | The time sample was rejected because: Duplicate timestamps were received from this peer.\r\n
0x0000005f | The time sample was rejected because: Message was received out-of-order.\r\n
0x00000060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions. This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response.\r\n
0x00000061 | The time sample was rejected because: Round-trip delay too large.\r\n
0x00000062 | The time sample was rejected because: Packet not authenticated.\r\n
0x00000063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization.\r\n
0x00000064 | The time sample was rejected because: The peer's stratum is less than the host's stratum.\r\n
0x00000065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values. This may be caused by poor network conditions.\r\n
0x00000066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.%0\r\n
0x00000067 | The server fails authenticating a request with netlogon failure.\r\n
0x00000068 | The client fails sending out a request.\r\n
0x00000069 | The client fails authenticating a response with netlogon failure.\r\n
0x0000006a | The client fails authenticating a response with a bad signature.\r\n
0x0000006b | The client fails authenticating a response with a missing signature.\r\n
0x00000070 | The peer is unresolved.\r\n
0x425a0003 | The time provider '%1' logged the following message: %2\r\n
0x425a0023 | The time service is now synchronizing the system time with the time source %1.\r\n
0x425a0025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x425a0026 | The time provider NtpClient has not received response from server %1.\r\n
0x425a0035 | The time provider NtpClient fails sending request to server %1.\r\n
0x425a0089 | NtpClient succeeds in resolving manual peer %1 after a previous failure.\r\n
0x425a008a | NtpClient succeeds in resolving domain peer %1 after a previous failure.\r\n
0x825a0002 | The time provider '%1' logged the following warning: %2\r\n
0x825a0006 | The time service encountered an error while reading its configuration from the registry, and will continue running with its previous configuration. The error was: %1\r\n
0x825a0007 | The time provider '%1' returned an error while updating its configuration. The error will be ignored. The error was: %2\r\n
0x825a0008 | The time provider '%1' returned an error when notified of a polling interval change. The error will be ignored. The error was: %2\r\n
0x825a0009 | The time provider '%1' returned an error when notified of a time jump. The error will be ignored. The error was: %2\r\n
0x825a000a | The time provider '%1' returned an error when asked for time samples. The error will be ignored. The error was: %2\r\n
0x825a000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x825a000e | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will try again in %1 minutes.\r\n
0x825a0010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually configured peer '%1'. This peer will not be used as a time source. The error was: %2\r\n
0x825a0011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will try the DNS lookup again in %3 minutes. The error was: %2\r\n
0x825a0012 | The time provider NtpClient failed to establish a trust relationship between this computer and the %1 domain in order to securely synchronize time. NtpClient will try again in %3 minutes. The error was: %2\r\n
0x825a0016 | The time provider NtpServer encountered an error while digitally signing the NTP response for peer %1. NtpServer cannot provide secure (signed) time to the client and will ignore the request. The error was: %2\r\n
0x825a0017 | The time provider NtpServer encountered an error while digitally signing the NTP response for symmetric peer %1. NtpServer cannot provide secure (signed) time to the peer and will not send a packet. The error was: %2\r\n
0x825a0018 | Time Provider NtpClient: No valid response has been received from domain controller %1 after 8 attempts to contact it. This domain controller will be discarded as a time source and NtpClient will attempt to discover a new domain controller from which to synchronize. The error was: %2\r\n
0x825a0019 | The time provider NtpClient cannot determine whether the response received from %1 has  a valid signature. The response will be ignored. The error was: %2\r\n
0x825a001a | Time Provider NtpClient: The response received from domain controller %1 has a bad signature. The response may have been tampered with and will be ignored.\r\n
0x825a001b | Time Provider NtpClient: The response received from domain controller %1 is missing the signature. The response may have been tampered with and will be ignored.\r\n
0x825a001f | The time service discovered that the system time zone information was corrupted. Because many system components require valid time zone information, the time service has reset the system time zone to GMT. Use the Date/Time control panel to set the correct time zone.\r\n
0x825a0021 | The time service has jumped the local system clock by %1 seconds. This occurs when the time source and local system time are far enough apart that clock rate adjustments cannot be made to reach the time specified by the time source.\r\n
0x825a0024 | The time service has not synchronized the system time for %1 seconds because none of the time service providers provided a usable time stamp. The time service will not update the local system time until it is able to synchronize with a time source. If the local system is configured to act as a time server for clients, it will stop advertising as a time source to clients. The time service will continue to retry and sync time with its time sources. Check system event log for other W32time events for more details. Run 'w32tm /resync' to force an instant time synchronization.\r\n
0x825a0027 | The time service is unable to register for network configuration change events. This may occur when TCP/IP is not correctly configured. The time service will be unable to sync time from network providers, but will still use locally installed hardware provdiers, if any are available.\r\n
0x825a0028 | The time provider '%1' was stopped with error %2.\r\n
0x825a002b | The time provider '%1' returned an error when notified of a network configuration change. The error will be ignored. The error was: %2\r\n
0x825a002f | Time Provider NtpClient: No valid response has been received from manually configured peer %1 after 8 attempts to contact it. This peer will be discarded as a time source and NtpClient will attempt to discover a new peer with this DNS name. The error was: %2\r\n
0x825a0030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will continue to try the DNS lookup every %3 minutes. This message will not be logged again until a successful lookup of this manually configured peer occurs. The error was: %2\r\n
0x825a0031 | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will continue trying to locate an AD DC every %1 minutes. This message will not be logged again until after a domain controller is found.\r\n
0x825a0032 | The time service detected a time difference of greater than %1 milliseconds for %2 seconds. The time difference might be caused by synchronization with low-accuracy time sources or by suboptimal network conditions. The time service is no longer synchronized and cannot provide the time to other clients or update the system clock. When a valid time stamp is received from a time service provider, the time service will correct itself.\r\n
0x825a0033 | Time Provider NtpClient: The time sample received from peer %1 differs from the local time by %2 seconds. The observed transmission delay from the server was %3 milliseconds.\r\n
0x825a0034 | The time service has set the time with offset %1 seconds.\r\n
0x825a0081 | NtpClient was unable to set a domain peer to use as a time source because of discovery error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x825a0082 | NtpClient was unable to set a domain peer to use as a time source because of failure in establishing  a trust relationship between this computer and the '%3' domain in order to securely synchronize time. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x825a0083 | NtpClient was unable to set a domain peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1.\r\n
0x825a0084 | NtpClient was unable to set a domain peer to use as a time source because of duplicate error on '%3'.  The same time source '%4' has been specified as manual peer in NtpServer. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x825a0085 | NtpClient was unable to set a domain peer to use a time source because of an unexpected error.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x825a0086 | NtpClient was unable to set a manual peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x825a0087 | NtpClient was unable to set a manual peer to use as a time source because of duplicate error on '%3'. The same time source '%4' has been either specified as manual peer in NtpServer or selected as domain peer.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x825a0088 | NtpClient was unable to set a manual peer to use as a time source because of an unexpected error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x90000001 | Microsoft-Windows-Time-Service\r\n
0xc25a0001 | The time provider '%1' logged the following error: %2\r\n
0xc25a0004 | The time provider '%1' failed to start due to the following error: %2\r\n
0xc25a0005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0xc25a000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is not a member of a domain. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0xc25a000d | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but the computer is joined to a Windows NT 4.0 domain. Windows NT 4.0 domain controllers do not have a time service and do not support domain hierarchy as a time source. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0xc25a000f | The time provider NtpClient was unable to find a domain controller to use as a time source.  NtpClient will fall back to the remaining configured time sources, if any are available. The error was: %1\r\n
0xc25a0013 | Logging was requested, but the time service encountered an error while trying to set up the log file: %1. The error was: %2. Please make sure that 'Local Service' has permission to write to the file or directory.\r\n
0xc25a0014 | Logging was requested, but the time service encountered an error while trying to write to the log file: %1. The error was: %2\r\n
0xc25a0015 | The time service is configured to use one or more input providers, however, none of the input providers are available. The time service has no source of accurate time.\r\n
0xc25a001c | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are accessible. NtpClient has no source of accurate time.\r\n
0xc25a001d | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are currently accessible. No attempt to contact a source will be made for %1 minutes. NtpClient has no source of accurate time.\r\n
0xc25a001e | The time service encountered an error while reading its configuration from the registry and cannot start. The error was: %1\r\n
0xc25a0020 | The time service discovered that the system time zone information was corrupted. The time service tried to reset the system time zone to GMT, but failed. The time service cannot start. The error was: %1\r\n
0xc25a0022 | The time service has detected that the system time needs to be  changed by %1 seconds. The time service will not change the system time by more than %2 seconds. Verify that your time and time zone are correct, and that the time source %3 is working properly.\r\n
0xc25a0029 | The time service has been configured to use one or more input providers, however, none of the input providers are still running. The time service has no source of accurate time.\r\n
0xc25a002a | The time service attempted to create a named event which was already opened. This could be the result of an attempt to compromise your system's security.\r\n
0xc25a002c | The time provider NtpClient encountered an error and was forced to shut down. The error was: %1\r\n
0xc25a002d | The time provider NtpServer encountered an error and was forced to shut down. The error was: %1\r\n
0xc25a002e | The time service encountered an error and was forced to shut down. The error was: %1\r\n
0xc25a0036 | The time service encountered an error while refreshing its configuration in the registry and cannot start. The error was: %1\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x00000001 | The time provider '%1' logged the following error: %2\r\n
0x00000002 | The time provider '%1' logged the following warning: %2\r\n
0x00000003 | The time provider '%1' logged the following message: %2\r\n
0x00000004 | The time provider '%1' failed to start due to the following error: %2\r\n
0x00000005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0x00000006 | The time service encountered an error while reading its configuration from the registry, and will continue running with its previous configuration. The error was: %1\r\n
0x00000007 | The time provider '%1' returned an error while updating its configuration. The error will be ignored. The error was: %2\r\n
0x00000008 | The time provider '%1' returned an error when notified of a polling interval change. The error will be ignored. The error was: %2\r\n
0x00000009 | The time provider '%1' returned an error when notified of a time jump. The error will be ignored. The error was: %2\r\n
0x0000000a | The time provider '%1' returned an error when asked for time samples. The error will be ignored. The error was: %2\r\n
0x0000000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is not a member of a domain. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000d | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but the computer is joined to a Windows NT 4.0 domain. Windows NT 4.0 domain controllers do not have a time service and do not support domain hierarchy as a time source. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000e | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will try again in %1 minutes.\r\n
0x0000000f | The time provider NtpClient was unable to find a domain controller to use as a time source.  NtpClient will fall back to the remaining configured time sources, if any are available. The error was: %1\r\n
0x00000010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually configured peer '%1'. This peer will not be used as a time source. The error was: %2\r\n
0x00000011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will try the DNS lookup again in %3 minutes. The error was: %2\r\n
0x00000012 | The time provider NtpClient failed to establish a trust relationship between this computer and the %1 domain in order to securely synchronize time. NtpClient will try again in %3 minutes. The error was: %2\r\n
0x00000013 | Logging was requested, but the time service encountered an error while trying to set up the log file: %1. The error was: %2. Please make sure that 'Local Service' has permission to write to the file or directory.\r\n
0x00000014 | Logging was requested, but the time service encountered an error while trying to write to the log file: %1. The error was: %2\r\n
0x00000015 | The time service is configured to use one or more input providers, however, none of the input providers are available. The time service has no source of accurate time.\r\n
0x00000016 | The time provider NtpServer encountered an error while digitally signing the NTP response for peer %1. NtpServer cannot provide secure (signed) time to the client and will ignore the request. The error was: %2\r\n
0x00000017 | The time provider NtpServer encountered an error while digitally signing the NTP response for symmetric peer %1. NtpServer cannot provide secure (signed) time to the peer and will not send a packet. The error was: %2\r\n
0x00000018 | Time Provider NtpClient: No valid response has been received from domain controller %1 after 8 attempts to contact it. This domain controller will be discarded as a time source and NtpClient will attempt to discover a new domain controller from which to synchronize. The error was: %2\r\n
0x00000019 | The time provider NtpClient cannot determine whether the response received from %1 has  a valid signature. The response will be ignored. The error was: %2\r\n
0x0000001a | Time Provider NtpClient: The response received from domain controller %1 has a bad signature. The response may have been tampered with and will be ignored.\r\n
0x0000001b | Time Provider NtpClient: The response received from domain controller %1 is missing the signature. The response may have been tampered with and will be ignored.\r\n
0x0000001c | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are accessible. NtpClient has no source of accurate time.\r\n
0x0000001d | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are currently accessible. No attempt to contact a source will be made for %1 minutes. NtpClient has no source of accurate time.\r\n
0x0000001e | The time service encountered an error while reading its configuration from the registry and cannot start. The error was: %1\r\n
0x0000001f | The time service discovered that the system time zone information was corrupted. Because many system components require valid time zone information, the time service has reset the system time zone to GMT. Use the Date/Time control panel to set the correct time zone.\r\n
0x00000020 | The time service discovered that the system time zone information was corrupted. The time service tried to reset the system time zone to GMT, but failed. The time service cannot start. The error was: %1\r\n
0x00000021 | The time service has jumped the local system clock by %1 seconds. This occurs when the time source and local system time are far enough apart that clock rate adjustments cannot be made to reach the time specified by the time source.\r\n
0x00000022 | The time service has detected that the system time needs to be  changed by %1 seconds. The time service will not change the system time by more than %2 seconds. Verify that your time and time zone are correct, and that the time source %3 is working properly.\r\n
0x00000023 | The time service is now synchronizing the system time with the time source %1.\r\n
0x00000024 | The time service has not synchronized the system time for %1 seconds because none of the time service providers provided a usable time stamp. The time service will not update the local system time until it is able to synchronize with a time source. If the local system is configured to act as a time server for clients, it will stop advertising as a time source to clients. The time service will continue to retry and sync time with its time sources. Check system event log for other W32time events for more details. Run 'w32tm /resync' to force an instant time synchronization.\r\n
0x00000025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x00000026 | The time provider NtpClient has not received response from server %1.\r\n
0x00000027 | The time service is unable to register for network configuration change events. This may occur when TCP/IP is not correctly configured. The time service will be unable to sync time from network providers, but will still use locally installed hardware provdiers, if any are available.\r\n
0x00000028 | The time provider '%1' was stopped with error %2.\r\n
0x00000029 | The time service has been configured to use one or more input providers, however, none of the input providers are still running. The time service has no source of accurate time.\r\n
0x0000002a | The time service attempted to create a named event which was already opened. This could be the result of an attempt to compromise your system's security.\r\n
0x0000002b | The time provider '%1' returned an error when notified of a network configuration change. The error will be ignored. The error was: %2\r\n
0x0000002c | The time provider NtpClient encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002d | The time provider NtpServer encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002e | The time service encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002f | Time Provider NtpClient: No valid response has been received from manually configured peer %1 after 8 attempts to contact it. This peer will be discarded as a time source and NtpClient will attempt to discover a new peer with this DNS name. The error was: %2\r\n
0x00000030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will continue to try the DNS lookup every %3 minutes. This message will not be logged again until a successful lookup of this manually configured peer occurs. The error was: %2\r\n
0x00000031 | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will continue trying to locate an AD DC every %1 minutes. This message will not be logged again until after a domain controller is found.\r\n
0x00000032 | The time service detected a time difference of greater than %1 milliseconds for %2 seconds. The time difference might be caused by synchronization with low-accuracy time sources or by suboptimal network conditions. The time service is no longer synchronized and cannot provide the time to other clients or update the system clock. When a valid time stamp is received from a time service provider, the time service will correct itself.\r\n
0x00000033 | Time Provider NtpClient: The time sample received from peer %1 differs from the local time by %2 seconds. The observed transmission delay from the server was %3 milliseconds.\r\n
0x00000034 | The time service has set the time with offset %1 seconds.\r\n
0x00000035 | The time provider NtpClient fails sending request to server %1.\r\n
0x00000036 | The time service encountered an error while refreshing its configuration in the registry and cannot start. The error was: %1\r\n
0x0000005a | NoAuth\r\n
0x0000005b | NtDigest\r\n
0x0000005c | The peer is unreachable.\r\n
0x0000005e | The time sample was rejected because: Duplicate timestamps were received from this peer.\r\n
0x0000005f | The time sample was rejected because: Message was received out-of-order.\r\n
0x00000060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions. This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response.\r\n
0x00000061 | The time sample was rejected because: Round-trip delay too large.\r\n
0x00000062 | The time sample was rejected because: Packet not authenticated.\r\n
0x00000063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization.\r\n
0x00000064 | The time sample was rejected because: The peer's stratum is less than the host's stratum.\r\n
0x00000065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values. This may be caused by poor network conditions.\r\n
0x00000066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.%0\r\n
0x00000067 | The server fails authenticating a request with netlogon failure.\r\n
0x00000068 | The client fails sending out a request.\r\n
0x00000069 | The client fails authenticating a response with netlogon failure.\r\n
0x0000006a | The client fails authenticating a response with a bad signature.\r\n
0x0000006b | The client fails authenticating a response with a missing signature.\r\n
0x00000070 | The peer is unresolved.\r\n
0x00000081 | NtpClient was unable to set a domain peer to use as a time source because of discovery error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000082 | NtpClient was unable to set a domain peer to use as a time source because of failure in establishing  a trust relationship between this computer and the '%3' domain in order to securely synchronize time. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000083 | NtpClient was unable to set a domain peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1.\r\n
0x00000084 | NtpClient was unable to set a domain peer to use as a time source because of duplicate error on '%3'.  The same time source '%4' has been specified as manual peer in NtpServer. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000085 | NtpClient was unable to set a domain peer to use a time source because of an unexpected error.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000086 | NtpClient was unable to set a manual peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000087 | NtpClient was unable to set a manual peer to use as a time source because of duplicate error on '%3'. The same time source '%4' has been either specified as manual peer in NtpServer or selected as domain peer.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000088 | NtpClient was unable to set a manual peer to use as a time source because of an unexpected error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000089 | NtpClient succeeds in resolving manual peer %1 after a previous failure.\r\n
0x0000008a | NtpClient succeeds in resolving domain peer %1 after a previous failure.\r\n
0x0000008b | The time service has started advertising as a time source.\r\n
0x0000008c | The time service has stopped advertising as a time source because the local machine is not an Active Directory Domain Controller.\r\n
0x0000008d | The time service has stopped advertising as a time source because there are no providers running.\r\n
0x0000008e | The time service has stopped advertising as a time source because the local clock is not synchronized.\r\n
0x0000008f | The time service has started advertising as a good time source.\r\n
0x00000090 | The time service has stopped advertising as a good time source.\r\n
0x00000091 | The time service has stopped advertising as a time source.\r\n
0x00000092 | The RODC has received %1 requests in the previous %2 minutes. %3 have resulted in success, and %4 have resulted in failure.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Time-Service\r\n
0x90000002 | System\r\n

### 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00000001 | The time provider '%1' logged the following error: %2\r\n
0x00000002 | The time provider '%1' logged the following warning: %2\r\n
0x00000003 | The time provider '%1' logged the following message: %2\r\n
0x00000004 | The time provider '%1' failed to start due to the following error: %2\r\n
0x00000005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0x00000006 | The time service encountered an error while reading its configuration from the registry, and will continue running with its previous configuration. The error was: %1\r\n
0x00000007 | The time provider '%1' returned an error while updating its configuration. The error will be ignored. The error was: %2\r\n
0x00000008 | The time provider '%1' returned an error when notified of a polling interval change. The error will be ignored. The error was: %2\r\n
0x00000009 | The time provider '%1' returned an error when notified of a time jump. The error will be ignored. The error was: %2\r\n
0x0000000a | The time provider '%1' returned an error when asked for time samples. The error will be ignored. The error was: %2\r\n
0x0000000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is not a member of a domain. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000d | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but the computer is joined to a Windows NT 4.0 domain. Windows NT 4.0 domain controllers do not have a time service and do not support domain hierarchy as a time source. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000e | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will try again in %1 minutes.\r\n
0x0000000f | The time provider NtpClient was unable to find a domain controller to use as a time source.  NtpClient will fall back to the remaining configured time sources, if any are available. The error was: %1\r\n
0x00000010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually configured peer '%1'. This peer will not be used as a time source. The error was: %2\r\n
0x00000011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will try the DNS lookup again in %3 minutes. The error was: %2\r\n
0x00000012 | The time provider NtpClient failed to establish a trust relationship between this computer and the %1 domain in order to securely synchronize time. NtpClient will try again in %3 minutes. The error was: %2\r\n
0x00000013 | Logging was requested, but the time service encountered an error while trying to set up the log file: %1. The error was: %2. Please make sure that 'Local Service' has permission to write to the file or directory.\r\n
0x00000014 | Logging was requested, but the time service encountered an error while trying to write to the log file: %1. The error was: %2\r\n
0x00000015 | The time service is configured to use one or more input providers, however, none of the input providers are available. The time service has no source of accurate time.\r\n
0x00000016 | The time provider NtpServer encountered an error while digitally signing the NTP response for peer %1. NtpServer cannot provide secure (signed) time to the client and will ignore the request. The error was: %2\r\n
0x00000017 | The time provider NtpServer encountered an error while digitally signing the NTP response for symmetric peer %1. NtpServer cannot provide secure (signed) time to the peer and will not send a packet. The error was: %2\r\n
0x00000018 | Time Provider NtpClient: No valid response has been received from domain controller %1 after 8 attempts to contact it. This domain controller will be discarded as a time source and NtpClient will attempt to discover a new domain controller from which to synchronize. The error was: %2\r\n
0x00000019 | The time provider NtpClient cannot determine whether the response received from %1 has  a valid signature. The response will be ignored. The error was: %2\r\n
0x0000001a | Time Provider NtpClient: The response received from domain controller %1 has a bad signature. The response may have been tampered with and will be ignored.\r\n
0x0000001b | Time Provider NtpClient: The response received from domain controller %1 is missing the signature. The response may have been tampered with and will be ignored.\r\n
0x0000001c | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are accessible. NtpClient has no source of accurate time.\r\n
0x0000001d | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are currently accessible. No attempt to contact a source will be made for %1 minutes. NtpClient has no source of accurate time.\r\n
0x0000001e | The time service encountered an error while reading its configuration from the registry and cannot start. The error was: %1\r\n
0x0000001f | The time service discovered that the system time zone information was corrupted. Because many system components require valid time zone information, the time service has reset the system time zone to GMT. Use the Date/Time control panel to set the correct time zone.\r\n
0x00000020 | The time service discovered that the system time zone information was corrupted. The time service tried to reset the system time zone to GMT, but failed. The time service cannot start. The error was: %1\r\n
0x00000021 | The time service has jumped the local system clock by %1 seconds. This occurs when the time source and local system time are far enough apart that clock rate adjustments cannot be made to reach the time specified by the time source.\r\n
0x00000022 | The time service has detected that the system time needs to be  changed by %1 seconds. The time service will not change the system time by more than %2 seconds. Verify that your time and time zone are correct, and that the time source %3 is working properly.\r\n
0x00000023 | The time service is now synchronizing the system time with the time source %1.\r\n
0x00000024 | The time service has not synchronized the system time for %1 seconds because none of the time service providers provided a usable time stamp. The time service will not update the local system time until it is able to synchronize with a time source. If the local system is configured to act as a time server for clients, it will stop advertising as a time source to clients. The time service will continue to retry and sync time with its time sources. Check system event log for other W32time events for more details. Run 'w32tm /resync' to force an instant time synchronization.\r\n
0x00000025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x00000026 | The time provider NtpClient has not received response from server %1.\r\n
0x00000027 | The time service is unable to register for network configuration change events. This may occur when TCP/IP is not correctly configured. The time service will be unable to sync time from network providers, but will still use locally installed hardware provdiers, if any are available.\r\n
0x00000028 | The time provider '%1' was stopped with error %2.\r\n
0x00000029 | The time service has been configured to use one or more input providers, however, none of the input providers are still running. The time service has no source of accurate time.\r\n
0x0000002a | The time service attempted to create a named event which was already opened. This could be the result of an attempt to compromise your system's security.\r\n
0x0000002b | The time provider '%1' returned an error when notified of a network configuration change. The error will be ignored. The error was: %2\r\n
0x0000002c | The time provider NtpClient encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002d | The time provider NtpServer encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002e | The time service encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002f | Time Provider NtpClient: No valid response has been received from manually configured peer %1 after 8 attempts to contact it. This peer will be discarded as a time source and NtpClient will attempt to discover a new peer with this DNS name. The error was: %2\r\n
0x00000030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will continue to try the DNS lookup every %3 minutes. This message will not be logged again until a successful lookup of this manually configured peer occurs. The error was: %2\r\n
0x00000031 | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will continue trying to locate an AD DC every %1 minutes. This message will not be logged again until after a domain controller is found.\r\n
0x00000032 | The time service detected a time difference of greater than %1 milliseconds for %2 seconds. The time difference might be caused by synchronization with low-accuracy time sources or by suboptimal network conditions. The time service is no longer synchronized and cannot provide the time to other clients or update the system clock. When a valid time stamp is received from a time service provider, the time service will correct itself.\r\n
0x00000033 | Time Provider NtpClient: The time sample received from peer %1 differs from the local time by %2 seconds. The observed transmission delay from the server was %3 milliseconds.\r\n
0x00000034 | The time service has set the time with offset %1 seconds.\r\n
0x00000035 | The time provider NtpClient fails sending request to server %1.\r\n
0x00000036 | The time service encountered an error while refreshing its configuration in the registry and cannot start. The error was: %1\r\n
0x0000005a | NoAuth\r\n
0x0000005b | NtDigest\r\n
0x0000005c | The peer is unreachable.\r\n
0x0000005e | The time sample was rejected because: Duplicate timestamps were received from this peer.\r\n
0x0000005f | The time sample was rejected because: Message was received out-of-order.\r\n
0x00000060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions. This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response.\r\n
0x00000061 | The time sample was rejected because: Round-trip delay too large.\r\n
0x00000062 | The time sample was rejected because: Packet not authenticated.\r\n
0x00000063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization.\r\n
0x00000064 | The time sample was rejected because: The peer's stratum is less than the host's stratum.\r\n
0x00000065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values. This may be caused by poor network conditions.\r\n
0x00000066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.%0\r\n
0x00000067 | The server fails authenticating a request with netlogon failure.\r\n
0x00000068 | The client fails sending out a request.\r\n
0x00000069 | The client fails authenticating a response with netlogon failure.\r\n
0x0000006a | The client fails authenticating a response with a bad signature.\r\n
0x0000006b | The client fails authenticating a response with a missing signature.\r\n
0x00000070 | The peer is unresolved.\r\n
0x00000081 | NtpClient was unable to set a domain peer to use as a time source because of discovery error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000082 | NtpClient was unable to set a domain peer to use as a time source because of failure in establishing  a trust relationship between this computer and the '%3' domain in order to securely synchronize time. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000083 | NtpClient was unable to set a domain peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1.\r\n
0x00000084 | NtpClient was unable to set a domain peer to use as a time source because of duplicate error on '%3'.  The same time source '%4' has been specified as manual peer in NtpServer. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000085 | NtpClient was unable to set a domain peer to use a time source because of an unexpected error.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000086 | NtpClient was unable to set a manual peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000087 | NtpClient was unable to set a manual peer to use as a time source because of duplicate error on '%3'. The same time source '%4' has been either specified as manual peer in NtpServer or selected as domain peer.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000088 | NtpClient was unable to set a manual peer to use as a time source because of an unexpected error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000089 | NtpClient succeeds in resolving manual peer %1 after a previous failure.\r\n
0x0000008a | NtpClient succeeds in resolving domain peer %1 after a previous failure.\r\n
0x0000008b | The time service has started advertising as a time source.\r\n
0x0000008c | The time service has stopped advertising as a time source because the local machine is not an Active Directory Domain Controller.\r\n
0x0000008d | The time service has stopped advertising as a time source because there are no providers running.\r\n
0x0000008e | The time service has stopped advertising as a time source because the local clock is not synchronized.\r\n
0x0000008f | The time service has started advertising as a good time source.\r\n
0x00000090 | The time service has stopped advertising as a good time source.\r\n
0x00000091 | The time service has stopped advertising as a time source.\r\n
0x00000092 | The RODC has received %1 requests in the previous %2 minutes. %3 have resulted in success, and %4 have resulted in failure.\r\n
0x0000009b | NtSignature\r\n
0x0000009c | The RODC was unable to forward a time sync request from client RID %1 because the client's RID value is too large and the domain peer (%2) does not support the uplevel timesync authentication format.\r\n
0x0000009d | The time provider NtpServer received a request from a client (%1) using a legacy protocol format. The request has been ignored per the RequireSecureTimeSyncRequests policy setting. By default, this message will be logged only once per day per unique client address.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Time-Service\r\n
0x90000002 | System\r\n

### 10.0.10586.0, 10.0.14393.0

Message identifier | Message string
--- | ---
0x00000001 | The time provider '%1' logged the following error: %2\r\n
0x00000002 | The time provider '%1' logged the following warning: %2\r\n
0x00000003 | The time provider '%1' logged the following message: %2\r\n
0x00000004 | The time provider '%1' failed to start due to the following error: %2\r\n
0x00000005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0x00000006 | The time service encountered an error while reading its configuration from the registry, and will continue running with its previous configuration. The error was: %1\r\n
0x00000007 | The time provider '%1' returned an error while updating its configuration. The error will be ignored. The error was: %2\r\n
0x00000008 | The time provider '%1' returned an error when notified of a polling interval change. The error will be ignored. The error was: %2\r\n
0x00000009 | The time provider '%1' returned an error when notified of a time jump. The error will be ignored. The error was: %2\r\n
0x0000000a | The time provider '%1' returned an error when asked for time samples. The error will be ignored. The error was: %2\r\n
0x0000000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is not a member of a domain. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000d | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but the computer is joined to a Windows NT 4.0 domain. Windows NT 4.0 domain controllers do not have a time service and do not support domain hierarchy as a time source. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000e | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will try again in %1 minutes.\r\n
0x0000000f | The time provider NtpClient was unable to find a domain controller to use as a time source.  NtpClient will fall back to the remaining configured time sources, if any are available. The error was: %1\r\n
0x00000010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually configured peer '%1'. This peer will not be used as a time source. The error was: %2\r\n
0x00000011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will try the DNS lookup again in %3 minutes. The error was: %2\r\n
0x00000012 | The time provider NtpClient failed to establish a trust relationship between this computer and the %1 domain in order to securely synchronize time. NtpClient will try again in %3 minutes. The error was: %2\r\n
0x00000013 | Logging was requested, but the time service encountered an error while trying to set up the log file: %1. The error was: %2. Please make sure that 'Local Service' has permission to write to the file or directory.\r\n
0x00000014 | Logging was requested, but the time service encountered an error while trying to write to the log file: %1. The error was: %2\r\n
0x00000015 | The time service is configured to use one or more input providers, however, none of the input providers are available. The time service has no source of accurate time.\r\n
0x00000016 | The time provider NtpServer encountered an error while digitally signing the NTP response for peer %1. NtpServer cannot provide secure (signed) time to the client and will ignore the request. The error was: %2\r\n
0x00000017 | The time provider NtpServer encountered an error while digitally signing the NTP response for symmetric peer %1. NtpServer cannot provide secure (signed) time to the peer and will not send a packet. The error was: %2\r\n
0x00000018 | Time Provider NtpClient: No valid response has been received from domain controller %1 after 8 attempts to contact it. This domain controller will be discarded as a time source and NtpClient will attempt to discover a new domain controller from which to synchronize. The error was: %2\r\n
0x00000019 | The time provider NtpClient cannot determine whether the response received from %1 has  a valid signature. The response will be ignored. The error was: %2\r\n
0x0000001a | Time Provider NtpClient: The response received from domain controller %1 has a bad signature. The response may have been tampered with and will be ignored.\r\n
0x0000001b | Time Provider NtpClient: The response received from domain controller %1 is missing the signature. The response may have been tampered with and will be ignored.\r\n
0x0000001c | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are accessible. NtpClient has no source of accurate time.\r\n
0x0000001d | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are currently accessible. No attempt to contact a source will be made for %1 minutes. NtpClient has no source of accurate time.\r\n
0x0000001e | The time service encountered an error while reading its configuration from the registry and cannot start. The error was: %1\r\n
0x0000001f | The time service discovered that the system time zone information was corrupted. Because many system components require valid time zone information, the time service has reset the system time zone to GMT. Use the Date/Time control panel to set the correct time zone.\r\n
0x00000020 | The time service discovered that the system time zone information was corrupted. The time service tried to reset the system time zone to GMT, but failed. The time service cannot start. The error was: %1\r\n
0x00000021 | The time service has jumped the local system clock by %1 seconds. This occurs when the time source and local system time are far enough apart that clock rate adjustments cannot be made to reach the time specified by the time source.\r\n
0x00000022 | The time service has detected that the system time needs to be  changed by %1 seconds. The time service will not change the system time by more than %2 seconds. Verify that your time and time zone are correct, and that the time source %3 is working properly.\r\n
0x00000023 | The time service is now synchronizing the system time with the time source %1.\r\n
0x00000024 | The time service has not synchronized the system time for %1 seconds because none of the time service providers provided a usable time stamp. The time service will not update the local system time until it is able to synchronize with a time source. If the local system is configured to act as a time server for clients, it will stop advertising as a time source to clients. The time service will continue to retry and sync time with its time sources. Check system event log for other W32time events for more details. Run 'w32tm /resync' to force an instant time synchronization.\r\n
0x00000025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x00000026 | The time provider NtpClient has not received response from server %1.\r\n
0x00000027 | The time service is unable to register for network configuration change events. This may occur when TCP/IP is not correctly configured. The time service will be unable to sync time from network providers, but will still use locally installed hardware provdiers, if any are available.\r\n
0x00000028 | The time provider '%1' was stopped with error %2.\r\n
0x00000029 | The time service has been configured to use one or more input providers, however, none of the input providers are still running. The time service has no source of accurate time.\r\n
0x0000002a | The time service attempted to create a named event which was already opened. This could be the result of an attempt to compromise your system's security.\r\n
0x0000002b | The time provider '%1' returned an error when notified of a network configuration change. The error will be ignored. The error was: %2\r\n
0x0000002c | The time provider NtpClient encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002d | The time provider NtpServer encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002e | The time service encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002f | Time Provider NtpClient: No valid response has been received from manually configured peer %1 after 8 attempts to contact it. This peer will be discarded as a time source and NtpClient will attempt to discover a new peer with this DNS name. The error was: %2\r\n
0x00000030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will continue to try the DNS lookup every %3 minutes. This message will not be logged again until a successful lookup of this manually configured peer occurs. The error was: %2\r\n
0x00000031 | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will continue trying to locate an AD DC every %1 minutes. This message will not be logged again until after a domain controller is found.\r\n
0x00000032 | The time service detected a time difference of greater than %1 milliseconds for %2 seconds. The time difference might be caused by synchronization with low-accuracy time sources or by suboptimal network conditions. The time service is no longer synchronized and cannot provide the time to other clients or update the system clock. When a valid time stamp is received from a time service provider, the time service will correct itself.\r\n
0x00000033 | Time Provider NtpClient: The time sample received from peer %1 differs from the local time by %2 seconds. The observed transmission delay from the server was %3 milliseconds.\r\n
0x00000034 | The time service has set the time with offset %1 seconds.\r\n
0x00000035 | The time provider NtpClient fails sending request to server %1.\r\n
0x00000036 | The time service encountered an error while refreshing its configuration in the registry and cannot start. The error was: %1\r\n
0x0000005a | NoAuth\r\n
0x0000005b | NtDigest\r\n
0x0000005c | The peer is unreachable.\r\n
0x0000005e | The time sample was rejected because: Duplicate timestamps were received from this peer.\r\n
0x0000005f | The time sample was rejected because: Message was received out-of-order.\r\n
0x00000060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions. This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response.\r\n
0x00000061 | The time sample was rejected because: Round-trip delay too large.\r\n
0x00000062 | The time sample was rejected because: Packet not authenticated.\r\n
0x00000063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization.\r\n
0x00000064 | The time sample was rejected because: The peer's stratum is less than the host's stratum.\r\n
0x00000065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values. This may be caused by poor network conditions.\r\n
0x00000066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.%0\r\n
0x00000067 | The server fails authenticating a request with netlogon failure.\r\n
0x00000068 | The client fails sending out a request.\r\n
0x00000069 | The client fails authenticating a response with netlogon failure.\r\n
0x0000006a | The client fails authenticating a response with a bad signature.\r\n
0x0000006b | The client fails authenticating a response with a missing signature.\r\n
0x00000070 | The peer is unresolved.\r\n
0x00000081 | NtpClient was unable to set a domain peer to use as a time source because of discovery error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000082 | NtpClient was unable to set a domain peer to use as a time source because of failure in establishing  a trust relationship between this computer and the '%3' domain in order to securely synchronize time. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000083 | NtpClient was unable to set a domain peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1.\r\n
0x00000084 | NtpClient was unable to set a domain peer to use as a time source because of duplicate error on '%3'.  The same time source '%4' has been specified as manual peer in NtpServer. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000085 | NtpClient was unable to set a domain peer to use a time source because of an unexpected error.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000086 | NtpClient was unable to set a manual peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000087 | NtpClient was unable to set a manual peer to use as a time source because of duplicate error on '%3'. The same time source '%4' has been either specified as manual peer in NtpServer or selected as domain peer.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000088 | NtpClient was unable to set a manual peer to use as a time source because of an unexpected error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000089 | NtpClient succeeds in resolving manual peer %1 after a previous failure.\r\n
0x0000008a | NtpClient succeeds in resolving domain peer %1 after a previous failure.\r\n
0x0000008b | The time service has started advertising as a time source.\r\n
0x0000008c | The time service has stopped advertising as a time source because the local machine is not an Active Directory Domain Controller.\r\n
0x0000008d | The time service has stopped advertising as a time source because there are no providers running.\r\n
0x0000008e | The time service has stopped advertising as a time source because the local clock is not synchronized.\r\n
0x0000008f | The time service has started advertising as a good time source.\r\n
0x00000090 | The time service has stopped advertising as a good time source.\r\n
0x00000091 | The time service has stopped advertising as a time source.\r\n
0x00000092 | The RODC has received %1 requests in the previous %2 minutes. %3 have resulted in success, and %4 have resulted in failure.\r\n
0x0000009b | NtSignature\r\n
0x0000009c | The RODC was unable to forward a time sync request from client RID %1 because the client's RID value is too large and the domain peer (%2) does not support the uplevel timesync authentication format.\r\n
0x0000009d | The time provider NtpServer received a request from a client (%1) using a legacy protocol format. The request has been ignored per the RequireSecureTimeSyncRequests policy setting. By default, this message will be logged only once per day per unique client address.\r\n
0x0000009e | The time provider '%1' has indicated that the current hardware and operating environment is not supported and has stopped. This behavior is expected for VMICTimeProvider on non-HyperV-guest environments. This may be the expected behavior for the current provider in the current operating environment as well.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Time-Service\r\n
0x90000002 | System\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x00000001 | The time provider '%1' logged the following error: %2\r\n
0x00000002 | The time provider '%1' logged the following warning: %2\r\n
0x00000003 | The time provider '%1' logged the following message: %2\r\n
0x00000004 | The time provider '%1' failed to start due to the following error: %2\r\n
0x00000005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0x00000006 | The time service encountered an error while reading its configuration from the registry, and will continue running with its previous configuration. The error was: %1\r\n
0x00000007 | The time provider '%1' returned an error while updating its configuration. The error will be ignored. The error was: %2\r\n
0x00000008 | The time provider '%1' returned an error when notified of a polling interval change. The error will be ignored. The error was: %2\r\n
0x00000009 | The time provider '%1' returned an error when notified of a time jump. The error will be ignored. The error was: %2\r\n
0x0000000a | The time provider '%1' returned an error when asked for time samples. The error will be ignored. The error was: %2\r\n
0x0000000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is not a member of a domain. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000d | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but the computer is joined to a Windows NT 4.0 domain. Windows NT 4.0 domain controllers do not have a time service and do not support domain hierarchy as a time source. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000e | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will try again in %1 minutes.\r\n
0x0000000f | The time provider NtpClient was unable to find a domain controller to use as a time source.  NtpClient will fall back to the remaining configured time sources, if any are available. The error was: %1\r\n
0x00000010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually configured peer '%1'. This peer will not be used as a time source. The error was: %2\r\n
0x00000011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will try the DNS lookup again in %3 minutes. The error was: %2\r\n
0x00000012 | The time provider NtpClient failed to establish a trust relationship between this computer and the %1 domain in order to securely synchronize time. NtpClient will try again in %3 minutes. The error was: %2\r\n
0x00000013 | Logging was requested, but the time service encountered an error while trying to set up the log file: %1. The error was: %2. Please make sure that 'Local Service' has permission to write to the file or directory.\r\n
0x00000014 | Logging was requested, but the time service encountered an error while trying to write to the log file: %1. The error was: %2\r\n
0x00000015 | The time service is configured to use one or more input providers, however, none of the input providers are available. The time service has no source of accurate time.\r\n
0x00000016 | The time provider NtpServer encountered an error while digitally signing the NTP response for peer %1. NtpServer cannot provide secure (signed) time to the client and will ignore the request. The error was: %2\r\n
0x00000017 | The time provider NtpServer encountered an error while digitally signing the NTP response for symmetric peer %1. NtpServer cannot provide secure (signed) time to the peer and will not send a packet. The error was: %2\r\n
0x00000018 | Time Provider NtpClient: No valid response has been received from domain controller %1 after 8 attempts to contact it. This domain controller will be discarded as a time source and NtpClient will attempt to discover a new domain controller from which to synchronize. The error was: %2\r\n
0x00000019 | The time provider NtpClient cannot determine whether the response received from %1 has  a valid signature. The response will be ignored. The error was: %2\r\n
0x0000001a | Time Provider NtpClient: The response received from domain controller %1 has a bad signature. The response may have been tampered with and will be ignored.\r\n
0x0000001b | Time Provider NtpClient: The response received from domain controller %1 is missing the signature. The response may have been tampered with and will be ignored.\r\n
0x0000001c | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are accessible. NtpClient has no source of accurate time.\r\n
0x0000001d | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are currently accessible. No attempt to contact a source will be made for %1 minutes. NtpClient has no source of accurate time.\r\n
0x0000001e | The time service encountered an error while reading its configuration from the registry and cannot start. The error was: %1\r\n
0x0000001f | The time service discovered that the system time zone information was corrupted. Because many system components require valid time zone information, the time service has reset the system time zone to GMT. Use the Date/Time control panel to set the correct time zone.\r\n
0x00000020 | The time service discovered that the system time zone information was corrupted. The time service tried to reset the system time zone to GMT, but failed. The time service cannot start. The error was: %1\r\n
0x00000021 | The time service has jumped the local system clock by %1 seconds. This occurs when the time source and local system time are far enough apart that clock rate adjustments cannot be made to reach the time specified by the time source.\r\n
0x00000022 | The time service has detected that the system time needs to be  changed by %1 seconds. The time service will not change the system time by more than %2 seconds. Verify that your time and time zone are correct, and that the time source %3 is working properly.\r\n
0x00000023 | The time service is now synchronizing the system time with the time source %1.\r\n
0x00000024 | The time service has not synchronized the system time for the last %1 seconds because none of the time service providers provided a usable time stamp. The time service will not update the local system time until it is able to synchronize with a time source. If the local system is configured to act as a time server for clients, it will stop advertising as a time source to clients after %2 seconds. The time service will continue to retry and sync time with its time sources. Check system event log for other W32time events for more details. Run 'w32tm /resync' to force an instant time synchronization. You can control the frequency of the time source rediscovery using ClockHoldoverPeriod W32time config setting. Modify the EventLogFlags W32time config setting if you wish to disable this message.\r\n
0x00000025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x00000026 | The time provider NtpClient has not received response from server %1.\r\n
0x00000027 | The time service is unable to register for network configuration change events. This may occur when TCP/IP is not correctly configured. The time service will be unable to sync time from network providers, but will still use locally installed hardware provdiers, if any are available.\r\n
0x00000028 | The time provider '%1' was stopped with error %2.\r\n
0x00000029 | The time service has been configured to use one or more input providers, however, none of the input providers are still running. The time service has no source of accurate time.\r\n
0x0000002a | The time service attempted to create a named event which was already opened. This could be the result of an attempt to compromise your system's security.\r\n
0x0000002b | The time provider '%1' returned an error when notified of a network configuration change. The error will be ignored. The error was: %2\r\n
0x0000002c | The time provider NtpClient encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002d | The time provider NtpServer encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002e | The time service encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002f | Time Provider NtpClient: No valid response has been received from manually configured peer %1 after 8 attempts to contact it. This peer will be discarded as a time source and NtpClient will attempt to discover a new peer with this DNS name. The error was: %2\r\n
0x00000030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will continue to try the DNS lookup every %3 minutes. This message will not be logged again until a successful lookup of this manually configured peer occurs. The error was: %2\r\n
0x00000031 | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will continue trying to locate an AD DC every %1 minutes. This message will not be logged again until after a domain controller is found.\r\n
0x00000032 | The time service detected a time difference of greater than %1 milliseconds for %2 seconds. The time difference might be caused by synchronization with low-accuracy time sources or by suboptimal network conditions. The time service is no longer synchronized and cannot provide the time to other clients or update the system clock. When a valid time stamp is received from a time service provider, the time service will correct itself.\r\n
0x00000033 | Time Provider NtpClient: The time sample received from peer %1 differs from the local time by %2 seconds. The observed transmission delay from the server was %3 milliseconds.\r\n
0x00000034 | The time service has set the time with offset %1 seconds.\r\n
0x00000035 | The time provider NtpClient fails sending request to server %1.\r\n
0x00000036 | The time service encountered an error while refreshing its configuration in the registry and cannot start. The error was: %1\r\n
0x0000005a | NoAuth\r\n
0x0000005b | NtDigest\r\n
0x0000005c | The peer is unreachable.\r\n
0x0000005e | The time sample was rejected because: Duplicate timestamps were received from this peer.\r\n
0x0000005f | The time sample was rejected because: Message was received out-of-order.\r\n
0x00000060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions. This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response.\r\n
0x00000061 | The time sample was rejected because: Round-trip delay too large.\r\n
0x00000062 | The time sample was rejected because: Packet not authenticated.\r\n
0x00000063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization.\r\n
0x00000064 | The time sample was rejected because: The peer's stratum is less than the host's stratum.\r\n
0x00000065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values. This may be caused by poor network conditions.\r\n
0x00000066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.%0\r\n
0x00000067 | The server fails authenticating a request with netlogon failure.\r\n
0x00000068 | The client fails sending out a request.\r\n
0x00000069 | The client fails authenticating a response with netlogon failure.\r\n
0x0000006a | The client fails authenticating a response with a bad signature.\r\n
0x0000006b | The client fails authenticating a response with a missing signature.\r\n
0x00000070 | The peer is unresolved.\r\n
0x00000081 | NtpClient was unable to set a domain peer to use as a time source because of discovery error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000082 | NtpClient was unable to set a domain peer to use as a time source because of failure in establishing  a trust relationship between this computer and the '%3' domain in order to securely synchronize time. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000083 | NtpClient was unable to set a domain peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1.\r\n
0x00000084 | NtpClient was unable to set a domain peer to use as a time source because of duplicate error on '%3'.  The same time source '%4' has been specified as manual peer in NtpServer. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000085 | NtpClient was unable to set a domain peer to use a time source because of an unexpected error.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000086 | NtpClient was unable to set a manual peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000087 | NtpClient was unable to set a manual peer to use as a time source because of duplicate error on '%3'. The same time source '%4' has been either specified as manual peer in NtpServer or selected as domain peer.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000088 | NtpClient was unable to set a manual peer to use as a time source because of an unexpected error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000089 | NtpClient succeeds in resolving manual peer %1 after a previous failure.\r\n
0x0000008a | NtpClient succeeds in resolving domain peer %1 after a previous failure.\r\n
0x0000008b | The time service has started advertising as a time source.\r\n
0x0000008c | The time service has stopped advertising as a time source because the local machine is not an Active Directory Domain Controller.\r\n
0x0000008d | The time service has stopped advertising as a time source because there are no providers running.\r\n
0x0000008e | The time service has stopped advertising as a time source because the local clock is not synchronized.\r\n
0x0000008f | The time service has started advertising as a good time source.\r\n
0x00000090 | The time service has stopped advertising as a good time source.\r\n
0x00000091 | The time service has stopped advertising as a time source.\r\n
0x00000092 | The RODC has received %1 requests in the previous %2 minutes. %3 have resulted in success, and %4 have resulted in failure.\r\n
0x0000009b | NtSignature\r\n
0x0000009c | The RODC was unable to forward a time sync request from client RID %1 because the client's RID value is too large and the domain peer (%2) does not support the uplevel timesync authentication format.\r\n
0x0000009d | The time provider NtpServer received a request from a client (%1) using a legacy protocol format. The request has been ignored per the RequireSecureTimeSyncRequests policy setting. By default, this message will be logged only once per day per unique client address.\r\n
0x0000009e | The time provider '%1' has indicated that the current hardware and operating environment is not supported and has stopped. This behavior is expected for VMICTimeProvider on non-HyperV-guest environments. This may be the expected behavior for the current provider in the current operating environment as well.\r\n
0x0000009f | W32time is unable to communicate with Netlogon Service. This failure prevents NTPClient from discovering and using domain peers, besides causing problems with correct W32time service state being advertised by Netlogon. This could be a temporary condition that resolves itself shortly. If this warning repeats over a considerable period of time, ensure the Netlogon service is running and is responsive and restart W32time service to reintiaize the overall state. The error was %1\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Time-Service\r\n
0x90000002 | System\r\n

### 10.0.16299.15, 10.0.17134.1

Message identifier | Message string
--- | ---
0x00000001 | The time provider '%1' logged the following error: %2\r\n
0x00000002 | The time provider '%1' logged the following warning: %2\r\n
0x00000003 | The time provider '%1' logged the following message: %2\r\n
0x00000004 | The time provider '%1' failed to start due to the following error: %2\r\n
0x00000005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0x00000006 | The time service encountered an error while reading its configuration from the registry, and will continue running with its previous configuration. The error was: %1\r\n
0x00000007 | The time provider '%1' returned an error while updating its configuration. The error will be ignored. The error was: %2\r\n
0x00000008 | The time provider '%1' returned an error when notified of a polling interval change. The error will be ignored. The error was: %2\r\n
0x00000009 | The time provider '%1' returned an error when notified of a time jump. The error will be ignored. The error was: %2\r\n
0x0000000a | The time provider '%1' returned an error when asked for time samples. The error will be ignored. The error was: %2\r\n
0x0000000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is not a member of a domain. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000d | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but the computer is joined to a Windows NT 4.0 domain. Windows NT 4.0 domain controllers do not have a time service and do not support domain hierarchy as a time source. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000e | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will try again in %1 minutes.\r\n
0x0000000f | The time provider NtpClient was unable to find a domain controller to use as a time source.  NtpClient will fall back to the remaining configured time sources, if any are available. The error was: %1\r\n
0x00000010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually configured peer '%1'. This peer will not be used as a time source. The error was: %2\r\n
0x00000011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will try the DNS lookup again in %3 minutes. The error was: %2\r\n
0x00000012 | The time provider NtpClient failed to establish a trust relationship between this computer and the %1 domain in order to securely synchronize time. NtpClient will try again in %3 minutes. The error was: %2\r\n
0x00000013 | Logging was requested, but the time service encountered an error while trying to set up the log file: %1. The error was: %2. Please make sure that 'Local Service' has permission to write to the file or directory.\r\n
0x00000014 | Logging was requested, but the time service encountered an error while trying to write to the log file: %1. The error was: %2\r\n
0x00000015 | The time service is configured to use one or more input providers, however, none of the input providers are available. The time service has no source of accurate time.\r\n
0x00000016 | The time provider NtpServer encountered an error while digitally signing the NTP response for peer %1. NtpServer cannot provide secure (signed) time to the client and will ignore the request. The error was: %2\r\n
0x00000017 | The time provider NtpServer encountered an error while digitally signing the NTP response for symmetric peer %1. NtpServer cannot provide secure (signed) time to the peer and will not send a packet. The error was: %2\r\n
0x00000018 | Time Provider NtpClient: No valid response has been received from domain controller %1 after 8 attempts to contact it. This domain controller will be discarded as a time source and NtpClient will attempt to discover a new domain controller from which to synchronize. The error was: %2\r\n
0x00000019 | The time provider NtpClient cannot determine whether the response received from %1 has  a valid signature. The response will be ignored. The error was: %2\r\n
0x0000001a | Time Provider NtpClient: The response received from domain controller %1 has a bad signature. The response may have been tampered with and will be ignored.\r\n
0x0000001b | Time Provider NtpClient: The response received from domain controller %1 is missing the signature. The response may have been tampered with and will be ignored.\r\n
0x0000001c | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are accessible. NtpClient has no source of accurate time.\r\n
0x0000001d | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are currently accessible. No attempt to contact a source will be made for %1 minutes. NtpClient has no source of accurate time.\r\n
0x0000001e | The time service encountered an error while reading its configuration from the registry and cannot start. The error was: %1\r\n
0x0000001f | The time service discovered that the system time zone information was corrupted. Because many system components require valid time zone information, the time service has reset the system time zone to GMT. Use the Date/Time control panel to set the correct time zone.\r\n
0x00000020 | The time service discovered that the system time zone information was corrupted. The time service tried to reset the system time zone to GMT, but failed. The time service cannot start. The error was: %1\r\n
0x00000021 | The time service has jumped the local system clock by %1 seconds. This occurs when the time source and local system time are far enough apart that clock rate adjustments cannot be made to reach the time specified by the time source.\r\n
0x00000022 | The time service has detected that the system time needs to be  changed by %1 seconds. The time service will not change the system time by more than %2 seconds. Verify that your time and time zone are correct, and that the time source %3 is working properly.\r\n
0x00000023 | The time service is now synchronizing the system time with the time source %1 with reference id %2. Current local stratum number is %3.\r\n
0x00000024 | The time service has not synchronized the system time for the last %1 seconds because none of the time service providers provided a usable time stamp. The time service will not update the local system time until it is able to synchronize with a time source. If the local system is configured to act as a time server for clients, it will stop advertising as a time source to clients after %2 seconds. The time service will continue to retry and sync time with its time sources. Check system event log for other W32time events for more details. Run 'w32tm /resync' to force an instant time synchronization. You can control the frequency of the time source rediscovery using ClockHoldoverPeriod W32time config setting. Modify the EventLogFlags W32time config setting if you wish to disable this message.\r\n
0x00000025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x00000026 | The time provider NtpClient has not received response from server %1.\r\n
0x00000027 | The time service is unable to register for network configuration change events. This may occur when TCP/IP is not correctly configured. The time service will be unable to sync time from network providers, but will still use locally installed hardware provdiers, if any are available.\r\n
0x00000028 | The time provider '%1' was stopped with error %2.\r\n
0x00000029 | The time service has been configured to use one or more input providers, however, none of the input providers are still running. The time service has no source of accurate time.\r\n
0x0000002a | The time service attempted to create a named event which was already opened. This could be the result of an attempt to compromise your system's security.\r\n
0x0000002b | The time provider '%1' returned an error when notified of a network configuration change. The error will be ignored. The error was: %2\r\n
0x0000002c | The time provider NtpClient encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002d | The time provider NtpServer encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002e | The time service encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002f | Time Provider NtpClient: No valid response has been received from manually configured peer %1 after 8 attempts to contact it. This peer will be discarded as a time source and NtpClient will attempt to discover a new peer with this DNS name. The error was: %2\r\n
0x00000030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will continue to try the DNS lookup every %3 minutes. This message will not be logged again until a successful lookup of this manually configured peer occurs. The error was: %2\r\n
0x00000031 | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will continue trying to locate an AD DC every %1 minutes. This message will not be logged again until after a domain controller is found.\r\n
0x00000032 | The time service detected a time difference of greater than %1 milliseconds for %2 seconds. The time difference might be caused by synchronization with low-accuracy time sources or by suboptimal network conditions. The time service is no longer synchronized and cannot provide the time to other clients or update the system clock. When a valid time stamp is received from a time service provider, the time service will correct itself.\r\n
0x00000033 | Time Provider NtpClient: The time sample received from peer %1 differs from the local time by %2 seconds. The observed transmission delay from the server was %3 milliseconds.\r\n
0x00000034 | The time service has set the time with offset %1 seconds.\r\n
0x00000035 | The time provider NtpClient fails sending request to server %1.\r\n
0x00000036 | The time service encountered an error while refreshing its configuration in the registry and cannot start. The error was: %1\r\n
0x0000005a | NoAuth\r\n
0x0000005b | NtDigest\r\n
0x0000005c | The peer is unreachable.\r\n
0x0000005e | The time sample was rejected because: Duplicate timestamps were received from this peer.\r\n
0x0000005f | The time sample was rejected because: Message was received out-of-order.\r\n
0x00000060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions. This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response.\r\n
0x00000061 | The time sample was rejected because: Round-trip delay too large.\r\n
0x00000062 | The time sample was rejected because: Packet not authenticated.\r\n
0x00000063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization.\r\n
0x00000064 | The time sample was rejected because: The peer's stratum is less than the host's stratum.\r\n
0x00000065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values. This may be caused by poor network conditions.\r\n
0x00000066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.%0\r\n
0x00000067 | The server fails authenticating a request with netlogon failure.\r\n
0x00000068 | The client fails sending out a request.\r\n
0x00000069 | The client fails authenticating a response with netlogon failure.\r\n
0x0000006a | The client fails authenticating a response with a bad signature.\r\n
0x0000006b | The client fails authenticating a response with a missing signature.\r\n
0x00000070 | The peer is unresolved.\r\n
0x00000081 | NtpClient was unable to set a domain peer to use as a time source because of discovery error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000082 | NtpClient was unable to set a domain peer to use as a time source because of failure in establishing  a trust relationship between this computer and the '%3' domain in order to securely synchronize time. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000083 | NtpClient was unable to set a domain peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1.\r\n
0x00000084 | NtpClient was unable to set a domain peer to use as a time source because of duplicate error on '%3'.  The same time source '%4' has been specified as manual peer in NtpServer. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000085 | NtpClient was unable to set a domain peer to use a time source because of an unexpected error.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000086 | NtpClient was unable to set a manual peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000087 | NtpClient was unable to set a manual peer to use as a time source because of duplicate error on '%3'. The same time source '%4' has been either specified as manual peer in NtpServer or selected as domain peer.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000088 | NtpClient was unable to set a manual peer to use as a time source because of an unexpected error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000089 | NtpClient succeeds in resolving manual peer %1 after a previous failure.\r\n
0x0000008a | NtpClient succeeds in resolving domain peer %1 after a previous failure.\r\n
0x0000008b | The time service has started advertising as a time source.\r\n
0x0000008c | The time service has stopped advertising as a time source because the local machine is not an Active Directory Domain Controller.\r\n
0x0000008d | The time service has stopped advertising as a time source because there are no providers running.\r\n
0x0000008e | The time service has stopped advertising as a time source because the local clock is not synchronized.\r\n
0x0000008f | The time service has started advertising as a good time source.\r\n
0x00000090 | The time service has stopped advertising as a good time source.\r\n
0x00000091 | The time service has stopped advertising as a time source.\r\n
0x00000092 | The RODC has received %1 requests in the previous %2 minutes. %3 have resulted in success, and %4 have resulted in failure.\r\n
0x0000009b | NtSignature\r\n
0x0000009c | The RODC was unable to forward a time sync request from client RID %1 because the client's RID value is too large and the domain peer (%2) does not support the uplevel timesync authentication format.\r\n
0x0000009d | The time provider NtpServer received a request from a client (%1) using a legacy protocol format. The request has been ignored per the RequireSecureTimeSyncRequests policy setting. By default, this message will be logged only once per day per unique client address.\r\n
0x0000009e | The time provider '%1' has indicated that the current hardware and operating environment is not supported and has stopped. This behavior is expected for VMICTimeProvider on non-HyperV-guest environments. This may be the expected behavior for the current provider in the current operating environment as well.\r\n
0x0000009f | W32time is unable to communicate with Netlogon Service. This failure prevents NTPClient from discovering and using domain peers, besides causing problems with correct W32time service state being advertised by Netlogon. This could be a temporary condition that resolves itself shortly. If this warning repeats over a considerable period of time, ensure the Netlogon service is running and is responsive and restart W32time service to reintiaize the overall state. The error was %1\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Time-Service\r\n
0x90000002 | System\r\n
0xb0000101 | W32time service has started at %1 (UTC), System Tick Count %2.%nConfiguration:%n%3%nTime Providers:%n%4Clock Rate:%5%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000102 | W32time service is stopping at %1 (UTC), System Tick Count %2 with return code: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000103 | NTP Client provider periodic status:%nNtp Client is receiving time data from the following NTP Servers: %1  and the chosen reference time server is %2. System Tick Count %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000104 | W32time Service periodic configuration and status message%nConfiguration:%n%1%nTime Providers:%n%2%nCurrent Status:%nLeap Indicator: %3%nStratum: %4%nPrecision: %5%nRootDelay: %6%nRootDispersion: %7%nReferenceId: %8%nLast Successful Sync Time: %9 (UTC)%nSource: %10%nPoll Interval: %11%nPhase Offset: %12%nClock Rate: %13%nState Machine: %14%nTime Source Flags: %15%nServer Role: %16%nLast Sync Error: %17%nTime Since Last Good Sync: %18%nSystem Tick Count: %19%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000105 | W32time service has set the system time to %1(UTC). Previous system time was %2(UTC). System Tick Count: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000106 | W32time service has adjusted the system clock rate by %1 PPM and the new nominal clock rate is %2. Previous nominal clock rate was %3. System Tick Count: %4.%nClock adjustments below %5 PPM are not logged. Performance counters are recommended to efficiently track small adjustment values.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000107 | W32time Service configuration parameters have been updated. This may impact the fine-grained time synchronization accuracy.%nUpdated Configuration:%n%1%nUpdated Time Providers:%n%2System Tick Count: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000108 | NTP Client observed a change peer reachability. Ntp Client is now receiving time data from the following NTP Servers: %1. System Tick Count: %2.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000109 | The time service is now synchronizing the system time with the reference time source %1 with reference id %2. Current local stratum number is %3, System Tick Count: %4.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb000010a | W32time Service received notification to rediscover its time sources and/or resynchronize time. Reason Code:%1 System Tick Count: %2%nReason code description:%n0 : An explicit time resynchronization request from an administrator%n1 : Power state changes on this machine%n2 : Changes to the network interface or to the network topology%n3 : State changes within W32time that require time synchronization%nThe actions that follow this notifcation may impact fine-grained time synchronization accuracy.For more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n

### 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x00000001 | The time provider '%1' logged the following error: %2\r\n
0x00000002 | The time provider '%1' logged the following warning: %2\r\n
0x00000003 | The time provider '%1' logged the following message: %2\r\n
0x00000004 | The time provider '%1' failed to start due to the following error: %2\r\n
0x00000005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0x00000006 | The time service encountered an error while reading its configuration from the registry, and will continue running with its previous configuration. The error was: %1\r\n
0x00000007 | The time provider '%1' returned an error while updating its configuration. The error will be ignored. The error was: %2\r\n
0x00000008 | The time provider '%1' returned an error when notified of a polling interval change. The error will be ignored. The error was: %2\r\n
0x00000009 | The time provider '%1' returned an error when notified of a time jump. The error will be ignored. The error was: %2\r\n
0x0000000a | The time provider '%1' returned an error when asked for time samples. The error will be ignored. The error was: %2\r\n
0x0000000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is not a member of a domain. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000d | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but the computer is joined to a Windows NT 4.0 domain. Windows NT 4.0 domain controllers do not have a time service and do not support domain hierarchy as a time source. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000e | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will try again in %1 minutes.\r\n
0x0000000f | The time provider NtpClient was unable to find a domain controller to use as a time source.  NtpClient will fall back to the remaining configured time sources, if any are available. The error was: %1\r\n
0x00000010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually configured peer '%1'. This peer will not be used as a time source. The error was: %2\r\n
0x00000011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will try the DNS lookup again in %3 minutes. The error was: %2\r\n
0x00000012 | The time provider NtpClient failed to establish a trust relationship between this computer and the %1 domain in order to securely synchronize time. NtpClient will try again in %3 minutes. The error was: %2\r\n
0x00000013 | Logging was requested, but the time service encountered an error while trying to set up the log file: %1. The error was: %2. Please make sure that 'Local Service' has permission to write to the file or directory.\r\n
0x00000014 | Logging was requested, but the time service encountered an error while trying to write to the log file: %1. The error was: %2\r\n
0x00000015 | The time service is configured to use one or more input providers, however, none of the input providers are available. The time service has no source of accurate time.\r\n
0x00000016 | The time provider NtpServer encountered an error while digitally signing the NTP response for peer %1. NtpServer cannot provide secure (signed) time to the client and will ignore the request. The error was: %2\r\n
0x00000017 | The time provider NtpServer encountered an error while digitally signing the NTP response for symmetric peer %1. NtpServer cannot provide secure (signed) time to the peer and will not send a packet. The error was: %2\r\n
0x00000018 | Time Provider NtpClient: No valid response has been received from domain controller %1 after 8 attempts to contact it. This domain controller will be discarded as a time source and NtpClient will attempt to discover a new domain controller from which to synchronize. The error was: %2\r\n
0x00000019 | The time provider NtpClient cannot determine whether the response received from %1 has  a valid signature. The response will be ignored. The error was: %2\r\n
0x0000001a | Time Provider NtpClient: The response received from domain controller %1 has a bad signature. The response may have been tampered with and will be ignored.\r\n
0x0000001b | Time Provider NtpClient: The response received from domain controller %1 is missing the signature. The response may have been tampered with and will be ignored.\r\n
0x0000001c | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are accessible. NtpClient has no source of accurate time.\r\n
0x0000001d | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are currently accessible. No attempt to contact a source will be made for %1 minutes. NtpClient has no source of accurate time.\r\n
0x0000001e | The time service encountered an error while reading its configuration from the registry and cannot start. The error was: %1\r\n
0x0000001f | The time service discovered that the system time zone information was corrupted. Because many system components require valid time zone information, the time service has reset the system time zone to GMT. Use the Date/Time control panel to set the correct time zone.\r\n
0x00000020 | The time service discovered that the system time zone information was corrupted. The time service tried to reset the system time zone to GMT, but failed. The time service cannot start. The error was: %1\r\n
0x00000021 | The time service has jumped the local system clock by %1 seconds. This occurs when the time source and local system time are far enough apart that clock rate adjustments cannot be made to reach the time specified by the time source.\r\n
0x00000022 | The time service has detected that the system time needs to be  changed by %1 seconds. The time service will not change the system time by more than %2 seconds. Verify that your time and time zone are correct, and that the time source %3 is working properly.\r\n
0x00000023 | The time service is now synchronizing the system time with the time source %1 with reference id %2. Current local stratum number is %3.\r\n
0x00000024 | The time service has not synchronized the system time for the last %1 seconds because none of the time service providers provided a usable time stamp. The time service will not update the local system time until it is able to synchronize with a time source. If the local system is configured to act as a time server for clients, it will stop advertising as a time source to clients after %2 seconds. The time service will continue to retry and sync time with its time sources. Check system event log for other W32time events for more details. Run 'w32tm /resync' to force an instant time synchronization. You can control the frequency of the time source rediscovery using ClockHoldoverPeriod W32time config setting. Modify the EventLogFlags W32time config setting if you wish to disable this message.\r\n
0x00000025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x00000026 | The time provider NtpClient has not received response from server %1.\r\n
0x00000027 | The time service is unable to register for network configuration change events. This may occur when TCP/IP is not correctly configured. The time service will be unable to sync time from network providers, but will still use locally installed hardware provdiers, if any are available.\r\n
0x00000028 | The time provider '%1' was stopped with error %2.\r\n
0x00000029 | The time service has been configured to use one or more input providers, however, none of the input providers are still running. The time service has no source of accurate time.\r\n
0x0000002a | The time service attempted to create a named event which was already opened. This could be the result of an attempt to compromise your system's security.\r\n
0x0000002b | The time provider '%1' returned an error when notified of a network configuration change. The error will be ignored. The error was: %2\r\n
0x0000002c | The time provider NtpClient encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002d | The time provider NtpServer encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002e | The time service encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002f | Time Provider NtpClient: No valid response has been received from manually configured peer %1 after 8 attempts to contact it. This peer will be discarded as a time source and NtpClient will attempt to discover a new peer with this DNS name. The error was: %2\r\n
0x00000030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will continue to try the DNS lookup every %3 minutes. This message will not be logged again until a successful lookup of this manually configured peer occurs. The error was: %2\r\n
0x00000031 | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will continue trying to locate an AD DC every %1 minutes. This message will not be logged again until after a domain controller is found.\r\n
0x00000032 | The time service detected a time difference of greater than %1 milliseconds for %2 seconds. The time difference might be caused by synchronization with low-accuracy time sources or by suboptimal network conditions. The time service is no longer synchronized and cannot provide the time to other clients or update the system clock. When a valid time stamp is received from a time service provider, the time service will correct itself.\r\n
0x00000033 | Time Provider NtpClient: The time sample received from peer %1 differs from the local time by %2 seconds. The observed transmission delay from the server was %3 milliseconds.\r\n
0x00000034 | The time service has set the time with offset %1 seconds.\r\n
0x00000035 | The time provider NtpClient fails sending request to server %1.\r\n
0x00000036 | The time service encountered an error while refreshing its configuration in the registry and cannot start. The error was: %1\r\n
0x0000005a | NoAuth\r\n
0x0000005b | NtDigest\r\n
0x0000005c | The peer is unreachable.\r\n
0x0000005e | The time sample was rejected because: Duplicate timestamps were received from this peer.\r\n
0x0000005f | The time sample was rejected because: Message was received out-of-order.\r\n
0x00000060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions. This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response.\r\n
0x00000061 | The time sample was rejected because: Round-trip delay too large.\r\n
0x00000062 | The time sample was rejected because: Packet not authenticated.\r\n
0x00000063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization.\r\n
0x00000064 | The time sample was rejected because: The peer's stratum is less than the host's stratum.\r\n
0x00000065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values. This may be caused by poor network conditions.\r\n
0x00000066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.%0\r\n
0x00000067 | The server fails authenticating a request with netlogon failure.\r\n
0x00000068 | The client fails sending out a request.\r\n
0x00000069 | The client fails authenticating a response with netlogon failure.\r\n
0x0000006a | The client fails authenticating a response with a bad signature.\r\n
0x0000006b | The client fails authenticating a response with a missing signature.\r\n
0x00000070 | The peer is unresolved.\r\n
0x00000081 | NtpClient was unable to set a domain peer to use as a time source because of discovery error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000082 | NtpClient was unable to set a domain peer to use as a time source because of failure in establishing  a trust relationship between this computer and the '%3' domain in order to securely synchronize time. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000083 | NtpClient was unable to set a domain peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1.\r\n
0x00000084 | NtpClient was unable to set a domain peer to use as a time source because of duplicate error on '%3'.  The same time source '%4' has been specified as manual peer in NtpServer. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000085 | NtpClient was unable to set a domain peer to use a time source because of an unexpected error.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000086 | NtpClient was unable to set a manual peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000087 | NtpClient was unable to set a manual peer to use as a time source because of duplicate error on '%3'. The same time source '%4' has been either specified as manual peer in NtpServer or selected as domain peer.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000088 | NtpClient was unable to set a manual peer to use as a time source because of an unexpected error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000089 | NtpClient succeeds in resolving manual peer %1 after a previous failure.\r\n
0x0000008a | NtpClient succeeds in resolving domain peer %1 after a previous failure.\r\n
0x0000008b | The time service has started advertising as a time source.\r\n
0x0000008c | The time service has stopped advertising as a time source because the local machine is not an Active Directory Domain Controller.\r\n
0x0000008d | The time service has stopped advertising as a time source because there are no providers running.\r\n
0x0000008e | The time service has stopped advertising as a time source because the local clock is not synchronized.\r\n
0x0000008f | The time service has started advertising as a good time source.\r\n
0x00000090 | The time service has stopped advertising as a good time source.\r\n
0x00000091 | The time service has stopped advertising as a time source.\r\n
0x00000092 | The RODC has received %1 requests in the previous %2 minutes. %3 have resulted in success, and %4 have resulted in failure.\r\n
0x0000009b | NtSignature\r\n
0x0000009c | The RODC was unable to forward a time sync request from client RID %1 because the client's RID value is too large and the domain peer (%2) does not support the uplevel timesync authentication format.\r\n
0x0000009d | The time provider NtpServer received a request from a client (%1) using a legacy protocol format. The request has been ignored per the RequireSecureTimeSyncRequests policy setting. By default, this message will be logged only once per day per unique client address.\r\n
0x0000009e | The time provider '%1' has indicated that the current hardware and operating environment is not supported and has stopped. This behavior is expected for VMICTimeProvider on non-HyperV-guest environments. This may be the expected behavior for the current provider in the current operating environment as well.\r\n
0x0000009f | W32time is unable to communicate with Netlogon Service. This failure prevents NTPClient from discovering and using domain peers, besides causing problems with correct W32time service state being advertised by Netlogon. This could be a temporary condition that resolves itself shortly. If this warning repeats over a considerable period of time, ensure the Netlogon service is running and is responsive and restart W32time service to reintiaize the overall state. The error was %1\r\n
0x00000115 | added\r\n
0x00000116 | subtracted\r\n
0x00000118 | Error %1 registering an RPC endpoint.  Please restart the Windows Time Service for it to become fully functional.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Time-Service\r\n
0x90000002 | System\r\n
0xb0000101 | W32time service has started at %1 (UTC), System Tick Count %2.%nConfiguration:%n%3%nTime Providers:%n%4Clock Rate:%5%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000102 | W32time service is stopping at %1 (UTC), System Tick Count %2 with return code: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000103 | NTP Client provider periodic status:%nNtp Client is receiving time data from the following NTP Servers: %1  and the chosen reference time server is %2. System Tick Count %3. IFTSTMP:%4.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000104 | W32time Service periodic configuration and status message%nConfiguration:%n%1%nTime Providers:%n%2%nCurrent Status:%nLeap Indicator: %3%nStratum: %4%nPrecision: %5%nRootDelay: %6%nRootDispersion: %7%nReferenceId: %8%nLast Successful Sync Time: %9 (UTC)%nSource: %10%nPoll Interval: %11%nPhase Offset: %12%nClock Rate: %13%nState Machine: %14%nTime Source Flags: %15%nServer Role: %16%nLast Sync Error: %17%nTime Since Last Good Sync: %18%nSystem Tick Count: %19%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000105 | W32time service has set the system time to %1(UTC). Previous system time was %2(UTC). System Tick Count: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000106 | W32time service has adjusted the system clock rate by %1 PPM and the new nominal clock rate is %2. Previous nominal clock rate was %3. System Tick Count: %4.%nClock adjustments below %5 PPM are not logged. Performance counters are recommended to efficiently track small adjustment values.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000107 | W32time Service configuration parameters have been updated. This may impact the fine-grained time synchronization accuracy.%nUpdated Configuration:%n%1%nUpdated Time Providers:%n%2System Tick Count: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000108 | NTP Client observed a change peer reachability. Ntp Client is now receiving time data from the following NTP Servers: %1. System Tick Count: %2.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000109 | The time service is now synchronizing the system time with the reference time source %1 with reference id %2. Current local stratum number is %3, System Tick Count: %4.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb000010a | W32time Service received notification to rediscover its time sources and/or resynchronize time. Reason Code:%1 System Tick Count: %2%nReason code description:%n0 : An explicit time resynchronization request from an administrator%n1 : Power state changes on this machine%n2 : Changes to the network interface or to the network topology%n3 : State changes within W32time that require time synchronization%nThe actions that follow this notifcation may impact fine-grained time synchronization accuracy.For more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000110 | Leap second configuration:%nEnabled: %1 (Local)%nCount: %2 (Local)%nCurrent Offset from UTC(Seconds): %3 (Local)%nRuntime state consistent with settings: %4%nNewest Leap Seconds List (Local):%n%5%nSystem Tick Count: %6.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000111 | A leap second will be %1 at %2 UTC (%3 local time). The local system data on this leap second matches with the data from the time provider %4.%nSystem Tick Count: %5.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000112 | The time provider %4 has signaled a leap second should be %1 at %2 UTC (%3 local time). However, there is no matching local system data. Please make sure you are synchronizing time from a time source that supports leap seconds and apply the latest Windows patches to avoid seeing this message.%nSystem Tick Count: %5.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000113 | Per configuration, W32time service attempted to add a leap second %1 UTC to local settings. Result: %2. System Tick Count: %3.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000114 | The local system data indicates that a leap second will be %1 at %2 UTC (%3 local time). This information is not corroborated by the current chosen time provider %4. W32time service will update the system data to excude this leap second. Please make sure you are synchronizing time from a time source that supports leap seconds and ensure you have applied the latest Windows patches. System Tick Count: %5.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000117 | W32time could not update the local system time data on leap seconds. Please make sure you are synchronizing time from a time source that supports leap seconds and ensure you have applied the latest Windows patches. System Tick Count: %1.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000001 | The time provider '%1' logged the following error: %2\r\n
0x00000002 | The time provider '%1' logged the following warning: %2\r\n
0x00000003 | The time provider '%1' logged the following message: %2\r\n
0x00000004 | The time provider '%1' failed to start due to the following error: %2\r\n
0x00000005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0x00000006 | The time service encountered an error while reading its configuration from the registry, and will continue running with its previous configuration. The error was: %1\r\n
0x00000007 | The time provider '%1' returned an error while updating its configuration. The error will be ignored. The error was: %2\r\n
0x00000008 | The time provider '%1' returned an error when notified of a polling interval change. The error will be ignored. The error was: %2\r\n
0x00000009 | The time provider '%1' returned an error when notified of a time jump. The error will be ignored. The error was: %2\r\n
0x0000000a | The time provider '%1' returned an error when asked for time samples. The error will be ignored. The error was: %2\r\n
0x0000000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is not a member of a domain. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000d | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but the computer is joined to a Windows NT 4.0 domain. Windows NT 4.0 domain controllers do not have a time service and do not support domain hierarchy as a time source. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000e | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will try again in %1 minutes.\r\n
0x0000000f | The time provider NtpClient was unable to find a domain controller to use as a time source.  NtpClient will fall back to the remaining configured time sources, if any are available. The error was: %1\r\n
0x00000010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually configured peer '%1'. This peer will not be used as a time source. The error was: %2\r\n
0x00000011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will try the DNS lookup again in %3 minutes. The error was: %2\r\n
0x00000012 | The time provider NtpClient failed to establish a trust relationship between this computer and the %1 domain in order to securely synchronize time. NtpClient will try again in %3 minutes. The error was: %2\r\n
0x00000013 | Logging was requested, but the time service encountered an error while trying to set up the log file: %1. The error was: %2. Please make sure that 'Local Service' has permission to write to the file or directory.\r\n
0x00000014 | Logging was requested, but the time service encountered an error while trying to write to the log file: %1. The error was: %2\r\n
0x00000015 | The time service is configured to use one or more input providers, however, none of the input providers are available. The time service has no source of accurate time.\r\n
0x00000016 | The time provider NtpServer encountered an error while digitally signing the NTP response for peer %1. NtpServer cannot provide secure (signed) time to the client and will ignore the request. The error was: %2\r\n
0x00000017 | The time provider NtpServer encountered an error while digitally signing the NTP response for symmetric peer %1. NtpServer cannot provide secure (signed) time to the peer and will not send a packet. The error was: %2\r\n
0x00000018 | Time Provider NtpClient: No valid response has been received from domain controller %1 after 8 attempts to contact it. This domain controller will be discarded as a time source and NtpClient will attempt to discover a new domain controller from which to synchronize. The error was: %2\r\n
0x00000019 | The time provider NtpClient cannot determine whether the response received from %1 has  a valid signature. The response will be ignored. The error was: %2\r\n
0x0000001a | Time Provider NtpClient: The response received from domain controller %1 has a bad signature. The response may have been tampered with and will be ignored.\r\n
0x0000001b | Time Provider NtpClient: The response received from domain controller %1 is missing the signature. The response may have been tampered with and will be ignored.\r\n
0x0000001c | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are accessible. NtpClient has no source of accurate time.\r\n
0x0000001d | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are currently accessible. No attempt to contact a source will be made for %1 minutes. NtpClient has no source of accurate time.\r\n
0x0000001e | The time service encountered an error while reading its configuration from the registry and cannot start. The error was: %1\r\n
0x0000001f | The time service discovered that the system time zone information was corrupted. Because many system components require valid time zone information, the time service has reset the system time zone to GMT. Use the Date/Time control panel to set the correct time zone.\r\n
0x00000020 | The time service discovered that the system time zone information was corrupted. The time service tried to reset the system time zone to GMT, but failed. The time service cannot start. The error was: %1\r\n
0x00000021 | The time service has jumped the local system clock by %1 seconds. This occurs when the time source and local system time are far enough apart that clock rate adjustments cannot be made to reach the time specified by the time source.\r\n
0x00000022 | The time service has detected that the system time needs to be  changed by %1 seconds. The time service will not change the system time by more than %2 seconds. Verify that your time and time zone are correct, and that the time source %3 is working properly.\r\n
0x00000023 | The time service is now synchronizing the system time with the time source %1 with reference id %2. Current local stratum number is %3.\r\n
0x00000024 | The time service has not synchronized the system time for the last %1 seconds because none of the time service providers provided a usable time stamp. The time service will not update the local system time until it is able to synchronize with a time source. If the local system is configured to act as a time server for clients, it will stop advertising as a time source to clients after %2 seconds. The time service will continue to retry and sync time with its time sources. Check system event log for other W32time events for more details. Run 'w32tm /resync' to force an instant time synchronization. You can control the frequency of the time source rediscovery using ClockHoldoverPeriod W32time config setting. Modify the EventLogFlags W32time config setting if you wish to disable this message.\r\n
0x00000025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x00000026 | The time provider NtpClient has not received response from server %1.\r\n
0x00000027 | The time service is unable to register for network configuration change events. This may occur when TCP/IP is not correctly configured. The time service will be unable to sync time from network providers, but will still use locally installed hardware provdiers, if any are available.\r\n
0x00000028 | The time provider '%1' was stopped with error %2.\r\n
0x00000029 | The time service has been configured to use one or more input providers, however, none of the input providers are still running. The time service has no source of accurate time.\r\n
0x0000002a | The time service attempted to create a named event which was already opened. This could be the result of an attempt to compromise your system's security.\r\n
0x0000002b | The time provider '%1' returned an error when notified of a network configuration change. The error will be ignored. The error was: %2\r\n
0x0000002c | The time provider NtpClient encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002d | The time provider NtpServer encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002e | The time service encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002f | Time Provider NtpClient: No valid response has been received from manually configured peer %1 after 8 attempts to contact it. This peer will be discarded as a time source and NtpClient will attempt to discover a new peer with this DNS name. The error was: %2\r\n
0x00000030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will continue to try the DNS lookup every %3 minutes. This message will not be logged again until a successful lookup of this manually configured peer occurs. The error was: %2\r\n
0x00000031 | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will continue trying to locate an AD DC every %1 minutes. This message will not be logged again until after a domain controller is found.\r\n
0x00000032 | The time service detected a time difference of greater than %1 milliseconds for %2 seconds. The time difference might be caused by synchronization with low-accuracy time sources or by suboptimal network conditions. The time service is no longer synchronized and cannot provide the time to other clients or update the system clock. When a valid time stamp is received from a time service provider, the time service will correct itself.\r\n
0x00000033 | Time Provider NtpClient: The time sample received from peer %1 differs from the local time by %2 seconds. The observed transmission delay from the server was %3 milliseconds.\r\n
0x00000034 | The time service has set the time with offset %1 seconds.\r\n
0x00000035 | The time provider NtpClient fails sending request to server %1.\r\n
0x00000036 | The time service encountered an error while refreshing its configuration in the registry and cannot start. The error was: %1\r\n
0x0000005a | NoAuth\r\n
0x0000005b | NtDigest\r\n
0x0000005c | The peer is unreachable.\r\n
0x0000005e | The time sample was rejected because: Duplicate timestamps were received from this peer.\r\n
0x0000005f | The time sample was rejected because: Message was received out-of-order.\r\n
0x00000060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions. This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response.\r\n
0x00000061 | The time sample was rejected because: Round-trip delay too large.\r\n
0x00000062 | The time sample was rejected because: Packet not authenticated.\r\n
0x00000063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization.\r\n
0x00000064 | The time sample was rejected because: The peer's stratum is less than the host's stratum.\r\n
0x00000065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values. This may be caused by poor network conditions.\r\n
0x00000066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.%0\r\n
0x00000067 | The server fails authenticating a request with netlogon failure.\r\n
0x00000068 | The client fails sending out a request.\r\n
0x00000069 | The client fails authenticating a response with netlogon failure.\r\n
0x0000006a | The client fails authenticating a response with a bad signature.\r\n
0x0000006b | The client fails authenticating a response with a missing signature.\r\n
0x00000070 | The peer is unresolved.\r\n
0x00000081 | NtpClient was unable to set a domain peer to use as a time source because of discovery error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000082 | NtpClient was unable to set a domain peer to use as a time source because of failure in establishing  a trust relationship between this computer and the '%3' domain in order to securely synchronize time. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000083 | NtpClient was unable to set a domain peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1.\r\n
0x00000084 | NtpClient was unable to set a domain peer to use as a time source because of duplicate error on '%3'.  The same time source '%4' has been specified as manual peer in NtpServer. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000085 | NtpClient was unable to set a domain peer to use a time source because of an unexpected error.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000086 | NtpClient was unable to set a manual peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000087 | NtpClient was unable to set a manual peer to use as a time source because of duplicate error on '%3'. The same time source '%4' has been either specified as manual peer in NtpServer or selected as domain peer.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000088 | NtpClient was unable to set a manual peer to use as a time source because of an unexpected error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000089 | NtpClient succeeds in resolving manual peer %1 after a previous failure.\r\n
0x0000008a | NtpClient succeeds in resolving domain peer %1 after a previous failure.\r\n
0x0000008b | The time service has started advertising as a time source.\r\n
0x0000008c | The time service has stopped advertising as a time source because the local machine is not an Active Directory Domain Controller.\r\n
0x0000008d | The time service has stopped advertising as a time source because there are no providers running.\r\n
0x0000008e | The time service has stopped advertising as a time source because the local clock is not synchronized.\r\n
0x0000008f | The time service has started advertising as a good time source.\r\n
0x00000090 | The time service has stopped advertising as a good time source.\r\n
0x00000091 | The time service has stopped advertising as a time source.\r\n
0x00000092 | The RODC has received %1 requests in the previous %2 minutes. %3 have resulted in success, and %4 have resulted in failure.\r\n
0x0000009b | NtSignature\r\n
0x0000009c | The RODC was unable to forward a time sync request from client RID %1 because the client's RID value is too large and the domain peer (%2) does not support the uplevel timesync authentication format.\r\n
0x0000009d | The time provider NtpServer received a request from a client (%1) using a legacy protocol format. The request has been ignored per the RequireSecureTimeSyncRequests policy setting. By default, this message will be logged only once per day per unique client address.\r\n
0x0000009e | The time provider '%1' has indicated that the current hardware and operating environment is not supported and has stopped. This behavior is expected for VMICTimeProvider on non-HyperV-guest environments. This may be the expected behavior for the current provider in the current operating environment as well.\r\n
0x0000009f | W32time is unable to communicate with Netlogon Service. This failure prevents NTPClient from discovering and using domain peers, besides causing problems with correct W32time service state being advertised by Netlogon. This could be a temporary condition that resolves itself shortly. If this warning repeats over a considerable period of time, ensure the Netlogon service is running and is responsive and restart W32time service to reintiaize the overall state. The error was %1\r\n
0x00000115 | added\r\n
0x00000116 | subtracted\r\n
0x00000118 | Error %1 registering an RPC endpoint.  Please restart the Windows Time Service for it to become fully functional.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Time-Service\r\n
0x90000002 | System\r\n
0xb0000101 | W32time service has started at %1 (UTC), System Tick Count %2.%nConfiguration:%n%3%nTime Providers:%n%4Clock Rate:%5%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000102 | W32time service is stopping at %1 (UTC), System Tick Count %2 with return code: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000103 | NTP Client provider periodic status:%nNtp Client is receiving time data from the following NTP Servers: %1  and the chosen reference time server is %2. System Tick Count %3. IFTSTMP:%4.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000104 | W32time Service periodic configuration and status message%nConfiguration:%n%1%nTime Providers:%n%2%nCurrent Status:%nLeap Indicator: %3%nStratum: %4%nPrecision: %5%nRootDelay: %6%nRootDispersion: %7%nReferenceId: %8%nLast Successful Sync Time: %9 (UTC)%nSource: %10%nPoll Interval: %11%nPhase Offset: %12%nClock Rate: %13%nState Machine: %14%nTime Source Flags: %15%nServer Role: %16%nLast Sync Error: %17%nTime Since Last Good Sync: %18%nSystem Tick Count: %19%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000105 | W32time service has set the system time to %1(UTC). Previous system time was %2(UTC). System Tick Count: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000106 | W32time service has adjusted the system clock rate by %1 PPM and the new nominal clock rate is %2. Previous nominal clock rate was %3. System Tick Count: %4.%nClock adjustments below %5 PPM are not logged. Performance counters are recommended to efficiently track small adjustment values.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000107 | W32time Service configuration parameters have been updated. This may impact the fine-grained time synchronization accuracy.%nUpdated Configuration:%n%1%nUpdated Time Providers:%n%2System Tick Count: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000108 | NTP Client observed a change peer reachability. Ntp Client is now receiving time data from the following NTP Servers: %1. System Tick Count: %2.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000109 | The time service is now synchronizing the system time with the reference time source %1 with reference id %2. Current local stratum number is %3, System Tick Count: %4.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb000010a | W32time Service received notification to rediscover its time sources and/or resynchronize time. Reason Code:%1 System Tick Count: %2%nReason code description:%n0 : An explicit time resynchronization request from an administrator%n1 : Power state changes on this machine%n2 : Changes to the network interface or to the network topology%n3 : State changes within W32time that require time synchronization%nThe actions that follow this notifcation may impact fine-grained time synchronization accuracy.For more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb000010b | NTP provider is receiving timestamps from the network stack. These typically help reduce the jitter in time error calculations and improve time sync accuracy.%nCurrent Tick Count:%1%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb000010c | NTP provider is not receiving any timestamps from the network stack, which may result in lowered time sync accuracy. This is the default configuration and the behavior on service startup. This can also occur if there are conflicting settings for a NIC or due to actual runtime issues.%nCurrent Tick Count:%1%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000110 | Leap second configuration:%nEnabled: %1 (Local)%nCount: %2 (Local)%nCurrent Offset from UTC(Seconds): %3 (Local)%nRuntime state consistent with settings: %4%nNewest Leap Seconds List (Local):%n%5%nSystem Tick Count: %6.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000111 | A leap second will be %1 at %2 UTC (%3 local time). The local system data on this leap second matches with the data from the time provider %4.%nSystem Tick Count: %5.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000112 | The time provider %4 has signaled a leap second should be %1 at %2 UTC (%3 local time). However, there is no matching local system data. Please make sure you are synchronizing time from a time source that supports leap seconds and apply the latest Windows patches to avoid seeing this message.%nSystem Tick Count: %5.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000113 | Per configuration, W32time service attempted to add a leap second %1 UTC to local settings. Result: %2. System Tick Count: %3.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000114 | The local system data indicates that a leap second will be %1 at %2 UTC (%3 local time). This information is not corroborated by the current chosen time provider %4. W32time service will update the system data to excude this leap second. Please make sure you are synchronizing time from a time source that supports leap seconds and ensure you have applied the latest Windows patches. System Tick Count: %5.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000117 | W32time could not update the local system time data on leap seconds. Please make sure you are synchronizing time from a time source that supports leap seconds and ensure you have applied the latest Windows patches. System Tick Count: %1.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000001 | The time provider '%1' logged the following error: %2\r\n
0x00000002 | The time provider '%1' logged the following warning: %2\r\n
0x00000003 | The time provider '%1' logged the following message: %2\r\n
0x00000004 | The time provider '%1' failed to start due to the following error: %2\r\n
0x00000005 | The time provider '%1' returned the following error during shutdown: %2\r\n
0x00000006 | The time service encountered an error while reading its configuration from the registry, and will continue running with its previous configuration. The error was: %1\r\n
0x00000007 | The time provider '%1' returned an error while updating its configuration. The error will be ignored. The error was: %2\r\n
0x00000008 | The time provider '%1' returned an error when notified of a polling interval change. The error will be ignored. The error was: %2\r\n
0x00000009 | The time provider '%1' returned an error when notified of a time jump. The error will be ignored. The error was: %2\r\n
0x0000000a | The time provider '%1' returned an error when asked for time samples. The error will be ignored. The error was: %2\r\n
0x0000000b | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is not a member of a domain. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000c | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000d | Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but the computer is joined to a Windows NT 4.0 domain. Windows NT 4.0 domain controllers do not have a time service and do not support domain hierarchy as a time source. NtpClient will attempt to use an alternate configured external time source if available. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.\r\n
0x0000000e | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will try again in %1 minutes.\r\n
0x0000000f | The time provider NtpClient was unable to find a domain controller to use as a time source.  NtpClient will fall back to the remaining configured time sources, if any are available. The error was: %1\r\n
0x00000010 | Time Provider NtpClient: An unexpected error occurred during DNS lookup of the manually configured peer '%1'. This peer will not be used as a time source. The error was: %2\r\n
0x00000011 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will try the DNS lookup again in %3 minutes. The error was: %2\r\n
0x00000012 | The time provider NtpClient failed to establish a trust relationship between this computer and the %1 domain in order to securely synchronize time. NtpClient will try again in %3 minutes. The error was: %2\r\n
0x00000013 | Logging was requested, but the time service encountered an error while trying to set up the log file: %1. The error was: %2. Please make sure that 'Local Service' has permission to write to the file or directory.\r\n
0x00000014 | Logging was requested, but the time service encountered an error while trying to write to the log file: %1. The error was: %2\r\n
0x00000015 | The time service is configured to use one or more input providers, however, none of the input providers are available. The time service has no source of accurate time.\r\n
0x00000016 | The time provider NtpServer encountered an error while digitally signing the NTP response for peer %1. NtpServer cannot provide secure (signed) time to the client and will ignore the request. The error was: %2\r\n
0x00000017 | The time provider NtpServer encountered an error while digitally signing the NTP response for symmetric peer %1. NtpServer cannot provide secure (signed) time to the peer and will not send a packet. The error was: %2\r\n
0x00000018 | Time Provider NtpClient: No valid response has been received from domain controller %1 after 8 attempts to contact it. This domain controller will be discarded as a time source and NtpClient will attempt to discover a new domain controller from which to synchronize. The error was: %2\r\n
0x00000019 | The time provider NtpClient cannot determine whether the response received from %1 has  a valid signature. The response will be ignored. The error was: %2\r\n
0x0000001a | Time Provider NtpClient: The response received from domain controller %1 has a bad signature. The response may have been tampered with and will be ignored.\r\n
0x0000001b | Time Provider NtpClient: The response received from domain controller %1 is missing the signature. The response may have been tampered with and will be ignored.\r\n
0x0000001c | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are accessible. NtpClient has no source of accurate time.\r\n
0x0000001d | The time provider NtpClient is configured to acquire time from one or more time sources, however none of the sources are currently accessible. No attempt to contact a source will be made for %1 minutes. NtpClient has no source of accurate time.\r\n
0x0000001e | The time service encountered an error while reading its configuration from the registry and cannot start. The error was: %1\r\n
0x0000001f | The time service discovered that the system time zone information was corrupted. Because many system components require valid time zone information, the time service has reset the system time zone to GMT. Use the Date/Time control panel to set the correct time zone.\r\n
0x00000020 | The time service discovered that the system time zone information was corrupted. The time service tried to reset the system time zone to GMT, but failed. The time service cannot start. The error was: %1\r\n
0x00000021 | The time service has jumped the local system clock by %1 seconds. This occurs when the time source and local system time are far enough apart that clock rate adjustments cannot be made to reach the time specified by the time source.\r\n
0x00000022 | The time service has detected that the system time needs to be  changed by %1 seconds. The time service will not change the system time by more than %2 seconds. Verify that your time and time zone are correct, and that the time source %3 is working properly.\r\n
0x00000023 | The time service is now synchronizing the system time with the time source %1 with reference id %2. Current local stratum number is %3.\r\n
0x00000024 | The time service has not synchronized the system time for the last %1 seconds because none of the time service providers provided a usable time stamp. The time service will not update the local system time until it is able to synchronize with a time source. If the local system is configured to act as a time server for clients, it will stop advertising as a time source to clients after %2 seconds. The time service will continue to retry and sync time with its time sources. Check system event log for other W32time events for more details. Run 'w32tm /resync' to force an instant time synchronization. You can control the frequency of the time source rediscovery using ClockHoldoverPeriod W32time config setting. Modify the EventLogFlags W32time config setting if you wish to disable this message.\r\n
0x00000025 | The time provider NtpClient is currently receiving valid time data from %1.\r\n
0x00000026 | The time provider NtpClient has not received response from server %1.\r\n
0x00000027 | The time service is unable to register for network configuration change events. This may occur when TCP/IP is not correctly configured. The time service will be unable to sync time from network providers, but will still use locally installed hardware provdiers, if any are available.\r\n
0x00000028 | The time provider '%1' was stopped with error %2.\r\n
0x00000029 | The time service has been configured to use one or more input providers, however, none of the input providers are still running. The time service has no source of accurate time.\r\n
0x0000002a | The time service attempted to create a named event which was already opened. This could be the result of an attempt to compromise your system's security.\r\n
0x0000002b | The time provider '%1' returned an error when notified of a network configuration change. The error will be ignored. The error was: %2\r\n
0x0000002c | The time provider NtpClient encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002d | The time provider NtpServer encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002e | The time service encountered an error and was forced to shut down. The error was: %1\r\n
0x0000002f | Time Provider NtpClient: No valid response has been received from manually configured peer %1 after 8 attempts to contact it. This peer will be discarded as a time source and NtpClient will attempt to discover a new peer with this DNS name. The error was: %2\r\n
0x00000030 | Time Provider NtpClient: An error occurred during DNS lookup of the manually configured peer '%1'. NtpClient will continue to try the DNS lookup every %3 minutes. This message will not be logged again until a successful lookup of this manually configured peer occurs. The error was: %2\r\n
0x00000031 | The time provider NtpClient was unable to find a domain controller to use as a time source. NtpClient will continue trying to locate an AD DC every %1 minutes. This message will not be logged again until after a domain controller is found.\r\n
0x00000032 | The time service detected a time difference of greater than %1 milliseconds for %2 seconds. The time difference might be caused by synchronization with low-accuracy time sources or by suboptimal network conditions. The time service is no longer synchronized and cannot provide the time to other clients or update the system clock. When a valid time stamp is received from a time service provider, the time service will correct itself.\r\n
0x00000033 | Time Provider NtpClient: The time sample received from peer %1 differs from the local time by %2 seconds. The observed transmission delay from the server was %3 milliseconds.\r\n
0x00000034 | The time service has set the time with offset %1 seconds.\r\n
0x00000035 | The time provider NtpClient fails sending request to server %1.\r\n
0x00000036 | The time service encountered an error while refreshing its configuration in the registry and cannot start. The error was: %1\r\n
0x0000005a | NoAuth\r\n
0x0000005b | NtDigest\r\n
0x0000005c | The peer is unreachable.\r\n
0x0000005e | The time sample was rejected because: Duplicate timestamps were received from this peer.\r\n
0x0000005f | The time sample was rejected because: Message was received out-of-order.\r\n
0x00000060 | The time sample was rejected because: The peer is not synchronized, or reachability has been lost in one, or both, directions. This may also indicate that the peer has incorrectly sent an NTP request instead of an NTP response.\r\n
0x00000061 | The time sample was rejected because: Round-trip delay too large.\r\n
0x00000062 | The time sample was rejected because: Packet not authenticated.\r\n
0x00000063 | The time sample was rejected because: The peer is not synchronized, or it has been too long since the peer's last synchronization.\r\n
0x00000064 | The time sample was rejected because: The peer's stratum is less than the host's stratum.\r\n
0x00000065 | The time sample was rejected because: Packet contains unreasonable root delay or root dispersion values. This may be caused by poor network conditions.\r\n
0x00000066 | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start.%0\r\n
0x00000067 | The server fails authenticating a request with netlogon failure.\r\n
0x00000068 | The client fails sending out a request.\r\n
0x00000069 | The client fails authenticating a response with netlogon failure.\r\n
0x0000006a | The client fails authenticating a response with a bad signature.\r\n
0x0000006b | The client fails authenticating a response with a missing signature.\r\n
0x00000070 | The peer is unresolved.\r\n
0x00000081 | NtpClient was unable to set a domain peer to use as a time source because of discovery error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000082 | NtpClient was unable to set a domain peer to use as a time source because of failure in establishing  a trust relationship between this computer and the '%3' domain in order to securely synchronize time. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000083 | NtpClient was unable to set a domain peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1.\r\n
0x00000084 | NtpClient was unable to set a domain peer to use as a time source because of duplicate error on '%3'.  The same time source '%4' has been specified as manual peer in NtpServer. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000085 | NtpClient was unable to set a domain peer to use a time source because of an unexpected error.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000086 | NtpClient was unable to set a manual peer to use as a time source because of DNS resolution error on '%3'. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000087 | NtpClient was unable to set a manual peer to use as a time source because of duplicate error on '%3'. The same time source '%4' has been either specified as manual peer in NtpServer or selected as domain peer.  NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000088 | NtpClient was unable to set a manual peer to use as a time source because of an unexpected error. NtpClient will try again in %2 minutes and double the reattempt interval thereafter. The error was: %1\r\n
0x00000089 | NtpClient succeeds in resolving manual peer %1 after a previous failure.\r\n
0x0000008a | NtpClient succeeds in resolving domain peer %1 after a previous failure.\r\n
0x0000008b | The time service has started advertising as a time source.\r\n
0x0000008c | The time service has stopped advertising as a time source because the local machine is not an Active Directory Domain Controller.\r\n
0x0000008d | The time service has stopped advertising as a time source because there are no providers running.\r\n
0x0000008e | The time service has stopped advertising as a time source because the local clock is not synchronized.\r\n
0x0000008f | The time service has started advertising as a good time source.\r\n
0x00000090 | The time service has stopped advertising as a good time source.\r\n
0x00000091 | The time service has stopped advertising as a time source.\r\n
0x00000092 | The RODC has received %1 requests in the previous %2 minutes. %3 have resulted in success, and %4 have resulted in failure.\r\n
0x0000009b | NtSignature\r\n
0x0000009c | The RODC was unable to forward a time sync request from client RID %1 because the client's RID value is too large and the domain peer (%2) does not support the uplevel timesync authentication format.\r\n
0x0000009d | The time provider NtpServer received a request from a client (%1) using a legacy protocol format. The request has been ignored per the RequireSecureTimeSyncRequests policy setting. By default, this message will be logged only once per day per unique client address.\r\n
0x0000009e | The time provider '%1' has indicated that the current hardware and operating environment is not supported and has stopped. This behavior is expected for VMICTimeProvider on non-HyperV-guest environments. This may be the expected behavior for the current provider in the current operating environment as well.\r\n
0x0000009f | W32time is unable to communicate with Netlogon Service. This failure prevents NTPClient from discovering and using domain peers, besides causing problems with correct W32time service state being advertised by Netlogon. This could be a temporary condition that resolves itself shortly. If this warning repeats over a considerable period of time, ensure the Netlogon service is running and is responsive and restart W32time service to reintiaize the overall state. The error was %1\r\n
0x00000115 | added\r\n
0x00000116 | subtracted\r\n
0x00000118 | Error %1 registering an RPC endpoint.  Please restart the Windows Time Service for it to become fully functional.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Time-Service\r\n
0x90000002 | System\r\n
0xb0000101 | W32time service has started at %1 (UTC), System Tick Count %2.%nConfiguration:%n%3%nTime Providers:%n%4Clock Rate:%5%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000102 | W32time service is stopping at %1 (UTC), System Tick Count %2 with return code: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000103 | NTP Client provider periodic status:%nNtp Client is receiving time data from the following NTP Servers: %1  and the chosen reference time server is %2. System Tick Count %3. IFTSTMP:%4.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000104 | W32time Service periodic configuration and status message%nConfiguration:%n%1%nTime Providers:%n%2%nCurrent Status:%nLeap Indicator: %3%nStratum: %4%nPrecision: %5%nRootDelay: %6%nRootDispersion: %7%nReferenceId: %8%nLast Successful Sync Time: %9 (UTC)%nSource: %10%nPoll Interval: %11%nPhase Offset: %12%nClock Rate: %13%nState Machine: %14%nTime Source Flags: %15%nServer Role: %16%nLast Sync Error: %17%nTime Since Last Good Sync: %18%nSystem Tick Count: %19%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000105 | W32time service has set the system time to %1(UTC). Previous system time was %2(UTC). System Tick Count: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000106 | W32time service has adjusted the system clock rate by %1 PPM and the new nominal clock rate is %2. Previous nominal clock rate was %3. System Tick Count: %4.%nClock adjustments below %5 PPM are not logged. Performance counters are recommended to efficiently track small adjustment values.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000107 | W32time Service configuration parameters have been updated. This may impact the fine-grained time synchronization accuracy.%nUpdated Configuration:%n%1%nUpdated Time Providers:%n%2System Tick Count: %3%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000108 | NTP Client observed a change peer reachability. Ntp Client is now receiving time data from the following NTP Servers: %1. System Tick Count: %2.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000109 | The time service is now synchronizing the system time with the reference time source %1 with reference id %2. Current local stratum number is %3, System Tick Count: %4.%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb000010a | W32time Service received notification to rediscover its time sources and/or resynchronize time. Reason Code:%1 System Tick Count: %2%nReason code description:%n0 : An explicit time resynchronization request from an administrator%n1 : Power state changes on this machine%n2 : Changes to the network interface or to the network topology%n3 : State changes within W32time that require time synchronization%nThe actions that follow this notifcation may impact fine-grained time synchronization accuracy.For more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb000010b | NTP provider is receiving timestamps from the network stack. These typically help reduce the jitter in time error calculations and improve time sync accuracy.%nCurrent Tick Count:%1%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb000010c | NTP provider is not receiving any timestamps from the network stack, which may result in lowered time sync accuracy. This is the default configuration and the behavior on service startup. This can also occur if there are conflicting settings for a NIC or due to actual runtime issues.%nCurrent Tick Count:%1%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000110 | Leap second configuration:%nEnabled: %1 (Local)%nCount: %2 (Local)%nCurrent Offset from UTC(Seconds): %3 (Local)%nRuntime state consistent with settings: %4%nNewest Leap Seconds List (Local):%n%5%nSystem Tick Count: %6.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000111 | A leap second will be %1 at %2 UTC (%3 local time). The local system data on this leap second matches with the data from the time provider %4.%nSystem Tick Count: %5.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000112 | The time provider %4 has signaled a leap second should be %1 at %2 UTC (%3 local time). However, there is no matching local system data. Please make sure you are synchronizing time from a time source that supports leap seconds and apply the latest Windows patches to avoid seeing this message.%nSystem Tick Count: %5.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000113 | Per configuration, W32time service attempted to add a leap second %1 UTC to local settings. Result: %2. System Tick Count: %3.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000114 | The local system data indicates that a leap second will be %1 at %2 UTC (%3 local time). This information is not corroborated by the current chosen time provider %4. W32time service will update the system data to excude this leap second. Please make sure you are synchronizing time from a time source that supports leap seconds and ensure you have applied the latest Windows patches. System Tick Count: %5.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000117 | W32time could not update the local system time data on leap seconds. Please make sure you are synchronizing time from a time source that supports leap seconds and ensure you have applied the latest Windows patches. System Tick Count: %1.%n%nFor more information, see https://go.microsoft.com/fwlink/?linkid=845961.\r\n
0xb0000119 | The local system clock requires a frequency correction of approximately %1 parts per million (PPM). This frequency correction averaged %2 PPM over the past %3 minutes. The system time can drift approx %4 seconds per day if the system clock is undisciplined. This drift can vary over time depending on external and internal factors.\r\n
0xb000011a | The local system clock required an average frequency correction of %1 parts per million (PPM) over the past %2 minutes. The system time can drift approx %3 seconds per day if the system clock is undisciplined. This is larger than the suggested upper limit of 1 second/day for high accuracy applications. A highly available good time source is necessary to run high accuracy applications on this machine. Ignore this message if your application does not require high accuracy time.\r\n
0xb000011b | Inconsistent timekeeping or a time jump has been detected.%nExpected System Time:%1%nActual System Time:%2%nSystem Tick Count:%3%n%nThe system time was changed by a different application or the underlying hardware has potential issues with keeping time reasonably accurately. Windows time service will attempt to correct this inaccuracy within the current operational parameters, when reliable time data becomes available next.\r\n
