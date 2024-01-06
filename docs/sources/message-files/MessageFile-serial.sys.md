## serial.sys

Path: %SystemRoot%\System32\drivers\serial.sys

### 5.0.2195.6655, 5.1.2600.5512, 5.2.3790.1830, 5.2.3790.3959, 6.0.6000.16386, 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384, 6.3.9600.18437, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x40060001 | The kernel debugger is already using %2.\r\n
0x40060002 | While validating that %2 was really a serial port, a fifo was detected. The fifo will be used.\r\n
0x40060003 | User configuration data for parameter %2 overriding firmware configuration data.\r\n
0x40060022 | Disabling %2 as requested by the configuration data.\r\n
0x80060004 | Unable to create the symbolic link for %2.\r\n
0x80060005 | Unable to create the device map entry for %2.\r\n
0x80060006 | Unable to delete the device map entry for %2.\r\n
0x8006002a | There is a serial mouse using the same interrupt as %2.  Therefore, %2 will not be started.\r\n
0x8006002b | There was a serial mouse found on %2.  Therefore, %2 will be assigned to the mouse.\r\n
0xc0060007 | Another driver on the system, which did not report its resources, has already claimed the interrupt used by %2.\r\n
0xc0060008 | Not enough resources were available for the driver.\r\n
0xc0060009 | The baud clock rate configuration is not supported on device %2.\r\n
0xc006000a | The hardware locations for %2 could not be translated to something the memory management system could understand.\r\n
0xc006000b | The hardware resources for %2 are already in use by another device.\r\n
0xc006000c | No memory could be allocated in which to place new data for %2.\r\n
0xc006000d | While validating that %2 was really a serial port, the interrupt enable register contained enabled bits in a must be zero bitfield.\r\nThe device is assumed not to be a serial port and will be deleted.\r\n
0xc006000e | While validating that %2 was really a serial port, the modem control register contained enabled bits in a must be zero bitfield.\r\nThe device is assumed not to be a serial port and will be deleted.\r\n
0xc006000f | While validating that %2 was really a serial port, the interrupt id register contained enabled bits in a must be zero bitfield.\r\nThe device is assumed not to be a serial port and will be deleted.\r\n
0xc0060010 | While validating that %2 was really a serial port, the baud rate register could not be set consistantly.\r\nThe device is assumed not to be a serial port and will be deleted.\r\n
0xc0060011 | Some firmware configuration information was incomplete.\r\n
0xc0060012 | No Parameters subkey was found for user defined data.  This is odd, and it also means no user configuration can be found.\r\n
0xc0060013 | Specific user configuration data is unretrievable.\r\n
0xc0060014 | On parameter %2 which indicates a multiport card, must have a port index specified greater than 0.\r\n
0xc0060015 | On parameter %2 which indicates a multiport card, the port index for the multiport card is too large.\r\n
0xc0060016 | The bus type for %2 is not recognizable.\r\n
0xc0060017 | The bus type for %2 is not available on this computer.\r\n
0xc0060018 | The bus specified for %2 does not support the specified method of interrupt.\r\n
0xc0060019 | User configuration for parameter %2 must have %3.\r\n
0xc006001a | The user specified port for %2 is way too high in physical memory.\r\n
0xc006001b | The status port for %2 is way too high in physical memory.\r\n
0xc006001c | The status port for %2 overlaps the control registers for the device.\r\n
0xc006001d | The control registers for %2 overlaps with the %3 control registers.\r\n
0xc006001e | The status register for %2 overlaps the %3 control registers.\r\n
0xc006001f | The status register for %2 overlaps with the %3 status register.\r\n
0xc0060020 | The control registers for %2 overlaps the %3 status register.\r\n
0xc0060021 | Two ports, %2 and %3, on a single multiport card can't have two different interrupts.\r\n
0xc0060023 | Parameter %2 data is unretrievable from the registry.\r\n
0xc0060024 | While validating that %2 was really a serial port, the contents of the divisor latch register was identical to the interrupt enable and the receive registers.\r\nThe device is assumed not to be a serial port and will be deleted.\r\n
0xc0060025 | Could not translate the user reported I/O port for %2.\r\n
0xc0060026 | Could not get the user reported interrupt for %2 from the HAL.\r\n
0xc0060027 | Could not translate the user reported Interrupt Status Register for %2.\r\n
0xc0060028 | Could not report the discovered legacy device %2 to the IO subsystem.\r\n
0xc0060029 | Error writing to the registry.\r\n
0xc006002c | Could not report device %2 to IO subsystem due to a resource conflict.\r\n
0xc006002d | The serial driver detected a hardware failure on device %2 and will disable this device.\r\n
