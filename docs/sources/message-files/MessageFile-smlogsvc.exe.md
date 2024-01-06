## smlogsvc.exe

Path: %SystemRoot%\System32\smlogsvc.exe

### 5.0.2195.6608

Message identifier | Message string
--- | ---
0x400007e7 | Log %1 has been started or restarted and is logging data to file %2.\r\n
0x400007e8 | Log %1, logging data to file %2, has been stopped.\r\n
0x400007ef | Counter: %1 has tripped its alert threshold. The counter value of %2 is %3 the limit\r\nvalue of %4.\r\n
0x400007f5 | Alert %1 has been started or restarted.\r\n
0x40000801 | Starting service.\r\n
0x40000802 | Handler registered.\r\n
0x40000803 | Clear run states.\r\n
0x40000804 | Default folder loaded.\r\n
0x40000805 | Event source registered.\r\n
0x40000806 | Config event created.\r\n
0x40000807 | Service control dispatcher started.\r\n
0x800007d4 | The service was unable to open the log file: %1 for log %2 and will be stopped.\r\nCheck the log folder for existence, spelling and permissions or reenter\r\nthe log file name using the configuration program.\r\nThis log will not be started.\r\nThe error returned is: %3.\r\n
0x800007d5 | Unable to read the configuration of the %1 log or alert.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007d6 | Unable to read the %1 value of the %2 log or alert configuration.\r\nThe default value will be used.\r\nThe error code returned is in the data.\r\n
0x800007d7 | Unable to read the %1 value of the %2 log or alert configuration.\r\nAn error occurred while trying to allocate memory for the default value.\r\nThe error code returned is in the data.\r\n
0x800007d8 | Unable to read the %1 value of the %2 log or alert configuration.\r\nNo default value provided.\r\nThe error code returned is in the data.\r\n
0x800007d9 | Log Type for the %1 log or alert configuration has invalid value.\r\nThis log or alert will not be started.\r\nThe invalid value is in the data.\r\n
0x800007da | An error occurred while trying to allocate memory for or read the command\r\nfilename to be executed by the %1 log or alert. The log or alert will continue, but no\r\ncommand file will be executed.\r\n
0x800007db | Unable to read the Last Modified value of the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007dc | Unable to allocate a data block for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007dd | Unable to start the thread for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007de | Unable to start the trace session for the %1 trace log configuration.\r\nOnly one instance of each trace provider can be enabled at any given time.\r\n
0x800007df | Unable to enable any trace providers for the %1 trace log configuration.\r\nThis log will not be started.\r\n
0x800007e0 | Unable to enable trace provider %1 for the %2 trace log configuration.\r\nOnly one instance of each trace provider can be enabled at any given time.\r\nThe error code returned is in the data.\r\n
0x800007e1 | Unable to start the trace session for the %1 trace log configuration.\r\nAnother trace session for this provider is currently enabled.\r\nOnly one instance of each trace provider can be enabled at any given time.\r\n
0x800007e2 | Unable to create the exit event for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e3 | Unable to start the thread for the %1 log or alert configuration.\r\nThe maximum number of active logs and alerts has been reached.\r\nRestart the log or alert when fewer logs and alerts are active.\r\n
0x800007e4 | Unable to read the list of counters from the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e5 | Unable to read the list of trace providers to log for the %1 trace log configuration.\r\nThis log will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e6 | Unable to allocate the memory for the counter list of the %1 log or alert configuration. \r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e9 | An error occurred while trying to update the log file with the current data\r\nfor the %1 log session.  This log session will be stopped.\r\nThe Pdh error returned is : %2.\r\n
0x800007ea | An error occurred while trying to reset the current state of the %1 log or alert to Stopped.\r\nThe service will continue, but the configuration of that log or alert might\r\nbe incorrect.\r\n
0x800007eb | An error occurred while trying to reset the current manual start state\r\nof the %1 log or alert to match its current stopped state.  The service\r\nwill continue, but the configuration of that log or alert might be incorrect.\r\n
0x800007ec | The service was unable to add the counter '%1' to the %2 log or alert.  This log or alert\r\nwill continue, but data for that counter will not be collected.\r\nThe error returned is: %3.\r\n
0x800007ed | The service was unable to add any counters to the %1 log or alert.  \r\nThis log or alert will not be started.\r\n
0x800007ee | The service was unable to parse the alert info for the %2 alert so this counter\r\nwill not be monitored.\r\nThe path string in error is: %1\r\n
0x800007f0 | An error occurred while trying to reset the current manual stop state\r\nof the %1 log or alert to match the its current stopped state.  The service\r\nwill continue, but the configuration of that log or alert might be incorrect.\r\n
0x800007f1 | Unable to create the reconfigure event for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007f2 | An error occurred while trying to collect data for the %1 alert scan.\r\nThe service will continue, but that alert scan will be stopped.\r\nThe error returned is: %2.\r\n
0x800007f3 | The addition of counter '%1' to the %2 log or alert generated a warning.\r\nData for that counter might not be collected.\r\nThe error returned is: %3.\r\n
0x800007f4 | Unable to create the %1 folder for the %2 log configuration.\r\nThis log will not be started.\r\nThe error returned is: %3.\r\n
0x800007f6 | Unable to execute command '%1' for the %2 alert.  \r\nThe alert will continue as scheduled.\r\nThe error code returned is in the data.\r\n
0x800007f7 | Unable to execute command '%1' for the %2 log.  \r\nThe log will continue as scheduled.\r\nThe error returned is: %3.\r\n
0x800007f8 | The service was unable to open the command or program file: %1. The %2 log or alert will\r\ncontinue as scheduled.  Check the file for existence, spelling and permissions or reenter\r\nthe file name using the configuration program.\r\nThe error returned is: %3.\r\n
0x800007f9 | Unable to allocate memory while starting the %1 log. \r\nThis log will not be started.\r\nThe error code returned is in the data.\r\n
0x800007fa | The service was unable to send a message for alert %1 to machine %2. The alert will\r\ncontinue as scheduled.\r\nThe error returned is: %3.\r\n
0x800007fb | Unable to read the configuration of the %1 log, started in response to the %2 alert trigger.  The alert will\r\ncontinue as scheduled.\r\n
0x800007fc | Unable to start the %1 log in response to the %2 alert trigger.  The alert will\r\ncontinue as scheduled.\r\nThe error code returned is in the data.\r\n
0x800007fd | Unable to create the %1 log file. The log will not be started.\r\nError returned is: %2.\r\n
0x800007fe | The service was unable to add the counter '%1' to the %2 log or alert.\r\nThis log or alert will continue, but data for that counter will not be collected.\r\nTo collect data from a remote computer, the Performance Logs and Alerts service\r\nmust run under an account that has access to the remote system.\r\n
0x800007ff | Unable to create the %1 folder for the %2 log configuration.\r\nThis log will be stopped.\r\nThe error returned is: %3.\r\n
0x80000800 | Creation of the %1 log or alert is not complete.\r\nThis log will not be started.\r\n
0x80000808 | The open operation on log file: %1 for log %2 generated a warning.\r\nThe log will continue.\r\nThe warning returned is: %3.\r\n
0xc00007d0 | Unable to initialize the service. Win32 error code returned is in the data.\r\n
0xc00007d1 | Unable to register the Service Control Handler function. Win32 error code returned\r\nis in the data.\r\n
0xc00007d2 | Unable to create the configuration event. Win32 error code returned is in the data.\r\n
0xc00007d3 | Unable to open the Performance Logs and Alerts configuration.\r\nThis configuration is initialized when you use the Performance\r\nLogs and Alerts Management Console snapin to create a Log or\r\nAlert session.\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x400007e7 | Log %1 has been started or restarted and is logging data to file %2.\r\n
0x400007e8 | Log %1, logging data to file %2, has been stopped.\r\n
0x400007ef | Counter: %1 has tripped its alert threshold. The counter value of %2 is %3 the limit\r\nvalue of %4.\r\n
0x400007f5 | Alert %1 has been started or restarted.\r\n
0x40000801 | Starting service.\r\n
0x40000802 | Handler registered.\r\n
0x40000803 | Clear run states.\r\n
0x40000804 | Default folder loaded.\r\n
0x40000805 | Event source registered.\r\n
0x40000806 | Config event created.\r\n
0x40000807 | Service control dispatcher started.\r\n
0x800007d4 | The service was unable to open the log file %1 for log %2 and will be stopped.\r\nCheck the log folder for existence, spelling, permissions, and ensure that \r\nno other logs or applications are writing to this log file. You can reenter\r\nthe log file name using the configuration program.  \r\nThis log will not be started.\r\nThe error returned is: %3.\r\n
0x800007d5 | Unable to read the configuration of the %1 log or alert.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007d6 | Unable to read the %1 value of the %2 log or alert configuration.\r\nThe default value will be used.\r\nThe error code returned is in the data.\r\n
0x800007d7 | Unable to read the %1 value of the %2 log or alert configuration.\r\nAn error occurred while trying to allocate memory for the default value.\r\nThe error code returned is in the data.\r\n
0x800007d9 | Log Type for the %1 log or alert configuration has invalid value.\r\nThis log or alert will not be started.\r\nThe invalid value is in the data.\r\n
0x800007dc | Unable to allocate a data block for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007dd | Unable to start the thread for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007de | Unable to start the trace session for the %1 trace log configuration.\r\nThe Kernel trace provider and some application trace providers require \r\nAdministrator privileges in order to collect data.  Use the Run As option \r\nin the configuration application to log under an Administrator account\r\nfor these providers. \r\nSystem error code returned is in the data.\r\n
0x800007df | Unable to enable any trace providers for the %1 trace log configuration.\r\nThis log will not be started.\r\n
0x800007e0 | Unable to enable trace provider %1 for the %2 trace log configuration.\r\nOnly one instance of each trace provider can be enabled at any given time.\r\nThe Kernel trace provider and some application trace providers require \r\nAdministrator privileges in order to collect data.  Use the Run As option \r\nin the configuration application to log under an Administrator account\r\nfor these providers. \r\nThe error code returned is in the data.\r\n
0x800007e2 | Unable to create the exit event for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e3 | Unable to start the thread for the %1 log or alert configuration.\r\nThe maximum number of active logs and alerts has been reached.\r\nRestart the log or alert when fewer logs and alerts are active.\r\n
0x800007e4 | Unable to read the list of counters from the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e5 | Unable to read the list of trace providers to log for the %1 trace log configuration.\r\nThis log will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e9 | An error occurred while trying to update the log file with the current data\r\nfor the %1 log session.  This log session will be stopped.\r\nThe Pdh error returned is: %2.\r\n
0x800007ea | An error occurred while trying to reset the current state of the %1 log or alert to Stopped.\r\nThe service will continue, but the configuration of that log or alert might\r\nbe incorrect.\r\n
0x800007eb | An error occurred while trying to reset the current manual start state\r\nof the %1 log or alert to match its current stopped state.  The service\r\nwill continue, but the configuration of that log or alert might be incorrect.\r\n
0x800007ec | The service was unable to add the counter '%1' to the %2 log or alert.  This log or alert\r\nwill continue, but data for that counter will not be collected.\r\nThe error returned is: %3.\r\n
0x800007ed | The service was unable to add any counters to the %1 log or alert.  \r\nThis log or alert will not be started.\r\n
0x800007ee | The service was unable to parse the alert info for the %2 alert so this counter\r\nwill not be monitored.\r\nThe path string in error is: %1\r\n
0x800007f0 | An error occurred while trying to reset the current manual stop state\r\nof the %1 log or alert to match the its current stopped state.  The service\r\nwill continue, but the configuration of that log or alert might be incorrect.\r\n
0x800007f1 | Unable to create the reconfigure event for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007f2 | An error occurred while trying to collect data for the %1 alert scan.\r\nThe service will continue, but that alert scan will be stopped.\r\nThe error returned is: %2.\r\n
0x800007f3 | The addition of counter '%1' to the %2 log or alert generated a warning.\r\nData for that counter might not be collected.\r\nThe error returned is: %3.\r\n
0x800007f4 | Unable to create the %1 folder for the %2 log configuration.\r\nThis log will not be started.\r\nThe error returned is: %3.\r\n
0x800007f6 | Unable to execute command '%1' for the %2 alert.  \r\nThe alert will continue as scheduled.\r\nThe error code returned is in the data.\r\n
0x800007f7 | Unable to execute command '%1' for the %2 log.  \r\nThe log will continue as scheduled.\r\nThe error returned is: %3.\r\n
0x800007f8 | The service was unable to open the command or program file: %1. The %2 log or alert will\r\ncontinue as scheduled.  Check the file for existence, spelling and permissions or reenter\r\nthe file name using the configuration program.\r\nThe error returned is: %3.\r\n
0x800007f9 | Unable to allocate memory while starting the %1 log. \r\nThis log will not be started.\r\nThe error code returned is in the data.\r\n
0x800007fa | The service was unable to send a message for alert %1 to machine %2. The alert will\r\ncontinue as scheduled.\r\nThe error returned is: %3.\r\n
0x800007fb | Unable to read the configuration of the %1 log, started in response to the %2 alert trigger.  The alert will\r\ncontinue as scheduled.\r\n
0x800007fc | Unable to start the %1 log in response to the %2 alert trigger.  The alert will\r\ncontinue as scheduled.\r\nThe error code returned is in the data.\r\n
0x800007fe | The service was unable to add the counter '%1' to the %2 log or alert.\r\nThis log or alert will continue, but data for that counter will not be collected.\r\nUse the Run As option in the configuration program to run the log under \r\nan account that has access to the performance data on the computer \r\nfrom which you are collecting data.\r\n
0x800007ff | Unable to create the %1 folder for the %2 log configuration.\r\nThis log will be stopped.\r\nThe error returned is: %3.\r\n
0x80000800 | Creation of the %1 log or alert is not complete.\r\nThis log will not be started.\r\n
0x80000808 | The open operation on log file: %1 for log %2 generated a warning.\r\nThe log will continue.\r\nThe warning returned is: %3.\r\n
0x80000809 | Unable to allocate memory while starting the %1 alert. \r\nThis alert will not be started.\r\nThe error code returned is in the data.\r\n
0x8000080a | An error occurred while trying to open the %1 log or alert session.  \r\nThis session will be stopped.\r\nThe Pdh error returned is: %2.\r\n
0x8000080b | Invalid user name or password for the %1 log session.\r\nThis session will not be started.\r\n
0x8000080c | The service was unable to parse the counter '%1' in the %2 log.  This log\r\nwill continue, but data for that counter will not be collected.\r\nThe error returned is: %3.\r\n
0x8000080d | Log %1 has failed. General internal application failure.\r\n
0x8000080e | Unable to start the trace session for the %1 trace log configuration.\r\nOnly one instance of each trace provider can be enabled at any given time.\r\n
0xc00007d0 | Unable to initialize the service. Win32 error code returned is in the data.\r\n
0xc00007d1 | Unable to register the Service Control Handler function. Win32 error code returned\r\nis in the data.\r\n
0xc00007d2 | Unable to create the configuration event. Win32 error code returned is in the data.\r\n
0xc00007d3 | Unable to open the Performance Logs and Alerts configuration.\r\nThis configuration is initialized when you use the Performance\r\nLogs and Alerts Management Console snapin to create a Log or\r\nAlert session.\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x400007e7 | Log %1 has been started or restarted and is logging data to file %2.\r\n
0x400007e8 | Log %1, logging data to file %2, has been stopped.\r\n
0x400007ef | Counter: %1 has tripped its alert threshold. The counter value of %2 is %3 the limit\r\nvalue of %4.\r\n
0x400007f5 | Alert %1 has been started or restarted.\r\n
0x40000801 | Starting service.\r\n
0x40000802 | Handler registered.\r\n
0x40000803 | Clear run states.\r\n
0x40000804 | Default folder loaded.\r\n
0x40000805 | Event source registered.\r\n
0x40000806 | Config event created.\r\n
0x40000807 | Service control dispatcher started.\r\n
0x800007d4 | The service was unable to open the log file %1 for log %2 and will be stopped.\r\nCheck the log folder for existence, spelling, permissions, and ensure that \r\nno other logs or applications are writing to this log file. You can reenter\r\nthe log file name using the configuration program.  \r\nThis log will not be started.\r\nThe error returned is: %3.\r\n
0x800007d5 | Unable to read the configuration of the %1 log or alert.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007d6 | Unable to read the %1 value of the %2 log or alert configuration.\r\nThe default value will be used.\r\nThe error code returned is in the data.\r\n
0x800007d7 | Unable to read the %1 value of the %2 log or alert configuration.\r\nAn error occurred while trying to allocate memory for the default value.\r\nThe error code returned is in the data.\r\n
0x800007d9 | Log Type for the %1 log or alert configuration has invalid value.\r\nThis log or alert will not be started.\r\nThe invalid value is in the data.\r\n
0x800007dc | Unable to allocate a data block for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007dd | Unable to start the thread for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007de | Unable to start the trace session for the %1 trace log configuration.\r\nThe Kernel trace provider and some application trace providers require \r\nAdministrator privileges in order to collect data.  Use the Run As option \r\nin the configuration application to log under an Administrator account\r\nfor these providers. \r\nSystem error code returned is in the data.\r\n
0x800007df | Unable to enable any trace providers for the %1 trace log configuration.\r\nThis log will not be started.\r\n
0x800007e0 | Unable to enable trace provider %1 for the %2 trace log configuration.\r\nOnly one instance of each trace provider can be enabled at any given time.\r\nThe Kernel trace provider and some application trace providers require \r\nAdministrator privileges in order to collect data.  Use the Run As option \r\nin the configuration application to log under an Administrator account\r\nfor these providers. \r\nThe error code returned is in the data.\r\n
0x800007e2 | Unable to create the exit event for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e3 | Unable to start the thread for the %1 log or alert configuration.\r\nThe maximum number of active logs and alerts has been reached.\r\nRestart the log or alert when fewer logs and alerts are active.\r\n
0x800007e4 | Unable to read the list of counters from the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e5 | Unable to read the list of trace providers to log for the %1 trace log configuration.\r\nThis log will not be started.\r\nThe error code returned is in the data.\r\n
0x800007e9 | An error occurred while trying to update the log file with the current data\r\nfor the %1 log session.  This log session will be stopped.\r\nThe Pdh error returned is: %2.\r\n
0x800007ea | An error occurred while trying to reset the current state of the %1 log or alert to Stopped.\r\nThe service will continue, but the configuration of that log or alert might\r\nbe incorrect.\r\n
0x800007eb | An error occurred while trying to reset the current manual start state\r\nof the %1 log or alert to match its current stopped state.  The service\r\nwill continue, but the configuration of that log or alert might be incorrect.\r\n
0x800007ec | The service was unable to add the counter '%1' to the %2 log or alert.  This log or alert\r\nwill continue, but data for that counter will not be collected.\r\nThe error returned is: %3.\r\n
0x800007ed | The service was unable to add any counters to the %1 log or alert.  \r\nThis log or alert will not be started.\r\n
0x800007ee | The service was unable to parse the alert info for the %2 alert so this counter\r\nwill not be monitored.\r\nThe path string in error is: %1\r\n
0x800007f0 | An error occurred while trying to reset the current manual stop state\r\nof the %1 log or alert to match the its current stopped state.  The service\r\nwill continue, but the configuration of that log or alert might be incorrect.\r\n
0x800007f1 | Unable to create the reconfigure event for the %1 log or alert configuration.\r\nThis log or alert will not be started.\r\nThe error code returned is in the data.\r\n
0x800007f2 | An error occurred while trying to collect data for the %1 alert scan.\r\nThe service will continue, but that alert scan will be stopped.\r\nThe error returned is: %2.\r\n
0x800007f3 | The addition of counter '%1' to the %2 log or alert generated a warning.\r\nData for that counter might not be collected.\r\nThe error returned is: %3.\r\n
0x800007f4 | Unable to create the %1 folder for the %2 log configuration.\r\nThis log will not be started.\r\nThe error returned is: %3.\r\n
0x800007f6 | Unable to execute command '%1' for the %2 alert.  \r\nThe alert will continue as scheduled.\r\nThe error code returned is in the data.\r\n
0x800007f7 | Unable to execute command '%1' for the %2 log.  \r\nThe log will continue as scheduled.\r\nThe error returned is: %3.\r\n
0x800007f8 | The service was unable to open the command or program file: %1. The %2 log or alert will\r\ncontinue as scheduled.  Check the file for existence, spelling and permissions or reenter\r\nthe file name using the configuration program.\r\nThe error returned is: %3.\r\n
0x800007f9 | Unable to allocate memory while starting the %1 log. \r\nThis log will not be started.\r\nThe error code returned is in the data.\r\n
0x800007fa | The service was unable to send a message for alert %1 to machine %2. The alert will\r\ncontinue as scheduled.\r\nThe error returned is: %3.\r\n
0x800007fb | Unable to read the configuration of the %1 log, started in response to the %2 alert trigger.  The alert will\r\ncontinue as scheduled.\r\n
0x800007fc | Unable to start the %1 log in response to the %2 alert trigger.  The alert will\r\ncontinue as scheduled.\r\nThe error code returned is in the data.\r\n
0x800007fe | The service was unable to add the counter '%1' to the %2 log or alert.\r\nThis log or alert will continue, but data for that counter will not be collected.\r\nUse the Run As option in the configuration program to run the log under \r\nan account that has access to the performance data on the computer \r\nfrom which you are collecting data.\r\n
0x800007ff | Unable to create the %1 folder for the %2 log configuration.\r\nThis log will be stopped.\r\nThe error returned is: %3.\r\n
0x80000800 | Creation of the %1 log or alert is not complete.\r\nThis log will not be started.\r\n
0x80000808 | The open operation on log file: %1 for log %2 generated a warning.\r\nThe log will continue.\r\nThe warning returned is: %3.\r\n
0x80000809 | Unable to allocate memory while starting the %1 alert. \r\nThis alert will not be started.\r\nThe error code returned is in the data.\r\n
0x8000080a | An error occurred while trying to open the %1 log or alert session.  \r\nThis session will be stopped.\r\nThe Pdh error returned is: %2.\r\n
0x8000080b | Invalid user name or password for the %1 log session.\r\nThis session will not be started.\r\n
0x8000080c | The service was unable to parse the counter '%1' in the %2 log.  This log\r\nwill continue, but data for that counter will not be collected.\r\nThe error returned is: %3.\r\n
0x8000080d | Log %1 has failed. General internal application failure.\r\n
0x8000080e | Unable to start the trace session for the %1 trace log configuration.\r\nOnly one instance of each trace provider can be enabled at any given time.\r\n
0x80000810 | The service was unable to start the %1 log or alert.  The open operation\r\nhas timed out.  The operation will be retried %2 times. This timeout\r\ncan occur when another log or alert is waiting to connect to a remote\r\ncomputer, or when data collection is taking a long time.\r\n
0x80000811 | The service was unable to add the counter %1 to the %2 log or alert.\r\nThe add operation has timed out.  The operation will be retried %3 times.\r\nThis timeout can occur when another log or alert is waiting to connect\r\nto a remote computer, or when data collection is taking a long time.\r\n
0xc00007d0 | Unable to initialize the service. Win32 error code returned is in the data.\r\n
0xc00007d1 | Unable to register the Service Control Handler function. Win32 error code returned\r\nis in the data.\r\n
0xc00007d2 | Unable to create the configuration event. Win32 error code returned is in the data.\r\n
0xc00007d3 | Unable to open the Performance Logs and Alerts configuration.\r\nThis configuration is initialized when you use the Performance\r\nLogs and Alerts Management Console snapin to create a Log or\r\nAlert session.\r\n
0xc000080f | Unable to register for WMI notification. Win32 error code returned\r\nis in the data.\r\n
