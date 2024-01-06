## wudfplatform.dll

Path: %SystemRoot%\system32\WUDFPlatform.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x70000010 | Startup of the driver manager service.\r\n
0x70000011 | Creation of a new driver host process.\r\n
0x70000012 | Shutdown of a driver host process.\r\n
0x70000020 | Startup of a new driver host process.\r\n
0x70000021 | Loading drivers to control a newly discovered device.\r\n
0x70000025 | Pnp or Power Management operation to a particular device.\r\n
0x70000029 | Shutdown of a driver host process.\r\n
0x70000030 | Installation or update of device drivers.\r\n
0x70000040 | User-mode Driver problems.\r\n
0x70000050 | Pnp or Power Management operation to a particular driver in a device stack.\r\n
0x90000001 | Microsoft-Windows-DriverFrameworks-UserMode\r\n
0x90000002 | Microsoft-Windows-DriverFrameworks-UserMode/Operational\r\n
0xb00103e8 | The Driver Manager service started successfully\r\n
0xb00103e9 | The Driver Manager service failed to start.  The error reported was %1.\r\n
0xb00103ea | The Driver Manager service was stopped\r\n
0xb00103eb | The Driver Manager service is starting a host process for device %2.\r\n
0xb00103ec | The host process (%1) started successfully.\r\n
0xb00103ed | The host process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00103ee | The host process (%1) is being asked to shutdown.\r\n
0xb00103ef | The host process (%1) has a problem (%2) and is being terminated.\r\n
0xb00103f0 | The host process (%1) has been shutdown.\r\n
0xb00107d0 | The UMDF Host Process (%1) is starting up.\r\n
0xb00107d1 | The UMDF Host Process (%1) started successfully.\r\n
0xb00107d2 | The UMDF Host Process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00107d3 | The UMDF Host Process (%1) has been asked to load drivers for device %2.\r\n
0xb00107d4 | The UMDF Host is loading driver %4 at level %3 for device %2.\r\n
0xb00107d5 | The UMDF Host Process (%1) has loaded module %3 while loading drivers for device %2.\r\n
0xb00107d6 | The UMDF Host successfully loaded the driver at level %3.\r\n
0xb00107d7 | The UMDF Host failed to load the driver at level %3.  The error reported was %4.\r\n
0xb00107da | The UMDF Host Process (%1) has successfully loaded drivers for device %2.\r\n
0xb00107db | The UMDF Host Process (%1) has failed to load drivers for device %2.  The error reported was %3\r\n
0xb0010834 | Received a Pnp or Power operation (%3, %4) for device %2.\r\n
0xb0010835 | Completed a Pnp or Power operation (%3, %4) for device %2 with status %8.\r\n
0xb0010836 | Forwarded a finished Pnp or Power operation (%3, %4) to the lower driver for device %2 with status %8.\r\n
0xb0010839 | Forwarded a Pnp or Power operation (%3, %4) for device %2 to the lower driver with status %9\r\n
0xb001083a | Received a Pnp or Power operation (%3, %4) for device %2 which was completed by the lower drivers with status %9\r\n
0xb0010b54 | The UMDF Host (%1) has been asked to shutdown.\r\n
0xb0010b55 | The UMDF Host (%1) has shutdown.\r\n
0xb0012710 | A driver package which uses user-mode driver framework version %2 is being installed on device %1.\r\n
0xb0012711 | The UMDF service %1 (CLSID %2) was installed.  It requires framework version %3 or higher.\r\n
0xb0012712 | The UMDF service %1 (CLSID %2) was upgraded.  It requires framework version %3 or higher.\r\n
0xb0012774 | The driver package installation has succeeded.\r\n
0xb0012775 | The driver package installation has failed.  The final status was %1.\r\n
0xb001277e | A problem has occurred with one or more user-mode drivers and the hosting process has been terminated.  This may temporarily interrupt your ability to access the devices.\r\n
0xb001277f | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times.  Please contact the device manufacturer for more information about this problem.\r\n
0xb0012780 | The device %2 (location %3) is offline due to a user-mode device crash.  Windows will no longer attempt to restart this device because the maximum restart limit has been reached.  Disconnecting the device and reconnecting it, or disabling it and re-enabling it from the device manager, will reset this limit and allow the device to be accessed again.  Please contact the device manufacturer for more information about this problem.\r\n
0xb0014e3e | Power IRP related event in the User-mode Driver Frameworks Host Process\r\n
0xd0000001 | QueueToTail\r\n
0xd0000002 | QueueToFront\r\n
0xd0000003 | QueueFull\r\n

### 6.1.7600.16385, 6.1.7601.17514

Message identifier | Message string
--- | ---
0x00002710 | A driver package which uses user-mode driver framework version %2 is being installed on device %1.\r\n
0x00002711 | The UMDF service %1 (CLSID %2) was installed.  It requires framework version %3 or higher.\r\n
0x00002712 | The UMDF service %1 (CLSID %2) was upgraded.  It requires framework version %3 or higher.\r\n
0x00002774 | The driver package installation has succeeded.\r\n
0x00002775 | The driver package installation has failed.  The final status was %1.\r\n
0x0000277e | A problem has occurred with one or more user-mode drivers and the hosting process has been terminated.  This may temporarily interrupt your ability to access the devices.\r\n
0x0000277f | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002780 | The device %2 (location %3) is offline due to a user-mode device crash.  Windows will no longer attempt to restart this device because the maximum restart limit has been reached.  Disconnecting the device and reconnecting it, or disabling it and re-enabling it from the device manager, will reset this limit and allow the device to be accessed again.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002781 | The device %2 was unable to start due to conflict between the settings for driver %5 (%3 - %4) and the other drivers.  Windows will not be able to start this device.  Please contact the device manufacturer for assistance.\r\n
0x00002782 | The UMDF reflector was unable to complete startup because the %2 service was not found.  This service may be started later during boot, at which point Windows will attempt to start the device again.\r\n
0x00004e1f | UMDF Test Event (%1)\r\n
0x10000031 | Response Time\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000010 | Startup of the driver manager service.\r\n
0x70000011 | Creation of a new driver host process.\r\n
0x70000012 | Shutdown of a driver host process.\r\n
0x70000020 | Startup of a new driver host process.\r\n
0x70000021 | Loading drivers to control a newly discovered device.\r\n
0x70000025 | Pnp or Power Management operation to a particular device.\r\n
0x70000029 | Shutdown of a driver host process.\r\n
0x70000030 | Installation or update of device drivers.\r\n
0x70000040 | User-mode Driver problems.\r\n
0x70000050 | Pnp or Power Management operation to a particular driver in a device stack.\r\n
0x70000065 | Startup of the UMDF reflector\r\n
0x70000070 | Performance measurement for installation or update of device drivers.\r\n
0x70000071 | Performance measurement for predevice install phase.\r\n
0x70000072 | Performance measurement for postdevice install phase.\r\n
0x70000073 | Performance measurement for framework update.\r\n
0x70000074 | Testing UMDF\r\n
0x90000001 | Microsoft-Windows-DriverFrameworks-UserMode\r\n
0x90000002 | Operational\r\n
0x90000003 | System\r\n
0xb00103e8 | The Driver Manager service started successfully\r\n
0xb00103e9 | The Driver Manager service failed to start.  The error reported was %2.\r\n
0xb00103ea | The Driver Manager service was stopped\r\n
0xb00103eb | The Driver Manager service is starting a host process for device %3.\r\n
0xb00103ec | The host process (%1) started successfully.\r\n
0xb00103ed | The host process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00103ee | The host process (%1) is being asked to shutdown.\r\n
0xb00103ef | The host process (%1) has a problem (%2) and is being terminated.\r\n
0xb00103f0 | The host process (%1) has been shutdown.\r\n
0xb00107d0 | The UMDF Host Process (%1) is starting up.\r\n
0xb00107d1 | The UMDF Host Process (%1) started successfully.\r\n
0xb00107d2 | The UMDF Host Process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00107d3 | The UMDF Host Process (%1) has been asked to load drivers for device %2.\r\n
0xb00107d4 | The UMDF Host is loading driver %4 at level %3 for device %2.\r\n
0xb00107d5 | The UMDF Host Process (%1) has loaded module %3 while loading drivers for device %2.\r\n
0xb00107d6 | The UMDF Host successfully loaded the driver at level %3.\r\n
0xb00107d7 | The UMDF Host failed to load the driver at level %3.  The error reported was %4.\r\n
0xb00107da | The UMDF Host Process (%1) has successfully loaded drivers for device %2.\r\n
0xb00107db | The UMDF Host Process (%1) has failed to load drivers for device %2.  The error reported was %3\r\n
0xb0010834 | Received a Pnp or Power operation (%3, %4) for device %2.\r\n
0xb0010835 | Completed a Pnp or Power operation (%3, %4) for device %2 with status %9.\r\n
0xb0010836 | Forwarded a finished Pnp or Power operation (%3, %4) to the lower driver for device %2 with status %9.\r\n
0xb0010839 | Forwarded a Pnp or Power operation (%3, %4) for device %2 to the lower driver with status %9\r\n
0xb001083a | Received a Pnp or Power operation (%3, %4) for device %2 which was completed by the lower drivers with status %9\r\n
0xb0010b54 | The UMDF Host (%1) has been asked to shutdown.\r\n
0xb0010b55 | The UMDF Host (%1) has shutdown.\r\n
0xb0010bb8 | UMDF State Machine %4 start processing event %5 (Queueing %6)\r\n
0xb0010bb9 | UMDF State Machine %4 dropped event %5\r\n
0xb0010bc2 | UMDF State Machine %4 state change from %5 to %7 on event %6\r\n
0xb0010bc3 | UMDF State Machine %4 event processing finished in state %5\r\n
0xb0010bcc | UMDF State Machine %4 event processing stopped in state %5\r\n
0xb0014e3e | Power IRP related event in the User-mode Driver Frameworks Host Process\r\n
0xb0017530 | A driver package which uses user-mode driver framework version %2 is being installed on device %1.\r\n
0xb0017531 | The driver package installation has finished. The final status was %1.\r\n
0xb0017532 | PreDevice installation (UMDF version %2) is starting for device %1.\r\n
0xb0017533 | PreDevice installation has finished. The final status was %1.\r\n
0xb0017534 | PostDevice installation (UMDF version %2) is starting for device %1.\r\n
0xb0017535 | PostDevice installation has finished. The final status was %1.\r\n
0xb0017536 | UMDF update has started.\r\n
0xb0017537 | UMDF has been updated. The final status was %1.\r\n
0xd0000001 | QueueToTail\r\n
0xd0000002 | QueueToFront\r\n
0xd0000003 | QueueFull\r\n

### 6.2.9200.16384, 6.3.9600.16384, 6.3.9600.17415

Message identifier | Message string
--- | ---
0x00002710 | A driver package which uses user-mode driver framework version %2 is being installed on device %1.\r\n
0x00002711 | The UMDF service %1 (CLSID %2) was installed.  It requires framework version %3 or higher.\r\n
0x00002712 | The UMDF service %1 (CLSID %2) was upgraded.  It requires framework version %3 or higher.\r\n
0x00002774 | The driver package installation has succeeded.\r\n
0x00002775 | The driver package installation has failed.  The final status was %1.\r\n
0x0000277e | A problem has occurred with one or more user-mode drivers and the hosting process has been terminated.  This may temporarily interrupt your ability to access the devices.\r\n
0x0000277f | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002780 | The device %2 (location %3) is offline due to a user-mode device crash.  Windows will no longer attempt to restart this device because the maximum restart limit has been reached.  Disconnecting the device and reconnecting it, or disabling it and re-enabling it from the device manager, will reset this limit and allow the device to be accessed again.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002781 | The device %2 was unable to start due to conflict between the settings for driver %5 (%3 - %4) and the other drivers.  Windows will not be able to start this device.  Please contact the device manufacturer for assistance.\r\n
0x00002782 | The UMDF reflector was unable to complete startup because the %2 service was not found.  This service may be started later during boot, at which point Windows will attempt to start the device again.\r\n
0x00002783 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002784 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device in the shared process %5 more times before moving the device in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00004e1f | UMDF Test Event (%1)\r\n
0x10000031 | Response Time\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000010 | Startup of the driver manager service.\r\n
0x70000011 | Creation of a new driver host process.\r\n
0x70000012 | Shutdown of a driver host process.\r\n
0x70000020 | Startup of a new driver host process.\r\n
0x70000021 | Loading drivers to control a newly discovered device.\r\n
0x70000025 | Pnp or Power Management operation to a particular device.\r\n
0x70000029 | Shutdown of a driver host process.\r\n
0x70000030 | Installation or update of device drivers.\r\n
0x70000040 | User-mode Driver problems.\r\n
0x70000050 | Pnp or Power Management operation to a particular driver in a device stack.\r\n
0x70000065 | Startup of the UMDF reflector\r\n
0x70000070 | Performance measurement for installation or update of device drivers.\r\n
0x70000071 | Performance measurement for predevice install phase.\r\n
0x70000072 | Performance measurement for postdevice install phase.\r\n
0x70000073 | Performance measurement for framework update.\r\n
0x70000074 | Testing UMDF\r\n
0x70000075 | DDI call to read from Hardware.\r\n
0x70000076 | Read from Hardware.\r\n
0x70000077 | DDI call to Write to hardware.\r\n
0x70000078 | Write to hardware.\r\n
0x70000079 | UMDF hardware interrupt notification.\r\n
0x7000007a | Sqm Task.\r\n
0x90000001 | Microsoft-Windows-DriverFrameworks-UserMode\r\n
0x90000002 | Operational\r\n
0x90000003 | System\r\n
0xb00103e8 | The Driver Manager service started successfully\r\n
0xb00103e9 | The Driver Manager service failed to start.  The error reported was %2.\r\n
0xb00103ea | The Driver Manager service was stopped\r\n
0xb00103eb | The Driver Manager service is starting a host process for device %3.\r\n
0xb00103ec | The host process (%1) started successfully.\r\n
0xb00103ed | The host process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00103ee | The host process (%1) is being asked to shutdown.\r\n
0xb00103ef | The host process (%1) has a problem (%2) and is being terminated.\r\n
0xb00103f0 | The host process (%1) has been shutdown.\r\n
0xb00107d0 | The UMDF Host Process (%1) is starting up.\r\n
0xb00107d1 | The UMDF Host Process (%1) started successfully.\r\n
0xb00107d2 | The UMDF Host Process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00107d3 | The UMDF Host Process (%1) has been asked to load drivers for device %2.\r\n
0xb00107d4 | The UMDF Host is loading driver %4 at level %3 for device %2.\r\n
0xb00107d5 | The UMDF Host Process (%1) has loaded module %3 while loading drivers for device %2.\r\n
0xb00107d6 | The UMDF Host successfully loaded the driver at level %3.\r\n
0xb00107d7 | The UMDF Host failed to load the driver at level %3.  The error reported was %4.\r\n
0xb00107da | The UMDF Host Process (%1) has successfully loaded drivers for device %2.\r\n
0xb00107db | The UMDF Host Process (%1) has failed to load drivers for device %2.  The error reported was %3\r\n
0xb0010834 | Received a Pnp or Power operation (%3, %4) for device %2.\r\n
0xb0010835 | Completed a Pnp or Power operation (%3, %4) for device %2 with status %9.\r\n
0xb0010836 | Forwarded a finished Pnp or Power operation (%3, %4) to the lower driver for device %2 with status %9.\r\n
0xb0010839 | Forwarded a Pnp or Power operation (%3, %4) for device %2 to the lower driver with status %9\r\n
0xb001083a | Received a Pnp or Power operation (%3, %4) for device %2 which was completed by the lower drivers with status %9\r\n
0xb0010b54 | The UMDF Host (%1) has been asked to shutdown.\r\n
0xb0010b55 | The UMDF Host (%1) has shutdown.\r\n
0xb0010bb8 | UMDF State Machine %4 start processing event %5 (Queueing %6)\r\n
0xb0010bb9 | UMDF State Machine %4 dropped event %5\r\n
0xb0010bc2 | UMDF State Machine %4 state change from %5 to %7 on event %6\r\n
0xb0010bc3 | UMDF State Machine %4 event processing finished in state %5\r\n
0xb0010bcc | UMDF State Machine %4 event processing stopped in state %5\r\n
0xb0014e3e | Power IRP related event in the User-mode Driver Frameworks Host Process\r\n
0xb0017530 | A driver package which uses user-mode driver framework version %2 is being installed on device %1.\r\n
0xb0017531 | The driver package installation has finished. The final status was %1.\r\n
0xb0017532 | PreDevice installation (UMDF version %2) is starting for device %1.\r\n
0xb0017533 | PreDevice installation has finished. The final status was %1.\r\n
0xb0017534 | PostDevice installation (UMDF version %2) is starting for device %1.\r\n
0xb0017535 | PostDevice installation has finished. The final status was %1.\r\n
0xb0017536 | UMDF update has started.\r\n
0xb0017537 | UMDF has been updated. The final status was %1.\r\n
0xb0017538 | DDI to read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017539 | DDI to read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753a | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753b | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753c | DDI to write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753d | DDI to write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753e | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753f | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017540 | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017541 | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017542 | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017543 | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017544 | UMDF Reflector sent notification for hardware interrupt (Message ID %1).\r\n
0xb0017545 | UMDF framework received notification for hardware interrupt (Message ID %1).\r\n
0xd0000001 | QueueToTail\r\n
0xd0000002 | QueueToFront\r\n
0xd0000003 | QueueFull\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x00002710 | A driver package which uses user-mode driver framework version %2 is being installed on device %1.\r\n
0x00002711 | The UMDF service %1 (CLSID %2) was installed.  It requires framework version %3 or higher.\r\n
0x00002712 | The UMDF service %1 (CLSID %2) was upgraded.  It requires framework version %3 or higher.\r\n
0x00002774 | The driver package installation has succeeded.\r\n
0x00002775 | The driver package installation has failed.  The final status was %1.\r\n
0x0000277e | A problem has occurred with one or more user-mode drivers and the hosting process has been terminated.  This may temporarily interrupt your ability to access the devices.\r\n
0x0000277f | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002780 | The device %2 (location %3) is offline due to a user-mode device crash.  Windows will no longer attempt to restart this device because the maximum restart limit has been reached.  Disconnecting the device and reconnecting it, or disabling it and re-enabling it from the device manager, will reset this limit and allow the device to be accessed again.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002781 | The device %2 was unable to start due to conflict between the settings for driver %5 (%3 - %4) and the other drivers.  Windows will not be able to start this device.  Please contact the device manufacturer for assistance.\r\n
0x00002782 | %2 (part of UMDF) did not load yet. After it does, Windows will start the device again.\r\n
0x00002783 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002784 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device in the shared process %5 more times before moving the device in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00004e1f | UMDF Test Event (%1)\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000010 | Startup of the driver manager service.\r\n
0x70000011 | Creation of a new driver host process.\r\n
0x70000012 | Shutdown of a driver host process.\r\n
0x70000020 | Startup of a new driver host process.\r\n
0x70000021 | Loading drivers to control a newly discovered device.\r\n
0x70000025 | Pnp or Power Management operation to a particular device.\r\n
0x70000029 | Shutdown of a driver host process.\r\n
0x70000030 | Installation or update of device drivers.\r\n
0x70000040 | User-mode Driver problems.\r\n
0x70000050 | Pnp or Power Management operation to a particular driver in a device stack.\r\n
0x70000065 | Startup of the UMDF reflector\r\n
0x70000074 | Testing UMDF\r\n
0x70000075 | DDI call to read from Hardware.\r\n
0x70000076 | Read from Hardware.\r\n
0x70000077 | DDI call to Write to hardware.\r\n
0x70000078 | Write to hardware.\r\n
0x70000079 | UMDF hardware interrupt notification.\r\n
0x90000001 | Microsoft-Windows-DriverFrameworks-UserMode\r\n
0x90000002 | Operational\r\n
0x90000003 | System\r\n
0xb00103e8 | The Driver Manager service started successfully\r\n
0xb00103e9 | The Driver Manager service failed to start.  The error reported was %2.\r\n
0xb00103ea | The Driver Manager service was stopped\r\n
0xb00103eb | The Driver Manager service is starting a host process for device %3.\r\n
0xb00103ec | The host process (%1) started successfully.\r\n
0xb00103ed | The host process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00103ee | The host process (%1) is being asked to shutdown.\r\n
0xb00103ef | The host process (%1) has a problem (%2) and is being terminated.\r\n
0xb00103f0 | The host process (%1) has been shutdown.\r\n
0xb00107d0 | The UMDF Host Process (%1) is starting up.\r\n
0xb00107d1 | The UMDF Host Process (%1) started successfully.\r\n
0xb00107d2 | The UMDF Host Process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00107d3 | The UMDF Host Process (%1) has been asked to load drivers for device %2.\r\n
0xb00107d4 | The UMDF Host is loading driver %4 at level %3 for device %2.\r\n
0xb00107d5 | The UMDF Host Process (%1) has loaded module %3 while loading drivers for device %2.\r\n
0xb00107d6 | The UMDF Host successfully loaded the driver at level %3.\r\n
0xb00107d7 | The UMDF Host failed to load the driver at level %3.  The error reported was %4.\r\n
0xb00107da | The UMDF Host Process (%1) has successfully loaded drivers for device %2.\r\n
0xb00107db | The UMDF Host Process (%1) has failed to load drivers for device %2.  The error reported was %3\r\n
0xb0010834 | Received a Pnp or Power operation (%3, %4) for device %2.\r\n
0xb0010835 | Completed a Pnp or Power operation (%3, %4) for device %2 with status %9.\r\n
0xb0010836 | Forwarded a finished Pnp or Power operation (%3, %4) to the lower driver for device %2 with status %9.\r\n
0xb0010839 | Forwarded a Pnp or Power operation (%3, %4) for device %2 to the lower driver with status %9\r\n
0xb001083a | Received a Pnp or Power operation (%3, %4) for device %2 which was completed by the lower drivers with status %9\r\n
0xb0010b54 | The UMDF Host (%1) has been asked to shutdown.\r\n
0xb0010b55 | The UMDF Host (%1) has shutdown.\r\n
0xb0010bb8 | UMDF State Machine %4 start processing event %5 (Queueing %6)\r\n
0xb0010bb9 | UMDF State Machine %4 dropped event %5\r\n
0xb0010bc2 | UMDF State Machine %4 state change from %5 to %7 on event %6\r\n
0xb0010bc3 | UMDF State Machine %4 event processing finished in state %5\r\n
0xb0010bcc | UMDF State Machine %4 event processing stopped in state %5\r\n
0xb0014e3e | Power IRP related event in the User-mode Driver Frameworks Host Process\r\n
0xb0017538 | DDI to read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017539 | DDI to read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753a | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753b | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753c | DDI to write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753d | DDI to write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753e | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753f | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017540 | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017541 | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017542 | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017543 | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017544 | UMDF Reflector sent notification for hardware interrupt (Message ID %1).\r\n
0xb0017545 | UMDF framework received notification for hardware interrupt (Message ID %1).\r\n
0xd0000001 | QueueToTail\r\n
0xd0000002 | QueueToFront\r\n
0xd0000003 | QueueFull\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x00002710 | A driver package which uses user-mode driver framework version %2 is being installed on device %1.\r\n
0x00002711 | The UMDF service %1 (CLSID %2) was installed.  It requires framework version %3 or higher.\r\n
0x00002712 | The UMDF service %1 (CLSID %2) was upgraded.  It requires framework version %3 or higher.\r\n
0x00002774 | The driver package installation has succeeded.\r\n
0x00002775 | The driver package installation has failed.  The final status was %1.\r\n
0x0000277e | A problem has occurred with one or more user-mode drivers and the hosting process has been terminated.  This may temporarily interrupt your ability to access the devices.\r\n
0x0000277f | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002780 | The device %2 (location %3) is offline due to a user-mode device crash.  Windows will no longer attempt to restart this device because the maximum restart limit has been reached.  Disconnecting the device and reconnecting it, or disabling it and re-enabling it from the device manager, will reset this limit and allow the device to be accessed again.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002781 | The device %2 was unable to start due to conflict between the settings for driver %5 (%3 - %4) and the other drivers.  Windows will not be able to start this device.  Please contact the device manufacturer for assistance.\r\n
0x00002782 | %2 (part of UMDF) did not load yet. After it does, Windows will start the device again.\r\n
0x00002783 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002784 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device in the shared process %5 more times before moving the device in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002785 | UMDF driver service %1 failed to load because it was compiled using a pre-release version of the Windows Driver Kit(WDK). The driver should be recompiled using a release version of the WDK. Driver's function table count is %2 and the expected count is %3.\r\n
0x00004e1f | UMDF Test Event (%1)\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000010 | Startup of the driver manager service.\r\n
0x70000011 | Creation of a new driver host process.\r\n
0x70000012 | Shutdown of a driver host process.\r\n
0x70000020 | Startup of a new driver host process.\r\n
0x70000021 | Loading drivers to control a newly discovered device.\r\n
0x70000025 | Pnp or Power Management operation to a particular device.\r\n
0x70000029 | Shutdown of a driver host process.\r\n
0x70000030 | Installation or update of device drivers.\r\n
0x70000040 | User-mode Driver problems.\r\n
0x70000050 | Pnp or Power Management operation to a particular driver in a device stack.\r\n
0x70000065 | Startup of the UMDF reflector\r\n
0x70000074 | Testing UMDF\r\n
0x70000075 | DDI call to read from Hardware.\r\n
0x70000076 | Read from Hardware.\r\n
0x70000077 | DDI call to Write to hardware.\r\n
0x70000078 | Write to hardware.\r\n
0x70000079 | UMDF hardware interrupt notification.\r\n
0x90000001 | Microsoft-Windows-DriverFrameworks-UserMode\r\n
0x90000002 | Operational\r\n
0x90000003 | System\r\n
0xb00103e8 | The Driver Manager service started successfully\r\n
0xb00103e9 | The Driver Manager service failed to start.  The error reported was %2.\r\n
0xb00103ea | The Driver Manager service was stopped\r\n
0xb00103eb | The Driver Manager service is starting a host process for device %3.\r\n
0xb00103ec | The host process (%1) started successfully.\r\n
0xb00103ed | The host process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00103ee | The host process (%1) is being asked to shutdown.\r\n
0xb00103ef | The host process (%1) has a problem (%2) and is being terminated.\r\n
0xb00103f0 | The host process (%1) has been shutdown.\r\n
0xb00107d0 | The UMDF Host Process (%1) is starting up.\r\n
0xb00107d1 | The UMDF Host Process (%1) started successfully.\r\n
0xb00107d2 | The UMDF Host Process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00107d3 | The UMDF Host Process (%1) has been asked to load drivers for device %2.\r\n
0xb00107d4 | The UMDF Host is loading driver %4 at level %3 for device %2.\r\n
0xb00107d5 | The UMDF Host Process (%1) has loaded module %3 while loading drivers for device %2.\r\n
0xb00107d6 | The UMDF Host successfully loaded the driver at level %3.\r\n
0xb00107d7 | The UMDF Host failed to load the driver at level %3.  The error reported was %4.\r\n
0xb00107da | The UMDF Host Process (%1) has successfully loaded drivers for device %2.\r\n
0xb00107db | The UMDF Host Process (%1) has failed to load drivers for device %2.  The error reported was %3\r\n
0xb0010834 | Received a Pnp or Power operation (%3, %4) for device %2.\r\n
0xb0010835 | Completed a Pnp or Power operation (%3, %4) for device %2 with status %9.\r\n
0xb0010836 | Forwarded a finished Pnp or Power operation (%3, %4) to the lower driver for device %2 with status %9.\r\n
0xb0010839 | Forwarded a Pnp or Power operation (%3, %4) for device %2 to the lower driver with status %9\r\n
0xb001083a | Received a Pnp or Power operation (%3, %4) for device %2 which was completed by the lower drivers with status %9\r\n
0xb0010b54 | The UMDF Host (%1) has been asked to shutdown.\r\n
0xb0010b55 | The UMDF Host (%1) has shutdown.\r\n
0xb0010bb8 | UMDF State Machine %4 start processing event %5 (Queueing %6)\r\n
0xb0010bb9 | UMDF State Machine %4 dropped event %5\r\n
0xb0010bc2 | UMDF State Machine %4 state change from %5 to %7 on event %6\r\n
0xb0010bc3 | UMDF State Machine %4 event processing finished in state %5\r\n
0xb0010bcc | UMDF State Machine %4 event processing stopped in state %5\r\n
0xb0014e3e | Power IRP related event in the User-mode Driver Frameworks Host Process\r\n
0xb0017538 | DDI to read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017539 | DDI to read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753a | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753b | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753c | DDI to write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753d | DDI to write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753e | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753f | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017540 | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017541 | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017542 | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017543 | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017544 | UMDF Reflector sent notification for hardware interrupt (Message ID %1).\r\n
0xb0017545 | UMDF framework received notification for hardware interrupt (Message ID %1).\r\n
0xd0000001 | QueueToTail\r\n
0xd0000002 | QueueToFront\r\n
0xd0000003 | QueueFull\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x00002710 | A driver package which uses user-mode driver framework version %2 is being installed on device %1.\r\n
0x00002711 | The UMDF service %1 (CLSID %2) was installed.  It requires framework version %3 or higher.\r\n
0x00002712 | The UMDF service %1 (CLSID %2) was upgraded.  It requires framework version %3 or higher.\r\n
0x00002774 | The driver package installation has succeeded.\r\n
0x00002775 | The driver package installation has failed.  The final status was %1.\r\n
0x0000277e | A problem has occurred with one or more user-mode drivers and the hosting process has been terminated.  This may temporarily interrupt your ability to access the devices.\r\n
0x0000277f | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002780 | The device %2 (location %3) is offline due to a user-mode device crash.  Windows will no longer attempt to restart this device because the maximum restart limit has been reached.  Disconnecting the device and reconnecting it, or disabling it and re-enabling it from the device manager, will reset this limit and allow the device to be accessed again.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002781 | The device %2 was unable to start due to conflict between the settings for driver %5 (%3 - %4) and the other drivers.  Windows will not be able to start this device.  Please contact the device manufacturer for assistance.\r\n
0x00002782 | %2 (part of UMDF) did not load yet. After it does, Windows will start the device again.\r\n
0x00002783 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002784 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device in the shared process %5 more times before moving the device in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002785 | UMDF driver service %1 failed to load because it was compiled using a pre-release version of the Windows Driver Kit(WDK). The driver should be recompiled using a release version of the WDK. Driver's function table count is %2 and the expected count is %3.\r\n
0x00004e1f | UMDF Test Event (%1)\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000010 | Startup of the driver manager service.\r\n
0x70000011 | Creation of a new driver host process.\r\n
0x70000012 | Shutdown of a driver host process.\r\n
0x70000020 | Startup of a new driver host process.\r\n
0x70000021 | Loading drivers to control a newly discovered device.\r\n
0x70000025 | Pnp or Power Management operation to a particular device.\r\n
0x70000029 | Shutdown of a driver host process.\r\n
0x70000030 | Installation or update of device drivers.\r\n
0x70000040 | User-mode Driver problems.\r\n
0x70000050 | Pnp or Power Management operation to a particular driver in a device stack.\r\n
0x70000065 | Startup of the UMDF reflector\r\n
0x70000074 | Testing UMDF\r\n
0x70000075 | DDI call to read from Hardware.\r\n
0x70000076 | Read from Hardware.\r\n
0x70000077 | DDI call to Write to hardware.\r\n
0x70000078 | Write to hardware.\r\n
0x70000079 | UMDF hardware interrupt notification.\r\n
0x90000001 | Microsoft-Windows-DriverFrameworks-UserMode\r\n
0x90000002 | Operational\r\n
0x90000003 | System\r\n
0xb00103e8 | The Driver Manager service started successfully\r\n
0xb00103e9 | The Driver Manager service failed to start.  The error reported was %2.\r\n
0xb00103ea | The Driver Manager service was stopped\r\n
0xb00103eb | The Driver Manager service is starting a host process for device %3.\r\n
0xb00103ec | The host process (%1) started successfully.\r\n
0xb00103ed | The host process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00103ee | The host process (%1) is being asked to shutdown.\r\n
0xb00103ef | The host process (%1) has a problem (%2) and is being terminated.\r\n
0xb00103f0 | The host process (%1) has been shutdown.\r\n
0xb00107d0 | The UMDF Host Process (%1) is starting up.\r\n
0xb00107d1 | The UMDF Host Process (%1) started successfully.\r\n
0xb00107d2 | The UMDF Host Process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00107d3 | The UMDF Host Process (%1) has been asked to load drivers for device %2.\r\n
0xb00107d4 | The UMDF Host is loading driver %4 at level %3 for device %2.\r\n
0xb00107d5 | The UMDF Host Process (%1) has loaded module %3 while loading drivers for device %2.\r\n
0xb00107d6 | The UMDF Host successfully loaded the driver at level %3.\r\n
0xb00107d7 | The UMDF Host failed to load the driver at level %3.  The error reported was %4.\r\n
0xb00107da | The UMDF Host Process (%1) has successfully loaded drivers for device %2.\r\n
0xb00107db | The UMDF Host Process (%1) has failed to load drivers for device %2.  The error reported was %3\r\n
0xb0010834 | Received a Pnp or Power operation (%3, %4) for device %2.\r\n
0xb0010835 | Completed a Pnp or Power operation (%3, %4) for device %2 with status %9.\r\n
0xb0010836 | Forwarded a finished Pnp or Power operation (%3, %4) to the lower driver for device %2 with status %9.\r\n
0xb0010839 | Forwarded a Pnp or Power operation (%3, %4) for device %2 to the lower driver with status %9\r\n
0xb001083a | Received a Pnp or Power operation (%3, %4) for device %2 which was completed by the lower drivers with status %9\r\n
0xb0010b54 | The UMDF Host (%1) has been asked to shutdown.\r\n
0xb0010b55 | The UMDF Host (%1) has shutdown.\r\n
0xb0010bb8 | UMDF State Machine %4 start processing event %5 (Queueing %6)\r\n
0xb0010bb9 | UMDF State Machine %4 dropped event %5\r\n
0xb0010bc2 | UMDF State Machine %4 state change from %5 to %7 on event %6\r\n
0xb0010bc3 | UMDF State Machine %4 event processing finished in state %5\r\n
0xb0010bcc | UMDF State Machine %4 event processing stopped in state %5\r\n
0xb0014e3e | Power IRP related event in the User-mode Driver Frameworks Host Process\r\n
0xb0017538 | DDI to read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017539 | DDI to read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753a | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753b | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753c | DDI to write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753d | DDI to write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753e | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753f | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017540 | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017541 | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017542 | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017543 | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017544 | UMDF Reflector sent notification for hardware interrupt (Message ID %1).\r\n
0xb0017545 | UMDF framework received notification for hardware interrupt (Message ID %1).\r\n
0xb00203e9 | The Driver Manager service failed to start.  The error reported was %1.\r\n
0xd0000001 | QueueToTail\r\n
0xd0000002 | QueueToFront\r\n
0xd0000003 | QueueFull\r\n

### 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x00002710 | A driver package which uses user-mode driver framework version %2 is being installed on device %1.\r\n
0x00002711 | The UMDF service %1 (CLSID %2) was installed.  It requires framework version %3 or higher.\r\n
0x00002712 | The UMDF service %1 (CLSID %2) was upgraded.  It requires framework version %3 or higher.\r\n
0x00002774 | The driver package installation has succeeded.\r\n
0x00002775 | The driver package installation has failed.  The final status was %1.\r\n
0x0000277e | A problem has occurred with one or more user-mode drivers and the hosting process has been terminated.  This may temporarily interrupt your ability to access the devices.\r\n
0x0000277f | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002780 | The device %2 (location %3) is offline due to a user-mode device crash.  Windows will no longer attempt to restart this device because the maximum restart limit has been reached.  Disconnecting the device and reconnecting it, or disabling it and re-enabling it from the device manager, will reset this limit and allow the device to be accessed again.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002781 | The device %2 was unable to start due to conflict between the settings for driver %5 (%3 - %4) and the other drivers.  Windows will not be able to start this device.  Please contact the device manufacturer for assistance.\r\n
0x00002783 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device %5 more times in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002784 | The device %2 (location %3) is offline due to a user-mode driver crash.  Windows will attempt to restart the device in the shared process %5 more times before moving the device in its own process.  Please contact the device manufacturer for more information about this problem.\r\n
0x00002785 | UMDF driver service %1 failed to load because it was compiled using a pre-release version of the Windows Driver Kit(WDK). The driver should be recompiled using a release version of the WDK. Driver's function table count is %2 and the expected count is %3.\r\n
0x00002786 | UMDF reflector is unable to connect to service control manager (SCM). This is expected during boot, when SCM has not started yet. Will retry when it starts.\r\n
0x00004e1f | UMDF Test Event (%1)\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000001 | Critical\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000010 | Startup of the driver manager service.\r\n
0x70000011 | Creation of a new driver host process.\r\n
0x70000012 | Shutdown of a driver host process.\r\n
0x70000020 | Startup of a new driver host process.\r\n
0x70000021 | Loading drivers to control a newly discovered device.\r\n
0x70000025 | Pnp or Power Management operation to a particular device.\r\n
0x70000029 | Shutdown of a driver host process.\r\n
0x70000030 | Installation or update of device drivers.\r\n
0x70000040 | User-mode Driver problems.\r\n
0x70000050 | Pnp or Power Management operation to a particular driver in a device stack.\r\n
0x70000065 | Startup of the UMDF reflector\r\n
0x70000074 | Testing UMDF\r\n
0x70000075 | DDI call to read from Hardware.\r\n
0x70000076 | Read from Hardware.\r\n
0x70000077 | DDI call to Write to hardware.\r\n
0x70000078 | Write to hardware.\r\n
0x70000079 | UMDF hardware interrupt notification.\r\n
0x90000001 | Microsoft-Windows-DriverFrameworks-UserMode\r\n
0x90000002 | Operational\r\n
0x90000003 | System\r\n
0xb00103e8 | The Driver Manager service started successfully\r\n
0xb00103e9 | The Driver Manager service failed to start.  The error reported was %2.\r\n
0xb00103ea | The Driver Manager service was stopped\r\n
0xb00103eb | The Driver Manager service is starting a host process for device %3.\r\n
0xb00103ec | The host process (%1) started successfully.\r\n
0xb00103ed | The host process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00103ee | The host process (%1) is being asked to shutdown.\r\n
0xb00103ef | The host process (%1) has a problem (%2) and is being terminated.\r\n
0xb00103f0 | The host process (%1) has been shutdown.\r\n
0xb00107d0 | The UMDF Host Process (%1) is starting up.\r\n
0xb00107d1 | The UMDF Host Process (%1) started successfully.\r\n
0xb00107d2 | The UMDF Host Process (%1) failed to start successfully.  The error reported was %2.\r\n
0xb00107d3 | The UMDF Host Process (%1) has been asked to load drivers for device %2.\r\n
0xb00107d4 | The UMDF Host is loading driver %4 at level %3 for device %2.\r\n
0xb00107d5 | The UMDF Host Process (%1) has loaded module %3 while loading drivers for device %2.\r\n
0xb00107d6 | The UMDF Host successfully loaded the driver at level %3.\r\n
0xb00107d7 | The UMDF Host failed to load the driver at level %3.  The error reported was %4.\r\n
0xb00107da | The UMDF Host Process (%1) has successfully loaded drivers for device %2.\r\n
0xb00107db | The UMDF Host Process (%1) has failed to load drivers for device %2.  The error reported was %3\r\n
0xb0010834 | Received a Pnp or Power operation (%3, %4) for device %2.\r\n
0xb0010835 | Completed a Pnp or Power operation (%3, %4) for device %2 with status %9.\r\n
0xb0010836 | Forwarded a finished Pnp or Power operation (%3, %4) to the lower driver for device %2 with status %9.\r\n
0xb0010839 | Forwarded a Pnp or Power operation (%3, %4) for device %2 to the lower driver with status %9\r\n
0xb001083a | Received a Pnp or Power operation (%3, %4) for device %2 which was completed by the lower drivers with status %9\r\n
0xb0010b54 | The UMDF Host (%1) has been asked to shutdown.\r\n
0xb0010b55 | The UMDF Host (%1) has shutdown.\r\n
0xb0010bb8 | UMDF State Machine %4 start processing event %5 (Queueing %6)\r\n
0xb0010bb9 | UMDF State Machine %4 dropped event %5\r\n
0xb0010bc2 | UMDF State Machine %4 state change from %5 to %7 on event %6\r\n
0xb0010bc3 | UMDF State Machine %4 event processing finished in state %5\r\n
0xb0010bcc | UMDF State Machine %4 event processing stopped in state %5\r\n
0xb0014e3e | Power IRP related event in the User-mode Driver Frameworks Host Process\r\n
0xb0017538 | DDI to read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017539 | DDI to read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753a | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753b | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753c | DDI to write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753d | DDI to write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753e | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb001753f | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017540 | Read from hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017541 | Read from hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017542 | Write to hardware begins (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017543 | Write to hardware ends (TargetType: %1, TargetSize: %2, BufferCount: %3).\r\n
0xb0017544 | UMDF Reflector sent notification for hardware interrupt (Message ID %1).\r\n
0xb0017545 | UMDF framework received notification for hardware interrupt (Message ID %1).\r\n
0xb00203e9 | The Driver Manager service failed to start.  The error reported was %1.\r\n
0xd0000001 | QueueToTail\r\n
0xd0000002 | QueueToFront\r\n
0xd0000003 | QueueFull\r\n
