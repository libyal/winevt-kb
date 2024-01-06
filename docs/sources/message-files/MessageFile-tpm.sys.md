## tpm.sys

Path: %SystemRoot%\System32\drivers\tpm.sys

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00000015 | A standard user issued Trusted Platform Module (TPM) command returned an authorization failure. This event is generated when a command sent to the TPM by a standard user returns a response indicating an authorization failure.  If too many authorization failures occur, standard users may be temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1. %nProcess Path %2.\r\n
0x00000017 | A standard user Trusted Platform Module (TPM) command was blocked because the standard user has exceeded the maximum authorization failures permitted. This event is generated when too many recent TPM commands sent to the TPM by a standard user returned a response indicating an authorization failure.  The standard user is currently temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1.\r\n
0x10000038 | Classic\r\n
0x40060011 | The Trusted Platform Module (TPM) hardware failed to execute a TPM command.\r\n
0x40060012 | This event triggers the Trusted Platform Module (TPM) provisioning/status check to run.\r\n
0x40060014 | A command was sent to the Trusted Platform Module (TPM) successfully resetting the TPM lockout logic. This event is generated when a successful command sent to the TPM resets the TPM lockout logic.  With this event, all prior standard user TPM authorization failures are ignored; allowing standard users to use the TPM normally again immediately.\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | TPM\r\n
0x90000002 | System\r\n
0xc0060002 | The TPM self test command failed.\r\n
0xc006000c | The device driver for the Trusted Platform Module (TPM) encountered an error in the TPM hardware, which might prevent some applications using TPM services from operating correctly.  Please restart your computer to reset the TPM hardware.  For further assistance on this hardware issue, please contact the computer manufacturer for more information.\r\n
0xc006000e | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0xc006000f | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0xc0060010 | A compatible TPM is not found.\r\n
0xc0060013 | The system firmware failed to enable overwriting of system memory on restart. The ACPI request could not be interpreted by the firmware. The firmware should be upgraded.\r\n
0xc0060016 | TPM Base Services (TBS) has been configured in a test mode until the next full restart. The TBS will not perform TPM resource virtualization or TPM command blocking until the next full restart.\r\n

### 6.3.9600.16384, 6.3.9600.18065, 10.0.10586.0, 10.0.14393.0, 10.0.14393.206

Message identifier | Message string
--- | ---
0x00000002 | The TPM self test command failed.\r\n
0x0000000c | The device driver for the Trusted Platform Module (TPM) encountered an error in the TPM hardware, which might prevent some applications using TPM services from operating correctly.  Please restart your computer to reset the TPM hardware.  For further assistance on this hardware issue, please contact the computer manufacturer for more information.\r\n
0x0000000e | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0x0000000f | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0x00000010 | A compatible TPM is not found.\r\n
0x00000011 | The Trusted Platform Module (TPM) hardware failed to execute a TPM command.\r\n
0x00000012 | This event triggers the Trusted Platform Module (TPM) provisioning/status check to run.\r\n
0x00000013 | The system firmware failed to enable overwriting of system memory on restart. The ACPI request could not be interpreted by the firmware. The firmware should be upgraded.\r\n
0x00000014 | A command was sent to the Trusted Platform Module (TPM) successfully resetting the TPM lockout logic. This event is generated when a successful command sent to the TPM resets the TPM lockout logic.  With this event, all prior standard user TPM authorization failures are ignored; allowing standard users to use the TPM normally again immediately.\r\n
0x00000015 | A standard user issued Trusted Platform Module (TPM) command returned an authorization failure. This event is generated when a command sent to the TPM by a standard user returns a response indicating an authorization failure.  If too many authorization failures occur, standard users may be temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1. %nProcess Path %2.\r\n
0x00000016 | TPM Base Services (TBS) has been configured in a test mode until the next full restart. The TBS will not perform TPM resource virtualization or TPM command blocking until the next full restart.\r\n
0x00000017 | A standard user Trusted Platform Module (TPM) command was blocked because the standard user has exceeded the maximum authorization failures permitted. This event is generated when too many recent TPM commands sent to the TPM by a standard user returned a response indicating an authorization failure.  The standard user is currently temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1.\r\n
0x00000018 | The Trusted Platform Module (TPM) status: %1 and %2.\r\n
0x00000019 | Creation of the Windows AIK directory failed.\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | TPM\r\n
0x90000002 | System\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | Inactive\r\n
0xd0000004 | Active\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x00000002 | The TPM self test command failed.\r\n
0x0000000c | The device driver for the Trusted Platform Module (TPM) encountered an error in the TPM hardware, which might prevent some applications using TPM services from operating correctly.  Please restart your computer to reset the TPM hardware.  For further assistance on this hardware issue, please contact the computer manufacturer for more information.\r\n
0x0000000e | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0x0000000f | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0x00000010 | A compatible TPM is not found.\r\n
0x00000011 | The Trusted Platform Module (TPM) hardware failed to execute a TPM command.\r\n
0x00000012 | This event triggers the Trusted Platform Module (TPM) provisioning/status check to run.\r\n
0x00000013 | The system firmware failed to enable overwriting of system memory on restart. The ACPI request could not be interpreted by the firmware. The firmware should be upgraded.\r\n
0x00000014 | A command was sent to the Trusted Platform Module (TPM) successfully resetting the TPM lockout logic. This event is generated when a successful command sent to the TPM resets the TPM lockout logic.  With this event, all prior standard user TPM authorization failures are ignored; allowing standard users to use the TPM normally again immediately.\r\n
0x00000015 | A standard user issued Trusted Platform Module (TPM) command returned an authorization failure. This event is generated when a command sent to the TPM by a standard user returns a response indicating an authorization failure.  If too many authorization failures occur, standard users may be temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1. %nProcess Path %2.\r\n
0x00000016 | TPM Base Services (TBS) has been configured in a test mode until the next full restart. The TBS will not perform TPM resource virtualization or TPM command blocking until the next full restart.\r\n
0x00000017 | A standard user Trusted Platform Module (TPM) command was blocked because the standard user has exceeded the maximum authorization failures permitted. This event is generated when too many recent TPM commands sent to the TPM by a standard user returned a response indicating an authorization failure.  The standard user is currently temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1.\r\n
0x00000018 | The Trusted Platform Module (TPM) status: %1 and %2.\r\n
0x00000019 | Creation of the Windows AIK directory failed.\r\n
0x0000001a | Creation of provisioning event has failed.\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | TPM\r\n
0x90000002 | System\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | Inactive\r\n
0xd0000004 | Active\r\n

### 10.0.16299.15, 10.0.17134.254, 10.0.17763.1, 10.0.18362.1, 10.0.18362.815, 10.0.19041.1, 10.0.19041.488

Message identifier | Message string
--- | ---
0x00000002 | The TPM self test command failed.\r\n
0x0000000c | The device driver for the Trusted Platform Module (TPM) encountered an error in the TPM hardware, which might prevent some applications using TPM services from operating correctly.  Please restart your computer to reset the TPM hardware.  For further assistance on this hardware issue, please contact the computer manufacturer for more information.\r\n
0x0000000e | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0x0000000f | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0x00000010 | A compatible TPM is not found.\r\n
0x00000011 | The Trusted Platform Module (TPM) hardware failed to execute a TPM command.\r\n
0x00000012 | This event triggers the Trusted Platform Module (TPM) provisioning/status check to run.\r\n
0x00000013 | The system firmware failed to enable overwriting of system memory on restart. The ACPI request could not be interpreted by the firmware. The firmware should be upgraded.\r\n
0x00000014 | A command was sent to the Trusted Platform Module (TPM) successfully resetting the TPM lockout logic. This event is generated when a successful command sent to the TPM resets the TPM lockout logic.  With this event, all prior standard user TPM authorization failures are ignored; allowing standard users to use the TPM normally again immediately.\r\n
0x00000015 | A standard user issued Trusted Platform Module (TPM) command returned an authorization failure. This event is generated when a command sent to the TPM by a standard user returns a response indicating an authorization failure.  If too many authorization failures occur, standard users may be temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1. %nProcess Path %2.\r\n
0x00000016 | TPM Base Services (TBS) has been configured in a test mode until the next full restart. The TBS will not perform TPM resource virtualization or TPM command blocking until the next full restart.\r\n
0x00000017 | A standard user Trusted Platform Module (TPM) command was blocked because the standard user has exceeded the maximum authorization failures permitted. This event is generated when too many recent TPM commands sent to the TPM by a standard user returned a response indicating an authorization failure.  The standard user is currently temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1.\r\n
0x00000018 | The Trusted Platform Module (TPM) status: %1 and %2.\r\n
0x00000019 | Creation of the Windows AIK directory failed.\r\n
0x0000001a | Creation of provisioning event has failed.\r\n
0x0000001b | The initialization of the Trusted Platform Module (TPM) failed. The TPM may be in failure mode. To allow diagnosis, contact the TPM manufacturer with the attached information.\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x90000001 | TPM\r\n
0x90000002 | System\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | Inactive\r\n
0xd0000004 | Active\r\n

### 10.0.22000.120

Message identifier | Message string
--- | ---
0x00000002 | The TPM self test command failed.\r\n
0x0000000c | The device driver for the Trusted Platform Module (TPM) encountered an error in the TPM hardware, which might prevent some applications using TPM services from operating correctly.  Please restart your computer to reset the TPM hardware.  For further assistance on this hardware issue, please contact the computer manufacturer for more information.\r\n
0x0000000e | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0x0000000f | The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.\r\n
0x00000010 | A compatible TPM is not found.\r\n
0x00000011 | The Trusted Platform Module (TPM) hardware failed to execute a TPM command.\r\n
0x00000012 | This event triggers the Trusted Platform Module (TPM) provisioning/status check to run.\r\n
0x00000013 | The system firmware failed to enable overwriting of system memory on restart. The ACPI request could not be interpreted by the firmware. The firmware should be upgraded.\r\n
0x00000014 | A command was sent to the Trusted Platform Module (TPM) successfully resetting the TPM lockout logic. This event is generated when a successful command sent to the TPM resets the TPM lockout logic.  With this event, all prior standard user TPM authorization failures are ignored; allowing standard users to use the TPM normally again immediately.\r\n
0x00000015 | A standard user issued Trusted Platform Module (TPM) command returned an authorization failure. This event is generated when a command sent to the TPM by a standard user returns a response indicating an authorization failure.  If too many authorization failures occur, standard users may be temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1. %nProcess Path %2.\r\n
0x00000016 | TPM Base Services (TBS) has been configured in a test mode until the next full restart. The TBS will not perform TPM resource virtualization or TPM command blocking until the next full restart.\r\n
0x00000017 | A standard user Trusted Platform Module (TPM) command was blocked because the standard user has exceeded the maximum authorization failures permitted. This event is generated when too many recent TPM commands sent to the TPM by a standard user returned a response indicating an authorization failure.  The standard user is currently temporarily prevented from sending TPM commands requiring authorization.  This helps prevent the TPM from entering a hardware lockout because of too many authorization failures. %nUser Security ID:%1.\r\n
0x00000018 | The Trusted Platform Module (TPM) status: %1 and %2.\r\n
0x00000019 | Creation of the Windows AIK directory failed.\r\n
0x0000001a | Creation of provisioning event has failed.\r\n
0x0000001b | The initialization of the Trusted Platform Module (TPM) failed. The TPM may be in failure mode. To allow diagnosis, contact the TPM manufacturer with the attached information.\r\n
0x0000001c | Information about the Storage Root Key creation.\r\n
0x0000001d | Creation of the Storage Root Key failed.\r\n
0x0000001e | Reset and/or resume count do not match expected values after hibernate/resume.\r\n
0x0000001f | Information about Kernel Soft Reboot.\r\n
0x00000020 | Encountered an error calling TpmApi.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | TPM\r\n
0x90000002 | System\r\n
0xd0000001 | Disabled\r\n
0xd0000002 | Enabled\r\n
0xd0000003 | Inactive\r\n
0xd0000004 | Active\r\n
