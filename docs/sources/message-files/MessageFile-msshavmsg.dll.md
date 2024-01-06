## msshavmsg.dll

Path: %SystemRoot%\System32\msshavmsg.dll

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x00ff0005 | This computer is not missing any security updates.\r\n
0x00ff0006 | This computer is missing some security updates.\r\n
0x00ff0008 | The Windows Server Update Services has not started.  An administrator may try to start the service manually.\r\n
0x00ff0019 | Windows is scanning for security updates.\r\n
0x00ff001a | An administrator must synchronize this computer with the Windows Server Update Services server.\r\n
0x00ff001c | An administrator must install required security updates.\r\n
0x00ff001e | The manual install of required security updates has exceeded the timeout period.  Network access on this computer will be limited until an administrator installs the required updates.\r\n
0x00ff001f | Windows is installing the required security updates.\r\n
0x00ff0021 | Windows is attempting to enable the Windows Firewall.\r\n
0x00ff0022 | An administrator must enable a firewall program that is compatible with Windows Security Center.\r\n
0x00ff0024 | Windows is attempting to turn on Automatic Updates.\r\n
0x00ff0025 | An administrator must turn on Automatic Updates.\r\n
0x00ff0029 | Windows is attempting to enable Windows Defender.\r\n
0x00ff002a | An administrator must enable an antispyware program that is compatible with Windows Security Center.\r\n
0x00ff002c | Windows is attempting to update signatures for Windows Defender.\r\n
0x00ff002d | An administrator must update the antispyware signatures on this computer.\r\n
0x00ff0032 | The Windows Security Center service has stopped.  Windows is restarting it.\r\n
0x00ff0033 | The Windows Security Center service has stopped.  An administrator must restart the service.\r\n
0x00ff0045 | Windows cannot determine the security state of this computer because the Windows Security Health Agent is waiting for other services to start. Windows will update the security state of this computer automatically once the services have started. This might take several minutes.\r\n
0x00ff0046 | Windows cannot determine the security state of this computer because the Windows Security Health Agent is waiting for other services to start. An administrator must update the security state of the system once initialization is completed. This might take several minutes.\r\n
0x00ff0053 | Windows System Health Agent is waiting for the Windows Security Center to update system status. This may take a few minutes.\r\n
0x00ff0054 | ProductCategory\r\n
0x00ff0055 | NumberOfOldProducts\r\n
0x00ff0056 | OldProductName\r\n
0x00ff0057 | OldProductStatus\r\n
0x00ff0058 | NumberOfNewProducts\r\n
0x00ff0059 | NewProductName\r\n
0x00ff005a | NewProductStatus\r\n
0x400003e8 | The Windows Security System Health Agent detected a change in the status of %1.\r\n
0x400003e9 | The Windows Security System Health Agent detected a change in the status of %1.\r\n
0x400003ea | The Windows Security Health Agent was initialized successfully.%rScan Interval: %1 minutes.%rTime delay before first scan: %2 seconds.%rTime interval between manual remediation state change: %3 seconds.%rManual remediation timeout interval: %4 seconds.\r\n
0x400003ec | The Windows Security Health Agent was uninitialized successfully.\r\n
0x400003ed | The Windows Security Health Agent completed an online scan.%rNumber of Updates : %1.%rUpdate Titles : %2.\r\n
0x400003ef | The Windows Security Health Agent completed an offline scan.%rNumber of Updates : %1.%rUpdate Titles : %2.\r\n
0x400003f1 | The Windows Security Health Agent completed a download of security updates.%rNumber of Updates : %1.%rUpdate Titles : %2.\r\n
0x400003f3 | The Windows Security Health Agent completed an install of security updates.%rNumber of Updates : %1.%rUpdate Titles : %2.\r\n
0x400003f5 | Automatic remediation for firewall succeeded. Windows Firewall was turned on successfully.\r\n
0x400003f7 | Automatic remediation for Automatic Updates succeeded. Automatic Updates was turned on successfully.\r\n
0x400003f9 | Automatic remediation for Windows Security Center service succeeded. Windows Security Center service was turned on successfully.\r\n
0x400003fb | Automatic remediation for antispyware succeeded. Windows defender was turned on successfully.\r\n
0x400003fd | Automatic remediation for antispyware signatures succeeded. Windows Defender signatures were updated successfully.\r\n
0x400003ff | The Windows Security Center detected a system health state change. The change in state was also successfully detected by the Windows Security Health Agent.\r\n
0x40000401 | The Windows Security Health Agent specified a new security health state for the computer.%rThe correlation id for this transaction is %1.\r\n
0x40000403 | The Windows Security Health Agent notified the Windows Network Access Protection Service of a change in the security health state of the computer.\r\n
0x40000405 | The Windows Security Health Agent successfully processed a response from the Windows Security Health Validator.%rThe correlation id for this transaction is %1.\r\n
0x4000046d | The Windows Security Health Agent has detected a Windows Update Agent service configuration change. If this change is unexpected, an administrator should verify that the Windows Update Agent service configuration is compliant with health policy.\r\n
0x4000046e | The Windows Security Health Agent has detected that the Windows Security Center service has stopped. If this is unexpected, an administrator should verify that the Windows Security Center service configuration is compliant with health policy.\r\n
0x4000046f | The Windows Security Center service state changed to running. The Windows Security Center service state is now initialized successfully.\r\n
0xc00003eb | The Windows Security Health Agent could not be initialized.%rFailure Code: %1.\r\n
0xc00003ee | The Windows Security Health Agent failed to complete an online scan.%rFailure Code: %1.\r\n
0xc00003f0 | The Windows Security Health Agent failed to complete an offline scan.%rFailure Code: %1.\r\n
0xc00003f2 | The Windows Security Health Agent failed to complete a download of security updates.%rFailure Code: %1.\r\n
0xc00003f4 | The Windows Security Health Agent failed to complete an install of security updates.%rFailure Code: %1.\r\n
0xc00003f6 | Automatic remediation for firewall failed. Windows could not turn on Windows Firewall.%rFailure Code: %1.\r\n
0xc00003f8 | Automatic remediation for Automatic Updates failed. Windows could not turn on Automatic Updates.%rFailure Code: %1.\r\n
0xc00003fa | Automatic remediation for Windows Security Center service failed. Windows could not turn on Windows Security Center service.%rFailure Code: %1.\r\n
0xc00003fc | Automatic remediation for antispyware failed. Windows could not turn on Windows Defender.%rFailure Code: %1.\r\n
0xc00003fe | Automatic remediation for antispyware signatures failed. Windows could not update signatures for Windows Defender.%rFailure Code: %1.\r\n
0xc0000400 | Windows Security Center detected a system health state change but the Windows Security Health Agent could not enumerate the state change.%rFailure Code: %1.\r\n
0xc0000402 | The Windows Security Health Agent failed to specify a new security health state for the computer.%rFailure Code: %1.%rThe correlation id for this transaction is %2.\r\n
0xc0000404 | The Windows Security Health Agent failed to notify the Windows Network Access Protection Service of a change in the security health state of the computer.%rFailure Code: %1.\r\n
0xc0000406 | The Windows Security Health Agent failed to process a response from the Windows Security Health Validator. %rFailure Code: %1.%rThe correlation id for this transaction is %2.\r\n
0xc000046b | Due to a Remote Procedure Call (RPC) error, there was a failure in contacting the Windows Security Center RPC service. The Windows Security Health Agent is unable to determine the computer's health state. The WSC and NAPAgent services might need to be restarted.\r\n
0xc000046c | The Windows Security System Health Agent failed to monitor the WUA service state.\r\n
0xc0000470 | The Windows Security Center service state changed to running. The Windows Security Center service state could not be initialized successfully.%rFailure Code :%1.\r\n
0xc0ff0001 | A system health component is not enabled.\r\n
0xc0ff0002 | A system health component is not installed.\r\n
0xc0ff0003 | The Windows Security Center service is not running.\r\n
0xc0ff0004 | The signatures for a particular system health component are not up to date.\r\n
0xc0ff0007 | This computer will be automatically synchronized with the Windows Server Update Services server and new security updates must be installed.\r\n
0xc0ff000c | The Windows Update Agent on this computer is not configured to synchronize with a Windows Server Update Services server.  An administrator must configure the Windows Update Agent service. Please click on the 'try again' button after configuration is done for the changes to take effect.\r\n
0xc0ff000d | Windows could not determine the Windows Server Update Services client ID of this computer.\r\n
0xc0ff000e | The Windows Update Agent service has been disabled or not configured to start automatically. An administrator must enable the service.\r\n
0xc0ff000f | The periodic scan of this computer for security updates failed.  An administrator must ensure that a Windows Server Update Services server is available and that the Windows Update Agent on this computer is configured to synchronize with the server.\r\n
0xc0ff0010 | Security updates have been installed and require this computer to be restarted.  Please close all applications and restart this computer.\r\n
0xc0ff0012 | The Network Policy Server was unable to validate the security update status of this computer.  An administrator must ensure that a Windows Server Update Services server is available and that the Windows Update Agent on this computer is configured to synchronize with the server.\r\n
0xc0ff0014 | Microsoft System Health Agent: E_MSSHV_UNKNOWN_CLIENT\r\n
0xc0ff0015 | Microsoft System Health Agent: E_MSSHV_SHC_FAILURE\r\n
0xc0ff0016 | Microsoft System Health Agent: E_MSSHV_POLICY_FAILURE\r\n
0xc0ff0017 | The Windows Security Health Validator could not process the latest Statement of Health (SoH) because the SoH is invalid.\r\n
0xc0ff0018 | The Windows Security Center service has not started. An administrator may try to start the service manually.\r\n
0xc0ff001b | Windows could not retrieve new security updates. An administrator must synchronize this computer with the Windows Server Update Services server, Microsoft Update, or Windows Update.\r\n
0xc0ff001d | A manual install of required security updates was attempted but failed.  An administrator must verify the Windows Update Agent service is running properly on this computer.\r\n
0xc0ff0020 | Windows could not install required security updates.  An administrator must install them manually.\r\n
0xc0ff0023 | Windows could not enable the Windows Firewall. An administrator must start it manually.\r\n
0xc0ff0026 | Windows could not turn on Automatic Updates. An administrator must start it manually.\r\n
0xc0ff0027 | One or more Windows Security Center-compatible antivirus applications are installed, but none are enabled.  An administrator must enable at least one for full network access.\r\n
0xc0ff0028 | The antivirus signatures on this computer are not up to date.  An administrator must update them for full network access.\r\n
0xc0ff002b | Windows could not enable Windows Defender.  An administrator must start it manually.\r\n
0xc0ff002e | Windows could not update signatures for Windows defender.  An administrator must update the signatures manually.\r\n
0xc0ff002f | Windows did not detect a firewall that is compatible with Windows Security Center.\r\n
0xc0ff0030 | Windows did not detect an antivirus program that is compatible with Windows Security Center.\r\n
0xc0ff0031 | Windows did not detect an antispyware program that is compatible with Windows Security Center.\r\n
0xc0ff0034 | The Windows Security Center service is disabled.  An administrator must enable the service.\r\n
0xc0ff0035 | Windows could not start the Windows Security Center Service.  An administrator may try to start the service manually.\r\n
0xc0ff0036 | Windows could not start the Windows Security Center Service.  An administrator may try to start the service manually.\r\n
0xc0ff0037 | Windows Security Health Agent\r\n
0xc0ff0038 | The Windows Security Health Agent checks the compliance of a computer with an administrator-defined policy.\r\n
0xc0ff0039 | Windows Security Health Validator\r\n
0xc0ff003a | The Windows Security Health Validator defines the policy that client computers must be compliant with.\r\n
0xc0ff003b | Microsoft Corporation\r\n
0xc0ff003c | 1.0\r\n
0xc0ff003d | The Windows Security Health Agent is in the process of updating its security state.\r\n
0xc0ff003e | The Windows Security Health Agent has finished updating its security state.\r\n
0xc0ff003f | The Windows Security Health Agent failed to update the security state of this computer.\r\n
0xc0ff0040 | Firewall.\r\n
0xc0ff0041 | Antivirus.\r\n
0xc0ff0042 | Antispyware.\r\n
0xc0ff0043 | Automatic Updates.\r\n
0xc0ff0044 | Security Updates.\r\n
0xc0ff0047 | A third-party system health component is not enabled.\r\n
0xc0ff0048 | The signatures for a particular third-party system health component are not up to date.\r\n
0xc0ff0049 | A third-party firewall product is not enabled. Windows cannot enable the firewall product automatically. An administrator must enable the firewall product manually.\r\n
0xc0ff004a | A third-party antivirus product is not enabled. Windows cannot enable the antivirus product automatically. An administrator must enable the antivirus product manually.\r\n
0xc0ff004b | A third-party antispyware product is not enabled. Windows cannot enable the antispyware product automatically. An administrator must enable the antispyware product manually.\r\n
0xc0ff004c | The signatures for a particular third-party antivirus product are not up to date. An administrator must update the antivirus signatures for the third-party product on this computer.\r\n
0xc0ff004d | The signatures for a particular third-party antispyware product are not up to date. An administrator must update the antispyware signatures for the third-party product on this computer\r\n
0xc0ff004e | This computer is not configured to receive security updates from a source approved for this network.  An administrator must configure the Windows Update Agent service to receive updates from Microsoft Update.\r\n
0xc0ff004f | This computer is not configured to receive security updates from a source approved for this network.  An administrator must configure the Windows Update Agent service to receive updates from Windows Update or Microsoft Update.\r\n
0xc0ff0050 | This computer is not configured to receive security updates from a source approved for this network.  An administrator must configure the Windows Update Agent service to receive updates from Windows Server Update Services or Microsoft Update.\r\n
0xc0ff0051 | The Windows Update Agent on this computer is not configured to receive security updates.  An administrator must configure the Windows Update Agent service.  The NAP Agent may have to be restarted for changes to take effect.\r\n
0xc0ff0052 | No Updates found\r\n
