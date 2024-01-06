## services.exe

Path: %SystemRoot%\system32\services.exe

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x40001b7b | The %1 service was successfully sent a %2 control.\r\n
0x40001b7c | The %1 service entered the %2 state.\r\n
0x40001b80 | The start type of the %1 service was changed from %2 to %3.\r\n
0x40001b82 | The %1 service was successfully sent a %2 control.%n%n The reason specified was: %3 [%4]%n%n Comment: %5\r\n
0x80001b7f | A service process other than the one launched by the Service Control Manager connected when starting the %1 service.  The Service Control Manager launched process %2 and process %3 connected instead.%n%n  Note that if this service is configured to start under a debugger, this behavior is expected.\r\n
0x80001b84 | The following service is taking more than %2 minutes to start and may have stopped responding: %1%n%nContact your system administrator or service vendor for approximate startup times for this service.%n%nIf you think this service might be slowing system response or logon time, talk to your system administrator about whether the service should be disabled until the problem is identified.%n%nYou may have to restart the computer in safe mode before you can disable the service.\r\n
0x90000001 | Microsoft Windows Services Performance Diagnostic Provider\r\n
0x91000001 | Microsoft Windows Services Svchost Performance Diagnostic Provider\r\n
0x92000001 | Service Control Manager Eventlog Provider\r\n
0xc0001b58 | The %1 service failed to start due to the following error: %n%2\r\n
0xc0001b59 | The %1 service depends on the %2 service which failed to start because of the following error: %n%3\r\n
0xc0001b5a | The %1 service depends on the %2 group and no member of this group started.\r\n
0xc0001b5b | The %1 service depends the following service: %2. This service might not be installed.\r\n
0xc0001b5d | The %1 call failed with the following error: %n%2\r\n
0xc0001b5e | The %1 call failed for %2 with the following error: %n%3\r\n
0xc0001b5f | The system reverted to its last known good configuration.  The system is restarting....\r\n
0xc0001b60 | No backslash is in the account name. The account name must be in the form: domain\user.\r\n
0xc0001b61 | A timeout was reached (%1 milliseconds) while waiting for the %2 service to connect.\r\n
0xc0001b62 | A timeout (%1 milliseconds) was reached while waiting for ReadFile.\r\n
0xc0001b63 | A timeout (%1 milliseconds) was reached while waiting for a transaction response from the %2 service.\r\n
0xc0001b64 | The message returned in the transaction has incorrect size.\r\n
0xc0001b65 | Logon attempt with current password failed with the following error: %n%1\r\n
0xc0001b66 | Second logon attempt with old password also failed with the following error: %n%1\r\n
0xc0001b67 | Boot-start or system-start driver (%1) must not depend on a service.\r\n
0xc0001b68 | The %1 service has reported an invalid current state %2.\r\n
0xc0001b69 | Detected circular dependencies demand starting %1. Check the service dependency tree.\r\n
0xc0001b6a | Detected circular dependencies auto-starting services. Check the service dependency tree.\r\n
0xc0001b6b | The %1 service depends on a service in a group which starts later. Change the order in the service dependency tree to ensure that all services required to start this service are starting before this service is started.\r\n
0xc0001b6c | The %1 service depends on a group which starts later. Change the order in the service dependency tree to ensure that all services required to start this service are starting before this service is started.\r\n
0xc0001b6d | About to revert to the last known good configuration because the %1 service failed to start.\r\n
0xc0001b6e | The %1 service hung on starting.\r\n
0xc0001b6f | The %1 service terminated with the following error: %n%2\r\n
0xc0001b70 | The %1 service terminated with service-specific error %2.\r\n
0xc0001b71 | At least one service or driver failed during system startup.  Use Event Viewer to examine the event log for details.\r\n
0xc0001b72 | The following boot-start or system-start driver(s) failed to load: %1\r\n
0xc0001b73 | Windows could not be started as configured. Starting Windows using a previous working configuration.\r\n
0xc0001b74 | The %1 Registry key denied access to SYSTEM account programs so the Service Control Manager took ownership of the Registry key.\r\n
0xc0001b75 | Service Control Manager %0\r\n
0xc0001b76 | The %1 service is marked as an interactive service.  However, the system is configured to not allow interactive services.  This service may not function properly.\r\n
0xc0001b77 | The %1 service terminated unexpectedly.  It has done this %2 time(s).  The following corrective action will be taken in %3 milliseconds: %5.\r\n
0xc0001b78 | The Service Control Manager tried to take a corrective action (%2) after the unexpected termination of the %3 service, but this action failed with the following error: %n%4\r\n
0xc0001b79 | The Service Control Manager did not initialize successfully. The security configuration server (scesrv.dll) failed to initialize with error %1.  The system is restarting...\r\n
0xc0001b7a | The %1 service terminated unexpectedly.  It has done this %2 time(s).\r\n
0xc0001b7d | The Service Control Manager encountered an error undoing a configuration change to the %1 service.  The service's %2 is currently in an unpredictable state.  If you do not correct this configuration, you may not be able to restart the %1 service or may encounter other errors.  To ensure that the service is configured properly, use the Services snap-in in Microsoft Management Console (MMC).\r\n
0xc0001b7e | The %1 service was unable to log on as %2 with the currently configured password due to the following error: %n%3%n%nTo ensure that the service is configured properly, use the Services snap-in in Microsoft Management Console (MMC).\r\n
0xc0001b81 | The %1 service was unable to log on as %2 with the currently configured password due to the following error: %nLogon failure: the user has not been granted the requested logon type at this computer.%n %nService: %1 %nDomain and account: %2%n %nThis service account does not have the required user right "Log on as a service."%n %nUser Action%n %nAssign "Log on as a service" to the service account on this computer. You can use Local Security Settings (Secpol.msc) to do this. If this computer is a node in a cluster, check that this user right is assigned to the Cluster service account on all nodes in the cluster.%n %nIf you have already assigned this user right to the service account, and the user right appears to be removed, check with your domain administrator to find out if a Group Policy object associated with this node might be removing the right.\r\n
0xc0001b83 | The %1 service did not shut down properly after receiving a preshutdown control.\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x10000031 | Response Time\r\n
0x12000038 | Classic\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x40001b7b | The %1 service was successfully sent a %2 control.\r\n
0x40001b7c | The %1 service entered the %2 state.\r\n
0x40001b80 | The start type of the %1 service was changed from %2 to %3.\r\n
0x40001b82 | The %1 service was successfully sent a %2 control.%n%n The reason specified was: %3 [%4]%n%n Comment: %5\r\n
0x40001b85 | A service was installed in the system.%n%nService Name:  %1%nService File Name:  %2%nService Type:  %3%nService Start Type:  %4%nService Account:  %5\r\n
0x50000004 | Information\r\n
0x80001b7f | A service process other than the one launched by the Service Control Manager connected when starting the %1 service.  The Service Control Manager launched process %2 and process %3 connected instead.%n%n  Note that if this service is configured to start under a debugger, this behavior is expected.\r\n
0x80001b84 | The following service is taking more than %2 minutes to start and may have stopped responding: %1%n%nContact your system administrator or service vendor for approximate startup times for this service.%n%nIf you think this service might be slowing system response or logon time, talk to your system administrator about whether the service should be disabled until the problem is identified.%n%nYou may have to restart the computer in safe mode before you can disable the service.\r\n
0x90000001 | Microsoft-Windows-Service Control Manager Performance Diagnostic Provider\r\n
0x91000001 | Microsoft-Windows-Svchost Performance Diagnostic Provider\r\n
0x92000001 | Microsoft-Windows-Service Control Manager\r\n
0x92000002 | System\r\n
0xc0001b58 | The %1 service failed to start due to the following error: %n%2\r\n
0xc0001b59 | The %1 service depends on the %2 service which failed to start because of the following error: %n%3\r\n
0xc0001b5a | The %1 service depends on the %2 group and no member of this group started.\r\n
0xc0001b5b | The %1 service depends the following service: %2. This service might not be installed.\r\n
0xc0001b5d | The %1 call failed with the following error: %n%2\r\n
0xc0001b5e | The %1 call failed for %2 with the following error: %n%3\r\n
0xc0001b5f | The system reverted to its last known good configuration.  The system is restarting....\r\n
0xc0001b60 | No backslash is in the account name. The account name must be in the form: domain\user.\r\n
0xc0001b61 | A timeout was reached (%1 milliseconds) while waiting for the %2 service to connect.\r\n
0xc0001b62 | A timeout (%1 milliseconds) was reached while waiting for ReadFile.\r\n
0xc0001b63 | A timeout (%1 milliseconds) was reached while waiting for a transaction response from the %2 service.\r\n
0xc0001b64 | The message returned in the transaction has incorrect size.\r\n
0xc0001b65 | Logon attempt with current password failed with the following error: %n%1\r\n
0xc0001b66 | Second logon attempt with old password also failed with the following error: %n%1\r\n
0xc0001b68 | The %1 service has reported an invalid current state %2.\r\n
0xc0001b69 | Detected circular dependencies demand starting %1. Check the service dependency tree.\r\n
0xc0001b6a | Detected circular dependencies auto-starting services. Check the service dependency tree.\r\n
0xc0001b6b | The %1 service depends on a service in a group which starts later. Change the order in the service dependency tree to ensure that all services required to start this service are starting before this service is started.\r\n
0xc0001b6c | The %1 service depends on a group which starts later. Change the order in the service dependency tree to ensure that all services required to start this service are starting before this service is started.\r\n
0xc0001b6d | About to revert to the last known good configuration because the %1 service failed to start.\r\n
0xc0001b6e | The %1 service hung on starting.\r\n
0xc0001b6f | The %1 service terminated with the following error: %n%2\r\n
0xc0001b70 | The %1 service terminated with service-specific error %2.\r\n
0xc0001b72 | The following boot-start or system-start driver(s) failed to load: %1\r\n
0xc0001b73 | Windows could not be started as configured. Starting Windows using a previous working configuration.\r\n
0xc0001b74 | The %1 Registry key denied access to SYSTEM account programs so the Service Control Manager took ownership of the Registry key.\r\n
0xc0001b75 | Service Control Manager %0\r\n
0xc0001b76 | The %1 service is marked as an interactive service.  However, the system is configured to not allow interactive services.  This service may not function properly.\r\n
0xc0001b77 | The %1 service terminated unexpectedly.  It has done this %2 time(s).  The following corrective action will be taken in %3 milliseconds: %5.\r\n
0xc0001b78 | The Service Control Manager tried to take a corrective action (%2) after the unexpected termination of the %3 service, but this action failed with the following error: %n%4\r\n
0xc0001b7a | The %1 service terminated unexpectedly.  It has done this %2 time(s).\r\n
0xc0001b7d | The Service Control Manager encountered an error undoing a configuration change to the %1 service.  The service's %2 is currently in an unpredictable state.  If you do not correct this configuration, you may not be able to restart the %1 service or may encounter other errors.  To ensure that the service is configured properly, use the Services snap-in in Microsoft Management Console (MMC).\r\n
0xc0001b7e | The %1 service was unable to log on as %2 with the currently configured password due to the following error: %n%3%n%nTo ensure that the service is configured properly, use the Services snap-in in Microsoft Management Console (MMC).\r\n
0xc0001b81 | The %1 service was unable to log on as %2 with the currently configured password due to the following error: %nLogon failure: the user has not been granted the requested logon type at this computer.%n %nService: %1 %nDomain and account: %2%n %nThis service account does not have the required user right "Log on as a service."%n %nUser Action%n %nAssign "Log on as a service" to the service account on this computer. You can use Local Security Settings (Secpol.msc) to do this. If this computer is a node in a cluster, check that this user right is assigned to the Cluster service account on all nodes in the cluster.%n %nIf you have already assigned this user right to the service account, and the user right appears to be removed, check with your domain administrator to find out if a Group Policy object associated with this node might be removing the right.\r\n
0xc0001b83 | The %1 service did not shut down properly after receiving a preshutdown control.\r\n

### 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0x10000031 | Response Time\r\n
0x12000038 | Classic\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x40001b7b | The %1 service was successfully sent a %2 control.\r\n
0x40001b7c | The %1 service entered the %2 state.\r\n
0x40001b80 | The start type of the %1 service was changed from %2 to %3.\r\n
0x40001b82 | The %1 service was successfully sent a %2 control.%n%n The reason specified was: %3 [%4]%n%n Comment: %5\r\n
0x40001b85 | A service was installed in the system.%n%nService Name:  %1%nService File Name:  %2%nService Type:  %3%nService Start Type:  %4%nService Account:  %5\r\n
0x50000004 | Information\r\n
0x80001b7f | A service process other than the one launched by the Service Control Manager connected when starting the %1 service.  The Service Control Manager launched process %2 and process %3 connected instead.%n%n  Note that if this service is configured to start under a debugger, this behavior is expected.\r\n
0x80001b84 | The following service is taking more than %2 minutes to start and may have stopped responding: %1%n%nContact your system administrator or service vendor for approximate startup times for this service.%n%nIf you think this service might be slowing system response or logon time, talk to your system administrator about whether the service should be disabled until the problem is identified.%n%nYou may have to restart the computer in safe mode before you can disable the service.\r\n
0x80001b86 | The following service has repeatedly stopped responding to service control requests: %1%n%nContact the service vendor or the system administrator about whether to disable this service until the problem is identified.%n%nYou may have to restart the computer in safe mode before you can disable the service.\r\n
0x80001b87 | The following services failed to start during a run level switch: %n%n%1%n%nPlease start the services manually and retry the run level switch again or contact the service vendor %nor administrator.\r\n
0x80001b88 | A run level switch failed. The %1 service did not stop correctly %nwith the following error: %n%n%2%n%nPlease stop this service manually and retry the run level switch again or contact the service vendor %nor administrator.\r\n
0x90000001 | Microsoft-Windows-Service Control Manager Performance Diagnostic Provider\r\n
0x91000001 | Microsoft-Windows-Svchost Performance Diagnostic Provider\r\n
0x92000001 | Microsoft-Windows-Service Control Manager\r\n
0x92000002 | System\r\n
0xc0001b58 | The %1 service failed to start due to the following error: %n%2\r\n
0xc0001b59 | The %1 service depends on the %2 service which failed to start because of the following error: %n%3\r\n
0xc0001b5a | The %1 service depends on the %2 group and no member of this group started.\r\n
0xc0001b5b | The %1 service depends on the following service: %2. This service might not be installed.\r\n
0xc0001b5d | The %1 call failed with the following error: %n%2\r\n
0xc0001b5e | The %1 call failed for %2 with the following error: %n%3\r\n
0xc0001b5f | The system reverted to its last known good configuration.  The system is restarting....\r\n
0xc0001b60 | No backslash is in the account name. The account name must be in the form: domain\user.\r\n
0xc0001b61 | A timeout was reached (%1 milliseconds) while waiting for the %2 service to connect.\r\n
0xc0001b62 | A timeout (%1 milliseconds) was reached while waiting for ReadFile.\r\n
0xc0001b63 | A timeout (%1 milliseconds) was reached while waiting for a transaction response from the %2 service.\r\n
0xc0001b64 | The message returned in the transaction has incorrect size.\r\n
0xc0001b65 | Logon attempt with current password failed with the following error: %n%1\r\n
0xc0001b66 | Second logon attempt with old password also failed with the following error: %n%1\r\n
0xc0001b68 | The %1 service has reported an invalid current state %2.\r\n
0xc0001b69 | Detected circular dependencies demand starting %1. Check the service dependency tree.\r\n
0xc0001b6a | Detected circular dependencies auto-starting services. Check the service dependency tree.\r\n
0xc0001b6b | The %1 service depends on a service in a group which starts later. Change the order in the service dependency tree to ensure that all services required to start this service are starting before this service is started.\r\n
0xc0001b6c | The %1 service depends on a group which starts later. Change the order in the service dependency tree to ensure that all services required to start this service are starting before this service is started.\r\n
0xc0001b6d | About to revert to the last known good configuration because the %1 service failed to start.\r\n
0xc0001b6e | The %1 service hung on starting.\r\n
0xc0001b6f | The %1 service terminated with the following error: %n%2\r\n
0xc0001b70 | The %1 service terminated with the following service-specific error: %n%2\r\n
0xc0001b72 | The following boot-start or system-start driver(s) did not load: %1\r\n
0xc0001b73 | Windows could not be started as configured. Starting Windows using a previous working configuration.\r\n
0xc0001b74 | The %1 Registry key denied access to SYSTEM account programs so the Service Control Manager took ownership of the Registry key.\r\n
0xc0001b75 | Service Control Manager %0\r\n
0xc0001b76 | The %1 service is marked as an interactive service.  However, the system is configured to not allow interactive services.  This service may not function properly.\r\n
0xc0001b77 | The %1 service terminated unexpectedly.  It has done this %2 time(s).  The following corrective action will be taken in %3 milliseconds: %5.\r\n
0xc0001b78 | The Service Control Manager tried to take a corrective action (%2) after the unexpected termination of the %3 service, but this action failed with the following error: %n%4\r\n
0xc0001b7a | The %1 service terminated unexpectedly.  It has done this %2 time(s).\r\n
0xc0001b7d | The Service Control Manager encountered an error undoing a configuration change to the %1 service.  The service's %2 is currently in an unpredictable state.  If you do not correct this configuration, you may not be able to restart the %1 service or may encounter other errors.  To ensure that the service is configured properly, use the Services snap-in in Microsoft Management Console (MMC).\r\n
0xc0001b7e | The %1 service was unable to log on as %2 with the currently configured password due to the following error: %n%3%n%nTo ensure that the service is configured properly, use the Services snap-in in Microsoft Management Console (MMC).\r\n
0xc0001b81 | The %1 service was unable to log on as %2 with the currently configured password due to the following error: %nLogon failure: the user has not been granted the requested logon type at this computer.%n %nService: %1 %nDomain and account: %2%n %nThis service account does not have the required user right "Log on as a service."%n %nUser Action%n %nAssign "Log on as a service" to the service account on this computer. You can use Local Security Settings (Secpol.msc) to do this. If this computer is a node in a cluster, check that this user right is assigned to the Cluster service account on all nodes in the cluster.%n %nIf you have already assigned this user right to the service account, and the user right appears to be removed, check with your domain administrator to find out if a Group Policy object associated with this node might be removing the right.\r\n
0xc0001b83 | The %1 service did not shut down properly after receiving a preshutdown control.\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x10000031 | Response Time\r\n
0x12000038 | Classic\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x40001b7b | The %1 service was successfully sent a %2 control.\r\n
0x40001b7c | The %1 service entered the %2 state.\r\n
0x40001b80 | The start type of the %1 service was changed from %2 to %3.\r\n
0x40001b82 | The %1 service was successfully sent a %2 control.%n%n The reason specified was: %3 [%4]%n%n Comment: %5\r\n
0x40001b85 | A service was installed in the system.%n%nService Name:  %1%nService File Name:  %2%nService Type:  %3%nService Start Type:  %4%nService Account:  %5\r\n
0x50000004 | Information\r\n
0x80001b7f | A service process other than the one launched by the Service Control Manager connected when starting the %1 service.  The Service Control Manager launched process %2 and process %3 connected instead.%n%n  Note that if this service is configured to start under a debugger, this behavior is expected.\r\n
0x80001b84 | The following service is taking more than %2 minutes to start and may have stopped responding: %1%n%nContact your system administrator or service vendor for approximate startup times for this service.%n%nIf you think this service might be slowing system response or logon time, talk to your system administrator about whether the service should be disabled until the problem is identified.%n%nYou may have to restart the computer in safe mode before you can disable the service.\r\n
0x80001b86 | The following service has repeatedly stopped responding to service control requests: %1%n%nContact the service vendor or the system administrator about whether to disable this service until the problem is identified.%n%nYou may have to restart the computer in safe mode before you can disable the service.\r\n
0x90000001 | Microsoft-Windows-Service Control Manager Performance Diagnostic Provider\r\n
0x91000001 | Microsoft-Windows-Svchost Performance Diagnostic Provider\r\n
0x92000001 | Microsoft-Windows-Service Control Manager\r\n
0x92000002 | System\r\n
0xc0001b58 | The %1 service failed to start due to the following error: %n%2\r\n
0xc0001b59 | The %1 service depends on the %2 service which failed to start because of the following error: %n%3\r\n
0xc0001b5a | The %1 service depends on the %2 group and no member of this group started.\r\n
0xc0001b5b | The %1 service depends on the following service: %2. This service might not be installed.\r\n
0xc0001b5d | The %1 call failed with the following error: %n%2\r\n
0xc0001b5e | The %1 call failed for %2 with the following error: %n%3\r\n
0xc0001b5f | The system reverted to its last known good configuration.  The system is restarting....\r\n
0xc0001b60 | No backslash is in the account name. The account name must be in the form: domain\user.\r\n
0xc0001b61 | A timeout was reached (%1 milliseconds) while waiting for the %2 service to connect.\r\n
0xc0001b62 | A timeout (%1 milliseconds) was reached while waiting for ReadFile.\r\n
0xc0001b63 | A timeout (%1 milliseconds) was reached while waiting for a transaction response from the %2 service.\r\n
0xc0001b64 | The message returned in the transaction has incorrect size.\r\n
0xc0001b65 | Logon attempt with current password failed with the following error: %n%1\r\n
0xc0001b66 | Second logon attempt with old password also failed with the following error: %n%1\r\n
0xc0001b68 | The %1 service has reported an invalid current state %2.\r\n
0xc0001b69 | Detected circular dependencies demand starting %1. Check the service dependency tree.\r\n
0xc0001b6a | Detected circular dependencies auto-starting services. Check the service dependency tree.\r\n
0xc0001b6b | The %1 service depends on a service in a group which starts later. Change the order in the service dependency tree to ensure that all services required to start this service are starting before this service is started.\r\n
0xc0001b6c | The %1 service depends on a group which starts later. Change the order in the service dependency tree to ensure that all services required to start this service are starting before this service is started.\r\n
0xc0001b6d | About to revert to the last known good configuration because the %1 service failed to start.\r\n
0xc0001b6e | The %1 service hung on starting.\r\n
0xc0001b6f | The %1 service terminated with the following error: %n%2\r\n
0xc0001b70 | The %1 service terminated with the following service-specific error: %n%2\r\n
0xc0001b72 | The following boot-start or system-start driver(s) did not load: %1\r\n
0xc0001b73 | Windows could not be started as configured. Starting Windows using a previous working configuration.\r\n
0xc0001b74 | The %1 Registry key denied access to SYSTEM account programs so the Service Control Manager took ownership of the Registry key.\r\n
0xc0001b75 | Service Control Manager %0\r\n
0xc0001b76 | The %1 service is marked as an interactive service.  However, the system is configured to not allow interactive services.  This service may not function properly.\r\n
0xc0001b77 | The %1 service terminated unexpectedly.  It has done this %2 time(s).  The following corrective action will be taken in %3 milliseconds: %5.\r\n
0xc0001b78 | The Service Control Manager tried to take a corrective action (%2) after the unexpected termination of the %3 service, but this action failed with the following error: %n%4\r\n
0xc0001b7a | The %1 service terminated unexpectedly.  It has done this %2 time(s).\r\n
0xc0001b7d | The Service Control Manager encountered an error undoing a configuration change to the %1 service.  The service's %2 is currently in an unpredictable state.  If you do not correct this configuration, you may not be able to restart the %1 service or may encounter other errors.  To ensure that the service is configured properly, use the Services snap-in in Microsoft Management Console (MMC).\r\n
0xc0001b7e | The %1 service was unable to log on as %2 with the currently configured password due to the following error: %n%3%n%nTo ensure that the service is configured properly, use the Services snap-in in Microsoft Management Console (MMC).\r\n
0xc0001b81 | The %1 service was unable to log on as %2 with the currently configured password due to the following error: %nLogon failure: the user has not been granted the requested logon type at this computer.%n %nService: %1 %nDomain and account: %2%n %nThis service account does not have the required user right "Log on as a service."%n %nUser Action%n %nAssign "Log on as a service" to the service account on this computer. You can use Local Security Settings (Secpol.msc) to do this. If this computer is a node in a cluster, check that this user right is assigned to the Cluster service account on all nodes in the cluster.%n %nIf you have already assigned this user right to the service account, and the user right appears to be removed, check with your domain administrator to find out if a Group Policy object associated with this node might be removing the right.\r\n
0xc0001b83 | The %1 service did not shut down properly after receiving a preshutdown control.\r\n
