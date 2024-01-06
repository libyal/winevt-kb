## wusa.exe

Path: %SystemRoot%\system32\wusa.exe

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x0000ea60 | Windows Update Standalone Installer\r\n
0x0000ea61 | wusa </? | /h | /help>\nwusa <update> [/quiet] [/norestart]\n        \n    /?, /h, /help - Display help information.\n\n    update -     Full path of the MSU file.\n\n    /quiet -     Quiet mode, no user interaction. reboot as needed\n    \n    /norestart - When combined with /quiet, installer will NOT initiate reboot. It is ignored if it is used alone\r\n
0x0000ea62 | Installer encountered an error: 0x%1!lx!\n\n%2!s!\r\n
0x0000ea63 | Only one instance of wusa.exe is allowed to run.\r\n
0x0000ea64 | The update does not apply to your system\r\n
0x0000ea65 | Only members of the Administrators group are allowed to install updates.\r\n
0x0000ea66 | Click OK to install the following Windows software update:\n                \n    %1\r\n
0x0000ea67 | Searching for updates...\r\n
0x0000ea68 | Search has completed.\r\n
0x0000ea69 | Copying packages to the Windows Update cache...\r\n
0x0000ea6a | Copy has completed.\r\n
0x0000ea6b | Cancel\r\n
0x0000ea6c | Preparing the installation...\r\n
0x0000ea6d | Preparation has completed.\r\n
0x90000001 | Microsoft-Windows-WUSA\r\n
0xb0000001 | %1\r\n
0xb0000002 | The Windows update %1 was successfully installed. (Command line: "%2")\r\n
0xb0000003 | The Windows update %1 could not be installed because of an error: %2 "%3" (Command line: "%4")\r\n
0xb0000004 | The Windows update %1 requires reboot. (Command line: "%2")\r\n
0xb0000005 | Reboot has been initiated for Windows update %1 (Command line: "%2")\r\n
0xb0000006 | The Windows Modules Installer must be updated before you can install this package (Command line: "%1")\r\n

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0x0000ea60 | Windows Update Standalone Installer\r\n
0x0000ea61 | wusa </? | /h | /help>\n\nwusa <update> /extract:<destination> [/log:<file name>]\n\nwusa <update> [/quiet] [/norestart | /warnrestart:<seconds> | /promptrestart | /forcerestart] [/log:<file name>]\n\nwusa /uninstall <<update> | /kb:<KB number>> [/quiet] [/norestart | /warnrestart:<seconds> | /promptrestart | /forcerestart] [/log:<file name>]\n\n\n/?, /h, /help\n-  Display help information.\n\nupdate\n-  Full path of the MSU file.\n\n/quiet\n-  Quiet mode, no user interaction. Reboot as needed.\n\n/uninstall\n-  Installer will uninstall the package.\n\n/kb\n-  When combined with /uninstall, installer will uninstall the package associated with the KB number.\n\n/extract\n-  Installer will extract the package contents to the destination folder.\n\n/norestart\n-  When combined with /quiet, installer will NOT initiate reboot.\n\n/warnrestart\n-  When combined with /quiet, installer will warn the user before initiating reboot.\n\n/promptrestart\n-  When combined with /quiet, installer will prompt before initiating reboot.\n\n/forcerestart\n-  When combined with /quiet, installer will forcefully close applications and initiate reboot.\n\n/log\n-  Installer will enable logging.\r\n
0x0000ea62 | Installer encountered an error: 0x%1!lx!\n\n%2!s!\r\n
0x0000ea63 | Only one instance of wusa.exe is allowed to run.\r\n
0x0000ea64 | The update is not applicable to your computer.\r\n
0x0000ea65 | Only members of the Administrators group are allowed to install updates.\r\n
0x0000ea66 | Do you want to install the following Windows software update?\n                \n    %1\r\n
0x0000ea67 | Searching for updates on this computer...\r\n
0x0000ea68 | The update %1 is not installed on this computer.\r\n
0x0000ea69 | Copying packages to the Windows Update cache...\r\n
0x0000ea6a | Extracting...\r\n
0x0000ea6b | Cancel\r\n
0x0000ea6c | Preparing the installation...\r\n
0x0000ea6d | Preparing to uninstall...\r\n
0x0000ea6e | %1 is already installed on this computer.\r\n
0x0000ea6f | %1 is not installed on this computer.\r\n
0x0000ea70 | %1 is required by your computer and cannot be uninstalled.\r\n
0x0000ea71 | Do you want to uninstall the following Windows software update?\n                \n    %1\r\n
0x0000ea72 | Uninstalling...\r\n
0x0000ea73 | %1 for Microsoft Windows (%2)\r\n
0x0000ea74 | Critical Update\r\n
0x0000ea75 | Hotfix\r\n
0x0000ea76 | Security Update\r\n
0x0000ea77 | Service Pack\r\n
0x0000ea78 | Software Update\r\n
0x0000ea79 | Update\r\n
0x0000ea7a | Update Rollup\r\n
0x0000ea7b | Driver\r\n
0x0000ea7c | Feature Pack\r\n
0x0000ea7d | Uninstalling update %1 is not supported.\r\n
0x50000000 | Log Always\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-WUSA\r\n
0xb0000001 | %1\r\n
0xb0000002 | Windows update %1 was successfully installed. (Command line: "%2")\r\n
0xb0000003 | Windows update %1 could not be installed because of error %2 "%3" (Command line: "%4")\r\n
0xb0000004 | Windows update %1 requires a computer restart to complete the installation. (Command line: "%2")\r\n
0xb0000005 | This computer will restart to complete the installation of Windows update %1 (Command line: "%2")\r\n
0xb0000006 | The Windows Modules Installer must be updated before you can install this package (Command line: "%1")\r\n
0xb0000007 | Windows update %1 was successfully uninstalled. (Command line: "%2")\r\n
0xb0000008 | Windows update %1 could not be uninstalled because of error %2 "%3" (Command line: "%4")\r\n
0xb0000009 | Windows update %1 requires a computer restart to finish uninstalling. (Command line: "%2")\r\n
0xb000000a | This computer will restart to finish uninstalling Windows update %1 (Command line: "%2")\r\n

### 10.0.10586.0, 10.0.14393.0

Message identifier | Message string
--- | ---
0x0000ea60 | Windows Update Standalone Installer\r\n
0x0000ea61 | wusa </? | /h | /help>\n\nwusa <update> [/quiet] [/norestart | /warnrestart:<seconds> | /promptrestart | /forcerestart] [/log:<file name>]\n\nwusa /uninstall <update> [/quiet] [/norestart | /warnrestart:<seconds> | /promptrestart | /forcerestart] [/log:<file name>]\n\nwusa /uninstall /kb:<KB number> [/norestart | /warnrestart:<seconds> | /promptrestart | /forcerestart] [/log:<file name>]\n\n/?, /h, /help\n-  Display help information.\n\nupdate\n-  Full path of the MSU file.\n\n/quiet\n-  Quiet mode, no user interaction. Reboot as needed.\n\n/uninstall\n-  Installer will uninstall the package.\n\n/kb\n-  When combined with /uninstall, installer will uninstall the package associated with the KB number.\n\n/norestart\n-  When combined with /quiet, installer will NOT initiate reboot.\n\n/warnrestart\n-  When combined with /quiet, installer will warn the user before initiating reboot.\n\n/promptrestart\n-  When combined with /quiet, installer will prompt before initiating reboot.\n\n/forcerestart\n-  When combined with /quiet, installer will forcefully close applications and initiate reboot.\n\n/log\n-  Installer will enable logging.\r\n
0x0000ea62 | Installer encountered an error: 0x%1!lx!\n\n%2!s!\r\n
0x0000ea63 | Only one instance of wusa.exe is allowed to run.\r\n
0x0000ea64 | The update is not applicable to your computer.\r\n
0x0000ea65 | Only members of the Administrators group are allowed to install updates.\r\n
0x0000ea66 | Do you want to install the following Windows software update?\n                \n    %1\r\n
0x0000ea67 | Searching for updates on this computer...\r\n
0x0000ea68 | The update %1 is not installed on this computer.\r\n
0x0000ea69 | Copying packages to the Windows Update cache...\r\n
0x0000ea6a | Extracting...\r\n
0x0000ea6b | Cancel\r\n
0x0000ea6c | Preparing the installation...\r\n
0x0000ea6d | Preparing to uninstall...\r\n
0x0000ea6e | %1 is already installed on this computer.\r\n
0x0000ea6f | %1 is not installed on this computer.\r\n
0x0000ea70 | %1 is required by your computer and cannot be uninstalled.\r\n
0x0000ea71 | Do you want to uninstall the following Windows software update?\n                \n    %1\r\n
0x0000ea72 | Uninstalling...\r\n
0x0000ea73 | %1 for Microsoft Windows (%2)\r\n
0x0000ea74 | Critical Update\r\n
0x0000ea75 | Hotfix\r\n
0x0000ea76 | Security Update\r\n
0x0000ea77 | Service Pack\r\n
0x0000ea78 | Software Update\r\n
0x0000ea79 | Update\r\n
0x0000ea7a | Update Rollup\r\n
0x0000ea7b | Driver\r\n
0x0000ea7c | Feature Pack\r\n
0x0000ea7d | Uninstalling update %1 is not supported.\r\n
0x0000ea7e | The /extract option is no longer supported.\r\n
0x50000000 | Log Always\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-WUSA\r\n
0xb0000001 | %1\r\n
0xb0000002 | Windows update %1 was successfully installed. (Command line: "%2")\r\n
0xb0000003 | Windows update %1 could not be installed because of error %2 "%3" (Command line: "%4")\r\n
0xb0000004 | Windows update %1 requires a computer restart to complete the installation. (Command line: "%2")\r\n
0xb0000005 | This computer will restart to complete the installation of Windows update %1 (Command line: "%2")\r\n
0xb0000006 | The Windows Modules Installer must be updated before you can install this package (Command line: "%1")\r\n
0xb0000007 | Windows update %1 was successfully uninstalled. (Command line: "%2")\r\n
0xb0000008 | Windows update %1 could not be uninstalled because of error %2 "%3" (Command line: "%4")\r\n
0xb0000009 | Windows update %1 requires a computer restart to finish uninstalling. (Command line: "%2")\r\n
0xb000000a | This computer will restart to finish uninstalling Windows update %1 (Command line: "%2")\r\n

### 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x0000ea60 | Windows Update Standalone Installer\r\n
0x0000ea61 | wusa </? | /h | /help>\r\n\r\nwusa <update> [/quiet] [/norestart | /warnrestart:<seconds> | /promptrestart | /forcerestart] [/log:<file name>]\r\n\r\nwusa /uninstall <update> [/quiet] [/norestart | /warnrestart:<seconds> | /promptrestart | /forcerestart] [/log:<file name>]\r\n\r\nwusa /uninstall /kb:<KB number> [/norestart | /warnrestart:<seconds> | /promptrestart | /forcerestart] [/log:<file name>]\r\n\r\n/?, /h, /help\r\n-  Display help information.\r\n\r\nupdate\r\n-  Full path of the MSU file.\r\n\r\n/quiet\r\n-  Quiet mode, no user interaction. Reboot as needed.\r\n\r\n/uninstall\r\n-  Installer will uninstall the package.\r\n\r\n/kb\r\n-  When combined with /uninstall, installer will uninstall the package associated with the KB number.\r\n\r\n/norestart\r\n-  When combined with /quiet, installer will NOT initiate reboot.\r\n\r\n/warnrestart\r\n-  When combined with /quiet, installer will warn the user before initiating reboot.\r\n\r\n/promptrestart\r\n-  When combined with /quiet, installer will prompt before initiating reboot.\r\n\r\n/forcerestart\r\n-  When combined with /quiet, installer will forcefully close applications and initiate reboot.\r\n\r\n/log\r\n-  Installer will enable logging.\r\n
0x0000ea62 | Installer encountered an error: 0x%1!lx!\r\n\r\n%2!s!\r\n
0x0000ea63 | Only one instance of wusa.exe is allowed to run.\r\n
0x0000ea64 | The update is not applicable to your computer.\r\n
0x0000ea65 | Only members of the Administrators group are allowed to install updates.\r\n
0x0000ea66 | Do you want to install the following Windows software update?\r\n                \r\n    %1\r\n
0x0000ea67 | Searching for updates on this computer...\r\n
0x0000ea68 | The update %1 is not installed on this computer.\r\n
0x0000ea69 | Copying packages to the Windows Update cache...\r\n
0x0000ea6a | Extracting...\r\n
0x0000ea6b | Cancel\r\n
0x0000ea6c | Preparing the installation...\r\n
0x0000ea6d | Preparing to uninstall...\r\n
0x0000ea6e | %1 is already installed on this computer.\r\n
0x0000ea6f | %1 is not installed on this computer.\r\n
0x0000ea70 | %1 is required by your computer and cannot be uninstalled.\r\n
0x0000ea71 | Do you want to uninstall the following Windows software update?\r\n                \r\n    %1\r\n
0x0000ea72 | Uninstalling...\r\n
0x0000ea73 | %1 for Microsoft Windows (%2)\r\n
0x0000ea74 | Critical Update\r\n
0x0000ea75 | Hotfix\r\n
0x0000ea76 | Security Update\r\n
0x0000ea77 | Service Pack\r\n
0x0000ea78 | Software Update\r\n
0x0000ea79 | Update\r\n
0x0000ea7a | Update Rollup\r\n
0x0000ea7b | Driver\r\n
0x0000ea7c | Feature Pack\r\n
0x0000ea7d | Uninstalling update %1 is not supported.\r\n
0x0000ea7e | The /extract option is no longer supported.\r\n
0x50000000 | Log Always\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-WUSA\r\n
0xb0000001 | %1\r\n
0xb0000002 | Windows update %1 was successfully installed. (Command line: "%2")\r\n
0xb0000003 | Windows update %1 could not be installed because of error %2 "%3" (Command line: "%4")\r\n
0xb0000004 | Windows update %1 requires a computer restart to complete the installation. (Command line: "%2")\r\n
0xb0000005 | This computer will restart to complete the installation of Windows update %1 (Command line: "%2")\r\n
0xb0000006 | The Windows Modules Installer must be updated before you can install this package (Command line: "%1")\r\n
0xb0000007 | Windows update %1 was successfully uninstalled. (Command line: "%2")\r\n
0xb0000008 | Windows update %1 could not be uninstalled because of error %2 "%3" (Command line: "%4")\r\n
0xb0000009 | Windows update %1 requires a computer restart to finish uninstalling. (Command line: "%2")\r\n
0xb000000a | This computer will restart to finish uninstalling Windows update %1 (Command line: "%2")\r\n
